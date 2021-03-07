WITH gas_prices AS(
    SELECT t.gas_price / 1e9 AS gwei
    FROM ethereum.transactions t
    WHERE t.block_time > now() - interval '5 minute'
)
SELECT
    gas_prices.gwei as gas_prices_gwei,
    ROUND(CAST(CUME_DIST() OVER (ORDER BY gas_prices.gwei ASC) * 100 as decimal(38,2)),2) || '%' cume_dist
FROM gas_prices
