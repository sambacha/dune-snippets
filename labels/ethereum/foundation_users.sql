SELECT
  address,
  name AS label,
  'foundation user' AS type,
  'foundation' AS author
FROM
  foundation.user_names
WHERE
  updated_at >= '{{timestamp}}';
