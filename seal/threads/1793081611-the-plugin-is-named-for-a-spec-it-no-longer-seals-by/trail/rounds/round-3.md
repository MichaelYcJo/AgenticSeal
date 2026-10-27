# Review round 3: 1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by

target: e9c0533b, fixes 83efd0fc..e9c0533b

This round reads the fix diff `83efd0fc..e9c0533b` (four commits) and the three round 2 findings it answers, and nothing else of the branch. Carried from round 2, not re-established: the coordinates of each finding, its probe's fixture shapes, and round 2's confirmations of round 1, none of which the fix diff touches. Re-established this round: every verdict below. Round 2's probe was written again from its `## Probes` row, as one file with four cases (detached HEAD, merge in progress, cherry-pick in progress, stopped rebase), run once in the same `bin/test` command as the two modules the findings concern, and deleted. The fix pass left the three verdict lines at `open`; this round set them to the commits that made each fix, as the spawn prompt directs. As the orchestrator directed, finding 1 was judged on whether its limit sentence states the limit truly, and the guard round 2 proposed is not asked for again. `frame/plan.md` *Verification this work item owes* binds the round: no finding asks for red-first evidence or a mutation run.

## Findings

### 1. The hook's docstring says each boundary is pinned in `tests/test_root_migrate.py`, and the second limit the fix added has no case

severity: should
location: `hooks/root-migrate.py:26`, `hooks/root-migrate.py:42-47`, `tests/test_root_migrate.py:619-641`
evidence: executed `grep -n -i "detach\|symbolic-ref\|MERGE_HEAD\|rebase\|cherry" tests/test_root_migrate.py`, `grep -n "def test_" tests/test_root_migrate.py`
verdict: open
regression: round-2#1

The unit is the module docstring of `hooks/root-migrate.py`, its boundary *on any branch*, which cc9b77e5 changed. `frame/design.md:188-190` keeps the move's boundaries and the docstring opens their list with "Boundaries, each pinned in `tests/test_root_migrate.py`" at `:26`; the fix wrote the second limit under that heading without a case; the defect comes from stating the limit where every other entry has a case and this one does not.

