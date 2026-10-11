# Implementation Plan: a reader declares its input class (#835)

<!-- seal/specs/1791384152-a-reader-declares-its-input-class/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. Reframed 2026-10-12 before the build: four phases, the first of
them the measurement, the population rule inverted (spec.md §*How a reader is
found*), the seams re-based on the tree after six siblings landed. -->

Approved <date> by <who>, when `smith` was spawned.

## Summary

Four phases, landed in order, each one commit or a few. Phase 1 is the
measurement: the walker, the census writer, and the counts read at the tree
the landed siblings leave, recorded before any rule is enforced. Phase 2 is
the registry check over that walker and census, and it changes no reader.
Phase 3 is the `## Removes` section: the template, the records arm that
reads it, the config row, and the per-phase table it retires. Phase 4 is the
document that states both rules and the fragments. The whole item builds
**after #836, #866, #870 and #868 have squashed into `release/v0.21.0` and
that branch is merged into this one, and before #834's build**, for the
reasons under *Operational impact*.

## Technical context

Existing code this builds on, as read on 2026-10-12 at 81037623 (this
branch's merge of `release/v0.21.0` at ad447367, which holds #858, #864,
#837, #867, #869 and #860):

- `skills/evidence-check/scripts/evidence_check.py#py_spans` (:454) —
  `{qualified name: [(start, end)]}` for defs, classes and constants,
  memoised per text; `#content_hash` (:450) — the eight-hex hash over a
  span. The census hashes with these two, imported by path the way
  `tests/test_a_document_has_room_for_the_next_fold.py#_load` loads
  `fold_check.py`.
- `evidence_check.py#claim_lines` (:5177) — which record lines are claims
  (fences and HTML comments are not); `#file_claims` (:5612) — the name
  half (`stated_names` :5308, `stated_coordinates` :5323,
  `coordinate_misses` :5390) and the stamp half over one record;
  `#check_records` (:5680) — every live work item's records plus
  `seal/follow-up.md`; `#coordinate_misses` — a `path#name` whose path
  resolves is read by token of that file, which is why a removed unit named
  in a live record is a miss today. `#resolve_unit` (:688) — the ledger's
  own resolution, used for the absence judgment; after #870 it answers
  `BROKEN` for a bare symbol in a file no rule bounds, which S5 turns into a
  refusal of the row. `#RECORD_COORD_RE` (:5114) and `#heading_rule` (:546)
  — the one coordinate reader and the one heading reader #867 left.
- `evidence_check.py#config_rule` (:3997) — `(config_text, config_rows,
  value_of)` from `hooks/config.py`, or the vendored trio where no `hooks/`
  sits beside the checker; `#frozen_from` (:4011) — the `Ledger frozen
  from` reader, which reads through it. **#867 has landed**, so `Removes
  from` reads through `config_rule()` in `frozen_from`'s shape: phase 3
  generalises `frozen_from` into `cutoff_row(root, item)` and has
  `frozen_from` call it, one reader for both rows (`questions.md` Q5,
  closed by this reading).
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
  `seal/config.md` (six rows at 81037623, `Ledger frozen from | 1790993141`).
- `docs/the-record-layout.md` §*docs/* — the table a new document takes a
  row in.
- `hooks/git/post-commit.py`, `pre-commit.py`, `reference-transaction.py` —
  three Python units with no docstring, in the population under (b); under
  (a) they were in too, by their calls. #868's reframe reads
  `reference-transaction` as the act a switch is observed by, so the file
  may change before the build; its class is #868's spec to state.

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
| (b) with module bodies inverted too — every module docstring declares for its body | about 251 more lines, nearly all `nothing`, for 14 module-level reads at 81037623; a module docstring in `hooks/` is already a page of policy | not taken; module bodies stay the one corner K1 selects, counted by phase 1 and stated as the limit. One row to flip if the count grows |
| (b) with a class word required on every unit K1 selects (no `nothing` there) | K1 then decides something about the population again, if only the word; and a unit that calls `exists` to write is honestly `nothing` | not taken; the contradiction check is the whole of K1's say. The owner's lever if `nothing` is abused |
| Exclude the `Reads:` line from the ledger hash so a backfill drifts no row | the hasher is `py_spans` + `content_hash`, the ledger's premise; changing what a hash covers is the question the owner's review opens for 0.22.0, not this item's | rejected; the cost is stated and handed to #834's timing |
| A table under `docs/`, the ticket's wording | the ceiling, the shared file, the second copy, the `Class` parse | rejected; the owner answered Q1 (a) on 2026-10-08 |
| A table under `docs/readers/`, outside the ceiling's top level | the same shared file and the same second copy | rejected |
| A per-work-item fragment `seal/readers/<id>.md`, folded at release | a second ledger with a fold of its own | rejected |
| Declaration by decorator | needs a module every hook imports; hooks are standalone entry points, and a docstring line needs nothing at runtime | rejected |
| Test modules' helpers in the population | 1,671 more units, 692 of them calling a primitive, at 81037623; their class is read at the assertion they serve | not now; one exclusion to delete, weighed with the census's size after #834's build |
| Rule 2 as a ratchet on `Reads: guess` | the count is unknown until the census empties; a ratchet needs an exemption list | deferred to the owner with the count |
| Rule 2 read from the pull request body or from prose | the guess class | rejected |
| Rule 2 in `unverified-check --baseline` | a second reader of `spec.md` beside the records arm, which would still refuse the removed names; a hygiene step name copied into `broad_gate.py` | rejected; the records arm reads it, and the warden opens the base |
| Keep the per-phase removal table beside `## Removes` | two records of one fact | rejected; the table retires |
| The census inside the test module as a constant | about 1,562 lines in a module; #834's script rewrites it | rejected for a `.txt` beside the test |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **The measurement, at the tree the landed siblings leave.** The walker as a module the test imports (`population(root)`: every top-level unit of every tracked `.py` outside `tests/test_*.py`; `k1_calls(unit)`: the two families with import resolution; `module_body_calls(path)`); the census writer that emits `tests/undeclared_readers.txt` from the walker; and `phases/phase-1.md` recording, with the SHA read: units per root, units K1 selects, units with no docstring, module bodies K1 selects, non-test defs inside `tests/test_*.py` and how many K1 selects, released ledger anchors on population units (distinct units and occurrences, the backfill's drift cost), and which sibling-added units are on the census. No reader's body changes | the walker's cases R5 and R7 as planted roots; the census file's grammar R6; `uvx ruff check` on the module; the record's numbers reproduced by one command the record names | |
| 2 | `tests/test_a_reader_declares_its_input_class.py`: the `Reads:` grammar reader, the census reader, the contradiction check, R1–R4, R8, R9, R10; `tests/undeclared_readers.txt` committed from phase 1's walker at this phase's tree; `py_spans` and `content_hash` imported from `evidence_check.py`. No reader's body changes | the module's cases; R8 seen red twice — one census line deleted, one census hash altered — and the texts of R1–R4, R7, R10 pinned (§14, §15) | |
| 3 | `templates/sdd-spec.md` §*Removes* above the mark; `agents/framer.md`'s writes table and report list name it; `evidence_check.py`: `claim_lines`/`file_claims` read the `## Removes` section's rows as absence claims (`STANDING` via `resolve_unit`, the names on those lines skipped by the name half, a non-coordinate cell and a `BROKEN`-resolving bare symbol refused), `cutoff_row(root, item)` generalised from `frozen_from` and both rows read through `config_rule()`, presence required at or above the cutoff; `templates/config.md` documents the row; `seal/config.md` gets `Removes from | <epoch at the write>`; `templates/sdd-phase.md` §*What this phase removes* removed with its pins in `tests/test_a_phase_hands_the_next_one_a_record.py` and every carrier `grep -rn "What this phase removes"` finds; this item's own `## Removes` row goes from `STANDING` to clean in the same phase | the arm's cases S1–S7 as planted roots in the evidence-check test module that owns the records arm; S8's pins; `bin/evidence-check .` exit 0 at the phase's last commit and exit 1 naming `STANDING` at a probe commit before the template section is removed (S9) | |
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

Six siblings are in this branch's tree already (ad447367); four are open on
their branches and reframed or unfinished on 2026-10-12. Units are named only
as far as each sibling's `spec.md` states them, because each will change
again before it lands; phase 1 reads the tree they leave.

| Sibling | State | Units it adds or removes, as its spec states them | What this build does |
|---|---|---|---|
| #867 (`hooks/config.py`; one coordinate and one heading reader) | landed | adds `hooks/config.py` (`config_rows`, `value_of`, `config_text`, `refusal`, `fence_map`, `hidden_lines`, `unfenced`, `declared_value`, `declared_mode`, …), `evidence_check.py#config_rule`, the `vendored_config_*` trio, `heading_rule`, `heading_level`, `markdown_lines` | all on the census at landing; `Removes from` reads through `config_rule()`; the Removes cell through `RECORD_COORD_RE`, the heading through `heading_rule` |
| #869, #852, #853 (the recorder) | landed | adds `skills/verify/scripts/pytest_record/specseal_pytest_record.py` (reads pytest's hooks: observed; its module body reads `os.environ`, R10's first real case), `broad_gate.py`'s record readers (`record_path`, `records_dir`, …), `release_seal.py`'s `SUITE_RECORDS` reader | on the census; not touched |
| #860, #805 (a fix range across a merge) | landed | `round_record.py#own_commits` and the `-z` listings | on the census; not touched |
| #858, #864, #837 | landed | no guessing reader added (#834's review) | on the census where they added units; not touched |
| #836 (a ledger row's claim is its test), reframed 2026-10-12 | open, `feat/836-…` | adds `evidence_check.py#named_unit` (D2) and a reader of the recorder's `*.jsonl` record (D9: owned), options `--suite-record`/`--suite-key` on `evidence-check` and their pass-through in `broad_gate.py#main` (D10), `fold_check.py#target_problem` loading `evidence_check.py` (D6); the names of the record reader are the work's (its Q6) | lands first (the run's handoff: it clears the release branch's drift); phase 3 edits `claim_lines`, `file_claims` and adds `cutoff_row` — none of #836's units — so the merge seam is the file, not a unit |
| #866 (a round-record cell has one reader) | open, `fix/866-…`, phase 5 stopped mid-edit | adds to `chain_check.py`: `deferred_home`, `issue_of`, `deferred_parts`, `record_facts`, `facts_at_head`, `floor_walks`, `cut_runs`, `gate_before_review`, `close_prefixes`, `fields`, `doubled_fields`, `pass_boxes`, `pull_request_from_gh`, `sealing_excuses`, each with its class in its spec's table; removes `broad_gate.py`'s `deferred_home`, `draft_env`, `round_record.py`'s `location_units`, `pull_request_is_ready` and the regexes its spec lists | its spec's class table is the backfill's source for those units; nothing shared with this build |
| #870, #848 (a unit the extractor cannot bound), reframed 2026-10-12 | open, `fix/870-…` | removes from `evidence_check.py`: `BRACE_FAMILY`, `BRACE_SUFFIXES`, `BLOCK_SUFFIXES`, `brace_family`, the `StringForm` forms, `_literal_at`, `brace_lexed`, `brace_span`, `block_span`, `declaration_opener`, `opens_declaration`, `STATEMENT_WORDS`, `generic_units`, `Resolution.resurrected`; from `rider_check.py`: the resurrection refusal in `region_lines`; keeps `resolve_unit`, `bounding_rule`, `file_units`, `text_regions`, `minor_region` | those units are not in the population at the build; S5 reads `resolve_unit`'s post-#870 `BROKEN` for a bare symbol in a file no rule bounds as a refusal of the row |
| #868, #856 (the hooks read the session, the waiver and a creation one way), reframed 2026-10-12 | open, `fix/868-…` | removes from `hooks/worktree-guard.py`: `_BRACE`, `_unquoted_brace`, `_finding_trees`, the brace arms of `_git_finding`, `_segment_finding`, `_command_findings`, `_first_finding_in`, `_described`'s brace branch; `worktree_consent.py#creation_directory`'s loop; `session-lease.py#owner_pid`; `commit-review-gate.py#git`, `#_reads_marker`, the body of `has_marker`; the guard's `has_token` body and `_without_bodies`; adds `hooks/tokens.py#given`, one placement function in `worktree_consent.py`, `hooksession.is_claude`, `hooksession.claude_pid`; and the reframe reads a switch through `hooks/git/reference-transaction.py` | those units are not in the population at the build; the ones it adds are on the census with the classes #868's spec states beside each |
| #834 (the inventory's build) | not started | every reader file's docstrings; `tests/undeclared_readers.txt` | builds after this item: it writes `Reads:` lines from the inventory's rows, decides how much of the unrowed population to backfill against the drift cost phase 1 measured, and says in its own spec where `inventory/` ends |

## Operational impact

- **No migration, one new config row.** `Removes from` in `seal/config.md`,
  set at the build to the epoch second of the write. A consuming repository
  without the row has presence unchecked; one with a `## Removes` section in
  a live `spec.md` has its rows read as absence claims from this release on,
  which the changelog fragment says.
- **The order of landing is the cost control.** This item builds after
  #836, #866, #870 and #868 have squashed into `release/v0.21.0` and that
  branch is merged into this one (never rebased), and before #834's build.
  Earlier, every sibling that edits a population unit would have to declare
  it and delete its census line on a branch cut before the file existed,
  and four branches deleting neighbouring lines of one sorted 1,562-line
  file conflict at the squash. Later than #834 is impossible, because the
  backfill shrinks a census that has to exist. What 0.21.0 therefore does
  not get: its own reader changes declared at the time they were made. The
  run's handoff asked each frame to state its readers' classes in its
  `spec.md`, so #834's backfill can read them there; #866, #870 and #868
  did.
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
  with `--reverify --into`. The backfill's drift (2,404 anchor occurrences
  on 952 units at 81037623, provisional) is #834's, and phase 1 hands it the
  number read at the tree it will build on.
- **Platform.** The walker is `ast` over UTF-8 text with paths spelled `/`
  as the ledger spells them; nothing it reads differs by platform.
