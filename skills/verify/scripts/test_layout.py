#!/usr/bin/env python3
"""test-layout: whether each test file stands where the test layout puts it.

  test-layout --check [paths]         refuse a file that breaks the layout
  test-layout --check --all [paths]   refuse a file that declares no TARGET too
  test-layout --pairs [paths]         name two cases of a class that look alike
  test-layout --moved BASE --from OLD... --to NEW...
                                      whether the NEW files hold the OLD
                                      files' cases, only moved

#942. A test file names the module it tests once, as the first assignment
after its imports, `TARGET = "<tracked path>"`, holds one class per public
top-level function of that module, `Test_<name>`, each with a case named
`test_accepts_...` and one named `test_refuses_...`, and ends with
`test_census = census_case(TARGET)`. `CONTRIBUTING.md`
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
  a file that declares TARGET and does not assign
  `test_census = census_case(TARGET)`
  a non-test top-level function defined byte-identically in two test files,
  or in a test file and `tests/conftest.py`, where one of them declares
  TARGET; the helpers of the paths named are compared with every test file
  and `tests/conftest.py`, whatever the paths name

`Test_module` holds what the module does as a whole and needs no pair. A
file under `tests/e2e/` tests a flow: its classes are scenarios, free-named,
and each keeps the pair. A TARGET that is not a `.py` file is a document,
and its file's name and classes are free.

It prints, on lines that open with `report:`, each file that declares no
TARGET, each twin between two such files, and each public top-level
function of a TARGET that has no class. `--all` makes the first two refusals.

`--pairs` prints, for each class, two cases that call the class's function
with equal argument expressions, or whose bodies are equal once every name
and every string constant is replaced by one placeholder. A call with an
argument that reads a name the case assigns or takes as a parameter is not
compared at all: two cases passing a local `source` pass two values, and
the input such a call reads is on disk or in a fixture, where the report
cannot see it. A call with no argument is not compared either, because any
two such calls are equal. Attribute names are kept, so two cases calling
different methods of one object differ.

`--moved` is the move check of `CONTRIBUTING.md` *The test layout*: it
passes a group of modules whose old cases were only moved into the NEW
files, with nothing cut, merged or rewritten, and such a group needs no
mutants. It reads each OLD file at BASE through `git show` and each NEW
file in the working tree; one path may stand in both lists, for an old
file that keeps cases for a later group. It prints a line opening with
`moved:` for each failure of the conditions below:

  count    pytest collects as many items from the NEW files as from the OLD
           files at BASE, each parametrize row one item, the census case
           left out on both sides; BASE's items are collected in a detached
           worktree of BASE added under a temporary directory and removed
           before the check ends
  body     each old case is a case of the NEW files unchanged apart from its
           name, its place, the class around it, a `self` parameter and its
           docstrings, its own and those of every function and class it
           defines at any depth, which the formatter the edit hook runs
           re-indents to the depth a move puts them at; each new case
           stands for one old case, and a new case that stands for none is
           named, so an old case that lands twice is named by its second
           landing
  fixture  the two cases request the same fixtures, by parameter, by
           `usefixtures` or as autouse, and each, followed through the
           fixtures it requests, is defined alike in both trees, in the
           case's class, its file or `tests/conftest.py`, read as a case's
           body is read; a name defined in neither tree is pytest's own
  names    each name the case and those fixtures read from the module
           around them, as Python's scoping resolves it, is defined alike in
           both trees: a helper, a constant a `parametrize` mark reads, a
           module an import or a loader's call binds, and `self.<name>`
           where the case's class binds it, outside a function or lambda
           that takes a `self` of its own; each definition is followed
           through the names it reads in turn. A name that
           `from <module> import` brings, or that `<module>.<name>` reads
           after `import <module>`, where the module is any module
           directly under `tests/`, a test file among them, is read where
           that module defines it, in the same tree, so a helper moved
           unchanged into `tests/conftest.py` or into another test file
           passes. A function or class compares as a case's body does, an
           import as the one alias that binds the name, any other
           statement as written, and a statement binding the name inside
           a compound statement as that whole statement. A name bound in
           neither tree is a builtin's or pytest's, a name bound in one
           tree only is a change, and so is a name one tree's reading
           reaches and the other's does not. Each name is compared as the
           set of its distinct definitions, so one definition reached
           from two files counts once. The condition has two limits: a
           name a case reaches only through a string, such as
           `globals()["x"]`, is not read, and two definitions of one name
           in two places a case reaches, swapped between the trees,
           compare equal. A case is tested on this condition only where
           it passed the body and fixture conditions, and its line names
           every name whose own definition differs, those both trees reach
           first and then those one tree's reading reaches alone, each run
           in alphabetical order: `name <name>: its definition differs
           from the base's` for one name, and `names <name>, <name>: their
           definitions differ from the base's` for more

It then prints the old cases, both counts and the failures on one last line.

Exit codes: `--check` 0 when nothing is refused and 1 when something is.
`--pairs` 0 whatever it prints. `--moved` 0 where the group passes and 1
where it does not. 2 for any of them: the directory is not inside a git
repository, a path names no file or directory, or the arguments do not
parse; for `--moved` that includes a path in neither list, so the new file
written as the last word after `--from` is refused. And 2 for `--moved`
where BASE names no commit, BASE does not hold an OLD file, a NEW file
cannot be read, or pytest cannot make a collection.
"""

