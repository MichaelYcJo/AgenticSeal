# Review round 7: 1793188384-the-release-notes-are-kept-twice

target: 9d39e4f6, fixes b5d041c6..9d39e4f6

This is the verifying round after round 6. The fix range holds two
commits, both the orchestrator's: `96610a28` rewrites the second cell of
the phase 5 row in `frame/plan.md`, and `9d39e4f6` writes round 6's
finding 1 `verdict:` and `answer:` lines. No fix pass ran. The round ran in
a `git clone --no-local` of the branch at `9d39e4f6`, held in the round's
scratch directory. The repository declares no `seal/parity.md`, so this
round writes no `original:` line.

Carried from earlier rounds, not established again: the 58 version tags,
and that `v0.23.1` holds all 58 files (S11, executed by phase 5 at
`58f3a6a7`; no commit since touches a tag or `changelog/`). Also carried:
that the v0.12.2 note holds neither 0.12.2 sentence (round 5's third
confirmation). Re-established this round: what `96610a28` changed, the
history behind each clause of the new cell, every sentence in the frame,
`gaps.md`, `changelog.md`, the phase records and `seal/follow-up.md` that
names the two 0.12.2 rows or says a note was or will be republished, and
the published listing.

The account checked. The spawn prompt answers round 6's two `## Not
judged` rows. First, it says the 16 restored notes, and v0.2.0, equal
their backups after whitespace is collapsed. Second, it says "a loop the
owner stopped" at `trail/phases/phase-5.md:42-43` and "a command the
orchestrator believed had been stopped" at `frame/questions.md:48` are
both true: the owner interrupted the command, and the orchestrator took
the interrupt to mean it had not run. Neither claim can be opened from the
tree or the API. The backups are outside the tree, and the API keeps no
earlier body. The two accounts do not contradict each other, and the
listing re-read this round is consistent with both: it shows no note
edited after the restore. The first answer is equality after whitespace
collapse, which is narrower than the byte equality round 6 asked about.
No record claims byte equality: `phase-5.md:43-44` says "restored each one
from its backup". So the remainder is a `## Not judged` row, not a finding.

## Findings

None. The close of round 6's finding 1 holds, and the sweep found no
sentence in the five places that says the two 0.12.2 rows stay or point
anywhere now, or that a published note was or will be republished. Each
hit and how it reads is under the second confirmation below.

## Confirmations

confirms: round-6#1
The phase 5 row no longer says the rows point anywhere. Round 6 asked for
the second cell of `frame/plan.md:74` to be replaced with its block. `git
diff b5d041c6..9d39e4f6 -- frame/plan.md` shows one line changed. The new
second cell equals round 6's block word for word, and the Verification
and Status cells are unchanged (executed). The row still has 4 cells, as
every row of the Phases table does (executed: `awk -F'|'` over
`plan.md:66-74`). Each clause of the new cell was checked against the
history:

- "The phase pointed the two `seal/follow-up.md` rows that name
  `changelog/0.12.2.md` at that file at `v0.23.1`". This holds.
  `git show 58f3a6a7 -- seal/follow-up.md` rewrites both rows to name
  "`changelog/0.12.2.md` at `v0.23.1`" as the released copy, where before
  they named the v0.12.2 GitHub Release. Phase 4's `449e5864` had only
  changed "read at `v0.12.2`" to "read at `v0.23.1`" (executed). So the
  phase 4 row's "the two `seal/follow-up.md` rows" (`plan.md:73`) and this
  clause describe two different edits, and both happened.
- "round 5's fix pass removed both rows". This holds. `git show bb1c65c5
  --stat -- seal/follow-up.md` shows 4 deletions (executed). `git grep`
  for `changelog/`, `0.12.2`, `republish`, `release note`, `GitHub
  Release`, `released copy` and this work item's id finds nothing in
  `seal/follow-up.md` at `9d39e4f6` (executed, exit 1).
- "as *Scope* item 8 now says". This holds: `frame/design.md:100-105`
  reads "Those two rows go" (read).

The close's `answer:` says a grep over the three frame files then found no
other sentence saying the rows stay or point anywhere. This round's wider
grep, described under the next confirmation, finds the same. The verdict
`fixed 96610a28` names a commit that changes `frame/plan.md`, the
finding's `location:`. Because the frame is the orchestrator's to write,
the orchestrator writing both lines is consistent with round 6's finding,
which said "The row is a frame row, so the orchestrator writes it". The
two fix commits are authored by the repository owner's commit identity
and touch only `frame/plan.md` and `round-6.md` (executed: `git show
--stat --format='%h %ae %s'`).

confirms: none
The sweep the spawn prompt asked for found no remaining instance. `git grep
-n -i -E` was run over the frame, `gaps.md`, `changelog.md`,
`trail/phases/` and `seal/follow-up.md` three times. The first pass looked
for `0.12.2`, `follow-up`, `republish`, `re-publish` and "published
again". The second looked for `S11`, `append`, `restor`, `edited`,
`backup`, "left as", `re-point`, "point at", "keep their", `stay`,
"released copy", "v0.12.2 Release" and "release note". The third ran
over the whole tree outside the round records, for `republish`,
`follow-up.md:47`, `follow-up.md:49` and `changelog/0.12.2` (all
executed). Each hit that names the rows or a republish reads as follows:

- `frame/design.md:18`, `:65-81`, `:100-105`, `:133-134` and `:524`,
  `frame/questions.md:40-43`, `frame/plan.md:13-15`, `:74` and `:86`,
  `gaps.md:14-15` and `:27`, `changelog.md:3` and `:8`. Each states the
  decision: no note is republished, the 26 are left as they are, and the
  rows go (read).
