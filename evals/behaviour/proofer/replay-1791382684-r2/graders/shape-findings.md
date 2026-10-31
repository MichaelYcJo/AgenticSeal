---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791382684-every-reader-and-record-is-inventoried/rounds/round-2.md'}
pattern: '^## Findings[ \t]*\n(?:(?!^## )[\s\S])*?^### \d+\. [^\n]+\n(?:(?!^##)[\s\S])*?^```seal\nseverity: \S'
flags: 'm'
---
The report carries `## Findings` with a `### <n>.` section and its finding block.
