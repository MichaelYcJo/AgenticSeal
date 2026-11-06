# Review round 1: 1793922919-three-link-cases-skip-on-windows-by-platform

```seal
target: 54286764 against release/v0.32.6
```

The range is `063e0678..54286764`, four commits. The frame on this rung is issue #1247 and `gaps.md` *Scope confirmation*; there is no `frame/design.md` or `frame/plan.md`, and no `seal/parity.md`. This is round 1, so no fact is carried from an earlier round: every coordinate below was opened in this round's clone at `54286764`.

Stage 1 axes: the issue's *Done when* line, the scope line, the class of link-making calls under `tests/`, the version move against `docs/releasing/branch-and-release.md`, and the closing memo's rows. Stage 2 axes: argument order of the helper call against `Path.symlink_to`, the link's parent directory at each call, the `directory` flag a Windows directory link needs, the module's remaining imports, and what the Windows legs did with the three cases.

## Findings

None. No defect was found on any axis named above.

## Confirmations

What matched: the issue's *Done when* holds. The orchestrator's `tests` run 42134062891 at `54286764` completed with every job `success`, the four `windows-latest` legs among them. A grep of the four Windows job logs for `test_agentic_pytest_record`, `symlink` and `symbolic links are not available` matched no line, so none of the three cases was skipped or failed on Windows; the legs printed 35 `SKIPPED` lines between them, none naming the module. The run's `test-durations-6` artifact, uploaded only by a Windows leg (`.github/workflows/test.yml:176-180`, `if: matrix.store != ''`), prices the three cases at 0.61, 0.60 and 0.62 seconds. The committed `.test_durations:3059`, `:3062` and `:3067` price them at under a thousandth of a second, which is a skip. So the three cases ran and passed on `windows-latest`. Executed: `gh run view 42134062891`, `gh run view --job` for the four Windows jobs, `gh run download 42134062891`.

What matched: the crafter claimed the three cases call `symlink_or_skip(target, link, directory=True)` and the three platform skips are gone. `tests/skills/test_agentic_pytest_record.py:881`, `:902` and `:926` call `symlink_or_skip(root, link, directory=True)`, `symlink_or_skip(root, link, directory=True)` and `symlink_or_skip(shared, root / "shared_tests", directory=True)`. Each passes the old `symlink_to` receiver as the link and its argument as the target, which is the order `tests/conftest.py:641` hands to `os.symlink(target, link, ...)`. The parent of each link (`tmp_path`, `root`) exists when the call is made, so the helper's parent assertion at `tests/conftest.py:638-639` holds. The import at `:38` adds `symlink_or_skip`, and `os` stays used at `:42` and `:931`. Read.

What matched: the crafter claimed `bin/test tests/skills/test_agentic_pytest_record.py -q -rs` exits 0 with 47 passed and none skipped. This round's run of the same command in the clone exited 0 with `47 passed`, and the three cases selected by `-k` printed `3 passed, 44 deselected`. Executed.

What matched: the crafter's `seal mutate` claim, that a raised `OSError` in place of `os.symlink` read `3 passed` at `296475ec` and `SKIPPED [3] tests/conftest.py:643` at `b97741a0`, was not re-run. Reading settles what it shows: at `296475ec` the cases called `Path.symlink_to` at `:882`, `:904` and `:929` (checked with `git grep` at that commit), so a broken helper could not reach them, and at HEAD they call the helper, whose `pytest.skip` stands at `tests/conftest.py:643`. Read.

What matched: `gaps.md` *Scope confirmation* says no other file of the suite changes. `git diff --stat 063e0678..54286764` lists `tests/skills/test_agentic_pytest_record.py` as the one file under `tests/`. Executed.

What matched: the phase record's census is whole for the class the issue names, a link case skipped by platform. `git grep -n 'skipif(os.name\|skipif(sys.platform\|platform.system()' -- tests` lists seven decorators at HEAD, none with a reason about links. `git grep -n 'symlink_to(\|os\.symlink(' -- tests` lists `tests/conftest.py` and `tests/github/test_finding_counts.py:255` alone, and the second search the phase record names (`ln -s`, `mklink`, `CreateJunction`, `hardlink_to`, `os.link(`) matched nothing. The phrase `a symlink needs privileges` stands only in this work item's `changelog.md` and `trail/phases/phase-1.md`. Every coordinate the phase record cites at `296475ec` (`:868`, `:882`, `:890`, `:904`, `:916`, `:929`, `tests/conftest.py:620`) stood where it says. Executed.

What matched: the version move. `docs/releasing/branch-and-release.md:30-38` moves the version in the commit that adds the changelog fragment of the release's first work item. `9a8dd7ec` moves `.claude-plugin/plugin.json` from `0.32.5` to `0.32.6` and adds `changelog.md` in the same commit; the base `063e0678` held `0.32.5`. `gh pr list --base release/v0.32.6 --state all` lists one earlier pull request, #1400, a settle with no work item, which left the version alone. `git grep -n '"version"' -- '*.json'` lists `plugin.json` alone. `bin/test tests/behaviour/test_release_hygiene.py -q -rs` exited 0 with 33 passed. Executed. That this item is the release's first to merge is the orchestrator's choice, read as a claim and not judged here.

What matched: the fragment opens with `### Fixed`, as the fragment of `1793863000-mutate-restore-is-held-by-no-case` at `a55c82c2` does for a change to tests alone. Read.

No test is added, so no case is owed a red and none is read against its group. `.test_durations` still prices the three cases at their skip time; the `durations` job of each run refreshes it, so that is no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| `gaps.md` `## Not verified` row 1 asks for the Windows legs' reading, and run 42134062891 answers it as the first confirmation above states. Marking the row `closed` is a write to the closing memo, which this round does not make | `seal/threads/1793922919-three-link-cases-skip-on-windows-by-platform/gaps.md` | the orchestrator |
| `tests/github/test_finding_counts.py:255` makes a link with a bare `Path.symlink_to`, the other direction of the defect `tests/conftest.py:620` names, so on a Windows machine without the link privilege that case fails rather than skips. This branch did not introduce it, and it lies outside the three cases issue #1247 scopes. On run 42134062891 it passed on every Windows leg, so CI does not show it. `gaps.md` `## Not done` names it with no home, and whether it gets an issue of its own is not this round's to decide | `tests/github/test_finding_counts.py:255` | the orchestrator |
| The full suite, the repository-wide lint and the typecheck at HEAD. The crafter's label `unverified` is honest: phase 1 ran one module, on macOS | the repository | the orchestrator, at the broad gate |

Nothing stays open from this round. What comes due is the orchestrator's broad run, then the sealer's spawn.

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_agentic_pytest_record.py -q -rs` | exit 0, `47 passed` |
| `bin/test tests/skills/test_agentic_pytest_record.py -q -rs -v -p no:xdist -k 'rootdir_named_through_a_symlink or argument_named_through_a_symlink or symlinked_directory_under_the_rootdir'` | exit 0, `3 passed, 44 deselected` |
| `bin/test tests/behaviour/test_release_hygiene.py -q -rs` | exit 0, `33 passed` |
| `gh run view 42134062891 --json status,conclusion,jobs` | `completed success`; every job `success`, `release-report` skipped |
| `gh run view 42134062891 --job <id> --log`, for the four `windows-latest` jobs, grepped for the module and the helper's skip reason | no line matched; the legs ended `1502 passed`, `521 passed`, `1099 passed, 17 skipped`, `3066 passed, 18 skipped` |
| `gh run download 42134062891`, grepped for the three case names | `test-durations-6` prices them at 0.61, 0.60 and 0.62 seconds |
