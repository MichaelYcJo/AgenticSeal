# Phase 2: 1793232075-the-living-text-still-calls-the-design-a-spec

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 92bd9acc |

## What this phase was asked

Build phase 2 of `frame/plan.md` against the frame at `d4b88f70`, in the
same spawn as phase 1, and leave phase 3 to the merge of #1020
(`frame/questions.md` Q1, default (a)). The phase rewrites the docstrings,
comments and printed strings of `skills/settle/scripts/settle.py`,
`skills/settle/scripts/rule_changes.py`,
`skills/verify/scripts/unverified_check.py` and
`skills/implement/scripts/seal.py`. It moves the pins at
`tests/skills/test_settle.py:1532` and
`tests/skills/test_unverified_check.py:2107`, rewrites the mirror path at
`skills/commit-pr-convention/SKILL.md:210`, and re-points the two cases
the 0.23.0 move left reading `seal/specs/`. Commands C1 to C6 run at the
phase's close, with their output recorded here.

## What this phase found

- **The frame held against the tree.** Every phase-2 row stood at its
  coordinate at `d4b88f70` (read). `settle.py:334` and `:927` format the
  value `seal/threads` through the key `specs`, not the identifier's name,
  as `plan.md` A2a says (read), so `SPECS` and that key stay.
- **The guarantee case was blind, and now it reads.** `bin/seal mutate`
  added a second `Verdict: sealed` line to
  `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/guarantee.md`
  and ran
  `test_every_committed_guarantee_shows_its_one_verdict_line`. Against the
  case as it stood, the run reported `SURVIVED` (executed, before the edit).
  Against the re-pointed case at `92bd9acc`, it reported `red` (executed).
  `seal mutate` restored the file from the bytes it held, and
  `git status` showed nothing changed.
- **The mirror case reads `seal/threads/` and lists nothing there.** No
  `pr.*.md` stands under `seal/threads/` (executed `ls`). To see it red, a
  file `pr.kr.md` was written into this work item's directory. The case
  failed with "a mirror is not named for a language this file knows:
  ['pr.kr.md']" (executed, exit 1). The file was then removed with `rm`,
  and the case passed (executed, exit 0). The case's local name `specs`
  became `threads` with its path, because the lines the frame re-points
  are the lines that name it. `frame/design.md` *Scope* keeps the
  identifiers of shipped code, and this is a local of one case.
- **Both moved pins were seen red through `bin/seal mutate`.** The purpose
  sentence in `settle.py#PURPOSES` was put back to "it is what reads a
  spec's `## Rule changes`", and
  `test_each_sibling_is_refused_with_its_own_purpose` went red (executed).
  The tally was put back to "overviews", and
  `test_accepts_a_tracked_link_counted_once_and_not_deleted` went red
  (executed). Both runs exit 0 with the verdict `red`.
- **The two dry-run headings needed no pin of their own.**
  `test_settle.py` reads `GROUPS_HEADING` and `WHOLE_HEADING` through the
  module, as `plan.md` *Technical context* says, and the module passed
  with the new text (executed).
- **`.test_durations` names the old parametrize id.** The case
  `test_each_sibling_is_refused_with_its_own_purpose[RULES-it is what reads a spec's ...]`
  is now `[RULES-it is what reads a design's ...]`, so its timing is
  unpriced. `CONTRIBUTING.md` refreshes the file from a `tests` run's
  artifact, and this branch has had none.
- **Q2 (c), a line that fits neither table.**
  `evals/scripts/replay_targets.py:132` reads `seal/specs/<item>/rounds/`
  in the working tree, and since 0.23.0 that directory holds nothing. It
  is the same blindness as the two cases. Its comment says it reads "the
  0.22.x layout of the records its cases come from", and the half that
  reads tags still finds them. `frame/design.md` *Scope* puts `evals/`
  out, so it stays, for the review to weigh.
- **The test modules this phase touches.** 43 modules under `tests/` name
  a phase-2 file. They ran with `tests/test_censuses.py`,
  `tests/behaviour/test_docs_line_wrap.py` and
  `tests/text/test_no_passage_is_pasted_into_a_second_file.py`. The run
  gave `1 failed, 2893 passed, 9 skipped`, and the one failure is the
  missing closing memo that `trail/phases/phase-1.md` names (executed,
  `bin/test -q`, exit 1). `uvx ruff check` and `uvx ruff format --check`
  over the eight changed Python files exited 0, and no added Python line
  passes 88 columns.

### C1 to C6 at `92bd9acc`

| Command | Output |
|---|---|
| C1 | 163 lines in 44 files. Every line in the phase-2 files is an identifier (`settle.py#SPECS` and its uses, `rule_changes.py`'s `specs` parameter, `SPECS` in two docstrings that name that parameter), history (`rule_changes.py:273`), or a reference root (`unverified_check.py:77`, `:926`, `:1022`, `:1075`). The rest is phase 1's kept list and phase 3's rows |
| C2 | 23 lines, the same as at `e3c6503f` |
| C3 | 18 lines. Two are Q2 (b) in `trail/phases/phase-1.md`. The other 16 are the identifiers `OVERVIEW`, `overviews`, `overviews_at` and the local `overview` in `unverified_check.py` and `settle.py` |
| C4 | 59 lines. All are fixtures under `tests/`, except `evals/scripts/replay_targets.py:132` above |
| C5 | `design`, `Design`, `designs`. No word holds `design` inside another word |
| C6 | 837 hits in 79 files under `tests/`. The two moved pins and the two re-pointed cases account for the 8 below `e3c6503f` |
