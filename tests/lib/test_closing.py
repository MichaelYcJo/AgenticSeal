"""`lib/closing.py`, one class per function.

What a pull request body and a squash subject say about issues and pull
requests, read by `skills/code-review/scripts/pr_body.py`,
`skills/code-review/scripts/chain_check.py#carried_by` and the release
automation under `.github/scripts/`. The class came from the closer's test
file, `tests/github/test_close_issues_on_release.py`, when the readers left
that script for `lib/` (#1571), unchanged but for the module its loader
reads. The readers' own cases stand in their files.
"""

import os

import pytest
from conftest import ROOT, census_case

TARGET = "lib/closing.py"


def _closer():
    """The closing readers, imported so their regexes can be read: a string
    search over the source cannot see what a regex matches. The name is the
    one the cases called when the readers stood in the release closer."""
    import importlib.util

    path = os.path.join(ROOT, "lib", "closing.py")
    spec = importlib.util.spec_from_file_location("iadd_closing_for_tests", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Test_keywords_in:
    def test_accepts_only_a_keyword_before_a_number(self):
        """The regexes, read rather than searched for.

        The fenced `Closes #88` in `docs/releasing/branch-and-release.md` is the example a
        person copies, so a pull request body quoting the document must not close
        the issue the document names — and bodies here quote documents routinely.
        """
        m = _closer()
        assert m.keywords_in("Closes #88") == ["88"]
        assert m.keywords_in("Closes #88, closes #92") == ["88", "92"]
        assert m.keywords_in("Part of #90") == []
        assert m.keywords_in("see #90 and #92") == [], (
            "a bare number with no keyword closes an issue"
        )
        assert m.keywords_in("```\nCloses #88\n```") == [], (
            "a fenced example closes the issue it names"
        )
        assert m.keywords_in("see `Closes #54` in the doc") == [], (
            "an inline code span closes the issue it names"
        )
        assert m.keywords_in("```\nCloses #1\n```\nCloses #88") == ["88"], (
            "prose after a fence stopped being read"
        )
        assert m.MERGED_PR.search("feat: a thing (#100)").group(1) == "100"
        assert m.MERGED_PR.search("fix: the (#61) thing was wrong") is None, (
            "a number mid-subject is read as a merged pull request"
        )

    # #266: review round 1 of work item 1788844400 enumerated five well-formed
    # shapes `FENCE` and `SPAN` did not mask, by construction rather than by
    # reading. A closing keyword inside any of them was read as a claim, so a
    # RELEASE closed the issue. Four are masked now, the HTML comment since
    # #1181 measured GitHub's reading of it, and the four-space indented block
    # is deliberately not; each shape has a case, so a later widening or
    # narrowing is a red rather than a drift. The direction is stated at the
    # patterns: masking more closes fewer, and an unclosed issue is visible and
    # re-runnable where a wrong close is a false record on the tracker.

    def test_refuses_a_keyword_inside_a_tilde_fence(self):
        """`~~~` is a fence to CommonMark and to GitHub, and it was invisible here
        because the pattern spelled backticks."""
        m = _closer()
        assert m.keywords_in("~~~\nCloses #1\n~~~\nCloses #4") == ["4"], (
            "a keyword inside a tilde fence closes the issue it names"
        )
        # A fence closes on ITS delimiter. Read as any delimiter, this one ends
        # at the backticks and the keyword after them is prose.
        assert m.keywords_in("~~~\n```\nCloses #1\n~~~\nCloses #4") == ["4"], (
            "a tilde fence was closed by a backtick line inside it"
        )

    def test_a_fence_indented_under_a_list_item_masks_a_keyword(self):
        """A fence inside a list item is indented to the item's content, and the
        pattern anchored the delimiter at column 0."""
        m = _closer()
        body = "- the example:\n  ```\n  Closes #2\n  ```\nCloses #4"
        assert m.keywords_in(body) == ["4"], (
            "a keyword inside a fence indented under a list item closes the issue"
        )

    def test_a_double_backtick_span_masks_a_keyword(self):
        """A span opened with two backticks closes with two, and may hold a
        single backtick inside. The one-backtick pattern read `` ``#150`` `` as
        two EMPTY spans with the number in prose between them."""
        m = _closer()
        assert m.keywords_in("Closes ``#3``\nCloses #4") == ["4"], (
            "a double-backtick span around the number leaves the keyword read"
        )
        assert m.keywords_in("see ``Closes #3`` there\nCloses #4") == ["4"], (
            "a double-backtick span around the whole claim leaves it read"
        )
        # The inner backtick is UNPAIRED on purpose: with a pair, the one-backtick
        # arm masks the claim anyway and the double form's reach is unmeasured.
        assert m.keywords_in("see ``Closes #3 ` x`` and Closes #4") == ["4"], (
            "a double-backtick span holding a single backtick is cut at the inner backtick"
        )

    def test_a_keyword_inside_an_html_comment_claims_nothing(self):
        """#1181. Pull requests into `main` measured GitHub's reading of a
        comment: a comment that closes hides its keyword wherever it stands
        (#1402, #1403), and a `<!--` that never closes hides everything below
        it where it begins a line (#1403, #1405). The fence, the comment and
        the span are masked in one pass, and whichever opens first wins."""
        m = _closer()
        assert m.keywords_in("<!-- Closes #6 -->") == [], (
            "a keyword inside a comment, the shape #1402 measured, closes the issue"
        )
        for body in (
            "a note <!-- Closes #1 --> mid-line\nCloses #4",
            "<!--\nCloses #1\nmore\n-->\nCloses #4",
            "- an item\n  <!-- Closes #1 -->\nCloses #4",
            "<!---->\nCloses #4",
        ):
            assert m.keywords_in(body) == ["4"], body
        # The first to open wins. A `<!--` inside a span opens no comment, and
        # a backtick inside a comment opens no span.
        assert m.keywords_in("the `<!--` marker\nCloses #4\nthe `-->` end") == ["4"], (
            "a comment opened inside a code span hid the claim after the span"
        )
        assert m.keywords_in("<!-- it's ` here --> Closes #4 and `x`") == ["4"], (
            "a backtick inside a comment opened a span that hid the claim"
        )
        # A `<!--` that never closes, at a line start (#1403, #1405), and
        # behind a list marker, where GitHub hides what follows past the
        # list's end (#1408).
        assert m.keywords_in("Closes #1401\nCloses #4\n<!-- Closes #32") == [
            "1401",
            "4",
        ], "a keyword after an opener that begins its line and never closes"
        assert m.keywords_in("Closes #1401\n<!--\nCloses #103") == ["1401"], (
            "a keyword below an opener that begins its line and never closes"
        )
        assert m.keywords_in("- <!-- note\nCloses #4") == [], (
            "a keyword below an opener behind a list marker that never closes"
        )

    @pytest.mark.parametrize(
        ("body", "claimed"),
        [
            # Four spaces open an indented code block to CommonMark, and they
            # are ALSO how this repository's pull request bodies continue a
            # bullet's text onto the next line, so masking the shape would
            # drop real claims, which is the wrong direction for a closer.
            ("- a bullet whose text\n    Closes #5", ["5"]),
            # A `<!--` that never closes, after other text on its line, is
            # text to GitHub: #1404 held this body with no `-->` anywhere, and
            # `closingIssuesReferences` named #1247 as well as the control.
            ("Closes #1401\nsee the <!-- marker\nCloses #1247", ["1401", "1247"]),
        ],
    )
    def test_accepts_a_shape_left_unmasked_as_a_claim(self, body, claimed):
        """Deliberately unmasked, each for the reason above its row. Stated at
        the pattern; this case turns a future widening into a decision."""
        m = _closer()
        assert m.keywords_in(body) == claimed


test_census = census_case(TARGET)
