WITH 
monolith_wallets AS (
	SELECT 
		block_time as creation_time,
		block_number as creation_block_number,
		address,
		'Monolith' as wallet_name
	from ethereum.traces 
	where "from" in ('\x95BEBe7bfc6aCc186C13D055D0Aacc2DE5f81502','\xb24d47364163f909e64cf2cf7788d22c51cea851', '\x85bb8a852c29d8f100cb97ecdf4589086d1be2dd') -- Monolith deployers
	    and type = 'create'
),
argent_wallets AS (
    select substring(topic2 from 13 for 20) as "address", eb.time as creation_time, eb.number as creation_block_number, 'Argent' as wallet_name
	from ethereum.logs el
	join ethereum.blocks eb 
		on el.block_number = eb."number"	
	where (topic1 = '\x5b03bfed1c14a02bdeceb5fa582eb1a5765fc0bc64ca0e6af4c20afc9487f081' -- WalletCreated event
		and contract_address = '\x851cc731ce1613ae4fd8ec7f61f4b350f9ce1020' -- Argent Factory
		) OR
		(topic1 = '\xca0b7dde26052d34217ef1a0cee48085a07ca32da0a918609937a307d496bbf5' -- WalletCreated event
		and contract_address = '\x40C84310Ef15B0c0E5c69d25138e0E16e8000fE9' -- Argent Factory
		) 
),
dharma_wallets AS (
	SELECT 
		block_time as creation_time,
		block_number as creation_block_number,
		address,
		'Dharma' as wallet_name
	from ethereum.traces 
	where "from" in ('\xfc00C80b0000007F73004edB00094caD80626d8D') -- DharmaSmartWalletFactoryV1
	and type = 'create'
),
mykey_wallets AS
  (SELECT substring(topic2
                    FROM 13
                    FOR 20) AS "address",
          eb.time AS creation_time,
          eb.number AS creation_block_number, 'MYKEY' as wallet_name
   FROM ethereum.logs el
   JOIN ethereum.blocks eb ON el.block_number = eb."number"
   WHERE topic1 = '\x485303d9c4fea77b8d5b334f4df76df3cd6e2a04a943dc0baa7e69896cd315a1' AND contract_address IN ('\x51Ee24DF42F6d1A36212D72D6199cc08b67f2d69', '\x185479fb2caecba11227db4186046496d6230243') 
),
dapper_wallets AS (
	SELECT 
		block_time as creation_time,
		block_number as creation_block_number,
		address,
		'Dapper' as wallet_name
	from ethereum.traces 
	where "from" in ('\xa78bbf97033e534c54b0a4fa62aa77b652ae4097', '\xab76c6d00c603a7615d5459132c1745eb1fb4f6c') -- Dapper  WalletFactories 
	and type = 'create'
),
wallets AS (
    select address, wallet_name from monolith_wallets union 
    select address, wallet_name from argent_wallets union
    select address, wallet_name from dharma_wallets union
    select address, wallet_name from mykey_wallets union
    select address, wallet_name from dapper_wallets
),
transfers AS (
	    SELECT
	    evt_tx_hash AS tx_hash,
	    tr."from" AS address,
	    -tr.value AS amount,
	    tokens.decimals,
	    tokens.symbol,
	    tokens.contract_address,
	    wallets.address,
	    wallets.wallet_name
	     FROM erc20."ERC20_evt_Transfer" tr
	     join erc20.tokens 
	     	on tr.contract_address = tokens.contract_address
	     join wallets
	        on tr.from = wallets.address
	   where tr.contract_address in 
	   ('\xdac17f958d2ee523a2206206994597c13d831ec7', '\xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', '\x6b175474e89094c44da98b954eedeac495271d0f','\x8e870d67f660d95d5be530380d0ec0bd388289e1', '\x5d3a536e4d6dbd6114cc1ead35777bab948e3643', '\x39aa39c021dfbae8fac545936693ac917d5e7563')  -- USDT, USDC, DAI, PAX, cUSDC, cDAI
	UNION ALL
	    SELECT
	    evt_tx_hash AS tx_hash,
	    tr."to" AS address,
	    tr.value AS amount,
	    tokens.decimals,
	    tokens.symbol,
	    tokens.contract_address,
	    wallets.address,
	    wallets.wallet_name
	     FROM erc20."ERC20_evt_Transfer" tr 
	     join erc20.tokens 
	     	on tr.contract_address = tokens.contract_address
	    join wallets
	        on tr.to = wallets.address
	   where tr.contract_address in 
	   ('\xdac17f958d2ee523a2206206994597c13d831ec7', '\xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', '\x6b175474e89094c44da98b954eedeac495271d0f', '\x8e870d67f660d95d5be530380d0ec0bd388289e1', '\x5d3a536e4d6dbd6114cc1ead35777bab948e3643', '\x39aa39c021dfbae8fac545936693ac917d5e7563')
	   
),
balances as (
	SELECT symbol, contract_address, decimals, wallet_name, sum(amount) as balance
	FROM transfers
	GROUP BY 1,2,3,4
)

select wallet_name, symbol, balance/10^decimals as balance 
from balances 
