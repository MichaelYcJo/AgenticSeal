# 1791852613-the-test-durations-are-refreshed-and-say-when-next — review round 2

| Field | Value |
|---|---|
| Target SHA | 808dc814b3ba7e0b3b914cb26f7c7bcb2681e7e5 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #924 |
| Broad gate | not yet |
| Fixes checked by | no fixes to check |
| Fix range | none |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | no |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Round 2 of #874, the verifying round, target 808dc814: the diff of round 1's fixes, `744c610f..dfd51a66`, including a measuring commit that the next one reverts and the second refreshed file from run 38342987499. The reviewer was asked whether 🟡 1 and 🟡 2 are closed, to treat `posix_id`, `interpreter_free` and the two new cases as a finding surface, and to check the refreshed file's claim of no unpriced case on POSIX and on Windows.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 1's finding 1 is closed — every test id is one spelling, and the refreshed file prices the whole collection on every leg | `tests/conftest.py:1024` | confirmed | executed: 13,482 collected, 13,482 keys, 0 unpriced, 0 not collected; the artifact of run 38342987499 equals the committed file once its CRs are removed; Windows by the key set, which `--clean-durations` makes the Windows collection |
| 🟢 | round 1's finding 2 is closed — the release box re-reads the macOS budget after a refresh | `docs/release-checklist.md:61` | confirmed | read: the sentence and its citation of `CONTRIBUTING.md` §*Running the checks*; executed: `evidence-check --strict .` exit 0 |
| 🟢 | the measuring commit is reverted byte for byte | `.github/workflows/test.yml` | confirmed | executed: `git diff 34d1d1e8^ c59c7664 -- .github/workflows/test.yml` is empty |
| 🟢 | the interpreter case is seen red with the fix removed (new unit, depth 1) | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:232` | confirmed | executed: 8 ids red, then green restored; read: it cannot fail on Windows, where pytest doubles each backslash in an id, and ubuntu and macOS refuse the class on every pull request |
| 🟢 | `posix_id`, `interpreter_free` and the forward-slash case (new units, depth 1) | `tests/conftest.py:1024` | confirmed | read: non-strings return None; executed: the touched modules pass and ruff passes on the eight files |
| ⬜ 1 | three in-place rewrites left their paragraphs unwrapped: a 106-column docstring line, two half lines in `CONTRIBUTING.md` (195, 209) and one in `docs/release-checklist.md` (65) | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:12` | open | read; the same class as round 1's ⬜ 4; `tests/test_docs_line_wrap.py` passes |
| ⬜ 2 | the heading says the path half is held on Windows; no leg refuses a path id written with a backslash, and ubuntu and macOS only count it as unpriced | `seal/specs/1791852613-the-test-durations-are-refreshed-and-say-when-next/overview.md:38` | open | read: the paragraph's body is correct; a correction to the run's paperwork |

## Paste-ready fixes

no paste-ready fix in the report

## Executed probes

| What was run | Result |
|---|---|
| `bin/test tests --collect-only -q -p no:xdist -p no:cacheprovider`, compared with `.test_durations` by a script outside the tree | exit 0; 13,482 collected; 13,482 keys; 0 unpriced; 0 not collected; no id holds `sys.executable`; 1,339 keys carry an escaped backslash |
| `gh run view 38342987499 --json headSha,jobs` and the Windows job's log | head `3e915950`; Windows job 03:50:16 to 04:24:31; `2 failed, 13255 passed, 225 skipped in 2014.50s` |
| `gh run download 38342987499 -n test-durations`, CRs removed, `cmp` against the committed file | identical; 13,483 CRLF in the artifact |
| `git diff 34d1d1e8^ c59c7664 -- .github/workflows/test.yml`; `git diff --stat 3e915950 808dc814 -- tests .github` | empty; only `test.yml` |
| `bin/test` on the shard module, `test_a_moved_rule_leaves_its_definition.py`, `test_every_agent_reads_the_contract.py`, `test_the_contributor_has_a_procedure.py`, `test_docs_line_wrap.py`, `test_local_mode_resolves_under_the_git_dir.py`, `-q -p no:cacheprovider -rs` | exit 0, `294 passed, 2 skipped`, both skips naming the `-k` form |
| `bin/test` on `test_the_seal_is_taken_once_by_the_sealer.py` and `test_unverified_rows_close.py`, `-k` the four parametrizations given new ids | exit 0, `24 passed` |
| The three `ids=interpreter_free` lines removed in the clone, `bin/test tests -q -k` the interpreter case and the durations case | exit 1, `1 failed, 1 passed`, 8 ids named; restored, exit 0, `2 passed` |
| `uvx ruff check` and `uvx ruff format --check` on the eight touched test files | exit 0 both |
| `python3 skills/evidence-check/scripts/evidence_check.py --strict .` | exit 0, `0 refused · 0 drifted` |
| The whole suite at `808dc814` (broad gate) | not yet: the sealer's, once, now that the rounds have nothing open to fix |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:56` | round 1's 🟡 1 — fixed |
| round-1 | `docs/release-checklist.md:55` | round 1's 🟡 2 — fixed |
| round-1 | `seal/ledger/1791852613-the-test-durations-are-refreshed-and-say-when-next.md:7` | round 1's ⬜ 3 — open |
| round-1 | `.github/workflows/test.yml:45` | round 1's ⬜ 4 — open |
| round-1 | `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#collects_the_suite` | round 1's 🟢 — confirmed |
| round-1 | `tests/conftest.py#pytest_collection_modifyitems` | round 1's 🟢 — confirmed |
| round-1 | `.test_durations` | round 1's 🟢 — confirmed |
| round-1 | `.github/workflows/test.yml:51` | round 1's 🟢 — confirmed |
| round-1 | `seal/ledger/1791852613-the-test-durations-are-refreshed-and-say-when-next.md` | round 1's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| A path parametrization that omits `ids=posix_id` is refused on no leg; it shows only as unpriced on ubuntu and macOS after the next refresh | `overview.md` §*Not done*, written by the fix pass | the orchestrator, who decides whether it becomes an issue |
