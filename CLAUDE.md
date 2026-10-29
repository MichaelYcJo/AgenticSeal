# AgenticSeal

## The first value: efficient development through the workflow

**This project exists for efficient development through an agent workflow,
and two things make it: the ability to judge where judgment is needed, and
the source documents a judgment is made against.** Neither does it alone. An
agent that judges everything spends more tokens than the work is worth and
drifts from what the project decided; an agent that only runs scripts and
sequences is a relay that adds nothing a script would not. Verification
through the workflow serves this value, and time and stability are what it
is argued for. The value decides between designs where no rule below is
broken either way, which is why it sits above them.

**Judgment is spent where meaning is the question, and a script answers the
rest.** Whether two things mean the same, or give the same result, is the
judgment the workflow exists to delegate, and the proofer's findings and the
sealer's verdict already gate a pull request on it. A script that answers
"these differ" where the meaning is the same is the worst result the
workflow can give, so a script does not re-encode that judgment as one more
grammar rule: it reads what a command wrote or what a real parser returns.
What a script answers exactly, the suite, the lint, the broad gate, the
merge check, stays a script, and the session waits on its exit code rather
than reasoning about what it would print.

**A rule is guidance for a judgment, not a sequence to execute.** The
orchestrator and the agents it spawns read the rules to judge in the
direction this project wants: what to weigh, what each option costs, and
which signals say a path is not converging. A rule written as "when X ends,
do Y" can only be executed, and an orchestrator that executes it relays one
finding after another without asking whether the work converges.

**A judgment stands on a source document, and is written down with both.**
The source documents are this file and the ones that outrank the code, in
the order `skills/implement/SKILL.md` *1. Read the documents that outrank
the code first* gives: the policy root, the work item's design, then the
issue. Whoever judges, the orchestrator or an agent, names the document it
judged against, and writes the decision, the grounds it weighed and that
source into the work item's records under `seal/threads/`, where the next
session reads it and nothing else has to remember it. The guidance is then
improved from that log rather than from memory: the settle, or a command
the owner runs, reads the judgments a release made against what they cost
and what they caught, rewrites the guidance where a kind of judgment keeps
costing more than it returns, and writes the source where a judgment had
none to stand on.

**Asking a person is the most expensive judgment.** Between two designs
that catch the same defect, the one that stops to ask a person costs more,
and the difference has to be argued rather than assumed. Whatever needs a
person is asked once, together, before the first edit, and nothing comes
back mid-run; `skills/implement/SKILL.md` *1. Read the documents that
outrank the code first* holds that rule with its reasoning.

**Judgment is not licence to skip a party.** A few invariants hold the chain
and are not open to judgment: no review without a build, no fix that no
round reads, no seal without the broad run at HEAD, no pull request without
a seal, and no question to a person after the routing answer. Each names
what it protects and is held by a mechanism; a rule that only orders acts,
without one of those protections, is guidance. #1167 lists the invariants
with their mechanisms and rewrites the rules that only sequence acts.

## The rule a mechanism is kept against

**A mechanism stays only while its history shows what it caught against what
it costs**; existing is no reason to keep it. A gate that stops a session,
the routing check among them, guards the work a work item owns. A change
that would be routed `no work item`, such as a formatter run, a dependency
bump or an identifier renamed across files by `sed`, is outside that work, so
where only such a change passes through a gap in that kind of gate, the gap
is not a weakness to close. A rule's proof is the test or behaviour eval its
`check:` line names. A fact has one source, and every other place links to
it. A script gates only a fact it reads in that closed form; a noisy
reading, or one guessed from words, is its report. Nothing is kept beside
the tree to stay in step with it, such as a stored count or coordinate. Do
not avoid the change a problem calls for: before a fix adapts to an existing
structure, ask whether the structure should change, and when fixes chase one
mechanism's edge cases, ask what it decides; what exists is a reference, not
a constraint. A thing is re-checked only when the diff or CI shows it
changed. A change rewrites the text it amends in place, and in the same
commit removes what stood on the old fact: a check, an exception, a comment,
a copy. History goes to git, the release notes and the work record.
`CONTRIBUTING.md` *What a change to a gate must carry* is where a pull
request answers this rule and the value above.

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
the owner's two directions bind every sentence of them. Nothing an agent
writes or a check reads uses a symbol a reader can trip on as syntax or
states a value twice, and a line a script reads is in the one form the
script reads; whether a line written otherwise meant the same is an agent's
judgment. Shorter is never bought with a second reading: an instruction
names who acts, when, on which file and what counts as done; a defined term
keeps its one meaning; and a thing more than one party can have is named
with whose. `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한
가지로만 읽히게 쓴다* states the rules with their checks.
