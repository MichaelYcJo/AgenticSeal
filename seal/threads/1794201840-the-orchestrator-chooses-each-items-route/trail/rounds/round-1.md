# Review round 1: 1794201840-the-orchestrator-chooses-each-items-route

```seal
target: 91421710 against release/v0.37.0
```

This round reviewed the whole diff `dfd0c995..91421710` (the merge base is
`release/v0.37.0` itself) in a `git clone --no-local` at `91421710`. It read
issue #1459's body and its seven comments, then `routing.md`, the three
frame files, `gaps.md`, `changelog.md`, `pr.md`, and both phase records,
each whole at the target. No `pr.<lang>.md` stands, and none is owed:
`seal/config.md` names English for both language rows. This is the first
round, so no earlier round's coordinates were carried. Every fact below was
established in this round.

## Findings

### 1. Both READMEs still say every run ends at a sealed pull request, while the answer they now mark may route a change with no seal

```seal
severity: should
location: `README.md:17`, `README.ko.md:21`
evidence: read `README.md:14-20`, `README.md:120-132`, `README.ko.md:14-23`, `README.ko.md:125-136`, `seal/threads/1794201840-the-orchestrator-chooses-each-items-route/trail/phases/phase-2.md:50-54`
```

Why it matters: a person deciding how to answer the routing question reads
the opening paragraph first. `README.md:14-17` now tells them to answer
`agentic`, and says the session decides which agents each item needs. The
next sentence at `README.md:17-19` stays as it was: "The run ends at a pull
request whose records carry a seal". The `agentic` bullet at
`README.md:121-125` says a small change is made "as under `direct`", and
the `direct` bullet at `README.md:131-132` says that means "no agent, no
frame, no review and no seal". So the opening promises a seal for every
run, and the list says the marked answer may skip it. `README.ko.md:21-22`
has the same sentence ("실행은 그 seal 을 기록에 담은 pull request 에서
끝나고").

Phase 2 claimed this paragraph was rewritten so that it does not promise
what the marked answer may not do (`trail/phases/phase-2.md:50-54`, judged
against *Scope* item 7). The rewrite qualified the agents sentence with
"Where an item needs them all", but the seal sentence still makes the
promise. Before this work, `automation` was the answer to give, and the
sentence was true for it.

The fix states the exception in each edition. Both are plain prose, and no
case pins either sentence (executed: `git grep -n "records carry a seal\|기록에 담은 pull request"` over `tests`, `evals` and `.github`, no hit).

```markdown
AgenticSeal is a Claude Code plugin. You hand the session an issue, and it
asks you one question at the start: how the work should be routed. Answer
`agentic`, the answer it marks, and the session decides for each item which
agents it needs and whether the run may stop to ask you. Where an item needs
them all, agents frame the change, build it, review it and seal it. Unless
the session made the change itself, as under `direct`, the run ends at a
pull request whose records carry a seal: the last agent's written guarantee
that the work agrees with the issue and the tree at one commit. It never
merges. Merging is yours.
```

```markdown
seal 은 마지막 에이전트가 쓰는 보증서입니다. 커밋 하나를 기준으로, 작업이
이슈와 트리에 맞는다고 적습니다. 세션이 `direct` 처럼 직접 고친 변경이
아니면, 실행은 그 seal 을 기록에 담은 pull request 에서 끝나고, 머지는 하지
않습니다. 머지는 사용자가 합니다.
```

### 2. The routing template asks for one or two sentences of grounds, while *Under agentic* asks the orchestrator for each row's grounds

```seal
severity: should
location: `templates/records/sdd-routing.md:16`
evidence: read `templates/records/sdd-routing.md:12-16`, `skills/implement/orchestration.md:367-370`, `skills/implement/orchestration.md:566-571`, `seal/threads/1794201840-the-orchestrator-chooses-each-items-route/frame/design.md:77`
```

Why it matters: the orchestrator writes `routing.md` from
`templates/records/sdd-routing.md`
(`skills/implement/orchestration.md:418-421`). The template's
`## Why this way` placeholder still reads `<one or two sentences>`. This
work changed what that section holds. *What the answer writes* now says
"one or two sentences where the person chose the rows, and where the
orchestrator chose them under `agentic`, the grounds *Under agentic* asks
for" (`skills/implement/orchestration.md:367-370`). *Under agentic* asks for
the person who answered question 1, that answer, and then each row's grounds
with the subsection named as the document judged against
(`:566-571`). A declaration has up to five answered rows, so the template
now gives the orchestrator a length the skill does not allow under
`agentic`. The sealer reads those grounds against the diff
(`agents/sealer.md:103-108`). Grounds squeezed to two sentences are the thin
account that reading needs to catch. They are also the thin account the
settle's step 5 sentence reads.

The frame names this template in *Out* (`frame/design.md:77`). The grounds
it gives cover only the `Answered <date> by <who>` line (G7), and the
frame's `## Removes` table took "one or two sentences nothing reads" out of
`orchestration.md` without naming the template's copy of the same length.
The fix below keeps the `Answered` line as it is and cites the skill instead
of restating it, so the length has one source. No case reads the
placeholder (executed: `git grep -n "one or two sentences"` over `tests`,
`evals` and `.github`, no hit), and `lib/routing.py#parse` reads only the
table rows (frame G6). The fix pass records the change to the template as a
departure from *Out* in its phase record or in its close.

```markdown
## Why this way

<the grounds `skills/implement/orchestration.md` *What the answer writes* asks for>
```

## Confirmations

What matched: the departure in phase 1 holds. The phase replaced *A label
names what it turns off, not where it ends* with *A label names no
destination, and its description says what it turns off*
(`skills/implement/orchestration.md:286-291`). The owner named the four
answers as modes (issue #1459 body, *The owner's decision*, third bullet),
so no label names what it turns off any more, and the old rule would be
false for all four labels. The phase claimed that what the rule guarded
still holds and is pinned. `tests/behaviour/test_waiver_decided_at_start.py:497-505`
still asserts that the exit's label carries neither "the PR" nor "pull
request" (read). No other file cites the old heading (executed:
`git grep -n -i "what it turns off\|not where it ends\|five things"`, whose
only hit inside the routing domain is the rewritten docstring at
`tests/behaviour/test_waiver_decided_at_start.py:489`).

What matched: four of phase 2's five departures hold as written
(`trail/phases/phase-2.md:42-68`). (1) The paragraph after each README's
list named `automation` as an answer and is in G22's list, so *Scope* item
10 reaches it. The new wording at `README.md:137-141` and
`README.ko.md:140-143` keys the no-stop behaviour to the `Automation` row,
which is how `docs/running/the-run.md:53` keys it (read). (3)
`skills/code-review/orchestration.md:417` names "a default taken where
`routing.md` reads `Automation` `yes`", which is what *Scope* item 10 asks
(read). (4) The settle's sentence that a settle's commit or a durations
refresh carries the trailer with no route chosen
(`skills/settle/SKILL.md:212-213`) agrees with frame G8 (read). (5) The
comment at `tests/text/test_the_direct_answer_owes_the_sealers_record.py:43-44`
gives the reason the frame's *Alternatives considered* gives for keeping the
names (read). Departure (2), the opening paragraph, holds only in part:
finding 1.

What matched: the template and the skill disagree, which was the question
this round was asked to judge. See finding 2.

What matched: read as a person deciding how to answer, both READMEs list the
four answers in the owner's order, say which answer is marked, and say what
`direct` gives up (`README.md:118-132`, `README.ko.md:121-136`). The two
editions say the same thing line for line. The one sentence that misleads
that person is finding 1.

What matched: *Scope* items 1 to 12 are each built at the target (read
against `git diff dfd0c995 91421710`). Question 1's table holds `agentic`,
`complete`, `manual` and `direct` in that order. The `complete` cell is the
old `automation` cell word for word. The `direct` cell is G2's sentence.
The mark goes to `agentic` (`skills/implement/orchestration.md:279-308`).
*Under agentic* states the four signals for `direct`, each row's choice,
the three combinations that do not stand, where the choice is written, the
raise-never-lower rule and what keeps a wrong choice visible (`:515-594`).
`agents/sealer.md:103-108` and `skills/settle/SKILL.md:208-217` hold the
sentences of *Scope* items 5 and 6. Every row of `## Removes` is gone from
the tree, except the policy-root sentences the four `## Rule changes` items
rewrite at the settle.

What matched: the old-label census in `trail/phases/phase-2.md:70-87` is
whole for its three commands. This round ran the same three greps at the
target and got the same remaining lines (executed): the policy root at
`docs/releasing/release-checklist.md:72` and
`docs/running/the-review-and-parity-arms.md:53`, `:54`, `:61`; history notes
at `tests/behaviour/test_waiver_decided_at_start.py:50`, `:379`, `:495`,
`tests/text/test_review_axes.py:254`,
`tests/text/test_the_direct_answer_owes_the_sealers_record.py:43`, `:89`;
and the row name and trailer value. This round also ran
`git grep -n -i "three answers\|two of its three\|first two options\|third answer\|three options"`.
In the routing domain it found only `the-review-and-parity-arms.md:54`, which
a rule change rewrites, and the #911 history comment at
`tests/text/test_review_axes.py:252`. The ladder class (G21), searched with
`git grep -n -i "ladder"` over `docs`, `agents`, `skills`, `templates`,
`README.md`, `README.ko.md` and `CONTRIBUTING.md`, holds no remaining
statement that the ladder alone decides the frame. That includes the
sentence phase 1 added at `skills/implement/orchestration.md:600-602`.

What matched: each `from` text in `frame/design.md` `## Rule changes`
stands in its file at the target, with whitespace collapsed (executed:
`python3 -I` reading the four files). `seal rules --check` exits 0
(executed).

What matched: `pr.md`'s eight quotes stand word for word at their sources:
the first seven in `changelog.md` at the items named, the eighth in
`gaps.md` *Not verified*, the first row (read). The changelog's Source URL
uses the repository path that the 23 earlier fragments and `CHANGELOG.md`
use (executed: `git grep -h -o`).

What matched: the new case
`#test_question_1_lists_the_four_modes_in_the_owners_order` covers the
labels' order and the `agentic` cell's naming of `direct`, and no case in
its group covers either. Its group pins only the count (`:386`) and finds
the exit by its label (`:497`). `seal layout --pairs` prints no pair for
the four test files the diff changes beyond pre-existing pairs in
`tests/lib/test_routing.py` that the diff does not touch (executed).
Phase 1's seen-red claims for the ceiling and order assertions match what
the assertions read (read: `tests/behaviour/test_waiver_decided_at_start.py:523-539` and
`:415-431`).

What matched: no case in the diff holds a fact the frame does not state.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate (full suite, ruff check, ruff format check) at the target. This round ran only the modules below, so the suite is `unverified`. | `seal/config.md` `Broad gate` row | the orchestrator, by its broad run before the sealer |
| Whether an orchestrator that was answered `agentic` chooses as *Under agentic* guides, and whether a sealer and a settle read chosen routes as the new sentences say. Both are behaviour of agents at run time, and no case runs either. | `gaps.md` *Not verified*, rows 1 and 2 | the repository owner, as `gaps.md` names |
| Whether the grounds sentence in a `direct` commit's body survives the merge in a repository whose squash setting takes the pull request body rather than the commit messages. This repository's squash keeps them (read: `git log origin/release/v0.36.0 --first-parent`, `c9c4d475`), so the settle's `git log --grep` finds them here. | `skills/settle/SKILL.md:208-213`, `skills/implement/orchestration.md:571-572` | the repository owner |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_waiver_decided_at_start.py tests/text/test_review_axes.py tests/lib/test_routing.py tests/text/test_the_direct_answer_owes_the_sealers_record.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_both_editions_carry_the_same_folds.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_the_sealer_guarantees.py tests/skills/test_settle.py tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q`, in the clone at `91421710` | exit 0, 410 passed |
| `bin/seal rules --check`, in the clone | exit 0, all 219 check lines in 68 rule files hold |
| `python3 -I` that collapses whitespace in the four files the `## Rule changes` items name and looks for each `from` text | all four found |
| `chain_check.py --baseline release/v0.37.0 --root <the branch worktree> --worktree`, run with both the installed 0.36.0 copy and the tree's copy, before this record | exit 0. It printed the missing round record, gate record and guarantee, and no notice at `frame/design.md` |
| `bin/seal layout --pairs` | no pair touching a case the diff adds or changes |
