/**
 * Get the average gas limit per block for the last 50 recent blocks
 */
SELECT block_number,
       avg(gas_price) / 10^9 AS avg_gas_price,
       min(gas_price) / 10^9 AS min_gas_price,
       max(gas_price) / 10^9 AS max_gas_price
FROM ethereum.transactions
GROUP BY block_number
ORDER BY block_number DESC
LIMIT 50