# Implementation Plan: a reader declares its input class (#835)

<!-- seal/specs/1791384152-a-reader-declares-its-input-class/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. Reframed 2026-10-12 before the build: four phases, the first of
them the measurement, the population rule inverted (spec.md §*How a reader is
found*), the seams re-based on the tree after six siblings landed. Re-based
again the same day against the tree every sibling left (`release/v0.21.0` at
c38f97d7, merged here as 4ba84e19): every count, line number and seam below
is read at 4ba84e19, and the seams describe landed code. -->

Approved 2026-10-12 by the repository owner, when `smith` was spawned.

## Summary

Four phases, landed in order, each one commit or a few. Phase 1 is the
measurement: the walker, the census writer, and the counts read at the tree
the landed siblings leave, recorded before any rule is enforced. Phase 2 is
the registry check over that walker and census, and it changes no reader.
Phase 3 is the `## Removes` section: the template, the records arm that
reads it, the config row, and the per-phase table it retires. Phase 4 is the
document that states both rules and the fragments. Every other 0.21.0
sibling has squashed into `release/v0.21.0` (c38f97d7) and that branch is
merged into this one (4ba84e19), so the item builds **now, and before
#834's build**, for the reasons under *Operational impact*.

## Technical context

Existing code this builds on, as read on 2026-10-12 at 4ba84e19 (this
branch's merge of `release/v0.21.0` at c38f97d7, which holds all ten
siblings: #858, #864, #837, #867, #869, #860, #836, #868, #870 and #866).
`evidence_check.py` is 6,698 lines there, so every line number is a reading
of that moment:

- `skills/evidence-check/scripts/evidence_check.py#py_spans` (:464) —
  `{qualified name: [(start, end)]}` for defs, classes and constants,
  memoised per text; `#content_hash` (:460) — the eight-hex hash over a
  span. The census hashes with these two, imported by path the way
  `tests/test_a_document_has_room_for_the_next_fold.py#_load` loads
  `fold_check.py`. Measured by the framer at 4ba84e19: a top-level unit is
  keyed by its bare name, a method `Class.method`, a nested function
  `outer.inner`, a constant by its name (`questions.md` Q2).
- `evidence_check.py#claim_lines` (:5559) — which record lines are claims
  (fences and HTML comments are not); `#file_claims` (:5994) — the name
  half (`stated_names` :5690, `stated_coordinates` :5705,
  `coordinate_misses` :5772) and the stamp half over one record;
  `#check_records` (:6062) — every live work item's records plus
  `seal/follow-up.md`; `#coordinate_misses` — a `path#name` whose path
  resolves is read by token of that file, which is why a removed unit named
  in a live record is a miss today. `#RECORD_COORD_RE` (:5496) reads
  `` `path#name` `` with `ANCHOR_NAME` and no quoted locator;
  `#heading_rule` (:559) is the one heading reader #867 left.
- `evidence_check.py#bounding_rule` (:696; `AST_SUFFIXES` and
  `HEADING_SUFFIXES` :692–693), `#unbounded` (:717), `#Resolution` (:748)
  and `#resolve_unit` (:783) — #870's landed shape. `resolve_unit` returns a
  `Resolution` whose `places` is `[(start, end)]` and whose `refused` is
  `None` or the sentence `unbounded` writes; a bare symbol in a file outside
  `.py`, `.pyi` and `.md` comes back with no places and the quoted-line
  remedy. S5 reads `refused` and refuses the row; the `BROKEN` word is
  `judge`'s, not the resolver's. The `generic_units` function and the brace
  lexer are gone, and nothing here brings a bounding rule back for any other
  suffix.
- `evidence_check.py#config_rule` (:4366) — `(config_text, config_rows,
  value_of)` from `hooks/config.py`, or the vendored trio where no `hooks/`
  sits beside the checker; `#frozen_from` (:4380) — the `Ledger frozen
  from` reader (`FROZEN_ROW` :4273), which reads through it. **#867 has
  landed**, so `Removes from` reads through `config_rule()` in
  `frozen_from`'s shape: phase 3 generalises `frozen_from` into
  `cutoff_row(root, item)` and has `frozen_from` call it, one reader for
  both rows (`questions.md` Q5, closed by this reading).
  `tests/test_a_released_row_is_read_again_in_a_fragment.py` holds the
  freeze reader's cases and is where S6's planted root sits beside them.
- `evidence_check.py#named_unit` (:2283), `#suite_record` (:2352),
  `#observed` (:2412), `#held_by_tests` (:2527), `SUITE_RECORD_OPTION`
  (:2321) and `broad_gate.py`'s `EVIDENCE_RECORD` (:232) — #836's landed
  test-row readers. Phase 3 touches none of them: a test row's token is
  `path::name` and the `## Removes` cell is `path#unit`, so a node id in a
  Removes row is not a coordinate and S5 refuses it. A test row has no hash,
  which is why the backfill drift count below excludes it.
- `tests/test_a_record_states_what_the_tree_has.py` — the module that
  drives `check_records`; S1–S7's planted roots go beside its cases.
- `tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py`
  — `tracked_python` (:540) walks `git ls-files '*.py'` through
  `conftest.git_listing`; `OPENERS` (:246) as its K1; `judge` (:393)
  resolving a module call through the file's imports;
  `test_the_failure_names_the_site_and_the_repair` (:634);
  `test_the_walk_reaches_a_root_nobody_listed` (:1162);
  `test_a_local_function_named_run_is_not_a_subprocess_call` (:1098). The
  registry walker copies the file walk, the import resolution and the
  failure shape; attribute-name matching for methods is the encoding test's
  `Path.open` approach, with the same honesty about what a static walk
  cannot follow.
- `tests/test_every_reader_ends_a_line_where_gfm_does.py#splitlines_calls`
  (:720) and `#_walk` (:738) — a census of calls keyed `(path, unit)`.
  The registry walker is this walk with every top-level unit collected and
  K1 asked only of a unit that declares `nothing`.
- `tests/conftest.py#git_listing`, `#on_disk`, `#decline_if_shrunken` —
  the listing splits on whitespace (inventory part 6 row 6), so the walker
  reads `ls-files -z` itself if `git_listing` cannot be asked for `-z`;
  either way the sweep declines when a listed path is off disk, which
  `tests/test_a_shrunken_corpus_declines_to_judge.py` requires of every
  sweep.
- `skills/verify/scripts/unverified_check.py#parse_section` and
  `#check_text` — the shape a machine-read markdown section has here: a
  fixed header, `none — <why>` as the alternative, the placeholder refused.
  The `## Removes` reader in the records arm copies the shape, not the code.
- `templates/sdd-spec.md` (the mark is the last line and
  `tests/test_waiver_decided_at_start.py` and
  `tests/test_the_chain_goes_back_to_its_framer.py` hold it there);
  `templates/sdd-phase.md` §*What this phase removes* (:79) and
  `tests/test_a_phase_hands_the_next_one_a_record.py` (:54, :236, :277);
  `agents/framer.md`'s writes table and report list.
- `templates/config.md` §*The ledger freeze* — the row table shape
  (`Row | Value | Absent`) a new config row is documented in;
  `seal/config.md` (six rows at 4ba84e19 — `Mode`, `Broad gate`, `Fold
  shape from`, `Document line ceiling`, `Over the ceiling`, `Ledger frozen
  from | 1790993141`).
- `docs/the-record-layout.md` §*docs/* — the table a new document takes a
  row in.
- `hooks/git/post-commit.py`, `pre-commit.py`, `reference-transaction.py` —
  each a `main` with no docstring under a module docstring, in the
  population under (b); under (a) they were in too, by their calls. #868
  weighed reading a switch through `reference-transaction` and rejected it
  (its `spec.md` §*Out*: the hook sees the switch after the tree moved on
  2.50.1, or not at all on 2.34–2.43), so the file is unchanged at 4ba84e19
  and its `main` is on the census like the other two.

**Constraints.** The check calls git only to list files (the encoding
test's precedent); the records arm calls git for nothing
(`docs/the-evidence-ledger.md`). Every text file is opened with
`encoding="utf-8"`. Each failure text a person reads is pinned in the
commit that writes it (§14). A case is seen red before it is planted
(§15). K1 is a list to extend, never an exemption list to grow, and it
never selects who declares.

**Failure scenario of the chosen approach, six months on.** Three, stated
so nobody discovers them. First, the census never shrinks below the units
nobody touches: that is allowed, it costs nothing, and the `grep` list of
`guess` is then the touched half of the tree — `docs/the-reader-registry.md`
says the list is complete only when the file is gone. Second, `nothing`
becomes the line people write to pass: K1 refuses the ones it can see, and
the warden reads the rest; if `nothing` lines outgrow the classes, the
owner's lever is the module-body rule's twin for units — require a class
word on any unit K1 selects — which is one Alternatives row below, not
built. Third, a `Reads:` line goes stale when a reader is redesigned and the
line is not moved: nothing re-reads a class, as nothing re-reads an
`Enforced by:` target; the warden reads the diff's lines, and the document
says so.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| (a) The population found by a list K1 of reading calls, the frame of 2026-10-08 | an unlisted call exempts a unit silently; the enumeration-over-an-open-domain shape that #868, #860, #836 and #870 each took three rounds to learn, kept as the population rule of the mechanism meant to end it | rejected at the owner's review; K1 is kept as a contradiction check on `nothing` only |
| (c) Readers found by what a run observed — `sys.addaudithook` during the suite, attributed by stack | coverage-bounded, so the quiet failure moves from the call list to the suite; hooks run as `python3 <script>` children that need the hook injected; a regex over a string is no audit event, so the `guess` class is invisible to it | rejected as the population rule; a later item may add it as a cross-check on `nothing` lines (what a run saw a unit open against what it declared); this frame files nothing |
| (b) with module bodies inverted too — every module docstring declares for its body | 73 more lines, one per non-test module (253 tracked `.py` less 180 `tests/test_*.py` at 4ba84e19), nearly all `nothing`, for two modules whose bodies K1 selects; a module docstring in `hooks/` is already a page of policy | not taken; module bodies stay the one corner K1 selects, counted by phase 1 and stated as the limit. One row to flip if the count grows |
| (b) with a class word required on every unit K1 selects (no `nothing` there) | K1 then decides something about the population again, if only the word; and a unit that calls `exists` to write is honestly `nothing` | not taken; the contradiction check is the whole of K1's say. The owner's lever if `nothing` is abused |
| Exclude the `Reads:` line from the ledger hash so a backfill drifts no row | the hasher is `py_spans` + `content_hash`, the ledger's premise; changing what a hash covers is the question the owner's review opens for 0.22.0, not this item's | rejected; the cost is stated and handed to #834's timing |
| A table under `docs/`, the ticket's wording | the ceiling, the shared file, the second copy, the `Class` parse | rejected; the owner answered Q1 (a) on 2026-10-08 |
| A table under `docs/readers/`, outside the ceiling's top level | the same shared file and the same second copy | rejected |
| A per-work-item fragment `seal/readers/<id>.md`, folded at release | a second ledger with a fold of its own | rejected |
| Declaration by decorator | needs a module every hook imports; hooks are standalone entry points, and a docstring line needs nothing at runtime | rejected |
| Test modules' helpers in the population | 1,683 more units (and 17 classes), 618 of them calling a K1 primitive, at 4ba84e19; their class is read at the assertion they serve | not now; one exclusion to delete, weighed with the census's size after #834's build |
| Rule 2 as a ratchet on `Reads: guess` | the count is unknown until the census empties; a ratchet needs an exemption list | deferred to the owner with the count |
| Rule 2 read from the pull request body or from prose | the guess class | rejected |
| Rule 2 in `unverified-check --baseline` | a second reader of `spec.md` beside the records arm, which would still refuse the removed names; a hygiene step name copied into `broad_gate.py` | rejected; the records arm reads it, and the warden opens the base |
| Keep the per-phase removal table beside `## Removes` | two records of one fact | rejected; the table retires |
| The census inside the test module as a constant | about 1,587 lines in a module; #834's script rewrites it | rejected for a `.txt` beside the test |
| A `Reads:` line read from a sibling's `spec.md` class table instead of the docstring | #866's and #870's specs state a class per unit they added, in prose tables; reading them would make the registry a reader of a person's table, the `guess` class, and a second home for the fact | rejected; the tables are #834's backfill source, and the units sit on the census until a docstring line is written |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **The measurement, at the build's own tree.** The walker as a module the test imports (`population(root)`: every top-level unit of every tracked `.py` outside `tests/test_*.py`; `k1_calls(unit)`: the two families with import resolution; `module_body_calls(path)`); the census writer that emits `tests/undeclared_readers.txt` from the walker; and `phases/phase-1.md` recording, with the SHA read: units per root, units K1 selects, units with no docstring, module bodies K1 selects, non-test defs inside `tests/test_*.py` and how many K1 selects, ledger anchors on population units in the released files and in the live fragments (distinct units and occurrences, the backfill's drift cost), and which of the 39 sibling-added units (`§Seams`) are on the census. The frame's reading at 4ba84e19 is in `spec.md` §*The population*; a number that differs there is reported as a difference, with both values. No reader's body changes | the walker's cases R5 and R7 as planted roots; the census file's grammar R6; `uvx ruff check` on the module; the record's numbers reproduced by the one command `spec.md` §*The population* gives for units and docstrings, and by the walker for K1 | 248c33b2 |
| 2 | `tests/test_a_reader_declares_its_input_class.py`: the `Reads:` grammar reader, the census reader, the contradiction check, R1–R4, R8, R9, R10; `tests/undeclared_readers.txt` committed from phase 1's walker at this phase's tree; `py_spans` and `content_hash` imported from `evidence_check.py`. No reader's body changes | the module's cases; R8 seen red twice — one census line deleted, one census hash altered — and the texts of R1–R4, R7, R10 pinned (§14, §15) | 33d0b0ca |
| 3 | `templates/sdd-spec.md` §*Removes* above the mark; `agents/framer.md`'s writes table and report list name it; `evidence_check.py`: `claim_lines`/`file_claims` read the `## Removes` section's rows as absence claims (`STANDING` where `resolve_unit(...).places` is non-empty, the names on those lines skipped by the name half, a non-coordinate cell, a `::` node id and a bare symbol `resolve_unit` answers with `refused` set all refused naming the row), `cutoff_row(root, item)` generalised from `frozen_from` and both rows read through `config_rule()`, presence required at or above the cutoff; `templates/config.md` documents the row; `seal/config.md` gets `Removes from | <epoch at the write>`; `templates/sdd-phase.md` §*What this phase removes* removed with its pins in `tests/test_a_phase_hands_the_next_one_a_record.py` and every carrier `grep -rn "What this phase removes"` finds; this item's own `## Removes` row goes from `STANDING` to clean in the same phase | the arm's cases S1–S5 and S7 as planted roots beside `tests/test_a_record_states_what_the_tree_has.py`'s cases, S6 beside `tests/test_a_released_row_is_read_again_in_a_fragment.py`'s; S8's pins; `bin/evidence-check .` exit 0 at the phase's last commit and exit 1 naming `STANDING` at a probe commit before the template section is removed (S9) | |
| 4 | `docs/the-reader-registry.md` (the four classes, the grammar, the population rule and K1's demoted role, the three ways weighed and the verdict, the census, module bodies, `## Removes`, the six limits, the counts at landing as phase 1 read them); `CONTRIBUTING.md` §*What a change to a gate must carry* two bullets; `docs/the-record-layout.md` §*docs/* row; `seal/specs/<id>/changelog.md`; `seal/ledger/1791384152-a-reader-declares-its-input-class.md` rows per scenario | `bin/fold-check` exit 0; D1–D2; the eight suite-wide guard modules the run's handoff names; `tests/test_a_folded_statement_names_what_enforces_it.py`; `tests/test_no_passage_is_pasted_into_a_second_file.py` unchanged | |

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true, which is the failure the evidence ledger exists to prevent.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past one
— someone can open it — which is the same trick that lets a round record live
beside the contract rather than in tool state.

What a phase discovers while it is being built, and needs the next phase to
know, goes to `seal/specs/<work-item-id>/phases/phase-N.md`, from
`templates/sdd-phase.md`, when the phase closes. Phase 3 of this item changes
that template; a phase record written after it carries no removal table, and
the records of phases 1 and 2, written before, carry one with a `none` row.

## Seams with the other 0.21.0 chains

Every 0.21.0 sibling is in this branch's tree: `origin/release/v0.21.0` at
c38f97d7, merged as 4ba84e19. The table names what each one added to or
removed from the population, as the framer's probe read the two trees
62c27416 and 4ba84e19 (39 top-level units added, 14 removed, two test
modules added, no file removed), and what this build reuses. A removed unit
is written as `file`'s `name` on purpose: it is not in the tree, and the
records arm reads a `path#name` as a claim that it is. No shipped unit
carries a `Reads:` line at 4ba84e19, so every added unit below is on the
census at landing.

| Sibling | Landed | Population units added (+) and removed (−) | What this build does with it |
|---|---|---|---|
| #867 (`hooks/config.py`; one coordinate and one heading reader) | 56ade5c8, in 62c27416 already | `hooks/config.py` whole, `evidence_check.py#config_rule`, the `vendored_config_*` trio, `heading_rule`, `heading_level`, `markdown_lines` | `Removes from` reads through `config_rule()`; the Removes cell through `RECORD_COORD_RE`, the heading through `heading_rule` |
| #869, #852, #853 (the recorder) | b6c81a83, in 62c27416 | `skills/verify/scripts/pytest_record/specseal_pytest_record.py` (its module body reads `os.environ` at :139–140, R10's real case with a docstring), `broad_gate.py`'s `record_path` and `records_dir`, `release_seal.py`'s `SUITE_RECORDS` reader | not touched |
| #860, #805 · #858 · #864 · #837 | ad447367 · 9b644676 · d712a632 · 279a580b, in 62c27416 | `round_record.py#own_commits` and the `-z` listings; no guessing reader (#834's review) | not touched |
| #836 (a ledger row's claim is its test) | 23f5977c | + `evidence_check.py`: `named_unit`, `node_tokens`, `node_finding`, `statement_at`, `unit_kinds`, `_parsed_kinds`, `record_name`, `suite_record`, `observed`, `held_by_tests`, `existence_line`; `fold_check.py#evidence`; options `--suite-record`/`--suite-key` and their pass-through in `broad_gate.py#main`; `tests/test_a_ledger_row_is_held_by_its_test.py` (excluded as a test module); `docs/the-evidence-ledger.md` §*A claim held by a test*; `templates/ledger.md` §*A row held by a test*. − none | phase 3 edits `claim_lines`, `file_claims`, `frozen_from` and none of these; a `::` token in a Removes cell is refused (S5); a test row has no hash and is outside the drift count |
| #870, #848 (a unit the extractor cannot bound) | be464c06 | + `evidence_check.py#Resolution`, `#bounding_rule`, `#unbounded`, `AST_SUFFIXES`, `HEADING_SUFFIXES`; `tests/test_a_unit_the_extractor_cannot_bound_is_refused.py` (a test module). − `evidence_check.py`'s `generic_units` and, below the top level, the brace lexer's forms and `Resolution`'s resurrection flag | S5 reads `resolve_unit(...).refused`; the registry walker is `ast` over `.py` only and bounds nothing else, so no lexer returns through it |
| #866 (a round-record cell has one reader) | c38f97d7 | + `chain_check.py`: `deferred_home`, `issue_of`, `deferred_parts`, `record_facts`, `facts_at_head`, `floor_walks`, `cut_runs`, `gate_before_review`, `close_prefixes`, `fields`, `doubled_fields`, `pass_boxes`, `pull_request_from_gh`, `sealing_excuses`, `event_payload_present`; `tests/conftest.py#gh_answers`, `#_write_gh_stub` (the conftest's `gh` stub answers *no pull request* for every case). − `chain_check.py`'s `run_reopened` and `wrote_fixes`; `round_record.py`'s `location_units` and `pull_request_is_ready`; `broad_gate.py`'s `deferred_home` and `draft_env` | nothing shared; its `spec.md` §*Data & interfaces* class table (owned / observed per unit, checked at c71b6fbb) is #834's backfill source for those units, by its own `questions.md` W3 |
| #868, #856 (the hooks read the session, the waiver and a creation one way) | 9afc90aa | + `hooks/gate.py#lines`, `hooks/hooksession.py#is_claude`, `#claude_pid`, `hooks/tokens.py#_read_words`, `hooks/worktree_consent.py#place`, `#segment_cwd`, `#split_with_separators`. − `hooks/commit-review-gate.py`'s `git` and `_reads_marker`; `hooks/session-lease.py`'s `owner_pid`; `hooks/worktree-guard.py`'s `_tokenize_with_separators`, `_without_bodies`, `judgeable`, `segment_cwd`, and below the top level its brace reader (`_BRACE`, `_unquoted_brace`, `_finding_trees`), a brace expansion being a named limit filed as #886. `hooks/git/reference-transaction.py` is unchanged: the switch arm was weighed and rejected (its `spec.md` §*Out*) | nothing shared; K1 reads no shell text and knows no brace, so nothing the guard deleted returns through the registry |
| #834 (the inventory's build) | not started | every reader file's docstrings; `tests/undeclared_readers.txt` | builds after this item: it writes `Reads:` lines from the inventory's rows and the siblings' class tables, decides how much of the unrowed population to backfill against the drift cost phase 1 measured, and says in its own spec where `inventory/` ends |

**What the plan does not rebuild**, checked against the three deletions
above: no reader of a brace or of shell text (K1 is `ast` names and
attribute names; a `sh -c` string is limit 3 in `spec.md`); no language
lexer (the walker and the Removes judgment read `.py` by `ast`, `.md` by
`heading_rule`, and refuse the rest through `bounding_rule`); and no static
prediction of what pytest would collect (the registry excludes
`tests/test_*.py` by file name and reads no test body; a test row's hold is
`held_by_tests`'s, from the recorder).

## Operational impact

- **No migration, one new config row.** `Removes from` in `seal/config.md`,
  set at the build to the epoch second of the write. A consuming repository
  without the row has presence unchecked; one with a `## Removes` section in
  a live `spec.md` has its rows read as absence claims from this release on,
  which the changelog fragment says.
- **The order of landing was the cost control, and it has been kept.**
  Every sibling has squashed into `release/v0.21.0` (c38f97d7) and that
  branch is merged into this one (4ba84e19, a merge and never a rebase);
  this item builds now and #834's build follows. Had it built earlier, every
  sibling that edits a population unit would have had to declare it and
  delete its census line on a branch cut before the file existed, and four
  branches deleting neighbouring lines of one sorted 1,587-line file would
  have conflicted at the squash. Later than #834 is impossible, because the
  backfill shrinks a census that has to exist. What 0.21.0 therefore does
  not get: its own reader changes declared at the time they were made. The
  run's handoff asked each frame to state its readers' classes in its
  `spec.md`, so #834's backfill can read them there; #866 and #870 did, in
  their `spec.md` tables, and #868's spec names its readers' classes in
  prose.
- **No new dependency, no new workflow step, no `CLAUDE.md` row.** The
  failure text of each check is the instruction, pinned; the always-on
  surface does not grow (`CONTRIBUTING.md` §*Proposing a new gate or skill*).
- **Prompt budget.** Zero. Neither check asks anything; each refuses with the
  repair in the message, at the commit (the advisor), in CI and in the broad
  gate.
- **Failure direction.** Both checks block more, never allow more: an
  undeclared, mis-declared or changed unit stops the branch at the suite; a
  named removal still standing, or a removal row the ledger cannot resolve,
  stops it at `--strict`. A wrong deny costs one docstring line or one row;
  a wrong allow — a false `nothing` K1 cannot see, a typo'd Python
  coordinate passing as gone — is the warden's to catch, and the document
  says so (`spec.md` §*What neither check can read*).
- **Cost this item itself adds to the ledger.** Phases 1 and 2 change no
  reader body and drift no row. Phase 3 edits `claim_lines`, `file_claims`,
  `frozen_from` and the templates, and re-reads the rows those units carry
  with `--reverify --into`. The backfill's drift (2,392 anchor occurrences
  on 943 units in the released files, and 691 on 247 units in the live
  fragments, at 4ba84e19) is #834's, and phase 1 hands it the number read
  at the tree it will build on.
- **Platform.** The walker is `ast` over UTF-8 text with paths spelled `/`
  as the ledger spells them; nothing it reads differs by platform.
