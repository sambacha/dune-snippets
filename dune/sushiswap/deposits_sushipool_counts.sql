SELECT 
CASE 
when pid= 0 THEN 'USDT-WETH'
when pid= 1 THEN 'USDC-WETH'
when pid = 2 THEN 'DAI-WETH'
when pid= 3 THEN 'SUSD-WETH'
when pid = 4 THEN 'COMP-WETH'
when pid = 5 THEN 'LEND-WETH'
when pid = 6 THEN 'SNX-WETH'
when pid= 7 THEN 'UMA-WETH'
when pid= 8 THEN 'LINK-WETH'
when pid= 9 THEN 'BAND-WETH'
when pid= 10 THEN 'AMPL-WETH'
when pid= 11 THEN 'YFI-WETH'
when pid = 12 THEN 'SUSHI-WETH'

when pid = 13 THEN 'REN-WETH'
when pid = 14 THEN 'BASED-WETH'

when pid = 15 THEN 'SRM-WETH'
when pid = 16 THEN 'YAMv2-WETH'

when pid = 17 THEN 'CRV-WETH'
END
as pool,
count(evt_tx_hash),
date_trunc('day', evt_block_time) as day

FROM sushi."MasterChef_evt_Deposit"
group by pid, day
ORDER by count desc
-- LIMIT 5
