# Review round 2: 1793718241-a-fix-pass-applied-paste-ready-text-as-given

```seal
target: 4d478f0f3, fixes e39849086..4d478f0f3
```

This is a verifying round. It read the diff of the last fixes,
`e39849086..4d478f0f3`, in a `git clone --no-local` at `4d478f0f3`. That
diff holds three commits. `533801c30` is the fix pass and changes
`agents/sealer.md`, `skills/verify/SKILL.md`, `skills/implement/SKILL.md`
and the work item's `changelog.md`. `6ad052ce3` is the orchestrator's fold
of `frame/design.md` *Scope* items 3 to 5, S4 and S5, with `frame/plan.md`
*Judgments of the run* row 2. `4d478f0f3` is round 1's close block.

Carried from round 1 as coordinates, not re-established: the list of
statements of a new case's red (round 1's two `git grep` probes, which the
fix diff does not touch outside the three rewritten sentences), and the
reading of the fixture at
`evals/behaviour/sealer/rule-sealer-false-red/scaffold.sh:143-146`, whose
phase record claims a red against the code before the change and not a
guard red. Every verdict below is this round's own.

## Findings

### 1. The verify sentence gives rule 15's guard red to a case asserting that nothing is named, where rule 15 and every other citing sentence give it to a case asserting that something is not named

```seal
severity: should
location: `skills/verify/SKILL.md:43-45`
evidence: executed `git grep -n -i -E "nothing is named|something is not named" -- . ':!*.ko.md'`
regression: round-1#1
```

Why it matters: the unit is the new-test sentence of `skills/verify/SKILL.md`
*2. Able to fail*, at `:43-45`, which `533801c30` rewrote. The folded frame
says at `frame/design.md` *Scope* item 4 that "A new test that asserts
something is not named, counted, read or let through, where it passes
there, is shown red as contract rule 15 says". The fix wrote "a new test
asserting that nothing is named, counted, read or let through". The defect
came from round 1's paste-ready text for this sentence, which kept "nothing
is named" from the old example, and the fix pass took that class into its
own words.

The two classes differ. Contract rule 15 at
`skills/agent-contract/SKILL.md:183-184` names "A case that asserts
something is not named, counted, read or let through". That is a case
asserting that one given thing is absent, such as #1216's case asserting
that the Korean edition is not named (`frame/design.md` G7). "A new test
asserting that nothing is named" is a case asserting that no thing at all
is named. It is a narrower class. A crafter at a completion claim reads
verify for a case asserting that one file is not named. Verify then says
the case must be observed failing against the pre-change code, which rule
15 says it cannot do. Rule 15 sends the same case to a guard red. So the
two documents give the crafter two answers for one case.

The search under `evidence:` prints the spelling at every other statement
of the class. `agents/sealer.md:146`, `skills/implement/SKILL.md:164`,
rule 15 at `:183`, the frame's items 2 to 5, S3 to S5, and both changelog
clauses (`changelog.md:4`, `:11`) say "something is not named". The
changelog says verify cites rule 15 "for such a case", so the release note
already states the class verify does not. Only `skills/verify/SKILL.md:44`
says "nothing is named". The other hits outside this work item are
unrelated docstrings and a script line.

The snippet below is the one statement the fix owes, since every other
statement already holds the frame's class. A probe applied it in the
clone and ran `tests/text/test_no_passage_is_pasted_into_a_second_file.py`
and `tests/behaviour/test_docs_line_wrap.py`: 55 passed, exit 0. The
shared run with the implement sentence, "asserting that something is not
named, counted, read or let through", is eleven words, and the passage
module refuses fifteen. The phase record's quotation of the old wording at
`trail/phases/phase-1.md:60` is phase 1's history, and the fix pass owes it
nothing.

```text
skills/verify/SKILL.md, 2. Able to fail, lines 42-48:

change (or fails when the change is reverted). For a new test: it was
observed failing against the pre-change code, except that a new test
asserting that something is not named, counted, read or let through, where
it passes there, is shown red the way contract rule 15 states. A check that
has never been seen red is a counterfeit seal. This is the condition
generic gates skip, and the one that catches assertion-free tests,
mocked-away behavior, and wrong-file test runs.
```

