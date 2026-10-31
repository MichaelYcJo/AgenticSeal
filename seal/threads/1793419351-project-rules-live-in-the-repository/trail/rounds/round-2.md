# Review round 2: 1793419351-project-rules-live-in-the-repository

target: 1c9f65bc, fixes 20d93152..1c9f65bc

Round 2 is a verifying round over round 1's fix pass: `a4280a14` (findings 1 and 4), `e971a99c` (2), `9ad3b9f9` (3), `47cc66d2` (5, 6 and 7), `3ad40200` (the fragment) and `1c9f65bc` (the answers). Facts carried from round 1 and its phase records, not re-established: where each changed paragraph stands, that `tests/text/test_the_rules_have_one_owner.py:337-358` is C4's pin, and that no case pins the wording of rule 12, of C3's paragraph or of C1's section. Round 1's `## Not judged` rows on `gh pr edit` and `gh pr checks <N> --watch` stand as written, because the fix diff did not touch those sentences. Every verdict below was reached this round, and each rewritten scope was read against the text it rests on.

The fix pass's account was read as claims. It claimed a six-module narrow run with 130 passed; this round ran the same six modules and got 130 passed, exit 0. It claimed no test was owed because the changes are prose and C4's pin is unchanged; read, it holds: the pinned clause "`MERGED` or `CLOSED` stops the push" stands at `skills/code-review/orchestration.md:190-191`. No test was added, so no new test is read against its group.

## Findings

### 1. Rule 12 calls every class of spellings endless, so the statements of a fact in the tree can be handed back as an open sample

severity: should
location: `skills/agent-contract/SKILL.md:164-167`, `seal/threads/1793419351-project-rules-live-in-the-repository/changelog.md:3`
evidence: read `skills/agent-contract/SKILL.md:159-169`, `skills/code-review/SKILL.md:167-169`, `seal/threads/1793419351-project-rules-live-in-the-repository/frame/design.md:47`, `seal/threads/1793419351-project-rules-live-in-the-repository/changelog.md:3`
verdict: open
regression: round-1#3

The unit is the sentence `9ad3b9f9` added to rule 12: "Where the class has no end, as spellings, keywords and constructs have none, no method makes the list whole". The frame's C2 (`frame/design.md:47`, phase 2's row of `frame/plan.md`) asks for a class enumerated "by a method that makes the list whole", the fix added a way out for a class with no end, and the defect came from round 1's own paste-ready text, which the fix pass applied as written.

The sentence rests on `skills/code-review/SKILL.md:167-169`: "An enumeration over an unbounded domain, of keywords, spellings or constructs, narrows a finding and does not close it". That sentence qualifies the domain. It is about a check whose inputs nobody bounds. Rule 12's sentence drops the qualifier and says spellings, keywords and constructs have no end, whatever they are drawn from.

Most classes a fix pass enumerates are drawn from the tree. Round 1's finding 4 named one: every other sentence stating an old fact. The tree has an end, and the sentence before, in the same rule, names the method that lists such a class whole: "take the artefact apart into every one of its parts". So for the commonest class, rule 12 now says both that a method makes the list whole and that no method does. A crafter reading the second can hand back a keyword search as an open class with its open part recorded, and the proofer has the rule's own example against calling the list short. This is the scope defect this run has met before: a rule written wider than the text it was read from. The fragment repeats it: "Where the class has no end, such as spellings".

Rewrite the rule's body in place. The words stay fresh against `skills/code-review/SKILL.md`, which `tests/text/test_no_passage_is_pasted_into_a_second_file.py` reads:

```markdown
Do not fix the coordinate. A finding names an instance; the fix is owed to
every instance the same cause produces. List them by a method that makes the
list whole: build it from what produces the defect, take the artefact apart
into every one of its parts, or run a command that lists each thing holding
the property. The instances in view, or a search for one wording, find only
the spellings already seen, and a list made that way is a sample. A class
drawn from the tree has an end, because the tree has one, and taking the
tree apart lists it whole. Where the class reaches past the tree, as the
spellings, keywords and constructs a check may be handed do, no method makes
the list whole: the hand-back says so, and names where the open part is
recorded. The hand-back names the method and what it listed, and the
proofer judges the method as well as the instances: a sample handed back as
a whole list is a finding even where every instance on it was fixed.
```

In the fragment, replace "Where the class has no end, such as spellings," with:

```markdown
Where the class reaches past the tree, such as the spellings a check may be handed,
```

answer:

### 2. Rule 12 now calls rule 19's search a sample, so a fix pass that follows rule 19 hands back a finding

severity: should
location: `skills/agent-contract/SKILL.md:228-230`, `agents/crafter.md:176-179`, `skills/code-review/orchestration.md:71-78`
evidence: read `skills/agent-contract/SKILL.md:159-169`, `skills/agent-contract/SKILL.md:228-232`, `agents/crafter.md:176-179`, `skills/code-review/orchestration.md:71-78`, `seal/threads/1793419351-project-rules-live-in-the-repository/trail/rounds/round-1.md:98`
verdict: open
regression: round-1#3

