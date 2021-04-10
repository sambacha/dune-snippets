import sgqlc.types


uniswap_graphql_schema = sgqlc.types.Schema()


########################################################################
# Scalars and Enumerations
########################################################################
class BigDecimal(sgqlc.types.Scalar):
    __schema__ = uniswap_graphql_schema


class BigInt(sgqlc.types.Scalar):
    __schema__ = uniswap_graphql_schema


Boolean = sgqlc.types.Boolean


class Bundle_orderBy(sgqlc.types.Enum):
    __schema__ = uniswap_graphql_schema
    __choices__ = ("id", "ethPrice")


class Burn_orderBy(sgqlc.types.Enum):
    __schema__ = uniswap_graphql_schema
    __choices__ = (
        "id",
        "transaction",
        "timestamp",
        "pair",
        "liquidity",
        "sender",
        "amount0",
        "amount1",
        "to",
        "logIndex",
        "amountUSD",
        "needsComplete",
        "feeTo",
        "feeLiquidity",
    )


class Bytes(sgqlc.types.Scalar):
    __schema__ = uniswap_graphql_schema


ID = sgqlc.types.ID

Int = sgqlc.types.Int


class LiquidityPositionSnapshot_orderBy(sgqlc.types.Enum):
    __schema__ = uniswap_graphql_schema
    __choices__ = (
        "id",
        "liquidityPosition",
        "timestamp",
        "block",
        "user",
        "pair",
        "token0PriceUSD",
        "token1PriceUSD",
        "reserve0",
        "reserve1",
        "reserveUSD",
        "liquidityTokenTotalSupply",
        "liquidityTokenBalance",
    )


class LiquidityPosition_orderBy(sgqlc.types.Enum):
    __schema__ = uniswap_graphql_schema
    __choices__ = ("id", "user", "pair", "liquidityTokenBalance")


class Mint_orderBy(sgqlc.types.Enum):
    __schema__ = uniswap_graphql_schema
    __choices__ = (
        "id",
        "transaction",
        "timestamp",
        "pair",
        "to",
        "liquidity",
        "sender",
        "amount0",
        "amount1",
        "logIndex",
        "amountUSD",
        "feeTo",
        "feeLiquidity",
    )


class OrderDirection(sgqlc.types.Enum):
    __schema__ = uniswap_graphql_schema
    __choices__ = ("asc", "desc")


class PairDayData_orderBy(sgqlc.types.Enum):
    __schema__ = uniswap_graphql_schema
    __choices__ = (
        "id",
        "date",
        "pairAddress",
        "token0",
        "token1",
        "reserve0",
        "reserve1",
        "totalSupply",
        "reserveUSD",
        "dailyVolumeToken0",
        "dailyVolumeToken1",
        "dailyVolumeUSD",
        "dailyTxns",
    )


class PairHourData_orderBy(sgqlc.types.Enum):
    __schema__ = uniswap_graphql_schema
    __choices__ = (
        "id",
        "hourStartUnix",
        "pair",
        "reserve0",
        "reserve1",
        "reserveUSD",
        "hourlyVolumeToken0",
        "hourlyVolumeToken1",
        "hourlyVolumeUSD",
        "hourlyTxns",
    )


class Pair_orderBy(sgqlc.types.Enum):
    __schema__ = uniswap_graphql_schema
    __choices__ = (
        "id",
        "token0",
        "token1",
        "reserve0",
        "reserve1",
        "totalSupply",
        "reserveETH",
        "reserveUSD",
        "trackedReserveETH",
        "token0Price",
        "token1Price",
        "volumeToken0",
        "volumeToken1",
        "volumeUSD",
        "untrackedVolumeUSD",
        "txCount",
        "createdAtTimestamp",
        "createdAtBlockNumber",
        "liquidityProviderCount",
    )


String = sgqlc.types.String


class Swap_orderBy(sgqlc.types.Enum):
    __schema__ = uniswap_graphql_schema
    __choices__ = (
        "id",
        "transaction",
        "timestamp",
        "pair",
        "sender",
        "amount0In",
        "amount1In",
        "amount0Out",
        "amount1Out",
        "to",
        "logIndex",
        "amountUSD",
    )


class TokenDayData_orderBy(sgqlc.types.Enum):
    __schema__ = uniswap_graphql_schema
    __choices__ = (
        "id",
        "date",
        "token",
        "dailyVolumeToken",
        "dailyVolumeETH",
        "dailyVolumeUSD",
        "dailyTxns",
        "totalLiquidityToken",
        "totalLiquidityETH",
        "totalLiquidityUSD",
        "priceUSD",
        "maxStored",
        "mostLiquidPairs",
    )


class Token_orderBy(sgqlc.types.Enum):
    __schema__ = uniswap_graphql_schema
    __choices__ = (
        "id",
        "symbol",
        "name",
        "decimals",
        "totalSupply",
        "tradeVolume",
        "tradeVolumeUSD",
        "untrackedVolumeUSD",
        "txCount",
        "totalLiquidity",
        "derivedETH",
        "mostLiquidPairs",
    )


class Transaction_orderBy(sgqlc.types.Enum):
    __schema__ = uniswap_graphql_schema
    __choices__ = ("id", "blockNumber", "timestamp", "mints", "burns", "swaps")


class UniswapDayData_orderBy(sgqlc.types.Enum):
    __schema__ = uniswap_graphql_schema
    __choices__ = (
        "id",
        "date",
        "dailyVolumeETH",
        "dailyVolumeUSD",
        "dailyVolumeUntracked",
        "totalVolumeETH",
        "totalLiquidityETH",
        "totalVolumeUSD",
        "totalLiquidityUSD",
        "maxStored",
        "mostLiquidTokens",
        "txCount",
    )


class UniswapFactory_orderBy(sgqlc.types.Enum):
    __schema__ = uniswap_graphql_schema
    __choices__ = (
        "id",
        "pairCount",
        "totalVolumeUSD",
        "totalVolumeETH",
        "untrackedVolumeUSD",
        "totalLiquidityUSD",
        "totalLiquidityETH",
        "txCount",
        "mostLiquidTokens",
    )


class User_orderBy(sgqlc.types.Enum):
    __schema__ = uniswap_graphql_schema
    __choices__ = ("id", "liquidityPositions", "usdSwapped")


class _SubgraphErrorPolicy_(sgqlc.types.Enum):
    __schema__ = uniswap_graphql_schema
    __choices__ = ("allow", "deny")


########################################################################
# Input Objects
########################################################################
class Block_height(sgqlc.types.Input):
    __schema__ = uniswap_graphql_schema
    __field_names__ = ("hash", "number")
    hash = sgqlc.types.Field(Bytes, graphql_name="hash")
    number = sgqlc.types.Field(Int, graphql_name="number")


class Bundle_filter(sgqlc.types.Input):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "id_not",
        "id_gt",
        "id_lt",
        "id_gte",
        "id_lte",
        "id_in",
        "id_not_in",
        "eth_price",
        "eth_price_not",
        "eth_price_gt",
        "eth_price_lt",
        "eth_price_gte",
        "eth_price_lte",
        "eth_price_in",
        "eth_price_not_in",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    id_not = sgqlc.types.Field(ID, graphql_name="id_not")
    id_gt = sgqlc.types.Field(ID, graphql_name="id_gt")
    id_lt = sgqlc.types.Field(ID, graphql_name="id_lt")
    id_gte = sgqlc.types.Field(ID, graphql_name="id_gte")
    id_lte = sgqlc.types.Field(ID, graphql_name="id_lte")
    id_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_in"
    )
    id_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_not_in"
    )
    eth_price = sgqlc.types.Field(BigDecimal, graphql_name="ethPrice")
    eth_price_not = sgqlc.types.Field(BigDecimal, graphql_name="ethPrice_not")
    eth_price_gt = sgqlc.types.Field(BigDecimal, graphql_name="ethPrice_gt")
    eth_price_lt = sgqlc.types.Field(BigDecimal, graphql_name="ethPrice_lt")
    eth_price_gte = sgqlc.types.Field(BigDecimal, graphql_name="ethPrice_gte")
    eth_price_lte = sgqlc.types.Field(BigDecimal, graphql_name="ethPrice_lte")
    eth_price_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="ethPrice_in",
    )
    eth_price_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="ethPrice_not_in",
    )


class Burn_filter(sgqlc.types.Input):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "id_not",
        "id_gt",
        "id_lt",
        "id_gte",
        "id_lte",
        "id_in",
        "id_not_in",
        "transaction",
        "transaction_not",
        "transaction_gt",
        "transaction_lt",
        "transaction_gte",
        "transaction_lte",
        "transaction_in",
        "transaction_not_in",
        "transaction_contains",
        "transaction_not_contains",
        "transaction_starts_with",
        "transaction_not_starts_with",
        "transaction_ends_with",
        "transaction_not_ends_with",
        "timestamp",
        "timestamp_not",
        "timestamp_gt",
        "timestamp_lt",
        "timestamp_gte",
        "timestamp_lte",
        "timestamp_in",
        "timestamp_not_in",
        "pair",
        "pair_not",
        "pair_gt",
        "pair_lt",
        "pair_gte",
        "pair_lte",
        "pair_in",
        "pair_not_in",
        "pair_contains",
        "pair_not_contains",
        "pair_starts_with",
        "pair_not_starts_with",
        "pair_ends_with",
        "pair_not_ends_with",
        "liquidity",
        "liquidity_not",
        "liquidity_gt",
        "liquidity_lt",
        "liquidity_gte",
        "liquidity_lte",
        "liquidity_in",
        "liquidity_not_in",
        "sender",
        "sender_not",
        "sender_in",
        "sender_not_in",
        "sender_contains",
        "sender_not_contains",
        "amount0",
        "amount0_not",
        "amount0_gt",
        "amount0_lt",
        "amount0_gte",
        "amount0_lte",
        "amount0_in",
        "amount0_not_in",
        "amount1",
        "amount1_not",
        "amount1_gt",
        "amount1_lt",
        "amount1_gte",
        "amount1_lte",
        "amount1_in",
        "amount1_not_in",
        "to",
        "to_not",
        "to_in",
        "to_not_in",
        "to_contains",
        "to_not_contains",
        "log_index",
        "log_index_not",
        "log_index_gt",
        "log_index_lt",
        "log_index_gte",
        "log_index_lte",
        "log_index_in",
        "log_index_not_in",
        "amount_usd",
        "amount_usd_not",
        "amount_usd_gt",
        "amount_usd_lt",
        "amount_usd_gte",
        "amount_usd_lte",
        "amount_usd_in",
        "amount_usd_not_in",
        "needs_complete",
        "needs_complete_not",
        "needs_complete_in",
        "needs_complete_not_in",
        "fee_to",
        "fee_to_not",
        "fee_to_in",
        "fee_to_not_in",
        "fee_to_contains",
        "fee_to_not_contains",
        "fee_liquidity",
        "fee_liquidity_not",
        "fee_liquidity_gt",
        "fee_liquidity_lt",
        "fee_liquidity_gte",
        "fee_liquidity_lte",
        "fee_liquidity_in",
        "fee_liquidity_not_in",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    id_not = sgqlc.types.Field(ID, graphql_name="id_not")
    id_gt = sgqlc.types.Field(ID, graphql_name="id_gt")
    id_lt = sgqlc.types.Field(ID, graphql_name="id_lt")
    id_gte = sgqlc.types.Field(ID, graphql_name="id_gte")
    id_lte = sgqlc.types.Field(ID, graphql_name="id_lte")
    id_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_in"
    )
    id_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_not_in"
    )
    transaction = sgqlc.types.Field(String, graphql_name="transaction")
    transaction_not = sgqlc.types.Field(String, graphql_name="transaction_not")
    transaction_gt = sgqlc.types.Field(String, graphql_name="transaction_gt")
    transaction_lt = sgqlc.types.Field(String, graphql_name="transaction_lt")
    transaction_gte = sgqlc.types.Field(String, graphql_name="transaction_gte")
    transaction_lte = sgqlc.types.Field(String, graphql_name="transaction_lte")
    transaction_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="transaction_in"
    )
    transaction_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="transaction_not_in",
    )
    transaction_contains = sgqlc.types.Field(
        String, graphql_name="transaction_contains"
    )
    transaction_not_contains = sgqlc.types.Field(
        String, graphql_name="transaction_not_contains"
    )
    transaction_starts_with = sgqlc.types.Field(
        String, graphql_name="transaction_starts_with"
    )
    transaction_not_starts_with = sgqlc.types.Field(
        String, graphql_name="transaction_not_starts_with"
    )
    transaction_ends_with = sgqlc.types.Field(
        String, graphql_name="transaction_ends_with"
    )
    transaction_not_ends_with = sgqlc.types.Field(
        String, graphql_name="transaction_not_ends_with"
    )
    timestamp = sgqlc.types.Field(BigInt, graphql_name="timestamp")
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name="timestamp_not")
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name="timestamp_gt")
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name="timestamp_lt")
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name="timestamp_gte")
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name="timestamp_lte")
    timestamp_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="timestamp_in"
    )
    timestamp_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="timestamp_not_in",
    )
    pair = sgqlc.types.Field(String, graphql_name="pair")
    pair_not = sgqlc.types.Field(String, graphql_name="pair_not")
    pair_gt = sgqlc.types.Field(String, graphql_name="pair_gt")
    pair_lt = sgqlc.types.Field(String, graphql_name="pair_lt")
    pair_gte = sgqlc.types.Field(String, graphql_name="pair_gte")
    pair_lte = sgqlc.types.Field(String, graphql_name="pair_lte")
    pair_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="pair_in"
    )
    pair_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="pair_not_in"
    )
    pair_contains = sgqlc.types.Field(String, graphql_name="pair_contains")
    pair_not_contains = sgqlc.types.Field(String, graphql_name="pair_not_contains")
    pair_starts_with = sgqlc.types.Field(String, graphql_name="pair_starts_with")
    pair_not_starts_with = sgqlc.types.Field(
        String, graphql_name="pair_not_starts_with"
    )
    pair_ends_with = sgqlc.types.Field(String, graphql_name="pair_ends_with")
    pair_not_ends_with = sgqlc.types.Field(String, graphql_name="pair_not_ends_with")
    liquidity = sgqlc.types.Field(BigDecimal, graphql_name="liquidity")
    liquidity_not = sgqlc.types.Field(BigDecimal, graphql_name="liquidity_not")
    liquidity_gt = sgqlc.types.Field(BigDecimal, graphql_name="liquidity_gt")
    liquidity_lt = sgqlc.types.Field(BigDecimal, graphql_name="liquidity_lt")
    liquidity_gte = sgqlc.types.Field(BigDecimal, graphql_name="liquidity_gte")
    liquidity_lte = sgqlc.types.Field(BigDecimal, graphql_name="liquidity_lte")
    liquidity_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="liquidity_in",
    )
    liquidity_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="liquidity_not_in",
    )
    sender = sgqlc.types.Field(Bytes, graphql_name="sender")
    sender_not = sgqlc.types.Field(Bytes, graphql_name="sender_not")
    sender_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name="sender_in"
    )
    sender_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name="sender_not_in"
    )
    sender_contains = sgqlc.types.Field(Bytes, graphql_name="sender_contains")
    sender_not_contains = sgqlc.types.Field(Bytes, graphql_name="sender_not_contains")
    amount0 = sgqlc.types.Field(BigDecimal, graphql_name="amount0")
    amount0_not = sgqlc.types.Field(BigDecimal, graphql_name="amount0_not")
    amount0_gt = sgqlc.types.Field(BigDecimal, graphql_name="amount0_gt")
    amount0_lt = sgqlc.types.Field(BigDecimal, graphql_name="amount0_lt")
    amount0_gte = sgqlc.types.Field(BigDecimal, graphql_name="amount0_gte")
    amount0_lte = sgqlc.types.Field(BigDecimal, graphql_name="amount0_lte")
    amount0_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name="amount0_in"
    )
    amount0_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="amount0_not_in",
    )
    amount1 = sgqlc.types.Field(BigDecimal, graphql_name="amount1")
    amount1_not = sgqlc.types.Field(BigDecimal, graphql_name="amount1_not")
    amount1_gt = sgqlc.types.Field(BigDecimal, graphql_name="amount1_gt")
    amount1_lt = sgqlc.types.Field(BigDecimal, graphql_name="amount1_lt")
    amount1_gte = sgqlc.types.Field(BigDecimal, graphql_name="amount1_gte")
    amount1_lte = sgqlc.types.Field(BigDecimal, graphql_name="amount1_lte")
    amount1_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name="amount1_in"
    )
    amount1_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="amount1_not_in",
    )
    to = sgqlc.types.Field(Bytes, graphql_name="to")
    to_not = sgqlc.types.Field(Bytes, graphql_name="to_not")
    to_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name="to_in"
    )
    to_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name="to_not_in"
    )
    to_contains = sgqlc.types.Field(Bytes, graphql_name="to_contains")
    to_not_contains = sgqlc.types.Field(Bytes, graphql_name="to_not_contains")
    log_index = sgqlc.types.Field(BigInt, graphql_name="logIndex")
    log_index_not = sgqlc.types.Field(BigInt, graphql_name="logIndex_not")
    log_index_gt = sgqlc.types.Field(BigInt, graphql_name="logIndex_gt")
    log_index_lt = sgqlc.types.Field(BigInt, graphql_name="logIndex_lt")
    log_index_gte = sgqlc.types.Field(BigInt, graphql_name="logIndex_gte")
    log_index_lte = sgqlc.types.Field(BigInt, graphql_name="logIndex_lte")
    log_index_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="logIndex_in"
    )
    log_index_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="logIndex_not_in",
    )
    amount_usd = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD")
    amount_usd_not = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD_not")
    amount_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD_gt")
    amount_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD_lt")
    amount_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD_gte")
    amount_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD_lte")
    amount_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="amountUSD_in",
    )
    amount_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="amountUSD_not_in",
    )
    needs_complete = sgqlc.types.Field(Boolean, graphql_name="needsComplete")
    needs_complete_not = sgqlc.types.Field(Boolean, graphql_name="needsComplete_not")
    needs_complete_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Boolean)),
        graphql_name="needsComplete_in",
    )
    needs_complete_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Boolean)),
        graphql_name="needsComplete_not_in",
    )
    fee_to = sgqlc.types.Field(Bytes, graphql_name="feeTo")
    fee_to_not = sgqlc.types.Field(Bytes, graphql_name="feeTo_not")
    fee_to_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name="feeTo_in"
    )
    fee_to_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name="feeTo_not_in"
    )
    fee_to_contains = sgqlc.types.Field(Bytes, graphql_name="feeTo_contains")
    fee_to_not_contains = sgqlc.types.Field(Bytes, graphql_name="feeTo_not_contains")
    fee_liquidity = sgqlc.types.Field(BigDecimal, graphql_name="feeLiquidity")
    fee_liquidity_not = sgqlc.types.Field(BigDecimal, graphql_name="feeLiquidity_not")
    fee_liquidity_gt = sgqlc.types.Field(BigDecimal, graphql_name="feeLiquidity_gt")
    fee_liquidity_lt = sgqlc.types.Field(BigDecimal, graphql_name="feeLiquidity_lt")
    fee_liquidity_gte = sgqlc.types.Field(BigDecimal, graphql_name="feeLiquidity_gte")
    fee_liquidity_lte = sgqlc.types.Field(BigDecimal, graphql_name="feeLiquidity_lte")
    fee_liquidity_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="feeLiquidity_in",
    )
    fee_liquidity_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="feeLiquidity_not_in",
    )


