WITH 
monolith_wallets AS (
	SELECT 
		address,
		'Monolith' as wallet_name
	from ethereum.traces 
	where "from" in ('\x95BEBe7bfc6aCc186C13D055D0Aacc2DE5f81502','\xb24d47364163f909e64cf2cf7788d22c51cea851', '\x85bb8a852c29d8f100cb97ecdf4589086d1be2dd') -- Monolith deployers
	    and type = 'create'
),
monolith_data as (
    select date_trunc('day', el.block_time) AS "day", count(distinct el.tx_hash) as transactions, 'Monolith' as wallet_name
    from ethereum.logs el
    join monolith_wallets w
        on w.address = el.contract_address
    where topic1 in (
			'\xd1ba4ac2e2a11b5101f6cb4d978f514a155b421e8ec396d2d9abaf0bb02917ee',  -- Transferred event
			'\xd4f62f23021706247dcffea245d104ae7ddaec7f23acf3d11d7136d5de6a69ad', -- BulkTransfer
			'\xaf022f6b53b11c364e2dfc0aea08eb9416c94f2661451ea82ead8831385617a6' -- ExecutedTransaction
			)
    group by 1
),
argent_wallets AS (
	SELECT address, 'Argent' as wallet_name, et.block_number as creation_block_number
	from ethereum.traces et
	where "from" in ('\x851cc731ce1613ae4fd8ec7f61f4b350f9ce1020','\x40C84310Ef15B0c0E5c69d25138e0E16e8000fE9') -- argent factory
	    and type = 'create'
),
argent_data as (
    select date_trunc('day', el.block_time) AS "day", count(distinct el.tx_hash) as transactions, 'Argent' as wallet_name
    from ethereum.logs el
    join argent_wallets w
        on w.address = el.contract_address and el.block_number <> w.creation_block_number  -- filter out creation tx
    where topic1 = '\x7d2476ab50663f025cff0be85655bcf355f62768615c0c478f3cd5293f807365' -- Invoke event
    group by 1
),
mykey_data as (
    select date_trunc('day', el.block_time) AS "day", count(distinct el.tx_hash) as transactions, 'MYKEY' as wallet_name
    from ethereum.logs el
    WHERE 
      (topic1 = '\x2792c8ad335b8f96afff7b8b99643a5e94063aabbc81eb0a6865417d4fde4fa6'
          AND el.contract_address ='\x52dAb11c6029862eBF1E65A4d5c30641f5FbD957')
      OR (topic1 = '\x3efc190d59645f005a5974aa84aa94401ad997938870e7b2aa74a45138ad679b'
          AND el.contract_address in('\x1C2349ACBb7f83d07577692c75B6D7654899BF10', '\xF391FFd0e92F80293E4b7a8e7a69CA797224dA6b'))
      OR (topic1 = '\x9bb189d41c9c6ff433f6726f149aed82fe9ae766771663b5eea49ffb71037d17'
          AND el.contract_address ='\x039aA54fEbe98AaaDb91aE2b1Db7aA00a82F8571')
      OR (topic1 = '\x79fe4c2a6e16a232d5cec08cce7e3fd31c0535038f359907c16fbf8ca69e7e9b'
          AND el.contract_address in('\xa385A32566CBFBc83221D90c6A1670ED8196f9D3', '\x2cd784297B10a53003092d6110c83C4092B2fbd2','\x847f5AbbA6A36c727eCfF76784eE3648BA868808'))
    group by 1
),
data AS (
    select day, wallet_name,transactions from monolith_data union 
    select day, wallet_name,transactions from argent_data union
    select day, wallet_name,transactions from mykey_data 
)


select day,wallet_name, transactions
from data
where day > now() - interval '30 days'
order by 1 desc
