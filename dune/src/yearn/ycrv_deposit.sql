with d as (
    select sum(curve.value) / 1e18 as deposited
    from erc20."ERC20_evt_Transfer" s
    left join erc20."ERC20_evt_Transfer" curve
        on s.evt_tx_hash = curve.evt_tx_hash
    where s.contract_address = '\x5dbcF33D8c2E976c6b560249878e6F1491Bca25c'
        and curve.contract_address = '\xdf5e0e81dff6faf3a7e52ba697820c5e32d806a8'
        and s."from" = '\x0000000000000000000000000000000000000000'
        and s."to" = curve."from"
),
w as (
    select sum(curve.value) / 1e18 as withdrawn
    from erc20."ERC20_evt_Transfer" s
    left join erc20."ERC20_evt_Transfer" curve
        on s.evt_tx_hash = curve.evt_tx_hash
    where s.contract_address = '\x5dbcF33D8c2E976c6b560249878e6F1491Bca25c'
        and curve.contract_address = '\xdf5e0e81dff6faf3a7e52ba697820c5e32d806a8'
        and s."to" = '\x0000000000000000000000000000000000000000'
        and s."from" = curve."to"
),
pretty as (
    select 
        (select * from d) as deposited, 
        (select * from w) as withdrawn
)
select 
    deposited, 
    withdrawn,
    deposited - withdrawn as in_vault
from pretty
;
