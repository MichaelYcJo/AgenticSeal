# 1793057294-close-the-mutation-gaps-the-old-tests-had — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | dbe80e99 |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Phase 2 only: the rows of #1017 for `hooks/dispatch.py`, starting with the
body's unclear row on `main`'s event name, then `hooks/console.py`,
`hooks/implementer-mark.py`, `hooks/implementer.py` in a new
`tests/test_implementer.py`, `hooks/implementer-notice.py`,
`hooks/sealer-stamp.py`, `hooks/lint-python.py`, `hooks/version-check.py` and
`hooks/review-skill-gate.py`. Follow phase 1's method and table shape: rebuild
each row at the head with `bin/mutation-check` and `-x`, run a survivor again
against the other test files that load the module, write a case only where it
survives all of them, and see each new case red alone under its mutant. One
commit per module, then this record and phase 2's Status in `plan.md`. Build
on `questions.md`'s defaults Q1 to Q5. Every case gives the same verdict on
Linux, macOS and Windows.

## The outcomes

24 rows, rebuilt as 23 mutants. 18 rows are killed by a case seen red on its
mutant, 2 were already closed, 3 are equivalent, and 1 left the tree. No row
is a finding.

| Module | Commit | Rows | Mutants | Killed by a case | Already closed | Equivalent | Left the tree |
|---|---|---|---|---|---|---|---|
| `hooks/dispatch.py` | 8a02b2db | 2 | 3 | 1 | 1 | 0 | 0 |
| `hooks/console.py` | 3272afd2 | 1 | 1 | 1 | 0 | 0 | 0 |
| `hooks/implementer-mark.py` | ef719a13 | 1 | 1 | 1 | 0 | 0 | 0 |
| `hooks/implementer.py` | 1ca0540f | 2 | 2 | 2 | 0 | 0 | 0 |
| `hooks/implementer-notice.py` | 3800415b | 8 | 6 | 5 | 0 | 2 | 1 |
| `hooks/sealer-stamp.py` | e94d192e | 2 | 2 | 2 | 0 | 0 | 0 |
| `hooks/lint-python.py` | cc0de0be | 5 | 5 | 3 | 1 | 1 | 0 |
| `hooks/version-check.py` | ccfb2161 | 1 | 1 | 1 | 0 | 0 | 0 |
| `hooks/review-skill-gate.py` | dbe80e99 | 2 | 2 | 2 | 0 | 0 | 0 |

## How the tables read

The tables read as phase 1's do. Each pair is written as the zsh command line
passed it to `bin/mutation-check --replace`, and a `$'...'` string is ANSI-C
quoted, so `\n` in it is a newline.

The before column is the module's batch with `-x` in `--tests`, run when the
build reached the module: first against the module's own test file, then, for
each survivor, against every other test file that loads the module. The files
are listed above each table. The tree then differed from 36df3702 only by this
phase's earlier test commits, and every red verdict in another file names a
case that stood at 36df3702. `hooks/implementer.py` had no file of its own, so
its before column is one run over the files that reach it. The after column is
the same batch against the module's own file at the module's commit. Every
batch passed its baseline.

A new case was seen red alone on its mutant with
`bin/mutation-check <module> --replace OLD NEW --tests "bin/test tests/test_<stem>.py -q -x -p no:xdist -k <case>"`,
or with the case's node id in single quotes for a parametrized one. Each of
those runs printed `red: the cases failed against the mutation (exit 1)` after
a passing baseline.

## `hooks/dispatch.py`

