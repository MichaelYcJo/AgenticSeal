# Round 2 — round 1's fixes, verified (#871)

Target SHA: 383d9f19 · the diff of the fixes, `aa0fc421..946360ab` (5
commits) · base 321e9de1 · reviewed in a `git clone --no-local` at the
target SHA. A verifying round: it answers round 1's verdicts and judges the
units round 1's fixes created. Round 1's note 6 is carried open and is not
reported again.

## How the findings relate

Round 1's five findings are closed for the shapes they named. The
blocking one is closed on the probe that found it: the vendored checker now
exits 0 over a repository holding this repository's config and over one
holding the config `seal mode` writes, and its predecessor exits 2 over the
same two.

What stays open is the edge of two of the fixes, each one class wider than
the shape it was aimed at (contract §12):

```
round 1's finding 4: the walker reads str.splitlines pieces, not GFM lines
  └─ the guard checks body rows only
        → 🟡 7   a header or delimiter after a form feed still reads a table
                 GitHub does not render
the owner's answer: an item written again below the stop has no value
  ├─ it reached config_value and not the readers beside it
  │     → 🟡 8   the vendored twin reads the value the plugin refuses
  │     → 🟡 9   fold-check reads it too
  └─ it reaches further than the walker's own "below the stop"
        → 🟡 10  a table of notes under the next heading doubles the row
round 1's finding 1: the twin follows blocks above the header
  └─ its sentences for the shapes it still refuses
        → 🟡 11  "close the block" for a block that is closed
        → 🟡 12  a fence or list line in the table "is one of its rows"
the owner's answer: the in-place rule reaches docstrings
        → 🟡 13  a fifth docstring still names the stop rule
```

Nothing found loses a record or crashes. Each 🟡 is a value read that the
plugin elsewhere refuses, or a refusal sentence that names the wrong edit.

## Round 1's findings, answered

- **Finding 1, the vendored checker refused every plugin-written config:
  closed.** Executed. The vendored `evidence_check.py --strict .` exits 0
  at 383d9f19 over a scratch repository holding this repository's
  `seal/config.md`, and exits 0 over one holding `NEW_CONFIG`'s output. At
  c5dde1f7 both exit 2 with `REFUSED seal/config.md`. Three
  `CONFIG_SHAPES` were added and `VENDORED_RAW_HTML` is held equal to
  the first five of `HTML_KINDS`. The vendored module's cases (49
  selected) pass.
- **Finding 2, `seal mode` called a walker refusal a defect in itself:
  closed.** Read and executed. `write_row` now prints the walker's sentence
  where the walk refuses the text it would write (`seal.py:1593`).
  `with_row` already refuses a file whose own table the walker refuses, so
  this branch is reached only by what the write itself adds. The new case
  passes.
- **Finding 3, the remedy for a second table: closed.** Read. All three
  documents name *put a heading between the two*, and the S8 document case
  passes.
- **Finding 4, a row after a break GFM does not honour: closed for that
  shape.** Executed for FF, U+2028, NEL and VT: the walker reads `Mode`
  only and refuses the second row, as cmark-gfm renders one row. The same
  cause still reaches the header and the delimiter row (🟡 7).
- **Finding 5, prose naming three walks: closed.** Read. No "three walks"
  remains in `hooks/`, `skills/`, `templates/`, `docs/` or `agents/`, and
  the `Broad gate` sentence in `missing_row` no longer describes this
  repository's config.
- **First question, the owner's rule reaches docstrings: applied at the
  four named spots.** Read: `hooks/config.py` `config_table`, `unfenced`,
  the walker's header comment and `broad_gate.py` `missing_row` no longer
  narrate. A fifth instance remains (🟡 13).
- **Second question, an item written again below the stop: done in
  `config_value`.** Executed: `Mode` read above a three-cell row and
  written again below it is "`Mode` appears 2 times — one value". It does
  less than that elsewhere (🟡 8, 🟡 9) and more than that past a heading
  (🟡 10).

## The new units

- `GFM_LINE_ENDS` and the row guard in `config_table`: correct for body
  rows; the header and the delimiter are not asked (🟡 7).
- `FIRST_CELL` and `rows_named_below`: the count does not stop where the
  walker's own "rows nobody reads" stops (🟡 10).
