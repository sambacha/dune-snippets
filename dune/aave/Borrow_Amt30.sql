SELECT sum(amt*price)  as borrow
FROM
(

-- Aave v1
SELECT sum("_amount"/10^decimals) as amt
        ,t.symbol as token
        ,date(evt_block_time) as dt
FROM aave."LendingPool_evt_Borrow" Borrow 
LEFT JOIN erc20."tokens" t ON Borrow."_reserve" = t.contract_address
WHERE evt_block_time > now() - interval '30 days'
GROUP BY 2,3

UNION ALL

-- Aave v2 
SELECT sum("amount"/10^decimals) as amt
        ,t.symbol as token
        ,date(evt_block_time) as dt
FROM aave_v2."LendingPool_evt_Borrow" Borrow 
LEFT JOIN erc20."tokens" t ON Borrow."reserve" = t.contract_address
WHERE evt_block_time > now() - interval '30 days'
GROUP BY 2,3

)main

LEFT JOIN 


    (SELECT avg(price) AS price,
              date(MINUTE) AS dt,
              symbol
       FROM prices.usd
       WHERE symbol<>'ETH'
       AND MINUTE > now() - interval '30 days'
       GROUP BY 2,
                3
                
       UNION SELECT avg(price) AS price,
                    date(MINUTE) AS dt,
                    symbol
       FROM prices.layer1_usd_eth
       WHERE symbol='ETH'
       AND MINUTE > now() - interval '30 days'
       GROUP BY 2,
                3)p

ON main.dt = p.dt
AND p.symbol = main.token
