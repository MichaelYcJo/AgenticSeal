# code-review, the orchestrator's half

This file is the orchestrator's: the session that spawns the proofer and the
crafter for each round, verifies what they report and opens the pull request.
It holds the procedure for **running** a review run: spawning each phase's
crafter, obtaining a fix pass, ending the run, writing the pull request
body's first part, and verifying the proofer's report. The steps from the
preflight to the open pull request are
`skills/code-review/gate-to-pull-request.md`'s.

`skills/code-review/SKILL.md` is the other half and holds the review itself:
the two stages, the comparison axes, the probe rules, the cross-session
records and the findings format. The orchestrator reads both. The proofer
opens that one at its first step and never opens this one.

A session orchestrating a review run holds the core once, from the plugin's
`SessionStart` hook where its repository holds an `agentory/` root, and opens
`skills/core/SKILL.md` once where no output opening `IADD core from`
stands in its context.

Every `##` heading here opens with `Orchestrator:`.

## Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer

**Where a crafter builds, each phase of a work item is built by a fresh
`crafter` spawn, and the orchestrator never resumes a crafter across a
phase boundary.** The
orchestrator hands the fresh crafter the phase records the earlier phases
wrote, `trail/phases/phase-N.md`, and a brief in the shape of
`docs/running/the-run.md` *The handoff*: coordinates rather than prose,
each fact labelled. A phase record is written to carry what one phase found
to the next, and a resumed crafter pays its whole earlier context again on
every turn to hold what the record already holds.

**Where `routing.md` answers `Implementation` with `the session`, the
orchestrator builds each phase itself, as the builder of
`skills/implement/SKILL.md` *Procedure*, and spawns no crafter for it.**

**A fix pass resumes the implementer only while the implementer's largest
per-turn context is below 806,241 tokens, and is a fresh `crafter` spawn
otherwise.** The implementer is the orchestrator where `routing.md` answers
`Implementation` with `the session`. In every other route it is the crafter
that made the work item's last build phase or fix pass, also where a fix
the orchestrator wrote after the last round came later. Before the fix
pass, the orchestrator runs
`agentic cost --segments <the implementer's agent-*.jsonl>` on the
implementer's own transcript, the file the harness's task output named, and
reads the largest value of its `context` column. Below the threshold, the
orchestrator resumes the implementer, whose context already holds the files
it wrote, the tests it ran and the grounds it recorded. At the threshold or
above it, the orchestrator spawns a fresh crafter and hands it the round record
and the phase records. The column reads the largest turn, so a compaction
that shrank the implementer's context does not lower the reading: the
orchestrator then spawns fresh where a resume was possible, which costs
calls and never a wrong tree.

A fix pass also takes a fresh spawn where the implementer's session no
longer exists, on a new day or another machine, and the orchestrator hands it
the same records. An orchestrator in a new session reads the routing from
the work item's `routing.md` and asks nothing again before the spawn.

**Where `routing.md` answers `Implementation` with `the session`, the
orchestrator makes each fix pass itself, by
`skills/implement/fix-pass.md`.** The resume threshold and the fresh spawn
above do not apply. The orchestrator appends the close blocks of its own
pass, as `skills/implement/fix-pass.md` *The close blocks, last* states.

**The crafter's fix pass appends one close block to each open finding of
`trail/rounds/round-N.md`, and it edits nothing else in the record**
(`docs/forms/the-round-record.md` *The round record*); it writes no
`trail/phases/phase-N.md` and no `plan.md` row.
**The orchestrator writes no close block of a finding the fix pass answers
where a crafter makes the pass, and its fix-pass prompt leaves every such
block to the crafter.** A close the
orchestrator doubts goes into the verifying round's spawn prompt, since that
round weighs every close. Where the row *No fix that no round reads* of
`skills/core/SKILL.md` *Judgment is not licence to skip a party* gives the
pass to the inspector and no round follows it, the doubt goes into the
inspector's spawn prompt, since the inspector reads that close at step 4 of
`agents/inspector.md`. The orchestrator does not rewrite the block.

