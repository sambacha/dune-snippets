WITH etc_transactions_book AS (
  SELECT TIMESTAMP_TRUNC(timestamp, DAY) AS etc_block_day,
         SUM(transaction_count) AS etc_total_daily_transaction_count
  FROM `bigquery-public-data.crypto_ethereum_classic.blocks`
  GROUP BY TIMESTAMP_TRUNC(timestamp, DAY)
),
eth_transactions_book AS (
  SELECT TIMESTAMP_TRUNC(timestamp, DAY) AS eth_block_day,
         SUM(transaction_count) AS eth_total_daily_transaction_count
  FROM `bigquery-public-data.crypto_ethereum.blocks`
  GROUP BY TIMESTAMP_TRUNC(timestamp, DAY)
),
btc_transactions_book AS (
  SELECT TIMESTAMP_TRUNC(timestamp, DAY) AS btc_block_day,
         SUM(transaction_count) AS btc_total_daily_transaction_count
  FROM `bigquery-public-data.crypto_bitcoin.blocks`
  GROUP BY TIMESTAMP_TRUNC(timestamp, DAY)
),
bch_transactions_book AS (
  SELECT TIMESTAMP_TRUNC(timestamp, DAY) AS bch_block_day,
         SUM(transaction_count) AS bch_total_daily_transaction_count
  FROM `bigquery-public-data.crypto_bitcoin_cash.blocks`
  GROUP BY TIMESTAMP_TRUNC(timestamp, DAY)
),
ltc_transactions_book AS (
  SELECT TIMESTAMP_TRUNC(timestamp, DAY) AS ltc_block_day,
         SUM(transaction_count) AS ltc_total_daily_transaction_count
  FROM `bigquery-public-data.crypto_litecoin.blocks`
  GROUP BY TIMESTAMP_TRUNC(timestamp, DAY)
),
dash_transactions_book AS (
  SELECT TIMESTAMP_TRUNC(timestamp, DAY) AS dash_block_day,
         SUM(transaction_count) AS dash_total_daily_transaction_count
  FROM `bigquery-public-data.crypto_dash.blocks`
  GROUP BY TIMESTAMP_TRUNC(timestamp, DAY)
),
zcash_transactions_book AS (
  SELECT TIMESTAMP_TRUNC(timestamp, DAY) AS zcash_block_day,
         SUM(transaction_count) AS zcash_total_daily_transaction_count
  FROM `bigquery-public-data.crypto_zcash.blocks`
  GROUP BY TIMESTAMP_TRUNC(timestamp, DAY)
),
total_transactions_book AS (
  SELECT *
  FROM etc_transactions_book etc
  LEFT JOIN eth_transactions_book eth ON etc.etc_block_day = eth.eth_block_day
  LEFT JOIN btc_transactions_book btc ON btc.btc_block_day = etc.etc_block_day
  LEFT JOIN bch_transactions_book bch ON bch.bch_block_day = etc.etc_block_day
  LEFT JOIN ltc_transactions_book ltc ON ltc.ltc_block_day = etc.etc_block_day
  LEFT JOIN dash_transactions_book dash ON dash.dash_block_day = etc.etc_block_day
  LEFT JOIN zcash_transactions_book zcash ON zcash.zcash_block_day = etc.etc_block_day
)
SELECT btc_block_day AS day,
       btc_total_daily_transaction_count AS BTC,
       eth_total_daily_transaction_count AS ETH,
       etc_total_daily_transaction_count AS ETC,
       zcash_total_daily_transaction_count +
       dash_total_daily_transaction_count +
       bch_total_daily_transaction_count +
       ltc_total_daily_transaction_count AS ZDBL_INDEX
FROM total_transactions_book 
WHERE DATE(btc_block_day) > DATE_SUB(CURRENT_DATE(), INTERVAL 2 MONTH)
ORDER BY btc_block_day 
