# 1791382684-every-reader-and-record-is-inventoried — review round 4 report

Round 4 is the redesign's first record. Target fce23e01 (pushed), base
`origin/release/v0.21.0` at 34fc36e9. The redesign is `spec.md` §*The
reframe* and `plan.md` at 73c1145a, approved at 3ca8699d; phases 4 and 5 are
ef8fb33c, c6dda5ca, the merge c778429d, 9c228af5 and fce23e01. Rounds 1 to 3
were read for coordinates; their verdicts are re-derived below.

## Summary

1. **The withdrawal is exact, executed.** At fce23e01 the branch differs from
   `origin/release/v0.21.0` only under this work item's directory: every
   `.py` file and `tests/undeclared_readers.txt` equal the release branch's,
   no ledger fragment of the item exists, the changelog fragment holds
   `### Added` alone, and `docs/`, `CHANGELOG.md` and `seal/follow-up.md`
   carry no sentence about the backfill.
2. **Removing `survivors.md` is right for CI, executed.** The hygiene step
   hands `--exempt` to every `survivors.md` that exists, and a header-only
   file makes `survivor-check` exit 2. Without the file the check exits 0,
   both here and in CI's own run at the merge ref.
3. **The decision to withdraw the 64 single-unit-row lines holds, but on
   grounds the records state differently from the frame (⬜ 3).** Round 1
   read all 189 bodies, the 64 included. The frame says the 64 "were
   sampled, not read", and `spec.md` says 94 lines were read by nobody. What
   carries the decision is round 1's measured recall, about 57% on the class
   it was hunting.
4. **Two things still say the backfill ships.** PR #901's title and body
   still say 189 units declare and phase 4 waits (🟡 1). The title is the
   squash subject and a line of the release note. Separately, the direction
   word's settled definition lives only in a `spec.md` that retires at the
   fold, while the standing registry document reads closer to the rule the
   reframe withdrew (🟡 2).
5. **For the owner (❓).** The reframe reverses three things a person
   answered or left at a default. The first is `questions.md` Q1 (c). The
   second is the run handoff's decision 2, "0.21.0 ships … #834's build".
   The third is #835's Q7, still ⬜ at default (a) on the release branch. The
   approval that took the reversal was the orchestrating session's, under
   the automation press. The one place the frame offers the owner a say is
   "at the approval", and the owner never held that approval.

## Findings from reading

### 🟡 1 · PR #901's title would publish the withdrawn build as a release-note line

The title reads `chore: 189 units the inventory read declare what they read,
and leave the census (#834)`. The body says the build "moves those readings
into the code: 189 units … now carry the `Reads:` line … and leave its census
(1,584 lines to 1,395)", and that "Phase 4 … waits for #894 and #896".
After the reframe each of those statements is false. No line was kept, the
census is the release branch's 1,583 lines, and phase 4 is gone.

