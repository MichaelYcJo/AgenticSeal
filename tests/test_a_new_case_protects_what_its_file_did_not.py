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

import pytest

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
    # A line keeps the end it has in the file, as a Windows checkout's CRLF.
    assert ("m.py:2 `2` made `3`", "y = 2\r\n", "y = 3\r\n") in module.mutants_of(
        "m.py", "x = 1\r\ny = 2\r\n", 2
    )


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


def test_what_was_not_run_counts_only_the_changed_lines_mutants():
    """A proof's kill of a mutant on an unchanged line of a changed file does
    not make a changed line's mutant count as run, so the summary's `not run
    within the bound` line neither shrinks nor goes."""
    every_diff = [
        ("m.py:6 `return` made `return None`", "m.py", "a", "b"),
        ("m.py:7 statement removed", "m.py", "c", "d"),
        ("m.py:8 statement removed", "m.py", "e", "f"),
    ]
    killed = {
        "m.py:2 `return` made `return None`": True,
        "m.py:8 statement removed": False,
    }
    assert case_check().unrun(every_diff, killed) == 2


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


def test_a_traced_run_that_times_out_hands_back_nothing_it_traced(tmp_path):
    """A traced run past its timeout returns no exit, no lines and no stopped
    ids, in the shape `check` unpacks, so the file is named to restructure
    rather than the check stopping on the tuple."""
    sleep = [sys.executable, "-c", "import time; time.sleep(30)"]
    found = case_check().traced_run(str(tmp_path), "tests/test_m.py", sleep, 0)
    assert found[0] is None and found[2] == "timed out"
    assert found[3:] == ({}, {}, set())


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


def tree(tmp_path, base, head, newline="\n"):
    """A repository whose branch `base` holds `base` and whose HEAD holds
    `base` overlaid with `head`; a None in `head` removes the file. Every file
    ends its lines with `newline` on every platform, so a row means the same
    bytes on Windows as on POSIX."""
    root = tmp_path / "r"
    root.mkdir()
    git(root, "init", "-q", "-b", "main")
    for path, text in {"conftest.py": "", "m.py": MODULE, **base}.items():
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8", newline=newline)
    git(root, "add", "-A")
    git(root, "commit", "-qm", "base")
    git(root, "branch", "base")
    for path, text in head.items():
        target = root / path
        if text is None:
            target.unlink()
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8", newline=newline)
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


