SELECT  project,
        date_trunc('month', block_time),
        SUM(usd_amount) as usd_volume
FROM dex."trades" t
WHERE block_time > date_trunc('month', now()) - interval '13 months'
AND block_time < date_trunc('day', Now())
AND category = 'DEX'
GROUP BY A, B;
