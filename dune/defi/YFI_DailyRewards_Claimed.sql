(SELECT date_trunc('day', evt_block_time) as time,
    sum(reward / 1e18) as reward
    from yearn."YearnGovernance_YFI_evt_RewardPaid"
    group by time)

UNION

(SELECT date_trunc('day', evt_block_time) as time,
    sum(reward / 1e18) as reward
    from yearn."YearnRewards_evt_RewardPaid"
    group by time)
order by time asc