**Two commits after the build are yours, not the crafter's**: a fix written after
the last round, and the commit that integrates a sibling's squash. Each one that
changes what the work item ships brings the work item's `changelog.md` along, the
way the crafter's fix pass does.
`docs/layout/the-record-layout.md` *A commit after the build brings its changelog
fragment along* owns that rule. A fix written after the last round makes the
reading `skills/implement/fix-pass.md` *The narrow set, then the read of the
range* binds, before the round or the inspector that reads the fix.

**The fix pass then finds what the fixes left standing.** A fix repairs the
coordinate a finding named, and the fact the finding was about is usually
stated in more than one place, so the other statements survive and arrive as
a later round; that is contract rule 12. A crafter's hand-back carries
the account of its read of its range and the work item's records that
`skills/implement/SKILL.md` *The account of that read quotes its commands
and describes no read in other words* states, each frame or `routing.md`
statement that read names, and the sample of statements across the tree,
as contract rule 12 asks of the party that fixes. The
round that follows reads that account as a claim. Where the hand-back names
a frame or `routing.md` statement, which the fix pass does not edit, the
orchestrator folds each file that holds such a statement, read whole, as
`skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket* states, in a commit of its own, before it spawns the verifying
round, so the round and the next crafter read one rule. Last, the fix pass
appends the close block of every finding it answered, after its fix
commits and the corrections its read made, because a `fixed` verdict names
a commit that already exists, and leaves the round record uncommitted. A
hand-back that leaves a finding open for the fold, as
`skills/implement/fix-pass.md` *A fix that needs a unit the frame does not
name waits for the fold* has it, ends no pass: the orchestrator sends the
finding to the framer, commits the fold, or its row that records the
framer's rejection, and resumes the fix pass, or spawns it fresh by the
threshold above. **On the hand-back that leaves no
finding open for a fold, and at the end of its own pass where it leaves
none open, the orchestrator commits the round record as the fix pass left
it, in one commit for the whole pass, before it reads whether a round
follows the pass, and changes none of its lines.** That commit holds
`trail/rounds/round-N.md` alone.

**You type only the half of a spawn prompt that changes between rounds.**
`skills/agent-contract/SKILL.md` reaches every agent you spawn at startup,
through the `skills:` list in its definition, and each agent's own half is in
`agents/<name>.md`. So the prompt holds what is specific to this round and
nothing else.

**That contract binds you too**, by the rules step 1 of
`skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket* names, which is where you open it.

## Orchestrator: the run ends with a verifying round

A round's findings are closed after it ends, by whoever writes the fixes. Every
round but the last has a reader for those fixes: the round that follows, which
answers each of its verdicts. The last round's fixes have none unless a round
is spawned for them, except a fix pass that the row *No fix that no round
reads* of `skills/core/SKILL.md` *Judgment is not licence to skip a party*
gives to the inspector: no round follows that pass, and the check passes its
`fixed <commit>` in the last record.

So a run ends with a **verifying round**, and three things define it.

| Property | What |
|---|---|
| When | **after the fixes** for the previous round are committed, never before, or it reviews what has already been reviewed; no round follows a fix pass that the row *No fix that no round reads* of `skills/core/SKILL.md` *Judgment is not licence to skip a party* gives to the inspector |
| Target | the **diff of those fixes**, not the branch, for the code it reviews. That is what keeps it bounded, and bounded is not cheap: its cost is set by the frame, the inherited records and the probes, so it runs close to a finding round. `agents/proofer.md` *Rules* states the bound, in the rule opening **A verifying round answers the closed findings**, and the read of the work item's records that stands beside the bound, in the rule opening **Every round reads the work item's records that state the present** |
| Job | the answers, not new findings. The round answers each finding the previous round closed `fixed <commit>` or `rejected`, as `skills/code-review/SKILL.md` *Earlier rounds* states |

**Whether a round follows a fix pass is read off the chain check, not
judged by eye.** Once it has committed the pass's round record, the
orchestrator runs the read the proofer runs before it hands back,
`python3 skills/code-review/scripts/chain_check.py --baseline <base>
--root <the branch worktree> --worktree`. Where its output names that
record with the words `skills/code-review/scripts/chain_check.py#VERIFYING_ROUND`
holds, "a verifying round is owed", a round reads the pass, and the
orchestrator spawns it, since the run does not end on a fix that the row
*No fix that no round reads* of `skills/core/SKILL.md` *Judgment is not
licence to skip a party* gives to a round. Where a line names that record
with other words, the check could not read the record as the pass left
it. The orchestrator has the party that wrote the named line repair it,
the fix pass where the line is a close block and the proofer where it is
the finding's own block, and runs the read again. Where no line of its
output names that record, no round follows the pass, and the orchestrator
opens `skills/code-review/gate-to-pull-request.md`.

