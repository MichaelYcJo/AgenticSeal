"""The record of what was never verified has to be readable, and rows have to
leave it by being closed rather than deleted.

Every case here is a way the corpus already drifted or a way a tolerant reader
would have reported zero. Zero is the dangerous answer: it is indistinguishable
from "everything has been closed", which is the sentence this repository exists
to make expensive.
"""

import atexit
import importlib.util
import os
import random
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import pytest
from conftest import posix_id, symlink_or_skip

ROOT = os.path.join(os.path.dirname(__file__), "..")
SCRIPT = os.path.join(ROOT, "skills", "verify", "scripts", "unverified_check.py")


def load():
    spec = importlib.util.spec_from_file_location("unverified_check", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


uc = load()
CLOSED_MARK = uc.CLOSED

CANONICAL = """## Not verified

| Item | Who must answer |
|---|---|
| how the gate renders in a TUI | user, on the next session |
| whether Windows hooks fire | a maintainer with a Windows machine |
"""


def write(tmp_path, section, name="1780000000-work"):
    d = tmp_path / "specs" / name
    d.mkdir(parents=True)
    p = d / "overview.md"
    p.write_text(
        f"# {name} — overview\n\n## Not done\n\nsomething.\n\n{section}",
        encoding="utf-8",
    )
    return str(p)


def run(argv):
    """The CLI's exit code, so a test asserts what CI would see."""
    return uc.main(argv)


def test_unmarked_rows_are_counted_open(tmp_path):
    """The default has to be open. If an unmarked row read as closed, doing
    nothing would close the record."""
    op, cl, err = uc.check_file(write(tmp_path, CANONICAL))
    assert not err
    assert len(op) == 2 and not cl


def test_a_marked_row_counts_closed_and_keeps_its_text(tmp_path):
    """Closing is marking, so the item stays legible after it is closed."""
    section = CANONICAL.replace(
        "| how the gate renders in a TUI | user, on the next session |",
        "| closed how the gate renders in a TUI | seen on screen 2026-08-25, session log |",
    )
    op, cl, err = uc.check_file(write(tmp_path, section))
    assert not err
    assert len(op) == 1
    assert cl[0][1] == "how the gate renders in a TUI"


def test_a_bare_closing_word_does_not_close_anything(tmp_path):
    """A word with nothing after it is the checkbox this repo refuses
    everywhere else — `plan.md`'s Verified-by column exists for the same
    reason."""
    section = CANONICAL.replace(
        "| how the gate renders in a TUI | user, on the next session |",
        "| closed | done |",
    )
    _, _, err = uc.check_file(write(tmp_path, section))
    assert err and "bare" in err[0][1]


# Spelt by code point, so the three stay legible in the source and no emoji
# stands in it.
OLD_MARK = chr(0x2705)
ZERO_WIDTH_SPACE = chr(0x200B)
EMOJI_SELECTOR = chr(0xFE0F)
CLOSED_ROW_CASES = {
    # name: (row, (what the reader makes of it, the item or the refusal's words))
    "the word and the item": (
        "| closed how the gate renders in a TUI | seen on screen |",
        ("closed", "how the gate renders in a TUI"),
    ),
    "the word, a tab, the item": (
        "| closed\thow the gate renders in a TUI | seen on screen |",
        ("closed", "how the gate renders in a TUI"),
    ),
    "a word that only begins with it": (
        "| closed-loop control on Windows | a maintainer |",
        ("open", None),
    ),
    "a word that only contains it": (
        "| enclosed paths on Windows | a maintainer |",
        ("open", None),
    ),
    "the bare word": ("| closed | done |", ("refused", "bare")),
    "the bare word and a zero-width space": (
        f"| closed{ZERO_WIDTH_SPACE} | done |",
        ("refused", "bare"),
    ),
    "the old mark and the item": (
        f"| {OLD_MARK} how the gate renders in a TUI | seen on screen |",
        ("refused", "U+2705"),
    ),
    "the old mark as a keyboard emits it": (
        f"| {OLD_MARK}{EMOJI_SELECTOR} how the gate renders in a TUI | seen on screen |",
        ("refused", "U+2705"),
    ),
    "the bare old mark": (f"| {OLD_MARK} | done |", ("refused", "U+2705")),
    "capitalised": (
        "| Closed how the gate renders in a TUI | seen on screen |",
        ("refused", "`Closed`"),
    ),
    "upper case": (
        "| CLOSED how the gate renders in a TUI | seen on screen |",
        ("refused", "`CLOSED`"),
    ),
    "with a colon": (
        "| closed: how the gate renders in a TUI | seen on screen |",
        ("refused", "`closed:`"),
    ),
}


class TestClosedRow:
    """T4 of `1792129100-the-mechanics-leave-before-the-agents-are-rewritten`.

    A closed row opens with the word `closed`, exact spelling, and the item
    after it. The emoji that used to close a row is refused naming the row
    and the edit, and so is a bare word and any other spelling of it.

    Protects: the emoji mark read by a gate, the class #923 found four
    times, and a closing that a capital letter or a colon would quietly turn
    back into an open row. No other case reads a row's first word."""

    @pytest.mark.parametrize(
        "row, expected", CLOSED_ROW_CASES.values(), ids=CLOSED_ROW_CASES.keys()
    )
    def test_the_word_closes_and_the_mark_and_the_bare_word_are_refused(
        self, tmp_path, row, expected
    ):
        section = CANONICAL.replace(
            "| how the gate renders in a TUI | user, on the next session |", row
        )
        op, cl, err = uc.check_file(write(tmp_path, section))
        kind, said = expected
        if kind == "refused":
            assert err, f"{row!r} was accepted"
            assert said in err[0][1], err
            return
        assert not err, err
        if kind == "closed":
            assert [c[1] for c in cl] == [said] and len(op) == 1
        else:
            assert not cl and len(op) == 2

    def test_the_old_marks_refusal_names_the_edit(self, tmp_path):
        """§14: the sentence a person reads when their overview still carries
        the old mark, pinned whole, because the edit it names is the whole of
        what they have to do."""
        section = CANONICAL.replace(
            "| how the gate renders in a TUI | user, on the next session |",
            f"| {OLD_MARK} how the gate renders in a TUI | seen on screen |",
        )
        _, _, err = uc.check_file(write(tmp_path, section))
        assert err[0] == (
            11,
            "the row opens with U+2705, which no longer closes a row: a closed "
            "row opens with the word `closed`, so write "
            "`| closed how the gate renders in a TUI | <what closed it> |`",
        )

    def test_a_base_closed_with_the_old_mark_is_still_compared(self, tmp_path, capsys):
        """A base revision cannot be edited, so it is read the way it was
        written: a row there opening with the old mark is a closed row. Read
        as a refusal, every base written before the word would be `not
        compared`, and a row deleted against it would pass.

        Protects: the deletion check going blind on every repository's base
        at the release that brings the word."""
        old = CANONICAL.replace(
            "| whether Windows hooks fire", f"| {OLD_MARK} whether Windows hooks fire"
        )
        d, p = git_repo(tmp_path, old)
        text = open(p, encoding="utf-8").read()
        with open(p, "w", encoding="utf-8") as f:
            f.write(text.replace(f"| {OLD_MARK} whether", "| closed whether"))
        assert run([str(d), "--baseline", "HEAD"]) == 0
        assert "not compared" not in capsys.readouterr().out
        with open(p, "w", encoding="utf-8") as f:
            f.write(
                "\n".join(ln for ln in text.splitlines() if "Windows" not in ln) + "\n"
            )
        assert run([str(d), "--baseline", "HEAD"]) == 1
        assert "2 rows at HEAD, 1 here" in capsys.readouterr().out


# Every shipped text that tells a session how a `## Not verified` row closes.
CLOSING_TEXTS = [
    ("templates", "sdd-overview.md"),
    ("templates", "config.md"),
    ("docs", "the-record-layout.md"),
    ("skills", "implement", "SKILL.md"),
    ("skills", "verify", "SKILL.md"),
    ("skills", "settle", "SKILL.md"),
    ("skills", "settle", "scripts", "settle.py"),
    ("skills", "verify", "scripts", "unverified_check.py"),
]


@pytest.mark.parametrize("parts", CLOSING_TEXTS, ids=lambda p: "/".join(p))
def test_no_text_that_states_the_closing_shows_the_old_mark(parts):
    """A text that still shows the emoji sends whoever follows it to a row
    the check refuses. Protects: one of these quietly keeping the old mark
    when the others moved, which is how a rule stated in five places drifts;
    no other case reads them for it."""
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        assert OLD_MARK not in f.read()


def test_the_template_shows_the_word():
    """The template is what a session copies, so its example row is the one
    the check accepts."""
    with open(
        os.path.join(ROOT, "templates", "sdd-overview.md"), encoding="utf-8"
    ) as f:
        text = f.read()
    assert "| closed <the item, kept> | <what closed it" in text


# Every shipped text that says which way an unmarked row reads.
OPEN_BY_DEFAULT_TEXTS = [
    ("templates", "sdd-overview.md"),
    ("skills", "implement", "SKILL.md"),
    ("skills", "verify", "scripts", "unverified_check.py"),
]


@pytest.mark.parametrize("parts", OPEN_BY_DEFAULT_TEXTS, ids=lambda p: "/".join(p))
def test_a_text_saying_a_row_counts_open_names_the_open_item_that_reads_closed(
    tmp_path, parts
):
    """§14, round 1's finding 1: an open item whose own text begins with the
    word `closed` reads as closed, and the reader cannot tell it from a
    closing. So each text that says an unmarked row counts open names that
    row too, and the reader's reading of it is checked beside the sentence.

    Protects: a text promising that the silent direction is always "still
    open" while `| closed issues are not re-read | the owner |` closes
    itself, and a reader that changes how it reads that row while the
    sentence stays. The closing-word cases read the row's first word and no
    text; no other case reads these texts for the exception."""
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        text = " ".join(f.read().split())
    assert "whose own text begins with the word `closed`" in text
    assert 'always "still open"' not in text
    section = CANONICAL.replace(
        "| how the gate renders in a TUI | user, on the next session |",
        "| closed issues are not re-read | the owner |",
    )
    op, cl, err = uc.check_file(write(tmp_path, section))
    assert not err and len(op) == 1
    assert [c[1] for c in cl] == ["issues are not re-read"]


def test_a_row_with_an_empty_cell_fails(tmp_path):
    section = CANONICAL + "| an item with no answerer | |\n"
    _, _, err = uc.check_file(write(tmp_path, section))
    assert err and "empty cell" in err[0][1]


def test_the_template_placeholder_row_fails(tmp_path):
    """A spec bootstrapped from the template and never filled in used to read
    as one open item with no content."""
    section = CANONICAL + "| <what was not verified> | <who answers it> |\n"
    _, _, err = uc.check_file(write(tmp_path, section))
    assert err and "placeholder" in err[0][1]


@pytest.mark.parametrize(
    "heading",
    [
        "## Not verified (who must answer)",
        "## Blocked / not verified (who must answer)",
        "## Not Verified",
    ],
)
def test_a_heading_spelling_it_does_not_know_is_an_error_not_a_zero(tmp_path, heading):
    """All three spellings are real. Two of them were in this corpus, and one
    kept its rows out of the hand count that opened this work. The failure
    being prevented is a reader that shrugs and returns zero."""
    section = CANONICAL.replace("## Not verified", heading)
    _, _, err = uc.check_file(write(tmp_path, section))
    assert err
    assert "no `## Not verified` section" in err[0][1]
    assert heading in err[0][1], "the error has to name the spelling it found"


def test_the_old_column_name_fails(tmp_path):
    """Three overviews used `| Item | Who |`. One accepted spelling is what
    keeps the next one from being invented silently."""
    section = CANONICAL.replace("| Item | Who must answer |", "| Item | Who |")
    _, _, err = uc.check_file(write(tmp_path, section))
    assert err and "header is" in err[0][1]


def test_a_missing_section_is_an_error(tmp_path):
    p = write(tmp_path, "## Fed back into the spec\n\nnone.\n")
    _, _, err = uc.check_file(p)
    assert err and "no `## Not verified` section" in err[0][1]


def test_two_sections_are_an_error(tmp_path):
    _, _, err = uc.check_file(write(tmp_path, CANONICAL + "\n" + CANONICAL))
    assert err and "more than one" in err[0][1]


def test_prose_where_the_table_belongs_fails(tmp_path):
    """Four overviews recorded this as bullet prose. Prose is not countable,
    and a section that cannot be counted is not a record of how much is open."""
    section = "## Not verified\n\n- the TUI rendering, nobody has seen it\n"
    _, _, err = uc.check_file(write(tmp_path, section))
    assert err and "found prose" in err[0][1]


def test_an_empty_table_fails(tmp_path):
    section = "## Not verified\n\n| Item | Who must answer |\n|---|---|\n"
    _, _, err = uc.check_file(write(tmp_path, section))
    assert err and "no rows" in err[0][1]


BLOCK = "the block `- nothing` with `  why: <reason>`"


@pytest.mark.parametrize(
    "block",
    [
        "- nothing\n  why: every claim in this item was executed.\n",
        "- nothing\n  why: every claim in this item\n    was executed.\n",
    ],
    ids=["one line", "continued four spaces in"],
)
def test_the_no_change_block_is_how_a_work_item_says_nothing_is_open(tmp_path, block):
    """S1 of #1000. Saying it explicitly is the point: silence and "nothing
    open" have to look different in the file, not only in the tally. The
    block is the one `## Rule changes` writes (`skills/settle/SKILL.md`
    §*Rule changes*), read by the same function."""
    op, cl, err = uc.check_file(write(tmp_path, f"## Not verified\n\n{block}"))
    assert not err and not op and not cl


def line_in(path, needle):
    """The file line number of the first line of PATH that is NEEDLE."""
    return Path(path).read_text(encoding="utf-8").split("\n").index(needle) + 1


@pytest.mark.parametrize(
    "first", ["none — x", "none - x", "none", "None.", "nothing — x"]
)
def test_the_old_line_is_refused_naming_the_block_and_read_at_a_base(tmp_path, first):
    """S2 of #1000. The working tree refuses the old `none — <why>` line and
    its near misses at the line, naming the block; a base revision reads the
    same line as no rows, because a commit cannot be edited (`OLD_MARK`'s
    precedent). Seen red against the prefix reader, which read every one of
    them but `nothing — x` as nothing open."""
    path = write(tmp_path, f"## Not verified\n\n{first}\n")
    _, _, err = uc.check_file(path)
    assert [line for line, _ in err] == [line_in(path, first)], err
    assert BLOCK in err[0][1], err
    text = Path(path).read_text(encoding="utf-8")
    assert uc.check_text(text, strict_header=False) == ([], [], [])


@pytest.mark.parametrize(
    "body, bad, says",
    [
        ("- nothing\n", "- nothing", "`nothing` needs `why`"),
        ("- nothing\n  why:\n", "  why:", "`why` is empty"),
        ("- Nothing\n  why: x\n", "- Nothing", BLOCK),
        ("* nothing\n  why: x\n", "* nothing", BLOCK),
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
        "another list marker",
        "no space after the dash",
        "why at three spaces",
        "a second field",
        "beside a table",
    ],
)
def test_a_near_miss_of_the_block_is_refused_at_its_line(tmp_path, body, bad, says):
    """S3 of #1000. Each spelling is refused at its line, saying what is
    wrong with it, and read as nothing else. Seen red against the prefix
    reader, which refused the block itself as prose at its first line."""
    path = write(tmp_path, f"## Not verified\n\n{body}")
    op, cl, err = uc.check_file(path)
    assert err and err[0][0] == line_in(path, bad), err
    assert says in err[0][1], err
    assert not op and not cl


def test_the_near_miss_reading_is_linear_in_the_line():
    """#941's round 3 met a pattern that backtracked exponentially; the
    pattern that finds a near miss of the block repeats, so a long line of
    its repeated characters is read in well under a second."""
    import time

    start = time.monotonic()
    for line in ("- " * 50000 + "x", " " * 100000 + "nonesuch", "-*+" * 30000):
        uc.parse_section([line], 1)
    assert time.monotonic() - start < 1.0


def test_a_fenced_example_is_not_a_second_section(tmp_path):
    """An overview that quotes this very format would otherwise report itself
    as having two sections."""
    fenced = CANONICAL + "\n```markdown\n## Not verified\n\n| Item | Who |\n```\n"
    op, _, err = uc.check_file(write(tmp_path, fenced))
    assert not err and len(op) == 2


def test_a_line_opening_with_an_issue_number_does_not_end_the_section(tmp_path):
    """S9 of #867. `headings` read `startswith("#")`, so a line beginning
    `#120)` ended `## Not verified` and the row below it went uncounted, at
    exit 0 — the permissive direction. By the one rule,
    `unverified_check.py#heading_level`, the line is paragraph text inside
    the section: the row below is counted, and the line itself is named as
    a line in the table that is not a row. Seen red against
    `startswith("#")`: two rows and no error."""
    text = CANONICAL + "#120) wrapped onto its own line\n| a third item | the owner |\n"
    op, _, err = uc.check_file(write(tmp_path, text))
    assert len(op) == 3, op
    assert [message for _line, message in err] == [
        "a line inside the table that is not a table row"
    ], err


@pytest.mark.parametrize(
    "line, level",
    [
        ("## Not verified", 2),
        ("   ## Not verified", 2),
        ("    ## Not verified", None),
        ("\t## Not verified", None),
        ("#120) wrapped", None),
        ("#84's line", None),
        ("####### seven", None),
        ("#\tx", 1),
        ("#", 1),
        ("## closed ##", 2),
    ],
)
def test_the_heading_rule_reads_commonmarks_atx_heading(line, level):
    """S8 and S9's shapes at the rule itself (#867): CommonMark 4.2, at most
    three spaces, one to six `#`, then a space, a tab or the end."""
    assert uc.heading_level(line) == level


@pytest.mark.parametrize(
    "line, matches",
    [
        ("## Not verified", True),
        ("### not VERIFIED, read", True),
        ("   ## Not verified", True),
        ("##\tNot verified", True),
        ("# Not verified", False),
        ("#### Not verified", False),
        ("#120) not verified", False),
        ("## Not done", False),
    ],
)
def test_a_base_revisions_heading_is_a_level_two_or_three_heading_by_the_rule(
    line, matches
):
    """#867 round 1, 🟡 6. `LOOSE_HEADING` decides a base revision's wording
    alone; whether the line is a heading, and at which level, is
    `heading_level`'s. Its own pattern, `^#{2,3}\\s`, missed a heading
    indented up to three spaces. Seen red against that pattern."""
    assert bool(uc.LOOSE_HEADING.match(line)) is matches


def test_escaped_pipes_inside_a_cell_do_not_split_it(tmp_path):
    section = CANONICAL + "| whether `a \\| b` parses | the next session |\n"
    op, _, err = uc.check_file(write(tmp_path, section))
    assert not err and len(op) == 3


def test_a_scan_that_finds_no_overview_exits_2(tmp_path, capsys):
    """Zero files and zero open items are different answers. Reporting the
    first as the second is how a wrong path reads as a clean record."""
    (tmp_path / "empty").mkdir()
    assert run([str(tmp_path / "empty")]) == 2
    assert "nothing was checked" in capsys.readouterr().err


def test_open_items_do_not_fail_the_run(tmp_path, capsys):
    """Never a red build for an honest row: 45 were open when this shipped,
    and punishing them teaches sessions to write none."""
    write(tmp_path, CANONICAL)
    assert run([str(tmp_path)]) == 0
    assert "2 open" in capsys.readouterr().out


def test_zero_open_and_unreadable_are_different_exits_and_different_words(
    tmp_path, capsys
):
    """The requirement in one case: a reader must never confuse "everything is
    closed" with "this could not be read"."""
    closed = tmp_path / "closed"
    closed.mkdir()
    write(closed, "## Not verified\n\n- nothing\n  why: all executed.\n")
    assert run([str(closed)]) == 0
    clean = capsys.readouterr().out
    assert "open: 0" in clean

    broken = tmp_path / "broken"
    broken.mkdir()
    write(broken, "## Not verified\n\n- prose\n")
    assert run([str(broken)]) == 1
    bad = capsys.readouterr().out
    assert "could not be read" in bad
    assert "open: 0" not in bad


_BARE_INITED_REPO_TEMPLATE = None


def _bare_inited_repo_template():
    """A git-inited, identity-configured, empty repo -- what every `git_repo()`
    call needs before it writes and commits its own (test-specific) content."""
    global _BARE_INITED_REPO_TEMPLATE
    if _BARE_INITED_REPO_TEMPLATE is None:
        d = (
            Path(tempfile.mkdtemp(prefix="specseal-bare-inited-repo-template-"))
            / "repo"
        )
        subprocess.run(["git", "init", "-q", str(d)], check=True)
        subprocess.run(
            ["git", "-C", str(d), "config", "user.email", "t@example.com"],
            check=True,
        )
        subprocess.run(["git", "-C", str(d), "config", "user.name", "t"], check=True)
        atexit.register(shutil.rmtree, d, True)
        _BARE_INITED_REPO_TEMPLATE = d
    return _BARE_INITED_REPO_TEMPLATE


def git_repo(tmp_path, section):
    d = tmp_path / "repo"
    shutil.copytree(_bare_inited_repo_template(), d)

    def git(*a):
        subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True)

    p = write(d, section)
    git("add", "-A")
    git("commit", "-qm", "base")
    return d, p