CHANGED = MODULE.replace("x * 2", "x + x")
TWIN = DOUBLE.replace("test_double", "test_double_too")
PIN = (
    '\ndef test_doc():\n    with open("doc.md", encoding="utf-8") as f:\n'
    '        assert "A second sentence." in f.read()\n'
)
S4 = "tests/test_m.py::test_double: proved — the only killer in its file of m.py:2"
# Cases pytest stops before their bodies run on this runner, one of each
# spelling a fixture can hold today. The check reads no list of them: the
# tracer reads pytest's call report, and these rows show what it decides.
ELSEWHERE = (
    "\nimport unittest\n\nimport pytest\n\n\n"
    '@pytest.mark.skip(reason="another platform")\n'
    "def test_by_a_mark():\n    assert m.double(2) == 4\n\n\n"
    "def test_in_its_body():\n    if True:\n"
    '        pytest.skip("another platform")\n    assert m.double(2) == 4\n\n\n'
    "def test_by_importorskip():\n"
    '    pytest.importorskip("a_module_no_runner_has")\n'
    "    assert m.double(2) == 4\n\n\n"
    '@pytest.fixture\ndef elsewhere():\n    pytest.skip("another platform")\n\n\n'
    "def test_by_a_fixture(elsewhere):\n    assert m.double(2) == 4\n\n\n"
    "@pytest.mark.xfail(run=False)\n"
    "def test_by_an_xfail_never_started():\n    assert m.double(2) == 4\n\n\n"
    "class TestUnittest(unittest.TestCase):\n"
    "    def test_by_skiptest(self):\n"
    '        self.skipTest("another platform")\n'
    "        assert m.double(2) == 4\n\n\n"
    "def test_by_xfail():\n"
    '    pytest.xfail("another platform")\n    assert m.double(2) == 4\n'
)
NEVER_STARTED = [
    "test_by_a_mark",
    "test_in_its_body",
    "test_by_importorskip",
    "test_by_a_fixture",
    "test_by_an_xfail_never_started",
    "TestUnittest::test_by_skiptest",
    "test_by_xfail",
]
NEVER_RAN = (
    "not proved: none of its ids ran its call to the end on this runner "
    "(skipped, deselected or not collected), so no mutant was run against it"
)
# A file skipped at import, whose run collects no case at all.
AT_IMPORT = '\nimport pytest\n\npytest.importorskip("a_module_no_runner_has")\n'
# An expected failure runs its body, and a mutant that raises other than the
# exception its mark names fails it.
EXPECTED = (
    "\nimport pytest\n\n\n@pytest.mark.xfail(raises=AssertionError)\n"
    "def test_double_xfail():\n    assert m.double(2) + 1 == 4\n"
)
# A unittest expected failure whose body raised: pytest's unittest plugin
# raises its own xfail stop on the body's behalf, and the case still ran. No
# mutant makes it pass, so it kills nothing, and it is never named as one
# that did not run.
UNITTEST_EXPECTED = (
    "\nimport unittest\n\n\nclass TestExpected(unittest.TestCase):\n"
    "    @unittest.expectedFailure\n"
    "    def test_by_expected_failure(self):\n"
    "        assert m.double(2) == 5\n"
)
# A sibling that asserts on the unit and then skips the rest on this runner:
# under the mutant it fails at its assertion, so it kills what it asserted.
PARTIAL = (
    "\nimport pytest\n\n\ndef test_partial():\n    assert m.double(2) == 4\n"
    '    pytest.skip("the rest runs on another platform")\n'
)


