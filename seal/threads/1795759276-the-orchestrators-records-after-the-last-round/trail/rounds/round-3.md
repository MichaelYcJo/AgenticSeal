# Review round 3: 1795759276-the-orchestrators-records-after-the-last-round

```seal
target: c33b7d32c, fixes f9d2756dd..c33b7d32c
```

This is a verifying round over the fix range `f9d2756dd..c33b7d32c`, against the base `origin/release/v0.39.3`, read in a `git clone --no-local` of the repository at `c33b7d32c`. The range holds seven commits after round 2's record `32e577e11`:

- `ef2c72eaf`, the framer's fold of *Scope* item 4, committed with the orchestrator's rows;
- `cec86a832`, the orchestrator's rows and `pr.md`;
- `9833b5b51`, `553a8ee9d` and `9edade97d`, the crafter's fix pass;
- the two close commits `b798d6418` and `c33b7d32c`.

It changes `skills/implement/orchestration.md` and the work item's records alone (executed, `git diff --stat f9d2756dd..c33b7d32c`). `seal/parity.json` is not declared. The round read `routing.md`, the three frame files, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and the two earlier round records whole at the target. No `pr.<lang>.md` stands.

Carried from round 1 and not re-derived: where `chain_check.py#follows` and the new case stand, and the case's mutation result. Neither file changed in this range, or in round 2's. Re-derived here: every verdict below.

The range changes no code. So the code axes have no new path, as in round 2. The round walked the four record axes, and checked each row of `frame/plan.md` *Judgments of the run* against the rule at `skills/implement/orchestration.md:135-154` as it now stands.

## Findings

### 1. The row rule now binds only a row that names a commit, so a row's inventory of a fold it names by no commit escapes, and the routing row of `round-1#2` holds one that is false

```seal
severity: should
location: `skills/implement/orchestration.md:135-143`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/design.md:52`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md:25`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md:66`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/changelog.md:4`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/changelog.md:11`
evidence: executed `git grep -n -i -F -e 'names a commit, it names it' -e 'where a row names a commit' -e 'names a commit only as a coordinate' -e 'Where it names a commit' -- . ':!seal/threads/*/trail/rounds'` (prints `skills/implement/orchestration.md:136`, `frame/design.md:52`, `frame/plan.md:25`, `changelog.md:4` and `changelog.md:11`, and a comment in `evals/scripts/rule_cases.py:790` on another subject), `git show --format= --word-diff=plain ef2c72eaf -- seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/design.md`; read `skills/implement/orchestration.md:126-156`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/design.md:24`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/design.md:51-53`
regression: round-2#2
```

Why it matters: the unit is the sentence at `skills/implement/orchestration.md:135-143`. The fix pass `9833b5b51` rewrote it for round 2's finding 2, and it now opens "Where a row of *Judgments of the run* ... names a commit, it names it as a coordinate and gives no inventory of what that commit changed". The frame's *Scope* item 4, first bullet (`frame/design.md:52`), says "Where it names a commit". That is round 2's paste-ready text, which the framer folded as given at `ef2c72eaf`. The fix built it as written. The defect came from that paste-ready text, which made the ban hold only where a commit is named.

The paragraph's own fold row is the case this misses. By `:130-132` the orchestrator writes that row "before it sends", so the fold's commit does not exist yet and the row cannot name it. A row written then that counts or labels what the fold will change names no commit, and the ban does not reach it. That is the instance G12 records (`frame/design.md:24`): a row "written before its fold and committed with it, said the fold narrowed only". A row that names a fold only as "the fold" escapes in the same way after the fold exists.

This run already holds such a row. The routing row of `round-1#2` (`frame/plan.md:66`) gives as its grounds "the fold narrows one sentence of the item and moves no scope and no phase". The fold is `ef2c72eaf`, and the row does not name it. It is a count and a word for the kind of change, the inventory `:137-139` lists. It is also false. The commit rewrote *Scope* item 4's title and both its bullets (executed, the word diff above). The first bullet gained a sentence on a row about a change, and the second widened the parties that may name a defect. So nothing about the fold was only a narrowing of one sentence.

The second sentence of `:139-143` licenses a route row's grounds to state "what the change means". The change it routes is the fix `f0a46ad0c`, not the fold that answers it. A count of the fold's sentences is neither.

Under the route table, this is the second regression of this unit routed in the run. Its third row (`skills/code-review/orchestration.md:278`) reads that as the signal that the frame is wrong. The route is the orchestrator's call.

The search is on the sentence's words, so the list is a sample under contract rules 12 and 19. The snippets cover each line it printed:

- the skill sentence;
- *Scope* item 4's first bullet and *Alternatives considered* row 7, which are frame statements;
- the routing row, which is the orchestrator's, and which a round's finding may now correct by `:150-154`;
- `changelog.md:4` and `:11`, which take the same clause as the skill sentence: "names a commit only as a coordinate and gives no inventory of a change, a commit's or a fold's still to come".

