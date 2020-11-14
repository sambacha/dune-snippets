WITH block_rows AS (
  SELECT *, ROW_NUMBER() OVER (ORDER BY timestamp) AS rn
  FROM `bigquery-public-data.crypto_ethereum_classic.blocks`
)
SELECT mp.timestamp AS block_time, 
TIMESTAMP_DIFF(mp.timestamp, mc.timestamp, SECOND) AS time_elapsed,
((mp.difficulty + mc.difficulty) / 2) AS average_difficulty,
((mp.difficulty + mc.difficulty) / 2) / TIMESTAMP_DIFF(mp.timestamp, mc.timestamp, SECOND) AS hashrate
FROM block_rows mc
JOIN block_rows mp
ON  mc.rn = mp.rn - 1
ORDER BY block_time ASC
