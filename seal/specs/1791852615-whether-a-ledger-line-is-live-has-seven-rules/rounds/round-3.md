# 1791852615-whether-a-ledger-line-is-live-has-seven-rules — review round 3

| Field | Value |
|---|---|
| Target SHA | f902093455c6e8c06b782e85ee4708c6da1a700e |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #918 |
| Broad gate | not yet |
| Fixes checked by | no fixes to check |
| Fix range | `f902093455c6e8c06b782e85ee4708c6da1a700e..f902093455c6e8c06b782e85ee4708c6da1a700e`, 0 commits |
| Contract changes | none |
| New units | none |
| Fix of a fix | first — 🟡 11 at hooks/config.py#hidden_lines, a unit round-2's fixes changed |
| Needs a fix | yes — 🟡 10, the routing sentence's comment half has no case and the sentence over-reaches past a fence that closes; 🟡 11, the `hidden_lines` `Reads:` line names one of its four inputs. |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 3 of #872, the verifying round after the run's one reopening, target f9020934: the diff of round 2's fix, `5eeb24b8..259b82ee`. The reviewer was asked whether 🟡 6, recorded fixed at 259b82ee, is closed, and to check the new text against `hooks/routing.py#shown` and the case the smith cited as its pin. The run ends at this record; its two open findings take the ladder (#922, in milestone 0.21.1, fixed in this release after this branch merges).

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 2's finding 6 is closed — the bullet credits `seal/config.md` to `hidden_lines` and `routing.md` to `hooks/routing.py#shown`, a routing row below a fence nobody closed is stated to declare, and the `Reads:` line no longer names `routing.md` | `docs/the-evidence-ledger.md:643` | confirmed | executed: the probe, `shown` shows a routing row below an unclosed fence and below an unclosed comment opener; read: `hooks/routing.py:127` to `:147`, `hooks/config.py:176`, `:189`, `:247`; R3 pins the fence half |
| 🟢 | the three re-stamped rows hold — P3-1, C2 and W2 — and no other row anchors the two moved anchors | `seal/ledger/1791852615-whether-a-ledger-line-is-live-has-seven-rules.md` | confirmed | executed: `bin/evidence-check --strict .` 0 drifted, 0 broken; `bin/fold-check` 0 over the ceiling; `git grep` over `seal/` finds exactly P3-1, C2 and W2 |
| 🟡 10 | the routing sentence's comment half is held by no case, and the cited case passes with the routing reader hiding that row; read literally, "a row below a fence or a comment opener nobody closed still declares" is false for a row a fence that closes holds (R8), for both readers | `docs/the-evidence-ledger.md:645` | deferred #922 | #922 — the run ends at this record (the reopening bound); #922 is in milestone 0.21.1 and is fixed after this branch merges; executed: a renderer-exact mutation of `shown` hid the row and the three routing modules passed, 225 cases; the proposed case was red on it and green at `f9020934`; R8 pins the routing reader hiding a fenced row below an unclosed opener. Text this run wrote at `259b82ee`, so rung 1: the branch's diff |
| 🟡 11 | `hidden_lines`' `Reads:` line names `seal/config.md` alone; through `unfenced` it is also handed `seal/pact.md`, `seal/pact-changes/` records and the machine-local pact path map; the fix commit says it names only what its callers hand it | `hooks/config.py:189` | deferred #922 | #922 — the run ends at this record (the reopening bound); #922 is in milestone 0.21.1 and is fixed after this branch merges; read: `hooks/config.py:176`, `:1350`, `:1460`, `:1504`, `:1553`; `pact_check.py:302`, `:542`, `:807`; `chain_check.py:4844`; `evidence_check.py:5237`. The line was written by this run in phase 2 and rewritten at `259b82ee`, so rung 1: the branch's diff |

## Paste-ready fixes

```markdown
  `hooks/config.py#hidden_lines`, which reads `seal/config.md`, keeps,
  wherever its walk is unsure, the fence-only reading it gave before #667:
  a row below a fence nobody closed declares nothing, and a row below a
  comment opener nobody closed still declares unless a fence that closes
  holds it, because that reading never hid one and work item 1790645290
  was bound to miss no row the older reading saw. `hooks/routing.py#shown`,
  which reads a `routing.md` and is not one of the seven, keeps the reading
  it gave before #667 the same way, and that reading hid nothing: a row
  below a fence or a comment opener nobody closed still declares there,
  unless a fence that closes holds it. Those rows are the places a line
  nobody wrote live declares something; at every other fence or comment,
  what this protects is that nothing is excused or declared by a line
  nobody wrote live. The wrong answer is a fold reported as a deletion at
  exit 1, a fragment the sweep keeps, a hook that says nothing, or a gate
  that asks.
