# Review round 5: 1793419351-project-rules-live-in-the-repository

target: 4cfded90, fixes 43249fdd..4cfded90

Round 5 is a verifying round over round 4's fix pass: `4d63917c` (finding 1, rule 12 and the fragment) and `4cfded90` (the answer). The review stayed inside that diff: rule 12 of `skills/agent-contract/SKILL.md`, the work item's `changelog.md` and the two closing lines of `round-4.md`. Facts carried from rounds 1 to 4, not re-established: that no case pins the wording of rule 12 or rule 19, that rule 12 and rule 19 are the only statements of a sample label or an open part in the policy text, and that `agents/crafter.md` and `skills/code-review/orchestration.md` are #1167's files in this run (`frame/plan.md:33`). The second fact was re-run anyway as a cheap check, and it holds. Every verdict below was reached this round. The two changed phrases were read word by word against the four sources the spawn prompt named: `skills/code-review/SKILL.md:167-169`, rule 12 as `9ad3b9f9` wrote it, C2 (`frame/design.md:47`) and the lesson row (`frame/design.md:98`).

The fix pass's account was read as claims. It claimed the paste-ready text of round 4's finding 1 was applied as written and nothing else in the rule changed. A word diff of rule 12 from `43249fdd` to `4cfded90` shows three changes and no other: "whole." became "whole, and the hand-back says so.", "its" became "the", and "of a sample or of such a class" was added (executed, `## Probes`). The rule body matches round 4's fenced block line for line, and the fragment's sentence matches its second block (read). It claimed the contract-reading modules pass. This round ran four of them, 101 passed. It claimed a 4-module set with 78 passed and a 95-module set with 4,458 passed. This round did not re-run either set. `4cfded90` changes only the `verdict:` and `answer:` lines of round 4's finding 1, the two lines a fix pass writes. No test was added, so no new test is read against its group.

## Findings

No finding this round.

## Confirmations

confirms: round-4#1
The close holds. Rule 12 now reads "no method makes the list whole, and the hand-back says so" and "says where the open part of a sample or of such a class stands" (`skills/agent-contract/SKILL.md:166-169`, read). Each phrase was read against its sources.

"and the hand-back says so": `skills/code-review/SKILL.md:167-168` says an enumeration over an unbounded domain "does not close it; the verdict says so". `9ad3b9f9` put the same duty in the hand-back: "no method makes the list whole: the hand-back says so". The new clause is that sentence with a comma in place of the colon. "so" has one referent, the clause before it: the list is not whole. The clause sits inside "Where the class ranges over an unbounded domain", so it binds only that class. Round 4's case now has a duty: a list one of the three methods made over an unbounded domain is not a sample, and the hand-back still says it is not whole.

"says where the open part of a sample or of such a class stands": `9ad3b9f9` had "names where the open part is recorded", and the source has "the limit goes to the skill's Known limits or a `deferred <home>`". "the open part" now has two named owners, a sample and a class over an unbounded domain. "such a class" can only point back to the class of the sentence before, so the phrase has one reading. A list one of the methods made over a bounded domain has no open part, and the phrase asks nothing of it. That matches C2's "a method that makes the list whole".

The word "stands" was weighed against "is recorded", since "where it stands" can mean a status as well as a place. In this file, "where" with "stands" names a place: rule 19's "where that text stands" (`skills/agent-contract/SKILL.md:230`, read). The duty to put the limit in a home is the closing round's under `skills/code-review/SKILL.md:167-169`, which the proofer reads before it closes a finding. Rule 12's part is to make the open part visible to that proofer, and both readings do that. So the word adds no gap that ships. It was the rule's word before this fix pass: `c5eec50b` wrote "says where its open part stands", and rounds 3 and 4 read it.

Neither phrase reaches past the frame. C2 (`frame/design.md:47`) asks for a method that makes the list whole, a hand-back that names it and a proofer that judges it. The lesson row (`frame/design.md:98`) names the three methods. Neither speaks of an unbounded domain or an open part, so the restored duty comes from the code-review source alone, as round 4's answer says (read). The fragment now reads "has no whole list, so the hand-back says so and where its open part stands" (`seal/threads/1793419351-project-rules-live-in-the-repository/changelog.md:3`, read). "its" is the class's, as in the rule. No other statement of the hand-back's duty for an open list stands in the policy text. A `git grep` on "open part", "says so", "whole list" and "unbounded domain" returns rules 12 and 19, `skills/code-review/SKILL.md:167-168`, and lines on other subjects (executed, `## Probes`). That search is a word search, so its list is a sample under rule 12. Its open part is any statement of the duty in other words, and the carried fact from round 4 covers it. Rule 19's "the hand-back says so as rule 12 asks" (`skills/agent-contract/SKILL.md:233-234`, read) still has one reading: it is rule 12's "calls a sample a sample". No line of rule 12 runs past 88 columns, the width `tests/behaviour/test_docs_line_wrap.py` holds (executed, `## Probes`).

confirms: none
The four modules this round ran pass at `4cfded90` in the branch worktree: 101 passed, exit 0 (executed, `## Probes`). This was a narrow run, not the broad gate.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad suite, the repository-wide lint and `seal gate` at HEAD. The fix pass's 4-module set (78 passed) and 95-module set (4,458 passed) were not re-run (`unverified`) | the branch at `4cfded90` | the orchestrator, by `seal gate --base release/v0.26.0 --record seal/threads/1793419351-project-rules-live-in-the-repository` |
| The fix pass's hand-back, which the spawn prompt says hands back its search for other statements as a sample. This round did not have the hand-back. It judged the close from the record's `answer:` line, the diff and its own search | the fix pass's hand-back | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `git diff --word-diff 43249fdd HEAD -- skills/agent-contract/SKILL.md` filtered for changed-word markers | three changes, all in rule 12: "whole." became "whole, and the hand-back says so.", "its" became "the", and "of a sample or of such a class" was added |
| `git show --stat 4d63917c`, `git show --stat 4cfded90` | `4d63917c` touches `skills/agent-contract/SKILL.md` and `changelog.md`; `4cfded90` touches only `round-4.md` |
| `git log --oneline -S 'open part is recorded' -- skills/agent-contract/SKILL.md` and `git show --stat c5eec50b` | "names where the open part is recorded" left with `c5eec50b`, round 2's fix pass, whose answer quotes the new "says where its open part stands" |
| `git grep -n -i -E 'open part\|says so\|whole list\|unbounded domain' -- skills agents docs templates hooks CONTRIBUTING.md` | rule 12 at `:166-169`, rule 19 at `:234` and `skills/code-review/SKILL.md:167-168` state a duty for an open list; every other hit is on another subject |
| `awk 'length>88' skills/agent-contract/SKILL.md` | lines 80 and 104 only, outside rule 12 and outside the fix diff |
| `bin/test tests/text/test_the_agent_contract_holds_the_universal_rules.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_docs_line_wrap.py tests/text/test_the_rules_have_one_owner.py -q` | 101 passed, exit 0, in the branch worktree at `4cfded90`; a narrow run, not the broad gate |
