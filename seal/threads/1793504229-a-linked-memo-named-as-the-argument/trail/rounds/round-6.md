# Review round 6: 1793504229-a-linked-memo-named-as-the-argument

```seal
target: a6c538e9, fixes 83133cc8..a6c538e9
```

This is a narrow verifying round. Its target is the diff from round 5's target (83133cc8) to HEAD: the round 5 record at 8c498aee, the test commit 4045ddf7, and the phase record commit a6c538e9. The base is `origin/release/v0.27.1`, whose merge base with HEAD is 48d035aa. The scope is the one the orchestrator set after its broad run: whether the new case asserts a real refusal of `repository_of` by `CONTRIBUTING.md` *The test layout*, `bin/seal layout --check tests` and the module run, and whether any other class this branch added or changed in `tests/skills/test_unverified_check.py` stands without a `test_refuses_` case. No `seal/parity.md` is declared, so no original is compared and no `original:` line is owed. The record language is English, since `seal/config.md` has no `Record language` row.

Round 5 closed no finding, so no `confirms:` line answers one. Carried from rounds 1 to 5, not re-established: where `repository_of`, `absolute`, `nearest_existing` and `main`'s repository lookup stand in `skills/verify/scripts/unverified_check.py`, and that `main` takes the root from `repository_of(args.path[0])`. Re-derived this round: every verdict below, and the line numbers, read at a6c538e9. Every run was in a `git clone --no-local` of the worktree at a6c538e9.

The orchestrator's account and the phase record's section *The broad gate's fix pass* are claims. The claims, and what this round found, are set out under each confirmation below.

## Findings

### 1. `absolute`, a public function this branch added, has no class `Test_absolute`, so the test layout's rule for it goes unkept

```seal
severity: should
location: `tests/skills/test_unverified_check.py:1544`, `skills/verify/scripts/unverified_check.py:1095-1119`
evidence: executed `bin/seal layout --check tests`, `git show 48d035aa:skills/verify/scripts/unverified_check.py`
regression: round-1#1
```

Why it matters: the unit is `absolute` (`skills/verify/scripts/unverified_check.py:1095-1119`), which round 1's fix pass added in b7d19345. `frame/plan.md:34`, the phase 1 *Verified by* row, names the classes the phase is verified by, and `frame/design.md` *Data & interfaces* names no `absolute`; b7d19345 added `absolute` as a public top-level function and gave it no class, so the gap came from that fix pass and not from the frame. `CONTRIBUTING.md:241-245` says the test file "holds one class per public top-level function of the module, `Test_<name>`", and that each such class holds a `test_accepts_` case and a `test_refuses_` case. `absolute` has no leading underscore and stands at the top level. At 48d035aa the module has no `absolute` (executed, `git show 48d035aa:...`, no `def absolute`). At a6c538e9, `bin/seal layout --check tests` exits 0 and prints `report: skills/verify/scripts/unverified_check.py: function absolute has no class Test_absolute` (executed). It is the one `report:` line for this module. No case in the module calls `absolute` directly (executed, `grep -n "absolute(" tests/skills/test_unverified_check.py` found none). Its branches are pinned only through its callers. The `ELOOP` branch is pinned by `Test_main::test_refuses_a_row_lost_under_a_named_link_loop_as_real_reads_it`, and the `..` branch by `Test_repository_of::test_accepts_a_parent_as_real_reads_it`.

This is the same rule the broad gate refused for `Test_repository_of`, one step earlier: there the class stood without its refusing case, and here the function stands without its class. `skills/verify/scripts/test_layout.py:44-46` grades a missing class as a `report:` line, not a `refused:` line, so the gate passes and no record of the branch names it. The fix pass's own hand-back read only the `refused:` lines (`trail/phases/phase-1.md`, *The runs* of *The broad gate's fix pass*: "exits 0 with no `refused:` line"). This is `should` and not `must`: the repository's own check grades a missing class as a report, so it does not block a merge, and what the release would ship is a function whose class a contributor looks for and does not find (`CONTRIBUTING.md:257-259`).

Two fixes keep the rule. One is a class for `absolute`, as below. The other is renaming it `_absolute`, since its two callers, `repository_of` and `as_named`, are in the same module, and `CONTRIBUTING.md:243` lets a private function go without a class. The phase record calls `absolute` "one rule two callers need" (`trail/phases/phase-1.md`, *Two departures from the frame*), which a private name also keeps. Either fix is shown red as contract rule 15 asks before it is committed.

