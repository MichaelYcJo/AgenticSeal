# Implementation Plan: a shipped rule cites this repository's process

## Technical context

The work edits prose in six files at the base `0c68b9933`. Every line number below was read there.

- `skills/code-review/orchestration.md:285-288`, under *Orchestrator: the pull request opens once the sealer seals*. This is the bold rule "A conflict with the base is integrated by merging the base into the branch, never by a rebase." and the sentence after it, which carries the citation.
- `skills/implement/orchestration.md:60-64`, under *Orchestrator: the order inside a ticket*. This is the sentence that folds a decision into the issue body before the frame is committed, and its citation. #1320's only hunk in this file is at line 361, so the two branches touch different paragraphs.
- `skills/settle/SKILL.md:66-71`, *When it runs*.
- `skills/implement/SKILL.md:303-307`, under *3. The SDD file set*, the sentence on a rebase during the work. Round 1's finding 1 added it (*Judgments of the run*).
- `docs/releasing/release-checklist.md:17-22`, the second box of *0. Before starting*, and `:31-35`, the first paragraph of *2b. Settle what earlier releases left behind*.
- `docs/releasing/issues-and-milestones.md:315-339`, *An issue is its body and its comments together*.

These cases read the edited sections and stay green. `tests/text/test_the_rules_have_one_owner.py#test_a_decision_after_the_frame_is_folded_into_it` pins "folds the decision into the issue body" inside the order, so the builder keeps those words in the sentence it extends. The same module pins "A conflict with the base is integrated by merging the base into the branch, never by a rebase." in the code-review section. `tests/text/test_settle_reads_before_it_removes.py#test_the_release_checklist_carries_the_by_hand_step` reads the checklist for `settle --apply` and `skills/settle/SKILL.md`. `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` reads *0. Before starting* for the absence of `.test_durations`. `tests/behaviour/test_docs_line_wrap.py` holds both process documents to their wrap. Each new citation is a backticked path followed by an italic section, which `tests/behaviour/test_a_cited_section_stands_in_its_file.py` resolves.

The failure scenario of the chosen approach, six months on: a later work item rewrites one of the three skill sections and drops the moved sentence. The process document's citation still resolves, because the heading stands. The rule is then stated nowhere, and no case goes red. The same risk already holds for every rule the skills state, and the proofer reads each rewritten section against its base text. This work adds no case that pins the moved wording, because `docs/running/what-a-script-gates.md` *The checks* removes such pins.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Each rule's home is the skill that applies it, the skill drops its citation, and the process document keeps the person's act for the day and cites the skill section | A rewrite of the skill section drops the rule, and the citation still resolves (*Technical context*) | Chosen. The applying party opens that skill at that step (`skills/core/SKILL.md` *A document is cut by who opens it and at which step*), and each skill states the rule in its own sentence, the code-review section once its conflict rule widens to every rebase. So the move mostly removes text |
| Each rule's home is a document under `docs/running/`, which the issue allows ("a document of `docs/` that `docs/README.md` lists outside *The process*"), and each skill cites it | The orchestrator integrating a conflict, or folding a decision, opens a second file for a rule its own skill could state. The skill paragraph shrinks to a pointer, and every spawn that opens the skill pays for the extra file | Rejected. It costs a read at each step and moves no rule closer to its reader |
| Keep the structure: the rules stay in the process documents, and the skills keep citing them | An agent in another repository follows the citation to this repository's release-day list for a rule its own run needs. A change to that list made for this repository's release, such as a restructured *2b*, moves the agent's rule without the skill's reader seeing it. The premise for keeping it is that the process documents ship, so the link resolves. That premise was checked and holds: the installed 0.30.0 copy has `docs/releasing/` (executed: `ls`). But the link resolving is not what the issue asks, and its *Done when* fails | Rejected |
| Drop the never-rebase box from *0. Before starting* entirely, with no citation | The owner working down the list on the day integrates a work item branch by a rebase. `chain_check.py`'s records arm refuses at the pull request, after CI, because HEAD no longer descends from the round records' commits (`skills/core/SKILL.md`, the invariants table). The box costs one line and catches the act before the cost | Rejected. The box stays, shortened, with the citation |
| State the three moves as operations in `## Rule changes` for the settle, as the issue body's *Rule change* paragraph asks | The process documents keep the rules until a settle the owner calls, and the settle gathers a decision this pull request can make. 0.30.0's boundary puts a policy-root subject in its own pull request, and the owner's second comment on #1234 applies it here | Rejected (`frame/design.md` *Grounding*, first row) |
| Pin each moved sentence with a new text case | A pin of wording goes red where the meaning holds, the result `skills/core/SKILL.md` *Judgment is spent where meaning is the question* calls the worst. At the 0.27.1 settle, #1216 met 11 such cases | Rejected. Citations that resolve and the existing cases are the verification (`frame/design.md` *User scenarios & acceptance*) |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope items 1, 2, 3, 4 and 5 of `frame/design.md`, and the six rows of its `## Removes` | A1 and A6 by their commands. A2, A3 and A5 in one narrow run of `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/text/test_the_rules_have_one_owner.py`, `tests/text/test_settle_reads_before_it_removes.py`, `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, `tests/behaviour/test_docs_line_wrap.py` and `tests/skills/test_settle.py`. The run also includes every other module that reads one of the five edited paths, which the builder lists with `git grep -l` on each path (contract rule 2). A4 is read by the proofer | 8b14bdbb7 |

## Operational impact

None. No script, hook, configuration row or dependency changes. The edits ship in 0.30.1 as text an agent reads.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-03 | Round 1's finding 1 is folded into the frame: *Scope* item 1 widens the code-review section's rule from a conflict to every rebase and brings `skills/implement/SKILL.md`'s rebase sentence in line, and the chosen approach's verdict says so. The fix pass builds it, and a verifying round reads it, because it touches files outside the records | The frame said the skill already stated the rule; it stated the conflict case only, so "for any reason" would have been lost (`trail/rounds/round-1.md`, finding 1) | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, a decision after the frame is folded into the frame; `skills/core/SKILL.md`, the invariants table, no fix that no round reads |
| 2026-11-03 | Round 2's finding 1 is folded into the frame: *Data & interfaces*, *Technical context* and the *Grounding* rows on the subject and on #1320 name `skills/implement/SKILL.md`, and `## Removes` gains a seventh row for the instruction the fix took out. Phase 1's Delivers cell stays, because phase 1 delivered six rows. The fix touches the work item's records alone, so no verifying round follows and the sealer reads it | The fold after round 1 widened *Scope* item 1 alone; this fold reads the whole frame against HEAD (`trail/rounds/round-2.md`, finding 1) | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*; `skills/core/SKILL.md`, the invariants table, no fix that no round reads, or by the sealer where it touched the work item's records alone |
