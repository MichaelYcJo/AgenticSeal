# Closing memo: 1794200906-settings-are-read-as-json

## Not verified

| Item | Who must answer |
|---|---|
| closed The whole suite, the repository-wide lint and the format check over the branch at its last commit: no phase runs them | answered by the work item's broad gate, `trail/gate.md` run bed47599d against 961fe52b1, on which `guarantee.md` sealed, and by run 42715396288 of the 0.37.0 release pull request #1467, whose lint job and eleven pytest jobs on ubuntu, macOS and Windows passed |

## Not done

`.test_durations` still lists the test names phases 1 to 5 removed or renamed. Phase 4's walker cases stand there under `tests/lib/test_config.py`, and the case renamed to `test_the_table_walker_never_leaves_both_readings` under its old name. `.github/scripts/durations_union.py` says a work item never commits that file.

`docs/` is the settle's to write, and design *Rule changes* holds what it rewrites. Until the settle, `docs/layout/the-pact.md:21` names the 0.18.x `| Signatory |` header, `:88` names `lib/config.py#gfm_table`, and `:147` names the `| Remote | Path |` table of `pact-paths.md`. `docs/checks/the-fold.md:117` names `lib/config.py#hidden_lines`, and `:122` names `lib/config.py#config_table`, which phase 1 removed. *Rule changes* removes the paragraphs holding `the-pact.md:21` and `the-fold.md:117` and `:122`, and rewrites `the-pact.md:88` and `:147`. When the fold paragraph leaves, the `tables.py#hidden_lines` row of `tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py#TABLE` spells a name the statement no longer holds, and its case must change in the same commit.

`seal settle --draft` does not place the operation at `seal/threads/1794188289-the-body-reads-in-the-teams-language/frame/design.md:226`, because 1794187229's operation rewrites the `seal pr-body --check` row of `docs/running/what-a-script-gates.md` *The checks* before it. Its `to:` names `config.md`'s two language rows. The settling session that places it by hand writes `config.json`'s two language keys and calls each a key.

A bare "row" meaning the `Broad gate` command stands in the parameter names and some docstrings of `tests/skills/test_broad_gate.py`, such as its `row` arguments and the section comment `# --- the row ---`. Identifiers that spell "row" stand too: `broad_gate.py#missing_row` and `#ROW_NOT_RUN`, and test constants such as `BROAD_ROW` and `LANGUAGE_ROWS`, and the file names `test_the_broad_gate_row_is_asked_for_and_runs_as_written.py` and `test_the_mode_is_a_row_and_a_command.py`. Phase 5 rewrote the text a reader acts on and left identifiers, because renaming them changes every caller and no reader acts on the spelling. `trail/phases/phase-5.md` says which reading reached which file.
