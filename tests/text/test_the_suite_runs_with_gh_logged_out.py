"""The suite runs with `gh` logged out, on every machine (#510): what the
contributor reads of it.

A case that fell through its stubs onto a live `gh` passed wherever `gh` was
logged in, which is every developer's machine and the broad gate, and failed
on CI, whose pytest job has no token. `tests/conftest.py` takes `gh`'s login
away at import, so the local answer is CI's answer. The two cases of that
block, the structural one that reads what the conftest does to an
environment and the behavioural one that asks `gh` which token it would
send, are `tests/test_conftest.py`'s `Test_module`. The case here reads
`CONTRIBUTING.md`.
"""

import os

from conftest import ROOT, census_case
from test_conftest import TOKENS

TARGET = "CONTRIBUTING.md"


def test_contributing_says_the_suite_runs_logged_out():
    """A6, the reader's half (contract rule 14). A contributor whose case
    goes red on a machine where `gh` works everywhere else needs to find why
    in the section that tells them how to run the suite."""
    path = os.path.join(ROOT, *TARGET.split("/"))
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    section = text.split("## Running the checks", 1)[1].split("\n## ", 1)[0]
    prose = " ".join(section.split())
    for needle in (
        # The variable the conftest points at an empty directory, which a
        # contributor reads when `gh` behaves differently under the suite.
        "`GH_CONFIG_DIR`",
        # The token variables `tests/test_conftest.py#TOKENS` names, which a
        # contributor reads beside `gh`'s behaviour under the suite.
        *(f"`{name}`" for name in TOKENS),
        # The prefix of the variables the conftest removes, and the call a
        # case writes to set one.
        "`GITHUB_`",
        "`monkeypatch.setenv`",
    ):
        assert needle in prose, (
            f"`CONTRIBUTING.md` *Running the checks* lacks: {needle}"
        )


test_census = census_case(TARGET)
