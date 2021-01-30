WITH
  mined_block AS (
    SELECT
      miner,
      DATE(timestamp)
    FROM
      `bigquery-public-data.crypto_ethereum_classic.blocks`
    WHERE
      DATE(timestamp) > DATE_SUB(`CURRENT_DATE`(), INTERVAL 1 MONTH)
    ORDER BY miner
  )
SELECT
  miner,
  COUNT(miner) AS total_block_reward
FROM
  mined_block
GROUP BY
  miner
ORDER BY total_block_reward;
