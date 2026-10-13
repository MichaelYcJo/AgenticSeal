# Implementation Plan: four `Reads:` lines say refused where an off-shape `## Removes` line passes (#905)

<!-- seal/specs/1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-13 by the orchestrating session, under the owner's `automation` answer, when `smith` was spawned.

## Summary

Make the four `refused` words true instead of changing them: a line under
`## Removes` that is neither a table row nor a `nothing — <why>` line is
`REFUSED` naming it, pinned by a case seen red. Reword the two sentences
#834's round 6 found stale (limit 5's reader, the recorder's *strict side*)
and tell the warden what limit 5 now says it does. Write the records last, so
the frame's own `## Removes` rows read as gone the moment the work item
becomes live.

**Reframed after round 3.** Phases 1–3 built that and are closed at their
commits. The review run then found the reader's own rule for telling a
table's header and delimiter row from its body rows wrong in each of three
rounds, each fix the next round's finding, and the chain stopped the fourth
patch (`rounds/round-3.md`, `Fix of a fix | second`). Phases 4 and 5 replace
the rule rather than correct it: `removes_section` reads the section's table
through `hooks/config.py#gfm_table`, the one walker held to cmark-gfm, and
through #871's vendored twin where the copy has no `hooks/` beside it; the
section's other two shapes are read on the lines the walker did not take;
and a sub-heading of the section holds prose and no table, one predicate
with no header in it. `spec.md` §*The reading, redesigned after round 3*
holds the grounds; the rows below hold what the smith builds.

## Technical context

- `skills/evidence-check/scripts/evidence_check.py#removes_section` (:6032 at
  39a315a5) walks `claim_lines` of a frame, keeps the section's table body
  rows and its `nothing` lines, and adds every line number to `cut`. A line
  that `cell_rule()` does not split and that `REMOVES_NOTHING_RE` does not
  match is dropped: no list, no finding. `#removal_findings` (:6066) refuses
  the section only under `required and not (rows or nothing)`; `#file_claims`
  (:6230) calls it for a `spec.md` with `removes` not None and skips the cut
  lines in the name half; `#check_records` (:6323) computes `removes` from
  `Removes from` and the item's epoch.
- `claim_lines` (:5580) hands back `(number, text)` with fences and HTML
  comments taken out, blank lines included as empty text. So the refusal's
  rule is on the stripped text: empty passes; a row passes to the row rules;
  a line beginning `nothing` passes to the reason rule; anything else is
  refused. A `NAME NOT IN TREE` marker exempts a name, not a shape, so a
  prose line carrying it is still refused — it should be a row.
- The quoted-line anchor (`text_regions`, :599) matches a whole line with
  whitespace collapsed, so this frame's three `## Removes` rows quote whole
  lines as they stand at 39a315a5 and read as gone once each clause is
  reworded, however it is reworded.
- `tests/test_a_record_states_what_the_tree_has.py` from line 1548 holds the
  section's cases: `REMOVES_HEAD`, `REMOVES_TAIL`, `frame(tmp_path, rows)`,
  `removes_config`, `refusals`, `work_item`. `test_presence_is_required_at_or_above_the_cutoff`
  pins today's empty-section words, which stay.
- `tests/test_a_folded_statement_names_what_enforces_it.py` and
  `skills/settle/scripts/fold_check.py` read every `Enforced by:` target in
  `docs/`, so the new node id goes in after the case exists.
- `seal/config.md`: `Ledger frozen from 1790993141`, `Removes from
  1791780031`. This item (1791852611) is bound: its `spec.md` carries the
  section. Its work item is live for the records arm only once
  `seal/ledger/1791852611-….md` exists (`unshipped`, :5334;
  `test_a_work_item_with_no_fragment_is_counted_as_unread`), which is why the
  fragment is the last phase's write.
- The warden is told nothing about `Reads:` lines today (`grep -n 'Reads:'
  agents/warden.md skills/code-review/*.md` is empty, 2026-10-13); the
  registry's limit 1 and the test module's item 1 both say it reads them.