@pytest.mark.parametrize(
    "base, head, options, code, expected",
    [
        pytest.param(
            {"tests/test_m.py": module_text(NAME)},
            {"m.py": CHANGED, "tests/test_m.py": module_text(NAME, DOUBLE)},
            {},
            0,
            [S4],
            id="S4 a new case alone kills a mutant of changed code",
        ),
        pytest.param(
            {"tests/test_m.py": module_text(NAME)},
            {"m.py": CHANGED, "tests/test_m.py": module_text(NAME, DOUBLE)},
            {"newline": "\r\n"},
            0,
            [S4],
            id="a checkout with CRLF line ends is mutated as its bytes stand",
        ),
        pytest.param(
            {"tests/test_m.py": module_text(DOUBLE)},
            {"tests/test_m.py": module_text(DOUBLE, TWIN)},
            {},
            1,
            [
                "tests/test_m.py::test_double_too: kills nothing its file does "
                "not: of the 2 mutants drawn for it, the lines fewest of its "
                "siblings run first and at most 12, each it killed was killed by "
                "another case too, or none was\n"
            ],
            id="S3 a case its file already covers is named",
        ),
        pytest.param(
            {"tests/test_m.py": module_text(NAME)},
            {"m.py": CHANGED, "tests/test_m.py": module_text(NAME, ELSEWHERE)},
            {},
            1,
            [f"tests/test_m.py::{name}: {NEVER_RAN}\n" for name in NEVER_STARTED],
            id="every way a case skips here names it as one that never ran",
        ),
        pytest.param(
            {"tests/test_m.py": module_text(NAME)},
            {"m.py": CHANGED, "tests/test_m.py": module_text(AT_IMPORT, NAME, DOUBLE)},
            {},
            1,
            [f"tests/test_m.py::test_double: {NEVER_RAN}\n"],
            id="a file skipped at import names its new case as one that never ran",
        ),
        pytest.param(
            {"tests/test_m.py": module_text(NAME)},
            {"m.py": CHANGED, "tests/test_m.py": module_text(NAME, EXPECTED)},
            {},
            0,
            [
                "tests/test_m.py::test_double_xfail: proved — the only killer in "
                "its file of m.py:2 `return` made `return None`"
            ],
            id="an expected failure that runs its body is a run",
        ),
        pytest.param(
            {"tests/test_m.py": module_text(NAME)},
            {"tests/test_m.py": module_text(NAME, UNITTEST_EXPECTED)},
            {},
            1,
            [
                "tests/test_m.py::TestExpected::test_by_expected_failure: kills "
                "nothing its file does not"
            ],
            id="a unittest expected failure whose body raised is a run",
        ),
        pytest.param(
            {"tests/test_m.py": module_text(PARTIAL)},
            {"tests/test_m.py": module_text(PARTIAL, DOUBLE)},
            {},
            1,
            ["tests/test_m.py::test_double: kills nothing its file does not"],
            id="a sibling that skips after its assertions still kills",
        ),
        pytest.param(
            {"tests/test_m.py": module_text(NAME)},
            {
                "m.py": CHANGED + "\n\ndef unused():\n    return 7\n",
                "tests/test_m.py": module_text(NAME, DOUBLE),
            },
            {},
            0,
            ["  survived m.py:10 `return` made `return None`"],
            id="a mutant of changed code nothing kills is reported",
        ),
        pytest.param(
            {"tests/test_m.py": module_text(DOUBLE)},
            {"tests/test_m.py": module_text(DOUBLE, NAME)},
            {},
            0,
            [
                "tests/test_m.py::test_name: proved — the only killer in its file of m.py:6"
            ],
            id="a tests-only change draws from the lines its case runs",
        ),
        pytest.param(
            {"tests/test_m.py": module_text(DOUBLE), "doc.md": "One sentence.\n"},
            {
                "doc.md": "One sentence.\nA second sentence.\n",
                "tests/test_m.py": module_text(DOUBLE, PIN),
            },
            {},
            0,
            [
                "tests/test_m.py::test_doc: proved — the only killer in its file "
                "of doc.md:2 line removed"
            ],
            id="S5 a prose pin is proved by its sentence removed",
        ),
        pytest.param(
            {"tests/test_m.py": module_text(DOUBLE)},
            {
                "tests/test_m.py": module_text(
                    DOUBLE.replace("double(2) == 4", "double(3) == 6")
                )
            },
            {},
            0,
            ["tests/test_m.py::test_double: proved"],
            id="S2 a changed function is read as new",
        ),
        pytest.param(
            {"tests/test_m.py": module_text(DOUBLE, NAME)},
            {"tests/test_m.py": module_text(DOUBLE)},
            {},
            0,
            ["  removed tests/test_m.py::test_name"],
            id="a removed case is listed",
        ),
        pytest.param(
            {"tests/test_m.py": module_text()},
            {"m.py": CHANGED, "tests/test_m.py": module_text(DOUBLE)},
            {"extra": ("--bound", "0.0001")},
            1,
            [
                "tests/test_m.py: restructure: test the decision directly",
                "  not run within the bound: ",
            ],
            id="a file whose proof would pass the bound is named to restructure",
        ),
    ],
)
def test_each_real_path_end_to_end(
    tmp_path, capsys, monkeypatch, base, head, options, code, expected
):
    """Each path the check takes, once, on a fixture repository at a base
    commit and at HEAD, with real mutants through `mutation_check.py`. The
    rows are one case on purpose: the check holds one function's ids as one
    killer, so a path's run is not named for sharing its lines with another
    path's. Each row's lines reach stdout and the step summary alike, and
    neither names a path outside the root; each function gets one verdict;
    a proof past the bound is named before any mutant runs, so nothing is
    proved."""
    root = tree(tmp_path, base, head, options.get("newline", "\n"))
    summary = tmp_path / "summary.md"
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(summary))
    found, out = run(root, capsys, *options.get("extra", ()))
    assert found == code, out
    for line in expected:
        assert line in out, out
        assert line in summary.read_text(encoding="utf-8")
    assert str(tmp_path) not in out, out
    verdicts = [v.strip().split(": ", 1)[0] for v in out.split("\n") if "::" in v]
    assert len(verdicts) == len(set(verdicts)), out
    if "extra" in options:
        assert "proved" not in out.split("\n", 1)[1], out
