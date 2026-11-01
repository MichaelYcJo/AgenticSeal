"""`skills/verify/scripts/unverified_check.py`, one class per function.

Rebuilt by #942's phase 5 from `tests/behaviour/test_unverified_rows_close.py`. The
script reads every `## Not verified` section, reports what is still open,
fails on a section it cannot read, and under `--baseline` fails on a row or
a record that left since the merge base, unless a settle removed it.

The readers of markdown, of a section and of a row run in the process on
lines and texts, with no git. The units that ask git, and `main` under
`--baseline`, read repositories built once for the module: a clone of two
work items and a tracked overview under `build/`, a clone whose second
overview is a tracked link to the first, built once with the link sorting
after its target and once before it, a clone whose base
revisions are written the way the corpus was before it was normalised, a
clone with a moved base branch beside its work branch, a clone of work items
a settle can remove, a clone with a `seal/` root beside a team's own `specs/`, a
`seal/` root with no `specs/`, and a `seal/` root whose one work item holds
no overview. A case that writes into a world takes a copy,
and the copy is the reset. No world holds a file a case runs, so the copies
are plain copies.
"""

import os
import random
import re
import shutil
import subprocess
import time

import pytest
from commonmark_oracle import heading_lines, hidden_text
from conftest import (
    ROOT,
    census_case,
    commit_everything_as_e,
    git,
    git_out,
    load_module,
    mark_root,
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
    """The path of `specs/<name>/gaps.md` under ROOT, written as
    `memo(section)`."""
    write(root, f"specs/{name}/gaps.md", memo(section, name))
    return os.path.join(str(root), "specs", name, "gaps.md")


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
    commit; a `seal/` among them is made a root."""
    d = base / "repo"
    d.mkdir()
    git(d, "init", "-q", "-b", "main")
    for rel, text in files.items():
        write(d, rel, text)
    if (d / "seal").is_dir():
        mark_root(d / "seal")
    commit_everything_as_e(d, "the base")
    return d


@pytest.fixture(scope="module")
def plain(tmp_path_factory):
    """Two work items in the 0.3.x spelling, `specs/<id>/`, and an overview
    tracked under `build/`, which every walk skips."""
    return _committed(
        tmp_path_factory.mktemp("plain"),
        {
            f"specs/{WORK}/gaps.md": memo(CANONICAL),
            f"specs/{OTHER}/gaps.md": memo(CANONICAL, OTHER),
            "build/x/gaps.md": memo(CANONICAL, "x"),
        },
    )


@pytest.fixture(
    scope="module",
    params=[OTHER, "1779999999-link"],
    ids=["the link sorts after its target", "the link sorts before its target"],
)
def linked(tmp_path_factory, request):
    """One work item and a second whose overview is a tracked link to the
    first's, the second's directory sorting after the first's or before it.
    #19 stood only where the link sorted first."""
    d = _committed(
        tmp_path_factory.mktemp("linked"),
        {f"specs/{WORK}/gaps.md": memo(CANONICAL)},
    )
    (d / "specs" / request.param).mkdir()
    symlink_or_skip(
        os.path.join("..", WORK, "gaps.md"),
        str(d / "specs" / request.param / "gaps.md"),
    )
    commit_everything_as_e(d, "a link")
    return d


def link_of(world):
    """The work item of WORLD, a `linked` repository, whose overview is the
    link."""
    (name,) = [n for n in os.listdir(world / "specs") if n != WORK]
    return name


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
        {f"specs/{name}/gaps.md": memo(s, name) for name, s in LEGACY.items()},
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
        {f"specs/{WORK}/gaps.md": memo(CANONICAL)},
    )
    git(d, "branch", "fork")
    git(d, "switch", "-qc", "base")
    write(d, f"specs/{SIBLING}/gaps.md", memo(CANONICAL, SIBLING))
    commit_everything_as_e(d, "another work item, squashed into the base")
    git(d, "switch", "-qc", "gained", "fork")
    write(
        d,
        f"specs/{WORK}/gaps.md",
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
        files[f"specs/{name}/gaps.md"] = memo(CLOSED_SECTION, name)
        files[f"specs/{name}/design.md"] = spec
    for name, section in (
        (CLOSED_ITEM, CLOSED_SECTION),
        (OPEN_ITEM, CANONICAL),
        (DROPPED, CLOSED_SECTION),
    ):
        files[f"specs/{name}/routing.md"] = f"# {name} routing\n"
        files[f"specs/{name}/gaps.md"] = memo(section, name)
    files[f"specs/{DROPPED}/design.md"] = "# a spec\n\nA rule.\n"
    d = _committed(tmp_path_factory.mktemp("settle"), files)
    git(d, "rm", "-q", f"specs/{DROPPED}/design.md")
    commit_everything_as_e(d, "an earlier pull request drops it")
    return d


TEAM = "specs/1788000001-team-thing"
OURS = "seal/threads/1790000000-ours"
MALFORMED = "## Not verified\n\nnot a table, and not a none line either\n"


@pytest.fixture(scope="module")
def joined(tmp_path_factory):
    """A `seal/` root holding one readable work item, and a team's own
    `specs/` whose overview the reader cannot read."""
    return _committed(
        tmp_path_factory.mktemp("joined"),
        {
            f"{OURS}/gaps.md": memo(CANONICAL, "ours"),
            f"{TEAM}/gaps.md": memo(MALFORMED, "team"),
            # exempt from old_names: another tool's own file, under a name the plugin once used
            f"{TEAM}/spec.md": "# the team's spec\n",
        },
    )


@pytest.fixture(scope="module")
def sealed(tmp_path_factory):
    """A `seal/` root with no `specs/`, the tree a complete settle leaves."""
    return _committed(tmp_path_factory.mktemp("sealed"), {"seal/ledger.md": "# l\n"})


@pytest.fixture(scope="module")
def unwritten(tmp_path_factory):
    """A `seal/` root whose one work item has a routing and a spec and never
    opened a closing memo."""
    return _committed(
        tmp_path_factory.mktemp("unwritten"),
        {
            f"seal/threads/{WORK}/routing.md": f"# {WORK} routing\n",
            f"seal/threads/{WORK}/frame/design.md": "# a spec\n",
        },
    )


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


class Test_comment_lines:
    def test_accepts_each_line_that_begins_with_the_opener(self):
        """*Scope* item 3 of #1012: a record carries no HTML comment, so a
        line whose text, leading whitespace removed, begins with `<!--` is
        found at its own index, for the reader of the record to refuse."""
        lines = UC.readable("# r\n\n<!-- a note -->\n  <!-- indented\nprose\n")
        assert UC.comment_lines(lines) == [2, 3]

    def test_refuses_an_opener_later_in_a_line_or_inside_a_fence(self):
        """A `<!--` after the start of a line is text, in a code span or not,
        and one inside a fence is part of a quotation `readable` blanks."""
        text = "a `<!--` b\nprose <!-- open\n```\n<!-- quoted\n```\n"
        assert UC.comment_lines(UC.readable(text)) == []


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

    def test_reads_an_opener_as_text_where_the_caller_keeps_no_comment_state(self):
        """#1012: `rule_changes.py#parse` reads a record with `comments=False`,
        so an opener opens nothing and a fence after it is a fence."""
        lines = ["<!-- open", "```", "-->", "```", "after"]
        assert UC.liveness(lines, spans_cross_lines=False, comments=False) == [
            True,
            True,
            False,
            False,
            True,
        ]


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
    """The marker ids on the live lines of BODY, each read line-anchored, on
    a line of its own."""

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

    def test_reads_an_opener_as_text_where_the_caller_keeps_no_comment_state(self):
        """#1012: both readings take the keyword, so a heading after an
        opener nobody closed begins live for `rule_changes.py#parse`."""
        lines = ["prose <!-- open", "## Rule changes"]
        assert [live for _, live in UC.live_lines(lines, comments=False)] == [
            True,
            True,
        ]
        assert [live for _, live in UC.live_lines(lines)] == [True, False]

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
    def test_accepts_the_lines_with_fences_blanked_and_a_comment_as_text(self):
        """#1012: a record carries no comment, so `readable` keeps none of
        the comment state and a comment comes back as the text it is."""
        text = "a\n<!-- b -->\n```\n| x | y |\n```\n| c | d |\n"
        assert UC.readable(text) == ["a", "<!-- b -->", "", "", "", "| c | d |"]

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
            ([(3, "none - x")], None),
        ],
        ids=["the block", "a table", "the old line"],
    )
    def test_accepts_the_block_and_passes_anything_else_on(self, body, answer):
        """#1167, *Scope* item 9: a line that opens like the block and is not
        it is passed on as any other line is, and its reader names it
        (`unread_block`). Seen red against its refusal here."""
        assert UC.nothing_block(body) == answer

    def test_refuses_a_second_item(self):
        body = [(3, "- nothing"), (4, "  why: x"), (5, "- nothing"), (6, "  why: y")]
        assert UC.nothing_block(body) == (
            None,
            (5, "`- nothing` is the section's one item"),
        )


