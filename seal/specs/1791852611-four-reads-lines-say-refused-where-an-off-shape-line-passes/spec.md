# Feature Specification: four `Reads:` lines say refused where an off-shape `## Removes` line passes (#905)

<!-- seal/specs/1791852611-four-reads-lines-say-refused-where-an-off-shape-line-passes/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate.
Framed by `specseal:framer` on Fable 5.1 for #905, for release 0.21.1, at
39a315a5 on `fix/905-four-reads-lines-say-refused-where-an-off-shape-line-passes`
(based on `release/v0.21.1`). Nobody is asked mid-run: what the tree could
answer is answered here, and what it could not is a row of `questions.md`
with a default the plan is built on. -->

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

### In

1. **The refusal.** Under a `## Removes` heading in a live frame, every claim
   line (`claim_lines`: outside fences and HTML comments) that is not blank,
   not a table row (header row and rule row included) and not a line
   beginning `nothing` is `REFUSED` at its line number, naming the line and
   the two shapes the section takes, and saying where prose goes. Required
   and unrequired frames alike, beside a row or alone. Exit 2, as every
   `REFUSED` in the records arm is. The existing refusal of a required
   section that is absent or holds no row and no `nothing` line stays as it
   is, in its words.
2. **The four words stay `refused`, and their paragraphs say so.**
   `removes_section`'s docstring describes what it hands back now;
   `removal_findings`'s docstring gains the sentence that an off-shape line
   in a present section is refused naming it. `file_claims` and
   `check_records` are not edited: their words are true read through once the
   helper refuses, and the ten released anchors on them (six on
   `check_records` and four on `file_claims`, in `seal/releases/*.md`) then
   owe no re-read.
3. **The rule's statement.** `docs/the-reader-registry.md` §*A frame names
   what its work removes*, first statement, gains one sentence saying an
   off-shape line is refused naming it, and its `Enforced by:` line gains the
   new test's node id. `templates/sdd-spec.md`'s comment under the table says
   that nothing else sits under the heading and where prose goes.
4. **⬜ 4.** The lead, limit 5 and the `Enforced by:` line of §*What neither
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
5. **⬜ 5.** The recorder module's line 108 says what the gate does with a
   missing record since #836: not measured where the suite failed, existence
   alone on the ledger arm, and a green run still seals. The module's
   `Reads:` line (`unknown passed`, restored by #904) is unchanged.
6. **The records.** `seal/ledger/1791852611-….md`: test-held rows for the
   refusal, hashed rows for the three sentences, and the `Re-read ·` row for
   #835's D1 that the registry document's edit owes, written by
   `--reverify --into`. `changelog.md` under `### Fixed`. `overview.md` from
   `templates/sdd-overview.md`. `phases/phase-N.md` per phase.

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

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 · an off-shape line is refused naming it | Given a live frame whose `## Removes` holds a valid row and, beside it, a bullet naming a unit that still stands / When the records arm reads it, unrequired and required alike / Then one `REFUSED` at `spec.md:<n>` names the line and says a line under `## Removes` is a table row or `nothing — <why>`, and where prose goes; the row beside it still reads `STANDING` or silent by its own rule; the run exits 2 | `tests/test_a_record_states_what_the_tree_has.py`, a new case parametrised over the bullet, a prose line, a capitalised `Nothing — …` line, and a wrapped second line of a `nothing` reason; **seen red** against 39a315a5's code (today: no finding unrequired, and `has an empty` required); green at the head |
| S2 · the shapes that belong there are not refused | Given a section holding the header row, the rule row, a blank line, an HTML comment, a fenced block and a `nothing — <why>` line / Then no finding | the same module: the existing `test_a_quoted_section_is_not_read` and `test_the_nothing_line_names_its_reason` still pass, and a new case pins the blank line and the comment |
| S3 · a required section with only an off-shape line | Given `Removes from` binds the frame and the section holds a bullet alone / Then the section is refused as empty, in today's words, and the bullet is refused naming it | the same module, one case, both findings asserted |
| S4 · the four words are true read through | Given the four `Reads:` lines unchanged / Then the one direction an off-shape line ends is `REFUSED` at `removal_findings`, which `file_claims` and `check_records` return; the two helper docstrings say so | read, the warden's: the diff of `removes_section` and `removal_findings`; `git diff --stat origin/release/v0.21.1 -- skills/evidence-check/scripts/evidence_check.py` shows hunks in those two units only; `bin/evidence-check .` names no `check_records` or `file_claims` anchor as DRIFTED |
| S5 · the registry names one reader and tells it | Given `docs/the-reader-registry.md` §*What neither check can read* / Then its lead, limit 5 and `Enforced by:` line name the warden, and limit 5 says the warden opens the helpers a changed caller feeds; `tests/test_a_reader_declares_its_input_class.py:30`'s item 5 says the same; `agents/warden.md` §*Role* carries the sentence | read; `git grep -n "does not show its line" -- docs tests agents` prints nothing; `bin/fold-check --root .` exit 0 (the `Enforced by:` targets exist, the ceiling holds) |
| S6 · the recorder says what the gate does | Given `specseal_pytest_record.py` / Then its line 108's clause says a missing record is not measured where the suite failed and existence alone on the ledger arm, and `the strict side` is gone from the module | read; `git grep -n "the strict side" -- skills` prints nothing; `bin/test -q -p no:cacheprovider tests/test_the_recorder_writes_what_its_process_ran.py tests/test_a_reader_declares_its_input_class.py` exit 0 |
| S7 · the records are written and the removals read as gone | Given the fragment, the changelog fragment and `overview.md` exist / Then `bin/evidence-check --strict .` exits 0: the three `## Removes` rows below find no line, the D1 `Re-read ·` row clears the registry document's drift, every test-held row resolves | executed at the last phase's head |
| S8 · the gate's four requirements are in the pull request | the test seen red (S1), the direction (block more; a wrong deny is one named line to move, a wrong allow is a removal nobody checked), the prompt budget (zero), the `Reads:` lines and this `## Removes` | read in the PR body by the orchestrator |

## Data & interfaces

- `skills/evidence-check/scripts/evidence_check.py#removes_section` — today
  `(present, cut, rows, nothing)`; it gains the off-shape lines as
  `[(line number, text)]`, in whatever shape the work chooses (W1). Only
  `removal_findings` calls it (grep, 2026-10-13).
- `#removal_findings` — one more `REFUSED` per off-shape line, graded as
  `REFUSED_STATUS` is, at `<shown>:<number>`. Its detail text is new text a
  person reads (§14): it names the line, the two shapes, and where prose
  goes.
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

The silent drop inside `removes_section` is no unit, sentence or pin and has no coordinate; the refusal replaces it in place. Each row above is read whole-line by `text_regions`, so it stands `STANDING` at 39a315a5 and reads as gone once the clause is rewritten; the work item is live for the records arm only once its ledger fragment exists, which the plan puts in the last phase.

## Open questions → questions.md

`questions.md` holds the residue: P1 and P2 are the owner's and do not block
the build, M1 is measured again at the release gather, W1 and W2 are the
work's.

Framed 2026-10-13 by framer, before the build.
