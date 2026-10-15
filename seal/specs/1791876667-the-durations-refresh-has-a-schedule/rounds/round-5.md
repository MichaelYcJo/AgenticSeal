# 1791876667-the-durations-refresh-has-a-schedule — review round 5

| Field | Value |
|---|---|
| Target SHA | a6919ade07f2e59f6f9d87152e44b9190cb91cc7 |
| Written late | no |
| Ran by | specseal:warden on claude-opus-5-5 |
| PR | #937 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are written and no round has opened them |
| Fix range | `bbf2daa3204ffab9d706dee8a2a4b5b84de11575..af18ab2e7d831b4ab39d467c78035011b3897bec`, 5 commits |
| Contract changes | none |
| New units | test_an_unlisted_slow_file_under_a_report_row_is_named (depth 1) |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 3, a report row's problems are never printed, so an unlisted slow file is not named; 🟡 1 and 🟡 2 are record corrections that `Needs a fix` does not count |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Round 5 of #931, the first after the reframe: phase 4 over 179e8ef3..a6919ade against its plan row and the reframed spec (REMEDY's command runs, one expected_level, 1791876665's records call slow-file a report row, the changelog's full command), then the branch as a whole against its PR body and records, and the two places left on purpose. Narrow checks only.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | work item 1791876665's S7 still says an unlisted slow file is "exit 1 naming the file"; the family is a `report` row and the tree exits 0; round 4's ⬜ 3 is closed at `spec.md:36` and `questions.md:8` and not here | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/spec.md:59` | **fixed** `4a61fb66` | fixed at 4a61fb66; executed: an unlisted file at 266 s gives exit 0 and an `over` report line; read: `spec.md:59`, S9 of this item's spec; a record correction, which `Needs a fix` does not count |
| 🟡 2 | work item 1791876665's changelog fragment says each slow file is "held to a ceiling" and "Two reports fail nothing"; 0.22.0 ships `slow-file` as a third report, and the fragment is gathered verbatim | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/changelog.md:17` | **fixed** `a3df4afd` | fixed at a3df4afd; read: `:17-19`, `:27`, `seal/budgets.md:41`; `docs/the-record-layout.md` §*A commit after the build brings its changelog fragment along*; a record correction, which `Needs a fix` does not count |
| 🟡 3 | a `report` row's problems are never printed, so an unlisted file past the `slow-file` threshold is not named anywhere; the PR body, this item's changelog and `seal/budgets.md` say each file's reading prints | `.github/scripts/budget_check.py:1410` | **fixed** `21ffe7fb` | fixed at 21ffe7fb; executed: an unlisted file at 266 s gives `266 seconds (largest unlisted) … report \| over` and no path in the output; read: `render` `:1265`, `unlisted_band`; the fix tried in the clone, its case red without it |
| ⬜ 4 | this item's closing memo lists S1–S8 and phases 1–3 and phase 1–2 mutation counts; the reframed spec has S9 and the plan phase 4 | `seal/specs/1791876667-the-durations-refresh-has-a-schedule/overview.md:7` | open | read: `overview.md:7-8`, `spec.md` S9, `plan.md` row 4, `phases/phase-4.md` |
| 🟢 | round 4's blocking finding is closed — the staleness message gives the whole restate command, and the case asserts it | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:284` | confirmed | executed: the command as typed exits 1 and writes one line, exit 0 with the PR body; the case exits 1 against 9021bc49's `REMEDY` |
| 🟢 | round 4's note 2 is closed — the price level has one expression, which the writer and the check both call | `.github/scripts/budget_check.py:1418` | confirmed | executed: the grep prints `:1424` alone; `+ 1` on its `return` turns 3 cases red, among them the writer's and the check's |
| 🟢 | the phase-4 records: 1791876665's `slow-file` Kind cell and questions bullet say `report` with no history narrative; this item's changelog gives the full command | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/questions.md:8` | confirmed | read: `spec.md:36`, `questions.md:8`, `changelog.md:23-25`; both `## Removes` texts absent |
| 🟢 | 1791876665's `overview.md:24` quoting the frame's old clause is left as written | `seal/specs/1791876665-each-budget-ratchets-and-every-pull-request-measures-it/overview.md:24` | confirmed | read: a divergence row's second column is what the frame said when phase 2 built; its decision still holds (executed: the family row holds an unlisted file at 120 s) |
| 🟢 | `seal/budgets.md:25`'s short `--restate-price` pointer is left as written | `seal/budgets.md:25` | confirmed | read: a comment that names the flag and points at the recipe for the command; the bare form's exit 2 names `--baseline` |

