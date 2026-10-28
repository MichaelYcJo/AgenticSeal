# Implementation Plan: 1793169126-a-case-passes-before-the-pull-request-and-fails-on-it

Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phases 1 and 2.

## Summary

The crafter makes `tests/conftest.py` remove every `GITHUB_` variable when it
is imported, pins that with one case in `tests/test_conftest.py`, and removes
every per-case line that cleared one by hand, all in one commit (phase 1).
Then it adds to the orchestrator's pre-pull-request CI paragraph in
`skills/code-review/orchestration.md` the name of the run it reads, and why
that run's cases see a pull request's environment, with one pinned assertion
(phase 2). The pull request still opens after the sealer, as #943 set.

## Technical context

- **The readers.** Six places in the shipped code read a variable a workflow
  sets: `skills/code-review/scripts/chain_check.py:764`, `:775`
  (`GITHUB_EVENT_PATH`) and `:2012` (`GITHUB_HEAD_REF`);
  `skills/verify/scripts/unverified_check.py:1449` (`GITHUB_ACTIONS`);
  `.github/scripts/durations_union.py:181` (`GITHUB_STEP_SUMMARY`, through an
  `env` argument); `.github/scripts/publish_release_note.py:439`
  (`GITHUB_OUTPUT`). Executed: `git grep -n "GITHUB_" -- '*.py'` at
  `977b6613`. Each read sits inside a function, so none is evaluated when a
  test module imports the script.
- **The conftest's precedent.** `tests/conftest.py:385` to `:416` already
  changes the environment at import, for `gh`'s login. Its comment states why
  import time: every entry point and every child that inherits `os.environ`
  sees the change. `tests/conftest.py#_no_session_in_the_environment` (`:536`)
  is the function-scoped alternative, used for `SESSION_VARIABLES`.
- **Fixtures wider than a function.** 32 fixtures under `tests/` are scoped to
  a module, a class, a package or the session (executed: `git grep -nE
  "scope=.(module|session|class|package)." -- tests`, counted with `wc -l`).
  Fourteen are in the three modules that drive the readers. One,
  `tests/skills/test_broad_gate.py#a_recorded_run` (`:2322`), starts the gate
  as a child, and today it passes `env=clean_env()` (`:2341`) because a
  function-scoped autouse fixture has not run yet when a module-scoped one
  does. That one coordinate is the failure scenario of every function-scoped
  design below.
- **The pin's shape.** `tests/test_conftest.py#test_the_conftest_takes_every_gh_login_away`
  (`:508`) runs `PROBE` (`:66`), which calls `runpy.run_path` on the conftest
  in a child whose environment the case sets, and prints what is left as
  JSON. The new case uses the same child, with the variables of
  `frame/design.md` S1 in place of the tokens.
- **The CI step.** `skills/code-review/orchestration.md:191` to `:198` tells
  the orchestrator to run `gh workflow run tests --ref <branch>` where the
  risk is platform-specific, and to read that run before the broad run.
  `.github/workflows/test.yml:3` to `:12` starts `tests` on `push` to `main`,
  on `pull_request` and on `workflow_dispatch`. The only places it reads the
  event are the concurrency group (`:20` and `:21`) and the `release-report`
  job's `github.base_ref == 'main'` guard (`:251`); executed, `grep -n
  "github\."` over the file. `.github/workflows/hygiene.yml:3` starts only on
  `pull_request`. The sealer reads no CI run: executed, a `grep -n` for `CI`
  as a word, `gh run`, `workflow` and `tests run` over `agents/sealer.md`
  printed nothing.
- **Failure scenario of the chosen approach, six months out.** A case writes
  `os.environ["GITHUB_..."]` directly instead of through `monkeypatch`, and
  the value leaks into the cases after it in the same xdist worker. That leak
  shows on a local run as well as on a pull request, so the run read before
  the pull request sees it; it is not this issue's class. The second
  scenario: a future step inside the pytest process needs the runner's real
  value of a `GITHUB_` variable, for example to write the step summary from a
  pytest hook. Today nothing in the pytest process does (the summary is
  written by a shell step, `.github/workflows/test.yml:285`), and such a hook
  would have to read the value before the conftest is imported. The conftest
  comment states this limit.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A function-scoped autouse fixture in `tests/conftest.py` that removes a named list of variables, as the issue's first bullet spells it | `tests/skills/test_broad_gate.py#a_recorded_run` is module-scoped and starts the gate before any function-scoped fixture runs, so its child still sees a `pull_request` run's `GITHUB_EVENT_PATH` and `GITHUB_HEAD_REF`. Its `clean_env()` filter could not go, and "no case clears by hand" would not hold. A list also has to be edited when a reader takes a new name, such as `GITHUB_REF`, and a reader added without that edit fails only on a pull request, which is the defect again. | rejected |
