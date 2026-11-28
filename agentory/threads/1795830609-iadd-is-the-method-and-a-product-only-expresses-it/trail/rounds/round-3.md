# Review round 3: 1795830609-iadd-is-the-method-and-a-product-only-expresses-it

```iadd
target: 193aba58 against 7e36d5cf
```

The round reads what rounds 1 and 2 did not: the range `7e36d5cf..193aba58`. `git diff --stat 7e36d5cf..193aba58` names three files of the work item's directory and no other path: `pr.md`, added whole in `193aba58`; two rows of `frame/plan.md` *Judgments of the run*, lines 73 and 74, added in the same commit; and `trail/gate.md`, added in `f418b999`, read only for its claims. No fix pass ran after round 2, which closed no finding, so no `confirms:`, `regression:` or `reopens:` line is owed and this round is no verifying round. The prompt narrowed the round to that range and asked for no review of the build, and the round followed it under contract rule 3.

The round read the work item's `routing.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md` whole at `193aba58`, `frame/design.md` *Grounding* and *Scope* whole and its other sections for the sentences `pr.md` could quote, the five phase records for what they say of `pr.md`, the rounds and the broad run, and rounds 1 and 2 whole. No `pr.<lang>.md` stands, and none is owed: `agentory/config.json` names English for both `Commit and pull request language` and `Record language`. `agentory/parity.json` is absent, so no parity comparison is owed. Runs went in a `git clone --no-local` at `193aba58` under `<scratchpad>/1795830609-iadd-is-the-method-and-a-product-only-expresses-it/round-3/clone`. Nothing in the checkout changed but this record.

Carried from round 2, not re-established: the base `801465cb`, #1656's merge on the release branch, and the fact that `agentory/threads/` holds no other work item of the release but #1656's, whose `## Rule changes` is `- nothing`. `git rev-parse --short origin/release/v0.40.0` printed `801465cb` at this round too (executed). Every verdict below is this round's own.

The rule `pr.md` is judged against is `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the work item is cleared*, its paragraph on `pr.md`. `agentic pr-body` composed the body from the clone and exited 0, and the body opens with `pr.md`, then `## From the records`, then the changelog fragment, and then the `<details>` fold (executed). So above the fold the owner reads `pr.md` and this work item's `changelog.md`, and nothing else. Everything else `pr-body` copies, `gaps.md`'s `## Not verified` and `## Not done` and every table line of `frame/questions.md` among it, stands inside the fold. The findings below weigh the selection against that.

## Findings

### 1. `pr.md` leaves out three records the owner must see before the fold: Q4's default taken, the install path no case runs, and the rewrite of #1656's release-note entry

```iadd
severity: should
location: `agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it/pr.md:6-8`
evidence: read `frame/questions.md:22`, `gaps.md:13`, `frame/design.md:51`, `changelog.md:1-12`, `pr.md:1-14`; executed `bin/agentic pr-body agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it --body <scratch>/body.md` in the clone at `193aba58`, exit 0, which places `gaps.md` and `frame/questions.md` inside the fold; executed `git grep -l 'agentic:proofer' 193aba58 -- 'evals/behaviour/proofer/replay-*' 'evals/behaviour/proofer/seeded-*'`, which lists 16 files
```

Why it matters: the rule says what the owner must see before the fold is quoted from the record that holds it, and it names *a default taken where `routing.md` reads `Automation` `yes`, from its `frame/questions.md` row* as one such record. `routing.md` reads `Automation` `yes`. Three records the owner would weigh before merging stand only inside the fold at `193aba58`:

- **Q4's default.** `pr.md:6` quotes Q4's question and marks it *open*, and quotes nothing of what the build did meanwhile. `frame/questions.md:22` gives the default *the cases keep the paths of the commits they fetch, and their agent type becomes `agentic:proofer`*, and the tree took it: the hand-written cases under `evals/behaviour/proofer/replay-*` and `seeded-*` name `agentic:proofer` in 16 files at the target. The answerer is *a measurement*, a paid `noninferiority.py run`, and nobody has run it. So the owner reads that a question is open and not that the cases were changed on a default no measurement checked.
- **The install path no case runs.** `gaps.md:13` *Not verified* says no case runs the harness against the renamed manifest and marketplace, so `/plugin install agentic@agenticseal`, `/agentic:update` and the `agentic:` agent types are unverified in a real session until the release is installed. The changelog above the fold says *an installed 0.39.x takes this release through `/agentic:update` with no new registration* (`changelog.md:4`) and does not say that this is unverified.
- **The rewrite of #1656's entry.** `frame/design.md` *Scope* item 6 rewrites #1656's `changelog.md` in place, another work item's entry in the same release's note. This work item's `changelog.md` names #1656 nowhere, and `pr.md` quotes only Q3, the link of that entry, and not that its text changed.

