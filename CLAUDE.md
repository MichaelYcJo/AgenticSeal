# AgenticSeal

## The core

The core of this project is `skills/core/SKILL.md`, one file for every
party. An agent receives it through the `skills:` list of its definition. A
session receives it from the plugin's `SessionStart` hook, and in this
repository the hook prints the tree's copy, whose path its first line
names, so the tree's core governs a session here and the session reads it
once. This file imports nothing and copies nothing.

Where no hook message opening `AgenticSeal core from` stands in the
session's context, the installed plugin predates the hook, and the session
opens `skills/core/SKILL.md` once. An agent spawned here receives the
installed plugin's copy, the last release's, through `skills:`, as it
receives every other installed skill.

`CONTRIBUTING.md` *What a change to a gate must carry* is where a pull
request to this repository answers the rule `skills/core/SKILL.md` *The
rule a mechanism is kept against* states and the value its *The first
value: efficient development through the workflow* states. The core is read
in every user's repository, so this repository's own files are cited here
and not there.
