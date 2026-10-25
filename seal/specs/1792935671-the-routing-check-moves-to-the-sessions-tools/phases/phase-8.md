# Phase 8: 1792935671-the-routing-check-moves-to-the-sessions-tools

| Field | Value |
|---|---|
| Phase | 8 |
| Commit | 4876c64e |

## What this phase was asked

Build phase 8 of `plan.md` *Phases*: the no-work-item record names its branch. The owner answered `questions.md` Q7 with (b) on 2026-10-26, so one run of `seal no-work-item` lets the session edit only on the branch it ran on. Before this phase the record at `<git-common-dir>/specseal-no-work-item/<session-id>` was an empty file and `hooks/routing.py#no_work_item` ignored the branch, so one run opened every branch of the clone.

1. In `hooks/routing.py`, the record holds one branch name per line, UTF-8, each line ending in a newline. `record_no_work_item` takes the branch and adds it as a line where the record does not name it yet; with an empty branch it writes nothing and returns "". `no_work_item` takes the branch and is true only where a line equals it. An empty record written by the code at `126ee7b5` names no branch, so it allows nothing. The prune of records older than `NO_WORK_ITEM_AGE` stays.
2. The branch is resolved one way in both places: the branch checked out in the worktree, else the branch a paused rebase there names. `hooks/routing-edit-gate.py#rebase_branch` moves into `hooks/routing.py`, and the gate keeps no copy.
3. `seal no-work-item` resolves the branch of the worktree at `--root` or the working directory. On a detached HEAD outside a paused rebase it records nothing, prints one line saying a branch has to be checked out first, and returns 1. Its success line names the branch. The usage text and the subcommand's help say the record is for the branch checked out.
4. `hooks/routing-edit-gate.py#decide` passes the resolved branch to `routing.no_work_item`. `PRESSED` and `ATTENDED` say to run `seal no-work-item` once on that branch. Where HEAD is detached, the ways on name checking out a branch first, and neither offers `seal no-work-item` on the detached HEAD.
5. The prose that says the record covers the session or the clone says it covers the session on one branch: `README.md`, `README.ko.md` (rewritten in Korean), `skills/implement/SKILL.md`, `skills/implement/orchestration.md`, `skills/settle/SKILL.md`, `skills/commit-pr-convention/SKILL.md`, and the changelog fragment's *What a session meets instead* and Q2 bullets.

Verify with `tests/test_routing_edit_gate.py` (S4 and the detached refusal text) and `tests/test_seal.py` `Test_no_work_item`, each new case seen red first, the modules pinning each changed file, and `rules --check`.

## What this phase found

**The frame holds** (read). Each coordinate the handoff named was where it said: the empty-file write at `hooks/routing.py#record_no_work_item`, the branch-blind `#no_work_item`, and `rebase_branch` in the gate, called at `decide`.

**One function resolves the branch.** `routing.worktree_branch(cwd)` returns `current_branch(cwd) or rebase_branch(cwd)`. The gate and `seal no-work-item` both call it, so the record names the branch the gate reads. `rebase_branch` now runs its own `git rev-parse --absolute-git-dir`, because the gate's `git` helper did not move with it.

**The record is rewritten on every run.** `record_no_work_item` reads the lines, adds the branch where it is missing, and writes the whole file again. A run on a branch the record already names leaves one line and still refreshes the file's modification time. Without that, the prune would remove a record that its session had just re-run more than a day after its first run. The lines are split at `\n` alone and the file is opened with `newline=""`, so no other character a branch name may hold ends a line, and Windows writes no `\r`.

**The detached refusal texts.** Both say to check out a branch in the repository and then write its declaration or run `seal no-work-item` on it. Each also says `seal no-work-item` records nothing on a detached HEAD. The spawn prompt's item 4 asked for this. `spec.md` *Rule changes* first said the refusal "names checking out a branch in place of `seal no-work-item`", which also reads as "never names it" (`rounds/round-4.md` finding 2). Since `5e171b5f` it says the ways on name `seal no-work-item` only as a run on the branch checked out first, as the code builds it.

