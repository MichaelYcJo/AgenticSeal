# Review round 1: 1795759276-the-orchestrators-records-after-the-last-round

```seal
target: c6bade81d against origin/release/v0.39.3
```

This is the first round, so no earlier record hands it a coordinate or a verdict, and every fact below was established at the target. `seal/parity.json` is not declared. The round read `routing.md`, the three frame files, `gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md` whole at `c6bade81d`; no `pr.<lang>.md` stands, since both language keys read English. It read the code diff `git diff origin/release/v0.39.3...c6bade81d -- skills tests` hunk by hunk, the sections around each hunk, and each commit of the range with `git show --stat`.

## Findings

### 1. No row of *Judgments of the run* says why the title takes its prefix, and `pr.md` quotes none

```seal
severity: must
location: `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md:55-60`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/pr.md:1-2`
evidence: executed `git grep -n -i -e 'title takes' -e 'prefix' -- seal/threads/1795759276-the-orchestrators-records-after-the-last-round/` (prints nothing, exit 1); read `skills/commit-pr-convention/SKILL.md:256-258`, `skills/code-review/orchestration.md:376-380`
```

Why it matters: `skills/commit-pr-convention/SKILL.md:256-258` says "Why the title takes its prefix, and the kind that came closest where one did, is one row of `frame/plan.md` *Judgments of the run*, which `pr.md` quotes. The orchestrator writes that row before it writes `pr.md`." `skills/code-review/orchestration.md:376-380` lists the same quote among what `pr.md` holds. `agents/sealer.md` step 4 reads those grounds against the design and the diff, so a body without them gives the sealer nothing to read the prefix against. The plan's section holds two rows, one for each fold, and neither names a prefix. `pr.md` was committed at `c6bade81d`, after both rows, and it quotes two sentences of *Operational impact* alone. The search above finds no word of a prefix anywhere in the work item's directory. The convention is kept elsewhere in the tree, for example `seal/threads/1794271935-the-releasing-documents-describe-the-note-twice/frame/plan.md:119` and its `pr.md:7`. The commits of this branch take `fix:` and `docs:`, so the title's prefix is a choice the orchestrator has made and not written down.

The paste-ready row below is this round's reading of the diff against the table in `skills/commit-pr-convention/SKILL.md` *Commit messages*. The prefix is the orchestrator's judgment, so it replaces the grounds where its own reading differs. `feat:` is named as the closest kind because the paragraph on the row gains a sentence that no rule stated in those words before.

```markdown
| 2026-11-27 | The title takes `fix:` | The diff rewrites a skill section that asked for a commit the policy it cites gives to a round (`frame/design.md` G1, G5), and adds to the paragraph on the orchestrator's row a sentence that follows from step 1, which already bound every fact a row states of a commit to a command the orchestrator ran (G16); `feat:` came closest, for that sentence | `skills/commit-pr-convention/SKILL.md` *Commit messages* |
```

and, in `pr.md`, above the `Closes` lines:

```markdown
- "The title takes `fix:`" (`frame/plan.md` *Judgments of the run*, the third row of 2026-11-27)
```

```seal
verdict: fixed 84522e154
answer: The orchestrator wrote the round's paste-ready row as the third row of 2026-11-27 in `frame/plan.md` *Judgments of the run*, committed in the framer's fold `84522e154`, and `b3e04afcc` adds the round's quote of it to `pr.md` above the `Closes` lines. `seal pr-body` composed the body at `b3e04afcc` without refusing the quote (executed).
```

### 2. The new rule on what a row states of a commit binds the fold's row alone, where the frame and the changelog state it of every row

```seal
severity: should
location: `skills/implement/orchestration.md:135-138`
evidence: executed `git grep -n -F -e 'names a commit as a coordinate' -e 'names a commit and gives no account' -- .`; read `skills/implement/orchestration.md:126-150`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/design.md:51-52`, `skills/code-review/orchestration.md:184`, `skills/implement/orchestration.md:504`, `skills/commit-pr-convention/SKILL.md:256`, `docs/running/the-run.md:24`
```

