# 1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker — review round 1

| Field | Value |
|---|---|
| Target SHA | c5dde1f706b53912acbc3fc705a848b72a66936f |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #925 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are not yet written |
| Fix range | none — the fixes are not yet written |
| Contract changes | none — the fixes are not yet written |
| New units | none — the fixes are not yet written |
| Fix of a fix | no |
| Needs a fix | yes — 🔴 1 (the vendored twin refuses every plugin-written config), 🟡 2 (`seal mode` names the wrong cause), 🟡 3 (the remedy for a second table), 🟡 4 (a row GitHub does not show is still read), 🟡 5 (prose naming a structure that is gone) |
| Loses a record or crashes | no |

- [ ] Pass

## What this round was asked

Round 1 of #871, target c5dde1f7 against `origin/release/v0.21.1`'s merge-base 321e9de1, over the whole build, phases 1–4. The reviewer was asked to check that this repository's own config, the one `seal mode` writes and the template's are read in full with nothing refused and that no hook asks or denies on a refusal (the owner asked that the change add no yes/no prompts); to judge the divergences in `overview.md` and `survivors.md`'s 47 answered places; to judge the open item on a comment opener after a character only Python's `splitlines` breaks at; and to check every doc, template and skill edit against the owner's rule that a change rewrites the existing text in place.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🔴 1 | The vendored checker refuses every config `seal mode` writes, this repository's own included, so an installed repository's evidence-check CI step exits 2 after its next `/specseal:evidence-ci` | `skills/evidence-check/scripts/evidence_check.py:4382` | open | executed: the twin refuses this repository's config and `NEW_CONFIG`; the vendored checker exits 2 at c5dde1f7 and 0 at 321e9de1 over the same repository |
| 🟡 2 | `seal mode`'s read-back guard calls a walker refusal "a defect in this command" | `skills/implement/scripts/seal.py:1591` | open | executed: a file with no table and an unclosed comment gets the generic sentence; the walker names the real cause |
| 🟡 3 | A second table under the config table before a heading is refused, and all three documents give "move it into the table" as its only remedy | `templates/config.md:62` | open | executed: cmark-gfm renders both tables; the base read the config rows with no refusal; the walker refuses; the heading remedy is named nowhere |
| 🟡 4 | The walker reads a row cmark-gfm does not render where a row shares its GFM line with another after FF or U+2028; the overview's Not verified row names only the harmless member of the class | `hooks/config.py#config_table` | open | executed: two rows read against one rendered; the base read the same, so not a regression, but S1 and the overview's claim are false of it |
| 🟡 5 | Prose states a structure the tree no longer has: "all three walks" in three places, and "the shape this repository's own config has" for a last-row Broad gate line | `templates/config.md:314` | open | read: also `hooks/config.py:151`, `skills/verify/scripts/broad_gate.py:1026` and `:1108`; the Broad gate row is second of seven here and fourth of seven in the template |
| ⬜ 6 | survivors.md's ground "Still true of this repository's config and the template's table" is false | `seal/specs/1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker/survivors.md` | open | read: neither table ends with the Broad gate row; a correction to the run's paperwork |
| 🟢 | The plugin's walker reads this repository's config, the template's table and the config `seal mode` writes whole, with nothing refused | `hooks/config.py#config_table` | confirmed | executed: 7, 7 and 1 rows, refusals empty |
| 🟢 | No hook asks, denies or prints on a refused table; the prompt budget is zero | `hooks/mode-gate.py:163` | confirmed | read, and the hook cases over shapes 1, 5 and 7 passed in the module run |
| 🟢 | Each of the overview's seven divergences has grounds the tree supports | `seal/specs/1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker/overview.md` | confirmed | read, each against its coordinate |
| 🟢 | Every released-row entry of survivors.md names a Corrected or Re-read row that exists in the fragment | `seal/ledger/1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker.md` | confirmed | read, all 23 released-file rows |
| 🟢 | The edited markdown documents rewrite in place and narrate nothing | `templates/config.md:45` | confirmed | read: also `skills/config/SKILL.md:104`, `skills/implement/orchestration.md:168`, `docs/the-broad-gate.md:84` |
| ❓ | Whether the owner's in-place rule reaches code docstrings: four narrate the change | `hooks/config.py:331` | ❓ out of verified scope | also `hooks/config.py:257`, `:1085` and `skills/verify/scripts/broad_gate.py:1114`; the rule names doc, template and skill, and a docstring is none of those by name; the owner answers it |
| ❓ | Whether a row the walk read is a value when the same item is written again below the stopping line | `hooks/config.py#config_value` | ❓ out of verified scope | S2 says the read row is a value, #867 says a doubled row has none, and `pact_declaration` alone guards the case; not a regression; the owner answers it |

