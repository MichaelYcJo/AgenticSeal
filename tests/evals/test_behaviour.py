"""`evals/scripts/behaviour.py`, the case writer the generators share.

`Test_report_regex` reads what the writer writes back through
`tests/workflows.py#front_matter`, the suite's one reader of a grader's
fields, so a writer that quotes a value the parser reads otherwise fails
here. The generators' output is held by the cases of the scripts that call
the writer: `tests/evals/test_rule_cases.py` and
`tests/evals/test_noninferiority.py`.
"""

import os

import pytest
from conftest import ROOT, census_case, load_module
from workflows import front_matter

TARGET = "evals/scripts/behaviour.py"

BEHAVIOUR = load_module(os.path.join(ROOT, *TARGET.split("/")), "behaviour_under_test")


class Test_report_regex:
    def test_accepts_a_path_and_a_pattern_holding_a_quote_field_for_field(self):
        """A quote doubled inside a single-quoted scalar, and a comma and
        braces inside a flow map's value, read back as written."""
        pattern = r"^location: .*it's(?:a|b)"
        _, text = BEHAVIOUR.report_regex(
            "truth", "q", "it's, {a}.md", pattern, "A defect.", "m", weight=2
        )
        assert front_matter(text) == {
            "type": "regex",
            "target": {"source": "file", "path": "it's, {a}.md"},
            "pattern": pattern,
            "flags": "m",
            "weight": "2",
        }

    def test_refuses_a_kind_outside_the_three(self):
        """A grader's kind is the prefix `noninferiority.py` reads, so a kind
        it does not know is refused where the grader is written."""
        with pytest.raises(ValueError, match="is not one of"):
            BEHAVIOUR.report_regex("loose", "q", "a.md", "x", "A defect.")


test_census = census_case(TARGET)
