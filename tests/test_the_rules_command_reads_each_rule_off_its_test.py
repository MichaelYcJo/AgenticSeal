"""`rules <doc>` prints each section with what its tests say they guard, and
`rules --check` fails where a target does not resolve.

A rule's text lives once, as the first sentence of the docstring of the test
that holds it, and a document lists its tests by `Enforced by:` (#944).
`.github/scripts/rules.py` reads the two together and prints them; it writes
nothing, because a committed copy would be a second source. `rules <doc>`
never fails for what it finds; `rules --check` reads every rule file and is
exit 1 where a target is gone, and one case here runs it over the tree, so
the suite is where the fact is read (#923 item 3).
"""

import fnmatch
import importlib.util
import os
import re
import shutil
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


CONSTANT = 1
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
    """`docs/the-record-layout.md`, the document #944's phase 1 gave every
    rule its test, prints a section line for each of its targets and none
    that does not resolve."""
    path = os.path.join(ROOT, "docs", "the-record-layout.md")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    out = rules.render(ROOT, text)
    assert out.count("  Enforced by, line ") >= 7, out
    assert "does not resolve" not in out, out


# --- `rules --check` -------------------------------------------------------

HELD = "tests/test_x.py"
HELD_CASE = f"{HELD}::test_held"


def rule(enforced):
    """One rule paragraph closed by `Enforced by: <enforced>`."""
    return f"**A rule.** Its one why.\nEnforced by: {enforced}\n"


def doc(*paragraphs):
    """A rule file whose paragraphs stand under `## The heading`, from line 5."""
    return "# D\n\n## The heading\n\n" + "\n".join(paragraphs)


def checked(tmp_path, files, capsys):
    """`(exit, stdout)` of `rules --check` over a tree holding the test module
    and `files`, each `{path: text}`."""
    for rel, text in {HELD: TESTS, **files}.items():
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, "utf-8", newline="\n")
    code = rules.main(["--check", "--root", str(tmp_path)])
    return code, capsys.readouterr().out


@pytest.mark.parametrize(
    "target, verdict, said",
    [
        (
            "tests/test_x.py::test_gone",
            1,
            "rules: docs/a.md:6 §*The heading*: tests/test_x.py::test_gone: no def "
            "or class named test_gone in tests/test_x.py",
        ),
        ("tests/test_gone.py", 1, "tests/test_gone.py does not exist"),
        (
            "tests/test_x.py::CONSTANT",
            1,
            "no def or class named CONSTANT in tests/test_x.py",
        ),
        (f"{HELD}, tests/test_gone.py", 1, "tests/test_gone.py does not exist"),
        (HELD_CASE, 0, "rules: all 1 `Enforced by:` targets in 1 rule files resolve."),
        (
            f"{HELD_CASE}, {HELD}",
            0,
            "rules: all 2 `Enforced by:` targets in 1 rule files resolve.",
        ),
        ("nothing", 1, "nothing does not exist"),
    ],
    ids=[
        "a case gone",
        "a file gone",
        "a constant",
        "one of two",
        "a case",
        "two",
        "nothing with no why",
    ],
)
def test_an_enforced_by_target_that_does_not_resolve_fails_naming_where(
    tmp_path, capsys, target, verdict, said
):
    """A target that is gone, or names a constant, is exit 1 naming the file,
    the `Enforced by:` line, the heading it stands under and why; a target
    that resolves holds. Every target of the line is read, not the first, and
    a `nothing` with no `— <why>` is read as a target."""
    code, out = checked(tmp_path, {"docs/a.md": doc(rule(target))}, capsys)
    assert code == verdict, out
    assert said in out, out
    if verdict:
        assert "rules: 1 of " in out and " do not resolve." in out, out


def test_an_enforced_by_line_outside_a_rule_or_inside_a_fence_is_read_or_skipped(
    tmp_path, capsys
):
    """Every `Enforced by:` line a renderer shows is resolved, inside a rule
    paragraph or not, in every rule file; one in a fence is an example and
    is not, and `nothing — <why>` names no target."""
    text = doc(
        "A sentence that states no rule.\nEnforced by: tests/test_gone_a.py\n",
        "```\nEnforced by: tests/test_gone_b.py\n```\n",
        "Enforced by: nothing — only a reader can tell\n",
    )
    code, out = checked(tmp_path, {"agents/warden.md": text}, capsys)
    assert code == 1, out
    assert (
        "agents/warden.md:6 §*The heading*: tests/test_gone_a.py does not exist" in out
    )
    assert "test_gone_b" not in out, out
    assert "rules: 1 of 1 `Enforced by:` targets in 1 rule files" in out, out


