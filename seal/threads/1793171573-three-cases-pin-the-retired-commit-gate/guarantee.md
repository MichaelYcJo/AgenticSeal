# Guarantee: 1793171573-three-cases-pin-the-retired-commit-gate

| Field | Value |
|---|---|
| Target SHA | da5b7ed4 against c825fd2c |
| Broad gate | 7a39f2e8 against c825fd2c |

The base `release/v0.24.0` resolved through `release/v0.24.0@{upstream}` to
`c825fd2c` (executed). The gate's commit `7a39f2e8` is an ancestor of HEAD,
and `git log --no-merges --name-only 7a39f2e8..HEAD ^c825fd2c` lists one
commit, `da5b7ed4`, touching only
`seal/threads/1793171573-three-cases-pin-the-retired-commit-gate/trail/gate.md`
(executed). `bin/seal pr-body seal/threads/1793171573-three-cases-pin-the-retired-commit-gate --body <the body file> --check`
exited 0, saying the part above `## Not from the records` is the records'
text (executed).

No claim in `trail/phases/phase-1.md` is a `seen red`: the phase removes
cases and adds none, so no case was re-run against the code before the
change. Every run below was made in a clone of the branch at `da5b7ed4`,
under the scratchpad, on git 2.50.1, and the clone was removed afterwards.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The three cases stood at `:176`, `:274` and `:318` with their markers at `:273` and `:317`, and `.test_durations` priced them at `:874`, `:876` and `:880` | `trail/phases/phase-1.md:24` | `git show 27a6bb6d:tests/behaviour/test_the_hook_surface_git_offers.py` and `git show 27a6bb6d:.test_durations`, each searched for the three names and `mark.rule` | holds: every line number matches (executed) |
| The three cases, both markers, `AUTHOR_DATE_LOG` and the three `.test_durations` entries are gone, and nothing outside the records cites them | issue #1039 *Done when*, `trail/phases/phase-1.md:31` and `:37` | `git grep -n -E` over the three case names, both markers and `AUTHOR_DATE_LOG`, at `6e322bb7` and at `HEAD` | holds: at `6e322bb7` the search finds the module and `.test_durations`, so the check can fail; at `HEAD` it finds only this work item's records and `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/frame/design.md:172`, another work item's record of the issue text (executed) |
| No import is left unused, and the module is formatted | `trail/phases/phase-1.md:40` | `uvx ruff check tests/behaviour/test_the_hook_surface_git_offers.py` and `uvx ruff format --check` on the same file | holds: exit 0 both (executed) |
| The seven remaining cases pass | `trail/rounds/round-2.md`, *Probes* | `bin/test tests/behaviour/test_the_hook_surface_git_offers.py -q -p no:xdist -rs` | holds: exit 0, 7 passed, none skipped, git 2.50.1 (executed) |
| `seal rules --check` passes, and both `check:` lines still name the module | issue #1039 *Done when* | `bin/seal rules --check`, and `grep -n test_the_hook_surface_git_offers docs/worktree-guard-spec.md` | holds: exit 0, all 266 check lines in 55 rule files hold; the module is named at `docs/worktree-guard-spec.md:360` and `:587` (executed) |
| `.test_durations` still prices the suite after the three entries left | `gaps.md:22` | `bin/test tests -q -k test_the_durations_file_prices_the_suite` | holds: exit 0, 1 passed (executed). The case tolerates a stale share up to `STALE_SHARE = 0.05`, so three stale entries would not have turned it red; the removal itself rests on the `git grep` row above (read) |
| The three cases cost 16.3 s of the serial suite | `gaps.md:10` | the three removed values from the diff of `.test_durations` summed in `python3` | holds: 16.30 s (executed) |
| `changelog/0.22.4.md` has no entry for #1028 | `gaps.md:29` | `grep -c 1028 changelog/0.22.4.md` | holds: 0 (executed) |
| The docstring states what the seven remaining cases pin for `docs/worktree-guard-spec.md` | issue #1039 *Done when*, `trail/phases/phase-1.md:41` | `git diff c825fd2c...HEAD -- tests/` | holds: the docstring names *Which tree* for the three switch cases and *Decided before git runs* with the creation half of *Which tree* for the four creation cases, and the switch case's failure message no longer names #692's design (read) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | Issue #1039: delete three cases and their three `.test_durations` entries, rewrite the docstring to state what the seven remaining cases pin, keep `seal rules --check` passing and both `check:` lines naming the module; the seven cases are out of scope | the build, the last round, and every row above | none |
| the build | The diff removes the three cases, the two markers, `AUTHOR_DATE_LOG` and the three entries, rewrites the docstring and one assertion message of a remaining case; `gaps.md` and `trail/phases/phase-1.md` describe that | the spec: the helper served only the removed cases, and the message change rewords text without changing what the case asserts; the tree, by the rows above | none |
| the last round | `trail/rounds/round-2.md` confirms round 1's three findings closed in `f8703927` and opens nothing | the tree: the docstring and message it quotes stand in the diff, and its probes re-ran with the same results | none |
| the changelog | No `changelog.md`; `gaps.md` *Not done* says nothing a plugin user installs, runs or reads changes | `docs/the-record-layout.md:57-58`, which owes a fragment nothing where no release note states the change; the diff touches only `.test_durations`, one test module and this work item's records | none |
| the orchestrator's part of the pull request body | `Closes #1039` | the spec: issue #1039 is open and is the issue this work item builds | none |

Not verified: the seven cases on git 2.34.1, 2.39.5 and 2.43.0. This audit
ran them on 2.50.1 only; the orchestrator answers from the pull request's CI
legs.

Verdict: sealed