**You end the rounds when they stop paying.** Which rounds count, the
three finding rounds at which the weighing is owed and which are no cap,
and where the count starts again are `docs/running/the-run.md` *The run*'s.
At that point, and at any round where a signal below shows, you weigh what
the next round can catch against what it costs:

| | What |
|---|---|
| The signals that the run is not converging | a round finds as many findings as the one before it, or more; a finding carries a `regression:` line; one kind of finding returns with a new instance, each fix pass having fixed the coordinate it was handed; a fix adds a mechanism, a check, a mark or a grammar rule, in place of removing a cause |
| What the next round can catch | what the diff of the last fixes can break, because that diff is the round's target (the *Target* row above), and a sentence of the work item's records that the fixes made false. A fix that changes no assertion, such as a test's comment or its name, can be caught out only on its own wording |
| What going on costs | a round close to a finding round's price, since the frame, the inherited records and the probes set it |
| What stopping costs | each open finding a home somebody acts on, by the homes *The run* gives, and a defect the release ships where the home is nobody's |

A fix that changes no assertion owes no round of its own where another fix
already owes one: it rides in that fix pass, and that pass's verifying
round reads it. This weighs what a round costs and changes no invariant.

The verifying round a regression's fix pass is owed whatever the count, and
the row of `frame/plan.md` *Judgments of the run* that each decision to go
on or to stop takes, are *The run*'s too. That round is not owed where the
row *No fix that no round reads* of `skills/core/SKILL.md` *Judgment is not
licence to skip a party* gives the pass to the inspector. When you stop, every
finding still open takes a home: you append its close block, its `verdict:`
reading `deferred <home>` and its `answer:` saying why the run stopped there,
and commit the close blocks of that step together.

**A row that judges the run excessive binds every row after it.** Its
grounds name what the next round could catch and what it would cost. From
that row on, a `must` gets its fix pass, and its verifying round unless the
core's row gives that pass to the inspector. Every
other finding takes a home that costs no round: rung 2, 3 or 4 of the homes
*The run* gives, where you append its close block reading
`deferred <home>` and spawn no fix pass for it, or a fix that the row *No
fix that no round reads* of `skills/core/SKILL.md` *Judgment is not licence
to skip a party* gives to the inspector. Rung 3 is such a home as a new issue,
and as an `agentory/follow-up.md` row only where a round is still to come after
the row's commit, because its commit after the last round costs a round
(`skills/implement/orchestration.md` *Orchestrator: drain the rows before
the broad run, and keep the records*). A later row spends no round on
a finding that is not a `must`, whatever document it cites. The first row
of `skills/implement/orchestration.md` *Orchestrator: drain the rows before
the broad run, and keep the records* and rung 1 of *The run*'s homes are
among those documents, because the stop row has already weighed that fix
against the round it costs. A finding with a `regression:` line is no
exception: from the stop row on, you route a `must` alone by *A regression
is routed by comparing the fix with the frame* below, and every other
regression takes a home that costs no round, as every other finding does,
never a fix pass and never the framer, whose redesign would end the stop.
Only a design change ends the stop, and the count starts again at the
first finding round that reviews the new design. A repair that the
inspector's withheld verdict asks for is no finding and takes no row, so the
stop does not reach it. A round reads that repair unless the core's row
gives it to the inspector.

