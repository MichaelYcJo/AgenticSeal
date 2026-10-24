"""`skills/settle/scripts/rule_changes.py`, one class per function.

The grammar of a spec's `## Rule changes` is `skills/settle/SKILL.md` *Rule
changes*, and this module is its one reader (#953). `Test_parse` asks the
reader directly; `Test_replay` replays specs over one document in memory.
Merge order is a fact only git holds, so the cases that read it run
`settle` over a repository and are in `tests/test_settle.py`.

#942's phase 6 placed these cases from
`tests/test_settle_applies_rule_changes_in_place.py`, which keeps the case
that reads the skill's example.
"""

import os

import pytest
from conftest import DOC, census_case, line_of, load_module, op, spec

TARGET = "skills/settle/scripts/rule_changes.py"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
rules = load_module(
    os.path.join(ROOT, "skills", "settle", "scripts", "rule_changes.py"),
    "specseal_rule_changes",
)


def parse(text):
    """The section of TEXT, read against a policy root of `docs/`."""
    return rules.parse(text, "docs")


# What the reader says of a no-change line in any other spelling: the block
# it expects, by name (S10).
NO_CHANGE = (
    "a section that holds nothing writes the block `- nothing` with `  why: <reason>`"
)


ALL_SHAPES = """\
- change
  file: docs/a.md
  section: S
  from: old sentence.
  to: New rule.
- add
  file: docs/a.md
  section: S
  to: **Rule.** Its grounds
    run on.
    check: none reader: review
- remove
  file: docs/a.md
  section: T
- remove
  file: docs/a.md
  section: S
  from: x.
- add
  file: docs/new.md
  to: # New"""


def replay(doc, *specs, held=None):
    """`(documents, applied, refused)` for SPECS, `(id, changes)` in merge
    order, over one document `docs/a.md` holding DOC."""
    texts = {"docs/a.md": doc}
    ordered = [(i, parse(spec(c)).ops) for i, c in specs]
    return rules.replay(texts.get, ordered, held or {})


