"""`skills/verify/scripts/unverified_check.py`, one class per function.

Rebuilt by #942's phase 5 from `tests/test_unverified_rows_close.py`. The
script reads every `## Not verified` section, reports what is still open,
fails on a section it cannot read, and under `--baseline` fails on a row or
a record that left since the merge base, unless a settle removed it.

The readers of markdown, of a section and of a row run in the process on
lines and texts, with no git. The units that ask git, and `main` under
`--baseline`, read repositories built once for the module: a clone of two
work items and a tracked overview under `build/`, a clone whose second
overview is a tracked link to the first, a clone whose base
revisions are written the way the corpus was before it was normalised, a
clone with a moved base branch beside its work branch, a clone of work items
a settle can remove, a clone whose spec was dropped on the far side of a
merge, a clone with a `seal/` root beside a team's own `specs/`, and a
`seal/` root with no `specs/`. A case that writes into a world takes a copy,
and the copy is the reset. No world holds a file a case runs, so the copies
are plain copies.

`Test_module` also runs the command over a repository with and without a
team's own `specs/`, the planted team's case of
`tests/test_a_reference_root_is_read_and_never_taken.py`, which #942's round
10 fix pass split into one case per command; `TEAM` and `OURS` are
`tests/conftest.py`'s since then, because `planted` reads them too.
"""

import os
import random
import re
import shutil
import subprocess
import sys
import time

import pytest
from commonmark_oracle import heading_lines, hidden_text
from conftest import (
    OURS,
    ROOT,
    TEAM,
    census_case,
    commit_everything_as_e,
    git,
    git_out,
    load_module,
    planted,
    symlink_or_skip,
    write,
)

TARGET = "skills/verify/scripts/unverified_check.py"

UC = load_module(os.path.join(ROOT, *TARGET.split("/")), "unverified_check_under_test")
# `UC` under the name the heading rule's oracle cases were written with, so
# they stand here as they stood in the file on the one heading rule.
uc = UC

WORK = "1780000000-work"
OTHER = "1780000001-other"
TUI = "| how the gate renders in a TUI | user, on the next session |"
WINDOWS = "| whether Windows hooks fire | a maintainer with a Windows machine |"
CANONICAL = f"""## Not verified

| Item | Who must answer |
|---|---|
{TUI}
{WINDOWS}
"""
CLOSED_SECTION = """## Not verified

| Item | Who must answer |
|---|---|
| closed how the gate renders in a TUI | seen on screen, 2026-01-01 |
"""
# The sentence a section that holds nothing is told to write, pinned as the
# person reads it.
BLOCK = "the block `- nothing` with `  why: <reason>`"
# Spelt by code point, so no emoji and no invisible character stands in
# this file.
OLD_MARK = chr(0x2705)
ZERO_WIDTH_SPACE = chr(0x200B)
EMOJI_SELECTOR = chr(0xFE0F)
WORD_JOINER = chr(0x2060)


def memo(section, name=WORK):
    """An overview's text holding SECTION, under a heading and a section
    before it."""
    return f"# {name} overview\n\n## Not done\n\nsomething.\n\n{section}"


def memo_at(root, section, name=WORK):
    """The path of `specs/<name>/overview.md` under ROOT, written as
    `memo(section)`."""
    write(root, f"specs/{name}/overview.md", memo(section, name))
    return os.path.join(str(root), "specs", name, "overview.md")


def parse(section, strict_header=True):
    """`parse_section` over SECTION's lines after its heading, each line
    numbered as SECTION numbers it."""
    return UC.parse_section(UC.gfm_lines(section)[1:], 2, strict_header)


def same_path(a, b):
    """Whether A and B name one place, as git and the disk each spell it."""
    return os.path.normcase(os.path.realpath(a)) == os.path.normcase(
        os.path.realpath(b)
    )


def copy_of(world, tmp_path):
    """A copy of WORLD under TMP_PATH, links kept as links."""
    dst = tmp_path / world.name
    shutil.copytree(world, dst, symlinks=True)
    return dst


def drop_line(path, line):
    """The file at PATH without its line LINE."""
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    assert line + "\n" in text, line
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text.replace(line + "\n", ""))


def replace_in(path, old, new):
    """The file at PATH with OLD, which it holds, replaced by NEW."""
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    assert old in text, old
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text.replace(old, new))


def _committed(base, files):
    """A repository at BASE/repo holding FILES, `{rel: text}`, in one
    commit."""
    d = base / "repo"
    d.mkdir()
    git(d, "init", "-q", "-b", "main")
    for rel, text in files.items():
        write(d, rel, text)
    commit_everything_as_e(d, "the base")
    return d


@pytest.fixture(scope="module")
def plain(tmp_path_factory):
    """Two work items in the 0.3.x spelling, `specs/<id>/`, and an overview
    tracked under `build/`, which every walk skips."""
    return _committed(
        tmp_path_factory.mktemp("plain"),
        {
            f"specs/{WORK}/overview.md": memo(CANONICAL),
            f"specs/{OTHER}/overview.md": memo(CANONICAL, OTHER),
            "build/x/overview.md": memo(CANONICAL, "x"),
        },
    )


@pytest.fixture(scope="module")
def linked(tmp_path_factory):
    """One work item and a second whose overview is a tracked link to the
    first's."""
    d = _committed(
        tmp_path_factory.mktemp("linked"),
        {f"specs/{WORK}/overview.md": memo(CANONICAL)},
    )
    (d / "specs" / OTHER).mkdir()
    symlink_or_skip(
        os.path.join("..", WORK, "overview.md"),
        str(d / "specs" / OTHER / "overview.md"),
    )
    commit_everything_as_e(d, "a link")
    return d


# Base revisions written before the corpus was normalised, one work item
# each, and what the working tree writes over each before a case compares.
LEGACY = {
    "1780000020-old-heading": CANONICAL.replace(
        "## Not verified", "## Not verified (who must answer)"
    ).replace("| Item | Who must answer |", "| Item | Who |"),
    "1780000021-old-mark": CANONICAL.replace(
        "| whether Windows", f"| {OLD_MARK} whether Windows"
    ),
    "1780000022-prose": "## Not verified\n\n- the TUI rendering, as prose\n",
    "1780000023-both": CANONICAL
    + "\n### Not verified on Windows\n\n| a | b |\n|---|---|\n| x | y |\n",
    "1780000024-hidden-separator": CANONICAL.replace(
        "|---|---|", f"|-{ZERO_WIDTH_SPACE}--|---|"
    ),
    "1780000025-none-line": "## Not verified\n\nnone - nothing was left open\n",
}


@pytest.fixture(scope="module")
def legacy(tmp_path_factory):
    return _committed(
        tmp_path_factory.mktemp("legacy"),
        {f"specs/{name}/overview.md": memo(s, name) for name, s in LEGACY.items()},
    )


SIBLING = "1780000001-squashed-sibling"


@pytest.fixture(scope="module")
def forked(tmp_path_factory):
    """A work branch at the fork point, checked out, beside four refs: `fork`
    at the fork point itself; `base`, which moved past it when a sibling
    work item was squashed into it; `gained`, which gained a row in this
    branch's overview after the fork; and `unrelated`, a history of its
    own."""
    d = _committed(
        tmp_path_factory.mktemp("forked"),
        {f"specs/{WORK}/overview.md": memo(CANONICAL)},
    )
    git(d, "branch", "fork")
    git(d, "switch", "-qc", "base")
    write(d, f"specs/{SIBLING}/overview.md", memo(CANONICAL, SIBLING))
    commit_everything_as_e(d, "another work item, squashed into the base")
    git(d, "switch", "-qc", "gained", "fork")
    write(
        d,
        f"specs/{WORK}/overview.md",
        memo(CANONICAL)
        + "| whether the hooks fire on Windows | the same maintainer |\n",
    )
    commit_everything_as_e(d, "a third row, on the base")
    git(d, "switch", "-q", "--orphan", "unrelated")
    write(d, "readme.md", "no commit in common\n")
    commit_everything_as_e(d, "an unrelated root")
    git(d, "switch", "-qc", "work", "fork")
    return d


DOC = "# a\n\n## S\n\nAn old rule.\n"


def rule(text):
    return f"- add\n  file: docs/a.md\n  section: S\n  to: {text}\n"


SETTLE_A = "1780000001-a"
SETTLE_B = "1780000002-b"
SETTLE_C = "1780000003-c"
SETTLE_BAD = "1780000004-bad"
CLOSED_ITEM = "1780000009-closed"
OPEN_ITEM = "1780000010-open"
DROPPED = "1780000011-dropped"


@pytest.fixture(scope="module")
def settle(tmp_path_factory):
    """`docs/a.md` and work items a settle may remove: two whose rule
    changes add a sentence each, one whose spec has no `## Rule changes`,
    one whose section will not parse, and three with no spec, closed, open,
    and one whose spec an earlier commit dropped."""
    files = {"docs/a.md": DOC}
    specs = {
        SETTLE_A: f"# a\n\n## Rule changes\n\n{rule('A new rule.')}",
        SETTLE_B: f"# b\n\n## Rule changes\n\n{rule('Another rule.')}",
        SETTLE_C: "# c\n",
        SETTLE_BAD: "# bad\n\n## Rule changes\n\nnot an item\n",
    }
    for name, spec in specs.items():
        files[f"specs/{name}/overview.md"] = memo(CLOSED_SECTION, name)
        files[f"specs/{name}/spec.md"] = spec
    for name, section in (
        (CLOSED_ITEM, CLOSED_SECTION),
        (OPEN_ITEM, CANONICAL),
        (DROPPED, CLOSED_SECTION),
    ):
        files[f"specs/{name}/routing.md"] = f"# {name} routing\n"
        files[f"specs/{name}/overview.md"] = memo(section, name)
    files[f"specs/{DROPPED}/spec.md"] = "# a spec\n\nA rule.\n"
    d = _committed(tmp_path_factory.mktemp("settle"), files)
    git(d, "rm", "-q", f"specs/{DROPPED}/spec.md")
    commit_everything_as_e(d, "an earlier pull request drops it")
    return d


@pytest.fixture(scope="module")
def merged(tmp_path_factory):
    """A spec added and dropped on `release`, which reached `main` through a
    merge commit whose result matches the parent that never held it."""
    d = _committed(tmp_path_factory.mktemp("merged"), {"README.md": "r\n"})
    git(d, "switch", "-qc", "release")
    write(d, "seal/specs/1780000009-x/routing.md", "# x routing\n")
    write(d, "seal/specs/1780000009-x/spec.md", "# a spec\n\nA rule.\n")
    commit_everything_as_e(d, "a work item with a spec")
    git(d, "rm", "-q", "seal/specs/1780000009-x/spec.md")
    commit_everything_as_e(d, "the spec, dropped")
    git(d, "switch", "-q", "main")
    write(d, "other.md", "o\n")
    commit_everything_as_e(d, "main moves")
    git(d, "merge", "-q", "--no-ff", "-m", "release into main", "release")
    return d


MALFORMED = "## Not verified\n\nnot a table, and not a none line either\n"


@pytest.fixture(scope="module")
def joined(tmp_path_factory):
    """A `seal/` root holding one readable work item, and a team's own
    `specs/` whose overview the reader cannot read."""
    return _committed(
        tmp_path_factory.mktemp("joined"),
        {
            f"{OURS}/overview.md": memo(CANONICAL, "ours"),
            f"{TEAM}/overview.md": memo(MALFORMED, "team"),
            f"{TEAM}/spec.md": "# the team's spec\n",
        },
    )


@pytest.fixture(scope="module")
def sealed(tmp_path_factory):
    """A `seal/` root with no `specs/`, the tree a complete settle leaves."""
    return _committed(tmp_path_factory.mktemp("sealed"), {"seal/ledger.md": "# l\n"})


def run(argv):
    """`main`'s exit code, so a case asserts what CI would see."""
    return UC.main(argv)


# --- the readers of a line, a row and a section -------------------------------


class Test__LooseHeading:
    """The base revision's matcher: a level 2 or 3 heading by the one rule,
    mentioning `not verified` in any case (#867 round 1, finding 6)."""

    @pytest.mark.parametrize(
        "line",
        [
            "## Not verified",
            "### not VERIFIED, read",
            "   ## Not verified",
            "##\tNot verified",
        ],
    )
    def test_accepts_a_level_two_or_three_heading_naming_it(self, line):
        assert UC.LOOSE_HEADING.match(line) is True

    @pytest.mark.parametrize(
        "line",
        ["# Not verified", "#### Not verified", "#120) not verified", "## Not done"],
    )
    def test_refuses_another_level_a_line_that_is_no_heading_and_another_name(
        self, line
    ):
        assert UC.LOOSE_HEADING.match(line) is False


