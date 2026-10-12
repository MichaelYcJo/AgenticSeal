# 1791382684-every-reader-and-record-is-inventoried — review round 5 report

Round 5 is the redesign's verifying round. Target 97c910d5 (round 4's closing
commit), base `origin/release/v0.21.0` at 34fc36e9, fix range
`602fb87b..9ceba9a3`. The owner's choice to withdraw the backfill whole is
taken as given. Rounds 1 to 4 were read for coordinates; round 4's verdicts
are re-derived below.

## Summary

1. **Round 4's six findings are closed for what each asked.** PR #901's
   title and body no longer announce the backfill. The direction definition
   now lives in `docs/the-reader-registry.md`. The fold marker and the
   `Enforced by:` line are untouched, #835's row D1 is re-stamped to the new
   text, and `evidence-check` reads 0 drifted. Every `.py` file and the
   census still equal the release branch's.
2. **The new sentence calls one shipped `Reads:` line false (🟡 1).** The
   recorder's module body, `specseal_pytest_record.py:16`, declares
   `unknown passed`, and its reason is a reading of its own body. The same
   docstring says the gate reads a missing record as "the strict side".
   Read through to the decision, as the sentence now says, that is
   `refused`. #835 wrote this line, and inventory part 5 row 46 reads the
   unit the same way. So the release would ship a definition and a line that
   disagree, and a changelog saying #835 adopted that definition.
3. **The sentence creates a staleness path its own document does not
   name (🟡 2).** If a helper's direction is read at its callers, a change to
   a caller makes the helper's line false. The helper's hash does not move,
   and the diff the warden reads does not contain the line. *What neither
   check can read* is the section that exists so nobody meets this by
   surprise, and it does not list it.
4. **The rest are corrections (⬜ 3 to ⬜ 7).** A second statement of the
   direction in the old words. A changelog bullet that describes history no
   release reader can see. Spec sentences that the fix's own docs edit made
   false. A sentence from round 4's own paste-ready that still overclaims.
   A PR body that does not mention the sentence the branch now ships.
5. **The changelog heading is right, though not for the reason the fix
   gave.** `docs/the-reader-registry.md` does not exist at `v0.20.0`. #835
   added it in this same release (dae101a), so a release-note reader meets
   the whole document as new. `### Added` is true for that reader. A
   `### Changed` entry would describe a change from a definition they never
   had.

## Findings from reading

### 🟡 1 · The new direction sentence makes a shipped `Reads:` line false, and #835 wrote it

`docs/the-reader-registry.md:31` now says a direction is read "through to the
decision the unit's value feeds … A helper's direction is therefore read at
its callers, not on its own body". The changelog bullet calls this "the
inventory's meaning, which #835 adopted".

I sampled every `Reads:` line on the release branch: 27 lines in 5 files
(probes). Twenty-six give the same word under the old sentence and under the
new one. Examples: `k1_call` passes an unlisted call, its caller then lets a
`nothing` stand, and its own docstring argues `passed` from that. The
`cutoff_row` family hands back a refusal its callers exit 2 on.

The one that does not agree is the recorder's module body:

- `skills/verify/scripts/pytest_record/specseal_pytest_record.py:16`
  declares `Reads: owned — the two variables above, which the broad gate
  sets; unknown passed`.
- `:18-19` gives the reason on the unit's own body: "With either variable
  absent no session records and nothing is written, which is why an input it
  cannot use passes rather than stops the run."
- `:105-108`, in the same docstring, follows the input to where it ends: a
  directory it cannot write gives "no record, which the gate reads as no
  record -- the strict side". `broad_gate.py`'s `NO_RECORD_AT_HEAD` and
  `NO_RECORD` print that case as `not measured`.
- `git log -S` puts the line at dae101a, #835's own squash. Inventory part 5
  row 46 reads the unit `passed` with the note "No key → no file → gate reads
  'no record', the strict side".

Under the sentence this item shipped, the input ends refused at the gate's
verdict, so the line's word is `refused`. It is not `passed`. One inventory
row and one of #835's own lines therefore read the direction on the body,
which is the reading `spec.md` §*The direction word, settled* withdrew.

