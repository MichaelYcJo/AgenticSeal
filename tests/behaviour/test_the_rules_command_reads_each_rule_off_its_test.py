"""The settle skill states the grammar the rules command reads.

The cases of `.github/scripts/rules.py`'s functions stand in
`tests/github/test_rules.py`, and its `Test_module` holds the case that
renders the record layout document. The case that reads the `rule` marker's
registration stands in `tests/test_conftest.py`'s `Test_module`.
"""

import os

from conftest import ROOT, census_case

TARGET = "skills/settle/rule-changes.md"

SETTLE = os.path.join(ROOT, *TARGET.split("/"))


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


test_census = census_case(TARGET)
