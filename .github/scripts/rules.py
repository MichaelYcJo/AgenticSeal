#!/usr/bin/env python3
"""rules — a document's sections with what their tests guard, or every target checked.

  rules <doc>               every heading of DOC, and under each the targets
                            of its `Enforced by:` lines, each with the first
                            sentence of its docstring, resolved in the
                            repository the current directory is in
  rules --check             every `Enforced by:` target in every rule file
                            resolved, each one that does not named
  rules ... --root DIR      resolve in DIR instead

A rule's text lives once, as the first sentence of the docstring of the test
that holds it, and a document lists its tests by `Enforced by:`. `rules <doc>`
prints the two together so the whole picture reads without a second copy:
nothing is written, committed or generated, because a committed copy would be
a second source and a file every branch rewrites.

`rules --check` reads every rule file `RULE_FILES` names and every `Enforced
by:` line a renderer shows in it, inside a rule paragraph or not, and resolves
each target. A target is a file, a `path::name` unit its Python file defines
once (`skills/settle/scripts/fold_check.py#target_problem`, the one resolver),
or an eval case directory, `evals/behaviour/<agent>/<case>/`, which resolves
where it holds `case.yaml`. `nothing — <why>` names no target. One suite case
runs it over the tree, so it is read wherever the suite runs.

**How it errs:** it cannot tell a test that exists from one that asserts the
rule, and a rule written with no `Enforced by:` line is read by nobody.

Exit codes: `rules <doc>` **0** the document was read, whatever its targets
are · `rules --check` **0** every target resolves · **1** a target does not
resolve, each named as `path:line §*heading*: why` · **2** for either: a file
it had to read cannot be read, a module it reads through is not in the tree,
or neither or both of DOC and `--check` were given.
"""

import argparse
import ast
import glob
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SENTENCE = re.compile(r"(.+?[.!?])(?:\s|$)")
DEFINITIONS = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
RULE_CLOSER = "Enforced by:"
# Where a rule is stated, and so where an `Enforced by:` line is read.
RULE_FILES = (
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "agents/*.md",
    "docs/*.md",
    "skills/*/SKILL.md",
    "skills/*/orchestration.md",
    "templates/*.md",
)
# The one target `fold_check.py#target_problem` does not read: an eval case,
# `evals/behaviour/<agent>/<case>/`, which resolves where this file is in it.
EVAL_CASES = "evals/behaviour/"
EVAL_CASE = "case.yaml"

# The modules this reads through, each the one reader of its input: the GFM
# line walker, the fence and comment rule, and the resolver of a target.
SIBLINGS = {
    "unverified_check": (
        os.path.join("skills", "verify", "scripts", "unverified_check.py"),
        "it is what splits a document into the lines GitHub renders",
    ),
    "config": (
        os.path.join("hooks", "config.py"),
        "it is what says which lines a fence or a comment hides",
    ),
    "fold_check": (
        os.path.join("skills", "settle", "scripts", "fold_check.py"),
        "it is the one resolver of an `Enforced by:` target",
    ),
}


class Unreadable(Exception):
    """Nothing could be read, and the sentence says why."""


_loaded = {}


