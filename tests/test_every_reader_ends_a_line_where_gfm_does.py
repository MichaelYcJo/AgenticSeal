"""Every reader of markdown or record text ends a line where GFM does (#664).

`str.splitlines` ends a line at LF, CR and CRLF, and also at U+2028, U+2029,
NEL, a form feed, VT and `\\x1c`-`\\x1e`. GFM, `ast` and git end one at the
first three alone. So below one of those eight a reader that split with
`splitlines` read lines no renderer shows: a table row cut in two, a marker or
a heading that stands mid-line read as a line of its own, a line number one
off the one `grep -n` prints, and, where the reader wrote the text back, the
character turned into a line break.

One splitter, `skills/verify/scripts/unverified_check.py#gfm_lines`, is what
every such reader now reads, and two readers of one text split it alike. The
scenarios are `seal/specs/1790655302-every-reader-ends-a-line-where-gfm-does/
spec.md`'s, numbered as it numbers them, and each was seen red at `2e392d46`
before it was committed.

Every one of the eight is built from its code point, never typed: an escape
typed into an editing tool can come back as the character itself, and a file
holding one is exactly what these cases are about.
"""

import ast
import datetime
import importlib.util
import json
import os
import subprocess
import sys

import pytest

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
READER = os.path.join(ROOT, "skills", "verify", "scripts", "unverified_check.py")
CHECKER = os.path.join(ROOT, "skills", "verify", "scripts", "coordinates.py")
ARM_CHECK = os.path.join(ROOT, "skills", "verify", "scripts", "arm_check.py")
FOLD_CHECK = os.path.join(ROOT, "skills", "settle", "scripts", "fold_check.py")
BLOCKS = os.path.join(ROOT, "hooks", "blocks.py")

# Every character `str.splitlines` ends a line at and GFM does not.
SPLITLINES_ONLY = [chr(c) for c in (0x0B, 0x0C, 0x1C, 0x1D, 0x1E, 0x85, 0x2028, 0x2029)]
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


def texts():
    """Every shape the copies could part on: each line end GFM has, each of
    the eight mid-line and at a line end, no trailing newline, and nothing."""
    out = ["", "a", "a\n", "a\n\n", "\n", "a\nb", "a\r\nb\r\n", "a\rb\r", "a\r\n\r\n"]
    for char in SPLITLINES_ONLY:
        out += [f"a{char}b\n", f"a{char}\nb", f"{char}", f"a\n{char}\n\nc{char}"]
    return out


def test_the_readers_splitter_ends_a_line_at_lf_cr_and_crlf_alone():
    for char in SPLITLINES_ONLY:
        assert reader.gfm_lines(f"a{char}b\nc") == [f"a{char}b", "c"], repr(char)
    assert reader.gfm_lines("a\r\nb\rc\nd") == ["a", "b", "c", "d"]
    assert reader.gfm_lines("a\r\nb\n", keepends=True) == ["a\r\n", "b\n"]


def test_the_splitter_is_splitlines_on_a_text_without_the_eight():
    for text in [t for t in texts() if not any(c in t for c in SPLITLINES_ONLY)]:
        assert reader.gfm_lines(text) == text.splitlines(), repr(text)
        assert reader.gfm_lines(text, True) == text.splitlines(True), repr(text)


def test_every_copy_of_the_splitter_is_the_readers():
    """S17. `hooks/blocks.py` keeps work item F's copy because a hook does not
    load a skill module on every call, and `arm_check._lines` splits Python
    source where `ast` does, ends kept. The coordinate kernel asks the reader
    itself. All are one rule, held equal here."""
    checker = _load("specseal_checker_for_gfm_lines", CHECKER)
    arm_check = _load("specseal_arm_check_for_gfm_lines", ARM_CHECK)
    blocks = _load("specseal_blocks_for_gfm_lines", BLOCKS)
    for text in texts():
        want = reader.gfm_lines(text)
        assert checker.gfm_lines(text) == want, repr(text)
        assert blocks.gfm_lines(text) == want, repr(text)
        kept = reader.gfm_lines(text, keepends=True)
        assert checker.gfm_lines(text, keepends=True) == kept, repr(text)
        assert blocks.gfm_lines(text, keepends=True) == kept, repr(text)
        assert arm_check._lines(text) == kept, repr(text)
    assert reader.GFM_LINE_RE.pattern == blocks.GFM_LINE_RE.pattern


