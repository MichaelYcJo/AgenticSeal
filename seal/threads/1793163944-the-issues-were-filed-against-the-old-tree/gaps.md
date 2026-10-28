# Overview: 1793163944-the-issues-were-filed-against-the-old-tree

## Why this work exists

The issues of 0.24.0 and 0.24.1 were filed against the tree before the rename and the reorganisation, so each is folded to the tree a framer will read, and the milestones state the order the read leaves.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| F2's `docs/` count | `frame/design.md` *F2*: "`docs/` 17"; the same command at `c1b79d40` counts 18 | 18, filed in #1110 with the command | the issue carries the measurement this phase ran (executed); `trail/phases/phase-1.md` names the three path lines the word-bound match counts |
| F3's assert counts | `frame/design.md` *F3*: "`tests/text` 193, `tests/behaviour` 340, `tests/skills` 270, `tests/github` 67, `tests/hooks` 36, `tests/evals` 15", with no command given; the command this phase ran counts 182, 308, 224, 57, 31, 13 | the re-run figures, filed in #1111 with their command | a count with no command cannot be re-run; the frame's own caveat that the figure bounds the class from above stays in the body |
| `frame/questions.md` Q1, #920's milestone | the spawn prompt: build on the default (a), move #920 to `release: 0.24.1` and comment the reason; phase 2 did both. The owner then answered (b) after the frame was committed, relayed in the orchestrator's message during phase 2: #920 stays in `release: 0.24.0`, no move comment, #1049 does not gain #920, and the 0.24.0 description keeps #920 in the small-fix group | (b): #920 put back in `release: 0.24.0` and the comment deleted, both exit 0; #1049's fold and both descriptions follow (b) | the owner's answer, as the orchestrator's message relays it; the orchestrator folded it into `frame/design.md` and `frame/questions.md` at `64dca63a`; acts in `trail/phases/phase-2.md` |
| #1056, who reads `LABEL_DESCRIPTION_LIMIT` | `frame/design.md` *#1056*: "only `tests/github/test_label_merged_on_release_branch.py:383` reads it"; `git grep` also finds `tests/github/test_tracker_labels.py:146`, through `.github/scripts/tracker_labels.py`'s `signal` | both readers, named in #1056 | executed, `git grep -n LABEL_DESCRIPTION_LIMIT` at `c1b79d40` |
| #1049, who imports `hooks/lib/cmdline.py` | `frame/design.md` *#1049*: `hooks/lib/tokens.py`, `hooks/lib/one_heredoc.py`, `hooks/worktree-guard.py` and `hooks/worktree_consent.py`, with `implementer-notice.py` replaced by that list; the tree: `hooks/worktree-guard.py:197`, `hooks/implementer-notice.py:47` and `hooks/lib/tokens.py:71` import it, `hooks/worktree_consent.py:94` imports `cmdline_base`, and `hooks/lib/one_heredoc.py` names it only in a docstring | the tree's three importers, the body's original list at its new paths | executed, `git grep -w cmdline -- hooks` with each import line read; `trail/phases/phase-3.md` |
| The order of `release: 0.24.0`, two changes | `frame/design.md` as committed at `cc314880`: F1 (#1109) in the small-fix group, and F3 (#1111) in parallel with #992 and #956. The owner changed both on 2026-10-28, after the frame was committed, relayed in the orchestrator's message during phase 3: #1109 leaves the small-fix group and is fixed directly in a no-work-item pull request before it, and #1111 runs after #956 | the owner's order: the small fixes are #1058, #913, #712 and #920, one sentence says #1109 was fixed directly before them without a work item, and step 4 is #992 and #956 in parallel, then #1111; #1109 is neither closed nor edited here | the owner's decision, as the orchestrator's message relays it; the orchestrator folds it into `frame/design.md`; applied in phase 4 |
| The mapping beyond the rows | each verdict row lists its instances; six bodies held an instance of a mapped class the row did not list: #913's `plan.md` of #871, #951's `arm-check`, #1042's "SpecSeal's", #992's "the warden's recall", #1055's `templates/seal-README.md`, #1058's `env.pop` line | each folded with its class | `frame/design.md` *The name mapping every fold applies*: "Each fold below applies these, where the issue's body uses the old form"; contract rule 12; each listed in `trail/phases/phase-2.md` |
| S5's "each once" against the frame's own text | `frame/design.md` S5: each description "names each open issue of its milestone once and no closed issue or issue of another milestone"; the frame's quoted text names #1040 three times and #920, #951 and #956 twice in 0.24.0's, and #1044 (closed) and #1103 (a merged pull request) in 0.24.1's | the quoted text, as the plan's Delivers cell and *Technical context* say to write it | `frame/plan.md` *Technical context*: "A description is the quoted text of *The two descriptions*"; each repeat is an earlier issue named as a later step's reason; `trail/phases/phase-4.md` |

## Not verified

| Item | Who must answer |
|---|---|
| The broad gate over this branch; no phase ran a test, because no tree file outside this directory changes | the orchestrator |
| closed `frame/questions.md` Q1, built on its default (a), moving #920 to `release: 0.24.1` | answered (b) by the owner, relayed by the orchestrator during phase 2; #920 put back in `release: 0.24.0` |
| Milestone 65's sentence "#1109 was fixed directly, before the small fixes, without a work item" holds only once #1109 is closed; it is open at phase 4's write | the orchestrator, whose no-work-item pull request into `release/v0.24.0` closes it |

## Not done

nothing

## Fed back into the spec

none
