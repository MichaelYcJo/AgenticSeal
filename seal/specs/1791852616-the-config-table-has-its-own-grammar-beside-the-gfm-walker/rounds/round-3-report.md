# Round 3 — round 2's fixes, verified (#871)

Target SHA: 46063a51 · the diff of round 2's fixes, `4dfb3d0d..40fab1ec`
(11 commits) · base 321e9de1 · reviewed in a `git clone --no-local` at the
target SHA. The verifying round after the run's one reopening, so this
record ends the run whatever it finds. Round 1's note 6 is carried open and
is not reported again.

## How the findings relate

Round 2's seven findings are closed for the shapes they named, and the pact
item round 2 deferred is closed with them: the line-start guard now sits in
`gfm_table`, so the `Signer` table and the two pact records refuse a row
after a form feed or U+2028 the way the config table does. Every pinned pact
case still passes.

What stays open comes from one new rule in the vendored twin, the rule that
decides where the stretch below the table ends:

```
round 2's fix for 🟡 11/12: a heading under a fence or a "<" line below
the table may be inside that block, so the twin stops trusting headings
  ├─ it never notices the block closing
  │     → 🟡 14  a closed comment or fence below the table, then any table
  │              under a later heading: the vendored CI step exits 2 where
  │              the plugin reads the file whole (exit 0 before the fix)
  └─ the item count below the stop takes the same view, to end of file
        → 🟡 15  round 2's 🟡 10 shape, fixed in the plugin, still doubles
                 the row in the twin; the reason the docstring gives for
                 it is false of the twin's own walk
```

Two notes sit beside them, neither a defect that ships: ledger row C1, N7
and the changelog overstate when a pact line stops `--reverify` at exit 2
(⬜ 16), and the re-pinned pact cases compute their expected exit from the
walker under test (⬜ 17).

Both 🟡 sit in units round 2's fixes changed: `vendored_config_rows` and
`vendored_config_value`, both changed by 91d9225d. So the branch owns them,
which is rung 1 of the ladder in `docs/review-chain-spec.md`. This record
ends the run under the reopening bound, though, and that bound commissions
no fix. So I give both the third rung, a new issue, with the owner as the
answerer: v0.21.1 would ship 🟡 14 into every installed repository's CI.
The paste-ready fix below was applied in the clone and seen green, so the
owner can also take it onto this branch instead.

## Round 2's findings, answered

- **🟡 7** (a header or delimiter after a break reads a table). Closed.
  `gfm_table` asks `gfm_line_starts` for the header and the delimiter row
  before reading a body row, and refuses with the "each on a line of its
  own" sentence. Executed:
  `tests/test_the_mode_question_is_asked_once.py#test_a_header_after_a_break_gfm_does_not_honour_is_no_table`
  passes for all eight characters in both places, in the plugin and the
  twin. Round 2 measured cmark-gfm for FF, U+2028, NEL and VT; I carried
  that measurement rather than re-running it.
- **🟡 8** (the twin reads an item the plugin refuses). Closed. Two shapes
  joined `CONFIG_SHAPES`, and the equality case passes on both.
- **🟡 9** (fold-check reads a row written twice). Closed.
  `fold_check.py#config_rows` asks `config_value` for each of its three
  rows when the walk refused, and raises `Unusable` with that sentence.
  Executed:
  `tests/test_a_document_has_room_for_the_next_fold.py#test_a_fold_row_written_again_below_the_stop_has_no_value`
  passes.
- **🟡 10** (the count runs past the next heading). Closed in the plugin.
  `rows_named_below` stops at the first heading it is shown, and skips a
  piece that does not begin a GFM line. The twin did not follow it, which
  is 🟡 15.
- **🟡 11** (the twin says a closed block is unclosed). Closed. The twin
  asks `vendored_block_closes_below` and names the example table instead.
  The case pins both closed shapes and both never-closed sentences.
- **🟡 12** (the twin calls a block line one of the rows). Closed for ten
  block lines, each pinned.
- **🟡 13** (a fifth narrating docstring). Closed. `with_row`'s docstring
  states the rule rather than the writer that is gone. Read.
