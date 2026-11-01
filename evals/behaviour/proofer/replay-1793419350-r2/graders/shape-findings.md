---
type: 'regex'
target: {source: 'file', path: 'seal/threads/1793419350-a-prefix-states-what-a-change-is/trail/rounds/round-2.md'}
pattern: '^## Findings[ \t]*\n(?:(?!^## )[\s\S])*?^### \d+\. [^\n]+\n(?:(?!^##)[\s\S])*?^```seal\nseverity: \S'
flags: 'm'
---
The report carries `## Findings` with a `### <n>.` section and its finding block.
