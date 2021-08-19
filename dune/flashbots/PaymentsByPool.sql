WITH uu_raw1 as
(
SELECT
*
FROM ethereum."traces"
WHERE gas_used = 0
AND "to" = '\xd224ca0c819e8e97ba0136b3b95ceff503b79f53'
AND block_time > '2020-12-18'
),

uu_raw2 as
(
SELECT
uu_raw1.block_time as block_time,
tx_hash,
'UUpool' as name,
CASE
    WHEN tx_index = 0 THEN uu_raw1.value/1e18
    ELSE uu_raw1.value/1e18 + (t.gas_used * 2.2e-7)
END as miner_payment_estimation
FROM uu_raw1
LEFT JOIN ethereum.transactions t ON t.hash = uu_raw1.tx_hash
WHERE t."from" != '\x7d92AD7e1b6Ae22c6a43283aF3856028CD3d856A'
),

sp_raw1 as
(
SELECT
*
FROM ethereum."traces"
WHERE gas_used = 0
AND "to" = '\x04668Ec2f57cC15c381b461B9fEDaB5D451c8F7F'
AND block_time > '2020-12-18'
),

sp_raw2 as
(
SELECT
sp_raw1.block_time as block_time,
tx_hash,
'Spiderpool' as name,
CASE
    WHEN tx_index = 0 THEN sp_raw1.value/1e18
    ELSE sp_raw1.value/1e18 + (t.gas_used * 2.2e-7)
END as miner_payment_estimation
FROM sp_raw1
LEFT JOIN ethereum.transactions t ON t.hash = sp_raw1.tx_hash
),

c8_raw1 as
(
SELECT
*
FROM ethereum."traces"
WHERE gas_used = 0
AND "to" = '\xc8F595E2084DB484f8A80109101D58625223b7C9'
AND block_time > '2020-12-18'
),

c8_raw2 as
(
SELECT
c8_raw1.block_time as block_time,
tx_hash,
'0xc8f...c9' as name,
CASE
    WHEN tx_index = 0 THEN c8_raw1.value/1e18
    ELSE c8_raw1.value/1e18 + (t.gas_used * 2.2e-7)
END as miner_payment_estimation
FROM c8_raw1
LEFT JOIN ethereum.transactions t ON t.hash = c8_raw1.tx_hash
),

flex_raw1 as
(
SELECT
*
FROM ethereum."traces"
WHERE gas_used = 0
AND "to" = '\x7F101fE45e6649A6fB8F3F8B43ed03D353f2B90c'
AND block_time > '2020-12-18'
),

flex_raw2 as
(
SELECT
flex_raw1.block_time as block_time,
tx_hash,
'Flexpool' as name,
CASE
    WHEN tx_index = 0 THEN flex_raw1.value/1e18
    ELSE flex_raw1.value/1e18 + (t.gas_used * 2.2e-7)
END as miner_payment_estimation
FROM flex_raw1
LEFT JOIN ethereum.transactions t ON t.hash = flex_raw1.tx_hash
),

e8_raw1 as
(
SELECT
*
FROM ethereum."traces"
WHERE gas_used = 0
AND "to" = '\x00192Fb10dF37c9FB26829eb2CC623cd1BF599E8'
OR "to" = '\x002e08000acbbaE2155Fab7AC01929564949070d'
AND block_time > '2020-12-18'
),

e8_raw2 as
(
SELECT
e8_raw1.block_time as block_time,
tx_hash,
'2Miners' as name,
CASE
    WHEN tx_index = 0 THEN e8_raw1.value/1e18
    ELSE e8_raw1.value/1e18 + (t.gas_used * 2.2e-7)
END as miner_payment_estimation
FROM e8_raw1
LEFT JOIN ethereum.transactions t ON t.hash = e8_raw1.tx_hash
),

_1a_raw1 as
(
SELECT
*
FROM ethereum."traces"
WHERE gas_used = 0
AND "to" = '\x1aD91ee08f21bE3dE0BA2ba6918E714dA6B45836'
AND block_time > '2020-12-18'
),

