# Review round 1: 1793726048-the-stop-judgment-holds-against-later-rows

```seal
target: fc885205a against release/v0.31.0
```

This round reviewed the branch `5005355d8..fc885205a` in a `git clone --no-local` of the main clone at `fc885205a`, made in the round's scratch directory and removed before hand-back. No earlier round exists, so nothing was carried from one. #1216's round 5 record was opened again at `v0.28.0` (`git show`) rather than taken from the frame's G7. `seal/parity.md` is not declared, so the round block holds no `original:` line. `seal/config.md` holds no `Record language` row, so the record is English. The diff adds no test, so *Each new test is read against its group* had nothing to read, and no case of the kind the new bullet in `skills/code-review/SKILL.md` *The record* weighs stands in the diff.

The implementer's account was read as claims: the spawn prompt's labels, `trail/phases/phase-1.md`, `gaps.md` and the commit messages. Each claim this round could open is answered under `## Confirmations` or in a finding. This round opens four findings, all `should`, and no `must`. Finding 1 disputes a decision of the frame's *Scope* Out. Finding 2 is a reading of the new paragraph that the frame's Out bullet on routes left open.

## Findings

### 1. `docs/running/the-run.md` still calls the three finding rounds the cap that stops a loop, beside the new sentence that they are no cap

```seal
severity: should
location: `docs/running/the-run.md:12-15`, `skills/code-review/orchestration.md:137-138`, `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:62`, `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:84-90`
evidence: read `docs/running/the-run.md:12-15`, `skills/code-review/orchestration.md:133-140`, `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:62`
```

Why it matters: `docs/running/the-run.md:12-15` reads "A round opening nothing that needs a fix does not count toward the cap: the cap stops a loop that is not converging". "Count toward" makes the cap the count of finding rounds, and "stops a loop" makes that count the stop. The new sentence at `skills/code-review/orchestration.md:137-138` says "The three rounds are where the weighing is owed, and they are no cap: no number of rounds decides that a run is excessive." The orchestrator reads both. The section cites *The run* at `:135-136` for the count, and `:13` is that section's first paragraph. So the policy root gives the reading the owner declined (G1), and the skill denies it.

The frame's *Scope* Out (`frame/design.md:62`) keeps `:13` because it "name[s] the weighing point that stays", and says it "stay[s] true". The crafter's rule-12 sample says the same (`trail/phases/phase-1.md`). This round found the claim true of "count toward" and false of "the cap stops a loop". S2's then-clause, "the three rounds read as where the weighing is owed", is the reading `:13` contradicts. The work edits `docs/` only through `## Rule changes` (G13), so the fix is a second `change` in that section:

```markdown
- change
  file: docs/running/the-run.md
  section: The run
  from: A round opening nothing that needs a fix does not count toward the cap: the cap stops a loop that is not converging, and such a round is the loop having converged.
  to: A round opening nothing that needs a fix does not count toward the three finding rounds: they mark where a loop that is not converging is weighed, and such a round is the loop having converged.
```

Where the snippet stops: `agents/proofer.md:132` ("a round told the run is capped") and `docs/forms/the-round-record.md:105` ("files at the cap") use the word for the stop row, not for the count, so they do not contradict `:137-138`. The fix pass weighs `agents/proofer.md:132`, because this branch already edits that file. The *Scope* Out bullet at `frame/design.md:62` goes stale with the fix, and the fix pass owes it too. `README.md:92` is #1102's (G18). The fix pass runs S7's command over the new `to` for copy notices.

