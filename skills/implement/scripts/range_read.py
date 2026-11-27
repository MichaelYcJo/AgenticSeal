#!/usr/bin/env python3
"""seal range: the read a builder makes of its range and of the work item's
records before it closes a phase or a fix pass, printed into one file.

  seal range <item> --from <commit> --out <file>

`<item>` is the work item's directory, `--from` the commit the range starts
after, and `--out` the file the command writes, replacing what it held.

The file opens with the line `RANGE_LINE`, both commits as full hashes. Then
comes each path `git diff <from> <HEAD>` changes, in git's order, under a
line naming it:

- a `.md` path, each hunk with every line of HEAD's file from the blank
  line, or the file's start, before the hunk's first changed line to the
  blank line, or the file's end, after its last (`PROSE_HEAD`). git's
  function context reaches a code unit and stops short of a prose
  paragraph, and no `git diff` flag bounds a hunk at blank lines, so the
  command reads the hunks `-U0` prints and HEAD's text and draws the
  bound itself. Hunks whose paragraphs meet print as one, and each printed
  hunk carries a header in git's form with no function line after it;
- every other text path as `git diff -W` prints it (`WHOLE_HEAD`);
- a binary path and a deleted path named and not printed (`BINARY`,
  `DELETED`).

Then come the work item's records that state the present, `RECORDS`, each
whole as HEAD holds it under a line naming its path (`RECORD`), and one HEAD
does not hold is named as absent (`ABSENT`). No line is cut or wrapped.

To standard output it prints the range, the file's path with the number of
lines written (`WROTE`), each path it named and did not print
(`NOT_PRINTED`, `ABSENT`), and each tracked path with an uncommitted change,
which it names as not read (`NOT_READ`): the file holds HEAD's text, and
the change on disk is in it nowhere.

It judges nothing. Whether a printed statement is one HEAD contradicts is
the builder's reading of the file, and the next round's.

Edge cases, stated here and held by no other text:

- A line is read as git numbers it, ended by LF alone. A line is blank where
  it holds nothing but spaces, tabs and a carriage return. A prose file
  with no blank line, one long table for instance, prints whole from the
  hunk to its edges: the cost is a longer file, never a missed line.
- A hunk that only deletes is bounded from the line of HEAD before the
  deletion, or from the file's first line where the deletion opens the
  file. A `.md` path HEAD holds empty prints the hunks `-U0` gives, as git
  prints them.
- A rename is read as git reads one with `--no-renames`: the old path
  deleted and the new one added, which prints whole.
- In local mode the records stand under the common git directory, which no
  commit holds, so they are read on disk and their line says so
  (`ON_DISK`, `ABSENT_ON_DISK`); the range itself is still read from git.
- Each git command is built by `lib/gitcmd.py#argv`, a pathspec is read
  literally, each path is taken from `-z` output, and an external diff, a
  textconv filter, colour and git's joining of nearby hunks are switched
  off, so a configuration cannot put text into what the command prints or
  reads. It writes nothing but `--out`, reads no transcript and reaches no
  network.

Exit: 0 the file is written. 2 nothing is written: an argument is missing,
`<item>` is not a directory directly under the work items of a marked
root, `--from` does not resolve to a commit or is not an ancestor of HEAD,
a git command did not answer or exited non-zero, or the file could not be
written; the line on stderr names which. It has no other exit, because it
judges nothing.
"""

import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(HERE, "..", "..", "..", "lib")

# `lib/sibling.py` loads every other module this command reads. Where it is
# absent, the refusal is its own sentence about itself, spelt here because
# the file that holds the sentence is the one missing.
sys.path.insert(0, LIB)
try:
    import sibling
except ImportError:
    sys.stderr.write(
        "cannot read "
        + os.path.normpath(os.path.join(LIB, "sibling.py"))
        + ", which this command loads. It ships in the plugin beside this "
        "script; a copy of one script taken on its own is not a plugin. "
        "Nothing was read.\n"
    )
    raise SystemExit(2) from None