class Test_unread_block:
    @pytest.mark.parametrize(
        "first", ["none - x", "None.", "- nothing - x", "-nothing", "* none"]
    )
    def test_refuses_a_first_line_that_opens_like_the_block_as_the_block(self, first):
        """The line is not taken as the block: it is named as read as prose.
        Refusing the section that holds it is its reader's act."""
        assert UC.unread_block([(3, first), (4, "more")]) == (
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
        assert UC.unread_block(body) is None


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
            # #1167, *Scope* item 9: the word is read exactly, so a row opening
            # with it in another case or with punctuation after it is open,
            # the safe direction. Seen red against the refusal of each.
            ("| closed. how the gate renders in a TUI | seen on screen |", None),
            ("| closed: how the gate renders in a TUI | seen on screen |", None),
            ("| Closed how the gate renders in a TUI | seen on screen |", None),
            ("| CLOSED how the gate renders in a TUI | seen on screen |", None),
        ],
        ids=[
            "the word",
            "the word and a tab",
            "an item that begins with it",
            "a word that begins with it",
            "a word that holds it",
            "an escaped pipe",
            "the word and a full stop",
            "the word and a colon",
            "capitalised",
            "upper case",
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
        ],
        ids=[
            "bare",
            "a zero-width space",
            "a selector",
            "a word joiner",
            "the old mark as a keyboard emits it",
            "the bare old mark",
        ],
    )
    def test_refuses_a_bare_word_and_the_old_mark(self, row, says):
        """T4 of `1792129100-the-mechanics-leave-before-the-agents-are-rewritten`:
        a bare word, and the emoji mark. Another spelling of the word is an
        open row (#1167), `test_accepts_open_rows_and_the_word_that_closes_one`."""
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
    def test_refuses_a_section_holding_the_old_line_and_names_the_line(self, first):
        """S2 of #1000 and #1167's *Scope* item 9: the old line and its near
        misses are not the block, so the section holds neither the table nor
        the block and is refused as unreadable at that line, and the refusal
        names the line as one it did not read, pinned whole (contract rule
        14). Seen red against the refusal naming the near miss as the
        block's."""
        section = f"## Not verified\n\n{first}\n"
        assert parse(section) == (
            [],
            [],
            [
                (
                    3,
                    "expected `| Item | Who must answer |`, found prose. Prose "
                    "belongs under `## Not done`; this section is read by a "
                    f"machine. Not read: `{first}` opens like {BLOCK} and is "
                    "not it, so it was read as prose",
                )
            ],
        )

    def test_names_no_line_that_does_not_open_like_the_block(self):
        """The naming is the prose refusal's only where the line opens like
        the block: other prose is refused without it."""
        section = "## Not verified\n\n- the TUI rendering, nobody has seen it\n"
        ((_line, says),) = parse(section)[2]
        assert says.endswith("this section is read by a machine"), says

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
        _, _, errors = UC.check_file(str(tmp_path / "gaps.md"))
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
            # Round 1 of #1000: a row quoting the opener in a code span hides
            # no row below it.
            (
                CANONICAL.replace(
                    "| how the gate renders in a TUI |",
                    "| whether `<!--` in a cell hides rows |",
                ),
                2,
            ),
            # #1012: a bare opener later in a line is text, so it hides no row
            # below it either.
            (
                CANONICAL.replace(
                    "| how the gate renders in a TUI |",
                    "| whether a bare <!-- in a cell hides rows |",
                ),
                2,
            ),
        ],
        ids=[
            "the table",
            "a fenced example",
            "a tilde fence",
            "an opener in a span",
            "a bare opener mid-line",
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

    @pytest.mark.rule("record-comment-line-refused")
    def test_refuses_a_comment_line_at_its_line(self):
        """S6 of #1012: the guidance comment an overview started before #1005
        carries is refused at its first line, before any row is counted,
        where the reader that kept a comment state read past it. The words
        are pinned here, once, because they are all a consuming repository
        is told to do (contract rule 14); every other case compares against
        the constant, which pins that each reader says the one message."""
        text = memo(
            "## Not verified\n\n<!-- guidance:\n| closed <item> | <what closed it> |"
            "\n-->\n\n" + CANONICAL.split("\n", 2)[2] + "<!-- a second -->\n"
        )
        line = text.splitlines().index("<!-- guidance:") + 1
        said = (
            "the line begins with `<!--`, and a record carries no HTML comment: "
            "the check reads one as text, so delete the comment"
        )
        assert UC.check_text(text) == ([], [], [(line, said)])


# --- the walk and the paths it compares ---------------------------------------


class Test_overviews:
    def test_accepts_every_overview_under_a_path_once_skipping_build_output(
        self, tmp_path
    ):
        for rel in ("specs/b", "specs/a", "build/c", "node_modules/d", ".venv/e"):
            write(tmp_path, f"{rel}/gaps.md", memo(CANONICAL))
        named = str(tmp_path / "specs" / "a" / "gaps.md")
        found = UC.overviews([str(tmp_path), named])
        here = os.path.realpath(str(tmp_path))
        assert found == [
            os.path.join(here, "specs", "a", "gaps.md"),
            os.path.join(here, "specs", "b", "gaps.md"),
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
        assert skip(str(joined / "seal" / "threads")) is False

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


class Test_repository_of:
    def test_accepts_the_repository_the_real_path_is_in_over_the_links(
        self, plain, tmp_path
    ):
        """A checkout linked from a directory that is itself a repository,
        such as a home directory, is compared in the checkout."""
        outer = tmp_path / "outer"
        outer.mkdir()
        git(outer, "init", "-q", "-b", "main")
        symlink_or_skip(str(plain), str(outer / "checkout"), directory=True)
        assert same_path(UC.repository_of(str(outer / "checkout" / "specs")), plain)

    def test_accepts_the_repository_holding_a_link_out_of_every_repository(
        self, plain, tmp_path
    ):
        """#1225: the real path is in no repository, and the link stands in
        one, so that one is where its own path is compared."""
        d = copy_of(plain, tmp_path)
        write(tmp_path, "beyond/gaps.md", memo(CANONICAL))
        symlink_or_skip(
            str(tmp_path / "beyond" / "gaps.md"), str(d / "specs" / WORK / "out.md")
        )
        assert same_path(UC.repository_of(str(d / "specs" / WORK / "out.md")), d)

    def test_accepts_a_parent_as_real_reads_it(self, plain, tmp_path):
        """A path that holds a `..` is compared in the repository `real`
        reads it in, on every platform. `ext` links into a second
        repository, so `ext/..` is the top of one of the two, whichever way
        the platform's `realpath` reads it; its text names the first."""
        d = copy_of(plain, tmp_path)
        second = tmp_path / "second"
        (second / "inner").mkdir(parents=True)
        git(second, "init", "-q", "-b", "main")
        symlink_or_skip(str(second / "inner"), str(d / "ext"), directory=True)
        given = str(d / "ext" / "..")
        assert same_path(UC.repository_of(given), os.path.realpath(given))


class Test_as_named:
    def test_accepts_a_link_inside_the_repository_under_its_own_name(
        self, plain, tmp_path
    ):
        """#1225: the components inside the repository are kept as the person
        named them, so a link among them is compared at its own path."""
        d = copy_of(plain, tmp_path)
        symlink_or_skip(WORK, str(d / "specs" / "named"), directory=True)
        given = os.path.join(str(d), "specs", "named", "gaps.md")
        assert UC.as_named(given) == os.path.join(
            os.path.realpath(str(d)), "specs", "named", "gaps.md"
        )

    def test_accepts_a_link_to_the_repositorys_top_resolved(self, plain, tmp_path):
        """git names the top with its links resolved, so the way to it is
        resolved too, or the path matches no line of `ls-tree`."""
        symlink_or_skip(str(plain), str(tmp_path / "link"), directory=True)
        assert UC.as_named(str(tmp_path / "link" / "specs")) == os.path.join(
            os.path.realpath(str(plain)), "specs"
        )

    def test_refuses_to_keep_a_name_outside_every_repository(self, tmp_path):
        (tmp_path / "target").mkdir()
        symlink_or_skip(str(tmp_path / "target"), str(tmp_path / "link"), True)
        assert UC.as_named(str(tmp_path / "link")) == os.path.realpath(
            str(tmp_path / "target")
        )

    def test_accepts_a_path_holding_a_parent_as_real_reads_it(self, plain, tmp_path):
        """A path that holds a `..` is its real path, on every platform, so
        `hop`, a link the `..` does not step out of, is resolved as well. By
        its text the path names `specs/hop/gaps.md`, and following only
        `jump`, the link the `..` steps out of, names `specs/hop/a/gaps.md`;
        a link the person named on such a path is #1240's."""
        d = copy_of(plain, tmp_path)
        (d / "specs" / WORK / "a" / "b").mkdir(parents=True)
        symlink_or_skip(WORK, str(d / "specs" / "hop"), True)
        symlink_or_skip(os.path.join("a", "b"), str(d / "specs" / WORK / "jump"), True)
        given = os.path.join(str(d), "specs", "hop", "jump", os.pardir, "gaps.md")
        assert UC.as_named(given) == os.path.realpath(given)


class Test_spellings:
    def test_accepts_each_spelling_from_as_named_to_the_real_path(
        self, plain, tmp_path
    ):
        """`view` is a link of this checkout to `specs`, and OTHER's memo a
        link to WORK's: the base may list the memo as named, with `view`
        resolved, or at its real path."""
        d = copy_of(plain, tmp_path)
        os.remove(d / "specs" / OTHER / "gaps.md")
        symlink_or_skip(
            os.path.join("..", WORK, "gaps.md"), str(d / "specs" / OTHER / "gaps.md")
        )
        symlink_or_skip("specs", str(d / "view"), directory=True)
        top = os.path.realpath(str(d))
        given = os.path.join(top, "view", OTHER, "gaps.md")
        assert UC.spellings(given, top) == [
            f"view/{OTHER}/gaps.md",
            f"specs/{OTHER}/gaps.md",
            f"specs/{WORK}/gaps.md",
        ]

    def test_refuses_a_second_spelling_where_no_link_stands(self, plain):
        top = os.path.realpath(str(plain))
        given = os.path.join(top, "specs", WORK, "gaps.md")
        assert UC.spellings(given, top) == [f"specs/{WORK}/gaps.md"]


class Test_git_path:
    def test_accepts_a_windows_path_as_git_spells_it(self, monkeypatch):
        r"""git answers and accepts `/` on every platform; `os.sep` is
        monkeypatched because `git_path` reads it at call time, so the
        Windows branch runs on every leg."""
        monkeypatch.setattr(os, "sep", "\\")
        assert UC.git_path("specs\\1780000000-work\\gaps.md") == (
            "specs/1780000000-work/gaps.md"
        )
        assert UC.git_path("specs/1780000000-work/gaps.md") == (
            "specs/1780000000-work/gaps.md"
        )

    def test_refuses_to_rewrite_a_backslash_in_a_posix_name(self, monkeypatch):
        monkeypatch.setattr(os, "sep", "/")
        assert UC.git_path("specs/odd\\name.md") == "specs/odd\\name.md"


def refuses(path, start=None):
    raise ValueError("path is on mount 'D:', start on mount 'C:'")


class Test_repo_relative:
    def test_accepts_a_path_inside_the_root(self, tmp_path):
        inside = os.path.join(str(tmp_path), "specs", "a", "gaps.md")
        assert UC.repo_relative(inside, str(tmp_path)) == "specs/a/gaps.md"

    def test_refuses_a_path_with_no_relative_form(self, monkeypatch):
        monkeypatch.setattr(os.path, "relpath", refuses)
        assert UC.repo_relative(os.path.abspath("x"), os.path.abspath("y")) is None


class Test_display_path:
    def test_accepts_a_path_relative_to_where_the_run_started(self, tmp_path):
        inside = os.path.join(str(tmp_path), "specs", "gaps.md")
        assert UC.display_path(inside, str(tmp_path)) == os.path.join(
            "specs", "gaps.md"
        )

    def test_refuses_to_die_on_a_path_with_no_relative_form(self, monkeypatch):
        """`relpath` raises on Windows across drives, and this is the footing
        for every line the tool prints; driven by making it raise, so every
        leg runs it."""
        monkeypatch.setattr(os.path, "relpath", refuses)
        where = os.path.join("x", "gaps.md")
        assert UC.display_path(where, os.path.abspath("y")) == os.path.abspath(where)


class Test_nearest_existing:
    def test_accepts_a_path_that_exists(self, tmp_path):
        assert UC.nearest_existing(str(tmp_path)) == os.path.abspath(str(tmp_path))

    def test_refuses_a_path_two_levels_gone_for_its_nearest_ancestor(self, tmp_path):
        gone = os.path.join(str(tmp_path), "a", "b", "gaps.md")
        assert UC.nearest_existing(gone) == os.path.abspath(str(tmp_path))


class Test_unique_by_target:
    def test_accepts_every_path_to_a_file_of_its_own(self, tmp_path):
        paths = [str(tmp_path / "a"), str(tmp_path / "b")]
        assert UC.unique_by_target(paths) == paths

    def test_refuses_a_second_path_to_one_file(self, tmp_path):
        p = str(tmp_path / "a")
        assert UC.unique_by_target([p, os.path.join(str(tmp_path), ".", "a")]) == [p]

    @pytest.mark.parametrize(
        "paths",
        [["a", "b"], ["a"]],
        ids=["the link sorting first", "the link alone"],
    )
    def test_accepts_the_real_files_own_path_wherever_the_link_sorts(
        self, tmp_path, paths
    ):
        """#19: the first path in sort order was kept, so a link sorting
        before its target had its own blob read at the base, and two deleted
        rows passed."""
        (tmp_path / "b").write_text("x", encoding="utf-8")
        symlink_or_skip("b", str(tmp_path / "a"))
        given = [str(tmp_path / p) for p in paths]
        assert UC.unique_by_target(given) == [os.path.realpath(tmp_path / "b")]


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
        assert same_path(UC.repo_root(str(plain / "specs" / WORK / "gaps.md")), plain)

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
        work, other = (f"specs/{n}/gaps.md" for n in (WORK, OTHER))
        assert UC.overviews_at(str(plain), "HEAD", ["."]) == [work, other]
        assert UC.overviews_at(str(plain), "HEAD", [f"specs/{WORK}"]) == [work]

    def test_accepts_a_reference_root_a_prefix_names(self, joined):
        assert UC.overviews_at(str(joined), "HEAD", ["."]) == [f"{OURS}/gaps.md"]
        assert UC.overviews_at(str(joined), "HEAD", ["specs"]) == [f"{TEAM}/gaps.md"]

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
        listed = [f"specs/{SETTLE_A}/design.md", f"specs/{SETTLE_A}/gaps.md"]
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
        assert UC.show(str(plain), "HEAD", f"specs/{WORK}/gaps.md") == memo(CANONICAL)

    def test_refuses_a_path_the_ref_does_not_hold(self, plain):
        assert UC.show(str(plain), "HEAD", "specs/none/gaps.md") is None

    def test_refuses_to_raise_on_a_byte_that_is_not_utf8(self, tmp_path):
        """#19: the base side decodes as `check_file` decodes the tree side,
        U+FFFD for a byte UTF-8 cannot read, or one such byte aborted the
        whole comparison."""
        d = _committed(tmp_path, {"gaps.md": memo(CANONICAL)})
        path = d / "gaps.md"
        path.write_bytes(memo(CANONICAL).encode("utf-8") + b"| a \xff b | c |\n")
        commit_everything_as_e(d, "a byte that is not UTF-8")
        with open(path, encoding="utf-8", errors="replace") as handle:
            on_disk = handle.read()
        assert "�" in on_disk
        assert UC.show(str(d), "HEAD", "gaps.md") == on_disk


class Test_mode_at:
    def test_accepts_a_tracked_link_as_a_link(self, linked):
        at = f"specs/{link_of(linked)}/gaps.md"
        assert UC.mode_at(str(linked), "HEAD", at) == UC.LINK_MODE

    @pytest.mark.parametrize(
        "at, mode",
        [(f"specs/{WORK}/gaps.md", "100644"), ("specs/none/gaps.md", None)],
        ids=["a file", "a path the ref does not hold"],
    )
    def test_refuses_a_file_or_an_absent_path_as_a_link(self, linked, at, mode):
        assert UC.mode_at(str(linked), "HEAD", at) == mode


class Test_compare_at:
    @pytest.mark.parametrize(
        "now, kind", [(1, "error"), (2, None)], ids=["fewer here", "as many"]
    )
    def test_refuses_fewer_rows_than_the_base_held_and_no_fewer(self, plain, now, kind):
        at = f"specs/{WORK}/gaps.md"
        found = UC.compare_at(str(plain), "HEAD", at, at, now, "HEAD")
        assert (found and found[0]) == kind, found
        if kind:
            assert "2 rows at HEAD, 1 here" in found[1], found

    def test_accepts_a_path_the_base_does_not_hold_as_nothing_to_compare(self, plain):
        at = "specs/none/gaps.md"
        assert UC.compare_at(str(plain), "HEAD", at, at, 0, "HEAD") is None

    def test_refuses_to_count_a_base_section_it_cannot_read(self, tmp_path):
        d = _committed(tmp_path, {"gaps.md": "# nothing here\n"})
        found = UC.compare_at(str(d), "HEAD", "gaps.md", "gaps.md", 0, "HEAD")
        assert found[0] == "notice" and "could not be read" in found[1], found


# --- what a settle removed ----------------------------------------------------


class Test_rule_changes:
    def test_accepts_the_one_reader_of_a_specs_rule_changes(self):
        assert callable(UC.rule_changes().parse)

    def test_refuses_to_load_it_twice(self):
        assert UC.rule_changes() is UC.rule_changes()


class Test_open_record_rows:
    def test_accepts_every_open_item_of_the_record(self, settle):
        assert UC.open_record_rows(str(settle), "HEAD", f"specs/{OPEN_ITEM}") == [
            ("gaps.md", "how the gate renders in a TUI"),
            ("gaps.md", "whether Windows hooks fire"),
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


class Test_settled:
    def test_accepts_every_directory_that_stood_at_the_ref(self, settle):
        """S6 at the predicate (#1033): a directory that stood at the ref is
        settled whatever its record and its spec say: an open row, a spec an
        earlier commit dropped, a rule `docs/` does not hold, a section that
        does not parse, a spec with no section, and no spec at all."""
        dirs = [
            f"specs/{n}"
            for n in (
                OPEN_ITEM,
                DROPPED,
                SETTLE_A,
                SETTLE_BAD,
                SETTLE_C,
                CLOSED_ITEM,
            )
        ]
        assert UC.settled(str(settle), "HEAD", dirs) == set(dirs)

    @pytest.mark.parametrize(
        "ref, name",
        [("HEAD", "1780000099-none"), ("nosuch", OPEN_ITEM)],
        ids=["a directory the ref never held", "a ref that does not resolve"],
    )
    def test_refuses_a_directory_the_ref_does_not_hold(self, settle, ref, name):
        assert UC.settled(str(settle), ref, [f"specs/{name}"]) == set()


class Test_settled_root:
    @pytest.mark.parametrize("state", ["absent", "empty", "a file only"])
    def test_accepts_a_roots_own_specs_with_no_work_item(self, tmp_path, state):
        (tmp_path / "seal").mkdir()
        if state != "absent":
            (tmp_path / "seal" / "threads").mkdir()
        if state == "a file only":
            write(tmp_path, "seal/threads/README.md", "r\n")
        assert UC.settled_root(str(tmp_path / "seal" / "threads")) is True

    @pytest.mark.parametrize("state", ["a work item", "another parent", "no root"])
    def test_refuses_a_work_item_another_parent_and_no_root(self, tmp_path, state):
        if state == "a work item":
            (tmp_path / "seal" / "threads" / WORK).mkdir(parents=True)
        if state == "another parent":
            (tmp_path / "other").mkdir()
        path = tmp_path / ("other" if state == "another parent" else "seal") / "threads"
        assert UC.settled_root(str(path)) is False


class Test_absent_root:
    def test_accepts_the_specs_path_of_a_top_level_holding_no_root(self, tmp_path):
        git(tmp_path, "init", "-q")
        assert UC.absent_root(str(tmp_path / "seal" / "threads")) is True

    @pytest.mark.parametrize(
        "state",
        ["a root", "a subdirectory", "no repository", "another parent", "a typo"],
    )
    def test_refuses_a_root_a_subdirectory_no_repository_and_another_name(
        self, sealed, tmp_path, state
    ):
        """Absence is read only at a working tree's top level and under the
        one spelling: anything else is a mistyped path, as it always was."""
        if state == "a typo":
            git(tmp_path, "init", "-q")
        path = {
            "a root": sealed / "seal" / "threads",
            "a subdirectory": sealed / "seal" / "seal" / "threads",
            "no repository": tmp_path / "seal" / "threads",
            "another parent": sealed / "other" / "threads",
            "a typo": tmp_path / "seal" / "spces",
        }[state]
        assert UC.absent_root(str(path)) is False


class Test_unwritten_root:
    def test_accepts_a_roots_specs_holding_work_items_and_no_overview(self, unwritten):
        assert UC.unwritten_root(str(unwritten / "seal" / "threads")) is True

    @pytest.mark.parametrize("state", ["an overview", "no work item", "another parent"])
    def test_refuses_an_overview_no_work_item_and_another_parent(self, tmp_path, state):
        (tmp_path / "seal" / "threads").mkdir(parents=True)
        path = tmp_path / ("other" if state == "another parent" else "seal") / "threads"
        if state == "another parent":
            write(tmp_path, f"other/threads/{WORK}/frame/design.md", "# a spec\n")
        if state == "an overview":
            write(tmp_path, f"seal/threads/{WORK}/gaps.md", memo(CANONICAL))
        assert UC.unwritten_root(str(path)) is False


class Test_under_root:
    def test_accepts_a_slash_joined_path_as_the_disk_spells_it(self):
        assert UC.under_root("r", "specs/a/gaps.md") == os.path.join(
            "r", "specs", "a", "gaps.md"
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
        elif "gaps.md:" in ln:
            found.append(ln.split(":")[0])
    return found


# How a person names a closing memo through a link, each shape the path as
# named and the path the base held the memo at.
NAMED_LINK = (
    "a file link",
    "a directory link",
    "a file under a linked directory",
    "a linked tree holding a file link",
)


def a_named_link(tmp_path, shape, lost):
    """`(repository, path as named)`: `specs/OTHER/gaps.md` held two rows at
    HEAD, and now the memo is a link to `specs/WORK/gaps.md`, or its
    directory a link to `specs/WORK`, by SHAPE. WORK's memo holds one row
    where LOST, and two otherwise. The linked tree is the file link reached
    through `view`, a link of this checkout to `specs`, so the base spells
    the memo neither as named nor as its real path."""
    target = CANONICAL.replace(WINDOWS + "\n", "") if lost else CANONICAL
    d = _committed(
        tmp_path,
        {
            f"specs/{WORK}/gaps.md": memo(target),
            f"specs/{OTHER}/gaps.md": memo(CANONICAL, OTHER),
        },
    )
    if shape in ("a file link", "a linked tree holding a file link"):
        named = d / "specs" / OTHER / "gaps.md"
        os.remove(named)
        symlink_or_skip(os.path.join("..", WORK, "gaps.md"), str(named))
        if shape == "a file link":
            return d, named
        symlink_or_skip("specs", str(d / "view"), directory=True)
        return d, d / "view"
    shutil.rmtree(d / "specs" / OTHER)
    symlink_or_skip(WORK, str(d / "specs" / OTHER), directory=True)
    named = d / "specs" / OTHER
    return d, named if shape == "a directory link" else named / "gaps.md"


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
            argv.append(str(tmp_path / "seal" / "threads"))
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
        14), and it names the fork point and the base's tip. Since #1033 it
        and the module's docstring say what reads as a settle, and nothing
        about the records or `docs/`."""
        with pytest.raises(SystemExit):
            UC.main(["--help"])
        rendered = " ".join(capsys.readouterr().out.split())
        assert (
            "the fork point on a branch checkout and the base's tip in CI" in rendered
        )
        said = "stood at the merge base and is gone whole, which reads as a settle"
        assert said in rendered, rendered
        assert "holding every rule change" not in rendered, rendered
        doc = " ".join(UC.__doc__.split())
        assert "unless its whole directory stood at the base and is gone" in doc
        assert "unless a settle removed its directory whole" not in doc

    # `--baseline`: a row and a record leave by being closed.

    def test_accepts_a_closed_row_and_a_fenced_example_against_the_baseline(
        self, plain, tmp_path, capsys
    ):
        """Marking keeps the row, so the count does not fall; and the strict
        reader and the base reader agree about an example added."""
        d = copy_of(plain, tmp_path)
        path = d / "specs" / WORK / "gaps.md"
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
        drop_line(d / "specs" / WORK / "gaps.md", WINDOWS)
        assert run([str(d), "--baseline", "HEAD"]) == 1
        out = capsys.readouterr().out
        assert "2 rows at HEAD, 1 here" in out
        assert "Re-add the row, its Item cell opening with the word `closed`" in out

    @pytest.mark.rule("record-comment-line-refused")
    def test_accepts_a_base_holding_a_comment_line_as_not_compared(
        self, plain, tmp_path, capsys
    ):
        """S6 of #1012: a base overview holding a line that begins `<!--` is
        named as not compared, never counted as zero rows, and the exit code
        is the working tree's, because nobody can edit a commit that already
        happened. A row deleted in the stripping commit goes uncompared once."""
        d = copy_of(plain, tmp_path)
        path = d / "specs" / WORK / "gaps.md"
        replace_in(path, "## Not verified\n", "## Not verified\n\n<!-- guidance -->\n")
        commit_everything_as_e(d, "an overview from an old template")
        replace_in(path, "\n<!-- guidance -->\n", "")
        drop_line(path, WINDOWS)
        assert run([str(d), "--baseline", "HEAD"]) == 0
        out = capsys.readouterr().out
        named = out.split("not compared against HEAD:")[1]
        assert WORK in named and UC.COMMENT_LINE in named, out

    @pytest.mark.parametrize(
        "change, gone, settled",
        [("delete one and rename the other", 1, 1), ("delete both", 2, 0)],
        ids=["a file and a rename", "every overview"],
    )
    def test_refuses_a_record_that_left_whole(
        self, plain, tmp_path, capsys, change, gone, settled
    ):
        """Deleting the file was cheaper and quieter than deleting a row, said
        out loud. A scan that finds nothing because every overview left
        reports the deletion rather than an empty scan. Since #1033 a
        directory gone whole reads as a settle, so a renamed one is named
        settled at its old path; its rows are listed where it went and are
        counted against nothing at the old one."""
        d = copy_of(plain, tmp_path)
        item = d / "specs" / WORK
        if change == "delete one and rename the other":
            os.remove(item / "gaps.md")
            os.rename(d / "specs" / OTHER, d / "specs" / "1780000001-renamed")
        if change == "delete both":
            os.remove(item / "gaps.md")
            os.remove(d / "specs" / OTHER / "gaps.md")
        assert run([str(d), "--baseline", "HEAD"]) == 1
        out = capsys.readouterr().out
        assert out.count("present at HEAD and not here") == gone, out
        assert out.count("settled: the directory stood at HEAD") == settled, out

    @pytest.mark.parametrize(
        "change, argv",
        [
            ("delete specs", ["specs"]),
            ("delete the item", [f"specs/{WORK}/gaps.md"]),
        ],
        ids=["the scan path", "two levels"],
    )
    def test_accepts_a_scan_path_gone_whole_as_a_settle(
        self, plain, tmp_path, capsys, change, argv
    ):
        """A scan path deleted wholesale is compared rather than called a bad
        argument, two levels gone too. Each directory under it stood at the
        base and is gone whole, which reads as a settle since #1033: the
        limit that work item states for a whole removal outside a settle,
        whose diff shows it to its review."""
        d = copy_of(plain, tmp_path)
        shutil.rmtree(d / "specs" if change == "delete specs" else d / "specs" / WORK)
        paths = [os.path.join(str(d), *a.split("/")) for a in argv]
        assert run([*paths, "--baseline", "HEAD"]) == 0
        out = capsys.readouterr().out
        assert "present at HEAD and not here" not in out, out
        assert "settled: the directory stood at HEAD" in out, out

    def test_refuses_an_unreadable_section_without_reporting_a_deletion(
        self, plain, tmp_path, capsys
    ):
        """A misspelt heading returns zero rows, and comparing that zero told
        the author to restore rows still in the file."""
        d = copy_of(plain, tmp_path)
        replace_in(
            d / "specs" / WORK / "gaps.md",
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
        if in_ci:
            monkeypatch.setenv("GITHUB_ACTIONS", "true")
        d = copy_of(plain, tmp_path)
        os.remove(d / "specs" / WORK / "gaps.md")
        drop_line(d / "specs" / OTHER / "gaps.md", WINDOWS)
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
        """One record, two paths: counting both doubles its open items,
        dropping one from the presence check reports it deleted, and reading
        the link's own blob at the base leaves the record uncompared (#19)."""
        assert run([str(linked), "--baseline", "HEAD"]) == 0
        out = capsys.readouterr().out
        tally = [ln for ln in out.split("\n") if ln.startswith("1 closing memos")]
        assert len(tally) == 1 and " 2 open " in tally[0], out
        assert "not compared" not in out and "left the record" not in out, out

    @pytest.mark.parametrize("scanned", ["the tree", "the link's directory alone"])
    def test_refuses_a_row_deleted_through_a_tracked_link_naming_the_real_file(
        self, linked, tmp_path, monkeypatch, capsys, scanned
    ):
        """#19: the path kept was the first in sort order, so a link sorting
        before its target, or standing alone under the scanned path, had its
        own blob read at the base, and a deleted row passed with exit 0. Both
        sides read the real file now, and the line names it."""
        d = copy_of(linked, tmp_path)
        drop_line(d / "specs" / WORK / "gaps.md", WINDOWS)
        where = d if scanned == "the tree" else d / "specs" / link_of(d)
        monkeypatch.chdir(d)
        assert run([str(where), "--baseline", "HEAD"]) == 1
        out = capsys.readouterr().out
        assert "2 rows at HEAD, 1 here" in out, out
        named = [os.path.basename(os.path.dirname(p)) for p in reported_paths(out)]
        assert named == [WORK], out

    @pytest.mark.parametrize(
        "name",
        [OTHER, "1779999999-link"],
        ids=["the link sorts after its target", "the link sorts before its target"],
    )
    def test_refuses_a_memo_replaced_by_a_link_to_one_holding_fewer_rows(
        self, tmp_path, monkeypatch, capsys, name
    ):
        """A memo that was a file at the base and is a link here held its own
        rows there. With only the real path kept, nothing read the base at the
        link's path, and its rows left with exit 0 in either order; before
        #19's change they were compared only where the link sorted first.
        They are compared with what the link reads now, under its own path."""
        one_row = CANONICAL.replace(WINDOWS + "\n", "")
        d = _committed(
            tmp_path,
            {
                f"specs/{WORK}/gaps.md": memo(one_row),
                f"specs/{name}/gaps.md": memo(CANONICAL, name),
            },
        )
        os.remove(d / "specs" / name / "gaps.md")
        symlink_or_skip(
            os.path.join("..", WORK, "gaps.md"), str(d / "specs" / name / "gaps.md")
        )
        monkeypatch.chdir(d)
        assert run([str(d), "--baseline", "HEAD"]) == 1
        out = capsys.readouterr().out
        assert "2 rows at HEAD, 1 here" in out, out
        named = [os.path.basename(os.path.dirname(p)) for p in reported_paths(out)]
        assert named == [name], out

    @pytest.mark.parametrize("named", ["the tree", "the link"])
    @pytest.mark.parametrize("volume", ["this volume", "another volume"])
    def test_accepts_a_link_to_a_file_beyond_the_repository_as_not_compared(
        self, tmp_path, monkeypatch, capsys, volume, named
    ):
        """#19: with the real path kept, a link's target outside the
        repository is a path no commit holds; `show` answered None and the
        file left the report in silence. Its open rows are read, and it is
        named with the reason that is true. On another volume it has no
        relative form at all, induced so every leg runs it. The link named
        itself has no real spelling in the repository there either, and the
        base is asked under the spellings it has."""
        d = _committed(tmp_path, {f"specs/{WORK}/gaps.md": memo(CANONICAL)})
        write(tmp_path, "beyond/gaps.md", memo(CANONICAL, OTHER))
        (d / "specs" / OTHER).mkdir()
        symlink_or_skip(
            str(tmp_path / "beyond" / "gaps.md"), str(d / "specs" / OTHER / "gaps.md")
        )
        commit_everything_as_e(d, "a link out of the repository")
        if volume == "another volume":
            real_relpath = os.path.relpath

            def refuses_beyond(path, start=None):
                if os.path.basename(os.path.dirname(str(path))) == "beyond":
                    raise ValueError("path is on mount 'D:', start on mount 'C:'")
                return real_relpath(path, start)

            monkeypatch.setattr(os.path, "relpath", refuses_beyond)
        monkeypatch.chdir(d)
        given = d if named == "the tree" else d / "specs" / OTHER / "gaps.md"
        assert run([str(given), "--baseline", "HEAD"]) == 0
        out = capsys.readouterr().out
        memos = "2 closing memos · 4" if named == "the tree" else "1 closing memos · 2"
        assert f"{memos} open" in out, out
        named = out.split("not compared against HEAD:")[1]
        said = (
            "not compared: the file lies outside the repository, so no commit "
            "of the repository holds it"
        )
        assert "beyond" in named and said in named, out

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
            drop_line(d / "specs" / WORK / "gaps.md", WINDOWS)
        else:
            os.remove(d / "specs" / WORK / "gaps.md")
        assert run([str(tmp_path / "link"), "--baseline", "HEAD"]) == 1

    @pytest.mark.parametrize(
        "tracked, named",
        [(True, "view"), (False, "view"), (False, f"view/{WORK}/gaps.md")],
        ids=[
            "a tracked link",
            "a link of this checkout",
            "the deleted memo named through the link",
        ],
    )
    def test_refuses_a_memo_deleted_behind_a_link_inside_the_repository(
        self, tmp_path, monkeypatch, capsys, tracked, named
    ):
        """`ls-tree` lists nothing through a link, so the base is read under
        each spelling of the path, the real one among them, and a memo
        deleted behind a link inside the repository is reported as it was
        before #1225. Named itself, the memo was a mistyped path with nothing
        under it at the base, though the base held it."""
        d = _committed(
            tmp_path,
            {
                f"specs/{WORK}/gaps.md": memo(CANONICAL),
                f"specs/{WORK}/keep.txt": "kept\n",
                f"specs/{OTHER}/gaps.md": memo(CANONICAL, OTHER),
            },
        )
        symlink_or_skip("specs", str(d / "view"), directory=True)
        if tracked:
            commit_everything_as_e(d, "the link")
        os.remove(d / "specs" / WORK / "gaps.md")
        monkeypatch.chdir(d)
        assert run([named, "--baseline", "HEAD"]) == 1
        out = capsys.readouterr().out
        assert "present at HEAD and not here" in out, out
        reported = [UC.git_path(p) for p in reported_paths(out)]
        assert reported == [f"specs/{WORK}/gaps.md"], out

    @pytest.mark.parametrize("shape", list(NAMED_LINK))
    def test_refuses_a_row_lost_through_a_link_the_person_names(
        self, tmp_path, monkeypatch, capsys, shape
    ):
        """#1225: the argument was read through `real()`, so a named link
        reached the scan as its target's path. Nothing read the base at the
        path as named, and the rows it held there left with exit 0. They are
        compared with what that path reads now, and the line names it."""
        d, named = a_named_link(tmp_path, shape, lost=True)
        monkeypatch.chdir(d)
        assert run([str(named), "--baseline", "HEAD"]) == 1
        out = capsys.readouterr().out
        assert "2 rows at HEAD, 1 here" in out, out
        reported = [UC.git_path(p) for p in reported_paths(out)]
        assert reported == [f"specs/{OTHER}/gaps.md"], out

    def test_refuses_a_row_lost_through_a_named_link_out_of_every_repository(
        self, tmp_path, monkeypatch, capsys
    ):
        """#1225: the repository was looked up from the link's target, which
        is in none, so the run exited 2 saying the path was in no repository,
        though the link stands in one. The link's own path is compared there,
        and the target, which no commit holds, is named as not compared."""
        d = _committed(tmp_path, {f"specs/{OTHER}/gaps.md": memo(CANONICAL, OTHER)})
        write(tmp_path, "beyond/gaps.md", memo(CANONICAL.replace(WINDOWS + "\n", "")))
        named = d / "specs" / OTHER / "gaps.md"
        os.remove(named)
        symlink_or_skip(str(tmp_path / "beyond" / "gaps.md"), str(named))
        monkeypatch.chdir(d)
        assert run([str(named), "--baseline", "HEAD"]) == 1
        out = capsys.readouterr().out
        left = out.split("rows left the record without being closed:")[1]
        assert "2 rows at HEAD, 1 here" in left, out
        reported = [UC.git_path(p) for p in reported_paths(left)]
        assert reported == [f"specs/{OTHER}/gaps.md"], out
        uncompared = out.split("not compared against HEAD:")[1].split("rows left")[0]
        said = (
            "not compared: the file lies outside the repository, so no commit "
            "of the repository holds it"
        )
        assert "beyond" in uncompared and said in uncompared, out

    @pytest.mark.parametrize(
        "shape",
        ["a file link", "a directory link", "a linked tree holding a file link"],
    )
    def test_accepts_a_link_the_person_names_that_lost_no_row(
        self, tmp_path, capsys, shape
    ):
        """The base lists the memo under one spelling of the path, and the
        scan counts it under each, so nothing reads as deleted; the target
        holds the two rows the base held there."""
        _repo, named = a_named_link(tmp_path, shape, lost=False)
        assert run([str(named), "--baseline", "HEAD"]) == 0
        out = capsys.readouterr().out
        assert "left the record" not in out and "not compared" not in out, out

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
            write(d, f"specs/{name}/gaps.md", memo(tree, name))
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
            write(d, f"specs/{name}/gaps.md", tree)
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
        os.remove(d / "specs" / WORK / "gaps.md")
        assert run([str(d), "--baseline", "base"]) == 1
        out = capsys.readouterr().out
        short = git_out(d, "rev-parse", "HEAD")[:7]
        assert (
            f"present at the merge-base of base and HEAD ({short}) and not here" in out
        )
        assert "squashed-sibling" not in out, out

    def test_refuses_a_deleted_row_under_a_moved_base(self, forked, tmp_path, capsys):
        d = copy_of(forked, tmp_path)
        drop_line(d / "specs" / WORK / "gaps.md", WINDOWS)
        assert run([str(d), "--baseline", "base"]) == 1
        assert "2 rows at the merge-base of base and HEAD" in capsys.readouterr().out

    def test_refuses_a_deletion_naming_a_ref_that_is_the_merge_base_alone(
        self, forked, tmp_path, capsys
    ):
        d = copy_of(forked, tmp_path)
        os.remove(d / "specs" / WORK / "gaps.md")
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
        """S6 of #1033: a directory that stood at the merge base and is gone
        whole is a settle and not this branch's deletion, whatever its record
        held there and whatever `docs/` holds of its spec: an open row, a rule
        `docs/` does not hold, a spec an earlier commit dropped, a section
        that does not parse, a spec with no section, and no spec. It is named
        rather than passed over in silence, in the line a person reads in the
        hygiene workflow's output."""
        d = copy_of(settle, tmp_path)
        removed = [OPEN_ITEM, SETTLE_A, DROPPED, SETTLE_BAD, SETTLE_C, CLOSED_ITEM]
        for name in removed:
            shutil.rmtree(d / "specs" / name)
        assert run([str(d), "--baseline", "HEAD"]) == 0
        out = capsys.readouterr().out
        assert "present at HEAD and not here" not in out, out
        named = out.split("not deleted from the record:")[1]
        assert "6 settled" in out and all(n in named for n in removed), out
        assert (
            "settled: the directory stood at HEAD and is gone whole, which "
            "reads as a settle"
        ) in " ".join(out.split())
        # A path whose every overview a settle removed reads no overview and
        # is still no empty scan.
        assert run([str(d / "specs" / SETTLE_C), "--baseline", "HEAD"]) == 0

    @pytest.mark.rule("a-settle-is-no-deletion")
    def test_a_squash_that_closes_and_removes_a_directory_is_a_settle(
        self, settle, tmp_path, capsys
    ):
        """S7 of #1033, the release pull request: the base holds the
        directory with its rows open, and one squash commit on the head
        removed it whole. Asked at that base, the directory is settled."""
        d = copy_of(settle, tmp_path)
        git(d, "branch", "release-base")
        git(d, "rm", "-rq", f"specs/{OPEN_ITEM}")
        commit_everything_as_e(d, "the settle, squashed")
        assert run([str(d), "--baseline", "release-base"]) == 0
        out = " ".join(capsys.readouterr().out.split())
        assert "1 settled" in out and OPEN_ITEM in out, out
        assert "and not here" not in out, out

    def test_refuses_a_removal_no_settle_explains(self, settle, tmp_path, capsys):
        """S8: a memo deleted from a directory that stays is a deletion
        whatever the predicate would say, open rows or closed, and each is
        named. Since #1033 a directory removed whole is a settle, so an open
        row and a dropped spec no longer make one a deletion, and the message
        names the one shape left: the directory still stands. A renamed
        directory is gone whole from its old path, so the message says nothing
        of a rename."""
        d = copy_of(settle, tmp_path)
        os.remove(d / "specs" / OPEN_ITEM / "gaps.md")
        os.remove(d / "specs" / CLOSED_ITEM / "gaps.md")
        assert run([str(d), "--baseline", "HEAD"]) == 1
        out = capsys.readouterr().out
        lines = [ln for ln in out.split("\n") if "present at HEAD and not here" in ln]
        for name in (OPEN_ITEM, CLOSED_ITEM):
            assert sum(name in ln for ln in lines) == 1, (name, out)
        for ln in lines:
            assert "its directory still stands, so this is no settle" in ln, out
        assert "settled" not in out and "renamed" not in out, out

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
            lambda root, ref, dirs: asked.extend(dirs) or set(),
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
        `--baseline origin/<base> seal/threads/`, and the path holds nothing at
        HEAD and held no overview at the merge base. That was a typo, exit 2,
        so every such pull request went red."""
        d = sealed
        if keep_empty_dir:
            d = copy_of(sealed, tmp_path)
            (d / "seal" / "threads").mkdir()
        argv = [str(d / "seal" / "threads")] + (
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

    # A pull request that declares nothing owes nothing (#952).

    @pytest.mark.rule("nothing-declared-nothing-owed")
    @pytest.mark.parametrize("baseline", [True, False], ids=["baseline", "plain"])
    def test_accepts_no_root_in_the_tree_and_compares_nothing_against_the_base(
        self, joined, tmp_path, capsys, baseline
    ):
        """S6: the pull request that moves a root to local mode with the
        workflow kept takes every overview out of the tree. With no root
        there nothing is declared, so the base is not read and the move is
        not this branch's deletion."""
        d = copy_of(joined, tmp_path)
        shutil.rmtree(d / "seal")
        argv = [str(d / "seal" / "threads")] + (
            ["--baseline", "HEAD"] if baseline else []
        )
        assert run(argv) == 0
        out = capsys.readouterr()
        said = " ".join((out.out + out.err).split())
        assert "has no `seal/` root in this tree" in said, said
        assert "present at HEAD" not in said and "open: 0" not in said, said

    @pytest.mark.rule("nothing-declared-nothing-owed")
    @pytest.mark.parametrize("baseline", [True, False], ids=["baseline", "plain"])
    def test_accepts_work_items_none_of_which_opened_a_closing_memo(
        self, unwritten, capsys, baseline
    ):
        """S6: every work item that never opened an `gaps.md` holds no
        row to read, and that was exit 2, `nothing was checked`."""
        argv = [str(unwritten / "seal" / "threads")] + (
            ["--baseline", "HEAD"] if baseline else []
        )
        assert run(argv) == 0
        out = capsys.readouterr()
        said = " ".join((out.out + out.err).split())
        assert "none of them carries an `gaps.md`" in said, said
        assert "open: 0" not in said, said

    @pytest.mark.rule("nothing-declared-nothing-owed")
    def test_refuses_a_memo_deleted_from_a_work_item_that_stays(
        self, joined, tmp_path, capsys
    ):
        """The second state holds only where the base comparison found
        nothing deleted: a root whose last overview left is still a
        deletion."""
        d = copy_of(joined, tmp_path)
        os.remove(d / OURS / "gaps.md")
        write(d, f"{OURS}/frame/design.md", "# a spec\n")
        assert run([str(d / "seal" / "threads"), "--baseline", "HEAD"]) == 1
        assert "present at HEAD and not here" in capsys.readouterr().out

    @pytest.mark.rule("nothing-declared-nothing-owed")
    @pytest.mark.parametrize("baseline", [True, False], ids=["baseline", "plain"])
    def test_refuses_a_missing_root_below_the_top_level_as_a_typo(
        self, sealed, capsys, baseline
    ):
        """Absence is read at the working tree's top level only, so a
        `seal/threads` typed from the wrong directory still names nothing."""
        argv = [str(sealed / "seal" / "seal" / "threads")] + (
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
        os.remove(d / TEAM / "gaps.md")
        assert run([str(d), "--baseline", "HEAD"]) == 0

    def test_refuses_a_team_overview_the_person_names(self, joined, tmp_path, capsys):
        """A person who names the file, or the directory it sits in, has
        asked for it, on both sides of the comparison."""
        assert run([str(joined / TEAM / "gaps.md")]) == 1
        assert run([str(joined / "specs")]) == 1
        d = copy_of(joined, tmp_path)
        os.remove(d / TEAM / "gaps.md")
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
        written once, in `hooks/lib/blocks.py`, and this module asks that copy."""
        blocks = os.path.join(ROOT, "hooks", "lib", "blocks.py")
        for name in ("fence_opener", "fence_closes", "gfm_lines"):
            code = getattr(UC, name).__code__
            assert os.path.samefile(code.co_filename, blocks), (name, code.co_filename)
        with open(UC.__file__, encoding="utf-8") as handle:
            source = handle.read()
        for defined in ("def fence_opener(", "def fence_closes(", "def gfm_lines("):
            assert defined not in source, defined
        assert "GFM_LINE_RE = re.compile" not in source

    def test_the_command_is_present_and_runs_the_script(self):
        """`bin/` lands on the Bash tool's PATH while the plugin is enabled,
        so `bin/seal` resolves its script relative to itself, a .cmd sibling
        ships for the platform that cannot run a POSIX shebang, and
        `seal unverified` hands its arguments to this script."""
        posix = os.path.join(ROOT, "bin", "seal")
        windows = os.path.join(ROOT, "bin", "seal.cmd")
        assert os.path.isfile(posix), "bin/seal missing"
        assert os.path.isfile(windows), "bin/seal.cmd missing"
        assert os.access(posix, os.X_OK), "bin/seal not executable"
        command = (
            [os.environ.get("COMSPEC", "cmd.exe"), "/c", windows]
            if os.name == "nt"
            else [posix]
        )
        done = subprocess.run(
            [*command, "unverified", "--help"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=120,
        )
        assert done.returncode == 0, done.stderr
        assert done.stdout.startswith("usage: seal unverified"), done.stdout

    def test_this_repositorys_own_overviews_are_all_readable(self):
        """The corpus is the real test, and it states the rule for new work:
        a work item that writes an overview writes this section in it."""
        assert run([os.path.join(ROOT, "seal", "threads")]) == 0


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
