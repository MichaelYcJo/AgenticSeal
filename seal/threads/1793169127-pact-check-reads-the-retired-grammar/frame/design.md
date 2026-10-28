# Feature Specification: 1793169127-pact-check-reads-the-retired-grammar

Issue #913, two leftovers in what `skills/verify/scripts/pact_check.py`
reads. The machine-local path map is read by a stop rule the config table
retired, and the pact anchor is an inline token whose quotes, slash and at
sign people mistype, so the reader grew a second grammar that names each
mistype.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *Repo rule: text an agent or a check reads has one reading*, and `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* | Nothing an agent writes or a check reads uses a symbol a reader can trip on as syntax, and no spelling a near miss could pass. This decides each symbol of the issue's second part (*Scope*, item 2) |
| `CLAUDE.md` *The rule a mechanism is kept against* | A mechanism stays only while it catches something. It removes the unit resolver in `skills/verify/scripts/coordinates.py`, which has had no caller since #944 removed the ledger, and the census that guarded the coordinate's hash grammar |
| `docs/the-pact.md` *The pact anchor*, *How a signer names the pact*, *`seal pact` reconciles, locally* | The policy in force for the anchor, the `Pact` row's name rule and the map. `## Rule changes` below states what changes in each |
| `docs/the-pact.md` *A signer's CI reads nothing of the pact* | `skills/code-review/scripts/chain_check.py` holds no pact arm (read; `git grep -n -i pact -- skills/code-review/scripts/` prints nothing, executed). Every sentence in the touched files that says a signer's CI prints the relationship stands on a fact #923 removed |
| `docs/the-pact.md` *The words*, the second rule | The tree's precedent for a retired spelling: a permanent file nobody regenerates (a pact headed `Signatory`) is read under the old spelling with a line in no exit class. A frame is not permanent, which is why this work refuses the inline anchor instead (`questions.md` Q1) |
| `hooks/lib/config.py#gfm_table` docstring, and #871's frame `0ed5dd3b:seal/specs/1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker/plan.md` *Operational impact* | One walker reads every table as GitHub renders it, or refuses it. The map and the anchor become tables that walker reads |
| `6046f062:seal/specs/1792627930-the-section-sign-is-still-syntax/questions.md` Q2, answered (a) by the owner on 2026-10-22 | The coordinate's `#` and `>`, the pact anchors and the pact template's comment were left to a later item "with the cross-repository migration a pact anchor needs". This is that item |
| `docs/the-reader-registry.md` *A frame names what its work removes* | `## Removes` below lists every unit and sentence the work takes out |

## Scope

**In.**

