SELECT day, sum(volume) AS volume FROM (
    select date_trunc('day', evt_block_time) AS day, ((sum(tokens_bought) / 1e8) * AVG(p.price)) as volume from curvefi."renbtc_evt_TokenExchange" as cst
    LEFT JOIN prices.usd_2260fac5e5542a773aa44fbcfedf7c193bc2c599 p ON p.minute = date_trunc('minute', evt_block_time)
    WHERE bought_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', evt_block_time) AS day, (sum(tokens_sold) / 1e8 * AVG(p.price)) as volume from curvefi."renbtc_evt_TokenExchange" as cst
    LEFT JOIN prices.usd_2260fac5e5542a773aa44fbcfedf7c193bc2c599 p ON p.minute = date_trunc('minute', evt_block_time)
    WHERE sold_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', evt_block_time) AS day, ((sum(tokens_bought) / 1e8) * AVG(p.price)) as volume from curvefi."sbtc_evt_TokenExchange" as cst
    LEFT JOIN prices.usd_2260fac5e5542a773aa44fbcfedf7c193bc2c599 p ON p.minute = date_trunc('minute', evt_block_time)
    WHERE bought_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', evt_block_time) AS day, (sum(tokens_sold) / 1e8 * AVG(p.price)) as volume from curvefi."sbtc_evt_TokenExchange" as cst
    LEFT JOIN prices.usd_2260fac5e5542a773aa44fbcfedf7c193bc2c599 p ON p.minute = date_trunc('minute', evt_block_time)
    WHERE sold_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', evt_block_time) AS day, ((sum(tokens_bought) / 1e18) * AVG(p.price)) as volume from curvefi."hbtc_evt_TokenExchange" as cst
    LEFT JOIN prices.usd_2260fac5e5542a773aa44fbcfedf7c193bc2c599 p ON p.minute = date_trunc('minute', evt_block_time)
    WHERE bought_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', evt_block_time) AS day, (sum(tokens_sold) / 1e18 * AVG(p.price)) as volume from curvefi."hbtc_evt_TokenExchange" as cst
    LEFT JOIN prices.usd_2260fac5e5542a773aa44fbcfedf7c193bc2c599 p ON p.minute = date_trunc('minute', evt_block_time)
    WHERE sold_id = 1
    
    GROUP BY 1
) a

GROUP BY 1
ORDER BY 1
