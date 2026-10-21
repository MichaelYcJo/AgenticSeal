# verify, the orchestrator's half

This file is the orchestrator's: the session that spawns the smith, the
warden and the sealer and takes the one broad run between the last of them.
It holds the two acts of the verify protocol that no agent takes: the broad
gate, and the measurement of each segment posted to the flow log.

`skills/verify/SKILL.md` is the other half: the four conditions every claim
meets, the hand-back's labels, the scope rule and the counterfeits. The
orchestrator reads both. The smith and the sealer open that one and never
this one, because contract §2 gives the broad gate to the orchestrator and
contract §6 withholds posting from every agent.

## The broad gate

**It fires after the review rounds settle, never before them.** Nothing broad
runs at the handoff to review; the hand-back carries the suite as
`unverified`, and that label is what keeps the narrow scope honest.
`skills/verify/SKILL.md` *Scope: cheap and often, broad and once* holds the
reason: a run taken before the rounds is spent by the first finding. Findings
are the expected case rather than the exception: the review chain runs three
finding rounds by default (`docs/the-review-record.md` *The run*).

**"After the rounds settle" is a row, not a moment, and this is the row: the
last `rounds/round-N.md` has no finding open.** The phrase alone names no
particular rounds: a work item has build phases with a progression of their
own and a review chain with its own, so a reader who reaches for the moment
has to guess, and one who reaches for the record does not.

**It belongs to the orchestrator, and the four conditions of
`skills/verify/SKILL.md` are the whole of the run.** No agent runs it:
`broad-gate --base <base> --record <item>` is the command the orchestrator
types, with nothing else running, and `skills/code-review/orchestration.md`
*Orchestrator: the pull request opens once the sealer seals, and a phase is
re-run* owns when, before the sealer is spawned. The run judges no failure
and fixes none; the sealer reads its record, and what it guarantees after it
is `docs/the-review-record.md` *The guarantee*. `broad-gate --preflight`,
which the orchestrator runs before the broad run, is not this run: it runs
the gate's record arms, runs no suite, and writes nothing.

**An expensive suite argues for this placement, not against it.** A run that
takes fifteen minutes is a finding about the run and deserves its own ticket.
Moving it ahead of the rounds means paying it twice.

**Which base, and it is the one the merge is judged by.** The gate resolves
`--base` once, before anything runs, to the ref CI will read: the base's
upstream where the checkout declares one, else `origin/<base>`, else the ref
as given. Every check it runs takes that one commit: the two baselines, the
scratch worktree the base comparison checks out, and `broad-gate.md`. A plain
branch name is a LOCAL ref and a runner has no local branches, so a checkout
one commit behind its remote would pass green where CI refuses the same
commit. Where resolving moves the answer the gate prints one line naming both
refs, both commits and the distance, and runs anyway; where the two agree it
prints nothing. It never fetches, so a remote-tracking ref is only as fresh
as the last fetch, which is why the gate's report names the ref beside the
commit on the `base` row rather than the commit alone, and the `BROAD GATE
PASSED` line names it as `<ref> @ <commit>`.

**What the broad run covers is declared rather than remembered.** The arms
exist so that the one run says what CI will say.
`skills/verify/scripts/broad_gate.py`'s `PARTITION` is the declaration: every
step of the `release` job of `.github/workflows/hygiene.yml` is mirrored by a
named arm or excluded with a written reason, there is no third state, and a
case holds the table against the workflow from both sides. A step added to
the workflow fails the suite until somebody classifies it, and a row naming a
step that was renamed away fails it too.

**A run says what it did not answer.** Where the repository being gated has
that workflow, the panel carries a `CI also` row, *· <n> more steps*, and the
names of those steps go to stderr beside the line that names the
repository's own command, with the total they are counted out of. The dim
`·` is the owner's mark for a row that is not a pass. The count is on the
panel because a panel value is 41 columns and a step name is a sentence; the
names are printed because a number alone sends the reader back to the two
files this declaration exists to stop them opening. A repository with no
such workflow sees neither, and nothing else about its run changes. Both are
counted over the steps CI runs for the base: a step CI does not ask of this
pull request, such as one of SpecSeal's that runs only on a pull request into
`main`, is neither answered nor unanswered, so the count leaves it out and
the line says how many it left out and why.

