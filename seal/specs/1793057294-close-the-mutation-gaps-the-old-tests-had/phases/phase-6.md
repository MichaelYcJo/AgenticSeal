# 1793057294-close-the-mutation-gaps-the-old-tests-had — phase 6

| Field | Value |
|---|---|
| Phase | 6 |
| Commit | fea473fc |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Phase 6 only: the rows of #1017 for `.github/scripts/issue_claims_check.py`,
`.github/scripts/roll_flow_measurement_issue.py`,
`.github/scripts/release_report.py` and the `tests/conftest.py` helpers.
Follow the method and table shape of phases 1 to 5: rebuild each row at the
head with `bin/mutation-check` and `-x`, run a survivor again against the
other test files that load the module, write a case only where it survives all
of them, and see each new case red alone under its mutant. #945's phase 5
added `seal/process/*.md` to `release_report.py`'s `DOCUMENTS`, with a case.
h2's case runs from a working directory that is not the repository root.

95fa9fb7 merged `release/v0.22.4` at 5daa931f into the branch, and with it
#945's changes to `session_cost.py` and `broad_gate.py`. Phases 1 to 5
measured their rows before that merge. Record, for phase 7, every row of
phases 1 to 5 whose code the merge removed or changed, checking the
`broad_gate.py` and `session_cost.py` rows against the head with `git grep`,
and re-run only those rows.

One commit per module that needs one, then this record and phase 6's Status
in `plan.md`. Build on `questions.md`'s defaults Q1 to Q5. Fake every decision
that reads the platform.

## The outcomes

25 rows, rebuilt as 25 mutants. 22 rows are killed by a new case and 3 are
equivalent. None was already closed, none left the tree, and none is a
finding.

| Module | Commit | Rows | Mutants | Killed by a new case | Already closed | Equivalent | Left the tree |
|---|---|---|---|---|---|---|---|
| `.github/scripts/issue_claims_check.py` | 0a1c3676, fea473fc | 10 | 10 | 8 | 0 | 2 | 0 |
| `.github/scripts/roll_flow_measurement_issue.py` | a2ce7489 | 4 | 4 | 3 | 0 | 1 | 0 |
| `.github/scripts/release_report.py` | 697fc63b | 3 | 3 | 3 | 0 | 0 | 0 |
| `tests/conftest.py` | dcec8fe8 | 8 | 8 | 8 | 0 | 0 | 0 |

## How the tables read

The tables read as phase 1's do. Each pair is written as the zsh command line
passed it to `bin/mutation-check --replace`. A `$'...'` string is ANSI-C
quoted, so `\n` in it is a newline. A `\|` in a cell is one `|` of the pair,
escaped for the table.

The before column is the module's batch with `-x -p no:xdist` in `--tests`,
first against the module's own test file, then, for each survivor, against
every other test file that names the module, found with `git grep -l` over
`tests/`. Every before batch ran at 95fa9fb7, before this phase wrote a case.
The other files are listed above each table. The conftest batch ran against
`tests/test_conftest.py` alone, as `plan.md`'s phase 6 row says. The after
column is the same batch against the module's own file at the module's commit,
or at fea473fc for `issue_claims_check.py`. Every batch passed its baseline.

A new case was seen red alone on its mutant with
`bin/mutation-check <module> --replace OLD NEW --tests "bin/test tests/test_<stem>.py -q -x -p no:xdist -k <case>"`.
Each of those runs printed `red: the cases failed against the mutation (exit 1)`
and exited 0, so its baseline passed against the code. Each failure was the
case's own assertion, except two. h4's mutant raises `CalledProcessError`
inside the case, and rr5's lets the stand-in meter's `PermissionError` out of
the case.

## `.github/scripts/issue_claims_check.py`

