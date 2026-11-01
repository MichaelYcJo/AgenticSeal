# Closing memo: 1793457436-row-deletion-check-and-a-symlink

## Not verified

| Item | Who must answer |
|---|---|
| closed `frame/questions.md` Q1: whether the link cases of `tests/skills/test_unverified_check.py` run on the Windows legs or skip there through `symlink_or_skip`. They ran on macOS here and skipped none | answered by run 41290162769, the Windows run #1221 dispatched (`1793521561-a-windows-run-names-its-skipped-cases/trail/phases/phase-2.md`), and run 41308322472 at `5f0cf7a7`: the four `windows-latest` legs list no `SKIPPED` case of `tests/skills/test_unverified_check.py`, so its link cases ran there through `symlink_or_skip`, and every leg passed |
| closed A tracked link whose target stands on another Windows drive, run end to end. The `another volume` case makes `os.path.relpath` raise to reach the branch, so what Windows `os.path.realpath` answers for such a link was not run | re-homed to #1264, a measurement no record holds |
| closed The full suite, the repository-wide `ruff check` and `ruff format --check` on this branch | answered by `trail/gate.md`: the broad gate row of `seal/config.md`, the full suite with the repository-wide `ruff check` and `ruff format --check`, passed at `4000a24f against a92c358b` (read by the settle that opens 0.27.3) |

## Not done

The list under *Out* in `frame/design.md` *Scope* gives each item left there and its grounds. Round 1's fix pass left one more.

A link named as the argument itself, such as `seal unverified --baseline <ref> specs/a/gaps.md` where `specs/a/gaps.md` was a file at the base and is a link now, still passes the rows it lost with exit 0. `#overviews` resolves each argument once with `real()`, so the scan holds only the target's path and the link's own path never reaches the comparison. The presence arm builds its prefixes from the same resolved argument. A probe on this branch after the fix showed exit 0 for this case. The same probe exited 1 for the class round 1 named, with the link reached by scanning its directory. The behaviour predates this work: a92c358b resolved the argument the same way. Closing it means resolving only the argument's directory, in `#overviews` and in the presence arm's prefixes together, or the presence arm reports the target as deleted. That changes the argument resolution the frame leaves alone (`frame/design.md` *Grounding*, the row on `#overviews` and `#main`). It goes to the orchestrator as a candidate row for `seal/follow-up.md`.
