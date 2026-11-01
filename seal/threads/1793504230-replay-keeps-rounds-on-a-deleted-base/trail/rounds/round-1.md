# Review round 1: 1793504230-replay-keeps-rounds-on-a-deleted-base

```seal
target: 61ff39aa against release/v0.27.1
```

This round reviews the branch `fix/1224-replay-keeps-rounds-on-a-deleted-base` at 61ff39aa against `origin/release/v0.27.1` at 48d035aa, in a `git clone --no-local` of the worktree with the origin's branches, tags and `refs/pull/*/head` fetched and pruned. No earlier round exists, so this round carried no fact from one. Every fact below was established this round.

## Findings

### 1. The docstrings call LANDED "the commit the work landed on", a phrase the two callers read in opposite ways, and the commit `targets` passes is at times neither

```seal
severity: should
location: `evals/scripts/replay_targets.py:528-531`, `evals/scripts/replay_targets.py:793-795`
evidence: executed `git log --format=%h --diff-filter=A v0.27.0 -- seal/threads/1793438028-pre-0-23-upgrade-readings-removed/trail/rounds/round-1.md`, `git log -1 --format=%h v0.27.0 -- seal/threads/1793438028-pre-0-23-upgrade-readings-removed/trail/rounds/round-1.md`, `git log --format=%h --diff-filter=A v0.27.0 -- seal/threads/1793443708-settle-keeps-a-gaps-file-anywhere/trail/rounds/round-1.md`, `git log -1 --format=%h v0.27.0 -- seal/threads/1793443708-settle-keeps-a-gaps-file-anywhere/trail/rounds/round-1.md`
```

Why it matters: `frame/design.md` *Scope* item 3 asks the docstrings to say what LANDED is for each caller, and `trail/phases/phase-1.md` claims they now do. `ref_base` (`evals/scripts/replay_targets.py:528-531`) calls LANDED "the commit the work landed on" and argues from it: "a squash puts none of TARGET's commits on that branch". `round_target` (`evals/scripts/replay_targets.py:793-795`) repeats "LANDED is the commit the work landed on" and then names two callers. `targets` passes the commit that last wrote the record. `seed_defects.py#target_at` passes the shipped commit's first parent.