import argparse
import ast
import copy
import importlib.util
import os
import posixpath
import shutil
import subprocess
import symtable
import sys
import tempfile
import types

TARGET_NAME = "TARGET"
MODULE_CLASS = "Test_module"
CLASS_PREFIX = "Test_"
ACCEPTS = "test_accepts_"
REFUSES = "test_refuses_"
E2E = "tests/e2e/"
TESTS = "tests/"
CONFTEST_MODULE = "conftest"


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
    found = []
    for node in tree.body:
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if node.name.startswith("test"):
            continue
        # From column 0 of the first decorator's line: the parser's own line
        # count, through `ast.get_source_segment`, places it.
        span = types.SimpleNamespace(
            lineno=min([node.lineno] + [d.lineno for d in node.decorator_list]),
            col_offset=0,
            end_lineno=node.end_lineno,
            end_col_offset=node.end_col_offset,
        )
        found.append((node.name, ast.get_source_segment(source, span)))
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


CENSUS_CASE = "test_census = census_case(TARGET)"


def runs_the_censuses(tree):
    """Whether TREE assigns `test_census` a call of `census_case` on
    `TARGET` at its top level, called bare or as `conftest.census_case`."""
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        name, call = node.targets[0], node.value
        if not (isinstance(name, ast.Name) and name.id == "test_census"):
            continue
        if not isinstance(call, ast.Call) or len(call.args) != 1:
            continue
        func = call.func
        called = func.id if isinstance(func, ast.Name) else getattr(func, "attr", None)
        argument = call.args[0]
        if (
            called == "census_case"
            and isinstance(argument, ast.Name)
            and argument.id == TARGET_NAME
        ):
            return True
    return False


def check(tests, tracked, read, every=False, peers=None):
    """`(refused, reported)`, two lists of lines, for TESTS, `{path: source}`.

    TRACKED is the set of paths git tracks, and READ returns a tracked
    path's source or None. With EVERY, a file that declares no TARGET and a
    twin between two such files are refused rather than reported. PEERS,
    `{path: source}`, are the files whose helpers TESTS' helpers are compared
    with, TESTS where none are given; a twin is judged only where one of its
    files is in TESTS.
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
        if not runs_the_censuses(tree):
            refused.append(
                f"refused: {rel}: does not assign {CENSUS_CASE}, "
                f"so no census judges {target}"
            )
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
    for name, files in twins(peers or tests):
        if not set(files) & set(tests):
            continue
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
    a call with no argument, since any two such calls are equal, and a call
    whose arguments read a name the case assigns or takes as a parameter:
    two cases passing a local `source` pass two values."""
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
        given = node.args or node.keywords
        if named and given and not reads & local:
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


