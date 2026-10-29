# Review round 2: 1793240966-the-framer-has-no-read-only-probe

target: fc6e507c, fixes ad4234f4..fc6e507c

## Findings

### 1. The rule's no-row half is now deferred to an orchestrator that no step tells to judge it

severity: should
location: `seal/threads/1793240966-the-framer-has-no-read-only-probe/gaps.md:22`, `seal/threads/1793240966-the-framer-has-no-read-only-probe/frame/design.md:45`, `seal/threads/1793240966-the-framer-has-no-read-only-probe/frame/design.md:48`, `seal/threads/1793240966-the-framer-has-no-read-only-probe/trail/phases/phase-3.md:69-70`
evidence: executed `git grep -n questions.md -- skills/implement/orchestration.md`, `git grep -n questions.md -- agents/proofer.md skills/code-review/`, `git grep -n -e "proofer at review" -e "read by the proofer" -- seal/threads/1793240966-the-framer-has-no-read-only-probe`
verdict: open
reopens: round-1#2

The close of round-1#2 does not hold. Its defect was a `## Not verified`
row whose answerer has no act that reads the rule's no-row half. Contract
rule 4 calls that a deferral to nobody. The fix renamed the answerer and
left that defect in place, for four reasons.

First, the cited grounds do not name the orchestrator. `gaps.md:22` cites
`skills/implement/SKILL.md` *3. The SDD file set*. At
`skills/implement/SKILL.md:334-335` that section says the Status column "is
written by whoever answered", never by whoever asked. It names no party. An
`a measurement` row is answered by whoever runs the measurement, and the
crafter reads `frame/questions.md` too (`agents/crafter.md:31-32`). The
orchestrator wrote Q1 to Q3's Status at `ecaf7c32`. That is a fact about
this work item. It is not a duty the tree gives the orchestrator for every
work item.

Second, writing a Status answers a row. The no-row half asks a different
question: should the row exist at all, because a probe could have answered
it? No step asks the party answering a row to weigh its reason against
`agents/framer.md:146-148`. The search over
`skills/implement/orchestration.md` finds `questions.md` once, at `:24`,
where the framer writes it. The fix pass's account says the same thing.
Its answer to round-1#2 says the reading "rests on the act of answering
each row, not on a stated step". A reader with no stated step is the
"someone will look at it" that rule 4 refuses.

Third, S2's Given is the `rule-framer-sharp-s` case's issue. In that eval
run, no orchestrator answers rows. So for the scenario S2 states, the reader
S2 names at `frame/design.md:45` never runs.

Fourth, the class has one more instance. The fix did not reach it.
`trail/phases/phase-3.md:69-70` still says "The no-row half of the rule is
read by the proofer at review, as S5 already is." Now the sealer meets two
readers for one half: the proofer in the phase record and the orchestrator
in `gaps.md` and the frame (contract rules 12 and 19).

Round 1 offered two honest closes. The one that remains costs no change
outside the work item: state the half as a limit. The other gives an agent
a step that reads `frame/questions.md`. That means widening
`agents/proofer.md` or `skills/implement/orchestration.md`. The frame's
*Scope* Out list puts the proofer's own rules out of this work, and no In
item names the orchestration file. The snippet takes the limit.

```markdown
<!-- gaps.md:22, the row's second cell -->
nobody after round 1. No case reads it since `shape-no-measurement-row` was removed at `7ac24a06`, and no agent definition or orchestration step opens `frame/questions.md` to judge a row's reason against the rule: the proofer's reading list in `agents/proofer.md` does not name the file, and `skills/implement/orchestration.md` names it only where the framer writes it. Round 1 read this work item's own `frame/questions.md` and found no `a measurement` row. For later work items it is a limit of the rule, read only where a person opens a frame

<!-- frame/design.md:45, the S2 row's third cell -->
read: the rule's sentence in `agents/framer.md`. No reader holds it after this work item's round 1 (`gaps.md` *Not verified*). No grader: one refusing every `a measurement` cell failed a correct row in the paid runs, a row about issue comments `gh` cannot read in the runner, so phase 3 removed it at 7ac24a06 (`gaps.md`)

<!-- frame/design.md:48, the S5 row's third cell -->
read: the rule's sentence in `agents/framer.md`. No reader holds it after this work item's round 1 (`gaps.md` *Not verified*). No case: a fixture that holds a Windows-only leg costs more than the sentence it would pin

<!-- trail/phases/phase-3.md:69-70, the sentence after "alone holds S8." -->
The no-row half of the rule has no reader after round 1, and `gaps.md` *Not verified* states it as a limit. `gaps.md` records the divergence.
```

