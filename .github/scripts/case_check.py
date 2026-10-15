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
must pass. Then, for each such function, at most `DRAW_CAP` mutants are
drawn, best first:

  1. the lines it runs, ranked by how many of its siblings run them too, so
     a line it runs alone comes first; among lines as many run, a changed
     line first, then one line of each unit before a second of any;
  2. the lines no case's call ran, whose mutants run the whole file: the
     units of its own file it names, a helper or a constant, followed
     through the helpers they name; then the lines the pull request changed
     in shipped code, a `.py` outside `tests/` and a `.md` outside `seal/`
     whose mutant is the line removed, the files it names first.

A line a sibling ran and it did not is never drawn, since under that line's
mutant only the cases that ran it run. The draw is ranked so a case that
protects something its file did not finds it near the front; the first run
on PR #939 drew 400 and more mutants for each case in path order and ran 23
within the bound. A test function's own lines are never mutated. On a line
the operators are an assertion dropped, a condition negated, the last operand
of a condition's `and` or `or` dropped, a comparison flipped (`in` and `is`
among them), `and` and `or` swapped, a boolean flipped, a `return` made
`return None`, an integer moved by one, the statement removed, and an element
of a list, a dict or a call removed; a mutant that does not parse is not
run.

How it errs. Under: a line reached only through a subprocess or a fixture's
setup is not traced, so a case whose decision runs in a child process gets
its mutants from the names it uses and from the diff alone. Over: a line one
case runs and its siblings do not may be setup only it needs, which costs a
mutant run and proves nothing.

**The pass rule.** Each such function is the only killer in its file of at
least one mutant: under it, through `mutation-check --baseline-passed`, its
own ids fail and no other case of its file that ran the mutant's line does.
Its own ids run first, and the others only where they failed, so a mutant it
does not kill costs one case's run. A case that never ran the line cannot
fail under it; where no case's call ran it, as at import or in a fixture's
setup, the whole file runs, since such a mutant can change which ids exist,
and a function is alone where every failing id is its own. A run of some of a file's cases keeps xdist's
workers only where the traced run timed their calls at `WORKERS_PAY_S` or
more. A function's proof stops at its first such
mutant. One whose draw runs out first is named, `kills nothing its file does
not`. Its scope is the function's file: a case in another file that kills the
same mutant is not seen, which is the price of running one file. The ids of
one parametrized function are one case here: a kill they share is that
function's own, so a row added to it is not proved on its own.

**What nothing kills is a report, not a gate.** Once every file's proofs are
done, the changed shipped lines' mutants not yet run run in what is left of
the bound. Those that ran and that no case killed are listed with their
lines, and so are the test functions the pull request removed. A gate there
would be red for a mutant a file this check did not run kills, and would
send a case into this pull request's files to quiet it; a removal is proven
by the mutation table its work item keeps.

**The proof has a bound, and the job ends on it, never on a timeout.**
`--bound` is minutes for the whole check, five by default. Each file gets an
equal share of what is left of it when its turn comes. A file whose traced
run alone passes what is left is named, `restructure: test the decision
directly`, and so is a function still unproven when the bound is spent: a file
that slow is testing its decisions through the whole stack.

It runs on ubuntu alone. A case none of whose ids ran its body there, because
pytest never started its call or its own stop ended it, is named for that,
`not proved: none of its ids ran its call to the end on this runner`, and no
mutant is run against it; the job fails as it does for any case not proved.
The tracer decides it once per id from pytest's call report, and only that
naming reads it: a case that asserted and then stopped keeps its traced
lines, so it is drawn from and run under mutants like any other. An expected
failure that runs its body is a run: a mutant fails it by making a strict one
pass or by raising other than the exception its mark names, and one whose
mark does neither is named for killing nothing.

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
# pytest's exit code for a run that collected no case, as a file skipped at
# import leaves it.
NONE_COLLECTED = 5

