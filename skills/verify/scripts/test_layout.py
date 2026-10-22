#!/usr/bin/env python3
"""test-layout: whether each test file stands where the test layout puts it.

  test-layout --check [paths]         refuse a file that breaks the layout
  test-layout --check --all [paths]   refuse a file that declares no TARGET too
  test-layout --pairs [paths]         name two cases of a class that look alike

#942. A test file names the module it tests once, as the first assignment
after its imports, `TARGET = "<tracked path>"`, and holds one class per
top-level definition of that module, `Test_<name>`, each with a case named
`test_accepts_...` and one named `test_refuses_...`. `CONTRIBUTING.md`
*The test layout* states the rules; this script is their one reader. It
reads `tests/**/test_*.py` under the repository the first path, or the
current directory, is in.

`--check` refuses, each on a line that opens with `refused:`:

  a TARGET git does not track
  a file whose name is not `test_<stem>.py` for its TARGET, where the stem
  is the module's file name without `.py` and with each hyphen written as
  an underscore, and takes its parent directory's name before it where
  another tracked module outside `tests/` has the same stem
  a class `Test_<name>` naming no top-level definition of TARGET
  a class lacking a `test_accepts_` case or a `test_refuses_` case
  a non-test top-level function defined byte-identically in two test files,
  where one of them declares TARGET

`Test_module` holds what the module does as a whole and needs no pair. A
file under `tests/e2e/` tests a flow: its classes are scenarios, free-named,
and each keeps the pair. A TARGET that is not a `.py` file is a document,
and its file's name and classes are free.

It prints, on lines that open with `report:`, each file that declares no
TARGET, each twin between two such files, and each public top-level
function of a TARGET that has no class. `--all` makes the first two refusals.

`--pairs` prints, for each class, two cases that call the class's function
with equal argument expressions, or whose bodies are equal once every name
and every string constant is replaced by one placeholder. An argument that
reads a name the case assigns or takes as a parameter is not compared,
because two cases passing a local `source` pass two values. Attribute names
are kept, so two cases calling different methods of one object differ.

Exit codes: `--check` 0 when nothing is refused and 1 when something is.
`--pairs` 0 whatever it prints. 2 for either: the directory is not inside a
git repository, or the arguments do not parse.
"""

import argparse
import ast
import copy
import os
import posixpath
import subprocess
import sys

TARGET_NAME = "TARGET"
MODULE_CLASS = "Test_module"
CLASS_PREFIX = "Test_"
ACCEPTS = "test_accepts_"
REFUSES = "test_refuses_"
E2E = "tests/e2e/"
TESTS = "tests/"


def declared_target(source):
    """The TARGET SOURCE declares, or None where it declares none.

    The declaration is the first statement after the module docstring and
    the imports, assigning one string to `TARGET`. A file whose first
    assignment is another name declares nothing, whatever it assigns later.
    """
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    return _declared(tree)


def _declared(tree):
    body = list(tree.body)
    if body and _is_docstring(body[0]):
        body = body[1:]
    while body and isinstance(body[0], (ast.Import, ast.ImportFrom)):
        body = body[1:]
    if not body or not isinstance(body[0], ast.Assign):
        return None
    node = body[0]
    if len(node.targets) != 1:
        return None
    name = node.targets[0]
    if not isinstance(name, ast.Name) or name.id != TARGET_NAME:
        return None
    if not isinstance(node.value, ast.Constant) or not isinstance(
        node.value.value, str
    ):
        return None
    return node.value.value


def _is_docstring(node):
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(node.value.value, str)
    )


def _stem(path):
    base = posixpath.basename(path)
    return base.rsplit(".", 1)[0].replace("-", "_")


def file_name_for(target, shipped):
    """The name of the test file for TARGET, or None for a document.

    SHIPPED is every tracked `.py` path outside `tests/`. Where another of
    them has TARGET's stem, the parent directory's name goes before it.
    """
    if not target.endswith(".py"):
        return None
    stem = _stem(target)
    if any(_stem(other) == stem for other in shipped if other != target):
        parent = posixpath.basename(posixpath.dirname(target))
        parent = parent.lstrip(".").replace("-", "_")
        if parent:
            stem = f"{parent}_{stem}"
    return f"test_{stem}.py"


def definitions(source):
    """`{name: "function" | "class"}` for each top-level definition."""
    found = {}
    for node in ast.parse(source).body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            found[node.name] = "function"
        elif isinstance(node, ast.ClassDef):
            found[node.name] = "class"
    return found


