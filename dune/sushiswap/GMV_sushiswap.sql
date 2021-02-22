WITH recet120 AS
  (SELECT date_trunc('day', block_time) as date,
          sum(usd_amount) AS daily_usd_amount
   FROM dex."trades" t
   WHERE project = 'Sushiswap'
     AND date_trunc('day', block_time) > now() - interval '240 days'
   GROUP BY 1
   ORDER BY 1 DESC),

F0_30 AS
  (SELECT daily_usd_amount,date
   FROM recet120
   LIMIT 30),

F90_120 AS
  (SELECT daily_usd_amount,date
   FROM recet120
   LIMIT 30 OFFSET 90),
   
-- SELECT sum(a.daily_usd_amount) as recent0_30
-- FROM F0_30 a, F90_120 b

a as (SELECT sum(daily_usd_amount) as total_usd_amount from F0_30),
b as (SELECT sum(daily_usd_amount) as total_usd_amount from F90_120)

select a.total_usd_amount as total_usd_volume_0_30, 
    b.total_usd_amount as total_usd_volume_90_120,
    POWER(a.total_usd_amount/b.total_usd_amount , 4) -1 as annualized_growth_rate
from a a,b b
