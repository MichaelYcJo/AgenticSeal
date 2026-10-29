# Phase 1: 1793240967-the-worktree-guard-was-never-weighed

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | ec43e94b |

## What this phase was asked

Build `frame/plan.md` *Phases* row 1 and nothing of rows 2 to 4. Move the `automation` press reader out of `hooks/worktree_consent.py` into `hooks/lib/press.py`, byte for byte, below a module docstring that names no guard. Make `hooks/question-gate.py` and `hooks/routing-edit-gate.py` import `press`. Keep the guard working until phase 2 by having `hooks/worktree_consent.py` import the moved names from `press`. Move the press cases to `tests/hooks/test_press.py` together with the labels case of `tests/behaviour/test_the_guard_asks_once_per_session.py`, and point the `PROJECTS_ROOT` patches of `tests/conftest.py` at `press`. Decide `frame/questions.md` W2 and record the decision here. Touch none of `skills/implement/orchestration.md`, `skills/implement/SKILL.md`, `hooks/mode-gate.py` and `tests/censuses.py`, which sibling work items edit. The move is proved by the moved cases passing at the new path; no new red-first case is owed.

## What this phase found

**The frame holds, with two coordinates missing from it.** `frame/plan.md` *Technical context* names the two `PROJECTS_ROOT` patches in `tests/conftest.py`. Two more cases patched `worktree_consent.PROJECTS_ROOT` at `7a3d76c3`: `tests/hooks/test_worktree_guard.py` in the `press` method of its guard helper, and the `projects` fixture of `tests/hooks/test_worktree_consent.py`. Once `transcript_for` lives in `press`, a patch on `worktree_consent` no longer reaches the reader. All four sites now patch `sys.modules["press"]` or the unit copy. `hooks/worktree_consent.py` keeps no `PROJECTS_ROOT`, so a patch still aimed at it raises `AttributeError` rather than patching nothing.

**W2 is decided as its default.** Both the moved press cases and the labels case stand in `tests/hooks/test_press.py`, the labels case in `Test_module`. `bin/seal layout --check tests/hooks/test_press.py` refuses nothing (executed, exit 0). It reports four public functions with no class of their own: `is_routing_question`, `last_routing_answer`, `leading_phrase` and `transcript_for`. Those functions had no class in the old file either. `tests/behaviour/test_the_guard_asks_once_per_session.py` held only the labels case, so it was deleted.

**The move is shown by two diffs, not by `seal layout --moved`.** Lines 27 to the end of `hooks/lib/press.py` equal lines 101 to 117 and 152 to 401 of `hooks/worktree_consent.py` at `7a3d76c3` (executed, `diff` exit 0). The 22 cases of `Test_automation_answered` and `Test__routing_preset` equal their old text once `wc.` is read as `press.`, except for the five `consent` assertions `gaps.md` records (executed, `diff`). The three `Test_module` cases and the labels case changed more, by reading: `test_no_case_reads_the_real_projects_root` reads a gate's copy of `press` in place of the guard's copy of `worktree_consent`, and `test_the_press_reader_reads_nothing_for_a_root_that_is_no_clone` calls the unit copy in place of a fresh copy of `worktree_consent`. `bin/seal layout --moved HEAD` refuses the move (executed, exit 1), because it compares case bodies literally and the module's alias changed in every body.

**`hooks/worktree_consent.py` imports two names from `press`, each with a redundant alias.** They are `automation_answered`, which `consent` calls, and `_clone_of`, which only the guard reads off this module. The `as` form marks each as a re-export for ruff, which would otherwise drop `_clone_of` as unused. The names are bound into this module rather than called as `press.automation_answered`. That keeps `consent` calling the name the guard's cases patch on `worktree_consent`. Phase 2 deletes both lines with the file.

**`hooks/routing-edit-gate.py` now imports `press` at the top of the module.** It used to import `worktree_consent` inside `decide`, which kept `hooks/lib/cmdline_base.py` (2,288 lines) off the path an allowed edit takes. `press` imports `glob`, `json`, `os` and `optin` only, so that reason no longer holds. A module-level import also means the first case of a test module finds `press` in `sys.modules` before the autouse fixture in `tests/conftest.py` runs. A deferred import would miss that fixture on its first case.

**The repository's PostToolUse lint hook rewrites imports between `Edit` calls.** `hooks/lint-python.py` runs `ruff check --fix` after each edit. It deleted `import press` from `hooks/question-gate.py` because that edit landed before the call sites used the name, and the import was added back. A crafter who edits an import and its uses in separate calls should change the uses first.

**Mutation runs, after the commit (executed, each exit 0 with the verdict red, and the file restored by `seal mutate`):**

- `hooks/lib/press.py`, clone check made always true, and `PRESET` set to `per axis`, against `tests/hooks/test_press.py`: 2 mutants, 2 red.
- `automation_answered` made to return `False`, against `tests/hooks/test_routing_edit_gate.py`: red, 2 cases failed.
- `is_routing_question` made to return `False`, against `tests/hooks/test_question_gate.py`: red, 2 cases failed.

**What phase 2 needs to know.**

- `hooks/lib/press.py` still names the guard in its moved docstrings. The docstring of `last_routing_answer` names `[worktree-ok]`, "the record as consent", the guard's deny and `consent`'s catch-all. It also cites `docs/worktree-guard-spec.md` *Creation consent*. `tests/behaviour/test_a_cited_section_stands_in_its_file.py` reads citations in `.py` files, so that citation dangles in the commit that deletes the document. Whichever phase deletes the document rewrites that docstring in the same commit.
- `tests/hooks/test_press.py` carries the guard in four moved docstrings. They are `test_accepts_question_1_alone_and_the_boxes_beside_it_as_the_same_press`, `test_refuses_a_typed_answer_that_qualifies_the_preset`, `test_refuses_both_shapes_that_raised_without_raising` (it names `consent`'s catch-all) and `test_the_labels_match_the_routing_question_the_orchestrator_asks`. None of them matches the sweep command of `frame/design.md` *Data & interfaces*, so the sweep will not find them.
- The `projects` fixture in `tests/conftest.py` now patches `sys.modules["press"]`. Its only user is `tests/hooks/test_worktree_guard.py` (read, `git grep`), so it goes with that file. The autouse fixture `_no_real_transcripts` stays, because it keeps the gates' copy of `press` off a real `~/.claude/projects`, and `tests/hooks/test_press.py#Test_module::test_no_case_reads_the_real_projects_root` reads it.
- `.test_durations` still holds the 26 keys of the moved cases' old ids (`gaps.md` *Not done*). They belong with the timing entries phase 2 removes.
- `hooks/question-gate.py` no longer loads `hooks/lib/cmdline_base.py`. The broken-module cases in `tests/hooks/test_dispatch.py` dispatch only `pre-bash` and `post-bash`, so none of them names `question-gate.py` (read). Phase 2 rewrites them without the guard.
- `hooks/question-gate.py`'s docstring still says the worktree guard never reads `routing.md` as consent. That sentence is phase 4's.
