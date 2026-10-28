---
name: verify
description: |
  Evidence protocol for completion claims (the Seal Test): name the proving
  command before running it, show the check can fail, bind the result to a
  tree state, and label every claim executed, read or unverified.
  Use when: about to say done, fixed, passes, or complete; before a commit;
  before handing work to the review chain.
  NOT for: deciding whether the work is worth doing, or reviewing someone
  else's diff (`code-review`).
---

# The Seal Test

This file is the crafter's and the sealer's: the crafter opens it before it hands
work back, and the sealer opens it for the conditions, the labels and the
verdicts it audits against. The orchestrator reads it too. The orchestrator's
own two acts, the broad gate and the measurement of each segment, are
`skills/verify/orchestration.md`, which the crafter and the sealer do not open.
Each instruction below binds the party making a claim, whichever of the three
it is.

A completion claim is a mark, and a mark must be *earned*: **a check that
cannot fail proves nothing, and evidence that outlives its tree state proves
less than nothing.** Freshness alone accepts any green command as proof; this
protocol asks more of the command.

A claim stands only when all four conditions hold.

## The four conditions

### 1. Named before run

State the proving command **before** executing it, next to the claim it
proves. Choosing the command after seeing what passes is how a test suite's
green becomes "feature works": the mapping from claim to command is the
verification, and the run only executes it.

### 2. Able to fail

Show the check CAN go red. For a bug fix: the reproduction failed before the
change (or fails when the change is reverted). For a new test: it was
observed failing against the pre-change code. A check that has never been
seen red is a counterfeit seal. This is the condition generic gates skip,
and the one that catches assertion-free tests, mocked-away behavior, and
wrong-file test runs.

#### An absence claim is only as good as the search behind it

"There are no callers", "the original has no such branch", "nothing reads
this column": these are claims about the whole tree, and their entire
evidence is that one search did not find something. An existence claim comes
with a coordinate anyone can open; an absence claim comes with nothing to
open, so the cost of checking it is asymmetric and it tends to pass unread.

Condition 2 applies to the search itself: **run it against a case known to be
present.** A pattern that finds nothing there was broken, not the tree empty.
Report the command and the scope it ran over, so the next session re-runs it
instead of re-inventing it.

An absence that cannot be demonstrated that way is `unverified` and reads "not
found", which is a different sentence from "not there". Never promote one to
a document: a policy or a rule built on a search nobody could repeat is the
same defect as a `read` reported as passing, with a longer fuse.

#### `seal arms` asks condition 2 of a whole module, one arm at a time

Condition 2 is asked of the case at hand. **A module has arms nobody
ever asked it of**, and a count of them taken by hand is wrong as soon as the
module changes.

```
seal arms hooks/routing-edit-gate.py
seal arms hooks/routing-edit-gate.py --tests "bin/test tests/hooks/test_routing_edit_gate.py -q"
```

With no `--tests` it lists the arms and mutates nothing. With `--tests` it
first runs that command once against the module as it is, which has to pass
(below). Then it makes each arm wrong in turn, runs the command again, and
names the arms nothing kills. It restores the module from held bytes and
compares the sha256 after every mutation, never with `git checkout`, which
reaches the uncommitted work in the rest of the tree.

**`--timeout` bounds the wait, and not the work.** Each operator's command is
waited for at most 900 seconds by default (`--timeout 0` removes the bound),
and an arm asks two operators, so one arm can take twice that. When the bound
is reached, only the command's own process is killed. A wrapper command is the
one that leaks: where `--tests` names a runner that starts pytest as a child of
its own, as the example above does, a timed-out pair leaves that suite running,
unbounded and unreported, beside every arm after it. The first run against the
unmutated module is waited for under the same bound and leaks the same way
when it reaches it, before the run is refused. Against a module whose
suite can approach the bound, name the pytest command in `--tests` directly
rather than a wrapper.

**There are two ways to be wrong and the counts differ by a lot**, so the
report keeps them apart and a quoted number has to say which one it is:

| Operator | Asks |
|---|---|
| `invert` | would a case notice this test being **backwards** |
| `remove` | would a case notice this arm being **absent** |

**A survivor count is a measurement, not a property of the module**: it moves
when either the module or its cases change. Take it with the command above
whenever it is needed, and never write one into a document.

The two denominators differ because **a pair both operators answer identically
is asked once.** A handler with one type left is aimed at what nothing raises
by either operator, so `invert` refuses it and the report names the pair;
`remove` keeps it.

An arm counts watched when **either** is noticed, because *does any case
depend on this arm* is answered by one yes.

An arm is an `ExceptHandler` counting each member of an except tuple
separately, or an `If`, `While` or `IfExp` counting each **top-level** member
of the boolean test separately, plus a `match_case`'s alternatives and guard
and a comprehension's `if` guards. The walk is derived from the grammar rather
than from a list, and it **refuses an AST node type it does not recognise**
instead of skipping it: a walk that skips silently undercounts the way a hand
count does.