```seal
verdict: fixed 252eaaa38
answer: The finding holds. Contract rule 15 at `skills/agent-contract/SKILL.md:183-184` and `frame/design.md` *Scope* item 4, as folded at 6ad052ce3, name a case that asserts something is not named, counted, read or let through, and my fix at 533801c30 wrote "nothing is named", which leaves out a case asserting that one given file is not named. Before applying the paste-ready text I read it against *Scope* item 4 and rule 15: it names the same class in the same words, and it changes nothing else in the sentence. So 252eaaa38 applies it as given, with the paragraph rewrapped as the snippet shows. `tests/text/test_no_passage_is_pasted_into_a_second_file.py` and `tests/behaviour/test_docs_line_wrap.py` gave 55 passed, exit 0. Then I read every file my two fix commits touched for another statement of the class: `agents/sealer.md`, `skills/verify/SKILL.md`, `skills/implement/SKILL.md` and the work item's `changelog.md`. Each other statement says "something is not named" in rule 15's words (`agents/sealer.md:145-146`, `skills/implement/SKILL.md:164-165`, `changelog.md:4` and `:11`). `skills/verify/SKILL.md:292`, "A new test that passed on first run and was never seen red", stays true. `git grep -n -i "nothing is named"` outside `trail/` and the Korean editions now prints no shipped sentence of the class. It prints `frame/design.md` G7, the framer's description of #1216's case, `frame/plan.md` *Judgments of the run* row 3, and three unrelated docstrings and comments.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the defect round 1 named, a guard red given to every case that
passes before the change, is gone from all three sentences and both
changelog clauses (read). `agents/sealer.md:145-147` keys the exception on
the case's class and the record's claim together: "unless it asserts that
something is not named, counted, read or let through and its record says
it was shown red with its named guard alone removed (rule 15)".
`skills/implement/SKILL.md:164-166` and `skills/verify/SKILL.md:43-45` no
longer make every case green at the base the class, and give the red to an
absence case alone. The verify sentence's class is narrower than rule 15's,
which is finding 1 and a defect of its own. The close's other claims were
checked. It claimed it applied the sealer text with one change, the
removal moved after the guard re-run. `agents/sealer.md:142-150` now runs
the named case with no removal in the first sentence, re-runs a guard case
"in that clone, with HEAD's code restored", and then reads "Remove the
clone once its runs are done" (read). So the guard re-run no longer names
a clone that is gone, and "its" has one referent, the clone. The fix pass
claimed its `git grep -n "rule 15"` over `agents skills docs templates
CONTRIBUTING.md README.md` prints the three fixed lines and no other
citation. The same search, run in the clone, printed
`agents/sealer.md:147`, `skills/implement/SKILL.md:166` and
`skills/verify/SKILL.md:45` and nothing else (executed). The
`at-base` clone has one other mention, `agents/sealer.md:48`, and it says
nothing of when the clone is removed (read).

```seal
confirms: none
```
What matched: the orchestrator's fold at `6ad052ce3`. `frame/design.md`
*Scope* items 3 to 5, S4 and S5 now state the class rule 15 names and the
sealer's re-run in its clone with HEAD's code restored, then the clone's
removal (read). `frame/plan.md` *Judgments of the run* row 2 records the
fold with its grounds and the document it judged against, and says round
1's finding took an ordinary fix pass because it carried no `regression:`
line, as `skills/code-review/orchestration.md` routes it (read). The folded
item 4 is the frame finding 1 sets the verify sentence beside.

```seal
confirms: none
```
What matched: the frame's S5, S6 and S7 at `4d478f0f3` (executed).
`git grep -n 'contract rule 15' -- skills/verify/SKILL.md
skills/implement/SKILL.md` printed one line in each and exited 0.
`git grep -n '(rule 15)' -- agents/sealer.md` printed `agents/sealer.md:147`.
`git grep -n 'takes the snippet as the repair' -- . ':!seal/'` printed
nothing and exited 1. `git diff --stat b47104fa6...HEAD -- ':!seal/'`
printed 7 files changed, so the fix pass added no file outside `seal/`.

```seal
confirms: none
```
What matched: the crafter's claim that `trail/phases/phase-1.md:60` quotes
the verify sentence's old wording and stands as phase 1's history. A fix
pass appends close blocks and writes no phase record
(`agents/crafter.md` *A fix pass appends close blocks and writes no phase
record*, read), and the quotation describes the text at phase 1's commit
(read). It is no finding.

```seal
confirms: none
```
What matched: the narrow cases that read the edited files still hold at
`4d478f0f3`. `bin/test -q -p no:xdist
tests/text/test_a_moved_rule_leaves_its_definition.py
tests/text/test_no_passage_is_pasted_into_a_second_file.py
tests/behaviour/test_docs_line_wrap.py
tests/text/test_the_agent_contract_holds_the_universal_rules.py
tests/text/test_every_agent_reads_the_contract.py` gave 282 passed, exit 0
(executed). The fix diff adds no test function, so no new test is read
against its group. The implement sentence at
`skills/implement/SKILL.md:164-166` chains two "that" clauses ("let through
that is already green"), where the frame's item 5 has "and is already
green". The second clause is read as the case's, since the thing a case
asserts absent is not what goes green, so the sentence has one reading and
is no finding (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The fix pass's 106-module boundary run at `533801c30`, 5222 passed and 12 skipped. This round ran the five modules S8 names and not the rest. The suite stays `unverified` until the broad run at HEAD | round 1's close block, `trail/rounds/round-1.md` | the orchestrator, at its broad run |
| `evals/behaviour/sealer/rule-sealer-false-red/` was not run, since an eval is a paid run. The paragraph it checks changed at `533801c30`, and its fixture claims a red against the code before the change, so the new exception does not reach it (read, carried from round 1) | `agents/sealer.md:154` | the orchestrator, where the release runs the sealer's evals |

## Probes

| Command | Result |
|---|---|
| `git grep -n -i -E "nothing is named\|something is not named" -- . ':!*.ko.md'` | `skills/verify/SKILL.md:44` alone says "nothing is named" among the statements of rule 15's class; `agents/sealer.md:146`, `skills/implement/SKILL.md:164`, `skills/agent-contract/SKILL.md:183`, the frame and both changelog clauses say "something is not named"; other hits are `skills/verify/scripts/session_cost.py:1613` and two test docstrings, unrelated |
| finding 1's snippet applied to `skills/verify/SKILL.md` in the clone with the `Edit` tool, then `bin/test -q -p no:xdist tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_docs_line_wrap.py` | 55 passed, exit 0; the patch was reverted with the `Edit` tool and `git status --short` printed nothing |
| `bin/test -q -p no:xdist` over the five modules S8 names | 282 passed, exit 0 |
| the S5, S6 and S7 commands of `frame/design.md` | as the third confirmation gives them |
| `git grep -n -i -E 'remove the clone\|clone is removed\|and remove the' -- agents skills docs` and `git grep -n "at-base" -- . ':!seal/threads'` | no statement of the sealer's clone removal other than `agents/sealer.md:149-150`; `agents/sealer.md:48` names the clone and not its removal |
