# Review round 1: 1795405728-lib-routing-splits-a-row-on-an-escaped-pipe

```seal
target: c47db7a144565c35c63fec401a09e2f59fba093c against origin/release/v0.38.6
```

The diff was read against the merge base `da7bd3968`, where the branch was
cut. `origin/release/v0.38.6` has moved to `c3f568c6a` since (#1582), and
`git diff --stat` over the range names no file #1582 changed. The work
item's `routing.md`, `frame/design.md`, `frame/plan.md`,
`frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md` were read whole
at the target. `Commit and pull request language` is English, so no
`pr.<lang>.md` stands. The three phase records were read whole. No earlier
round exists, so nothing is carried from one.

Carried from the phase records, not re-run: the red runs of S1, S2's
`gfm_table` half, S3 and S5, the three `seal mutate` tables, and the phase
boundary runs. The searches of S6, S7's comparison, the touched modules'
cases and the claims below were run again.

## Findings

### 1. Three readers now refuse or skip a row they read before, and no account of the change names it

```seal
severity: should
location: `seal/threads/1795405728-lib-routing-splits-a-row-on-an-escaped-pipe/frame/design.md:73`, `seal/threads/1795405728-lib-routing-splits-a-row-on-an-escaped-pipe/frame/plan.md:52`, `seal/threads/1795405728-lib-routing-splits-a-row-on-an-escaped-pipe/changelog.md:10`
evidence: executed `uv run --no-project --with cmarkgfm==2025.10.22 --with pytest python -m pytest -q -s -p no:cacheprovider test_tmp_round1.py` in the round's scratch directory; read `lib/tables.py:305`, `lib/tables.py:323`, `lib/gaps.py:140-143`, `skills/settle/scripts/fold_check.py:156-163`, `lib/routing.py:161-166`
```

Why it matters: the shape is a row that holds a pipe after an even run of
backslashes, such as `| a\\|b | the orchestrator |`. `table_cells` returns
None for it (`lib/tables.py:323`, `EVEN_ESCAPED_PIPE` at `:305`). The
readers that moved onto `table_cells` read it before:

- The probe ran `lib/gaps.py#check_text` at the base and at the target
  over a closing memo holding that row. At the base the row read as the
  open item `a\|b`, because `split_row` kept it as one cell. At the target
  the memo answers `(7, 'a line inside the table that is not a table row')`.
  So `seal unverified` and `settle --apply` refuse a memo they accepted.
  cmark-gfm renders the row as `a|b` and `the orchestrator` (the probe's
  `rows_under` line).
- `fold_check.py#index_rows` sets `in_table` false on the None, so the row
  is dropped, and the row under it is taken for a header and dropped too
  (`skills/settle/scripts/fold_check.py:156-163`, read).
  `index_problems` then reports a document named on neither row as having
  no row.
- `lib/routing.py#table_rows` read the old split's first two cells, so the
  `Branch` value was `a\\`. It now skips the row (`lib/routing.py:164-166`,
  read), and the declaration has no `Branch` row at all.

`frame/design.md` G8 states that `table_cells` returns None on this shape,
and *Scope* item 1 keeps it so. The frame chose the refusal, so the code
holds to the frame. The account of what changes does not carry that
choice. `frame/design.md:73` says `table_rows` "differs on the shapes S1
to S3 name and on two no committed declaration holds", and this shape is
a third. `frame/plan.md:52` lists what the readers now do and leaves it
out. `changelog.md`'s `### Changed` names the indented row alone. The
plan's second *Alternatives considered* row rejects a design because
"`lib/gaps.py` refuses a row GitHub shows". This is the same failure, on a
rarer shape. G9 says no committed record holds the shape, so nothing
reads differently today. The release notes still ship a behaviour change
they do not name. Finding 2 takes up the direction row these sentences
feed.

The fix reaches the three statements. The `changelog.md` bullet is the one
a person reads in the release notes:

```markdown
- **A row indented four spaces or a tab is no table row in any reader**, as cmark-gfm renders it as code. The routing reader, `lib/gaps.py` and `seal fold`'s index reader read such a row before. No committed record holds one, and every committed `routing.md` reads the same before and after.
- **A row holding a pipe after an even run of backslashes is refused by `lib/gaps.py` and skipped by the routing reader and `seal fold`'s index reader**, which read it before. `lib/tables.py#table_cells` refuses the shape, because cmark-gfm splits it otherwise. No committed record holds one.
```

In `frame/design.md:73`, "and on two no committed declaration holds: a row
indented four spaces or a tab is not read, and a row whose first cell is
empty is read with the label `''`, where the old separator test skipped
it" becomes:

```markdown
and on three no committed declaration holds: a row indented four spaces or a tab is not read, a row holding a pipe after an even run of backslashes is not read, and a row whose first cell is empty is read with the label `''`, where the old separator test skipped it.
```

In `frame/plan.md:52`, after "is no longer a row there, as cmark-gfm reads
it.":

```markdown
A row holding a pipe after an even run of backslashes, which those two readers and `lib/routing.py` read before, is no longer a row in any of them: `table_cells` refuses it (`frame/design.md` G8), so `lib/gaps.py` names it as a line that is not a table row, and the other two skip it.
```

```seal
verdict: fixed 9a06f602f
answer: The finding holds. The orchestrator took the round's three texts as given: the changelog's *Changed* section gains the even-run bullet, `frame/design.md` *Data & interfaces* names three shapes no committed declaration holds, and `frame/plan.md` *Operational impact* says how each reader now treats that row. The fix touches the work item's records alone, so the sealer reads it.
```

### 2. The row on what the gate change carries states no block-more or allow-more direction, and its one claim of direction is false for one shape

```seal
severity: should
location: `seal/threads/1795405728-lib-routing-splits-a-row-on-an-escaped-pipe/frame/plan.md:59`, `seal/threads/1795405728-lib-routing-splits-a-row-on-an-escaped-pipe/pr.md:2`
evidence: read `CONTRIBUTING.md:383-389`, `CONTRIBUTING.md:410-418`, `skills/core/SKILL.md:48-56`, `lib/gaps.py:140-143`, `skills/settle/scripts/fold_check.py:156-163`, `lib/tables.py:569-572`; executed `test_tmp_round1.py` (finding 1)
```

Why it matters: `pr.md:2` quotes the row into the pull request body. The
sealer also reads it as the pull request's answer to `CONTRIBUTING.md`
*What a change to a gate must carry*. That section asks "whether the
change makes the gate block more or allow more, and why that direction is
the cheaper mistake here" (`CONTRIBUTING.md:383-389`). The row answers
"its failure direction is toward what the renderer shows". That says what
the new reading matches, not whether each gate now blocks or allows more.
By the code, the gates move in both directions:

- `seal pact` and the settle's reading of *Judgments of the run* read a row
  without its closing pipe that `gfm_table` refused. They allow more
  (`lib/tables.py:569-572`, read).
- `seal unverified` and `settle --apply` refuse an indented row and an
  even-run row that `lib/gaps.py` read (`lib/gaps.py:140-143`). They block
  more.
- `seal fold` drops those rows from the index and reports a document named
  on no row (`fold_check.py:156-163`). It blocks more.
- `chain-check` no longer reads those rows of a `routing.md`. A required
  row so written leaves no declaration, which blocks more. An optional row
  such as `Planning` reads as unanswered, which allows more.

The row's grounds also say "Each change makes a gate read what a person
sees rendered". Finding 1's probe shows otherwise for the even-run shape.
cmark-gfm renders that row, and `lib/gaps.py` now refuses it. The grounds
cite `skills/core/SKILL.md` as naming this "the cheaper error to keep".
That passage names a script answering "these differ" where the meaning is
the same as the worst result (`skills/core/SKILL.md:48-56`). It ranks no
direction. The section's *What it reads* item (`CONTRIBUTING.md:410-418`)
asks for "the form the gate reads, what the gate names as a line it did
not read". The row does not answer it. `gfm_table` and `lib/gaps.py` name
each such line. `fold_check.py` and the routing reader name none.

The fix rewrites the row's Judgment and Grounds cells. `pr.md:2` quotes
the Judgment cell word for word, so it changes in the same commit:

```markdown
| 2026-11-23 | What this change to the gates carries: it allows more in `seal pact` and the settle's judgments reading, blocks more in `seal unverified`, `settle --apply` and `seal fold`, moves both ways in `chain-check`, and its prompt budget is zero | `seal pact` and the settle's reading of *Judgments of the run* now read a row without its closing pipe, which `gfm_table` refused, so they allow more. `seal unverified` and `settle --apply` (`lib/gaps.py`) now refuse a row indented four spaces or a tab and a row holding a pipe after an even run of backslashes, and `seal fold`'s index reader skips both, so they block more. `chain-check` reads neither in a `routing.md`: a required row so written leaves no declaration, and an optional one reads as unanswered. The indented row is code to cmark-gfm, so each deny on it stops a row nobody sees as a row. The even-run row is a wrong deny, which the run pays only on a row nobody writes: no committed record holds either shape (`frame/design.md` G9), and a deny is the cheaper mistake beside a gate reading a value GitHub does not show. What each reads is a GFM table row through `lib/tables.py#table_cells`; `gfm_table` and `lib/gaps.py` name each line they do not read, and `fold_check.py#index_rows` and `lib/routing.py#table_rows` name none. `seal pact` counts a line where GFM ends it. No step asks a person anything, no platform is left unrun but the Windows leg CI answers, and the change removes two splitters and the bridge between two line splits, adding no mechanism | `CONTRIBUTING.md` *What a change to a gate must carry* |
```

```markdown
- "What this change to the gates carries: it allows more in `seal pact` and the settle's judgments reading, blocks more in `seal unverified`, `settle --apply` and `seal fold`, moves both ways in `chain-check`, and its prompt budget is zero" (`frame/plan.md` *Judgments of the run*, the row on what a gate change carries)
```

```seal
verdict: fixed 9a06f602f
answer: The finding holds. The orchestrator replaced the row on what the gate change carries with the round's row, which names each gate's direction and answers *What it reads*, and `pr.md`'s quote with the round's line. The fix touches the work item's records alone, so the sealer reads it.
```

### 3. The release note and S5's case say the old fence rule hid every word after the run, and it hid them only up to the next backtick line

```seal
severity: should
location: `seal/threads/1795405728-lib-routing-splits-a-row-on-an-escaped-pipe/changelog.md:6`, `tests/skills/test_passages.py:141-144`
evidence: executed `test_tmp_round1.py` in the round's scratch directory (the base's `passages.py#words`); read `skills/settle/scripts/passages.py` at `da7bd3968`, its `words` at `:73-97`
```

Why it matters: `changelog.md:6` says the old rule meant "a backtick run
four spaces in at the top level of a rule document hid every word after it
from the check". The base's `words` ends a fence at the next line of a
backtick run of the same character with nothing after it (read,
`passages.py:73-97` at `da7bd3968`). The probe gave it `Intro.`, a run four
spaces in, `alpha beta`, a fenced `sh` block holding `code here`, and
`gamma delta`. It returned `['intro.', 'gamma', 'delta']`. So the words
after the four-space run were hidden only up to the next closing line,
and `gamma delta` below it was read. The release note tells a person the
check went blind for the rest of the document, which overstates the old
defect. The S5 case's docstring makes the same claim in history form
("took the run at any indentation and dropped everything after it",
`tests/skills/test_passages.py:143-144`). Phase 3 left that sentence for a
round to weigh. Its words are false beyond the case's own text, and
`skills/core/SKILL.md` *The rule a mechanism is kept against* sends history
to git and the release notes. So the fix drops the sentence rather than
correct it.

```markdown
- **The paste check and `chain-check`'s copy notice read fences as every other reader does.** `skills/settle/scripts/passages.py` opened a fence on three backticks at any indentation. So a backtick run four spaces in at the top level of a rule document hid the words after it from the check, up to the next line of backticks. It now takes its lines and fences from `lib/lines.py#readable`, where a fence opens three spaces in at most. One rule document reads differently: `docs/releasing/release-checklist.md`, whose backtick lines six spaces in under a list item are an indented code block, not a fence. Their words are now compared, and no other rule document shares a run of them.
```

```python
    def test_reads_the_words_after_a_backtick_run_four_spaces_in(self):
        """#1574: four spaces in, three backticks open no fence (CommonMark
        4.5), so the prose below them is read, as `lib/lines.py#readable`
        reads it."""
