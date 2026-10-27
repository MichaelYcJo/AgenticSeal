# 1793057294-close-the-mutation-gaps-the-old-tests-had — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 17e03fe5 |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Phase 1 only: the rows of #1017 for `hooks/session-lease.py`,
`hooks/hooksession.py`, `hooks/mode-gate.py`, `hooks/optin.py` and
`hooks/routing.py`. For each row, rebuild the mutant at the head with
`bin/mutation-check` and record the one outcome `spec.md` allows: left the
tree, already closed with the killing case, killed by a new case seen red on
its mutant, equivalent with the reason from the code, or a finding under
`questions.md` Q4. One commit per module. Then write this record with each
module's table and set phase 1's Status in `plan.md`. Build on `questions.md`'s
defaults Q1 to Q5. Every case gives the same verdict on Linux, macOS and
Windows.

## The outcomes

25 rows, rebuilt as 23 mutants. 21 rows are killed by a new case, 1 was
already closed, 3 are equivalent. No row left the tree, and no row is a
finding.

| Module | Commit | Rows | Mutants | Killed by a new case | Already closed | Equivalent |
|---|---|---|---|---|---|---|
| `hooks/session-lease.py` | cdc77738 | 10 | 8 | 10 | 0 | 0 |
| `hooks/hooksession.py` | 5ed03d99 | 3 | 3 | 1 | 0 | 2 |
| `hooks/mode-gate.py` | 010164e5 | 4 | 4 | 3 | 0 | 1 |
| `hooks/optin.py` | 50a2293b | 5 | 5 | 4 | 1 | 0 |
| `hooks/routing.py` | 17e03fe5 | 3 | 3 | 3 | 0 | 0 |

## How the tables read

Each pair is written as the zsh command line passed it to `bin/mutation-check
--replace`. A `$'...'` string is ANSI-C quoted, so `\n` in it is a newline. A
`\|` in a cell stands for `|`, escaped so the table keeps its columns.

The before column is the module's batch at `a24c883a`, with `-x` in
`--tests`, first against the module's own test file and then, for each
survivor, against every other test file that loads the module. The files are
listed above each table. The after column is the same batch against the
module's own file at the module's commit. Every batch passed its baseline.

A new case was seen red alone on its mutant with
`bin/mutation-check <module> --replace OLD NEW --tests "bin/test tests/test_<stem>.py -q -x -p no:xdist -k <case>"`,
or with the case's node id in place of `-k` for a parametrized one. Each of
those runs printed `red: the cases failed against the mutation (exit 1)` and
exited 0, so its baseline passed against the code.

## `hooks/session-lease.py`

