# Closing memo: 1794465688-feature-prs-wait-on-the-macos-runner

## Not verified

| Item | Who must answer |
|---|---|
| the suite, the repository-wide lint and the format check beyond phase 1's boundary set | the orchestrator's broad gate |
| whether GitHub reads the `&pytest-steps` alias, runs `pytest`'s legs and skips `pytest-wide` on this pull request's first `pull_request` run, and the name the skipped check shows (`frame/questions.md` Q1, S1) | the orchestrator, from this pull request's first run with `gh api …/runs/<id>/jobs` |
| whether GitHub reads the `&pytest-steps` alias for `pytest-wide` and its legs report under the names G7 lists. On an entry with no `split` or `store`, the cache restore and the upload skip and the pytest line ends with two empty expansions, as jobs 130936327013 and 130936327217 of run 43143655875 showed (round 1). actionlint 1.7.12 reports the same two properties as undefined, and it is not a check of this repository | the orchestrator, from a `workflow_dispatch` run of `tests` on this branch before the pull request merges (`gh workflow run test.yml --ref chore/1516-feature-prs-wait-on-the-macos-runner`, then `gh api …/runs/<id>/jobs`): `github.base_ref` is empty on a dispatch, so `pytest-wide` runs |

## Not done

`job_scripts` moved into `tests/workflows.py` without a `Test_job_scripts`
class, which `seal layout --check` reports and does not refuse. The unit
moved unchanged, and the cases that held it in the CI case module hold it
at the new path, so a class written now would cover nothing those cases do
not (`skills/verify/SKILL.md` *The narrow command still has to be able to
fail*).

The six `test_a_job_that_calls_pytest_any_way_is_held_to_the_whole_history`
cases, which hold the reach of `RUNS_PYTEST`, stay in the CI case module
and reach the regex through `shallow_pytest_jobs` and `pytest_jobs`. Moving
them beside `Test_pytest_jobs` would rewrite cases the phase did not need
to change.

`pytest-wide`'s entries do not carry `split: ""` and `store: ""` to quiet
actionlint's three lines. Those keys would fail the rule that only Windows
entries carry a split or a store, and actionlint is not a check of this
repository.
