---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791384160-a-fix-range-is-its-own-commits-across-a-merge/rounds/round-2.md'}
pattern: '^## Findings[ \t]*\n(?:(?!^## )[\s\S])*?^### \d+\. [^\n]+\n(?:(?!^##)[\s\S])*?^verdict: \S'
flags: 'm'
---
The report carries `## Findings` with a `### <n>.` section and its `verdict:` line.