Records: the issue body's six rows, `phases/phase-6.md:163` at `79f9c3fd`, and
the round 3 comment's s6, s9, s10 and s12, `phases/phase-6.md:1711` at
`fc4f81ae`. Before: `tests/test_session_lease.py`, then
`tests/test_dispatch.py tests/test_seal.py tests/test_hooksession.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| body: a tool other than Bash and the editors is taken as Bash | `'elif tool == "Bash":'` `'elif True:'` | SURVIVED, every file | red, `Test_main::test_refuses_a_tool_that_is_neither_bash_nor_an_editor` | killed by a new case |
| body: a target that is not a directory; round 3 s9, the same pair | `'if not target or not os.path.isdir(target):'` `'if not target:'` | SURVIVED, every file | red, `Test_main::test_refuses_a_target_that_is_no_directory_whatever_git_answers` | killed by a new case |
| body: `git_dir` answers nothing outside a repository; round 3 s10, the same pair | `$'    if not gd:\n        return'` `$'    if False:\n        return'` | SURVIVED, every file | red, `Test_main::test_refuses_a_call_outside_any_repo_without_raising` | killed by a new case |
| body: `git_dir` answers on a non-zero exit | `'return r.stdout.strip() if r.returncode == 0 else None'` `'return r.stdout.strip()'` | SURVIVED, every file | red, `Test_git_dir::test_refuses_a_failed_git_whatever_it_printed` | killed by a new case |
| body: the session id is joined without `basename` | `'session = os.path.basename(payload.get("session_id", ""))'` `'session = payload.get("session_id", "")'` | SURVIVED, every file | red, `Test_main::test_accepts_a_session_id_with_a_separator_and_files_it_by_its_basename` | killed by a new case |
| body: the write's `OSError` is let through | `$'        pass\n    except OSError:\n        pass\n'` `$'        pass\n    except ZeroDivisionError:\n        pass\n'` | SURVIVED, every file | red, `Test_main::test_refuses_to_raise_where_the_lease_directory_cannot_be_made` | killed by a new case |
| round 3 s6: a notebook edit is not taken as an edit | `'("Write", "Edit", "NotebookEdit")'` `'("Write", "Edit")'` | SURVIVED, every file | red, `Test_main::test_accepts_a_notebook_edit_and_leases_the_notebooks_repo` | killed by a new case |
| round 3 s12: an error reading the owner other than `OSError` is caught | `$'    except Exception:\n        pid = None'` `$'    except OSError:\n        pid = None'` | SURVIVED, every file | red, `Test_main::test_refuses_to_record_a_pid_when_reading_the_owner_raises` | killed by a new case |

## `hooks/hooksession.py`

Records: the round 3 comment's h3, h4 and h8, `phases/phase-6.md:1711` at
`fc4f81ae`. Before: `tests/test_hooksession.py`, then
`tests/test_session_lease.py tests/test_worktree_guard.py tests/test_tokens.py tests/test_seal.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| h3: the ancestor walk passes pid 1 | `'if pid is None or pid <= 1:'` `'if pid is None or pid < 1:'` | SURVIVED, every file | red, `Test_claude_ancestor::test_refuses_pid_1_even_where_it_is_named_claude` | killed by a new case |
| h4: an empty `ps` answer is walked on | `$'        if not out:\n            return None'` `$'        if False:\n            return None'` | SURVIVED, every file | SURVIVED | equivalent: an empty answer partitions into an empty parent and an empty name. `is_claude("")` is false, and `int("")` raises `ValueError`, whose handler returns None. That is the None the skipped test returns, in the same pass and with no further `ps` call |
| h8: an unreadable parent is walked as pid 0 | `$'        except ValueError:\n            return None'` `$'        except ValueError:\n            pid = 0'` | SURVIVED, every file | SURVIVED | equivalent: pid 0 meets the floor `pid <= 1` at the top of the next pass, which returns None. Where the pass was the last one, the loop ends and the function returns None. No `ps` call is made for pid 0 either way |

## `hooks/mode-gate.py`

