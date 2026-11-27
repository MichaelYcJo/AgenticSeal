# Review round 4: 1795759276-the-orchestrators-records-after-the-last-round

```seal
target: 9ef37f933, fixes be757f2b7..9ef37f933
```

This round is the first finding round of the redesign that round 3 sent back by the framer's route. It reads the range `be757f2b7..9ef37f933` against the base `origin/release/v0.39.3`, in a `git clone --no-local` of the repository at `9ef37f933`. The range holds six commits:

- `592395799`, the framer's reframe;
- `487a9afcc`, the orchestrator's rewrite of round 2's route row for `round-1#2`;
- `f187056e6`, `b83175868`, `6f9b8f56f` and `9ef37f933`, the crafter's phase 2.

The orchestrator's `bc37193f5`, which routed round 3, comes before `be757f2b7`. Its row is read here with the other rows. The range changes `skills/implement/orchestration.md` and the work item's records alone (executed, `git diff --stat be757f2b7..9ef37f933`). `seal/parity.json` is not declared. The round read `routing.md`, the three frame files, `gaps.md`, `changelog.md`, `pr.md`, both phase records and the three earlier round records whole at the target, and #1639's *Done when* (`gh issue view 1639 --json body,comments`, executed; no comment). No `pr.<lang>.md` stands.

Round 3 closed both its findings `deferred the frame` (`trail/rounds/round-3.md:80`, `:104`), so no `confirms:` line is owed. What the redesign does with each is read below as prose. Carried from round 1 and not re-derived: where `chain_check.py#follows` and the case stand, and the case's mutation result. Neither file changed in the range.

The range changes no code. The round walked the four record axes. It also read each row of `frame/plan.md` *Judgments of the run* (`:61-70`) against the rule at `skills/implement/orchestration.md:135-146` as reframed.

## Findings

### 1. "No list of what the change ... will rewrite" also reads as forbidding what a row sends, and this run's route rows name what their fixes are given

```seal
severity: should
location: `skills/implement/orchestration.md:135-141`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/design.md:55`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md:64`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md:67`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md:68`
evidence: read `skills/implement/orchestration.md:68-81`, `skills/implement/orchestration.md:126-146`, `skills/code-review/orchestration.md:274-282`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/design.md:54-57`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md:61-70`; executed `git show --format= --word-diff=plain 487a9afcc` (the route row's grounds rewritten after the reframe, its judgment cell left)
```

Why it matters: the first fact at `skills/implement/orchestration.md:137-140` says a row "gives no inventory of a change, whether a commit holds the change or the change is still to come". It then lists "no list of what the change rewrote or will rewrite". *Scope* item 4's first bullet (`frame/design.md:55`) says the same.

The fold's row is written before the decision is sent (`:130-132`). The route row is written before its fix pass. So the change still to come is the one the row itself sends. What a row sends is its decision: the findings, and the files or sections a fold or a fix pass is given. `:77` counts "a scope a spawn gives beyond a plan row" among the decisions, and the route table (`skills/code-review/orchestration.md:277`) has the crafter told what the frame says. Read with one meaning, "no list of what the change ... will rewrite" also forbids that decision. A reader cannot tell from the sentence where the decision's coordinates end and the forbidden prediction begins.

This run's rows show the line has to be drawn.

- **Row `:64`** sends "finding 6, in `frame/design.md` `## Rule changes`, to the framer's fold".
- **Row `:67`** sends "the orchestrator's return of the second row to its `471dc15b9` text, and a row of its own for the later judgment".
- **Row `:68`** sends a fix "to the crafter's fix pass for `skills/implement/orchestration.md` and `changelog.md`". `487a9afcc` rewrote that row's grounds after the reframe, and its judgment cell kept this list.

Under one reading each row breaks the rule it was written under. Under the other, each states its decision. The 0.39.2 instances the rule answers (`frame/design.md` G11, G12) are accounts: a count of folded lines, a list of what the framer folded with two items missing, and "narrowed only". None is a statement of what was sent.

The reframe and phase 2 built this sentence, so this is new work and takes neither a `regression:` nor a `reopens:` line. The fact stands in *Scope* item 4, a frame file. The skill sentence and the fragment's two lines follow from it. One added sentence fixes all three.

For `skills/implement/orchestration.md`, after the sentence that ends "no word for the kind of change a fold made or will make.":

