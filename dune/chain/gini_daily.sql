WITH
  double_entry_book AS (
    -- debits
    SELECT
      to_address AS address,
      value AS value,
      block_timestamp
    FROM
      `bigquery-public-data.crypto_ethereum_classic.traces`
    WHERE
      to_address IS NOT null AND status = 1 AND (call_type NOT IN ('delegatecall', 'callcode', 'staticcall') OR
      call_type IS null)
    UNION ALL -- credits
    SELECT
      from_address AS address,
      - value AS value,
      block_timestamp
    FROM
      `bigquery-public-data.crypto_ethereum_classic.traces`
    WHERE
      from_address IS NOT null AND status = 1 AND (call_type NOT IN ('delegatecall', 'callcode', 'staticcall') OR
      call_type IS null)
    UNION ALL -- transaction fees debits
    SELECT
      miner AS address,
      sum(CAST(receipt_gas_used AS numeric) * CAST(gas_price AS numeric)) AS value,
      block_timestamp
    FROM
      `bigquery-public-data.crypto_ethereum_classic.transactions` AS transactions
      JOIN
      `bigquery-public-data.crypto_ethereum_classic.blocks` AS blocks
      ON blocks.number = transactions.block_number
    GROUP BY
      blocks.miner,
      block_timestamp
    UNION ALL -- transaction fees credits
    SELECT
      from_address AS address,
      - (CAST(receipt_gas_used AS numeric) * CAST(gas_price AS numeric)) AS value,
      block_timestamp
    FROM
      `bigquery-public-data.crypto_ethereum_classic.transactions`
  ),
  double_entry_book_by_date AS (
    SELECT
      date(block_timestamp) AS date,
      address,
      sum(value / POWER(10, 0)) AS value
    FROM
      double_entry_book
    GROUP BY
      address,
      date
  ),
  daily_balances_with_gaps AS (
    SELECT
      address,
      date,
      sum(value) OVER (PARTITION BY address
        ORDER BY date) AS balance,
      lead(date, 1, `current_date`()) OVER (PARTITION BY address
        ORDER BY date) AS next_date
    FROM
      double_entry_book_by_date
  ),
  calendar AS (
    SELECT
      date
    FROM
      UNNEST(generate_date_array('2015-07-30', `current_date`())) AS date
  ),
  daily_balances AS (
    SELECT
      address,
      calendar.date,
      balance
    FROM
      daily_balances_with_gaps
      JOIN
      calendar
      ON daily_balances_with_gaps.date <= calendar.date AND calendar.date < daily_balances_with_gaps.next_date
  ),
  supply AS (
    SELECT
      date,
      sum(balance) AS daily_supply
    FROM
      daily_balances
    GROUP BY
      date
  ),
  ranked_daily_balances AS (
    SELECT
      daily_balances.date,
      balance,
      row_number() OVER (PARTITION BY daily_balances.date
        ORDER BY balance DESC) AS rank
    FROM
      daily_balances
      JOIN
      supply
      ON daily_balances.date = supply.date
    WHERE
      safe_divide(balance, daily_supply) >= 0.0001
    ORDER BY safe_divide(balance, daily_supply) DESC
  ),
  gini_daily AS (
    SELECT
      date,
      -- (1 − 2B) https://en.wikipedia.org/wiki/Gini_coefficient
      1 - 2 * sum((balance * (rank - 1) + balance / 2)) / count(*) / sum(balance) AS gini
    FROM
      ranked_daily_balances
    GROUP BY
      date
  )
SELECT
  date,
  gini,
  avg(gini) OVER (
    ORDER BY date ROWS 7 PRECEDING) AS gini_sma7,
  avg(gini) OVER (
    ORDER BY date ROWS 30 PRECEDING) AS gini_sma30
FROM
  gini_daily
ORDER BY date;
