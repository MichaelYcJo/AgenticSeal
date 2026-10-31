# Review round 3: 1793457436-row-deletion-check-and-a-symlink

```seal
target: 9622a7a5, fixes 1fbecdf9..9622a7a5
```

This is a verifying round. It reads the range `1fbecdf9..9622a7a5`. `git diff --stat 1fbecdf9 HEAD` outside the work item's directory lists one file, `.claude-plugin/plugin.json`, one line, changed by 4000a24f (executed). Every other commit in the range touches only `seal/threads/1793457436-row-deletion-check-and-a-symlink/`: the round 2 record (39d2d5db), the fix of its finding (b3c2c162), its close block (c4287245), the broad run record (4f3b9908), the sealer's two withheld blocks (c1f1e954, bed475df), the repair of two record sentences (62bd3f75), and one row of `frame/plan.md` *Judgments of the run* (9622a7a5) (executed, `git log --name-only`). The work ran in the branch worktree at 9622a7a5, which the prompt named. No clone was made and nothing was written there but this record.

Carried from round 2 as coordinates and not established again: the code and the cases (`skills/verify/scripts/unverified_check.py`, `tests/skills/test_unverified_check.py`) and round 2's verdicts on them. Neither file changed in the range (executed, the diff above), so they are outside this round's target. The two Windows rows of `## Not judged` are carried unchanged. Every verdict below was reached this round.

## Findings

None. The version move and the record repairs hold, and nothing else in the tree has to move with the version.

## Confirmations

```seal
confirms: round-2#1
```
What holds: round 2's finding asked two frame sentences to stop standing on the facts before the mode read. The close claims b3c2c162 folded both with the round's paste-ready text. `frame/design.md:36` now names `#mode_at` as the read that a precise notice would cost, one more `git ls-tree` per closing memo, and `frame/plan.md:43` counts three report lines and says the changelog fragment states all three. Both read word for word as the finding's fenced text. b3c2c162 touches those two files alone, both inside the work item's records. Read, and executed for the commit's file list.

```seal
confirms: none
```
What matched: the version move. 4000a24f changes one line of `.claude-plugin/plugin.json`, `"version": "0.27.0"` to `"version": "0.27.1"`, and nothing else in the file. The base a92c358b (`origin/release/v0.27.1`) holds 0.27.0, as does `origin/main`, and the only tag of the line is `v0.27.0`. The version matches the branch the pull request targets, `release/v0.27.1`, and the open milestone `release: 0.27.1`, which issue #19 carries (`gh issue view 19 --json milestone`). The commit subject claims this is the release's first work item. The base holds no fragment of this release, since a92c358b is the settle that removed the released work items' directories. The local branches of the two sibling items, `fix/1150-replay-targets-reads-both-layouts` and `fix/1128-readers-state-the-shapes-they-pass`, both still name 0.27.0. So no other branch moves the version and no move conflicts with this one. Executed.

```seal
confirms: none
```
What matched: nothing else in the tree has to move with the version. Two methods listed the class. First, stored copies: `git grep -n -E '0\.27\.(0|1)'` outside the work item finds `.claude-plugin/plugin.json:4` and two test docstrings that name releases as history, `tests/skills/test_chain_check.py:2512` and `tests/text/test_the_rules_have_one_owner.py:686`. Neither docstring is in the range. That search is complete for the literal spelling, and a copy spelt another way would escape it. Second, readers: `git grep -l` on `plugin\.json|plugin_version|\bversion\(` lists 18 test modules and about 25 code and document files. That list is a search on wordings, so it is a sample (contract rule 12). Of the readers named in the prompt, the `hygiene` step *a change to what ships must move the version* (`.github/workflows/hygiene.yml:70-110`) exits 0 for any base other than `main`. At the release pull request it reads 0.27.0 at `main` against 0.27.1 here and passes. `tests/hooks/test_version_check.py` builds its own `plugin.json` in a temporary directory, so the root's version does not reach it. `tests/behaviour/test_release_hygiene.py` reads the running version from the root and refuses a loaded file naming a version at or above it, less the tagged ones. At 0.27.1 the stored-copy search above finds no such file. `hooks/lib/core.py`, `skills/verify/scripts/broad_gate.py` and `skills/implement/scripts/seal.py` read the version when they run and keep no copy (read). The 18 test modules ran through `bin/test` at 9622a7a5 and gave 1162 passed, 1 skipped, exit 0. The skip is `tests/skills/test_broad_gate.py:1126`, "the shell here is not cmd.exe". Executed.

