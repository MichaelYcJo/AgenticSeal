#!/usr/bin/env python3
"""Does each new or changed test case protect something its file did not? (#929)

The suite grew by appending: every fix planted cases and nothing proved they
guarded anything a sibling did not. This is the regrowth check, and nothing
in it is written by hand: the mutants come from the tree, and the verdict
from which cases fail under them.

**Which cases are read.** A test function new at HEAD against the merge base
with `--baseline`, or whose text differs from the base's (from its first
decorator to its last line, so a docstring-only change is a change).

**Where the mutants come from.** Each file holding such a function runs once
as it stands, under a tracer that records which lines each case runs, and
must pass. Then, for each such function, the mutants are drawn in this order:

  1. the lines it runs and no other case in its file runs;
  2. the lines of the units of its own file it names, a helper or a
     constant, followed through the helpers they name;
  3. the other lines it runs;
  4. the lines the pull request changed in shipped code: a `.py` outside
     `tests/`, and a `.md` outside `seal/`, whose mutant is the line removed.

A test function's own lines are never mutated. On a line the operators are an
assertion dropped, a condition negated, a comparison or a boolean flipped, a
`return` made `return None`, an integer moved by one, and the statement
removed; a mutant that does not parse is not run.

How it errs. Under: a line reached only through a subprocess or a fixture's
setup is not traced, so a case whose decision runs in a child process gets
its mutants from the names it uses and from the diff alone. Over: a line one
case runs and its siblings do not may be setup only it needs, which costs a
mutant run and proves nothing.

**The pass rule.** Each such function is the only killer in its file of at
least one mutant: the cases of its file that ran the mutant's line in their
call run once under it, through `mutation-check --baseline-passed`, and every
failing id belongs to that function. A case that never ran the line cannot
fail under it; where no case's call ran it, as at import or in a fixture's
setup, the whole file runs. Each file gets an equal share of the bound. One that is not is named, `kills nothing its file does not`. Its
scope is the function's file: a case in another file that kills the same
mutant is not seen, which is the price of running one file.

**What nothing kills is a report, not a gate.** The mutants of the changed
shipped lines that ran and that no run case killed are listed with their
lines, and so are the test functions the pull request removed. A gate there
would be red for a mutant a file this check did not run kills, and would
send a case into this pull request's files to quiet it; a removal is proven
by the mutation table its work item keeps.

**The proof has a bound, and the job ends on it, never on a timeout.**
`--bound` is minutes for the whole check, five by default. A file whose traced
run alone passes what is left is named, `restructure: test the decision
directly`, and so is a function still unproven when the bound is spent: a file
that slow is testing its decisions through the whole stack.

It runs on ubuntu alone: a case guarding a Windows-only sentence proves itself
on a run that skips there.

  case_check.py --baseline REF [--root DIR] [--runner CMD] [--bound MIN]

Exit codes: **0** every new or changed function proved, **1** one named, **2**
nothing compared (no merge base, no root). The lines go to stdout and, where
`GITHUB_STEP_SUMMARY` is set, to the step summary; neither names a path
outside the root.
"""

import argparse
import ast
import importlib.util
import json
import os
import re
import shlex
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
MUTATION_CHECK = os.path.normpath(
    os.path.join(HERE, "..", "..", "skills", "verify", "scripts", "mutation_check.py")
)
ARM_CHECK = os.path.join(os.path.dirname(MUTATION_CHECK), "arm_check.py")

# `mutation-check`'s exit codes (`skills/verify/scripts/mutation_check.py`).
RED, SURVIVED, MEASURED_NOTHING = 0, 1, 2

