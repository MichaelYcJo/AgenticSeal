# Phase 6: 1792935671-the-routing-check-moves-to-the-sessions-tools

| Field | Value |
|---|---|
| Phase | 6 |
| Commit | 9a4e7cb7 |

## What this phase was asked

Build phase 6 of `plan.md` *Phases*: nothing is installed into git. `hooks/stub-remove.py` runs at `session-start` and removes only the stubs carrying the marker line, and a case shows a foreign hook left byte for byte. Remove `hooks/git/*`, `hooks/commitgate.py`, `hooks/githooks.py`, `hooks/hook-install.py`'s write path, the arms in `hooks/gate.py`, the session route in `hooks/hooksession.py`, `hooks/answers.py`, `hooks/answer-write.py`, `hooks/answer-clear.py`, `hooks/implementer-notice.py`'s stand-aside and `seal_stamp.py#queue_for_guarantee`, with their tests. Move `hooks/gate.py#declaration_hint` into the edit gate before the arms go. Remove `pre-commit`'s refusal writer. Remove the `post-commit` fallback clauses in both READMEs, in `skills/verify/SKILL.md` *Form* and in the stamp paragraph of `skills/code-review/orchestration.md`. Leave `docs/` alone. Verify with `tests/test_stub_remove.py` (S15, S17), `tests/test_dispatch.py` (S16), `tests/test_implementer_notice.py`, `tests/test_session_lease.py`, `tests/test_worktree_guard.py`, `rules --check`, and a `git grep` for `hooks_dir`, `specseal-judged` and `GIT_AUTHOR_DATE` under `hooks/` that finds none.

## What this phase found

**The frame holds, with two places where the tree disagrees with it.**

- `spec.md` *Removes* keeps `hooks/gate.py#git` and `#lines` "for `chain_check.py`". `chain_check.py` loads `gate.py` and calls only `touches_code` (executed: `grep` over `skills/code-review/scripts/chain_check.py`), and nothing else in the tree calls the two. `gate.py` is now `DOC_ROOTS` and `touches_code` alone. A divergence row in `overview.md` records it.
- *Removes* lists units of `hooks/hook-install.py` to remove. What was left of the file once they went was `remove_ours`, which read stubs through `hooks/githooks.py`, and `main`. `hooks/stub-remove.py` replaces both. So the whole file went, as `spec.md` *Registration* implies by replacing it in `session-start`.

**The phase-5 commit left one case red, and this phase repaired it.** `tests/test_every_orchestrator_act_names_its_delivery.py` reads the delivered-by rows of `skills/implement/orchestration.md`, and two of them named `hooks/commit-review-gate.py`, which phase 5 removed. The rows for *how the work is routed* and *multi-repository* now name `hooks/routing-edit-gate.py`. The row for *closing the cycle* is now "still a sentence", because the stand-aside it named is gone. The phase-5 run selected modules by the names they import, and this module reads the file's text, so that run did not include it.

**`hooks/stub-remove.py`.** A stub is a file in the common git directory's `hooks/` whose second line starts with `# specseal-git-hook`. Every file in the directory is read, so a stub of any name goes. A file without the marker is never touched, including one that names the marker on another line. The message names the directory and the removed names, in the order an earlier release wrote them. Every failure is silent. The case helper that runs the hook fails a case on a non-zero exit or any stderr: the first mutation run showed that the guard on an empty removal had no case behind it, because the hook crashed into the same silence (commit `647fe1d0`).

**`declaration_hint` moved to `hooks/routing-edit-gate.py`, without the branch for a repository with no `seal/` root.** That branch was reachable from the commit gate's arms. The edit gate refuses only where the root exists (`decide` returns early otherwise), so the branch had no caller left. `mutation-check` showed it surviving, and it was removed in commit `f4cf5454`.

**Other units.**

- `hooks/hooksession.py` keeps `SESSION_VARIABLE`, `PID_VARIABLE`, `is_claude`, `claude_pid` and `claude_ancestor`.
- `hooks/tokens.py#KNOWN` keeps `[worktree-ok]` and `[shared-tree-ok]`.
- `seal_stamp.py#sealed_before` reads `git log HEAD`. Its only caller now is the write-time writer, which runs before the guarantee is committed.
- `hooks/dispatch.py#GROUPS`: `pre-bash` is the worktree guard and the mode gate; `post-bash` no longer runs `answer-clear.py`; `session-start` runs `stub-remove.py` in `hook-install.py`'s place.

