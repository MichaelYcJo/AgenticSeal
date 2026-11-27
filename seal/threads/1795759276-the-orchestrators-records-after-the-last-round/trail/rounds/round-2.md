# Review round 2: 1795759276-the-orchestrators-records-after-the-last-round

```seal
target: f9d2756dd, fixes c6bade81d..f9d2756dd
```

This is a verifying round over the fix range `c6bade81d..f9d2756dd`, against the base `origin/release/v0.39.3`, read in a `git clone --no-local` of the repository at `f9d2756dd`. The range holds five commits: the framer's fold with the orchestrator's rows `84522e154`, the `pr.md` quote `b3e04afcc`, the crafter's fix pass `f0a46ad0c`, and the two close commits of round 1. It changes `skills/implement/orchestration.md` and the work item's records alone (executed, `git diff --stat c6bade81d..f9d2756dd`). `seal/parity.json` is not declared. The round read `routing.md`, the three frame files, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/rounds/round-1.md` whole at the target. No `pr.<lang>.md` stands, since both language keys of `seal/config.json` read English.

Carried from round 1 and not re-derived: where `chain_check.py#follows` and the new case stand, and the case's mutation result. Neither `skills/code-review/scripts/chain_check.py` nor `tests/skills/test_chain_check.py` changed in the range. The case still passes at the target (executed, `## Probes`). Re-derived here: every verdict below, and the overlap with the release's other two branches. Neither branch changes a file under `skills/` (executed, `git diff --name-only origin/release/v0.39.3...<branch>` for each).

The fix range changes no code. So the axes *Inputs*, *Authorization*, *Query scope*, *Concurrency & atomicity* and *Security* have no new path to walk. The round walked the four record axes and *Error paths*, which here means what an orchestrator meets when two rules disagree. It also walked one axis of its own: whether each row of `frame/plan.md` *Judgments of the run* keeps the rule that `skills/implement/orchestration.md:135-149` now states of every row.

## Findings

### 1. The prefix row's grounds say the new sentence follows from step 1, which the plan's own *Alternatives considered* row 12 denies

```seal
severity: should
location: `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md:61`
evidence: executed `git grep -n -F -e 'follows from step 1' -e 'adds what the row leaves out' -- seal/threads/1795759276-the-orchestrators-records-after-the-last-round/` (prints `frame/plan.md:61`, `frame/plan.md:30` and round 1's quote at `trail/rounds/round-1.md:24`); read `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md:25`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md:30`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/design.md:28`, `skills/implement/orchestration.md:36-40`, `skills/commit-pr-convention/SKILL.md:126-140`, `docs/releasing/branch-and-release.md:425`
regression: round-1#1
```

Why it matters: the prefix row was added by the orchestrator's commit `84522e154`, which closed finding 1. The frame says, in `frame/plan.md:30` (*Alternatives considered* row 12), that step 1 alone is "Rejected as the whole answer", because "The row's form still invites an inventory of the fold", and that "row 7 adds what the row leaves out". The fix wrote that the new sentence "follows from step 1". The defect came from round 1's paste-ready grounds, which were applied as given.

The two readings differ in what they allow. Step 1 (`skills/implement/orchestration.md:36-40`, quoted at `frame/design.md:28` G16) lets a row state a fact of a commit "that a command the orchestrator ran printed". So under step 1 alone a row may say that `dc13d16d7` changed `frame/design.md` and `frame/plan.md`, as `git show --stat` printed. The new sentence at `:135-139` forbids that row. A rule that forbids what step 1 allows does not follow from step 1.

The prefix decides the release. The `fix:` row of `skills/commit-pr-convention/SKILL.md:132` reads "behaviour that was wrong against a rule the tree stated before the change". `feat:` at `:131` covers "a refusal on a rule the change itself states". `docs/releasing/branch-and-release.md:425` says "the prefix is never lowered to fit the number", and a `feat:` in this patch moves #1639 to a minor. So the grounds the prefix stands on decide which release ships the work. The sealer reads every party's account against the tree, and it would find this one contradicted by the plan it sits in.

The frame does give a ground that the tree stated before this change. Row 7 (`frame/plan.md:25`) cites the core's "A fact has one source" and "Nothing is kept beside the tree to stay in step with it". A row that restates a commit's content keeps a second account of what git holds. The paste-ready row keeps `fix:` on that ground. The prefix is the orchestrator's judgment. If it reads the sentence as a new rule for an orchestrator to meet, the title takes `feat:`, #1639 moves, and the row says so instead.

