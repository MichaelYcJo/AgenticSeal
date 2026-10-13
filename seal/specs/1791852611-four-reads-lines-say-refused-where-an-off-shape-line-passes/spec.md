# Feature Specification: four `Reads:` lines say refused where an off-shape `## Removes` line passes (#905)

<!-- seal/specs/1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate.
Framed by `specseal:framer` on Fable 5.1 for #905, for release 0.21.1, at
39a315a5 on `fix/905-four-reads-lines-say-refused-where-an-off-shape-line-passes`
(based on `release/v0.21.1`). Nobody is asked mid-run: what the tree could
answer is answered here, and what it could not is a row of `questions.md`
with a default the plan is built on. Reframed by the same, after round 3, at
ac5c6ac7: the review run stopped on a second fix of a fix inside
`removes_section`, and §*The reading, redesigned after round 3* is what the
reframe changes; everything above it stands as framed. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `docs/the-reader-registry.md` §*The four classes and the line that declares one* | The direction word is *where an input the unit does not understand ends, read through to the decision the unit's value feeds*: `refused` where that decision refuses it, `passed` where it is let through as if understood, `mixed` where both happen; a helper's direction is read at its callers. The four lines this item is about are judged against that sentence and no other. |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | The `## Removes` section's grammar: table rows whose coordinate is the ledger's grammar without a hash, or one `nothing — <why>` line; `evidence-check`'s records arm reads it in every live frame, a cell the ledger would refuse is `REFUSED`, never read as gone. This item adds to that statement what happens to a line that is neither shape, and its `Enforced by:` line names the new case. |
| `docs/the-reader-registry.md` §*What neither check can read*, limits 1 and 5 | A false or stale `Reads:` line passes both checks and the reviewer is its reader. ⬜ 4 is that section disagreeing with itself about who that reader is for limit 5; this item makes the lead, limit 5 and the `Enforced by:` line name one reader and say how that reader sees a caller-staled helper's line. |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | The refusal this item adds is a change to a gate: a test seen red, a stated failure direction (block more), a prompt budget (zero), and — by the same section's last two bullets — a `Reads:` line on every changed unit and a frame that names what it removes. |
| `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment* | `seal/config.md` declares `Ledger frozen from 1790993141`, so the one released row this item drifts (#835's D1 on `docs/the-reader-registry.md`) is re-read by a `Re-read ·` row in `seal/ledger/1791852611-….md`, written by `evidence-check --reverify --into … --checked <date>`, never in `seal/releases/0.21.0.md`. |
| `docs/the-evidence-ledger.md` §*A claim held by a test* | A row whose claim is a behaviour names the test that holds it instead of a hash, so the refusal's rows owe no re-read when the code is next edited. |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file*; §*A commit after the build brings its changelog fragment along* | The ledger rows go in `seal/ledger/1791852611-….md` and the release note in this directory's `changelog.md`; a fix after the build that changes what ships brings the fragment along. |
| `skills/agent-contract/SKILL.md` §14, §15 | The refusal's text is something a person reads and acts on, so the commit that adds it pins it; the case is shown red against the code as it stands before it is committed. |
| `CLAUDE.md` §*The goal a design is chosen against* | Between the two fixes of the four words below, the one that converges without a person re-reading prose is preferred; the direction is argued, not assumed. |

## Scope

### Why this item exists

#835 shipped 26 `Reads:` lines. #834's round 6 read all of them under the
settled direction sentence and found four false: `removes_section` and the
three units that hand its reading on, `removal_findings`, `file_claims` and
`check_records`, each ending `unknown refused`. Executed by that round, and
read again by the framer in the code at 39a315a5
(`skills/evidence-check/scripts/evidence_check.py#removes_section`,
`#removal_findings`): a line inside `## Removes` that is neither a table row
nor a line beginning `nothing` is added to the cut set and kept in no list.
`removal_findings` refuses the section only where `required and not (rows or
nothing)`. So a bullet naming a unit, a capitalised `Nothing — …`, a prose
paragraph or the wrapped second line of a `nothing` reason is `REFUSED` in
one case — the cutoff requires the section and it holds nothing else — and
passes unread beside a row or in a frame no cutoff binds. Under the registry's
sentence that is `mixed`, and the word on all four lines is `refused`.

