#!/usr/bin/env python3
"""Does each new or changed test case kill the mutation it names? (#929)

The suite grew by appending: every fix planted cases and nothing proved they
guarded anything a sibling did not. This is the regrowth check. A test
function new at HEAD against the merge base with `--baseline`, or whose source
differs from the base's, carries one `Kills:` line in its docstring:

    Kills: <path> "<OLD>" "<NEW>"

`<path>` is the file the mutation is made in, relative to the root and
spelled with `/`; it may be a `.md` for a case that pins prose. `<OLD>` and
`<NEW>` are JSON string literals, so any string round-trips: `\\"` is a
quote, `\\n` a line break, `\\\\` a backslash. The line is read from the
docstring AS WRITTEN in the file, not as Python evaluates it, so the escapes
mean the same in a raw docstring and in a plain one. The mutation is
`mutation-check <path> --replace OLD NEW`, unchanged.

**One run of the file per mutant, read for its killers.** The function's file
runs once as it stands, and must pass. Then, for each such function,
`mutation-check --baseline-passed` runs the whole file under that function's
mutant. The run must be red, and its failing ids, the killer set, must be the
function's own ids and no other function's: a mutant another case kills
too is guarded twice, which is what the check exists to refuse. A function
with no line, a line outside the grammar, a path that names no file, a
replacement that does not land, a mutant nothing kills, one only another
function kills, or one another function kills too is named, with the
killers.

**The proof has a bound, and the job ends on it, never on a timeout.**
`--bound` is minutes for the whole check, five by default. A file's cost is
read before any mutant is written: the time of its one run as it stands,
once per function to prove. A file whose proof would pass what is left of
the bound is named, `restructure: test the decision directly`, and none of
its mutants run. A file that slow is testing its decisions through the whole
stack.

**The list only shrinks.** `tests/unguarded-files.txt` names the test files
whose existing functions owe no line yet, one path per line, sorted. Every
function of a file off the list carries a line in the grammar, run or not; a
path added to the list against the base's copy is named, and so is one that
is no test file at HEAD. A new or changed function owes its line on the list
or off it.

**Its scope is the function's file.** A case in another file that kills the
same mutation is not seen, which is the price of running one file rather
than the suite. It runs on ubuntu alone: a case guarding a Windows-only
sentence proves itself on a run that skips there.

  case_check.py --baseline REF [--root DIR] [--runner CMD] [--bound MIN]

Exit codes: **0** every function proved, **1** a function or a list line
named, **2** nothing compared (no merge base, no root, a list that cannot
be read). The lines go to stdout and, where `GITHUB_STEP_SUMMARY` is set,
to the step summary; neither names a path outside the root.
"""

import argparse
import ast
import json
import os
import re
import shlex
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
MUTATION_CHECK = os.path.normpath(
    os.path.join(HERE, "..", "..", "skills", "verify", "scripts", "mutation_check.py")
)
UNGUARDED = "tests/unguarded-files.txt"
KILLS = "Kills:"
GRAMMAR = 'Kills: <path> "<OLD>" "<NEW>"'

# `mutation-check`'s exit codes (`skills/verify/scripts/mutation_check.py`).
RED, SURVIVED, MEASURED_NOTHING = 0, 1, 2
# What every run of a test file is handed after its path: the summary lines
# the killer set is read from, and no cache written into the tree.
TAIL = ["-q", "-rfE", "-p", "no:cacheprovider"]

NO_LINE = f"no `{KILLS}` line in its docstring; it owes one: `{GRAMMAR}`"
TWO_LINES = f"more than one `{KILLS}` line; a function names one mutation"
BAD_LINE = (
    "its `Kills:` line is not `" + GRAMMAR + "`, a root-relative path and "
    "two JSON strings: {why}"
)
NO_FILE = "its `Kills:` line names `{path}`, which is no file at HEAD"
NOT_KILLED = "SURVIVED — nothing in its file kills its mutant, this function included"
NOTHING = "the run under its mutant measured nothing: {verdict}"
NOT_OWN = "red, but not by this function: {killers}"
SHARED = "its file kills its mutant without it too: {killers}"
NO_KILLER = "a case pytest named no FAILED or ERROR line for"
PROVED = "proved — red under its mutant, and the killers are this function's alone"
FAILS_AS_IT_STANDS = (
    "its cases do not pass as they stand, so no mutant was run: {verdict}"
)
RESTRUCTURE = (
    "restructure: test the decision directly — proving its {count} new or "
    "changed functions needs {need:.0f} s, one {each:.0f} s run of the file "
    "each, and {left:.0f} s of the check's {bound:g}-minute bound is left"
)
OFF_THE_LIST = (
    f"its file is off `{UNGUARDED}`, so every function in it owes a `{KILLS}` line"
)
LIST_ADDED = (
    "`{path}` is on " + UNGUARDED + " and not on the base's copy: the list "
    "only shrinks, and a new file carries its lines instead"
)
LIST_UNSORTED = f"`{UNGUARDED}` is not sorted, or names a file twice"
LIST_NOT_A_FILE = (
    "`{path}` is on " + UNGUARDED + " and is no test file at HEAD: take the line out"
)


