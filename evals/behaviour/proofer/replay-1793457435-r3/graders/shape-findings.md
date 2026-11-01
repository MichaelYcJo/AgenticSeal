---
type: 'regex'
target: {source: 'file', path: 'seal/threads/1793457435-replay-targets-reads-both-layouts/trail/rounds/round-3.md'}
pattern: '^## Findings[ \t]*\n(?:(?!^## )[\s\S])*?^### \d+\. [^\n]+\n(?:(?!^##)[\s\S])*?^```seal\nseverity: \S'
flags: 'm'
---
The report carries `## Findings` with a `### <n>.` section and its finding block.