```markdown
rewrite, and no word for the kind of change a fold made or will make.
What a row sends, the findings and the files or sections a fold or a fix
pass is given, is its decision and the decision's coordinates, and not
that inventory. `git show <commit>` is that account once the commit exists.
```

For `frame/design.md` *Scope* item 4, the first bullet gains, after "no word for the kind of change a fold made or will make.":

```markdown
What a row sends, the findings and the files or sections a fold or a fix pass is given, is its decision and the decision's coordinates, and not that inventory.
```

`changelog.md:4` takes no new clause. It states the rule's edge, and the added sentence states what stands outside it.

```seal
verdict: fixed 28b7ffc12
answer: Read against *Scope* item 4's first bullet as the framer folded it at `2dfbfe6fc`, the round's paste-ready sentence is the fold's, so it went in as given, after "no word for the kind of change a fold made or will make." in `skills/implement/orchestration.md`. The coordinator's spawn also asked for it in `changelog.md:4`, where the entry states the rule's facts, so the entry states the sentence after the same clause. `bin/test -q tests/text tests/behaviour` passes after the fix (executed).
```

### 2. The fragment and *Alternatives considered* row 15 forbid a word for the kind of any change, where the rule forbids it of a fold's

```seal
severity: should
location: `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/changelog.md:4`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md:33`
evidence: executed `git grep -n -F -e 'word for its kind' -e 'word for the kind' -- skills docs seal/threads/1795759276-the-orchestrators-records-after-the-last-round ':!*/trail/rounds/*'` (prints `changelog.md:4`, `frame/design.md:55`, `frame/design.md:85`, `frame/plan.md:11`, `:26`, `:33`, `trail/phases/phase-2.md:6` and `skills/implement/orchestration.md:140`); read `skills/implement/orchestration.md:138-146`, `skills/commit-pr-convention/SKILL.md:126-140`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md:63`
```

Why it matters: the skill (`skills/implement/orchestration.md:140`) and *Scope* item 4 (`frame/design.md:55`) forbid "a word for the kind of change a fold made or will make". Round 2's finding 2 drew that limit because the prefix row is a word for the kind of the change: `skills/commit-pr-convention/SKILL.md:129-137` is a table of kinds, and this run's row at `frame/plan.md:63` is "The title takes `fix:`".

Two records state the fact without the limit.

- **The fragment.** `changelog.md:4` says the paragraph "now says" a row gives "no word for its kind", where "its" is "a change". That fragment is the release note a person reads. So it gives the rule a reach the skill does not have, and that reach forbids the prefix row the next sentence of the same entry names.
- **Row 15.** *Alternatives considered* row 15 (`frame/plan.md:33`) gives the chosen edge as "no number, list or word for the kind of a change, made or still to come". That is the frame's own reading of the edge, and it is broader than *Scope* item 4.

The other lines the search printed keep the fold's limit, or speak of a fold or of 0.39.2's rows: `design.md:85` (S6), `plan.md:11`, `plan.md:26` and `phase-2.md:6`. The search is on the fact's words, so the list is a sample under contract rules 12 and 19. Row 15 is the framer's. The fragment is the crafter's, and its fix waits on no fold.

For `changelog.md:4`, the clause:

```markdown
no number of lines, sentences or items, no list of what the change rewrote or will rewrite, and no word for the kind of change a fold made or will make.
```

For `frame/plan.md:33`, row 15's verdict cell, the sentence "The edge is drawn by what a row says: no number, list or word for the kind of a change, made or still to come, and a row about a change states what it means." becomes:

```markdown
The edge is drawn by what a row says: no number or list of a change, made or still to come, no word for the kind of a fold's, and a row about a change states what it means.
```

```seal
verdict: fixed 28b7ffc12
answer: `changelog.md:4` takes the round's clause: "no word for the kind of change a fold made or will make", as *Scope* item 4 and the skill read. Row 15 of *Alternatives considered* is the framer's, and the fold `2dfbfe6fc` limits its kind word to a fold's. `git grep -n -F -e 'word for its kind' -- skills docs seal/threads/1795759276-the-orchestrators-records-after-the-last-round ':!*/trail/rounds/*'` prints nothing after `28b7ffc12` (exit 1, executed).
```

## Confirmations

What matched, round 3's finding 1 against the redesign. *Scope* item 4 (`frame/design.md:54-57`) now draws the rule by what a row says, "neither by which row it is nor by whether it names a commit" (G27). Its first bullet covers a change "still to come, as a fold's is when its row is written", so a row written before its fold is bound. `skills/implement/orchestration.md:135-146` builds both facts. The ban also follows the license sentence: a row about a change states what it means "and no inventory of it".