def test_deleting_a_row_fails_against_the_baseline(tmp_path, capsys):
    """The whole convention rests on this. Without it, the cheapest way to
    lower the count stays "delete the line", and a closed item and a tidied-up
    one become the same edit."""
    d, p = git_repo(tmp_path, CANONICAL)
    text = open(p, encoding="utf-8").read()
    kept = "\n".join(ln for ln in text.splitlines() if "Windows" not in ln)
    with open(p, "w", encoding="utf-8") as f:
        f.write(kept + "\n")
    assert run([str(d), "--baseline", "HEAD"]) == 1
    out = capsys.readouterr().out
    assert "2 rows at HEAD, 1 here" in out


def test_closing_a_row_passes_the_baseline(tmp_path):
    """Marking keeps the row, so the count does not fall and the check is
    silent — the convention has to be the cheap path, not the expensive one."""
    d, p = git_repo(tmp_path, CANONICAL)
    text = open(p, encoding="utf-8").read()
    with open(p, "w", encoding="utf-8") as f:
        f.write(text.replace("| whether Windows", "| closed whether Windows"))
    assert run([str(d), "--baseline", "HEAD"]) == 0


def test_an_old_spelling_base_is_compared_again(tmp_path):
    """How the heading is found is the one argument the reader takes. A base
    revision written before this normalization is still a countable record,
    and refusing to read it stopped comparing four files that had been
    compared the commit before."""
    old = CANONICAL.replace("## Not verified", "## Not verified (who must answer)")
    d, p = git_repo(tmp_path, old)
    text = open(p, encoding="utf-8").read()
    with open(p, "w", encoding="utf-8") as f:
        f.write(
            text.replace(
                "## Not verified (who must answer)", "## Not verified"
            ).replace(
                "| whether Windows hooks fire | a maintainer with a Windows machine |\n",
                "",
            )
        )
    assert run([str(d), "--baseline", "HEAD"]) == 1


def test_the_canonical_heading_wins_over_a_looser_match_in_the_base(tmp_path, capsys):
    """The looser matcher must not select a different section from the one the
    working tree reads. A file holding both used to be reported as having lost
    rows nobody removed."""
    both = (
        CANONICAL + "\n### Not verified on Windows\n\n| a | b |\n|---|---|\n| x | y |\n"
    )
    d, _ = git_repo(tmp_path, both)
    assert run([str(d), "--baseline", "HEAD"]) == 0
    out = capsys.readouterr().out
    assert "not compared" not in out, (
        "exit 0 is not enough — without the canonical heading winning, the "
        "base matches twice, reads as unreadable, and is skipped rather than "
        "compared"
    )


def test_a_base_no_reader_can_make_sense_of_is_reported_as_not_compared(
    tmp_path, capsys
):
    """Not counted as zero, and not an error either: the author cannot edit a
    commit that already happened, and a count nobody can take is the one
    number this must not print."""
    d, p = git_repo(tmp_path, "## Not verified\n\n- the TUI rendering, as prose\n")
    with open(p, "w", encoding="utf-8") as f:
        f.write("# w — overview\n\n" + CANONICAL)
    assert run([str(d), "--baseline", "HEAD"]) == 0
    out = capsys.readouterr().out
    assert "not compared" in out
    assert "found prose" in out


def test_this_repositorys_own_overviews_are_all_readable():
    """The corpus is the real test. It also states the rule for new work: a
    spec directory that writes an overview writes this section in it."""
    assert run([os.path.join(ROOT, "seal", "specs")]) == 0


