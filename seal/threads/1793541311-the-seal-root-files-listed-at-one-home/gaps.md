# Closing memo: 1793541311-the-seal-root-files-listed-at-one-home

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the format check at the branch's head. Phase 1 ran 87 modules chosen by `git grep` (`trail/phases/phase-1.md` *The phase-boundary run*) | answered: `trail/gate.md`, the `Broad gate` row passed at `b6ef9288` against `361ed0cb`, and `guarantee.md` sealed on it |
| closed S3 and S4 of `frame/design.md`: once 0.27.3 is released, the settle writes the *seal/* table with six entries and names `docs/the-record-layout.md` alone for the layout in `docs/one-root-by-lifetime.md` and its Korean edition. P3 at `f15fcb33` found each `from` in its section (`trail/phases/phase-1.md` *How the phase is proved*), and no settle has run | answered: this settle (`chore/settle-0.28-0.29`) wrote groups 3 to 5 of its dry run: the *seal/* table of `docs/the-record-layout.md` and both editions of `docs/one-root-by-lifetime.md` naming it alone for the layout |
| closed S5 of `frame/design.md`: `chain-check` reads the three `change` items at the pull request and refuses nothing. P3 parsed them at `f15fcb33` with no error and no unread line | answered: this settle (`chore/settle-0.28-0.29`)'s dry run read the three `change` items through `rule_changes.py`, placed them in groups 3 to 5, and listed no line of the design as not read |

## Not done

The `### Process changes` row that `docs/the-record-layout.md` *A change writes fragments, never a shared file* asks for, because the diff changes `skills/verify/orchestration.md`. The same section names the orchestrator as its writer, so this phase left the row to the orchestrator (`trail/phases/phase-1.md` *Owed by another party*), and the orchestrator wrote it before round 1.
