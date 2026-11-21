# Design: 1795276650-the-batch-spans-every-issue-of-the-request

## Grounding

The tree as read at `5c4bdc8d5`, which differs from `main` at `f8056edde` only by this work item's `routing.md` (executed, `git diff --stat f8056edde 5c4bdc8d5`). Every line number below is a line of that commit.

| Policy clause | What it fixes for this work |
|---|---|
| G1 `skills/core/SKILL.md` *The first value: efficient development through the AgenticSeal process*, **Asking a person is the most expensive step.** (`:93-98`) (read) | The core states when a person is asked and cites the batch section for the reasoning. Its sentence "Whatever needs a person is asked once, together, before the first edit" is one of the three statements the issue's *Decision* aligns. It keeps the citation, which `tests/text/test_the_rules_claude_md_names_have_one_home.py#LINKED` requires (G8). |
| G2 `skills/implement/orchestration.md` *Orchestrator: what needs a person is asked in one batch, before the first edit* (`:194-227`) (read) | The home of the rule. Its first paragraph (`:196-200`) has the orchestrator read "the policy, the SDD set and the ticket", one ticket. Nothing in the section says what "before the first edit" means where the person's request names several issues. The first bullet (`:210-211`) says "Read the documents and the code first" and says nothing of an issue line that leaves a decision to a person. The lead at `:220` says "Once the batch is answered, the session runs to the pull request", one pull request. The list at `:208` opens "Two things sharpen the list", and *Scope* item 1 keeps that list at its two bullets. |
| G3 `skills/implement/SKILL.md` *1. Read the documents that outrank the code first* (`:163-166`) (read) | "What needs a person is asked once, in one batch, before the first edit, by the orchestrator, which opens [the section] when it starts a work item." The clause "when it starts a work item" is the reading the issue names: each item's start opens the section again. |
| G4 Where the tree already holds a request of several items (read) | `skills/implement/orchestration.md` *Under agentic* (`:359-361`): "two items of one batch may take different routes". `skills/implement/merge-order.md:1-4` and its section: the release's other work items, each started by the orchestrator. `skills/implement/routing-question.md:148-149`: "Where the batch reaches no person, because the routing answer was given for the release and the run is unattended". Question 1's `agentic` description (`skills/implement/routing-question.md` *Question 1, the mode*): "you are not asked the route again". So the tree already treats the routing answer as the request's and not the item's, and the batch section is the one place that does not say so. |
| G5 `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph opening **Before the frame is committed, the orchestrator folds a decision into the issue body instead, in place.** (`:135-143`) (read) | A decision made before an item's frame is committed is folded into that item's issue body, and the framer receives the body as folded. An answer the request's batch gives for a later item's issue is such a decision. So it already has a home that outlives the session, and *Scope* item 1 cites that home rather than adding one. |
| G6 `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both* (read) | Whoever judges writes the decision, its grounds and the document it judged against into the work item's records under `seal/threads/`. An answer the tree gives to an issue's open decision is the orchestrator's judgment against a coordinate. So it is written in the item's `routing.md` *Why this way*, the record the orchestrator writes before the first edit, which the framer reads at its step 1 and the sealer reads at its step 4. No script reads *Why this way* (executed, `git grep -n 'Why this way' -- lib 'skills/*/scripts' .github bin`, 0 lines), so a sentence added there refuses nothing. `templates/records/sdd-routing.md` asks for "the grounds" there. For `direct`, the body of the commit holds the grounds (`skills/implement/orchestration.md` *Under agentic*, *Where the choice is written*, `:408-414`). |
| G7 `docs/running/the-run.md` *The run*, the paragraph opening **On a run whose `routing.md` reads `Automation` `yes`** (`:33-53`) (read) | It has the orchestrator look in the tree before it asks a question that arises during the run. The issue's second bullet adds the same check while the batch is collected, before the run starts. The paragraph stays true and needs no change. `docs/` is the policy root, since `seal/config.json` has no `Policy root` key (read). This work's subject is skill text outside the policy root, so the policy root is not edited and `## Rule changes` holds the no-change block (G11). |
| G8 Every case under `tests/` and `evals/` that pins a sentence this work rewrites (executed: `test_tmp_pins.py` under the scratch directory parsed every tracked `.py` file under `tests/` and `evals/` with `ast` and matched each string constant of at least 16 characters and 3 words, whitespace collapsed, against the flattened text of `skills/implement/orchestration.md:194-227`, `skills/implement/SKILL.md:163-166` and `skills/core/SKILL.md:93-98`; 150 files, 3 hits. Also executed, `git grep -n -F` over `tests evals lib bin skills/*/scripts .github` for 21 phrases of the three passages; each hit read in its case) | The 3 hits are one literal, the section's heading, at `tests/text/test_the_rules_claude_md_names_have_one_home.py:72`, matched in all three regions because the two other files cite it. The heading stays, so the case needs no change. The phrase searches found three more cases, and each keeps passing under *Data & interfaces* D1 to D4: `tests/behaviour/test_waiver_decided_at_start.py#test_the_skill_names_where_a_late_finding_goes` (`:773-787`) asserts `questions.md`, `seal/follow-up.md` and `Not done` in the orchestration file, and D1 keeps the paragraph that names them; its docstring quotes "Once the batch is answered the session runs to the pull request", and D1 keeps those words. `#test_the_batch_asks_for_the_language_rows_and_names_where_a_default_is_recorded` (`:790-813`) asserts four literals in `skills/implement/routing-question.md` *Orchestrator: the two language keys*, and D4 keeps all four. `tests/behaviour/test_chain_hooks_hardening.py#test_no_agent_definition_tells_its_agent_to_collect_questions` reads `agents/*.md` alone, which this work does not touch. The literal match misses a pin written as a regular expression or assembled at run time, so for those forms the list is a sample; the narrow run of *User scenarios & acceptance* S7 is what reaches them. |
| G9 The cases that constrain the new text without pinning the old (read) | `tests/text/test_no_passage_is_pasted_into_a_second_file.py` names a pair of files that share a run of 15 words (`skills/settle/scripts/passages.py#WINDOW`). `tests/behaviour/test_docs_line_wrap.py#COVERED` holds all four files this work edits at 88 display columns. `tests/behaviour/test_a_cited_section_stands_in_its_file.py` requires each cited heading or bold lead to stand in its file. `tests/text/test_the_rules_claude_md_names_have_one_home.py#LINKED` requires `skills/core/SKILL.md` to name the batch section's path and heading. D1 to D4 were checked against the first two (executed: `test_tmp_windows.py` under the scratch directory compared every run of 15 words of each draft, lowercased and stripped of `` ` ``, `*`, `\|`, `>` and `#`, with each other draft and with every tracked `.md` outside `*.ko.md` and the draft's own file: 0 shared runs; and an `awk` over the drafts: no line past 88 columns). That probe approximates `passages.py`'s normalisation and is not its code, so S7's narrow run is the check. |
| G10 The size of the files every run opens (executed, `wc -w` at `5c4bdc8d5`) | `skills/implement/orchestration.md` holds 5,326 words. The passages D1 replaces hold 99 words and D1 holds 328 (executed, `wc -w` on `:196-200`, `:210-211` and the lead at `:220` and on the draft), so the file grows by about 229 words. `skills/core/SKILL.md` holds 1,645 words, and D3 replaces 71 words with 66. `skills/implement/SKILL.md` holds 4,334, and D2 replaces 40 with 48. `frame/plan.md` *Technical context* weighs the growth. |
| G11 The other sentences that say when the two language keys are asked (executed, `git grep -n -i -E "work item.s first edit\|before (its\|the) first edit\|starts a work item"` over `skills agents docs templates CONTRIBUTING.md README.md README.ko.md`; each hit read) | These eight sentences say the keys are asked before a work item's first edit wherever either is missing: `README.md:127`, `README.ko.md:132`, `templates/setup/config.md:89`, `skills/config/SKILL.md:57`, `skills/implement/bootstrap.md:206-207`, `skills/commit-pr-convention/SKILL.md:84-85`, `docs/layout/one-root-by-lifetime.md:232-233`, and its edition at `docs/layout/one-root-by-lifetime.ko.md:221-223`. Each stays true: the request's batch comes before every item's first edit, and it asks for the keys wherever either is missing when the request starts. A later item's base lacks a key only where an earlier item of the same request has not merged its routing commit, and that case is stated in the home, `skills/implement/routing-question.md` *Orchestrator: the two language keys*, which the orchestrator opens on that very condition (`skills/implement/routing-question.md:4-7`). D4 states it there. The other hits name the routing declaration written before the first edit, the settle's own questions, or `merge-order.md`'s opening, none of them a batch. The search covers the spellings it lists, so the list is a sample over other spellings. |
| G12 The issue and its comments (executed, `gh issue view 1563 --json body,comments`, 2026-11-22: the body and 0 comments) | The body is the request whole. Its *Decision* has two bullets and its *Done when* three items, and *Scope* answers each. |
| G13 The version (executed, `grep -n '"version"' .claude-plugin/plugin.json .claude-plugin/marketplace.json` and `grep -n '0\.38' .claude-plugin/marketplace.json`) | `.claude-plugin/plugin.json:4` reads `"version": "0.38.3"`. `.claude-plugin/marketplace.json` holds no version field, and the commit that moved 0.38.2 to 0.38.3 (`c63d0b070`) changed its descriptions alone (executed, `git show c63d0b070 -- .claude-plugin/marketplace.json`). So the move to 0.38.4 is one line of `plugin.json`, and `marketplace.json` has no line to move. |
| G14 The release (executed: `gh pr list --base release/v0.38.4 --state all` lists 0 pull requests; `git branch -a --list '*0.38.4*'`) | This is the release's only work item, so no other frame is read (`frame/plan.md` *Overlap with the release*). |
| G15 `seal/follow-up.md` (read) | Both tables are empty, so no item waits on this work. |

