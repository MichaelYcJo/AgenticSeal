"""`lib/items.py`, one class per function.

The item grammar of `skills/settle/rule-changes.md` *Rule changes*, read
by `lib/gaps.py` for a closing memo's `## Not verified` and by
`skills/settle/scripts/rule_changes.py` for a design's `## Rule changes`.
The cases run in the process on lines, with no git. They came, unchanged
but for the module they call, from `tests/skills/test_unverified_check.py`
when the grammar left that script (#1482).
"""

import pytest
from conftest import census_case, load_lib_module

TARGET = "lib/items.py"

ITEMS = load_lib_module("items.py", "items_for_its_own_file")

# The sentence a section that holds nothing is told to write, pinned as the
# person reads it.
BLOCK = "the block `- nothing` with `  why: <reason>`"


class Test_items:
    def test_accepts_items_their_fields_and_a_continued_value(self):
        body = [
            (1, "- add"),
            (2, "  file: a.md"),
            (3, "  to: one"),
            (4, "    two"),
            (5, ""),
        ]
        found, error = ITEMS.items(body)
        assert error is None
        assert found == [
            {
                "kind": "add",
                "line": 1,
                "fields": {"file": [2, ["a.md"]], "to": [3, ["one", "two", ""]]},
            }
        ]

    @pytest.mark.parametrize(
        "body, error",
        [
            ([(1, "text")], (1, "a line outside an item")),
            ([(1, "- add"), (2, "  to: a"), (3, "  to: b")], (3, "`to` given twice")),
            (
                [(1, "- nothing"), (2, "   why: x")],
                (2, "a line that is not a field of the item above"),
            ),
        ],
        ids=["outside an item", "a field twice", "three spaces in"],
    )
    def test_refuses_a_line_that_is_no_part_of_an_item(self, body, error):
        assert ITEMS.items(body)[1] == error


class Test_field_values:
    def test_accepts_each_field_joined_and_trimmed(self):
        item = {
            "kind": "nothing",
            "line": 1,
            "fields": {"why": [2, ["every claim", "was run", ""]]},
        }
        assert ITEMS.field_values(item, ("why",), ()) == (
            {"why": "every claim\nwas run"},
            None,
        )

    @pytest.mark.parametrize(
        "fields, error",
        [
            (
                {"why": [2, ["x"]], "who": [3, ["y"]]},
                (3, "`who` is not a field of `nothing`"),
            ),
            ({}, (1, "`nothing` needs `why`")),
            ({"why": [2, [""]]}, (2, "`why` is empty")),
        ],
        ids=["another field", "no why", "an empty why"],
    )
    def test_refuses_a_field_outside_the_kind_a_missing_one_and_an_empty_one(
        self, fields, error
    ):
        item = {"kind": "nothing", "line": 1, "fields": fields}
        assert ITEMS.field_values(item, ("why",), ()) == (None, error)


class Test_opens_the_block:
    def test_accepts_the_item_nothing(self):
        assert ITEMS.opens_the_block("- nothing") is True

    @pytest.mark.parametrize("line", ["- Nothing", "* nothing", "- nothings"])
    def test_refuses_another_spelling(self, line):
        assert ITEMS.opens_the_block(line) is False


class Test_nothing_block:
    @pytest.mark.parametrize(
        "body, answer",
        [
            ([(3, "- nothing"), (4, "  why: all run.")], []),
            ([(3, "- nothing")], []),
            ([(3, "| Item | Who must answer |")], None),
            ([(3, "none - x")], None),
        ],
        ids=["the block", "the block with no why", "a table", "the old line"],
    )
    def test_accepts_the_block_and_passes_anything_else_on(self, body, answer):
        """#1167, *Scope* item 9: a line that opens like the block and is not
        it is passed on as any other line is, and its reader names it
        (`unread_block`). Seen red against its refusal here. The block
        answers with its errors alone: no reader uses its reason (#1319)."""
        assert ITEMS.nothing_block(body) == answer

    def test_refuses_a_second_item(self):
        body = [(3, "- nothing"), (4, "  why: x"), (5, "- nothing"), (6, "  why: y")]
        assert ITEMS.nothing_block(body) == [
            (5, "`- nothing` is the section's one item")
        ]


class Test_unread_block:
    @pytest.mark.parametrize(
        "first", ["none - x", "None.", "- nothing - x", "-nothing", "* none"]
    )
    def test_refuses_a_first_line_that_opens_like_the_block_as_the_block(self, first):
        """The line is not taken as the block: it is named as read as prose.
        Refusing the section that holds it is its reader's act."""
        assert ITEMS.unread_block([(3, first), (4, "more")]) == (
            3,
            f"`{first}` opens like {BLOCK} and is not it, so it was read as prose",
        )

    @pytest.mark.parametrize(
        "body",
        [
            [(3, "- nothing"), (4, "  why: x")],
            [(3, "| Item | Who must answer |")],
            [(3, "nonesuch")],
            [(3, "| a | b |"), (4, "none - x")],
        ],
        ids=["the block", "a table", "another word", "not the first line"],
    )
    def test_accepts_the_block_and_any_first_line_that_does_not_open_like_it(
        self, body
    ):
        assert ITEMS.unread_block(body) is None


test_census = census_case(TARGET)