The unit is rule 12's clause "and a list made that way is a sample", with "a sample handed back as a whole list is a finding", both added by `9ad3b9f9`. The frame's C2 (`frame/design.md:47`) has the proofer judge the method a list was made by, the fix defined which methods make a sample, and the defect came from round 1's paste-ready text, which was never read against rule 19 or against the fix pass's own instructions.

Rule 19, in the same file, tells every agent to find "every other sentence, case and citation stating it, found with `git grep` on its words". `agents/crafter.md:176-179` tells the fix pass to find "every other place stating each rule your range reworded or removed, by `git grep` and its `check:` target", and cites rule 12 for it. `skills/code-review/orchestration.md:71-78` says the same: "by its words and by the `check:` target". Each prescribes a search for the rule's own wording, which is the method rule 12 now calls a sample. Each hands the result back as every other place, which is a whole list, and rule 12 now calls that a finding.

The record this round answers shows it. Finding 4's answer says `git grep -n 'mergeable'` "returns C4's paragraph, its pin, this row and the test-duration index, and nothing else states the old read" (`round-1.md:98`). That is a one-word search handed back as the whole class. It did what rule 19 asks, and by rule 12's words it is a finding. The close of finding 4 holds on this round's own listing (its confirmation below), so the conflict is in the rules and not in that answer.

Before `9ad3b9f9`, rule 12 said "a list made by sampling" and never said what sampling was, so the two rules could still be read together. The definition is what makes them disagree. Rule 19 is in this work item's file. The other two places stand in text `frame/design.md` *Scope*, **Out**, leaves to #1167: `agents/crafter.md` step 8, and the paragraph opening **The fix pass then finds what the fixes left standing**. The fix pass therefore either edits them under the orchestrator's integration with #1167, or answers with `deferred` naming #1167's work item as their home.

Rule 19's body:

```markdown
A change rewrites the text it amends where that text stands, and in the
same commit removes or corrects what stood on the old fact: every other
sentence, case and citation stating it, listed as rule 12 lists a class. A
`git grep` on its words begins that list and does not finish it. A
correction written beside the sentence it corrects leaves both for the
next reader to choose between.
```

In `agents/crafter.md:178`, replace "by `git grep` and its `check:` target" with "by a method rule 12 accepts, a `git grep` on its words and its `check:` target among the searches". In `skills/code-review/orchestration.md:75-76`, replace "by its words and by the `check:` target that holds it" with "by a method rule 12 accepts, its words and the `check:` target that holds it among the searches".

answer:

## Confirmations

confirms: round-1#1
`skills/code-review/orchestration.md:188-197` now sends the repair after `MERGED` to a new branch from the base, and after `CLOSED` pushes nothing and names the pending repair in the report (read). The scope was read against its source. The frame's scenario names `MERGED` alone (`frame/design.md:184`), and the `CLOSED` route is round 1's finding 1. The sentence claims nothing past that finding: under `CLOSED` the orchestrator stops, and the person decides. Its ground, "the base does not hold the work", is what `CLOSED` means in this repository's flow, where a work item reaches the base by a squash merge, which GitHub reads as `MERGED` (`docs/release-checklist.md:13-16`). No step of the tree lands a branch any other way (executed: `git grep -n -E 'CLOSED|closes? (the|its) pull request|pull request (is|was) closed|closed pull request'` over `skills`, `agents`, `docs`, `hooks`, `templates` and `CONTRIBUTING.md`, which returns this paragraph, the acts row and no procedure). Where a branch did land outside GitHub and its pull request was then closed, the ordered act, pushing nothing and reporting, is still right. The pinned clause stands and its pin passes in the narrow run.

confirms: round-1#2
`skills/verify/orchestration.md:102-109` says the gate runs its whole row once more at the base and reads each failing file against that run (read). That is `templates/setup/config.md:365`, rule 3: "the row runs once more, unchanged, at the base", and "The cost is one more run of the whole row". The one case where the gate does not run the base, no pytest record at `HEAD`, stands in the same section's **New?** bullet (`:115-123`), so the paragraph is not wider than rule 3. The other statements of the base run agree: `skills/verify/scripts/broad_gate.py:58-66`, `agents/crafter.md:154` and `skills/code-review/orchestration.md:299-300` (executed: `git grep -n -i 'files that failed\|only for the fail\|at the base'` and `git grep -n -i 'comparison is reactive\|is reactive and'`, each hit read).

confirms: round-1#3
What finding 3 named is closed. Rule 12 now says what a sample is, and says what the hand-back does with a class no list can close (`skills/agent-contract/SKILL.md:159-169`, read). The two sentences that close it each carry a finding of this round, findings 1 and 2. The rewrite shares no run of words with `skills/code-review/SKILL.md`, which the narrow run's `tests/text/test_no_passage_is_pasted_into_a_second_file.py` confirms. The places citing rule 12 are `agents/crafter.md:179` and `skills/code-review/orchestration.md:74` (executed: `git grep -n -i 'rule 12\|enumerat'` over `skills`, `agents`, `docs`, `templates` and `CONTRIBUTING.md`, every hit read; the rest are code identifiers and other subjects), and finding 2 covers both.