The rule's list of records is examples, not a closed list, so the round judged the rest of the records for what an owner weighs before merging. Q5 is answered by *the work*, and each phase records the names it chose, so its default is the build's and is not added. The second paragraph of `gaps.md` *Not done*, on the range phase 2 did not read to its end, is a limit of a crafter's read that round 1's method covered, and is not added. The `## Not verified` rows for the broad gate over each phase are answered by `trail/gate.md`'s run, and are not added.

In `pr.md`, after line 6, after line 8 and after the line the fix of finding 2 adds after line 8, the lines below. `agentic pr-body` accepted each in the clone with exit 0, and refused a copy of the first with one word changed, at its line, with exit 1 (executed; `## Probes`):

```markdown
- "the cases keep the paths of the commits they fetch, and their agent type becomes `agentic:proofer`" (`frame/questions.md` Q4, *Default until answered*)
```

```markdown
- "#1656's `changelog.md` is rewritten in place where it states a product's or a place's name, and its other files stay byte for byte." (`frame/design.md` *Scope* item 6)
- "Whether `/plugin install agentic@agenticseal`, `/agentic:update` and the `agentic:` agent types work in a real session once the release that carries this work is installed." (`gaps.md` *Not verified*, the row the orchestrator answers after the release is installed)
```

### 2. Three quotes of `pr.md` carry a verdict or a warning and leave out what the record gives with it: the title's grounds, the fence's reason and the 0.39.x copy's repair

```iadd
severity: should
location: `agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it/pr.md:1`, `agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it/pr.md:7`, `agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it/pr.md:8`
evidence: read `frame/plan.md:27`, `frame/plan.md:61`, `frame/plan.md:73`, `skills/code-review/orchestration.md:374-380`; executed `bin/agentic pr-body` on the corrected `pr.md` in the clone, exit 0
```

Why it matters: each of the three lines quotes the part of a record that the owner can least act on alone.

- `pr.md:1` quotes the *Judgment* cell of `frame/plan.md:73`, *The title takes `feat:`*. The rule asks for *why the title takes its prefix*, and the why is the row's *Grounds* cell. The title itself already shows `feat:`, so the line tells the owner nothing the title does not.
- `pr.md:7` quotes the *Approach* cell of `frame/plan.md:27`, *Rename the fence `agentic`, the product's name*. That it was rejected stands only in the coordinate's words *the row rejected*, which are the orchestrator's, and why it was rejected stands nowhere above the fold. The row's *Failure scenario* cell gives the reason. The coordinate *the row rejected* also fits each rejected row of the table; the quote's words pick the row, and the corrected coordinate names it.
- `pr.md:8` quotes the warning from the bullet of `frame/plan.md:61` that a 0.39.x copy whose tag alone moves runs `seal.py`. It leaves out the repair that the same bullet gives one sentence before, `agentic pr-checks remove` and then `agentic pr-checks install`, which round 1's finding 1 put there. Read alone, the line says a repository breaks and not what it does.

Each line below was read in its record at `193aba58`, and `agentic pr-body` accepted all of them in the clone with exit 0 (executed). `pr.md:1` stays and is followed by the first line. `pr.md:7` is replaced by the second and third. `pr.md:8` is preceded by the fourth and its coordinate takes the bullet:

```markdown
- "The pull request changes what the plugin is called, what its command and its root are named, and how a repository at 0.39.x moves, and #1658 is titled `feat:`" (`frame/plan.md` *Judgments of the run*, the row that opens *The title takes*, *Grounds*)
```

```markdown
- "Rename the fence `agentic`, the product's name" (`frame/plan.md` *Alternatives considered*, the row that opens *Rename the fence `agentic`*)
- "a record form would carry one product's name, where `docs/method/iadd.md` *The record forms* lists the forms as the method's and #1658 keeps the records' vocabulary (G14)" (`frame/plan.md` *Alternatives considered*, the row that opens *Rename the fence `agentic`*, *Failure scenario*)
```

```markdown
- "`.github/workflows/hygiene.yml` written again by `agentic pr-checks remove` and then `agentic pr-checks install`, pinned to the release that carries this work." (`frame/plan.md` *Operational impact*, the bullet that opens *Each repository that runs the plugin moves*)
- "A 0.39.x copy whose tag alone moves still runs `skills/implement/scripts/seal.py` in its mode step, which this release does not ship." (`frame/plan.md` *Operational impact*, the bullet that opens *Each repository that runs the plugin moves*)
```

