---
type: 'regex'
target: {source: 'file', path: 'seal/threads/1793419351-project-rules-live-in-the-repository/trail/rounds/round-4.md'}
pattern: '^## Findings[ \t]*\n(?:(?!^## )[\s\S])*?^### \d+\. [^\n]+\n(?:(?!^##)[\s\S])*?^```seal\nseverity: \S'
flags: 'm'
---
The report carries `## Findings` with a `### <n>.` section and its finding block.
