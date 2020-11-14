WITH block_rows AS (
  SELECT *, ROW_NUMBER() OVER (ORDER BY timestamp) AS rn
  FROM `bigquery-public-data.ethereum_crypto_ethereum_classic.blocks`
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
SELECT TIMESTAMP_TRUNC(block_time, HOUR) as block_hour,
AVG(hashrate) as hashrate
FROM time_and_hash
GROUP BY TIMESTAMP_TRUNC(block_time, HOUR)
