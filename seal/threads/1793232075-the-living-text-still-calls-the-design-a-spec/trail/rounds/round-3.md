# Review round 3: 1793232075-the-living-text-still-calls-the-design-a-spec

target: f3ad1f7e, fixes 8396dff0..f3ad1f7e

This round verifies round 2's one close. It read the diff
`8396dff0..f3ad1f7e` and the lines that diff stands on, and nothing wider.
Two commits make up the range, and no fix pass ran. `3b5c4bb6` changes one
line, `gaps.md:19`. `f3ad1f7e` changes only the `verdict:` and `answer:`
lines of round 2's finding 1 (read, `git diff 8396dff0..f3ad1f7e`).

Some facts are carried from round 2 and not established again here: that
`036b87ab` and `e2b93c49` are the orchestrator's folds of the frame, what
each of them changed, and round 2's two confirmations of round 1. No commit
in the range touches the lines those facts rest on. The count of ten
citations is carried from round 1, which ran `git grep -n -i 'Read the spec'`
at the base. The `frame/design.md` rows at `:162` and `:169` that list them
did not change in the range (read).

## Findings

This round raises no finding.

## Confirmations

confirms: round-2#1
The close holds. `3b5c4bb6` writes round 2's paste-ready row to
`gaps.md:19` word for word, and changes no other line (read, `git diff
8396dff0..f3ad1f7e`). Each claim of the new row was checked against the
tree. The first claim is that the frame said "twelve" when phase 3 was built.
`git grep -n -i -w twelve 3816dfca` over the work item finds it at
`frame/design.md:74` and at `frame/plan.md:31`, `:74` and `:88` (executed).
The second claim is that the orchestrator dropped the count at `036b87ab`
and `e2b93c49`. `git show` of the two commits removes the design line and
the three plan lines (executed). The same search at `f3ad1f7e` finds no
line under `frame/` (executed). The row's one remaining "twelve" is now in
the past tense, so a reader who opens the frame no longer finds a claim it
contradicts. The row's last two cells did not change.

The fix made nothing else false. No other row of `gaps.md` names the count.
`trail/phases/phase-3.md:41-42` still says the frame's two lines "say twelve", and
round 2 left that line as the record of its moment. The orchestrator's
answer says that `bin/seal unverified` on the work item exits 0. Run again,
it exits 0 and reads `gaps.md` as one open row and one closed row (executed).
The open row is the broad gate's, named below. `3b5c4bb6` touches
`gaps.md`, the path the finding's `location:` names, so the `fixed` commit
touches a named path.

Round 2's `evidence: executed` line was run again, and it settles nothing on
this machine. `git grep -n -i -E '\btwelve\b'` prints nothing at `3816dfca`
and at `2d8d8301`, where the word stands on four frame lines (executed).
Round 2's probe row with the same pattern has the same problem. This round
put a `-w` search in its place. That search agrees with round 2's conclusion
at `e2b93c49` and at `f3ad1f7e`, so the close does not rest on the command.
This is not raised as a finding: no later round weighs that finding again,
and round records do not ship in the release.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck. The crafter labels the suite `unverified`, and the label is honest: this round ran only the two modules below. Nothing is open after this round, so the next step is the orchestrator's broad run and then the sealer's spawn | `seal/threads/1793232075-the-living-text-still-calls-the-design-a-spec/gaps.md` | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `git grep -n -i -w twelve <rev>` over the work item, at `3816dfca`, `2d8d8301`, `e2b93c49` and `f3ad1f7e` | four frame lines at `3816dfca` and at `2d8d8301`; no frame line at `e2b93c49` or `f3ad1f7e`; at `f3ad1f7e` the hits are `gaps.md:19`, `trail/phases/phase-3.md:41-42` and the round records |
| `git grep -n -i -E '\btwelve\b'` over the work item's `frame/`, at `3816dfca`, `2d8d8301` and `f3ad1f7e` | nothing printed at any of the three, including the two where the word stands |
| `git show 036b87ab e2b93c49`, lines holding `twelve` | one removed line of `frame/design.md`, three removed lines of `frame/plan.md` |
| `bin/seal unverified seal/threads/1793232075-the-living-text-still-calls-the-design-a-spec` | exit 0; 1 open, 1 closed, 0 unreadable |
| `bin/test -q tests/behaviour/test_chain_hooks_hardening.py tests/skills/test_unverified_check.py` | 363 passed, exit 0 |
| `bin/seal layout --check` | exit 0 |
| `bin/seal rules --check` | exit 0, all 266 check lines in 55 rule files hold |
