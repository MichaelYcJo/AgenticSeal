# Review round 2: 1793922919-three-link-cases-skip-on-windows-by-platform

```seal
target: 8a038181, fixes 6444e3cc..8a038181
```

This is a verifying round over the three commits after round 1's record: `ad9943fd`, `cc851ef3` and `8a038181`. Round 1 opened no finding, so no close is owed a `confirms:` line. The diff holds new work instead. The orchestrator widened the scope to `tests/github/test_finding_counts.py:255`, which round 1 left in `## Not judged`, and `ad9943fd` builds it as a continuation of phase 1. That commit is reviewed here as code. A unit a build phase made takes neither a `regression:` nor a `reopens:` line. The frame on this rung is issue #1247 and `gaps.md` *Scope confirmation*. There is no `frame/design.md`, no `frame/plan.md` and no `seal/parity.md`.

Carried from round 1, not re-established: the three cases of `tests/skills/test_agentic_pytest_record.py` and their helper calls at `:881`, `:902` and `:926`, which this diff does not touch; the version move in `9a8dd7ec`; and the Windows reading of run 42134062891 at `54286764`. Re-established this round: the census of link-making calls under `tests/`, the helper's body at `tests/conftest.py:620-643`, and every verdict below.

Stage 1 axes: the scope line against the diff, the closing memo's rows and what left it, the phase record's new paragraphs against the tree at `8a038181`, the fragment, and `routing.md`'s grounds. Stage 2 axes: argument order of the new helper call against `Path.symlink_to`, the relative target `held`, the link's parent at the call, the `directory` flag, the widened import, and what the Windows legs did with the fourth case.

## Findings

None. No defect was found on any axis named above.

## Confirmations

What matched: the crafter claimed `ad9943fd` moves the fourth case onto `symlink_or_skip("held", rounds, directory=True)`. `tests/github/test_finding_counts.py:262` makes that call where `rounds.symlink_to("held", target_is_directory=True)` stood. `Path.symlink_to` is called on the link and takes the target, and the helper takes the target first, so `held` is the target and `rounds` the link, the order `tests/conftest.py:641` hands to `os.symlink(target, link, target_is_directory=directory)`. `Path.symlink_to` itself calls `os.symlink(target, self, target_is_directory)`, so the relative target `held` is written as given both before and after, and the link still names a sibling of `trail/rounds`. The helper's parent assertion at `tests/conftest.py:638-639` reads `trail/`, which `item(root)` made and which `held.mkdir()` at `:258` needs too. `directory=True` keeps the directory link Windows needs for a directory target. Read.

What matched: the widened import at `tests/github/test_finding_counts.py:14-21` adds `symlink_or_skip` beside the five names it took. `tests/github/` has no `conftest.py` of its own, so the name resolves to `tests/conftest.py:620`. Read.

What matched: the crafter claimed `bin/test tests/github/test_finding_counts.py -q -rs` exits 0 with 18 passed and no skip, and that both parameters of the case print `PASSED` run verbose. This round's runs in the clone at `8a038181` exited 0 with `18 passed`, and the `-k` run printed `[a file] PASSED` and `[a link to a directory of records] PASSED`. Executed.

What matched: the crafter's `seal mutate` claim, that a raised `OSError` in place of `os.symlink` read `2 passed` at `6444e3cc` and skipped the link parameter at `tests/conftest.py:643` at `ad9943fd`, was not re-run. Reading settles what it shows: at `6444e3cc` the link parameter called `Path.symlink_to` and so could not reach a broken helper, and at `ad9943fd` it calls the helper, whose `pytest.skip` stands at `tests/conftest.py:643`. The `[a file]` parameter makes no link on either tree. Read.

What matched: the class is whole for the tests tree at `8a038181`. `git grep -n 'symlink_to(\|os\.symlink(' -- tests` lists `tests/conftest.py:621` and `:641` alone, the helper's docstring and its call. The second search the phase record names (`ln -s`, `mklink`, `CreateJunction`, `hardlink_to`, `os.link(`) matches nothing under `tests/`. So the phase record's sentence that HEAD lists nothing outside `tests/conftest.py` holds at the target. The class was built from what makes a link in Python, the first of contract rule 12's methods, so it is a list and not a sample. Executed.

What matched: `gaps.md` *Scope confirmation* says no other file of the suite changes. `git diff --stat 063e0678..8a038181` lists `tests/skills/test_agentic_pytest_record.py` and `tests/github/test_finding_counts.py` as the two files under `tests/`. Executed.