- **Round 2's deferred pact row.** Closed by moving the guard into
  `gfm_table`. Executed:
  `tests/test_one_table_walker_reads_what_gfm_renders.py#test_a_signer_after_a_break_gfm_does_not_honour_is_no_signer`
  passes, and the pact modules — signer, records, review, pact-check, the
  signer's CI and the anchor case — pass whole. Read: `pact_check.py`
  prints each refusal as `REFUSED`, and `chain_check.py` prints it as a
  notice. A header refused by the new guard says "renders no table", so
  `pact_signers` does not add "lists nobody" on top of it.
- **Q7, exit 2 for a pact line the walk refuses.** The re-pins match the
  orchestrator's answer. Where `walk_refused` names a sentence, the case
  requires exit 2, that sentence, the ledger byte for byte and no record.
  Where it names none, the old exit 1 and its `LEFT` line still hold.
  Executed: 18 of the 39 parametrised cases take the exit-2 branch (1 of
  5, 2 of 3 and 15 of 31), which is the ten the smith named plus the eight
  `cut at` shapes the twin refuses since 91d9225d.

## The new units

`gfm_line_starts`, `VENDORED_FIRST_CELL`, `VENDORED_THEMATIC_BREAK` and
`VENDORED_PIECE_BREAK` are correct as written. The two patterns are held
equal to the plugin's, and the piece-break class is held equal to every
character `str.splitlines` ends a line at, LF and CR aside.
`vendored_block_closes_below` is correct for what it is asked: it is called
only on an opener `vendored_block_left_open` returned, so the `next(...)`
over `VENDORED_RAW_HTML` always finds its kind. The new cases were each
seen red by the smith against 4dfb3d0d, by their docstrings; I did not
re-run that. The finding surface is the rule the same fix added inside
`vendored_config_rows`, below.

## Findings

### 🟡 14 — A closed block below the table makes the twin refuse every table under every later heading

`skills/evidence-check/scripts/evidence_check.py#vendored_config_rows`,
lines 4505–4535.

After a blank line ends the table, the twin records the first fence opener
or line beginning `<` as `block`, and from then on a heading no longer ends
its look for stray rows. Nothing ever resets `block`, so a block that closed
on its own line counts as open to the end of the file. Any `| … |` line
further down, in any table under any later heading, is then refused with
the "run the plugin's own `evidence-check`" sentence.

Why it matters: the vendored copy is what an installed repository's CI
runs. Measured end to end with the vendored script on its own, over a
config holding `| Mode | shared |`, a closed one-line comment under the
table, then `## Notes` and a two-column notes table:

| | 4dfb3d0d's twin | 46063a51's twin | the plugin |
|---|---|---|---|
| exit of `--strict .` | 0 | 2, `REFUSED seal/config.md` | reads the table whole, no refusal |

A fenced example and an autolink line in the same place give the same
answer. cmark-gfm renders both tables. The exit comes from the `Removes
from` row: it is not in the table, so the twin's table refusal becomes its
answer (`cutoff_row`), and a config `seal mode` writes holds `Mode` alone.

This is round 1's 🔴 1 class on a narrower shape — the twin refusing a
config the plugin reads — and it is a regression of round 2's fix: the twin
exited 0 on this shape before it. The stated direction lets the twin refuse
where it lacks block state, but here it has the state. It follows a fence
to its close above the header with `vendored_fence_closes`, and an HTML
block of kinds 1–5 with `VENDORED_RAW_HTML`. What it needs below the table
is the same walk, reset when the block closes.

The fix is one helper that walks the lines below the table down to the
first heading outside a block, and that both readers of that stretch use.
The fence is under *Paste-ready fixes*. Applied in the clone: the twin's 67
evidence-check cases, the pact-records module and the mode module pass (209
cases), and three new `CONFIG_SHAPES` entries are red against the tree and
green with the fix. `uvx ruff check` and `ruff format --check` are clean on
both files.

### 🟡 15 — The twin still doubles a row named in a table under the next heading

`skills/evidence-check/scripts/evidence_check.py#vendored_config_value`,
lines 4606–4610.

Where the table was refused and the item read above the refusal, the twin
counts every line to the end of the file whose first cell names the item.
The plugin counts only down to the next heading it is shown (round 2's 🟡
10). On round 2's own 🟡 10 shape, executed:

