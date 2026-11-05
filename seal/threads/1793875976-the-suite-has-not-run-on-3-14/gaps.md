# Closing memo: 1793875976-the-suite-has-not-run-on-3-14

## Not verified

| Item | Who must answer |
|---|---|
| Whether the whole suite passes on Python 3.14: phase 1 ran nothing on 3.14, and no case requires the 3.14 entry to exist | the dispatched `tests` run of phase 3, read by the crafter the orchestrator spawns for that phase |
| The release table's `` `ubuntu 3.14` leg (minutes) `` row over a real run's job list: phase 2's cases read job lists written by hand, and the `release-report` job runs only on a pull request into `main` | the 0.32.5 release pull request's `release-report` summary, read by whoever prepares the release (`docs/releasing/release-checklist.md` *5. The release pull request*) |

## Not done

The floor case in `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py` reads each operating system's floor entries, and not whether those entries cover every shard. A macOS or Windows shard moved off the floor leaves the system with other floor entries, so the case passes it. A mutation measured this at `315358a8`. A reading per shard would require each system's floor entries to cover every group of its split. It was not built, because Scope 2 asks for one floor entry per system, and `plan.md` alternative F keeps 3.14 off the sharded systems. The case's docstring states the limit.

The release table reads both job lists against one floor, this tree's `hooks/lib/launch.py#FLOOR`. On a release that moves the floor, the tag's jobs at the old floor print as `<os> <old floor>` rows, and the three rows read `no run found` at the tag. A floor read from each tree, the tag's from `--at`, would keep the three rows comparable across that release. It was not built, because Scope 4 names one floor and no release in this work moves it.