```seal
confirms: none
```
What matched: where the version move sits in the branch. `docs/branch-and-release.md:37-39` places the move in the commit that adds the changelog fragment of the release's first work item, here b2e4ca18. The orchestrator made it later, in 4000a24f, after round 2's target. The plan row at `frame/plan.md:51` says so and gives its grounds, which the tree confirms. `chain_check.py --worktree` printed, before this record, `round-2.md:0  the last round's target: is behind HEAD: commit 4000a24f after it touches .claude-plugin/plugin.json`. The two sections the row cites exist, `docs/the-review-record.md:113` and `docs/branch-and-release.md` *Cutting a release*. The departure reaches no line the release ships. Pull requests into a release branch land as squash merges: a92c358b and 7a8899d5 each have one parent. So this pull request's diff against `release/v0.27.1` carries the move whichever commit inside it made the move. Executed and read.

```seal
confirms: none
```
What matched: the repair in 62bd3f75. `frame/design.md:7` and `frame/design.md:61` now cite `docs/the-record-layout.md` *The fold, and what tells it from a deletion* for the rule that a `## Not verified` table that lost rows fails the run. That section opens at `docs/the-record-layout.md:78`, and `:91-94` says a pull request removing a row from a table is still a deletion, with one predicate answering `seal unverified --baseline`. The bullet that `frame/design.md:8` names stands inside the same section, which runs to the next heading at `:237`. `trail/phases/phase-1.md:5` now says `seal/follow-up.md` holds no row naming #19, `unverified_check` or a link. A `grep -n -i -E` on those words over the file exits 1 with no line. Executed and read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the link cases run or skip on the Windows legs (`frame/questions.md` Q1), carried from round 1 | `tests/skills/test_unverified_check.py` | a measurement: the Windows legs of `.github/workflows/test.yml` on this pull request; naming a skip there is #1221's |
| What Windows `os.path.realpath` and `os.path.islink` answer for a tracked link whose target is on another drive, run end to end, carried from round 1 | `skills/verify/scripts/unverified_check.py` | a maintainer with a Windows machine holding two drives |
| Whether this pull request is the first into `release/v0.27.1`, as 4000a24f's subject says. If a sibling merges first without a move, the move still reaches the branch with this pull request | `.claude-plugin/plugin.json` | the orchestrator, at the merge order of the three 0.27.1 items |
| The full suite, the repository-wide `ruff check` and `ruff format --check` at HEAD. `trail/gate.md` names a run at 4000a24f, and only the work item's records follow it | `trail/gate.md` | the orchestrator, through `seal gate`, and the sealer at its next run |

## Probes

| Command | Result |
|---|---|
| `git diff --stat 1fbecdf9 HEAD -- . ':!seal/threads/1793457436-row-deletion-check-and-a-symlink'` | one file, `.claude-plugin/plugin.json`, one line each way |
| `git grep -n -E '0\.27\.(0\|1)' -- . ':!seal/threads'` | `.claude-plugin/plugin.json:4`, `tests/skills/test_chain_check.py:2512`, `tests/text/test_the_rules_have_one_owner.py:686` |
| `bin/test` over the 18 test modules that `git grep -l -E 'plugin\.json\|plugin_version\|\bversion\('` lists under `tests/`, `-q` | 1162 passed, 1 skipped, exit 0 |
| `bin/test` over seven of them with `-rs` | 828 passed, 1 skipped: `tests/skills/test_broad_gate.py:1126`, the shell is not cmd.exe |
| `git show <branch>:.claude-plugin/plugin.json` for the two sibling branches, `origin/main` and a92c358b | 0.27.0 in each |
| `gh issue view 19 --json milestone,state`; open milestones; `git tag -l 'v0.27*'` | `release: 0.27.1`, open; milestones `release: 0.27.1`, `release: 0.27.2`, `release: 0.28.0` open; tag `v0.27.0` alone |
| `grep -n -i -E '#19\b\|unverified_check\|symlink\|\blink' seal/follow-up.md` | exit 1, no line |
| `python3 skills/code-review/scripts/chain_check.py --baseline a92c358b --root . --worktree`, before this record | exit 0, not judged as a ready pull request; `round-2.md:0` names 4000a24f as unread, and `guarantee.md` is behind HEAD |
