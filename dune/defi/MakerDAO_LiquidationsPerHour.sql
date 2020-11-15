SELECT
date_trunc('hour', block_time) as hour,
sum(art/1e18) as liq,
sum(sum(art/1e18)) over (order by date_trunc('hour', block_time)) as total_liq ,
avg(p.price) as ETH_price
FROM makermcd."CAT_evt_Bite"
LEFT JOIN ethereum."transactions" tx ON evt_tx_hash = tx.hash
INNER JOIN prices.usd p ON p.minute = date_trunc('hour', block_time)
WHERE p.symbol = 'WETH'
GROUP BY 1
ORDER BY 1 desc
LIMIT 20
