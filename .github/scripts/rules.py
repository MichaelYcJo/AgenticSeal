#!/usr/bin/env python3
"""seal rules: a document's sections with what their tests guard, or every check line read.

  seal rules <doc>          every heading of DOC, and under each the targets
                            of its `check:` lines, each with the first
                            sentence of its docstring, resolved in the
                            repository the current directory is in
  seal rules --check        every `check:` line in every rule file read, and
                            each one that is out of grammar or names a target
                            that does not resolve named
  seal rules ... --root DIR resolve in DIR instead

A rule's text lives once, as the first sentence of the docstring of the test
that holds it, and a rule file lists its tests by `check:` line. `seal rules <doc>`
prints the two together so the whole picture reads without a second copy:
nothing is written, committed or generated, because a committed copy would be
a second source and a file every branch rewrites.

The grammar of the line is `skills/settle/SKILL.md` *A rule has one shape*,
and this module is its one reader. `seal rules --check` reads every rule file
`RULE_FILES` names and every line a renderer shows in it, inside a rule
paragraph or not. One suite case runs it over the tree, so it is read wherever
the suite runs.

**How it errs:** it cannot tell a test that exists from one that asserts the
rule, and a rule written with no `check:` line is read by nobody.

`seal rules --check` excuses one shape of a pending rule change: a refused
line inside a section that an unsettled design's `remove` with no `from`
takes out at the settle is printed as `seal rules: excused: path:line:
heading: why; <work item> removes this section at the settle`, and is no
refusal. The designs are read through
`skills/settle/scripts/rule_changes.py#pending`, under `<root>/seal/threads/`.
A pending `change`, or a `remove` with a `from`, whose `from` holds the line
excuses nothing, so the test the line names stays until the settle
(`tests/github/test_gather_changelog.py`). In local mode the designs sit under
the common git directory, which a CI checkout does not hold, so no line is
excused there.

Exit codes: `seal rules <doc>` 0 the document was read, whatever its lines say.
`seal rules --check` 0 every line holds or is excused, 1 a line is refused,
each named as `seal rules: path:line: heading: why`. 2 for either: a file it had to read cannot
be read, a module it reads through is not in the tree, or neither or both of
DOC and `--check` were given.
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
# Where a rule is stated, and so where a `check:` line is read.
RULE_FILES = (
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "agents/*.md",
    "docs/*.md",
    "skills/*/SKILL.md",
    "skills/*/orchestration.md",
    "templates/*/*.md",
)
LABEL = "check: "
NO_TARGET = "none reader: "
# Markdown block markup, one mark: a heading's `#` run, a list bullet or
# number, a task box, a blockquote's `>`, a table's `|`.
BLOCK_MARK = r"(?:#|[-+*]|[0-9]{1,9}[.)]|\[[ xX]\]|>|\|)"
# What a near miss of the label looks like: the words in any case, with
# nothing before them but spaces, block markup and emphasis, before a colon
# with spaces around it. A line whose only content before `check:` is block
# markup is refused at its line; only the exact shape is read.
NEAR = re.compile(
    rf"^(?:\s|{BLOCK_MARK})*[*_]*\s*(?:checks?|enforced\s+by)\s*[*_]*\s*:",
    re.IGNORECASE,
)
REFUSED_IN_VALUE = ("::", ",", "—")
MARKER = re.compile(r"[a-z0-9-]+")
EVAL_CASES = "evals/behaviour/"
EVAL_CASE = "case.yaml"
EXPECTED = f"`{LABEL}<targets>` or `{LABEL}{NO_TARGET}<who reads it>`"

# The modules this reads through, each the one reader of its input: the GFM
# line walker, the fence and comment rule, and the resolver of the repository.
SIBLINGS = {
    "unverified_check": (
        os.path.join("skills", "verify", "scripts", "unverified_check.py"),
        "it is what splits a document into the lines GitHub renders",
    ),
    "config": (
        os.path.join("hooks", "lib", "config.py"),
        "it is what says which lines a fence or a comment hides",
    ),
    "optin": (
        os.path.join("hooks", "lib", "optin.py"),
        "it is what finds the repository the command is typed in",
    ),
    "rule_changes": (
        os.path.join("skills", "settle", "scripts", "rule_changes.py"),
        "it is what reads the rule changes the settle has not yet written",
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
    spec = importlib.util.spec_from_file_location(f"agentic_rules_{key}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    _loaded[key] = module
    return module


def shown_lines(text):
    """`[(line, shown, heading)]` for one markdown document: each GFM line
    (`hooks/lib/blocks.py#gfm_lines`), whether a renderer shows it outside a
    fence or a comment (`hooks/lib/config.py#unfenced`), and the text of the
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


def check_lines(text):
    """`[(line number, heading, line)]` for every shown line of one markdown
    document that is a `check:` line or a near miss of one, the line with its
    ends stripped."""
    return [
        (index + 1, heading, line.strip())
        for index, (line, visible, heading) in enumerate(shown_lines(text))
        if visible and NEAR.match(line)
    ]