class LiquidityPositionSnapshot_filter(sgqlc.types.Input):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "id_not",
        "id_gt",
        "id_lt",
        "id_gte",
        "id_lte",
        "id_in",
        "id_not_in",
        "liquidity_position",
        "liquidity_position_not",
        "liquidity_position_gt",
        "liquidity_position_lt",
        "liquidity_position_gte",
        "liquidity_position_lte",
        "liquidity_position_in",
        "liquidity_position_not_in",
        "liquidity_position_contains",
        "liquidity_position_not_contains",
        "liquidity_position_starts_with",
        "liquidity_position_not_starts_with",
        "liquidity_position_ends_with",
        "liquidity_position_not_ends_with",
        "timestamp",
        "timestamp_not",
        "timestamp_gt",
        "timestamp_lt",
        "timestamp_gte",
        "timestamp_lte",
        "timestamp_in",
        "timestamp_not_in",
        "block",
        "block_not",
        "block_gt",
        "block_lt",
        "block_gte",
        "block_lte",
        "block_in",
        "block_not_in",
        "user",
        "user_not",
        "user_gt",
        "user_lt",
        "user_gte",
        "user_lte",
        "user_in",
        "user_not_in",
        "user_contains",
        "user_not_contains",
        "user_starts_with",
        "user_not_starts_with",
        "user_ends_with",
        "user_not_ends_with",
        "pair",
        "pair_not",
        "pair_gt",
        "pair_lt",
        "pair_gte",
        "pair_lte",
        "pair_in",
        "pair_not_in",
        "pair_contains",
        "pair_not_contains",
        "pair_starts_with",
        "pair_not_starts_with",
        "pair_ends_with",
        "pair_not_ends_with",
        "token0_price_usd",
        "token0_price_usd_not",
        "token0_price_usd_gt",
        "token0_price_usd_lt",
        "token0_price_usd_gte",
        "token0_price_usd_lte",
        "token0_price_usd_in",
        "token0_price_usd_not_in",
        "token1_price_usd",
        "token1_price_usd_not",
        "token1_price_usd_gt",
        "token1_price_usd_lt",
        "token1_price_usd_gte",
        "token1_price_usd_lte",
        "token1_price_usd_in",
        "token1_price_usd_not_in",
        "reserve0",
        "reserve0_not",
        "reserve0_gt",
        "reserve0_lt",
        "reserve0_gte",
        "reserve0_lte",
        "reserve0_in",
        "reserve0_not_in",
        "reserve1",
        "reserve1_not",
        "reserve1_gt",
        "reserve1_lt",
        "reserve1_gte",
        "reserve1_lte",
        "reserve1_in",
        "reserve1_not_in",
        "reserve_usd",
        "reserve_usd_not",
        "reserve_usd_gt",
        "reserve_usd_lt",
        "reserve_usd_gte",
        "reserve_usd_lte",
        "reserve_usd_in",
        "reserve_usd_not_in",
        "liquidity_token_total_supply",
        "liquidity_token_total_supply_not",
        "liquidity_token_total_supply_gt",
        "liquidity_token_total_supply_lt",
        "liquidity_token_total_supply_gte",
        "liquidity_token_total_supply_lte",
        "liquidity_token_total_supply_in",
        "liquidity_token_total_supply_not_in",
        "liquidity_token_balance",
        "liquidity_token_balance_not",
        "liquidity_token_balance_gt",
        "liquidity_token_balance_lt",
        "liquidity_token_balance_gte",
        "liquidity_token_balance_lte",
        "liquidity_token_balance_in",
        "liquidity_token_balance_not_in",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    id_not = sgqlc.types.Field(ID, graphql_name="id_not")
    id_gt = sgqlc.types.Field(ID, graphql_name="id_gt")
    id_lt = sgqlc.types.Field(ID, graphql_name="id_lt")
    id_gte = sgqlc.types.Field(ID, graphql_name="id_gte")
    id_lte = sgqlc.types.Field(ID, graphql_name="id_lte")
    id_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_in"
    )
    id_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_not_in"
    )
    liquidity_position = sgqlc.types.Field(String, graphql_name="liquidityPosition")
    liquidity_position_not = sgqlc.types.Field(
        String, graphql_name="liquidityPosition_not"
    )
    liquidity_position_gt = sgqlc.types.Field(
        String, graphql_name="liquidityPosition_gt"
    )
    liquidity_position_lt = sgqlc.types.Field(
        String, graphql_name="liquidityPosition_lt"
    )
    liquidity_position_gte = sgqlc.types.Field(
        String, graphql_name="liquidityPosition_gte"
    )
    liquidity_position_lte = sgqlc.types.Field(
        String, graphql_name="liquidityPosition_lte"
    )
    liquidity_position_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="liquidityPosition_in",
    )
    liquidity_position_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="liquidityPosition_not_in",
    )
    liquidity_position_contains = sgqlc.types.Field(
        String, graphql_name="liquidityPosition_contains"
    )
    liquidity_position_not_contains = sgqlc.types.Field(
        String, graphql_name="liquidityPosition_not_contains"
    )
    liquidity_position_starts_with = sgqlc.types.Field(
        String, graphql_name="liquidityPosition_starts_with"
    )
    liquidity_position_not_starts_with = sgqlc.types.Field(
        String, graphql_name="liquidityPosition_not_starts_with"
    )
    liquidity_position_ends_with = sgqlc.types.Field(
        String, graphql_name="liquidityPosition_ends_with"
    )
    liquidity_position_not_ends_with = sgqlc.types.Field(
        String, graphql_name="liquidityPosition_not_ends_with"
    )
    timestamp = sgqlc.types.Field(Int, graphql_name="timestamp")
    timestamp_not = sgqlc.types.Field(Int, graphql_name="timestamp_not")
    timestamp_gt = sgqlc.types.Field(Int, graphql_name="timestamp_gt")
    timestamp_lt = sgqlc.types.Field(Int, graphql_name="timestamp_lt")
    timestamp_gte = sgqlc.types.Field(Int, graphql_name="timestamp_gte")
    timestamp_lte = sgqlc.types.Field(Int, graphql_name="timestamp_lte")
    timestamp_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="timestamp_in"
    )
    timestamp_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="timestamp_not_in"
    )
    block = sgqlc.types.Field(Int, graphql_name="block")
    block_not = sgqlc.types.Field(Int, graphql_name="block_not")
    block_gt = sgqlc.types.Field(Int, graphql_name="block_gt")
    block_lt = sgqlc.types.Field(Int, graphql_name="block_lt")
    block_gte = sgqlc.types.Field(Int, graphql_name="block_gte")
    block_lte = sgqlc.types.Field(Int, graphql_name="block_lte")
    block_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="block_in"
    )
    block_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="block_not_in"
    )
    user = sgqlc.types.Field(String, graphql_name="user")
    user_not = sgqlc.types.Field(String, graphql_name="user_not")
    user_gt = sgqlc.types.Field(String, graphql_name="user_gt")
    user_lt = sgqlc.types.Field(String, graphql_name="user_lt")
    user_gte = sgqlc.types.Field(String, graphql_name="user_gte")
    user_lte = sgqlc.types.Field(String, graphql_name="user_lte")
    user_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="user_in"
    )
    user_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="user_not_in"
    )
    user_contains = sgqlc.types.Field(String, graphql_name="user_contains")
    user_not_contains = sgqlc.types.Field(String, graphql_name="user_not_contains")
    user_starts_with = sgqlc.types.Field(String, graphql_name="user_starts_with")
    user_not_starts_with = sgqlc.types.Field(
        String, graphql_name="user_not_starts_with"
    )
    user_ends_with = sgqlc.types.Field(String, graphql_name="user_ends_with")
    user_not_ends_with = sgqlc.types.Field(String, graphql_name="user_not_ends_with")
    pair = sgqlc.types.Field(String, graphql_name="pair")
    pair_not = sgqlc.types.Field(String, graphql_name="pair_not")
    pair_gt = sgqlc.types.Field(String, graphql_name="pair_gt")
    pair_lt = sgqlc.types.Field(String, graphql_name="pair_lt")
    pair_gte = sgqlc.types.Field(String, graphql_name="pair_gte")
    pair_lte = sgqlc.types.Field(String, graphql_name="pair_lte")
    pair_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="pair_in"
    )
    pair_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="pair_not_in"
    )
    pair_contains = sgqlc.types.Field(String, graphql_name="pair_contains")
    pair_not_contains = sgqlc.types.Field(String, graphql_name="pair_not_contains")
    pair_starts_with = sgqlc.types.Field(String, graphql_name="pair_starts_with")
    pair_not_starts_with = sgqlc.types.Field(
        String, graphql_name="pair_not_starts_with"
    )
    pair_ends_with = sgqlc.types.Field(String, graphql_name="pair_ends_with")
    pair_not_ends_with = sgqlc.types.Field(String, graphql_name="pair_not_ends_with")
    token0_price_usd = sgqlc.types.Field(BigDecimal, graphql_name="token0PriceUSD")
    token0_price_usd_not = sgqlc.types.Field(
        BigDecimal, graphql_name="token0PriceUSD_not"
    )
    token0_price_usd_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="token0PriceUSD_gt"
    )
    token0_price_usd_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="token0PriceUSD_lt"
    )
    token0_price_usd_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="token0PriceUSD_gte"
    )
    token0_price_usd_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="token0PriceUSD_lte"
    )
    token0_price_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="token0PriceUSD_in",
    )
    token0_price_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="token0PriceUSD_not_in",
    )
    token1_price_usd = sgqlc.types.Field(BigDecimal, graphql_name="token1PriceUSD")
    token1_price_usd_not = sgqlc.types.Field(
        BigDecimal, graphql_name="token1PriceUSD_not"
    )
    token1_price_usd_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="token1PriceUSD_gt"
    )
    token1_price_usd_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="token1PriceUSD_lt"
    )
    token1_price_usd_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="token1PriceUSD_gte"
    )
    token1_price_usd_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="token1PriceUSD_lte"
    )
    token1_price_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="token1PriceUSD_in",
    )
    token1_price_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="token1PriceUSD_not_in",
    )
    reserve0 = sgqlc.types.Field(BigDecimal, graphql_name="reserve0")
    reserve0_not = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_not")
    reserve0_gt = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_gt")
    reserve0_lt = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_lt")
    reserve0_gte = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_gte")
    reserve0_lte = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_lte")
    reserve0_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserve0_in",
    )
    reserve0_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserve0_not_in",
    )
    reserve1 = sgqlc.types.Field(BigDecimal, graphql_name="reserve1")
    reserve1_not = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_not")
    reserve1_gt = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_gt")
    reserve1_lt = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_lt")
    reserve1_gte = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_gte")
    reserve1_lte = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_lte")
    reserve1_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserve1_in",
    )
    reserve1_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserve1_not_in",
    )
    reserve_usd = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD")
    reserve_usd_not = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_not")
    reserve_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_gt")
    reserve_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_lt")
    reserve_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_gte")
    reserve_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_lte")
    reserve_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserveUSD_in",
    )
    reserve_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserveUSD_not_in",
    )
    liquidity_token_total_supply = sgqlc.types.Field(
        BigDecimal, graphql_name="liquidityTokenTotalSupply"
    )
    liquidity_token_total_supply_not = sgqlc.types.Field(
        BigDecimal, graphql_name="liquidityTokenTotalSupply_not"
    )
    liquidity_token_total_supply_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="liquidityTokenTotalSupply_gt"
    )
    liquidity_token_total_supply_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="liquidityTokenTotalSupply_lt"
    )
    liquidity_token_total_supply_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="liquidityTokenTotalSupply_gte"
    )
    liquidity_token_total_supply_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="liquidityTokenTotalSupply_lte"
    )
    liquidity_token_total_supply_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="liquidityTokenTotalSupply_in",
    )
    liquidity_token_total_supply_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="liquidityTokenTotalSupply_not_in",
    )
    liquidity_token_balance = sgqlc.types.Field(
        BigDecimal, graphql_name="liquidityTokenBalance"
    )
    liquidity_token_balance_not = sgqlc.types.Field(
        BigDecimal, graphql_name="liquidityTokenBalance_not"
    )
    liquidity_token_balance_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="liquidityTokenBalance_gt"
    )
    liquidity_token_balance_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="liquidityTokenBalance_lt"
    )
    liquidity_token_balance_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="liquidityTokenBalance_gte"
    )
    liquidity_token_balance_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="liquidityTokenBalance_lte"
    )
    liquidity_token_balance_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="liquidityTokenBalance_in",
    )
    liquidity_token_balance_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="liquidityTokenBalance_not_in",
    )


class LiquidityPosition_filter(sgqlc.types.Input):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "id_not",
        "id_gt",
        "id_lt",
        "id_gte",
        "id_lte",
        "id_in",
        "id_not_in",
        "user",
        "user_not",
        "user_gt",
        "user_lt",
        "user_gte",
        "user_lte",
        "user_in",
        "user_not_in",
        "user_contains",
        "user_not_contains",
        "user_starts_with",
        "user_not_starts_with",
        "user_ends_with",
        "user_not_ends_with",
        "pair",
        "pair_not",
        "pair_gt",
        "pair_lt",
        "pair_gte",
        "pair_lte",
        "pair_in",
        "pair_not_in",
        "pair_contains",
        "pair_not_contains",
        "pair_starts_with",
        "pair_not_starts_with",
        "pair_ends_with",
        "pair_not_ends_with",
        "liquidity_token_balance",
        "liquidity_token_balance_not",
        "liquidity_token_balance_gt",
        "liquidity_token_balance_lt",
        "liquidity_token_balance_gte",
        "liquidity_token_balance_lte",
        "liquidity_token_balance_in",
        "liquidity_token_balance_not_in",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    id_not = sgqlc.types.Field(ID, graphql_name="id_not")
    id_gt = sgqlc.types.Field(ID, graphql_name="id_gt")
    id_lt = sgqlc.types.Field(ID, graphql_name="id_lt")
    id_gte = sgqlc.types.Field(ID, graphql_name="id_gte")
    id_lte = sgqlc.types.Field(ID, graphql_name="id_lte")
    id_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_in"
    )
    id_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_not_in"
    )
    user = sgqlc.types.Field(String, graphql_name="user")
    user_not = sgqlc.types.Field(String, graphql_name="user_not")
    user_gt = sgqlc.types.Field(String, graphql_name="user_gt")
    user_lt = sgqlc.types.Field(String, graphql_name="user_lt")
    user_gte = sgqlc.types.Field(String, graphql_name="user_gte")
    user_lte = sgqlc.types.Field(String, graphql_name="user_lte")
    user_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="user_in"
    )
    user_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="user_not_in"
    )
    user_contains = sgqlc.types.Field(String, graphql_name="user_contains")
    user_not_contains = sgqlc.types.Field(String, graphql_name="user_not_contains")
    user_starts_with = sgqlc.types.Field(String, graphql_name="user_starts_with")
    user_not_starts_with = sgqlc.types.Field(
        String, graphql_name="user_not_starts_with"
    )
    user_ends_with = sgqlc.types.Field(String, graphql_name="user_ends_with")
    user_not_ends_with = sgqlc.types.Field(String, graphql_name="user_not_ends_with")
    pair = sgqlc.types.Field(String, graphql_name="pair")
    pair_not = sgqlc.types.Field(String, graphql_name="pair_not")
    pair_gt = sgqlc.types.Field(String, graphql_name="pair_gt")
    pair_lt = sgqlc.types.Field(String, graphql_name="pair_lt")
    pair_gte = sgqlc.types.Field(String, graphql_name="pair_gte")
    pair_lte = sgqlc.types.Field(String, graphql_name="pair_lte")
    pair_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="pair_in"
    )
    pair_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="pair_not_in"
    )
    pair_contains = sgqlc.types.Field(String, graphql_name="pair_contains")
    pair_not_contains = sgqlc.types.Field(String, graphql_name="pair_not_contains")
    pair_starts_with = sgqlc.types.Field(String, graphql_name="pair_starts_with")
    pair_not_starts_with = sgqlc.types.Field(
        String, graphql_name="pair_not_starts_with"
    )
    pair_ends_with = sgqlc.types.Field(String, graphql_name="pair_ends_with")
    pair_not_ends_with = sgqlc.types.Field(String, graphql_name="pair_not_ends_with")
    liquidity_token_balance = sgqlc.types.Field(
        BigDecimal, graphql_name="liquidityTokenBalance"
    )
    liquidity_token_balance_not = sgqlc.types.Field(
        BigDecimal, graphql_name="liquidityTokenBalance_not"
    )
    liquidity_token_balance_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="liquidityTokenBalance_gt"
    )
    liquidity_token_balance_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="liquidityTokenBalance_lt"
    )
    liquidity_token_balance_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="liquidityTokenBalance_gte"
    )
    liquidity_token_balance_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="liquidityTokenBalance_lte"
    )
    liquidity_token_balance_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="liquidityTokenBalance_in",
    )
    liquidity_token_balance_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="liquidityTokenBalance_not_in",
    )


