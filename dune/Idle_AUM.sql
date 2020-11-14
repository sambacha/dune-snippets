WITH 
    vars AS (
        SELECT
            '\x4215606a720477178AdFCd5A59775C63138711e8'::bytea AS fee_address,
            '\xdac17f958d2ee523a2206206994597c13d831ec7'::bytea AS usdt_underlying_token, --USDT
            '\xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'::bytea AS usdc_underlying_token, -- USDC
            '\x6b175474e89094c44da98b954eedeac495271d0f'::bytea AS dai_underlying_token, -- DAI
            '\x57ab1ec28d129707052df4df418d58a2d46d5f51'::bytea AS susd_underlying_token, -- SUSD
            '\x0000000000085d4780b73119b644ae5ecd22b376'::bytea AS tusd_underlying_token, -- TUSD
            '\x2260fac5e5542a773aa44fbcfedf7c193bc2c599'::bytea AS wbtc_underlying_token  -- WBTC
    ),
    idle_usdt_risk AS ( -- Change name here
        SELECT
            blocktime,
            idle_token/1e18 as idle_token,
            source_token as source_token,
            fee as fee,
            (SELECT usdt_underlying_token FROM vars) as underlying_token_address, -- Change var here
            success,
            contract_address,
            'IdleV4 USDT Risk Adjusted' as contract_name
        FROM
        (
            SELECT
                mi.call_block_time AS blocktime,
                mi."output_mintedTokens" AS idle_token,
                mi."_amount" AS source_token,
                mi.call_success as success,
                mi.contract_address,
                0 as fee
            FROM idle_v4."IdleUSDT_v4_Risk_call_mintIdleToken" mi -- Change table here
        UNION
            SELECT
                re.call_block_time AS blocktime,
                -re."_amount" AS idle_token,
                -re."output_redeemedTokens" AS source_token,
                re.call_success as success,
                re.contract_address,
                -fee.value as fee
           FROM idle_v4."IdleUSDT_v4_Risk_call_redeemIdleToken" re -- Change table here
           LEFT OUTER JOIN (
                SELECT value, evt_tx_hash, contract_address
                FROM erc20."ERC20_evt_Transfer"
                WHERE "to" IN(SELECT fee_address FROM vars)
                AND contract_address IN (SELECT usdt_underlying_token from vars) ) fee ON fee.evt_tx_hash=re.call_tx_hash -- Change var here
        ) idle_usdt_risk -- Change name here
        WHERE idle_token <> 0),
    idle_usdc_risk AS ( -- Change name here
        SELECT
            blocktime,
            idle_token/1e18 as idle_token,
            source_token as source_token,
            fee as fee,
            (SELECT usdc_underlying_token FROM vars) as underlying_token_address, -- Change var here
            success,
            contract_address,
            'IdleV4 USDC Risk Adjusted' as contract_name
        FROM
        (
            SELECT
                mi.call_block_time AS blocktime,
                mi."output_mintedTokens" AS idle_token,
                mi."_amount" AS source_token,
                mi.call_success as success,
                mi.contract_address,
                0 as fee
            FROM idle_v4."IdleUSDC_v4_Risk_call_mintIdleToken" mi -- Change table here
        UNION
            SELECT
                re.call_block_time AS blocktime,
                -re."_amount" AS idle_token,
                -re."output_redeemedTokens" AS source_token,
                re.call_success as success,
                re.contract_address,
                -fee.value as fee
           FROM idle_v4."IdleUSDC_v4_Risk_call_redeemIdleToken" re -- Change table here
           LEFT OUTER JOIN (
                SELECT value, evt_tx_hash, contract_address
                FROM erc20."ERC20_evt_Transfer"
                WHERE "to" IN(SELECT fee_address FROM vars)
                AND contract_address IN (SELECT usdc_underlying_token from vars) ) fee ON fee.evt_tx_hash=re.call_tx_hash -- Change var here
        ) idle_usdc_risk -- Change name here
        WHERE idle_token <> 0),
    idle_dai_risk AS ( -- Change name here
        SELECT
            blocktime,
            idle_token/1e18 as idle_token,
            source_token as source_token,
            fee as fee,
            (SELECT dai_underlying_token FROM vars) as underlying_token_address, -- Change var here
            success,
            contract_address,
            'IdleV4 DAI Risk Adjusted' as contract_name
        FROM
        (
            SELECT
                mi.call_block_time AS blocktime,
                mi."output_mintedTokens" AS idle_token,
                mi."_amount" AS source_token,
                mi.call_success as success,
                mi.contract_address,
                0 as fee
            FROM idle_v4."IdleDAI_v4_Risk_call_mintIdleToken" mi -- Change table here
        UNION
            SELECT
                re.call_block_time AS blocktime,
                -re."_amount" AS idle_token,
                -re."output_redeemedTokens" AS source_token,
                re.call_success as success,
                re.contract_address,
                -fee.value as fee
           FROM idle_v4."IdleDAI_v4_Risk_call_redeemIdleToken" re -- Change table here
           LEFT OUTER JOIN (
                SELECT value, evt_tx_hash, contract_address
                FROM erc20."ERC20_evt_Transfer"
                WHERE "to" IN(SELECT fee_address FROM vars)
                AND contract_address IN (SELECT dai_underlying_token from vars) ) fee ON fee.evt_tx_hash=re.call_tx_hash -- Change var here
        ) idle_dai_risk -- Change name here
        WHERE idle_token <> 0),
    idle_wbtc_yield AS ( -- Change name here
        SELECT
            blocktime,
            idle_token/1e18 as idle_token,
            source_token as source_token,
            fee as fee,
            (SELECT wbtc_underlying_token FROM vars) as underlying_token_address, -- Change var here
            success,
            contract_address,
            'IdleV4 WBTC Best Yield' as contract_name
        FROM
        (
            SELECT
                mi.call_block_time AS blocktime,
                mi."output_mintedTokens" AS idle_token,
                mi."_amount" AS source_token,
                mi.call_success as success,
                mi.contract_address,
                0 as fee
            FROM idle_v4."IdleWBTC_v4_Yield_call_mintIdleToken" mi -- Change table here
        UNION
            SELECT
                re.call_block_time AS blocktime,
                -re."_amount" AS idle_token,
                -re."output_redeemedTokens" AS source_token,
                re.call_success as success,
                re.contract_address,
                -fee.value as fee
           FROM idle_v4."IdleWBTC_v4_Yield_call_redeemIdleToken" re -- Change table here
           LEFT OUTER JOIN (
                SELECT value, evt_tx_hash, contract_address
                FROM erc20."ERC20_evt_Transfer"
                WHERE "to" IN(SELECT fee_address FROM vars)
                AND contract_address IN (SELECT wbtc_underlying_token from vars) ) fee ON fee.evt_tx_hash=re.call_tx_hash -- Change var here
        ) idle_wbtc_yield -- Change name here
        WHERE idle_token <> 0),
    idle_tusd_yield AS ( -- Change name here
        SELECT
            blocktime,
            idle_token/1e18 as idle_token,
            source_token as source_token,
            fee as fee,
            (SELECT tusd_underlying_token FROM vars) as underlying_token_address, -- Change var here
            success,
            contract_address,
            'IdleV4 TUSD Best Yield' as contract_name
        FROM
        (
            SELECT
                mi.call_block_time AS blocktime,
                mi."output_mintedTokens" AS idle_token,
                mi."_amount" AS source_token,
                mi.call_success as success,
                mi.contract_address,
                0 as fee
            FROM idle_v4."IdleTUSD_v4_Yield_call_mintIdleToken" mi -- Change table here
        UNION
            SELECT
                re.call_block_time AS blocktime,
                -re."_amount" AS idle_token,
                -re."output_redeemedTokens" AS source_token,
                re.call_success as success,
                re.contract_address,
                -fee.value as fee
           FROM idle_v4."IdleTUSD_v4_Yield_call_redeemIdleToken" re -- Change table here
           LEFT OUTER JOIN (
                SELECT value, evt_tx_hash, contract_address
                FROM erc20."ERC20_evt_Transfer"
                WHERE "to" IN(SELECT fee_address FROM vars)
                AND contract_address IN (SELECT tusd_underlying_token from vars) ) fee ON fee.evt_tx_hash=re.call_tx_hash -- Change var here
        ) idle_tusd_yield -- Change name here
        WHERE idle_token <> 0),
    idle_usdt_yield AS ( -- Change name here
        SELECT
            blocktime,
            idle_token/1e18 as idle_token,
            source_token as source_token,
            fee as fee,
            (SELECT usdt_underlying_token FROM vars) as underlying_token_address, -- Change var here
            success,
            contract_address,
            'IdleV4 USDT Best Yield' as contract_name
        FROM
        (
            SELECT
                mi.call_block_time AS blocktime,
                mi."output_mintedTokens" AS idle_token,
                mi."_amount" AS source_token,
                mi.call_success as success,
                mi.contract_address,
                0 as fee
            FROM idle_v4."IdleUSDT_v4_Yield_call_mintIdleToken" mi -- Change table here
        UNION
            SELECT
                re.call_block_time AS blocktime,
                -re."_amount" AS idle_token,
                -re."output_redeemedTokens" AS source_token,
                re.call_success as success,
                re.contract_address,
                -fee.value as fee
           FROM idle_v4."IdleUSDT_v4_Yield_call_redeemIdleToken" re -- Change table here
           LEFT OUTER JOIN (
                SELECT value, evt_tx_hash, contract_address
                FROM erc20."ERC20_evt_Transfer"
                WHERE "to" IN(SELECT fee_address FROM vars)
                AND contract_address IN (SELECT usdt_underlying_token from vars) ) fee ON fee.evt_tx_hash=re.call_tx_hash -- Change var here
        ) idle_usdt_yield -- Change name here
        WHERE idle_token <> 0),
    idle_susd_yield AS ( -- Change name here
        SELECT
            blocktime,
            idle_token/1e18 as idle_token,
            source_token as source_token,
            fee as fee,
            (SELECT susd_underlying_token FROM vars) as underlying_token_address, -- Change var here
            success,
            contract_address,
            'IdleV4 SUSD Best Yield' as contract_name
        FROM
        (
            SELECT
                mi.call_block_time AS blocktime,
                mi."output_mintedTokens" AS idle_token,
                mi."_amount" AS source_token,
                mi.call_success as success,
                mi.contract_address,
                0 as fee
            FROM idle_v4."IdleSUSD_v4_Yield_call_mintIdleToken" mi -- Change table here
        UNION
            SELECT
                re.call_block_time AS blocktime,
                -re."_amount" AS idle_token,
                -re."output_redeemedTokens" AS source_token,
                re.call_success as success,
                re.contract_address,
                -fee.value as fee
           FROM idle_v4."IdleSUSD_v4_Yield_call_redeemIdleToken" re -- Change table here
           LEFT OUTER JOIN (
                SELECT value, evt_tx_hash, contract_address
                FROM erc20."ERC20_evt_Transfer"
                WHERE "to" IN(SELECT fee_address FROM vars)
                AND contract_address IN (SELECT susd_underlying_token from vars) ) fee ON fee.evt_tx_hash=re.call_tx_hash -- Change var here
        ) idle_susd_yield -- Change name here
        WHERE idle_token <> 0),
    idle_usdc_yield AS (
        SELECT
            blocktime,
            idle_token/1e18 as idle_token,
            source_token as source_token,
            fee as fee,
            (SELECT usdc_underlying_token FROM vars) as underlying_token_address,
            success,
            contract_address,
            'IdleV4 USDC Best Yield' as contract_name
        FROM
        (
            SELECT
                mi.call_block_time AS blocktime,
                mi."output_mintedTokens" AS idle_token,
                mi."_amount" AS source_token,
                mi.call_success as success,
                mi.contract_address,
                0 as fee
            FROM idle_v4."IdleUSDC_v4_Yield_call_mintIdleToken" mi
        UNION
            SELECT
                re.call_block_time AS blocktime,
                -re."_amount" AS idle_token,
                -re."output_redeemedTokens" AS source_token,
                re.call_success as success,
                re.contract_address,
                -fee.value as fee
           FROM idle_v4."IdleUSDC_v4_Yield_call_redeemIdleToken" re
           LEFT OUTER JOIN (
                SELECT value, evt_tx_hash
                FROM erc20."ERC20_evt_Transfer"
                WHERE "to" IN(SELECT fee_address FROM vars)
                AND contract_address IN (SELECT usdc_underlying_token from vars) ) fee ON fee.evt_tx_hash=re.call_tx_hash
        ) idle_usdc_yield
        WHERE idle_token <> 0),
    idle_dai_yield AS (
        SELECT
            blocktime,
            idle_token/1e18 as idle_token,
            source_token as source_token,
            fee as fee,
            (SELECT dai_underlying_token FROM vars) as underlying_token_address,
            success,
            contract_address,
            'IdleV4 DAI Best Yield' as contract_name
        FROM
        (
            SELECT
                mi.call_block_time AS blocktime,
                mi."output_mintedTokens" AS idle_token,
                mi."_amount" AS source_token,
                mi.call_success as success,
                mi.contract_address,
                0 as fee
            FROM idle_v4."IdleDAI_v4_Yield_call_mintIdleToken" mi
        UNION
            SELECT
                re.call_block_time AS blocktime,
                -re."_amount" AS idle_token,
                -re."output_redeemedTokens" AS source_token,
                re.call_success as success,
                re.contract_address,
                -fee.value as fee
           FROM idle_v4."IdleDAI_v4_Yield_call_redeemIdleToken" re
           LEFT OUTER JOIN (
                SELECT value, evt_tx_hash
                FROM erc20."ERC20_evt_Transfer"
                WHERE "to" IN(SELECT fee_address FROM vars)
                AND contract_address IN (SELECT dai_underlying_token from vars) ) fee ON fee.evt_tx_hash=re.call_tx_hash
        ) idle_dai_yield
        WHERE idle_token <> 0),
    idle_combined as (
        SELECT * FROM idle_dai_yield
        UNION
        SELECT * FROM idle_usdc_yield
        UNION
        SELECT * FROM idle_usdt_yield
        UNION
        SELECT * FROM idle_tusd_yield
        UNION
        SELECT * FROM idle_susd_yield
        UNION
        SELECT * FROM idle_wbtc_yield
        UNION
        SELECT * FROM idle_dai_risk
        UNION
        SELECT * FROM idle_usdc_risk
        UNION
        SELECT * FROM idle_usdt_risk
    ),
    idle_token_movements as (
        SELECT
            idle_token,
            date_trunc('day', blocktime) as blockday,
            underlying_token_address,
            contract_address,
            contract_name,
            (source_token+fee)/idle_token as token_price_no_decimals
        FROM
            idle_combined
        WHERE success=True
    ),
    idle_token_daily_movement as (
        SELECT
            blockday,
            underlying_token_address,
            contract_address,
            contract_name,
            SUM(idle_token * token_price_no_decimals) as underlying_tokens_movement
        FROM idle_token_movements
        GROUP BY underlying_token_address, contract_address, contract_name, blockday
    ),
    days AS (
        SELECT
            generate_series AS ts
        FROM
            generate_series(
                '08-11-2020',
                (SELECT max(blockday) FROM idle_token_daily_movement),
                '1 day')
    ),
    tokens AS (SELECT contract_name FROM idle_token_daily_movement GROUP BY contract_name),
    idle_usd_movement as (
        SELECT
            blockday,
            contract_name,
            idle_token_daily_movement.contract_address,
            p.price * underlying_tokens_movement / 10^p.decimals as usd_movement
        FROM idle_token_daily_movement 
        LEFT OUTER JOIN prices.usd p ON
            p.minute = blockday
            AND p.contract_address=underlying_token_address
    )

SELECT
    -- *,
    day.ts as blockday,
    day.contract_name,
    SUM(COALESCE(usd_movement, 0)) over (PARTITION BY day.contract_name ORDER BY day.ts) AS aum 
FROM (
    SELECT * FROM days CROSS JOIN tokens
) day
LEFT JOIN idle_usd_movement ON day.ts=idle_usd_movement.blockday AND day.contract_name=idle_usd_movement.contract_name