Why it matters: *Scope* item 4 (`frame/design.md:51-52`) states the fact of "A row of *Judgments of the run*": it "names a commit as a coordinate" and "states nothing of what the commit changed". `changelog.md:4` and its process row at `changelog.md:11` say the same of "a row of *Judgments of the run*". The build put the fact into the fold paragraph as "The row names a commit as a coordinate", and in that paragraph "the row" is the one the orchestrator writes before it sends a decision to the framer. Rows that are not about a fold get no rule. These include the row that decides to go on or stop (`skills/code-review/orchestration.md:184`), a raise (`skills/implement/orchestration.md:504`), the title prefix (`skills/commit-pr-convention/SKILL.md:256`) and a leftover's home (`docs/running/the-run.md:24`). An orchestrator writing a stop row reads no sentence that forbids an account of a commit. Not every false row of 0.39.2 was a fold row: G13's row judged a policy sentence in a routing decision. The search above prints the skill line as the only statement outside the work item's records, and every record statement it prints is general. The search is on the fact's words, so the list is a sample under contract rule 12. `trail/phases/phase-1.md:8` says the fact "follows the sentence on the row the framer reads". That is true of where the sentence stands, so the fix leaves that line as it is.

```markdown
settle reads the row. A row of *Judgments of the run*, this one and every
other the orchestrator writes, names a commit as a coordinate and states
nothing of what the commit changed: no number of lines, no list of the
sentences or items a fold rewrote and no word for the kind of change,
because `git show <commit>` is that account. The orchestrator resumes the
```

```seal
verdict: fixed f0a46ad0c
answer: The sentence now opens "A row of *Judgments of the run*, this one and every other the orchestrator writes, names a commit as a coordinate", the round's paste-ready text applied after reading it against `frame/design.md` *Scope* item 4, which states the fact of every row. `git grep -n -F -e 'names a commit as a coordinate' -e 'names a commit and gives no account' -- .` run again after `f0a46ad0c` prints, outside `seal/threads/`, `skills/implement/orchestration.md:136` alone, the fixed sentence; inside it, `changelog.md:4` and `:11`, `frame/design.md:52` and `frame/plan.md:25`, each of which states the fact of every row and stands, and this record's own quotes. `trail/phases/phase-1.md`'s bullet on where the fact went stands, as the finding says.
```

### 3. The drain's third paragraph says "that document", and the nearest document it can mean is the wrong one

```seal
severity: should
location: `skills/implement/orchestration.md:563-566`
evidence: read `skills/implement/orchestration.md:545-566`, `skills/code-review/gate-to-pull-request.md:51`, `skills/code-review/gate-to-pull-request.md:153`, `skills/code-review/gate-to-pull-request.md:181`
```

Why it matters: the paragraph reads "Its commit outside the work item's directory costs the verifying round that document names". The document meant is `docs/checks/the-pull-request-check.md` *What the check reads at the pull request*, which the first paragraph names at `:547-549`. The document named last before the sentence is `skills/code-review/gate-to-pull-request.md`, at the end of the second paragraph (`:560-561`). That file also names verifying rounds (`:51`, `:153`, `:181`), so a reader who takes the nearer document finds an answer there and never notices the misreading. `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* asks text an agent acts on to have one reading. The same paragraph's last sentence already names its document by path, so naming this one costs a few words.

```markdown
**A row that first arises once no round is to follow is weighed.** Its
commit outside the work item's directory costs the verifying round
`docs/checks/the-pull-request-check.md` *What the check reads at the pull
request* names, and a home that needs no such commit costs none. The homes
are those `docs/running/the-run.md` *The run* gives.
```

```seal
verdict: fixed f0a46ad0c
answer: The third paragraph of the drain section now names `docs/checks/the-pull-request-check.md` *What the check reads at the pull request* in place of "that document", the round's paste-ready text. `git grep -n -F -e 'that document names' -- skills docs agents` prints nothing after `f0a46ad0c` (exit 1).
```

### 4. The orchestrator's first row states what the fold commit and three earlier commits changed, and was written after the fold

```seal
severity: should
location: `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md:59`
evidence: executed `git show --format= -U0 04ef48112`, `git show --stat dc13d16d7`, `git show 46f17076c:seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/plan.md` (its *Judgments of the run* holds only the empty template row); read `skills/implement/orchestration.md:126-150`
```

Why it matters: the row reads "the orchestrator sent the framer the corrections of #1641's and #1639's bodies and the three commits that rewrote 0.39.2's lane B rows; the framer folded them at `dc13d16d7`". Two parts of it give an account of a commit. "Folded them at `dc13d16d7`" says what that commit holds, and "commits that rewrote 0.39.2's lane B rows" uses a word for the kind of change three commits made. The rule phase 1 writes at `skills/implement/orchestration.md:135-138` forbids both. The row's history is the defect #1639 names. The frame before the fold, `46f17076c`, held only the empty template row. The fold `dc13d16d7` changed `frame/design.md` and `frame/plan.md` and left that empty row in place. The row was then written and committed alone at `04ef48112`. So the framer read no row while folding, and the row was written from the fold that had already happened. The paragraph in force at `e503c6961` asks the orchestrator to write the row before it sends the decision, leave it uncommitted so that the framer reads it, and commit it in one commit with the frame files the framer changed. The order cannot be undone, but the row's text can be brought under the rule. The commits are the ones `frame/design.md` G15 names. The second row (`:60`), added in the fold commit `471dc15b9`, names its commit only as a coordinate and states the decision as it was sent. Its claim about what the crafter's read found is a row of `## Not judged`.

