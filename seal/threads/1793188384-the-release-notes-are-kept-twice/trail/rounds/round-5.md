# Review round 5: 1793188384-the-release-notes-are-kept-twice

target: 2e0c895d against cb98937d

This round reviews the reframed phase 5 and its build: the orchestrator's
`10cbc6e9`, the crafter's `58f3a6a7`, and `2e0c895d`, which adds the phase
record. The round ran in a `git clone --no-local` of the branch at
`2e0c895d`, held in the round's scratch directory. The repository declares
no `seal/parity.md`, so this round writes no `original:` line. The reframe
is a design change, so this is the first finding round of a new count.
Round 4 closed nothing as `fixed` or `rejected`, so no `confirms:` line is
owed to it.

Carried from earlier rounds, not searched for again: the 58 version tags,
the fact that `v0.23.1` holds all 58 files (phase 4, round 1), and the
*Scope* item 5 criterion for whether a note holds its file. Re-established
this round: S11, the `republish` grep, the two sentences' absence from the
v0.12.2 note, and the state of every published note on GitHub.

The account checked against GitHub: the spawn prompt, `gaps.md:14` and
`frame/questions.md:47` all say that v0.2.0's note was edited once and
restored, and that no other release was touched. GitHub's release API says
otherwise (finding 1).

## Findings

### 1. Sixteen of the 26 published notes were republished on 2026-10-28, and every record says none was

severity: must
location: `seal/threads/1793188384-the-release-notes-are-kept-twice/gaps.md:14`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/questions.md:47`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:18`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:65-78`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:148`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/plan.md:13-15`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/plan.md:86-88`, `seal/threads/1793188384-the-release-notes-are-kept-twice/trail/phases/phase-4.md:21-23`, `seal/threads/1793188384-the-release-notes-are-kept-twice/trail/phases/phase-5.md:36-38`
evidence: executed `gh api --paginate 'repos/MichaelYcJo/SpecSeal/releases?per_page=100' -q '.[] | [.tag_name, .updated_at, (.body | length), (.body | test("Full changelog — what each change"))] | @tsv'`, `python3 -I test_tmp_notes.py`, `diff -q notes/v0.3.0.block notes/file-0.3.0.body`
verdict: open

The owner decided that no published note is republished. The records state
that decision as done. `gaps.md:14` says v0.2.0's note "was restored from
its backup the same day, and no other release was touched". `frame/questions.md:47`
says only v0.2.0's note was edited. `frame/design.md:65-66` and `:18` say
the 26 notes "are left as they are". `frame/plan.md:86` says "No published
note changes". `phase-5.md:36-38` says the 26 keep their text only in the
file at `v0.23.1`.

GitHub's release API says otherwise (executed). The releases v0.3.0, v0.4.0,
v0.5.0, v0.6.0, v0.7.0, v0.8.0, v0.8.1, v0.8.2, v0.8.3, v0.9.0, v0.9.1,
v0.9.2, v0.9.3, v0.9.4, v0.9.5 and v0.10.0 carry `updated_at` stamps from
2026-10-28T13:53:34Z to 2026-10-28T13:54:02Z, about two seconds apart. Each
body now holds the folded block that Q2's option (a) describes: a
`<details>` element with the summary `U+1F4CB Full changelog — what each change does and why`.
For v0.3.0, the text inside that block equals `changelog/0.3.0.md` at
`v0.23.1` without its heading line, with blank lines ignored (`diff -q`
exit 0). Above the block, the v0.3.0 note still holds its original text.
So 16 notes were appended to, in the shape of the republish the owner turned
down. v0.2.0's `updated_at` is 2026-10-28T13:55:41Z, and it does not hold
the block. No other note before v0.14.0 has a 2026-10-28 stamp. The
releases v0.11.0 to v0.13.0 carry 2026-09-23 stamps.

A probe applied the *Scope* item 5 criterion to all 58 notes as they stand
now: each paragraph of the file below its heading line, with whitespace
collapsed, must be a substring of the note with whitespace collapsed. Ten
notes lack their file: 0.2.0, 0.11.0, 0.11.1, 0.11.2, 0.11.3, 0.11.5,
0.12.0, 0.12.2, 0.12.3 and 0.13.0. The frame says 26. The difference is
exactly the 16 above.

