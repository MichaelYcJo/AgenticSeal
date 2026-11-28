# Review round 4: 1795830609-iadd-is-the-method-and-a-product-only-expresses-it

```iadd
target: 1349c2fc, fixes 193aba58..1349c2fc
```

The round is the verifying round over the fixes of round 3. `git log --oneline 193aba58..1349c2fc` names three commits: `8e41532c`, the round 3 record; `d0811133`, the orchestrator's application of round 3's paste-ready lines to `pr.md` and to `frame/plan.md` *Judgments of the run*; and `1349c2fc`, the close blocks of round 3. `git show --stat d0811133` names `pr.md` and `frame/plan.md` alone, and `git diff --stat 7e36d5cf..1349c2fc` names only files of this work item's directory (executed). The round read `git diff 193aba58..1349c2fc` whole.

The round read the work item's `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and `trail/gate.md` whole at `1349c2fc`, and round 3 whole. No `pr.<lang>.md` stands, and none is owed: `agentory/config.json` names English for both `Commit and pull request language` and `Record language`. `agentory/parity.json` is absent, so no parity comparison is owed. Runs went in a `git clone --no-local` at `1349c2fc` under `<scratchpad>/1795830609-iadd-is-the-method-and-a-product-only-expresses-it/round-4/clone`. Nothing in the checkout changed but this record.

Carried from round 3, not re-established: the rule `pr.md` is judged against, `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the work item is cleared*, its paragraph on `pr.md`; the body's order, `pr.md`, then `## From the records`, the changelog fragment and the `<details>` fold; and the fact that `agentory/threads/` holds no other work item of the release but #1656's, whose `## Rule changes` is `- nothing`. `ls agentory/threads` printed the two directories at this round too (executed). `git rev-parse --short origin/release/v0.40.0` printed `801465cb` (executed). Every verdict below is this round's own.

`python3 skills/code-review/scripts/chain_check.py --baseline 801465cb --root . --worktree` in the clone at `1349c2fc`, before this record was written, exited 0 and printed no line that names `trail/rounds/round-3.md` (executed). So the check reads each `fixed d0811133` of round 3 as a fix that touched this work item's records alone, with each finding's `location:` in those records. By the row *No fix that no round reads* of `skills/core/SKILL.md` *Judgment is not licence to skip a party*, the reader of that fix is the inspector, and `docs/running/the-run.md` *The run* says no round follows such a pass. The round was spawned all the same, and it reads the fix as asked. No rule the round found asks for it, and no row of `frame/plan.md` *Judgments of the run* records the decision to spawn it. *The run* asks for such a row only at or past the third finding round, and round 2 opened nothing, so this is the second finding round's verifying round, and the round opens no finding on the missing row.

## Findings

None. The round opens no finding.

## Confirmations

```iadd
confirms: round-3#1
```
What holds: the three records the finding named now stand above the fold, each as a quote in the one spelling the rule gives, read in `d0811133` and at `1349c2fc`.

- `pr.md:8` quotes Q4's *Default until answered* cell, *the cases keep the paths of the commits they fetch, and their agent type becomes `agentic:proofer`*. `frame/questions.md:22` holds those words in that column, and Q4's *Status* still reads `open`, as `pr.md:7`'s coordinate says (read).
- `pr.md:14` quotes `frame/design.md` *Scope* item 6. Its words stand at `frame/design.md:51`, in item 6 (read).
- `pr.md:15` quotes the first sentence of the *Item* cell of `gaps.md:13`, whose *Who must answer* cell reads *the orchestrator, after the release is installed*, which the coordinate names (read).

The lines are the finding's paste-ready text, word for word. Their place differs from the finding's instruction in one respect: the *Scope* item 6 line and the `gaps.md` line stand after the line that quotes the first row of *Judgments of the run*, `pr.md:13`, not after the 0.39.x warning. The finding's instruction named the line that finding 2's fix adds after line 8, and finding 2 adds no line there: it adds the repair line before the warning. No rule orders the quotes of `pr.md`, so the place changes nothing a reader acts on. `pr.md:15`, that the install path is unverified in a real session, now stands above the fold beside `changelog.md:4`, which says an installed 0.39.x takes this release through `/agentic:update` with no new registration. The two do not contradict each other: one states the design and the other states what no case has run.

```iadd
confirms: round-3#2
```
What holds: each of the three quotes now carries what its record gives with it, read at `1349c2fc`.

- `pr.md:2` quotes the *Grounds* cell of the row at `frame/plan.md:73`, word for word, and the table's header at `frame/plan.md:68` names that column *Grounds* (read). `pr.md:1` stays.
- `pr.md:9` names the row that opens *Rename the fence `agentic`*, `frame/plan.md:27`, and no other row opens with those words: the next row opens *Rename the fence `agentory`* (read). `pr.md:10` quotes the first sentence of that row's *Failure scenario* cell, and the table's header at `frame/plan.md:19` names that column (read).
- `pr.md:11` quotes the clause of the bullet at `frame/plan.md:61` that gives the repair, `agentic pr-checks remove` and then `agentic pr-checks install`, and `pr.md:12` keeps the warning. Both coordinates name the bullet by its opening words, *Each repository that runs the plugin moves*, which are its bold lead-in (read).