# --- the move check ----------------------------------------------------------


def _all_cases(tree):
    """`[(qualified name, class or None, case)]` for every case pytest
    collects by its default names: a `test...` function at the top, or a
    `test...` method of a `Test...` class."""
    found = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name.startswith("test"):
                found.append((node.name, None, node))
        elif isinstance(node, ast.ClassDef) and node.name.startswith("Test"):
            found += [(f"{node.name}::{c.name}", node, c) for c in _cases(node)]
    return found


def _without_docstring(body):
    return body[1:] if body and _is_docstring(body[0]) else body


def _moved_form(definition):
    """DEFINITION, a case, a fixture, or a function or class a case reads,
    as an AST dump that keeps its decorators, its parameters and its body,
    and drops its name, a first `self`, and the docstring of DEFINITION and
    of every function and class it defines, at any depth. The formatter the
    edit hook runs re-indents a nested docstring's continuation lines to the
    depth a move puts it at, so a docstring compared would fail a case whose
    code did not change."""
    node = copy.deepcopy(definition)
    node.name = ""
    for inner in list(ast.walk(node)):
        if isinstance(inner, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            inner.body = _without_docstring(inner.body) or [ast.Pass()]
    if isinstance(node, ast.ClassDef):
        return ast.dump(node)
    params = node.args.posonlyargs or node.args.args
    if params and params[0].arg == "self":
        del params[0]
    return ast.dump(node)


def _parametrized(case):
    """The names CASE's `parametrize` marks hand it, which are no fixture."""
    names = set()
    for mark in case.decorator_list:
        if not (
            isinstance(mark, ast.Call)
            and getattr(mark.func, "attr", None) == "parametrize"
            and mark.args
        ):
            continue
        first = mark.args[0]
        if isinstance(first, ast.Constant) and isinstance(first.value, str):
            names |= {n.strip() for n in first.value.split(",")}
        elif isinstance(first, (ast.List, ast.Tuple)):
            names |= {e.value for e in first.elts if isinstance(e, ast.Constant)}
    return names


def _used(decorators):
    """The fixture names `usefixtures` marks among DECORATORS name."""
    names = set()
    for node in decorators:
        for call in ast.walk(node):
            if (
                isinstance(call, ast.Call)
                and getattr(call.func, "attr", None) == "usefixtures"
            ):
                names |= {
                    a.value
                    for a in call.args
                    if isinstance(a, ast.Constant) and isinstance(a.value, str)
                }
    return names


def _parameters(node):
    args = node.args
    return [a.arg for a in args.posonlyargs + args.args + args.kwonlyargs]


def _fixtures(body):
    """`{name: (definition, autouse)}` for each function in BODY that a
    `pytest.fixture` decorator, called or not, makes a fixture; a fixture
    renamed through `name=` is read under its function's name, a spelling
    no test file here uses."""
    found = {}
    for node in body:
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        for mark in node.decorator_list:
            call = mark if isinstance(mark, ast.Call) else None
            func = call.func if call else mark
            if getattr(func, "attr", None) != "fixture":
                continue
            autouse = any(
                k.arg == "autouse" and getattr(k.value, "value", False) is True
                for k in (call.keywords if call else [])
            )
            found[node.name] = (node, autouse)
    return found


def _requested(tree, cls, case, conftest):
    """The fixtures CASE asks for: its parameters less `self` and what its
    `parametrize` marks hand it, the `usefixtures` marks on it, on its class
    and in the file's `pytestmark`, and the autouse fixtures of its class,
    its file and CONFTEST's tree."""
    names = set(_parameters(case)) - {"self"} - _parametrized(case)
    names |= _used(case.decorator_list)
    scopes = [tree.body] + ([cls.body] if cls is not None else [])
    if conftest is not None:
        scopes.append(conftest.body)
    if cls is not None:
        names |= _used(cls.decorator_list)
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "pytestmark" for t in node.targets
        ):
            names |= _used([node.value])
    for body in scopes:
        names |= {n for n, (_d, auto) in _fixtures(body).items() if auto}
    return names


