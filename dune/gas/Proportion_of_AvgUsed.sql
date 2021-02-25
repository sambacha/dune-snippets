SELECT date_trunc('week', time) as day,
       AVG(gas_used * 100 / gas_limit) as avg_block_filled
  FROM ethereum."blocks"
 WHERE time > DATE('2020-01-01')
 GROUP BY 1
 ORDER BY 1 DESC
