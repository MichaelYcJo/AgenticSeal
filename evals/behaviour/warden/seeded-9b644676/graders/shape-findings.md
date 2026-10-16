---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1791384161-the-plugin-directory-check-reads-the-directory/rounds/round-1.md'}
pattern: '^## Findings[ \t]*\n(?:(?!^## )[\s\S])*?^### \d+\. [^\n]+\n(?:(?!^##)[\s\S])*?^verdict: \S'
flags: 'm'
---
The report carries `## Findings` with a `### <n>.` section and its `verdict:` line.
