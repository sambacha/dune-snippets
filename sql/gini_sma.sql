with double_entry_book as (
  select to_address as address, value as value, block_timestamp as row_timestamp
    -- debits
    from `bigquery-public-data.crypto_ethereum_classic.traces`
    where to_address is not null
    and status = 1
    and (call_type not in ('delegatecall', 'callcode', 'staticcall') or call_type is null)
    union all
    -- credits
    select from_address as address, -value as value, block_timestamp as row_timestamp
    from `bigquery-public-data.crypto_ethereum_classic.traces`
    where from_address is not null
    and status = 1
    and (call_type not in ('delegatecall', 'callcode', 'staticcall') or call_type is null)
    union all
    -- transaction fees debits
    select miner as address, sum(cast(receipt_gas_used as numeric) * cast(gas_price as numeric)) as value, block_timestamp as row_timestamp
    from `bigquery-public-data.crypto_ethereum_classic.transactions` as transactions
    join `bigquery-public-data.crypto_ethereum_classic.blocks` as blocks on blocks.number = transactions.block_number and blocks.timestamp = transactions.block_timestamp
    group by blocks.miner, block_timestamp
    union all
    -- transaction fees credits
    select from_address as address, -(cast(receipt_gas_used as numeric) * cast(gas_price as numeric)) as value, block_timestamp as row_timestamp
    from `bigquery-public-data.crypto_ethereum_classic.transactions`
),
double_entry_book_by_date as (
  select 
        date(row_timestamp) as date, 
        address, 
        sum(value * 0.00000001) as value
    from double_entry_book
    group by address, date
),
daily_balances_with_gaps as (
    select
        address,
        date,
        sum(value) over (partition by address order by date) as balance,
        lead(date, 1, current_date()) over (partition by address order by date) as next_date
        from double_entry_book_by_date
),
calendar as (
    select date from unnest(generate_date_array('2015-07-30', current_date())) as date
),
daily_balances as (
    select address, calendar.date, balance
    from daily_balances_with_gaps
    join calendar on daily_balances_with_gaps.date <= calendar.date and calendar.date < daily_balances_with_gaps.next_date
    where balance > 1
),
address_counts as (
    select
        date,
        count(*) as address_count
    from
        daily_balances
    group by date
),
daily_balances_sampled as (
    select address, daily_balances.date, balance
    from daily_balances
    join address_counts on daily_balances.date = address_counts.date
    where mod(abs(farm_fingerprint(address)), 100000000)/100000000 <= safe_divide(10000, address_count)
),
ranked_daily_balances as (
    select
        date,
        balance,
        row_number() over (partition by date order by balance desc) as rank
    from daily_balances
),
gini_daily as (
   select
    date,
    -- (1 − 2B) https://en.wikipedia.org/wiki/Gini_coefficient
    1 - 2 * sum((balance * (rank - 1) + balance / 2)) / count(*) / sum(balance) as gini
  from ranked_daily_balances
  group by date
having sum(balance) > 1
order by date asc
)
select date,
avg(gini) over (order by date asc rows 7 preceding) as gini_sma7
from gini_daily
order by date asc
