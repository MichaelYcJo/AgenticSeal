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

## Not done

- `frame/design.md`'s `## Rule changes` add to `docs/the-review-record.md` *The guarantee* does not say that a base the clone cannot resolve writes no mark and is named (`trail/phases/phase-1.md` *Decision: a base that does not resolve writes no mark, and is named*). The design is the framer's to write, and the sentence it adds holds as written, so the departure is recorded in the phase record and left for the orchestrator to fold into the frame or leave.
