# 1792540458-on-demand-files-state-the-current-rule — phase 2

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | d4dcd59e |


## What this phase was asked

`skills/implement/orchestration.md` rewritten to the current rule. Its
routing section receives every reasoning sentence the block will drop in
phase 3, the block's routing bullet compared sentence by sentence, each
landing or going with its grounds, and the map is this record. The
approval-line shape is stated once, at the step where the orchestrator spawns
the build, with no reader but the warden. The spawn step links the writing
rules of phase 1. Headings hold no dash: `Question 1`, `Question 2`,
*Orchestrator: how the work is routed*. Section signs of heading citations
become the backticked path and the heading in italics. #945's rules are not
written here (`questions.md` Q2, default (b)).

## What this phase found

**The frame holds for this phase, with one addition.** Two more headings
carried a dash and are renamed with the three the plan names:
*Orchestrator: Bootstrap* and *Orchestrator: Parity setup*. No `docs/` line
cites either by its old text (executed `git grep`), so neither adds a
`## Rule changes` item; the one `docs/` item phase 2 owes, the worktree guard
spec's *Question 1 — single-select*, is already in `spec.md`. The old headings'
text outside `seal/`, `changelog/` and `docs/` is gone (S14, executed `git grep`
for each of the five old headings and their tails: the one hit, a docstring in
`tests/test_the_mode_is_a_row_and_a_command.py`, was rewritten, and the
comment in `hooks/worktree_consent.py` names *Question 1*).

**The approval line is stated in a `###` under the order**, *The plan is
approved at the spawn*, because the order is where the spawn is; a `###`
directly beneath an `Orchestrator:` heading is an act of the table, so it has
a row there, `part of its parent's act`. Its `check:` line is
`check: none reader: the warden at review`. The session-built case keeps the
moment the template's comment gives it, the first edit.

**The block's routing bullet, sentence by sentence** (`templates/claude-md-block.md`
at b3154f43). Phase 3 keeps what the spec's Scope 2 names; every other
sentence lands here or in the file named.

| Block sentence | Kept in the block | Where it lands |
|---|---|---|
| first, where no `seal/` root exists, stop and follow the Bootstrap section | yes | *Orchestrator: Bootstrap* |
| writing the file creates the root, creating it opts in, and where it lands is the person's decision | no | *Orchestrator: Bootstrap*, the paragraph on the once-per-repository question |
| before the first edit, write `routing.md` from the template and commit it, the write in a command of its own | yes | *Orchestrator: how the work is routed* |
| the gate reads the working tree, so the declaration silences the commit that adds it | no | the paragraph on writing the file in a command of its own |
| in a clone whose hooks slot is somebody else's, a `PreToolUse` hook denies the whole call, so a batched write is lost | no | the same paragraph; the section said only the `PreToolUse` half before |
| where the plugin's git hooks run, git decides the commit and the separate command costs nothing | no | the same paragraph, new to this file |
| this is the one place the batching rule misleads | no | the same paragraph |
| ask question 1 alone; the boxes in a second call only under `per axis` | yes | the routing section's bold sentence, kept word for word |
| never one axis at a time: the boxes mean nothing under two answers, and under `per axis` the second call follows at once | no | the routing section's second paragraph |
| question 1's three options with their descriptions | the three labels | *Question 1* |
| question 2's four boxes, their order and their unchecked meanings | no | *Question 2* |
| four options is the cap and a fifth box breaks the shape | no | *Question 2*, the ceiling |
| what is checked is the answer, and each box is a row | no | *Question 2* |
| the file records which answer was pressed | no | *What the answer writes* |
| a subagent has no `AskUserQuestion`, so the framer cannot ask | no | the routing section, *The routing question is the orchestrator's* |
| the reviewer in the middle and the pull request at the end are three waits for one decision | no | the routing section's opening paragraph, reworded so it shares no fifteen-word run with the block before phase 3 cuts it |
| the commit gate reads the file for either review answer, and CI reads it at the pull request | no | the paragraph after the wake and quiet table |
| for no work item, `[no-review]` waives one command, `[no-parity]` too | yes | the same paragraph links `skills/implement/SKILL.md` *1. Read the spec before the code*, which spells the waiver and its git spelling |
| `git -c specseal.waive=review commit` is the same waiver | no | `skills/implement/SKILL.md` *1. Read the spec before the code* (read, lines 196 to 214) |
| deciding at the commit is what stops a release mid-run | no | the routing section's closing sentence |

