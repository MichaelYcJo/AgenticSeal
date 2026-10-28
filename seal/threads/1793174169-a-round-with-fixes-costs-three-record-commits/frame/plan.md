# Implementation Plan: 1793174169-a-round-with-fixes-costs-three-record-commits

Approved <date> by <who>, when `crafter` was spawned.

## Summary

In #955 and #1016 the fix pass wrote only the `answer:` lines, and the
orchestrator rewrote every `verdict:` in a commit of its own. A round with
fixes then cost three record commits where the tree describes two. The tree
already named the fix pass as the one writer. The split came from the
orchestrator's fix-pass spawn prompts in that session, which told the fix
pass to leave the verdicts alone (`frame/design.md`, *Scope*, item 4).

This work keeps the fix pass as the writer. It states, in the orchestrator's
file, that the orchestrator writes neither line of a finding a fix pass
answers, and that a close it doubts goes into the verifying round's prompt.
It states, in the crafter's rule, that both lines of a finding go in one
commit. A finding the orchestrator closes without a fix pass takes both
lines from the orchestrator, in one commit. The rule goes to the policy
root through `frame/design.md`'s `## Rule changes`. No check changes. One
phase builds it.

## Technical context

- **What the tree says now (read, at `5287dd42`).**
  - `agents/crafter.md:17-21` (*Job*) names "in a fix pass the `verdict:`
    and `answer:` lines of each open finding" as the crafter's writes.
  - `agents/crafter.md:148-157` (*A fix pass writes two lines of each
    finding and no phase record.*) says how. It does not say the two lines
    go in one commit.
  - `docs/the-review-record.md:135-146` says "The fix pass writes two
    lines per finding and nothing else in the file."
  - `skills/code-review/orchestration.md:54-58` says the crafter's fix pass
    changes "its verdict and its answer". It says nothing about the
    orchestrator's own hand on either line.
  - `skills/implement/SKILL.md:484-489` names the fix pass and cites the
    review record.
  - `skills/code-review/orchestration.md:155`, the framer's route, has the
    orchestrator close every open finding `deferred the frame` and names no
    `answer:`.
- **What reads the lines (read).** `chain_check.py#verdict_problems`
  (`:1643-1685`) refuses an `open` verdict. For a `fixed <commit>` it
  checks that HEAD descends from the commit and that the commit touches a
  `location:` path. It reads no history of who wrote the line, or when.
  `seal pr-body` copies the `verdict:` and `answer:` lines into the pull
  request body (`changelog/0.23.1.md:31`).
- **The tests that hold the text (read).**
  - `tests/text/test_a_moved_rule_leaves_its_definition.py:495-512` holds
    the crafter's fix-pass paragraph by its clauses.
  - `tests/text/test_the_rules_have_one_owner.py#RULES` (`:133-138`, rule
    18) and `test_the_fix_pass_reads_the_implementers_context_before_it_resumes`
    (`:167-182`) hold the orchestration section this work edits.
  - `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`
    requires a `Grounds` cell for a `still a sentence` row (`:249-252`). It
    does not read the cell's words.
- **The evidence (executed).** The counts of `+verdict:` and `+answer:`
  lines per answer commit are in `frame/design.md`, *Scope*, under *What a
  round with fixes costs after this work*. The spawn-prompt lines that
  caused the split are in item 4 of the same section.
