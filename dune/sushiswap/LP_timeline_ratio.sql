/*
 SELECT d.pid, d.sum as deposit, w.sum as withdraw, d.sum - w.sum as liquidity FROM
 ( select pid, 0 as "type", sum(amount) / 1e18 as sum , count(*) as count from sushi."MasterChef_evt_Deposit" group by pid order by pid) as d
 LEFT JOIN
 (select pid, 1 as "type", sum(amount) / 1e18 as sum, count(*) as count  from sushi."MasterChef_evt_Withdraw" group by pid order by pid) as w
 ON d.pid = w.pid

*/
DROP TABLE IF EXISTS lp_names;

CREATE TEMP TABLE lp_names(
    pid INT,
    name char(20),
    pair1 char(10),
    pair2 char(10)
);
INSERT INTO lp_names(pid, name) values(0, '0:WETH/USDT');
INSERT INTO lp_names(pid, name) values(1, '1:ETH/USDC');
INSERT INTO lp_names(pid, name) values(2, '2:DAI/WETH');
INSERT INTO lp_names(pid, name) values(3, '3:Synth/WETH');
INSERT INTO lp_names(pid, name) values(4, '4:COMP/WETH');
INSERT INTO lp_names(pid, name) values(5, '5:LEND/WETH');
INSERT INTO lp_names(pid, name) values(6, '6:Synthetix/WETH');
INSERT INTO lp_names(pid, name) values(7, '7:UMA/WETH');
INSERT INTO lp_names(pid, name) values(8, '8:LINK/WETH');
INSERT INTO lp_names(pid, name) values(9, '9:BAND/WETH');
INSERT INTO lp_names(pid, name) values(10, '10:WETH/AMPL');
INSERT INTO lp_names(pid, name) values(11, '11:FYI/WETH');
INSERT INTO lp_names(pid, name) values(12, '12:SUSHI/WETH');
INSERT INTO lp_names(pid, name) values(13, '13:REN/WETH');
INSERT INTO lp_names(pid, name) values(14, '14:Synth/$BASED');
INSERT INTO lp_names(pid, name) values(15, '15:SERUM/WETH');
INSERT INTO lp_names(pid, name) values(16, '16:YAM2/WETH');
INSERT INTO lp_names(pid, name) values(17, '17:WETH/CRV');

WITH data AS(
 SELECT day, name, s.pid, deposit, withdraw, liquidity, count FROM (
 SELECT d.day, d.pid, d.sum as deposit, w.sum as withdraw, d.sum - w.sum as liquidity, w.count FROM
 ( SELECT date_trunc('day', evt_block_time) as day, pid, sum(amount) / 1e18 as sum , count(*) as count from sushi."MasterChef_evt_Deposit" GROUP BY 1, 2) as d
 LEFT JOIN
 ( SELECT date_trunc('day', evt_block_time) as day, pid, sum(amount) / 1e18 as sum , count(*) as count from sushi."MasterChef_evt_Withdraw" GROUP BY 1, 2) as w
 ON d.pid = w.pid AND d.day = w.day
 ) as s
 INNER JOIN lp_names as l ON l.pid = s.pid
)

SELECT
  day, name,
  sum(liquidity) over (partition by name order by day asc rows between unbounded preceding and current row) as liquidity
FROM data WHERE day <= current_date - interval '1 day';