class Test_split_row:
    @pytest.mark.parametrize(
        "line, cells",
        [
            ("| a | b |", ["a", "b"]),
            ("  | a | b", ["a", "b"]),
            (
                "| whether `a \\| b` parses | the next session |",
                ["whether `a | b` parses", "the next session"],
            ),
            ("| a \\|", ["a |"]),
        ],
        ids=["closed", "open at the end", "an escaped pipe", "an escaped last pipe"],
    )
    def test_accepts_a_row_and_its_escaped_pipes(self, line, cells):
        assert UC.split_row(line) == cells

    def test_refuses_a_line_that_is_no_row(self):
        assert UC.split_row("- the TUI rendering, nobody has seen it") is None


class Test_is_separator:
    def test_accepts_dashes_and_alignment_colons(self):
        assert UC.is_separator(["---", ":-:", "-:"]) is True

    @pytest.mark.parametrize("cells", [[], ["---", "a"]], ids=["no cells", "a word"])
    def test_refuses_no_cells_and_a_cell_with_a_word(self, cells):
        assert UC.is_separator(cells) is False


class Test_is_header:
    def test_accepts_item_in_any_case(self):
        assert UC.is_header([" ITEM ", "Who"]) is True

    @pytest.mark.parametrize("cells", [[], ["Thing", "Who"]], ids=["no cells", "thing"])
    def test_refuses_no_cells_and_another_first_column(self, cells):
        assert UC.is_header(cells) is False


class Test_visible:
    def test_accepts_a_cell_without_what_takes_no_width(self):
        assert UC.visible(f" closed{ZERO_WIDTH_SPACE}{EMOJI_SELECTOR} ") == "closed"

    def test_refuses_to_take_out_what_a_reader_sees(self):
        assert UC.visible(" a  b ") == "a  b"


class Test_comment_scan:
    def test_accepts_each_line_with_the_state_it_began_in(self):
        lines = [
            "prose <!-- open",
            "still inside",
            "closed --> and prose again",
            "<!-- specs/x-1 -->",
        ]
        assert list(UC.comment_scan(lines)) == [
            (True, "prose "),
            (False, ""),
            (False, " and prose again"),
            (True, ""),
        ]

    @pytest.mark.parametrize(
        "lines, kept",
        [
            # Round 1 of #1000, finding 2: a table cell quoting the opener in
            # a code span, as two merged guarantees do.
            (["| `<!-- specs/` | y |", "Verdict: sealed"], None),
            # A double-backtick span holding a single backtick and the opener.
            (["a ``x `<!--` y`` b", "after"], None),
            # A run with no partner on its line is literal, so the opener
            # after it opens a comment.
            (["a ` b <!-- c", "hidden", "--> d"], ["a ` b ", "", " d"]),
            (["`a` <!-- c --> e", "x"], ["`a`  e", "x"]),
            # Inside a comment backticks are ordinary characters.
            (["<!-- `x --> y`", "z"], [" y`", "z"]),
        ],
        ids=[
            "a cell",
            "a doubled span",
            "an unpartnered run",
            "a span, then a comment",
            "backticks in a comment",
        ],
    )
    def test_refuses_an_opener_a_code_span_quotes(self, lines, kept):
        """CommonMark 6.1 gives a code span opened first precedence over an
        HTML comment inside it."""
        scanned = [text for _began, text in UC.comment_scan(lines)]
        assert scanned == (lines if kept is None else kept)

    @pytest.mark.parametrize(
        "tail", ["", "<!--"], ids=["no opener", "an opener at the end"]
    )
    def test_the_comment_scan_is_not_quadratic_in_backtick_runs(self, tail):
        """Round 2 of #1000, finding 1: 800000 characters of closed code
        spans, with no opener or with one at the end, and a line of backtick
        runs each without a partner of its own length, are each read inside
        the bound. The linear scan takes under 0.2 s on the first; the scan
        that sliced the line again per span took 54 s at 800000. The bound
        sits an order of magnitude from each, so a loaded runner does not
        fail it."""
        for line in (
            "`a` " * 200000 + tail,
            "".join("`" * k + "x" for k in range(1, 400)) + tail,
        ):
            start = time.monotonic()
            UC.strip_comments([line, "-->"])
            assert time.monotonic() - start < 5.0, len(line)


class Test_strip_comments:
    def test_accepts_comment_text_blanked_with_the_lines_kept(self):
        """A record started from a template before #1005 keeps the comment
        that explained a section beside it; #1012 retires the state."""
        lines = ["a <!-- b", "c", "d --> e"]
        assert UC.strip_comments(lines) == ["a ", "", " e"]

    def test_refuses_a_walk_of_its_own(self, monkeypatch):
        """A second copy of the walk inside `strip_comments` would answer as
        the real one does, so the scanner is replaced and the reader has to
        answer from the stub."""
        monkeypatch.setattr(UC, "comment_scan", lambda lines: iter([(False, "S")]))
        assert UC.strip_comments(["a <!-- b"]) == ["S"]


class Test_fence_spans:
    def test_accepts_each_closed_block_with_its_delimiters(self):
        lines = ["a", "```", "x", "```", "~~~", "y", "~~~"]
        assert UC.fence_spans(lines) == [(1, 3), (4, 6)]
        # A block with nothing in it closes on the line after its opener.
        assert UC.fence_spans(["```", "```", "x"]) == [(0, 1)]

    def test_refuses_to_close_a_block_nobody_closed(self):
        assert UC.fence_spans(["a", "```", "x"]) == [(1, None)]


class Test_closed_fence_lines:
    def test_accepts_the_lines_of_a_block_that_closes(self):
        assert UC.closed_fence_lines(["a", "```", "x", "```", "b"]) == {1, 2, 3}

    def test_refuses_the_lines_of_a_block_that_never_closes(self):
        assert UC.closed_fence_lines(["a", "```", "x", "```", "b", "```", "c"]) == {
            1,
            2,
            3,
        }


class Test_blank_fences:
    def test_accepts_a_closed_block_blanked_and_the_lines_kept(self):
        assert UC.blank_fences(["a", "```", "x", "```", "b"]) == ["a", "", "", "", "b"]

    def test_refuses_to_read_past_a_block_nobody_closed(self):
        assert UC.blank_fences(["a", "```", "x", "b"]) == ["a", "", "", ""]


class Test_liveness:
    SPAN = ("a span opens `here", "<!-- specs/s-6 -->", "and closes` there")

    @pytest.mark.parametrize(
        "lines, live",
        [
            (SPAN, [True, True, True]),
            (["x `<!--` y", "after"], [True, True]),
            (["x <!-- `y`", "after"], [True, False]),
            (
                ["<!-- open", "```", "-->", "<!-- specs/x -->"],
                [True, False, False, True],
            ),
        ],
        ids=[
            "a run alone is literal",
            "a span first",
            "an opener first",
            "no fence in a comment",
        ],
    )
    def test_accepts_the_literal_reading(self, lines, live):
        assert UC.liveness(lines, spans_cross_lines=False) == live

    def test_refuses_lines_a_span_reaching_across_them_parks(self):
        assert UC.liveness(self.SPAN, spans_cross_lines=True) == [True, False, False]


# The heading rule held to `tests/commonmark_oracle.py`, which reads
# markdown-it and nothing of this repository's (#867): on every line a
# renderer shows, `heading_level` answers what the parser's top-level ATX
# headings answer. A heading indented one to three spaces under a list item
# is that item's content, and a rule that reads one line cannot see the item
# above it, so the comparison skips such a line and counts it.
LIST_ITEM = ("- ", "* ", "+ ", "1. ", "1) ")


def disagreements(lines):
    """`([(index, ours, theirs)], skipped)` over the lines of a document a
    renderer shows, skipping a line indented one to three spaces below a
    list item (the module's stated limit). The file on the one heading rule
    imports it for its corpus of tracked files."""
    text = "\n".join(lines)
    hidden = hidden_text(text)
    theirs = heading_lines(text)
    out, skipped, under_a_list = [], 0, False
    for index, line in enumerate(lines):
        if line.lstrip(" ").startswith(LIST_ITEM):
            under_a_list = True
        if index in hidden:
            continue
        ours = uc.heading_level(line)
        if ours != theirs.get(index):
            if (
                under_a_list
                and line[:1] == " "
                and len(line) - len(line.lstrip(" ")) <= 3
            ):
                skipped += 1
                continue
            out.append((index, ours, theirs.get(index)))
    return out, skipped


SHAPES = {
    "a heading": (["## B"], 2),
    "indented three spaces": (["   ## B"], 2),
    "indented four spaces": (["    ## B"], None),
    "a tab before the run": (["\t## B"], None),
    "an issue number at column 0": (["#84's line"], None),
    "a wrapped issue reference": (["text", "#120) was it"], None),
    "seven hashes": (["####### x"], None),
    "a run and a tab": (["#\tx"], 1),
    "a run alone": (["#"], 1),
    "a closing run": (["## B ##"], 2),
    "no space after the run": (["#hello"], None),
    "a heading in a block quote": (["> # q"], None),
    "a heading in a list item": (["- # item"], None),
    "a heading after a paragraph": (["text", "## B"], 2),
}

SEED = 867
CORPUS_SIZE = 2000
ALPHABET = [
    "",
    "## B",
    "   ## B",
    "  ## B",
    " # x",
    "    ## B",
    "#120) x",
    "#84's",
    "####### x",
    "#",
    "#\tx",
    "\t# x",
    "## B ##",
    "x",
    "```",
    "~~~",
    "> # q",
    "- # item",
    "- item",
    "1. x",
    "<div>",
    "</div>",
    "---",
    "===",
    "* * *",
    "    code",
    "<!--",
    "-->",
    "| a | b |",
    "|---|---|",
]


class Test_heading_level:
    @pytest.mark.parametrize(
        "line, level",
        [("## Not verified", 2), ("   ## Not verified", 2), ("#\tx", 1), ("#", 1)],
    )
    def test_accepts_commonmarks_atx_heading(self, line, level):
        """CommonMark 4.2: at most three spaces, one to six `#`, then a
        space, a tab or the end (#867)."""
        assert UC.heading_level(line) == level

    @pytest.mark.parametrize(
        "line",
        ["    ## Not verified", "\t## Not verified", "#120) wrapped", "####### seven"],
    )
    def test_refuses_four_spaces_a_tab_an_issue_number_and_seven_hashes(self, line):
        assert UC.heading_level(line) is None

    @pytest.mark.parametrize("name", sorted(SHAPES))
    def test_the_frames_shapes(self, name):
        """S8's and S9's shapes: the rule's answer for the shape's last line, and
        markdown-it's, agree, and both are the level written beside it."""
        lines, level = SHAPES[name]
        assert uc.heading_level(lines[-1]) == level
        assert disagreements(lines) == ([], 0), name

    def test_a_seeded_generated_corpus(self):
        """S10, the generated half: CORPUS_SIZE documents of one to twelve lines
        drawn from ALPHABET, the same ones on every run (SEED), so a red is
        reproducible. Measured while building it: 3,000 documents found
        disagreements only on the stated limit."""
        rng = random.Random(SEED)
        found, skipped = [], 0
        for _ in range(CORPUS_SIZE):
            lines = [rng.choice(ALPHABET) for _ in range(rng.randint(1, 12))]
            wrong, limit = disagreements(lines)
            skipped += limit
            found.extend((lines, w) for w in wrong)
        assert not found, found[:5]
        assert skipped, "the corpus no longer reaches the stated limit"


class Test__paragraph_ends_at:
    @pytest.mark.parametrize(
        "line",
        [
            "",
            "| a |",
            "> q",
            "   # a heading",
            "```",
            "***",
            "- item",
            "===",
            "1. item",
        ],
    )
    def test_accepts_each_line_the_format_ends_a_paragraph_at(self, line):
        assert UC._paragraph_ends_at(line) is True

    @pytest.mark.parametrize(
        "line",
        [
            "text",
            "#hello",
            "####### seven",
            "    # four spaces is paragraph text",
            "3. item",
        ],
    )
    def test_refuses_paragraph_text(self, line):
        """#491's round-7 comment: four spaces before a heading is a lazy
        continuation line, and an ordered list interrupts a paragraph only
        when it starts with 1."""
        assert UC._paragraph_ends_at(line) is False


class Test__partner_ahead:
    def test_accepts_a_run_of_its_width_inside_the_paragraph(self):
        assert UC._partner_ahead(["text", "a ` b"], 0, 1) is True

    @pytest.mark.parametrize(
        "lines", [["", "a ` b"], ["a `` b"]], ids=["past a blank line", "another width"]
    )
    def test_refuses_a_run_past_the_paragraph_or_of_another_width(self, lines):
        assert UC._partner_ahead(lines, 0, 1) is False


MARKER = r"^<!-- specs/(\S+) -->$"


