# 1791876667-the-durations-refresh-has-a-schedule — review round 4

| Field | Value |
|---|---|
| Target SHA | 25728e2cc1f4369cd4e87d7e1c487e339f4a8cfa |
| Written late | no |
| Ran by | specseal:warden on claude-opus-5-5 |
| PR | #937 |
| Broad gate | not yet |
| Fixes checked by | no fixes to check |
| Fix range | `25728e2cc1f4369cd4e87d7e1c487e339f4a8cfa..25728e2cc1f4369cd4e87d7e1c487e339f4a8cfa`, 0 commits |
| Contract changes | none |
| New units | none |
| Fix of a fix | second — 🟡 1 at tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#REMEDY, a unit round-3's fixes changed; the fix passes stop here and the work item goes back to its framer |
| Needs a fix | yes — 🟡 1, the staleness message gives a restate command without `--baseline`, which exits 2 |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Verifying round 4 of #931, the run's last: round 3's two fixes over 5c93835e..2ce9df33 (slow-file rows report; --restate-price writes the price level), whether --restate-price is the one writer of the level, whether the flag oversteps a fix pass, and the PR body against budget_check.py. Narrow checks only.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | the staleness message gives `budget_check.py --restate-price` with no `--baseline`, which the checker refuses with exit 2; the PR body's item 2 and the work item's changelog say the message gives the `--baseline origin/<base>` form, and the case asserts the short form | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:284` | deferred the frame | the frame — the second fix of a fix in this run stops the fix passes; the reframe takes it; executed: the command without `--baseline` exits 2 in the clone; read: `REMEDY`, the assertion at line 401, `changelog.md:23` and `:48-50`, PR body item 2 |
| ⬜ 2 | the level `--restate-price` writes and the level `price_problems` demands are one expression written twice, so a change to one copy makes the writer write a level the check refuses | `.github/scripts/budget_check.py:1396` | deferred the frame | the frame — the price-level expression written twice goes with the reframe; read: `:1396` and `:1423`; executed: today both give 1136 on round 3's union |
| ⬜ 3 | work item 1791876665's spec still says `slow-file` is a gate that fails an unlisted file over 120 s, and its questions list it among the gates; that item is settled into `docs/` at the 0.22.0 release | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md:36` | deferred the frame | the frame — work item 1791876665 still calls slow-file a gate; the reframe corrects it with this item; read: `spec.md:36`, `questions.md:8`; this branch's `seal/budgets.md:41` makes the family `report` |
| ⬜ 4 | the PR body says "Measured over eight refreshes"; round 3 measured eight pairs, and 0.67 to 1.72 is the range over its four union-to-union pairs | PR #937 body, *What changes* item 4 | answered | the PR body says four union-to-union pairs, edited on the pull request; read: round 3's report §3 table |
| 🟢 | round 3's 🟡 2 is closed — the `slow-file` family is a `report` row and `suite-seconds` stays the gate | `seal/budgets.md:41` | confirmed | executed: the case goes red with the row set to `gate`; the PR body's 20 removal lines give exit 0; round 3's union with the level restated holds with the body |
| 🟢 | round 3's 🟡 1 is closed — `--restate-price` writes the level the check demands and the recipe gives the full command | `.github/scripts/budget_check.py:1439`, `CONTRIBUTING.md:182` | confirmed | executed: on round 3's union the check names 1136, the flag writes 1136 on one line, and the run with the body is exit 0; the case goes red without the line that clears the price problem; the message's remaining gap is this round's 🟡 1 |
| 🟢 | adding `--restate-price` in a fix pass does not overstep | `.github/scripts/budget_check.py:1341` | confirmed | read: the alternative stops for a person on every refresh, against `CLAUDE.md`'s first goal; the flag writes only where the check would fail on the level, and both refusals leave the file untouched (executed by the module's cases) |
| 🟢 | the PR body passes the hygiene step's command at the tip | PR #937 body | confirmed | executed: `--baseline 5b1f6fae --base-ref release/v0.22.0 --pr-body-env PR_BODY`, exit 0 |

## Paste-ready fixes

```python
REMEDY = (
    "Refresh it from this branch's latest `tests` run, whose `durations` job "
    "unioned the Windows shards' parts: `gh run download <run id> -n "
    "test-durations -D <dir>`, then move <dir>/.test_durations over the "
    "committed .test_durations, write the price level it implies into "
    "seal/budgets.md with `python3 .github/scripts/budget_check.py "
    "--baseline origin/<base> --restate-price`, where <base> is the branch "
    "the pull request merges into, and commit both; "
    "the file's line ends are already LF. "
    "A run older than the artifact's seven days is re-run first, with "
    "`gh run rerun <run id>`; a branch with no pull request, or whose run "
    "is too old to re-run, gets one with `gh workflow run test.yml --ref "
    "<branch>` (CONTRIBUTING.md §Running the checks)."
)
```
```python
    assert (
        "`python3 .github/scripts/budget_check.py --baseline origin/<base> "
        "--restate-price`, where <base> is the branch the pull request merges "
        "into, and commit both" in sentence
    )
```
```markdown
    the file over the committed one, write its price level with
    `budget_check.py --baseline origin/<base> --restate-price`, commit both. The download needs a
