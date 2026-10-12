# 1791382684-every-reader-and-record-is-inventoried — review round 2

| Field | Value |
|---|---|
| Target SHA | 7ef6abbf3f7413e68761ea2046723f9093f3ff38 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #901 |
| Broad gate | not yet |
| Fixes checked by | round-3 |
| Fix range | `062e31e46ea465fafb471b1b11a1780e42b75d97..d0541ae449b26d6f1a9455cd98c3a5db091e7bcc`, 1 commit |
| Contract changes | none |
| New units | none |
| Fix of a fix | first — 🟡 3 at skills/verify/scripts/unverified_check.py#sections, a unit round-1's fixes changed |
| Needs a fix | yes — 🟡 1 (thirteen more `Reads:` lines naming a read their unit never makes), 🟡 2 (three direction words and one class word from the row, not the unit), 🟡 3 (`sections` and `flat`, two units the fix pass rewrote, still declare a read that is not theirs) |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 2 of #834's build, the verifying round, target 7ef6abbf. It was asked to inherit round 1's verdicts and check each fix (fix range a6b0ac20..bf1e425a) against the code, to judge the six "front" units the fix pass left alone, to check that `plan.md`'s corrected mapping rule would not reproduce round 1's 🟡 1 in phase 4, and then to read the rest of the build `7608d82c..HEAD` fresh.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | thirteen more units carry a `Reads:` line or paragraph naming a read their own code never makes, the class round 1 found and the plan's corrected rule forbids | `skills/evidence-check/scripts/correction_check.py:780` | **fixed** `d0541ae4` | fixed at d0541ae4 — the thirteen units, each read against its body and the callees it relies on (`merges`' caller, `_env_option`, `running`, `_ordered`, `top_units`, both `run_gh` callers, `is_header`); and the class closed by construction: every unit the three enumerations below selected was read against its own body, and 11 more lines that named a read their unit does not make were corrected; the one place `survivor-check` names over the fix range is the inventory's own row for `run_gh`, a row in `survivors.md`; each read beside its body; found by a by-construction list of non-lead units, word-for-word shared lines, and names absent from body and callees (probes) |
| 🟡 2 | three direction words and one class word come from the row, not the unit: `merges`, `parents`, `_ordered`, `parse_section` | `hooks/routing.py:415` | **fixed** `d0541ae4` | fixed at d0541ae4 — `merges` `refused` (it only raises `Refused`), `parents` `passed` (a failure gives [] and the caller lists the merge as unjudged), `_ordered` `mixed` (it re-raises `NotADirectoryError` and gives [] on any other `OSError`), `parse_section` `guess` (its `strict_header=False` arm is `check_text`'s loose reading), each confirmed in the code first; `merges` only raises, `parents` only gives `[]`, `_ordered` re-raises `NotADirectoryError`; `check_text` is `guess` and its loose arm is `parse_section`'s |
| 🟡 3 | two units the fix pass rewrote still declare a read that is not theirs: `sections`' new line holds for a pattern heading only, and `flat` keeps `read_record`'s line above its new paragraph | `skills/verify/scripts/unverified_check.py:882` | **fixed** `d0541ae4` | fixed at d0541ae4 — `sections` says a string heading is matched exactly and a pattern falls back after `## Not verified`; `flat` says it reads one field `describe` hands it, and the record's line and paragraph are gone from it; the string arm returns exact matches of the string, and the shared reader's callers pass `VERDICTS`; `flat` joins one value's whitespace |
| ⬜ 4 | the corrected mapping rule leaves the reading unit to position and drops round 1's presence-test class, which guard row 114 contradicts | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md` | answered | corrected at `d0541ae4`: `plan.md`'s `Unit → units` bullet now names the unit that does the reading by what its body (or a same-file callee) does — the K1 call, the `open`, the `git` or `gh` command, the AST walk — never by position, says that where no one unit makes every read none does, gives each word a mechanical meaning, and carries round 1 ⬜ 4's decision with guard row 114 named; correction to the run's paperwork; the guard's `already_asked` runs `os.path.exists` and its row says `owned` |
| ⬜ 5 | `survivors.md` calls `parse_section` the row's lead and says it reads that shape | `seal/specs/1791382684-every-reader-and-record-is-inventoried/survivors.md` | answered | corrected at `d0541ae4`: the `parse_section` row is gone from `survivors.md`, since its line no longer carries the quoted prose; `check_text`, which the row names first and whose line carries that prose with `guess`, has a row of its own already; correction to the run's paperwork; part 5 row 75 names `check_text` first |
| 🟢 | round 1's finding 1 is closed for 31 of its 32 units — each new line true of its own body | `hooks/commitgate.py:144` | confirmed | all 32 read at 7ef6abbf, with the callers four of them cite; the 32nd, `sections`, is this round's 3 |
| 🟢 | round 1's finding 2 is closed — both `parse_range` bodies declare one line, and four class words follow the code | `skills/evidence-check/scripts/correction_check.py:746` | confirmed | read in code: `Refused` raises, `merge-base` keeps the left end; `tree_at`, `lease_dirs`, `other_ci_files`, `agents_in` |
| 🟢 | round 1's finding 3 is closed — no docstring in the build counts lines | `hooks/cmdline.py:340` | confirmed | `_heredoc_split`'s comment found; search of every added line, no line-number shape |
| 🟢 | round 1's ⬜ 5 and ⬜ 7 are closed — Q4 ticked, the approval line read by `APPROVED_RE` | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md` | confirmed | `APPROVED_RE.match` on the line, executed |
| 🟢 | the fix commit and the build change no reader's behaviour | the 44 changed `.py` files | confirmed | syntax trees equal with docstrings removed (probe) |

## Paste-ready fixes

```
🟡 1 — thirteen units, each line replaced (and the paragraph named, where one is)

skills/evidence-check/scripts/correction_check.py:780  merges, the line and its `Mixed:` paragraph
    Reads: observed — `rev-list --merges a..b`; unknown refused

    Refused: a walk git cannot make raises `Refused`.

skills/evidence-check/scripts/correction_check.py:792  parents, the line and its `Mixed:` paragraph
    Reads: observed — `rev-parse <rev>^@`; unknown passed

    Passed: a failure gives [], so the merge has no merge base and is listed as unjudged.

skills/verify/scripts/arm_check.py:408  _members
    Reads: observed — one boolean test's AST: a `BoolOp`'s values, else the test alone; unknown passed

hooks/cmdline.py:1872  _env_long, the line and its `Passed:` paragraph
    Reads: guess — one `--` option name after `env`, exact or a GNU getopt prefix of one `_ENV_LONG` name; unknown passed

    Passed: a name that is no option, or a prefix of two, gives None.

hooks/version-check.py:65  parse — and delete the `What it reads, continued:` paragraph
    Reads: owned — the `version` string `running` takes from `plugin.json`, matched as `v?X.Y.Z`; unknown passed

hooks/routing.py:448  rounds
    Reads: owned — `listdir(item/rounds)` through `_ordered`, filtered by #87; unknown passed

hooks/routing.py:526  stray_rounds
    Reads: owned — `listdir(item)` through `_ordered`, filtered by #87; unknown passed

tests/conftest.py:752  symlink_or_skip
    Reads: observed — the OSError raised by the attempted `os.symlink`; unknown passed

tests/conftest.py:812  fifo_or_skip
    Reads: observed — whether `os.mkfifo` exists, and the OSError its attempt raises; unknown passed

skills/code-review/scripts/round_record.py:3568  enclosing_unit
    Reads: observed — the line spans `top_units` read from a module's AST; unknown passed

skills/code-review/scripts/survivor_check.py:1129  shape_pattern
    Reads: owned — one of the `LEDGER_SHAPES` path globs, `**/` and `*`; unknown passed

skills/verify/scripts/session_cost.py:2838  run_gh
    Reads: observed — `gh <args>`: its exit code, stdout and stderr; unknown mixed

skills/verify/scripts/unverified_check.py:767  parse_section (the class is 🟡 2's)
    Reads: guess — one section's body lines: the `Item` header (exact under `strict_header`), 2-cell rows, ✅ prefix; unknown refused

overview.md, the 32-unit divergence row: "32 units" becomes "46 units", and its Grounds cell gains "; round 2 🟡 1 and 🟡 3".

Verify: bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py tests/test_a_rider_reaches_its_file.py
        bin/evidence-check .   (none of these units is cited; it should stay exit 0)
```
```
🟡 2 — the direction and class words (merges, parents and parse_section are in 🟡 1's block)

hooks/routing.py:415  _ordered, the line and a paragraph under it
    Reads: owned — `listdir(where)` filtered by #87; unknown mixed

    Mixed: a directory that will not list gives []; a `rounds` that is a file raises
    `NotADirectoryError` for the caller to name.

Verify: the same two commands as 🟡 1.
```
```
🟡 3 — two units the fix pass rewrote

skills/verify/scripts/unverified_check.py:882  sections
    Reads: owned — a file's headings: a string heading matched exactly, or `## Not verified` first, else the pattern; unknown refused

hooks/dispatch.py:449  flat — and delete the `What it reads, continued:` paragraph
    Reads: owned — one field of a `.pending` record, as `describe` hands it; unknown passed

Verify: the same two commands as 🟡 1.
```
```
⬜ 4 — plan.md, the `Unit → units` bullet: replace the sentences from "only the unit whose body" to "apply this rule instead."

  Only a unit whose body, or a unit it calls, makes every read the row's `What
  it reads` names takes that cell as its prose; being named first in the cell
  does not make a unit that one. Where no one unit makes all of them, none
  does. Every other unit the row names is read on its own code, and its prose,
  class and direction are what that code bears out. A test of whether a file
  this plugin writes exists is `observed`, whatever the row's `Class` cell says
  (round 1 ⬜ 4); part 1 row 114, the guard's `already_asked`, says `owned`.
  Phase 2 gave every named unit the row's prose; rounds 1 and 2 found 46 lines
  describing another unit. Phase 4 and any later rerun apply this rule instead.
```

## Executed probes

| What was run | Result |
|---|---|
| `git clone --no-local` of the worktree, checked out at 7ef6abbf | clone at the target |
| each `.py` file's syntax tree with docstrings removed, `a6b0ac20` against `bf1e425a`, and `7608d82c` against HEAD | 23 files, 0 differ; 44 files, 0 differ |
| list every top-level unit that gained a `Reads:` line between `7608d82c` and HEAD | 189 units |
| for each, every backticked name in its `Reads:` line and `What it reads, continued:` paragraph, looked for in its body and the bodies of the module's units it calls | 42 units flagged; each read; most are module constants, the rest are in 🟡 1 |
| group the 189 by identical `Reads:` line | 17 groups of two to four; each group read against its units' code |
| map each unit to its inventory row and list the units not named first in a multi-unit `Unit` cell | 71 units; those not in round 1's list read beside their code |
| `bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py tests/test_a_rider_reaches_its_file.py` | 126 passed, exit 0 |
| `bin/evidence-check .` | exit 0; 0 refused, 0 drifted |
| search of every added `.py` line in `7608d82c..HEAD` for a line-number shape and the inventory's shorthand | no line number outside three rider stamps; no shorthand |
| `APPROVED_RE.match` on each `plan.md` line starting `Approved` | the one line matches |
| a search of `seal/ledger.md`, `seal/releases/` and `seal/ledger/` for each unit named in 🟡 1–3 as `<file>#<unit>@`, and of `hooks`, `skills` and `tests` for a rider stamp on any of them | 0 citations, 0 stamps |
| the broad gate: full suite, lint, typecheck | not yet — the sealer's, after the rounds settle |

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

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