def collapsed(*parts):
    """File text with newlines flattened, so a match is not asserting where
    the author happened to wrap a line."""
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return " ".join(f.read().split())


def test_the_template_is_the_shape_the_checker_reads(tmp_path):
    """Template and checker drift apart silently otherwise: every new work
    item would copy a section the release check then refuses."""
    with open(
        os.path.join(ROOT, "templates", "sdd-overview.md"), encoding="utf-8"
    ) as f:
        template = f.read()

    d = tmp_path / "specs" / "1780000000-work"
    d.mkdir(parents=True)
    p = d / "overview.md"

    p.write_text(template, encoding="utf-8")
    _, _, err = uc.check_file(str(p))
    assert err and "placeholder" in err[0][1], (
        "a template copied and never filled in has to fail, or an empty record "
        "passes as a complete one"
    )

    filled = template.replace("<what was not verified>", "the TUI rendering").replace(
        "<who or what can answer it>", "user, on the next session"
    )
    p.write_text(filled, encoding="utf-8")
    op, _, err = uc.check_file(str(p))
    assert not err and len(op) == 1


def test_the_memo_no_longer_asks_for_what_the_diff_holds():
    """Item 2 wanted a line per file, which is `git diff --stat` retyped from
    memory after the fact."""
    skill = collapsed("skills", "implement", "SKILL.md")
    assert "each file path with a one-line description" not in skill
    assert "not a summary of the work" in skill
    assert "`git diff --stat` already holds the file list" in skill


def test_the_memo_keeps_one_line_of_purpose():
    """Below the six-file line no `spec.md` is written, so this line is the
    only place the purpose stays in the repository."""
    skill = collapsed("skills", "implement", "SKILL.md")
    assert "Why this work exists and what the result changes — **one line**" in skill
    assert "the only place the purpose stays in the repository" in skill
    with open(
        os.path.join(ROOT, "templates", "sdd-overview.md"), encoding="utf-8"
    ) as f:
        assert "## Why this work exists" in f.read()


def test_the_ladder_does_not_still_say_at_the_end():
    """Three of the four parts are written when they happen. A ladder that
    still says `overview.md at the end` contradicts the step above it, and the
    contradiction is what sessions resolve by reconstructing at the end. The
    smith's copy of the ladder left with #967; it opens the skill instead."""
    skill = collapsed("skills", "implement", "SKILL.md")
    assert "`overview.md` at the end" not in skill
    assert (
        "opened at the first divergence, unverified item, or fed-back clause" in skill
    )
    assert "`overview.md` at the end" not in collapsed("agents", "smith.md")


def test_the_skill_states_the_closing_convention():
    """The writer of a row is the one who has to know how it closes."""
    skill = collapsed("skills", "implement", "SKILL.md")
    assert "closed by marking it, never by deleting it" in skill
    assert "unverified-check --baseline" in skill


def test_a_comment_beside_the_section_is_not_read_as_content(tmp_path):
    """The template ships its guidance as a comment in this section, and an
    overview keeps it. Reading it as prose would fail every filled-in copy."""
    section = (
        "## Not verified\n\n<!-- guidance:\n| closed <item> | <what closed it> |\n-->\n\n"
        + CANONICAL.split("\n", 2)[2]
    )
    op, _, err = uc.check_file(write(tmp_path, section))
    assert not err and len(op) == 2


# --- round 2: what the first round's tests did not hold ----------------------


def test_a_row_with_three_cells_is_an_error_not_a_traceback():
    """`item, who = cells` unpacks two. Without the length guard this raises
    ValueError, and a gate that crashes is a gate nobody can read."""
    section = CANONICAL + "| an item | an answerer | a third cell |\n"
    _, _, err = uc.parse_section(section.splitlines()[2:], 3)
    assert err and "3 cells" in err[0][1]


def test_a_missing_separator_row_is_an_error(tmp_path):
    """Without it the header's own row would be read as the first item."""
    section = "## Not verified\n\n| Item | Who must answer |\n| an item | someone |\n"
    _, _, err = uc.check_file(write(tmp_path, section))
    assert err and "separator" in err[0][1]


def test_an_empty_section_is_an_error_not_a_traceback(tmp_path):
    """`content[0]` on an empty section is an IndexError. The section also has
    to say something: silence and "nothing open" are different claims."""
    section = "## Not verified\n\n## Fed back into the spec\n\nnone.\n"
    _, _, err = uc.check_file(write(tmp_path, section))
    assert err and "empty" in err[0][1]


def test_a_second_header_or_separator_inside_the_section_is_an_error(tmp_path):
    """Two tables in one section made `|---|---|` count as an open item."""
    section = (
        CANONICAL + "\n| Item | Who must answer |\n|---|---|\n| another | someone |\n"
    )
    _, _, err = uc.check_file(write(tmp_path, section))
    assert err and "one table" in err[0][1]


def test_rows_after_a_fenced_example_are_still_counted(tmp_path):
    """The reader used to stop at the fence, so anything below an example
    vanished — the silent omission this tool exists to refuse."""
    section = (
        CANONICAL
        + "\n```markdown\n| Item | Who must answer |\n```\n\n| a third item | someone |\n"
    )
    op, _, err = uc.check_file(write(tmp_path, section))
    assert not err, err
    assert len(op) == 3


def test_adding_a_fenced_example_is_not_read_as_a_deletion(tmp_path):
    """The strict reader truncated at the fence and the base reader skipped
    it, so the two disagreed and an honest edit came back as a deleted row."""
    d, p = git_repo(tmp_path, CANONICAL)
    text = open(p, encoding="utf-8").read()
    with open(p, "w", encoding="utf-8") as f:
        f.write(
            text.replace(
                "| how the gate renders in a TUI | user, on the next session |\n",
                "| how the gate renders in a TUI | user, on the next session |\n"
                "\n```\nan example\n```\n\n",
            )
        )
    assert run([str(d), "--baseline", "HEAD"]) == 0


def test_deleting_the_whole_file_fails_the_baseline(tmp_path, capsys):
    """Deleting the file was cheaper and quieter than deleting one row from
    it: the scan walks the current tree, so a file that is gone never enters
    the comparison at all."""
    d, p = git_repo(tmp_path, CANONICAL)
    # A second overview, so the scan is not empty and cannot exit 2 instead.
    other = d / "specs" / "1780000001-other"
    other.mkdir(parents=True)
    (other / "overview.md").write_text("# o\n\n" + CANONICAL, encoding="utf-8")
    subprocess.run(["git", "-C", str(d), "add", "-A"], check=True, capture_output=True)
    subprocess.run(
        ["git", "-C", str(d), "commit", "-qm", "two"], check=True, capture_output=True
    )
    os.remove(p)
    assert run([str(d), "--baseline", "HEAD"]) == 1
    assert "present at HEAD and not here" in capsys.readouterr().out


def test_renaming_the_work_item_directory_fails_the_baseline(tmp_path, capsys):
    """A rename is indistinguishable from a deletion here, and saying so out
    loud is the right default: Q5 fixed the filename, so a legitimate rename
    of one of these is rare."""
    d, p = git_repo(tmp_path, CANONICAL)
    os.rename(os.path.dirname(p), os.path.join(str(d), "specs", "1780000000-renamed"))
    assert run([str(d), "--baseline", "HEAD"]) == 1
    assert "present at HEAD and not here" in capsys.readouterr().out


def test_a_baseline_ref_that_does_not_resolve_exits_2(tmp_path, capsys):
    """The comparison silently did nothing and the run passed. In CI that is
    one shallow checkout away: the base branch is not there, every file reads
    as new, and the deletion check reports success without running."""
    d, _ = git_repo(tmp_path, CANONICAL)
    assert run([str(d), "--baseline", "origin/nosuchbranch"]) == 2
    assert "does not resolve" in capsys.readouterr().err


@pytest.mark.parametrize("invisible", ["️", "​", "⁠"])
def test_an_invisible_character_does_not_turn_a_bare_word_into_a_closing(
    tmp_path, invisible
):
    """`| closed\\u200b | done |` pastes in from anywhere, and on screen it is
    the bare word this refuses. `.strip()` does not remove any of these."""
    section = CANONICAL.replace(
        "| how the gate renders in a TUI | user, on the next session |",
        f"| {CLOSED_MARK}{invisible} | done |",
    )
    _, _, err = uc.check_file(write(tmp_path, section))
    assert err and "bare" in err[0][1]


def test_the_wrapper_is_present_and_executable():
    """bin/ lands on the Bash tool's PATH while the plugin is enabled, so the
    wrapper resolves the script relative to itself and a .cmd sibling ships
    for the platform that cannot run a POSIX shebang."""
    posix = os.path.join(ROOT, "bin", "unverified-check")
    windows = os.path.join(ROOT, "bin", "unverified-check.cmd")
    assert os.path.isfile(posix), "bin/unverified-check missing"
    assert os.path.isfile(windows), "bin/unverified-check.cmd missing"
    assert os.access(posix, os.X_OK), "bin/unverified-check not executable"
    assert os.path.isfile(SCRIPT), "the wrapper points at a missing script"


# --- round 3: the two comparisons had doors of their own -----------------------


def test_a_symlinked_path_still_compares(tmp_path):
    """`git rev-parse --show-toplevel` answers with links resolved and
    `abspath` does not, so reaching the tree through one — `/tmp` on macOS,
    a code directory linked from home — made every repo-relative path match
    no line of `ls-tree`. Both comparisons then did nothing and passed."""
    d, p = git_repo(tmp_path, CANONICAL)
    link = tmp_path / "link"
    symlink_or_skip(str(d), str(link))
    text = open(p, encoding="utf-8").read()
    with open(p, "w", encoding="utf-8") as f:
        f.write(
            text.replace(
                "| whether Windows hooks fire | a maintainer with a Windows machine |\n",
                "",
            )
        )
    assert run([str(link), "--baseline", "HEAD"]) == 1


def test_a_tracked_overview_under_a_skipped_directory_is_not_read_as_deleted(tmp_path):
    """The scan skips build/ and node_modules/; the base listing did not. A
    tracked overview.md under one of them was absent from every scan and so
    reported deleted on every run — a red build the author could only clear
    by renaming the directory."""
    d, _ = git_repo(tmp_path, CANONICAL)
    buried = d / "build" / "x"
    buried.mkdir(parents=True)
    (buried / "overview.md").write_text("# b\n\n" + CANONICAL, encoding="utf-8")
    subprocess.run(["git", "-C", str(d), "add", "-A"], check=True, capture_output=True)
    subprocess.run(
        ["git", "-C", str(d), "commit", "-qm", "build"], check=True, capture_output=True
    )
    assert run([str(d), "--baseline", "HEAD"]) == 0


def test_deleting_every_overview_reports_the_deletion_not_an_empty_scan(
    tmp_path, capsys
):
    """The scan finding nothing used to exit 2 saying "nothing was checked",
    which reads as a mistyped argument rather than a record that just left. A
    repository with one work item reaches this by deleting one file."""
    d, p = git_repo(tmp_path, CANONICAL)
    os.remove(p)
    assert run([str(d), "--baseline", "HEAD"]) == 1
    assert "present at HEAD and not here" in capsys.readouterr().out


def test_a_row_of_invisible_cells_is_not_an_open_item(tmp_path):
    """Two zero-width spaces read as "not empty" and counted as an item
    nobody can see. Against the row-count comparison that is a way to delete
    a real row and keep the number."""
    section = CANONICAL.replace(
        "| how the gate renders in a TUI | user, on the next session |",
        "| ​ | ​ |",
    )
    _, _, err = uc.check_file(write(tmp_path, section))
    assert err and "empty cell" in err[0][1]


def test_a_separator_hidden_by_an_invisible_character_is_still_a_separator(tmp_path):
    """`|-​--|---|` misses the separator pattern, so the row that round 1
    refused to count as an item came back as one."""
    section = CANONICAL + "|-​--|---|\n"
    _, _, err = uc.check_file(write(tmp_path, section))
    assert err and "one table" in err[0][1]


def test_an_unreadable_section_does_not_also_report_a_deletion(tmp_path, capsys):
    """A misspelt heading returns zero rows, and comparing that zero told the
    author to restore rows that are still sitting in the file."""
    d, p = git_repo(tmp_path, CANONICAL)
    text = open(p, encoding="utf-8").read()
    with open(p, "w", encoding="utf-8") as f:
        f.write(text.replace("## Not verified", "## Not verified (who must answer)"))
    assert run([str(d), "--baseline", "HEAD"]) == 1
    out = capsys.readouterr().out
    assert "no `## Not verified` section" in out
    assert "rows at HEAD" not in out, "the rows never left the file"


