with transactions as 
(
select tok.symbol
        , evt_block_time
        , sum("value"/10^v.decimals) as amt
from erc20."ERC20_evt_Transfer" t
inner join  
(
    select * from dune_user_generated."view_v2_atokens" 
    union all
    select * from dune_user_generated."view_v1_atokens" 
) v
on v. contract_address = t.contract_address
left join erc20."tokens" tok on tok.contract_address = v.underlying_token_address
--where   evt_block_time > now() - interval '1 days'


group by 1,2
order by 3 desc

)

, prices as 
(
SELECT avg(price) AS price,
          date(MINUTE) AS dt,
          symbol
   FROM prices.usd
   WHERE symbol<>'ETH'
   --and minute   > now() - interval '1 days'

   GROUP BY 2,3
   
   UNION SELECT avg(price) AS price,
                date(MINUTE) AS dt,
                symbol
   FROM prices.layer1_usd_eth
   WHERE symbol='ETH'
   -- and minute   > now() - interval '1 days'
   GROUP BY 2,3
   )

SELECT t.symbol
     , date_trunc('month', evt_block_time) as month
     , sum(amt*price) as "usd amount"
from transactions t
left join prices p on date(evt_block_time) = p.dt
AND p.symbol = t.symbol
group by 1,2
order by 3 desc




--select * from erc20."tokens"