The fix also took out the coordinate words *the row rejected* of the old `pr.md:7`, which round 3 judged ambiguous. So no line of `pr.md` now says that the fence's rename was rejected. The owner reads the alternative and its failure scenario under the coordinate *Alternatives considered*, and `changelog.md:3`, above the fold, says the info string `iadd` keeps IADD's spelling. So the outcome is stated above the fold, and no line tells the owner something wrong. The line reads more thinly than it did, as round 3's confirmation said of `pr.md:3` on Q2, and the round opens no finding on it. If the orchestrator wants the verdict itself above the fold, the line below after `pr.md:9` does it. `agentic pr-body` accepted it in the clone with exit 0 (executed; `## Probes`):

```markdown
- "rejected" (`frame/plan.md` *Alternatives considered*, the row that opens *Rename the fence `agentic`*, *Verdict*)
```

```iadd
confirms: round-3#3
```
What holds: `frame/plan.md:74` and `:75` are the finding's paste-ready rows, word for word (read, `git diff 193aba58..d0811133`). They no longer disagree with each other or with the rule they cite.

- `frame/plan.md:74` says round 3 reads `pr.md` with *the two rows its commit adds to this table*. `git show 193aba58 -- frame/plan.md` adds two rows, the title's row at `:73` and the row at `:74` itself, and no other (executed). Its claim that the broad run at `7e36d5cf` stands holds at `1349c2fc`: every commit after `7e36d5cf` changes only this work item's records (executed, `git diff --stat 7e36d5cf..1349c2fc`), `trail/gate.md` reads `run: 7e36d5cf against 801465cb`, and the chain check printed no line on the broad run (executed).
- `frame/plan.md:75` says the rounds over the build end after round 2, and that round 3 reads `pr.md` and the table's rows on it and no fix of the build. Round 3's target, `193aba58 against 7e36d5cf`, is that range. This round reads only fixes of the records, so the row holds beside it.
- `grep -rn -F 'round 3'` over the work item's directory at `1349c2fc` prints only `frame/plan.md:74`, `:75` and lines of `trail/rounds/round-3.md` (executed). The search is a sample under contract rules 12 and 19, since a statement of the same fact in other words escapes it. No line it printed says the rounds end after round 3 or that a broad run is owed. Round 3's own prose says what comes due once its findings close is the inspector's spawn, which was true of its target and stays as history.

What matched: `bin/agentic pr-body agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it --body <scratch>/body.md` in the clone at `1349c2fc` exited 0. The body opens with `pr.md`'s fifteen quote lines, then the `Closes`, `Part of` and attribution lines, then `## From the records` and the changelog fragment (executed). `pr.md` still holds no sentence of the orchestrator's own, no heading and no bold lead-in. It quotes no sentence of `changelog.md` and carries no broad-run figure (read, `pr.md:1-20`).

What matched: no sentence of the work item's records that state the present is contradicted by `d0811133`. `frame/design.md` is unchanged in the range, and its coordinates are dated to `1790fab7` (read). `gaps.md`, `routing.md`, `changelog.md` and `frame/questions.md` are unchanged in the range, and the quotes `pr.md` takes from them stand in them at `1349c2fc` (read; `agentic pr-body` exit 0, executed).

The round leaves nothing open. The fix of round 3 changes only this work item's records, so no broad run is owed again. What comes due is `agentic pr-body` on the body file and the inspector's spawn.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the broad run at `7e36d5cf` passed: the full suite, the repository-wide lint and the format check of `agentory/config.json`'s `Broad gate` key, under contract rule 2 | `trail/gate.md` | the orchestrator, from the run's exit code |
| Whether the hand-written proofer cases still reach their graders under `agentic:proofer` | `frame/questions.md` Q4 | a measurement, `evals/scripts/noninferiority.py run` |
| Whether `/plugin install agentic@agenticseal`, `/agentic:update` and the `agentic:` agent types work in a real session | `gaps.md` *Not verified*, its last row | the orchestrator, after the release is installed |
| The build, the phase records, and rounds 1, 2 and 3's reads outside `193aba58..1349c2fc`, which the prompt left out of this round | `801465cb..193aba58` | rounds 1 to 3, already closed |

## Probes

| Command | Result |
|---|---|
| `bin/agentic pr-body agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it --body <scratch>/body.md` in the clone at `1349c2fc` | exit 0; the body opens with `pr.md`, then `## From the records` and the changelog fragment |
| the same command with the line `- "rejected" (...)` of round-3#2's confirmation added after `pr.md:9`, in the clone | exit 0; the clone's `pr.md` was restored with `git checkout` and `git status --short` printed nothing |
| `python3 skills/code-review/scripts/chain_check.py --baseline 801465cb --root . --worktree` in the clone at `1349c2fc`, before the record was written | exit 0; one notice that no `inspection.md` stands, none on the broad run, and no line that names `trail/rounds/round-3.md` |
| `git diff --stat 7e36d5cf..1349c2fc` | four files, all under this work item's directory: `frame/plan.md`, `pr.md`, `trail/gate.md`, `trail/rounds/round-3.md` |
| `git show 193aba58 -- agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it/frame/plan.md` | two rows added, the title's row and the row on `pr.md`'s late commit |
