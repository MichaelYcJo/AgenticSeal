## The goal a design is chosen against

**Verification through an automated workflow is this project's first goal.**
Between two designs that catch the same defect, the one that stops to ask a
person is the more expensive, and the difference has to be argued rather than
assumed. Time and stability are what the argument is being made for.

This is a goal, not a rule, which is why it sits above them: it decides
between options where no rule is broken either way.
`skills/implement/SKILL.md` *1. Read the spec before the code* holds the rule
this goal produces for a session, with its reasoning: whatever needs a person
is asked once, together, before the first edit, and nothing comes back mid-run.

## The rule a mechanism is kept against

**A mechanism stays only while its history shows what it caught against what
it costs**; existing is no reason to keep it. A rule's proof is the test or
behaviour eval its `check:` line names. A fact has one source, and every
other place links to it. A check gates only a fact it reads; a noisy reading,
or one guessed from words, is a report. Nothing is kept beside the tree to
stay in step with it, such as a stored count or coordinate. Do not avoid the
change a problem calls for: before a fix adapts to an existing structure, ask
whether the structure should change, and when fixes chase one mechanism's
edge cases, ask what it decides; what exists is a reference, not a
constraint. A thing is re-checked only when the diff or CI shows it
changed. A change rewrites the text it amends in place, and in the same
commit removes what stood on the old fact: a check, an exception, a comment,
a copy. History goes to git, the changelog and the work record.
`CONTRIBUTING.md` *What a change to a gate must carry* is where a pull
request answers this rule and the goal above.

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
