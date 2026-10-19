# sealer — phase 3 non-inferiority

| Field | Value |
|---|---|
| Agent | sealer |
| Phase | 3 |
| Baseline run | 2026-10-19T00:16:46.093Z ddd1e8207689 |
| New run | 2026-10-19T04:16:48.957Z 6a143d1e342b |
| Baseline suite | 981b0accef73b28456e844a69e1a6181a3165f06 5c3e81195bb9d2319018e2f3abfd5aaf1d9e5447 |
| New suite | 981b0accef73b28456e844a69e1a6181a3165f06 5c3e81195bb9d2319018e2f3abfd5aaf1d9e5447 |
| Baseline cut short | no |
| New cut short | no |
| Baseline report rows | 0 |
| Baseline false rows | 0 |
| New report rows | 0 |
| New false rows | 0 |
| Baseline spend USD | 3.3379 |
| New spend USD | 3.2547 |
| Baseline tokens read, every model | 2883649 |
| New tokens read, every model | 2664594 |
| Baseline tool calls | 81 |
| New tool calls | 76 |
| Baseline wall seconds | 140.5 |
| New wall seconds | 324.9 |
| Baseline preload bytes | 24690 |
| New preload bytes | 24807 |
| Baseline tokens per tool call | 35600.6 |
| New tokens per tool call | 35060.4 |
| Baseline tokens per true find | 360456 |
| New tokens per true find | 333074 |

## Graders

| Kind | Case | Grader | Old passed | Old runs | New passed | New runs |
|---|---|---|---|---|---|---|
| reach | sealer rule-sealer-false-red | reach-sealer | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-commits-nothing | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-runs-no-broad-gate | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-verdict | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-writes-only-the-guarantee-edit | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-writes-only-the-guarantee-write | 2 | 2 | 2 | 2 |
| truth | sealer rule-sealer-false-red | truth-false-red | 2 | 2 | 2 | 2 |
| reach | sealer rule-sealer-no-gate | reach-sealer | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-no-gate | shape-commits-nothing | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-no-gate | shape-runs-no-broad-gate | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-no-gate | shape-verdict | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-no-gate | shape-writes-only-the-guarantee-edit | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-no-gate | shape-writes-only-the-guarantee-write | 2 | 2 | 2 | 2 |
| truth | sealer rule-sealer-no-gate | truth-no-gate | 2 | 2 | 2 | 2 |
| reach | sealer rule-sealer-sealed | reach-sealer | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sealed | shape-commits-nothing | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sealed | shape-runs-no-broad-gate | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sealed | shape-verdict | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sealed | shape-writes-only-the-guarantee-edit | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sealed | shape-writes-only-the-guarantee-write | 2 | 2 | 2 | 2 |
| reach | sealer rule-sealer-stale-gate | reach-sealer | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-stale-gate | shape-commits-nothing | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-stale-gate | shape-runs-no-broad-gate | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-stale-gate | shape-verdict | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-stale-gate | shape-writes-only-the-guarantee-edit | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-stale-gate | shape-writes-only-the-guarantee-write | 2 | 2 | 2 | 2 |
| truth | sealer rule-sealer-stale-gate | truth-stale-gate | 2 | 2 | 2 | 2 |
| reach | sealer rule-sealer-untrue-body | reach-sealer | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-commits-nothing | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-runs-no-broad-gate | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-verdict | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-writes-only-the-guarantee-edit | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-writes-only-the-guarantee-write | 2 | 2 | 2 | 2 |
| truth | sealer rule-sealer-untrue-body | truth-untrue-body | 2 | 2 | 2 | 2 |

## New preload

| File | sha256 |
|---|---|
| agents/sealer.md | 1a1c4ca32af1ca6f273ffb62c31cdb8001a3dc77600b986a9915a50dfe5d7ee8 |
| skills/agent-contract/SKILL.md | 642b0da67c6795a1aa75ba16d0b17bac4e48639d05134bcdb050c34fcec6ee4e |

Verdict: fail

- the new preload is 24807 bytes, not below the baseline's 24690 (rule 4)