This matters for two reasons. First, the published state contradicts the
owner's decision. Second, it contradicts every record a sealer reads. The
sealer reads the issue and the tree, and the tree states a fact about
GitHub that is false at this round's reading. The repair for the 16 notes
is made on GitHub, and only the orchestrator may make it, since contract
rule 6 withholds a post from every agent. The records then state what was
done.

The fix that keeps the owner's decision restores the 16 notes and then
corrects the history sentence. The frame says each note was backed up
before an edit (`frame/design.md:77`), so the restore uses those backups.
Where a backup is missing, the original is the body above the appended
`<details>` line. That cut can leave the original's trailing whitespace
different, so the backup is the exact source. After the restore, the
orchestrator re-runs the release listing above, and S11's record carries
it. Then these lines change:

```markdown
<!-- frame/questions.md:47, the Status cell -->
answered 2026-10-28 by the owner: neither; no note is republished. The files stay readable at `v0.23.1`, the 26 releases predate 0.14.0, and the edit buys no reader anything. On 2026-10-28 the notes of v0.2.0 to v0.10.0, 17 of the 26, were edited by appending the file folded under the summary; each was restored from its backup by <date>, and the release listing after the restore shows no note holding the appended block before v0.15.1

<!-- gaps.md:14, the Grounds cell -->
The owner's answer to `frame/questions.md` Q2, 2026-10-28. The notes of v0.2.0 to v0.10.0, edited on 2026-10-28, were restored from their backups by <date> (`trail/phases/phase-5.md`)

<!-- trail/phases/phase-5.md, a paragraph after the S11 table -->
**The published notes after the restore (executed <date>).** `gh api --paginate 'repos/MichaelYcJo/SpecSeal/releases?per_page=100'`, read for each release's `updated_at` and whether its body holds the folded full-changelog block. <the 58 rows, or the 17 restored ones with their new stamps>. The *Scope* item 5 criterion, re-run over the 58: 32 notes hold their file and 26 do not, the same 26 *Scope* item 5 lists.
```

If the owner keeps the 16 notes instead, the restore does not happen. In
that case each sentence `location:` names is rewritten to "16 republished
by appending, 10 left as they are". That reverses part of Q2's answer, so
only the owner can choose it.

answer:

### 2. The departure row in `gaps.md` has five cells, its neighbour has three, and it does not name the *Done when* clause it departs from

severity: should
location: `seal/threads/1793188384-the-release-notes-are-kept-twice/gaps.md:13-14`
evidence: executed `awk -F'|' 'NR>=9 && NR<=18 {print NR": "NF-2" cells"}' gaps.md`
verdict: open

The divergence table has four columns (`gaps.md:9`). After `58f3a6a7`, row
13 has three cells, and row 14, the new departure row, has five. The cell
"Measured: #770 split the per-release files out of `CHANGELOG.md` on
2026-10-04, after `v0.18.0`" was row 13's *Grounds*. The diff moved it to
the end of row 14 (read: `git diff cb98937d..2e0c895d -- gaps.md`). A
renderer drops a row's fifth cell, so row 13 shows no grounds, and row 14's
extra cell is lost. A sealer reading the table sees a divergence with no
grounds, beside a departure whose grounds cell is the only one shown.

The departure row also quotes the issue's *The change* bullet, "republished
from the file". It does not quote the *Done when* clause the sealer checks:
"every released version's GitHub Release holds its notes"
(`gh issue view 1053`). With no republish, that clause holds for 32
versions, not 58. The sealer reads *Done when* first, so the row should
name that clause.

