# Review round 2: 1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by

target: c1e26886, fixes 52656000..c1e26886

This round reads the fix diff `52656000..c1e26886` (eight commits) and the round 1 findings it answers. Carried from round 1, not re-established: the coordinates of each finding, and the round 1 confirmations of the trailer, the marker's one reader, the command line and the plugin identity, none of which the fix diff touches. Re-established this round: every verdict below, and the executed lines of round 1 findings 4 and 7, run again. Round 1's probe was not written again. Its first two cases are now cases of the suite (`Test_main::test_accepts_a_branch_cut_before_the_move_moved_at_its_own_start`, `Test_rename_state::test_accepts_a_clone_whose_tree_another_person_moved`), and both passed in this round's run. `frame/plan.md` *Verification this work item owes* binds the round: no finding asks for red-first evidence or a mutation run.

## Findings

### 1. A session start on a detached HEAD stages the move, and a rebase stopped on a conflict folds it into the commit it replays

severity: should
location: `hooks/root-migrate.py:563-606`, `hooks/root-migrate.py:34-41`, `tests/test_root_migrate.py:598-617`
evidence: executed `bin/test <scratch>/round-2/test_tmp_round2_probe.py -s -q -p no:xdist`
verdict: fixed cc9b77e5
regression: round-1#1

The unit is `hooks/root-migrate.py#main`, which 9ce5c698 changed. `frame/design.md` *The migration* keeps the boundary "once per repository" and `frame/plan.md` phase 2 delivers "the new stamp"; the fix removed the stamp so that every session start moves what the checked-out tree holds; the defect comes from the stamp having also kept the move off every checkout that is not a branch someone is working forward.

`main` now lists the units of whatever is checked out and stages them. Nothing reads where HEAD is. The docstring's boundary says "on any branch", but a detached HEAD is no branch. The probe built a repository whose `main` holds a 0.22.x work item, ran the move, committed it, and checked out the commit before the move with `git checkout --detach`. The session start there printed "agentic:moved seal/specs/ into seal/ — review the diff and commit" and staged the README rewrite and the rename onto the detached HEAD. That checkout is a tag, an old commit opened to read, or a bisect step. Nothing there is committed forward, and a staged rename blocks or rides along the next checkout.

The rebase case does harm to history. The probe's `feat/b` holds three commits: `b1` adds `seal/specs/1788000002-b/routing.md`, `b2` changes `x.txt`, and `b3` adds `seal/specs/1788000002-b/rounds/round-1.md`. `main` changes `x.txt` too, then commits the move. `git rebase main` stopped on `b2` with `UU x.txt`. The `dirty` check reads only the units' directories, so the session start moved `1788000002-b/routing.md` and staged it beside the conflict. After `x.txt` was resolved, `git rebase --continue` exited 0. The rewritten `b2`, titled "b2 conflicts on x", now carries `rename seal/{specs => threads}/1788000002-b/routing.md`. `b3` replayed its round record at `seal/specs/1788000002-b/rounds/round-1.md`, so the work item stood half in each layout until the next session start. A session is started at a stopped rebase whenever a person opens one to resolve the conflict.

The class is a session start where HEAD is not a branch tip being worked forward: a detached HEAD, which covers a tag, a bisect step and a stopped rebase, and a merge, cherry-pick or revert in progress on a branch, where the staged move goes into the commit that operation makes. The local move is not in the class: it renames under the git directory and nothing is committed.