## Paste-ready fixes

```python
# What this copy can follow above the header without `hooks/blocks.py`: a
# fence, by the twin's own fence rule, and an HTML block of CommonMark 4.6's
# kinds 1-5, the kinds no blank line ends, spelled as
# `hooks/config.py#HTML_KINDS` spells them. A block still open at the header
# is refused; one that closed above it hides nothing from GFM, so a header
# under a closed comment -- the one `seal.py#NEW_CONFIG` writes into every
# config -- is read.
VENDORED_RAW_HTML = (
    (
        re.compile(r"<(?:script|pre|style|textarea)(?:[ \t>]|$)", re.I),
        re.compile(r"</(?:script|pre|style|textarea)>", re.I),
    ),
    (re.compile(r"<" r"!--"), re.compile(r"-->")),
    (re.compile(r"<\?"), re.compile(r"\?>")),
    (re.compile(r"<![A-Za-z]"), re.compile(r">")),
    (re.compile(r"<!\[CDATA\["), re.compile(r"\]\]>")),
)


def vendored_block_left_open(lines):
    """The line opening a fence or an HTML block of kinds 1-5 that is still
    open after LINES, as written, or None where every such block closed.

    Reads: guess — the lines of a person's `config.md` above its header; unknown refused"""
    fence, end, opener = None, None, None
    for line in lines:
        if fence is not None:
            if vendored_fence_closes(line, fence):
                fence, opener = None, None
            continue
        if end is not None:
            if end.search(line):
                end, opener = None, None
            continue
        if line.startswith(("    ", "\t")):
            continue
        fence = vendored_fence_opener(line)
        if fence is not None:
            opener = line
            continue
        content = line.lstrip(" ")
        for start, closer in VENDORED_RAW_HTML:
            if start.match(content):
                if not closer.search(content, 1):
                    end, opener = closer, line
                break
    return opener
```
```python
    opener = vendored_block_left_open(lines[:at])
```
```python
    # The shape every config `seal mode` writes, `seal.py#NEW_CONFIG`: a
    # closed comment above the header, a blank line between (#871 round 1).
    "the config seal mode writes": "# Repository config\n\n"
    + config_shapes.OPEN
    + " What this repository says about itself. This file was\n"
    + "created by `seal mode`. "
    + config_shapes.CLOSE
    + "\n\n| Item | Value |\n|---|---|\n| Mode | shared |\n",
```
```python
    assert [
        (s.pattern, s.flags, e.pattern, e.flags) for s, e in ec.VENDORED_RAW_HTML
    ] == [(s.pattern, s.flags, e.pattern, e.flags) for s, e in config.HTML_KINDS[:5]]
```
```python
        walked = config_table(new)[1]
        if walked:
            return (
                f"{path}, with the `{ROW_ITEM}` row written into it, "
                f"{walked[0]}. Nothing was written and your file is exactly "
                "as it was"
            )
```
```markdown
- a row under a comment, a fence or a blank line that ends the table: move
  it into the table; where it heads a table of something else, put a
  heading between the two tables.
```
```markdown
  - a row stranded after a comment, a fence or an empty line: move it into
    the table; if it belongs to another table, put a heading between the two.
```
```python
      - a row under a comment, a fence or a blank line that ends the table:
        move it into the table; where it heads another table, put a
        heading between the two.