```markdown
| Where a released file is read after the removal | `frame/design.md` *Scope* 5: "The files stay readable at their own tags after the removal, `git show vX.Y.Z:changelog/X.Y.Z.md`"; S11 and `plan.md`'s phase 5 row read each file at its own tag. `git cat-file -e` finds a tag's own file at `v0.18.1` to `v0.23.1` only, 14 of 58, and at none of the 26 whose note lacks its file's text | This work item's `changelog.md`, the two `seal/follow-up.md` rows and S11 read each file at `v0.23.1`, which holds all 58, identical to `49ca77ee` | Measured: #770 split the per-release files out of `CHANGELOG.md` on 2026-10-04, after `v0.18.0` |
| The 26 published notes that lack their file's text | Issue #1053 *The change* asks that they be "republished from the file", and its *Done when* asks that "every released version's GitHub Release holds its notes" | Not built. No published note is republished, so the first *Done when* item holds for the 32 releases whose note holds its file, and the other 26 keep their text in `changelog/X.Y.Z.md` at `v0.23.1` | The owner's answer to `frame/questions.md` Q2, 2026-10-28. <the history sentence as finding 1's fix leaves it> |
```

answer:

### 3. The frame still says the two follow-up rows' coordinate becomes the v0.12.2 GitHub Release

severity: should
location: `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:522`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/questions.md:40-42`
evidence: read `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:522`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/questions.md:40-42`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:100-103`
verdict: open

The reframe at `10cbc6e9` rewrote *Scope* item 8. The rows' coordinate now
"becomes `changelog/0.12.2.md` at `v0.23.1`, since the v0.12.2 GitHub
Release is not republished" (`design.md:100-103`). Two other sentences of
the frame still give the old coordinate. The `## Removes` row at
`design.md:522` says the rows' coordinate is replaced by "The v0.12.2
GitHub Release". `frame/questions.md:40-42` says "Their coordinate becomes
the v0.12.2 GitHub Release". The spawn prompt lists the *Removes* row for
`changelog/` (`:496`) among the reframed lines, and that row was rewritten.
The row at `:522` was not. The frame now gives two coordinates for one
fact, and the crafter's build followed the one at `:100-103`. A later
reader, the settle among them, could follow the other one. Contract rule
19 asks that every sentence stating the old fact is rewritten in the same
change.

```markdown
<!-- frame/design.md:522 -->
| The coordinate `changelog/0.12.2.md` and the sentence on how `gather_changelog.py#ungathered` decides | `seal/follow-up.md:47`, `:49` | `changelog/0.12.2.md` at `v0.23.1`, since the v0.12.2 GitHub Release holds neither sentence and is not republished (*Scope* item 8). The rows' questions and answerer stay |

<!-- frame/questions.md:40-42 -->
- **What becomes of the two `seal/follow-up.md` rows that name
  `changelog/0.12.2.md`.** Their coordinate becomes `changelog/0.12.2.md`
  at `v0.23.1`, since the v0.12.2 GitHub Release holds neither sentence and
  is not republished. Their question and their answerer stay.
```

If finding 4's fix removes the two rows, both places instead say the rows
go, in the words that fix gives *Scope* item 8.

answer:

### 4. The two follow-up rows ask a question that no act can now answer, and their reader premise is false

severity: should
location: `seal/follow-up.md:47`, `seal/follow-up.md:49`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:100-103`, `seal/threads/1793188384-the-release-notes-are-kept-twice/frame/design.md:131-132`
evidence: executed `gh release view v0.12.2 -R MichaelYcJo/SpecSeal --json body -q .body`, `grep -n -i -E "404|190 rows|baseline|ledger" notes/v0.12.2.txt`, `git show v0.23.1:changelog/0.12.2.md`
verdict: open

Row 47 asks "whether the label is carried into a released copy of 0.12.2".
Row 49 says "one answer settles both". After this work, only two released
copies of 0.12.2 could take a correction. Neither can be changed.

- The v0.12.2 GitHub Release holds neither sentence (executed: no line
  matches "404", "190 rows", "baseline" or "ledger"). Carrying the label
  or the corrected figure into it means adding the file's text to a
  published note. That is the republish the owner turned down in Q2.
- `changelog/0.12.2.md` holds both sentences, but only in the tree of tag
  `v0.23.1`. Row 47's own words say "no commit after `v0.23.1` holds the
  file". So no branch can amend it short of rewriting a release tag.

So the question has one possible answer, no, and Q2 already gave it: "the
edit buys no reader anything". The row keeps an owner's question open that
nobody can act on, and a sealer weighing `seal/follow-up.md` counts it as
pending.