Records: the issue body's i1 to i31, `phases/phase-6.md:1360` to `:1371` at
`79f9c3fd`. Before: `tests/test_issue_claims_check.py`, then
`tests/test_a_body_naming_two_issues_claims_one.py tests/test_every_reader_ends_a_line_where_gfm_does.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| i1: the masking turns a newline inside a fence into a space | `'        return "".join("\n" if c == "\n" else " " for c in m.group(0))'` `'        return " " * len(m.group(0))'` | SURVIVED, every file | red, `Test_prose_only::test_accepts_a_fenced_block_blanked_with_its_newlines_kept` | killed by a new case |
| i7: a whitespace-only segment is kept | `' if text[a:b].strip()]'` `']'` | SURVIVED, every file | red, `Test_segments::test_refuses_a_run_of_whitespace_as_a_segment` | killed by a new case. The record marks it equivalent; *What this phase found* says why it is a gap |
| i8: a claim's span starts at its keyword, not its digits | `'(m.group(1), m.start(1), m.end(1))'` `'(m.group(1), m.start(0), m.end(1))'` | SURVIVED, every file | red, `Test_claimed_spans::test_accepts_the_digits_of_a_claim_as_its_span` | killed by a new case |
| i9: `claimed` keeps a number claimed twice | `'if number not in claimed:'` `'if True:'` | SURVIVED, every file | red, `Test_read::test_accepts_a_number_written_twice_once_in_its_list` | killed by a new case |
| i11: `mentioned` keeps a number named twice | `'if number in claimed or number in mentioned:'` `'if number in claimed:'` | SURVIVED, every file | red, `Test_read::test_accepts_a_number_written_twice_once_in_its_list` | killed by a new case |
| i12: a segment counts a claim after its end | `'if start <= c[1] < end]'` `'if start <= c[1]]'` | SURVIVED, every file | SURVIVED | equivalent: `here` is read twice. `before` keeps the claims whose digits start before a number, and every number the loop reads starts before `end`, so a claim past the end is never in `before`. `if not here` lets a segment through that the code skips, and that segment then warns about nothing for the same reason |
| i13: a segment with no claim is not passed over | `$'        if not here:\n            continue'` `$'        if False:\n            continue'` | SURVIVED, every file | SURVIVED | equivalent: in a segment with no claim, `before` is empty for every number, so no warning is appended. The `sentence` built on the way is read by nothing else |
| i22: a sentence is shortened at any length | `'return sentence if len(sentence) <= limit else sentence[: limit - 1] + "…"'` `'return sentence[: limit - 1] + "…"'` | SURVIVED, every file | red, `Test__short::test_accepts_a_sentence_at_the_limit_whole` | killed by a new case |
| i27: `ISSUE_REF` reads `#22abc` as a number | `'ISSUE_REF = re.compile(r"#(\d+)\b")'` `'ISSUE_REF = re.compile(r"#(\d+)")'` | SURVIVED, every file | red, `Test_read::test_refuses_a_number_glued_to_letters_as_an_issue` | killed by a new case |
| i31: an ordered-list line opens no block | `'    r"\|\d+[.)](?=\s)"'` `'    r""'` | SURVIVED, every file | red, `Test_segments::test_accepts_an_ordered_list_item_as_a_segment_of_its_own` | killed by a new case |

## `.github/scripts/roll_flow_measurement_issue.py`

