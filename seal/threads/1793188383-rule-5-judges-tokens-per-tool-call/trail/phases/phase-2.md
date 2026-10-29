# Phase 2: 1793188383-rule-5-judges-tokens-per-tool-call

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | ca55a8f1 |

## What this phase was asked

Run `noninferiority.py check` on each of the 17 records of `frame/design.md`
*Data & interfaces* at phase 1's commit, with no paid run. Write the table
that *Data & interfaces* describes into this record, with phase 1's base
column beside it. A verdict that differs from S9's prediction goes to
`gaps.md` as a divergence. Write `changelog.md` from both phases. Q2's
default, rule 5 alone, sends the section on rules 1 and 2 to `gaps.md` *Not
done*, citing Q2.

## What this phase found

**S9's prediction holds on all 17 records (executed).** Each record was
read from the scratch copy phase 1 made with `git show`, by `python3
evals/scripts/noninferiority.py check <record>` with the code of
`c6e47cfe`, and each exit code was read directly. `git diff --quiet c6e47cfe
HEAD -- evals` exited 0 before the runs, so the code that ran is phase 1's.
Rule 5 now fails `957-framer-p3` alone. The verdict of `967-framer-p4`,
`967-warden-p4` and `943-sealer-p3b` turns from `fail` to `pass`. No other
record's verdict moves.

The base columns are phase 1's runs at `cf8127eb`. "Rule 5 line" is the
line `check` printed for rule 5, or `none` where rule 5 passed.

| Name | Record | Recorded | Base exit | Base verdict | Base rule 5 line | After exit | After verdict | After rule 5 line |
|---|---|---|---|---|---|---|---|---|
| 957-framer-p3 | `2fc33333:seal/specs/1792126889-every-agent-is-written-anew-from-its-job/evals/framer-phase-3.md` | fail | 1 | fail | 33595.1 a call (4736908 over 141), not below 28253.1 (3164345 over 112) | 1 | fail | the new side read 4736908 tokens across every model over 141 tool calls, 33595.1 a call, against the baseline's 3164345 over 112, 28253.1 a call: the total and the figure per call both rose by more than 7% (rule 5) |
| 957-sealer-p3 | the same directory, `sealer-phase-3.md` | fail | 1 | fail, rules 3 and 5 | 36861.5 a call (3096365 over 84), not below 34268.9 (3324087 over 97) | 1 | fail, rule 3 | none |
| 957-smith-p3 | the same directory, `smith-phase-3.md` | pass | 0 | pass | none | 0 | pass | none |
| 957-warden-p2-run-1 | the same directory, `warden-phase-2-run-1.md` | fail | 1 | fail, rule 3 | none | 1 | fail, rule 3 | none |
| 957-warden-p2 | the same directory, `warden-phase-2.md` | fail | 1 | pass | none | 1 | pass | none |
| 957-warden-p3 | the same directory, `warden-phase-3.md` | pass | 0 | pass | none | 0 | pass | none |
| 967-framer-p4 | `f6ae6db6:seal/specs/1792251842-the-smith-is-written-anew-from-its-job/evals/framer-phase-4.md` | fail | 1 | fail | 29894.6 a call (3258508 over 109), not below 27296.7 (3275602 over 120) | 1 | pass | none |
| 967-smith-p4 | the same directory, `smith-phase-4.md` | pass | 0 | pass | none | 0 | pass | none |
| 967-warden-p4 | the same directory, `warden-phase-4.md` | fail | 1 | fail | 87862.4 a call (82590654 over 940), not below 87197.6 (81616964 over 936) | 1 | pass | none |
| 969-sealer-p4 | `4a6e24f6:seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/evals/sealer-phase-4.md` | pass | 0 | pass | none | 0 | pass | none |
| 969-sealer-model | the same directory, `sealer-model.md` | fail | 1 | fail, rules 3, 4 and 5 | 34719.4 a call (1909566 over 55), not below 33386.8 (2303686 over 69) | 1 | fail, rules 3 and 4 | none |
| 975-sealer-p4 | `f1c9932d:seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/evals/sealer-phase-4.md` | pass | 0 | pass | none | 0 | pass | none |
| 976-sealer-p5 | `75502328:seal/specs/1792363231-a-local-mode-work-item-draws-no-stamp/evals/sealer-phase-5.md` | pass | 0 | pass | none | 0 | pass | none |
| 943-sealer-p3 | `b196fe9b:seal/specs/1792367880-ci-runs-once-when-the-pull-request-opens/evals/sealer-phase-3.md` | fail | 1 | fail, rule 4 | none | 1 | fail, rule 4 | none |
| 943-sealer-p3b | the same directory, `sealer-phase-3b.md` | fail | 1 | fail | 35906.3 a call (2585256 over 72), not below 35600.6 (2883649 over 81) | 1 | pass | none |
| 968-framer-p2 | `a1909096:seal/specs/1792368014-the-framer-is-written-anew-from-its-job/evals/framer-phase-2.md` | pass | 0 | pass | none | 0 | pass | none |
| 985-warden-p3 | `2ff7b963:seal/specs/1792368015-every-finding-carries-an-evidence-line/evals/warden-phase-3.md` | fail | 1 | fail, rules 1 and 2 | none | 1 | fail, rules 1 and 2 | none |

The base rule 5 lines are shortened to their figures here. Phase 1's record
quotes each in full. A "fail" with no rule named failed on rule 5 alone.

**Where the recorded verdict and the computed one differ, `check` exits 1
whatever it computed (executed).** On `967-framer-p4`, `967-warden-p4` and
`943-sealer-p3b` after the change, and on `957-warden-p2` at the base and
after, `check` printed "it says `fail` and its numbers give `pass`" and
exited 1. `frame/plan.md`'s phase 2 *Verified by* cell expects 0 for `pass`
and 1 for `fail`, so the computed verdict here is read from the printed
line. `gaps.md` holds this as a divergence of the plan's cell. It is not a
divergence of S9, whose verdicts all hold.

**What the records still fail on (executed).** Five records keep a `fail`
from another rule, as `frame/design.md` *Data & interfaces* reads them:
`957-sealer-p3` and `957-warden-p2-run-1` on rule 3, `969-sealer-model` on
rules 3 and 4, `943-sealer-p3` on rule 4, and `985-warden-p3` on rules 1 and
2. `957-sealer-p3` and `969-sealer-model` lost their rule 5 line and kept
the other.

**No record was written into the tree, and no earlier record was edited.**
The 17 copies sit in a scratch directory outside the tree, and that
directory is removed when the work hands back.

**The defaults this phase built on.** Q2: rule 5 alone. The section on rules
1 and 2 is `gaps.md` *Not done*, citing Q2. Q1 and Q3: the changelog states
the margin as 7%, sized from the 6.8-point figure. `gaps.md` *Not verified*
names the owner as Q1's answerer and the paid pair of Q3 as the
measurement the total's spread waits on.