class Mint_filter(sgqlc.types.Input):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "id_not",
        "id_gt",
        "id_lt",
        "id_gte",
        "id_lte",
        "id_in",
        "id_not_in",
        "transaction",
        "transaction_not",
        "transaction_gt",
        "transaction_lt",
        "transaction_gte",
        "transaction_lte",
        "transaction_in",
        "transaction_not_in",
        "transaction_contains",
        "transaction_not_contains",
        "transaction_starts_with",
        "transaction_not_starts_with",
        "transaction_ends_with",
        "transaction_not_ends_with",
        "timestamp",
        "timestamp_not",
        "timestamp_gt",
        "timestamp_lt",
        "timestamp_gte",
        "timestamp_lte",
        "timestamp_in",
        "timestamp_not_in",
        "pair",
        "pair_not",
        "pair_gt",
        "pair_lt",
        "pair_gte",
        "pair_lte",
        "pair_in",
        "pair_not_in",
        "pair_contains",
        "pair_not_contains",
        "pair_starts_with",
        "pair_not_starts_with",
        "pair_ends_with",
        "pair_not_ends_with",
        "to",
        "to_not",
        "to_in",
        "to_not_in",
        "to_contains",
        "to_not_contains",
        "liquidity",
        "liquidity_not",
        "liquidity_gt",
        "liquidity_lt",
        "liquidity_gte",
        "liquidity_lte",
        "liquidity_in",
        "liquidity_not_in",
        "sender",
        "sender_not",
        "sender_in",
        "sender_not_in",
        "sender_contains",
        "sender_not_contains",
        "amount0",
        "amount0_not",
        "amount0_gt",
        "amount0_lt",
        "amount0_gte",
        "amount0_lte",
        "amount0_in",
        "amount0_not_in",
        "amount1",
        "amount1_not",
        "amount1_gt",
        "amount1_lt",
        "amount1_gte",
        "amount1_lte",
        "amount1_in",
        "amount1_not_in",
        "log_index",
        "log_index_not",
        "log_index_gt",
        "log_index_lt",
        "log_index_gte",
        "log_index_lte",
        "log_index_in",
        "log_index_not_in",
        "amount_usd",
        "amount_usd_not",
        "amount_usd_gt",
        "amount_usd_lt",
        "amount_usd_gte",
        "amount_usd_lte",
        "amount_usd_in",
        "amount_usd_not_in",
        "fee_to",
        "fee_to_not",
        "fee_to_in",
        "fee_to_not_in",
        "fee_to_contains",
        "fee_to_not_contains",
        "fee_liquidity",
        "fee_liquidity_not",
        "fee_liquidity_gt",
        "fee_liquidity_lt",
        "fee_liquidity_gte",
        "fee_liquidity_lte",
        "fee_liquidity_in",
        "fee_liquidity_not_in",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    id_not = sgqlc.types.Field(ID, graphql_name="id_not")
    id_gt = sgqlc.types.Field(ID, graphql_name="id_gt")
    id_lt = sgqlc.types.Field(ID, graphql_name="id_lt")
    id_gte = sgqlc.types.Field(ID, graphql_name="id_gte")
    id_lte = sgqlc.types.Field(ID, graphql_name="id_lte")
    id_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_in"
    )
    id_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_not_in"
    )
    transaction = sgqlc.types.Field(String, graphql_name="transaction")
    transaction_not = sgqlc.types.Field(String, graphql_name="transaction_not")
    transaction_gt = sgqlc.types.Field(String, graphql_name="transaction_gt")
    transaction_lt = sgqlc.types.Field(String, graphql_name="transaction_lt")
    transaction_gte = sgqlc.types.Field(String, graphql_name="transaction_gte")
    transaction_lte = sgqlc.types.Field(String, graphql_name="transaction_lte")
    transaction_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="transaction_in"
    )
    transaction_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="transaction_not_in",
    )
    transaction_contains = sgqlc.types.Field(
        String, graphql_name="transaction_contains"
    )
    transaction_not_contains = sgqlc.types.Field(
        String, graphql_name="transaction_not_contains"
    )
    transaction_starts_with = sgqlc.types.Field(
        String, graphql_name="transaction_starts_with"
    )
    transaction_not_starts_with = sgqlc.types.Field(
        String, graphql_name="transaction_not_starts_with"
    )
    transaction_ends_with = sgqlc.types.Field(
        String, graphql_name="transaction_ends_with"
    )
    transaction_not_ends_with = sgqlc.types.Field(
        String, graphql_name="transaction_not_ends_with"
    )
    timestamp = sgqlc.types.Field(BigInt, graphql_name="timestamp")
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name="timestamp_not")
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name="timestamp_gt")
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name="timestamp_lt")
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name="timestamp_gte")
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name="timestamp_lte")
    timestamp_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="timestamp_in"
    )
    timestamp_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="timestamp_not_in",
    )
    pair = sgqlc.types.Field(String, graphql_name="pair")
    pair_not = sgqlc.types.Field(String, graphql_name="pair_not")
    pair_gt = sgqlc.types.Field(String, graphql_name="pair_gt")
    pair_lt = sgqlc.types.Field(String, graphql_name="pair_lt")
    pair_gte = sgqlc.types.Field(String, graphql_name="pair_gte")
    pair_lte = sgqlc.types.Field(String, graphql_name="pair_lte")
    pair_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="pair_in"
    )
    pair_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="pair_not_in"
    )
    pair_contains = sgqlc.types.Field(String, graphql_name="pair_contains")
    pair_not_contains = sgqlc.types.Field(String, graphql_name="pair_not_contains")
    pair_starts_with = sgqlc.types.Field(String, graphql_name="pair_starts_with")
    pair_not_starts_with = sgqlc.types.Field(
        String, graphql_name="pair_not_starts_with"
    )
    pair_ends_with = sgqlc.types.Field(String, graphql_name="pair_ends_with")
    pair_not_ends_with = sgqlc.types.Field(String, graphql_name="pair_not_ends_with")
    to = sgqlc.types.Field(Bytes, graphql_name="to")
    to_not = sgqlc.types.Field(Bytes, graphql_name="to_not")
    to_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name="to_in"
    )
    to_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name="to_not_in"
    )
    to_contains = sgqlc.types.Field(Bytes, graphql_name="to_contains")
    to_not_contains = sgqlc.types.Field(Bytes, graphql_name="to_not_contains")
    liquidity = sgqlc.types.Field(BigDecimal, graphql_name="liquidity")
    liquidity_not = sgqlc.types.Field(BigDecimal, graphql_name="liquidity_not")
    liquidity_gt = sgqlc.types.Field(BigDecimal, graphql_name="liquidity_gt")
    liquidity_lt = sgqlc.types.Field(BigDecimal, graphql_name="liquidity_lt")
    liquidity_gte = sgqlc.types.Field(BigDecimal, graphql_name="liquidity_gte")
    liquidity_lte = sgqlc.types.Field(BigDecimal, graphql_name="liquidity_lte")
    liquidity_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="liquidity_in",
    )
    liquidity_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="liquidity_not_in",
    )
    sender = sgqlc.types.Field(Bytes, graphql_name="sender")
    sender_not = sgqlc.types.Field(Bytes, graphql_name="sender_not")
    sender_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name="sender_in"
    )
    sender_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name="sender_not_in"
    )
    sender_contains = sgqlc.types.Field(Bytes, graphql_name="sender_contains")
    sender_not_contains = sgqlc.types.Field(Bytes, graphql_name="sender_not_contains")
    amount0 = sgqlc.types.Field(BigDecimal, graphql_name="amount0")
    amount0_not = sgqlc.types.Field(BigDecimal, graphql_name="amount0_not")
    amount0_gt = sgqlc.types.Field(BigDecimal, graphql_name="amount0_gt")
    amount0_lt = sgqlc.types.Field(BigDecimal, graphql_name="amount0_lt")
    amount0_gte = sgqlc.types.Field(BigDecimal, graphql_name="amount0_gte")
    amount0_lte = sgqlc.types.Field(BigDecimal, graphql_name="amount0_lte")
    amount0_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name="amount0_in"
    )
    amount0_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="amount0_not_in",
    )
    amount1 = sgqlc.types.Field(BigDecimal, graphql_name="amount1")
    amount1_not = sgqlc.types.Field(BigDecimal, graphql_name="amount1_not")
    amount1_gt = sgqlc.types.Field(BigDecimal, graphql_name="amount1_gt")
    amount1_lt = sgqlc.types.Field(BigDecimal, graphql_name="amount1_lt")
    amount1_gte = sgqlc.types.Field(BigDecimal, graphql_name="amount1_gte")
    amount1_lte = sgqlc.types.Field(BigDecimal, graphql_name="amount1_lte")
    amount1_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name="amount1_in"
    )
    amount1_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="amount1_not_in",
    )
    log_index = sgqlc.types.Field(BigInt, graphql_name="logIndex")
    log_index_not = sgqlc.types.Field(BigInt, graphql_name="logIndex_not")
    log_index_gt = sgqlc.types.Field(BigInt, graphql_name="logIndex_gt")
    log_index_lt = sgqlc.types.Field(BigInt, graphql_name="logIndex_lt")
    log_index_gte = sgqlc.types.Field(BigInt, graphql_name="logIndex_gte")
    log_index_lte = sgqlc.types.Field(BigInt, graphql_name="logIndex_lte")
    log_index_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="logIndex_in"
    )
    log_index_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="logIndex_not_in",
    )
    amount_usd = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD")
    amount_usd_not = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD_not")
    amount_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD_gt")
    amount_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD_lt")
    amount_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD_gte")
    amount_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD_lte")
    amount_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="amountUSD_in",
    )
    amount_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="amountUSD_not_in",
    )
    fee_to = sgqlc.types.Field(Bytes, graphql_name="feeTo")
    fee_to_not = sgqlc.types.Field(Bytes, graphql_name="feeTo_not")
    fee_to_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name="feeTo_in"
    )
    fee_to_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name="feeTo_not_in"
    )
    fee_to_contains = sgqlc.types.Field(Bytes, graphql_name="feeTo_contains")
    fee_to_not_contains = sgqlc.types.Field(Bytes, graphql_name="feeTo_not_contains")
    fee_liquidity = sgqlc.types.Field(BigDecimal, graphql_name="feeLiquidity")
    fee_liquidity_not = sgqlc.types.Field(BigDecimal, graphql_name="feeLiquidity_not")
    fee_liquidity_gt = sgqlc.types.Field(BigDecimal, graphql_name="feeLiquidity_gt")
    fee_liquidity_lt = sgqlc.types.Field(BigDecimal, graphql_name="feeLiquidity_lt")
    fee_liquidity_gte = sgqlc.types.Field(BigDecimal, graphql_name="feeLiquidity_gte")
    fee_liquidity_lte = sgqlc.types.Field(BigDecimal, graphql_name="feeLiquidity_lte")
    fee_liquidity_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="feeLiquidity_in",
    )
    fee_liquidity_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="feeLiquidity_not_in",
    )


class PairDayData_filter(sgqlc.types.Input):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "id_not",
        "id_gt",
        "id_lt",
        "id_gte",
        "id_lte",
        "id_in",
        "id_not_in",
        "date",
        "date_not",
        "date_gt",
        "date_lt",
        "date_gte",
        "date_lte",
        "date_in",
        "date_not_in",
        "pair_address",
        "pair_address_not",
        "pair_address_in",
        "pair_address_not_in",
        "pair_address_contains",
        "pair_address_not_contains",
        "token0",
        "token0_not",
        "token0_gt",
        "token0_lt",
        "token0_gte",
        "token0_lte",
        "token0_in",
        "token0_not_in",
        "token0_contains",
        "token0_not_contains",
        "token0_starts_with",
        "token0_not_starts_with",
        "token0_ends_with",
        "token0_not_ends_with",
        "token1",
        "token1_not",
        "token1_gt",
        "token1_lt",
        "token1_gte",
        "token1_lte",
        "token1_in",
        "token1_not_in",
        "token1_contains",
        "token1_not_contains",
        "token1_starts_with",
        "token1_not_starts_with",
        "token1_ends_with",
        "token1_not_ends_with",
        "reserve0",
        "reserve0_not",
        "reserve0_gt",
        "reserve0_lt",
        "reserve0_gte",
        "reserve0_lte",
        "reserve0_in",
        "reserve0_not_in",
        "reserve1",
        "reserve1_not",
        "reserve1_gt",
        "reserve1_lt",
        "reserve1_gte",
        "reserve1_lte",
        "reserve1_in",
        "reserve1_not_in",
        "total_supply",
        "total_supply_not",
        "total_supply_gt",
        "total_supply_lt",
        "total_supply_gte",
        "total_supply_lte",
        "total_supply_in",
        "total_supply_not_in",
        "reserve_usd",
        "reserve_usd_not",
        "reserve_usd_gt",
        "reserve_usd_lt",
        "reserve_usd_gte",
        "reserve_usd_lte",
        "reserve_usd_in",
        "reserve_usd_not_in",
        "daily_volume_token0",
        "daily_volume_token0_not",
        "daily_volume_token0_gt",
        "daily_volume_token0_lt",
        "daily_volume_token0_gte",
        "daily_volume_token0_lte",
        "daily_volume_token0_in",
        "daily_volume_token0_not_in",
        "daily_volume_token1",
        "daily_volume_token1_not",
        "daily_volume_token1_gt",
        "daily_volume_token1_lt",
        "daily_volume_token1_gte",
        "daily_volume_token1_lte",
        "daily_volume_token1_in",
        "daily_volume_token1_not_in",
        "daily_volume_usd",
        "daily_volume_usd_not",
        "daily_volume_usd_gt",
        "daily_volume_usd_lt",
        "daily_volume_usd_gte",
        "daily_volume_usd_lte",
        "daily_volume_usd_in",
        "daily_volume_usd_not_in",
        "daily_txns",
        "daily_txns_not",
        "daily_txns_gt",
        "daily_txns_lt",
        "daily_txns_gte",
        "daily_txns_lte",
        "daily_txns_in",
        "daily_txns_not_in",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    id_not = sgqlc.types.Field(ID, graphql_name="id_not")
    id_gt = sgqlc.types.Field(ID, graphql_name="id_gt")
    id_lt = sgqlc.types.Field(ID, graphql_name="id_lt")
    id_gte = sgqlc.types.Field(ID, graphql_name="id_gte")
    id_lte = sgqlc.types.Field(ID, graphql_name="id_lte")
    id_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_in"
    )
    id_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_not_in"
    )
    date = sgqlc.types.Field(Int, graphql_name="date")
    date_not = sgqlc.types.Field(Int, graphql_name="date_not")
    date_gt = sgqlc.types.Field(Int, graphql_name="date_gt")
    date_lt = sgqlc.types.Field(Int, graphql_name="date_lt")
    date_gte = sgqlc.types.Field(Int, graphql_name="date_gte")
    date_lte = sgqlc.types.Field(Int, graphql_name="date_lte")
    date_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="date_in"
    )
    date_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="date_not_in"
    )
    pair_address = sgqlc.types.Field(Bytes, graphql_name="pairAddress")
    pair_address_not = sgqlc.types.Field(Bytes, graphql_name="pairAddress_not")
    pair_address_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name="pairAddress_in"
    )
    pair_address_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Bytes)),
        graphql_name="pairAddress_not_in",
    )
    pair_address_contains = sgqlc.types.Field(
        Bytes, graphql_name="pairAddress_contains"
    )
    pair_address_not_contains = sgqlc.types.Field(
        Bytes, graphql_name="pairAddress_not_contains"
    )
    token0 = sgqlc.types.Field(String, graphql_name="token0")
    token0_not = sgqlc.types.Field(String, graphql_name="token0_not")
    token0_gt = sgqlc.types.Field(String, graphql_name="token0_gt")
    token0_lt = sgqlc.types.Field(String, graphql_name="token0_lt")
    token0_gte = sgqlc.types.Field(String, graphql_name="token0_gte")
    token0_lte = sgqlc.types.Field(String, graphql_name="token0_lte")
    token0_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="token0_in"
    )
    token0_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="token0_not_in"
    )
    token0_contains = sgqlc.types.Field(String, graphql_name="token0_contains")
    token0_not_contains = sgqlc.types.Field(String, graphql_name="token0_not_contains")
    token0_starts_with = sgqlc.types.Field(String, graphql_name="token0_starts_with")
    token0_not_starts_with = sgqlc.types.Field(
        String, graphql_name="token0_not_starts_with"
    )
    token0_ends_with = sgqlc.types.Field(String, graphql_name="token0_ends_with")
    token0_not_ends_with = sgqlc.types.Field(
        String, graphql_name="token0_not_ends_with"
    )
    token1 = sgqlc.types.Field(String, graphql_name="token1")
    token1_not = sgqlc.types.Field(String, graphql_name="token1_not")
    token1_gt = sgqlc.types.Field(String, graphql_name="token1_gt")
    token1_lt = sgqlc.types.Field(String, graphql_name="token1_lt")
    token1_gte = sgqlc.types.Field(String, graphql_name="token1_gte")
    token1_lte = sgqlc.types.Field(String, graphql_name="token1_lte")
    token1_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="token1_in"
    )
    token1_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="token1_not_in"
    )
    token1_contains = sgqlc.types.Field(String, graphql_name="token1_contains")
    token1_not_contains = sgqlc.types.Field(String, graphql_name="token1_not_contains")
    token1_starts_with = sgqlc.types.Field(String, graphql_name="token1_starts_with")
    token1_not_starts_with = sgqlc.types.Field(
        String, graphql_name="token1_not_starts_with"
    )
    token1_ends_with = sgqlc.types.Field(String, graphql_name="token1_ends_with")
    token1_not_ends_with = sgqlc.types.Field(
        String, graphql_name="token1_not_ends_with"
    )
    reserve0 = sgqlc.types.Field(BigDecimal, graphql_name="reserve0")
    reserve0_not = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_not")
    reserve0_gt = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_gt")
    reserve0_lt = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_lt")
    reserve0_gte = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_gte")
    reserve0_lte = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_lte")
    reserve0_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserve0_in",
    )
    reserve0_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserve0_not_in",
    )
    reserve1 = sgqlc.types.Field(BigDecimal, graphql_name="reserve1")
    reserve1_not = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_not")
    reserve1_gt = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_gt")
    reserve1_lt = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_lt")
    reserve1_gte = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_gte")
    reserve1_lte = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_lte")
    reserve1_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserve1_in",
    )
    reserve1_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserve1_not_in",
    )
    total_supply = sgqlc.types.Field(BigDecimal, graphql_name="totalSupply")
    total_supply_not = sgqlc.types.Field(BigDecimal, graphql_name="totalSupply_not")
    total_supply_gt = sgqlc.types.Field(BigDecimal, graphql_name="totalSupply_gt")
    total_supply_lt = sgqlc.types.Field(BigDecimal, graphql_name="totalSupply_lt")
    total_supply_gte = sgqlc.types.Field(BigDecimal, graphql_name="totalSupply_gte")
    total_supply_lte = sgqlc.types.Field(BigDecimal, graphql_name="totalSupply_lte")
    total_supply_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalSupply_in",
    )
    total_supply_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalSupply_not_in",
    )
    reserve_usd = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD")
    reserve_usd_not = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_not")
    reserve_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_gt")
    reserve_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_lt")
    reserve_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_gte")
    reserve_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_lte")
    reserve_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserveUSD_in",
    )
    reserve_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserveUSD_not_in",
    )
    daily_volume_token0 = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeToken0"
    )
    daily_volume_token0_not = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeToken0_not"
    )
    daily_volume_token0_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeToken0_gt"
    )
    daily_volume_token0_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeToken0_lt"
    )
    daily_volume_token0_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeToken0_gte"
    )
    daily_volume_token0_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeToken0_lte"
    )
    daily_volume_token0_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="dailyVolumeToken0_in",
    )
    daily_volume_token0_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="dailyVolumeToken0_not_in",
    )
    daily_volume_token1 = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeToken1"
    )
    daily_volume_token1_not = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeToken1_not"
    )
    daily_volume_token1_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeToken1_gt"
    )
    daily_volume_token1_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeToken1_lt"
    )
    daily_volume_token1_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeToken1_gte"
    )
    daily_volume_token1_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeToken1_lte"
    )
    daily_volume_token1_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="dailyVolumeToken1_in",
    )
    daily_volume_token1_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="dailyVolumeToken1_not_in",
    )
    daily_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name="dailyVolumeUSD")
    daily_volume_usd_not = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUSD_not"
    )
    daily_volume_usd_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUSD_gt"
    )
    daily_volume_usd_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUSD_lt"
    )
    daily_volume_usd_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUSD_gte"
    )
    daily_volume_usd_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUSD_lte"
    )
    daily_volume_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="dailyVolumeUSD_in",
    )
    daily_volume_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="dailyVolumeUSD_not_in",
    )
    daily_txns = sgqlc.types.Field(BigInt, graphql_name="dailyTxns")
    daily_txns_not = sgqlc.types.Field(BigInt, graphql_name="dailyTxns_not")
    daily_txns_gt = sgqlc.types.Field(BigInt, graphql_name="dailyTxns_gt")
    daily_txns_lt = sgqlc.types.Field(BigInt, graphql_name="dailyTxns_lt")
    daily_txns_gte = sgqlc.types.Field(BigInt, graphql_name="dailyTxns_gte")
    daily_txns_lte = sgqlc.types.Field(BigInt, graphql_name="dailyTxns_lte")
    daily_txns_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="dailyTxns_in"
    )
    daily_txns_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="dailyTxns_not_in",
    )


