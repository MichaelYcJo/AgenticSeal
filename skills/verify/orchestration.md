# verify, the orchestrator's half

This file is the orchestrator's: the session that spawns the crafter, the
proofer and the sealer and takes the one broad run between the last of them.
It holds the two acts of the verify protocol that no agent takes: the broad
gate, and the measurement of each run posted to the flow log.

`skills/verify/SKILL.md` is the other half: the four conditions every claim
meets, the hand-back's labels, the scope rule and the counterfeits. The
orchestrator reads both. The crafter and the sealer open that one and never
this one, because contract rule 2 gives the broad gate to the orchestrator and
contract rule 6 withholds posting from every agent.

## The broad gate

**It fires after the review rounds settle, never before them.** Nothing broad
runs at the handoff to review; the hand-back carries the suite as
`unverified`, and that label is what keeps the narrow scope honest.
`skills/verify/SKILL.md` *Scope: cheap and often, broad and once* holds the
reason: a run taken before the rounds is spent by the first finding. Findings
are the expected case rather than the exception: the review chain runs three
finding rounds by default (`docs/running/the-run.md` *The run*).

**"After the rounds settle" is a row, not a moment, and this is the row: the
last `trail/rounds/round-N.md` has no finding open.** The phrase alone names no
particular rounds: a work item has build phases with a progression of their
own and a review chain with its own, so a reader who reaches for the moment
has to guess, and one who reaches for the record does not.

**It belongs to the orchestrator, and the four conditions of
`skills/verify/SKILL.md` are the whole of the run.** No agent runs it:
`seal gate --base <base> --record <item>` is the command the orchestrator
types, with nothing else running, and `skills/code-review/orchestration.md`
*Orchestrator: the pull request opens once the sealer seals* owns when,
before the sealer is spawned. The run judges no failure and fixes none; the
sealer reads its record, and what it guarantees after it
is `docs/forms/the-guarantee.md` *The guarantee*. `seal gate --preflight`,
which the orchestrator runs before the broad run, is not this run: it runs
the gate's record arms, runs no suite, and writes nothing.

**An expensive suite argues for this placement, not against it.** A run that
takes fifteen minutes is a finding about the run and deserves its own ticket.
Moving it ahead of the rounds means paying it twice.

**Which base, and it is the one the merge is judged by.** The gate resolves
`--base` once, before anything runs, to the ref CI will read: the base's
upstream where the checkout declares one, else `origin/<base>`, else the ref
as given. Every check it runs takes that one commit: the chain check's
baseline, the scratch worktree the base comparison checks out, and `trail/gate.md`. A plain
branch name is a LOCAL ref and a runner has no local branches, so a checkout
one commit behind its remote would pass green where CI refuses the same
commit. Where resolving moves the answer the gate prints one line naming both
refs, both commits and the distance, and runs anyway; where the two agree it
prints nothing. It never fetches, so a remote-tracking ref is only as fresh
as the last fetch, which is why the gate's report names the ref beside the
commit on the `base` row rather than the commit alone, and the `BROAD GATE
PASSED` line names it as `<ref> @ <commit>`.

A full suite carries failures that were already there. Attributing them to
this work is a wrong finding; passing over them is a silent pass. Both are
avoided the same way: read the run against the base commit.

**That comparison is reactive.** A baseline answers whose failure this is, so
it is taken only once an unexplained failure appears. The gate takes it
itself: it runs its whole command once more at the base and reads each failing
file against that run, as `templates/setup/config.md` *The criterion for
choosing a value*, rule 3, states. A file run at the base by hand runs in a
`git worktree add` of the base commit, never under `git stash`: every
worktree and session of the clone shares the one stash stack, so a pop can
take another session's entry.

- **Failing on base too**: not this work's finding. Name it, record it as a
  follow-up, and it does not block.
- **New**: this work broke it. Back to the implement and review loop, and the
  broad gate runs again afterwards.
