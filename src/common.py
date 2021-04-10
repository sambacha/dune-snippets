import pandas as pd
import json
import re
import numpy as np
import glob


class EmptySolutionError(Exception):
    pass


def get_max_xrate(o):
    if o["isSellOrder"]:
        return o["maxSellAmount"] / o["minBuyAmount"]
    else:
        return o["maxBuyAmount"] / o["maxSellAmount"]


def compute_avg_eth_price_usd(orders):
    return sum(
        [o["sellTokenDailyPriceUSD"] for o in orders if o["sellToken"] == "WETH"]
        + [o["buyTokenDailyPriceUSD"] for o in orders if o["buyToken"] == "WETH"]
    ) / len([o for o in orders if "WETH" in {o["sellToken"], o["buyToken"]}])


# O(n) iterator that for every element A in the first iterable returns
# the largest element B on the second iterable that satisfies test.
# Assumes that both lists are sorted.
# Example: for this input
# 1 2 4 5 9
# 1 3 6 10
# test(a,b) = a >= b
# returns:
# 1 1 3 3 6
def get_largest_element_sequence(a, b, test):
    idx_b = 0
    for idx_a in range(len(a)):
        while idx_b < len(b) - 1 and test(a[idx_a], b[idx_b + 1]):
            idx_b += 1
        if not test(a[idx_a], b[idx_b]):
            raise ValueError("Found no element satisfying test.")
        yield b[idx_b]


def load_block_data_file_to_df(fname):
    with open(fname, "r") as f:
        d = json.load(f)
    eth_price_usd = compute_avg_eth_price_usd(d["orders"])
    d = [
        {
            "block": o["uniswap"]["block"],
            "index": o["uniswap"]["index"],
            "sell_token": o["sellToken"],
            "buy_token": o["buyToken"],
            "max_buy_amount": o["maxBuyAmount"] if not o["isSellOrder"] else None,
            "max_sell_amount": o["maxSellAmount"] if o["isSellOrder"] else None,
            "sell_token_price_eth": o["sellTokenPriceETH"],
            "buy_token_price_eth": o["buyTokenPriceETH"],
            "sell_token_price_usd": o["sellTokenPriceETH"] * eth_price_usd,
            "buy_token_price_usd": o["buyTokenPriceETH"] * eth_price_usd,
            "timestamp": o["uniswap"]["timestamp"],
            "exec_sell_amount": o["uniswap"]["amounts"][0],
            "exec_buy_amount": o["uniswap"]["amounts"][-1],
            "nr_pools": len(o["uniswap"]["amounts"]) - 1,
            "is_sell_order": o["isSellOrder"],
            "address": o["address"],
            "sell_reserve": float(o["uniswap"]["balancesSellToken"][0]),
            "buy_reserve": float(o["uniswap"]["balancesBuyToken"][-1]),
            #'max_xrate': get_max_xrate(o)
        }
        for o in d["orders"]
    ]
    df = pd.DataFrame.from_records(d)
    df["xrate"] = df.exec_sell_amount / df.exec_buy_amount
    df["block_index"] = df.apply(
        lambda r: "_".join(r[["block", "index"]].astype(str).values), axis=1
    )
    df["token_pair"] = df.apply(
        lambda r: "-".join(sorted([r["sell_token"], r["buy_token"]])), axis=1
    )
    df["exec_vol"] = df.exec_sell_amount * df.sell_token_price_usd
    df["max_vol_usd"] = df.apply(
        lambda r: r.max_sell_amount * r.sell_token_price_usd
        if r.is_sell_order
        else r.max_buy_amount * r.buy_token_price_usd,
        axis=1,
    )
    df["max_vol_eth"] = df.apply(
        lambda r: r.max_sell_amount * r.sell_token_price_eth
        if r.is_sell_order
        else r.max_buy_amount * r.buy_token_price_eth,
        axis=1,
    )

    return df.set_index("block_index")


def remove_most_active_users(df_exec, fraction_to_remove):
    nr_addresses = df_exec.address.nunique()
    addresses = (
        df_exec.address.value_counts()
        .iloc[round(nr_addresses * fraction_to_remove) :]
        .index
    )
    return df_exec[df_exec.address.isin(addresses)]