def parse(line):
    """`(targets, reader, why)` for one stripped check line: the targets it
    names, or the reader of a no-target line, or why it is refused."""
    if not line.startswith(LABEL):
        return [], None, f"`{line}` is no check line: write {EXPECTED}"
    value = line[len(LABEL) :]
    for symbol in REFUSED_IN_VALUE:
        if symbol in value:
            return [], None, f"`{symbol}` is no part of a check line: write {EXPECTED}"
    if value == "none" or value.startswith("none "):
        reader = value[len(NO_TARGET) :]
        if not value.startswith(NO_TARGET) or not reader or reader != reader.strip():
            return (
                [],
                None,
                f"a line naming no target names its reader: write {EXPECTED}",
            )
        return [], reader, None
    targets = value.split(" ")
    if not all(targets):
        return [], None, "targets are separated by one space"
    return targets, None, None


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


def carried_by(decorator):
    """The marker name a `@pytest.mark.rule("<name>")` decorator carries, or
    None for any other decorator."""
    if not (isinstance(decorator, ast.Call) and len(decorator.args) == 1):
        return None
    func, arg = decorator.func, decorator.args[0]
    spelled = []
    while isinstance(func, ast.Attribute):
        spelled.insert(0, func.attr)
        func = func.value
    if not isinstance(func, ast.Name) or [func.id, *spelled] != [
        "pytest",
        "mark",
        "rule",
    ]:
        return None
    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
        return arg.value
    return None


_markers = {}


def markers(root):
    """`{marker: [(test file, qualified name, docstring)]}` for every test
    under `root` that carries `@pytest.mark.rule("<marker>")`, read once per
    root. A test file is a `test_*.py` outside a directory whose name starts
    with a dot; one that does not parse is Unreadable."""
    if root in _markers:
        return _markers[root]
    found = {}
    for top, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if not d.startswith("."))
        for name in sorted(files):
            if not (name.startswith("test_") and name.endswith(".py")):
                continue
            path = os.path.join(top, name)
            rel = os.path.relpath(path, root).replace(os.sep, "/")
            try:
                with open(path, encoding="utf-8") as handle:
                    text = handle.read()
                if "mark.rule(" not in text:
                    continue
                tree = ast.parse(text)
            except (OSError, ValueError, SyntaxError) as error:
                raise Unreadable(
                    f"{rel} could not be read as Python ({type(error).__name__})"
                ) from None
            for qualified, node in definitions(tree):
                for decorator in node.decorator_list:
                    marker = carried_by(decorator)
                    if marker is not None:
                        doc = ast.get_docstring(node)
                        found.setdefault(marker, []).append((rel, qualified, doc))
    _markers[root] = found
    return found


def definitions(tree, prefix=""):
    """`(qualified name, node)` for every function and class in TREE, a
    method named `Class.method`: into an `if`, a `try` or a `with`, as pytest
    collects, and never into a function's body."""
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            yield prefix + node.name, node
            if isinstance(node, ast.ClassDef):
                yield from definitions(node, f"{prefix}{node.name}.")
        elif not isinstance(node, ast.expr):
            yield from definitions(node, prefix)


def target_problem(root, target):
    """Why one target does not resolve in the tree at `root`, or None where
    it does: a marker some test carries, an eval case directory holding
    `case.yaml`, or a file inside the repository."""
    if MARKER.fullmatch(target):
        if markers(root).get(target):
            return None
        return f"no test carries the marker `{target}`"
    base = os.path.realpath(root)
    if target.startswith(EVAL_CASES) and target.endswith("/"):
        parts = target[len(EVAL_CASES) : -1].split("/")
        if len(parts) != 2 or not all(parts):
            return f"{target} is no eval case: write `{EVAL_CASES}<agent>/<case>/`"
        full = os.path.realpath(os.path.join(base, *target[:-1].split("/")))
        if os.path.commonpath([full, base]) != base:
            return f"{target} is not a path inside the repository"
        if not os.path.isfile(os.path.join(full, EVAL_CASE)):
            return f"{target} holds no {EVAL_CASE}"
        return None
    # Both sides through `realpath`, so a symlink inside the root that opens a
    # file outside it is outside, and a root reached through one is itself.
    full = os.path.realpath(os.path.join(base, *target.split("/")))
    if os.path.commonpath([full, base]) != base:
        return f"{target} is not a path inside the repository"
    if not os.path.exists(full):
        return f"{target} does not exist"
    if not os.path.isfile(full):
        return f"{target} is not a file in the repository"
    return None


def line_problems(root, line):
    """Every reason one stripped check line is refused, empty where it holds."""
    targets, _reader, why = parse(line)
    if why:
        return [why]
    return [p for p in (target_problem(root, t) for t in targets) if p]


