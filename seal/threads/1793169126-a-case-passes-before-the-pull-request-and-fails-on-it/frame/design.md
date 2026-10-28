# Feature Specification: 1793169126-a-case-passes-before-the-pull-request-and-fails-on-it

Issue #1058. Pull request #1057 went red on every platform after the sealer
had sealed it. Three cases called `chain_check.declared_for_this_branch` in
process, and that function reads the branch from `GITHUB_HEAD_REF` before the
checked-out one (`skills/code-review/scripts/chain_check.py:2012`). A
`pull_request` run sets that variable, and every run before the pull request
(the local runs, the broad gate, and the `workflow_dispatch` run of `tests`)
leaves it empty. This work makes every case see the same environment under
both events, removes the per-case lines that cleared it by hand, and has the
orchestrator's pre-pull-request CI step name the run it reads.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The goal a design is chosen against* | Between two designs that catch the same defect, the one that stops for a person costs more. Both designs for the CI run are weighed on that: the chosen one asks nobody and keeps the order #943 set. |
| `CLAUDE.md` *The rule a mechanism is kept against* | "A change rewrites the text it amends in place, and in the same commit removes what stood on the old fact." So the per-case clearing lines leave in the commit that adds the conftest sweep, and phase 1 is one commit. "Nothing is kept beside the tree to stay in step with it": the sweep removes every name with the `GITHUB_` prefix, not a list of the names today's readers take. "A check gates only a fact it reads": no new check searches the tests for a clearing line written by hand. |
| `docs/the-broad-gate.md` *One act, one owner, and the owner is the orchestrator* | The sealer runs nothing broad and reads `trail/gate.md`, the orchestrator's local broad run. So "the run the sealer reads" in the issue's third *Done when* bullet is that local run, whose environment holds no `GITHUB_` variable, the same as a case's after the sweep. |
| `docs/branch-and-release.md` *Cutting a release*, its closing paragraph at `:98` to `:100`, opening "Which workflows GitHub starts on which event" | Which workflows GitHub starts on which event is GitHub's behaviour, and no case here can start a run. What a `workflow_dispatch` run lacks against a `pull_request` run is stated in the orchestration step, and no case pins it. |
| `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* | The pull request opens ready once the sealer has sealed (#943). The paragraph opening "Where the work's risk is platform-specific" is the step that reads CI before the sealer, and it is the one this work amends. |
| contract rule 12 | The class is every case that clears a `GITHUB_` variable the case did not set itself, in every test file, not only the six `GITHUB_HEAD_REF` lines the issue lists. The enumeration is under `## Removes`. |
| contract rule 15 | The new conftest case is seen red against `tests/conftest.py` as it stands at `977b6613` before it is committed. |

## Scope

In:

- **`tests/conftest.py` removes every environment variable whose name starts
  with `GITHUB_` when it is imported.** It sits beside the block that logs
  `gh` out (`tests/conftest.py:385` to `:416` at `977b6613`), and it is
  import-time for the same reason that block is: every entry point (`bin/test`,
  bare `pytest`, each xdist worker), every fixture of every scope, and every
  child that inherits `os.environ` sees the result. A case that needs one of
  these variables sets it with `monkeypatch.setenv`, as the cases that set
  `GITHUB_HEAD_REF` already do.
- **One new case in `tests/test_conftest.py` pins the sweep.** A child process
  whose environment carries the variables a `pull_request` run sets runs the
  conftest's import-time code and reports every `GITHUB_` name left. The case
  takes the shape of `tests/test_conftest.py#test_the_conftest_takes_every_gh_login_away`
  and its `PROBE`.
- **Every line in `tests/` that clears a `GITHUB_` variable the case did not
  set itself goes, in the same commit.** `## Removes` lists each one.
- **`CONTRIBUTING.md`'s paragraph "The suite runs with `gh` logged out" gains
  one sentence** saying the conftest also removes every `GITHUB_` variable,
  and that a case needing one sets it. That paragraph is where a contributor
  already learns what the conftest takes from the environment.
- **The paragraph in `skills/code-review/orchestration.md` opening "Where the
  work's risk is platform-specific" names the run it reads**: a
  `workflow_dispatch` run of `tests`. It says that run's cases see what a
  `pull_request` run's cases see, because `tests/conftest.py` removes every
  `GITHUB_` variable at import. It also says what the dispatch run cannot
  have: a pull request's merge commit, and the `hygiene` workflow, which
  starts only on a `pull_request` event (`.github/workflows/hygiene.yml:3`).
  `tests/text/test_the_rules_have_one_owner.py#test_the_owner_states_the_dispatch_step_and_the_limit`
  gains an assertion on the new sentence.

