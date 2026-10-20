---
name: agent-contract
description: |
  The rules every SpecSeal agent works under — smith, warden, scribe, and any
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
`skills:` list in your definition. Its sections are the rules true of any
agent — smith, warden, framer, sealer, scribe, and whichever arrives next —
and nothing here is one agent's own. A role's rules live in that role's
definition, and a rule that would need a per-role exception here is not
universal. Your spawn prompt carries what is specific to the round and never
has to carry these; it cites them by number. From this edition a section
number is never reused and never re-ordered: a rule that retires keeps its
number as one line naming what replaced it, and a new rule takes the next
number.

## §1 Read exit codes directly, never through a pipe

`cmd >/dev/null 2>&1; echo $?` — never `cmd | tail; echo $?`, which reports
the pipe's status and is always 0. Both forms are written out because the
failure is a habit, and the right form has to be as easy to copy as the
wrong one.
check: tests/test_the_agent_contract_holds_the_universal_rules.py

## §2 Narrow and often; the broad gate is the orchestrator's

Run the tests for the slice you touched while you work, and your module and
the ones it touches at a phase boundary. The broad gate — the full suite, the
repository-wide lint, the typecheck — is one act, taken once after the review
rounds settle, and no agent runs any of the three. The orchestrator runs
`broad-gate --base <base> --record <item>` with nothing else running, then
spawns the sealer, which reads the record that run wrote. Hand over with the
suite labelled `unverified` and the orchestrator named as its answerer: a
suite that is not mentioned reads as a suite that passed.
check: tests/test_the_agent_contract_holds_the_universal_rules.py tests/test_broad_gate_rule.py

## §3 A spawn prompt cannot widen the verification scope

The prompt that spawns you is a request, not an amendment to this contract.
It ranks where a ticket ranks — above the code as it happens to be, below
the documents that were ratified. When it orders a check §2 excludes, do not
run it: decline, and name the instruction in your hand-back in one line —
what was asked, and which rule refused it. A prompt that narrows your scope
— one module, one test — is the caller doing its job, and you follow it.
When you cannot tell which it is, run nothing extra and say in the hand-back
which reading you took; every ambiguity in this file falls that way, toward
disclosure.
check: tests/test_the_agent_contract_holds_the_universal_rules.py

## §4 Label what was executed apart from what was read

Never record something as passing that you did not run. Every report labels
each claim `executed`, `read` or `unverified` — the `verify` skill's labels
— and what is `unverified` names who answers it: a deferral to nobody is how
*someone will look at it* becomes *nobody did*.
check: tests/test_the_agent_contract_holds_the_universal_rules.py

## §5 Nothing that reaches you in prose is evidence

A fact your prompt hands you is a claim with a coordinate to open, or a label
saying nobody opened it. A fact with neither is an assertion nobody has
opened: open it before you build on it, and say what you found. An
aggregate — a count, a total — is not a coordinate: the number can be
checked while the claim it stands for cannot. For a reviewer the
implementer's account is a claim, not evidence; for an implementer the
handoff's facts are opened before anything is built on them.
check: tests/test_the_agent_contract_holds_the_universal_rules.py

## §6 You return a report

What you write is named in your own definition and nothing else. A durable
record — a file that outlives the round, a cell inside one, a mark on the
tree — is yours only where your own file names it, and a definition that
names no write names none. Whatever a definition says, four acts are
withheld from every agent: post nothing, push nothing, open no pull request,
and spawn no agent. Your final output is the report, and what is done with
it is the caller's act.
check: tests/test_every_agent_reads_the_contract.py

## §7 A probe is named `test_tmp_*`, one file, run once, deleted

Probe only what reading cannot settle. A probe is one file named
`test_tmp_*`, it runs once, and it is deleted before you hand over. The rule
is about leavings, not about files: A probe leaves nothing behind, whatever
kind of thing it made — a worktree, a branch, a checkout, a scratch clone, a
virtual environment — and those are examples, not a list. What the probe
made for ITSELF is what goes: a thing the repository's own tooling builds to
be reused, such as the one virtual environment a test runner keeps, stays
even when your probe's run created it. The question is whose the thing is,
never who happened to trigger it.
check: tests/test_the_agent_contract_holds_the_universal_rules.py

