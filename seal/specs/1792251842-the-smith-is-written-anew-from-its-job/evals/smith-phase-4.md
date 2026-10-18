# smith — phase 4 non-inferiority

| Field | Value |
|---|---|
| Agent | smith |
| Phase | 4 |
| Baseline run | 2026-10-17T16:02:43.061Z 04215553e333 |
| New run | 2026-10-18T04:01:07.018Z 008fe9de406b |
| Baseline suite | af9c924b7c5b03af5291017c226842655a8d83dd 613190e8d1ff62a399c435b3e799b8e0b7aa6a8a |
| New suite | af9c924b7c5b03af5291017c226842655a8d83dd 613190e8d1ff62a399c435b3e799b8e0b7aa6a8a |
| Baseline cut short | no |
| New cut short | no |
| Baseline report rows | 0 |
| Baseline false rows | 0 |
| New report rows | 0 |
| New false rows | 0 |
| Baseline spend USD | 6.6210 |
| New spend USD | 5.3675 |
| Baseline tokens read, every model | 9561086 |
| New tokens read, every model | 7342587 |
| Baseline tool calls | 222 |
| New tool calls | 204 |
| Baseline wall seconds | 1360.8 |
| New wall seconds | 1081.3 |
| Baseline preload bytes | 90728 |
| New preload bytes | 26596 |
| Baseline tokens per tool call | 43068.0 |
| New tokens per tool call | 35993.1 |
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
| agents/smith.md | fdaeb3a0cb7c8b62923f92ce8e31eceb20c197677c96ca64535cf24d453cde01 |
| skills/agent-contract/SKILL.md | 642b0da67c6795a1aa75ba16d0b17bac4e48639d05134bcdb050c34fcec6ee4e |

Verdict: pass

- every pass rule holds