The defect under the word is the one that matters: **a removal written as a
bullet is a claim of absence that nobody reads.** The section exists so that
what a work item takes out of the tree is a checked claim; a line the reader
drops silently is exactly the record-nobody-reads that #834's inventory
found behind every reader that kept being reopened.

Two sentences ride with it, from the same round:

- **⬜ 4.** `docs/the-reader-registry.md` §*What neither check can read*: the
  lead says *the reviewer is the reader of each*, the `Enforced by:` line says
  *each is the warden's reading of the diff at review*, and limit 5's last
  sentence (added by #834's round 5) says a caller-staled helper's line is one
  *the diff the warden reads does not show*. The document names, for one
  limit, a reader that by its own sentence cannot see it. The test module's
  docstring item 5 (`tests/test_a_reader_declares_its_input_class.py:30`)
  mirrors the sentence.
- **⬜ 5.** `skills/verify/scripts/pytest_record/specseal_pytest_record.py:108`
  says a record the recorder cannot write is one *which the gate reads as no
  record -- the strict side*. True when #825 wrote it; since #836 (23f5977)
  the ledger arm reads a missing record as *existence alone* and a green run
  still seals. The sentence misled #834's round 5 into a wrong fix, which #904
  took back; the sentence itself is still in the tree.

### The judgment the ticket left open: correct the four words, or make the word true

Round 6's paste-ready offered three fixes: change the four words to `mixed`
and add a paragraph; refuse the off-shape line, which makes `refused` true;
or state in the registry that prose under the section is read as prose and
keep `refused`. The issue asks that the choice be weighed against #834's
inventory, whose finding is that *a direction word a reader cannot check
costs what the withdrawn backfill cost*.

**This item makes `refused` true**: `removes_section` hands back every line
under the heading that is neither a table row nor a `nothing` line, and
`removal_findings` refuses each one naming it. The four words stay as they
are, and a test holds the behaviour they describe. The grounds, each
openable:

1. **It is the converged shape, and `mixed` is the one that did not.**
   #834's own table (`seal/specs/1791382684-every-reader-and-record-is-inventoried/spec.md`
   §*Families since 0.18.0*): what converged *read an owned format or an
   observed fact and refused the unknown*; what did not *read someone else's
   text and let the unknown through*. `## Removes` is an owned format — this
   repository's template, `templates/sdd-spec.md` §*Removes*, allows a table
   or one `nothing — <why>` line and nothing else. Writing `mixed` on an
   owned-format reader records, as a fact, the tolerant reading the inventory
   found behind every reopened family, and keeps the bullet case unread.
2. **It is what #836 prescribes for a claim.** `docs/the-evidence-ledger.md`
   §*A claim held by a test*: a claim is the test that enforces it. A
   direction word is a claim about where the unknown ends; for these four
   units the claim is one case — an off-shape line ends `REFUSED` — and a
   test can hold it. Writing `mixed` plus a paragraph is the other form, a
   prose description a reviewer has to re-read, which is limit 5 of the
   registry and the shape round 5 got wrong once already.
3. **The third option is a guess-class reader.** *Prose under the section is
   read as prose* means deciding, from a person's line, whether it is prose
   or a claim — a bullet naming a unit is both. That is reading a person's
   text for its shape, `guess` by the registry's own table.
4. **The cost is measured and small.** The framer's probe over every
   `seal/specs/*/spec.md` at 39a315a5 (executed 2026-10-13): 4 frames carry a
   `## Removes` heading; 2 carry lines under it that are neither a row nor a
   `nothing` line — `1791382684` (a three-line paragraph, and its two mark
   lines, because its spec has no `## Open questions` heading after the
   section) and `1791781864` (a four-line paragraph the smith wrote under its
   rows). Both shipped in 0.21.0 and hold no ledger fragment, so neither is
   a live frame and neither is read. The six 0.21.1 sibling branches pushed
   today (`fix/871`, `fix/872`, `fix/873`, `chore/844`, `chore/874`,
   `fix/903`) hold a `routing.md` and no `spec.md` yet (read 2026-10-13 from
   `origin/*`), so no frame this refusal would meet exists. A frame that
   wants prose under the heading has three places for it that are not read as
   claims: a row's last cell, the `nothing` line's `<why>`, and an HTML
   comment, which `claim_lines` already treats as an aside.
