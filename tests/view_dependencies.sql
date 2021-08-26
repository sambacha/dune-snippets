-- source: https://stackoverflow.com/a/48770535/1838257

--CREATE OR REPLACE VIEW dune_user_generated.gosuto_view_dependencies AS
SELECT DISTINCT srcobj.oid AS src_oid,
    srcnsp.nspname AS src_schemaname,
    srcobj.relname AS src_objectname,
    tgtobj.oid AS dependent_viewoid,
    tgtnsp.nspname AS dependant_schemaname,
    tgtobj.relname AS dependant_objectname
FROM pg_class srcobj
  JOIN pg_depend srcdep ON srcobj.oid = srcdep.refobjid
  JOIN pg_depend tgtdep ON srcdep.objid = tgtdep.objid
  JOIN pg_class tgtobj ON tgtdep.refobjid = tgtobj.oid AND srcobj.oid <> tgtobj.oid
  LEFT JOIN pg_namespace srcnsp ON srcobj.relnamespace = srcnsp.oid
  LEFT JOIN pg_namespace tgtnsp ON tgtobj.relnamespace = tgtnsp.oid
WHERE tgtdep.deptype = 'i'::"char" AND tgtobj.relkind = 'v'::"char"
    AND src_objectname LIKE '%badgerdao%'
-- filter like so:
-- SELECT * FROM dune_user_generated.gosuto_view_dependencies
-- WHERE src_objectname LIKE '%filter_word%'
