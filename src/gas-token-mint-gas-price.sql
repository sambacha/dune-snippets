-- CREATE OR REPLACE FUNCTION _final_median(NUMERIC[])
--   RETURNS NUMERIC AS
-- $$
--   SELECT AVG(val)
--   FROM (
--      SELECT val
--      FROM unnest($1) val
--      ORDER BY 1
--      LIMIT  2 - MOD(array_upper($1, 1), 2)
--      OFFSET CEIL(array_upper($1, 1) / 2.0) - 1
--   ) sub;
-- $$
-- LANGUAGE 'sql' IMMUTABLE;
 
-- CREATE AGGREGATE median(NUMERIC) (
--   SFUNC=array_append,
--   STYPE=NUMERIC[],
--   FINALFUNC=_final_median,
--   INITCOND='{}'
-- );

SELECT
    date_trunc('day', tx.block_time) AS time,
    MIN(tx.gas_price)/1e9 as "min",
    AVG(tx.gas_price)/1e9 as "avg",
    MAX(tx.gas_price)/1e9 as "max",
    MEDIAN(tx.gas_price)/1e9 as "median",
    SUM(gst.value) as "count"
FROM gastoken."GasToken2_call_mint" gst
LEFT JOIN ethereum.transactions tx ON gst.call_tx_hash = tx.hash
WHERE tx.gas_price > 0 AND gst.call_success
  AND tx.block_time > now() - interval '30 days'
GROUP BY 1
ORDER BY 1 DESC
