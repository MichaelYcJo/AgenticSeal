# Review round 3: 1793419351-project-rules-live-in-the-repository

target: d7426b0c, fixes e55812a8..d7426b0c

Round 3 is a verifying round over round 2's fix pass: `c5eec50b` (findings 1 and 2) and `d7426b0c` (the answers). The review stayed inside that diff: rules 12 and 19 of `skills/agent-contract/SKILL.md` and the work item's `changelog.md`. Facts carried from rounds 1 and 2, not re-established: where rules 12 and 19 stand, that no case pins the wording of rule 12, and that `agents/crafter.md` and `skills/code-review/orchestration.md` are #1167's files in this run (`frame/plan.md:33`, read). Every verdict below was reached this round. Each sentence the fix added was read against the text it rests on: `skills/code-review/SKILL.md:167-169` for the unbounded-domain sentence, and the frame's C2 row (`frame/design.md:47`) with its lesson row (`frame/design.md:98`) for what a sample is.

The fix pass's account was read as claims. It claimed that round 2's paste-ready text for finding 1 added a sentence no source states, "a class drawn from the tree has an end". Read, the claim holds: neither `skills/code-review/SKILL.md:167-169` nor the frame's C2 row says it, and round 2 gave it as its own reasoning. It claimed that `agents/crafter.md:177-179` and `skills/code-review/orchestration.md:74-77` stay consistent with the reconciled rules and owe nothing at the merge with #1167. That claim does not hold, and finding 1 gives the grounds. It claimed a 4-module quick set with 78 passed and a 95-module set with 4,458 passed. This round ran its own four modules, 101 passed, and did not re-run either set. No test was added, so no new test is read against its group.

## Findings

### 1. The crafter's step still makes its list by a word search and the check target, and the reconciled rules call that list neither whole nor a sample

severity: should
location: `skills/agent-contract/SKILL.md:162-168`, `skills/agent-contract/SKILL.md:230-234`, `agents/crafter.md:177-179`, `skills/code-review/orchestration.md:74-77`, `seal/threads/1793419351-project-rules-live-in-the-repository/changelog.md:3`
evidence: executed `git grep -n -i -E 'sample|least' -- agents/crafter.md skills/code-review/orchestration.md`, `git diff origin/release/v0.26.0 chore/1167-judgment-where-meaning-is-the-question -- agents/crafter.md skills/code-review/orchestration.md`
verdict: fixed 777ca4d8
reopens: round-2#2

The close does not hold at two of the three places round 2's finding 2 named. The rule 12 and rule 19 part holds: a fix pass that runs only rule 19's search and calls its list a sample now breaks neither rule. The fix pass then claimed that `agents/crafter.md:177-179` and `skills/code-review/orchestration.md:74-77` owe nothing, because they prescribe the word search and the `check:` target, rule 19 names the search as the least one, and rule 12 decides the label. Read against the rules as `c5eec50b` wrote them, the label does not reach the list those two files make.

`c5eec50b` defines a sample by how the list was made, and alone: rule 12 says "a list made that way alone is a sample", and rule 19 says "Where nothing but that search listed them, the list is a sample". The crafter's step prescribes two searches together: "find every other place stating each rule your range reworded or removed, by `git grep` and its `check:` target". `skills/code-review/orchestration.md:75-76` says the same: "by its words and by the `check:` target that holds it". A list made that way is not made by the word search alone, so by their own words neither rule calls it a sample. It is not whole either. A rule's `check:` target is the test module that pins it, one coordinate, and it lists none of the other statements. None of rule 12's three methods made the list: built from what produces the defect, the artefact taken apart, or a command listing each thing holding the property. So the list the crafter's step makes falls between rule 12's two kinds. The step calls it "every other place", and neither file tells the crafter to label it (executed: `git grep -n -i -E 'sample|least'` over the two files returns nothing). A crafter following its own step hands back a word-search list as a whole one. A proofer can call that "a sample handed back as a whole list" only by reading "alone" out of rule 12. That gives two readings of the step's list, and that is the defect round 2 named at these two places. #1167's branch leaves both sentences as they are (executed: the `git diff` on this finding's `evidence:` line), so the merge carries them unchanged.

This is the run's recurring defect: a rule written wider than its source. Neither source has "alone" or "nothing but". The frame's lesson row (`frame/design.md:98`) reads "never by the instances you can see or a grep of one wording", and C2 (`frame/design.md:47`) asks for "a method that makes the list whole". By those words, a list no whole-making method made falls short, whatever other search was joined to the grep. The fragment repeats the narrowing twice: "A list made only from those is handed back as a sample" and "a list made by that search alone is handed back as a sample".

Define a sample by what did not make the list. Then both files' search gives a sample under the rule they cite, and they need no edit. In rule 12, `skills/agent-contract/SKILL.md:163-164`, replace "find only the spellings already seen, and a list made that way alone is a sample." with:

```markdown
find only the spellings already seen, and a list that none of the three
methods made is a sample, whatever searches were joined to make it.
```

