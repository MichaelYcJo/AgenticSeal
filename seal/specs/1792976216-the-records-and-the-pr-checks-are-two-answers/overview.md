# Overview: 1792976216-the-records-and-the-pr-checks-are-two-answers

## Why this work exists

Choosing shared mode installed a workflow that judged every teammate's pull
request, so first setup now asks where the records live and whether CI checks
pull requests as two answers, `seal pr-checks` installs and removes the
workflow, and every step of that workflow passes a pull request that declares
nothing.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The flow case's skips on a machine that cannot run the template | `questions.md` Q2's default: the case skips through `tests/conftest.py#symlink_or_skip` where `$RUNNER_TEMP/specseal` cannot be made to resolve to the tree. The code also skips where `bash -c 'command -v python3'` fails | both skips | Every step the template runs names `python3`, and the template pins `ubuntu-latest`, which always has one. A machine without it cannot run the steps the case exists to run (`phases/phase-1.md`) |
| The line a switch to shared prints where another party's file is at the workflow's path | `spec.md` *In* item 4: "After a switch to shared, where no such file is there, it prints one line naming `seal pr-checks install`." The code prints nothing where a file this plugin did not write stands there | print nothing there | spec silent on that state. `seal pr-checks install` refuses there, so naming it would send a person to a refusal (`phases/phase-2.md`) |
| The switch's dirty-tree refusal | The refusal read *the paths this would stage*. The code reads *the path this would stage* | one path | spec silent. The switch stages `seal/` only after `spec.md` *Removes* took the workflow path out of the guard (`phases/phase-2.md`) |

## Not verified

| Item | Who must answer |
|---|---|
| closed whether the flow cases of `tests/e2e/teammate/test_teammate_flow.py` run or skip on the Windows legs of `.github/workflows/test.yml` (`questions.md` Q2) | the `tests` workflow run 40264357704 on the branch at `895db45e` passed every leg, and the flow cases ran on `windows-latest` with 3.37s and 2.83s in its durations report (`questions.md` Q2, answered (a)) |
| closed the full suite, the repository-wide lint and format check, and the typecheck at the branch head | `broad-gate.md` records the run at `80f60abd` against `02ee12de`, after rounds 5 to 9; its printed report read BROAD GATE PASSED, ruff check and format clean, the suite 6,564 passed and 14 skipped, chain-check exit 0. The branch's `tests` workflow run 40271486400 at `f8f65ea4` passed every leg, Windows included. The repository has no typecheck to run (#951 adds one) |
| closed Whether the settle applies this spec in merge order, behind the specs the merge-order replay refused for reasons outside this branch. Phase 3 replayed this spec alone onto `docs/` at `02ee12de` | answered by #1033's redesign, merged as #1035, and this settle's dry run at 434334d9: every operation of this spec is listed in its section's group in merge order, with no spec to read whole and no unordered pair (executed, `settle.py --released-at origin/release/v0.22.4`) |

## Not done

A gate at the pull request that applies each judged spec's `## Rule changes`
and runs the documents' own cases over the result was not built. Rounds 1, 2
and 3 each found a case green on the branch and red at the settle, and S8
carries that class here as a probe that phase 3 and the verifying round run.
A gate over every unsettled spec would go red today on the three specs the
merge-order replay already refuses, and it owes the argument `CONTRIBUTING.md`
*What a change to a gate must carry* asks for. `questions.md` Q4 holds the
choice, and its default (a), no new gate, is what was built.

S9's five mutants of the chain step's no-root test were run once and are not
kept as a check. What stays is one case per answer in `tests/test_chain_check.py`
`Test_retired` and the module's other cases, which turn red when a later edit
drops an answer.

No version comparison was added for a workflow pinned to a release newer than
the installed one, and no guard for a `seal/` that is a symbolic link out of
the tree. `spec.md` *Out* states both as limits: the one-issue flow does not
produce either shape.

## Fed back into the spec

none