**Census (S11): what left, and why it could go.** Each row is a paragraph
or sentence of the file at b3154f43 that is not in the rewrite.

| What left | Grounds |
|---|---|
| the opening's account of #292 moving three sections and #351 deleting the shared checklist, and the rule about which headings kept their prefix | history; the opening now says who reads the file and what it holds |
| *One interruption or two is the whole of what is being decided* | restated by the sentence after it, that this is the only place either question is asked |
| *until #401 nothing ever asked for it*, and the moment the refusal lands | the refusal's moment stays in one sentence; the issue is history |
| *The parity setup below is the shape that answers that* | a cross-reference with no instruction; the principle it introduced stays bold |
| *offering it with a source that does not exist is worse than offering nothing* | covered by *say so rather than inventing one* |
| `seal mode shared` on a shared root answers with the switch narrative | an orchestrator that runs it is not misled, only shown more text |
| #151 named twice, as the report and as the measurement | the argument stays, that an unwritten row makes a chosen root and a default one the same bytes; the decline paragraph states its asymmetry with the mode row without the number |
| *every 0.3.x work item carried `routing.md` (#688)* | history; the told path names its two marks |
| *nobody who lands in shared mode without a question goes looking in a README* | the half sentence before it carries the rule |
| *How this work is routed is one of them* | its referent was the batch of `skills/implement/SKILL.md`, which the sentence now names |
| #911's account of four meaningless boxes shown on every run | the reason stays in the present tense |
| *This document warns below that a preset makes the least-verified path the cheapest* | nothing below warns it; the sentence pointed at text that is gone |
| the owner's misreading of `straight to the PR` as an anecdote | kept as the reason a label names what it turns off |
| *a new day is one only where it starts one* | the list of what a new session is already excludes a day by itself |
| #894's measured run and the 2026-10-12 transcript counts | measurement kept as anecdote |
| *the half the measured instance got wrong* | the half it names is stated |
| *#88's original wall* | the two ways out are named without the issue |
| #151's shape, as the reason for `Answer pressed` | the reason stays: a pressed preset and four ticks are the same bytes without it |
| *#88 holds the rule a box here would break* | the rule is stated in place: the question grows only where a decision is a person's |
| the two agents' measurement of the missing tool | the fact stays: a subagent here has no `AskUserQuestion` |
| *Measured here: routing at the start, the reviewer in the middle, the pull request at the end* | the routing section's opening states it as a rule |
| the arrows in the order and in the diagram | Scope 7 and rule (a): the order is said in words, the diagram names each party |
| *the session reads a chicken-and-egg*, *two questions put to a user*, *in all three milestone runs* | anecdote; the rule and its reason stay |
| *Prose has described this three times*, and the parenthesis on a misreading | history; the table and the sentence after it stay |
| *A work item routed to the chain used to carry "no marker at all"* | history; the rule that replaced it, the declaration quiets the arm for either answer, stays |
| *`main` is what the marketplace serves*, with `CONTRIBUTING.md` | this file ships to every repository, where the marketplace is not the reason; what a pull request into each branch does stays, and so does the criterion for taking `main` (restored at d4dcd59e after the first rewrite dropped it) |
| *the measured difference between them is 282 calls against 30* in the fix-pass row | measurement kept as anecdote in a table of deliveries |
| *the condition #330 set*, the repeated account of the meter sitting unreferenced | history; the paragraph says once that nothing makes the posting run |

**Cases rewritten or retired with the sentences they pinned** (each seen red
after the commit by `mutation-check` on the new text, executed):

| Case | What changed |
|---|---|
| `tests/test_waiver_decided_at_start.py#test_the_row_that_said_no_marker_at_all_is_gone` | retired: it pinned the narrated correction, and its absence half is `tests/test_one_word_one_meaning.py#test_the_row_that_could_not_be_true_is_corrected_not_reworded`'s |
| `tests/test_one_word_one_meaning.py#test_the_row_that_could_not_be_true_is_corrected_not_reworded` | the presence half now pins the rule, *for **either** review answer* |
| `tests/test_waiver_decided_at_start.py`, the three vocabulary rows and the planning row | `` `yes` or `no` `` in place of a middle dot; the planning row's rule sentence in place of `#88` |
| `tests/test_first_setup_asks_once.py`, the criterion pointer and the decline's asymmetry | the citation form without a section sign; the asymmetry sentence in place of `#151` |
| `tests/test_the_rules_have_one_owner.py`, the order's two cases and two links | the order in words; `AFTER_THE_SEAL_LINK` and `CRITERION_LINK` carry the new citation form for this file while `CONTRIBUTING.md` and `skills/config/SKILL.md` keep the old one until phases 8 and 6 |
| `tests/test_broad_gate_rule.py`, `tests/test_chain_hooks_hardening.py`, `tests/test_release_hygiene.py`, `tests/test_the_guard_asks_once_per_session.py` | the new spellings of the order, the wake table's cell, the base-branch sentence and the *Question 1* heading |

**New pin.** `tests/test_the_set_a_work_item_always_has.py#test_the_orchestrator_states_the_approval_line_where_it_spawns_the_build`
holds the spawn step's line equal to the template's and its two rules;
`tests/test_a_language_section_of_writing_style_opens_alone.py`'s phase 1 case
now also holds the spawn step's link to the writing rules. Both seen red under
`mutation-check` (executed): the fenced line deleted, the full-stop rule
reworded, the link's italics removed.

**Imperative sentences whose actor or condition the smith chose.** The file
is read by the orchestrator alone, so a bare imperative here has one reading;
where a pin held the imperative, it stayed, and elsewhere the sentence names
the orchestrator.

| Sentence | What was chosen |
|---|---|
| *The orchestrator approves `plan.md` by writing one line under its title when it spawns the smith* | the moment is the spawn, as the template's comment has it; the line names no commit |
| *`<who>` is the person, or the orchestrator acting under the person's routing answer* | the second reading is the one this work item's own line records |
| *Where `routing.md` answers `Implementation` with `the session`, … the line names the first edit as its moment* | the condition is the routing row, not who happens to be typing |
| *The orchestrator writes it to the rules of `skills/writing-style/SKILL.md` …* | the actor is the orchestrator and the file is the spawn prompt |
| *Ask question 1 alone; the boxes in a second call only under `per axis`.* followed by *The orchestrator puts both.* | the pinned imperative stays and the next sentence names who asks |
| *The orchestrator takes `main` when the accumulated entries read as one release, or when the change is a gate or a hook firing where it should not* | the actor is the orchestrator, who answers the base-branch half of the routing question |
| *Write `seal/specs/<work-item-id>/routing.md` into each one … and commit each* | the pinned imperative stays; the section is the orchestrator's |
| *Name such a repository in the handback and write nothing into it* | as above |
| *A run resumed in a new session puts question 1 through `AskUserQuestion` again, before the first spawn* | kept as it stood; its actor is the run's orchestrator, which the next sentences name |

**Restatement pairs of this file** (Scope 10, measured at d4dcd59e with the
module's own `shared_counts`, executed):

| Pair | Measured | `BASELINE` | Whose the residue is |
|---|---|---|---|
| `README.md` | 1 | 1 | the README, outside this item's scope beyond its block rows |
| `skills/config/SKILL.md` | 5 | 5 | phase 6, which rewrites the config skill |
| `templates/sdd-routing.md` | 3 | 10 | phase 7, which rewrites the template |
| `agents/smith.md` | 0 | 1 | drained; phase 9 removes the entry |
| `skills/code-review/orchestration.md` | 0 | 7 | drained; phase 9 removes the entry |
| `skills/implement/SKILL.md` | 0 | 1 | drained; phase 9 removes the entry |

**Bytes.** 45,087 at b3154f43, 40,967 at d4dcd59e (executed `wc -c`).
