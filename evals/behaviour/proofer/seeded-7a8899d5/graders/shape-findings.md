---
type: 'regex'
target: {source: 'file', path: 'seal/threads/1793437163-fields-stand-in-marked-blocks/trail/rounds/round-1.md'}
pattern: '^## Findings[ \t]*\n(?:(?!^## )[\s\S])*?^### \d+\. [^\n]+\n(?:(?!^##)[\s\S])*?^```seal\nseverity: \S'
flags: 'm'
---
The report carries `## Findings` with a `### <n>.` section and its finding block.
