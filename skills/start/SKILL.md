---
name: start
description: Start a piece of work through the AgenticSeal workflow. Opens the core, asks the routing question once, writes the work item's routing.md before the first edit, then runs the work as the orchestrator.
disable-model-invocation: true
---

# /agentic:start, where the workflow starts

The person types `/agentic:start <issue or request>`, and the session
running it becomes the orchestrator of that work. Typing the command and
answering question 1 is the person's consent to the run's agents and the
tokens they spend. A session that never types it opens no core, declares
nothing and is outside the workflow, which the first paragraph of
`skills/core/SKILL.md` allows of a session doing other work.

Every path below is the plugin's, relative to `${CLAUDE_PLUGIN_ROOT}`, the
directory two above the base directory the harness printed with this file,
except `seal/`, which resolves as contract rule 11 states. This file names
each section it follows and copies none of them.

The request is: $ARGUMENTS

Where nothing follows the command, ask the person which issue or request to
work on, and go on once they name one.

## Procedure

**1. Open the core once.** Read `${CLAUDE_PLUGIN_ROOT}/skills/core/SKILL.md`
whole. Where the repository's top level holds `.claude-plugin/plugin.json`
whose `name` is the `name` of `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`,
and holds `skills/core/SKILL.md`, the repository is a clone of this plugin:
read the tree's copy in place of the plugin's, so the tree's core governs
there. Open one of the two, and only once in the session; where the session
already holds it since its last compaction, do not open it again.

**2. Find the root.** Where no `seal/` whose `README.md` opens with the
marker stands at `<repo>/seal/` or at
`$(git rev-parse --git-common-dir)/seal/`, open
`skills/implement/bootstrap.md` and follow it before the next step.

**3. Read the ticket.** Read the issue or the request as
`skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket* says, with the documents `skills/implement/SKILL.md` *1. Read the
documents that outrank the code first* names.

**4. Decide whether a work item opens.** Judge the work on the ladder of
`skills/implement/orchestration.md` *Orchestrator: when a work item is
required*. Where the ladder puts the change on its last rung, no work item
opens: say so to the person, and make the change as the third answer of
*Question 1* describes, its commits' trailer among it. The steps below are
then not taken.

**5. Ask once.** Put the batch of `skills/implement/orchestration.md`
*Orchestrator: what needs a person is asked in one batch, before the first
edit*, with question 1 put as *Question 1* states it, `automation` first,
and the boxes of *Question 2* only under `per axis`, as *Orchestrator: how
the work is routed* says.

**6. Write the declaration before the first edit.** Branch as *Orchestrator:
the order inside a ticket* step 1 says, write
`seal/threads/<work-item-id>/routing.md` from
`templates/records/sdd-routing.md` as *What the answer writes* states, and
commit it. No other file is edited before that commit.

**7. Run the work.** Follow `skills/implement/orchestration.md`
*Orchestrator: the order inside a ticket* from its step 2 on, as the
routing the person answered says.