Records: the issue body's r1, r2, r4 and r18, `phases/phase-6.md:1436` to
`:1441` at `79f9c3fd`. Before: `tests/test_roll_flow_measurement_issue.py`,
then `tests/test_a_release_rolls_the_flow_measurement_issue.py tests/test_session_cost.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| r1: `run` does not exit on a failed call | `$'    if out.returncode:\n        sys.exit('` `$'    if False:\n        sys.exit('` | SURVIVED, every file | red, `Test_run::test_refuses_a_failed_call_by_exiting_with_its_stderr` | killed by a new case |
| r2: `try_run` answers a failed call's output | `'return None if out.returncode else out.stdout'` `'return out.stdout'` | SURVIVED, every file | red, `Test_try_run::test_refuses_a_failed_calls_output_as_none` | killed by a new case |
| r4: `rolled_from` takes the prefix anywhere in the title | `'if not title.startswith(TITLE_PREFIX):'` `'if TITLE_PREFIX not in title:'` | SURVIVED, every file | red, `Test_rolled_from::test_refuses_a_title_carrying_the_whole_prefix_after_other_text` | killed by a new case |
| r18: `find_baseline_issue` names the last open log, not the first | `'return (issues[0]["number"], None) if issues else (None, None)'` `'return (issues[-1]["number"], None) if issues else (None, None)'` | SURVIVED, every file | SURVIVED | equivalent: `if len(issues) > 1` returns on the line above, so the list this line reads holds one entry or none, and its first entry is its last |

## `.github/scripts/release_report.py`

Records: the round 3 comment's rr3, rr5 and rr7, `phases/phase-6.md:1744` at
`fc4f81ae`. Since then `DOCUMENTS`, `documents`' docstring and the module
docstring changed, and none of these rows' lines (`executed`,
`git diff fc4f81ae HEAD`). Before: `tests/test_release_report.py`, then
`tests/test_release_completeness_check.py tests/test_the_release_table_reads_two_trees_and_fails_nothing.py tests/test_ci_gives_the_checks_what_they_need.py`.
The last of these names the tests workflow's `release-report` step and not the
module's file name.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| rr3: a durations file of other values is read | `'isinstance(v, (int, float)) and not isinstance(v, bool) for v in data.values()'` `'isinstance(v, (int, float)) for v in data.values()'` | SURVIVED, every file | red, `Test_durations::test_refuses_a_file_of_booleans_as_seconds` | killed by a new case |
| rr5: an agent definition that cannot be read is let out | `'    except OSError as error:'` `'    except () as error:'` | SURVIVED, every file | red, `Test_preloads::test_refuses_a_definition_it_cannot_read_as_unreadable` | killed by a new case |
| rr7: a job name is read by its prefix | `'PYTEST_JOB.fullmatch(job["name"])'` `'PYTEST_JOB.match(job["name"])'` | SURVIVED, every file | red, `Test_leg_minutes::test_refuses_a_job_whose_name_only_begins_as_a_pytest_job` | killed by a new case |

## `tests/conftest.py`

Records: the issue body's h2 to h23, `phases/phase-4.md:32` to `:57` at
`79f9c3fd`, and the round 3 comment's ch6, `phases/phase-7.md:170` at
`fc4f81ae`. Before: `tests/test_conftest.py` alone.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| h2: `read` is not joined under the repository root | `'with open(os.path.join(ROOT, *parts), encoding="utf-8") as handle:'` `'with open(os.path.join(*parts), encoding="utf-8") as handle:'` | SURVIVED | red, `Test_read::test_refuses_the_working_directorys_file_for_the_roots` | killed by a new case |
| h4: `git` always checks the exit code | `$'        ["git", "-C", str(repo), *args],\n        check=check,'` `$'        ["git", "-C", str(repo), *args],\n        check=True,'` | SURVIVED | red, `Test_git::test_accepts_a_failing_call_with_checking_off_as_its_process` | killed by a new case |
| h6: `commit_everything_as_e` without its identity | `'git_out(repo, *identity, "commit", "-qm", message)'` `'git_out(repo, "commit", "-qm", message)'` | SURVIVED | red, `Test_commit_everything_as_e::test_accepts_a_commit_by_e_in_a_repository_of_another_identity` | killed by a new case |
| h12: `imported_roots` does not mark a relative import | `'roots.add((node.module or "").split(".")[0] if not node.level else ".")'` `'roots.add((node.module or "").split(".")[0])'` | SURVIVED | red, `Test_imported_roots::test_refuses_a_relative_import_as_a_name` | killed by a new case |
| h14: `q` does not quote | `'return shlex.quote(str(text))'` `'return str(text)'` | SURVIVED | red, `Test_q::test_refuses_a_space_unquoted` | killed by a new case |
| h21: `guard_decision`'s silent answer is renamed | `'return "silent", ""'` `'return "quiet", ""'` | SURVIVED | red, `Test_guard_decision::test_refuses_a_guard_that_prints_nothing_as_anything_but_silent` | killed by a new case |
| h23: `repo_relative` returns the base name | `'return posix_id(os.path.relpath(path, ROOT))'` `'return posix_id(os.path.basename(path))'` | SURVIVED | red, `Test_repo_relative::test_refuses_to_drop_the_directories_of_a_nested_path` | killed by a new case |
| ch6: `decline_if_shrunken` skips a whole tree | `$'    if missing:\n        pytest.skip('` `$'    if True:\n        pytest.skip('` | SURVIVED | red, `Test_decline_if_shrunken::test_refuses_to_decline_when_nothing_is_missing`, rewritten | killed by a rewritten case |

## The rows the merge moved

95fa9fb7 changed five Python files outside `tests/` (`executed`,
`git diff --stat c617012b 95fa9fb7 -- '*.py'`). Two hold rows of phases 1 to
5: `skills/verify/scripts/session_cost.py` and
`skills/verify/scripts/broad_gate.py`, both phase 4's. The other three hold
none: `.github/scripts/release_report.py` is this phase's,
`hooks/root-migrate.py` is outside the work (`spec.md` *Out*), and
`skills/verify/scripts/unverified_check.py` has no row.

**The merge removed no row's code.** Each of phase 4's 17 pairs, 13 in
`session_cost.py` and 4 in `broad_gate.py`, lands exactly once in its module
both at c617012b and at 95fa9fb7 (`executed`, a scratch script counting each
pair's old text in `git show <commit>:<module>`). The `broad_gate.py` lines
the merge removed, `UNVERIFIED`, `UNVERIFIED_NAME`, `SPECS`, the `unverified`
arm of `gate` and its `PARTITION` row, hold none of b22, b29, b50 or b70. Those
four stand in `refused_broad_row`, `missing_row`, the command-name scan and
`compare_at_base`, which the merge did not touch.

**One row's function changed, and the row is unmoved.** The merge gave
`session_cost.py#report_segments` a `context` column and left the line s46
mutates, `if segments["unnamed"]:`, as it was. Re-run at 95fa9fb7 against
`tests/test_session_cost.py`, s46 is `red`, on
`Test_report_segments::test_refuses_to_print_an_unnamed_segment_without_saying_why_it_has_no_name`,
the case phase 4 named. No other row's function changed. In `session_cost.py`
the merge also changed `segment_slices` and added `largest_context`, and in
`broad_gate.py` it changed `gate` and a comment in `failed_form`; none of them
holds a row. The merge's hunks in the two test files sit in
`tests/test_broad_gate.py`'s `WORKFLOW` constant, which `Test_job_steps` and
`Test_steps_for` read, in `Test_unquote`, `Test_unanswered`,
`Test_failed_form`, `Test_gate` and `Test_main`, and in the new
`Test_largest_context`. None of them is a case phase 4 named as killing
(`read`). Phase 7's overview can say the merge moved no outcome.