**What breaks in six months.** A framer writes a wrapped `nothing — <why>`
across two lines and meets a `REFUSED` naming the second line; the remedy in
the text says to keep the reason on one line or move the rest under a
sub-heading. That is the same one-line rule the `Reads:` line already has (*a
wrapped line has no last word to read*), and the refusal says so. The other
direction — nobody writes prose there any more and the refusal fires never —
costs one unit's worth of code that reads a shape the template forbids, which
is what an owned-format reader is for.

**Technical context of the reframe** (read 2026-10-13 at ac5c6ac7 here and
at beec7bf9 on `fix/871`):

- `hooks/config.py#gfm_table(text, header)` (:1293) returns `(rows,
  refusals)`: rows as `(line number, cells)`, line numbers 1-based into
  `text.splitlines()`, cells stripped and unescaped by `table_cells`;
  refusals as sentences written to read after a noun naming the file, each
  quoting the line. It finds the first shown line (`unfenced`: outside
  fences and closed HTML comment blocks) whose `table_cells` equal `header`,
  refuses a header with a non-blank line directly above it, requires a
  delimiter row of the header's width directly under it, reads rows of that
  width until the table ends (`table_end`: a blank line, a heading, a
  thematic break, a block quote, a list item, an HTML block, a line four
  columns in), refuses a delimiter row anywhere else, a row of another width
  and a line with no pipe inside the table, and after the end refuses a `|`
  line before the next ATX heading as a row the walk never reaches while
  skipping every other line. It returns no header index; #871's writer
  re-finds the header through `table_cells` over `unfenced`
  (`seal.py#with_row` on `fix/871`), and this item does the same.
- `evidence_check.py#config_rule` (:4369) loads `hooks/config.py` by path
  where `CONFIG_READER` and the skill's `SKILL.md` both exist, and returns
  the vendored twins otherwise. `gfm_table` and `table_cells` are two more
  attributes of the module that load already returns; no new loader.
- #871's `evidence_check.py` (243 lines changed on `fix/871`) replaces
  `vendored_config_rows` with the walker's grammar on lines it can judge
  alone — `vendored_cells`, the row, delimiter, heading and list-item · NAME NOT IN TREE
  patterns, a block-opener refusal above the header — header-bound to
  `("Item", "Value")` and returning rows as `(index, item, value)` with
  0-based indices into `gfm_lines(text)`. Its phase 3 (d427badd) is in the
  tree on that branch and its `plan.md` Status column lags it. Lifting the
  header into a parameter and returning `(line number, cells)` is the one
  change this item makes to it, with the config projection kept.
- `removes_section` at ac5c6ac7 (:6032): the header heuristic is the sets
  the loop consults before reading a row; the loop's bounds (`inside`,
  `under`, `level`) are the section's and stay; `claim_lines` with the
  marker blanked is what the leftover reading walks. `heading_level` is the
  one heading rule.
- Measured over the seven live 0.21.1 frames on this machine: every
  `## Removes` table is headed as the template writes it, none has a line
  directly under the heading, none has a `|` line under its sub-heading,
  and #874's five-line `nothing` reason is already refused at ac5c6ac7
  (`spec.md` §*The reading, redesigned after round 3*, ground 5).
- `tests/undeclared_readers.txt:397` holds `hooks/config.py#gfm_table@0f0796e9`:
  a docstring edit to the walker moves that hash and owes a declaration,
  which is why this item does not touch `hooks/config.py`.
- Every `.md` under the work item is a record the name half reads
  (`record_files`), and the corpus excludes `seal/specs/` and
  `seal/ledger/` (`tree_names`). `rounds/round-3.md` and
  `round-3-report.md` name the two sets the heuristic kept, on claim lines
  (round-3.md:31 and :98; the report at :10, :34, :42, :97, :173); once the
  sets leave, those lines are `NOT-IN-TREE` unless they carry the marker,
  which is the shape every round record at v0.21.0 that names a unit that
  left already has (ten of them, `git ls-tree v0.21.0`).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **Refuse the off-shape line; the four words stay `refused`, held by a test** | a frame that wants prose under the heading meets a refusal and moves one line; a wrapped `nothing` reason is refused at its second line | **chosen** — the converged shape of #834's table (owned format, unknown refused), #836's form for a claim (the test holds it), block-more as the cheaper direction, zero prompts; cost measured at two shipped, unread frames and no live one |