```
```python
    rows, refusals = gfm_table(text, CONFIG_TABLE)
    if refusals and refusals[0].startswith("holds no "):
        return [], []
    kept = text.splitlines(keepends=True)
    for at, (line, _cells) in enumerate(rows):
        if line > 1 and not kept[line - 2].endswith(GFM_LINE_ENDS):
            read = [(n - 1, item, value) for n, (item, value) in rows[:at]]
            return read, [
                f"has a `{' | '.join(CONFIG_TABLE)}` table that stops at "
                f"`{kept[line - 1].strip()}`, which is not a row of its own "
                "to GFM: a form feed, U+2028 or another character only "
                "Python ends a line at stands before it, so GitHub reads it "
                "as more of the line above — put it on a line of its own"
            ]
    return [(line - 1, item, value) for line, (item, value) in rows], refusals


# Where GFM ends a line. `str.splitlines` also ends one at eight characters
# GFM reads as part of the line -- a form feed, U+2028 and six more -- so a
# piece the walk reads as a row may be the tail of a line GitHub shows as
# the row above it.
GFM_LINE_ENDS = ("\r\n", "\n", "\r")
```
```markdown
line somebody wrote as a row. One rule says so and the one walk of this
table reads through it — the gates, the mode gate, and `seal mode`'s writer
all read the rows it names — so the reader and the writer can never
disagree about which row is the row.
```
```python
    `unfenced` below is the generator form the one walk of every table reads
    the file through, and this is the same walk with the state it ENDS in kept. A fence
```
```python
    only one that may ask it.** `hooks/config.py#unfenced` makes a fenced line
    invisible to the one walk of that table, which is what stops an example
```
```python
        line written `| … |` stands below it. A `Broad gate` line written
        LAST in its table — the shape a stub `seal mode` wrote can take —
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test tests/test_one_table_walker_reads_what_gfm_renders.py -q -p no:xdist` at c5dde1f7, with `SPECSEAL_CASE_CEILING_S=600` | exit 0, 894 passed |
| `bin/test` over the seven touched modules: the mode question, the signer's pact, the pull-request language, the mode row, pact-check, first setup, and the sealer; ceiling 600 | exit 0, 3601 passed |
| `bin/test tests/test_evidence_check.py -q -k "vendored_config or vendored_table"`, ceiling 600 | exit 0, 39 passed |
| The plugin walker and the twin over this repository's config, the template and `NEW_CONFIG` | plugin: 7, 7 and 1 rows with no refusal; twin: refuses this repository's config and `NEW_CONFIG`, reads the template |
| The vendored `evidence_check.py --strict .` over a scratch repository holding this repository's config, at c5dde1f7 and at 321e9de1 | exit 2 with REFUSED seal/config.md at c5dde1f7; exit 0 at 321e9de1 |
| cmark-gfm 2025.10.22 against the walker: FF and U+2028 mid-row, the smith's open-item shape with and without its closer, a second table under the config table, an indented code line under it | rendered one row, the walker read two; the walker refused at the header where GFM shows `Mode`; GFM rendered both tables and the code, the walker refused both |
| The base's `config_rows` on the mid-row and second-table shapes | the mid-row Broad gate row was read at the base too; the second-table shape was read at the base with no refusal |
| `write_row` and `mode_refusal` over a file with no table and an unclosed comment, and over a read Mode row with a stray line below | the generic "defect in this command" sentence; refused naming the stray line, file unchanged |
| The 🔴 1 fix applied to a copy of the checker, over `CONFIG_SHAPES`, `NEW_CONFIG`, this repository's config and `LACKS_BLOCK_STATE` | 32 shapes equal to the plugin, 4 direction shapes refuse, 0 bad |
| The 🟡 4 guard applied in the clone, five modules with `-k "config or Mode or mode or pact or walker or gfm or broad or refus"`; reverted after | exit 0, 3793 passed; FF and U+2028 read Mode only and refuse Broad gate |
| A walker-level alternative for 🟡 3 (stop at another table's header) applied in the clone; reverted after | exit 1: breaks the pinned pact case and the four-column case named in 🟡 3 |
| The broad gate (full suite, lint, typecheck) | not yet — the sealer's, after the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