- `VENDORED_RAW_HTML` and `vendored_block_left_open`: the direction holds.
  Executed over 12,719 documents built from 23 line kinds above the header:
  the twin never reads `Mode` where the plugin refuses it. In 36 documents
  the twin reads `Mode` where the plugin answers "no table", and cmark-gfm
  renders the twin's row in all 36. Each is a fence inside an HTML block of
  kinds 1–5 above the header, the limit `hooks/config.py#hidden_lines`
  documents, and the base read none of them either. Not a finding.
- The three new cases pass (10 parametrised, executed).

## Findings

### 🟡 7 — A header after a form feed still reads a table GitHub does not render

`hooks/config.py#config_table`, the guard at line 352. Executed against
cmark-gfm.

The guard asks whether each body row begins a GFM line. It does not ask
the header or the delimiter row. Two shapes pass it:

- `| Item | Value |`, a form feed, `|---|---|` on the same GFM line, then
  `| Mode | shared |`;
- a form feed alone before `| Item | Value |`.

For both, with FF and with U+2028, cmark-gfm renders no table. The walker
reads `Mode` as `shared`. So the mode gate, `broad-gate` and the cutoff
readers act on a row GitHub does not show, which is what round 1's finding
4 and S1 were about. The fix asks the header and delimiter pieces the same
question and refuses the table. Applied in the clone: all four breaks
measured (FF, U+2028, NEL, VT) refuse in both positions, cmark-gfm renders
no table for any of them, and a header on the file's first line still
reads.

### 🟡 8 — The vendored twin reads an item the plugin refuses as written twice

`skills/evidence-check/scripts/evidence_check.py#vendored_config_value`.
Executed.

`config_value` now refuses a row read above a line the walk refused when a
line below names the same item. `vendored_config_value` was not changed.
For `| Ledger frozen from | 100 |`, a three-cell row, then
`| Ledger frozen from | 200 |`, the plugin answers "`Ledger frozen from`
appears 2 times — one value" and the twin answers `100`. That is the twin
reading where the plugin refuses, the one direction its docstring and the
changelog say it never takes. In a repository's CI, the vendored copy then
turns the freeze on where the plugin's own `evidence-check` refuses.

The equality case did not catch it because no shape in `CONFIG_SHAPES`
writes an item again below the stop. Applied in the clone, the fix makes
both new shapes equal on every item, and the 30+ existing shapes stay
equal.

### 🟡 9 — fold-check reads a row `config_value` gives no value

`skills/settle/scripts/fold_check.py#config_rows`, with `declared` at line
571. Executed.

`fold_check.py` reads its three rows through `value_of` over the walked
rows, not through `config_value`. Its docstring says "A refusal below all
three rows touches none of them". Measured with all three rows read, a
three-cell row, and `| Document line ceiling | 9000 |` below it:
`declared` returns a ceiling of 400, while `config_value` refuses the same
row as written twice. Two readers give two answers about one file, the
split #867 closed.

`skills/verify/scripts/broad_gate.py#broad_command` behaves correctly,
because it asks `config_value`. Its docstring at line 840 still says a row
read above a refused line "is a value, and the gate runs it", which is now
false where the row is written again. The fix carries that sentence too.

### 🟡 10 — A row named under the next heading doubles the config row

`hooks/config.py#rows_named_below`. Executed.

`gfm_table` treats a line written `| … |` after the table's end as a row
nobody reads only until the next heading. `rows_named_below` counts to the
end of the file. So a config whose walk is refused for another reason, and
which holds a notes section such as `## Notes` with a table headed
`| Mode | what it means |`, has its `Mode` row refused as "appears 2
times". The person wrote `Mode` once in the config table. The sentence
then points them at their notes rather than at the line the walk stopped
at. The owner's answer was that an item written again below the stop has
no value. A table under another heading is not below the stop by the
walker's own definition, so this is more than that answer. The fix stops
the count at the next heading, as `gfm_table` does.

### 🟡 11 — The twin tells a person to close a block that is closed

`skills/evidence-check/scripts/evidence_check.py:4430`, in
`vendored_config_rows`. Executed.

