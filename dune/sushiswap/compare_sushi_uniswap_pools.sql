-- Pair, Uni, decimals, Sushi
-- ETH/WBTC 0xbb2b8038a1640196fbe3e38816f3e67cba72d940 - 8 - 0xceff51756c56ceffca006cd410b03ffc46dd3a58
-- ETH/USDT 0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852 - 6 - 0x06da0fd433c1a5d7a4faa01111c044910a184553
-- ETH/DAI 0xa478c2975ab1ea89e8196811f51a7b7ade33eb11 - 18 - 0xc3d03e4f041fd4cd388c549ee2a29a9e5075882f
-- ETH/USDC 0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc - 6 - 0x397ff1542f962076d0bfe58ea045ffa2d347aca0
WITH prices AS (                                                                                       
    SELECT  date_trunc('hour', minute) as hour,                                                         
            AVG(price) as price                                                                                
    FROM prices.layer1_usd
    WHERE symbol = 'ETH'
    GROUP BY 1                                                                                      
)

select
    *, eth * 2 * a.price / 1e17 as val
from (
    select
        avg(CASE
            WHEN contract_address in (
                '\x0d4a11d5eeaac28ec3f61d100daf4d40471f1852', '\x06da0fd433c1a5d7a4faa01111c044910a184553'
            ) THEN reserve0
            ELSE reserve1
        END) / 1e1 as eth,
        date_trunc('hour', evt_block_time) as h,
        CASE
            WHEN contract_address = '\xbb2b8038a1640196fbe3e38816f3e67cba72d940' THEN 'eth-wbtc'
            WHEN contract_address = '\x0d4a11d5eeaac28ec3f61d100daf4d40471f1852' THEN 'eth-usdt'
            WHEN contract_address = '\xa478c2975ab1ea89e8196811f51a7b7ade33eb11' THEN 'eth-dai'
            WHEN contract_address = '\xb4e16d0168e52d35cacd2c6185b44281ec28c9dc' THEN 'eth-usdc'
            --Sushi Swap Contracts
            when contract_address = '\xceff51756c56ceffca006cd410b03ffc46dd3a58' THEN 'eth-wbtc'
            when contract_address = '\x06da0fd433c1a5d7a4faa01111c044910a184553' THEN 'eth-usdt'
            when contract_address = '\xc3d03e4f041fd4cd388c549ee2a29a9e5075882f' THEN 'eth-dai'
            when contract_address = '\x397ff1542f962076d0bfe58ea045ffa2d347aca0' THEN 'eth-usdc'
        END as pool,
        protocol
    from (
        select *, 'uni' as protocol from uniswap_v2."Pair_evt_Sync"
        union
        select *, 'sushi' as protocol from sushi."Pair_evt_Sync"
    ) y
    where contract_address in ('\xbb2b8038a1640196fbe3e38816f3e67cba72d940','\x0d4a11d5eeaac28ec3f61d100daf4d40471f1852','\xa478c2975ab1ea89e8196811f51a7b7ade33eb11','\xb4e16d0168e52d35cacd2c6185b44281ec28c9dc','\xceff51756c56ceffca006cd410b03ffc46dd3a58','\x06da0fd433c1a5d7a4faa01111c044910a184553','\xc3d03e4f041fd4cd388c549ee2a29a9e5075882f','\x397ff1542f962076d0bfe58ea045ffa2d347aca0')
    group by contract_address, h, protocol
) x
JOIN prices a
    ON x.h = a.hour
where pool = {{ pools }}