```python
# hooks/root-migrate.py, beside CACHE
# Where git keeps an operation in progress on a branch: a move staged during
# one goes into the commit that operation makes, not into one of its own.
IN_PROGRESS = ("MERGE_HEAD", "CHERRY_PICK_HEAD", "REVERT_HEAD")


def worked_branch(root):
    """True where HEAD names a branch and no merge, cherry-pick or revert is
    in progress. A detached HEAD is a tag or an old commit checked out to
    read, a bisect step, or a rebase stopped on a conflict; the branch's own
    session start moves what it holds. A git that cannot answer is no branch,
    so nothing is staged."""
    try:
        if git(root, "symbolic-ref", "-q", "HEAD").returncode != 0:
            return False
        return all(
            git(root, "rev-parse", "-q", "--verify", name).returncode != 0
            for name in IN_PROGRESS
        )
    except (OSError, subprocess.SubprocessError):
        return False


# hooks/root-migrate.py#main, after the `if not units:` branch and before
# `dirty`; silent, because the branch's own next session start moves it:
    if not worked_branch(root):
        return

# The docstring's boundary "on any branch" gains: a detached HEAD (a tag, an
# old commit, a bisect step, a stopped rebase) and a merge, cherry-pick or
# revert in progress move nothing, because the move would land in a commit
# that is not its own.
#
# tests/test_root_migrate.py#Test_main gains one case: after the move is
# committed on `main`, `git checkout --detach` of the commit before it hears
# nothing and `git status --porcelain` is empty; and a rebase of a branch cut
# before the move, stopped on a conflict outside `seal/`, hears nothing and
# stages nothing under `seal/`.
# Precondition: `git(root, *args)` returns a CompletedProcess, as in `move`.
```

answer: The fix is a limit sentence, not the guard this record proposes. `hooks/root-migrate.py`'s docstring, in its boundary *on any branch*, now states a second limit, not guarded: nothing reads where HEAD points, so a session start on a detached HEAD (a tag, an old commit, a bisect step, a rebase stopped on a conflict) or during a merge, cherry-pick or revert stages the move there as well, and the commit that operation makes carries it. The reason stands with it: a session in this plugin's flow starts on its work item's own branch, so the flow does not produce that shape, and the owner's standing rule gives a shape the flow does not produce a limit sentence rather than a guard. No case is added. No document under `docs/` states the move's boundaries. `docs/the-record-layout.md` *The files keep these paths until the settle after their release, and leave together* states when the move runs, "at the session start of each branch whose tree still holds them", and names the hook, and the limit does not contradict it. `docs/one-root-by-lifetime.md` now cites the docstring's boundaries (finding 2).

### 2. The policy still says the hook stamps the repository so a local-mode repository's old branch is never moved into its tree, and a test pins that sentence

severity: should
location: `docs/one-root-by-lifetime.md:109-114`, `docs/one-root-by-lifetime.ko.md:104-108`, `tests/test_first_setup_asks_once.py:711-738`
evidence: executed `bin/test <scratch>/round-2/test_tmp_round2_probe.py -s -q -p no:xdist`, `git grep -n -i "stamps the repository" -- docs tests`
verdict: fixed b11b2d80
reopens: round-1#1

The close of round 1 finding 1 holds in the code. `Test_main::test_accepts_a_branch_cut_before_the_move_moved_at_its_own_start` passed in this round's run, and `attempted`, `stamp`, `MARKER` and `has_root` are gone. It does not hold in the policy. 9ce5c698 rewrote `docs/the-record-layout.md`, the changelog fragment and the frame's premise, and left `docs/one-root-by-lifetime.md` *What first setup asks* as it was: "has its work items moved into the thread layout once, by the session-start hook. Once a root exists at either place and nothing of the earlier layout is left, that hook stamps the repository as moved, so a local-mode repository that later checks out an old branch is not moved into the tree it chose to keep clean." The Korean edition says the same at lines 104-108. `tests/test_first_setup_asks_once.py:711-738` requires both editions to hold "that hook stamps the repository as moved" and its Korean twin, so the case pins the old fact.

No stamp exists, and the hook does what the sentence denies. The probe's third case left shared mode for local mode on `main` (`git rm -r seal`, then a marked `.git/seal/`) and kept a branch `old-shared` cut before the switch. The start on `main` printed nothing. The start on `old-shared` printed "agentic:moved seal/specs/ into seal/", staged the README rewrite and the rename in the tree, and `optin.home_at` then answered the tree's `seal/`. That is the limit sentence the fix wrote into the hook's docstring (`hooks/root-migrate.py:38-41`). The policy and the docstring now state opposite facts, and the policy is what a session reads first.

