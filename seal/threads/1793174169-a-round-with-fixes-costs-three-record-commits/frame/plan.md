# Implementation Plan: 1793174169-a-round-with-fixes-costs-three-record-commits

Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned.

## Summary

In #955 and #1016 the fix pass wrote only the `answer:` lines, and the
orchestrator rewrote every `verdict:` in a commit of its own. A round with
fixes then cost three record commits where the tree describes two. The tree
already named the fix pass as the one writer. The split came from the
orchestrator's fix-pass spawn prompts in that session, which told the fix
pass to leave the verdicts alone (`frame/design.md`, *Scope*, item 5).

Phase 1 kept the fix pass as the writer and had it commit both lines
itself, in one commit for the pass. The sealer stopped on issue #1041
*Done when* bullet 1, which gives that commit to the orchestrator, and the
owner answered on 2026-10-28 that the orchestrator makes it
(`guarantee.md:40`).

So the work now stands on row F below. The fix pass writes both lines of
every finding it answered, last, after its fix commits and its sweep's
corrections, and commits neither. On the hand-back the orchestrator commits
the round record as the pass left it, in one commit for the whole pass,
before it spawns the verifying round, and changes none of its lines. The
orchestrator writes neither line of a finding a fix pass answers, and a
close it doubts goes into the verifying round's prompt. A finding the
orchestrator closes without a fix pass takes both lines from the
orchestrator, in one commit. The rule goes to the policy root through
`frame/design.md`'s `## Rule changes`. No check changes. Phase 2 reworks
phase 1's build to this decision.

## Technical context

- **What the tree says now (read, at `aa8b54cb`).**
  - `agents/crafter.md:17-21` (*Job*) names "in a fix pass the `verdict:`
    and `answer:` lines of each open finding" as the crafter's writes.
  - `agents/crafter.md:148-159` (*A fix pass writes two lines of each
    finding and no phase record.*) ends at `:156-158` with phase 1's
    sentence, which has the crafter commit both lines in one commit for
    the pass.
  - `skills/code-review/orchestration.md:54-62` says the orchestrator
    writes neither line of a finding the fix pass answers, that its
    fix-pass prompt leaves both lines to the crafter, and that a doubted
    close goes into the verifying round's spawn prompt. `:78-80` ends the
    paragraph *The fix pass then finds what the fixes left standing* with
    phase 1's sentence, which has the fix pass make the commit.
  - `skills/code-review/orchestration.md:161`, row *The record* of the
    framer's route, has the orchestrator write both lines of every open
    finding in one commit.
  - `skills/implement/orchestration.md:666`, the `Grounds` cell, ends with
    phase 1's sentence on who wrote the two lines and in which commit.
  - `docs/the-review-record.md:135-146` says "The fix pass writes two
    lines per finding and nothing else in the file." It says nothing about
    who commits them.
  - `skills/implement/SKILL.md:484-489` names the fix pass as the writer
    and cites the review record. It says nothing about who commits.
- **What reads the lines (read).** `chain_check.py#verdict_problems`
  refuses an `open` verdict. For a `fixed <commit>` it checks that HEAD
  descends from the commit and that the commit touches a `location:` path.
  It reads no history of who wrote or committed the line. `seal pr-body`
  copies the `verdict:` and `answer:` lines into the pull request body.
- **The tests that hold the text (read).**
  - `tests/text/test_a_moved_rule_leaves_its_definition.py:495-516` holds
    the crafter's fix-pass paragraph by its clauses, phase 1's one-commit
    clause at `:512-514` among them.
  - `tests/text/test_the_rules_have_one_owner.py#RULES` rule 19
    (`:140-148`) holds the orchestrator's bold sentence.
    `test_the_fix_pass_reads_the_implementers_context_before_it_resumes`
    (`:176-199`) holds phase 1's commit clause at `:192-193`.
    `test_the_framers_route_closes_each_finding_with_both_lines_in_one_commit`
    (`:205-221`) holds row *The record*.
  - `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`
    requires a `Grounds` cell for a `still a sentence` row. It does not
    read the cell's words, and it reads headings only, so the
    orchestrator's new step needs no row of its own.
