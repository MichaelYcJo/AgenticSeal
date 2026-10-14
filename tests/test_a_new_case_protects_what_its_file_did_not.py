"""A new or changed test case protects something its file did not (#929).

`.github/scripts/case_check.py` is the regrowth check, and nothing in it is
written by hand: the mutants come from the lines each new or changed case
runs, the units it names and the lines the pull request changed, and the
verdict is which cases fail under them. The decisions are tested directly;
each real path the check takes is tested once end to end, on a fixture
repository at a base commit and at HEAD, with real mutants through the
repository's own `mutation_check.py`.
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


# --- the decisions -------------------------------------------------------------


def test_each_operator_makes_one_mutant_of_its_kind():
    found = dict(
        (label, line) for label, line in case_check().operators("    if a == b and c:")
    )
    assert found == {
        "condition negated": "    if not (a == b and c):",
        "`==` made `!=`": "    if a != b and c:",
        "`and` made `or`": "    if a == b or c:",
        "the last operand of `and` dropped": "    if a == b:",
    }
    found = dict(case_check().operators("    return x not in y, z is None"))
    assert found["`not in` made `in`"] == "    return x in y, z is None"
    found = dict(case_check().operators("    k = z is not None"))
    assert found["`is not` made `is`"] == "    k = z is None"
    assert dict(case_check().operators('    "a row",')) == {"element removed": None}
    found = dict(case_check().operators("    assert total == 3, total"))
    assert found["assertion dropped"] == "    assert True, total"
    assert found["`3` made `4`"] == "    assert total == 4, total"
    found = dict(case_check().operators("    return compute(x)"))
    assert found == {"`return` made `return None`": "    return None"}
    found = dict(case_check().operators("    done = False"))
    assert found == {
        "`False` made `True`": "    done = True",
        "statement removed": "    pass",
    }
    assert case_check().operators("    # a comment") == []
    assert case_check().operators("def f():") == []


def test_a_mutant_widens_until_it_lands_once_and_one_that_cannot_parse_is_left_out():
    module = case_check()
    source = (
        "def f():\n    x = 1\n    return x\n\n\ndef g():\n    x = 1\n    return 2\n"
    )
    labels = {
        label: (old, new) for label, old, new in module.mutants_of("m.py", source, 7)
    }
    old, new = labels["m.py:7 statement removed"]
    assert old == "def g():\n    x = 1\n" and new == "def g():\n    pass\n"
    assert source.count(old) == 1
    assert module.mutants_of("doc.md", "One.\nTwo.\n", 2) == [
        ("doc.md:2 line removed", "Two.\n", "")
    ]
    inside = module.mutants_of("m.py", "x = (\n    1\n)\n", 2)
    assert [label for label, _old, _new in inside] == ["m.py:2 `1` made `2`"]


def test_the_sole_killer_is_one_function_or_none():
    module = case_check()
    functions = {"test_a": None, "test_b": None}
    file = "tests/test_m.py"
    assert (
        module.sole_killer(
            [f"{file}::test_a[1]", f"{file}::test_a[2]"], file, functions
        )
        == "test_a"
    )
    assert (
        module.sole_killer([f"{file}::test_a", f"{file}::test_b"], file, functions)
        is None
    )
    assert module.sole_killer([f"{file}::test_c"], file, functions) is None
    assert module.sole_killer([], file, functions) is None


THREE = "def test_a():\n    pass\n\n\ndef test_b():\n    pass\n\n\ndef test_c():\n    pass\n"


def test_a_case_draws_first_the_lines_fewest_of_its_siblings_run(tmp_path):
    """The draw ranks the lines a case runs by how many of its siblings run
    them too, so a line it runs alone comes first; among as many, a changed
    line first, then one line of each unit before a second of any. A line
    only a sibling ran is never drawn: under its mutant only that sibling
    runs. A changed line no case ran comes last, and runs the whole file."""
    module = case_check()
    lines = "".join(f"V{n} = {n}\n" for n in range(1, 6))
    lines += "\ndef f():\n    a = 6\n    b = 7\n\ndef g():\n    c = 8\n"
    (tmp_path / "m.py").write_text(lines, encoding="utf-8")
    file = "tests/test_m.py"
    m = [("m.py", n) for n in range(13)]
    hits = {
        f"{file}::test_a": {m[1], m[2], m[3], m[8], m[9], m[12]},
        f"{file}::test_b": {m[1], m[2], m[3], m[4]},
        f"{file}::test_c": {m[1]},
    }
    found = module.drawn(
        str(tmp_path),
        file,
        "test_a",
        module.test_functions(THREE),
        hits,
        {},
        {"m.py": [3, 4, 5]},
        cap=None,
    )
    order = list(dict.fromkeys(label.split(" ")[0] for label, *_ in found))
    assert order == [f"m.py:{n}" for n in (8, 12, 9, 3, 2, 1, 5)]


def test_a_case_draws_no_more_mutants_than_the_cap(tmp_path):
    """A case that protects something its file did not finds it near the
    front of a ranked draw; one that finds nothing by the cap is named, not
    run to the bound. PR #939's first run drew 400 and more for each case."""
    module = case_check()
    # Two mutants on the first line and three on each after it, so the draw
    # passes the cap inside a line and has to be cut there.
    lines = "V1 = 1\n" + "".join(f"V{n} = {n} < x\n" for n in range(2, 40))
    (tmp_path / "m.py").write_text(lines, encoding="utf-8")
    file = "tests/test_m.py"
    hits = {f"{file}::test_a": {("m.py", n) for n in range(1, 40)}}
    found = module.drawn(
        str(tmp_path), file, "test_a", module.test_functions(THREE), hits, {}, {}
    )
    assert len(found) == module.DRAW_CAP == 12