The rows' premise is also false now. Row 47 says the file at `v0.23.1` "is
the one a reader outside the work item actually reads", and its question
weighs "leaving a true sentence unlabelled where most readers meet it". A
reader of 0.12.2 meets the GitHub Release, which holds neither sentence. A
reader of the tag's file is someone who runs `git show`. The issue's last
*Done when* item says no living text names `changelog/` as where the notes
are. Row 47 names the file at `v0.23.1` as the copy readers read.

The change this calls for is to remove both rows, not to reword them.
*Scope* item 8 and the out-of-scope bullet at `design.md:131-132` keep the
rows as the owner's question, so the orchestrator reframes those two
places, and the crafter deletes the rows.

```markdown
<!-- frame/design.md:100-103, replacing "Those two rows keep ... (*Scope* item 5)." -->
   the two `seal/follow-up.md` rows that name `changelog/0.12.2.md`. Those
   two rows go. Each asked whether a correction is carried into a released
   copy of 0.12.2. The v0.12.2 GitHub Release holds neither sentence and is
   not republished (*Scope* item 5). The only copy holding them is
   `changelog/0.12.2.md` in the tree of `v0.23.1`, which no commit changes.
   The owner's answer to `frame/questions.md` Q2 is the answer to both.

<!-- frame/design.md:131-132 -->
- **Correcting the 0.12.2 sentences the two follow-up rows described.** No
  released copy can take the correction (*Scope* item 8), and the rows go.
```

Then the crafter deletes `seal/follow-up.md:47` and `:49`, each with the
blank line after it. The crafter also adds a `gaps.md` divergence row that
says the rows were removed and cites Q2. `frame/plan.md:61` cites
`seal/follow-up.md:47` and `:49` as evidence that two copies drift. After
the deletion that citation reads `8a1173c8:seal/follow-up.md:47` and
`:49`, the commit the frame was opened at. If the orchestrator reads Q2 as
not covering the rows, the rows stay. In that case each still needs a
question that names an act a person can take, and this round found none.

answer:

## Confirmations

confirms: none
S11 holds as the reframed frame states it (`frame/design.md:148`). In the
clone, `git cat-file -e v0.23.1:changelog/<version>.md` ran for each of the
58 `v*` tags, sorted with `--sort=v:refname`. All 58 exited 0
(executed). `git ls-tree --name-only v0.23.1 changelog/` lists 58 files.
`changelog/0.12.2.md` and `CHANGELOG.md` are absent at `2e0c895d`
(`git cat-file -e` exit 128 each). This matches the table at
`trail/phases/phase-5.md:30-34`. The half of S11 about the 32 notes held in
their GitHub Release is finding 1's.

confirms: none
The `republish` grep in the plan row, re-run in the worktree at
`2e0c895d`, printed the same hits `phase-5.md:68-78` judges, at the same
lines (executed). Each hit in `frame/`, `gaps.md`, `phase-4.md` and
`seal/follow-up.md` states the decision. The round-record hits quote the
frame as it stood at each round's target. Outside the work item and
`seal/follow-up.md`, the word appears only at
`.github/scripts/publish_release_note.py:51` and
`docs/branch-and-release.md:52`, and both state the workflow's rule that a
release already published is never republished. A wider search for the
shape of the republish ran over the work item outside its round records
and over `seal/follow-up.md`: "append", "gh release edit", "folded under",
"the 26", "holds its file", "rebuil" and "backed up" (executed). It found
no sentence saying a republish happens or that S11 waits on one. The
sentences that are now false are false about GitHub, not about the
decision (finding 1).