1. **The machine-local map is read by the table walker.**
   `pact_check.py#path_map` (`:249`, read) reads `~/.claude/agentic/pact-paths.md`
   with `config.gfm_table(text, ("Remote", "Path"))`. Its own header pattern
   `MAP_HEADER` (`:144`), its row pattern built on `config.CELL` (`:261`) and
   its use of `config.CONFIG_SEPARATOR` (`:269`) go. With them goes
   `hooks/lib/config.py#CONFIG_SEPARATOR` (`:102`), whose comment names
   `path_map` as its one reader (read; `git grep -n CONFIG_SEPARATOR -- '*.py'`
   prints `:102` and `pact_check.py:269` only, executed). `CELL` stays,
   because `TABLE_ROW`, `CELL_PIPE` and `FIRST_CELL` are built on it; the
   sentence of its comment that names `path_map` goes.
   What the map's reader refuses, each printed as
   `REFUSED ~/.claude/agentic/pact-paths.md — the map <sentence>` at exit 2:
   - a map that is there and will not read: `the map is there and could not
     be read`. Today the line prints the path twice (`:259`), and the
     sentence now reads after the words `the map` like every other;
   - a map holding no `| Remote | Path |` table, which today reads as empty
     with nothing printed. The docstring's own rule, *a map that is there and
     will not read is a refusal, because reading it as empty would report
     every signer it names as not found*, covers this case too;
   - every refusal the walk returns (a header under a non-blank line, a
     row the walk never reaches, a row of another width). This is the
     defect: the first line that is not a row ends the map today with
     nothing printed (#834 part 4 row P4);
   - a row with an empty cell;
   - a remote written on two rows, compared normalised: neither row is
     read, as a `Pact` row written twice has no value
     (`hooks/lib/config.py#pact_declaration`);
   - a second `| Remote | Path |` header in the file, named at its line,
     because the walk reads the first table only.
   The rows the walk did read are used, as `pact_signers` uses the signer
   rows it read before a refusal.

2. **Each symbol the issue names, judged.**
   - **The pact anchor's `:`, `/`, quotes and `@` are syntax a reader trips
     on.** The evidence is the tree's own. `pact_check.py#PACT_MENTION_RE`
     (`:159` to `:188`) and `#near_miss` (`:210`) exist to name a mistyped
     anchor, they were built across four review findings (round 1 of #647
     yellow 4, round 2 yellow 13, round 3 of #735 yellow 19, round 1 of PR
     #749 yellow 4, read from their comments), and
     `tests/skills/test_pact_check.py:72` lists fifteen mistyped shapes. A
     grammar that needs a second grammar to name its typos is the case the
     repo rule names. **The anchor becomes one row of a
     `| Pact | Clause | Hash |` table** in a signer's `frame/design.md`, read
     by `gfm_table`. `PACT_ANCHOR_RE`, `PACT_NAME` and `unescape` in
     `coordinates.py`, and `PACT_MENTION_RE`, `near_miss`, `OPEN_QUOTE` and
     `CLOSE_QUOTE` in `pact_check.py`, go. The term *pact anchor* stays,
     and means one row of that table.
   - **The `Pact` cell holds the origin remote URL of the pact's
     repository**, the value the signer's `Pact` row holds, compared
     normalised. So *Pact* keeps one meaning in a signer's two files, and a
     pact has one identifier. The name derived from the URL's last segment
     existed for the inline token alone, so `config.pact_name`,
     `config.PACT_NAME_RE`, the `named` parameter of
     `config.remote_entries` and its two refusals go. Two pacts whose URLs
     end in one segment are no longer refused. `pact_declaration` answers
     `(as written, normalised)` pairs.
   - **The inline form is refused** (`questions.md` Q1, default): a `pact:`
     token outside a closed fenced code block, in a signer's frame, is
     refused at its line at exit 2, and the refusal names the row to write
     in its place. A token is `pact:` with no letter, digit, `_`, `.`, `@`,
     `/` or `-` before it and a character that is not a space after it, so
     `compact:` is no token. One pattern, and it names no typo.
   - **The `#` of `path#unit` is a spelling every reader agrees on**, as
     `##` is for a heading: it is a URL fragment, and no shipped script
     reads it as grammar. Its readers are `chain_check.py:914`, which
     refuses it in a `location:` line, and `evals/scripts/replay_targets.py:83`,
     which reads an eval truth (read; `git grep` over the scripts,
     executed). It stays, and so does the hint in
     `templates/records/sdd-design.md`'s `## Removes` table, which names it.
   - **The `>` has no reader and no writer.** It was the ledger's
     `path#unit>"a line"`, and the ledger left with #944 (`5b1f6fae`). No
     line outside `seal/`, `changelog/` and `CHANGELOG.md` holds the form
     (executed, `git grep -n -E 'unit>|#[a-z_]+>'`). Nothing changes for it.
   - **`templates/setup/pact.md`'s comment stays and states the table.**
     The file is begun in a consuming repository, where `docs/the-pact.md`
     is not, so the comment is the only guidance there. Its four-space
     example of the inline token becomes the table's header, delimiter row
     and one placeholder row.

3. **`coordinates.py` keeps what `pact_check.py` reads.** The unit resolver,
   `resolve_unit` and every unit only it reaches (`Resolution`, `py_spans`,
   `parsed_spans`, `text_regions`, `bounding_rule`, `unbounded`,
   `AST_SUFFIXES`, `HEADING_SUFFIXES`), has no caller outside the tests
   (executed, `git grep -l -w <name> -- '*.py' ':!tests' ':!seal'` for each
   name prints only `coordinates.py`; three other files match `unbounded` as a
   word of their own). It served the ledger's `path#unit@hash` rows. What stays:
   `HASH_LEN`, `shared_reader`, `quoted_lines`, `BLANK_RE`, `gfm_lines`,
   `unquoted`, `normalise`, `content_hash`, `heading_level`,
   `markdown_lines`, `_shown_lines`, `HEADING_SEP` and `heading_path`. The
   census `tests/censuses.py#coordinate_grammar`, which refuses a second
   spelling of the coordinate's `@hash` and exempts only `PACT_ANCHOR_RE`,
   goes with the grammar it guarded.

4. **The sentences that stand on #923's removed pact arm**, in the files
   this work already edits (contract rule 12, the class enumerated by
   `git grep` on *both callers*, *both commands*, *signer's CI* and
   `pact_notices`, executed): `pact_check.py:19` to `:21`;
   `coordinates.py:7` to `:8`; `hooks/lib/config.py:717` to `:722`,
   `:847` to `:849`, `:864` to `:865`, `:1141` to `:1142`, `:1345` and
   `:1409`; `templates/setup/config.md:417` to `:421`; and the last sentence
   of `README.md:269` and its edition `README.ko.md:261`. Each says what the
   one caller, `seal pact`, does.

5. **Every text that states the inline anchor's shape, or the name rule**,
   rewritten to the table: `templates/setup/config.md:147` (the list of
   words no row translates: the header cells `Pact`, `Clause` and `Hash`
   stay English, because a checker matches them), `templates/setup/config.md:416`
   to `:417`, `skills/implement/orchestration.md:598` to `:599`, and the
   docstrings of `pact_check.py` and `coordinates.py`.

**Out, and whose.**

| Left out | Whose, and why |
|---|---|
| The `#` in `path#unit` everywhere it is written, the contract and `agents/*.md` included | Nobody's: *Scope* item 2 judges it a spelling, so nothing changes |
| An anchor table in `templates/records/sdd-design.md` | Nobody's: a pact is rare, and a section every frame carries empty is a value stated where it holds nothing. `docs/the-pact.md` and `templates/setup/pact.md`'s comment state the shape |
| The ` / ` between the headings of a clause path, and a heading that holds ` / ` | Nobody's: the separator is unchanged, and a heading holding it cannot be cited, as today (`docs/the-pact.md` *What this does not see* names the address rule) |
| The summary line's middle dots and the em dash in `seal pact`'s lines | A later item the owner opens: they separate printed words a person reads, no check reads them, and #913 does not name them |
| `.test_durations` entries for the cases phase 3 deletes | The orchestrator's broad run regenerates the file (`.github/scripts/durations_union.py`) |
| `evals/scripts/replay_targets.py`'s `#unit` reading | `evals/`: a reader of recorded eval truths, not of anything this work writes |
| `docs/` | Not edited in this diff: `## Rule changes` |

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1, the map as the walker reads it | Given a map whose table, headed with the cells `Remote` and `Path`, holds two rows, when `path_map` reads it, then both are keyed by the remote normalised and no refusal is returned | `tests/skills/test_pact_check.py` *Test_path_map*, the existing case |
| S2, a row past the map's end | Given the map with a paragraph and then a row below the table, when `seal pact` runs, then the row above is used and `REFUSED ~/.claude/agentic/pact-paths.md — the map has a ...` names the unread row, at exit 2 | a case in *Test_path_map* and one in *Test_check*, each seen red against `977b6613`, where the row is dropped with nothing printed |
| S3, a map with no table, a doubled remote, an empty cell, a second header | Given each shape, when `seal pact` runs, then one `REFUSED ~/.claude/agentic/pact-paths.md — the map ...` line names it, at exit 2, and a doubled remote's rows are both unread | one case per shape, seen red |
| S4, an unreadable map | Given the map as a directory or a dangling link, when `seal pact` runs, then it prints `REFUSED ~/.claude/agentic/pact-paths.md — the map is there and could not be read` once, at exit 2 | the two existing cases, their pinned text rewritten |
| S5, no map | Given no file, when `path_map` reads, then the answer is an empty map and nothing is printed | the existing case |
| S6, an anchor row graded | Given a signer frame whose anchor table names the pact by any spelling of its URL, when `seal pact` runs, then each row naming the pact is graded `OK`, `SUPERSEDED`, `NOT TAKEN`, `UNMATCHED` or `BROKEN` as an inline anchor was, and each line that is not `OK` names the frame, the row's line and the clause path | `tests/skills/test_pact_check.py` *Test_check* and *Test_grade*, rewritten to rows |
| S7, rows that are not graded | Given a row naming another pact, and a table inside a closed fenced block, when `seal pact` runs, then neither is graded nor refused | a case in *Test_check* |
| S8, a row that cannot be graded | Given a row whose `Pact` cell is not one remote URL (a space, a backtick, no host and path), or a row naming the pact whose `Clause` cell opens with no heading, or whose `Hash` cell is not eight lowercase hex digits, when `seal pact` runs, then each is refused at its line, at exit 2 | one case per shape, seen red |
| S9, the inline form | Given a signer frame holding `pact:orders-api/"## A"@1a2b3c4d`, in a table cell or in prose and outside a fence, when `seal pact` runs, then it is refused at its line, at exit 2, and the line names the row to write; `compact:x` and a token inside a closed fence are not refused | cases in *Test_check*, the first seen red against `977b6613`, where the token is graded |
| S10, one identifier for a pact | Given a signer's `Pact` row listing two URLs that end in one segment, when `pact_declaration` reads it, then both are answered and nothing is refused; `pact_declaration` answers pairs | `tests/hooks/test_config.py` *Test_pact_declaration*; `tests/behaviour/test_a_signer_declares_its_pact.py` |
| S11, what leaves | When the work ends, the grep `plan.md` *Technical context* writes out prints nothing | the grep, its output in the last phase's record |
| S12, what stays | The cases that read `content_hash`, `heading_path`, `markdown_lines`, `unquoted` and `quoted_lines` pass unchanged | `tests/skills/test_coordinates.py`, `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py` |
| S13, the words a person reads | Every sentence `seal pact` prints is still read by `tests/behaviour/test_one_word_one_meaning.py`, and passes it | that module |
| S14, the rule changes parse | The `## Rule changes` block below is read by `skills/settle/scripts/rule_changes.py` with no refusal | `chain-check` at the pull request reads it through that reader |

## Data & interfaces

**The map**, unchanged on disk:

| Remote | Path |
|---|---|
| `git@example.com:org/orders-web.git` | `~/work/orders-web` |

`path_map(config, home_dir)` answers `(found, refusals)`, where `refusals`
is a list of sentences, each reading after the words `the map`; `check`
prints each as `REFUSED ~/.claude/agentic/pact-paths.md — the map <sentence>`.

**The pact anchor** is one row of the **anchor table**, the table headed
with the three cells `Pact`, `Clause` and `Hash`, in a signer's
`frame/design.md` under `## Grounding`:

| Pact | Clause | Hash |
|---|---|---|
| `git@example.com:org/orders-api.git` | `## Order response shape / ### Fields` | `1a2b3c4d` |

In the file the cells are written bare; the backticks above are this
record's, around values. A cell holds no backtick: a `Pact` cell holding
one is not one remote URL, and a `Clause` cell holding one opens with no
heading, so both are refused (S8). A `|` inside a heading is written `\|`,
which `config.table_cells` reduces. The header cells are matched by
`gfm_table` exactly, so they stay English in every record language.

- `pact_check.py#clause_hash(checker, text, clause)` takes the heading path
  as the cell holds it, with no quotes to strip and no escape but `\|`,
  which the walker has already reduced.
- `pact_check.py#grade` takes the clause path where it took a quoted
  locator.
- `hooks/lib/config.py#remote_entries(entries, empty)` loses `named`, and
  `pact_declaration` answers `[(as written, normalised)]`.
- `seal pact`'s `READ` line and summary line name the pact by its origin
  URL as written where they named it by its last segment, for example
  `READ <signer> <path> — 2 pact anchors naming this pact` and
  `seal pact: the pact at git@example.com:org/orders-api.git — ...`. The
  exact sentences are the build's, pinned by a case each (contract rule 14).
- The refusal of a repository with no origin says no anchor can be matched
  to the pact, where it said the name cannot be derived.

## Rule changes

- change
  file: docs/the-pact.md
  section: How a signer names the pact
  from: `Pact` is the origin remote URL of the pact's repository, several
    separated by `;`, compared normalised; its last path segment is the name
    an anchor carries, so two pacts ending in one segment are refused.
  to: `Pact` is the origin remote URL of the pact's repository, several
    separated by `;`, compared normalised, and a pact anchor names the pact
    by that same URL.
- change
  file: docs/the-pact.md
  section: The pact anchor
  from: **A signer cites a clause as `pact:<name>/"<heading path>"@<hash>`.**
    Every `##` heading of `seal/pact.md` below its `| Signer |` table is a
    clause, and a `###` narrows inside one. The hash is the content hash
    `coordinates.py#content_hash` gives the clause's region, the value a
    local coordinate to that heading carries. A signer writes the anchor in
    a spec's Grounding, recording what the work was built against.
  to: **A signer cites a clause as one row of a `| Pact | Clause | Hash |`
    table in a work item's `frame/design.md`, and `seal pact` reads the table
    with `hooks/lib/config.py#gfm_table`.** The row is the pact anchor, and
    it records what the work was built against. `Pact` is the origin remote
    URL of the pact's repository, as the signer's `Pact` row writes it,
    compared normalised. `Clause` is the clause's heading path, such as
    `## Order response shape / ### Fields`: every `##` heading of
    `seal/pact.md` below its `| Signer |` table is a clause, and a `###`
    narrows inside one. `Hash` is the eight lowercase hex digits
    `coordinates.py#content_hash` gives the clause's region, `00000000`
    until the first report names the real one. The walker reads the table as
    GitHub renders it, as it reads every other table here, so nothing in a
    row is quoted or escaped except a pipe, written `\|`. A row naming
    another pact is passed over.
- change
  file: docs/the-pact.md
  section: The pact anchor
  from: **A token begins a pact anchor where `pact:<name>` is followed at
    once by `/` or `#`, or by the rest of an anchor with its `/` missing, and
    `seal pact` refuses a token that begins one and does not go on to
    parse.** The rest of an anchor is a quoted heading path closed by `@`, or
    `@` and a hash, at once or after one mark or one space. The marks are
    `.`, `-` and `_`, which the name itself could otherwise hold, and one of
    them standing just before the `/` counts too, so the commonest typos are
    named rather than read by nobody. Anything else naming the pact is a
    mention and is left alone: `pact:<name>` followed by punctuation, a
    space or the end of a code span. The one form that begins an anchor and
    is not an attempt is the one this plugin prints to show the shape, its
    heading path a placeholder, `/"<heading path>"`. So `pact:<name>/`
    written in prose is refused, and the refusal names both ways out: quote
    the heading path and give it a hash, or, where the text shows the shape
    rather than citing a clause, put it in a fenced code block, which
    nothing reads.
  to: **`seal pact` refuses, at exit 2, a row it cannot grade and every
    `pact:` token in a signer's frame.** A row whose `Pact` cell is not one
    remote URL names no pact anybody can tell, and a row naming this pact
    whose `Clause` cell does not open with a heading, or whose `Hash` cell
    is not eight lowercase hex digits, grades nothing; each is refused at
    its line. A `pact:` token outside a fenced code block is the inline
    anchor `seal pact` read through 0.23.x, and it is refused at its line
    with the row to write in its place. A frame leaves the tree at the
    settle after its release, so the rewrite is one row in a file that is
    leaving anyway, and a token passed over would read as a signer citing
    nothing. A text that shows the retired shape rather than citing a clause
    puts it in a fenced code block, which nothing reads.
- change
  file: docs/the-pact.md
  section: `seal pact` reconciles, locally
  from: It finds each checkout through `~/.claude/agentic/pact-paths.md` or
    the one sibling directory with that origin, guessing nothing; refuses a
    signer whose config does not name the pact; and grades every anchor
    naming the pact.
  to: It finds each checkout through the `| Remote | Path |` table of
    `~/.claude/agentic/pact-paths.md` or the one sibling directory with that
    origin, guessing nothing; refuses a signer whose config does not name
    the pact; and grades every anchor naming the pact. The map is read by
    `gfm_table`, as every other table is, and a map that is there and will
    not read, holds no such table, holds it twice, or has a row the walk
    does not read is refused at exit 2, because a row nobody reads reports
    its signer as not found. A remote written on two rows of the map is
    refused, and neither row is read.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The config table's separator pattern | `hooks/lib/config.py#CONFIG_SEPARATOR` | Its one reader, `path_map`, reads through `gfm_table`, whose `DELIMITER_ROW` judges the delimiter |
| The map's own header and row patterns | `skills/verify/scripts/pact_check.py#MAP_HEADER`, and the `row` pattern inside `pact_check.py#path_map` | `gfm_table` with the header `("Remote", "Path")` |
| The sentence of `CELL`'s comment naming `path_map` | `hooks/lib/config.py#CELL` | `path_map` no longer builds on `CELL` |
| The inline anchor's grammar | `skills/verify/scripts/coordinates.py#PACT_ANCHOR_RE`, `coordinates.py#PACT_NAME` | The anchor table, read by `gfm_table` |
| The near-miss grammar | `pact_check.py#PACT_MENTION_RE`, `pact_check.py#near_miss`, `pact_check.py#OPEN_QUOTE`, `pact_check.py#CLOSE_QUOTE`, and the comment above them | A row's cells are judged by their shape, and the inline form by one `pact:` token pattern |
| The heading path's quote and escape reader | `coordinates.py#unescape` | `config.table_cells` reduces an escaped pipe; nothing quotes a clause path |
| The pact's name | `hooks/lib/config.py#pact_name`, `config.py#PACT_NAME_RE`, the `named` parameter of `config.py#remote_entries` and its two refusals | The anchor names the pact by its URL, as the `Pact` row and the `Signer` table do |
| The unit resolver | `coordinates.py#resolve_unit`, `#Resolution`, `#py_spans`, `#parsed_spans`, `#text_regions`, `#bounding_rule`, `#unbounded`, `#AST_SUFFIXES`, `#HEADING_SUFFIXES` | No caller since the ledger left (#944) |
| The resolver's cases | `tests/behaviour/test_a_unit_is_bounded_where_a_parser_decides.py`, and the cases of `tests/skills/test_coordinates.py` that call a removed unit | Their unit goes; no `check:` line names the behaviour module (executed, `git grep`) |
| The census of the coordinate's hash | `tests/censuses.py#coordinate_grammar`, `tests/censuses.py#HASH_AFTER_AT`, its entry in the census list at `tests/censuses.py:1221`, and `tests/test_censuses.py` *Test_coordinate_grammar* | The grammar it guarded is gone; `heading_rule` beside it stays |
| The cases pinning the near-miss grammar | `tests/skills/test_pact_check.py` *Test_module* `test_accepts_each_attempt_at_an_anchor_as_beginning_one` and `test_refuses_to_read_prose_naming_the_pact_as_an_attempt`; *Test_check* `test_refuses_an_anchor_that_does_not_parse` and `test_accepts_the_pact_s_name_inside_a_graded_anchor_s_heading`; `tests/skills/test_coordinates.py:378` to `:380` | The row-shape cases of S8 and the inline-form cases of S9 |
| The refusal of a `Pact` URL a name cannot carry | `tests/hooks/test_config.py:1389`, and the case holding it | The name rule goes |
| The sentences that say a signer's CI prints the pact relationship | *Scope* item 4's coordinates | `docs/the-pact.md` *A signer's CI reads nothing of the pact* |
| The inline anchor's shape in the templates and the orchestration skill | `templates/setup/pact.md`'s comment example; `templates/setup/config.md:147`, `:416` to `:417`; `skills/implement/orchestration.md:598` | Each states the table instead |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-28 by framer, before the build.
