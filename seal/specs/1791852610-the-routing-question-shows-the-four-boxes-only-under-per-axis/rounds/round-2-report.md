# Round 2 report — 1791852610, the routing question shows the four boxes only under per axis (#911)

Target `9ba76fad`, base `origin/release/v0.21.1` at `321e9de1`. This is the
verifying round: its target is the fix range `ab821298..4d55d7a5`, two
commits, and its job is whether round 1's three closed verdicts are closed.
Reading was done in the worktree. Everything run was run in a
`git clone --no-local` of it at the target, under this round's directory in
the session scratchpad, with `SPECSEAL_CASE_CEILING_S=600` set because the
machine was loaded. The clone, its virtualenv, the probe script and the logs
were deleted before this report was handed over.

## The shape of what was found

All three fixes hold, and the new case is correct and watches both directions
of what it claims.

1. Round 1's finding 1 is closed. The paragraph now calls the second call a
   second wait and cites §1 only for what §1 says.
2. Round 1's finding 2 is closed. The assertion reads the sentence that
   carries the claim, and deleting that sentence turns it red.
3. Round 1's finding 3 is closed. The count is six.
4. The new units are correct. Two mutations of the reader, one in each
   direction, each turn the new case red.
5. What is left is in the records and one policy paragraph, and none of it
   needs a fix: the frame still reads §1 and the old grounds the way round 1
   corrected (⬜ 7, ⬜ 8, corrections), and the guard spec does not name the
   shape the new case pins (⬜ 9).

The smith's history question has an answer and owes no change: the comment at
`tests/test_review_axes.py:123` is true of #88.

## The three answers

### Finding 1 — the §1 citation (`skills/implement/orchestration.md:270-278`)

The paragraph now reads *That is a second wait, and it is the trade #911
took*, and cites §1 for one thing: a question asked before the first edit
costs a reply rather than a stopped session. `skills/implement/SKILL.md:203-206`
says exactly that (*Asked before the work starts, it costs a reply. Asked at
minute thirty, it stops everything*), and the new paragraph no longer
contradicts the sentence after it (*three interruptions cost three waits*).
The trade is attributed to #911, which is where `questions.md` Q1 takes it
from. Closed. Read.

### Finding 2 — the batching test (`tests/test_chain_hooks_hardening.py:1275-1309`)

The assertion now reads `Question 1 goes in one call of its own` over the
whitespace-flattened file, and that sentence is at
`skills/implement/orchestration.md:263`, wrapped across two lines, which is
why the flattening is needed. Its message states the new shape. The bare
`in one call` it replaced is gone, and the comment says why: the
`routing.md`-batching sentence at `orchestration.md:439` satisfied it too.

The comment at `:1305-1309` now quotes `agents/framer.md`'s diagram line,
and `agents/framer.md:275` carries those words. The sentence is broken after
*will* onto a short line, which is cosmetic and not reported.

Executed: `mutation-check` replaced *Question 1 goes in one call of its own,
and two* with *Question 1 goes first, and two* and ran the case. It went red
with the new message at `:1279`, and the file was restored from its bytes.
Closed.

The class was swept again (§12): `git grep` for *one call*, *one wait*,
*same call*, *is five*, *presets beside* and *second click* over `tests`,
`skills`, `agents`, `templates`, `docs`, `hooks` and `CLAUDE.md`. No other
reader pins the retired shape. `tests/test_first_setup_asks_once.py:147`
reads the bootstrap's own two-question call, which the spec leaves out of
scope. Read.

### Finding 3 — five for six (`skills/implement/orchestration.md:276`)

The sentence reads *two presets beside the four boxes is six*. Closed. Read.

**The smith's question about `tests/test_review_axes.py:123`.** The comment
says the #88 shape moved *because two presets beside the axes is five
options*. That is true of #88. Before #88 the section asked *one
`multiSelect` question with three checkboxes*
(`865a9807~1:skills/implement/orchestration.md:183`). #88's frame rejected
*#88's own two presets plus three axes* as *Five options in one question,
which the four-option cap refuses* (`plan.md:101` of work item
1789518345 at `865a9807`), and the fourth box arrived in the same build.
So the five counted the three axes #88 measured. It went wrong in
`orchestration.md` only because that document already sat beside four boxes,
which is what round 1 found. The test comment is history and stays as it is.

## The new units

`tests/test_the_guard_asks_once_per_session.py#boxes_alone` (`:1483`) builds
the second call through `ask_entries` with `BOXES`, `multi=True` and
`BOXES_QUESTION`, which is the shape `with_the_boxes` already uses for the
boxes inside the first call. An empty tick joins to an empty answer, which
the reader never looks at because it skips the question on `multiSelect`.