5. **The failure direction is the cheaper one.** A wrong deny here costs one
   edit of one line in a `spec.md`, named by the refusal; a wrong allow is a
   removal nobody checked, which is the class #107 recorded and the section
   exists to end. The refusal puts no question in front of a person.

**What this item does not do about the direction word in general.** It does
not remove the word from the grammar, does not add a checker that reads
direction words, and does not re-read the other 22 lines. Grounds: the word
is the inventory's one predictive column — a `guess` is allowed by #835's
rule 1 *only as an allow-list that refuses what it does not recognise*, and
the direction word is how that condition is stated per unit; without it
`grep -rn "Reads: guess"` cannot tell a bounded guess from an unbounded one.
A general checker cannot read it (limit 1: it is a semantic claim read
through to a decision), and per-unit the way to make it checkable is what
this item does for one class: make the word true and name the test that
holds it. Whether that becomes a rule for every direction word, or the word
retires, is a change to #835's shipped rule and `docs/`, a `feat:` in a
patch release, and the owner's — `questions.md` P1 carries it as a
non-blocking row. The 22 other lines were read true by #834's round 6
(`rounds/round-6.md`, the last 🟢 row) and are not reopened.

### The reading, redesigned after round 3

The build made `refused` true at 8879db49, and the review run then found the
reader's own account of a table wrong three times, once per round, each fix
the next round's finding (`rounds/round-1.md` 🟡 1, `round-2.md` 🟡 1,
`round-3.md` 🟡 1): a table row under a sub-heading was read by nobody; then
a header was known by its first cell, so a foreign header was refused and a
body row reading `Removes` passed; then any row a rule-shaped row follows
was a header, so a body row above `| - | - | - |` vanished with it. Three
patches to one question — *which lines of the section are its table, and
which of those are the header and the delimiter row* — and
`skills/code-review/orchestration.md` §*A fix of a fix twice sends the work
item back to its framer* stops a fourth. The redesign answers the question
with the unit this repository already holds to GitHub's renderer, and writes
no rule of its own for it.

**`removes_section` reads the section's table through the one GFM table
walker, `hooks/config.py#gfm_table`**, held to cmark-gfm over an enumerated
corpus by `tests/test_one_table_walker_reads_what_gfm_renders.py` (#647).
The walker knows a header and a delimiter row by construction: the header is
the first line whose cells equal the header it is handed, the delimiter row
is the line directly under it of the same width, and every line after that
is a row of that width, the table's end, or a refusal in a sentence quoting
the line — a delimiter row out of place, a row of another width, a line with
no pipe that GFM reads as a row, a `|` line after the table ended. Round 3's
`| - | - | - |` is *a delimiter row out of place* to it, round 2's foreign
header is a line it never reads as this table, and round 1's heuristic has
nothing left to decide. The grounds, each openable:

1. **It is the reader this release is converging on.** #871, built in
   parallel, moves `seal/config.md`'s table onto the same walker because an
   owned grammar beside it handed gates rows GitHub does not render and
   dropped rows it does (`seal/specs/1791852616-…/spec.md` §*Data &
   interfaces*, sixteen measured shapes, read 2026-10-13 at beec7bf9 on
   `fix/871`). A fourth header rule in `removes_section` is the
   grammar-beside-the-walker that item retires one file over.
2. **The walker's property is the one the three rounds were trying to
   state.** S1 of #647: on every shape the walker's cells equal cmark-gfm's,
   or the walker refuses. That is the direction the four `Reads:` lines
   claim, `unknown refused`, held by an oracle over an enumerated corpus
   rather than by one case per shape somebody thought of. Round 3's reviewer
   found its shape by generating 40,000 sections; the oracle enumerates that
   corpus by construction and runs on every suite.
3. **The copy with no `hooks/` beside it is already provided for.**
   `evidence-ci` vendors `evidence_check.py` alone into a repository's
   `tools/`, where `hooks/config.py` is not beside it. `config_rule` loads
   the module where it stands and falls back to a vendored twin where it
   does not, and #871 writes that twin for the walker (a cell reader and
   `vendored_config_rows`, header-bound to `| Item | Value |`, read
   2026-10-13 at beec7bf9 on `fix/871`). This item lifts the twin's header into a
   parameter and reads the section through it; it writes no second twin
   (§*Data & interfaces*).
