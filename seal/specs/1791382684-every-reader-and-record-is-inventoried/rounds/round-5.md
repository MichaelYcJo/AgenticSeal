# 1791382684-every-reader-and-record-is-inventoried — review round 5

| Field | Value |
|---|---|
| Target SHA | 97c910d5bdaddf61aece9018c465857883978d37 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #901 |
| Broad gate | not yet |
| Fixes checked by | round-6 |
| Fix range | `6945a4741ed4b26624b1f45033dfcce5ee61865b..76f500a13665ce0ac68910d979b6173012a94468`, 1 commit |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1 (the registry's new direction sentence makes the recorder module's shipped `unknown passed` false), 🟡 2 (a helper's line staled by a caller's change is a limit the registry does not state) |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 5 of #834, the redesign's verifying round, target 97c910d5. It was asked to inherit round 4's verdicts and check each fix in 602fb87b..9ceba9a3 — above all the direction definition now in `docs/the-reader-registry.md`: that it is the inventory's meaning, unambiguous, consistent with #835's spec and with every `Reads:` line already on the release branch, with the document's `Enforced by:` lines and fold markers intact — and whether the changelog's second bullet under `### Added` reads true, then the rest of the item fresh. The owner's choice to withdraw the backfill was not to be reopened.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | the new direction sentence makes the recorder module's shipped `unknown passed` false: its own docstring says the gate reads the missing record as the strict side, so read through it is `refused`; #835 wrote the line, inventory part 5 row 46 reads it the same way, and the changelog says #835 adopted the definition | `skills/verify/scripts/pytest_record/specseal_pytest_record.py:16` | **fixed** `76f500a1` | fixed at 76f500a1 — read first against the code: with the gate's two variables set and the record unwritable, the module writes nothing and warns, and `broad_gate.py`'s `NO_RECORD_AT_HEAD` and `NO_RECORD` print the file as not measured, the strict side; so under the registry's direction the recorder's module line is `unknown refused`, and its paragraph now follows the input to that verdict. The edit is to the module docstring, so it drifted no ledger row (`evidence-check .` read only #835's D1, from finding 2). `overview.md` §*Why this work exists* and `spec.md` §*Removes* now name this docstring line and the test module's docstring (finding 3) as the branch's only code differences from the release branch, and the changelog bullet says the recorder declares `refused` under the definition instead of claiming #835 adopted it. The class: the reviewer read all 27 `Reads:` lines on the release branch beside their units and found this one alone; the 27 are 22 class lines and 5 `nothing` lines, and the `reader_registry.py` lines that say `passed` (`bindings`, `k1_call`, `k1_calls`, `module_body_calls`) were read again here: an unlisted call ends with a `nothing` left standing, which is `passed` under the settled meaning too; `:18-19` argue from the body; `:105-108` follow the input to the gate; `broad_gate.py` `NO_RECORD_AT_HEAD`; `git log -S"unknown passed"` gives dae101a; 26 of the 27 sampled lines read the same under both sentences |
| 🟡 2 | a helper's line goes stale when only a caller changes, with no hash moved and no line in the diff, and §*What neither check can read* does not name it | `docs/the-reader-registry.md:159` | **fixed** `76f500a1` | fixed at 76f500a1 — `docs/the-reader-registry.md` §*What neither check can read* limit 5 now says a helper's line goes stale when only a caller changes, with no hash moved and no line in the warden's diff; the count stays seven. #835's D1 drifted, was read against the document (each statement bold with one `Enforced by:` line; `bin/fold-check --root .` exit 0, 19 documents, none over the ceiling) and re-stamped in place by `evidence-check --reverify --checked 2026-10-12 --ledger` that fragment. The test module's docstring item 5 carries the same sentence (finding 3); the section's own close: "each is the warden's reading of the diff at review"; the census rule asks only a changed unit; the paste-ready text passes the registry tests and `fold-check`, and drifts D1 (probes) |
| ⬜ 3 | the enforcing test module's docstring still states the direction in the old words | `tests/test_a_reader_declares_its_input_class.py:5` | answered | corrected at `76f500a1`: `tests/test_a_reader_declares_its_input_class.py`'s module docstring states the direction as where an input the unit does not understand ends, read through to the decision it feeds, and its item 5 takes finding 2's sentence; "what it does with an input it does not understand"; the docstring names the doc as the rule's home |
| ⬜ 4 | the changelog bullet says "now defines" and "had kept getting wrong" about a document and lines no release reader had | `seal/specs/1791382684-every-reader-and-record-is-inventoried/changelog.md:12` | answered | corrected at `76f500a1`: the changelog's second bullet describes the definition as a 0.21.0 reader meets it, drops "now defines" and "had kept getting wrong", and names the recorder's `refused`; `git cat-file -e v0.20.0:docs/the-reader-registry.md` fails; the document was added by dae101a in this release; the 189 lines never shipped |
| ⬜ 5 | §*Removes*, §*Data & interfaces* and §*The direction word, settled* say the item changes no rule sentence of the registry and keeps the definition in `spec.md`; acceptance row `spec.md:326` exits 1 at HEAD | `seal/specs/1791382684-every-reader-and-record-is-inventoried/spec.md:341` | answered | corrected at `76f500a1`: `spec.md` §*Removes* names the one rule sentence the item replaces and the recorder's line; §*Data & interfaces* names the item's sentences in the registry; §*The direction word, settled* points at `docs/the-reader-registry.md` and says no line the inventory's rows wrote is in the tree; the acceptance row diffs `7608d82c ef8fb33c`, which exits 0; `survivor-check`: 2 removed sentences, none standing; `git diff --quiet 7608d82c HEAD` exit 1, `7608d82c ef8fb33c` exit 0 |
| ⬜ 6 | "94 … opened by no later round" rests on round 3's probe alone; `plan.md:103` states one count as "at most 65" and "at least 65" | `seal/specs/1791382684-every-reader-and-record-is-inventoried/spec.md:164` | answered | corrected at `76f500a1`: `spec.md` says round 3 opened 95 bodies and left 94 outside its union, and that how many of those round 2 had opened is not counted; `plan.md:103` states the count once as 65; `rounds/round-3.md` probe row, "outside the union"; `rounds/round-2.md` probes read 17 groups and 42 flagged units against code |
| ⬜ 7 | PR #901's title and body do not mention the registry sentence the branch ships | PR #901 body | answered | corrected on the pull request by the orchestrator: PR #901's body is the orchestrator's to edit, and nothing in the tree changes for it; `gh pr view 901`; `git diff --name-only origin/release/v0.21.0 HEAD` names `docs/the-reader-registry.md` |
| 🟢 | round 4's finding 1 is closed — PR #901's title and body no longer announce the backfill, the census shrink or phase 4 | PR #901 title | confirmed | `gh pr view 901` at this round: the title says the backfill is withdrawn, and the body says the owner chose withdrawal |
| 🟢 | round 4's finding 2 is closed for what it asked — the definition lives in `docs/`, the fold marker and `Enforced by:` line are untouched, and D1 was re-stamped against the new text | `docs/the-reader-registry.md:31` | confirmed | the diff changes the paragraph's prose only; `evidence-check .` 0 drifted at the head; `fold-check` 19 documents, 0 over; D1's claim names bold statements and `Enforced by:` lines, which the edit did not touch; the live fragment is re-stamped in place, as `docs/the-evidence-ledger.md` prescribes; the new text's own consequences are 🟡 1 and 🟡 2 |
| 🟢 | round 4's ⬜ 3 is closed in `plan.md` and `overview.md` | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md:103` | confirmed | the recall ground and both splits are stated; the residue is ⬜ 6 |
| 🟢 | round 4's ⬜ 4 is closed for the five sentences it named | `seal/specs/1791382684-every-reader-and-record-is-inventoried/spec.md:327` | confirmed | census row, survivor row, `overview.md` 9, 23, 32 and `spec.md` 339 all read true at the head; the missed member of the class is ⬜ 5 |
| 🟢 | round 4's ⬜ 5 is closed — the handoff's state row names PR #901 and the reframe, and decision 2 carries a dated supersession note with its own text unchanged | `seal/specs/1791382684-every-reader-and-record-is-inventoried/handoff.md:39` | confirmed | the diff of `handoff.md` |
| 🟢 | round 4's ⬜ 6 is closed — the changelog names the inventory's full path and the tag it is read at after retire | `seal/specs/1791382684-every-reader-and-record-is-inventoried/changelog.md` | confirmed | the diff; the bullet's other words are ⬜ 4 |
| 🟢 | round 4's ❓ is answered on the record — Q1 and #835's Q7 carry the owner's answer as the orchestrating session relayed it | `seal/specs/1791382684-every-reader-and-record-is-inventoried/questions.md` | confirmed | the record was checked, not the conversation; the spawn prompt says not to reopen the choice; #835's Q7 answer matches `docs/the-reader-registry.md` §*The census*, "The census need not empty on a schedule" |
| 🟢 | the withdrawal is still exact for code — `.py` files and the census equal the release branch's; the diff now also reaches `docs/`, #835's ledger fragment and #835's `questions.md`, each the fix's and accounted for | `tests/undeclared_readers.txt` | confirmed | `git diff --quiet origin/release/v0.21.0 HEAD -- '*.py' tests/undeclared_readers.txt` exit 0; `git diff --name-only` outside the item's directory names exactly those three files; no ledger fragment of the item; one `###` heading |

