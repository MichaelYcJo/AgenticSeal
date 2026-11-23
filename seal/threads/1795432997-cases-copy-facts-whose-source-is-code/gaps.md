# Closing memo: 1795432997-cases-copy-facts-whose-source-is-code

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the build's last commit. Phase 1 changes `tests/conftest.py`, which every test module imports, and ran only `frame/plan.md`'s phase 1 set. That set holds one case of `tests/skills/test_chain_check.py`, the one the removed `template_section` fed | the orchestrator's broad run, after the review rounds settle |
| The test modules outside phase 2's boundary set. That set was `tests/text`, `tests/behaviour`, `tests/skills/test_passages.py`, and the two other modules that load `skills/settle/scripts/passages.py`, `tests/skills/test_rule_changes.py` and `tests/skills/test_chain_check.py`. No other module reads a path phase 2 changed: `git grep passages -- 'tests/**/*.py'` lists those five files, and the one module that imports a changed test module, `tests/text/test_the_direct_answer_owes_the_sealers_record.py`, stands in `tests/text` | the orchestrator's broad run, after the review rounds settle |

## Not done

Phase 2 left four template cases of `tests/behaviour/test_waiver_decided_at_start.py` as they were. They put `lib/` on `sys.path` and `import routing` inside the case, beside the module-level `routing` that phase loads. Each parses the template through `routing.parse`, which is the same module either way. Moving them onto the module-level loader is a refactor no *Scope* item of `frame/design.md` names, so it was not taken (`trail/phases/phase-2.md`).
