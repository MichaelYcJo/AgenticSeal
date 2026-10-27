#!/usr/bin/env python3
"""seal fold — hold the policy root's documents to one read and one index.

`skills/settle/SKILL.md` gives a document one read and the policy root one
index. This is the reader of both, shipped (#566, #953).

  seal fold                      every check, with the values seal/config.md states
  seal fold --ceiling N          report documents past N estimated tokens, this run
  seal fold --root DIR           a repository other than this one

The policy root is `seal/config.md`'s `Policy root` row, `docs` when absent,
read through `hooks/config.py#policy_root`, and every check reads its top
level alone.

**One read.** Each document whose estimate (`tokens`) is past the `Document
token ceiling` row is named as one to split along its own headings. That is a
report and never a failure: the estimate is a guess from bytes, and a
document past one tool's per-call cap is still read in more calls (the
owner's answer of 2026-10-20).

**One index.** Where `<policy root>/README.md` exists, each other top-level
document is named on exactly one row of its tables, and every row names one.

**What it cannot read.** Size and naming are all it checks. Whether a
document is true, or whether two contradict each other, stays review's.

**It sets no value.** The repository states the values as rows of
`seal/config.md`, read through `hooks/config.py#config_rows`, and
`templates/setup/config.md` *The fold's values* states each row once. An absent
row means *not declared*, as every optional row of that file does: the check
it governs is not run, and the output says so in one line rather than
refusing. A flag overrides its row for one run.

Live lines and table rows come from
`skills/verify/scripts/unverified_check.py` (`live_lines`, `gfm_lines`,
`split_row`), loaded rather than re-spelled (#664).

Typed with no `--root`, it reads the repository the current directory is in,
so a run from a subdirectory checks that repository and not nothing.

Exit codes: 0 nothing found, including the run where nothing is declared and
one that names documents past the ceiling · 1 an index out of step, each
problem on a line of its own · 2 the root, a value or a file it had to read
was unusable, such as a document that is not UTF-8, and no result was
printed, or a sibling script it loads is not beside it. An interpreter below
the floor never reaches this file through `seal fold`: `hooks/launch.py`
refuses `seal` with 2 first.
"""

import argparse
import importlib.util
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
READER = os.path.join(HERE, "..", "..", "verify", "scripts", "unverified_check.py")
CONFIG_READER = os.path.join(HERE, "..", "..", "..", "hooks", "config.py")
OPTIN = os.path.join(HERE, "..", "..", "..", "hooks", "optin.py")

CONFIG = "config.md"
INDEX = "README.md"

# The `seal/config.md` rows this reads, each optional.
CEILING_ROW = "Document token ceiling"
POLICY_ROW = "Policy root"
ROWS = (CEILING_ROW, POLICY_ROW)
WHOLE = re.compile(r"[0-9]+")
# The estimate's one constant, a token taken as two bytes of UTF-8;
# `templates/setup/config.md` *The fold's values* states it.
BYTES_PER_TOKEN = 2


def load(path, name, purpose):
    """Import a sibling script by path, or refuse with a sentence that says
    what the missing file is for — `purpose` — rather than one reason for
    every file (round 1, note 7).

    The refusal is exit 2, written to stderr: nothing about the tree has been
    read, which is what 2 means here, and 1 is a problem found in `docs/`.
    It used to be `SystemExit(<sentence>)`, and a string argument exits 1, so
    a copy missing its sibling read as a finding (#590)."""
    if not os.path.isfile(path):
        sys.stderr.write(
            f"seal fold: cannot read {path}, and {purpose}. This command "
            "ships beside it in the plugin; a copy of one script taken on its "
            "own is not a plugin. Nothing was read.\n"
        )
        raise SystemExit(2)
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        sys.stderr.write(f"seal fold: cannot load {path}, and {purpose}.\n")
        raise SystemExit(2)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_loaded = {}


def reader():
    """`unverified_check.py`, loaded once on first use."""
    if "reader" not in _loaded:
        _loaded["reader"] = load(
            READER,
            "agentic_unverified_reader_for_folds",
            "it is where a document's lines and table rows are read from",
        )
    return _loaded["reader"]


class Unusable(Exception):
    """A row whose value will not parse, or a file the run had to read and
    could not (exit 2, no result printed)."""


# --- one read and one index --------------------------------------------------


