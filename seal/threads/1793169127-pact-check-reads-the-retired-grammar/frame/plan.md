# Implementation Plan: 1793169127-pact-check-reads-the-retired-grammar

Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phases 1 to 3.

## Summary

`seal pact` reads two tables of its own grammar. The machine-local map
`~/.claude/agentic/pact-paths.md` moves onto `hooks/lib/config.py#gfm_table`,
which every other table is read by, so a line the walk does not read is
refused instead of ending the map with nothing printed. The pact anchor
moves from the inline token `pact:<name>/"<heading path>"@<hash>` to a row
of the anchor table (cells `Pact`, `Clause`, `Hash`), read by the same
walker, so the near-miss grammar that named its typos goes, and the pact is
named by its origin URL as everywhere else. `skills/verify/scripts/coordinates.py`
keeps the heading-path and hash units `pact_check.py` reads and loses the
unit resolver nobody has called since #944. Three phases, in order.

## Technical context

**What this builds on, by coordinate (read at `977b6613`).**

- `skills/verify/scripts/pact_check.py#path_map` (`:249` to `:276`) walks
  `config.unfenced` lines, waits for `MAP_HEADER` (`:144`), skips
  `config.CONFIG_SEPARATOR` (`:269`) and breaks at the first line its `row`
  pattern (`:261`) refuses. `check` (`:510` to `:512`) prints one refusal,
  `REFUSED <map> — <sentence>`, and `REFUSED` is in `EXIT_TWO` (`:191`).
- `hooks/lib/config.py#gfm_table` (`:1092`) answers `(rows, refusals)`, the
  rows read before a refusal included, and a first refusal starting
  `holds no ` where the header is absent. `pact_signers` (`:1327`) is the
  model for using both halves: rows read, refusals printed.
  `config.table_cells` reduces `\|` to a pipe in each cell.
- `pact_check.py#check` (`:571` to `:617`) reads each signer frame through
  `checker.unquoted`, grades `checker.PACT_ANCHOR_RE` matches with `grade`,
  then refuses `PACT_MENTION_RE` tokens that did not parse. `clause_hash`
  (`:391`) strips the locator's quotes and calls `checker.unescape`.
  `anchor_files` (`:326`) lists every `threads/*/frame/design.md`.
- `hooks/lib/config.py#remote_entries` (`:791`) refuses on `named` a name
  outside `PACT_NAME_RE` and two entries ending in one segment;
  `pact_declaration` (`:833`) passes `named=True`. `pact_check.py#check`
  derives `name` with `config.pact_name(mine)` (`:480`) for its filter, its
  `READ` line and its summary.
- `tests/conftest.py:1420` to `:1515` holds the pact world: `PACT_URL`,
  `LOCATOR`, `ORDERS`, `clause`, `grounding_row`, and `World.cite` and
  `World.map`. `World.map` already writes a well-formed table.
- `coordinates.py#resolve_unit` and the units only it reaches have no caller
  outside `tests/skills/test_coordinates.py` and
  `tests/behaviour/test_a_unit_is_bounded_where_a_parser_decides.py`
  (executed, `git grep -l -w`).

**The grep S11 runs, on one line:**
`git grep -n -w -E 'CONFIG_SEPARATOR|MAP_HEADER|PACT_ANCHOR_RE|PACT_MENTION_RE|near_miss|PACT_NAME|PACT_NAME_RE|pact_name|resolve_unit|coordinate_grammar|pact_notices' -- ':!seal' ':!changelog' ':!CHANGELOG.md' ':!.test_durations'`

