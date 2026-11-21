# Implementation Plan: 1795276650-the-batch-spans-every-issue-of-the-request

## Technical context

The tree as read at `5c4bdc8d5`.

The rule's home is `skills/implement/orchestration.md` *Orchestrator: what needs a person is asked in one batch, before the first edit* (`:194-227`), and two files point at it: `skills/implement/SKILL.md:163-166` and `skills/core/SKILL.md:93-98` (`frame/design.md` G1 to G3). The tree already treats the routing answer as the request's (G4), and it already has a home for a decision made before an item's frame, the item's issue body (G5). So the work states the scope in the home, cites those two existing homes, and adds no record. `skills/implement/routing-question.md` *Orchestrator: the two language keys* is the one rule under which a later item's start would ask again, for a missing language key, and D4 closes it. Three statements a person reads, in `README.md`, `README.ko.md` and `skills/config/SKILL.md`, describe the same asking at a work item's start, and D5 to D7 rewrite them (`frame/design.md` G11).

Constraints: the section's heading stays, because `tests/text/test_the_rules_claude_md_names_have_one_home.py` reads it in the home and in the core (G8). The list that opens "Two things sharpen the list" keeps its two bullets, so its count stays true. No two files may share a run of 15 words, and every edited file but `skills/config/SKILL.md` wraps at 88 columns (G9). `skills/implement/orchestration.md` grows by the words `frame/design.md` G10 gives, and every orchestrating session reads it.

Failure scenario of the chosen approach, six months on: a milestone of ten issues puts one long batch in front of the person, who answers a later item's question without the context that item's work will reveal. The section's bullet **Assume, in writing, whatever would not change what you build** still trims the batch, and a decision that only the build reveals still goes to `frame/questions.md` as the paragraph opening **Once the batch is answered** says. A second failure: the orchestrator forgets to fold a later item's answer into its issue body, and that item's framer frames without it. The fold rule G5 cites is the one the orchestrator already keeps for every decision made before a frame, so this work adds no new act to forget, only a new source of decisions for it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. Amend the section in place: a scope paragraph after the first, the tree check inside the first bullet, and the lead naming every item; the two other files point with the same scope (D1 to D3) | The section grows by the words `frame/design.md` G10 gives, and every orchestrating session reads them. | Chosen. It is the issue's *Decision*, and the scope stands once, in the home. |
| 2. Keep a batch per item and add only the tree check | The incident the issue reports repeats wherever the tree does not answer: a question at a later item's start stops a run the person left unattended. The issue's first *Done when* item is not met. | Rejected. |
| 3. Replace the structure: drop the batch for a request of several issues and let every later question take the default of `docs/running/the-run.md` *The run* | That paragraph applies only where `routing.md` reads `Automation` `yes`. Under `no`, or for a decision only a person can make, the question still arrives at minute thirty. The premise that keeps the batch is the section's own: a question asked before the work starts costs a reply, and one asked later stops everything. The issue's incident shows the premise holding (`frame/design.md` G12). | Rejected. The structure stays. |
| 4. State the scope in full in `skills/implement/SKILL.md` and the core as well | Three statements of one rule drift apart, and `tests/text/test_no_passage_is_pasted_into_a_second_file.py` refuses a pasted run. The issue asks that the two files copy none of it. | Rejected. |
| 5. A new section for a request of several issues, beside the batch section | Two homes for when a person is asked. The core and `skills/implement/SKILL.md` cite the batch section, so a reader following either never reaches the new one. | Rejected. |
| 6. Write the tree's answer into the issue body, as G5's fold does | An outward write on GitHub for each answer, and the work item's records under `seal/threads/` keep none of it, against `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both*. The answer is the orchestrator's judgment against a coordinate, not the person's decision. | Rejected. The answer goes in *Why this way* of the `routing.md` of the work item the issue opens, written at that item's start (G6). |
| 7. Write every later item's `routing.md` when the request starts | A later item's branch is cut from the release branch when the item starts, so a `routing.md` written earlier stands on no branch of the item. The decisions a batch answers already have a home that outlives the session, the issue body (G5). | Rejected. Each `routing.md` is written when its item starts, from the batch's routing answer. |
| 8. Rewrite every sentence that says the language keys are asked before a work item's first edit (`frame/design.md` G11 lists them) | The sentences whose subject is the batch or an act placed before an edit change for nothing, the policy root's two editions among them through `## Rule changes`: they stay true. If they stayed and were misread, an orchestrator would ask for the keys again at a later item whose base lacks them; it opens `skills/implement/routing-question.md` on exactly that condition, and D4 answers it there. The three whose subject is a work item's start do not stay true (round 1 finding 3). | Rewrite the three, `frame/design.md` *Scope* items 6 to 8, and keep the rest. |
| 9. Add a case that pins the new scope's words | A case matching words re-encodes a judgment of meaning as a grammar rule, which `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest* rules out. The cases that read the section say its sentences are the proofer's to read (`tests/behaviour/test_waiver_decided_at_start.py:776-777`, one of them). | Rejected. S1 to S4 and S8 are read at review. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 5, with this work item's `changelog.md`; the version move of *Scope* item 5 goes in the commit that adds `changelog.md` | S1 to S6 read or run at the phase's commit; S7's narrow run exits 0 | `2c3c68807` |

## Overlap with the release

The spawn names no other work item of `release/v0.38.4`, and the release branch holds no pull request (`frame/design.md` G14), so nothing meets this work.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|

## Operational impact

No migration, environment variable, dependency or compatibility break. The version moves from 0.38.3 to 0.38.4 at `.claude-plugin/plugin.json:4`, because this is the first pull request into `release/v0.38.4` (`skills/implement/orchestration.md` *Orchestrator: how the work is routed*). Phase 1's crafter makes the move in the commit that adds `changelog.md`. `.claude-plugin/marketplace.json` holds no version field (`frame/design.md` G13), so it has no line to move. The fragment closes its entries with "The version moves to 0.38.4." as the 0.38.3 fragment did, and it carries a `### Process changes` row in the shape of `templates/records/process.md` for the change to the batch section.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-22 | The title takes `fix:` | The section let an orchestrator stop a run over several issues with a question at a later issue's start, and let an issue's line that leaves a decision to a person enter the batch unchecked: behaviour the rule exists to prevent, which the diff corrects without adding a mechanism | `skills/commit-pr-convention/SKILL.md`, the prefix vocabulary; issue #1563 *Decision* |
| 2026-11-22 | Round 1 findings 1 and 2 change the frame: D1's scope paragraph names the moment "there" points to, and the bullet names the work item whose `routing.md` takes the tree's answer, when that file is written, and that a later work item checks the issue's line against the tree again at its start | Both findings are located in `frame/design.md` D1, the text the crafter copies word for word, so the fix is the frame's before it is the build's | `trail/rounds/round-1.md` findings 1 and 2; `skills/implement/orchestration.md` *A decision made after the frame is committed is folded* |
| 2026-11-22 | Round 1 finding 3 widens *Scope*: `README.md`, `README.ko.md` and `skills/config/SKILL.md` state the language-key question at the request's first edit, and the two READMEs the routing question as well | Each still ties a question to a work item's start, which the section now contradicts for a request of several issues; G11 read those sentences as true and its search missed the READMEs' routing sentence | `trail/rounds/round-1.md` finding 3; `frame/design.md` G11 and *Scope* |
