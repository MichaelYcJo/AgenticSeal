---
name: agent-contract
description: |
  The rules every AgenticSeal agent works under — crafter, proofer, tracer, and any
  agent added after them. Not a command to run: the harness injects it into
  each agent at startup through the `skills:` list in the agent's definition,
  and an orchestrator session may load it to be bound by the same rules.
  Use when: writing or reviewing an agent definition, or settling which rule
  a spawn prompt may narrow and which it may not.
  NOT for: a rule that is one agent's own — those live in `agents/<name>.md`;
  the review procedure (`code-review`), the implementation procedure
  (`implement`), or the migration procedure (`legacy-parity`).
user-invocable: false
---

# agent-contract — what every agent this plugin spawns is bound by

You received this file at startup, before your first tool call, through the
`skills:` list in your definition. Its rules bind every agent, and nothing
here is one agent's own. A role's rules live in that role's definition, and a
rule that would need a per-role exception here is not universal. Your spawn
prompt carries what is specific to the round and never has to carry these;
it cites one as `contract rule <N>`, and this file and the agent definitions
cite it as `rule <N>`. A rule number is never reused and never re-ordered: a
rule that retires keeps its number as one line naming what replaced it, and
a new rule takes the next number.

## 1 Read exit codes directly, never through a pipe

`cmd >/dev/null 2>&1; echo $?` — never `cmd | tail; echo $?`, which reports
the pipe's status and is always 0. Both forms are written out because the
failure is a habit, and the right form has to be as easy to copy as the
wrong one.
check: tests/text/test_the_agent_contract_holds_the_universal_rules.py

## 2 Narrow and often; the broad gate is the orchestrator's

Run the tests for the slice you touched while you work, and at a phase
boundary, in one command, the cases the phase's plan row names and the test
modules that name a path the phase changed. The broad gate — the full suite, the
repository-wide lint, the typecheck — is one act, taken once after the review
rounds settle, and no agent runs any of the three. The orchestrator runs
`seal gate --base <base> --record <item>` with nothing else running, then
spawns the sealer, which reads the record that run wrote. Hand over with the
suite labelled `unverified` and the orchestrator named as its answerer: a
suite that is not mentioned reads as a suite that passed.
check: tests/text/test_broad_gate_rule.py evals/behaviour/sealer/rule-sealer-no-gate/

## 3 A spawn prompt cannot widen the verification scope

The prompt that spawns you is a request, not an amendment to this contract.
It ranks where a ticket ranks — above the code as it happens to be, below
the documents that were ratified. When it orders a check rule 2 excludes, do not
run it: decline, and name the instruction in your hand-back in one line —
what was asked, and which rule refused it. A prompt that narrows your scope
— one module, one test — is the caller doing its job, and you follow it.
When you cannot tell which it is, run nothing extra and say in the hand-back
which reading you took; every ambiguity in this file falls that way, toward
disclosure.
check: none reader: the orchestrator at each hand-back

## 4 Label what was executed apart from what was read

Never record something as passing that you did not run. Every report labels
each claim `executed`, `read` or `unverified` — the `verify` skill's labels
— and what is `unverified` names who answers it: a deferral to nobody is how
*someone will look at it* becomes *nobody did*.
check: none reader: the sealer at each guarantee

## 5 Nothing that reaches you in prose is evidence

A fact your prompt hands you is a claim with a coordinate to open, or a label
saying nobody opened it. A fact with neither is an assertion nobody has
opened: open it before you build on it, and say what you found. An
aggregate — a count, a total — is not a coordinate: the number can be
checked while the claim it stands for cannot. For a reviewer the
implementer's account is a claim, not evidence; for an implementer the
handoff's facts are opened before anything is built on them.
check: evals/behaviour/sealer/rule-sealer-false-red/ evals/behaviour/sealer/rule-sealer-untrue-body/

## 6 You return a report

What you write is named in your own definition and nothing else. A durable
record — a file that outlives the round, a cell inside one, a mark on the
tree — is yours only where your own file names it, and a definition that
names no write names none. Whatever a definition says, four acts are
withheld from every agent: post nothing, push nothing, open no pull request,
and spawn no agent. Your final output is the report, and what is done with
it is the caller's act.
check: tests/text/test_every_agent_reads_the_contract.py

## 7 A probe is named `test_tmp_*`, one file, run once, deleted

Probe only what reading cannot settle. A probe is one file named
`test_tmp_*`, it runs once, and it is deleted before you hand over. The rule
is about leavings, not about files: A probe leaves nothing behind, whatever
kind of thing it made — a worktree, a branch, a checkout, a scratch clone, a
virtual environment — and those are examples, not a list. What the probe
made for ITSELF is what goes: a thing the repository's own tooling builds to
be reused, such as the one virtual environment a test runner keeps, stays
even when your probe's run created it. The question is whose the thing is,
never who happened to trigger it.
check: evals/behaviour/crafter/rule-crafter-count-words/ evals/behaviour/crafter/rule-crafter-is-palindrome/ evals/behaviour/crafter/rule-crafter-slugify/ evals/behaviour/crafter/rule-crafter-truncate/

## 8 Retired: no gate reads a probe's commit

