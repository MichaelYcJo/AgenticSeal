"""`.github/scripts/rules.py`, one class per function.

`seal rules <doc>` prints each section with what its tests say they guard, and
`seal rules --check` fails where a check line is refused. A rule's text lives
once, as the first sentence of the docstring of the test that holds it, and
a rule file lists its tests by `check:` line, in the grammar
`skills/settle/SKILL.md` *A rule has one shape* states. `seal rules <doc>` never
fails for what it finds; `seal rules --check` reads every rule file and is exit 1
where a line is out of grammar or a target is gone, and one case here runs
it over the tree, so the suite is where the fact is read.

#942's phase 6 placed these cases from
`tests/behaviour/test_the_rules_command_reads_each_rule_off_its_test.py`, which keeps
the cases that read the record layout document, the marker's registration
and the settle skill.
"""

import fnmatch
import glob
import importlib.util
import os
import re
import shutil
import subprocess
import sys

import pytest
from conftest import ROOT, census_case

TARGET = ".github/scripts/rules.py"

SCRIPT = os.path.join(ROOT, ".github", "scripts", "rules.py")


def _load():
    spec = importlib.util.spec_from_file_location("agentic_rules", SCRIPT)
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


HELD = "tests/test_x.py"


def rule(line):
    """One rule paragraph closed by LINE."""
    return f"**A rule.** Its one why.\n{line}\n"


def doc(*paragraphs):
    """A rule file whose paragraphs stand under `## The heading`, from line 5."""
    return "# D\n\n## The heading\n\n" + "\n".join(paragraphs)


def checked(tmp_path, files, capsys):
    """`(exit, stdout)` of `seal rules --check` over a tree holding the test module
    and `files`, each `{path: text}`."""
    for rel, text in {HELD: TESTS, **files}.items():
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, "utf-8", newline="\n")
    code = rules.main(["--check", "--root", str(tmp_path)])
    return code, capsys.readouterr().out


EXPECTED = "write `check: <targets>` or `check: none reader: <who reads it>`"


