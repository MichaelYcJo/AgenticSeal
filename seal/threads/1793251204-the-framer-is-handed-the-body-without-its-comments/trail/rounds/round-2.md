# Review round 2: 1793251204-the-framer-is-handed-the-body-without-its-comments

target: 5c524020, fixes 66142f5c..5c524020

## Findings

## Confirmations

confirms: round-1#1
The close holds (executed). Claimed in the fix pass's `answer:`: the four
saved traces show side A's run 0 alone calling `gh issue view`, both side B
runs write the orchestrator's line into `## Grounding`, and the paragraph
is replaced with round 1's text. Found: `phase-3.md:67-78` at `5c524020` is
round 1's fenced paragraph word for word. A probe walked every `Bash`
`tool_use` block of the four traces under `<scratchpad>/1158/sides/`, with
its result, and every `Write` and `Edit` of a frame file, naming the
`## ` heading outside a code fence above each line on the issue's comments.
Side A's run 0 ran `gh release view` and then `gh issue view 106 --json
body,comments 2>&1 | head -20` in one Bash call, and both printed the
`gh auth login` prompt. Its line on the relayed body stands under
`## Scope` of `frame/design.md`, and no `Edit` in that trace has an
`old_string` holding that text. Side A's run 1 and both side B runs called
`gh release view`, got the same prompt, and called no `gh issue view`.
Side A's run 1 wrote "the orchestrator executed `gh issue view 106 --json
body,comments` on 2026-10-14 and found no comments" under `## Grounding`.
Side B's run 0 wrote "comments: none, the orchestrator's finding" there,
and run 1 wrote "the orchestrator's finding, `executed` on 2026-10-14".
`agents/framer.md:72-76` sends the spawn's line into `## Grounding` where
`gh` cannot read the issue, which is the paragraph's "step 4 of this work's
definition". `agents/framer.md` at `c48cd5e3`, line 66 inside step 4,
holds `gh release view` too, so "as step 4 of both definitions asks"
holds. The answer's last claim holds: `git grep` for `gh issue view` over
the work item finds no other sentence saying that no run called it. The
sentence "No run wrote a row about the issue's comments" was not
re-established and is carried from round 1, since the fix kept it
unchanged.

confirms: round-1#2
The close holds (read). `gaps.md:5` at `5c524020` is round 1's fenced
sentence word for word. Read against the committed record, each clause
holds. In `phase-3.md:25-28`, `shape-answers-by-run` fails 2 of 2 on
side A and passes 2 of 2 on side B, and `shape-no-measurement-row` passes
2 of 2 on both. The sentence's *Not verified* pointer lands on
`gaps.md:18`, which now agrees with it. The fix pass claimed that the
other sentences on the same fact stand, and each was opened.
`changelog.md:4` says the row grader passed both runs before #1047 and is
kept as a pin "that nothing yet shows red". `evals/scripts/rule_cases.py:20-27`
says what the sixth case's graders read, not what they separated.
`frame/plan.md:21-23` and `routing.md:17` state the frame's and the
orchestrator's intent before the build. The divergence is recorded in the
`gaps.md` *Not verified* row that names the owner, and the fix pass leaves
those two files alone because they are not the crafter's to write.

confirms: none
The fix pass stayed inside the records (executed: `git show --stat` of
`122b609b` and `5c524020`). `122b609b` changes `gaps.md` and
`trail/phases/phase-3.md` only. `5c524020` changes four lines of
`trail/rounds/round-1.md`: the two `verdict:` lines and the two `answer:`
lines, nothing else.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether `Closes #1158` stands while the no-row half is not seen pinned. Round 1's first row carries over unchanged, since the fix pass only made the memo's opening agree with it | `seal/threads/1793251204-the-framer-is-handed-the-body-without-its-comments/gaps.md:18` | the owner, at the pull request |
| Step 4's branch where `gh` can read the issue. No paid run had `gh` authenticated, so no run opened the comments itself. Round 1's second row carries over unchanged | `agents/framer.md:72-74` | the orchestrator, at each framer spawn |
| The full suite, the repository-wide lint and the typecheck. The fix pass touched records only, and the suite stays labelled `unverified`. With nothing open in this round, what comes due is the orchestrator's broad run and then the sealer's spawn | the branch at `5c524020` | the orchestrator, at `seal gate` |

## Probes

| Command | Result |
|---|---|
| `python3 -I <scratchpad>/1158-r2/test_tmp_traces.py` over the four traces under `<scratchpad>/1158/sides/`, printing each Bash call holding `gh ` with its result, and each line on the issue's comments in a `Write` or `Edit` with the `## ` heading above it outside a code fence | exit 0. Side A's run 0 made one call to `gh issue view` and one to `gh release view`, and both printed the `gh auth login` prompt. The other three runs each called `gh release view` once, with the same prompt. The comment line sits under `## Scope` in side A's run 0 and under `## Grounding` in the other three |
| `grep -o` for `"old_string":` text holding the relay sentence, over side A's `traces/000.jsonl` | count 0: no `Edit` replaced the *Scope* sentence |
| `git grep -n -i` for `gh issue view` over the work item, then for sentences saying the sixth case pins the no-row half or that no row is left, over the tree with the round records excluded | exit 0. Outside the round records, phase 3's paragraph is the work item's only sentence on which runs called `gh issue view`. The pin wording stands at `frame/plan.md:21`, `routing.md:17` and `evals/scripts/rule_cases.py:27`, as the second confirmation reads them |
| `git show --stat` of `122b609b` and `5c524020` | two record files and one round record, as the third confirmation says |