class PairHourData_filter(sgqlc.types.Input):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "id_not",
        "id_gt",
        "id_lt",
        "id_gte",
        "id_lte",
        "id_in",
        "id_not_in",
        "hour_start_unix",
        "hour_start_unix_not",
        "hour_start_unix_gt",
        "hour_start_unix_lt",
        "hour_start_unix_gte",
        "hour_start_unix_lte",
        "hour_start_unix_in",
        "hour_start_unix_not_in",
        "pair",
        "pair_not",
        "pair_gt",
        "pair_lt",
        "pair_gte",
        "pair_lte",
        "pair_in",
        "pair_not_in",
        "pair_contains",
        "pair_not_contains",
        "pair_starts_with",
        "pair_not_starts_with",
        "pair_ends_with",
        "pair_not_ends_with",
        "reserve0",
        "reserve0_not",
        "reserve0_gt",
        "reserve0_lt",
        "reserve0_gte",
        "reserve0_lte",
        "reserve0_in",
        "reserve0_not_in",
        "reserve1",
        "reserve1_not",
        "reserve1_gt",
        "reserve1_lt",
        "reserve1_gte",
        "reserve1_lte",
        "reserve1_in",
        "reserve1_not_in",
        "reserve_usd",
        "reserve_usd_not",
        "reserve_usd_gt",
        "reserve_usd_lt",
        "reserve_usd_gte",
        "reserve_usd_lte",
        "reserve_usd_in",
        "reserve_usd_not_in",
        "hourly_volume_token0",
        "hourly_volume_token0_not",
        "hourly_volume_token0_gt",
        "hourly_volume_token0_lt",
        "hourly_volume_token0_gte",
        "hourly_volume_token0_lte",
        "hourly_volume_token0_in",
        "hourly_volume_token0_not_in",
        "hourly_volume_token1",
        "hourly_volume_token1_not",
        "hourly_volume_token1_gt",
        "hourly_volume_token1_lt",
        "hourly_volume_token1_gte",
        "hourly_volume_token1_lte",
        "hourly_volume_token1_in",
        "hourly_volume_token1_not_in",
        "hourly_volume_usd",
        "hourly_volume_usd_not",
        "hourly_volume_usd_gt",
        "hourly_volume_usd_lt",
        "hourly_volume_usd_gte",
        "hourly_volume_usd_lte",
        "hourly_volume_usd_in",
        "hourly_volume_usd_not_in",
        "hourly_txns",
        "hourly_txns_not",
        "hourly_txns_gt",
        "hourly_txns_lt",
        "hourly_txns_gte",
        "hourly_txns_lte",
        "hourly_txns_in",
        "hourly_txns_not_in",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    id_not = sgqlc.types.Field(ID, graphql_name="id_not")
    id_gt = sgqlc.types.Field(ID, graphql_name="id_gt")
    id_lt = sgqlc.types.Field(ID, graphql_name="id_lt")
    id_gte = sgqlc.types.Field(ID, graphql_name="id_gte")
    id_lte = sgqlc.types.Field(ID, graphql_name="id_lte")
    id_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_in"
    )
    id_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_not_in"
    )
    hour_start_unix = sgqlc.types.Field(Int, graphql_name="hourStartUnix")
    hour_start_unix_not = sgqlc.types.Field(Int, graphql_name="hourStartUnix_not")
    hour_start_unix_gt = sgqlc.types.Field(Int, graphql_name="hourStartUnix_gt")
    hour_start_unix_lt = sgqlc.types.Field(Int, graphql_name="hourStartUnix_lt")
    hour_start_unix_gte = sgqlc.types.Field(Int, graphql_name="hourStartUnix_gte")
    hour_start_unix_lte = sgqlc.types.Field(Int, graphql_name="hourStartUnix_lte")
    hour_start_unix_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="hourStartUnix_in"
    )
    hour_start_unix_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)),
        graphql_name="hourStartUnix_not_in",
    )
    pair = sgqlc.types.Field(String, graphql_name="pair")
    pair_not = sgqlc.types.Field(String, graphql_name="pair_not")
    pair_gt = sgqlc.types.Field(String, graphql_name="pair_gt")
    pair_lt = sgqlc.types.Field(String, graphql_name="pair_lt")
    pair_gte = sgqlc.types.Field(String, graphql_name="pair_gte")
    pair_lte = sgqlc.types.Field(String, graphql_name="pair_lte")
    pair_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="pair_in"
    )
    pair_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="pair_not_in"
    )
    pair_contains = sgqlc.types.Field(String, graphql_name="pair_contains")
    pair_not_contains = sgqlc.types.Field(String, graphql_name="pair_not_contains")
    pair_starts_with = sgqlc.types.Field(String, graphql_name="pair_starts_with")
    pair_not_starts_with = sgqlc.types.Field(
        String, graphql_name="pair_not_starts_with"
    )
    pair_ends_with = sgqlc.types.Field(String, graphql_name="pair_ends_with")
    pair_not_ends_with = sgqlc.types.Field(String, graphql_name="pair_not_ends_with")
    reserve0 = sgqlc.types.Field(BigDecimal, graphql_name="reserve0")
    reserve0_not = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_not")
    reserve0_gt = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_gt")
    reserve0_lt = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_lt")
    reserve0_gte = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_gte")
    reserve0_lte = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_lte")
    reserve0_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserve0_in",
    )
    reserve0_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserve0_not_in",
    )
    reserve1 = sgqlc.types.Field(BigDecimal, graphql_name="reserve1")
    reserve1_not = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_not")
    reserve1_gt = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_gt")
    reserve1_lt = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_lt")
    reserve1_gte = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_gte")
    reserve1_lte = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_lte")
    reserve1_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserve1_in",
    )
    reserve1_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserve1_not_in",
    )
    reserve_usd = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD")
    reserve_usd_not = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_not")
    reserve_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_gt")
    reserve_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_lt")
    reserve_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_gte")
    reserve_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_lte")
    reserve_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserveUSD_in",
    )
    reserve_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserveUSD_not_in",
    )
    hourly_volume_token0 = sgqlc.types.Field(
        BigDecimal, graphql_name="hourlyVolumeToken0"
    )
    hourly_volume_token0_not = sgqlc.types.Field(
        BigDecimal, graphql_name="hourlyVolumeToken0_not"
    )
    hourly_volume_token0_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="hourlyVolumeToken0_gt"
    )
    hourly_volume_token0_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="hourlyVolumeToken0_lt"
    )
    hourly_volume_token0_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="hourlyVolumeToken0_gte"
    )
    hourly_volume_token0_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="hourlyVolumeToken0_lte"
    )
    hourly_volume_token0_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="hourlyVolumeToken0_in",
    )
    hourly_volume_token0_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="hourlyVolumeToken0_not_in",
    )
    hourly_volume_token1 = sgqlc.types.Field(
        BigDecimal, graphql_name="hourlyVolumeToken1"
    )
    hourly_volume_token1_not = sgqlc.types.Field(
        BigDecimal, graphql_name="hourlyVolumeToken1_not"
    )
    hourly_volume_token1_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="hourlyVolumeToken1_gt"
    )
    hourly_volume_token1_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="hourlyVolumeToken1_lt"
    )
    hourly_volume_token1_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="hourlyVolumeToken1_gte"
    )
    hourly_volume_token1_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="hourlyVolumeToken1_lte"
    )
    hourly_volume_token1_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="hourlyVolumeToken1_in",
    )
    hourly_volume_token1_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="hourlyVolumeToken1_not_in",
    )
    hourly_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name="hourlyVolumeUSD")
    hourly_volume_usd_not = sgqlc.types.Field(
        BigDecimal, graphql_name="hourlyVolumeUSD_not"
    )
    hourly_volume_usd_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="hourlyVolumeUSD_gt"
    )
    hourly_volume_usd_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="hourlyVolumeUSD_lt"
    )
    hourly_volume_usd_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="hourlyVolumeUSD_gte"
    )
    hourly_volume_usd_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="hourlyVolumeUSD_lte"
    )
    hourly_volume_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="hourlyVolumeUSD_in",
    )
    hourly_volume_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="hourlyVolumeUSD_not_in",
    )
    hourly_txns = sgqlc.types.Field(BigInt, graphql_name="hourlyTxns")
    hourly_txns_not = sgqlc.types.Field(BigInt, graphql_name="hourlyTxns_not")
    hourly_txns_gt = sgqlc.types.Field(BigInt, graphql_name="hourlyTxns_gt")
    hourly_txns_lt = sgqlc.types.Field(BigInt, graphql_name="hourlyTxns_lt")
    hourly_txns_gte = sgqlc.types.Field(BigInt, graphql_name="hourlyTxns_gte")
    hourly_txns_lte = sgqlc.types.Field(BigInt, graphql_name="hourlyTxns_lte")
    hourly_txns_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="hourlyTxns_in"
    )
    hourly_txns_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="hourlyTxns_not_in",
    )


class Pair_filter(sgqlc.types.Input):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "id_not",
        "id_gt",
        "id_lt",
        "id_gte",
        "id_lte",
        "id_in",
        "id_not_in",
        "token0",
        "token0_not",
        "token0_gt",
        "token0_lt",
        "token0_gte",
        "token0_lte",
        "token0_in",
        "token0_not_in",
        "token0_contains",
        "token0_not_contains",
        "token0_starts_with",
        "token0_not_starts_with",
        "token0_ends_with",
        "token0_not_ends_with",
        "token1",
        "token1_not",
        "token1_gt",
        "token1_lt",
        "token1_gte",
        "token1_lte",
        "token1_in",
        "token1_not_in",
        "token1_contains",
        "token1_not_contains",
        "token1_starts_with",
        "token1_not_starts_with",
        "token1_ends_with",
        "token1_not_ends_with",
        "reserve0",
        "reserve0_not",
        "reserve0_gt",
        "reserve0_lt",
        "reserve0_gte",
        "reserve0_lte",
        "reserve0_in",
        "reserve0_not_in",
        "reserve1",
        "reserve1_not",
        "reserve1_gt",
        "reserve1_lt",
        "reserve1_gte",
        "reserve1_lte",
        "reserve1_in",
        "reserve1_not_in",
        "total_supply",
        "total_supply_not",
        "total_supply_gt",
        "total_supply_lt",
        "total_supply_gte",
        "total_supply_lte",
        "total_supply_in",
        "total_supply_not_in",
        "reserve_eth",
        "reserve_eth_not",
        "reserve_eth_gt",
        "reserve_eth_lt",
        "reserve_eth_gte",
        "reserve_eth_lte",
        "reserve_eth_in",
        "reserve_eth_not_in",
        "reserve_usd",
        "reserve_usd_not",
        "reserve_usd_gt",
        "reserve_usd_lt",
        "reserve_usd_gte",
        "reserve_usd_lte",
        "reserve_usd_in",
        "reserve_usd_not_in",
        "tracked_reserve_eth",
        "tracked_reserve_eth_not",
        "tracked_reserve_eth_gt",
        "tracked_reserve_eth_lt",
        "tracked_reserve_eth_gte",
        "tracked_reserve_eth_lte",
        "tracked_reserve_eth_in",
        "tracked_reserve_eth_not_in",
        "token0_price",
        "token0_price_not",
        "token0_price_gt",
        "token0_price_lt",
        "token0_price_gte",
        "token0_price_lte",
        "token0_price_in",
        "token0_price_not_in",
        "token1_price",
        "token1_price_not",
        "token1_price_gt",
        "token1_price_lt",
        "token1_price_gte",
        "token1_price_lte",
        "token1_price_in",
        "token1_price_not_in",
        "volume_token0",
        "volume_token0_not",
        "volume_token0_gt",
        "volume_token0_lt",
        "volume_token0_gte",
        "volume_token0_lte",
        "volume_token0_in",
        "volume_token0_not_in",
        "volume_token1",
        "volume_token1_not",
        "volume_token1_gt",
        "volume_token1_lt",
        "volume_token1_gte",
        "volume_token1_lte",
        "volume_token1_in",
        "volume_token1_not_in",
        "volume_usd",
        "volume_usd_not",
        "volume_usd_gt",
        "volume_usd_lt",
        "volume_usd_gte",
        "volume_usd_lte",
        "volume_usd_in",
        "volume_usd_not_in",
        "untracked_volume_usd",
        "untracked_volume_usd_not",
        "untracked_volume_usd_gt",
        "untracked_volume_usd_lt",
        "untracked_volume_usd_gte",
        "untracked_volume_usd_lte",
        "untracked_volume_usd_in",
        "untracked_volume_usd_not_in",
        "tx_count",
        "tx_count_not",
        "tx_count_gt",
        "tx_count_lt",
        "tx_count_gte",
        "tx_count_lte",
        "tx_count_in",
        "tx_count_not_in",
        "created_at_timestamp",
        "created_at_timestamp_not",
        "created_at_timestamp_gt",
        "created_at_timestamp_lt",
        "created_at_timestamp_gte",
        "created_at_timestamp_lte",
        "created_at_timestamp_in",
        "created_at_timestamp_not_in",
        "created_at_block_number",
        "created_at_block_number_not",
        "created_at_block_number_gt",
        "created_at_block_number_lt",
        "created_at_block_number_gte",
        "created_at_block_number_lte",
        "created_at_block_number_in",
        "created_at_block_number_not_in",
        "liquidity_provider_count",
        "liquidity_provider_count_not",
        "liquidity_provider_count_gt",
        "liquidity_provider_count_lt",
        "liquidity_provider_count_gte",
        "liquidity_provider_count_lte",
        "liquidity_provider_count_in",
        "liquidity_provider_count_not_in",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    id_not = sgqlc.types.Field(ID, graphql_name="id_not")
    id_gt = sgqlc.types.Field(ID, graphql_name="id_gt")
    id_lt = sgqlc.types.Field(ID, graphql_name="id_lt")
    id_gte = sgqlc.types.Field(ID, graphql_name="id_gte")
    id_lte = sgqlc.types.Field(ID, graphql_name="id_lte")
    id_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_in"
    )
    id_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_not_in"
    )
    token0 = sgqlc.types.Field(String, graphql_name="token0")
    token0_not = sgqlc.types.Field(String, graphql_name="token0_not")
    token0_gt = sgqlc.types.Field(String, graphql_name="token0_gt")
    token0_lt = sgqlc.types.Field(String, graphql_name="token0_lt")
    token0_gte = sgqlc.types.Field(String, graphql_name="token0_gte")
    token0_lte = sgqlc.types.Field(String, graphql_name="token0_lte")
    token0_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="token0_in"
    )
    token0_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="token0_not_in"
    )
    token0_contains = sgqlc.types.Field(String, graphql_name="token0_contains")
    token0_not_contains = sgqlc.types.Field(String, graphql_name="token0_not_contains")
    token0_starts_with = sgqlc.types.Field(String, graphql_name="token0_starts_with")
    token0_not_starts_with = sgqlc.types.Field(
        String, graphql_name="token0_not_starts_with"
    )
    token0_ends_with = sgqlc.types.Field(String, graphql_name="token0_ends_with")
    token0_not_ends_with = sgqlc.types.Field(
        String, graphql_name="token0_not_ends_with"
    )
    token1 = sgqlc.types.Field(String, graphql_name="token1")
    token1_not = sgqlc.types.Field(String, graphql_name="token1_not")
    token1_gt = sgqlc.types.Field(String, graphql_name="token1_gt")
    token1_lt = sgqlc.types.Field(String, graphql_name="token1_lt")
    token1_gte = sgqlc.types.Field(String, graphql_name="token1_gte")
    token1_lte = sgqlc.types.Field(String, graphql_name="token1_lte")
    token1_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="token1_in"
    )
    token1_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="token1_not_in"
    )
    token1_contains = sgqlc.types.Field(String, graphql_name="token1_contains")
    token1_not_contains = sgqlc.types.Field(String, graphql_name="token1_not_contains")
    token1_starts_with = sgqlc.types.Field(String, graphql_name="token1_starts_with")
    token1_not_starts_with = sgqlc.types.Field(
        String, graphql_name="token1_not_starts_with"
    )
    token1_ends_with = sgqlc.types.Field(String, graphql_name="token1_ends_with")
    token1_not_ends_with = sgqlc.types.Field(
        String, graphql_name="token1_not_ends_with"
    )
    reserve0 = sgqlc.types.Field(BigDecimal, graphql_name="reserve0")
    reserve0_not = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_not")
    reserve0_gt = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_gt")
    reserve0_lt = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_lt")
    reserve0_gte = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_gte")
    reserve0_lte = sgqlc.types.Field(BigDecimal, graphql_name="reserve0_lte")
    reserve0_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserve0_in",
    )
    reserve0_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserve0_not_in",
    )
    reserve1 = sgqlc.types.Field(BigDecimal, graphql_name="reserve1")
    reserve1_not = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_not")
    reserve1_gt = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_gt")
    reserve1_lt = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_lt")
    reserve1_gte = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_gte")
    reserve1_lte = sgqlc.types.Field(BigDecimal, graphql_name="reserve1_lte")
    reserve1_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserve1_in",
    )
    reserve1_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserve1_not_in",
    )
    total_supply = sgqlc.types.Field(BigDecimal, graphql_name="totalSupply")
    total_supply_not = sgqlc.types.Field(BigDecimal, graphql_name="totalSupply_not")
    total_supply_gt = sgqlc.types.Field(BigDecimal, graphql_name="totalSupply_gt")
    total_supply_lt = sgqlc.types.Field(BigDecimal, graphql_name="totalSupply_lt")
    total_supply_gte = sgqlc.types.Field(BigDecimal, graphql_name="totalSupply_gte")
    total_supply_lte = sgqlc.types.Field(BigDecimal, graphql_name="totalSupply_lte")
    total_supply_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalSupply_in",
    )
    total_supply_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalSupply_not_in",
    )
    reserve_eth = sgqlc.types.Field(BigDecimal, graphql_name="reserveETH")
    reserve_eth_not = sgqlc.types.Field(BigDecimal, graphql_name="reserveETH_not")
    reserve_eth_gt = sgqlc.types.Field(BigDecimal, graphql_name="reserveETH_gt")
    reserve_eth_lt = sgqlc.types.Field(BigDecimal, graphql_name="reserveETH_lt")
    reserve_eth_gte = sgqlc.types.Field(BigDecimal, graphql_name="reserveETH_gte")
    reserve_eth_lte = sgqlc.types.Field(BigDecimal, graphql_name="reserveETH_lte")
    reserve_eth_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserveETH_in",
    )
    reserve_eth_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserveETH_not_in",
    )
    reserve_usd = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD")
    reserve_usd_not = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_not")
    reserve_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_gt")
    reserve_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_lt")
    reserve_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_gte")
    reserve_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name="reserveUSD_lte")
    reserve_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserveUSD_in",
    )
    reserve_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="reserveUSD_not_in",
    )
    tracked_reserve_eth = sgqlc.types.Field(
        BigDecimal, graphql_name="trackedReserveETH"
    )
    tracked_reserve_eth_not = sgqlc.types.Field(
        BigDecimal, graphql_name="trackedReserveETH_not"
    )
    tracked_reserve_eth_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="trackedReserveETH_gt"
    )
    tracked_reserve_eth_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="trackedReserveETH_lt"
    )
    tracked_reserve_eth_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="trackedReserveETH_gte"
    )
    tracked_reserve_eth_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="trackedReserveETH_lte"
    )
    tracked_reserve_eth_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="trackedReserveETH_in",
    )
    tracked_reserve_eth_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="trackedReserveETH_not_in",
    )
    token0_price = sgqlc.types.Field(BigDecimal, graphql_name="token0Price")
    token0_price_not = sgqlc.types.Field(BigDecimal, graphql_name="token0Price_not")
    token0_price_gt = sgqlc.types.Field(BigDecimal, graphql_name="token0Price_gt")
    token0_price_lt = sgqlc.types.Field(BigDecimal, graphql_name="token0Price_lt")
    token0_price_gte = sgqlc.types.Field(BigDecimal, graphql_name="token0Price_gte")
    token0_price_lte = sgqlc.types.Field(BigDecimal, graphql_name="token0Price_lte")
    token0_price_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="token0Price_in",
    )
    token0_price_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="token0Price_not_in",
    )
    token1_price = sgqlc.types.Field(BigDecimal, graphql_name="token1Price")
    token1_price_not = sgqlc.types.Field(BigDecimal, graphql_name="token1Price_not")
    token1_price_gt = sgqlc.types.Field(BigDecimal, graphql_name="token1Price_gt")
    token1_price_lt = sgqlc.types.Field(BigDecimal, graphql_name="token1Price_lt")
    token1_price_gte = sgqlc.types.Field(BigDecimal, graphql_name="token1Price_gte")
    token1_price_lte = sgqlc.types.Field(BigDecimal, graphql_name="token1Price_lte")
    token1_price_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="token1Price_in",
    )
    token1_price_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="token1Price_not_in",
    )
    volume_token0 = sgqlc.types.Field(BigDecimal, graphql_name="volumeToken0")
    volume_token0_not = sgqlc.types.Field(BigDecimal, graphql_name="volumeToken0_not")
    volume_token0_gt = sgqlc.types.Field(BigDecimal, graphql_name="volumeToken0_gt")
    volume_token0_lt = sgqlc.types.Field(BigDecimal, graphql_name="volumeToken0_lt")
    volume_token0_gte = sgqlc.types.Field(BigDecimal, graphql_name="volumeToken0_gte")
    volume_token0_lte = sgqlc.types.Field(BigDecimal, graphql_name="volumeToken0_lte")
    volume_token0_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="volumeToken0_in",
    )
    volume_token0_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="volumeToken0_not_in",
    )
    volume_token1 = sgqlc.types.Field(BigDecimal, graphql_name="volumeToken1")
    volume_token1_not = sgqlc.types.Field(BigDecimal, graphql_name="volumeToken1_not")
    volume_token1_gt = sgqlc.types.Field(BigDecimal, graphql_name="volumeToken1_gt")
    volume_token1_lt = sgqlc.types.Field(BigDecimal, graphql_name="volumeToken1_lt")
    volume_token1_gte = sgqlc.types.Field(BigDecimal, graphql_name="volumeToken1_gte")
    volume_token1_lte = sgqlc.types.Field(BigDecimal, graphql_name="volumeToken1_lte")
    volume_token1_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="volumeToken1_in",
    )
    volume_token1_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="volumeToken1_not_in",
    )
    volume_usd = sgqlc.types.Field(BigDecimal, graphql_name="volumeUSD")
    volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name="volumeUSD_not")
    volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name="volumeUSD_gt")
    volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name="volumeUSD_lt")
    volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name="volumeUSD_gte")
    volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name="volumeUSD_lte")
    volume_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="volumeUSD_in",
    )
    volume_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="volumeUSD_not_in",
    )
    untracked_volume_usd = sgqlc.types.Field(
        BigDecimal, graphql_name="untrackedVolumeUSD"
    )
    untracked_volume_usd_not = sgqlc.types.Field(
        BigDecimal, graphql_name="untrackedVolumeUSD_not"
    )
    untracked_volume_usd_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="untrackedVolumeUSD_gt"
    )
    untracked_volume_usd_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="untrackedVolumeUSD_lt"
    )
    untracked_volume_usd_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="untrackedVolumeUSD_gte"
    )
    untracked_volume_usd_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="untrackedVolumeUSD_lte"
    )
    untracked_volume_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="untrackedVolumeUSD_in",
    )
    untracked_volume_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="untrackedVolumeUSD_not_in",
    )
    tx_count = sgqlc.types.Field(BigInt, graphql_name="txCount")
    tx_count_not = sgqlc.types.Field(BigInt, graphql_name="txCount_not")
    tx_count_gt = sgqlc.types.Field(BigInt, graphql_name="txCount_gt")
    tx_count_lt = sgqlc.types.Field(BigInt, graphql_name="txCount_lt")
    tx_count_gte = sgqlc.types.Field(BigInt, graphql_name="txCount_gte")
    tx_count_lte = sgqlc.types.Field(BigInt, graphql_name="txCount_lte")
    tx_count_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="txCount_in"
    )
    tx_count_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="txCount_not_in"
    )
    created_at_timestamp = sgqlc.types.Field(BigInt, graphql_name="createdAtTimestamp")
    created_at_timestamp_not = sgqlc.types.Field(
        BigInt, graphql_name="createdAtTimestamp_not"
    )
    created_at_timestamp_gt = sgqlc.types.Field(
        BigInt, graphql_name="createdAtTimestamp_gt"
    )
    created_at_timestamp_lt = sgqlc.types.Field(
        BigInt, graphql_name="createdAtTimestamp_lt"
    )
    created_at_timestamp_gte = sgqlc.types.Field(
        BigInt, graphql_name="createdAtTimestamp_gte"
    )
    created_at_timestamp_lte = sgqlc.types.Field(
        BigInt, graphql_name="createdAtTimestamp_lte"
    )
    created_at_timestamp_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="createdAtTimestamp_in",
    )
    created_at_timestamp_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="createdAtTimestamp_not_in",
    )
    created_at_block_number = sgqlc.types.Field(
        BigInt, graphql_name="createdAtBlockNumber"
    )
    created_at_block_number_not = sgqlc.types.Field(
        BigInt, graphql_name="createdAtBlockNumber_not"
    )
    created_at_block_number_gt = sgqlc.types.Field(
        BigInt, graphql_name="createdAtBlockNumber_gt"
    )
    created_at_block_number_lt = sgqlc.types.Field(
        BigInt, graphql_name="createdAtBlockNumber_lt"
    )
    created_at_block_number_gte = sgqlc.types.Field(
        BigInt, graphql_name="createdAtBlockNumber_gte"
    )
    created_at_block_number_lte = sgqlc.types.Field(
        BigInt, graphql_name="createdAtBlockNumber_lte"
    )
    created_at_block_number_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="createdAtBlockNumber_in",
    )
    created_at_block_number_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="createdAtBlockNumber_not_in",
    )
    liquidity_provider_count = sgqlc.types.Field(
        BigInt, graphql_name="liquidityProviderCount"
    )
    liquidity_provider_count_not = sgqlc.types.Field(
        BigInt, graphql_name="liquidityProviderCount_not"
    )
    liquidity_provider_count_gt = sgqlc.types.Field(
        BigInt, graphql_name="liquidityProviderCount_gt"
    )
    liquidity_provider_count_lt = sgqlc.types.Field(
        BigInt, graphql_name="liquidityProviderCount_lt"
    )
    liquidity_provider_count_gte = sgqlc.types.Field(
        BigInt, graphql_name="liquidityProviderCount_gte"
    )
    liquidity_provider_count_lte = sgqlc.types.Field(
        BigInt, graphql_name="liquidityProviderCount_lte"
    )
    liquidity_provider_count_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="liquidityProviderCount_in",
    )
    liquidity_provider_count_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="liquidityProviderCount_not_in",
    )


