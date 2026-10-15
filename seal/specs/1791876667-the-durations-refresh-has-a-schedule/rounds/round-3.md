# 1791876667-the-durations-refresh-has-a-schedule — review round 3

| Field | Value |
|---|---|
| Target SHA | e14cdff4fd89b41f68f1292e16ce2b227dc39956 |
| Written late | no |
| Ran by | specseal:warden on claude-opus-5-5 |
| PR | #937 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are written and no round has opened them |
| Fix range | `5c93835ea279898eb9e5a5ea3602164f3dfec6b0..2ce9df3341490229b66f5dc2b713639662c338aa`, 3 commits |
| Contract changes | check → main, check, spec.md, 6-tests.md, 7-records.md, plural, pytest |
| New units | restate_price (depth 1); test_a_slow_file_is_reported_and_the_suite_seconds_are_gated (depth 1); test_restate_price_writes_the_level_a_refresh_implies (depth 1); test_restate_price_with_nothing_to_restate_against_or_into_is_exit_2 (depth 1) |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1, the refresh recipe and `REMEDY` omit the price level and the `slow-file` rows the refresh commit is refused for; 🟡 2, the `slow-file` band does not hold a union refresh's spread (a decision between forms (a) and (b), and which branch carries it). |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Round 3 of #931 after its rebase onto #944 (5b1f6fae): the conflict resolutions, the cleanup commit e14cdff4, the design on the new tree (a union that moves the price level; --clean-durations through the union), the spec's retention divergence, and whether rounds 1 and 2's fixes hold by content. Narrow checks only.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | the refresh recipe and `REMEDY` end at "commit it", and the hygiene budget step refuses that commit: for the price level on every refresh, and for a `slow-file` row on every refresh measured; neither text names either step | `CONTRIBUTING.md:177` | **fixed** `2ce9df33` | fixed at 2ce9df33; executed: run 38655519975's union over the tip's file, `budget_check.py --baseline 5b1f6fae` exit 1 naming level 1136 and unlisted `tests/test_worktree_guard.py` at 124 s; with 1136 written, still exit 1 on that file; `REMEDY` at `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:279` read |
| 🟡 2 | a union refresh moves single test files 0.67–1.72 times the level, past the 1.3 one-sided `slow-file` band that was set from one refresh's 0.76–1.14, so every refresh needs `Budget raised:` lines for files nobody changed | `.github/scripts/budget_check.py:91` | **fixed** `e16fcabb` | fixed at e16fcabb; executed: eight pairs through `price_level`; one unsharded pair 0.80–1.19 with none over; seven union refreshes each trip a `slow-file` row, two of them run through the gate; the choice between (a) and (b), and which branch carries it, is the orchestrator's |
| ⬜ 3 | `spec.md` Data & interfaces says parts are kept 1 day; the code keeps them 7 with `overwrite: true`, and `overview.md` has no divergence row | `seal/specs/1791876667-the-durations-refresh-has-a-schedule/spec.md:58` | open | read: `.github/workflows/test.yml:176`, `:209`; round 1's finding 1 decided seven days |
| ⬜ 4 | the changelog and overview say the `budgets` job names the price level; that job runs `--ci-jobs`, which keeps only `ci-minutes` rows | `seal/specs/1791876667-the-durations-refresh-has-a-schedule/changelog.md:40` | open | read: `.github/scripts/budget_check.py:1341-1351`; the step that names it is `.github/workflows/hygiene.yml:175-184`; `overview.md:43` says the same |
| 🟢 | the rebase's conflict resolutions mean what both sides mean: nothing #944 removed came back, and the job count, recipe, budgets row and checklist hold | `.github/workflows/test.yml`, `CONTRIBUTING.md:135`, `seal/budgets.md:85` | confirmed | executed: `budget_check.py --baseline 5b1f6fae` at the tip, exit 0; read: the diff against 5b1f6fae, `git grep` for the old recipe |
| 🟢 | e14cdff4 rewrites the live records in place and leaves history records as history | `seal/specs/1791876667-the-durations-refresh-has-a-schedule/` | confirmed | read: `git show e14cdff4`; phases and rounds untouched |
| 🟢 | round 1's finding 1 is closed — parts and union kept seven days with `overwrite: true` | `.github/workflows/test.yml:168-176` | confirmed | read at e14cdff4; the two cases assert both keys and pass (executed) |
| 🟢 | round 1's finding 2 is closed — the dispatch for a branch with no run | `CONTRIBUTING.md:183-185` | confirmed | read at e14cdff4: `REMEDY` and the recipe both carry it |
| 🟢 | round 1's finding 3 is closed — pytest read as a word on every code line but `needs:` | `tests/test_ci_gives_the_checks_what_they_need.py:328` | confirmed | executed: the module passes; the `budgets` job is not selected |
| 🟢 | round 1's finding 4 is closed — a `--count` below one is refused | `.github/scripts/durations_union.py:234` | confirmed | read at e14cdff4; its case passes (executed) |
| 🟢 | round 2's finding 5 stays answered with grounds | `tests/test_ci_gives_the_checks_what_they_need.py#runs_pytest` | confirmed | read: no job on the rebased tree has the shapes it names; `budgets` uses the one-line `needs:` |
| 🟢 | `--clean-durations` through the union drops what the unsharded run dropped: the union is the collection | `.github/workflows/test.yml:94` | confirmed | executed: union of run 38655519975 holds 9,242 entries; the collection is 9,242 |

