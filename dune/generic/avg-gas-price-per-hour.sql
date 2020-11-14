/// average gas price per hour

SELECT date_trunc('hour', block_time) as time,
       avg(gas_price) / 10^9 AS avg_gas_price,
       min(gas_price) / 10^9 AS min_gas_price,
       max(gas_price) / 10^9 AS max_gas_price
FROM ethereum.transactions
WHERE block_time > now() - interval '14 days'
GROUP BY 1
ORDER BY 1 DESC