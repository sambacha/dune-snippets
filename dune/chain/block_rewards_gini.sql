#standardSQL
-- MIT License
-- Copyright (c) 2019 Yaz Khoury, yaz.khoury@gmail.com


WITH total_reward_book AS (
  SELECT miner, 
    DATE(timestamp) as date,
    COUNT(miner) as total_block_reward
  FROM `bigquery-public-data.crypto_ethereum_classic.blocks` 
  GROUP BY miner, date
),
total_reward_book_by_date AS (
 SELECT date, 
        miner AS address, 
        SUM(total_block_reward / POWER(10,0)) AS value
  FROM total_reward_book
  GROUP BY miner, date
),
daily_rewards_with_gaps AS (
  SELECT
    address, 
    date,
    SUM(value) OVER (PARTITION BY ADDRESS ORDER BY date) AS block_rewards,
    LEAD(date, 1, CURRENT_DATE()) OVER (PARTITION BY ADDRESS ORDER BY date) AS next_date
  FROM total_reward_book_by_date
),
calendar AS (
  SELECT date 
  FROM UNNEST(GENERATE_DATE_ARRAY('2015-07-30', CURRENT_DATE())) AS date
),
daily_rewards AS (
  SELECT address, 
    calendar.date, 
    block_rewards
  FROM daily_rewards_with_gaps
  JOIN calendar ON daily_rewards_with_gaps.date <= calendar.date 
  AND calendar.date < daily_rewards_with_gaps.next_date
),
supply AS (
  SELECT date,
    SUM(block_rewards) AS total_rewards
  FROM daily_rewards
  GROUP BY date
),
ranked_daily_rewards AS (
  SELECT daily_rewards.date AS date,
    block_rewards,
    ROW_NUMBER() OVER (PARTITION BY daily_rewards.date ORDER BY block_rewards DESC) AS rank
  FROM daily_rewards
  JOIN supply ON daily_rewards.date = supply.date
  WHERE SAFE_DIVIDE(block_rewards, total_rewards) >= 0.01
  ORDER BY block_rewards DESC
),
daily_gini AS (
  SELECT date,
    -- (1 − 2B) https://en.wikipedia.org/wiki/Gini_coefficient
    1 - 2 * SUM((block_rewards * (rank - 1) + block_rewards / 2)) / COUNT(*) / SUM(block_rewards) AS gini
  FROM ranked_daily_rewards
  GROUP BY DATE
)
SELECT date,
  gini,
  AVG(gini) OVER (ORDER BY date ASC ROWS 7 PRECEDING) AS gini_sma_7,
  AVG(gini) OVER (ORDER BY date ASC ROWS 30 PRECEDING) AS gini_sma_30
FROM daily_gini