**A `killed` is a measurement only when the command passed without the
mutation**, so `--tests` runs once against the module as it is before
anything is written. A `-k` that selects no case, a module path that does not
exist and a case already failing each exit non-zero whatever the module
holds, so without that run each would read `killed` beside every arm. When
that first run exits non-zero, does not return within `--timeout`, or cannot
be spawned, the command prints `no baseline:` with the cause and what the
command printed, writes nothing, measures no arm, and exits 2, the code it
already gives a negative `--timeout`. If the command itself changed the module
during that run, the module is put back from the bytes read before it and the
line says so instead. Where it cannot be put back, because the command left
it unreadable, unwritable or replaced by a directory, the line names the
error.

Two things it does not claim. **A survivor is not automatically a defect:** an
arm that cannot be constructed, or one whose removal preserves behaviour,
belongs in the report and is not work anybody owes. And a measured run is
**report-only, exit 0 either way**: whether an unwatched arm should fail a
run is an open decision, not an omission.

#### `seal mutate` asks condition 2 of one unit, one break at a time

`seal arms` breaks a module's arms under two fixed operators. The unit an
implementer has just added is usually something else: a constant, a flipped
comparison, a sentence a case pins. The break is whatever makes that unit
wrong, so the loop is one command per break:

```
seal mutate <file> --replace "<old>" "<new>" --tests "bin/test tests/<module>.py -q -k <cases> -p no:xdist"
```

`<old>` is literal text and must occur exactly once in the file, or nothing
is written; `<new>` may be empty, which deletes. Any UTF-8 text file can be
the target. The command first runs `--tests` against the file as it is, and
goes on only if that passes. A `-k` that selects nothing, a mistyped module
and a case that already fails each exit non-zero, and without that run each
would read `red` for a unit no case ran against. Then it writes the break,
removes that file's cached bytecode
for every interpreter tag, runs `--tests` with `PYTHONDONTWRITEBYTECODE=1`,
puts the file back from the bytes it read first and compares their sha256,
and removes the bytecode again. Nothing is read from git. The script is
`skills/verify/scripts/mutation_check.py`, and it uses `seal arms`'s own two
functions for the bytecode and the restore.

The first line printed is the verdict, then the command's own output:

- `red`, exit 0: a case failed against the break, so the unit is watched.
- `SURVIVED`, exit 1: the cases passed, so nothing they run watches the unit.
- exit 2 for every run that measured nothing: `no baseline` (the cases fail
  without the break, so the break was never written), `timed out`, `could not
  start`, `could not run`, `refused` (nothing was written), `not restored`
  (the file may still hold the break; restore it from the commit made
  before the run), and
  `interrupted`.

So `seal mutate … && seal mutate …` stops at the first unit nothing
watches, or at the first run that could not say.

**Several mutants of one file go in one call.** Give `--replace OLD NEW` once
per mutant. Every pair is checked before anything runs, and one that does not
land exactly once refuses the whole call. The baseline then runs once, and
each mutant is written alone, run once and restored, in the order given. The
call prints `mutant <n>: <verdict>` per pair and a line counting the
verdicts, and exits 1 where any mutant survived, 2 where none did and a run
measured nothing, and 0 where every mutant is red. Put `-x` in `--tests`, so
each mutant's run stops at the first case that notices it; the command does
not stop the cases itself.

**Why the cache beside the file, and not `tests/__pycache__`.** CPython runs
a cached `.pyc` instead of the source whenever the size and whole-second
mtime it recorded still match, and a same-length break written inside one
second matches. Only the mutated file's cache can be stale. An importer's is
valid for its unchanged source, so clearing `tests/__pycache__` removes
caches that are right and misses the one that matters whenever the mutated
file lives anywhere else. Every tag goes, because the
interpreter that runs the command and the one that runs the cases can
differ.

**The cases inherit `PYTHONDONTWRITEBYTECODE=1`.** A case that needs a
`.pyc` to exist, such as one that plants a cache to show it is removed, has
to write it itself, with `py_compile` or with `sys.dont_write_bytecode`
switched off for the plant. An import made under the variable writes
nothing, and the case then goes red on its own precondition whatever the
break was.

**The bound ends the run, not only the process it spawned.** `--timeout` is
300 seconds by default for each of the two runs, and `0` removes it. On
POSIX the command runs in a session of its own and a timed-out run's whole
process group is killed, so a wrapper's pytest does not outlive the verdict.
That is the hole `seal arms`'s bound still has. The group of a run
that exited is ended too, and the wait is on the process rather than on its
output, so a child the cases leave behind neither outlives the verdict nor
holds it back. A process that put itself in yet another session is outside
the group and outlives the kill; the verdict names that as the bound's
limit, and cannot tell whether one did. Ctrl-C
reaches this command rather than the cases, and it ends the group before the
restore. On Windows only the direct child is ended, and the verdict says that
anything it started was not.

