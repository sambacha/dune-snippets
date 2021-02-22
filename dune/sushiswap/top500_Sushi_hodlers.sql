select 
TEXT(CONCAT('0x',SUBSTRING(TEXT(address),3))) as holder_address,
sushi_balance from (SELECT address, SUM(amount)/1e18 as sushi_balance
FROM (
    SELECT "from" AS address, -value AS amount
    FROM erc20."ERC20_evt_Transfer" 
    WHERE contract_address='\x6b3595068778dd592e39a122f4f5a5cf09c90fe2'
UNION ALL
    SELECT "to" AS address, value AS amount
    FROM erc20."ERC20_evt_Transfer"  
    WHERE contract_address='\x6b3595068778dd592e39a122f4f5a5cf09c90fe2'
) t
WHERE address not in (
'\xf73B31c07e3f8Ea8f7c59Ac58ED1F878708c8A76',
'\xf942dba4159cb61f8ad88ca4a83f5204e8f4a6bd',
'\xce84867c3c02b05dc570d0135103d3fb9cc19433',
'\x3f5ce5fbfe3e9af3971dd833d26ba9b5c936f0be',
'\xe93381fb4c4f14bda253907b18fad305d799241a',
'\xc2edad668740f1aa35e4d8f227fb8e17dca888cd',
'\x6cc5f688a315f3dc28a7781717a9a798a59fda7b',
'\x1c4b70a3968436b9a0a9cf5205c787eb81bb558c',
'\x4938960c507a4d7094c53a8cddcf925835393b8f',
'\x0d0707963952f2fba59dd06f2b425ace40b492fe',
'\xc8d02f2669ef9aabe6b3b75e2813695aed63748d',
'\x0211f3cedbef3143223d3acf0e589747933e8527',
'\x2faf487a4414fe77e2327f0bf4ae2a264a776ad2',
'\xd2e8827d4b1c44f64d1fa01bfbc14dc8545eca41')

GROUP BY 1
ORDER BY sushi_balance DESC
LIMIT 500) x
