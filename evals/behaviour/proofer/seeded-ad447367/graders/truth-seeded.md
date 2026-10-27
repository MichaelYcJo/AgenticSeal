---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791384160-a-fix-range-is-its-own-commits-across-a-merge/rounds/round-1.md'}
pattern: '^location: .*(?:skills\/code-review\/scripts\/chain_check\.py:(?:4515|4516|4517|4518|4519|4520|4521|4522|4523|4524|4525|4526|4527|4528|4529|4530|4531|4532|4533|4534|4535|4536|4537|4538|4539|4540|4541|4542|4543|4544|4545)(?!\d))'
flags: 'm'
---
The seeded defect: 'while i < len(tokens):' made 'while i <= len(tokens):' in `skills/code-review/scripts/chain_check.py#own_commits`.
