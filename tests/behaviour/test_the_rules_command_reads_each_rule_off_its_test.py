"""What is left of the rules command's old file: the cases that read the
`rule` marker's registration and the settle skill.

The cases of `.github/scripts/rules.py`'s functions stand in
`tests/github/test_rules.py`, and its `Test_module` holds the case that
renders the record layout document.
"""

import os

from conftest import ROOT

SETTLE = os.path.join(ROOT, "skills", "settle", "rule-changes.md")


def test_the_rule_marker_is_registered(pytestconfig):
    """`tests/conftest.py` registers `rule`, so a gate test carries it with no
    unknown-mark warning."""
    assert any(line.startswith("rule(") for line in pytestconfig.getini("markers")), (
        pytestconfig.getini("markers")
    )


def test_settle_owns_the_grammar():
    """The grammar is stated once, in the settle skill, the document a spec's
    author reads; this module and `rules.py` only read it."""
    with open(SETTLE, encoding="utf-8") as handle:
        text = handle.read()
    section = text.split("\n## A rule has one shape\n")[1].split("\n## ")[0]
    section = " ".join(section.split())
    for phrase in (
        # The label `.github/scripts/rules.py#LABEL` matches at a check line,
        # which a framer writes into a rule.
        "`check: `",
        # The marker a test carries for a rule its check line names by
        # marker, which `rules.py` reads off the collected tests.
        '`@pytest.mark.rule("<marker>")`',
        # The command a person runs to read every check line.
        "`seal rules --check`",
    ):
        assert phrase in section, f"settle no longer says: {phrase!r}"
