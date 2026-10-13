# Round 1 — the config table is read by the walker cmark-gfm holds (#871)

Target SHA: c5dde1f7 · base: the merge-base 321e9de1 · scope: the whole
build, phases 1–4 · reviewed in a `git clone --no-local` at the target SHA.

## How the findings relate

The move itself holds in the plugin. Inside `hooks/config.py` the config
table now has one walk, every caller reads it, and no hook asks or denies on
a refusal. The defects sit at the edges the move reached, one cause each:

```
the walker refuses more than the stop rule did
  ├─ a copy that walks without the plugin's block state refuses more again
  │     → 🔴 1  the vendored checker refuses every config `seal mode` writes
  ├─ refusals now reach code written before refusals could reach it
  │     → 🟡 2  `seal mode` calls a walker refusal a defect in itself
  ├─ a shape GitHub renders that the 16 measured shapes do not hold
  │     → 🟡 3  a second table under the config table: refused, wrong remedy
  └─ the walker reads `str.splitlines` pieces, not GFM lines
        → 🟡 4  a row GitHub does not show is still read (the open item's class)
the prose kept a structure that is gone
        → 🟡 5  "all three walks", and a claim about this repository's config
        → ⬜ 6  survivors.md grounds one row on that same false claim
```

## Findings

### 🔴 1 — The vendored checker refuses every config `seal mode` writes

`skills/evidence-check/scripts/evidence_check.py:4382`, in
`vendored_config_rows`. Executed.

The twin refuses a header with any line above it that starts with `<`
(`VENDORED_BLOCK_OPENER`, line 4302). It does not ask whether that block is · NAME NOT IN TREE
still open. `skills/implement/scripts/seal.py#NEW_CONFIG` writes a closed
`&lt;!-- … -->` comment above the header into every config it creates, and
this repository's own `seal/config.md` has the same comment. So the twin
refuses both. The plugin's walker reads both whole.

Why it matters: `templates/evidence-check.yml` runs
`python3 tools/evidence_check.py --strict .`, and the records arm reads
`Removes from` through `cutoff_row`. Measured over a repository holding this
repository's config and the vendored file alone, the branch's checker exits
2 with `REFUSED seal/config.md`, and the base's checker exits 0. Every
installed repository whose config `seal mode` wrote fails that CI step after
its next `/specseal:evidence-ci`. The refusal then tells the person to "take
that line out of this file", which is the comment the plugin wrote there.

The changelog says the twin refuses "a fence or an HTML line above the
header". It does not say that every plugin-written config has one. The
equality table `tests/test_evidence_check.py#CONFIG_SHAPES` holds no closed
comment above the header, which is how the case stayed green.

The fix follows a fence and an HTML block of kinds 1–5 to their close, and
refuses only one still open at the header. A block of kinds 6 and 7 ends at
the blank line that the walker already requires. Executed against the fix:
all 30 equality shapes, plus `NEW_CONFIG` and this repository's config, come
out equal to the plugin's walker. All four `LACKS_BLOCK_STATE` shapes still
refuse. The fix reuses `vendored_fence_opener` and `vendored_fence_closes`
rather than adding a third fence pattern.

### 🟡 2 — `seal mode` calls a walker refusal "a defect in this command"

`skills/implement/scripts/seal.py:1591`, in `write_row`. Executed.

