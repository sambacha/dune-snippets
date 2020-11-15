SELECT date(block_time_solution) AS day,
    AVG(token_usd_price)
FROM gnosis_protocol.view_price_batch
WHERE token_id=7
GROUP BY day
ORDER BY day asc