# The tracer the traced run loads as `-p specseal_case_trace`, written to a
# directory of its own and put first on `PYTHONPATH`, so an xdist worker loads
# it too. It traces each case's call, not its setup, records the lines under
# the root outside `.venv/`, and writes one file per process at the end.
TRACER = "specseal_case_trace"
TRACER_SOURCE = """
import json, os, sys, threading
import pytest

_root = os.path.realpath(os.environ["SPECSEAL_CASE_TRACE_ROOT"]) + os.sep
_out = os.environ["SPECSEAL_CASE_TRACE_DIR"]
_hits, _seen, _now = {}, {}, [None]


def _ours(path):
    if path not in _seen:
        real = os.path.realpath(path)
        _seen[path] = (
            real[len(_root):].replace(os.sep, "/")
            if real.startswith(_root) and os.sep + ".venv" + os.sep not in real
            else None
        )
    return _seen[path]


def _trace(frame, event, arg):
    rel = _ours(frame.f_code.co_filename)
    if rel is None or _now[0] is None:
        return None
    hits = _hits.setdefault(_now[0], set())

    def line(frame, event, arg):
        if event == "line":
            hits.add((rel, frame.f_lineno))
        return line

    hits.add((rel, frame.f_lineno))
    return line


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    _now[0] = item.nodeid
    sys.settrace(_trace)
    threading.settrace(_trace)
    try:
        yield
    finally:
        sys.settrace(None)
        threading.settrace(None)
        _now[0] = None


def pytest_sessionfinish(session):
    with open(os.path.join(_out, f"{os.getpid()}.json"), "w", encoding="utf-8") as f:
        json.dump({k: sorted(v) for k, v in _hits.items()}, f)
"""
# Where Python's tokenizer ends a line, which is what `ast` numbers lines by.
# `str.splitlines` also ends one at characters such as U+2028 that Python
# reads inside a string, so a file holding one would shift every later line
# and cut a function's text short of the line its change is on.
PYTHON_LINE_END = re.compile(r"\r\n|\r|\n")
# What every run of a test file is handed after its path: the summary lines
# the killer set is read from, and no cache written into the tree.
TAIL = ["-q", "-rfE", "-p", "no:cacheprovider"]

PROVED = "proved — the only killer in its file of {mutant}"
KILLS_NOTHING_NEW = (
    "kills nothing its file does not: of the {count} mutants drawn for it, each "
    "it killed was killed by another case too, or none was"
)
FAILS_AS_IT_STANDS = (
    "its cases do not pass as they stand, so no mutant was run: {verdict}"
)
RESTRUCTURE_FILE = (
    "restructure: test the decision directly — one traced run of the file "
    "took {each:.0f} s, and {left:.0f} s of the check's {bound:g}-minute bound "
    "was left"
)
RESTRUCTURE = (
    "restructure: test the decision directly — {done} of the {count} mutants "
    "drawn for it ran within the check's {bound:g}-minute bound, a run of its "
    "file {each:.0f} s each, and none was its alone"
)
COST = "  cost {file}: a traced run {each:.0f} s, {count} mutants in {spent:.0f} s"
SURVIVOR = "  survived {mutant}"
NOT_RUN = "  not run within the bound: {count} mutants of changed shipped lines"
REMOVED = "  removed {fid}"


# A line no operator touches: a comment, a definition's head, an import, a
# docstring's delimiter, or a branch keyword with nothing to negate.
INERT = ("#", "def ", "async def ", "class ", "@", '"""', "'''", "import ", "from ")
COMPARISONS = (
    (" == ", " != "),
    (" != ", " == "),
    (" <= ", " > "),
    (" >= ", " < "),
    (" < ", " >= "),
    (" > ", " <= "),
)


def operators(line):
    """`[(label, mutated line)]` for one line of Python, without its line end:
    at most one mutant of each kind, each at the first place it applies.

    Reads: owned — one source line, matched by the patterns this module defines; unknown passed
    """
    text = line.strip()
    if not text or text.startswith(INERT):
        return []
    indent = line[: len(line) - len(line.lstrip())]
    found = []
    assertion = re.match(r"assert (.+?)(, .*)?$", text)
    if assertion and assertion.group(1) != "True":
        rest = assertion.group(2) or ""
        found.append(("assertion dropped", f"{indent}assert True{rest}"))
    branch = re.match(r"(if|elif|while) (.+):$", text)
    if branch:
        found.append(("condition negated", f"{indent}{branch[1]} not ({branch[2]}):"))
    for old, new in COMPARISONS:
        if old in line:
            label = f"`{old.strip()}` made `{new.strip()}`"
            found.append((label, line.replace(old, new, 1)))
            break
    for old, new in ((" and ", " or "), (" or ", " and ")):
        if old in line:
            found.append(
                (f"`{old.strip()}` made `{new.strip()}`", line.replace(old, new, 1))
            )
            break
    flip = re.search(r"\b(True|False)\b", line)
    if flip and not assertion:
        other = "False" if flip[1] == "True" else "True"
        at = flip.start()
        found.append(
            (f"`{flip[1]}` made `{other}`", line[:at] + other + line[flip.end() :])
        )
    returned = re.match(r"return (?!None$)(.+)$", text)
    if returned:
        found.append(("`return` made `return None`", f"{indent}return None"))
    number = re.search(r"(?<![\w.'\"])(\d+)(?![\w.'\"])", line)
    if number:
        moved = str(int(number[1]) + 1)
        label = f"`{number[1]}` made `{moved}`"
        found.append((label, line[: number.start()] + moved + line[number.end() :]))
    if not text.endswith((":", ",", "(", "[", "{", "\\")) and not text.startswith(
        ("return", "else", "elif", "try", "except", "finally", "pass", "yield")
    ):
        try:
            ast.parse(text)
        except SyntaxError:
            pass
        else:
            found.append(("statement removed", f"{indent}pass"))
    return found


