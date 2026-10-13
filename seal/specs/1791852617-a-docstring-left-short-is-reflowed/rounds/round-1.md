# 1791852617-a-docstring-left-short-is-reflowed — review round 1

| Field | Value |
|---|---|
| Target SHA | c88d537de66d88299a6722d8de4e18c59e9968e0 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #912 |
| Broad gate | not yet |
| Fixes checked by | no fixes to check |
| Fix range | none |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | no |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 1 of #844, target c88d537d against `origin/release/v0.21.1` at 321e9de1, over the whole build: the rewrap of `tests/test_one_word_one_meaning.py#without_the_policy_span`'s docstring to round 3's fence of work item 1791270163, and the `Re-read ·` row the moved hash owes in this work item's ledger fragment. The reviewer was also asked to judge the smith's choice to write no changelog fragment. The two other short docstring lines the reviewer found, in `hooks/config.py#reference_roots` and `tests/test_every_reader_ends_a_line_where_gfm_does.py`, were left by neither #831 nor this branch; the orchestrator leaves them for the next change to each unit, as #844 itself was left.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| ⬜ 1 | The re-read row says #844 rewrapped "the last five lines" of the docstring; six lines were rewrapped into five, and `overview.md:16` says the same | `seal/ledger/1791852617-a-docstring-left-short-is-reflowed.md:1` | answered | corrected at 90fbe8fb — the ledger row's Read clause and `overview.md:16` say six lines rewrapped into five, round 1's paste-ready text; executed: the base docstring ends in six lines (widths 35, 76, 77, 75, 70, 12) and HEAD's in five; the diff removes six and adds five. A correction to paperwork under `seal/`, not counted in `Needs a fix` |
| 🟢 | the docstring equals round 3's fence and changes no word and no code | `tests/test_one_word_one_meaning.py:737` | confirmed | executed: a deleted probe; lines 737–745 equal the fence from 25a05c68 byte for byte; the same 255 words in order; the body's AST and every line outside the function unchanged; `bin/test tests/test_one_word_one_meaning.py -q`, exit 0, 21 passed; `ruff check` and `ruff format --check` on the file, exit 0 |
| 🟢 | the re-read row keeps R6's family current at the reflowed unit's hash | `seal/ledger/1791852617-a-docstring-left-short-is-reflowed.md:1` | confirmed | executed: `evidence-check --strict --ledger` on the fragment exits 0 (2 ok); on `seal/releases/0.20.0.md` and `seal/releases/0.19.0.md` each exits 0 with nothing drifted; with the fragment moved out, `seal/releases/0.20.0.md` exits 2 with `without_the_policy_span` DRIFTED in a family of three rows, so the row is what clears it |
| 🟢 | no changelog fragment is owed for this work item | `seal/specs/1791852617-a-docstring-left-short-is-reflowed/overview.md:34` | confirmed | read: `docs/the-record-layout.md` states a commit that changes nothing a release note states owes the fragment nothing, and no document requires a fragment per work item; executed: three other live work items carry none, 1791090072 among them |

## Paste-ready fixes

```
**Read** 2026-10-13: #844 rewrapped the last six lines of `without_the_policy_span`'s docstring into five, to the text round 3 of #831 gave as a fence, and changed no code;
```
```
Rewrap the last six lines of `tests/test_one_word_one_meaning.py#without_the_policy_span`'s docstring into five, to round 3's fence, change no word and no code, and re-read the one ledger family the rewrap drifts.
```

## Executed probes

| What was run | Result |
|---|---|
| a deleted probe: the module parsed at the base and at HEAD, the docstring's words and the body's AST compared, round 3's fence from 25a05c68 compared with HEAD, line 741 printed at eea27ad0 and at the base | same 255 words; same body; nothing outside the function changed; the fence equals lines 737–745 byte for byte; line 741 is the short line at both revisions; the base's last six docstring lines became five |
| `bin/test tests/test_one_word_one_meaning.py -q` in the clone at c88d537d | exit 0, 21 passed |
| `ruff check` and `ruff format --check` on `tests/test_one_word_one_meaning.py` (ruff 0.17.0 through `uvx`; CI installs ruff unpinned) | exit 0 both |
| `bin/evidence-check --strict --ledger` on the fragment | exit 0; 2 ok · 0 drifted · 0 broken |
| `bin/evidence-check --strict --ledger` on `seal/releases/0.20.0.md`, then on `seal/releases/0.19.0.md` | exit 0, 579 ok · 0 drifted; exit 0, 714 ok · 0 drifted |
| the same check on `seal/releases/0.20.0.md` with the fragment moved out of the clone, then moved back | exit 2; `without_the_policy_span` DRIFTED, "no reading in this row's family of 3 rows holds the current content"; clone status clean after the move back |
| a deleted probe: every docstring in the four Python files #831 touched, scanned for a line the next line's first word would fit on | two prose instances outside this diff, at `hooks/config.py:683` and `tests/test_every_reader_ends_a_line_where_gfm_does.py:1160`; the rest were table or list layouts |
| the broad gate: the full suite, the repository-wide lint and the typecheck | not yet; this round ran none of it, and the sealer answers it once, after the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| Two more docstring lines of the same short shape, neither from #831 nor from this branch: `hooks/config.py:683` (left by 821e592d) and `tests/test_every_reader_ends_a_line_where_gfm_does.py:1160` (left by 20d1b289) | not filed; named here for the ladder | the orchestrator of this run, who decides whether this work item takes them or they wait for the next change to each unit |