**The failure scenario of the chosen approach, six months on.** A signer's
framer writes the anchor table with the clause path in backticks, as this
repository writes most values in a cell, and `seal pact` refuses the row at
exit 2 with the shape named; the cost is one edit, in the direction that
speaks. A person who keeps an old frame with an inline anchor across the
upgrade gets a refusal on every run until the frame settles (`questions.md`
Q1). A heading that holds ` / ` still cannot be cited, as today. And a frame
holding two anchor tables is refused at the second header, because the walk
reads the first table only; without that refusal the second table's rows
would read as citing nothing.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. The map keeps its own reader, with a refusal added where the loop now breaks | Two grammars for one kind of table: the map's loop and `gfm_table` answer an indented row, an escaped pipe after an even run of backslashes, or a row under a list item differently, and each difference is found one review finding at a time, which is how `gfm_table`'s docstring says the first walker failed. Its premise, that the map needs a reader of its own, does not hold: it is a GFM table under a header, the shape `gfm_table` exists for | Not taken |
| A2. The map moves to another format, one `remote path` pair per line | Paths with spaces need a quoting rule, which is a new grammar; every map already written in a table breaks with no reader to name it; and `seal pact`'s remedy line prints a table row today (`pact_check.py:313`) | Not taken |
| A3. The map read by `gfm_table` with the header `("Remote", "Path")`, every refusal printed after the words `the map`, at exit 2 | A map a person edits by hand and never renders is held to GitHub's rendering; a header written directly under a line of prose is refused with the blank-line remedy, one edit | **Taken**: the one line the issue names, and the refusals of the class |
| A4. The inline anchor stays; its symbols are declared spellings everyone agrees on (keeps the structure) | The premise that keeps it is that readers agree on the spelling, and the tree shows they do not: fifteen mistyped shapes in `tests/skills/test_pact_check.py:72` and four review findings built `PACT_MENTION_RE` and `near_miss`. The next typo shape found is another branch of that regex, and the quote rule already reaches into curly quotes by code point (`pact_check.py:178`) | Not taken |
| A5. An inline anchor in words, such as `pact orders-api clause "## A" hash 1a2b3c4d` | Still a token grammar in prose, still quoted, and a mistyped keyword passes as prose unread: the near-miss reader comes back under new words | Not taken |
| A6. The anchor as a row of the anchor table, read by `gfm_table` (replaces the structure) | A cell is judged by shape, so the class of near misses is the walker's and the three shape rules', not a list of typos; the cost is a migration of in-flight signer frames (A8) and a table a framer has to know to write, which `docs/the-pact.md`, `templates/setup/pact.md` and `skills/implement/orchestration.md` state | **Taken** |
| A7. The `Pact` cell holds the pact's name, the URL's last segment, as the inline token did | *Pact* would mean a URL in the signer's `Pact` row and a name in the anchor table, one word with two meanings in the files one signer holds; and the refusal of two pacts ending in one segment, which exists only so a short token can tell them apart, would stay | Not taken |
| A8. The `Pact` cell holds the origin remote URL, compared normalised | Longer cells; a URL written with a typo matches no pact and its row is passed over as another pact's, the same direction a wrong URL in the `Pact` row has today | **Taken**: one identifier for a pact, and the name machinery goes |
| A9. The inline token, after the upgrade, is graded as before with a line in no exit class, the precedent of the `Signatory` header | The old grammar, its near-miss reader and its cases stay for as long as any signer might hold a token, which nothing can measure, and a later item has to remove them; the precedent is for a permanent file nobody regenerates, and a frame is neither | Not taken (`questions.md` Q1, option b) |
| A10. The inline token is refused at exit 2 by one `pact:` pattern, naming the row to write | A frame mid-flight in a signer repository is refused until one line is rewritten; `seal pact` runs in no CI, so nothing automated stops | **Taken** as `questions.md` Q1's default |
| A11. The inline token is passed over, unread | A signer whose every anchor is inline reads `0 pact anchors` at exit 0, a silent pass | Not taken |
| A12. The `#` of `path#unit` becomes words, such as `gfm_table` in `hooks/lib/config.py`, everywhere it is written (replaces the structure) | Every agent definition and the contract cite this way, so the change rewrites the preloads, which owes the paid non-inferiority run (`6046f062:seal/specs/1792627930-the-section-sign-is-still-syntax/questions.md` Q3), to remove a spelling no script reads as grammar | Not taken |
| A13. The `#` stays (keeps the structure) | Premise checked: no shipped script parses `path#unit` as grammar; `chain_check.py:914` reads it only to refuse it in a `location:` line, and `evals/scripts/replay_targets.py:83` reads recorded truths (executed, `git grep`). Should a reader start parsing it, the census removed in phase 3 is no longer there to say a second grammar appeared | **Taken** |
| A14. `coordinates.py`'s unit resolver stays, as a kernel for a future reader | Premise checked and false: no caller outside its own tests since #944 removed the ledger (executed); its docstring names two readers, one of which (`chain_check.py`) reads no anchor. Kept, it is maintained and reviewed for nothing, and its tests price the suite | Not taken |
| A15. The resolver and the census of the coordinate's hash go (phase 3) | A future reader of code units would rebuild it; git holds it at `977b6613` | **Taken** |
| A16. `templates/setup/pact.md`'s comment goes, as #1005 took the record templates' comments | The template is copied into a consuming repository, where `docs/the-pact.md` does not exist, so the person writing the pact would have no statement of the clause rule or the anchor's shape | Not taken |
| A17. The comment stays and states the anchor table | One more place states the shape beside `docs/the-pact.md`; the two live in different repositories once the template is copied, so neither can link the other | **Taken** |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The map through the walker (*Scope* item 1): `path_map` reads `("Remote", "Path")` with `config.gfm_table` and answers `(found, refusals)`; `check` prints each as `REFUSED ~/.claude/agentic/pact-paths.md — the map <sentence>`; a map with no table, a doubled remote, an empty cell and a second header are refused; `MAP_HEADER` and the `row` pattern go, and so does `config.CONFIG_SEPARATOR`, with `CELL`'s comment rewritten; `pact_check.py`'s docstring section *Where the signers are* states the refusals | `tests/skills/test_pact_check.py` *Test_path_map* and *Test_check*, a new case per refusal seen red against `977b6613`; `tests/hooks/test_config.py`; `git grep -n CONFIG_SEPARATOR -- '*.py'` prints nothing | |
| 2 | The anchor as a row (*Scope* items 2, 4 and 5): `check` reads the anchor table of each signer frame with `gfm_table`, grades each row naming the pact by URL, refuses a row by S8's three shapes, a second anchor table, and every `pact:` token outside a closed fence; `clause_hash` and `grade` take the clause path; `PACT_ANCHOR_RE`, `PACT_NAME`, `unescape`, `PACT_MENTION_RE`, `near_miss`, `OPEN_QUOTE`, `CLOSE_QUOTE`, `pact_name`, `PACT_NAME_RE` and `remote_entries`' `named` go; `pact_declaration` answers pairs; `READ`, summary and no-origin lines name the pact by URL; the sentences of *Scope* item 4 and the shape texts of item 5 are rewritten; `tests/conftest.py`'s pact world cites by row (`questions.md` Q2) | `tests/skills/test_pact_check.py`, `tests/hooks/test_config.py`, `tests/behaviour/test_a_signer_declares_its_pact.py`, `tests/behaviour/test_one_word_one_meaning.py`, `tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py`, `tests/skills/test_coordinates.py`; S8 and S9 cases seen red against `977b6613`; each changed printed sentence pinned (contract rule 14) | |
| 3 | `coordinates.py` keeps what `pact_check.py` reads (*Scope* item 3): the resolver and its units go, with `tests/behaviour/test_a_unit_is_bounded_where_a_parser_decides.py` and the resolver's cases in `tests/skills/test_coordinates.py`; `tests/censuses.py#coordinate_grammar`, `HASH_AFTER_AT`, its list entry and `tests/test_censuses.py` *Test_coordinate_grammar* go; the module docstring says what it holds and who reads it | `tests/skills/test_coordinates.py`, `tests/test_censuses.py`, `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py`, `tests/skills/test_pact_check.py`; S11's grep prints nothing | |