```

```seal
verdict: fixed b6425753e
answer: The finding holds. The base's `words` closes a backtick fence at the next line that holds nothing but a run of at least as many backticks (read, `passages.py:81-88` at `da7bd3968`), and a probe of the base over five shapes gave the same, with a closer that carries an info string such as `sh` leaving the fence open (executed, `test_tmp_close.py` in the pass's scratch directory). The case's docstring takes the round's text as given. The changelog bullet is in the pass's own words: the round's "up to the next line of backticks" would take in a line of backticks followed by `sh`, which closes nothing, so the bullet reads "up to the next line that holds nothing but a run of at least as many backticks". `cb69dac5b`'s commit subject states the old claim as well, and it stands in the history, since the branch is never rebased.
```

### 4. The plan says `CELL` stays as it is, and the design counts its new alternative as the fourth

```seal
severity: should
location: `seal/threads/1795405728-lib-routing-splits-a-row-on-an-escaped-pipe/frame/plan.md:7`, `seal/threads/1795405728-lib-routing-splits-a-row-on-an-escaped-pipe/frame/design.md:28`
evidence: read `lib/tables.py:49-63`, `lib/tables.py:299`, `seal/threads/1795405728-lib-routing-splits-a-row-on-an-escaped-pipe/trail/phases/phase-1.md:13-31`
```

Why it matters: `frame/plan.md:7` says "Scope item 1 widens `TABLE_ROW`'s
grammar to the open end and leaves `CELL`, `unescaped` and
`EVEN_ESCAPED_PIPE` as they are". That sentence says what the work does,
so it is read against the target. At the target, `CELL` has gained an
alternative, a backslash that ends the line (`lib/tables.py:63`).
`TABLE_ROW` now matches a row's start alone (`:299`), and is not widened.
Phase 1 recorded both departures (`trail/phases/phase-1.md:13-31`). The fold
at `179c682bc` carried the backslash into `frame/design.md` *Scope* item 1
and left this sentence standing. The folded sentence calls the backslash
"`CELL`'s fourth alternative" (`frame/design.md:28`). `CELL` is
`(?:[^|\\]|\\.|\\\Z)`, three alternatives, and the comment over it lists
three (`lib/tables.py:49-52`). The settle and the sealer read the frame
for what the change did to the grammar, and both sentences misstate it.

```markdown
Scope item 1 reads the open end: `TABLE_ROW` matches a row's start alone, at most three spaces and a pipe, `CELL` gains a third alternative, a backslash that ends the line, and `unescaped` and `EVEN_ESCAPED_PIPE` stay as they are.
```

In `frame/design.md:28`, "(`CELL`'s fourth alternative)" becomes
"(`CELL`'s third alternative)".

```seal
verdict: fixed 9a06f602f
answer: The finding holds. The orchestrator took the round's sentence for `frame/plan.md` *Technical context* as given, and `frame/design.md` *Scope* item 1 names `CELL`'s third alternative. The fix touches the work item's records alone, so the sealer reads it.
```

## Confirmations

What matched: S6's seven searches print nothing at the target, each with
the pathspec `frame/design.md:58-64` gives (executed, each exit 1). Search
6 prints `lib/lines.py:93` and `lib/routing.py:147` at `da7bd3968`
(executed, exit 0), so it can fail.

What matched: S7 holds at the target. Phase 2 ran no S7 probe (`gaps.md`
*Not done*, read). This round ran `routing.parse` and
`routing.table_rows` under the base's `lib/` and the target's over the 40
files `git ls-files 'seal/threads/*/routing.md'` lists. It printed
`40 files; 0 differ` (executed, `test_tmp_s7.py`).

What matched: G9's census holds at the target. None of the 799 tracked
`.md` files holds any of the eight characters `str.splitlines` ends a line
at and GFM does not (executed). No file of this work item holds one
either, so the escape `71d7587cf` wrote for phase 2's U+2028 left no
literal one behind (executed).

What matched: the touched modules pass at the target. `bin/test -q` over
`tests/lib/test_tables.py`, `test_routing.py`, `test_gaps.py`,
`test_lines.py`, `test_blocks.py`, `tests/skills/test_passages.py`,
`test_pact_check.py`, `test_fold_check.py`, `tests/test_commonmark_oracle.py`
and `tests/test_censuses.py` gave 1345 passed (executed, in a clone at the
target). The suite as a whole stays `unverified`, and the orchestrator
answers it.

What matched: G12 holds at the target. `ast.parse(..., feature_version=(3, 9))`
parses `lib/tables.py`, `lib/blocks.py`, `lib/routing.py`, `lib/lines.py`,
`lib/gaps.py`, `passages.py` and `fold_check.py` (executed).

What matched: the call sites the frame moves were enumerated from what
produces the defect. `git grep` found every call to `walk`, `fence_only`,
`unfenced`, `hidden_lines`, `fence_map`, `opens_table` and `gfm_table`
outside `tests/` (executed). Each one's lines come from `gfm_lines`
(read: `lib/fields.py:337-338`,
`skills/settle/scripts/rules.py:153-156`,
`skills/settle/scripts/rule_changes.py:435`,
`skills/settle/scripts/settle.py:1234`,
`skills/verify/scripts/session_cost.py:3287-3289`). The tree still holds
three cell splits written outside `table_cells`, and each reads something
else: `evals/scripts/noninferiority.py:748` (out of scope by the design),
and the delimiter-row counts at `lib/tables.py:426` and `:531` (executed,
`git grep` on `split("|")`, `strip("|")` and `startswith("|")` over
non-test Python).

What matched: `pr.md`'s two quotes stand word for word in the Judgment
cells of `frame/plan.md:58` and `:59` (read). Finding 2's fix changes the
second quote with its cell.

What matched: phase 1's claim that `seal mutate` "shows each red with its
guard removed" for the three cases that passed at base is wrong for the
`a third cell` shape. The mutant its table names for that shape removed
the `DELIMITER_ROW` skip, which is not that shape's guard
(`trail/phases/phase-1.md:91-109`, read). This round made `table_rows` read
rows of exactly two cells. The shape went red, and `an escaped pipe` and
`no closing pipe` stayed green (executed, `test_tmp_third_cell.py`). So
the case pins its own guard, and no finding is opened. The phase record
names the wrong mutant for it.

What matched: phase 3's second item, the paste check now comparing words
a renderer shows inside an indented code block. *Scope* item 7 asks for
`lib/lines.py#readable`. `readable` does not model an indented code block,
and `live_lines`' docstring says so. Every reader through `lib/lines.py`
already reads such a block the same way. The one rule document it changes
gains 21 windows that no other corpus file holds (`trail/phases/phase-3.md:39-62`,
carried). No finding is opened.

