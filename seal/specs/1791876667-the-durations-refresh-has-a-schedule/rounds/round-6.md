# 1791876667-the-durations-refresh-has-a-schedule — review round 6

| Field | Value |
|---|---|
| Target SHA | 701bc6c1ce477b3b85772adf4094ced82c4a7140 |
| Written late | no |
| Ran by | specseal:warden on claude-opus-5-5 |
| PR | #937 |
| Broad gate | c5bd3ca0 against 5b1f6fae |
| Fixes checked by | no fixes to check |
| Fix range | none |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | no |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Verifying round 6 of #931: round 5's three fixes over bbf2daa3..af18ab2e (render names a report row's problems, gate messages unchanged, 1791876665's S7 and changelog), and whether 1791876665's T10 row needs the report-kind case. Narrow checks only.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| ⬜ 1 | work item 1791876665's changelog fragment says "Three reports", and the third, `ledger-rereads`, was removed on the base by #944; the same row stands at that item's `spec.md:39` and `questions.md:8` | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/changelog.md:27` | answered | corrected at cf72ab77 — cf72ab77; executed: grep finds `ledger-rereads` in neither `seal/budgets.md` nor the checker at 701bc6c1 or 5b1f6fae, and the summary lists two report kinds; read: `changelog.md:27-28`, `spec.md:39`, `questions.md:8`; a record correction, which `Needs a fix` does not count |
| ⬜ 2 | work item 1791876665's `plan.md:74` links S7 to T10 alone, and T10 asserts exit 1 under a `gate` fixture; S7 now states the `report` kind, which only `test_an_unlisted_slow_file_under_a_report_row_is_named` holds | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/plan.md:74` | answered | corrected at cf72ab77 — cf72ab77; read: `plan.md:74`, `spec.md:59`, `tests/test_a_budget_ratchets.py:474` and `:604-622`, settle's *A standing statement has one shape*; the implementer's open question, answered yes; a record correction |
| ⬜ 3 | T10's docstring says an unlisted file over the threshold "fails" under S7; S7 says it fails nothing | `tests/test_a_budget_ratchets.py:619` | answered | corrected at cf72ab77 — cf72ab77; read: `:619-620` against `spec.md:59` of work item 1791876665; the behaviour is right and the sentence is wrong |
| ⬜ 4 | a module docstring line runs 135 characters after 21ffe7fb's insert, and `render`'s docstring keeps a short line mid-paragraph | `.github/scripts/budget_check.py:120` | answered | corrected at cf72ab77 — cf72ab77; executed: awk line lengths, ruff exit 0 (E501 not selected); read: `:113-121`, `:1229-1232` |
| 🟢 | round 5's finding 3 is closed — `render` prints every report row's problems under a heading that says they fail nothing, and an unlisted slow file is named | `.github/scripts/budget_check.py:1284` | confirmed | executed: the real tree with 300 s added to an unlisted file gives exit 0, `slow-file` `over`, and the list names the file; the new case red against bbf2daa3 and 21ffe7fb and green at af18ab2e; failing problems still come from gate rows alone (`:1432-1434`, read) |
| 🟢 | a gate row's problem text is unchanged byte for byte across the range; a report row's differs only in its last clause | `.github/scripts/budget_check.py:1067` | confirmed | executed: probe over all 103 rows, `band` and `unlisted_band`, 624 comparisons against bbf2daa3's checker, exit 0 |
| 🟢 | a report row's problem saying it needs no `Budget raised:` line is true of `ratchet` | `.github/scripts/budget_check.py:1169` | confirmed | read: `ratchet` skips a base row that is not a gate; file rows inherit the family's kind (`:436`) and `effective` copies the family row (`:1146`); executed: the checker with PR #937's body exits 0 and with an empty body exits 1 on the 20 kind changes alone |
| 🟢 | round 5's finding 1 is closed — 1791876665's S7 says exit 0 and where the summary names the file | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md:59` | confirmed | executed: the real-tree probe matches each clause; read: `spec.md:59` |
| 🟢 | round 5's finding 2 is closed in what it named — the fragment no longer holds each slow file to a ceiling and calls it a report | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/changelog.md:17` | confirmed | read: `:17-22`, `:27`; the count in item 5 is ⬜ 1 |
| 🟢 | 1791876667's changelog fragment states the report row and its grounds once, and its sentence about the list matches `render` | `seal/specs/1791876667-the-durations-refresh-has-a-schedule/changelog.md:44` | confirmed | read: `:36-55` against `render` `:1284-1294` |

## Paste-ready fixes

