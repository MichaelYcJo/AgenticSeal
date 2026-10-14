# 1791876665-each-budget-ratchets-and-every-pull-request-measures-it — review round 3

| Field | Value |
|---|---|
| Target SHA | 400a54df5a56ffaa2d5fdd7a6b6970f575b84632 |
| Written late | no |
| Ran by | warden on Opus 5.5 |
| PR | 938 |
| Broad gate | not yet |
| Fixes checked by | no fixes to check |
| Fix range | `eea3dbc84d59502eaf1e1c32d4ac5f063fdaea63..eea3dbc84d59502eaf1e1c32d4ac5f063fdaea63`, 0 commits |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | no |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 3 of #930 against 400a54df, the run's last round: verify round 2's fix pass (f594450d..4ddf0edb), the fenced-heading fix with its cases and the corrected spread, and check that the fix created nothing new.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 2's finding 1 is closed — `section` reads headings as GitHub shows them and refuses a doubled title | `.github/scripts/budget_check.py:384` | confirmed | executed: the three planted cases pass at 400a54df and fail against f594450d's `section` |
| 🟢 | round 2's note 2 is closed — the spread is stated with its set, 0.76 to 1.14 and 0.46 to 1.54 | `.github/scripts/budget_check.py:75` | confirmed | read: the docstring, `spec.md` and `overview.md`; no `1.16` left |
| 🟢 | the fix created nothing new | `.github/scripts/budget_check.py:384` | confirmed | read: a section's start is outside every fence and comment; executed: the tree exits 0, four census modules 182 passed |

## Paste-ready fixes

no paste-ready fix in the report

## Executed probes

| What was run | Result |
|---|---|
| the three new cases in `tests/test_a_budget_ratchets.py` at 400a54df, through `bin/test -k` | 3 passed, exit 0 |
| the same three with `budget_check.py` checked out from f594450d, then restored | 3 failed, exit 1; the clone was clean afterwards |
| `budget_check.py` over the tree at 400a54df | exit 0, every gate row holds |
| 4 census modules through `bin/test` at 400a54df | 182 passed, exit 0 |
| the broad gate (full suite, lint, typecheck) at this branch's tip | not yet: the sealer's, and it is due now |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `.github/scripts/budget_check.py:321` | round 1's 🟡 1 — fixed |
| round-1 | `.github/scripts/budget_check.py:863` | round 1's 🟡 2 — fixed |
| round-1 | `.github/scripts/budget_check.py:632` | round 1's 🟡 3 — fixed |
| round-1 | `.github/scripts/budget_check.py:934` | round 1's 🟡 4 — fixed |
| round-1 | `skills/verify/SKILL.md:484` | round 1's 🟡 5 — fixed |
| round-1 | `seal/ledger/1791876665-each-budget-ratchets-and-every-pull-request-measures-it.md:6` | round 1's ⬜ 6 — answered |
| round-1 | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md:69` | round 1's ⬜ 7 — answered |
| round-1 | `.github/scripts/budget_check.py:1227` | round 1's ⬜ 8 — answered |
| round-1 | `skills/verify/scripts/broad_gate.py:2416` | round 1's 🟢 — confirmed |
| round-1 | `.github/workflows/hygiene.yml:17` | round 1's 🟢 — confirmed |
| round-1 | `tests/` | round 1's 🟢 — confirmed |
| round-1 | `tests/test_a_budget_ratchets.py` | round 1's ❓ — out of verified scope |
| round-2 | `.github/scripts/budget_check.py:383` | round 2's 🟡 1 — fixed |
| round-2 | `.github/scripts/budget_check.py:76` | round 2's ⬜ 2 — answered |
| round-2 | `.github/scripts/budget_check.py:324` | round 2's 🟢 — confirmed |
| round-2 | `.github/scripts/budget_check.py:682` | round 2's 🟢 — confirmed |
| round-2 | `.github/scripts/budget_check.py:805` | round 2's 🟢 — confirmed |
| round-2 | `.github/scripts/budget_check.py:568` | round 2's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
