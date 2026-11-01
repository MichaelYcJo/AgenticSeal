# Closing memo: 1793521561-a-windows-run-names-its-skipped-cases

## Not verified

| Item | Who must answer |
|---|---|
| Whether every `pytest` leg's short summary prints one `SKIPPED <node id> - Skipped: <reason>` line per skipped case and keeps its `FAILED` lines on the runners, and whether the pytest the legs install takes `--no-fold-skipped` (S1). The local pytest 9.2.0 lists the option, and no CI leg has run the line yet | a measurement: the dispatched `tests` run on phase 1's commit, read in phase 2 |
| The full suite, the repository-wide `ruff check` and `ruff format --check` on this branch, among them the shard module's two cases that skip unless the whole suite is collected | the orchestrator, through `seal gate` |

## Not done

The list under *Out* in `frame/design.md` *Scope* gives each item left there and its grounds. The `arms-grammar` job's pytest line in `.github/workflows/test.yml` is not given the flags. It runs one module on ubuntu, and no row defers a question to it (`trail/phases/phase-1.md`).