- **What else touches an uncommitted round record (read).**
  `hooks/worktree-guard.py` reads tracked changes only before a branch
  switch or a worktree creation (`docs/worktree-guard-spec.md` *Decision
  matrix*). `hooks/lib/routing.py:600-601` reads the round records from the
  working tree on purpose, and the pull request check reads what git
  carries. No hook reads the tree at a subagent's hand-back.
- **The evidence (executed).** The counts of `+verdict:` and `+answer:`
  lines per answer commit are in `frame/design.md`, *Scope*, under *What a
  round with fixes costs after this work*. The spawn-prompt lines that
  caused the split are in item 5 of the same section.
- **Failure scenario of the chosen approach.** Three ways it goes wrong.
  First, the rule stays a sentence, and nothing refuses a split. Six months
  on, an orchestrator writes a fix-pass prompt from memory and moves the
  verdicts to itself again. Where it writes them before its one commit, the
  history shows the commit the rule asks for and nothing shows the split;
  only a transcript does. Where it commits them apart, each round costs one
  more record commit, which the fix range's commits show. No wrong verdict reaches a merge, because the verdict is still
  checked against its commit and weighed by the next round. Second, a
  crafter follows *Order of work* step 6, "Commit", out of habit and
  commits the lines itself. The orchestrator then finds nothing to commit,
  and the count is unchanged; only the history shows the wrong committer.
  Third, the round record sits modified from the hand-back until the
  orchestrator's commit. That window is one orchestrator turn. A session
  that ends inside it, at a context limit or a crash, leaves the file
  modified in this work item's worktree. The next session sees it in
  `git status`. A branch switch there meets the worktree guard's
  tracked-changes row, which under the `automation` press is a deny to the
  model that names `git commit` and asks no person. The cost is a turn. An
  orchestrator that spawns the verifying round without committing gives
  that round a `target:` whose closes are in no commit, the case row C
  below describes, until the next record commit carries them.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. Keep the fix pass as the one writer, and have it commit both lines of every finding it answered in one commit for the whole pass, after its last fix commit and its corrections. The orchestrator writes neither line of a finding the pass answers, and puts a doubted close into the verifying round's prompt. A finding the orchestrator closes without a fix pass takes both lines from it. | The rule is text, and an orchestrator's prompt can still split the lines. The cost of a split is one record commit per round, visible in the history. It leaves no window with an uncommitted record, and it gives the orchestrator no act after the fix pass. | Built in phase 1 (`749cb56c`) and corrected by its fix passes (`b413456f`, `ea5f22e6`). Replaced by row F on the owner's answer of 2026-10-28 (`guarantee.md:40`): issue #1041 *Done when* bullet 1 gives the commit to the orchestrator, and the frame had named no departure from it. |
