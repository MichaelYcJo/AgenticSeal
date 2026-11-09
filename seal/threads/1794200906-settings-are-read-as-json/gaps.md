# Closing memo: 1794200906-settings-are-read-as-json

## Not verified

| Item | Who must answer |
|---|---|
| The whole suite, the repository-wide lint and the format check over the branch at its last commit: no phase runs them | the orchestrator, through `seal gate` |

## Not done

Phase 1 leaves to phases 2 to 5 what `frame/plan.md` gives them: `parity.json` (2), `Pact signers` and `pact-paths.json` (3), the walker's move to `lib/tables.py` (4), and the shipped text (5). Phase 1 regenerated the eval scaffolds, which phase 5's row also names (`trail/phases/phase-1.md` says why). Until phase 5, the cases that read `templates/setup/config.md`, `skills/config/SKILL.md` and `skills/commit-pr-convention/SKILL.md` still pin those documents' table wording, and `trail/phases/phase-1.md` names them.

Phase 2 left two sentences of `templates/setup/config.md` that name `parity.md` as a table beside the config: line 4, "beside `parity.md`, in the same shape: a markdown table", and line 173, "the same rule `parity.md` already follows". Both state `config.md`'s own table shape too, which phase 5 rewrites with the whole document, so rewriting half of each now would leave a sentence phase 5 rewrites again. `.test_durations` still lists the test names this phase removed or renamed; `.github/scripts/durations_union.py` says a work item never commits that file.

`skills/verify/scripts/broad_gate.py` still calls the `Broad gate` value "the row" in about forty comments and docstrings, such as "The row runs with a pytest recorder" in its module docstring. Phase 1 reworded only the lines it changed. Design *Scope* item 7's `git grep` set lists `Broad gate row` but not a bare "the row", so phase 5 reaches these lines only if it reads the file.
