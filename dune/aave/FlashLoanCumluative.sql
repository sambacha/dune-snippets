WITH fl AS 
(
SELECT
evt_block_time,
t.symbol as token,
sum("amount"/10^decimals) as amount
FROM aave_v2."LendingPool_evt_FlashLoan" fl
LEFT JOIN erc20."tokens" t ON fl."asset" = t.contract_address
GROUP BY 1,2
)

select dt, sum(USDamt) over (
                        ORDER BY dt ASC ROWS BETWEEN unbounded preceding AND CURRENT ROW) AS total_usd
from
(select dt,sum(USDamt) as USDamt
from
(select min(day) as dt,
        USDvalue as USDamt
from
(SELECT 
date_trunc('day',evt_block_time) as day, 
sum(amount*price) As USDvalue
from fl
LEFT JOIN 
(SELECT avg(price) AS price,
          date(MINUTE) AS dt,
          symbol
   FROM prices.usd
   WHERE symbol<>'ETH'
   GROUP BY 2,
            3
   UNION SELECT avg(price) AS price,
                date(MINUTE) AS dt,
                symbol
   FROM prices.layer1_usd_eth
   WHERE symbol='ETH'
   GROUP BY 2,
            3)p
            ON date(evt_block_time) = p.dt
AND p.symbol = fl.token
group by 1) t1
group by 2) t2
group by 1)t3
