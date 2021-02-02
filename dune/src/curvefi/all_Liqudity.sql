with timeseries as (select coalesce(a.day,b.day) as day, 
max(case when b.busd > 0 then b.busd else a.busd end) as busd, 
max(case when a.y > 0 then a.y else b.y end) as y, 
max(case when b.usdt > 0 then b.usdt else a.usdt end) as usdt, 
max(case when b.compound > 0 then b.compound else a.compound end) as compound,
max(case when b.susd > 0 then b.susd else a.susd end) as susd,
max(case when b.susdv2 > 0 then b.susdv2 else a.susdv2 end) as susdv2,
max(case when b.pax > 0 then b.pax else a.pax end) as pax,
max(case when b.ren > 0 then b.ren else a.ren end) as ren,
max(case when b.sbtc > 0 then b.sbtc else a.sbtc end) as sbtc,
max(case when b.hbtc > 0 then b.hbtc else a.hbtc end) as hbtc,
max(case when b.TriPool > 0 then b.TriPool else a.TriPool end) as TriPool
from (

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, max((token_supply/1e18)) AS y, 0 AS usdt, 0 AS compound, 0 as susd, 0 as susdv2, 0 as pax, 0 as ren, 0 as sbtc, 0 as hbtc, 0 as TriPool from curvefi."y_evt_AddLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."y_evt_AddLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day   group by 1

union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, 0 AS usdt, 0 AS compound, max((token_supply/1e18)) as susd, 0 as susdv2, 0 as pax, 0 as ren, 0 as sbtc, 0 as hbtc, 0 as TriPool from curvefi."susd_evt_AddLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."susd_evt_AddLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day   group by 1

union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, max((token_supply/1e18)) AS usdt, 0 AS compound, 0 as susd, 0 as susdv2, 0 as pax, 0 as ren, 0 as sbtc, 0 as hbtc, 0 as TriPool from curvefi."usdt_evt_AddLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."usdt_evt_AddLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day   group by 1

union

(select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, 0 AS usdt, max((token_supply/1e18)) AS compound, 0 as susd, 0 as susdv2, 0 as pax, 0 as ren, 0 as sbtc, 0 as hbtc, 0 as TriPool from curvefi."compound_v2_evt_AddLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."compound_v2_evt_AddLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day   group by 1

union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, 0 AS usdt, max((token_supply/1e18)) AS compound, 0 as susd, 0 as susdv2, 0 as pax, 0 as ren, 0 as sbtc, 0 as hbtc, 0 as TriPool from curvefi."compound_v3_evt_AddLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."compound_v3_evt_AddLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day   group by 1)

union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, max((token_supply/1e18)) AS busd, 0 AS y, 0 AS usdt, 0 AS compound, 0 as susd, 0 as susdv2, 0 as pax, 0 as ren, 0 as sbtc, 0 as hbtc, 0 as TriPool from curvefi."busd_evt_AddLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."busd_evt_AddLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day   group by 1


union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, 0 AS usdt, 0 AS compound, 0 as susd, max((token_supply/1e18)) as susdv2, 0 as pax, 0 as ren, 0 as sbtc, 0 as hbtc, 0 as TriPool from curvefi."susd_v2_evt_AddLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."susd_v2_evt_AddLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day   group by 1


union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, 0 AS usdt, 0 AS compound, 0 as susd, 0 as susdv2, max((token_supply / 1e18)) as pax, 0 as ren, 0 as sbtc, 0 as hbtc, 0 as TriPool from curvefi."pax_evt_AddLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."pax_evt_AddLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day   group by 1

union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, 0 AS usdt, 0 AS compound, 0 as susd, 0 as susdv2, 0 as pax, max((token_supply/1e18)) * AVG(p.price) as ren, 0 as sbtc, 0 as hbtc, 0 as TriPool from curvefi."renbtc_evt_AddLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."renbtc_evt_AddLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day
LEFT JOIN "prices".usd_2260fac5e5542a773aa44fbcfedf7c193bc2c599 p ON p.minute = date_trunc('minute', evt_block_time) group by 1

union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, 0 AS usdt, 0 AS compound, 0 as susd, 0 as susdv2, 0 as pax, 0 as ren, max((token_supply/1e18)) * AVG(p.price) as sbtc, 0 as hbtc, 0 as TriPool from curvefi."sbtc_evt_AddLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."sbtc_evt_AddLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day
LEFT JOIN "prices".usd_2260fac5e5542a773aa44fbcfedf7c193bc2c599 p ON p.minute = date_trunc('minute', evt_block_time) group by 1

union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, 0 AS usdt, 0 AS compound, 0 as susd, 0 as susdv2, 0 as pax, 0 as ren, 0 as sbtc, max((token_supply/1e18)) * AVG(p.price) as hbtc, 0 as TriPool from curvefi."hbtc_evt_AddLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."hbtc_evt_AddLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day
LEFT JOIN "prices".usd_2260fac5e5542a773aa44fbcfedf7c193bc2c599 p ON p.minute = date_trunc('minute', evt_block_time) group by 1

union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, 0 AS usdt, 0 AS compound, 0 as susd, 0 as susdv2, 0 as pax, 0 as ren, 0 as sbtc, 0 as hbtc, max((token_supply/1e18)) as TriPool from curvefi."dai_usdc_usdt_evt_AddLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."dai_usdc_usdt_evt_AddLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day   group by 1

) a


FULL OUTER JOIN 
(

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, min((token_supply/1e18)) AS y, 0 AS usdt, 0 AS compound, 0 as susd, 0 as susdv2, 0 as pax, 0 as ren, 0 as sbtc, 0 as hbtc, 0 as TriPool from curvefi."y_evt_RemoveLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."y_evt_RemoveLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day  group by 1

union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, 0 AS usdt, 0 AS compound, min((token_supply/1e18)) as susd, 0 as susdv2, 0 as pax, 0 as ren, 0 as sbtc, 0 as hbtc, 0 as TriPool from curvefi."susd_evt_RemoveLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."susd_evt_RemoveLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day  group by 1

union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, min((token_supply/1e18)) AS usdt, 0 AS compound, 0 as susd, 0 as susdv2, 0 as pax, 0 as ren, 0 as sbtc, 0 as hbtc, 0 as TriPool from curvefi."usdt_evt_RemoveLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."usdt_evt_RemoveLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day  group by 1

union

(select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, 0 AS usdt, min((token_supply/1e18)) AS compound, 0 as susd, 0 as susdv2, 0 as pax, 0 as ren, 0 as sbtc, 0 as hbtc, 0 as TriPool from curvefi."compound_v2_evt_RemoveLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."compound_v2_evt_RemoveLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day  group by 1

union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, 0 AS usdt, min((token_supply/1e18)) AS compound, 0 as susd, 0 as susdv2, 0 as pax, 0 as ren, 0 as sbtc, 0 as hbtc, 0 as TriPool from curvefi."compound_v2_evt_RemoveLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."compound_v2_evt_RemoveLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day  group by 1)

union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, min((token_supply/1e18)) AS busd, 0 AS y, 0 AS usdt, 0 AS compound, 0 as susd, 0 as susdv2, 0 as pax, 0 as ren, 0 as sbtc, 0 as hbtc, 0 as TriPool from curvefi."busd_evt_RemoveLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."busd_evt_RemoveLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day  group by 1

union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, 0 AS usdt, 0 AS compound, 0 as susd, min((token_supply / 1e18)) as susdv2, 0 as pax, 0 as ren, 0 as sbtc, 0 as hbtc, 0 as TriPool from curvefi."susd_v2_evt_RemoveLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."susd_v2_evt_RemoveLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day  group by 1

union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, 0 AS usdt, 0 AS compound, 0 as susd, 0 as susdv2, min((token_supply / 1e18)) as pax, 0 as ren, 0 as sbtc, 0 as hbtc, 0 as TriPool from curvefi."pax_evt_RemoveLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."pax_evt_RemoveLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day  group by 1

union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, 0 AS usdt, 0 AS compound, 0 as susd, 0 as susdv2, 0 as pax, min((token_supply / 1e18)) as ren, 0 as sbtc, 0 as hbtc, 0 as TriPool from curvefi."renbtc_evt_RemoveLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."renbtc_evt_RemoveLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day
LEFT JOIN "prices".usd_2260fac5e5542a773aa44fbcfedf7c193bc2c599 p ON p.minute = date_trunc('minute', evt_block_time) group by 1

union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, 0 AS usdt, 0 AS compound, 0 as susd, 0 as susdv2, 0 as pax, 0 as ren, min((token_supply / 1e18)) as sbtc, 0 as hbtc, 0 as TriPool from curvefi."sbtc_evt_RemoveLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."sbtc_evt_RemoveLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day
LEFT JOIN "prices".usd_2260fac5e5542a773aa44fbcfedf7c193bc2c599 p ON p.minute = date_trunc('minute', evt_block_time) group by 1

union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, 0 AS usdt, 0 AS compound, 0 as susd, 0 as susdv2, 0 as pax, 0 as ren, 0 as sbtc, min((token_supply / 1e18)) as hbtc, 0 as TriPool from curvefi."hbtc_evt_RemoveLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."hbtc_evt_RemoveLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day
LEFT JOIN "prices".usd_2260fac5e5542a773aa44fbcfedf7c193bc2c599 p ON p.minute = date_trunc('minute', evt_block_time) group by 1

union

select date_trunc('day', evt_block_time) AS day, max(a.mx) AS mx, 0 AS busd, 0 AS y, 0 AS usdt, 0 AS compound, 0 as susd, 0 as susdv2, 0 as pax, 0 as ren, 0 as sbtc, 0 as hbtc, min((token_supply / 1e18)) as TriPool from curvefi."dai_usdc_usdt_evt_RemoveLiquidity" csa
INNER JOIN (select date_trunc('day', evt_block_time) AS day, max(evt_block_time) mx from curvefi."dai_usdc_usdt_evt_RemoveLiquidity" csa group by 1) a ON a.mx = evt_block_time and date_trunc('day', evt_block_time) = a.day  group by 1


) b ON a.day=b.day group by 1)




