---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1792363189-rule-3-decides-on-the-agent-not-one-run/rounds/round-1.md'}
pattern: '^## Findings[ \t]*\n(?:(?!^## )[\s\S])*?^### \d+\. [^\n]+\n(?:(?!^##)[\s\S])*?^```seal\nseverity: \S'
flags: 'm'
---
The report carries `## Findings` with a `### <n>.` section and its finding block.