def live_markers(body):
    """The marker ids on the live lines of BODY, read line-anchored as the
    changelog gather writes one."""

    return {
        found
        for line, live in UC.live_lines(UC.gfm_lines(body))
        if live
        for found in re.findall(MARKER, line)
    }


class Test_live_lines:
    @pytest.mark.parametrize(
        "body, found",
        [
            ("<!-- specs/x-1 -->\n", {"x-1"}),
            ("```\nx\n```\n<!-- specs/x-6 -->\n", {"x-6"}),
            ("<!-- parked\n-->\n<!-- specs/c-3 -->\n", {"c-3"}),
            ("<!-- a note --> and prose\n<!-- specs/c-5 -->\n", {"c-5"}),
            # An opener quoted inside a code span is prose, not a draft
            # (round 3, finding 2).
            ("see `<!--` here\n<!-- specs/c-7 -->\n", {"c-7"}),
            # Round 1. Inside a draft nothing is markdown, so the quoted
            # closing delimiter really ends it and the marker below is live.
            (
                "<!-- a draft, parked\nprose with `-->` in it\n<!-- specs/s-1 -->\n-->\n",
                {"s-1"},
            ),
            # Round 2. A span quoting a whole comment keeps its closer.
            (
                "<!-- a draft, parked\nends with `<!-- a note -->` whole\n<!-- specs/s-2 -->\n-->\n",
                {"s-2"},
            ),
            # The control, without which every refusal is satisfied by a
            # reader that parks the whole document.
            ("# a policy\n\n<!-- specs/s-7 -->\nThe standing statement.\n", {"s-7"}),
        ],
        ids=[
            "a marker",
            "after a closed fence",
            "after a closed draft",
            "after a comment on one line",
            "after an opener in a span",
            "a closer quoted alone inside a draft",
            "a whole comment quoted inside a draft",
            "a genuine marker",
        ],
    )
    def test_accepts_a_marker_on_a_line_that_begins_live(self, body, found):
        assert live_markers(body) == found

    @pytest.mark.parametrize(
        "body",
        [
            "```markdown\n<!-- specs/x-2 -->\n```\n",
            "~~~\n<!-- specs/x-3 -->\n~~~\n",
            # A ``` inside a ```` block does not close it (CommonMark).
            "````\n```markdown\n<!-- specs/x-4 -->\n```\n````\n",
            "```\n<!-- specs/x-5 -->\n",
            "see `<!-- specs/x-7 -->` here\n",
            "<!-- parked\n<!-- specs/c-2 -->\n-->\n",
            "<!-- parked\n<!-- specs/c-4 -->\n",
            "<!-- parked\n```\n<!-- specs/c-6 -->\n```\n-->\n",
            # Round 3. A closer and then an opener inside one span: the draft
            # ends and re-opens, so the marker begins inside it.
            "<!-- a draft, parked\nquotes `--> and then <!--` here\n<!-- specs/s-3 -->\n-->\n",
            # Round 4. The same pair in two spans on one line.
            "<!-- a draft, parked\n`-->` and then `<!--` more\n<!-- specs/s-4 -->\n-->\n",
            # Round 5. An unclosed run, a draft opener on the next line, the
            # partner after it: the two readings disagree, so the line parks.
            "prose with an unclosed `run\n<!-- a draft, parked\nclosing ` here\n<!-- specs/s-5 -->\n-->\n",
            # A marker between the two halves of a code span.
            "a span opens `here\n<!-- specs/s-6 -->\nand closes` there\n",
            # Round 6. A delimiter indented four spaces is no delimiter, so it
            # does not invert the fence state of the example below.
            "A fence opens with\n\n    ```python\n\nand closes with a run "
            "at least as long.\n\n```markdown\n<!-- specs/s-8 -->\n```\n",
        ],
        ids=[
            "in a fence",
            "in a tilde fence",
            "in a longer fence",
            "in a fence nobody closed",
            "in a code span",
            "in a draft",
            "in a draft nobody closed",
            "in a fence in a draft",
            "a closer then an opener in one span",
            "a closer and an opener in two spans",
            "a span reaching past a draft opener",
            "inside a multi-line code span",
            "under an indented delimiter",
        ],
    )
    def test_refuses_a_marker_on_a_line_that_begins_parked(self, body):
        assert live_markers(body) == set()

    @pytest.mark.parametrize(
        "line, opens",
        [
            ("a `<!--` c", False),
            ("``a ` <!--`` c", False),
            ("`a` <!-- b", True),
            ("`open <!--", True),
            ("no span <!--", True),
            ("no span at all", False),
        ],
    )
    def test_a_code_span_closes_at_a_backtick_string_of_equal_length(self, line, opens):
        """CommonMark 6.1's span rule: equal-length backtick strings, an
        unmatched one left literal, observed as whether the line leaves a
        comment open."""
        answer = [live for _, live in UC.live_lines([line, "<!-- specs/x-1 -->"])]
        assert answer[0] is True
        assert answer[1] is not opens

    def test_the_scan_decides_a_fence_before_a_comment_or_a_span(self):
        """A fence opener owns its whole line, so a comment opener on it is
        fenced content and opens nothing."""
        lines = ["```markdown <!--", "<!-- specs/x-1 -->", "```", "<!-- specs/x-2 -->"]
        assert [live for _, live in UC.live_lines(lines)] == [True, False, False, True]

    def test_the_scan_never_reads_live_what_the_format_parks(self):
        """The safety direction, against a reading written from the format.
        `live_lines` parks a line wherever its two readings differ, so it
        parks lines the format calls live on purpose; what may never happen
        is the scan calling a line live that the format parks."""
        unsafe, live_seen = [], 0
        for lines in documents_with_several_spans_on_a_line(2000):
            scan = [live for _, live in UC.live_lines(lines)]
            truth = a_reading_from_the_commonmark_rules(lines)
            live_seen += sum(1 for v in scan if v)
            for n in range(len(lines)):
                if scan[n] and not truth[n]:
                    unsafe.append((lines, n, scan, truth))
        assert not unsafe, (
            f"{len(unsafe)} line(s) read live where the format parks; first: {unsafe[0]}"
        )
        # Not vacuous: a reader that parked everything would satisfy the above.
        assert live_seen > 2000, live_seen


class Test_readable:
    def test_accepts_the_lines_with_comments_and_fences_blanked(self):
        text = "a\n<!-- b -->\n```\n| x | y |\n```\n| c | d |\n"
        assert UC.readable(text) == ["a", "", "", "", "", "| c | d |"]

    def test_refuses_an_indented_delimiter_as_a_fence(self):
        """Four spaces before a run of backticks is never a delimiter
        (CommonMark 4.5); read as one, it opens a fence nobody closes and
        every row below it disappears."""
        text = "A fence opens with\n\n    ```\n\n| a | b |\n|---|---|\n| c | d |\n"
        assert "| c | d |" in UC.readable(text)

    @pytest.mark.parametrize(
        "lines, fenced",
        [
            # A closer carries nothing after its run.
            (["```", "inside", "```python", "quoted", "```", "after"], {0, 1, 2, 3, 4}),
            # A backtick opener whose info string holds a backtick opens nothing.
            (["```x`", "quoted", "after"], set()),
            # A tilde opener's info string is unrestricted.
            (["~~~ `x`", "quoted", "~~~", "after"], {0, 1, 2}),
        ],
    )
    def test_each_reader_asks_the_one_delimiter_rule(self, lines, fenced):
        """`readable` blanks exactly the fenced lines, and `live_lines` calls
        exactly those not live but the opener's own line."""
        blanked = {
            n for n, line in enumerate(UC.readable("\n".join(lines))) if not line
        }
        assert blanked == fenced, blanked
        openers = {first for first, _ in UC.fence_spans(lines)}
        parked = {n for n, (_, live) in enumerate(UC.live_lines(lines)) if not live}
        assert parked == fenced - openers, parked

    def test_readable_would_erase_every_fold_record(self):
        """Why the pair `check_text` uses is the wrong reader for a marker:
        it blanks the marker, which `live_lines` reads live."""
        marker = ["<!-- specs/1780000000-work -->", "A standing statement."]
        assert UC.readable("\n".join(marker))[0] == ""
        assert next(iter(UC.live_lines(marker)))[1] is True


class Test_headings:
    def test_accepts_each_heading_by_the_one_rule(self):
        lines = ["## a", "text", "   ### b  ", "#120) wrapped"]
        assert UC.headings(lines) == [(0, "## a"), (2, "   ### b")]

    def test_refuses_a_line_opening_with_an_issue_number(self):
        assert UC.headings(["#120) wrapped onto its own line"]) == []


class Test_items:
    def test_accepts_items_their_fields_and_a_continued_value(self):
        body = [
            (1, "- add"),
            (2, "  file: a.md"),
            (3, "  to: one"),
            (4, "    two"),
            (5, ""),
        ]
        found, error = UC.items(body)
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
        assert UC.items(body)[1] == error


