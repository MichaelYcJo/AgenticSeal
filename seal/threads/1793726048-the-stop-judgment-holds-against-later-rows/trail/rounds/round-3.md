# Review round 3: 1793726048-the-stop-judgment-holds-against-later-rows

```seal
target: a70991a3c, fixes d7cf65d1d..a70991a3c
```

This verifying round read the diff of the last fixes, `d7cf65d1d..a70991a3c`, in a `git clone --no-local` of the main clone at `a70991a3c`, made in the round's scratch directory and removed before hand-back. The diff holds four commits: the orchestrator's records fix for round 2's finding 2 at `71078b4cb`, the fix pass for round 2's finding 1 at `bffc022d6`, the orchestrator's fold of *Scope* item 3's first point at `a4be575e4`, and round 2's close blocks at `a70991a3c`. `seal/parity.md` is not declared, so the round block holds no `original:` line. `seal/config.md` holds no `Record language` row, so the record is English. The diff adds no test, so *Each new test is read against its group* had nothing to read.

Carried from rounds 1 and 2, not re-established: the location of #1216's record at tag `v0.28.0`, the base ranges of the stop paragraph and the proofer rule, and that `in_corpus` is the helper round 5 of #1216 wrote its finding on. Re-derived this round: every verdict below, the reading of #1216's *Scope* item 1 that finding 1 rests on, and each claim of the spawn prompt named under `## Confirmations`. Round 1's finding 1 stays `deferred frame/design.md ## Rule changes, the orchestrator's fold`, which round 2 confirmed; this round does not write it up again.

This round opens one finding, a `must`, on a `regression:` line. It is in the sentence the fix pass wrote for round 2's finding 1, and the orchestrator's fold copied the same sentence into the frame.

## Findings

### 1. The fix's condition on a moved helper's test reads what the helper does, not what the test asserts, so #1216's round 5 finding is a `should` again and S5 fails

```seal
severity: must
location: `skills/code-review/SKILL.md:136-138`, `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:42`
evidence: read `skills/code-review/SKILL.md:132-141`, `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:42`, `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:75`, `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:116`
regression: round-2#1
```

The unit is the sentence of the `skills/code-review/SKILL.md` *The record* bullet that `bffc022d6` wrote at `:136-138`: "A test of a helper the work moved, or wrote beside its *Scope*, is such a case only where no *Scope* item, acceptance row or `check:` line states what the helper does." The frame, as `frame/plan.md` *Judgments of the run* row 3 routed the fix, defined such a case by what its assertions hold and gave the moved helper's test as an example; the fix put a second condition beside that definition, which reads what the helper does; the defect came from the fix pass's own wording, written after it declined round 2's paste-ready text, and row 4's fold at `a4be575e4` copied that wording into *Scope* item 3's first point (`frame/design.md:42`).

Why it matters: the bullet now has two conditions for one case, and they disagree.

- The definition at `:133-136` looks at the test: such a case is one "whose assertions hold no behaviour that a *Scope* item, an acceptance row or a `check:` line of a rule the diff changes states", and a fact that only a *Grounding* row states does not count.
- The new sentence at `:136-138` looks at the helper: its test is such a case "only where no *Scope* item, acceptance row or `check:` line states what the helper does". It also drops "of a rule the diff changes", so a `check:` line of a rule the diff leaves alone now counts for a helper's test, though the definition says it does not.

The two disagree on the case this work exists for. #1216's *Scope* item 1 (`frame/design.md:43` at `v0.28.0`, read through the `git show` row of `## Probes`, since the file is no longer in the tree) states what `in_corpus` does: "`in_corpus(rel)` (the selection rule of G8 as a predicate on a repository path)", "moved as they stand". Round 5's finding was on `Test_in_corpus`, whose assertions hold the `TOP_FILES` membership and the `.ko.md` exclusion, which G8, a *Grounding* row, states alone. By the definition, that test holds no fact the frame states, so its gap is no `should`. That is S5's *Then* (`frame/design.md:75`) and the claim of the closing paragraph of *Removes* (`:116`): "Under items 1 and 3, round 5's finding is not a `should`". By the new sentence, a *Scope* item states what the helper does, so the test is not such a case. Its gap is then weighed like any gap, and round 5's `should` stands. A *Scope* item that orders a helper's move names the helper and usually says what it is for. So the new sentence takes out of the class nearly every moved helper's test, the case G7 and the changelog fragment's second bullet name as the reason for the bullet. A proofer reads this bullet each round to decide whether a finding opens. Under the plain reading of the new sentence, the work fails its own acceptance row S5, so this is a `must`.

