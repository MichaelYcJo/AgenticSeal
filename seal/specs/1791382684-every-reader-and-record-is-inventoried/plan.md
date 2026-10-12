# Implementation Plan: every reader and record is inventoried (#834) — the backfill, withdrawn at the reframe

<!-- seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-12 by the repository owner, when `smith` was spawned.
Approved 2026-10-12 by the orchestrating session under the owner's automation press, for the reframe, when `smith` was spawned.

`questions.md` Q1 was answered (c) by the owner with that approval. The
reframe of 2026-10-12, after round 3, withdraws the build that answer sized
(`spec.md` §*The reframe*); the redesign is approved by a second `Approved`
line under this one when `smith` is spawned for it
(`skills/code-review/orchestration.md` §*A fix of a fix twice sends the work
item back to its framer*).

## Summary

The first frame moved the inventory's classes into the code as `Reads:`
lines, for the 245 units no ledger row cites; phases 1–3 wrote 189 of them in
44 files by transcribing the rows. Three review rounds read the lines against
the code and found 40, then 27, then 4 false, the last four in lines the fix
passes themselves had written, and the run stopped on the second fix of a
fix. The reframe's judgment is `spec.md` §*The reframe*: nothing in a
transcribed line is verifiable by a check beyond its two vocabulary words, so
the build is a guess-and-patch loop under 0.21.0's theme, and the fate of the
reader that produced it is deletion. Phases 4 and 5 put the tree back — the
44 files and the census return to what 7608d82c holds, in one file-level
restore, and the records stop claiming lines — and the item ships as the
inventory, which was its first scope. The direction word's two definitions
are settled on the inventory's, and the guard's phase is gone with the rest.

## Technical context

**The withdrawal is a restore, not an edit.** Every `.py` change on this
branch since 7608d82c is the build's: a `Reads:` line, the paragraph under
it, or one of three rider stamps. `git diff 7608d82c HEAD -- '*.py'` is 44
files, 684 insertions and 71 deletions, read line by line at the reframe, and
rounds 1–3 each found the syntax trees with docstrings removed equal at both
ends. The release branch has not been merged in since 57e2bc13, so no
sibling's change sits in those files. Phase 4 is therefore one
`git checkout 7608d82c -- <paths>` over the 44 files and
`tests/undeclared_readers.txt`, the paths taken from
`git diff --name-only 7608d82c HEAD -- '*.py' tests/undeclared_readers.txt`,
and its verification is `git diff --quiet 7608d82c HEAD -- '*.py'
tests/undeclared_readers.txt`. The three rider stamps come back with their
old hashes, which are the restored units' hashes, so
`tests/test_a_rider_reaches_its_file.py` is green with no re-stamp. No `Edit`
call touches a docstring and no script is written: the restore is git's, and
what it leaves is checkable by one diff.

**What each record becomes** (phase 5):

- `seal/ledger/1791382684-every-reader-and-record-is-inventoried.md` —
  removed. Its two rows (B1, B2) claim lines and a shrink the tree no longer
  has, and no test holds a claim the item still makes: the inventory is read,
  not tested. With no fragment the item is not live, so the records arm reads
  none of its files; the `· NAME NOT IN TREE` markers phase 3 put on ten
  inventory lines stay, because they are true and cost nothing.
- `changelog.md` — the `### Changed` entry removed; `### Added` stands as
  written.
- `overview.md` — one more divergence row (the build withdrawn at the
  reframe, `spec.md` §*The reframe* as grounds); in `## Not verified`, the
  189-lines row and the phase-4 row closed with ✅ and what closed them (no
  line left to verify, no phase left), the full-suite row left for the
  sealer; `## Not done` rewritten: the 912 rowed units stay on the census and
  declare when touched, the inventory beside them at the tag.
- `survivors.md` — re-derived from `survivor-check --range
  origin/release/v0.21.0...HEAD` at the phase-4 head. The census block is no
  longer a removed sentence, so most rows go; what the check still names is
  read again and kept with its grounds.
- `phases/phase-4.md` and `phases/phase-5.md` — written as each closes, from
  `templates/sdd-phase.md`.
- this file's Status cells for 4 and 5.