| Change the four words to `mixed` and add a paragraph under `removes_section` (round 6's first paste-ready) | records a tolerant owned-format reader as a fact; a removal written as a bullet stays a claim nobody reads; the paragraph is prose a reviewer re-reads, limit 5 again — round 5 fixed a direction word by prose and round 6 found the fix false | rejected |
| State in the registry that prose under the section is read as prose and keep `refused` | deciding from a person's line whether it is prose or a claim is a guess-class reader; a bullet naming a unit is both | rejected |
| Refuse only lines that look like claims (a bullet, a backticked name) and pass plain prose | the same guess-class reader, one shape narrower; the next shape is the next issue | rejected |
| Remove the direction word from the `Reads:` grammar, or add a checker that reads direction words | a change to #835's shipped rule in `docs/`, a `feat:` in a patch release; a checker cannot read a semantic claim (limit 1); without the word a bounded guess (allow-list, unknown refused) and an unbounded one read alike in `grep -rn "Reads: guess"` | out of scope; `questions.md` P1 carries it to the owner, non-blocking |
| ⬜ 4 by rewording the document alone, limit 5 stated as *read by nobody until the helper changes* | honest, but the lead then says the reviewer reads each limit and limit 5 says nobody does; and a reviewer did read helpers' lines at their callers in round 6, as the registry's own definition asks | rejected in favour of naming the warden and telling it, one sentence in `agents/warden.md`; P2 lets the owner take this one instead |
| ⬜ 5 by deleting the clause | leaves the module saying nothing about what a missing record means to the gate, which is what a reader opening it wants to know | rejected; the clause is replaced on its line by what #836 made true (round 6's option B wording) |
| Write the ledger fragment at phase 1 | the item becomes live while the three `## Removes` rows still stand, and `evidence-check` exits 2 on the frame's own rows until phases 2 and 3 land | rejected; records are the last phase |
| Edit `file_claims` and `check_records` docstrings too, for symmetry | moves ten released anchors and owes ten `Re-read ·` rows for words that are already true read through | rejected; the two helpers that change are the two whose text was false |
| **(reframe) Read the section's table through `hooks/config.py#gfm_table`, the walker held to cmark-gfm, and #871's vendored twin where the copy has no `hooks/`** | a frame whose table is headed otherwise than the template's, or whose header sits directly under `## Removes`, is refused where it was read before; the walker's sentences name the line and the edit, and no live frame has either shape (measured) | **chosen** — the header and the delimiter row are the walker's by construction, held by an enumerated oracle rather than by a case per shape; it is the reader #871 is moving the config table onto this release, and a fourth header rule here is the grammar-beside-the-walker that item retires |
| (reframe) Patch the header rule a fourth time with round 3's paste-ready fix (a header is a table's first row when a rule row follows it) | the fix reads a row's neighbours to decide what GFM decides by position, and the next shape — a table whose first row is not the header the template writes, a delimiter row of another width, a `\|` line after the table ended — is the next round's finding; three rounds measured exactly that | rejected; the chain's stop rule forbids it and the measurement agrees |
| (reframe) A GFM-shaped reader of `evidence_check.py`'s own, used by both copies and held to `gfm_table` by a case over shared shapes | a second table walker in the plugin beside the one the oracle holds, which is #871's finding one file over; held to the walker only on the shapes somebody wrote, never to the renderer | rejected; the plugin's copy loads the walker, the vendored copy takes the twin, the pattern `config_rule` already is |
| (reframe) Read the first table under the heading whatever its header, rather than the template's header | the walker is header-keyed, so this is a walker variant or a pre-pass that guesses which `\|` line is a header — the question the three rounds could not answer; and a frame's table headed otherwise is a shape the template forbids | rejected; the header is pinned to the template's, English under any `Record language` as every field name a checker reads is, and every live frame already writes it |
| (reframe) Under a sub-heading of the section, refuse a body row and let a header and its delimiter row through (round 2's reading) | needs the header rule the reframe retires; a foreign table's body rows are refused with a remedy that says to move them into the table above, which is wrong for a comparison table | rejected; a sub-heading of the section holds prose and no table — every `\|` claim line there is refused naming it, and a table goes in a section of its own |
| (reframe) Let the `nothing — <why>` line wrap as a paragraph | GFM reads the lines as one paragraph, so the rule is decidable; but it is a second reading of one line kind (the `Reads:` line's one-line rule stays), a template change, and #874's five-line reason is already refused at ac5c6ac7, so the gather names it either way | rejected; one line, the refusal names the sub-heading as the home for the rest |
| (reframe) A fifth oracle pass for the `## Removes` header | a three-cell header already takes a pass (the pact-review table) and the walker reads a header as a tuple to equal; the pass costs suite time and edits a file #871 is editing | rejected |
| (reframe) Write the twin in this item without waiting for #871 | two twins of one walker in one file, each held to it by its own case — the fork the seam exists to prevent | rejected; phase 4 is built on a base that holds #871's twin, and the smith hands back rather than writing one |
| (reframe) Keep the three closed round-3 records untouched and let them read `NOT-IN-TREE` after the sets leave | the branch's `evidence-check --strict` fails on records nobody can repair but by the marker, and the sealer's broad gate is that run | rejected; phase 4 puts the marker on those lines and moves no other byte of a closed record, the shape the v0.21.0 round records already take |
| (reframe) Append to `docs/the-reader-registry.md` and `templates/sdd-spec.md` a paragraph saying what changed and why | the document stops stating the rule and starts narrating its history, and the next reader cannot tell the rule from the story | rejected, the owner's rule of 2026-10-13: a document or template that states the rule is rewritten in place to the current rule; the account of the change is the issue's, the round records' and the changelog's |

## Phases

Vertical slices — each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **The two stale sentences and the warden's sentence (⬜ 4, ⬜ 5).** `docs/the-reader-registry.md` §*What neither check can read*: the lead, limit 5 and the `Enforced by:` line name the warden, and limit 5 says the warden reading a caller's change opens the lines of the helpers whose value it changes; `tests/test_a_reader_declares_its_input_class.py`'s docstring item 5 says the same; `agents/warden.md` §*Role* gains one sentence telling the warden to; `specseal_pytest_record.py:108` says a missing record is not measured where the suite failed and existence alone on the ledger arm. The three quoted lines of `spec.md` §*Removes* are gone from the tree. | `git grep -n "the strict side" -- skills` and `git grep -n "does not show its line" -- docs tests agents` print nothing; `bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py tests/test_the_recorder_writes_what_its_process_ran.py tests/test_one_word_one_meaning.py tests/test_a_section_marked_for_one_role_reaches_only_that_role.py` exit 0; `bin/fold-check --root .` exit 0; `bin/evidence-check .` names #835's D1 row on `docs/the-reader-registry.md` as the one DRIFTED anchor and nothing BROKEN | 3a66113f |
| 2 | **The refusal (S1–S4).** `removes_section` hands back the off-shape lines; `removal_findings` refuses each at its line, naming the line, the two shapes and where prose goes; both docstrings say so, their `Reads:` lines unchanged; the new cases in `tests/test_a_record_states_what_the_tree_has.py`, each shown red against phase 1's commit before it is committed; `docs/the-reader-registry.md` §*A frame names what its work removes* gains the sentence and its `Enforced by:` line the node id; `templates/sdd-spec.md`'s comment says nothing else sits under the heading and where prose goes. | the new cases red at phase 1's head and green at this one, the method in `phases/phase-2.md`; `bin/test -q -p no:cacheprovider tests/test_a_record_states_what_the_tree_has.py tests/test_a_reader_declares_its_input_class.py tests/test_a_folded_statement_names_what_enforces_it.py tests/test_a_phase_hands_the_next_one_a_record.py` exit 0; `bin/evidence-check .` names no `file_claims` or `check_records` anchor; `git diff --stat origin/release/v0.21.1 -- skills/evidence-check/scripts/evidence_check.py` shows hunks only inside `removes_section` and `removal_findings` | 8879db49 |
| 3 | **The records (S7).** `seal/ledger/1791852611-….md`: `evidence-check --reverify --into seal/ledger/1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes.md --checked <date>` writes D1's `Re-read ·` row; test-held rows for S1–S3; hashed rows for S5 and S6 (quoted-line anchors on the three rewritten clauses, and on the warden's sentence); `changelog.md` under `### Fixed`; `overview.md`; `phases/phase-3.md`. | `bin/evidence-check --strict .` exit 0 with the fragment present — the frame's three `## Removes` rows silent, D1 cleared, every test row resolving; `bin/correction-check --range origin/release/v0.21.1...HEAD` exit 0; `bin/unverified-check --baseline origin/release/v0.21.1` exit 0 | 49835329 |
| 4 | **The table through the walker (S1–S4, S9–S12; the reframe).** Built on a base that holds #871's vendored twin (§*Operational impact*). `removes_section` hands the section's body to `gfm_table` with the template's header where `hooks/config.py` stands beside the skill — through the module `config_rule` already loads — and to the twin where it does not; the twin is #871's `vendored_config_rows` lifted to take a header and return `(line number, cells)`, with `vendored_config_rows` left as its projection; the header constant beside `REMOVES_HEADING`; the header's line re-found through the module's `table_cells` and the twin's cell reader; the two sets the heuristic kept and the header distinction gone; `strayed` is every `\|` claim line under a sub-heading up to the next level-2 heading; `removal_findings` surfaces a walker sentence once at the frame quoting the line, does not fire the empty-section refusal where the walker refused the table it found, and rewrites the off-shape, sub-heading and wrapped-`nothing` details (round 1's ⬜ 3). Both docstrings rewritten to what the units do: `removes_section`'s class word `guess`, every direction word `refused`. Tests: S9, S11 and S12's cases new, S10's re-pinned with the foreign-table ids, the header pin deleted; every new or re-pinned id shown red against ac5c6ac7's reader before it is committed. **`docs/the-reader-registry.md` §*A frame names what its work removes* and `templates/sdd-spec.md`'s comment are rewritten in place to the current rule: the sentences that state the rule are edited where they stand, and no paragraph is appended narrating the header rule, the rounds or this reframe — that account is the issue's, the round records' and the changelog's (the owner's rule, 2026-10-13).** The `Enforced by:` line names the cases that hold the statement and drops the deleted one. The claim lines of `rounds/round-3.md` and `round-3-report.md` that name the two sets gain ` · NAME NOT IN TREE`, and no other byte of a closed record moves. `hooks/config.py` is not edited. Direction: refuse more, in one command; prompt budget zero | the new and re-pinned ids red at ac5c6ac7's reader (method in `phases/phase-4.md`) and green at this head; `bin/test -q -p no:cacheprovider tests/test_a_record_states_what_the_tree_has.py tests/test_evidence_check.py tests/test_a_reader_declares_its_input_class.py tests/test_a_folded_statement_names_what_enforces_it.py tests/test_one_word_one_meaning.py` exit 0; `bin/fold-check --root .` exit 0; `git grep -n "rule row directly follows" -- docs templates skills tests` prints nothing; `git diff --stat origin/release/v0.21.1 -- hooks/config.py` prints nothing; `bin/evidence-check .` names no `file_claims` or `check_records` anchor and no `NOT-IN-TREE` in `rounds/` | |
| 5 | **The records (S7, S13; the reframe).** `seal/ledger/1791852611-….md` edited in place, as this item's own fragment: F1 reworded to the sub-heading's one predicate, F3 replaced by S9–S11's test-held rows, F4 kept, S1–S3 and M1 re-checked against the redesigned reader with their red-first evidence re-stated, R1 and R2 re-hashed on the rewritten lines, a row for S12; `evidence-check --reverify --into seal/ledger/1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes.md --checked <date>` after the rows are in, for any released row the registry edit drifts. **`changelog.md` rewritten in place** to what ships — the walker reading, the sub-heading rule, the off-shape refusal, the two corrected sentences — with no entry narrating the header rule it replaced. `overview.md`'s divergence table gains what phase 4 found; `phases/phase-4.md` and `phase-5.md` | `bin/evidence-check --strict .` exit 0 — the frame's six `## Removes` rows silent, every test-held row resolving; `bin/correction-check --range origin/release/v0.21.1...HEAD` exit 0; `bin/unverified-check --baseline origin/release/v0.21.1` exit 0 | |

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true, which is the failure the evidence ledger exists to prevent.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past one
— someone can open it — which is the same trick that lets a round record live
beside the contract rather than in tool state.

Fill it in as each phase closes, not at the end. What a phase discovers while
it is being built, and needs the next phase to know, goes to
`seal/specs/1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes/phases/phase-N.md`,
from `templates/sdd-phase.md`, when the phase closes. Re-read the Status
column after any rebase: a squashed or rebased commit still answers
`git cat-file` in the worktree that wrote it and nowhere else.

### Notes for the builder, by phase

- **Phase 1.** The three clauses are quoted whole in `spec.md` §*Removes*;
  any rewording clears them. Limit 5's new last sentence should keep the two
  facts (the hash does not move, the diff does not show the line) and add the
  act (the warden opens the helpers a changed caller feeds); round 6's
  paste-ready for ⬜ 4 is one wording. The warden's sentence belongs where
  §*Role* tells the warden what to open for a changed unit, one sentence, no
  new heading; the `seal` word rule (`tests/test_one_word_one_meaning.py`)
  and the role-marker test run on `agents/*.md`. Round 6's option B is one
  wording for the recorder's clause. Phase 1 edits no code outside
  docstrings, so the only anchor that moves is D1; leave its re-read to
  phase 3, where the fragment is written once.
- **Phase 2.** Red first: run the new cases against phase 1's head (a
  `git stash` of the code edit, or `git -C <wt> show <phase-1 sha>:…` into a
  scratch copy under the scratchpad) and record the failing assertion in
  `phases/phase-2.md`. The refusal's detail is new text (§14): name the
  line in backticks, say *a line under `## Removes` is a table row or
  `nothing — <why>`*, and say where prose goes — a row's last cell, the
  `nothing` line's reason, or an HTML comment. Keep the existing
  empty-section refusal's words byte for byte; S3 asserts both findings.
  Blank lines and the header and rule rows pass (S2). The `## Removes` rows
  of this frame are read by nothing until phase 3, so the registry document
  can change in this phase without a STANDING finding.
