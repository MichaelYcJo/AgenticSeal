# AgenticSeal

## The core

The core of this project is `skills/core/SKILL.md`, one file for every
party. An agent receives it through the `skills:` list of its definition. A
session receives it when `/agentic:start` opens it, and in this repository
the entry opens the tree's copy, so the tree's core governs a session here
and the session reads it once. A session that never types `/agentic:start`
is outside the workflow and bound by nothing in the core. This file imports
nothing and copies nothing.

An agent spawned here receives the installed plugin's copy, the last
release's, through `skills:`, as it receives every other installed skill.

`CONTRIBUTING.md` *What a change to a gate must carry* is where a pull
request to this repository answers the rule `skills/core/SKILL.md` *The
rule a mechanism is kept against* states and the value its *The first
value: efficient development through the workflow* states. The core is read
in every user's repository, so this repository's own files are cited here
and not there.
