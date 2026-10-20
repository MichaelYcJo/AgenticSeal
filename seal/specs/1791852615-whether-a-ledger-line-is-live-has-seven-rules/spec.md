# Feature Specification: whether a ledger or record line is live has seven rules with four failure directions (#872)

<!-- seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` §*The goal a design is chosen against — verification that runs unattended* | between two readers that catch the same defect, the one that drops a parked claim in silence is the costlier; nothing this work builds asks a person anything, and no gate's verdict moves |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | every unit this work touches carries a `Reads:` line; the frame names what it removes; the direction of every change is stated; the prompt budget is zero in every phase because no verdict moves |
| `docs/the-evidence-ledger.md` §*The fold, and what tells it from a deletion* > "A marker counts only on a live line, and one function decides what live means" | the EXCUSING direction, already stated: a marker parks on doubt, `live_lines` ANDs both readings, and the cost is a fold reported as a deletion at exit 1 |
| `docs/the-evidence-ledger.md` §*The fold, and what tells it from a deletion* > "A retirement would break every ledger row anchored inside the directory it removes" | the HOLDING direction, already stated for one reader: `settle` reads every line, fenced or commented, because a guard that reads more than the checker keeps a directory the checker would not break, which is the direction to be wrong in |
| `docs/the-reader-registry.md` §*The four classes and the line that declares one* | the grammar of the line each of the seven units gains: `Reads: <class> — <what it reads>; unknown <direction>`, the direction read through to the decision the value feeds, a helper's at its callers |
| `docs/the-reader-registry.md` §*The census: the units that stood undeclared at landing* | every one of the seven stands on `tests/undeclared_readers.txt` today; a changed unit declares and its line leaves, and the check says so |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | the `## Removes` grammar; `seal/config.md`'s `Removes from` is 1791780031, so this frame carries the section |
| `skills/evidence-check/SKILL.md` §*What counts as a claim* and the three *still read* bullets above it | how a session reads the checker's and the records arm's directions today — an unclosed fence read, a comment read, a mid-line comment read with its text — and the paragraph a pointer to the standing statement is added to |
| `skills/settle/SKILL.md` §*2. Write one standing statement per segment* | the shape of the statement this work writes into `docs/`: a bold rule, its grounds, one `Enforced by:` line, under a `<!-- specs/<id> -->` marker |
| `seal/specs/1790260566-a-row-inside-a-fence-reads-as-live/questions.md` §*Decided from the tree* D1, D2, D4, D8 | the two biases were decided there and are not re-argued here: `live_lines` is the one definition for a line that EXCUSES something and not for a line that HOLDS something; `anchored_rows` reads fenced rows on purpose; the ledger's comments stay read; `hooks/config.py` keeps its own definition on the hook path |
| #834 `inventory/4-ledger-settle-seal.md` §*Observations* (the *four rules* bullet) and rows E9, E58, S9; `inventory/5-verify-bin-ci.md` rows 72–74; `inventory/2-hooks-rest.md` row 96 | the classes and directions the inventory read for six of the seven, which the `Reads:` lines below start from |
| #867 `plan.md` §*Operational impact*, issue text 2 | the measurements this frame rests on — `quoted_lines` and `live_lines` agree on every released ledger row; `readable` would blank 46 rows across eight release files. **Read, not executed**: the probe is not in the tree, and phase 2 re-derives both figures before citing them in a ledger row |

## Scope

**The issue asks two things, and the tree answers both.** For each of the
seven readers, which consequence its failure direction protects; and whether
one rule with a stated bias can carry all seven. The answer to the second is
no, and not for symmetry's sake: the seven give three answers because they
read three different kinds of line, and each answer is tied to what the wrong
answer costs. The work is to write that rule down once where a session reads
it, to make each of the seven units say which answer it gives and why, and to
pin the seven directions in one table so a reader that changes its direction
changes a visible row.

**In.**

