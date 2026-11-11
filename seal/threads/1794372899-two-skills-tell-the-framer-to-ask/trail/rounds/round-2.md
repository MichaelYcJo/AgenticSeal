# Review round 2: 1794372899-two-skills-tell-the-framer-to-ask

```seal
target: 74e453da3, fixes 2af43c27f..74e453da3
```

This is a verifying round. The range `2af43c27f..74e453da3` holds four commits: the round 1 record (`4adfc5a3d`), the framer's fold of finding 1 (`03606ef77`), the fix (`89a0546cf`), and the close block (`74e453da3`). Its one change outside the records is step 5 of `agents/framer.md`, one hunk that removes four lines and adds five (executed, `git diff 4adfc5a3d..HEAD`). Every command ran in a `git clone --no-local` at `74e453da3` under the round's scratch directory. The branch worktree received this record and nothing else.

The records read at the target are `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/rounds/round-1.md`. The range changes `frame/design.md`, `frame/plan.md`, `gaps.md`, `changelog.md` and `round-1.md`, and each change was read in the diff and in its file. The other four files are unchanged since round 1, which read each whole at `2af43c27f`, and they were read again for any sentence the fix now contradicts (executed, `git diff --stat 4adfc5a3d..HEAD`). Both language keys of `seal/config.json` are English, so no `pr.<lang>.md` stands. No `seal/parity.json` stands.

Carried from round 1 as coordinates and not re-derived, because the range does not touch the files they stand in: the removed skills' text at `7b2b0fe6a`, the README rows, the removed test units, `.test_durations`, and S1's reach. Re-derived this round: step 5 against D1, the byte figures, S1, S7, and the G4 transcript count where the fold rewrote G4.

## Findings

This round opens no finding.

## Confirmations

```seal
confirms: round-1#1
```
What holds: step 5 now reads a library's API in the version the work moves it to as well as the installed one. `agents/framer.md:101-103` reads "a library's API is the one its installed version holds, or the version the work moves it to, read there and not recalled" (read). D1 at `frame/design.md:60-72` stands in `agents/framer.md` word for word, and is 766 B with its longest line 74 columns (executed, a `python3` substring test and a byte count of D1's fence). `wc -c agents/framer.md` gives 15,051 B, 227 B over the base's 14,824 B, the figure S4 (`frame/design.md:49`) and G6 (`:14`) give. `git diff 7b2b0fe6a -- agents/framer.md` holds one hunk, and `git diff --stat 7b2b0fe6a -- skills/core/SKILL.md skills/agent-contract/SKILL.md` prints nothing (executed). D2's row at `frame/design.md:86` and the paragraph at `:74` now say check 3 moved whole, and the row gives check 5's half on features its home in *Scope*, with the base coordinate `:41-43` that holds it (read). `frame/plan.md:15` cites G6 for the figure instead of repeating it. `changelog.md:3` gives 227 bytes and 15,051 and names the version the work moves to, and `changelog.md:13` names it too (read). The close block's claims hold against this: the fix replaced step 5's last four lines, and the narrow run of S7's four modules gave 100 passed, which this round's own run repeats (executed).

What matched: the fold's other rows. G4 at `frame/design.md:12` now says every matching call is an `Edit` or `Write`, of `skills/feature-planner/SKILL.md` in both transcripts and of `skills/confidence-check/SKILL.md` in the first. The transcript holding the `confidence-check` calls opens on 2026-10-21 and the other on 2026-10-27, so "the first" is the one that holds them (executed, the first `timestamp` of each). G8 at `:16` cites round 1's grep over the four files its first list left out, and states what round 1 found there (read). The new row of *Judgments of the run* (`frame/plan.md:46`) names the finding, the fix taken, and the owner's decision it is judged against (read).

What matched: the new unit. The fix diff's only new text an agent acts on is the clause at `agents/framer.md:101-102`. It names the two versions a frame can rest on, keeps "read there and not recalled" for both, and leaves the other two assumptions and the routing to `frame/questions.md` as they were (read). Its lines stay inside 88 columns, and `tests/behaviour/test_docs_line_wrap.py` in S7's run passes on them (executed). The range adds no test, so no case is read against its group.

What matched: S1 and S7 at the target. `git grep -n -i -E 'feature-planner|confidence-check' -- . ':!seal/threads' ':!.test_durations'` printed nothing and exited 1. `bin/test tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/behaviour/test_docs_line_wrap.py tests/text/test_review_axes.py -q` exited 0 with 100 passed (executed).

What matched: `gaps.md`. The range rewords row 1 in place to name fix pass 1's run beside phase 1's, and removes no row (read, the diff).

What matched: `pr.md`. Its three quotes still stand word for word at `frame/plan.md:15`, `:17` and `:45`: the fold changed row 1's failure scenario and left its Verdict cell, and added its new row after `:45` (executed, `grep -n -F` on each quote). The tree's `bin/seal pr-body` composed the body into the round's scratch directory with exit 0 (executed).

What matched: the records the range did not change. `trail/phases/phase-1.md` states the build commit `7ffcf1ab9`, where 15,011 B was the figure, and the target does not contradict it. `frame/plan.md:35` on #1475 still holds: the fix moves the definition's `check:` lines by one more line and changes none of them (read).

What matched: the chain check over this record. `python3 skills/code-review/scripts/chain_check.py --baseline 7b2b0fe6a --root <the branch worktree> --worktree` exited 0 and printed no notice at a line of `frame/design.md` naming a test pin or a copy. Its other lines say git carries no `trail/gate.md` and no `guarantee.md` yet, which the orchestrator's broad run and the sealer write after the rounds (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at HEAD; the suite stays `unverified` in this round, which ran S7's four modules alone | `seal/threads/1794372899-two-skills-tell-the-framer-to-ask/gaps.md:7` | the orchestrator, by `seal gate --record` |
| The test files outside S7 that walk `skills/`, which the crafter's sample lists | `seal/threads/1794372899-two-skills-tell-the-framer-to-ask/gaps.md:8` | the orchestrator, by the broad gate |
| Whether another installation typed either removed command | `seal/threads/1794372899-two-skills-tell-the-framer-to-ask/gaps.md:9` | the owner, from what users report after the release |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/behaviour/test_docs_line_wrap.py tests/text/test_review_axes.py -q`, in the clone | exit 0, 100 passed |
| a `python3` heredoc reading D1's fence from `frame/design.md` and `agents/framer.md` in the clone | D1 is 766 B, stands in `agents/framer.md`, longest line 74 columns; nothing written |
| `git grep -n -i -E 'feature-planner\|confidence-check' -- . ':!seal/threads' ':!.test_durations'`, in the clone | no output, exit 1 |
| `grep -o -m1 '"timestamp":"[^"]*"'` over the two transcripts G4 names | 2026-10-21 for the one holding the `confidence-check` calls, 2026-10-27 for the other |
| `bin/seal pr-body seal/threads/1794372899-two-skills-tell-the-framer-to-ask --body <scratch>/body.md`, in the clone | exit 0, the body written into the round's scratch directory |