def test_a_tilde_fence_is_a_fence(tmp_path):
    """CommonMark accepts `~~~`, and an example wrapped in one used to be read
    as rows — a red build on an honest document whose only remedy was to
    change fence style."""
    section = (
        CANONICAL
        + "\n~~~markdown\n| Item | Who must answer |\n~~~\n\n| a third item | someone |\n"
    )
    op, _, err = uc.check_file(write(tmp_path, section))
    assert not err, err
    assert len(op) == 3


# --- round 4: one reader, and the pairs it retires ---------------------------


def test_a_second_not_verified_heading_is_not_counted_by_the_base_reader(tmp_path):
    """The loose reader counted every heading that mentioned "not verified",
    the strict one counted the canonical section, and a file holding both
    reported a deletion nobody had made. The author's only remedy was to
    rename a heading that was never this tool's business."""
    section = (
        CANONICAL + "\n### Not verified on Windows\n\n| a | b |\n|---|---|\n| x | y |\n"
    )
    d, _ = git_repo(tmp_path, section)
    assert run([str(d), "--baseline", "HEAD"]) == 0


def test_an_invisible_separator_in_the_base_is_not_counted_as_a_row(tmp_path):
    """The cell normalization landed in one reader and not the other, so a
    zero-width space in the base made a separator count as a row there and
    not here — a deletion report on a file nobody touched."""
    hidden = CANONICAL.replace("|---|---|", "|-​--|---|")
    d, p = git_repo(tmp_path, hidden)
    with open(p, "w", encoding="utf-8") as f:
        f.write("# w — overview\n\n" + CANONICAL)
    assert run([str(d), "--baseline", "HEAD"]) == 0


def test_a_tracked_symlink_is_not_reported_as_deleted(tmp_path):
    """`ls-tree` lists a tracked link under its own path. Resolving every
    scanned file — the round-2 fix, applied one level too deep — made a link
    that is right there read as gone."""
    d, _ = git_repo(tmp_path, CANONICAL)
    linked = d / "specs" / "1780000001-link"
    linked.mkdir()
    symlink_or_skip(
        os.path.join("..", "1780000000-work", "overview.md"),
        str(linked / "overview.md"),
    )
    subprocess.run(["git", "-C", str(d), "add", "-A"], check=True, capture_output=True)
    subprocess.run(
        ["git", "-C", str(d), "commit", "-qm", "link"], check=True, capture_output=True
    )
    assert run([str(d), "--baseline", "HEAD"]) == 0


def test_a_deleted_scan_path_is_compared_not_called_a_bad_argument(tmp_path, capsys):
    """The workflow runs `--baseline origin/<base> seal/specs/`. A change that
    deletes the scan path wholesale was told it had mistyped an argument, while
    the    record it removed went unmentioned."""
    d, _ = git_repo(tmp_path, CANONICAL)
    subprocess.run(["rm", "-rf", str(d / "specs")], check=True)
    assert run([str(d / "specs"), "--baseline", "HEAD"]) == 1
    assert "present at HEAD and not here" in capsys.readouterr().out


def test_deleting_a_file_through_a_symlinked_path_is_caught(tmp_path):
    """The row check and the file check resolve paths separately, so the
    symlink case has to be shown for both. The sibling test above deletes a
    row; this one deletes the file."""
    d, p = git_repo(tmp_path, CANONICAL)
    other = d / "specs" / "1780000001-other"
    other.mkdir(parents=True)
    (other / "overview.md").write_text("# o\n\n" + CANONICAL, encoding="utf-8")
    subprocess.run(["git", "-C", str(d), "add", "-A"], check=True, capture_output=True)
    subprocess.run(
        ["git", "-C", str(d), "commit", "-qm", "two"], check=True, capture_output=True
    )
    link = tmp_path / "link"
    symlink_or_skip(str(d), str(link))
    os.remove(p)
    assert run([str(link), "--baseline", "HEAD"]) == 1


def reported_paths(out):
    """The path each report line names, in EITHER output shape.

    `annotate` emits `::error file=<path>,line=<n>::…` when `GITHUB_ACTIONS` is
    set and `<path>:<line>  …` anywhere else. This test read only the second
    shape, so it passed on a developer's machine and failed in the only place
    the check actually runs — 1 failed, 524 passed on all three runners, while
    the same tree was green locally. `run`'s own docstring says a test here
    asserts what CI would see; reading one of the two shapes is how that stopped
    being true.
    """
    found = []
    for ln in out.splitlines():
        if ln.startswith("::"):
            _, _, rest = ln.partition(" file=")
            path, _, _ = rest.partition(",line=")
            if path:
                found.append(path)
        elif "overview.md:" in ln:
            found.append(ln.split(":")[0])
    return found


@pytest.mark.parametrize("in_ci", [False, True])
def test_both_deletion_reports_name_paths_on_the_same_footing(
    tmp_path, capsys, monkeypatch, in_ci
):
    """One line came from `relpath(path, cwd)` and the other from `ls-tree`'s
    repo-relative path. They agreed only when the command ran at the
    repository root, and the README hands this command to users.

    Run in both output shapes, because the paths are the subject and the shape
    is not — and because pinning one shape is what let this pass everywhere
    except CI.
    """
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
    if in_ci:
        monkeypatch.setenv("GITHUB_ACTIONS", "true")
    d, p = git_repo(tmp_path, CANONICAL)
    other = d / "specs" / "1780000001-other"
    other.mkdir(parents=True)
    (other / "overview.md").write_text("# o\n\n" + CANONICAL, encoding="utf-8")
    subprocess.run(["git", "-C", str(d), "add", "-A"], check=True, capture_output=True)
    subprocess.run(
        ["git", "-C", str(d), "commit", "-qm", "two"], check=True, capture_output=True
    )
    os.remove(p)  # the file check reports this one
    text = open(other / "overview.md", encoding="utf-8").read()
    with open(other / "overview.md", "w", encoding="utf-8") as f:
        f.write(
            text.replace("| whether Windows hooks fire", "| closed whether Windows")
        )
        # closed, not deleted -- now drop a row so the row check reports too
    with open(other / "overview.md", "w", encoding="utf-8") as f:
        f.write(
            text.replace(
                "| whether Windows hooks fire | a maintainer with a Windows machine |\n",
                "",
            )
        )

    here = os.getcwd()
    os.chdir(str(d / "specs"))
    try:
        assert run([".", "--baseline", "HEAD"]) == 1
        paths = reported_paths(capsys.readouterr().out)
    finally:
        os.chdir(here)
    assert len(paths) == 2, paths
    assert all(q.startswith("1780000") for q in paths), paths


# --- round 5: what the matcher argument left to settle ------------------------


def test_a_path_two_levels_gone_still_names_its_repository(tmp_path, capsys):
    """`repo_root` steps back one level on its own, so this only earns its
    place deeper than that — and `specs/<item>/` is exactly two."""
    d, _ = git_repo(tmp_path, CANONICAL)
    gone = d / "specs" / "1780000000-work"
    subprocess.run(["rm", "-rf", str(gone)], check=True)
    assert run([str(gone / "overview.md"), "--baseline", "HEAD"]) == 1
    assert "present at HEAD and not here" in capsys.readouterr().out


def test_a_mistyped_path_is_still_a_mistyped_path(tmp_path, capsys):
    """The guard was narrowed so a deleted scan path could be compared, and
    that let `specs/ spces/` pass in silence. A path with nothing under it at
    the base is a typo, not a question."""
    d, _ = git_repo(tmp_path, CANONICAL)
    assert run([str(d / "specs"), str(d / "spces"), "--baseline", "HEAD"]) == 2
    assert "nothing under it" in capsys.readouterr().err


def test_a_tracked_symlink_is_counted_once(tmp_path, capsys):
    """One record, two paths. Counting both doubles its open items, and
    dropping one from the presence check reports a file that is right there
    as deleted — so the two questions are answered differently on purpose."""
    d, _ = git_repo(tmp_path, CANONICAL)
    linked = d / "specs" / "1780000001-link"
    linked.mkdir()
    symlink_or_skip(
        os.path.join("..", "1780000000-work", "overview.md"),
        str(linked / "overview.md"),
    )
    subprocess.run(["git", "-C", str(d), "add", "-A"], check=True, capture_output=True)
    subprocess.run(
        ["git", "-C", str(d), "commit", "-qm", "link"], check=True, capture_output=True
    )
    assert run([str(d), "--baseline", "HEAD"]) == 0
    out = capsys.readouterr().out
    assert "1 overviews · 2 open" in out, out


def test_the_summary_names_how_many_were_not_compared(tmp_path, capsys):
    """The tally is the line most readers stop at, so a file left out of the
    comparison has to be visible there and not only in the block below."""
    d, p = git_repo(tmp_path, "## Not verified\n\n- prose at the base\n")
    with open(p, "w", encoding="utf-8") as f:
        f.write("# w — overview\n\n" + CANONICAL)
    assert run([str(d), "--baseline", "HEAD"]) == 0
    assert "· 1 not compared" in capsys.readouterr().out


def test_a_legacy_column_name_in_the_base_is_read_but_not_in_the_tree(tmp_path):
    """The four files this branch normalized renamed the column as well as the
    heading, so relaxing the heading alone would still have stopped comparing
    them. The relaxation is the base's alone: the working tree is held to the
    exact header, or the spelling drifts back in through the front door."""
    legacy = CANONICAL.replace("## Not verified", "## Not verified (who must answer)")
    legacy = legacy.replace("| Item | Who must answer |", "| Item | Who |")
    d, p = git_repo(tmp_path, legacy)
    text = open(p, encoding="utf-8").read()
    with open(p, "w", encoding="utf-8") as f:
        f.write(
            text.replace("## Not verified (who must answer)", "## Not verified")
            .replace("| Item | Who |", "| Item | Who must answer |")
            .replace(
                "| whether Windows hooks fire | a maintainer with a Windows machine |\n",
                "",
            )
        )
    assert run([str(d), "--baseline", "HEAD"]) == 1

    _, _, tree_errors = uc.check_text(legacy.replace(" (who must answer)", ""))
    assert tree_errors and "header is" in tree_errors[0][1]


def test_the_legacy_read_still_wants_an_item_column(tmp_path):
    """A relaxation with no floor reads any two-column table as the record."""
    odd = CANONICAL.replace("| Item | Who must answer |", "| Thing | Who |")
    _, _, errors = uc.check_text(odd, heading=uc.LOOSE_HEADING, strict_header=False)
    assert errors and "header is" in errors[0][1]


# --- the two path dialects: what git is told, and what the caller is shown ----


def test_a_path_handed_to_git_is_spelled_the_way_git_spells_it(monkeypatch):
    r"""Repo-relative paths are built with `os.path.relpath` and then spent as
    `git show <ref>:<rel>` and compared against `ls-tree` output. git answers
    and accepts `/` on every platform, so on Windows the two sides were built
    by two rules: `show` returned None and the row check silently compared
    nothing, while the presence check matched no path and called every tracked
    overview deleted.

    The substitution is asserted with `os.sep` monkeypatched, because
    `git_path` reads it at call time. Round 1 was right that the `os.path.join`
    form alone asserts `x == x` on the three POSIX legs, so the branch it
    exists for was bound on Windows only -- which is the shape this work item
    is otherwise about removing."""
    joined = os.path.join("specs", "1780000000-work", "overview.md")
    assert uc.git_path(joined) == "specs/1780000000-work/overview.md"

    # The Windows branch, on every platform.
    monkeypatch.setattr(os, "sep", "\\")
    assert uc.git_path("specs\\1780000000-work\\overview.md") == (
        "specs/1780000000-work/overview.md"
    )
    # Idempotent there too: `overviews_at` returns git's spelling and a path
    # that already came from git goes through here unchanged.
    assert uc.git_path("specs/1780000000-work/overview.md") == (
        "specs/1780000000-work/overview.md"
    )

    # And the POSIX branch does NOT substitute, so a backslash that is part of
    # a real filename survives.
    monkeypatch.setattr(os, "sep", "/")
    assert uc.git_path("specs/odd\\name.md") == "specs/odd\\name.md"


