# 1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker — review round 3

| Field | Value |
|---|---|
| Target SHA | 46063a511f525a5c567db56226eed19f173f2c94 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #925 |
| Broad gate | not yet |
| Fixes checked by | no fixes to check |
| Fix range | none |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 14 (a closed block below the table makes the vendored CI step exit 2 on a config the plugin reads whole), 🟡 15 (the twin doubles a row named under the next heading) |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Round 3 of #871, the verifying round after the run's one reopening, target 46063a51: the diff of round 2's fixes, `4dfb3d0d..40fab1ec`. The reviewer was asked whether 🟡 7–13 are closed, to treat the units round 2 added as a finding surface, to check the line-start guard moved into `gfm_table` and the pact tables it now covers, the ten re-pinned pact-change cases against the orchestrator's answer to Q7 (exit 2 stands), and the twin counting a written-again item to the end of the file. The run ends at this record; its two open findings go to #928, in milestone 0.21.1, fixed before release.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 14 | a closed comment, fence or `<` line below the table makes the twin refuse every `\| … \|` line under every later heading, so the vendored CI step exits 2 on a config the plugin reads whole | `skills/evidence-check/scripts/evidence_check.py#vendored_config_rows` | deferred #928 | executed: vendored `--strict .` exits 0 at 4dfb3d0d and 2 at 46063a51 over the same config; the plugin refuses nothing; cmark-gfm renders both tables; the fix applied in the clone is green. A unit round 2's fixes changed (91d9225d); the run ends here under the reopening bound |
| 🟡 15 | the twin counts an item named in a table under the next heading, where the plugin stops at the heading, and says the row appears twice | `skills/evidence-check/scripts/evidence_check.py#vendored_config_value` | deferred #928 | executed: on round 2's 🟡 10 shape the plugin reads `shared` and `100`, the twin refuses both as "appears 2 times"; the docstring's reason is false of `vendored_config_rows`' own walk. A unit round 2's fixes changed (91d9225d); the same issue as 🟡 14, whose helper it uses |
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

## Paste-ready fixes

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
```python
    if values and refusals:
        for _below, line, _block in vendored_below(gfm_lines(text), rows[-1][0] + 1):
            first = VENDORED_FIRST_CELL.match(line)
            if first and first.group(1).strip().replace("\\|", "|") == item:
                values.append(None)
```
```python
    In a table the walk refused, a line below its last row naming ITEM in
    its first cell makes the row read above it one of two, as it does to
    the plugin, down to the next heading outside a block opened below the
    table (`vendored_below`). A heading inside a fence or an HTML block this
    copy saw open is no stop, so it counts every line the plugin may count,
    and refuses where the plugin reads rather than the other way round.
```

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
| round-2 | `skills/evidence-check/scripts/evidence_check.py:4430` | round 2's 🟢 — confirmed |
| round-2 | `skills/implement/scripts/seal.py:1593` | round 2's 🟢 — confirmed |
| round-2 | `skills/evidence-check/scripts/evidence_check.py#vendored_block_left_open` | round 2's 🟢 — confirmed |
| round-2 | `skills/evidence-check/scripts/evidence_check.py#vendored_config_value` | round 2's 🟡 8 — fixed |
| round-2 | `skills/settle/scripts/fold_check.py#config_rows` | round 2's 🟡 9 — fixed |
| round-2 | `hooks/config.py#rows_named_below` | round 2's 🟡 10 — fixed |
| round-2 | `skills/evidence-check/scripts/evidence_check.py:4496` | round 2's 🟡 12 — fixed |
| round-2 | `skills/implement/scripts/seal.py:1475` | round 2's 🟡 13 — fixed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| 🟡 14: the twin refuses every table under every later heading after a closed block below the config table | a new issue, labelled `from-review` — rung 3; rung 1 fits by ownership, and the reopening bound allows no fix pass | the repository owner: v0.21.1 ships this vendored checker into installed CI, and the verified fix in this report lets the owner take it onto this branch instead |
| 🟡 15: the twin doubles a row named under the next heading | the same issue as 🟡 14, whose helper it uses | the repository owner, with 🟡 14 |