- **Phase 3.** Write the fragment from `templates/ledger.md`'s row shapes:
  a test-held row is `tests/test_x.py::test_y` in backticks in the Code
  grounds cell with how it was seen red in Verified behavior
  (`docs/the-evidence-ledger.md` §*A claim held by a test*); a hashed row is
  `path#"<whole line>"@<hash>` or `path#unit@hash`. Run `--reverify --into`
  after the new rows are in the file, so one run dates everything. The
  changelog fragment is one `### Fixed` entry in the shape of
  `changelog/0.21.0.md`'s: what a reader meets (a refusal naming the line),
  why (a removal written as a bullet was read by nobody), and the two
  sentences corrected, each with its issue number.
- **Phase 4.** Red first against ac5c6ac7's reader: `git -C <wt> show
  ac5c6ac7:skills/evidence-check/scripts/evidence_check.py` into a scratch
  copy under the scratchpad, or the module swap round 2's reviewer used,
  and the failing assertion of each new or re-pinned id in
  `phases/phase-4.md`. Keep the six-tuple so `removal_findings` unpacks
  nothing new; W3 is where a walker refusal rides. The body handed to the
  walker is text joined from the file's own lines with the marker blanked,
  so the walker's `(line number, cells)` offsets by the body's first line;
  `claim_lines` over the same blanked lines is the leftover reading, and a
  line both hide (a fence, a comment) is in neither set. Where the walker
  says it holds no such table, every `|` claim line of the body is refused
  naming the header the table takes, and the empty-section refusal keeps
  today's words. The twin's lift: the header parameter replaces the config
  constant inside the function body, `name`, `written` and the width follow
  it, rows come back as `(index + 1, cells)`, and `vendored_config_rows`
  becomes `[(index - 1, *cells) …]` over them or whatever keeps its callers'
  `(index, item, value)` byte for byte — #871's config case decides. S12's
  case: the mechanism of `tests/test_evidence_check.py#test_the_vendored_config_rule_agrees_with_the_shared_one`,
  so the twin is exercised without a second plugin copy; W4 is where the
  switch sits. The documents: edit the registry statement's sentences where
  they stand and the template comment's lines where they stand, and leave
  the surrounding statements alone; `tests/test_a_folded_statement_names_what_enforces_it.py`
  and `bin/fold-check` read the `Enforced by:` line, so the deleted pin
  leaves it in the same commit the test file loses it. The round-3 marker
  lines are the claim lines the technical context names, and the marker is
  ` · NAME NOT IN TREE` at the line's end as the v0.21.0 round records
  write it.