def _resolver(label, tree, cls, conftest):
    """A function from a fixture name to its definition's form
    (`_moved_form`), the fixtures it requests, and where it stands, `(label,
    class or None, definition)`, read in CASE's class, then its file LABEL,
    then CONFTEST's tree, labelled `conftest`; None where none of them
    defines it, which is a fixture pytest itself provides."""
    scopes = ([(label, cls)] if cls is not None else []) + [(label, None)]
    if conftest is not None:
        scopes.append((CONFTEST_MODULE, None))
    trees = {label: tree, CONFTEST_MODULE: conftest}
    tables = [
        (where, owner, _fixtures((owner or trees[where]).body))
        for where, owner in scopes
    ]

    def resolve(name):
        for where, owner, table in tables:
            if name in table:
                node = table[name][0]
                requests = set(_parameters(node)) - {"request"}
                return _moved_form(node), requests, (where, owner, node)
        return None

    return resolve


def _reached(resolve, names):
    """Where each fixture under NAMES stands, `(label, class or None,
    definition)`, followed through the fixtures each requests as RESOLVE
    reads them; a name RESOLVE does not define is pytest's and left out."""
    found, seen, todo = [], set(), sorted(names)
    while todo:
        name = todo.pop(0)
        if name in seen:
            continue
        seen.add(name)
        hit = resolve(name)
        if hit is not None:
            found.append(hit[2])
            todo += sorted(hit[1] - seen)
    return found


def _alias_name(alias):
    return (alias.asname or alias.name).split(".")[0]


