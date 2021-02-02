select t.*, b.miner --t.block_time, t.success, t."hash", t."from", t."to", b.miner, t.index, t.gas_used, t.nonce, t.block_number, t.block_hash, t.gas_limit, t.gas_price, t.data
from ethereum.transactions t
join ethereum.blocks b
    on t.block_hash = b.hash
where t.gas_price = 0
    and t.block_time >= '2021-01-01'
