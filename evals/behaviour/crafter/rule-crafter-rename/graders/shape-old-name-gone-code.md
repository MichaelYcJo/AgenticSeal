---
type: 'regex'
target: {source: 'file', path: 'src/textutil.py'}
pattern: 'shout'
flags: 'i'
match: 'not_contains'
---
`src/textutil.py` no longer names `shout`, in any case or as part of a name.
