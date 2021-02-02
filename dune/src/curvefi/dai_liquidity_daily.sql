SELECT day, sum(volume) AS volume FROM (
    select date_trunc('day', block_time) AS day, sum(tokens_bought) / 1e18 as volume from curvefi."susd_v2_evt_TokenExchange" as cst
    LEFT JOIN ethereum."transactions" tx ON cst.evt_tx_hash = tx.hash
    WHERE bought_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', block_time) AS day, sum(tokens_bought) / 1e18 as volume from curvefi."susd_v2_evt_TokenExchangeUnderlying" as cst
    LEFT JOIN ethereum."transactions" tx ON cst.evt_tx_hash = tx.hash
    WHERE bought_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', block_time) AS day, sum(tokens_sold) / 1e18 as volume from curvefi."susd_v2_evt_TokenExchange" as cst
    LEFT JOIN ethereum."transactions" tx ON cst.evt_tx_hash = tx.hash
    WHERE sold_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', block_time) AS day, sum(tokens_sold) / 1e18 as volume from curvefi."susd_v2_evt_TokenExchangeUnderlying" as cst
    LEFT JOIN ethereum."transactions" tx ON cst.evt_tx_hash = tx.hash
    WHERE sold_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', block_time) AS day, sum(tokens_sold) / 1e18 as volume from curvefi."compound_v2_evt_TokenExchangeUnderlying" as cst
    LEFT JOIN ethereum."transactions" tx ON cst.evt_tx_hash = tx.hash
    WHERE bought_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', block_time) AS day, sum(tokens_sold) / 1e18 as volume from curvefi."compound_v2_evt_TokenExchangeUnderlying" as cst
    LEFT JOIN ethereum."transactions" tx ON cst.evt_tx_hash = tx.hash
    WHERE sold_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', block_time) AS day, sum(tokens_sold) / 1e18 as volume from curvefi."compound_v3_evt_TokenExchangeUnderlying" as cst
    LEFT JOIN ethereum."transactions" tx ON cst.evt_tx_hash = tx.hash
    WHERE bought_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', block_time) AS day, sum(tokens_sold) / 1e18 as volume from curvefi."compound_v3_evt_TokenExchangeUnderlying" as cst
    LEFT JOIN ethereum."transactions" tx ON cst.evt_tx_hash = tx.hash
    WHERE sold_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', block_time) AS day, sum(tokens_sold) / 1e18 as volume from curvefi."usdt_evt_TokenExchangeUnderlying" as cst
    LEFT JOIN ethereum."transactions" tx ON cst.evt_tx_hash = tx.hash
    WHERE bought_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', block_time) AS day, sum(tokens_sold) / 1e18 as volume from curvefi."usdt_evt_TokenExchangeUnderlying" as cst
    LEFT JOIN ethereum."transactions" tx ON cst.evt_tx_hash = tx.hash
    WHERE sold_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', block_time) AS day, sum(tokens_sold) / 1e18 as volume from curvefi."y_evt_TokenExchangeUnderlying" as cst
    LEFT JOIN ethereum."transactions" tx ON cst.evt_tx_hash = tx.hash
    WHERE bought_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', block_time) AS day, sum(tokens_sold) / 1e18 as volume from curvefi."y_evt_TokenExchangeUnderlying" as cst
    LEFT JOIN ethereum."transactions" tx ON cst.evt_tx_hash = tx.hash
    WHERE sold_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', block_time) AS day, sum(tokens_sold) / 1e18 as volume from curvefi."busd_evt_TokenExchangeUnderlying" as cst
    LEFT JOIN ethereum."transactions" tx ON cst.evt_tx_hash = tx.hash
    WHERE bought_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', block_time) AS day, sum(tokens_sold) / 1e18 as volume from curvefi."busd_evt_TokenExchangeUnderlying" as cst
    LEFT JOIN ethereum."transactions" tx ON cst.evt_tx_hash = tx.hash
    WHERE sold_id = 1
    
    GROUP BY 1
    
    UNION
    
    select date_trunc('day', evt_block_time) AS day, sum(tokens_sold) / 1e18 as volume from curvefi."dai_usdc_usdt_evt_TokenExchange" as cst
    WHERE sold_id = 1
    
    GROUP BY 1
) a

GROUP BY 1
ORDER BY 1