| | `Mode` | `Ledger frozen from` (same shape) |
|---|---|---|
| plugin | `shared` | `100` |
| twin | "appears 2 times — one value" | "appears 2 times — one value" |

The sentence is false: the item is written once in the config table and
once in a notes table under another heading. A person who reads it looks
for a second row to delete, and the edit that clears the file is the stray
line. Where the freeze or the `Removes from` row is read above that line,
the plugin's `--strict` passes and the twin's exits 2.

The docstring says the twin counts to the end of the file because "it
cannot tell a heading inside a fence from one outside". That is not true
of the twin's own walk. `vendored_config_rows` already decides, line by
line, whether a block opened below the table, and 🟡 14's fix makes it
decide when the block closes too. Counting over the same stretch keeps the
stated direction: a heading inside an open block is not a stop, so the
twin still counts every line the plugin may count. The case
`CONFIG_SHAPES["an item named in a table under the next heading"]` is red
against the tree and green with the fix.

### ⬜ 16 — C1, N7 and the changelog say every refused table stops `--reverify` at exit 2

`seal/ledger/1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker.md`,
row `Corrected · C1`; also row N7 and the changelog fragment's
*Every command reading the table* bullet.

C1 says a config whose table the walk refuses "is refused at exit 2 on the
freeze row before anything is planned", and the changelog says a pact line
below the table "now stops the run on the freeze row at exit 2". Both hold
only where the freeze row is not read above the refused line. Executed,
`cutoff_row` over a table holding `Ledger frozen from | 100`, then a blank
line and `| Pact notify | always |`: it returns `(100, None)`, and the twin
returns `100` too. So `--reverify` goes on to the pact reader, and the
moved row reaches the `LEFT` line at exit 1, as before. Read, not run end
to end. The behaviour is the per-item rule Q7's answer chose; only the
three sentences are wider than it. The fixtures hold no freeze row, which
is why the cases agree with the sentences.

### ⬜ 17 — The re-pinned pact cases take their expected exit from the walker under test

`tests/test_a_signer_records_a_pact_change.py#walk_refused`.

Each of the three re-pinned cases asks `walk_refused` which branch to
assert. Both branches pin what must never happen, a row re-stamped or a
record written. What they no longer pin is which shapes stop at exit 2: if
a later change made the walk read one of them, that case would move to the
exit-1 branch and still pass. A per-shape expectation, for instance a set
of the 18 ids expected to stop, would pin the answer Q7 settled.

## Regression tests to plant

- `tests/test_evidence_check.py`, `CONFIG_SHAPES`: the three entries in the
  🟡 14 fence. The equality case,
  `tests/test_evidence_check.py#test_the_vendored_config_rule_agrees_with_the_shared_one`,
  then holds the twin to the plugin on each. All three were seen red
  against 46063a51's twin and green with the fix.

## Facts for the evidence ledger

- N8, which describes the vendored twin, should state the twin's rule
  below the table once 🟡 14 lands: a heading ends the look for stray rows
  unless it stands inside a fence or HTML block opened below the table and
  not yet closed. Its anchors move with `vendored_config_rows` and
  `vendored_config_value`.
