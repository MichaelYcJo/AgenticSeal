"""`rules <doc>` prints each section with what its tests say they guard, and
`rules --check` fails where a check line is refused.

A rule's text lives once, as the first sentence of the docstring of the test
that holds it, and a rule file lists its tests by `check:` line, in the
grammar `skills/settle/SKILL.md` *A rule has one shape* states.
`.github/scripts/rules.py` reads the two together and prints them; it writes
nothing, because a committed copy would be a second source. `rules <doc>`
never fails for what it finds; `rules --check` reads every rule file and is
exit 1 where a line is out of grammar or a target is gone, and one case here
runs it over the tree, so the suite is where the fact is read.
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
SETTLE = os.path.join(ROOT, "skills", "settle", "SKILL.md")


def _load():
    spec = importlib.util.spec_from_file_location("specseal_rules", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


rules = _load()

TESTS = '''"""The module guards a whole thing. It says more."""

import pytest


@pytest.mark.rule("held-rule")
def test_held():
    """A held rule is guarded. The rest is grounds."""


@pytest.mark.rule("bare-rule")
def test_bare():
    pass


class TestGroup:
    @pytest.mark.rule("inner-rule")
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
        ("tests/test_x.py", "tests/test_x.py: The module guards a whole thing."),
        ("held-rule", "held-rule: tests/test_x.py test_held: A held rule is guarded."),
        (
            "inner-rule",
            "inner-rule: tests/test_x.py TestGroup.test_inner: An inner case wraps "
            "its sentence.",
        ),
        ("bare-rule", "bare-rule: tests/test_x.py test_bare: (no docstring)"),
        (
            "gone-rule",
            "gone-rule: does not resolve: no test carries the marker `gone-rule`",
        ),
        (
            "tests/test_gone.py",
            "tests/test_gone.py: does not resolve: tests/test_gone.py does not exist",
        ),
    ],
    ids=[
        "a file",
        "a marker",
        "a method's marker",
        "no docstring",
        "a marker gone",
        "a file gone",
    ],
)
def test_each_target_prints_its_first_sentence_or_why_it_has_none(
    tmp_path, capsys, target, said
):
    """S1, S3. Each target prints under its section with the first sentence of
    the docstring it names: a file's module docstring, or each test carrying a
    marker; `(no docstring)`, or why it does not resolve. The command exits 0
    whatever it found."""
    root = tree(tmp_path, f"# A\n\n## The section\n\n**A rule.**\ncheck: {target}\n")
    code, out, _ = run(root, capsys)
    assert code == 0
    assert out.startswith("# A\n  (no check line)\n\n## The section\n"), out
    assert f"\n    {said}\n" in out, out


GATED = '''import sys

import pytest

if sys.platform:

    @pytest.mark.rule("gated-rule")
    @pytest.mark.slow
    def test_gated():
        """A gated case is read. More."""


class TestGroup:
    try:

        @pytest.mark.rule("tried-rule")
        def test_tried(self):
            """A tried method is read."""

    except ImportError:
        pass
'''


@pytest.mark.parametrize(
    "target, said",
    [
        ("gated-rule", "tests/test_g.py test_gated: A gated case is read."),
        ("tried-rule", "tests/test_g.py TestGroup.test_tried: A tried method is read."),
    ],
    ids=["under an if, decorated twice", "a method under a try"],
)
def test_a_marker_on_a_test_inside_a_block_is_read(tmp_path, capsys, target, said):
    """A test pytest collects inside an `if` or a `try` carries its marker as
    any other does, and is described from its own docstring, at exit 0."""
    root = tree(tmp_path, f"## A\n\n**R.** Why.\ncheck: {target}\n")
    (root / "tests" / "test_g.py").write_text(GATED, "utf-8", newline="\n")
    code, out, _ = run(root, capsys)
    assert code == 0
    assert f"\n    {target}: {said}\n" in out, out


@pytest.mark.parametrize("where", ["top", "subdirectory"])
def test_with_no_root_the_targets_resolve_where_the_command_runs(
    tmp_path, capsys, monkeypatch, where
):
    """`rules <doc>` with no `--root` resolves in the repository it is typed
    in, from its top or a subdirectory, not in the tree the script ships in."""
    root = tree(tmp_path, "## A\n\n**Held.** Why.\ncheck: held-rule\n")
    doc = "docs/a.md"
    if where == "subdirectory":
        subprocess.run(["git", "init", "-q", str(root)], check=True)
        monkeypatch.chdir(root / "docs")
        doc = "a.md"
    else:
        monkeypatch.chdir(root)
    assert rules.main([doc]) == 0
    out = capsys.readouterr().out
    assert "    held-rule: tests/test_x.py test_held: A held rule is guarded.\n" in out


def test_a_refused_line_is_printed_with_why(tmp_path, capsys):
    """`rules <doc>` prints a line out of grammar under its section with the
    reason `--check` refuses it, and still exits 0."""
    root = tree(tmp_path, "## One\n\nEnforced by: tests/test_x.py\n")
    code, out, _ = run(root, capsys)
    assert code == 0
    assert (
        "  check, line 3:\n    refused: `Enforced by: tests/test_x.py` is no check "
        "line: write `check: <targets>` or `check: none reader: <who reads it>`\n"
    ) in out, out


def test_a_test_under_a_dot_directory_is_not_read_for_markers(tmp_path, capsys):
    """A virtual environment or a tool's cache holds `test_*.py` files that
    are no test of the repository, and one may not parse here: the walk skips
    every directory whose name starts with a dot."""
    hidden = tmp_path / ".venv" / "lib"
    hidden.mkdir(parents=True)
    (hidden / "test_vendored.py").write_text(
        'import pytest\n\n@pytest.mark.rule("hidden-rule")\ndef test_x(:\n',
        "utf-8",
    )
    code, out = checked(tmp_path, {"docs/a.md": doc(rule("check: held-rule"))}, capsys)
    assert code == 0, out
    code, out = checked(
        tmp_path, {"docs/a.md": doc(rule("check: hidden-rule"))}, capsys
    )
    assert code == 1, out
    assert "no test carries the marker `hidden-rule`" in out, out


def test_an_eval_case_and_a_no_target_line_are_printed_as_what_they_are(
    tmp_path, capsys
):
    """S4's reading half. An eval case directory resolves and is named as one;
    `check: none reader: <who>` names no target and prints its reader."""
    root = tree(
        tmp_path,
        "## One\n\ncheck: evals/behaviour/warden/a/\n\n"
        "## Two\n\ncheck: none reader: the warden at review\n",
    )
    case = root / "evals" / "behaviour" / "warden" / "a"
    case.mkdir(parents=True)
    (case / "case.yaml").write_text("name: a\n", "utf-8")
    code, out, _ = run(root, capsys)
    assert code == 0
    assert "    evals/behaviour/warden/a/: an eval case\n" in out, out
    assert "    no target, read by the warden at review\n" in out, out


def test_a_fenced_or_commented_line_is_an_example_and_writes_nothing(tmp_path, capsys):
    """S6. A `check:` line, or a refused spelling, inside a fence or an HTML
    comment is an example: the section reads as having none, `--check`
    neither resolves nor refuses it, and the run leaves the tree as it was."""
    root = tree(
        tmp_path,
        "## One\n\n```\ncheck: tests/test_gone.py\nEnforced by: x\n```\n\n"
        "<!--\ncheck: tests/test_gone.py\n-->\n",
    )
    before = sorted(
        (p, os.path.getsize(os.path.join(d, p)))
        for d, _, files in os.walk(root)
        for p in files
    )
    code, out, _ = run(root, capsys)
    assert rules.main(["--check", "--root", str(root)]) == 0, capsys.readouterr()
    after = sorted(
        (p, os.path.getsize(os.path.join(d, p)))
        for d, _, files in os.walk(root)
        for p in files
    )
    assert code == 0
    assert out == "## One\n  (no check line)\n", out
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
    assert out.count("  check, line ") >= 7, out
    assert "does not resolve" not in out and "refused" not in out, out


def test_the_rule_marker_is_registered(pytestconfig):
    """`tests/conftest.py` registers `rule`, so a gate test carries it with no
    unknown-mark warning."""
    assert any(line.startswith("rule(") for line in pytestconfig.getini("markers")), (
        pytestconfig.getini("markers")
    )


def test_settle_owns_the_grammar():
    """The grammar is stated once, in the settle skill, the document a spec's
    author reads; this module and `rules.py` only read it."""
    with open(SETTLE, encoding="utf-8") as handle:
        text = handle.read()
    section = text.split("\n## A rule has one shape\n")[1].split("\n## ")[0]
    section = " ".join(section.split())
    for phrase in (
        "starts with `check: `",
        "`check: none reader: <who reads it>`",
        '`@pytest.mark.rule("<marker>")`',
        "It ships `rules --check`",
        "it is review's to find",
    ):
        assert phrase in section, f"settle no longer says: {phrase!r}"


# --- `rules --check` -------------------------------------------------------

HELD = "tests/test_x.py"


def rule(line):
    """One rule paragraph closed by LINE."""
    return f"**A rule.** Its one why.\n{line}\n"


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
    "line, said",
    [
        (f"check: {HELD}", "rules: all 1 check lines in 1 rule files hold."),
        (f"check: {HELD} held-rule", "rules: all 1 check lines in 1 rule files hold."),
        (
            "check: none reader: the warden at review",
            "rules: all 1 check lines in 1 rule files hold.",
        ),
        (f"  check: {HELD}", "rules: all 1 check lines in 1 rule files hold."),
    ],
    ids=["a file", "S2 two targets", "S4 no target", "indented under a list item"],
)
def test_a_check_line_in_grammar_holds(tmp_path, capsys, line, said):
    """S1, S2, S4. A line of resolving targets, one space apart, or the
    no-target form with its reader, is exit 0."""
    code, out = checked(tmp_path, {"docs/a.md": doc(rule(line))}, capsys)
    assert code == 0, out
    assert said in out, out


EXPECTED = "write `check: <targets>` or `check: none reader: <who reads it>`"


@pytest.mark.parametrize(
    "line, why",
    [
        (f"Enforced by: {HELD}", f"`Enforced by: {HELD}` is no check line: {EXPECTED}"),
        (f"Check: {HELD}", f"`Check: {HELD}` is no check line: {EXPECTED}"),
        (f"**check:** {HELD}", f"`**check:** {HELD}` is no check line: {EXPECTED}"),
        (f"check : {HELD}", f"`check : {HELD}` is no check line: {EXPECTED}"),
        (f"- check: {HELD}", f"`- check: {HELD}` is no check line: {EXPECTED}"),
        (f"checks: {HELD}", f"`checks: {HELD}` is no check line: {EXPECTED}"),
        (f"check: {HELD}::test_held", f"`::` is no part of a check line: {EXPECTED}"),
        (f"check: {HELD}, {HELD}", f"`,` is no part of a check line: {EXPECTED}"),
        ("check: none — a reader", f"`—` is no part of a check line: {EXPECTED}"),
        ("check: none", f"a line naming no target names its reader: {EXPECTED}"),
        (
            "check: none reader:",
            f"a line naming no target names its reader: {EXPECTED}",
        ),
        (
            "check: none reader the warden",
            f"a line naming no target names its reader: {EXPECTED}",
        ),
        (f"check: {HELD}  held-rule", "targets are separated by one space"),
        ("check: gone-rule", "no test carries the marker `gone-rule`"),
        ("check: tests/test_gone.py", "tests/test_gone.py does not exist"),
        (f"check: {HELD} tests/test_gone.py", "tests/test_gone.py does not exist"),
    ],
    ids=[
        "the old label",
        "a capital",
        "in bold",
        "a space before the colon",
        "a list bullet",
        "a plural",
        "a test named after the path",
        "a comma",
        "an em dash",
        "none alone",
        "a reader with nothing after it",
        "a reader with no colon",
        "two spaces",
        "a marker no test carries",
        "a file gone",
        "one of two gone",
    ],
)
def test_every_other_spelling_is_refused_at_its_line(tmp_path, capsys, line, why):
    """S5. A line out of grammar is exit 1 at `path:line`, under its heading,
    naming the spelling it expected, never skipped; so is a target that does
    not resolve."""
    code, out = checked(tmp_path, {"docs/a.md": doc(rule(line))}, capsys)
    assert code == 1, out
    assert f"rules: docs/a.md:6: The heading: {why}\n" in out, out
    assert "rules: 1 refused in 1 check lines of 1 rule files." in out, out


@pytest.mark.parametrize(
    "target, why",
    [
        (".", ". is not a file in the repository"),
        ("tests/data", "tests/data is not a file in the repository"),
        ("../outside.txt", "../outside.txt is not a path inside the repository"),
    ],
    ids=["the root", "a directory", "outside"],
)
def test_a_path_that_is_no_file_of_the_repository_is_refused(
    tmp_path, capsys, target, why
):
    """The root, a directory and a path outside the root all exist, and none
    of them is a file the repository holds."""
    (tmp_path / "outside.txt").write_text("x", encoding="utf-8")
    repo = tmp_path / "repo"
    (repo / "tests" / "data").mkdir(parents=True)
    code, out = checked(repo, {"docs/a.md": doc(rule(f"check: {target}"))}, capsys)
    assert code == 1, out
    assert f": {why}\n" in out, out


def test_a_symlink_inside_the_root_that_leaves_it_is_refused(tmp_path, capsys):
    """The path is inside, and the file it opens is not."""
    from conftest import symlink_or_skip

    (tmp_path / "outside.txt").write_text("x", encoding="utf-8")
    repo = tmp_path / "repo"
    (repo / "docs").mkdir(parents=True)
    symlink_or_skip(str(tmp_path / "outside.txt"), str(repo / "docs" / "link.txt"))
    code, out = checked(repo, {"docs/a.md": doc(rule("check: docs/link.txt"))}, capsys)
    assert code == 1, out
    assert "docs/link.txt is not a path inside the repository" in out, out


def test_a_line_outside_a_rule_is_read_in_every_rule_file(tmp_path, capsys):
    """Every check line a renderer shows is read, inside a rule paragraph or
    not, in an agent definition as in a document."""
    text = doc("A sentence that states no rule.\ncheck: tests/test_gone_a.py\n")
    code, out = checked(tmp_path, {"agents/warden.md": text}, capsys)
    assert code == 1, out
    assert (
        "rules: agents/warden.md:6: The heading: tests/test_gone_a.py does not exist"
        in out
    ), out


@pytest.mark.parametrize(
    "files, verdict, said",
    [
        ({"case.yaml": "name: a\n"}, 0, "rules: all 1 check lines"),
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
    written = {"docs/a.md": doc(rule(f"check: {case}"))}
    written.update({case + name: text for name, text in files.items()})
    code, out = checked(tmp_path, written, capsys)
    assert code == verdict, out
    assert said in out, out


def test_an_eval_target_that_names_no_case_is_refused(tmp_path, capsys):
    """The directory is `<agent>/<case>/`, so an agent's directory alone names
    no case and does not resolve."""
    written = {
        "docs/a.md": doc(rule("check: evals/behaviour/warden/")),
        "evals/behaviour/warden/case.yaml": "name: a\n",
    }
    code, out = checked(tmp_path, written, capsys)
    assert code == 1, out
    assert "is no eval case: write `evals/behaviour/<agent>/<case>/`" in out, out


def test_a_check_and_a_document_together_or_neither_is_exit_2(tmp_path, capsys):
    """`--check` reads every rule file and a document names one, so asking for
    both, or for neither, is a usage error and reads nothing."""
    root = tree(tmp_path, rule("check: held-rule"))
    assert rules.main(["--check", "docs/a.md", "--root", str(root)]) == 2
    assert rules.main(["--root", str(root)]) == 2
    captured = capsys.readouterr()
    assert captured.out == "", captured.out
    assert "rules: name a document, or --check, and not both." in captured.err


def test_every_check_line_in_the_tree_holds(tmp_path, capsys):
    """The fact read on every pull request: `rules --check` over this tree is
    exit 0. On a scratch copy of what the check reads (the rule files, the
    files their targets name and the tests carrying their markers) one target
    renamed is exit 1 naming its line, and so is the old label planted in a
    file of every other rule-file glob, so a walk that read `docs/*.md` alone,
    or read a renamed target as resolving, goes red here."""
    assert rules.main(["--check", "--root", ROOT]) == 0, capsys.readouterr().out
    capsys.readouterr()
    files = rules.rule_files(ROOT)
    carriers = rules.markers(ROOT)
    named, renamed = {}, None
    for rel, text in files.items():
        held = [(n, rules.parse(line)[0]) for n, _, line in rules.check_lines(text)]
        for target in (t for _, targets in held for t in targets):
            if rules.MARKER.fullmatch(target):
                sources = [path for path, _, _ in carriers[target]]
            elif target.endswith("/"):
                sources = [target + rules.EVAL_CASE]
            else:
                sources = [target]
            for source in sources:
                destination = tmp_path / source
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(os.path.join(ROOT, *source.split("/")), destination)
        pattern = next(p for p in rules.RULE_FILES if fnmatch.fnmatchcase(rel, p))
        line = next((n for n, targets in held if targets), None)
        # One file per glob carries the planted defect, so a glob whose first
        # file names no target is planted there, not renamed in a later one.
        if renamed is None and line is not None and pattern not in named:
            lines = text.split("\n")
            first = rules.parse(lines[line - 1].strip())[0][0]
            lines[line - 1] = lines[line - 1].replace(first, f"{first}-renamed-away", 1)
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
    assert re.search(rf"^rules: {re.escape(renamed)}:\d+: .*-renamed-away", out, re.M)
    for rel in named.values():
        assert re.search(rf"^rules: {re.escape(rel)}:\d+: ", out, re.M), (rel, out)
    assert f"rules: {len(named)} refused in " in out, out