| B. Replace the writer: the crafter hands its verdicts and answers back, and the orchestrator writes both lines. | The party that did not judge the finding retypes the grounds for a `rejected`. Retyped records are the class #1044 removed from pull request bodies: `seal/process/0.23.1.md` row 2 counts four of five withheld sealer runs in 0.23.0 and 0.23.1 over a hand-written sentence that restated a record wrongly. The commit count is the same as A. | Rejected. Row F keeps the writer and moves only the commit, so nothing is retyped. |
| C. The fix pass leaves both lines uncommitted, and the orchestrator commits them with the next round's record. This saves one record commit per round. | The verifying round's `target:` names the fix commit, and the closes that round weighs are in no commit. `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test* says work still in the working tree is not visible to the reviewer. The record stays modified for a whole proofer run, and a session that ends in that span leaves it modified. | Rejected. Row F differs from it in when the orchestrator commits. F commits at the hand-back, before the verifying round is spawned, so that round's `target:` holds every close and the uncommitted span is one orchestrator turn rather than a proofer run. F pays the record commit C saves. |
| D. Add a check. `chain_check.py` reads each round record's history and refuses a finding whose verdict left `open` in a commit that did not also write its `answer:`, or one the fix pass did not write. | The refusal comes at the pull request, after the split is committed. The only cure is rewriting the branch's history, and nobody in a run rebases. So a true refusal stops a ready pull request over a defect that harmed nothing at merge. It adds a mechanism and removes none (`CONTRIBUTING.md` *What a change to a gate must carry*). Reading every commit of every round record also puts a git-history walk into a check that today reads one commit per finding. Under row F, who made the commit could not be told apart either: on this branch the crafter's `749cb56c` and the orchestrator's `9c162a3c` carry the same author (executed, `git log --format='%an'`). | Rejected. `frame/questions.md` head item 1 records that this departs from `routing.md`'s *Why this way*. |
| E. Replace the verdict's shape. A bare `fixed` goes in the fix commit itself, and the check finds the commit through the line's history (`git log -L`). The answer commit disappears. | The grammar row lives in `docs/the-review-record.md` *The round record*, and `chain_check.py` loads it from there at import. The policy root changes only at the settle after the release, so until then the check refuses a bare `fixed`. `seal pr-body` copies the verdict line, so the body would also lose the commit a reader opens. | Rejected. |
| F. The fix pass writes both lines of every finding it answered, last, after its fix commits and its sweep's corrections, and commits neither. On the hand-back the orchestrator commits the round record as the pass left it, in one commit for the whole pass, before it spawns the verifying round, and changes none of its lines. Everything else is as in A. | The three ways in *Technical context*, *Failure scenario of the chosen approach*: a split from a remembered prompt, a crafter committing out of habit, and a modified record left by a session that ends in the one-turn window. None puts a wrong verdict into a merge. | Chosen, by the owner on 2026-10-28 (`guarantee.md:40`), as issue #1041 *Done when* bullet 1 states. The structure kept from A is the answer commit after the fix commits. Its premise was checked: a `fixed` verdict names an existing commit (`docs/the-review-record.md:50`, the grammar row), and `chain_check.py#verdict_problems` reads ancestry and touched paths from that commit, so a commit cannot name itself. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 2, 3, 5 and 6. In `skills/code-review/orchestration.md`, the fix-pass paragraph at `:54-58` is rewritten in place, and row *The record* of the framer's-route table at `:155` gains the `answer:` line and one commit. `agents/crafter.md:148-157` gains the one-commit sentence. `skills/implement/orchestration.md:666` gains one `Grounds` sentence. The changelog fragment names the cause by session id and line. The S1, S2 and S3 clauses go into `tests/text/test_the_rules_have_one_owner.py` and `tests/text/test_a_moved_rule_leaves_its_definition.py`, each seen red against `5287dd42` before the text lands. | S1 to S4 of `frame/design.md`. `bin/test` runs over `tests/text/test_the_rules_have_one_owner.py`, `tests/text/test_a_moved_rule_leaves_its_definition.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/behaviour/test_docs_line_wrap.py` and `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`, one module at a time, all green. The phase record names each seen-red run (contract rule 15). S5 is the round's `chain_check.py` run, and S6 is the round's and the sealer's reading. | 749cb56c |
| 2 | The rework to the owner's answer, `frame/design.md` *Scope* item 6. `skills/code-review/orchestration.md:78-80` is rewritten in place: the fix pass writes the two lines last and commits neither, and a new bold sentence states that the orchestrator commits the round record as the pass left it, in one commit for the whole pass, before it spawns the verifying round, changing none of its lines. `agents/crafter.md:156-158` is rewritten in place to write the lines last and leave them uncommitted. The last sentence of the `Grounds` cell at `skills/implement/orchestration.md:666` is rewritten to name the orchestrator's commit. In `tests/text/test_the_rules_have_one_owner.py`, `RULES` gains an entry for the new bold sentence and the clause at `:192-193` is replaced. In `tests/text/test_a_moved_rule_leaves_its_definition.py` the clause at `:512-514` is replaced. The first bullet of `changelog.md` is rewritten to the decision. Each new clause and entry is seen red against the text at `aa8b54cb` before the text lands. `gaps.md` gains the rework's divergence row. | S1, S3, S4 and S7 of `frame/design.md`, and S2 still green. `bin/test` runs over the same five modules as phase 1, one module at a time, all green. The phase record names each seen-red run (contract rule 15) and the S7 measurement. S5 is the round's `chain_check.py` run, and S6 is the round's and the sealer's reading. | 44f37009 |

## Operational impact

None for a deployer. There is no migration, environment variable,
dependency or compatibility break. An orchestrator in a repository that
uses the plugin makes one commit after each fix pass, of the round record
the pass left, before it spawns the verifying round. The crafter leaves
that record uncommitted. The round record's grammar and every check's
verdict are unchanged. The policy sentence reaches
`docs/the-review-record.md` at the settle after the release.