```python
class Test_absolute:
    def test_accepts_a_link_kept_by_its_text(self, tmp_path):
        """A path with no `..` and no link loop is made absolute by its
        text, so a link on it stays as the person named it."""
        (tmp_path / "target").mkdir()
        symlink_or_skip(str(tmp_path / "target"), str(tmp_path / "link"), True)
        given = str(tmp_path / "link" / "gaps.md")
        assert UC.absolute(given) == os.path.abspath(given)

    def test_refuses_to_drop_a_parent_by_its_text(self, tmp_path):
        """`os.path.abspath` drops `link/..` by its text and names the
        link's own directory. The path is read as `real` reads it."""
        (tmp_path / "far" / "target").mkdir(parents=True)
        symlink_or_skip(
            str(tmp_path / "far" / "target"), str(tmp_path / "link"), True
        )
        given = str(tmp_path / "link" / "..")
        assert same_path(UC.absolute(given), os.path.realpath(given))
```

The precondition at the OS boundary: on POSIX, `os.path.realpath("link/..")` reads `..` from the link's target, so it gives `far`, and a body that returns `os.path.abspath` gives `tmp_path` and fails the second case. On Windows `realpath` may read `..` by its text, as the docstring of `test_accepts_a_parent_as_real_reads_it` allows. There the second case passes for either body, so it is seen red on POSIX. The class goes after `Test_repository_of`, before `Test_as_named`.

```seal
verdict: fixed 9580f0f9
answer: Fixed by the second option, not the paste-ready class: `absolute` is renamed `_absolute` at its definition and at its two calls, in `repository_of` and `as_named`, and `as_named`'s docstring names it by the new name. Its only callers are those two, in the same module, so `CONTRIBUTING.md` *The test layout* owes a private helper no class, and `Test_repository_of` and `Test_as_named` keep the cases that pin its `..` branch, and `Test_main` the case that pins its loop branch. `git grep` found no other caller and no attribute access to the old name in the tree. `trail/phases/phase-1.md` and `gaps.md` name the function by the new name. After the rename, `bin/seal layout --check tests` exits 0 with `151 files read, 0 refused, 86 declare no TARGET` and prints no `report:` line for `skills/verify/scripts/unverified_check.py`, where this round's probe at a6c538e9 printed `function absolute has no class Test_absolute` (executed at 9580f0f9; the earlier line read from `## Probes`). `bin/test tests/skills/test_unverified_check.py tests/skills/test_test_layout.py -q` gives 472 passed (executed), and `uvx ruff check` and `uvx ruff format --check` on the module exit 0 (executed).
```

## Confirmations

```seal
confirms: none
```
What holds: the new case asserts a real refusal of `repository_of`. `Test_repository_of::test_refuses_a_link_that_stands_in_no_repository` (`tests/skills/test_unverified_check.py:1581-1587`) links `link` to `target` under `tmp_path` and asserts that `repository_of("link/gaps.md")` is None (read). None is the answer `repository_of` gives where there is no repository (`skills/verify/scripts/unverified_check.py:1043-1061`). `main` refuses on it with exit 2 and `--baseline ... needs a git repository, and ... is not in one` (`:1682-1690`, read). So the case's name says what it asserts. The path takes the branch the case is written for. `nearest_existing` stops at `link`, `repo_root(real(link))` is None, and the walk reaches `os.path.islink(link)` and asks git at `tmp_path`, which answers no repository (read, `:1054-1060`). The case assumes `tmp_path` lies in no repository. That is the same assumption `test_accepts_the_repository_holding_a_link_out_of_every_repository` makes in the same class (`:1556-1566`), so the case adds no new premise. It uses the group's helper, `tests/conftest.py#symlink_or_skip`. The docstring says a link names a repository only where git finds one at the link's own directory, which is what `:1059` does.

```seal
confirms: none
```
What matched: the new case pins something its group does not. Three mutations were made through `Edit` in the clone, and after each the module ran whole (executed). The first returned `top or start` in place of `top`. It failed the new case and two `Test_main` cases that reach the None through `main`: `test_refuses_a_baseline_outside_a_repository` and `test_refuses_a_path_on_another_volume_instead_of_aborting`. The second made the link branch take `os.path.dirname(p)` without asking git. It failed the new case, `Test_repository_of::test_accepts_the_repository_holding_a_link_out_of_every_repository`, `Test_as_named::test_refuses_to_keep_a_name_outside_every_repository`, and `Test_main::test_refuses_a_row_lost_through_a_named_link_out_of_every_repository`. The third changes only the answer for a link that stands in no repository: `repo_root(...) or os.path.dirname(p)`. It failed the new case and `Test_as_named::test_refuses_to_keep_a_name_outside_every_repository` alone, 388 passed. So within `Test_repository_of`, the new case is the only one that pins a link in no repository. The module also pins that branch through `as_named`'s class, which tests a different function. The phase record says "No other case in the class pins the None", which holds within the class. The record does not say the module has no such case, so the claim is not overstated. The phase record says the case was seen red by two `seal mutate` runs, and this round's first two mutations are those two, run module-wide instead of `-k Test_repository_of`. Both failed the new case. `bin/seal layout --pairs tests/skills/test_unverified_check.py` exits 0 with 0 pairs (executed), so no duplicate check names the new case.

