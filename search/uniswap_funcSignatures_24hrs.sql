WITH uniswap_trades AS (
    SELECT tx_hash, usd_amount
    FROM dex."trades" d
    WHERE project = 'Uniswap' AND version ='2'
        AND block_time >= (DATE_TRUNC('hour', CURRENT_TIMESTAMP) - '24 hours'::INTERVAL)
    ), -- transaction hash in UNISWAP v2

    dex_trade_type AS (
        SELECT "to",
        CASE WHEN "to" in ('\x7a250d5630b4cf539739df2c5dacb4c659f2488d','\xf164fc0ec4e93095b804a4795bbe1e041497b92a','\xc9f8878ebba65ab04743f374f57fb652981e222c') then 'Uniswap'
            WHEN "to" in ('\x111111125434b319222cdbf8c261674adb56f3ae','\x1111111254fc78fdddb1ca73c8c15f91342af92e','\x11111112542d85b3ef69ae05771c2dccff4faa26') then '1inch'
            WHEN "to" in ('\xdef1c0ded9bec7f1a1670819833240f027b25eff','\x881d40237659c251811cec9c364ef91dc08d300c') then '0x'
            WHEN "to"='\xf90e98f3d8dce44632e5020abf2e122e0f99dfab' then 'Paraswap'
            WHEN "to"='\xa356867fdcea8e71aeaf87805808803806231fdc' then 'DODO V2'
            WHEN "to"='\x7c40c393dc0f283f318791d746d894ddd3693572' then 'Mooncats'
            WHEN "to" in ('\x7d2768de32b0b80b7a3454c06bdac94a69ddc7a9','\x63a3f444e97d14e671e7ee323c4234c8095e3516','\x498c5431eb517101582988fbb36431ddaac8f4b1') then 'AAVE Flashloan'
            WHEN "to"='\xa013afbb9a92cef49e898c87c060e6660e050569' then 'Furucombo'
            ELSE NULL END AS label,
        SUBSTRING(t.input, 1, 4), -- get first 4 characters in the input
        s.signature, -- identfier?
        COUNT(*), -- count number of tos?
        MIN(block_time) as first_seen,
        MAX(t.tx_hash::text) as example_tx, -- 1 trace contains multiple tx, get max
        SUM(usd_amount) as amt
        FROM ethereum."traces" t
        JOIN uniswap_trades u on u.tx_hash = t.tx_hash -- join uniswap with the same tx hashes in ethereum
        LEFT JOIN ethereum."signatures" s on s.id = substring(t.input,1,4)
        WHERE
             trace_address::text = '{}'
            -- only top level call
            AND t.block_time >= (DATE_TRUNC('hour',CURRENT_TIMESTAMP) - '24 hours'::INTERVAL)
    GROUP BY 1,2,3,4
    HAVING COUNT(*) >= 0
    ORDER BY 5 desc, 8 desc)

    SELECT "to",label,"substring",signature,"count",first_seen,example_tx,"amt"
    FROM dex_trade_type dt
    WHERE dt.label = {{param}}
-- on dune frontend, enter example, 'uniswap trader'



--select * from ethereum."signatures" limit 10

-- look closer into this tx example
-- https://bloxy.info/tx/0xbeca2c54c268e4616b3e44adcfc9df05f88380a561d8b4966343ede9c0add8ae


--select substring(input,1,4) from ethereum."traces" where tx_hash = '\xffe0f7a47b877259b09c4465727c7d0d315020ae48e80845538f2c2fd95471c9'
