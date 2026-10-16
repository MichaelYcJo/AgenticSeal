# 1791940762-the-record-of-truth-is-tests-not-coordinates — phase 4

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 9c9b99fb |
| Ran by | smith on Opus 5.5 |

## What this phase was asked

The checker cut to its kernel, as `plan.md` phase 4 states it: cut
`evidence_check.py` to the coordinate kernel its importers use, at its own
path, so no importer moves; delete `correction_check.py`, `fold_ledger.py`,
`hooks/evidence-advisor.py`, `hooks/ledger-migrate.py`, `root-migrate.py`'s
two mapping rows, the `bin/` wrappers and the ledger test modules, keeping the
kernel cases in one module (W2). Phase 3's open items 3 and 4: `claim_lines`
leaves with the records arm, with its six-readers sentence in
`docs/the-record-layout.md` and its row in
`test_whether_a_line_is_live_is_asked_by_what_the_line_does.py`. Lower
`suite-seconds` and `slow-file:*` from a durations union, or record the
numbers for the pull request's run. `enforced-unresolved` at 0 at every
commit, no ledger rows, census and registry modules after every commit.

## What this phase found

**The kernel is 545 lines of 7,272.** Read off every importer's attribute
uses (M2, executed with an `ast` walk over each file that loads the checker):
`fold_check.py` takes `named_unit`; `rider_check.py` `ANCHOR_LOCATOR`,
`ANCHOR_HASH`, `resolve_unit`, `content_hash`, `gfm_lines`, `py_spans`;
`pact_check.py` `PACT_ANCHOR_RE`, `HEADING_SEP`, `heading_path`,
`heading_level`, `markdown_lines`, `unescape`, `unquoted`, `content_hash`,
`gfm_lines`; `chain_check.py` `PACT_ANCHOR_RE`, `unquoted`;
`tests/reader_registry.py` `py_spans`, `content_hash`, `gfm_lines`. What
those call stays with them. `ANCHOR_RE` and `ANCHOR_PATH` went although the
frame lists them: their two remaining readers were `correction_check.py` and
`root-migrate.py#repoint`, both deleted here. So did `resolve` (its callers
were cases), the minor-level readers, `blank_pact_anchors` and every vendored
copy: no command runs the file any more, so nothing runs it alone in a user's
`tools/`, and `gfm_lines`, `heading_level` and the fence rule are now asked
of `unverified_check.py` rather than copied. Units whose docstring or body
changed declare their read class; 192 census lines left with their units.

**W2, the kernel cases**, 51 in
`tests/test_a_unit_is_bounded_where_a_parser_decides.py`, each unit seen red
by one `mutation-check` (executed; 21 kernel mutations and the root-migrate
one below, all red):

| Unit | Mutation | Case that went red |
|---|---|---|
| `parsed_spans` | span starts at the `def`, not the decorator | `test_a_decorator_is_part_of_the_span` |
| `parsed_spans` | memo removed | `test_the_units_of_one_text_cost_one_parse` |
| `parsed_spans` | `{}` for a SyntaxError | `test_a_file_that_will_not_parse_yields_no_symbols` |
| `py_spans` | hands back the stored dict | `test_changing_the_returned_spans_does_not_reach_the_next_caller` |
| `normalise` | trailing whitespace kept | `test_the_hash_ignores_trailing_whitespace_and_blank_lines` |
| `normalise` | indentation stripped | `test_the_hash_does_not_ignore_indentation` |
| `heading_path` | any heading ends a section | `test_a_markdown_heading_owns_its_section` |
| `heading_path` | the parent stops narrowing | `test_a_repeated_heading_is_disambiguated_by_its_parent` |
| `text_regions` | no paragraph walk | `test_a_text_anchor_owns_its_contiguous_block` |
| `text_regions` | heading read on the raw lines | `test_text_regions_reads_a_heading_on_the_lines_it_is_shown` |
| `unescape` | `\|` left escaped | `test_an_escaped_pipe_matches_a_real_one` |
| `quoted_lines` | no fence ever closes | `test_a_heading_quoted_in_a_closed_fence_opens_no_section` |
| `heading_level` | any `#` line is a heading | `test_only_a_real_heading_opens_a_section` |
| `bounding_rule` | `.md` bounded by nothing | `test_a_bare_symbol_in_markdown_is_refused_and_names_the_heading_path` |
| `unbounded` | the remedy reworded | `test_a_bare_symbol_outside_the_two_parsers_is_refused_with_the_shape` |
| `resolve_unit` | the refusal dropped | `test_a_syntax_error_is_refused_rather_than_read_by_the_text_rule` |
| `resolve_unit` | a quoted line resolves nowhere | `test_a_quoted_line_resolves_in_any_file` |
| `unit_kinds` | hands back the stored dict | `test_the_resolver_hands_each_caller_its_own_answer` |
| `named_unit` | `A.b` accepted as a part | `test_the_resolver_hands_each_caller_its_own_answer` |
| `PACT_ANCHOR_RE` | look-behind removed | `test_a_word_ending_in_pact_is_not_a_pact_anchor` |
| `gfm_lines` | `str.splitlines` | `test_every_reader_ends_a_line_where_gfm_does.py::test_every_copy_of_the_splitter_is_the_readers` |