```markdown
| 2026-11-27 | The title takes `fix:` | The diff rewrites a skill section that asked for a commit the policy it cites gives to a round (`frame/design.md` G1, G5), and adds to the paragraph on the orchestrator's row a sentence that applies to the rows the core's rule that a fact has one source (`frame/plan.md` *Alternatives considered* row 7); step 1 alone lets a row state what a command printed of a commit (G16), which row 12 rejects as the whole answer, so `feat:` came closest, for that sentence | `skills/commit-pr-convention/SKILL.md` *Commit messages* |
```

The quote at `pr.md:3`, "The title takes `fix:`", still stands in the row's first cell and needs no change while the prefix stays.

```seal
verdict: fixed cec86a832
answer: The orchestrator rewrote the prefix row's grounds to the round's paste-ready text, committed with the framer's fold `ef2c72eaf`, and at `cec86a832` made its "a sentence" plural, since the work adds to that paragraph the fold row's sentence too, as the framer's hand-back named. The prefix stays `fix:`, on the core's rule that a fact has one source. `cec86a832` adds the quote of the row's grounds to `pr.md`; `seal pr-body` composed the body there (executed).
```

### 2. The row rule now binds every row, and two rows the tree prescribes must say what a change did

```seal
severity: should
location: `skills/implement/orchestration.md:135-139`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/design.md:52`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/changelog.md:4`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/changelog.md:11`
evidence: executed `git grep -n -F -e 'names a commit as a coordinate' -- .` (prints `skills/implement/orchestration.md:136`, `changelog.md:4`, `changelog.md:11`, `frame/design.md:52` and round 1's quotes); read `skills/code-review/orchestration.md:263-282`, `skills/code-review/SKILL.md:163-167`, `skills/commit-pr-convention/SKILL.md:126-140`, `skills/commit-pr-convention/SKILL.md:256-258`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md:61`
regression: round-1#2
```

Why it matters: the unit is the sentence at `skills/implement/orchestration.md:135-139`, which the fix pass `f0a46ad0c` widened to "A row of *Judgments of the run*, this one and every other the orchestrator writes". The frame states the fact of every row (`frame/design.md:52`, *Scope* item 4). The fix applied that as written. The defect came from the frame's statement, which weighed the fold rows of G11 to G15 and not the rows whose judgment is about a change.

Two rows the tree prescribes now meet the ban.

- **A regression's route.** `skills/code-review/orchestration.md:280-282` writes each route as a row of *Judgments of the run* with "the comparison as its grounds". The comparison is the sentence `skills/code-review/SKILL.md:166` defines: "what the frame says, what the fix did, and where the defect came from". The row at `:278` writes "why the frame holds and the fix alone was wrong". A fix is a commit, so those grounds state what a commit changed, which the sentence at `:136-139` forbids.
- **The prefix.** `skills/commit-pr-convention/SKILL.md:256-258` asks for a row on why the title takes its prefix. A prefix is a word for the kind of change (the table at `:129-137`). This work's own row at `frame/plan.md:61` says what "the diff rewrites" and "adds".

"Names a commit as a coordinate", said of every row, also has two readings: that every row names a commit, or that a row that names one names it only as a coordinate. The prefix row names none. Before `f0a46ad0c` the sentence bound the fold's row, which names its fold commit and needs no account of it, so neither conflict arose. An orchestrator writing a route row now reads one rule that asks what the fix did and another that forbids it.

The route is the framer's, since the fix built *Scope* item 4 as written. The search is on the sentence's words, so the list is a sample under contract rules 12 and 19. The snippets below cover each line it printed. The skill sentence goes to the fix pass after the fold, and the two lines of `changelog.md` owe the same change.

For `skills/implement/orchestration.md`, replacing the sentence that opens "A row of *Judgments of the run*, this one and every other" and ends "is that account.":

```markdown
settle reads the row. Where a row of *Judgments of the run*, this one or
any other the orchestrator writes, names a commit, it names it as a
coordinate and gives no inventory of what that commit changed: no number of
lines, no list of the sentences or items a fold rewrote and no word for the
kind of change a fold made, because `git show <commit>` is that account. A
row whose judgment is about a change, such as a regression's route
(`skills/code-review/orchestration.md` *A regression is routed by comparing
the fix with the frame*) or why the title takes its prefix, states as its
grounds what the change means against the document it judges against. The
orchestrator resumes the
```

For `frame/design.md` *Scope* item 4, its first bullet:

```markdown
   - A row of *Judgments of the run* states the judgment, its grounds and the document judged against. Where it names a commit, it names it as a coordinate and gives no inventory of what that commit changed: no number of lines, no list of the sentences or items a fold rewrote, no word for the kind of change a fold made. `git show <commit>` is that account. A row whose judgment is about a change, such as a regression's route or the title's prefix, states as its grounds what the change means against the document it judges against.
```

For `changelog.md:4`, the clause "now says that a row names a commit as a coordinate and states nothing of what the commit changed" becomes "now says that a row names a commit only as a coordinate and gives no inventory of what that commit changed". For `changelog.md:11`, "a row of *Judgments of the run* names a commit as a coordinate and states nothing of what it changed" becomes "a row of *Judgments of the run* names a commit only as a coordinate and gives no inventory of what it changed".

```seal
verdict: fixed 9833b5b51
answer: Read against *Scope* item 4's first bullet as the framer folded it at `ef2c72eaf`, the round's paste-ready sentence states the same facts, so it went in as given. The sentence binds a row where it names a commit, and gives a row about a change its grounds. `changelog.md:4` and `:11` take the round's clauses. `changelog.md:4` also gains the sentence on a row about a change. `553a8ee9d` rewraps the line the fix left at 124 columns, which `tests/behaviour/test_docs_line_wrap.py` refused. `9edade97d` changes the entry's lead from "no account" to "no inventory", as the fold's item 4 title reads. `git grep -n -F -e 'names a commit as a coordinate' -- .` run again after `9edade97d` prints no line outside `seal/threads/` (exit 1). Inside it, it prints only this record's quotes and round 1's.
```

### 3. The rule on a fold's row lets no round or sealer correct it, and this run's own correction of the first row is the act it forbids

```seal
severity: should
location: `skills/implement/orchestration.md:146-149`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/design.md:53`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/changelog.md:4`
evidence: executed `git grep -n -F -e 'changes it only where' -e "only where the framer's hand-back names a defect" -- .` (prints the three lines of the location), `git show --format= -U0 --word-diff=plain 84522e154 -- seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md`; read `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/trail/rounds/round-1.md:84-100`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/design.md:23-27`
```

Why it matters: the sentence at `skills/implement/orchestration.md:146-149` reads "After the fold the orchestrator changes it only where the framer's hand-back names a defect in it, which it corrects, or where the framer rejects the decision". A round's finding and the sealer's verdict are neither of these. Phase 1 built the sentence, so this is new work and takes neither a `regression:` nor a `reopens:` line. The fix range is what puts it into effect. Round 1's finding 4 found the first row false, a fold's row folded at `dc13d16d7`. The orchestrator rewrote it at `84522e154`, as the finding asked, with no framer hand-back naming it. Read with one meaning, "only" forbids that correction.

The instances this work rests on were corrected the same way. G12 (`frame/design.md:24`) is a round's finding on fold rows, fixed by `6a1347cc5` (G15, `:27`). G11 (`:23`) is a sealer's `withheld` on a row. An orchestrator that keeps the sentence leaves such a row false, and the sealer withholds again on the same row, so the run cannot close. The frame states the sentence this way at `frame/design.md:53`, so the change is the framer's. The fix pass after the fold owes the skill sentence and `changelog.md:4`.

For `skills/implement/orchestration.md`:

```markdown
answers. The row for a fold states the decision as it was sent. After the
fold the orchestrator changes it only where the framer's hand-back, a
round's finding or the sealer's verdict names a defect in it, which it
corrects, or where the framer rejects the decision, as the next paragraph
states. It then commits the frame files the framer
```

For `frame/design.md` *Scope* item 4, its second bullet:

```markdown
   - The row for a fold states the decision as it is sent. After the fold the orchestrator changes it only where the framer's hand-back, a round's finding or the sealer's verdict names a defect in it, or where the framer rejects the decision, which the next paragraph already states.
```

For `changelog.md:4`, "only where the framer's hand-back names a defect in it or the framer rejects the decision" becomes "only where the framer's hand-back, a round's finding or the sealer's verdict names a defect in it, or the framer rejects the decision".

```seal
verdict: fixed 9833b5b51
answer: The sentence on a fold's row now names the framer's hand-back, a round's finding or the sealer's verdict as what names a defect in it, the round's paste-ready text. That text matches *Scope* item 4's second bullet as folded at `ef2c72eaf`. `changelog.md:4` takes the round's clause. `git grep -n -F -e 'changes it only where' -e "only where the framer's hand-back names a defect" -- .` run again after `9edade97d` prints, outside `seal/threads/`, `skills/implement/orchestration.md:151`, the fixed sentence. Inside it, it prints `frame/design.md:53`, the fold, and this record's quotes.
```

### 4. The second row was rewritten after its fold on no finding, and now names a document its decision was not judged against

```seal
severity: should
location: `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md:60`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md:62`
evidence: executed `git show --format= -U0 --word-diff=plain 84522e154 -- seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md`, `git show 471dc15b9:seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md` (the row as committed with its fold); read `skills/implement/orchestration.md:68-101`, `skills/implement/orchestration.md:146-149`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/trail/rounds/round-1.md:100`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/trail/rounds/round-1.md:165`
regression: round-1#4
```

Why it matters: the unit is the second row of *Judgments of the run*, which `84522e154` changed as part of finding 4's close. The frame says, in `frame/design.md:53` (*Scope* item 4), that a fold's row "states the decision as it is sent" and changes after the fold only on the framer's hand-back or rejection. The fix rewrote all three of the row's cells after its fold `471dc15b9`, on no hand-back and on no finding. Finding 4's close says "which no finding named". The defect came from the orchestrator rewriting its row to its later reading of the procedure. It would stay outside the rule under finding 3's wider sentence as well.

At `471dc15b9` the row named the paragraph opening **A decision made after the frame is committed is folded** as its document, with the grounds "A coordinate in a frame file is the framer's to fold". At the target it names the paragraph opening **The framer writes a decision's fold**. That paragraph (`skills/implement/orchestration.md:86-90`) says that for a frame statement a crafter's hand-back names, "the orchestrator folds it in a commit of its own and spawns no framer". So the row now says that a framer spawn was judged against the paragraph that refuses one. The grounds, "The coordinate stood in a frame file", are what that paragraph says does not lead to the spawn. The settle reads the row for what the orchestrator weighed when it acted. The row no longer says, and the misreading the settle would learn from is gone.

The reading that the spawn was not the procedure's is a judgment of its own, made at round 1's closes. It has no row. The fourth row (`:62`) records the rewrite as "beside the second row's grounds", where `84522e154` also rewrote the row's *Judgment* and *Judged against* cells. Finding 4's close (`trail/rounds/round-1.md:100`) gives the same part account, and it stands as an earlier record.

The *Judgment* cell's "the crafter's hand-back named" in place of "the crafter's read found HEAD contradicts" answers round 1's question at `trail/rounds/round-1.md:165`. Both wordings are true of the phase: the read found the one coordinate, and finding 5's close says the hand-back named one. So the row as sent can return whole.

The second row, as committed at `471dc15b9`:

```markdown
| 2026-11-27 | After phase 1 (`cc4aad5f9`), the orchestrator sent the framer the one frame coordinate the crafter's read found HEAD contradicts, *Alternatives considered* row 14's citation of `skills/implement/orchestration.md` | A coordinate in a frame file is the framer's to fold | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph opening **A decision made after the frame is committed is folded** |
```

In the fourth row, the clause ", beside the second row's grounds, which no round named" is deleted. A new row follows it:

```markdown
| 2026-11-27 | At round 1's closes, the orchestrator judged that its spawn of the framer for the coordinate of the second row was not the procedure's; the fold of that coordinate, `471dc15b9`, stands | The paragraph opening **The framer writes a decision's fold** gives a frame statement a crafter's hand-back names to the orchestrator's own fold, with no framer spawned | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph opening **The framer writes a decision's fold** |
```

```seal
verdict: fixed cec86a832
answer: The orchestrator returned the second row to its `471dc15b9` text, deleted the clause from the fourth row and added the round's row for the judgment at round 1's closes, all committed with the framer's fold `ef2c72eaf`. At `cec86a832` it replaced round 2's single routing row, which named no regression, with one row per regression and one for finding 3, as the framer's hand-back named.
```


## Confirmations

```seal
confirms: round-1#1
```
What holds: `frame/plan.md:61` holds a row on why the title takes `fix:`, with the kind that came closest. `pr.md:3` quotes its first cell, and `b3e04afcc` committed that quote after `84522e154` committed the row, as `skills/commit-pr-convention/SKILL.md:256-258` asks. `seal pr-body` composed the body at the target and refused nothing (executed). The row's grounds are finding 1 of this round.

```seal
confirms: round-1#2
```
What holds: the sentence at `skills/implement/orchestration.md:135-139` now binds every row, as `frame/design.md:52` states. The finding's search, run again, prints that line alone outside `seal/threads/` (executed). What the widening collides with is finding 2 of this round.

```seal
confirms: round-1#3
```
What holds: the drain's third paragraph (`skills/implement/orchestration.md:564-568`) names `docs/checks/the-pull-request-check.md` *What the check reads at the pull request*. `git grep -n -F -e 'that document names' -- skills docs agents` prints nothing (executed, exit 1). `tests/behaviour/test_a_cited_section_stands_in_its_file.py` passes with the new citation (executed).

```seal
confirms: round-1#4
```
What holds: the first row (`frame/plan.md:59`) names `ecbbfa0a9`, `6a1347cc5`, `5c7781602` and `dc13d16d7` as coordinates and says nothing of what they changed. The close's claim that the fourth row was written before the framer's fold and committed with it is consistent with `84522e154` holding both. Git cannot show the order of uncommitted writes, so that part is unverified, and the orchestrator answers it. The rewrite of the second row in the same commit is finding 4 of this round.

```seal
confirms: round-1#5
```
What holds: `trail/phases/phase-1.md:5` opens with the three false coordinates. `git show 04ef48112:skills/implement/orchestration.md | grep -n` on the passages' first and last lines prints 121, 123, 126 and 144, and line 124 ends the sentence that opens at 121, as the bullet says (executed, `sed -n 124p`). The close says the hand-back named row 14 alone, and the second row says the same. The hand-back is not among the records, so both rest on the orchestrator's account, and this round answers round 1's question at `trail/rounds/round-1.md:165` with that label.

```seal
confirms: round-1#6
```
What holds: the `to` at `frame/design.md:93` states the decision, cites the paragraph opening **The orchestrator writes its row before it sends a decision** (it stands at `skills/implement/orchestration.md:126`), and restates no rule. *Scope* item 5 (`:54`), S5's *Then* cell (`:80`) and the paragraph under `## Removes` (`:102`) say the same. `chain_check.py --worktree` refuses no operation of `## Rule changes` and prints no notice at a line of `frame/design.md` (executed). Its claim that the false rows named by 0.39.2's rounds and sealer "restated what a fold commit changed or judged what a sentence meant" holds of G11, G12 and G13, the rows those parties named (read). No other unsettled design changes the paragraph the `to` cites (executed, `grep -n -F` on its opening words over `seal/threads/*/frame/design.md`).

What matched: round 1 left the orchestrator one question, whether `frame/questions.md` Q1's default, "The rows stay text", must be quoted in `pr.md` under `Automation` `yes`. It need not be. The paragraph of `docs/running/the-run.md:33-52` governs a question the orchestrator would otherwise put to the owner. For such a question it proceeds on the default, writes it as a row, and quotes it "where the owner can overturn it". Q1's *Who can answer* is a measurement, the settle after the next release. No person can answer it, and `agents/framer.md:206-210` says of a measurement's row and the work's row that "neither holds anything for the reader to act on". The choice that rows stay text is the frame's, `frame/plan.md` *Alternatives considered* row 7, not a default taken in an owner's place. So `skills/code-review/orchestration.md:374-376` asks no quote of it (read).

What matched: the range adds no test, so no new case is read against its group.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at the target, labelled `unverified` (contract rule 2) | the branch at `f9d2756dd` | the orchestrator, by `seal gate --base origin/release/v0.39.3 --record seal/threads/1795759276-the-orchestrators-records-after-the-last-round` after the rounds settle |
| Whether the title takes `fix:` or `feat:`, once finding 1's grounds are corrected. The prefix is the orchestrator's judgment, and `feat:` moves #1639 out of this patch | `frame/plan.md:61` | the orchestrator |
| What the phase 1 hand-back named, which finding 5's close and the second row both state and no record holds | `frame/plan.md:60` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test -q -p no:xdist tests/text/test_the_rules_have_one_owner.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_waiver_decided_at_start.py tests/behaviour/test_docs_line_wrap.py tests/skills/test_chain_check.py -k 'follow_up or code_commit_after_the_last_record or Test_follows or not chain_check'` in the round's clone at `f9d2756dd` | exit 0, 221 passed, 259 deselected |
| `bin/seal pr-body --body <scratch>/body.md seal/threads/1795759276-the-orchestrators-records-after-the-last-round` in the clone | exit 0; the body opens with the three quotes of `pr.md` |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.39.3 --root . --worktree` in the clone | exit 0; it names findings 2, 3 and 5 of round 1 and `f0a46ad0c` as owed a verifying round, which this record is, and the gate record and guarantee as not yet written; no notice at `frame/design.md` |
