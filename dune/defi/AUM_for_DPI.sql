WITH transfers AS (
    
    SELECT  day,
            address, 
            token_address, 
            sum(amount) AS amount -- Net inflow or outflow per day
    FROM
    
    (
        SELECT  date_trunc('day', evt_block_time) AS day,
                "to" AS address,
                tr.contract_address AS token_address,
                value AS amount
        FROM erc20."ERC20_evt_Transfer" tr
        WHERE "to" IN (SELECT asset_pool_address from index.view_indices where "status" = 'ready') --asset holding pools with filter for pools that don't have productive assets

        UNION ALL
        
        SELECT  date_trunc('day', evt_block_time) AS day,
                "from" AS address,
                tr.contract_address AS token_address,
                -value AS amount
        FROM erc20."ERC20_evt_Transfer" tr
        WHERE "from" IN (SELECT asset_pool_address from index.view_indices where "status" = 'ready') --asset holding pools with filter for pools that don't have productive assets
    ) t
   GROUP BY 1, 2, 3
   )

, balances_with_gap_days AS (
    SELECT  t.day,
            address,
            t.token_address,
            SUM(amount) OVER (PARTITION BY token_address, address ORDER BY t.day) AS balance, -- balance per day with a transfer
            lead(day, 1, now()) OVER (PARTITION BY token_address, address ORDER BY t.day) AS next_day -- the day after a day with a transfer
    FROM transfers t
    )
    
 , days AS (
    SELECT generate_series('2020-09-01'::timestamp, date_trunc('day', NOW()), '1 day') AS day -- Generate all days since the first contract
    )
    
 , balance_all_days AS (
    SELECT  d.day,
            address,
            erc.symbol,
            b.token_address,
            SUM(balance/10^decimals) AS balance
    FROM balances_with_gap_days b
    INNER JOIN days d ON b.day <= d.day AND d.day < b.next_day -- Yields an observation for every day after the first transfer until the next day with transfer
    INNER JOIN erc20.tokens erc ON b.token_address = erc.contract_address
    GROUP BY 1, 2, 3, 4
    ORDER BY 1, 2, 3, 4
)

, raw_data as (
SELECT  b.day,
        address as index,
        i.project,
        i.symbol as indexsymbol,
        b.symbol as tokensymbol,
        b.token_address,
        SUM(balance) AS token_balance,
        SUM(balance*p.price) AS balance_usd_value
FROM balance_all_days b
LEFT JOIN  ( 
                 SELECT  date_trunc('day', minute) AS day,
                            contract_address, 
                            AVG(price) AS price
                    FROM prices.usd
                    GROUP BY 1, 2

                    union all

                    select  date_trunc('day', hour) AS day,
                            contract_address, 
                            (PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY median_price)) AS price
                    FROM dex.view_token_prices
                    GROUP BY 1, 2
            ) p ON b.day = p.day AND b.token_address = p.contract_address
LEFT JOIN dune_user_generated.view_indices i on b.address = i.asset_pool_address
            where b.day < now() -interval '1 day'
            
GROUP BY 1,2,3,4,5,6
ORDER BY 1,2,3,4,5,6
)

SELECT 
day,
tokensymbol,
sum(balance_usd_value)

FROM raw_data
where indexsymbol = 'DPI'
and tokensymbol = 'YFI' 
or tokensymbol = 'MKR'
or tokensymbol = 'SNX'
or tokensymbol = 'REPv2'
or tokensymbol = 'REN'
or tokensymbol = 'LRC'
or tokensymbol = 'LEND'
or tokensymbol = 'KNC'
or tokensymbol = 'COMP'
or tokensymbol = 'BAL'
or tokensymbol = 'AAVE'
or tokensymbol = 'MTA'

group by 1,2
