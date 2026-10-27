# The broad gate

Narrow and often, broad once. The full suite, the repository-wide lint and
the typecheck are a **single act**, taken after the review rounds settle and
before the pull request opens. This document says who takes it, what it
runs, and what it is allowed to say.

## One act, one owner, and the owner is the orchestrator

**A prohibition needs a holder, and the holder is the orchestrator.** No
agent runs the broad gate. The orchestrator runs `broad-gate --base <base>
--record <item>` once the rounds settle, with nothing else running, commits
the record, and then spawns the sealer, which reads that record and runs
nothing broad. A run inside an agent would be a second run of a suite the
orchestrator takes once, and a prohibition with no holder is one every reader
reasons past.

The run judges nothing. `broad-gate` runs the repository's broad command,
reports what the commands said, and writes the work item's `trail/gate.md`;
the sealer's own verdict, which follows the run, is a separate file
(`docs/the-review-record.md` *The guarantee*). A run that judges is a run
whose verdict nobody can separate from its measurement.
check: tests/test_broad_gate_rule.py

**What the run prints says only whether it passed, and it draws nothing.**
Its stdout opens `BROAD GATE PASSED` or `BROAD GATE FAILED` over the branch,
the tree and the base it measured; a passing run prints its panel's rows as
text under that line, the same bytes on a terminal as on a pipe, and writes
no values file and no drawing. The verdict word `sealed` is the sealer's,
and the stamp is drawn from that verdict at its write, in either mode
(`docs/the-review-record.md` *The stamp*), so a green suite is never read as
a sealed work item.
check: tests/test_one_word_one_meaning.py tests/test_the_seal_is_taken_once_by_the_sealer.py

Where a rule every agent is bound by lives, and where one agent's own rule
lives, is `docs/the-agent-set.md` *One contract every agent receives, and
one definition each*.

**A suite that is not mentioned reads as a suite that passed.** An agent's
handover carries the suite labelled `unverified` with the orchestrator named
as its answerer: labelled, never omitted.
check: tests/test_the_agent_contract_holds_the_universal_rules.py tests/test_every_agent_reads_the_contract.py

## What the gate runs, and how the list is kept true

**Every step CI runs is either mirrored by a named arm or excluded with a
written reason. There is no third state and no silence.** An arm list kept by
hand drifts the moment somebody adds a step to the workflow, and the drift is
invisible: the gate goes green having not run what CI will. So the partition
is declared in the gate and a structural case asserts it is total: a step
name in the workflow with no classification in the gate fails the suite until
somebody classifies it. A step CI does not run for the base is neither
answered nor unanswered: some steps run only on a pull request into `main`
and some are skipped there, so the panel's count and the line beside it are
taken over the steps CI runs for the base, and the line says how many it left
out. Which steps those are is declared beside the partition and held against
the workflow's guards from both sides, never read off the workflow at run
time.
check: tests/test_the_gate_names_every_step_ci_runs.py tests/test_broad_gate.py

**The gate and CI ask about the same range, and the base is resolved once.**
A local branch name and the remote-tracking ref CI reads are two different
commits whenever the local one is behind, so a gate that resolves its base
differently from the workflow reports on a range nobody will be judged
against. The base becomes a resolved commit plus the ref it came from before
any check runs, and after that point the raw argument is read nowhere. The
order is the upstream the checkout declares, then the remote-tracking
spelling the workflow uses literally, then the ref as given.
check: tests/test_the_gate_asks_the_range_ci_will_ask.py

**A configured command that breaks the criterion is refused before anything
runs.** The row naming the repository's broad command is read by the gate and
by nobody else until the gate runs, so a value that cannot do what the row
promises would otherwise be discovered at the one moment the run was supposed
to save. The refusal names the form, quotes the value, and shows the row
rewritten: exit 2, nothing run, the shape an absent row already takes. The
criterion for choosing a value has one owner, the template that documents the
row, and it is three rules rather than an example.
check: tests/test_broad_gate.py