class Swap_filter(sgqlc.types.Input):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "id_not",
        "id_gt",
        "id_lt",
        "id_gte",
        "id_lte",
        "id_in",
        "id_not_in",
        "transaction",
        "transaction_not",
        "transaction_gt",
        "transaction_lt",
        "transaction_gte",
        "transaction_lte",
        "transaction_in",
        "transaction_not_in",
        "transaction_contains",
        "transaction_not_contains",
        "transaction_starts_with",
        "transaction_not_starts_with",
        "transaction_ends_with",
        "transaction_not_ends_with",
        "timestamp",
        "timestamp_not",
        "timestamp_gt",
        "timestamp_lt",
        "timestamp_gte",
        "timestamp_lte",
        "timestamp_in",
        "timestamp_not_in",
        "pair",
        "pair_not",
        "pair_gt",
        "pair_lt",
        "pair_gte",
        "pair_lte",
        "pair_in",
        "pair_not_in",
        "pair_contains",
        "pair_not_contains",
        "pair_starts_with",
        "pair_not_starts_with",
        "pair_ends_with",
        "pair_not_ends_with",
        "sender",
        "sender_not",
        "sender_in",
        "sender_not_in",
        "sender_contains",
        "sender_not_contains",
        "amount0_in",
        "amount0_in_not",
        "amount0_in_gt",
        "amount0_in_lt",
        "amount0_in_gte",
        "amount0_in_lte",
        "amount0_in_in",
        "amount0_in_not_in",
        "amount1_in",
        "amount1_in_not",
        "amount1_in_gt",
        "amount1_in_lt",
        "amount1_in_gte",
        "amount1_in_lte",
        "amount1_in_in",
        "amount1_in_not_in",
        "amount0_out",
        "amount0_out_not",
        "amount0_out_gt",
        "amount0_out_lt",
        "amount0_out_gte",
        "amount0_out_lte",
        "amount0_out_in",
        "amount0_out_not_in",
        "amount1_out",
        "amount1_out_not",
        "amount1_out_gt",
        "amount1_out_lt",
        "amount1_out_gte",
        "amount1_out_lte",
        "amount1_out_in",
        "amount1_out_not_in",
        "to",
        "to_not",
        "to_in",
        "to_not_in",
        "to_contains",
        "to_not_contains",
        "log_index",
        "log_index_not",
        "log_index_gt",
        "log_index_lt",
        "log_index_gte",
        "log_index_lte",
        "log_index_in",
        "log_index_not_in",
        "amount_usd",
        "amount_usd_not",
        "amount_usd_gt",
        "amount_usd_lt",
        "amount_usd_gte",
        "amount_usd_lte",
        "amount_usd_in",
        "amount_usd_not_in",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    id_not = sgqlc.types.Field(ID, graphql_name="id_not")
    id_gt = sgqlc.types.Field(ID, graphql_name="id_gt")
    id_lt = sgqlc.types.Field(ID, graphql_name="id_lt")
    id_gte = sgqlc.types.Field(ID, graphql_name="id_gte")
    id_lte = sgqlc.types.Field(ID, graphql_name="id_lte")
    id_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_in"
    )
    id_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_not_in"
    )
    transaction = sgqlc.types.Field(String, graphql_name="transaction")
    transaction_not = sgqlc.types.Field(String, graphql_name="transaction_not")
    transaction_gt = sgqlc.types.Field(String, graphql_name="transaction_gt")
    transaction_lt = sgqlc.types.Field(String, graphql_name="transaction_lt")
    transaction_gte = sgqlc.types.Field(String, graphql_name="transaction_gte")
    transaction_lte = sgqlc.types.Field(String, graphql_name="transaction_lte")
    transaction_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="transaction_in"
    )
    transaction_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="transaction_not_in",
    )
    transaction_contains = sgqlc.types.Field(
        String, graphql_name="transaction_contains"
    )
    transaction_not_contains = sgqlc.types.Field(
        String, graphql_name="transaction_not_contains"
    )
    transaction_starts_with = sgqlc.types.Field(
        String, graphql_name="transaction_starts_with"
    )
    transaction_not_starts_with = sgqlc.types.Field(
        String, graphql_name="transaction_not_starts_with"
    )
    transaction_ends_with = sgqlc.types.Field(
        String, graphql_name="transaction_ends_with"
    )
    transaction_not_ends_with = sgqlc.types.Field(
        String, graphql_name="transaction_not_ends_with"
    )
    timestamp = sgqlc.types.Field(BigInt, graphql_name="timestamp")
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name="timestamp_not")
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name="timestamp_gt")
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name="timestamp_lt")
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name="timestamp_gte")
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name="timestamp_lte")
    timestamp_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="timestamp_in"
    )
    timestamp_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="timestamp_not_in",
    )
    pair = sgqlc.types.Field(String, graphql_name="pair")
    pair_not = sgqlc.types.Field(String, graphql_name="pair_not")
    pair_gt = sgqlc.types.Field(String, graphql_name="pair_gt")
    pair_lt = sgqlc.types.Field(String, graphql_name="pair_lt")
    pair_gte = sgqlc.types.Field(String, graphql_name="pair_gte")
    pair_lte = sgqlc.types.Field(String, graphql_name="pair_lte")
    pair_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="pair_in"
    )
    pair_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="pair_not_in"
    )
    pair_contains = sgqlc.types.Field(String, graphql_name="pair_contains")
    pair_not_contains = sgqlc.types.Field(String, graphql_name="pair_not_contains")
    pair_starts_with = sgqlc.types.Field(String, graphql_name="pair_starts_with")
    pair_not_starts_with = sgqlc.types.Field(
        String, graphql_name="pair_not_starts_with"
    )
    pair_ends_with = sgqlc.types.Field(String, graphql_name="pair_ends_with")
    pair_not_ends_with = sgqlc.types.Field(String, graphql_name="pair_not_ends_with")
    sender = sgqlc.types.Field(Bytes, graphql_name="sender")
    sender_not = sgqlc.types.Field(Bytes, graphql_name="sender_not")
    sender_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name="sender_in"
    )
    sender_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name="sender_not_in"
    )
    sender_contains = sgqlc.types.Field(Bytes, graphql_name="sender_contains")
    sender_not_contains = sgqlc.types.Field(Bytes, graphql_name="sender_not_contains")
    amount0_in = sgqlc.types.Field(BigDecimal, graphql_name="amount0In")
    amount0_in_not = sgqlc.types.Field(BigDecimal, graphql_name="amount0In_not")
    amount0_in_gt = sgqlc.types.Field(BigDecimal, graphql_name="amount0In_gt")
    amount0_in_lt = sgqlc.types.Field(BigDecimal, graphql_name="amount0In_lt")
    amount0_in_gte = sgqlc.types.Field(BigDecimal, graphql_name="amount0In_gte")
    amount0_in_lte = sgqlc.types.Field(BigDecimal, graphql_name="amount0In_lte")
    amount0_in_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="amount0In_in",
    )
    amount0_in_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="amount0In_not_in",
    )
    amount1_in = sgqlc.types.Field(BigDecimal, graphql_name="amount1In")
    amount1_in_not = sgqlc.types.Field(BigDecimal, graphql_name="amount1In_not")
    amount1_in_gt = sgqlc.types.Field(BigDecimal, graphql_name="amount1In_gt")
    amount1_in_lt = sgqlc.types.Field(BigDecimal, graphql_name="amount1In_lt")
    amount1_in_gte = sgqlc.types.Field(BigDecimal, graphql_name="amount1In_gte")
    amount1_in_lte = sgqlc.types.Field(BigDecimal, graphql_name="amount1In_lte")
    amount1_in_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="amount1In_in",
    )
    amount1_in_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="amount1In_not_in",
    )
    amount0_out = sgqlc.types.Field(BigDecimal, graphql_name="amount0Out")
    amount0_out_not = sgqlc.types.Field(BigDecimal, graphql_name="amount0Out_not")
    amount0_out_gt = sgqlc.types.Field(BigDecimal, graphql_name="amount0Out_gt")
    amount0_out_lt = sgqlc.types.Field(BigDecimal, graphql_name="amount0Out_lt")
    amount0_out_gte = sgqlc.types.Field(BigDecimal, graphql_name="amount0Out_gte")
    amount0_out_lte = sgqlc.types.Field(BigDecimal, graphql_name="amount0Out_lte")
    amount0_out_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="amount0Out_in",
    )
    amount0_out_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="amount0Out_not_in",
    )
    amount1_out = sgqlc.types.Field(BigDecimal, graphql_name="amount1Out")
    amount1_out_not = sgqlc.types.Field(BigDecimal, graphql_name="amount1Out_not")
    amount1_out_gt = sgqlc.types.Field(BigDecimal, graphql_name="amount1Out_gt")
    amount1_out_lt = sgqlc.types.Field(BigDecimal, graphql_name="amount1Out_lt")
    amount1_out_gte = sgqlc.types.Field(BigDecimal, graphql_name="amount1Out_gte")
    amount1_out_lte = sgqlc.types.Field(BigDecimal, graphql_name="amount1Out_lte")
    amount1_out_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="amount1Out_in",
    )
    amount1_out_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="amount1Out_not_in",
    )
    to = sgqlc.types.Field(Bytes, graphql_name="to")
    to_not = sgqlc.types.Field(Bytes, graphql_name="to_not")
    to_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name="to_in"
    )
    to_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name="to_not_in"
    )
    to_contains = sgqlc.types.Field(Bytes, graphql_name="to_contains")
    to_not_contains = sgqlc.types.Field(Bytes, graphql_name="to_not_contains")
    log_index = sgqlc.types.Field(BigInt, graphql_name="logIndex")
    log_index_not = sgqlc.types.Field(BigInt, graphql_name="logIndex_not")
    log_index_gt = sgqlc.types.Field(BigInt, graphql_name="logIndex_gt")
    log_index_lt = sgqlc.types.Field(BigInt, graphql_name="logIndex_lt")
    log_index_gte = sgqlc.types.Field(BigInt, graphql_name="logIndex_gte")
    log_index_lte = sgqlc.types.Field(BigInt, graphql_name="logIndex_lte")
    log_index_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="logIndex_in"
    )
    log_index_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="logIndex_not_in",
    )
    amount_usd = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD")
    amount_usd_not = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD_not")
    amount_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD_gt")
    amount_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD_lt")
    amount_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD_gte")
    amount_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD_lte")
    amount_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="amountUSD_in",
    )
    amount_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="amountUSD_not_in",
    )


class TokenDayData_filter(sgqlc.types.Input):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "id_not",
        "id_gt",
        "id_lt",
        "id_gte",
        "id_lte",
        "id_in",
        "id_not_in",
        "date",
        "date_not",
        "date_gt",
        "date_lt",
        "date_gte",
        "date_lte",
        "date_in",
        "date_not_in",
        "token",
        "token_not",
        "token_gt",
        "token_lt",
        "token_gte",
        "token_lte",
        "token_in",
        "token_not_in",
        "token_contains",
        "token_not_contains",
        "token_starts_with",
        "token_not_starts_with",
        "token_ends_with",
        "token_not_ends_with",
        "daily_volume_token",
        "daily_volume_token_not",
        "daily_volume_token_gt",
        "daily_volume_token_lt",
        "daily_volume_token_gte",
        "daily_volume_token_lte",
        "daily_volume_token_in",
        "daily_volume_token_not_in",
        "daily_volume_eth",
        "daily_volume_eth_not",
        "daily_volume_eth_gt",
        "daily_volume_eth_lt",
        "daily_volume_eth_gte",
        "daily_volume_eth_lte",
        "daily_volume_eth_in",
        "daily_volume_eth_not_in",
        "daily_volume_usd",
        "daily_volume_usd_not",
        "daily_volume_usd_gt",
        "daily_volume_usd_lt",
        "daily_volume_usd_gte",
        "daily_volume_usd_lte",
        "daily_volume_usd_in",
        "daily_volume_usd_not_in",
        "daily_txns",
        "daily_txns_not",
        "daily_txns_gt",
        "daily_txns_lt",
        "daily_txns_gte",
        "daily_txns_lte",
        "daily_txns_in",
        "daily_txns_not_in",
        "total_liquidity_token",
        "total_liquidity_token_not",
        "total_liquidity_token_gt",
        "total_liquidity_token_lt",
        "total_liquidity_token_gte",
        "total_liquidity_token_lte",
        "total_liquidity_token_in",
        "total_liquidity_token_not_in",
        "total_liquidity_eth",
        "total_liquidity_eth_not",
        "total_liquidity_eth_gt",
        "total_liquidity_eth_lt",
        "total_liquidity_eth_gte",
        "total_liquidity_eth_lte",
        "total_liquidity_eth_in",
        "total_liquidity_eth_not_in",
        "total_liquidity_usd",
        "total_liquidity_usd_not",
        "total_liquidity_usd_gt",
        "total_liquidity_usd_lt",
        "total_liquidity_usd_gte",
        "total_liquidity_usd_lte",
        "total_liquidity_usd_in",
        "total_liquidity_usd_not_in",
        "price_usd",
        "price_usd_not",
        "price_usd_gt",
        "price_usd_lt",
        "price_usd_gte",
        "price_usd_lte",
        "price_usd_in",
        "price_usd_not_in",
        "max_stored",
        "max_stored_not",
        "max_stored_gt",
        "max_stored_lt",
        "max_stored_gte",
        "max_stored_lte",
        "max_stored_in",
        "max_stored_not_in",
        "most_liquid_pairs",
        "most_liquid_pairs_not",
        "most_liquid_pairs_contains",
        "most_liquid_pairs_not_contains",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    id_not = sgqlc.types.Field(ID, graphql_name="id_not")
    id_gt = sgqlc.types.Field(ID, graphql_name="id_gt")
    id_lt = sgqlc.types.Field(ID, graphql_name="id_lt")
    id_gte = sgqlc.types.Field(ID, graphql_name="id_gte")
    id_lte = sgqlc.types.Field(ID, graphql_name="id_lte")
    id_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_in"
    )
    id_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_not_in"
    )
    date = sgqlc.types.Field(Int, graphql_name="date")
    date_not = sgqlc.types.Field(Int, graphql_name="date_not")
    date_gt = sgqlc.types.Field(Int, graphql_name="date_gt")
    date_lt = sgqlc.types.Field(Int, graphql_name="date_lt")
    date_gte = sgqlc.types.Field(Int, graphql_name="date_gte")
    date_lte = sgqlc.types.Field(Int, graphql_name="date_lte")
    date_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="date_in"
    )
    date_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="date_not_in"
    )
    token = sgqlc.types.Field(String, graphql_name="token")
    token_not = sgqlc.types.Field(String, graphql_name="token_not")
    token_gt = sgqlc.types.Field(String, graphql_name="token_gt")
    token_lt = sgqlc.types.Field(String, graphql_name="token_lt")
    token_gte = sgqlc.types.Field(String, graphql_name="token_gte")
    token_lte = sgqlc.types.Field(String, graphql_name="token_lte")
    token_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="token_in"
    )
    token_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="token_not_in"
    )
    token_contains = sgqlc.types.Field(String, graphql_name="token_contains")
    token_not_contains = sgqlc.types.Field(String, graphql_name="token_not_contains")
    token_starts_with = sgqlc.types.Field(String, graphql_name="token_starts_with")
    token_not_starts_with = sgqlc.types.Field(
        String, graphql_name="token_not_starts_with"
    )
    token_ends_with = sgqlc.types.Field(String, graphql_name="token_ends_with")
    token_not_ends_with = sgqlc.types.Field(String, graphql_name="token_not_ends_with")
    daily_volume_token = sgqlc.types.Field(BigDecimal, graphql_name="dailyVolumeToken")
    daily_volume_token_not = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeToken_not"
    )
    daily_volume_token_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeToken_gt"
    )
    daily_volume_token_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeToken_lt"
    )
    daily_volume_token_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeToken_gte"
    )
    daily_volume_token_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeToken_lte"
    )
    daily_volume_token_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="dailyVolumeToken_in",
    )
    daily_volume_token_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="dailyVolumeToken_not_in",
    )
    daily_volume_eth = sgqlc.types.Field(BigDecimal, graphql_name="dailyVolumeETH")
    daily_volume_eth_not = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeETH_not"
    )
    daily_volume_eth_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeETH_gt"
    )
    daily_volume_eth_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeETH_lt"
    )
    daily_volume_eth_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeETH_gte"
    )
    daily_volume_eth_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeETH_lte"
    )
    daily_volume_eth_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="dailyVolumeETH_in",
    )
    daily_volume_eth_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="dailyVolumeETH_not_in",
    )
    daily_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name="dailyVolumeUSD")
    daily_volume_usd_not = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUSD_not"
    )
    daily_volume_usd_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUSD_gt"
    )
    daily_volume_usd_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUSD_lt"
    )
    daily_volume_usd_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUSD_gte"
    )
    daily_volume_usd_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUSD_lte"
    )
    daily_volume_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="dailyVolumeUSD_in",
    )
    daily_volume_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="dailyVolumeUSD_not_in",
    )
    daily_txns = sgqlc.types.Field(BigInt, graphql_name="dailyTxns")
    daily_txns_not = sgqlc.types.Field(BigInt, graphql_name="dailyTxns_not")
    daily_txns_gt = sgqlc.types.Field(BigInt, graphql_name="dailyTxns_gt")
    daily_txns_lt = sgqlc.types.Field(BigInt, graphql_name="dailyTxns_lt")
    daily_txns_gte = sgqlc.types.Field(BigInt, graphql_name="dailyTxns_gte")
    daily_txns_lte = sgqlc.types.Field(BigInt, graphql_name="dailyTxns_lte")
    daily_txns_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="dailyTxns_in"
    )
    daily_txns_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="dailyTxns_not_in",
    )
    total_liquidity_token = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityToken"
    )
    total_liquidity_token_not = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityToken_not"
    )
    total_liquidity_token_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityToken_gt"
    )
    total_liquidity_token_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityToken_lt"
    )
    total_liquidity_token_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityToken_gte"
    )
    total_liquidity_token_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityToken_lte"
    )
    total_liquidity_token_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalLiquidityToken_in",
    )
    total_liquidity_token_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalLiquidityToken_not_in",
    )
    total_liquidity_eth = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityETH"
    )
    total_liquidity_eth_not = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityETH_not"
    )
    total_liquidity_eth_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityETH_gt"
    )
    total_liquidity_eth_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityETH_lt"
    )
    total_liquidity_eth_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityETH_gte"
    )
    total_liquidity_eth_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityETH_lte"
    )
    total_liquidity_eth_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalLiquidityETH_in",
    )
    total_liquidity_eth_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalLiquidityETH_not_in",
    )
    total_liquidity_usd = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityUSD"
    )
    total_liquidity_usd_not = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityUSD_not"
    )
    total_liquidity_usd_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityUSD_gt"
    )
    total_liquidity_usd_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityUSD_lt"
    )
    total_liquidity_usd_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityUSD_gte"
    )
    total_liquidity_usd_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityUSD_lte"
    )
    total_liquidity_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalLiquidityUSD_in",
    )
    total_liquidity_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalLiquidityUSD_not_in",
    )
    price_usd = sgqlc.types.Field(BigDecimal, graphql_name="priceUSD")
    price_usd_not = sgqlc.types.Field(BigDecimal, graphql_name="priceUSD_not")
    price_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name="priceUSD_gt")
    price_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name="priceUSD_lt")
    price_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name="priceUSD_gte")
    price_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name="priceUSD_lte")
    price_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="priceUSD_in",
    )
    price_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="priceUSD_not_in",
    )
    max_stored = sgqlc.types.Field(Int, graphql_name="maxStored")
    max_stored_not = sgqlc.types.Field(Int, graphql_name="maxStored_not")
    max_stored_gt = sgqlc.types.Field(Int, graphql_name="maxStored_gt")
    max_stored_lt = sgqlc.types.Field(Int, graphql_name="maxStored_lt")
    max_stored_gte = sgqlc.types.Field(Int, graphql_name="maxStored_gte")
    max_stored_lte = sgqlc.types.Field(Int, graphql_name="maxStored_lte")
    max_stored_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="maxStored_in"
    )
    max_stored_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="maxStored_not_in"
    )
    most_liquid_pairs = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="mostLiquidPairs",
    )
    most_liquid_pairs_not = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="mostLiquidPairs_not",
    )
    most_liquid_pairs_contains = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="mostLiquidPairs_contains",
    )
    most_liquid_pairs_not_contains = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="mostLiquidPairs_not_contains",
    )


