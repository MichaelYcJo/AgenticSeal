# Review round 1: 1793721630-the-party-that-fixes-checks-its-fix-first

```seal
target: 8f40bffc5 against release/v0.31.0
```

The target is `git diff 6ca420572..8f40bffc5`, read in a `git clone --no-local` of the repository at `8f40bffc5` under the round's scratch directory. This is the first round, so no fact was carried from an earlier one, and every coordinate below was opened this round. `seal/parity.md` is not declared, so no `original:` line is owed. The request was read whole with `gh issue view 1318 --json title,body,comments`: the body and its one comment (executed). `seal/config.md` has no `Record language` row, so the record is in English.

The implementer's account was read as claims. The crafter claimed 9 of 9 mutants red over `agents/crafter.md`, 3 of 3 over `skills/implement/orchestration.md` and 1 of 1 over `skills/code-review/orchestration.md` at `e23058b4c`. This round re-ran two of them at HEAD, one in each of the first two files, and both went red (`## Probes`). It claimed S7's seven modules at 355 cases. This round ran the same seven and got 355 passed. It claimed S1, S3, S5 and S6 as the frame states them, and this round re-ran each with the same result. The framer claimed G9's count of 45 work items, 177 findings and 37 `regression:` findings. This round re-derived those three figures and each release row's figures (`## Probes`), and did not re-derive the 17, 18 and 2 split (`## Not judged`).

## Findings

### 1. The new rule lets the crafter fix only what its *Job* lets it write, and the *Job* gives a fix pass no write to `changelog.md`

```seal
severity: should
location: `agents/crafter.md:19-24`, `agents/crafter.md:166-171`, `skills/implement/orchestration.md:63-67`
evidence: read `agents/crafter.md:19-24`, `agents/crafter.md:161-177`, `skills/implement/orchestration.md:63-67`, `docs/layout/the-record-layout.md:65-73`, `skills/implement/SKILL.md:416-420`, `seal/threads/1793678623-each-rule-rides-with-the-agent-that-uses-it/trail/rounds/round-2.md:76-127`
```

Why it matters: the issue's own instance is a fix pass that left a census figure standing in `changelog.md` (#1313's round 2, finding 2, closed `fixed d90b20d83` by a fix pass). The new rule at `agents/crafter.md:166-168` says "Fix in your range every statement HEAD contradicts in a file your *Job* lets you write". The *Job* at `agents/crafter.md:19-24` names "`changelog.md` in the last phase" and gives a fix pass only `gaps.md` rows and close blocks, and it ends "a write not named here is a write you do not make". So a fix-pass crafter that reads the new rule as written finds a stale `changelog.md` statement and may not fix it. The rule's other branch does not catch it either. It names the files the crafter does not write as "`routing.md` or any line of the frame but your Status cell in `frame/plan.md`", so `changelog.md` falls between the two branches. Three other texts already say a fix pass writes the fragment: `docs/layout/the-record-layout.md:67-73` ("The rule binds whoever writes the commit: the crafter's fix pass, ..."), `skills/implement/SKILL.md:416-420`, and the new sentence at `skills/implement/orchestration.md:63-67`, which calls `changelog.md` "a file the crafter writes" and hands it to a crafter "resumed as a fix pass is". The *Job* sentence predates this diff, but the new rule makes it the test of what the crafter fixes, so the gap now decides the case #1318 was raised for. This round read nothing that pins the *Job*'s list (`git grep` for its clauses under `tests` and `evals` printed only the closing clause, at `tests/text/test_every_agent_reads_the_contract.py:159`).

The fix gives the fix pass the write that the other three texts already give it, at `agents/crafter.md:19-24`:

```markdown
You build one phase of one work item, or run one fix pass. Your writes are the
code and tests of the phase, `seal/threads/<work-item-id>/trail/phases/phase-N.md`,
`frame/plan.md`'s Status cell for the phase, `gaps.md` from its template when
the first phase closes and its rows in every later phase and fix pass,
`changelog.md` in the last phase and in every fix pass, and in a fix pass one
close block under each open finding; a write not named here is a write you do
not make.
```

The new rule's wording then holds as it stands. No other statement of the crafter's writes needs to change: `docs/layout/the-record-layout.md` *A commit after the build brings its changelog fragment along* and `skills/implement/SKILL.md:416-420` already say the same. The fix pass also decides whether this fact goes into the work item's `changelog.md`, which describes the new rule at `seal/threads/1793721630-the-party-that-fixes-checks-its-fix-first/changelog.md:3`.

