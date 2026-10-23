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
import shutil
import textwrap

import pytest
from conftest import census_case, commit_everything_as_e, git_out, write

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
    "\n"
    "\n"
    "test_census = census_case(TARGET)\n"
)
CENSUS_LINE = "\n\ntest_census = census_case(TARGET)\n"
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
        scenario = PLACED.split("\n\nclass Test_module")[0] + CENSUS_LINE
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

    def test_refuses_a_declared_file_that_runs_no_census(self):
        source = PLACED.replace(CENSUS_LINE, "\n")
        refused, _ = checked({"tests/test_x.py": source})
        assert refused == [
            "refused: tests/test_x.py: does not assign test_census = "
            "census_case(TARGET), so no census judges hooks/x.py"
        ]
        other = PLACED.replace("census_case(TARGET)", 'census_case("hooks/y.py")')
        assert checked({"tests/test_x.py": other})[0] == refused
        qualified = PLACED.replace("census_case(", "conftest.census_case(")
        assert checked({"tests/test_x.py": qualified}) == ([], [])

    def test_refuses_a_copy_of_a_conftest_helper_in_a_declared_file(self):
        tests = {"tests/test_x.py": PLACED + "\n\n" + HELPER}
        peers = {**tests, "tests/conftest.py": HELPER, "tests/test_a.py": HELPER}
        refused, _ = layout.check(
            tests, TRACKED, {"hooks/x.py": MODULE}.get, peers=peers
        )
        assert refused == [
            "refused: read is defined byte-identically in tests/conftest.py, "
            "tests/test_a.py, tests/test_x.py"
        ]
        alone = {"tests/conftest.py": HELPER, "tests/test_a.py": HELPER}
        assert layout.check(
            {"tests/test_x.py": PLACED},
            TRACKED,
            {"hooks/x.py": MODULE}.get,
            peers={**alone, "tests/test_x.py": PLACED},
        ) == ([], [])

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

    @pytest.mark.parametrize(
        "first, second",
        [
            (
                'text = "a"\n        assert x.parse(text, strict=True) == 1',
                'text = ""\n        assert x.parse(text, strict=True) == 2',
            ),
            ("assert x.parse() == 1", "assert x.parse() == 2"),
        ],
        ids=["a-local-of-one-name", "no-argument"],
    )
    def test_refuses_two_cases_whose_calls_show_no_input(self, first, second):
        source = PLACED.replace('assert x.parse("a") == 1', first).replace(
            'assert x.parse("") is None', second
        )
        assert layout.pairs({"tests/test_x.py": source}) == []


