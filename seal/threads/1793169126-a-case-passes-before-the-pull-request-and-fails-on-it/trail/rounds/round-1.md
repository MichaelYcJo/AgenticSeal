# Review round 1: 1793169126-a-case-passes-before-the-pull-request-and-fails-on-it

target: 87f3e454 against 977b6613

This is the first round, so no earlier round's coordinates were carried; every fact below was established this round. `seal/parity.md` is not declared and the diff changes paths outside `docs/` and `seal/` with no migration config, so no `original:` line is written.

## Findings

### 1. The conftest comment and the changelog say a `workflow_dispatch` run sets no `GITHUB_EVENT_PATH` and no other workflow variable

severity: should
location: `tests/conftest.py:418-424`, `seal/threads/1793169126-a-case-passes-before-the-pull-request-and-fails-on-it/changelog.md:3`
evidence: read `tests/conftest.py:418-424`, `seal/threads/1793169126-a-case-passes-before-the-pull-request-and-fails-on-it/changelog.md:3`, `skills/code-review/scripts/chain_check.py:771-787`
verdict: fixed d28b2375

The new comment above the sweep says: "A `pull_request` run sets `GITHUB_HEAD_REF`, `GITHUB_EVENT_PATH` and the rest for every step, and a `workflow_dispatch` run, a local run and the broad gate do not." The changelog fragment says the same: "A `pull_request` run of `tests` sets `GITHUB_HEAD_REF`, `GITHUB_EVENT_PATH` and other workflow variables, and a local run, the broad gate and a `workflow_dispatch` run do not."

That is wrong for the dispatch run. GitHub sets `GITHUB_ACTIONS`, `GITHUB_EVENT_PATH`, `GITHUB_EVENT_NAME` and `GITHUB_REF` for every workflow run, whatever the event. Only `GITHUB_HEAD_REF` and `GITHUB_BASE_REF` are reserved for a pull request event. The tree knows this. `skills/code-review/scripts/chain_check.py:785-787` handles an event payload that exists and names no pull request, which is what a dispatch or push run hands it. The `item` fixture this branch edits cleared `GITHUB_ACTIONS` because "Under Actions the check prints `::error` annotations" (`tests/skills/test_chain_check.py:2326-2329` at `977b6613`). Under the old sentence that line would have had nothing to clear on a dispatch run. `frame/design.md` states the difference correctly: only `GITHUB_HEAD_REF` separates the two events.

Why it matters: the comment is the text a later contributor or agent reads to learn which run sees what. Read as written, it says a dispatch run's cases already had a local run's environment before the sweep. A reader would then expect a case that reads `GITHUB_ACTIONS` or the event payload to behave the same on a dispatch run and on a laptop. That was false before this branch. After the branch it holds only because of the sweep. The changelog carries the same sentence into the release note a user reads. The sweep itself is unaffected: it removes every `GITHUB_` name whichever ones the event set.

```python
# The suite runs with no workflow variable, under every event (#1058). Every
# workflow run sets `GITHUB_ACTIONS`, `GITHUB_EVENT_PATH` and the rest, and
# only a `pull_request` run sets `GITHUB_HEAD_REF`; a local run and the broad
# gate set none. Three cases that judged the checked-out branch passed on a
# local run, the broad gate and a `workflow_dispatch` run, and failed on pull
# request #1057's run (`gh run view 40446828473 --log-failed`), because the
# script they drove reads `GITHUB_HEAD_REF` first. So every name that starts
# with `GITHUB_` is removed here, at import, for the reason the block above
# is: every entry point, every fixture of every scope and every child that
# inherits `os.environ` sees the same environment.
```

The changelog's first two sentences, as they would read:

```markdown
- **A case could pass on every run before a pull request and fail on the pull request's own run (#1058).** Only a `pull_request` run of `tests` sets `GITHUB_HEAD_REF`. A `workflow_dispatch` run sets `GITHUB_EVENT_PATH`, `GITHUB_ACTIONS` and the other workflow variables, and a local run and the broad gate set none of them.
```