# The tracer the traced run loads as `-p specseal_case_trace`, written to a
# directory of its own and put first on `PYTHONPATH`, so an xdist worker loads
# it too. It traces each case's call, not its setup, records the lines under
# the root outside `.venv/` and the call's seconds, and writes one file per
# process at the end, every id's lines and, apart, the ids that stopped short.
TRACER = "specseal_case_trace"
TRACER_SOURCE = """
import json, os, sys, threading, time
import pytest

_root = os.path.realpath(os.environ["SPECSEAL_CASE_TRACE_ROOT"]) + os.sep
_out = os.environ["SPECSEAL_CASE_TRACE_DIR"]
_hits, _seen, _now, _seconds, _skipped = {}, {}, [None], {}, set()


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
    began = time.monotonic()
    sys.settrace(_trace)
    threading.settrace(_trace)
    try:
        yield
    finally:
        sys.settrace(None)
        threading.settrace(None)
        _now[0] = None
        _seconds[item.nodeid] = time.monotonic() - began


# An id stopped short when pytest's own stop ended its call, whatever spelled
# it, and ran its body when the call ended any other way, an expected failure
# whose body raised included. This reads the finished call report, outermost
# so every other implementation has written it, and pytest's xfail stop is a
# run only where its unittest plugin raised it for an expected failure. The
# stopped ids are written apart, and their lines are kept: a case that
# asserted and then stopped fails under a mutant of what it asserted.
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    report = (yield).get_result()
    if report.when != "call" or not report.skipped:
        return
    stop = call.excinfo is not None and call.excinfo.errisinstance(
        pytest.xfail.Exception
    )
    expected = getattr(
        getattr(item, "obj", None), "__unittest_expecting_failure__", False
    )
    if not hasattr(report, "wasxfail") or (stop and not expected):
        _skipped.add(report.nodeid)


def pytest_sessionfinish(session):
    with open(os.path.join(_out, f"{os.getpid()}.json"), "w", encoding="utf-8") as f:
        hits = {k: sorted(v) for k, v in _hits.items()}
        json.dump({"hits": hits, "seconds": _seconds, "short": sorted(_skipped)}, f)
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
    "kills nothing its file does not: of the {count} mutants drawn for it, the "
    "lines fewest of its siblings run first and at most {cap}, each it killed "
    "was killed by another case too, or none was"
)
NEVER_RAN = (
    "not proved: none of its ids ran its call to the end on this runner "
    "(skipped, deselected or not collected), so no mutant was run against it"
)
# The most mutants one case's draw holds. The draw is ranked, so a case that
# protects something its file did not finds it near the front, and one that
# has found nothing by here is named rather than run to the bound. PR #939's
# first run drew 400 and more for each case, and ran 23.
DRAW_CAP = 12
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
# Membership and identity, the comparisons Python spells in words; the
# longer spelling first, since ` in ` is inside ` not in `.
MEMBERSHIPS = (
    (" not in ", " in "),
    (" in ", " not in "),
    (" is not ", " is "),
    (" is ", " is not "),
)
# The shapes a line ending in `,` is tried in: an element of a list, an
# entry of a dict, an argument of a call.
ELEMENT_SHAPES = ("[{}]", "{{{}}}", "f({})")


def operators(line):
    """`[(label, mutated line)]` for one line of Python, without its line end:
    at most one mutant of each kind, each at the first place it applies. The
    mutated line is `None` where the mutant removes the line.

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
        try:
            test = ast.parse(branch[2], mode="eval").body
        except SyntaxError:
            test = None
        if isinstance(test, ast.BoolOp):
            # A case guarding the operand a sibling never makes true is told
            # apart only by that operand gone; flipping `and` and `or` fails
            # the siblings too.
            word = "and" if isinstance(test.op, ast.And) else "or"
            kept = test.values[:-1]
            kept = kept[0] if len(kept) == 1 else ast.BoolOp(op=test.op, values=kept)
            found.append(
                (
                    f"the last operand of `{word}` dropped",
                    f"{indent}{branch[1]} {ast.unparse(kept)}:",
                )
            )
    for table in (COMPARISONS, MEMBERSHIPS):
        for old, new in table:
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
    for shape in ELEMENT_SHAPES if text.endswith(",") else ():
        try:
            ast.parse(shape.format(text))
        except SyntaxError:
            continue
        # `None`: the line goes, as a changed `.md` line's does.
        found.append(("element removed", None))
        break
    return found


