# Review round 3: 1793718241-a-fix-pass-applied-paste-ready-text-as-given

```seal
target: bbd072d7b, fixes 9659b309e..bbd072d7b
```

This is a verifying round. It read the diff of the last fixes,
`9659b309e..bbd072d7b`, in a `git clone --no-local` at `bbd072d7b`. That
diff holds three commits. `812adbd35` is the orchestrator's `frame/plan.md`
*Judgments of the run* row 3, which routes round 2's regression. `252eaaa38`
is the fix pass, and it changes two lines of `skills/verify/SKILL.md`.
`bbd072d7b` is round 2's close block. Outside `seal/`, the diff touches
`skills/verify/SKILL.md` alone (executed, `git diff --stat
9659b309e..HEAD -- ':!seal/'`).

Carried from rounds 1 and 2 as coordinates, not re-established: the list of
statements of a new case's red, from round 1's two `git grep` probes, which
the fix diff does not touch outside the one rewritten sentence; and the
reading of the fixture at
`evals/behaviour/sealer/rule-sealer-false-red/scaffold.sh:143-146`. Every
verdict below is this round's own.

## Findings

This round opens no finding.

## Confirmations

```seal
confirms: round-2#1
```
What holds: the verify sentence now names the class rule 15 names.
`skills/verify/SKILL.md:42-45` reads "except that a new test asserting that
something is not named, counted, read or let through, where it passes
there, is shown red the way contract rule 15 states" (read). That is the
class of contract rule 15 at `skills/agent-contract/SKILL.md:183-184`, of
`agents/sealer.md:145-147`, of `skills/implement/SKILL.md:164-166` and of
the folded `frame/design.md` *Scope* item 4 (read). This round ran
`git grep -n -i "nothing is named" -- . ':!*.ko.md'` and a wider search for
`nothing is (named|counted|read|let through)`, `asserting that nothing` and
`asserts nothing` (executed). No shipped statement of the class says
"nothing is named" any more. The hits are the work item's own records, the
`skills/verify/scripts/session_cost.py:1613` docstring and the two test
docstrings at `tests/skills/test_chain_check.py:2028` and
`tests/skills/test_rule_changes.py:243`. The wider search adds five lines
that say "nothing is counted" or "nothing is read" of a script and state no
red: `skills/verify/scripts/session_cost.py:1671` and `:1904`,
`skills/verify/scripts/mutation_check.py:117`,
`skills/verify/seal-mutate.md:51` and `tests/skills/test_settle.py:2797`. No skill has
a Korean edition, so the `.ko.md` exclusion leaves out no copy of this
sentence (executed, `git ls-files` for `*.ko.md`).

The close's claims were checked against the tree. It claimed the snippet
was applied as given with the paragraph rewrapped as shown: the seven lines
at `skills/verify/SKILL.md:41-47` match round 2's snippet line for line
(read). It claimed the passage and line-wrap modules passed: they pass
inside this round's S8 run below (executed). It claimed the search prints
`frame/design.md` G7, `frame/plan.md` row 3 and three unrelated docstrings
and comments, and the search above printed those (executed). It claimed
`skills/verify/SKILL.md:292`, "A new test that passed on first run and was
never seen red", stays true. That holds: a guard case that passes at the
base is still never seen red until its guard is removed (read). The crafter's
reading of the four files its fixes touched is a sample by rule 12. The
repository-wide search above covers the spellings named and no others,
and the spellings are an unbounded domain, so it is a sample too.

```seal
confirms: none
```
What matched: `frame/plan.md` *Judgments of the run* row 3, at `812adbd35`.
It routes round 2's `regression: round-1#1` to an ordinary fix pass. The
route is the second row of `skills/code-review/orchestration.md` *A
regression is routed by comparing the fix with the frame*: "the fix did
something the frame does not say, ... a review record's paste-ready fix
applied as given among them" (read). The grounds hold as read. The folded
*Scope* item 4 says "something is not named". The fix at `533801c30` wrote
"nothing is named". That wording came from round 1's paste-ready text at
`trail/rounds/round-1.md:85`. The third route row does not apply. This was
the unit's first regression, since round 1's finding carried no
`regression:` line (`frame/plan.md` row 2, read). The row names the
regression, the route, the comparison and *The run*, which stands at
`docs/running/the-run.md:6` (read). The row says "one word from the class".
The two spellings differ by more than one word. The row quotes both
spellings in its grounds, so a reader can still tell what it judged. That
is no finding.

```seal
confirms: none
```
What matched: the orchestrator's account of `frame/design.md` G7, half of
it. G7 quotes #1216's phase record, "The two cases that expect nothing
passed at the base", as the orchestrator says (read). The line
`git grep "nothing is named"` prints in G7 is not that quotation. It is the
framer's next sentence, "A case asserting that nothing is named passes
against old code that names nothing" (read). That sentence holds for the case
it describes. It is grounding, and it states no class that a party acts on:
*Scope* items 2 to 5 and S3 to S5 state the class in rule 15's words. G7
lies outside the fix diff. So it is no finding.

```seal
confirms: none
```
What matched: the frame's S5, S6 and S7 at `bbd072d7b` (executed).
`git grep -n 'contract rule 15' -- skills/verify/SKILL.md
skills/implement/SKILL.md` printed `skills/implement/SKILL.md:166` and
`skills/verify/SKILL.md:45`. `git grep -n '(rule 15)' -- agents/sealer.md`
printed `agents/sealer.md:147`. `git grep -n 'takes the snippet as the
repair' -- . ':!seal/'` printed nothing and exited 1. `git diff --stat
b47104fa6...HEAD -- ':!seal/'` printed 7 files changed. S8's five modules
gave 282 passed, exit 0 (executed, under `## Probes`). The fix diff adds no
test function, so no new test is read against its group.

This round leaves nothing open. What comes due is the orchestrator's broad
run at HEAD, and the sealer's spawn after it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite beyond the five modules S8 names. The suite stays `unverified` until the broad run at HEAD | `trail/phases/phase-1.md`, *The boundary run*, and round 1's close block | the orchestrator, at its broad run |
| `evals/behaviour/sealer/rule-sealer-false-red/` was not run, since an eval is a paid run. The fix diff does not touch `agents/sealer.md`, and the fixture reading is carried from round 1 | `agents/sealer.md:154` | the orchestrator, where the release runs the sealer's evals |

## Probes

| Command | Result |
|---|---|
| `git grep -n -i "nothing is named" -- . ':!*.ko.md'`, and the same with `-E "nothing is (named\|counted\|read\|let through)\|asserting that nothing\|asserts nothing"` | no shipped statement of rule 15's class says "nothing is named"; the first search prints the work item's records, `skills/verify/scripts/session_cost.py:1613` and two test docstrings; the second adds the five lines the first confirmation names, each saying what a script reads or counts |
| `git grep -n -i "something is not named" -- . ':!*.ko.md'` | `agents/sealer.md:146`, `skills/agent-contract/SKILL.md:183`, `skills/implement/SKILL.md:164`, `skills/verify/SKILL.md:44`, and the work item's records |
| `bin/test -q -p no:xdist` over the five modules S8 names | 282 passed, exit 0 |
| the S5, S6 and S7 commands of `frame/design.md` | as the fourth confirmation gives them |
| `python3 skills/code-review/scripts/chain_check.py --baseline b47104fa6 --root <the branch worktree> --worktree`, before this record | exit 0; it names round 2's finding 1 and the `target:` behind HEAD as owing a verifying round, which this record is; no notice at a line of `frame/design.md` |
