# Phase 4: 1792628098-tests-rebuilt-one-file-per-module

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 4496bb0f |

## What this phase was asked

Each helper defined byte-identically in two or more test files is defined once, in `tests/conftest.py`. The phase's first step is `bin/test-layout --check`, which lists the twins. The phase is done when the check names no twin, and each touched file passes `bin/test <file> -q`.

## What this phase found

**Measured at 1136e7ac, before the first edit** (`executed`). `bin/test-layout --check` reports 46 twin groups, 141 definitions in all. The most copied names are `read` (5 groups, 39 definitions), `flat` (6 groups, 16), `git` (5 groups, 10) and `opt_in` (1 group, 6). The frame counted 46 groups and 141 definitions at a16acb40 too.

**Whether the frame holds.** It holds. One name often held more than one body, so a group could not move under its own name alone, and the build settled each case this way.

- Where two groups under one name did the same thing, they became one helper. The five `read` groups differed only in the variable's name and in taking a path or path parts, and `read(*parts)` joined under the repository root reads an absolute path where it stands, so all five read through one `read`. The same holds for the six `flat` groups that read a file, the two `q` groups, the two `write` groups and three of the five `git` groups.
- Where two groups under one name did different things, each got a name of its own in `tests/conftest.py`, and a module imports it under the name its cases already call: `git_out as git` for the `git` that returns its output, `flattened as flat` for the `flat` that takes text, `commit_everything` and `commit_everything_as_e` for the two `commit` groups.
- Three helpers read a module the case loaded itself: `check` reads the chain check, `found` reads the commit gate, and `decide` reads the worktree guard. Each conftest helper takes that module as its first argument, and the case's module binds it with `functools.partial`. A partial is an assignment, so the layout check reads no definition there.
- Two fixtures needed no helper at all. `_installer_writes` was an autouse fixture whose body was its docstring; the two modules now name `git_hooks_installed` in `pytestmark`. The two `repo` fixtures copied a template exactly as `tests/conftest.py#repo` does, so each module now names its template `_repo_template`, which conftest's `repo` copies.
- The `load(path, name)` and `_load(name, path)` groups took their arguments in opposite orders. `tests/conftest.py#load_module` takes `(path, name)`, `load_hook_module`'s order, and the 21 `_load` calls were rewritten to it.
- `payload` lost its `tool` and `**extra` parameters: no case passes either, and a mutation of `**extra` survived every caller.

**What changed and what did not** (`executed`). 28 helpers in `tests/conftest.py` replace 141 definitions in 87 modules. `bin/test-layout --check` names no twin and ends `test-layout: 145 files read, 0 refused, 141 declare no TARGET`, and `--pairs` prints 0 pairs. Two behaviours moved by a hair, and neither is reached by a case today. `test_the_sealer_guarantees.py`'s `commit` called a `git` that decoded output strictly, and `commit_everything` decodes with `errors="replace"`. `linked_worktree` now captures git's output as text where it captured bytes. `tests/conftest.py`'s docstring still named the case ceiling phase 2 removed, and this phase's commit corrects it. One loop variable in `tests/test_the_guard_asks_once_per_session.py` was named `dirty` and shadowed the imported helper; it is `changed` now.

**The mutation table** (`executed`). Each moved helper was broken once in `tests/conftest.py`, with the modules that call it as the command.

| # | Mutation | Modules run | Verdict |
|---|---|---|---|
| h1 | `load_module` with its two names swapped | `test_a_document_has_room_for_the_next_fold.py` | red |
| h2 | `read` not joined under the repository root | `test_the_handoff_before_round_one.py` | SURVIVED |
| h3 | `flattened` returning its text unchanged | `test_settle_reads_before_it_removes.py` | red |
| h4 | `git` always checking the exit code | `test_the_mode_is_a_row_and_a_command.py` | SURVIVED |
| h5 | `git_out` not stripped | `test_chain_check.py` | red |
| h6 | `commit_everything_as_e` without its identity | `test_the_gate_asks_the_range_ci_will_ask.py` | SURVIVED |
| h7 | `branch_of` asking for the commit, not the branch | `test_routing_is_recorded.py` | red |
| h8 | `git_dir` relative | `test_chain_hooks.py` | red |
| h9 | `write` making no directories | `test_pact_check.py` | red |
| h10 | `opt_in` doing nothing | `test_version_check.py` | red |
| h11 | `dirty` changing nothing | `test_the_guard_asks_once_per_session.py` | red |
| h12 | `imported_roots` not marking a relative import | `test_the_hooks_hide_what_a_renderer_hides.py`, `test_one_table_walker_reads_what_gfm_renders.py` | SURVIVED |
| h13 | `iso` in the future | `test_lease_liveness.py` survived, `test_worktree_guard_signals.py` red | red |
| h14 | `q` not quoting | `test_no_shape_the_base_stops_reads_silent.py`, `test_one_heredoc_shape_is_data_to_the_commit_gate.py` | SURVIVED |
| h15 | `payload`'s extras dropped | `test_chain_hooks.py`, `test_the_mode_question_is_asked_once.py` | SURVIVED, and the parameters removed |
| h16 | `reason_of` reading the decision | `test_local_mode_resolves_under_the_git_dir.py` | red |
| h17 | `run_gate` dropping the session | `test_gate_judges_the_repo_it_commits_to.py` | red |
| h18 | `config_table` without its header | `test_a_reference_root_is_read_and_never_taken.py` | red |
| h19 | `chain_check_run` without its baseline | `test_the_sealer_guarantees.py` | red |
| h20 | `commit_found` returning the list | `test_a_commit_behind_a_reserved_word_is_judged.py` | red |
| h21 | `guard_decision`'s silent answer renamed | `test_lease_liveness.py`, `test_worktree_guard_signals.py` | SURVIVED |
| h22 | `projects` patching nothing | `test_a_creation_in_another_clone_asks_nobody.py` | red |
| h23 | `repo_relative` returning the base name | `test_every_agent_reads_the_contract.py`, `test_a_moved_rule_leaves_its_definition.py` | SURVIVED |
| h24 | `linked_worktree` adding no worktree | `test_optin_home.py` | red |
| h25 | `payload` ignoring its session | `test_chain_hooks.py`, `test_the_mode_question_is_asked_once.py` | red |

The helpers were moved, not written, and each survivor survived every module that had defined the twin. They are gaps the old modules already had. h2 survives because `bin/test` runs from the repository root, so a path relative to the root and to the working directory are one path. h6 survives because the suite's environment gives git an identity. h4, h12, h14, h21 and h23 name branches no case reaches: a failing git call with checking off, a relative import, a path that needs quoting, a silent guard, and a nested path. Each belongs to the batch that rebuilds the module whose cases would reach it, phases 5 and 6. `git status` was clean after every run.

**The phase boundary** (`executed`, at 4496bb0f). One `bin/test ... -q` over 118 modules: the 87 this phase edited, phase 1's 69, and the four layout modules. 6,515 passed, 14 skipped and 1 failed in 270 s of wall time. The failure is the overview census, as at phases 1 to 3. No case was named slow. `bin/rules --check`, `bin/unverified-check seal/specs/` and `chain_check.py --baseline release/v0.22.3 --worktree` each exit 0.
