"""A new or changed test case names the mutant it kills, and CI runs it (#929).

`.github/scripts/case_check.py` is the regrowth check: each test function new
or changed against the merge base carries one `Kills: <path> "<OLD>" "<NEW>"`
line, and its file runs once under that mutant, which must be red with the
function's own ids the only killers. Each case here builds a fixture repository with a module,
a test file and, where the case needs one, `tests/unguarded-files.txt`, at a
base commit and at HEAD, and reads what the check says. The mutations run for
real, through the repository's own `mutation_check.py`.
"""

import importlib.util
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, ".github", "scripts", "case_check.py")


def case_check():
    spec = importlib.util.spec_from_file_location("case_check_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


MODULE = 'def double(x):\n    return x * 2\n\n\ndef name():\n    return "a"\n'

DOUBLE = '''
def test_double():
    """Doubling.

    Kills: m.py "return x * 2" "return x * 3"
    """
    assert m.double(2) == 4
'''

BARE_DOUBLE = """
def test_double():
    assert m.double(2) == 4
"""


def module_text(*functions):
    return "import m\n" + "\n".join(functions)


def git(root, *args):
    subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "-c",
            "user.email=x@example.com",
            "-c",
            "user.name=x",
            *args,
        ],
        check=True,
        capture_output=True,
    )


def tree(tmp_path, base, head):
    """A repository whose branch `base` holds `base` and whose HEAD holds
    `base` overlaid with `head`; a None in `head` removes the file."""
    root = tmp_path / "r"
    root.mkdir()
    git(root, "init", "-q", "-b", "main")
    for path, text in {"conftest.py": "", "m.py": MODULE, **base}.items():
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
    git(root, "add", "-A")
    git(root, "commit", "-qm", "base")
    git(root, "branch", "base")
    for path, text in head.items():
        target = root / path
        if text is None:
            target.unlink()
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
    git(root, "add", "-A")
    git(root, "commit", "-qm", "head")
    return root


def run(root, capsys, *extra):
    code = case_check().main(
        [
            "--baseline",
            "base",
            "--root",
            str(root),
            "--runner",
            f"{sys.executable} -m pytest -p no:xdist",
            *extra,
        ]
    )
    return code, capsys.readouterr().out


def test_a_new_function_without_a_kills_line_is_named(tmp_path, capsys):
    """S2: a function new at HEAD with no line is exit 1 and named, though
    its file is on the list that exempts the file's existing functions.

    Kills: .github/scripts/case_check.py "        return NO_LINE, None" "        return BAD_LINE.format(why=\"absent\"), None"
    """
    bare_name = "\ndef test_name():\n    assert m.name() == 'a'\n"
    root = tree(
        tmp_path,
        {
            "tests/test_m.py": module_text(BARE_DOUBLE),
            "tests/unguarded-files.txt": "tests/test_m.py\n",
        },
        {"tests/test_m.py": module_text(BARE_DOUBLE, bare_name)},
    )
    code, out = run(root, capsys)
    assert code == 1, out
    assert "tests/test_m.py::test_name: no `Kills:` line" in out, out
    assert "test_double" not in out, out


def test_a_line_whose_replacement_does_not_land_is_named(tmp_path, capsys):
    """S2: a line whose OLD occurs nowhere in its path is named with
    mutation-check's refusal, and is not read as proved.

    Kills: .github/scripts/case_check.py "        return NOTHING.format(verdict=verdict), None" "        return None, PROVED"
    """
    stale = (
        '\ndef test_name():\n    """Kills: m.py "return \\"z\\"" "return \\"y\\""\n'
        '    """\n    assert m.name() == "a"\n'
    )
    root = tree(
        tmp_path,
        {"tests/test_m.py": module_text(DOUBLE)},
        {"tests/test_m.py": module_text(DOUBLE, stale)},
    )
    code, out = run(root, capsys)
    assert code == 1, out
    assert (
        "tests/test_m.py::test_name: the run under its mutant measured nothing: refused"
    ) in out, out


def test_a_mutation_the_file_kills_without_the_function_is_named_with_its_killer(
    tmp_path, capsys
):
    """S3: a function whose mutant another function of its file kills too
    is named, with that function. One run under the mutant, read for its
    killers, is the whole proof.

    Kills: .github/scripts/case_check.py "    if rest:" "    if rest and False:"
    """
    twin = DOUBLE.replace("test_double", "test_double_too")
    root = tree(
        tmp_path,
        {"tests/test_m.py": module_text(DOUBLE)},
        {"tests/test_m.py": module_text(DOUBLE, twin)},
    )
    code, out = run(root, capsys)
    assert code == 1, out
    assert (
        "tests/test_m.py::test_double_too: its file kills its mutant without it "
        "too: tests/test_m.py::test_double"
    ) in out, out


