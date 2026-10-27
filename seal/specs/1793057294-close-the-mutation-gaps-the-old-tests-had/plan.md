# Implementation Plan: close the mutation gaps the old tests had (#1017)

Approved 2026-10-27 by the orchestrator, when `smith` was spawned.

## Summary

#942 found mutants of shipped code that survive both its rebuilt test files
and the old files, and recorded them on #1017 without closing any. This work
rebuilds each row that still stands at the branch's head, gives it one of the
four outcomes `spec.md` *In* item 1 names, and adds a case only where the
mutant survives every test file that reaches its module. The rows are spread
over many modules, so the build is cut into seven phases of whole modules.
Each phase is sized so that one smith spawn with a fresh context can rebuild,
run and close its modules, and each module lands in one commit.

## Technical context

- **The instrument is `bin/mutation-check`**
  (`skills/verify/scripts/mutation_check.py`). A batch is one call with
  `--replace OLD NEW` once per mutant and `-x` in `--tests`. The baseline
  runs once; each mutant is written alone, run, and restored, and one line
  is printed per pair. A pair that does not land exactly once refuses the
  whole batch before anything runs, which is what makes a rebuilt mutant
  trustworthy: a pair written against code that changed is refused, not
  silently skipped. Each run has a bound of 300 s unless `--timeout` says
  otherwise. `tests/test_chain_check.py` is the slowest file these phases
  run: `.test_durations` prices it at about 261 s over 256 cases on Windows
  (`executed`, read from the file at `134d7203`). Phase 5 passes a
  `--timeout` above its baseline's seconds where the baseline nears the
  bound.
- **The rows carry no drivers.** #942's mutant drivers were scratch files.
  Each row's sentence, and the line of its record at the commit the issue
  names, say what the mutant changes. 37 body rows have no id and are prose
  (the issue body, *Where the list comes from*). The phase writes the pair
  that realises the sentence and records it verbatim.
- **The test layout bounds where a case can go.** `bin/test-layout --check
  <file>` refuses a class that names no function of the file's `TARGET`, a
  function class without both a `test_accepts_` and a `test_refuses_`
  case, and a top-level helper defined byte-identically in two test files
  (#942's changelog fragment, read at
  `seal/specs/1792628098-tests-rebuilt-one-file-per-module/changelog.md`).
  So a class a phase adds holds both kinds of case, even where the mutant
  needs only one, and a helper two files need goes into `tests/conftest.py`.
  Many module files have only some of their functions' classes:
  `tests/test_session_cost.py` has `Test_main`, `Test_emit`, `Test_post`,
  `Test_family` and `Test_module` (`executed`, `grep '^class '`), so most of
  its cases open new classes.
