---
type: 'regex'
target: {source: 'file', path: 'tests/test_textutil.py'}
pattern: 'shout'
flags: 'i'
match: 'not_contains'
---
`tests/test_textutil.py` no longer names `shout`, in any case or as part of a name.
