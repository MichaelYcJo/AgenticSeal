# 1791382684-every-reader-and-record-is-inventoried — review round 3

| Field | Value |
|---|---|
| Target SHA | fe5270200d027257d228ec2584a18d6f546b91ce |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #901 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are not yet written |
| Fix range | none — the fixes are not yet written |
| Contract changes | none — the fixes are not yet written |
| New units | none — the fixes are not yet written |
| Fix of a fix | second — 🟡 1 at hooks/cmdline.py#_name_at, a unit round-2's fixes changed; the fix passes stop here and the work item goes back to its framer |
| Needs a fix | yes — 🟡 1 (`_name_at`'s line and paragraph describe one caller of eight, in a unit round 2's fix wrote), 🟡 2 (`_expands`, `cell_index`, `shared_reader` still carry a line false of their body) |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Round 3 of #834's build, the last round of the run, target fe527020. Round 2 spent the one reopening and recorded `Fix of a fix | first`. It was asked to verify round 2's fixes (fix range 062e31e4..d0541ae4) against the code, to re-run the three enumerations independently and say whether any selected unit's line is still false, and to check that `plan.md`'s mechanical mapping rule would give phase 4 correct lines on `hooks/worktree-guard.py`.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | `_name_at`'s line and paragraph, rewritten by round 2's fix, describe `_substitute`, one of its eight callers; the other seven skip the word and involve no `$` | `hooks/cmdline.py#_name_at` | open | eight call sites read in `hooks/cmdline.py`: `_substitute`, `_forget` ×3, `_unseen` ×2, `_bind`; the row says `refused` and the fix moved it to `passed` on ⬜ 3's rule |
| 🟡 2 | three units round 2's enumerations selected still carry a line false of their body: `_expands` (the lead's prose), `cell_index` (one column of two, and `mixed`, not `passed`), `shared_reader` (`hooks/*.py`, another unit's read) | `skills/evidence-check/scripts/evidence_check.py#cell_index` | open | `cell_index` called for `NOTES` in `family_view`, and -1 there emits `MALFORMED`; `held_by_tests` alone skips; `shared_reader` tests `READER` and `SKILL.md` only; `_expands` is handed `command_word(toks)[0]` or `[t]`, a token list |
| ⬜ 3 | `plan.md`'s corrected rule defines the direction word by whether a body raises, not by where the unknown ends, as the `Unknown` cells, `spec.md` and the plan's *Class and direction* bullet do; thirteen written lines and `_name_at` now disagree, and phase 4 would write `passed` on the guard's `_cut_unread` | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md` | open | correction to the run's paperwork; part 1 rows 57 and 124, part 6's rule for presence pins, `spec.md` §*The build*; `_cut_unread` returns `Finding("unread", …)` |
| 🟢 | round 2's finding 1 is closed for the thirteen units it named and for ten of the eleven the enumerations corrected; the eleventh, `_name_at`, is this round's 1, and the class is this round's 2 | `skills/evidence-check/scripts/correction_check.py:780` | confirmed | each read at fe527020 with its callers: `merges`, `parents`, `_members`, `_env_long`, `parse` (only `running` calls it), `rounds`, `stray_rounds`, `symlink_or_skip`, `fifo_or_skip`, `enclosing_unit`, `shape_pattern`, `run_gh`, `parse_section`; `_cd_target`, `near_miss`, `resolve`, `Check`, `parse_module`, `signature`, `return_arities` and the three `payload_meter` helpers |
| 🟢 | round 2's finding 2 is closed — `merges` `refused`, `parents` `passed`, `_ordered` `mixed`, `parse_section` `guess` | `hooks/routing.py:415` | confirmed | `merges` raises `Refused`; the `parents` caller lists an empty result as unjudged; `_ordered` re-raises `NotADirectoryError` and gives [] on any other `OSError`; `rounds` catches it |
| 🟢 | round 2's finding 3 is closed — `sections` and `flat` each say what their own body reads | `skills/verify/scripts/unverified_check.py:882` | confirmed | `sections`' string arm matches exactly and its pattern arm falls back after `## Not verified`; `describe` hands `flat` one field at a time |
| 🟢 | round 2's ⬜ 4 and ⬜ 5 are closed for what they asked — position no longer picks the reading unit, a presence test is `observed`, the `parse_section` row is gone from `survivors.md` | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md` | confirmed | the direction sentence the ⬜ 4 correction added is this round's ⬜ 3 |
| 🟢 | round 1's findings 1–3 and ⬜ 4–7 stay closed | `hooks/commitgate.py:144` | confirmed | round 2 confirmed them at 7ef6abbf; the fix range rewrote two of round 1's units, `sections` and `flat`, confirmed above; the round-1 units this round's enumerations selected were read again |
| 🟢 | the fix commit changes no reader's behaviour | the 15 `.py` files of `062e31e4..d0541ae4` | confirmed | syntax trees equal with docstrings removed (probe) |

## Paste-ready fixes

```
hooks/cmdline.py#_name_at — the line and the paragraph under it
    Reads: guess — the shell name starting at one index of a word; unknown refused

    Refused: no name there gives (None, i), and no caller fills, binds or forgets
    anything from it: `_substitute` keeps the `$`, which `EXPANDS` then makes
    `Unresolved`; `_forget`, `_unseen` and `_bind` skip the word.

(If ⬜ 3 keeps the plan's rule instead, the last word is `passed` and the
paragraph is headed `Passed:`; the prose is the same.)

Verify: bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py tests/test_a_rider_reaches_its_file.py
```
```
hooks/cmdline.py#_expands — the line
    Reads: guess — the first token of one command word: a reserved word, `[`, or an `EXPANDS` character; unknown refused

skills/evidence-check/scripts/evidence_check.py#cell_index — the line and its paragraph
    Reads: owned — a ledger row's header, for the column its caller names (`Code grounds` or `Notes`), else that name's `LEDGER_COLUMNS` position; unknown mixed

    Mixed: a column the header does not hold gives -1; `held_by_tests` leaves that
    table out of the check, and `family_view` reports the row `MALFORMED`.

skills/evidence-check/scripts/evidence_check.py#shared_reader — the line; delete the `What it reads, continued:` paragraph
    Reads: observed — whether `unverified_check.py` and this skill's `SKILL.md` are files beside it; unknown mixed

    Mixed: either one absent gives None, and `fence_rule` and `cell_rule` switch to the
    vendored copy; present but broken raises.

Verify: the same command as 🟡 1, and bin/evidence-check .  (none of the three is cited; it should stay exit 0)
```
```
plan.md, the `Unit → units` bullet: replace the sentence that begins "its direction is
what that body does" with

  its direction is where an input it does not understand ends, read through
  the caller its value goes to, as the `Unknown` cells read it: `refused`
  where it ends refused (raised, stopped, or handed back as a value its
  caller refuses on, as `read_mark`'s "" and `_cut_unread`'s "unread"
  finding are), `passed` where it is let through as if understood, `mixed`
  where both happen.

and add after "rounds 1 and 2 found 46 lines describing another unit":

  ; round 3 found that round 2 had moved `_name_at` to `passed` on a
  narrower reading of the word, and moved it back
```

## Executed probes

| What was run | Result |
|---|---|
| `git clone --no-local` of the worktree, checked out at fe527020 | clone at the target |
| each `.py` file's syntax tree with docstrings removed, `062e31e4` against `d0541ae4` | 15 files, 0 differ |
| list the 189 units whose census line the build removed (`7608d82c`'s census less HEAD's) | 189 |
| (a) units not the first name, or not the first top-level unit, in a matching inventory row's `Unit` cell | 71 units, the fix table's after-fix count |
| (b) groups of units sharing a byte-identical `Reads:` line | 10 groups, 22 units, the fix table's after-fix count |
| (c) units whose `Reads:` line or `What it reads, continued:` paragraph names a backticked identifier, path or command absent from the body, the bodies of same-file units it calls, and the module constants it names | 35 units; narrower than the fix table's 78, which did not count constants |
| the union of (a)–(c), each line read against its body and callees | 95 units; three lines false (🟡 2), and `_name_at` (🟡 1) |
| the 94 written units outside the union, each line printed beside its unit name | read, bodies not opened: no line reads as another unit's; this is a sample, not a verdict |
| the (a) units' declared direction against "raises or stops" in the body and its same-file callees | 25 flagged; read by hand to the thirteen named in ⬜ 3 (the rest raise through a callee, make the row's reads themselves, or were flagged by a comment) |
| `grep` of every call of `_name_at` in `hooks/cmdline.py` and `cell_index` in `evidence_check.py` | 8 and 5 call sites, each read |
| `bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py tests/test_a_rider_reaches_its_file.py` | 126 passed, exit 0 |
| `bin/evidence-check .` | exit 0; 8397 ok, 0 drifted, 0 refused |
| the broad gate: full suite, lint, typecheck | not yet — the sealer's, after the rounds settle; not due while 🟡 1 and 🟡 2 are open |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `hooks/commitgate.py:144` | round 1's 🟡 1 — fixed |
| round-1 | `skills/evidence-check/scripts/correction_check.py:746` | round 1's 🟡 2 — fixed |
| round-1 | `hooks/cmdline.py:339` | round 1's 🟡 3 — fixed |
| round-1 | `hooks/commit-review-gate.py:686` | round 1's ⬜ 4 — answered |
| round-1 | `seal/specs/1791382684-every-reader-and-record-is-inventoried/questions.md` | round 1's ⬜ 5 — answered |
| round-1 | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md` | round 1's ⬜ 6 — answered |
| round-1 | the 44 changed `.py` files | round 1's 🟢 — confirmed |
| round-1 | `tests/undeclared_readers.txt` | round 1's 🟢 — confirmed |
| round-2 | `skills/evidence-check/scripts/correction_check.py:780` | round 2's 🟡 1 — fixed |
| round-2 | `hooks/routing.py:415` | round 2's 🟡 2 — fixed |
| round-2 | `skills/verify/scripts/unverified_check.py:882` | round 2's 🟡 3 — fixed |
| round-2 | `seal/specs/1791382684-every-reader-and-record-is-inventoried/survivors.md` | round 2's ⬜ 5 — answered |
| round-2 | `hooks/cmdline.py:340` | round 2's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
