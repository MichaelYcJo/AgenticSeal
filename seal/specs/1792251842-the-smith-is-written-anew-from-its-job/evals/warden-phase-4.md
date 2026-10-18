# warden — phase 4 non-inferiority

| Field | Value |
|---|---|
| Agent | warden |
| Phase | 4 |
| Baseline run | 2026-10-18T00:28:18.813Z 3cd4f2ae45df |
| New run | 2026-10-18T01:57:03.155Z f381cc81d7ed |
| Baseline suite | af9c924b7c5b03af5291017c226842655a8d83dd d8dfd549c0100c131019193b35655c59e7218282 |
| New suite | af9c924b7c5b03af5291017c226842655a8d83dd d8dfd549c0100c131019193b35655c59e7218282 |
| Baseline cut short | no |
| New cut short | no |
| Baseline report rows | 43 |
| Baseline false rows | 29 |
| New report rows | 39 |
| New false rows | 23 |
| Baseline spend USD | 42.2333 |
| New spend USD | 38.3511 |
| Baseline tokens read, every model | 81616964 |
| New tokens read, every model | 71473472 |
| Baseline tool calls | 936 |
| New tool calls | 872 |
| Baseline wall seconds | 8177.8 |
| New wall seconds | 6784.2 |
| Baseline preload bytes | 27198 |
| New preload bytes | 27198 |
| Baseline tokens per tool call | 87197.6 |
| New tokens per tool call | 81965.0 |
| Baseline tokens per true find | 5829783 |
| New tokens per true find | 4764898 |

## Graders

| Kind | Case | Grader | Old passed | Old runs | New passed | New runs |
|---|---|---|---|---|---|---|
| reach | warden replay-1791382684-r2 | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden replay-1791382684-r2 | shape-findings | 2 | 2 | 2 | 2 |
| shape | warden replay-1791382684-r2 | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden replay-1791382684-r2 | shape-words-only | 2 | 2 | 2 | 2 |
| truth | warden replay-1791382684-r2 | truth-1 | 1 | 2 | 0 | 2 |
| truth | warden replay-1791382684-r2 | truth-2 | 0 | 2 | 0 | 2 |
| truth | warden replay-1791382684-r2 | truth-3 | 0 | 2 | 1 | 2 |
| reach | warden replay-1791382684-r5 | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden replay-1791382684-r5 | shape-findings | 2 | 2 | 2 | 2 |
| shape | warden replay-1791382684-r5 | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden replay-1791382684-r5 | shape-words-only | 2 | 2 | 2 | 2 |
| truth | warden replay-1791382684-r5 | truth-2 | 0 | 2 | 0 | 2 |
| reach | warden replay-1791384160-r2 | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden replay-1791384160-r2 | shape-findings | 2 | 2 | 2 | 2 |
| shape | warden replay-1791384160-r2 | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden replay-1791384160-r2 | shape-words-only | 2 | 2 | 2 | 2 |
| truth | warden replay-1791384160-r2 | truth-1 | 2 | 2 | 2 | 2 |
| truth | warden replay-1791384160-r2 | truth-2 | 0 | 2 | 2 | 2 |
| reach | warden replay-1791779434-r5 | reach-warden | 2 | 2 | 2 | 2 |
| shape | warden replay-1791779434-r5 | shape-findings | 2 | 2 | 1 | 2 |
| shape | warden replay-1791779434-r5 | shape-report-exists | 2 | 2 | 2 | 2 |
| shape | warden replay-1791779434-r5 | shape-words-only | 2 | 2 | 2 | 2 |
| truth | warden replay-1791779434-r5 | truth-1 | 1 | 2 | 0 | 2 |
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
| agents/warden.md | 13d9b9ac81eefe60980ecb686a845c72eabdca8d612819379e138a2d7c47a41e |
| skills/agent-contract/SKILL.md | 9764cedd19617d9ba1af4d05a27384004456cf72c5333390c49cb7d57f7110dc |

Verdict: fail

- shape grader warden replay-1791779434-r5/shape-findings passed 1/2 on the new side, less often than the baseline's 2/2 (rule 3)
- the new preload is 27198 bytes, not below the baseline's 27198 (rule 4)
