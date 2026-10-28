# Phase 5: 1793163944-the-issues-were-filed-against-the-old-tree

| Field | Value |
|---|---|
| Phase | 5, the fix pass of review round 1 |
| Commit | the commit that adds this record, named in `trail/rounds/round-1.md`'s two `verdict:` lines |

## What this phase was asked

The fix pass of `trail/rounds/round-1.md` (`a895ce30`), at `bb9130fc`, where
the orchestrator had already folded both findings' `frame/design.md` lines.
Finding 1: apply the record's paste-ready body changes to #1109, #1110 and
#1111, so #1109's census question moves to #1110 and #1111 names #956 as its
predecessor. Finding 2: run the record's eight `gh issue edit <N> --title`
commands, on the review's default, since the owner has not answered whether
titles change. Write `frame/questions.md` Q2's Status cell. Edit no other
frame file.

## What this phase found

**Both findings hold, judged at their coordinates.** #1109's third *Done
when* bullet asked for a frame that a no-work-item change does not have, and
#1110's body held no census question. #1111's only order sentence named
#1040, and the body never said that #1111 waits for #956. The premise in
`frame/design.md:47-50` was false: #1039's title named a path absent at
`0b75346f`.

**Bodies (executed; each `gh issue edit --body-file` exit code read
directly, each body read back equal to the file sent).**

| Issue | updatedAt before | updatedAt after | Exit code | Change |
|---|---|---|---|---|
| #1109 | 2026-10-28T06:01:52Z | 2026-10-28T06:06:36Z | 0 | third *Done when* bullet replaced with the record's text |
| #1110 | 2026-10-28T05:29:42Z | 2026-10-28T06:06:37Z | 0 | one bullet added to *What this work decides* |
| #1111 | 2026-10-28T05:29:49Z | 2026-10-28T06:06:39Z | 0 | second bullet of *How it differs* replaced; `## Order` added before *Done when* |

#1109's `updatedAt` before the edit was later than its creation in phase 1.
The body as fetched equalled the body phase 1 filed (`diff` against the
fetched body showed only the bullet this pass replaced). The later
`updatedAt` is GitHub's, from an event that left the body unchanged, most
likely the link from #1112.

**Titles (executed; each `gh issue edit --title` exited 0, and each title
read back with `gh issue view <N> --json title` equals the record's text).**

| Issue | Old title | New title |
|---|---|---|
| #712 | fix: session-cost's spawn rows push every cell past its header when an agent's name is longer than the label column | fix: seal cost's spawn rows push every cell past its header when an agent's name is longer than the label column |
| #1039 | test: after #1027's settle, three cases of tests/test_the_hook_surface_git_offers.py still pin what only the retired commit gate inside git needed, at 19.5 s of the serial suite; they go with their .test_durations entries | test: after #1027's settle, three cases of tests/behaviour/test_the_hook_surface_git_offers.py still pin what only the retired commit gate inside git needed, at 16.3 s of the serial suite; they go with their .test_durations entries |
| #1042 | test: the behaviour suite tells the agent under test it is being evaluated, through an eval commit author, .git/specseal-eval/ input paths and a specseal-eval- plugin tree that holds the truth graders | test: the behaviour suite tells the agent under test it is being evaluated, through an eval commit author, .git/agentic-eval/ input paths and an agentic-eval- plugin tree that holds the truth graders |
| #1043 | docs: docs/the-review-record.md cites Measure the segment in skills/verify/SKILL.md, which moved to skills/verify/orchestration.md, and no check reads a citation of any file but implement's | docs: gather_changelog.py cites a heading docs/the-record-layout.md does not have, and no check reads a citation of any file but implement's |
| #1045 | chore: a fix to a work item's own records still costs a verifying round, and 36 of 0.22.x's 226 findings named only seal/ files; chain-check and the sealer confirm a records-only fix, and overview.md's divergence table goes | chore: a fix to a work item's own records still costs a verifying round, and 36 of 0.22.x's 226 findings named only seal/ files; chain-check and the sealer confirm a records-only fix, and gaps.md's divergence table goes |
| #1046 | chore: every orchestrating session reads Bootstrap and Parity setup, 1,836 of the 7,047 words of implement's orchestration, which apply only to a first session or a migration; they move to a file opened when they apply | chore: every orchestrating session reads Bootstrap and Parity setup, 1,993 of the 7,649 words of implement's orchestration, which apply only to a first session or a migration; they move to a file opened when they apply |
| #1048 | feat: the sealer re-runs a sample of the smith's claims and leaves the rest on its word, 23 of 28 mutation claims in #955; it checks every executed claim against the implementer's transcript and re-runs a sample | feat: the sealer re-runs a sample of the crafter's claims and leaves the rest on its word, 23 of 28 mutation claims in #955; it checks every executed claim against the implementer's transcript and re-runs a sample |
| #1049 | chore: the worktree guard has never been weighed against what it costs, about 6,500 lines of hooks and 99 s of tests against no recorded catch; the record decides keep, narrow or remove | chore: the worktree guard has never been weighed against what it costs, about 6,500 lines of hooks and 106 s of tests against no recorded catch; the record decides keep, narrow or remove |

#1049's "about 6,500 lines of hooks" stays as the record writes it. It
matches the guard, `hooks/lib/cmdline_base.py` and `hooks/worktree_consent.py`
together (3,624 + 2,288 + 632 = 6,544 at `0b75346f`, executed in phase 3), and
leaves out `hooks/lib/cmdline.py`, which other hooks also import.

**`frame/questions.md` Q2.** Its Status cell now reads `answered 2026-10-28 by
the crafter: never arose; every updatedAt before an edit was earlier than the
frame's read`, as phases 2 and 3 recorded (executed there). #1109's later
`updatedAt` in this pass is after the frame's read but not someone's edit of
the body, as stated above.

The three body files were written to the crafter's scratch directory outside
the tree and removed by their paths when this phase closed.