Records: the issue body's four rows, `phases/phase-6.md:191` at `79f9c3fd`.
Before: `tests/test_mode_gate.py`, then
`tests/test_config.py tests/test_dispatch.py tests/test_first_setup_asks_once.py tests/test_one_word_one_meaning.py tests/test_the_mode_question_is_asked_once.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| `already_asked`: a session id of `.` or `..` | `'if not git_dir or not session or session in (".", ".."):'` `'if not git_dir or not session:'` | SURVIVED, every file | red, `Test_already_asked::test_refuses_a_dot_session_id_as_asked_and_records_nothing` | killed by a new case |
| `undeclared` answers the falsy home it was given in place of `""` | `$'    if not home:\n        return ""\n    kind'` `$'    if not home:\n        return home\n    kind'` | SURVIVED, every file | SURVIVED | equivalent: `home` is `optin.home_at`'s answer, and every return of `home_at` is either `""` or a path that passed `if found`. So a falsy `home` is always `""`, and `return home` returns `""` |
| `git_dir_of` answers on a non-zero exit | `$'    if done.returncode != 0:\n        return ""'` `$'    if False:\n        return ""'` | SURVIVED, every file | red, `Test_git_dir_of::test_refuses_a_failed_git_whatever_it_printed` | killed by a new case |
| `main`: the question's first sentence leaves out the root's path | `'f"{root} runs the SpecSeal workflow — its root is at {home} — and "'` `'f"{root} runs the SpecSeal workflow and "'` | SURVIVED, every file | red, `Test_main::test_refuses_with_a_first_paragraph_that_names_the_root` | killed by a new case |

## `hooks/optin.py`

Records: the issue body's five rows, `phases/phase-6.md:350` at `79f9c3fd`.
Before: `tests/test_optin.py`, then
`tests/test_a_rider_reaches_its_file.py tests/test_a_shrunken_corpus_declines_to_judge.py tests/test_chain_check.py tests/test_config.py tests/test_dispatch.py tests/test_first_setup_asks_once.py tests/test_fold_check.py tests/test_mode_gate.py tests/test_optin_home.py tests/test_question_gate.py tests/test_root_migrate.py tests/test_routing.py tests/test_routing_edit_gate.py tests/test_seal.py tests/test_sealer_stamp.py tests/test_settle.py tests/test_the_pull_request_language_is_the_repositorys.py tests/test_worktree_consent.py tests/test_worktree_guard.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| `repo_root` asks git for a path that is not a directory | `'if not cwd or not os.path.isdir(cwd):'` `'if not cwd:'` | SURVIVED, every file | red, `Test_repo_root::test_refuses_a_path_that_is_no_directory_whatever_git_answers` | killed by a new case |
| `repo_root` answers git's spelling without `normpath` | `'return os.path.normpath(out) if out else ""'` `'return out if out else ""'` | SURVIVED, every file | red, `Test_repo_root::test_accepts_gits_answer_in_this_platforms_spelling` | killed by a new case |
| `home_paths` asks git when the caller passed the common directory | ``$'    if common is None:\n        common = git_common_dir(root)\n    # `normpath`'`` ``$'    if True:\n        common = git_common_dir(root)\n    # `normpath`'`` | SURVIVED on `tests/test_optin.py`; red on `tests/test_settle.py::Test_main::test_the_refusal_path_asks_for_the_common_directory_once` | red, `Test_home_paths::test_accepts_a_passed_common_directory_in_this_platforms_spelling` | already closed |
| `home_paths` leaves the local place unnormalised | `'os.path.normpath(os.path.join(common, HOME)) if common else ""'` `'os.path.join(common, HOME) if common else ""'` | SURVIVED, every file | red, `Test_home_paths::test_accepts_a_passed_common_directory_in_this_platforms_spelling` | killed by a new case |
| `parity_config` reads a repository with no root | `$'    root = home(cwd)\n    if not root:\n        return ""'` `$'    root = home(cwd)\n    if False:\n        return ""'` | SURVIVED, every file | red, `Test_parity_config::test_refuses_a_repository_with_no_root_whatever_the_cwd_holds` | killed by a new case |

## `hooks/routing.py`

