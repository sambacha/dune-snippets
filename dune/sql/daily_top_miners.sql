#standardSQL
-- MIT License
-- Copyright (c) 2019 Yaz Khoury, yaz.khoury@gmail.com


SELECT miner, 
    DATE(timestamp) as date,
    COUNT(miner) as total_block_reward
FROM `bigquery-public-data.crypto_ethereum_classic.blocks` 
GROUP BY miner, date
HAVING COUNT(miner) > 100
ORDER BY date, COUNT(miner) ASC
