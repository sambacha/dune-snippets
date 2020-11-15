SELECT
    a.evt_block_time AS block_time,
    'Curve' AS project,
    NULL::text AS version,
    buyer AS trader_a,
    NULL::bytea AS trader_b,
    (tokens_bought / 4) AS token_a_amount_raw,
    (tokens_sold / 4) AS token_b_amount_raw,
    '\xdF5e0e81Dff6FAF3A7e52BA697820c5e32D806A8'::bytea as token_a_address,
    '\xF61718057901F84C4eEC4339EF8f0D86D2B45600'::bytea as token_b_address,
    a.contract_address AS exchange_contract_address,
    a.evt_tx_hash AS tx_hash,
    NULL::integer[] AS trace_address,
    a.evt_index AS evt_index
FROM curvefi."susd_evt_TokenExchange" a
WHERE bought_id = 0

UNION

SELECT
    a.evt_block_time AS block_time,
    'Curve' AS project,
    NULL::text AS version,
    buyer AS trader_a,
    NULL::bytea AS trader_b,
    (tokens_bought / 4) AS token_a_amount_raw,
    (tokens_sold / 4) AS token_b_amount_raw,
    '\xdF5e0e81Dff6FAF3A7e52BA697820c5e32D806A8'::bytea as token_a_address,
    '\xF61718057901F84C4eEC4339EF8f0D86D2B45600'::bytea as token_b_address,
    a.contract_address AS exchange_contract_address,
    a.evt_tx_hash AS tx_hash,
    NULL::integer[] AS trace_address,
    a.evt_index AS evt_index
FROM curvefi."susd_evt_TokenExchange" a
WHERE bought_id = 1

UNION

SELECT
    a.evt_block_time AS block_time,
    'Curve' AS project,
    NULL::text AS version,
    buyer AS trader_a,
    NULL::bytea AS trader_b,
    (tokens_bought / 4) AS token_a_amount_raw,
    (tokens_sold / 4) AS token_b_amount_raw,
    '\xdF5e0e81Dff6FAF3A7e52BA697820c5e32D806A8'::bytea as token_a_address,
    '\xF61718057901F84C4eEC4339EF8f0D86D2B45600'::bytea as token_b_address,
    a.contract_address AS exchange_contract_address,
    a.evt_tx_hash AS tx_hash,
    NULL::integer[] AS trace_address,
    a.evt_index AS evt_index
FROM curvefi."susd_evt_TokenExchange" a
WHERE bought_id = 2

UNION

SELECT
    a.evt_block_time AS block_time,
    'Curve' AS project,
    NULL::text AS version,
    buyer AS trader_a,
    NULL::bytea AS trader_b,
    (tokens_bought / 4) AS token_a_amount_raw,
    (tokens_sold / 4) AS token_b_amount_raw,
    '\xdF5e0e81Dff6FAF3A7e52BA697820c5e32D806A8'::bytea as token_a_address,
    '\xF61718057901F84C4eEC4339EF8f0D86D2B45600'::bytea as token_b_address,
    a.contract_address AS exchange_contract_address,
    a.evt_tx_hash AS tx_hash,
    NULL::integer[] AS trace_address,
    a.evt_index AS evt_index
FROM curvefi."susd_evt_TokenExchange" a
WHERE bought_id = 3

UNION

SELECT
    a.evt_block_time AS block_time,
    'Curve' AS project,
    NULL::text AS version,
    buyer AS trader_a,
    NULL::bytea AS trader_b,
    (tokens_bought / 4) AS token_a_amount_raw,
    (tokens_sold / 4) AS token_b_amount_raw,
    '\xdF5e0e81Dff6FAF3A7e52BA697820c5e32D806A8'::bytea as token_a_address,
    '\x57Ab1ec28D129707052df4dF418D58a2D46d5f51'::bytea as token_b_address,
    a.contract_address AS exchange_contract_address,
    a.evt_tx_hash AS tx_hash,
    NULL::integer[] AS trace_address,
    a.evt_index AS evt_index
FROM curvefi."susd_evt_TokenExchangeUnderlying" a
WHERE bought_id = 0

UNION

SELECT
    a.evt_block_time AS block_time,
    'Curve' AS project,
    NULL::text AS version,
    buyer AS trader_a,
    NULL::bytea AS trader_b,
    (tokens_bought / 4) AS token_a_amount_raw,
    (tokens_sold / 4) AS token_b_amount_raw,
    '\xdF5e0e81Dff6FAF3A7e52BA697820c5e32D806A8'::bytea as token_a_address,
    '\x57Ab1ec28D129707052df4dF418D58a2D46d5f51'::bytea as token_b_address,
    a.contract_address AS exchange_contract_address,
    a.evt_tx_hash AS tx_hash,
    NULL::integer[] AS trace_address,
    a.evt_index AS evt_index
FROM curvefi."susd_evt_TokenExchangeUnderlying" a
WHERE bought_id = 1

UNION

SELECT
    a.evt_block_time AS block_time,
    'Curve' AS project,
    NULL::text AS version,
    buyer AS trader_a,
    NULL::bytea AS trader_b,
    (tokens_bought / 4) AS token_a_amount_raw,
    (tokens_sold / 4) AS token_b_amount_raw,
    '\xdF5e0e81Dff6FAF3A7e52BA697820c5e32D806A8'::bytea as token_a_address,
    '\x57Ab1ec28D129707052df4dF418D58a2D46d5f51'::bytea as token_b_address,
    a.contract_address AS exchange_contract_address,
    a.evt_tx_hash AS tx_hash,
    NULL::integer[] AS trace_address,
    a.evt_index AS evt_index
FROM curvefi."susd_evt_TokenExchangeUnderlying" a
WHERE bought_id = 2

UNION

SELECT
    a.evt_block_time AS block_time,
    'Curve' AS project,
    NULL::text AS version,
    buyer AS trader_a,
    NULL::bytea AS trader_b,
    (tokens_bought / 4) AS token_a_amount_raw,
    (tokens_sold / 4) AS token_b_amount_raw,
    '\xdF5e0e81Dff6FAF3A7e52BA697820c5e32D806A8'::bytea as token_a_address,
    '\x57Ab1ec28D129707052df4dF418D58a2D46d5f51'::bytea as token_b_address,
    a.contract_address AS exchange_contract_address,
    a.evt_tx_hash AS tx_hash,
    NULL::integer[] AS trace_address,
    a.evt_index AS evt_index
FROM curvefi."susd_evt_TokenExchangeUnderlying" a
WHERE bought_id = 3
