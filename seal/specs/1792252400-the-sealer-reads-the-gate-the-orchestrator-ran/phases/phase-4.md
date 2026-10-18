# 1792252400-the-sealer-reads-the-gate-the-orchestrator-ran — phase 4

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | the commit that adds this record and the four files under `evals/` it names |

## What this phase was asked

The proof and the model, run by the orchestrator with the lid open: the
sealer at 5ca68b5d (phase 3 closed, T7 built, the contract's §2 target
repointed) on phase 1's suite (c2544c8f) against `evals/baseline-sealer.json`;
then a copy of the same tree with `agents/sealer.md`'s `model: sonnet`
against the Opus side; `noninferiority.py model` on the second record.

## What this phase found

**The rewritten sealer passes against the baseline (`evals/sealer-phase-4.md`,
`Verdict: pass`).** Every grader of every case passed in both runs, 54 of 54.
The baseline passed 39 of 54. The behaviours phase 3 was for moved as the
spec asked:

| Grader | Baseline (2fc33333) | Phase 4 (5ca68b5d, Opus) |
|---|---|---|
| `shape-runs-no-broad-gate`, four cases | 0 of 8 | 8 of 8 |
| `truth-no-gate` (`rule-sealer-no-gate`) | 0 of 2 | 2 of 2 |
| `shape-verdict`, four cases | 4 of 8 | 8 of 8 |
| `truth-untrue-body` | 1 of 2 | 2 of 2 |

| Figure | Baseline | Phase 4, Opus | Phase 4, Sonnet copy |
|---|---|---|---|
| Runs / cut short | 8 / no | 8 / no | 8 / no |
| Spend USD | 3.1901 | 2.8036 | 1.4076 |
| Tokens read, every model | 3,549,090 | 2,303,686 | 1,909,566 |
| Tool calls | 100 | 69 | 55 |
| Tokens per tool call | 35,490.9 | 33,386.8 | 34,719.4 |
| Preload bytes | 24,652 | 23,792 | 23,794 |
| Session seconds | 577.9 | 438.3 | 252.4 |
| Graders passed | 39 of 54 | 54 of 54 | 53 of 54 |

**The model stays Opus (`evals/sealer-model.md`).** `noninferiority.py model`
printed `opus`, exit 0, with the reason `shape grader sealer
rule-sealer-sound/shape-verdict passed 1/2 on Sonnet, 2/2 on Opus`. The
Sonnet side cost half as much and lost one verdict line's shape, which is
the line `chain_check.py` reads at a ready pull request. The record's own
verdict is `fail` (rule 3 on that grader; rule 4 by construction, the
`model:` line two bytes longer; rule 5, 34,719.4 against 33,386.8 tokens per
call), and `check` exits 1 on it as on any record that reads `fail`. The
decision is `model`'s, which reads the graders and the spend and not the
record's verdict (phase 3's T7 note). `agents/sealer.md` keeps `model: opus`
and the README rows are unchanged.

**Questions the traces answered.**

- Q3: the sandbox's interpreter refusal (`blocked by sandbox`) appears in 6 of
  the Opus side's 8 traces, and every run reached its verdict with every
  grader passing, so the re-run works round it as the baseline's did.
- Q4: the Sonnet side's traces hold 79 assistant events, all naming
  `claude-sonnet-5-5`: 60 are the sealer's (each with a `parent_tool_use_id`)
  and 19 the case session's, which runs on Sonnet by `case.yaml`. The Opus
  side's 73 sealer events all name `claude-opus-5-5`, beside 17 session
  events on Sonnet. So `run --tree` honoured the copy's `model: sonnet`.
  Recounted after round 1, which found the 90 first written here to be the
  Opus side's total: every `traces/*.jsonl` line parsed as JSON, kept where
  `type` is `assistant`, and counted by `message.model` and by whether
  `parent_tool_use_id` is set.
- Q5: the item's sides so far cost 3.1901 + 2.8036 + 1.4076 = 7.4013 USD;
  phase 6's reference side is the fourth.

## Commands

`$P` is the session scratch directory's `969-phase-4/`, `$K` is
`SpecSeal-worktrees/969-phase-4-raw/`, `$E` is this work item's `evals/`.

| Command | Exit |
|---|---|
| `noninferiority.py run --agent sealer --rev 5ca68b5d --suite-rev c2544c8f --out $P/sealer-phase-4.json --runs 2 -j 4 --max-cost-usd 10` | 0 |
| `git archive 5ca68b5d` into `$P/sonnet-tree`, `model: opus` → `model: sonnet` in its `agents/sealer.md`, `diff` against `git show 5ca68b5d:agents/sealer.md` showing that line alone | 0, 1 |
| `noninferiority.py run --agent sealer --tree $P/sonnet-tree --suite-rev c2544c8f --out $P/sealer-sonnet-phase-4.json --runs 2 -j 4 --max-cost-usd 10` | 0 |
| `cp -R` each raw directory to `$K`, `diff -r` | 0, 0 |
| `run --agent sealer --from-raw $K/<side> --out $E/<side>.json`, then `cmp` against the scratch copy, both sides | 0, 0 each |
| `compare --agent sealer --phase 4 --old $E/baseline-sealer.json --new $E/sealer-phase-4.json --out $E/sealer-phase-4.md` | 0 |
| `compare --agent sealer --phase 4 --old $E/sealer-phase-4.json --new $E/sealer-sonnet-phase-4.json --out $E/sealer-model.md` | 0 |
| `check $E/sealer-phase-4.md` | 0 |
| `check $E/sealer-model.md` | 1, the record reads `fail` |
| `model $E/sealer-model.md` | 0, `opus` |
| After round 1 (finding 7): `run --agent sealer --from-raw $K/sealer-sonnet-phase-4 --out $E/sealer-sonnet-phase-4.json`, whose `rev` now reads `tree`, then the `compare` for `sealer-model.md` above, `check` on both records and `model` | 0; 0; 0 and 1; 0, `opus` |

The raw output is kept at `SpecSeal-worktrees/969-phase-4-raw/` for a later
rule change to re-read at no cost.
