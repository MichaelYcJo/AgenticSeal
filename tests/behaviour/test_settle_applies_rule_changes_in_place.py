"""The settle skill's example of `## Rule changes` reads as the skill says.

The cases of the reader and the replay stand in
`tests/skills/test_rule_changes.py`, and the cases that run `settle` over a
git history in `tests/skills/test_settle.py`. No `check:` line names this file.
"""

import os

from conftest import ROOT, census_case, spec
from test_rule_changes import parse, rules

TARGET = "skills/settle/rule-changes.md"


def test_the_skills_example_reads_as_the_skill_says():
    """The grammar has one statement, the skill's; its example is read by the
    parser, so the two cannot drift apart."""
    with open(os.path.join(ROOT, *TARGET.split("/")), encoding="utf-8") as f:
        section = f.read().split("\n## Rule changes\n", 1)[1]
    example = section.split("```\n", 2)[1]
    parsed = parse(spec(example.rstrip("\n")))
    assert parsed.errors == [], parsed.errors
    [only] = parsed.ops
    assert (only.kind, only.file, only.section) == (
        "change",
        "docs/forms/the-round-record.md",
        "The round record",
    )
    for kind, (need, may) in rules.GRAMMAR.items():
        row = next(
            line for line in section.splitlines() if line.startswith(f"| `{kind}`")
        )
        fields = row.split("|")[2]
        # Each field name of `rules.GRAMMAR`, which a framer writing an
        # operation copies and the parser matches.
        assert all(f"`{name}`" in fields for name in need + may), row


test_census = census_case(TARGET)
