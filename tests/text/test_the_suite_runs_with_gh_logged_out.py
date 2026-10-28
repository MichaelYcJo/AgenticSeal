"""The suite runs with `gh` logged out, on every machine (#510): what the
contributor reads of it.

A case that fell through its stubs onto a live `gh` passed wherever `gh` was
logged in, which is every developer's machine and the broad gate, and failed
on CI, whose pytest job has no token. `tests/conftest.py` takes `gh`'s login
away at import, so the local answer is CI's answer. The two cases of that
block, the structural one that reads what the conftest does to an
environment and the behavioural one that asks `gh` which token it would
send, are `tests/test_conftest.py`'s `Test_module` since #942's phase 7. The
case left here reads `CONTRIBUTING.md`'s prose, which is #923's.
"""

import os

from conftest import ROOT
from test_conftest import TOKENS


def test_contributing_says_the_suite_runs_logged_out():
    """A6, the reader's half (contract rule 14). A contributor whose case
    goes red on a machine where `gh` works everywhere else needs to find why
    in the section that tells them how to run the suite."""
    path = os.path.join(ROOT, "CONTRIBUTING.md")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    section = text.split("## Running the checks", 1)[1].split("\n## ", 1)[0]
    prose = " ".join(section.split())
    for needle in (
        "The suite runs with `gh` logged out, on a contributor's machine as on CI.",
        "it points `GH_CONFIG_DIR` at an empty directory",
        "sets `GH_TOKEN` and `GH_ENTERPRISE_TOKEN` to a value no server accepts",
        "without a token variable, `gh` reads the login it keeps in the OS keyring",
        *(f"`{name}`" for name in TOKENS),
        "A case that needs `gh` stubs it.",
    ):
        assert needle in prose, (
            f"`CONTRIBUTING.md` *Running the checks* lacks: {needle}"
        )
    assert "removes `GH_TOKEN`" not in prose, (
        "CONTRIBUTING.md still says the suite removes `GH_TOKEN`, which would "
        "leave `gh` reading the login in the OS keyring"
    )
