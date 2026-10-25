# 1792251842-the-smith-is-written-anew-from-its-job — phase 4

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | the commit that adds this record and the three sides it names |

## What this phase was asked

The evaluation of the three agents, run by the orchestrator on the suite at
af9c924b, two runs a case, each compared with its phase-1 baseline at
2fc33333. A `fail` is recorded as it reads; where its cause is a sentence of
`agents/smith.md`, `implement` or `writing-style`, the cause is fixed once
and that agent's set runs a second time; where its cause is
`agents/framer.md` it goes to #968. A side cut short is rerun once for a
named transient cause.

## Two takes, and why the second is the record

**The first take, at 7053c184 (records 668fd5f4 and a3bf3832), is history.**
smith passed; warden failed on rule 4 (its preload unchanged, by
construction) and on one two-run grader; the framer's side was cut short by
the account's usage limit in two runs. Before its re-run was taken, #969
merged into `release/v0.22.1` (4a6e24f6) and changed contract §2, which all
three agents preload, one sentence of `agents/warden.md`, and
`docs/the-review-record.md`, `skills/code-review/scripts/chain_check.py` and
`agents/sealer.md`, which the warden reads in the evaluated tree. Under the
milestone's rolling baseline an agent whose read set changed is measured
again, so the three sides were taken again on the merged tree, and the
framer's re-run is one of them.