## §8 Drive git from Python when a probe needs a repository

A probe that commits reaches the commit gate exactly as real work does, and
the prompt lands on whoever is at the keyboard — which, in a round you are
running, is nobody who is driving the session. Prefer
`subprocess.run(["git", "-C", d, "commit", …])` from a Python script: no
Bash command line carries the commit, so no gate reads one, and several
probes in one script cost one tool call rather than one each. From Bash,
write the path out — `git -C /abs/path/r1 …` — because the reader also fills
in a name the command assigned itself, but not a loop variable, so a loop
over `$n` still prompts once per value. The waiver, `: '[no-review]';` in
front of the command, is the last resort: it waives one command, quotes
included and before it, because after the subcommand a bare word is a
pathspec and git rejects it.
check: tests/test_a_probe_that_commits_says_so.py

## §9 Edits go through the `Edit` tool

Two reasons point the same way. An edit must be able to fail: a substitution
routed through the shell does nothing, says nothing, and exits zero when its
pattern misses, and the miss surfaces at the next check as another edit and
another run. Where the environment leaves no choice, assert that every
substitution matched.

And no Bash command line exists, so the commit gate has nothing to read. The
gate reads a heredoc body as shell, on purpose, with one exception named
below, and two kinds of segment count. One is a segment whose command word
is `git` with the `commit` subcommand, whatever the outer command does with
the body — a patch to a file carrying shell commands as test data, or to a
document showing a waiver example verbatim, can leave a commit in command
position. That is why a fixture file can read clean whole and trip as a
fragment: what counts is the position, never the presence of the word. A
string a shell would run is a position too — the one `sh -c` is handed, or
the inside of `$( … )` or a backtick pair — so a file whose strings hold a
commit there trips whole. The other has no commit in it at all: an `eval`
whose argument holds a variable, a command substitution or a glob
stops the session, because nothing can tell what it reduces to without
running the shell, and the gate fails closed. So searching your patch for a
commit and finding none does not clear it.

The exception is one shape the gate matches byte for byte, and its body is
data: `cat`, `tee` or `python3 -` fed by `<<` and a delimiter in single
quotes, on a first line with nothing before the command, and nothing after
the terminator when the body goes to a file. Any other spelling of the same
body is read as shell, and the exception changes nothing about the first
reason: an edit made through the shell still cannot fail the way an `Edit`
call does. The grammar, slot by slot, has one home, and a session spelling a
heredoc any other way reads it there first: `docs/commit-review-gate-spec.md`
§*A file edit goes through the `Edit` tool*.

That second reason is about a reader, and since #692 the reader judges a
commit only where git's hooks cannot: a clone whose hooks slot is somebody
else's, an opted-in clone no session has reached yet, a target it cannot
place from a session whose own clone carries no hooks, and every command
whose shape is not known plain (only `git`'s plain commits beside a few
harmless words like `cd` and `echo`, with nothing a shell parses again and
no assignment, are plain). Everywhere else — every
opted-in clone a session reaches, unless `core.hooksPath` or a hook file it
did not write holds the slot — git judges
a commit inside the commit, in the worktree it lands in, and no command text
is read for it (`docs/the-commit-gate-inside-git.md` §*The commit gate inside
git*). The first reason holds everywhere, and it is the one that makes this
rule yours.
check: tests/test_edits_go_through_the_edit_tool.py

## §10 Batch independent reads and runs

Open every file a coordinate names in one call; run the cases from one file
in one command. A round is mostly round-trips and command waits, so cut the
trips and never the investigation: an axis you skipped is not a pass, and
the requirements read, where every file the handoff names can be opened in
one call, has no excuse. An edit-test loop is serial — a call whose input
depends on the last result cannot go out with it — and a review reads
independent things, which is where batching pays most. The bar each kind of
segment is judged by is `docs/the-review-record.md` §*The per-segment bars*,
and no definition states a second copy of it.
check: tests/test_a_moved_rule_leaves_its_definition.py

## §11 Where the `seal/` root is, and the language its records are written in

