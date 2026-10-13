# Round 2 report — 1791852613-the-test-durations-are-refreshed-and-say-when-next (#874)

| Field | Value |
|---|---|
| Target | `chore/874-the-test-durations-are-refreshed-and-say-when-next` at `808dc814`; the fix diff `744c610f..dfd51a66`, 8 commits |
| Kind | the verifying round: it answers round 1's two findings and judges the units the fixes created |
| Where it ran | a `git clone --no-local` of the worktree at `808dc814`, under `<scratchpad>/1791852613/round-2/clone`, removed at handover |
| Ran by | specseal:warden on claude-opus-5-5 |
| Load | every `bin/test` call ran with `SPECSEAL_CASE_CEILING_S=600` |

Round 1's record and report were read for coordinates. Its two findings are
answered below on this round's own grounds, and its two notes (⬜ 3, ⬜ 4)
are carried open under `## Inherited coordinates` and not reported again.
The commit messages, the ledger fragment, `overview.md` and the spawn
prompt were read as the implementer's account. Each claim this report
relies on was checked against the clone, the measuring run on GitHub, or
the artifact it uploaded.

## How the findings relate

```
fa4e9cce: every test id is one spelling (posix_id, interpreter_free)
        |
        +--> run 38342987499 measures the file again with --clean-durations
        |        +--> round 1's finding 1 closed: 0 of 13,482 unpriced, executed
        |
        +--> the in-place rewrites leave three ragged wraps     ⬜ 1
        |
        +--> the path half has no guard on any leg; overview.md's
             heading says Windows holds it                       ⬜ 2 (paperwork)

0b71b66d: the release box re-reads the macOS budget
        +--> round 1's finding 2 closed, read
```

Nothing this round found needs a fix.

## Round 1's finding 1 is closed: the refreshed file prices the whole collection on every leg

The claim was that every test id is now one spelling on every machine, so
a file measured on Windows prices every collected case on ubuntu and macOS
too. Each part was checked.

- **The collection matches the file exactly (executed).** `bin/test tests
  --collect-only -q -p no:xdist` in the clone collected 13,482 ids. A
  script outside the tree compared them with the keys of `.test_durations`:
  13,482 keys, 0 collected ids unpriced, 0 keys the suite does not
  collect. No collected id holds `sys.executable`.
- **The file is the run's own output (executed).** The artifact
  `test-durations` of run 38342987499, downloaded with `gh run download`,
  has 13,483 CRLF line ends. With the CRs removed it is byte for byte the
  committed `.test_durations`. The run's head is `3e915950`. Its Windows
  job ran from 03:50:16 to 04:24:31 (34 m 15 s) and its log ends
  `2 failed, 13255 passed, 225 skipped`. Those are the 13,482 ids.
- **Windows is priced by construction (read, from the executed facts
  above).** `--clean-durations` writes only the ids the Windows run
  collected, and that key set equals the POSIX collection. So at this tree
  Windows collects the same 13,482 ids, and none is unpriced there either.
  The prompt called this "derived from the count, not listed". It is now
  listed: the key set is the Windows list.
- **No test changed after the measuring run (executed).**
  `git diff 3e915950 808dc814 -- tests .github` touches only `test.yml`.
- **The measuring commit is gone (executed).**
  `git diff 34d1d1e8^ c59c7664 -- .github/workflows/test.yml` is empty.
