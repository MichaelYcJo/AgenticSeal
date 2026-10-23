"""`.github/scripts/issue_claims_check.py`, one class per function.

`Closes #153 and #150` claims one issue, and nothing said so. PR #162 wrote
that sentence; the 0.8.0 release closed #153 and left #150 open. A closing
keyword claims the one number that follows it, and this check warns where a
sentence claims one number and names another beside it.

Two things the cases watch for, because both are ways the check quietly
stops being worth having. **A false positive**: a warning on a body that is
correct teaches people to scroll past the check, so most of `Test_read`'s
cases are bodies that must produce nothing. **A missed hard wrap**: every
body here is wrapped at 88 columns, so one sentence spans lines routinely,
and a segmenter that treats a line as a sentence misses the case it was
written for. The real #162 body is not a fixture: it carries a session URL
on a domain outside this repository's fixture allowlist.

#942's phase 6 placed these cases from
`tests/test_a_body_naming_two_issues_claims_one.py`, which keeps the cases
that read the issues document, the hygiene workflow and its template. Its
round 9 fix pass placed in `Test_module` the body cut after a U+2028,
`segments`' one case, from
`tests/test_every_reader_ends_a_line_where_gfm_does.py`, a case of this module
alone.
"""

import importlib.util
import os
import sys

import pytest
from conftest import LS, census_case

TARGET = ".github/scripts/issue_claims_check.py"

ROOT = os.path.join(os.path.dirname(__file__), "..")


def _load(name):
    path = os.path.join(ROOT, ".github", "scripts", name + ".py")
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


check = _load("issue_claims_check")


def read(body):
    return check.read(body)


def warned(body):
    """The `(claimed, unclaimed)` pairs the body earns a warning for."""
    return [(kept, lost) for kept, lost, _ in read(body)[2]]


class _args:
    def __init__(self, body_file):
        self.body_file = body_file


