# Review round 4: 1793419351-project-rules-live-in-the-repository

target: 837ac652, fixes bc44b3f5..837ac652

Round 4 is a verifying round over round 3's fix pass: `9194dd0e` (finding 1), `777ca4d8` (a rewrap of the same paragraph) and `837ac652` (the answer). The review stayed inside that diff: rules 12 and 19 of `skills/agent-contract/SKILL.md`, the work item's `changelog.md` and the answer line of `round-3.md`. Facts carried from rounds 1 to 3, not re-established: that no case pins the wording of rule 12 or rule 19, and that `agents/crafter.md` and `skills/code-review/orchestration.md` are #1167's files in this run (`frame/plan.md:33`). Every verdict below was reached this round. The new definition of a sample was read word by word against the three sources the rule rests on: the frame's lesson row (`frame/design.md:98`), its C2 row (`frame/design.md:47`) and `skills/code-review/SKILL.md:167-169`. Reading rule 12 whole against the third source led one step outside the fix diff, to the sentence after the definition, and finding 1 is what that read found.

The fix pass's account was read as claims. It claimed the paste-ready text of round 3's finding 1 was applied as written in `9194dd0e`. Read against round 3's fenced blocks, the claim holds for rule 12, rule 19 and both sentences of the fragment. It claimed `777ca4d8` rewrapped one line with no word changed. A word diff of the two commits shows no changed word (executed, `## Probes`). It claimed a 4-module set with 78 passed and a 95-module set with 4,458 passed. This round ran its own four modules, 101 passed, and did not re-run either set. No test was added, so no new test is read against its group.

## Findings

### 1. Rule 12 no longer asks the hand-back to say that a list over an unbounded domain is open when one of its methods made the list

severity: should
location: `skills/agent-contract/SKILL.md:166-168`, `seal/threads/1793419351-project-rules-live-in-the-repository/changelog.md:3`
evidence: executed `git show c5eec50b^:skills/agent-contract/SKILL.md`, `git grep -n -i -E 'open part|says so' -- skills agents docs templates CONTRIBUTING.md`
verdict: fixed 4d63917c
regression: round-2#1

The unit is the sentence of rule 12 that `c5eec50b` rewrote for round 2's finding 1: "Where the class ranges over an unbounded domain of keywords, spellings or constructs, no method makes the list whole." It ends at that point. The frame's C2 (`frame/design.md:47`, phase 2's row of `frame/plan.md`) asks for a method that makes the list whole and has the hand-back name the method. The fix restored the source's unbounded-domain qualifier. It also dropped the clause `9ad3b9f9` had put after it, "the hand-back says so, and names where the open part is recorded", and moved the duty to state an open part onto "a sample" alone. The defect came from that move, and `9194dd0e`'s definition of a sample now settles it.

The source is `skills/code-review/SKILL.md:167-169`: an enumeration over an unbounded domain "narrows a finding and does not close it; the verdict says so". Rule 12 keeps the first half: no method makes the list whole. The second half now reaches only a sample. The hand-back "calls a sample a sample, and says where its open part stands" (`skills/agent-contract/SKILL.md:168`). Since `9194dd0e`, a sample is "a list that none of the three methods made". Take a list one of the methods did make over an unbounded domain. An example is every spelling of a phrase in the tree, listed by a command, for a check that may be handed spellings the tree does not hold. That list is not a sample, and by the sentence before it, no method makes it whole. No sentence of rule 12 asks the hand-back to say it is open. "its open part" reads as the sample's, the nearest noun, or as the list's. Only the second reading reaches this list. This is the shape round 3's finding 1 named: a list between rule 12's two kinds, with two readings of what the hand-back owes it.

The crafter reads rule 12 and not `skills/code-review/SKILL.md`, so the source's "the verdict says so" does not reach the agent that writes the hand-back. Rule 12 and rule 19 are the only statements of an open part or a sample label in the policy text (executed: the `git grep` on this finding's `evidence:` line; the other hits are on other subjects). Round 1's finding 3 named exactly this class, "says nothing of a class no list can close", and round 2 confirmed its close at `9ad3b9f9`'s text. Round 3 confirmed round 2's finding 1 on the restored qualifier and did not read what the rewrite dropped. This is the run's scope defect turned around: the rule is narrower than its source, where the five earlier instances were wider.

Restore the clause and let the open part reach both kinds. In rule 12, `skills/agent-contract/SKILL.md:164-170`, replace the body from "the spellings already seen" to the end with:

```markdown
the spellings already seen, and a list that none of the three methods made
is a sample, whatever searches were joined to make it. Where the class
ranges over an unbounded domain of keywords, spellings or constructs, no
method makes the list whole, and the hand-back says so. The hand-back names
the method and what it listed, calls a sample a sample, and says where the
open part of a sample or of such a class stands. The proofer judges the
method as well as the instances: a sample handed back as a whole list is a
finding even where every instance on it was fixed.
```

The text adds no reach past the source. "the hand-back says so" is the source's "the verdict says so", moved to the crafter's report, as `9ad3b9f9` had it. "says where the open part ... stands" is rule 12's own phrase, standing for the source's "the limit goes to the skill's Known limits or a `deferred <home>`".

In the fragment, `changelog.md:3`, replace "and a class over an unbounded domain of keywords, spellings or constructs has no whole list." with:

```markdown
and a class over an unbounded domain of keywords, spellings or constructs has no whole list, so the hand-back says so and where its open part stands.
```

answer: Holds. The paste-ready text was applied as written, rule 12 and the fragment, and nothing else in the rule changed. Each added word was checked against its sources. "no method makes the list whole, and the hand-back says so" is `skills/code-review/SKILL.md:167-169`'s "does not close it; the verdict says so", placed in the hand-back as `9ad3b9f9` had it. "says where the open part of a sample or of such a class stands" carries `9ad3b9f9`'s "names where the open part is recorded" and the source's "the limit goes to the skill's Known limits or a `deferred <home>`", in the word the rule already used. C2 (`frame/design.md:47`) and the lesson row (`frame/design.md:98`) say nothing about an unbounded domain, so neither is crossed. A list one of the three methods made over an unbounded domain now owes the hand-back's statement that it is open, and "the open part" names both kinds, so it has one reading. The contract-reading modules, line wrap among them, pass.

## Confirmations

confirms: round-3#1
The close holds. Rule 12 now reads "a list that none of the three methods made is a sample, whatever searches were joined to make it" (`skills/agent-contract/SKILL.md:164-165`, read). Rule 19 reads "Where none of rule 12's three methods listed them, the list is a sample" (`skills/agent-contract/SKILL.md:232-233`, read). Both match round 3's fenced blocks word for word. Read against the sources word by word, the definition adds no reach. The lesson row (`frame/design.md:98`) names the three methods and rules out "the instances you can see or a grep of one wording". C2 (`frame/design.md:47`) asks for "a method that makes the list whole". So a list none of the methods made is not whole, and the rule's sentence says only that, under its own name for such a list. "whatever searches were joined to make it" restates that complement for the case round 3 named and says nothing about a list a method made. A command that lists each thing holding a property is one of the methods, so the clause does not reach it. "alone" and "nothing but that search" stand nowhere in the policy text, and "sample" stands there only in rules 12 and 19 and in the sealer's sample of claims (executed: `git grep -n -i -E 'alone is a sample|nothing but that|made only from|a sample'`). The fragment's two sentences match round 3's replacements (`changelog.md:3`, read). Under the new definition, the list `agents/crafter.md:177-179` and `skills/code-review/orchestration.md:74-77` make by the word search and the `check:` target is a sample under rule 12, which each cites, so the step has one reading and owes no edit (read). #1167's branch, as it stands now, leaves both sentences unchanged. Its one hunk next to them adds a sentence on folding a statement that stands in the frame, and it states no label for the list (executed: `git diff origin/release/v0.26.0 chore/1167-judgment-where-meaning-is-the-question -- agents/crafter.md skills/code-review/orchestration.md skills/agent-contract/SKILL.md`). So the merge with #1167 owes nothing for this finding. `777ca4d8` changed no word (executed: the word diff in `## Probes`). Rule 19's rewritten line at `skills/agent-contract/SKILL.md:233` is 82 columns, wider than the paragraph around it and inside the 88 columns `tests/behaviour/test_docs_line_wrap.py` holds (read), so it is no finding.

confirms: none
The four modules this round ran pass at `837ac652` in the branch worktree: 101 passed, exit 0 (executed, `## Probes`). A narrow run, not the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad suite, the repository-wide lint and `seal gate` at HEAD; the fix pass's 4-module set (78 passed) and 95-module set (4,458 passed) were not re-run (`unverified`) | the branch at `837ac652` | the orchestrator, by `seal gate --base release/v0.26.0 --record seal/threads/1793419351-project-rules-live-in-the-repository` |
| The fix pass's hand-back, which the spawn prompt says names its word search for other statements as a sample. This round did not have it, and judged the close from the record's `answer:` line, the diff and its own listings | the fix pass's hand-back | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_the_agent_contract_holds_the_universal_rules.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_docs_line_wrap.py tests/text/test_the_rules_have_one_owner.py -q` | 101 passed, exit 0, in the branch worktree at `837ac652`; a narrow run, not the broad gate |
| `git diff --word-diff 9194dd0e 777ca4d8` filtered for changed-word markers | no marker, so the rewrap changed no word |
| `git show c5eec50b^:skills/agent-contract/SKILL.md` | rule 12 at `9ad3b9f9` carries "no method makes the list whole: the hand-back says so, and names where the open part is recorded" |
| `git grep -n -i -E 'open part\|says so' -- skills agents docs templates CONTRIBUTING.md` | rule 12 at `:168` and rule 19 at `:233` state the hand-back's duty; `skills/code-review/SKILL.md:168` states the verdict's; the other hits are on other subjects |
| `git grep -n -i -E 'alone is a sample\|nothing but that\|made only from\|a sample'` over `skills`, `agents`, `docs`, `templates`, `hooks`, `CONTRIBUTING.md` and the fragment | rules 12 and 19, the fragment and the sealer's sample of claims; no old wording stands |
| `git diff origin/release/v0.26.0 chore/1167-judgment-where-meaning-is-the-question -- agents/crafter.md skills/code-review/orchestration.md skills/agent-contract/SKILL.md` | #1167 leaves `agents/crafter.md:177-179` and `skills/code-review/orchestration.md:74-77` unchanged and does not touch the contract; its hunk after the latter adds a sentence on folding a frame statement |