- **The three sentences were rewritten in place (read).** The `STALE_SHARE`
  comment, `CONTRIBUTING.md:191` and the module docstring now state the
  one-spelling rule instead of the false ground. The recipe at
  `CONTRIBUTING.md:207` names `--clean-durations` and says why. No other
  copy of the recipe in a policy document names `--store-durations` (grep
  over `.md`, `.yml` and `.py`; `spec.md` and `plan.md` still show the
  frame's spelling, and `overview.md` records the divergence).

## Round 1's finding 2 is closed: the release box re-reads the macOS budget

`docs/release-checklist.md:61` now tells the release to read the release
pull request's macOS shard times and set their `timeout` by the rule beside
the values, citing `CONTRIBUTING.md` §*Running the checks*. That is the
step round 1 found missing (read). The ledger row S4 re-anchors the
checklist at `3515a27d`, and `evidence-check --strict .` exits 0 (executed).

## The new units hold

- **`test_no_collected_id_carries_the_interpreters_path` is seen red
  (executed).** With the three `ids=interpreter_free` lines removed in the
  clone, `bin/test tests -q -k "test_no_collected_id_carries_the_interpreters_path
  or test_the_durations_file_prices_the_suite"` exited 1 with
  `8 collected ids carry <clone>/.venv/bin/python`. Restored, the same
  command exited 0, `2 passed`. That matches the 8 the ledger row claims.
- **That case cannot fail on Windows, and this costs nothing (read).**
  pytest passes an `ids=` function's return through its own escaping
  (pytest 9.1.1: its function-id path returns through its value path),
  which doubles every backslash. On Windows the
  interpreter's path has backslashes, so `sys.executable in node` never
  matches there. The ubuntu and macOS legs run the case on every pull
  request and see the plain path, so the class is still refused before it
  merges. Recorded as a confirmation, not a finding.
- **`posix_id` (read and executed).** It rewrites only strings and
  returns None otherwise, so pytest keeps its own id for other values.
  `test_a_path_id_is_written_with_forward_slashes` fails if the body
  returned the value unchanged (read). The five path parametrizations it
  serves, and the three `interpreter_free` ones, pass their modules
  (executed, below). `ruff check` and `ruff format --check` pass on the
  eight touched test files (executed, narrow).

One hazard was looked for and not found. `posix_id` is passed to
`test_the_documents_state_the_merge_base_footing`, whose three arguments
include prose. On Windows any backslash in that prose would become `/`,
and the id would then differ from POSIX. The executed key-set equality
shows no current value does this.

## ⬜ 1 — the in-place rewrites left three ragged wraps

`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:12` is
106 columns wide in a docstring wrapped at about 76. `CONTRIBUTING.md:195`
and `CONTRIBUTING.md:209` are left half-length, and so is
`docs/release-checklist.md:65`. Each is a sentence rewritten in place
without rewrapping the paragraph. This is round 1's ⬜ 4 again, at new
coordinates. The behaviour and every fact stay right, and
`tests/test_docs_line_wrap.py` passes, so it is ⬜. The fix is to rewrap
the four paragraphs.

## ⬜ 2 — `overview.md` says Windows holds the path half, and no leg does

The prompt carried the implementer's note that a new path parametrization
which forgets `posix_id` "is caught only on Windows". The heading at
`overview.md:38` says the same: "The separator half is held only on
Windows." Nothing on Windows refuses such a case. After a refresh its
Windows id is a key in the file, so it is priced there. On ubuntu and macOS
it stays unpriced and counts toward `STALE_SHARE`. The paragraph's body
says exactly that, and it is correct. Only the heading is wrong. This is a
correction to the run's paperwork, so it is not counted in `Needs a fix`.

The gap itself is real and already recorded in that section: no case
refuses a path id written with `\`. It cannot be refused by a backslash
search, because 1,339 of the file's keys carry an escaped backslash on
every platform (executed, the same script). It goes under `## Deferred`.

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
| round 1, ⬜ 3, open | `seal/ledger/1791852613-the-test-durations-are-refreshed-and-say-when-next.md:7` | the `Corrected · S3` row is unchanged by the fixes; it closes at the run's end |
| round 1, ⬜ 4, open | `.github/workflows/test.yml:45` | `c59c7664` restored `test.yml` byte for byte, so the short line stands; it closes at the run's end |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| A path parametrization that omits `ids=posix_id` is refused on no leg; it shows only as unpriced on ubuntu and macOS after the next refresh | `overview.md` §*Not done*, written by the fix pass | the orchestrator, who decides whether it becomes an issue |

Needs a fix: no
Loses a record or crashes: no

The broad gate has come due: nothing in this round is open to fix, so the
next act is the sealer's spawn at `808dc814`.

## Proof block

Files opened this round: `seal/specs/1791852613-the-test-durations-are-refreshed-and-say-when-next/rounds/round-1.md`,
`rounds/round-1-report.md`, `overview.md`, `survivors.md`, `questions.md`
(lines 1–40), `CONTRIBUTING.md` (lines 185–225),
`docs/release-checklist.md` (lines 45–75), `bin/test`,
`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` (lines
1–40 and the diff), `tests/test_every_agent_reads_the_contract.py` (lines
225–245), `tests/test_the_seal_is_taken_once_by_the_sealer.py` (lines
1924–1928), `tests/test_the_contributor_has_a_procedure.py` (lines
172–173), `docs/round-record-spec.md` (lines 160–200, 255–275), and the
full diff `744c610f..dfd51a66` outside `.test_durations`.