def test_a_mutant_only_another_function_kills_is_named(tmp_path, capsys):
    """S3: a function whose mutant its file kills, but not through it, is
    named with the function that does.

    Kills: .github/scripts/case_check.py "    if not own:" "    if not own and False:"
    """
    elsewhere = (
        '\ndef test_name():\n    """Kills: m.py "return x * 2" "return x * 4"\n'
        '    """\n    assert m.name() == "a"\n'
    )
    root = tree(
        tmp_path,
        {"tests/test_m.py": module_text(DOUBLE)},
        {"tests/test_m.py": module_text(DOUBLE, elsewhere)},
    )
    code, out = run(root, capsys)
    assert code == 1, out
    assert (
        "tests/test_m.py::test_name: red, but not by this function: "
        "tests/test_m.py::test_double"
    ) in out, out


def test_a_proven_function_passes_and_the_summary_lists_both_runs(
    tmp_path, capsys, monkeypatch
):
    """S4: red under its mutant with its own ids the only killers is exit 0,
    and the step summary says so. The line's quotes round-trip through JSON.

    Kills: .github/scripts/case_check.py "PROVED = \"proved — red under its mutant, and the killers are this function's alone\"" "PROVED = \"proved\""
    """
    named = (
        '\ndef test_name():\n    """Kills: m.py "return \\"a\\"" "return \\"b\\""\n'
        '    """\n    assert m.name() == "a"\n'
    )
    root = tree(
        tmp_path,
        {"tests/test_m.py": module_text(DOUBLE)},
        {"tests/test_m.py": module_text(DOUBLE, named)},
    )
    summary = tmp_path / "summary.md"
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(summary))
    code, out = run(root, capsys)
    line = (
        "tests/test_m.py::test_name: proved — red under its mutant, and the "
        "killers are this function's alone"
    )
    assert code == 0, out
    assert line in out, out
    assert line in summary.read_text(encoding="utf-8")
    assert str(tmp_path) not in out, out


def test_a_changed_function_is_read_as_new(tmp_path, capsys):
    """S2: a function whose body changed is read even though its name is at
    the base, so a line the change left stale is named: the body asserts
    what the line's mutant leaves true.

    Kills: .github/scripts/case_check.py "            if name not in base or base[name][1] != text:" "            if name not in base:"
    """
    changed = DOUBLE.replace("double(2) == 4", "double(0) == 0")
    root = tree(
        tmp_path,
        {"tests/test_m.py": module_text(DOUBLE)},
        {"tests/test_m.py": module_text(changed)},
    )
    code, out = run(root, capsys)
    assert code == 1, out
    assert "tests/test_m.py::test_double: SURVIVED — nothing in its file" in out, out


def test_a_prose_pin_runs_through_the_document(tmp_path, capsys):
    """S5: a case pinning a sentence names the document as its path and the
    sentence as OLD, and is proved through it.

    Kills: .github/scripts/case_check.py "    if not os.path.isfile(os.path.join(root, path)):" "    if not os.path.isfile(os.path.join(root, path)) or path.endswith(\".md\"):"
    """
    pin = (
        '\ndef test_doc():\n    """Kills: doc.md "Every case names its mutant." '
        '"Every case names nothing."\n    """\n'
        '    with open("doc.md", encoding="utf-8") as f:\n'
        '        assert "Every case names its mutant." in f.read()\n'
    )
    root = tree(
        tmp_path,
        {
            "tests/test_m.py": module_text(DOUBLE),
            "doc.md": "Every case names its mutant.\n",
        },
        {"tests/test_m.py": module_text(DOUBLE, pin)},
    )
    code, out = run(root, capsys)
    assert code == 0, out
    assert "tests/test_m.py::test_doc: proved" in out, out