4. **What the walker does not decide is decidable from one line.** The
   walker reads the table; the section's two other shapes are the template's
   and are read on the lines the walker did not take: a line beginning
   `nothing` is the `nothing` line, and every other claim line of the body is
   off-shape and `REFUSED` naming it — the deliverable this item opened with,
   unchanged. Under a sub-heading of the section the rule is one predicate
   with no header in it: **a sub-heading of `## Removes` holds prose and no
   table**, so a line written `| …` there is `REFUSED` naming it, whatever
   it is the header or the body of. Round 2's 🟡 1 read a foreign table's
   header there as a thing to let through; that reading is what put a header
   rule under the sub-heading at all, and it is reversed — a comparison table
   has a home in the frame, which is a section of its own.
5. **The cost is measured, and the walker's refusals meet no live frame.**
   Executed 2026-10-13 over the seven live 0.21.1 frames on this machine
   (`17918526*` in the sibling worktrees): every table is headed as the
   template writes it, none has a line directly under `## Removes`, none has
   a `|` line under its sub-heading. One frame, #874's, writes its
   `nothing — <why>` reason across five lines; the reader at ac5c6ac7
   already refuses lines two to five of it, so the gather's run (M1) names
   it with or without this redesign.

### In

1. **The table, through the walker.** `removes_section` hands the section's
   body — its lines from the `## Removes` heading to the first heading of any
   level, with the marker blanked — to `gfm_table` with the template's
   header, `("Removes", "Coordinate", "Where it lands, or why it can go")`,
   where the plugin's copy stands, and to the vendored twin where it does
   not. The rows it reads are the removals. Where it refuses, its sentence is
   one `REFUSED` of the records arm at the frame, quoting the line as the
   walker writes it; the rows it read above the stop are still read, and the
   lines it never reached are not refused a second time.
2. **The off-shape refusal, unchanged in what it catches.** Every claim line
   of the body the walker did not read as the header, the delimiter row or a
   row, and that does not begin `nothing`, is `REFUSED` at its line number,
   naming the line, saying the section holds one table headed as the
   template writes it or one `nothing — <why>` line, and saying prose goes
   under a sub-heading after the table. Required and unrequired alike, beside
   a row or alone, exit 2. A body with no such table and a `|` line in it is
   refused at that line naming the header the table takes. The existing
   refusal of a required section that is absent or holds no table and no
   `nothing` line stays in its words, and does not fire where the walker
   refused the table it found.
3. **A sub-heading of the section holds prose and no table.** From the first
   sub-heading to the next heading of level 2 or above, a claim line written
   `| …` is `REFUSED` naming it, with the remedy: a removal goes in the table
   above, any other table in a section of its own. Every other line there is
   read by the name half as the rest of the frame is, and is not cut. No
   header rule and no rule-row rule: the two sets the heuristic kept, the
   header distinction inside `strayed` and the sentences describing them
   leave `removes_section`.
4. **The marker is blanked before the walker and the leftover reading see
   the lines**, as round 1's 🟡 2 settled: a marked row is a row, a marked
   bullet is off-shape, and no line of the section is exempt.
5. **The four words stay `refused`.** `removes_section`'s docstring is
   rewritten to what the unit does — the table through the walker, the two
   template shapes on the lines the walker did not take, the sub-heading's
   one predicate — and its `Reads:` class word moves from `owned` to `guess`,
   the class #871 gives every reader of a person's table through the walker;
   its direction word stays `refused`. `removal_findings`'s docstring says
   the same in its own terms, and its `Reads:` line is unchanged: it reads
   coordinates, an owned grammar. `file_claims` and `check_records` are not
   edited: their words are true read through, and the ten released anchors
   on them (six on `check_records` and four on `file_claims`, in
   `seal/releases/*.md`) owe no re-read.