**The merge.** `origin/release/v0.21.0` moved to 34fc36e9 (#894) after this
branch's base; phase 5 merges it in — a merge, never a rebase — so the
redesign's review round and the sealer read the landed guard. After phase 4
this branch changes no `.py` file, so the merge meets no code conflict, and
`tests/undeclared_readers.txt` takes the release branch's lines (#894's
`main` left it) because this branch's copy equals the base's. A later landing
(#896) is the landing step's own merge, `handoff.md` §*How a chain is run*
item 2.

**The direction word.** Settled in `spec.md` §*The direction word, settled*:
the inventory's meaning, which #835's spec made the registry's. The rule
rounds 1 and 2 wrote into this file's `Unit → units` bullet is withdrawn with
the bullet; the bullet, and the six mapping rules phase 1 applied, are in
this file at 8938af5b and in `phases/phase-1.md`.

**Where it breaks in six months.** The 912 rowed units carry no line, and the
inventory's reading of them is in a directory that retires at the fold. A
session touching one of them reads the code, not the row, and writes the
line from that reading; the inventory is at the tag for anyone who wants the
2026-10-07 reading beside it. Nothing re-reads the census but the hash,
which is the registry's own design.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **withdraw all 189 lines; every unit returns to the census** | `grep -rn "Reads: guess"` loses 53 entries the inventory still lists; the units declare when touched, one reading per diff, read by the diff's reviewer | **chosen**; `spec.md` §*The reframe* |
| keep the 64 lines from rows naming one unit, withdraw the 125 from rows naming several | measured by the framer's probe: 3 of the 64 were found false in round 1 and none since, against 65 distinct false lines among the 125. Round 1 read all 189 bodies, the 64 among them, and caught about 37 of those 65, rounds 2 and 3 finding the rest, a recall of about 57%; a 3-of-64 result from a reader with that recall is a lower rate, not a verified set. (Round 1's own matching split the lines 83 / 97 with 9 unmatched; the 64 / 125 split is the framer's probe.) Keeping them keeps the part of the guess that looked better, which is the patch the theme refuses | rejected; the owner can overturn it at the approval with this row's numbers |
| keep the lines a check can verify | the set is empty: `declarations` reads two vocabulary words, K1 refuses `nothing` beside a primitive and none of the 189 says `nothing`, and `docs/the-reader-registry.md` §*What neither check can read* lists the rest as the reviewer's | the chosen approach is this one with its set measured at zero |
| a fourth fix pass over the four lines round 3 named and the 94 nobody opened | the loop the owner's review of the run names; each pass so far wrote a false line of its own (`sections` after round 1, `_name_at` after round 2) | rejected by the stop itself (`skills/code-review/orchestration.md` §*A fix of a fix twice sends the work item back to its framer*) |
| read all 189 units afresh and write lines from the code, not the rows | 189 hand readings by one agent in one spawn, reviewed by sampling — the instrument that produced the three rounds' error rate, with no row grounding it; the registry pays the reading when the unit is touched, one at a time, in a diff a reviewer reads whole | rejected |
| a checker that reads the prose against the body (every backticked name present in the unit or its callees) | mechanism in a reframe, and a necessary condition only: `_name_at`'s line passed it and was false; `docs/the-reader-registry.md` §*Who declares: every unit, found by a rule* chose a loud rule over a quiet enumeration for this reason | rejected |
| `git revert` of the build's commits | the commits carry records (phase records, this file's Status cells, round-record closures) the history keeps; reverting them re-edits the record set and reopens closed phases | rejected; a file-level restore of the code and the census, the records rewritten by hand |
| keep phase 4 (the guard) as framed, after #896 lands | the same transcription over the guard's 25 uncited units, from the part whose rows the rounds found wrongest (part 1: 98 `guess` readers, most of the multi-unit rows) | rejected; the guard's units declare under #894 and #896, and the rest when touched |

The first frame's alternatives — the Q1 sizes, the stale units, the one-shot
script, the inventory's home, `Reads: nothing` on the unrowed units — are in
this file at 8938af5b; they sized a build the reframe withdraws and are not
re-argued.

## Phases

