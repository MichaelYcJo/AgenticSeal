"""`seal mutate`: what the crafter's definition and the verify skill say of it.

#641, with #129 as its twin. `agents/crafter.md` told the implementer to "clear
`tests/__pycache__` between mutations", which aims at the wrong cache. It
clears the importers, whose bytecode is valid and unchanged, and it misses
the one cache that can be stale -- the one beside the MUTATED file, wherever
that file lives
(`.github/scripts/__pycache__` in #129, `skills/verify/scripts/__pycache__`
in #326). Nothing bounded a mutated run either, and one hung for 32 minutes
(#577).

The cases that run the command stand in `tests/skills/test_mutation_check.py`.
What stays here reads the sentences a session acts on: the
crafter's definition, `skills/verify/seal-mutate.md`, and the bound both of
them state.

**How the script is loaded here.** By path, with an `importlib` spec,
registered in `sys.modules` before it executes, so nothing has to be put on
the path first.
"""

import importlib.util
import os
import re
import sys

from conftest import ROOT, flat

# No TARGET: its cases hold seal mutate's command and bound across agents/crafter.md, skills/verify/seal-mutate.md and the script's constant.

SCRIPT = os.path.join(ROOT, "skills", "verify", "scripts", "mutation_check.py")


def module():
    """The command, loaded from its path and registered first.

    Missing, this raises -- which is how every case below was seen red before
    the script existed (contract rule 15)."""
    spec = importlib.util.spec_from_file_location("agentic_mutation_check", SCRIPT)
    loaded = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = loaded
    spec.loader.exec_module(loaded)
    return loaded


# --- S9 · the definition names the command ----------------------------------


def test_the_crafters_definition_names_the_command_and_its_flag():
    """Contract rule 14: the sentence the crafter acts on changed, so the
    command it now copies is pinned. *Clear `tests/__pycache__`* cleared the
    importers, whose bytecode is never stale, and missed the mutated file's,
    which is (#129); the command restores and clears for itself. The rule's
    sentences around the command are the proofer's to read."""
    crafter = flat("agents", "crafter.md")
    # The `seal mutate` command line with its `--replace` and `--tests`
    # arguments, which the crafter copies for each unit it mutates.
    # Any runner: the definition ships to repositories with no `bin/test`,
    # so the pattern names none.
    assert re.search(r"seal mutate \S+ --replace .+? --tests \"", crafter), (
        "`agents/crafter.md` does not show the mutation loop as one command, "
        "with its replacement and the cases it runs"
    )
    # The flag `-p no:xdist`, which the crafter adds to the runner where
    # pytest-xdist starts workers by default.
    assert "-p no:xdist" in crafter, (
        "the example dropped `-p no:xdist`, which `questions.md` Q1's "
        "measurement put there for a handful of cases"
    )


def test_the_verify_skill_says_what_each_verdict_means():
    """The section a reader opens to learn the command: the command line and
    its verdicts with their exit codes. The section is
    `skills/verify/seal-mutate.md`'s since #1312, and runs to the end of that
    file; its bound is the next case's."""
    skill = flat("skills", "verify", "seal-mutate.md")
    section = skill[skill.index("## `seal mutate`") :]
    for said in (
        # The command line a reader copies for each break.
        "seal mutate <file> --replace",
        # The verdicts `skills/verify/scripts/mutation_check.py#RED` and
        # `skills/verify/scripts/mutation_check.py#SURVIVED` print, with the
        # exit codes a caller's `&&` chain acts on.
        "`red`, exit 0",
        "`SURVIVED`, exit 1",
        # The exit code a caller reads as a run that measured nothing.
        "exit 2",
        # The variable the cases inherit, which a case that plants a `.pyc`
        # has to switch off.
        "PYTHONDONTWRITEBYTECODE",
        # The verdict `skills/verify/scripts/mutation_check.py#NO_BASELINE`
        # prints.
        "`no baseline`",
    ):
        assert said in section, f"the section does not say {said!r}"


def test_the_default_bound_is_the_one_both_documents_state(tmp_path, monkeypatch):
    """`questions.md` Q4: a value somebody waits on. The constant, the bound a
    call with no `--timeout` actually gets, and the figure the crafter and the
    skill are told are one number, so moving one is seen in all three."""
    mc = module()
    seen = {}

    def records(path, old, new, command, *, cwd, timeout):
        seen["timeout"] = timeout
        return mc.RED, "recorded", ""

    monkeypatch.setattr(mc, "mutation_run", records)
    target = tmp_path / "target.py"
    target.write_text("VALUE = 1\n", encoding="utf-8")
    assert mc.main([str(target), "--replace", "1", "2", "--tests", "x"]) == 0
    assert seen["timeout"] == mc.DEFAULT_TIMEOUT == 300.0
    bound = f"{mc.DEFAULT_TIMEOUT:g}"
    # The bound in seconds, which the crafter waits on for a run with no
    # `--timeout`.
    assert f" {bound} s " in flat("agents", "crafter.md")
    # The same bound, which a reader of the command's section waits on.
    assert f" {bound} seconds " in flat("skills", "verify", "seal-mutate.md")
