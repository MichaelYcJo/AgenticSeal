---
name: start
description: |
  Starts a piece of work through the AgenticSeal workflow: opens the core,
  puts the routing question, writes the work item's routing.md before the
  first edit, then runs the work as the orchestrator.
  Use when: a person asks, in plain words, to change code in a repository
  where this plugin is installed, such as to fix a bug, add or change a
  feature, refactor, or work an issue, as in "fix #42" or "이 기능 고쳐줘";
  or types `/agentic:start <issue or request>`.
  NOT for: a question about how code works, a request to review a PR, a diff
  or a branch (`code-review`), or a session already orchestrating a work
  item, which follows `skills/implement/orchestration.md`.
---

# /agentic:start, where the workflow starts

Where this plugin is installed, a plain request to change code reaches this
skill first, and so does a person typing `/agentic:start <issue or
request>`. The session running it becomes the orchestrator of that work,
and the routing question is where the person chooses the route. Invoking
this skill and answering question 1 is the person's consent to the run's
agents and the tokens they spend. A session this skill never reached opens
no core, declares nothing and is outside the workflow, which the first
paragraph of `skills/core/SKILL.md` allows of a session doing other work.

Every path below is the plugin's, relative to `${CLAUDE_PLUGIN_ROOT}`, the
directory two above the base directory the harness printed with this file,
except `seal/`, which resolves as contract rule 11 states. This file names
each section it follows and copies none of them.

The request is: $ARGUMENTS

Where that is empty, the request is the person's message that brought the
session here. Where neither names the work, ask the person which issue or
request to work on, and go on once they name one.

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
`skills/implement/bootstrap.md` and follow it before the next step. The
data directory its stamp question passes is `${CLAUDE_PLUGIN_DATA}`.

**3. Read the ticket.** Read the issue or the request as
`skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket* says, with the documents `skills/implement/SKILL.md` *1. Read the
documents that outrank the code first* names.

**4. Read the work on the ladder.** Judge it on the ladder of
`skills/implement/orchestration.md` *Orchestrator: when a work item is
required*, for which answer of question 1 to mark. The ladder never skips
the question.

**5. Ask once.** Put the batch of `skills/implement/orchestration.md`
*Orchestrator: what needs a person is asked in one batch, before the first
edit*, with question 1 put as *Question 1* states it, with the answer the
ladder reads marked, and the boxes of *Question 2* only under `per axis`,
as *Orchestrator: how the work is routed* says. Where the person answers
`no work item`, make the change as the third answer of *Question 1*
describes, its commits' trailer among it, and take none of the steps below.

**6. Write the declaration before the first edit.** Branch as *Orchestrator:
the order inside a ticket* step 1 says, write
`seal/threads/<work-item-id>/routing.md` from
`templates/records/sdd-routing.md` as *What the answer writes* states, and
commit it. No other file is edited before that commit.

**7. Run the work.** Follow `skills/implement/orchestration.md`
*Orchestrator: the order inside a ticket* from its step 2 on, as the
routing the person answered says.