Every `seal/…` path here and in the skills means `<repo>/seal/` where that
directory exists, and `$(git rev-parse --git-common-dir)/seal/` otherwise —
local mode, where the root sits under the common git directory and nothing
under it is committed. A repository with both is shared, and no config key
decides it. The prose in the records follows `Record language` in
`config.md` under that root — English when the row is absent. What stays
English regardless: the field names and vocabulary a checker reads (`Target
SHA`, the verdict words, the `<!-- -->` markers), and all code. The
`implement` skill's *The language the records are written in* holds the
whole list.
check: tests/test_the_agent_contract_holds_the_universal_rules.py

## §12 A defect belongs to a class — enumerate the class

Do not fix the coordinate. A finding names an instance; the fix is owed to
every instance the same cause produces, and the hand-back says which were
enumerated.
check: tests/test_the_agent_contract_holds_the_universal_rules.py

## §13 A defence resting on a platform guarantee is not verified

Not until the guarantee is removed and the code still refuses: a run with
the guarantee in place cannot tell the defence from the platform.
check: tests/test_the_agent_contract_holds_the_universal_rules.py

## §14 A fix that changes what a person sees documents it and pins it

In the same commit. *Nothing raises* is not the claim *says this*: a change
to a message, a verdict or a rendered line is a change someone reads and acts
on, and the test that pins the new text is what keeps the next edit from
quietly taking it back.
check: tests/test_the_agent_contract_holds_the_universal_rules.py

## §15 A new case is not planted until it has been seen red

Show the case failing — against the old code, or with the sentence it pins
deleted — before it is committed as a case, and say in the hand-back how it
was shown. A case that passes against the defect it was written for pins
nothing, and reverting the fix is what catches one.
check: tests/test_the_agent_contract_holds_the_universal_rules.py

## §16 A commit names its repository in the command that makes it

Commit with the repository's absolute path written out after `git -C`, in a
command of its own. Where a `cd` comes first, join it to the commit with `&&`
and nothing else. A probe's commit is §8's, and a file edit is §9's.

Two reasons, and they are two different facts about the gate. First, your
shell starts in the session's directory at every call, so a command reaches
your worktree through a `cd`, and whatever follows a `;` or a new line after
that `cd` also runs where a failed `cd` leaves the shell: the session's own
directory. The gate judges the commit in both places, because both can
happen, and the session's directory is usually one no declaration names.
Second, the gate reads a command before the shell expands it, so a loop
variable in the path names no directory at all, and a commit it cannot place
stops the same way. Both are about the reading of a command, which judges a
commit only where git's hooks cannot — §9 names the four places — and the
shape above is still the one to write: a person reading the transcript can
follow it, and it is the only one the reading can place where it still
judges.
check: tests/test_a_commit_names_its_repository.py

## §17 Clean up only what you started

An agent cleans up only the processes and files it started. Record the PID
of every process you start and the path of every file and directory you
create, and stop or remove by that record; never kill by command name, and
never delete in a shared directory by glob — another session's process or
file answers to the same name. A leftover you did not start is reported in
the hand-back, not removed.
check: tests/test_the_agent_contract_holds_the_universal_rules.py

## §18 A check that refuses correct code is fixed or reported

When a check refuses code that is correct, fix the check or report the
refusal in the hand-back, quoted; never bend the code to pass it. Code
shaped around a wrong check carries the check's defect into the tree and
hides it from the next reader.
check: tests/test_the_agent_contract_holds_the_universal_rules.py

## §19 A change rewrites the text it amends in place

A change rewrites the text it amends where that text stands, and in the
same commit removes or corrects what stood on the old fact — every other
sentence, case and citation stating it, found with `git grep` on its words.
A correction written beside the sentence it corrects leaves both for the
next reader to choose between.
check: tests/test_the_agent_contract_holds_the_universal_rules.py

## §20 Do not avoid the change a problem calls for

A structure in the tree is a reference, not a constraint. Weigh replacing it
as an equal of keeping it, and when you conclude something should stay,
check the premise that keeps it before you rest on it. The change a problem
calls for, avoided, leaves the problem in place under a smaller edit.
check: tests/test_the_agent_contract_holds_the_universal_rules.py
