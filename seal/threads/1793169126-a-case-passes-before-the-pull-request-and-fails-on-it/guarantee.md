# Guarantee: 1793169126-a-case-passes-before-the-pull-request-and-fails-on-it

| Field | Value |
|---|---|
| Target SHA | f3443866 against 6e322bb7 |
| Broad gate | 6d49f1df against 6e322bb7 |

## Claims re-run

The claims were re-run in a clone of the branch at `f3443866`, with files restored from `6e322bb7` where a claim says red. The clone was removed afterwards. Exit codes were read directly.

| Claim | Source | Command | Result |
|---|---|---|---|
| The gate's record is at HEAD: only `trail/gate.md` follows the run's commit | `trail/gate.md:5` | `git log --no-merges --name-only 6d49f1df..HEAD ^6e322bb7`; `git merge-base --is-ancestor 6d49f1df HEAD` | holds (executed): one commit, `f3443866`, touching only `seal/threads/1793169126-a-case-passes-before-the-pull-request-and-fails-on-it/trail/gate.md`; `6d49f1df` is an ancestor of HEAD |
| The body's first part is the records' own text | the body file the orchestrator wrote | `bin/seal pr-body seal/threads/1793169126-a-case-passes-before-the-pull-request-and-fails-on-it --body <scratchpad>/1058-pr-body.md --check` | holds (executed): exit 0 |
| seen red: the new case fails against `tests/conftest.py` at the base, with all six names left | `trail/phases/phase-1.md:29-34` | `tests/conftest.py` restored from `6e322bb7`, then `bin/test tests/test_conftest.py -q -p no:xdist -k github_variable` | holds (executed): exit 1, `left by the conftest: ['GITHUB_ACTIONS', 'GITHUB_BASE_REF', 'GITHUB_EVENT_NAME', 'GITHUB_EVENT_PATH', 'GITHUB_HEAD_REF', 'GITHUB_REF']` at `tests/test_conftest.py:569` |
| seen red: without the sweep and under the exported variables, the three `declared_for_this_branch` cases fail, four results with the parametrisation | `trail/phases/phase-1.md:47-51` | `tests/conftest.py` restored from `6e322bb7`; `GITHUB_HEAD_REF=feature/x GITHUB_EVENT_PATH=<event.json naming a ready pull request> GITHUB_ACTIONS=true bin/test tests/skills/test_chain_check.py -q -k 'Test_declared_for_this_branch or shared_sentence_says_what_it_searched'` | holds (executed): exit 1, 5 failed, 4 passed; the four `declared_for_this_branch` results and `test_the_shared_sentence_says_what_it_searched_and_for_what`, which round 1 also saw fail |
| Without the sweep, `tests/skills/test_broad_gate.py` stays green under the exported variables, so S3's run is not evidence by itself; round 1's `## Not judged` left this to the sealer | `trail/phases/phase-1.md:52-57`, `gaps.md` divergence 4 | `tests/conftest.py` restored from `6e322bb7`; the same three exports; `bin/test tests/skills/test_broad_gate.py -q` | holds (executed): exit 0, 308 passed, 1 skipped |
| The seven modules pass at HEAD with the three variables exported | `trail/phases/phase-1.md:36-41` | at `f3443866`, the same three exports; `bin/test tests/test_conftest.py tests/skills/test_chain_check.py tests/skills/test_broad_gate.py tests/skills/test_unverified_check.py tests/github/test_publish_release_note.py tests/github/test_durations_union.py tests/e2e/teammate/test_teammate_flow.py -q` | holds (executed): exit 0, 1009 passed, 1 skipped, the figure the phase recorded |
| seen red: the orchestration assertion fails without the new sentences | `trail/phases/phase-2.md:18-23` | `skills/code-review/orchestration.md` restored from `6e322bb7`, then `bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist` | holds (executed): `test_the_owner_states_the_dispatch_step_and_the_limit` failed on the `workflow_dispatch` sentence; with HEAD's text restored, exit 0 |
| seen red: the CONTRIBUTING needle fails without the new sentence | `trail/phases/phase-1.md:77-81` | `CONTRIBUTING.md` restored from `6e322bb7`, then `bin/test tests/text/test_the_suite_runs_with_gh_logged_out.py -q -p no:xdist`, in the same run as the row above | holds (executed): exit 1 for the two files together, `CONTRIBUTING.md *Running the checks* lacks: The conftest also removes every variable whose name starts with GITHUB_ ...`; with HEAD's text restored, both files exit 0, 32 passed |
| Every `## Removes` row of `frame/design.md` is gone from the tree | `frame/design.md` *Removes*, eleven rows | `git grep -n` at HEAD for `_no_ambient_pull_request`, `env.pop("GITHUB`, `delenv("GITHUB_OUTPUT`, `k != "GITHUB_STEP_SUMMARY"` and `"GIT_", "GITHUB_"`; `git grep -nE 'delenv\("GITHUB_\|pop\("GITHUB_\|startswith\(.*"GITHUB_' HEAD -- tests` | holds (executed): the first grep printed nothing; the second prints the sweep, the probe's two readers, and `tests/skills/test_chain_check.py:1810`, `:1815` and `tests/skills/test_unverified_check.py:1816`, which `frame/questions.md` keeps because each clears a value its own case set (read: `:1804` sets `GITHUB_ACTIONS`, `tests/skills/test_unverified_check.py:1814` sets it) |
| The changelog's removal, "Every line in the tests that cleared one of these variables by hand, where its case had not set it, is removed" | `changelog.md:3` | the row above | holds (executed): the same grep |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | `tests/conftest.py` removes every `GITHUB_` name at import, one case pins it, the eleven *Removes* rows go, `CONTRIBUTING.md` gains a sentence, and the orchestration step names the `workflow_dispatch` run and what it lacks; the pull request still opens after the sealer | the issue's three *Done when* bullets, the build, the changelog | none. The issue's first change bullet names an autouse fixture; the spec chose import time, with its ground in `frame/plan.md` *Alternatives considered* (a module-scoped fixture starts before any function-scoped one). The issue's *Done when* names no mechanism, so this is a design choice, not a contradiction (read) |
| the build | the diff `6e322bb7...HEAD` holds the sweep at `tests/conftest.py:433`, the new case, every removal, the two prose changes and their pins; the phase records claim the reds and runs re-run above | the spec, the changelog, the tree | none. `gaps.md` names four divergences from the frame (an extra pin, two commits for phase 1, three sentences for "one or two", S3 resting on S1); each was read against the diff and agrees with it, and the S3 claim was re-run above |
| the last round | round 2 confirms round 1's one finding closed by `d28b2375` and opens nothing; round 1 confirms S1, S2, S4, S5 and the *Removes* rows | the build, the tree: `tests/conftest.py:418-427` and `changelog.md:3` state that every workflow run sets `GITHUB_ACTIONS` and `GITHUB_EVENT_PATH` and only a `pull_request` run sets `GITHUB_HEAD_REF` (read) | none |
| the changelog | Fixed: the conftest removes every `GITHUB_` variable at import and the hand-written clearing lines go; Changed: the orchestration step names the `workflow_dispatch` run, why its cases match, and what it cannot have | the diff of `tests/conftest.py`, `CONTRIBUTING.md:205-208` and `skills/code-review/orchestration.md:195-199` (read), and the grep above | none |
| the orchestrator's part of the pull request body | `Closes #1058` and nothing else | the issue number | none |

Not verified here: `frame/questions.md` M1, whether this pull request's own `pull_request` run of `tests` is green on every platform leg. Only GitHub starts that run, after the pull request opens. The orchestrator answers it by reading that run. The re-runs above were on macOS only.

Verdict: sealed