This matters beyond the draft. `.github/scripts/publish_release_note.py`
composes the release note from pull request titles ("every line is a pull
request title, a number, or a handle"), and the squash into
`release/v0.21.0` takes the title as its commit subject. The body's own
line says the full body comes before ready, but nothing in the work item
records that the *title* must change too. So the false line ships unless
someone remembers. Nothing in the item's records makes the change, and the
orchestrator holds the only write that can.

### 🟡 2 · The direction word's settled definition has no home that outlives the item

`spec.md` §*The direction word, settled* decides between two definitions.
The settled one says the direction is where an unknown input ends, read
through to the decision the unit feeds, and a helper's direction is its
callers' to read. The plan's body-local rule is withdrawn. The section
closes: "the definition is here for whoever next writes a line on one of
these units". `overview.md` §*Not done* repeats it: "`spec.md` §*The
direction word, settled* is the definition that hand applies".

But that hand arrives after the fold. `spec.md` retires with the directory
at `settle --retire`, and `overview.md` §*Fed back into the spec* says
`none`. The standing rule is `docs/the-reader-registry.md:31`: "The
direction says what the unit does with input it does not understand". Read
on one body, that is the narrower rule. Round 3's ⬜ 3 measured what the
narrower rule produces: thirteen written lines and `_name_at` disagreeing
with the inventory. `questions.md` itself says answered rows "feed back into
docs/ before this directory's work merges".

The outcome is a release whose registry document still invites the reading
this run spent a round on, while the decision against it is filed where no
later writer looks. Fix it, or justify it: either the sentence below goes
into the registry document, or an issue carries it with the registry's
owner as the answerer.

### ⬜ 3 · The withdrawal's grounds misstate what the rounds read; the decision holds on round 1's recall

- `plan.md:103`, the alternative row for keeping the 64, says: "Rounds 2
  and 3 opened a single-unit line's body only where an enumeration … selected
  it, so the 64 were sampled, not read." Round 1 read every one. Its probe
  row in `rounds/round-1.md` says "189 units, 4,268 lines of source, all
  read", and `spec.md`'s own table, row 1, says "all 189 units' bodies".
- `spec.md:164` says "94 of the 189 lines have been read against their body
  by nobody but the inventory's agent". This contradicts the same table four
  rows up. Round 3's "read, bodies not opened" describes round 3 alone.
- The split the frame argues from (64 single, 125 several) is the framer's
  probe. Round 1's own matching gave 83 single, 97 several and 9 unmatched.
  Neither is reproduced here, and the frame does not mention the other.
- "71 false" in `overview.md:24` counts findings rather than lines. At least
  three of them are a second false version of a unit already counted:
  `sections` and `flat` in round 2, and `_name_at` in round 3. Distinct
  lines number at most 68, and at most 65 from multi-unit rows.

**The decision still holds.** Round 1 did read the 64 and found 3 false.
It also read the 125 and found 37, and rounds 2 and 3 then found at least
28 more distinct ones in that class. So a full read by round 1 caught about
37 of 65, roughly 57%. A clean single-unit result from the same reader is
not a verified set, which is the frame's conclusion on a ground its text
does not state. This matters because the frame invites the owner to
overturn the choice "with this row's numbers", and two of the row's numbers
point the wrong way.

### ⬜ 4 · Sentences true at phase 4 that the merge made false at the head

The merge (c778429d) brought #894's `hooks/worktree-guard.py`, and #894
declared `hooks/worktree-guard.py#main`. Five sentences still describe the
phase-4 tree:

- `overview.md:9` and `spec.md:339` say the tree's code "is" or "returns
  to" what 7608d82c holds. At the head, `hooks/worktree-guard.py` and two
  test modules differ from 7608d82c. The code now equals the release
  branch's.
- `spec.md:327`, acceptance row "The census is the one #835 landed", says
  "Given the head … the census holds 1,584 lines". The head's census holds
  1,583, the same as the release branch's.
- `spec.md:328` names `--exempt` this item's `survivors.md` as the command
  that verifies the acceptance row. Phase 5 removed that file, so the
  command cannot run as written. `overview.md:16` records the divergence for
  the plan but not for the spec row.
- `overview.md:23` assigns the sealer "the full suite … over the build's
  tree". No build remains.
- `overview.md:32`, "The inventory's other columns (`Decides`, `Duplicates`,
  `Note`) stay", implies the `Class` and `Unknown` columns went somewhere.
  After the reframe every column stays.

### ⬜ 5 · The run handoff's state row for #834 still schedules the build

`handoff.md:39` reads: PR "none"; next step "spawn the smith for phases
1–3; phase 4 (`hooks/worktree-guard.py`) after #894 and #896 land". The PR
is #901, the build was withdrawn, and phase 4 is gone. The file is the run's
dated snapshot (last written at 7608d82c), so this is the orchestrator's to
update. The owner's decision 2 at `handoff.md:140` should not be rewritten;
it should carry a dated line saying the reframe superseded it.