console = sibling.load("lib/console.py")
gitcmd = sibling.load("lib/gitcmd.py")
optin = sibling.load("lib/optin.py")
routing = sibling.load("lib/routing.py")

# The records of a work item that state the present, in the order the file
# prints them.
RECORDS = (
    routing.FILENAME,
    optin.DESIGN,
    optin.PLAN,
    optin.QUESTIONS,
    optin.GAPS,
    optin.CHANGELOG,
)

# The paths printed a paragraph at a time.
PROSE = ".md"

# Every pathspec is a path, never a pattern.
LITERAL = {"GIT_LITERAL_PATHSPECS": "1"}

# The options of every `git diff` the command runs.
DIFF = ("diff", "--no-color", "--no-ext-diff", "--no-textconv", "--no-renames")

# A hunk header as `git diff` prints it, the function line after it unread.
HUNK = re.compile(r"@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")

RANGE_LINE = "range: {start}..{head}"
PROSE_HEAD = "==> {path}: each hunk with its paragraph at HEAD <=="
WHOLE_HEAD = "==> {path}: git diff -W <=="
BINARY = "==> {path}: binary, not printed <=="
DELETED = "==> {path}: deleted, not printed <=="
RECORD = "==> {path}: whole at HEAD <=="
ABSENT = "==> {path}: not at HEAD <=="
ON_DISK = "==> {path}: whole on disk, since the root is local <=="
ABSENT_ON_DISK = "==> {path}: not on disk, since the root is local <=="

SUMMARY = "seal range: {start}..{head}"
WROTE = "wrote: {out}, {lines} lines"
NOT_PRINTED = "not printed: {path}, {why}"
NOT_READ = "not read: {path} has an uncommitted change, which the file does not hold"


class Refused(Exception):
    """An input the command cannot read a range from; its one line names
    why."""


def _git(root, *args):
    """What git printed for ARGS in ROOT, a pathspec read literally;
    `lib/gitcmd.py#Exited` for a non-zero exit."""
    return gitcmd.git(root, *args, env=LITERAL, check=True).stdout


def _fields(out):
    """The NUL-ended fields of OUT, git's `-z` output."""
    return [field for field in out.split("\0") if field]


def _lines(text):
    """TEXT's lines as git numbers them, ended by LF alone, with no empty
    line after a final LF."""
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    return lines


def _blank(line):
    return line.strip(" \t\r") == ""


def _work_item(item, cwd):
    """`(root, directory, rel)`: the repository ITEM's range is read in,
    ITEM's real path, and its `/`-joined path in the tree, or None where
    the root is local. `Refused` where ITEM is not a directory directly
    under the work items of a marked root."""
    if not os.path.isdir(item):
        raise Refused(f"{item} is not a directory")
    full = os.path.realpath(item)
    # A local-mode item sits under the common git directory, where git finds
    # no checkout, so its repository is the working directory's.
    root = optin.repo_root(full) or optin.repo_root(cwd)
    home = optin.home_at(root)
    if not home or os.path.dirname(full) != os.path.realpath(
        os.path.join(home, optin.WORK_ITEMS)
    ):
        raise Refused(
            f"{item} is not a work item's directory: one directly under "
            f"`{optin.WORK_ITEMS}/` of a marked records root"
        )
    if not optin.home_name(root):
        return root, full, None
    rel = os.path.relpath(full, os.path.realpath(root))
    return root, full, gitcmd.git_path(rel)


def _commit(root, name):
    """The full hash of the commit NAME resolves to in ROOT; `Refused`
    where it resolves to none."""
    done = gitcmd.git(
        root,
        "rev-parse",
        "--verify",
        "--quiet",
        "--end-of-options",
        f"{name}^{{commit}}",
    )
    if done.returncode:
        raise Refused(f"--from {name} does not resolve to a commit")
    return done.stdout.strip()