```markdown
| 2026-11-27 | Before the build, the orchestrator sent the framer the corrections of #1641's and #1639's bodies and the commits `ecbbfa0a9`, `6a1347cc5` and `5c7781602` of 0.39.2's lane B, to fold; the fold is `dc13d16d7` | Frame sentences cited issue bodies the orchestrator had corrected the same day, and a reading the frame left unverified had commits to open | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph opening **A decision made after the frame is committed is folded** |
```

```seal
verdict: fixed 84522e154
answer: The orchestrator rewrote the first row in place to the round's paste-ready text, which names `ecbbfa0a9`, `6a1347cc5`, `5c7781602` and `dc13d16d7` as coordinates and states nothing of what they changed, uncommitted, and the framer committed it with its fold `84522e154`. The order the round names, the row written after the fold it records, is not undone; the fourth row, for this round's decisions, was written before the framer's fold and committed with it. The orchestrator also rewrote the second row's grounds, which no finding named: they said a frame coordinate is the framer's to fold, where the paragraph opening **The framer writes a decision's fold** gives a statement a crafter's hand-back names to the orchestrator's own fold.
```

### 5. The phase record says the frame holds against the tree at `04ef48112`, where three of its line coordinates did not

```seal
severity: should
location: `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/trail/phases/phase-1.md:5`
evidence: executed `git show e503c6961:skills/implement/orchestration.md | sed -n 116,144p`, `git log --oneline e503c6961..c6bade81d -- skills/implement/orchestration.md` (only `33bce0f99`, so the file at `04ef48112` is the file at `e503c6961`), `git show --format= -U0 --word-diff=plain 471dc15b9`
```

Why it matters: `phase-1.md:5` opens "**The frame holds against the tree at `04ef48112`.**" At that commit, three of the frame's coordinates of `skills/implement/orchestration.md` were false. *Alternatives considered* row 14 cited `:118-121` for the sentence opening "After a fold commit of its own", which runs from line 121 to 124. `frame/design.md` G16 read the paragraph opening **The orchestrator writes its row before it sends a decision** as "lines 126 to 141", and *Technical context* cited `:126-141`, while that paragraph ran to line 144. The phase record checked only where the paragraph starts ("stood at line 126 of that file"). The orchestrator's row at `frame/plan.md:60` reports that the crafter's read found one of the three, row 14. The framer's fold at `471dc15b9` corrected all three. `agents/proofer.md` *Every round reads the work item's records that state the present* counts a statement that a builder's read held, where the account missed what the read should have found, as a finding on the method, even when every instance has since been fixed. A sealer reading `phase-1.md:5` takes it as a frame the crafter found sound, and it was not sound.