## What this phase found

**i7 is a gap, though #942's record marks it equivalent.** Through `read`, no
input tells the two apart: a run of whitespace holds no claim, and
`if not here` skips it. But `segments` is a public function, a case of
`Test_module` already calls it directly, and its docstring says empty runs are
dropped. Under the mutant, `segments("Closes #11.\n\n#22 is next.")` returns
the blank line between the sentences as a segment of its own. `spec.md` *In*
item 1 counts a mutant equivalent only where no input tells it from the code,
and a direct call does, so it got a case. The filter's one effect is on what
`segments` returns, which `read` never needs. Under `CLAUDE.md` *The rule a
mechanism is kept against*, phase 7 can name it in `overview.md` as one for the
repository owner to keep or remove.

**i12 and i13 are two guards of `read` that change nothing anyone receives.**
The `< end` bound and the `if not here` skip each leave every warning as it
was, for the reasons the table gives. `spec.md` *Out* leaves shipped code
alone, so phase 7 can carry both into `overview.md` beside phase 5's k12 and
s47, for the repository owner to decide.

**One module took two commits.** At 0a1c3676 `bin/test-layout --pairs` named
i27's first case and `test_an_anchor_is_not_an_issue_number` as one pair, so
the two were made one parametrized case. That rewrote the existing case's
`def` line, and phase 7's check reads every removed line holding `def test_`
as a removed case. fea473fc restores the anchor case unchanged and gives i27 a
case of its own, whose body `--pairs` does not pair. `git diff 95fa9fb7 HEAD
-- tests` removes no line holding `def test_` (`executed`).

