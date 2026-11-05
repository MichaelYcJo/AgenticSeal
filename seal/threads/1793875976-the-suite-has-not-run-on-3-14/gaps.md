# Closing memo: 1793875976-the-suite-has-not-run-on-3-14

## Not verified

| Item | Who must answer |
|---|---|
| Whether the whole suite passes on Python 3.14: phase 1 ran nothing on 3.14, and no case requires the 3.14 entry to exist | the dispatched `tests` run of phase 3, read by the crafter the orchestrator spawns for that phase |

## Not done

The floor case in `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py` reads each operating system's floor entries, and not whether those entries cover every shard. A macOS or Windows shard moved off the floor leaves the system with other floor entries, so the case passes it. A mutation measured this at `315358a8`. A reading per shard would require each system's floor entries to cover every group of its split. It was not built, because Scope 2 asks for one floor entry per system, and `plan.md` alternative F keeps 3.14 off the sharded systems. The case's docstring states the limit.