class Test_read:
    def test_refuses_the_sentence_that_lost_an_issue_with_a_warning(self):
        """PR #162's shape, with neutral numbers. One claim, one loss, one line
        telling the author which is which."""
        claimed, mentioned, warnings = read("Closes #11 and #22 — both are done.")
        assert claimed == ["11"]
        assert mentioned == ["22"]
        assert [(k, lost) for k, lost, _ in warnings] == [("11", "22")]

    @pytest.mark.parametrize(
        "body, warning",
        [
            # The form the sibling script's own comment names.
            ("Closes #11, #22", ("11", "22")),
            # The row that rules out "a line is a sentence": every body here is
            # wrapped at 88 columns, and #162's `Closes` sentence ran across
            # three lines.
            ("Closes #11 and\n#22 are both done.", ("11", "22")),
            # One warning per unclaimed NUMBER, not per occurrence: the same
            # annotation printed twice reads as two things to fix.
            ("Closes #11 and #22, and #22 again.", ("11", "22")),
            # A link ending `#22` reads as an issue number here, as the mention
            # list already says; excluding a `#N` after a URL character would be
            # a second syntax to be wrong about.
            ("Closes #11, and https://example.com/x#22 has the rest.", ("11", "22")),
            # With two keywords ahead of it, the number the author was reusing
            # is the one beside it; naming the first sends them to the wrong
            # keyword.
            ("Closes #11 and closes #22 and #33", ("22", "33")),
            # `0.9.2` would split the sentence if a full stop alone ended one.
            ("Closes #11 in 0.9.2 and #22 with it.", ("11", "22")),
        ],
        ids=[
            "comma",
            "hard-wrapped",
            "one-number-twice",
            "url-fragment",
            "nearest-claim",
            "version-number",
        ],
    )
    def test_refuses_a_number_beside_a_claim_with_one_warning(self, body, warning):
        """Each spelling of the defect earns one warning, naming the claim the
        author was reusing and the number it lost."""
        assert warned(body) == [warning]

    def test_the_warning_quotes_the_sentence_as_the_author_wrote_it(self):
        """Not the masked copy. A code span blanked out of the quote reads as a
        different sentence, and the author has to recognise their own."""
        body = "Closes #11 and #22 — see `close_issues_on_release.py` for why."
        ((_, _, sentence),) = read(body)[2]
        assert "`close_issues_on_release.py`" in sentence

    def test_the_same_number_in_two_sentences_earns_a_warning_each(self):
        """The set is per segment. Two sentences that each lose the number are two
        places the author has to write the keyword."""
        assert warned("Closes #11 and #22. Closes #33 and #22.") == [
            ("11", "22"),
            ("33", "22"),
        ]

    def test_a_fenced_quote_of_the_failure_shape_is_not_an_instance_of_it(self):
        """A body quoting `Closes #1, #2` as an EXAMPLE of the defect must not be
        reported as one. This repository's own documents do exactly that, and its
        bodies quote its documents routinely."""
        body = "The defect looks like this:\n\n```\nCloses #11, #22\n```\n\nDo not write that."
        assert read(body) == ([], [], [])

    @pytest.mark.parametrize(
        "body",
        ["see `Closes #11, #22` in the ticket", "A tidy-up with no ticket behind it."],
        ids=["an-inline-span", "no-numbers"],
    )
    def test_accepts_a_body_that_claims_and_mentions_nothing(self, body):
        """An inline span claims nothing and mentions nothing, and a body with no
        numbers says so."""
        assert read(body) == ([], [], [])

    def test_the_shapes_the_closer_masks_since_266_are_masked_here_too(self):
        """The patterns are imported, so a widening of the closer's masks is a
        widening here — which is the reason for importing them (#266). Three
        shapes, each holding a body that would otherwise warn or claim."""
        for body in (
            "~~~\nCloses #11, #22\n~~~\n\nDo not write that.",
            "- the example:\n  ```\n  Closes #11, #22\n  ```\n\nDo not write that.",
            "see ``Closes #11, #22`` in the ticket",
        ):
            assert read(body) == ([], [], []), body

    def test_a_fence_does_not_splice_the_line_above_it_onto_the_line_below(self):
        """The masking is length-preserving for this reason. Collapsing a fenced
        block to one space would join `Closes #11` to `#22` across it, and invent
        the very warning the fence exists to prevent."""
        body = "Closes #11\n\n```\nsome code\n```\n\n#22 is a different matter."
        assert warned(body) == []

    def test_accepts_a_second_keyword_and_loses_nothing(self):
        claimed, mentioned, warnings = read("Closes #11 and closes #22")
        assert claimed == ["11", "22"]
        assert mentioned == []
        assert warnings == []

    @pytest.mark.parametrize(
        "body",
        [
            # A number the body claims elsewhere is claimed, so nothing is lost,
            # wherever else it also appears.
            "Closes #11 and #22 is the other one. This closes #22.",
            "Closes #11. See #22 for the background.",
            "Closes #11\n\n#22 is unrelated.",
            # Consecutive list items carry no blank line between them, so the
            # block rule is the only thing separating them.
            "- Closes #11\n- #22 is next\n",
            "| Closes #11 |\n| #22 |\n",
            "Closes #11. #22 is separate.",
        ],
        ids=[
            "claimed-elsewhere",
            "a-new-sentence",
            "a-blank-line",
            "a-list-item",
            "a-table-row",
            "a-full-stop-after-a-number",
        ],
    )
    def test_accepts_a_number_a_segment_boundary_keeps_apart(self, body):
        """A number after a claim is lost only within one segment: a new
        sentence, a blank line, a list item, a table row or a full stop after a
        number ends it, and a number claimed elsewhere loses nothing."""
        assert warned(body) == []

    @pytest.mark.parametrize("rule", ["---", "***", "___", "==="])
    def test_a_horizontal_rule_ends_the_segment(self, rule):
        """A thematic break and a setext underline are blocks of their own, and
        the space every other marker requires takes all four out of the class. A
        claim above one and an unrelated number below it are not one sentence, and
        warning about them is the false positive this check spends everything to
        avoid."""
        assert warned(f"Closes #11\n{rule}\n#22 is unrelated.") == []

    def test_a_number_before_the_keyword_is_not_the_shape(self):
        """`Part of #11, and this closes #22` is not somebody losing a claim. Only
        a number AFTER the claim is a candidate, and that is where the whole
        false-positive budget goes."""
        claimed, mentioned, warnings = read("Part of #11, and this closes #22.")
        assert claimed == ["22"]
        assert mentioned == ["11"]
        assert warnings == []

    def test_an_anchor_is_not_an_issue_number(self):
        """`#L45` and `#heading` need a digit immediately after the hash."""
        assert read("Closes #11, see file.py#L45 and the #overview section") == (
            ["11"],
            [],
            [],
        )


class Test_report:
    def test_refuses_a_lost_claim_in_a_job_annotation(self):
        """`::warning::` at the start of the line is what makes GitHub render this
        on the job rather than bury it in the log. Dropping the prefix while
        tidying the f-string leaves every other case green."""
        lines = []
        check.report(*read("Closes #11 and #22"), out=lines.append)
        annotations = [line for line in lines if line.startswith("::warning::")]
        assert len(annotations) == 1, lines
        assert "#11" in annotations[0] and "#22" in annotations[0]

    def test_the_two_lists_say_what_closes_and_what_does_not(self):
        """The author acts on these two lines. A rename that leaves `read()` alone
        changes what they are told and no case notices."""
        lines = []
        check.report(*read("Closes #11 and #22"), out=lines.append)
        assert lines[0] == "claimed (closed when the release reaches `main`): #11"
        assert lines[1] == "mentioned only (nothing closes these): #22"

    def test_accepts_a_clean_body_and_says_so(self):
        """Silence reads as a check that did not run."""
        lines = []
        check.report(*read("Closes #11"), out=lines.append)
        assert lines[-1] == "no sentence claims one number and names another beside it"


