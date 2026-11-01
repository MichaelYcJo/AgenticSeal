# Closing memo: 1793521562-the-proofer-cases-come-from-thread-records

## Not verified

| Item | Who must answer |
|---|---|
| closed Whether the proofer, on the current release, reads a new case's earlier round records and writes its own record at the path the case's prompt names (`frame/questions.md` Q1, `frame/design.md` Scenario 7). Only a paid run shows it, and the owner withheld every paid eval run in 0.27.2 (`frame/plan.md` *Judgments of the run*, the first row) | re-homed to #1266, a paid run the owner withheld in 0.27.2 |
| closed The full suite, the repository-wide lint and the format check at the work item's head. Phase 1 ran its phase-boundary set in one command and ran `ruff check` and `ruff format --check` on its four changed Python files alone (contract rule 2; `trail/phases/phase-1.md`, *Scenario 5 and contract rule 2*) | answered by `trail/gate.md`: the broad gate row of `seal/config.md`, the full suite with the repository-wide `ruff check` and `ruff format --check`, passed at `25eebe60 against ad5246ce` (read by the settle that opens 0.27.3) |

## Not done

The replacement cases are what `--count 4` writes with each generator, `frame/questions.md` Q2's default (a). Its options (b), rounds chosen by hand for more truths, and (c), a larger `--count`, were within reach and not taken. Q2 is the owner's choice, and the orchestrator recorded the build on (a) in `frame/plan.md` *Judgments of the run*, the second row. Either option is one `--case` or `--count` run and the removal of the cases it replaces.
