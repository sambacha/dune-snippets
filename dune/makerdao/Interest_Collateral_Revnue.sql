with raw_data as (
    select i as ilk, call_block_time, call_block_number, dart, null as rate
    from makermcd."VAT_call_frob"
    where call_success
        and dart <> 0.0
    union all
    select i as ilk, call_block_time, call_block_number, dart, 0.0 as rate
    from makermcd."VAT_call_grab"
    where call_success
        and dart <> 0.0
    union all
    select i as ilk, call_block_time, call_block_number, null as dart, rate 
    from makermcd."VAT_call_fold"
    where call_success
        and rate <> 0.0
),
running_amounts as (
    select ilk, call_block_time, call_block_number, rate, sum(dart) over(partition by ilk order by call_block_number asc) as dart
    from raw_data 
),
debt_revenues as (
    select ilk, call_block_time, call_block_number, dart, dart * rate/10^45 as interest
    from running_amounts
    where rate is not null
),
revenues_ilk_detail as (
    select to_char(call_block_time, 'YYYY-MM') as period,  replace(encode(ilk, 'escape'), '\000', '') as collateral, sum(interest) as revenues
    from debt_revenues
    group by 1, 2
),
other_cat as (
    select collateral, sum(revenues) as collateral_total_revenues
    from revenues_ilk_detail
    group by 1
),
other_ca_order as (
    select collateral, row_number() over (order by collateral_total_revenues desc) as collateral_rank
    from other_cat
    where collateral not in ('USDC-A', 'USDC-B', 'TUSD-A', 'GUSD-A', 'PAXUSD-A', 'PSM-USDC-A')
)
select 
    period, case when collateral_rank > 5 then 'Others' else collateral end as collateral, 
        case when collateral_rank > 5 then 99 else collateral_rank end as collateral_rank,
    sum(revenues) as revenues
from revenues_ilk_detail
inner join other_ca_order using (collateral)
group by 1, 2, 3
order by 1 desc