### 3. The plan's new row says a verifying round reads `pr.md` before the broad run is taken again, beside an older row that says the rounds end after round 2, and no broad run is owed

```iadd
severity: should
location: `agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it/frame/plan.md:74`, `agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it/frame/plan.md:75`
evidence: executed `grep -rn -F 'after round 2' agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it` and `grep -rn -F 'broad run is taken again' agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it` at `193aba58`, which print `frame/plan.md:74` and `:75`, and `:74` alone; executed `git diff --stat 7e36d5cf..193aba58`; executed `python3 skills/code-review/scripts/chain_check.py --baseline 801465cb --root . --worktree` in the clone, exit 0, with no notice on the broad run; read `skills/code-review/orchestration.md:322-330`, `agents/proofer.md:141-144` *A verifying round answers the closed findings*
```

Why it matters: the inspector and the settle read these rows as the run's judgments, and the two rows disagree with each other and with the rule they cite.

- `frame/plan.md:75` says *The rounds end after round 2*. `frame/plan.md:74`, added in `193aba58`, orders a round after round 2. The two rows state when the rounds end in two ways, and contract rule 19 asks a change to rewrite the text it amends in place.
- `frame/plan.md:74` says the round comes *before the broad run is taken again*. `skills/code-review/orchestration.md` says a commit after the newest broad run that changes only files under `agentory/threads/<work-item-id>/` owes no broad run. `7e36d5cf..193aba58` changes only this work item's records, and so does this round's record, and the chain check reads the broad run at `7e36d5cf` as standing. So the row either names a run the rule does not ask for, which spends the suite again, or names an act that will not happen.
- `frame/plan.md:74` calls the round *a verifying round*. A verifying round answers the findings the round before closed, and round 2 closed none. Its grounds also say the round is *over `pr.md` alone*, where the same commit adds the two rows this round reads.

The search is a sample under contract rules 12 and 19, since a statement of the same fact in other words escapes it. It printed nothing outside these two rows. Round 2's record says *What comes due is the orchestrator's broad run*, which was true of `6b77bf02` and stays as history.

In `frame/plan.md`, lines 74 and 75:

```markdown
| 2026-11-28 | `pr.md` is committed after round 2, and round 3 reads it with the two rows its commit adds to this table | The orchestrator wrote no `pr.md` before round 1, which the rule asks for so that every round reads the body; a round over that commit gives it the read it missed. The commit changes only this work item's records, so the broad run at `7e36d5cf` stands and owes no second run | `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the work item is cleared* |
| 2026-11-28 | The rounds over the build end after round 2 | Round 2, the verifying round over round 1's fixes, confirmed all three closes and opened no finding. Round 3 reads `pr.md` and this table's rows on it, and no fix of the build | `skills/code-review/orchestration.md` *the run ends with a verifying round* |
```

## Confirmations

What matched: the `Closes` and `Part of` lines. `pr.md:11` reads `Closes #1658.`, and #1658 is this work item's issue, open, titled `feat:` (`gh issue view 1658`, executed). `pr.md:12` reads `Part of #1651.`, and #1651 is open and is not done by this pull request alone: its *Order* step 3 moves CodeChallenge after the release, and #1658's body ends `Part of #1651.` (`gh issue view 1651`, `gh issue view 1658`, executed). Neither line is copied from a record, and the composed body holds no other closing keyword (executed: `agentic pr-body` exit 0).

What matched: `pr.md` holds no sentence of the orchestrator's own. Every line but `Closes`, `Part of` and the attribution line is a quote in the one spelling the rule gives, ``- "<sentence>" (`<path>` <coordinate>)``, with no heading, no bold lead-in and no sentence that frames or joins two quotes (read, `pr.md:1-14`). It quotes no sentence of `changelog.md`, and it carries no broad-run figure (read). The attribution line is the one the session's attribution names.