def _binds(statement):
    """The names STATEMENT stores, defines or imports in the scope it stands
    in. A compound statement stands for every name bound inside it; a
    function or class binds its own name, and what it stores for itself is
    its own."""
    names, todo = set(), [statement]
    while todo:
        inner = todo.pop()
        if isinstance(inner, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names.add(inner.name)
            continue
        if isinstance(inner, ast.Name) and not isinstance(inner.ctx, ast.Load):
            names.add(inner.id)
        elif isinstance(inner, (ast.Import, ast.ImportFrom)):
            names |= {_alias_name(a) for a in inner.names}
        todo += ast.iter_child_nodes(inner)
    return names


def _form(statement, name):
    """How STATEMENT, which binds NAME, is compared: an import as the one
    alias that binds NAME, its module, the name taken and the relative
    level; a function or class as a case's body is (`_moved_form`); any
    other statement as written."""
    if isinstance(statement, (ast.Import, ast.ImportFrom)):
        alias = next(a for a in statement.names if _alias_name(a) == name)
        return repr(
            (
                getattr(statement, "module", None),
                alias.name,
                getattr(statement, "level", None),
            )
        )
    if isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return _moved_form(statement)
    return ast.dump(statement)


class _Names:
    """One tree's side of the name condition. TREES is `{label: tree}` for
    the old or new files under their paths and for every module directly
    under `tests/`, test files among them, under its import name, which
    MODULES lists."""

    def __init__(self, trees, modules):
        self.trees, self.modules = trees, modules
        self._binders, self._reads = {}, {}

    def binders(self, body):
        """`{name: [statement, ...]}` for the statements of BODY, in order."""
        if id(body) not in self._binders:
            found = {}
            for statement in body:
                for name in sorted(_binds(statement)):
                    found.setdefault(name, []).append(statement)
            self._binders[id(body)] = found
        return self._binders[id(body)]

    def reads(self, node):
        """`(names, attributes, own)`: the names NODE reads from the module
        around it, as Python's own scoping (`symtable`) resolves them, each
        `(name, attribute)` it reads as `name.attribute`, and each attribute
        it reads of its own `self`, outside a function or lambda it defines
        that takes a `self` of its own."""
        if id(node) not in self._reads:
            table = symtable.symtable(ast.unparse(node), "<moved>", "exec")
            names = {s.get_name() for s in table.get_symbols() if s.is_referenced()}
            todo = list(table.get_children())
            while todo:
                child = todo.pop()
                todo += child.get_children()
                names |= {
                    s.get_name()
                    for s in child.get_symbols()
                    if s.is_referenced() and s.is_global()
                }
            attributes = {
                (inner.value.id, inner.attr)
                for inner in ast.walk(node)
                if isinstance(inner, ast.Attribute)
                and isinstance(inner.value, ast.Name)
            }
            own, below = set(), list(ast.iter_child_nodes(node))
            while below:
                inner = below.pop()
                if isinstance(
                    inner, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)
                ) and "self" in _parameters(inner):
                    continue
                if (
                    isinstance(inner, ast.Attribute)
                    and isinstance(inner.value, ast.Name)
                    and inner.value.id == "self"
                ):
                    own.add(inner.attr)
                below += ast.iter_child_nodes(inner)
            self._reads[id(node)] = names, attributes, own
        return self._reads[id(node)]

    def items(self, label, cls, node):
        """What NODE, standing in the file or module LABEL and in CLS where it
        is a method, reads, as `(label, class or None, key, name)`: a name
        looked up in LABEL; `self.<name>` looked up in CLS; and
        `<module>.<name>`, where `import <module>` binds a module directly
        under `tests/`, looked up in that module."""
        names, attributes, own = self.reads(node)
        found = [(label, None, name, name) for name in sorted(names)]
        if cls is not None:
            found += [(label, cls, f"self.{name}", name) for name in sorted(own)]
        binders = self.binders(self.trees[label].body)
        for owner, attribute in sorted(attributes):
            if owner in names:
                found += [
                    (alias.name, None, f"{owner}.{attribute}", attribute)
                    for statement in binders.get(owner, [])
                    if isinstance(statement, ast.Import)
                    for alias in statement.names
                    if _alias_name(alias) == owner and alias.name in self.modules
                ]
        return found

    def forms(self, todo):
        """`{key: [form, ...]}` for each definition TODO's items reach, the
        distinct forms in order, so one definition reached from two places
        counts once; an item whose name nothing binds records no form. A
        definition's own reads join TODO, so a name reached through a helper
        is compared itself, and a name imported by `from <module> import`
        from a module directly under `tests/` is read where that module
        defines it."""
        found, seen = {}, set()
        while todo:
            label, cls, key, name = todo.pop(0)
            if (label, id(cls), key, name) in seen:
                continue
            seen.add((label, id(cls), key, name))
            forms = found.setdefault(key, [])
            body = cls.body if cls is not None else self.trees[label].body
            for statement in self.binders(body).get(name, []):
                if (
                    isinstance(statement, ast.ImportFrom)
                    and not statement.level
                    and statement.module in self.modules
                    and statement.module != label
                ):
                    alias = next(a for a in statement.names if _alias_name(a) == name)
                    todo.append((statement.module, None, key, alias.name))
                    continue
                forms.append(_form(statement, name))
                todo += self.items(label, cls, statement)
        return {key: sorted(set(forms)) for key, forms in found.items()}


def _name_change(before, after):
    """Every key whose definitions BEFORE and AFTER, `{key: forms}`, read
    apart where both reached it, then every key one side reached and the
    other did not, each run in alphabetical order; an empty list where every
    one reads alike."""
    apart = sorted(k for k in before.keys() & after.keys() if before[k] != after[k])
    return apart + sorted(before.keys() ^ after.keys())


