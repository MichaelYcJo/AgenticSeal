"""`rules <doc>` prints each section with what its tests say they guard.

Work item 1791940762 (#944), the owner's decision of 2026-10-14: a rule's text
lives once, as the first sentence of the docstring of the test that holds it,
and a document lists its tests by `Enforced by:`. `.github/scripts/rules.py`
reads the two together and prints them; it writes nothing, because a
committed copy would be a second source. A target is resolved by the
resolver the `enforced-unresolved` budget row reads with, and the command
never fails for what it finds — that row is what fails.
"""

import importlib.util
import os
import subprocess

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, ".github", "scripts", "rules.py")


def _load():
    spec = importlib.util.spec_from_file_location("specseal_rules", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


rules = _load()

TESTS = '''"""The module guards a whole thing. It says more."""


def test_held():
    """A held rule is guarded. The rest is grounds."""


def test_bare():
    pass


class TestGroup:
    def test_inner(self):
        """An inner case
        wraps its sentence."""
'''


def tree(tmp_path, text):
    """A repository holding `docs/a.md` as `text` and one test module."""
    (tmp_path / "docs").mkdir()
    (tmp_path / "tests").mkdir()
    (tmp_path / "docs" / "a.md").write_text(text, "utf-8", newline="\n")
    (tmp_path / "tests" / "test_x.py").write_text(TESTS, "utf-8", newline="\n")
    return tmp_path


def run(root, capsys):
    code = rules.main([str(root / "docs" / "a.md"), "--root", str(root)])
    captured = capsys.readouterr()
    return code, captured.out, captured.err


@pytest.mark.parametrize(
    "target, said",
    [
        (
            "tests/test_x.py::test_held",
            "tests/test_x.py::test_held — A held rule is guarded.",
        ),
        ("tests/test_x.py", "tests/test_x.py — The module guards a whole thing."),
        (
            "tests/test_x.py::TestGroup::test_inner",
            "tests/test_x.py::TestGroup::test_inner — An inner case wraps its sentence.",
        ),
        ("tests/test_x.py::test_bare", "tests/test_x.py::test_bare — (no docstring)"),
        (
            "tests/test_x.py::test_gone",
            "tests/test_x.py::test_gone — does not resolve: tests/test_x.py::test_gone: "
            "no def or class named test_gone in tests/test_x.py",
        ),
        (
            "tests/test_gone.py",
            "tests/test_gone.py — does not resolve: tests/test_gone.py does not exist",
        ),
    ],
    ids=[
        "a case",
        "a module",
        "a method",
        "no docstring",
        "a case gone",
        "a file gone",
    ],
)
def test_each_target_prints_its_first_sentence_or_why_it_has_none(
    tmp_path, capsys, target, said
):
    """Each target prints under its section with its docstring's first
    sentence, `(no docstring)`, or why it does not resolve, and the command
    exits 0 whatever it found."""
    root = tree(
        tmp_path, f"# A\n\n## The section\n\n**A rule.**\nEnforced by: {target}\n"
    )
    code, out, _ = run(root, capsys)
    assert code == 0
    assert out.startswith("# A\n  (no `Enforced by:` line)\n\n## The section\n"), out
    assert f"\n    {said}\n" in out, out


GATED = '''import sys

import pytest

if sys.platform:

    @pytest.mark.slow
    def test_gated():
        """A gated case is read. More."""


class TestGroup:
    try:

        def test_tried(self):
            """A tried method is read."""

    except ImportError:
        pass
'''


@pytest.mark.parametrize(
    "target, said",
    [
        ("tests/test_g.py::test_gated", "A gated case is read."),
        ("tests/test_g.py::TestGroup::test_tried", "A tried method is read."),
    ],
    ids=["under an if, decorated", "a method under a try"],
)
def test_a_target_the_resolver_finds_in_a_block_prints_its_sentence(
    tmp_path, capsys, target, said
):
    """A unit the resolver finds inside an `if` or a `try` is described from
    the same unit, at exit 0, never a traceback."""
    root = tree(tmp_path, f"## A\n\n**R.** Why.\nEnforced by: {target}\n")
    (root / "tests" / "test_g.py").write_text(GATED, "utf-8", newline="\n")
    code, out, _ = run(root, capsys)
    assert code == 0
    assert f"\n    {target} — {said}\n" in out, out


@pytest.mark.parametrize("where", ["top", "subdirectory"])
def test_with_no_root_the_targets_resolve_where_the_command_runs(
    tmp_path, capsys, monkeypatch, where
):
    """`rules <doc>` with no `--root` resolves in the repository it is typed
    in, from its top or a subdirectory, not in the tree the script ships in."""
    root = tree(
        tmp_path, "## A\n\n**Held.** Why.\nEnforced by: tests/test_x.py::test_held\n"
    )
    doc = "docs/a.md"
    if where == "subdirectory":
        subprocess.run(["git", "init", "-q", str(root)], check=True)
        monkeypatch.chdir(root / "docs")
        doc = "a.md"
    else:
        monkeypatch.chdir(root)
    assert rules.main([doc]) == 0
    out = capsys.readouterr().out
    assert "    tests/test_x.py::test_held — A held rule is guarded.\n" in out, out


def test_an_eval_case_and_a_nothing_line_are_printed_as_what_they_are(tmp_path, capsys):
    """An eval case directory resolves and is named as one; `nothing — <why>`
    names no target and prints its reason as written."""
    root = tree(
        tmp_path,
        "## One\n\nEnforced by: evals/behaviour/warden/a/\n\n"
        "## Two\n\nEnforced by: nothing — no case reads it\n",
    )
    case = root / "evals" / "behaviour" / "warden" / "a"
    case.mkdir(parents=True)
    (case / "case.yaml").write_text("name: a\n", "utf-8")
    code, out, _ = run(root, capsys)
    assert code == 0
    assert "    evals/behaviour/warden/a/ — an eval case\n" in out, out
    assert "    nothing — no case reads it\n" in out, out


def test_a_fenced_line_is_an_example_and_writes_nothing(tmp_path, capsys):
    """A fenced `Enforced by:` is an example, so the section reads as having
    none; and the run leaves the tree exactly as it found it."""
    root = tree(tmp_path, "## One\n\n```\nEnforced by: tests/test_x.py\n```\n")
    before = sorted(
        (p, os.path.getsize(os.path.join(d, p)))
        for d, _, files in os.walk(root)
        for p in files
    )
    code, out, _ = run(root, capsys)
    after = sorted(
        (p, os.path.getsize(os.path.join(d, p)))
        for d, _, files in os.walk(root)
        for p in files
    )
    assert code == 0
    assert out == "## One\n  (no `Enforced by:` line)\n", out
    assert before == after


def test_a_document_that_cannot_be_read_is_exit_2(tmp_path, capsys):
    """Nothing was read, so nothing is printed as if it had been."""
    code = rules.main([str(tmp_path / "missing.md"), "--root", str(tmp_path)])
    captured = capsys.readouterr()
    assert code == 2
    assert "rules: cannot read" in captured.err
    assert captured.out == ""


def test_the_slice_document_resolves_every_target():
    """`docs/the-record-layout.md`, the document #944's phase 1 takes to no
    unenforced rule, prints a section line for each of its targets and none
    that does not resolve."""
    path = os.path.join(ROOT, "docs", "the-record-layout.md")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    out = rules.render(rules.checker(), ROOT, text)
    assert out.count("  Enforced by, line ") >= 7, out
    assert "does not resolve" not in out, out
