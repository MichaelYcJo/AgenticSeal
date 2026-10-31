---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791384154-a-records-finding-closes-once-at-the-runs-end/rounds/round-1.md'}
pattern: '^## Findings[ \t]*\n(?:(?!^## )[\s\S])*?^### \d+\. [^\n]+\n(?:(?!^##)[\s\S])*?^```seal\nseverity: \S'
flags: 'm'
---
The report carries `## Findings` with a `### <n>.` section and its finding block.