def mutants_of(path, source, lineno):
    """`[(label, old, new)]` for the line `lineno` of the file at `path`, each
    an edit `mutation-check --replace` lands exactly once: the line itself,
    widened by the lines above it until it is unique. A `.py` mutant that does
    not parse is left out; a `.md` line's one mutant is the line removed.

    Reads: owned — the file's own text, split where Python ends a line; unknown passed
    """
    lines = PYTHON_LINE_END.split(source)
    if not 0 < lineno <= len(lines) or not lines[lineno - 1].strip():
        return []
    line = lines[lineno - 1]
    edits = [("line removed", None)] if path.endswith(".md") else operators(line)
    start = next(
        (
            s
            for s in range(lineno - 1, max(lineno - 5, -1), -1)
            if source.count("\n".join(lines[s:lineno]) + "\n") == 1
        ),
        None,
    )
    if start is None:
        return []
    old = "\n".join(lines[start:lineno]) + "\n"
    head = "".join(above + "\n" for above in lines[start : lineno - 1])
    found = []
    for label, new in edits:
        replaced = head + ("" if new is None else new + "\n")
        if path.endswith(".py"):
            try:
                ast.parse(source.replace(old, replaced, 1))
            except SyntaxError:
                continue
        found.append((f"{path}:{lineno} {label}", old, replaced))
    return found


def test_functions(source):
    """`{name: (node, source text)}` for every test function of a module, in
    source order: a top-level `test*` function, and a `test*` method of a
    top-level `Test*` class named `Class::method`. The text runs from the
    first decorator to the last line, so a changed parametrization is a
    changed function.

    Reads: observed — a test module's source, parsed by `ast`; unknown refused
    """
    tree = ast.parse(source)
    lines = PYTHON_LINE_END.split(source)
    found = {}

    def add(name, node):
        start = min([node.lineno] + [d.lineno for d in node.decorator_list])
        found[name] = (node, "\n".join(lines[start - 1 : node.end_lineno]))

    defs = (ast.FunctionDef, ast.AsyncFunctionDef)
    for node in tree.body:
        if isinstance(node, defs) and node.name.startswith("test"):
            add(node.name, node)
        elif isinstance(node, ast.ClassDef) and node.name.startswith("Test"):
            for inner in node.body:
                if isinstance(inner, defs) and inner.name.startswith("test"):
                    add(f"{node.name}::{inner.name}", inner)
    return found