def test_a_report_survives_a_path_with_no_relative_form(monkeypatch):
    r"""`os.path.relpath` raises on Windows when the two paths are on different
    drives -- measured: `ValueError: path is on mount 'D:', start on mount
    'C:'`. It is the reporting footing for every line the tool prints, so a run
    with the workspace and the temp directory on two volumes died before
    printing a single row.

    Driven by making `relpath` raise rather than by finding two drives, so the
    ubuntu leg runs this case too."""

    def refuses(path, start=None):
        raise ValueError("path is on mount 'D:', start on mount 'C:'")

    monkeypatch.setattr(os.path, "relpath", refuses)
    where = os.path.abspath(os.path.join("x", "overview.md"))
    assert uc.display_path(where, os.path.abspath("y")) == where
    # The git-facing half answers None instead, because there is no
    # repo-relative form of a path that is not in the repository.
    assert uc.repo_relative(where, os.path.abspath("y")) is None


def test_a_path_on_another_volume_stops_the_run_instead_of_aborting_it(
    tmp_path, monkeypatch, capsys
):
    r"""Round 1, finding 2: `display_path` guarded the two reporting sites and
    the four git-facing ones kept a bare `relpath`. Executed then, the run
    printed one row and died mid-report with the same `ValueError` the helper
    existed to prevent.

    Every argument is read against ONE repository, the one the first argument
    is in. That was always the rule and nothing stated it, so this says it: a
    path with no relative form to that root is not in it, and the answer is
    exit 2 with the path named, not a traceback and not a silent zero.

    The raise is induced rather than found, so this runs on every leg. It is
    scoped to the second argument, so everything the first one needs still
    resolves and the case reaches the check rather than falling over earlier."""
    d, _ = git_repo(tmp_path, CANONICAL)
    elsewhere = tmp_path / "elsewhere"
    (elsewhere / "specs").mkdir(parents=True)

    real_relpath = os.path.relpath

    def refuses_for_elsewhere(path, start=None):
        if "elsewhere" in str(path):
            raise ValueError("path is on mount 'D:', start on mount 'C:'")
        return real_relpath(path, start)

    monkeypatch.setattr(os.path, "relpath", refuses_for_elsewhere)
    assert run([str(d), str(elsewhere), "--baseline", "HEAD"]) == 2
    err = capsys.readouterr().err
    assert "is not in" in err and "another volume" in err, err


# --- #272: the baseline is the pull request's base, and the base moves -------


def forked(tmp_path, section=CANONICAL):
    """A repository whose `base` and `work` branches sit on one fork point.

    Checked out on `work`, which is where a feature branch lives. Each case
    below moves `base` forward the way a release branch does when another work
    item squashes into it, and then asks what THIS branch removed."""
    d = tmp_path / "repo"
    shutil.copytree(_bare_inited_repo_template(), d)

    def git(*a):
        subprocess.run(["git", "-C", str(d), *a], check=True, capture_output=True)

    p = write(d, section)
    git("add", "-A")
    git("commit", "-qm", "the fork point")
    git("branch", "base")
    git("switch", "-q", "-c", "work")
    return d, p, git


def squash_a_sibling_into_the_base(d, git, name="1780000001-squashed-sibling"):
    """What the base branch does when another work item is squashed into it.

    The sibling's `overview.md` is then at the base and was never on this
    branch at all -- which is the whole of #272."""
    git("switch", "-q", "base")
    other = d / "specs" / name
    other.mkdir(parents=True)
    (other / "overview.md").write_text(
        f"# {name} — overview\n\n" + CANONICAL, encoding="utf-8"
    )
    git("add", "-A")
    git("commit", "-qm", "another work item, squashed into the base")
    git("switch", "-q", "work")


def short(d, ref="HEAD"):
    out = subprocess.run(
        ["git", "-C", str(d), "rev-parse", ref],
        check=True,
        capture_output=True,
        encoding="utf-8",
    )
    return out.stdout.strip()[:7]


@pytest.mark.rule("one-merge-base")
def test_a_work_item_squashed_after_the_fork_is_not_this_branchs_removal(
    tmp_path, capsys
):
    """#272, and the case the repair exists for. On 0.9.2 three of four
    branches met this: the moment one work item squashed into the release
    branch, every sibling cut before that squash read the squashed item's
    `overview.md` as rows that left the record. The message was right about
    what it measured and wrong about what happened -- nothing left, the base
    moved.

    The merge base is the last commit this branch and the base agreed on, so a
    file present there and absent here was removed by this branch. A file that
    arrived on the base after the fork is not this branch's business."""
    d, _, git = forked(tmp_path)
    squash_a_sibling_into_the_base(d, git)
    assert run([str(d), "--baseline", "base"]) == 0
    out = capsys.readouterr().out
    assert "left the record" not in out, out
    assert "squashed-sibling" not in out, out


def test_the_moved_base_does_not_excuse_this_branchs_own_deletion(tmp_path, capsys):
    """The control. Without it the repair is indistinguishable from making the
    arm inert, which is the direction that loses a real removal.

    Same moved base, and this branch really did delete its own record."""
    d, p, git = forked(tmp_path)
    squash_a_sibling_into_the_base(d, git)
    os.remove(p)
    assert run([str(d), "--baseline", "base"]) == 1
    out = capsys.readouterr().out
    assert "1780000000-work" in out, out
    # And still only its own: the sibling is not reported alongside it.
    assert "squashed-sibling" not in out, out


@pytest.mark.rule("one-merge-base")
def test_a_row_the_base_gained_after_the_fork_is_not_a_deletion(tmp_path, capsys):
    """The row-count arm reads the base revision too, through
    `git show <ref>:<path>`, so it is in the same class as the arm the ticket
    names -- the ticket's own repair section says otherwise, and that is what
    reading it rather than assuming it settles (questions.md Q1).

    Reachable the moment the base gains a row in THIS branch's overview after
    the fork: a row closed on the base, or one added there by a later work
    item."""
    d, p, git = forked(tmp_path)
    git("switch", "-q", "base")
    text = open(p, encoding="utf-8").read()
    with open(p, "w", encoding="utf-8") as f:
        f.write(text + "| whether the hooks fire on Windows | the same maintainer |\n")
    git("add", "-A")
    git("commit", "-qm", "a third row, on the base")
    git("switch", "-q", "work")
    assert run([str(d), "--baseline", "base"]) == 0
    out = capsys.readouterr().out
    assert "left the record" not in out, out


def test_the_moved_base_does_not_excuse_a_deleted_row(tmp_path, capsys):
    """The row arm's control, for the same reason as the file arm's."""
    d, p, git = forked(tmp_path)
    squash_a_sibling_into_the_base(d, git)
    text = open(p, encoding="utf-8").read()
    with open(p, "w", encoding="utf-8") as f:
        f.write(
            text.replace(
                "| whether Windows hooks fire | a maintainer with a Windows machine |\n",
                "",
            )
        )
    assert run([str(d), "--baseline", "base"]) == 1
    assert "2 rows at" in capsys.readouterr().out


def test_a_moved_base_report_names_the_merge_base_it_compared(tmp_path, capsys):
    """A refusal is read and acted on, so it names the revision it actually
    compared against -- in the shortest form that is true. Naming `base` here
    would send the reader to a commit this run never opened.

    The sibling cases above assert the other half: with `--baseline HEAD`, the
    ref IS the merge base, so the ref's own name is the true short form and
    every earlier case still reads `present at HEAD and not here`."""
    d, p, git = forked(tmp_path)
    squash_a_sibling_into_the_base(d, git)
    os.remove(p)
    assert run([str(d), "--baseline", "base"]) == 1
    out = capsys.readouterr().out
    assert f"the merge-base of base and HEAD ({short(d)})" in out, out
    assert "present at base and not here" not in out, out


def test_a_base_that_is_the_merge_base_is_named_by_its_ref_alone(tmp_path, capsys):
    """The shortest true form, stated as its own case rather than left to the
    earlier ones. Where the ref's commit IS the merge base -- every local run
    against `HEAD`, and CI, where the checkout is the merge of the head into
    the base -- the extra words carry nothing."""
    d, p, _ = forked(tmp_path)
    os.remove(p)
    assert run([str(d), "--baseline", "base"]) == 1
    out = capsys.readouterr().out
    assert "present at base and not here" in out, out
    assert "merge-base" not in out, out


def test_a_baseline_that_shares_no_history_with_head_exits_2(tmp_path, capsys):
    """A comparison against nothing is not a comparison -- the same answer the
    module already gives for a ref that does not resolve. Without a common
    commit there is no question of the form "what did THIS branch remove", so
    there is nothing to degrade to.

    A shallow clone whose base ref resolves while the common ancestor sits
    beyond the graft lands here too. Both workflows set `fetch-depth: 0`;
    questions.md Q2 carries the case that does not."""
    d, _, git = forked(tmp_path)
    git("switch", "-q", "--orphan", "unrelated")
    (d / "readme.md").write_text("no commit in common\n", encoding="utf-8")
    git("add", "-A")
    git("commit", "-qm", "an unrelated root")
    git("switch", "-q", "work")
    assert run([str(d), "--baseline", "unrelated"]) == 2
    err = capsys.readouterr().err
    assert "share no history" in err, err
    assert "nothing was compared" in err, err


def test_a_scan_path_that_only_the_base_ever_had_is_a_mistyped_argument(
    tmp_path, capsys
):
    """The missing-path arm asks the same `overviews_at` question, so it moves
    with the other two rather than being left on the tip.

    A path this branch never had, and that the fork point never held either,
    is a mistyped argument from this branch — whatever the base's tip carries
    now. Left on the tip it read as a work item this branch had deleted, which
    is #272 arriving through the third door."""
    d, _, git = forked(tmp_path)
    squash_a_sibling_into_the_base(d, git)
    gone = d / "specs" / "1780000001-squashed-sibling"
    assert run([str(gone), "--baseline", "base"]) == 2
    err = capsys.readouterr().err
    assert "no such path" in err, err


def test_a_merge_base_that_answers_with_nothing_is_not_a_comparison(
    tmp_path, monkeypatch, capsys
):
    """`git merge-base` answering exit 0 with an empty line is not a revision,
    and an empty string reaching `git ls-tree` lists nothing — the silent zero
    this whole module refuses, reached through the one code path that cannot
    be driven by a fixture.

    Induced rather than found, the way the `relpath` cases below are, so it
    runs on every leg. No git this repository requires answers that way; the
    guard is here because the alternative to a guard is a pass."""
    d, _, git = forked(tmp_path)
    squash_a_sibling_into_the_base(d, git)
    real_run = subprocess.run

    def empty_merge_base(argv, *a, **kw):
        if isinstance(argv, list) and "merge-base" in argv:
            return subprocess.CompletedProcess(argv, 0, "\n", "")
        return real_run(argv, *a, **kw)

    monkeypatch.setattr(uc.subprocess, "run", empty_merge_base)
    assert run([str(d), "--baseline", "base"]) == 2
    assert "share no history" in capsys.readouterr().err


def test_a_ref_that_resolves_to_nothing_is_a_ref_that_does_not_resolve(
    tmp_path, monkeypatch, capsys
):
    """`commit_of` answers two questions at once — whether the ref resolves and
    which commit it is — and `chain_check.py` loads it for the first through
    `resolves`. `rev-parse --verify --quiet` exits 1 for a name it cannot find,
    so the empty-output guard is reached only by a git that exits 0 and prints
    nothing, and a mutation loop found it the one branch here no fixture drives.

    Induced, like the merge-base case above and the `relpath` cases below. What
    it pins is that an empty answer is a refusal rather than a truthy sentinel
    travelling into `base_label` and out to `chain_check.py` as a resolved
    ref."""
    d, _, _ = forked(tmp_path)
    real_run = subprocess.run

    def empty_verify(argv, *a, **kw):
        if isinstance(argv, list) and "--verify" in argv:
            return subprocess.CompletedProcess(argv, 0, "\n", "")
        return real_run(argv, *a, **kw)

    monkeypatch.setattr(uc.subprocess, "run", empty_verify)
    assert uc.resolves(str(d), "base") is False
    assert run([str(d), "--baseline", "base"]) == 2
    assert "does not resolve" in capsys.readouterr().err


# The phrase each language's files use for the base's tip, where CI's
# comparison lands (#612).
TIP_EN = "the base's tip"
TIP_KO = "base 브랜치의 끝"