def _ancestor(root, start, head):
    """`Refused` where START is not an ancestor of HEAD."""
    done = gitcmd.git(root, "merge-base", "--is-ancestor", start, head)
    if done.returncode == 1:
        raise Refused(f"--from {start} is not an ancestor of HEAD, {head}")
    if done.returncode:
        raise gitcmd.Exited(
            ["git", "merge-base", "--is-ancestor", start, head],
            done.returncode,
            done.stderr,
        )


def _changed(root, start, head):
    """`[(path, status)]` of each path the range changes, in git's order."""
    fields = _fields(_git(root, *DIFF, "--name-status", "-z", start, head))
    return list(zip(fields[1::2], fields[0::2], strict=True))


def _binary(root, start, head):
    """The paths the range changes that git reads as binary."""
    held = set()
    for field in _fields(_git(root, *DIFF, "--numstat", "-z", start, head)):
        added, deleted, path = field.split("\t", 2)
        if added == "-" and deleted == "-":
            held.add(path)
    return held


def _hunks(lines):
    """`(header, hunks)` of LINES, what `git diff -U0` printed for one
    path: the lines before the first hunk, and each hunk as the list
    `[old_start, old_count, new_start, new_count, body]`."""
    header, hunks = [], []
    for line in lines:
        found = HUNK.match(line)
        if found:
            old, old_count, new, new_count = found.groups()
            hunks.append(
                [
                    int(old),
                    1 if old_count is None else int(old_count),
                    int(new),
                    1 if new_count is None else int(new_count),
                    [],
                ]
            )
        elif hunks:
            hunks[-1][4].append(line)
        else:
            header.append(line)
    return header, hunks


def _at(start, count):
    """One side of a hunk header, as git writes it."""
    if count == 0:
        return f"{start - 1},0"
    return str(start) if count == 1 else f"{start},{count}"


def _paragraphs(new, hunks):
    """The lines that print HUNKS, `_hunks`'s, against NEW, HEAD's lines of
    the path: each hunk widened to the blank lines around it, hunks whose
    paragraphs meet joined, each joined hunk under a header in git's form."""
    count = len(new)
    spans = []
    for hunk in hunks:
        _old, _old_count, start, length, _body = hunk
        if length:
            first, last = start, start + length - 1
        else:
            first = last = max(start, 1)
        while first > 1 and not _blank(new[first - 2]):
            first -= 1
        while last < count and not _blank(new[last]):
            last += 1
        if spans and first <= spans[-1][1] + 1:
            spans[-1][1] = max(spans[-1][1], last)
            spans[-1][2].append(hunk)
        else:
            spans.append([first, last, [hunk]])
    printed, moved = [], 0
    for first, last, held in spans:
        grown = sum(length - old_count for _o, old_count, _s, length, _b in held)
        size = last - first + 1
        printed.append(f"@@ -{_at(first - moved, size - grown)} +{_at(first, size)} @@")
        at = first
        for _old, _old_count, start, length, body in held:
            upto = start - 1 if length else start
            printed += [" " + line for line in new[at - 1 : upto]]
            printed += body
            at = start + length if length else start + 1
        printed += [" " + line for line in new[at - 1 : last]]
        moved += grown
    return printed


def _prose(root, start, head, path):
    """The lines that print PATH's hunks, each with its paragraph at HEAD."""
    printed = _lines(
        _git(root, *DIFF, "-U0", "--inter-hunk-context=0", start, head, "--", path)
    )
    new = _lines(_git(root, "cat-file", "blob", f"{head}:{path}"))
    if not new:
        return printed
    header, hunks = _hunks(printed)
    return header + _paragraphs(new, hunks)


def _diff(root, start, head, path, context):
    """The lines `git diff CONTEXT` prints for PATH."""
    return _lines(_git(root, *DIFF, context, start, head, "--", path))


