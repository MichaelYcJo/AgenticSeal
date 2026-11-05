# Review round 4: 1793853197-a-bare-commit-goes-or-states-its-reason

```seal
target: d1c2d3f8, fixes 9b2bc6ae..d1c2d3f8
```

This is a verifying round. The range holds two commits. 38cd9881 rewrites
eight statements in `frame/design.md` and `frame/plan.md`. d1c2d3f8 appends
the close block of round 3's finding 1, `fixed 38cd9881`, to
`trail/rounds/round-3.md`. The range changes no file outside `seal/`
(`git diff 9b2bc6ae d1c2d3f8 -- . ':(exclude)seal/'`, empty, executed), so
there is no code, no test and no hex token for the squash case to read.
Round 3 closed one finding, and it is answered below by a `confirms:` line.

No probe was needed: every claim this round weighs is settled by reading the
records and by one `git` query in the worktree. No scratch clone was made.
The worktree was not changed except by this record.

Carried, not re-established: round 3's confirmations of the merged tree at
9591cb4e. They cover the docstring, the module run, M1 and M2, and the
merge. The range touches none of what they cover. Re-run: round 3 finding
1's `evidence: executed` line, `git for-each-ref --contains 3538fd59`, which
still lists only `refs/heads/docs/1382-the-readme-names-two-of-four-network-places`
(executed).

The fix pass's account was read as a claim. Its `answer:` says the
orchestrator applied the paste-ready text at each of the eight statements,
word for word. It also says the dated *Grounding* rows, *Scope* item 3, S1
and S5 stay. The diff of 38cd9881 was read against round 3's fix block line
by line.

## Findings

None. The round opens no finding, so nothing is open for a fix pass. The
range changed only the work item's records after the broad run at 9de1ab25.
What comes due is the orchestrator's broad run at HEAD, since the merge and
caab8bc0 already came after 9de1ab25, and then the sealer's spawn.

## Confirmations

```seal
confirms: round-3#1
```
What holds: each of the eight statements round 3 named now counts row 47,
and each is round 3's text word for word (read, `git diff 9b2bc6ae
d1c2d3f8`). The D1 heading at `frame/design.md:29` now names the 115
lines at `31558c76` and row 47's line from `703ab88c`. D2's first bullet at
`:92` says 35 of 45, with 34 of 44 at `31558c76`. *Scope* item 1 at `:103`
says 86 lines, rows 1 to 40 and row 47. *Removes* at `:174` says 73 lines.
The catch record at `:184` says 35 and names row 47 as the token the case
itself refused. `frame/plan.md:5` names row 47's line at `703ab88c`'s line
numbers and 86 rewritten. `:7` drops "adds". A2 at `:24` says 35, row 47's
among them. Each figure agrees with `changelog.md:3`: 86 lines, 35
unreached and 73 P. It also agrees with the phase 1 addendum's 86 and 73,
and with D1's total paragraph at `frame/design.md:88` (read). The fix
pass's `answer:` describes the plan's technical context as "116 lines". The
sentence itself says 115 lines and one more in row 47. That is the same
count, and the frame carries no wrong figure from it.

What matched, no other statement of D1's totals was missed. The list is a
closed set. Every line of `frame/design.md`, `frame/plan.md`,
`frame/questions.md`, `changelog.md` and `gaps.md` that holds one of the
figures the counts take was found by a `grep` for those figures (executed).
That covers 10, 21, 29, 30, 33 to 35, 44 to 46, 49, 61, 62, 72, 73, 85, 86,
115 and 116, with D1's own rows set aside. Each line found was read in
context (read). Apart from the eight fixed statements, each falls into one
of three groups.

- **A measurement dated at `31558c76`, which the plan's third judgment row
  keeps as read.** These are the *Grounding* rows at `frame/design.md:12`,
  `:17`, `:18`, `:19` and `:20`, each naming the commands it ran. They also
  include the plan's `:15`, which is about a tree case built before phase
  1, and `:25` (A3), which gives M2's 33 of 45 at framing. `:12`'s "Of the 44
  bare tokens D1 rewrites, 34" now matches the dated half of D2's bullet,
  "34 of 44 at `31558c76`".
- **A statement of phase 1's commit.** These are *Scope* item 3 at `:105`,
  S1 at `:122` and S5 at `:126`, which speak of the 115 lines and the 61
  tokens at the base the phase was built on. The phase record keeps its 115
  rows and adds row 116 in its addendum.
- **A figure row 47 does not change.** `:96` says "Of D1's rewrite tokens,
  10 are" reached, and 45 less 35 is still 10. `:93` and `:112` give the 33
  M2 reads as no commit, and row 47's token resolves, so M2 is unchanged.
  Round 3 re-ran it and got 33. `:104` gives 30 data lines in rows 41 to 46.
  `:132` and `:136` give the six bare commits in rows 42 to 46 that the tree
  case reads, and row 47's token is gone from the tree.
  `frame/design.md:21` (lines 34 and 108), `:24` (line 62, rows 21 and 22),
  `:36` (rows 45 and 46), `frame/plan.md:17` (10^8), `:28` (rows 44 to 46)
  and `frame/questions.md:7` (rows 45 and 46) are line numbers, row numbers
  or a probability, not totals. `gaps.md:9` names rows 1 to
  85 and row 116.

The fix range adds no test, so no new case is read against its group.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at d1c2d3f8. The last broad run, at 9de1ab25, predates the merge of 703ab88c and caab8bc0's change to a test module | `trail/gate.md` | the orchestrator, at the broad run at HEAD |
| The sealer's re-run of its withheld claim at the new HEAD | `guarantee.md` | the sealer |

## Probes

| Command | Result |
|---|---|
| `git diff 9b2bc6ae d1c2d3f8 -- . ':(exclude)seal/'` | empty |
| `git for-each-ref --contains 3538fd59`, round 3 finding 1's executed evidence, re-run | `refs/heads/docs/1382-the-readme-names-two-of-four-network-places` alone |
| `grep -nE` over the frame, `changelog.md` and `gaps.md` for the figures the counts take, outside D1's rows | the lines listed under `## Confirmations`, each read |