select 
    day, 
    first_value(busd) over (partition by grp_busd) as busd,
    first_value(y) over (partition by grp_y) as y,
    first_value(usdt) over (partition by grp_usdt) as usdt,
    first_value(compound) over (partition by grp_compound) as compound,
    first_value(susd) over (partition by grp_susd) as susd,
    first_value(susdv2) over (partition by grp_susdv2) as susdv2,
    first_value(pax) over (partition by grp_pax) as pax,
    first_value(ren) over (partition by grp_ren) as ren,
    first_value(sbtc) over (partition by grp_sbtc) as sbtc,
    first_value(hbtc) over (partition by grp_hbtc) as hbtc,
    first_value(TriPool) over (partition by grp_TriPool) as TriPool
from (
      select day, y, usdt, compound, busd, susd, susdv2, pax, ren, sbtc, hbtc, TriPool,
             sum(case when busd > 0 then 1 end) over (order by day) as grp_busd,
             sum(case when y > 0 then 1 end) over (order by day) as grp_y,
             sum(case when usdt > 0 then 1 end) over (order by day) as grp_usdt,
             sum(case when compound > 0 then 1 end) over (order by day) as grp_compound,
             sum(case when susd > 0 then 1 end) over (order by day) as grp_susd,
             sum(case when susdv2 > 0 then 1 end) over (order by day) as grp_susdv2,
             sum(case when pax > 0 then 1 end) over (order by day) as grp_pax,
             sum(case when ren > 0 then 1 end) over (order by day) as grp_ren,
             sum(case when sbtc > 0 then 1 end) over (order by day) as grp_sbtc,
             sum(case when hbtc > 0 then 1 end) over (order by day) as grp_hbtc,
             sum(case when TriPool > 0 then 1 end) over (order by day) as grp_TriPool
      from   timeseries
) t order by 1