- **Failure scenario of the chosen approach.** The rule stays a sentence,
  and nothing refuses a split. Six months on, an orchestrator writes a
  fix-pass prompt from memory and moves the verdicts to itself again. Each
  round then costs one more record commit until a proofer reads the fix
  range's commits, or the owner reads the history. No wrong verdict reaches
  a merge either way. The verdict is still checked against its commit and
  weighed by the next round. The cost is a commit and an orchestrator turn
  per round.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. Keep the fix pass as the one writer. Its two lines per finding go in one commit after its fix commits. The orchestrator writes neither line of a finding the pass answers, and puts a doubted close into the verifying round's prompt. A finding the orchestrator closes without a fix pass takes both lines from it. Each party's file states its own act. The policy rule is added through `## Rule changes`. | The rule is text, and an orchestrator's prompt can still split the lines. The cost of a split is one record commit per round, visible in the history. | Chosen. The structure kept is the answer commit after the fix commit. The premise that keeps it was checked: a `fixed` verdict names an existing commit (`docs/the-review-record.md:50`, the grammar row), and `chain_check.py#verdict_problems` (`:1643-1685`) reads ancestry and touched paths from that commit. A commit cannot name itself. |
| B. Replace the writer: the crafter hands its verdicts and answers back, and the orchestrator writes both lines. | The party that did not judge the finding retypes the grounds for a `rejected`. Retyped records are the class #1044 removed from pull request bodies: `seal/process/0.23.1.md` row 2 counts four of five withheld sealer runs in 0.23.0 and 0.23.1 over a hand-written sentence that restated a record wrongly. The commit count is the same as A. | Rejected. |
| C. The fix pass leaves both lines uncommitted, and the orchestrator commits them with the next round's record. This saves one record commit per round. | The verifying round's `target:` names the fix commit, and the closes that round weighs are in no commit. `skills/implement/SKILL.md` *2. Implement test-first* says work still in the working tree is not visible to the reviewer. A session that ends between the hand-back and the record commit leaves a dirty worktree. The worktree guard then asks about it mid-run, under automation. | Rejected. |
| D. Add a check. `chain_check.py` reads each round record's history and refuses a finding whose verdict left `open` in a commit that did not also write its `answer:`. | The refusal comes at the pull request, after the split is committed. The only cure is rewriting the branch's history, and nobody in a run rebases. So a true refusal stops a ready pull request over a defect that harmed nothing at merge. It adds a mechanism and removes none (`CONTRIBUTING.md` *What a change to a gate must carry*). Reading every commit of every round record also puts a git-history walk into a check that today reads one commit per finding. | Rejected. `frame/questions.md` head item 1 records that this departs from `routing.md`'s *Why this way*. |
| E. Replace the verdict's shape. A bare `fixed` goes in the fix commit itself, and the check finds the commit through the line's history (`git log -L`). The answer commit disappears. | The grammar row lives in `docs/the-review-record.md` *The round record*, and `chain_check.py` loads it from there at import (`:63-87` of that document). The policy root changes only at the settle after the release, so until then the check refuses a bare `fixed`. `seal pr-body` copies the verdict line, so the body would also lose the commit a reader opens. | Rejected. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 2, 3, 5 and 6. In `skills/code-review/orchestration.md`, the fix-pass paragraph at `:54-58` is rewritten in place, and row *The record* of the framer's-route table at `:155` gains the `answer:` line and one commit. `agents/crafter.md:148-157` gains the one-commit sentence. `skills/implement/orchestration.md:666` gains one `Grounds` sentence. The changelog fragment names the cause by session id and line. The S1, S2 and S3 clauses go into `tests/text/test_the_rules_have_one_owner.py` and `tests/text/test_a_moved_rule_leaves_its_definition.py`, each seen red against `5287dd42` before the text lands. | S1 to S4 of `frame/design.md`. `bin/test` runs over `tests/text/test_the_rules_have_one_owner.py`, `tests/text/test_a_moved_rule_leaves_its_definition.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/behaviour/test_docs_line_wrap.py` and `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`, one module at a time, all green. The phase record names each seen-red run (contract rule 15). S5 is the round's `chain_check.py` run, and S6 is the round's and the sealer's reading. | |

## Operational impact

None. There is no migration, environment variable, dependency or
compatibility break. An orchestrator in a repository that uses the plugin
reads one more instruction for the fix pass, and the crafter reads one more
sentence. The round record's grammar and every check's verdict are
unchanged. The policy sentence reaches `docs/the-review-record.md` at the
settle after the release.