### ⬜ 6 · The changelog line points at a directory that leaves `main` after the release

`changelog.md` says "The work item's `inventory/` holds 1,467 reader rows".
`spec.md` §*The inventory's fate* says `settle --retire` takes the directory
after the release, and that it is read at the tag from then on. The
`CHANGELOG.md` line outlives the directory and names no tag. This sentence
predates the reframe, and the reframe made it the item's only shipped
sentence.

### ❓ · The reframe reverses answers the owner gave, under a session's approval

Reading settles the fact. It does not settle whether the owner accepts it:

- `questions.md` Q1 was answered (c) by the owner. Its Status cell now reads
  "superseded by the reframe". That file's own rule says "the `Status`
  column is ticked by whoever answered, never by whoever asked", and the
  supersession was written by the framer.
- The outcome is close to Q1's option (d), "#834 ships as the inventory
  alone", which the owner did not pick. It also goes past (d), because the
  backfill is not deferred to 0.22.0. Units declare one by one when touched.
- `handoff.md:140`, the owner's decision 2 of 2026-10-12: "0.21.0 ships as
  … #834's build".
- #835's `questions.md` Q7 stays ⬜ at default (a), "#834 writes lines for
  the rowed units only", on the release branch. That default now describes
  a build that will not come. The file is a sibling's, outside this diff.
- `plan.md` gives the owner the way back as "the owner can overturn it at
  the approval", and `questions.md:55` says "the approver can overturn
  this". The reframe's approval line reads "by the orchestrating session
  under the owner's automation press". The owner never held the approval
  those sentences point to.

Under `automation` the session's approval is procedurally valid, and the
reframe is the chain's own exit after a second fix of a fix. Whether the
owner wants to see a reversal of their own answer before the release is the
owner's question, not the chain's.

## Findings from execution