| The same fixture, removing every name with the `GITHUB_` prefix | Fixes the list going stale. The scope failure of the row above stands unchanged. | rejected |
| **Import-time removal of every `GITHUB_` name in `tests/conftest.py`, beside the `gh` block** | A case writing `os.environ` directly leaks to later cases in its worker, which a local run shows too. A future in-process hook that needs a runner's real `GITHUB_` value reads it before the conftest import. Both are stated in Technical context. | chosen |
| Keep the per-case lines, and add a text check that refuses a case reading a `GITHUB_` variable without clearing it | The check guesses from words which case reaches a reader, through helpers and children it cannot follow. `CLAUDE.md` *The rule a mechanism is kept against*: a check gates only a fact it reads, and a reading guessed from words is a report. A new case that forgets is still the failure. | rejected |
| Keep the `workflow_dispatch` run and name it in the orchestration step | The dispatch run cannot have a pull request's merge commit or the `hygiene` workflow, and the paragraph says so. The premise that keeps the dispatch run is #943's order: the pull request opens ready once the sealer has sealed (`skills/code-review/orchestration.md:161`, read). After the sweep, the environment difference between the two events no longer reaches any case, which is the part of the gap this issue is about. | chosen |
| A `tests` job that, when dispatched for a branch, sets the variables a `pull_request` run sets | It keeps a copy of GitHub's event environment in the workflow file that has to stay in step with GitHub, against `CLAUDE.md` *The rule a mechanism is kept against*. After the sweep no case sees those variables, so the copy would catch nothing. It still has no merge commit. | rejected |
| Open the pull request before the sealer, so the run read before sealing is the `pull_request` run | It reverses #943, which the owner set. A ready pull request would show an unsealed branch to reviewers and to `hygiene`, and the dispatch-run step and its stated limit would be rewritten for a defect the sweep already closes at the case. It would also need a person to reverse a recorded decision, which the goal in `CLAUDE.md` weighs against. | rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `tests/conftest.py` removes every `GITHUB_` variable at import; one new case in `tests/test_conftest.py` pins it (S1); every per-case clearing line `frame/design.md` *Removes* names goes; `CONTRIBUTING.md`'s "The suite runs with `gh` logged out" paragraph gains the sentence on `GITHUB_` variables. One commit. | The new case seen red against `tests/conftest.py` at `977b6613` before the sweep is written. Then `bin/test tests/test_conftest.py tests/skills/test_chain_check.py tests/skills/test_broad_gate.py tests/skills/test_unverified_check.py tests/github/test_publish_release_note.py tests/github/test_durations_union.py tests/e2e/teammate/test_teammate_flow.py -q`, run twice: once as is, and once with `GITHUB_HEAD_REF=feature/x`, `GITHUB_EVENT_PATH` naming a file that holds `{"pull_request": {"draft": false}}`, and `GITHUB_ACTIONS=true` exported (S2, S3). Exit codes read directly. `git grep -n GITHUB_ -- tests` read against S4. | 84668705 |
| 2 | The paragraph opening "Where the work's risk is platform-specific" in `skills/code-review/orchestration.md` names the `workflow_dispatch` run of `tests`, says why its cases see a `pull_request` run's environment, and names what it cannot have (S5). `tests/text/test_the_rules_have_one_owner.py#test_the_owner_states_the_dispatch_step_and_the_limit` gains one assertion on the new sentence. | The new assertion seen red with the new sentence deleted, then `bin/test tests/text/test_the_rules_have_one_owner.py -q` green. | |

## Operational impact

None for a deployer: no new environment variable, no new dependency, no
workflow change. A contributor's case that needs a `GITHUB_` variable sets it
with `monkeypatch.setenv`, because the conftest removes them all at import.
The full suite is `unverified` in every phase, and the orchestrator answers it
with the one broad run.
