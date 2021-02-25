with items as (
    select 'PnL' as item, 0 as item_rank, '1 - PnL' as label
    union all 
    select 'Lending Revenues' as item, 1 as item_rank, '1.1 - Lending Revenues' as label
    union all
    select 'Liquidations Revenues' as item, 2 as item_rank, '1.2 - Liquidations Revenues' as label
    union all
    select 'Trading Revenues' as item, 3 as item_rank, '1.3 - Trading Revenues' as label
    union all
    select 'Lending Expenses' as item, 4 as item_rank, '1.4 - Lending Expenses' as label
    union all
    select 'Liquidations Expenses' as item, 5 as item_rank, '1.5 - Liquidations Expenses' as label
    union all
    select 'Workforce Expenses' as item, 6 as item_rank, '1.6 - Workforce Expenses' as label
    union all
    select 'Net Income' as item, 6 as item_rank, '1.9 - Net Income' as label
    union all
    select 'Assets' as item, 100 as item_rank, '2 - Assets' as label
    union all
    select 'Crypto Loans' as item, 101 as item_rank, '2.1 - Crypto Loans' as label
    union all
    select 'Trading Assets' as item, 102 as item_rank, '2.2 - Trading Assets' as label
    union all
    select 'Total Assets' as item, 199 as item_rank, '2.9 - Total Assets' as label
    union all
    select 'Liabilities & Equity' as item, 200 as item_rank, '3 - Liabilities & Equity' as label
    union all
    select 'Liabilities (DAI)' as item, 201 as item_rank, '3.1 - Liabilities (DAI)' as label
    union all
    select 'Equity (Surplus Buffer)' as item, 202 as item_rank, '3.2 - Equity (Surplus Buffer)' as label
    union all
    select 'Total Liabilities & Equity' as item, 299 as item_rank, '3.9 - Total Liabilities & Equity' as label
    
),
periods as (
    select period::date, extract(year from period) as year, extract(month from period) as month
    from generate_series('2019-11-01'::date, current_date, '1 months') period
),
maker_addresses as (
    select '\xa950524441892a31ebddf91d3ceefa04bf454466'::bytea as address, 'Vow' as name
),
contracts as(
    select 'PSM' as contrat_type, '\x89b78cfa322f6c5de0abceecab66aee45393cc5a'::bytea as contract_address -- PM
    union all
    select distinct 'FlapFlop' as contrat_type, data from makermcd."VOW_call_file0" -- Vow Flappers and Floppers 
),
liquidation_excluded_tx as (
    select distinct tx_hash
    from ethereum."traces"
    inner join contracts on "from" = contract_address
    where contrat_type in ('PSM', 'FlapFlop')
),
liquidation_revenues as (
    select extract(year from call_block_time) as year, extract(month from call_block_time) as month, sum(rad/10^45) as revenues
    from makermcd."VAT_call_move"
    where dst = '\xa950524441892a31ebddf91d3ceefa04bf454466' -- vow
        and call_success
        and call_tx_hash not in (select * from liquidation_excluded_tx)
    group by 1, 2
),
liquidation_expenses as (
    select extract(year from call_block_time) as year, extract(month from call_block_time) as month, sum(tab/10^45) as expenses
    from makermcd."VOW_call_fess"
    where call_success
    group by 1, 2
),
liquidation as (
    select year, month, 
        case when revenues > expenses then revenues - expenses end as liquidation_revenues, 
        case when revenues < expenses then expenses - revenues end as liquidation_expenses
    from liquidation_revenues
    full outer join liquidation_expenses using (year, month)
),
trading_tx as (
    select distinct call_tx_hash
    from makermcd."VAT_call_frob"
    where replace(encode(i, 'escape'), '\000', '') = 'PSM-USDC-A'
        and call_success
),
trading_revenues as (
    select extract(year from call_block_time) as year, extract(month from call_block_time) as month, sum(rad)/10^45 as trading_revenues
    from makermcd."VAT_call_move" 
    inner join trading_tx using (call_tx_hash)
    where call_success
        and dst = '\xa950524441892a31ebddf91d3ceefa04bf454466' -- Vow
    group by 1, 2
),
lending_expenses as ( 
    select extract(year from call_block_time) as year, extract(month from call_block_time) as month, sum(rad)/10^45 as lending_expenses
    from makermcd."VAT_call_suck"
    where u = '\xa950524441892a31ebddf91d3ceefa04bf454466' -- Vow
        and v = '\x197e90f9fad81970ba7976f33cbd77088e5d7cf7' -- Pot
        and call_success
    group by 1, 2
),
lending_revenues_1 as (
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
lending_revenues_2 as (
    select *, sum(dart) over(partition by ilk order by call_block_number asc) as debt
    from lending_revenues_1 
),
lending_revenues_3 as (
    select replace(encode(ilk, 'escape'), '\000', '') as ilk, extract(year from call_block_time) as year, extract(month from call_block_time) as month, sum(debt * rate)/10^45 as lending_revenues
    from lending_revenues_2
    where rate is not null
    group by 1, 2, 3
),
lending_revenues as (
    select year, month, 
        -- Stablescoins vault with fixed value is counted as trading revenues, not sure what to do with USDC-B
        sum(case when ilk not in ('USDC-A', 'USDC-B', 'TUSD-A', 'USDT-A', 'PAXUSD-A', 'GUSD-A') then lending_revenues end) as lending_revenues,
        sum(case when ilk in ('USDC-A', 'USDC-B', 'TUSD-A', 'USDT-A', 'PAXUSD-A', 'GUSD-A') then lending_revenues end) as stablecoin_lending_revenues
    from lending_revenues_3
    group by 1, 2
),
-- List all suck operation from executive actions
operating_expenses_suck_tx as (
    select distinct call_tx_hash
    from makermcd."VAT_call_suck"
    where "u" = '\xa950524441892a31ebddf91d3ceefa04bf454466' -- Vow
        and "v" = '\xbe8e3e3618f7474f8cb1d074a26affef007e98fb' -- DS Pause Proxy
        and call_success
),
-- When a suck operation is used to directly transfer DAI to a third party
operating_expenses_direct as (
    select extract(year from evt_block_time) as year, extract(month from evt_block_time) as month, sum(value)/10^18 as operating_expenses_direct
    from erc20."ERC20_evt_Transfer"
    inner join operating_expenses_suck_tx on  evt_tx_hash = call_tx_hash
    where "from" = '\x0000000000000000000000000000000000000000'
        and "to" not in ( 
                '\x73f09254a81e1f835ee442d1b3262c1f1d7a13ff', -- Interim multisig
                '\xbe8e3e3618f7474f8cb1d074a26affef007e98fb', -- DS Pause Proxy
                '\x0000000000000000000000000000000000000000' -- DAI ERC-20 minting
            )
        and contract_address = '\x6b175474e89094c44da98b954eedeac495271d0f' -- DAI ERC-20
    group by 1, 2
),
-- When a DAO owned wallet is making an expense
operating_expenses as ( 
    select extract(year from evt_block_time) as year, extract(month from evt_block_time) as month, sum(value)/10^18 as operating_expenses
    from erc20."ERC20_evt_Transfer"
    where "from" in (
                '\x73f09254a81e1f835ee442d1b3262c1f1d7a13ff', -- Interim multisig
                '\xbe8e3e3618f7474f8cb1d074a26affef007e98fb' -- DS Pause Proxy
            )
        and "to" not in ( 
                '\x73f09254a81e1f835ee442d1b3262c1f1d7a13ff', -- Interim multisig
                '\xbe8e3e3618f7474f8cb1d074a26affef007e98fb', -- DS Pause Proxy
                '\x0000000000000000000000000000000000000000' -- DAI ERC-20 creation from the Maker internal system
            )
        and contract_address = '\x6b175474e89094c44da98b954eedeac495271d0f' -- DAI ERC-20
    group by 1, 2
),
-- When we got incoming money on a DAO owned wallet.
operating_expenses_reverse as ( 
    select extract(year from evt_block_time) as year, extract(month from evt_block_time) as month, sum(value)/10^18 as operating_expenses_reverse
    from erc20."ERC20_evt_Transfer"
    where "from" not in (
                '\x73f09254a81e1f835ee442d1b3262c1f1d7a13ff', -- Interim multisig
                '\xbe8e3e3618f7474f8cb1d074a26affef007e98fb', -- DS Pause Proxy
                '\x0000000000000000000000000000000000000000' -- DAI ERC-20 creation from the Maker internal system
            )
        and "to" in ( 
                '\x73f09254a81e1f835ee442d1b3262c1f1d7a13ff', -- Interim multisig
                '\xbe8e3e3618f7474f8cb1d074a26affef007e98fb' -- DS Pause Proxy
            )
        and contract_address = '\x6b175474e89094c44da98b954eedeac495271d0f' -- DAI ERC-20
    group by 1, 2
),
------------------------------------------------------------------------------------------
--- ASSETS
-------------------------------------------------------------------------------------------
assets_1 as (
    select i as ilk, call_block_time, call_block_number, dart as dart, null as rate
    from makermcd."VAT_call_frob"
    where call_success
        and dart <> 0.0
    union all
    select i as ilk, call_block_time, call_block_number, dart as dart, 0.0 as rate
    from makermcd."VAT_call_grab"
    where call_success
        and dart <> 0.0
    union all
    select i as ilk, call_block_time, call_block_number, null as dart, rate as rate 
    from makermcd."VAT_call_fold"
    where call_success
        and rate <> 0.0
),
assets_2 as (
    select ilk, call_block_time, call_block_number, 
        coalesce(1+sum(rate) over(partition by ilk order by call_block_number asc)/10^27,1) as rate,
        sum(dart) over(partition by ilk order by call_block_number asc)/10^18 as dart
    from assets_1 
),
assets_with_rk as (
    select to_char(call_block_time, 'YYYY-MM') as period, extract(year from call_block_time) as year, extract(month from call_block_time) as month, 
        replace(encode(ilk, 'escape'), '\000', '') as collateral, 
        dart*rate as asset_value,
        row_number() over (partition by ilk, to_char(call_block_time, 'YYYY-MM') order by call_block_time desc) as rk
    from assets_2
),
assets_group_by as (
    select *
    from assets_with_rk
    where rk = 1
        and asset_value <> 0.0
),
assets as ( 
    select year, month, sum(asset_value) as asset_value,
        sum(case when collateral like 'PSM%' or collateral in ('USDC-A','USDC-B','SAI', 'TUSD-A','GUSD-A','PAXUSD-A') 
            then asset_value end) as other_assets,
        sum(case when collateral not like 'PSM%' and collateral not in ('USDC-A','USDC-B','SAI', 'TUSD-A','GUSD-A','PAXUSD-A') 
            then asset_value end) as crypto_loans
    from assets_group_by
    group by 1, 2
),
sb_dai_in as (
    select extract(year from call_block_time) as year, extract(month from call_block_time) as month, sum(rad/10^45) as dai_inflow
    from makermcd."VAT_call_move"
    where dst in (select address from maker_addresses)
        and call_success
    group by 1, 2
),
sb_dai_out as (
    select extract(year from call_block_time) as year, extract(month from call_block_time) as month, sum(rad/10^45) as dai_outflow
    from makermcd."VAT_call_move"
    where src in (select address from maker_addresses)
        and call_success
    group by 1, 2
),
sb_sin_out as (
    select extract(year from call_block_time) as year, extract(month from call_block_time) as month, sum(rad/10^45) as sin_outflow
    from makermcd."VAT_call_suck"
    where u in (select address from maker_addresses)
        and call_success
    group by 1, 2
),
sb_sin_in as (
    select extract(year from call_block_time) as year, extract(month from call_block_time) as month, sum(rad/10^45) as sin_inflow
    from makermcd."VAT_call_suck"
    where v in (select address from maker_addresses)
        and call_success
    group by 1, 2
),
sb_fess as (
    select extract(year from call_block_time) as year, extract(month from call_block_time) as month, sum(tab/10^45) as fess
    from makermcd."VOW_call_fess"
    where call_success
    group by 1, 2
),
sb_accrued_interest_1 as (
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
    select i as ilk, call_block_time-interval'5 second' /* to be sure frob is called first */, call_block_number, null as dart, rate 
    from makermcd."VAT_call_fold"
    where call_success
        and rate <> 0.0
),
sb_accrued_interest_2 as (
    select *, sum(dart) over(partition by ilk order by call_block_time asc) as debt
    from sb_accrued_interest_1 
),
sb_accrued_interest_3 as (
    select replace(encode(ilk, 'escape'), '\000', '') as ilk, extract(year from call_block_time) as year, 
        extract(month from call_block_time) as month, sum(debt * rate)/10^45 as lending_revenues
    from sb_accrued_interest_2
    where rate is not null
    group by 1, 2, 3
),
sb_accrued_interest as (
    select year, month, sum(lending_revenues) as accrued_interests
    from sb_accrued_interest_3
    group by 1, 2
),
sb_fusion as (
    select year, month, sum(dai_inflow) as dai_inflow, sum(dai_outflow) as dai_outflow, sum(sin_outflow) as sin_outflow, sum(sin_inflow) as sin_inflow, 
        sum(fess) as fess, sum(accrued_interests) as accrued_interests
    from periods
    left join sb_dai_in using (year, month)
    left join sb_dai_out using (year, month)
    left join sb_sin_out using (year, month)
    left join sb_sin_in using (year, month)
    left join sb_fess using (year, month)
    left join sb_accrued_interest using (year, month)
    group by 1, 2
),
sb as (
    select year, month,
        sum(coalesce(dai_inflow, 0)-coalesce(dai_outflow, 0)-coalesce(sin_outflow, 0)+coalesce(sin_inflow, 0)
            -coalesce(fess, 0)+coalesce(accrued_interests, 0)) over (order by year, month) as surplus_buffer
    from sb_fusion 
)
select extract(year from period) as year, extract(month from period) as month, label as item, 
    sum(case item 
        when 'Liquidations Revenues' then liquidation_revenues
        when 'Liquidations Expenses' then -liquidation_expenses
        when 'Trading Revenues' then coalesce(trading_revenues,0) + coalesce(stablecoin_lending_revenues,0)
        when 'Lending Revenues' then lending_revenues
        when 'Lending Expenses' then -lending_expenses
        when 'Workforce Expenses' then coalesce(-operating_expenses,0)+coalesce(-operating_expenses_direct,0)+coalesce(operating_expenses_reverse,0)
        when 'Net Income' then 
            coalesce(liquidation_revenues,0) + coalesce(-liquidation_expenses,0) 
            + coalesce(trading_revenues,0) + coalesce(stablecoin_lending_revenues,0)
            + coalesce(lending_revenues,0) + coalesce(-lending_expenses,0)
            + coalesce(-operating_expenses,0)+coalesce(-operating_expenses_direct,0)+coalesce(operating_expenses_reverse,0)
        when 'Crypto Loans' then crypto_loans
        when 'Trading Assets' then other_assets
        when 'Total Assets' then asset_value
        when 'Total Assets' then asset_value
        when 'Liabilities (DAI)' then coalesce(asset_value,0)-coalesce(surplus_buffer,0)
        when 'Equity (Surplus Buffer)' then coalesce(surplus_buffer,0)
        when 'Total Liabilities & Equity' then asset_value
        end
        ) as value
from periods
cross join items
left outer join liquidation using (year, month)
left outer join trading_revenues using (year, month)
left outer join lending_expenses using (year, month)
left outer join lending_revenues using (year, month)
left outer join operating_expenses_direct using (year, month)
left outer join operating_expenses using (year, month)
left outer join operating_expenses_reverse using (year, month)
left outer join assets using (year, month)
left outer join sb using (year, month)
group by 1, 2, 3