# The move check's world: three old files at a base commit and the conftest
# beside them. A case asks for a fixture by a parameter, by `usefixtures` on
# its class or in `pytestmark`, and by an autouse fixture of its class; `box`
# requests `base_dir`, and `a` is both a conftest fixture and a parametrized
# name. The third old file holds a case and a fixture that define functions
# and a class with docstrings over three lines, at every depth. Each case
# writes its new file into a copy and runs `--moved` there, which collects
# at the base in a worktree of its own and in the copy.
MOVED_CONFTEST = (
    "import pytest\n"
    "\n"
    "\n"
    "def root_of(path):\n"
    "    return path\n"
    "\n"
    "\n"
    "@pytest.fixture\n"
    "def base_dir(tmp_path):\n"
    "    return root_of(tmp_path)\n"
    "\n"
    "\n"
    "@pytest.fixture\n"
    "def box(base_dir):\n"
    "    return base_dir\n"
    "\n"
    "\n"
    "@pytest.fixture\n"
    "def a():\n"
    "    return 0\n"
    "\n"
    "\n"
    "def census_case(target):\n"
    "    def test_census():\n"
    "        assert target\n"
    "\n"
    "    return test_census\n"
)
MOVED_OLD_A = (
    "import pytest\n"
    "\n"
    'pytestmark = pytest.mark.usefixtures("box")\n'
    "\n"
    "\n"
    "@pytest.fixture\n"
    "def local():\n"
    "    return 1\n"
    "\n"
    "\n"
    "def test_one(box, local):\n"
    "    assert box.exists() and local\n"
    "\n"
    "\n"
    '@pytest.mark.parametrize("a", [1, 2])\n'
    "def test_two(a):\n"
    "    assert a\n"
)
MOVED_OLD_B = (
    "import pytest\n"
    "\n"
    "\n"
    '@pytest.mark.usefixtures("box")\n'
    "class TestThree:\n"
    "    @pytest.fixture(autouse=True)\n"
    "    def quiet(self, monkeypatch):\n"
    '        monkeypatch.setenv("QUIET", "1")\n'
    "\n"
    "    def test_three(self):\n"
    '        """Three."""\n'
    "        assert 3\n"
    "\n"
    "    def test_three_again(self):\n"
    "        assert 3\n"
)
LOCAL = "@pytest.fixture\ndef local():\n    return 1\n\n\n"
# A function with a fixture's name that no fixture decorator makes one.
NOT_A_FIXTURE = "@functools.cache\ndef base_dir():\n    return None\n\n\n"
REFUSE_3 = "    def test_refuses_three(self):\n        assert 3\n"
THREE = (
    "class Test_three:\n"
    "    @pytest.fixture(autouse=True)\n"
    "    def quiet(self, monkeypatch):\n"
    '        monkeypatch.setenv("QUIET", "1")\n'
    "\n"
    "    def test_accepts_three(self):\n"
    "        assert 3\n"
    "\n" + REFUSE_3 + "\n"
    "\n"
)
# The pure move: every old case under a new name, out of a class or into
# one, with its docstring and `self` gone, its fixture moved with it, and the
# census case beside them.
MOVED_NEW = (
    "import functools\n"
    "\n"
    "import pytest\n"
    "from conftest import census_case\n"
    "\n"
    'TARGET = "x.py"\n'
    "\n"
    'pytestmark = pytest.mark.usefixtures("box")\n'
    "\n"
    "\n" + LOCAL + NOT_A_FIXTURE + "class Test_one:\n"
    "    def test_accepts_one(self, box, local):\n"
    "        assert box.exists() and local\n"
    "\n"
    '    @pytest.mark.parametrize("a", [1, 2])\n'
    "    def test_refuses_two(self, a):\n"
    "        assert a\n"
    "\n"
    "\n" + THREE + "test_census = census_case(TARGET)\n"
)
MERGED = MOVED_NEW.replace(
    "        assert box.exists() and local\n",
    "        assert box.exists() and local\n        assert 3\n",
).replace(THREE, "")
SHADOWED = MOVED_NEW.replace(
    LOCAL, LOCAL + "@pytest.fixture\ndef tmp_path():\n    return 1\n\n\n"
)
NESTED_FIXTURE = (
    "@pytest.fixture\n"
    "def maker():\n"
    "    def make():\n"
    '        """Make one.\n'
    "\n"
    "        Over three lines.\n"
    '        """\n'
    "        return 1\n"
    "\n"
    "    return make\n"
)
NESTED_CASE = (
    "def test_four(maker):\n"
    "    def helper():\n"
    '        """Help.\n'
    "\n"
    "        Over three lines.\n"
    '        """\n'
    "\n"
    "        class Four:\n"
    '            """Four.\n'
    "\n"
    "            Over three lines.\n"
    '            """\n'
    "\n"
    "            async def value(self):\n"
    '                """The value.\n'
    "\n"
    "                Over three lines.\n"
    '                """\n'
    "                return 3\n"
    "\n"
    "        return Four\n"
    "\n"
    "    assert helper().value and maker() == 1\n"
)
MOVED_OLD_C = "import pytest\n\n\n" + NESTED_FIXTURE + "\n\n" + NESTED_CASE
# The third old file's case and fixture moved into a class, as the formatter
# the edit hook runs leaves them: every line four spaces deeper, the
# continuation lines of each docstring among them.
NESTED_NEW = "import pytest\n\n\nclass Test_four:\n" + textwrap.indent(
    NESTED_FIXTURE.replace("def maker():", "def maker(self):")
    + "\n"
    + NESTED_CASE.replace(
        "def test_four(maker):", "def test_accepts_four(self, maker):"
    ),
    "    ",
)
# The fourth old file's cases read names from the module around them: a
# helper, a module bound by an import, a row constant, a helper the fixture
# a requested fixture requests calls, a name a loader's call binds, an
# attribute of a module under `tests/`, a class, a name another test file
# defines and a helper of their class; one case reads `self.value` of a fake
# it defines, and a helper no case reads stores a name a case reads. Its new
# file holds them in classes, each name defined as it was. The base also
# holds a directory under `tests/` that is no module.
PARSE = "def parse(s):\n    return loads(s)\n\n\n"
ROWS = 'ROWS = [("a", 1), ("bb", 2)]\n'
D_MODULE = (
    "import posixpath as subject\n"
    "from json import loads\n"
    "\n"
    "import pytest\n"
    "import shapes_d\n"
    "from test_e import V\n"
    "\n" + ROWS + "\n"
    "\n" + PARSE + "def build():\n"
    "    return [1]\n"
    "\n"
    "\n"
    "def load(path):\n"
    "    return path\n"
    "\n"
    "\n"
    'reader = load("hooks/a.py")\n'
    "\n"
    "\n"
    "def unread():\n"
    "    reader = 2\n"
    "    return reader\n"
    "\n"
    "\n"
    "class Pair:\n"
    "    first = 1\n"
    "\n"
    "\n"
    "@pytest.fixture\n"
    "def making():\n"
    "    return build()\n"
    "\n"
    "\n"
    "@pytest.fixture\n"
    "def made(making):\n"
    "    return making\n"
    "\n"
    "\n"
)
D_CASES = (
    "def test_parse():\n"
    '    assert parse("[1, 2]") == loads("[1, 2]")\n'
    "\n"
    "\n"
    "def test_subject():\n"
    '    assert subject.join("a", "b")\n'
    "\n"
    "\n"
    '@pytest.mark.parametrize("text, n", ROWS)\n'
    "def test_rows(text, n):\n"
    "    assert len(text) == n\n"
    "\n"
    "\n"
    "def test_made(made):\n"
    "    assert made\n"
    "\n"
    "\n"
    "def test_reader():\n"
    "    assert reader\n"
    "\n"
    "\n"
    "def test_limit():\n"
    "    assert shapes_d.LIMIT\n"
    "\n"
    "\n"
    "def test_pair():\n"
    "    assert Pair.first\n"
    "\n"
    "\n"
    "def test_value():\n"
    "    assert V\n"
    "\n"
    "\n"
    "def test_fake():\n"
    "    class Fake:\n"
    "        pass\n"
    "\n"
    "    def get(self):\n"
    "        return self.value\n"
    "\n"
    "    Fake.get, Fake.value = get, 1\n"
    "    assert Fake().get()\n"
)
DOUBLE = (
    "class {}:\n"
    "    def _double(self, x):\n"
    "        return 2 * x\n"
    "\n"
    "    def {}(self):\n"
    "        assert self._double(2) == 4\n"
)
SHAPES = "LIMIT = 3\n"
MOVED_OLD_D = D_MODULE + D_CASES + "\n\n" + DOUBLE.format("TestDouble", "test_double")
NAMED_NEW = (
    D_MODULE
    + "class Test_d:\n"
    + textwrap.indent(
        D_CASES.replace("():", "(self):")
        .replace("(made):", "(self, made):")
        .replace("(text, n):", "(self, text, n):"),
        "    ",
    )
    + "\n\n"
    + DOUBLE.format("Test_double", "test_accepts_double")
)
X, Y, Z = "tests/test_x.py", "tests/test_y.py", "tests/test_z.py"
OLD_A, OLD_B = "tests/test_old_a.py", "tests/test_old_b.py"
OLD_C, OLD_D, D = "tests/test_old_c.py", "tests/test_old_d.py", "tests/test_d.py"
CONFTEST, SHAPES_D = "tests/conftest.py", "tests/shapes_d.py"
MARKED = 'import pytest\n\npytestmark = pytest.mark.usefixtures("box")\n\n\n'
# `test_old_a.py` split between two modules' files, one case to each.
SPLIT = {
    X: MARKED + LOCAL + "class Test_one:\n"
    "    def test_accepts_one(self, box, local):\n"
    "        assert box.exists() and local\n",
    Y: MARKED + "class Test_two:\n"
    '    @pytest.mark.parametrize("a", [1, 2])\n'
    "    def test_refuses_two(self, a):\n"
    "        assert a\n",
}
# `test_old_b.py` keeps `test_three_again` for a later group, and its
# `test_three` moved to the new file with `test_old_a.py`'s cases.
KEPT = {
    X: MOVED_NEW.replace(REFUSE_3 + "\n", ""),
    OLD_B: MOVED_OLD_B.replace(
        '    def test_three(self):\n        """Three."""\n        assert 3\n\n', ""
    ),
}
# `test_old_a.py`'s `test_one` landing a second time, in a second new file.
TWICE = "def test_one_again(box, local):\n    assert box.exists() and local\n"
TWO_SCOPED = MOVED_CONFTEST.replace(
    "@pytest.fixture\ndef base_dir", '@pytest.fixture(scope="module")\ndef base_dir'
).replace("@pytest.fixture\ndef a(", '@pytest.fixture(scope="module")\ndef a(')
BODY_GONE = "body: not in the new files unchanged"
NO_OLD = "body: stands for no old case"
DIFFERS = "its definition differs from the base's"
COUNT = "moved: count: the new files collect {} items, the old files 5 at the base"
ONE, TWO = (
    "moved: tests/test_old_a.py::test_one",
    "moved: tests/test_old_a.py::test_two",
)
THREE_OLD = "moved: tests/test_old_b.py::TestThree::test_three"
AGAIN = "moved: tests/test_old_b.py::TestThree::test_three_again"
EVERY = (ONE, TWO, THREE_OLD, AGAIN)


