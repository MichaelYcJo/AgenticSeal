# Overview: 1792935671-the-routing-check-moves-to-the-sessions-tools

## Why this work exists

The routing check governed the session but ran inside git, so it reached a person's own terminal commits and a hooks slot other tools need; it now runs at the session's edit tools and at the pull request, and nothing is installed into git.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Which commits the trailer arm reads | `spec.md` *Rule changes*, *At the pull request*: "The commits are the pull request's own, merges left out". `chain_check.py#routing_trailers` also leaves out a squash GitHub committed | Left out | A release pull request into `main` carries other pull requests' squashes, whose bodies keep the trailers of the commits they squashed. Read as its own, each would name a work item no declaration it judges names, and every release pull request would fail. The squash rule is `carried_by`'s, which already leaves such a declaration to the pull request that carried it (`phases/phase-3.md`) |
| Which history read skips a recorded refusal | `spec.md` *Rule changes*, *The stamp*: "`sealed_before` skips a `sealed` this clone recorded refusing". `post-commit`'s `_queue_one` asks without the record | Only the write-time writer hands the clone and the work item | With the skip on the `post-commit` path, `tests/test_commitgate.py::Test_post_commit::test_refuses_to_draw_again_over_a_refused_row_of_a_drawn_seal` drew a work item twice after a rebase (executed, `phases/phase-4.md`). `post-commit` goes in phase 6 |
| The caseless test files the frame removes | `spec.md` *Removes*: `tests/test_a_commit_behind_a_reserved_word_is_judged.py`, `tests/test_a_commit_behind_a_wrapper_or_in_a_substitution_is_judged.py`, `tests/test_an_automation_run_meets_no_commit_prompt.py`, `tests/test_gate_judges_the_repo_it_commits_to.py` and `tests/test_the_waiver_can_be_typed.py` go. Each holds no case and stays | Kept, with no case | `docs/the-commit-gate-inside-git.md`, `docs/commit-review-gate-spec.md` and `docs/the-review-and-parity-arms.md` name each on a `check:` line, and the policy root changes only at the settle that applies this spec. `rules --check` reads every check line in the tree as it stands (`tests/test_rules.py::Test_main::test_every_check_line_in_the_tree_holds`), so a removed file fails it until then. The settle removes them with the documents |
| Markers the retired documents name | `spec.md` *Removes*: "a marker a kept rule names stays carried by a kept test". The retired documents name markers whose only carriers were removed: `review-arm-asks`, `judged-inside-the-commit`, `text-reading-stands-aside` | Each is carried by a class with no case in `tests/test_the_retired_rules_await_their_settle.py` | The same reason as the row above, for markers: `rules --check` refuses a marker no test carries. The frame named only the kept rules; the retired documents stand in the tree until the settle. The settle removes the file with them |
| `tests/e2e/commit/test_commit_flow.py` leaves in phase 5 | `plan.md` *Phases*: phase 6 removes the git hooks and their tests | Removed in phase 5 | 65 of its cases ran the text reading this phase removes, and the rest test git hooks phase 6 removes; their units keep their cases in `tests/test_commitgate.py` until then (`phases/phase-5.md`) |

## Not verified

| Item | Who must answer |
|---|---|
| Whether the `PreToolUse` edit hook fires for a subagent's `Edit` and its deny stops the edit (`questions.md` Q3, `spec.md` S9) | the owner, in a live session after an installed release carries the hook |
| The full suite, the repository-wide lint and format check, and the typecheck at the branch head | the orchestrator's broad run |

## Not done

The two operations of earlier unsettled specs that no longer place, `seal/specs/1792619408-an-automation-run-stops-at-the-parity-arm/spec.md` line 192 and `seal/specs/1792627930-the-section-sign-is-still-syntax/spec.md` line 279, were left: their `from` texts are older than `docs/the-review-record.md`, and replayed spec by spec, as `settle` replays, every later spec waits on the first, this one included (`phases/phase-1.md`). Rewriting another work item's frame is that work item's or the settle's, not this one's.

The rule-9 departure of phase 4 is recorded here because no other file holds it: to see the new stamp cases red, a copy of HEAD's `skills/verify/scripts/seal_stamp.py`, renamed in one place, was written over the new file by a short Python script through the shell, and the new file was copied back and compared byte for byte with `cmp` (`phases/phase-4.md`).

## Fed back into the spec

none