```
```python
def expected_level(base_level, ratio):
    """The price level here, per mille: the base's times the ratio the
    durations file moved by, rounded.

    Reads: nothing — a number from the numbers handed to it"""
    return seconds(base_level * ratio)
```
```python
            if restate and priced:
                level = restate_price(root, head_text, expected_level(base_level, ratio))
```
```python
    expected = expected_level(base_level, ratio)
```
```markdown
| report · gated at first; #931 made the family a `report` row, because one union of the Windows shards' parts moves a single file 0.67 to 1.72 times the level from the next, and `suite-seconds` is the gate |
```
```markdown
4. **`slow-file` rows report instead of gating.** Over four unions of one tree, a single test file moved 0.67 to 1.72 times the level from one union to the next, past the 1.3 band, on files nobody changed.
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` on `tests/test_a_budget_ratchets.py`, `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, `tests/test_every_reader_ends_a_line_where_gfm_does.py` at 25728e2c | exit 0: 339 passed, 2 skipped |
| `budget_check.py --baseline 5b1f6fae --base-ref release/v0.22.0 --pr-body-env PR_BODY`, body from `gh pr view 937` | exit 0 |
| run 38655519975's union over `.test_durations`, `budget_check.py --restate-price` with no baseline | exit 2: "given without --baseline"; the file untouched |
| the same union, `budget_check.py --baseline 5b1f6fae` | exit 1: level 1136 named, plus the 20 removals with no body |
| the same union, `--baseline 5b1f6fae --restate-price` | exit 1: wrote 1136, one line of `seal/budgets.md` changed; the 20 removals remain with no body |
| the same, then the check with the PR body | exit 0 |
| mutation: `slow-file` row set to `gate`, and the clearing of the price problem after a restate removed; the two new cases run | exit 1: both fail; reverted, clone clean |
| `round-record new` on a copy of this report, in the clone only | exit 0; wrote `Fix of a fix` as second for 🟡 1 at `REMEDY`, and said this record ends the run |
| `bin/test tests/test_no_real_identifiers.py` with that copy staged in the clone | exit 0: 6 passed |
| the full suite, lint and typecheck | not yet: the sealer's, after the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `.github/workflows/test.yml:175` | round 1's 🟡 1 — fixed |
| round-1 | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:272` | round 1's 🟡 2 — fixed |
| round-1 | `tests/test_ci_gives_the_checks_what_they_need.py:325` | round 1's 🟡 3 — fixed |
| round-1 | `.github/scripts/durations_union.py:153` | round 1's 🟡 4 — fixed |
| round-1 | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` | round 1's 🟢 — confirmed |
| round-1 | `.github/scripts/durations_union.py`, `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#staleness` | round 1's 🟢 — confirmed |
| round-1 | `CONTRIBUTING.md:169`, `seal/specs/1791876667-the-durations-refresh-has-a-schedule/survivors.md` | round 1's 🟢 — confirmed |
| round-1 | `.github/workflows/test.yml:186-207` | round 1's 🟢 — confirmed |
| round-1 | `tests/` | round 1's 🟢 — confirmed |
| round-1 | `.github/workflows/test.yml:168-175`, `.github/workflows/test.yml:201-207` | round 1's ❓ — out of verified scope |
| round-2 | `.github/workflows/test.yml:168-177` | round 2's 🟢 — confirmed |
| round-2 | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:279-288`, `CONTRIBUTING.md:215-218` | round 2's 🟢 — confirmed |
| round-2 | `tests/test_ci_gives_the_checks_what_they_need.py#runs_pytest` | round 2's 🟢 — confirmed |
| round-2 | `.github/scripts/durations_union.py:234-235` | round 2's 🟢 — confirmed |
| round-2 | `seal/ledger/1791876667-the-durations-refresh-has-a-schedule.md` | round 2's ⬜ 6 — answered |
| round-2 | `.github/workflows/test.yml:168-177`, `.github/workflows/test.yml:203-210` | round 2's carried — deferred |
| round-3 | `CONTRIBUTING.md:177` | round 3's 🟡 1 — fixed |
| round-3 | `.github/scripts/budget_check.py:91` | round 3's 🟡 2 — fixed |
| round-3 | `seal/specs/1791876667-the-durations-refresh-has-a-schedule/spec.md:58` | round 3's ⬜ 3 — answered |
| round-3 | `seal/specs/1791876667-the-durations-refresh-has-a-schedule/changelog.md:40` | round 3's ⬜ 4 — answered |
| round-3 | `.github/workflows/test.yml`, `CONTRIBUTING.md:135`, `seal/budgets.md:85` | round 3's 🟢 — confirmed |
| round-3 | `seal/specs/1791876667-the-durations-refresh-has-a-schedule/` | round 3's 🟢 — confirmed |
| round-3 | `.github/workflows/test.yml:168-176` | round 3's 🟢 — confirmed |
| round-3 | `CONTRIBUTING.md:183-185` | round 3's 🟢 — confirmed |
| round-3 | `tests/test_ci_gives_the_checks_what_they_need.py:328` | round 3's 🟢 — confirmed |
| round-3 | `.github/scripts/durations_union.py:234` | round 3's 🟢 — confirmed |
| round-3 | `.github/workflows/test.yml:94` | round 3's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
