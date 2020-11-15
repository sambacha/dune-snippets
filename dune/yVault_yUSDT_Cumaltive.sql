with d as (
    select date_trunc('days', usdt.evt_block_time) as "time",
           sum(usdt.value) / 1e6 as usdt
    from erc20."ERC20_evt_Transfer" yusdt
    left join erc20."ERC20_evt_Transfer" usdt
        on yusdt.evt_tx_hash = usdt.evt_tx_hash
    where yusdt.contract_address = '\x2f08119C6f07c006695E079AAFc638b8789FAf18'
        and usdt.contract_address = '\xdAC17F958D2ee523a2206206994597C13D831ec7'
        and yusdt."from" = '\x0000000000000000000000000000000000000000'
        and yusdt."to" = usdt."from"
    group by "time"
),
w as (
    select date_trunc('days', yusdt.evt_block_time) as "time",
           sum(usdt.value) / 1e6 as usdt
    from erc20."ERC20_evt_Transfer" yusdt
    left join erc20."ERC20_evt_Transfer" usdt
        on yusdt.evt_tx_hash = usdt.evt_tx_hash
    where yusdt.contract_address = '\x2f08119C6f07c006695E079AAFc638b8789FAf18'
        and usdt.contract_address = '\xdAC17F958D2ee523a2206206994597C13D831ec7'
        and yusdt."to" = '\x0000000000000000000000000000000000000000'
        and yusdt."from" = usdt."to"
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
       sum(usdt) over (partition by operation order by "time" asc) as usdt
from pretty 
;
