# Implementation Plan: 1794142458-config-dir-readers

## Technical context

The tree as read at `b2a04d6d9`.

Two scripts and three prose lines name Claude Code's directory as a fixed `~/.claude` (`frame/design.md` G1, G2). `session_cost.py` fixes the projects root at import (`:82-83`), and `newest` (`:2879-2893`) is its one reader. `payload_meter.py` threads one `home` through `measure` (`:761`), `session_composition` (`:506`), `composition` (`:451`), `pair_rows` (`:471`) and `imports_of` (`:369`). It uses that `home` for two different things: the user's config directory (`:461`, `:480`) and the target of a `@~/` import (`:439-440`). Claude Code moves the first with `CLAUDE_CONFIG_DIR` and not the second (G6), so the build splits them. The meter's in-process cases pass `home` explicitly (G8), and the meter promises that it never reads the process's home on its own. The build keeps that promise for the config directory: only `main` reads the variable.

The tree has no Python reader of the variable since `core_check.py` left in #1376 (G3), so this work writes the expression again in each of the two scripts. The shell spelling stands in `skills/update/SKILL.md`.

**What breaks in six months.** Claude Code changes how it resolves its directory, for example by honouring a second variable or by reading an empty value differently (G4 shows it already treats an empty or relative value in its own way). The two Python expressions and the shell spelling then each need the change. `git grep -n CLAUDE_CONFIG_DIR -- skills` lists every one of them, because each spells the variable's name, and nothing else in the tree reads the directory. A reader added later that builds the path from `expanduser` alone is the same defect again. No check refuses it (row 5 below), and the review catches it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. Each script resolves the directory with the expression `core_check.py` used. `session_cost.py` reads it at each call; `payload_meter.py` takes it as an input beside `home`, read once in `main`, and labels a file under a set variable `$CLAUDE_CONFIG_DIR/…` | The expression stands twice, so a change to Claude Code's resolution has two Python places to change; both are found by the variable's name (*Technical context*) | **Chosen** |
| 2. One function in a new `lib/` module that both scripts load by path | `session_cost.py` loads nothing from `lib/` today. It would gain a load that exits 2 where the script was copied without the plugin, for a one-line expression whose every copy the variable's name already finds. `payload_meter.py` already depends on `lib/core.py`, but the second script would carry the cost | Rejected: a new failure mode in one script, to save one line |
| 3. Keep `PROJECTS` a module constant, computed from the variable at import (keeps the structure) | The premise that keeps it is that nothing needs to move the root after import. Checked: `newest` is its one reader (G1), and the only seam the cases have is `monkeypatch.setattr(module, "PROJECTS", …)` (G8). A constant fixed at import cannot be moved by `monkeypatch.setenv`, so a case of the variable has to reload the module or patch the constant, and the second is not a case of the variable at all | Rejected: the premise fails for the case the issue asks for |
| 4. `payload_meter.py` reads the variable inside `pair_rows` and `composition` | Every in-process call reads the developer's environment, so the in-process calls G8 counts measure a different file on a machine that sets the variable. This also breaks the module's promise that it reads the home it was given, never the process's (`:385`) | Rejected |
| 5. A text case that refuses a fixed `~/.claude` in every shipped file | It needs an exception for `~/.claude/agentic/`, for the dated experiment record and for history, and a list of spellings for a fixed path. `skills/core/SKILL.md` *The rule a mechanism is kept against* refuses such a list. The instances found so far, in #1184 and #1367, were each found by one search, and the two searches of G2 find the class again | Rejected: the review and the G2 searches cover it, and the searches are named in *Phases* |
| 6. Label a file under a set variable by its absolute path | The label carries the account name into every record that quotes the table, which `tests/test_censuses.py#real_identifiers` refuses (G7) | Rejected |
| 7. Keep the label `~/.claude/…` whatever the variable says | The row names a file the meter did not read, which is this issue's defect moved from the read to the label | Rejected |
| 8. Replace `home` with the config directory as the meter's one root (replaces the structure) | The premise that keeps `home` is that a `@~/` import resolves against the home directory. Checked: `imports_of` (`:369-400`) follows code.claude.com/docs/en/memory.md, where `~` is the home directory (G6). With the config directory in its place, a set variable sends every `@~/` import to `<config>/…`, which is wrong | Rejected: the premise holds, so `home` stays and the config directory joins it |
| 9. Drop the variable in `test_payload_meter.py#run` alone, in place of `conftest.py` | `Test_newest` calls `newest` in process, so a helper for children does not reach it. A module added later that runs either script inherits the developer's variable again. `conftest.py` already moves `GH_CONFIG_DIR` for every case and child (G9) | Rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 3 and 4, and item 5 for `session_cost.py` | S1 and S2, each case seen red as its row says; S7's search for the coordinates of items 1 and 3; S8 for `tests/skills/test_session_cost.py`; a narrow run of `tests/skills/test_session_cost.py` | c4deded6 |
| 2 | `frame/design.md` *Scope* item 2, item 5 for `payload_meter.py`, the changelog fragment `changelog.md`, and the version move *Operational impact* names | S3 to S6, each case seen red as its row says; S7's search for item 2's coordinates; S8 for `tests/skills/test_payload_meter.py`; a narrow run of `tests/skills/test_payload_meter.py` | e6652dac |

## Operational impact

- **The version moves to `0.35.1`.** This is the first pull request into `release/v0.35.1`, whose `.claude-plugin/plugin.json` reads `0.35.0` (G12), and the orchestrator chose this work item to carry the move. Phase 2's crafter sets `"version": "0.35.1"` in `.claude-plugin/plugin.json` in the same commit that adds `seal/threads/1794142458-config-dir-readers/changelog.md` (`docs/releasing/branch-and-release.md` *The version moves at the start of a release*).
- **No new dependency.** The scripts read `CLAUDE_CONFIG_DIR`, which Claude Code defines; the plugin adds no variable of its own.
- **Compatibility.** `session_cost.HOME` and `session_cost.PROJECTS` leave. No file of the tree outside the script and its test module names either (G1). On a machine that sets the variable, a `seal payload` row moves from `~/.claude/CLAUDE.md` to `$CLAUDE_CONFIG_DIR/CLAUDE.md`. A `--baseline` taken there before the fix does not pair that row (G7), and those readings measured the wrong file anyway. Under an unset variable nothing a person sees changes.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-08 | *Scope* item 4 and S8 take the case phase 1 added, `tests/test_conftest.py#Test_module::test_the_conftest_takes_the_claude_config_directory_away`, and the frame is folded to it | The phase-1 crafter's hand-back: a `seal mutate` that turned the `conftest.py` removal into `pass` survived S8's run (executed by the crafter), so S8 alone could not fail on the unit it verifies; the crafter added the case under its mutation rule | `agents/crafter.md` *Mutation-test every unit that adds behaviour*; `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