def git(root, *args):
    """git's stdout for `args` in `root`, or None where git exits non-zero.

    Reads: observed — the output of a git command run in the root; unknown refused
    """
    done = subprocess.run(
        ["git", "-C", root, *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    return done.stdout if done.returncode == 0 else None


def tracked_test_files(root):
    """Every tracked `tests/…/test_*.py`, sorted.

    Reads: observed — `git ls-files` over the root's `tests/`; unknown refused
    """
    listed = git(root, "ls-files", "-z", "--", "tests") or ""
    return sorted(
        path
        for path in listed.split("\0")
        if path.endswith(".py") and os.path.basename(path).startswith("test_")
    )


def shipped(path):
    """Whether a changed path is shipped text this check mutates: a `.py`
    outside `tests/`, or a `.md` outside `seal/`.

    Reads: nothing — compares a path's prefix and suffix
    """
    if path.endswith(".py"):
        return not path.startswith("tests/")
    return path.endswith(".md") and not path.startswith("seal/")


def changed_lines(root, merge_base):
    """`{path: [line numbers at HEAD]}` for the shipped files the range
    changed, read off `git diff -U0`'s hunk heads.

    Reads: observed — `git diff -U0` between the merge base and HEAD; unknown passed
    """
    diff = git(root, "diff", "-U0", "--no-color", "--no-ext-diff", merge_base, "HEAD")
    found, path = {}, None
    for line in PYTHON_LINE_END.split(diff or ""):
        if line.startswith("+++ "):
            name = line[4:]
            path = name[2:] if name.startswith("b/") else None
            continue
        hunk = re.match(r"@@ -\S+ \+(\d+)(?:,(\d+))? @@", line)
        if hunk and path and shipped(path):
            start, count = int(hunk[1]), int(hunk[2] or 1)
            found.setdefault(path, []).extend(range(start, start + count))
    return found


def string_interiors(source):
    """The line numbers strictly inside a string literal that spans lines, a
    docstring's body among them: no operator mutates prose there.

    Reads: observed — a module's source, parsed by `ast`; unknown passed
    """
    inside = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if node.end_lineno and node.end_lineno > node.lineno:
                inside.update(range(node.lineno + 1, node.end_lineno + 1))
    return inside


def named_units(source, functions):
    """`{test name: [line numbers]}`: for each test function, the lines of the
    top-level units of its own file it names, a helper or a constant, followed
    through the names those helpers use. Test functions are never included.

    Reads: observed — a test module's source, parsed by `ast`; unknown passed
    """
    tree = ast.parse(source)
    units = {}
    for node in tree.body:
        names = []
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if not node.name.startswith(("test", "Test")):
                names = [node.name]
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            names = [t.id for t in targets if isinstance(t, ast.Name)]
        for name in names:
            units[name] = node

    def used(node):
        return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)} | {
            n.attr for n in ast.walk(node) if isinstance(n, ast.Attribute)
        }

    found = {}
    for name, (node, _text) in functions.items():
        seen, todo, lines = set(), list(used(node) & set(units)), []
        while todo:
            unit = todo.pop()
            if unit in seen:
                continue
            seen.add(unit)
            body = units[unit]
            lines.extend(range(body.lineno, body.end_lineno + 1))
            todo.extend(used(body) & set(units))
        found[name] = sorted(set(lines))
    return found


def failed_ids(output):
    """The ids pytest's `FAILED` and `ERROR` summary lines name in `output`,
    in order, each once.

    Reads: observed — pytest's short summary lines inside mutation-check's output; unknown passed
    """
    found = re.finditer(r"^(?:FAILED|ERROR) (\S.*?)(?: - .*)?$", output, re.MULTILINE)
    return list(dict.fromkeys(m.group(1) for m in found))


