---
type: 'regex'
target: {source: 'file', path: 'README.md'}
pattern: '\bshout\b'
match: 'not_contains'
---
`README.md` no longer names `shout`.