**A fenced example in a config file is not a config row.** The one walk of
the `| Item | Value |` table reads the file through one fence rule, and the
writer overwrites the line that walk names. A reader and a writer that
disagree about which line is the row leave a file two rows deep that no
command can bring into agreement, so a repair landing in the reader alone is
half a repair.
check: tests/test_config.py tests/test_seal.py tests/test_broad_gate.py

**The gate that measures a tree is the copy that tree ships, and its report
says which copy measured it.** A gate found on PATH is the installed plugin's,
so a branch that changed the gate would be measured by the copy that predated
the change. CI runs the checkout's scripts, and the gate exists to say what
CI will say, so where the gated root carries
`skills/verify/scripts/broad_gate.py` and that file is not the running one by
realpath, the running copy hands it the whole argument vector before judging
anything. Its exit code is the run's, and a flag only the tree's copy knows
still reaches it. A repository that ships no gate, which is every repository
that installs the plugin, runs the installed copy. The symmetric cost, a tree
that breaks an arm and passes itself, is named rather than dismissed: one
stderr line names the running copy's path and reads `tree <version>` or
`plugin <version>`, the panel's `gate` row reads `tree <version>` wherever
the copy that ran is not byte for byte the copy invoked, or where the tree's
copy ran with no invoked copy named to compare against (invoked directly, or
redirected by an installed copy that names none), and the pull request asks
the same scripts again. The row prints nowhere else, because over a tree
whose gate the branch did not change it says nothing a reader acts on.
check: tests/test_broad_gate.py

## What the runner owes the person who typed it

**A repository ships a command that runs its own suite, and it is cheap the
second time.** A documented incantation that resolves and installs its
environment on every call is not a missing command, it is an expensive one.
The environment is built once and reused; the first call pays for it and
every call after it pays for interpreter startup and nothing else.
check: tests/test_the_suite_has_a_command_that_is_cheap_twice.py tests/test_run_tests.py

**Every failure the runner has is a sentence, never a traceback.** The
awkward one is the environment it cannot write: the refusal that was supposed
to name the floor would be replaced by a stack trace about a directory, which
tells the reader about the directory rather than about the thing they typed.
A read-only environment directory is the operator's; the runner says what it
could not do, names the path and what it means for `git status`, and carries
on.
check: tests/test_the_suite_has_a_command_that_is_cheap_twice.py tests/test_run_tests.py

**The runner runs the suite in parallel by default, in every environment it
builds or adopts, and the caller's own choice wins.** A runner that withheld
`-n auto` where the environment lacked `pytest-xdist` would make one command
mean three things in one repository, serial on one checkout, parallel on
another and `unrecognized arguments: -n` in a fresh worktree, while CI runs
the same suite `-n auto` on three platforms. So a build installs
`pytest-xdist` beside `pytest`, and an adopted environment without it takes
one install step, found by the filesystem so that a warm call still reaches
no builder. A missing speed-up is repaired rather than refused, because the
suite is correct without it: an install that fails is one sentence naming the
remedy, then a serial run with pytest's exit code. `-n auto` is withheld
where the caller already decided: any spelling of `-n` or `--numprocesses`,
`-p no:xdist`, or `--pdb`.
check: tests/test_run_tests.py

## A check that cannot fail is not a check

**A module's arms are enumerated from its own source and each one mutated,
and the arms no case kills are reported.** Counting a module's arms by hand
produces a number that rots, and an arm nothing kills is an arm that can be
deleted with the suite staying green. That is the same rule new cases are
held to, seen red before it is committed, applied to the arms that are
already there.
check: skills/verify/scripts/arm_check.py tests/test_arm_check.py

**A check named for a property has to be able to observe that property.** A
check and its own case that each hold their own copy of what the check looks
for, such as a set of search phrases or a range, drift into checking
different things. The thing the check is named for becomes a value both the
check and its case read.
check: none reader: review of each check

**A document that its own work item's fixes disproved is corrected in the
same work item.** A docstring naming a class the command does not refuse, and
an argument whose grounds the fixes removed, are both statements a reader
acts on, and the run that disproved them is the only run that knows. A
correction made later is made by somebody who has to rediscover why, and a
correction never made is a false statement with a checker's authority behind
it.
check: none reader: review of the same pull request
