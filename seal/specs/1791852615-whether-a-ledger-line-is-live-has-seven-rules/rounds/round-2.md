# 1791852615-whether-a-ledger-line-is-live-has-seven-rules — review round 2

| Field | Value |
|---|---|
| Target SHA | 65385bd1edcc280e108e32457d4e9960795ee79f |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #918 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are written and no round has opened them |
| Fix range | `5eeb24b8eee864277e780c44e6f4c19acaf71529..259b82ee0cf591e396a9f9c8a71a026d5007b0d1`, 1 commit |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 6: the excusing bullet attributes `routing.md` rows to `hidden_lines`, and its new "one place" sentence is false for a routing row below a fence nobody closed. |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Round 2 of #872, the verifying round, target 65385bd1: the diff of round 1's fixes, `9b5239c6..e224390f`. The reviewer was asked whether 🟡 1, 🟡 2 and 🟡 3, recorded fixed at e224390f, are closed; to check the other five readers' cells on the two new shapes, which rest on round 1's measurements rather than on mutations; and to check the nine re-stamped rows, C2 among them.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 1's 🟡 1 is closed — the excusing headline names the declaring reader's exception, and the protection sentence is scoped away from the `seal/config.md` row below an unclosed comment opener | `docs/the-evidence-ledger.md:633` | confirmed | read: lines 633 to 646; executed: the statement test passes at `65385bd1`; the new sentence at `:642` opens 🟡 6 on a different row |
| 🟢 | round 1's 🟡 2 is closed — the three partings are stated, the two added shapes are in the table, and the overview says three | `docs/the-evidence-ledger.md:625` | confirmed | executed: all seven readers asked on both added shapes, every cell equal to the table; the five readers' cells resting on round 1's measurement are right and match their docstrings |
| 🟢 | round 1's 🟡 3 is closed — the four holding readers declare `unknown refused` | `skills/evidence-check/scripts/evidence_check.py:370` | confirmed | read: `:370`, `:5591`, `rider_check.py:238`, `settle.py:590` and `docs/the-reader-registry.md:31` to `:35`; W2 says `refused` |
| 🟢 | the nine re-stamped rows hold, C2 included, and no moved anchor was missed | `seal/ledger/1791852615-whether-a-ledger-line-is-live-has-seven-rules.md` | confirmed | executed: `bin/evidence-check --strict .` 0 drifted, 0 broken; `bin/fold-check` 0 over the ceiling, which is C2's claim; `git grep` finds exactly A4, P2-1, P2-3, P4-1, P4-2, R5 and C2 anchored to the three moved anchors |
| 🟡 6 | the excusing bullet attributes `routing.md` rows to `hidden_lines` and calls a row below an unclosed comment opener the one place a hidden line declares; `routing.md` is read by `hooks/routing.py#shown`, which declares a row below a fence nobody closed; `hidden_lines`' `Reads:` line names `routing.md`, which no caller hands it | `docs/the-evidence-ledger.md:642` | **fixed** `259b82ee` | fixed at 259b82ee; executed: the probe, routing row below an unclosed fence declared by `table_rows` and hidden by `hidden_lines`; read: `hooks/routing.py:127` to `:149`, `hooks/config.py:176`, `:189`, `:247`, `broad_gate.py#hidden_row_at` |
| ⬜ 7 | the frame says `routing.py#shown` reads `hidden_lines` through `unfenced`, and gives `hidden_lines` `routing.md` lines as input | `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/plan.md:58` | open | read: `plan.md:58`, `spec.md:151`, `hooks/routing.py:127` to `:149` |
| ⬜ 8 | the changelog fragment says `hooks/config.py` is the one reader of its kind that reads a row below an unclosed comment opener; the routing reader does too | `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/changelog.md:14` | open | executed: 🟡 6's probe, second row |
| ⬜ 9 | the holding bullet says a renderer "shows" comment text; it shows none | `docs/the-evidence-ledger.md:631` | open | read: the bullet and the rider check's `quoted_lines` docstring; the behaviour stated is right |

## Paste-ready fixes

```markdown
  `hooks/config.py#hidden_lines`, which reads `seal/config.md`, keeps,
  wherever its walk is unsure, the fence-only reading it gave before #667:
  a row below a fence nobody closed declares nothing, and a row below a
  comment opener nobody closed still declares, because that reading never
  hid one and work item 1790645290 was bound to miss no row the older
  reading saw. `hooks/routing.py#shown`, which reads a `routing.md`, keeps
  the reading it gave before #667 the same way, and that reading hid
  nothing: a row below a fence or a comment opener nobody closed still
  declares there. Those rows are the places a line nobody wrote live
  declares something; at every other fence or comment, what this protects
  is that nothing is excused or declared by a line nobody wrote live. The
  wrong answer is a fold reported as a deletion at exit 1, a fragment the
  sweep keeps, a hook that says nothing, or a gate that asks.
```
```python
    Reads: guess — the lines of `seal/config.md`, through `hooks/blocks.py#walk`; unknown mixed
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` on `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`, `tests/test_docs_line_wrap.py` and `tests/test_a_folded_statement_names_what_enforces_it.py` with `-q` and `SPECSEAL_CASE_CEILING_S=600`, in the clone at `65385bd1` | exit 0, 145 passed |
| `bin/fold-check --root .` in the clone | exit 0: 186 statements in 19 documents, 0 over the 1000-line ceiling; `docs/the-evidence-ledger.md` is 708 lines |
| `bin/evidence-check --strict .` in the clone | exit 0: 8474 ok, 0 drifted, 0 broken, 0 malformed |
| `git diff --stat 321e9de1 HEAD -- seal/releases seal/ledger.md` in the clone | empty, exit 0 |
| one test_tmp probe module in the clone's `tests/`, run once through `bin/test`, then deleted: the seven readers through the table module's adapters on the two added shapes and on two indented-code shapes | the two added shapes match the table in every cell; on a four-space indented row after a blank line all seven read the row |
| one test_tmp probe module in the clone's `tests/`, run once through `bin/test`, then deleted: `hooks/routing.py#table_rows` and `hooks/config.py#hidden_lines` on one routing row in four shapes | below an unclosed fence: declared, hidden. Below an unclosed comment opener: declared, not hidden. Inside a closed fence: not declared, hidden. Four-space indented: declared, not hidden |
| the broad gate: full suite, repository lint, typecheck | not yet. It belongs to the sealer, once the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `docs/the-evidence-ledger.md:629` | round 1's 🟡 1 — fixed |
| round-1 | `docs/the-evidence-ledger.md:625` | round 1's 🟡 2 — fixed |
| round-1 | `skills/evidence-check/scripts/evidence_check.py:370` | round 1's 🟡 3 — fixed |
| round-1 | `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py:222` | round 1's ⬜ 4 — open |
| round-1 | `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/overview.md:31` | round 1's ⬜ 5 — open |
| round-1 | `tests/undeclared_readers.txt` | round 1's 🟢 — confirmed |
| round-1 | `skills/verify/scripts/unverified_check.py:744` | round 1's 🟢 — confirmed |
| round-1 | `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py:79` | round 1's 🟢 — confirmed |
| round-1 | `seal/ledger/1791852615-whether-a-ledger-line-is-live-has-seven-rules.md` | round 1's 🟢 — confirmed |
| round-1 | `seal/releases` | round 1's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
