# AgenticSeal

## The core

The core of this project is `skills/core/SKILL.md`, one file for every
party. An agent receives it through the `skills:` list of its definition. A
session receives it from the plugin's `SessionStart` hook, which prints it
where the session's repository holds a `seal/` root. This repository is a
clone of the plugin and holds a marked root, so the hook prints the tree's
copy here, the tree's core governs a session here, and the session reads it
once. A session whose context holds no output opening
`AgenticSeal core from` opens `skills/core/SKILL.md` once. This file
imports nothing and copies nothing.

An agent spawned here receives the installed plugin's copy, the last
release's, through `skills:`, as it receives every other installed skill.

`CONTRIBUTING.md` *What a change to a gate must carry* is where a pull
request to this repository answers the rule `skills/core/SKILL.md` *The
rule a mechanism is kept against* states and the value its *The first
value: efficient development through the workflow* states. The core is read
in every user's repository, so this repository's own files are cited here
and not there.
