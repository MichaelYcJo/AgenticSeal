# Design: a fix writes a count into a record

Issue: #1613, `fix: a fix pass or a fold writes a count or a universal into a record, and the next fix makes it false`.

## Grounding

The tree as read at `b03b0e290`.

| Policy clause | What it fixes for this work |
|---|---|
| G1. `skills/core/SKILL.md` *The rule a mechanism is kept against*: "A fact has one source, and every other place links to it" (read) | A count of a list, and a claim that every one, none or only one of its members holds something, restates the list without its words. The rule governs every fact, so the new rule reaches every text a change writes, and not records alone |
| G2. `skills/agent-contract/SKILL.md` rule 19, *A change rewrites the text it amends in place* (read, lines 193 to 200) | Rule 19 has a change find what stood on the old fact "at least with `git grep` on its words". A count or a universal holds none of the words of the list it stands on, so that search does not find it and the sentence stays, false. The rule this work adds is the other half of the same fact, what a change writes, so it stands in rule 19 |
| G3. `skills/agent-contract/SKILL.md` rule 5, *Nothing that reaches you in prose is evidence* (read) | Rule 5 keeps an aggregate from serving as a coordinate when a party reads it. It says nothing of what a party writes, and this work leaves it as it stands |
| G4. Where the fix and the fold procedures cite the contract (executed: `git grep -n -E 'rule +(12\|19\|5)([^0-9]\|$)' -- ':!seal/threads'` at `b03b0e290`) | `skills/implement/fold-and-reframe.md:21` and `:24` cite rules 5 and 12, `skills/implement/orchestration.md:100` cites rule 12, and `skills/code-review/orchestration.md:73` and `:76` cite rule 12 for the fix pass. No file of the tree cites rule 19 by number |
| G5. Who receives the contract (executed: `grep -c -- '- agent-contract' agents/*.md` prints 1 for each file `ls agents/` lists: crafter, framer, proofer, sealer, tracer; read: `skills/implement/orchestration.md:31` to `:33`, `skills/code-review/orchestration.md:96` to `:99`) | Every agent preloads the contract through its `skills:` list. The orchestrator opens it once beside the core at step 1 of `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, where the step names only rule 21 for the orchestrator's own commands |
| G6. `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each*: "A rule that would need a per-role exception is not universal" (read) | Every party writes text after round 1: the crafter's fix pass, the framer's fold, the orchestrator's record edits and merges, the proofer's paste-ready fix and round records, the sealer's `guarantee.md`. The rule needs no exception for any of them, so it is the contract's and not one definition's |
| G7. `docs/running/the-agent-set.md`, the paragraph opening **The contract's rule numbers are stable.** (read) | A new rule would take number 22. Extending rule 19 takes no number and leaves the retired list as it is |
| G8. The one party-scoped statement of the rule (executed: `git grep -n -F 'A count of a list is stated once' -- agents skills docs templates` and `git grep -n -E 'beside the list\|stated once, beside' -- agents skills docs templates CONTRIBUTING.md README.md` at `b03b0e290`, each printing `agents/framer.md:224` alone) | `agents/framer.md` *Rules*, the paragraph opening **A count of a list is stated once, beside the list.**, binds the framer alone and the frame files alone. It came in with #1419. Under rule 19 extended it is a restatement of a contract rule in a definition, which `tests/text/test_a_moved_rule_leaves_its_definition.py`'s docstring calls a reviewer's finding |
| G9. The same rule applied in the orchestrator's guidance (executed: `git grep -n -F 'no sentence counts the examples' -- agents skills docs templates` at `b03b0e290`, printing `skills/code-review/orchestration.md:180` alone) | The paragraph opening **Where the signal is one mechanism whose edges each fix pass chased** ends its list-of-shapes guidance with "and no sentence counts the examples or calls one of them the only one", a statement of this rule for one case |
| G10. A wider search for other statements of the class (executed: `git grep -n -i -w -E 'count\|counts\|counted' -- agents 'skills/implement/*.md' 'skills/code-review/*.md' skills/verify/SKILL.md 'skills/settle/*.md' docs/forms docs/running docs/layout templates/records CONTRIBUTING.md`, and the same tree for `universal`, at `b03b0e290`) | Each line it prints other than G8's and G9's is about counting rounds, sessions, failures, mutation scores or a run's proposals, or is the framer's *A row only a person can answer is reproduced in full in the report*, which is about reporting a row rather than counting it. None states that a party may not write a count. The search is a sample (contract rule 12): a statement of this rule in words the search does not hold stands outside it |
| G11. The tree already keeps counts out of code text (executed in G10's search over the whole tree: `skills/verify/scripts/broad_gate.py:184` "There is no count in this comment on purpose", `tests/behaviour/test_this_repository_passes_its_own_checks.py:167` "No count is written down here either"; read: the v0.38.8 release body, which moved the count of the plugin's hooks to one place in each README edition) | The reach of G1 is practised in comments, docstrings and documents, so the rule's reach is every text a change writes. 29 of the issue's 72 fix-made defects were in code (the issue body, nobody's finding here) |
| G12. `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | This work's subject is the code: it edits `skills/`, `agents/` and `tests/`, and no document of the policy root. So the policy's account of the rule goes into `## Rule changes` for the settle. `docs/running/the-agent-set.md` keeps such an account for contract rule 21, the paragraph opening **Contract rule 21 writes out the command forms**, which is the precedent |
| G13. `CONTRIBUTING.md` *What a change to a gate must carry*, the item **What it removes.** (read) | A rule is a mechanism. `## Removes` names what goes in return: the framer's paragraph of G8, and the clause of G9 |
| G14. `tests/text/test_the_rules_have_one_owner.py` `RULES` (read, lines 110 to 338; executed: the highest key is `"29 `) | The table holds an owner and the carriers that cite it, and `test_every_link_names_the_owner` fails a carrier whose text does not name the owner. A row for rule 19 holds the citation at each step Scope items 2 to 5 edit |
| G15. `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, as `tests/text/test_a_moved_rule_leaves_its_definition.py`'s docstring describes it (read) | The contract and each definition are compared by runs of words, so the framer's paragraph has to leave `agents/framer.md` in the commit that writes its rule into the contract |
| G16. The version (executed: `git grep -n -F '0.38.8' -- ':!seal/threads'` at `b03b0e290`, printing `.claude-plugin/plugin.json:4` alone; read: `skills/implement/merge-order.md` *Orchestrator: the order the work items of a release merge in*) | `.claude-plugin/plugin.json` is the one place outside the records that states the version. The move to 0.39.0 is the orchestrator's decision in the spawn prompt, given to the first item to merge |
| G17. `seal/follow-up.md` (read whole) | Neither of its rows waits on this work |
| G18. The issue's comments (executed: `gh issue view 1613 --json body,comments --jq '.comments\|length'` printed 0 on 2026-11-25) | The body as the spawn prompt hands it is the request |
| G19. `routing.md` (read) | `Planning` framer, `Implementation` crafter, `Review` through the review chain, `Automation` yes. The issue's second *Done when* line goes to `seal/follow-up.md` with the owner as answerer |
| G20. The parse of this design's `## Rule changes` (executed: a probe `test_tmp_parse_rule_changes.py` calling `skills/settle/scripts/rule_changes.py#parse(text, "docs")` with `python3 -I`, from a `git clone --no-local` of `b03b0e290` under the framer's scratch directory, over a copy of this file) | The section parses as one `add` on `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each*, with `errors` and `unread` empty |
| G21. The mechanisms a plugin can ship beside its text (read: `<scratchpad>/release-0.39.0/mechanism-inventory.md`, a claude-code-guide agent's reading of the Claude Code docs on 2026-11-25; each line a claim, none probed here; harness `claude --version` 2.1.331, executed) | The hook events, the `command`, `prompt` and `agent` hook types with their inputs, turns and timeouts, the agent-definition fields a plugin agent honours and ignores, and the other components. `frame/plan.md` *Alternatives considered* weighs each against rule 19, and no row's verdict rests on a line of it alone: where a verdict cites one, the row names it as not probed |
| G22. What this run's parties wrote, as the hook rows' cost basis (executed on 2026-11-25 at HEAD `a6feb7831`: a probe `test_tmp_count_edits.py` counting `Edit` and `Write` tool calls in the session's transcripts under the framer's scratch directory; `git diff cbaae0c59..7415cad73` added lines, counted with `wc -l` and with `grep -c -i -E` on a number or a word such as `every`, `none` or `only`) | Up to the fold, the session made 10 `Edit` or `Write` calls, 3 under `seal/threads/`; the framer 12, all under it; phase 1's crafter 37, 13 under it. Phase 1's range adds 96 lines, and 52 of them hold a number or such a word |

## Scope

In:

1. `skills/agent-contract/SKILL.md` rule 19 keeps its number, takes the heading of *Data & interfaces*, and gains the clauses listed there after its present text.
2. `skills/implement/fix-pass.md` *A paste-ready fix is read before it is applied*: a count or a universal that contract rule 19 refuses, in a paste-ready fix, is a reading that fails, so the fix pass writes that part in its own words. The section cites contract rule 19.
3. `skills/implement/fold-and-reframe.md`: the sentence that has the framer rewrite in place every sentence a decision changes also has the fold write no count and no universal contract rule 19 refuses, citing it.
4. `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* step 1: beside contract rule 21 for the orchestrator's commands, the step names contract rule 19 for the text the orchestrator's commits write, its record edits, folds, `pr.md`, *Judgments of the run* rows and a merge's resolution among them. The orchestrator opens both rules in the one reading of `skills/agent-contract/SKILL.md` the step already asks for.
5. `skills/code-review/orchestration.md`, the paragraph opening **Where the signal is one mechanism whose edges each fix pass chased**: the clause "and no sentence counts the examples or calls one of them the only one" becomes a citation of contract rule 19. The sentence that a measured shape is cited as an example and named as one stays.
6. `agents/framer.md` *Rules*: the paragraph opening **A count of a list is stated once, beside the list.** goes (`## Removes`).
7. `tests/text/test_the_rules_have_one_owner.py`: `RULES` gains a row, numbered after the highest key, whose owner is `skills/agent-contract/SKILL.md` and whose carriers are the files of Scope items 2 to 5, each linked by the citation `contract rule 19`. The row is seen red for each carrier with that carrier's citation removed (contract rule 15).
8. The work item's `changelog.md`, with a `### Process changes` row for the rule, and the version move of `frame/plan.md` *Operational impact*.

Out:

- Rewriting the counts and universals that stand in the tree today. They are true now, the class is open over every sentence of the tree, and rule 19 meets each one where a later change edits what it counts. A count found false is a finding where it stands.
- A script that reads text for a count or a universal. Whether a sentence states what the tree holds or a rule that must hold is a meaning question, which `skills/core/SKILL.md` *The first value: efficient development through the AgenticSeal process* gives to the reader and never to a grammar rule.
- A hook, a `seal` subcommand, a workflow, an agent-definition field or another component that reads text against rule 19. Each was weighed against its cost in `frame/plan.md` *Alternatives considered*, and none earns it in this item; the independent reader of a fix's records is #1615's subject.
- `skills/code-review/SKILL.md`, the paragraph opening **A paste-ready fix reaches every statement of the fact it repairs**. The proofer preloads the contract, the fix pass's reading of Scope item 2 is the step where a snippet is applied, and #1612 and #1615 both change that file (`frame/plan.md` *Overlap with the release*).
- The issue's second *Done when* line, a count in another repository's next release (`frame/questions.md` Q1).
- An edit of the policy root. Its account of the rule is the `add` of `## Rule changes`, which the settle writes.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A1. A fix pass applies a paste-ready fix | Given a round record whose paste-ready fix says "the three callers", when the crafter opens `skills/implement/fix-pass.md` at its step 9, then *A paste-ready fix is read before it is applied* tells it that such a snippet fails the reading and names contract rule 19 | the `RULES` row of Scope item 7, carrier `skills/implement/fix-pass.md`; the proofer reads that the sentence stands in that section |
| A2. A framer folds a decision | Given a fold, when the framer opens `skills/implement/fold-and-reframe.md`, then the sentence on rewriting in place names contract rule 19 for what the fold writes | the `RULES` row, carrier `skills/implement/fold-and-reframe.md` |
| A3. The orchestrator edits a record | Given a run, when the orchestrator reads step 1 of *Orchestrator: the order inside a ticket*, then the step names contract rule 19 for the text its commits write, beside rule 21 | the `RULES` row, carrier `skills/implement/orchestration.md` |
| A4. The orchestrator weighs a mechanism's edges | Given the paragraph of Scope item 5, when the orchestrator reads it, then it cites contract rule 19 and states the count clause in no words of its own | the `RULES` row, carrier `skills/code-review/orchestration.md`; and `git grep -n -F 'no sentence counts the examples' -- agents skills docs templates` prints nothing. At `b03b0e290` it prints `skills/code-review/orchestration.md:180`, which Scope item 5 rewrites |
| A5. A framer frames a new item | Given the build, when a framer is spawned, then it receives the rule from the contract and its definition holds no second statement of it | `git grep -n -F 'A count of a list is stated once' -- agents skills docs templates` prints nothing. At `b03b0e290` it prints `agents/framer.md:224`, which Scope item 6 removes |
| A6. Every agent receives the rule | Given any spawn, when the agent starts, then rule 19 is in the contract its `skills:` list preloads | `tests/text/test_every_agent_reads_the_contract.py`, unchanged; the proofer reads rule 19's body against the clauses of *Data & interfaces* |
| A7. A count stated of a moment stays | Given a frame section dated to the commit it read, or a measurement with its date, when a later change edits what it counted, then the sentence is not false, because it states that moment | the proofer reads rule 19's clause on a dated count |
| A8. The release moves to a minor version | Given the build's last phase, when it commits `changelog.md`, then `.claude-plugin/plugin.json` reads `0.39.0` in the same commit and the fragment says the version moves to 0.39.0 | `git show <phase commit> -- .claude-plugin/plugin.json`; the release checks the orchestrator runs |

## Data & interfaces

No code interface changes. The units are text.

Rule 19's heading becomes `## 19 A change rewrites the text it amends in place, and writes no count a later change makes false`, or words of the same meaning that keep the number. Its body keeps its present text, and the crafter adds these clauses in its own words, each of them:

- R1. What a change writes states no count and no universal about the tree that a later change can make false without touching the sentence. A count is a number of files, rows, callers, places or rounds; a universal is a claim that every one, none, or only one of them holds something.
- R2. The reason: such a sentence holds none of the words of the list it stands on, so the `git grep` this rule asks of the next change does not find it.
- R3. In its place, the text names the members, or cites the list, the section or the command that lists them.
- R4. A count stands in the sentence that opens the list it counts, or beside the list, where a change to the list meets it. An item's own number, such as *Scope* item 3, is a coordinate and not a count.
- R5. A universal that states a rule, what must hold, is the rule and stays. A count or a universal stated of a named commit, release or dated measurement is a claim about that moment and stays.
- R6. The reach: every text a change writes, a record, a document, a comment or a docstring, and a paste-ready fix written for another party to apply.

Where each party that writes after round 1 receives the rule, the parties being the agents `ls agents/` lists and the orchestrator:

| Party | What it writes after round 1 | Receives rule 19 | Points at it at the step |
|---|---|---|---|
| crafter, in a fix pass | code, close blocks, `gaps.md`, `changelog.md`, a paste-ready fix it applies | preload | `skills/implement/fix-pass.md`, opened at `agents/crafter.md` step 9 (Scope item 2) |
| framer, in a fold | the three frame files | preload | `skills/implement/fold-and-reframe.md`, opened before a fold (Scope item 3) |
| orchestrator | folds of what a crafter names, `pr.md`, `routing.md`, *Judgments of the run* rows, a fix after the last round, a merge's resolution | step 1 of *Orchestrator: the order inside a ticket* | the same step (Scope item 4), and *Orchestrator: the run ends with a verifying round* (Scope item 5) |
| proofer | round records and paste-ready fixes | preload | none added (Out) |
| sealer | `guarantee.md` | preload | none added |
| tracer | facts with coordinates | preload | none added |

## Rule changes

- add
  file: docs/running/the-agent-set.md
  section: One contract every agent receives, and one definition each
  to: **Contract rule 19 keeps a change from writing a count or a universal
    that a later change makes false, and nothing reads a sentence for one.**
    A count of files, rows or places, or a claim that every one, none or
    only one of them holds something, restates a list without the list's
    words, so the `git grep` the same rule asks of the next change does not
    find it, and the sentence stands false until a round reads it. In
    releases 0.0.2 to 0.0.4 of a repository that runs the chain, 14 of the 72
    defects that a commit after round 1 introduced were such a sentence,
    written by the crafter's fix pass, the framer's fold and the
    orchestrator's record edits (#1613). Until 0.39.0 the rule stood in
    `agents/framer.md` for the frame's counts alone, so it bound the framer
    and no other party that edits a record. In the contract it binds every
    agent, and the orchestrator opens it at step 1 of
    `skills/implement/orchestration.md` *Orchestrator: the order inside a
    ticket*. Whether a sentence states what the tree holds or a rule that
    must hold is the reader's judgment, so no script reads for one.
    check: tests/text/test_the_rules_have_one_owner.py

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| a rule sentence: the framer's count rule, scoped to the frame files | `agents/framer.md` *Rules*, the paragraph opening **A count of a list is stated once, beside the list.** | contract rule 19, clauses R3 and R4 of *Data & interfaces*, which the framer preloads. Its catch record: it came in with #1419 for a count restated across a frame, and it bound no party but the framer |
| a copy: the count clause of the orchestrator's guidance on a mechanism's edges | `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*, the paragraph opening **Where the signal is one mechanism whose edges each fix pass chased**, the clause "and no sentence counts the examples or calls one of them the only one" | contract rule 19, which the paragraph cites in its place (Scope item 5) |

Framed 2026-11-25 by framer, before the build.
