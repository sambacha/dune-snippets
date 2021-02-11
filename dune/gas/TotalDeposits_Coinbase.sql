SELECT address, time, sum(amount/ 1e18) over(order by time)
FROM (

    -- outbound transfers
    SELECT "from" AS address, -tr.value AS amount , date_trunc('day', block_time) as time
    FROM ethereum.traces tr
    WHERE "from" = '\x713E11c146911B2cBa7df18b89BFfaa64F2c9D24'
    AND success
    AND (call_type NOT IN ('delegatecall', 'callcode', 'staticcall') OR call_type IS null)
    AND block_time > '2021-01-04'AND block_time < '2021-02-07'


    UNION ALL

    -- inbound transfers
    SELECT "to" AS address, value AS amount ,date_trunc('day', block_time) as time 
    FROM ethereum.traces
    WHERE "to" = '\x713E11c146911B2cBa7df18b89BFfaa64F2c9D24'
    AND success
    AND (call_type NOT IN ('delegatecall', 'callcode', 'staticcall') OR call_type IS null)
    AND block_time > '2021-01-04' AND block_time < '2021-02-07'

    UNION ALL
    
    -- gas costs
    SELECT "from" AS address, -gas_used * gas_price AS amount, date_trunc('day', block_time) as time
    FROM ethereum.transactions
    WHERE "from" = '\x713E11c146911B2cBa7df18b89BFfaa64F2c9D24'
    AND block_time > '2021-01-04'AND block_time < '2021-02-07'
    
) as t