class Test_main:
    def test_accepts_every_body_at_exit_0(self, tmp_path, capsys):
        """It reports; it never fails a pull request. A check that goes red on
        prose stops a release for a false positive."""
        for body in ("Closes #11 and #22", "", "no numbers here"):
            f = tmp_path / "body.md"
            f.write_text(body, encoding="utf-8")
            assert check.main(["--body-file", str(f)], env={}) == 0
        capsys.readouterr()

    def test_refuses_a_step_that_examined_nothing(self, capsys):
        """No `--body-file` and no `PR_BODY` at all is a misconfigured workflow.
        The alternative is a step that is green having read nothing, which is the
        failure `templates/hygiene.yml`'s own header argues against."""
        assert check.main([], env={}) == 2
        assert "examined nothing" in capsys.readouterr().err


class Test_module:
    @pytest.mark.parametrize(
        "prose",
        [
            # A run of markers that OPENS the line and then carries prose. These
            # are what the whole-line anchor is for, and nothing else here needs
            # it: every other shape below is rejected at the first character, so a
            # case built only from those leaves the anchor unpinned. Measured --
            # dropping `$` from one alternative left all forty-two green.
            "--- not a rule",
            "*** not a rule",
            "___ not a rule",
            "=== not an underline",
            "= x",
            # And the shapes the space requirement rejects, which the four
            # alternatives must not take back.
            "a --- b",
            "--",
            "-x",
            "#22",
            "*bold* x",
        ],
    )
    def test_a_run_of_markers_inside_a_line_is_still_prose(self, prose):
        """The four break alternatives match a WHOLE line only. Widened to match
        anywhere, they would take `#22` at the start of a line back out of the
        segment it belongs to -- which is the defect this module exists to see,
        hard-wrapped."""
        assert check.BLOCK_START.match(prose) is None

    def test_an_empty_body_is_a_body(self):
        """A pull request opened with no description is ordinary, and reporting
        nothing for it is the answer -- not an exit code."""
        assert check.body_from(_args(None), {"PR_BODY": ""}) == ""

    def test_the_environment_is_read_when_no_file_is_given(self):
        assert check.body_from(_args(None), {"PR_BODY": "Closes #11"}) == "Closes #11"

    def test_the_check_imports_the_closers_definition_rather_than_restating_it(self):
        """Two lists of what a closing keyword is would drift apart the first time
        either was widened, and widening one of them is precisely the repair this
        issue rejected. Identity, not equality: a copied literal passes an
        equality check on the day it is copied.

        The sibling is taken from `sys.modules`, where the check's own import put
        it — NOT loaded again by path. A second load builds a second module
        object, and then `KEYWORDS is KEYWORDS` is false for a module that
        imported it correctly. `CLOSING` would still pass, because `re.compile`
        caches by pattern and flags and hands both loads the same object: the two
        regex identities are true whether the import happened or not, and only the
        tuple actually asks the question. Measured here, in this file's first
        run."""
        closer = sys.modules["close_issues_on_release"]
        assert os.path.samefile(
            closer.__file__,
            os.path.join(ROOT, ".github", "scripts", "close_issues_on_release.py"),
        ), "the check imported some other module of that name"
        assert check.CLOSING is closer.CLOSING
        assert check.KEYWORDS is closer.KEYWORDS
        assert check.FENCE is closer.FENCE
        assert check.SPAN is closer.SPAN

    def test_the_source_defines_no_keyword_list_of_its_own(self):
        """The identity case above passes for a module that ALSO carries its own
        copy and never uses it. This reads the file."""
        with open(
            os.path.join(ROOT, ".github", "scripts", "issue_claims_check.py"),
            encoding="utf-8",
        ) as f:
            source = f.read()
        body = source.split('"""', 2)[2]
        for spelling in ("KEYWORDS = (", "CLOSING = re.compile", "FENCE = re.compile"):
            assert spelling not in body, (
                f"{spelling!r} is defined here as well as next door — one of the "
                "two will be widened alone"
            )

    def test_an_issue_body_is_cut_where_github_renders_a_block(self):
        """S13 of #664. A list-item shape after a U+2028 mid-line is not a
        block GitHub renders, so it is no cut: `segments` ends a line where GFM
        does."""
        text = f"The parser drops a row{LS}- when the cell is wide"
        assert check.segments(text) == [(0, len(text))]


test_census = census_case(TARGET)