The grounds of the route row for `round-1#2` (`frame/plan.md:68`) no longer count the fold's sentences. `487a9afcc` gave them round 3's text. G29's search prints nothing at the target (executed, exit 1), and at `be757f2b7` it prints the four lines G29 gives (executed). *Alternatives considered* rows 7 and 15 and `changelog.md:4` and `:11` state the reframed edge, except the kind word that finding 2 names.

What matched, round 3's finding 2. `## Removes` (`frame/design.md`, the paragraph opening "The work adds no gate") now reads "It adds to a skill the rule sentences of *Scope* item 4". That agrees with the prefix row's "sentences" (`frame/plan.md:63`, `pr.md:4`) (read).

What matched, the reframe's form. `frame/design.md` ends with `Reframed 2026-11-27 by framer, after round 3.` under the mark, in the spelling `docs/running/the-run.md` *The run* gives. `chain_check.py --worktree` refuses nothing from its frame arm (executed). The framer wrote S6, G27 to G29, row 15, *Phases* row 2 and Q1's new reason. The new phase row's *Verified by* search is the one S6 runs, and it printed what the row says it prints (executed). Q1's new reason states this run as one reading and not the answer. That holds against `frame/design.md` G28 (read).

What matched, phase 2 against the reframe. The skill sentence writes "names any commit only as a coordinate", where *Scope* item 4 writes "It names a commit only as a coordinate". `trail/phases/phase-2.md:6` records that departure and its grounds. The frame's wording keeps the two readings round 2's finding 2 named. The build's wording has one reading, the one G27 asks for, so the departure follows the frame's intent (read). The third fact already stood in the skill as the reframe words it (`:152-156`), as the phase record says. `tests/behaviour/test_docs_line_wrap.py` passes over the rewrap `b83175868` (executed). The phase adds no case, which `gaps.md`'s row on the unpinned sentences already gives to this round. S4 and S6 were read against the paragraph here (read).

What matched, the orchestrator's rows against the reframed rule (`frame/plan.md:61-70`). Each names a commit only as a coordinate. None counts or labels the kind of a fold, made or to come. The prefix row's grounds say what the diff means against the convention. The rows at `:64`, `:67` and `:68` name what each sends, which is finding 1. The row for round 3's route (`:70`) states the framer's route as the table gives it. That holds against round 3's closes (`trail/rounds/round-3.md:80`, `:104`) and against this round, which restarts the count (read).

What matched: #1639's first *Done when* line asks for a recorded decision, and `## Rule changes` still records it, now citing the skill for what a row states of a change. The second line is conditional on a mechanism, and none is chosen (read). The range adds no test.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at the target, labelled `unverified` (contract rule 2) | the branch at `9ef37f933` | the orchestrator, by `seal gate --base origin/release/v0.39.3 --record seal/threads/1795759276-the-orchestrators-records-after-the-last-round` after the rounds settle |
| Whether the framer received the run's round records and nothing else, as the framer's route asks of its prompt | `skills/code-review/orchestration.md:289` | the orchestrator, from its spawn prompt |

## Probes

| Command | Result |
|---|---|
| `bin/test -q -p no:xdist tests/text/test_the_rules_have_one_owner.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_waiver_decided_at_start.py tests/skills/test_chain_check.py -k 'follow_up or code_commit_after_the_last_record or Test_follows or not chain_check'` in the round's clone at `9ef37f933` | exit 0, 221 passed, 259 deselected |
| `git grep -n -F -e 'names a commit, it names it' -e 'inventory of what that commit changed' -e 'inventory of what it changed' -- skills seal/threads/1795759276-the-orchestrators-records-after-the-last-round/changelog.md` at the target, and the same at `be757f2b7` | exit 1 at the target; four lines at `be757f2b7`, `skills/implement/orchestration.md:136`, `:137` and `changelog.md:4`, `:11` |
| `bin/seal pr-body --body <scratch>/body.md seal/threads/1795759276-the-orchestrators-records-after-the-last-round` in the clone | exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.39.3 --root . --worktree` in the clone | exit 0; it names `f187056e6` as owed a round, which this record is, and the gate record and guarantee as not yet written; no refusal from the frame arm and no notice at `frame/design.md` |
