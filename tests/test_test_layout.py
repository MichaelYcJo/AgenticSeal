"""`test-layout` holds the test layout, and these are its cases (#942).

Every case but one reads fixture text handed to the script's functions, so
no case builds a repository or runs git: `check` takes the tracked paths
and a reader of the target's source as arguments. `Test_main` replaces the
two git readings with fixture values, and its one case over this
repository's own `tests/` is the suite case the layout rests on: it runs
`--check` there and fails when a file in the layout breaks it.

Seen red before they were committed (contract rule 15): every case failed
against the tree without the script, and `mutation-check` broke each refusal
in turn and watched a case of its class fail (the work item's
`phases/phase-1.md`).
"""

import importlib.util
import os

import pytest
from conftest import census_case

TARGET = "skills/verify/scripts/test_layout.py"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_SPEC = importlib.util.spec_from_file_location(
    "specseal_test_layout_under_test", os.path.join(ROOT, TARGET)
)
layout = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(layout)

MODULE = "def parse(text):\n    return text\n\n\ndef _helper():\n    pass\n"
TRACKED = {"hooks/x.py", "tests/test_x.py"}
PLACED = (
    "import os\n"
    "\n"
    'TARGET = "hooks/x.py"\n'
    "\n"
    "\n"
    "class Test_parse:\n"
    "    def test_accepts_text(self):\n"
    '        assert x.parse("a") == 1\n'
    "\n"
    "    def test_refuses_nothing(self):\n"
    '        assert x.parse("") is None\n'
    "\n"
    "\n"
    "class Test_module:\n"
    "    def test_imports(self):\n"
    "        assert os\n"
)
HELPER = "def read(path):\n    return path\n"
UNDECLARED = "import os\n\n\ndef test_a():\n    assert os\n"


def checked(tests, tracked=TRACKED, every=False):
    """`check` over TESTS, the module `MODULE` standing at `hooks/x.py`."""
    return layout.check(tests, tracked, {"hooks/x.py": MODULE}.get, every=every)


class Test_declared_target:
    def test_accepts_the_first_assignment_after_the_imports(self):
        source = '"""Doc."""\n\nimport os\n\nTARGET = "hooks/x.py"\nB = 1\n'
        assert layout.declared_target(source) == "hooks/x.py"

    def test_refuses_a_target_that_is_not_the_first_assignment(self):
        source = 'import os\n\nreader = "/reader"\nTARGET = "/target"\n'
        assert layout.declared_target(source) is None

    def test_refuses_a_target_that_is_not_a_string(self):
        assert layout.declared_target("import os\nTARGET = 1\n") is None


class Test_file_name_for:
    def test_accepts_a_hyphen_written_as_an_underscore(self):
        shipped = ["hooks/worktree-guard.py", "hooks/x.py"]
        name = layout.file_name_for("hooks/worktree-guard.py", shipped)
        assert name == "test_worktree_guard.py"

    def test_accepts_the_parent_before_a_shared_stem(self):
        shipped = ["hooks/config.py", "hooks/git/config.py"]
        assert layout.file_name_for("hooks/git/config.py", shipped) == (
            "test_git_config.py"
        )

    def test_refuses_to_name_a_document(self):
        assert layout.file_name_for("docs/the-review-record.md", []) is None


class Test_definitions:
    def test_accepts_functions_and_classes_at_the_top(self):
        source = (
            "def a():\n    pass\n\n\nasync def b():\n    pass\n\n\nclass C:\n    pass\n"
        )
        assert layout.definitions(source) == {
            "a": "function",
            "b": "function",
            "C": "class",
        }

    def test_refuses_a_method_a_nested_function_and_an_assignment(self):
        source = (
            "X = 1\n\n\nclass C:\n    def m(self):\n        pass\n\n\n"
            "def a():\n    def inner():\n        pass\n"
        )
        assert layout.definitions(source) == {"C": "class", "a": "function"}


