# 1791382684-every-reader-and-record-is-inventoried — round 2 report

| Field | Value |
|---|---|
| Round | 2 |
| Target SHA | 7ef6abbf3f7413e68761ea2046723f9093f3ff38 |
| Base | `origin/release/v0.21.0`; the fix range under check is `a6b0ac20..bf1e425a`, and the build read afresh is `7608d82c..7ef6abbf` |
| Reviewer | warden on Opus 5.5 |
| Where | a `git clone --no-local` of the worktree at the target SHA, under the session scratchpad's `1791382684-every-reader-and-record-is-inventoried/round-2/clone`; removed before hand-over |

## How the findings relate

Round 1's three findings were closed where round 1 pointed. The class behind
its first finding was not exhausted, and the plan's corrected rule has two
gaps that would let phase 4 repeat it.

1. **What held, executed.** The fix commit changes no code: 23 `.py` files,
   the same syntax tree at both ends once docstrings are removed. The whole
   build still holds that, 44 files. The registry and rider modules pass, 126
   cases, and `bin/evidence-check .` exits 0.
2. **Round 1's 32 lines, read.** I opened all 32 units and the 5 class-word
   units against their bodies. 31 of the 32 new lines are true of their own
   code. The 32nd, `sections`, is half true, and `flat`, whose paragraph
   the fix pass rewrote, kept a line that is not its own (🟡 3).
3. **The class round 1 missed (🟡 1).** I enumerated the non-lead units of
   every multi-unit inventory row by construction (71 units by my split of the
   `Unit` cells), and separately every line shared word for word by two units
   and every backticked name in a line that appears nowhere in the unit or the
   units it calls. 13 more units carry a line naming a read their code never
   makes, and a 14th, `flat`, is in a unit the fix pass rewrote (🟡 3). Each
   is a unit the plan's own corrected rule says is read on its own code.
4. **Direction and class words in the same rows (🟡 2).** Three direction
   words and one class word come from the row and not the unit.
5. **Paperwork (⬜ 4, ⬜ 5).** The corrected mapping rule decides "the unit
   whose body does the reading" by nothing a reader can apply mechanically, and
   it does not carry round 1's ⬜ 4 decision. The guard's own `already_asked`
   row says `owned`, so phase 4 would split that shape again. `survivors.md`
   calls `parse_section` the row's lead, which it is not.

## Round 1's verdicts, each checked against the code

- **🟡 1, 32 lines.** Closed for 31. Each new line and paragraph was read
  beside its body at 7ef6abbf. The claims that rest on another unit were
  opened too: `calendar_date`'s caller `reading_date` drops a non-date and
  defaults to `""`; `origin`'s empty answer is refused in `check` by
  `config.pact_name`; `short_commit`'s None sends `resolve_base` to its next
  step; `already_asked`'s True leads `main` to `ask`. The four shorthand words
  are gone. The 32nd, `sections`, is 🟡 3.
- **🟡 2, five class words and two direction words.** Closed. Both
  `parse_range` bodies are identical and now declare one line and one
  paragraph, and the paragraph matches the code (`Refused` raised for no
  separator or an unresolved end, `merge-base` failure keeps the left end).
  `tree_at` reads `os.walk` or `ls-tree` and gives `[]` on failure.
  `lease_dirs` lists directories and opens no JSON. `other_ci_files` runs
  `isfile` and lists `.buildkite/`. `agents_in` takes `name` through
  `frontmatter`.
- **🟡 3, three line references.** Closed. `_heredoc_split`'s comment on an
  unbalanced `${` is where the two paragraphs say, and no line number was
  added anywhere in the build: a search of every added `.py` line for a
  line-number shape finds only the three rider stamps' `Verified … against`
  comments.
- **⬜ 4.** Closed in the code: the commit-review gate's `already_asked` and
  the consent module's `granted` now declare `observed`, beside
  `review-skill-gate.py` and `hook-install.py`, which already did. Not
  carried into the plan (⬜ 4 of this round).
- **⬜ 5.** Closed: `questions.md` Q4 is ✅ with phase 2's answer.
- **⬜ 6.** Answered in words, with two gaps (⬜ 4 of this round).
- **⬜ 7.** Closed. Executed: `APPROVED_RE`, matched line by line as the
  chain check reads it, matches the plan's approval line.

## The front units the fix pass left alone

The prompt named six units whose line is the row's prose left in place.

- `hooks/cmdline.py#_land` — true. It unpacks the cd kind and operand and
  returns `prev` for `cd -`.
- `skills/code-review/scripts/chain_check.py#reachable` — true. Both reads
  are its own, through `is_ancestor` and `carried_by_a_pull_head`.
- `skills/code-review/scripts/chain_check.py#last_round_end` — true. It takes
  the range's second end through `range_ends`, and the last `Target SHA`
  where the row says `none`.