The twin still refuses the two `LACKS_BLOCK_STATE` shapes whose first
header sits inside a block that closes below it: a fenced example table
above the live one, and a commented old table above the live one. Its
docstring names both as refused shapes. The sentences the fix wrote are:

- for the comment: "inside an HTML block opened above it and never closed
  … — close the block";
- for the fence: "which a copy of the checker … reads as never closed —
  close the fence above the table, or run the plugin's own
  `evidence-check`".

Both blocks are closed. A person following the first sentence has nothing
to close, and the CI step stays at exit 2. This is round 1's finding 2
over again: a refusal naming a cause it did not check. No case pins either
sentence, since the direction case asserts only that something is refused,
and §14 asks for a pin. The fix asks whether the block closes below the
header and says so in a sentence of its own. The never-closed sentences
stay, so the equality case is unaffected.

### 🟡 12 — The twin calls a fence or list line inside the table one of its rows

`skills/evidence-check/scripts/evidence_check.py:4496`, in
`vendored_config_rows`. This sentence is the build's, at c5dde1f7, not
round 1's fix. I opened it because 🟡 11 is the same family. Executed
against cmark-gfm.

A line directly under the last row that opens a fence, a list item, a
block quote, an HTML block or a code block four columns in gets: "a line
with no pipe that GFM reads as one of its rows — write it as
`| … | … |`". cmark-gfm ends the table at each of the six lines measured
and renders `Mode shared`, and the plugin reads the table whole with no
refusal. The refusal is the twin's stated direction. The sentence is
false, though, and its edit would have a person turn a fence or a
comment into a table row. The fix gives such a line a sentence that says
what the twin cannot judge, and names the edit that clears it: a blank line
above it.

### 🟡 13 — A fifth docstring still narrates the stop rule

`skills/implement/scripts/seal.py:1475`, in `with_row`'s docstring. Read.

"the stop rule's writer wrote a second `Mode` row under a bare-piped
line". The branch added this sentence, and it names a reader the tree no
longer has, the same class as the four the fix rewrote under the owner's
answer to round 1's first question. A search of `hooks/`, `skills/`,
`templates/`, `docs/` and `agents/` finds no other.

## Regression tests to plant

- `tests/test_the_mode_question_is_asked_once.py`: a header after a break,
  and a delimiter after the header's break, read no row and refuse naming
  *each on a line of its own* (🟡 7). Red at 383d9f19: `Mode` is read as
  `shared`.
- `tests/test_evidence_check.py`: two `CONFIG_SHAPES`, `Mode` and
  `Ledger frozen from` each written again below a three-cell row, plus a
  pattern-equality line for the twin's first-cell pattern (🟡 8). Red at
  383d9f19 on the cutoff shape: the twin reads `100`.
- `tests/test_a_document_has_room_for_the_next_fold.py`: fold-check's
  `declared` over a ceiling written again below the stop raises `Unusable`
  (🟡 9). Red at 383d9f19: it returns 400.
- `tests/test_the_mode_question_is_asked_once.py`: a notes table under the
  next heading leaves `Mode` its value (🟡 10). Red at 383d9f19.
- `tests/test_evidence_check.py`: the twin's sentence for an example table
  inside a closed fence and a closed comment, and for a block line inside
  the table (🟡 11, 🟡 12). Each is red at 383d9f19 on its phrase.

## Facts for the evidence ledger

- The vendored `evidence_check.py` at 383d9f19 exits 0 over a repository
  holding this repository's `seal/config.md`, and over one holding
  `NEW_CONFIG`'s output. At c5dde1f7 it exits 2 over both. Executed.
- cmark-gfm renders no table for `| Item | Value |`, FF or U+2028, then
  `|---|---|` on the same GFM line. The walker at 383d9f19 reads `Mode` as
  `shared` from it. Executed.
- `fold_check.py#declared` at 383d9f19 returns a ceiling of 400 where
  `config_value` refuses the same row as written twice. Executed.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 1's blocking finding 1 is closed — the vendored checker reads the config `seal mode` writes and this repository's own | `skills/evidence-check/scripts/evidence_check.py:4430` | confirmed | executed: the vendored `--strict .` exits 0 over both repositories at 383d9f19, 2 over both at c5dde1f7; the vendored module's cases pass |
