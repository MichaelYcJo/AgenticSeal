# Phase 2: 1795406406-code-stands-on-facts-that-no-longer-hold

## What this phase found

**The frame holds for this phase, with three statements the tree does not bear out.** Each was judged against `skills/core/SKILL.md` *The rule a mechanism is kept against*: a change removes in the same commit what stood on the old fact. The phase built to the part that holds and removed what the frame did not name.

- `frame/design.md` *Scope* item 8 says "the `rounds`-file cases of `tests/lib/test_routing.py`" follow. That file held no such case at `89fefd100` or at `24aee6a21`, and no case of `lib/routing.py#rounds_unreadable` at all (executed: `git show 89fefd100:tests/lib/test_routing.py | grep -n -e rounds_unreadable -e NotADirectory` prints nothing). The file shape stood in three callers' cases instead: `tests/github/test_finding_counts.py`, `tests/skills/test_settle.py` and `tests/github/test_release_seal.py#test_an_unlistable_rounds_leaves_rounds_unread_not_zero`. The frame names the first two. The third is not in `frame/plan.md`'s phase 2 *Verified by* cell either. Its case now builds a link in place of the file, because a file no longer reads as unlistable, and it keeps its assertion that the rounds row reads `not read`.
- `frame/design.md` *Scope* item 6 names the `confirms: none` clause of `tests/skills/test_chain_check.py:4916` and `:4932` as the chain-check cases that read `none`. Three more stood there at `89fefd100` (`:615`, `:1293`, `:1326`) and at `24aee6a21` (`:616`, `:1294`, `:1327`): each builds a confirmation block reading `confirms: none` and expects it to pass. `test_accepts_each_confirmation_block_as_a_reference_or_none` loses its `none` block and its name's `_or_none`. `none` joins the refused values of `test_refuses_a_value_it_cannot_read_and_reads_prose_as_nothing`. `test_refuses_a_reference_naming_no_earlier_record_or_finding` builds its first record and its `quiet` record without one.
- `frame/design.md` *Scope* item 7 moves the `plain` and `linked` fixtures of `tests/skills/test_unverified_check.py` under a marked root. It does not name the two cases that need `plain` to have no root, `Test_config_at#test_refuses_to_invent_a_root` and `Test_references_at`, or `tests/skills/test_settle.py#Test_show`, which reads `plain` at its `specs/` path. A module fixture `rootless`, a repository with no root and one overview under `specs/`, now serves the first two cases and S12's walk case. `Test_show` reads `plain` at `seal/threads/<id>/gaps.md`. That edit landed in `a2aa3afe6`, whose message says the commit before it moved the fixture. The fixture moved two commits before it, in `0e8aafb3c`. The message stays as written, since the branch is not rewritten.

**Five texts stood on the removed readings and are not in `frame/design.md` `## Removes`.** Each changed in the commit that removed its reading.

- `skills/code-review/scripts/chain_check.py#round_read` kept a confirmation block's reference only where `.match["round"]` was set, which only `none` left unset. That `elif` is now an `else` that reads the reference from every confirmation block. A block outside every finding is a round block or a confirmation block, because a finding or close block there is refused in the branch above (read: `lib/fields.py#ROUND_RECORD`, the branches of `round_read`).
- `lib/lines.py#visible`'s docstring said keyboards emit "the old mark" followed by U+FE0F. It now says "an emoji".
- `skills/settle/rule-changes.md` *Rule changes* gives `- Nothing` where it gave `- none`, as *Scope* item 6 asks. `tests/skills/test_rule_changes.py#test_a_line_that_opens_like_the_block_is_named_beside_its_refusal` takes `- Nothing` in place of its `- none` entry, so the case and the document's example agree.
- `skills/settle/SKILL.md` *What the dry run shows* said a `trail/rounds` "that is not a directory the dry run can list" is named in place of a count. A file is not a directory, and it now reads as a count of none. The sentence now names a link or a directory the dry run cannot list. The docstring of `skills/settle/scripts/settle.py#judgments` changed the same way.
- `skills/settle/scripts/rule_changes.py`'s `# exempt from root_name:` line over `EARLIER` left with `EARLIER`. *Scope* item 7 names its `old_names` line alone.

**Two texts were kept on purpose.** The message `settle.py` prints for an unlistable `trail/rounds`, "its trail/rounds is not a directory this can list, so no round was counted", stays. Each state it is still printed for, a link and a directory nothing can list, fits those words. The 0.26.0 fixture `LABELLED` of `tests/skills/test_chain_check.py` keeps its `confirms: none` line. That record has no `seal` block, so no reader takes the line as a confirmation, and *Scope*'s *Out* list leaves the fixture to the work only where its expectation needs a change, which it does not.