answer:

## Confirmations

confirms: round-1#1
The close holds on all three lines. Read: the `## Grounding` table at
`frame/design.md:3-21` no longer holds the `shape-words-only.md` row, and
the Scope In item at `frame/design.md:27` reads "One grader beyond the four
shared ones". Executed: `git show d2acd3b9` of `frame/design.md`. Its S2 at
`:46` reads "then no row names `a measurement` as who answers", held by "a
`not_contains` regex over `frame/questions.md` for a table cell holding `a
measurement`". Its S8 at `:52` reads "both pass every run of the new side".
`gaps.md:13` quotes these words at `d2acd3b9`. Read: S2 at
`frame/design.md:45` now reads "then no row asks what `shout` returns", and
S8 at `:51` names `shape-answers-by-probe` alone, as `gaps.md:13` now says.
The fix also dropped the Q2 citation, and that holds: Q2's Status at
`frame/questions.md:37` reads "not reached". Executed: `git grep -n -e
"no-row grader" -e "Two graders"` over the work item finds the phrases only
in `trail/rounds/round-1.md`, as the fix pass claimed. One sentence of the
same kind was checked and is not an instance. `frame/plan.md:43` says
`shape_regex` takes `match="not_contains"`, and that is still true at
`evals/scripts/rule_cases.py:421`, the crafter case's `no-probe-left`
grader.

confirms: none
The frame fold `542404ee` is a new unit. Apart from S2's and S5's reader,
which finding 1 reopens, it leaves nothing dangling. Executed: a search of
the work item for `shape-words-only`, `no-row`, `Two graders` and
`not_contains`. Outside the round records, the remaining hits are the two
committed side files under `evals/`, which record the removed grader's
runs, and the history sentences at `frame/plan.md:86`,
`trail/phases/phase-1.md` and `trail/phases/phase-3.md`, each of which says
the grader was removed at `7ac24a06`.

confirms: none
`fc6e507c` changes `trail/rounds/round-1.md` only in its two `verdict:`
lines and its two `answer:` lines. Executed: `git diff ad4234f4 fc6e507c`
of that file lists four removed and four added lines, and all are those
labels.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck over the branch: `unverified`, not run by this round under contract rule 2 | the branch at `fc6e507c` | the orchestrator, at `seal gate --base release/v0.24.1 --record 1793240966-the-framer-has-no-read-only-probe` |
| Whether the new rule made the other four framer cases worse: carried from round 1, still unmeasured | `evals/behaviour/framer/` | the owner, at #947's milestone run |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the worktree into the round's scratch directory, at `fc6e507c` | exit 0 |
| `git grep -n -e "no-row grader" -e "Two graders"` over the work item | exit 0, hits in `trail/rounds/round-1.md` only |
| `git grep -n questions.md -- agents/proofer.md skills/code-review/` | exit 0, one hit, `skills/code-review/scripts/pr_body.py:14` |
| `git grep -n questions.md -- skills/implement/orchestration.md` | exit 0, one hit, `:24` |
| `git grep -n -e "proofer at review" -e "read by the proofer"` over the work item | exit 0, `trail/phases/phase-3.md:69` and two lines of `trail/rounds/round-1.md` |
| `git show d2acd3b9` of `frame/design.md`, the S2 and S8 rows | exit 0, the two rows `gaps.md:13` quotes |
| `git diff ad4234f4 fc6e507c` of `trail/rounds/round-1.md` | exit 0, four lines out and four in, all `verdict:` and `answer:` |
