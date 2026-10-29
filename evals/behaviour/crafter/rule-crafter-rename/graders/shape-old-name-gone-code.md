---
type: 'regex'
target: {source: 'file', path: 'src/textutil.py'}
pattern: '\bshout\b'
match: 'not_contains'
---
`src/textutil.py` no longer names `shout`.
