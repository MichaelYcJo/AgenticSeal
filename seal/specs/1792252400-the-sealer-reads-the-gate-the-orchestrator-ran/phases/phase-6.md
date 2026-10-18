# 1792252400-the-sealer-reads-the-gate-the-orchestrator-ran — phase 6

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 6 |
| Commit | the commit that adds this record and `evals/reference-sealer.json` |

## What this phase was asked

The reference, run by the orchestrator: the sealer at b394e929 (phase 5's
words, plus the encoding fix to T7's test) on the suite at the same commit,
on the model phase 4 decided (Opus), two runs a case, written to
`evals/reference-sealer.json`. No `compare`: the suites differ from phase
4's by design (`spec.md` S10). The check is every grader's passed count at
least phase 4's on the same model, read from the two sides.

## What this phase found

**Every grader passed in both runs, 54 of 54, as in phase 4.** The table
reads phase 5's case `rule-sealer-sealed` as phase 4's `rule-sealer-sound`:
phase 5 renamed the case with its verdict word, and its graders are the
same six.

| Case (phase 4 name → phase 6 name) | Graders | Phase 4 passed | Phase 6 passed |
|---|---|---|---|
| `rule-sealer-false-red` | 7 | 14 of 14 | 14 of 14 |
| `rule-sealer-no-gate` | 7 | 14 of 14 | 14 of 14 |
| `rule-sealer-sound` → `rule-sealer-sealed` | 6 | 12 of 12 | 12 of 12 |
| `rule-sealer-untrue-body` | 7 | 14 of 14 | 14 of 14 |

| Figure | Phase 4 (5ca68b5d, suite c2544c8f) | Phase 6 (b394e929, suite b394e929) |
|---|---|---|
| Runs / cut short | 8 / no | 8 / no |
| Spend USD | 2.8036 | 2.9882 |
| Session seconds | 438.3 | 395.1 |
| Tool calls | 69 | 76 |
| Tokens read, every model | 2,303,686 | 2,648,585 |
| Tokens per tool call | 33,386.8 | 34,849.8 |
| Preload bytes | 23,792 | 23,825 |

The cost figures are recorded, not judged: the two sides ran different
suites.

**The reference a later sealer change compares against** is this side:
`suite_tree` b46fd08b364a0320268249cbef7c06ed4533f315 at suite rev
b394e929b414dcf0520b7d365e5e3fd56e4c764d. A later change passes
`evals/reference-sealer.json` to `compare --old`.

**Round 1 adds a fifth case, `rule-sealer-stale-gate`, so the reference is
re-run on the five-case suite after round 1**; the orchestrator writes its
figures here, and until then the side above measured four cases.

**Spend.** The item's four sides: 3.1901 + 2.8036 + 1.4076 + 2.9882 =
**10.3895 USD**, under the item's $40 (`questions.md` Q5's estimate was $17
to $22).

## Commands

`$P` is the session scratch directory's `969-phase-6/`, `$K` is
`SpecSeal-worktrees/969-phase-6-raw/`, `$E` is this work item's `evals/`.

| Command | Exit |
|---|---|
| `git diff --stat 284b3597 b394e929 -- evals/behaviour` | 0, empty |
| `noninferiority.py run --agent sealer --rev b394e929 --suite-rev b394e929 --out $P/reference-sealer.json --runs 2 -j 4 --max-cost-usd 10` | 0 |
| `cp -R $P/reference-sealer.raw $K`, `diff -r` | 0, 0 |
| `run --agent sealer --from-raw $K --out $E/reference-sealer.json`, `cmp` against the scratch copy | 0, 0 |
