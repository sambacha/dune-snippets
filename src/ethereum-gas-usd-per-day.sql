/// Ethereum Gas USD per Day
SELECT
date_trunc('day', tx.block_time) as date,
SUM(rs.gas_used * tx.gas_price * p.price)/1e9 as gas_usd
FROM ethereum.transactions tx 
LEFT JOIN ethereum.receipts rs ON tx."hash" = rs."tx_hash"
INNER JOIN prices.usd p ON p.minute = date_trunc('day', tx.block_time)
WHERE tx.block_time > '2017-05-01'
AND p.symbol = 'WETH'
GROUP BY 1
ORDER BY 1 DESC
LIMIT 100