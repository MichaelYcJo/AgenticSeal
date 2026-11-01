---
type: 'regex'
target: {source: 'file', path: 'seal/threads/1793457436-row-deletion-check-and-a-symlink/trail/rounds/round-1.md'}
pattern: '^location: .*(?:skills\/verify\/scripts\/unverified_check\.py:(?:1590|1591|1592|1593|1594|1595|1596|1597|1598|1599|1600|1601|1602|1603|1604|1605|1606|1607|1608|1609|1610|1611|1612|1613|1614|1615|1616|1617|1618|1619|1620)(?!\d))'
flags: 'm'
---
The seeded defect: 'if at is None or at.split("/")[0] == "..":' made 'if at is None or at.split("/")[0] != "..":' in `skills/verify/scripts/unverified_check.py#main`.
