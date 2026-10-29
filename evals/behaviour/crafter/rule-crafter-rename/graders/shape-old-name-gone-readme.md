---
type: 'regex'
target: {source: 'file', path: 'README.md'}
pattern: 'shout'
flags: 'i'
match: 'not_contains'
---
`README.md` no longer names `shout`, in any case or as part of a name.