For `skills/implement/orchestration.md`, replacing the two sentences from "Where a row of *Judgments of the run*" to "the document it judges against.":

```markdown
settle reads the row. A row of *Judgments of the run*, this one or any
other the orchestrator writes, names a commit only as a coordinate and
gives no inventory of a change, a commit's or a fold's still to come: no
number of lines, no list of the sentences or items a fold rewrote or will
rewrite and no word for the kind of change a fold made or will make,
because `git show <commit>` is that account. A row whose judgment is about
a change, such as a regression's route
(`skills/code-review/orchestration.md` *A regression is routed by comparing
the fix with the frame*) or why the title takes its prefix, states as its
grounds what the change means against the document it judges against, and
no inventory of it. The
orchestrator resumes the work item's framer while that session still
```

For `frame/design.md` *Scope* item 4, its first bullet:

```markdown
   - A row of *Judgments of the run* states the judgment, its grounds and the document judged against. It names a commit only as a coordinate and gives no inventory of a change, a commit's or a fold's still to come: no number of lines, no list of the sentences or items a fold rewrote or will rewrite, no word for the kind of change a fold made or will make. `git show <commit>` is that account. A row whose judgment is about a change, such as a regression's route or the title's prefix, states as its grounds what the change means against the document it judges against, and no inventory of it.
```

For `frame/plan.md:25`, row 7's approach cell: "where a row names a commit it gives no inventory of what that commit changed" becomes "a row names a commit only as a coordinate and gives no inventory of a change, a commit's or a fold's still to come".

For `frame/plan.md:66`, the routing row's grounds:

```markdown
The fix built *Scope* item 4 as written and the defect stands, the case the route table gives to the framer's route; the defect lies in how far the item's rule reached and not in the design *Alternatives considered* row 7 chose, so a redesign would rebuild the design the fold keeps, and the run's count is kept, not restarted
```

```seal
verdict: deferred the frame
answer: Regression `round-2#2`, the second regression of `frame/design.md` *Scope* item 4 in this run, sent the work item back by the framer's route (`frame/plan.md` *Judgments of the run*, the row opening "Round 3's findings 1 and 2").
```

### 2. `## Removes` says the work adds one rule sentence to a skill, where the fold's *Scope* item 4 and the prefix row now give it several

```seal
severity: should
location: `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/design.md:102`
evidence: executed `git grep -n -F -e 'one rule sentence' -e 'sentences that apply' -- seal/threads/1795759276-the-orchestrators-records-after-the-last-round ':!*/trail/rounds/*'` (prints `frame/design.md:102`, `frame/plan.md:61` and `pr.md:4`); read `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/design.md:51-53`, `skills/implement/orchestration.md:135-154`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/trail/rounds/round-2.md:40`
regression: round-2#2
```

Why it matters: `frame/design.md:102` reads "It adds one rule sentence to a skill, and to the policy root the decision that kept the rows as text with a citation of that sentence. What the sentence removes is content". The fold `ef2c72eaf`, made for round 2's finding 2, rewrote this paragraph ("account" became "inventory") and left the count. The same fold gave *Scope* item 4's first bullet a second sentence, on a row about a change. `skills/implement/orchestration.md:139-143` builds that sentence. So the paragraph now gains two rule sentences beside the rewritten one on a fold's row.

The prefix row says "sentences" (`frame/plan.md:61`, quoted at `pr.md:4`). Round 2's close of its finding 1 (`round-2.md:40`) made that word plural for this reason. So two records the sealer reads state different counts of the same diff.

This is the count contract rule 19 refuses. It was stated of the diff, and a later change made it false without editing it. The frame sentence follows the fix of `round-2#2`: the frame changed, and the paragraph kept the count. The paragraph is a frame file, so the change is the framer's.

```markdown
The work adds no gate, check, hook, CI step, line grammar, label or mark, so it owes no removal in return. It adds to a skill the rule sentences of *Scope* item 4, and to the policy root the decision that kept the rows as text with a citation of them. What they remove is content: the inventory of a commit that a judgment row held.
```