```markdown
<!-- docs/one-root-by-lifetime.md, in place of "has its work items moved
into the thread layout once, by the session-start hook. Once a root exists
... the tree it chose to keep clean." -->
A repository installed before the plugin was renamed
AgenticSeal has its work items moved into the thread layout by the
session-start hook, on each branch whose tree still holds them. No stamp
stands between a branch and its move. So in a repository that left shared
mode for local mode, a branch cut before the switch has its own `seal/`
moved and marked in the tree, and the hooks read that root first
(`hooks/root-migrate.py`, its boundaries).

<!-- docs/one-root-by-lifetime.ko.md, in place of lines 104-108 -->
플러그인 이름이 AgenticSeal 로 바뀌기 전에 설치한 저장소는 트리에 앞선
배치가 남아 있는 브랜치마다 세션 시작 훅이 작업 항목을 스레드 배치로
옮깁니다. 브랜치와 그 이동 사이를 막는 표시는 없습니다. 그래서 shared 모드에서
local 모드로 옮긴 저장소에서는 전환 전에 만든 브랜치의 `seal/` 이 트리
안에서 옮겨지고 표시가 붙으며, 훅은 그 루트를 먼저 읽습니다
(`hooks/root-migrate.py` 의 경계).
```

```python
# tests/test_first_setup_asks_once.py:711-738: the fourth parameter is the
# move, not the stamp.
@pytest.mark.parametrize(
    "parts, opt_in, setup, move",
    [
        (
            ("docs", "one-root-by-lifetime.md"),
            "## The opt-in signal is the root itself",
            "## What first setup asks",
            "on each branch whose tree still holds them",
        ),
        (
            ("docs", "one-root-by-lifetime.ko.md"),
            "## 옵트인 신호는 루트 자체다",
            "## 처음 설정에서 무엇을 묻는가",
            "앞선 배치가 남아 있는 브랜치마다",
        ),
    ],
)
# ...and the docstring reads "the migration hook's move", the loop's needle
# `move`.
```

answer: Both editions of *What first setup asks* are rewritten in place to this record's text. The session-start hook moves the work items on each branch whose tree still holds them, no stamp stands between a branch and its move, and in a repository that left shared mode for local mode a branch cut before the switch has its own `seal/` moved and marked in the tree, which the hooks read first. The sentence cites `hooks/root-migrate.py`'s boundaries, and it states the same fact as the docstring's first limit sentence. `tests/test_first_setup_asks_once.py::test_the_design_record_states_the_setup_rules_where_they_rule` takes `move` as its fourth parameter and pins "on each branch whose tree still holds them" and "앞선 배치가 남아 있는 브랜치마다", and its docstring names the migration hook's move. The change corrects prose, so no red-first case is written. `git grep` for "stamps the repository", "옮겼다는 표시", "keep clean" and "chose to keep" finds no other living line. `changelog/0.5.0.md` is a released version, and `.test_durations` is the runner's cache, which the runner rewrites.

### 3. `test_refuses_to_write_the_tree_beside_a_local_root` names a refusal the hook no longer makes, and pins only what the 0.3.x case already pins

severity: should
location: `tests/test_root_migrate.py:619-637`
evidence: executed `bin/test <scratch>/round-2/test_tmp_round2_probe.py -s -q -p no:xdist`
verdict: fixed bd326e20
regression: round-1#1

The unit is `tests/test_root_migrate.py#Test_main::test_refuses_to_write_the_tree_beside_a_local_root`, which 9ce5c698 renamed and rewrote from `test_accepts_a_local_root_as_stamped_and_leaves_an_old_branch_alone`. `frame/plan.md` phase 2 names "a 0.22.x fixture migrated end to end, shared and local" and `frame/design.md` *The migration* keeps the once-per-repository boundary; the fix kept the case's old promise in its name while removing the stamp that made the promise true; the defect comes from renaming the case for what it used to guard rather than for what it now reads.

The case checks out a branch carrying the 0.3.x layout (`.specseal/` and a top-level `specs/`) beside a marked `.git/seal/` and asserts that nothing is written. No 0.3.x unit exists in the hook at all, so the assertion holds with or without a local root. `test_refuses_to_read_another_tools_specs_or_the_0_3_x_root` (`tests/test_root_migrate.py:580-593`) already pins that the 0.3.x layout is never read. The case's name and its "S9 of #80" docstring say the hook refuses to write the tree beside a local root. For the layout this move does read, the hook writes the tree beside a local root: the probe's third case, described under finding 2, moved a 0.22.x branch in the tree with a marked `.git/seal/` standing. A person or agent reading the suite for what local mode guarantees reads a guard that is not there.

