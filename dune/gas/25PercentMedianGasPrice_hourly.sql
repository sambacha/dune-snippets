SELECT
    DATE_TRUNC('hour',block_time) AS dt
    , (PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY gas_price)) / 1e9  AS _25_gas_price_gwei
    , (PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY gas_price)) / 1e9  AS median_gas_price_gwei
    , (PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY gas_price)) / 1e9  AS _75_gas_price_gwei
FROM ethereum.transactions
WHERE
    block_time >= (DATE_TRUNC('hour',CURRENT_TIMESTAMP) - '3 days'::INTERVAL)
GROUP BY 1
ORDER BY 1;
