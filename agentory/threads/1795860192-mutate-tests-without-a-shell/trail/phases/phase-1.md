# Phase 1: 1795860192-mutate-tests-without-a-shell

## What this phase found

- `seen red` (executed): the new `Test_main` case and the eleven `shell_operators` cases failed against `aec6390b`. The `Test_main` case printed `SURVIVED` for `--tests "true && false"`, which is the defect itself: `true` ran with `&&` and `false` as its arguments and passed.
- `agentic mutate` over `mutation_check.py` with five pairs (executed): dropping the POSIX backslash rule, either quote's close, the final run's append, and the refusal in `main` each read `red`, 5 of 5.
- The refusal goes through `parser.error`, as the refusal of a `--tests` that names nothing does, so it exits 2 with the usage line before anything is written.