- `frame/plan.md:61` names the rows only as readers that
  `8a1173c8:seal/follow-up.md:47` and `:49` held when the frame was
  opened. `plan.md:73` lists them among phase 4's readers, which phase 4
  re-pointed (read).
- `trail/phases/phase-4.md:16-17` and `phase-5.md:12-14` stand in each
  record's `## What this phase was asked`. `phase-5.md:12-14` still reads
  "The two `seal/follow-up.md` rows that name `changelog/0.12.2.md` point
  at that file at `v0.23.1`". `skills/implement/SKILL.md:371-377` defines
  that section as a copy of what the spawn prompt or task asked the phase
  to build. `phase-5.md:10-11` names the plan as reframed at `10cbc6e9`.
  At `10cbc6e9`, the phase 5 row said exactly this (round 6's finding 1
  quotes it). So the sentence is an accurate copy of the ask, and policy,
  not only the fix pass's account, keeps it. The record's own `## What
  this phase found` says the rows went (`phase-5.md:71-80`), and so does
  `phase-4.md:40-42` and `:84-88` (read).
- `frame/questions.md:48`, Q2. The question cell names "The republish of
  the 26 notes" because that is the question the owner answered. Its
  *Default until answered* cell reads "(a), done by the orchestrator in
  phase 5". That cell records the default that applied until the answer.
  Other work items keep that cell once answered, for example
  `seal/threads/1793163944-the-issues-were-filed-against-the-old-tree/frame/questions.md:30`.
  The Status cell gives the answer, "neither; no note is republished",
  and the 17 edits made and restored (read). Read with its Status, the
  row says no note stays republished.
- `phase-5.md:100-106`, the plan row's grep table, is labelled as run at
  `58f3a6a7`. Its coordinates are that commit's, and its row for
  `seal/follow-up.md:47` and `:49` says the rows were removed (read).

No sentence in the five places says the rows stay, say where they point
now, or say a note will be or has stayed republished.

confirms: none
The published state is unchanged since round 6. The release listing,
re-read at 2026-10-28T14:28:45Z with `gh api --paginate
'repos/MichaelYcJo/AgenticSeal/releases?per_page=100'` (a read), returned
58 releases (executed). The summary text "Full changelog — what each
change", the character `U+1F4CB` and a `<details` element appear only in
the notes of v0.15.1 to v0.23.1. No release has an `updated_at` later than
the restore's last stamp, 2026-10-28T14:11:56Z (executed). So nothing was
published or edited on GitHub after the restore that `phase-5.md:40-69`
records.

confirms: none
The narrow verification for this round passed. In the clone, `git grep -l
-E "follow-up\.md|1793188384" -- tests/` finds 21 files. The 20 modules
among them, `tests/conftest.py` left out because it is not a module, ran
with `bin/test -q`: 1297 passed, exit 0 (executed). The list of files is
the same at `b5d041c6` (executed: `diff` of the two lists, exit 0). `bin/seal
layout --check` exited 0 (160 files read, 0 refused), and `bin/seal rules
--check` exited 0 (all 266 check lines in 55 rule files hold). This is not
the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the 17 restored notes equal their backups byte for byte, beyond the equality after whitespace collapse that the orchestrator reports. No record claims more than "restored each one from its backup", and the backups are outside the tree | the GitHub Releases v0.2.0 to v0.10.0 | the orchestrator, if a byte comparison is wanted |
| The full suite, the repository-wide lint and the typecheck: unverified | the branch at `9d39e4f6` | the orchestrator, at `seal gate`, before the sealer is spawned |
| Whether the tag's job can list the milestones under `contents: write` alone (Q3, default (a)) | `.github/workflows/publish-release.yml` | the orchestrator, reading the log of the tag run of the release carrying this work |
| Step 3 of the update skill run by a session updating across a real release | `skills/update/SKILL.md` | the first person to update to the release carrying this work |

This round leaves nothing open. What comes due is the orchestrator's broad
run, `seal gate`, and the sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `git diff b5d041c6..9d39e4f6`, `git show --stat --format='%h %ae %s' 96610a28 9d39e4f6` | one line of `frame/plan.md` and two lines of `round-6.md` changed; both commits by the owner's identity |
| `git show 58f3a6a7 -- seal/follow-up.md`, `git show 449e5864 -- seal/follow-up.md`, `git show bb1c65c5 --stat -- seal/follow-up.md` | phase 4 changed the tag the rows read the file at; phase 5 made the file at `v0.23.1` the rows' released copy; `bb1c65c5` deleted 4 lines |
| `git grep -n -i -E` over the frame, `gaps.md`, `changelog.md`, `trail/phases/` and `seal/follow-up.md`, in the first two passes the second confirmation names | the hits that confirmation lists; none in `seal/follow-up.md` |
| `git grep -n -i -E "republish\|follow-up\.md:4[79]\|changelog/0\.12\.2"` over the tree outside this work item's round records | the work item's hits above, plus `publish_release_note.py:51` and `docs/branch-and-release.md:52`, which state the workflow's own rule |
| `awk -F'\|' 'NR>=66 && NR<=74 && /^\|/ {print NR": "NF-2" cells"}' frame/plan.md` | 4 cells on every row |
| `gh api --paginate 'repos/MichaelYcJo/AgenticSeal/releases?per_page=100'`, at 2026-10-28T14:28:45Z, read with `python3 -I` for the folded block and any `updated_at` after 14:12:00Z | exit 0; 58 releases; the block only in v0.15.1 to v0.23.1; no release updated after the restore |
| `bin/test -q` over the 20 modules the last confirmation names | 1297 passed, exit 0 |
| `bin/seal layout --check`, `bin/seal rules --check` | exit 0, exit 0 |

No probe file was written. The clone, its `.venv`, the fetched listing and
the module lists are in the round's scratch directory, which is removed
before hand-back.