def unresolved(root):
    """`(failures, excused, files, lines)`: each refusal in the rule files at
    `root`, as `path:line: heading: why`; each refusal of a line inside a
    section a pending `remove` takes out at the settle, the same with
    `; <work item> removes this section at the settle` after it; and how
    many rule files and check lines were read. Only that one shape of a
    pending rule change is excused; the module docstring names what is
    not."""
    found, excused, read, files = [], [], 0, rule_files(root)
    changes = sibling("rule_changes")
    policy = sibling("config").policy_root(os.path.join(root, "seal"))
    items = changes.pending(root, policy)
    for path, text in files.items():
        for number, heading, line in check_lines(text):
            read += 1
            problems = line_problems(root, line)
            item = changes.removed_by(items, path, text, number) if problems else None
            for problem in problems:
                failure = f"{path}:{number}: {heading}: {problem}"
                if item:
                    excused.append(
                        f"{failure}; {item} removes this section at the settle"
                    )
                else:
                    found.append(failure)
    return found, excused, len(files), read


def check(root):
    """Print each refusal, each excused line and the count read; the exit
    code is the verdict, and an excused line is no refusal."""
    found, excused, files, lines = unresolved(root)
    for failure in found:
        print(f"seal rules: {failure}")
    for line in excused:
        print(f"seal rules: excused: {line}")
    if found:
        print(
            f"seal rules: {len(found)} refused in {lines} check lines of {files} rule files."
        )
        return 1
    if excused:
        print(
            f"seal rules: {len(excused)} excused in {lines} check lines of {files} "
            "rule files, and every other line holds."
        )
        return 0
    print(f"seal rules: all {lines} check lines in {files} rule files hold.")
    return 0


def first_sentence(doc):
    """The first sentence of a docstring's first paragraph, its whitespace
    folded, or the whole paragraph where it holds no sentence end."""
    paragraph = " ".join(doc.strip().split("\n\n", 1)[0].split())
    found = SENTENCE.match(paragraph)
    return found.group(1) if found else paragraph


def said(doc):
    """What one docstring says it guards, in one line."""
    return first_sentence(doc) if doc else "(no docstring)"


def describe(root, target):
    """The printed lines for one target: what its docstring says it guards,
    or why it says nothing."""
    try:
        problem = target_problem(root, target)
    except Unreadable as error:
        return [f"{target}: does not resolve: {error}"]
    if problem:
        return [f"{target}: does not resolve: {problem}"]
    if MARKER.fullmatch(target):
        return [
            f"{target}: {path} {name}: {said(doc)}"
            for path, name, doc in markers(root)[target]
        ]
    if target.startswith(EVAL_CASES):
        return [f"{target}: an eval case"]
    if not target.endswith(".py"):
        return [f"{target}: (no docstring)"]
    try:
        with open(os.path.join(root, *target.split("/")), encoding="utf-8") as handle:
            doc = ast.get_docstring(ast.parse(handle.read()))
    except (OSError, ValueError, SyntaxError):
        return [f"{target}: (cannot be read as Python)"]
    return [f"{target}: {said(doc)}"]


def render(root, text):
    """The printed walk of one document: each heading, and under it each
    check line's targets described, or a line saying it has none."""
    out, heading, held = [], None, False
    by_number = {number: line for number, _, line in check_lines(text)}
    reader = sibling("unverified_check")
    for number, (line, visible, _) in enumerate(shown_lines(text), 1):
        stripped = line.strip()
        if visible and reader.heading_level(line) is not None:
            if heading is not None and not held:
                out.append("  (no check line)")
            out += ["", stripped]
            heading, held = stripped, False
            continue
        if number not in by_number:
            continue
        held = True
        targets, who, why = parse(by_number[number])
        out.append(f"  check, line {number}:")
        if why:
            out.append(f"    refused: {why}")
        elif who is not None:
            out.append(f"    no target, read by {who}")
        for target in targets:
            out += [f"    {each}" for each in describe(root, target)]
    if heading is not None and not held:
        out.append("  (no check line)")
    return "\n".join(out).lstrip("\n") + "\n"


def main(argv=None):
    """Read DOC and print its walk, or check every rule file with `--check`;
    the exit code says which, as the module docstring lists."""
    # exempt from splitlines: the docstring's first line
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("doc", nargs="?")
    parser.add_argument(
        "--check",
        action="store_true",
        help="read every `check:` line in every rule file",
    )
    parser.add_argument(
        "--root", default=None, help="the repository to resolve in (default: cwd)"
    )
    args = parser.parse_args(argv)
    if args.check == (args.doc is not None):
        sys.stderr.write("seal rules: name a document, or --check, and not both.\n")
        return 2
    root = os.path.abspath(args.root or os.getcwd())
    try:
        if args.root is None:
            # Typed anywhere inside a repository, the command reads that
            # repository, as `seal fold` does. `bin/` is on a user's PATH,
            # and the tree this script ships in is the plugin's, not theirs.
            root = sibling("optin").repo_root(root) or root
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
            sys.stderr.write(f"seal rules: cannot read {args.doc}: {error}.\n")
            return 2
        sys.stdout.write(render(root, text))
    except Unreadable as error:
        sys.stderr.write(f"seal rules: {error}.\n")
        return 2
    return 0


if __name__ == "__main__":
    for _name in ("stdout", "stderr"):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
