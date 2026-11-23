- "The pull request's title takes `fix:`" (`frame/plan.md` *Judgments of the run*, the row on the title's prefix)
- "The same batch decided this issue's direction: the cmd.exe rewriter goes and the gate refuses instead, naming the `\` spelling." (`routing.md` *Why this way*)
- "A separator glued to a word, as in `a&& bin/x` or `echo a^&& bin/x`, is a bound of the reading: the word after it is neither refused nor named." (`frame/plan.md` *Judgments of the run*, the row on the glued separator)
- "Whether `cmd.exe` runs a command name that opens with a drive and `/`, such as `C:/Python/python.exe`, as written." (`gaps.md` *Not verified*, the drive row; who must answer: a measurement, one run of such a name under `cmd.exe` on a Windows machine)
- "What `templates/setup/config.md` *Broad gate* says `cmd.exe` does where the reading and `cmd.exe` differ: that `rem` ignores the `&& bin/test` after it, and that a separator glued to a word, as in `a&& bin/x` or `a &&bin/x`, still separates two commands." (`gaps.md` *Not verified*, the template row; who must answer: a measurement, one run of each value under `cmd.exe` on a Windows machine)
- "Does `uvx ruff check . && uvx ruff format --check . && uv run --no-project tests/run_tests.py -q` run the suite under `cmd.exe` on Windows, with `PYTHONPATH` and `PYTEST_ADDOPTS` kept as the gate sets them?" (`frame/questions.md`, row M1, the question)
- "The spelling of `design.md` *Scope* item 9 stands" (`frame/questions.md`, row M1, the default until answered)
- "No run under `cmd.exe` stands behind what the template says `cmd.exe` does with them" (`gaps.md` *Not verified*, the `@bin/test` row; who must answer: a measurement, one run of each value under `cmd.exe` on a Windows machine)

Closes #1577.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