def sibling(key):
    """The module `SIBLINGS[key]` names, loaded by path once, or Unreadable."""
    if key in _loaded:
        return _loaded[key]
    rel, purpose = SIBLINGS[key]
    path = os.path.join(ROOT, rel)
    if not os.path.isfile(path):
        raise Unreadable(f"cannot read {rel}, and {purpose}")
    spec = importlib.util.spec_from_file_location(f"specseal_rules_{key}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    _loaded[key] = module
    return module


def shown_lines(text):
    """`[(line, shown, heading)]` for one markdown document: each GFM line
    (`unverified_check.py#gfm_lines`), whether a renderer shows it outside a
    fence or a comment (`hooks/config.py#unfenced`), and the text of the
    heading it stands under, "" above the first."""
    reader = sibling("unverified_check")
    lines = reader.gfm_lines(text)
    shown = {index for index, _ in sibling("config").unfenced(lines)}
    out, heading = [], ""
    for index, line in enumerate(lines):
        visible = index in shown
        if visible and reader.heading_level(line) is not None:
            heading = line.strip().strip("#").strip()
        out.append((line, visible, heading))
    return out


def enforcer_lines(text):
    """`[(line number, heading, value)]` for every `Enforced by:` line one
    markdown document shows, inside a rule paragraph or not."""
    return [
        (index + 1, heading, line.strip()[len(RULE_CLOSER) :].strip())
        for index, (line, visible, heading) in enumerate(shown_lines(text))
        if visible and line.strip().startswith(RULE_CLOSER)
    ]


def rule_files(root):
    """`{path: text}` of every rule file in the tree at `root`, by
    `RULE_FILES`, its path written with `/`."""
    out = {}
    for pattern in RULE_FILES:
        for path in sorted(glob.glob(os.path.join(root, *pattern.split("/")))):
            if os.path.isfile(path):
                rel = os.path.relpath(path, root).replace(os.sep, "/")
                with open(path, encoding="utf-8", errors="replace") as handle:
                    out[rel] = handle.read()
    return out


def targets_of(value):
    """The targets an `Enforced by:` value names, none where it says
    `nothing — <why>` — read by `fold_check.py#names_targets`, so `rules` and
    `fold-check` split one line alike."""
    if not sibling("fold_check").names_targets(value):
        return []
    return value.split(",")


def target_problem(root, target):
    """Why one `Enforced by:` target does not resolve in the tree at `root`,
    or None where it does. An eval case directory, `evals/behaviour/<agent>/
    <case>/` with its slash, resolves where it holds `case.yaml`; every other
    target is `fold_check.py#target_problem`'s, and a Python file it cannot
    parse is Unreadable."""
    cell = target.strip().strip("`")
    if cell.startswith(EVAL_CASES) and cell.endswith("/"):
        parts = cell[len(EVAL_CASES) : -1].split("/")
        if len(parts) < 2 or not all(parts):
            return f"{cell} is no eval case: write `{EVAL_CASES}<agent>/<case>/`"
        base = os.path.realpath(root)
        full = os.path.realpath(os.path.join(base, *cell[:-1].split("/")))
        if os.path.commonpath([full, base]) != base:
            return f"{cell} is not a path inside the repository"
        if not os.path.isfile(os.path.join(full, EVAL_CASE)):
            return f"{cell} holds no {EVAL_CASE}"
        return None
    fold_check = sibling("fold_check")
    try:
        return fold_check.target_problem(root, cell)
    except fold_check.Unusable as error:
        raise Unreadable(f"a target {error}") from None


def unresolved(root):
    """`(failures, files, targets)`: each `Enforced by:` target in the rule
    files at `root` that does not resolve, as `path:line §*heading*: why`,
    and how many rule files and targets were read."""
    found, read, files = [], 0, rule_files(root)
    for path, text in files.items():
        for number, heading, value in enforcer_lines(text):
            for target in targets_of(value):
                read += 1
                problem = target_problem(root, target)
                if problem:
                    found.append(f"{path}:{number} §*{heading}*: {problem}")
    return found, len(files), read


def check(root):
    """Print each target that does not resolve and the count read; the exit
    code is the verdict."""
    found, files, targets = unresolved(root)
    for failure in found:
        print(f"rules: {failure}")
    if found:
        print(
            f"rules: {len(found)} of {targets} `Enforced by:` targets in "
            f"{files} rule files do not resolve."
        )
        return 1
    print(f"rules: all {targets} `Enforced by:` targets in {files} rule files resolve.")
    return 0


def first_sentence(doc):
    """The first sentence of a docstring's first paragraph, its whitespace
    folded, or the whole paragraph where it holds no sentence end."""
    paragraph = " ".join(doc.strip().split("\n\n", 1)[0].split())
    found = SENTENCE.match(paragraph)
    return found.group(1) if found else paragraph


def docstring(root, target):
    """The docstring a resolved target carries: a `path::name` unit's, a
    Python file's module docstring, or None where it has none or is no
    Python.

    The unit is the one the resolver found. `coordinates.py#py_spans` walks
    the file as `coordinates.py#named_unit` does, into an `if`, a `try` or a
    `with` and never into another `def`, so its one span for the name is the
    unit `target_problem` accepted, and the definition read is the one that
    starts and ends there."""
    path, _, name = target.strip().strip("`").partition("::")
    if not path.endswith(".py"):
        return None
    with open(os.path.join(root, *path.split("/")), encoding="utf-8") as handle:
        text = handle.read()
    tree = ast.parse(text)
    if not name:
        return ast.get_docstring(tree)
    kernel = sibling("fold_check").coordinates()
    places = (kernel.py_spans(text) or {}).get(".".join(name.split("::")), [])
    if len(places) != 1:
        return None
    for node in ast.walk(tree):
        if (
            isinstance(node, DEFINITIONS)
            and (
                min([node.lineno] + [d.lineno for d in node.decorator_list]),
                node.end_lineno,
            )
            == places[0]
        ):
            return ast.get_docstring(node)
    return None


def describe(root, target):
    """One printed line for one target: what its docstring says it guards,
    or why it says nothing."""
    cell = target.strip().strip("`")
    try:
        problem = target_problem(root, cell)
    except Unreadable as error:
        return f"{cell} — does not resolve: {error}"
    if problem:
        return f"{cell} — does not resolve: {problem}"
    if cell.startswith(EVAL_CASES):
        return f"{cell} — an eval case"
    try:
        doc = docstring(root, cell)
    except (OSError, ValueError, SyntaxError):
        return f"{cell} — (cannot be read as Python)"
    return f"{cell} — {first_sentence(doc) if doc else '(no docstring)'}"


def render(root, text):
    """The printed walk of one document: each heading, and under it each
    `Enforced by:` line's targets described, or a line saying it has none."""
    out, heading, held = [], None, False
    for number, (line, visible, _) in enumerate(shown_lines(text), 1):
        stripped = line.strip()
        level = sibling("unverified_check").heading_level(line)
        if visible and level is not None:
            if heading is not None and not held:
                out.append("  (no `Enforced by:` line)")
            out += ["", stripped]
            heading, held = stripped, False
            continue
        if not visible or not stripped.startswith(RULE_CLOSER):
            continue
        held = True
        value = stripped[len(RULE_CLOSER) :].strip()
        targets = targets_of(value)
        out.append(f"  Enforced by, line {number}:")
        if not targets:
            out.append(f"    {value}")
        out += [f"    {describe(root, target)}" for target in targets]
    if heading is not None and not held:
        out.append("  (no `Enforced by:` line)")
    return "\n".join(out).lstrip("\n") + "\n"


def main(argv=None):
    """Read DOC and print its walk, or check every rule file with `--check`;
    the exit code says which, as the module docstring lists."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("doc", nargs="?")
    parser.add_argument(
        "--check",
        action="store_true",
        help="resolve every `Enforced by:` target in every rule file",
    )
    parser.add_argument(
        "--root", default=None, help="the repository to resolve in (default: cwd)"
    )
    args = parser.parse_args(argv)
    if args.check == (args.doc is not None):
        sys.stderr.write("rules: name a document, or --check, and not both.\n")
        return 2
    root = os.path.abspath(args.root or os.getcwd())
    try:
        if args.root is None:
            # Typed anywhere inside a repository, the command reads that
            # repository, as `fold-check` does. `bin/` is on a user's PATH,
            # and the tree this script ships in is the plugin's, not theirs.
            root = sibling("fold_check").optin().repo_root(root) or root
        if args.check:
            return check(root)
        path = args.doc
        if not os.path.isabs(path):
            path = os.path.join(os.getcwd(), path)
        if not os.path.isfile(path):
            path = os.path.join(root, args.doc)
        try:
            with open(path, encoding="utf-8") as handle:
                text = handle.read()
        except (OSError, UnicodeDecodeError) as error:
            sys.stderr.write(f"rules: cannot read {args.doc}: {error}.\n")
            return 2
        sys.stdout.write(render(root, text))
    except Unreadable as error:
        sys.stderr.write(f"rules: {error}.\n")
        return 2
    return 0


if __name__ == "__main__":
    for _name in ("stdout", "stderr"):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