`tests/test_the_guard_asks_once_per_session.py#test_the_boxes_asked_alone_neither_give_nor_take_back_the_press`
(`:1495`) makes three claims, and each was read against
`hooks/worktree_consent.py#_routing_answer` and executed:

| Claim | Watched by | How it was shown red |
|---|---|---|
| `per axis` then a boxes call is not the press, for all, one or no box | the loop at `:1504-1507` | mutation A: `_routing_preset(result) or` any `multiSelect: true` question. Red at `:1506` |
| an earlier press stays taken back | `:1509-1511` | covered by mutation A as well |
| a boxes call alone does not take a press back | `:1513-1515` | mutation B: the take-back loop also returns False for a `multiSelect: true` question. Red at `:1514` |

The smith's docstring and the ledger's S5b row name only mutation A. Mutation
B is the one that shows the third clause is watched, so it is recorded below
as a fact for the ledger rather than as a finding. Correct.

## Findings from reading

### ⬜ 7 — the frame still reads §1 the way round 1 corrected (a correction)

`spec.md:20`, the Grounding row for `skills/implement/SKILL.md` §1, says *a
second call that follows the first immediately, before the first edit, is
still the one batch*. `questions.md:17`, Q1, says *§1 says a question's cost
is when it arrives, not its click count*. Both are the reading round 1's
finding 1 removed from `orchestration.md`, and the fixed paragraph now says
the opposite: *That is a second wait*. The decision is unchanged and its
grounds are #911's own table. Only the attribution in the records is stale.

### ⬜ 8 — the frame keeps two grounds round 1 found false (a correction)

`spec.md:21` says the old section's grounds *two presets beside the boxes is
five options … stay true and are kept*, which is round 1's finding 3.
`spec.md:113-117` keeps the bare `in one call` assertion *because that case
is about the batch being one wait and still holds*, which is round 1's
finding 2. Both were fixed in the tree and not in the frame.

### ⬜ 9 — the guard spec names two shapes, and `per axis` now writes a third

`docs/worktree-guard-spec.md:306-311`, rule 3 of §*Creation consent*, says
that question 1 alone and question 1 with the boxes beside it read the same.
The shape a `per axis` run now writes, question 1 alone and then the boxes in
a call of their own, is pinned by the new case and the S5b ledger row, but no
policy sentence states it. The `Enforced by:` line at `:529` lists the S5
case and not the new one. The behaviour follows from the rule's mechanism (a
`multiSelect` question is skipped), so nothing ships wrong; a reader of the
policy has to derive it.

## Findings from execution

None. Every run confirmed: the two cases at the target, the six prose
readers of the rewritten paragraph, three mutations, and the ledger fragment.

## Regression tests to plant

None. The case the round 1 report proposed is planted, and both directions
of it are watched.

## Facts for the evidence ledger

- `tests/test_the_guard_asks_once_per_session.py#test_the_boxes_asked_alone_neither_give_nor_take_back_the_press`
  goes red at `:1514` when the take-back loop of
  `hooks/worktree_consent.py#_routing_answer` also returns False for a
  `multiSelect: true` question. Executed this round through `mutation-check`,
  file restored from its bytes. It backs the S5b row's last clause, *a press
  is not taken back by a boxes call alone*, which the row's own evidence (the
  True-direction mutation) does not reach.
- `tests/test_chain_hooks_hardening.py#test_the_questions_are_collected_before_the_work_not_during_it`
  goes red when *Question 1 goes in one call of its own* is removed from
  `skills/implement/orchestration.md`. Executed this round.
- The ledger fragment reads 81 ok, 0 drifted, 0 broken under
  `evidence-check --ledger` at `9ba76fad`, and the work item's records refuse
  no name. Executed this round. The three new `Re-read ·` rows for
  `tests/test_chain_hooks_hardening.py` were read against the released rows
  they cite (`seal/releases/0.12.0.md` rows 69 and 81, `seal/releases/0.12.1.md`
  R1): all three are about the agent-definition sweep, which the fix did not
  touch, so a re-read is the right row and not a correction.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 1's finding 1 is closed — the paragraph calls the second call a second wait and cites §1 only for its pricing | `skills/implement/orchestration.md:270` | confirmed | Read: `orchestration.md:271` *That is a second wait*; the cited half is `skills/implement/SKILL.md:203-206` *Asked before the work starts, it costs a reply* |