def test_fold_check_keeps_no_copy_of_its_own():
    """The copy `fold_check.py` held while the reader was being rewritten on
    another branch is gone, and the ceiling counts with the reader's."""
    fold_check = _load("specseal_fold_check_for_gfm_lines", FOLD_CHECK)
    assert not hasattr(fold_check, "gfm_lines")
    assert not hasattr(fold_check, "GFM_LINE_RE")


# --- S3, S4: a marker GFM does not show as its own line excuses nothing -----


MARKED = f"# A policy\n\nprose{LS}<!-- specs/1700000000-a -->\n\n**A rule.**\n"


def test_a_marker_after_a_separator_is_not_a_fold(tmp_path):
    """S3. The marker is line-anchored, and GFM renders it mid-line, so no
    fold wrote it there. Read as a fold, it excused the removal of a
    directory nothing absorbed."""
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "x.md").write_text(MARKED, encoding="utf-8")
    assert reader.folded_items(str(tmp_path)) == set()


def test_the_ceiling_and_the_fold_agree_about_that_marker():
    """S4. `fold-check` counts what the fold reads, so it counts no marker
    there either: the frozen count, the digest and the statements."""
    fold_check = _load("specseal_fold_check_s4", FOLD_CHECK)
    assert fold_check.markers(MARKED) == 0
    assert fold_check.marker_digest(MARKED) == fold_check.marker_digest("")
    assert fold_check.numbered_statements(MARKED) == []


@pytest.mark.parametrize("char", SPLITLINES_ONLY, **BY_CODE_POINT)
def test_no_one_of_the_eight_makes_a_marker_a_line(tmp_path, char):
    text = MARKED.replace(LS, char)
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "x.md").write_text(text, encoding="utf-8")
    assert reader.folded_items(str(tmp_path)) == set(), repr(char)


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


# --- S9-S15: the independent readers ----------------------------------------


CHAIN = os.path.join(ROOT, "skills", "code-review", "scripts", "chain_check.py")
PAYLOAD = os.path.join(ROOT, "skills", "verify", "scripts", "payload_meter.py")
CLAIMS = os.path.join(ROOT, ".github", "scripts", "issue_claims_check.py")
CLAUDE_BLOCK = os.path.join(ROOT, ".github", "scripts", "claude_block.py")


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


START, END = "<!-- specseal:start -->", "<!-- specseal:end -->"


def test_the_claude_md_block_is_cut_where_awk_cuts_it(tmp_path):
    """S15. `install.sh`'s `awk` ends a record at LF alone. A template line
    holding a U+2028 mid-line is one line to it, so `--write` copies that line
    whole and `--check` then agrees. The target's last line has no line
    end, and it is still a line: `awk` prints it, and `--write` keeps it."""
    template = tmp_path / "block.md"
    target = tmp_path / "CLAUDE.md"
    template.write_text(f"{START}\n## Rules\nalpha{LS}beta\n{END}\n", encoding="utf-8")
    target.write_text(
        f"# repo\n\n{START}\n## Rules\nold\n{END}\n\ntail", encoding="utf-8"
    )
    paths = ["--template", str(template), "--target", str(target)]

    def run(mode):
        return subprocess.run(
            [sys.executable, CLAUDE_BLOCK, mode, *paths],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )

    wrote = run("--write")
    assert wrote.returncode == 0, wrote.stdout + wrote.stderr
    written = target.read_text(encoding="utf-8")
    assert written == f"# repo\n\n{START}\n## Rules\nalpha{LS}beta\n{END}\n\ntail"
    checked = run("--check")
    assert checked.returncode == 0, checked.stdout + checked.stderr


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


# --- S19: the class stays closed --------------------------------------------