@pytest.mark.parametrize(
    "doc, tip, false_sentence",
    [
        ("README.md", TIP_EN, None),
        ("README.ko.md", TIP_KO, None),
        # True at both places without naming either, and so not held to the tip
        # (`seal/specs/1790381329-the-deferred-sentences-and-pins/spec.md`,
        # *Out of scope*): a sibling squashed after this branch was cut is not
        # its removal on a branch checkout or at the merge ref.
        (os.path.join("docs", "release-checklist.md"), None, None),
        (os.path.join("skills", "verify", "SKILL.md"), TIP_EN, None),
        (os.path.join(".github", "workflows", "hygiene.yml"), TIP_EN, None),
        (os.path.join("templates", "hygiene.yml"), TIP_EN, None),
        # The module's docstrings (#612). The phrase stands here three times,
        # so this row cannot see the `--baseline` help alone go back to the
        # fork point; `test_the_baseline_help_names_both_places` renders it.
        (
            os.path.join("skills", "verify", "scripts", "unverified_check.py"),
            TIP_EN,
            None,
        ),
    ],
    ids=posix_id,
)
def test_the_documents_state_the_merge_base_footing(doc, tip, false_sentence):
    """Eight files told a reader that `--baseline` compares against the base
    revision; #272 made it compare against `git merge-base REF HEAD`. A
    corrected behaviour whose old sentence survives somewhere else is #180's
    class, and these files are where this one could survive.

    That commit is the fork point on a branch checkout -- a local run, the
    broad gate's -- and the base's tip in CI, whose checkout of a pull request
    is the head already merged into the base. The files said only the first
    and placed it in CI (#612), and two of them said CI never compares at the
    tip, which is false. So each file that places the comparison names the
    base's tip too, in one phrase per language, and the false sentence is
    asserted gone where it stood.

    Positive assertions, the way `test_the_skill_states_the_closing_convention`
    is: the sentence has to be there, rather than one old wording having to be
    absent, because the old wording had several phrasings. Nothing else in
    these files had reason to name a merge base."""
    text = open(os.path.join(ROOT, doc), encoding="utf-8").read()
    assert "merge-base" in text or "merge base" in text, (
        f"{doc} describes `unverified-check --baseline` and does not say the "
        "comparison is against the merge base"
    )
    flat_text = " ".join(text.replace("#", " ").split())
    if tip:
        assert tip in flat_text, (
            f"{doc} does not say that in CI the merge base is the base's tip"
        )
    if false_sentence:
        assert false_sentence not in flat_text, (
            f"{doc} still says CI never compares at the base's tip"
        )


def test_the_baseline_help_names_both_places(capsys):
    """#612: the `--baseline` help is a rendered line (contract §14). The
    documents case above reads the whole file, where the module docstring and
    `merge_base`'s docstring carry the same phrase, so it cannot see the help
    go back to the fork point. The help is rendered and read on its own. Red
    with the tip dropped from the help alone (round 1's 🟡 2)."""
    with pytest.raises(SystemExit):
        uc.main(["--help"])
    rendered = " ".join(capsys.readouterr().out.split())
    assert "the fork point on a branch checkout and the base's tip in CI" in rendered, (
        rendered
    )


# --- a settle is not this branch's deletion ---------------------------------

DOC = "# a\n\n## S\n\nAn old rule.\n"


def rule(text):
    return f"- add\n  file: docs/a.md\n  section: S\n  to: {text}\n"


def settle_repo(tmp_path, changes):
    """Work items with a closed memo and a spec, committed over `docs/a.md`.
    CHANGES maps each id to its `## Rule changes` body, or None for a spec
    written before the section existed. Returns the repository."""
    d = tmp_path / "repo"
    shutil.copytree(_bare_inited_repo_template(), d)
    (d / "docs").mkdir()
    (d / "docs" / "a.md").write_text(DOC, encoding="utf-8")
    for name, body in changes.items():
        item = d / "specs" / name
        item.mkdir(parents=True)
        (item / "overview.md").write_text(f"# o\n\n{CLOSED_SECTION}", encoding="utf-8")
        section = "" if body is None else f"\n## Rule changes\n\n{body}"
        (item / "spec.md").write_text(f"# {name}\n{section}", encoding="utf-8")
    subprocess.run(["git", "-C", str(d), "add", "-A"], check=True, capture_output=True)
    subprocess.run(
        ["git", "-C", str(d), "commit", "-qm", "specs"], check=True, capture_output=True
    )
    return d


def remove(d, *names, docs=DOC):
    """Remove each work item's directory whole, and write `docs/a.md` as DOCS."""
    for name in names:
        shutil.rmtree(d / "specs" / name)
    (d / "docs" / "a.md").write_text(docs, encoding="utf-8")


@pytest.mark.rule("a-settle-is-no-deletion")
def test_a_settled_work_item_is_not_read_as_this_branchs_deletion(tmp_path, capsys):
    """S9. A released directory removed whole, with nothing open, whose rule
    changes `docs/` holds, is a settle and not this branch's deletion. It is
    named rather than passed over in silence."""
    d = settle_repo(tmp_path, {"1780000001-a": rule("A new rule.")})
    remove(d, "1780000001-a", docs=DOC + "\nA new rule.\n")
    assert run([str(d), "--baseline", "HEAD"]) == 0
    out = capsys.readouterr().out
    assert "present at HEAD and not here" not in out, out
    assert "1 settled" in out and "1780000001-a" in out.split("settled —")[1], out


@pytest.mark.rule("a-settle-is-no-deletion")
def test_a_removal_whose_rule_docs_does_not_hold_still_fails(tmp_path, capsys):
    """S10, and the half that keeps the predicate from being a way past the
    check: two directories leave together, and `docs/` holds only one of
    their rules."""
    d = settle_repo(
        tmp_path,
        {"1780000001-a": rule("A new rule."), "1780000002-b": rule("Another rule.")},
    )
    remove(d, "1780000001-a", "1780000002-b", docs=DOC + "\nA new rule.\n")
    assert run([str(d), "--baseline", "HEAD"]) == 1
    out = capsys.readouterr().out
    deleted = out.split("rows left the record")[1]
    assert "1780000002-b" in deleted and "1780000001-a" not in deleted, out


@pytest.mark.rule("a-settle-is-no-deletion")
def test_a_spec_with_no_rule_changes_and_nothing_open_is_settled(tmp_path, capsys):
    """S11, Q2's answer (a): a spec written before the section existed states
    nothing to replay, so its removal with nothing open passes."""
    d = settle_repo(tmp_path, {"1780000001-a": None})
    remove(d, "1780000001-a")
    assert run([str(d), "--baseline", "HEAD"]) == 0, capsys.readouterr().out


def test_the_settled_line_reads_as_a_sentence(tmp_path, capsys):
    """§14: the line a person reads in the hygiene workflow's output."""
    d = settle_repo(tmp_path, {"1780000001-a": rule("A new rule.")})
    remove(d, "1780000001-a", docs=DOC + "\nA new rule.\n")
    run([str(d), "--baseline", "HEAD"])
    out = " ".join(capsys.readouterr().out.split())
    assert (
        "settled: at HEAD nothing in its record was open, and `docs/` holds "
        "every rule change its spec states"
    ) in out, out


MARKER = re.compile(r"^<!-- specs/(\S+) -->$")


def live_markers(body):
    """The marker ids on the live lines of BODY: `live_lines`, the one rule
    for whether a line is live, and a line-anchored marker as the changelog
    gather writes one."""
    return {
        found
        for line, live in uc.live_lines(uc.gfm_lines(body))
        if live
        for found in MARKER.findall(line)
    }


@pytest.mark.parametrize(
    "body, found",
    [
        ("<!-- specs/x-1 -->\n", {"x-1"}),
        ("```markdown\n<!-- specs/x-2 -->\n```\n", set()),
        ("~~~\n<!-- specs/x-3 -->\n~~~\n", set()),
        # A ``` inside a ```` block does not close it, which is CommonMark and
        # which `blank_fences` already implements — the reason this reuses
        # that reader instead of writing a second one.
        ("````\n```markdown\n<!-- specs/x-4 -->\n```\n````\n", set()),
        ("```\n<!-- specs/x-5 -->\n", set()),
        ("```\nx\n```\n<!-- specs/x-6 -->\n", {"x-6"}),
        ("see `<!-- specs/x-7 -->` here\n", set()),
    ],
)
def test_every_fence_shape_a_policy_document_can_carry(body, found):
    assert live_markers(body) == found


@pytest.mark.parametrize(
    "body, found",
    [
        # A marker is itself a comment, which is why the state a line STARTED
        # in is the question and the line's surviving text is not.
        ("<!-- specs/c-1 -->\n", {"c-1"}),
        ("<!-- parked\n<!-- specs/c-2 -->\n-->\n", set()),
        # The draft closes before the marker, so the marker is live again.
        ("<!-- parked\n-->\n<!-- specs/c-3 -->\n", {"c-3"}),
        # An unclosed comment runs to the end of the file.
        ("<!-- parked\n<!-- specs/c-4 -->\n", set()),
        # Opened and closed on one line before the marker on the next.
        ("<!-- a note --> and prose\n<!-- specs/c-5 -->\n", {"c-5"}),
        # Both ways of not being live at once.
        ("<!-- parked\n```\n<!-- specs/c-6 -->\n```\n-->\n", set()),
        # An opener quoted inside a code span is prose, not a draft. Three
        # top-level `docs/` documents quote the marker's shape inside
        # backticks today, each closed on its own line; one `<!--` alone in a
        # sentence would park every marker below it (round 3, finding 2).
        ("see `<!--` here\n<!-- specs/c-7 -->\n", {"c-7"}),
        # And its mirror. A CLOSER quoted inside a span is left alone, because
        # inside a comment nothing is markdown and the quotation really does
        # end the draft. So the marker below it is live and this IS a fold
        # record — the one shape where the narrowed pass reads MORE than the
        # pass that blanked every span. Deliberate, and pinned here so that a
        # later edit cannot take the direction back in silence.
        ("<!-- parked\nprose with `-->` in it\n<!-- specs/c-8 -->\n-->\n", {"c-8"}),
    ],
)
def test_every_comment_shape_a_policy_document_can_carry(body, found):
    assert live_markers(body) == found


def test_strip_comments_reads_through_the_one_comment_scanner(monkeypatch):
    """`strip_comments` keeps no private copy of the comment walk.

    It used to share `comment_scan` with `opens_outside_a_comment`, and this
    case was named for that pair. The pair is gone: `live_lines` carries the
    comment state itself now, so `comment_scan` has one reader left. What is
    still worth pinning is the half that has not changed — a second copy of
    the walk inside `strip_comments` would answer identically to the real one
    and no assertion comparing outputs could see it (round 3 of the parent
    chain, finding 4), so the scanner is replaced at module level and the
    reader has to answer from the stub."""
    lines = [
        "prose <!-- open",
        "still inside",
        "closed --> and prose again",
        "<!-- specs/x-1 -->",
    ]
    assert uc.strip_comments(lines) == [
        "prose ",
        "",
        " and prose again",
        "",
    ]
    monkeypatch.setattr(uc, "comment_scan", lambda lines: iter([(False, "SENTINEL")]))
    assert uc.strip_comments(lines) == ["SENTINEL"]


@pytest.mark.parametrize(
    "lines, kept",
    [
        # Round 1 of #1000, finding 2: a table cell quoting the opener in a
        # code span, as two merged guarantees do. The page shows code, and
        # the line after it is text.
        (["| `<!-- specs/` | y |", "Verdict: sealed"], None),
        # A double-backtick span holding a single backtick and the opener.
        (["a ``x `<!--` y`` b", "after"], None),
        # A run with no partner on its line is literal, so the opener after
        # it opens a comment, as before.
        (["a ` b <!-- c", "hidden", "--> d"], ["a ` b ", "", " d"]),
        # A span before a real comment on the same line.
        (["`a` <!-- c --> e", "x"], ["`a`  e", "x"]),
        # Inside a comment backticks are ordinary characters.
        (["<!-- `x --> y`", "z"], [" y`", "z"]),
    ],
)
def test_a_comment_opener_inside_a_code_span_opens_no_comment(lines, kept):
    """Round 1 of #1000, finding 2. CommonMark 6.1 gives a code span opened
    first precedence over an HTML comment inside it. Seen red against the
    scan that found the opener anywhere on a line: the first two blanked
    every line after the span."""
    assert uc.strip_comments(lines) == (lines if kept is None else kept)


def test_a_row_after_an_opener_quoted_in_a_code_span_is_counted(tmp_path):
    """Round 1 of #1000, the row it left to the fix pass: an open row of
    `## Not verified` below a row quoting the opener in a code span is
    counted, not hidden. Seen red against the scan that read the opener."""
    section = CANONICAL.replace(
        "| how the gate renders in a TUI |", "| whether `<!--` in a cell hides rows |"
    )
    op, _, err = uc.check_file(write(tmp_path, section))
    assert not err and len(op) == 2, (op, err)