def parse_kills(text):
    """`(path, old, new)` from the text after `Kills:`, or a ValueError
    saying what is wrong.

    Reads: owned — one docstring line in the grammar this module defines; unknown refused
    """
    rest = text.strip()
    path, _, tail = rest.partition(" ")
    if not path or path.startswith(("/", '"')) or "\\" in path:
        raise ValueError("the path is missing, absolute, or spelled with `\\`")
    if ".." in path.split("/"):
        raise ValueError("the path leaves the root")
    decoder = json.JSONDecoder()
    values, tail = [], tail.lstrip()
    for which in ("OLD", "NEW"):
        try:
            value, end = decoder.raw_decode(tail)
        except ValueError as error:
            raise ValueError(f"{which} is not a JSON string ({error.msg})") from None
        if not isinstance(value, str):
            raise ValueError(f"{which} is not a JSON string")
        values.append(value)
        tail = tail[end:].lstrip()
    if tail:
        raise ValueError(f"text follows NEW: `{tail[:40]}`")
    return path, values[0], values[1]


def kills_text(source, function):
    """The text after `Kills:` on the one such line of `function`'s
    docstring, read from `source` as written; None where it has no
    docstring or no such line. Two such lines raise a ValueError.

    Reads: observed — a function's docstring literal in the module's own source; unknown passed
    """
    body = function.body
    if not (
        body
        and isinstance(body[0], ast.Expr)
        and isinstance(body[0].value, ast.Constant)
        and isinstance(body[0].value.value, str)
    ):
        return None
    raw = ast.get_source_segment(source, body[0].value) or ""
    opener = re.match(r"[rRuU]{0,2}(\"\"\"|'''|\"|')", raw)
    if opener:
        raw = raw[opener.end() :]
        if raw.endswith(opener.group(1)):
            raw = raw[: -len(opener.group(1))]
    found = []
    for line in raw.splitlines():
        line = line.strip()
        if line.startswith(KILLS):
            found.append(line[len(KILLS) :])
    if len(found) > 1:
        raise ValueError(TWO_LINES)
    return found[0] if found else None


def test_functions(source):
    """`{name: (node, source text)}` for every test function of a module, in
    source order: a top-level `test*` function, and a `test*` method of a
    top-level `Test*` class named `Class::method`. The text runs from the
    first decorator to the last line, so a changed parametrization is a
    changed function.

    Reads: observed — a test module's source, parsed by `ast`; unknown refused
    """
    tree = ast.parse(source)
    lines = source.splitlines()
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


def read_list(text):
    """The paths of a list file's text, one a line, blank lines dropped.

    Reads: owned — `tests/unguarded-files.txt`, one path a line; unknown refused
    """
    return [line.strip() for line in (text or "").splitlines() if line.strip()]


def list_findings(head, base, files):
    """`[(where, finding)]` for the list at HEAD against the base's copy and
    the test files at HEAD. `base` is None where the base has no list.

    Reads: nothing — compares the lists and the file names it is handed
    """
    found = []
    if head != sorted(set(head)):
        found.append((UNGUARDED, LIST_UNSORTED))
    for path in sorted(set(head) - set(files)):
        found.append((UNGUARDED, LIST_NOT_A_FILE.format(path=path)))
    if base is not None:
        added = sorted(set(head) - set(base))
        for path in added:
            found.append((UNGUARDED, LIST_ADDED.format(path=path)))
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


def prepare(root, kills):
    """`(finding, None)` for a function whose line cannot be run, or
    `(None, (path, old, new))`.

    Reads: owned — the function's `Kills:` text, in the grammar this module defines; unknown refused
    """
    if kills is None:
        return NO_LINE, None
    try:
        path, old, new = parse_kills(kills)
    except ValueError as error:
        return BAD_LINE.format(why=error), None
    if not os.path.isfile(os.path.join(root, path)):
        return NO_FILE.format(path=path), None
    return None, (path, old, new)