**Where the signal is one mechanism whose edges each fix pass chased, the next
fix pass decides what the mechanism reads, and takes no further edge.** That is
the core's question for this signal (`skills/core/SKILL.md` *The rule a
mechanism is kept against*). The fix states the rule the mechanism decides by.
Where its inputs are a closed set, such as a parser's kinds or the guards of
one function, the fix enumerates them, pins each with one case, and answers
any other input by naming the form it takes. Where they are open, such as the
shapes a merge's status can take, a list of them is one more edge to chase:
the fix, and every sentence about it, states the rule and lists no kinds. A
list grows in prose as it does in code: a limits paragraph, a comment or a
record that names the shapes one by one gains one shape per fix pass, and
each shape it names is a sentence the next round contradicts with the shape
beside it. A shape that was measured is cited as an example of the rule and
named as one, and a sentence about the examples writes no count and no
universal contract rule 19 refuses. The signal shows at the first fix pass
that adds a shape, and the weighing is owed there, not at the round after.
Where deciding it is a rebuild the issue did not ask for, the mechanism leaves
as its own issue and the branch keeps the release's reading of it, so the run
reads no edge the release did not have. The row that decides either names the
next verifying round as the run's last.

The condition is not *this round found nothing*, which would be unbounded. A
verifying round that raises a `should` finding the crafter closes `rejected`,
with its grounds, has opened nothing needing a fix, and it does not count.
Its record is still not the last one: the check refuses a `rejected`
finding in the last record, and a `fixed` one that the row *No fix that no
round reads* of `skills/core/SKILL.md` *Judgment is not licence to skip a
party* gives to a round, so one more verifying round
reads that answer alone, and answers it as `skills/code-review/SKILL.md`
*Earlier rounds* states. A finding of that round that carries a `reopens:`
line gets its fix pass, and one more verifying round unless the core's row
gives that pass to the inspector; a round carrying a
`regression:` line is routed as the section below says, and where the work
item returns to its framer the run goes on with the redesign. The run ends
only on a round whose record holds no finding without a close block, no
`rejected` one, and no `fixed` one the core's row gives to a round, and
whose `target:` commit is HEAD, or is followed only by commits the core's
row gives to the inspector (a verifying round, or the round you stopped at,
whose open findings took their homes), since the check refuses a ready pull
request whose last record fails either. A fix committed after that round
that the core's row gives to a round, a leftover whose home is the diff
among them, is followed by one more verifying round.

### A regression is routed by comparing the fix with the frame

**The route comes first, because a stop that names no exit is a wall.** A
finding's `regression:` line routes nothing by itself. Its grounds hold one
sentence comparing the fix with the frame, as `skills/code-review/SKILL.md`
*Earlier rounds* states, and you route the round on that sentence
(`docs/running/the-run.md` *The run*). Once a
row has judged the run excessive, only a `must` takes a route below, and
any other regression takes a home by the paragraph opening **A row that
judges the run excessive binds every row after it**:

| The sentence says | The route |
|---|---|
| the fix built the phase's `plan.md` row and `frame/design.md` as written, and the defect stands anyway | no fix pass; the work item goes back to its framer, by the steps below |
| the fix did something the frame does not say, or the defect is in how it was written, a review record's paste-ready fix applied as given among them | an ordinary fix pass, with the crafter told what the frame says; where what the fix did is add a unit the frame does not hold, the framer's fold designs the unit before that fix pass, as `skills/implement/fix-pass.md` *A fix that needs a unit the frame does not name waits for the fold* states |
| the unit already had a regression routed to a fix pass in this run | the signal that the frame is wrong whatever the sentence reads: the framer, by the steps below, unless you can write, as the grounds of a row in `frame/plan.md` *Judgments of the run*, why the frame holds and the fix alone was wrong |

Each route is a judgment, and you write it as one row of that table: the
regression it answers and the route as the judgment, the comparison as its
grounds, and *The run* as the document.

The framer's route:

| Step | What |
|---|---|
| The record | you append a close block to every open finding, its `verdict:` reading `deferred the frame` and its `answer:` naming the regression that sent the work item back, and commit every such block in one commit |
| The framer | spawned again with the run's round records as its input; they are in the tree, so the prompt names them and carries nothing else. It rewrites `plan.md` (new phase rows; a closed phase keeps its commit) and `frame/design.md` where the scope moves, and adds the `Reframed` line under the `Framed` line, spelt as `docs/running/the-run.md` *The run* spells it. Where `routing.md` answers `Automation` with `yes`, the spawn asks nobody |
| The redesign | you approve it when you spawn `crafter` for it; the spawn is the approval. It is then built and reviewed, and its first finding round starts the count again |

## Orchestrator: the pull request opens once the work item is cleared

