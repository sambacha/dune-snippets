SELECT
  t.*,
  b.miner --t.block_time, t.success, t."hash", t."from", t."to", b.miner, t.index, t.gas_used, t.nonce, t.block_number, t.block_hash, t.gas_limit, t.gas_price, t.data
FROM
  ethereum.transactions AS t
  JOIN
  ethereum.blocks AS b
  ON t.block_hash = b.`hash`
WHERE
  t.gas_price = 0 AND t.block_time >= '2021-01-01';
