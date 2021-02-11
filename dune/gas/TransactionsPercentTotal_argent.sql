with relays as 
(select DISTINCT "from" from ethereum.transactions where "to" = '\x2B6D87F12B106E1D3fA7137494751566329d1045'),


all_txs as (select * from ethereum.transactions e 
where e.block_time >= (DATE_TRUNC('day',CURRENT_TIMESTAMP) - '60 days'::INTERVAL)),

argent_txs as (select * from all_txs 
where "from" IN (select "from"::bytea from relays)),

all_tx_cost as(select date_trunc('day', block_time), sum(gas_used) as "Total_Gas", count(all_txs.hash) as "Total_Transactions"
    from all_txs
    group by 1),
    
argent_tx_cost as(select date_trunc('day', block_time), sum(gas_used) "Argent_Gas", count(argent_txs.hash) as "Argent_Transactions"
    from argent_txs
    group by 1)
    
select l.date_trunc as "Date", l."Total_Gas", t."Argent_Gas", l."Total_Gas" - t."Argent_Gas" as "Diff", t."Argent_Gas" / l."Total_Gas" as "Ratio", (t."Argent_Gas" / l."Total_Gas") * 100 as "Gas Percentage", 
"Total_Transactions", "Argent_Transactions", "Argent_Transactions"::float/"Total_Transactions"::float * 100 as "Trasaction Percentage"
from all_tx_cost l Left join argent_tx_cost t on l.date_trunc = t.date_trunc