6. **The rule's statement, rewritten in place.** `docs/the-reader-registry.md`
   §*A frame names what its work removes*, first statement, states the
   current rule in the sentences it has: the table read as cmark-gfm renders
   it through the one walker, headed as the template writes it; a line the
   walker refuses `REFUSED` in the walker's sentence; any other line
   `REFUSED` naming it; where the section ends; the sub-heading that holds
   prose and no table. No paragraph is appended narrating the header rule,
   the rounds or this reframe — that account is the issue's, the round
   records' and the changelog's. Its `Enforced by:` line names the cases that
   hold the statement and drops the retired one. `templates/sdd-spec.md`'s
   comment under the table says the same in the template's voice, edited
   where it stands.
7. **⬜ 4.** The lead, limit 5 and the `Enforced by:` line of §*What neither
   check can read* name one reader. Limit 5 keeps its fact — the helper's
   hash does not move, the diff does not show its line — and says how the
   named reader sees it: the warden, reading a caller's change, opens the
   lines of the helpers whose value it changes. `tests/test_a_reader_declares_its_input_class.py`'s
   module docstring item 5 says the same. `agents/warden.md` §*Role* gains
   one sentence telling the warden to do it, so the document names a reader
   that is told rather than hoped for — the registry's own limit 1 says the
   warden reads the diff's `Reads:` lines, and nothing in `agents/warden.md`
   or `skills/code-review/` says so today (read 2026-10-13: `grep -n
   'Reads:'` over both finds nothing).
8. **⬜ 5.** The recorder module's line 108 says what the gate does with a
   missing record since #836: not measured where the suite failed, existence
   alone on the ledger arm, and a green run still seals. The module's
   `Reads:` line (`unknown passed`, restored by #904) is unchanged.
9. **The records.** `seal/ledger/1791852611-….md`: test-held rows for the
   refusal, hashed rows for the three sentences, and the `Re-read ·` row for
   #835's D1 that the registry document's edit owes, written by
   `--reverify --into`; after the reframe, F1 reworded to the sub-heading's
   one predicate, F3 replaced by S9–S11's rows, R1 and R2 re-hashed on the
   rewritten lines, a row for S12, and S1–S3 and M1 re-checked against the
   redesigned reader — the fragment is this item's own and is edited in
   place. `changelog.md` under `### Fixed`, rewritten in place to what ships.
   `overview.md` from `templates/sdd-overview.md`. `phases/phase-N.md` per
   phase.

### Out

- Removing the direction word from the grammar, a checker over direction
  words, or a rule that every direction word be held by a test (P1).
- The 21 other `Reads:` lines #835 shipped and the recorder's `unknown
  passed` (#904, shipped in 0.21.0 as the true word).
- The `Removes from` cutoff's value, and requiring the section below it.
- The `cut` set: a refused line is still cut from the name half, as every
  line under the heading is today, because the refusal already names it.
- Reading prose under the section tolerantly (a guess-class reader; §*The
  judgment* 3).
- `CONTRIBUTING.md`'s *A frame that names what it removes* bullet, which
  cites the document and needs no new sentence.
- `README.md` and `README.ko.md`: neither mentions `## Removes` (grep,
  2026-10-13), so the agent-set description does not move. `agents/framer.md`
  and `agents/smith.md` mention the section as rows or a `nothing` line,
  which stays true.
- The two shipped frames that carry prose under the section (`1791382684`,
  `1791781864`): not live, not read, not edited.
- `hooks/config.py`: not edited by this item. `gfm_table`'s body, its
  docstring and its `Reads:` line are #871's and the census's
  (`tests/undeclared_readers.txt` holds `hooks/config.py#gfm_table@0f0796e9`;
  a docstring edit here would move that hash and owe a declaration two
  branches would write differently). The header's line is re-found through
  the module's own `table_cells`, as #871's writer re-finds it
  (`seal.py#with_row`), not through a new return value of the walk.
- A fifth pass of the oracle for the `## Removes` header. The walker reads a
  header as a tuple to equal and a width; a three-cell header already takes
  a pass (the pact-review table), so the pass would enumerate the same shapes
  again under another name, and `tests/test_one_table_walker_reads_what_gfm_renders.py`
  is a file #871 is already editing.
- The `nothing — <why>` line stays one line. A wrapped reason is refused at
  its second line, as at ac5c6ac7, and the refusal names the sub-heading as
  the home for the rest. A paragraph reading was weighed (`plan.md`
  §*Alternatives considered*).