"The commit the work landed on" has two readings. Read as the commit the work was put on top of, it is the first parent that `seed_defects.py` passes, the branch's tip before the squash. Read as the commit the work landed in, it is the squash itself. `targets` passes neither for every record. Of the 10 work items whose rounds this change newly keeps over v0.27.0 and v0.26.0, 8 have the item's own squash as the last writer of round 1 (executed, each record's adding commit set beside its last writer). Two have a later commit of another work item. Round 1 of `1793438028-pre-0-23-upgrade-readings-removed` was added by 5560c742 and last written by 7a8899d5, #1198's squash. Round 1 of `1793443708-settle-keeps-a-gaps-file-anywhere` was added by ea73e94f and last written by 7a8899d5.

The base is still right for both. 7a8899d5 holds no commit of either target. The base each gets equals the merge-base of its target with every tip `release/v0.27.0` held from its base onward (`## Probes`, the branch-history row). What makes it right is that no commit of the branch's line, at the landing or after it, holds the target's commits. `frame/plan.md` row A4 states that argument, and neither docstring does. An agent who judges a wrong base reads these docstrings and takes LANDED for one commit, while the code hands it another. #1228's crafter edits this module next and reads the same text. `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* asks text an agent reads to have one reading.

The fix rewrites both docstrings in place. It names what LANDED stands for and the property each caller's commit has:

```python
def ref_base(target, ref, landed=None):
    """The merge-base of TARGET and REF, or an empty string. Where REF no
    longer resolves, a release branch deleted after its release, LANDED
    stands for it: a commit of the line the work was squashed onto, the
    tip the squash landed on or any commit from the squash on. A squash
    puts none of TARGET's commits on that line, so LANDED and TARGET share
    the fork REF named.

    A tip that holds TARGET, the last writer of a branch still in progress
    or a branch merged with a merge commit, gives no base: their merge-base
    is TARGET itself, and the case would review an empty diff."""
```

```python
    for this tree's check. LANDED stands for a base ref that no longer
    resolves (`ref_base`): `targets` passes the commit that last wrote the
    record, the squash that landed the work or a later commit that
    rewrote the record, and `seed_defects.py#target_at` the shipped
    commit's first parent, the tip the squash landed on. A
```

## Confirmations

```seal
confirms: none
```
What matched: the issue's first *Done when* and `frame/design.md` Scenario 1. The phase claimed that `replay_targets.py --list` leaves no round out as `the target line names no base that resolves`. Executed in the clone at 61ff39aa and, with `evals/scripts/replay_targets.py` checked out at 48d035aa, at the base: both runs printed 63 lines, exited 0 and wrote nothing to stderr. The base gave 18 such lines, and 61ff39aa gives none: 41 kept, 22 left out (15 `no next round to confirm a fix`, 7 `no fixed finding the next round confirmed`). Each of the base's other 45 lines appears unchanged at 61ff39aa (executed, `comm -23` of the sorted outputs printed nothing). `evals/scripts/replay_targets.py:874-885` passes `written_at` of the record's own path as `landed=`, through the one cached `wrote`, so `written_at` stays the one source (read).

```seal
confirms: none
```
What matched: `gaps.md`'s row for `release/v0.25.2`. The question was whether the base its one record now gets is the base the review saw. It is. The record is round 1 of `1793408293-less-text-means-nothing-said-twice`, `target: 9a803e0b against release/v0.25.2`. GitHub's branch-activity log (`gh api repos/MichaelYcJo/AgenticSeal/activity?ref=refs/heads/release/v0.25.2`, executed) shows three events for that branch. It was created at 13dc7c63 on 2026-10-31T00:55:28Z. It moved once, by PR #1196's merge at 01:44:57Z, from 13dc7c63 to f80f48e6. It was deleted at 07:44:17Z. The target 9a803e0b was committed at 01:12:56Z and descends from 13dc7c63, so the branch's tip was 13dc7c63 throughout the review. The review's base was therefore `git merge-base 9a803e0b 13dc7c63`, which is 13dc7c63. That is the base this change gives (executed, the dump of kept targets). PR #1196's recorded base is `release/v0.25.2` at 13dc7c63 (`gh pr view 1196`, executed).

The same log, read for `release/v0.25.0`, `release/v0.25.1`, `release/v0.26.0` and `release/v0.27.0`, settles the other 17 without the frame's `v<X.Y.Z>^2` comparison. For 9 of those 17 the frame's comparison set a commit beside itself, because the record's last writer is the release branch's last tip, `v<X.Y.Z>^2`. For each of the 18, the merge-base of the target with every tip the branch held from the round's base onward equals the base this change gives (executed). Where an earlier tip gives another answer, that tip is an ancestor of the base. Each such base is a pull request's merge commit, made on the branch as its new tip, so the target, which descends from it, was made after the branch had left the earlier tip. The frame's premise, a release branch that only moves forward, holds for every branch the 18 name: each log shows creation, merges only, and deletion.

```seal
confirms: none
```
What matched: the phase's decision 2, the merge-base comparison in place of `git merge-base --is-ancestor`. The spawn prompt calls this the departure from the frame. It is not one: `frame/design.md` *Data & interfaces*, second bullet, names both tests and says "The crafter picks the test". The comparison holds. TARGET is an ancestor of the tip exactly when the best common ancestor of the two is TARGET. `git merge-base` and `resolve` both print a full SHA, so a record's short SHA compares correctly. The `base and` guard keeps an unresolvable TARGET's empty `resolve` from matching an empty merge-base (`evals/scripts/replay_targets.py:536-538`, read).

The departure the phase does name, decision 3, also holds. `frame/design.md` Scenario 3 said `test_a_labelled_target_names_its_base` would gain a stubbed `--is-ancestor` answer. That case stubs `resolve` from a table without `"T"` (`tests/evals/test_replay_targets.py:631-632`, read), so `resolve("T")` is empty and the guard cannot fire there. The stub was needed only for an `--is-ancestor` call, and the build makes none. The guard is covered with real git by `test_a_tip_that_holds_the_target_gives_no_base`.

```seal
confirms: none
```
What matched: the class scope item 2 names, a tip that holds the target. `git grep` for `merge-base`, `ref_base`, `round_target(` and `landed=` over `evals/scripts` finds one `git merge-base` call, `evals/scripts/replay_targets.py:537` (executed). Both `target_base` and `base_of`, and so both generators and both tip sources, the ref that resolves and LANDED, reach it. The list is whole by that method: it lists every call that computes a merge-base, not a wording.

```seal
confirms: none
```
What matched: the second *Done when* and Scenarios 2 and 3. The two new cases are red against the unchanged generator. With `evals/scripts/replay_targets.py` checked out at 48d035aa, both failed: the deleted-branch case at the kept list, the tip case at the `ref_base` call on a resolving ref pointed at the writer (executed). With only the guard at `evals/scripts/replay_targets.py:538` removed, through a probe edit undone by `git checkout`, the tip case failed at `kept == []` and the deleted-branch case passed (executed). That bears out the phase's claim for each mutant. Read against their group: the module declares `TARGET`, and `bin/seal layout --pairs` names no pair with it (executed). `test_a_labelled_target_names_its_base` stubs `git` and `resolve`. `test_targets_reads_the_next_round_by_the_commit_that_wrote_it` stubs `written_at` and `target_base`. No other case builds a history whose base ref is gone or whose tip holds the target, so each new case covers something its group does not (read).

```seal
confirms: none
```
What matched: Scenarios 4 and 5. The four replay cases and the four seeded cases were each regenerated with `--case NAME --out` into scratch directories at 61ff39aa and with `evals/scripts/replay_targets.py` at 48d035aa. All 16 runs exited 0, and `diff -r` of the two trees printed nothing. `seed_defects.py --list` printed the same 8 lines on both sides (executed). `seed_defects.py` imports the generator under review, so the base-side runs exercised the old `ref_base`.

```seal
confirms: none
```
What matched: the boundary with #1228. `git diff 48d035aa..61ff39aa -- evals/scripts/replay_targets.py` has three hunks. They are `ref_base` (`:527-538`), the docstring of `round_target` (`:793-797`), and `targets` (`:868-886`). `say_unanswered` (`:970`), `main` (`:997`) and the module docstring, its `--case` sentence included, are as they were at 48d035aa (executed).

```seal
confirms: none
```
What matched: scope item 3's test comment, `tests/evals/test_replay_targets.py:643-646`. It now names both callers and drops "where the caller knows that commit". `git grep` for `caller knows` outside `seal/threads` finds nothing (executed). The changelog fragment's two bullets agree with what ran: 18 rounds, the eight cases unchanged, and the reason a left-out round gets. It sits under `### Fixed` (read).

```seal
confirms: none
```
What matched: the suite's label. `gaps.md` *Not verified* names the full suite, the repository-wide lint and the format check as unverified at the head, answered by the orchestrator's `seal gate`. That is the honest label (contract rule 2). The narrow runs agree: `bin/test tests/evals/test_replay_targets.py tests/evals/test_seed_defects.py -q` passed 46, and `uvx ruff check` and `uvx ruff format --check` on the two changed Python files passed (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at 61ff39aa (contract rule 2) | the branch | the orchestrator, by `seal gate --base origin/release/v0.27.1 --record 1793504230-replay-keeps-rounds-on-a-deleted-base` once finding 1 is answered and a verifying round reads the fix |
| Whether every target the unchanged generator keeps over every release tag, v0.0.1 to v0.27.0, comes out equal with LANDED passed. The frame's probe found 184 of 184. This round ran `--list` over the last two tags and the eight `--case` regenerations, not that probe | `frame/design.md` *Grounding*, the every-tag row | the sealer, where it samples the frame's executed claims |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/evals/test_replay_targets.py tests/evals/test_seed_defects.py -q` at 61ff39aa | 46 passed, exit 0 |
| `python3 evals/scripts/replay_targets.py --list` at 61ff39aa and with the generator at 48d035aa | both exit 0, 63 lines, empty stderr; 18 lines name no base that resolves at the base, none at the head; the base's other 45 lines all appear at the head |
| A `python3 -c` dump of `targets(last_tags())` for each kept target whose base ref does not resolve: item, round, target, base, base ref, size, `written_at` | 18 rounds kept through LANDED; no base equals its target; the `release/v0.25.2` round gets 13dc7c63 |
| `gh api repos/MichaelYcJo/AgenticSeal/activity?ref=refs/heads/release/vX.Y.Z` for 0.25.0, 0.25.1, 0.25.2, 0.26.0 and 0.27.0 | each branch: one creation, merges only, one deletion; `release/v0.25.2` held 13dc7c63 from 00:55:28Z to 01:44:57Z on 2026-10-31 |
| For each of the 18 rounds, `git merge-base --is-ancestor` and `git merge-base` of the target with every tip its branch held (the branch-history row) | from the round's base onward, every tip gives the base this change gives; no tip holds a target |
| `gh pr view 1196 --json baseRefName,baseRefOid,mergeCommit` | base `release/v0.25.2` at 13dc7c63, merged as f80f48e6 |
| `git log --format=%h --diff-filter=A` beside `git log -1 --format=%h` on each newly kept item's round 1, at v0.26.0 or v0.27.0 | 8 of 10 last written by their own squash; `1793438028` and `1793443708` last written by 7a8899d5 (finding 1) |
| `--case NAME --out` for the eight committed cases at 61ff39aa and with the generator at 48d035aa, then `diff -r` | 16 runs exit 0; `diff -r` printed nothing |
| `python3 evals/scripts/seed_defects.py --list` at both sides, then `diff` | 8 lines each side; no difference |
| `bin/test tests/evals/test_replay_targets.py -q -k "deleted_release_branch or tip_that_holds"` with the generator at 48d035aa | 2 failed |
| The same, with `ref_base`'s last line edited to `return base` and restored by `git checkout` | 1 failed (`kept == []`), 1 passed |
| `bin/seal layout --pairs` | exit 0; no pair names `tests/evals/test_replay_targets.py` |
| `uvx ruff check` and `uvx ruff format --check` on the two changed Python files | both pass |
