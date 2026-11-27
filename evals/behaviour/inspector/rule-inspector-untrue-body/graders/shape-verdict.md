---
type: 'regex'
target: {source: 'file', path: 'seal/threads/1790000030-inspection-untrue-body/inspection.md'}
pattern: '^```seal\n(?:[^`\n][^\n]*\n)*?Verdict: withheld reason: \S'
flags: 'm'
---
`inspection.md` carries the verdict `withheld` in a verdict block.
