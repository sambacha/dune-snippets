WITH
    median_gas_price AS (
        SELECT
            (PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY gas_price))  AS median_gas_price
        FROM ethereum.transactions
        WHERE
            block_time >= (CURRENT_TIMESTAMP - '15 minutes'::INTERVAL)    
    )
    , eth_price AS (
        SELECT DISTINCT
            LAST_VALUE(price)
                OVER
                (
                    ORDER BY minute
                    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
                ) AS price
        FROM prices.layer1_usd_eth
        WHERE
            minute > (CURRENT_DATE - '1 days'::INTERVAL)
    )
    SELECT
        mgp.median_gas_price / 1e9 AS median_gas_price
        , ((mgp.median_gas_price * 21000) / 1e18) * ep.price AS cost_of_eth_transfer
        , ((mgp.median_gas_price * 41209) / 1e18) * ep.price AS cost_of_erc20_transfer
        , ((mgp.median_gas_price * 126899) / 1e18) * ep.price AS cost_of_uniswap_trade
        , ((mgp.median_gas_price * 189275) / 1e18) * ep.price AS cost_of_compound_erc20_deposit
        --, ((mgp.median_gas_price * 225000) / 1e18) * ep.price AS cost_of_0x_fill
        --, ((mgp.median_gas_price * 471097) / 1e18) * ep.price AS cost_of_kyber_trade
    FROM median_gas_price mgp
    CROSS JOIN eth_price ep;
