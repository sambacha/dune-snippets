from .subgraph import UniswapClient
import pickle
import os


def get_swaps(use_cache, filename):
    if os.path.exists(filename) and use_cache:
        with open(filename, "br") as f:
            swaps_by_block = pickle.load(f)
    else:
        swaps_by_block = get_uniswap_swaps()
        print("uniswap swap data downloaded")
        with open(filename, "bw+") as f:
            pickle.dump(swaps_by_block, f)

    return swaps_by_block


def get_uniswap_swaps(end_block=11098514, investigation_period=(60 * 60 // 17)):
    uniswap = UniswapClient()

    # Download data from start_block to end_block.
    start_block = end_block - investigation_period
    swap_transactions = uniswap.get_swaps(
        {"block_number_gte": start_block, "block_number_lte": end_block}
    )

    swaps_by_block = dict()

    for swap_transaction in swap_transactions:
        for swap in swap_transaction.swaps:
            if float(swap.amount0_in) > 0:
                sell_token = swap.pair.token0.symbol
                buy_token = swap.pair.token1.symbol
                sell_amount = swap.amount0_in
                buy_amount = swap.amount1_out
                volume = swap.amount_usd
            else:
                sell_token = swap.pair.token1.symbol
                buy_token = swap.pair.token0.symbol
                sell_amount = swap.amount1_in
                buy_amount = swap.amount0_out
                volume = swap.amount_usd
            o = {
                "sellToken": sell_token,
                "buyToken": buy_token,
                "sellAmount": sell_amount,
                "buyAmount": buy_amount,
                "volume": volume,
            }
            block_number = int(swap_transaction.block_number)
            if block_number not in swaps_by_block.keys():
                swaps_by_block[block_number] = []
            swaps_by_block[block_number].append(o)
    return swaps_by_block
