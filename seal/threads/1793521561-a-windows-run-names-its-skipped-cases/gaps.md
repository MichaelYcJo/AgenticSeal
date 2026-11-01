# Closing memo: 1793521561-a-windows-run-names-its-skipped-cases

## Not verified

| Item | Who must answer |
|---|---|
| closed whether every `pytest` leg's short summary prints one `SKIPPED <node id> - Skipped: <reason>` line per skipped case and keeps its `FAILED` lines on the runners, and whether the pytest the legs install takes `--no-fold-skipped` (S1). The local pytest 9.2.0 lists the option, and no CI leg has run the line yet | run 41290162769 at 585234f6, read in phase 2 (`trail/phases/phase-2.md`): every leg of the `pytest` job installed pytest 9.2.0, ran the line with both flags and concluded `success`, and each of those legs that skipped printed one `SKIPPED` line per skipped case. It answered the `SKIPPED` half and the option. No case failed on any leg, so the `FAILED` half is the next row |
| Whether a red `pytest` leg on the runners keeps one `FAILED <node id> - <message>` line per failed case under `-rfEs`. Run 41290162769 had no failed case on any leg. The framer's probe showed the line on macOS at pytest 9.2.0, pytest-xdist 3.8.0 and pytest-split 0.11.0, the versions every leg of that run's `pytest` job installed | a measurement: the first `pytest` leg that goes red, read by the orchestrator through `gh run view --job <id> --log` |
| The full suite, the repository-wide `ruff check` and `ruff format --check` on this branch, among them the shard module's two cases that skip unless the whole suite is collected | the orchestrator, through `seal gate` |

## Not done

The list under *Out* in `frame/design.md` *Scope* gives each item left there and its grounds. The `arms-grammar` job's pytest line in `.github/workflows/test.yml` is not given the flags. It runs one module on ubuntu, and no row defers a question to it (`trail/phases/phase-1.md`).

The three link cases of `tests/skills/test_agentic_pytest_record.py` that skip on the Windows legs through `skipif(os.name == "nt")` are not moved onto `tests/conftest.py#symlink_or_skip`. Run 41290162769 shows the runner can make links, so they go unproved there for a reason that does not hold. `frame/design.md` *Scope*, *Out* keeps every case under `tests/` out of this work. The orchestrator filed them as #1247 in `backlog: release & platform` (`frame/plan.md` *Judgments of the run*), from the draft in `trail/phases/phase-2.md`.