Out:

- **Opening the pull request before the sealer.** It reverses #943's order,
  and the sweep already makes the dispatch run's cases equal to the
  `pull_request` run's. `plan.md` *Alternatives considered* holds the
  comparison.
- **A `tests` job that sets a `pull_request` run's variables when dispatched.**
  With the sweep in place no case would see them. `plan.md` holds the
  comparison.
- **`RUNNER_` variables and `CI`.** No reader in the tree takes either from
  the environment (executed: `git grep -nE 'environ(\.get)?\(?\[?"(CI|RUNNER_[A-Z_]*)"' -- '*.py'`
  printed nothing). `tests/e2e/teammate/test_teammate_flow.py#without_this_run`
  keeps stripping the `GIT_` and `RUNNER_` prefixes for its own child.
- **`SESSION_VARIABLES` reaching a fixture wider than a function.** The
  conftest clears them per case (`tests/conftest.py#_no_session_in_the_environment`),
  so a module-scoped fixture still sees a live session's variables. That
  defect shows on a local run inside a session and not on CI, so the run
  read before the pull request already sees it. It is not this issue's class.
  `tests/skills/test_broad_gate.py#clean_env` keeps stripping
  `CLAUDE_CODE_SESSION_ID` for the module-scoped `a_recorded_run` for that
  reason.
- **The six readers themselves.** `chain_check.py:764`, `:775` and `:2012`,
  `unverified_check.py:1449`, `durations_union.py:181` and
  `publish_release_note.py:439` read the workflow's environment because they
  run in a workflow. The defect is in how the cases meet that environment.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1, the sweep | Given a process whose environment holds `GITHUB_HEAD_REF`, `GITHUB_BASE_REF`, `GITHUB_EVENT_NAME`, `GITHUB_EVENT_PATH`, `GITHUB_ACTIONS` and `GITHUB_REF`, as a `pull_request` runner sets them. When `tests/conftest.py`'s import-time code runs. Then no name starting with `GITHUB_` is left in `os.environ`, and the `gh` token result of the existing probe case is unchanged. | A new case in `tests/test_conftest.py` beside `test_the_conftest_takes_every_gh_login_away`, run by `bin/test tests/test_conftest.py -q`. It is seen red against `tests/conftest.py` at `977b6613` first. |
| S2, a case under a pull request's environment | Given the three cases of `tests/skills/test_chain_check.py` that call `chain.declared_for_this_branch` (the ones holding `:2875`, `:2891` and `:2906` at `977b6613`), with their `delenv` lines removed. When the suite runs with `GITHUB_HEAD_REF`, `GITHUB_EVENT_PATH` and `GITHUB_ACTIONS` exported in the shell that starts it. Then each case judges the checked-out branch and passes. | The crafter runs the seven edited test modules with those three variables exported, and runs them again without them; both runs pass. The `pull_request` run of the pull request itself confirms it on every platform (`questions.md` M1). |
| S3, a wider fixture under a pull request's environment | Given `tests/skills/test_broad_gate.py#a_recorded_run`, a module-scoped fixture that starts the gate as a child, with `GITHUB_EVENT_PATH` and `GITHUB_HEAD_REF` gone from `AMBIENT`. When the module runs with those variables exported. Then the gate child sees neither variable and the module passes. | The same exported run as S2, over `tests/skills/test_broad_gate.py`. |
| S4, no case clears by hand | Given the tree after phase 1. When `git grep -n GITHUB_ -- tests` runs. Then every line it prints that removes or filters out a `GITHUB_` variable removes one the same case set earlier (`test_chain_check.py:1812` and `:1817`, `test_unverified_check.py:1816` at `977b6613`). | check: none reader: the proofer at review. The proofer runs the `git grep` and reads each line against this cell. |
| S5, the CI step names its run | Given the orchestrator at the paragraph opening "Where the work's risk is platform-specific". When it reads the paragraph. Then the paragraph names the `workflow_dispatch` run of `tests` as the run it reads, says its cases see a `pull_request` run's environment because `tests/conftest.py` removes every `GITHUB_` variable at import, and names what that run cannot have. The sentence "run `gh workflow run tests --ref <branch>`" and the stated limit stay as they read. | `tests/text/test_the_rules_have_one_owner.py#test_the_owner_states_the_dispatch_step_and_the_limit`, with one new assertion seen red with the new sentence deleted. |

## Data & interfaces

