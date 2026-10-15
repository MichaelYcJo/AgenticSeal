# 1791876666-the-test-suite-is-held-to-a-budget — phase 4

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 423c916d |
| Ran by | smith on Opus 5.5, as `routing.md` names it |

## What this phase was asked

Phase 4 of the plan as the owner rewrote its row on 2026-10-15 (e5ee4c97),
a subtraction: the per-pull-request regrowth check leaves entirely, by the
owner's decision recorded in #929, *What this item ships, and where the rest
went*, item 3, over the changed-lines design of the reframe after round 6.

- Delete `.github/scripts/case_check.py`, its test module and the `cases`
  job in `.github/workflows/test.yml` with its comment.
- In the same commits, remove everything that stood only on them: cases,
  fixtures, census entries, `Enforced by:` lines naming them, wrapper
  references, `CONTRIBUTING.md`'s paragraph on what a case owes (rewritten in
  place to the rule that stands — a function's tests in its group with a
  success and a failure case, #942; the smith's and warden's test rules,
  #923 — or removed where nothing stands), and `docs/` and skill sentences
  describing the `cases` job.
- Keep `mutation-check`, its wrapper and its script, named as the tool #942's
  release sweep runs.
- Rewrite in place `spec.md` (the changed-lines check, its scenarios,
  `## Removes`), `questions.md` (Q8 moot), `changelog.md` (no per-case
  check) and `overview.md`; leave the phase and round records as history.
- Leave `seal/budgets.md` alone unless `budget_check.py` refuses only
  because a listed file no longer exists.
- Fill phase 4's Status and write this record of what was removed.

## What this phase found

**The removal list, with its counts, is `spec.md` §*Removes*, under the
five `Phase 4` bullets.** `templates/sdd-phase.md` keeps what a work item
takes out of the tree in the frame's `## Removes` and out of this record, so
the counts asked for here (1,105 lines and 26 functions of
`case_check.py`; 618 lines, 13 functions and 27 ids of its test module; 33
lines of the job; 17 lines and one `Enforced by:` of the paragraph) are
written there once. The three removals the frame's row did not name are
divergence rows in `overview.md`.

**`--baseline-passed` stood only on the check.** Phase 2 added it to
`mutation-check` for `case_check.py`, whose docstring named that file as its
one caller, and nothing else in the tree passes it (`git grep` at
e5ee4c97). It leaves with its case, and `mutation-check` keeps the options
it had on the base. #942's sweep runs the baseline every time, which is what
the option skipped.

**One case outlived its module.**
`test_a_windows_command_line_keeps_the_backslashes_of_its_paths` calls
`arm_check.py#command_words`, which stays and whose fix the changelog's
`Fixed` entry ships. It moved to `tests/test_arm_check.py`, the group of
the function it calls, and uses that module's loaded `ARM` rather than a
load of its own. Seen red there: `bin/mutation-check
skills/verify/scripts/arm_check.py --replace '        lexer.escape = ""'
'        pass'` with the case selected, exit 0 (`red`), the file restored.

**Nothing stands in the tree for the `CONTRIBUTING.md` paragraph to say.**
The success-and-failure rule, the placement check and the new-test rules
are #942's and #923's and live only in those issues, so a rewritten
paragraph would have had no `Enforced by:` target, and `unenforced` is a
gate at `+0 rules` per file. The paragraph was this branch's own, so
removing it leaves the base's text.

**The frame still describes the changed-lines design in four places of
`plan.md`** that this phase does not own: the Summary's third paragraph
(*What stays is the half the owner kept …*), the Technical context bullets
on the `cases` job's shape and its cost, the Test rows T1–T8 for phase 4
and their sentence citing Q8, and the first two Operational impact bullets
(*one new CI job*; *From phase 4 on, the `cases` job names no test case
…*). Alternatives T to AD cite `spec.md` §*The changed-lines check*, which
is now §*The per-pull-request check leaves*. They are the framer's or the
orchestrating session's to rewrite; this phase built to the phase 4 row,
which is the part that holds.

**#944's frame says the `cases` job exists.**
`seal/specs/1791940762-the-record-of-truth-is-tests-not-coordinates/spec.md`
line 46, merged into the release branch, says *the `cases` job of #929
proves a new case kills what it says*. That frame is another work item's,
and when `settle` folds it into a `docs/` policy that sentence would carry a
job that never shipped. This phase did not edit it.