```markdown
  5. Two reports fail nothing: each slow test file, and the largest round
     records in the tree. A release pull request prints every budget
     against the last release tag.
```
```markdown
| T10 `test_an_unlisted_file_over_the_threshold_fails_and_a_listed_one_may_not_grow`, `test_an_unlisted_slow_file_under_a_report_row_is_named` | S7 (the first under a `gate` family, the second under the `report` kind this repository gives it) | the threshold check removed; the per-file compare removed; `render`'s list of report rows' problems removed, or a report row's problem asking for a `Budget raised:` line |
```
```python
    """T10, S7 under a `gate` family: a test file over the threshold that
    the table does not list fails, naming it; a listed one is held to its
    own ceiling. This repository's family is a `report` row, which
    `test_an_unlisted_slow_file_under_a_report_row_is_named` holds."""
```
```python
ceiling of their own. So where the family is a `gate`, an unlisted file
over the threshold fails, and listing it is a raise from the threshold
that needs its line, as is a row the table drops whose ceiling was under
it. Where the family is a `report`, that file fails nothing and the
summary names it in the list of report rows past their band. Every test
file whose reading times 1.3 reaches the threshold is listed, so an
unlisted one has the same room to move before it reads over. A docs
```
```python
    """The summary as markdown: one line per budget, each report row's
    problems, the raises read, the price level the seconds rows were read
    at, and where the docs were classified, each document's history and
    rule lines.
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test tests/test_a_budget_ratchets.py tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py -q` | exit 0, 191 passed, 2 skipped |
| `bin/test` over `tests/test_docs_line_wrap.py`, `tests/test_no_real_identifiers.py`, `tests/test_one_word_one_meaning.py`, `tests/test_the_changelog_is_gathered_at_release.py` | exit 0, 116 passed |
| `bin/test tests/test_every_reader_ends_a_line_where_gfm_does.py -q` | exit 0, 149 passed |
| a probe comparing `band` and `unlisted_band` at bbf2daa3 and 701bc6c1 over every row of `seal/budgets.md`, each as a gate and as a report | exit 0, 624 comparisons over 103 rows; gate text equal; report text differs only in its last clause; deleted |
| the new case against `.github/scripts/budget_check.py` at bbf2daa3, at 21ffe7fb and at af18ab2e | exit 1 (no list in the summary); exit 1 at `tests/test_a_budget_ratchets.py:714`; exit 0; file restored |
| `python3 .github/scripts/budget_check.py --baseline origin/release/v0.22.0 --pr-body-env PRBODY` with PR #937's body (`gh pr view 937 --json body -q .body`, head 701bc6c1) | exit 0; the list holds `rounds-bytes` alone, 151,863 over 142,823; 20 `slow-file` removals read as declared |
| the same with an empty body | exit 1, 20 `Budget removed:` problems, one per `slow-file` row that is no longer a gate |
| 300 s added to one case of `tests/test_docs_line_wrap.py` in `.test_durations`, the checker with no baseline | exit 0; `slow-file` `266 seconds (largest unlisted)`, `report`, `over`; the list names the file with the listing clause; reverted |
| `uvx ruff check` and `uvx ruff format --check` over the two changed Python files | exit 0, exit 0 |
| the full suite, lint and typecheck at 701bc6c1 | not yet — not this round's to run; the sealer runs it once, and this round leaves nothing needing a fix, so the sealer's spawn comes due |

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
| round-4 | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:284` | round 4's 🟡 1 — deferred |
| round-4 | `.github/scripts/budget_check.py:1396` | round 4's ⬜ 2 — deferred |
| round-4 | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md:36` | round 4's ⬜ 3 — deferred |
| round-4 | PR #937 body, *What changes* item 4 | round 4's ⬜ 4 — answered |
| round-4 | `seal/budgets.md:41` | round 4's 🟢 — confirmed |
| round-4 | `.github/scripts/budget_check.py:1439`, `CONTRIBUTING.md:182` | round 4's 🟢 — confirmed |
| round-4 | `.github/scripts/budget_check.py:1341` | round 4's 🟢 — confirmed |
| round-4 | PR #937 body | round 4's 🟢 — confirmed |
| round-5 | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md:59` | round 5's 🟡 1 — fixed |
| round-5 | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/changelog.md:17` | round 5's 🟡 2 — fixed |
| round-5 | `.github/scripts/budget_check.py:1410` | round 5's 🟡 3 — fixed |
| round-5 | `seal/specs/1791876667-the-durations-refresh-has-a-schedule/overview.md:7` | round 5's ⬜ 4 — answered |
| round-5 | `.github/scripts/budget_check.py:1418` | round 5's 🟢 — confirmed |
| round-5 | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/questions.md:8` | round 5's 🟢 — confirmed |
| round-5 | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/overview.md:24` | round 5's 🟢 — confirmed |
| round-5 | `seal/budgets.md:25` | round 5's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