confirms: none
The crafter's account of the v0.12.2 note holds. `gh release view v0.12.2
--json body` returned 4,345 bytes. Neither "404 marker" nor "a baseline
carried forward drops" occurs in it, and the same two phrases each occur
once in `changelog/0.12.2.md` at `v0.23.1` (executed). This matches
`phase-5.md:40-46`. So the rows' new clause, "the v0.12.2 GitHub Release
does not hold the sentence", is true. Finding 4 is about what the rows ask
after that.

confirms: none
The three commits touch only the paths the prompt names: `10cbc6e9` the
three frame files, `58f3a6a7` `seal/follow-up.md`, `gaps.md` and
`phase-4.md`, and `2e0c895d` `plan.md`'s Status cell and `phase-5.md`
(executed: `git show --stat`). All three are authored by the repository
owner's commit identity (executed: `git log --format='%h %ae %s'`). No
shipped file changed in the range, so no shipped file states a republish.

confirms: none
The narrow verification for this round passed. In the clone, the 20 test
modules under `tests/` that `git grep -l -E "follow-up\.md|1793188384"`
finds ran with `bin/test -q`, with `tests/conftest.py` left out because it
is not a module: 1297 passed, exit 0 (executed). `bin/seal layout --check`
exited 0 (160 files read, 0 refused), and `bin/seal rules --check` exited
0 (all 266 check lines in 55 rule files hold). This is not the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether v0.2.0's note as published now equals its text before the edit. No backup was visible to this round | the v0.2.0 GitHub Release | the orchestrator, against the backup it holds |
| Whether a backup exists for each of the 16 notes finding 1 names | outside the tree | the orchestrator |
| The full suite, the repository-wide lint and the typecheck: unverified | the branch at `2e0c895d` | the orchestrator, at `seal gate`, before the sealer is spawned |
| Whether the tag's job can list the milestones under `contents: write` alone (Q3, default (a)) | `.github/workflows/publish-release.yml` | the orchestrator, reading the log of the tag run of the release carrying this work |
| Step 3 of the update skill run by a session updating across a real release | `skills/update/SKILL.md` | the first person to update to the release carrying this work |

## Probes

| Command | Result |
|---|---|
| `git cat-file -e v0.23.1:changelog/$v.md` for each tag of `git tag -l "v*" --sort=v:refname`, in `bash -c` | 58 versions, 0 non-zero exits |
| `git grep -n -i -E "republish" -- seal/threads/1793188384-the-release-notes-are-kept-twice seal/follow-up.md`, then the same over every other path | exit 0 each; the first lists the hits `phase-5.md` judges, the second only `publish_release_note.py:51` and `docs/branch-and-release.md:52` |
| `git grep -n -i -E "append\|gh release edit\|folded under\|the 26\|26 notes\|after (the )?phase 5\|holds its file\|holds its notes\|every note\|re-?publish\|rebuil\|release edit\|backup\|backed up"` over the work item without its round records, and `seal/follow-up.md` | exit 0; no hit says a republish happens |
| `gh release view v0.12.2 --json body`, then `grep -c` for "404 marker" and "a baseline carried forward drops"; the same two over `git show v0.23.1:changelog/0.12.2.md` | 4,345 bytes; 0 and 0 in the note, 1 and 1 in the file |
| `gh api --paginate 'repos/MichaelYcJo/SpecSeal/releases?per_page=100'` for each release's tag, `updated_at`, body length and whether the body holds the folded full-changelog summary | v0.3.0 to v0.10.0, 16 notes, stamped 2026-10-28T13:53:34Z to 13:54:02Z, each holding the block; v0.2.0 stamped 13:55:41Z without it; v0.11.0 to v0.14.0 stamped in September |
| `test_tmp_notes.py`, run once with `python3 -I` in the clone and then deleted: the *Scope* item 5 criterion over the 58 notes as published now | 10 notes lack their file: 0.2.0, 0.11.0, 0.11.1, 0.11.2, 0.11.3, 0.11.5, 0.12.0, 0.12.2, 0.12.3, 0.13.0 |
| The v0.3.0 note's text between its `<summary>` line and `</details>`, against `changelog/0.3.0.md` at `v0.23.1` without its heading line, blank lines dropped, `diff -q` | exit 0: identical |
| `bin/test -q` over the 20 modules the last confirmation names | 1297 passed, exit 0 |
| `bin/seal layout --check`, `bin/seal rules --check` | exit 0, exit 0 |

The probe file was deleted after its one run, and `git status --short` in
the clone printed nothing. The clone, its `.venv` and the fetched notes sit
under the round's scratch directory, and the scratch directory is removed
before hand-back.
