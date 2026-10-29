## The goal a design is chosen against

**Verification through an automated workflow is this project's first goal.**
Between two designs that catch the same defect, the one that stops to ask a
person is the more expensive, and the difference has to be argued rather than
assumed. Time and stability are what the argument is being made for.

This is a goal, not a rule, which is why it sits above them: it decides
between options where no rule is broken either way.
`skills/implement/SKILL.md` *1. Read the documents that outrank the code
first* holds the rule this goal produces for a session, with its reasoning:
whatever needs a person is asked once, together, before the first edit, and
nothing comes back mid-run.

## The rule a mechanism is kept against

**A mechanism stays only while its history shows what it caught against what
it costs**; existing is no reason to keep it. A gate that stops a session,
the routing check among them, guards the work a work item owns. A change
that would be routed `no work item`, such as a formatter run, a dependency
bump or an identifier renamed across files by `sed`, is outside that work, so
where only such a change passes through a gap in that kind of gate, the gap
is not a weakness to close. A rule's proof
is the test or behaviour eval its `check:` line names. A fact has one source,
and every other place links to it. A script gates only a fact it reads; a
noisy reading, or one guessed from words, is a script's report, and whether
two things mean the same is an agent's judgment (the section below).
Nothing is kept beside the tree to stay in step with it, such as a stored
count or coordinate. Do
not avoid the change a problem calls for: before a fix adapts to an existing
structure, ask whether the structure should change, and when fixes chase one
mechanism's edge cases, ask what it decides; what exists is a reference, not
a constraint. A thing is re-checked only when the diff or CI shows it
changed. A change rewrites the text it amends in place, and in the same
commit removes what stood on the old fact: a check, an exception, a comment,
a copy. History goes to git, the release notes and the work record.
`CONTRIBUTING.md` *What a change to a gate must carry* is where a pull
request answers this rule and the goal above.

## The rules steer judgment, and a few invariants hold the chain

**A rule here is guidance for a judgment, not a sequence to execute.** The
orchestrator and the agents it spawns read the rules to judge in the
direction this project wants: what to weigh, what each option costs, and
which signals say a path is not converging. A rule written as "when X ends,
do Y" can only be executed, and an orchestrator that executes it relays one
finding after another without asking whether the work converges. Whether two
things mean the same, or give the same result, is the judgment an agent
workflow exists to delegate. The proofer's findings and the sealer's verdict
already gate a pull request on it, so a script does not re-encode that
judgment as one more grammar rule; it reads what a command wrote or what a
real parser returns.

**Judgment is not licence to skip a party.** A few invariants hold the chain
and are not open to judgment: no review without a build, no fix that no
round reads, no seal without the broad run at HEAD, no pull request without
a seal, and no question to a person after the routing answer. Each names
what it protects and is held by a mechanism; a rule that only orders acts,
without one of those protections, is guidance. #1167 lists the invariants
with their mechanisms and rewrites the rules that only sequence acts.

**A judgment is written down with its reasons, so it can be measured.**
Whoever judges, the orchestrator or an agent, writes the decision and the
grounds it weighed into the work item's records under `seal/threads/`, where
the next session reads it and nothing else has to remember it. The guidance
is then improved from that log rather than from memory: the settle, or a
command the owner runs, reads the judgments a release made against what they
cost and what they caught, and rewrites the guidance where a kind of judgment
keeps costing more than it returns.

## Repo rule: the merge method is fixed per direction, and it is not a preference

A pull request into `release/vX.Y.Z` is squashed and one into `main` takes a
merge commit, whichever button a page offers first. The rule and its reasons
are `docs/branch-and-release.md` *Work accumulates on a release branch*.

## Repo rule: no real identifiers in examples or fixtures

A domain in an example or fixture is `example.com` and a user path is
`/Users/x/`, never a real domain, path or organisation name
(`CONTRIBUTING.md` *House rules*).

## Repo rule: text an agent or a check reads has one reading

A session here writes skills, agent definitions, templates and frames, and
the owner's two directions bind every sentence of them. Nothing an agent writes or a check
reads uses a symbol a reader can trip on as syntax, states a value twice, or
takes a spelling a near miss could pass. Shorter is never bought with a
second reading: an instruction names who acts, when, on which file and what
counts as done; a defined term keeps its one meaning; and a thing more than
one party can have is named with whose. `skills/writing-style/SKILL.md`
*에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* states the rules with
their checks.
