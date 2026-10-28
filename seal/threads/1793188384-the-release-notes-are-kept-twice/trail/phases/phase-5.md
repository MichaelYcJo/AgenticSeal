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

So each version keeps its text: the 32 *Scope* item 5 measured, in their
GitHub Release, and every one of the 58, the other 26 among them, in its
file at `v0.23.1`.

**The two follow-up rows needed more than a coordinate (executed).** Phase 4
had them name the v0.12.2 GitHub Release as the released copy, whose folded
text would be the file after the republish. `gh release view v0.12.2 --json
body`, a read, returned a 4,345-byte note that holds neither sentence the
rows are about. `grep -c` found 0 matches each for "404 marker" and "a
baseline carried forward drops". The same two counts over
`changelog/0.12.2.md` at `v0.23.1` were 1 each. So each row now names
`changelog/0.12.2.md` at `v0.23.1` as the released copy, says the v0.12.2
Release does not hold the sentence and is not republished, and gives as the
reason the copy does not close that no commit after `v0.23.1` holds the
file. Each keeps its question and its answerer. The first row's question
names "a released copy of 0.12.2" where it named the v0.12.2 release note.
The second row loses its sentence that one edit of the v0.12.2 release note
can carry the correction, because that note holds no figure to correct.

**The records rewritten to the decision.** `phase-4.md:21-23` says phase 5
is not built there and that Q2's answer made it a phase in which no note is
republished. `:39-43` names the file at `v0.23.1` as the released copy.
`:47-54` counts the 26 as the versions whose note lacks its file's text,
not the ones a republish covers. `:83-87` describes the rows as this phase
left them. `gaps.md` now has a divergence row saying the issue's
"republished from the file" is not built (Q2). Its row on where a released
file is read no longer speaks of a republish. Its S11 row is closed on the
measurement above. `changelog.md` never said a republish happens (read).

**The plan row's grep (executed at `58f3a6a7`, before this record).** `git
grep -n -i -E "republish" -- seal/threads/1793188384-the-release-notes-are-kept-twice
seal/follow-up.md`, each hit judged:

| Hit | States the decision? |
|---|---|
| `seal/follow-up.md:47`, `:49` | yes: "it is not republished (that work item's `frame/questions.md` Q2)" |
| `frame/design.md:18` | yes, the orchestrator's: the *Grounding* row on the workflow's "never republishes" |
| `frame/design.md:74`, `:78`, `:103` | yes, the orchestrator's: *Scope* items 5 and 8 |
| `frame/plan.md:74` | yes, the orchestrator's: the phase 5 row |
| `frame/questions.md:47` | yes: Q2 itself, the question the owner answered, with its Status |
| `gaps.md:14` | yes: the divergence row this phase added |
| `trail/phases/phase-4.md:23`, `:43` | yes: rewritten in this phase |
| `trail/rounds/round-1.md:217`, `:231`, `:376`; `round-2.md:225`; `round-3.md:233`; `round-4.md:144` | no, and they stay: each quotes the frame as it read at that round's target, or lists S11 under *Not judged* at that round. A round record carries the commit it reviewed and asserts no present state |

This record's own sentences that name the decision are hits too, once it is
committed.
