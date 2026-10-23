"""Every reader of markdown or record text ends a line where GFM does (#664).

`str.splitlines` ends a line at LF, CR and CRLF, and also at U+2028, U+2029,
NEL, a form feed, VT and `\\x1c`-`\\x1e`. GFM, `ast` and git end one at the
first three alone. So below one of those eight a reader that split with
`splitlines` read lines no renderer shows: a table row cut in two, a marker or
a heading that stands mid-line read as a line of its own, a line number one
off the one `grep -n` prints, and, where the reader wrote the text back, the
character turned into a line break.

One splitter, `hooks/blocks.py#gfm_lines`, which `unverified_check.py` hands
its callers, is what
every such reader now reads, and two readers of one text split it alike. The
scenarios are `seal/specs/1790655302-every-reader-ends-a-line-where-gfm-does/
spec.md`'s, numbered as it numbers them, and each was seen red at `2e392d46`
before it was committed.

Every one of the eight is built from its code point, never typed: an escape
typed into an editing tool can come back as the character itself, and a file
holding one is exactly what these cases are about.

The splitter's own cases are `tests/test_blocks.py`'s `Test_gfm_lines`
(#942's phase 6); what stays holds every copy of it, and each other reader,
to it.
"""

import datetime
import importlib.util
import json
import os
import sys

from conftest import texts

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
READER = os.path.join(ROOT, "skills", "verify", "scripts", "unverified_check.py")
CHECKER = os.path.join(ROOT, "skills", "verify", "scripts", "coordinates.py")
ARM_CHECK = os.path.join(ROOT, "skills", "verify", "scripts", "arm_check.py")
FOLD_CHECK = os.path.join(ROOT, "skills", "settle", "scripts", "fold_check.py")

LS = chr(0x2028)
FF = chr(0x0C)
BY_CODE_POINT = {"ids": lambda c: f"U+{ord(c):04X}"}


def _load(name, path):
    """A script by path, registered under NAME first: `arm_check.py` defines
    dataclasses, which look their own module up in `sys.modules`."""
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


reader = _load("specseal_reader_for_gfm_lines", READER)


# --- S17: one splitter, and its copies agree ---------------------------------


def test_every_copy_of_the_splitter_is_the_readers():
    """S17. The reader's split is `hooks/blocks.py`'s, which it imports since
    #1005; `arm_check._lines` splits Python source where `ast` does, ends
    kept, and the coordinate kernel asks the reader itself. All are one rule,
    held equal here."""
    checker = _load("specseal_checker_for_gfm_lines", CHECKER)
    arm_check = _load("specseal_arm_check_for_gfm_lines", ARM_CHECK)
    for text in texts():
        want = reader.gfm_lines(text)
        assert checker.gfm_lines(text) == want, repr(text)
        kept = reader.gfm_lines(text, keepends=True)
        assert checker.gfm_lines(text, keepends=True) == kept, repr(text)
        assert arm_check._lines(text) == kept, repr(text)


def test_fold_check_keeps_no_copy_of_its_own():
    """The copy `fold_check.py` held while the reader was being rewritten on
    another branch is gone."""
    fold_check = _load("specseal_fold_check_for_gfm_lines", FOLD_CHECK)
    assert not hasattr(fold_check, "gfm_lines")
    assert not hasattr(fold_check, "GFM_LINE_RE")


# --- S5-S8: the changelog readers and their partner ---------------------------


GATHER = os.path.join(ROOT, ".github", "scripts", "gather_changelog.py")