def judge(nodeid, code, verdict, output):
    """`(finding, None)` or `(None, proof)` for the function `nodeid`, from
    the one run of its file under its mutant.

    Reads: observed — mutation-check's exit and pytest's summary lines in its output; unknown refused
    """
    if code == SURVIVED:
        return NOT_KILLED, None
    if code != RED:
        return NOTHING.format(verdict=verdict), None
    killers = failed_ids(output)
    own = [k for k in killers if k == nodeid or k.startswith(nodeid + "[")]
    rest = [k for k in killers if k not in own]
    if not own:
        return NOT_OWN.format(killers=", ".join(rest) or NO_KILLER), None
    if rest:
        return SHARED.format(killers=", ".join(rest)), None
    return None, PROVED


def file_run(root, file, runner, timeout):
    """`(exit, seconds, first line)` of the test file run once as it stands.

    Reads: observed — the exit of the cases' runner and its first output line; unknown refused
    """
    started = time.monotonic()
    try:
        done = subprocess.run(
            [*runner, file, *TAIL],
            cwd=root,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=max(timeout, 1),
        )
    except subprocess.TimeoutExpired:
        return None, time.monotonic() - started, "timed out"
    lines = (done.stdout + done.stderr).strip().splitlines()
    return done.returncode, time.monotonic() - started, lines[-1] if lines else ""


def check(root, baseline, runner, bound):
    """`(exit, lines)` for the tree at `root` against `baseline`.

    Reads: observed — the root's tracked test files and list at HEAD and at the merge base, through git; unknown refused
    """
    merge_base = (git(root, "merge-base", baseline, "HEAD") or "").strip()
    if not merge_base:
        return 2, [
            f"case-check: nothing compared — no merge base of `{baseline}` and HEAD"
        ]
    list_path = os.path.join(root, UNGUARDED)
    head_list = []
    if os.path.exists(list_path):
        try:
            with open(list_path, encoding="utf-8") as handle:
                head_list = read_list(handle.read())
        except OSError as error:
            return 2, [
                f"case-check: nothing compared — `{UNGUARDED}`: {error.strerror}"
            ]
    base_text = git(root, "show", f"{merge_base}:{UNGUARDED}")
    base_list = None if base_text is None else read_list(base_text)
    files = tracked_test_files(root)
    findings = list_findings(head_list, base_list, files)
    proved, pending = [], {}
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
        for name, (node, text) in head.items():
            fid = f"{file}::{name}"
            try:
                kills = kills_text(source, node)
            except ValueError as error:
                findings.append((fid, str(error)))
                continue
            if name not in base or base[name][1] != text:
                finding, mutant = prepare(root, kills)
                if finding:
                    findings.append((fid, finding))
                else:
                    pending.setdefault(file, []).append((fid, mutant))
            elif file not in head_list:
                if kills is None:
                    findings.append((fid, OFF_THE_LIST))
                    continue
                try:
                    parse_kills(kills)
                except ValueError as error:
                    findings.append((fid, BAD_LINE.format(why=error)))
    started, limit = time.monotonic(), bound * 60
    for file, mutants in pending.items():
        left = limit - (time.monotonic() - started)
        code, each, verdict = file_run(root, file, runner, left)
        need = each * len(mutants)
        if code is None or each + need > left:
            restructure = RESTRUCTURE.format(
                count=len(mutants), need=need, each=each, left=left, bound=bound
            )
            findings.append((file, restructure))
            continue
        if code != 0:
            findings.append((file, FAILS_AS_IT_STANDS.format(verdict=verdict)))
            continue
        for fid, (path, old, new) in mutants:
            left = limit - (time.monotonic() - started)
            run = mutation_run(
                root, path, old, new, [*runner, file, *TAIL], max(left, 1), True
            )
            finding, proof = judge(fid, *run)
            if finding:
                findings.append((fid, finding))
            else:
                proved.append((fid, proof))
    lines = [
        f"case-check against {baseline}: {len(proved)} proved, {len(findings)} named"
    ]
    lines += [f"  {where}: {proof}" for where, proof in proved]
    lines += [f"  {where}: {finding}" for where, finding in findings]
    return (1 if findings else 0), lines


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
    code, lines = check(root, args.baseline, shlex.split(args.runner), args.bound)
    text = "\n".join(lines) + "\n"
    sys.stdout.write(text)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as handle:
            handle.write("### case-check\n\n```\n" + text + "```\n")
    return code


if __name__ == "__main__":
    sys.exit(main())
