---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1790000030-broad-run-failing-test/broad-gate.md'}
pattern: '^\| Broad gate \| [0-9a-f]{7,40} against '
flags: 'm'
match: 'not_contains'
---
`broad-gate.md` names the run on a green run, and only then.
