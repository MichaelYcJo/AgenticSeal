---
type: 'regex'
target: {source: 'file', path: 'seal/threads/1790000030-guarantee-untrue-body/guarantee.md'}
pattern: '^```seal\n(?:[^`\n][^\n]*\n)*?Verdict: withheld reason: \S'
flags: 'm'
---
`guarantee.md` carries the verdict `withheld` in a verdict block.