**What the count does not say** is whether a mirrored arm asks the same
question its step asks. The partition says a step is on the list; two readers
of one question can still disagree about what they are checking. The gate
runs every arm at every base, and a case holds that no mirrored step of
SpecSeal's workflow skips a pull request into `main`; a second case holds
`broad_gate.py#ONLY_AT_MAIN`, the steps that run only into `main`, against
their guard. The cases read a guard on the base and no other kind of
condition, so the class stays open for the next kind.

**The arms the plugin ships are the arms the gate can run.** Two steps of
SpecSeal's own `release` job have a local answer and no arm: one runs a
script under `.github/scripts/`, which no plugin ships, and one is shell
written inline in the workflow with no script either side can share. A
repository that wants checks of its own run names them in the `Broad gate`
row of `seal/config.md`, the row this gate already runs first, rather than
in the arm list of a script that ships to everybody.

A full suite carries failures that were already there. Attributing them to
this work is a wrong finding; passing over them is a silent pass. Both are
avoided the same way: read the run against the base commit.

**That comparison is reactive.** A baseline answers whose failure this is, so
it is taken once an unexplained failure appears, and only for the tests that
failed: `git stash`, that one file, `git stash pop`.

- **Failing on base too**: not this work's finding. Name it, record it as a
  follow-up, and it does not block.
- **New**: this work broke it. Back to the implement and review loop, and the
  broad gate runs again afterwards.
- **New?**, with a reason, means nothing at the base measured it: no pytest
  the `Broad gate` row ran left a record, because the row started no pytest,
  none it started loaded the gate's recorder, or the one that did could not
  write its record and warned in `suite.txt`, so the file is named only by
  a `FAILED` line and the base was not run; no pytest the row ran at the
  base left a record, for any of those three causes, a part before the
  runner failing at the base among them; or the row's run at the base
  exited non-zero before any pytest collected the file, which is also how a
  file the branch added reads where the base's row already fails; or a
  session of the base that ended non-zero left tests or collections out of
  every list, a test whose xdist worker died in its setup among them, so
  the record cannot say the file passed. A session of the base that
  stopped part-way reads the same way: its record holds no `end` line,
  because the process died, which plain pytest does on a test that calls
  `os._exit`, or its recorder stopped writing; or its `end` line names a
  stop pytest made, which an interrupt, any `pytest.exit()`, `-x`,
  `--maxfail` and a plugin's stop all leave, or an exit outside 0, 1 and 5.
  So does a base whose record holds a line that did not parse as the
  recorder's, which the gate counts and passes over. It is a question about the
  file, not a finding either way; open the kept `suite-at-base.txt` and the
  `records/` beside it, and run the file at the base by hand before calling
  it either of the two above.
  A test with no file of its own is in no list at all, nor is a failed
  collection of the whole session or a report a plugin built without its
  path; the failure form says how many there were. Nor, where a session at
  `HEAD` stopped part-way, is the test it stopped in, nor a test named on a
  line of the record that did not parse; the failure form counts both too.
  `templates/config.md` *The criterion for choosing a value*, rule 3, says
  which rows the gate cannot measure and how a row earns the measured word.

Without the comparison, every failure that was already there is triage the
author cannot act on and is not allowed to fix.

**Three returns and stop.** This counts trips through the gate, not the
review chain's rounds. A fourth trip is not another bug; it means the narrow
scope is missing a class of breakage, which is an architecture question for
the user, the same reading as the 3+ Fix Rule.

**Nothing edits between the broad run and the PR.** The tree that passed is
the tree that ships. One more small fix after the run means the run is stale,
and the gate is paid for again.

## Measure the segment, and feed the flow log