The withdrawal, the CI behaviour and the narrow checks are in
`## Executed probes`. Every 🟡 and ⬜ above is from reading. The ❓ is
reading only.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | PR #901's title and body still say 189 units declare and leave the census and phase 4 waits; the title is the squash subject and a release-note line | PR #901 title | open | `gh pr view 901` at fce23e01; `.github/scripts/publish_release_note.py` composes the note from PR titles |
| 🟡 2 | the settled direction definition lives only in a `spec.md` that retires at the fold, while the registry document reads closer to the withdrawn body-local rule | `docs/the-reader-registry.md:31` | open | `spec.md` §*The direction word, settled*; `overview.md` §*Not done* points future writers at the retiring spec; §*Fed back into the spec* `none`; round 3 ⬜ 3 measured the disagreement |
| ⬜ 3 | the withdrawal's grounds say the 64 were "sampled, not read" and 94 lines were read by nobody; round 1 read all 189; the 64/125 split and "71 false" are stated without their caveats | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md:103` | open | `rounds/round-1.md` probe "189 units, 4,268 lines of source, all read", and 83/97/9 matching; `spec.md:164` against `spec.md`'s own round table; the decision holds on round 1's recall, about 37 of 65 |
| ⬜ 4 | five sentences describe the phase-4 tree and are false at the head after the merge: 7608d82c's code, 1,584 census lines, `--exempt` a removed file, "the build's tree", "other columns" | `seal/specs/1791382684-every-reader-and-record-is-inventoried/spec.md:327` | open | census `wc -l` 1,583 at fce23e01 and at 34fc36e9; `git diff 7608d82c HEAD -- '*.py'` names `hooks/worktree-guard.py` and two test modules; also `spec.md:328`, `spec.md:339`, `overview.md:9`, `overview.md:23`, `overview.md:32` |
| ⬜ 5 | the run handoff's state row still schedules #834's build, phases 1–3 and phase 4, with no PR | `seal/specs/1791382684-every-reader-and-record-is-inventoried/handoff.md:39` | open | last written at 7608d82c; PR #901 exists; decision 2 at `handoff.md:140` needs a dated note, not an edit |
| ⬜ 6 | the changelog line names "the work item's `inventory/`", which `settle --retire` removes after the release | `seal/specs/1791382684-every-reader-and-record-is-inventoried/changelog.md` | open | `spec.md` §*The inventory's fate*: read at the tag after retire |
| ❓ | whether the owner accepts the reframe reversing Q1 (c), their decision 2 of 2026-10-12, and leaving #835's Q7 at a default that describes no build | `seal/specs/1791382684-every-reader-and-record-is-inventoried/questions.md` | ❓ out of verified scope | the approval was the orchestrating session's under `automation`; `plan.md` and `questions.md` offer the overturn "at the approval", which the owner did not hold; answered by the repository owner |
| 🟢 | the withdrawal is exact: `.py` files and the census equal the release branch's, the diff is confined to this item's directory, no ledger fragment, `### Added` alone, nothing of the backfill in `docs/` or the changelog | `tests/undeclared_readers.txt` | confirmed | `git diff --quiet origin/release/v0.21.0 HEAD -- '*.py' tests/undeclared_readers.txt` exit 0; `git diff --name-only` names only the item's files; grep of `docs/`, `CHANGELOG.md`, `seal/follow-up.md`, `seal/config.md` (probes) |
| 🟢 | removing `survivors.md` rather than keeping it empty is right for CI | `.github/workflows/hygiene.yml:259` | confirmed | the step adds `--exempt` for each existing file; a header-only file exits 2 ("An exemption file with nothing in it silences nothing"); without it exit 0, 0 sentences; CI at the merge ref 90784ec printed the same; `broad_gate.py#exemptions` globs, so absence is not an error |
| 🟢 | withdrawing rather than keeping the 64 single-unit-row lines holds against the round records | `seal/specs/1791382684-every-reader-and-record-is-inventoried/spec.md` | confirmed | round 1's full read caught about 37 of at least 65 distinct multi-unit false lines, so its 3-of-64 is not a verified set; the stated grounds are ⬜ 3 |
| 🟢 | round 3's finding 1 is closed by the withdrawal — `_name_at` carries no line this item wrote and is back on the census | `tests/undeclared_readers.txt` | confirmed | already deferred in round 3 to the frame; the census equals the release branch's, and the unit's docstring equals 7608d82c's |
| 🟢 | round 3's finding 2 is closed by the withdrawal — `_expands`, `cell_index`, `shared_reader` carry no line this item wrote | `tests/undeclared_readers.txt` | confirmed | already deferred in round 3 to the frame; same diff |
| 🟢 | round 3's ⬜ 3 is closed for what it asked — the frame chose the inventory's definition and withdrew the plan's rule | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md` | confirmed | already deferred in round 3 to the frame; `spec.md` §*The direction word, settled*; where that definition lives is this round's 🟡 2 |
| 🟢 | rounds 1 and 2's findings no longer apply — every line they found or fixed left with the restore | the 44 restored `.py` files | confirmed | `git diff --quiet origin/release/v0.21.0 HEAD -- '*.py'` exit 0; the three rider stamps are back at #835's hashes, rider check green |

## Paste-ready fixes

### 🟡 1

```
# the orchestrator's act; no commit
gh pr edit 901 \
  --title "chore: every reader and record of 0.20.0 is inventoried, and the Reads: backfill it framed is withdrawn (#834)" \
  --body-file <file holding the text below>

Closes #834

#834's inventory classifies every reader of 0.20.0 as owned, observed or
guess, beside 35 record mechanisms and the 63 issues since 0.18.0 by family.
It is in the work item's `inventory/`, and the decisions it led to are their
own issues in this release.

This branch also built a backfill that moved the inventory's readings into
the code as 189 `Reads:` lines. Three review rounds kept finding false ones,
and the reframe withdrew the backfill whole. No `.py` file and no census
line changes: the units are back on `tests/undeclared_readers.txt` and
declare when next touched. The phase for `hooks/worktree-guard.py` was
dropped with it.

The work item is `seal/specs/1791382684-every-reader-and-record-is-inventoried/`.
```