**Retired check targets kept until the settle, as in phase 5.**

- `tests/test_the_hooks_are_installed_where_git_runs_them.py` stays with no case, because `docs/the-commit-gate-inside-git.md` names it on a `check:` line.
- The class `Test_sealed_off_the_branch_refused`, with no case, joins `tests/test_the_retired_rules_await_their_settle.py` for the marker `sealed-off-the-branch-refused`, which `docs/the-commit-gate-inside-git.md` line 110 names.
- `rules --check`: all 250 check lines in 62 rule files hold (executed).

**The `git grep` the plan names** (`hooks_dir`, `specseal-judged`, `GIT_AUTHOR_DATE` under `hooks/`) found nothing, exit 1 (executed). The first draft of the remover named a function `hooks_directory`, which the pattern `hooks_dir` matches. It was renamed `stub_folder`, so the grep reads as the plan states it.

**Prose and comments.**

- The fallback clauses went from `README.md`, `README.ko.md`, `skills/verify/SKILL.md` *Form* and `skills/code-review/orchestration.md`. The refusal record is now written by the edit hook in either mode.
- The orchestration paragraph about `pre-commit` refusing a stale `sealed` now says that the pull request's check refuses such a row as stale, and that the sealer is spawned again at HEAD.
- `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` pins the new sentences.
- The README rows for the git hooks and the commit gate, with their `pre-commit` sentence, are phase 7's.
- Code comments that named the commit gate's lease route, arms or text reading as present now name what reads them (commit `9a4e7cb7`): `hooks/mode-gate.py`, `hooks/one_heredoc.py`, `hooks/optin.py`, `hooks/question-gate.py`, `hooks/routing.py`, `hooks/worktree-guard.py`, `skills/code-review/scripts/chain_check.py`, `tests/test_hooksession.py` and `tests/test_chain_hooks_hardening.py`. Comments that tell the history in the past tense stay. `hooks/cmdline_base.py` is frozen and keeps its two mentions.

**`.test_durations` now fails its own case.** `bin/test tests -q -p no:xdist -k test_the_durations_file_prices_the_suite`, run at the working tree before the phase commit: 424.2 s of the file's 1,657.1 s (25.6%) belong to 1,378 entries the suite no longer collects, over the 5% the case allows (executed). `CONTRIBUTING.md` *Running the checks* says the file is refreshed from the branch's latest `tests` run artifact. That needs a push and a CI run, and neither is mine. A hand edit of 1,378 keys is the shell rewrite my definition refuses. The orchestrator refreshes the file before the broad gate.

**How each new or changed unit was seen red, executed after the commit with `mutation-check`.** `git status --short` was empty after every run.

- `stub-remove.py`: the marker test widened to anywhere in the head; `os.remove` replaced by `pass`; the spoken order replaced by name order; the hooks directory taken from the worktree instead of the common git directory (the linked-worktree case); `if removed:` forced true (the no-stub case, red only after the helper change above).
- `dispatch.py`: `stub-remove.py` dropped from `session-start`.
- `seal_stamp.py#sealed_before`: `HEAD` read as `HEAD~1`.
- `tokens.py#KNOWN`: `[shared-tree-ok]` dropped.
- `routing-edit-gate.py#declaration_hint`: the relative path replaced by the absolute one.

**Tests, executed.**

- The phase-6 commit's run: 82 modules, the changed test files plus every module that names a changed hook, script, README or skill file. 4,001 passed, 14 skipped.
- After the case renames, the plan's modules with `tests/test_stub_remove.py`, `tests/test_dispatch.py` and `tests/test_chain_hooks_hardening.py`: 472 passed, 3 skipped.
- After the comment commit, the nine modules of the edited files with the three text-reading hygiene modules: 936 passed, 3 skipped.
- `test-layout --check`: 0 refused. `ruff check` and `ruff format --check` over the changed files: clean.