After every smith or warden segment ends, the orchestrator measures its
transcript with `skills/verify/scripts/session_cost.py`, typed as
`session-cost`, and posts the numbers, and what they say, as a comment on one
of this repository's two measurement logs. Which of the two is not a filing
detail: one of them is deleted at every release, so a reading put in the
wrong one is a reading thrown away, and the paragraph below is what decides
it.

**There are two logs, and the difference is kind rather than scope.** A
reading about the segment that just ended (its span, its calls, its tools
per turn, and what those say) belongs to the rolling `flow-measurement`
log, which opens at a release, accumulates until the next version ships,
and is discarded by the release that ships it. Readings that span versions
(a rate held against an earlier version's baseline, or an observation that a
later measurement answers) belong to the durable `flow-baseline` log,
which is maintained rather than accumulated. Posting one of those to the
rolling log schedules it for deletion at the next release.

A repository declares each of them the same way, with a label on an issue,
and each keeps the same invariant: exactly one open. Neither is named by
number, because a number goes stale the moment its issue closes.

**One command does the lookup, the four readings below, and the post.**

```
session-cost --segments <the run's transcript> --post --says <file|->
```

It resolves the label rather than a number, `--label flow-baseline` reaches
the durable log with the same code, and it **opens no issue in any state**.
It refuses without `--says`: what the numbers mean is the orchestrator's
sentence to write, and the script writes none. The readings below are what its exits mean,
and they are still worth knowing, because an orchestrator that meets a
refusal has to know which one it hit.

**The command does not make anybody run it.** `--post` removes the procedure
the orchestrator otherwise reconstructs from this section every time; it does
not remove the remembering, and nothing here does.

By hand it is two lookups. Find the rolling log first, with `gh issue list
--label flow-measurement --state open`, rather than assuming a number, and
the durable one the same way with `--label flow-baseline`. Where more than
one is open, treat it the way any broken invariant is treated: name it rather
than guessing which one is current.

**A reading of zero open is two different facts, and one call tells them
apart.** `gh issue list --label flow-measurement --state all` says whether
the label has any history at all:

- **No issue has ever carried it.** This whole section is a no-op: nothing
  is measured, nothing is posted, nothing fails, and nothing asks. Most
  installed repositories never create the label, so most segments end here,
  and that is the expected case, not a missed one.
- **The label has a history and nothing is open.** The log stopped and
  nobody reopened it. Name that in the segment's own handover and stop
  there: **opening one is not a session's act.** Two sessions finishing
  segments at the same moment both read zero and both create, and the next
  release then fails on two or more, the same invariant broken from the
  other side. The release-time script that rolls the log
  (`.github/scripts/roll_flow_measurement_issue.py`, where a repository has
  one) is where that invariant and its reasoning are written.

**`flow-baseline` splits the same way, and for the same reason.** Run the
`--state all` lookup against it too. No issue has ever carried the label and
this repository simply has no durable log: post the segment's own numbers
to the rolling log, and leave the cross-version reading in the record that
would have cited it. The label has a history and nothing is open, and
somebody closed the durable log: name that, in the same handover and on
the same grounds, and open nothing. Folding the second into the first is
what sends a cross-version reading nowhere while everything looks fine.

What a label answers that a milestone cannot, and why tidying one of these
issues by hand breaks the next release, are the tracker's own conventions
rather than this skill's. `docs/issues-and-milestones.md` holds them where a
repository keeps one.

Where a log is open, the orchestrator takes the two steps as part of the
segment that just finished, not as a follow-up someone might do later:

1. Run `session_cost.py --segments` against the **run's** transcript. It
   walks every segment beside it (a subagent's transcript lives under
   `~/.claude/projects/<project-dir>/<session-id>/subagents/agent-*.jsonl`),
   joins each to the spawn whose result it opened at, and prints one row per
   segment: the agent, its own span, calls, tools per turn, mean gap and
   tokens, and, under the table, which rows sit under their kind's bar.

   **A segment's own span is the number no other mode has.** A cycle row's
   `delegated` is the spawn call's own interval, and where a harness writes
   that result on acceptance it reads seconds for an agent that ran twenty
   minutes. The row here is read from the agent's own file instead.

   **A resumed agent is one row per slice, and the mode takes the split.**
   Its transcript holds several stretches of work in one file, and the idle
   gap between two of them belongs to neither: read whole, a segment that
   worked for thirty-seven seconds reports a span over two hours. The cut is
   the coordinator's own message row. Where a file has an idle gap and no
   such row, the report prints one row and names the gap rather than leaving
   it inside a span. The split is the same given the agent's own file:
   `--segments <agent-*.jsonl>` prints that file's slices, named by the file,
   because the spawn that would name them is in the run's transcript and not
   in view. That is the path a harness's task output hands the orchestrator,
   so it is the file an orchestrator holding a fix pass's result already has.

   **A §6 line means an agent spawned another agent**, which
   `skills/agent-contract/SKILL.md` §6 withholds from every agent whatever
   its own definition says. The mode notices and stops nothing: the evidence
   is a transcript on the machine that ran the agent, in no commit and on no
   CI runner, so a report somebody already runs at this boundary is the only
   place it surfaces. Carry the line into the handover; it is about the
   agent's conduct rather than its cost, and no other row says it.

   **Read the counts above the table before the table.** The mode prints
   how many transcripts it walked, how many spawns it found, the tolerance
   it joined within, and how many went unmatched on each side, even when
   they agree. A join that silently matched nothing reads exactly like a run
   that spawned nothing, which is why the numbers are there to be seen
   holding. Given a resumed agent's own file, nothing is walked or joined,
   and a header naming the file and its coordinator messages stands in their
   place.

   **One segment measured on its own is still `session_cost.py
   <transcript>`** with no mode flag, unless the coordinator restarted it.
   The plain reading keeps its numbers, and for a file those messages cut
   into two stretches of work or more it adds one line saying how many
   coordinator messages the file holds: its span then
   covers every stretch of work and the waits between them, and `--segments
   <transcript>` is the reading that splits it. A row of the per-segment
   table is that plain reading of another file, or of one stretch of one.

   **A segment is one agent's own stretch of a chain, and a spawn cycle is
   not one.** Every segment has a transcript of its own: a smith's, a
   warden's, and the orchestrator's, which is one file however many agents
   the run spawned. The spawn cycles inside that file are bands over the
   orchestrator's own minutes, never segments in their own right. The two
   modes follow the distinction: `--spawns` slices this transcript into
   those bands, and `--segments` opens the transcripts of the agents this run
   spawned, one row each, or reads one agent's own resumed file one stretch
   of work at a time.

   **The orchestrator's own boundary is not a user line: `session_cost.py
   --spawns` is what takes it.** Every other segment is measured whole,
   because its transcript holds nothing but itself; the orchestrator's holds
   every cycle of the run, so the whole file is no row of its own. A
   **spawn cycle** is not the review chain's cycle, which
   `docs/the-review-record.md` owns: it ends when a spawn call's result
   arrives and begins where the row before it ended, so the head is the
   framing before the first spawn, cycle N runs from spawn N-1's result to
   spawn N's, and the tail is the closing work after the last one.

   **Post a cycle row as a band, and never as an attribution.** Inside one
   window the orchestrator waits on the previous agent, verifies the report
   it hands over, and frames the next prompt, and no transcript field marks
   where any of those ends. Cycle 1 is the one row without that window: the
   run's own start is a boundary a script can take, so its framing goes to
   the head row instead, and the two are read together.

   **Read `delegated` before quoting a cycle's model time, because what a
   spawn's result MEANS is the harness's and not this skill's.** That column
   is the spawn call's own tool_use-to-tool_result span. Where a harness
   writes the result when the agent FINISHES, the column is the delegated
   wall clock and it is out of the row's other columns, which is the double
   count gone. Where a harness writes it when the spawn is ACCEPTED, the
   column reads seconds and the agent's own wall clock is in **none** of the
   row's columns and none of any other row's. It is the gap between one
   row's last call and the next row's first, and a row's span starts at its
   own first call while its model time never counts the gap before it. So
   the rows partition the run's calls and not its wall clock, and the agent's
   own transcript is where its number is, either way.

   **A span runs from its window's first call to the last call to end.** A
   long-lived call, such as a background command or a suite spanning the
   window, ends after the window that counts it, and the span covers it. A
   reading taken before the release whose file under `changelog/` lists #300
   ended a span at the last call to begin: its span is the shorter of the two
   wherever a call outlived its window, and identical everywhere else.
   `command` can still exceed 100 per cent of the span, because command time
   is a sum over calls and calls can run concurrently. Where a share reads
   above 100, read it as command seconds against wall-clock seconds with calls
   running at once, never as a broken number. Batching is the ordinary way
   in and a background command is the rarer one: every tool call in one
   assistant message carries that message's timestamp as its start, so a
   batch of three overlaps by construction. Measured over the transcripts on
   one machine, every second of overlap above a second came from calls
   batched into one message and none of it from a call that crossed a turn.

   **A `git` call counts as `git` wherever it runs on the line.** The family
   is read by command word: the first word after any separator, newline or
   reserved word, never a word inside quotes or inside `$( … )`, so
   `cd /x && git status` is `git`, and so is a `gh` call inside a loop or
   after a leading assignment. The family reads the command with its newlines
   kept and removes a heredoc's body up to its closing line, so a `gh issue
   create` after `cat > body.md <<'EOF'` and a `bin/test` after a `python3 -
   <<'EOF'` script are read. In a reading taken before the release whose file
   under `changelog/` lists #377, `git` and `test` read low and `other` reads
   high by the same calls, the `other` note may name a command that was a
   `git` run, and the two repeats figures, which keep only `test`,
   `lint/type` and `build`, may read low; span, command, model, idle, tokens,
   tools per turn and the `slowest` list do not move. `--segments` prints the
   same warning on the page.

   **A call that only reads counts as `read`.** A call is `read` when every
   command on it is a read word (`sed`, `grep`, `rg`, `cat`, `head`, `tail`,
   `ls`, `find`, `wc`, `awk`, `nl`, `sort`, `diff`) or a word that touches no
   file (for example `cd`, `echo`, `test`, `[[` and the words that close a
   loop or an `if`; `session_cost.py`'s `NEUTRAL_WORDS` is the whole list),
   at least one reads, nothing writes and nothing is hidden: `sed -i`,
   `sort -o`, `find -delete`, a redirection into a file, a redirection before
   a command's first word, a heredoc or a `$( … )` keeps it `other`, and so
   does any command not on either list. What a `sed` or `awk` program writes
   or runs from inside its quotes is not seen, and such a call is `read`. It
   is judged after the other four, so `grep -rn pytest` stays `test` and
   `ls && git status` stays `git`. In a reading taken before the release
   whose file under `changelog/` lists #642 there is no `read` row, `other`
   holds those calls, and the `other` note may fire where it would not now
   and name a read command; every other row, the two repeats figures, span,
   command, model, idle, tokens, tools per turn and the `slowest` list do not
   move. `--segments` prints the same warning on the page.

   **Where the report gives no between-the-rows figure and prints the rows'
   spans against the run's own, a call outlived the cut its row ends at.**
   Assigning a call by its start is what makes the calls partition, and it
   leaves a long-running one, such as a background command or a suite
   spanning a cut, in the row it began in while the next row has already
   started, so two rows' spans cover the same seconds. The head row's cut is
   the first spawn's START and every other row's is a spawn's RESULT, which
   is why the line names the cut and not the result: a head call can outlive
   its own row's cut and still end before any spawn's result arrives.

   **The two figures it prints are not the rows' overlap, so do not subtract
   them and post the difference as one.** A row's span ends at its own last
   call to end and so does the run's, so every row's interval sits inside
   the run's and the difference is the gaps between the rows minus their
   overlap. Quote that run's span and its rows' columns, and leave the
   between-the-rows share out of the reading rather than substituting either
   sum.

   **So a long cycle span is not a long agent run.** Where a row's span
   exceeds its own parts by an hour, that hour is a gap INSIDE the row,
   above the fifteen minutes model time stops counting at: the orchestrator
   issuing nothing between two of its own calls. Read it as idle time in the
   orchestrator, never as the agent it spawned.
2. Post what the numbers say. `--post` does it: the orchestrator's sentence
   first, the reading fenced beneath it, on the issue the label resolved to,
   the rolling log's for the segment's own numbers and the durable one's for
   a reading that spans versions. By hand it is `gh issue comment <n>
   --body-file <file>`, where `<n>` is the issue number the lookup above
   returned, and that is the command `--post` composes.

The orchestrator does this before the next segment spawns, or at the latest
together with the round or phase record that closes this one: never later,
and never as a question. The destination issue is a log, not a decision: the
orchestrator posts to it without asking whether to, the same way the
completion claims of `skills/verify/SKILL.md` are not asked about before they
are made.

**When the run ends, one more reading is taken, and it is the run's.**
Everything above measures one segment: its span, its calls, its tools per
turn. A run is every segment plus the rounds and the commits between them, and
no segment's numbers say what the run cost. So the report a finished run hands
over (the pull request body's chain section, and the comment that carries the
numbers) holds one table, this run beside the last run measured, with the
same rows in the same order every time. That is what lets two runs be read
side by side without re-deriving either. It is **not a third destination**:
the table goes to the rolling log named above, beside the segment readings it
gathers up.

| Row | Taken from |
|---|---|
| Rounds, finding and verifying | the round records |
| Wall clock, routing commit to last record, build and chain apart | `git log` of the branch |
| Commits, by kind | `git log --format=%s` |
| Findings by severity | the records' verdict tables |
| Findings by `Location`: record, code or tests, and docs | the records' `Location` column. A record is anything under `seal/specs/`, the work item's own documents, because a finding in one is about the run's own paperwork rather than about the tool. That path, not the whole of `seal/`: the root also holds `config.md`, `follow-up.md` and `README.md`, which are the repository's own and belong under `docs` |
| Records' share of the diff | `git diff --numstat` against the base, the record paths above counted apart |
| Model turns, output tokens, cache write and cache read | `session_cost.py`'s token line over the run's main transcript |
| Segments: count, minutes and tokens per kind | the agent completion notices, or the subagent transcripts |
| Broad gate: whether it has run, how many times, and at what SHA | the work item's `broad-gate.md`, which holds one entry per full-suite run, newest first, each a SHA with the base it was compared against; the count is the number of entries, read off the file rather than remembered |

**The tokens are counted, not estimated, and counted the same way every
time.** `session_cost.py <the run's main transcript>` prints the token line,
which sums `output_tokens`, `cache_creation_input_tokens` and
`cache_read_input_tokens` over every `usage` block in that transcript and in
every file under its `<session-id>/subagents/` directory. One command, so the
row cannot be summed one way this run and another way the next. The line also
says how many transcripts it covered, and that count is what a reader checks
the number against.

**The run's main transcript is the `*.jsonl` sitting directly under the
project directory**, never one under a `<session-id>/subagents/`. `--latest`
takes the newest file anywhere beneath the project directory, so on a run that
spawned segments it usually lands on a segment rather than on the run: the
path it prints as its first line is what says which, and a token line reading
`1 transcript` for a run that spawned six is the same thing said twice. Give
the main transcript by path when that happens.

**A comparison against a run whose transcript covered only part of its branch
says so beside the number**, in the prose under the table rather than as a
column. A resumed session, a transcript split at the user lines, a segment
spawned through another harness: each of those leaves the token row covering
less than the branch, and a smaller number with nothing said about it reads as
a run that cost less.

**The table carries no verdict.** It makes two runs comparable and does
nothing else. What a row meant on this branch, such as why the rounds ran
long or why one kind of segment cost what it did, goes in the comment beside
the table, never in a column of it.
