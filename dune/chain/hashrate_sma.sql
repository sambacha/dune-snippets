WITH block_rows AS (
  SELECT *, ROW_NUMBER() OVER (ORDER BY timestamp) AS rn
  FROM `bigquery-public-data.crypto_ethereum_classic.blocks`
),
time_and_hash AS (
  SELECT
  mp.timestamp AS block_time,
  TIMESTAMP_DIFF(mp.timestamp, mc.timestamp, SECOND) AS delta_block_time,
  ((mp.difficulty + mc.difficulty) / 2) AS average_difficulty,
  ((mp.difficulty + mc.difficulty) / 2) / TIMESTAMP_DIFF(mp.timestamp, mc.timestamp, SECOND) AS hashrate,
  1 / TIMESTAMP_DIFF(mp.timestamp, mc.timestamp, SECOND) AS block_frequency
  FROM block_rows mc
  JOIN block_rows mp
  ON mc.rn = mp.rn - 1
)
SELECT block_time, 
AVG(hashrate) OVER (ORDER BY block_time ASC ROWS 100 PRECEDING) AS sma_hashrate_100_blocks,
AVG(block_frequency) OVER (ORDER BY block_time ASC ROWS 100 PRECEDING) AS sma_frequency_100_blocks
FROM time_and_hash
ORDER BY block_time ASC