**A branch with no commit yet, closed by round 4's fix.** `routing.current_branch` returns "" on a branch with no commit, as on a detached HEAD. As this phase first built it, `seal no-work-item` there said HEAD is detached and recorded nothing, and the gate refused with the detached text. The code at `126ee7b5` had recorded and allowed there, so a new opted-in repository lost its way to edit before the first commit (`rounds/round-4.md` finding 1). `6030237f` adds `routing.unborn_branch`, which reads `git symbolic-ref -q --short HEAD`. `worktree_branch` asks it after `current_branch` and before the paused-rebase read. It names the branch HEAD points at and exits 1 on a detached HEAD, so a paused rebase still falls through to `rebase_branch`. Two cases hold it, one in `tests/test_seal.py` and one in `tests/test_routing_edit_gate.py`, both seen red before the fix (executed). `mutation-check` turned both red when the fallback was removed, and the `seal` case red when `--short` was dropped (executed).

**A case `tests/test_routing.py` gained.** Mutating `record_no_work_item`'s guard on an empty branch left every case of the gate and `seal` modules green (`mutation-check`, SURVIVED), because `seal no-work-item` refuses an empty branch before it calls the guard. `Test_record_no_work_item` in `tests/test_routing.py` holds it. `test-layout --check` then refused a class with no accepts case. The accepts case is the one behaviour no other group held: a run on a branch adds its line to the empty record the build at `126ee7b5` left.

**How each new or changed case was seen red** (executed).

- Against `df57fee9`, before any code change, `bin/test tests/test_routing_edit_gate.py tests/test_seal.py -q -p no:xdist -k "no_work_item or detached or refuses_an_edit or automation_press or record_naming"` ran 9 failed and 13 passed. The 9 were the two pinned refusal texts, the detached text, the S4 case on a second branch, the empty-record case, and the four new or changed `Test_no_work_item` cases. Each failed on its assertion: a text diff, `silent` where `deny` was due, or `''` where the record's line was due.
- The two `tests/test_routing.py` cases were seen red by `mutation-check`: the empty-branch guard removed, and the record's write emptied.

**Mutation, executed.** Every run ended with the mutated file restored from the bytes `mutation-check` held, and `git status --short` showed no change to it.

- `hooks/routing.py`: 6 mutants, 6 red. They were `no_work_item` reverted to the file's existence, `no_work_item` true for any non-empty record, the line filter removed, the add-once check removed, `worktree_branch` without the rebase half, and the `refs/heads/` prefix kept.
- `hooks/routing-edit-gate.py`: 3 mutants, 3 red. They were the branch texts used for a detached HEAD, `current_branch` in place of `worktree_branch`, and the record asked about its own first line in place of the edited file's branch.
- `skills/implement/scripts/seal.py`: 2 mutants, 2 red. They were the detached check removed, and `current_branch` in place of `worktree_branch`.
- `hooks/routing.py`'s empty-branch guard: SURVIVED over the gate, `seal` and `routing` modules, then red with the new case.

**Commands and results** (executed).

- `bin/test tests/test_routing_edit_gate.py tests/test_seal.py -q -p no:xdist`: 370 passed.
- The modules naming a changed unit or text (`tests/test_console.py`, `tests/test_dispatch.py`, `tests/test_first_setup_asks_once.py`, `tests/test_optin.py`, `tests/test_release_seal.py`, `tests/test_review_axes.py`, `tests/test_settle_reads_before_it_removes.py`, `tests/test_the_direct_answer_owes_the_sealers_record.py`, `tests/test_the_retired_rules_await_their_settle.py`, `tests/test_unverified_check.py`, `tests/test_waiver_decided_at_start.py`, `tests/test_routing.py`): 626 passed.
- 115 modules naming a changed README, skill or the changelog fragment, or walking the tree's Markdown: 4,884 passed, 14 skipped, 1 failed. The failure was `tests/test_test_layout.py`'s refusal of the class described above. After the accepts case, `tests/test_routing.py` and `tests/test_test_layout.py` passed, and `test-layout --check` refused nothing.
- `bin/rules --check`: all 249 check lines in 62 rule files hold.
- `ruff check` and `ruff format --check` over each commit's Python files: clean.
- `git grep` for the clone-wide wording (`in this clone`, `this session in`, `이 클론에서`, `empty file per session`) found no other sentence about this record. `templates/claude-md-block.md` says to run `seal no-work-item` before the first edit, which still holds, so it was left unchanged.

**Commits.** `67205fc3` holds the code and the gate and `seal` cases. `587ac6ab` and `8b6eac03` hold the `tests/test_routing.py` cases. `4876c64e` holds the prose and the changelog fragment.
