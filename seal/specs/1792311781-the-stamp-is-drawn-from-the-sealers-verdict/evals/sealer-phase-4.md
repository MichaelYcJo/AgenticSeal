# sealer — phase 4 non-inferiority

| Field | Value |
|---|---|
| Agent | sealer |
| Phase | 4 |
| Baseline run | 2026-10-18T03:09:06.468Z 82e53421aa0d |
| New run | 2026-10-18T10:01:15.351Z 7b2ba04c112d |
| Baseline suite | 1483d8bae3c220242f0c87653bb9b8f87fdcec45 5c3e81195bb9d2319018e2f3abfd5aaf1d9e5447 |
| New suite | 981b0accef73b28456e844a69e1a6181a3165f06 5c3e81195bb9d2319018e2f3abfd5aaf1d9e5447 |
| Baseline cut short | no |
| New cut short | no |
| Baseline report rows | 0 |
| Baseline false rows | 0 |
| New report rows | 0 |
| New false rows | 0 |
| Baseline spend USD | 3.3898 |
| New spend USD | 3.5731 |
| Baseline tokens read, every model | 2855195 |
| New tokens read, every model | 3239330 |
| Baseline tool calls | 77 |
| New tool calls | 90 |
| Baseline wall seconds | 191.7 |
| New wall seconds | 452.0 |
| Baseline preload bytes | 24702 |
| New preload bytes | 24700 |
| Baseline tokens per tool call | 37080.5 |
| New tokens per tool call | 35992.6 |
| Baseline tokens per true find | 356899 |
| New tokens per true find | 404916 |

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
| agents/sealer.md | cae0d6366194e9f34fb801ecc684792d56ac2277ecac1c6947eeb57cd9fcc4f7 |
| skills/agent-contract/SKILL.md | 642b0da67c6795a1aa75ba16d0b17bac4e48639d05134bcdb050c34fcec6ee4e |

Verdict: pass

- every pass rule holds