- The `cut` set's reach: the body is cut from the name half and the lines
  under a sub-heading are not, as the orchestrator's M1 amendment decided.
- A fourth patch to the header rule, round 3's paste-ready fix included. The
  rule leaves rather than being corrected (`plan.md` §*Alternatives
  considered*).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 · an off-shape line is refused naming it | Given a live frame whose `## Removes` holds a valid row and, beside it, a bullet naming a unit that still stands / When the records arm reads it, unrequired and required alike / Then one `REFUSED` at `spec.md:<n>` names the line and says a line under `## Removes` is a table row or `nothing — <why>`, and where prose goes; the row beside it still reads `STANDING` or silent by its own rule; the run exits 2 | `tests/test_a_record_states_what_the_tree_has.py`, a new case parametrised over the bullet, a prose line, a capitalised `Nothing — …` line, and a wrapped second line of a `nothing` reason; **seen red** against 39a315a5's code (today: no finding unrequired, and `has an empty` required); green at the head |
| S2 · the shapes that belong there are not refused | Given a section holding the header row, the rule row, a blank line, an HTML comment, a fenced block and a `nothing — <why>` line / Then no finding | the same module: the existing `test_a_quoted_section_is_not_read` and `test_the_nothing_line_names_its_reason` still pass, and a new case pins the blank line and the comment |
| S3 · a required section with only an off-shape line | Given `Removes from` binds the frame and the section holds a bullet alone / Then the section is refused as empty, in today's words, and the bullet is refused naming it | the same module, one case, both findings asserted |
| S4 · the four words are true read through | Given the four `Reads:` lines, every direction word `refused` and `removes_section`'s class word `guess` / Then the one direction an unknown line of the section ends is `REFUSED` — the walker's sentence, the off-shape refusal or the sub-heading's — at `removal_findings`, which `file_claims` and `check_records` return; the two helper docstrings say so | read, the warden's: the diff of `removes_section` and `removal_findings`; `git diff --stat origin/release/v0.21.1 -- skills/evidence-check/scripts/evidence_check.py` shows hunks in those two units, in the twin's lift and in the header constant only; `bin/evidence-check .` names no `check_records` or `file_claims` anchor as DRIFTED |
| S5 · the registry names one reader and tells it | Given `docs/the-reader-registry.md` §*What neither check can read* / Then its lead, limit 5 and `Enforced by:` line name the warden, and limit 5 says the warden opens the helpers a changed caller feeds; `tests/test_a_reader_declares_its_input_class.py:30`'s item 5 says the same; `agents/warden.md` §*Role* carries the sentence | read; `git grep -n "does not show its line" -- docs tests agents` prints nothing; `bin/fold-check --root .` exit 0 (the `Enforced by:` targets exist, the ceiling holds) |
| S6 · the recorder says what the gate does | Given `specseal_pytest_record.py` / Then its line 108's clause says a missing record is not measured where the suite failed and existence alone on the ledger arm, and `the strict side` is gone from the module | read; `git grep -n "the strict side" -- skills` prints nothing; `bin/test -q -p no:cacheprovider tests/test_the_recorder_writes_what_its_process_ran.py tests/test_a_reader_declares_its_input_class.py` exit 0 |
| S7 · the records are written and the removals read as gone | Given the fragment, the changelog fragment and `overview.md` exist / Then `bin/evidence-check --strict .` exits 0: the three `## Removes` rows below find no line, the D1 `Re-read ·` row clears the registry document's drift, every test-held row resolves | executed at the last phase's head |
| S8 · the gate's four requirements are in the pull request | the test seen red (S1), the direction (block more; a wrong deny is one named line to move, a wrong allow is a removal nobody checked), the prompt budget (zero), the `Reads:` lines and this `## Removes` | read in the PR body by the orchestrator |
| S9 · the walker's refusals reach the frame | Given a live frame whose body holds, one shape per case: a `\| - \| - \| - \|` row under a body row; a repeated `\|---\|---\|---\|` under a body row; a two-cell row; the header directly under `## Removes`; a prose line directly under the last row; a `\|` line after a blank line below the table / Then each is one `REFUSED` at the frame quoting the line in the walker's own sentence, the rows above the stop are still read (`STANDING` where one names a standing unit), nothing below the stop is refused a second time, and the run exits 2 | `tests/test_a_record_states_what_the_tree_has.py`, one parametrised case; **seen red** against ac5c6ac7's reader, where the first two shapes pass in silence (round 3's 🟡 1) and the others are refused in other words or not at all |
| S10 · a sub-heading of the section holds prose and no table | Given `### Why these rows` under the table, holding prose that names a gone unit with the marker on its line, a foreign `\| Before \| After \|` table with its delimiter row and one body row, and a row naming a standing unit / Then every `\|` line under the sub-heading is `REFUSED` naming it — header, delimiter and body rows alike — the prose is read by the name half and not refused, and a table in the frame's next level-2 section is read as the rest of the frame is | the same module: `test_a_table_row_under_a_sub_heading_of_removes_is_refused` re-pinned, its ids extended with the foreign table whose header and delimiter row are now refused (**seen red** at ac5c6ac7, where both pass); `test_a_table_in_the_next_section_is_no_strayed_row` unchanged and green |
| S11 · the table is headed as the template writes it | Given a body whose table is headed `\| What \| Where \| Why \|` over a delimiter row and rows / Then the walker holds no table there, each `\|` line of it is `REFUSED` naming the header the section's table takes, and a required frame is refused as holding no table in today's words | the same module, one case, **seen red** at ac5c6ac7, where the rows are read as removals |
| S12 · the plugin's copy and the vendored copy read the section alike | Given the shapes of S1–S3 and S9–S11 / Then `removes_section` through `gfm_table` and through the vendored twin hand back the same six values on every shape with no fence, comment or HTML line in it, and on a shape that carries one the twin refuses where the plugin reads and never reads where the plugin refuses | `tests/test_evidence_check.py`, one case beside `test_the_vendored_config_rule_agrees_with_the_shared_one` and in its mechanism; #871's config case still green over the lifted twin |
| S13 · the retired rule is gone and the documents state the current one | Given the head / Then the header pin and the two sets the heuristic kept are not in the tree; `docs/the-reader-registry.md`'s statement and `templates/sdd-spec.md`'s comment carry no sentence about a header known by its rule row and no paragraph narrating the rounds; the `Enforced by:` line resolves | read; `git grep -n "rule row directly follows" -- docs templates skills tests` prints nothing; `bin/fold-check --root .` exit 0; `bin/evidence-check --strict .` exit 0 with the three reframe rows of `## Removes` below silent |

