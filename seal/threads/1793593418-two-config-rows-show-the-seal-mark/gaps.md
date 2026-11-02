# Closing memo: 1793593418-two-config-rows-show-the-seal-mark

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the work item's head. Phase 1 ran its phase-boundary set of 54 modules and `bin/seal layout --check tests`, and ran `ruff check` and `ruff format --check` on its own three changed Python files alone (`trail/phases/phase-1.md` *The phase-boundary run*, contract rule 2) | the orchestrator, by `seal gate` after the review rounds settle |
| The new cases of `tests/skills/test_pr_body.py` on Linux and Windows. They build git repositories and ran on macOS alone | the orchestrator, by the `tests` workflow on the branch before the broad run, or by CI when the pull request opens |
| Where the placement of this design's three rule changes lands. Phase 1 ran `rule_changes.py#parse` alone, with no error and no unread line; `apply_op` was not run | the orchestrator, by `seal chain-check` at the pull request |
| The mark in local mode, where no commit touches the work item and `follows` answers None only at HEAD. No case builds a local-mode root; `_seal_at_head` hands `follows` the same arguments in either mode | the proofer at review, reading `pr_body.py#_seal_at_head` against `chain_check.py#follows` |
| Whether a pull request page draws the mark line as the icon in a browser, at desktop and at phone width | a measurement, on the first pull request whose body `seal pr-body` from 0.28.0 or later writes after a seal (`frame/questions.md` Q1) |
| Whether the mark at width 128 looks as the owner wants | the owner (`frame/questions.md` Q2) |
| Phase 2's code at the tag, in the `seal` job of `.github/workflows/publish-release.yml`: the row read from the checkout's `seal/config.md`, the image attached and the two-cell header written under `yes`. The cases run `seal_release` with `gh` and the tree replaced by fixtures (`trail/phases/phase-2.md` *The cases, and how each was shown red*) | the orchestrator, reading the `seal` job's log and the published note of the 0.28.0 release |

## Not done

- No case runs `DRY_RUN=1` under a row other than `yes`. The dry run's only branch on the row is the draw, which the S6 cases already hold, and `release_seal.py`'s docstring states that the PNG is drawn only where the row turns the image on. A case for it would repeat S6 through a second door.