## Scope

In:

1. **`skills/implement/orchestration.md` *Orchestrator: what needs a person is asked in one batch, before the first edit*** takes D1 in place. Its first paragraph (`:196-200`) reads each ticket the person's request names. A new paragraph follows it and states the batch's scope for a request that names several issues. The first bullet (`:210-211`) gains the check against the tree for an issue line that leaves a decision to a person. The lead at `:220-221` names every work item of the request. The heading, the second bullet, the paragraph opening "Something a session cannot do for itself" and the rest of the paragraph opening **Once the batch is answered** keep their text.
2. **`skills/implement/SKILL.md:163-166`** becomes D2. It points at the section with the same scope and copies none of it.
3. **`skills/core/SKILL.md:95-98`**, the sentence opening "Whatever needs a person", becomes the matching sentence of D3. The bold lead and the sentence before it keep their text.
4. **`skills/implement/routing-question.md:148-150`** becomes D4: a later work item of the same request writes the keys the request's batch got, and the default for an unattended run keeps every word but the clause that named the routing answer given for the release.
5. **The version** moves from 0.38.3 to 0.38.4 at `.claude-plugin/plugin.json:4`, in the commit that adds this work item's `changelog.md` (G13; `frame/plan.md` *Operational impact*).

Out:

- `docs/running/the-run.md` *The run* keeps its text (G7).
- The language-key sentences G11 lists keep their text (G11; `frame/plan.md` *Alternatives considered* row 8).
- No case is added for D1 to D4 (`frame/plan.md` *Alternatives considered* row 9).
- `skills/implement/routing-question.md` *Question 1, the mode* keeps its text: question 1 is still put on every new request, as the issue says.
- A request whose session ends before its last item, handed to another session through `handoff.md`, is not addressed. The answers the batch gave for later items stand in their issue bodies (G5), so a session that takes the request over can read them.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The batch covers a request of several issues | Given a request that names several issues, when the orchestrator reads the section, then it reads that it asks one batch, before the first edit of the first work item, covering every issue, and that a later item's start asks nothing new and sends what surfaces where the paragraph opening **Once the batch is answered** sends it. | The section read against D1 at the build commit. |
| S2 An issue's "the owner decides" is checked against the tree first | Given an issue line that leaves a decision to a person, when the orchestrator collects the batch, then the section tells it to check the line against the policy root, `seal/config.json`, the code and the earlier work items' records, and where they answer it, to write the answer and its coordinate in the item's `routing.md` *Why this way* and not ask. | The first bullet read against D1. |
| S3 The two other statements point at the section with the same scope | `skills/implement/SKILL.md` and `skills/core/SKILL.md` each name the section's path and heading, and each says the batch is asked before the first edit of the request, for every issue it names. Neither file shares a run of 15 words with the section. | `tests/text/test_the_rules_claude_md_names_have_one_home.py` and `tests/text/test_no_passage_is_pasted_into_a_second_file.py`; the two sentences read against D2 and D3. |
| S4 A later item does not ask for the language keys again | `skills/implement/routing-question.md` *Orchestrator: the two language keys* says a later work item of the request writes the answers the batch gave, and keeps the default for an unattended run and its record in `routing.md` *Why this way*. | `tests/behaviour/test_waiver_decided_at_start.py#test_the_batch_asks_for_the_language_rows_and_names_where_a_default_is_recorded`; the paragraph read against D4. |
| S5 The version is 0.38.4 | `.claude-plugin/plugin.json` reads `"version": "0.38.4"`, and `git grep -n '0\.38\.3' -- .claude-plugin` prints nothing, at the commit that adds `changelog.md`. | The two commands at that commit. |
| S6 The diff stays inside *Scope* | `git diff --stat 5c4bdc8d5 -- skills .claude-plugin docs agents templates README.md README.ko.md CONTRIBUTING.md tests` lists `skills/implement/orchestration.md`, `skills/implement/SKILL.md`, `skills/core/SKILL.md`, `skills/implement/routing-question.md` and `.claude-plugin/plugin.json`, and no other file. | The command at the build's last commit. |
| S7 The touched files and every case G8 and G9 name still pass | The narrow run of `tests/text/test_the_rules_claude_md_names_have_one_home.py`, `tests/behaviour/test_waiver_decided_at_start.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_chain_hooks_hardening.py` and `tests/behaviour/test_release_hygiene.py` exits 0. | The crafter's narrow run, through `bin/test`. |