| 🟢 | round 1's finding 2 is closed — `write_row` prints the walker's sentence | `skills/implement/scripts/seal.py:1593` | confirmed | executed: the new case passes; read: `with_row` refuses a file already refused, so only the write reaches this branch |
| 🟢 | round 1's finding 3 is closed — all three documents name the heading remedy | `templates/config.md:62` | confirmed | read; executed: the S8 document case passes |
| 🟢 | round 1's finding 4 is closed for a row after a break on another row's line | `hooks/config.py#config_table` | confirmed | executed: FF, U+2028, NEL and VT read `Mode` only, as cmark-gfm renders; the header and delimiter members are 🟡 7 |
| 🟢 | round 1's finding 5 is closed — no "three walks" remains, and the `Broad gate` sentence no longer describes this repository's config | `templates/config.md:314` | confirmed | read: a search of hooks, skills, templates, docs and agents |
| 🟢 | round 1's first question is applied at the four named docstrings | `hooks/config.py:331` | confirmed | read: also `:257`, the walker's header comment, `broad_gate.py` `missing_row`; a fifth is 🟡 13 |
| 🟢 | round 1's second question is answered in `config_value` | `hooks/config.py#config_value` | confirmed | executed: a row written again below a refused line has no value; its reach is 🟡 8, 🟡 9 and 🟡 10 |
| 🟢 | the twin's block-following above the header never reads where the plugin refuses | `skills/evidence-check/scripts/evidence_check.py#vendored_block_left_open` | confirmed | executed: 12,719 documents, none; 36 where the plugin answers no table are cmark-gfm's rows, the limit `hidden_lines` documents |
| 🟡 7 | a header or delimiter row after a form feed or U+2028 reads a table cmark-gfm does not render; the guard asks body rows only | `hooks/config.py#config_table` | open | executed: plugin reads `Mode shared`, cmark-gfm renders no table, for FF and U+2028 in both positions; the fix applied in the clone refuses all four breaks measured |
| 🟡 8 | the vendored twin reads an item the plugin refuses as written again below the stop | `skills/evidence-check/scripts/evidence_check.py#vendored_config_value` | open | executed: plugin "`Ledger frozen from` appears 2 times — one value", twin `100`; no `CONFIG_SHAPES` shape holds it |
| 🟡 9 | fold-check reads a row `config_value` gives no value; `broad_command`'s docstring says such a row is a value | `skills/settle/scripts/fold_check.py#config_rows` | open | executed: `declared` returns 400, `config_value` refuses; read: `broad_gate.py:840` |
| 🟡 10 | `rows_named_below` counts past the next heading, so a notes table doubles the config row | `hooks/config.py#rows_named_below` | open | executed: `Mode` refused as "appears 2 times" over a notes table under `## Notes`; `gfm_table` stops its stray rows at a heading |
| 🟡 11 | the twin tells a person to close a fence or a comment that closes below the header | `skills/evidence-check/scripts/evidence_check.py:4430` | open | executed: both `LACKS_BLOCK_STATE` example shapes get the never-closed sentences; no case pins either sentence |
| 🟡 12 | the twin says a fence, list, quote, HTML or code line under the table is one of its rows and to write it as a row | `skills/evidence-check/scripts/evidence_check.py:4496` | open | executed: cmark-gfm ends the table at all six lines and the plugin reads it whole; the build's sentence, opened beside 🟡 11 |
| 🟡 13 | `with_row`'s docstring narrates the stop rule the tree no longer has | `skills/implement/scripts/seal.py:1475` | open | read: the fifth instance of round 1's first question; no other in hooks, skills, templates, docs or agents |

## Executed probes

