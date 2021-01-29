SELECT 
  (labels.get(contract))[2]  as name,
  '0x' || RIGHT(c.contract::VARCHAR,-2) as contract_address,
  c.n_transfers as n_transfers
FROM (SELECT 
  contract_address as contract,
  count(*) as n_transfers
FROM erc721."ERC721_evt_Transfer" AS tx
WHERE evt_block_time >= (DATE_TRUNC('month',CURRENT_TIMESTAMP) - '24 months'::INTERVAL)
GROUP BY contract_address
ORDER BY n_transfers DESC
) as c
WHERE c.n_transfers >= 10