class Test_main:
    @pytest.mark.parametrize(
        "target, said",
        [
            ("tests/test_x.py", "tests/test_x.py: The module guards a whole thing."),
            (
                "held-rule",
                "held-rule: tests/test_x.py test_held: A held rule is guarded.",
            ),
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
        self, tmp_path, capsys, target, said
    ):
        """S1, S3. Each target prints under its section with the first sentence of
        the docstring it names: a file's module docstring, or each test carrying a
        marker; `(no docstring)`, or why it does not resolve. The command exits 0
        whatever it found."""
        root = tree(
            tmp_path, f"# A\n\n## The section\n\n**A rule.**\ncheck: {target}\n"
        )
        code, out, _ = run(root, capsys)
        assert code == 0
        assert out.startswith("# A\n  (no check line)\n\n## The section\n"), out
        assert f"\n    {said}\n" in out, out

    @pytest.mark.parametrize(
        "target, said",
        [
            ("gated-rule", "tests/test_g.py test_gated: A gated case is read."),
            (
                "tried-rule",
                "tests/test_g.py TestGroup.test_tried: A tried method is read.",
            ),
        ],
        ids=["under an if, decorated twice", "a method under a try"],
    )
    def test_a_marker_on_a_test_inside_a_block_is_read(
        self, tmp_path, capsys, target, said
    ):
        """A test pytest collects inside an `if` or a `try` carries its marker as
        any other does, and is described from its own docstring, at exit 0."""
        root = tree(tmp_path, f"## A\n\n**R.** Why.\ncheck: {target}\n")
        (root / "tests" / "test_g.py").write_text(GATED, "utf-8", newline="\n")
        code, out, _ = run(root, capsys)
        assert code == 0
        assert f"\n    {target}: {said}\n" in out, out

    @pytest.mark.parametrize("where", ["top", "subdirectory"])
    def test_with_no_root_the_targets_resolve_where_the_command_runs(
        self, tmp_path, capsys, monkeypatch, where
    ):
        """`seal rules <doc>` with no `--root` resolves in the repository it is typed
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
        assert (
            "    held-rule: tests/test_x.py test_held: A held rule is guarded.\n" in out
        )

    def test_a_refused_line_is_printed_with_why(self, tmp_path, capsys):
        """`seal rules <doc>` prints a line out of grammar under its section with the
        reason `--check` refuses it, and still exits 0."""
        root = tree(tmp_path, "## One\n\ncheck: tests/test_x.py, tests/test_x.py\n")
        code, out, _ = run(root, capsys)
        assert code == 0
        assert (
            "  check, line 3:\n    refused: `,` is no part of a check line: write "
            "`check: <targets>` or `check: none reader: <who reads it>`\n"
        ) in out, out

    def test_a_line_not_read_is_printed_as_one_and_holds_nothing(
        self, tmp_path, capsys
    ):
        """#1167, *Scope* item 8: `seal rules <doc>` prints a line that opens
        like a check line and is not one as not read, with the reason
        `--check` names it, and the section it stands in holds no check line.
        Seen red against the line printed as refused."""
        root = tree(tmp_path, "## One\n\nEnforced by: tests/test_x.py\n")
        code, out, _ = run(root, capsys)
        assert code == 0
        assert out == (
            "## One\n"
            "  not read, line 3: `Enforced by: tests/test_x.py` opens like a check "
            "line and is not one, so it was not read: write `check: <targets>` or "
            "`check: none reader: <who reads it>`\n"
            "  (no check line)\n"
        ), out

    def test_a_test_under_a_dot_directory_is_not_read_for_markers(
        self, tmp_path, capsys
    ):
        """A virtual environment or a tool's cache holds `test_*.py` files that
        are no test of the repository, and one may not parse here: the walk skips
        every directory whose name starts with a dot."""
        hidden = tmp_path / ".venv" / "lib"
        hidden.mkdir(parents=True)
        (hidden / "test_vendored.py").write_text(
            'import pytest\n\n@pytest.mark.rule("hidden-rule")\ndef test_x(:\n',
            "utf-8",
        )
        code, out = checked(
            tmp_path, {"docs/a.md": doc(rule("check: held-rule"))}, capsys
        )
        assert code == 0, out
        code, out = checked(
            tmp_path, {"docs/a.md": doc(rule("check: hidden-rule"))}, capsys
        )
        assert code == 1, out
        assert "no test carries the marker `hidden-rule`" in out, out

    def test_an_eval_case_and_a_no_target_line_are_printed_as_what_they_are(
        self, tmp_path, capsys
    ):
        """S4's reading half. An eval case directory resolves and is named as one;
        `check: none reader: <who>` names no target and prints its reader."""
        root = tree(
            tmp_path,
            "## One\n\ncheck: evals/behaviour/proofer/a/\n\n"
            "## Two\n\ncheck: none reader: the proofer at review\n",
        )
        case = root / "evals" / "behaviour" / "proofer" / "a"
        case.mkdir(parents=True)
        (case / "case.yaml").write_text("name: a\n", "utf-8")
        code, out, _ = run(root, capsys)
        assert code == 0
        assert "    evals/behaviour/proofer/a/: an eval case\n" in out, out
        assert "    no target, read by the proofer at review\n" in out, out

    def test_a_fenced_or_commented_line_is_an_example_and_writes_nothing(
        self, tmp_path, capsys
    ):
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
        assert "not read" not in capsys.readouterr().out
        after = sorted(
            (p, os.path.getsize(os.path.join(d, p)))
            for d, _, files in os.walk(root)
            for p in files
        )
        assert code == 0
        assert out == "## One\n  (no check line)\n", out
        assert before == after

    def test_a_document_that_cannot_be_read_is_exit_2(self, tmp_path, capsys):
        """Nothing was read, so nothing is printed as if it had been."""
        code = rules.main([str(tmp_path / "missing.md"), "--root", str(tmp_path)])
        captured = capsys.readouterr()
        assert code == 2
        assert "seal rules: cannot read" in captured.err
        assert captured.out == ""

    @pytest.mark.parametrize(
        "line, said",
        [
            (f"check: {HELD}", "seal rules: all 1 check lines in 1 rule files hold."),
            (
                f"check: {HELD} held-rule",
                "seal rules: all 1 check lines in 1 rule files hold.",
            ),
            (
                "check: none reader: the proofer at review",
                "seal rules: all 1 check lines in 1 rule files hold.",
            ),
            (f"  check: {HELD}", "seal rules: all 1 check lines in 1 rule files hold."),
        ],
        ids=["a file", "S2 two targets", "S4 no target", "indented under a list item"],
    )
    def test_accepts_a_check_line_in_grammar(self, tmp_path, capsys, line, said):
        """S1, S2, S4. A line of resolving targets, one space apart, or the
        no-target form with its reader, is exit 0, and is read, not named."""
        code, out = checked(tmp_path, {"docs/a.md": doc(rule(line))}, capsys)
        assert code == 0, out
        assert out == f"{said}\n", out

    @pytest.mark.parametrize(
        "line, why",
        [
            (
                f"check: {HELD}::test_held",
                f"`::` is no part of a check line: {EXPECTED}",
            ),
            (f"check: {HELD}, {HELD}", f"`,` is no part of a check line: {EXPECTED}"),
            ("check: none — a reader", f"`—` is no part of a check line: {EXPECTED}"),
            ("check: none", f"a line naming no target names its reader: {EXPECTED}"),
            (
                "check: none reader:",
                f"a line naming no target names its reader: {EXPECTED}",
            ),
            (
                "check: none reader the proofer",
                f"a line naming no target names its reader: {EXPECTED}",
            ),
            (
                "check: none reader:  the proofer",
                f"a line naming no target names its reader: {EXPECTED}",
            ),
            (f"check: {HELD}  held-rule", "targets are separated by one space"),
            ("check: gone-rule", "no test carries the marker `gone-rule`"),
            ("check: tests/test_gone.py", "tests/test_gone.py does not exist"),
            (f"check: {HELD} tests/test_gone.py", "tests/test_gone.py does not exist"),
        ],
        ids=[
            "a test named after the path",
            "a comma",
            "an em dash",
            "none alone",
            "a reader with nothing after it",
            "a reader with no colon",
            "a reader behind two spaces",
            "two spaces",
            "a marker no test carries",
            "a file gone",
            "one of two gone",
        ],
    )
    def test_refuses_every_other_spelling_at_its_line(
        self, tmp_path, capsys, line, why
    ):
        """S5. A line out of grammar is exit 1 at `path:line`, under its heading,
        naming the spelling it expected, never skipped; so is a target that does
        not resolve."""
        code, out = checked(tmp_path, {"docs/a.md": doc(rule(line))}, capsys)
        assert code == 1, out
        assert f"seal rules: docs/a.md:6: The heading: {why}\n" in out, out
        assert "seal rules: 1 refused in 1 check lines of 1 rule files." in out, out

    @pytest.mark.parametrize(
        "line",
        [
            f"Enforced by: {HELD}",
            f"Check: {HELD}",
            f"**check:** {HELD}",
            f"check : {HELD}",
            f"check:{HELD}",
            f"checks: {HELD}",
            f"- check: {HELD}",
            f"1. check: {HELD}",
            f"> check: {HELD}",
            f"## check: {HELD}",
            f"- [ ] check: {HELD}",
            f"| check: {HELD}",
        ],
        ids=[
            "the old label",
            "a capital",
            "in bold",
            "a space before the colon",
            "no space after the colon",
            "a plural",
            "a list bullet",
            "an ordered-list number",
            "a blockquote mark",
            "a heading mark",
            "a task box",
            "a table pipe",
        ],
    )
    def test_names_a_line_that_opens_like_one_and_is_not_one_at_exit_0(
        self, tmp_path, capsys, line
    ):
        """#1167, *Scope* item 8: only the one shape is read. A line that opens
        like a check line and is not one, another case, emphasis, a space
        before the colon, the plural, the old label or block markup before
        the label, is named at its line, under its heading, as not read, and
        decides nothing: the run is exit 0, and the line is no check line in
        the count. Pinned whole (contract rule 14). Seen red against the
        refusal at exit 1."""
        code, out = checked(tmp_path, {"docs/a.md": doc(rule(line))}, capsys)
        # A line that is a heading stands under itself.
        heading = line[3:] if line.startswith("## ") else "The heading"
        assert code == 0, out
        assert out == (
            f"seal rules: not read: docs/a.md:6: {heading}: `{line}` opens like "
            "a check line and is not one, so it was not read: write "
            "`check: <targets>` or `check: none reader: <who reads it>`\n"
            "seal rules: all 0 check lines in 1 rule files hold.\n"
        ), out

    @pytest.mark.parametrize(
        "line",
        [f"Checked: {HELD}", f"The check: {HELD}", f"A check line: {HELD}"],
        ids=["another word", "a word before it", "words between"],
    )
    def test_names_no_line_that_does_not_open_like_one(self, tmp_path, capsys, line):
        """A line whose label is another word, or that has words before the
        label, is prose: neither read nor named."""
        code, out = checked(tmp_path, {"docs/a.md": doc(rule(line))}, capsys)
        assert code == 0, out
        assert out == "seal rules: all 0 check lines in 1 rule files hold.\n", out

    def test_names_a_line_beside_a_refusal_and_keeps_the_refusal(
        self, tmp_path, capsys
    ):
        """The naming decides nothing either way: a refused check line in the
        same file is still exit 1, and the named line is printed too."""
        text = doc(rule(f"Check: {HELD}"), rule("check: tests/test_gone.py"))
        code, out = checked(tmp_path, {"docs/a.md": text}, capsys)
        assert code == 1, out
        assert (
            "seal rules: docs/a.md:9: The heading: tests/test_gone.py does not" in out
        )
        assert "seal rules: not read: docs/a.md:6: The heading: `Check: " in out, out
        assert "seal rules: 1 refused in 1 check lines of 1 rule files." in out, out

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
        self, tmp_path, capsys, target, why
    ):
        """The root, a directory and a path outside the root all exist, and none
        of them is a file the repository holds."""
        (tmp_path / "outside.txt").write_text("x", encoding="utf-8")
        repo = tmp_path / "repo"
        (repo / "tests" / "data").mkdir(parents=True)
        code, out = checked(repo, {"docs/a.md": doc(rule(f"check: {target}"))}, capsys)
        assert code == 1, out
        assert f": {why}\n" in out, out

    def test_a_symlink_inside_the_root_that_leaves_it_is_refused(
        self, tmp_path, capsys
    ):
        """The path is inside, and the file it opens is not."""
        from conftest import symlink_or_skip

        (tmp_path / "outside.txt").write_text("x", encoding="utf-8")
        repo = tmp_path / "repo"
        (repo / "docs").mkdir(parents=True)
        symlink_or_skip(str(tmp_path / "outside.txt"), str(repo / "docs" / "link.txt"))
        code, out = checked(
            repo, {"docs/a.md": doc(rule("check: docs/link.txt"))}, capsys
        )
        assert code == 1, out
        assert "docs/link.txt is not a path inside the repository" in out, out

    def test_a_line_outside_a_rule_is_read_in_every_rule_file(self, tmp_path, capsys):
        """Every check line a renderer shows is read, inside a rule paragraph or
        not, in an agent definition as in a document."""
        text = doc("A sentence that states no rule.\ncheck: tests/test_gone_a.py\n")
        code, out = checked(tmp_path, {"agents/proofer.md": text}, capsys)
        assert code == 1, out
        assert (
            "seal rules: agents/proofer.md:6: The heading: tests/test_gone_a.py does not exist"
            in out
        ), out

    @pytest.mark.parametrize(
        "files, verdict, said",
        [
            ({"case.yaml": "name: a\n"}, 0, "seal rules: all 1 check lines"),
            ({"prompt.md": "Review.\n"}, 1, "holds no case.yaml"),
        ],
        ids=["with its case.yaml", "without"],
    )
    def test_an_eval_case_directory_resolves_where_its_case_yaml_is(
        self, tmp_path, capsys, files, verdict, said
    ):
        """An agent's rule can be held by an eval case alone, so
        `evals/behaviour/<agent>/<case>/` is a target, resolving where the
        directory holds `case.yaml`."""
        case = "evals/behaviour/proofer/a-case/"
        written = {"docs/a.md": doc(rule(f"check: {case}"))}
        written.update({case + name: text for name, text in files.items()})
        code, out = checked(tmp_path, written, capsys)
        assert code == verdict, out
        assert said in out, out

    def test_an_eval_target_that_names_no_case_is_refused(self, tmp_path, capsys):
        """The directory is `<agent>/<case>/`, so an agent's directory alone names
        no case and does not resolve."""
        written = {
            "docs/a.md": doc(rule("check: evals/behaviour/proofer/")),
            "evals/behaviour/proofer/case.yaml": "name: a\n",
        }
        code, out = checked(tmp_path, written, capsys)
        assert code == 1, out
        assert "is no eval case: write `evals/behaviour/<agent>/<case>/`" in out, out

    def test_a_refusal_in_a_section_a_pending_remove_takes_out_is_excused_and_named(
        self, tmp_path, capsys
    ):
        """A `check:` line inside a section an unsettled design's `remove` with
        no `from` takes out at the settle is excused: printed with the work item
        that removes it, and exit 0. A `remove` of another section, and one
        with a `from` that takes out a text and leaves the section, excuse
        nothing."""
        gone = doc(rule("check: tests/test_gone.py"))
        design = "seal/threads/1-a/frame/design.md"
        removal = "# Design\n\n## Rule changes\n\n- remove\n  file: docs/a.md\n"
        written = {"docs/a.md": gone, design: removal + "  section: The heading\n"}
        code, out = checked(tmp_path, written, capsys)
        assert code == 0, out
        assert (
            "seal rules: excused: docs/a.md:6: The heading: tests/test_gone.py does "
            "not exist; seal/threads/1-a/ removes this section at the settle\n"
        ) in out, out
        assert (
            "seal rules: 1 excused in 1 check lines of 1 rule files, and every other "
            "line holds.\n"
        ) in out, out
        for kept in (
            "  section: Another heading\n",
            "  section: The heading\n  from: **A rule.**\n",
        ):
            written[design] = removal + kept
            code, out = checked(tmp_path, written, capsys)
            assert code == 1, (kept, out)
            assert "excused" not in out, (kept, out)

    def test_a_check_and_a_document_together_or_neither_is_exit_2(
        self, tmp_path, capsys
    ):
        """`--check` reads every rule file and a document names one, so asking for
        both, or for neither, is a usage error and reads nothing."""
        root = tree(tmp_path, rule("check: held-rule"))
        assert rules.main(["--check", "docs/a.md", "--root", str(root)]) == 2
        assert rules.main(["--root", str(root)]) == 2
        captured = capsys.readouterr()
        assert captured.out == "", captured.out
        assert "seal rules: name a document, or --check, and not both." in captured.err

    def test_every_check_line_in_the_tree_holds(self, tmp_path, capsys):
        """The fact read on every pull request: `seal rules --check` over this tree is
        exit 0. On a scratch copy of what the check reads (the rule files, the
        files their targets name and the tests carrying their markers) one target
        renamed is exit 1 naming its line, and so is a check line naming a gone
        file, planted in a file of every other rule-file glob, so a walk that
        read `docs/*.md` alone, or read a renamed target as resolving, goes red
        here. The pending designs
        are copied too, so a line a pending `remove` excuses stays excused, and
        no defect is planted in a file such a `remove` names."""
        assert rules.main(["--check", "--root", ROOT]) == 0, capsys.readouterr().out
        capsys.readouterr()
        files = rules.rule_files(ROOT)
        carriers = rules.markers(ROOT)
        designs = glob.glob(os.path.join(ROOT, "seal", "threads", "*", "frame", "*.md"))
        for path in designs:
            destination = tmp_path / os.path.relpath(path, ROOT)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, destination)
        policy = rules.sibling("config").policy_root(os.path.join(ROOT, "seal"))
        pending = rules.sibling("rule_changes").pending(ROOT, policy)
        removing = {o.file for o, _ in pending if o.kind == "remove"}
        named, renamed = {}, None
        for rel, text in files.items():
            held = [(n, rules.parse(line)[0]) for n, _, line in rules.check_lines(text)]
            for target in (t for _, targets in held for t in targets):
                if rules.MARKER.fullmatch(target):
                    sources = [path for path, _, _ in carriers.get(target, ())]
                elif target.endswith("/"):
                    sources = [target + rules.EVAL_CASE]
                else:
                    sources = [target]
                for source in sources:
                    origin = os.path.join(ROOT, *source.split("/"))
                    if not os.path.isfile(origin):
                        continue  # an excused line's target, gone from the tree
                    destination = tmp_path / source
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(origin, destination)
            pattern = next(p for p in rules.RULE_FILES if fnmatch.fnmatchcase(rel, p))
            line = next((n for n, targets in held if targets), None)
            # One file per glob carries the planted defect, so a glob whose first
            # file names no target is planted there, not renamed in a later one.
            # A file a pending `remove` names carries none.
            if rel in removing:
                pass
            elif renamed is None and line is not None and pattern not in named:
                lines = text.split("\n")
                first = rules.parse(lines[line - 1].strip())[0][0]
                lines[line - 1] = lines[line - 1].replace(
                    first, f"{first}-renamed-away", 1
                )
                text, renamed, named[pattern] = "\n".join(lines), rel, rel
            elif pattern not in named:
                text += "\n\ncheck: tests/test_planted_and_gone.py\n"
                named[pattern] = rel
            destination = tmp_path / rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(text, "utf-8", newline="\n")
        assert renamed is not None, "no rule file in the tree names a target"
        assert set(named) == set(rules.RULE_FILES), named
        assert rules.main(["--check", "--root", str(tmp_path)]) == 1
        out = capsys.readouterr().out
        assert re.search(
            rf"^seal rules: {re.escape(renamed)}:\d+: .*-renamed-away", out, re.M
        )
        for rel in named.values():
            assert re.search(rf"^seal rules: {re.escape(rel)}:\d+: ", out, re.M), (
                rel,
                out,
            )
        assert f"seal rules: {len(named)} refused in " in out, out


class Test_module:
    @pytest.mark.parametrize("mark", ["#", "-", "*", ">", "|", "1. ", " "])
    def test_a_long_run_of_markup_with_no_label_is_answered_at_once(self, mark):
        """A run of one mark is matched in one way, so a shown line of markup
        that holds no label is answered in time linear in its length, never in
        time exponential in it. The child process holds the timeout, so a
        pattern that backtracks fails this case and does not stall the run."""
        child = (
            "import importlib.util, sys\n"
            "spec = importlib.util.spec_from_file_location('r', sys.argv[1])\n"
            "r = importlib.util.module_from_spec(spec); spec.loader.exec_module(r)\n"
            "assert r.NEAR.match(sys.argv[2] * 64 + ' x') is None\n"
        )
        done = subprocess.run(
            [sys.executable, "-c", child, SCRIPT, mark],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
        )
        assert done.returncode == 0, done.stderr


test_census = census_case(TARGET)