| What was run | Result |
|---|---|
| The vendored `evidence_check.py --strict .` over a scratch repository holding this repository's `seal/config.md`, and over one holding `NEW_CONFIG`'s output, at 383d9f19 and at c5dde1f7 | exit 0 and 0 at 383d9f19; exit 2 and 2 at c5dde1f7 with `REFUSED seal/config.md` |
| pytest over `tests/test_the_mode_question_is_asked_once.py -k "break_gfm or written_again or refused_append"` at 383d9f19, the worktree's `.venv` interpreter run in the clone, `SPECSEAL_CASE_CEILING_S=600` | exit 0, 10 passed |
| The S8 document case, and `tests/test_every_reader_ends_a_line_where_gfm_does.py`, `tests/test_a_format_has_one_reader.py`, `tests/test_a_reader_declares_its_input_class.py` at 383d9f19, ceiling 600 | exit 0, 1 passed; exit 0, 234 passed |
| cmark-gfm 2025.10.22 and the walker over FF and U+2028 between rows, between header and delimiter, and before the header | between rows: one row read and the rest refused, as rendered; the other two: walker reads `Mode shared`, cmark-gfm renders no table |
| `config_value` and `vendored_config_value` over `Mode` and `Ledger frozen from` each written again below a three-cell row | plugin refuses as appearing 2 times; twin reads `shared` and `100` |
| `fold_check.py#declared` over its three rows read, a three-cell row, and the ceiling written again below | returns 400; `config_value` refuses the row |
| `config_value` over a refused table and a notes table under `## Notes` headed by a `Mode` cell | refused as appearing 2 times |
| The twin's sentences over the four `LACKS_BLOCK_STATE` shapes, and over six block lines under the last row against cmark-gfm | the never-closed sentences for both closed-block shapes; "GFM reads as one of its rows" for all six, where cmark-gfm ends the table |
| Twin against plugin over 12,719 documents built from 23 line kinds above the header | 0 where the twin reads and the plugin refuses; 36 where the plugin answers no table, each a fence inside an HTML block of kinds 1–5, cmark-gfm rendering the twin's row in all 36 |
| `pact_signers` against cmark-gfm over a signer row, FF or U+2028, then a second signer row | the walker reads two signers, cmark-gfm renders one; deferred below |
| The fixes for 🟡 7–12 applied in the clone; reverted after | the shapes above answer as described in each finding; `tests/test_evidence_check.py -k "vendored or config or frozen or cutoff or removes"` exit 0, 49 passed; nine config, broad-gate, fold, reader and format modules exit 0, 606 passed; ceiling 600 |
| The broad gate (full suite, lint, typecheck) | not yet — the sealer's, after the rounds settle |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| A pact table's row after a form feed or U+2028 on another signer's line is read as a signer cmark-gfm does not render. It is the same cause as 🟡 7, at `gfm_table`, which this work item's guard does not reach. Pre-existing, and the pact tables are outside this work item | a new issue | the owner |

## Paste-ready fixes

### 🟡 7 — `hooks/config.py#config_table`

Replace the first line of the guard with the header and delimiter check
and keep the row loop under it:

```python
    kept = text.splitlines(keepends=True)
    head = rows[0][0] - 3 if rows else 0
    for piece in (head, head + 1) if rows else ():
        if piece > 0 and not kept[piece - 1].endswith(GFM_LINE_ENDS):
            return [], [
                f"has a `| {' | '.join(CONFIG_TABLE)} |` header that shares a "
                "line with the line beside it to GFM: a form feed, U+2028 or "
                "another character only Python ends a line at stands between "
                "them, so GitHub renders no table there — put the header and "
                "its delimiter row each on a line of its own"
            ]
    for at, (line, _cells) in enumerate(rows):
```

The docstring paragraph, rewritten in place:

```python
    **A row is a row only where it, the header and the delimiter row each
    begin a line GFM begins.** The walker reads `str.splitlines` pieces, and
    that ends a line at eight characters GFM reads as part of the line -- a
    form feed, U+2028 and six more. A row piece after one of them is the
    tail of the row above it, which GitHub shows cut off at its cells, so
    the walk stops there and refuses it, and the row above keeps the value
    GitHub shows. A header or delimiter piece after one is no table GitHub
    renders, so the walk refuses the table and reads no row.
```

The bullet, in `config_rows`' docstring, `templates/config.md` and
`skills/config/SKILL.md` in turn:

```python
      - a row, the header or the delimiter row after a form feed or U+2028
        on another line of the table: put it on a line of its own.
```

```markdown
- a row, the header or the delimiter row after a form feed or U+2028 on
  another line of the table, which GitHub shows as more of that line: put
  it on a line of its own.
```