`-p no:xdist` belongs on a handful of cases: starting the workers takes
longer than the cases do. For a module's arms rather than one unit,
`seal arms` above is the command.

### 3. Bound to the tree

Evidence attaches to a tree state, not to a session. Note the state the
proof ran against (commit + dirty files); **any edit after the run voids
the claim**: re-run, don't re-tell.

### 4. Each claim labelled executed, read or unverified

Every claim carries one of three labels:

- `executed`: ran it, read the full output, checked the exit code.
- `read`: inferred from reading code, which is a judgment and not proof.
- `unverified`: names who or what can answer it.

Reporting a `read` as passing is the lie this whole skill exists to prevent.

## Procedure

1. List the claims this response is about to make.
2. For each, name the proving command (condition 1). Where no command exists,
   label the claim `read` or `unverified`, never "should work".
3. Run fresh; read the FULL output; record the exit code and the line that
   proves or refutes (conditions 2 and 3).
4. Where any claim is red or unproven, report the actual state. The claim is
   withheld, not negotiated.

## The hand-back's labels carry the claims, and the one seal is the sealer's

**The hand-back's labels carry the claims, and the one seal over the whole
project is the sealer's `guarantee.md`.** An agent hands its claims back under
condition 4's three labels, and a proofer's report says what its review looked
at; neither is a seal and neither ends in a block.

Two properties tell the sealer's seal apart from every other account of a
run.

- **Scope.** An agent's hand-back covers what that agent touched. The
  sealer's seal covers a tree nobody is still editing, which is why the rule
  that nothing edits between the broad run and the pull request
  (`skills/verify/orchestration.md` *The broad gate*) is one that seal rests
  on.
- **Form.** The sealer's seal is the only mark drawn, and only over a verdict
  that earned it: the stamp is drawn from the sealer's `guarantee.md` reading
  `sealed`, once per work item, at the end of the turn in which that file is
  written. The edit hook writes the values it is drawn from at the file's
  write, under either root, and the `Stop` hook draws them in the
  orchestrator's session
  (`docs/the-review-record.md` *The stamp*). The broad gate draws nothing:
  its line reads `BROAD GATE PASSED` or `BROAD GATE FAILED` and judges
  nothing. So seeing the drawing means the last seal was earned.

**A bare "the seal" is ambiguous the moment more than one exists, so every
reference to an INSTANCE names whose**: the sealer's seal, the proofer's
round record. The concept and its formats stay bare: the Seal Test, a
counterfeit seal, AgenticSeal itself. The shape to watch for is a sentence that
names one party and leaves the seal anonymous: *the proofer's audit of the
seal* names an auditor and not what is audited.

## Scope: cheap and often, broad and once

Condition 3 decides where a broad check belongs. Evidence binds to a tree
state, so **any run followed by an edit was spent, not banked**.

Review rounds are edits already scheduled. Running the whole suite before
them measures a tree that is going to change.

| When | What runs | Label |
|---|---|---|
| Each slice | the tests for what the slice just wrote | `executed`, narrow |
| Phase boundary | the module the phase changed and the ones it touches, in parallel | `executed`, scoped |
| Handoff to review | nothing broad | the suite is `unverified`, and says so |
| Review rounds 1..n | what the fix touches | `executed`, narrow |
| **After the rounds settle** | full suite, lint, typecheck, **once**, by the orchestrator | `executed`, broad, once |

The last row is the orchestrator's, and `skills/verify/orchestration.md` *The
broad gate* holds it, read against the base commit.

Narrowing is not permission to go quiet. A suite the party making the claim did
not run is `unverified` with who answers it, never omitted: condition 4 is what makes
the smaller scope honest rather than a loophole. The loophole reopens three
ways, below.

### The narrow command still has to be able to fail

Condition 2 does not relax when the scope shrinks. A smaller command is still
a command being chosen, and it is easier to choose wrong: it can come back
green because it examined nothing. A Python linter aimed at a directory that
holds no Python reads this way:

```
$ ruff check docs/
warning: No Python files found under the given path(s)
All checks passed!                                        (exit 0)
```

Exit 0, nothing read, and a green line in the hand-back. Before a narrow
command counts, say which files it opened. If the answer is none, the honest
row is `unverified`, not a passing one.

What can fail depends on what changed, which is the axis worth picking the
command from:

| What changed | What can fail |
|---|---|
| Prose only: docs, comments, docstrings | Whatever actually parses those files. Often nothing does, and then there is no seal to earn here. |
| A comment or docstring inside source | That the module still imports. |
| Logic | The tests covering that file. |
| A merge, or a dependency bump | The broad gate. What breaks is outside what was edited, so a scope drawn around the edit cannot see it. |

The last row is the one that gets narrowed by mistake. A merge is the moment
the tree stops being the one that was tested.

### The answerer has to exist

`unverified; CI covers it` satisfies condition 4 on its face and voids it
underneath. The row names an answerer, and nothing checked there was one: a
repository's workflows can assign reviewers, deploy on push and validate a
migration graph while none of them runs the suite, and a pre-commit hook runs
on the committer's machine alone.

Resolve the answerer before writing the row:

```
seal deferrals .              # is the test suite answered here?
seal deferrals . --kind all   # tests, lint, typecheck
```

It separates four outcomes that a reader otherwise collapses into one:

- something answers on pull requests;
- something answers, but only after the point being deferred;
- a local hook answers on the committer's machine only;
- nothing answers.

Exit 1 means the row about to be written is not true.

It reads command text rather than a YAML graph, so a runner reached through a
composite action, a reusable workflow, or a script it cannot see reads as
absent. Disagreement with what CI really does is a finding about this tool,
not permission to keep the row.

### And something has to read the row afterwards

An answerer that exists still answers nothing if nobody returns to the row.

```
seal unverified .                                   # what is still open, and where
seal unverified --baseline origin/main seal/threads/  # and nothing was deleted from it
```

It never fails for an open item: punishing an honest row is how sessions learn
to write none. It fails for a section it cannot read, because a tolerant reader
reports zero there and zero reads as "everything has been closed". Close an
item by opening its row with the word `closed` and saying what closed it; the
row stays.

**`--baseline` names the branch the work merges into, and what it reads is
`git merge-base <ref> HEAD`**: the fork point on a branch checkout, and the
base's tip in CI, whose checkout of a pull request is the branch's head
already merged into the base. Either way a work item squashed into that
branch after this branch was cut is not this branch's removal.

## The cost of a run that repeats

Scope decides how often the expensive command fires. It does nothing about
what the command costs, and the narrow run is the one that multiplies: every
slice, every round.

Measure before accepting it. The suspect is usually wrong, and the fast path
is often already in the project: a parallel runner installed and unused, its
recipe written in a comment. A recipe in a comment is not a recipe. Nobody
runs it, and an agent least of all.

So before paying a check's cost repeatedly, spend a minute on where the time
goes, and look for the fast path the project already has: a runner in the
lockfile, a target in the Makefile that is not the default, a line in a README
or a comment. Repairing one is cheaper than paying its absence once per round.

**Capture once, filter locally.** A command re-run to see its output a
different way returns nothing the first run did not already have. Redirect to a file
and read the file:

```
out=<scratchpad>/<work-item-id>/run.txt; mkdir -p "$(dirname "$out")"
uv run pytest <scope> > "$out" 2>&1; tail -8 "$out"
grep '^FAILED' "$out"                # same run, second question
```

The tell is a second invocation whose only difference is after the pipe.
The file is under the scratchpad and carries the work item id, never a name
every session on the machine would also pick: agents of one session share
one scratchpad, so a generic name is overwritten by a sibling work item's run.

`seal cost` reads a finished transcript and reports the split: command
time, model time between calls, the repeats, and how many tools went out per
turn. None of it is visible from inside the session:

```
seal cost --latest          # newest transcript for this repo
seal cost <transcript.jsonl>
```

## Counterfeits (stop on sight)

- Output quoted from an earlier run: freshness is per tree state, not per
  conversation.
- "Tests pass" for a claim no test covers: green suite, unproven claim.
- Satisfaction vocabulary before the run: should, probably, seems, likely.
- A new test that passed on first run and was never seen red (condition 2).
- Partial evidence generalized: one endpoint checked, "API works" claimed.
- A broad run reported as the gate's pass when edits followed it, including
  the one small fix made after it.
- A pre-existing failure counted as this work's, or waved past without
  being named. Both need the base comparison; neither survives it.
- A narrow command that was green because it opened no files: a linter
  pointed at a directory holding none of its language, a test path that
  collected zero tests. Condition 2 does not relax with the scope.
- A check that stopped before reaching the code it was aimed at: a config
  error, a collection error, two modules under one name. The run ends early
  and cheaply, and "it was fast" reads as "it was clean". It is neither a pass
  nor somebody else's problem: that axis now has no answer, and the honest row
  is `unverified` with the cause named.
- A failure count with no base state behind it. "1 failed" is a claim about
  a change only where what the tree failed before the change is known.
- A deferral to an answerer nobody resolved. "CI covers it" in a repository
  where nothing runs it is the `unverified` label doing the opposite of its
  job: it reads as handled.