This matters because the release would carry a registry document whose
definition calls one of the release's own declarations false. The changelog
would also tell readers the definition is what #835 adopted, when #835's own
line on this unit follows the other reading. The sentence itself is sound,
and the line is what needs to change. The item says "the branch's code is
the release branch's" (`overview.md`, `spec.md` §*Removes*), so fixing the
line means amending those rows too. That is one docstring line on a
sibling's unit and not the backfill, so it does not reopen the owner's
choice. The other answer is an issue that carries the line, named in
`overview.md` §*Not done*.

### 🟡 2 · A helper's line goes stale when only a caller changes, and the limits section does not say so

`docs/the-reader-registry.md` §*What neither check can read* says "Seven
things pass both checks, and the reviewer is the reader of each", and closes
with "each is the warden's reading of the diff at review". Limit 5 is "A
stale line: a reader redesigned from `guess` to `owned` keeps its old line
until somebody moves it".

The new sentence makes a helper's direction depend on its callers. When a
caller changes what it does with the helper's value, the helper's line
becomes false and nothing records it:

- the helper's body is unchanged, so its hash does not move and the census
  rule ("a listed unit owes nothing until it changes") never asks;
- the diff the warden reads is the caller's, and the helper's line is not in
  it.

That is not a redesign of the reader, and the reviewer the section names as
the reader of each limit cannot see it. The class rule already had this
property for a unit that parses text its caller handed it, and the
direction rule now has it in writing. This section is the doc's statement of
its own edge, so the gap is a defect in the one behaviour-bearing edit this
item ships. The paste-ready text below keeps the count at seven. It passes
the registry tests and `fold-check` (probes). It drifts #835's row D1 again,
which is re-stamped in place the way round 4's fix did it.

### ⬜ 3 · The direction is stated a second time, in the old words

Round 4's 🟡 2 was about where the definition lives. The class is every
statement of it. `docs/` now carries the settled one. The module docstring
of `tests/test_a_reader_declares_its_input_class.py:5-6`, the case that
enforces the rule, still says the line states "what it does with an input it
does not understand". Those are the words round 4 found closer to the
withdrawn body-local rule. The docstring names `docs/the-reader-registry.md`
as the rule's home, so this is a correction. Its item 5 also mirrors the
doc's limit 5 and should take 🟡 2's sentence if that lands. The other
statements are `tests/reader_registry.py`, which states only the grammar,
and #835's `spec.md` "The direction is the inventory's", which retires at
the fold.

### ⬜ 4 · The changelog bullet describes history a release reader cannot see

The heading is right (summary item 5). The bullet's words are not:

- "now defines the direction as …" implies an earlier definition. A
  0.21.0 reader never had one, because the document is new in this release.
- "the reading a declaration on a helper had kept getting wrong" refers to
  the 189 withdrawn lines, which never shipped. A reader looking for those
  declarations finds none.
- "This is the inventory's meaning, which #835 adopted" is the claim 🟡 1
  qualifies.

### ⬜ 5 · The fix's own docs edit made three spec sentences false, and one ⬜ 4 sentence was missed

- `spec.md` §*Removes*: "no unit, heading, rule sentence or test pin that
  stood before this item leaves the tree". The direction sentence #835
  landed has left `docs/the-reader-registry.md`, replaced by this item's.
  `survivor-check` counts 2 removed sentences in the range and none standing
  (probe), so the replacement is clean. The frame's sentence about it is
  still false.
- `spec.md` §*Data & interfaces*: "this item adds no word to it and, after
  the reframe, no line in it". The item now writes a sentence of that
  document.
- `spec.md` §*The direction word, settled* closes "the definition is here
  for whoever next writes a line". `overview.md` now points that writer at
  `docs/`.
- `spec.md:326`, acceptance row "The tree carries no line the inventory
  wrote", verifies with `git diff --quiet 7608d82c <head> …`. At HEAD that
  exits 1, because of the merge's guard files. At phase 4's commit,
  ef8fb33c, it exits 0 (probes). This is the class of round 4's ⬜ 4, which
  named five sentences and not this one.

### ⬜ 6 · Round 4's own paste-ready carried an overclaim into `spec.md:164`

