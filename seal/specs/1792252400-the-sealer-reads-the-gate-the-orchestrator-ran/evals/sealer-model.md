# sealer — phase 4 non-inferiority

| Field | Value |
|---|---|
| Agent | sealer |
| Phase | 4 |
| Baseline run | 2026-10-18T01:17:21.347Z 6ada776745e0 |
| New run | 2026-10-18T01:19:51.027Z 2ffff3f1e708 |
| Baseline suite | c2544c8f67e96a766d064d0c2b246c0d72326b6a 72c702939a50dab96a52afdc0d7f4f50b225d9ef |
| New suite | c2544c8f67e96a766d064d0c2b246c0d72326b6a 72c702939a50dab96a52afdc0d7f4f50b225d9ef |
| Baseline cut short | no |
| New cut short | no |
| Baseline report rows | 0 |
| Baseline false rows | 0 |
| New report rows | 0 |
| New false rows | 0 |
| Baseline spend USD | 2.8036 |
| New spend USD | 1.4076 |
| Baseline tokens read, every model | 2303686 |
| New tokens read, every model | 1909566 |
| Baseline tool calls | 69 |
| New tool calls | 55 |
| Baseline wall seconds | 438.3 |
| New wall seconds | 252.4 |
| Baseline preload bytes | 23792 |
| New preload bytes | 23794 |
| Baseline tokens per tool call | 33386.8 |
| New tokens per tool call | 34719.4 |
| Baseline tokens per true find | 383948 |
| New tokens per true find | 318261 |

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
| reach | sealer rule-sealer-sound | reach-sealer | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sound | shape-commits-nothing | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sound | shape-runs-no-broad-gate | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sound | shape-verdict | 2 | 2 | 1 | 2 |
| shape | sealer rule-sealer-sound | shape-writes-only-the-guarantee-edit | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sound | shape-writes-only-the-guarantee-write | 2 | 2 | 2 | 2 |
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
| agents/sealer.md | d2ee55e727e2081c49de81aed54e6105b54243188bd82ce6ae5966724fac803c |
| skills/agent-contract/SKILL.md | 642b0da67c6795a1aa75ba16d0b17bac4e48639d05134bcdb050c34fcec6ee4e |

Verdict: fail

- shape grader sealer rule-sealer-sound/shape-verdict passed 1/2 on the new side, less often than the baseline's 2/2 (rule 3)
- the new preload is 23794 bytes, not below the baseline's 23792 (rule 4)
- the new side read 34719.4 tokens across every model per tool call (1909566 over 55), not below the baseline's 33386.8 (2303686 over 69) (rule 5)
