SELECT profit/1e18 AS profit,
       loss/1e18 AS loss,
       evt_block_time,
       evt_block_number
FROM yearn."StrategyHegicETH_evt_Harvested"
ORDER BY evt_block_time DESC;