Records: the issue body's three rows, `phases/phase-6.md:298` at `79f9c3fd`.
Before: `tests/test_routing.py`, then
`tests/test_a_reference_root_is_read_and_never_taken.py tests/test_a_section_marked_for_one_role_reaches_only_that_role.py tests/test_chain_check.py tests/test_config.py tests/test_question_gate.py tests/test_routing_is_recorded.py tests/test_seal.py tests/test_settle.py tests/test_settle_reads_before_it_removes.py tests/test_the_hooks_hide_what_a_renderer_hides.py tests/test_waiver_decided_at_start.py tests/test_release_seal.py tests/test_implementer_mark.py tests/test_implementer_notice.py tests/test_routing_edit_gate.py tests/test_broad_gate.py tests/test_unverified_check.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| `table_rows` reads a line that does not start with a pipe | `$'        if not line.startswith("\|"):\n            continue'` `$'        if False:\n            continue'` | SURVIVED, every file | red, `Test_table_rows::test_refuses_a_line_that_is_no_two_cell_row[no-leading-pipe]` | killed by a new case |
| `table_rows` reads a one-cell row | `'if len(cells) < 2:'` `'if len(cells) < 1:'` | SURVIVED, every file | red, `Test_table_rows::test_refuses_a_line_that_is_no_two_cell_row[one-cell]` | killed by a new case |
| `declarations` reads a repository with no `seal/` as its own root | `$'    home = optin.home_at(root)\n    if not home:\n        return []'` `$'    home = optin.home_at(root)\n    if False:\n        return []'` | SURVIVED, every file | red, `Test_declarations::test_refuses_a_repository_with_no_root_whatever_the_cwd_holds` | killed by a new case |

## What this phase found

**Two pairs of rows are one mutant each (Q2).** In `hooks/session-lease.py`,
the body's directory-test row and round 3's s9 rebuild as the same pair, and so
do the body's "`git_dir` answers nothing outside a repository" and round 3's
s10. The reading behind the second (Q1, default (a)): #942's site list at
`79f9c3fd` names `main`'s "git directory test" beside `git_dir`'s exit, and
its `--absolute-git-dir` mutant was among the red ones. So the row that
answers nothing outside a repository is `main`'s `if not gd` test. Without it,
`os.path.join(None, ...)` raises. The old case for a call outside a repository
ran the hook as a subprocess and read only its stdout, so the traceback on
stderr passed it.

**Four rows rest on a guarantee the real git gives, and their cases fake git
(contract rule 13).** The body's non-zero-exit rows for
`hooks/session-lease.py#git_dir` and `hooks/mode-gate.py#git_dir_of`: the real
git prints nothing on stdout when it fails. The two directory-test rows for
`session-lease`'s target and `optin.repo_root`: the real git refuses a path
that is no directory, and so does `subprocess.run`'s `cwd`. Read against the
real git alone, all four are equivalent. Each case replaces git with an answer
for any path, or a failure that still printed one, and asserts the function's
own answer. A warden who reads "equivalent with the real git" as the outcome
the spec meant can rebuild each pair from the tables.

**`optin`'s `normpath` rows need a spelling `normpath` changes on every
platform.** The real git answers with forward slashes, which `normpath`
changes only on Windows, so a case built on git's real answer is red on one CI
leg alone. The cases use a `..` segment instead, which `normpath` folds on
every platform.

**The case written for `home_paths`' unnormalised local place also kills the
`home_paths` row that was already closed.** That row was red at the start on
`tests/test_settle.py` and got no case of its own. The `normpath` case passes
a common directory other than the repository's, which the mutant ignores.
`tests/test_optin.py` now kills both.

**`bin/test-layout --pairs` named the two `table_rows` refusals as one pair,
so they are one parametrized case.** Each parameter was seen red alone on its
own mutant, by node id. The other pairs `--pairs` prints for these files
(`tests/test_optin.py::Test_module`'s review-skill-gate pair and
`tests/test_routing.py::Test_parse`'s pair) were there before this phase,
and #942's records give their reasons. `bin/test-layout --check` exits 0 on
all five files, and its `report:` lines name public functions with no class
yet. Adding those classes is a sweep, which `spec.md` *Out* leaves to another
item.

**A formatter hook in this session drops an import the file does not use
yet.** An `Edit` that adds an import before the code that uses it loses the
import when the hook runs. Add the import in the same `Edit` as its first use,
or after it.

**In zsh, `$N[...]` inside double quotes is a subscript, not a node id.** Two
seen-red runs built their `--tests` that way, so `bin/test` got no node id and
started the whole suite with `-x`, as each baseline. Each stopped after 1,313
passed at
`tests/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
which fails because this work item has no `overview.md`. `plan.md` gives
`overview.md` to phase 7, and the orchestrator's broad gate meets that case
before then if no earlier phase opens it. Neither run was a gate run, and
neither measured anything for this phase. The next phase writes node ids in single
quotes.

**No case reads the platform, the process tree or the console without a
fake.** The process tree goes through `conftest.stub_process_tree`. The
unmade lease directory is a FILE where the directory goes, because a mode bit
does not stop a write on Windows. No case reads stdin text that carries a
newline.
