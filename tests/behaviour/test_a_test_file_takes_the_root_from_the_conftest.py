"""A test file takes the repository root from `tests/conftest.py`, and no two
Python files under `tests/` share a name (`CONTRIBUTING.md` *The test
layout*).

Both cases walk `tests/` whole. The cases of the conftest's helpers stand
in `tests/test_conftest.py`.
"""

import ast
import os

import conftest
from conftest import posix_id
from test_conftest import TESTS

# No TARGET: its cases walk every Python file under tests/.


def python_files(top):
    """The path of every Python file under TOP, `__pycache__` left out, in
    walk order."""
    found = []
    for directory, subdirectories, names in os.walk(top):
        subdirectories[:] = sorted(d for d in subdirectories if d != "__pycache__")
        found += [
            os.path.join(directory, n) for n in sorted(names) if n.endswith(".py")
        ]
    return found


def own_path_directories(path):
    """The line numbers at which the Python file at PATH takes a directory
    from its own `__file__`: the name inside a `dirname` call, or under a
    `.parent` or `.parents` of a path built from it. A `__file__` inside a
    string, such as a fixture's source, is no name in this file, and a loaded
    module's `module.__file__` is an attribute, so neither is read."""
    with open(path, encoding="utf-8") as handle:
        tree = ast.parse(handle.read(), path)
    lines = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            climbs = getattr(func, "attr", getattr(func, "id", None)) == "dirname"
        else:
            climbs = isinstance(node, ast.Attribute) and node.attr in (
                "parent",
                "parents",
            )
        if climbs:
            lines |= {
                n.lineno
                for n in ast.walk(node)
                if isinstance(n, ast.Name) and n.id == "__file__"
            }
    return sorted(lines)


def shared_names(top):
    """`{name: [paths]}` for each file name two Python files under TOP hold,
    each path relative to TOP and written with `/`."""
    held = {}
    for path in python_files(top):
        rel = posix_id(os.path.relpath(path, top))
        held.setdefault(os.path.basename(path), []).append(rel)
    return {name: paths for name, paths in held.items() if len(paths) > 1}


def test_no_test_file_derives_the_root_from_its_own_path():
    """`ROOT` is the one source of the repository root (#1060). A test
    file that climbed from its own `__file__` was right only at the depth
    it stood at: moving the test files one directory down meant one edit
    in each, and a file left at the old depth made a glob under the root
    empty, so a case looping over it passed over nothing. A test file
    imports `ROOT` from `tests/conftest.py`, and `CONTRIBUTING.md` *The
    test layout* says so."""
    found = [
        f"{conftest.repo_relative(path)}:{line}"
        for path in python_files(TESTS)
        if os.path.basename(path).startswith("test_")
        for line in own_path_directories(path)
    ]
    assert found == [], (
        "a test file takes the repository root from `tests/conftest.py#ROOT`, "
        f"not from its own `__file__`: {found}"
    )


def test_no_two_python_files_under_tests_share_a_name():
    """The module puts every directory under `tests/` that holds a test
    file on `sys.path`, and pytest's `prepend` mode imports each test
    file by its bare name (#1060). Two files of one name then import as
    one module: pytest fails the collection of the second test file, and
    a helper of one name shadows the other wherever the path finds it
    first. Files that are not Python are not imported and are not read."""
    found = shared_names(TESTS)
    assert found == {}, (
        "each Python file under `tests/` keeps a name no other one holds, "
        f"wherever it stands: {found}"
    )
