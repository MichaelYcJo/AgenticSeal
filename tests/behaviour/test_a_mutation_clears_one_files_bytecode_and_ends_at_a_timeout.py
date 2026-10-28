"""`seal mutate`: what the crafter's definition and the verify skill say of it.

#641, with #129 as its twin. `agents/crafter.md` told the implementer to "clear
`tests/__pycache__` between mutations", which aims at the wrong cache. It
clears the importers, whose bytecode is valid and unchanged, and it misses
the one cache that can be stale -- the one beside the MUTATED file, wherever
that file lives
(`.github/scripts/__pycache__` in #129, `skills/verify/scripts/__pycache__`
in #326). Nothing bounded a mutated run either, and one hung for 32 minutes
(#577).

The cases that run the command moved to `tests/skills/test_mutation_check.py` in
#942's phase 6. What stays here reads the sentences a session acts on: the
crafter's definition, the verify skill's section, and the bound both of them
state.

**How the script is loaded here.** By path, with an `importlib` spec,
registered in `sys.modules` before it executes -- the way
`tests/skills/test_arm_check.py` loads `arm_check.py`. The script reaches
`arm_check.py` the same way rather than through `sys.path`, so nothing has to
be put on the path first: a bare `from arm_check import ...` resolves only
when the script is run by its path and `PYTHONSAFEPATH` is unset.
"""

import importlib.util
import os
import re
import sys

from conftest import ROOT, flat

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


# --- S9 · the definition names the command and no directory to clear -------


def test_the_crafters_definition_names_the_command_and_no_directory_to_clear():
    """Contract rule 14: the sentence the crafter acts on changed, so the new text is pinned
    and so is the absence of the old one. *Clear `tests/__pycache__`* cleared
    the importers, whose bytecode is never stale, and missed the mutated
    file's, which is; any second directory named in its place would miss the
    third the same way (#129).

    The two sentences `tests/text/test_the_handoff_before_round_one.py` pins are
    asserted here too, because the rewording happens around them and that
    case is the one that would notice their loss -- this one says the loss
    did not come from this edit."""
    crafter = flat("agents", "crafter.md")
    # Any runner: the definition ships to repositories with no `bin/test`,
    # and `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py` holds it
    # to naming none.
    assert re.search(r"seal mutate \S+ --replace .+? --tests \"", crafter), (
        "`agents/crafter.md` does not show the mutation loop as one command, "
        "with its replacement and the cases it runs"
    )
    assert "-p no:xdist" in crafter, (
        "the example dropped `-p no:xdist`, which `questions.md` Q1's "
        "measurement put there for a handful of cases"
    )
    assert "tests/__pycache__" not in crafter, (
        "`agents/crafter.md` still names a directory to clear between mutations"
    )
    assert "Mutation-test every unit you added, one command each." in crafter
    assert "watch one go red" in crafter


def test_the_boundaries_bullet_says_the_command_holds_the_copy():
    crafter = flat("agents", "crafter.md")
    rule = crafter[crafter.index("**Commit before you mutate") :]
    rule = rule[: rule.index(" check: ")]
    assert "`seal mutate` holds the bytes it read" in rule, rule


def test_the_verify_skill_says_what_each_verdict_means_and_what_the_bound_ends():
    """The section a reader opens to learn the command: its verdicts with
    their exit codes, its bound, and what that bound ends on each platform."""
    skill = flat("skills", "verify", "SKILL.md")
    start = skill.index("#### `seal mutate`")
    section = skill[start : skill.index("### 3. Bound to the tree")]
    for said in (
        "seal mutate <file> --replace",
        "`red`, exit 0",
        "`SURVIVED`, exit 1",
        "exit 2",
        "300 seconds",
        "process group",
        "Windows",
        "PYTHONDONTWRITEBYTECODE",
        "seal arms",
        # Round 1, 🔴 1: the baseline, and the verdict it gives.
        "first runs `--tests` against the file as it is",
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
    assert f"bounded at {bound} s unless `--timeout`" in flat("agents", "crafter.md")
    assert f"{bound} seconds by default" in flat("skills", "verify", "SKILL.md")