### 🟡 2

```
docs/the-reader-registry.md:31 — replace the paragraph's first sentence

The direction says where an input the unit does not understand ends, read
through to the decision the unit's value feeds: `refused` where that
decision refuses it (raised, stopped, or handed back as a value its caller
refuses on), `passed` where it is let through as if understood, `mixed`
where both happen. A helper's direction is therefore read at its callers,
not on its own body.

overview.md §Fed back into the spec — replace `none` with
- `spec.md` §*The direction word, settled* → `docs/the-reader-registry.md`
  §*The four classes and the line that declares one*, its direction sentence

overview.md §Not done — point the hand at docs/, not spec.md:
`docs/the-reader-registry.md` §*The four classes and the line that declares
one* is the definition that hand applies.

Verify: bin/pact-check and bin/evidence-check . exit 0;
bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py tests/test_one_word_one_meaning.py

Or justify: an issue in milestone 0.21.1 carrying the sentence above, its
answerer the registry's owner, named in `overview.md` §Not done instead of
spec.md.
```

### ⬜ 3

```
plan.md:103, the alternative row's failure-scenario cell — replace the second sentence with
  Round 1 read all 189 bodies, the 64 among them, and caught about 37 of the
  at least 65 distinct false lines of the multi-unit class that rounds 2 and
  3 went on to find; a 3-of-64 result from a reader with that recall is a
  lower rate, not a verified set. (Round 1's own matching split the lines
  83 / 97 with 9 unmatched; the 64 / 125 split is the framer's probe.)

spec.md:164 — replace "94 of the 189 lines have been read against their body by nobody but the inventory's agent at 5623d728" with
  Round 1 read every line beside its body; after it, 94 of the 189 were
  opened by no later round

overview.md:24 — "found 71 false" → "made 71 findings of a false line, at most 68 of them distinct lines"
```

### ⬜ 4

```
overview.md:9   "so the tree's code is what 7608d82c holds" → "so the branch's code is the release branch's"
spec.md:339     "so the tree's code returns to what 7608d82c holds" → "so the branch's code is the release branch's"
spec.md:327     "the census holds 1,584 lines" → "the census equals the release branch's (1,584 lines #835 landed, less the units siblings have since declared)"
spec.md:328     "`bin/survivor-check --range origin/release/v0.21.0...HEAD --exempt` this item's `survivors.md`" → "`bin/survivor-check --range origin/release/v0.21.0...HEAD`, with no exemption file (`phases/phase-5.md`)"
overview.md:23  "over the build's tree" → "at the head"
overview.md:32  "The inventory's other columns (`Decides`, `Duplicates`, `Note`) stay where they are" → "The inventory stays where it is, every column of it,"
```

## Executed probes