class Test_twins:
    def test_accepts_one_helper_defined_in_two_files(self):
        tests = {"tests/test_a.py": HELPER, "tests/test_b.py": HELPER}
        assert layout.twins(tests) == [("read", ["tests/test_a.py", "tests/test_b.py"])]

    def test_refuses_a_case_a_second_definition_in_one_file_and_a_near_copy(self):
        case = "def test_a():\n    assert 1\n"
        tests = {
            "tests/test_a.py": HELPER + "\n\n" + HELPER + "\n\n" + case,
            "tests/test_b.py": HELPER.replace("return path", "return  path") + case,
        }
        assert layout.twins(tests) == []

    def test_refuses_one_body_under_two_decorators(self):
        tests = {
            "tests/test_a.py": "@pytest.fixture\n" + HELPER,
            "tests/test_b.py": '@pytest.fixture(scope="module")\n' + HELPER,
        }
        assert layout.twins(tests) == []


class Test_check:
    def test_accepts_a_placed_file(self):
        assert checked({"tests/test_x.py": PLACED}) == ([], [])

    def test_accepts_a_function_with_no_class_as_a_report(self):
        module = MODULE + "\n\ndef render(text):\n    return text\n"
        refused, reported = layout.check(
            {"tests/test_x.py": PLACED}, TRACKED, {"hooks/x.py": module}.get
        )
        assert refused == []
        assert reported == [
            "report: hooks/x.py: function render has no class Test_render"
        ]

    def test_accepts_an_undeclared_file_as_a_report_until_every_file_is_asked(self):
        tests = {"tests/test_x.py": PLACED, "tests/test_old.py": UNDECLARED}
        assert checked(tests) == ([], ["report: tests/test_old.py: declares no TARGET"])
        refused, _ = checked(tests, every=True)
        assert refused == ["refused: tests/test_old.py: declares no TARGET"]

    def test_accepts_free_names_for_a_flow_and_a_document(self):
        scenario = PLACED.split("\n\nclass Test_module")[0] + "\n"
        flow = scenario.replace("class Test_parse", "class TestOneCommit")
        document = PLACED.replace("hooks/x.py", "docs/x.md").replace(
            "class Test_parse", "class TestTheHeading"
        )
        tests = {"tests/e2e/commit/test_flow.py": flow, "tests/test_doc.py": document}
        refused, _ = checked(tests, tracked=TRACKED | {"docs/x.md"})
        assert refused == []

    def test_refuses_a_class_that_names_no_function_of_the_target(self):
        tests = {"tests/test_x.py": PLACED.replace("Test_parse", "Test_render")}
        refused, _ = checked(tests)
        assert refused == [
            "refused: tests/test_x.py: class Test_render names no top-level "
            "definition of hooks/x.py"
        ]

    def test_refuses_a_class_without_its_refusing_case(self):
        source = PLACED.replace("test_refuses_nothing", "test_accepts_nothing")
        refused, _ = checked({"tests/test_x.py": source})
        assert refused == [
            "refused: tests/test_x.py: class Test_parse has no test_refuses_ case"
        ]

    def test_refuses_a_flow_scenario_without_its_accepting_case(self):
        flow = PLACED.replace("class Test_parse", "class TestOneCommit").replace(
            "test_accepts_text", "test_text"
        )
        refused, _ = checked({"tests/e2e/commit/test_flow.py": flow})
        assert refused == [
            "refused: tests/e2e/commit/test_flow.py: class TestOneCommit has no "
            "test_accepts_ case",
            "refused: tests/e2e/commit/test_flow.py: class Test_module has no "
            "test_accepts_ case",
            "refused: tests/e2e/commit/test_flow.py: class Test_module has no "
            "test_refuses_ case",
        ]

    def test_refuses_a_twin_beside_a_declared_file(self):
        tests = {
            "tests/test_x.py": PLACED + "\n\n" + HELPER,
            "tests/test_old.py": HELPER,
        }
        refused, _ = checked(tests)
        assert refused == [
            "refused: read is defined byte-identically in tests/test_old.py, "
            "tests/test_x.py"
        ]
        _, reported = checked({"tests/test_a.py": HELPER, "tests/test_b.py": HELPER})
        assert (
            "report: read is defined byte-identically in tests/test_a.py, tests/test_b.py"
            in reported
        )

    def test_refuses_a_target_git_does_not_track(self):
        refused, _ = checked({"tests/test_x.py": PLACED}, tracked={"tests/test_x.py"})
        assert refused == [
            "refused: tests/test_x.py: TARGET hooks/x.py is not a file git tracks"
        ]

    def test_refuses_a_file_named_for_another_module(self):
        refused, _ = checked({"tests/test_y.py": PLACED})
        assert refused == [
            "refused: tests/test_y.py: the file for hooks/x.py is named test_x.py"
        ]

    def test_refuses_a_file_that_does_not_parse(self):
        refused, _ = checked({"tests/test_x.py": "def (:\n"})
        assert len(refused) == 1
        assert refused[0].startswith("refused: tests/test_x.py: does not parse")