**The pull request opens ready, once the work item is cleared, and CI runs
then.** Where `Destination` reads `open the pull request`, push the branch as
often as you like while the work is built and reviewed: a branch with no
pull request runs nothing. Under `stop before the pull request` nothing is
pushed, and the branch is handed back committed and unpushed. The steps
from the preflight to the open pull request are
`skills/code-review/gate-to-pull-request.md` *Orchestrator: from the
preflight to the open pull request*'s.

**A conflict with the base is integrated by merging the base into the
branch, never by a rebase.** A work item's branch is not rebased for any
reason, because a rebase orphans the commits every round record names on
its `target:` line. The orchestrator merges once, after the branch whose
changes conflict with this one has landed on the base. Where a work item's
`frame/plan.md` *Overlap with the release* orders this branch after another
work item, the orchestrator merges the base into this branch once that item
has landed, before this branch's next round, or before its broad run where
its rounds have ended. So a round already owed reads the resolution, and
the broad run and the inspector read the merged tree once. Where the merge
resolved a conflict in a file outside the work item's records, the
orchestrator spawns a verifying round on that resolution, because the chain
check lists the branch's commits with `--no-merges` and reads no merge commit
(`skills/code-review/scripts/chain_check.py#follows`). The merge moves HEAD
past `trail/gate.md` and `inspection.md`, so after the merge, and after that
verifying round's record is committed where one is owed, the orchestrator
runs the broad gate again, commits its record, runs `agentic pr-body` on the
body file again and spawns the inspector again.

**A commit after the newest broad run that changes only files under
`agentory/threads/<work-item-id>/` owes no broad run.** Where such a commit
changes a record other than `trail/gate.md` and `inspection.md` after the
inspector has written its verdict, it owes `agentic pr-body` on the body file
again and the inspector again, and the inspector reads every record at HEAD.
Those two files may follow the verdict's commit, as the inspection arm
reads it (`skills/code-review/scripts/chain_check.py#CLOSING_RECORDS`), so
their commits owe neither another broad run nor another inspector. A commit
that changes any other path owes the broad run again, after the round that
the row *No fix that no round reads* of `skills/core/SKILL.md` *Judgment
is not licence to skip a party* gives it.
`agents/inspector.md` step 1 and the pull request check's broad gate arm read
the same rule over the branch's own commits
(`skills/code-review/scripts/chain_check.py#follows`), so neither reads a
merge, which the paragraph above holds to its own rule. What a `Broad gate`
command that reads the records misses then is `templates/setup/config.md`
*Broad gate*'s.

**Where the work's risk is platform-specific, run the other platforms before
the broad run.** Line endings, the shell and the Python version are such
risks. Push the branch once the build's last phase closes and run
`gh workflow run tests --ref <branch>`, then read that run's result before
you take the broad run. That run is a `workflow_dispatch` run of `tests`.
Its cases see what a `pull_request` run's cases see, because
`tests/conftest.py` removes every `GITHUB_` variable at import. It cannot
have a pull request's merge commit, or the `hygiene` workflow, which starts
only on a `pull_request` event. A leg that fails there is a defect like any a round
finds, and it is repaired before the rounds settle. Under `stop before the
pull request` push nothing: name the platform risk in the hand-back, for
whoever opens the pull request.