answer: The finding holds: every workflow run sets `GITHUB_ACTIONS`, `GITHUB_EVENT_PATH`, `GITHUB_EVENT_NAME` and `GITHUB_REF`, and only a pull request event sets `GITHUB_HEAD_REF` and `GITHUB_BASE_REF`. `d28b2375` puts the record's text into the conftest comment (`tests/conftest.py:418-427`) and into the changelog fragment's first two sentences; the sweep's code is unchanged. The same commit also corrects one more instance of the fact, which `location:` does not list: the new case's docstring at `tests/test_conftest.py:560-563` said a case sees "the environment of a run with no pull request", and a dispatch run has no pull request and sets workflow variables, so it now says a case sees no workflow variable. `git grep` over `CONTRIBUTING.md`, `skills/code-review/orchestration.md`, `gaps.md`, the changelog's second entry and the phase records finds no other sentence stating it: `CONTRIBUTING.md:205-208` and `orchestration.md:195-197` state what a case sees after the sweep, `gaps.md`'s purpose line says only that `GITHUB_HEAD_REF` is pull-request-only, and the phase records state what their phases did. Executed: `uvx ruff check` and `uvx ruff format --check` on `tests/conftest.py` and `tests/test_conftest.py` exit 0, and `bin/test tests/test_conftest.py -q` exits 0 (54 passed).

## Confirmations

confirms: none
S1 holds. The crafter claimed the new case `tests/test_conftest.py:559` goes red without the sweep. Executed: with the delete at `tests/conftest.py:433` replaced by `pass` in this round's clone and the three variables exported, the case failed. At `87f3e454` it passed. Its `given` assertion (`tests/test_conftest.py:568`) makes the probe child's own environment part of the claim. So a child that silently lost its environment cannot pass, as `84668705` says.

confirms: none
S2 holds. Executed: at `87f3e454`, with `GITHUB_HEAD_REF=feature/x`, `GITHUB_EVENT_PATH` naming a payload with a ready pull request and `GITHUB_ACTIONS=true` exported, the `Test_declared_for_this_branch` cases and both conftest probe cases passed (11 passed). With the sweep disabled under the same exports, the three cases that call `chain.declared_for_this_branch` failed, four results counting the parametrisation. So did `test_the_shared_sentence_says_what_it_searched_and_for_what`, which goes through `run_check`. That is #1057's failure, and it shows that the `env.pop` lines removed from `run_check` (`tests/skills/test_chain_check.py:2776-2794`) now rest on the sweep.

confirms: none
S4 holds. Executed: `git grep -n GITHUB_ -- tests` at `87f3e454`. Read: the only lines it prints that remove a variable are `tests/skills/test_chain_check.py:1810` and `:1815` and `tests/skills/test_unverified_check.py:1816`. Each one clears a value its own case or that case's fixture set a few lines earlier. No pytest file outside `tests/` clears a `GITHUB_` name; executed, `git grep` over `*.py` outside `tests/` printed only the six readers the plan names.

confirms: none
Every row of `frame/design.md` *Removes* is gone in the diff, and the lines it says to keep stay. Read: `git diff 977b6613..87f3e454` over the seven test modules. The `event` helper keeps its `setenv` (`tests/skills/test_chain_check.py:247`). `AMBIENT` keeps `CLAUDE_CODE_SESSION_ID` for `clean_env` (`tests/skills/test_broad_gate.py:79`, `:154-155`), and its comment now says why. `without_this_run` keeps `GIT_` and `RUNNER_` (`tests/e2e/teammate/test_teammate_flow.py:125-128`). Dropping `_no_ambient_pull_request` loses nothing: `CLAUDE_CODE_SESSION_ID` is in `SESSION_VARIABLES`, which the autouse `_no_session_in_the_environment` clears for every case (`tests/conftest.py:543-556`). `GH_CREDENTIALS` keeps its four names (`tests/conftest.py:402-407`). The e2e module is under the root conftest: the clone has no `pytest.ini`, no pytest section in `pyproject.toml` and no `conftest.py` under `tests/e2e`.

confirms: none
The sweep leaves the CI suite nothing it needed. Read: the `pytest` job runs `pytest` with `pytest-xdist` and `pytest-split` (`.github/workflows/test.yml:149`, `:158`). Neither the plugins nor any code in the pytest process reads a `GITHUB_` variable. The step summary is written by shell steps, and the six readers are scripts that run as their own steps. No module under `tests/` reads a `GITHUB_` variable at import to decide a skip; executed, the same `git grep`.

