# Phase 5: 1793188384-the-release-notes-are-kept-twice

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | 58f3a6a7 |

## What this phase was asked

Build phase 5 of `frame/plan.md` as the orchestrator reframed it at
`10cbc6e9`. The owner answered `frame/questions.md` Q2 on 2026-10-28, and
under that answer no published note is republished. The two `seal/follow-up.md`
rows that name `changelog/0.12.2.md` point at that file at `v0.23.1`, since
the v0.12.2 Release is not republished. Every record of this work item that
says a republish happens, or that S11 waits on one, is rewritten to the
decision: the `gaps.md` *Not verified* S11 row, `phase-4.md:21-22` and
`:44-52`, and `changelog.md` if it says so. A `gaps.md` divergence row
records that the issue's "republished from the file" is not built, citing
Q2. S11 runs `git cat-file -e v0.23.1:changelog/X.Y.Z.md` over the 58
versions, and each exit code is recorded here. The plan row's `git grep`
for "republish" runs, and each hit is judged. Nothing is published or edited
on GitHub.

## What this phase found

**S11 (executed 2026-10-28, at `58f3a6a7`).** `git cat-file -e
v0.23.1:changelog/<version>.md` for each of the 58 `v*` tags, read with
`--sort=v:refname`. All 58 exit 0:

| Versions | Exit code |
|---|---|
| 0.0.1, 0.1.0, 0.2.0, 0.3.0, 0.4.0, 0.5.0, 0.6.0, 0.7.0, 0.8.0, 0.8.1, 0.8.2, 0.8.3, 0.9.0, 0.9.1, 0.9.2, 0.9.3, 0.9.4, 0.9.5, 0.10.0 | 0 each |
| 0.11.0, 0.11.1, 0.11.2, 0.11.3, 0.11.4, 0.11.5, 0.12.0, 0.12.1, 0.12.2, 0.12.3, 0.13.0, 0.13.1, 0.13.2, 0.14.0, 0.15.0, 0.15.1, 0.15.2, 0.15.3, 0.15.4 | 0 each |
| 0.15.5, 0.15.6, 0.15.7, 0.16.0, 0.17.0, 0.18.0, 0.18.1, 0.18.2, 0.18.3, 0.19.0, 0.20.0, 0.21.0, 0.21.1, 0.22.0, 0.22.1, 0.22.2, 0.22.3, 0.22.4, 0.23.0, 0.23.1 | 0 each |

So each version keeps its text. The 32 notes *Scope* item 5 measured hold
it in their GitHub Release, and all 58 files, the other 26 among them, are
at `v0.23.1`.

**The published notes after the restore (executed 2026-10-28T14:13:26Z).**
On 2026-10-28 the notes of v0.2.0 to v0.10.0, 17 of the 26, were edited by
appending the file folded under the summary. v0.2.0 was edited once and the
others in a loop the owner stopped. The orchestrator restored each one from
its backup the same day. This phase did not see the edits. Round 5 found
them, and this record states them. `gh api --paginate
'repos/MichaelYcJo/AgenticSeal/releases?per_page=100'`, a read, listed 58
releases. For each of the 26, its `updated_at` and whether its body holds
the summary `📋 Full changelog — what each change does and why`:

| Release | `updated_at` | Holds the folded block |
|---|---|---|
| v0.2.0 | 2026-10-28T13:55:41Z | no |
| v0.3.0, v0.4.0, v0.5.0 | 2026-10-28T14:11:30Z, 14:11:31Z, 14:11:33Z | no |
| v0.6.0, v0.7.0, v0.8.0 | 2026-10-28T14:11:35Z, 14:11:37Z, 14:11:39Z | no |
| v0.8.1, v0.8.2, v0.8.3 | 2026-10-28T14:11:40Z, 14:11:42Z, 14:11:44Z | no |
| v0.9.0, v0.9.1, v0.9.2 | 2026-10-28T14:11:45Z, 14:11:47Z, 14:11:49Z | no |
| v0.9.3, v0.9.4, v0.9.5 | 2026-10-28T14:11:51Z, 14:11:52Z, 14:11:54Z | no |
| v0.10.0 | 2026-10-28T14:11:56Z | no |
| v0.11.0, v0.11.1, v0.11.2 | 2026-09-23T03:15:39Z, 03:15:38Z, 03:15:37Z | no |
| v0.11.3, v0.11.5, v0.12.0 | 2026-09-23T02:35:06Z, 02:35:13Z, 02:35:16Z | no |
| v0.12.2, v0.12.3, v0.13.0 | 2026-09-23T02:35:23Z, 02:35:26Z, 02:35:30Z | no |

The 16 stamps from 14:11:30Z to 14:11:56Z are the restore. The summary
stands in the notes of v0.15.1 to v0.23.1 alone, which the tag's job
published with it. The *Scope* item 5 criterion, re-run over the 58 as one
deleted `test_tmp_*` probe, compares each paragraph of the file at
`v0.23.1` below its heading line, whitespace collapsed, with the note,
whitespace collapsed. 32 notes hold their file and 26 do not, the same 26
*Scope* item 5 lists.

**The two follow-up rows went.** This phase first re-pointed them. `gh
release view v0.12.2 --json body`, a read, returned a 4,345-byte note
holding neither sentence the rows are about: 0 matches each for "404
marker" and "a baseline carried forward drops", against 1 each in
`changelog/0.12.2.md` at `v0.23.1`. So no released copy of 0.12.2 can take
a correction. The note is not republished (Q2), and the file stands in the
tree of `v0.23.1`, which no commit changes. Round 5, finding 4, found the
rows' question had only Q2's answer. The fix pass deleted both rows, each
with the blank line after it, as the frame now says, and `gaps.md` records
it.

**The records rewritten to the decision.** `phase-4.md:21-23` says phase 5
is not built there and that Q2's answer made it a phase in which no note is
republished. `:40-42` and `:84-88` say the two follow-up rows were removed.
`:47-54` counts the 26 as the versions whose note lacks its file's text,
not the ones a republish covers. `gaps.md` now has a divergence row saying
the issue's "republished from the file" is not built (Q2), and naming the
*Done when* clause it departs from. It records the 17 notes edited and
restored, and holds a row on the follow-up rows' removal. Its row on where
a released file is read no longer speaks of a republish. Its S11 row is
closed on the measurement above. `changelog.md` never said a republish
happens (read).

**The plan row's grep (executed at `58f3a6a7`, before this record).** `git
grep -n -i -E "republish" -- seal/threads/1793188384-the-release-notes-are-kept-twice
seal/follow-up.md`, each hit judged:

| Hit | States the decision? |
|---|---|
| `seal/follow-up.md:47`, `:49` | yes then: "it is not republished (that work item's `frame/questions.md` Q2)". Both rows were removed in round 5's fix pass |
| `frame/design.md:18` | yes, the orchestrator's: the *Grounding* row on the workflow's "never republishes" |
| `frame/design.md:74`, `:78`, `:103` | yes, the orchestrator's: *Scope* items 5 and 8 |
| `frame/plan.md:74` | yes, the orchestrator's: the phase 5 row |
| `frame/questions.md:47` | yes: Q2 itself, the question the owner answered, with its Status |
| `gaps.md:14` | yes: the divergence row this phase added |
| `trail/phases/phase-4.md:23`, `:43` | yes: rewritten in this phase |
| `trail/rounds/round-1.md:217`, `:231`, `:376`; `round-2.md:225`; `round-3.md:233`; `round-4.md:144` | no, and they stay: each quotes the frame as it read at that round's target, or lists S11 under *Not judged* at that round. A round record carries the commit it reviewed and asserts no present state |

This record's own sentences that name the decision are hits too, once it is
committed.
