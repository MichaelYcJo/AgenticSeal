"""`hooks/blocks.py`, one class per function its cases reach.

The walk's own answers came from `tests/test_the_hooks_hide_what_a_renderer_hides.py`
and the splitter's from `tests/test_every_reader_ends_a_line_where_gfm_does.py`
(#942's phase 6). Those files keep what holds the walk to a CommonMark oracle
and every copy of the splitter to this one, because a check that judges
markdown against an oracle, or files against each other, stays where it is.
`tests/test_unverified_rows_close.py` keeps the case that holds this module's
fence walks to `unverified_check.py`'s and `hooks/config.py`'s, for the same
reason.
"""

import pytest
from block_shapes import BREAKS, CLOSE, INLINE_KINDS, OPEN
from conftest import SPLITLINES_ONLY, census_case, load_hook_module, texts

TARGET = "hooks/blocks.py"

blocks = load_hook_module("blocks.py", "specseal_blocks_under_test")
# The name the splitter's cases read it by, where they read it through
# `unverified_check.py`, which hands this module's `gfm_lines` to its callers.
reader = blocks

# An opener and a closer of every other kind of inline raw HTML, with a
# closer that can stand at a line's start or directly after the opener (#673).
# The closing tag's closer is `>` and is only ever written on the same line.
INLINE_OPEN_CLOSE = [
    *INLINE_KINDS,
    ("<span", 'a="b">'),
    ("</span", ">"),
]


class Test_gfm_lines:
    def test_refuses_to_end_a_line_at_any_of_the_eight(self):
        for char in SPLITLINES_ONLY:
            assert reader.gfm_lines(f"a{char}b\nc") == [f"a{char}b", "c"], repr(char)
        assert reader.gfm_lines("a\r\nb\rc\nd") == ["a", "b", "c", "d"]
        assert reader.gfm_lines("a\r\nb\n", keepends=True) == ["a\r\n", "b\n"]

    def test_accepts_a_text_without_the_eight_as_splitlines_splits_it(self):
        for text in [t for t in texts() if not any(c in t for c in SPLITLINES_ONLY)]:
            assert reader.gfm_lines(text) == text.splitlines(), repr(text)
            assert reader.gfm_lines(text, True) == text.splitlines(True), repr(text)


class Test_walk_text:
    def test_refuses_to_claim_a_piece_inside_its_lines_open_comment(self):
        """#667 round 2, yellow 1. A piece after a break inside an inline
        comment its line left open is uncertain; a piece of a fenced line
        stays fenced and claimed; a piece that starts before the line's opener
        is claimed live. Each of the three conditions is one line of this
        case."""
        ls = BREAKS["LS"]
        inside = blocks.walk_text(f"a {OPEN} x{ls}| r |\n{CLOSE}\n")
        assert inside.uncertain[:2] == [False, True], inside.uncertain
        fenced = blocks.walk_text(f"```\nx {OPEN} a{ls}y\n```\n")
        assert (fenced.kinds[2], fenced.uncertain[2]) == (blocks.FENCED, False)
        before = blocks.walk_text(f"a{ls}b {OPEN} c\n\nd\n")
        assert before.uncertain[:2] == [False, False], before.uncertain

    def test_refuses_to_claim_a_piece_inside_other_inline_html_its_line_left_open(
        self,
    ):
        """#673's S4. A piece after a break inside CDATA, a processing
        instruction, a declaration or a tag its line left open is uncertain; a
        piece after one its line closed is claimed; a piece of a fenced line
        stays fenced and claimed. And an opener a renderer does not honour
        does not step over one it does."""
        ls = BREAKS["LS"]
        for opener, closer in INLINE_OPEN_CLOSE:
            inside = blocks.walk_text(f"a {opener}{ls}{closer} x\n\nd\n")
            assert inside.uncertain[:2] == [False, True], (opener, inside.uncertain)
            closed = blocks.walk_text(f"a {opener} {closer}{ls}| r |\n\nd\n")
            assert closed.uncertain[:2] == [False, False], (opener, closed.uncertain)
            fenced = blocks.walk_text(f"```\nx {opener}{ls}y\n```\n")
            assert (fenced.kinds[2], fenced.uncertain[2]) == (blocks.FENCED, False)
        nested = blocks.walk_text(f"a `<?` <![CDATA[ b ?> c{ls}| r |\n]]>\n")
        assert nested.uncertain[:2] == [False, True], nested.uncertain
        # a `>` inside a quoted value does not end the tag
        quoted = blocks.walk_text(f'a <span title="b>c{ls}d">\n\ne\n')
        assert quoted.uncertain[:2] == [False, True], quoted.uncertain
        # `<?>` does not close a processing instruction: the `?` is the opener's
        instruction = blocks.walk_text(f"a <?>{ls}| r |\n?>\n\nd\n")
        assert instruction.uncertain[:2] == [False, True], instruction.uncertain
        # a closer before its opener closes nothing
        early = blocks.walk_text(f"a ?> <? b{ls}| r |\n?>\n\nd\n")
        assert early.uncertain[:2] == [False, True], early.uncertain
        # a `>` inside a single-quoted value does not end the tag either
        single = blocks.walk_text(f"a <span title='b>c{ls}d'>\n\ne\n")
        assert single.uncertain[:2] == [False, True], single.uncertain

    def test_accepts_an_unclosed_fence_at_the_reader_line_it_starts(self):
        """#667 round 1, yellow 1. `walk_text` answers per reader line, and a
        fence opener whose info string holds a U+2028 is one GFM line and two
        reader lines. The opener that never closes is the first of them, the
        one a person can be sent to; the piece after the break opens
        nothing."""
        text = "```" + BREAKS["LS"] + "x\n| a |\n"
        walked = blocks.walk_text(text)
        assert walked.unclosed == [0], walked.unclosed
        assert len(walked.kinds) == len(text.splitlines()) == 3


class Test_module:
    @pytest.mark.parametrize("opener", [o for o, _ in INLINE_OPEN_CLOSE[:-1]])
    def test_a_paragraph_left_inside_other_inline_html_is_unsure_to_its_end(
        self, opener
    ):
        """#673's S5, `walk`'s paragraph state. The lines after a line that
        leaves CDATA, a processing instruction, a declaration or a tag open are
        uncertain to the paragraph's end, because the walk does not follow that
        construct's end across lines; a blank line ends it. A `-->` does not end
        it either, where the comment it closes is one the parser never formed."""
        found = blocks.walk([f"a {opener}", "b", "c", "", "d"])
        assert found.uncertain == [False, True, True, False, False], found.uncertain
        past = blocks.walk([f"a {opener}", "b " + CLOSE + " c", "d", "", "e"])
        assert past.uncertain == [False, True, True, False, False], past.uncertain
        fake = blocks.walk(
            ["a `" + OPEN + "` b", "c <? d " + CLOSE + " e", "f", "", "g"]
        )
        assert fake.uncertain == [False, True, True, False, False], fake.uncertain


test_census = census_case(TARGET)
