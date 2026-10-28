# Phase 2: 1793169127-pact-check-reads-the-retired-grammar

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 20f3f2aa |

## What this phase was asked

Build `plan.md`'s phase 2 as its row states. `check` reads the anchor
table of each signer frame with `gfm_table` and grades each row naming the
pact by URL. It refuses a row by S8's three shapes, a second anchor table,
and every `pact:` token outside a closed fence (`questions.md` Q1, default
(a), which the owner has not answered and is not asked). `clause_hash` and
`grade` take the clause path. `PACT_ANCHOR_RE`, `PACT_NAME`, `unescape`,
`PACT_MENTION_RE`, `near_miss`, `OPEN_QUOTE`, `CLOSE_QUOTE`, `pact_name`,
`PACT_NAME_RE` and `remote_entries`' `named` go, and `pact_declaration`
answers pairs. The `READ`, summary and no-origin lines name the pact by URL.
The sentences of *Scope* item 4 and the shape texts of item 5 are rewritten.
`tests/conftest.py`'s pact world cites by row, and only that block changes
(Q2), away from #1058's region near `:514-536`. `docs/` is not edited.

## What this phase found

- `coordinates.py#unescape` still had one caller after this phase:
  `resolve_unit`, which phase 3 removes. So `unescape` leaves with the
  resolver in phase 3 and not here. `gaps.md` records it.
- The anchor table's walk can refuse in its own words, for example a row
  of another width. S8 names three row shapes and the plan names a second
  table, but neither names the walk's refusals. A row the walk does not
  reach would read as a signer citing nothing. So every walk refusal except
  `holds no` is printed after `the frame` at exit 2, as the map's are.
  `gaps.md` *Fed back into the spec* records it as inferred.
- The second-header refusal is now one function, `first_table`, which the
  map and the frames both call. It holds the rule phase 1 found: a second
  header is named only where the walk refused nothing.
- The refusal sentences for a row do not quote the cell. A cell holding a
  backtick cannot be quoted inside backticks, and the row's line already
  locates it. The four sentences are pinned whole in
  `tests/skills/test_pact_check.py` (`NOT_ONE_URL`, `NO_HEADING`,
  `NOT_A_HASH`, `INLINE`).
- A `Pact` cell is judged by `config.remote_entries`, the reader of the
  `Pact` row, plus one rule of its own: a backtick. Without that rule a
  backticked URL normalises to a string ending in a backtick, matches no
  pact, and is passed over in silence.
- The no-origin refusal now tests for an origin that is not set. Before,
  it tested for one whose name could not be derived. An origin that
  reduces to no host and path is now read, and no row can match it.
- *Scope* item 4's class, enumerated with `git grep -n -i -E 'both
  callers|both commands|signer.s CI|pact_notices|prints the relationship'`,
  held four sentences the frame did not list. All four were in test files
  this phase already edited: `tests/behaviour/test_a_signer_declares_its_pact.py:11`,
  `tests/behaviour/test_one_word_one_meaning.py:761` and `:771`, and
  `tests/hooks/test_config.py:1710` (lines at `977b6613`). Each now names
  `seal pact` alone. The grep's other hits are about other commands.
- `tests/conftest.py`, the lines changed, at `977b6613`: `:1423` (`LOCATOR`
  became `CLAUSE_PATH`, the bare clause path), `:1430` (`ORDERS` pairs, and
  `ANCHOR_LINE`), `:1448` (`clause`), `:1459-1460` (`grounding_row` became
  `anchor_table`) and `:1509-1512` (`World.cite`). Nothing outside
  `:1420-1530` changed.
- The post-edit formatter removes an import that is not yet used. Imports
  added before the cases that use them were dropped once, and the first red
  run stopped at collection. They were added again with their uses.
- Red runs: 26 cases failed against the code as at `977b6613` (exit 1).
  At the base an inline token was graded `BROKEN`, an anchor row was never
  read and the run exited 0, two URLs ending in `api` were refused, and
  `pact_declaration` answered triples.
- Mutants over `pact_check.py`: 16 in one batch, 15 red. The survivor was
  the guard that keeps a frame with no anchor table silent. It was red
  after the accept case gained such a frame (commit `20f3f2aa`). The
  `(?=\S)` half of the token pattern got a case of its own before the
  batch ran (commit `39e84833`). Mutants over `config.py#remote_entries`:
  the no-host-and-path arm and the one-repository arm, both red.
- Green: `tests/skills/test_pact_check.py`, `tests/hooks/test_config.py`,
  `tests/behaviour/test_a_signer_declares_its_pact.py`,
  `tests/behaviour/test_one_word_one_meaning.py`,
  `tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py`,
  `tests/skills/test_coordinates.py`, and three modules that read the
  edited texts (`test_docs_line_wrap.py`,
  `test_a_document_that_names_a_script_says_how_to_reach_it.py`,
  `test_no_document_names_the_old_roots.py`): 960 passed, 8 skipped, exit 0.