What matched: `gaps.md` *Not done* places `docs/releasing/release-checklist.md:358-366`
as an indented code block under the list item at `:352`. Its lines stand
six spaces in, past the item's content column of two (read). The issue
does not ask for that paragraph to be re-indented.

The re-pinned docstrings in `tests/lib/test_tables.py` and
`tests/test_commonmark_oracle.py` state their old readings with "until
#1574". That is the form the repository's case docstrings already use for
an issue's history. Each states the old reading correctly, so this round
opens no finding on them.

New tests were read against their groups. `seal layout --pairs` names no
pair that holds a case this diff adds (executed). `Test_table_cells`
carries `split_row`'s four shapes and adds three more. `a backslash last`
pins `CELL`'s third alternative, `blanks after the closing pipe` pins the
dropped blank last piece, and `a pipe alone` pins `tuple(cells) or None`.
Each new routing shape holds a fact *Scope* item 2 or S1 to S3 states.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate, the full suite, lint and format check, over the target | `seal/config.json`, `Broad gate` | the orchestrator, at the broad run after the rounds settle |
| The Windows leg of CI over the readers' changes | `frame/plan.md:59` | CI, read by the orchestrator |
| The textual conflict with #1573 in `tests/lib/test_routing.py`'s copy case, whose siblings list both change | `frame/plan.md:45` | the orchestrator, when the later work item merges the base |

## Probes

| Command | Result |
|---|---|
| `uv run --no-project --with cmarkgfm==2025.10.22 --with pytest python -m pytest -q -s -p no:cacheprovider test_tmp_round1.py` | The row's first cell is `a`, two backslashes, a pipe and `b`, and its second is `the orchestrator`. cmark-gfm renders the first cell as `a`, a pipe and `b`. At base `split_row` read it, and `check_text` read it as an open item. At target `table_cells` is None, and `check_text` refuses line 7 as "a line inside the table that is not a table row". The base's `passages.py#words` returned `intro.`, `gamma`, `delta`, so it dropped the words after the four-space run only up to the next closing line. The target's returned all five words |
| `uv run --no-project --with pytest python -m pytest -q -s -p no:cacheprovider test_tmp_s7.py` | `40 files; 0 differ`: `parse` and `table_rows` agree under the base's `lib/` and the target's on every committed `routing.md` |
| `uv run --no-project --with pytest python -m pytest -q -s -p no:cacheprovider test_tmp_third_cell.py` | With `table_rows` reading rows of exactly two cells, `a third cell` went red, and `an escaped pipe` and `no closing pipe` stayed green |
| `bin/test -q` over the ten modules under *Confirmations*, in a clone at the target | 1345 passed |