## Data & interfaces

No schema, payload or command changes. The interface is text the orchestrator reads at the start of every request. Each block below is the text as it reads after the build; the crafter wraps it at the file's width and keeps every word.

**D1 The section, the parts *Scope* item 1 changes.** The first paragraph replaces `:196-200`. The second paragraph is new and stands between it and the paragraph opening "The cost of a question is not its difficulty". The bullet replaces `:210-211`. The last line replaces the bold lead at `:220`, and the paragraph's text after the lead is unchanged.

```
**Collect what needs a person before the first edit, and ask it in one batch.**
The orchestrator reads the policy, the SDD set and each ticket the person's
request names, looking for the questions as well as the answers, and puts
every one of them in front of the person at the start: a decision only they
can make, an approval, a credential, a permission the session does not have.

**A request that names several issues, such as a milestone or a release, has
one batch, and the batch covers every one of them.** The orchestrator asks it
once, before the first edit of the request's first work item. A later work
item of the same request asks nothing new when it starts. Its `routing.md` is
written from the routing answer the batch got. An answer the batch gave for
its issue is folded into that issue's body, as *Orchestrator: the order inside
a ticket* states for a decision made before the frame is committed. What
surfaces there goes where the paragraph opening *Once the batch is answered*
sends it. A new request is asked a batch of its own, question 1 of
`skills/implement/routing-question.md` among it.

- **A question you can answer is not a question.** Read the documents and the
  code first. An issue's line that leaves a decision to a person is a claim
  dated by the issue: it records what was open when the issue was filed.
  Before its question enters the batch, the orchestrator checks it against
  the policy root, `seal/config.json`, the code, and the records under
  `seal/threads/` of the work items that came before. Where they answer it,
  the orchestrator does not ask, and writes the answer with its coordinate in
  that item's `routing.md` *Why this way*, or for `direct` in the body of the
  commit that carries the change. What survives that is the batch.

**Once the batch is answered, the session runs to the pull request, through
every work item the request names.**
```