Vertical slices — each phase ends with something runnable and verified.
Phases 1–3 are closed and keep their commits; what they built, phases 4 and
5 withdraw. Phase 4 as the first frame drew it (`hooks/worktree-guard.py`
after #894 and #896) is gone, not deferred.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The mapping at the build's tree, by the first frame's six rules (this file at 8938af5b), read with `reader_registry.population()`: the rowed, clean, stale, conflicting and unparsed counts, the Q1 sets (a)–(c) with their re-read counts, each beside the frame's reading at 57e2bc13; the per-unit listing stays in the phase record's text only as counts and the names of the 30 hand-read units. No tree edit | `phases/phase-1.md` holds both readings with their SHAs; `bin/test tests/test_a_reader_declares_its_input_class.py` green before any edit | 681fa7b1 |
| 2 | The lines on every unit in Q1's answered set (default: the units no ledger row cites) in every file but `hooks/worktree-guard.py`, and the census lines of exactly those units removed, by the one-shot script, deleted after. The 30 hand-read units are decided here, the weakest class winning | the registry test green; `git diff --stat` on the census shows a line removed per unit written and no other; `bin/evidence-check .` reports no drifted released row under (c), and the live rows it names are re-stamped in place (`--reverify --checked <date>`, narrowed with `--ledger` to the fragments read); under (a) or (b) the `Re-read ·` rows are written with `--reverify --into` after each cited row is read | 36491ddb |
| 3 | The rows in `seal/ledger/1791382684-every-reader-and-record-is-inventoried.md`: one claim per acceptance row of `spec.md` §*User scenarios & acceptance* that a test holds, anchored on the test by #836's form where one holds it and on the census file's heading-less line count otherwise; the changelog fragment; `overview.md` opened with the divergences phase 2 met | `bin/evidence-check .` exit 0; `correction-check` clean; `survivor-check --range origin/release/v0.21.0...HEAD` clean | 8160ad69 |
| 4 | The withdrawal: the 44 `.py` files the build changed and `tests/undeclared_readers.txt` restored from 7608d82c by `git checkout 7608d82c -- <paths>`, the paths from `git diff --name-only 7608d82c HEAD -- '*.py' tests/undeclared_readers.txt`, in one commit that touches nothing else; no docstring edited by hand, no script written | `git diff --quiet 7608d82c HEAD -- '*.py' tests/undeclared_readers.txt` exit 0; `wc -l tests/undeclared_readers.txt` prints 1584; `bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py tests/test_a_rider_reaches_its_file.py` green; `bin/evidence-check .` exit 0 | ef8fb33c |
| 5 | The records say what the tree now has: the ledger fragment removed, the changelog's `### Changed` entry removed, `overview.md`'s two `Not verified` rows closed and its divergence and `Not done` sections rewritten, `survivors.md` re-derived, `phases/phase-4.md` and `phases/phase-5.md` written; then `origin/release/v0.21.0` merged in, a merge and never a rebase | `bin/evidence-check .` exit 0 and no `Re-read ·` row owed; `bin/correction-check --range origin/release/v0.21.0...HEAD` exit 0; `bin/survivor-check --range origin/release/v0.21.0...HEAD --exempt` this item's `survivors.md`, exit 0; `bin/unverified-check` with `--baseline origin/release/v0.21.0`, exit 0; the eleven suite-wide guard modules green; `grep -c "^### "` on this item's `changelog.md` prints 1; `ls seal/ledger/` names no file of this item; `git diff --stat origin/release/v0.21.0...HEAD -- hooks/worktree-guard.py` prints nothing | 9c228af5 |

This table is also where the work records how far it got. There is no separate
task list. **Status is empty, or the commit that closed the phase.**

## Seams

- `hooks/worktree-guard.py` — untouched by this branch at every commit, and
  after phase 5's merge it is the release branch's. #896's branch changes 121
  lines of it and declares three of its units; nothing here meets that.
- `hooks/cmdline_base.py` — untouched at every commit (its bytes below the
  rider are pinned); nothing to restore.
- `tests/undeclared_readers.txt` — the one file both this item and every
  sibling edit. After phase 4 this branch's copy equals the base's, so the
  merge takes the release branch's lines with no conflict.
- `seal/specs/1791382684-every-reader-and-record-is-inventoried/inventory/`
  — the ten marker lines stay; the records arm reads them only while a
  fragment exists, and after phase 5 none does.

## Operational impact

No migration, dependency or environment change. What a deployer meets:

- **No code change ships from this item.** The census is #835's 1,584 lines
  less whatever the siblings declared; `grep -rn "Reads: guess"` lists
  exactly what the release branch lists.
- **The fold at 0.21.0 gathers this item's changelog fragment and no ledger
  rows**; the `Re-read ·` cost the first frame measured is not paid.
- **Any branch open against `release/v0.21.0` meets no docstring conflict
  from this item.**
