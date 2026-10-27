---
type: 'regex'
target: {source: 'file', path: 'seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/rounds/round-1.md'}
pattern: '^## Findings[ \t]*\n(?:(?!^## )[\s\S])*?^### \d+\. [^\n]+\n(?:(?!^##)[\s\S])*?^verdict: \S'
flags: 'm'
---
The report carries `## Findings` with a `### <n>.` section and its `verdict:` line.