# Every `.splitlines(` call left in shipped code, by file and enclosing unit,
# with how many calls the unit makes and why it is outside the class: the text
# it splits is not a document's lines. A reader of markdown or record text
# reads `gfm_lines`, or splits at LF where its partner does (`claude_block.py`,
# the transcript tails). A call in a unit this does not list, or one more call
# in a unit it does, fails the case until somebody says which kind of text it
# splits -- here, with the reason.
GIT = "git output of paths, refs, subjects or status, not a document's lines"
TOOL = "a tool's or a subprocess's own output, not a document's lines"
YAML = "YAML read for event and key names, not markdown or a record"
F = (
    "work item F's (#667, PR #672): its walk reads GFM lines and maps each "
    "reader line to the one it starts in"
)
OUT_OF_CLASS = {
    (".github/scripts/rules.py", "main"): (1, "the docstring's first line"),
    (".github/scripts/close_issues_on_release.py", "arrived"): (2, GIT),
    (".github/scripts/issue_claims_check.py", "main"): (
        1,
        "the docstring's first line",
    ),
    (".github/scripts/release_completeness_check.py", "subjects_since"): (1, GIT),
    (".github/scripts/run_tests.py", "venv_version"): (1, "`pyvenv.cfg`"),
    ("hooks/dispatch.py", "first_line"): (1, "an exception's message"),
    ("hooks/githooks.py", "read_stub"): (1, "a git hook file this plugin wrote"),
    ("hooks/commitgate.py", "waived"): (1, GIT),
    # The one path reader the commit gate's three path lists go through since
    # #868 (`changed_paths`, `pre_commit`, `_paths_between`).
    ("hooks/gate.py", "lines"): (1, GIT),
    ("hooks/git/reference-transaction.py", "main"): (
        1,
        "the `<old> <new> <ref>` lines git hands a reference-transaction hook",
    ),
    ("hooks/root-migrate.py", "attempted"): (1, "a marker file of root paths"),
    ("hooks/root-migrate.py", "dirty"): (1, GIT),
    ("hooks/version-check.py", "latest"): (1, GIT),
    ("hooks/worktree-guard.py", "lease_owner_alive"): (1, TOOL),
    ("hooks/worktree-guard.py", "proc_cwd"): (1, TOOL),
    ("hooks/worktree-guard.py", "sessions_in_tree"): (1, TOOL),
    ("hooks/worktree-guard.py", "tracked_changes"): (1, GIT),
    ("skills/implement/scripts/seal.py", "gitlinks_under_root"): (1, GIT),
    ("skills/implement/scripts/seal.py", "other_worktrees"): (1, GIT),
    ("skills/implement/scripts/seal.py", "porcelain"): (1, GIT),
    # #867: the lines `with_row` splits, for the same walk, so the refusal
    # of two `Mode` rows names the lines the writer would have read.
    ("skills/implement/scripts/seal.py", "mode_refusal"): (1, F),
    ("skills/implement/scripts/seal.py", "with_row"): (1, F),
    ("skills/implement/scripts/seal.py", "write_row"): (1, F),
    ("skills/settle/scripts/settle.py", "released"): (1, GIT),
    ("skills/verify/scripts/broad_gate.py", "Check.first_lines"): (1, TOOL),
    ("skills/verify/scripts/broad_gate.py", "fence_left_open"): (1, F),
    ("skills/verify/scripts/broad_gate.py", "hidden_row_at"): (1, F),
    # #871: the `Broad gate` line the walker did not read, the line it
    # stopped at and what is written below that line, each read through
    # `unfenced` on the split the walker itself numbers its rows on.
    ("skills/verify/scripts/broad_gate.py", "refused_broad_row"): (1, F),
    ("skills/verify/scripts/broad_gate.py", "stopping_line"): (1, F),
    ("skills/verify/scripts/broad_gate.py", "rows_written_below"): (1, F),
    ("skills/verify/scripts/broad_gate.py", "job_steps"): (1, YAML),
    # The recorder's JSON Lines (#825): `json.dumps` escapes every control
    # character and every non-ASCII one, so no separator but LF is in it.
    ("skills/verify/scripts/broad_gate.py", "read_record"): (1, TOOL),
    ("skills/verify/scripts/deferral_check.py", "read_events"): (1, YAML),
    ("skills/verify/scripts/deferral_check.py", "runners_in"): (1, YAML),
    # The disc's mark chart (#832): every character but `.` and `M` is refused
    # after the split, so a line any other separator made is refused as well.
    ("skills/verify/scripts/seal_stamp.py", "read_chart"): (
        1,
        "the disc's mark chart, a grid of `.` and `M`, not a document's lines",
    ),
    # #975: the paths a commit touched (`git diff-tree`) and the round records
    # it holds (`git ls-tree`); `guarantee.md` itself is read through
    # `chain_check.py`'s readers.
    ("skills/verify/scripts/seal_stamp.py", "queue_for_guarantee"): (1, GIT),
    ("skills/verify/scripts/seal_stamp.py", "_queue_one"): (1, GIT),
    ("skills/verify/scripts/payload_meter.py", "frontmatter"): (1, YAML),
    ("skills/verify/scripts/session_cost.py", "open_log"): (1, TOOL),
    ("skills/verify/scripts/unverified_check.py", "overviews_at"): (1, GIT),
    ("skills/verify/scripts/unverified_check.py", "tree_at"): (1, GIT),
}
# Work item F's units, named one by one now that F has landed. Its files used
# to be exempt whole, which let any new call in them through (round 1, 🟡 4).
OUT_OF_CLASS.update(
    {
        # #871: the walker's pieces kept with their endings, so a piece that
        # does not begin a GFM line is told from one that does.
        ("hooks/config.py", "gfm_line_starts"): (
            1,
            "the walker's pieces with their endings, each asked whether it "
            "begins a GFM line",
        ),
        # The lines below the walk's last row, through `unfenced`, on the
        # split the walker numbers its rows on.
        ("hooks/config.py", "rows_named_below"): (1, F),
        ("hooks/blocks.py", "walk_text"): (1, F),
        # The one GFM table walker `seal/config.md`'s table (#871), the
        # pact's `Signer` table and both pact records are read through,
        # reading what `unfenced` shows it (#647; ⬜ 21 of #735's round 3).
        ("hooks/config.py", "gfm_table"): (1, F),
        # A glued old header quoted as written, read back by its row number.
        ("hooks/config.py", "read_table"): (
            1,
            "reads back the line `gfm_table` numbered, with the split it "
            "numbered on (#831)",
        ),
        # The machine-local map `pact-check` reads, the same walk (#647).
        ("skills/verify/scripts/pact_check.py", "path_map"): (1, F),
        ("hooks/routing.py", "table_rows"): (1, F),
    }
)
SHIPPED = ("hooks", "skills", os.path.join(".github", "scripts"))