**The pull request body's first part is the work item's `pr.md`, opened by
its `pr.<lang>.md` where the two language keys differ, as the paragraph on
`pr.<lang>.md` below says. The orchestrator writes `pr.md` once the build's
last phase has closed and commits it before it spawns the first round.**
Where no round runs, the orchestrator writes it before the broad run.
Every round reads `pr.md` at its target, so no sentence of the body
reaches the inspector unread. `pr.md` holds the `Closes` and `Part of` lines,
quotes of the work item's records, and the attribution line. `pr.md` quotes
no sentence of `changelog.md`, because `agentic pr-body` writes the fragment
whole under the line `skills/code-review/scripts/pr_body.py#HEADING` holds,
above the fold, so the reader meets it there and a fix to a changelog
sentence touches no `pr.md`. A quote is one line in one spelling,
``- "<the sentence>" (`<path>` <coordinate>)``, where `<path>` is the
record's path under the work item's directory and `<coordinate>` the
heading, row, finding or line that holds the sentence, and `agentic pr-body`
refuses a quote whose words, with runs of whitespace collapsed, do not
stand in the file its path names
(`skills/code-review/scripts/pr_body.py#first_part`). The orchestrator
opens that record when it writes the quote. `pr.md` holds no sentence of
the orchestrator's own account: no sentence frames a quote or joins two,
and no heading or bold lead-in of the orchestrator's stands in it. What
the owner must see before the fold is quoted from the record that holds
it, and a decision quoted from a table row is quoted with the cell of the
same row that names what was decided: two quote lines, the naming cell's
first and the decision's on the next line, with no sentence joining them.
A default taken where `routing.md` reads `Automation` `yes` is quoted from
its `frame/questions.md` row as the `Question` cell, then the `Default
until answered` cell, or the `Status` cell once the row is answered. The
framer's judgment left after the exchange is quoted from its
`frame/plan.md` *Alternatives considered* row as the `Approach` cell, then
the `Verdict` cell. Why the title takes its prefix is quoted from the
orchestrator's row of `frame/plan.md` *Judgments of the run*, which it
writes before `pr.md`, as the `Judgment` cell, then the `Grounds` cell.
The orchestrator writes each row of *Judgments of the run* with a
`Judgment` cell that names the question the judgment answers, then its
answer, as `templates/records/sdd-plan.md` asks. The broad run's
printed figures, a CI run taken after the rounds and the run's comparison
table come after the last round, so none stands in `pr.md`: the copy
carries `trail/gate.md`'s `run:` line, and the table goes to the flow log's
comment alone (`skills/verify/orchestration.md` *Measure the run, and
feed the flow log*).

**Where `config.json`'s `Commit and pull request language` and `Record
language` keys name different languages, the orchestrator writes
`pr.<lang>.md` beside `pr.md` and commits the two together.** It holds
sentences rendered in `Commit and pull request language`, each followed by
its coordinate in the shape a quote of `pr.md` carries one. First comes the
sentence that opens each list item of the work item's `changelog.md`, in
the fragment's order. Then comes each quote of `pr.md`, in `pr.md`'s order,
with the coordinate the quote carries in `pr.md`. It holds nothing else. It
renders no other sentence of the fragment, which stands whole in `Record
language` under the line `skills/code-review/scripts/pr_body.py#HEADING`
holds, above the fold. It holds no `Closes`, `Part of` or attribution line,
which `pr.md` already holds in that language, and no sentence of the
orchestrator's own. `<lang>` is the orchestrator's spelling for the file's
own language, the commit language, such as `ko`. `agentic pr-body` writes it
above `pr.md`, so the body opens in the team's language, and every round
reads it whole beside `pr.md`. Where the two keys name one language, no
`pr.<lang>.md` is written.

**Where a fix pass or a fold changes a sentence that `pr.<lang>.md`
renders, the orchestrator rewrites each rendering that stood on it, and
commits them before it spawns the next round.** A quote of `pr.md` whose
sentence changed is rewritten where `agentic pr-body` refuses it, or earlier
where a hand-back names it or the plugin's `PostToolUse` hook,
`hooks/edit-leaves-copies.py`, names it after the edit of its source. A
round finding located in `pr.md` or `pr.<lang>.md` is the orchestrator's
to repair, since no crafter writes either: the orchestrator commits the
repair before the fix pass, and the pass's close block reads
`fixed <that commit>`, as for a finding located in a frame file.

**A session that has compacted hands the next round to a fresh one, and the
round record is the handoff.** A compacted context holds a summary of what
it read, and a round run from a summary either re-reads what the summary
dropped or trusts it. The record carries the target, the verdicts and the
probes as the reviewer wrote them, so the fresh session opens the record and
its coordinates rather than the summary.

## Orchestrator: verify before posting

Never post the proofer's output as it stands. Check, by opening the
coordinates yourself:

1. The coordinates behind every highest-severity finding, because those are
   the heaviest to act on and the hardest to retract.
2. Every claim that a state can occur, because a constraint, an enum or a
   default may forbid the state.
3. Citations of a policy's or a design's clauses, because clause numbers move
   while a review runs.
4. Test-pass claims: run them, and count the skips, which read as passes.

Also check whether HEAD moved during the review; if source changed, those
verdicts need a re-pass, and the next round's `target:` line names the new HEAD.