## Paste-ready fixes

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
```
tests/test_a_reader_declares_its_input_class.py:5-6 — replace
"the class of input it reads and
what it does with an input it does not understand"
with
"the class of input it reads and
where an input it does not understand ends, read through to the decision it feeds"

and, if 🟡 2 lands, give item 5 of the same docstring the sentence 🟡 2 adds.
```
```
changelog.md, second bullet — replace with

- **The reader registry says where a `Reads:` line's direction is read
  (#834).** In `docs/the-reader-registry.md`, the direction word names where
  an input the unit does not understand ends, followed to the decision its
  value feeds, so a helper's direction is read at its callers and not on its
  own body. It is the meaning the inventory's `Unknown` column was settled
  on, after a reading of the helper's body alone kept giving the wrong word.
```
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

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `hooks/commitgate.py:144` | round 1's 🟡 1 — fixed |
| round-1 | `skills/evidence-check/scripts/correction_check.py:746` | round 1's 🟡 2 — fixed |
| round-1 | `hooks/cmdline.py:339` | round 1's 🟡 3 — fixed |
| round-1 | `hooks/commit-review-gate.py:686` | round 1's ⬜ 4 — answered |
| round-1 | `seal/specs/1791382684-every-reader-and-record-is-inventoried/questions.md` | round 1's ⬜ 5 — answered |
| round-1 | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md` | round 1's ⬜ 6 — answered |
| round-1 | the 44 changed `.py` files | round 1's 🟢 — confirmed |
| round-1 | `tests/undeclared_readers.txt` | round 1's 🟢 — confirmed |
| round-2 | `skills/evidence-check/scripts/correction_check.py:780` | round 2's 🟡 1 — fixed |
| round-2 | `hooks/routing.py:415` | round 2's 🟡 2 — fixed |
| round-2 | `skills/verify/scripts/unverified_check.py:882` | round 2's 🟡 3 — fixed |
| round-2 | `seal/specs/1791382684-every-reader-and-record-is-inventoried/survivors.md` | round 2's ⬜ 5 — answered |
| round-2 | `hooks/cmdline.py:340` | round 2's 🟢 — confirmed |
| round-3 | `hooks/cmdline.py#_name_at` | round 3's 🟡 1 — deferred |
| round-3 | `skills/evidence-check/scripts/evidence_check.py#cell_index` | round 3's 🟡 2 — deferred |
| round-3 | the 15 `.py` files of `062e31e4..d0541ae4` | round 3's 🟢 — confirmed |
| round-4 | PR #901 title | round 4's 🟡 1 — answered |
| round-4 | `docs/the-reader-registry.md:31` | round 4's 🟡 2 — fixed |
| round-4 | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md:103` | round 4's ⬜ 3 — answered |
| round-4 | `seal/specs/1791382684-every-reader-and-record-is-inventoried/spec.md:327` | round 4's ⬜ 4 — answered |
| round-4 | `seal/specs/1791382684-every-reader-and-record-is-inventoried/handoff.md:39` | round 4's ⬜ 5 — answered |
| round-4 | `seal/specs/1791382684-every-reader-and-record-is-inventoried/changelog.md` | round 4's ⬜ 6 — answered |
| round-4 | `.github/workflows/hygiene.yml:259` | round 4's 🟢 — confirmed |
| round-4 | `seal/specs/1791382684-every-reader-and-record-is-inventoried/spec.md` | round 4's 🟢 — confirmed |
| round-4 | the 44 restored `.py` files | round 4's 🟢 — confirmed |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