## Data & interfaces

- `skills/evidence-check/scripts/evidence_check.py#removes_section` — at
  ac5c6ac7 `(present, cut, rows, nothing, other, strayed)`; the shape stays
  so `removal_findings` changes nowhere in what it unpacks, and what fills it
  changes. The body (heading to first sub-heading) goes to the table walker
  as text with the marker blanked; its rows come back as `(line number,
  cells)` and are offset to the file's numbering; the header's line is
  re-found as the first of the walker's shown lines whose `table_cells`
  equal the template's header, the delimiter row is the line under it; `other` is
  every claim line of the body that is none of those and no `nothing` line;
  `strayed` is every `|` claim line between the first sub-heading and the
  next level-2 heading. How a walker refusal rides back — a seventh value, or
  a tagged entry of `other` — is the work's (W3). Only `removal_findings`
  calls it (grep, 2026-10-13).
- `#removal_findings` — one `REFUSED` per walker sentence at the frame,
  quoting the line; the off-shape detail rewritten to name the header the
  table takes and the sub-heading for prose; the sub-heading detail
  rewritten to *a sub-heading of `## Removes` holds prose and no table*;
  round 1's ⬜ 3 wording — a wrapped `nothing` reason told to move "after the
  table" where there is none — fixed in the same pass. Every detail is text a
  person reads (§14) and is pinned whole.
