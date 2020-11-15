-- mind decimals! usdc: 10 ^ 6
with d as (
    select date_trunc('days', s.evt_block_time) as "time",
           sum(usdc.value) / 1e6 as usdc
    from erc20."ERC20_evt_Transfer" s
    left join erc20."ERC20_evt_Transfer" usdc
        on s.evt_tx_hash = usdc.evt_tx_hash
    where s.contract_address = '\x597aD1e0c13Bfe8025993D9e79C69E1c0233522e'
        and usdc.contract_address = '\xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'
        and s."from" = '\x0000000000000000000000000000000000000000'
        and s."to" = usdc."from"
    group by "time"
),
w as (
    select date_trunc('days', s.evt_block_time) as "time",
           sum(usdc.value) / 1e6 as usdc
    from erc20."ERC20_evt_Transfer" s
    left join erc20."ERC20_evt_Transfer" usdc
        on s.evt_tx_hash = usdc.evt_tx_hash
    where s.contract_address = '\x597aD1e0c13Bfe8025993D9e79C69E1c0233522e'
        and usdc.contract_address = '\xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'
        and s."to" = '\x0000000000000000000000000000000000000000'
        and s."from" = usdc."to"
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
       sum(usdc) over (partition by operation order by "time" asc) as usdc
from pretty 
;
