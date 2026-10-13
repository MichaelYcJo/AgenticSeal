# 1791852613-the-test-durations-are-refreshed-and-say-when-next — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 3d2324ce |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

Read measuring run 38332345615 (`workflow_dispatch` at `9ec6faca`). Find the
cause of each failing job yourself, and do not assume a red job was the
expected red. Read the Windows job's time and summary line. Download
artifact `test-durations` into a scratch directory, convert it to LF, and
check the unpriced count against the collection. Commit the file in one
commit with `test.yml` restored byte for byte to its shape before the
measuring commit. Fill the Status cell. Fill `Ran by` here and in
`phase-1.md` as `specseal:smith on Opus 5.5`. Then stop and hand back the
second push and dispatch. Run anything slow under
`SPECSEAL_CASE_CEILING_S=600`.

## What this phase found

**The run, read with `gh run view 38332345615 --json jobs` and each job's
log (executed 2026-10-13).**

| Job | `startedAt` → `completedAt` | Summary line | Why it is red |
|---|---|---|---|
| Windows, `--store-durations`, 55 | 01:29:13 → 02:06:34, **37 m 21 s** | `4 failed, 13251 passed, 225 skipped in 2210.75s (0:36:50)` | the census case (below), the two shard cases, the staleness case |
| ubuntu, 15 | 01:29:13 → 01:38:56, 9 m 43 s | `4 failed, 13395 passed, 81 skipped in 568.22s` | the same four |
| macOS group 1, 15 | 01:29:17 → 01:33:46, 4 m 29 s | `1 failed, 6475 passed, 9 skipped in 253.57s` | the census case only |
| macOS group 2, 15 | 01:29:21 → 01:37:03, 7 m 42 s | `3810 passed, 75 skipped in 436.17s` | green |
| macOS group 3, 15 | 01:29:18 → 01:37:47, 8 m 29 s | `3 failed, 3102 passed, 5 skipped in 489.50s` | the two shard cases and the staleness case, which the old file puts in group 3 |

Windows ran 13,251 + 225 + 4 = 13,480 cases, the local collection's count.
The macOS groups ran 6,485 + 3,885 + 3,110 = 13,480 between them (failed
plus passed plus skipped), and ubuntu ran 4 + 13,395 + 81 = 13,480.

**A red phase 1 left, and it was not one the plan expected.**
`tests/test_a_reader_declares_its_input_class.py::test_every_unit_of_shipped_python_declares_or_is_on_the_census`
failed on every job whose group held it: *"tests/conftest.py#pytest_collection_modifyitems
(line 1007) declares no input class"*. Phase 1's narrow run did not cover
the census module. `12571941` adds `Reads: observed — the items pytest
collected, recorded unjudged; unknown passed` to the hook's docstring. Its
red is this run's log, and its green is
`bin/test tests/test_a_reader_declares_its_input_class.py …` below.

**The Windows staleness case read 1,063, not 1,276.** Ubuntu and macOS
group 3 read 1,276 of 13,480. Windows read 1,063 (7.9 %) under
`--store-durations`. This is a race inside the measuring run, and it does
not happen in a normal run. `pytest-split` 0.11.0 registers
`PytestSplitCachePlugin` in every process that sees the option, so each
xdist worker writes the file at its own `pytest_sessionfinish`, and the
controller writes it last (`read` from the wheel, `plugin.py` lines 103–113
and 188–222). A worker that finished early had already merged its results
into the file before the staleness case read it. The committed file is the
controller's, written after every worker had finished.

**The recipe merges, and does not replace.** Without `--clean-durations`,
`pytest_sessionfinish` updates the file it loaded at start. The download has
14,105 entries: 13,480 measured by this run, which is every Windows node id,
plus 625 old entries carried over unchanged. The frame's "838 dead" were
603 gone cases and 235 Windows-form ids. `spec.md` Out forbids editing the
file by hand, so the 625 stay. They are noted in `overview.md`.

**Zero unpriced does not hold on POSIX, and nothing in this recipe can make
it hold.** The local collection has 213 node ids that are not in the file
(1.58 %): 170 in `test_a_moved_rule_leaves_its_definition.py`, 25 in
`test_every_agent_reads_the_contract.py`, 8 in
`test_the_seal_is_taken_once_by_the_sealer.py`, 7 in
`test_unverified_rows_close.py`, 2 in
`test_local_mode_resolves_under_the_git_dir.py` and 1 in
`test_the_contributor_has_a_procedure.py`. Each is a parametrized case whose
id carries a path. Windows writes `[agents\\framer.md-10]` and POSIX writes
`[agents/framer.md-10]`. The Windows shards price them, and ubuntu and
macOS give them the mean. That share sits under every POSIX reading of the
case, so on those legs the room before `STALE_SHARE` is 3.4 points, not 5.
Recorded for whoever revisits Q1. Whether these 213 cases skew a macOS
group is phase 3's reading.

**The file, before and after, counted against the 13,480-case collection by
a script in the session's scratch directory (executed).**

| | Bytes | Entries | Seconds | Unpriced | Not collected on POSIX |
|---|---|---|---|---|---|
| At `4ce7b710` | 1,996,254 | 13,042 | 7,530.0 | 1,276 (9.47 %) | 838 |
| At `3d2324ce` | 2,152,902 | 14,105 | 9,065.7 | 213 (1.58 %) | 838 (625 carried over, 213 live on Windows) |

The download was 2,167,008 bytes with 14,106 CRLF line ends. The
conversion script asserted that a CRLF was present, that no bare CR was
left, that the length dropped by exactly the CRLF count, and that the parsed
JSON was unchanged. The result is 2,152,902 bytes, which `file` reports as
`ASCII text`. Its keys are sorted, and it has no trailing newline, the same
as the old file.

**Verified at `3d2324ce`'s tree, exit codes read directly (executed
2026-10-13, `SPECSEAL_CASE_CEILING_S=600`).**

- `git diff --quiet 4ce7b710 -- .github/workflows/test.yml`: exit 0. The
  workflow is byte for byte its shape before the measuring commit.
- `bin/test tests -q -k test_the_durations_file_prices_the_suite`: exit 0,
  `1 passed in 12.32s`.
- `bin/test tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py
  tests/test_a_reader_declares_its_input_class.py
  tests/test_a_slow_case_names_itself.py
  tests/test_ci_gives_the_checks_what_they_need.py
  tests/test_a_workflow_is_read_the_one_way.py -q -rs`: exit 0,
  `124 passed, 1 skipped`. The skip is the suite case, with its reason.
- `mutation-check tests/conftest.py --replace "…[item.nodeid for item in
  items])" "…[])" --tests "bin/test tests -q -p no:xdist -k
  test_the_durations_file_prices_the_suite"`: `red` (ValueError *an empty
  collection*). With the suite case green, the hook could now be broken
  through the tool, which was not possible in phase 1.
- `uvx ruff check` / `ruff format --check tests/conftest.py`: exit 0.

**Unverified, and who answers it.** The whole suite: the sealer. Whether
every shard on GitHub is green at `3d2324ce`, and whether the hook reads the
whole collection there (Q4): the post-refresh run, read in phase 3.
