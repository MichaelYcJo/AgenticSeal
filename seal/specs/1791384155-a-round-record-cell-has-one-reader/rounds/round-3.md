# 1791384155-a-round-record-cell-has-one-reader — review round 3

| Field | Value |
|---|---|
| Target SHA | ec02e1562543d8dcd2f10a84ea7873af204617fd |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | 890 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are not yet written |
| Fix range | none — the fixes are not yet written |
| Contract changes | none — the fixes are not yet written |
| New units | none — the fixes are not yet written |
| Fix of a fix | no |
| Needs a fix | no |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

This round verified round 2's fixes, ff88f31d..07449c19, plus the fix table and the close at ec02e156, and it ends the run. The spawn named four things to judge, in order. First, whether 🔴 1 is closed: the paste ratchet counts the docs pair at its baseline of 31, docs/review-chain-spec.md stays at or under 1,000 lines, and the module that failed on three CI legs passes. Second, whether each of the three notices for 🟡 2 reads true both for a draft and for a run with no observed pull request, each pinned in both states, and whether any fourth sentence still asserts a draft. Third, whether the answers to ⬜ 3–5 hold. Fourth, the fix range as a finding surface for unknown read as ready, or ready read as unknown. Probes were to run in a scratch repository. The facts arrived labelled. Read: the owner's direction that an unobserved state reads as unknown. Read: the 33 release-branch drifted rows that #836 clears.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 2's blocking finding 1 is closed — the review-chain-spec sentence no longer repeats the round-record-spec row | `docs/review-chain-spec.md:655` | confirmed | executed: the module's own `shared_counts` gives 31 at 6b9f311e, 07449c19 and ec02e156 (33 at ff88f31d); `over_baseline` over the tree is empty; the file is 999 lines; `bin/test` on the module and the three other touched modules gives 301 passed, exit 0. read: CI at ec02e156 still pending |
| 🟢 | round 2's finding 2 is closed — the three notices read true for a draft and for an unseen run | `skills/code-review/scripts/chain_check.py:5955` | confirmed | executed: with `chain_check.py` from ff88f31d the new pins give 4 failed, 1 passed (the `[ready]` case, which asserts no notice). read: only three of the six places that branch on `strict` print when not strict, and `broad_gate.py` holds no draft sentence |
| 🟢 | round 2's note 3 stands as answered — the unseen line's CI clause is Q1's | `skills/code-review/scripts/chain_check.py:1335` | confirmed | read: `questions.md` Q1 and `templates/hygiene.yml` lines 12-22; the same Q1 covers the re-arm half of the three notices on a route with no pull request |
| 🟢 | round 2's note 4 stands as answered — the payload test is one reading | `skills/code-review/scripts/chain_check.py:1341` | confirmed | read: `event_payload_present` and `pull_request_state` test `GITHUB_EVENT_PATH` the same way |
| 🟢 | round 2's note 5 stands as answered — no cell has the shape | `skills/code-review/scripts/chain_check.py:1947` | confirmed | read: round 2 executed it over every cell in the tree; nothing in the fix range writes a deferral cell |
| ⬜ 1 | The docs and docstrings describing the three non-strict arms still name the draft alone, though an unseen run is excused the same way | `skills/code-review/scripts/chain_check.py:5033` | open | read: also `skills/code-review/orchestration.md:238`, `docs/review-chain-spec.md` §*What a draft is excused, and what it is not*, `chain_check.py:5455` and `chain_check.py:166`; none is false, each omits the unseen state; `docs/review-chain-spec.md` is at 999 lines |
| ⬜ 2 | Round 2's fix table says each notice is pinned in both states, and the empty-`rounds/` wording is asserted in the unseen run only | `tests/test_chain_check_at_the_pull_request.py:246` | open | read: the draft case asserts the notice prints and names `ready_for_review`; executed: one shared literal, so the wording revert fails the unseen case |

## Paste-ready fixes

no paste-ready fix in the report

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` on `tests/test_no_passage_is_pasted_into_a_second_file.py`, `tests/test_a_note_closes_once_at_the_runs_end.py`, `tests/test_chain_check_at_the_pull_request.py` and `tests/test_the_last_rounds_fixes_are_checked.py`, in the scratch clone at ec02e156 | 301 passed, exit 0 |
| a probe calling the module's `shared_counts` on the docs pair at b10835ff, ff88f31d, 6b9f311e, 07449c19 and ec02e156, and `over_baseline` on the tree | 31, 33, 31, 31, 31; 999 lines each; `over_baseline` empty |
| `chain_check.py` restored from ff88f31d, then the open-note, unseen-run and `Pass`-beside-`nobody` cases | 4 failed, 1 passed (`[ready]`); restored to the target afterwards |
| `bin/evidence-check --strict --ledger` on this item's fragment, the 1791384154 and 1791384160 fragments, and `seal/releases/0.9.5.md` | 194 ok exit 0; 1 drifted exit 2; 3 drifted exit 2, all on paths this branch does not touch; 66 ok exit 0 |
| `bin/survivor-check --range ff88f31d..07449c19`, with and without this item's `survivors.md` | exit 0 with it (one exempt place); exit 1 without it, naming `seal/releases/0.9.5.md:31` |
| `gh pr checks 890` | read: every pytest leg pending at ec02e156 (CI's run, not this round's) |
| the full suite, the repository-wide lint and the typecheck (the broad gate) | not yet — the sealer's, after the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `skills/code-review/scripts/round_record.py:2735` | round 1's 🟡 1 — fixed |
| round-1 | `tests/conftest.py:560` | round 1's 🟡 2 — fixed |
| round-1 | `skills/verify/scripts/broad_gate.py:2938` | round 1's 🟡 3 — fixed |
| round-1 | `skills/code-review/scripts/chain_check.py:1891` | round 1's 🟡 4 — fixed |
| round-1 | `skills/code-review/scripts/chain_check.py:1325` | round 1's ⬜ 5 — answered |
| round-1 | `skills/code-review/scripts/chain_check.py:4441` | round 1's ⬜ 6 — answered |
| round-1 | `skills/code-review/scripts/chain_check.py:5707` | round 1's 🟢 — confirmed |
| round-1 | `skills/code-review/scripts/chain_check.py:4448` | round 1's 🟢 — confirmed |
| round-1 | `skills/code-review/scripts/chain_check.py:1330` | round 1's 🟢 — confirmed |
| round-1 | `skills/code-review/scripts/chain_check.py:1255` | round 1's ❓ — out of verified scope |
| round-2 | `docs/review-chain-spec.md:656` | round 2's 🔴 1 — fixed |
| round-2 | `skills/code-review/scripts/chain_check.py:5956` | round 2's 🟡 2 — fixed |
| round-2 | `skills/code-review/scripts/chain_check.py:1335` | round 2's ⬜ 3 — answered |
| round-2 | `skills/code-review/scripts/chain_check.py:1341` | round 2's ⬜ 4 — answered |
| round-2 | `skills/code-review/scripts/chain_check.py:1947` | round 2's ⬜ 5 — answered |
| round-2 | `skills/code-review/scripts/chain_check.py:5737` | round 2's 🟢 — confirmed |
| round-2 | `tests/conftest.py:559` | round 2's 🟢 — confirmed |
| round-2 | `skills/verify/scripts/broad_gate.py:2942` | round 2's 🟢 — confirmed |
| round-2 | `skills/code-review/scripts/chain_check.py:1943` | round 2's 🟢 — confirmed |
| round-2 | `skills/code-review/scripts/chain_check.py:1302` | round 2's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
