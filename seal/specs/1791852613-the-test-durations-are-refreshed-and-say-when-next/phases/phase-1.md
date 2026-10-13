# 1791852613-the-test-durations-are-refreshed-and-say-when-next — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | e4c84963 |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Build phase 1 of `plan.md` from the committed frame, and stop at the push.
Commit A: the `conftest.py` hook that records the collection, `STALE_SHARE =
0.05` (Q1 approved as written), the pure arithmetic, the suite case
`test_the_durations_file_prices_the_suite` with its fixture cases at the
boundary, the `CONTRIBUTING.md` sentence, and the `docs/release-checklist.md`
§0 box (Q5 approved as written). Every new case seen red first, the suite
case's red being the real tree's share. Commit B: `test.yml` in the recipe's
measuring shape and nothing else. Verify the phase by its own command with
exit codes read directly, then hand back. The orchestrator pushes and
dispatches the measuring run; the smith does neither.

## What this phase found

**Three commits, not two.** A is `4ce7b710`. `f2ae0092` drops a
`split("::")` from `collects_the_suite`: no argument carrying `::` can name
the repository or its `tests` directory, so the split decided nothing and a
mutation of it could not go red. B is `e4c84963`, and the branch's tip at
dispatch is the commit that adds this record, whose `test.yml` is B's.

**The frame's decline rule would have declined under the sealer's run.**
`plan.md` §*Declining a partial collection* reads
`session.config.invocation_params.args` and skips when no argument resolves
to `tests`. This repository's `Broad gate` row in `seal/config.md` is
`bin/test -q`, which hands pytest no path at all, so that rule would have
skipped the case in the one local run of the whole suite. The case reads
`config.args` instead: pytest fills it with the invocation directory when no
path was named, so `bin/test -q` from the root counts as the suite, and
`collects_the_suite` also requires `config.rootpath` to be the repository's,
which is what makes node ids start `tests/`. Executed: `bin/test -q -k
test_the_durations_file_prices_the_suite` ran the case (red, 1 failed, exit
1) rather than skipping it. Also recorded in `overview.md`.

**The arithmetic is two functions, not one.** `unpriced(collected,
durations)` returns the ids the frame named; `staleness(collected,
durations)` holds the share comparison and the sentence, so the fixture
cases pin the boundary on the function the suite case calls. The boundary is
derived from `STALE_SHARE` on a thousand cases (50 passes, 51 fails at 0.05),
so overturning Q1 moves the fixtures with it.

**The artifact is named `test-durations`.** The recipe names no artifact;
`actions/upload-artifact@v4`'s default would be `artifact`. Phase 2
downloads with `gh run download <id> -n test-durations`.

**At B, two shard cases are red, both expected.** `test_every_group_of_each_
sharded_leg_runs_exactly_once` ("a windows-latest leg that is not a shard")
and `test_the_pytest_line_hands_the_split_to_pytest` (the line now ends in
`${{ matrix.store }}`). The recipe's *the shard cases … fail* covers both.
The staleness case is red on every leg of the measuring run as well, so
every pytest job of that run is red; `always()` is what uploads the file.

**The ledger drift is wider than the plan's ledger paragraph.** 0.21.0's
re-read rows of 0.20.0's S9 (`seal/releases/0.21.0.md`, the two `Re-read ·
S9` rows) anchor `CONTRIBUTING.md#"## Running the checks"@7b26acf8`, the
whole section, which the new sentence moves. Phase 3's `--reverify --into`
owes that anchor a re-read too, beside `test.yml#"pytest:"`. The plan named
nothing for `docs/release-checklist.md`, and the box drifts a family of five
rows anchored on `docs/release-checklist.md#"## 0. Before starting"`; those
are owed re-reads as well. The two quoted lines (`ubuntu, macOS and Windows
at the floor…`, `Windows and macOS shards and drops no case…`) were not
rewrapped, so no `Corrected ·` row is owed for them. Executed at B,
`python3 skills/evidence-check/scripts/evidence_check.py .`: exit 1, the
lenient reading, with exactly two DRIFTED lines, those two headings, and
nothing BROKEN.

