- "**Every phase boundary and every fix pass runs the repository's tree-wide test files, and a phase no longer pays for test files that only write a changed path's name into a fixture (#1441).**" (`changelog.md` *Fixed*, the first item)
- "A fix pass ran "what the fix touches", which reached no file that reads the whole tree, so a guard over the records or the documents failed first at the broad gate." (`changelog.md` *Fixed*, the first item)
- "A test file reads a path when its cases open it, import it or load it, directly or through another test file, and a file that writes the path's name only into a fixture, a parameter or a docstring does not." (`changelog.md` *Fixed*, the first item)
- "**This repository's tree-wide test files are `tests/text/` and `tests/behaviour/`, the files that declare no `TARGET`, and every case that reads the repository's own tree stands in one of them.**" (`changelog.md` *Fixed*, the second item)
- "The pull request's title takes `fix:`, and the kind that came closest is `chore:`." (`frame/plan.md` *Judgments of the run*, the prefix row)
- "whether a case that takes a temporary directory still reads this repository's tree through a command's default root without naming `ROOT`" (`gaps.md` *Not verified*, the third row)

Closes #1441.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