class Token_filter(sgqlc.types.Input):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "id_not",
        "id_gt",
        "id_lt",
        "id_gte",
        "id_lte",
        "id_in",
        "id_not_in",
        "symbol",
        "symbol_not",
        "symbol_gt",
        "symbol_lt",
        "symbol_gte",
        "symbol_lte",
        "symbol_in",
        "symbol_not_in",
        "symbol_contains",
        "symbol_not_contains",
        "symbol_starts_with",
        "symbol_not_starts_with",
        "symbol_ends_with",
        "symbol_not_ends_with",
        "name",
        "name_not",
        "name_gt",
        "name_lt",
        "name_gte",
        "name_lte",
        "name_in",
        "name_not_in",
        "name_contains",
        "name_not_contains",
        "name_starts_with",
        "name_not_starts_with",
        "name_ends_with",
        "name_not_ends_with",
        "decimals",
        "decimals_not",
        "decimals_gt",
        "decimals_lt",
        "decimals_gte",
        "decimals_lte",
        "decimals_in",
        "decimals_not_in",
        "total_supply",
        "total_supply_not",
        "total_supply_gt",
        "total_supply_lt",
        "total_supply_gte",
        "total_supply_lte",
        "total_supply_in",
        "total_supply_not_in",
        "trade_volume",
        "trade_volume_not",
        "trade_volume_gt",
        "trade_volume_lt",
        "trade_volume_gte",
        "trade_volume_lte",
        "trade_volume_in",
        "trade_volume_not_in",
        "trade_volume_usd",
        "trade_volume_usd_not",
        "trade_volume_usd_gt",
        "trade_volume_usd_lt",
        "trade_volume_usd_gte",
        "trade_volume_usd_lte",
        "trade_volume_usd_in",
        "trade_volume_usd_not_in",
        "untracked_volume_usd",
        "untracked_volume_usd_not",
        "untracked_volume_usd_gt",
        "untracked_volume_usd_lt",
        "untracked_volume_usd_gte",
        "untracked_volume_usd_lte",
        "untracked_volume_usd_in",
        "untracked_volume_usd_not_in",
        "tx_count",
        "tx_count_not",
        "tx_count_gt",
        "tx_count_lt",
        "tx_count_gte",
        "tx_count_lte",
        "tx_count_in",
        "tx_count_not_in",
        "total_liquidity",
        "total_liquidity_not",
        "total_liquidity_gt",
        "total_liquidity_lt",
        "total_liquidity_gte",
        "total_liquidity_lte",
        "total_liquidity_in",
        "total_liquidity_not_in",
        "derived_eth",
        "derived_eth_not",
        "derived_eth_gt",
        "derived_eth_lt",
        "derived_eth_gte",
        "derived_eth_lte",
        "derived_eth_in",
        "derived_eth_not_in",
        "most_liquid_pairs",
        "most_liquid_pairs_not",
        "most_liquid_pairs_contains",
        "most_liquid_pairs_not_contains",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    id_not = sgqlc.types.Field(ID, graphql_name="id_not")
    id_gt = sgqlc.types.Field(ID, graphql_name="id_gt")
    id_lt = sgqlc.types.Field(ID, graphql_name="id_lt")
    id_gte = sgqlc.types.Field(ID, graphql_name="id_gte")
    id_lte = sgqlc.types.Field(ID, graphql_name="id_lte")
    id_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_in"
    )
    id_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_not_in"
    )
    symbol = sgqlc.types.Field(String, graphql_name="symbol")
    symbol_not = sgqlc.types.Field(String, graphql_name="symbol_not")
    symbol_gt = sgqlc.types.Field(String, graphql_name="symbol_gt")
    symbol_lt = sgqlc.types.Field(String, graphql_name="symbol_lt")
    symbol_gte = sgqlc.types.Field(String, graphql_name="symbol_gte")
    symbol_lte = sgqlc.types.Field(String, graphql_name="symbol_lte")
    symbol_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="symbol_in"
    )
    symbol_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="symbol_not_in"
    )
    symbol_contains = sgqlc.types.Field(String, graphql_name="symbol_contains")
    symbol_not_contains = sgqlc.types.Field(String, graphql_name="symbol_not_contains")
    symbol_starts_with = sgqlc.types.Field(String, graphql_name="symbol_starts_with")
    symbol_not_starts_with = sgqlc.types.Field(
        String, graphql_name="symbol_not_starts_with"
    )
    symbol_ends_with = sgqlc.types.Field(String, graphql_name="symbol_ends_with")
    symbol_not_ends_with = sgqlc.types.Field(
        String, graphql_name="symbol_not_ends_with"
    )
    name = sgqlc.types.Field(String, graphql_name="name")
    name_not = sgqlc.types.Field(String, graphql_name="name_not")
    name_gt = sgqlc.types.Field(String, graphql_name="name_gt")
    name_lt = sgqlc.types.Field(String, graphql_name="name_lt")
    name_gte = sgqlc.types.Field(String, graphql_name="name_gte")
    name_lte = sgqlc.types.Field(String, graphql_name="name_lte")
    name_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="name_in"
    )
    name_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="name_not_in"
    )
    name_contains = sgqlc.types.Field(String, graphql_name="name_contains")
    name_not_contains = sgqlc.types.Field(String, graphql_name="name_not_contains")
    name_starts_with = sgqlc.types.Field(String, graphql_name="name_starts_with")
    name_not_starts_with = sgqlc.types.Field(
        String, graphql_name="name_not_starts_with"
    )
    name_ends_with = sgqlc.types.Field(String, graphql_name="name_ends_with")
    name_not_ends_with = sgqlc.types.Field(String, graphql_name="name_not_ends_with")
    decimals = sgqlc.types.Field(BigInt, graphql_name="decimals")
    decimals_not = sgqlc.types.Field(BigInt, graphql_name="decimals_not")
    decimals_gt = sgqlc.types.Field(BigInt, graphql_name="decimals_gt")
    decimals_lt = sgqlc.types.Field(BigInt, graphql_name="decimals_lt")
    decimals_gte = sgqlc.types.Field(BigInt, graphql_name="decimals_gte")
    decimals_lte = sgqlc.types.Field(BigInt, graphql_name="decimals_lte")
    decimals_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="decimals_in"
    )
    decimals_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="decimals_not_in",
    )
    total_supply = sgqlc.types.Field(BigInt, graphql_name="totalSupply")
    total_supply_not = sgqlc.types.Field(BigInt, graphql_name="totalSupply_not")
    total_supply_gt = sgqlc.types.Field(BigInt, graphql_name="totalSupply_gt")
    total_supply_lt = sgqlc.types.Field(BigInt, graphql_name="totalSupply_lt")
    total_supply_gte = sgqlc.types.Field(BigInt, graphql_name="totalSupply_gte")
    total_supply_lte = sgqlc.types.Field(BigInt, graphql_name="totalSupply_lte")
    total_supply_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="totalSupply_in"
    )
    total_supply_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="totalSupply_not_in",
    )
    trade_volume = sgqlc.types.Field(BigDecimal, graphql_name="tradeVolume")
    trade_volume_not = sgqlc.types.Field(BigDecimal, graphql_name="tradeVolume_not")
    trade_volume_gt = sgqlc.types.Field(BigDecimal, graphql_name="tradeVolume_gt")
    trade_volume_lt = sgqlc.types.Field(BigDecimal, graphql_name="tradeVolume_lt")
    trade_volume_gte = sgqlc.types.Field(BigDecimal, graphql_name="tradeVolume_gte")
    trade_volume_lte = sgqlc.types.Field(BigDecimal, graphql_name="tradeVolume_lte")
    trade_volume_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="tradeVolume_in",
    )
    trade_volume_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="tradeVolume_not_in",
    )
    trade_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name="tradeVolumeUSD")
    trade_volume_usd_not = sgqlc.types.Field(
        BigDecimal, graphql_name="tradeVolumeUSD_not"
    )
    trade_volume_usd_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="tradeVolumeUSD_gt"
    )
    trade_volume_usd_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="tradeVolumeUSD_lt"
    )
    trade_volume_usd_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="tradeVolumeUSD_gte"
    )
    trade_volume_usd_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="tradeVolumeUSD_lte"
    )
    trade_volume_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="tradeVolumeUSD_in",
    )
    trade_volume_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="tradeVolumeUSD_not_in",
    )
    untracked_volume_usd = sgqlc.types.Field(
        BigDecimal, graphql_name="untrackedVolumeUSD"
    )
    untracked_volume_usd_not = sgqlc.types.Field(
        BigDecimal, graphql_name="untrackedVolumeUSD_not"
    )
    untracked_volume_usd_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="untrackedVolumeUSD_gt"
    )
    untracked_volume_usd_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="untrackedVolumeUSD_lt"
    )
    untracked_volume_usd_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="untrackedVolumeUSD_gte"
    )
    untracked_volume_usd_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="untrackedVolumeUSD_lte"
    )
    untracked_volume_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="untrackedVolumeUSD_in",
    )
    untracked_volume_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="untrackedVolumeUSD_not_in",
    )
    tx_count = sgqlc.types.Field(BigInt, graphql_name="txCount")
    tx_count_not = sgqlc.types.Field(BigInt, graphql_name="txCount_not")
    tx_count_gt = sgqlc.types.Field(BigInt, graphql_name="txCount_gt")
    tx_count_lt = sgqlc.types.Field(BigInt, graphql_name="txCount_lt")
    tx_count_gte = sgqlc.types.Field(BigInt, graphql_name="txCount_gte")
    tx_count_lte = sgqlc.types.Field(BigInt, graphql_name="txCount_lte")
    tx_count_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="txCount_in"
    )
    tx_count_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="txCount_not_in"
    )
    total_liquidity = sgqlc.types.Field(BigDecimal, graphql_name="totalLiquidity")
    total_liquidity_not = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidity_not"
    )
    total_liquidity_gt = sgqlc.types.Field(BigDecimal, graphql_name="totalLiquidity_gt")
    total_liquidity_lt = sgqlc.types.Field(BigDecimal, graphql_name="totalLiquidity_lt")
    total_liquidity_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidity_gte"
    )
    total_liquidity_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidity_lte"
    )
    total_liquidity_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalLiquidity_in",
    )
    total_liquidity_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalLiquidity_not_in",
    )
    derived_eth = sgqlc.types.Field(BigDecimal, graphql_name="derivedETH")
    derived_eth_not = sgqlc.types.Field(BigDecimal, graphql_name="derivedETH_not")
    derived_eth_gt = sgqlc.types.Field(BigDecimal, graphql_name="derivedETH_gt")
    derived_eth_lt = sgqlc.types.Field(BigDecimal, graphql_name="derivedETH_lt")
    derived_eth_gte = sgqlc.types.Field(BigDecimal, graphql_name="derivedETH_gte")
    derived_eth_lte = sgqlc.types.Field(BigDecimal, graphql_name="derivedETH_lte")
    derived_eth_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="derivedETH_in",
    )
    derived_eth_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="derivedETH_not_in",
    )
    most_liquid_pairs = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="mostLiquidPairs",
    )
    most_liquid_pairs_not = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="mostLiquidPairs_not",
    )
    most_liquid_pairs_contains = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="mostLiquidPairs_contains",
    )
    most_liquid_pairs_not_contains = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="mostLiquidPairs_not_contains",
    )


class Transaction_filter(sgqlc.types.Input):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "id_not",
        "id_gt",
        "id_lt",
        "id_gte",
        "id_lte",
        "id_in",
        "id_not_in",
        "block_number",
        "block_number_not",
        "block_number_gt",
        "block_number_lt",
        "block_number_gte",
        "block_number_lte",
        "block_number_in",
        "block_number_not_in",
        "timestamp",
        "timestamp_not",
        "timestamp_gt",
        "timestamp_lt",
        "timestamp_gte",
        "timestamp_lte",
        "timestamp_in",
        "timestamp_not_in",
        "mints",
        "mints_not",
        "mints_contains",
        "mints_not_contains",
        "burns",
        "burns_not",
        "burns_contains",
        "burns_not_contains",
        "swaps",
        "swaps_not",
        "swaps_contains",
        "swaps_not_contains",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    id_not = sgqlc.types.Field(ID, graphql_name="id_not")
    id_gt = sgqlc.types.Field(ID, graphql_name="id_gt")
    id_lt = sgqlc.types.Field(ID, graphql_name="id_lt")
    id_gte = sgqlc.types.Field(ID, graphql_name="id_gte")
    id_lte = sgqlc.types.Field(ID, graphql_name="id_lte")
    id_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_in"
    )
    id_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_not_in"
    )
    block_number = sgqlc.types.Field(BigInt, graphql_name="blockNumber")
    block_number_not = sgqlc.types.Field(BigInt, graphql_name="blockNumber_not")
    block_number_gt = sgqlc.types.Field(BigInt, graphql_name="blockNumber_gt")
    block_number_lt = sgqlc.types.Field(BigInt, graphql_name="blockNumber_lt")
    block_number_gte = sgqlc.types.Field(BigInt, graphql_name="blockNumber_gte")
    block_number_lte = sgqlc.types.Field(BigInt, graphql_name="blockNumber_lte")
    block_number_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="blockNumber_in"
    )
    block_number_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="blockNumber_not_in",
    )
    timestamp = sgqlc.types.Field(BigInt, graphql_name="timestamp")
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name="timestamp_not")
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name="timestamp_gt")
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name="timestamp_lt")
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name="timestamp_gte")
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name="timestamp_lte")
    timestamp_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="timestamp_in"
    )
    timestamp_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)),
        graphql_name="timestamp_not_in",
    )
    mints = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="mints"
    )
    mints_not = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="mints_not"
    )
    mints_contains = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="mints_contains"
    )
    mints_not_contains = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="mints_not_contains",
    )
    burns = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="burns"
    )
    burns_not = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="burns_not"
    )
    burns_contains = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="burns_contains"
    )
    burns_not_contains = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="burns_not_contains",
    )
    swaps = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="swaps"
    )
    swaps_not = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="swaps_not"
    )
    swaps_contains = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="swaps_contains"
    )
    swaps_not_contains = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="swaps_not_contains",
    )


