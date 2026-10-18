# 1792251842-the-smith-is-written-anew-from-its-job — phase 4

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | not closed: 668fd5f4 holds the three sides and their comparisons; the framer's side owes one re-run |

## What this phase was asked

The evaluation of the three agents at phase 3's commit (7053c184), run by
the orchestrator on the suite at af9c924b, two runs a case, each compared
with its phase-1 baseline. A `fail` is recorded as it reads; where its cause
is a sentence of `agents/smith.md`, `implement` or `writing-style`, the cause
is fixed once and that agent's set runs a second time; where its cause is
`agents/framer.md` it goes to #968. A side cut short is rerun once for a
named transient cause.

## What this phase found

| Figure | smith | warden | framer |
|---|---|---|---|
| Verdict (`evals/<a>-phase-4.md`) | **pass** | **fail** (rules 3 and 4) | **no result** (cut short) |
| Runs / cut short | 8 / no | 18 / no | 8 / 2 runs |
| Spend USD, baseline → phase 4 | 6.6210 → 5.6044 | 42.2333 → 38.3511 | 16.9055 → 16.5573 |
| Tool calls | 222 → 210 | 936 → 872 | 120 → 94 |
| Tokens per tool call | 43,068.0 → 36,389.4 | 87,197.6 → 81,965.0 | 27,296.7 → 37,916.5 |
| Preload bytes (agent share) | 90,728 → 26,664 | 27,198 → 27,198 | 89,444 → 86,421 |
| Truths found | — | 14 → 15 of 24 | — |
| Report rows / false rows | — | 43 / 29 → 39 / 23 | — |

**The smith passes on every rule.** Its preload fell by 70.6% and its tokens
per tool call by 15.5%, with every grader passing in all eight runs. Q6 (S3)
is answered from the traces: all 8 runs opened `skills/implement/SKILL.md`
and all 8 opened `skills/writing-style/SKILL.md` (a `tool_use` line naming
each path, counted per trace in `SpecSeal-worktrees/967-phase-4-raw/smith/traces`).

**The warden's `fail` is not caused by this item's files, so it is recorded
and not rerun.**

- Rule 4 fails by construction. This item does not touch `agents/warden.md`
  or the contract, so the warden's preload is the same 27,198 bytes and
  cannot be below the baseline's. The same holds for any item that leaves an
  agent's preload alone.
- Rule 3 fails on one grader: `replay-1791779434-r5/shape-findings`, 1 of 2
  against 2 of 2. In the failing run (trace `006.jsonl`) the warden wrote a
  round record whose `## Findings` holds no `### N.` finding at all, so the
  shape pattern, which asks for at least one finding, has nothing to match.
  The same run found neither of that case's truths. The run did open
  `skills/writing-style/SKILL.md`, the one file of this item the warden
  reads at a step: it read `## English prose rules` alone with one `awk`,
  as the new orientation line allows. The record it wrote has every section
  in its place, `## Findings` among them; what it lacks is a finding. That is
  a judgement about the case, and nothing in `writing-style` speaks to
  whether a finding exists. So the cause is not a sentence of this item's
  files, and a fix-and-rerun has nothing to fix. It is two runs' variance,
  the per-grader sample size #966 holds.
- On outcome the warden moved the right way: 15 truths against 14, 23 false
  rows against 29, 9.2% less spend and 6.0% fewer tokens per tool call.

**The framer's side has no result.** Two runs of `rule-framer-word-count`
ended with `exit 1: You've hit your session limit` (the account's usage
limit, reached at about 11:35 KST). The other six runs passed every grader.
That is a named transient cause, so the plan allows one re-run. Its cost,
about $17 at this side's spend, is over what remained of the night's $200
budget, so the re-run waits for the owner's word. Until then Q7 (the
framer's rule 5) stays open: the six runs that finished read 37,916.5
tokens per call against 27,296.7, which repeats #957's framer reading, but a
cut side is no result.

**Spend for this phase (eval `costUsd`):** smith 5.6044, warden 38.3511,
framer 16.5573, **60.5128 in all**.

## Commands

`$S` is the session scratch directory's `967-phase-4/`, `$K` is
`SpecSeal-worktrees/967-phase-4-raw/`, `$E` is this work item's `evals/`.

| Command | Exit |
|---|---|
| `noninferiority.py run --agent <a> --rev 7053c184 --suite-rev af9c924b --out $S/<a>-phase-4.json --runs 2 -j 4 --max-cost-usd <cap>` for smith (12), warden (55), framer (25), each started only while its cap fit the budget left | 0, 0, 0 |
| `cp -R $S/<a>-phase-4.raw $K/<a>`; `run --agent <a> --from-raw $K/<a> --out $E/<a>-phase-4.json`; `cmp` against the scratch copy, each agent | 0 each |
| `compare --agent <a> --phase 4 --old $E/baseline-<a>.json --new $E/<a>-phase-4.json --out $E/<a>-phase-4.md`, each agent | 0 each |
| the failing warden trace read for its round-5 writes and its `writing-style` reads (`$K/warden/traces/006.jsonl`) | 0 |
| the smith traces read for `implement` and `writing-style` opens | 0 |
