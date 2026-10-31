---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791779434-under-automation-the-guard-asks-nobody/rounds/round-5.md'}
pattern: '^## Findings[ \t]*\n(?:(?!^## )[\s\S])*?^### \d+\. [^\n]+\n(?:(?!^##)[\s\S])*?^```seal\nseverity: \S'
flags: 'm'
---
The report carries `## Findings` with a `### <n>.` section and its finding block.