The new sentence reads "Round 1 read every line beside its body; after it,
94 of the 189 were opened by no later round". The 94 come from round 3's
probe ("the 94 written units outside the union … read, bodies not opened"),
which covers round 3 alone. Round 2's probes read 17 identical-line groups
"against its units' code" and 42 flagged units, and nothing measures how many
of those are among round 3's 94. Round 4 proposed this text. The same cell
of `plan.md:103` also says "at most 65" and "at least 65" of one count. The
two bounds together mean 65, and the cell should say that once.

### ⬜ 7 · PR #901 does not mention the registry sentence the branch now ships

The title ("the inventory of every reader and record ships, and the Reads:
backfill built from it is withdrawn") and the body describe the inventory
and the withdrawal. The branch also rewrites a definition in
`docs/the-reader-registry.md`. The title becomes the squash subject and a
release-note line. The body says the full text comes before ready, so this is
a note for that write, which is the orchestrator's.

## Findings from execution

Every check in `## Executed probes` exited 0, apart from `pact-check`, which
does not apply (no `seal/pact.md`). The two proposed fixes for 🟡 1 and 🟡 2
were applied in the clone, run, and reverted. Every 🟡 and ⬜ above is from
reading. 🟡 1's divergence is a reading of the code and was not executed.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | the new direction sentence makes the recorder module's shipped `unknown passed` false: its own docstring says the gate reads the missing record as the strict side, so read through it is `refused`; #835 wrote the line, inventory part 5 row 46 reads it the same way, and the changelog says #835 adopted the definition | `skills/verify/scripts/pytest_record/specseal_pytest_record.py:16` | open | `:18-19` argue from the body; `:105-108` follow the input to the gate; `broad_gate.py` `NO_RECORD_AT_HEAD`; `git log -S"unknown passed"` gives dae101a; 26 of the 27 sampled lines read the same under both sentences |
| 🟡 2 | a helper's line goes stale when only a caller changes, with no hash moved and no line in the diff, and §*What neither check can read* does not name it | `docs/the-reader-registry.md:159` | open | the section's own close: "each is the warden's reading of the diff at review"; the census rule asks only a changed unit; the paste-ready text passes the registry tests and `fold-check`, and drifts D1 (probes) |
| ⬜ 3 | the enforcing test module's docstring still states the direction in the old words | `tests/test_a_reader_declares_its_input_class.py:5` | open | "what it does with an input it does not understand"; the docstring names the doc as the rule's home |
| ⬜ 4 | the changelog bullet says "now defines" and "had kept getting wrong" about a document and lines no release reader had | `seal/specs/1791382684-every-reader-and-record-is-inventoried/changelog.md:12` | open | `git cat-file -e v0.20.0:docs/the-reader-registry.md` fails; the document was added by dae101a in this release; the 189 lines never shipped |
| ⬜ 5 | §*Removes*, §*Data & interfaces* and §*The direction word, settled* say the item changes no rule sentence of the registry and keeps the definition in `spec.md`; acceptance row `spec.md:326` exits 1 at HEAD | `seal/specs/1791382684-every-reader-and-record-is-inventoried/spec.md:341` | open | `survivor-check`: 2 removed sentences, none standing; `git diff --quiet 7608d82c HEAD` exit 1, `7608d82c ef8fb33c` exit 0 |
| ⬜ 6 | "94 … opened by no later round" rests on round 3's probe alone; `plan.md:103` states one count as "at most 65" and "at least 65" | `seal/specs/1791382684-every-reader-and-record-is-inventoried/spec.md:164` | open | `rounds/round-3.md` probe row, "outside the union"; `rounds/round-2.md` probes read 17 groups and 42 flagged units against code |
| ⬜ 7 | PR #901's title and body do not mention the registry sentence the branch ships | PR #901 body | open | `gh pr view 901`; `git diff --name-only origin/release/v0.21.0 HEAD` names `docs/the-reader-registry.md` |
| 🟢 | round 4's finding 1 is closed — PR #901's title and body no longer announce the backfill, the census shrink or phase 4 | PR #901 title | confirmed | `gh pr view 901` at this round: the title says the backfill is withdrawn, and the body says the owner chose withdrawal |
| 🟢 | round 4's finding 2 is closed for what it asked — the definition lives in `docs/`, the fold marker and `Enforced by:` line are untouched, and D1 was re-stamped against the new text | `docs/the-reader-registry.md:31` | confirmed | the diff changes the paragraph's prose only; `evidence-check .` 0 drifted at the head; `fold-check` 19 documents, 0 over; D1's claim names bold statements and `Enforced by:` lines, which the edit did not touch; the live fragment is re-stamped in place, as `docs/the-evidence-ledger.md` prescribes; the new text's own consequences are 🟡 1 and 🟡 2 |
| 🟢 | round 4's ⬜ 3 is closed in `plan.md` and `overview.md` | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md:103` | confirmed | the recall ground and both splits are stated; the residue is ⬜ 6 |
| 🟢 | round 4's ⬜ 4 is closed for the five sentences it named | `seal/specs/1791382684-every-reader-and-record-is-inventoried/spec.md:327` | confirmed | census row, survivor row, `overview.md` 9, 23, 32 and `spec.md` 339 all read true at the head; the missed member of the class is ⬜ 5 |
| 🟢 | round 4's ⬜ 5 is closed — the handoff's state row names PR #901 and the reframe, and decision 2 carries a dated supersession note with its own text unchanged | `seal/specs/1791382684-every-reader-and-record-is-inventoried/handoff.md:39` | confirmed | the diff of `handoff.md` |
| 🟢 | round 4's ⬜ 6 is closed — the changelog names the inventory's full path and the tag it is read at after retire | `seal/specs/1791382684-every-reader-and-record-is-inventoried/changelog.md` | confirmed | the diff; the bullet's other words are ⬜ 4 |
| 🟢 | round 4's ❓ is answered on the record — Q1 and #835's Q7 carry the owner's answer as the orchestrating session relayed it | `seal/specs/1791382684-every-reader-and-record-is-inventoried/questions.md` | confirmed | the record was checked, not the conversation; the spawn prompt says not to reopen the choice; #835's Q7 answer matches `docs/the-reader-registry.md` §*The census*, "The census need not empty on a schedule" |
| 🟢 | the withdrawal is still exact for code — `.py` files and the census equal the release branch's; the diff now also reaches `docs/`, #835's ledger fragment and #835's `questions.md`, each the fix's and accounted for | `tests/undeclared_readers.txt` | confirmed | `git diff --quiet origin/release/v0.21.0 HEAD -- '*.py' tests/undeclared_readers.txt` exit 0; `git diff --name-only` outside the item's directory names exactly those three files; no ledger fragment of the item; one `###` heading |

## Paste-ready fixes

### 🟡 1

```
skills/verify/scripts/pytest_record/specseal_pytest_record.py:16-19 — replace

Reads: owned — the two variables above, which the broad gate sets; unknown passed

With either variable absent no session records and nothing is written,
which is why an input it cannot use passes rather than stops the run.

with

Reads: owned — the two variables above, which the broad gate sets; unknown refused

With either variable absent no session records and nothing is written, and
the run goes on: that is a pytest the gate did not start, and nothing reads
its record. Where the gate set them and the record cannot be written, the
gate reads the missing record as not measured -- the strict side, as below
-- so an input the recorder cannot use ends refused at the verdict it feeds.

Then, because the branch's code is no longer the release branch's:
- overview.md §Why this work exists: "so the branch's code is the release
  branch's" → "so the branch's code is the release branch's but for one
  docstring line on the recorder's module body, which the registry's settled
  direction made false (round 5 🟡 1)"
- spec.md acceptance rows that diff '*.py' against the release branch: name
  the one file as the expected difference.
- changelog.md second bullet: see ⬜ 4.

Verify (applied in the clone this round, 103 passed, exit 0):
bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py tests/test_one_word_one_meaning.py tests/test_no_real_identifiers.py

Or justify: an issue in the release milestone carrying the line above, its
answerer the orchestrator, named in overview.md §Not done; and the changelog
bullet drops "which #835 adopted".
```

### 🟡 2

```
docs/the-reader-registry.md, §What neither check can read, item 5 — append to the item

   A helper's line goes stale the same way when only a caller changes: its
   direction, and its class where it parses text a caller handed it, are
   read at its callers, so the helper's hash does not move and the diff the
   warden reads does not show its line.

The count stays seven. Then re-stamp #835's row D1 in place, as round 4 did:
evidence-check --reverify --checked <date> --ledger seal/ledger/1791384152-a-reader-declares-its-input-class.md

Verify (applied in the clone this round): bin/fold-check --root . exit 0,
19 documents, 0 over; the registry tests 103 passed; bin/evidence-check .
reports D1 DRIFTED until the re-stamp.
```

### ⬜ 3

```
tests/test_a_reader_declares_its_input_class.py:5-6 — replace
"the class of input it reads and
what it does with an input it does not understand"
with
"the class of input it reads and
where an input it does not understand ends, read through to the decision it feeds"

and, if 🟡 2 lands, give item 5 of the same docstring the sentence 🟡 2 adds.
```

### ⬜ 4

```
changelog.md, second bullet — replace with

- **The reader registry says where a `Reads:` line's direction is read
  (#834).** In `docs/the-reader-registry.md`, the direction word names where
  an input the unit does not understand ends, followed to the decision its
  value feeds, so a helper's direction is read at its callers and not on its
  own body. It is the meaning the inventory's `Unknown` column was settled
  on, after a reading of the helper's body alone kept giving the wrong word.
```

### ⬜ 5

```
spec.md §Removes — replace "no unit, heading, rule sentence or test pin that stood before this item leaves the tree" with
  no unit, heading or test pin that stood before this item leaves the tree,
  and the one rule sentence it replaces is the direction sentence of
  `docs/the-reader-registry.md`, rewritten to the settled meaning
  (`overview.md` §*Fed back into the spec*)

spec.md §Data & interfaces — replace "this item adds no word to it and, after the reframe, no line in it" with
  this item adds no word to it, and after the reframe its one sentence there
  is the direction's definition

spec.md §The direction word, settled — replace "the definition is here for whoever next writes a line on one of these units" with
  the definition is `docs/the-reader-registry.md`'s, for whoever next writes
  a line on one of these units

spec.md:326 — replace `git diff --quiet 7608d82c <head> -- '*.py' tests/undeclared_readers.txt` with
  `git diff --quiet 7608d82c ef8fb33c -- '*.py' tests/undeclared_readers.txt`
```

### ⬜ 6

```
spec.md:164 — replace "after it, 94 of the 189 were opened by no later round" with
  round 3 then opened 95 against their bodies and left 94 outside its
  union, reading those lines without their bodies; how many of the 94
  round 2 had opened is not counted

plan.md:103 — replace "against at most 65 distinct false lines among the 125" with
  against 65 distinct false lines among the 125
and "caught about 37 of the at least 65 distinct false lines" with
  caught about 37 of those 65
```

### ⬜ 7

```
# the orchestrator's act; no commit — add to PR #901's body before ready:

It also settles one sentence of `docs/the-reader-registry.md`: a `Reads:`
line's direction word names where an input the unit does not understand
ends, followed to the decision it feeds, so a helper's direction is read at
its callers.
```

## Executed probes

| What was run | Result |
|---|---|
| `git clone --no-local` of the worktree into the round's scratch directory, checked out at 97c910d5, `origin/release/v0.21.0` fetched at 34fc36e9 | clone at the target |
| `git diff --quiet origin/release/v0.21.0 HEAD -- '*.py' tests/undeclared_readers.txt` | exit 0 |
| `git diff --name-only origin/release/v0.21.0 HEAD`, outside the item's directory | `docs/the-reader-registry.md`, `seal/ledger/1791384152-a-reader-declares-its-input-class.md`, `seal/specs/1791384152-a-reader-declares-its-input-class/questions.md` |
| `git diff --quiet 7608d82c HEAD` and `7608d82c ef8fb33c`, both `-- '*.py' tests/undeclared_readers.txt` | exit 1 and exit 0 (⬜ 5) |
| `git cat-file -e v0.20.0:docs/the-reader-registry.md`; `git log --diff-filter=A` on it | not in `v0.20.0`; added by dae101a (#835) |
| `git grep` of every `Reads:` line in non-test `.py` | 27 lines in 5 files; each read beside its unit; 26 give one word under both sentences, the recorder's does not (🟡 1) |
| `git log -S"unknown passed"` on the recorder module | dae101a |
| `git grep` for other statements of the direction | `docs/the-reader-registry.md:31`, `tests/test_a_reader_declares_its_input_class.py:5-6` (⬜ 3); the rest state only the grammar |
| `bin/evidence-check .` | exit 0; 8,415 ok, 0 drifted; records 0 refused, 0 drifted |
| `bin/correction-check --range origin/release/v0.21.0...HEAD` | exit 0; 2 merges, no marker dropped; no released ledger file changed |
| `bin/survivor-check --range origin/release/v0.21.0...HEAD` | exit 0; 2 removed sentences, none still standing |
| `bin/fold-check --root .` | exit 0; 185 statements in 19 documents, 0 over 1,000 lines |
| `bin/unverified-check --baseline origin/release/v0.21.0` | exit 0 |
| `bin/pact-check` | exit 2: no `seal/pact.md` in this repository, so not applicable |
| `bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py tests/test_a_rider_reaches_its_file.py tests/test_no_real_identifiers.py tests/test_one_word_one_meaning.py` | 153 passed, exit 0 |
| 🟡 1's and 🟡 2's paste-ready text applied in the clone; the registry, one-word and identifier tests; `fold-check`; `evidence-check .`; then both files restored with `git checkout` | 103 passed, exit 0; `fold-check` exit 0, 0 over; `evidence-check` exit 1, D1 DRIFTED (content changed), as expected before a re-stamp |
| `gh pr view 901` | title and body as round 4's 🟡 1 asked; draft; no mention of the registry sentence (⬜ 7) |
| the broad gate: full suite, lint, typecheck | not yet — the sealer's, after the rounds settle; not due while 🟡 1 and 🟡 2 are open |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

## Regression tests to plant

None for 🟡 1 or 🟡 2. A direction word is the reviewer's to read
(`docs/the-reader-registry.md` §*What neither check can read*, limit 1), and
a pin on a docstring's prose would be the kind of guess the inventory
counted.

## Facts for the evidence ledger

None from this item, which has no fragment. If 🟡 2 lands, #835's D1 is
re-stamped in place. No new row is written.

Needs a fix: yes — 🟡 1 (the registry's new direction sentence makes the recorder module's shipped `unknown passed` false), 🟡 2 (a helper's line staled by a caller's change is a limit the registry does not state)
Loses a record or crashes: no

## Proof

Opened in the worktree at 97c910d5 or in the clone of it:

- `seal/specs/1791382684-every-reader-and-record-is-inventoried/`: `rounds/round-4.md`, `rounds/round-4-report.md`, `rounds/round-4-fixes.md`, `rounds/round-3.md` (probe table), `rounds/round-2.md` (probe table), `overview.md`, `routing.md`, `spec.md` (head, §*The direction word, settled*, the acceptance table, §*Data & interfaces*, §*Removes*), `changelog.md`; `inventory/1-hooks-shell.md`, `inventory/2-hooks-rest.md`, `inventory/5-verify-bin-ci.md`, `inventory/6-tests.md` by grep and their keys
- the whole diff `602fb87b..9ceba9a3`
- `docs/the-reader-registry.md`, whole
- `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment*, the paragraph on re-stamping a fragment's row in place
- `seal/specs/1791384152-a-reader-declares-its-input-class/spec.md` §*The vocabulary* (lines 200–232), its `changelog.md`
- `tests/reader_registry.py` lines 30–300; `tests/test_a_reader_declares_its_input_class.py` module docstring
- `skills/evidence-check/scripts/evidence_check.py`, the units around lines 4389, 4424, 6038–6175, 6250, 6338
- `skills/verify/scripts/pytest_record/specseal_pytest_record.py` lines 1–110
- `skills/verify/scripts/broad_gate.py` lines 2100–2185
- `hooks/worktree-guard.py` lines 2790–2815; `tests/conftest.py` lines 1–30