- **`tests/conftest.py`**, at import, beside the `GH_CREDENTIALS` block: every
  key of `os.environ` that starts with `GITHUB_` is popped. The names are read
  from `os.environ` itself, so a workflow variable a future reader takes is
  covered without an edit. The `GH_CREDENTIALS` tuple keeps its four names:
  its comment explains `gh`'s lookup order, and that is a different fact from
  the workflow's environment. A comment above the sweep names #1058 and the
  failed run (`gh run view 40446828473 --log-failed`), and says that a case
  needing one of these variables sets it.
- **`tests/test_conftest.py`**: one new case. Its child runs the conftest as
  `PROBE` does (`runpy.run_path` with `cwd=TESTS`), with the six variables of
  S1 set in the child's environment, and prints the sorted list of `GITHUB_`
  names left. The case asserts the list is empty.
- **`skills/code-review/orchestration.md`**, the paragraph at `:191` to
  `:198` at `977b6613`: one or two sentences added after "then read that
  run's result before you take the broad run". The rest of the paragraph and
  the stated-limit paragraph at `:200` keep their text, because
  `tests/text/test_the_rules_have_one_owner.py:262` and `:263` pin it.
- No script, hook, workflow file or record shape changes.

## Rule changes

- nothing
  why: the rule this work adds lives in `tests/conftest.py`, and the step it amends lives in `skills/code-review/orchestration.md`. Neither is in the policy root, and no section of `docs/` states how a case meets the workflow's environment or which CI run the orchestrator reads.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `delenv` of `GITHUB_ACTIONS` and of `GITHUB_HEAD_REF` in the `event` helper | `tests/skills/test_chain_check.py#event`, `:248` and `:249` at `977b6613` | The conftest sweep. The helper keeps its `setenv` of `GITHUB_EVENT_PATH`. |
| The `delenv` of `GITHUB_HEAD_REF`, the two comment lines below it, and the `delenv` of `GITHUB_ACTIONS` | `tests/skills/test_chain_check.py`, `:2326` to `:2329` at `977b6613` | The conftest sweep. The comment explained why the line cleared `GITHUB_ACTIONS`, and the line goes with it. |
| The two `env.pop` lines for `GITHUB_EVENT_PATH` and `GITHUB_HEAD_REF` | `tests/skills/test_chain_check.py#run_check`, `:2784` and `:2785` at `977b6613` | The conftest sweep. `dict(os.environ)` already holds neither name. |
| Three `delenv` lines of `GITHUB_HEAD_REF` | `tests/skills/test_chain_check.py`, `:2875`, `:2891` and `:2906` at `977b6613` | The conftest sweep. These are the cases #1057's `pull_request` run failed. |
| `GITHUB_EVENT_PATH` and `GITHUB_HEAD_REF` in the `AMBIENT` tuple, and the comment above it | `tests/skills/test_broad_gate.py:75` to `:77` at `977b6613` | The conftest sweep. `AMBIENT` keeps `CLAUDE_CODE_SESSION_ID` for `clean_env`, whose caller `a_recorded_run` is module-scoped. Its comment is rewritten to say so. |
| The `_no_ambient_pull_request` autouse fixture | `tests/skills/test_broad_gate.py#_no_ambient_pull_request`, `:152` to `:157` at `977b6613` | Its `GITHUB_` names go to the conftest sweep. Its one remaining name, `CLAUDE_CODE_SESSION_ID`, is in `SESSION_VARIABLES`, which `tests/conftest.py#_no_session_in_the_environment` clears for every case. |
| The `env=` filter on `GITHUB_EVENT_PATH` and `GITHUB_HEAD_REF` | `tests/skills/test_broad_gate.py#run_gate`, `:2489` to `:2493` at `977b6613` | The conftest sweep. The child inherits `os.environ`. |
| Two `delenv` lines of `GITHUB_ACTIONS` that precede a conditional `setenv` | `tests/skills/test_unverified_check.py:1821` and `:2045` at `977b6613` | The conftest sweep. |
| The `delenv` of `GITHUB_OUTPUT` and the two comment lines above it | `tests/github/test_publish_release_note.py:146` to `:148` at `977b6613` | The conftest sweep. |
| The `env=` filter on `GITHUB_STEP_SUMMARY` | `tests/github/test_durations_union.py:110` at `977b6613` | The conftest sweep. The child inherits `os.environ`. |
| `"GITHUB_"` in the prefix tuple, and the word "GitHub" in the docstring | `tests/e2e/teammate/test_teammate_flow.py#without_this_run`, `:126` to `:131` at `977b6613` | The conftest sweep. The function keeps stripping `GIT_` and `RUNNER_`. |

## Open questions

<none here: each is a row of `questions.md`>

Framed 2026-10-28 by framer, before the build.
