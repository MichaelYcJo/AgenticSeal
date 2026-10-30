# sealer — phase 8 non-inferiority

| Field | Value |
|---|---|
| Agent | sealer |
| Phase | 8 |
| Baseline run | 2026-10-30T01:33:46.270Z 12cc790fcb89 |
| New run | 2026-10-30T01:36:45.088Z b61eb5eb1ec4 |
| Baseline suite | 769a1413c5877f6d5755eae18c8f54bffc8bae5e dbdd2080619fe82173a6ba7305064c55849db2dd |
| New suite | 769a1413c5877f6d5755eae18c8f54bffc8bae5e dbdd2080619fe82173a6ba7305064c55849db2dd |
| Baseline cut short | no |
| New cut short | no |
| Baseline report rows | 0 |
| Baseline false rows | 0 |
| New report rows | 0 |
| New false rows | 0 |
| Baseline spend USD | 3.1919 |
| New spend USD | 3.2614 |
| Baseline tokens read, every model | 2943469 |
| New tokens read, every model | 3255891 |
| Baseline tool calls | 79 |
| New tool calls | 85 |
| Baseline wall seconds | 195.4 |
| New wall seconds | 99.4 |
| Baseline preload bytes | 28269 |
| New preload bytes | 28221 |
| Baseline tokens per tool call | 37259.1 |
| New tokens per tool call | 38304.6 |
| Baseline tokens per true find | 367934 |
| New tokens per true find | 406986 |

## Graders

| Kind | Case | Grader | Old passed | Old runs | New passed | New runs |
|---|---|---|---|---|---|---|
| reach | sealer rule-sealer-false-red | reach-sealer | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-commits-nothing | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-runs-no-broad-run | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-verdict | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-writes-only-the-guarantee-edit | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-false-red | shape-writes-only-the-guarantee-write | 2 | 2 | 2 | 2 |
| truth | sealer rule-sealer-false-red | truth-false-red | 2 | 2 | 2 | 2 |
| reach | sealer rule-sealer-no-gate | reach-sealer | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-no-gate | shape-commits-nothing | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-no-gate | shape-runs-no-broad-run | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-no-gate | shape-verdict | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-no-gate | shape-writes-only-the-guarantee-edit | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-no-gate | shape-writes-only-the-guarantee-write | 2 | 2 | 2 | 2 |
| truth | sealer rule-sealer-no-gate | truth-no-gate | 2 | 2 | 2 | 2 |
| reach | sealer rule-sealer-sealed | reach-sealer | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sealed | shape-commits-nothing | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sealed | shape-runs-no-broad-run | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sealed | shape-verdict | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sealed | shape-writes-only-the-guarantee-edit | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-sealed | shape-writes-only-the-guarantee-write | 2 | 2 | 2 | 2 |
| reach | sealer rule-sealer-stale-gate | reach-sealer | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-stale-gate | shape-commits-nothing | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-stale-gate | shape-runs-no-broad-run | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-stale-gate | shape-verdict | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-stale-gate | shape-writes-only-the-guarantee-edit | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-stale-gate | shape-writes-only-the-guarantee-write | 2 | 2 | 2 | 2 |
| truth | sealer rule-sealer-stale-gate | truth-stale-gate | 2 | 2 | 2 | 2 |
| reach | sealer rule-sealer-untrue-body | reach-sealer | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-commits-nothing | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-runs-no-broad-run | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-verdict | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-writes-only-the-guarantee-edit | 2 | 2 | 2 | 2 |
| shape | sealer rule-sealer-untrue-body | shape-writes-only-the-guarantee-write | 2 | 2 | 2 | 2 |
| truth | sealer rule-sealer-untrue-body | truth-untrue-body | 2 | 2 | 2 | 2 |

## New preload

| File | sha256 |
|---|---|
| agents/sealer.md | 01cdf6433f99ac13f433e1556682f2eed502081e1c5ff5b0fda9706393bcbe5a |
| skills/agent-contract/SKILL.md | 0c4ef4aac455941006677e1e92f08e3f048809a08de87e75966a2be82ad4a645 |
| skills/core/SKILL.md | ad7d05bb47d1f0dd9d3675edd4c84bae54f0a2c3c4a5ee6228349a839c30127b |

Verdict: pass

- every pass rule holds
