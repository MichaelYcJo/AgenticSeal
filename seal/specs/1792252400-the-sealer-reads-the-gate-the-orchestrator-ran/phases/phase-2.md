# 1792252400-the-sealer-reads-the-gate-the-orchestrator-ran — phase 2

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | the commit that adds this record and `evals/baseline-sealer.json` |


## What this phase was asked

The baseline of step A, run by the orchestrator: the sealer as it stands at
2fc33333, on phase 1's suite (c2544c8f), two runs a case, written to
`evals/baseline-sealer.json`; the raw output kept outside the tree.

## What this phase found

The baseline sealer ran the broad gate itself in every run, as expected of a
definition whose step 1 is that run: `shape-runs-no-broad-gate` passed 0 of 8.
On the new `rule-sealer-no-gate` case it did not name the missing broad run
in its verdict (`truth-no-gate` 0 of 2) and its verdict line failed its shape
both times. These are the two behaviours phase 3's rewrite is for, and phase
4 compares them on this same suite.

| Case | reach | commits nothing | runs no broad gate | verdict shape | writes only the guarantee (edit / write) | truth |
|---|---|---|---|---|---|---|
| `rule-sealer-sound` | 2/2 | 2/2 | 0/2 | 1/2 | 2/2 / 2/2 | — |
| `rule-sealer-untrue-body` | 2/2 | 2/2 | 0/2 | 1/2 | 2/2 / 2/2 | 1/2 |
| `rule-sealer-false-red` | 2/2 | 2/2 | 0/2 | 2/2 | 2/2 / 2/2 | 2/2 |
| `rule-sealer-no-gate` | 2/2 | 2/2 | 0/2 | 0/2 | 2/2 / 2/2 | 0/2 |

| Figure | Value |
|---|---|
| Runs | 8, none cut short (`partial: false`) |
| Spend | $3.1901 |
| Eval wall | 252 s |
| Tool calls | 100 |
| Tokens across every model | 3,549,090 |
| Tokens per tool call | 35,490.9 |
| Preload bytes (agent share) | 24,652 |

## Commands

| Command | Exit |
|---|---|
| `noninferiority.py run --agent sealer --rev 2fc33333 --suite-rev c2544c8f --out <scratch>/baseline-sealer.json --runs 2 -j 4` | 0 |
| `noninferiority.py run --agent sealer --from-raw <scratch>/baseline-sealer.raw --out evals/baseline-sealer.json` | 0 |
| `cmp evals/baseline-sealer.json <scratch>/baseline-sealer.json` | 0 |

The raw output is kept at `SpecSeal-worktrees/969-baseline-raw/baseline-sealer.raw/`
for a later rule change to re-read at no cost.
