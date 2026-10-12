# 1791382684-every-reader-and-record-is-inventoried — review round 3 report

Round 3 of #834's build, the last round of the run, target fe527020. Round 2
spent the one reopening (`Fix of a fix | first`). This round checks round 2's
fix range `062e31e4..d0541ae4` against the code, re-runs the three
enumerations of `rounds/round-2-fixes.md` §*The class, enumerated* on its own
probe, samples the units the fix pass left standing, and reads `plan.md`'s
corrected mapping rule against `hooks/worktree-guard.py`. Phase 4 is not built
and is otherwise out of scope.

Everything below was read at fe527020 in a `git clone --no-local` of the
worktree. What was executed is in *Executed probes*; everything else is read.

## Summary

- Round 2's three findings are closed for every unit they named. The fix
  commit changes docstrings only (syntax trees equal with docstrings removed).
- The class round 2's 🟡 1 claimed closed by construction is not closed. Three
  units its own enumerations selected still carry a line describing another
  unit or one caller: `_expands`, `cell_index`, `shared_reader` (this round's
  🟡 2).
- One unit the round-2 fix pass rewrote is still wrong: `_name_at`'s new line
  and paragraph describe `_substitute`, one of its eight callers (🟡 1). Its
  `Location` is inside round 2's fix range, so the record generator counts it
  as a fix of a fix.
- `plan.md`'s corrected rule defines the direction word differently from the
  `Unknown` cells it is read from, from `spec.md`, and from the plan's own
  *Class and direction* bullet. The build's lines now carry both meanings, and
  phase 4 would write a false word on the guard (⬜ 3, a correction to the
  run's paperwork).

## 🟡 1 — `_name_at`'s rewritten line describes one caller of eight

`hooks/cmdline.py#_name_at` reads one shell name at an index of whatever text
it is handed. Round 2's fix gave it this line and paragraph:

> Reads: guess — the shell name starting at one index of an operand; unknown passed
>
> Passed: no name there gives (None, i), and the caller keeps the `$` as written.

`_name_at` has eight call sites in `hooks/cmdline.py`. One is `_substitute`,
which reads an operand and keeps the `$` when no name follows it. The other
seven are in `_forget` (an assignment word's head, the name after `${`, a
`read` or `let` argument), `_unseen` (a loop head, a `read` or `let`
argument) and `_bind` (an assignment's left side). None of them involves a
`$`; on `(None, i)` each skips the word. So the paragraph is false for seven
callers, and "of an operand" names the row's lead reading, not this unit's.
This is the class round 2's 🟡 1 named, in a unit round 2's own fix wrote.

The direction word is the second half. The row (part 1 row 9) says `refused`,
because an unfilled `$` reaches `EXPANDS` and the target becomes
`Unresolved`. The fix pass moved it to `passed` on `plan.md`'s new rule (⬜ 3
below). Under the definition the row, `spec.md` and thirteen sibling lines
use, no input `_name_at` cannot read ends anywhere but refused or skipped, so
the word is `refused`. The paste-ready fix uses that word; if ⬜ 3 settles the
other way, the word is `passed` and the prose stands.

Why it matters: the line is what a reviewer reads instead of the code. A
reader who trusts this one concludes every caller fails closed through
`EXPANDS`, and seven of them do not go through it at all.

## 🟡 2 — three selected units still describe another unit or one caller

Round 2's 🟡 1 is recorded fixed with the class "closed by construction:
every unit the three enumerations below selected was read against its own
body". This round's enumerations (below) select these three, and each line is
false of its own body:

- `hooks/cmdline.py#_expands` — "Reads: guess — a string handed to a shell".
  That is the row lead's reading (`names_an_unknown_command`, part 1 row 27).
  `_expands` is handed a list of tokens and reads its first token: whether it
  is a reserved word, `[`, or holds an `EXPANDS` character. Round 1 rewrote
  only its `Refused:` paragraph; selected by (a).
- `skills/evidence-check/scripts/evidence_check.py#cell_index` — "header named
  `Code grounds`, or `LEDGER_COLUMNS` position; unknown passed", with
  "Passed: a renamed column takes the table out of the check". The unit
  reads the column its caller names, and `family_view` calls it for `Notes`
  as well as `Code grounds`. Only `held_by_tests` skips the table on -1. In
  `family_view` a missing `Notes` or `Code grounds` column is emitted as
  `MALFORMED`, so the direction is `mixed`, not `passed`. Selected by (a).
- `skills/evidence-check/scripts/evidence_check.py#shared_reader` — its
  `What it reads, continued:` paragraph names `hooks/*.py`. The body tests two
  files, the shared reader `unverified_check.py` and this skill's `SKILL.md`,
  and reads no hook. The row (part 4 E8) names five units, and `hooks/*.py`
  belongs to another of them. Selected by (c).

Why it matters: these are the instances the fix pass said it had read and
left true. The class is still open, and "closed by construction" is a claim
the next reader would otherwise inherit.

## ⬜ 3 — `plan.md` gives the direction word a second meaning

Round 2's ⬜ 4 correction added this to the `Unit → units` bullet: a unit's
direction is "`refused` where it raises or stops, `passed` where it hands back
a default for its caller to judge, `mixed` where it does both". That is not
what the `Unknown` cells mean. The inventory writes `refused` for a unit that
hands back a value its caller refuses on (part 1 row 57, `read_mark`:
"unreadable gives "", which is not HEAD, so the arm stands"; part 6:
"A presence pin is `refused`, because a rewording fails it"). `spec.md`
§*The build* takes the direction from the row's `Unknown` cell. The plan's own
*Class and direction* bullet still does the same.

The build now carries both meanings. The fix pass moved `_name_at` to `passed`
on the new rule. Thirteen units the plan's rule reads on their own body keep
`refused` while their body only hands a value back: `_process`, `_clone_of`,
`is_ancestor`, `carried_by_a_pull_head`, `nobody_reason`, `_dedup`,
`_directories`, `_expands`, `_step`, `opens_at`, `sections`, `visible` and
`_squash`. Each is right under the inventory's meaning and wrong under the
plan's.

On the guard, the rule would give phase 4 a false line. Part 1 row 124 names
`_merged_findings` and `_cut_unread`. `_cut_unread` does not read the row's
`wide.merged_view` groups, so it is read on its own body. That body returns a
list of `Finding("unread", …)` for each `&` cut with git beside it, which is
how the guard stops a command it cannot read. The plan's rule makes that
`passed`, and the row says `refused`. The rule's other parts hold on the
guard: row 114's `already_asked` runs `os.path.exists` on its marker and comes
out `observed`, row 106's `git_dir` hands back "" and comes out `passed` as its
row says, and row 123's `shape_of` makes its reads through `_segment_finding`,
a same-file callee, so it takes the row.

This is a correction to the run's paperwork. The paste-ready block replaces
the sentence with the inventory's meaning, which leaves the thirteen lines as
they are and changes `_name_at`'s word back (in 🟡 1's fix).