**S10's case stands in `Test_parse_section`, not in a case of `check_file`.** `frame/design.md` S10 says the row is read through `lib/gaps.py#check_file`. `check_file` reads a file through `check_text`, which reads the section through `parse_section`. The group that already holds the open and closed rows is `Test_parse_section#test_accepts_open_rows_and_the_word_that_closes_one`, so the two U+2705 rows joined it. `Test_closing_word` holds the unit's own answer: `U+2705how it renders` splits at whitespace like any other word.

**S10 to S13 were each seen red against `89fefd100`** (executed). The phase's six changed test files were copied into a `git clone --shared` of the branch checked out at `89fefd100`, under `<scratchpad>/1795406406-code-stands-on-facts-that-no-longer-hold/phase-2/at-89fefd100/`. The new cases were run there with the worktree's interpreter. Eight cases failed, each on the reading it is about:

- S10: the two U+2705 rows of `test_accepts_open_rows_and_the_word_that_closes_one`, each refused with the U+2705 sentence, and `Test_closing_word`'s `U+2705 with no space`.
- S11: `test_items.py`'s `none` case, where `unread_block` named `- none`, and `test_fields.py#test_refuses_confirms_none_at_its_line`, where the block was read.
- S12: `test_config.py#test_no_row_means_every_specs_directory_outside_the_root`, where the answer was `()`, and `Test_overviews#test_refuses_a_specs_directory_on_a_walk_of_a_repository_with_no_root`, where the walk returned the overview.
- S13: `Test_rounds_unreadable#test_refuses_no_rounds_a_listable_directory_and_a_file[a file]`, where the answer was True.

Each was also seen red against the commit before its change. `chain_check.py#round_of`'s `none` entry was seen red there alone. Of the reading units in these cases, only `lib/routing.py#current_branch` and `unverified_check.py#repo_root` differ between `89fefd100` and `24aee6a21`, and neither is under test here.

**`seal mutate` turned each change back, and a case went red each time** (executed, the file restored by the command each time):

- `lib/gaps.py#closing_word` got its U+2705 arm back, and `-k U+2705` went red.
- `#parse_section` got a refusal of a word opening with U+2705, and the open-rows case went red.
- `lib/items.py#NEAR_NOTHING` matched `none|nothing` again, and `unread_block` went red. With its `re.IGNORECASE` dropped, `unread_block`'s `Nothing.` entry went red.
- `lib/fields.py#CONFIRMATION_BLOCK` read `none|round-…` again, and `test_refuses_confirms_none_at_its_line` went red.
- `lib/config.py#reference_roots` answered `()` for an empty HOME, and the rootless walk case went red.
- `lib/routing.py#rounds_unreadable` got its file arm back, and its `a file` case went red.
- `finding_counts.py#NOT_LISTED` named "a file" again, and the case that pins it whole went red.

`rule_changes.py#order` only lost a reading. Its removed case is not replaced, as *Scope* item 7 asks, and nothing new stands there to mutate.

**S14 holds** (executed at `d748e04e2`). `git grep -n -w -e OLD_MARK -e EARLIER -e NotADirectoryError -- lib skills .github` and `git grep -n 'none|' -- lib/items.py lib/fields.py` each print nothing and exit 1.

**The other statements of each rule this phase reworded were searched, as a sample** (executed at `d748e04e2`). The search ran `git grep` on each rule's words over the whole tree outside `seal/threads/`: `U+2705`, `old mark`, `confirms: none`, `` `- none` ``, `none —`, `0.3.x`, `seal/specs`, `session-start move`, `a link, a file`, `flat location` and `migration command`; `EARLIER` and `not a directory` were searched over `lib`, `skills`, `.github`, `docs`, `agents` and `templates`. Outside the phase's own new cases it finds `LABELLED`'s line, kept as above, and `tests/censuses.py:1161`, the `old_names` census's 0.3.x comment, which *Scope* item 9 removes in phase 5. Its other four matches are about other things: the release note's old marker in `settle.py:464` and `tests/skills/test_settle.py:2756`, the words "holds none —" in `tests/behaviour/test_one_heading_rule_holds_to_commonmark.py:23`, and the emoji census's "old marks" in `tests/text/test_the_record_is_written_in_words.py:25`. `docs/` holds none of these readings, so no operation of `## Rule changes` follows from this phase. What the sample did not reach is a statement of these rules in other words.

**The next phase needs one thing from this one.** `tests/skills/test_unverified_check.py` now holds a `rootless` fixture beside `unwritten` and `sealed`. Phase 3 removes `Test_absent_root` and the G6 cases. S2's case, a tree with no root exiting 2, can build its tree from `rootless` or from `tmp_path`.
