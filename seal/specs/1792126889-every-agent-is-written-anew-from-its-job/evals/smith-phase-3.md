# smith — phase 3 non-inferiority

| Field | Value |
|---|---|
| Agent | smith |
| Phase | 3 |
| Baseline run | 2026-10-17T01:02:31.923Z f5cd1c49284b |
| New run | 2026-10-17T13:46:38.873Z c61d238d69b9 |
| Baseline suite | af9c924b7c5b03af5291017c226842655a8d83dd 613190e8d1ff62a399c435b3e799b8e0b7aa6a8a |
| New suite | af9c924b7c5b03af5291017c226842655a8d83dd 613190e8d1ff62a399c435b3e799b8e0b7aa6a8a |
| Baseline cut short | no |
| New cut short | no |
| Baseline report rows | 0 |
| Baseline false rows | 0 |
| New report rows | 0 |
| New false rows | 0 |
| Baseline spend USD | 6.3830 |
| New spend USD | 5.9980 |
| Baseline tokens read, every model | 8978191 |
| New tokens read, every model | 8270573 |
| Baseline tool calls | 197 |
| New tool calls | 183 |
| Baseline wall seconds | 1144.5 |
| New wall seconds | 1320.6 |
| Baseline preload bytes | 94693 |
| New preload bytes | 90594 |
| Baseline tokens per tool call | 45574.6 |
| New tokens per tool call | 45194.4 |
| Baseline tokens per true find | unknown |
| New tokens per true find | unknown |

## Graders

| Kind | Case | Grader | Old passed | Old runs | New passed | New runs |
|---|---|---|---|---|---|---|
| reach | smith rule-smith-count-words | reach-smith | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-count-words | shape-built | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-count-words | shape-committed | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-count-words | shape-no-probe-left | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-count-words | shape-phase-record | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-count-words | shape-tested | 2 | 2 | 2 | 2 |
| reach | smith rule-smith-is-palindrome | reach-smith | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-is-palindrome | shape-built | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-is-palindrome | shape-committed | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-is-palindrome | shape-no-probe-left | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-is-palindrome | shape-phase-record | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-is-palindrome | shape-tested | 2 | 2 | 2 | 2 |
| reach | smith rule-smith-slugify | reach-smith | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-slugify | shape-built | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-slugify | shape-committed | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-slugify | shape-no-probe-left | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-slugify | shape-phase-record | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-slugify | shape-tested | 2 | 2 | 2 | 2 |
| reach | smith rule-smith-truncate | reach-smith | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-truncate | shape-built | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-truncate | shape-committed | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-truncate | shape-no-probe-left | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-truncate | shape-phase-record | 2 | 2 | 2 | 2 |
| shape | smith rule-smith-truncate | shape-tested | 2 | 2 | 2 | 2 |

## New preload

| File | sha256 |
|---|---|
| agents/smith.md | 81f63874580681eac6d1920f2b6a10fd3ff24b376c2cd0b6308b0f57d879d1cd |
| skills/agent-contract/SKILL.md | e4f679e31c041d4f7934367a9ce3bd826cf68af03e9e5319e84b3a8d327e34b3 |
| skills/implement/SKILL.md | bafff509c7b31c46ba8be3bcd71681a8682c5af6c76bd3fa28a5d743415315d9 |
| skills/writing-style/SKILL.md | f509dfeeaec143e9c4d6580e77c919b885629da5bd28186db3bf569210dcd33e |

Verdict: pass

- every pass rule holds