```seal
verdict: deferred frame/design.md ## Rule changes, the orchestrator's fold
answer: The finding holds: `docs/running/the-run.md:13` makes the count the cap that stops a loop, and `skills/code-review/orchestration.md:137-138` says the three rounds are no cap. This pass edits nothing in `docs/` (G13) and does not write `frame/design.md`, so the repair is a second `change` in `## Rule changes`, handed to the orchestrator to fold. Its `from` is the sentence at `:12-15` as HEAD holds it. Its `to` is written in this pass's own words so that it also says the rounds are no cap: "A round opening nothing that needs a fix does not count toward the three finding rounds, which mark where the orchestrator weighs a loop that is not converging and are no cap: such a round is the loop having converged." In a scratch copy of the design, `rule_changes.py` parsed it and placed it in `docs/running/the-run.md`, and `chain_check.py#pins_and_copies_in` printed no pin and no copy notice (executed). The same reading named a planted 15-word copy. `agents/proofer.md:132` stays as it is. There "capped" is the word of the `chain: capped` label and of `docs/releasing/branch-and-release.md:91` for a run the orchestrator stopped, not for the count, and a round spawned after a stop row still reports what it finds at its severity. The *Scope* Out bullet at `frame/design.md:62` goes stale with the fold, and the hand-back names it.
```

### 2. After a stop row, a `should` that carries a `regression:` line can still take the framer's route, and the redesign that route makes ends the stop

```seal
severity: should
location: `skills/code-review/orchestration.md:164-180`, `skills/code-review/orchestration.md:224-234`, `docs/running/the-run.md:29-30`, `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:84-90`
evidence: executed `sed -n 164,180p skills/code-review/orchestration.md | grep -c -i -e route -e regression -e framer`, `sed -n 222,240p skills/code-review/orchestration.md | grep -c -i -e excessive -e 'stop row' -e must`
```

Why it matters: the new paragraph (`skills/code-review/orchestration.md:164-180`) says that after a stop row every finding but a `must` takes rung 2, 3 or 4 or a fix confined to the records, and that "A later row spends no round on a finding that is not a `must`". It also says "Only a design change ends the stop". The route section routes the round on the regression sentence (`:227-228`), and its table sends two cases to the framer with "no fix pass" (`:232`, `:234`). `docs/running/the-run.md:29-30` says the orchestrator routes "at any round of the run". Neither text names a stop row: the two greps printed `0` and `0`.

The framer's route spawns no fix pass, and the finding's close reads `deferred the frame` (`:244`). So the route fits the stop paragraph's literal words. The reframe it makes is a design change, which the same paragraph says ends the stop and restarts the count. #1216 had this shape: rounds 7 to 9 each carried a `regression:` line in `Test_in_corpus` (G7). From round 8 on, the third route row (`:234`, "the unit already had a regression routed to a fix pass in this run") sends that unit to the framer. So S1's then-clause, that "the rows after rounds 7 and 9 have no ground the section leaves open", does not hold: a route row is that ground. The frame's Out bullet (`frame/design.md:64`) says item 1 binds only whether a round is spent, and that "a regression that is a `must` still takes its route". That implies a regression that is not a `must` takes no route after a stop, but no shipped sentence says so. An orchestrator acts on this text at every round that carries a `regression:` line, so the sentence it lacks is a `should`.

The fix puts one sentence after "whatever document it cites." (`:171`):

```markdown
A finding that is not a `must` takes such a home whether or not it carries a
`regression:` line: from the stop row on, *A regression is routed by
comparing the fix with the frame* routes a `must` alone, so no later row
sends another finding to a fix pass or to the framer, whose redesign would
end the stop.
```

It also changes the route section's lead at `:227-228`:

```markdown
the frame says, what the fix did and where the defect came from. You route
the round on that sentence (`docs/running/the-run.md` *The run*), and once a
row has judged the run excessive you route a `must` alone, by the paragraph
opening **A row that judges the run excessive binds every row after it**:
```

It adds a `change` to `frame/design.md` `## Rule changes` for the policy root's statement:

```markdown
- change
  file: docs/running/the-run.md
  section: The run
  from: No label carries that sentence, and the orchestrator routes the round on it, at any round of the run.
  to: No label carries that sentence, and the orchestrator routes the round on it, at any round of the run, except that once the run has been judged excessive in a row of `frame/plan.md` *Judgments of the run* it routes a `must` alone, and every other regression takes a home (`skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*).
```

Where the snippets stop: the *Scope* Out bullet at `frame/design.md:64` and S1 at `:70` state the old reach, and the fix pass owes them. `skills/implement/acts.md`'s row for the route section stays true. The fix pass runs S7's command, because the two `to` values and the new sentences must share no run of 15 words.

```seal
verdict: fixed 89480ded9
answer: The finding holds, and the fix is in this pass's own words at both coordinates. In the stop paragraph, the sentence on a finding with a `regression:` line stands after the sentence naming the drain row and rung 1, not after "whatever document it cites.", because placed there it would part "those documents" from the sentence it refers to. It says that from the stop row on you route a `must` alone, and every other regression takes a home that costs no round, never a fix pass and never the framer, whose redesign would end the stop. The route section's lead says that once a row has judged the run excessive, only a `must` takes a route below, and any other regression takes a home by the stop paragraph. `docs/running/the-run.md:29-30` is handed to the orchestrator as a third `change` to fold, from "No label carries that sentence, and the orchestrator routes the round on it, at any round of the run." to the same sentence followed by ", except that once a row of `frame/plan.md` *Judgments of the run* has judged the run excessive, only a `must` takes a route, and every other regression takes a home that costs no round", with a citation of `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*. The scratch reading printed no refusal and no notice for it (executed). The *Scope* Out bullet at `frame/design.md:64` and S1 at `:70` state the old reach, and the hand-back names them.
```