| What was run | Result |
|---|---|
| `git clone --no-local` of the worktree into the round's scratch directory, checked out at fce23e01, `origin/release/v0.21.0` fetched at 34fc36e9 | clone at the target |
| `git diff --quiet origin/release/v0.21.0 HEAD -- '*.py' tests/undeclared_readers.txt` | exit 0 |
| `git diff --name-only origin/release/v0.21.0 HEAD`, filtered to paths outside the item's directory | none |
| `git diff --quiet 7608d82c HEAD -- '*.py' tests/undeclared_readers.txt` | exit 1: `hooks/worktree-guard.py`, `tests/test_the_guard_asks_once_per_session.py`, `tests/test_worktree_guard.py`, `tests/undeclared_readers.txt`, all the merge's (⬜ 4) |
| `wc -l` of the census at 7608d82c, ef8fb33c, 34fc36e9 and fce23e01 | 1,584, 1,584, 1,583, 1,583; the one line is `hooks/worktree-guard.py#main`, declared by #894 |
| `ls seal/ledger/` for the item's id; `grep -c '^### '` on the item's `changelog.md` | no fragment; 1 |
| grep of `docs/`, `CHANGELOG.md`, `seal/follow-up.md`, `seal/config.md` for `backfill`, `#834` and the item's id | only `docs/the-reader-registry.md:11`, which credits the inventory and claims no line |
| `git grep 'Reads: guess'` over non-test `.py` at 7608d82c and 31057238 | 2 and 55, so the build's 53 `guess` lines are as `spec.md` states |
| `bin/evidence-check .` | exit 0; 0 refused, 0 drifted; the item is unread (no fragment) |
| `bin/correction-check --range origin/release/v0.21.0...HEAD` | exit 0; 2 merges examined, no marker dropped; no released ledger file changed |
| `bin/survivor-check --range origin/release/v0.21.0...HEAD` | exit 0; 1,042 files against 0 removed sentences |
| the same with `--exempt` a `survivors.md` holding only its heading, intro and table header (written in the clone, then deleted) | exit 2: "An exemption file with nothing in it silences nothing" |
| `bin/unverified-check --baseline origin/release/v0.21.0` | exit 0; this item 1 open (the sealer's), 2 closed |
| `bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py tests/test_a_rider_reaches_its_file.py tests/test_no_real_identifiers.py tests/test_one_word_one_meaning.py` | 153 passed, exit 0 |
| `gh pr view 901` title and body; `gh pr checks 901`; the `release` job's log | title and body as 🟡 1 quotes; `release`, `ledger`, `lint` pass, pytest legs pending; the survivor step printed 0 sentences at 90784ec (read from CI, not run here) |
| the broad gate: full suite, lint, typecheck | not yet — the sealer's, after the rounds settle; not due while 🟡 1 and 🟡 2 are open |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

## Regression tests to plant

None. The item changes no code at the head, and every claim it still makes
is read rather than tested, as `spec.md` says.

## Facts for the evidence ledger

None. The item has no ledger fragment after phase 5, and nothing above
gives it a claim a test holds.

Needs a fix: yes — 🟡 1 (PR #901's title and body still announce the withdrawn backfill and phase 4), 🟡 2 (the settled direction definition has no home that outlives the item)
Loses a record or crashes: no

## Proof

Opened in the worktree at fce23e01 or in the clone of it:

- `seal/specs/1791382684-every-reader-and-record-is-inventoried/`: `routing.md`, `changelog.md`, `overview.md`, `plan.md`, `spec.md`, `questions.md`, `phases/phase-4.md`, `phases/phase-5.md`, `handoff.md` (head, §*What the owner decided (2026-10-12)*, the state table), `rounds/round-1.md`, `rounds/round-1-report.md` (summary), `rounds/round-1-fixes.md`, `rounds/round-2.md`, `rounds/round-3.md`, `rounds/round-3-fixes.md`; `inventory/*.md` by grep only
- the diffs of ef8fb33c (stat), c6dda5ca, 9c228af5 and fce23e01, including the removed `survivors.md` and the removed ledger fragment
- `.github/workflows/hygiene.yml` (the survivor and correction steps)
- `skills/code-review/scripts/survivor_check.py` (the empty-exemption refusal)
- `skills/verify/scripts/broad_gate.py#exemptions`
- `skills/code-review/scripts/chain_check.py#frame_foot` and its `REFRAME_RE`
- `.github/scripts/publish_release_note.py` (how the note reads PR titles)
- `docs/the-reader-registry.md` lines 5–37
- `seal/specs/1791384152-a-reader-declares-its-input-class/questions.md` Q7, and that item's `handoff.md` and `plan.md` by grep
