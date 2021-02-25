with psm_tx as (
    select call_block_time, replace(encode(i, 'escape'), '\000', ''), dink/10^18 as amount, call_tx_hash as tx
    from makermcd."VAT_call_frob"
    where replace(encode(i, 'escape'), '\000', '') = 'PSM-USDC-A'
        and call_success
),
tx_fees as (
    select call_tx_hash as tx, rad/10^45 as fees
    from makermcd."VAT_call_move"
    inner join psm_tx on tx = call_tx_hash
    where dst = '\xa950524441892a31ebddf91d3ceefa04bf454466'
)
select to_char(call_block_time, 'YYYY-MM') as period, sum(fees) as revenues
from psm_tx
left join tx_fees using (tx)
group by 1
order by 1
