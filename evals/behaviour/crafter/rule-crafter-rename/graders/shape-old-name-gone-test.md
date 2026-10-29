---
type: 'regex'
target: {source: 'file', path: 'tests/test_textutil.py'}
pattern: '\bshout\b'
match: 'not_contains'
---
`tests/test_textutil.py` no longer names `shout`.
