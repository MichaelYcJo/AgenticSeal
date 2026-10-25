# Phase 2: 1792935671-the-routing-check-moves-to-the-sessions-tools

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | d132a312 |

## What this phase was asked

Build phase 2 of `plan.md` *Phases*: the edit check. Write `hooks/routing-edit-gate.py`, a `PreToolUse` `Write|Edit|NotebookEdit` entry in `hooks/hooks.json` and the `pre-edit` group, `seal no-work-item` in `skills/implement/scripts/seal.py`, and the deny texts. `skills/implement/orchestration.md` *Orchestrator: how the work is routed* and `skills/implement/SKILL.md` *1. Read the spec before the code* name the check and `seal no-work-item`. Nothing is removed. Verify with `tests/test_routing_edit_gate.py` (S1 to S8), `tests/test_seal.py` and `tests/test_dispatch.py`, each case seen red first. Build `questions.md` Q2's default (a): the model may run `seal no-work-item`. Answer Q4: measure the median latency the gate adds per edit and write it here. Record Q3 as unverified, with the owner as its answerer after an installed release, because the plugin loaded in this run is the installed 0.22.3 copy and the tree's new hook runs in no session of the run. Run tests with `bin/test -n auto -q <files>`, lint each changed Python file before each commit, and leave the broad gate to the orchestrator.

## What this phase found

**The frame holds for this phase, with one placement choice.** The handoff's coordinates opened as stated: `hooks/dispatch.py` maps a `pre-` group to `PreToolUse`, `routing.py#current_branch` returns `""` for a detached HEAD, and `worktree_consent.py#automation_answered` reads the press. The frame did not say where the no-work-item record's address lives. It lives in `hooks/routing.py` (`NO_WORK_ITEM`, `session_name`, `no_work_item_path`, `no_work_item`, `record_no_work_item`), because both the gate and `seal.py` need it and `routing.py` already owns what routes a branch. `seal.py` now imports `routing` and `hooksession`, and `HOOK_PURPOSES` names both, so a copy of the script taken alone still exits 2 with a sentence per missing module.

**For phase 6.** The deny's declaration path comes from `hooks/gate.py#declaration_hint`, imported inside `reason()` only. *Removes* says that function moves to the edit gate. Phase 6 has to move it before it removes the arms around it, or the deny stops loading. The gate imports `gate` and `worktree_consent` only on the refusal path, which keeps both off an allowed edit's cost.

**Decisions settled while writing the code.**

- The checks run cheapest-first on the path an allowed edit takes: the root, the `seal/` root, then the branch's declaration. The ignore test, the no-work-item record and the press run only where no declaration names the branch.
- A path that is not absolute is not judged. The frame says the gate reads no `cwd`, and the edit tools refuse a relative path. A case pins it with the hook's own working directory set to the repository and a relative path naming a directory there.
- A `Write` may create the directories above its file, so the repository is found from the nearest existing directory above the path.
- A detached HEAD outside a rebase gets its own state sentence: HEAD is detached, so no declaration can name its branch. Its ways on name `the branch you check out` where a branch would stand. A case pins both.
- The no-work-item record names the session by its basename, and `seal no-work-item` refuses an id that is empty, `.` or `..`. The mutation run below found that the first version of the cases did not pin this, and the fix commit `d132a312` adds the cases and rewords the refusal to fit all three.

**Q4, executed.** A probe script outside the tree measured the gate in this clone, on this branch, which a declaration names, editing `hooks/routing-edit-gate.py`. That is the allowed path, so the gate takes every check up to the declaration. Python 3.12.11, macOS, 43 work-item directories under `seal/specs/`.

- In process, `decide(event)`: median 39.0 ms over 200 calls. A file in no repository: median 14.2 ms, the cost of the one `git rev-parse` that finds no root.
- Whole process, `python3 hooks/dispatch.py pre-edit` fed the payload: median 67.9 ms over 60 runs. The same dispatcher with a group that holds no gate: median 26.0 ms. The difference, 41.9 ms, is what the gate adds per edit. The 26.0 ms is the interpreter start that a new `PreToolUse` entry also adds, because the harness starts one hook process per edit. So a person waits about 68 ms more per `Write`, `Edit` or `NotebookEdit` in an opted-in repository.
- The 39 ms in process is two `git` calls (`rev-parse --show-toplevel` and `rev-parse --abbrev-ref HEAD`) plus reading every work item's `routing.md`. No part of it was optimised: Q4's default is to build on any value and report it.

**Q3 and S9, unverified.** Whether this `PreToolUse` hook fires for a subagent's `Edit`, and whether its deny stops the edit, was not measured. The session that built this phase runs the installed 0.22.3 copy of the plugin, so the tree's `hooks/hooks.json` entry loads in no session of this run. The answerer is the owner, in a live session after an installed release carries the hook. The tests prove the gate in process and through `dispatch.py pre-edit` only.

**How each new case was seen red, executed before the code.** With `tests/test_routing_edit_gate.py` written and no gate file, the module failed to collect: `FileNotFoundError` for `hooks/routing-edit-gate.py`, 10 errors. The new `tests/test_seal.py` cases failed: `Test_no_work_item` (5 cases) and the `no-work-item` row of `test_accepts_each_subcommand_and_hands_it_on` on argparse's `invalid choice: 'no-work-item'`, and the `routing.py` and `hooksession.py` rows of `test_a_script_copied_alone_exits_2_and_names_what_it_misses` on the missing purposes. The cases whose expected answer is silence pass against a missing gate too, so each was shown red by the mutant that breaks what it pins, below.

**`mutation-check`, executed after the commits.** 20 mutants, 20 red once the survivor was fixed:

- `hooks/routing-edit-gate.py`, 11, against `tests/test_routing_edit_gate.py`: the tool test off, `NotebookEdit` read by `file_path`, the absolute-path test off, the nearest-directory walk off, the `seal/` root exemption off, the rebase branch unread, the ignore test off, the no-work-item record unread, the press never read, the detached text replaced by the branch text, and `head-name` read with `refs/heads/` kept.
- `hooks/routing.py`, 4: `session_name` accepting `.` and `..` survived the first run, which the fix commit closed and a second run showed red; pruning off; pruning that takes fresh records too; and a record read as standing without its file.
- `skills/implement/scripts/seal.py`, 3: `--root` ignored, the session test off, and the subcommand's dispatch removed.
- `hooks/dispatch.py`, 1: the `pre-edit` group removed. `hooks/hooks.json`, 1: `NotebookEdit` dropped from the `pre-edit` matcher.

`git status --short` was clean after each run.

**Tests, executed.** `bin/test -n auto -q` over `tests/test_routing_edit_gate.py` (21 cases), `tests/test_seal.py`, `tests/test_dispatch.py` and `tests/test_routing.py`: green, 455 passed before the three cases the mutation run added, which then passed as well. The 20 modules that name `skills/implement/SKILL.md` or `skills/implement/orchestration.md`: 562 passed and 1 failed. The failure is `tests/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`, for this work item, which has no `overview.md`. It fails at the frame's commit too, because the frame wrote `spec.md` and `plan.md` and no memo, and this phase did not add one: the plan's rows do not ask for it. `test-layout --check` and `--pairs` over the changed test files: 0 refused, 0 pairs, after the gate's test took `reason_of` from `conftest.py` instead of a byte-identical copy of `tests/test_question_gate.py`'s.