The class is the cases and sentences that still state the stamp's protection of a local-mode tree. Finding 2 holds the policy's two editions and the case that pins them. This finding holds the case in `tests/test_root_migrate.py`. `git grep -n -i "keep clean\|chose to keep"` over `docs`, `README.md`, `skills`, `hooks` and `templates` finds no other.

```python
# tests/test_root_migrate.py#Test_main, in place of
# test_refuses_to_write_the_tree_beside_a_local_root: the limit the hook's
# docstring states, pinned, with the linked-worktree half kept.
    def test_accepts_a_branch_cut_before_a_switch_to_local_mode_moved_in_its_tree(
        self, hook, layout, tmp_path
    ):
        """The limit `hooks/root-migrate.py`'s docstring states: a repository
        that left shared mode for local mode still carries its 0.22.x `seal/`
        on a branch cut before the switch, and that branch's session start
        moves it in the tree and marks it, so the hooks read it before the
        local root. The local-mode branch, and a linked worktree of it, hear
        nothing."""
        git(layout, "switch", "-qc", "old-shared")
        git(layout, "switch", "-q", "main")
        git(layout, "rm", "-rq", "seal")
        commit(layout, "left shared mode")
        mark_root(layout / ".git" / "seal")
        assert start(hook, layout) == ""
        linked = tmp_path / "linked"
        git(layout, "worktree", "add", "-q", str(linked), "-b", "feature/x", "main")
        assert start(hook, linked) == ""
        git(layout, "switch", "-q", "old-shared")
        said = message(start(hook, layout))
        assert said.startswith("agentic:moved seal/specs/ into seal/"), said
        assert first_line(layout / "seal" / "README.md") == ROOT_MARKER
```

answer: Replaced, not removed. The old case's 0.3.x half is already pinned by `test_refuses_to_read_another_tools_specs_or_the_0_3_x_root`. Its linked-worktree half is pinned by no other case in `tests/test_root_migrate.py`, and the limit the docstring states had no case. `test_accepts_a_branch_cut_before_a_switch_to_local_mode_moved_in_its_tree` stands in its place as this record proposes. On `main`, after `git rm -r seal` and a marked `.git/seal/`, the session start prints nothing, and so does the start in a linked worktree of `main`. On `old-shared`, cut before the switch, the start prints "agentic:moved seal/specs/ into seal/" and `seal/README.md` opens with the marker.

## Confirmations

confirms: round-1#2
`hooks/root-migrate.py#main` calls `rename_state(root)` at `:576`, before the root test and the symbolic-link check, and the two calls inside the moves are gone. A clone that pulls a moved tree renames its own state: `Test_rename_state::test_accepts_a_clone_whose_tree_another_person_moved` passed in this round's run, including the second start that changes nothing. On the two questions the spawn prompt put: the merge never overwrites. Each pair moves only where `os.path.lexists(new)` is false (`:479`), and the one deletion is the old `version-check` where the new directory holds its own (`:484-489`), a cache `hooks/version-check.py` rewrites, which `hooks/dispatch.py:100` runs before this hook. Two session starts racing over one entry both pass the test, the first rename wins and the second raises `FileNotFoundError` inside the `except OSError`, so nothing is lost. The window between the test and `os.rename` can replace a destination only if another writer creates that name in it, and no hook of this release writes a name of `STATE_NAMES` or of the old home at session start except `version-check`. On Windows `os.rename` refuses an existing destination. An entry both directories hold as a directory stays in the old one, which is stated in the docstring. `tests/test_stub_remove.py#test_the_dispatcher_carries_the_message` now runs the real group with `HOME` and `USERPROFILE` under the case's directory, and every root-migrate case that calls `main` takes the `hook` fixture, which points both state directories at the case's directory. In this round's run `~/.claude/specseal/` listed the same seven entries before and after. Executed and read.

