"""What is left of the rule-change file: the case that reads the settle
skill's example of `## Rule changes`, which waits for #923.

#942's phase 6 placed the reader's and the replay's cases in
`tests/test_rule_changes.py`, and the cases that run `settle` over a git
history in `tests/test_settle.py`. No `check:` line names this file.
"""

import os

from conftest import spec
from test_rule_changes import parse, rules

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def test_the_skills_example_reads_as_the_skill_says():
    """The grammar has one statement, the skill's; its example is read by the
    parser, so the two cannot drift apart."""
    with open(
        os.path.join(ROOT, "skills", "settle", "SKILL.md"), encoding="utf-8"
    ) as f:
        section = f.read().split("\n## Rule changes\n", 1)[1]
    example = section.split("```\n", 2)[1]
    parsed = parse(spec(example.rstrip("\n")))
    assert parsed.errors == [], parsed.errors
    [only] = parsed.ops
    assert (only.kind, only.file, only.section) == (
        "change",
        "docs/the-review-record.md",
        "The round record",
    )
    for kind, (need, may) in rules.GRAMMAR.items():
        row = next(
            line for line in section.splitlines() if line.startswith(f"| `{kind}`")
        )
        fields = row.split("|")[2]
        assert all(f"`{name}`" in fields for name in need + may), row
