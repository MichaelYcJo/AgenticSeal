# Closing memo: 1794200906-settings-are-read-as-json

## Not verified

| Item | Who must answer |
|---|---|
| The whole suite, the repository-wide lint and the format check over the branch at its last commit: no phase runs them | the orchestrator, through `seal gate` |

## Not done

`.test_durations` still lists the test names phases 1 to 5 removed or renamed. Phase 4's walker cases stand there under `tests/lib/test_config.py`, and the case renamed to `test_the_table_walker_never_leaves_both_readings` under its old name. `.github/scripts/durations_union.py` says a work item never commits that file.

`docs/` is the settle's to write, and design *Rule changes* holds what it rewrites. Until the settle, `docs/layout/the-pact.md:21` names the 0.18.x `| Signatory |` header, `:88` names `lib/config.py#gfm_table`, and `:147` names the `| Remote | Path |` table of `pact-paths.md`. `docs/checks/the-fold.md:117` names `lib/config.py#hidden_lines`, and `:122` names `lib/config.py#config_table`, which phase 1 removed. *Rule changes* removes the paragraphs holding `the-pact.md:21` and `the-fold.md:117` and `:122`, and rewrites `the-pact.md:88` and `:147`. When the fold paragraph leaves, the `tables.py#hidden_lines` row of `tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py#TABLE` spells a name the statement no longer holds, and its case must change in the same commit.

`docs/running/the-broad-gate.md` calls the `Broad gate` command "the row" at `:41` ("whatever the row's exit"), `:44` ("can change the row's exit"), `:45` ("an exit of 0 from the row"), `:57` ("Where the row exited 0") and `:63` ("row's exit into 0"). Design *Rule changes* rewrites two other paragraphs of that file and none of these five lines, and design *Scope* item 7's `git grep` set does not reach a bare "the row". Phase 5 does not write `docs/`, so its hand-back names the five lines for the orchestrator to fold into *Rule changes*.

A bare "row" meaning the `Broad gate` command stands in the parameter names and some docstrings of `tests/skills/test_broad_gate.py`, such as its `row` arguments and the section comment `# --- the row ---`. Identifiers that spell "row" stand too: `broad_gate.py#missing_row` and `#ROW_NOT_RUN`, and test constants such as `BROAD_ROW` and `LANGUAGE_ROWS`, and the file names `test_the_broad_gate_row_is_asked_for_and_runs_as_written.py` and `test_the_mode_is_a_row_and_a_command.py`. Phase 5 rewrote the text a reader acts on and left identifiers, because renaming them changes every caller and no reader acts on the spelling. `trail/phases/phase-5.md` says which reading reached which file.
