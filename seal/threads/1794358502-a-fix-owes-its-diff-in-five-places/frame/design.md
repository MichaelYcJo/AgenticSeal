# Design: 1794358502-a-fix-owes-its-diff-in-five-places

## Grounding

The tree as read at `ebe6ceed3`.

Each row is labelled `read` where the framer opened the text and `executed` where a command printed the fact. The branch's one commit after `0b55462b2` adds `routing.md` alone, so every coordinate below also holds at `0b55462b2`. The issue took its coordinates at `ba4d85629`, before #1471 and #1473 merged, and each one is re-taken here.

| Policy clause | What it fixes for this work |
|---|---|
| G1 `skills/core/SKILL.md` *A document is cut by who opens it and at which step* (read) | A party pays for every byte it preloads, on every spawn. A rule that one party acts on stands in the file that party opens at the step where it acts. |
| G2 `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | A fact has one source and every other place links to it. A change rewrites the text it amends in place and removes, in the same commit, each citation and pin that stood on the old fact. |
| G3 `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each* (read) | "A rule that would need a per-role exception is not universal": what is true of every agent is the contract's, and what is one agent's own is in that agent's definition. The closed set names the crafter's files and the cell it writes, so its definition is the crafter's. |
| G4 Contract rule 12, `skills/agent-contract/SKILL.md:141-164` (read; executed: `awk '/^## 12 /{f=1} /^## 13 /{f=0} f' skills/agent-contract/SKILL.md \| wc -c` printed 1654) | The rule is eleven sentences, cited below as R1 to R11 in the order they stand. R1 to R4 (`:143-149`) state the class, the three methods and "a list that none of the three methods made is a sample". R5 to R7 (`:149-153`) define the closed set. R8 (`:153-158`) says where a sample stays one. R9 (`:158-160`) says what the hand-back names. R10 (`:160-161`) says nothing left over is the proofer's share. R11 (`:161-164`) addresses the proofer. The rule carries no `check:` line. |
| G5 Contract rule 19, `skills/agent-contract/SKILL.md:207-215` (read; executed: the same `awk` between `## 19 ` and `## 21 ` printed 524) | Its third sentence (`:212-214`) restates R4 and R9: "Where none of rule 12's three methods listed them, the list is a sample, and the hand-back says so as rule 12 asks." The rule states nothing of the closed set (executed: `git grep -n -e 'closed set' -e 'states the present'` prints no line of it). |
| G6 `agents/crafter.md:178-200`, the rule *Before you hand back, your range and the work item's records are read whole against HEAD* (read; executed: `awk` from its lead to the next rule's lead printed 1535) | The rule already holds the whole definition: the range read hunk by hunk, the files of the work item's directory that state the present, named one by one (`:182-183`), what is fixed and what is named for the orchestrator, and the tree-wide search as a sample. It points at the contract for the reason the set is closed: "That set is closed (rule 12)" (`:193`). Step 10 (`:65-74`) and `skills/implement/fix-pass.md:47-49` cite the rule by its lead. |
| G7 `agents/proofer.md` step 3 (`:30-35`) and the rule *Every round reads the work item's records that state the present, whole, against its target* (`:122-139`) (read; executed: `awk` over the rule printed 1248) | The proofer's definition names the records a round reads twice, once in step 3 and once in the rule (`:123-126`). Its order of work opens `skills/code-review/SKILL.md` and neither `agents/crafter.md` nor `skills/implement/SKILL.md`, so what the proofer does with a fix's account has to stand in its own file once R11 leaves the contract. |
| G8 Every other statement at HEAD (executed: `git grep -n -i -E "closed set\|states the present\|is a sample\|a sample\|dated to the commit" -- skills agents docs templates tests evals lib bin CONTRIBUTING.md README.md`, and `git grep -n -E "rule 12\|rule 19" -- . ':!seal'`; each hit read) | Two sentences cite rule 12 for a reading of whole files, which only R5 states: `skills/implement/orchestration.md:91-94` and `skills/implement/fold-and-reframe.md:22-24`, each ending "as contract rule 12 asks of the party that fixes". Each states its own set in its own words. `skills/code-review/orchestration.md:68-74` cites rule 12 for the class and for what a hand-back carries, and `skills/implement/orchestration.md:367` cites it for the open class; R1 to R4 and R9 keep both true. `agents/framer.md` holds no statement: #1473 moved the one the issue names to `skills/implement/fold-and-reframe.md:27-28`, where it says the framer keeps a dated section's date. No file under `docs/` holds any of these phrases. |
| G9 `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, the paragraph opening **Nothing else follows them** (read) | It is the source of R6: a round record carries the SHA it reviewed and `plan.md`'s Status cell the commit that closed a phase, so neither asserts a present state. The crafter opens this file at step 1 and its rule cites the section. |
| G10 Sizes at HEAD (executed: `wc -c`) | `skills/agent-contract/SKILL.md` 13,186 B, `agents/crafter.md` 11,299 B, `agents/proofer.md` 10,746 B, `skills/core/SKILL.md` 9,322 B. A spawn preloads the core, the contract and its own definition: 33,807 B for a crafter, 33,254 B for a proofer. |
| G11 The replacement texts of *Data & interfaces*, measured (executed: a probe script under the session's scratch directory read the three files, put T1 and T2 in place of the text they replace, and printed the sizes, and the directory is removed; the final wording of T1 and T2 was counted again by a read-only script on standard input, which printed `13186 -822 12364`) | The contract holds 12,364 B with T1 and T2, 822 B less. T3 adds about 112 B to `agents/crafter.md`, and T4 with T5 about 218 B to `agents/proofer.md`. A reflow changes no count, because it trades a space for a newline. The margin over 820 B is 2 B, so a word added to T1 or T2 at the build puts S1 out of reach. |
| G12 The pins (read) | `tests/text/test_a_moved_rule_leaves_its_definition.py#test_the_crafter_reads_its_range_and_the_records_whole_before_it_hands_back` (`:464-504`) pins "That set is closed (rule 12), so none of it is handed on as a sample." at `:491`. `tests/text/test_the_rules_have_one_owner.py` pins the two citations of G8 that change, at `:589-594` and `:716-718`. The same module's `test_no_definition_carries_a_sections_own_sentences` fails where a definition shares a run of `WINDOW` words with a contract section, so it turns red on a paste of T3 or T5 back into the contract, and the sentences this work moves leave the contract. `test_the_proofer_checks_its_record_in_the_branch_worktree` (`:349`) is the module's case on `agents/proofer.md`. No case reads the body of rule 12 or of rule 19. |
| G13 `docs/running/what-a-script-gates.md` *The checks*, the row for the cases that read prose (read) | "a case pins a fact a reader acts on; one that pins wording goes". The pins of G12 change with their sentences. The clauses this work adds pin two facts a reader acts on at their new homes, T3b for the crafter and T5 for the proofer, and none pins the contract's wording. |
| G14 The history of R5 to R11 (executed: `git log --oneline -S"proofer's share" -- skills/agent-contract/SKILL.md` and the same for "The reach of your" print `5005355d8` alone, the commit of #1327; read: `git show v0.31.0:seal/threads/1793721630-the-party-that-fixes-checks-its-fix-first/frame/design.md` and its `frame/plan.md`) | #1318's frame counted 35 of the 37 `regression:` findings of 0.27.0 to 0.30.1 inside the fixing party's own diff or its work item's records (its G9). It closed the exit in the old rule 12 that let the rest of any list be handed on as a sample (its G4). It left `agents/proofer.md` unedited because "Rule 12 already says the proofer judges the method" (its G10). It rejected "the crafter's rule alone, with rule 12 left as it is" because the exit would stay. This work keeps the exit closed in T1 and gives the proofer its sentence in T5. |
| G15 The latest release's *Process changes* (executed: `gh release view --json tagName,body`, tag `v0.37.2`) | #1477 rewrote, one release ago, the sentences on a dated frame section in `agents/crafter.md:183-188` and `agents/proofer.md:126-130`, after the proofer was told the target does not contradict a stale *Grounding* conclusion. Those sentences are out of scope here. |
| G16 The policy in force (read: `docs/README.md`; executed: the `## Rule changes` block of every `frame/design.md` under `seal/threads/` printed, and the first `git grep` of G8 over `docs`) | No document of the policy root states the closed set, what a hand-back names, or who verifies it, and no unsettled design changes a section this work reads. The work's subject is the contract, two agent definitions and two skill files. |
| G17 `seal/follow-up.md` (read) | Both tables are empty, so no row waits on this work. |
| G18 The issue and its comments (executed: `gh issue view 1472 --json title,body,comments,milestone,labels`, 2026-11-11) | The issue has no comment. Its *Done when* asks that the closed set's file list appear once across all preloaded files and that the contract be at least 0.8 KB smaller. 0.8 KB is 800 B, or 820 B where a KB is 1,024 B, and S1 takes the larger. |
| G19 `routing.md` (read) | It stands, declares a framer and a crafter under `agentic`, and names the branch. |
| G20 The release's other open items (executed: `gh issue view` for #1474, #1503, #1480 and #1475; `git branch -r` lists no branch naming any of them) | `frame/plan.md` *Overlap with the release* reads each against this work. |
| G21 The version (executed: `grep '"version"' .claude-plugin/plugin.json` printed `0.37.3`) | The release's version move landed with #1471, and this work takes none. |

## Scope

In:

1. **Contract rule 12, rewritten in place.** R1 to R4 stay word for word. R5 to R11 give way to T1. The rule then says: count the class by a method that makes the list whole, a list stays a sample only where no method makes it whole, and the hand-back names the method, calls a sample a sample, says where the part it did not reach stands, and names what was not finished as not done.
2. **Contract rule 19, its third sentence, rewritten in place** as T2, a citation of rule 12.
3. **`agents/crafter.md` *Before you hand back, your range and the work item's records are read whole against HEAD*.** The sentence "That set is closed (rule 12), so none of it is handed on as a sample." becomes T3a, which gives the reason the contract gave: reading the set whole is rule 12's second method. T3b, the fact of R10, follows the rule's last sentence. The rule's other sentences, its lead and its `check:` line stay as they are.
4. **`agents/proofer.md` *Every round reads the work item's records that state the present, whole, against its target*.** The sentence that names the records a second time (`:123-126`) becomes T4, which cites step 3. T5, the proofer's half of R11, follows the rule's last sentence.
5. **`skills/implement/orchestration.md:91-94`.** "as contract rule 12 asks of the party that fixes" becomes "the second method of contract rule 12". The sentence keeps its own statement of what the orchestrator reads.
6. **`skills/implement/fold-and-reframe.md:22-24`.** The same phrase becomes the same words.
7. **Tests.** In `tests/text/test_a_moved_rule_leaves_its_definition.py`, the crafter's case takes T3a in place of the clause at `:491` and gains T3b. One clause of T5, "is a finding on the method, even where every instance on the list was fixed", joins the module's case on `agents/proofer.md` or a case beside it where the crafter's read of the group finds that fits better; #1474 rewrites the same definition next, and the clause is what keeps T5 from leaving as a copy. In `tests/text/test_the_rules_have_one_owner.py`, the clauses at `:589-594` and `:716-718` take the words of items 5 and 6. Each changed or added clause is seen red with its sentence deleted, as contract rule 15 asks. No case asserts what rule 12 no longer holds (`frame/plan.md` *Alternatives considered*, row 11).
8. **The work item's `changelog.md`**, with one `### Process changes` row: where the closed set is defined, what rule 12 keeps, and where the proofer's sentence stands.

Decided, and nothing is built for it:

9. Rule 19 cites rule 12 and not `agents/crafter.md` (`frame/plan.md` *Alternatives considered*, row 3). The issue's *Change* says "rule 19 cites it".
10. `agents/framer.md` takes no edit (G8).
11. `skills/code-review/orchestration.md:68-74`, `skills/implement/orchestration.md:367`, `skills/implement/fix-pass.md:47-49` and step 10 of `agents/crafter.md` keep their text (G6, G8).
12. No eval, hook, check script or mark is added (G2).

Out:

- The sentences on a dated frame section in `agents/crafter.md:183-188` and `agents/proofer.md:126-130`. #1477 wrote them one release ago on a catch of its own (G15), each definition's reader preloads one copy, and the issue's *Change* and *Done when* name no change to them.
- The crafter's clause "and by its `check:` target" (`agents/crafter.md:195-196`) and every `check:` line. #1475 deletes the check lines of the preloaded files and weighs that clause against what is left.
- The sentences #1474 names in the same three files: step 10's labels, the scratch, runner and test-group rules, and `agents/proofer.md` *The implementer's account is a claim*.
- The records of other work items under `seal/threads/` that quote rule 12 as it stood. They state the commit they were written at and leave at the settle.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The contract is at least 820 B smaller | Given `skills/agent-contract/SKILL.md` after the work, when its bytes are counted, then it holds 12,366 B or fewer, against 13,186 B at `ebe6ceed3` | `wc -c skills/agent-contract/SKILL.md` |
| S2 The contract no longer defines the closed set or addresses the proofer | Given rules 12 and 19 after the work, when any agent reads them, then rule 12 holds R1 to R4 and T1, rule 19 holds T2, and neither names the work item's files, the closed set or the proofer | `git grep -n -e 'closed set' -e 'states the present' -e "proofer's share" -e 'finding on the method' -- skills/agent-contract/SKILL.md` prints nothing; review reads both rules |
| S3 The exit #1318 closed stays closed | Given rule 12 after the work, when a party holds a list a method could have made whole, then the rule gives it no sentence to hand the rest on as a sample | read: T1's "A list stays a sample only where no method makes it whole"; review |
| S4 The closed set's file list stands once in a crafter's preload | Given the core, the contract and `agents/crafter.md` after the work, when the files of the work item's directory that a fix reads whole are looked for, then `agents/crafter.md:182-183` alone names them, with the reason the set is closed (T3a) and the fact of R10 (T3b) | the crafter's case of *Scope* item 7 passes; `git grep -n 'states the present' -- skills/core skills/agent-contract agents` prints lines of `agents/crafter.md` alone |
| S5 The proofer's definition names the records once and holds its own sentence on a fix's account | Given `agents/proofer.md` after the work, when a round reads the rule of *Scope* item 4, then the rule sends it to step 3 for the files and says that a statement the account missed, or a sample handed back as a whole list, is a finding on the method | the T5 clause of *Scope* item 7 passes; read: step 3 and the rule |
| S6 No citation names rule 12 for a sentence it no longer holds | Given the two skill files of *Scope* items 5 and 6, when their sentences are read beside rule 12, then each names the second method, which R3 states | `git grep -n 'asks of the party that fixes' -- skills agents docs` prints `skills/code-review/orchestration.md:73` alone, whose citation R9 keeps true (G8); the cases of `tests/text/test_the_rules_have_one_owner.py` that pin them pass |
| S7 The cases that read the edited files hold | Given the edits, when the narrow cases that read any text *Scope* items 1 to 6 edit run, then they pass | the crafter's narrow run, with `tests/text/test_a_moved_rule_leaves_its_definition.py`, `tests/text/test_the_rules_have_one_owner.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/text/test_the_agent_contract_holds_the_universal_rules.py`, `tests/text/test_every_agent_reads_the_contract.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and `tests/behaviour/test_docs_line_wrap.py` among them; the broad gate is the orchestrator's |
| S8 Nothing else changes | Given the branch's diff outside `seal/`, when it is listed, then it holds the files *Scope* items 1 to 7 name and no other | `git diff --stat 0b55462b2...HEAD -- ':!seal/'` |

## Data & interfaces

No script, form, field, template, hook or eval changes. The work is the texts below, each written as it will stand, to be wrapped as its file wraps.

**T1, rule 12 from the end of R4.** R4 ends "is a sample, whatever searches were joined to make it." The rule then reads, to its end:

> A list stays a sample only where no method makes it whole: the other statements of a rule across the tree, or a class over an unbounded domain of keywords, spellings or constructs. The hand-back names the method and what it listed, calls a sample a sample, says where the part it did not reach stands, and names what you did not finish as not done.

R9's "each part's method" becomes "the method", because the parts were the closed set and the open class of R5 to R8.

**T2, rule 19.** The second sentence ends "found at least with `git grep` on its words" and continues, in place of the third sentence:

> ; rule 12 calls that a sample.

**T3a, `agents/crafter.md`,** in place of "That set is closed (rule 12), so none of it is handed on as a sample.":

> That set is closed, and reading it whole is rule 12's second method, so none of it is handed on as a sample.

**T3b, `agents/crafter.md`,** after "What you did not finish goes to `gaps.md` `## Not done` with why.":

> Neither that nor the part a sample did not reach is the proofer's share.

**T4, `agents/proofer.md`,** in place of the sentence at `:123-126`:

> A finding round and a verifying round alike open the files step 3 reads whole, at the commit the target names, and read each to its end.

**T5, `agents/proofer.md`,** after "This read makes a round, not the sealer, the first reader of each sentence in them.":

> The implementer's account of what its own reading of its diff and of these records listed is a claim you verify on your own: a statement that reading held and the account missed, or a sample handed back as a whole list, is a finding on the method, even where every instance on the list was fixed.

## Rule changes

- nothing
  why: no document of the policy root states the closed set, what a hand-back names of its lists, or who verifies that account (G16). The work moves sentences between `skills/agent-contract/SKILL.md`, `agents/crafter.md` and `agents/proofer.md` and re-points two citations in `skills/implement/`, all outside `docs/`.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| R5 and R7, the definition of the closed set and "A list of a closed set is never a sample" | `skills/agent-contract/SKILL.md` *12 A defect belongs to a class, so enumerate the class*, `:149-153` | `agents/crafter.md` *Before you hand back, your range and the work item's records are read whole against HEAD*, which already names the set and takes the reason in T3a. The orchestrator's and the framer's sets stand in the sentences of *Scope* items 5 and 6 |
| R6, "A phase record or a round record states the commit it names, and HEAD contradicts neither" | the same rule, `:152-153` | `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* states it (G9), the crafter's rule cites that section, and the crafter's list of files names neither record |
| R8's second clause and R9's "each part's", folded into one sentence | the same rule, `:157-160` | T1 |
| R10, "Neither the part a sample did not reach nor what you did not finish is the proofer's share" | the same rule, `:160-161` | T3b in `agents/crafter.md`. Its catch was a crafter's `gaps.md` row naming the proofer as a sample's answerer (G14) |
| R11, the sentences addressed to the proofer | the same rule, `:161-164` | T5 in `agents/proofer.md` |
| the third sentence of rule 19, a restatement of R4 and R9 | `skills/agent-contract/SKILL.md` *19 A change rewrites the text it amends in place*, `:212-214` | T2, a citation of rule 12 |
| the crafter's pointer at rule 12 for the closed set | `agents/crafter.md:193` | T3a |
| the second list of the records a round reads | `agents/proofer.md:123-126` | `agents/proofer.md` step 3, which T4 cites |
| two citations of rule 12 for the reading of whole files | `skills/implement/orchestration.md:93-94`, `skills/implement/fold-and-reframe.md:23-24` | the words of *Scope* items 5 and 6 |
| the pin's clause for the crafter's pointer, and the pinned citations | `tests/text/test_a_moved_rule_leaves_its_definition.py#test_the_crafter_reads_its_range_and_the_records_whole_before_it_hands_back`, `tests/text/test_the_rules_have_one_owner.py#test_a_decision_after_the_frame_is_folded_into_it`, `tests/text/test_the_rules_have_one_owner.py#test_the_framer_folds_a_decision_it_is_sent` | the same cases, holding the new words |

The work adds no gate, check script, hook, CI step, rule, line grammar, label or mark, so nothing is owed in return. The clauses *Scope* item 7 adds join cases that stand, and each pins a fact at the home this work gives it (G13).

Framed 2026-11-11 by framer, before the build.
