# Closing memo: 1793829112-a-release-branch-requires-its-checks

## Not verified

| Item | Who must answer |
|---|---|
| closed The `release` ruleset does not yet require `lint` and `release`. `docs/releasing/branch-and-release.md` *Work accumulates on a release branch* and `changelog.md` state the setting `frame/design.md` *Scope* item 1 applies, and until that `gh api` act they state a setting the repository does not hold. Scenarios S1, S2 and S5 of `frame/design.md` read it | the orchestrator applied Scope 1 on 2026-11-05 after round 2 and read S1 and S2 (`frame/plan.md` *Judgments of the run*, the row of the apply); S5 is read at the merge |
| closed The test modules that read `docs/releasing/` or `.claude-plugin/plugin.json` and that `frame/plan.md`'s Verified by grep does not list were not run, such as `tests/text/test_the_rules_have_one_owner.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and `tests/hooks/test_version_check.py`. The spawn limited the phase to the modules that grep lists | the orchestrator's broad run at 60f2e40a ran the whole suite, 6342 passed and 12 skipped (`trail/gate.md`) |
| closed The suite, the repository-wide lint and the typecheck | the orchestrator's broad run at 60f2e40a passed its `Broad gate` row, `uvx ruff check .`, `uvx ruff format --check .` and `bin/test -q`; the row runs no typechecker (`trail/gate.md`, `seal/config.md`) |

## Not done

nothing