def mutants_of(path, source, lineno):
    """`[(label, old, new)]` for the line `lineno` of the file at `path`, each
    an edit `mutation-check --replace` lands exactly once: the line itself,
    widened by the lines above it until it is unique. A `.py` mutant that does
    not parse is left out; a `.md` line's one mutant is the line removed.

    Each line keeps the end it has in `source`, so `old` is the file's own
    text: `mutation-check` matches it against the bytes on disk, and a
    checkout with CRLF line ends, as Windows makes, held no line `\\n`-joined
    (PR #939's `windows-latest` leg, every mutant refused).

    Reads: owned — the file's own text, split where Python ends a line; unknown passed
    """
    lines = PYTHON_LINE_END.split(source)
    if not 0 < lineno <= len(lines) or not lines[lineno - 1].strip():
        return []
    ends = [*PYTHON_LINE_END.findall(source), ""]
    whole = [text + end for text, end in zip(lines, ends, strict=True)]
    line = lines[lineno - 1]
    edits = [("line removed", None)] if path.endswith(".md") else operators(line)
    start = next(
        (
            s
            for s in range(lineno - 1, max(lineno - 5, -1), -1)
            if source.count("".join(whole[s:lineno])) == 1
        ),
        None,
    )
    if start is None:
        return []
    old = "".join(whole[start:lineno])
    head = "".join(whole[start : lineno - 1])
    found = []
    for label, new in edits:
        replaced = head + ("" if new is None else new + ends[lineno - 1])
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
    """`(exit, output)` of one `mutation-check` run.

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
    return done.returncode, done.stdout + done.stderr


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


def under(root, mutant, cases, runner, file, calls, deadline):
    """`(exit, output)` of `mutation-check` for `cases` run under `mutant`,
    bounded by what is left before `deadline`.

    Reads: observed — mutation-check's exit code and its output; unknown refused
    """
    _label, path, old, new = mutant
    return mutation_run(
        root,
        path,
        old,
        new,
        [*narrowed(runner, cases, file, calls), *TAIL],
        deadline - time.monotonic(),
        True,
    )


def own_ids(hits, file, functions, name):
    """The ids of the test function `name` the traced run recorded, sorted.

    Reads: nothing — compares the ids it is handed
    """
    return sorted(i for i in hits if sole_killer([i], file, functions) == name)


def selected(hits, path, label):
    """The cases that ran the mutant's line during their call, sorted; none
    where no case did, as for a line run at import or in a fixture's setup.
    A case that never runs a line cannot fail under its mutant, so where any
    case ran it, those cases alone decide the killer set.

    Reads: owned — the mutant's label, `<path>:<line> <operator>` as `mutants_of` writes it; unknown passed
    """
    lineno = int(label.split(" ", 1)[0].rsplit(":", 1)[1])
    return sorted(nodeid for nodeid, pairs in hits.items() if (path, lineno) in pairs)


def unrun(every_diff, diff_killed):
    """How many of the changed shipped lines' mutants no run gave a verdict.
    A proof's kill is recorded for any line of a changed file, so one on an
    unchanged line is in `diff_killed` and is not one of these.

    Reads: nothing — compares the labels it is handed
    """
    return sum(1 for label, *_rest in every_diff if label not in diff_killed)


# The seconds of the cases' calls, as the traced run measured them, below
# which a run of some of a file's cases turns xdist's workers off: starting
# them costs about this on a four-core runner.
WORKERS_PAY_S = 4.0


def narrowed(runner, cases, file, seconds=None):
    """The command for a run of `cases`: the runner and the ids, with xdist's
    workers turned off where the runner asks for them, only some of the
    file's cases run, and their calls took under `WORKERS_PAY_S` in the
    traced run, since starting the workers then costs more than they save.

    Reads: nothing — joins the words it is handed
    """
    if cases != [file] and "-n" in runner:
        spent = sum((seconds or {}).get(case, 0.0) for case in cases)
        if spent < WORKERS_PAY_S:
            return [*runner, *cases, "-n", "0"]
    return [*runner, *cases]


def traced_run(root, file, runner, timeout):
    """`(exit, seconds, last line, {nodeid: {(path, line)}}, {nodeid:
    seconds}, {nodeid})` of the test file run once as it stands, each case's
    call traced and timed; the last are the ids pytest stopped short of their
    body, empty on a timeout.

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
            return None, time.monotonic() - started, "timed out", {}, {}, set()
        seconds = time.monotonic() - started
        hits, calls, short = {}, {}, set()
        for name in os.listdir(out):
            try:
                with open(os.path.join(out, name), encoding="utf-8") as f:
                    found = json.load(f)
                for nodeid, pairs in found["hits"].items():
                    hits.setdefault(nodeid, set()).update(map(tuple, pairs))
                calls.update(found["seconds"])
                short.update(found["short"])
            except (OSError, ValueError, KeyError, AttributeError, TypeError):
                continue
    lines = (done.stdout + done.stderr).strip().splitlines()
    return done.returncode, seconds, lines[-1] if lines else "", hits, calls, short