| 🟢 | round 1's finding 2 is closed — the assertion reads the sentence that carries the claim, and its comment quotes what `agents/framer.md` says | `tests/test_chain_hooks_hardening.py:1279` | confirmed | Executed: `mutation-check` removing *goes in one call of its own* from `orchestration.md:263` is red at `:1279` with the new message; `agents/framer.md:275` carries the quoted line; class re-swept with `git grep` |
| 🟢 | round 1's finding 3 is closed — the count is six | `skills/implement/orchestration.md:276` | confirmed | Read; the comment at `tests/test_review_axes.py:123` is true of #88, whose frame counted two presets beside three axes (`plan.md:101` of 1789518345 at `865a9807`) |
| 🟢 | The new units are correct and watch both directions | `tests/test_the_guard_asks_once_per_session.py:1495` | confirmed | Executed: green at the target; mutation A (boxes read as the press) red at `:1506`; mutation B (boxes read as taking it back) red at `:1514` |
| ⬜ 7 | The frame's Grounding row and Q1 still read §1 as making a second call one batch | `seal/specs/1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis/spec.md:20` | open | Also `questions.md:17`; the reading round 1's finding 1 removed from `orchestration.md`; a record correction, outside `Needs a fix` |
| ⬜ 8 | The frame keeps *five options* and the bare `in one call` assertion as grounds that still hold | `seal/specs/1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis/spec.md:21` | open | Also `spec.md:113-117`; round 1's findings 3 and 2, fixed in the tree and not in the frame; a record correction, outside `Needs a fix` |
| ⬜ 9 | Rule 3 names two shapes of the routing answer and not the two-call shape `per axis` now writes; `Enforced by:` omits the new case | `docs/worktree-guard-spec.md:306` | open | Behaviour right and pinned by the new case and S5b; the policy reader has to derive it from the `multiSelect` skip; `:529` lists S5's case only |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test tests/test_the_guard_asks_once_per_session.py tests/test_chain_hooks_hardening.py -q -k "boxes_asked_alone or questions_are_collected_before_the_work"` in the clone at `9ba76fad` | exit 0, 2 passed |
| `bin/test tests/test_docs_line_wrap.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_one_word_one_meaning.py tests/test_review_axes.py tests/test_the_rules_have_one_owner.py tests/test_a_moved_rule_leaves_its_definition.py -q` | exit 0, 319 passed |
| `mutation-check hooks/worktree_consent.py`, A: `if _routing_preset(result):` widened to any `multiSelect: true` question; tests `-k boxes_asked_alone` | red (exit 0 from the tool); the case failed at `:1506`; file restored |
| `mutation-check hooks/worktree_consent.py`, B: the take-back match widened to any `multiSelect: true` question; tests `-k boxes_asked_alone` | red; the case failed at `:1514`; file restored |
| `mutation-check skills/implement/orchestration.md`, *Question 1 goes in one call of its own, and two* to *Question 1 goes first, and two*; tests `-k questions_are_collected_before_the_work` | red; failed at `tests/test_chain_hooks_hardening.py:1279` with the new message; file restored |
| `evidence_check.py --ledger seal/ledger/1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis.md .` | exit 0; 81 ok, 0 drifted, 0 broken; records: 0 refused |
| `git status --short` in the clone after the probes | empty |
| Broad gate: the full suite, the repository-wide lint and the typecheck | not yet. Not run by this round. It is the sealer's, and with nothing open needing a fix it is now due: the next act is the sealer's spawn |

Every command above ran with `SPECSEAL_CASE_CEILING_S=600`.

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round 1, ⬜ 4 (open) | `skills/implement/orchestration.md:303-305` | carried open; closes at the run's end |
| round 1, ⬜ 5 (open) | `docs/worktree-guard-spec.md:981` | carried open; closes at the run's end |
| round 1, ⬜ 6 (open) | `seal/specs/1791852610-the-routing-question-shows-the-four-boxes-only-under-per-axis/overview.md` | carried open; a record correction, closes at the run's end |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

Needs a fix: no

Loses a record or crashes: no

## Proof block

Opened this round: `rounds/round-1.md` and `rounds/round-1-report.md`; the
diffs `ab821298..4d55d7a5` and `4d55d7a5..9ba76fad`;
`skills/implement/orchestration.md` (lines 250-310), `skills/implement/SKILL.md`
(lines 190-225), `agents/framer.md:275`, `tests/test_review_axes.py`
(lines 100-140), `tests/test_chain_hooks_hardening.py` (lines 1255-1320),
`tests/test_the_guard_asks_once_per_session.py` (lines 1194-1256 and
1422-1520), `tests/test_first_setup_asks_once.py` (lines 125-150),
`hooks/worktree_consent.py` (lines 195-300), `docs/worktree-guard-spec.md`
(lines 300-316 and the `Enforced by:` lines), this work item's `spec.md`
(lines 18-22 and 110-118) and `questions.md:17`, `seal/releases/0.12.0.md`
rows 69 and 81, `seal/releases/0.12.1.md` R1,
`865a9807~1:skills/implement/orchestration.md:183`, and work item
1789518345's `plan.md` at `865a9807` (grep).
