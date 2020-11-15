with d as (
    select date_trunc('days', s.evt_block_time) as "time",
           sum(curve.value) / 1e18 as ycrv 
    from erc20."ERC20_evt_Transfer" s
    left join erc20."ERC20_evt_Transfer" curve
        on s.evt_tx_hash = curve.evt_tx_hash
    where s.contract_address = '\x5dbcF33D8c2E976c6b560249878e6F1491Bca25c'
        and curve.contract_address = '\xdf5e0e81dff6faf3a7e52ba697820c5e32d806a8'
        and s."from" = '\x0000000000000000000000000000000000000000'
        and s."to" = curve."from"
    group by "time"
),
w as (
    select date_trunc('days', s.evt_block_time) as "time",
           sum(curve.value) / 1e18 as ycrv
    from erc20."ERC20_evt_Transfer" s
    left join erc20."ERC20_evt_Transfer" curve
        on s.evt_tx_hash = curve.evt_tx_hash
    where s.contract_address = '\x5dbcF33D8c2E976c6b560249878e6F1491Bca25c'
        and curve.contract_address = '\xdf5e0e81dff6faf3a7e52ba697820c5e32d806a8'
        and s."to" = '\x0000000000000000000000000000000000000000'
        and s."from" = curve."to"
    group by "time"
),
pretty as (
    select *, 
           'withdrawal' as operation
    from w
    union all
    select *, 
           'deposit' as operation
    from d
)
select "time",
       operation,
       sum(ycrv) over (partition by operation order by "time" asc) as ycrv
from pretty 
;
