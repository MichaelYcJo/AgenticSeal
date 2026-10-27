---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791384154-a-records-finding-closes-once-at-the-runs-end/rounds/round-1.md'}
pattern: '^location: .*(?:skills\/code-review\/scripts\/round_record\.py:(?:4840|4841|4842|4843|4844|4845|4846|4847|4848|4849|4850|4851|4852|4853|4854|4855|4856|4857|4858|4859|4860|4861|4862|4863|4864|4865|4866|4867|4868|4869|4870)(?!\d))'
flags: 'm'
---
Round 1's finding 3: A stopped run whose notes were not closed at the `second` leaves them open for good: `seal`, `carried_notes` and `carried_line` stop reading them, and `notes` refuses them as outside the run