### 3. The drain row's new clause does only a `must` now, while the paragraph it cites makes a fix confined to the work item's records one of the homes

```seal
severity: should
location: `skills/implement/orchestration.md:480`, `skills/code-review/orchestration.md:167-171`
evidence: read `skills/implement/orchestration.md:480`, `skills/code-review/orchestration.md:164-171`, `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:89-90`
```

Why it matters: the drain row's new clause (`skills/implement/orchestration.md:480`) reads "only a `must` is done now, and every other item takes a home that costs no round, as `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* states". The paragraph it cites names two homes for a finding that is not a `must`: rung 2, 3 or 4, "or a fix confined to the work item's records, which the sealer reads" (`:167-171`). A records-only fix done at the drain is done now. So the row answers twice for an item that is not a `must` and whose fix touches only the records: not done now by its own words, done now by the home it cites. The design's `to` (`frame/design.md:90`) keeps both on the first rung, "only a `must` and a fix confined to the work item's records", so the drain row is the statement that disagrees. The orchestrator acts on this row at the drain.

```markdown
| Doable within this pull request | done now, by the party that builds the work item, and reviewed by a verifying round before the broad run, unless every finding it closes is located in the work item's records and it touched nothing else. Once a row of `frame/plan.md` *Judgments of the run* judges the run excessive, only a `must`, or an item whose fix is confined to the work item's records, is done now, and every other item takes a home that costs no round, as `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* states |
```

Where the snippet stops: *Scope* item 2 (`frame/design.md:39`) and S4 (`:73`) state "only a `must` is done now" too. They are the frame's records, and the fix pass weighs them.

```seal
verdict: fixed 89480ded9
answer: The finding holds. The paste-ready row was read against `skills/code-review/orchestration.md:164-171` and the design's `to` at `frame/design.md:90`, which both keep a fix confined to the work item's records after a stop, and it was applied as given. The row's first clause already says that such a fix owes no verifying round, so the two clauses agree. *Scope* item 2 and S4 still say "only a `must` is done now", and the hand-back names them for the orchestrator to fold.
```

### 4. The new bullet tests whether a *Scope* item names the case, so "a case that holds no fact the frame states" reads two ways on the case S5 cites

```seal
severity: should
location: `skills/code-review/SKILL.md:132-136`, `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:41`, `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:74`
evidence: executed `git show v0.28.0:seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/trail/rounds/round-5.md`
```

Why it matters: the bullet's label is "a case that holds no fact the frame states". Its definition is "one that no *Scope* item, no acceptance row and no `check:` line of a rule the diff changes names" (`skills/code-review/SKILL.md:132-136`). The object of "names" is the case. A *Scope* item names behaviour and seldom names a test. Read that way, almost every case qualifies, and the closing exception ("a behaviour the diff changed that no case then holds") carries the whole rule. Read as "names the fact the case holds", the bullet turns on which parts of the frame count, and it does not say.

S5 is that instance. #1216's round 5 grounds its finding on "a corpus boundary of G8 that no case keeps", and quotes that design's G8 (`frame/design.md:14` there), a *Grounding* row. By the label, `Test_in_corpus` holds a fact the frame states. By the definition, no *Scope* item named it. S5 (`frame/design.md:74`) takes the second reading, and the issue's third *Done when* bullet ("a test of a helper outside the design's scope") supports it. The bullet still does not say that a *Grounding* row does not count. A proofer acts on this sentence to decide whether a finding opens, so it is a `should`.

The fix replaces the bullet's first three sentences and keeps the rest as written:

```markdown
- A case that holds no fact the frame states is weighed by what the release
  ships without the fix. Such a case is one whose assertions hold no
  behaviour that a *Scope* item, an acceptance row or a `check:` line of a
  rule the diff changes states. A fact that only a *Grounding* row states
  does not count. A test of a helper the work moved, or wrote beside its
  *Scope*, is such a case. A
  parameter in it that pins nothing, a guard in it of code the diff did not
