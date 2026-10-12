# 1791382684-every-reader-and-record-is-inventoried — review round 6 report

Round 6 is the run's last round: round 5 spent the one reopening, so this
record ends the run whatever it finds. Target 52444be3 (round 5's closing
commit), base `origin/release/v0.21.0` at 34fc36e9, fix range
`6945a474..76f500a1` and the record correction 9ae17fdb. The owner's choice to
withdraw the backfill is settled and is not reopened here. Rounds 4 and 5 were
read for coordinates; their verdicts are re-derived below.

## Summary

1. **Round 5's finding 1 is not closed, and its fix made a true line false
   (🟡 1).** Round 5 read the recorder's missing record as "the strict side"
   and changed the recorder module's word from `passed` to `refused`. At the
   head the gate does not refuse on a missing record. A run whose suite
   passes still seals, and its ledger arm reads the cited tests for existence
   alone (#836). A failing suite was already refused by its exit code, and the
   missing record only changes how its files are named. So the release
   branch's `unknown passed` was the true word under the settled direction,
   and the line, its paragraph, the changelog's last sentence and two record
   sentences now say otherwise.
2. **Four release-branch lines are `mixed` read through, not `refused`
   (🟡 2).** `removes_section` drops a `## Removes` line that is neither a
   table row nor a `nothing` line. That line is refused only where a cutoff
   requires the section and nothing else is in it. Beside a row, or in a frame
   no cutoff binds, it passes unread. The three callers that hand the section
   on say `refused` too. Round 5 read these lines and named the recorder's as
   the one disagreement.
3. **Round 5's other six findings are closed for what each asked.** The
   limit-5 sentence is in the document and the test module, #835's row D1
   reads OK at its new hash, and the spec's sentences and acceptance rows read
   true. The branch differs from the release branch in exactly two `.py`
   files, each a module docstring.
4. **The rest are corrections (⬜ 3 to ⬜ 6).** Two statements of the
   direction still use the withdrawn words. Limit 5's new sentence and the
   section's own lead name different readers. A recorder sentence that misled
   round 5 predates #836. The round-5 record counts 27 lines where the
   registry's parser counts 26.

## Findings from reading, then execution

### 🟡 1 · The recorder's `unknown refused` is false: the gate seals a run whose record could not be written

Round 5's finding 1 claimed `passed` was false under the settled direction.
Its fix, 76f500a1, wrote at `skills/verify/scripts/pytest_record/specseal_pytest_record.py:16-22`:

- `Reads: owned — the two variables above, which the broad gate sets; unknown refused`
- "Where the gate set them and the record cannot be written, the gate reads
  the missing record as not measured -- the strict side, as below -- so an
  input the recorder cannot use ends refused at the verdict it feeds."

Read through to the decision, as `docs/the-reader-registry.md:31` asks, the
recorder's value is the record, and the gate reads it in three places:

- **The verdict.** `broad_gate.py` builds `failures` from each check's own
  `check.failed` and seals when the list is empty. A missing record changes
  no check's exit.
- **The ledger arm (#836, 23f5977).** The gate hands `evidence_check.py` the
  record directory and key. Where no session carries the key,
  `existence_line` prints "test rows were read for existence alone" and the
  arm passes. Executed: `--strict` with an empty record directory exits 0 at
  the head. `tests/test_the_seal_is_taken_once_by_the_sealer.py::test_a_seal_over_existence_alone_says_so`
  pins it as "The run still seals", and it passes here.
- **The failure form.** Only under a failing suite does `NO_RECORD_AT_HEAD`
  or `NO_RECORD` name a file "not measured". The verdict was already
  `NOT SEALED` from the suite's exit.

Nothing raises, stops, or refuses on the missing record. On a green run the
seal stands, with one line saying what was not read. Under the definition
that is `passed`. At most it is `mixed`, if one reads the "not measured" word
as a refusal. It is never `refused` alone. The phrase round 5 built on,
`:111` "which the gate reads as no record -- the strict side", was written by
#825 (6de64c1) before #836 made the ledger arm read the record (⬜ 5).

The same claim stands in four more places:

- `changelog.md:18-19`: "The broad gate's pytest recorder declares
  `unknown refused` under it: a record it cannot write is read by the gate as
  not measured."
- `overview.md:9-11` and `spec.md` §*Removes* say the registry's definition
  "made false" the recorder's word.

This matters for the reason round 5 gave for its own finding 1. The release
would ship a registry definition and one of its own declarations that
disagree, and a changelog line stating the false one. It is a finding inside
a line the run's own fix wrote. The reopening bound says no later record may
close on a fix, so the verdict below is a home. Rung 1 still fits, because
the branch owns the line. The orchestrator chooses between the diff with no
round record and an issue.

### 🟡 2 · `removes_section` and its three callers say `refused` where an off-shape line passes

`skills/evidence-check/scripts/evidence_check.py#removes_section` declares
`Reads: owned — the section's lines, on the lines claim_lines reads, by the template's shape; unknown refused`.
The template (`templates/sdd-spec.md` §*Removes*) has a table or one
`nothing — <why>` line. A line in the section that is neither is input
outside the template's shape. `removes_section` adds its number to the cut
set and keeps it in no list. `file_claims` then skips it for names too.

Where it ends, by execution on the clone's `removal_findings`:

| The section | No cutoff binds it | A cutoff requires it |
|---|---|---|
| `Nothing — …` (capital N) | no finding | `REFUSED`, the section reads as empty |
| a bullet naming a unit that still stands | no finding | `REFUSED`, the section reads as empty |
| a table row naming the same unit | `STANDING` | `STANDING` |

A bullet beside a valid row passes even where the section is required,
because `rows` is not empty. So an off-shape line is refused in one place and
passed in another, which the registry calls `mixed`. Read through, the same
path reaches `removal_findings`, `file_claims` and `check_records`, whose
lines also end `refused`.

These are #835's lines on the release branch, not this run's. Round 5 read
them and found "this one alone"; the fixes table carried that. The body
reading gives `passed` or `mixed` too, so this is not a disagreement between
the two definitions. It is a false line under either one. One reading would
save it: that prose in the section is understood rather than unknown.
`spec.md` §*Removes* of this very item carries two prose paragraphs under its
`nothing` line, which shows prose is written there. But the template allows
only the table or the one line, and the bullet case shows a claim of absence
read by nobody.

### ⬜ 3 · Two statements of the direction still use the withdrawn words

Round 5's ⬜ 3 named the class: every statement of the direction. Two members
remain:

- `changelog.md:7`, the first bullet, describes the inventory's column as
  "what it does with input it does not understand". The next bullet says the
  column was settled on where the input ends. A release reader meets both.
- `spec.md:234-236` says `docs/the-reader-registry.md` "carries [the
  inventory's meaning] as *what the unit does with input it does not
  understand*". The registry has not carried that phrase since 4d2c56c6.

A third is smaller. `spec.md` §*Data & interfaces* calls the definition "its
one sentence there". The definition at `docs/the-reader-registry.md:31-36` is
two sentences.

### ⬜ 4 · Limit 5's new sentence and its section's lead name different readers

Since 76f500a1, limit 5 says a caller-staled helper's line is one "the diff
the warden reads does not show". The section's lead says "the reviewer is the
reader of each". Its `Enforced by:` line says "each is the warden's reading of
the diff at review". The document now names, for one limit, a reader that by
its own sentence cannot see the limit. Behaviour is unchanged, and the fix
drifts #835's row D1 again.

### ⬜ 5 · The recorder sentence round 5 built on predates the ledger arm

`specseal_pytest_record.py:111`: "no record, which the gate reads as no
record -- the strict side." That was true when #825 wrote it, because the
record fed only the failure form. Since #836 the ledger arm also reads it,
and there a missing record is the lenient side. This is release-branch text.
It is a separate finding from 🟡 1 because it is at a different depth: 🟡 1 is
the line the run wrote, and this is the sentence that misled it.

### ⬜ 6 · The round-5 record counts 27 release-branch lines; the parser counts 26

`rounds/round-5-fixes.md` row 1 and `rounds/round-5.md` say "the 27 are 22
class lines and 5 `nothing` lines". `tests/reader_registry.py`'s
`declarations`, run over every module and unit docstring of the population
at 34fc36e9 and at the head, gives 26: 21 class lines and 5 `nothing` lines.
This spawn's prompt carried the 27 as well.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | round 5's fix made the recorder module's line false: `unknown refused`, and a paragraph saying an unusable input "ends refused at the verdict it feeds"; the gate seals a green run whose record could not be written, its ledger arm reading cited tests for existence alone, so round 5's finding 1 is not closed and the release branch's `passed` was the true word; the changelog's last sentence, `overview.md:9-11` and `spec.md` §*Removes* repeat the claim | `skills/verify/scripts/pytest_record/specseal_pytest_record.py:16` | deferred #904 | the run is capped by the reopening bound, so no later record closes on a code change; rung 1 fits, as round 5's own fix wrote the line, and the orchestrator chooses the diff with no round record or a new issue; `broad_gate.py` seals when no check failed and a missing record changes no check's exit; `evidence_check.py --strict` with an empty record directory exits 0 with the existence line (probe); the case pinning "The run still seals" passes; option A of the paste-ready, run in the clone: 122 passed |
| 🟡 2 | `removes_section` declares `unknown refused`, but a `## Removes` line that is neither a table row nor a `nothing` line is refused only where a cutoff requires the section and it holds nothing else, and passes unread beside a row or below the cutoff: `mixed` read through; `removal_findings`, `file_claims` and `check_records` carry the same path and also say `refused` | `skills/evidence-check/scripts/evidence_check.py#removes_section` | deferred #905 | #835's lines on the release branch, not this run's; probe on the clone's `removal_findings`: a capital `Nothing` line and a bullet naming a standing unit give no finding unrequired and `REFUSED` required, a table row gives `STANDING`; `required and not (rows or nothing)` is the one refusal; the template allows a table or one `nothing` line |
| ⬜ 3 | two statements of the direction still use the withdrawn words: the changelog's first bullet ("what it does with input it does not understand") and `spec.md:234-236`, which says the registry carries that phrase; §*Data & interfaces* calls a two-sentence definition "one sentence" | `seal/specs/1791382684-every-reader-and-record-is-inventoried/changelog.md:7` | open | a correction to the run's paperwork; `git grep` for "does not understand" outside the rounds; `docs/the-reader-registry.md:31-36` |
| ⬜ 4 | limit 5's new sentence says the warden's diff does not show a caller-staled helper's line, while the section's lead and its `Enforced by:` line name the warden's reading of the diff as the reader of each limit | `docs/the-reader-registry.md:161` | deferred #905 | the lead, limit 5 and the `Enforced by:` line, read together; a rewording drifts #835's row D1 |
| ⬜ 5 | the recorder docstring's "which the gate reads as no record -- the strict side" predates #836's ledger arm, which reads a missing record as existence alone; round 5's finding 1 and its fix rested on it | `skills/verify/scripts/pytest_record/specseal_pytest_record.py:111` | deferred #905 | release-branch text: `git log -S` puts it at 6de64c1 (#825) and the existence fallback at 23f5977 (#836) |
| ⬜ 6 | the round-5 record and fix table count 27 release-branch `Reads:` lines, 22 of them class lines; the registry's parser counts 26, 21 and 5 | `seal/specs/1791382684-every-reader-and-record-is-inventoried/rounds/round-5-fixes.md:2` | open | a correction to the run's paperwork; `declarations` run over every module and unit docstring of the population at 34fc36e9 and at the head (probe) |
| 🟢 | round 5's finding 2 is closed — limit 5 names a helper staled by its caller, the count stays seven, and #835's row D1 reads OK at its new hash | `docs/the-reader-registry.md:161` | confirmed | the sentence is in the document and in the test module's item 5; `evidence-check .` exit 0, 0 drifted; `fold-check` 19 documents, 0 over; the section's lead is ⬜ 4 |
| 🟢 | round 5's ⬜ 3 is closed — the test module docstring states the settled direction and its item 5 mirrors limit 5 | `tests/test_a_reader_declares_its_input_class.py:5` | confirmed | the diff; the module passes with three others, 153 |
| 🟢 | round 5's ⬜ 4 is closed for the words it named — "now defines", "had kept getting wrong" and "which #835 adopted" are gone from the second bullet | `seal/specs/1791382684-every-reader-and-record-is-inventoried/changelog.md:12` | confirmed | the diff; the bullet's last sentence is finding 1's, the first bullet's words are ⬜ 3 |
| 🟢 | round 5's ⬜ 5 is closed — §*Removes*, §*Data & interfaces* and §*The direction word, settled*'s close read true of the tree, and the acceptance row diffs 7608d82c against ef8fb33c | `seal/specs/1791382684-every-reader-and-record-is-inventoried/spec.md:331` | confirmed | `git diff --quiet 7608d82c ef8fb33c` exit 0; `survivor-check` 4 removed sentences, none standing; "made false" in §*Removes* is finding 1's |
| 🟢 | round 5's ⬜ 6 is closed — `spec.md` says round 3 left 94 outside its union and round 2's overlap is not counted, and `plan.md:103` states the count once as 65 | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md:103` | confirmed | the diff; 37 of 65 is the stated 57% |
| 🟢 | round 5's ⬜ 7 is closed — PR #901's body names the registry's direction sentence | PR #901 body | confirmed | `gh pr view 901` at 52444be3: "`docs/the-reader-registry.md` now states the direction word by the inventory's meaning" |
| 🟢 | 9ae17fdb's correction is true — the branch differs from the release branch in two `.py` files, each inside a module docstring | `seal/specs/1791382684-every-reader-and-record-is-inventoried/overview.md:9` | confirmed | `git diff --name-only origin/release/v0.21.0 HEAD -- '*.py'` names the recorder module and the registry test module; both hunks lie inside the module docstring |
| 🟢 | the spec's acceptance rows run green at the head | `seal/specs/1791382684-every-reader-and-record-is-inventoried/spec.md:329` | confirmed | census equals the release branch's, 1,583 lines; guard diff empty; no ledger fragment; one `###` heading; `evidence-check`, `correction-check`, `survivor-check`, `unverified-check` each exit 0 |
| 🟢 | 21 of the 26 release-branch `Reads:` lines read true under the settled direction; the recorder's release-branch `passed` reads true too, so only the four of finding 2 do not | `tests/reader_registry.py` | confirmed | each read beside its unit and, for a helper, its callers: the registry's own units (a malformed line or census line is refused by the test that calls them), `cutoff_row` and `frozen_from` (refusals their callers exit on), `tests/conftest.py`'s ceiling (raises), `hooks/worktree-guard.py#main` (`mixed`, argued in its paragraph) |

## Paste-ready fixes

### 🟡 1

```
Option A — the release branch's line was the true one; return to it.

git -C <worktree> checkout origin/release/v0.21.0 -- skills/verify/scripts/pytest_record/specseal_pytest_record.py

changelog.md, second bullet — delete its last two sentences:
  "The broad gate's pytest recorder declares `unknown refused` under it: a
  record it cannot write is read by the gate as not measured."

overview.md §Why this work exists — replace
  "so the branch's code is the release branch's but for two docstrings: the
  pytest recorder's module line, whose direction word the registry's settled
  definition made false (round 5 🟡 1), and the registry test module's own
  statement of the rule (round 5 ⬜ 3)."
with
  "so the branch's code is the release branch's but for one docstring, the
  registry test module's own statement of the rule (round 5 ⬜ 3). Round 5
  changed the pytest recorder's direction word to `refused`; round 6 found
  that the gate seals a run whose record could not be written, so the release
  branch's `passed` stands and the change was taken back."

spec.md §Removes — replace
  "but for two docstrings, the pytest recorder's direction word (round 5 🟡 1)
  and the registry test module's statement of the rule (round 5 ⬜ 3)"
with
  "but for one docstring, the registry test module's statement of the rule
  (round 5 ⬜ 3)"

Verify (option A applied in the clone this round, 122 passed, exit 0):
bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py tests/test_the_recorder_writes_what_its_process_ran.py
git diff --name-only origin/release/v0.21.0 HEAD -- '*.py'   # names the test module alone

Option B — keep a paragraph that reads through, with the true word.
specseal_pytest_record.py:16-22 — replace with

Reads: owned — the two variables above, which the broad gate sets; unknown passed

With either variable absent, or a directory it cannot write, no record is
written and the run goes on, and the gate does not refuse on the missing
record: a run whose suite passed still seals, its ledger arm reading the
cited tests for existence alone and saying so, and a failing suite names its
files as not measured.

and :111 "which the gate reads as no record -- the strict side" with
"which the gate reads as no record: not measured where the suite failed,
existence alone on the ledger arm" (⬜ 5); the changelog's last sentence
becomes "The broad gate's pytest recorder declares `unknown passed` under it:
the gate seals a run whose record could not be written, reading its cited
tests for existence alone."; overview.md and spec.md name the recorder's
paragraph, not its word.
```

### 🟡 2

```
skills/evidence-check/scripts/evidence_check.py#removes_section — replace the line's last word
  ...by the template's shape; unknown refused
with
  ...by the template's shape; unknown mixed

and add under it:

    A line in the section that is neither a table row nor a `nothing` line
    is read by no rule: where a cutoff requires the section and nothing else
    is in it, `removal_findings` refuses the section as empty; beside a row,
    or in a frame no cutoff binds, it passes unread.

The same word, read through, on the three units that hand the section on:
removal_findings, file_claims, check_records — `unknown refused` → `unknown mixed`.

Each edit moves the unit's hash: run bin/evidence-check . and re-read any
row it reports DRIFTED. Verify:
bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py tests/test_a_record_states_what_the_tree_has.py

Or justify: refuse an off-shape line in a present section (a code change to
`removes_section`, which makes `refused` true), or state in
docs/the-reader-registry.md §A frame names what its work removes that prose
under the section is read as prose, and keep `refused`.
```

### ⬜ 3

```
changelog.md:7 — replace
  "what it does with input it does not understand"
with
  "where input it does not understand ends"

spec.md §The direction word, settled — replace
  "which `docs/the-reader-registry.md` carries as *what the unit does with
  input it does not understand*."
with
  "which `docs/the-reader-registry.md` now states in the inventory's words."

spec.md §Data & interfaces — replace "its one sentence there is the
direction's definition" with "its two sentences there are the direction's
definition"
```

### ⬜ 4

```
docs/the-reader-registry.md, limit 5 — append to the sentence 76f500a1 added:
  "; the warden reading a caller's change reads the lines of the helpers
  whose value it changes."
Then re-stamp #835's row D1 in place:
evidence-check --reverify --checked <date> --ledger seal/ledger/1791384152-a-reader-declares-its-input-class.md
```

## Executed probes

| What was run | Result |
|---|---|
| `git clone --no-local` of the worktree into the round's scratch directory, checked out at 52444be3, `origin/release/v0.21.0` set to 34fc36e9 | clone at the target |
| `git diff --name-only origin/release/v0.21.0 HEAD -- '*.py'` | `skills/verify/scripts/pytest_record/specseal_pytest_record.py`, `tests/test_a_reader_declares_its_input_class.py`; each hunk inside the module docstring |
| `git diff --name-only origin/release/v0.21.0 HEAD`, outside the item's directory | the two above, `docs/the-reader-registry.md`, #835's ledger fragment and #835's `questions.md` |
| `git diff --quiet 7608d82c ef8fb33c -- '*.py' tests/undeclared_readers.txt` | exit 0 |
| `git diff --quiet origin/release/v0.21.0 HEAD -- tests/undeclared_readers.txt`; `wc -l` at both | exit 0; 1,583 and 1,583 |
| `git diff --stat origin/release/v0.21.0...HEAD -- hooks/worktree-guard.py` | empty |
| `ls seal/ledger/` for the item's id; `grep -c '^### '` on `changelog.md` | none; 1 |
| `bin/evidence-check .` | exit 0; 8,415 ok, 0 drifted; records 0 refused, 0 drifted |
| `bin/correction-check --range origin/release/v0.21.0...HEAD` | exit 0; 2 merges, no marker dropped; no released ledger file changed |
| `bin/survivor-check --range origin/release/v0.21.0...HEAD` | exit 0; 4 removed sentences, none standing |
| `bin/unverified-check --baseline origin/release/v0.21.0` | exit 0 |
| `bin/fold-check --root .` | exit 0; 185 statements in 19 documents, 0 over 1,000 lines |
| `bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py tests/test_a_rider_reaches_its_file.py tests/test_no_real_identifiers.py tests/test_one_word_one_meaning.py` | 153 passed, exit 0 |
| `evidence_check.py --strict --suite-record` an empty directory `--suite-key` an unused key, over the clone | exit 0; prints "test rows were read for existence alone: no session under … carries the key …" (🟡 1) |
| `bin/test -q -p no:cacheprovider -p no:xdist` on `tests/test_the_seal_is_taken_once_by_the_sealer.py::test_a_seal_over_existence_alone_says_so`, `tests/test_a_ledger_row_is_held_by_its_test.py::test_a_record_with_no_session_under_the_key_names_the_key`, `tests/test_the_recorder_writes_what_its_process_ran.py::test_a_record_it_cannot_write_leaves_pytest_its_own_exit_under_w_error` | 4 passed, exit 0 (🟡 1) |
| 🟡 1's option A applied in the clone; the registry and recorder modules; then the file restored with `git checkout HEAD` | 122 passed, exit 0; the `.py` diff then names the test module alone |
| a probe script running `tests/reader_registry.py`'s `declarations` over every module and unit docstring of the population, at 34fc36e9 and at the head | 26 declarations each: 21 class lines, 5 `nothing` (⬜ 6) |
| a probe script calling the clone's `removal_findings` on three one-section frames, unrequired and required, in a scratch git repository | as the table under 🟡 2 |
| `git grep` for statements of the direction, rounds and inventory excluded | `docs/the-reader-registry.md:31`, the test module, `changelog.md:7` and `:14`, `spec.md:236` and `:238` (⬜ 3) |
| `git log -S` on the recorder's "the strict side" and on evidence_check's "existence alone" | 6de64c1 (#825) and 23f5977 (#836) (⬜ 5) |
| `gh pr view 901` | draft; head 52444be3; the body names the registry's direction sentence |
| the broad gate: full suite, lint, typecheck | not yet — the sealer's, once the orchestrator has settled 🟡 1 and 🟡 2; this round ends the run |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
| 🟡 1 · the recorder's `unknown refused`, written by round 5's fix, is false | the diff with no round record (rung 1, the branch wrote the line) or a new issue; the reopening bound forbids a fix-closing record | the orchestrator of this run, who commissioned round 5's fix |
| 🟡 2 · `removes_section` and three callers say `refused` where an off-shape line passes | a new issue in milestone `release: 0.21.0` or 0.21.1, grounded in `docs/the-reader-registry.md` §*The four classes* | the orchestrator of this run, who files it; whoever next changes those units declares `mixed` or makes `refused` true |
| ⬜ 4 · limit 5 and its section's lead name different readers | with 🟡 2's issue, as one edit of the registry document | the orchestrator of this run, who files it |
| ⬜ 5 · the recorder's "the strict side" predates #836 | with 🟡 1, where option B takes it | the orchestrator of this run |

## Regression tests to plant

None. A direction word is the reviewer's to read (`docs/the-reader-registry.md`
§*What neither check can read*, limit 1). The behaviour 🟡 1 rests on is
already pinned: "The run still seals" in
`tests/test_the_seal_is_taken_once_by_the_sealer.py::test_a_seal_over_existence_alone_says_so`.

## Facts for the evidence ledger

None from this item, which has no fragment. ⬜ 4's fix would drift #835's D1,
to be re-stamped in place as rounds 4 and 5 did.

Needs a fix: yes — 🟡 1 (round 5's fix wrote the recorder's `unknown refused`, and the gate seals a run whose record could not be written), 🟡 2 (`removes_section` and three callers declare `refused` where an off-shape `## Removes` line passes unread)
Loses a record or crashes: no

## Proof

Opened in the worktree at 52444be3 or in the clone of it:

- `seal/specs/1791382684-every-reader-and-record-is-inventoried/`: `rounds/round-4.md`, `rounds/round-5-report.md`, `rounds/round-5-fixes.md`, `rounds/round-5.md`, `changelog.md`, `overview.md`, `spec.md` (§*The reframe* to §*The direction word, settled*, the acceptance table, §*Data & interfaces*, §*Removes*), `plan.md:103`; inventory lines by grep
- the whole diff `6945a474..76f500a1`, and 9ae17fdb, 22a47261, 52444be3 by stat and diff
- `docs/the-reader-registry.md` lines 1–175; `docs/review-chain-spec.md` lines 41–200 and 377–598
- `skills/verify/scripts/pytest_record/specseal_pytest_record.py` lines 1–200
- `skills/verify/scripts/broad_gate.py` lines 230–245, 2095–2300, 2790–2830, 3190–3300, 3505–3560, 3580–3700, 3825–3870, and the panel's use of `run`
- `skills/evidence-check/scripts/evidence_check.py` lines 2300–2460, 4380–4470, 6025–6130, 6240–6420, 6885–6910
- `skills/code-review/scripts/chain_check.py` lines 428–483
- `tests/reader_registry.py` lines 150–530; `tests/conftest.py` lines 1–30, 488–572, 938–992; `tests/test_a_reader_declares_its_input_class.py` lines 60–90 and 430–455; `tests/test_a_ledger_row_is_held_by_its_test.py` lines 1053–1092; `tests/test_the_seal_is_taken_once_by_the_sealer.py` lines 3910–3950
- `hooks/worktree-guard.py` lines 2790–2815; `templates/sdd-spec.md` §*Removes*; `CONTRIBUTING.md` lines 262–276