def splitlines_calls(root=ROOT):
    """`{(path, unit): count}` for every `.splitlines(` call under the
    shipped directories, the unit being the dotted chain of enclosing
    `def`s and `class`es, or `<module>`."""
    found = {}
    for top in SHIPPED:
        for directory, _dirs, names in os.walk(os.path.join(root, top)):
            for name in sorted(names):
                if not name.endswith(".py"):
                    continue
                path = os.path.join(directory, name)
                rel = os.path.relpath(path, root).replace(os.sep, "/")
                with open(path, encoding="utf-8") as f:
                    tree = ast.parse(f.read())
                _walk(tree, [], rel, found)
    return found


def _walk(node, names, rel, found):
    for child in ast.iter_child_nodes(node):
        inner = names
        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            inner = [*names, child.name]
        if (
            isinstance(child, ast.Call)
            and isinstance(child.func, ast.Attribute)
            and child.func.attr == "splitlines"
        ):
            key = (rel, ".".join(names) or "<module>")
            found[key] = found.get(key, 0) + 1
        _walk(child, inner, rel, found)


def test_every_splitlines_call_left_is_named_with_its_reason():
    """S19. The class is held closed by a list, not by the next reviewer."""
    found = splitlines_calls()
    unnamed = {key: n for key, n in found.items() if key not in OUT_OF_CLASS}
    assert not unnamed, (
        f"`.splitlines(` in a unit this case does not name: {unnamed}. A reader "
        "of markdown or record text reads `unverified_check.py#gfm_lines`; any "
        "other text goes into OUT_OF_CLASS with the reason it is not a "
        "document's lines"
    )
    more = {
        key: (n, OUT_OF_CLASS[key][0])
        for key, n in found.items()
        if n != OUT_OF_CLASS[key][0]
    }
    assert not more, f"a named unit's count of calls moved, (found, named): {more}"
    gone = sorted(set(OUT_OF_CLASS) - set(found))
    assert not gone, f"named units that no longer split with `splitlines`: {gone}"


def test_the_class_case_sees_a_planted_call(tmp_path):
    """The walk is what the case rests on, so it is asked of a tree with one
    call planted in an unlisted unit and one more call in a listed one."""
    for top in SHIPPED:
        (tmp_path / top).mkdir(parents=True)
    (tmp_path / "skills" / "new.py").write_text(
        "def reader(text):\n    return text.splitlines()\n", encoding="utf-8"
    )
    (tmp_path / "hooks" / "dispatch.py").write_text(
        "def first_line(exc):\n    str(exc).splitlines()\n"
        "    return str(exc).splitlines()\n",
        encoding="utf-8",
    )
    assert splitlines_calls(str(tmp_path)) == {
        ("skills/new.py", "reader"): 1,
        ("hooks/dispatch.py", "first_line"): 2,
    }