Take a hand-written `config.md` that has no table and holds an `&lt;!--`
that never closes. `with_row` appends a table at the end. The walker then
refuses the appended header ("inside an HTML block opened above it and never
closed"), so the read-back guard fails. The guard's generic sentence then
says: *"This is a defect in this command rather than in your file: please
report it with the file's first lines."*

The guard's own comment says *"the next member of the class must not be
misdescribed either"*. This is that next member. The base wrote the row
there, into a block GitHub does not render. The branch writes nothing,
which is the better direction, but it names the wrong cause. The fix prints
the walker's sentence when the walk refuses the text it would write.

### 🟡 3 — A second table under the config table is refused, and the documents' remedy for it is wrong

`templates/config.md:62`, `skills/config/SKILL.md:119` and
`hooks/config.py:384` (the remedy). `hooks/config.py#gfm_table` is the walk
that refuses. Executed against cmark-gfm 2025.10.22.

A config written as the Item/Value table, a blank line, a line of prose, and
then a three-column table is one GitHub renders as two tables, with every
config row shown. The base read it with no refusal. The walker reads the
rows and refuses with *"a row the walk never reaches — it and every row
below it would go unread"*. Per S2, every item that table does not hold
becomes a refusal:

- `fold-check`, `broad-gate` (where the row is absent), `evidence-check`'s
  two cutoff rows and `pact-check` exit 2;
- `seal mode` writes nothing;
- the mode gate stays silent where `Mode` is not in the table.

The refusal itself follows the walker's stated rule, which the pact tables
already pin (`test_s4_a_pact_holding_both_tables_reads_signer_and_refuses_the_old_one`).
The defect is the remedy. All three documents tell the person to *"move it
into the table"*, which is wrong for a table of something else. The edit
that clears it is a heading between the two tables, because the walk stops
at a heading. That remedy appears nowhere. A line indented four columns
after the table, which GitHub shows as code, is refused the same way.

I measured the walker-level alternative too: stop at another table's header
without refusing. It breaks the pinned pact case above and
the "a row four columns in" case of
`test_every_way_the_table_ends_is_read_or_refused`.
That makes it a decision about all four tables, not a repair, so the
paste-ready fix below is the remedy line.

### 🟡 4 — The walker still reads a row GitHub does not show (the open item's class)

`hooks/config.py#config_table`, where it reads `gfm_table`'s pieces
(`hooks/config.py:1293`, `text.splitlines()`). Executed against cmark-gfm
2025.10.22.

The smith's open item holds for its own shape. Measured on that shape,
cmark-gfm shows `Mode shared` and a `-->` row. The walker refuses at the
header and names an HTML block GitHub does not see. The direction is a
refusal, and the cause is named wrongly.

The class is wider than the item names (contract §12). Take a row followed
on the same line by a form feed or U+2028 and a second row:
`| Mode | shared |`, the break character, then `| Broad gate | x |`.
cmark-gfm renders one row, `Mode shared`. The walker reads two, and
`Broad gate` is `x`, so `broad-gate` would run a command GitHub does not
show.

The base's `config_rows` read the same two rows, so this is not a
regression. It does contradict S1 ("the rows equal cmark-gfm's cells or the
walk refuses"). It also contradicts the overview's *"a gate is never handed
a row GitHub does not show"*. And the Not verified row describes the class
by its one harmless member.

The fix is narrow, and I executed it. A row piece that does not begin a
GFM line is the tail of the row above it. GitHub folds it into that row's
cut-off cells. So the walk stops there and refuses it, and the row above
keeps its value, as GitHub shows it. With the guard applied, the five
config and pact modules (3793 selected cases) passed, the FF and U+2028
shapes read `Mode shared` only, and `Broad gate` is refused. The other
answer is grounds: widen the overview's Not verified row to name this
member, and leave the fix to the owner with the walker's line ending.

### 🟡 5 — Prose that states a structure the tree no longer has

The class is "three walks of the table", which this work removed. It was
rewritten in `docs/the-broad-gate.md` and in `unfenced`'s docstring. It
stands in three other places. Read.

- `templates/config.md:314`: *"all three walks of this table read through
  it — the gates' reader, the mode gate's reader, and `seal mode`'s
  writer"*. There is one walk.
- `hooks/config.py:151`, in `fence_map`'s docstring: *"`unfenced` below is
  the generator form all three walks read the file through"*. This diff
  edited the same docstring and kept the sentence.
- `skills/verify/scripts/broad_gate.py:1026`, in `fenced_row`: *"invisible
  to all three walks of that table"*.

A fourth sentence is new in this diff and false at the base too.
`skills/verify/scripts/broad_gate.py:1108`, in `missing_row`'s docstring,
says a `Broad gate` line written last in its table is *"the shape this
repository's own config has"*. In `seal/config.md` the `Broad gate` row is
the second of seven. In `templates/config.md` it is the fourth of seven.

### ⬜ 6 — survivors.md grounds a row on the same false claim

`seal/specs/1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker/survivors.md`,
the row quoting *"seal/config.md in this repository ends with the Broad gate
row"*. Read. Its grounds say *"Still true of this repository's config and
the template's table"*. Neither table ends with that row. The quote lives in
a test's docstring and the case's assertions do not depend on it, so the
row's verdict to keep the text can stand. Its grounds should say "history,
false of both tables". This is a correction to the run's paperwork and is
not counted in `Needs a fix`.

## What the orchestrator asked about, answered

- **This repository's `seal/config.md`, the template's table and
  `NEW_CONFIG` are read whole by the plugin's walker, with nothing
  refused.** Executed: 7, 7 and 1 rows, refusals `[]`. The vendored twin
  is the exception (🔴 1).
- **No hook asks or denies on a refusal.** Read: `hooks/mode-gate.py:163`
  answers `refused` with silence. `hooks/evidence-advisor.py:228` reads only
  whether the freeze is on. No hook calls `pact_declaration`. Executed: the
  hook cases over shapes 1, 5 and 7 in
  `tests/test_the_mode_question_is_asked_once.py` passed in the module run
  below. The prompt budget is zero.
- **The overview's divergences.** Each one has grounds the tree supports
  (read):
  - The removals moved to phase 3 with their last caller.
  - `refused_row` had one caller, a test, at 321e9de1, and the reader
    registry routes an unnamed removal to `overview.md`, which is where it
    went.
  - S5 states the two writer re-pins in words.
  - cmark-gfm renders a row indented one to three spaces.
  - Shape 5 is refused by both readers at different lines, which is the
    stated direction.
  - The unit is `undeclared` at `hooks/mode-gate.py:128`.
  - The bootstrap warning was rewritten in place.
  - The `VENDORED_ATX_HEADING` exemption is held equal by
    `test_the_vendored_table_grammar_is_the_walkers`.
- **`survivors.md`.** Every released-row entry names a `Corrected ·` or
  `Re-read · Corrected ·` row, and each named row exists in the fragment
  (read, all 23 released-file rows). The "phrase-only" grounds I opened
  hold. One "still true" ground is false (⬜ 6).
- **The owner's in-place rule.** Every edited markdown document rewrites in
  place and narrates nothing: `templates/config.md` head and its pipe row,
  `skills/config/SKILL.md`'s bullet, `skills/implement/orchestration.md`'s
  warning, and `docs/the-broad-gate.md`. Four code docstrings and comments
  do narrate the change, so whether the rule reaches code is a question
  for the owner (❓ below).

## Regression tests to plant

- `tests/test_evidence_check.py`: `CONFIG_SHAPES` gains the config
  `seal mode` writes, a closed comment above the header with a blank line
  between. It is red at c5dde1f7, where the twin refuses it. Also add a
  pattern-equality line holding the twin's HTML kinds to
  `hooks/config.py#HTML_KINDS`. Both are in the 🔴 1 fix.
- `tests/test_the_mode_question_is_asked_once.py`: `write_row` over a file
  with no table and an `&lt;!--` that never closes prints the walker's
  sentence and never "a defect in this command". The current tree is red.
- `tests/test_the_mode_question_is_asked_once.py`: a row followed on its
  line by FF, then a second row, reads the first row only and refuses the
  second. It is red at c5dde1f7 for each of the eight characters in
  `tests/block_shapes.py#BREAKS`.
- The S8 document case in
  `tests/test_the_pull_request_language_is_the_repositorys.py` gains the
  phrase *put a heading between the two*, read in all three documents.

## Facts for the evidence ledger

- The vendored `evidence_check.py` at c5dde1f7 refuses a `seal/config.md`
  holding `NEW_CONFIG`'s closed comment above the header, and the base's
  copy reads it. Executed over a scratch repository: exit 2 against exit 0.
- cmark-gfm 2025.10.22 renders one body row, `Mode shared`, for
  `| Mode | shared |`, FF or U+2028, then `| Broad gate | x |`, all on one
  line. The walker reads two rows from it. Executed.
- cmark-gfm 2025.10.22 renders the Item/Value table, a blank line, prose
  and a three-column table as two tables. The walker refuses the second
  one's header as a row the walk never reaches. Executed.

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

## Paste-ready fixes

### 🔴 1 — `skills/evidence-check/scripts/evidence_check.py`

Replace the `VENDORED_BLOCK_OPENER` comment and definition (lines 4299–4302) · NAME NOT IN TREE
with:

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

and the first line of the check in `vendored_config_rows` (line 4382) with:

```python
    opener = vendored_block_left_open(lines[:at])
```

The refusal sentence under it can stay as it is. Its remedy "take that line
out of this file" is still wrong for a block that is merely left open, so
"close the block, or take that line out of this file" is the truer ending.
`tests/test_a_format_has_one_reader.py` may ask for an exemption for the
HTML patterns, as it already has one for `VENDORED_ATX_HEADING`.

In `tests/test_evidence_check.py`, add to `CONFIG_SHAPES`:

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

and to `test_the_vendored_table_grammar_is_the_walkers`:

```python
    assert [
        (s.pattern, s.flags, e.pattern, e.flags) for s, e in ec.VENDORED_RAW_HTML
    ] == [(s.pattern, s.flags, e.pattern, e.flags) for s, e in config.HTML_KINDS[:5]]
```

### 🟡 2 — `skills/implement/scripts/seal.py#write_row`

Insert after the unclosed-fence branch, before the generic `return` at
line 1590:

```python
        walked = config_table(new)[1]
        if walked:
            return (
                f"{path}, with the `{ROW_ITEM}` row written into it, "
                f"{walked[0]}. Nothing was written and your file is exactly "
                "as it was"
            )
```

### 🟡 3 — the remedy line, rewritten in place in the three documents

`templates/config.md:62–63`:

```markdown
- a row under a comment, a fence or a blank line that ends the table: move
  it into the table; where it heads a table of something else, put a
  heading between the two tables.
```

`skills/config/SKILL.md:119–120`:

```markdown
  - a row stranded after a comment, a fence or an empty line: move it into
    the table; if it belongs to another table, put a heading between the two.
```

`hooks/config.py:384–385`, in `config_rows`' docstring:

```python
      - a row under a comment, a fence or a blank line that ends the table:
        move it into the table; where it heads another table, put a
        heading between the two.
```

### 🟡 4 — `hooks/config.py#config_table`

Replace the function's last line with the guard, and define the constant
below the function. Executed with the sentence worded differently. This
wording ends its quoted line on *which is not*, so
`skills/verify/scripts/broad_gate.py#stopping_line` finds it:

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

### 🟡 5 — the three sentences, rewritten in place

`templates/config.md:314–317`:

```markdown
line somebody wrote as a row. One rule says so and the one walk of this
table reads through it — the gates, the mode gate, and `seal mode`'s writer
all read the rows it names — so the reader and the writer can never
disagree about which row is the row.
```

`hooks/config.py:151`, in `fence_map`'s docstring:

```python
    `unfenced` below is the generator form the one walk of every table reads
    the file through, and this is the same walk with the state it ENDS in kept. A fence
```

`skills/verify/scripts/broad_gate.py:1026`, in `fenced_row`'s docstring:

```python
    only one that may ask it.** `hooks/config.py#unfenced` makes a fenced line
    invisible to the one walk of that table, which is what stops an example
```

`skills/verify/scripts/broad_gate.py:1107–1108`, in `missing_row`'s
docstring:

```python
        line written `| … |` stands below it. A `Broad gate` line written
        LAST in its table — the shape a stub `seal mode` wrote can take —
```

Needs a fix: yes — 🔴 1 (the vendored twin refuses every plugin-written
config), 🟡 2 (`seal mode` names the wrong cause), 🟡 3 (the remedy for a
second table), 🟡 4 (a row GitHub does not show is still read), 🟡 5 (prose
naming a structure that is gone)
Loses a record or crashes: no

## Proof block

```
📋 code-review applied (warden, round 1)
· target:   c5dde1f7, a --no-local clone, merge-base 321e9de1
· read:     seal/specs/1791852616-…/ spec.md, plan.md, questions.md,
            overview.md, survivors.md, changelog.md; the ledger fragment's
            claim column; the diff of hooks/config.py,
            skills/implement/scripts/seal.py, skills/verify/scripts/broad_gate.py,
            skills/evidence-check/scripts/evidence_check.py,
            skills/evidence-check/scripts/correction_check.py,
            skills/settle/scripts/fold_check.py, templates/config.md,
            skills/config/SKILL.md, skills/implement/orchestration.md,
            docs/the-broad-gate.md, tests/config_shapes.py,
            tests/test_evidence_check.py (the twin's cases),
            tests/test_a_format_has_one_reader.py, tests/undeclared_readers.txt,
            tests/test_every_reader_ends_a_line_where_gfm_does.py,
            tests/test_one_table_walker_reads_what_gfm_renders.py;
            hooks/config.py gfm_table and its helpers; hooks/mode-gate.py
            undeclared; hooks/evidence-advisor.py around the freeze;
            seal/config.md; docs/the-reader-registry.md (a frame names what
            its work removes); the pact readers in chain_check.py,
            evidence_check.py and pact_check.py
· executed: the modules and probes in the table above, exit codes read
            directly; every probe edit in the clone was reverted, and the
            clone is clean at c5dde1f7
· unverified: the full suite, lint and typecheck — the sealer's; the
            phases' red-first claims (§15) were read, not re-run
```
