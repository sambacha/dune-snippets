WITH s as (SELECT e."to" as sushier, contract_address, -value AS amount
    FROM erc20."ERC20_evt_Transfer" e
    WHERE e."from" = '\xc2EdaD668740f1aA35E4D8f227fB8E17dcA888Cd'
UNION ALL
    SELECT t."from" as sushier, contract_address, value AS amount
    FROM erc20."ERC20_evt_Transfer"  t
    WHERE t."to" ='\xc2EdaD668740f1aA35E4D8f227fB8E17dcA888Cd')
    
    -- p as 
    -- (SELECT (amount1Out/amount0In +amount1In/amount0Out)/2 as price
    -- FROM uniswap_v2."Pair_evt_Swap"
    -- )
select 
sushier,
contract_address,
SUM(amount)/1e18 as lp_balance
FROM s
WHERE sushier != '\x0000000000000000000000000000000000000000'
AND contract_address != '\x6b3595068778dd592e39a122f4f5a5cf09c90fe2'
GROUP by 1,2
ORDER BY lp_balance DESC
