WITH prices AS (
    SELECT MINUTE,
           contract_address,
           price
    FROM prices.usd
    where date_trunc('day', MINUTE) > now() - interval '120 days'
      and date_trunc('day', MINUTE) < date_trunc('day', now())
)
SELECT day,
       SUM(usd_volume) OVER (ORDER BY DAY) as cumulative_usd_volume
FROM (
         SELECT date_trunc('day', block_time) AS DAY,
                SUM(CASE
                        WHEN token_a_address = a.contract_address
                            THEN token_a_amount * a.price -- Use token A when there's USD price for it

                        ELSE token_b_amount * b.price -- Else use token b

                    END)                      AS usd_volume
         FROM (
                  SELECT *
                  FROM dex."trades" t
                  WHERE project = 'Sushiswap'
                    and date_trunc('day', block_time) > now() - interval '120 days'
                    and date_trunc('day', block_time) < date_trunc('day', now())
              ) AS trades
                  LEFT JOIN prices a ON date_trunc('minute', block_time) = a.minute
             AND token_a_address = a.contract_address -- Joining with prices on time and token address for token A
                  LEFT JOIN prices b ON date_trunc('minute', block_time) = b.minute
             AND token_b_address = b.contract_address -- Joining with prices on time and token address for token B
         GROUP BY DAY
     ) AS days
;