class Test_pairs:
    @pytest.mark.parametrize(
        "second, why",
        [
            ('x.parse("a") is not None', "call parse with equal arguments"),
            (
                'y.parse("b") == 1',
                "have equal bodies once names and strings are normalised",
            ),
        ],
        ids=["arguments", "bodies"],
    )
    def test_accepts_two_cases_that_look_alike_as_a_pair(self, second, why):
        source = PLACED.replace('x.parse("") is None', second)
        assert layout.pairs({"tests/test_x.py": source}) == [
            f"pair: tests/test_x.py::Test_parse: test_accepts_text and "
            f"test_refuses_nothing {why}"
        ]

    def test_refuses_two_cases_with_other_arguments_and_other_bodies(self):
        source = PLACED.replace('x.parse("") is None', 'x.parse("b") == 2')
        assert layout.pairs({"tests/test_x.py": source}) == []

    def test_refuses_two_cases_passing_a_local_of_one_name(self):
        source = PLACED.replace(
            'assert x.parse("a") == 1', 'text = "a"\n        assert x.parse(text) == 1'
        ).replace(
            'assert x.parse("") is None', 'text = ""\n        assert x.parse(text) == 2'
        )
        assert layout.pairs({"tests/test_x.py": source}) == []


class Test_main:
    def test_accepts_this_repositorys_tests(self, capsys):
        assert layout.main(["--check", os.path.join(ROOT, "tests")]) == 0
        out = capsys.readouterr().out
        assert "refused:" not in out, out
        assert "tests/test_test_layout.py: declares no TARGET" not in out
        assert "declare no TARGET" in out.splitlines()[-1]

    def test_accepts_a_pair_and_exits_zero(self, tmp_path, monkeypatch, capsys):
        (tmp_path / "tests").mkdir()
        source = PLACED.replace('x.parse("") is None', 'x.parse("a") is not None')
        (tmp_path / "tests" / "test_x.py").write_text(source, encoding="utf-8")
        monkeypatch.setattr(layout, "_toplevel", lambda start: str(tmp_path))
        assert layout.main(["--pairs"]) == 0
        assert "test_accepts_text and test_refuses_nothing" in capsys.readouterr().out

    def test_refuses_a_misplaced_class_with_exit_one(
        self, tmp_path, monkeypatch, capsys
    ):
        (tmp_path / "tests").mkdir()
        (tmp_path / "hooks").mkdir()
        source = PLACED.replace("Test_parse", "Test_render")
        (tmp_path / "tests" / "test_x.py").write_text(source, encoding="utf-8")
        (tmp_path / "hooks" / "x.py").write_text(MODULE, encoding="utf-8")
        monkeypatch.setattr(layout, "_toplevel", lambda start: str(tmp_path))
        monkeypatch.setattr(layout, "_tracked", lambda root: set(TRACKED))
        assert layout.main(["--check"]) == 1
        out = capsys.readouterr().out
        assert "tests/test_x.py: class Test_render" in out

    def test_refuses_all_without_check(self, capsys):
        with pytest.raises(SystemExit) as stopped:
            layout.main(["--pairs", "--all"])
        assert stopped.value.code == 2
        assert "--all" in capsys.readouterr().err

    def test_refuses_a_directory_outside_a_repository(self, monkeypatch, capsys):
        monkeypatch.setattr(layout, "_toplevel", lambda start: None)
        assert layout.main(["--check", "--all"]) == 2
        assert "not inside a git repository" in capsys.readouterr().out


test_census = census_case(TARGET)
