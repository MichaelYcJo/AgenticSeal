---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791384160-a-fix-range-is-its-own-commits-across-a-merge/rounds/round-1.md'}
pattern: '^\| (?:🔴|🟡) \d+ \|.*(?:skills\/code-review\/scripts\/chain_check\.py#(?:own_commits)\b|skills\/code-review\/scripts\/chain_check\.py:(?:4632|4633|4634|4635|4636|4637|4638|4639|4640|4641|4642|4643|4644|4645|4646|4647|4648|4649|4650|4651|4652|4653|4654|4655|4656|4657|4658|4659|4660|4661|4662)(?!\d))'
flags: 'm'
---
The seeded defect: 'while i < len(tokens):' made 'while i <= len(tokens):' in `skills/code-review/scripts/chain_check.py#own_commits`.