```markdown
- **The frame holds against the tree at `04ef48112`, except three line coordinates of `skills/implement/orchestration.md`.** *Alternatives considered* row 14 cited `:118-121` for the sentence opening "After a fold commit of its own", which ran from line 121 to 124, and `frame/design.md` G16 and `frame/plan.md` *Technical context* gave the paragraph opening **The orchestrator writes its row before it sends a decision** as ending at line 141, where it ended at 144 (read). The search of `frame/design.md` G24 printed `skills/implement/orchestration.md:539` alone before the build (read).
```

The rest of the bullet, from "`chain_check.py#follows` stood at line 1007" on, stays as it is.

```seal
verdict: fixed f0a46ad0c
answer: The bullet's opening is now the round's paste-ready text, and the rest of it stands. `git show 04ef48112:skills/implement/orchestration.md | grep -n` on each passage's first and last words printed lines 121, 124, 126 and 144 (executed): at `04ef48112` the sentence opening "After a fold commit of its own" starts at line 121 of `skills/implement/orchestration.md` and runs to 124, and the paragraph opening **The orchestrator writes its row before it sends a decision** runs from line 126 to 144, where `frame/design.md` G16 and `frame/plan.md` *Technical context* gave 141 until the fold `471dc15b9`. The phase-1 hand-back had named row 14 alone; the other two coordinates were missed because the read checked only where the paragraph starts.
```

### 6. The `## Rule changes` `to` restates the rule the skill now holds, so after the settle the rule has two sources

```seal
severity: should
location: `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/design.md:93`, `seal/threads/1795759276-the-orchestrators-records-after-the-last-round/frame/design.md:80`
evidence: executed `git grep -n -F -e 'its grounds and the document it stands on' -- docs skills`, `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.39.3 --root . --worktree` in the clone (no notice at `frame/design.md`); read `skills/implement/orchestration.md:135-138`, `docs/running/the-run.md:54`
```

Why it matters: the `to` adds to `docs/running/the-run.md` *The run* this rule: "A row states the judgment, its grounds and the document it stands on. Of a commit it states the name alone. What the commit changed, such as how many lines, which sentences a fold rewrote or what kind of change it was, is read from the commit". The skill now states the same rule at `skills/implement/orchestration.md:135-138`, in other words, and the settle writes only the policy root, so after the settle both stand. `skills/core/SKILL.md` *The rule a mechanism is kept against* asks for one source with links to it, and contract rule 19 explains the harm: the next change to one statement does not find the other with `git grep`, because the words differ. That is also why the check's copy reading, a window of words, printed no notice here. The first sentence of the `to` also repeats the bold lead of the section's own paragraph at `docs/running/the-run.md:54`, "each with its grounds and the document it stands on". What the policy root does not hold anywhere else is the decision: that #1639 kept the rows as text, and why. The fix below keeps that decision and cites the skill for the rule. S5 (`frame/design.md:80`) says the section "says what a row states of a commit", so it changes with the fix. If the framer would rather have the policy hold the rule and the skill cite it, that is a design the settle cannot write on its own, since the settle edits no skill. The fold says which way it goes.

```markdown
- add
  file: docs/running/the-run.md
  section: The run
  to: **#1639 kept the orchestrator's rows of *Judgments of the run* as text.** What a row states of a commit is `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*'s, in the paragraph opening **The orchestrator writes its row before it sends a decision**. #1639 weighed a check of the records arm, a `seal` subcommand, a hook and an agent field for these rows: the false rows that release 0.39.2's rounds and its sealer named restated what a fold commit changed or judged what a sentence meant, a script reads neither exactly, and a row that holds no account of a commit has none to get wrong.
```

and the S5 row's *Then* cell: "then the section says that #1639 kept the rows as text and cites the skill for what a row states of a commit".

```seal
verdict: fixed 84522e154
answer: The framer folded the round's paste-ready `to` into `frame/design.md` `## Rule changes`, with S5's *Then* cell, *Scope* item 5 and the paragraph under `## Removes`, at `84522e154`. The policy root then holds the decision and cites `skills/implement/orchestration.md`'s paragraph for the rule.
```


## Confirmations

What matched: *Scope* item 3's case `tests/skills/test_chain_check.py::Test_main::test_refuses_a_follow_up_row_after_the_last_record` passes at the target. With `chain_check.py#follows` mutated to let `seal/follow-up.md` through, it goes red at its one assertion, and its group, `Test_follows` and `test_refuses_a_code_commit_after_the_last_record`, stays green under the same mutation (executed, `## Probes`). That matches phase 1's claims at `phase-1.md:9-10`. The case holds a fact the frame states, S1, so it covers something its group does not.