```seal
verdict: fixed ad41ec7a8
answer: Holds. The *Job* at `agents/crafter.md:19-25` now names `changelog.md` "in the last phase and in every fix pass", the paste-ready text applied after reading it against `docs/layout/the-record-layout.md` *A commit after the build brings its changelog fragment along* and `skills/implement/SKILL.md` *5.*, which already give the fix pass that write. The new rule's wording stands. The fragment's *Changed* entry and first *Process changes* row now say so (`ad41ec7a8`, `f70ee91e4`). No case reads the clause, as none read the list before; `gaps.md` has the row (`908706952`).
```

### 2. The fold paragraph's new sentences receive only frame statements and hand back only to "the crafter that made the fix", while the crafter's rule sends it `routing.md` lines and the paragraph also governs folds no fix made

```seal
severity: should
location: `skills/implement/orchestration.md:51-67`, `skills/code-review/orchestration.md:78-83`, `agents/crafter.md:168-171`, `tests/text/test_the_rules_have_one_owner.py:385-391`
evidence: read `skills/implement/orchestration.md:51-67`, `skills/code-review/orchestration.md:71-89`, `agents/crafter.md:161-177`, `seal/threads/1793721630-the-party-that-fixes-checks-its-fix-first/frame/design.md:14`, `seal/threads/1793721630-the-party-that-fixes-checks-its-fix-first/frame/design.md:52`
```

Why it matters: the crafter's rule at `agents/crafter.md:168-171` names each statement "in a file you do not write, `routing.md` or any line of the frame but your Status cell in `frame/plan.md`, ... for the orchestrator to fold". The orchestrator's two texts take only part of that. The fold paragraph's lead at `skills/implement/orchestration.md:51-52` folds into "`frame/design.md` or `plan.md`". Its new sentence at `:58-61` reads "Where a crafter's hand-back names a frame statement ..., the orchestrator reads each frame file it folds into whole". `skills/code-review/orchestration.md:78` reads "Where the hand-back names a frame statement". No sentence tells the orchestrator what to do with a named `routing.md` statement, which only the orchestrator writes, or with a `frame/questions.md` line, which the lead does not fold into. The issue's item 1 asks that "a statement in a file it does not write is named in the hand-back for the party that writes it, and that party reads the file whole". For `routing.md`, that party has no rule to read it by.

The paragraph's last new sentence, at `skills/implement/orchestration.md:63-67`, hands a stale `gaps.md` or `changelog.md` statement "to the crafter that made the fix, resumed as a fix pass is". The paragraph governs every fold after the frame is committed. `frame/design.md` G7 (`frame/design.md:14`) says so: "It covers a fold after a fix pass, after a phase ... and after an issue comment". After an issue comment no crafter made a fix. After a phase, "the fix" names nothing the phase did. So on two of the three occasions the sentence names a party the orchestrator cannot find, and a statement it found stays standing for the next round, which is the regression this work exists to move earlier. The frame's *Scope* item 5 (`frame/design.md:52`) carries the same two gaps, so the build matches the frame and the defect is the frame's as well.

The fix rewrites the three new sentences at `skills/implement/orchestration.md:58-67`:

```markdown
settle reads the row. Where a crafter's hand-back names a statement its work
contradicts in a file the crafter does not write, a frame file or
`routing.md`, the orchestrator reads each such file whole against HEAD, not
only the named line, and rewrites every statement HEAD contradicts: the
crafter's list is its reading of a file it does not write. After the fold
commit, the orchestrator reads that commit and each file of the work item's
directory that states the present whole against HEAD, as contract rule 12
asks of the party that fixes. Where that reading finds a statement in a file
the crafter writes, `gaps.md` or `changelog.md`, the orchestrator hands it
to the implementer, the crafter that wrote the work item's last build or fix
commit, resumed as a fix pass is, before it spawns the next round or phase.
```

This snippet does not reach every statement of the fact. The fix pass owes these too:

- `skills/code-review/orchestration.md:78`: "Where the hand-back names a frame statement" becomes "Where the hand-back names a frame or `routing.md` statement".
- `tests/text/test_the_rules_have_one_owner.py:385-391`: the pinned clauses "the orchestrator reads each frame file it folds into whole against HEAD, not only the named line, and rewrites every statement HEAD contradicts" and "the orchestrator hands it to the crafter that made the fix" follow the new wording, with each seen red with its sentence deleted (contract rule 15).
- `frame/design.md` *Scope* item 5 (`:52`) states the old sentences. The frame is the orchestrator's to fold, with a `frame/plan.md` *Judgments of the run* row, and the fix pass names it in its hand-back.
- The work item's `changelog.md:3` and its second *Process changes* row say the fold reads "each frame file whole". They stay true, and the fix pass reads them against its new wording.

