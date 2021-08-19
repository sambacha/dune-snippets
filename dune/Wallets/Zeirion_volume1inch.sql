SELECT
    time,
    volume,
    trades
FROM (
SELECT
    date_trunc('day', tx.block_time) AS time,
    MAX(tx.block_time) AS last_time,
    SUM(
        GREATEST(
            oi."fromAmount" * (
                CASE
                    WHEN oi."fromToken" IN (
                        '\xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee', -- ETH
                        '\xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', -- WETH
                        '\x5e74c9036fb86bd7ecdcb084a0673efc32ea31cb', -- sETH
                        '\x3a3a65aab0dd2a17e3f1947ba16138cd37d08c04', -- aETH
                        '\xc0829421c1d260bd3cb3e0f06cfe2d52db2ce315'  -- BETH
                    ) THEN (
                        SELECT p.price
                        FROM prices."layer1_usd" p
                        WHERE p.symbol = 'ETH'
                        AND p.minute = date_trunc('minute', tx.block_time)
                        LIMIT 1
                    )
                    WHEN oi."fromToken" IN (
                        '\x89d24a6b4ccb1b6faa2625fe562bdd9a23260359', -- SAI
                        '\x6b175474e89094c44da98b954eedeac495271d0f', -- DAI
                        '\x0000000000085d4780B73119b644AE5ecd22b376', -- TUSD
                        '\xdac17f958d2ee523a2206206994597c13d831ec7', -- USDT
                        '\x309627af60f0926daa6041b8279484312f2bf060', -- USDB
                        '\x57ab1e02fee23774580c119740129eac7081e9d3'  -- sUSD
                    ) THEN (1)
                    ELSE
                        (
                            SELECT p.price
                            FROM prices."usd" p
                            WHERE p.contract_address = oi."fromToken"
                            AND p.minute = date_trunc('minute', tx.block_time)
                            LIMIT 1
                        )
                END
            ) / POWER(10, (
                    SELECT decimals FROM (
                        (SELECT decimals FROM erc20.tokens WHERE contract_address = oi."fromToken" LIMIT 1)
                        UNION ALL
                        SELECT '18'
                    ) ttt LIMIT 1
                )),
            oi."toAmount" * (
                CASE
                    WHEN oi."toToken" IN (
                        '\xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee', -- ETH
                        '\xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', -- WETH
                        '\x5e74c9036fb86bd7ecdcb084a0673efc32ea31cb', -- sETH
                        '\x3a3a65aab0dd2a17e3f1947ba16138cd37d08c04', -- aETH
                        '\xc0829421c1d260bd3cb3e0f06cfe2d52db2ce315'  -- BETH
                    ) THEN (
                        SELECT p.price
                        FROM prices."layer1_usd" p
                        WHERE p.symbol = 'ETH'
                        AND p.minute = date_trunc('minute', tx.block_time)
                        LIMIT 1
                    )
                    WHEN oi."toToken" IN (
                        '\x89d24a6b4ccb1b6faa2625fe562bdd9a23260359', -- SAI
                        '\x6b175474e89094c44da98b954eedeac495271d0f', -- DAI
                        '\x0000000000085d4780B73119b644AE5ecd22b376', -- TUSD
                        '\xdac17f958d2ee523a2206206994597c13d831ec7', -- USDT
                        '\x309627af60f0926daa6041b8279484312f2bf060', -- USDB
                        '\x57ab1e02fee23774580c119740129eac7081e9d3'  -- sUSD
                    ) THEN (1)
                    ELSE
                        (
                            SELECT p.price
                            FROM prices."usd" p
                            WHERE p.contract_address = oi."toToken"
                            AND p.minute = date_trunc('minute', tx.block_time)
                            LIMIT 1
                        )
                END
            ) / POWER(10, (
                    SELECT decimals FROM (
                        (SELECT decimals FROM erc20.tokens WHERE contract_address = oi."toToken" LIMIT 1)
                        UNION ALL
                        SELECT '18'
                    ) ttt LIMIT 1
                ))
        )
    ) AS volume,
    count(*) as trades
FROM
(
    SELECT * FROM (
        SELECT '\x'::bytea as referrer, "toToken", "fromToken", "minReturn" as "toAmount", "amount" as "fromAmount", "call_tx_hash" as "tx_hash" FROM onesplit."OneSplit_call_swap" WHERE call_success UNION ALL
        SELECT '\x'::bytea as referrer, "toToken", "fromToken", "minReturn" as "toAmount", "amount" as "fromAmount", "call_tx_hash" as "tx_hash" FROM onesplit."OneSplit_call_goodSwap" WHERE call_success --UNION ALL
    ) z87878
    WHERE "tx_hash" NOT IN (
        SELECT "call_tx_hash" FROM oneinch."exchange_v1_call_aggregate" WHERE call_success UNION ALL
        SELECT "call_tx_hash" FROM oneinch."exchange_v2_call_aggregate" WHERE call_success UNION ALL
        SELECT "call_tx_hash" FROM oneinch."exchange_v3_call_aggregate" WHERE call_success UNION ALL
        SELECT "call_tx_hash" FROM oneinch."exchange_v4_call_aggregate" WHERE call_success UNION ALL
        SELECT "call_tx_hash" FROM oneinch."exchange_v5_call_aggregate" WHERE call_success UNION ALL
        SELECT "call_tx_hash" FROM oneinch."exchange_v6_call_aggregate" WHERE call_success UNION ALL
        SELECT "call_tx_hash" FROM oneinch."exchange_v7_call_swap" WHERE call_success UNION ALL
        SELECT "call_tx_hash" FROM oneinch."OneInchExchange_call_swap" WHERE call_success UNION ALL
        SELECT "call_tx_hash" FROM oneinch_v2."OneInchExchange_call_swap" WHERE call_success -- UNION ALL
    ) UNION ALL

    SELECT referrer, "toToken", "fromToken", "minTokensAmount" as "toAmount", "tokensAmount" as "fromAmount", "call_tx_hash" as "tx_hash" FROM oneinch."exchange_v1_call_aggregate" WHERE call_success UNION ALL
    SELECT referrer, "toToken", "fromToken", "minTokensAmount" as "toAmount", "tokensAmount" as "fromAmount", "call_tx_hash" as "tx_hash" FROM oneinch."exchange_v2_call_aggregate" WHERE call_success UNION ALL
    SELECT referrer, "toToken", "fromToken", "minTokensAmount" as "toAmount", "tokensAmount" as "fromAmount", "call_tx_hash" as "tx_hash" FROM oneinch."exchange_v3_call_aggregate" WHERE call_success UNION ALL
    SELECT referrer, "toToken", "fromToken", "minTokensAmount" as "toAmount", "tokensAmount" as "fromAmount", "call_tx_hash" as "tx_hash" FROM oneinch."exchange_v4_call_aggregate" WHERE call_success UNION ALL
    SELECT referrer, "toToken", "fromToken", "minTokensAmount" as "toAmount", "tokensAmount" as "fromAmount", "call_tx_hash" as "tx_hash" FROM oneinch."exchange_v5_call_aggregate" WHERE call_success UNION ALL
    SELECT referrer, "toToken", "fromToken", "minTokensAmount" as "toAmount", "tokensAmount" as "fromAmount", "call_tx_hash" as "tx_hash" FROM oneinch."exchange_v6_call_aggregate" WHERE call_success UNION ALL
    SELECT referrer, "toToken", "fromToken", "minReturnAmount" as "toAmount", "fromTokenAmount" as "fromAmount", "call_tx_hash" as "tx_hash" FROM oneinch."exchange_v7_call_swap" WHERE call_success UNION ALL
    SELECT referrer, "toToken", "fromToken", "minReturnAmount" as "toAmount", "fromTokenAmount" as "fromAmount", "call_tx_hash" as "tx_hash" FROM oneinch."OneInchExchange_call_swap" WHERE call_success UNION ALL
    SELECT decode(substring("desc"::json->>'referrer', 3), 'hex'), decode(substring("desc"::json->>'dstToken', 3), 'hex'), decode(substring("desc"::json->>'srcToken', 3), 'hex'), "output_returnAmount" as "toAmount", ("desc"::json->>'amount')::numeric as "fromAmount", "call_tx_hash" as "tx_hash" FROM oneinch_v2."OneInchExchange_call_swap" WHERE call_success UNION ALL

    SELECT referral as referrer, "dst" as "toToken", "src" as "fromToken", "result" as "toAmount", "amount" as "fromAmount", "evt_tx_hash" as "tx_hash" FROM mooniswap."MooniSwap_evt_Swapped"
) oi
INNER JOIN ethereum.transactions tx on tx.hash = oi.tx_hash
WHERE referrer = '\xd26d332c71daa06bb24dded5c3c167961e9eb994'
-- AND tx_hash in (SELECT tx_hash FROM dex.trades WHERE project = '0x')
GROUP BY 1
) zzz
ORDER BY 1 DESC

-- SELECT ("desc"::json->>'amount')::numeric, ("desc"::json->>'amount')::numeric + 1 FROM oneinch_v2."OneInchExchange_call_swap" limit 1