Claimed (the fix pass's close of round 2's finding 1): round 2's "such as a test of a helper the work moved" still listed that test under the definition without its condition, so the pass wrote the condition in its own words. Round 2's case holds now: a moved helper whose behaviour an acceptance row states, with a test whose assertions hold that behaviour, is not such a case under either sentence. This round confirms that close below. The condition the pass wrote is a new defect beside it, so this finding is a `regression:` and not a `reopens:`. Claimed: the changelog fragment and `agents/proofer.md:139-141` state no example and needed no change. Read: both hold. The changelog's bullet and its second *Process changes* row state the definition alone, and the proofer rule cites the bullet.

The statements of the condition, listed by taking apart each file that states the definition (the bullet, *Scope* item 3's first point, the changelog fragment, `agents/proofer.md:139-141`, S5, and `frame/plan.md` *Judgments of the run*): only the bullet and *Scope* item 3's first point state the helper condition. Row 4 of *Judgments of the run* records the fold that wrote it, and it stays true as a record of that act. The fix writes the helper's test as a case weighed by its assertions, and it says that a *Scope* item that only names the helper, orders its move or cites a *Grounding* row for its rule states no behaviour. That keeps S5 one way: #1216's *Scope* item 1 names `in_corpus`, orders its move and cites G8. The bullet's `:136-138` becomes four lines, and `:139` onward stays as written:

```markdown
  does not count. A test of a helper the work moved, or wrote beside its
  *Scope*, is weighed by its assertions as any case is, and a *Scope* item
  that only names the helper, orders its move or cites a *Grounding* row
  for what it does states no behaviour of it. A parameter in such a case
```

*Scope* item 3's first point, at `frame/design.md:42`, takes the same sentence. That cell is the orchestrator's to fold, as row 4 folded it, and the fix pass owes it with the bullet:

```markdown
   1. A case that holds no fact the frame states is weighed by what the release ships without the fix. Such a case is one whose assertions hold no behaviour that a *Scope* item, an acceptance row or a `check:` line of a rule the diff changes states; a fact that only a *Grounding* row states does not count. A test of a helper the work moved or wrote beside its *Scope* is weighed by its assertions as any case is, and a *Scope* item that only names the helper, orders its move or cites a *Grounding* row for what it does states no behaviour of it.
```

The four bullet lines are 72 to 74 columns, inside the 88 that `tests/behaviour/test_docs_line_wrap.py` reads, and the fix pass runs that module.

```seal
verdict: fixed 67cac0f00
answer: The finding holds: the condition bffc022d6 wrote read what the helper does and dropped "of a rule the diff changes", so it put #1216's `Test_in_corpus` back in the class of weighed gaps. By the route of `frame/plan.md` *Judgments of the run* row 5, this pass did not apply the paste-ready sentences, which keep an example. It removed the helper-test sentence from the bullet of `skills/code-review/SKILL.md` *The record*. The definition and the *Grounding* exclusion stand word for word, and the bullet names no kind of case. The next sentence already opened "A parameter in such a case", which now points back to the definition, and the lines from there to the bullet's end are rewrapped. Against S5, read at `v0.28.0`: #1216's *Scope* item 1 names `in_corpus(rel)` as "the selection rule of G8 as a predicate on a repository path", moved as it stands. G8, a *Grounding* row, alone states the corpus: the tracked `*.md` under `docs/`, `skills/`, `agents/` and `templates/`, the three top files, and no `*.ko.md`. `Test_in_corpus`'s assertions hold that membership and exclusion, a fact only a *Grounding* row states, so under the bullet the case holds no fact the frame states and round 5's gap is no `should`. That reading takes *Scope* item 1's citation of G8 as no statement of the fact, which is what "a fact that only a *Grounding* row states" says, and the proofer reads it there. `tests/behaviour/test_docs_line_wrap.py`, `tests/text/test_the_rules_have_one_owner.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py` and `tests/behaviour/test_a_cited_section_stands_in_its_file.py` exited 0 in one command (executed).
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: the case round 2's finding named now reads one way. Read: `skills/code-review/SKILL.md:136-138` no longer makes every test of a moved helper such a case. A moved helper whose behaviour an acceptance row states, with a test that holds that behaviour, is not such a case under the definition at `:133-136` or under the new sentence. The new sentence's own condition is finding 1, a new defect beside this close and not a reopening of it. Executed: `tests/behaviour/test_docs_line_wrap.py`, `tests/text/test_the_rules_have_one_owner.py` and `tests/text/test_no_passage_is_pasted_into_a_second_file.py` passed, 84 cases, so the rewrap holds the width and the fix moved no pinned sentence. Claimed: "it" became "A parameter in such a case" at `:138`. Read: it did, and the sentence now refers to the case and not to the helper.

```seal
confirms: round-2#2
```
What holds: each *Removes* row of `frame/design.md` now names its `change` by the opening words of its `from`. Read: `:112` names "The homes, with when each fits", the opening of the `from` at `:90`. `:113` names "A round opening nothing that needs a fix", the opening of the `from` at `:96`. `:114` names "No label carries that sentence", the opening of the `from` at `:102`. Each row's *Removes* cell matches the paragraph its entry changes. The counts the finding listed now read three changes and seven points: G13 (`:21`), S1 (`:71`), S7 (`:77`), the closing paragraph of *Removes* (`:116`) and `frame/plan.md:15`. Executed: a search of the work item's frame, changelog, gaps and phase record for "six points", "one change", "first `change`", "second `change`", "that `to`", "rules above" and "the fourth" found no stale count. `trail/phases/phase-1.md`'s count of what the phase built stays true, as round 2 said. Executed: `rule_changes.parse` read three entries, with no error and nothing unread, and `apply_op` placed each in `docs/running/the-run.md` in memory. `## Rule changes` is unchanged by the fix. Claimed (the orchestrator, executed): `chain_check --worktree` read finding 2's close block with no refusal. Executed below: it holds.

```seal
confirms: none
```
What matched: the crafter's and the orchestrator's claims that `chain_check.py --worktree` refuses nothing for the rule changes. Executed in the clone at `a70991a3c`: `python3 skills/code-review/scripts/chain_check.py --baseline 5005355d8 --root . --worktree` exited 0. It printed no rule-change refusal, no pin notice and no copy notice. Its lines name the verifying round owed for round 2's finding 1 and for `bffc022d6`, which this record answers, and the gate record and guarantee not yet written. So no notice at a line of `frame/design.md` was left to weigh.

```seal
confirms: none
```
What matched: S8. Executed: `git diff --stat 5005355d8...HEAD -- ':!seal/'` in the clone lists `agents/proofer.md`, `skills/code-review/SKILL.md`, `skills/code-review/orchestration.md` and `skills/implement/orchestration.md`, and nothing else. The crafter's run of 2567 passed and 10 skipped over the modules that name the skill was not repeated. This round's three modules are named above.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the full suite passes at `a70991a3c`. This round ran three modules, and the crafter's wider run is its claim | the repository's `Broad gate` row | the orchestrator, at the broad run |
| Q1: whether a fix that changes no assertion owes no verifying round. The build stands on the default **No**, carried from rounds 1 and 2 | `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/questions.md` | the repository owner |

## Probes

| Command | Result |
|---|---|
| `python3 skills/code-review/scripts/chain_check.py --baseline 5005355d8 --root . --worktree`, in the clone at `a70991a3c` | exit 0; no rule-change refusal, pin notice or copy notice; it names the verifying round owed for round 2's finding 1 and `bffc022d6`, and no gate record or guarantee yet |
| `bin/test tests/behaviour/test_docs_line_wrap.py tests/text/test_the_rules_have_one_owner.py tests/text/test_no_passage_is_pasted_into_a_second_file.py -q`, in the clone | exit 0, 84 passed |
| `python3 -I -c` loading `skills/settle/scripts/rule_changes.py` by path, running `parse` over `frame/design.md` and `apply_op` for each entry over `docs/running/the-run.md` in memory | three entries, no error, nothing unread, each placed; nothing written to disk |
| `git show v0.28.0:seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/frame/design.md`, searched for `in_corpus` | *Scope* item 1 at `:43` names `in_corpus(rel)` as "the selection rule of G8 as a predicate on a repository path", moved as it stands |
| `git grep -n -i -e 'helper the work moved' -e 'states what the helper does' -- tests evals skills agents docs templates` | only `skills/code-review/SKILL.md:136` and `:138`; no case pins the sentence |
| `git diff --stat 5005355d8...HEAD -- ':!seal/'`, in the clone | four files, as S8 names |
