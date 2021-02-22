WITH prices AS (
    SELECT  *
    FROM prices.usd
    where minute > now() - interval '6 months'
),

users AS (
    SELECT block_time, a.trader_a AS trader
    FROM dex.trades a
    WHERE block_time > now() - interval '6 months'
    and project = 'Sushiswap'
    UNION
    SELECT block_time, a.trader_b AS trader
    FROM dex.trades a
    WHERE block_time > now() - interval '6 months'
    and project = 'Sushiswap'
)

SELECT  date_trunc('week', t.block_time) as week,
        COUNT(DISTINCT u.trader) AS unique_traders,
         (SUM(COALESCE(
                    usd_amount,                 
                    token_a_amount * a.price,  
                    token_b_amount * b.price    
                ))) as usd_volume,
        SUM(COALESCE(
                    usd_amount,                 
                    token_a_amount * a.price,  
                    token_b_amount * b.price    
                )*0.0025) as usd_protocol_fees,
        SUM(COALESCE(
                    usd_amount,                 
                    token_a_amount * a.price,  
                    token_b_amount * b.price    
                )*0.0005) as usd_tokenholder_fees        
        FROM dex."trades" t
LEFT JOIN prices a ON date_trunc('minute', block_time) = a.minute AND token_a_address = a.contract_address 
LEFT JOIN prices b ON date_trunc('minute', block_time) = b.minute AND token_b_address = b.contract_address 
LEFT JOIN users u ON t.block_time = u.block_time 
WHERE t.block_time > now() - interval '6 months'
and t.project = 'Sushiswap'
GROUP BY 1 
ORDER BY 1 DESC;
