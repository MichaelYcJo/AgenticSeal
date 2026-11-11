"""The broad gate hands `cmd.exe` a command name it can run (#448).

`broad_gate.run(..., shell=True)` hands the `Broad gate` key to `%COMSPEC%`,
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

from conftest import ROOT


def test_the_template_shows_the_rewrite_and_the_form_that_keeps_a_switch():
    """A2, the reader's half. `templates/setup/config.md` *Broad gate* is
    where a person writing the key learns what `cmd.exe` is handed. What
    the scan rewrites and leaves as written is
    `tests/skills/test_broad_gate.py`'s to pin, and the section's account
    of it is the proofer's to read."""
    path = os.path.join(ROOT, "templates", "setup", "config.md")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    section = text.split("## Broad gate", 1)[1].split("\n## ", 1)[0]
    prose = " ".join(section.split())
    for fact in (
        # The name `cmd.exe` is handed for `bin/test`, which a person reads
        # on the gate's line saying what `cmd.exe` was handed.
        "`bin\\test`",
        # The form a person writes to keep a switch where a glued one reads
        # as a path.
        "`xcopy /e`",
    ):
        assert fact in prose, f"`templates/setup/config.md` *Broad gate* lacks: {fact}"
