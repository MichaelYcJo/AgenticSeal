# Phase 3: 1794200906-settings-are-read-as-json

## What this phase found

**The frame holds for this phase.** Design *Scope* item 5, scenario S7, *Data & interfaces* and the *Removes* rows for the pact were read against the tree at `c58a69a5` before the build (read). The units *Removes* names for this phase stood there and are gone at `fe9e7072`: `lib/config.py#read_table`, `#renamed_header`, `#RENAMED_IN`, `#SIGNER_HEADER`, `#pact_signers` and `#_signer`, `pact_check.py#MAP_TABLE` and the call that printed the 0.18.x rename (`#renamed`), and the `| Signer |` table of `templates/setup/pact.md` with the paragraph that introduced it. After the commit, `git grep` of each name outside `seal/threads/` finds two lines, `docs/layout/the-pact.md:21` and `:147`. Design *Rule changes* removes the first's paragraph and rewrites the second at the settle (executed). The only remaining callers of `gfm_table` outside `tests/` and `docs/` are `seal.py`'s converter, `settle.py` and `pact_check.py#first_table` over the anchor table (executed: `git grep -n 'gfm_table('`). So phase 2's hand-off is met: the module docstring's "no setting is read through it" is now true.

**Decisions made in the build, each with its grounds.**

- The signers are read by a new `lib/config.py#signer_declaration(pairs)`, beside `pact_declaration`. `pact_signers` is not rewritten in its place. *Data & interfaces* names no reader function. The old function read `pact.md`'s text and the new one reads `config.json`'s pairs, so it is a second reader of the same grammar as `Pact` and not the old reader changed. Its contract is `(signers, refusals)`. An absent or empty key returns the one sentence `lib/config.py#NO_SIGNER`, which names the key and the remedy. A key written twice, or one holding no string, returns `config_value`'s refusal. Judged against design *Scope* item 5 ("in the grammar of `Pact`, read through `remote_entries`").
- `lib/config.py#remote_list(key, value)` splits a value at `;` and runs `remote_entries`. Both `pact_declaration` and `signer_declaration` end with it, so the empty-entry sentence has one source and names the key it came from. Judged against `skills/core/SKILL.md` *The rule a mechanism is kept against*: a fact has one source.
- In `pact_check.py#check`, a `config.json` at the pact's repository that will not parse is printed as `UNREADABLE` and exits 2 at once, the way an unreadable `pact.md` already does. This includes an earlier release's `config.md` standing alone. Each `signer_declaration` refusal is printed as `REFUSED seal/config.json — <sentence>`, and the signers it did read are still graded. A key listing the pact's own repository is refused at `seal/config.json`, with the remedy to take the entry out. The ONE-SIDED remedy now says to take the signer out of the `Pact signers` key of the pact's repository. Judged against design S7 and the existing exit-code rule of the script's docstring: exit 2 for what it cannot read.
- `pact_check.py#path_map` parses `pact-paths.json` with `json.loads(object_pairs_hook=config.Members)`, so a key written twice reaches the reader and is not silently folded by a dict. It refuses the following, each with the file named:
  - a file that does not parse as JSON, or whose top level is not one object, with no entry read;
  - an empty remote;
  - a value that is an empty string or not a string;
  - two or more keys that normalise to one remote, with none of them read.

  The other entries are read. `pact_check.py#checkout`'s remedy now gives the entry to add as a JSON member, written through `json.dumps`. Judged against design *Scope* item 5 and the *Rule changes* sentence for *`seal pact` reconciles, locally* ("will not parse as a JSON object, or that holds a value that is not a path, is refused at exit 2").
- `pact_check.py#after_path` strips the machine path from a reader's sentence, or returns "could not be read" where the sentence does not start with it. The pact's config and a signer's config both print through it. This replaces the inline strip that only the signer branch had.
- Two files beyond those the frame names state where the signers are written, and were rewritten in this phase. `skills/implement/multi-repository.md` now says the orchestrator writes a `Pact signers` key into the pact's repository's `seal/config.json`, not a row into `pact.md`. `skills/config/SKILL.md` gains a `Pact signers` row in its table and in its routing bullet. Both texts are read by an agent at that step, and each stated the removed table as current. That file's wider "row" wording is left for phase 5, whose *Scope* item 7 rewrites it.
- `templates/setup/config.md` *Pact* documents both keys and names the two readers. Its `Pact notify` paragraph is left as it stands, because a text case pins it verbatim and phase 5 rewrites the document.
- `frame/questions.md` Q1 stays on its default, no converter. An old `| Signer |` table or `pact-paths.md` is not detected (design A14). A pact with no `Pact signers` key is refused at exit 2, and a signer only the old map would have found is reported NOT FOUND with the JSON entry to add.

**Cases removed with the code they pinned.** `tests/lib/test_config.py`:

- all of `Test_pact_signers`, both the text cases and the world cases. These were the table, the 0.18.x header, a pact holding both tables, the walker's row refusals and the entry refusals printed after the pact;
- `Test_renamed_header`;
- `Test_gfm_table::test_a_signer_after_a_break_gfm_does_not_honour_is_no_signer`. Its walker half is held by `_Old_config_table::test_a_row_after_a_break_gfm_does_not_honour_is_no_row_of_its_own`.

`tests/skills/test_pact_check.py`:

- `Test_check::test_refuses_a_signer_row_the_table_walk_cannot_read`;
- `::test_refuses_a_map_row_past_the_tables_end_and_reads_the_row_above`;
- `::test_refuses_each_map_line_it_does_not_read_at_exit_2`;
- `::test_refuses_a_pact_listing_its_own_repository_by_the_table_it_holds`, which became `::test_refuses_a_pact_listing_its_own_repository`;
- all of `Test_renamed`.

`tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py`:

- `test_the_old_header_is_read_through_the_second_attempt`, whose second attempt left with `renamed_header`.

The oracle's one-cell `signer` header stays, because it holds the walker over a one-cell table that records may still hold. A comment now says no reader asks for that word. `tests/conftest.py#old_header` left, because nothing uses it.

`Test_path_map`'s accepts case and its entry-refusal case were rewritten from table lines to JSON members. The pact world in `tests/conftest.py` now writes the api's `seal/config.json` with a `Pact signers` key (`#pact_config`, `World.sign`), and writes the map as `.claude/agentic/pact-paths.json` (`World.map`).

**Cases added or rewritten, each seen red.** The changed test files were run against `c58a69a5`'s code with the new conftest in place (executed: `bin/test` over `tests/skills/test_pact_check.py`, `tests/behaviour/test_a_signer_declares_its_pact.py`, `tests/lib/test_config.py` and `tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py` with `-q -p no:xdist`). The run exited 1, with 92 failed and 680 passed. Every case below was among the failures:

- `Test_signer_declaration`'s four cases;
- `Test_path_map`'s rewritten and new cases;
- in `Test_check`, the cases on the own repository, the absent key, the signer entries, the pact config, the map entry and the map that will not parse;
- `tests/behaviour/test_a_signer_declares_its_pact.py#test_the_template_and_the_config_skill_carry_the_pact_signers_key`.

After `fe9e7072`, each guard was broken under the worktree's `bin/seal mutate` against the case that names it (executed; every verdict `red`, exit 0, and the tree clean after each):

| Mutation | The case that went red |
|---|---|
| `signer_declaration` returns no refusal for an absent or empty key | `tests/lib/test_config.py#Test_signer_declaration::test_refuses_a_pact_no_key_signs_naming_the_key`, all five ids |
| `signer_declaration` ignores `config_value`'s refusal | `#Test_signer_declaration::test_refuses_a_key_written_twice_or_holding_no_string` |
| `signer_declaration` reads the `Pact` key | `#Test_signer_declaration::test_refuses_a_pact_no_key_signs_naming_the_key[a Pact key alone]` |
| `remote_list` does not split at `;` | `#Test_signer_declaration::test_accepts_every_signer_the_key_lists_in_its_order` |
| `check` passes over a config that will not parse | `tests/skills/test_pact_check.py#Test_check::test_refuses_a_pact_config_that_will_not_read` |
| `check` prints a signer refusal without `REFUSED` | `#Test_check::test_refuses_a_pact_no_key_signs_naming_the_key`, exit 0 against 2 |
| `check` never refuses the pact's own repository | `#Test_check::test_refuses_a_pact_listing_its_own_repository`, exit 1 against 2 |
| `after_path` returns the sentence whole | `#Test_check::test_refuses_a_pact_config_that_will_not_read` |
| `path_map` folds members through a dict | `#Test_path_map::test_refuses_each_entry_it_does_not_read_and_reads_the_rest[one key three times]` |
| `path_map` takes a top level that is not an object | `#Test_path_map::test_refuses_a_map_that_is_not_one_object_and_reads_none_of_it[an array]` |
| `path_map` returns nothing for text that will not parse | the same case's trailing comma and earlier table, and `#Test_check::test_refuses_a_map_that_will_not_parse_once_at_exit_2` |
| `path_map` reads an empty remote | `#Test_path_map::test_refuses_each_entry_it_does_not_read_and_reads_the_rest[an empty remote]` |
| `path_map` reads an empty path | the same case's `[an empty path]`, and `#Test_check::test_refuses_a_map_entry_it_cannot_use_and_reads_the_one_beside_it` |
| `path_map` reads a path that is not a string | the same case's `[a path that is not a string]` |
| `path_map` reads a remote held by several keys | the same case's `[one remote twice]` and `[one key three times]` |
| `checkout`'s remedy is not written through `json.dumps` | the `Test_checkout` and `Test_check` NOT FOUND cases that pin the remedy |
| `MAP_PARTS` names `pact-paths.md` | every `Test_path_map` case |

One mutant went red by an error, not an assertion. With the guard for a path that is not a string removed, `[a path that is not a string]` fails with a `TypeError` in `os.path.expanduser`. That is the crash the guard exists to prevent, so the case holds the guard. The `TypeError` does not mean the case's sentence was compared.

**Verification.** The plan row's command passed at `fe9e7072` (executed: `bin/test tests/skills/test_pact_check.py tests/behaviour/test_a_signer_declares_its_pact.py tests/lib/test_config.py`, exit 0, 319 passed). The phase boundary set ran as one command at `fe9e7072` (executed, exit 0, 3870 passed and 9 skipped). It held:

- the row's files, and every test file this range changed;
- each test file outside `tests/text` and `tests/behaviour` that names a changed path: `lib/config.py`, `pact_check.py`, `conftest.py`'s pact helpers, the pact and config templates, `skills/config/SKILL.md` and `skills/implement/multi-repository.md`;
- `tests/text tests/behaviour`.

`ruff check` and `ruff format --check` passed over the seven changed Python files (executed). `seal layout --check` and `seal layout --pairs` over the changed test files exited 0 (executed). Reading the range whole after the build found two comments the build left wrong. `a2fbe61c` wraps a comment line of `lib/config.py` that ran to 113 characters. It also rewrites the docstring of `tests/lib/test_config.py`, which still counted seven `seal pact` cases where one stands. The plan row's command passed after it (executed, exit 0, 319 passed).
