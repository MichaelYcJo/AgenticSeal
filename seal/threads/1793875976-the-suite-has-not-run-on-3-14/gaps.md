# Closing memo: 1793875976-the-suite-has-not-run-on-3-14

## Not verified

| Item | Who must answer |
|---|---|
| closed whether the whole suite passes on Python 3.14: phase 1 ran nothing on 3.14, and no case requires the 3.14 entry to exist | run 42019408766 at `b1669859`: its `pytest (ubuntu-latest, 3.14, 15)` job concluded `success`, 6208 passed and 10 skipped, read by the crafter of phase 3 (`trail/phases/phase-3.md`) |
| closed The 3.14 job at `af153874` and later: run 42019408766 measured `b1669859`, and `af153874` changes `test.yml` only in a comment | answered: #1397's `tests` run 42024868242 ran `pytest (ubuntu-latest, 3.14)` at `40fc3d61`, after `af153874`, and it passed; so did #1398's run 42116087219 at `c475b894` |
| closed The release table's `` `ubuntu 3.14` leg (minutes) `` row over a real run's job list: phase 2's cases read job lists written by hand, and the `release-report` job runs only on a pull request into `main` | answered: #1398's body reads the release table's `ubuntu 3.14` row at 1.9 minutes, from run 42116087219's job list |

## Not done

The floor case in `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py` reads each operating system's floor entries, and not whether those entries cover every shard. A macOS or Windows shard moved off the floor leaves the system with other floor entries, so the case passes it. A mutation measured this at `315358a8`. A reading per shard would require each system's floor entries to cover every group of its split. It was not built, because Scope 2 asks for one floor entry per system, and `plan.md` alternative F keeps 3.14 off the sharded systems. The case's docstring states the limit.

The release table reads both job lists against one floor, this tree's `hooks/lib/launch.py#FLOOR`. On a release that moves the floor, the tag's jobs at the old floor print as `<os> <old floor>` rows, and the three rows read `no run found` at the tag. A floor read from each tree, the tag's from `--at`, would keep the three rows comparable across that release. It was not built, because Scope 4 names one floor and no release in this work moves it.

`tests/skills/test_mutation_check.py::Test_main::test_a_mutant_is_compiled_without_the_scripts_own_future_flags` is skipped on the 3.14 job, because its probe line compiles the same on 3.14 with `from __future__ import annotations` and without it. A probe line that the flag still changes on 3.14 would let the case run there. Six annotation forms were tried, and none differs on 3.14.4 (`trail/phases/phase-3.md`). The search went no further, because the eight floor jobs run the case and hold the guard, and on 3.14 the six forms show the flag changes nothing the compile accepts.