- C1, N7 and the changelog bullet: ⬜ 16's narrowing, "where the freeze row
  is not read above the refused line".

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 14 | a closed comment, fence or `<` line below the table makes the twin refuse every `\| … \|` line under every later heading, so the vendored CI step exits 2 on a config the plugin reads whole | `skills/evidence-check/scripts/evidence_check.py#vendored_config_rows` | deferred a new issue | executed: vendored `--strict .` exits 0 at 4dfb3d0d and 2 at 46063a51 over the same config; the plugin refuses nothing; cmark-gfm renders both tables; the fix applied in the clone is green. A unit round 2's fixes changed (91d9225d); the run ends here under the reopening bound |
| 🟡 15 | the twin counts an item named in a table under the next heading, where the plugin stops at the heading, and says the row appears twice | `skills/evidence-check/scripts/evidence_check.py#vendored_config_value` | deferred a new issue | executed: on round 2's 🟡 10 shape the plugin reads `shared` and `100`, the twin refuses both as "appears 2 times"; the docstring's reason is false of `vendored_config_rows`' own walk. A unit round 2's fixes changed (91d9225d); the same issue as 🟡 14, whose helper it uses |
| ⬜ 16 | C1, N7 and the changelog say every refused table stops `--reverify` at exit 2, which holds only where the freeze row is not read above the refused line | `seal/ledger/1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker.md` | open | executed: `cutoff_row` returns `(100, None)` with a freeze row above a refused pact line; read: `--reverify` then reaches the pact reader |
| ⬜ 17 | the three re-pinned pact cases take their expected exit from `walk_refused`, so which shapes stop at exit 2 is not pinned | `tests/test_a_signer_records_a_pact_change.py#walk_refused` | open | executed: 18 of 39 cases take the exit-2 branch; read: both branches pin no re-stamp and no record |
| 🟢 | round 2's finding 7 is closed — the header and the delimiter row are asked whether they begin a GFM line | `hooks/config.py#gfm_table` | confirmed | executed: the 16-case header test passes in plugin and twin; cmark-gfm's answer carried from round 2 |
| 🟢 | round 2's finding 8 is closed — the twin gives no value to an item written again below the stop | `skills/evidence-check/scripts/evidence_check.py#vendored_config_value` | confirmed | executed: the two new `CONFIG_SHAPES` entries pass the equality case |
| 🟢 | round 2's finding 9 is closed — fold-check refuses a row written again below the stop | `skills/settle/scripts/fold_check.py#config_rows` | confirmed | executed: the new fold case passes; read: the loop asks `config_value` only where the walk refused |
| 🟢 | round 2's finding 10 is closed in the plugin — the count stops at the next heading it is shown | `hooks/config.py#rows_named_below` | confirmed | executed: the heading case and the break case pass; the twin's half is 🟡 15 |
| 🟢 | round 2's finding 11 is closed — the twin names an example table in a block that closes below the header | `skills/evidence-check/scripts/evidence_check.py#vendored_block_closes_below` | confirmed | executed: the case pins both closed shapes and both never-closed sentences |
| 🟢 | round 2's finding 12 is closed — a block line under the last row gets the blank-line sentence | `skills/evidence-check/scripts/evidence_check.py#vendored_config_rows` | confirmed | executed: ten block lines pinned and passing |
| 🟢 | round 2's finding 13 is closed — `with_row`'s docstring states the rule | `skills/implement/scripts/seal.py#with_row` | confirmed | read |
| 🟢 | round 2's deferred pact row is closed — a signer row after a break is refused, not read | `hooks/config.py#gfm_table` | confirmed | executed: the signer case passes for eight characters; the six pact modules pass whole |
| 🟢 | the Q7 re-pins match the answer — exit 2, the walker's sentence, the ledger unchanged and no record where the walk refuses | `tests/test_a_signer_records_a_pact_change.py#walk_refused` | confirmed | executed: the module passes; 18 cases on the exit-2 branch; their strength is ⬜ 17 |

## Executed probes