def test_gathering_below_a_separator_lands_in_the_section_and_keeps_it():
    """S5. `insert` found the section by counting LF and then indexed a list
    `splitlines` had made, so a U+2028 above the section put the new entries
    above its heading, and the file was written back with a line break where
    the character stood."""
    gather = _load("specseal_gather_s5", GATHER)
    text = (
        "# Changelog\n\n"
        f"Intro alpha{LS}beta.\n\n"
        "## 1.1.0 — 2026-01-02\n\n"
        "<!-- specs/1-a -->\nentry a\n\n"
        "## 1.0.0 — 2026-01-01\n\nold\n"
    )
    block = gather.section("1.1.0", "2026-01-03", [("2-b", f"entry{FF}b")])
    assert gather.insert(text, block, "1.1.0") == (
        "# Changelog\n\n"
        f"Intro alpha{LS}beta.\n\n"
        "## 1.1.0 — 2026-01-02\n\n"
        "<!-- specs/1-a -->\nentry a\n\n"
        f"<!-- specs/2-b -->\nentry{FF}b\n\n"
        "## 1.0.0 — 2026-01-01\n\nold\n"
    )
    fresh = gather.section("1.2.0", "2026-01-03", [("2-b", f"entry{FF}b")])
    assert gather.insert(text, fresh, "1.2.0") == (
        "# Changelog\n\n"
        f"Intro alpha{LS}beta.\n\n"
        f"## 1.2.0 — 2026-01-03\n\n<!-- specs/2-b -->\nentry{FF}b\n\n"
        "## 1.1.0 — 2026-01-02\n\n"
        "<!-- specs/1-a -->\nentry a\n\n"
        "## 1.0.0 — 2026-01-01\n\nold\n"
    )


def test_the_sections_index_is_counted_on_the_list_it_indexes():
    """`insert` indexes `gfm_lines(text)`, and the heading's index is counted
    with the same split. A text read through `open()` never holds a lone CR,
    so counting LF agrees on every file `main` reads; handed one directly,
    the two counts part and the entries land above the heading."""
    gather = _load("specseal_gather_index", GATHER)
    text = "# Changelog\n\nIntro\rmore.\n\n## 1.1.0 — 2026-01-02\n\nentry a\n"
    block = gather.section("1.1.0", "2026-01-03", [("2-b", "entry b")])
    assert gather.insert(text, block, "1.1.0") == (
        "# Changelog\n\nIntro\nmore.\n\n## 1.1.0 — 2026-01-02\n\n"
        "entry a\n\n<!-- specs/2-b -->\nentry b\n"
    )


def fragment_tree(tmp_path, body):
    """A repository root holding one changelog fragment and a changelog."""
    item = tmp_path / "seal" / "specs" / "2-b"
    item.mkdir(parents=True)
    (item / "changelog.md").write_text(body, encoding="utf-8")
    (tmp_path / "CHANGELOG.md").write_text(
        "# Changelog\n\n## 1.0.0 — 2026-01-01\n\nold\n", encoding="utf-8"
    )
    return tmp_path


def test_the_dry_run_prints_a_fragments_character_as_it_stands(tmp_path, capsys):
    gather = _load("specseal_gather_dry_run", GATHER)
    root = fragment_tree(tmp_path, f"entry{LS}b\n")
    argv = ["--version", "1.1.0", "--date", "2026-01-02", "--dry-run"]
    assert gather.main([*argv, "--root", str(root)]) == 0
    assert f"entry{LS}b" in capsys.readouterr().out


def test_a_fence_after_a_separator_opens_nothing_in_a_fragment():
    """`leaves_open` asks `live_lines` whether a marker written below the
    body would be live. A fence run after a U+2028 is mid-line to GFM, so it
    opens nothing, and the fragment is not refused for one."""
    gather = _load("specseal_gather_leaves_open", GATHER)
    assert gather.leaves_open(f"an entry{LS}```\n") is False


def test_a_section_line_is_a_line_that_starts_one(tmp_path):
    """`section_lines` names every fragment line starting `## `, by the
    number `grep -n` prints. One after a form feed mid-line starts none."""
    gather = _load("specseal_gather_section_lines", GATHER)
    root = fragment_tree(tmp_path, f"entry{FF}## not a heading\n\n## one\n")
    assert gather.section_lines(str(root), "2-b") == [(3, "## one")]


def test_the_gatherer_reads_a_marker_after_a_separator_as_no_line():
    """S6. A marker after a U+2028 on its line is not a line of its own to
    GFM, so the gatherer does not call the fragment gathered; the same marker
    on a line of its own is read, so the empty answer is the separator's
    doing."""
    gather = _load("specseal_gather_s6", GATHER)
    text = f"# Changelog\n\n## 1.0.0 — 2026-01-01\n\nold{LS}<!-- specs/1-a -->\n"
    assert gather.live_markers(text) == []
    assert gather.live_markers(text.replace(LS, "\n")) == ["1-a"]


