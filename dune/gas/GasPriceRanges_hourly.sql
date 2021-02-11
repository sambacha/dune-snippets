        SELECT
            (PERCENTILE_CONT(0.1) WITHIN GROUP (ORDER BY gas_price)) / 1e9  AS _10_gas_price_gwei
            ,(PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY gas_price)) / 1e9  AS _25_gas_price_gwei
            ,(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY gas_price)) / 1e9  AS median_gas_price_gwei
            ,(PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY gas_price)) / 1e9  AS _75_gas_price_gwei
            ,(PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY gas_price)) / 1e9  AS _90_gas_price_gwei
        FROM ethereum.transactions
        WHERE
            block_time >= (DATE_TRUNC('minute',CURRENT_TIMESTAMP) - '1 hour'::INTERVAL)