1. **The rule, stated once, in `docs/the-evidence-ledger.md`.** Whether a
   line is live is asked by what the line DOES, and there are three answers:

   - **A line that HOLDS something — a claim, an anchor, a rider — is read on
     doubt.** The checker's `quoted_lines` (and `unquoted`, which hashes
     through it), the records arm's `claim_lines`, `settle.py#anchored_rows`
     and the rider check's `quoted_lines`. An unclosed fence is a malformed
     file whose lines are read; a commented-out row is a parked claim and is
     read; where `hooks/blocks.py#walk` is unsure, a marker line is a rider.
     The consequence protected: a claim never leaves a ledger or a record in
     silence. The wrong answer is loud — BROKEN, a refused name, a kept
     directory, exit 2 — and a person answers it with an edit or a marker.
     Two readers in this group hide less or more than the others, each with
     its reason stated in the registry and left standing: `claim_lines` hides
     a line-start HTML comment that closes, because a record's template
     comments describe fields and a paste-ready fix is code the tree does
     not have yet (round 1 of #434, 🟡 11), and reads a mid-line comment with
     its text (Q1 (a) of 1790260566); `anchored_rows` reads a fence that
     closes, which the checker skips since #444 (D2).
   - **A line that EXCUSES or DECLARES something — a fold marker, a
     `<!-- specs/<id> -->` marker, a config row, a routing label — is parked
     on doubt.** `unverified_check.py#live_lines`, which computes both span
     readings and keeps a line only where both call it live, and
     `hooks/config.py#hidden_lines`, which keeps the fence-only reading where
     the walk is unsure. The consequence protected: nothing is excused or
     declared by a line nobody wrote live. The wrong answer is a fold reported
     as a deletion at exit 1, a fragment kept in the survivor sweep, a hook
     that says nothing or a gate that asks — each one a person sees.
   - **A line a record's rows are COUNTED on, or a closing word is searched
     on, is blanked the same way on both sides of a comparison.**
     `unverified_check.py#readable`, indices intact, an unclosed fence or
     comment blanked to the end. The consequence protected: the working tree
     and the base revision count the same table, and a hidden table is
     refused as absent by the record readers that call it (`chain_check.py`,
     `round_record.py`, `check_text`) rather than read as empty. It reads no
     ledger file in shipped code — its callers are the round records, a work
     item's `overview.md`, a `survivors.md` passed to `--exempt` and the
     review-history guard — so the 46 rows it would blank are the price of a
     merge this frame refuses, not a defect in the tree.

   The statement goes in §*The fold, and what tells it from a deletion*,
   beside the two direction statements already there, or in a section of its
   own if the builder judges the fold section the wrong home; it opens bold,
   carries this work item's marker, and its `Enforced by:` line names the
   direction table test of item 3. `skills/evidence-check/SKILL.md` §*What
   counts as a claim* gains one sentence pointing at it, so a session reading
   the skill meets the three answers rather than the two bullets.

2. **Each of the seven units declares.** A `Reads:` line in the registry's
   grammar, and one sentence in the prose naming which of the three answers
   the unit gives and what the wrong answer costs — a pointer to the statement
   above, not a second copy of it. The seven census lines leave
   `tests/undeclared_readers.txt`. The classes and directions the frame
   proposes are in §*Data & interfaces*; the builder settles each at the unit
   and records a move in the phase record.

3. **One direction table.** A test module holding one corpus of line shapes
   and, for each of the seven readers, the answer the statement says it gives
   on each shape. An adapter per reader turns its own return shape — indices,
   `(line, flag)` pairs, `(number, text)` pairs, blanked lines, named rows —
   into one question: *is the line in shape N read as holding, declaring or
   counting?* The table is the one place the seven stand side by side, so a
   change to one reader's direction is a change to a row somebody reads. The
   shapes are the ones whose answer a docstring already states (§*Data &
   interfaces*); a shape no docstring answers is not in the table, because
   the table pins stated directions and does not discover edges — the
   per-reader modules already own the edges.

4. **The released rows that cite the seven are read again.** A docstring line
   moves a unit's hash, so every released row anchored on one of the seven
   drifts. Under `Ledger frozen from` the repair is `evidence-check --reverify
   --into seal/ledger/<this id>.md --checked <date>`, each `Re-read ·` row
   read by the builder; the released files are not edited.

**Out, with the ground for each.**

| What | Why it is out | Who answers what is left |
|---|---|---|
| Merging any two of the seven | Each pair was judged, and no pair has the same consequence AND a behaviour difference worth paying for. `plan.md` §*Alternatives considered* holds the table: the checker's `quoted_lines` against the rider's (a delimiter rule against a walk; the checker ships alone in `tools/` where `hooks/blocks.py` is not beside it, Q6 of 1790260566; the released ledgers carry no fence line, P2-3, so the two differ on no row here); `claim_lines`' fence arm onto `quoted_lines` (it would recognise a closed comment inside a never-closed fence as an aside, which moves the stated judgment *read rather than drop* on a malformed record, against four released rows and no issue); `anchored_rows` onto the checker's rule (D2); `live_lines` and `hidden_lines` (D8: the hook path loads no skill module; different files, different wrong answers); `readable` onto `live_lines` (37 test modules call `readable`, `tests/test_chain_hooks.py#reader_blanking_passes` refuses a pass added or removed, and a flag is not a blanked line). No issue since 0.18.0 traces to any of the seven (#834 part 8), which is the measurement the issue itself cites as the ground for not merging | nothing left; a reader who wants a merge opens the row of the Alternatives table and overturns it there |
| `claim_lines`' positional scanner (Q1 (b) of 1790260566) | Q1 chose (a), the narrowed sentence, and (a) is built and documented in `skills/evidence-check/SKILL.md` §*A comment is an aside only where it begins a line*. (b) widens the quiet direction: a `<!--` quoted in backticks that the code-span state gets wrong drops every claim to the next `-->` in silence, and getting that state right cost `live_lines` five review rounds. The wrong answer under (a) is a loud false refusal a marker answers. No issue since reports one. This frame records the grounds; the Q1 row of that file is the owner's to tick | the repository owner, `questions.md` Q1 |
| `hooks/dispatch.py#readable` | a predicate over parsed hook JSON that shares the name and nothing else; not a line rule | nothing left |
| `tests/commonmark_oracle.py#hidden_lines` | the oracle every hook text reader is held to, not a rule of its own; it answers what a renderer hides, and the readers decide what to do where it is unsure | nothing left |
| `_liveness`, `_partner_ahead`, `_paragraph_ends_at`, `blank_fences`, `strip_comments`, `comment_scan`, `fence_spans`, `unquoted` | the parts the seven are built from; the registry reads a helper's direction at its callers, so they declare nothing this work owes and their census lines stay until they change | nothing left |
| The fence delimiter rule and the line split | one rule each since #584, #491 and #664, held equal across readers by `tests/test_unverified_rows_close.py` and `tests/test_every_reader_ends_a_line_where_gfm_does.py`; the seven already share them | nothing left |
| The other bullets of #834 part 4 §*Observations* | each is its own issue or already landed (#867, #870, #866) | the issues that hold them |
| The inventory's class and direction for any unit outside the seven | the backfill was withdrawn (#834 part 8, #901); a unit declares when it changes | the work item that changes the unit |

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 the statement | Given `docs/the-evidence-ledger.md`, when a session asks whether a line is live, then one bold statement under this work item's marker names the three answers, the readers that give each, and the consequence each protects, with one `Enforced by:` line naming the direction table test; the document stays under the 1000-line ceiling | `bin/fold-check`; `tests/test_a_folded_statement_names_what_enforces_it.py`; `tests/test_docs_line_wrap.py` |
| S2 the skill points at it | Given `skills/evidence-check/SKILL.md` §*What counts as a claim*, then one sentence says the records arm's answer is the holding one of three and names the statement | read; `tests/test_docs_line_wrap.py` |
| S3 the seven declare | Given each of the seven units, then its docstring carries one `Reads:` line in the grammar and one sentence naming its answer and the cost of the wrong one; `tests/undeclared_readers.txt` is seven lines shorter and names none of them | `tests/test_a_reader_declares_its_input_class.py` green; `evidence-check --strict .`'s records arm reads this frame's `## Removes` rows as gone |
| S4 the direction table | Given the corpus of shapes in §*Data & interfaces*, when each of the seven readers is asked of each shape through its adapter, then the answer is the one the statement states; and when one reader's answer on doubt is flipped by a mutation (an unclosed fence hidden by `quoted_lines`, a disagreement read live by `live_lines`), the table goes red naming the reader and the shape | the new module, seen red under that mutation before it is planted (`agent-contract` §15), the mutation and its output in `phases/phase-1.md` |
| S5 the released rows | Given the released rows anchored on the seven (`quoted_lines` P2-1, P2-3; `claim_lines` A4, P4-1, P4-2, R5; `anchored_rows` G3, L8, K12, K16 and their re-reads; `live_lines` R11; `readable` P1-4, G1, T2; `hidden_lines` P3-1; the rider's `quoted_lines` P5-1 where it anchors on that unit), when the docstrings change, then each drifted row gets a `Re-read ·` row in `seal/ledger/1791852615-whether-a-ledger-line-is-live-has-seven-rules.md`, read by the builder, and no released file changes | `evidence-check --strict .` exit 0 on the branch; `correction-check --range` exit 0; `git diff --stat origin/release/v0.21.1 -- seal/releases seal/ledger.md` empty |
| S6 no verdict moves | Given this repository's own tree, then `evidence-check --strict .` counts the same anchors with the same verdicts before and after, the records arm reads the same number of names and refuses the same number, and `settle --dry-run` names the same anchored rows | the three commands at the base and at the branch, their counts in `phases/phase-2.md`, labelled executed |
| S7 the measurements the issue cites | Given the released ledgers, when the two figures the issue carries are re-derived — the rows `quoted_lines` skips against the rows `live_lines` parks, and the rows `readable` would blank — then the figures in this work's ledger row are the ones read on this branch, with their moment | one probe in phase 2, `test_tmp_*`, deleted; the figures in `phases/phase-2.md` and the ledger row |

## Data & interfaces

No interface changes. No gate's verdict moves. Three artefacts:

**The `Reads:` lines the frame proposes.** The inventory's reading where it
read the unit, this frame's where it did not; the builder settles each at the
unit.

| Unit | Class | Direction | Answer | What the wrong answer costs |
|---|---|---|---|---|
| `skills/evidence-check/scripts/evidence_check.py#quoted_lines` | owned — a ledger file's lines, this repository's own writer's format | passed — an unclosed fence and a comment are read as claims | holds | a parked or malformed row is reported, never dropped |
| `skills/evidence-check/scripts/evidence_check.py#claim_lines` | guess — a record's prose | passed — an unclosed region and a mid-line comment are read | holds | a false refusal a marker answers |
| `skills/settle/scripts/settle.py#anchored_rows` | owned — every line of every ledger the checker reads | refused — a directory an unsure line anchors into is kept | holds | a kept directory, named at exit 1 |
| `.github/scripts/rider_check.py#quoted_lines` | guess — a markdown file's lines, through the walk | refused — where the walk is unsure the line is a rider, BROKEN at exit 2 if unstamped | holds | a quoted example reported as a rider |
| `skills/verify/scripts/unverified_check.py#live_lines` | guess — markdown lines under an approximated block model | mixed — a disagreement parks the line: refused at the fold (a deletion at exit 1), passed at the gather and the sweep (a marker not counted, the fragment kept) | excuses | a fold reported as a deletion |
| `hooks/config.py#hidden_lines` | guess — `seal/config.md` and `routing.md` lines, through the walk (**corrected 2026-10-13** by round 2's note 7: `seal/config.md` lines only; `hooks/routing.py#shown` reads a `routing.md`) | mixed — the hook says nothing, the gate asks | declares | nothing declared; `broad-gate` names the fence |
| `skills/verify/scripts/unverified_check.py#readable` | owned — a record's lines | passed — a hidden table reads as absent, and every record reader refuses an absent table | counts | a record refused as having no table |

**The corpus of shapes for the direction table**, each a short markdown text
holding one row or marker line in the position named, the stated answers
taken from the docstrings and the two policy statements:

1. a row inside a fence that closes;
2. a row below a fence that never closes;
3. a row inside a line-start HTML comment that closes;
4. a row below a `<!--` that never closes;
5. a row on a line that carries a mid-line `<!-- … -->` before it;
6. a row on a plain line, the control.

For each shape the table states, per reader, *read* or *not read* in the
reader's own terms: an index absent from `quoted_lines`' set, a `(number,
text)` pair present in `claim_lines`' list, a row named by `anchored_rows`,
a `True` flag from `live_lines`, a non-blank line from `readable`, an index
absent from `hidden_lines`' map, an index absent from the rider's set. A
shape whose answer for one reader no docstring states is answered by the
reader's stated bias and labelled so in the module, which is the builder's
to judge at the unit.

**The ledger fragment.** `seal/ledger/1791852615-whether-a-ledger-line-is-live-has-seven-rules.md`:
one row per statement and per new unit, the `Re-read ·` rows `--reverify
--into` writes, and the two re-derived figures with their moment.

## Rule changes

- nothing
  why: written: the three answers, in docs/the-record-layout.md *Whether a line is live is
    asked by what the line does*; overturned: the ledger's readers (5b1f6fae).

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the census line for the checker's `quoted_lines` | `tests/undeclared_readers.txt#"skills/evidence-check/scripts/evidence_check.py#quoted_lines@de284263"` | the unit declares (`docs/the-reader-registry.md` §*The census*) |
| the census line for `claim_lines` | `tests/undeclared_readers.txt#"skills/evidence-check/scripts/evidence_check.py#claim_lines@e5006cc3"` | the unit declares |
| the census line for `anchored_rows` | `tests/undeclared_readers.txt#"skills/settle/scripts/settle.py#anchored_rows@a1c9cd21"` | the unit declares |
| the census line for the rider's `quoted_lines` | `tests/undeclared_readers.txt#".github/scripts/rider_check.py#quoted_lines@b8d6b67b"` | the unit declares |
| the census line for `live_lines` | `tests/undeclared_readers.txt#"skills/verify/scripts/unverified_check.py#live_lines@ad7653a3"` | the unit declares |
| the census line for `hidden_lines` | `tests/undeclared_readers.txt#"hooks/config.py#hidden_lines@c76b94d3"` | the unit declares |
| the census line for `readable` | `tests/undeclared_readers.txt#"skills/verify/scripts/unverified_check.py#readable@4ee19967"` | the unit declares |

### Why these rows

No reader, rule sentence or test pin leaves the tree. The seven lines above
leave by the registry's own rule, and are named here so the records arm reads
each as a claim of absence from the build on rather than as a divergence
after it.

## Open questions → questions.md

Anything a planner must answer lives in questions.md, not inline — unanswered
questions buried in prose read as decided.

Framed 2026-10-13 by framer, before the build.