def test_the_comment_scan_is_not_quadratic_in_backtick_runs():
    """A line of backtick runs, each without a partner of its own length,
    and one of runs that pair, are read in well under a second."""
    import time

    start = time.monotonic()
    uc.strip_comments(["".join("`" * k + "x" for k in range(1, 400)) + "<!--"])
    uc.strip_comments(["` " * 50000 + "<!--", "-->"])
    assert time.monotonic() - start < 1.0


@pytest.mark.parametrize(
    "line, opens",
    [
        # A comment opener inside a code span is a quotation and opens nothing.
        ("a `<!--` c", False),
        # A backtick string closes at the next one of EQUAL length, so the
        # single backtick inside this double-backtick span is span content and
        # the opener after it is still quoted.
        ("``a ` <!--`` c", False),
        # Closed span, then a real opener outside it.
        ("`a` <!-- b", True),
        # An unmatched backtick run is literal text, so the opener is real.
        ("`open <!--", True),
        ("no span <!--", True),
        ("no span at all", False),
    ],
)
def test_a_code_span_closes_at_a_backtick_string_of_equal_length(line, opens):
    """CommonMark 6.1's span rule, asked of the scan that now implements it:
    equal-length backtick strings, an unmatched one left literal. Observed
    where it matters rather than through a blanked string — whether the line
    leaves a comment open, which is what the next line's liveness answers."""
    answer = [live for _, live in uc.live_lines([line, "<!-- specs/x-1 -->"])]
    assert answer[0] is True
    assert answer[1] is not opens


def test_the_scan_decides_a_fence_before_a_comment_or_a_span():
    """Precedence, half one. A fence opener owns its whole line, so a comment
    opener or a backtick run on the same line is fenced content and opens
    nothing — and the lines inside the block are not live however they read."""
    lines = ["```markdown <!--", "<!-- specs/x-1 -->", "```", "<!-- specs/x-2 -->"]
    assert [live for _, live in uc.live_lines(lines)] == [True, False, False, True]


def test_the_first_delimiter_on_the_line_wins():
    """Precedence, half two. Where a comment opener and a backtick run are
    both ahead, whichever comes first in the text decides: the opener first
    parks what follows, the backtick run first quotes it."""
    run_first = [live for _, live in uc.live_lines(["x `<!--` y", "after"])]
    opener_first = [live for _, live in uc.live_lines(["x <!-- `y`", "after"])]
    assert run_first == [True, True]
    assert opener_first == [True, False]


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


def test_the_scan_never_reads_live_what_the_format_parks():
    """The safety direction, against a reading written from the format.

    Not full agreement: `live_lines` computes two readings and parks a line
    wherever they differ, so it deliberately parks lines the format calls
    live, and a case demanding agreement would forbid the thing that ends
    this class. What may never happen is the other direction — the scan
    calling a line live that the format parks — because a line read live
    there excuses or declares what nobody wrote live. Five review rounds each
    found one shape of exactly that.
    """
    unsafe, live_seen = [], 0
    for lines in documents_with_several_spans_on_a_line(2000):
        scan = [live for _, live in uc.live_lines(lines)]
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


@pytest.mark.parametrize(
    "name, body, found",
    [
        # Round 1. Inside a draft nothing is markdown, so the quoted closing
        # delimiter really ends it and the marker below is a fold record.
        (
            "a closer quoted alone inside a draft",
            "<!-- a draft, parked\nprose with `-->` in it\n<!-- specs/s-1 -->\n-->\n",
            {"s-1"},
        ),
        # Round 2. A span quoting a COMPLETE comment keeps its closer, for the
        # same reason: the quotation is not one while the draft is open.
        (
            "a whole comment quoted inside a draft",
            "<!-- a draft, parked\nends with `<!-- a note -->` whole\n<!-- specs/s-2 -->\n-->\n",
            {"s-2"},
        ),
        # Round 3. A closer and then an opener inside ONE span: the draft ends
        # and re-opens, so the marker begins inside it.
        (
            "a closer then an opener in one span",
            "<!-- a draft, parked\nquotes `--> and then <!--` here\n<!-- specs/s-3 -->\n-->\n",
            set(),
        ),
        # Round 4. The same pair in two different spans on one line.
        (
            "a closer and an opener in different spans",
            "<!-- a draft, parked\n`-->` and then `<!--` more\n<!-- specs/s-4 -->\n-->\n",
            set(),
        ),
        # Round 5. An unclosed run, a draft opener on the next line, the
        # partner after it. The crossing reading calls the opener quoted and
        # the literal reading calls it real; they disagree, so the line parks.
        (
            "a span reaching past a draft opener",
            "prose with an unclosed `run\n<!-- a draft, parked\nclosing ` here\n<!-- specs/s-5 -->\n-->\n",
            set(),
        ),
        # The door `overview.md` carried from round 2: a marker between the
        # two halves of a code span. The literal reading calls it live and the
        # crossing reading parks it.
        (
            "a marker inside a multi-line code span",
            "a span opens `here\n<!-- specs/s-6 -->\nand closes` there\n",
            set(),
        ),
        # Round 6. A fence delimiter indented four spaces is an indented code
        # block, not a delimiter. One of them inverts the fence state for the
        # rest of the file, and the marker quoted inside the real fenced
        # example below reads live. The generator builds no indentation, so
        # this arrives as a row.
        (
            "a marker in a fenced example under an indented delimiter",
            "A fence opens with\n\n    ```python\n\nand closes with a run "
            "at least as long.\n\n```markdown\n<!-- specs/s-8 -->\n```\n",
            set(),
        ),
        # And the control, without which every answer above is satisfied by a
        # reader that parks the whole document.
        (
            "a genuine marker, nothing quoted",
            "# a policy\n\n<!-- specs/s-7 -->\nThe standing statement.\n",
            {"s-7"},
        ),
    ],
)
def test_every_shape_five_review_rounds_named(name, body, found):
    """One row per shape a review round of this work item found, and the two
    controls. Each was found by a round rather than by a case, which is what
    this family exists to change."""
    assert live_markers(body) == found, name


def test_readable_would_erase_every_fold_record():
    """Why the pair `check_text` uses is the wrong reader here, asked of the
    code rather than asserted in a comment. Round 2 confirmed the rejection by
    execution and this is the standing form of it."""
    marker = ["<!-- specs/1780000000-work -->", "A standing statement."]
    assert uc.readable("\n".join(marker))[0] == ""
    assert next(iter(uc.live_lines(marker)))[1] is True


# --- #517 D3: a spec-less directory is retired by the rule, not by a record -

CLOSED_SECTION = """## Not verified

| Item | Who must answer |
|---|---|
| closed how the gate renders in a TUI | seen on screen, 2026-01-01 |
"""


def moment_repo(tmp_path, section, spec=False, name="1780000009-release-0-1-0"):
    """A committed spec-less work item — a routing declaration and a memo —
    beside the fixture's own, and the path of its directory."""
    d, _ = git_repo(tmp_path, CANONICAL)
    item = d / "specs" / name
    item.mkdir(parents=True)
    (item / "routing.md").write_text(f"# {name} — routing\n", encoding="utf-8")
    (item / "overview.md").write_text(f"# {name}\n\n{section}", encoding="utf-8")
    if spec:
        (item / "spec.md").write_text("# a spec\n\nA rule.\n", encoding="utf-8")
    subprocess.run(["git", "-C", str(d), "add", "-A"], check=True, capture_output=True)
    subprocess.run(
        ["git", "-C", str(d), "commit", "-qm", "moment"],
        check=True,
        capture_output=True,
    )
    return d, item


def test_a_rule_retirement_is_not_this_branchs_deletion(tmp_path, capsys):
    """A6. `settle --apply` removes a released directory that held no
    `spec.md` and nothing open, and this arm used to call that a deletion."""
    d, item = moment_repo(tmp_path, CLOSED_SECTION)
    shutil.rmtree(item)
    assert run([str(d), "--baseline", "HEAD"]) == 0
    out = capsys.readouterr().out
    assert "present at HEAD and not here" not in out, out
    assert "1 settled" in out and item.name in out.split("settled —")[1], out


def test_a_rule_retirement_with_an_open_row_at_the_base_still_fails(tmp_path, capsys):
    d, item = moment_repo(tmp_path, CANONICAL)
    shutil.rmtree(item)
    assert run([str(d), "--baseline", "HEAD"]) == 1
    assert "present at HEAD and not here" in capsys.readouterr().out


def test_a_spec_deleted_by_an_earlier_merge_is_still_a_deletion(tmp_path, capsys):
    """Round 1's finding 3: a base whose `spec.md` an earlier commit already
    deleted still read as a spec-less work item. The predicate asks history."""
    d, item = moment_repo(tmp_path, CLOSED_SECTION, spec=True)
    (item / "spec.md").unlink()
    subprocess.run(
        ["git", "-C", str(d), "commit", "-qam", "an earlier pull request drops it"],
        check=True,
        capture_output=True,
    )
    shutil.rmtree(item)
    assert run([str(d), "--baseline", "HEAD"]) == 1
    out = capsys.readouterr().out
    assert "present at HEAD and not here" in out, out
    assert "settled —" not in out, out


def test_a_spec_dropped_on_the_far_side_of_a_merge_is_still_written(tmp_path):
    """Round 2's finding 6. A spec added and dropped on a branch that reached
    this one through a merge commit is history git's default simplification
    prunes: at the merge the path matches the parent that never held it, so
    `git log` follows that parent alone. Every release reaches `main` that
    way, so a spec dropped in one release read as never written in the next."""
    d = tmp_path / "r"
    d.mkdir()

    def git(*args):
        subprocess.run(["git", "-C", str(d), *args], check=True, capture_output=True)

    git("init", "-q", "-b", "main")
    git("config", "user.email", "x@example.com")
    git("config", "user.name", "x")
    (d / "README.md").write_text("r\n", encoding="utf-8")
    git("add", "-A")
    git("commit", "-qm", "root")
    git("switch", "-qc", "release")
    item = d / "seal" / "specs" / "1780000009-x"
    item.mkdir(parents=True)
    (item / "routing.md").write_text("# x — routing\n", encoding="utf-8")
    (item / "spec.md").write_text("# a spec\n\nA rule.\n", encoding="utf-8")
    git("add", "-A")
    git("commit", "-qm", "a work item with a spec")
    git("rm", "-q", "seal/specs/1780000009-x/spec.md")
    git("commit", "-qm", "the spec, dropped")
    git("switch", "-q", "main")
    (d / "other.md").write_text("o\n", encoding="utf-8")
    git("add", "-A")
    git("commit", "-qm", "main moves")
    git("merge", "-q", "--no-ff", "-m", "release into main", "release")
    assert uc.wrote_a_spec(str(d), "HEAD", "seal/specs/1780000009-x"), (
        "a spec dropped before a merge commit read as never written"
    )
    assert not uc.settled(str(d), "HEAD", ["seal/specs/1780000009-x"])


def test_a_history_git_cannot_read_counts_as_a_spec_written(tmp_path):
    """`wrote_a_spec`'s failure direction: a git that cannot answer keeps the
    directory, because *never wrote one* is the answer that removes it."""
    assert uc.wrote_a_spec(str(tmp_path), None, "seal/specs/1780000009-x")


def test_a_removed_memo_in_a_directory_that_stays_is_not_a_retirement(tmp_path, capsys):
    """A retirement removes the directory. Deleting only the memo of a
    spec-less directory that stays is deleting a record, whatever it held."""
    d, item = moment_repo(tmp_path, CLOSED_SECTION)
    (item / "overview.md").unlink()
    assert run([str(d), "--baseline", "HEAD"]) == 1
    assert "present at HEAD and not here" in capsys.readouterr().out


def test_the_baseline_arm_asks_the_one_predicate(tmp_path, capsys, monkeypatch):
    """The reader calls `settled` rather than re-deriving it, so the next
    condition added to the predicate reaches this reader too."""
    d, item = moment_repo(tmp_path, CLOSED_SECTION)
    shutil.rmtree(item)
    asked = []
    monkeypatch.setattr(
        uc, "settled", lambda root, ref, dirs, here=None: asked.extend(dirs) or set()
    )
    assert run([str(d), "--baseline", "HEAD"]) == 1
    assert asked == [f"specs/{item.name}"], asked