```markdown
  - a row, the header or the delimiter row sharing a line with the line
    above, after a form feed or U+2028: give it a line of its own.
```

The case, in `tests/test_the_mode_question_is_asked_once.py`:

```python
@pytest.mark.parametrize("name", ["LS", "PS", "NEL", "FF", "VT", "FS", "GS", "RS"])
@pytest.mark.parametrize("where", ["above the header", "under the header"])
def test_a_header_after_a_break_gfm_does_not_honour_is_no_table(config, name, where):
    """#871 round 2, yellow 7. A header after a character only
    `str.splitlines` ends a line at, or a delimiter row after one on the
    header's line, is no table to cmark-gfm (measured for FF, U+2028, NEL
    and VT). The walk reads no row and refuses. Seen red against 383d9f19:
    `Mode` was read as `shared`."""
    from block_shapes import BREAKS

    brk = BREAKS[name]
    text = (
        f"# c\n\n{brk}| Item | Value |\n|---|---|\n| Mode | shared |\n"
        if where == "above the header"
        else f"# c\n\n| Item | Value |{brk}|---|---|\n| Mode | shared |\n"
    )
    assert config.config_rows(text) == [], config.config_rows(text)
    value, said = config.config_value(text, "Mode")
    assert value is None and "each on a line of its own" in (said or ""), said
```

### 🟡 8 — `skills/evidence-check/scripts/evidence_check.py#vendored_config_value`

Below `VENDORED_CONFIG_HEADER`:

```python
# `hooks/config.py#FIRST_CELL`, spelled as that file spells it: how the twin
# tells that a line the walk did not read names an item.
VENDORED_FIRST_CELL = re.compile(rf"^ {{0,3}}\|((?:{VENDORED_CELL})*)\|")
```

In `vendored_config_value`, after the `len(values) > 1` return. The
heading stop goes in only with 🟡 10's; without it, drop the three lines
that break at a heading, so the twin never counts fewer lines than the
plugin:

```python
    if values and refusals:
        below = 0
        for line in gfm_lines(text)[rows[-1][0] + 1 :]:
            if VENDORED_ATX_HEADING.match(line.lstrip(" ")) and not line.startswith(
                ("    ", "\t")
            ):
                break
            first = VENDORED_FIRST_CELL.match(line)
            if first and first.group(1).strip().replace("\\|", "|") == item:
                below += 1
        if below:
            return None, f"`{item}` appears {1 + below} times — one value"
```

In `tests/test_evidence_check.py`, two `CONFIG_SHAPES`:

```python
    # #871 round 2: an item written again below the line the walk stopped
    # at has no value, in the twin as in the plugin.
    "an item written again below the stop": _HEAD
    + "| Mode | shared |\n| a | b | c |\n| Mode | local |\n",
    "a cutoff written again below the stop": _HEAD
    + "| Ledger frozen from | 100 |\n| a | b | c |\n| Ledger frozen from | 200 |\n",
```

and in `test_the_vendored_table_grammar_is_the_walkers`:

```python
    assert (ec.VENDORED_FIRST_CELL.pattern, ec.VENDORED_FIRST_CELL.flags) == (
        config.FIRST_CELL.pattern,
        config.FIRST_CELL.flags,
    )
```

### 🟡 9 — `skills/settle/scripts/fold_check.py#config_rows` and `broad_gate.py:840`

```python
    rows, refusals = reader.config_table(text)
    read = {item for _index, item, _value in rows}
    if refusals and not {SHAPE_ROW, CEILING_ROW, OVER_ROW} <= read:
        raise Unusable(f"the file {refusals[0]}")
    for item in (SHAPE_ROW, CEILING_ROW, OVER_ROW) if refusals else ():
        refused = reader.config_value(text, item)[1]
        if refused is not None:
            raise Unusable(refused)
    return [(item, value) for _index, item, value in rows]
```

The docstring's last sentence:

```python
    gave. A refusal below all three rows touches none of them, unless one of
    them is written again below it: `config_value` gives that row no value,
    and neither does this command."""
```

`skills/verify/scripts/broad_gate.py:839–841`, in `broad_command`:

```python
    edit, which is `missing_row`'s to write. A row the walk read above a
    line it refused is a value, and the gate runs it: GitHub shows that row
    as the person wrote it. A line below that one naming the row again makes
    it a row written twice, which has no value (`config_value`)."""
```

In `tests/test_a_document_has_room_for_the_next_fold.py`:

```python
def test_a_fold_row_written_again_below_the_stop_has_no_value(tmp_path):
    """#871 round 2, yellow 9. A row read above a line the walk refused and
    written again below it has no value, in fold-check as in
    `config_value`. Seen red against 383d9f19: `declared` returned 400."""
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    path = os.path.join(root, "skills", "settle", "scripts", "fold_check.py")
    spec = importlib.util.spec_from_file_location("fold_check_for_871_r2", path)
    fold = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fold)
    (tmp_path / "config.md").write_text(
        "# c\n\n| Item | Value |\n|---|---|\n| Fold shape from | 100 |\n"
        "| Document line ceiling | 400 |\n| Over the ceiling | none |\n"
        "| a | b | c |\n| Document line ceiling | 9000 |\n",
        encoding="utf-8",
    )
    with pytest.raises(fold.Unusable, match="appears 2 times"):
        fold.declared(str(tmp_path))
```

### 🟡 10 — `hooks/config.py#rows_named_below`

```python
    """How many lines of TEXT below the line at INDEX and above the next
    heading, of those the walk is shown, name ITEM in their first cell --
    the stretch `gfm_table` calls rows nobody reads.

    Reads: guess — the lines of a person's `config.md` below the last row the walk read; unknown refused"""
    count = 0
    for at, line in unfenced(text.splitlines(), text):
        if at <= index:
            continue
        if ATX_HEADING.match(line.lstrip(" ")) and blocks.columns(line) < 4:
            break
        first = FIRST_CELL.match(line)
        if first and unescaped(first.group(1).strip()) == item:
            count += 1
    return count
```

In `config_value`'s docstring:

```python
    what keeps a fenced example from doubling the live row. **In a table the
    walk refused, a line written below its last row and above the next
    heading that names ITEM in its first cell counts too**: the walk did not
```

In `tests/test_the_mode_question_is_asked_once.py`:

```python
def test_an_item_named_under_the_next_heading_is_another_tables(config):
    """#871 round 2, yellow 10. A table under the next heading is not below
    the line the walk stopped at, so a `Mode` cell in it does not double the
    config's `Mode` row. Seen red against 383d9f19: "appears 2 times"."""
    text = TABLE.format(
        rows="| Mode | shared |\n| a | b | c |\n\n## Notes\n\n"
        "| Mode | what it means |\n|---|---|\n| local | x |\n"
    )
    assert config.config_value(text, "Mode") == ("shared", None)
```

### 🟡 11 — `skills/evidence-check/scripts/evidence_check.py:4430`

A helper beside `vendored_block_left_open`:

```python
def vendored_block_closes_below(lines, at, opener):
    """Whether the block OPENER opened, still open at line AT of LINES,
    closes on a line below AT.

    Reads: guess — the lines of a person's `config.md` below its header; unknown refused"""
    fence = vendored_fence_opener(opener)
    if fence is not None:
        return any(vendored_fence_closes(line, fence) for line in lines[at + 1 :])
    content = opener.lstrip(" ")
    closer = next(end for start, end in VENDORED_RAW_HTML if start.match(content))
    return any(closer.search(line) for line in lines[at + 1 :])
```

and, in `vendored_config_rows`, a branch before the two never-closed
sentences:

```python
    opener = vendored_block_left_open(lines[:at])
    if opener is not None and vendored_block_closes_below(lines, at, opener):
        return [], [
            f"has a `| {name} |` header inside a block `{opener.strip()}` "
            "opens above it and that closes below it — an example table a "
            "copy of the checker with no `hooks/` beside it cannot tell from "
            "the live one; take the example out of this file, or run the "
            "plugin's own `evidence-check`"
        ]
```

In `tests/test_evidence_check.py`:

```python
def test_the_twin_names_an_example_table_inside_a_closed_block():
    """#871 round 2, yellow 11. A header inside a fence or a comment that
    closes below it is an example the twin cannot tell from the live table:
    its sentence says so, never that the block is unclosed. Seen red
    against 383d9f19, which said "never closed" for both."""
    ec = _checker("ec_vendored_example_table")
    for name in (
        "a fenced example above the live table",
        "a commented old table above the live one",
    ):
        said = ec.vendored_config_rows(LACKS_BLOCK_STATE[name])[1]
        assert said and "closes below it" in said[0], (name, said)
        assert "never closed" not in said[0], (name, said)
    unclosed = "# c\n\n```\n\n| Item | Value |\n|---|---|\n| Mode | shared |\n"
    said = ec.vendored_config_rows(unclosed)[1]
    assert said and "close the fence above the table" in said[0], said
```

### 🟡 12 — `skills/evidence-check/scripts/evidence_check.py:4496`

In `vendored_config_rows`' loop, a branch before `elif "|" in line:`:

```python
        elif (
            line.startswith(("    ", "\t"))
            or vendored_fence_opener(line) is not None
            or VENDORED_LIST_ITEM.match(line.lstrip(" "))
            or line.lstrip(" ").startswith(("<", ">"))
        ):
            stray = (
                f"has a `{name}` table that stops at `{line.strip()}`, a line "
                "that may end the table by block state a copy of the checker "
                "with no `hooks/` beside it does not carry — leave a blank line "
                "above it, or run the plugin's own `evidence-check`"
            )
```

In `tests/test_evidence_check.py`:

```python
@pytest.mark.parametrize("line", ["```", "- item", "> quoted", "    code", "<div>"])
def test_the_twin_does_not_call_a_block_line_a_row(line):
    """#871 round 2, yellow 12. cmark-gfm ends the table at each of these
    lines, so the twin's refusal names what it cannot judge and the blank
    line that clears it. Seen red against 383d9f19, which said GFM reads
    the line as one of the table's rows."""
    ec = _checker("ec_vendored_block_line")
    said = ec.vendored_config_rows(_HEAD + "| Mode | shared |\n" + line + "\n")[1]
    assert said and "leave a blank line above it" in said[0], said
    assert "reads as one of its rows" not in said[0], said
```

### 🟡 13 — `skills/implement/scripts/seal.py:1474–1476`

```python
    itself starts at. A writer with a walk of its own is the file two rows
    deep (#429, #415): a `Mode` row it adds under a line its walk reads past
    is a second `Mode` row to a reader that stops there. **A table the
    walker refused is refused here** in the
```

Needs a fix: yes — 🟡 7 (a header after a break reads a table GitHub does
not render), 🟡 8 (the twin reads an item the plugin refuses), 🟡 9
(fold-check reads it too), 🟡 10 (the count runs past the next heading),
🟡 11 and 🟡 12 (the twin's refusal sentences name a wrong edit), 🟡 13
(a fifth narrating docstring)
Loses a record or crashes: no

The broad gate has not run. Nothing here is due to it yet: the rounds have
not settled while 🟡 7–13 stand open.

## Proof block

```
📋 code-review applied (warden, round 2, verifying)
· target:   383d9f19, a --no-local clone; the fix diff aa0fc421..946360ab
· read:     rounds/round-1.md and round-1-report.md; the fix diff of
            hooks/config.py, skills/evidence-check/scripts/evidence_check.py,
            skills/implement/scripts/seal.py, skills/verify/scripts/broad_gate.py,
            templates/config.md, skills/config/SKILL.md and the four test
            files; hooks/config.py config_table through value_of, hidden_lines,
            gfm_table, html_start, raw_html_open, pact_declaration;
            evidence_check.py from the vendored grammar through cutoff_row;
            seal.py doubled_modes, with_row, write_row, mode_refusal;
            broad_gate.py broad_command, refused_broad_row, fenced_row;
            fold_check.py config_rows and declared; tests/test_evidence_check.py
            CONFIG_SHAPES through the grammar case; the ledger fragment's rows
            N8, N10 and N11; the changelog and survivors diffs; seal/config.md
· executed: the probes in the table above, exit codes read directly; the
            clone's edits were reverted, the probe files deleted, and the
            clone removed
· unverified: the full suite, lint and typecheck — the sealer's, after the
            rounds settle
```
