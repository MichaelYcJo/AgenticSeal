# warden — phase 2 non-inferiority

| Field | Value |
|---|---|
| Agent | warden |
| Phase | 2 |
| Baseline run | 2026-10-17T01:17:39.397Z d9a7d879cb6e |
| New run | 2026-10-17T03:16:55.356Z f28b5b4974cf |
| Baseline suite | af9c924b7c5b03af5291017c226842655a8d83dd d8dfd549c0100c131019193b35655c59e7218282 |
| New suite | af9c924b7c5b03af5291017c226842655a8d83dd d8dfd549c0100c131019193b35655c59e7218282 |
| Baseline cut short | no |
| New cut short | no |
| Baseline report rows | 55 |
| Baseline false rows | 43 |
| New report rows | 39 |
| New false rows | 22 |
| Baseline spend USD | 36.0352 |
| New spend USD | 37.8482 |
| Baseline tokens read, every model | 66468871 |
| New tokens read, every model | 70472015 |
| Baseline tool calls | 746 |
| New tool calls | 826 |
| Baseline wall seconds | 5779.5 |
| New wall seconds | 6669.7 |
| Baseline preload bytes | 76019 |
| New preload bytes | 30620 |
| Baseline tokens per tool call | 89100.4 |
| New tokens per tool call | 85317.2 |
| Baseline tokens per true find | 5112990 |
| New tokens per true find | 4404501 |

## Graders

| Kind | Case | Grader | Old passed | Old runs | New passed | New runs |
|---|---|---|---|---|---|---|
| reach | warden replay-1791382684-r2 | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden replay-1791382684-r2 | shape-findings | 2 | 2 | 2 | 2 |
| shape | warden replay-1791382684-r2 | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden replay-1791382684-r2 | shape-words-only | 2 | 2 | 2 | 2 |
| truth | warden replay-1791382684-r2 | truth-1 | 1 | 2 | 0 | 2 |
| truth | warden replay-1791382684-r2 | truth-2 | 1 | 2 | 1 | 2 |
| truth | warden replay-1791382684-r2 | truth-3 | 0 | 2 | 0 | 2 |
| reach | warden replay-1791382684-r5 | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden replay-1791382684-r5 | shape-findings | 2 | 2 | 2 | 2 |
| shape | warden replay-1791382684-r5 | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden replay-1791382684-r5 | shape-words-only | 2 | 2 | 2 | 2 |
| truth | warden replay-1791382684-r5 | truth-2 | 0 | 2 | 1 | 2 |
| reach | warden replay-1791384160-r2 | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden replay-1791384160-r2 | shape-findings | 1 | 2 | 2 | 2 |
| shape | warden replay-1791384160-r2 | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden replay-1791384160-r2 | shape-words-only | 1 | 2 | 2 | 2 |
| truth | warden replay-1791384160-r2 | truth-1 | 1 | 2 | 2 | 2 |
| truth | warden replay-1791384160-r2 | truth-2 | 1 | 2 | 1 | 2 |
| reach | warden replay-1791779434-r5 | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden replay-1791779434-r5 | shape-findings | 0 | 2 | 1 | 2 |
| shape | warden replay-1791779434-r5 | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden replay-1791779434-r5 | shape-words-only | 1 | 2 | 2 | 2 |
| truth | warden replay-1791779434-r5 | truth-1 | 0 | 2 | 1 | 2 |
| reach | warden rule-warden-one-finding | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden rule-warden-one-finding | shape-findings | 2 | 2 | 2 | 2 |
| shape | warden rule-warden-one-finding | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden rule-warden-one-finding | shape-words-only | 2 | 2 | 2 | 2 |
| truth | warden rule-warden-one-finding | truth-shout-twice | 2 | 2 | 2 | 2 |
| reach | warden seeded-279a580b | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden seeded-279a580b | shape-findings | 2 | 2 | 2 | 2 |
| shape | warden seeded-279a580b | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden seeded-279a580b | shape-words-only | 1 | 2 | 2 | 2 |
| truth | warden seeded-279a580b | truth-seeded | 1 | 2 | 2 | 2 |
| reach | warden seeded-4d316179 | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden seeded-4d316179 | shape-findings | 2 | 2 | 2 | 2 |
| shape | warden seeded-4d316179 | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden seeded-4d316179 | shape-words-only | 2 | 2 | 2 | 2 |
| truth | warden seeded-4d316179 | truth-seeded | 2 | 2 | 2 | 2 |
| reach | warden seeded-9b644676 | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden seeded-9b644676 | shape-findings | 2 | 2 | 1 | 2 |
| shape | warden seeded-9b644676 | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden seeded-9b644676 | shape-words-only | 2 | 2 | 2 | 2 |
| truth | warden seeded-9b644676 | truth-seeded | 2 | 2 | 2 | 2 |
| reach | warden seeded-ad447367 | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden seeded-ad447367 | shape-findings | 2 | 2 | 2 | 2 |
| shape | warden seeded-ad447367 | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden seeded-ad447367 | shape-words-only | 2 | 2 | 2 | 2 |
| truth | warden seeded-ad447367 | truth-seeded | 2 | 2 | 2 | 2 |

## New preload

| File | sha256 |
|---|---|
| agents/warden.md | cf5e1bad6664ce2563522ba9f9aa2ad6a0f818daccd9d5afa11047b74e9a40cc |
| skills/agent-contract/SKILL.md | a58c7a0541cc25660929a41f7bee1fe9e9976463e38397d74fd001764925ffa9 |

Verdict: pass

- every pass rule holds