```seal
verdict: deferred the frame
answer: Regression `round-2#2`, the second regression of `frame/design.md` *Scope* item 4 in this run, sent the work item back by the framer's route (`frame/plan.md` *Judgments of the run*, the row opening "Round 3's findings 1 and 2").
```


## Confirmations

```seal
confirms: round-2#1
```
What holds: the prefix row's grounds (`frame/plan.md:61`) no longer say the new sentence follows from step 1. They rest on the core's rule that a fact has one source, cite row 7, and say that row 12 rejects step 1 as the whole answer. `pr.md:3` quotes the row's first cell and `pr.md:4` its grounds, and both quotes stand in the row word for word. `seal pr-body` composed the body at the target (executed, exit 0). The prefix stays `fix:`, and that choice is the orchestrator's.

```seal
confirms: round-2#2
```
What holds: the sentence at `skills/implement/orchestration.md:135-143` no longer forbids a regression route row or the prefix row to state what a change means. It names both and cites `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame*. `tests/behaviour/test_a_cited_section_stands_in_its_file.py` passes with that citation, and `tests/behaviour/test_docs_line_wrap.py` passes over the rewrap `553a8ee9d` (executed). How far the narrowed sentence now reaches is finding 1, and the count it left in `## Removes` is finding 2.

```seal
confirms: round-2#3
```
What holds: `skills/implement/orchestration.md:150-154` and *Scope* item 4's second bullet (`frame/design.md:53`) name the framer's hand-back, a round's finding and the sealer's verdict as what may name a defect in a fold's row, and the framer's rejection beside them. `changelog.md:4` says the same (read).

```seal
confirms: round-2#4
```
What holds: the second row (`frame/plan.md:60`) is byte for byte its text at `471dc15b9` (executed, `cmp` of the two lines, exit 0). The fourth row (`:62`) no longer carries the clause on the second row's grounds. The row at `:63` records the later judgment on the spawn, with the paragraph opening **The framer writes a decision's fold** as its grounds and its document. That paragraph is the one the judgment rests on.

What matched, the routing row the orchestrator asked this round to weigh. The row for `round-1#2` (`frame/plan.md:66`) departs from the framer's route that the table's first row (`skills/code-review/orchestration.md:276`) gives to a fix that built the frame as written. The route's steps are at `:286-290`: the open findings close `deferred the frame`, the framer is spawned with the round records, a `Reframed` line follows the mark, and the count starts again. The orchestrator took the framer's fold, then a fix pass. It closed findings 2 and 3 `fixed`, wrote no `Reframed` line, and kept the count.

This round judges the departure sound on four facts.

- **The framer still judged the frame change.** `ef2c72eaf` carries the framer's attribution line, and the route exists so that the framer writes the frame (`skills/core/SKILL.md` *Each agent judges its own target, independently of the others*).
- **The closes stay open to a round.** Closing `fixed` rather than `deferred the frame` makes a round owe the closes. `chain_check.py --worktree` names findings 2 and 3 of round 2 and `9833b5b51` as owed a verifying round, which this record is (executed).
- **No check needs the missing line.** The check's frame arm refuses nothing for the absent `Reframed` line (executed).
- **The kept count is the stricter choice.** A kept count reaches the stop point no later than a restarted one.

The row writes its departure and its grounds where the settle reads them (`docs/running/the-run.md:54`). The table names no route for a frame sentence that a fold mends without a redesign, and that row is how a settle would meet the case. One clause of the row's grounds is a false inventory of the fold, and that is finding 1.

What matched: the routing rows for `round-1#1` (`:64`) and `round-1#4` (`:65`) each give the sentence the table's second row reads, "applied ... as given" and "which the frame does not say", and route an ordinary fix. The row for round 2's finding 3 (`:67`) cites the paragraph that gives a round finding on a frame sentence to the framer's fold. `cec86a832` changed these rows after the fold on the framer's hand-back, which `:150-152` permits (read).

What matched: the range adds no test, so no new case is read against its group. `gaps.md` is unchanged in the range.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at the target, labelled `unverified` (contract rule 2) | the branch at `c33b7d32c` | the orchestrator, by `seal gate --base origin/release/v0.39.3 --record seal/threads/1795759276-the-orchestrators-records-after-the-last-round` after the rounds settle |
| The route of finding 1, the second regression of the sentence at `skills/implement/orchestration.md:135-143` routed in this run, which `skills/code-review/orchestration.md:278` reads as the signal for the framer's route | `frame/plan.md` *Judgments of the run* | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test -q -p no:xdist tests/text/test_the_rules_have_one_owner.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_waiver_decided_at_start.py tests/behaviour/test_docs_line_wrap.py tests/skills/test_chain_check.py -k 'follow_up or code_commit_after_the_last_record or Test_follows or not chain_check'` in the round's clone at `c33b7d32c` | exit 0, 221 passed, 259 deselected |
| `bin/seal pr-body --body <scratch>/body.md seal/threads/1795759276-the-orchestrators-records-after-the-last-round` in the clone | exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.39.3 --root . --worktree` in the clone | exit 0; it names findings 2 and 3 of round 2 and `9833b5b51` as owed a verifying round, which this record is, and the gate record and guarantee as not yet written; no notice at `frame/design.md` and no refusal from the frame arm |
| `sed -n 60p` of `frame/plan.md` at the target against the same line at `471dc15b9`, through `cmp` | exit 0 |