class Test_parse:
    def test_accepts_each_shape_as_one_operation_with_its_line(self):
        text = spec(ALL_SHAPES)
        parsed = parse(text)
        assert parsed.errors == [], parsed.errors
        got = [(o.kind, o.file, o.section, o.old, o.new) for o in parsed.ops]
        assert got == [
            ("change", "docs/a.md", "S", "old sentence.", "New rule."),
            (
                "add",
                "docs/a.md",
                "S",
                None,
                "**Rule.** Its grounds\nrun on.\ncheck: none reader: review",
            ),
            ("remove", "docs/a.md", "T", None, None),
            ("remove", "docs/a.md", "S", "x.", None),
            ("add", "docs/new.md", None, None, "# New"),
        ]
        assert [o.line for o in parsed.ops] == [
            i + 1 for i, line in enumerate(text.split("\n")) if line.startswith("- ")
        ]

    @pytest.mark.parametrize(
        "body, why",
        [
            (
                "- nothing\n  why: this item changes no rule.",
                "this item changes no rule.",
            ),
            (
                "- nothing\n  why: this item changes\n    no rule.",
                "this item changes\nno rule.",
            ),
        ],
        ids=["one line", "continued"],
    )
    def test_the_no_change_block_is_a_section_with_no_operation(self, body, why):
        """S10. `- nothing` with its one field, `why`, is a section that changes
        no rule: no operation and no error, and the reason read as any field's
        value is."""
        parsed = parse(spec(body))
        assert (parsed.ops, parsed.errors) == ([], [])
        assert parsed.nothing == why

    def test_a_spec_with_no_section_is_told_apart_from_an_empty_one(self):
        """A spec written before the section existed has nothing to replay; an
        empty section is a frame nobody filled in, and it is refused."""
        assert parse("# old\n\n## Scope\n\nIn.\n").ops is None
        assert parse(spec("")).errors

    @pytest.mark.parametrize(
        "heading",
        [
            "## Rule Changes",
            "### Rule changes",
            "# Rule changes",
            "## Rule changes:",
            "## Rule-changes",
            "## RULE CHANGES.",
        ],
    )
    @pytest.mark.parametrize(
        "beside", [False, True], ids=["alone", "beside-the-heading"]
    )
    def test_a_near_miss_of_the_heading_is_refused_at_its_line(self, heading, beside):
        """A heading whose letters, case folded, are those of `Rule changes` and
        that is not `## Rule changes` is a section its author wrote, not a spec
        written before the section existed. It is refused at its line, naming
        the one heading, whether or not the right heading stands too."""
        body = "- nothing\n  why: a reason.\n\n"
        text = (
            "# a work item\n\n"
            + (f"## Rule changes\n\n{body}" if beside else "")
            + f"{heading}\n\n{body}## Open questions\n\nNone.\n"
        )
        parsed = parse(text)
        assert parsed.errors, parsed
        line, why = parsed.errors[0]
        assert line == line_of(text, heading), (line, why)
        assert f"`{heading}`" in why and "`## Rule changes`" in why, why
        assert parsed.ops == [] and parsed.nothing is None

    def test_a_heading_with_other_letters_is_no_near_miss(self):
        """The class is the letters of `Rule changes`; a heading with other
        letters is another section, and a spec holding only it has none."""
        for heading in ("## Rules changes", "## Rule changes made", "## Changes"):
            assert parse(f"# x\n\n{heading}\n\nText.\n") == rules.Parsed(None, None, [])

    def test_a_section_quoted_in_a_fence_or_a_comment_is_not_read(self):
        fenced = "# x\n\n```\n## Rule changes\n\n- remove\n  file: docs/a.md\n```\n"
        assert parse(fenced).ops is None
        commented = spec(
            "<!-- the grammar is the skill's\n- remove\n  file: docs/a.md -->\n"
            "- nothing\n  why: a reason."
        )
        parsed = parse(commented)
        assert parsed.errors == [] and parsed.nothing == "a reason."

    def test_a_line_that_begins_inside_a_code_span_is_refused_at_its_line(self):
        """Round 1 of #988, finding 2. A value's code span opened at the end of
        one line and closed on the next leaves the second line beginning inside
        the span, which the shared reader reads as not live. The reader dropped
        such a line as it drops a comment, so the section parsed clean and
        settle wrote the value without it. It is refused at its line, and the
        spec applies nothing; a comment's lines are still skipped."""
        wrapped = "    the review chain` carries one line."
        text = spec(
            "<!-- guidance, never an operation\n  - remove -->\n"
            "- add\n  file: docs/a.md\n  section: S\n"
            "  to: **Rule.** A branch declaring `through\n"
            f"{wrapped}"
        )
        parsed = parse(text)
        assert parsed.ops == [], parsed
        [(line, why)] = parsed.errors
        assert line == line_of(text, wrapped), (line, why)
        assert "begins inside a code span" in why, why
        # The same value with the span closed on the line that opens it.
        closed = text.replace("`through\n", "`through the review chain`\n").replace(
            "    the review chain` carries", "    carries"
        )
        parsed = parse(closed)
        assert parsed.errors == [], parsed.errors
        assert parsed.ops[0].new.endswith(
            "`through the review chain`\ncarries one line."
        )
        # Round 3 of #988: the line inside the span opens with `<!--`, which the
        # span makes text, so it is refused too and not skipped as a comment.
        opener = "    <!-- the review chain` carries"
        commented = text.replace(f"\n{wrapped}", f"\n{opener}\n    one line. -->")
        [(line, why)] = parse(commented).errors
        assert line == line_of(commented, opener), (line, why)
        assert "begins inside a code span" in why, why

    def test_a_comment_opener_inside_a_fence_above_the_section_hides_no_operation(self):
        """Round 2 of #988, finding 1. A comment opener inside a fenced block is
        code, not a comment, as `live_lines` reads it. The reader that refused a
        wrapped span read it as a comment that ran to the next closer, so a
        section after such a fence parsed as empty (shape A), or kept only the
        operations after a later comment closed it, with no error (shape B)."""
        fence = "# a work item\n\n```html\n<!-- an example of a comment\n```\n\n"
        adds = [f"- add\n  file: docs/{name}.md\n  to: A rule." for name in "abc"]
        shape_b = (
            f"{fence}## Rule changes\n\n{adds[0]}\n{adds[1]}\n"
            f"<!-- the third one -->\n{adds[2]}\n\n## Open questions\n\nNone.\n"
        )
        parsed = parse(shape_b)
        assert parsed.errors == [], parsed.errors
        assert [o.file for o in parsed.ops] == ["docs/a.md", "docs/b.md", "docs/c.md"]
        shape_a = (
            f"{fence}## Rule changes\n\n{adds[0]}\n\n## Open questions\n\n"
            "None. <!-- a note -->\n"
        )
        parsed = parse(shape_a)
        assert parsed.errors == [], parsed.errors
        assert [o.file for o in parsed.ops] == ["docs/a.md"]
        # Below such a fence a wrapped span is still refused at its line, and
        # not skipped as part of a comment that is not there.
        wrapped = "    the review chain` carries one line."
        shape_c = shape_a.replace(
            "  to: A rule.", f"  to: A branch declaring `through\n{wrapped}"
        )
        [(line, why)] = parse(shape_c).errors
        assert line == line_of(shape_c, wrapped) and "code span" in why, (line, why)
        # A fenced block inside the section is read as lines, so it is refused
        # as no field of the item above, never skipped.
        shape_d = shape_a.replace(
            "  to: A rule.\n",
            "  to: A rule.\n\n```\n- remove\n  file: docs/b.md\n```\n",
        )
        lines = shape_d.split("\n")
        opener = lines.index("```", lines.index("## Rule changes")) + 1
        assert parse(shape_d).errors == [
            (opener, "a line that is not a field of the item above")
        ]

    @pytest.mark.parametrize(
        "body, bad, reason",
        [
            ("- rename\n  file: docs/a.md\n  to: x", "- rename", "`rename`"),
            (
                "- add\n  file: docs/a.md\n  heading: S\n  to: x",
                "  heading: S",
                "`heading`",
            ),
            (
                "- change\n  file: docs/a.md\n  section: S\n  to: y",
                "- change",
                "`from`",
            ),
            (
                "- add\n  file: docs/a.md\n  file: docs/b.md\n  to: x",
                "  file: docs/b.md",
                "twice",
            ),
            (
                "A sentence.\n- remove\n  file: docs/a.md\n  section: S",
                "A sentence.",
                "item",
            ),
            ("- remove\n  file: src/a.md\n  section: S", "- remove", "docs/"),
            ("- remove\n  file: docs/sub/a.md\n  section: S", "- remove", "docs/"),
            ("- add\n  file: docs/..\\..\\evil.md\n  to: x", "- add", "docs/"),
            ("- add\n  file: docs/C:\\x\\evil.md\n  to: x", "- add", "docs/"),
            ("- add\n  file: docs/\\evil.md\n  to: x", "- add", "docs/"),
            ("- add\n  file: docs/sub\\b.md\n  to: x", "- add", "docs/"),
            ("- add\n  file: docs/a.md\n  section: S\n  to:", "  to:", "empty"),
            ("nothing — a reason.", "nothing — a reason.", NO_CHANGE),
            ("nothing - a reason.", "nothing - a reason.", NO_CHANGE),
            ("Nothing — a reason.", "Nothing — a reason.", NO_CHANGE),
            ("- nothing", "- nothing", "`nothing` needs `why`"),
            ("- nothing\n  why:", "  why:", "`why` is empty"),
            (
                "- nothing\n  why: a reason.\n  file: docs/a.md",
                "  file: docs/a.md",
                "`file` is not a field of `nothing`",
            ),
            (
                "- nothing\n  why: a reason.\n- remove\n  file: docs/a.md\n  section: S",
                "- remove",
                "`- nothing` is the section's one item",
            ),
            (
                "- remove\n  file: docs/a.md\n  section: S\n- nothing\n  why: a reason.",
                "- nothing",
                "`- nothing` is the section's one item",
            ),
        ],
        ids=[
            "unknown-op",
            "unknown-field",
            "missing-field",
            "field-twice",
            "outside-an-item",
            "outside-the-root",
            "below-the-top-level",
            "windows-parent",
            "windows-drive",
            "windows-root",
            "windows-subdirectory",
            "empty-value",
            "the em-dash form",
            "the em-dash form with a hyphen",
            "the em-dash form capitalised",
            "the block without why",
            "the block with an empty why",
            "the block with another field",
            "the block beside an operation",
            "the block after an operation",
        ],
    )
    def test_refuses_a_block_that_does_not_match_whole_at_its_line(
        self, body, bad, reason
    ):
        """Never skipped and never half-read: one error at the line, and the spec
        applies nothing."""
        text = spec(body)
        parsed = parse(text)
        assert parsed.errors, parsed
        line, why = parsed.errors[0]
        assert line == line_of(text, bad), (line, why)
        assert reason in why, why

    def test_a_second_block_is_refused_at_its_own_line(self):
        """The block stands alone, so a second `- nothing` is refused at its own
        line rather than passed unread behind the first; its unknown field would
        otherwise reach nobody."""
        text = spec("- nothing\n  why: a reason.\n- nothing\n  bogus: x")
        parsed = parse(text)
        lines = text.split("\n")
        second = lines.index("- nothing", lines.index("- nothing") + 1) + 1
        assert parsed.errors, parsed
        assert parsed.errors[0][0] == second, parsed.errors
        assert "`- nothing` is the section's one item" in parsed.errors[0][1]
        assert parsed.nothing is None and parsed.ops == []