@pytest.mark.parametrize(
    "script",
    [
        ("skills", "code-review", "scripts", "chain_check.py"),
        ("skills", "settle", "scripts", "settle.py"),
    ],
)
def test_every_reader_of_a_retirement_calls_the_one_predicate(script):
    """Three parties ask whether a removed directory was settled, and a
    predicate spelled in each would take the next condition in one and not
    the others. The behaviour is pinned per reader in its own module; this
    pins that each one reaches the answer by calling `settled` on the module
    that owns it, so a reader that re-derives the rule inline goes red here
    even while it agrees today."""
    import ast

    with open(os.path.join(ROOT, *script), encoding="utf-8") as f:
        tree = ast.parse(f.read())
    calls = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "settled"
    ]
    assert calls, f"{'/'.join(script)} decides a removal without asking the predicate"
    assert not [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == "settled"
    ], f"{'/'.join(script)} defines a second `settled`"


# --- G7: the root's own seal/specs/, empty or absent, is a settled state ----


def settled(tmp_path, keep_empty_dir):
    d = tmp_path / "repo"
    shutil.copytree(_bare_inited_repo_template(), d)
    (d / "seal").mkdir()
    (d / "seal" / "ledger.md").write_text("# ledger\n", encoding="utf-8")
    subprocess.run(["git", "-C", str(d), "add", "-A"], check=True, capture_output=True)
    subprocess.run(
        ["git", "-C", str(d), "commit", "-qm", "settled"],
        check=True,
        capture_output=True,
    )
    if keep_empty_dir:
        (d / "seal" / "specs").mkdir()
    return d


@pytest.mark.rule("an-empty-root-is-settled")
@pytest.mark.parametrize("keep_empty_dir", [True, False], ids=["empty", "absent"])
@pytest.mark.parametrize("baseline", [True, False], ids=["baseline", "plain"])
def test_the_roots_own_specs_path_is_settled_when_nothing_is_under_it(
    tmp_path, capsys, keep_empty_dir, baseline
):
    """G7. Every pull request after a complete fold runs
    `--baseline origin/<base> seal/specs/`, the shipped `templates/hygiene.yml`
    included, and the path holds nothing at HEAD and held no overview at the
    merge base. That was *a typo*, exit 2 — so every such pull request red."""
    d = settled(tmp_path, keep_empty_dir)
    path = str(d / "seal" / "specs")
    argv = [path] + (["--baseline", "HEAD"] if baseline else [])
    assert run(argv) == 0, capsys.readouterr()
    out = capsys.readouterr()
    assert "holds no work item" in out.out + out.err, out


@pytest.mark.parametrize("baseline", [True, False], ids=["baseline", "plain"])
def test_any_other_missing_path_is_still_a_typo(tmp_path, capsys, baseline):
    d = settled(tmp_path, keep_empty_dir=False)
    argv = [str(d / "seal" / "spces")] + (["--baseline", "HEAD"] if baseline else [])
    assert run(argv) == 2
    assert "no such path" in capsys.readouterr().err


# --- #491: one fence-delimiter rule ---------------------------------------
#
# `fence_opener` and `fence_closes` are the rule, and every reader of this
# module that walks a fence asks them. Before #491 `blank_fences` read a
# delimiter at any indentation while `_liveness` bounded it to three spaces,
# and neither refused a closer carrying an info string.


def fenced_by_the_shared_rule(lines):
    """The indices `uc.fence_spans` puts inside a block, unclosed ones to the
    end — the same question `hooks/config.py#fence_map` answers."""
    out = set()
    for first, last in uc.fence_spans(lines):
        out.update(range(first, len(lines) if last is None else last + 1))
    return out


def test_an_indented_delimiter_is_not_a_fence_for_the_gates_reader():
    """S4. Four spaces before a run of backticks is an indented code block or
    a lazy continuation line, never a delimiter (CommonMark 4.5). Read as one,
    it opens a fence nobody closes and every row below it disappears from
    `check_text` and `chain_check.py` at once. Seen red
    against `c52e8350`'s `blank_fences`, whose `^\\s*` took the line as an
    opener and blanked the table."""
    text = "A fence opens with\n\n    ```\n\n| a | b |\n|---|---|\n| c | d |\n"
    kept = uc.readable(text)
    assert "| c | d |" in kept, kept


@pytest.mark.parametrize(
    "lines, fenced",
    [
        # S5: a closer carries nothing after its run.
        (["```", "inside", "```python", "quoted", "```", "after"], {0, 1, 2, 3, 4}),
        # A backtick opener whose info string holds a backtick opens nothing.
        (["```x`", "quoted", "after"], set()),
        # A tilde opener's info string is unrestricted, which is the format.
        (["~~~ `x`", "quoted", "~~~", "after"], {0, 1, 2}),
    ],
)
def test_each_reader_asks_the_one_delimiter_rule(lines, fenced):
    """S5, asked of both readers. `readable` blanks exactly the fenced lines,
    and `live_lines` calls exactly those not live. Seen red against
    `c52e8350`: both closed the first block on ```` ```python ````, so the
    quoted line read live and the final ```` ``` ```` opened a second block
    that swallowed `after`; and both opened a block on ```` ```x` ````.

    `live_lines` answers whether a line BEGINS live, so an opener's own line
    is live and every other line of the block is not."""
    blanked = {n for n, line in enumerate(uc.readable("\n".join(lines))) if not line}
    assert blanked == fenced, blanked
    openers = {first for first, _ in uc.fence_spans(lines)}
    parked = {n for n, (_, live) in enumerate(uc.live_lines(lines)) if not live}
    assert parked == fenced - openers, parked


FENCE_SHAPES = [
    ["```", "x", "```"],
    ["~~~", "x", "~~~"],
    ["   ```", "x", "   ```"],
    ["    ```", "x", "    ```"],
    ["```", "x", "    ```", "y", "```"],
    ["```python", "x", "```"],
    ["```", "x", "```python", "y", "```"],
    ["```", "x", "```   ", "y"],
    ["````", "```", "x", "````"],
    ["```", "x", "``````", "y"],
    ["```", "x", "~~~", "y", "```"],
    ["~~~", "```", "x", "~~~"],
    ["```x`", "y", "```"],
    ["``` `x`", "y"],
    ["~~~ `x`", "y", "~~~", "z"],
    ["``", "x", "``"],
    ["```", "x", "y"],
    ["a", "```\r", "x\r", "```\r", "b\r"],
    ["| a |", "```", "| b |", "```", "| c |"],
]


@pytest.mark.parametrize("lines", FENCE_SHAPES, ids=range(len(FENCE_SHAPES)))
def test_the_fence_rule_agrees_with_the_config_reader(lines):
    """S6. `hooks/blocks.py#FENCE` is the one deliberate second copy of the
    delimiter rule — it runs on the hook path, where loading a skill module
    would cost every hook call — so this holds the two in step, shape by
    shape, over which lines are fenced and where an unclosed block opened.
    Seen red against `c52e8350`'s `blank_fences` rule on shapes 3, 4, 6, 12
    and 13 — the indentation bound, the closer's info string and the opener's
    backtick.

    Asked of the config reader and of the walk's fence half both (#667, the
    frame's S3): the copy moved out of `hooks/config.py` into the walk the
    hook-path readers share, and neither may drift from this rule on a file
    that holds no comment. `blocks.fence_only` is the fence rule alone;
    `blocks.walk` on these shapes, where it claims a line, hides the same
    fenced lines."""
    spec = importlib.util.spec_from_file_location(
        "specseal_config_for_fence_agreement", os.path.join(ROOT, "hooks", "config.py")
    )
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    shown, opened_at = config.fence_map(lines)
    theirs = set(range(len(lines))) - {n for n, _ in shown}
    assert fenced_by_the_shared_rule(lines) == theirs
    unclosed = [first for first, last in uc.fence_spans(lines) if last is None]
    assert unclosed == ([] if opened_at is None else [opened_at])

    from conftest import load_hook_module

    blocks = load_hook_module("blocks.py", "specseal_blocks_for_fence_agreement")
    assert blocks.fence_only(lines) == (fenced_by_the_shared_rule(lines), opened_at)
    walked = blocks.walk(lines)
    claimed = {n for n in range(len(lines)) if not walked.uncertain[n]}
    assert set(walked.hidden()) & claimed == fenced_by_the_shared_rule(lines) & claimed


@pytest.mark.parametrize(
    "line, ends",
    [("   # a heading", True), ("    # four spaces is paragraph text", False)],
)
def test_an_atx_heading_ends_a_paragraph_only_within_three_spaces(line, ends):
    """#491's round-7 comment. CommonMark 4.2 bounds an ATX heading to three
    spaces of indentation, and the oracle `block_ends_at` above has always
    said so. Seen red against `c52e8350`, whose `line.strip()` stopped the
    paragraph on the four-space line."""
    assert uc._paragraph_ends_at(line) is ends


# --- #688: a reference root is read and never checked ---------------------
#
# A project's own `specs/` is a team's document. A walk leaves it out, so a
# malformed `## Not verified` there is not this plugin's finding; a path the
# person names is read as named; and the base is read by the same rule, so an
# overview the walk leaves out is never reported deleted.

TEAM = "specs/1788000001-team-thing"
MALFORMED = "## Not verified\n\nnot a table, and not a none line either\n"


def joined_repo(tmp_path):
    """A repository with a `seal/` root holding one readable work item, and a
    team's own `specs/` whose overview the reader cannot read."""
    d = tmp_path / "joined"
    shutil.copytree(_bare_inited_repo_template(), d)
    item = d / "seal" / "specs" / "1790000000-ours"
    item.mkdir(parents=True)
    (item / "overview.md").write_text(f"# ours\n\n{CANONICAL}", encoding="utf-8")
    team = d / TEAM
    team.mkdir(parents=True)
    (team / "overview.md").write_text(f"# the team's\n\n{MALFORMED}", encoding="utf-8")
    (team / "spec.md").write_text("# the team's spec\n", encoding="utf-8")
    subprocess.run(["git", "-C", str(d), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(d), "commit", "-qm", "joined"], check=True)
    return d


def test_a_walk_from_the_repository_root_leaves_a_team_specs_out(tmp_path, capsys):
    """D2. Red against the walk before #688: the team's overview was read and
    its unreadable section failed the run."""
    d = joined_repo(tmp_path)
    assert run([str(d)]) == 0
    out = capsys.readouterr().out
    assert "1790000000-ours" in out and "team-thing" not in out, out


def test_a_team_overview_named_explicitly_is_still_read(tmp_path):
    """D2's other half: a person who names the file, or the directory it
    sits in, has asked for it."""
    d = joined_repo(tmp_path)
    assert run([str(d / TEAM / "overview.md")]) == 1
    assert run([str(d / "specs")]) == 1


def test_a_team_overview_deleted_since_the_base_is_not_reported(tmp_path):
    """The base side by the walk's rule: a team removing its own overview is
    not a record this branch deleted."""
    d = joined_repo(tmp_path)
    os.remove(d / TEAM / "overview.md")
    assert run([str(d), "--baseline", "HEAD"]) == 0


def test_a_team_directory_named_is_compared_against_its_base(tmp_path, capsys):
    """Named, the team's directory is read on both sides: its overview gone
    since the base is reported as a deletion, as any named path's is."""
    d = joined_repo(tmp_path)
    os.remove(d / TEAM / "overview.md")
    assert run([str(d / "specs"), "--baseline", "HEAD"]) == 1
    assert "team-thing" in capsys.readouterr().out


def test_a_copy_with_no_hooks_beside_it_prunes_nothing(tmp_path, monkeypatch):
    """`references_at` loads `hooks/config.py` beside this script. A copy
    taken alone reads every overview, as it did before reference roots
    existed, rather than refusing a run that needed none of this — the walk
    and the base alike."""
    d = joined_repo(tmp_path)
    monkeypatch.setattr(uc, "HOOKS", str(tmp_path / "no-hooks-here"))
    assert run([str(d)]) == 1
    assert run([str(d), "--baseline", "HEAD"]) == 1


def test_a_walk_outside_a_repository_reads_no_reference_root(tmp_path, monkeypatch):
    """Outside a git repository there is no root to be outside of, and every
    fixture of the 0.3.x spelling lives there: nothing about reference roots
    is read, and a path with no relative form to a repository is never asked
    for one."""

    def refuse(top):
        raise AssertionError(f"reference roots were read for {top!r}")

    monkeypatch.setattr(uc, "references_at", refuse)
    write(tmp_path, CANONICAL)
    assert run([str(tmp_path)]) == 0
