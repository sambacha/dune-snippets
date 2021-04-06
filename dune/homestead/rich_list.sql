#standardSQL
--MIT License-- Copyright (c) 2018 Evgeny Medvedev,
    evge.medvedev @gmail.com WITH double_entry_book
    AS (--debits SELECT to_address AS address,
        value AS value FROM
      `bigquery - public
            - data.crypto_ethereum_classic.traces` WHERE to_address IS NOT null
                  AND status
        = 1 AND (call_type NOT IN ('delegatecall', 'callcode', 'staticcall')
                     OR call_type IS null)
            UNION ALL-- credits SELECT from_address AS address,
        -value AS value FROM
      `bigquery - public
            - data.crypto_ethereum_classic.traces` WHERE from_address IS NOT
                  null AND status
        = 1 AND (call_type NOT IN ('delegatecall', 'callcode', 'staticcall')
                     OR call_type IS null)
            UNION ALL-- transaction fees debits SELECT miner AS address,
        sum (CAST (receipt_gas_used AS numeric) * CAST (gas_price AS numeric))
                AS value FROM
      `bigquery
            - public
            - data.crypto_ethereum_classic.transactions` AS transactions JOIN
      `bigquery - public
            - data.crypto_ethereum_classic.blocks` AS blocks ON blocks.number
        = transactions.block_number GROUP BY blocks.miner UNION
              ALL-- transaction fees credits SELECT from_address AS address,
        -(CAST (receipt_gas_used AS numeric) * CAST (gas_price AS numeric))
                AS value FROM
      `bigquery
            - public
            - data.crypto_ethereum_classic.transactions` ) SELECT address,
    sum (value)
        / 1000000000 AS balance FROM
        double_entry_book GROUP BY address ORDER BY balance DESC LIMIT 20;