Records: the issue body's two rows, `phases/phase-6.md:267` and `:486` at
`79f9c3fd`. Before: `tests/test_dispatch.py`, then
`tests/e2e/creation/test_creation_flow.py tests/test_a_gate_that_fails_says_so.py tests/test_a_rider_reaches_its_file.py tests/test_arm_check.py tests/test_chain_hooks_hardening.py tests/test_config.py tests/test_console.py tests/test_first_setup_asks_once.py tests/test_implementer_mark.py tests/test_implementer_notice.py tests/test_launch.py tests/test_mode_gate.py tests/test_one_word_one_meaning.py tests/test_question_gate.py tests/test_routing_edit_gate.py tests/test_routing.py tests/test_seal_stamp.py tests/test_sealer_stamp_queue.py tests/test_sealer_stamp.py tests/test_stub_remove.py tests/test_the_root_migrates_itself.py tests/test_the_rules_have_one_owner.py tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/test_worktree_consent.py tests/test_worktree_guard.py`,
with `tests/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`
deselected, because it fails until phase 7 writes `overview.md`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| body: `main` runs a known group's gates for an unknown group | `'gates = GROUPS.get(group)'` `'gates = GROUPS.get(group) or GROUPS["pre-bash"]'` | SURVIVED, every file | red, `Test_main::test_refuses_an_unknown_group_where_a_known_groups_gates_would_deny` | killed by a new case |
| body, unclear: `main`'s event name, first reading, `EVENTS` dropped | `'event_name = EVENTS.get(group) or ('` `'event_name = ('` | red on `tests/test_dispatch.py`, `Test_main::test_accepts_the_stop_group_and_names_its_event` | red, the same case | already closed |
| body, unclear: `main`'s event name, second reading, every group named `PostToolUse` | `'"PreToolUse" if group.startswith("pre-") else "PostToolUse"'` `'"PostToolUse"'` | SURVIVED on `tests/test_dispatch.py`; red on `tests/test_routing_edit_gate.py::Test_module::test_the_dispatcher_carries_the_refusal` | SURVIVED on `tests/test_dispatch.py`; the other file is unchanged | already closed |

## `hooks/console.py`

Records: the issue body's row, `phases/phase-6.md:268` at `79f9c3fd`. Before:
`tests/test_console.py`, then
`tests/test_censuses.py tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py tests/test_mode_gate.py tests/test_arm_check.py tests/test_dispatch.py tests/test_seal_stamp.py tests/test_routing.py tests/test_launch.py tests/test_worktree_guard.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| `to_utf8` leaves stdout unconfigured | `'(("stdin", "replace"), ("stdout", "replace"), ("stderr", "backslashreplace"))'` `'(("stdin", "replace"), ("stderr", "backslashreplace"))'` | SURVIVED, every file | red, `Test_to_utf8::test_accepts_each_of_the_three_streams_and_makes_it_utf8` | killed by a new case |

## `hooks/implementer-mark.py`

Records: the issue body's row, `phases/phase-6.md:322` at `79f9c3fd`. Before:
`tests/test_implementer_mark.py`, then
`tests/test_dispatch.py tests/test_implementer_notice.py tests/test_the_implementer_is_recorded.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| `main` takes a tool other than `Agent` or `Task` | `'if event.get("tool_name") not in ("Agent", "Task"):'` `'if False:'` | SURVIVED, every file | red, `Test_main::test_refuses_a_tool_other_than_agent_or_task_naming_smith` | killed by a new case |

## `hooks/implementer.py`

Records: the issue body's two rows, `phases/phase-6.md:323` at `79f9c3fd`.
Before, one run:
`tests/test_implementer_mark.py tests/test_implementer_notice.py tests/test_the_implementer_is_recorded.py tests/test_dispatch.py tests/test_sealer_stamp.py`.
After: the new `tests/test_implementer.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| `git_dir` answers on a non-zero exit | `'return (out.stdout or "").strip() if out.returncode == 0 else ""'` `'return (out.stdout or "").strip()'` | SURVIVED | red, `Test_git_dir::test_refuses_a_failed_git_whatever_it_printed` | killed by a new case |
| `write` writes an empty branch, a detached HEAD | `$'if not gd or not branch or not mark:\n        return False\n    try:\n        with open(os.path.join(gd, mark), "w"'` `$'if not gd or not mark:\n        return False\n    try:\n        with open(os.path.join(gd, mark), "w"'` | SURVIVED | red, `Test_write::test_refuses_an_empty_branch_and_writes_no_mark` | killed by a new case |

## `hooks/implementer-notice.py`

Records: the issue body's five rows, `phases/phase-6.md:324` at `79f9c3fd`,
and the round 3 comment's n1, n3 and n7, `phases/phase-6.md:1730` at
`fc4f81ae`. Before: `tests/test_implementer_notice.py`, then
`tests/test_dispatch.py tests/test_worktree_consent.py tests/test_the_implementer_is_recorded.py tests/test_cmdline.py tests/test_optin.py tests/test_arm_check.py tests/test_routing_edit_gate.py tests/test_first_setup_asks_once.py tests/e2e/creation/test_creation_flow.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| body: `commits` reads the command without dropping comments and heredoc bodies | `'split_segments(drop_heredoc_bodies(drop_comments(command)))'` `'split_segments(command)'` | SURVIVED, every file | red, `Test_commits::test_refuses_a_commit_that_is_only_a_heredoc_body` | killed by a new case |
| body: `already_told` takes a missing or dot session id | `'if not gd or not session or session in (".", ".."):'` `'if not gd:'` | SURVIVED, every file | red, `Test_already_told::test_refuses_a_missing_or_dot_session_id_and_records_nothing` | killed by a new case |
| body: `notify` skips the opt-in; round 3 n3, a repository that does not opt in is told, the same pair | `'if not top or not optin.opted_in(cwd):'` `'if not top:'` | SURVIVED, every file | SURVIVED | equivalent: `optin.opted_in(cwd)` is `bool(home_at(repo_root(cwd)))`, and `top` is `repo_root(cwd)`. Past the test, `routing.for_branch(top, branch)` calls `declarations(top)`, which asks the same `home_at(top)` and returns `[]` where it is falsy, so `for_branch` answers None and `notify` returns `""`. The mutant reaches that `""` after one more git call for the branch, and prints nothing either way |
| body: `main` takes a tool other than Bash | `'if payload.get("tool_name") != "Bash":'` `'if False:'` | SURVIVED, every file | red, `Test_main::test_refuses_a_tool_other_than_bash_whose_input_commits` | killed by a new case |
| body: the one-axis line's `no smith was spawned` | `'gone = f"no {missing[0][1]} was spawned on this branch"'` `'gone = "neither was spawned on this branch"'` | SURVIVED, every file | red, `Test_line::test_accepts_one_axis_and_says_its_agent_was_not_spawned` | killed by a new case |
| round 3 n1: the routing file is named by its absolute path | `'os.path.join(os.path.relpath(item, top), routing.FILENAME)'` `'os.path.join(item, routing.FILENAME)'` | SURVIVED, every file | red, `Test_notify::test_accepts_a_declared_smith_and_names_the_file_from_the_root` | killed by a new case |
| round 3 n7: a clone whose git hooks decide is told here too | no mutant | not run | not run | left the tree: `61a8455a` (#1027) removed `main`'s `githooks.decides` test and the `githooks` import, found with `git log -S githooks -- hooks/implementer-notice.py` |

## `hooks/sealer-stamp.py`

Records: the issue body's s4 and s8, `phases/phase-6.md:480` and `:484` at
`79f9c3fd`, with the ids from `rounds/round-3.md:229`. Before:
`tests/test_sealer_stamp.py`, then
`tests/test_dispatch.py tests/test_one_word_one_meaning.py tests/test_specseal_pytest_record.py tests/test_release_hygiene.py tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/test_sealer_stamp_queue.py tests/test_seal_stamp.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| s4: `drawings` draws no file before it claims it | `$'            stamp.stamp(values["rows"], shape=False)\n'` `''` | SURVIVED, every file | red, `Test_drawings::test_refuses_to_claim_a_file_that_reads_and_labels_but_does_not_draw` | killed by a new case |
| s8: `main` with no `if not session` test | `$'    if not session:\n        return\n    top'` `$'    if False:\n        return\n    top'` | SURVIVED, every file | red, `Test_main::test_refuses_a_stop_with_no_session_where_a_file_waits_for_none` | killed by a new case |

## `hooks/lint-python.py`

Records: the issue body's five rows, `phases/phase-6.md:101` at `79f9c3fd`.
Before: `tests/test_lint_python.py`, then `tests/test_dispatch.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| `resolve_runner`'s `uv` branch | `'if shutil.which("uv"):'` `'if False:'` | SURVIVED, every file | red, `Test_resolve_runner::test_accepts_uv_where_the_projects_environment_runs_ruff` | killed by a new case |
| `main`: a non-`.py` path gets past the suffix test | `'if not file.endswith(".py"):'` `'if False:'` | SURVIVED, every file | red, `Test_main::test_refuses_a_non_python_file_before_it_looks_for_a_runner`, given a `ruff.toml` | killed by a case given a ruff config |
| `main`: a missing runner | `$'    if not runner:\n        return\n'` `$'    if False:\n        return\n'` | SURVIVED, every file | SURVIVED, with `Test_main::test_refuses_quietly_where_no_runner_is_found` given a `ruff.toml` | equivalent: with `runner` None, `[*runner, *args, file]` raises `TypeError` while the list is built, before `subprocess.run` is called. That is inside the loop's `try`, whose `except Exception` swallows it, once per pass. Nothing runs and nothing escapes, as with the early return |
| `main`: the stdin payload | `'file = (json.load(sys.stdin).get("tool_input") or {}).get("file_path", "")'` `'file = ""'` | SURVIVED on `tests/test_lint_python.py`; red on `tests/test_dispatch.py::Test_run_gate::test_accepts_an_edit_and_hands_the_gate_its_file_not_the_group_name` | SURVIVED on `tests/test_lint_python.py`; the other file holds its case | already closed |
| `main`: a failing formatter | `$'        except Exception:\n            pass\n'` `$'        except ZeroDivisionError:\n            pass\n'` | SURVIVED, every file | red, `Test_main::test_refuses_to_let_a_failing_formatter_block_the_edit`, given a `ruff.toml` | killed by a case given a ruff config |

## `hooks/version-check.py`

Records: the issue body's row, `phases/phase-6.md:102` at `79f9c3fd`. Before:
`tests/test_version_check.py`, then
`tests/test_dispatch.py tests/test_optin.py tests/test_gather_changelog.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| `running` with no plugin root | `$'    if not root:\n        return None, None\n'` `$'    if False:\n        return None, None\n'` | SURVIVED, every file | red, `Test_running::test_refuses_no_plugin_root_whatever_the_cwd_holds` | killed by a new case |

## `hooks/review-skill-gate.py`

Records: the issue body's two rows, `phases/phase-6.md:103` at `79f9c3fd`.
Before: `tests/test_review_skill_gate.py`, then
`tests/test_one_word_one_meaning.py tests/test_optin.py tests/test_a_rider_reaches_its_file.py tests/test_dispatch.py`.

| Row | Pair as run | Before | After | Outcome |
|---|---|---|---|---|
| `git` returns output on a non-zero exit | `'return out.stdout.strip() if out.returncode == 0 else ""'` `'return out.stdout.strip()'` | SURVIVED, every file | red, `Test_git::test_refuses_a_failed_git_whatever_it_printed` | killed by a new case |
| a payload that is not an object | `$'    except (ValueError, AttributeError):\n        return\n\n    if skill'` `$'    except ValueError:\n        return\n\n    if skill'` | SURVIVED, every file | red, `Test_main::test_accepts_a_payload_that_is_no_object_silently`, each of its three parameters by node id | killed by a new case |

## What this phase found

**The unclear event-name row of `hooks/dispatch.py` has two readings, and
both are already closed (Q1).** #942's group 7 recorded one mutant at "the
event name" and kept no driver. The name is decided in two places: the
`EVENTS` lookup for `stop`, and the `pre-` prefix for every other group. Both
were run. Dropping `EVENTS` is red on `tests/test_dispatch.py`, on the case
group 13 placed there. Naming every group `PostToolUse` survives
`tests/test_dispatch.py` and is red on `tests/test_routing_edit_gate.py`,
whose case reads the `hookEventName` of the `pre-edit` group's refusal. Each
reading has its own line in the table, so the row closes on either.

**Two `hooks/lint-python.py` rows are killed by an existing case given a ruff
config, not by an added case.** The record says why they survived: the cases
for a non-`.py` path, a missing runner and a failing formatter built no ruff
config, so `uses_ruff` returned before the decision each case names. A new
case beside each would assert what the old one meant to assert, so each old
case gets a `ruff.toml` instead. `spec.md` *In* item 1 says the case for a
standing gap "is added". This is a divergence for phase 7's `overview.md`:
the spec says a case is added, and the build gave an existing case the input
it lacked, on the rule that a case covering nothing its group does not
already cover is not added. With the config, the missing-runner case reaches
its branch and the mutant still survives, which is how the row was read as
equivalent.

**Three rows rest on a guarantee their caller gives, and their cases remove it
(contract rule 13).** Two are git's: `hooks/implementer.py#git_dir` and
`hooks/review-skill-gate.py#git` on a non-zero exit, where the real git
prints nothing on stdout, so each case fakes a failed git that printed a
path, as phase 1 did. The third is s4 of `hooks/sealer-stamp.py`. Every file
the shipped `seal_stamp.read_values` accepts also draws, because its rows are
`None` or pairs of strings, and `stamp` draws any such row. So with the
shipped module the draw before the claim cannot fail, and s4 is equivalent.
The case hands `drawings` a stand-in for the module whose draw fails for one
file's rows, and asserts that file stays pending. A warden who reads s4 as
equivalent with the shipped module can rebuild the pair from the table.

**s4's first case passed under its mutant, and was rewritten until it went
red.** The bad file was the newer of two, and one message carries only the
oldest seal, so under the mutant the bad file was never admitted and nothing
claimed it. The case now makes the bad file the older one. This is the reason
contract rule 15 asks for the red run.

**The two notice rows on the opt-in are one pair (Q2).** The body's "`notify`
skips the opt-in" and round 3's n3 rebuild as the same replacement at the
head, and it is equivalent, for the reason the table gives.

**`hooks/implementer.py`'s census passes on `tests/test_implementer.py`
(Q3).** No line of the module was changed. `bin/test-layout --check` reports
`mark_for` and `stands` with no class; their cases stay with the two hooks'
files, as the new file's docstring says.

**The formatter hook dropped two imports again.** `io` and `sys` went into
`tests/test_review_skill_gate.py` in an `Edit` before the code that used
them, and the hook removed both. The seen-red run then stopped at `no
baseline` with a `NameError`, and the imports were added again once the code
stood. The lesson phase 1 wrote holds: add an import in the same `Edit` as its
first use.

**No case reads the platform, the process tree or the console without a
fake.** The console case hands `to_utf8` three cp949 text streams in place of
`sys.stdin`, `sys.stdout` and `sys.stderr`. The `resolve_runner` cases fake
`shutil.which` and the `uv run ruff --version` probe. The version-check case
sets `CLAUDE_PLUGIN_ROOT` and the working directory, and no case starts a
process whose verdict depends on the leg.

**Run for the phase** (`executed`, at dbe80e99):
`bin/test tests/test_dispatch.py tests/test_console.py tests/test_implementer_mark.py tests/test_implementer.py tests/test_implementer_notice.py tests/test_sealer_stamp.py tests/test_lint_python.py tests/test_version_check.py tests/test_review_skill_gate.py -q`
exited 0, 184 passed. `bin/test-layout --check` over the nine files reads 9
files with 0 refused, and `--pairs` prints one pair, `tests/test_review_skill_gate.py::Test_main`'s,
which #942's records name and give their reason for. `uvx ruff check` and
`uvx ruff format --check` over the same files exit 0.
