# sealer — phase 3 non-inferiority

| Field | Value |
|---|---|
| Agent | sealer |
| Phase | 3 |
| Baseline run | 2026-10-17T00:58:30.850Z e041f34ad0dd |
| New run | 2026-10-17T13:25:30.124Z df7eda63c330 |
| Baseline suite | af9c924b7c5b03af5291017c226842655a8d83dd 2ef872f0f7b86292bf8e84bd0e6978dc3301ac3b |
| New suite | af9c924b7c5b03af5291017c226842655a8d83dd 2ef872f0f7b86292bf8e84bd0e6978dc3301ac3b |
| Baseline cut short | no |
| New cut short | no |
| Baseline report rows | 0 |
| Baseline false rows | 0 |
| New report rows | 0 |
| New false rows | 0 |
| Baseline spend USD | 3.0366 |
| New spend USD | 4.0836 |
| Baseline tokens read, every model | 3324087 |
| New tokens read, every model | 3096365 |
| Baseline tool calls | 97 |
| New tool calls | 84 |
| Baseline wall seconds | 577.2 |
| New wall seconds | 578.6 |
| Baseline preload bytes | 28358 |
| New preload bytes | 24527 |
| Baseline tokens per tool call | 34268.9 |
| New tokens per tool call | 36861.5 |
| Baseline tokens per true find | 831022 |
| New tokens per true find | 1032122 |

## Graders

| Kind | Case | Grader | Old passed | Old runs | New passed | New runs |
|---|---|---|---|---|---|---|
| reach | sealer rule-sealer-false-red | reach-sealer | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-commits-nothing | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-verdict | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-writes-only-the-guarantee-edit | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-writes-only-the-guarantee-write | 2 | 2 | 2 | 2 |
| truth | sealer rule-sealer-false-red | truth-false-red | 2 | 2 | 2 | 2 |
| reach | sealer rule-sealer-sound | reach-sealer | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sound | shape-commits-nothing | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sound | shape-verdict | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sound | shape-writes-only-the-guarantee-edit | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sound | shape-writes-only-the-guarantee-write | 2 | 2 | 2 | 2 |
| reach | sealer rule-sealer-untrue-body | reach-sealer | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-commits-nothing | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-verdict | 2 | 2 | 1 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-writes-only-the-guarantee-edit | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-writes-only-the-guarantee-write | 2 | 2 | 2 | 2 |
| truth | sealer rule-sealer-untrue-body | truth-untrue-body | 2 | 2 | 1 | 2 |

## New preload

| File | sha256 |
|---|---|
| agents/sealer.md | cf8afe40eba6eac3caabd9821a8ec4372bbd46bb6295f49436aec5b28dff101d |
| skills/agent-contract/SKILL.md | e4f679e31c041d4f7934367a9ce3bd826cf68af03e9e5319e84b3a8d327e34b3 |

Verdict: fail

- shape grader sealer rule-sealer-untrue-body/shape-verdict passed 1/2 on the new side, less often than the baseline's 2/2 (rule 3)
- the new side read 36861.5 tokens across every model per tool call (3096365 over 84), not below the baseline's 34268.9 (3324087 over 97) (rule 5)