def load_solver_solution(fname):
    with open(fname, "r") as f:
        d = json.load(f)
    d = [
        {
            "block": int(oid.split("-")[0]),
            "index": int(oid.split("-")[1]),
            "sell_token": o["sell_token"],
            "buy_token": o["buy_token"],
            "exec_sell_amount": int(o["exec_sell_amount"]) * 1e-18,
            "exec_buy_amount": int(o["exec_buy_amount"]) * 1e-18,
            "is_sell_order": o["is_sell_order"],
        }
        for oid, o in d["orders"].items()
    ]
    if len(d) == 0:
        raise EmptySolutionError()
    df = pd.DataFrame.from_records(d)
    df["xrate"] = df.exec_sell_amount / df.exec_buy_amount
    df["block_index"] = df.apply(
        lambda r: "_".join(r[["block", "index"]].astype(str).values), axis=1
    )
    return df.set_index("block_index")


def merge_exec_and_solved(fname, df_exec, from_timestamp, to_timestamp):
    df_sol = load_solver_solution(fname)
    df = df_exec[
        (df_exec.timestamp >= from_timestamp) & (df_exec.timestamp <= to_timestamp)
    ].merge(
        df_sol[["exec_sell_amount", "exec_buy_amount", "xrate"]],
        how="inner",
        on="block_index",
        suffixes=("_uni", "_gp"),
    )
    df["batch_start_time"] = from_timestamp
    df["batch_end_time"] = to_timestamp
    df["surplus"] = df.xrate_uni / df.xrate_gp
    savings_buy = df.exec_buy_amount_gp - df.exec_buy_amount_uni
    savings_sell = df.exec_sell_amount_uni - df.exec_sell_amount_gp
    df["savings_vol_usd"] = (
        savings_buy * df["buy_token_price_usd"]
        + savings_sell * df["sell_token_price_usd"]
    )
    return df


def create_batch_table(solution_fname, df_exec):
    m = re.search(r"_([0-9]+)\-([0-9]+)(\-[0-9]+)*\.json$", solution_fname)
    from_timestamp, to_timestamp = int(m[1]), int(m[2])
    return merge_exec_and_solved(solution_fname, df_exec, from_timestamp, to_timestamp)


def compute_savings_per_token(df):
    savings_buy_per_token = df.groupby("buy_token").savings_buy.sum()
    savings_sell_per_token = df.groupby("sell_token").savings_sell.sum()
    return savings_buy_per_token.add(savings_sell_per_token, fill_value=0)


def compute_mean_gp_rel_surplus(df):
    return np.exp(np.mean(np.log(df.xrate_uni) - np.log(df.xrate_gp)))


def create_batches_table(solution_dir, df_exec):
    dfs = []
    for fname in glob.glob(f"{solution_dir}/*.json"):
        try:
            dfs.append(create_batch_table(fname, df_exec))
        except EmptySolutionError:
            pass
    return pd.concat(dfs, axis=0).sort_index()


def compute_orig_batch(batchdf, df_exec):
    batch_start_time = batchdf.batch_start_time.iloc[0]
    batch_end_time = batchdf.batch_end_time.iloc[0]
    return df_exec[
        (df_exec.timestamp >= batch_start_time) & (df_exec.timestamp <= batch_end_time)
    ]


def compute_orig_batch_size(batchdf, df_exec):
    batch_start_time = batchdf.batch_start_time.iloc[0]
    batch_end_time = batchdf.batch_end_time.iloc[0]
    return (
        (df_exec.timestamp >= batch_start_time) & (df_exec.timestamp <= batch_end_time)
    ).sum()


def remove_batches_not_fully_executed(df_sol, df_exec):
    problem_batch_sizes = df_sol.groupby(["batch_start_time", "batch_end_time"]).apply(
        compute_orig_batch_size, df_exec=df_exec
    )
    solution_batch_sizes = (
        df_sol.groupby(["batch_start_time", "batch_end_time"]).count().block
    )
    batch_start_times = [
        b[0]
        for b in solution_batch_sizes[solution_batch_sizes == problem_batch_sizes].index
    ]
    return df_sol[df_sol.batch_start_time.isin(batch_start_times)]


def compute_orig_total_orders(df_sol, df_exec):
    df = df_sol.groupby(["batch_start_time", "batch_end_time"]).apply(
        compute_orig_batch, df_exec=df_exec
    )
    tokens = pd.concat([df_sol.sell_token, df_sol.buy_token], axis=0).unique()
    return (df.sell_token.isin(tokens) & df.buy_token.isin(tokens)).sum()


