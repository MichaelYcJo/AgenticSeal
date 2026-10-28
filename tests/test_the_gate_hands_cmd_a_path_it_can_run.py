"""The broad gate hands `cmd.exe` a command name it can run (#448).

`broad_gate.run(..., shell=True)` hands the `Broad gate` row to `%COMSPEC%`,
and on Windows that is `cmd.exe`, which reads a `/` inside a command NAME as
the start of a switch. `bin/test -q && …` ran a command called `bin` with the
argument `/test`, the shell said "not recognized" and exited 1, and the
failure form reported the suite as failing. `bin/test.cmd` exists so that
`cmd.exe` can call the runner, and it is reached as `bin\\test`.

#942 moved the cases of `skills/verify/scripts/broad_gate.py` from this file
into `tests/skills/test_broad_gate.py`: `Test_handed_to_shell`,
`Test_command_names_backslashed`, `Test_run`, `Test_failure_lines` and
`Test_module` hold them. What stays reads `templates/setup/config.md`, which #923
places.
"""

import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def test_the_template_says_which_positions_are_rewritten():
    """A2, the reader's half (contract rule 14). `templates/setup/config.md` *Broad gate* is
    where a person writing the row learns what `cmd.exe` is handed, and it
    states the rule and names the positions the scan leaves as written —
    the gap `tests/skills/test_broad_gate.py`'s cases pin is only a gap nobody is surprised by while
    it is written down. It must not read as a complete count of them."""
    path = os.path.join(ROOT, "templates", "setup", "config.md")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    section = text.split("## Broad gate", 1)[1].split("\n## ", 1)[0]
    prose = " ".join(section.split())
    for needle in (
        "the gate hands it the row with `/` written `\\` inside a command name "
        "that starts in a directory, and nowhere else",
        "It starts in a directory where the part before its first `/`, with its "
        "quotes and carets removed and every leading `@` dropped, names a "
        "directory that exists where the row runs",
        # Round 1's 🟡 3, where the person typing the row reads it; #616
        # narrowed it to the plain form and named what is not expanded.
        "A plain `%VAR%` in that part is expanded first, because `cmd.exe` "
        "expands it before it reads the name",
        "`%CD%` as the directory the row runs in unless the environment defines `CD`",
        "A substring or substitution (`%VAR:~0,2%`, `%VAR:a=b%`) is not "
        "expanded, so a name that starts with one keeps its `/`",
        "`bin/test` then runs as `bin\\test`",
        "a path after `call`, `start` or `if`, or after `else`, `for … do` and "
        "`cmd /c`",
        "the definition above is the rule, and these are examples of it "
        "rather than the whole list",
        "a `/` written straight after one of `cmd.exe`'s own commands, which "
        "is that command's switch (`rd/s/q build`)",
        "a command name after a redirection that opens its command "
        "(`>out.txt bin/test`)",
        "the gate prints one line saying what `cmd.exe` was handed",
        # #596, written where the person typing the row reads it.
        "A `/` written straight after any other program's name reaches "
        "`cmd.exe` as written too",
        "`xcopy/e/i` stays `xcopy/e/i`",
        "A blank before the switch (`xcopy /e`) works as well",
        # And its two bounds, named rather than claimed away.
        "A directory an earlier command in the row makes, or one a `cd` "
        "earlier in the row enters, is not seen",
        "a directory at the root named like a program the row calls with a "
        "glued switch (an `xcopy/` directory) makes `xcopy/e` read as a path",
    ):
        assert needle in prose, (
            f"`templates/setup/config.md` *Broad gate* lacks: {needle}"
        )
    assert "Two positions are not rewritten" not in prose, (
        "the template still counts the positions it leaves as written"
    )
    assert "#596" not in prose, "the template still names #596 as open"