- **Phase 5.** The fragment is this item's own (`seal/ledger/1791852611-….md`),
  not a released file, so its rows are edited in place; a `Re-read ·` row is
  owed only to a released row, and `--reverify --into` writes those. Run it
  after the rows are in, so one run dates everything. The changelog entry
  is one `### Fixed` entry in the shape it has now, saying what a reader
  meets — a refusal in the walker's sentence, an off-shape refusal naming
  the line, a sub-heading that holds prose and no table — and not how the
  reader got there.

## Operational impact

- **A new refusal in `evidence-check`'s records arm**, exit 2, in every
  repository that runs it: a live frame with a line under `## Removes` that is
  neither a row nor a `nothing — <why>` line. At 39a315a5 no live frame in
  this repository has one; the two shipped frames that do are not read. A
  sibling 0.21.1 frame that writes prose there meets the refusal at its own
  `evidence-check` run and moves the line (`questions.md` M1 names who
  re-measures at the gather).
- No migration, no new dependency, no environment variable. The direction is
  block more; the prompt budget is zero.
- One released ledger row drifts (#835's D1) and is re-read in this item's
  fragment; `seal/releases/0.21.0.md` is not edited.
- **Sequencing with #871 (the reframe).** Phase 4 is built on a base that
  holds #871's vendored twin: `release/v0.21.1` after #871 merges, merged
  into this branch. The orchestrator sequences it. If #871 has not merged
  when the smith is spawned for phase 4, the smith hands back at phase 4's
  first edit rather than writing a twin of its own: two twins of one walker
  in one file is the fork the seam exists to prevent. Past that, the two
  branches share no edit — this item touches neither `hooks/config.py` nor
  the oracle module, and #871 touches neither `removes_section` nor the
  records tests.
- **What a frame meets after phase 4**, beyond ac5c6ac7's refusals: a table
  headed otherwise than the template's; a header directly under
  `## Removes`; a delimiter-shaped row anywhere but under the header; a row
  of another width; a `|` line after the table ended; any `|` line under a
  sub-heading of the section. Each is one `REFUSED` with the line quoted and
  the edit named, exit 2, in `evidence-check` alone; no hook changes what it
  says. Measured over the seven live 0.21.1 frames: none has any of them,
  and #874's five-line `nothing` reason is refused at ac5c6ac7 already and
  still is (M2 re-measures at the gather).
- **The frame's three reframe rows of `## Removes` read `STANDING` from the
  reframe's commit until phase 4's**, exit 2 on the branch's
  `evidence-check --strict`: the item is live and the redesign is named
  before it is built, as the section asks. The pull request's evidence job
  is red for that span by design, and green again at phase 4.
