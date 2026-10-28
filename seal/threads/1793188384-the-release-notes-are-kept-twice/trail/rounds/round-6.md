# Review round 6: 1793188384-the-release-notes-are-kept-twice

target: b97ded39, fixes 49869962..b97ded39

This is the verifying round after round 5. It reads the fix range: the
orchestrator's `4b42844b` (the frame), the crafter's `bb1c65c5` (the fix
pass) and `b97ded39` (round 5's record as the fix pass left it). The round
ran in a `git clone --no-local` of the branch at `b97ded39`, held in the
round's scratch directory. The repository declares no `seal/parity.md`, so
this round writes no `original:` line.

Carried from earlier rounds, not established again: the 58 version tags,
that `v0.23.1` holds all 58 files (S11, executed by round 5 at `2e0c895d`;
no commit in the fix range touches a tag or `changelog/`), and that the
v0.12.2 note holds neither 0.12.2 sentence (round 5's third confirmation).
Re-established this round: the state of every published note on GitHub, the
*Scope* item 5 criterion over the 58 notes, the cell counts of the `gaps.md`
table, and every sentence in the work item and `seal/follow-up.md` that
states the two 0.12.2 rows or the 26 notes.

The account checked: the spawn prompt says the orchestrator restored the 16
notes v0.3.0 to v0.10.0 from their backups and read each back equal. The
release API shows the restore's stamps and no appended block in any of the
26 (executed). Byte equality with the backups is not checkable from here
(`## Not judged`).

## Findings

### 1. The plan's phase 5 row still says the two 0.12.2 follow-up rows point at the file at `v0.23.1`, "as *Scope* item 8 now says"

severity: should
location: `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/plan.md:74`
evidence: executed `git grep -n -E "v0\.12\.2|0\.12\.2|follow-up" -- seal/threads/1793188384-the-release-notes-are-kept-twice/frame seal/threads/1793188384-the-release-notes-are-kept-twice/gaps.md seal/threads/1793188384-the-release-notes-are-kept-twice/changelog.md`, `sed -n 74p seal/threads/1793188384-the-release-notes-are-kept-twice/frame/plan.md`, `git log -L74,74:seal/threads/1793188384-the-release-notes-are-kept-twice/frame/plan.md`
verdict: fixed 96610a28
reopens: round-5#4

Round 5's finding 4 asked that the two `seal/follow-up.md` rows go, and
that the frame's sentences keeping them be reframed. The rows are gone
(`bb1c65c5`), and four frame places now say so: *Scope* item 8
(`frame/design.md:100-105`), the out-of-scope bullet (`:133-134`), the
*Removes* row (`:524`) and `frame/questions.md:40-43`. `frame/plan.md:61`
cites `8a1173c8:seal/follow-up.md:47`. Those parts of the close hold.

One frame sentence still states the old fact. The phase 5 row of the plan's
Phases table, `frame/plan.md:74`, says: "The two `seal/follow-up.md` rows
that name `changelog/0.12.2.md` point at that file at `v0.23.1`, as *Scope*
item 8 now says". *Scope* item 8 now says the opposite: "Those two rows
go". No such rows stand in `seal/follow-up.md` at `b97ded39` (executed:
`git grep -n "changelog/0\.12\.2" -- seal/follow-up.md` finds nothing). The
line was last changed at `10cbc6e9`, the reframe before round 5 (executed:
`git log -L`), so `4b42844b` did not reach it. Round 5's finding 4 named
`plan.md:61` and not this row, so the miss is round 5's as well as the
fix's.

This matters because the plan is what a sealer reads beside the tree. A
reader of the phase 5 row looks for two rows that do not exist, and the
row's own citation sends that reader to a *Scope* item that contradicts
it. Contract rule 19 asks that every sentence stating the old fact is
rewritten in the change that retires it. The row is a frame row, so the
orchestrator writes it.

```markdown
<!-- frame/plan.md:74, the second cell -->
| 5 | No note is republished (`frame/questions.md` Q2, the owner's answer of 2026-10-28). Every record of this work item that says a republish happens, or that S11 waits on one, is rewritten to the decision. The phase pointed the two `seal/follow-up.md` rows that name `changelog/0.12.2.md` at that file at `v0.23.1`; round 5's fix pass removed both rows, as *Scope* item 8 now says | <the Verification cell unchanged> | 58f3a6a7 |
```

answer: The orchestrator applied the block above to the phase 5 row's second cell as given at `96610a28`, leaving its Verification and Status cells, since the frame is not the crafter's to write; a `grep -n -i -E "follow-up|0\.12\.2"` over the three frame files then finds no other sentence saying the rows stay or point anywhere (the phase 4 row names them among the readers that phase re-pointed, which it did). No fix pass ran for this finding, so the orchestrator writes both its lines.

## Confirmations

confirms: round-5#1
The published state now matches the owner's decision, and the records say
what happened. The release listing, re-read at 2026-10-28T14:19:39Z with
`gh api --paginate 'repos/MichaelYcJo/AgenticSeal/releases?per_page=100'`
(a read), returned 58 releases (executed). None of the 26 *Scope* item 5
lists holds the summary text "Full changelog — what each change", the
character `U+1F4CB`, or a `<details>` element. All three stand in the
notes of v0.15.1 to v0.23.1 only. The stamps equal the table at
`trail/phases/phase-5.md:50-61`: v0.2.0 at 13:55:41Z, v0.3.0 to v0.10.0
from 14:11:30Z to 14:11:56Z, and the other nine on 2026-09-23. The
*Scope* item 5 criterion, written again from round 5's `## Probes` row and
run once, found 32 notes holding their file and 26 not. The 26 are exactly
the list at `frame/design.md:70-73` (executed). `gaps.md:14`'s *Grounds*,
Q2's Status at `frame/questions.md:47` and `phase-5.md:40-69` each state
the 17 edits and the restore. A `git grep -i` over the whole tree outside
the round records, for "no other release", "only v0.2.0", "v0.2.0's note",
"edited once", "rows keep", "keep their question", "coordinate becomes",
"left as they are", "no published note changes" and "stay as they are",
found no sentence saying only v0.2.0 was touched (executed). The hits
that remain, `frame/design.md:18`, `:66` and `frame/plan.md:14`, `:86`,
state the decision. The restored notes make them true of GitHub as it now
reads.

confirms: round-5#2
`awk -F'|' 'NR>=9 && NR<=19 && /^\|/ {print NR": "NF-2" cells"}' gaps.md`
printed 4 cells for every row from 9 to 19 (executed). Row 13 has its
*Grounds* cell back. Row 14 quotes the issue's *The change* and its *Done
when* clause, and says the first *Done when* item holds for the 32 (read:
`gaps.md:13-14`). The new row 15 quotes *Scope* item 8 "as first framed".
`git log -S'keep their question'` shows the phrase came in with the first
frame, `49ca77ee`, and left at `4b42844b`, so the quote is accurate
(executed).

confirms: round-5#3
The two places round 5 named no longer give the v0.12.2 GitHub Release as
the rows' coordinate. `frame/design.md:524` reads "Nothing: both rows go",
and `frame/questions.md:40-43` reads "Both rows go" (read). The grep in
finding 1's `evidence:` line finds no other sentence naming the v0.12.2
Release as the rows' coordinate (executed). The other frame sentence that
keeps the rows is finding 1. It gives the coordinate finding 4 retired, so
finding 1 reopens finding 4, not this one.

confirms: none
The deletion left `seal/follow-up.md` intact. The diff removes the two
rows and the blank line after each, so the row before them and the row
after them are still separated by one blank line (read: `git diff
49869962..bb1c65c5 -- seal/follow-up.md`). `git grep` for
`changelog/0.12.2`, `404 marker`, `190 rows` and `1789996775` in
`seal/follow-up.md` finds only the figure-class row, which quotes `404 ...
on 190 rows` as an example and does not depend on the removed rows
(executed). No other work item under `seal/threads/` names `0.12.2` or this
work item's id (executed). `tests/text/test_a_rider_reaches_its_file.py`
passes in the run below.

confirms: none
The phase records' cross-references hold. `phase-5.md:82-85` cites
`phase-4.md:21-23`, `:40-42` and `:84-88`. Each of those lines says what
`phase-5.md` says it does (read). The grep table at `phase-5.md:98-107` is
labelled as run at `58f3a6a7`, and its row for `seal/follow-up.md:47` and
`:49` now says the rows were removed. The three commits in the range are
authored by the repository owner's commit identity (executed: `git show
--stat --format='%h %ae %s'`), and they touch only the frame, `gaps.md`,
the two phase records, `seal/follow-up.md` and round 5's record. No
shipped file changed in the range.

confirms: none
The narrow verification for this round passed. In the clone, the 19 test
modules under `tests/` that `git grep -l -E "follow-up\.md|1793188384"`
finds ran with `bin/test -q`, `tests/conftest.py` left out because it is
not a module: 1243 passed, exit 0 (executed). The module list is the same
at `49869962` (executed: `diff` of the two lists, exit 0). `bin/seal
layout --check` exited 0 (160 files read, 0 refused), and `bin/seal rules
--check` exited 0 (all 266 check lines in 55 rule files hold). This is not
the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether each of the 17 restored notes equals its text before the edit, byte for byte. The listing shows the appended block gone and the criterion's result unchanged, not byte equality, and the backups are outside the tree | the GitHub Releases v0.2.0 to v0.10.0 | the orchestrator, which reports comparing 16 of 16 against its backups |
| How the 16 edits came about. `phase-5.md:42-43` says the others were edited "in a loop the owner stopped"; Q2's Status says "by a command the orchestrator believed had been stopped". The two can both be true, and neither is checkable from the tree or the API | `trail/phases/phase-5.md:42-43`, `frame/questions.md:47` | the orchestrator |
| The full suite, the repository-wide lint and the typecheck: unverified | the branch at `b97ded39` | the orchestrator, at `seal gate`, before the sealer is spawned |
| Whether the tag's job can list the milestones under `contents: write` alone (Q3, default (a)) | `.github/workflows/publish-release.yml` | the orchestrator, reading the log of the tag run of the release carrying this work |
| Step 3 of the update skill run by a session updating across a real release | `skills/update/SKILL.md` | the first person to update to the release carrying this work |

## Probes

| Command | Result |
|---|---|
| `gh api --paginate 'repos/MichaelYcJo/AgenticSeal/releases?per_page=100'`, at 2026-10-28T14:19:39Z, tabulated per release: tag, `updated_at`, body length, whether the body holds "Full changelog — what each change", `U+1F4CB` or `<details` | exit 0; 58 releases; all three only in v0.15.1 to v0.23.1; the 26 stamped as `phase-5.md:50-61` gives |
| `test_tmp_notes.py`, run once with `python3 -I` in the clone and then deleted: the *Scope* item 5 criterion over the 58 notes as published now | exit 0; 32 hold their file, 26 do not, the 26 of `frame/design.md:70-73` |
| `git grep -n -E "v0\.12\.2\|0\.12\.2\|follow-up"` over the work item's frame, `gaps.md` and `changelog.md` | `frame/plan.md:74` still has the rows pointing at the file at `v0.23.1` (finding 1) |
| `git grep -n -i -E` for the ten phrases the first confirmation names, over the tree without this work item's round records | no sentence says only v0.2.0 was touched |
| `awk -F'\|' 'NR>=9 && NR<=19 && /^\|/ {print NR": "NF-2" cells"}' gaps.md` | 4 cells on every row |
| `bin/test -q` over the 19 modules the last confirmation names | 1243 passed, exit 0 |
| `bin/seal layout --check`, `bin/seal rules --check` | exit 0, exit 0 |

The probe file was deleted after its one run, and `git status --short` in
the clone printed nothing. The clone, its `.venv` and the fetched listing
sit under the round's scratch directory, which is removed before hand-back.
