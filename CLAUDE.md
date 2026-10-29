# AgenticSeal

## The core

The core of this project is `skills/core/SKILL.md`, one file for every
party. An agent receives it through the `skills:` list of its definition. A
session receives it through the preset block in `~/.claude/CLAUDE.md`,
whose one line imports the copy in the marketplace clone, which is the last
release's. This file does not import it, because a session here would then
read it twice.

Where the branch changes `skills/core/SKILL.md`, which `git diff --stat
<base>...HEAD -- skills/core/SKILL.md` shows, the tree's copy governs, and
a session here opens it before judging by the installed one. Where the
branch does not change it, the two are one text, except before the release
that first ships the file: until then the installed clone holds no core at
all, and a session here opens the tree's copy whatever the branch changes.