**D2 `skills/implement/SKILL.md:163-166`.**

```
What needs a person is asked by the orchestrator once, in one batch, before
the first edit of the person's request, whatever number of issues the request
names. The orchestrator opens `skills/implement/orchestration.md`
*Orchestrator: what needs a person is asked in one batch, before the first
edit* when the request starts, and not again when a later work item of the
request starts.
```

**D3 `skills/core/SKILL.md:93-98`, the whole paragraph.** Only its last sentence changes.

```
**Asking a person is the most expensive step.** Between two designs that
catch the same defect, the one that stops to ask a person costs more, and
the design that asks argues why its question is worth that cost. Whatever
needs a person is asked once, together, before the first edit of the
person's request, for every issue it names, as
`skills/implement/orchestration.md` *Orchestrator: what needs a person is
asked in one batch, before the first edit* states with its reasoning.
```

**D4 `skills/implement/routing-question.md:148-150`**, from the end of the code span that opens `:148` to the sentence's end at `:150`. The sentence after it, opening "`routing.md` *Why this way* then says", is unchanged.

```
`"<key>": "<answer>"`. A later work item of the same request asks nothing:
where its base lacks either key, its routing commit writes the answers the
request's batch gave. Where the batch reaches no person, because the run is
unattended, the orchestrator writes both keys as the language it reads the
titles in, and as `English` where the list gives none.
```

## Rule changes

- nothing
  why: no document of the policy root, `docs/`, changes. The rule's three statements and the language-key home stand under `skills/`, and the policy sentences G7 and G11 read stay true under the new scope.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The clause "when it starts a work item", which let each item's start open the batch again | `skills/implement/SKILL.md` *1. Read the documents that outrank the code first* (`:166`) | D2: the section is opened when the request starts and not again at a later item. This is what the work takes out in return for the scope paragraph D1 adds (`agents/framer.md` *A mark is not the answer to a blocked step*) |
| "the ticket", one ticket, as what the batch is read from | `skills/implement/orchestration.md` *Orchestrator: what needs a person is asked in one batch, before the first edit* (`:197`) | D1's first paragraph: each ticket the person's request names |
| The clause "because the routing answer was given for the release", which made a later item's start a batch that reaches nobody | `skills/implement/routing-question.md` *Orchestrator: the two language keys* (`:148-149`) | D4: a later item writes the answers the request's batch gave. The default stays for a run with nobody there |
| "before the first edit" read as each item's first edit | `skills/core/SKILL.md` *The first value: efficient development through the AgenticSeal process* (`:96`) | D3: before the first edit of the person's request |

Framed 2026-11-22 by framer, before the build.