Where the fix pass judges instead that `routing.md` states no present fact a fix can contradict, the other repair is to drop `routing.md` from the crafter's read set at `agents/crafter.md:166` and from its list of files it does not write at `:168-169`. Either way, it says which in its answer.

```seal
verdict: fixed ad41ec7a8
answer: Holds, and `routing.md` stays in the crafter's read set: its `## Why this way` and `Branch` row state present facts a fix can contradict, and the orchestrator writes it. The fold sentences at `skills/implement/orchestration.md:58-71` take a statement "in a file the crafter does not write, a frame file or `routing.md`" and read each such file whole. The hand-over no longer names "the crafter that made the fix": I wrote it in my own words rather than the paste-ready "the implementer, the crafter that wrote ...", because `skills/code-review/orchestration.md` defines the implementer as the crafter of the last commit a round reviewed, which no fold after a phase or an issue comment has. The orchestrator now hands the statement to "a fix pass", which "is the crafter that wrote the work item's last build or fix commit, resumed or spawned fresh as" the review skill's section on that choice states, so its context threshold applies. `skills/code-review/orchestration.md:74-80` names "a frame or `routing.md` statement" in both places and folds "it". `agents/crafter.md` step 10 says "each statement named for the orchestrator". The pins at `tests/text/test_the_rules_have_one_owner.py:383-396` follow, each seen red with its clause reverted by `seal mutate` (2 of 2). `changelog.md`'s entry and second process row now name `routing.md` and the fix pass (`ad41ec7a8`). `frame/design.md` *Scope* items 4, 5 and 6 and S2 are named in the hand-back for the orchestrator to fold.
```

### 3. Rule 12 no longer asks a hand-back to say where the open part of an open class is kept, so that part may be named nowhere

```seal
severity: should
location: `skills/agent-contract/SKILL.md:163-169`, `seal/threads/1793721630-the-party-that-fixes-checks-its-fix-first/changelog.md:3`
evidence: executed `git diff 6ca420572..8f40bffc5 -- skills/agent-contract/SKILL.md`, `git grep -n -e "open part" -e "proofer's share" -- agents skills docs templates hooks README.md CONTRIBUTING.md`
```

Why it matters: at the base, rule 12 asked the hand-back to say "where the open part of a sample or of such a class stands". The issue named that clause as the exit, because a hand-back could name the proofer as the home of a closed list's remainder. This diff removes the clause whole. The new text at `skills/agent-contract/SKILL.md:163-169` says a sample stays a sample only where the class is open, "the hand-back says so", and what the party did not finish is named "as not done, never as the proofer's share". For a closed set, that closes the exit. For an open class, such as the other statements of a rule across the tree or a class over an unbounded domain, the text now asks only that the hand-back call it a sample. It no longer asks where its open part is kept. That open part is not "what you did not finish" in the sense `gaps.md` `## Not done` holds, which is "what was within reach and deliberately not taken" (`frame/design.md` G12). So a crafter's tree-wide sample, or a class over spellings, can now be handed back with no home for its remainder. Contract rule 4 states the cost: "a deferral to nobody is how *someone will look at it* becomes *nobody did*". The frame's *Removes* row (`frame/design.md:98`) argues for removing the exit for "the rest of any list, a closed one among them". Its grounds are about closed lists, and nothing in the frame argues that an open class's remainder needs no home. `seal/follow-up.md` holds rows that name open classes under rule 12, and those rows are where such a remainder has gone so far.

The fix keeps the closed-set sentences and puts the duty back for the open class only, at `skills/agent-contract/SKILL.md:163-169`:

```markdown
HEAD contradicts neither. A list of a closed set is never a sample. A
sample stays a sample only where the class is open, as the other
statements of a rule across the tree are, or a class over an unbounded
domain of keywords, spellings or constructs, where no method makes the list
whole; the hand-back says so and names where that open part is kept, which
is never the proofer's review. The hand-back names each part's method and
what it listed, calls a sample a sample, and names what you did not finish
as not done, never as the proofer's share. The proofer reads that account
```

The wording keeps S1 true, since no line then holds "open part of a sample" (`frame/design.md` S1). This snippet does not reach every statement of the fact. The fix pass owes these too:

- `seal/threads/1793721630-the-party-that-fixes-checks-its-fix-first/changelog.md:3`: "Rule 12 no longer lets a party hand on the rest of a list by saying where the open part of a sample stands" becomes a sentence saying that a closed list's rest is no longer handed on that way, and that an open class's hand-back still names where its open part is kept.
- `agents/crafter.md:175`, "that list is a sample, and the hand-back calls it one": the fix pass judges whether the crafter's rule also names where the tree-wide sample's open part goes, a leftover for `seal/follow-up.md` named in the hand-back as step 10 already allows, or whether rule 12's sentence is enough. It says which in its answer.
- `frame/design.md` *Scope* item 1 (`:42-44`) and the *Removes* row at `:98` state the old wording. They are the orchestrator's to fold, and the fix pass names them in its hand-back.

```seal
verdict: fixed ad41ec7a8
answer: Holds. The issue's item 2 keeps a sample only for an open class, and contract rule 4 asks every deferral to name where it goes, so the open part's location goes back for the open class alone. I wrote rule 12's sentence in my own words: the paste-ready "names where that open part is kept, which is never the proofer's review" has no antecedent for "that open part" and reads "kept" as a record the old text did not ask for. `skills/agent-contract/SKILL.md:167-171` now says the hand-back "says where the part of the class its list did not reach stands", and "Neither the part a sample did not reach nor what you did not finish is the proofer's share". S1 still prints the "proofer's share" line alone. `agents/crafter.md:176-177` applies it to the tree-wide sample, "calls it one and says where the part it did not reach stands", pinned in `tests/text/test_a_moved_rule_leaves_its_definition.py` and seen red with that clause reverted. `changelog.md:3` and its first process row say a closed list's rest is no longer handed on and an open class's still says where it stands (`ad41ec7a8`, `f70ee91e4`); `gaps.md` row 1 follows (`908706952`). `frame/design.md` *Scope* items 1 and 2 and the *Removes* row are named in the hand-back for the orchestrator to fold.
```

## Confirmations

```seal
confirms: none
```
What matched: S1, S3, S5 and S6 of `frame/design.md` hold at `8f40bffc5` (executed in the clone). S1's `git grep` printed `skills/agent-contract/SKILL.md:169` alone, the line holding "proofer's share", and nothing for "open part of a sample". S3's and S5's `git grep` printed nothing and exited 1. S6's `git diff --name-only 6ca420572...HEAD -- ':!seal/'` listed `agents/crafter.md`, `skills/agent-contract/SKILL.md`, `skills/code-review/orchestration.md`, `skills/implement/orchestration.md` and the two test modules, and nothing else. No reference root is touched.

```seal
confirms: none
```
What matched: S7. `bin/test` over the seven modules S7 names, in the clone at `8f40bffc5`, exited 0 with 355 passed (executed). That matches the crafter's account at `trail/phases/phase-1.md`. This is a narrow run of the slice, not the broad gate.

```seal
confirms: none
```
What matched: the crafter's mutation claim, sampled. `bin/seal mutate` over `skills/implement/orchestration.md`, turning "not only the named line" into "only the named line", made `test_a_decision_after_the_frame_is_folded_into_it` fail. Over `agents/crafter.md`, turning "every statement HEAD contradicts" into "the named statement", it made `test_the_crafter_reads_its_range_and_the_records_whole_before_it_hands_back` fail. Both files were restored, and `git status --short` printed nothing (executed). A mutation score licenses *tested*, never *safe*. The parenthesis naming the files the crafter does not write, at `agents/crafter.md:168-169`, is in no pinned clause, so a mutant that dropped it would stay green (read `tests/text/test_a_moved_rule_leaves_its_definition.py:476-492`). Finding 2's fix touches that sentence's receiver, not the parenthesis.

```seal
confirms: none
```
What matched: the new case is read against its group, and it covers what the group does not. `CRAFTERS_FOUR_RULES` and its case at `tests/text/test_a_moved_rule_leaves_its_definition.py:383-451` pin three other rules, and its docstring reads "S4's four rules", so a fifth entry would make the constant's name and docstring false, as `trail/phases/phase-1.md` claims (read). The new case at `:461-498` pins the new rule's clauses, its `check:` line and step 10's citation. No other case reads them. The `crafter_rule` change at `:375-376` compares the paragraph with its whitespace joined and still returns the raw paragraph. The other callers' leads stand on one line, so their reading is unchanged, and the fix-pass case and the four-rules case pass (read; executed in the S7 run).