def compute_orig_total_users(df_sol, df_exec):
    df = df_sol.groupby(["batch_start_time", "batch_end_time"]).apply(
        compute_orig_batch, df_exec=df_exec
    )
    tokens = pd.concat([df_sol.sell_token, df_sol.buy_token], axis=0).unique()
    return df[df.sell_token.isin(tokens) & df.buy_token.isin(tokens)].address.nunique()


def filter_batches_with_large_liquidity_updates(df_sol):
    # remove batches for which there was a liquidity update to some used pool
    # that resulted in a change of more or less CUTOFF fraction of its liquidity
    CUTOFF = 0.3

    def large_liquidity_update_occurred_in_batch(batch_df):
        def occurred_in_token_pair(batch_df):
            if batch_df.shape[0] == 1:
                return False

            def occurred_between_consecutive_trades(r):
                n1 = r.sell_reserve.iloc[0] + r.exec_sell_amount_uni.iloc[0]
                if r.sell_token.iloc[0] == r.sell_token.iloc[1]:
                    n2 = r.sell_reserve.iloc[1]
                else:
                    assert r.sell_token.iloc[0] == r.buy_token.iloc[1]
                    n2 = r.buy_reserve.iloc[1]
                return abs(n1 - n2) / max(n1, n2) >= CUTOFF

            df = pd.concat([batch_df, batch_df.shift(-1)], axis=1).iloc[:-1]
            return np.any(df.apply(occurred_between_consecutive_trades, axis=1))

        return np.any(batch_df.groupby("token_pair").apply(occurred_in_token_pair))

    df = df_sol[
        [
            "batch_start_time",
            "token_pair",
            "sell_token",
            "buy_token",
            "sell_reserve",
            "buy_reserve",
            "exec_sell_amount_uni",
            "exec_buy_amount_uni",
        ]
    ].groupby("batch_start_time")
    m = df.apply(large_liquidity_update_occurred_in_batch)
    bad_batches = m[m].index
    return df_sol[~df_sol.batch_start_time.isin(bad_batches)]


def get_dfs(
    instance_path, batch_duration, nr_tokens, user_frac, limit_xrate_relax_frac
):
    data_path = f"{instance_path}/s{batch_duration}-t{nr_tokens}-u{user_frac}-l{limit_xrate_relax_frac}/"
    df_exec = load_block_data_file_to_df(f"{data_path}/per_block.json")
    df_sol = create_batches_table(f"{data_path}/solutions/", df_exec)

    # remove batches where there were untouched orders
    df_sol = remove_batches_not_fully_executed(df_sol, df_exec)

    # remove outliers (bottom and top OUTLIER_FRAC quantile of surplus variable)
    # OUTLIER_FRAC = 0.01
    # not_outlier = (df_sol.surplus > df_sol.surplus.quantile(OUTLIER_FRAC)) & (df_sol.surplus < df_sol.surplus.quantile(1-OUTLIER_FRAC))
    # df_sol = df_sol[not_outlier]

    # v = df_sol.max_vol_usd.quantile(.99)
    # df_sol = df_sol[df_sol.max_vol_usd <= v]

    df_sol = filter_batches_with_large_liquidity_updates(df_sol)

    # remove batches with weird results
    # df_sol = df_sol[~df_sol.batch_start_time.isin([1603206524])]

    return (df_sol, df_exec)


def get_block_data_file(
    instance_path, batch_duration, nr_tokens, user_frac, limit_xrate_relax_frac
):
    data_path = f"{instance_path}/s{batch_duration}-t{nr_tokens}-u{user_frac}-l{limit_xrate_relax_frac}/"
    return load_block_data_file_to_df(f"{data_path}/per_block.json")


def get_prices_at_blocks(data_path, blocks, tokens):
    with open(f"{data_path}/per_block.json", "r") as f:
        d = json.load(f)
    prices_in_file = {int(k): v for k, v in d["spot_prices"].items()}
    blocks_in_file = list(prices_in_file.keys())

    prices = {b: {t: None} for b in blocks for t in tokens}
    for t in tokens:
        blocks_with_prices_for_t = list(
            get_largest_element_sequence(
                blocks,
                blocks_in_file,
                lambda a, b: b <= a and t in prices_in_file[b].keys(),
            )
        )
        for bi in range(len(blocks)):
            prices[blocks[bi]][t] = prices_in_file[blocks_with_prices_for_t[bi]][t]
    # prices = {blocks[bi]: {t: prices[blocks_in_file[bi]][t]} for bi in range(len(blocks)) for t in prices[blocks_in_file[bi]].keys()}
    assert set(prices.keys()) == set(blocks)
    return prices
