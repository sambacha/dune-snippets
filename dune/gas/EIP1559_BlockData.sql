SELECT
    number,
    gas_limit,
    gas_used,
    base_fee_per_gas/1e9 as base_fee,
    (gas_used * base_fee_per_gas)/1e18 as "Burned ETH per Block",
    avg(base_fee_per_gas/1e9) OVER (order by number Rows Between 5 preceding and current row) as basefee_ma_5bk,
    avg((gas_used * base_fee_per_gas)/1e18) OVER (order by number Rows Between 30 preceding and current row) as "MA Burned ETH per Block",
    gas_used/gas_limit as "Block Usage",
    avg(gas_used/gas_limit) OVER (order by number Rows Between 30 preceding and current row) as "MA Block Usage",
    sum((gas_used * base_fee_per_gas)/1e18) OVER (order by number) as total_burn,
    0.5 as "Target Block Usage",
    2 as "Deflationary Limit"
FROM ethereum.blocks
WHERE time > now() - INTERVAL '6 hours'
ORDER BY number DESC
