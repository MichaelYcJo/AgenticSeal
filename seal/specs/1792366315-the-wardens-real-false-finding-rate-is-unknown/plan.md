# Implementation Plan: the warden's real false-finding rate is unknown (#971)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-19 by the orchestrator, under the owner's `automation` answer and Q1's answer (phases 1–4; phase 5 is #985's), when `smith` was spawned.

## Summary

The warden's false-finding rate counts every row that no `truth-` grader
matches, so a real defect a case does not list reads as false. The issue's
first comment already classed every one of those rows, while the raw traces
still existed. The traces are gone now, but the committed side JSONs keep
every row and reproduce every truth result (`spec.md` §*What the issue's
step 1 stands on, opened*).

So the work runs in four free phases:

1. The classing goes into the tree, tied row by row to the committed rows.
2. `noninferiority.py regrade` re-grades a side under another suite's
   truths from those rows.
3. The real defects that recurred become truths through the generators.
4. Both warden sides are re-graded onto the new suite and recorded beside
   their af9c924b figures.

A fifth phase, a rule for the warden, is built only if the owner answers
`questions.md` Q1 `yes`. It is the only phase with a paid run.

## Technical context

- `evals/scripts/noninferiority.py:62-64` `FINDING_ROW`; `:179`
  `report_rows` (the last printed record's `location:` lines); `:376`
  `annotate` (writes `specseal.report_rows` per run); `:497`
  `side_numbers` (`rows`, and `false` where no truth regex matches); `:971`
  `compare` (refuses two sides whose suite trees differ); `:578` `verdict`
  (rule 4: the new preload's bytes must be below the baseline's,
  `new_bytes >= old_bytes` fails).
- `evals/scripts/replay_targets.py:351` `truth_pattern` (±15 lines around a
  `path:line`, or a unit's span, or the bare path; never `path#unit`);
  `:380` `targets` (a truth is a 🔴/🟡 closed `fixed` that the next round
  confirmed); `:497` `graders`.
- `evals/scripts/seed_defects.py:205` (the seeded truth is
  `truth_pattern` of the mutated line); `evals/scripts/rule_cases.py:217`
  `warden_case` (its truth, `truth-shout-twice`, written in code).
- `evals/scripts/behaviour.py:29` `grader` and `:48` `report_regex` write a
  grader file as YAML front matter (`type`, `target`, `pattern`, `flags`)
  and a body. `regrade` reads the same shape back.
- `tests/test_a_rewritten_definition_proved_non_inferior.py` holds the
  harness's and the generators' cases (`:988` a non-matching row is false,
  `:1116`–`:1345` truth derivation and patterns). The new cases go there.
  `tests/test_evals_layout.py` holds every case to the runner's schema.
- The warden's preload at 8a100e13 is not the one its last side measured:
  `agents/warden.md` hashes `9506b562…` against `ad823e75…`, and the
  contract `642b0da6…` against `e4f679e3…` (executed, `git show 8a100e13:<f>
  | shasum -a 256` beside `warden-phase-3.json`'s `specseal.preload`).
  Three commits since #957 merged touch its read set: f6ae6db6 (#967),
  4a6e24f6 (#969), f1c9932d (#975). Under #968's guard 1 that rules out
  reusing `warden-phase-3.json` as a baseline for a change to the warden.

**What breaks in six months.**

- *A case leaves the suite and the input file still names it.* The
  generator stops with exit 1 on an entry naming a case it does not write
  (`spec.md` §*Data & interfaces*), so the file cannot go stale silently.
- *A later run's record is edited after its last `cat`.* Then `report_rows`
  no longer equals what the eval graded, and a regrade would be wrong
  without saying so. `regrade` re-derives the side's own truth results
  first and refuses on any disagreement. The committed sides agree 24 of
  24 a side today (executed 2026-10-19).
- *The next warden change takes the re-graded phase-3 side as its
  baseline.* Guard 1 already refuses that: its preload is not the tree's.
  `Operational impact` says so, and the changelog fragment repeats it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Re-run both warden sides on the new suite instead of re-grading | About $72 (two sides of 18 runs; the committed sides cost $36.04 and $36.67) to learn what the rows already say. Phase 3's side would also have to be re-run on a preload that is no longer the tree's | Rejected: the owner's decision asks for a re-read at no cost, and the rows reproduce every truth result |
| `run --from-raw` (the issue's own means) | The raw output it reads does not exist | Rejected: not available. `regrade` reads what survived |
| A judge that classes each finding in the harness | `evals/README.md` says no judge scores anything. A judge's class cannot be re-checked by a regex | Rejected by policy |
| Hand-written `truth-*.md` files in the case directories | The next `--case` regeneration erases them, and `evals/README.md` forbids it | Rejected by policy |
| A generic replay rule: every ⬜ answered with a correction, confirmed next round, is a truth | It adds truths no run recurred on, which goes beyond step 2. It also depends on parsing two eras of record shapes, and nobody has measured whether the next round confirms ⬜ closures in a readable form | Not taken. One input file of the recurred defects covers what the issue asks. The generic rule can be weighed on its own later |
| Count only `must` rows as false (change rule 2's numerator) | The baseline's `wrong` row is a `should`, so the real false findings would vanish from the measure along with the noise | Rejected, and out of scope (`spec.md` §*Scope*) |
| Fix the scaffold's `git rm rounds/` and the fenced-row reader in this work | Both change what is read, so a side run without them cannot be re-read with them: the side-by-side would need two paid baselines | Out; the owner files it for the next release (`spec.md` §*Scope*) |
| Build the warden rule now (step 3) | One `wrong` row a side, with different causes. Rule 4 fails a preload that is not smaller. About $72–108 for a result that cannot tell the rule from noise | Not by default; `questions.md` Q1 is the owner's |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `evals/false-rows.md`: the 74 false rows of the two committed warden sides, each tied to its verbatim `location:` line, classed with the comment's vocabulary, and each class resting on a tree fact re-checked at the case's commits; the totals by class for both sides | The join command in `phases/phase-1.md` exits 0 only on an exact one-to-one cover of the 43 + 31 rows (S1); every `wrong`, `unclear` and `remark` row names its re-run command and result (S2). The reviewer re-runs the join and the named commands | c1a2f8a5 |
| 2 | `noninferiority.py regrade`, its refusals, and its cases; `evals/README.md` and the module docstring rewritten in place to name it | The cases for S3 and S4 in `tests/test_a_rewritten_definition_proved_non_inferior.py`, each seen red (§15); `regrade --suite-rev af9c924b` over both committed sides reproduces 55/43 and 47/31 and every truth result (executed) | cd39630a |
| 3 | The input file of added and widened truths, the three generators reading it, the regenerated warden cases, the cases for each generator path, and the README and docstrings rewritten in place. It opens by regenerating the nine committed warden cases from the generators **unchanged**, which must give an empty diff before anything is added (`questions.md` Q3) | Generator cases seen red (S6); `git status --porcelain evals/behaviour/` empty after a second regeneration; the other agents' suite trees unchanged (S7); the S5 join over both sides re-graded onto this phase's commit exits 0 | 864798a4 |
| 4 | Both sides re-graded onto phase 3's commit and committed here, `compare`'s record of them, the side-by-side table in `evals/false-rows.md`, and `changelog.md` stating that the new suite decides from the release after 0.22.2 | `noninferiority.py check` recomputes the new record's verdict from its numbers (executed). A verdict other than `pass` under the new suite is a figure to record, and it decides nothing (S8). The table's figures are recomputed by the S1 and S5 commands; S8 and S9 are read | 837ee9bc |
| 5 (only on Q1 `yes`) | A rule against the shared cause the owner names, in `agents/warden.md`, written so the preload is fewer bytes than at the tree this work starts from; a baseline side and a new side on af9c924b's suite, both re-graded onto the new suite at no cost | `compare` on af9c924b's suite gives `pass`; the new side's `wrong` rows, classed as in phase 1, are no more than the baseline's. **Paid: about $36 a side, two sides, so about $72; up to about $108 if a `fail` is fixed once and re-run.** The orchestrator schedules it | |

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past one
— someone can open it — which is the same trick that lets a round record live
beside the contract rather than in tool state.

Fill it in as each phase closes, not at the end. A phase reconstructed
afterwards is reconstructed from the diff, which is where it already was.

What a phase discovers while it is being built, and needs the next phase to
know, does not fit in this table's cells. Write it to
`seal/specs/<work-item-id>/phases/phase-N.md`, from `templates/sdd-phase.md`,
when the phase closes.

One caveat, so nobody builds on it, and it has two halves. Where feature
branches squash, these commits stop resolving at the merge — and **a rebase
during the work does the same thing earlier and far more quietly**, because the
orphaned object still answers `git cat-file` in the worktree that wrote it.
The quiet half is the one that bites: this column was wrong on its own first
use, nine SHAs deep, and only a reviewer opening them found it. **Re-read the
column after any rebase**, or it names commits that resolve in one clone and
nowhere else. That is tolerable because nothing measures from this column.

**How a reviewer re-checks phase 1, since its output is a table.** Three
things can be re-checked, and one cannot.

- **The cover.** The join command is mechanical. It reads both side JSONs,
  recomputes the false rows with af9c924b's truths, and compares them with
  the table's `(side, case, run, row, location)` keys.
- **The tree facts.** Each such reason names its command at a commit the
  case's `scaffold.sh` fetches. For example, phase 3's `wrong` row rests on
  `git cat-file -e 7ef6abbf:docs/the-review-record.md` failing.
- **The location.** Every class can be re-read against the code at the
  location, at the case's target.
- **What cannot be re-checked** is the finding's own wording beyond its
  location. The traces that held it are gone, so the comment's paraphrase
  is the only record, and the table labels it so.

## Operational impact

- **No new dependency or environment variable.** `regrade` is stdlib, as
  the module is.
- **The warden's suite tree moves at phase 3's commit; no other agent's
  does** (S7). A 0.22.2 comparison of the warden that passes `--suite-rev
  af9c924b` is unaffected. One that passes the default (`HEAD`) meets the
  new suite and is refused by `compare` against an af9c924b baseline.
  #968 and #970 name `--suite-rev af9c924b` in their bodies.
- **From the release after 0.22.2, a warden comparison uses the new suite.**
  Its baseline still has to be a run of the tree it starts from (#968's
  guard 1). The re-graded phase-3 side measured a preload that is no
  longer the tree's, so it is a record and not a baseline.
- **Generating cases now reads one more file.** Running `seed_defects.py`
  or `replay_targets.py --count N` for a new selection is unaffected; an
  entry in the file applies only to the case it names.