## Paste-ready fixes

```markdown
| S7 a slow file appears | a test file not listed reaches ≥ 120 s in `.test_durations` | exit 0: the family is a `report` row (#931), so its summary line reads `over` and the list of report rows past their band names the file |
```
```markdown
  3. The suite's seconds and each slow file are read off one run's
     `.test_durations`, so each has a ceiling 1.3 times its reading with no
     lower band. The suite's seconds are a gate. A slow file is a report,
     because one union moves a single file 0.67 to 1.72 times the level
     from the next. A refresh restates one number, its price level, rather
     than every seconds ceiling, so a refresh on faster or slower runners
     fails nothing, and a cleanup of one file moves only that file.
  4. Each leg's minutes are read off the run itself by a `budgets` job
     after the suite, held to a ceiling with no lower band, and printed with
     the run's billable minutes, priced at a figure the line says to check
     against GitHub's price list.
  5. Three reports fail nothing: each slow test file, the largest round
     records in the tree, and how many rows a release re-read. A release
     pull request prints every budget against the last release tag.
```
```python
    noted = [
        (result.row.name, problem)
        for result in results
        if result.row.kind == REPORT
        for problem in result.problems
    ]
    if noted:
        lines += ["", "Report rows past their band, failing nothing:", ""]
        lines += [f"- `{name}`: {problem}" for name, problem in noted]
```
```python
def test_an_unlisted_slow_file_under_a_report_row_is_named(tmp_path, capsys):
    """S7 under the kind this repository gives the family: a test file that
    crosses the threshold unlisted fails nothing, and the summary names it,
    because the family's own line reads only the largest unlisted value."""
    head = budgets(("slow-file", "seconds", 120, "one-sided", "report")) + table(
        "Seconds ceiling", []
    )
    root = tree(tmp_path, head, files={".test_durations": json.dumps(SMALL)})
    assert run(root) == 0
    out = capsys.readouterr().out
    assert "Report rows past their band, failing nothing:" in out, out
    assert (
        "- `slow-file`: tests/test_a.py is not listed and measures 130 seconds"
        in out
    ), out
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` over the four modules plan row 4 names | exit 0, 415 passed, 2 skipped |
| `bin/test` over line wrap, changelog gathering, no real identifiers, one word one meaning | exit 0, 116 passed |
| run 38655519975's union over `.test_durations`, `python3 .github/scripts/budget_check.py --baseline origin/release/v0.22.0 --restate-price` | exit 1; wrote 1136 per mille, one line of `seal/budgets.md` changed; 20 `Budget removed:` problems; reverted |
| the same with `--pr-body-env` holding PR #937's body | exit 0, "every gate row holds"; reverted |
| T8 against 9021bc49's `REMEDY` with the new assertion | exit 1 at the whole-command assertion; file restored |
| `expected_level`'s `return` given `+ 1`, the writer's and the check's cases | exit 1, 3 failed; file restored |
| 300 s added to one case of `tests/test_docs_line_wrap.py`, checker with no baseline | exit 0; `slow-file` line `266 seconds (largest unlisted)`, `report`, `over`; no path printed; reverted |
| 🟡 3's fix and case in the clone | with the fix: exit 0, 236 passed over two modules, and the probe above names the file; without it: the case exits 1 |
| the full suite, lint and typecheck at a6919ade | not yet — not this round's to run; the sealer runs it once the rounds settle |

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

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