**The second take, at af716289** (this branch with release merged in at
16e8d4c8, plus two test fixes that no agent reads), is the record:
`evals/<agent>-phase-4.json` and `.md`. The baselines stay those of phase 1
at 2fc33333 (the orchestrator's decision, 2026-10-18): re-taking them on the
merged tree would cost about $60 more, so the comparison below includes
#969's changes named above as well as this item's, and says so.

## What this phase found

| Figure, 2fc33333 → af716289 | smith | warden | framer |
|---|---|---|---|
| Verdict (`evals/<a>-phase-4.md`) | **pass** | **fail**, rule 5 alone | **fail**, rule 5 alone |
| Runs / cut short | 8 / no | 18 / no | 8 / no |
| Preload bytes (agent share) | 90,728 → 26,596 (−70.7%) | 27,198 → 27,173 | 89,444 → 86,353 |
| Tokens per tool call | 43,068.0 → 35,993.1 (−16.4%) | 87,197.6 → 87,862.4 (+0.8%) | 27,296.7 → 29,894.6 (+9.5%) |
| Tokens read, all models | — | — | 3,275,602 → 3,258,508 (−0.5%) |
| Tool calls | 222 → 204 | 936 → 940 | 120 → 109 |
| Spend USD | 6.6210 → 5.3675 (−18.9%) | 42.2333 → 41.7424 (−1.2%) | 16.9055 → 16.1196 (−4.6%) |
| Graders passed | 48 → 48 of 48 | 86 → 91 of 96 | 64 → 64 of 64 |
| Truths found | — | 14 → 19 of 24 | — |
| Report rows / false rows | — | 43 / 29 → 43 / 24 | — |

**The smith passes on every rule.** It preloads 70.7% less and reads 16.4%
fewer tokens per tool call, with every grader passing in all eight runs. In
the first take all 8 runs opened `skills/implement/SKILL.md` and all 8
opened `skills/writing-style/SKILL.md` (Q6).

**The warden's `fail` is rule 5 by 0.8%, and its outcome rose.** It found
19 of 24 truths against 14, with 24 false rows against 29; every shape
and reach grader passed on both sides (72 of 72), so the 91 of 96 against
86 is the five more truths. Rule 4 now passes, since
#969's §2 is shorter. The 0.8% is not traced to a sentence of this item's
files: the same `writing-style` text read at 7053c184 gave 81,965.0 tokens
per call, 6.0% below the baseline, and every file the warden reads that
differs between the two takes is #969's: contract §2, one sentence of
`agents/warden.md`, `docs/the-review-record.md` and
`skills/code-review/scripts/chain_check.py` (each named at the evaluated
tree's path in 17 or 18 of each take's 18 runs) and `agents/sealer.md` (in
2 and 1). `skills/code-review/orchestration.md` is named in 6 runs of each
take, every time as the reviewed fixture's own copy rather than the
plugin's. Two takes 6.8 points apart is the run-to-run spread #966 holds,
so the fail is recorded as it reads and nothing is rerun. All 18 runs
opened `writing-style` at their record step.

**The framer's `fail` is rule 5, and it goes to #968 (decision 5).** Its
total tokens fell 0.5% and its spend 4.6%, with every grader passing, but it
made 11 fewer tool calls, so tokens per call rose 9.5%: fewer calls on a
smaller read. It preloads `implement` and `writing-style`, both rewritten
here, so all eight runs read both at startup and no count of opens clears
them; no sentence of this item's files is identified as the cause. The
fail is recorded as it reads and carried to #968, which measures the framer
on a tree carrying this item.

**Spend for this phase (eval `costUsd`):** the first take 60.5128 (smith
5.6044, warden 38.3511, framer 16.5573, two framer runs of it cut short);
the second take 63.2295 (smith 5.3675, warden 41.7424, framer 16.1196);
**123.7423 in all**.

**The smith's side was taken again after round 1.** Round 1's fixes changed
`agents/smith.md` at a72d5b53, after the take measured above, so the
orchestrator re-ran the smith's side at 28d6a453 on the same suite. It is
the side in `evals/smith-phase-4.json` and `.md` now: **pass**, every rule.

| Figure, 2fc33333 → 28d6a453 | smith |
|---|---|
| Runs / cut short | 8 / no |
| Preload bytes (agent share) | 90,728 → 26,879 (−70.4%) |
| Tokens per tool call | 43,068.0 → 35,691.6 (−17.1%) |
| Tool calls | 222 → 212 |
| Spend USD | 6.6210 → 5.4509 (−17.7%) |
| Graders passed | 48 → 48 of 48 |

All 8 runs opened `skills/implement/SKILL.md` and all 8 opened
`skills/writing-style/SKILL.md` (a `tool_use` line naming each path, per
trace in `SpecSeal-worktrees/967-phase-4c-raw/smith/traces`). The
phase's spend becomes **129.1932** with this side's 5.4509.

## Commands

`$S` is the session scratch directory's `967-phase-4b/`, `$K` is
`SpecSeal-worktrees/967-phase-4b-raw/`, `$E` is this work item's `evals/`.
The first take's commands are the same with `967-phase-4/`, rev 7053c184.

| Command | Exit |
|---|---|
| `noninferiority.py run --agent <a> --rev af716289 --suite-rev af9c924b --out $S/<a>-phase-4.json --runs 2 -j 4 --max-cost-usd <cap>` for smith (12), warden (55), framer (25) | 0, 0, 0 |
| `cp -R $S/<a>-phase-4.raw $K/<a>`, `diff -r`; `run --agent <a> --from-raw $K/<a> --out $E/<a>-phase-4.json`; `cmp` against the scratch copy, each agent | 0 each |
| `compare --agent <a> --phase 4 --old $E/baseline-<a>.json --new $E/<a>-phase-4.json --out $E/<a>-phase-4.md`, each agent | 0 each |
| the warden's and the framer's traces read for `writing-style` opens | 0 |
| after round 1: `run --agent smith --rev 28d6a453 --suite-rev af9c924b --runs 2 -j 4 --max-cost-usd 12` through the scratch `967-phase-4c/` and `SpecSeal-worktrees/967-phase-4c-raw/smith`, then `diff -r`, `--from-raw`, `cmp`, `compare` | 0, 0, 0, 0, 0 |
| the warden's traces of both takes read for each file `git diff --name-only 7053c184 af716289` lists, at the evaluated tree's path and at the reviewed fixture's (round 1's fix pass) | 0 |