def _fixture_change(old, new, names):
    """The first fixture under NAMES, followed through the fixtures each
    requests, whose definition the two resolvers OLD and NEW read apart, as
    `(name, what)`; None where every one reads alike."""
    seen, todo = set(), sorted(names)
    while todo:
        name = todo.pop(0)
        if name in seen:
            continue
        seen.add(name)
        before, after = old(name), new(name)
        if before is None and after is None:
            continue
        if before is None:
            return name, "defined in the working tree only"
        if after is None:
            return name, "defined at the base only"
        if before[0] != after[0]:
            return name, "its definition differs from the base's"
        todo += sorted(before[1] - seen)
    return None


def moved(old, new, old_modules=None, new_modules=None):
    """One line for each old case the new files do not hold as it was, and
    one for each case of the new files that stands for no old case.

    OLD is `{path: source}` of the old files at the base, NEW `{path:
    source}` of the new files in the working tree, and the two module maps
    are `{import name: source}` of the modules directly under `tests/` in
    each tree, test files and `conftest` among them where they are
    present. An old case holds where a case of the new files has its form
    (`_moved_form`), each new case standing for one old case, where the two
    cases request the same fixtures (`_requested`), where every fixture
    requested reads alike in both trees (`_fixture_change`), and where every
    name the case and those fixtures read from the module around them is
    defined alike in both trees (`_Names`, `_name_change`). The files on
    each side are read in path order, so an old case whose form two new
    cases have is held by the first and the second is named. The count of
    collected items is `main`'s, which runs pytest."""
    sides = []
    for files, modules in ((old, old_modules or {}), (new, new_modules or {})):
        trees = {rel: ast.parse(source) for rel, source in {**files, **modules}.items()}
        sides.append(_Names(trees, set(modules)))
    before_side, after_side = sides
    old_conf = before_side.trees.get(CONFTEST_MODULE)
    new_conf = after_side.trees.get(CONFTEST_MODULE)
    standing = {}
    for new_rel in sorted(new):
        new_tree = after_side.trees[new_rel]
        for name, cls, case in _all_cases(new_tree):
            standing.setdefault(_moved_form(case), []).append(
                (f"{new_rel}::{name}", new_rel, cls, case)
            )
    lines = []
    for rel in sorted(old):
        tree = before_side.trees[rel]
        for name, cls, case in _all_cases(tree):
            where = f"moved: {rel}::{name}"
            match = standing.get(_moved_form(case))
            if not match:
                lines.append(f"{where}: body: not in the new files unchanged")
                continue
            _place, new_rel, new_cls, new_case = match.pop(0)
            new_tree = after_side.trees[new_rel]
            before = _requested(tree, cls, case, old_conf)
            after = _requested(new_tree, new_cls, new_case, new_conf)
            apart = sorted(before ^ after)
            if apart:
                side = "at the base" if apart[0] in before else "in the working tree"
                lines.append(f"{where}: fixture {apart[0]}: requested {side} only")
                continue
            old_resolve = _resolver(rel, tree, cls, old_conf)
            new_resolve = _resolver(new_rel, new_tree, new_cls, new_conf)
            change = _fixture_change(old_resolve, new_resolve, before)
            if change:
                lines.append(f"{where}: fixture {change[0]}: {change[1]}")
                continue
            reached = []
            for side, label, owner, node, resolve in (
                (before_side, rel, cls, case, old_resolve),
                (after_side, new_rel, new_cls, new_case, new_resolve),
            ):
                todo = side.items(label, owner, node)
                for at, at_class, fixture in _reached(resolve, before):
                    todo += side.items(at, at_class, fixture)
                reached.append(side.forms(todo))
            names = _name_change(*reached)
            if len(names) == 1:
                lines.append(
                    f"{where}: name {names[0]}: its definition differs from the base's"
                )
            elif names:
                lines.append(
                    f"{where}: names {', '.join(names)}: their definitions differ "
                    "from the base's"
                )
    for left in standing.values():
        lines += [
            f"moved: {place}: body: stands for no old case" for place, *_rest in left
        ]
    return lines