# --- S9-S13: the independent readers ----------------------------------------


CHAIN = os.path.join(ROOT, "skills", "code-review", "scripts", "chain_check.py")
PAYLOAD = os.path.join(ROOT, "skills", "verify", "scripts", "payload_meter.py")
CLAIMS = os.path.join(ROOT, ".github", "scripts", "issue_claims_check.py")


def test_the_framers_mark_is_the_last_line_a_renderer_shows():
    """S10. The mark stands after a U+2028 on the file's last line, so the
    last line does not begin with one."""
    chain = _load("specseal_chain_s10", CHAIN)
    spec = f"# spec\n\nprose{LS}Framed 2026-01-01 by framer, before the build.\n"
    assert chain.frame_foot(reader, spec)[0] is None
    whole = "# spec\n\nprose\nFramed 2026-01-01 by framer, before the build.\n"
    assert chain.frame_foot(reader, whole)[0] == ("2026-01-01", "framer")


def test_a_heading_after_a_separator_starts_no_section():
    """S12. No section starts mid-line, and the one that does start is at
    its offset in the file, which is where the ends kept put it."""
    payload = _load("specseal_payload_s12", PAYLOAD)
    text = f"intro\n\nprose{LS}## Not a section\n\n## Real\nbody\n"
    assert payload.heading_starts(text) == [text.index("## Real")]


def test_an_issue_body_is_cut_where_github_renders_a_block():
    """S13. A list-item shape after a U+2028 mid-line is not a block GitHub
    renders, so it is no cut."""
    claims = _load("specseal_claims_s13", CLAIMS)
    text = f"The parser drops a row{LS}- when the cell is wide"
    assert claims.segments(text) == [(0, len(text))]


# --- S16: the transcript tails ----------------------------------------------


GUARD = os.path.join(ROOT, "hooks", "worktree-guard.py")


def jsonl(path, events):
    """JSON Lines as a JavaScript writer emits them: a U+2028 inside a
    string stays raw, which JSON permits."""
    path.write_text(
        "".join(json.dumps(e, ensure_ascii=False) + "\n" for e in events),
        encoding="utf-8",
    )


def test_a_transcript_record_holding_a_raw_separator_is_read(monkeypatch, tmp_path):
    """S16. Cut at the separator, the last user record was two halves that
    each failed to parse, and the snippet named an earlier message."""
    guard = _load("specseal_guard_s16", GUARD)
    cwd = tmp_path / "tree"
    cwd.mkdir()
    monkeypatch.setenv("HOME", str(tmp_path))
    monkeypatch.setenv("USERPROFILE", str(tmp_path))
    proj = tmp_path / ".claude" / "projects" / guard.project_slug(str(cwd))
    proj.mkdir(parents=True)
    jsonl(
        proj / "abcd1234-x.jsonl",
        [
            {
                "type": "user",
                "timestamp": "2026-01-01T00:00",
                "message": {"content": "first"},
            },
            {
                "type": "user",
                "timestamp": "2026-01-01T00:05",
                "message": {"content": f"second{LS}message"},
            },
        ],
    )
    _sid, when, text = guard.last_user_snippet(str(cwd), "me")
    assert when == "2026-01-01T00:05"
    assert text.startswith("second")


def test_the_newest_active_event_holding_a_raw_separator_is_read(tmp_path):
    """S16's second reader. The newest active event carries a U+2028 in a
    string, and its time is the answer rather than an older event's."""
    guard = _load("specseal_guard_s16b", GUARD)
    path = tmp_path / "t.jsonl"
    jsonl(
        path,
        [
            {"type": "user", "timestamp": "2026-01-01T00:00:00Z"},
            {
                "type": "assistant",
                "timestamp": "2026-01-01T00:30:00Z",
                "text": f"a{LS}b",
            },
        ],
    )

    want = datetime.datetime(2026, 1, 1, 0, 30, tzinfo=datetime.UTC).timestamp()
    assert guard.last_active_event_epoch(str(path)) == want


# S19, that no shipped reader of a document splits with `.splitlines(`, is
# the `splitlines` census in `tests/censuses.py`; each call left carries its
# exemption on the line above it.