confirms: round-1#4
`skills/implement/acts.md:75` names the reads at the opening and before and after each push, and the stop on `MERGED` or `CLOSED`, which matches `skills/code-review/orchestration.md:188-197` (read). Finding 4's evidence was re-run: `git grep -n -i 'json mergeable\|mergeable' -- . ':!seal/threads'` returns C4's paragraph, the acts row, the pin and `.test_durations`. The class was also listed by construction rather than by one word: the files citing the section by its heading (executed: `git grep -n -i 'pull request opens once the sealer seals'`) are `CONTRIBUTING.md:36`, `skills/verify/orchestration.md:34`, the acts row and four test modules. The two prose citations say who owns the order and state no read.

confirms: round-1#5
The fix pass did not apply round 1's split by when a decision was made, and its grounds hold. Under that split, the owner's ruling on a release's version, made while another work item is built, counts as made in the work item in progress and goes to that work item's records. That is the two-place problem finding 5 named, in another form. The rows now split by what a decision is about (`skills/implement/orchestration.md:362-364`, read). Row 1 matches the core's sentence, which is about the judgments a work item makes. Row 3 matches the frame's **In an issue** paragraph, which puts #1199's owner decision in an issue (`frame/design.md:149`). A decision about a file a running work item changes has that file as its home, so it fits row 1 and not row 3. A decision whose home no running item changes fits row 3 alone. The fragment says the same (`changelog.md:3`). Only the acts row cites the section by its heading (executed: `git grep -n -i 'where a decision or a lesson is written'`), and its grounds state no split.

confirms: round-1#6
`skills/implement/orchestration.md:354-358` reads "never into a session's local memory" (read). The section's last paragraph (`:374-377`) keeps in memory only one machine's facts and how the person wants to be worked with. Neither is a decision or a lesson of a run, so the two give one reading. Outside the records, `local memory` and `session memory` stand only in `skills/implement/acts.md:69`, which describes what no check sees (executed: `git grep -n -i 'local memory\|session memory'`).

confirms: round-1#7
Row 3 (`skills/implement/orchestration.md:364`) sends a lesson about a file the plugin ships, learnt in another repository, to the person through the orchestrator's report. It names the tracker under `repository` in `.claude-plugin/plugin.json`, and the orchestrator edits no installed copy (read). That field exists in the tree (`.claude-plugin/plugin.json:10`, read) and in the installed plugin's copy of the same file (read). The home was judged against the two alternatives. An issue in the user's own tracker is read by nobody who can change the plugin, which was finding 7's point. Filing in the plugin's tracker from another repository is an act on a third party's tracker under the person's account. The report is the channel the orchestrator already has, and a report is not a question, so the core's rule on asking a person is not engaged. The limit the answer states, that nothing records whether the person carried the lesson over, falls under the acts row's grounds, "Nothing reads where a lesson went" (`skills/implement/acts.md:69`). The scope was read against its source. The clause applies only where the home is a file the plugin ships and the run is in another repository. A run in this repository falls under the row's first sentence, and its tracker is the plugin's.

confirms: none
The fix pass's narrow run holds: the same six modules gave 130 passed, exit 0, in the branch worktree at `1c9f65bc` (executed, `## Probes`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad suite, the repository-wide lint and `seal gate` at HEAD; the crafter's 110-module run (4,880 passed) was not re-run (`unverified`) | the branch at `1c9f65bc` | the orchestrator, by `seal gate --base release/v0.26.0 --record seal/threads/1793419351-project-rules-live-in-the-repository` |
| The fix pass's hand-back, which the spawn prompt says names its rule 12 search as a sample. This round did not have it, and judged the method from the record's `answer:` lines and from its own listings | the fix pass's hand-back | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_every_orchestrator_act_names_its_delivery.py tests/text/test_the_agent_contract_holds_the_universal_rules.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py -q` | 130 passed, exit 0, in the branch worktree at `1c9f65bc`; a narrow run, not the broad gate |
| `git grep -n -E 'CLOSED\|closes? (the\|its) pull request\|pull request (is\|was) closed\|closed pull request'` over `skills`, `agents`, `docs`, `hooks`, `templates` and `CONTRIBUTING.md` | C4's paragraph and the acts row; the rest are code comments and identifiers on other subjects |
| `git grep -n -i 'pull request opens once the sealer seals'`, and the same for `where a decision or a lesson is written` and `comparison is reactive` | the citing files each confirmation names, and no other statement of the changed facts |
| `git grep -n -i 'rule 12\|enumerat'`, `git grep -n -i 'sampl'` and `git grep -n -i -E 'git grep. on its words\|found with .git grep\|by its words'` over `skills`, `agents`, `docs`, `templates` and `CONTRIBUTING.md` | rule 12, rule 19 at `skills/agent-contract/SKILL.md:230`, `agents/crafter.md:178-179` and `skills/code-review/orchestration.md:74-75` (finding 2); the other hits are code identifiers and the sealer's sample of claims |
