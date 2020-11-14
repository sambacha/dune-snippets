WITH block_rows AS (
  SELECT *, ROW_NUMBER() OVER (ORDER BY timestamp) AS rn
  FROM `bigquery-public-data.crypto_ethereum_classic.blocks`
),
delta_time AS (
  SELECT
  mp.timestamp AS block_time,
  mp.difficulty AS difficulty,
  TIMESTAMP_DIFF(mp.timestamp, mc.timestamp, SECOND) AS delta_block_time
  FROM block_rows mc
  JOIN block_rows mp
  ON mc.rn = mp.rn - 1
),
hashrate_book AS (
  SELECT TIMESTAMP_TRUNC(block_time, DAY) AS block_day,
  AVG(delta_block_time) as daily_avg_block_time,
  AVG(difficulty) as daily_avg_difficulty
  FROM delta_time
  GROUP BY TIMESTAMP_TRUNC(block_time, DAY)
)
SELECT block_day,
(daily_avg_difficulty/daily_avg_block_time)/1000000000 as hashrate
FROM hashrate_book
ORDER BY block_day ASC
