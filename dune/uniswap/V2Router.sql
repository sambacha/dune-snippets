/*
 * NOTES:
 *
 * If sell_amount=-1, it is a sell order, and
 *   - the fixed sell amount provided is output_amounts[0]
 *   - the minimum buy amount asked is buy_amount
 *
 * If buy_amount=-1, it is a buy order, and
 *   - the fixed buy amount provided is output_amounts[last]
 *   - the maximum sell amount asked is sell_amount
 *
 *
 * Running this query can be slooow.
 *
 * marco.correia@gnosis.pm
 */
SELECT ethereum.transactions.block_number,
       ethereum.transactions.index,
       sell_amount,
       buy_amount,
       path,
       output_amounts,
       extract(epoch from ethereum.transactions.block_time) as block_time,
       address
FROM (
        (SELECT call_block_number,
                -1 AS sell_amount,
                "amountOutMin" AS buy_amount,
                path,
                output_amounts,
                call_tx_hash,
                "to" AS address
         FROM uniswap_v2."Router02_call_swapExactTokensForTokens"
         WHERE call_success=TRUE
           AND call_block_number>={{from_block}}
           AND call_block_number<{{to_block}})
      UNION
        (SELECT call_block_number,
                "amountInMax" AS sell_amount,
                -1 AS buy_amount,
                path,
                output_amounts,
                call_tx_hash,
                "to" AS address
         FROM uniswap_v2."Router02_call_swapTokensForExactTokens"
         WHERE call_success=TRUE
           AND call_block_number>={{from_block}}
           AND call_block_number<{{to_block}})
      UNION
        (SELECT call_block_number,
                ethereum.transactions.value AS sell_amount,
                -1 AS buy_amount,
                path,
                output_amounts,
                call_tx_hash,
                uniswap_v2."Router02_call_swapETHForExactTokens".to AS address
         FROM uniswap_v2."Router02_call_swapETHForExactTokens"
         INNER JOIN ethereum.transactions ON ethereum.transactions.hash = call_tx_hash
         WHERE call_success=TRUE
           AND call_block_number>={{from_block}}
           AND call_block_number<{{to_block}})
      UNION
        (SELECT call_block_number,
                -1 AS sell_amount,
                "amountOutMin" AS buy_amount,
                path,
                output_amounts,
                call_tx_hash,
                "to" AS address
         FROM uniswap_v2."Router02_call_swapExactETHForTokens"
         WHERE call_success=TRUE
           AND call_block_number>={{from_block}}
           AND call_block_number<{{to_block}})
      UNION
        (SELECT call_block_number,
                -1 AS sell_amount,
                "amountOutMin" AS buy_amount,
                path,
                output_amounts,
                call_tx_hash,
                "to" AS address
         FROM uniswap_v2."Router02_call_swapExactTokensForETH"
         WHERE call_success=TRUE
           AND call_block_number>={{from_block}}
           AND call_block_number<{{to_block}})
      UNION
        (SELECT call_block_number,
                "amountInMax" AS sell_amount,
                -1 AS buy_amount,
                path,
                output_amounts,
                call_tx_hash,
                "to" AS address
         FROM uniswap_v2."Router02_call_swapTokensForExactETH"
         WHERE call_success=TRUE
           AND call_block_number>={{from_block}}
           AND call_block_number<{{to_block}})
           ) AS query

INNER JOIN ethereum.transactions ON ethereum.transactions.hash = call_tx_hash
ORDER BY ethereum.transactions.block_number, ethereum.transactions.index ASC;