```

Where the snippet stops: `agents/proofer.md:139-140` uses the label and cites the bullet, so it needs no change. *Scope* item 3's first point (`frame/design.md:41`) states the same definition, and the fix pass weighs it as the frame's record.

```seal
verdict: fixed 89480ded9
answer: The finding holds. The paste-ready sentences were read against *Scope* item 3's first point and S5. The frame lists only *Scope* items, acceptance rows and `check:` lines, and S5 takes round 5's case as one that holds no fact the frame states although its grounds quoted a *Grounding* row. So excluding a fact that only a *Grounding* row states is the frame's reading made explicit, and the sentences were applied as given, with the bullet's following lines rewrapped to the 88-column limit `tests/behaviour/test_docs_line_wrap.py` reads (executed). `agents/proofer.md:139-141` cites the bullet and needed no change. *Scope* item 3's first point still states the old definition, and the hand-back names it.
```

## Confirmations

```seal
confirms: none
```
What matched: S8. Claimed (`trail/phases/phase-1.md`): the diff outside `seal/` lists four files. Executed: `git diff --stat 5005355d8...HEAD -- ':!seal/'` listed `agents/proofer.md`, `skills/code-review/SKILL.md`, `skills/code-review/orchestration.md` and `skills/implement/orchestration.md`, 47 insertions and 3 deletions. `skills/core/SKILL.md`, `skills/code-review/scripts/chain_check.py` and `docs/` are not in it, so the build wrote nothing for Q1, and its default **No** stands as `frame/questions.md` states.

```seal
confirms: none
```
What matched: S2 and S9. Executed in the clone: `grep -c 'three finding rounds by default' docs/running/the-run.md` printed `1`. `bin/test` over the five modules S9 names passed, 116 cases. The crafter's 103-module run was not repeated. It is a subset, not the suite, and the phase record names how its module list was built. The broad gate is the orchestrator's (contract rule 2).

```seal
confirms: none
```
What matched: the orchestrator's fold (`frame/plan.md` *Judgments of the run* row 1). Executed: `git show 5005355d8:skills/code-review/orchestration.md` line 154 is "and commit the close blocks of that step together.", and `git show 5005355d8:agents/proofer.md` line 140 is the rule's last line. So `:133-154` and `:136-140` are the base ranges, and `fc885205a` touched only `frame/design.md` and `frame/plan.md`.

```seal
confirms: none
```
What matched: the decision to add no case, which the crafter asked this round to weigh. Claimed: three `seal mutate` mutants over the new sentences survived, by the frame's choice. Read: `skills/settle/rule-changes.md:79` says "A rule no case holds carries no check line, and review reads it". `skills/verify/SKILL.md` *The narrow command still has to be able to fail* gives a prose-only change "no seal to earn here". `docs/running/what-a-script-gates.md` *The checks* lets a case pin "a fact a reader acts on" and sends away a case that pins wording, and nothing there makes such a case owed. Contract rule 15 binds a case that is added, and none is. So the survivors are a correct report of a rule that review reads, and they open no `Regression test` row `should`. The new sentences were read for meaning, which gives findings 1 to 4.

```seal
confirms: none
```
What matched: S3 and S6, read. S3: `skills/code-review/orchestration.md:166-167` gives a `must` its fix pass and its verifying round from the stop row on. S6: `agents/proofer.md:139-141` keeps the group rule's first sentence and sends a case that holds no fact the frame states to `skills/code-review/SKILL.md` *The record* without restating it. S1, S4 and S5 do not hold as written (findings 2, 3 and 4).

```seal
confirms: none
```
What matched: the crafter's rule-12 sample is labelled a sample, names its `git grep` terms, and says where its open part stands (`trail/phases/phase-1.md`, the last section). Findings 1 and 2 stand in that open part, or in a judgment the sample made. The method is reported honestly, and no whole list is claimed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the full suite passes at `fc885205a`. This round ran five modules, and the crafter ran 103 | the repository's `Broad gate` row | the orchestrator, at the broad run |
| Q1: whether a fix that changes no assertion owes no verifying round. The build stands on the default **No** and writes nothing for it | `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/questions.md` | the repository owner |
| The design's `to` says "The row the orchestrator writes in that table", and "that table" stands after a sentence that names both *Judgments of the run* and the homes' rungs. The reader can resolve it, since no row is written in the rungs' table, so this round opens no finding | `seal/threads/1793726048-the-stop-judgment-holds-against-later-rows/frame/design.md:90` | the fix pass, where finding 1 or 2 edits `## Rule changes` |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_chain_hooks_hardening.py tests/text/test_the_verifying_round_is_bounded_not_cheapest.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_docs_line_wrap.py -q`, in the clone | exit 0, 116 passed |
| `git diff --stat 5005355d8...HEAD -- ':!seal/'` | four files, as S8 states |
| `grep -c 'three finding rounds by default' docs/running/the-run.md` | `1` |
| `sed -n 164,180p skills/code-review/orchestration.md \| grep -c -i -e route -e regression -e framer` | `0`: the stop paragraph names no route |
| `sed -n 222,240p skills/code-review/orchestration.md \| grep -c -i -e excessive -e 'stop row' -e must` | `0`: the route section names no stop |
| `git show v0.28.0:seal/threads/1793577579-the-pull-request-names-each-pin-a-rule-change-breaks/trail/rounds/round-5.md` | round 5's finding grounds itself on #1216's G8 corpus boundary |
