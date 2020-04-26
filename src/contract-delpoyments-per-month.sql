/// Contract Deployments Per Month
SELECT date_trunc('month', block_time),
count(*),
SUM(gas_used * (
            SELECT AVG(p.price)
            FROM prices."usd" p
            WHERE p.symbol = 'ETH'
            AND p.minute = date_trunc('minute', t.block_time)
            LIMIT 1
        )*0.000000001)
FROM ethereum.traces t
WHERE block_time >= now()::date - interval '1 year'
AND block_time < date_trunc('month', NOW())
AND type='create'
AND tx_success = true
GROUP BY 1;