confirms: round-1#3
`hooks/optin.py#earlier` reads `EARLIER_HEADINGS` the way `marked` reads the marker, and `root-migrate.py#ours` reads the same tuple. `seal.py#import_` refuses before `destination_root` wherever no root is in force and the tree's `seal/` is an earlier release's, whatever `--into` says, and `no_root` and `install_workflow` print `earlier_root()`. The enumeration of writers holds: the `home_paths` and `marked` callers outside `optin` (`git grep -n "home_paths\|optin\.marked\|optin\.earlier"`) are `mode-gate.py`, which acts only on a marked root, `chain_check.py`, `broad_gate.py` and `pact_check.py`, which read and write no root, and the three `seal.py` subcommands the fix wired. `skills/implement/orchestration.md` places the earlier-root paragraph before the project's-own one, pinned by `tests/test_first_setup_asks_once.py::test_a_projects_own_seal_gets_nothing_and_the_root_goes_under_the_git_dir`. `Test_import_::test_refuses_beside_a_root_an_earlier_release_wrote` pins the one line for `import`, `mode` and `pr-checks install`. Both passed. Executed and read.

confirms: round-1#4
`hooks/root-migrate.py#stale_workflow` loads `seal.py` and appends the re-pin step only where `workflow_at` answers `plugin` and `PLUGIN_CLONE` is absent, which only a release before the rename writes. A `seal.py` that will not load, a `SyntaxError` on the hooks' floor included, is caught by `except (Exception, SystemExit)` and leaves the plain line. `ruff.toml:50` lints `seal.py` at py39, and the `floor_syntax` census passed in this round's run. README.md and README.ko.md *Coming from `specseal@specseal`* and the changelog fragment carry the step. `install_workflow` refuses an earlier root, and the move's line asks for the install after the README is rewritten in the working tree, so the step the line names is one the command accepts. `Test_main::test_accepts_the_move_naming_the_workflow_an_earlier_release_wrote` pins both lines and passed. Round 1's executed lines ran again: `v0.22.4`'s `hooks/optin.py:41` reads `WORK_ITEMS = "specs"` and its `chain_check.py:2054` reads `TRAILER = "SpecSeal-Routing"`. Executed and read.

confirms: round-1#5
`hooks/routing.py#parse` maps `OLD_BY_CRAFTER` to `BY_CRAFTER` before the `IMPLEMENTATION_ANSWERS` test (`:257-259`, `:278`), and `hooks/implementer-notice.py#AXES` compares against `BY_CRAFTER`. The mark the notice then reads is `agentic-implementer`, which `rename_state` carries from `specseal-implementer` (`STATE_NAMES` holds `implementer`), so an in-flight item's mark and answer both reach the notice. `Test_parse::test_accepts_the_answer_written_before_the_rename_as_the_crafter` passed. Executed and read.

confirms: round-1#6
`rule_changes.py#order` passes both paths to one `git log --no-renames --diff-filter=A` and keeps each id's first add at either one (`:287`, `:299-302`), so a moved thread takes its place from its first `spec.md`. `Test_module::test_merge_order_of_a_moved_thread_is_its_first_add_before_the_move` and the existing `test_a_spec_moved_into_place_is_ordered_by_the_commit_that_moved_it` passed. Executed and read.

confirms: round-1#7
Every citation of a released work item outside the records is now `<commit>:<path>`. `git grep -ohE '[0-9a-f]{7,40}\^?:seal/specs/[0-9]{10}-[a-z0-9-]+(/[A-Za-z0-9_.-]+)*/?'` outside `seal/threads` lists 22, and `git cat-file -e` resolves each of them. Round 1's enumeration grep, run again, lists only fixture ids and the example `1784780439-center-list-sort` in `skills/implement/SKILL.md:337`. Round 1's `git log --all` lines ran again: the old path answers `5f11923f`, and the thread path is held by no commit. `Test_old_names::test_accepts_an_old_path_only_where_a_commit_holds_it` passed. Executed.