- **New?**, with a reason, means nothing at the base measured it: no pytest
  the `Broad gate` command ran left a record, because the command started
  no pytest, none it started loaded the gate's recorder, or the one that
  did could not write its record and warned in `suite.txt`, so the file is
  named only by a `FAILED` line and the base was not run; no pytest the
  command ran at the base left a record, for any of those three causes, a
  part before the runner failing at the base among them; or the command's
  run at the base exited non-zero before any pytest collected the file,
  which is also how a file the branch added reads where the base's command
  already fails; or a
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
  `templates/setup/config.md` *The criterion for choosing a value*, rule 3, says
  which commands the gate cannot measure and how a command earns the
  measured word.

Without the comparison, every failure that was already there is triage the
author cannot act on and is not allowed to fix.

**Three returns and stop.** This counts trips through the gate, not the
review chain's rounds. A fourth trip is not another bug; it means the narrow
scope is missing a class of breakage, which is an architecture question for
the user, the same reading as the three-fix rule of `skills/implement/SKILL.md`
*2. Implement test-first, and let each rule name its test*.

**Nothing edits between the broad run and the PR.** The tree that passed is
the tree that ships. One more small fix after the run means the run is stale,
and the gate is paid for again.

## Measure the run, and feed the flow log

When a work item's run ends, the orchestrator measures it once with
`skills/verify/scripts/session_cost.py`, typed as `seal cost`, and posts the
numbers, and what they say, as one comment on one of this repository's two
measurement logs. Which of the two is not a filing detail: one of them is
deleted at every release, so a reading put in the wrong one is a reading
thrown away, and the paragraph below is what decides it.

**There are two logs, and the difference is kind rather than scope.** A
reading of what one run of this version cost (its segments' spans, calls and
tokens, and what those say) belongs to the rolling `flow-measurement` log,
which opens at a release, accumulates until the next version ships, and is
discarded by the release that ships it. Readings that span versions (a rate
held against an earlier version's baseline, or an observation that a later
measurement answers) belong to the durable `flow-baseline` log, which is
maintained rather than accumulated. Posting one of those to the rolling log
schedules it for deletion at the next release. A repository declares each
log with a label on an issue, and each keeps the same invariant: exactly one
open. Neither is named by number, because a number goes stale the moment
its issue closes. Where no issue has ever carried `flow-baseline`, the
repository has no durable log, and a cross-version reading stays in the
record that would have cited it.

**The run ends when the work item's last segment has handed back**, the
sealer's where one runs. The orchestrator first reads the run, and the read
posts nothing:

```
seal cost --work-item <the work item's directory>
```

It prints the rows the post will carry, any `Contract rule 6` line below
them, and the log's state. The orchestrator writes the `--says` file from
that reading, then posts it with the same command:

```
seal cost --work-item <the work item's directory> --post --says <file>
```

The read comes first because the posting form sends the reading into the
comment and shows the terminal only one state line. The `--says` file holds
the orchestrator's sentence on what the readings say, read against the work
item's records, then the run's table below, then the counts of the frame
exchange. What each segment cost goes into this one comment, and no segment
gets a comment of its own. The command finds the work item's segments by
their spawn prompts naming its directory or the branch its `routing.md`
names. A segment whose prompt also names another work item, as a framer's
prompt names the release's other items (`skills/implement/merge-order.md`),
is counted for each, and the reading names it with those items. Which run
it belongs to is the orchestrator's judgment, written in the `--says`
sentence. The command posts one row per segment that no comment on the open
log names, each segment's file named on a `# <file name>` line inside its
fence, and where no segment transcript on the machine names the work item,
the comment says so. A reading that spans versions takes
`--label flow-baseline` on both the read and the post.

The release runs the posting command for each work item it ships
(`docs/releasing/release-checklist.md` *The release pull request*), and for
this work item it then posts nothing, except a segment that ran after this
comment. The table is not a third destination: it goes into this comment,
and not into the pull request body, whose first part every round reads
before the run ends. The orchestrator posts without asking, never as a
question. The log is a log, not a decision, the same way the completion
claims of `skills/verify/SKILL.md` are not asked about before they are made.
The meter's other modes, `--latest`, `--spawns`, `--segments` and `--json`,
and how to read their columns, are stated in `session_cost.py`'s module
docstring and on the pages they print.

