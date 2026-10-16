# 1791940762-the-record-of-truth-is-tests-not-coordinates — review round 3

| Field | Value |
|---|---|
| Target SHA | ce1795fad460ffa4025bfd492bef934b060ddb8d |
| Written late | no |
| Ran by | specseal:warden on claude-opus-5-5 |
| PR | #950 |
| Broad gate | e5bfda3e against f975ea66 |
| Fixes checked by | no fixes to check |
| Fix range | none |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | no |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Verifying round 3 of #944: round 2's one fix at 005919e3 (test_pact_check.py's ceiling 157 and the PR body's line), the overview's three places written at fa8f9872, and the PR body's removed budget lines. Narrow checks only.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 2's finding 1 is closed — `tests/test_pact_check.py`'s ceiling is 157, 1.3 times its 120.69 s priced reading rounded up, and the PR body's one line says `120 -> 157` | `seal/budgets.md:73` | confirmed | executed: `budget_check.py` exit 0 with the PR body (36 s headroom), exit 1 with an empty body naming only that line, exit 1 with a stale `120 -> 121` line quoting it; read: `seal/budgets.md:15-17` |
| 🟢 | the overview text round 2's note 2 named now says what the tree has, in all three places | `seal/specs/1791940762-the-record-of-truth-is-tests-not-coordinates/overview.md:34` | confirmed | executed: entries 11,863 to 9,208 across 8a63e245; no id names a missing file; the durations case passes; read: run 38646055747's Windows leg is unsharded with `--clean-durations`; the note itself is carried and closes at the run's end |
| 🟢 | the range changes nothing beyond the fix, the overview paperwork and round 2's close | `seal/specs/1791940762-the-record-of-truth-is-tests-not-coordinates/rounds/round-2.md:10` | confirmed | executed: `git diff --stat 04edf1aa..ce1795fa` is three files; the close's fix range holds one commit; no new unit |
| 🟢 | the lines removed from the PR body were inert | PR #950 body | confirmed | executed: with an empty body the checker's only refusal is the `slow-file:tests/test_pact_check.py` raise |
| ⬜ 1 | the changelog's "the suite's priced total fell by 796.5 seconds" is in the base's prices, and the refreshed `.test_durations` prices the suite at x1.132, a fall of 1,008 priced seconds against the base | `seal/specs/1791940762-the-record-of-truth-is-tests-not-coordinates/changelog.md:49` | answered | corrected at dfb5c7ed — dfb5c7ed; executed: totals 7,861.7 at the base, 7,066.9 before 8a63e245, 7,758.7 raw at the tip; read: the fragment last changed at 7b8edffb, before 8a63e245; paperwork, not counted in `Needs a fix` |

## Paste-ready fixes

```markdown
  Measured against the merge base `f975ea66`: the branch is 4,302 lines in
  and 54,867 out, and 19.1 more Windows seconds left with cases cut from
  kept modules, so the deleted cases cost 796.5 seconds at the base's
  prices. The refreshed `.test_durations` prices the whole suite at 6,854
  seconds against the base's 7,862.
```

## Executed probes

| What was run | Result |
|---|---|
| `python3 .github/scripts/budget_check.py --root <clone> --baseline origin/release/v0.22.0 --pr-body-env PRB --base-ref release/v0.22.0`, with `PRB` from `gh pr view 950 --json body -q .body`, at ce1795fa | exit 0; `slow-file:tests/test_pact_check.py` 121 s (raw 137 at x1.132) against 157, 36 (22.9 %) headroom; "every gate row holds" |
| the same with `PRB` empty | exit 1; one refusal line, naming only `slow-file:tests/test_pact_check.py` `120 -> 157` |
| the same with the body's line edited to `120 -> 121` | exit 1; the refusal quotes "The body's line says 120 -> 121" |
| `python3` over `.test_durations`: the file's total for `tests/test_pact_check.py`, entry counts at 8a63e245's parent, 8a63e245 and HEAD, ids naming a missing file | 136.62 s raw, 120.69 s priced, 156.89 at 1.3 times; 11,863 / 9,208 / 9,208; no missing file; six `ledger` ids, each a case that exists |
| `bin/test tests -q -k test_the_durations_file_prices_the_suite` in the clone | 1 passed, exit 0 |
| `.test_durations` totals at f975ea66, 8a63e245's parent and HEAD | 7,861.7 s / 7,066.9 s / 7,758.7 s raw (6,854 at x1.132); the base's price level is 1000 |
| `round-record new` on this report, inside the clone, then discarded with it | run twice, exit 0 both times. The first run, before ⬜ 1 was written, ticked `Pass`; its chain check printed the changelog-fragment notice that led to ⬜ 1. The second run, with ⬜ 1 in the table, left `Pass` unticked. `Needs a fix` read no both times |
| `gh run view 38646055747` and its failed log | read, not run: a `pull_request` run at e05213e0; the Windows leg ran with `--store-durations --clean-durations` and no split; its 3 failures are in the shard test module |
| `gh pr checks 950` | read, not run: lint, release and arm-check-grammar pass; every pytest leg pending |
| the broad gate (full suite, lint, typecheck) | not yet — the sealer's, once, after the rounds settle; nothing above stands for it |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `.github/scripts/rules.py:139` | round 1's 🟡 1 — fixed |
| round-1 | `.github/scripts/rules.py:73` | round 1's 🟡 2 — fixed |
| round-1 | `.github/scripts/budget_check.py:219` | round 1's 🟡 3 — fixed |
| round-1 | `docs/the-record-layout.md:243` | round 1's 🟡 4 — fixed |
| round-1 | `skills/implement/orchestration.md:56` | round 1's 🟡 5 — fixed |
| round-1 | `seal/follow-up.md:74` | round 1's 🟡 6 — fixed |
| round-1 | `docs/the-record-layout.md:17` | round 1's 🟡 7 — fixed |
| round-1 | `tests/test_the_set_a_work_item_always_has.py:308` | round 1's 🟡 8 — fixed |
| round-1 | `tests/test_a_unit_is_bounded_where_a_parser_decides.py` | round 1's ❓ — out of verified scope |
| round-2 | `seal/budgets.md:73` | round 2's 🟡 1 — fixed |
| round-2 | `seal/specs/1791940762-the-record-of-truth-is-tests-not-coordinates/overview.md:56` | round 2's ⬜ 2 — answered |
| round-2 | `.github/scripts/rules.py:163` | round 2's 🟢 — confirmed |
| round-2 | `.github/scripts/rules.py:62` | round 2's 🟢 — confirmed |
| round-2 | `skills/implement/orchestration.md:18` | round 2's 🟢 — confirmed |
| round-2 | `tests/test_the_rules_command_reads_each_rule_off_its_test.py:111` | round 2's 🟢 — confirmed |
| round-2 | `.github/workflows/test.yml:94` | round 2's 🟢 — confirmed |
| round-2 | `seal/budgets.md:49` | round 2's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