@pytest.fixture(scope="module")
def _moved_world(tmp_path_factory):
    repo = tmp_path_factory.mktemp("moved") / "repo"
    repo.mkdir()
    git_out(repo, "init", "-q")
    write(repo, "tests/conftest.py", MOVED_CONFTEST)
    write(repo, "tests/test_old_a.py", MOVED_OLD_A)
    write(repo, "tests/test_old_b.py", MOVED_OLD_B)
    write(repo, OLD_C, MOVED_OLD_C)
    write(repo, OLD_D, MOVED_OLD_D)
    write(repo, SHAPES_D, SHAPES)
    write(repo, "tests/test_e.py", "V = 1\n")
    write(repo, "tests/data/rows.txt", "a 1\n")
    return repo, commit_everything_as_e(repo, "base")


def run_moved(world, tmp_path, monkeypatch, news, beside=None, olds=(OLD_A, OLD_B)):
    """`--moved` over the base with OLDS as `--from` and NEWS, `{path:
    source}`, written in a copy of the world and named as `--to`, and
    BESIDE, `{path: source}` such as `tests/conftest.py`, written there and
    named in neither list; (exit code, how many worktrees the copy lists
    beside its own, the base)."""
    template, base = world
    repo = tmp_path / "repo"
    shutil.copytree(template, repo, symlinks=True)
    for rel, source in {**news, **(beside or {})}.items():
        write(repo, rel, source)
    monkeypatch.chdir(repo)
    code = layout.main(["--moved", base, "--from", *olds, "--to", *news])
    return code, git_out(repo, "worktree", "list").count("\n"), base


