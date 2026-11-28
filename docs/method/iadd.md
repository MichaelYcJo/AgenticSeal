# The IADD definition

This document defines IADD: what it is, the principles it stands on, the
names of its parts, and the document that owns the form of each record.
It governs nothing itself. Each principle names the file that states it,
and that file is the rule.

## What IADD is

IADD is Independent AI-Driven Development. Its line is *Zero Self-Approval:
no AI approves its own work.*

A person hands a session one issue. Before the first edit, the session
that runs the work, the orchestrator, asks the person how the work is
routed and everything else only a person can answer, in one batch, and
writes the routing answer into the work item's `routing.md`. Which agents
a work item needs is decided by that answer
(`skills/implement/routing-question.md`), and the orchestrator does what no
agent is spawned for. Where a work item needs them all, a separate agent
takes each part of the work. The framer draws what the work is and how it
is phased. The crafter builds each phase against that frame. The proofer
reviews the diff in rounds, and the crafter fixes what a round finds. In a
migration, the tracer establishes what the original code does. The
orchestrator takes the one broad run of the whole tree. Last, the inspector
reads every party's record against the issue and the tree at one commit
and writes its verdict. The run ends at a pull request whose records carry
that verdict, unless the person asked for the branch back, and a person
merges it.

## The principles

- No party approves its own work: the party that draws the frame does not
  build to it, and each agent reaches its result on its own target without
  leaning on another's (`skills/core/SKILL.md` *Each agent judges its own
  target, independently of the others*, and
  `docs/running/the-agent-set.md` *The party that draws a contract is not
  the party that executes it*).
- An agent judges where the question is what something means, and a
  script answers what it can answer exactly, such as the suite, the lint
  and the merge check (`skills/core/SKILL.md` *Judgment is spent where
  meaning is the question, and a script answers the rest*).
- A judgment stands on a source document and is written into the work
  item's records with its grounds and that document (`skills/core/SKILL.md`
  *A judgment stands on a source document, and is written down with both*).
- The inspection is bound to one commit: its verdict names the commit it
  read, and it lapses once a commit that touches a file other than the
  closing records follows that commit (`docs/forms/the-inspection.md` *The
  three states*).
- What the work needs from a person is asked once, together, before the
  first edit, because asking a person costs more than any other step
  (`skills/core/SKILL.md` *Asking a person is the most expensive step*).
- Some links of the chain no party may skip on its own judgment, and a
  mechanism holds each of them. No review without a build, and no pull
  request without a cleared inspection, are among them (the table of
  `skills/core/SKILL.md` *Judgment is not licence to skip a party*).
- A mechanism, such as a gate, a check or a rule, is kept only while what
  it has caught is worth more than its cost, and each fact is stated in one
  place that the others link to (`skills/core/SKILL.md` *The rule a
  mechanism is kept against*).
- Each party pays for every byte of each file it opens, so a document holds
  what one kind of reader needs at one step (`skills/core/SKILL.md` *A
  document is cut by who opens it and at which step, so a party opens only
  what its step needs*).

## The names

**The product is IADD, and `iadd` is the name of each of its parts**:
the root `iadd/`, the command line, the plugin's `name`, the prefix of
every agent and skill, and the marketplace. Every identifier is lowercase
with no separator, and `IADD` is written only where a person reads the
brand.

| Name | Its one sentence |
|---|---|
| IADD | the plugin, whose one sentence is the first line of `README.md` under its title, and the `description` of `.claude-plugin/plugin.json`; *the IADD process* is what it does with one issue, from the routing question to the final inspector's verdict |
| `iadd` | the command line, the plugin's `name`, the prefix `iadd:` of every agent and skill, and the marketplace's name |
| `iadd/` | the root, visible beside `docs/`, because the work items in flight are what people read while a pull request is open; where it stands in each mode is the opening paragraph of `skills/core/SKILL.md` |
| the thread | one work item: one issue, one branch and one pull request, with one directory that holds its records until the settle after its release |
| `iadd/threads/<id>/` | a thread's directory, with `frame/` for the design before the build, `trail/` for what passed between the parties, and the other records at its top, each placed by what it is and never by which agent wrote it |
| framer, crafter, proofer, inspector, tracer | the agents, each named for its part of one order, which `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each* states |
| the inspection | the inspector's verdict on the work at one commit, and its record `inspection.md`; the stamp and the inspection mark are drawings of it |
| cleared, lapsed, not cleared | the three states of a work item's inspection, which `docs/forms/the-inspection.md` *The three states* defines |
| the settle | the step after a release that writes the released work items' decisions into the policy root, decides every open row of their records, and removes their directories (`skills/settle/SKILL.md`) |
| `IADD-Routing:` | the trailer of a session's commit where the root is shared, naming its work item or reading `no work item` (`skills/commit-pr-convention/SKILL.md`) |

A directory and an agent say what each is to whoever meets it first, so
neither is named for a metaphor. Every shipped artifact is written in
English, because the plugin is for others and every token is paid for.
The language a repository's own records and pull requests are written in
is that repository's answer, which `docs/layout/one-root-by-lifetime.md`
*What the repository decides for itself, and how it is read* states.

The Korean documents name the inspector 검수자, and 최종 검수자 where a
text introduces it as the final inspector. They name the inspection 검수,
and its three states 합격, 효력을 잃음 and 합격 아님. A Korean document
writes the Korean name with the English identifier in parentheses at its
first use, as `검수자(inspector)`. The agent type, the file names, the
verdict words of a `Verdict:` line and every word a script prints stay
English.

## The record forms

Each record of a work item has one document that owns its form.
`docs/layout/the-record-layout.md` *iadd/threads/<work-item-id>/* lists
every file of a work item's directory and the question each answers.

| Record | The document that owns its form |
|---|---|
| `trail/rounds/round-N.md` | `docs/forms/the-round-record.md` *The round record* |
| `inspection.md` | `docs/forms/the-inspection.md` *The inspection* |
| each other file of a work item's directory | `docs/layout/the-record-layout.md` *iadd/threads/<work-item-id>/* |