| What was run | Result |
|---|---|
| pytest over the pact modules (records, declares, pact-check, review, the signer's CI, the anchor case), the walker module, the mode module, the fold module, the line-end class and the reader declarations, at 46063a51, the worktree's `.venv` interpreter run in the clone, `SPECSEAL_CASE_CEILING_S=600` | exit 0, 4266 passed |
| pytest over `tests/test_evidence_check.py -k "vendored or config or frozen or cutoff or removes or twin"`, ceiling 600 | exit 0, 67 passed |
| `bin/evidence-check --strict .` in the clone at 46063a51 | exit 0 |
| The vendored `evidence_check.py --strict .`, copied alone, over three scratch repositories, at 4dfb3d0d and at 46063a51 | closed comment below the table then a notes table under a heading: 0 at 4dfb3d0d, 2 at 46063a51; fenced example in the same place: 2 and 2; round 2's 🟡 10 shape with a freeze row: 2 and 2 |
| `config_table` and `vendored_config_rows`, plus cmark-gfm 9.1.1, over a closed comment, a fenced example and an autolink line below the table, then `## Notes` and a table | plugin: one row, no refusal; twin: one row and the block refusal for all three; cmark-gfm: two tables |
| `config_value` and `vendored_config_value` over round 2's 🟡 10 shape, for `Mode` and `Ledger frozen from`, with the notes in a table and in a fence | plugin `shared` and `100`; twin "appears 2 times" in all three |
| Both readers over this repository's `seal/config.md`, `NEW_CONFIG` and `templates/config.md` | 7, 1 and 7 rows on both sides, no refusal, equal values |
| `walk_refused` over every parametrised shape of the three re-pinned cases | 1 of 5, 2 of 3 and 15 of 31 take the exit-2 branch |
| `cutoff_row` and the twin over a table with and without a `Ledger frozen from` row, then a blank line and `\| Pact notify \| always \|` | without: the walker's sentence; with: `(100, None)` and `100` |
| 🟡 14 and 🟡 15's fix applied in the clone with three new `CONFIG_SHAPES` entries; reverted after | the three shapes red against the tree, green with the fix; 209 passed over the twin's cases, the pact-records and mode modules; ruff check and format clean |
| `round_record.py new` over this report, in the clone, then discarded with the clone | exit 0: the tables parse; it reads the run as ending here, `Fix of a fix` `no` and `Fixes checked by` `no fixes to check` |
| `tests/test_no_real_identifiers.py` and `tests/test_one_word_one_meaning.py` with this report staged in the clone; `bin/evidence-check --strict .` over the worktree with the report beside it | exit 0, 27 passed; exit 0, no name refused |
| The broad gate (full suite, lint, typecheck) | not yet — the sealer's, after the rounds settle |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| 🟡 14: the twin refuses every table under every later heading after a closed block below the config table | a new issue, labelled `from-review` — rung 3; rung 1 fits by ownership, and the reopening bound allows no fix pass | the repository owner: v0.21.1 ships this vendored checker into installed CI, and the verified fix in this report lets the owner take it onto this branch instead |
| 🟡 15: the twin doubles a row named under the next heading | the same issue as 🟡 14, whose helper it uses | the repository owner, with 🟡 14 |

## Paste-ready fixes

### 🟡 14 — `skills/evidence-check/scripts/evidence_check.py#vendored_config_rows`

A helper after `vendored_block_closes_below`:

```python
def vendored_below(lines, start):
    """(index, line, block) for each line of LINES from START down to the
    first heading outside a block opened below the table, BLOCK being the
    line that opened the block LINE is in, or None.

    Reads: guess — the lines of a person's `config.md` below its table; unknown refused

    A fence closes where `vendored_fence_closes` says, an HTML block of
    kinds 1-5 at its closer, and any other line starting `<` at the next
    blank line, where kinds 6 and 7 end; a heading inside any of them is no
    heading, and one below a block that closed is one."""
    fence, end, opener = None, None, None
    for index in range(start, len(lines)):
        line = lines[index]
        if opener is not None:
            yield index, line, opener
            if (
                vendored_fence_closes(line, fence)
                if fence is not None
                else end.search(line)
                if end is not None
                else not line.strip()
            ):
                fence, end, opener = None, None, None
            continue
        if VENDORED_ATX_HEADING.match(line.lstrip(" ")) and not line.startswith(
            ("    ", "\t")
        ):
            return
        content = line.lstrip(" ")
        fence = vendored_fence_opener(line)
        if fence is not None:
            opener = line.strip()
        elif content.startswith("<"):
            kind = [close for open_, close in VENDORED_RAW_HTML if open_.match(content)]
            end = kind[0] if kind else None
            if not (end is not None and end.search(content, 1)):
                opener = line.strip()
            else:
                end = None
        yield index, line, opener
```

The loop in `vendored_config_rows`, from `rows, stray, ended, block = …`
down to the `continue` before `if heading:`, becomes:

```python
    rows, stray = [], None
    for index in range(at + 2, len(lines)):
        line = lines[index]
        heading = VENDORED_ATX_HEADING.match(line.lstrip(" ")) and not line.startswith(
            ("    ", "\t")
        )
        if not line.strip():
            for _below, line, block in vendored_below(lines, index):
                if any(
                    piece.lstrip().startswith("|")
                    for piece in VENDORED_PIECE_BREAK.split(line)
                ):
                    stray = (
                        f"has a `{name}` table that ends above `{line.strip()}`, "
                        "a row the walk never reaches — it and every row below "
                        "it would go unread"
                        if block is None
                        else f"has a `{name}` table with `{block}` below it, a "
                        "block a copy of the checker with no `hooks/` beside it "
                        f"does not follow, and `{line.strip()}` inside it, which "
                        "may be a row the walk never reaches — run the plugin's "
                        "own `evidence-check`"
                    )
                    break
            break
        if heading:
```

The cases, in `tests/test_evidence_check.py`'s `CONFIG_SHAPES` after "a
cutoff written again below the stop":

```python
    # #871 round 3: a block below the table that closes, then a table under
    # the next heading, is read whole by the plugin; and a table under the
    # next heading names nothing the stopped walk counts.
    "a closed comment below the table, a table under the next heading": _HEAD
    + "| Mode | shared |\n\n"
    + config_shapes.OPEN
    + " a note "
    + config_shapes.CLOSE
    + "\n\n## Notes\n\n| What | Why |\n|---|---|\n| a | b |\n",
    "a closed fence below the table, a table under the next heading": _HEAD
    + "| Mode | shared |\n\n```\nan example\n```\n\n## Notes\n\n"
    + "| What | Why |\n|---|---|\n| a | b |\n",
    "an item named in a table under the next heading": _HEAD
    + "| Mode | shared |\n| a | b | c |\n\n## Notes\n\n"
    + "| Mode | what it means |\n|---|---|\n| local | x |\n",
```

### 🟡 15 — `skills/evidence-check/scripts/evidence_check.py#vendored_config_value`

The count, over the helper above:

```python
    if values and refusals:
        for _below, line, _block in vendored_below(gfm_lines(text), rows[-1][0] + 1):
            first = VENDORED_FIRST_CELL.match(line)
            if first and first.group(1).strip().replace("\\|", "|") == item:
                values.append(None)
```

The docstring paragraph that gave the end-of-file reason:

```python
    In a table the walk refused, a line below its last row naming ITEM in
    its first cell makes the row read above it one of two, as it does to
    the plugin, down to the next heading outside a block opened below the
    table (`vendored_below`). A heading inside a fence or an HTML block this
    copy saw open is no stop, so it counts every line the plugin may count,
    and refuses where the plugin reads rather than the other way round.
```

Needs a fix: yes — 🟡 14 (a closed block below the table makes the vendored
CI step exit 2 on a config the plugin reads whole), 🟡 15 (the twin doubles
a row named under the next heading)
Loses a record or crashes: no

The broad gate has not run. It is not due: 🟡 14 and 🟡 15 are open, and
the owner decides whether a fix lands before the sealer's spawn.

## Proof block

```
📋 code-review applied (warden, round 3, verifying)
· target:   46063a51, a --no-local clone; the fix diff 4dfb3d0d..40fab1ec
· read:     rounds/round-1.md, round-2.md and round-2-report.md's structure;
            questions.md; the fix diff of hooks/config.py,
            skills/evidence-check/scripts/evidence_check.py, seal.py,
            fold_check.py, broad_gate.py, templates/config.md,
            skills/config/SKILL.md and the seven test files; hooks/config.py
            hidden_lines through rows_named_below, table_end through
            pact_signers; evidence_check.py's vendored fence rule, gfm_lines,
            the vendored grammar through vendored_config_value, config_rule,
            cutoff_row and the Removes-from check; pact_check.py's signer
            loop; chain_check.py's signer notices; the ledger fragment's T1,
            C1 and N7 rows; the changelog, overview, questions and survivors
            diffs; docs/review-chain-spec.md's cap, reopening and ladder
            sections; round_record.py's close and depth rules
· executed: the probes in the table above, exit codes read directly; the
            clone's edits reverted, the probe files deleted, the clone
            removed
· unverified: the full suite, lint and typecheck — the sealer's, after the
            rounds settle; the end-to-end --reverify of ⬜ 16's shape
```