- The walker and its twin. `hooks/config.py#gfm_table(text, header)`,
  reached the way `config_rule` reaches the module — one more attribute of
  the same load, no new loader — and, in `evidence_check.py`, #871's
  `vendored_config_rows` with its header lifted into a parameter and its
  rows returned as `(line number, cells)` the way `gfm_table` returns them,
  `vendored_config_rows` becoming a projection of it that keeps `(index,
  item, value)` for its callers. The two names the build adds, beside
  `REMOVES_HEADING`, are quoted here rather than stated, because neither is
  in the tree until phase 4:

  ```
  vendored_table(text, header) -> (rows, refusals)
  REMOVES_HEADER = ("Removes", "Coordinate", "Where it lands, or why it can go")
  ```

  The twin declares its `Reads:` line as #871 wrote it, with the header as
  a parameter.
- `docs/the-reader-registry.md` — two statements edited (§*A frame names
  what its work removes*, §*What neither check can read*); one `Enforced by:`
  line gains a node id. The document is 180 lines against the 1,000 ceiling.
- `templates/sdd-spec.md` — the HTML comment under the `## Removes` table.
- `agents/warden.md` §*Role* — one sentence.
- `tests/test_a_reader_declares_its_input_class.py` — the module docstring's
  item 5; no case changes.
- `skills/verify/scripts/pytest_record/specseal_pytest_record.py:108` — one
  clause of the module docstring.
- Ledger anchors this work moves: #835's D1 row in `seal/releases/0.21.0.md`,
  anchored on `docs/the-reader-registry.md`'s title heading (hash `129aa589`
  at 39a315a5); one `Re-read ·` row in this item's fragment. No released row
  anchors `removes_section` or `removal_findings` (grep over
  `seal/releases/*.md` and `seal/ledger.md`, 2026-10-13); the nine released
  anchors on the recorder file name its `Recorder` class and four hook
  functions, not the module docstring, and do not move.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the recorder's clause saying the gate reads a missing record as *the strict side* | `skills/verify/scripts/pytest_record/specseal_pytest_record.py#"1), and no record, which the gate reads as no record -- the strict side."` | replaced on the same line by what the gate does since #836: not measured where the suite failed, existence alone on the ledger arm (⬜ 5) |
| limit 5's clause that a caller-staled helper's line is one the warden's diff does not show, as the last word on who reads it | `docs/the-reader-registry.md#"warden reads does not show its line."` | the fact stays in limit 5 and is followed by how the warden reads it: opening the lines of the helpers a changed caller feeds (⬜ 4) |
| the same clause mirrored in the registry test module's docstring | `tests/test_a_reader_declares_its_input_class.py#"and the diff the warden reads does not show its line."` | reworded with limit 5, so the module's item 5 and the document's say the same thing |
| the header heuristic's pin — a header is the row a rule row follows | `tests/test_a_record_states_what_the_tree_has.py#test_a_header_is_the_row_a_rule_row_follows` | the walker knows a header by construction and `tests/test_one_table_walker_reads_what_gfm_renders.py` holds it to cmark-gfm; the shapes the pin's ids built become ids of S9 and S10 |
| the reader's own sentence stating the header rule | `skills/evidence-check/scripts/evidence_check.py#removes_section>"the row a rule row directly follows whatever it reads, and its rule row"` | the docstring says the table is read through the walker, which has no header rule of its own to describe |
| the template's grounds for refusing a row under the sub-heading | `templates/sdd-spec.md#"sub-heading is refused, because only the table above it is read as"` | reworded in place: a sub-heading of the section holds prose and no table |

### Why these rows

The silent drop inside `removes_section` is no unit, sentence or pin and has no coordinate; the refusal replaces it in place. Each row is read whole-line by `text_regions`, so it stands `STANDING` while its clause is in the tree and reads as gone once the clause is rewritten. The first three rows were gone at phase 1. The three rows added at the reframe read `STANDING` from the reframe's commit until phase 4 lands: this item has been live for the records arm since phase 3 wrote its fragment, so the arm reads a claim of absence the build has not made true yet, which is the arm doing its job on a redesign named before it is built. The two sets the header heuristic kept are names inside one unit and have no coordinate; the retired pin above stands for them.

## Open questions → questions.md

`questions.md` holds the residue: P1 and P2 are the owner's and do not block
the build, M1 and M2 are measured at the release gather, W1 and W2 were the
first build's and W3 and W4 are the redesign's.

Framed 2026-10-13 by framer, before the build.
Reframed 2026-10-13 by framer, after round 3.