In rule 19, `skills/agent-contract/SKILL.md:231-233`, replace "Where nothing but that search listed them, the list is a sample, and the hand-back says so as rule 12 asks." with:

```markdown
Where none of rule 12's three methods listed them, the list is a sample,
and the hand-back says so as rule 12 asks.
```

In the fragment, replace "A list made only from those is handed back as a sample" with "A list none of the three methods made is handed back as a sample", and replace "a list made by that search alone is handed back as a sample" with "a list that search makes without one of those methods is handed back as a sample".

The other route is to edit the step itself. In `agents/crafter.md:177-179` and `skills/code-review/orchestration.md:74-77`, the search would be named the least one, and its list a sample unless one of rule 12's methods made it. That edits #1167's files, so it goes under the orchestrator's integration with #1167, or closes `deferred` naming #1167's work item.

answer: Holds. The paste-ready definitions were read as the contract's reader and checked against `frame/design.md:98` ("never by the instances you can see or a grep of one wording"), C2 at `frame/design.md:47` ("a method that makes the list whole") and `skills/code-review/SKILL.md:167-169`. Each defines a sample as what none of the whole-making methods made, which is what those sources say falls short, and adds no reach of its own. They were applied as written in `9194dd0e`: rule 12 reads "a list that none of the three methods made is a sample, whatever searches were joined to make it", and rule 19 reads "Where none of rule 12's three methods listed them, the list is a sample". The fragment's two sentences were replaced as given in the same commit. `9194dd0e` left one line of rule 12 at 128 columns, which `tests/behaviour/test_docs_line_wrap.py` refused, and `777ca4d8` rewrapped it with no word changed. "alone" and "nothing but that" no longer stand in either rule. Under the new definition, the list `agents/crafter.md:177-179` and `skills/code-review/orchestration.md:74-77` make by the word search and the `check:` target is a sample under rule 12, which they cite, and rule 12 has the hand-back say so. They stay as they are, so the merge with #1167 owes nothing for this finding.

## Confirmations

confirms: round-2#1
Rule 12 now reads "Where the class ranges over an unbounded domain of keywords, spellings or constructs, no method makes the list whole" (`skills/agent-contract/SKILL.md:165-166`, read). That is the qualifier of `skills/code-review/SKILL.md:167-169`, "an enumeration over an unbounded domain, of keywords, spellings or constructs", with nothing added to it. A class drawn from the tree is no longer called endless, so rule 12's "take the artefact apart" method stands for it. The fragment's sentence carries the same qualifier: "a class over an unbounded domain of keywords, spellings or constructs has no whole list" (`changelog.md:3`, read). No other statement of the old wording "has no end" stands in the policy text (executed: `git grep -n -i -E 'has no end|no end,'` over `skills`, `agents`, `docs`, `templates`, `hooks` and `CONTRIBUTING.md`, which returns two code comments on other subjects, `hooks/lib/blocks.py:216` and `skills/verify/scripts/session_cost.py:619`). The fix pass did not apply round 2's paste-ready text, and its grounds hold, as the account above says. The new wording shares no run with `skills/code-review/SKILL.md`: `tests/text/test_no_passage_is_pasted_into_a_second_file.py` passes in this round's narrow run.

confirms: none
The four modules this round ran pass at `d7426b0c` in the branch worktree: 101 passed, exit 0 (executed, `## Probes`). A narrow run, not the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad suite, the repository-wide lint and `seal gate` at HEAD; the fix pass's 4-module set (78 passed) and 95-module set (4,458 passed) were not re-run (`unverified`) | the branch at `d7426b0c` | the orchestrator, by `seal gate --base release/v0.26.0 --record seal/threads/1793419351-project-rules-live-in-the-repository` |
| The fix pass's hand-back, which the spawn prompt says names its word search for other statements as a sample. This round did not have it. Finding 1 is judged from the record's `answer:` lines and from the tree | the fix pass's hand-back | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_the_agent_contract_holds_the_universal_rules.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_docs_line_wrap.py tests/text/test_the_rules_have_one_owner.py -q` | 101 passed, exit 0, in the branch worktree at `d7426b0c`; a narrow run, not the broad gate |
| `git grep -n -i -E 'sample\|least' -- agents/crafter.md skills/code-review/orchestration.md` | no hit, exit 1: neither file labels the list its step makes |
| `git diff origin/release/v0.26.0 chore/1167-judgment-where-meaning-is-the-question -- agents/crafter.md skills/code-review/orchestration.md` | #1167's hunks leave the sentences at `agents/crafter.md:177-179` and `skills/code-review/orchestration.md:74-77` unchanged; its `skills/code-review/orchestration.md` hunk there adds a sentence after them, and its `agents/crafter.md` hunk stands in step 8 near line 60 |
| `git grep -n -i -E 'has no end\|no end,'` over `skills`, `agents`, `docs`, `templates`, `hooks` and `CONTRIBUTING.md` | two code comments on other subjects; no statement of rule 12's old wording |