- `skills/verify/scripts/deferral_check.py#inspect` — true, and partial. It
  reads runner words in the files `other_ci_files` finds and in
  `.pre-commit-config.yaml`, as the line says. The line leaves out the
  `.github/workflows` files and their triggers, which it reads through
  `workflow_files` and `read_events`. Nothing it names is false, so this is
  not a finding.
- `skills/verify/scripts/unverified_check.py#check_text` — true, with its
  loose base reading in the paragraph under the line.
- `skills/verify/scripts/unverified_check.py#parse_section` — not true. See
  🟡 1 and 🟡 2.

## Findings from reading

### 🟡 1 · Thirteen more units carry a line naming a read their code never makes

The plan's corrected rule (`plan.md`, the `Unit → units` bullet) now says that
every unit a row names, other than the one doing the reading, "is read on its
own code" and "its prose says what that unit reads". Phase 2's output was not
re-read against that rule. The fix pass replaced round 1's list, and the same
shape stands on these units:

- `skills/evidence-check/scripts/correction_check.py:780` `merges` runs only
  `rev-list --merges`; its line also names `rev-parse ^@`.
  `correction_check.py:792` `parents` runs only `rev-parse <rev>^@`; its
  line names `rev-list --merges`. Each one's paragraph describes both.
- `skills/verify/scripts/arm_check.py:408` `_members` reads a `BoolOp`'s
  values and nothing else. `Tuple`, `MatchOr` and guards are `_node_arms`'s.
- `hooks/cmdline.py:1872` `_env_long` matches one long option name, and only
  under GNU: `_env_option` never calls it under `bsd`. Its line says both
  grammars, and its `Passed:` paragraph about "an unknown letter" is
  `_env_option`'s short-letter loop.
- `hooks/version-check.py:65` `parse` matches one string against
  `v?X.Y.Z`. The line names `plugin.json` and `repository`, which `running`
  reads.
- `hooks/routing.py:448` `rounds` lists `item/rounds` only, and
  `hooks/routing.py:526` `stray_rounds` lists `item` only. Both lines name both
  listings.
- `tests/conftest.py:752` `symlink_or_skip` attempts only `os.symlink`, and
  `tests/conftest.py:812` `fifo_or_skip` only `os.mkfifo`. Both lines name
  both.
- `skills/code-review/scripts/round_record.py:3568` `enclosing_unit` reads a
  map of line spans that `top_units` built. It reads no AST, and its line says
  "Python AST at both ends".
- `skills/code-review/scripts/survivor_check.py:1129` `shape_pattern` turns
  one of `LEDGER_SHAPES` into a regex. It compares no committed path, which is
  what its line says.
- `skills/verify/scripts/session_cost.py:2838` `run_gh` runs `gh` with
  whatever `args` it is handed. Its line names one caller's
  `issue list --json number,state`, and the other caller runs
  `issue comment`, which returns no JSON.
- `skills/verify/scripts/unverified_check.py:767` `parse_section` reads one
  section's body lines. The `## Not verified` heading in its line is read by
  `sections` for `check_text`, and "exact header" holds only when
  `strict_header` is set: `check_text` calls it with `strict_header=False` for
  a base revision, and then any header whose first cell is `Item` passes
  (`is_header`).

**Why it matters.** It is the same false declaration round 1 found, limit 1
of `docs/the-reader-registry.md` §*What neither check can read*. A reviewer
who trusts `merges`' line looks there for a parent read that is not in it.
`overview.md`'s divergence row says each of "32 units" now says what its own
unit reads. It does not cover these, though they are the same kind of unit.

**What the fix keeps and costs.** Each replacement keeps the row's class. The
direction changes only where 🟡 2 says it does. Executed: no unit here, nor
`_ordered`, `sections` or `flat`, carries a rider stamp, and no row in `seal/ledger.md`,
`seal/releases/` or `seal/ledger/` cites any of them, so no `Re-read ·` row is
owed.

### 🟡 2 · Three direction words and one class word the unit's code contradicts

- `correction_check.py:780` `merges` declares `mixed`. Its own failure only
  raises `Refused`, so its direction is `refused`.
- `correction_check.py:792` `parents` declares `mixed`. Its own failure only
  gives `[]`, so its direction is `passed`. The `mixed` belongs to the pair
  together, which is the row and not either unit.
- `hooks/routing.py:415` `_ordered` declares `passed`. It re-raises
  `NotADirectoryError` on purpose, which its own comment says, and gives `[]`
  on any other `OSError`. That is `mixed`.
- `unverified_check.py:767` `parse_section` declares `owned`. Its only caller,
  `check_text`, was decided `guess … mixed` by hand in phase 2, because of the
  loose base reading. The loose half of that reading is `parse_section`'s own
  `strict_header=False` arm. The registry gives a unit parsing text its caller
  handed it the class of where the text came from, so it is `guess`.

