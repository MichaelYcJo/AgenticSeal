# 1792619289-the-pull-request-check-parses-rule-changes — review round 3

target: d7705fa5, fixes 06e3232f..d7705fa5

This verifying round read the fix diff 06e3232f..d7705fa5 and nothing outside it. The diff holds round 2's record (75e477c7), the fix f31de4a4, and the fix pass's record (d7705fa5). f31de4a4 changes two prose passages: a docstring in `chain_check.py` and a sentence in `skills/settle/SKILL.md`. It changes no code. This round carried from round 2 where the edited set's qualifier stands, in `spec.md` *Scope* item 1 and in `main`'s `if not declarations` return. It did not open those again. Its own verdict was reached on the two rewritten sentences. The owner's direction, `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다*, was the criterion they were read against.

## Findings

None.

## Confirmations

confirms: round-2#1
The fix holds at `skills/code-review/scripts/chain_check.py:16-22` and `skills/settle/SKILL.md:79-82`. Both now name the second set with *Scope* item 1's qualifier, "on a pull request that declares at least one work item". That matches the code, which computes the set only after the declared-nothing return.

The class was checked as well. A `git grep` at d7705fa5 found 16 places, outside the round records, with the words "commits add or". Five are about declarations and not about specs: `chain_check.py:7`, `spec.md:11`, the 0.22.0 changelog, and an earlier work item's changelog and plan. Of the eleven that state this work item's spec set, every one holds the qualifier in the same sentence or under a sentence before it, with one exception. That exception is the docstring of `edited_work_items` (`chain_check.py:1597`), which describes what the function returns.

Read against the owner's three rules, the two sentences hold:

- They use no separator symbol, and they state the qualifier in the same words *Scope* item 1 uses.
- They give no instruction, so no actor or end state is missing.
- In "its own commits", the nearest noun is "work item", while the pull request is the subject the sentence means. Both readings name the same commits, because a declaring pull request's own commits are its work items' commits. So no reader acts differently on either reading.

Executed (`git grep`) and read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at d7705fa5 (the orchestrator reports `tests` run 39689643276 at 06e3232f passed every leg) | the branch at d7705fa5 | the orchestrator, through `broad-gate --base release/v0.22.3 --record seal/specs/1792619289-the-pull-request-check-parses-rule-changes` |
| Whether `--sealing` should judge strictly where no pull request exists yet, carried from round 1 | `skills/code-review/scripts/chain_check.py:1969-1970` | the orchestrator, for the owner |

## Probes

| Command | Result |
|---|---|
| `git grep -n "commits add or change" d7705fa5`, then the same search widened to "commits add or", with the round records left out | 16 places. Five are about declarations. Every place that states the spec set holds the qualifier, except the function docstring named above |