def test_a_run_of_some_cases_keeps_the_workers_where_their_calls_pay_for_them():
    """A run of some of a file's cases turns xdist's workers off unless the
    traced run timed their calls at `WORKERS_PAY_S` or more together: a
    case's mutant ran its own ids alone, and S2's 35 rows must not run one by
    one when a sibling's mutant runs them all."""
    module = case_check()
    runner, file = ["py", "-m", "pytest", "-n", "4"], "tests/test_m.py"
    slow = {"t::a": 3.0, "t::b": 1.5, "t::c": 0.1}
    assert module.narrowed(runner, ["t::a", "t::b"], file, slow) == [
        *runner,
        "t::a",
        "t::b",
    ]
    assert module.narrowed(runner, ["t::a", "t::c"], file, slow) == [
        *runner,
        "t::a",
        "t::c",
        "-n",
        "0",
    ]
    assert module.narrowed(runner, [file], file, {}) == [*runner, file]


def test_a_function_named_in_a_case_is_followed_through_its_helpers():
    module = case_check()
    source = (
        "LIMIT = 3\n\n\ndef helper():\n    return LIMIT\n\n\n"
        "def unused():\n    return 0\n\n\ndef test_x():\n    assert helper() == 3\n"
    )
    functions = module.test_functions(source)
    assert module.named_units(source, functions) == {"test_x": [1, 4, 5]}


def test_a_line_end_python_does_not_read_moves_no_function():
    """A function's text is cut where Python ends a line, which is what `ast`
    numbers lines by; a U+2028 inside a string is no line end there."""
    source = 'def test_a():\n    s = "x' + chr(0x2028) + 'y"\n    assert s\n'
    (_node, text) = case_check().test_functions(source)["test_a"]
    assert text.endswith("    assert s")


def test_a_run_that_prints_nothing_is_named_by_its_exit(tmp_path, monkeypatch):
    """A `mutation-check` run that ends with no output, as a process killed by
    a signal does, still gives the finding something to say: its exit."""
    silent = tmp_path / "silent.py"
    silent.write_text("import sys\nsys.exit(3)\n", encoding="utf-8")
    module = case_check()
    monkeypatch.setattr(module, "MUTATION_CHECK", str(silent))
    code, verdict, _ = module.mutation_run(str(tmp_path), "m.py", "a", "b", ["true"], 5)
    assert code == 3
    assert verdict == "exit 3, and mutation-check printed nothing"


def test_a_windows_command_line_keeps_the_backslashes_of_its_paths():
    """The `--tests` and `--runner` command lines are split by the platform's
    rule for a backslash. On Windows it is the path separator and stays, so
    an interpreter's path reaches the process whole; PR #939's
    `windows-latest` leg started `C:hostedtoolcache…python.exe` and found
    nothing. On POSIX it escapes, as `shlex.split` reads it."""
    name = "specseal_arm_check_for_case_tests"
    spec = importlib.util.spec_from_file_location(
        name, os.path.join(ROOT, "skills", "verify", "scripts", "arm_check.py")
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    line = r'C:\py\python.exe -c "raise SystemExit(1)" a\ b #c'
    assert module.command_words(line, windows=True) == [
        r"C:\py\python.exe",
        "-c",
        "raise SystemExit(1)",
        "a\\",
        "b",
        "#c",
    ]
    assert module.command_words(line, windows=False) == [
        "C:pypython.exe",
        "-c",
        "raise SystemExit(1)",
        "a b",
        "#c",
    ]
    assert module.command_words(line) == module.command_words(
        line, windows=os.name == "nt"
    )


def test_a_caller_that_ran_the_baseline_skips_it_in_mutation_check(tmp_path):
    """`mutation-check --baseline-passed` writes the mutant without running
    the cases against the file as it is first; without it the same failing
    command is `no baseline`."""
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


# --- each path end to end ------------------------------------------------------

MODULE = 'def double(x):\n    return x * 2\n\n\ndef name():\n    return "a"\n'
DOUBLE = "\ndef test_double():\n    assert m.double(2) == 4\n"
NAME = '\ndef test_name():\n    assert m.name() == "a"\n'


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


def test_a_new_case_that_alone_kills_a_mutant_of_changed_code_is_proved(
    tmp_path, capsys, monkeypatch
):
    """S4: a pull request changes a line and adds the case that guards it; the
    case is its file's only killer of a mutant of that line. The summary says
    which, on stdout and in the step summary, naming no path outside the root."""
    root = tree(
        tmp_path,
        {"tests/test_m.py": module_text(NAME)},
        {
            "m.py": MODULE.replace("x * 2", "x + x"),
            "tests/test_m.py": module_text(NAME, DOUBLE),
        },
    )
    summary = tmp_path / "summary.md"
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(summary))
    code, out = run(root, capsys)
    assert code == 0, out
    line = (
        "tests/test_m.py::test_double: proved — the only killer in its file of m.py:2"
    )
    assert line in out, out
    assert line in summary.read_text(encoding="utf-8")
    assert str(tmp_path) not in out, out


