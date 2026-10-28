"""`skills/verify/scripts/coordinates.py`, one class per function.

The units `pact_check.py` loads to grade a pact anchor: a clause is named by
its heading path, and its hash covers what the clause holds (#867).

  the heading path  a section runs down to the next heading at its level
                    or above, a path narrows inside it, and a heading is
                    read on the lines a renderer shows
  the hash          trailing whitespace and blank lines are no change, and
                    indentation is one
"""

import os

from conftest import ROOT, census_case, load_module

TARGET = "skills/verify/scripts/coordinates.py"

KERNEL = os.path.join(ROOT, "skills", "verify", "scripts", "coordinates.py")


ec = load_module(KERNEL, "agentic_kernel_for_its_cases")


def section(text, path):
    """The regions the heading path PATH names in the markdown TEXT, asked
    as `pact_check.py#clause_hash` asks for a clause's."""
    parts = [p for p in path.split(ec.HEADING_SEP) if p.strip()]
    return ec.heading_path(ec.markdown_lines(text), parts)


class Test_heading_path:
    def test_accepts_a_deeper_heading_as_part_of_its_section(self):
        """Down to the next heading at its level OR ABOVE: a DEEPER one is part
        of the section, not the end of it."""
        text = (
            "# Top\n\nintro\n\n## A\n\nbody of A\n\n"
            "### A1\n\nnested body\n\n## B\n\nbody of B\n"
        )
        assert section(text, "## A") == [(5, 12)]
        assert section(text, "### A1") == [(9, 12)]
        assert section(text, "# Top") == [(1, 15)]

    def test_a_markdown_locator_is_a_heading_path(self):
        """A section runs to the line before the next heading at its level or
        above, and a path narrows inside it."""
        text = "# Top\n\n## A\n\nbody\n\n### Deep\n\nmore\n\n## B\n\nlast\n"
        assert section(text, "## A") == [(3, 10)]
        assert section(text, "## A / ### Deep") == [(7, 10)]

    def test_a_repeated_heading_is_disambiguated_by_its_parent(self):
        text = "## A\n\n### Same\n\none\n\n## B\n\n### Same\n\ntwo\n"
        assert len(section(text, "### Same")) == 2
        assert section(text, "## B / ### Same") == [(9, 11)]

    def test_refuses_an_indented_heading_as_the_start_of_a_section(self):
        """An INDENTED `## B` normalises to the same text as the heading but is
        not one."""
        text = "## A\n\n    ## B\n\n## B\n\nreal\n"
        assert ec.heading_level("    ## B") is None
        assert section(text, "## B") == [(5, 7)]

    def test_a_heading_quoted_in_a_closed_fence_opens_no_section(self):
        """Read on the lines a renderer shows, a fenced `## B` is no heading: one
        place, and `## A` runs past the fence (#867)."""
        text = "## A\n\nintro\n\n```markdown\n## B\n```\n\nmore\n\n## B\n\nreal\n"
        assert section(text, "## B") == [(11, 13)]
        assert section(text, "## A") == [(1, 10)]

    def test_a_heading_indented_three_spaces_is_a_heading_and_an_issue_number_is_not(
        self,
    ):
        """CommonMark 4.2 lets a heading stand three spaces in, and wants a space
        after the run, so `#84's line` at column 0 is prose and ends no section."""
        text = "## A\n\n#84's line\n\nbody\n\n   ## B\n\nlast\n"
        assert ec.heading_level("   ## B") == 2
        assert ec.heading_level("#84's line") is None
        assert section(text, "## A") == [(1, 6)]
        assert section(text, "## B") == [(7, 9)]


class Test_content_hash:
    def test_accepts_trailing_whitespace_and_blank_lines_as_no_change(self):
        a = ["def f():", "    return 1"]
        b = ["def f():   ", "", "    return 1\t"]
        assert ec.content_hash(a) == ec.content_hash(b)

    def test_refuses_to_ignore_indentation(self):
        """A dedent moves a statement out of the block it belonged to."""
        inside = ["def f():", "    if x:", "        go()"]
        outside = ["def f():", "    if x:", "    go()"]
        assert ec.content_hash(inside) != ec.content_hash(outside)


test_census = census_case(TARGET)