def _records(root, head, item, rel):
    """`(lines, absent)`: the lines that print the work item's records whole,
    and the path of each one not there."""
    lines, absent = [], []
    if rel is None:
        for name in RECORDS:
            path = os.path.join(item, *name.split("/"))
            shown = gitcmd.git_path(os.path.relpath(path, root))
            try:
                with open(path, encoding="utf-8", errors="replace", newline="") as f:
                    text = f.read()
            except FileNotFoundError:
                lines.append(ABSENT_ON_DISK.format(path=shown))
                absent.append(shown)
                continue
            lines += [ON_DISK.format(path=shown), *_lines(text)]
        return lines, absent
    paths = [f"{rel}/{name}" for name in RECORDS]
    held = set(
        _fields(_git(root, "ls-tree", "-r", "-z", "--name-only", head, "--", *paths))
    )
    for path in paths:
        if path not in held:
            lines.append(ABSENT.format(path=path))
            absent.append(path)
            continue
        text = _git(root, "cat-file", "blob", f"{head}:{path}")
        lines += [RECORD.format(path=path), *_lines(text)]
    return lines, absent


def _uncommitted(root):
    """Each tracked path in ROOT with a change no commit holds, staged or
    not."""
    out = _git(
        root, "status", "--porcelain=v1", "-z", "--no-renames", "--untracked-files=no"
    )
    return [field[3:] for field in _fields(out)]


def _read(item, start, cwd):
    """`(text, summary)`: the file's text, and the summary's lines but the
    one `WROTE` gives, which `main` prints second once the file is written,
    for the range from START to HEAD and the work item ITEM, read from CWD.
    `Refused` or `lib/gitcmd.py#Failed` where no file can be written."""
    root, full, rel = _work_item(item, cwd)
    head = _commit(root, "HEAD")
    start = _commit(root, start)
    _ancestor(root, start, head)
    lines, summary = [RANGE_LINE.format(start=start, head=head)], []
    binary = _binary(root, start, head)
    for path, status in _changed(root, start, head):
        if status == "D":
            lines.append(DELETED.format(path=path))
            summary.append(NOT_PRINTED.format(path=path, why="deleted"))
        elif path in binary:
            lines.append(BINARY.format(path=path))
            summary.append(NOT_PRINTED.format(path=path, why="binary"))
        elif path.endswith(PROSE):
            lines += [PROSE_HEAD.format(path=path), *_prose(root, start, head, path)]
        else:
            lines += [
                WHOLE_HEAD.format(path=path),
                *_diff(root, start, head, path, "-W"),
            ]
    records, absent = _records(root, head, full, rel)
    lines += records
    summary += [NOT_PRINTED.format(path=path, why="absent") for path in absent]
    summary += [NOT_READ.format(path=path) for path in _uncommitted(root)]
    return "".join(line + "\n" for line in lines), [
        SUMMARY.format(start=start, head=head),
        *summary,
    ]


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="seal range",
        description="Print into one file every hunk of a range with the "
        "paragraph or unit around it, then the work item's records that "
        "state the present, whole.",
    )
    parser.add_argument("item", help="the work item's directory")
    parser.add_argument(
        "--from",
        dest="start",
        required=True,
        metavar="COMMIT",
        help="the commit the range starts after",
    )
    parser.add_argument(
        "--out", required=True, metavar="FILE", help="the file to write, replaced"
    )
    args = parser.parse_args(argv)
    try:
        text, summary = _read(args.item, args.start, os.getcwd())
    except Refused as refused:
        print(f"seal range: {refused}", file=sys.stderr)
        return 2
    except gitcmd.Failed as failed:
        print(f"seal range: {failed.line}", file=sys.stderr)
        return 2
    try:
        with open(args.out, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
    except OSError as exc:
        print(f"seal range: {args.out} could not be written ({exc})", file=sys.stderr)
        return 2
    print(summary[0])
    print(WROTE.format(out=args.out, lines=text.count("\n")))
    for line in summary[1:]:
        print(line)
    return 0


if __name__ == "__main__":
    console.to_utf8()
    sys.exit(main())