- **The records' line coordinates are pinned to commits.** #942's directory
  still stands at the head, but `97bf7a9a` (#1026) stripped template
  comments from its records, so a line number at the head is not the line
  the issue cites. Every phase reads a record with `git show
  <commit>:<path>` at the commit the issue or its comment names.
- **CI runs Linux, macOS and Windows.** Some decisions read the platform:
  `hooks/hooksession.py` walks the process tree with `ps`, which Windows
  does not have; `hooks/console.py#to_utf8` reconfigures the console; and
  `hooks/worktree_consent.py`'s k25 is the Windows branch of
  `split_with_separators`. A case for such a decision fakes the reading,
  with `monkeypatch` on the subprocess call, the platform name or the
  stream, so it gives one verdict on all three legs.

The failure scenario of the chosen approach, six months on: a case written
to kill one mutant asserts the mutant's own wrong output too exactly, such as
a full message string or a count of internal calls. The next honest change
to that function then fails the case for a reason that has nothing to do with
the protection it was written for, and the contributor deletes it. The
guard is in the scenario table of `spec.md`: a case asserts the behaviour the
function owes its caller, accepted or refused, which the mutant breaks. It
does not assert an incidental string.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Rebuild each row at the head, run it against the module's test file and then the other files reaching the module, and add a case only where it survives all of them (chosen) | A row's prose admits two replacements, and the phase picks one the old files would have killed; the gap the record meant stays open under a case that pins a neighbour. The phase records the pair verbatim, so the warden can rebuild the other reading | Chosen. It is the only approach that tells a standing gap from a closed one before writing anything |
| Write a case from each row's sentence, trusting the records, without rebuilding at the head | 30 rows name code `61a8455a` removed (`spec.md` *Rows whose code left the tree*), so their cases cannot be written; others are red already, such as k25 of `hooks/worktree_consent.py`, which #942's round 3 record says is red on `tests/test_worktree_guard.py` at its head (read, `phases/phase-6.md:1720` at `fc4f81ae`). A case for a red mutant is a duplicate that `bin/test-layout --pairs` may not even name | Rejected |
| Run a fresh decision-point sweep of every module at the head and close every survivor, the list's and new ones alike | The scope is no longer the list the issue states, and the phase sizes cannot be known before the sweep runs. A sweep is a measurement of its own, and a later item can take it with the instrument this work leaves unchanged | Rejected |
| Mark a row equivalent wherever a case is hard to write | A gap that needs a fixture, a fake process tree or a second clone is recorded as unprovable, and nobody looks again. Equivalence is a claim about every input, and the records already mark the rows they found so | Rejected. A row is equivalent only where reading the code shows no input tells the two apart |
| Replace the structure the mutant exposes rather than pin it: remove code no caller reaches | Removing code a caller does reach breaks the caller. The premise that keeps each structure is checked by `git grep` for callers. `gh_json` has none, so it goes (`spec.md` *Removes*). `run`, `try_run`, `_issue_api` and `arrived` are called by the scripts' own `main` paths and are only faked by the cases, so they stay and get a case that calls the real function | Chosen for `gh_json` alone. A phase that finds another function no caller reaches records it as a divergence in `overview.md` and does not remove it |
| Keep `tests/test_implementer_mark.py` and `tests/test_implementer_notice.py` as the home of `hooks/implementer.py`'s two cases, as #942 left it | A case in a file whose `TARGET` is another module is a case `bin/test-layout --check` cannot place, and the next contributor reading `hooks/implementer.py` finds no file that names it. The premise that kept it, that #942 did not rebuild the module, does not bind a new case | Rejected. `tests/test_implementer.py` is added (`spec.md` *In* item 3) |
| One phase per module | Thirty-odd spawns, most for one or two rows, each paying a fresh context's reading of the contract, the frame and the tooling | Rejected. Seven phases of whole modules, grouped by the directory and the readers they share |

## How a phase rebuilds a row

The smith runs this for each module of its phase, in one commit per module:

1. **Read the row and its record.** The row is in the issue body's *The
   gaps* or in one of the three comments' tables. Its `Record` cell is read
   with `git show <commit>:seal/specs/1792628098-tests-rebuilt-one-file-per-module/<path>`
   at the commit the body or the comment names.
2. **Find the decision at the head.** Where the function or constant the
   row names is not defined at the head, or the module no longer makes the
   decision the sentence describes, the row has left the tree. The phase
   names the commit that removed it, found with `git log -S '<text>' --
   <module>` or `git log -L`, and runs no mutant. `spec.md` *Rows whose code
   left the tree* already settles 30 rows this way; the phase does not
   re-run them.
3. **Write the pair.** One `--replace OLD NEW` that makes the change the
   sentence describes, at that decision point. Where two rows of the list
   produce the same pair, such as the round 3 comment's s9 and the body's
   "a target that is not a directory" in `hooks/session-lease.py`, they are
   one mutant, and the table says so.
4. **Run the before column.** One batch for the module's rows, against the
   module's test file at the phase's start, with `-x`:
   `bin/mutation-check <module> --replace ... --tests "bin/test tests/test_<stem>.py -q -x"`.
   A survivor there is run again against every other test file that loads
   the module, found with `git grep -l '<module path or stem>' -- tests/`.
   A mutant red anywhere is already closed, and the table names the case
   and its file.
5. **Write the case.** For each mutant that survives every file, add a case
   to the class of the function it changes (`spec.md` *In* item 2). See it
   red alone:
   `bin/mutation-check <module> --replace OLD NEW --tests "bin/test tests/test_<stem>.py -q -x -k <case name>"`
   prints `red` after a passing baseline. Contract rule 15 is met by that
   line, which the phase record quotes.
6. **Run the after column.** The same batch as step 4, at the module's
   commit, prints `red` for every mutant that stands.
7. **Confirm an equivalent row by reading.** For a row the records mark
   equivalent, read the code at the head. Write the reason no input tells
   the mutant apart, or, where an input does, treat the row as a gap from
   step 5.

The phase record's table has one row per issue row: the id or the
sentence, the pair as run, the before verdict with its file, the after
verdict with the killing case, and the outcome.

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The list's rows for `hooks/session-lease.py`, `hooks/hooksession.py`, `hooks/mode-gate.py`, `hooks/optin.py` and `hooks/routing.py`, each closed by one of the four outcomes, in one commit per module; `phases/phase-1.md` with each module's table | For each module, the before and after batches of *How a phase rebuilds a row*, and each new case's single-mutant `red` line, quoted in the phase record; `bin/test tests/test_session_lease.py tests/test_hooksession.py tests/test_mode_gate.py tests/test_optin.py tests/test_routing.py -q`; `bin/test-layout --check` and `--pairs` on each file the phase changed; `uvx ruff check` and `uvx ruff format --check` on the same files | 17e03fe5 |
| 2 | The same for `hooks/dispatch.py`, starting with the body's unclear row on `main`'s event name, then `hooks/console.py`, `hooks/implementer-mark.py`, `hooks/implementer.py` in the new `tests/test_implementer.py`, `hooks/implementer-notice.py`, `hooks/sealer-stamp.py`, `hooks/lint-python.py`, `hooks/version-check.py` and `hooks/review-skill-gate.py`; `phases/phase-2.md` | As phase 1, over `tests/test_dispatch.py tests/test_console.py tests/test_implementer_mark.py tests/test_implementer.py tests/test_implementer_notice.py tests/test_sealer_stamp.py tests/test_lint_python.py tests/test_version_check.py tests/test_review_skill_gate.py`; for `tests/test_implementer.py`, its census case passes | dbe80e99 |
| 3 | The same for `hooks/cmdline.py`'s seven standing rows (`spec.md` *Rows whose code left the tree*, last paragraph), `hooks/one_heredoc.py`, `hooks/tokens.py`, `hooks/blocks.py`, `hooks/worktree_consent.py` and `hooks/config.py`; `phases/phase-3.md` | As phase 1, over `tests/test_cmdline.py tests/test_one_heredoc.py tests/test_tokens.py tests/test_blocks.py tests/test_worktree_consent.py tests/test_config.py`; k25's before column also runs against `tests/test_worktree_guard.py` | bde49386 |
| 4 | The same for `skills/verify/scripts/session_cost.py`, whose cases stand only in `Test_<function>` classes placed in the module's function order (`spec.md` *Where the branches meet*), `skills/verify/scripts/broad_gate.py`, `skills/verify/scripts/mutation_check.py` and `skills/verify/scripts/pytest_record/specseal_pytest_record.py`'s two survivors; `phases/phase-4.md` | As phase 1, over `tests/test_session_cost.py tests/test_broad_gate.py tests/test_mutation_check.py tests/test_specseal_pytest_record.py`. The two pytest_record survivors' before column runs against every test file that reaches the recorder, as #942's round 2 named five | c2951650 |
| 5 | The same for `skills/code-review/scripts/chain_check.py` (the body's rows and the round 10 comment's c3 and c4), `skills/implement/scripts/seal.py`, `skills/settle/scripts/settle.py` (the round 3 comment's st rows and the round 10 comment's s4 and s5), `skills/settle/scripts/rule_changes.py` and `evals/scripts/seed_defects.py`; `phases/phase-5.md` | As phase 1, over `tests/test_chain_check.py tests/test_seal.py tests/test_settle.py tests/test_rule_changes.py tests/test_seed_defects.py`, with `--timeout` set above the chain_check baseline where it nears 300 s. `settle.py` and `rule_changes.py` were rewritten by `91d57028` and `fa7d1374` after #942 measured them, so step 2 decides each of their rows before any pair is written | 8ef4f419 |
| 6 | The same for `.github/scripts/issue_claims_check.py`, `.github/scripts/roll_flow_measurement_issue.py`, `.github/scripts/release_report.py` and the `tests/conftest.py` helpers (the body's seven rows and the round 3 comment's ch6), whose cases go in `tests/test_conftest.py`; `phases/phase-6.md` | As phase 1, over `tests/test_issue_claims_check.py tests/test_roll_flow_measurement_issue.py tests/test_release_report.py tests/test_conftest.py`. A conftest mutant runs against `tests/test_conftest.py` alone; h2's case runs from a working directory that is not the repository root | fea473fc |
| 7 | The same for `.github/scripts/close_issues_on_release.py`, with `gh_json` removed and c13 closed by that commit, `.github/scripts/label_merged_on_release_branch.py` and `.github/scripts/tracker_labels.py`; `phases/phase-7.md`; `changelog.md` from the outcomes the seven phase records state; `overview.md` closed | As phase 1, over `tests/test_close_issues_on_release.py tests/test_label_merged_on_release_branch.py tests/test_tracker_labels.py`; `git grep -n gh_json -- '*.py'` prints nothing; `git diff 134d7203 -- tests/` shows no removed line holding `def test_`, so no case was removed | cfdf2e7b |

## Operational impact

- **`.test_durations`.** No case is removed, so the file prices nothing the
  suite stops collecting. The new cases have no price until the file is
  refreshed. `test_the_durations_file_prices_the_suite` fails only when more
  than one collected case in twenty has none
  (`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#STALE_SHARE`).
  The orchestrator's broad gate runs that case. Where it fails, the
  orchestrator refreshes the file from the branch's `tests` run artifact as
  `CONTRIBUTING.md` describes, and commits it.
- **No new dependency, environment variable or migration.** One CI script
  loses a function nothing called.
- **A smith edits through the Edit and Write tools only.** No heredoc patch,
  no `sed -i`, and a commit is `git -C <worktree> add` and `git -C
  <worktree> commit` in commands of their own.
