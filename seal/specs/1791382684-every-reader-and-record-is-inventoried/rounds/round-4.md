# 1791382684-every-reader-and-record-is-inventoried — review round 4

| Field | Value |
|---|---|
| Target SHA | fce23e01735afb2ed6927e60cda37dd090d48f21 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | #901 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are written and no round has opened them |
| Fix range | `602fb87b709abe077db23ec520df331284754242..9ceba9a34a5061def93b43fdd96e20217df72512`, 2 commits |
| Contract changes | none |
| New units | none |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1 (PR #901's title and body still announce the withdrawn backfill and phase 4), 🟡 2 (the settled direction definition has no home that outlives the item) |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 4 of #834, the redesign's first record after the run stopped at round 3 (`Reframed 2026-10-12 by framer, after round 3`), target fce23e01. The reframe withdraws the 189-line backfill whole, returns the census, settles the direction word on the inventory's meaning and drops phase 4. The reviewer was asked to judge that the withdrawal is exact, that what the item still ships says only what is true after it, that the reasoning for withdrawing rather than keeping the 64 single-unit-row lines holds against the round records, that removing `survivors.md` is right for CI, and what the owner should see about the reversal of their Q1 (c) answer.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | PR #901's title and body still say 189 units declare and leave the census and phase 4 waits; the title is the squash subject and a release-note line | PR #901 title | answered | corrected on the pull request by the orchestrator: PR #901's title and body are the orchestrator's to edit, and nothing in the tree changes for them; `gh pr view 901` at fce23e01; `.github/scripts/publish_release_note.py` composes the note from PR titles |
| 🟡 2 | the settled direction definition lives only in a `spec.md` that retires at the fold, while the registry document reads closer to the withdrawn body-local rule | `docs/the-reader-registry.md:31` | **fixed** `4d2c56c6` | fixed at 4d2c56c6 — `docs/the-reader-registry.md` §*The four classes and the line that declares one* now says the direction is where an input the unit does not understand ends, read through to the decision its value feeds, and that a helper's direction is read at its callers; read first against the inventory's key (part 6: a presence pin is `refused` because a rewording fails it) and #835's spec ("The direction is the inventory's"). The fold marker and the `Enforced by:` line are untouched. The edit drifted #835's live row D1, which was read and re-executed (`bin/fold-check --root .` exit 0, 19 documents, none over the ceiling) and re-stamped in place by `evidence-check --reverify --checked 2026-10-12 --ledger` that fragment. `overview.md` §*Fed back into the spec* and §*Not done* point at `docs/`, and `9ceba9a3` names the sentence in the changelog fragment, under `### Added`, which stays the fragment's one heading; `spec.md` §*The direction word, settled*; `overview.md` §*Not done* points future writers at the retiring spec; §*Fed back into the spec* `none`; round 3 ⬜ 3 measured the disagreement |
| ⬜ 3 | the withdrawal's grounds say the 64 were "sampled, not read" and 94 lines were read by nobody; round 1 read all 189; the 64/125 split and "71 false" are stated without their caveats | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md:103` | answered | corrected at `4d2c56c6`: `plan.md`'s alternative row now rests on round 1's recall (it read all 189 bodies and caught about 37 of at least 65 distinct multi-unit false lines, about 57%), counts at most 65 distinct false lines among the 125, and states round 1's 83 / 97 / 9 matching beside the framer's 64 / 125; `spec.md` says round 1 read every line and 94 were opened by no later round; `overview.md` says 71 findings, at most 68 distinct lines; `rounds/round-1.md` probe "189 units, 4,268 lines of source, all read", and 83/97/9 matching; `spec.md:164` against `spec.md`'s own round table; the decision holds on round 1's recall, about 37 of 65 |
| ⬜ 4 | five sentences describe the phase-4 tree and are false at the head after the merge: 7608d82c's code, 1,584 census lines, `--exempt` a removed file, "the build's tree", "other columns" | `seal/specs/1791382684-every-reader-and-record-is-inventoried/spec.md:327` | answered | corrected at `4d2c56c6`: `overview.md` and `spec.md` §*Removes* say the branch's code is the release branch's; the census acceptance row says it equals the release branch's, 1,583 at 34fc36e9 after #894 declared `hooks/worktree-guard.py#main`; the record-checks row runs `survivor-check` with no exemption file; the sealer's row reads "at the head"; `Not done` says every column of the inventory stays; census `wc -l` 1,583 at fce23e01 and at 34fc36e9; `git diff 7608d82c HEAD -- '*.py'` names `hooks/worktree-guard.py` and two test modules; also `spec.md:328`, `spec.md:339`, `overview.md:9`, `overview.md:23`, `overview.md:32` |
| ⬜ 5 | the run handoff's state row still schedules #834's build, phases 1–3 and phase 4, with no PR | `seal/specs/1791382684-every-reader-and-record-is-inventoried/handoff.md:39` | answered | corrected at `4d2c56c6`: `handoff.md`'s state row for #834 names PR #901, the build, the reframe, phases 4–5 and the owner's choice of withdrawal, and decision 2 carries a dated line saying the reframe and the owner's answer superseded it for #834, its own text unchanged; last written at 7608d82c; PR #901 exists; decision 2 at `handoff.md:140` needs a dated note, not an edit |
| ⬜ 6 | the changelog line names "the work item's `inventory/`", which `settle --retire` removes after the release | `seal/specs/1791382684-every-reader-and-record-is-inventoried/changelog.md` | answered | corrected at `4d2c56c6`: the changelog fragment names the inventory's full path and says it is read at the `v0.21.0` tag once `settle --retire` removes the directory; `spec.md` §*The inventory's fate*: read at the tag after retire |
| ❓ | whether the owner accepts the reframe reversing Q1 (c), their decision 2 of 2026-10-12, and leaving #835's Q7 at a default that describes no build | `seal/specs/1791382684-every-reader-and-record-is-inventoried/questions.md` | ❓ out of verified scope | the approval was the orchestrating session's under `automation`; `plan.md` and `questions.md` offer the overturn "at the approval", which the owner did not hold; answered by the repository owner |
| 🟢 | the withdrawal is exact: `.py` files and the census equal the release branch's, the diff is confined to this item's directory, no ledger fragment, `### Added` alone, nothing of the backfill in `docs/` or the changelog | `tests/undeclared_readers.txt` | confirmed | `git diff --quiet origin/release/v0.21.0 HEAD -- '*.py' tests/undeclared_readers.txt` exit 0; `git diff --name-only` names only the item's files; grep of `docs/`, `CHANGELOG.md`, `seal/follow-up.md`, `seal/config.md` (probes) |
| 🟢 | removing `survivors.md` rather than keeping it empty is right for CI | `.github/workflows/hygiene.yml:259` | confirmed | the step adds `--exempt` for each existing file; a header-only file exits 2 ("An exemption file with nothing in it silences nothing"); without it exit 0, 0 sentences; CI at the merge ref 90784ec printed the same; `broad_gate.py#exemptions` globs, so absence is not an error |
| 🟢 | withdrawing rather than keeping the 64 single-unit-row lines holds against the round records | `seal/specs/1791382684-every-reader-and-record-is-inventoried/spec.md` | confirmed | round 1's full read caught about 37 of at least 65 distinct multi-unit false lines, so its 3-of-64 is not a verified set; the stated grounds are ⬜ 3 |
| 🟢 | round 3's finding 1 is closed by the withdrawal — `_name_at` carries no line this item wrote and is back on the census | `tests/undeclared_readers.txt` | confirmed | already deferred in round 3 to the frame; the census equals the release branch's, and the unit's docstring equals 7608d82c's |
| 🟢 | round 3's finding 2 is closed by the withdrawal — `_expands`, `cell_index`, `shared_reader` carry no line this item wrote | `tests/undeclared_readers.txt` | confirmed | already deferred in round 3 to the frame; same diff |
| 🟢 | round 3's ⬜ 3 is closed for what it asked — the frame chose the inventory's definition and withdrew the plan's rule | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md` | confirmed | already deferred in round 3 to the frame; `spec.md` §*The direction word, settled*; where that definition lives is this round's 🟡 2 |
| 🟢 | rounds 1 and 2's findings no longer apply — every line they found or fixed left with the restore | the 44 restored `.py` files | confirmed | `git diff --quiet origin/release/v0.21.0 HEAD -- '*.py'` exit 0; the three rider stamps are back at #835's hashes, rider check green |

## Paste-ready fixes

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

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|
