# Implementation Plan: rule 3 decides on the agent, not on one run (#966)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved <date> by <who>, when `smith` was spawned.

<!-- The line above is the record that the gate happened. Fill it in at the
spawn: reading this plan and spawning the builder IS the approval, so nothing
extra is being asked for here — only that the approval stop living in a
transcript. -->

## Summary

Rule 3 of `noninferiority.py#verdict` stops comparing each shape and reach
grader on its own. It compares the side's pooled shape and reach passes with
the baseline's, and it still fails, by name, any grader the new side failed
on every run where the baseline passed it at least once. Then #957's six
records are read again under the new rule from the committed side files,
with no paid run.

## Technical context

Coordinates are at 769f2aa4 (read).

- `evals/scripts/noninferiority.py:577-687`, `verdict`. Rule 3 is the loop
  at 657-669. Its first branch (a grader the baseline lacks, which must pass
  every new run) stays. Its `elif` branch (per-grader `np_ * oruns < op *
  nruns`) is what is replaced. Lines 615-627 already return `no result` for
  any grader run a different number of times on the two sides, unless it is
  a shape or reach grader with 0 runs on one side. So every grader that
  reaches the new totals has `oruns == nruns`.
- `evals/scripts/noninferiority.py:26-29` (module docstring) and `:586-587`
  (`verdict` docstring) state rule 3.
- `evals/scripts/noninferiority.py:918-945`, `cheaper_model`, has its own
  per-grader comparison and is out of scope (`spec.md` Scope, Out).
- `evals/README.md:32-33`, rule 3.
- `tests/test_a_rewritten_definition_proved_non_inferior.py:47-77` is the
  `numbers()` fixture, `:79-262` is `CASES`, and `:106-149` holds the rule 3
  cases. `test_the_verdict_is_recomputed_from_the_records_numbers` asserts
  the verdict alone. The reason assertions S2 and S3 ask for are a new
  test function, or a third element read by that test, as the builder
  judges.
- #957's inputs: `seal/specs/1792126889-every-agent-is-written-anew-from-its-job/evals/`,
  four `baseline-<agent>.json` and six `<name>.json`. Each holds
  `specseal.report_rows`, `cost` and `tool_calls` per run and
  `specseal.suite_tree` per side (read off `warden-phase-2.json`).
  `compare` needs nothing else.

**What breaks in six months.** A rewrite that gains on many easy graders
can hide a partial loss on one grader that matters, 1/2 where it was 2/2,
because only a loss on every run is named. That is the trade the owner
chose over more runs. A grader that matters enough to be judged alone is
a suite change, which #971 schedules after 0.22.2. The opposite edge also
stays: where the baseline passes every run, one run still decides
(`spec.md` Scope, the consequence paragraph).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **Shape and reach pooled into one total per side, plus the naming clause** | The six-month scenario above | **Chosen.** It is the decision's own wording, "a side's total shape and reach passes". It is also the figure the decision was made against: #957 phase 2's row "Shape and reach grader passes, of 36 graders × 2 runs \| 66 of 72 \| 70 of 72", and #966's "70 of 72 shape runs against the baseline's 66" |
| Separate totals for shape and for reach | A side that lost one reach run and gained one shape run fails. That is one run deciding again, which the decision removes. No #957 record tells the two apart (reach is equal on every side) | Rejected on the decision's wording. The reviewer can overturn it by reading #966's `## Decision`; S5 is the case that pins the choice |
| Compare rates instead of counts | None. The denominators are equal on both sides for every grader that reaches rule 3 (Technical context), so a rate and a count give the same verdict | Counts kept: they are what the record's table shows and what a reader adds up |
| Fold the graders the baseline lacks into the totals | A new grader passing every run offsets a common grader's loss, and the baseline's total has nothing to set against it | Rejected. S6 pins it. Under a fixed suite (#971) the case does not arise in 0.22.2 at all |
| Re-read through `run --from-raw` as the issue says | The raw output is gone (`spec.md` Scope, Out) | Replaced by `compare` over the committed side JSONs, which #957's sealer showed byte-identical to what `run --from-raw` writes |
| Rewrite #957's records in place with the new verdicts | #957's phase records would then quote verdicts their phases were never judged by | Rejected. New records go in this work item's `evals/` |
| `--runs 3`, or a per-grader tolerance of one run | — | The owner's decision (#966) rejected both. Not reopened |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **Rule 3 aggregates per agent.** Cases first: S1–S6 added and the two per-grader cases renamed (S7), each seen red as `spec.md` says, then `verdict`'s rule 3 rewritten to the total and the naming clause with the reason lines of *Data & interfaces*. The README, module and `verdict` docstrings, and the rule 3 case comments rewritten in place (S8) | Each new case seen red as its row says, then green; `bin/test tests/test_a_rewritten_definition_proved_non_inferior.py tests/test_evals_layout.py -q` exit 0; `git grep -n "at least as often" -- evals tests` output quoted in the phase record | |
| 2 | **#957 re-read, and the fragment.** `compare` for the six records into `evals/957-<name>.md` (no paid run, no `run`); the phase record's table of verdicts as recorded against as re-read, with the reasons; `changelog.md` written from this work item's two phases | Six `compare` exits 0; each new `## Graders` section diffed against #957's record, every diff empty; `check` on each new record, exit 0 for `pass` and 1 for `fail`, with no "it says … and its numbers give …" line; verdicts match `spec.md` S9's prediction, or the divergence goes to `overview.md` | |

This table is also where the work records how far it got. **Status is
empty, or the commit that closed the phase.**

What a phase discovers and the next phase needs goes to
`phases/phase-N.md` from `templates/sdd-phase.md`, when the phase closes.

## Operational impact

- No migration, no environment variable, no dependency.
- **Every later `compare` judges rule 3 the new way**, starting with #968's
  and #970's phases in 0.22.2.
- **`check` on a record written under the old rule can now disagree with
  it.** `check` recomputes the verdict with the code that runs it. On
  #957's `warden-phase-2.md` it will report "it says `fail` and its numbers
  give `pass`". Nothing in the tree runs `check` over committed records:
  `git grep` finds `check_record` only in the test module, on records it
  builds itself (read). A reader running it by hand meets this, and the
  `957-*.md` records of this work item are the ones written under the
  current rule.