_1a_raw2 as
(
SELECT
_1a_raw1.block_time as block_time,
tx_hash,
'HiveOn' as name,
CASE
    WHEN tx_index = 0 THEN _1a_raw1.value/1e18
    ELSE _1a_raw1.value/1e18 + (t.gas_used * 2.2e-7)
END as miner_payment_estimation
FROM _1a_raw1
LEFT JOIN ethereum.transactions t ON t.hash = _1a_raw1.tx_hash
),

_82_raw1 as
(
SELECT
*
FROM ethereum."traces"
WHERE gas_used = 0
AND "to" = '\x829BD824B016326A401d083B33D092293333A830'
AND block_time > '2020-12-18'
),

_82_raw2 as
(
SELECT
_82_raw1.block_time as block_time,
tx_hash,
'F2Pool' as name,
CASE
    WHEN tx_index = 0 THEN _82_raw1.value/1e18
    ELSE _82_raw1.value/1e18 + (t.gas_used * 2.2e-7)
END as miner_payment_estimation
FROM _82_raw1
LEFT JOIN ethereum.transactions t ON t.hash = _82_raw1.tx_hash
),

_99_raw1 as
(
SELECT
*
FROM ethereum."traces"
WHERE gas_used = 0
AND "to" = '\x99C85bb64564D9eF9A99621301f22C9993Cb89E3'
AND block_time > '2020-12-18'
),

_99_raw2 as
(
SELECT
_99_raw1.block_time as block_time,
tx_hash,
'BeePool' as name,
CASE
    WHEN tx_index = 0 THEN _99_raw1.value/1e18
    ELSE _99_raw1.value/1e18 + (t.gas_used * 2.2e-7)
END as miner_payment_estimation
FROM _99_raw1
LEFT JOIN ethereum.transactions t ON t.hash = _99_raw1.tx_hash
),

babel_raw1 as
(
SELECT
*
FROM ethereum."traces"
WHERE gas_used = 0
AND "to" = '\xB3b7874F13387D44a3398D298B075B7A3505D8d4'
AND block_time > '2020-12-18'
),

babel_raw2 as
(
SELECT
babel_raw1.block_time as block_time,
tx_hash,
'Babel Pool' as name,
CASE
    WHEN tx_index = 0 THEN babel_raw1.value/1e18
    ELSE babel_raw1.value/1e18 + (t.gas_used * 2.2e-7)
END as miner_payment_estimation
FROM babel_raw1
LEFT JOIN ethereum.transactions t ON t.hash = babel_raw1.tx_hash
),

spark_raw1 as
(
SELECT
*
FROM ethereum."traces"
WHERE gas_used = 0
AND "to" = '\x5A0b54D5dc17e0AadC383d2db43B0a0D3E029c4c'
AND block_time > '2020-12-18'
),

spark_raw2 as
(
SELECT
spark_raw1.block_time as block_time,
tx_hash,
'Spark Pool' as name,
CASE
    WHEN tx_index = 0 THEN spark_raw1.value/1e18
    ELSE spark_raw1.value/1e18 + (t.gas_used * 2.2e-7)
END as miner_payment_estimation
FROM spark_raw1
LEFT JOIN ethereum.transactions t ON t.hash = spark_raw1.tx_hash
),

events as
(
SELECT * FROM uu_raw2 UNION ALL
SELECT * FROM sp_raw2 UNION ALL
SELECT * FROM c8_raw2 UNION ALL
SELECT * FROM flex_raw2 UNION ALL
SELECT * FROM e8_raw2 UNION ALL
SELECT * FROM _1a_raw2 UNION ALL
SELECT * FROM _82_raw2 UNION ALL
SELECT * FROM _99_raw2 UNION ALL
SELECT * FROM babel_raw2 UNION ALL
SELECT * FROM spark_raw2
)

SELECT
date_trunc('day', block_time) as Date,
name,
sum(miner_payment_estimation) as miner_payment_estimation
FROM events
WHERE block_time > '2021-01-01'
GROUP BY 1, 2
ORDER BY 1 DESC
