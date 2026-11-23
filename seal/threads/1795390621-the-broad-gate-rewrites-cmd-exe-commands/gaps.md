# Closing memo: 1795390621-the-broad-gate-rewrites-cmd-exe-commands

## Not verified

| Item | Who must answer |
|---|---|
| The `cmd.exe` half of `Test_run`'s two real-platform cases: `bin/probe` refused naming `bin\probe`, `bin\probe` run under `cmd`, and `where/q cmd` not refused and exiting 0. The shell where phase 1 was built is `/bin/sh`, so neither half ran here | CI's `windows-latest` leg, read by the orchestrator at the pull request |
| Whether `cmd.exe` runs a command name that opens with a drive and `/`, such as `C:/Python/python.exe`, as written. The gate refuses it on Windows, because `os.path.join(root, "C:")` names a directory (`trail/phases/phase-1.md`) | a measurement: one run of such a name under `cmd.exe` on a Windows machine |

## Not done

Phase 1 leaves this repository's own key, `uvx ruff check . && uvx ruff format --check . && bin/test -q`, as it is. On the Windows shards, `test_this_repositorys_own_config_is_answered_exactly_as_before` now refuses it, because the case passes `ROOT` and `ROOT` holds `bin/`. The new spelling names `tests/run_tests.py`, which exists only once #1571 has merged, so `plan.md` *Phases* gives the key to phase 3. No CI leg runs before the pull request, and phase 3 is built before it opens.