def test_a_new_case_its_file_already_covers_is_named(tmp_path, capsys):
    """S3: a case that runs only what a sibling runs and asserts what it
    asserts kills nothing its file does not, and is named."""
    twin = DOUBLE.replace("test_double", "test_double_too")
    root = tree(
        tmp_path,
        {"tests/test_m.py": module_text(DOUBLE)},
        {"tests/test_m.py": module_text(DOUBLE, twin)},
    )
    code, out = run(root, capsys)
    assert code == 1, out
    assert (
        "tests/test_m.py::test_double_too: kills nothing its file does not: of "
        "the 2 mutants drawn for it, the lines fewest of its siblings run first "
        "and at most 12, each it killed was killed by another case too, or none "
        "was\n"
    ) in out, out


def test_a_mutant_of_changed_code_nothing_kills_is_reported_and_fails_nothing(
    tmp_path, capsys
):
    """What nothing kills is a report: a changed line no case runs is listed
    as a survivor, and the pull request's proved case still passes."""
    root = tree(
        tmp_path,
        {"tests/test_m.py": module_text(NAME)},
        {
            "m.py": MODULE.replace("x * 2", "x + x")
            + "\n\ndef unused():\n    return 7\n",
            "tests/test_m.py": module_text(NAME, DOUBLE),
        },
    )
    code, out = run(root, capsys)
    assert code == 0, out
    assert "  survived m.py:10 `return` made `return None`" in out, out


def test_a_tests_only_change_draws_its_mutants_from_the_lines_it_runs(tmp_path, capsys):
    """A pull request that changes no shipped line and adds a case: the case's
    mutants come from what it runs and its siblings do not."""
    root = tree(
        tmp_path,
        {"tests/test_m.py": module_text(DOUBLE)},
        {"tests/test_m.py": module_text(DOUBLE, NAME)},
    )
    code, out = run(root, capsys)
    assert code == 0, out
    assert (
        "tests/test_m.py::test_name: proved — the only killer in its file of m.py:6"
        in out
    ), out


def test_a_prose_pin_is_proved_by_its_sentence_removed(tmp_path, capsys):
    """S5: a pull request adds a sentence and the case that pins it; the
    sentence removed is the mutant only that case kills."""
    pin = (
        '\ndef test_doc():\n    with open("doc.md", encoding="utf-8") as f:\n'
        '        assert "A second sentence." in f.read()\n'
    )
    root = tree(
        tmp_path,
        {"tests/test_m.py": module_text(DOUBLE), "doc.md": "One sentence.\n"},
        {
            "doc.md": "One sentence.\nA second sentence.\n",
            "tests/test_m.py": module_text(DOUBLE, pin),
        },
    )
    code, out = run(root, capsys)
    assert code == 0, out
    assert (
        "tests/test_m.py::test_doc: proved — the only killer in its file of doc.md:2 line removed"
        in out
    ), out


def test_a_changed_function_is_read_as_new(tmp_path, capsys):
    """S2: a function whose body changed is read, though its name is at the
    base, so it is proved again rather than passed over."""
    root = tree(
        tmp_path,
        {"tests/test_m.py": module_text(DOUBLE)},
        {
            "tests/test_m.py": module_text(
                DOUBLE.replace("double(2) == 4", "double(3) == 6")
            )
        },
    )
    code, out = run(root, capsys)
    assert code == 0, out
    assert "tests/test_m.py::test_double: proved" in out, out


def test_a_removed_case_is_listed(tmp_path, capsys):
    """A removal is reported, never gated: the work item's mutation table is
    its proof."""
    root = tree(
        tmp_path,
        {"tests/test_m.py": module_text(DOUBLE, NAME)},
        {"tests/test_m.py": module_text(DOUBLE)},
    )
    code, out = run(root, capsys)
    assert code == 0, out
    assert "  removed tests/test_m.py::test_name" in out, out


def test_a_file_whose_proof_would_pass_the_bound_is_named_to_restructure(
    tmp_path, capsys
):
    """The owner's bound (#929): the proof ends within `--bound` minutes and
    never on a timeout. A file whose traced run alone passes what is left is
    named before any mutant runs."""
    root = tree(
        tmp_path,
        {"tests/test_m.py": module_text()},
        {"tests/test_m.py": module_text(DOUBLE)},
    )
    code, out = run(root, capsys, "--bound", "0.0001")
    assert code == 1, out
    assert "tests/test_m.py: restructure: test the decision directly" in out, out
    assert "proved" not in out.split("\n", 1)[1], out
