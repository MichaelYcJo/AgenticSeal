# Questions for the planner: 1793163944-the-issues-were-filed-against-the-old-tree

## Answered by the tree, not to be reopened

- **No open issue is closed.** Each issue of both milestones still has work
  left at `0b75346f`. Two were partly done since they were filed (#1043's
  first citation by `de11df75`, #1055's items 1 and 2), and each keeps only
  what is left (`frame/design.md` *Verdicts*).
- **#1044's leftover count goes into #947, not a new issue.** #947 is already
  the measurement taken on 0.24.1's final state, and the count is one more
  reading of the same records.
- **The word `spec` for the frame's design is filed as F2, not asked.**
  `seal/process/0.23.0.md` row 2 already records the decision: "the frame's
  design is no longer called a spec". F2's own frame decides the word that
  replaces it.
- **The three new issues go into `release: 0.24.0`.** Its purpose is "review
  the renamed tree and lighten what it carries, first the checks", and each of
  F1, F2 and F3 is a leftover of the rename or a check that reads text.
- **Only #1040's title changes.** It names three agents that no longer exist,
  which the next framer reads first; every other title still names what its
  issue is about.
- **#1046's Parity setup section may become a pointer instead of moving.** The
  fold states the duplication with its evidence; #1046's framer chooses.
- **#1096 stays in 0.24.0.** The owner decided it on 2026-10-28 with #1049
  already in 0.24.1, and its larger half, removing `SPECSEAL_LINT`, does not
  touch the guard.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does #920, the fix to two `[worktree-ok]` hints of `hooks/worktree-guard.py#steer_to_switch`, leave 0.24.0's small fixes for 0.24.1, to be decided inside #1049? The tree cannot answer it: the owner placed #920 among the small fixes, and #1049, which decides whether the guard stays, narrows or goes, came later | a person | (a) Move #920 to 0.24.1 and add it to #1049's list of guard issues to close or carry: no chain run is spent on a hint the guard's removal would delete; the hint stays wrong until #1049 decides. (b) Keep #920 in 0.24.0: the hint is fixed sooner, at the cost of one chain run that may be removed. (c) Move #1049 into 0.24.0 ahead of #920 and #1096: every guard edit follows the decision, and 0.24.0 takes on a decision that 0.24.1's purpose, lightening the process, was planned to hold | (a): the crafter moves #920, comments the reason, and both descriptions are written for it | answered 2026-10-28 by the owner: (b), #920 stays in 0.24.0 among the small fixes |
| Q2 | An issue body edited by someone after the frame's read on 2026-10-28 | the work | The crafter applies the issue's row to the body as fetched. Where the later edit already made a change the row names, the crafter records that and does not repeat it. Where it contradicts the row, the crafter keeps the later edit and records the conflict in the phase record for the review | Apply the row to the body as fetched, and record each difference | answered 2026-10-28 by the crafter: never arose; every updatedAt before an edit was earlier than the frame's read |