What matched: the first two paragraphs of the drain section (`skills/implement/orchestration.md:545-561`) state the first three facts of *Scope* item 1 and keep the heading and the table's destinations. The stop rule at `skills/code-review/orchestration.md:196-203` no longer counts a `seal/follow-up.md` row committed after the last round among the homes that cost no round, and cites the drain section, as *Scope* item 2 asks (read). `git grep -n -F -e 'moves every unresolved row out once the last round record' -- . ':!seal/threads'` prints nothing at the target (executed, exit 1), as S2 asks. Findings 2 and 3 are this round's read of the new sentences, which is the read `gaps.md:9` hands to the round.

What matched: `chain_check.py --worktree` at the target refuses no operation of `## Rule changes` and prints no notice at a line of `frame/design.md`. It refuses only for the round record, gate record and guarantee that are still owed (executed). The five text and behaviour modules phase 1 names pass, 164 cases (executed).

What matched: the weighing in `frame/plan.md` *Alternatives considered*, judged against `skills/core/SKILL.md` *The rule a mechanism is kept against*. For #1630 the check keeps its rule. Rows 2, 3 and 5 would widen an invariant that has no catch record either way, and G1 and G2 give the commit to a round, so changing the procedure is the change the problem calls for, and the frame did not adapt to a structure. For #1639, rows 8 to 11 each fail on a fact this round opened. A commit cell would refuse none of G11's commits, since both stand on the branch and both changed `frame/design.md`. The core forbids a gate on a count or a word for a kind of change. The `skills:`, `tools:` and `hooks:` fields reach an agent and never the session. `hooks/edit-leaves-copies.py` is a `PostToolUse` hook on `Edit` (`hooks/hooks.json:35-41`) whose catch record still waits in `seal/follow-up.md`. Row 7 removes the claim that a check, a print or a hook would verify, so the chosen text has nothing for a mechanism to read, and `frame/questions.md` Q1 measures whether the text holds (read).

What matched: neither parallel lane touches a file this work changes. `fix/1640-1642-...` changes `lib/gitcmd.py`, `range_read.py` and the tests of `gitcmd`, `seal` and `settle`, and `fix/1641-...` changes `lib/core.py`, the version files and the core tests (executed, `git diff --name-only origin/release/v0.39.3...<branch>`). The new case holds no submodule, so `--ignore-submodules=none` on `diff-tree` does not change what it reads.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the crafter's read named one frame coordinate that HEAD contradicts, as the second row of *Judgments of the run* says. The hand-back is not in the records, and `phase-1.md:5` says the frame holds (finding 5) | `frame/plan.md:60` | the orchestrator, from the crafter's hand-back |
| Whether `frame/questions.md` Q1's default, "The rows stay text", is a default taken under `Automation` `yes` that `pr.md` must quote (`skills/code-review/orchestration.md:373-376`). It is the framer's question, answered by a measurement rather than by a person | `frame/questions.md:20`, `pr.md` | the orchestrator |
| The full suite, the repository-wide lint and the format check at the target, labelled `unverified` (contract rule 2) | the branch at `c6bade81d` | the orchestrator, by `seal gate --base <base> --record <item>` after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/skills/test_chain_check.py -k 'follow_up or code_commit_after_the_last_record or Test_follows' -p no:xdist` in the clone at `c6bade81d` | 5 passed |
| The same command with `chain_check.py#follows`'s test changed by an `Edit` to `if path != "seal/follow-up.md" and not path.startswith(f"{item}/") or (`, then `git checkout -- skills/code-review/scripts/chain_check.py` | exit 1: `test_refuses_a_follow_up_row_after_the_last_record` failed at its `assert any(...)`, 4 passed; `git status --short` was empty after the restore |
| `bin/test -q tests/text/test_the_rules_have_one_owner.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_waiver_decided_at_start.py` in the clone | 164 passed |
