# 1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis — review round 2

| Field | Value |
|---|---|
| Target SHA | 9ba76fad037a6464cd9c44d105863ff0c504f2d7 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #917 |
| Broad gate | not yet |
| Fixes checked by | no fixes to check |
| Fix range | none |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | no |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 2 of #911, the verifying round, target 9ba76fad: the diff of round 1's fixes, `ab821298..4d55d7a5`. The reviewer was asked whether 🟡 1, 🟡 2 and 🟡 3, recorded fixed at 44e0d652, are closed; to treat `boxes_alone` and the new case as a finding surface; and to judge the two things the smith left: `tests/test_review_axes.py:123`'s "five" comment, and the frame's Grounding row reading §1 the way 🟡 1 corrected.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 1's finding 1 is closed — the paragraph calls the second call a second wait and cites §1 only for its pricing | `skills/implement/orchestration.md:270` | confirmed | Read: `orchestration.md:271` *That is a second wait*; the cited half is `skills/implement/SKILL.md:203-206` *Asked before the work starts, it costs a reply* |
| 🟢 | round 1's finding 2 is closed — the assertion reads the sentence that carries the claim, and its comment quotes what `agents/framer.md` says | `tests/test_chain_hooks_hardening.py:1279` | confirmed | Executed: `mutation-check` removing *goes in one call of its own* from `orchestration.md:263` is red at `:1279` with the new message; `agents/framer.md:275` carries the quoted line; class re-swept with `git grep` |
| 🟢 | round 1's finding 3 is closed — the count is six | `skills/implement/orchestration.md:276` | confirmed | Read; the comment at `tests/test_review_axes.py:123` is true of #88, whose frame counted two presets beside three axes (`plan.md:101` of 1789518345 at `865a9807`) |
| 🟢 | The new units are correct and watch both directions | `tests/test_the_guard_asks_once_per_session.py:1495` | confirmed | Executed: green at the target; mutation A (boxes read as the press) red at `:1506`; mutation B (boxes read as taking it back) red at `:1514` |
| ⬜ 7 | The frame's Grounding row and Q1 still read §1 as making a second call one batch | `seal/specs/1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis/spec.md:20` | answered | corrected at fb273c69 — the frame's §1 Grounding row and Q1 (a) say a second call is a second wait, the trade #911 accepted, with a dated correction mark; Also `questions.md:17`; the reading round 1's finding 1 removed from `orchestration.md`; a record correction, outside `Needs a fix` |
| ⬜ 8 | The frame keeps *five options* and the bare `in one call` assertion as grounds that still hold | `seal/specs/1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis/spec.md:21` | answered | corrected at fb273c69 — the frame says two presets beside four boxes is six, and that the case now asserts *Question 1 goes in one call of its own*, with a dated correction mark; Also `spec.md:113-117`; round 1's findings 3 and 2, fixed in the tree and not in the frame; a record correction, outside `Needs a fix` |
| ⬜ 9 | Rule 3 names two shapes of the routing answer and not the two-call shape `per axis` now writes; `Enforced by:` omits the new case | `docs/worktree-guard-spec.md:306` | answered | corrected at fb273c69 — rule 3 says a boxes-only result answers no routing question and neither gives nor takes back the press; its `Enforced by:` names the new case; Behaviour right and pinned by the new case and S5b; the policy reader has to derive it from the `multiSelect` skip; `:529` lists S5's case only |

## Paste-ready fixes

no paste-ready fix in the report

## Executed probes

| What was run | Result |
|---|---|
| `bin/test tests/test_the_guard_asks_once_per_session.py tests/test_chain_hooks_hardening.py -q -k "boxes_asked_alone or questions_are_collected_before_the_work"` in the clone at `9ba76fad` | exit 0, 2 passed |
| `bin/test tests/test_docs_line_wrap.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_one_word_one_meaning.py tests/test_review_axes.py tests/test_the_rules_have_one_owner.py tests/test_a_moved_rule_leaves_its_definition.py -q` | exit 0, 319 passed |
| `mutation-check hooks/worktree_consent.py`, A: `if _routing_preset(result):` widened to any `multiSelect: true` question; tests `-k boxes_asked_alone` | red (exit 0 from the tool); the case failed at `:1506`; file restored |
| `mutation-check hooks/worktree_consent.py`, B: the take-back match widened to any `multiSelect: true` question; tests `-k boxes_asked_alone` | red; the case failed at `:1514`; file restored |
| `mutation-check skills/implement/orchestration.md`, *Question 1 goes in one call of its own, and two* to *Question 1 goes first, and two*; tests `-k questions_are_collected_before_the_work` | red; failed at `tests/test_chain_hooks_hardening.py:1279` with the new message; file restored |
| `evidence_check.py --ledger seal/ledger/1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis.md .` | exit 0; 81 ok, 0 drifted, 0 broken; records: 0 refused |
| `git status --short` in the clone after the probes | empty |
| Broad gate: the full suite, the repository-wide lint and the typecheck | not yet. Not run by this round. It is the sealer's, and with nothing open needing a fix it is now due: the next act is the sealer's spawn |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `skills/implement/orchestration.md:270` | round 1's 🟡 1 — fixed |
| round-1 | `tests/test_chain_hooks_hardening.py:1275` | round 1's 🟡 2 — fixed |
| round-1 | `skills/implement/orchestration.md:274` | round 1's 🟡 3 — fixed |
| round-1 | `skills/implement/orchestration.md:301` | round 1's ⬜ 4 — answered |
| round-1 | `docs/worktree-guard-spec.md:981` | round 1's ⬜ 5 — answered |
| round-1 | `seal/specs/1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis/overview.md` | round 1's ⬜ 6 — answered |
| round-1 | `hooks/worktree_consent.py#_routing_preset` | round 1's 🟢 — confirmed |
| round-1 | `skills/implement/orchestration.md`, `templates/claude-md-block.md`, `CLAUDE.md`, `skills/implement/SKILL.md`, `agents/framer.md` | round 1's 🟢 — confirmed |
| round-1 | `templates/claude-md-block.md:16` | round 1's ❓ — out of verified scope |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