confirms: none
The `old_names` exemptions that round 1 left unjudged each have a sound reason, and none hides an old name in living text that should have been renamed. Each `KEPT_OLD_NAMES` spelling was read at every living line it stands on (`git grep -nF` per spelling, outside the records). `SpecSeal-Routing` appears where `chain_check.py#OLD_TRAILER` reads it and where `docs/the-routing-check.md` explains it. The block markers appear in `install.sh`, `uninstall.sh` and the two skills that replace the block. `# specseal-git-hook` appears where `stub-remove.py` and the docs name the stub's marker. The old clone line appears in `seal.py#OLD_PLUGIN_CLONE`. The install names and the `renames` entry appear in README *Install* and `marketplace.json`. `.specseal` appears only in the 0.3.x by-hand path and its readers' cases. `SPECSEAL_LINT` and `SPECSEAL_LANG` are the live names of two variables a person sets, kept by the frame's no-behaviour-change scope and put to the owner in `gaps.md` *Not verified*. In `OLD_NAME_RECORDS`, `changelog/` holds only released versions, `seal/process/` only `0.22.4.md`, and `seal/threads/` only this work item. `KEPT_FILES` was searched for old names other than the 0.22.x layout and the state names: `hooks/root-migrate.py`, its two case files, and the replay and seeded cases' tests hold none, and `hooks/cmdline_base.py` holds only frozen bytes and one commit-tied citation. Each `# exempt from old_names:` line, twenty-three outside the census and its own cases (`git grep -c`), sits over a 0.22.x path that a reader takes from history or the 0.3.x by-hand path writes, the old `smith` answer, another tool's `spec.md`, a stub's recorded bytes, or a word census's pattern for the old brand. Two exemptions are wider than their reasons, and neither ships a wrong name now. The prefixes `seal/process/` and `seal/threads/` also pass every future archive and frame. The whole-file `hooks/cmdline_base.py` also passes its rider, which is living text above the frozen bytes. Read, with the searches executed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| `stale_workflow` loading `seal.py` and `workflow_at` returning under the hooks' floor interpreter, Python 3.9; this round's run used the repository's venv | `hooks/root-migrate.py:521-535`, `skills/implement/scripts/seal.py:1939-1960` | the orchestrator, reading the floor leg of `.github/workflows/test.yml` on the pull request |
| whether `SPECSEAL_LINT` and `SPECSEAL_LANG` take new names with a grace reading | `seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/gaps.md:45` | the owner |
| the crafter's "seen red" claims for the seven new cases; this round read them and ran the cases green only | `seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/trail/rounds/round-1.md` | the sealer, which re-runs a sample of the crafter's claims |
| the full suite, the repository-wide lint and the typecheck over this branch | the branch | the orchestrator's broad run after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test <scratch>/round-2/test_tmp_round2_probe.py -s -q -p no:xdist --basetemp=<scratch>/round-2/tmp`, three cases over fixture repositories, the hook loaded from the tree with both state directories under the case directory | 3 passed, with printed results. Detached HEAD: after the move was committed on `main`, `git checkout --detach` of the commit before it, `symbolic-ref` exit 1; the start printed "agentic:moved seal/specs/ into seal/ — review the diff and commit" and `git status --porcelain` listed `M  seal/README.md` and `R  seal/specs/1788000001-a/routing.md -> seal/threads/1788000001-a/routing.md`. Stopped rebase: `git rebase main` exit 1 with `UU x.txt`; the start moved `1788000002-b/routing.md`; after resolving, `git rebase --continue` exit 0; `b2` carries `rename seal/{specs => threads}/1788000002-b/routing.md (100%)`, and `ls-files` lists `seal/specs/1788000002-b/rounds/round-1.md` beside `seal/threads/1788000002-b/routing.md`. Local mode: on `main` with a marked `.git/seal/` the start printed nothing; on `old-shared` it printed "agentic:moved seal/specs/ into seal/", staged the README and the rename, and `optin.home_at` answered the tree's `seal/`. The probe file and its fixtures were deleted after the run |
| `bin/test tests/test_root_migrate.py tests/test_seal.py tests/test_routing.py tests/test_settle.py tests/test_censuses.py tests/test_first_setup_asks_once.py tests/test_stub_remove.py tests/test_optin.py -q` | 885 passed, exit 0. `ls -la ~/.claude/specseal/` was the same before and after, apart from its parent's link count; the `~/.claude/agentic/` the run created, holding only `version-check`, was removed |
| `git cat-file -e` over each of the 22 `<commit>:seal/specs/...` citations `git grep -ohE` listed outside `seal/threads` | all 22 resolve |