**Seen red (§15), executed 2026-10-13.**

- The suite case on this tree at A, `bin/test tests -q -k
  test_the_durations_file_prices_the_suite`, exit 1, 1 failed in 34.98 s:

  ```
  AssertionError: 1276 of the 13480 collected cases (9.5%) have no price in
  .test_durations, over the 5% STALE_SHARE allows: pytest-split gives each
  the file's mean, which unbalances the Windows and macOS shards. Refresh the
  file by the recipe in CONTRIBUTING.md §Running the checks. First unpriced:
  tests/test_a_corrected_sentence_survives_elsewhere.py::test_a_ledger_row_below_an_issue_led_line_keeps_its_heading, …
  ```

  1,276 is the frame's 1,270 plus this phase's six new cases; 13,480 is the
  frame's 13,474 plus the same six.
- Under `pytest-split` (S3), the `uvx` form of `plan.md` with
  `--splits 3 --group k`: group 1 exit 1, `1 failed, 13479 deselected`, the
  same 1,276 of 13,480 — the whole suite, not the group's third; groups 2
  and 3 exit 5, `13480 deselected`. Exactly one group runs the case, and it
  reads the whole collection. `bin/test tests -q -k …` above ran under
  `-n auto`, so an xdist worker's record is the whole suite too.
- One module named, `bin/test
  tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py -q -rs`:
  exit 0, `8 passed, 1 skipped`, the skip reason *the suite was not
  collected, so its collection cannot be read against .test_durations; run
  `bin/test tests -q -k test_the_durations_file_prices_the_suite` from the
  repository*.
- Each new unit broken once through `mutation-check`, every verdict `red`
  (exit 0), on `f2ae0092`'s tree:

  | Break | Case that went red |
  |---|---|
  | `share <= STALE_SHARE` → `<` | `test_exactly_the_share_unpriced_passes` |
  | `share <= STALE_SHARE + 0.001` | `test_one_more_unpriced_fails_and_names_the_counts_and_the_recipe` |
  | `if not collected` → `if collected is None` | `test_an_empty_collection_is_refused` |
  | dead entries added to the unpriced list | `test_an_entry_nobody_collects_is_not_counted` |
  | `CONTRIBUTING.md §Running the checks` dropped from the sentence | `test_one_more_unpriced_fails_and_names_the_counts_and_the_recipe` |
  | the rootdir test → `if False:` | `test_only_the_suite_or_the_repository_is_the_whole_collection` |
  | `tests` dropped from the whole set | the same |
  | the repository dropped from the whole set | the same |
  | a matching argument returns False | the same |

  The hook itself was not broken through `mutation-check`: the only case
  that reads it is the suite case, red at baseline until phase 2, so the
  tool stops at `no baseline`. Its evidence is the group-1 run above, which
  read 13,480 cases inside a third of them.

**Verified at the phase's boundary, executed 2026-10-13, exit read
directly.** At A: the plan's five modules, `bin/test
tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py
tests/test_a_slow_case_names_itself.py
tests/test_ci_gives_the_checks_what_they_need.py
tests/test_a_workflow_is_read_the_one_way.py tests/test_docs_line_wrap.py -q
-rs`, exit 0, `86 passed, 1 skipped`; the eleven modules that read
`CONTRIBUTING.md` or `docs/release-checklist.md` by name for wording, wrap,
identifiers or duplicated passages, exit 0, `449 passed, 7 skipped`; `uvx
ruff check` and `uvx ruff format --check` on the two changed modules, exit 0.
At B: the same five modules, exit 1, `2 failed, 84 passed, 1 skipped`, the
two failures being the shard cases named above; the workflow parses under
PyYAML with one Windows entry, `timeout: 55`, and the upload step last.

**Unverified, and who answers it.** The whole suite: the sealer, once,
after the rounds. Whether the measuring run finishes inside 55 minutes and
uploads the file: the run the orchestrator dispatches, read in phase 2.