What matched: each coordinate names the place that holds its sentence, read at `193aba58`. `pr.md:1` names the row at `frame/plan.md:73`. `pr.md:2` names Q1's *Question* cell at `frame/questions.md:19`. `pr.md:3` names the *Status* cell, which reads the same in Q1 and Q2, at `frame/questions.md:19-20`. `pr.md:4` and `:5` name Q3 at `frame/questions.md:21`, the question and option (a), which the *Default until answered* cell gives and `frame/plan.md:72` records as taken. `pr.md:6` names Q4 at `frame/questions.md:22`, whose *Status* is `open`. `pr.md:8` names `frame/plan.md` *Operational impact*, whose bullet at line 61 holds the sentence. `pr.md:9` names the first row of *Judgments of the run*, `frame/plan.md:70`, and every row there is dated 2026-11-28. `pr.md:7`'s coordinate fits any rejected row, and finding 2 gives it the row's opening words.

What matched: `pr.md:3` names Q2 in its coordinate, and no line of `pr.md` quotes Q2's question, and neither Q1's nor Q2's option (a) is quoted. Q1's answer stands above the fold in `changelog.md:4`, which gives the display name `agentic` and the description sentence, and Q2's answer (a) leaves `TRADEMARKS.md`, `LICENSE` and the emblem's text as they are. Both are the owner's own answers, so the line reads thinly and misleads nobody, and the round opens no finding on it.

What matched: `frame/plan.md:73`, the title's row. Its grounds hold: #1658's title opens `feat:` (executed, `gh issue view 1658`), and the row's grounds match `skills/commit-pr-convention/SKILL.md:131`, where `feat:` is something new to use or to meet, such as a command (read). The pull request renames the command, the root and the plugin's display name, which a person meets.

What matched: `trail/gate.md` holds one block, `run: 7e36d5cf against 801465cb`, in the shape `lib/fields.py:216-218` gives a run (read). `7e36d5cf` is the commit before it, and `801465cb` is the merge base with `origin/release/v0.40.0` (executed, `git merge-base`). Every commit after `7e36d5cf` changes only this work item's records (executed, `git diff --stat 7e36d5cf..193aba58`), so the run stands at HEAD as `skills/core/SKILL.md` *Judgment is not licence to skip a party* row *No inspection without the broad run* reads it. The chain check in the clone printed no notice on the broad run (executed). Whether that run passed is the gate's exit code, which the round did not see: `trail/gate.md` holds no figure and, by the rule, none is owed.

The `## Not verified` rows of `gaps.md` for the broad gate over each phase and over the fix pass name the orchestrator at the broad run as their answerer, and `trail/gate.md` now records that run. No rule the round found asks for those rows to be marked `closed` after the run, and the round opens no finding on them.

The round has nothing open beyond its three findings, each located in a file the orchestrator repairs (`skills/code-review/orchestration.md`, the paragraph on a round finding located in `pr.md`). Once they close, `agentic pr-body` runs on the body file again, and what comes due is the inspector's spawn. No broad run is owed again by these repairs, since they change only this work item's records.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the broad run at `7e36d5cf` passed: the full suite, the repository-wide lint and the format check of `agentory/config.json`'s `Broad gate` key, under contract rule 2 | `trail/gate.md` | the orchestrator, from the run's exit code |
| Whether the hand-written proofer cases still reach their graders under `agentic:proofer` | `frame/questions.md` Q4 | a measurement, `evals/scripts/noninferiority.py run` |
| Whether `/plugin install agentic@agenticseal`, `/agentic:update` and the `agentic:` agent types work in a real session | `gaps.md` *Not verified*, its last row | the orchestrator, after the release is installed |
| The build, the phase records and round 1's and round 2's closes, which the prompt left out of this round | `801465cb..7e36d5cf` | rounds 1 and 2, already closed |

## Probes

| Command | Result |
|---|---|
| `bin/agentic pr-body agentory/threads/1795830609-iadd-is-the-method-and-a-product-only-expresses-it --body <scratch>/body.md` in the clone at `193aba58` | exit 0; the body opens with `pr.md`, then `## From the records`, the changelog fragment and `<details>` |
| the same command with `pr.md` replaced by the `pr.md` findings 1 and 2 give, in the clone | exit 0; the clone's `pr.md` was restored with `git checkout` and `git status --short` printed nothing |
| the same command with the Q4 default line's words `agent type` changed to `agent kind`, in the clone | exit 1, refused at `pr.md:8` as a quote of words `frame/questions.md` does not hold; restored, `git status --short` printed nothing |
| `python3 skills/code-review/scripts/chain_check.py --baseline 801465cb --root . --worktree` in the clone at `193aba58`, before the record was written | exit 0; one notice that no `inspection.md` stands, and none on the broad run |
| `git grep -l 'agentic:proofer' 193aba58 -- 'evals/behaviour/proofer/replay-*' 'evals/behaviour/proofer/seeded-*'` | 16 files |