```seal
confirms: none
```
What matched: no class this branch added or changed in `tests/skills/test_unverified_check.py` stands without a `test_refuses_` case (executed). `bin/seal layout --check tests` exits 0 with `151 files read, 0 refused, 86 declare no TARGET` and no `refused:` line. The classes the branch added or changed in this file, from `git diff 48d035aa..HEAD`, are `Test_repository_of`, `Test_as_named` and `Test_spellings`, which were added, and `Test_main`, which was changed. Their cases, counted by name at HEAD (executed): `Test_repository_of` has 3 accepting and 1 refusing; `Test_as_named` has 3 and 1; `Test_spellings` has 1 and 1; `Test_main` has 15 and 30. The diff's hunk at the old line 1541 has `class Test_real:` only as context and changes nothing in that class. The one gap the same command reports for this module is a missing class, not a missing case, and that is finding 1.

```seal
confirms: none
```
What matched: the phase record's account of the cause holds (executed). The record says `e4ba92f5` added `Test_repository_of` with two accepting cases and no refusing case, that no later commit added one, and that b46c616b only renamed an accepting case. The class's cases at each commit of the branch that touched the file show this. e4ba92f5 has two accepting cases. b7d19345 adds a third accepting case, `test_accepts_a_parent_after_a_link_as_the_file_system_reads_it`. b46c616b renames it `test_accepts_a_parent_as_real_reads_it`. 4045ddf7 adds the refusing case. The record's runs reproduce. `bin/seal layout --check tests` exits 0 with no `refused:` line. `bin/test tests/skills/test_unverified_check.py tests/skills/test_test_layout.py -q` gives 472 passed with exit 0, which includes `Test_main::test_accepts_this_repositorys_tests`, the case the broad run failed. `uvx ruff check` and `uvx ruff format --check` on the test file exit 0. The record's reading of `CONTRIBUTING.md` *The test layout* is right: only `Test_module`, an `e2e` flow's classes and a document target's classes are free of the pair (`CONTRIBUTING.md:244-250`), and `repository_of` is none of them.

```seal
confirms: none
```
What matched: the label on the broad gate is honest. a6c538e9 ends its section with "The broad gate is the orchestrator's to run again", and no record on the branch claims a broad run after 4045ddf7 (read). This round ran none.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the new case runs, and not skips, on the Windows legs, and whether the runner's temporary directory lies in no repository there. Read, and no run here reached Windows | `tests/skills/test_unverified_check.py:1581-1587` | the Windows legs of `.github/workflows/test.yml` on this pull request |
| The full suite, the repository-wide `ruff check` and `ruff format --check`, at a6c538e9 | the branch at a6c538e9 | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `bin/seal layout --check tests`, in the clone at a6c538e9 | EXIT=0, `151 files read, 0 refused, 86 declare no TARGET`. For this module, one line: `report: skills/verify/scripts/unverified_check.py: function absolute has no class Test_absolute` |
| `bin/seal layout --pairs tests/skills/test_unverified_check.py` | EXIT=0, `1 files read, 0 pairs` |
| `bin/test tests/skills/test_unverified_check.py tests/skills/test_test_layout.py -q` | EXIT=0, 472 passed |
| `repository_of`'s `return top` made `return top or start` through `Edit`, then `bin/test tests/skills/test_unverified_check.py -q -p no:xdist -rf` | EXIT=1, 3 failed, 387 passed: the new case, `Test_main::test_refuses_a_baseline_outside_a_repository`, `Test_main::test_refuses_a_path_on_another_volume_instead_of_aborting` |
| the link branch's `top = repo_root(real(os.path.dirname(p)))` made `top = os.path.dirname(p)` through `Edit`, the same command | EXIT=1, 4 failed, 386 passed: the new case, `Test_repository_of::test_accepts_the_repository_holding_a_link_out_of_every_repository`, `Test_as_named::test_refuses_to_keep_a_name_outside_every_repository`, `Test_main::test_refuses_a_row_lost_through_a_named_link_out_of_every_repository` |
| the same line made `top = repo_root(real(os.path.dirname(p))) or os.path.dirname(p)` through `Edit`, the same command | EXIT=1, 2 failed, 388 passed: the new case, `Test_as_named::test_refuses_to_keep_a_name_outside_every_repository`. The line was put back through `Edit`, and `git diff --quiet` in the clone exited 0 |
| the cases of `Test_repository_of` at each commit of `git log 48d035aa..HEAD -- tests/skills/test_unverified_check.py`, read through `git show` | two accepting cases from e4ba92f5, a third from b7d19345, renamed at b46c616b, the refusing case from 4045ddf7 |
| `uvx ruff check` and `uvx ruff format --check` on `tests/skills/test_unverified_check.py` | EXIT=0; EXIT=0 |

The clone and the round's scratch outputs were removed before hand-back.