confirms: none
S5 holds. Read: `skills/code-review/orchestration.md:195-199` names the `workflow_dispatch` run, says why its cases match a `pull_request` run's, and names the merge commit and `hygiene`. `hygiene` starts only on `pull_request` (`.github/workflows/hygiene.yml:3-4`). The `release-report` job is the only other thing a dispatch run lacks (`.github/workflows/test.yml:251`, `github.base_ref == 'main'`). A work item's pull request into a release branch does not run it either, so the list is complete for the run this step reads. The command sentence and the stated-limit paragraph keep their text. Executed: `bin/test tests/text/test_the_rules_have_one_owner.py tests/text/test_the_suite_runs_with_gh_logged_out.py tests/behaviour/test_docs_line_wrap.py -q` passed (71 passed). The new assertion is a substring of the paragraph, so deleting the sentences turns it red by construction (read, `tests/text/test_the_rules_have_one_owner.py:265-271`).

confirms: none
The four divergences in `gaps.md` were checked against the code. (1) The CONTRIBUTING needle (`tests/text/test_the_suite_runs_with_gh_logged_out.py:36-39`) is what contract rule 14 asks of a changed sentence a person reads; read. (2) Phase 1 took two commits. Executed, `git show --stat`: `8b8e85f6` holds the sweep and every removal, and `84668705` adds three lines to `tests/test_conftest.py` only. So the frame's ground for "one commit", that the removals land with the sweep, holds. (3) The three sentences each carry one of the three facts S5 asks for; read. (4) S3 resting on S1: read. `a_recorded_run` builds its child's environment from `os.environ` through `clean_env` (`tests/skills/test_broad_gate.py:2335`), so the gate child inherits whatever the import-time sweep left. Whether that module stays green with the sweep disabled was not re-run; see `## Not judged`.

confirms: none
The new case was read against its group. It adds what `test_the_conftest_takes_every_gh_login_away` does not cover, the `GITHUB_` names. Its token assertion is the one S1 asks for in its Then clause. Executed: `bin/seal layout --pairs` prints no pair in `tests/test_conftest.py`, `tests/text/test_the_rules_have_one_owner.py` or `tests/text/test_the_suite_runs_with_gh_logged_out.py`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck over this branch; `unverified` | the branch at `87f3e454` | the orchestrator, by its one `seal gate` run after the rounds settle |
| `frame/questions.md` M1: the `declared_for_this_branch` cases and `a_recorded_run` on this pull request's own `pull_request` run, on every platform leg; this round ran on macOS only | `.github/workflows/test.yml:35` | the orchestrator, reading the `pull_request` run once the pull request opens |
| Whether `tests/skills/test_broad_gate.py` stays green under the exported variables with the sweep disabled (`gaps.md` divergence 4); not re-run, and no verdict here rests on it | `tests/skills/test_broad_gate.py:2335` | the sealer, where it samples the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `GITHUB_HEAD_REF=feature/x GITHUB_EVENT_PATH=<scratch>/event.json GITHUB_ACTIONS=true bin/test tests/test_conftest.py tests/skills/test_chain_check.py -q -k 'github_variable or gh_login or Test_declared_for_this_branch'`, in a clone at `87f3e454` | exit 0, 11 passed |
| The same command, with `del os.environ[_name]` at `tests/conftest.py:433` replaced by `pass` in the clone | exit 1, 6 failed: the new conftest case, the three `declared_for_this_branch` cases (four results) and `test_the_shared_sentence_says_what_it_searched_and_for_what` |
| `bin/test tests/text/test_the_rules_have_one_owner.py tests/text/test_the_suite_runs_with_gh_logged_out.py tests/behaviour/test_docs_line_wrap.py -q`, in the clone | exit 0, 71 passed |
| `bin/seal layout --pairs`, in the clone | exit 0, 128 pairs, none in a file this branch changes |
| `git grep -n GITHUB_ -- tests`, at `87f3e454` | three removing lines, each clearing a value its own case set |
