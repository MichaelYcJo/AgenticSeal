# warden — phase 3 non-inferiority

| Field | Value |
|---|---|
| Agent | warden |
| Phase | 3 |
| Baseline run | 2026-10-18T04:06:13.352Z 2225219e1eb1 |
| New run | 2026-10-19T05:23:26.008Z 60a81e1e9abf |
| Baseline suite | af9c924b7c5b03af5291017c226842655a8d83dd d8dfd549c0100c131019193b35655c59e7218282 |
| New suite | af9c924b7c5b03af5291017c226842655a8d83dd d8dfd549c0100c131019193b35655c59e7218282 |
| Baseline cut short | no |
| New cut short | no |
| Baseline report rows | 43 |
| Baseline false rows | 24 |
| New report rows | 39 |
| New false rows | 25 |
| Baseline spend USD | 41.7424 |
| New spend USD | 39.7893 |
| Baseline tokens read, every model | 82590654 |
| New tokens read, every model | 74387414 |
| Baseline tool calls | 940 |
| New tool calls | 872 |
| Baseline wall seconds | 7586.7 |
| New wall seconds | 6959.8 |
| Baseline preload bytes | 27173 |
| New preload bytes | 27168 |
| Baseline tokens per tool call | 87862.4 |
| New tokens per tool call | 85306.7 |
| Baseline tokens per true find | 4346877 |
| New tokens per true find | 5722109 |

## Graders

| Kind | Case | Grader | Old passed | Old runs | New passed | New runs |
|---|---|---|---|---|---|---|
| reach | warden replay-1791382684-r2 | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden replay-1791382684-r2 | shape-findings | 2 | 2 | 2 | 2 |
| shape | warden replay-1791382684-r2 | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden replay-1791382684-r2 | shape-words-only | 2 | 2 | 2 | 2 |
| truth | warden replay-1791382684-r2 | truth-1 | 2 | 2 | 0 | 2 |
| truth | warden replay-1791382684-r2 | truth-2 | 1 | 2 | 0 | 2 |
| truth | warden replay-1791382684-r2 | truth-3 | 1 | 2 | 0 | 2 |
| reach | warden replay-1791382684-r5 | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden replay-1791382684-r5 | shape-findings | 2 | 2 | 2 | 2 |
| shape | warden replay-1791382684-r5 | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden replay-1791382684-r5 | shape-words-only | 2 | 2 | 2 | 2 |
| truth | warden replay-1791382684-r5 | truth-2 | 1 | 2 | 0 | 2 |
| reach | warden replay-1791384160-r2 | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden replay-1791384160-r2 | shape-findings | 2 | 2 | 2 | 2 |
| shape | warden replay-1791384160-r2 | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden replay-1791384160-r2 | shape-words-only | 2 | 2 | 2 | 2 |
| truth | warden replay-1791384160-r2 | truth-1 | 2 | 2 | 2 | 2 |
| truth | warden replay-1791384160-r2 | truth-2 | 1 | 2 | 0 | 2 |
| reach | warden replay-1791779434-r5 | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden replay-1791779434-r5 | shape-findings | 2 | 2 | 2 | 2 |
| shape | warden replay-1791779434-r5 | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden replay-1791779434-r5 | shape-words-only | 2 | 2 | 2 | 2 |
| truth | warden replay-1791779434-r5 | truth-1 | 1 | 2 | 1 | 2 |
| reach | warden rule-warden-one-finding | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden rule-warden-one-finding | shape-findings | 2 | 2 | 2 | 2 |
| shape | warden rule-warden-one-finding | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden rule-warden-one-finding | shape-words-only | 2 | 2 | 2 | 2 |
| truth | warden rule-warden-one-finding | truth-shout-twice | 2 | 2 | 2 | 2 |
| reach | warden seeded-279a580b | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden seeded-279a580b | shape-findings | 2 | 2 | 2 | 2 |
| shape | warden seeded-279a580b | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden seeded-279a580b | shape-words-only | 2 | 2 | 2 | 2 |
| truth | warden seeded-279a580b | truth-seeded | 2 | 2 | 2 | 2 |
| reach | warden seeded-4d316179 | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden seeded-4d316179 | shape-findings | 2 | 2 | 2 | 2 |
| shape | warden seeded-4d316179 | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden seeded-4d316179 | shape-words-only | 2 | 2 | 2 | 2 |
| truth | warden seeded-4d316179 | truth-seeded | 2 | 2 | 2 | 2 |
| reach | warden seeded-9b644676 | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden seeded-9b644676 | shape-findings | 2 | 2 | 2 | 2 |
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
| agents/warden.md | 12c1c4c2dc9e2c64d83d4d1c910836e5f51108efd566f73a6976017b07974c6e |
| skills/agent-contract/SKILL.md | 642b0da67c6795a1aa75ba16d0b17bac4e48639d05134bcdb050c34fcec6ee4e |

Verdict: fail

- recall fell from 19 to 13 finds: warden replay-1791382684-r2/truth-1, warden replay-1791382684-r2/truth-2, warden replay-1791382684-r2/truth-3, warden replay-1791382684-r5/truth-2, warden replay-1791384160-r2/truth-2
- false-finding rate rose from 0.558 to 0.641
