WITH dex_trades AS(
SELECT tx_hash as tx_hash, date_trunc('day', block_time) AS day, date_trunc('minute', block_time) AS tx_minute
FROM dex."trades" c
where project = '1inch'
and tx_to in ('\x11111112542d85b3ef69ae05771c2dccff4faa26',
        '\x111111125434b319222CdBf8C261674aDB56F3ae'
        , '\x11111254369792b2ca5d084ab5eea397ca8fa48b')
and date_trunc('month', block_time) >= date_trunc('month', now())
)
SELECT day
    , count(*) as swaps
    , count(oi.minute) as swaps_with_price
    , sum(tx.gas_used) as gas_used
    , sum(tx.gas_used * tx.gas_price)/1e18 as eth_used
    , sum(tx.gas_used * tx.gas_price * u.price) /1e18 as usd_used
    , sum(tx.gas_used * tx.gas_price * u.price * 0.9) /1e18 as usd_refund
    , sum(tx.gas_used * tx.gas_price * u.price * 0.9 / oi.price)  /1e18 as oneinch_refund
FROM dex_trades b

INNER JOIN ethereum.transactions tx ON tx.hash = b.tx_hash
INNER JOIN prices.usd u ON u.minute = b.tx_minute and u.contract_address = '\xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'
INNER JOIN prices.usd oi ON oi.minute = b.tx_minute and oi.contract_address = '\x111111111117dc0aa78b770fa6a738034120c302'
group by day
ORDER by day
