SELECT
    date_trunc('hour', time) as day,
    AVG(gas_used * 100 / gas_limit) as avg_block_filled
FROM ethereum."blocks"
WHERE time > now() - interval '14 days'
GROUP BY 1
ORDER BY 1 DESC