class Unreadable(Exception):
    """The base, a file or the collection cannot be read; `main` exits 2."""


def _interpreter(root):
    """An interpreter that can run pytest: this one where it can, else the
    repository's `.venv`, which `bin/test` builds."""
    if importlib.util.find_spec("pytest") is not None:
        return sys.executable
    for venv in (("bin", "python"), ("Scripts", "python.exe")):
        candidate = os.path.join(root, ".venv", *venv)
        if os.path.exists(candidate):
            return candidate
    raise Unreadable("no interpreter with pytest; run bin/test once to build .venv")


def _collected(python, root, paths):
    """How many items pytest collects from PATHS under ROOT, leaving out the
    census case each module file assigns."""
    env = {
        k: v
        for k, v in os.environ.items()
        if k not in ("PYTEST_ADDOPTS", "PYTEST_PLUGINS")
    }
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    quiet = ["--collect-only", "-q", "-p", "no:xdist", "-p", "no:cacheprovider"]
    run = subprocess.run(
        [python, "-m", "pytest", *quiet, *paths],
        cwd=root,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        env=env,
        stdin=subprocess.DEVNULL,
    )
    if run.returncode != 0:
        # exempt from splitlines: pytest's own output
        tail = (run.stdout + run.stderr).strip().splitlines()[-1:]
        raise Unreadable(
            f"pytest cannot collect {' '.join(paths)} under {root}: {tail}"
        )
    items = []
    # exempt from splitlines: pytest's own output
    for line in run.stdout.splitlines():
        if not line.strip():
            break
        items.append(line.strip())
    return sum(1 for item in items if item.rsplit("::", 1)[-1] != "test_census")