def test_a_file_leaves_the_list_only_when_every_function_carries_the_line(
    tmp_path, capsys
):
    """S6: a file taken off the list with a function that carries no line is
    named at that function, and a file added to the list is named too.

    Kills: .github/scripts/case_check.py "                    findings.append((fid, OFF_THE_LIST))" "                    pass"
    """
    root = tree(
        tmp_path,
        {
            "tests/test_m.py": module_text(DOUBLE),
            "tests/test_n.py": module_text(BARE_DOUBLE),
            "tests/unguarded-files.txt": "tests/test_m.py\ntests/test_n.py\n",
        },
        {
            "tests/test_p.py": module_text(DOUBLE),
            "tests/unguarded-files.txt": "tests/test_m.py\ntests/test_p.py\n",
        },
    )
    code, out = run(root, capsys)
    assert code == 1, out
    assert "tests/test_n.py::test_double: its file is off" in out, out
    assert (
        "`tests/test_p.py` is on tests/unguarded-files.txt and not on the base's copy"
        in out
    ), out


def test_a_run_that_prints_nothing_is_named_by_its_exit(tmp_path, monkeypatch):
    """A `mutation-check` run that ends with no output, as a process killed
    by a signal does, still gives the finding something to say: its exit.
    Seen in this work item's phase 2, where two runs another process killed
    came back empty.

    Kills: .github/scripts/case_check.py "f\"exit {done.returncode}, and mutation-check printed nothing\"" "\"\""
    """
    silent = tmp_path / "silent.py"
    silent.write_text("import sys\nsys.exit(3)\n", encoding="utf-8")
    module = case_check()
    monkeypatch.setattr(module, "MUTATION_CHECK", str(silent))
    code, verdict, _ = module.mutation_run(str(tmp_path), "m.py", "a", "b", ["true"], 5)
    assert code == 3
    assert verdict == "exit 3, and mutation-check printed nothing"


def test_a_file_whose_proof_would_pass_the_bound_is_named_to_restructure(
    tmp_path, capsys
):
    """The owner's bound (#929): the proof ends within `--bound` minutes and
    never on a timeout. A file whose one run, times the functions it owes,
    would pass what is left is named before any mutant runs.

    Kills: .github/scripts/case_check.py "        if code is None or each + need > left:" "        if code is None:"
    """
    root = tree(
        tmp_path,
        {"tests/test_m.py": module_text()},
        {"tests/test_m.py": module_text(DOUBLE)},
    )
    code, out = run(root, capsys, "--bound", "0.0001")
    assert code == 1, out
    assert "tests/test_m.py: restructure: test the decision directly" in out, out
    assert "proved" not in out.split("\n", 1)[1], out


def test_a_caller_that_ran_the_baseline_skips_it_in_mutation_check(tmp_path):
    """`mutation-check --baseline-passed` writes the mutant without running
    the cases against the file as it is first, which is how the regrowth
    check runs one mutant per function after one run of the file. Without
    the option, the same failing command is `no baseline`.

    Kills: skills/verify/scripts/mutation_check.py "        if baseline:\n            before, detail, output = run_cases(" "        if True:\n            before, detail, output = run_cases("
    """
    target = tmp_path / "x.py"
    target.write_text("A = 1\n", encoding="utf-8")
    script = os.path.join(ROOT, "skills", "verify", "scripts", "mutation_check.py")
    command = f'{sys.executable} -c "raise SystemExit(1)"'

    def check(*extra):
        return subprocess.run(
            [
                *(sys.executable, script, str(target), "--replace", "A = 1", "A = 2"),
                *("--tests", command, "--cwd", str(tmp_path), *extra),
            ],
            capture_output=True,
            encoding="utf-8",
        )

    passed = check("--baseline-passed")
    assert passed.returncode == 0, passed.stdout
    assert passed.stdout.startswith("red"), passed.stdout
    assert check().stdout.startswith("no baseline")
    assert target.read_text(encoding="utf-8") == "A = 1\n"


def test_a_line_end_python_does_not_read_moves_no_function(tmp_path, capsys):
    """A function's text is cut where Python ends a line, which is what `ast`
    numbers lines by. A U+2028 inside a string is no line end there, so a
    change on the function's last line is still read as a change.

    Kills: .github/scripts/case_check.py "    lines = PYTHON_LINE_END.split(source)" "    lines = source.splitlines()"
    """
    body = (
        '\ndef test_a():\n    """Kills: m.py "return x * 2" "return x * 3"\n'
        '    """\n    s = "x' + chr(0x2028) + 'y"\n    assert m.double(2) == 4\n'
    )
    root = tree(
        tmp_path,
        {"tests/test_m.py": module_text(body)},
        {
            "tests/test_m.py": module_text(
                body.replace("double(2) == 4", "double(0) == 0")
            )
        },
    )
    code, out = run(root, capsys)
    assert code == 1, out
    assert "tests/test_m.py::test_a: SURVIVED" in out, out