The direction word is half of what the registry's check reads. A `mixed`
where the unit refuses outright hides the one unit in the pair that stops.

### 🟡 3 · Two units the fix pass rewrote still declare a read that is not theirs

These are kept apart from 🟡 1 because the fix pass changed both units, so
they sit one depth deeper than 🟡 1's.

- `skills/verify/scripts/unverified_check.py:882` `sections`. The fix pass
  wrote "a file's headings: the exact `## Not verified` first, else the
  matcher given". That is the pattern arm. Handed a string, `sections`
  returns the headings equal to that string and never looks for
  `## Not verified` first. Its string callers are `check_text`'s default and
  the shared reader's callers in `skills/code-review/scripts/chain_check.py`
  and `round_record.py`, which pass `VERDICTS` and their own headings. This
  is the one of round 1's 32 lines that the fix did not make true.
- `hooks/dispatch.py:449` `flat` joins the whitespace of one value. Its line
  and the paragraph under it name the whole `.pending` record and its four
  fields, which is `read_record`'s line word for word. The fix pass rewrote
  this unit's `Passed:` paragraph and left the two lines above it. This is
  🟡 1's shape, in a unit the fix pass opened and did not finish.

### ⬜ 4 · Correction: the plan's corrected rule has two gaps that phase 4 meets

`seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md`, the
`Unit → units` bullet.

- **Which unit is "the unit whose body does the reading"** is left to the
  reader. The build itself read it by position: `survivors.md` calls
  `parse_section` the lead of part 5 row 75, whose cell names `check_text`
  first and whose reading `check_text` does. Nor does the rule say what
  happens on a row whose reading is split across its units, which is where
  `merges`/`parents` and `rounds`/`stray_rounds` came from.
- **The class word.** "Keeps the row's class and direction where its code
  bears them out" gives no word for where the code does not. Round 1's ⬜ 4
  decision, that a presence test of a marker this plugin writes is `observed`,
  sits only in `overview.md`. Part 1 row 114, the guard's `already_asked`,
  says `owned`, and its body is `os.path.exists` on its marker. Run as
  written, phase 4 writes `owned` there and splits the four-unit shape ⬜ 4
  just unified.

I read the guard's rows 106 and 113 against its code. Both are rows where each
named unit does the row's reading or calls the one that does, so the rule
handles them. The paste-ready text is below.

### ⬜ 5 · Correction: `survivors.md` gives a reason that is not so

`seal/specs/1791382684-every-reader-and-record-is-inventoried/survivors.md`,
the `parse_section` row, says "`parse_section`'s line, the row's lead: it
reads exactly that shape". It is not the lead, and it does not read that
shape (🟡 1). Once 🟡 1 is closed the quote no longer survives there. The row
then either goes, or names `check_text`, whose line carries the same prose
with `guess` and is true of it.

## What the code confirmed

- The fix commit changes no behaviour: executed, by syntax tree with
  docstrings removed, `a6b0ac20` against `bf1e425a`, 23 files equal. The whole
  build, `7608d82c` against HEAD, 44 files equal.
- The census and the registry: executed. The registry and rider modules pass,
  126 cases.
- Ledger coordinates: executed. `bin/evidence-check .` exits 0.
- Carried from round 1 and not re-established: the census count (1,395) and
  the three re-stamped riders, which the fix range does not touch.
- Not checked by me: the full suite, lint and typecheck. They are the
  sealer's, and not yet run.

## Regression tests to plant

None. These are false declarations, which the registry names as the
reviewer's to read (limit 1); no case reads prose against code. A case that
two units do not share one `Reads:` line word for word would catch
`merges`/`parents`, `rounds`/`stray_rounds` and the two `conftest.py` pairs,
and wrongly refuse the four `below_floor` units, which share a line truly. So
I do not propose one.

## Facts for the evidence ledger

