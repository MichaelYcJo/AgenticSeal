---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791384154-a-records-finding-closes-once-at-the-runs-end/rounds/round-1.md'}
pattern: '^location: .*(?:skills\/code-review\/scripts\/chain_check\.py:(?:841|842|843|844|845|846|847|848|849|850|851|852|853|854|855|856|857|858|859|860|861|862|863|864|865|866|867|868|869|870|871)(?!\d))'
flags: 'm'
---
Round 1's finding 2: `NOTES_FROM` is this item's id, but the batch's siblings (1791384155 to 1791384162) run under 0.20.0's `close`, which demands and admits ⬜ `fixed`; #858's records already fail arm A three times
