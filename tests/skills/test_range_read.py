"""`skills/implement/scripts/range_read.py`, `seal range`, one class per
function.

A case builds a repository of its own under its `tmp_path`, with a marked
records root and one work item, commits a base and a change, and runs the
command's `main` in that repository; the local-mode case keeps its root
under the git directory, and the case of a missing argument builds none.
Where a case holds a print against git's own, the oracle is `git diff` run
in the same repository with a context that reaches the paragraph's edges
exactly, so the case reads the bound and not a spelling this file chose.
"""

import os
import re

import pytest
from conftest import (
    ROOT,
    census_case,
    commit_everything,
    git,
    git_out,
    load_module,
    local_home,
    mark_root,
    write,
)

TARGET = "skills/implement/scripts/range_read.py"

RANGE = load_module(os.path.join(ROOT, *TARGET.split("/")), "range_read_under_test")

ITEM = "seal/threads/1700000000-a-work-item"
DOC = "docs/a-document.md"

# A configuration that would put text into what `git diff` prints: an
# external diff and a textconv filter that each fail, colour on every
# command, and nearby hunks joined. The command switches each off, and an
# oracle below asks git with the same switches.
HOSTILE = (
    ("diff.external", "false"),
    ("diff.hostile.textconv", "false"),
    ("color.ui", "always"),
    ("diff.interHunkContext", "20"),
)
PLAIN = ("--no-color", "--no-ext-diff", "--no-textconv", "--inter-hunk-context=0")

# A document of three paragraphs: four lines from the file's start, eleven
# in the middle, four to the file's end.
FIRST = [f"First paragraph, line {n}." for n in range(1, 5)]
MIDDLE = [f"Middle paragraph, line {n}." for n in range(1, 12)]
LAST = [f"Last paragraph, line {n}." for n in range(1, 5)]


def document(first=FIRST, middle=MIDDLE, last=LAST, gap=""):
    """The three paragraphs, the blank line GAP between each two."""
    return "\n".join([*first, gap, *middle, gap, *last]) + "\n"


def built(tmp_path, files):
    """A repository at TMP_PATH/repo under `HOSTILE`'s configuration, with
    every path's diff driver the hostile one, a marked root and FILES
    committed as its base; the repository and the base commit."""
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init", "-q")
    git(repo, "config", "user.email", "t@t.example")
    git(repo, "config", "user.name", "t")
    for key, value in HOSTILE:
        git(repo, "config", key, value)
    write(repo, ".gitattributes", "* diff=hostile\n")
    mark_root(repo / "seal")
    write(repo, f"{ITEM}/routing.md", "# Routing\n")
    for rel, text in files.items():
        write(repo, rel, text)
    return repo, commit_everything(repo, "base")


def ran(monkeypatch, capsys, repo, item, start, out):
    """`seal range ITEM --from START --out OUT` run in REPO: the exit code,
    the summary it printed and what it wrote to stderr."""
    monkeypatch.chdir(repo)
    code = RANGE.main([str(item), "--from", start, "--out", str(out)])
    said = capsys.readouterr()
    return code, said.out, said.err


def written(path):
    with open(path, encoding="utf-8", newline="") as handle:
        return handle.read()


def hunks(repo, start, head, path, context):
    """What `git diff -U<CONTEXT>` prints for PATH from its first hunk on,
    each hunk header without the function line git puts after it."""
    out = git_out(repo, "diff", *PLAIN, f"-U{context}", start, head, "--", path)
    body = out[out.index("\n@@") + 1 :]
    return re.sub(r"(?m)^(@@ [^@]* @@).*$", r"\1", body) + "\n"


