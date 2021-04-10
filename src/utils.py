def filter_out_arbitrageur_swaps(swaps_by_block, max_amount_swaps_retail_traders=50):
    # Arbitrageur traders are identified as frequent traders
    # frequent traders are identified as traders with more than
    # max_amount_swaps_retail_traders swaps
    print(
        "Before filtering out arbitrageurs, the data contains ",
        count_swaps(swaps_by_block),
        " swaps",
    )
    owners = {
        o["address"] for k in swaps_by_block.keys() for o in swaps_by_block.get(k, [])
    }
    for owner in owners:
        count = 0
        for block_index in swaps_by_block.keys():
            for swaps in swaps_by_block.get(block_index):
                if swaps["address"] == owner:
                    count += 1
        if count > max_amount_swaps_retail_traders:
            for block_index in swaps_by_block.keys():
                swaps_by_block[block_index] = [
                    swaps
                    for swaps in swaps_by_block.get(block_index)
                    if swaps["address"] != owner
                ]

    print(
        "After filtering out arbitrageurs, the data contains ",
        count_swaps(swaps_by_block),
        " swaps",
    )
    return swaps_by_block


def count_swaps(swaps_by_block):
    data_points = 0
    for block_index in swaps_by_block.keys():
        data_points += len(swaps_by_block.get(block_index))
    return data_points


def generate_focus_pairs(sorted_blocks, swaps_by_block):
    focus_pairs = [
        [o["sellToken"], o["buyToken"]]
        for block in sorted_blocks[1:-1]
        for o in swaps_by_block.get(block, [])
    ]
    return list({(tuple(t)) for t in focus_pairs})


def find_order_in_block(block, focus_pair, swaps_by_block):
    for o in swaps_by_block.get(block, []):
        if focus_pair[0] == o["buyToken"] and (
            focus_pair[1] == o["sellToken"]
            or (len(focus_pair) >= 3 and focus_pair[2] == o["sellToken"])
            or (len(focus_pair) >= 4 and focus_pair[3] == o["sellToken"])
        ):
            return True
    return False


def find_order_in_next_k_blocks(
    start_block_index, k, focus_pair, swaps_by_block, sorted_blocks
):
    assert focus_pair is not None
    for block_index in range(start_block_index, start_block_index + k):
        if find_order_in_block(sorted_blocks[block_index], focus_pair, swaps_by_block):
            return True
    return False


def plot_match_survivor(results, filename=None):
    """If filename is not None then creates file on disk."""
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(results.values(), bins=20, density=False, cumulative=-1, log=True)
    plt.title("Number of matchable pairs")
    plt.xlabel("x")
    plt.ylabel("Nr pairs with probability of match >= x")
    if filename is not None:
        plt.savefig(filename)
    plt.show()