```seal
confirms: none
```
What matched: `gaps.md`'s two `## Not verified` rows, which name the proofer, were read this round. Rule 12's new sentences at `skills/agent-contract/SKILL.md:159-172` state the five things `frame/design.md` *Scope* item 1 asks for, in the order of its draft, word for word against the draft at `frame/design.md:44` (read). Finding 3 is about what the draft and the rule both left out, not about a departure. The new sentences of `skills/code-review/orchestration.md:74-89` state what the fix pass's hand-back carries, say the round reads that account as a claim, cite `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* for the fold, and keep the close-block and round-record sentences (read). Finding 2 covers the one gap there. The two rows are honest: no case reads either text, and a `## Not verified` row may name the proofer for a sentence no case pins (`frame/plan.md` *Alternatives considered*, the third row).

```seal
confirms: none
```
What matched: the departure from *Done when* bullet 1 holds. The fold rule has one home, `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, which `docs/running/the-agent-set.md:104-105` and `docs/releasing/issues-and-milestones.md:319-321` also cite. The review file's paragraph cites it and does not restate it (read). This meets `skills/core/SKILL.md` *The rule a mechanism is kept against*: a fact has one source.

```seal
confirms: none
```
What matched: the orchestrator's fold at `8f40bffc5`. *Scope* item 6 now names the rewritten back-reference "the corrections its read made", which `skills/code-review/orchestration.md:84` holds. G13 now names `docs/forms/the-round-record.md:98`, "the corrections its sweep made", and that sentence stays true under the new rule, which keeps a tree-wide search and its corrections (read). The fold's *Judgments of the run* row at `frame/plan.md:52` names its grounds and the document it was judged against.

```seal
confirms: none
```
What matched: the crafter's tree-wide sample in `trail/phases/phase-1.md` is called a sample, names its method, and lists what it found. This round's own `git grep -n -i` over `agents`, `skills`, `docs`, `templates`, `hooks`, `evals`, `README.md`, `CONTRIBUTING.md` and `CLAUDE.md` for "reworded", "every other place", "left standing", "sweep", "statements beside", "named line" and "that statement" found no statement of the removed sweep or of the one-statement fold that the sample missed (executed). The hits outside this diff are about other acts, such as the built-in review's sweep and the release checklist's sweep. This is a sample too.

## Not judged

| What | Location | Who answers |
|---|---|---|
| G9's split of the 37 `regression:` findings into 17 in the records alone, 18 in the records or the fix's diff, and 2 outside both. This round re-derived only the counts of work items, findings and `regression:` lines. The split needs each pull request's `refs/pull/<n>/head` fetched from the host, which this round did not do. | `seal/threads/1793721630-the-party-that-fixes-checks-its-fix-first/frame/design.md:17-36` | the sealer, who may sample it, as the framer's account says |
| Whether the read before every hand-back costs less than the rounds it saves. | `seal/threads/1793721630-the-party-that-fixes-checks-its-fix-first/frame/questions.md:17` | the settle after 0.31.0, against G9's baseline |
| The full suite, the repository-wide lint and the typecheck at `8f40bffc5`. The suite stays `unverified`. This round leaves three findings open, so what comes due next is their fix pass and a verifying round, then the orchestrator's broad run and the sealer's spawn after it. | the whole tree | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the seven S7 modules, `-q`, in a `git clone --no-local` at `8f40bffc5` | exit 0; 355 passed |
| `bin/seal mutate skills/implement/orchestration.md --replace "not only the named line" "only the named line" --tests "bin/test tests/text/test_the_rules_have_one_owner.py -q -k folded_into_it"` | the case failed at `tests/text/test_the_rules_have_one_owner.py:393`; the file was restored |
| `bin/seal mutate agents/crafter.md --replace "your range every statement HEAD contradicts in a file your *Job* lets you" "your range the named statement in a file your *Job* lets you" --tests "bin/test tests/text/test_a_moved_rule_leaves_its_definition.py -q -k reads_its_range"` | the case failed at `tests/text/test_a_moved_rule_leaves_its_definition.py:493`; the file was restored, and `git status --short` printed nothing |
| A `bash` loop over the tags `v0.26.0` to `v0.30.1`: each work item new at a tag and holding a `routing.md` is counted once, and each round record's lines that open with `severity: ` and `regression: ` are counted with `grep -c` | 45 work items, 177 findings, 37 `regression:` lines; by release 24, 102, 22 for 0.27.0 to 0.27.3, 10, 37, 7 for 0.28.0, 7, 24, 3 for 0.29.0, and 4, 14, 5 for 0.30.0 and 0.30.1, as G9's table gives them. It reads line starts, not `hooks/lib/fields.py`'s blocks, so it is a probe of the figures and not the framer's method |