@pytest.mark.parametrize(
    "files, verdict, said",
    [
        ({"case.yaml": "name: a\n"}, 0, "rules: all 1 `Enforced by:` targets"),
        ({"prompt.md": "Review.\n"}, 1, "holds no case.yaml"),
    ],
    ids=["with its case.yaml", "without"],
)
def test_an_eval_case_directory_resolves_where_its_case_yaml_is(
    tmp_path, capsys, files, verdict, said
):
    """An agent's rule can be held by an eval case alone, so
    `evals/behaviour/<agent>/<case>/` is a target, resolving where the
    directory holds `case.yaml`."""
    case = "evals/behaviour/warden/a-case/"
    written = {"docs/a.md": doc(rule(case))}
    written.update({case + name: text for name, text in files.items()})
    code, out = checked(tmp_path, written, capsys)
    assert code == verdict, out
    assert said in out, out


def test_an_eval_target_that_names_no_case_is_refused(tmp_path, capsys):
    """The directory is `<agent>/<case>/`, so an agent's directory alone names
    no case and does not resolve."""
    written = {
        "docs/a.md": doc(rule("evals/behaviour/warden/")),
        "evals/behaviour/warden/case.yaml": "name: a\n",
    }
    code, out = checked(tmp_path, written, capsys)
    assert code == 1, out
    assert "is no eval case: write `evals/behaviour/<agent>/<case>/`" in out, out


def test_a_check_and_a_document_together_or_neither_is_exit_2(tmp_path, capsys):
    """`--check` reads every rule file and a document names one, so asking for
    both, or for neither, is a usage error and reads nothing."""
    root = tree(tmp_path, rule(HELD_CASE))
    assert rules.main(["--check", "docs/a.md", "--root", str(root)]) == 2
    assert rules.main(["--root", str(root)]) == 2
    captured = capsys.readouterr()
    assert captured.out == "", captured.out
    assert "rules: name a document, or --check, and not both." in captured.err


def test_every_enforced_by_target_in_the_tree_resolves(tmp_path, capsys):
    """The fact read on every pull request: `rules --check` over this tree is
    exit 0. On a scratch copy of what the check reads — the rule files and
    the files their targets name — one target renamed is exit 1 naming its
    line, and so is a gone target planted in a file of every other rule-file
    glob, so a walk that read `docs/*.md` alone, or read a renamed target as
    resolving, goes red here."""
    assert rules.main(["--check", "--root", ROOT]) == 0, capsys.readouterr().out
    capsys.readouterr()
    files = rules.rule_files(ROOT)
    named, renamed = {}, None
    for rel, text in files.items():
        held = [(n, rules.targets_of(v)) for n, _, v in rules.enforcer_lines(text)]
        for target in (t for _, targets in held for t in targets):
            cell = target.strip().strip("`")
            source = cell + rules.EVAL_CASE if cell.endswith("/") else cell
            source = source.partition("::")[0]
            destination = tmp_path / source
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(os.path.join(ROOT, *source.split("/")), destination)
        pattern = next(p for p in rules.RULE_FILES if fnmatch.fnmatchcase(rel, p))
        line = next((n for n, targets in held if targets), None)
        if renamed is None and line is not None:
            lines = text.split("\n")
            first = rules.targets_of(lines[line - 1].split(":", 1)[1].strip())[0]
            lines[line - 1] = lines[line - 1].replace(
                first.strip(), f"{first.strip()}_renamed_away", 1
            )
            text, renamed, named[pattern] = "\n".join(lines), rel, rel
        elif pattern not in named:
            text += "\n\nEnforced by: tests/test_planted_and_gone.py\n"
            named[pattern] = rel
        destination = tmp_path / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text, "utf-8", newline="\n")
    assert renamed is not None, "no rule file in the tree names a target"
    assert set(named) == set(rules.RULE_FILES), named
    assert rules.main(["--check", "--root", str(tmp_path)]) == 1
    out = capsys.readouterr().out
    assert re.search(rf"^rules: {re.escape(renamed)}:\d+ §\*.*_renamed_away", out, re.M)
    for rel in named.values():
        assert re.search(rf"^rules: {re.escape(rel)}:\d+ §\*", out, re.M), (rel, out)
    assert f"rules: {len(named)} of " in out, out