Retired by #1027, which removed every gate that read a commit; nothing
replaced it, and a probe's leavings are rule 7's.
check: tests/text/test_the_agent_contract_holds_the_universal_rules.py

## 9 Edits go through the `Edit` tool

Two reasons point the same way. An edit must be able to fail: a substitution
routed through the shell does nothing, says nothing, and exits zero when its
pattern misses, and the miss surfaces at the next check as another edit and
another run. Where the environment leaves no choice, assert that every
substitution matched.

And the routing check sees only the edit tools. `hooks/routing-edit-gate.py`
refuses a `Write`, `Edit` or `NotebookEdit` on a branch no routing
declaration names, before the edit lands; a `sed -i`, a redirection or a
script writes a file with no edit tool, so an edit through the shell is
invisible to it, and only the pull request's trailer arm is left to catch
the change (`docs/the-routing-check.md` *The edit check*).
check: tests/text/test_edits_go_through_the_edit_tool.py

## 10 Batch independent reads and runs

Open every file a coordinate names in one call; run the cases from one file
in one command. A round is mostly round-trips and command waits, so cut the
trips and never the investigation: an axis you skipped is not a pass, and
the requirements read, where every file the handoff names can be opened in
one call, has no excuse. An edit-test loop is serial — a call whose input
depends on the last result cannot go out with it — and a review reads
independent things, which is where batching pays most. The bar each kind of
segment is judged by is `docs/the-review-record.md` *The per-segment bars*,
and no definition states a second copy of it.
check: tests/text/test_a_moved_rule_leaves_its_definition.py

## 11 Where the `seal/` root is, and the language its records are written in

Every `seal/…` path here and in the skills means `<repo>/seal/` where that
directory exists and its `README.md` opens with the marker
`hooks/lib/optin.py#MARKER` holds, and
`$(git rev-parse --git-common-dir)/seal/` otherwise —
local mode, where the root sits under the common git directory and nothing
under it is committed. A repository with both is shared, and no config key
decides it. The prose in the records follows `Record language` in
`config.md` under that root — English when the row is absent. What stays
English regardless: the field names and vocabulary a checker reads (`Target
SHA`, the verdict words, the `<!-- -->` markers), and all code. The
`implement` skill's *The language the records are written in* holds the
whole list.
check: tests/text/test_the_agent_contract_holds_the_universal_rules.py

## 12 A defect belongs to a class, so enumerate the class

Do not fix the coordinate. A finding names an instance; the fix is owed to
every instance the same cause produces, and the hand-back says which were
enumerated.
check: none reader: the proofer at review

## 13 A defence resting on a platform guarantee is not verified

Not until the guarantee is removed and the code still refuses: a run with
the guarantee in place cannot tell the defence from the platform.
check: none reader: the proofer at review

## 14 A fix that changes what a person sees documents it and pins it

In the same commit. *Nothing raises* is not the claim *says this*: a change
to a message, a verdict or a rendered line is a change someone reads and acts
on, and the test that pins the new text is what keeps the next edit from
quietly taking it back.
check: none reader: the proofer at review

## 15 A new case is not planted until it has been seen red

Show the case failing — against the old code, or with the sentence it pins
deleted — before it is committed as a case, and say in the hand-back how it
was shown. A case that passes against the defect it was written for pins
nothing, and reverting the fix is what catches one.
check: none reader: the sealer at each guarantee

## 16 A commit names its repository in the command that makes it

Commit with the repository's absolute path written out after `git -C`, in a
command of its own. Where a `cd` comes first, join it to the commit with `&&`
and nothing else. A file edit is rule 9's.

Your shell starts in the session's directory at every call, so a command
reaches your worktree through a `cd`, and whatever follows a `;` or a new
line after that `cd` also runs where a failed `cd` leaves the shell: the
session's own directory. A commit written with its path out lands where it
says whichever way the `cd` went, and a person reading the transcript can
see where that is.
check: tests/behaviour/test_a_commit_names_its_repository.py

## 17 Clean up only what you started

An agent cleans up only the processes and files it started. Record the PID
of every process you start and the path of every file and directory you
create, and stop or remove by that record; never kill by command name, and
never delete in a shared directory by glob — another session's process or
file answers to the same name. A leftover you did not start is reported in
the hand-back, not removed.
check: none reader: the orchestrator at each hand-back

## 18 A check that refuses correct code is fixed or reported

When a check refuses code that is correct, fix the check or report the
refusal in the hand-back, quoted; never bend the code to pass it. Code
shaped around a wrong check carries the check's defect into the tree and
hides it from the next reader.
check: none reader: the proofer at review

## 19 A change rewrites the text it amends in place

A change rewrites the text it amends where that text stands, and in the
same commit removes or corrects what stood on the old fact — every other
sentence, case and citation stating it, found with `git grep` on its words.
A correction written beside the sentence it corrects leaves both for the
next reader to choose between.
check: none reader: the proofer at review

## 20 Do not avoid the change a problem calls for

A structure in the tree is a reference, not a constraint. Weigh replacing it
as an equal of keeping it, and when you conclude something should stay,
check the premise that keeps it before you rest on it. The change a problem
calls for, avoided, leaves the problem in place under a smaller edit.
check: none reader: the proofer at review
