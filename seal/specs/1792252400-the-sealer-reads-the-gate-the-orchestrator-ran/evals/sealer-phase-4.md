# sealer — phase 4 non-inferiority

| Field | Value |
|---|---|
| Agent | sealer |
| Phase | 4 |
| Baseline run | 2026-10-17T16:14:02.233Z 6b70799d3df9 |
| New run | 2026-10-18T01:17:21.347Z 6ada776745e0 |
| Baseline suite | c2544c8f67e96a766d064d0c2b246c0d72326b6a 72c702939a50dab96a52afdc0d7f4f50b225d9ef |
| New suite | c2544c8f67e96a766d064d0c2b246c0d72326b6a 72c702939a50dab96a52afdc0d7f4f50b225d9ef |
| Baseline cut short | no |
| New cut short | no |
| Baseline report rows | 0 |
| Baseline false rows | 0 |
| New report rows | 0 |
| New false rows | 0 |
| Baseline spend USD | 3.1901 |
| New spend USD | 2.8036 |
| Baseline tokens read, every model | 3549090 |
| New tokens read, every model | 2303686 |
| Baseline tool calls | 100 |
| New tool calls | 69 |
| Baseline wall seconds | 577.9 |
| New wall seconds | 438.3 |
| Baseline preload bytes | 24652 |
| New preload bytes | 23792 |
| Baseline tokens per tool call | 35490.9 |
| New tokens per tool call | 33386.8 |
| Baseline tokens per true find | 1183030 |
| New tokens per true find | 383948 |

## Graders

| Kind | Case | Grader | Old passed | Old runs | New passed | New runs |
|---|---|---|---|---|---|---|
| reach | sealer rule-sealer-false-red | reach-sealer | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-commits-nothing | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-runs-no-broad-gate | 0 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-verdict | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-writes-only-the-guarantee-edit | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-writes-only-the-guarantee-write | 2 | 2 | 2 | 2 |
| truth | sealer rule-sealer-false-red | truth-false-red | 2 | 2 | 2 | 2 |
| reach | sealer rule-sealer-no-gate | reach-sealer | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-no-gate | shape-commits-nothing | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-no-gate | shape-runs-no-broad-gate | 0 | 2 | 2 | 2 |
| shape | sealer rule-sealer-no-gate | shape-verdict | 0 | 2 | 2 | 2 |
| shape | sealer rule-sealer-no-gate | shape-writes-only-the-guarantee-edit | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-no-gate | shape-writes-only-the-guarantee-write | 2 | 2 | 2 | 2 |
| truth | sealer rule-sealer-no-gate | truth-no-gate | 0 | 2 | 2 | 2 |
| reach | sealer rule-sealer-sound | reach-sealer | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sound | shape-commits-nothing | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sound | shape-runs-no-broad-gate | 0 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sound | shape-verdict | 1 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sound | shape-writes-only-the-guarantee-edit | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sound | shape-writes-only-the-guarantee-write | 2 | 2 | 2 | 2 |
| reach | sealer rule-sealer-untrue-body | reach-sealer | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-commits-nothing | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-runs-no-broad-gate | 0 | 2 | 2 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-verdict | 1 | 2 | 2 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-writes-only-the-guarantee-edit | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-writes-only-the-guarantee-write | 2 | 2 | 2 | 2 |
| truth | sealer rule-sealer-untrue-body | truth-untrue-body | 1 | 2 | 2 | 2 |

## New preload

| File | sha256 |
|---|---|
| agents/sealer.md | bf15099ab35038abfb7cd06d2bbde38099d30f9097ecf807d5e59ef7452e0207 |
| skills/agent-contract/SKILL.md | 642b0da67c6795a1aa75ba16d0b17bac4e48639d05134bcdb050c34fcec6ee4e |

Verdict: pass

- every pass rule holds