class Test_replay:
    def test_accepts_a_change_and_rewrites_the_text_where_it_stands(self):
        """S1: the rest of the document is byte-identical."""
        docs, applied, refused = replay(
            DOC, ("a", op("change", "S", "old sentence.", "New rule."))
        )
        assert (applied, refused) == (["a"], [])
        assert docs["docs/a.md"] == DOC.replace("old sentence.", "New rule.")

    def test_a_rewrapped_sentence_still_matches_and_non_ascii_is_plain_text(self):
        doc = "# P\n\n## S\n\nA rule that\nwraps — here 🙂 now.\n"
        docs, applied, _ = replay(
            doc,
            ("a", op("change", "S", "rule that wraps — here 🙂 now.", "rule.")),
        )
        assert applied == ["a"]
        assert docs["docs/a.md"] == "# P\n\n## S\n\nA rule.\n"

    def test_an_add_ends_its_section_before_the_next_heading(self):
        """S2. A section with a sub-heading takes the rule at the end of its own
        text, so it is not read as the sub-section's."""
        docs, applied, _ = replay(DOC, ("a", op("add", "T", new="Rule.")))
        assert applied == ["a"]
        assert "T's text.\n\nRule.\n\n## U\n" in docs["docs/a.md"]
        docs, _, _ = replay(DOC, ("a", op("add", "S", new="Rule.")))
        assert "After.\n\nRule.\n\n### S child\n" in docs["docs/a.md"]
        docs, _, _ = replay(DOC, ("a", op("add", "U", new="Rule.")))
        assert docs["docs/a.md"].endswith("Last.\n\nRule.\n")

    def test_a_remove_takes_the_text_or_the_whole_section(self):
        """S3: the section goes up to the next heading of its level or higher."""
        docs, applied, _ = replay(
            DOC, ("a", op("remove", "T", "x.")), ("b", op("remove", "S"))
        )
        assert applied == ["a", "b"]
        assert docs["docs/a.md"] == "# A policy\n\n## T\n\nT's text.\n\n## U\n\nLast.\n"

    @pytest.mark.parametrize(
        "change, reason",
        [
            (op("change", "S", "not there.", "y."), "not in"),
            (op("change", "S", "x.", "y."), "not in"),
            (op("change", "Nowhere", "x.", "y."), "no heading"),
            (op("remove", "S", "e"), "not in"),
            (op("change", "T", "tex", "y"), "not in"),
            (op("remove", "S", file="docs/absent.md"), "does not exist"),
            (op("add", new="# again"), "exists"),
        ],
        ids=[
            "text-absent",
            "text-in-another-section",
            "heading-absent",
            "a-word-inside-another",
            "a-word-inside-another-at-the-end",
            "file-absent",
            "add-over-a-document",
        ],
    )
    def test_refuses_a_spec_whose_place_it_cannot_find(self, change, reason):
        """S4: nothing applies, and the refusal names the spec, the line and the
        reason."""
        docs, applied, refused = replay(DOC, ("a", change))
        assert applied == [] and docs == {}
        [(work_item, line, why)] = refused
        assert work_item == "a" and line == line_of(spec(change), change.split("\n")[0])
        assert reason in why, why

    def test_a_heading_or_a_text_found_twice_is_refused(self):
        doc = DOC + "\n## S\n\nold sentence.\n"
        _, _, refused = replay(doc, ("a", op("change", "S", "old sentence.", "y.")))
        assert "2 times" in refused[0][2], refused
        doc = DOC.replace("After.", "After. old sentence.")
        _, _, refused = replay(doc, ("a", op("change", "S", "old sentence.", "y.")))
        assert "2 times" in refused[0][2], refused

    def test_a_heading_inside_a_fence_is_not_a_place(self):
        doc = "# P\n\n```\n## S\n```\n\n## T\n\nx.\n"
        _, _, refused = replay(doc, ("a", op("add", "S", new="Rule.")))
        assert "no heading" in refused[0][2], refused

    def test_a_spec_applies_all_of_its_operations_or_none(self):
        """S7."""
        both = op("change", "S", "old sentence.", "y.") + "\n" + op("remove", "Nowhere")
        docs, applied, refused = replay(DOC, ("a", both))
        assert applied == [] and docs == {}
        assert refused[0][1] == line_of(spec(both), "- remove")

    def test_the_later_spec_applies_over_the_earlier_one(self):
        """S5, in memory."""
        docs, applied, _ = replay(
            DOC,
            ("a", op("change", "S", "old sentence.", "y.")),
            ("b", op("change", "S", "y.", "z.")),
        )
        assert applied == ["a", "b"]
        assert "Before. z. After." in docs["docs/a.md"]

    def test_a_spec_after_a_refused_one_at_its_place_waits(self):
        """Applying it now would let the earlier spec apply over it at the next
        settle, so the newer one would not win."""
        _, applied, refused = replay(
            DOC,
            ("a", op("change", "S", "not there.", "y.")),
            ("b", op("add", "S", new="Rule.")),
            ("c", op("add", "T", new="Rule.")),
        )
        assert applied == ["c"]
        assert [r[0] for r in refused] == ["a", "b"]
        assert "waits on a," in refused[1][2], refused

    def test_a_spec_at_a_section_holding_or_held_by_a_refused_ones_waits(self):
        """A section's range holds its sub-sections, so `S` and `S child` can
        name one text; a section beside them cannot."""
        _, applied, refused = replay(
            DOC,
            ("a", op("change", "S", "not there.", "y.")),
            ("b", op("change", "S child", "Child text.", "z.")),
            ("c", op("add", "T", new="Rule.")),
        )
        assert applied == ["c"], refused
        assert "waits on a, refused earlier at docs/a.md section `S`" in refused[1][2]

    def test_a_held_spec_applies_nothing_and_holds_its_places(self):
        _, applied, refused = replay(
            DOC,
            ("a", op("add", "S", new="One.")),
            ("b", op("add", "S", new="Two.")),
            held={"a": [(0, "its record holds an open row")]},
        )
        assert applied == []
        assert refused[0] == ("a", 0, "its record holds an open row")


test_census = census_case(TARGET)
