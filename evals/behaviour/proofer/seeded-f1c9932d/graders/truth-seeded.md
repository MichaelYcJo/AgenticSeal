---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/rounds/round-1.md'}
pattern: '^location: .*(?:skills\/code-review\/scripts\/chain_check\.py:(?:1357|1358|1359|1360|1361|1362|1363|1364|1365|1366|1367|1368|1369|1370|1371|1372|1373|1374|1375|1376|1377|1378|1379|1380|1381|1382|1383|1384|1385|1386|1387)(?!\d))'
flags: 'm'
---
The seeded defect: 'for entry in (cell or "").split(EARLIER_RUN)[1:]:' made 'for entry in (cell and "").split(EARLIER_RUN)[1:]:' in `skills/code-review/scripts/chain_check.py#earlier_verdicts`.