Each phase runs the modules it names and no broad run: the full suite,
the repository-wide lint and the typecheck are the orchestrator's one broad
gate after the review rounds settle (contract rule 2).

## Operational impact

- **A signer repository's in-flight frame with an inline anchor is refused
  by `seal pact` after the upgrade**, at exit 2, with the row to write named
  (`questions.md` Q1's default). `seal pact` runs in no CI, so no pull
  request and no hook changes verdict. The changelog fragment says so, with
  the row's shape.
- **A map at `~/.claude/agentic/pact-paths.md` that today reads silently**
  is refused at exit 2 where it holds no `| Remote | Path |` table, a row
  the walk does not read, an empty cell, a remote on two rows, or the header
  twice. A map `seal pact`'s remedy line taught has none of those shapes.
- **A signer's `Pact` row listing two URLs that end in one segment** is
  accepted where it was refused.
- **`seal pact`'s printed lines change**: the map's refusals, the `READ`
  line, the summary line and the no-origin refusal. Each is pinned by a
  case.
- **A census leaves `tests/censuses.py`** (phase 3). `CONTRIBUTING.md`
  *What a change to a gate must carry* is where the pull request answers for
  it and for `seal pact`'s changed verdicts; that body is the orchestrator's.
- No new dependency, no environment variable, no migration script: no
  command rewrites a signer's frame, as no command rewrites a pact.