The cases came from `test_a_row_points_by_content.py` (21),
`test_a_unit_the_extractor_cannot_bound_is_refused.py` (7, the S3 one over
22 suffixes), `test_a_ledger_row_is_held_by_its_test.py` (1) and
`test_a_pact_anchor_is_no_coordinate_of_the_signer.py` (1). The parse-once
case was rewritten to count parses over five `resolve_unit` calls, since the
ledger walk it measured is gone. `test_the_ledger_cases_hold_under_a_latin_1_locale.py`
held none: its four cases ran released-row cases.

**What left.** 14 test modules, 16,342 lines, 1,214 priced cases, 407.1
Windows seconds, and 47 cases cut from 15 kept modules, 19.1 seconds. Code:
9,747 lines out of `skills/`, `.github/`, `hooks/` and `bin/`, 245 in. With
phase 2's modules, `.test_durations` lost 796.5 Windows seconds; it is
7,065.2 now and `suite-seconds` is 9185 (1.3 times it). The two deleted
`slow-file` rows went; no other listed file moved. `budget_check.py` exit 0
on the tree and against `origin/release/v0.22.0`; `fold-check` exit 0.

**The durations file was not refreshed from a run, and is one case from
its limit.** No run is available without a push. The deletion shrank the
collection, so the share of unpriced cases rose past `STALE_SHARE` (5.4 %,
executed) with no new case unpriced. The 54 moved and renamed cases carry
their old Windows prices to their new ids, which is the price the file
would hold for an unchanged body; that brings the share to 4.97 %, 610 of
12,270, and `test_the_durations_file_prices_the_suite` passes (executed).
One new unpriced case, `test_the_moved_file_is_its_old_bytes_and_nothing_is_rewritten`,
is in it. The refresh is owed at the pull request's run.

**The pact's change records lost their writer, which the frame did not
see.** `record_pact_changes` ran inside `--reverify`, on ledger rows whose
code moved under a pact clause; with `--reverify` gone, nothing writes
`seal/pact-changes/`. `test_a_signer_records_a_pact_change.py` went whole;
`docs/the-pact.md` lost its §*A signer records a pact change* (three
statements), the vendored-copy half of its local-mode statement, the
record-first statement (`nothing`, so its `unenforced` count is unchanged:
the local-mode half took `nothing — no pact case builds two clones of one
repository`) and the ledger's part of the anchor statement, which now names
`test_pact_check.py::test_s12_a_signer_citing_the_current_clause_is_clean`.
`pact_check.py` still reads records and pact reviews, and still globs a
signer's `seal/ledger*.md` for anchors; `test_a_pact_review_takes_a_pact_change.py`
now writes each record in the writer's shape instead of running it (23
passed, executed). The `hooks/config.py` copies the test held equal to the
checker's (`PACT_WORD`, `HTML_CELL`, `UNDER_A_HEADER`, `names_a_pact`) are
the one copy now, and the cases comparing them went.

**`root-migrate.py` lost its re-point step with its mapping rows.** Step 6
read the ledgers through `ANCHOR_RE`; a 0.3.x `.specseal/map.md` now moves
to `seal/map.md` as any other entry, and the hook's line says only what
moved. Its rider was anchored on `PREFIXES`, which went; it is re-anchored
on `moves` and re-stamped after a re-read. The README's by-hand block in
both editions follows (`git mv .specseal/* seal/` replaces the two map lines
and the `--reverify` line), because `test_the_readmes_by_hand_sequence_yields_the_hooks_tracked_set`
runs it; the rest of the READMEs is phase 5's. The new case pinning that the
moved map keeps its bytes was red against a message naming re-pointed rows.

**Printed text that changed** (§14): `seal import`'s closing line no longer
names `evidence-check .`, pinned by
`test_the_import_asks_nothing_and_says_it_overwrote_nothing`; the
root-migrate line, pinned above.

**Phase 3's items 3 and 4.** `claim_lines` left with the checker; the
liveness statement names five readers and its HOLDS bullet the kernel's
`quoted_lines` and the rider check's; the table lost its row.

**`seal/follow-up.md`**: the `--reverify` re-stamp row, the seven heading-path
rows row and the subagent-median row named a ledger that is gone and were
deleted; the floor row lost `fold_ledger.py` and `root-migrate.py` (its
`zip(strict=True)` was in `repoint`) and counts three scripts.

**Left for phase 5, by S9's grep or by name:** prose in code naming the
ledger as an analogy, in units still on the census, where an edit would
re-hash a unit for a sentence: `rider_check.py#reverify` and `#migrate`,
`chain_check.py#fix_range`, `pact_check.py#shown`,
`hooks/config.py#pact_declaration`, and `round_record.py#RECORD_COMMENT_NEVER_CLOSED`,
a printed message that still lists `evidence-check` among a record's readers.
`skills/evidence-check/SKILL.md`, `skills/evidence-ci/`, `templates/ledger.md`
and `templates/evidence-check.yml` stand and describe a command that is gone.
