WITH d AS
  (SELECT date_trunc('days', alink.evt_block_time) AS "time",
          sum(alink.value) / 1e18 AS deposited
   FROM erc20."ERC20_evt_Transfer" yalink
   LEFT JOIN erc20."ERC20_evt_Transfer" alink ON yalink.evt_tx_hash = alink.evt_tx_hash
   WHERE yalink.contract_address = '\x29E240CFD7946BA20895a7a02eDb25C210f9f324'
     AND alink.contract_address = '\xA64BD6C70Cb9051F6A9ba1F163Fdc07E0DfB5F84'
     AND yalink."from" = '\x0000000000000000000000000000000000000000'
     AND yalink."to" = alink."from"
   GROUP BY "time"),
     w AS
  (SELECT date_trunc('days', s.evt_block_time) AS "time",
          sum(alink.value) / 1e18 AS alink
   FROM erc20."ERC20_evt_Transfer" s
   LEFT JOIN erc20."ERC20_evt_Transfer" alink ON s.evt_tx_hash = alink.evt_tx_hash
   WHERE s.contract_address = '\x29E240CFD7946BA20895a7a02eDb25C210f9f324'
     AND alink.contract_address = '\xA64BD6C70Cb9051F6A9ba1F163Fdc07E0DfB5F84'
     AND s."to" = '\x0000000000000000000000000000000000000000'
     AND s."from" = alink."to"
   GROUP BY "time"),
     pretty AS
  (SELECT *,
          'withdrawal' AS OPERATION
   FROM w
   UNION ALL SELECT *,
                    'deposit' AS OPERATION
   FROM d)
SELECT "time",
       OPERATION,
       sum(alink) OVER (PARTITION BY OPERATION
                        ORDER BY "time" ASC) AS alink
FROM pretty ;

