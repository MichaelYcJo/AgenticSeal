# Feature Specification: the config table is read by the walker cmark-gfm holds (#871)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against — verification that runs unattended* | between a refusal a command prints with its remedy and a question put to a person, the refusal is chosen; nothing in this work asks anybody anything |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | every phase that changes what a gate or a hook answers states its direction and its prompt budget (zero throughout), plants its case red first, and puts a `Reads:` line on every unit it touches |
| `docs/the-reader-registry.md` §*The four classes and the line that declares one* | the config reader declares `guess` — a person's table, read as cmark-gfm renders it, unknown refused — and every unit this work changes leaves `tests/undeclared_readers.txt` by declaring |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | `## Removes` below names each reader, rule and pin this work takes out, once, before the build |
| `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment* | the released rows whose claim the stop rule's removal moves are re-read or corrected in `seal/ledger/1791852616-….md`, never re-stamped (`Ledger frozen from 1790993141`) |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file* | the changelog entry, the ledger rows and the re-reads go to this work item's fragments |
| `docs/the-broad-gate.md` §*What the gate runs, and how the list is kept true* (the refusal of a configured command, lines 73–81) | the sealer's answer to a config it cannot read stays a refusal at exit 2 with nothing run, naming the line and the edit |
| `templates/config.md`, head (*One reader answers every row of this file, `hooks/config.py`*) and §*Broad gate* (the `\|` row) | the one-reader rule this work completes, and the two sentences this work rewrites: the escape stays, the stop rule goes |

## Scope

**In.** `hooks/config.py#config_rows` and its walk `indexed_config_rows`,
its third walk `refusal`, and the writer's walk `seal.py#table_span` are
replaced by one reading of the `| Item | Value |` table through
`hooks/config.py#gfm_table`, the walker `tests/gfm_table_oracle.py` holds to
cmark-gfm. Every caller of the config table reads the walker's answer — rows
it is certain of, or a refusal naming the line and the edit — through the
functions `hooks/config.py` already exports, with one new one for the pair.
That is:

- `hooks/config.py`: `config_rows`, `indexed_config_rows`, `config_value`,
  `value_of`, `declared_value`, `declared_mode`, `pact_declaration`,
  `pact_lines_not_read`, and the sentences a refusal is given in;
- the two hooks that read the file, `hooks/mode-gate.py` and
  `hooks/evidence-advisor.py`, which stay silent on a refusal and are pinned
  silent over the shapes below;
- the writer, `skills/implement/scripts/seal.py#with_row` and `write_row`;
- the commands, `skills/verify/scripts/broad_gate.py` (`broad_command`,
  `missing_row` and the units it reads), `skills/settle/scripts/fold_check.py#config_rows`,
  `skills/evidence-check/scripts/correction_check.py#cutoff_at`,
  `skills/evidence-check/scripts/evidence_check.py#cutoff_row` with its
  vendored twin `vendored_config_rows`, and `pact_check.py` where it reads a
  signer's config through `declared_pacts`;
- the oracle case, which gains the config header as a fourth pass;
- the three documents that describe the stop rule: `templates/config.md`
  (head and §*Broad gate*), `skills/config/SKILL.md` §*Procedure* step 3's
  `\|` bullet, and `hooks/config.py`'s own docstrings;
- the record: the changelog fragment, the ledger fragment with the re-reads
  under the freeze, `tests/undeclared_readers.txt` shrinking by every unit
  touched.

**Out, with the ground for each.**

- `skills/evidence-check/scripts/pact_check.py#path_map`, which reads
  `~/.claude/specseal/pact-paths.md` — a machine-local `| Remote | Path |`
  map, not `seal/config.md` — with `config.CELL` and `config.CONFIG_SEPARATOR`.
  It is the sibling of this issue one file over, and it is why those two
  names stay exported after `CONFIG_ROW` and `CONFIG_HEADER` leave. · NAME NOT IN TREE
  `plan.md` §*Operational impact* carries the issue text.
