---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791384154-a-records-finding-closes-once-at-the-runs-end/rounds/round-1.md'}
pattern: '^location: .*(?:skills\/code-review\/scripts\/chain_check\.py:(?:1850|1851|1852|1853|1854|1855|1856|1857|1858|1859|1860|1861|1862|1863|1864|1865|1866|1867|1868|1869|1870|1871|1872|1873|1874|1875|1876|1877|1878|1879|1880)(?!\d))'
flags: 'm'
---
The seeded defect: 'if found is None or NOTE not in found.group(0):' made 'if found is None and NOTE not in found.group(0):' in `skills/code-review/scripts/chain_check.py#note_rows`.
