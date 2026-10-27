# Questions for the planner: close the mutation gaps the old tests had (#1017)

## Judgments the ticket left open that the tree answered

Nobody reopens these. Each names what answered it.

- **The list is the body and its three comments, not the body's 135
  rows.** The body says an old gap a later fix pass adds "is posted as a
  comment on this issue", and the three comments add 33, 6 and 4 rows. #942's
  changelog fragment says the same: "The 178 such gaps are on #1017" (read,
  `seal/specs/1792628098-tests-rebuilt-one-file-per-module/changelog.md`).
- **The two `specseal_pytest_record.py` survivors are in scope.** They meet
  the body's definition of an old gap, and the body left them uncounted only
  because a review round recorded them (`spec.md` *What the list is*).
- **The `hooks/cmdline.py` rows no longer wait.** #1014 closed on 2026-10-25
  as superseded by #1027, which shipped as `61a8455a` and removed the text
  reading. Ten of the seventeen rows left the tree with it, and seven stand
  (`spec.md` *Rows whose code left the tree*).
- **30 rows left the tree and get no mutant.** Their modules, test file or
  functions are absent at `134d7203` (`executed`, `spec.md` *Rows whose code
  left the tree*). The body's two unclear `hooks/commitgate.py` rows, c15
  and c17, are among them. The third unclear row, `hooks/dispatch.py`'s
  event name, opens phase 2.
- **`hooks/implementer.py`'s cases go in a new `tests/test_implementer.py`.**
  `CONTRIBUTING.md` *The test layout* gives each shipped module one file.
- **`gh_json` is removed, not pinned.** It has no caller (`executed`,
  `git grep`), and `CLAUDE.md` keeps a mechanism only for what it does
  (`spec.md` *Removes*).
- **The record's two columns are before and after.** #942's two columns
  were its new file and the old files. Here the columns are the test files
  at the phase's start and the same files after the phase's cases
  (`spec.md` *In* item 5).
- **A survivor of the module's own file is run against the other files that
  reach the module before a case is written.** #942's round 3 did the same,
  and its record says k25 of `hooks/worktree_consent.py` is red on
  `tests/test_worktree_guard.py` (read, `phases/phase-6.md:1720` at
  `fc4f81ae`). A second case would duplicate it.
- **A record is read at the commit the issue names, not at the head.**
  `97bf7a9a` stripped template comments from #942's records, so the head's
  line numbers are not the issue's.
- **A case that reads the platform fakes it.** CI runs three legs, and a
  case that only one leg can turn red protects that leg alone (`plan.md`
  *Technical context*).

## Rows

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Which `--replace` pair realises a row that #942 described in prose, with no id and sometimes no function? | the work | (a) the narrowest replacement at the decision point the record's line names, which is the reading #942's own sentence most likely meant; (b) every replacement the sentence admits, one mutant each, which multiplies the batch and may close rows the record did not mean. The tree cannot answer it: #942's drivers were scratch files and are not in the tree, so the sentence is all that stands | (a), with the pair recorded verbatim in the phase's table, so a warden can rebuild another reading and run it | open |
| Q2 | Are two rows that produce the same pair one gap, such as the round 3 comment's s9 and the body's "a target that is not a directory" in `hooks/session-lease.py`? | the work | (a) one mutant, one case, and both rows point to that table row; (b) a case for each row, which writes a duplicate that `bin/test-layout --pairs` may name. The rows came from tables with separate id spaces, so only the rebuilt pairs can show whether they are one change | (a). The phase compares the two pairs at the head, and only byte-identical pairs are merged | open |
| Q3 | What happens if a census flags a line of `hooks/implementer.py` once `tests/test_implementer.py` ends with `test_census = census_case(TARGET)`? | the work | (a) the phase brings the flagged line to the shape the census names, in the module's commit, and records it as a divergence in `overview.md`; (b) the phase adds a `# exempt from <census>: <why>` line, which holds only where the shape is deliberate; (c) the cases go elsewhere, which breaks the layout. Reading the module found its `subprocess.run` and both `open` calls naming `encoding="utf-8"` and no `__main__` guard (read, `hooks/implementer.py:71`, `:97`, `:116`), so no flag is expected. The censuses were not run here, because a framer runs no check of the repository | (a) where the census names a shape for the line; (b) only where the line is deliberate and its reason can be written | open |
| Q4 | What is a row whose mutant survives because the code, and not the cases, is wrong: the mutant's behaviour is the one the caller needs? | the work | (a) a finding: no case, the row's outcome cell says `finding`, and `overview.md` *Not done* and the hand-back name it with the repository owner as its answerer; (b) fix the code here, which is a change of behaviour outside a test work item's scope and unreviewed as one; (c) a case pinning the current behaviour, which would pin the defect. Which rows are such can only be told by reading each at the head | (a) | open |
| Q5 | Do the new cases push the share of unpriced cases in `.test_durations` past one in twenty? | a measurement | (a) under the share: nothing to do; (b) over it: `test_the_durations_file_prices_the_suite` fails, and the file is refreshed from the branch's `tests` run artifact as `CONTRIBUTING.md` says. The share depends on how many cases the seven phases add and on how many the file already misses, and the second needs a collection of the suite, which a framer does not run | The orchestrator's broad gate runs the case. On a failure the orchestrator refreshes the file from the artifact and commits it | open |