def drawn(root, file, name, functions, hits, units, diff, cap=DRAW_CAP):
    """The mutants drawn for the test function `name`, best first and at most
    `cap`, in the order the module docstring gives: the lines it ran, those
    fewest of its siblings ran first, then the lines no case ran, its file's
    units it names before the changed shipped lines.

    Reads: observed — the files the drawn lines are in, read from the root; unknown passed
    """
    runners = {}
    for nodeid, pairs in hits.items():
        owner = sole_killer([nodeid], file, functions)
        for pair in pairs:
            runners.setdefault(pair, set()).add(owner)
    spans = {
        (file, n)
        for _, (node, _text) in functions.items()
        for n in range(node.lineno, node.end_lineno + 1)
    }
    changed = {(path, n) for path, numbers in diff.items() for n in numbers}

    tops = {}

    def rank(pair):
        # Fewer siblings under the mutant, fewer who can share its kill; a
        # changed line before an unchanged one that as many run.
        return len(runners[pair]), pair not in changed

    def unit(pair):
        path, lineno = pair
        if path not in tops:
            tops[path] = top_units(root, path)
        return next((s for s, e in tops[path] if s <= lineno <= e), 0)

    ran = sorted(
        (p for p, who in runners.items() if name in who and p not in spans),
        key=lambda p: (*rank(p), p),
    )
    # Among lines as many siblings run, one line of each unit before a second
    # of any: a unit's lines tend to fall to the same cases, and taken in path
    # order one unit's lines filled the whole draw.
    taken, keyed = {}, []
    for pair in ran:
        group = (*rank(pair), pair[0], unit(pair))
        taken[group] = taken.get(group, -1) + 1
        keyed.append(((*rank(pair), taken[group], pair), pair))
    order = [pair for _key, pair in sorted(keyed)]
    # Then the lines no case ran in its call, whose mutants run the whole
    # file. A changed file the case names in its own text comes first: a case
    # that runs a script as a child process names its path, and runs none of
    # it where the tracer can see. A line a sibling ran and this case did not
    # is never drawn: under its mutant only the cases that ran it run.
    text = functions[name][1] if name in functions else ""
    named_first = sorted(diff, key=lambda p: (os.path.basename(p) not in text, p))
    untraced = [(file, n) for n in units.get(name, [])]
    untraced += [(path, n) for path in named_first for n in diff[path]]
    order += [p for p in untraced if p not in runners]
    return mutants_at(root, [p for p in order if p not in spans], cap)


def top_units(root, path):
    """`[(first line, last line)]` of each top-level `def` and `class` in the
    `.py` file at `path`; none for another file or one that will not parse.

    Reads: observed — the file's source, parsed by `ast`; unknown passed
    """
    if not path.endswith(".py"):
        return []
    try:
        with open(os.path.join(root, path), encoding="utf-8") as f:
            tree = ast.parse(f.read())
    except (OSError, SyntaxError, ValueError):
        return []
    defs = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
    return [(n.lineno, n.end_lineno) for n in tree.body if isinstance(n, defs)]