class UniswapDayData_filter(sgqlc.types.Input):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "id_not",
        "id_gt",
        "id_lt",
        "id_gte",
        "id_lte",
        "id_in",
        "id_not_in",
        "date",
        "date_not",
        "date_gt",
        "date_lt",
        "date_gte",
        "date_lte",
        "date_in",
        "date_not_in",
        "daily_volume_eth",
        "daily_volume_eth_not",
        "daily_volume_eth_gt",
        "daily_volume_eth_lt",
        "daily_volume_eth_gte",
        "daily_volume_eth_lte",
        "daily_volume_eth_in",
        "daily_volume_eth_not_in",
        "daily_volume_usd",
        "daily_volume_usd_not",
        "daily_volume_usd_gt",
        "daily_volume_usd_lt",
        "daily_volume_usd_gte",
        "daily_volume_usd_lte",
        "daily_volume_usd_in",
        "daily_volume_usd_not_in",
        "daily_volume_untracked",
        "daily_volume_untracked_not",
        "daily_volume_untracked_gt",
        "daily_volume_untracked_lt",
        "daily_volume_untracked_gte",
        "daily_volume_untracked_lte",
        "daily_volume_untracked_in",
        "daily_volume_untracked_not_in",
        "total_volume_eth",
        "total_volume_eth_not",
        "total_volume_eth_gt",
        "total_volume_eth_lt",
        "total_volume_eth_gte",
        "total_volume_eth_lte",
        "total_volume_eth_in",
        "total_volume_eth_not_in",
        "total_liquidity_eth",
        "total_liquidity_eth_not",
        "total_liquidity_eth_gt",
        "total_liquidity_eth_lt",
        "total_liquidity_eth_gte",
        "total_liquidity_eth_lte",
        "total_liquidity_eth_in",
        "total_liquidity_eth_not_in",
        "total_volume_usd",
        "total_volume_usd_not",
        "total_volume_usd_gt",
        "total_volume_usd_lt",
        "total_volume_usd_gte",
        "total_volume_usd_lte",
        "total_volume_usd_in",
        "total_volume_usd_not_in",
        "total_liquidity_usd",
        "total_liquidity_usd_not",
        "total_liquidity_usd_gt",
        "total_liquidity_usd_lt",
        "total_liquidity_usd_gte",
        "total_liquidity_usd_lte",
        "total_liquidity_usd_in",
        "total_liquidity_usd_not_in",
        "max_stored",
        "max_stored_not",
        "max_stored_gt",
        "max_stored_lt",
        "max_stored_gte",
        "max_stored_lte",
        "max_stored_in",
        "max_stored_not_in",
        "most_liquid_tokens",
        "most_liquid_tokens_not",
        "most_liquid_tokens_contains",
        "most_liquid_tokens_not_contains",
        "tx_count",
        "tx_count_not",
        "tx_count_gt",
        "tx_count_lt",
        "tx_count_gte",
        "tx_count_lte",
        "tx_count_in",
        "tx_count_not_in",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    id_not = sgqlc.types.Field(ID, graphql_name="id_not")
    id_gt = sgqlc.types.Field(ID, graphql_name="id_gt")
    id_lt = sgqlc.types.Field(ID, graphql_name="id_lt")
    id_gte = sgqlc.types.Field(ID, graphql_name="id_gte")
    id_lte = sgqlc.types.Field(ID, graphql_name="id_lte")
    id_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_in"
    )
    id_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_not_in"
    )
    date = sgqlc.types.Field(Int, graphql_name="date")
    date_not = sgqlc.types.Field(Int, graphql_name="date_not")
    date_gt = sgqlc.types.Field(Int, graphql_name="date_gt")
    date_lt = sgqlc.types.Field(Int, graphql_name="date_lt")
    date_gte = sgqlc.types.Field(Int, graphql_name="date_gte")
    date_lte = sgqlc.types.Field(Int, graphql_name="date_lte")
    date_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="date_in"
    )
    date_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="date_not_in"
    )
    daily_volume_eth = sgqlc.types.Field(BigDecimal, graphql_name="dailyVolumeETH")
    daily_volume_eth_not = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeETH_not"
    )
    daily_volume_eth_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeETH_gt"
    )
    daily_volume_eth_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeETH_lt"
    )
    daily_volume_eth_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeETH_gte"
    )
    daily_volume_eth_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeETH_lte"
    )
    daily_volume_eth_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="dailyVolumeETH_in",
    )
    daily_volume_eth_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="dailyVolumeETH_not_in",
    )
    daily_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name="dailyVolumeUSD")
    daily_volume_usd_not = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUSD_not"
    )
    daily_volume_usd_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUSD_gt"
    )
    daily_volume_usd_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUSD_lt"
    )
    daily_volume_usd_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUSD_gte"
    )
    daily_volume_usd_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUSD_lte"
    )
    daily_volume_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="dailyVolumeUSD_in",
    )
    daily_volume_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="dailyVolumeUSD_not_in",
    )
    daily_volume_untracked = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUntracked"
    )
    daily_volume_untracked_not = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUntracked_not"
    )
    daily_volume_untracked_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUntracked_gt"
    )
    daily_volume_untracked_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUntracked_lt"
    )
    daily_volume_untracked_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUntracked_gte"
    )
    daily_volume_untracked_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="dailyVolumeUntracked_lte"
    )
    daily_volume_untracked_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="dailyVolumeUntracked_in",
    )
    daily_volume_untracked_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="dailyVolumeUntracked_not_in",
    )
    total_volume_eth = sgqlc.types.Field(BigDecimal, graphql_name="totalVolumeETH")
    total_volume_eth_not = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeETH_not"
    )
    total_volume_eth_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeETH_gt"
    )
    total_volume_eth_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeETH_lt"
    )
    total_volume_eth_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeETH_gte"
    )
    total_volume_eth_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeETH_lte"
    )
    total_volume_eth_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalVolumeETH_in",
    )
    total_volume_eth_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalVolumeETH_not_in",
    )
    total_liquidity_eth = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityETH"
    )
    total_liquidity_eth_not = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityETH_not"
    )
    total_liquidity_eth_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityETH_gt"
    )
    total_liquidity_eth_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityETH_lt"
    )
    total_liquidity_eth_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityETH_gte"
    )
    total_liquidity_eth_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityETH_lte"
    )
    total_liquidity_eth_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalLiquidityETH_in",
    )
    total_liquidity_eth_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalLiquidityETH_not_in",
    )
    total_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name="totalVolumeUSD")
    total_volume_usd_not = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeUSD_not"
    )
    total_volume_usd_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeUSD_gt"
    )
    total_volume_usd_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeUSD_lt"
    )
    total_volume_usd_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeUSD_gte"
    )
    total_volume_usd_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeUSD_lte"
    )
    total_volume_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalVolumeUSD_in",
    )
    total_volume_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalVolumeUSD_not_in",
    )
    total_liquidity_usd = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityUSD"
    )
    total_liquidity_usd_not = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityUSD_not"
    )
    total_liquidity_usd_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityUSD_gt"
    )
    total_liquidity_usd_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityUSD_lt"
    )
    total_liquidity_usd_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityUSD_gte"
    )
    total_liquidity_usd_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityUSD_lte"
    )
    total_liquidity_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalLiquidityUSD_in",
    )
    total_liquidity_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalLiquidityUSD_not_in",
    )
    max_stored = sgqlc.types.Field(Int, graphql_name="maxStored")
    max_stored_not = sgqlc.types.Field(Int, graphql_name="maxStored_not")
    max_stored_gt = sgqlc.types.Field(Int, graphql_name="maxStored_gt")
    max_stored_lt = sgqlc.types.Field(Int, graphql_name="maxStored_lt")
    max_stored_gte = sgqlc.types.Field(Int, graphql_name="maxStored_gte")
    max_stored_lte = sgqlc.types.Field(Int, graphql_name="maxStored_lte")
    max_stored_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="maxStored_in"
    )
    max_stored_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="maxStored_not_in"
    )
    most_liquid_tokens = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="mostLiquidTokens",
    )
    most_liquid_tokens_not = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="mostLiquidTokens_not",
    )
    most_liquid_tokens_contains = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="mostLiquidTokens_contains",
    )
    most_liquid_tokens_not_contains = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="mostLiquidTokens_not_contains",
    )
    tx_count = sgqlc.types.Field(BigInt, graphql_name="txCount")
    tx_count_not = sgqlc.types.Field(BigInt, graphql_name="txCount_not")
    tx_count_gt = sgqlc.types.Field(BigInt, graphql_name="txCount_gt")
    tx_count_lt = sgqlc.types.Field(BigInt, graphql_name="txCount_lt")
    tx_count_gte = sgqlc.types.Field(BigInt, graphql_name="txCount_gte")
    tx_count_lte = sgqlc.types.Field(BigInt, graphql_name="txCount_lte")
    tx_count_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="txCount_in"
    )
    tx_count_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="txCount_not_in"
    )


class UniswapFactory_filter(sgqlc.types.Input):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "id_not",
        "id_gt",
        "id_lt",
        "id_gte",
        "id_lte",
        "id_in",
        "id_not_in",
        "pair_count",
        "pair_count_not",
        "pair_count_gt",
        "pair_count_lt",
        "pair_count_gte",
        "pair_count_lte",
        "pair_count_in",
        "pair_count_not_in",
        "total_volume_usd",
        "total_volume_usd_not",
        "total_volume_usd_gt",
        "total_volume_usd_lt",
        "total_volume_usd_gte",
        "total_volume_usd_lte",
        "total_volume_usd_in",
        "total_volume_usd_not_in",
        "total_volume_eth",
        "total_volume_eth_not",
        "total_volume_eth_gt",
        "total_volume_eth_lt",
        "total_volume_eth_gte",
        "total_volume_eth_lte",
        "total_volume_eth_in",
        "total_volume_eth_not_in",
        "untracked_volume_usd",
        "untracked_volume_usd_not",
        "untracked_volume_usd_gt",
        "untracked_volume_usd_lt",
        "untracked_volume_usd_gte",
        "untracked_volume_usd_lte",
        "untracked_volume_usd_in",
        "untracked_volume_usd_not_in",
        "total_liquidity_usd",
        "total_liquidity_usd_not",
        "total_liquidity_usd_gt",
        "total_liquidity_usd_lt",
        "total_liquidity_usd_gte",
        "total_liquidity_usd_lte",
        "total_liquidity_usd_in",
        "total_liquidity_usd_not_in",
        "total_liquidity_eth",
        "total_liquidity_eth_not",
        "total_liquidity_eth_gt",
        "total_liquidity_eth_lt",
        "total_liquidity_eth_gte",
        "total_liquidity_eth_lte",
        "total_liquidity_eth_in",
        "total_liquidity_eth_not_in",
        "tx_count",
        "tx_count_not",
        "tx_count_gt",
        "tx_count_lt",
        "tx_count_gte",
        "tx_count_lte",
        "tx_count_in",
        "tx_count_not_in",
        "most_liquid_tokens",
        "most_liquid_tokens_not",
        "most_liquid_tokens_contains",
        "most_liquid_tokens_not_contains",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    id_not = sgqlc.types.Field(ID, graphql_name="id_not")
    id_gt = sgqlc.types.Field(ID, graphql_name="id_gt")
    id_lt = sgqlc.types.Field(ID, graphql_name="id_lt")
    id_gte = sgqlc.types.Field(ID, graphql_name="id_gte")
    id_lte = sgqlc.types.Field(ID, graphql_name="id_lte")
    id_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_in"
    )
    id_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_not_in"
    )
    pair_count = sgqlc.types.Field(Int, graphql_name="pairCount")
    pair_count_not = sgqlc.types.Field(Int, graphql_name="pairCount_not")
    pair_count_gt = sgqlc.types.Field(Int, graphql_name="pairCount_gt")
    pair_count_lt = sgqlc.types.Field(Int, graphql_name="pairCount_lt")
    pair_count_gte = sgqlc.types.Field(Int, graphql_name="pairCount_gte")
    pair_count_lte = sgqlc.types.Field(Int, graphql_name="pairCount_lte")
    pair_count_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="pairCount_in"
    )
    pair_count_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name="pairCount_not_in"
    )
    total_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name="totalVolumeUSD")
    total_volume_usd_not = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeUSD_not"
    )
    total_volume_usd_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeUSD_gt"
    )
    total_volume_usd_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeUSD_lt"
    )
    total_volume_usd_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeUSD_gte"
    )
    total_volume_usd_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeUSD_lte"
    )
    total_volume_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalVolumeUSD_in",
    )
    total_volume_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalVolumeUSD_not_in",
    )
    total_volume_eth = sgqlc.types.Field(BigDecimal, graphql_name="totalVolumeETH")
    total_volume_eth_not = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeETH_not"
    )
    total_volume_eth_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeETH_gt"
    )
    total_volume_eth_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeETH_lt"
    )
    total_volume_eth_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeETH_gte"
    )
    total_volume_eth_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalVolumeETH_lte"
    )
    total_volume_eth_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalVolumeETH_in",
    )
    total_volume_eth_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalVolumeETH_not_in",
    )
    untracked_volume_usd = sgqlc.types.Field(
        BigDecimal, graphql_name="untrackedVolumeUSD"
    )
    untracked_volume_usd_not = sgqlc.types.Field(
        BigDecimal, graphql_name="untrackedVolumeUSD_not"
    )
    untracked_volume_usd_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="untrackedVolumeUSD_gt"
    )
    untracked_volume_usd_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="untrackedVolumeUSD_lt"
    )
    untracked_volume_usd_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="untrackedVolumeUSD_gte"
    )
    untracked_volume_usd_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="untrackedVolumeUSD_lte"
    )
    untracked_volume_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="untrackedVolumeUSD_in",
    )
    untracked_volume_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="untrackedVolumeUSD_not_in",
    )
    total_liquidity_usd = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityUSD"
    )
    total_liquidity_usd_not = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityUSD_not"
    )
    total_liquidity_usd_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityUSD_gt"
    )
    total_liquidity_usd_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityUSD_lt"
    )
    total_liquidity_usd_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityUSD_gte"
    )
    total_liquidity_usd_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityUSD_lte"
    )
    total_liquidity_usd_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalLiquidityUSD_in",
    )
    total_liquidity_usd_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalLiquidityUSD_not_in",
    )
    total_liquidity_eth = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityETH"
    )
    total_liquidity_eth_not = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityETH_not"
    )
    total_liquidity_eth_gt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityETH_gt"
    )
    total_liquidity_eth_lt = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityETH_lt"
    )
    total_liquidity_eth_gte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityETH_gte"
    )
    total_liquidity_eth_lte = sgqlc.types.Field(
        BigDecimal, graphql_name="totalLiquidityETH_lte"
    )
    total_liquidity_eth_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalLiquidityETH_in",
    )
    total_liquidity_eth_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="totalLiquidityETH_not_in",
    )
    tx_count = sgqlc.types.Field(BigInt, graphql_name="txCount")
    tx_count_not = sgqlc.types.Field(BigInt, graphql_name="txCount_not")
    tx_count_gt = sgqlc.types.Field(BigInt, graphql_name="txCount_gt")
    tx_count_lt = sgqlc.types.Field(BigInt, graphql_name="txCount_lt")
    tx_count_gte = sgqlc.types.Field(BigInt, graphql_name="txCount_gte")
    tx_count_lte = sgqlc.types.Field(BigInt, graphql_name="txCount_lte")
    tx_count_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="txCount_in"
    )
    tx_count_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name="txCount_not_in"
    )
    most_liquid_tokens = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="mostLiquidTokens",
    )
    most_liquid_tokens_not = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="mostLiquidTokens_not",
    )
    most_liquid_tokens_contains = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="mostLiquidTokens_contains",
    )
    most_liquid_tokens_not_contains = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="mostLiquidTokens_not_contains",
    )


class User_filter(sgqlc.types.Input):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "id_not",
        "id_gt",
        "id_lt",
        "id_gte",
        "id_lte",
        "id_in",
        "id_not_in",
        "usd_swapped",
        "usd_swapped_not",
        "usd_swapped_gt",
        "usd_swapped_lt",
        "usd_swapped_gte",
        "usd_swapped_lte",
        "usd_swapped_in",
        "usd_swapped_not_in",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    id_not = sgqlc.types.Field(ID, graphql_name="id_not")
    id_gt = sgqlc.types.Field(ID, graphql_name="id_gt")
    id_lt = sgqlc.types.Field(ID, graphql_name="id_lt")
    id_gte = sgqlc.types.Field(ID, graphql_name="id_gte")
    id_lte = sgqlc.types.Field(ID, graphql_name="id_lte")
    id_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_in"
    )
    id_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name="id_not_in"
    )
    usd_swapped = sgqlc.types.Field(BigDecimal, graphql_name="usdSwapped")
    usd_swapped_not = sgqlc.types.Field(BigDecimal, graphql_name="usdSwapped_not")
    usd_swapped_gt = sgqlc.types.Field(BigDecimal, graphql_name="usdSwapped_gt")
    usd_swapped_lt = sgqlc.types.Field(BigDecimal, graphql_name="usdSwapped_lt")
    usd_swapped_gte = sgqlc.types.Field(BigDecimal, graphql_name="usdSwapped_gte")
    usd_swapped_lte = sgqlc.types.Field(BigDecimal, graphql_name="usdSwapped_lte")
    usd_swapped_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="usdSwapped_in",
    )
    usd_swapped_not_in = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)),
        graphql_name="usdSwapped_not_in",
    )


########################################################################
# Output Objects and Interfaces
########################################################################
class Bundle(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = ("id", "eth_price")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    eth_price = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="ethPrice"
    )


class Burn(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "transaction",
        "timestamp",
        "pair",
        "liquidity",
        "sender",
        "amount0",
        "amount1",
        "to",
        "log_index",
        "amount_usd",
        "needs_complete",
        "fee_to",
        "fee_liquidity",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    transaction = sgqlc.types.Field(
        sgqlc.types.non_null("Transaction"), graphql_name="transaction"
    )
    timestamp = sgqlc.types.Field(
        sgqlc.types.non_null(BigInt), graphql_name="timestamp"
    )
    pair = sgqlc.types.Field(sgqlc.types.non_null("Pair"), graphql_name="pair")
    liquidity = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="liquidity"
    )
    sender = sgqlc.types.Field(Bytes, graphql_name="sender")
    amount0 = sgqlc.types.Field(BigDecimal, graphql_name="amount0")
    amount1 = sgqlc.types.Field(BigDecimal, graphql_name="amount1")
    to = sgqlc.types.Field(Bytes, graphql_name="to")
    log_index = sgqlc.types.Field(BigInt, graphql_name="logIndex")
    amount_usd = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD")
    needs_complete = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="needsComplete"
    )
    fee_to = sgqlc.types.Field(Bytes, graphql_name="feeTo")
    fee_liquidity = sgqlc.types.Field(BigDecimal, graphql_name="feeLiquidity")


class LiquidityPosition(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = ("id", "user", "pair", "liquidity_token_balance")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    user = sgqlc.types.Field(sgqlc.types.non_null("User"), graphql_name="user")
    pair = sgqlc.types.Field(sgqlc.types.non_null("Pair"), graphql_name="pair")
    liquidity_token_balance = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="liquidityTokenBalance"
    )


class LiquidityPositionSnapshot(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "liquidity_position",
        "timestamp",
        "block",
        "user",
        "pair",
        "token0_price_usd",
        "token1_price_usd",
        "reserve0",
        "reserve1",
        "reserve_usd",
        "liquidity_token_total_supply",
        "liquidity_token_balance",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    liquidity_position = sgqlc.types.Field(
        sgqlc.types.non_null(LiquidityPosition), graphql_name="liquidityPosition"
    )
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="timestamp")
    block = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="block")
    user = sgqlc.types.Field(sgqlc.types.non_null("User"), graphql_name="user")
    pair = sgqlc.types.Field(sgqlc.types.non_null("Pair"), graphql_name="pair")
    token0_price_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="token0PriceUSD"
    )
    token1_price_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="token1PriceUSD"
    )
    reserve0 = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="reserve0"
    )
    reserve1 = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="reserve1"
    )
    reserve_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="reserveUSD"
    )
    liquidity_token_total_supply = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="liquidityTokenTotalSupply"
    )
    liquidity_token_balance = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="liquidityTokenBalance"
    )


class Mint(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "transaction",
        "timestamp",
        "pair",
        "to",
        "liquidity",
        "sender",
        "amount0",
        "amount1",
        "log_index",
        "amount_usd",
        "fee_to",
        "fee_liquidity",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    transaction = sgqlc.types.Field(
        sgqlc.types.non_null("Transaction"), graphql_name="transaction"
    )
    timestamp = sgqlc.types.Field(
        sgqlc.types.non_null(BigInt), graphql_name="timestamp"
    )
    pair = sgqlc.types.Field(sgqlc.types.non_null("Pair"), graphql_name="pair")
    to = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name="to")
    liquidity = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="liquidity"
    )
    sender = sgqlc.types.Field(Bytes, graphql_name="sender")
    amount0 = sgqlc.types.Field(BigDecimal, graphql_name="amount0")
    amount1 = sgqlc.types.Field(BigDecimal, graphql_name="amount1")
    log_index = sgqlc.types.Field(BigInt, graphql_name="logIndex")
    amount_usd = sgqlc.types.Field(BigDecimal, graphql_name="amountUSD")
    fee_to = sgqlc.types.Field(Bytes, graphql_name="feeTo")
    fee_liquidity = sgqlc.types.Field(BigDecimal, graphql_name="feeLiquidity")


class Pair(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "token0",
        "token1",
        "reserve0",
        "reserve1",
        "total_supply",
        "reserve_eth",
        "reserve_usd",
        "tracked_reserve_eth",
        "token0_price",
        "token1_price",
        "volume_token0",
        "volume_token1",
        "volume_usd",
        "untracked_volume_usd",
        "tx_count",
        "created_at_timestamp",
        "created_at_block_number",
        "liquidity_provider_count",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    token0 = sgqlc.types.Field(sgqlc.types.non_null("Token"), graphql_name="token0")
    token1 = sgqlc.types.Field(sgqlc.types.non_null("Token"), graphql_name="token1")
    reserve0 = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="reserve0"
    )
    reserve1 = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="reserve1"
    )
    total_supply = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="totalSupply"
    )
    reserve_eth = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="reserveETH"
    )
    reserve_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="reserveUSD"
    )
    tracked_reserve_eth = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="trackedReserveETH"
    )
    token0_price = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="token0Price"
    )
    token1_price = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="token1Price"
    )
    volume_token0 = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="volumeToken0"
    )
    volume_token1 = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="volumeToken1"
    )
    volume_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="volumeUSD"
    )
    untracked_volume_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="untrackedVolumeUSD"
    )
    tx_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name="txCount")
    created_at_timestamp = sgqlc.types.Field(
        sgqlc.types.non_null(BigInt), graphql_name="createdAtTimestamp"
    )
    created_at_block_number = sgqlc.types.Field(
        sgqlc.types.non_null(BigInt), graphql_name="createdAtBlockNumber"
    )
    liquidity_provider_count = sgqlc.types.Field(
        sgqlc.types.non_null(BigInt), graphql_name="liquidityProviderCount"
    )