def tokens(text):
    """The estimate: TEXT's UTF-8 bytes over `BYTES_PER_TOKEN`, rounded up."""
    return -(-len(text.encode("utf-8")) // BYTES_PER_TOKEN)


def documents(root, policy):
    """Every top-level `.md` of the directory POLICY, repo-relative with `/`,
    in name order."""
    top = os.path.join(root, *policy.split("/"))
    return [
        f"{policy}/{name}"
        for name in sorted(os.listdir(top))
        if name.endswith(".md") and os.path.isfile(os.path.join(top, name))
    ]


def why(error):
    """A reader's reason, in the few words a person acts on."""
    if isinstance(error, UnicodeDecodeError):
        return "not UTF-8"
    if isinstance(error, SyntaxError):
        return f"SyntaxError at line {error.lineno}"
    return type(error).__name__


def read(root, rel):
    """A document's text, or `Unusable` naming it (round 1, finding 2)."""
    try:
        with open(os.path.join(root, *rel.split("/")), encoding="utf-8") as f:
            return f.read()
    except (OSError, ValueError) as unreadable:
        raise Unusable(
            f"{rel} could not be read as text ({why(unreadable)})"
        ) from unreadable


def past_ceiling(root, policy, ceiling):
    """`[(document, estimate)]` for each top-level document of POLICY whose
    estimate is past CEILING."""
    found = [(rel, tokens(read(root, rel))) for rel in documents(root, policy)]
    return [(rel, count) for rel, count in found if count > ceiling]


def past_ceiling_lines(found, ceiling):
    """The report a person reads for `past_ceiling`'s answer, one line each."""
    return [
        f"{rel} is about {count} tokens, past the ceiling of {ceiling}: split "
        "it along its own headings"
        for rel, count in found
    ]


def index_problems(root, policy):
    """What is out of step in `<policy>/README.md`, or None where it is absent.

    Each row of its tables after the header names the documents it is about
    as backticked paths, and each other top-level document of POLICY is named
    on exactly one row."""
    index = f"{policy}/{INDEX}"
    if not os.path.isfile(os.path.join(root, *index.split("/"))):
        return None
    uc = reader()
    names = [rel for rel in documents(root, policy) if rel != index]
    rows, problems, in_table = {}, [], False
    lines = uc.live_lines(uc.gfm_lines(read(root, index)))
    for number, (line, live) in enumerate(lines, 1):
        cells = uc.split_row(line) if live else None
        if cells is None or not in_table or uc.is_separator(cells):
            in_table = cells is not None
            continue
        named = {t for t in re.findall(r"`([^`]+)`", line) if t in names}
        if not named:
            problems.append(f"{index}:{number} names no document of {policy}/")
        for rel in named:
            rows[rel] = rows.get(rel, 0) + 1
    for rel in names:
        if not rows.get(rel):
            problems.append(f"{index} has no row naming {rel}")
        elif rows[rel] > 1:
            problems.append(f"{index} names {rel} on {rows[rel]} rows")
    return problems


# --- the rows --------------------------------------------------------------


def optin():
    """`hooks/optin.py`, the one resolver, loaded once on first use."""
    if "optin" not in _loaded:
        _loaded["optin"] = load(
            OPTIN,
            "agentic_optin_for_folds",
            "it is what finds the repository's seal/ root",
        )
    return _loaded["optin"]


def located(root):
    """`(home, where)`: the `seal/` root of the repository at `root`, or ""
    where it has none, and the words that name where its rows were read.

    Through `hooks/optin.py#home_at`, the way `settle.py#main` reaches it:
    `<root>/seal/`, else the common git directory's `seal/`. `home_at`
    answers "" for two states, and they are given two sentences, because
    one was false for the other: a repository that opted out HAS a root, and
    settle met the same defect as its own round 2 finding 7 (round 1,
    finding 3)."""
    resolver = optin()
    common = resolver.git_common_dir(root)
    home = resolver.home_at(root, common)
    if home:
        return home, os.path.join(home, CONFIG)
    if common and os.path.isfile(os.path.join(common, resolver.SCRATCH)):
        return "", (
            f"{root}, which has opted out — `{resolver.SCRATCH}` is under its "
            "git directory, so its seal/config.md is not read"
        )
    return "", f"{root}, which has no seal/ root at either place"


def seal_home(root):
    """The `seal/` root of the repository at `root`, or "" where it has none
    or opted out."""
    return located(root)[0]


def config_reader():
    """`hooks/config.py`, the one reader of `seal/config.md`, or exit 2."""
    return load(
        CONFIG_READER,
        "agentic_config_for_folds",
        "it is what reads the rows of seal/config.md",
    )


def config_rows(home):
    """Every `| Item | Value |` row of `<home>/config.md` the table walker
    read, through the one table reader, `hooks/config.py#config_table`. No
    root and no file are no row at all; a file that is there and will not
    read is `Unusable`, in the reader's own sentence (#867), because reading
    it as no row turned every check this command runs off at exit 0.

    **A table the walker refused is `Unusable` where it did not read one of
    the rows this command reads** (#871), in the walker's sentence: an
    unread row may be written below the line it stopped at, so it is not
    absent, and reading it as absent is the same exit 0 an unreadable file
    gave. A refusal below all of them touches none of them, unless one of
    them is written again below it: `config_value` gives that row no value,
    and neither does this command."""
    if not home:
        return []
    reader = config_reader()
    text, refused = reader.config_text(home)
    if refused is not None:
        raise Unusable(refused)
    if text is None:
        return []
    rows, refusals = reader.config_table(text)
    read = {item for _index, item, _value in rows}
    if refusals and not set(ROWS) <= read:
        raise Unusable(f"the file {refusals[0]}")
    for item in ROWS if refusals else ():
        refused = reader.config_value(text, item)[1]
        if refused is not None:
            raise Unusable(refused)
    return [(item, value) for _index, item, value in rows]


def declared(home):
    """`(ceiling, policy root)` as the root's `config.md` states them, None
    for a ceiling row that is absent or empty, or `Unusable` naming the row.
    Each value is the reader's own answer, `hooks/config.py#value_of`, so a
    row written twice is `Unusable` rather than its first (#867); the policy
    root is `hooks/config.py#policy_root`'s."""
    rows = config_rows(home)
    reader = config_reader()

    def stated(item):
        value, refused = reader.value_of(rows, item)
        if refused is not None:
            raise Unusable(refused)
        return value or None

    ceiling = stated(CEILING_ROW)
    if ceiling is not None:
        if not WHOLE.fullmatch(ceiling) or int(ceiling) < 1:
            raise Unusable(
                f"the `{CEILING_ROW}` row holds `{ceiling}`, which is not a "
                "positive whole number of tokens"
            )
        ceiling = int(ceiling)
    stated(POLICY_ROW)
    return ceiling, reader.policy_root(home)


# --- the command -----------------------------------------------------------


def positive(text):
    value = int(text)
    if value < 1:
        raise argparse.ArgumentTypeError(f"{text} is not a positive integer")
    return value


def plural(count, word):
    return f"{count} {word}" if count == 1 else f"{count} {word}s"


def run(root, values, where, out):
    """Every check over `root`, the lines they print, and the problems.

    `where` names what the values were read from, for the line that says a
    check was not run because nothing declared its value."""
    ceiling, policy = values
    names = documents(root, policy)
    if ceiling is None:
        out.write(
            f"seal fold: `{CEILING_ROW}` is not declared in {where}, so no "
            "document's length was checked\n"
        )
    else:
        past = past_ceiling(root, policy, ceiling)
        out.write(
            f"seal fold: held {plural(len(names), 'document')} under {policy}/ "
            f"to {ceiling} estimated tokens, {len(past)} past it\n"
        )
        for line in past_ceiling_lines(past, ceiling):
            out.write(f"seal fold: {line}\n")
    found = index_problems(root, policy)
    if found is None:
        out.write(f"seal fold: there is no {policy}/{INDEX}, so no index was checked\n")
    elif not found:
        out.write(f"seal fold: the index {policy}/{INDEX} names every document\n")
    return found or []


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="seal fold",
        description="Hold the policy root's documents to one read and one "
        "index, with the values seal/config.md states.",
    )
    ap.add_argument("--root", help="the repository to read (default: cwd)")
    ap.add_argument(
        "--ceiling",
        type=positive,
        metavar="N",
        help=f"report each top-level document past N estimated tokens, for "
        f"this run only, over the `{CEILING_ROW}` row",
    )
    args = ap.parse_args(argv)

    root = os.path.abspath(args.root or os.getcwd())
    if not os.path.isdir(root):
        sys.stderr.write(
            f"seal fold: {root} is not a directory — nothing was checked\n"
        )
        return 2
    if args.root is None:
        # Typed anywhere inside a repository, the command reads that
        # repository, the way `seal.py` and `chain_check.py` resolve theirs.
        # Read from the directory it was typed in, a subdirectory has no
        # `seal/` and no `docs/`, and the run passed having checked nothing
        # (round 1, finding 1).
        root = optin().repo_root(root) or root
    home, where = located(root)
    try:
        ceiling, policy = declared(home)
    except Unusable as refused:
        sys.stderr.write(f"seal fold: in {where}, {refused} — nothing was checked\n")
        return 2
    if args.ceiling is not None:
        ceiling = args.ceiling
    index = os.path.join(root, *policy.split("/"), INDEX)
    if ceiling is None and not os.path.isfile(index):
        sys.stdout.write(
            f"seal fold: `{CEILING_ROW}` is not declared in {where}, and there "
            f"is no {policy}/{INDEX}, so nothing was checked\n"
        )
        return 0
    if not os.path.isdir(os.path.join(root, *policy.split("/"))):
        sys.stderr.write(
            f"seal fold: {root} has no {policy}/ directory — nothing was checked\n"
        )
        return 2
    # The run's lines are held until it has a result, so a file it cannot read
    # stops it with nothing on stdout that reads as one (round 1, finding 2).
    out = io.StringIO()
    try:
        problems = run(root, (ceiling, policy), where, out)
    except Unusable as refused:
        sys.stderr.write(f"seal fold: {refused} — no result was printed\n")
        return 2
    sys.stdout.write(out.getvalue())
    for problem in problems:
        sys.stdout.write(problem + "\n")
    return 1 if problems else 0


if __name__ == "__main__":
    # The console's encoding is not UTF-8 everywhere — cp1252 on Windows —
    # and every line this prints carries an em dash, so stdio is reconfigured
    # before `main()`, as every other shipped script does (found by CI's
    # `windows-latest` leg after the seal).
    for _name, _errors in (
        ("stdin", "replace"),
        ("stdout", "replace"),
        ("stderr", "backslashreplace"),
    ):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)
    sys.exit(main())