## Executed and read, apart

- Executed: the clone, the syntax-tree comparison, the enumeration probe, the
  direction comparison, the two test modules, `bin/evidence-check .`, and the
  `grep` for every caller named above. Results are in *Executed probes*.
- Read: every verdict above, including each selected unit's line against its
  body and same-file callees.
- Not run: the broad gate (full suite, lint, typecheck). It is the sealer's,
  after the rounds settle. With this report two findings stay open, so it has
  not come due.

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

### 🟡 1

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

### 🟡 2

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

### ⬜ 3

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

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

Needs a fix: yes — 🟡 1 (`_name_at`'s line and paragraph describe one caller of eight, in a unit round 2's fix wrote), 🟡 2 (`_expands`, `cell_index`, `shared_reader` still carry a line false of their body)

Loses a record or crashes: no

## Proof

Files opened at fe527020 in the clone: `rounds/round-1.md`, `rounds/round-2.md`,
`rounds/round-2-fixes.md`, `plan.md`, `spec.md` (the build section),
`overview.md` and `survivors.md` (through the fix diff), `inventory/1-hooks-shell.md`,
`inventory/4-ledger-settle-seal.md`, `inventory/6-tests.md` (heads and rows),
`docs/the-reader-registry.md` (the grammar section), `tests/reader_registry.py`,
and the units named above in `hooks/cmdline.py`, `hooks/routing.py`,
`hooks/review-history-guard.py`, `hooks/worktree-guard.py`,
`hooks/hook-install.py`, `skills/evidence-check/scripts/evidence_check.py`,
`skills/evidence-check/scripts/correction_check.py`,
`skills/evidence-check/scripts/pact_check.py`,
`skills/code-review/scripts/survivor_check.py`,
`skills/code-review/scripts/round_record.py`,
`skills/implement/scripts/seal.py`, `skills/verify/scripts/session_cost.py`,
plus every unit the enumeration dump printed.