class PairDayData(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "date",
        "pair_address",
        "token0",
        "token1",
        "reserve0",
        "reserve1",
        "total_supply",
        "reserve_usd",
        "daily_volume_token0",
        "daily_volume_token1",
        "daily_volume_usd",
        "daily_txns",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    date = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="date")
    pair_address = sgqlc.types.Field(
        sgqlc.types.non_null(Bytes), graphql_name="pairAddress"
    )
    token0 = sgqlc.types.Field(sgqlc.types.non_null("Token"), graphql_name="token0")
    token1 = sgqlc.types.Field(sgqlc.types.non_null("Token"), graphql_name="token1")
    reserve0 = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="reserve0"
    )
    reserve1 = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="reserve1"
    )
    total_supply = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="totalSupply"
    )
    reserve_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="reserveUSD"
    )
    daily_volume_token0 = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="dailyVolumeToken0"
    )
    daily_volume_token1 = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="dailyVolumeToken1"
    )
    daily_volume_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="dailyVolumeUSD"
    )
    daily_txns = sgqlc.types.Field(
        sgqlc.types.non_null(BigInt), graphql_name="dailyTxns"
    )


class PairHourData(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "hour_start_unix",
        "pair",
        "reserve0",
        "reserve1",
        "reserve_usd",
        "hourly_volume_token0",
        "hourly_volume_token1",
        "hourly_volume_usd",
        "hourly_txns",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    hour_start_unix = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="hourStartUnix"
    )
    pair = sgqlc.types.Field(sgqlc.types.non_null(Pair), graphql_name="pair")
    reserve0 = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="reserve0"
    )
    reserve1 = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="reserve1"
    )
    reserve_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="reserveUSD"
    )
    hourly_volume_token0 = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="hourlyVolumeToken0"
    )
    hourly_volume_token1 = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="hourlyVolumeToken1"
    )
    hourly_volume_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="hourlyVolumeUSD"
    )
    hourly_txns = sgqlc.types.Field(
        sgqlc.types.non_null(BigInt), graphql_name="hourlyTxns"
    )


class Query(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "uniswap_factory",
        "uniswap_factories",
        "token",
        "tokens",
        "pair",
        "pairs",
        "user",
        "users",
        "liquidity_position",
        "liquidity_positions",
        "liquidity_position_snapshot",
        "liquidity_position_snapshots",
        "transaction",
        "transactions",
        "mint",
        "mints",
        "burn",
        "burns",
        "swap",
        "swaps",
        "bundle",
        "bundles",
        "uniswap_day_data",
        "uniswap_day_datas",
        "pair_hour_data",
        "pair_hour_datas",
        "pair_day_data",
        "pair_day_datas",
        "token_day_data",
        "token_day_datas",
        "_meta",
    )
    uniswap_factory = sgqlc.types.Field(
        "UniswapFactory",
        graphql_name="uniswapFactory",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    uniswap_factories = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("UniswapFactory"))
        ),
        graphql_name="uniswapFactories",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        UniswapFactory_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        UniswapFactory_filter, graphql_name="where", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    token = sgqlc.types.Field(
        "Token",
        graphql_name="token",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    tokens = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null("Token"))),
        graphql_name="tokens",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        Token_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(Token_filter, graphql_name="where", default=None),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    pair = sgqlc.types.Field(
        Pair,
        graphql_name="pair",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    pairs = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Pair))),
        graphql_name="pairs",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(Pair_orderBy, graphql_name="orderBy", default=None),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(Pair_filter, graphql_name="where", default=None),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    user = sgqlc.types.Field(
        "User",
        graphql_name="user",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    users = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null("User"))),
        graphql_name="users",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(User_orderBy, graphql_name="orderBy", default=None),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(User_filter, graphql_name="where", default=None),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    liquidity_position = sgqlc.types.Field(
        LiquidityPosition,
        graphql_name="liquidityPosition",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    liquidity_positions = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(LiquidityPosition))
        ),
        graphql_name="liquidityPositions",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        LiquidityPosition_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        LiquidityPosition_filter, graphql_name="where", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    liquidity_position_snapshot = sgqlc.types.Field(
        LiquidityPositionSnapshot,
        graphql_name="liquidityPositionSnapshot",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    liquidity_position_snapshots = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(LiquidityPositionSnapshot))
        ),
        graphql_name="liquidityPositionSnapshots",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        LiquidityPositionSnapshot_orderBy,
                        graphql_name="orderBy",
                        default=None,
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        LiquidityPositionSnapshot_filter,
                        graphql_name="where",
                        default=None,
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    transaction = sgqlc.types.Field(
        "Transaction",
        graphql_name="transaction",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    transactions = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null("Transaction"))),
        graphql_name="transactions",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        Transaction_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        Transaction_filter, graphql_name="where", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    mint = sgqlc.types.Field(
        Mint,
        graphql_name="mint",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    mints = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Mint))),
        graphql_name="mints",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(Mint_orderBy, graphql_name="orderBy", default=None),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(Mint_filter, graphql_name="where", default=None),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    burn = sgqlc.types.Field(
        Burn,
        graphql_name="burn",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    burns = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Burn))),
        graphql_name="burns",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(Burn_orderBy, graphql_name="orderBy", default=None),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(Burn_filter, graphql_name="where", default=None),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    swap = sgqlc.types.Field(
        "Swap",
        graphql_name="swap",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    swaps = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null("Swap"))),
        graphql_name="swaps",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(Swap_orderBy, graphql_name="orderBy", default=None),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(Swap_filter, graphql_name="where", default=None),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    bundle = sgqlc.types.Field(
        Bundle,
        graphql_name="bundle",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    bundles = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Bundle))),
        graphql_name="bundles",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        Bundle_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(Bundle_filter, graphql_name="where", default=None),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    uniswap_day_data = sgqlc.types.Field(
        "UniswapDayData",
        graphql_name="uniswapDayData",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    uniswap_day_datas = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("UniswapDayData"))
        ),
        graphql_name="uniswapDayDatas",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        UniswapDayData_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        UniswapDayData_filter, graphql_name="where", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    pair_hour_data = sgqlc.types.Field(
        PairHourData,
        graphql_name="pairHourData",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    pair_hour_datas = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PairHourData))),
        graphql_name="pairHourDatas",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        PairHourData_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        PairHourData_filter, graphql_name="where", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    pair_day_data = sgqlc.types.Field(
        PairDayData,
        graphql_name="pairDayData",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    pair_day_datas = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PairDayData))),
        graphql_name="pairDayDatas",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        PairDayData_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        PairDayData_filter, graphql_name="where", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    token_day_data = sgqlc.types.Field(
        "TokenDayData",
        graphql_name="tokenDayData",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    token_day_datas = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null("TokenDayData"))),
        graphql_name="tokenDayDatas",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        TokenDayData_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        TokenDayData_filter, graphql_name="where", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    _meta = sgqlc.types.Field(
        "_Meta_",
        graphql_name="_meta",
        args=sgqlc.types.ArgDict(
            (
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )


class Subscription(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "uniswap_factory",
        "uniswap_factories",
        "token",
        "tokens",
        "pair",
        "pairs",
        "user",
        "users",
        "liquidity_position",
        "liquidity_positions",
        "liquidity_position_snapshot",
        "liquidity_position_snapshots",
        "transaction",
        "transactions",
        "mint",
        "mints",
        "burn",
        "burns",
        "swap",
        "swaps",
        "bundle",
        "bundles",
        "uniswap_day_data",
        "uniswap_day_datas",
        "pair_hour_data",
        "pair_hour_datas",
        "pair_day_data",
        "pair_day_datas",
        "token_day_data",
        "token_day_datas",
        "_meta",
    )
    uniswap_factory = sgqlc.types.Field(
        "UniswapFactory",
        graphql_name="uniswapFactory",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    uniswap_factories = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("UniswapFactory"))
        ),
        graphql_name="uniswapFactories",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        UniswapFactory_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        UniswapFactory_filter, graphql_name="where", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    token = sgqlc.types.Field(
        "Token",
        graphql_name="token",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    tokens = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null("Token"))),
        graphql_name="tokens",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        Token_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(Token_filter, graphql_name="where", default=None),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    pair = sgqlc.types.Field(
        Pair,
        graphql_name="pair",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    pairs = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Pair))),
        graphql_name="pairs",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(Pair_orderBy, graphql_name="orderBy", default=None),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(Pair_filter, graphql_name="where", default=None),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    user = sgqlc.types.Field(
        "User",
        graphql_name="user",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    users = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null("User"))),
        graphql_name="users",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(User_orderBy, graphql_name="orderBy", default=None),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(User_filter, graphql_name="where", default=None),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    liquidity_position = sgqlc.types.Field(
        LiquidityPosition,
        graphql_name="liquidityPosition",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    liquidity_positions = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(LiquidityPosition))
        ),
        graphql_name="liquidityPositions",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        LiquidityPosition_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        LiquidityPosition_filter, graphql_name="where", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    liquidity_position_snapshot = sgqlc.types.Field(
        LiquidityPositionSnapshot,
        graphql_name="liquidityPositionSnapshot",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    liquidity_position_snapshots = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(LiquidityPositionSnapshot))
        ),
        graphql_name="liquidityPositionSnapshots",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        LiquidityPositionSnapshot_orderBy,
                        graphql_name="orderBy",
                        default=None,
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        LiquidityPositionSnapshot_filter,
                        graphql_name="where",
                        default=None,
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    transaction = sgqlc.types.Field(
        "Transaction",
        graphql_name="transaction",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    transactions = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null("Transaction"))),
        graphql_name="transactions",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        Transaction_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        Transaction_filter, graphql_name="where", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    mint = sgqlc.types.Field(
        Mint,
        graphql_name="mint",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    mints = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Mint))),
        graphql_name="mints",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(Mint_orderBy, graphql_name="orderBy", default=None),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(Mint_filter, graphql_name="where", default=None),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    burn = sgqlc.types.Field(
        Burn,
        graphql_name="burn",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    burns = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Burn))),
        graphql_name="burns",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(Burn_orderBy, graphql_name="orderBy", default=None),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(Burn_filter, graphql_name="where", default=None),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    swap = sgqlc.types.Field(
        "Swap",
        graphql_name="swap",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    swaps = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null("Swap"))),
        graphql_name="swaps",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(Swap_orderBy, graphql_name="orderBy", default=None),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(Swap_filter, graphql_name="where", default=None),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    bundle = sgqlc.types.Field(
        Bundle,
        graphql_name="bundle",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    bundles = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Bundle))),
        graphql_name="bundles",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        Bundle_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(Bundle_filter, graphql_name="where", default=None),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    uniswap_day_data = sgqlc.types.Field(
        "UniswapDayData",
        graphql_name="uniswapDayData",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    uniswap_day_datas = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("UniswapDayData"))
        ),
        graphql_name="uniswapDayDatas",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        UniswapDayData_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        UniswapDayData_filter, graphql_name="where", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    pair_hour_data = sgqlc.types.Field(
        PairHourData,
        graphql_name="pairHourData",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    pair_hour_datas = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PairHourData))),
        graphql_name="pairHourDatas",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        PairHourData_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        PairHourData_filter, graphql_name="where", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    pair_day_data = sgqlc.types.Field(
        PairDayData,
        graphql_name="pairDayData",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    pair_day_datas = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PairDayData))),
        graphql_name="pairDayDatas",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        PairDayData_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        PairDayData_filter, graphql_name="where", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    token_day_data = sgqlc.types.Field(
        "TokenDayData",
        graphql_name="tokenDayData",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    token_day_datas = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null("TokenDayData"))),
        graphql_name="tokenDayDatas",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        TokenDayData_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        TokenDayData_filter, graphql_name="where", default=None
                    ),
                ),
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )
    _meta = sgqlc.types.Field(
        "_Meta_",
        graphql_name="_meta",
        args=sgqlc.types.ArgDict(
            (
                (
                    "block",
                    sgqlc.types.Arg(Block_height, graphql_name="block", default=None),
                ),
            )
        ),
    )


class Swap(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "transaction",
        "timestamp",
        "pair",
        "sender",
        "amount0_in",
        "amount1_in",
        "amount0_out",
        "amount1_out",
        "to",
        "log_index",
        "amount_usd",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    transaction = sgqlc.types.Field(
        sgqlc.types.non_null("Transaction"), graphql_name="transaction"
    )
    timestamp = sgqlc.types.Field(
        sgqlc.types.non_null(BigInt), graphql_name="timestamp"
    )
    pair = sgqlc.types.Field(sgqlc.types.non_null(Pair), graphql_name="pair")
    sender = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name="sender")
    amount0_in = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="amount0In"
    )
    amount1_in = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="amount1In"
    )
    amount0_out = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="amount0Out"
    )
    amount1_out = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="amount1Out"
    )
    to = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name="to")
    log_index = sgqlc.types.Field(BigInt, graphql_name="logIndex")
    amount_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="amountUSD"
    )


class Token(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "symbol",
        "name",
        "decimals",
        "total_supply",
        "trade_volume",
        "trade_volume_usd",
        "untracked_volume_usd",
        "tx_count",
        "total_liquidity",
        "derived_eth",
        "most_liquid_pairs",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="symbol")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    decimals = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name="decimals")
    total_supply = sgqlc.types.Field(
        sgqlc.types.non_null(BigInt), graphql_name="totalSupply"
    )
    trade_volume = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="tradeVolume"
    )
    trade_volume_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="tradeVolumeUSD"
    )
    untracked_volume_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="untrackedVolumeUSD"
    )
    tx_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name="txCount")
    total_liquidity = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="totalLiquidity"
    )
    derived_eth = sgqlc.types.Field(BigDecimal, graphql_name="derivedETH")
    most_liquid_pairs = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(PairDayData)),
        graphql_name="mostLiquidPairs",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        PairDayData_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        PairDayData_filter, graphql_name="where", default=None
                    ),
                ),
            )
        ),
    )


class TokenDayData(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "date",
        "token",
        "daily_volume_token",
        "daily_volume_eth",
        "daily_volume_usd",
        "daily_txns",
        "total_liquidity_token",
        "total_liquidity_eth",
        "total_liquidity_usd",
        "price_usd",
        "max_stored",
        "most_liquid_pairs",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    date = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="date")
    token = sgqlc.types.Field(sgqlc.types.non_null(Token), graphql_name="token")
    daily_volume_token = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="dailyVolumeToken"
    )
    daily_volume_eth = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="dailyVolumeETH"
    )
    daily_volume_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="dailyVolumeUSD"
    )
    daily_txns = sgqlc.types.Field(
        sgqlc.types.non_null(BigInt), graphql_name="dailyTxns"
    )
    total_liquidity_token = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="totalLiquidityToken"
    )
    total_liquidity_eth = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="totalLiquidityETH"
    )
    total_liquidity_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="totalLiquidityUSD"
    )
    price_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="priceUSD"
    )
    max_stored = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="maxStored")
    most_liquid_pairs = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PairDayData))),
        graphql_name="mostLiquidPairs",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        PairDayData_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        PairDayData_filter, graphql_name="where", default=None
                    ),
                ),
            )
        ),
    )


class Transaction(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = ("id", "block_number", "timestamp", "mints", "burns", "swaps")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    block_number = sgqlc.types.Field(
        sgqlc.types.non_null(BigInt), graphql_name="blockNumber"
    )
    timestamp = sgqlc.types.Field(
        sgqlc.types.non_null(BigInt), graphql_name="timestamp"
    )
    mints = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(Mint)),
        graphql_name="mints",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(Mint_orderBy, graphql_name="orderBy", default=None),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(Mint_filter, graphql_name="where", default=None),
                ),
            )
        ),
    )
    burns = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(Burn)),
        graphql_name="burns",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(Burn_orderBy, graphql_name="orderBy", default=None),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(Burn_filter, graphql_name="where", default=None),
                ),
            )
        ),
    )
    swaps = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(Swap)),
        graphql_name="swaps",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(Swap_orderBy, graphql_name="orderBy", default=None),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(Swap_filter, graphql_name="where", default=None),
                ),
            )
        ),
    )


class UniswapDayData(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "date",
        "daily_volume_eth",
        "daily_volume_usd",
        "daily_volume_untracked",
        "total_volume_eth",
        "total_liquidity_eth",
        "total_volume_usd",
        "total_liquidity_usd",
        "max_stored",
        "most_liquid_tokens",
        "tx_count",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    date = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="date")
    daily_volume_eth = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="dailyVolumeETH"
    )
    daily_volume_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="dailyVolumeUSD"
    )
    daily_volume_untracked = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="dailyVolumeUntracked"
    )
    total_volume_eth = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="totalVolumeETH"
    )
    total_liquidity_eth = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="totalLiquidityETH"
    )
    total_volume_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="totalVolumeUSD"
    )
    total_liquidity_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="totalLiquidityUSD"
    )
    max_stored = sgqlc.types.Field(Int, graphql_name="maxStored")
    most_liquid_tokens = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TokenDayData))),
        graphql_name="mostLiquidTokens",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        TokenDayData_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        TokenDayData_filter, graphql_name="where", default=None
                    ),
                ),
            )
        ),
    )
    tx_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name="txCount")


class UniswapFactory(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = (
        "id",
        "pair_count",
        "total_volume_usd",
        "total_volume_eth",
        "untracked_volume_usd",
        "total_liquidity_usd",
        "total_liquidity_eth",
        "tx_count",
        "most_liquid_tokens",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    pair_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="pairCount")
    total_volume_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="totalVolumeUSD"
    )
    total_volume_eth = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="totalVolumeETH"
    )
    untracked_volume_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="untrackedVolumeUSD"
    )
    total_liquidity_usd = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="totalLiquidityUSD"
    )
    total_liquidity_eth = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="totalLiquidityETH"
    )
    tx_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name="txCount")
    most_liquid_tokens = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TokenDayData))),
        graphql_name="mostLiquidTokens",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        TokenDayData_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        TokenDayData_filter, graphql_name="where", default=None
                    ),
                ),
            )
        ),
    )


class User(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = ("id", "liquidity_positions", "usd_swapped")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    liquidity_positions = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(LiquidityPosition)),
        graphql_name="liquidityPositions",
        args=sgqlc.types.ArgDict(
            (
                ("skip", sgqlc.types.Arg(Int, graphql_name="skip", default=0)),
                ("first", sgqlc.types.Arg(Int, graphql_name="first", default=100)),
                (
                    "order_by",
                    sgqlc.types.Arg(
                        LiquidityPosition_orderBy, graphql_name="orderBy", default=None
                    ),
                ),
                (
                    "order_direction",
                    sgqlc.types.Arg(
                        OrderDirection, graphql_name="orderDirection", default=None
                    ),
                ),
                (
                    "where",
                    sgqlc.types.Arg(
                        LiquidityPosition_filter, graphql_name="where", default=None
                    ),
                ),
            )
        ),
    )
    usd_swapped = sgqlc.types.Field(
        sgqlc.types.non_null(BigDecimal), graphql_name="usdSwapped"
    )


class _Block_(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = ("hash", "number")
    hash = sgqlc.types.Field(Bytes, graphql_name="hash")
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="number")


class _Meta_(sgqlc.types.Type):
    __schema__ = uniswap_graphql_schema
    __field_names__ = ("block", "deployment", "has_indexing_errors")
    block = sgqlc.types.Field(sgqlc.types.non_null(_Block_), graphql_name="block")
    deployment = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="deployment"
    )
    has_indexing_errors = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="hasIndexingErrors"
    )


########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
uniswap_graphql_schema.query_type = Query
uniswap_graphql_schema.mutation_type = None
uniswap_graphql_schema.subscription_type = Subscription