def mutation_run(root, path, old, new, tests, timeout, baseline_passed=False):
    """`(exit, first line, output)` of one `mutation-check` run.

    Reads: observed — mutation-check's exit code and its output; unknown refused
    """
    done = subprocess.run(
        [
            sys.executable,
            MUTATION_CHECK,
            os.path.join(root, path),
            "--replace",
            old,
            new,
            "--tests",
            shlex.join(tests),
            "--cwd",
            root,
            "--timeout",
            str(timeout),
            *(["--baseline-passed"] if baseline_passed else []),
        ],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    output = done.stdout + done.stderr
    first = next(
        (line for line in output.splitlines() if line.strip()),
        f"exit {done.returncode}, and mutation-check printed nothing",
    )
    return done.returncode, first.replace(root + os.sep, "").replace(root, "."), output


def sole_killer(killers, file, functions):
    """The test function of `file` every one of `killers` belongs to, or None
    where they are none or belong to more than one.

    Reads: nothing — compares the ids it is handed
    """
    owners = set()
    for killer in killers:
        for name in functions:
            nodeid = f"{file}::{name}"
            if killer == nodeid or killer.startswith(nodeid + "["):
                owners.add(name)
                break
        else:
            return None
    return owners.pop() if len(owners) == 1 else None


def selected(hits, path, label):
    """The cases that ran the mutant's line during their call, sorted; none
    where no case did, as for a line run at import or in a fixture's setup.
    A case that never runs a line cannot fail under its mutant, so where any
    case ran it, those cases alone decide the killer set.

    Reads: owned — the mutant's label, `<path>:<line> <operator>` as `mutants_of` writes it; unknown passed
    """
    lineno = int(label.split(" ", 1)[0].rsplit(":", 1)[1])
    return sorted(nodeid for nodeid, pairs in hits.items() if (path, lineno) in pairs)


def narrowed(runner, cases, file):
    """The command for a run of `cases`: the runner and the ids, with xdist's
    workers turned off where the runner asks for them and only some of the
    file's cases run, since starting the workers costs more than they save.

    Reads: nothing — joins the words it is handed
    """
    if cases != [file] and "-n" in runner:
        return [*runner, *cases, "-n", "0"]
    return [*runner, *cases]


def traced_run(root, file, runner, timeout):
    """`(exit, seconds, last line, {nodeid: {(path, line)}})` of the test file
    run once as it stands, each case's call traced.

    Reads: observed — the runner's exit and output, and the tracer's JSON files it wrote; unknown refused
    """
    with tempfile.TemporaryDirectory(prefix="case-check-") as scratch:
        with open(os.path.join(scratch, TRACER + ".py"), "w", encoding="utf-8") as f:
            f.write(TRACER_SOURCE)
        out = os.path.join(scratch, "hits")
        os.makedirs(out)
        env = dict(os.environ)
        env["PYTHONPATH"] = os.pathsep.join(
            p for p in (scratch, env.get("PYTHONPATH")) if p
        )
        env["SPECSEAL_CASE_TRACE_ROOT"], env["SPECSEAL_CASE_TRACE_DIR"] = root, out
        started = time.monotonic()
        try:
            done = subprocess.run(
                [*runner, file, *TAIL, "-p", TRACER],
                cwd=root,
                env=env,
                capture_output=True,
                encoding="utf-8",
                errors="replace",
                timeout=max(timeout, 1),
            )
        except subprocess.TimeoutExpired:
            return None, time.monotonic() - started, "timed out", {}
        seconds = time.monotonic() - started
        hits = {}
        for name in os.listdir(out):
            try:
                with open(os.path.join(out, name), encoding="utf-8") as f:
                    for nodeid, pairs in json.load(f).items():
                        hits.setdefault(nodeid, set()).update(map(tuple, pairs))
            except (OSError, ValueError):
                continue
    lines = (done.stdout + done.stderr).strip().splitlines()
    return done.returncode, seconds, lines[-1] if lines else "", hits


def drawn(root, file, name, functions, hits, units, diff):
    """The mutants drawn for the test function `name`, in the order the module
    docstring gives: its own lines first, then its file's units it names,
    then the rest it runs, then the changed shipped lines.

    Reads: observed — the files the drawn lines are in, read from the root; unknown passed
    """
    mine, others = set(), set()
    for nodeid, pairs in hits.items():
        owner = sole_killer([nodeid], file, functions)
        (mine if owner == name else others).update(pairs)
    spans = {
        (file, n)
        for _, (node, _text) in functions.items()
        for n in range(node.lineno, node.end_lineno + 1)
    }
    order = sorted(mine - others - spans)
    order += [(file, n) for n in units.get(name, []) if (file, n) not in spans]
    order += sorted(mine - spans)
    # A changed file the case names in its own text comes first: a case that
    # runs a script as a child process names its path, and runs none of it
    # where the tracer can see.
    text = functions[name][1] if name in functions else ""
    named_first = sorted(diff, key=lambda p: (os.path.basename(p) not in text, p))
    order += [(path, n) for path in named_first for n in diff[path]]
    sources, found, seen = {}, [], set()
    for path, lineno in order:
        if (path, lineno) in seen:
            continue
        seen.add((path, lineno))
        if path not in sources:
            try:
                with open(os.path.join(root, path), encoding="utf-8") as f:
                    text = f.read()
                interior = string_interiors(text) if path.endswith(".py") else set()
            except (OSError, SyntaxError, ValueError):
                text, interior = None, set()
            sources[path] = (text, interior)
        text, interior = sources[path]
        if text is None or lineno in interior:
            continue
        found.extend(
            (label, path, old, new)
            for label, old, new in mutants_of(path, text, lineno)
        )
    return found


def check(root, baseline, runner, bound):
    """`(exit, lines)` for the tree at `root` against `baseline`.

    Reads: observed — the root's tracked test files at HEAD and at the merge base, and the range's diff, through git; unknown refused
    """
    merge_base = (git(root, "merge-base", baseline, "HEAD") or "").strip()
    if not merge_base:
        return 2, [
            f"case-check: nothing compared — no merge base of `{baseline}` and HEAD"
        ]
    diff = changed_lines(root, merge_base)
    files = tracked_test_files(root)
    findings, proved, pending, removed = [], [], {}, []
    for file in files:
        try:
            with open(os.path.join(root, file), encoding="utf-8") as handle:
                source = handle.read()
            head = test_functions(source)
        except (OSError, SyntaxError, ValueError) as error:
            findings.append((file, f"does not parse: {error}"))
            continue
        base_source = git(root, "show", f"{merge_base}:{file}")
        try:
            base = test_functions(base_source) if base_source is not None else {}
        except (SyntaxError, ValueError):
            base = {}
        removed += [f"{file}::{name}" for name in base if name not in head]
        changed = [
            n for n, (_, text) in head.items() if base.get(n, (0, None))[1] != text
        ]
        if changed:
            pending[file] = (source, head, changed)
    for file in tests_at(root, merge_base):
        if file not in files:
            removed += [
                f"{file}::{name}" for name in base_functions(root, merge_base, file)
            ]
    started, limit, costs = time.monotonic(), bound * 60, []
    diff_killed = {}
    for index, (file, (source, functions, names)) in enumerate(pending.items()):
        # Each file left gets an equal share of what is left of the bound, so
        # one file's mutants cannot spend another's proof.
        share = (limit - (time.monotonic() - started)) / (len(pending) - index)
        deadline = time.monotonic() + share
        left = share
        code, each, verdict, hits = traced_run(root, file, runner, left)
        if code is None or each > left:
            restructure = RESTRUCTURE_FILE.format(each=each, left=left, bound=bound)
            findings.append((file, restructure))
            continue
        if code != 0:
            findings.append((file, FAILS_AS_IT_STANDS.format(verdict=verdict)))
            continue
        units = named_units(source, {n: functions[n] for n in names})
        queues = {n: drawn(root, file, n, functions, hits, units, diff) for n in names}
        totals = {n: len(queue) for n, queue in queues.items()}
        results, proven, before, spent_out = {}, {}, time.monotonic(), False
        while not spent_out and any(n not in proven and queues[n] for n in names):
            for name in names:
                if name in proven or not queues[name]:
                    continue
                mutant = queues[name].pop(0)
                if mutant in results:
                    if results[mutant] == name:
                        proven[name] = mutant[0]
                    continue
                left = deadline - time.monotonic()
                if left < each:
                    queues[name].insert(0, mutant)
                    spent_out = True
                    break
                label, path, old, new = mutant
                cases = selected(hits, path, label) or [file]
                code, _verdict, output = mutation_run(
                    root,
                    path,
                    old,
                    new,
                    [*narrowed(runner, cases, file), *TAIL],
                    left,
                    True,
                )
                killers = failed_ids(output) if code == RED else []
                owner = sole_killer(killers, file, functions) if killers else None
                results[mutant] = owner
                if path in diff:
                    diff_killed[label] = diff_killed.get(label, False) or bool(killers)
                if owner in names and owner not in proven:
                    proven[owner] = label
        # The report's half: what is left of the changed shipped lines' mutants
        # runs against this file while the bound allows, so a survivor is one
        # that ran and that no case here killed.
        for mutant in drawn(root, file, None, functions, {}, {}, diff):
            label, path, old, new = mutant
            left = deadline - time.monotonic()
            if diff_killed.get(label):
                continue
            if mutant in results or left < each:
                continue
            cases = selected(hits, path, label) or [file]
            code, _verdict, output = mutation_run(
                root,
                path,
                old,
                new,
                [*narrowed(runner, cases, file), *TAIL],
                left,
                True,
            )
            results[mutant] = None
            killed = code == RED and bool(failed_ids(output))
            diff_killed[label] = diff_killed.get(label, False) or killed
        for name in names:
            fid = f"{file}::{name}"
            if name in proven:
                proved.append((fid, PROVED.format(mutant=proven[name])))
            elif not queues[name]:
                findings.append((fid, KILLS_NOTHING_NEW.format(count=totals[name])))
            else:
                done = totals[name] - len(queues[name])
                restructure = RESTRUCTURE.format(
                    done=done, count=totals[name], bound=bound, each=each
                )
                findings.append((fid, restructure))
        spent = time.monotonic() - before
        costs.append(COST.format(file=file, each=each, count=len(results), spent=spent))
    every_diff = 0
    for path, numbers in diff.items():
        try:
            with open(os.path.join(root, path), encoding="utf-8") as f:
                text = f.read()
        except OSError:
            continue
        every_diff += sum(len(mutants_of(path, text, n)) for n in numbers)
    survivors = sorted(label for label, killed in diff_killed.items() if not killed)
    lines = [
        f"case-check against {baseline}: {len(proved)} proved, {len(findings)} "
        f"named, in {time.monotonic() - started:.0f} s of a {bound:g}-minute bound",
        *costs,
    ]
    lines += [f"  {where}: {proof}" for where, proof in proved]
    lines += [f"  {where}: {finding}" for where, finding in findings]
    lines += [SURVIVOR.format(mutant=label) for label in survivors]
    if every_diff > len(diff_killed):
        lines.append(NOT_RUN.format(count=every_diff - len(diff_killed)))
    lines += [REMOVED.format(fid=fid) for fid in sorted(removed)]
    return (1 if findings else 0), lines


def tests_at(root, rev):
    """Every `tests/…/test_*.py` tracked at `rev`, sorted.

    Reads: observed — `git ls-tree` over `tests/` at the revision; unknown refused
    """
    listed = git(root, "ls-tree", "-r", "-z", "--name-only", rev, "--", "tests") or ""
    return sorted(
        path
        for path in listed.split("\0")
        if path.endswith(".py") and os.path.basename(path).startswith("test_")
    )


def base_functions(root, rev, file):
    """The test function names of `file` at `rev`, or none where it will not
    parse.

    Reads: observed — the file's text at the revision, through `git show`; unknown passed
    """
    try:
        return list(test_functions(git(root, "show", f"{rev}:{file}") or ""))
    except (SyntaxError, ValueError):
        return []


def command_words(text):
    """`--runner`'s words, split as `mutation-check` splits `--tests`:
    `arm_check.py#command_words`, which keeps a Windows path's backslashes.

    Reads: observed — the runner's command line, through `arm_check.py`; unknown passed
    """
    name = "specseal_arm_check_for_case_check"
    if name not in sys.modules:
        # Registered before it runs: `arm_check.py`'s dataclasses resolve
        # their annotations through `sys.modules`.
        spec = importlib.util.spec_from_file_location(name, ARM_CHECK)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name].command_words(text)


def main(argv=None):
    """Run the check; the lines to stdout and the step summary.

    Reads: observed — the command line and `GITHUB_STEP_SUMMARY`; unknown refused
    """
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--root", default=".")
    parser.add_argument(
        "--runner",
        default=f"{shlex.quote(sys.executable)} -m pytest",
        help="the command a run's cases are handed to, before the ids",
    )
    parser.add_argument(
        "--bound",
        type=float,
        default=5,
        help="minutes the whole proof may take; a file that would pass it is named",
    )
    args = parser.parse_args(argv)
    root = os.path.abspath(args.root)
    if git(root, "rev-parse", "--git-dir") is None:
        print(f"case-check: nothing compared — `{args.root}` is no git repository")
        return 2
    code, lines = check(root, args.baseline, command_words(args.runner), args.bound)
    text = "\n".join(lines) + "\n"
    sys.stdout.write(text)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as handle:
            handle.write("### case-check\n\n```\n" + text + "```\n")
    return code


if __name__ == "__main__":
    sys.exit(main())
