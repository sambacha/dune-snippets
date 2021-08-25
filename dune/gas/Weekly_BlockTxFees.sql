WITH tx AS(
    SELECT
        date_trunc('hour', block_time) as hour,
        block_number,
        t.hash,
        type,
        --gas_price as gas_price,
        t.gas_used,
        CASE WHEN priority_fee_per_gas IS NOT NULL THEN priority_fee_per_gas ELSE gas_price-b.base_fee_per_gas END as priority_fee_per_gas,
        b.base_fee_per_gas as block_base_fee
    FROM ethereum.transactions t
    LEFT JOIN ethereum.blocks b ON block_number = number
    WHERE block_time > now() - INTERVAL '1 weeks'
    AND success
),
block_fees AS(
    SELECT
        block_number,
        hour,
        SUM(gas_used*priority_fee_per_gas)/1e18 as priority_total,
        SUM(gas_used*Block_base_fee)/1e18 as base_total
    FROM tx
    GROUP BY 1,2
),
hour_fees AS(
    SELECT
        t.hour,
        AVG(block_base_fee) AS block_base_fee,
        AVG(priority_fee_per_gas/1e9) as avg_priority_fee,
        AVG(priority_total) as priority_total,
        AVG(base_total) as base_total,
        COUNT(hash) FILTER (WHERE type = 'Legacy') AS legacy_count,
        COUNT(hash) FILTER (WHERE type = 'DynamicFee') AS dynamicFee_count
    FROM tx t
    LEFT JOIN block_fees b ON t.hour=b.hour
    GROUP BY 1
)

SELECT
    hour,
    block_base_fee/1e9 as "Base Fee (Gwei)",
    --AVG(block_base_fee/1e9) OVER (order by hour Rows Between 5 preceding and current row) as "Base Fee MA (Gwei)",
    avg_priority_fee as "Tip (Gwei)",
    --AVG(avg_priority_fee) OVER (order by hour Rows Between 5 preceding and current row) as "Tip MA(Gwei)",
    priority_total as "Block Tips (ETH)",
    base_total as "Block Base Fees (ETH)",
    legacy_count as "Legacy # TX",
    dynamicFee_count as "Dynamic # TX"
    --avg(priority_total) OVER (order by hour Rows Between 30 preceding and current row) as "Block Tips MA (ETH)",
    --avg(base_total) OVER (order by hour Rows Between 30 preceding and current row) as "Block Base Fees MA (ETH)",
    --avg(legacy_count) OVER (order by hour Rows Between 30 preceding and current row) as "Legacy MA # TX",
    --avg(dynamicFee_count) OVER (order by hour Rows Between 30 preceding and current row) as "Dynamic MA # TX"
FROM hour_fees
ORDER BY hour DESC