def _helpers(source):
    """`[(name, text)]` for each top-level function not named `test...`,
    its text running from its first decorator to its last line."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []
    lines = source.splitlines(keepends=True)
    found = []
    for node in tree.body:
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if node.name.startswith("test"):
            continue
        start = min([node.lineno] + [d.lineno for d in node.decorator_list])
        found.append((node.name, "".join(lines[start - 1 : node.end_lineno])))
    return found


def twins(tests):
    """`[(name, [files])]` for each function `_helpers` finds defined
    byte-identically in two or more of TESTS, `{path: source}`."""
    where = {}
    for rel in sorted(tests):
        for name, text in _helpers(tests[rel]):
            files = where.setdefault((name, text), [])
            if rel not in files:
                files.append(rel)
    return sorted(
        (name, files) for (name, _text), files in where.items() if len(files) > 1
    )


def _test_classes(tree):
    return [
        node
        for node in tree.body
        if isinstance(node, ast.ClassDef) and node.name.startswith("Test")
    ]


def _cases(cls):
    return [
        node
        for node in cls.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name.startswith("test")
    ]


def _missing_kinds(rel, cls):
    names = [case.name for case in _cases(cls)]
    return [
        f"refused: {rel}: class {cls.name} has no {prefix} case"
        for prefix in (ACCEPTS, REFUSES)
        if not any(name.startswith(prefix) for name in names)
    ]


def check(tests, tracked, read, every=False):
    """`(refused, reported)`, two lists of lines, for TESTS, `{path: source}`.

    TRACKED is the set of paths git tracks, and READ returns a tracked
    path's source or None. With EVERY, a file that declares no TARGET and a
    twin between two such files are refused rather than reported.
    """
    shipped = sorted(
        p for p in tracked if p.endswith(".py") and not p.startswith(TESTS)
    )
    refused, reported = [], []
    covered = {}
    declared = set()
    for rel in sorted(tests):
        try:
            tree = ast.parse(tests[rel])
        except SyntaxError as exc:
            refused.append(
                f"refused: {rel}: does not parse: {exc.msg} at line {exc.lineno}"
            )
            continue
        target = _declared(tree)
        if target is None:
            line = f"{rel}: declares no {TARGET_NAME}"
            (refused if every else reported).append(
                f"refused: {line}" if every else f"report: {line}"
            )
            continue
        declared.add(rel)
        if target not in tracked:
            refused.append(
                f"refused: {rel}: {TARGET_NAME} {target} is not a file git tracks"
            )
            continue
        flow = rel.startswith(E2E)
        module = target.endswith(".py") and not flow
        defs = {}
        if module:
            expected = file_name_for(target, shipped)
            if posixpath.basename(rel) != expected:
                refused.append(
                    f"refused: {rel}: the file for {target} is named {expected}"
                )
            try:
                defs = definitions(read(target) or "")
            except SyntaxError:
                refused.append(f"refused: {rel}: {TARGET_NAME} {target} does not parse")
                continue
            covered.setdefault(target, (defs, set()))
        for cls in _test_classes(tree):
            if module:
                if cls.name == MODULE_CLASS:
                    continue
                name = (
                    cls.name[len(CLASS_PREFIX) :]
                    if cls.name.startswith(CLASS_PREFIX)
                    else None
                )
                if name not in defs:
                    refused.append(
                        f"refused: {rel}: class {cls.name} names no top-level "
                        f"definition of {target}"
                    )
                    continue
                covered[target][1].add(name)
            elif not flow:
                continue
            refused.extend(_missing_kinds(rel, cls))
    for target in sorted(covered):
        defs, classes = covered[target]
        for name in sorted(defs):
            if (
                defs[name] == "function"
                and not name.startswith("_")
                and name not in classes
            ):
                reported.append(
                    f"report: {target}: function {name} has no class {CLASS_PREFIX}{name}"
                )
    for name, files in twins(tests):
        line = f"{name} is defined byte-identically in {', '.join(files)}"
        if every or declared.intersection(files):
            refused.append(f"refused: {line}")
        else:
            reported.append(f"report: {line}")
    return refused, reported


class _Normalised(ast.NodeTransformer):
    """Every name and every string constant replaced by one placeholder."""

    def visit_Name(self, node):
        return ast.copy_location(ast.Name(id="_", ctx=node.ctx), node)

    def visit_arg(self, node):
        node.arg = "_"
        return self.generic_visit(node)

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            return ast.copy_location(ast.Constant(value=""), node)
        return node


def _body(case):
    body = copy.deepcopy(case.body)
    module = ast.Module(body=body, type_ignores=[])
    return ast.dump(_Normalised().visit(module))


def _calls(case, function):
    """Each call of FUNCTION in CASE, dumped without its callee, leaving out
    a call whose arguments read a name the case assigns or takes as a
    parameter: two cases passing a local `source` pass two values."""
    local = {arg.arg for arg in ast.walk(case.args) if isinstance(arg, ast.arg)}
    local |= {
        node.id
        for node in ast.walk(case)
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store)
    }
    found = set()
    for node in ast.walk(case):
        if not isinstance(node, ast.Call):
            continue
        callee = node.func
        named = (isinstance(callee, ast.Name) and callee.id == function) or (
            isinstance(callee, ast.Attribute) and callee.attr == function
        )
        arguments = ast.Tuple(elts=[*node.args, *node.keywords], ctx=ast.Load())
        reads = {n.id for n in ast.walk(arguments) if isinstance(n, ast.Name)}
        if named and not reads & local:
            found.add(
                ast.dump(
                    ast.Call(
                        func=ast.Name(id="_"), args=node.args, keywords=node.keywords
                    )
                )
            )
    return found


def pairs(tests):
    """One line for each two cases of one class in TESTS, `{path: source}`,
    that call the class's function with equal arguments or have bodies equal
    once names and strings are normalised."""
    lines = []
    for rel in sorted(tests):
        try:
            tree = ast.parse(tests[rel])
        except SyntaxError:
            continue
        for cls in _test_classes(tree):
            function = (
                cls.name[len(CLASS_PREFIX) :]
                if cls.name.startswith(CLASS_PREFIX)
                else None
            )
            cases = _cases(cls)
            for i, first in enumerate(cases):
                for second in cases[i + 1 :]:
                    where = f"pair: {rel}::{cls.name}: {first.name} and {second.name}"
                    if function and _calls(first, function) & _calls(second, function):
                        lines.append(f"{where} call {function} with equal arguments")
                    elif _body(first) == _body(second):
                        lines.append(
                            f"{where} have equal bodies once names and strings are normalised"
                        )
    return lines


def _toplevel(start):
    """The repository START is in, or None outside one."""
    result = subprocess.run(
        ["git", "-C", start, "rev-parse", "--show-toplevel"],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def _tracked(root):
    result = subprocess.run(
        ["git", "-C", root, "ls-files", "-z"],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        check=True,
    )
    return {path for path in result.stdout.split("\0") if path}


def _read(root, rel):
    try:
        with open(os.path.join(root, rel), encoding="utf-8") as handle:
            return handle.read()
    except OSError:
        return None


def _read_tests(root, paths):
    """`{path: source}` for each `test_*.py` at or under PATHS, each path
    relative to ROOT and written with `/`."""
    files = []
    for path in paths:
        if os.path.isfile(path):
            files.append(path)
            continue
        for directory, subdirectories, names in os.walk(path):
            subdirectories[:] = sorted(d for d in subdirectories if d != "__pycache__")
            files += [
                os.path.join(directory, name)
                for name in names
                if name.startswith("test_") and name.endswith(".py")
            ]
    found = {}
    for path in files:
        rel = os.path.relpath(path, root).replace(os.sep, "/")
        text = _read(root, rel)
        if text is not None:
            found[rel] = text
    return found


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="test-layout",
        description="Whether each test file stands where the test layout puts it.",
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--check", action="store_true", help="refuse what breaks the layout"
    )
    mode.add_argument("--pairs", action="store_true", help="name cases that look alike")
    parser.add_argument(
        "--all",
        action="store_true",
        help="with --check, refuse a file that declares no TARGET",
    )
    parser.add_argument(
        "paths", nargs="*", help="files or directories; tests/ when none"
    )
    args = parser.parse_args(argv)
    if args.all and not args.check:
        parser.error("--all goes with --check")
    first = args.paths[0] if args.paths else os.getcwd()
    start = first if os.path.isdir(first) else os.path.dirname(os.path.abspath(first))
    root = _toplevel(start)
    if root is None:
        print(f"test-layout: {start} is not inside a git repository", flush=True)
        return 2
    tests = _read_tests(root, args.paths or [os.path.join(root, "tests")])
    if args.pairs:
        lines = pairs(tests)
        for line in lines:
            print(line)
        print(f"test-layout: {len(tests)} files read, {len(lines)} pairs", flush=True)
        return 0
    refused, reported = check(
        tests, _tracked(root), lambda rel: _read(root, rel), every=args.all
    )
    for line in refused + reported:
        print(line)
    undeclared = sum(
        1 for line in refused + reported if line.endswith(f"declares no {TARGET_NAME}")
    )
    print(
        f"test-layout: {len(tests)} files read, {len(refused)} refused, "
        f"{undeclared} declare no {TARGET_NAME}",
        flush=True,
    )
    return 1 if refused else 0


if __name__ == "__main__":
    sys.exit(main())
