# Closing memo: 1795390621-the-broad-gate-rewrites-cmd-exe-commands

## Not verified

| Item | Who must answer |
|---|---|
| The `cmd.exe` half of `Test_run`'s two real-platform cases: `bin/probe` refused naming `bin\probe`, `bin\probe` run under `cmd`, and `where/q cmd` not refused and exiting 0. The shell where phase 1 was built is `/bin/sh`, so neither half ran here | CI's `windows-latest` leg, read by the orchestrator at the pull request |
| Whether `cmd.exe` runs a command name that opens with a drive and `/`, such as `C:/Python/python.exe`, as written. The gate refuses it on Windows, because `os.path.join(root, "C:")` names a directory (`trail/phases/phase-1.md`) | a measurement: one run of such a name under `cmd.exe` on a Windows machine |
| What `templates/setup/config.md` *Broad gate* says `cmd.exe` does where the reading and `cmd.exe` differ: that `rem` ignores the `&& bin/test` after it, and that a separator glued to a word, as in `a&& bin/x` or `a &&bin/x`, still separates two commands. Phase 2 states both as `design.md` *Scope* item 6 and `plan.md` *Judgments of the run* state them, and no Windows shell was in reach to run either | a measurement: one run of each value under `cmd.exe` on a Windows machine |
| Whether this repository's key, `uvx ruff check . && uvx ruff format --check . && uv run --no-project tests/run_tests.py -q`, runs the suite under `cmd.exe` on Windows, with `PYTHONPATH` and `PYTEST_ADDOPTS` kept as the gate sets them. Phase 3 ran `uv run --no-project tests/run_tests.py` over one module on macOS only (`trail/phases/phase-3.md`). This is `frame/questions.md` M1 | a measurement: one `seal gate` run on a Windows machine |

## Not done

Nothing. Phase 1 left this repository's own key naming `bin/test -q`, which `test_this_repositorys_own_config_is_answered_exactly_as_before` refused on the Windows shards, because the new spelling names `tests/run_tests.py` and that path stood only once #1571 had merged. Phase 3 changed the key at `96ec27a50`, after the merge of the base at `f4eddf52c`.