class Test_main:
    def test_accepts_a_prose_hunk_printed_with_its_paragraph_whole(
        self, tmp_path, monkeypatch, capsys
    ):
        """S4: one sentence changed in the middle of the eleven-line
        paragraph prints the paragraph from the blank line before it to the
        blank line after it, as `git diff -U5` prints that one hunk, and no
        line of the paragraphs around it. A print of `git diff -U3` holds
        three lines each side, and fails here. The blank lines hold a space
        and a tab, which is still blank."""
        repo, base = built(tmp_path, {DOC: document(gap=" \t")})
        changed = [*MIDDLE]
        changed[5] = "Middle paragraph, line 6, rewritten."
        write(repo, DOC, document(middle=changed, gap=" \t"))
        head = commit_everything(repo, "change")
        out = tmp_path / "read.txt"
        code, said, _err = ran(monkeypatch, capsys, repo, repo / ITEM, base, out)
        assert code == 0, said
        text = written(out)
        assert hunks(repo, base, head, DOC, 5) in text
        for line in FIRST + LAST:
            assert line not in text

    def test_accepts_a_hunk_at_each_edge_of_the_file_printed_to_that_edge(
        self, tmp_path, monkeypatch, capsys
    ):
        """S4 at the file's start and end: a paragraph that opens the file
        is printed from its first line, one that ends it to its last, each
        as `git diff -U2` prints it, and the middle paragraph not at all."""
        repo, base = built(tmp_path, {DOC: document()})
        first, last = [*FIRST], [*LAST]
        first[1] = "First paragraph, line 2, rewritten."
        last[2] = "Last paragraph, line 3, rewritten."
        write(repo, DOC, document(first=first, last=last))
        head = commit_everything(repo, "change")
        out = tmp_path / "read.txt"
        code, said, _err = ran(monkeypatch, capsys, repo, repo / ITEM, base, out)
        assert code == 0, said
        text = written(out)
        assert hunks(repo, base, head, DOC, 2) in text
        for line in MIDDLE:
            assert line not in text

    def test_accepts_a_deleted_line_and_two_hunks_of_one_paragraph(
        self, tmp_path, monkeypatch, capsys
    ):
        """A line deleted from the first paragraph prints what is left of
        it whole, and the hunk of the last paragraph after it is numbered
        for the line the deletion took, each as `git diff -U2` prints them;
        two changes in one paragraph print it once, as one hunk, as
        `git diff -U3` prints the pair; and a deletion that opens the file is
        numbered from its first line, as `git diff -U2` prints it."""
        repo, base = built(tmp_path, {DOC: document()})
        last = [*LAST]
        last[2] = "Last paragraph, line 3, rewritten."
        write(repo, DOC, document(first=FIRST[:1] + FIRST[2:], last=last))
        head = commit_everything(repo, "delete")
        out = tmp_path / "read.txt"
        code, said, _err = ran(monkeypatch, capsys, repo, repo / ITEM, base, out)
        assert code == 0, said
        assert hunks(repo, base, head, DOC, 2) in written(out)
        pair = [*MIDDLE]
        pair[3] = "Middle paragraph, line 4, rewritten."
        pair[7] = "Middle paragraph, line 8, rewritten."
        write(repo, DOC, document(first=FIRST[:1] + FIRST[2:], middle=pair, last=last))
        again = commit_everything(repo, "pair")
        code, said, _err = ran(monkeypatch, capsys, repo, repo / ITEM, head, out)
        assert code == 0, said
        text = written(out)
        assert hunks(repo, head, again, DOC, 3) in text
        assert text.count("\n@@ ") == 1
        write(repo, DOC, document(first=FIRST[2:], middle=pair, last=last))
        opened = commit_everything(repo, "delete the first line")
        code, said, _err = ran(monkeypatch, capsys, repo, repo / ITEM, again, out)
        assert code == 0, said
        assert hunks(repo, again, opened, DOC, 2) in written(out)

    def test_accepts_a_one_line_paragraph_an_added_and_an_emptied_file(
        self, tmp_path, monkeypatch, capsys
    ):
        """A one-line paragraph prints as `git diff -U0` prints its hunk, an
        added `.md` path prints whole as `git diff` prints its one hunk, and
        a `.md` path emptied prints the hunk git gives."""
        lone = "docs/lone.md"
        repo, base = built(tmp_path, {lone: "Above.\n\nOnly line.\n\nBelow.\n"})
        write(repo, lone, "Above.\n\nOnly line, rewritten.\n\nBelow.\n")
        write(repo, DOC, document())
        head = commit_everything(repo, "change")
        out = tmp_path / "read.txt"
        code, said, _err = ran(monkeypatch, capsys, repo, repo / ITEM, base, out)
        assert code == 0, said
        text = written(out)
        assert hunks(repo, base, head, lone, 0) in text
        assert hunks(repo, base, head, DOC, 3) in text
        write(repo, DOC, "")
        emptied = commit_everything(repo, "empty")
        code, said, _err = ran(monkeypatch, capsys, repo, repo / ITEM, head, out)
        assert code == 0, said
        assert hunks(repo, head, emptied, DOC, 0) in written(out)

    def test_accepts_a_path_that_reads_as_a_pattern_as_that_path_alone(
        self, tmp_path, monkeypatch, capsys
    ):
        """A path whose name a pathspec would read as a pattern, here one
        that matches a second changed path, prints its own hunks alone."""
        pattern, other = "docs/a[1].md", "docs/a1.md"
        repo, base = built(tmp_path, {pattern: "Pattern.\n", other: "Other.\n"})
        write(repo, pattern, "Pattern, rewritten.\n")
        write(repo, other, "Other, rewritten.\n")
        commit_everything(repo, "change")
        out = tmp_path / "read.txt"
        code, said, _err = ran(monkeypatch, capsys, repo, repo / ITEM, base, out)
        assert code == 0, said
        text = written(out)
        own = text.split(RANGE.PROSE_HEAD.format(path=pattern), 1)[1]
        own = own.split("==> ", 1)[0]
        assert "Pattern, rewritten." in own
        assert "Other" not in own

    def test_accepts_another_text_path_as_git_diff_W_prints_it(
        self, tmp_path, monkeypatch, capsys
    ):
        """A path that is not a `.md` file is printed as `git diff -W`
        prints it, so a changed line deep in a function brings the whole
        function, its `def` line among it, past the blank line the
        function's body holds above the change."""
        body = [f"    step_{n} = {n}" for n in range(1, 12)]
        body[3] = ""
        code_text = "def unit():\n" + "\n".join(body) + "\n    return step_1\n"
        repo, base = built(tmp_path, {"lib/unit.py": code_text})
        body[6] = "    step_7 = 70"
        write(
            repo,
            "lib/unit.py",
            "def unit():\n" + "\n".join(body) + "\n    return step_1\n",
        )
        head = commit_everything(repo, "change")
        out = tmp_path / "read.txt"
        code, said, _err = ran(monkeypatch, capsys, repo, repo / ITEM, base, out)
        assert code == 0, said
        whole = git(repo, "diff", *PLAIN, "-W", base, head, "--", "lib/unit.py").stdout
        assert whole in written(out)

    def test_accepts_a_hunk_inside_a_docstring_widened_to_its_paragraph(
        self, tmp_path, monkeypatch, capsys
    ):
        """S11: a line changed in the middle of the eleven-line paragraph of
        a module's docstring, where every line opens with a letter and so
        reads to `git diff -W` as a function line, prints the paragraph from
        the blank line before it to the blank line after it, as
        `git diff -U5` prints that one hunk. `git diff -W` alone prints from
        the paragraph's third line, and fails here."""
        path = "lib/module.py"

        def module(middle):
            return '"""A module.\n\n' + "\n".join(middle) + '\n\n"""\n\nimport os\n'

        repo, base = built(tmp_path, {path: module(MIDDLE)})
        changed = [*MIDDLE]
        changed[5] = "Middle paragraph, line 6, rewritten."
        write(repo, path, module(changed))
        head = commit_everything(repo, "change")
        out = tmp_path / "read.txt"
        code, said, _err = ran(monkeypatch, capsys, repo, repo / ITEM, base, out)
        assert code == 0, said
        assert hunks(repo, base, head, path, 5) in written(out)

    def test_accepts_the_records_whole_at_head_and_names_each_absent(
        self, tmp_path, monkeypatch, capsys
    ):
        """S5: over a range that changes no record, the file still holds
        `routing.md`, the three frame files and `changelog.md` whole as HEAD
        has them, each under the line naming it, and names `gaps.md`, which
        HEAD does not hold, in the file and in the summary."""
        records = {
            "frame/design.md": "# Design\n\nA design.\n\n## Scope\n\nIn.\n",
            "frame/plan.md": "# Plan\n\n| Phase | Status |\n|---|---|\n| 1 | |\n",
            "frame/questions.md": "# Questions\n\nNone.\n",
            "changelog.md": "### Fixed\n\n- A fix.\n",
        }
        repo, base = built(
            tmp_path, {f"{ITEM}/{name}": text for name, text in records.items()}
        )
        records["routing.md"] = "# Routing\n"
        out = tmp_path / "read.txt"
        code, said, _err = ran(monkeypatch, capsys, repo, repo / ITEM, base, out)
        assert code == 0, said
        text = written(out)
        for name, record in records.items():
            assert RANGE.RECORD.format(path=f"{ITEM}/{name}") + "\n" + record in text
        assert RANGE.ABSENT.format(path=f"{ITEM}/gaps.md") in text
        assert f"{ITEM}/gaps.md" in said

    def test_accepts_a_local_root_reading_the_records_on_disk(
        self, tmp_path, monkeypatch, capsys
    ):
        """In local mode the records stand under the git directory, where
        HEAD holds none, so the file reads them on disk and says so on the
        line naming each, or names one that is not there."""
        repo = tmp_path / "repo"
        repo.mkdir()
        git(repo, "init", "-q")
        git(repo, "config", "user.email", "t@t.example")
        git(repo, "config", "user.name", "t")
        write(repo, "f.txt", "one\n")
        base = commit_everything(repo, "base")
        item = local_home(repo) / "threads" / "1700000000-a-work-item"
        write(item, "routing.md", "# Routing, local\n")
        out = tmp_path / "read.txt"
        code, said, _err = ran(monkeypatch, capsys, repo, item, base, out)
        assert code == 0, said
        text = written(out)
        name = os.path.relpath(item / "routing.md", repo).replace(os.sep, "/")
        assert RANGE.ON_DISK.format(path=name) + "\n# Routing, local\n" in text
        gaps = os.path.relpath(item / "gaps.md", repo).replace(os.sep, "/")
        assert RANGE.ABSENT_ON_DISK.format(path=gaps) in text
        assert RANGE.NOT_PRINTED.format(path=gaps, why="absent") in said

    def test_accepts_a_binary_path_by_name_and_does_not_print_it(
        self, tmp_path, monkeypatch, capsys
    ):
        """S6: a binary path is named in the file and in the summary, and
        git's line on it is not printed."""
        repo, base = built(tmp_path, {})
        (repo / "image.bin").write_bytes(b"\x00\x01\x02binary")
        commit_everything(repo, "binary")
        out = tmp_path / "read.txt"
        code, said, _err = ran(monkeypatch, capsys, repo, repo / ITEM, base, out)
        assert code == 0, said
        text = written(out)
        assert RANGE.BINARY.format(path="image.bin") in text
        assert "Binary files" not in text
        assert RANGE.NOT_PRINTED.format(path="image.bin", why="binary") in said

    def test_accepts_a_renamed_path_as_one_deleted_and_one_added(
        self, tmp_path, monkeypatch, capsys
    ):
        """A rename is the old path named as deleted and the new one printed
        whole, as git reads a rename with `--no-renames`."""
        repo, base = built(tmp_path, {"docs/old.md": "Moved.\n"})
        git(repo, "mv", "docs/old.md", "docs/new.md")
        head = commit_everything(repo, "rename")
        out = tmp_path / "read.txt"
        code, said, _err = ran(monkeypatch, capsys, repo, repo / ITEM, base, out)
        assert code == 0, said
        text = written(out)
        assert RANGE.DELETED.format(path="docs/old.md") in text
        assert hunks(repo, base, head, "docs/new.md", 3) in text

    def test_accepts_a_deleted_path_by_name_and_does_not_print_it(
        self, tmp_path, monkeypatch, capsys
    ):
        """S6: a path the range deletes is named in the file and in the
        summary, and none of its lines is printed."""
        repo, base = built(tmp_path, {DOC: document()})
        git(repo, "rm", "-q", DOC)
        commit_everything(repo, "delete")
        out = tmp_path / "read.txt"
        code, said, _err = ran(monkeypatch, capsys, repo, repo / ITEM, base, out)
        assert code == 0, said
        text = written(out)
        assert RANGE.DELETED.format(path=DOC) in text
        assert MIDDLE[0] not in text
        assert RANGE.NOT_PRINTED.format(path=DOC, why="deleted") in said

    def test_accepts_an_uncommitted_change_named_as_not_read(
        self, tmp_path, monkeypatch, capsys
    ):
        """S6: a tracked path with an uncommitted change is named as not
        read in the summary, and the file holds HEAD's text of it. A rename
        staged and not committed names both paths, and an untracked file
        is not named."""
        repo, base = built(tmp_path, {"docs/old.md": "Old.\n"})
        write(repo, f"{ITEM}/routing.md", "# Routing, edited and not committed\n")
        git(repo, "mv", "docs/old.md", "docs/new.md")
        write(repo, "untracked.txt", "untracked\n")
        out = tmp_path / "read.txt"
        code, said, _err = ran(monkeypatch, capsys, repo, repo / ITEM, base, out)
        assert code == 0, said
        text = written(out)
        assert "not committed" not in text
        assert "# Routing\n" in text
        for path in (f"{ITEM}/routing.md", "docs/old.md", "docs/new.md"):
            assert RANGE.NOT_READ.format(path=path) in said
        assert "untracked.txt" not in said

    def test_accepts_the_range_line_first_and_counts_the_lines_written(
        self, tmp_path, monkeypatch, capsys
    ):
        """The file opens with the range as two full hashes, and the
        summary gives the range, the file's path and how many lines it
        wrote."""
        repo, base = built(tmp_path, {DOC: document()})
        write(repo, DOC, document(last=LAST[:3]))
        head = commit_everything(repo, "change")
        out = tmp_path / "read.txt"
        code, said, _err = ran(monkeypatch, capsys, repo, repo / ITEM, "HEAD~1", out)
        assert code == 0, said
        text = written(out)
        assert text.split("\n", 1)[0] == f"range: {base}..{head}"
        assert f"seal range: {base}..{head}" in said
        assert RANGE.WROTE.format(out=out, lines=text.count("\n")) in said

    @pytest.mark.parametrize(
        "start, why",
        [
            ("no-such-commit", "does not resolve"),
            ("aside", "is not an ancestor of HEAD"),
        ],
    )
    def test_refuses_a_commit_that_does_not_start_the_range(
        self, tmp_path, monkeypatch, capsys, start, why
    ):
        """S6: a `--from` that names no commit, or one HEAD does not
        descend from, ends at exit 2 with the reason and writes no file."""
        repo, _base = built(tmp_path, {})
        git(repo, "checkout", "-q", "-b", "aside")
        write(repo, "aside.txt", "aside\n")
        commit_everything(repo, "aside")
        git(repo, "checkout", "-q", "-")
        write(repo, "main.txt", "main\n")
        commit_everything(repo, "main")
        out = tmp_path / "read.txt"
        code, _said, err = ran(monkeypatch, capsys, repo, repo / ITEM, start, out)
        assert code == 2
        assert why in err
        assert not out.exists()

    @pytest.mark.parametrize("where", ["docs", "seal", "seal/threads"])
    def test_refuses_a_directory_that_is_no_work_items(
        self, tmp_path, monkeypatch, capsys, where
    ):
        """S6: a directory that is not one directly under the marked root's
        work items ends at exit 2 and writes no file."""
        repo, base = built(tmp_path, {"docs/a.md": "A.\n"})
        out = tmp_path / "read.txt"
        code, _said, err = ran(monkeypatch, capsys, repo, repo / where, base, out)
        assert code == 2
        assert "is not a work item's directory" in err
        assert not out.exists()

    def test_refuses_a_missing_argument_at_exit_2(self, tmp_path, monkeypatch):
        """An argument left out ends at exit 2 before anything is read."""
        monkeypatch.chdir(tmp_path)
        with pytest.raises(SystemExit) as caught:
            RANGE.main([str(tmp_path), "--out", str(tmp_path / "read.txt")])
        assert caught.value.code == 2
        assert not (tmp_path / "read.txt").exists()


test_census = census_case(TARGET)