**Each exit of the posting command prints one line naming its state, and
its code says what the orchestrator does next.**

- **Exit 0**: one comment was posted, or nothing was due. Nothing is due
  where every segment of the work item is already named on the log, where
  no issue has ever carried the label, or where `gh` could not run. No issue
  ever carrying the label is the case most installed repositories meet, and
  there the post is a no-op: nothing is posted, nothing fails, and nothing
  asks. The read still runs there, because it is where the orchestrator
  sees a `Contract rule 6` line. Exit 0 needs nothing more.
- **Exit 1**: nothing was posted. The label has a history and nothing is
  open, more than one log is open, the log's comments could not be read,
  the comment failed, or `--says` gave an empty reading. An empty reading is
  the orchestrator's to write and run again. Every other exit 1 is named in
  the run's hand-over with the line the command printed. The orchestrator
  opens no log, because opening one is not a session's act, and
  `docs/running/measuring-a-run.md` *Where a reading goes* holds the
  reasoning. Where more than one log is open, it names them rather than
  guessing which one is current.
- **Exit 2**: the command line was refused before any lookup, such as
  `--post` without `--says`, or `--work-item` beside another reading. The
  orchestrator corrects the line and runs it again.

**A `Contract rule 6` line in the reading means an agent spawned another
agent**, which contract rule 6 withholds from every agent whatever its own
definition says. The read without `--post` prints it where a segment's own
transcript holds an `Agent` call, and names that segment's file and its
count, and the posted comment carries the same line inside its fence. The line
is about the agent's conduct rather than its cost, so the orchestrator gives
it the home that `skills/implement/orchestration.md` *Orchestrator: where a
decision or a lesson is written* gives a lesson about how an act is done.
Any other lesson about an agent's conduct, such as a broken spawn rule, takes
that home when the orchestrator sees it, and the run's comment carries what
the run cost.

**The run's table is one table, this run beside the last run measured, with
the same rows in the same order every time**, so two runs read side by side
without re-deriving either. A run is every segment plus the rounds and the
commits between them, and no segment's numbers say what the run cost.

| Row | Taken from |
|---|---|
| Rounds, finding and verifying | the round records |
| Wall clock, routing commit to last record, build and chain apart | `git log` of the branch |
| Commits, by kind | `git log --format=%s` |
| Findings by severity | the `severity:` line of each finding block in the round records |
| Findings by `Location`: record, code or tests, and docs | the `location:` line of each finding block. A record is anything under `seal/threads/`, the work item's own documents, because a finding in one is about the run's own paperwork rather than about the tool. That path, not the whole of `seal/`: every file the root holds outside `threads/`, each named in `docs/layout/the-record-layout.md` *seal/*, is the repository's own and belongs under `docs` |
| Records' share of the diff | `git diff --numstat` against the base, the record paths above counted apart |
| Model turns, output tokens, cache write and cache read | `session_cost.py`'s token line over the run's main transcript, the `*.jsonl` directly under the project directory and never one under a `<session-id>/subagents/`, given by path |
| Segments: count, minutes and tokens per kind | the agent completion notices, or the subagent transcripts |
| Broad gate: whether it has run, how many times, and at what SHA | the work item's `trail/gate.md`, which holds one `seal` block per full-suite run it recorded, the newest last, each a `run:` line naming the tree and the base it was compared against; the count is the number of blocks, read off the file rather than remembered |

**The tokens are counted, not estimated, and counted the same way every
time.** `session_cost.py <the run's main transcript>` prints the token line,
which sums `output_tokens`, `cache_creation_input_tokens` and
`cache_read_input_tokens` over every `usage` block in that transcript and in
every file under its `<session-id>/subagents/` directory. The line also says
how many transcripts it covered, and that count is what a reader checks the
number against.

**A comparison against a run whose transcript covered only part of its branch
says so in the prose under the table**, never as a column. A resumed session
or a segment spawned through another harness leaves the token row covering
less than the branch, and a smaller number with nothing said about it reads as
a run that cost less.

**The table carries no verdict.** What a row meant on this branch, such as
why the rounds ran long, goes in the orchestrator's sentence beside the
table, never in a column of it.