class Test_field_values:
    def test_accepts_each_field_joined_and_trimmed(self):
        item = {
            "kind": "nothing",
            "line": 1,
            "fields": {"why": [2, ["every claim", "was run", ""]]},
        }
        assert UC.field_values(item, ("why",), ()) == (
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
        assert UC.field_values(item, ("why",), ()) == (None, error)


class Test_opens_the_block:
    def test_accepts_the_item_nothing(self):
        assert UC.opens_the_block("- nothing") is True

    @pytest.mark.parametrize("line", ["- Nothing", "* nothing", "- nothings"])
    def test_refuses_another_spelling(self, line):
        assert UC.opens_the_block(line) is False


class Test_nothing_block:
    @pytest.mark.parametrize(
        "body, answer",
        [
            ([(3, "- nothing"), (4, "  why: all run.")], ("all run.", None)),
            ([(3, "| Item | Who must answer |")], None),
        ],
        ids=["the block", "a table"],
    )
    def test_accepts_the_block_and_passes_a_table_on(self, body, answer):
        assert UC.nothing_block(body) == answer

    @pytest.mark.parametrize(
        "body, error",
        [
            ([(3, "none - x")], (3, f"a section that holds nothing writes {BLOCK}")),
            (
                [(3, "- nothing"), (4, "  why: x"), (5, "- nothing"), (6, "  why: y")],
                (5, "`- nothing` is the section's one item"),
            ),
        ],
        ids=["the old line", "two items"],
    )
    def test_refuses_a_near_miss_and_a_second_item(self, body, error):
        assert UC.nothing_block(body) == (None, error)


def line_of(section, needle):
    """The line number SECTION gives its first line that is NEEDLE."""
    return section.split("\n").index(needle) + 1


class Test_parse_section:
    @pytest.mark.parametrize(
        "row, closed",
        [
            (
                "| closed how the gate renders in a TUI | seen on screen |",
                "how the gate renders in a TUI",
            ),
            (
                "| closed\thow the gate renders in a TUI | seen on screen |",
                "how the gate renders in a TUI",
            ),
            # The open item whose own text begins with the word reads closed,
            # which only a reader catches.
            ("| closed issues are not re-read | the owner |", "issues are not re-read"),
            ("| closed-loop control on Windows | a maintainer |", None),
            ("| enclosed paths on Windows | a maintainer |", None),
            ("| whether `a \\| b` parses | the next session |", None),
        ],
        ids=[
            "the word",
            "the word and a tab",
            "an item that begins with it",
            "a word that begins with it",
            "a word that holds it",
            "an escaped pipe",
        ],
    )
    def test_accepts_open_rows_and_the_word_that_closes_one(self, row, closed):
        open_rows, closed_rows, errors = parse(CANONICAL.replace(TUI, row))
        assert not errors, errors
        if closed is None:
            assert not closed_rows and len(open_rows) == 2
        else:
            assert [c[1] for c in closed_rows] == [closed] and len(open_rows) == 1

    @pytest.mark.parametrize(
        "block",
        [
            "- nothing\n  why: every claim in this item was executed.\n",
            "- nothing\n  why: every claim in this item\n    was executed.\n",
        ],
        ids=["one line", "continued four spaces in"],
    )
    def test_accepts_the_no_change_block_as_nothing_open(self, block):
        """S1 of #1000: silence and "nothing open" look different in the
        file, not only in the tally."""
        assert parse(f"## Not verified\n\n{block}") == ([], [], [])

    @pytest.mark.parametrize(
        "section, rows",
        [
            (
                CANONICAL.replace("| whether Windows", f"| {OLD_MARK} whether Windows"),
                (1, 1),
            ),
            ("## Not verified\n\nnone - x\n", (0, 0)),
            (CANONICAL.replace("| Item | Who must answer |", "| Item | Who |"), (2, 0)),
        ],
        ids=["the old mark", "the old line", "the old column"],
    )
    def test_accepts_what_a_base_revision_wrote_before_the_word(self, section, rows):
        """A base revision cannot be edited, so it is read the way it was
        written: the old mark closes a row, the old `none` line holds no
        rows, and a header needs only `Item` first."""
        open_rows, closed_rows, errors = parse(section, strict_header=False)
        assert not errors, errors
        assert (len(open_rows), len(closed_rows)) == rows

    @pytest.mark.parametrize(
        "section, at, says",
        [
            ("## Not verified\n\n", 2, "the section is empty"),
            (
                "## Not verified\n\n- the TUI rendering, nobody has seen it\n",
                3,
                "found prose",
            ),
            (
                CANONICAL.replace("| Item | Who must answer |", "| Item | Who |"),
                3,
                "header is |Item|Who|",
            ),
            (
                "## Not verified\n\n| Item | Who must answer |\n| an item | someone |\n",
                3,
                "not followed by a separator row",
            ),
            (
                "## Not verified\n\n| Item | Who must answer |\n|---|---|\n",
                3,
                "no rows",
            ),
            (CANONICAL + "#120) wrapped onto its own line\n", 7, "not a table row"),
            (
                CANONICAL + "| an item | an answerer | a third cell |\n",
                7,
                "3 cells, expected 2",
            ),
            (CANONICAL + "| Item | Who must answer |\n", 7, "one table"),
            (CANONICAL + f"|-{ZERO_WIDTH_SPACE}--|---|\n", 7, "one table"),
            (CANONICAL + "| an item with no answerer | |\n", 7, "an empty cell"),
            (
                CANONICAL + f"| {ZERO_WIDTH_SPACE} | {ZERO_WIDTH_SPACE} |\n",
                7,
                "an empty cell",
            ),
            (
                CANONICAL + "| <what was not verified> | <who answers it> |\n",
                7,
                "placeholder",
            ),
            (CANONICAL + "| an item | <who answers it> |\n", 7, "placeholder"),
        ],
        ids=[
            "empty",
            "prose",
            "the old column",
            "no separator",
            "no rows",
            "an issue number",
            "three cells",
            "a second header",
            "a hidden separator",
            "an empty cell",
            "invisible cells",
            "the placeholder",
            "a placeholder answerer",
        ],
    )
    def test_refuses_a_section_it_cannot_count_at_its_line(self, section, at, says):
        errors = parse(section)[2]
        assert errors and errors[0][0] == at and says in errors[0][1], errors

    @pytest.mark.parametrize(
        "row, says",
        [
            ("| closed | done |", "bare"),
            (f"| closed{ZERO_WIDTH_SPACE} | done |", "bare"),
            (f"| closed{EMOJI_SELECTOR} | done |", "bare"),
            (f"| closed{WORD_JOINER} | done |", "bare"),
            (
                f"| {OLD_MARK}{EMOJI_SELECTOR} how the gate renders in a TUI | seen |",
                "U+2705",
            ),
            (f"| {OLD_MARK} | done |", "U+2705"),
            ("| Closed how the gate renders in a TUI | seen on screen |", "`Closed`"),
            ("| CLOSED how the gate renders in a TUI | seen on screen |", "`CLOSED`"),
            ("| closed: how the gate renders in a TUI | seen on screen |", "`closed:`"),
        ],
        ids=[
            "bare",
            "a zero-width space",
            "a selector",
            "a word joiner",
            "the old mark as a keyboard emits it",
            "the bare old mark",
            "capitalised",
            "upper case",
            "a colon",
        ],
    )
    def test_refuses_a_bare_word_the_old_mark_and_another_spelling(self, row, says):
        """T4 of `1792129100-the-mechanics-leave-before-the-agents-are-rewritten`:
        a closing that a capital or a colon would turn back into an open
        row, a bare word, and the emoji mark."""
        _, _, errors = parse(CANONICAL.replace(TUI, row))
        assert errors and says in errors[0][1], errors

    def test_refuses_the_old_mark_naming_the_edit(self):
        """Contract rule 14: the sentence a person reads when their overview
        still carries the old mark, pinned whole."""
        row = f"| {OLD_MARK} how the gate renders in a TUI | seen on screen |"
        _, _, errors = parse(CANONICAL.replace(TUI, row))
        assert errors[0] == (
            5,
            "the row opens with U+2705, which no longer closes a row: a closed "
            "row opens with the word `closed`, so write "
            "`| closed how the gate renders in a TUI | <what closed it> |`",
        )

    @pytest.mark.parametrize("first", ["none - x", "none", "None.", "nothing - x"])
    def test_refuses_the_old_line_naming_the_block(self, first):
        """S2 of #1000: the working tree refuses the old line and its near
        misses at the line, naming the block."""
        section = f"## Not verified\n\n{first}\n"
        assert parse(section) == (
            [],
            [],
            [(3, f"a section that holds nothing writes {BLOCK}")],
        )

    @pytest.mark.parametrize(
        "body, bad, says",
        [
            ("- nothing\n", "- nothing", "`nothing` needs `why`"),
            ("- nothing\n  why:\n", "  why:", "`why` is empty"),
            ("- Nothing\n  why: x\n", "- Nothing", BLOCK),
            ("-nothing\n  why: x\n", "-nothing", BLOCK),
            ("- nothing\n   why: x\n", "   why: x", "not a field"),
            ("- nothing\n  why: x\n  who: y\n", "  who: y", "`who` is not a field"),
            (
                "- nothing\n  why: x\n" + CANONICAL.split("\n", 2)[2],
                "| Item | Who must answer |",
                "not a field",
            ),
        ],
        ids=[
            "no why",
            "an empty why",
            "capitalised",
            "no space after the dash",
            "why at three spaces",
            "a second field",
            "beside a table",
        ],
    )
    def test_refuses_a_near_miss_of_the_block_at_its_line(self, body, bad, says):
        """S3 of #1000: each spelling is refused at its line, saying what is
        wrong with it, and read as nothing else."""
        section = f"## Not verified\n\n{body}"
        open_rows, closed_rows, errors = parse(section)
        assert errors and errors[0][0] == line_of(section, bad), errors
        assert says in errors[0][1], errors
        assert not open_rows and not closed_rows

    def test_refuses_a_header_without_item_first_even_at_a_base(self):
        """A relaxation with no floor reads any two-column table as the
        record."""
        section = CANONICAL.replace("| Item | Who must answer |", "| Thing | Who |")
        _, _, errors = parse(section, strict_header=False)
        assert errors and "header is" in errors[0][1]

    def test_the_near_miss_reading_is_linear_in_the_line(self):
        """#941's round 3 met a pattern that backtracked exponentially; a
        long line of the near-miss pattern's repeated characters is read
        well inside the bound."""
        start = time.monotonic()
        for line in ("- " * 50000 + "x", " " * 100000 + "nonesuch", "-*+" * 30000):
            UC.parse_section([line], 1)
        assert time.monotonic() - start < 5.0


class Test_closing_word:
    @pytest.mark.parametrize(
        "cell, answer",
        [
            ("closed how it renders", ("closed", "how it renders")),
            (f"{OLD_MARK}how it renders", (OLD_MARK, "how it renders")),
            (
                f"{OLD_MARK}{EMOJI_SELECTOR} how it renders",
                (OLD_MARK, "how it renders"),
            ),
        ],
        ids=[
            "the word",
            "the old mark with no space",
            "the old mark as a keyboard emits it",
        ],
    )
    def test_accepts_the_first_word_and_the_rest(self, cell, answer):
        assert UC.closing_word(cell) == answer

    def test_refuses_to_invent_a_word_for_an_empty_cell(self):
        assert UC.closing_word("") == ("", "")


class Test_check_file:
    def test_accepts_an_overview_on_disk(self, tmp_path):
        open_rows, closed_rows, errors = UC.check_file(memo_at(tmp_path, CANONICAL))
        assert not errors and len(open_rows) == 2 and not closed_rows

    def test_refuses_a_file_it_cannot_open(self, tmp_path):
        _, _, errors = UC.check_file(str(tmp_path / "overview.md"))
        assert (
            errors and errors[0][0] == 0 and errors[0][1].startswith("cannot be read: ")
        )


class Test_sections:
    LINES = (
        "## Not verified",
        "x",
        "## Not verified (who must answer)",
        "### Not verified on Windows",
    )

    def test_accepts_the_canonical_heading_over_a_looser_match(self):
        """A base holding both the heading and one that mentions it would
        otherwise count differently from the working tree."""
        assert UC.sections(self.LINES, UC.LOOSE_HEADING) == [0]
        assert UC.sections(self.LINES[1:], UC.LOOSE_HEADING) == [1, 2]

    def test_refuses_another_spelling_of_the_heading(self):
        assert UC.sections(self.LINES[1:], UC.HEADING) == []


class Test_check_text:
    @pytest.mark.parametrize(
        "section, count",
        [
            (CANONICAL, 2),
            # Rows below an example are counted, and the example is no
            # second section.
            (
                CANONICAL
                + "\n```markdown\n## Not verified\n\n| Item | Who |\n```\n\n| a third item | someone |\n",
                3,
            ),
            (
                CANONICAL
                + "\n~~~markdown\n| Item | Who must answer |\n~~~\n\n| a third item | someone |\n",
                3,
            ),
            # A guidance comment an overview started before #1005 keeps;
            # #1012 retires the state.
            (
                "## Not verified\n\n<!-- guidance:\n| closed <item> | <what closed it> |\n-->\n\n"
                + CANONICAL.split("\n", 2)[2],
                2,
            ),
            # Round 1 of #1000: a row quoting the opener in a code span hides
            # no row below it.
            (
                CANONICAL.replace(
                    "| how the gate renders in a TUI |",
                    "| whether `<!--` in a cell hides rows |",
                ),
                2,
            ),
        ],
        ids=[
            "the table",
            "a fenced example",
            "a tilde fence",
            "a guidance comment",
            "an opener in a span",
        ],
    )
    def test_accepts_the_rows_of_the_one_section(self, section, count):
        open_rows, _, errors = UC.check_text(memo(section))
        assert not errors, errors
        assert len(open_rows) == count

    def test_accepts_a_line_opening_with_an_issue_number_inside_the_section(self):
        """S9 of #867: the line is paragraph text inside the section, so the
        row below it is counted and the line is named as no row."""
        text = memo(
            CANONICAL
            + "#120) wrapped onto its own line\n| a third item | the owner |\n"
        )
        open_rows, _, errors = UC.check_text(text)
        assert len(open_rows) == 3
        assert [message for _, message in errors] == [
            "a line inside the table that is not a table row"
        ]

    @pytest.mark.parametrize(
        "heading",
        [
            "## Not verified (who must answer)",
            "## Blocked / not verified (who must answer)",
            "## Not Verified",
        ],
    )
    def test_refuses_a_spelling_it_does_not_know_and_names_it(self, heading):
        """All three spellings were in this corpus. The failure prevented is
        a reader that shrugs and returns zero."""
        _, _, errors = UC.check_text(
            memo(CANONICAL.replace("## Not verified", heading))
        )
        assert errors == [
            (1, f"no `## Not verified` section (found `{heading}` at line 7)")
        ]

    @pytest.mark.parametrize(
        "text, error",
        [
            (
                memo("## Fed back into the spec\n\nnone.\n"),
                (1, "no `## Not verified` section"),
            ),
            (
                memo(CANONICAL + "\n" + CANONICAL),
                (14, "more than one `## Not verified` section: lines 7, 14"),
            ),
            (
                memo("## Not verified\n\n## Fed back into the spec\n\nnone.\n"),
                (8, "the section is empty: write the table, or " + BLOCK),
            ),
        ],
        ids=["none", "two", "an empty one"],
    )
    def test_refuses_no_section_two_sections_and_an_empty_one(self, text, error):
        assert UC.check_text(text)[2] == [error]


# --- the walk and the paths it compares ---------------------------------------


class Test_overviews:
    def test_accepts_every_overview_under_a_path_once_skipping_build_output(
        self, tmp_path
    ):
        for rel in ("specs/b", "specs/a", "build/c", "node_modules/d", ".venv/e"):
            write(tmp_path, f"{rel}/overview.md", memo(CANONICAL))
        named = str(tmp_path / "specs" / "a" / "overview.md")
        found = UC.overviews([str(tmp_path), named])
        here = os.path.realpath(str(tmp_path))
        assert found == [
            os.path.join(here, "specs", "a", "overview.md"),
            os.path.join(here, "specs", "b", "overview.md"),
        ]

    def test_refuses_a_reference_root_on_a_walk_and_reads_it_named(self, joined):
        """D2 of #688: a team's own `specs/` is read as history, never as
        this plugin's record, unless the person names it."""
        walked = UC.overviews([str(joined)])
        assert [os.path.basename(os.path.dirname(p)) for p in walked] == [
            "1790000000-ours"
        ]
        named = UC.overviews([str(joined / "specs")])
        assert [os.path.basename(os.path.dirname(p)) for p in named] == [
            "1788000001-team-thing"
        ]


class Test_config_at:
    def test_accepts_the_config_reader_and_the_root(self, joined):
        config, home = UC.config_at(str(joined))
        assert callable(config.reference_roots)
        assert same_path(home, joined / "seal")

    def test_refuses_to_invent_a_root(self, plain):
        _config, home = UC.config_at(str(plain))
        assert not home


class Test_references_at:
    def test_accepts_the_default_under_a_root_and_none_without_one(self, joined, plain):
        assert UC.references_at(str(joined))[1] is None
        assert UC.references_at(str(plain))[1] == ()

    def test_refuses_to_fail_a_copy_with_no_hooks_beside_it(
        self, joined, monkeypatch, tmp_path
    ):
        monkeypatch.setattr(UC, "HOOKS", str(tmp_path / "no-hooks-here"))
        assert UC.references_at(str(joined)) is None


class Test_policy_root:
    def test_accepts_the_row_a_config_writes(self, joined, tmp_path):
        d = copy_of(joined, tmp_path)
        write(
            d,
            "seal/config.md",
            "| Item | Value |\n|---|---|\n| Policy root | rules |\n",
        )
        assert UC.policy_root(str(d)) == "rules"

    def test_refuses_to_read_anything_but_docs_with_no_row(self, joined):
        assert UC.policy_root(str(joined)) == "docs"


class Test_reference_rule:
    def test_accepts_a_predicate_true_for_a_reference_root(self, joined):
        skip = UC.reference_rule(str(joined))
        assert skip(str(joined / "specs")) is True
        assert skip(str(joined / "seal" / "specs")) is False

    @pytest.mark.parametrize("where", ["inside", "outside"])
    def test_refuses_to_prune_a_named_root_or_outside_a_repository(
        self, joined, tmp_path, where
    ):
        start = joined / "specs" if where == "inside" else tmp_path
        assert UC.reference_rule(str(start)) is None


class Test_real:
    def test_accepts_a_path_through_a_link_as_its_target(self, tmp_path):
        (tmp_path / "target").mkdir()
        symlink_or_skip(str(tmp_path / "target"), str(tmp_path / "link"))
        assert UC.real(str(tmp_path / "link")) == os.path.realpath(
            str(tmp_path / "target")
        )

    def test_refuses_to_move_a_path_with_no_link(self, tmp_path):
        assert UC.real(str(tmp_path)) == os.path.realpath(str(tmp_path))


class Test_git_path:
    def test_accepts_a_windows_path_as_git_spells_it(self, monkeypatch):
        r"""git answers and accepts `/` on every platform; `os.sep` is
        monkeypatched because `git_path` reads it at call time, so the
        Windows branch runs on every leg."""
        monkeypatch.setattr(os, "sep", "\\")
        assert UC.git_path("specs\\1780000000-work\\overview.md") == (
            "specs/1780000000-work/overview.md"
        )
        assert UC.git_path("specs/1780000000-work/overview.md") == (
            "specs/1780000000-work/overview.md"
        )

    def test_refuses_to_rewrite_a_backslash_in_a_posix_name(self, monkeypatch):
        monkeypatch.setattr(os, "sep", "/")
        assert UC.git_path("specs/odd\\name.md") == "specs/odd\\name.md"


def refuses(path, start=None):
    raise ValueError("path is on mount 'D:', start on mount 'C:'")


class Test_repo_relative:
    def test_accepts_a_path_inside_the_root(self, tmp_path):
        inside = os.path.join(str(tmp_path), "specs", "a", "overview.md")
        assert UC.repo_relative(inside, str(tmp_path)) == "specs/a/overview.md"

    def test_refuses_a_path_with_no_relative_form(self, monkeypatch):
        monkeypatch.setattr(os.path, "relpath", refuses)
        assert UC.repo_relative(os.path.abspath("x"), os.path.abspath("y")) is None


class Test_display_path:
    def test_accepts_a_path_relative_to_where_the_run_started(self, tmp_path):
        inside = os.path.join(str(tmp_path), "specs", "overview.md")
        assert UC.display_path(inside, str(tmp_path)) == os.path.join(
            "specs", "overview.md"
        )

    def test_refuses_to_die_on_a_path_with_no_relative_form(self, monkeypatch):
        """`relpath` raises on Windows across drives, and this is the footing
        for every line the tool prints; driven by making it raise, so every
        leg runs it."""
        monkeypatch.setattr(os.path, "relpath", refuses)
        where = os.path.join("x", "overview.md")
        assert UC.display_path(where, os.path.abspath("y")) == os.path.abspath(where)


class Test_nearest_existing:
    def test_accepts_a_path_that_exists(self, tmp_path):
        assert UC.nearest_existing(str(tmp_path)) == os.path.abspath(str(tmp_path))

    def test_refuses_a_path_two_levels_gone_for_its_nearest_ancestor(self, tmp_path):
        gone = os.path.join(str(tmp_path), "a", "b", "overview.md")
        assert UC.nearest_existing(gone) == os.path.abspath(str(tmp_path))


class Test_unique_by_target:
    def test_accepts_every_path_to_a_file_of_its_own(self, tmp_path):
        paths = [str(tmp_path / "a"), str(tmp_path / "b")]
        assert UC.unique_by_target(paths) == paths

    def test_refuses_a_second_path_to_one_file(self, tmp_path):
        p = str(tmp_path / "a")
        assert UC.unique_by_target([p, os.path.join(str(tmp_path), ".", "a")]) == [p]


# --- what git answers ---------------------------------------------------------


def answering(monkeypatch, word, stdout):
    """`subprocess.run` in the module answering exit 0 with STDOUT to every
    git call that carries WORD, and running every other call."""
    real_run = subprocess.run

    def stub(argv, *a, **kw):
        if isinstance(argv, list) and word in argv:
            return subprocess.CompletedProcess(argv, 0, stdout, "")
        return real_run(argv, *a, **kw)

    monkeypatch.setattr(UC.subprocess, "run", stub)


class Test_repo_root:
    def test_accepts_a_directory_and_a_file_inside_the_repository(self, plain):
        assert same_path(UC.repo_root(str(plain / "specs")), plain)
        assert same_path(
            UC.repo_root(str(plain / "specs" / WORK / "overview.md")), plain
        )

    def test_refuses_a_directory_outside_every_repository(self, tmp_path):
        assert UC.repo_root(str(tmp_path)) is None


class Test_commit_of:
    def test_accepts_a_ref_as_its_commit(self, plain):
        assert UC.commit_of(str(plain), "HEAD") == git_out(plain, "rev-parse", "HEAD")

    def test_refuses_a_ref_that_does_not_resolve_or_answers_nothing(
        self, plain, monkeypatch
    ):
        assert UC.commit_of(str(plain), "origin/nosuchbranch") is None
        answering(monkeypatch, "--verify", "\n")
        assert UC.commit_of(str(plain), "HEAD") is None


class Test_resolves:
    def test_accepts_a_ref_that_names_a_commit(self, plain):
        assert UC.resolves(str(plain), "HEAD") is True

    def test_refuses_a_ref_git_answers_with_nothing(self, plain, monkeypatch):
        """`chain_check.py` loads this for whether a ref resolves; an empty
        answer is a refusal, not a sentinel travelling out as resolved."""
        answering(monkeypatch, "--verify", "\n")
        assert UC.resolves(str(plain), "HEAD") is False


class Test_merge_base:
    def test_accepts_the_fork_point_of_a_moved_base(self, forked):
        assert UC.merge_base(str(forked), "base") == git_out(
            forked, "rev-parse", "fork"
        )

    def test_refuses_an_unrelated_history_and_an_empty_answer(
        self, forked, monkeypatch
    ):
        assert UC.merge_base(str(forked), "unrelated") is None
        answering(monkeypatch, "merge-base", "\n")
        assert UC.merge_base(str(forked), "base") is None


class Test_base_label:
    def test_accepts_the_ref_where_it_is_the_merge_base(self):
        assert UC.base_label("HEAD", "a" * 40, "a" * 40) == "HEAD"

    def test_refuses_the_ref_alone_where_the_base_moved(self):
        assert UC.base_label("base", "a" * 40, "b" * 40) == (
            "the merge-base of base and HEAD (bbbbbbb)"
        )
        assert UC.base_label("HEAD", None, "c" * 40).endswith("(ccccccc)")


class Test_overviews_at:
    def test_accepts_the_overviews_under_each_prefix(self, plain):
        work, other = (f"specs/{n}/overview.md" for n in (WORK, OTHER))
        assert UC.overviews_at(str(plain), "HEAD", ["."]) == [work, other]
        assert UC.overviews_at(str(plain), "HEAD", [f"specs/{WORK}"]) == [work]

    def test_accepts_a_reference_root_a_prefix_names(self, joined):
        assert UC.overviews_at(str(joined), "HEAD", ["."]) == [f"{OURS}/overview.md"]
        assert UC.overviews_at(str(joined), "HEAD", ["specs"]) == [
            f"{TEAM}/overview.md"
        ]

    @pytest.mark.parametrize(
        "ref, prefix",
        [("HEAD", "specs/1780000000-wor"), ("HEAD", "build"), ("nosuch", ".")],
        ids=[
            "a prefix of a name",
            "a skipped directory",
            "a ref that does not resolve",
        ],
    )
    def test_refuses_a_partial_name_a_skipped_directory_and_an_unknown_ref(
        self, plain, ref, prefix
    ):
        assert UC.overviews_at(str(plain), ref, [prefix]) == []


class Test_tree_at:
    def test_accepts_a_directory_at_a_ref_and_on_disk(self, settle):
        listed = [f"specs/{SETTLE_A}/overview.md", f"specs/{SETTLE_A}/spec.md"]
        assert UC.tree_at(str(settle), "HEAD", f"specs/{SETTLE_A}") == listed
        assert UC.tree_at(str(settle), None, f"specs/{SETTLE_A}") == listed

    @pytest.mark.parametrize("ref", ["HEAD", None, "nosuch"])
    def test_refuses_a_directory_that_is_not_there(self, settle, ref):
        directory = "specs/none" if ref != "nosuch" else f"specs/{SETTLE_A}"
        assert UC.tree_at(str(settle), ref, directory) == []


class Test__text_at:
    def test_accepts_a_file_at_a_ref_and_on_disk(self, settle):
        assert UC._text_at(str(settle), "HEAD", "docs/a.md") == DOC
        assert UC._text_at(str(settle), None, "docs/a.md") == DOC

    @pytest.mark.parametrize("ref", ["HEAD", None])
    def test_refuses_a_file_that_is_not_there(self, settle, ref):
        assert UC._text_at(str(settle), ref, "docs/none.md") is None


class Test_show:
    def test_accepts_a_path_at_a_ref(self, plain):
        assert UC.show(str(plain), "HEAD", f"specs/{WORK}/overview.md") == memo(
            CANONICAL
        )

    def test_refuses_a_path_the_ref_does_not_hold(self, plain):
        assert UC.show(str(plain), "HEAD", "specs/none/overview.md") is None


# --- what a settle removed ----------------------------------------------------


class Test_rule_changes:
    def test_accepts_the_one_reader_of_a_specs_rule_changes(self):
        rules = UC.rule_changes()
        assert callable(rules.parse) and callable(rules.replay)

    def test_refuses_to_load_it_twice(self):
        assert UC.rule_changes() is UC.rule_changes()


class Test_policy_documents:
    def test_accepts_each_file_under_the_policy_root(self, settle):
        assert UC.policy_documents(str(settle), "HEAD", "docs") == {"docs/a.md": DOC}
        assert UC.policy_documents(str(settle), None, "docs") == {"docs/a.md": DOC}

    def test_refuses_a_policy_root_that_is_not_there(self, settle):
        assert UC.policy_documents(str(settle), "HEAD", "rules") == {}


class Test_open_record_rows:
    def test_accepts_every_open_item_of_the_record(self, settle):
        assert UC.open_record_rows(str(settle), "HEAD", f"specs/{OPEN_ITEM}") == [
            ("overview.md", "how the gate renders in a TUI"),
            ("overview.md", "whether Windows hooks fire"),
        ]
        assert UC.open_record_rows(str(settle), None, f"specs/{CLOSED_ITEM}") == []

    def test_accepts_a_base_written_before_the_normalisation(self, legacy):
        rows = UC.open_record_rows(str(legacy), "HEAD", "specs/1780000020-old-heading")
        assert [item for _, item in rows] == [
            "how the gate renders in a TUI",
            "whether Windows hooks fire",
        ]

    def test_refuses_to_read_a_section_it_cannot_read_as_nothing_open(self, legacy):
        """A count this cannot read is not a count of nothing."""
        rows = UC.open_record_rows(str(legacy), "HEAD", "specs/1780000022-prose")
        assert len(rows) == 1 and rows[0][1].startswith("cannot be read (expected"), (
            rows
        )


class Test_wrote_a_spec:
    @pytest.mark.parametrize("directory", [DROPPED, SETTLE_A])
    def test_accepts_a_spec_written_once_and_one_still_there(self, settle, directory):
        """Round 1's finding 3: a spec an earlier commit deleted was still
        written, so its directory is no spec-less work item."""
        assert UC.wrote_a_spec(str(settle), "HEAD", f"specs/{directory}") is True

    def test_accepts_a_spec_dropped_on_the_far_side_of_a_merge(self, merged):
        """Round 2's finding 6: at the merge the path matches the parent that
        never held it, so `git log` without `--full-history` follows that
        parent alone."""
        assert UC.wrote_a_spec(str(merged), "HEAD", "seal/specs/1780000009-x") is True
        assert not UC.settled(str(merged), "HEAD", ["seal/specs/1780000009-x"])

    def test_accepts_a_history_git_cannot_read_as_a_spec_written(self, tmp_path):
        """*Never wrote one* is the answer that removes the directory."""
        assert UC.wrote_a_spec(str(tmp_path), None, "seal/specs/1780000009-x") is True

    def test_refuses_a_directory_that_never_wrote_one(self, settle):
        assert UC.wrote_a_spec(str(settle), None, f"specs/{CLOSED_ITEM}") is False


class Test_settled:
    def test_accepts_a_spec_less_item_and_one_whose_spec_states_no_rule(self, settle):
        dirs = [f"specs/{CLOSED_ITEM}", f"specs/{SETTLE_C}"]
        assert UC.settled(str(settle), "HEAD", dirs) == set(dirs)

    def test_accepts_an_item_whose_rule_the_policy_root_holds_here(
        self, settle, tmp_path
    ):
        d = copy_of(settle, tmp_path)
        write(d, "docs/a.md", DOC + "\nA new rule.\n")
        assert UC.settled(str(d), "HEAD", [f"specs/{SETTLE_A}"]) == {
            f"specs/{SETTLE_A}"
        }

    def test_refuses_an_open_row_a_dropped_spec_a_rule_not_held_and_an_unread_one(
        self, settle
    ):
        dirs = [
            f"specs/{n}"
            for n in (OPEN_ITEM, DROPPED, SETTLE_A, SETTLE_BAD, "1780000099-none")
        ]
        assert UC.settled(str(settle), "HEAD", dirs) == set()


class Test_settled_root:
    @pytest.mark.parametrize("state", ["absent", "empty", "a file only"])
    def test_accepts_a_roots_own_specs_with_no_work_item(self, tmp_path, state):
        (tmp_path / "seal").mkdir()
        if state != "absent":
            (tmp_path / "seal" / "specs").mkdir()
        if state == "a file only":
            write(tmp_path, "seal/specs/README.md", "r\n")
        assert UC.settled_root(str(tmp_path / "seal" / "specs")) is True

    @pytest.mark.parametrize("state", ["a work item", "another parent", "no root"])
    def test_refuses_a_work_item_another_parent_and_no_root(self, tmp_path, state):
        if state == "a work item":
            (tmp_path / "seal" / "specs" / WORK).mkdir(parents=True)
        if state == "another parent":
            (tmp_path / "other").mkdir()
        path = tmp_path / ("other" if state == "another parent" else "seal") / "specs"
        assert UC.settled_root(str(path)) is False


class Test_under_root:
    def test_accepts_a_slash_joined_path_as_the_disk_spells_it(self):
        assert UC.under_root("r", "specs/a/overview.md") == os.path.join(
            "r", "specs", "a", "overview.md"
        )

    def test_refuses_to_read_the_path_as_one_name(self):
        assert UC.under_root("r", "a/b") != os.path.join("r", "a" + chr(0) + "b")


class Test_annotate:
    def test_accepts_a_path_as_git_spells_it_in_ci_and_plain_elsewhere(
        self, monkeypatch
    ):
        monkeypatch.setenv("GITHUB_ACTIONS", "true")
        assert UC.annotate("error", "a/b.md", 3, "m") == "::error file=a/b.md,line=3::m"
        monkeypatch.delenv("GITHUB_ACTIONS")
        assert UC.annotate("error", "a/b.md", 3, "m") == "a/b.md:3  m"

    @pytest.mark.parametrize("in_ci, line", [(True, "::notice::m"), (False, "m")])
    def test_refuses_to_name_a_path_it_was_not_given(self, monkeypatch, in_ci, line):
        monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
        if in_ci:
            monkeypatch.setenv("GITHUB_ACTIONS", "true")
        assert UC.annotate("notice", None, 1, "m") == line


# --- the command ---------------------------------------------------------------


def reported_paths(out):
    """The path each report line names, in either output shape: `annotate`
    emits `::error file=<path>,line=<n>::...` in CI and `<path>:<line>  ...`
    anywhere else."""
    found = []
    for ln in out.split("\n"):
        if ln.startswith("::"):
            _, _, rest = ln.partition(" file=")
            path, _, _ = rest.partition(",line=")
            if path:
                found.append(path)
        elif "overview.md:" in ln:
            found.append(ln.split(":")[0])
    return found


class Test_main:
    # The plain run: what is open is reported, and a record that cannot be
    # read fails.

    def test_accepts_open_items_without_failing_the_run(self, tmp_path, capsys):
        """Never a red build for an honest row: punishing them teaches
        sessions to write none."""
        memo_at(tmp_path, CANONICAL)
        assert run([str(tmp_path)]) == 0
        out = capsys.readouterr().out
        assert "2 open" in out and "open: 0" not in out

    def test_accepts_every_item_closed_as_open_0(self, tmp_path, capsys):
        memo_at(tmp_path, "## Not verified\n\n- nothing\n  why: all executed.\n")
        assert run([str(tmp_path)]) == 0
        assert "open: 0" in capsys.readouterr().out

    def test_refuses_a_record_it_cannot_read_by_another_exit_and_other_words(
        self, tmp_path, capsys
    ):
        """A reader must never confuse "everything is closed" with "this
        could not be read", and a section that could not be read lists none
        of the rows it did read as open."""
        memo_at(tmp_path, CANONICAL + "| an item | an answerer | a third cell |\n")
        assert run([str(tmp_path)]) == 1
        out = capsys.readouterr().out
        assert "could not be read" in out and "open: 0" not in out
        assert "This is not a report of zero open items." in out
        assert "open  how the gate renders in a TUI" not in out, out

    @pytest.mark.parametrize("state", ["empty", "missing", "and a root"])
    def test_refuses_a_path_that_holds_no_overview(self, tmp_path, capsys, state):
        """Zero files and zero open items are different answers, and a path
        beside the root's settled `specs/` is still read."""
        (tmp_path / "empty").mkdir()
        argv = [str(tmp_path / "empty")]
        if state == "missing":
            argv = [str(tmp_path / "spces")]
        if state == "and a root":
            (tmp_path / "seal").mkdir()
            argv.append(str(tmp_path / "seal" / "specs"))
        assert run(argv) == 2
        err = capsys.readouterr().err
        assert ("no such path" if state == "missing" else "nothing was checked") in err

    def test_accepts_a_walk_outside_a_repository_reading_no_reference_root(
        self, tmp_path, monkeypatch
    ):
        """Outside a git repository there is no root to be outside of, and
        every fixture of the 0.3.x spelling lives there."""

        def refuse(top):
            raise AssertionError(f"reference roots were read for {top!r}")

        monkeypatch.setattr(UC, "references_at", refuse)
        memo_at(tmp_path, CANONICAL)
        assert run([str(tmp_path)]) == 0

    def test_accepts_the_baseline_help_naming_both_places(self, capsys):
        """#612: the `--baseline` help is a rendered line (contract rule
        14), and it names the fork point and the base's tip."""
        with pytest.raises(SystemExit):
            UC.main(["--help"])
        rendered = " ".join(capsys.readouterr().out.split())
        assert (
            "the fork point on a branch checkout and the base's tip in CI" in rendered
        )

    # `--baseline`: a row and a record leave by being closed.

    def test_accepts_a_closed_row_and_a_fenced_example_against_the_baseline(
        self, plain, tmp_path, capsys
    ):
        """Marking keeps the row, so the count does not fall; and the strict
        reader and the base reader agree about an example added."""
        d = copy_of(plain, tmp_path)
        path = d / "specs" / WORK / "overview.md"
        replace_in(path, "| whether Windows", "| closed whether Windows")
        replace_in(path, TUI + "\n", TUI + "\n\n```\nan example\n```\n\n")
        assert run([str(d), "--baseline", "HEAD"]) == 0
        out = capsys.readouterr().out
        assert "left the record" not in out and "not compared" not in out

    def test_accepts_an_overview_tracked_under_a_skipped_directory(self, plain):
        """The scan skips `build/`, and so does the base listing, or a
        tracked overview there reads as deleted on every run."""
        assert run([str(plain), "--baseline", "HEAD"]) == 0

    def test_refuses_a_deleted_row(self, plain, tmp_path, capsys):
        """Without it the cheapest way to lower the count stays "delete the
        line", and a closed item and a tidied-up one become one edit."""
        d = copy_of(plain, tmp_path)
        drop_line(d / "specs" / WORK / "overview.md", WINDOWS)
        assert run([str(d), "--baseline", "HEAD"]) == 1
        out = capsys.readouterr().out
        assert "2 rows at HEAD, 1 here" in out
        assert "Re-add the row, its Item cell opening with the word `closed`" in out

    @pytest.mark.parametrize(
        "change, argv, gone",
        [
            ("delete one and rename the other", ["."], 2),
            ("delete both", ["."], 2),
            ("delete specs", ["specs"], 2),
            ("delete the item", [f"specs/{WORK}/overview.md"], 1),
        ],
        ids=["a file and a rename", "every overview", "the scan path", "two levels"],
    )
    def test_refuses_a_record_that_left_whole(
        self, plain, tmp_path, capsys, change, argv, gone
    ):
        """Deleting the file was cheaper and quieter than deleting a row, and
        a rename reads the same way, said out loud. A scan that finds nothing
        because every overview left reports the deletion rather than an
        empty scan, and a scan path deleted wholesale is compared rather than
        called a bad argument, two levels gone too."""
        d = copy_of(plain, tmp_path)
        item = d / "specs" / WORK
        if change == "delete one and rename the other":
            os.remove(item / "overview.md")
            os.rename(d / "specs" / OTHER, d / "specs" / "1780000001-renamed")
        if change == "delete both":
            os.remove(item / "overview.md")
            os.remove(d / "specs" / OTHER / "overview.md")
        if change == "delete specs":
            shutil.rmtree(d / "specs")
        if change == "delete the item":
            shutil.rmtree(item)
        paths = [os.path.join(str(d), *a.split("/")) for a in argv]
        assert run([*paths, "--baseline", "HEAD"]) == 1
        assert capsys.readouterr().out.count("present at HEAD and not here") == gone

    def test_refuses_an_unreadable_section_without_reporting_a_deletion(
        self, plain, tmp_path, capsys
    ):
        """A misspelt heading returns zero rows, and comparing that zero told
        the author to restore rows still in the file."""
        d = copy_of(plain, tmp_path)
        replace_in(
            d / "specs" / WORK / "overview.md",
            "## Not verified",
            "## Not verified (who must answer)",
        )
        assert run([str(d), "--baseline", "HEAD"]) == 1
        out = capsys.readouterr().out
        assert "no `## Not verified` section" in out and "rows at HEAD" not in out

    @pytest.mark.parametrize("in_ci", [False, True])
    def test_refuses_both_deletions_naming_paths_on_one_footing(
        self, plain, tmp_path, capsys, monkeypatch, in_ci
    ):
        """One line came from `relpath(path, cwd)` and the other from
        `ls-tree`'s path; they agreed only at the repository root. Run in
        both output shapes, because pinning one is what let this pass
        everywhere except CI."""
        monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
        if in_ci:
            monkeypatch.setenv("GITHUB_ACTIONS", "true")
        d = copy_of(plain, tmp_path)
        os.remove(d / "specs" / WORK / "overview.md")
        drop_line(d / "specs" / OTHER / "overview.md", WINDOWS)
        monkeypatch.chdir(d / "specs")
        assert run([".", "--baseline", "HEAD"]) == 1
        paths = reported_paths(capsys.readouterr().out)
        assert len(paths) == 2 and all(q.startswith("1780000") for q in paths), paths

    @pytest.mark.parametrize(
        "argv, says",
        [
            (["specs", "spces"], "nothing under it at HEAD either"),
            (["spces"], "nothing under it at HEAD either"),
        ],
        ids=["beside a real path", "alone"],
    )
    def test_refuses_a_mistyped_path_under_the_baseline(
        self, plain, capsys, argv, says
    ):
        """A path with nothing under it at the base is a typo, not a
        question, which keeps `specs/ spces/` from passing in silence."""
        paths = [os.path.join(str(plain), a) for a in argv]
        assert run([*paths, "--baseline", "HEAD"]) == 2
        assert says in capsys.readouterr().err

    def test_refuses_a_ref_that_does_not_resolve(self, plain, capsys):
        """In CI the base branch is one shallow checkout away, and every file
        then reads as new."""
        assert run([str(plain), "--baseline", "origin/nosuchbranch"]) == 2
        assert "does not resolve" in capsys.readouterr().err

    def test_refuses_a_baseline_outside_a_repository(self, tmp_path, capsys):
        memo_at(tmp_path, CANONICAL)
        assert run([str(tmp_path), "--baseline", "HEAD"]) == 2
        assert "needs a git repository" in capsys.readouterr().err

    def test_refuses_a_path_on_another_volume_instead_of_aborting(
        self, plain, tmp_path, monkeypatch, capsys
    ):
        """Every argument is read against the repository the first is in,
        and a path with no relative form to it is exit 2, named. The raise is
        induced, so every leg runs this."""
        elsewhere = tmp_path / "elsewhere"
        (elsewhere / "specs").mkdir(parents=True)
        real_relpath = os.path.relpath

        def refuses_for_elsewhere(path, start=None):
            if "elsewhere" in str(path):
                raise ValueError("path is on mount 'D:', start on mount 'C:'")
            return real_relpath(path, start)

        monkeypatch.setattr(os.path, "relpath", refuses_for_elsewhere)
        assert run([str(plain), str(elsewhere), "--baseline", "HEAD"]) == 2
        err = capsys.readouterr().err
        assert "is not in" in err and "another volume" in err, err

    def test_accepts_a_tracked_link_counted_once_and_not_deleted(self, linked, capsys):
        """One record, two paths: counting both doubles its open items, and
        dropping one from the presence check reports it deleted."""
        assert run([str(linked), "--baseline", "HEAD"]) == 0
        out = capsys.readouterr().out
        tally = [ln for ln in out.split("\n") if ln.startswith("1 overviews")]
        assert len(tally) == 1 and " 2 open " in tally[0], out

    @pytest.mark.parametrize("change", ["a row", "a file"])
    def test_refuses_a_deletion_reached_through_a_linked_path(
        self, plain, tmp_path, change
    ):
        """`git rev-parse --show-toplevel` answers with links resolved, so a
        tree reached through one matched no line of the listing and both
        comparisons passed."""
        d = copy_of(plain, tmp_path)
        symlink_or_skip(str(d), str(tmp_path / "link"))
        if change == "a row":
            drop_line(d / "specs" / WORK / "overview.md", WINDOWS)
        else:
            os.remove(d / "specs" / WORK / "overview.md")
        assert run([str(tmp_path / "link"), "--baseline", "HEAD"]) == 1

    # `--baseline` at a base written before the corpus was normalised.

    def test_accepts_a_base_written_before_the_word_and_names_one_it_cannot_read(
        self, legacy, tmp_path, capsys
    ):
        """A base revision written before this normalisation is still a
        countable record: the old heading and column, the old mark, the old
        `none` line, and a looser heading beside the canonical one, which
        wins. Read as a refusal, every base before the word would go
        uncompared, and a row deleted against it would pass. A base no reader
        can read is not counted as zero and is no error either, since nobody
        can edit a commit: it is named, and the tally counts it."""
        d = copy_of(legacy, tmp_path)
        trees = {
            "1780000020-old-heading": CANONICAL,
            "1780000021-old-mark": CANONICAL.replace("| whether", "| closed whether"),
            "1780000022-prose": CANONICAL,
            "1780000024-hidden-separator": CANONICAL,
            "1780000025-none-line": "## Not verified\n\n- nothing\n  why: x\n",
        }
        for name, tree in trees.items():
            write(d, f"specs/{name}/overview.md", memo(tree, name))
        assert run([str(d / "specs"), "--baseline", "HEAD"]) == 0
        out = capsys.readouterr().out
        named = out.split("not compared against HEAD:")[1]
        assert [n for n in LEGACY if n in named] == [
            "1780000022-prose",
            "1780000024-hidden-separator",
        ], out
        assert "found prose" in named and "2 not compared" in out

    def test_refuses_a_row_deleted_against_a_base_written_before_the_word(
        self, legacy, tmp_path, capsys
    ):
        """The base is compared, so a row deleted against it fails, and the
        working tree is held to the exact header and the word."""
        d = copy_of(legacy, tmp_path)
        names = ["1780000020-old-heading", "1780000021-old-mark"]
        for name in names:
            tree = memo(CANONICAL.replace(WINDOWS + "\n", ""), name)
            write(d, f"specs/{name}/overview.md", tree)
        assert run([str(d / "specs" / n) for n in names] + ["--baseline", "HEAD"]) == 1
        assert capsys.readouterr().out.count("2 rows at HEAD, 1 here") == 2
        for name in names:
            tree = memo(LEGACY[name].replace(" (who must answer)", ""))
            assert UC.check_text(tree)[2], name

    # `--baseline` against a base that moved after the fork (#272).

    @pytest.mark.parametrize("ref", ["base", "gained"])
    @pytest.mark.rule("one-merge-base")
    def test_a_work_item_squashed_after_the_fork_is_not_this_branchs_removal(
        self, forked, capsys, ref
    ):
        """A file or a row that arrived on the base after the fork is not
        this branch's business. The merge base is the last commit this
        branch and the base agreed on, so a file present there and absent
        here was removed by this branch; on 0.9.2 three of four branches read
        a squashed sibling's overview as rows that left the record."""
        assert run([str(forked), "--baseline", ref]) == 0
        out = capsys.readouterr().out
        assert "left the record" not in out and "squashed-sibling" not in out, out

    def test_refuses_this_branchs_own_deletion_under_a_moved_base(
        self, forked, tmp_path, capsys
    ):
        """The control: a moved base excuses nothing this branch did, and
        the refusal names the merge base it compared, not the ref."""
        d = copy_of(forked, tmp_path)
        os.remove(d / "specs" / WORK / "overview.md")
        assert run([str(d), "--baseline", "base"]) == 1
        out = capsys.readouterr().out
        short = git_out(d, "rev-parse", "HEAD")[:7]
        assert (
            f"present at the merge-base of base and HEAD ({short}) and not here" in out
        )
        assert "squashed-sibling" not in out, out

    def test_refuses_a_deleted_row_under_a_moved_base(self, forked, tmp_path, capsys):
        d = copy_of(forked, tmp_path)
        drop_line(d / "specs" / WORK / "overview.md", WINDOWS)
        assert run([str(d), "--baseline", "base"]) == 1
        assert "2 rows at the merge-base of base and HEAD" in capsys.readouterr().out

    def test_refuses_a_deletion_naming_a_ref_that_is_the_merge_base_alone(
        self, forked, tmp_path, capsys
    ):
        d = copy_of(forked, tmp_path)
        os.remove(d / "specs" / WORK / "overview.md")
        assert run([str(d), "--baseline", "fork"]) == 1
        out = capsys.readouterr().out
        assert "present at fork and not here" in out and "merge-base" not in out

    def test_refuses_a_base_with_no_history_and_a_path_only_its_tip_holds(
        self, forked, capsys
    ):
        """A comparison against nothing is not a comparison, and a path the
        fork point never held is a mistyped argument from this branch,
        whatever the base's tip carries now."""
        assert run([str(forked), "--baseline", "unrelated"]) == 2
        err = capsys.readouterr().err
        assert "share no history" in err and "nothing was compared" in err, err
        assert run([str(forked / "specs" / SIBLING), "--baseline", "base"]) == 2
        assert "no such path" in capsys.readouterr().err

    @pytest.mark.parametrize(
        "word, says",
        [("merge-base", "share no history"), ("--verify", "does not resolve")],
    )
    def test_refuses_a_git_that_answers_with_nothing(
        self, forked, monkeypatch, capsys, word, says
    ):
        """An empty answer is no revision, and an empty string reaching the
        listing lists nothing: the silent zero, reached through the one path
        no fixture drives."""
        answering(monkeypatch, word, "\n")
        assert run([str(forked), "--baseline", "base"]) == 2
        assert says in capsys.readouterr().err

    # `--baseline` and a settle, which removes a directory whole.

    @pytest.mark.rule("a-settle-is-no-deletion")
    def test_a_settled_work_item_is_not_read_as_this_branchs_deletion(
        self, settle, tmp_path, capsys
    ):
        """A released directory removed whole, with nothing open, whose rule
        changes `docs/` holds, that states none, or that never wrote a spec,
        is a settle and not this branch's deletion (S9 and S11 of the settle
        work, A6 of #517). It is named rather than passed over in silence, in
        the line a person reads in the hygiene workflow's output."""
        d = copy_of(settle, tmp_path)
        removed = [SETTLE_A, SETTLE_C, CLOSED_ITEM]
        for name in removed:
            shutil.rmtree(d / "specs" / name)
        write(d, "docs/a.md", DOC + "\nA new rule.\n")
        assert run([str(d), "--baseline", "HEAD"]) == 0
        out = capsys.readouterr().out
        assert "present at HEAD and not here" not in out, out
        named = out.split("not deleted from the record:")[1]
        assert "3 settled" in out and all(n in named for n in removed), out
        assert (
            "settled: at HEAD nothing in its record was open, and `docs/` holds "
            "every rule change its spec states"
        ) in " ".join(out.split())
        # A path whose every overview a settle removed reads no overview and
        # is still no empty scan.
        assert run([str(d / "specs" / SETTLE_C), "--baseline", "HEAD"]) == 0

    @pytest.mark.rule("a-settle-is-no-deletion")
    def test_a_removal_whose_rule_docs_does_not_hold_still_fails(
        self, settle, tmp_path, capsys
    ):
        """S10: two directories leave together, and `docs/` holds one of
        their rules."""
        d = copy_of(settle, tmp_path)
        shutil.rmtree(d / "specs" / SETTLE_A)
        shutil.rmtree(d / "specs" / SETTLE_B)
        write(d, "docs/a.md", DOC + "\nA new rule.\n")
        assert run([str(d), "--baseline", "HEAD"]) == 1
        deleted = capsys.readouterr().out.split("rows left the record")[1]
        assert SETTLE_B in deleted and SETTLE_A not in deleted

    def test_refuses_a_removal_no_settle_explains(self, settle, tmp_path, capsys):
        """An open row at the base, a spec an earlier merge deleted, and a
        memo deleted from a directory that stays are deletions whatever the
        predicate would say, and each is named."""
        d = copy_of(settle, tmp_path)
        shutil.rmtree(d / "specs" / OPEN_ITEM)
        shutil.rmtree(d / "specs" / DROPPED)
        os.remove(d / "specs" / CLOSED_ITEM / "overview.md")
        assert run([str(d), "--baseline", "HEAD"]) == 1
        out = capsys.readouterr().out
        lines = [ln for ln in out.split("\n") if "present at HEAD and not here" in ln]
        for name in (OPEN_ITEM, DROPPED, CLOSED_ITEM):
            assert sum(name in ln for ln in lines) == 1, (name, out)
        assert "settled" not in out, out

    def test_refuses_to_decide_a_removal_without_the_one_predicate(
        self, settle, tmp_path, monkeypatch
    ):
        """The reader calls `settled` rather than re-deriving it, so the next
        condition added to the predicate reaches this reader too."""
        d = copy_of(settle, tmp_path)
        shutil.rmtree(d / "specs" / CLOSED_ITEM)
        asked = []
        monkeypatch.setattr(
            UC,
            "settled",
            lambda root, ref, dirs, here=None: asked.extend(dirs) or set(),
        )
        assert run([str(d), "--baseline", "HEAD"]) == 1
        assert asked == [f"specs/{CLOSED_ITEM}"], asked

    @pytest.mark.rule("an-empty-root-is-settled")
    @pytest.mark.parametrize("keep_empty_dir", [True, False], ids=["empty", "absent"])
    @pytest.mark.parametrize("baseline", [True, False], ids=["baseline", "plain"])
    def test_the_roots_own_specs_path_is_settled_when_nothing_is_under_it(
        self, sealed, tmp_path, capsys, keep_empty_dir, baseline
    ):
        """G7: every pull request after a complete fold runs
        `--baseline origin/<base> seal/specs/`, and the path holds nothing at
        HEAD and held no overview at the merge base. That was a typo, exit 2,
        so every such pull request went red."""
        d = sealed
        if keep_empty_dir:
            d = copy_of(sealed, tmp_path)
            (d / "seal" / "specs").mkdir()
        argv = [str(d / "seal" / "specs")] + (
            ["--baseline", "HEAD"] if baseline else []
        )
        assert run(argv) == 0
        out = capsys.readouterr()
        assert "holds no work item" in out.out + out.err, out

    @pytest.mark.parametrize("baseline", [True, False], ids=["baseline", "plain"])
    def test_refuses_any_other_missing_path_as_a_typo(self, sealed, capsys, baseline):
        argv = [str(sealed / "seal" / "spces")] + (
            ["--baseline", "HEAD"] if baseline else []
        )
        assert run(argv) == 2
        assert "no such path" in capsys.readouterr().err

    # A team's own `specs/` is read as history and never checked (#688).

    def test_accepts_a_walk_from_the_root_leaving_a_team_specs_out(
        self, joined, tmp_path, capsys
    ):
        """D2: the team's unreadable overview fails nothing, and a team
        removing its own overview is not a record this branch deleted."""
        assert run([str(joined)]) == 0
        out = capsys.readouterr().out
        assert "1790000000-ours" in out and "team-thing" not in out, out
        d = copy_of(joined, tmp_path)
        os.remove(d / TEAM / "overview.md")
        assert run([str(d), "--baseline", "HEAD"]) == 0

    def test_refuses_a_team_overview_the_person_names(self, joined, tmp_path, capsys):
        """A person who names the file, or the directory it sits in, has
        asked for it, on both sides of the comparison."""
        assert run([str(joined / TEAM / "overview.md")]) == 1
        assert run([str(joined / "specs")]) == 1
        d = copy_of(joined, tmp_path)
        os.remove(d / TEAM / "overview.md")
        capsys.readouterr()
        assert run([str(d / "specs"), "--baseline", "HEAD"]) == 1
        assert "team-thing" in capsys.readouterr().out

    def test_refuses_nothing_less_in_a_copy_with_no_hooks_beside_it(
        self, joined, tmp_path, monkeypatch
    ):
        """A copy taken alone reads every overview, as it did before
        reference roots existed, the walk and the base alike."""
        monkeypatch.setattr(UC, "HOOKS", str(tmp_path / "no-hooks-here"))
        assert run([str(joined)]) == 1
        assert run([str(joined), "--baseline", "HEAD"]) == 1


class Test_module:
    def test_the_fence_rule_and_the_line_split_are_the_hooks(self):
        """S12 of #1005: the fence delimiter rule and the line split are
        written once, in `hooks/blocks.py`, and this module asks that copy."""
        blocks = os.path.join(ROOT, "hooks", "blocks.py")
        for name in ("fence_opener", "fence_closes", "gfm_lines"):
            code = getattr(UC, name).__code__
            assert os.path.samefile(code.co_filename, blocks), (name, code.co_filename)
        with open(UC.__file__, encoding="utf-8") as handle:
            source = handle.read()
        for defined in ("def fence_opener(", "def fence_closes(", "def gfm_lines("):
            assert defined not in source, defined
        assert "GFM_LINE_RE = re.compile" not in source

    def test_the_wrapper_is_present_and_executable(self):
        """`bin/` lands on the Bash tool's PATH while the plugin is enabled,
        so the wrapper resolves the script relative to itself and a .cmd
        sibling ships for the platform that cannot run a POSIX shebang."""
        posix = os.path.join(ROOT, "bin", "unverified-check")
        windows = os.path.join(ROOT, "bin", "unverified-check.cmd")
        assert os.path.isfile(posix), "bin/unverified-check missing"
        assert os.path.isfile(windows), "bin/unverified-check.cmd missing"
        assert os.access(posix, os.X_OK), "bin/unverified-check not executable"
        assert os.path.isfile(UC.__file__), "the wrapper points at a missing script"

    def test_this_repositorys_own_overviews_are_all_readable(self):
        """The corpus is the real test, and it states the rule for new work:
        a work item that writes an overview writes this section in it."""
        assert run([os.path.join(ROOT, "seal", "specs")]) == 0

    def test_a_planted_team_specs_changes_no_checks_verdict(self, tmp_path):
        """#688's D3. This command run over the repository with and without a
        team's `specs/` exits the same and prints the same, with the
        repository's own path written out of both; and the team's directory
        is on disk, untouched, after it ran. `tests/conftest.py#planted`
        builds the two repositories, and `tests/test_chain_check.py` and
        `tests/test_settle.py` run their commands over them."""
        name, script = TARGET, TARGET
        args = ["{r}"]
        alone = planted(tmp_path / "alone", team=False)
        joined = planted(tmp_path / "joined", team=True)
        before = {
            rel: (joined / TEAM / rel).read_bytes()
            for rel in ("spec.md", "overview.md", "design.md")
        }
        said = []
        for repo in (alone, joined):
            r = subprocess.run(
                [sys.executable, os.path.join(ROOT, script)]
                + [a.replace("{r}", str(repo)) for a in args],
                cwd=str(repo),
                capture_output=True,
                encoding="utf-8",
                errors="replace",
            )
            # The two repositories' paths and commits differ by construction.
            text = re.sub(
                r"\b[0-9a-f]{7,40}\b",
                "<sha>",
                (r.stdout + r.stderr).replace(str(repo), "<repo>"),
            )
            said.append((r.returncode, text))
        assert said[0] == said[1], (
            f"{name} says something else once a team's specs/ is planted:\n"
            f"alone:\n{said[0]}\njoined:\n{said[1]}"
        )
        assert "team-thing" not in said[1][1], f"{name} read the team's specs/"
        for rel, data in before.items():
            assert (joined / TEAM / rel).read_bytes() == data, rel


# --- a reading written from the format, for `Test_live_lines` -----------------


def a_reading_from_the_commonmark_rules(lines):
    """A reference reading of a markdown document, written from the format.

    Nothing here is named after, or copied from, a choice `live_lines` made —
    that was round 5's finding 2, where this function's block rule was the
    reader's own and the case built on it could not report the reader being
    wrong. Every rule below cites the specification it comes from, so a
    disagreement is settled by reading the spec rather than by reading the
    module under test.

    - **Fenced code blocks** (CommonMark 4.5): a line whose first non-space
      run is three or more backticks or tildes opens one, unless a backtick
      run's info string holds a backtick; a line whose run is the same
      character and at least as long, with nothing after it but spaces,
      closes it. Nothing inside is parsed. The two info-string clauses
      arrived with #491: before them this reading closed a block on
      ```` ```python ```` and opened one on ```` ```x` ````, which the format
      does neither of.
    - **HTML comments** (CommonMark 6.6, raw HTML): `<!--` opens and the next
      `-->` closes, and between them the document is not markdown at all, so
      backticks are ordinary characters.
    - **Code spans** (CommonMark 6.1): a backtick string is closed by the
      next backtick string of equal length; one with no partner is literal
      text. A code span is inline content of a leaf block, so its partner
      must lie in the same block.
    - **Where a block ends** (CommonMark 4.1, 4.2, 4.3, 4.5, 4.8, 5.1, 5.2
      and GFM 4.10): a blank line, a thematic break, an ATX heading, a fence
      delimiter, a block quote marker, a list item marker, a setext
      underline, or a table row. **A richer list is a WEAKER case, not a
      safer one**, and the sentence here used to claim the opposite. Every
      extra stop shortens `partner_in_this_block`, which makes this reading
      see fewer spans, which makes it call MORE lines live — and the only
      violation this case can report is the scan live where this reading
      parks. So each rule is the format's rule and no other, and the two
      indentation bounds below are where that stopped being true (round 6,
      finding 2).

    A line is live when it begins outside all three.
    """

    def block_ends_at(line):
        indent = len(line) - len(line.lstrip(" "))
        s = line.strip()
        if not s:
            return True
        if s.startswith("|") or s.startswith(">"):
            return True
        if indent <= 3 and s.startswith("#"):
            # CommonMark 4.2: one to six hashes, then a space, a tab or the
            # end of the line. The guard this replaces read
            # `s.lstrip("#").startswith((" ", ""))`, and `str.startswith("")`
            # is true of every string, so it asserted nothing.
            n = len(s) - len(s.lstrip("#"))
            if 1 <= n <= 6 and (len(s) == n or s[n] in " \t"):
                return True
        if set(s) == {"="}:
            return True
        # Only an opener interrupts a paragraph (CommonMark 4.5), and `opens`
        # below is this reading's opener rule, bound and info string included.
        if opens(line) is not None:
            return True
        if len(s) >= 3 and s[0] in "*-_" and set(s.replace(" ", "")) == {s[0]}:
            return True
        if s[:2] in ("- ", "* ", "+ "):
            return True
        return s[:2] in ("1.", "1)") and len(s) > 2 and s[2] in " \t"

    def runs(text, at):
        n = 0
        while at + n < len(text) and text[at + n] == "`":
            n += 1
        return n

    def partner_in_this_block(start_line, start_at, width):
        # Every line reached here is a LATER line than the run's own, so each
        # one is checked: a block that ends on the first of them ends the
        # paragraph the run was opened in.
        for i in range(start_line, len(lines)):
            if block_ends_at(lines[i]):
                return False
            text = lines[i]
            j = start_at if i == start_line else 0
            while j < len(text):
                if text[j] == "`":
                    n = runs(text, j)
                    if n == width:
                        return True
                    j += n
                else:
                    j += 1
        return False

    def fence_of(line):
        # CommonMark 4.5 bounds an opening fence to three spaces. Stripping
        # the line first was the one rule this reading still took from
        # `live_lines`, and while it did, this case agreed with the scan on
        # the very shape that removed a directory (round 6, finding 2).
        # Returns (the run, what follows it), and the two info-string
        # clauses are asked by the caller, because one is an opener's and
        # the other a closer's.
        if len(line) - len(line.lstrip(" ")) > 3:
            return None
        s = line.strip()
        if len(s) < 3 or s[0] not in "`~":
            return None
        n = runs(s, 0) if s[0] == "`" else len(s) - len(s.lstrip("~"))
        return (s[0] * n, s[n:]) if n >= 3 else None

    def opens(line):
        found = fence_of(line)
        if found is None or (found[0][0] == "`" and "`" in found[1]):
            return None
        return found[0]

    def closes(line, run):
        found = fence_of(line)
        return (
            found is not None
            and found[0][0] == run[0]
            and len(found[0]) >= len(run)
            and not found[1].strip()
        )

    fence = None
    in_comment = False
    open_span = None
    verdict = []
    for n, line in enumerate(lines):
        verdict.append(fence is None and not in_comment and open_span is None)
        if fence is not None:
            if closes(line, fence):
                fence = None
            continue
        if not in_comment and open_span is None and opens(line) is not None:
            fence = opens(line)
            continue
        i = 0
        while i < len(line):
            if in_comment:
                if line.startswith("-->", i):
                    in_comment, i = False, i + 3
                else:
                    i += 1
            elif open_span is not None:
                width = runs(line, i)
                if width == open_span:
                    open_span, i = None, i + width
                else:
                    i += width if width else 1
            elif line.startswith("<!--", i):
                in_comment, i = True, i + 4
            elif line[i] == "`":
                width = runs(line, i)
                j, closed = i + width, None
                while j < len(line):
                    here = runs(line, j)
                    if here == width:
                        closed = j + here
                        break
                    j += here if here else 1
                if closed is not None:
                    i = closed
                elif partner_in_this_block(n + 1, 0, width):
                    open_span, i = width, len(line)
                else:
                    i += width
            else:
                i += 1
    return verdict


def documents_with_several_spans_on_a_line(count, seed=20260922):
    """Documents whose lines can carry several code spans, unclosed backtick
    runs, and the block starts a span could be asked to reach past.

    The generator is half of what a fuzz is worth. With at most one span per
    line every formulation of this rule scored zero, and round 5's defect
    needs an unclosed run, a block start on a later line and the run's
    partner after it — so the tokens below include the delimiters, backtick
    runs of two lengths, a table row, a heading, a bullet and a fence.
    """
    rng = random.Random(seed)
    tokens = [
        "<!--",
        "-->",
        "`",
        "``",
        "text",
        " ",
        "<!-- specs/a -->",
        "| row |",
        "```",
        "# head",
        "- item",
        "> quote",
        # The shapes a paragraph rule can be WRONG about, without which the
        # case cannot report the class it is written for. Reverting any of
        # the three paragraph corrections reddened nothing until these
        # arrived (round 6, findings 3 and 4): a hash with no space and seven
        # hashes are paragraph text, an ordered marker that is not 1 does not
        # interrupt a paragraph, a run of `=` is a setext underline, and four
        # spaces before a delimiter is an indented code block.
        "#nospace",
        "####### seven",
        "3. item",
        "===",
        "    ```",
    ]

    def line():
        # One token alone some of the time. A setext underline and an
        # indented delimiter are only themselves when nothing follows them on
        # the line, and while every line was a join of several tokens the
        # case could not see either (round 6, findings 1 and 3).
        if rng.random() < 0.25:
            return rng.choice(tokens)
        return "".join(rng.choice(tokens) for _ in range(rng.randint(1, 8)))

    return [[line() for _ in range(rng.randint(1, 7))] for _ in range(count)]


test_census = census_case(TARGET)