**ch6 is closed by rewriting an existing case, not by adding one.** The case
asserting no decline could not fail: under the mutant `pytest.skip` ended it
as skipped, which a run reads as no failure. The case now catches the skip and
fails on it, and it was seen red alone that way. It is the one row of this
phase closed by changing an existing case. No row was closed by giving an
existing case a fixture.

**`Test_q`'s accepts case reads a path object.** `--pairs` named `Test_q`'s
first two cases as one pair, since `q("plain")` and `q("a b")` normalise
alike. The accepts case now hands `q` a `pathlib.PurePosixPath`, which pins
the `str()` before the quoting: `shlex.quote` raises `TypeError` on a path
(`executed`, this worktree's interpreter). The one pair `--pairs` prints over
the four files is `Test_find_baseline_issue`'s, which this phase did not touch.

**Each new function class holds both kinds of case.** `Test_prose_only`,
`Test_segments`, `Test_claimed_spans`, `Test__short`, `Test_run`,
`Test_try_run`, `Test_preloads`, `Test_durations`, `Test_leg_minutes`,
`tests/test_conftest.py`'s `Test_read`, `Test_repo_relative`, `Test_git`,
`Test_commit_everything_as_e`,
`Test_imported_roots`, `Test_q` and `Test_guard_decision` are new, and
`bin/test-layout --check` asks each for an accepts case and a refuses case.
Each partner case reads an input its group did not. In some classes the killing
case is the accepts one: i1, i8, i22, i31, h4 and h6.

**No case fakes a guarantee the platform gives (contract rule 13).** `run`
and `try_run` are called for real, on this interpreter, which each CI leg has.
`Test_git` and `Test_commit_everything_as_e` run real git in a scratch
repository. h6's case gives that repository the identity `t` and removes the
four `GIT_AUTHOR_*` and `GIT_COMMITTER_*` variables, so the identity the
mutant falls back to is the repository's and never a machine's. h2's case
moves the working directory into a scratch directory holding a decoy
`CLAUDE.md`, a directory other than the root, which `bin/test` never runs
from. Two cases hand the function a stand-in for a module it takes as an
argument: `Test_preloads` a meter whose composition raises `PermissionError`,
and `Test_guard_decision` a guard whose `main` prints and exits. Neither stands
in for the platform. Every path a case builds is built with `os.path.join` or
`pathlib`, and `repo_relative`'s cases compare the `/` spelling the helper
returns, so a Windows separator gives the same verdict.

**The conftest batches ran with nothing else running.** A mutant of
`tests/conftest.py` reaches every pytest run in the worktree while it stands,
so no other batch shared the window.

**Q5 is the orchestrator's.** This phase adds 35 cases, none of them priced
in `.test_durations` (`executed`, `git diff 95fa9fb7 HEAD -- tests`, the lines
adding `def test_`). Whether the seven phases' cases pass one in twenty
unpriced is read by `test_the_durations_file_prices_the_suite` in the broad
gate.

**Run for the phase** (`executed`, at fea473fc):
`bin/test tests/test_issue_claims_check.py tests/test_roll_flow_measurement_issue.py tests/test_release_report.py tests/test_conftest.py -q`
exited 0, 168 passed. `bin/test-layout --check` over the four files reads 4
files with 0 refused, and `--pairs` prints the one pair named above.
`uvx ruff check` and `uvx ruff format --check` over the four files exit 0.
`git diff 95fa9fb7 HEAD -- tests` removes no line holding `def test_`.