class Test_moved:
    @pytest.mark.parametrize(
        "news, beside, olds, cases, items",
        [
            ({X: MOVED_NEW}, None, (OLD_A, OLD_B), 4, 5),
            ({Z: NESTED_NEW}, None, (OLD_C,), 1, 1),
        ]
        + [
            ({D: new}, beside, (OLD_D,), 10, 11)
            for new, beside in [
                (
                    NAMED_NEW.replace(PARSE, "").replace(
                        "import shapes_d\n",
                        "import shapes_d\nfrom conftest import parse\n",
                    ),
                    {
                        CONFTEST: "from json import loads\n\n"
                        + MOVED_CONFTEST
                        + "\n\n"
                        + PARSE.replace("(s):\n", '(s):\n    """Parse S."""\n')
                    },
                ),
                (
                    NAMED_NEW.replace(ROWS, "").replace(
                        "import shapes_d\n",
                        "import shapes_d\nfrom shapes_d import ROWS\n",
                    ),
                    {SHAPES_D: SHAPES + ROWS},
                ),
                (
                    NAMED_NEW.replace("json import loads", "json import dumps, loads"),
                    None,
                ),
                (NAMED_NEW.replace("    reader = 2\n", "    reader = 3\n"), None),
            ]
        ],
        ids=[
            "every-kind-of-move",
            "a-nested-docstring-re-indented",
            "a-helper-moved-into-conftest",
            "a-constant-moved-into-a-module-under-tests",
            "a-name-imported-beside-another",
            "a-name-a-helper-stores-for-itself-changed",
        ],
    )
    def test_accepts_a_pure_move(
        self,
        _moved_world,
        tmp_path,
        monkeypatch,
        capsys,
        news,
        beside,
        olds,
        cases,
        items,
    ):
        code, others, base = run_moved(
            _moved_world, tmp_path, monkeypatch, news, beside, olds
        )
        out = capsys.readouterr().out
        assert code == 0, out
        assert "moved:" not in out.replace("test-layout: moved:", "")
        assert out.splitlines()[-1] == (
            f"test-layout: moved: {cases} old cases, {items} items against {items} "
            f"at {base[:12]}, 0 failed"
        )
        assert others == 0, "the base's worktree was left behind"

    @pytest.mark.parametrize(
        "news, olds",
        [(SPLIT, (OLD_A,)), (KEPT, (OLD_A, OLD_B))],
        ids=["one-old-file-in-two-new-files", "an-old-file-in-both-sets"],
    )
    def test_accepts_an_old_file_split_across_two_new_files(
        self, _moved_world, tmp_path, monkeypatch, capsys, news, olds
    ):
        code, others, _base = run_moved(
            _moved_world, tmp_path, monkeypatch, news, olds=olds
        )
        out = capsys.readouterr().out
        assert code == 0, out
        assert out.splitlines()[-1].endswith(", 0 failed"), out
        assert others == 0, "the base's worktree was left behind"

    @pytest.mark.parametrize(
        "news, beside, lines, olds",
        [
            (*row, (OLD_A, OLD_B))
            for row in [
                (
                    {X: MOVED_NEW.replace(THREE, "")},
                    None,
                    [
                        COUNT.format(3),
                        f"{THREE_OLD}: {BODY_GONE}",
                        f"{AGAIN}: {BODY_GONE}",
                    ],
                ),
                (
                    {X: MERGED},
                    None,
                    [
                        COUNT.format(3),
                        f"{ONE}: {BODY_GONE}",
                        f"{THREE_OLD}: {BODY_GONE}",
                        f"{AGAIN}: {BODY_GONE}",
                        f"moved: {X}::Test_one::test_accepts_one: {NO_OLD}",
                    ],
                ),
                (
                    {X: MOVED_NEW.replace(REFUSE_3 + "\n", "")},
                    None,
                    [COUNT.format(4), f"{AGAIN}: {BODY_GONE}"],
                ),
                (
                    {X: MOVED_NEW, Y: TWICE},
                    None,
                    [COUNT.format(6), f"moved: {Y}::test_one_again: {NO_OLD}"],
                ),
                (
                    {
                        X: MOVED_NEW.replace(
                            REFUSE_3, REFUSE_3.replace("assert 3", "assert 4")
                        )
                    },
                    None,
                    [
                        f"{AGAIN}: {BODY_GONE}",
                        f"moved: {X}::Test_three::test_refuses_three: {NO_OLD}",
                    ],
                ),
                (
                    {X: MOVED_NEW},
                    {CONFTEST: TWO_SCOPED},
                    [
                        f"{where}: fixture base_dir: its definition differs from the base's"
                        for where in EVERY
                    ],
                ),
                (
                    {X: MOVED_NEW.replace('"QUIET", "1"', '"QUIET", "2"')},
                    None,
                    [
                        f"{where}: fixture quiet: its definition differs from the base's"
                        for where in (THREE_OLD, AGAIN)
                    ],
                ),
                (
                    {
                        X: MOVED_NEW.replace(
                            "@pytest.fixture(autouse=True)", "@pytest.fixture"
                        )
                    },
                    None,
                    [
                        f"{where}: fixture quiet: requested at the base only"
                        for where in (THREE_OLD, AGAIN)
                    ],
                ),
                (
                    {X: MOVED_NEW.replace(LOCAL, "")},
                    None,
                    [f"{ONE}: fixture local: defined at the base only"],
                ),
                (
                    {X: SHADOWED},
                    None,
                    [
                        f"{where}: fixture tmp_path: defined in the working tree only"
                        for where in EVERY
                    ],
                ),
            ]
        ]
        + [
            (
                {Z: NESTED_NEW.replace("return 3", "return 4")},
                None,
                [
                    f"moved: {OLD_C}::test_four: {BODY_GONE}",
                    f"moved: {Z}::Test_four::test_accepts_four: {NO_OLD}",
                ],
                (OLD_C,),
            )
        ]
        + [
            (
                {D: NAMED_NEW.replace(*change)} if change else {D: NAMED_NEW},
                beside,
                [f"moved: {OLD_D}::{case}: name {name}: {DIFFERS}"],
                (OLD_D,),
            )
            for change, beside, case, name in [
                (("return loads(s)", "return [1, 2]"), None, "test_parse", "parse"),
                (("posixpath as", "ntpath as"), None, "test_subject", "subject"),
                (('("bb", 2)', '("a", 1)'), None, "test_rows", "ROWS"),
                (("return [1]", "return []"), None, "test_made", "build"),
                (("hooks/a.py", "hooks/b.py"), None, "test_reader", "reader"),
                (None, {SHAPES_D: "LIMIT = 4\n"}, "test_limit", "shapes_d.LIMIT"),
                (
                    ("return 2 * x", "return x + x"),
                    None,
                    "TestDouble::test_double",
                    "self._double",
                ),
                (("return path", "return None"), None, "test_reader", "load"),
                (
                    ("import shapes_d\n", "from conftest import shapes_d\n"),
                    {CONFTEST: "import shapes_d\n" + MOVED_CONFTEST},
                    "test_limit",
                    "shapes_d.LIMIT",
                ),
                (
                    ("from test_e import", "from test_f import"),
                    {"tests/test_f.py": "V = 1\n"},
                    "test_value",
                    "V",
                ),
            ]
        ]
        + [
            (
                {X: MOVED_NEW},
                {CONFTEST: MOVED_CONFTEST.replace("return path", "return None")},
                [f"{where}: name root_of: {DIFFERS}" for where in EVERY],
                (OLD_A, OLD_B),
            ),
            (
                {D: NAMED_NEW.replace("return making\n", "return making or ROWS\n")},
                None,
                [f"moved: {OLD_D}::test_made: fixture made: {DIFFERS}"],
                (OLD_D,),
            ),
        ],
        ids=[
            "a-cut",
            "a-merge",
            "two-alike-merged",
            "a-case-landing-twice",
            "an-edited-body",
            "a-changed-fixture",
            "a-changed-class-fixture",
            "a-lost-autouse",
            "a-fixture-left-behind",
            "a-shadowed-fixture",
            "an-edited-nested-function",
            "a-changed-helper",
            "a-rebound-module",
            "a-changed-row-constant",
            "a-changed-fixture-helper",
            "a-loader-given-another-path",
            "a-changed-module-attribute",
            "a-changed-class-helper",
            "a-name-a-helper-reads",
            "a-module-reached-another-way",
            "a-name-imported-from-another-test-file",
            "a-changed-conftest-helper",
            "a-changed-fixture-reading-another-name",
        ],
    )
    def test_refuses_a_cut_a_merge_an_edited_body_and_a_changed_fixture(
        self, _moved_world, tmp_path, monkeypatch, capsys, news, beside, lines, olds
    ):
        code, others, _base = run_moved(
            _moved_world, tmp_path, monkeypatch, news, beside, olds
        )
        out = capsys.readouterr().out
        assert code == 1, out
        assert [line for line in out.splitlines() if line.startswith("moved:")] == (
            lines
        )
        assert out.splitlines()[-1].endswith(f"{len(lines)} failed"), out
        assert others == 0, "the base's worktree was left behind"

    def test_refuses_a_base_or_a_file_it_cannot_read(
        self, _moved_world, tmp_path, monkeypatch, capsys
    ):
        repo, base = _moved_world
        monkeypatch.chdir(repo)
        args = ["--from", OLD_A, "--to", OLD_A]
        assert layout.main(["--moved", "no-such-commit", *args]) == 2
        assert "no-such-commit names no commit" in capsys.readouterr().out
        args = ["--from", "tests/test_gone.py", "--to", OLD_A]
        assert layout.main(["--moved", base, *args]) == 2
        assert "tests/test_gone.py is not a file at" in capsys.readouterr().out
        args = ["--from", OLD_A, "--to", "tests/test_gone.py"]
        assert layout.main(["--moved", base, *args]) == 2
        assert "tests/test_gone.py cannot be read" in capsys.readouterr().out

    @pytest.mark.parametrize(
        "args",
        [
            ["--moved", "HEAD", "--from", OLD_A, X],
            ["--moved", "HEAD", "--from", OLD_A, "--to", X, "--", Y],
            ["--check", "--to", X],
        ],
        ids=[
            "the-new-file-as-the-last-from-word",
            "a-path-after-the-lists",
            "to-alone",
        ],
    )
    def test_refuses_a_new_file_no_to_names(self, args, capsys):
        with pytest.raises(SystemExit) as stopped:
            layout.main(args)
        assert stopped.value.code == 2
        assert "--to" in capsys.readouterr().err


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

    def test_refuses_a_path_that_names_nothing(self, capsys):
        missing = os.path.join(ROOT, "tests", "test_no_such_file.py")
        assert layout.main(["--check", missing]) == 2
        assert f"{missing} names no file or directory" in capsys.readouterr().out

    def test_refuses_a_directory_outside_a_repository(self, monkeypatch, capsys):
        monkeypatch.setattr(layout, "_toplevel", lambda start: None)
        assert layout.main(["--check", "--all"]) == 2
        assert "not inside a git repository" in capsys.readouterr().out


test_census = census_case(TARGET)