```
```markdown
Enforced by: tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py::test_each_reader_gives_its_stated_answer_on_each_shape, tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py::test_the_statement_names_each_reader_under_its_answer, tests/test_routing_is_recorded.py::test_the_routing_shapes_read_as_the_frame_expects, tests/test_routing_is_recorded.py::test_a_declaration_below_a_comment_opener_nobody_closed_still_reads
```
```python
def test_a_declaration_below_a_comment_opener_nobody_closed_still_reads():
    """#872 round 3, finding 10. `hooks/routing.py#shown` keeps the reading
    it gave before #667 wherever its walk is unsure, and that reading hid
    nothing, so a table below a line-start comment opener nobody closed
    still declares, although a renderer hides it. R3 holds the fence half;
    this holds the comment half, which no case did."""
    text = "<" + "!-- nobody closed this\n\n" + two_axis_text()
    parsed = routing.parse(text)
    assert parsed is not None and parsed["review"] == CHAIN, parsed
```
```python
    Reads: guess — the lines of `seal/config.md`, `seal/pact.md`, a `seal/pact-changes/` record and the machine-local pact path map, through `unfenced` and `hooks/blocks.py#walk`; unknown mixed
```

## Executed probes

| What was run | Result |
|---|---|
| one test_tmp probe script, run with the clone's `.venv` interpreter against the clone's modules, then deleted: `hooks/routing.py#shown`, `hooks/config.py#hidden_lines` and the walk on a routing row in four shapes, plus R3 and R8 | below an unclosed fence: shown, hidden, walk unsure. Below an unclosed line-start comment opener: shown, not hidden, walk unsure. In a closed fence below an unclosed `~~~~`: not shown, hidden, walk sure. In a closed fence below an unclosed comment opener: not shown, hidden, walk sure. R8's fenced row: not shown, hidden. R3's rows: shown |
| a crude mutation of `shown` in the clone, hiding every walk-unsure line below the first line-start comment opener with no closer after it; `bin/test` on the three routing modules with `-q` and `SPECSEAL_CASE_CEILING_S=600` | exit 1: `test_the_routing_reader_never_leaves_both_readings` failed on 403 documents, 224 passed |
| a renderer-exact mutation of `shown` in the clone, hiding below an unclosed line-start comment opener only the lines the renderer oracle hides; the same three modules, same flags | exit 0, 225 passed. The probe above, rerun, showed the row below the unclosed opener hidden |
| the case in 🟡 10's fix as a test_tmp module in the clone's `tests/`, run once on the second mutation and once after `git checkout -- hooks/routing.py`, then deleted | exit 1 on the mutation, exit 0 at `f9020934` |
| `bin/evidence-check --strict .` in the clone | exit 0: every section 0 drifted, 0 broken, 0 malformed |
| `bin/fold-check --root .` in the clone | exit 0: 186 statements in 19 documents, 0 over the 1000-line ceiling |
| `git diff --stat 321e9de1 HEAD -- seal/releases seal/ledger.md` in the clone | empty, exit 0 |
| the broad gate: full suite, repository lint, typecheck | not yet. It belongs to the sealer, once the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `docs/the-evidence-ledger.md:629` | round 1's 🟡 1 — fixed |
| round-1 | `docs/the-evidence-ledger.md:625` | round 1's 🟡 2 — fixed |
| round-1 | `skills/evidence-check/scripts/evidence_check.py:370` | round 1's 🟡 3 — fixed |
| round-1 | `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py:222` | round 1's ⬜ 4 — answered |
| round-1 | `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/overview.md:31` | round 1's ⬜ 5 — answered |
| round-1 | `tests/undeclared_readers.txt` | round 1's 🟢 — confirmed |
| round-1 | `skills/verify/scripts/unverified_check.py:744` | round 1's 🟢 — confirmed |
| round-1 | `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py:79` | round 1's 🟢 — confirmed |
| round-1 | `seal/ledger/1791852615-whether-a-ledger-line-is-live-has-seven-rules.md` | round 1's 🟢 — confirmed |
| round-1 | `seal/releases` | round 1's 🟢 — confirmed |
| round-2 | `docs/the-evidence-ledger.md:633` | round 2's 🟢 — confirmed |
| round-2 | `docs/the-evidence-ledger.md:642` | round 2's 🟡 6 — fixed |
| round-2 | `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/plan.md:58` | round 2's ⬜ 7 — answered |
| round-2 | `seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/changelog.md:14` | round 2's ⬜ 8 — answered |
| round-2 | `docs/the-evidence-ledger.md:631` | round 2's ⬜ 9 — answered |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