The claim was that no case is added (round 2's `answer:` for finding 1). That is what the tree shows: the grep over `tests/test_root_migrate.py` for a detached HEAD, `symbolic-ref`, `MERGE_HEAD`, a rebase or a cherry-pick finds nothing. Every other entry of the list has its case. The uncommitted-work refusal has `test_refuses_work_in_progress_under_a_units_directory` and `test_refuses_to_move_over_work_in_progress`. The ignored file has `test_accepts_an_ignored_file_under_a_source_left_where_it_is`. A stopped move has `test_refuses_to_finish_a_stopped_move_and_the_next_start_continues`. The silent start has `test_refuses_to_speak_where_nothing_is_old`. The first limit got its case in this fix diff (bd326e20). A reader who takes the heading at its word believes the second limit is held by a case, and a later change to it turns nothing red.

This finding does not ask for the guard. It asks for the case that pins the limit as stated, the way bd326e20 pinned the first limit. Where the crafter keeps no case, the other fix is the heading: "Boundaries, each pinned in `tests/test_root_migrate.py` except the second limit under *on any branch*". The case below was assembled from this round's probe, whose merge and detached halves ran with these steps and printed these results. It was not run as written.

```python
# tests/test_root_migrate.py#Test_main, after
# test_accepts_a_branch_cut_before_a_switch_to_local_mode_moved_in_its_tree.
# `write`, `commit`, `commit_staged`, `start`, `message`, `git` and `ITEM` are
# this module's. Precondition: `git(..., check=False)` returns the
# CompletedProcess, and `git merge` exits 1 on a conflict.
    def test_accepts_a_merge_in_progress_and_a_detached_head_moved_where_they_stand(
        self, hook, layout
    ):
        """The second limit `hooks/root-migrate.py`'s docstring states:
        nothing reads where HEAD points. A start during a merge stopped on a
        conflict outside `seal/` stages the move, and the merge commit carries
        it; a start on a detached HEAD stages it there."""
        write(layout, "x.txt", "base\n")
        commit(layout, "x base")
        git(layout, "switch", "-qc", "side")
        write(layout, "x.txt", "side\n")
        commit(layout, "x side")
        git(layout, "switch", "-q", "main")
        write(layout, "x.txt", "main\n")
        commit(layout, "x main")
        assert git(layout, "merge", "side", check=False).returncode == 1
        said = message(start(hook, layout))
        assert said.startswith("agentic:moved seal/specs/ into seal/"), said
        write(layout, "x.txt", "resolved\n")
        git(layout, "add", "x.txt")
        commit_staged(layout)
        carried = git(layout, "diff", "--name-status", "-M", "HEAD^1", "HEAD").stdout
        assert f"seal/threads/{ITEM}/routing.md" in carried
        git(layout, "checkout", "-q", "--detach", "HEAD^1")
        said = message(start(hook, layout))
        assert said.startswith("agentic:moved seal/specs/ into seal/"), said
        cached = git(layout, "diff", "--cached", "--name-only").stdout
        assert f"seal/threads/{ITEM}/routing.md" in cached
```

answer: fixed in f8732393 by the heading, the finding's second way: the heading now says the second limit under **on any branch** is stated and not pinned. A case pinning it would hold the move staged on a detached HEAD as wanted behaviour, which the limit does not claim, so no case is added. The orchestrator made this fix, as a prose fix too small for a crafter spawn.

### 2. The Korean edition uses one word for the stamp it denies and for the marker the move writes, two sentences apart

severity: should
location: `docs/one-root-by-lifetime.ko.md:104-109`
evidence: read `docs/one-root-by-lifetime.ko.md:104-109`, `docs/one-root-by-lifetime.ko.md:52-70`, `docs/one-root-by-lifetime.md:109-115`
verdict: open
regression: round-2#2

The unit is `docs/one-root-by-lifetime.ko.md` *처음 설정에서 무엇을 묻는가*, the paragraph b11b2d80 rewrote. `frame/design.md:15` makes the root the signal only with its marker, and the Korean edition names that marker 표식 at `:55-61`; the fix copied round 2's proposed Korean text word for word, and that text writes "marked" as 표시가 붙으며; the defect comes from round 2's own proposal, which took the edition's word for a mark under `.git/` (`:68`, 표시 파일) for the README's marker.

The paragraph reads at `:106` "브랜치와 그 이동 사이를 막는 표시는 없습니다", which is the English "No stamp stands between a branch and its move". At `:108` it reads "트리 안에서 옮겨지고 표시가 붙으며", which is the English "moved and marked in the tree". In the English edition the two words differ, stamp and marked. In the Korean edition both are 표시, so the second sentence reads as the stamp the first one denies, now attached. The edition's own term for the README's first line is 표식 (`:55`, `:56`, `:58`, `:61`). An agent that reads the Korean policy reads a contradiction about the one fact this paragraph exists to correct. The test pins "앞선 배치가 남아 있는 브랜치마다" only, so it stays green either way, and the line the fix changes is not one the test reads.

```markdown
<!-- docs/one-root-by-lifetime.ko.md:104-109, in place of the paragraph -->
플러그인 이름이 AgenticSeal 로 바뀌기 전에 설치한 저장소는 트리에 앞선
배치가 남아 있는 브랜치마다 세션 시작 훅이 작업 항목을 스레드 배치로
옮깁니다. 브랜치와 그 이동 사이를 막는 표시는 없습니다. 그래서 shared
모드에서 local 모드로 옮긴 저장소에서는 전환 전에 만든 브랜치의 `seal/` 이
트리 안에서 옮겨지고 그 `README.md` 가 표식으로 시작하게 되며, 훅은 그
루트를 먼저 읽습니다(`hooks/root-migrate.py` 의 경계).
```

answer: fixed in f8732393: `:106` now says that a record of an earlier move does not stop a branch's move, without 표시, and `:108` says 표식, the document's word for the README marker. The orchestrator made this fix, as a prose fix too small for a crafter spawn.

## Confirmations

confirms: round-2#1
The limit sentence at `hooks/root-migrate.py:42-47` states what the hook does. Nothing in `hooks/root-migrate.py` reads HEAD: its one `rev-parse` is `--absolute-git-dir` at `:461`, and no `symbolic-ref` stands in the file. This round's probe ran each shape the sentence names except a revert. On a detached HEAD at the commit before a committed move, `symbolic-ref` exited 1, the start printed "agentic:moved seal/specs/ into seal/ — review the diff and commit", and `git status --porcelain` listed `M  seal/README.md` and the eleven renames. During a merge stopped with `UU x.txt`, the start staged the move, and the merge commit's first-parent diff carried the README rewrite and the eleven `R100` renames beside `x.txt`. During a cherry-pick stopped on `x.txt`, the commit `cherry-pick --continue` made, titled "x side", carried them. During a rebase stopped on `b2`, `symbolic-ref` exited 1, the start moved `1788000002-b/routing.md`, and the replayed "b2 conflicts on x" carried `R100 seal/specs/1788000002-b/routing.md seal/threads/1788000002-b/routing.md`. A revert in progress goes through the same index and commit as a cherry-pick, which is read, not executed. The reason the sentence gives also holds. A start reaches a stopped operation only through a session that starts there or is compacted or resumed there, since `hooks/hooks.json` registers `SessionStart` with no matcher. The flow never rebases a work item's branch (`docs/release-checklist.md:19-21`). The one operation it allows mid-run, merging the release branch into a work item's branch (`docs/release-checklist.md:17-18`), meets a branch whose own first session start already listed its 0.22.x units, and a release branch cut after the rename brings none. A session that starts on `main` before routing creates the branch starts on a branch tip, so the conclusion stands although the sentence names the work item's own branch. The sentence carries the pin defect of finding 1 above. Executed and read.

confirms: round-2#2
Both editions of *What first setup asks* are rewritten in place. The English text at `docs/one-root-by-lifetime.md:109-115` is round 2's proposed text, and it states the same fact as the docstring's first limit at `hooks/root-migrate.py:38-42`. `tests/test_first_setup_asks_once.py::test_the_design_record_states_the_setup_rules_where_they_rule` takes `move` and pins "on each branch whose tree still holds them" and "앞선 배치가 남아 있는 브랜치마다"; both parameters were collected and passed in this round's run. The crafter's grep claim holds: `git grep` for "stamps the repository", "옮겼다는 표시", "keep clean", "chose to keep", "once per repository", "layout once" and "root-migrated" outside the records, the released changelogs and `.test_durations` finds only `hooks/implementer-notice.py:23` and two test docstrings about the first-setup question, none about the move. The remaining "stamp" lines are `hooks/root-migrate.py:118-119`, two old state names `rename_state` carries, and the old-state fixture at `tests/test_root_migrate.py:922-930`. The Korean edition's word choice is finding 2 above. Executed and read.

confirms: round-2#3
`test_refuses_to_write_the_tree_beside_a_local_root` is gone and `test_accepts_a_branch_cut_before_a_switch_to_local_mode_moved_in_its_tree` stands at `tests/test_root_migrate.py:619-640`, as round 2 proposed. It keeps the linked-worktree half, asserts silence on `main` with a marked `.git/seal/`, and asserts the move and the marker on `old-shared`, so a guard that refused the move beside a local root would turn it red. The case was collected and passed in this round's run. The 0.3.x half the old case held is pinned by `test_refuses_to_read_another_tools_specs_or_the_0_3_x_root`, which round 2 read and this round did not re-open. Executed and read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| a revert in progress, which this round's probe did not run; the cherry-pick case stands for it | `hooks/root-migrate.py:42-47` | the crafter, if finding 1's case is extended to it |
| the full suite, the repository-wide lint and the typecheck over this branch | the branch | the orchestrator's broad run after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test <scratch>/round-3/test_tmp_round3_probe.py tests/test_root_migrate.py tests/test_first_setup_asks_once.py -s -q -p no:xdist --basetemp=<scratch>/round-3/tmp`, the probe's four cases over `layout` fixtures with the `hook` fixture's state directories under each case's directory | exit 0, 114 passed. Detached HEAD: `symbolic-ref` exit 1, the start printed "agentic:moved seal/specs/ into seal/ — review the diff and commit", status `M  seal/README.md` and eleven `R` lines. Merge: exit 1 with `UU x.txt`, the start moved, the merge commit (two parents) carried the README and eleven `R100` renames. Cherry-pick: exit 1, the start moved, `--continue` exit 0, the "x side" commit carried them. Rebase: exit 1, `symbolic-ref` exit 1, the start moved, `--continue` exit 0, "b2 conflicts on x" carried `R100 seal/specs/1788000002-b/routing.md`. The probe file, its fixtures and its log were deleted after the run |
| `bin/test tests/test_root_migrate.py tests/test_first_setup_asks_once.py --collect-only -q -p no:xdist` | 110 collected, including `Test_main::test_accepts_a_branch_cut_before_a_switch_to_local_mode_moved_in_its_tree` and both parameters of `test_the_design_record_states_the_setup_rules_where_they_rule` |
| `ls -la ~/.claude/specseal/` and `ls -la ~/.claude/agentic` before and after the run | `~/.claude/specseal/` listed the same seven entries; `~/.claude/agentic` did not exist before or after, so nothing was removed |