## Paste-ready fixes

```markdown
To refresh the file, take the artifact from your branch's latest `tests`
run: `gh run download <run id> -n test-durations -D <dir>`, then move
`<dir>/.test_durations` over the committed file and commit it. Its line
ends are already LF. The download goes to a directory of its own because
`gh` will not write over a file that is already there. A run older than
seven days is re-run first, with `gh run rerun <run id>`. A branch with no
pull request has no `tests` run until one is dispatched, and neither has a
branch whose run is too old to re-run:
`gh workflow run test.yml --ref <branch>` starts one. A new file moves
the prices `seal/budgets.md` reads it at. In the same commit, write the
`## Price level` the `durations` job's summary names, and answer each
`slow-file` row it names over its ceiling, as the hygiene workflow's
budget step will ask.
```
```python
    "<branch>` (CONTRIBUTING.md §Running the checks). In the same commit, "
    "write the `## Price level` the `durations` job's summary names in "
    "seal/budgets.md, and answer each `slow-file` row it names, with a "
    "`Budget raised:` line where one is asked."
)
```
```yaml
      # What committing the union asks of `seal/budgets.md`, before anyone
      # commits it (#931): the price level the refresh moves, and any
      # `slow-file` row its prices put over a ceiling. `--baseline HEAD`
      # reads the committed file as the base and the union as the tree,
      # which is the verdict the refresh's pull request gets. Exit 1 is that
      # preview and leaves the job green; exit 2 is a checker that could not
      # read the tree, and fails it.
      - name: what committing the union asks of seal/budgets.md
        shell: bash
        run: |
          cp union/.test_durations .test_durations
          set +e
          python .github/scripts/budget_check.py --baseline HEAD
          code=$?
          [ "$code" -le 1 ] || exit "$code"
```
```python
        if any(row.name.partition(":")[0] in PRICED for row in head):
            text = blob_at(root, base, DURATIONS, against)
            before = (
                None
                if text is None
                else durations_from(text, f"{DURATIONS} at {against}")
            )
            here = durations(root)
            ratio, common = price_level(before, here, against)
            cache["price"] = (ratio, common)
            # A refresh re-prices the suite and does not grow it (#931): one
            # union moves single files 0.67 to 1.72 times the level from the
            # next, past the 1.3 band, so where the file moved against the
            # base its `slow-file` rows are shown and not gated.
            cache["refreshed"] = before is not None and before != here
            priced = price_problems(base_level, ratio, common, level)
    for row in head:
        try:
            results.append(measured_row(root, row, names, cache))
        except Unreadable as error:
            refusals.append(str(error))
    refreshed = cache.get("refreshed", False)
    problems = priced + [
        (r.row.name, p)
        for r in results
        if r.row.kind == GATE
        and not (refreshed and r.row.name.partition(":")[0] == "slow-file")
        for p in r.problems
    ]
```
```markdown
| Part retention | `spec.md` Data & interfaces: "Parts retained 1 day, the union 7" | parts and union both `retention-days: 7`, uploaded with `overwrite: true` | round 1's finding 1: re-running failed jobs re-runs the `durations` job, which reads every part again, so a part is kept as long as the union it makes |
```
```markdown
    on, so no scaling is applied to the union. A pull request that commits
    a union restates `## Price level` in `seal/budgets.md` to the number the
    hygiene workflow's budget step names for it.
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` on the six touched modules (`test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, `test_ci_gives_the_checks_what_they_need.py`, `test_docs_line_wrap.py`, `test_release_hygiene.py`, `test_the_contributor_has_a_procedure.py`, `test_a_budget_ratchets.py`) | exit 0: 309 passed, 2 skipped |
| `bin/test tests -q -k test_the_durations_file_prices_the_suite -p no:xdist` | exit 0: 1 passed, 9241 deselected |
| `budget_check.py --baseline 5b1f6fae` at the tip, unmodified | exit 0: every gate row holds |
| the same, with run 38655519975's union over `.test_durations` | exit 1: level 1136; unlisted `tests/test_worktree_guard.py` 124 s |
| the same, with `## Price level` at 1136 | exit 1: `tests/test_worktree_guard.py` 123 s |
| the same, with run 38523258950's union (the 21 files #944 deleted taken out) | exit 1: level 1088; two listed rows over |
| the same, with `## Price level` at 1088 | exit 1: the same two rows, 263 over 224 and 174 over 157 |
| `budget_check.py --baseline HEAD` with that union in the working tree | exit 1: the same three lines as against the base |
| `test_tmp_spread.py` over the eight pairs in §3 | exit 0: the table in §3 |
| the full suite, lint and typecheck at the tip | not yet: the sealer's, after the rounds settle |

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

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
