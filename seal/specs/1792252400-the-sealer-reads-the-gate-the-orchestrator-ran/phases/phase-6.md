# 1792252400-the-sealer-reads-the-gate-the-orchestrator-ran — phase 6

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

**Round 1 added a fifth case, `rule-sealer-stale-gate`, so the orchestrator
re-ran the reference on the five-case suite at 90fa7046** (round 1's fixes,
suite at the same commit). Every grader passed in both runs, 68 of 68: the
four cases above at 14, 14, 12 and 14 of their passes again, and the new
case 14 of 14, its truth `^Verdict:.*no broad run` included. That side
replaces the four-case side in `evals/reference-sealer.json`.

Round 2's step-1 fix (e15490c5) changed `agents/sealer.md`, so the
orchestrator re-ran the reference at 6f76b0b0 (round 2's fixes, the same
five-case suite: `suite_tree` 5c3e8119… at both commits). Every grader
passed again, 68 of 68. Round 3's fix (3e6d3896) changed the definition's
base paragraph once more, so the orchestrator re-ran it at 1483d8ba on the
same suite: 68 of 68 again, and that side is the one in
`evals/reference-sealer.json`.

| Figure | Four cases (b394e929) | Five cases (90fa7046) | Five cases (6f76b0b0) | Five cases (1483d8ba) |
|---|---|---|---|---|
| Runs / cut short | 8 / no | 10 / no | 10 / no | 10 / no |
| Spend USD | 2.9882 | 3.0973 | 3.3431 | 3.3898 |
| Session seconds | 395.1 | 423.1 | 295.4 | 191.7 |
| Tool calls | 76 | 73 | 77 | 77 |
| Tokens read, every model | 2,648,585 | 2,564,595 | 2,747,167 | 2,855,195 |
| Tokens per tool call | 34,849.8 | 35,131.4 | 35,677.5 | 37,080.5 |
| Preload bytes | 23,825 | 24,209 | 24,555 | 24,702 |
| Graders passed | 54 of 54 | 68 of 68 | 68 of 68 | 68 of 68 |

**The reference a later sealer change compares against** is the side at
1483d8ba: `suite_tree` 5c3e81195bb9d2319018e2f3abfd5aaf1d9e5447 at suite rev
1483d8bae3c220242f0c87653bb9b8f87fdcec45. A later change passes
`evals/reference-sealer.json` to `compare --old`.

**Spend.** The item's seven sides: 3.1901 + 2.8036 + 1.4076 + 2.9882 +
3.0973 + 3.3431 + 3.3898 = **20.2197 USD**, under the item's $40 (`questions.md` Q5's estimate was $17
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
| after round 1: `noninferiority.py run --agent sealer --rev 90fa7046 --suite-rev 90fa7046 --out $P2/reference-sealer.json --runs 2 -j 4 --max-cost-usd 10`, `$P2` the scratch `969-phase-6b/` | 0 |
| `cp -R $P2/reference-sealer.raw SpecSeal-worktrees/969-phase-6b-raw`, `diff -r`; `run --from-raw` into `$E/reference-sealer.json`, `cmp` | 0, 0, 0, 0 |
| after round 2: the same `run` at `--rev 6f76b0b0 --suite-rev 6f76b0b0 --max-cost-usd 6` into the scratch `969-phase-6c/`, then `cp -R` to `SpecSeal-worktrees/969-phase-6c-raw`, `diff -r`, `run --from-raw` into `$E/reference-sealer.json`, `cmp` | 0, 0, 0, 0, 0 |
| after round 3: the same at `--rev 1483d8ba --suite-rev 1483d8ba` through the scratch `969-phase-6d/` and `SpecSeal-worktrees/969-phase-6d-raw` | 0, 0, 0, 0, 0 |
