# Closing memo: 1794200906-settings-are-read-as-json

## Not verified

| Item | Who must answer |
|---|---|
| The whole suite, the repository-wide lint and the format check over the branch at its last commit: no phase runs them | the orchestrator, through `seal gate` |

## Not done

Phase 1 leaves to phases 2 to 5 what `frame/plan.md` gives them: `parity.json` (2), `Pact signers` and `pact-paths.json` (3), the walker's move to `lib/tables.py` (4), and the shipped text (5). Phase 1 regenerated the eval scaffolds, which phase 5's row also names (`trail/phases/phase-1.md` says why). Until phase 5, the cases that read `templates/setup/config.md`, `skills/config/SKILL.md` and `skills/commit-pr-convention/SKILL.md` still pin those documents' table wording, and `trail/phases/phase-1.md` names them.

Phase 2 left two sentences of `templates/setup/config.md` that name `parity.md` as a table beside the config: line 4, "beside `parity.md`, in the same shape: a markdown table", and line 173, "the same rule `parity.md` already follows". Both state `config.md`'s own table shape too, which phase 5 rewrites with the whole document, so rewriting half of each now would leave a sentence phase 5 rewrites again. `.test_durations` still lists the test names this phase removed or renamed; `.github/scripts/durations_union.py` says a work item never commits that file.

`skills/verify/scripts/broad_gate.py` still calls the `Broad gate` value "the row" in about forty comments and docstrings, such as "The row runs with a pytest recorder" in its module docstring. Phase 1 reworded only the lines it changed. Design *Scope* item 7's `git grep` set lists `Broad gate row` but not a bare "the row", so phase 5 reaches these lines only if it reads the file.

Phase 3 left two texts calling a setting a row, beside the `Pact signers` key it added to each. `skills/config/SKILL.md` keeps its `Row` column and "is only a row too". `templates/setup/config.md` *Pact* keeps its `Pact notify` paragraph, which `tests/behaviour/test_a_signer_declares_its_pact.py` pins verbatim. Phase 5 rewrites both documents whole (design *Scope* item 7), so rewording them here would be rewritten again. `skills/verify/scripts/pact_check.py#shown`'s docstring still names `seal/config.md` as an example of a path it shows, which design *Scope* item 7's `git grep` set reaches. `docs/layout/the-pact.md:21` still names the 0.18.x `| Signatory |` header, and `:147` the `| Remote | Path |` table of `pact-paths.md`. Design *Rule changes* removes the paragraph holding `:21` and rewrites `:147`, both at the settle. `.test_durations` also lists the cases phase 3 removed, for the reason given above.

Phase 4 left two lines of `docs/` naming the walker in `lib/config.py`. `docs/checks/the-fold.md:117` names `lib/config.py#hidden_lines`, and `:122` names `lib/config.py#config_table`, which phase 1 removed. `docs/layout/the-pact.md:88` names `lib/config.py#gfm_table`. The settle writes `docs/`. Design *Rule changes* removes the paragraph holding `the-fold.md:117` and `:122`, and rewrites `the-pact.md:88` to `lib/tables.py#gfm_table`. When that paragraph leaves, the `tables.py#hidden_lines` row of `tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py#TABLE` spells a name the statement no longer holds, and its case must change in the same commit. `.test_durations` lists the walker's cases under `tests/lib/test_config.py` and the case renamed to `test_the_table_walker_never_leaves_both_readings` under its old name, for the reason given above.
