(
                    SELECT date_trunc('day', minute) AS day, contract_address AS token, AVG(price) AS price
                    FROM prices.usd
                    GROUP BY 1, 2

                    union all

                    select date_trunc('day', hour) AS day, contract_address AS token, AVG(median_price) AS price
                    FROM dex.view_token_prices
                    GROUP BY 1, 2
    ) as prices on b.day = prices.day
