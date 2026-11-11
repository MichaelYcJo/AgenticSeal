"""`evals/scripts/behaviour.py`, one class per function it has cases for.

`scalar` and `grader_from`, the reader of a grader file the case writer
writes, moved here from `evals/scripts/noninferiority.py` with their cases
in #1487, when no command of that script read them any more.
"""

import os

import pytest
from conftest import ROOT, census_case, load_module

TARGET = "evals/scripts/behaviour.py"

BEHAVIOUR = load_module(os.path.join(ROOT, *TARGET.split("/")), "behaviour_under_test")


class Test_scalar:
    @pytest.mark.parametrize(
        "text, want",
        [
            (
                "{source: file, path: 'it''s, {a}.md'}",
                {"source": "file", "path": "it's, {a}.md"},
            ),
            ("'it''s'", "it's"),
            ("2", 2),
            ("-3", -3),
        ],
        ids=["a flow map", "a quoted string", "an integer", "a negative integer"],
    )
    def test_accepts_a_map_a_quoted_string_and_an_integer(self, text, want):
        assert BEHAVIOUR.scalar(text) == want

    @pytest.mark.parametrize("text", ["regex", "1.5"])
    def test_refuses_anything_else_and_keeps_its_text(self, text):
        assert BEHAVIOUR.scalar(f" {text} ") == text


class Test_grader_from:
    def test_accepts_what_behaviour_writes_field_for_field(self):
        pattern = r"^location: .*it's(?:a|b)"
        name, text = BEHAVIOUR.report_regex(
            "truth", "q", "it's, {a}.md", pattern, "A defect.", "m", weight=2
        )
        assert BEHAVIOUR.grader_from(f"graders/{name}", text) == {
            "name": "truth-q",
            "type": "regex",
            "weight": 2,
            "config": {
                "target": {"source": "file", "path": "it's, {a}.md"},
                "pattern": pattern,
                "flags": "m",
                "match": "contains",
            },
        }

    def test_accepts_a_file_naming_no_weight_and_no_match(self):
        got = BEHAVIOUR.grader_from(
            "graders/truth-1.md", "---\ntype: regex\npattern: 'x'\n---\nA defect.\n"
        )
        assert (got["weight"], got["config"]["match"]) == (1, "contains")

    def test_refuses_a_file_with_no_front_matter(self):
        with pytest.raises(
            ValueError, match=r"^graders/truth-1\.md has no front matter$"
        ):
            BEHAVIOUR.grader_from("graders/truth-1.md", "A defect.\n")


test_census = census_case(TARGET)