def _git(root, *args):
    return subprocess.run(
        ["git", "-C", root, *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


def _test_modules(paths, read):
    """`{import name: source}` for each of PATHS, `tests/<entry>` for each
    entry directly under `tests/`, that is a module, a test file among them,
    its source as READ gives it. pytest imports a test file directly under
    `tests/` under its file name, so `from test_x import` in another file
    reads that file's definition."""
    found = {}
    for path in sorted(paths):
        name = posixpath.basename(path)
        if name.endswith(".py"):
            source = read(path)
            if source is not None:
                found[name[: -len(".py")]] = source
    return found


def _moved_main(root, base, olds, news):
    """`--moved`: the exit code, having printed each failure and a last
    line."""
    sha = _git(root, "rev-parse", "--verify", "--quiet", f"{base}^{{commit}}")
    if sha.returncode != 0:
        raise Unreadable(f"{base} names no commit")
    sha = sha.stdout.strip()

    def rel(path):
        return os.path.relpath(os.path.abspath(path), root).replace(os.sep, "/")

    old_rels, new_rels = [rel(p) for p in olds], [rel(p) for p in news]
    old = {}
    for path in old_rels:
        shown = _git(root, "show", f"{sha}:{path}")
        if shown.returncode != 0:
            raise Unreadable(f"{path} is not a file at {sha[:12]}")
        old[path] = shown.stdout
    new = {}
    for path in new_rels:
        new[path] = _read(root, path)
        if new[path] is None:
            raise Unreadable(f"{path} cannot be read")

    def shown_at_base(path):
        shown = _git(root, "show", f"{sha}:{path}")
        return shown.stdout if shown.returncode == 0 else None

    listed = _git(root, "ls-tree", "--name-only", sha, TESTS).stdout.split("\n")
    here = os.path.join(root, TESTS)
    present = os.listdir(here) if os.path.isdir(here) else []
    lines = moved(
        old,
        new,
        _test_modules(listed, shown_at_base),
        _test_modules([TESTS + name for name in present], lambda p: _read(root, p)),
    )
    python = _interpreter(root)
    holder = tempfile.mkdtemp(prefix="test-layout-moved-")
    tree = os.path.join(holder, "base")
    try:
        added = _git(root, "worktree", "add", "--detach", "--quiet", tree, sha)
        if added.returncode != 0:
            raise Unreadable(f"git cannot check out {sha[:12]}: {added.stderr.strip()}")
        before = _collected(python, tree, old_rels)
    finally:
        # This worktree alone, by its path: a prune would drop every other
        # worktree's record whose directory is missing too.
        _git(root, "worktree", "remove", "--force", tree)
        shutil.rmtree(holder, ignore_errors=True)
    after = _collected(python, root, new_rels)
    if after != before:
        lines.insert(
            0,
            f"moved: count: the new files collect {after} items, the old files "
            f"{before} at the base",
        )
    for line in lines:
        print(line)
    cases = sum(len(_all_cases(ast.parse(source))) for source in old.values())
    print(
        f"test-layout: moved: {cases} old cases, {after} items against {before} "
        f"at {sha[:12]}, {len(lines)} failed",
        flush=True,
    )
    return 1 if lines else 0


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
    mode.add_argument(
        "--moved",
        metavar="BASE",
        help="whether the new files hold the old files' cases at BASE, only moved",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="with --check, refuse a file that declares no TARGET",
    )
    parser.add_argument(
        "--from",
        dest="olds",
        nargs="+",
        metavar="OLD",
        help="with --moved, the old test files at BASE",
    )
    parser.add_argument(
        "--to",
        dest="news",
        nargs="+",
        metavar="NEW",
        help="with --moved, the new test files in the working tree",
    )
    parser.add_argument(
        "paths", nargs="*", help="files or directories; tests/ when none"
    )
    args = parser.parse_args(argv)
    if args.all and not args.check:
        parser.error("--all goes with --check")
    if (args.olds or args.news) and args.moved is None:
        parser.error("--from and --to go with --moved")
    if args.moved is not None:
        # Each path's list is told by the word before it, so a path in
        # neither list is refused rather than counted into one.
        if not args.olds or not args.news or args.paths:
            parser.error(
                "--moved takes the old files after --from and the new files "
                "after --to, and no other path"
            )
        start = os.path.dirname(os.path.abspath(args.news[0]))
        root = _toplevel(start)
        if root is None:
            print(f"test-layout: {start} is not inside a git repository", flush=True)
            return 2
        try:
            return _moved_main(root, args.moved, args.olds, args.news)
        except Unreadable as exc:
            print(f"test-layout: {exc}", flush=True)
            return 2
    first = args.paths[0] if args.paths else os.getcwd()
    start = first if os.path.isdir(first) else os.path.dirname(os.path.abspath(first))
    root = _toplevel(start)
    if root is None:
        print(f"test-layout: {start} is not inside a git repository", flush=True)
        return 2
    missing = [path for path in args.paths if not os.path.exists(path)]
    if missing:
        print(
            f"test-layout: {', '.join(missing)} names no file or directory",
            flush=True,
        )
        return 2
    tests = _read_tests(root, args.paths or [os.path.join(root, "tests")])
    if args.pairs:
        lines = pairs(tests)
        for line in lines:
            print(line)
        print(f"test-layout: {len(tests)} files read, {len(lines)} pairs", flush=True)
        return 0
    # Helpers are compared over every test file and `tests/conftest.py`,
    # whatever the paths name; the paths choose the files judged.
    peers = _read_tests(root, [os.path.join(root, "tests")])
    shared = _read(root, "tests/conftest.py")
    if shared is not None:
        peers["tests/conftest.py"] = shared
    refused, reported = check(
        tests,
        _tracked(root),
        lambda rel: _read(root, rel),
        every=args.all,
        peers=peers,
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
