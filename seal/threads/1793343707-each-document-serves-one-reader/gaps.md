# Closing memo: 1793343707-each-document-serves-one-reader

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check` on this branch | the orchestrator, through `seal gate` |
| Phase 3: the records-only exemption as `README.md:207-213`, `README.ko.md:201-206`, the acts row *Orchestrator: the run ends with a verifying round* (in `skills/implement/acts.md` since phase 4) and the drain row at `skills/implement/SKILL.md:511` state it, with no case behind any of the four | the proofer at review |
| Phase 5: `skills/code-review/scripts/pr_body.py#_composed` refuses a copied line equal to `<details>` or `</details>` outside a fence, as `frame/design.md` *`pr_body.py`* states, and no other line. A copied `</details>` inside a sentence, an indented one, `<details open>` and `</DETAILS>` are not refused, and whether GitHub ends or nests the fold at any of them is not known here (`trail/phases/phase-5.md`) | the orchestrator, reading the first body this change writes on GitHub |
| Phase 6: GitHub's rendering of the pull request body's fold, that the `<details>` block opens closed and that the copied Markdown after the blank line under `<summary>` renders as Markdown inside it. It is the owner's statement, and no run here can render a pull request (`frame/questions.md`, its last head item) | the orchestrator, reading the first body this change writes on GitHub |
| Phase 6: the behaviour suite (`evals/scripts/noninferiority.py run` at the merge base and at HEAD, then `compare`) over `agents/framer.md`, `agents/crafter.md`, `agents/proofer.md` and `agents/sealer.md`, not run on `frame/questions.md` Q1's default; the proofer's stage 1 reading of each changed sentence stands in for it | the owner, at the pull request (`frame/questions.md` Q1) |
| closed Phase 4: `docs/the-pact.md:59-60` cites `skills/implement/orchestration.md` *A work item that commits in more than one repository*, and no rule change of `frame/design.md` moves it to `skills/implement/multi-repository.md`; the citation resolves to the one pointer sentence left in `orchestration.md` (`trail/phases/phase-4.md`) | closed by the orchestrator at the fold after phase 4: `frame/design.md` `## Rule changes` gains the `docs/the-pact.md` change to `skills/implement/multi-repository.md`, which the settle writes; the pointer sentence carries the citation until then |

## Not done

Phase 3 left six shipped files naming `CONTRIBUTING.md`, which row 3's
`git grep -l 'CONTRIBUTING' agents skills templates hooks` was to show
empty: `hooks/lib/config.py:410`, `hooks/lib/launch.py:55`,
`hooks/mode-gate.py:49`, `hooks/version-check.py:24`,
`skills/verify/scripts/session_cost.py:3103` and
`skills/verify/scripts/test_layout.py:15` and `:58`. The design took
`agents/proofer.md:67` for the one instance, and the spawn named that file
alone. `hooks/lib/launch.py:55` is a refusal a person reads in their own
repository, so its change also needs a pin (`trail/phases/phase-3.md`).
After phase 3 the orchestrator folded the rest into the frame: phase 4
took `hooks/lib/launch.py#REFUSAL` and its pin, and the five others are
comments and docstrings, whose reader is a contributor, which the
direction rule in `frame/design.md` `## Rule changes` lets cite
`CONTRIBUTING.md`. They stand.

The change does not remove more lines than it adds outside
`seal/threads/`, which `frame/design.md` *Scope* item 11 and scenario S10
ask. `git diff --shortstat fba13ab2...HEAD -- . ':(exclude)seal/threads'`
gives `59 files changed, 1128 insertions(+), 988 deletions(-)` at the
fragment's commit: 140 more lines added than removed
(`trail/phases/phase-6.md`). The shipped files outside `tests/` remove 80
more lines than they add, and `tests/` adds 220 more than it removes. The
change was neither padded nor trimmed to meet the count, as the spawn for
phase 6 directed.