- `hooks/routing.py#table_rows` and `skills/code-review/scripts/chain_check.py#table_rows`
  (#866's seam): other files, other failure directions, put out by #867's
  frame on the same grounds.
- `evidence_check.py#CONFIG_ROW_RE`, the line-shape judgment
  `notify_may_be_always` makes for itself: it is the checker's twin of
  `pact_lines_not_read`'s *was this line taken as a row*, and it reads no
  row's value. If the builder finds it reads one, that is a divergence row
  in `overview.md`, not a widening.
- A notice from a hook. The mode gate says nothing on a refusal today
  (#867) and keeps saying nothing; a line printed by a `PreToolUse` hook is
  a change to what a person sees that this work does not make.
  `questions.md` records it as decided.
- Rewriting an installed `seal/config.md` into the walker's shape. Decided
  against in `plan.md` §*Alternatives considered*; the migration is the
  refusal's remedy, one line, printed by the first command that reads the
  file.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 · one walk | Given any markdown text, when `config_rows`, `indexed_config_rows`, `config_value`, `declared_mode`, `pact_declaration`, `seal.py#with_row` and `broad_gate.py#broad_command` read the `\| Item \| Value \|` table, then every one of them reads it through `gfm_table` with the header `("Item", "Value")`, and on every shape of the oracle's enumerated corpus the rows equal cmark-gfm's cells or the walk refuses | `tests/test_one_table_walker_reads_what_gfm_renders.py` with `HEADERS["config"] = ("Item", "Value")` as a fourth pass, executed; a case asserting the four readers' rows are one walk's over the 16 shapes of §*Data & interfaces* |
| S2 · a refusal is per item, never an absent row | Given a table the walker refuses, when a caller asks `config_value(text, item)`, then an item whose row the walk READ before it stopped is `(value, None)`; an item it did not read is `(None, sentence)` where the sentence is the walker's, naming the stopping line and the edit; a doubled row is `(None, sentence)` as #867 left it; and `(None, None)` is only ever an unrefused table with no such row, or no table at all (a file of prose holds no table and declares nothing) | one case per arm in `tests/test_the_mode_question_is_asked_once.py`, over shapes 1, 5, 7 and 13 of §*Data & interfaces*; seen red against the stop rule |
| S3 · hooks say nothing | Given a `seal/config.md` whose table the walker refuses, when the mode gate runs on a Bash call and the evidence advisor after a commit, then neither denies and neither asks; the mode gate asks only where the table is read and holds no `Mode` row, exactly as today | `tests/test_the_mode_question_is_asked_once.py` hook cases over shapes 1, 5 and 7: `allow` on the first call, `allow` on the second; the advisor's existing refusal case |
| S4 · commands refuse at exit 2, naming the line and the edit | Given the same file, when `broad-gate`, `seal mode`, `seal mode --check`, `evidence-check --reverify`, `correction-check`, `fold-check` or `pact-check` reads a row the walk did not read, then it prints the walker's sentence after its own prefix and exits 2 with nothing run, written, judged or checked | one case per command, each asserting the exit code read directly and the sentence; `broad-gate`'s asserting no worktree was added and no command ran |
| S5 · the writer and the reader agree | Given a config whose `Mode` row sits anywhere the walk reads it, when `seal mode` writes, then it overwrites that line and no other, keeps every other byte, and inserts a new row at the table's end through the walk's own line numbers; given a table the walker refuses, it writes nothing and prints the sentence; the read-back guard of `write_row` stays | `test_the_writer_and_the_reader_agree_about_which_row_is_the_row` kept and extended with a refused shape; a case for `seal mode` on shape 7 asserting the file's bytes are unchanged |
| S6 · the sealer's refusal is one sentence, with #430's condition kept | Given a `Broad gate` row the walk did not read, when `broad-gate` refuses, then the sentence quotes the stopping line as written, names the edit, adds *write it `\|`* where that line's first cell is `Broad gate` and holds a bare pipe, and says rows below it go unread only where a line is written below it; a `\| Broad gate \|` line that exists only inside a fence or a closed comment is still named as fenced or commented, never absent; a file with no such line still gets the absent-row refusal unchanged | the sealer's refusal cases re-pinned to the new sentences; `test_a_broad_gate_line_only_inside_a_fence_is_named_and_not_called_absent`, `test_the_absent_row_refusal_still_reaches_a_file_with_no_such_line` and `test_a_broad_gate_row_written_twice_is_refused_and_nothing_runs` unchanged and green |
| S7 · the vendored twin follows | Given the checker copy `evidence-ci` vendors, when it reads a config, then on every shape of `tests/test_evidence_check.py#CONFIG_SHAPES` — the table extended with the walker's refusal shapes — its rows and its refusal equal the plugin's; where it lacks block state the plugin has (a fence, a comment, an HTML block above the header), it may refuse what the plugin reads and never reads what the plugin refuses, and its docstring says so | `test_the_vendored_config_rule_agrees_with_the_shared_one` over the extended table; a case for the stated direction on a fenced shape |
| S8 · the documents say which shapes are refused and the edit for each | Given `templates/config.md`'s head and §*Broad gate*, `skills/config/SKILL.md`'s `\|` bullet and `hooks/config.py#config_rows`' docstring, when a person reads them, then each names the shapes of §*Data & interfaces* the walker refuses with the one-line edit, and none says the reader stops at a line and reads on, or that a `Mode` row below a bad line is invisible | `tests/test_the_pull_request_language_is_the_repositorys.py#test_the_skill_names_every_way_of_not_naming_one`'s pattern: a case reading the three documents for the phrases *leave a blank line above the header* and *write it `\|`*, and for the absence of *stops reading the table there* |
| S9 · the record | Given the build's end, when `evidence-check --strict .` and `tests/test_a_record_states_what_the_tree_has.py` run over this directory, then every `## Removes` row resolves gone, every touched unit carries a `Reads:` line and is off the census, and the released rows the stop rule's removal moves carry a `Re-read ·` or `Corrected ·` row in this work item's fragment | the two commands, exit codes read directly; the fragment's rows named in `overview.md` |

## Data & interfaces

**The reading, measured.** Executed 2026-10-13 under `cmarkgfm==2025.10.22`
(the suite's pin, `.github/scripts/run_tests.py#CMARKGFM_VERSION`), from a
probe that imported the renderer and the standard library alone, over the
shapes `config_rows` reads today and `gfm_table` would answer differently.
`HEAD` is `| Item | Value |` over `|---|---|`.

| # | Shape | cmark-gfm renders | `config_rows` today | the walker |
|---|---|---|---|---|
| 1 | `<!-- note -->` directly above the header | the table, `Mode` | `Mode` | refused: *header directly under `<!-- note -->` — leave a blank line above the header* |
| 2 | a line of prose directly above the header | the table, `Mode` | `Mode` | refused, the same sentence |
| 3 | the header with no delimiter row | no table | `Mode` — a row GitHub does not show | refused: *no delimiter row under it* |
| 4 | a line of prose between the delimiter and the first row | a row `("a paragraph", "")`, then the rows | the rows, the prose stepped past | refused: *a line with no pipe that GFM reads as one of its rows* |
| 5 | a comment line inside the table (`tests/block_shapes.py` C5, C7) | `Mode` only; the row below the comment is not in the table | both rows — one GitHub does not show | `Mode`; the row below refused: *a row the walk never reaches* |
| 6 | a three-cell row mid-table | `("a", "b")`, truncated, then the rows below | the rows above; every row below silently dropped | the rows above; refused at the line: *not a 2-cell row written `\| … \| … \|`* |
| 7 | `\| Broad gate \| bin/test -q \| tee out \|` — a bare pipe | `("Broad gate", "bin/test -q")` — the command truncated, the row below | no `Broad gate`; `Mode` below it stepped to | refused at the line, the same sentence; the sealer adds *write it `\|`* |
| 8 | a stray `\|---\|---\|` mid-table | a row `("---", "---")`, then the rows | the rows above; the rest dropped | the rows above; refused: *a delimiter row out of place* |
| 9 | a second `\| Item \| Value \|` mid-table, with its delimiter | rows `("Item", "Value")`, `("---", "---")`, then the rest | the rows above; the rest dropped | `("Item", "Value")` read as a row, then refused at the delimiter |
| 10 | a row above the header, a blank line between | the table | the table | the table |
| 11 | a row directly above the header | the table; the row above is a paragraph | the table | refused, as 1 |
| 12 | the header indented one space | the table | no header found: nothing | the table |
| 13 | `\| not a row` before the first row | a row `("not a row", "")`, then the rows | the rows, the line stepped past | refused at the line: *not a 2-cell row* |
| 14 | a line with no pipe after the rows | a row of it, then the rows below | the rows above; the rest dropped | the rows above; refused: *a line with no pipe* |
| 15 | `## Notes` directly under the table, a `\|` line after it | the table ends; the line after the heading is not read | the same | the same, refusing nothing |
| 16 | a three-cell delimiter under the two-cell header | no table | `Mode` | refused: *a delimiter row of 3 cells* |

Three things the table shows, and the frame is built on them. Rows 3, 4, 5,
13, 16 are shapes where today's reader hands a gate a row GitHub does not
show. Rows 6, 7, 8, 14 are shapes where today's reader drops rows GitHub
shows, silently, with each dropped row falling to its default — #415's
defect, still present for every line kind but the piped one. Rows 1, 2 and
11 are the migration: a config GitHub renders and the walker refuses, with a
one-line edit as the remedy. Row 7 is the one the issue named: the sealer
stops there today too, reporting the row absent or quoting the line; after
this work it quotes the line and names the escape, and runs nothing — the
command GitHub shows for that row is not the one the person wrote.

**The interface.** `hooks/config.py` keeps every exported name a caller
spells today except the four `## Removes` names, and adds one:

- `config_table(text) -> (rows, refusals)`: `gfm_table(text, CONFIG_TABLE)`
  where `CONFIG_TABLE = ("Item", "Value")`, with rows as
  `(index, item, value)` — `index` the row's line in `text.splitlines()`,
  as `indexed_config_rows` numbers it, and the cells stripped and unescaped
  as `table_cells` returns them. A text holding no such table is
  `([], [])`: no table declares nothing, everywhere, as no file does.
- `indexed_config_rows(text)` and `config_rows(text)` are projections of
  `config_table`'s rows, kept for the callers that spell them.
- `config_value(text, item)` reads `config_table`: `(value, None)` for a row
  the walk read; `(None, sentence)` for a doubled row, as today; and
  `(None, sentence)` — the walker's first refusal — for an item the walk
  did not read in a refused table. `value_of(rows, item)` is unchanged and
  stays the rule for a caller holding rows; such a caller asks
  `config_table` for the refusals and acts on them by its own kind.
- `declared_mode` answers `"refused"` on either sentence, which the mode
  gate already reads as silence (`hooks/mode-gate.py#undeclared`).
- `pact_declaration` appends the walker's refusals to the list it already
  returns, with `notify` None, so `pact-check` exits 2 and a signer's CI
  prints a notice, the split #647 decided.
- `refusal(text)` leaves (`## Removes`); the walker's sentences are the
  refusal, and `config_table` is where a caller with somebody to tell reads
  them.

**The refusal sentences are the walker's own**, as `gfm_table` already
writes them for the pact tables, each after a noun naming the file. The
sealer's one addition is the `\|` remedy where the stopping line's first
cell names its row, and #430's condition on the clause about rows below —
`missing_row` owns both, the walker's sentence is not changed for one
caller.

**The `Reads:` class.** `config_table`, `config_rows`, `indexed_config_rows`,
`config_value` and `declared_value` declare `guess — a person's
\`| Item | Value |\` table, read as cmark-gfm renders it; unknown refused`.
Row 95 of the inventory called the grammar `owned` because `seal mode`
writes the file; the walker's own row 108 declares `guess`, and a reader of
a table a person edits takes the class of the text it reads.

**The writer** locates the `Mode` rows and the insertion point from
`config_table`'s row indices: the line to overwrite is a row whose item is
`Mode`; the insertion point is the line after the last row, or after the
delimiter row where the table holds no row yet — the delimiter's index is
the header's plus one, and the header is the first shown line whose cells
are `CONFIG_TABLE`, which `gfm_table` already finds; the builder either
exposes that index from the walk or re-finds it through `table_cells` over
`unfenced`, and does not write a third grammar for it. A refused table is
refused by `with_row` in the shape a doubled `Mode` row already is: `(None,
sentence)`, and `write_row` prints it with *Nothing was written*.

**The vendored twin** carries the walker's table grammar on lines it can
judge alone — the header, a delimiter row of the header's width directly
under it, a row of the header's width written `| … |`, a blank line ending
the table, a line it cannot read as one of those refused in the plugin's
sentence — and nothing of `hooks/blocks.py`. It returns `(rows, refusals)`;
`cutoff_row` reads it as it reads the plugin's. Where a line is a table end
to the walker by block state the twin lacks, the twin refuses the line
instead, which is the stated direction: a vendored `--reverify` may refuse
where the plugin reads, never read where the plugin refuses.

## Rule changes

- nothing
  why: internal: one walker held to cmark-gfm reads the config table, held by
    tests/test_the_mode_question_is_asked_once.py.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the config table's own row grammar | `hooks/config.py#CONFIG_ROW` | the walker's `TABLE_ROW` and `table_cells`; `CELL` stays, because `TABLE_ROW` and `pact_check.py#path_map` are built on it |
| the config table's own header grammar | `hooks/config.py#CONFIG_HEADER` | `CONFIG_TABLE`, the header tuple `gfm_table` is handed; `CONFIG_SEPARATOR` stays for `pact_check.py#path_map` alone, and its comment says so |
| the third walk, and its `(refused, below, stopper)` contract | `hooks/config.py#refusal` | `config_table`'s refusals, the walker's sentences |
| the writer's walk | `skills/implement/scripts/seal.py#table_span` | `with_row` over `config_table`'s row indices |
| the sealer's pass-through of the triple | `skills/verify/scripts/broad_gate.py#refusal` | `missing_row` reads `config_table` |
| the arm that asked what parsed below the quoted line | `skills/verify/scripts/broad_gate.py#rows_read` | nothing: the walker never steps past a line, so no row is ever read below a refused one |
| the arm that asked whether the row was among those the stopping line took | `skills/verify/scripts/broad_gate.py#hides_this_row` | nothing: an item the walk did not read is a refusal naming the stopping line, by S2 |
| the pin that a three-cell row ends the table silently | `tests/test_the_mode_question_is_asked_once.py#test_a_three_column_row_still_ends_the_table` | a case that the line is refused and the rows above it arrive (shape 6) |
| the pin that `seal mode` writes a second `Mode` row under a bare-piped line | `tests/test_the_mode_question_is_asked_once.py#test_seal_mode_still_writes_a_second_mode_row_for_a_bare_pipe` | S5's case: nothing is written and the line is named |
| the pin that a separator below the rows ends the table silently | `tests/test_the_pull_request_language_is_the_repositorys.py#test_a_separator_below_the_rows_ends_the_table` | a case that it is refused as a delimiter row out of place (shape 8) |
| the pin that a repeated header ends the table | `tests/test_the_pull_request_language_is_the_repositorys.py#test_a_repeated_header_ends_the_table` | a case that the header is read as a row and the doubled item is refused (shape 9) |
| the pin that a blank line between the delimiter and the first row is tolerated | `tests/test_the_pull_request_language_is_the_repositorys.py#test_junk_above_the_first_row_is_still_tolerated` | a case that the table ends at the blank line and the row below is refused as never reached |
| the sealer's pin that rows below a first-row refusal arrive | `tests/test_the_seal_is_taken_once_by_the_sealer.py#test_the_rows_below_a_first_row_refusal_really_do_arrive` | nothing: the walker reads no row below a refused line |
| the sealer's pin on the *rows below were read* arm | `tests/test_the_seal_is_taken_once_by_the_sealer.py#test_a_refusal_above_the_first_row_says_what_actually_arrived` | the same |
| the sealer's pin on the *more than one line to write* arm | `tests/test_the_seal_is_taken_once_by_the_sealer.py#test_the_arm_whose_repair_costs_a_row_says_there_is_more_to_write` | the same: the instructed edit loses no row, because none was read past the line |
| the sealer's pin that a second refused line decides the first one's cost | `tests/test_the_seal_is_taken_once_by_the_sealer.py#test_a_second_refused_line_is_what_decides_what_a_first_one_cost` | the first refused line is always the stopping line |
| the sealer's pin that every refused line is read, not only the first | `tests/test_the_seal_is_taken_once_by_the_sealer.py#test_the_gate_reads_every_refused_line_and_not_only_the_first` | the same |
| the sealer's pin on the arm where the quoted line was read and a lower line stopped the reader | `tests/test_the_seal_is_taken_once_by_the_sealer.py#test_a_stopping_line_lower_down_with_nothing_under_it_names_no_rows` | a `Broad gate` row the walk read is a value and the gate runs; there is no refusal to word |
| the sealer's pin on `hides_this_row` | `tests/test_the_seal_is_taken_once_by_the_sealer.py#test_a_hidden_row_alone_under_the_stopping_line_has_no_others` | S6's sentence for a row under the stopping line, re-pinned under its own name |

### Why these rows

Every other case the stop rule's cases hold is re-pinned in place to the
walker's answer and keeps its name; a removal a phase makes that this table
did not name is a divergence row in `overview.md`.

## Open questions → questions.md

Anything a planner must answer lives in questions.md, not inline —
unanswered questions buried in prose read as decided. Both decisions the
issue left open are decided in `plan.md` and recorded there as decided.

Framed 2026-10-13 by framer, before the build.