None.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | thirteen more units carry a `Reads:` line or paragraph naming a read their own code never makes, the class round 1 found and the plan's corrected rule forbids | `skills/evidence-check/scripts/correction_check.py:780` | open | each read beside its body; found by a by-construction list of non-lead units, word-for-word shared lines, and names absent from body and callees (probes) |
| 🟡 2 | three direction words and one class word come from the row, not the unit: `merges`, `parents`, `_ordered`, `parse_section` | `hooks/routing.py:415` | open | `merges` only raises, `parents` only gives `[]`, `_ordered` re-raises `NotADirectoryError`; `check_text` is `guess` and its loose arm is `parse_section`'s |
| 🟡 3 | two units the fix pass rewrote still declare a read that is not theirs: `sections`' new line holds for a pattern heading only, and `flat` keeps `read_record`'s line above its new paragraph | `skills/verify/scripts/unverified_check.py:882` | open | the string arm returns exact matches of the string, and the shared reader's callers pass `VERDICTS`; `flat` joins one value's whitespace |
| ⬜ 4 | the corrected mapping rule leaves the reading unit to position and drops round 1's presence-test class, which guard row 114 contradicts | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md` | open | correction to the run's paperwork; the guard's `already_asked` runs `os.path.exists` and its row says `owned` |
| ⬜ 5 | `survivors.md` calls `parse_section` the row's lead and says it reads that shape | `seal/specs/1791382684-every-reader-and-record-is-inventoried/survivors.md` | open | correction to the run's paperwork; part 5 row 75 names `check_text` first |
| 🟢 | round 1's finding 1 is closed for 31 of its 32 units — each new line true of its own body | `hooks/commitgate.py:144` | confirmed | all 32 read at 7ef6abbf, with the callers four of them cite; the 32nd, `sections`, is this round's 3 |
| 🟢 | round 1's finding 2 is closed — both `parse_range` bodies declare one line, and four class words follow the code | `skills/evidence-check/scripts/correction_check.py:746` | confirmed | read in code: `Refused` raises, `merge-base` keeps the left end; `tree_at`, `lease_dirs`, `other_ci_files`, `agents_in` |
| 🟢 | round 1's finding 3 is closed — no docstring in the build counts lines | `hooks/cmdline.py:340` | confirmed | `_heredoc_split`'s comment found; search of every added line, no line-number shape |
| 🟢 | round 1's ⬜ 5 and ⬜ 7 are closed — Q4 ticked, the approval line read by `APPROVED_RE` | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md` | confirmed | `APPROVED_RE.match` on the line, executed |
| 🟢 | the fix commit and the build change no reader's behaviour | the 44 changed `.py` files | confirmed | syntax trees equal with docstrings removed (probe) |

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

## Paste-ready fixes

Line numbers are at 7ef6abbf. Indentation is the docstring's own four spaces,
except a one-line docstring, which keeps its quotes. Each block is marked in
`code-review`'s findings format.

### 🟡 1

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

### 🟡 2

```
🟡 2 — the direction and class words (merges, parents and parse_section are in 🟡 1's block)

hooks/routing.py:415  _ordered, the line and a paragraph under it
    Reads: owned — `listdir(where)` filtered by #87; unknown mixed

    Mixed: a directory that will not list gives []; a `rounds` that is a file raises
    `NotADirectoryError` for the caller to name.

Verify: the same two commands as 🟡 1.
```

### 🟡 3

```
🟡 3 — two units the fix pass rewrote

skills/verify/scripts/unverified_check.py:882  sections
    Reads: owned — a file's headings: a string heading matched exactly, or `## Not verified` first, else the pattern; unknown refused

hooks/dispatch.py:449  flat — and delete the `What it reads, continued:` paragraph
    Reads: owned — one field of a `.pending` record, as `describe` hands it; unknown passed

Verify: the same two commands as 🟡 1.
```

### ⬜ 4

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

Needs a fix: yes — 🟡 1 (thirteen more `Reads:` lines naming a read their unit never makes), 🟡 2 (three direction words and one class word from the row, not the unit), 🟡 3 (`sections` and `flat`, two units the fix pass rewrote, still declare a read that is not theirs)
Loses a record or crashes: no

Not mine to run, and not yet due: the sealer's broad gate, once a round
leaves nothing open.

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

## Proof block

Opened in the clone at 7ef6abbf, or in the worktree for the frame:

- `seal/specs/1791382684-every-reader-and-record-is-inventoried/`:
  `rounds/round-1-report.md`, `rounds/round-1-fixes.md`, `rounds/round-1.md`,
  `plan.md` (the mapping rules and the approval line), `survivors.md`,
  `phases/phase-2.md` (its head), and from `inventory/`, the rows for the
  units named above and part 1's guard rows 86 to 127, by search.
- `docs/the-reader-registry.md` §*The four classes and the line that declares
  one*.
- The full diff `a6b0ac20..bf1e425a`.
- The source of every unit that diff touched, and of `_land`, `reachable`,
  `last_round_end`, `inspect`, `parse_section`, `check_text`.
- The source of each unit named in 🟡 1 and 🟡 2, and of the callers their
  lines rest on: `reading_date`, `check` in `pact_check.py`, `resolve_base`,
  `main` in `hooks/commit-review-gate.py` around its two `already_asked`
  calls, `_node_arms`, `_env_option`, `running`, `describe`'s use of `flat`,
  the `merges`/`parents` caller in `correction_check.py`, both `run_gh`
  callers, `is_header`, and `_heredoc_split`'s comment.
- In `hooks/worktree-guard.py`, read only to judge the plan: `already_asked`,
  `lease_dir`, `git_dir`, `repo_paths`, `git_at`.