def mutants_at(root, order, cap=None):
    """The mutants of the `(path, line)` pairs in `order`, in that order, each
    pair once, at most `cap`; a line inside a multi-line string has none.

    Reads: observed — the files the lines are in, read from the root; unknown passed
    """
    sources, found, seen = {}, [], set()
    for path, lineno in order:
        if cap is not None and len(found) >= cap:
            break
        if (path, lineno) in seen:
            continue
        seen.add((path, lineno))
        if path not in sources:
            try:
                # The line ends as they stand: a mutant is matched against
                # the file's bytes, and reading CRLF as `\n` built mutants no
                # Windows checkout holds.
                with open(
                    os.path.join(root, path),
                    encoding="utf-8",
                    newline="",
                ) as f:
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
    if cap is not None:
        del found[cap:]
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
    started, limit, costs, contexts = time.monotonic(), bound * 60, [], []
    diff_killed = {}
    for index, (file, (source, functions, names)) in enumerate(pending.items()):
        # Each file left gets an equal share of what is left of the bound, so
        # one file's mutants cannot spend another's proof, and what one file
        # leaves unspent goes to the files after it.
        share = (limit - (time.monotonic() - started)) / (len(pending) - index)
        deadline = time.monotonic() + share
        left = share
        code, each, verdict, hits, calls, short = traced_run(root, file, runner, left)
        if code is None or each > left:
            restructure = RESTRUCTURE_FILE.format(each=each, left=left, bound=bound)
            findings.append((file, restructure))
            continue
        if code not in (0, NONE_COLLECTED):
            findings.append((file, FAILS_AS_IT_STANDS.format(verdict=verdict)))
            continue
        # One none of whose ids ran its body here is named for that rather
        # than for killing nothing its siblings do not. Only this reads the
        # stopped ids: the draw and the cases run under a mutant read every
        # traced line, a stopped call's included.
        through = {i: pairs for i, pairs in hits.items() if i not in short}
        never_ran = [n for n in names if not own_ids(through, file, functions, n)]
        findings += [(f"{file}::{n}", NEVER_RAN) for n in never_ran]
        names = [n for n in names if n not in never_ran]
        units = named_units(source, {n: functions[n] for n in names})
        queues = {n: drawn(root, file, n, functions, hits, units, diff) for n in names}
        totals = {n: len(queue) for n, queue in queues.items()}
        results, proven, before, spent_out = {}, {}, time.monotonic(), False
        tried = set()
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
                mine = own_ids(hits, file, functions, name)
                ran = selected(hits, path, label)
                # A line no case's call ran is run at import or in a fixture,
                # and its mutant can change which ids exist, as an element
                # removed from a parametrization's list does: the whole file
                # runs, never a list of ids it may no longer hold.
                rest = [i for i in ran if i not in mine] if ran else [file]

                tried.add(mutant)
                command = (runner, file, calls, deadline)
                # Its own ids first: it kills few of the mutants drawn for it,
                # and a miss is then one case's run, not its siblings' too.
                # `mine` is never empty here: a function none of whose ids
                # ran was named before the draw.
                code = under(root, mutant, mine, *command)[0]
                if code == RED:
                    code, output = (
                        under(root, mutant, rest, *command) if rest else (SURVIVED, "")
                    )
                    if rest == [file]:
                        owner = sole_killer(failed_ids(output), file, functions)
                        alone = code == RED and owner == name
                    else:
                        alone = code == SURVIVED
                    if alone:
                        results[mutant], proven[name] = name, label
                    elif code == RED:
                        results[mutant] = None
                    if code in (RED, SURVIVED) and path in diff:
                        diff_killed[label] = True
                if code not in (RED, SURVIVED):
                    # Timed out or measured nothing: no verdict, and the share
                    # is spent.
                    spent_out = True
                    break
        for name in names:
            fid = f"{file}::{name}"
            if name in proven:
                proved.append((fid, PROVED.format(mutant=proven[name])))
            elif not queues[name]:
                findings.append(
                    (fid, KILLS_NOTHING_NEW.format(count=totals[name], cap=DRAW_CAP))
                )
            else:
                done = totals[name] - len(queues[name])
                restructure = RESTRUCTURE.format(
                    done=done, count=totals[name], bound=bound, each=each
                )
                findings.append((fid, restructure))
        spent = time.monotonic() - before
        contexts.append((file, hits, calls, results, tried, each, spent))
    # The report's half, once every file's proofs are done: what is left of
    # the changed shipped lines' mutants runs while the bound allows, so a
    # survivor is one that ran and that no case killed.
    end = started + limit
    pairs = [(path, n) for path, numbers in diff.items() for n in numbers]
    every_diff = mutants_at(root, pairs)
    for file, hits, calls, results, tried, each, spent in contexts:
        before = time.monotonic()
        for mutant in every_diff:
            label, path, old, new = mutant
            left = end - time.monotonic()
            if diff_killed.get(label) or mutant in results or left < each:
                continue
            cases = selected(hits, path, label) or [file]
            code, output = mutation_run(
                root,
                path,
                old,
                new,
                [*narrowed(runner, cases, file, calls), *TAIL],
                left,
                True,
            )
            results[mutant] = None
            tried.add(mutant)
            killed = code == RED and bool(failed_ids(output))
            diff_killed[label] = diff_killed.get(label, False) or killed
        spent += time.monotonic() - before
        costs.append(COST.format(file=file, each=each, count=len(tried), spent=spent))
    survivors = sorted(label for label, killed in diff_killed.items() if not killed)
    lines = [
        f"case-check against {baseline}: {len(proved)} proved, {len(findings)} "
        f"named, in {time.monotonic() - started:.0f} s of a {bound:g}-minute bound",
        *costs,
    ]
    lines += [f"  {where}: {proof}" for where, proof in proved]
    lines += [f"  {where}: {finding}" for where, finding in findings]
    lines += [SURVIVOR.format(mutant=label) for label in survivors]
    if unrun(every_diff, diff_killed):
        lines.append(NOT_RUN.format(count=unrun(every_diff, diff_killed)))
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
