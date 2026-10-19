# 1792363189-rule-3-decides-on-the-agent-not-one-run — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | c8e8329e |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Read #957's six records again under phase 1's rule 3 with `compare`, into
this work item's `evals/957-<name>.md`. No paid run, no `run` and no `run
--from-raw`: the raw directories do not exist, so the input is #957's
committed side JSONs, as `spec.md` says. Diff each new `## Graders` section
against #957's record. Run `check` on each new record, expecting exit 0 for
`pass` and 1 for `fail`, with no "it says … and its numbers give …" line.
Write this record's table of verdicts as recorded against as re-read, with
the reasons, and compare the verdicts with `spec.md` S9's prediction. A
divergence opens `overview.md`. Write `changelog.md` from both phases, per
`docs/the-record-layout.md`.

## What this phase found

**Every verdict matches S9's prediction, so no `overview.md` was opened.**
Each record was written by `noninferiority.py compare --agent <a> --phase
<N> --old <#957>/evals/baseline-<a>.json --new <#957>/evals/<name>.json
--out evals/957-<name>.md`, run at 8c244ae0's code. All six exited 0.

| #957 record | As recorded | Shape and reach passes, old → new | As re-read | Reasons as re-read |
|---|---|---|---|---|
| `warden-phase-2.md` | fail: rule 3 on `seeded-9b644676/shape-findings`, 1/2 against 2/2 | 66 → 70 of 72 | pass | every pass rule holds |
| `warden-phase-2-run-1.md` | fail: rule 3 on five graders, four at 1/2 and one at 0/2, each against 2/2 | 66 → 66 of 72 | fail | `shape grader warden seeded-9b644676/shape-findings failed every new run (0/2) where the baseline passed it 2/2 (rule 3)` |
| `warden-phase-3.md` | pass | 66 → 70 of 72 | pass | every pass rule holds |
| `smith-phase-3.md` | pass | 48 → 48 of 48 | pass | every pass rule holds |
| `framer-phase-3.md` | fail: rule 5, 33595.1 against 28253.1 tokens per tool call | 64 → 64 of 64 | fail | rule 5, the same line as recorded |
| `sealer-phase-3.md` | fail: rule 3 on `rule-sealer-untrue-body/shape-verdict` 1/2 against 2/2, and rule 5 | 30 → 29 of 30 | fail | `shape and reach graders passed 29/30 runs on the new side, fewer than the baseline's 30/30 (rule 3): sealer rule-sealer-untrue-body/shape-verdict 1/2 against 2/2`, and rule 5 as recorded |

The pass totals were computed with `noninferiority.py#parse_record` over
each record's `## Graders` table, on both #957's record and the re-read one.
They agree, and they are the framer's figures in S9. Reach passes are equal
on both sides of every record (warden 18, smith 8, framer 8, sealer 6), so
per-kind totals would give the same six verdicts.

**The case names carry the agent.** S9 and #957's records name the
grader `seeded-9b644676/shape-findings`. The suite's case is `warden
seeded-9b644676`, so the reason line reads `warden
seeded-9b644676/shape-findings`. This is only a shorter spelling of the
same grader, and the verdict does not change.

**Each `## Graders` section is byte-identical to #957's.** The section was
cut from `## Graders` to the next `## ` heading in both files and compared
with `diff`. All six exited 0, at 53, 53, 53, 29, 37 and 22 lines. A
`diff` of the whole files shows the same thing. `warden-phase-3`,
`smith-phase-3` and `framer-phase-3` are identical to #957's records. The
other three differ only in the `Verdict:` block: `warden-phase-2`'s verdict
word and reason, `warden-phase-2-run-1`'s five reasons becoming one, and
`sealer-phase-3`'s rule 3 line.

**`check` on each new record.** `warden-phase-2`, `warden-phase-3` and
`smith-phase-3` exited 0. `warden-phase-2-run-1`, `framer-phase-3` and
`sealer-phase-3` exited 1. None printed "it says … and its numbers give …".
Each printed only `its numbers give `fail`: ` followed by the reasons above.

**The side effect in `plan.md` §*Operational impact*, measured.** `check`
on #957's own records: `warden-phase-2.md` exited 1 and printed "it says
`fail` and its numbers give `pass`". That is the one disagreement the plan
names. The other five printed no such line. `warden-phase-3` and
`smith-phase-3` exited 0, and the remaining three exited 1 on their `fail`.
#957's records were not changed.

**The fragment.** `changelog.md` holds one `### Changed` entry. It covers
phase 1's rule and its reason lines, the case where one run still decides,
the table above, and the `check` disagreement a reader meets on an older
record. `bin/test tests/test_the_changelog_is_gathered_at_release.py
tests/test_no_passage_is_pasted_into_a_second_file.py -q` exited 0, 60
passed.
