# 1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker — review round 2

| Field | Value |
|---|---|
| Target SHA | 383d9f198a497af7b1adc5eb62d602431281b80a |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #925 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are written and no round has opened them |
| Fix range | `4dfb3d0d9bb0a2fc4a4dec1ed4291dd53f1a87ce..40fab1ec06e7658ac941a3c46cddf1dd82ad0bed`, 11 commits |
| Contract changes | test_a_vendored_copy_under_a_notify_row_leaves_a_row_citing_no_clause → pytest only; test_s6_a_pact_line_below_the_table_leaves_the_moved_row → pytest only; test_s9_a_vendored_copy_leaves_where_the_plugin_refuses_a_pact_line → pytest only |
| New units | gfm_line_starts (depth 1); VENDORED_FIRST_CELL (depth 1); VENDORED_THEMATIC_BREAK (depth 1); VENDORED_PIECE_BREAK (depth 1); vendored_block_closes_below (depth 1); test_a_fold_row_written_again_below_the_stop_has_no_value (depth 1); walk_refused (depth 1); assert_refused_by_the_walk (depth 1); test_the_twin_names_an_example_table_inside_a_closed_block (depth 1); test_the_twin_does_not_call_a_block_line_a_row (depth 1); test_a_signer_after_a_break_gfm_does_not_honour_is_no_signer (depth 1); test_a_heading_after_a_break_does_not_end_the_rows_nobody_reads (depth 1); test_a_header_after_a_break_gfm_does_not_honour_is_no_table (depth 1); test_an_item_named_under_the_next_heading_is_another_tables (depth 1); test_a_line_below_the_stop_is_a_line_where_gfm_begins_one (depth 1) |
| Fix of a fix | first — 🟡 7 at hooks/config.py#config_table, a unit round-1's fixes changed; 🟡 10 at hooks/config.py#rows_named_below, a unit round-1's fixes added; 🟡 11 at skills/evidence-check/scripts/evidence_check.py#vendored_config_rows, a unit round-1's fixes changed; 🟡 12 at skills/evidence-check/scripts/evidence_check.py#vendored_config_rows, a unit round-1's fixes changed |
| Needs a fix | yes — 🟡 7 (a header after a break reads a table GitHub does not render), 🟡 8 (the twin reads an item the plugin refuses), 🟡 9 (fold-check reads it too), 🟡 10 (the count runs past the next heading), 🟡 11 and 🟡 12 (the twin's refusal sentences name a wrong edit), 🟡 13 (a fifth narrating docstring) |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 2 of #871, the verifying round, target 383d9f19: the diff of round 1's fixes, `aa0fc421..946360ab`. The reviewer was asked whether 🔴 1 and 🟡 2–5 are closed — re-running the vendored checker on a repository holding this repository's config and on one holding the config `seal mode` writes — to treat the units the fixes added as a finding surface, and to check the orchestrator's two answers: the rewrite-in-place rule applied to docstrings, and an item written again below the stop holding no value.

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
| 🟡 7 | a header or delimiter row after a form feed or U+2028 reads a table cmark-gfm does not render; the guard asks body rows only | `hooks/config.py#config_table` | **fixed** `c21fd899` | fixed at c21fd899; executed: plugin reads `Mode shared`, cmark-gfm renders no table, for FF and U+2028 in both positions; the fix applied in the clone refuses all four breaks measured |
| 🟡 8 | the vendored twin reads an item the plugin refuses as written again below the stop | `skills/evidence-check/scripts/evidence_check.py#vendored_config_value` | **fixed** `91d9225d` | fixed at 91d9225d; executed: plugin "`Ledger frozen from` appears 2 times — one value", twin `100`; no `CONFIG_SHAPES` shape holds it |
| 🟡 9 | fold-check reads a row `config_value` gives no value; `broad_command`'s docstring says such a row is a value | `skills/settle/scripts/fold_check.py#config_rows` | **fixed** `191b343b` | fixed at 191b343b; executed: `declared` returns 400, `config_value` refuses; read: `broad_gate.py:840` |
| 🟡 10 | `rows_named_below` counts past the next heading, so a notes table doubles the config row | `hooks/config.py#rows_named_below` | **fixed** `176d03b5` | fixed at 176d03b5; executed: `Mode` refused as "appears 2 times" over a notes table under `## Notes`; `gfm_table` stops its stray rows at a heading |
| 🟡 11 | the twin tells a person to close a fence or a comment that closes below the header | `skills/evidence-check/scripts/evidence_check.py:4430` | **fixed** `91d9225d` | fixed at 91d9225d; executed: both `LACKS_BLOCK_STATE` example shapes get the never-closed sentences; no case pins either sentence |
| 🟡 12 | the twin says a fence, list, quote, HTML or code line under the table is one of its rows and to write it as a row | `skills/evidence-check/scripts/evidence_check.py:4496` | **fixed** `91d9225d` | fixed at 91d9225d; executed: cmark-gfm ends the table at all six lines and the plugin reads it whole; the build's sentence, opened beside 🟡 11 |
| 🟡 13 | `with_row`'s docstring narrates the stop rule the tree no longer has | `skills/implement/scripts/seal.py:1475` | **fixed** `aaba2cd9` | fixed at aaba2cd9; read: the fifth instance of round 1's first question; no other in hooks, skills, templates, docs or agents |

## Paste-ready fixes

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
```python
# `hooks/config.py#FIRST_CELL`, spelled as that file spells it: how the twin
# tells that a line the walk did not read names an item.
VENDORED_FIRST_CELL = re.compile(rf"^ {{0,3}}\|((?:{VENDORED_CELL})*)\|")
```
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
```python
    # #871 round 2: an item written again below the line the walk stopped
    # at has no value, in the twin as in the plugin.
    "an item written again below the stop": _HEAD
    + "| Mode | shared |\n| a | b | c |\n| Mode | local |\n",
    "a cutoff written again below the stop": _HEAD
    + "| Ledger frozen from | 100 |\n| a | b | c |\n| Ledger frozen from | 200 |\n",
```
```python
    assert (ec.VENDORED_FIRST_CELL.pattern, ec.VENDORED_FIRST_CELL.flags) == (
        config.FIRST_CELL.pattern,
        config.FIRST_CELL.flags,
    )
```
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
```python
    gave. A refusal below all three rows touches none of them, unless one of
    them is written again below it: `config_value` gives that row no value,
    and neither does this command."""
```
```python
    edit, which is `missing_row`'s to write. A row the walk read above a
    line it refused is a value, and the gate runs it: GitHub shows that row
    as the person wrote it. A line below that one naming the row again makes
    it a row written twice, which has no value (`config_value`)."""
```
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
```python
    what keeps a fenced example from doubling the live row. **In a table the
    walk refused, a line written below its last row and above the next
    heading that names ITEM in its first cell counts too**: the walk did not
```
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
```python
    itself starts at. A writer with a walk of its own is the file two rows
    deep (#429, #415): a `Mode` row it adds under a line its walk reads past
    is a second `Mode` row to a reader that stops there. **A table the
    walker refused is refused here** in the
```

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

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `skills/evidence-check/scripts/evidence_check.py:4382` | round 1's 🔴 1 — fixed |
| round-1 | `skills/implement/scripts/seal.py:1591` | round 1's 🟡 2 — fixed |
| round-1 | `templates/config.md:62` | round 1's 🟡 3 — fixed |
| round-1 | `hooks/config.py#config_table` | round 1's 🟡 4 — fixed |
| round-1 | `templates/config.md:314` | round 1's 🟡 5 — fixed |
| round-1 | `seal/specs/1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker/survivors.md` | round 1's ⬜ 6 — open |
| round-1 | `hooks/mode-gate.py:163` | round 1's 🟢 — confirmed |
| round-1 | `seal/specs/1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker/overview.md` | round 1's 🟢 — confirmed |
| round-1 | `seal/ledger/1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker.md` | round 1's 🟢 — confirmed |
| round-1 | `templates/config.md:45` | round 1's 🟢 — confirmed |
| round-1 | `hooks/config.py:331` | round 1's ❓ — out of verified scope |
| round-1 | `hooks/config.py#config_value` | round 1's ❓ — out of verified scope |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| A pact table's row after a form feed or U+2028 on another signer's line is read as a signer cmark-gfm does not render. It is the same cause as 🟡 7, at `gfm_table`, which this work item's guard does not reach. Pre-existing, and the pact tables are outside this work item | a new issue | the owner |
