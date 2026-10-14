---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791852614-survivor-check-reads-a-range-as-its-own-commits/rounds/round-1-report.md'}
pattern: '^\| (?:🔴|🟡) \d+ \|.*(?:skills\/code-review\/scripts\/survivor_check\.py#(?:owned)\b|skills\/code-review\/scripts\/survivor_check\.py:(?:513|514|515|516|517|518|519|520|521|522|523|524|525|526|527|528|529|530|531|532|533|534|535|536|537|538|539|540|541|542|543)(?!\d))'
flags: 'm'
---
The seeded defect: 'if separator(spec) != "..":' made 'if separator(spec) == "..":' in `skills/code-review/scripts/survivor_check.py#owned`.
