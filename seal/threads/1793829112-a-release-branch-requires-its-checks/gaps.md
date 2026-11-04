# Closing memo: 1793829112-a-release-branch-requires-its-checks

## Not verified

| Item | Who must answer |
|---|---|
| The `release` ruleset does not yet require `lint` and `release`. `docs/releasing/branch-and-release.md` *Work accumulates on a release branch* and `changelog.md` state the setting `frame/design.md` *Scope* item 1 applies, and until that `gh api` act they state a setting the repository does not hold. Scenarios S1, S2 and S5 of `frame/design.md` read it | the orchestrator, once the last round record has no finding open and before it runs `seal gate --preflight` (`frame/plan.md` *Operational impact*) |
| The test modules that read `docs/releasing/` or `.claude-plugin/plugin.json` and that `frame/plan.md`'s Verified by grep does not list were not run, such as `tests/text/test_the_rules_have_one_owner.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and `tests/hooks/test_version_check.py`. The spawn limited the phase to the modules that grep lists | the orchestrator, at the broad gate |
| The suite, the repository-wide lint and the typecheck | the orchestrator, at the broad gate |

## Not done

nothing
