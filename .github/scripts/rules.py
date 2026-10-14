#!/usr/bin/env python3
"""rules — a document's sections, each with what its tests say they guard.

  rules <doc>              every heading of DOC, and under each the targets
                           of its `Enforced by:` lines, each with the first
                           sentence of its docstring, resolved in the
                           repository the current directory is in
  rules <doc> --root DIR   resolve the targets in DIR instead

A rule's text lives once, as the first sentence of the docstring of the test
that holds it, and a document lists its tests by `Enforced by:`. This prints
the two together so the whole picture reads without a second copy: nothing
is written, committed or generated, because a committed copy would be a
second source and a file every branch rewrites.

A target is resolved by `.github/scripts/budget_check.py#target_problem`, the
resolver the `enforced-unresolved` budget row reads with. A `path::name`
target prints its function's or class's docstring, a Python file its
module's; a target that does not resolve prints why, and one with no
docstring says so. An eval case directory prints that it is one.

Exit codes: **0** the document was read, whatever its targets are — the
budget row is what fails · **2** DOC cannot be read, or the checker this
reads through is not beside it.
"""

import argparse
import ast
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKER = os.path.join(HERE, "budget_check.py")
SENTENCE = re.compile(r"(.+?[.!?])(?:\s|$)")


def checker():
    """`budget_check.py`, loaded by path, or None where it is not beside this.

    Reads: owned — a module this repository ships beside this script; unknown refused"""
    if not os.path.isfile(CHECKER):
        return None
    spec = importlib.util.spec_from_file_location("specseal_rules_budget", CHECKER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def first_sentence(doc):
    """The first sentence of a docstring's first paragraph, its whitespace
    folded, or the whole paragraph where it holds no sentence end.

    Reads: guess — a docstring a person wrote, handed by its caller; unknown passed"""
    paragraph = " ".join(doc.strip().split("\n\n", 1)[0].split())
    found = SENTENCE.match(paragraph)
    return found.group(1) if found else paragraph


def docstring(root, target):
    """The docstring a resolved target carries: a `path::name` unit's, a
    Python file's module docstring, or None where it has none or is no
    Python.

    Reads: observed — the Python file the target names, parsed; unknown passed"""
    path, _, name = target.strip().strip("`").partition("::")
    if not path.endswith(".py"):
        return None
    with open(os.path.join(root, *path.split("/")), encoding="utf-8") as handle:
        node = ast.parse(handle.read())
    for part in name.split("::") if name else []:
        node = next(
            child
            for child in node.body
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
            and child.name == part
        )
    return ast.get_docstring(node)


def describe(budget, root, target):
    """One printed line for one target: what its docstring says it guards,
    or why it says nothing.

    Reads: observed — the tree at `root`, through `budget_check.py#target_problem` and `docstring`; unknown passed"""
    cell = target.strip().strip("`")
    try:
        problem = budget.target_problem(root, cell)
    except budget.Unreadable as error:
        return f"{cell} — does not resolve: {error}"
    if problem:
        return f"{cell} — does not resolve: {problem}"
    if cell.startswith(budget.EVAL_CASES):
        return f"{cell} — an eval case"
    try:
        doc = docstring(root, cell)
    except (OSError, ValueError, SyntaxError):
        return f"{cell} — (cannot be read as Python)"
    return f"{cell} — {first_sentence(doc) if doc else '(no docstring)'}"


def render(budget, root, text):
    """The printed walk of one document: each heading, and under it each
    `Enforced by:` line's targets described, or a line saying it has none.

    Reads: guess — a person's markdown, through `budget_check.py#shown_lines`; unknown passed"""
    out, heading, held = [], None, False
    for number, (line, visible, _) in enumerate(budget.shown_lines(text), 1):
        stripped = line.strip()
        level = budget.sibling("unverified_check").heading_level(line)
        if visible and level is not None:
            if heading is not None and not held:
                out.append("  (no `Enforced by:` line)")
            out += ["", stripped]
            heading, held = stripped, False
            continue
        if not visible or not stripped.startswith(budget.RULE_CLOSER):
            continue
        held = True
        value = stripped[len(budget.RULE_CLOSER) :].strip()
        targets = budget.targets_of(value)
        out.append(f"  Enforced by, line {number}:")
        if not targets:
            out.append(f"    {value}")
        out += [f"    {describe(budget, root, target)}" for target in targets]
    if heading is not None and not held:
        out.append("  (no `Enforced by:` line)")
    return "\n".join(out).lstrip("\n") + "\n"


def main(argv=None):
    """Read DOC, print its walk; the exit code says only whether it was read.

    Reads: guess — the arguments and the document they name; unknown refused"""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("doc")
    parser.add_argument(
        "--root", default=None, help="the repository to resolve in (default: cwd)"
    )
    args = parser.parse_args(argv)
    budget = checker()
    if budget is None:
        sys.stderr.write("rules: budget_check.py is not beside this script.\n")
        return 2
    root = os.path.abspath(args.root or os.getcwd())
    if args.root is None:
        # Typed anywhere inside a repository, the command reads that
        # repository, as `fold-check` does. `bin/` is on a user's PATH, and
        # the tree this script ships in is the plugin's, not theirs.
        try:
            root = budget.sibling("fold_check").optin().repo_root(root) or root
        except budget.Unreadable as error:
            sys.stderr.write(f"rules: {error}.\n")
            return 2
    path = args.doc if os.path.isabs(args.doc) else os.path.join(os.getcwd(), args.doc)
    if not os.path.isfile(path):
        path = os.path.join(root, args.doc)
    try:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
    except (OSError, UnicodeDecodeError) as error:
        sys.stderr.write(f"rules: cannot read {args.doc}: {error}.\n")
        return 2
    try:
        sys.stdout.write(render(budget, root, text))
    except budget.Unreadable as error:
        sys.stderr.write(f"rules: {error}.\n")
        return 2
    return 0


if __name__ == "__main__":
    for _name in ("stdout", "stderr"):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