What matched: what the diff changes in `gaps.md`. The first `## Not verified` row is rewritten in place to open with `closed`, and its second cell names run 42134062891 and what it showed, which round 1's first confirmation established. The second row is reworded in place to two test files. The third row is new and open, and names its answerer. No row of `## Not verified` left. `## Not done` now reads `nothing`: its one memo was the fourth case left out of scope, and that case is now built, so nothing within reach stands deliberately not taken. The decision and its grounds stand in `trail/phases/phase-1.md` *After round 1, the scope widened to the fourth case*. Read.

What matched: the fragment's added sentence names `Test_main::test_rounds_that_cannot_be_listed_read_not_read_in_every_cell`, which is the case's class and name at `tests/github/test_finding_counts.py:121` and `:241`, and its bold line says the case would fail on a Windows machine without the link privilege, which is the direction `tests/conftest.py:627-630` names for a bare link call. `routing.md`'s grounds now say four link cases, which matches the scope line. Read.

What matched: the commits `ad9943fd`, `cc851ef3` and `8a038181` are authored by the address the repository's commit identity names. Executed: `git log --format='%h %ae' 6444e3cc..8a038181`.

What matched: the fourth case ran and passed on the `windows-latest` legs at `8a038181`. The orchestrator's `tests` run 42135588653 at that commit completed every `pytest` job and `lint` with `success`, the four Windows legs among them. The legs run pytest with `-rfEs --no-fold-skipped` (`.github/workflows/test.yml:167`), so each skip prints its own line. A grep of the four Windows job logs for `test_finding_counts`, `symbolic links are not available` and `conftest.py:643` matched no line; the legs printed 35 `SKIPPED` lines between them, none naming the module. The run's `test-durations-5` artifact, uploaded only by a Windows leg (`.github/workflows/test.yml:108-111` set `store` on the Windows rows alone, and `:176-179` upload only where it is set), prices `[a file]` at 0.72 seconds and `[a link to a directory of records]` at 0.80 seconds. A skip costs under a thousandth of a second, so the link parameter made its link through the helper and passed. Executed: `gh run view 42135588653`, `gh run view --job` for the four Windows jobs, `gh run download 42135588653`.

No test is added: the diff moves an existing case onto an existing helper, so no case is owed a red and none is read against its group.

## Not judged

| What | Location | Who answers |
|---|---|---|
| `gaps.md` `## Not verified` row 3 asks whether the fourth case passes on the `windows-latest` legs at `ad9943fd`, and run 42135588653 at `8a038181` answers it as the last confirmation above states. Marking the row `closed` is a write to the closing memo, which this round does not make | `seal/threads/1793922919-three-link-cases-skip-on-windows-by-platform/gaps.md` | the orchestrator |
| The full suite, the repository-wide lint and the typecheck at HEAD. The crafter's label `unverified` is honest: the phase ran two modules, on macOS | the repository | the orchestrator, at the broad gate |

Nothing stays open from this round. What comes due is the orchestrator's broad run, then the sealer's spawn.

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_finding_counts.py -q -rs` | exit 0, `18 passed` |
| `bin/test tests/github/test_finding_counts.py -v -rs -p no:xdist -k test_rounds_that_cannot_be_listed_read_not_read_in_every_cell` | exit 0, `2 passed, 16 deselected`, both parameters `PASSED` |
| `git grep -n 'symlink_to(\|os\.symlink(' -- tests` at `8a038181` | `tests/conftest.py:621` and `:641` alone |
| `git grep -n 'ln -s\|mklink\|CreateJunction\|hardlink_to\|os\.link(' -- tests` at `8a038181` | no line |
| `gh run view 42135588653 --json status,conclusion,jobs`, read again once the Windows legs ended | `lint` and every `pytest` job `completed success`; `release-report` skipped; `durations` queued |
| `gh run view --job <id> --log`, for the four `windows-latest` jobs, grepped for `test_finding_counts`, the helper's skip reason and `conftest.py:643` | no line matched; the legs ended `3066 passed, 18 skipped`, `1099 passed, 17 skipped`, `1502 passed`, `521 passed` |
| `gh run download 42135588653`, grepped for the case name | `test-durations-5` prices `[a file]` at 0.72 and `[a link to a directory of records]` at 0.80 seconds |
