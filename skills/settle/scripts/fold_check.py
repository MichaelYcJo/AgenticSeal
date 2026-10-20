#!/usr/bin/env python3
"""fold-check — hold the policy root's documents to their shape, one read
and one index.

`skills/settle/SKILL.md` gives a rule one shape, a document one read and the
policy root one index. This is the reader of all three, shipped (#566, #953).

  fold-check                     every check, with the values seal/config.md states
  fold-check --shape-from ID     bind the shape from this work-item id on, this run
  fold-check --ceiling N         report documents past N estimated tokens, this run
  fold-check --root DIR          a repository other than this one

The policy root is `seal/config.md`'s `Policy root` row, `docs` when absent,
read through `hooks/config.py#policy_root`, and every check reads its top
level alone.

**The shape.** Every statement whose marker group holds a work-item id at or
above the cutoff opens with a bold rule sentence and carries exactly one live
`Enforced by:` line, whose targets each resolve: a file inside the repository
and, with `::name`, a `def` or `class` it defines once, as pytest spells a node
id — `::Class::method` for a method — and resolved by the coordinate kernel,
`skills/verify/scripts/coordinates.py#named_unit`. Or the line says
`nothing — <why>`, with a reason. Ids are epoch-prefixed, so the cutoff is a
comparison and needs no list of exemptions, and `--shape-from 0` binds every
statement there is.

**One read.** Each document whose estimate (`tokens`) is past the `Document
token ceiling` row is named as one to split along its own headings. That is a
report and never a failure: the estimate is a guess from bytes, and a
document past one tool's per-call cap is still read in more calls (the
owner's answer of 2026-10-20).

**One index.** Where `<policy root>/README.md` exists, each other top-level
document is named on exactly one row of its tables, and every row names one.

**What it cannot read.** Presence, count and resolution are all it checks. It
cannot tell whether a target really enforces the rule, whether a statement is
true, or whether two statements contradict each other; those stay review's.

**It sets no value.** The repository states the values as rows of
`seal/config.md`, read through `hooks/config.py#config_rows`, and
`templates/config.md` §*The fold's values* states each row once. An absent
row means *not declared*, as every optional row of that file does: the check
it governs is not run, and the output says so in one line rather than
refusing. A flag overrides its row for one run, which is how a retrofit lists
every statement still missing the shape without editing the config first.

Markers, live lines and table rows come from
`skills/verify/scripts/unverified_check.py` (`live_lines`, `FOLD_MARKER`,
`gfm_lines`, `split_row`), loaded rather than re-spelled (#664).

Typed with no `--root`, it reads the repository the current directory is in,
so a run from a subdirectory checks that repository and not nothing.

Exit codes: 0 nothing found, including the run where nothing is declared and
one that names documents past the ceiling · 1 a statement out of shape or an
index out of step, each on a line of its own · 2 the root, a value or a
file it had to read was unusable — a document that is not UTF-8, a `::name`
target that will not parse — and no result was printed, or a sibling script it
loads is not beside it. An interpreter below the floor never reaches this file
through `bin/fold-check`: `hooks/launch.py` refuses it with 2 first.
"""

import argparse
import ast
import importlib.util
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
READER = os.path.join(HERE, "..", "..", "verify", "scripts", "unverified_check.py")
CONFIG_READER = os.path.join(HERE, "..", "..", "..", "hooks", "config.py")
OPTIN = os.path.join(HERE, "..", "..", "..", "hooks", "optin.py")
# The coordinate kernel, whose `named_unit` is the one resolver of a
# `path::name` target (#836), so `fold-check` and `rules --check` read an
# `Enforced by:` line in one grammar.
COORDINATES = os.path.join(HERE, "..", "..", "verify", "scripts", "coordinates.py")

CONFIG = "config.md"
INDEX = "README.md"

# The `seal/config.md` rows this reads, each optional.
SHAPE_ROW = "Fold shape from"
CEILING_ROW = "Document token ceiling"
POLICY_ROW = "Policy root"
ROWS = (SHAPE_ROW, CEILING_ROW, POLICY_ROW)
WHOLE = re.compile(r"[0-9]+")
# The estimate's one constant, a token taken as two bytes of UTF-8;
# `templates/config.md` §*The fold's values* states it.
BYTES_PER_TOKEN = 2

BOLD_OPENING = re.compile(r"^\*{2,3}[^*\s]")
ENFORCED = "Enforced by: "


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
            f"fold-check: cannot read {path}, and {purpose}. This command "
            "ships beside it in the plugin; a copy of one script taken on its "
            "own is not a plugin. Nothing was read.\n"
        )
        raise SystemExit(2)
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        sys.stderr.write(f"fold-check: cannot load {path}, and {purpose}.\n")
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
            "specseal_unverified_reader_for_folds",
            "it is where the fold's markers are read from",
        )
    return _loaded["reader"]


def coordinates():
    """`coordinates.py`, loaded once on first use, for `named_unit`."""
    if "coordinates" not in _loaded:
        _loaded["coordinates"] = load(
            COORDINATES,
            "specseal_coordinates_for_folds",
            "it is where a `path::name` target is resolved",
        )
    return _loaded["coordinates"]


class Unusable(Exception):
    """A row whose value will not parse, or a file the run had to read and
    could not (exit 2, no result printed)."""


# --- the shape -------------------------------------------------------------


def numbered_statements(text):
    """`[(marker ids, [(1-based line number, live line)])]`, in document order.

    Consecutive marker lines are one group. A statement runs from its markers
    to the next marker, the next heading or the end of the file. A heading is
    the one rule's, `unverified_check.py#heading_level` (#867), which this
    module spelled again as a pattern of its own."""
    uc = reader()
    found = []
    current = None
    previous_was_marker = False
    for number, (line, live) in enumerate(uc.live_lines(uc.gfm_lines(text)), 1):
        if not live:
            previous_was_marker = False
            continue
        ids = uc.FOLD_MARKER.findall(line)
        if ids:
            if previous_was_marker:
                current[0].extend(ids)
            else:
                current = (list(ids), [])
                found.append(current)
            previous_was_marker = True
            continue
        previous_was_marker = False
        if uc.heading_level(line) is not None:
            current = None
            continue
        if current is not None:
            current[1].append((number, line))
    return found


def statements(text):
    """`[(marker ids, the statement's live lines)]`, in document order."""
    return [
        (ids, [line for _number, line in lines])
        for ids, lines in numbered_statements(text)
    ]


def names_targets(value):
    """Whether an `Enforced by:` value is read as targets rather than as
    `nothing — <why>`. The shape check and `enforced_lines` both ask this, so
    the lines a wrap limit skips are exactly the lines read as paths."""
    return not value.startswith(reader().NOTHING.strip())


def enforced_lines(text):
    """The 1-based numbers of the lines this reader reads as a statement's
    `Enforced by:` line with targets, whatever the cutoff.

    A line of paths cannot be wrapped without ceasing to be one line, which
    is what the shape counts, so a wrap limit asks this which lines to skip.
    A `nothing — <why>` line is not among them: its reason is prose."""
    return [
        number
        for _ids, lines in numbered_statements(text)
        for number, line in lines
        if line.startswith(ENFORCED) and names_targets(line[len(ENFORCED) :].strip())
    ]


def bound(ids, cutoff):
    """Whether any id in the group is at or above the cutoff."""
    for work_item in ids:
        prefix = work_item.split("-", 1)[0]
        if prefix.isdigit() and int(prefix) >= cutoff:
            return True
    return False


def target_problem(root, target):
    """Why `target` does not resolve under `root`, or None when it does: a
    file inside the repository, or a `def` or `class` its Python file
    defines once."""
    target = target.strip().strip("`")
    if not target:
        return "an empty target"
    path, _, name = target.partition("::")
    # Both sides through `realpath`, so a symlink inside the root that opens
    # a file outside it is outside, and a root reached through one is itself.
    base = os.path.realpath(root)
    full = os.path.realpath(os.path.join(base, *path.split("/")))
    if os.path.commonpath([full, base]) != base:
        return f"{path} is not a path inside the repository"
    if not os.path.exists(full):
        return f"{path} does not exist"
    if not os.path.isfile(full):
        return f"{path} is not a file in the repository"
    if not name:
        return None
    if not path.endswith(".py"):
        return f"{target}: `::name` needs a Python file"
    try:
        with open(full, encoding="utf-8") as f:
            text = f.read()
        # The kernel's resolver (#836): `::A::b` is `b` inside `A`, as pytest
        # spells a method, and a name is looked up where it is defined rather
        # than anywhere in the file.
        kinds = coordinates().named_unit(text, name.split("::"))
        if kinds is None:
            ast.parse(text)
    except (OSError, ValueError, SyntaxError) as unreadable:
        # Not a problem with the statement and not a result: a target written
        # for a newer Python than this one does not parse here, and a file
        # that is not UTF-8 does not decode. Exit 1 means problems found, so
        # this goes to exit 2 by `Unusable`, never as a traceback (round 1,
        # finding 2). `ast.parse` runs only to name the line that will not.
        raise Unusable(
            f"names `{target}`, and {path} could not be read as Python "
            f"({why(unreadable)})"
        ) from unreadable
    if kinds is not None and len(kinds) > 1:
        # A name defined twice is no one unit — pytest collects the last
        # `def` — so a rule bound to it is not bound (#944).
        return (
            f"{target}: {name} is defined {len(kinds)} times in {path}, so it "
            "names no one unit"
        )
    if kinds is not None and ("def" in kinds or "class" in kinds):
        return None
    return f"{target}: no def or class named {name} in {path}"


def shape_problems(root, name, text, cutoff):
    """What is wrong with the shape of each bound statement in `text`."""
    problems = []
    for ids, lines in statements(text):
        if not bound(ids, cutoff):
            continue
        where = f"{name}: the statement under {ids}"
        body = [line for line in lines if line.strip()]
        if not body or not BOLD_OPENING.match(body[0]):
            problems.append(f"{where} does not open with a bold rule sentence")
        enforced = [line for line in lines if line.startswith(ENFORCED)]
        if len(enforced) != 1:
            problems.append(
                f"{where} carries {len(enforced)} `Enforced by:` lines, not one"
            )
            continue
        value = enforced[0][len(ENFORCED) :].strip()
        if not names_targets(value):
            if not value[len(reader().NOTHING.strip()) :].strip():
                problems.append(f"{where} says `nothing` and gives no reason")
            continue
        for target in value.split(","):
            try:
                problem = target_problem(root, target)
            except Unusable as refused:
                raise Unusable(f"{where} {refused}") from refused
            if problem:
                problems.append(f"{where}: {problem}")
    return problems


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
            "specseal_optin_for_folds",
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
        "specseal_config_for_folds",
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
    """`(cutoff, ceiling, policy root)` as the root's `config.md` states
    them, None for a value row that is absent or empty, or `Unusable` naming
    the row. Each value is the reader's own answer, `hooks/config.py#value_of`,
    so a row written twice is `Unusable` rather than its first (#867); the
    policy root is `hooks/config.py#policy_root`'s."""
    rows = config_rows(home)
    reader = config_reader()

    def stated(item):
        value, refused = reader.value_of(rows, item)
        if refused is not None:
            raise Unusable(refused)
        return value or None

    cutoff = stated(SHAPE_ROW)
    if cutoff is not None:
        if not WHOLE.fullmatch(cutoff):
            raise Unusable(
                f"the `{SHAPE_ROW}` row holds `{cutoff}`, which is not a "
                "work-item id's epoch prefix (a whole number; `0` binds every "
                "statement)"
            )
        cutoff = int(cutoff)
    ceiling = stated(CEILING_ROW)
    if ceiling is not None:
        if not WHOLE.fullmatch(ceiling) or int(ceiling) < 1:
            raise Unusable(
                f"the `{CEILING_ROW}` row holds `{ceiling}`, which is not a "
                "positive whole number of tokens"
            )
        ceiling = int(ceiling)
    stated(POLICY_ROW)
    return cutoff, ceiling, reader.policy_root(home)


# --- the command -----------------------------------------------------------


def positive(text):
    value = int(text)
    if value < 1:
        raise argparse.ArgumentTypeError(f"{text} is not a positive integer")
    return value


def not_negative(text):
    value = int(text)
    if value < 0:
        raise argparse.ArgumentTypeError(f"{text} is not a work-item id prefix")
    return value


def plural(count, word):
    return f"{count} {word}" if count == 1 else f"{count} {word}s"


def run(root, values, where, out):
    """Every check over `root`, the lines they print, and the problems.

    `where` names what the values were read from, for the line that says a
    check was not run because nothing declared its value."""
    cutoff, ceiling, policy = values
    names = documents(root, policy)
    problems = []
    if cutoff is None:
        out.write(
            f"fold-check: `{SHAPE_ROW}` is not declared in {where}, so the "
            "shape was not checked\n"
        )
    else:
        groups = bound_groups = 0
        for rel in names:
            text = read(root, rel)
            found = statements(text)
            groups += len(found)
            bound_groups += sum(1 for ids, _ in found if bound(ids, cutoff))
            problems += shape_problems(root, rel, text, cutoff)
        out.write(
            f"fold-check: read {plural(groups, 'statement')} in "
            f"{plural(len(names), 'document')} under {policy}/; the cutoff "
            f"{cutoff} binds {bound_groups}\n"
        )
    if ceiling is None:
        out.write(
            f"fold-check: `{CEILING_ROW}` is not declared in {where}, so no "
            "document's length was checked\n"
        )
    else:
        past = past_ceiling(root, policy, ceiling)
        out.write(
            f"fold-check: held {plural(len(names), 'document')} under {policy}/ "
            f"to {ceiling} estimated tokens, {len(past)} past it\n"
        )
        for line in past_ceiling_lines(past, ceiling):
            out.write(f"fold-check: {line}\n")
    found = index_problems(root, policy)
    if found is None:
        out.write(
            f"fold-check: there is no {policy}/{INDEX}, so no index was checked\n"
        )
    elif not found:
        out.write(f"fold-check: the index {policy}/{INDEX} names every document\n")
    return problems + (found or [])


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="fold-check",
        description="Hold the policy root's documents to their shape, one read "
        "and one index, with the values seal/config.md states.",
    )
    ap.add_argument("--root", help="the repository to read (default: cwd)")
    ap.add_argument(
        "--shape-from",
        type=not_negative,
        metavar="ID",
        help=f"bind the shape from this work-item id prefix on, for this run "
        f"only, over the `{SHAPE_ROW}` row; 0 binds every statement",
    )
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
            f"fold-check: {root} is not a directory — nothing was checked\n"
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
        cutoff, ceiling, policy = declared(home)
    except Unusable as refused:
        sys.stderr.write(f"fold-check: in {where}, {refused} — nothing was checked\n")
        return 2
    if args.shape_from is not None:
        cutoff = args.shape_from
    if args.ceiling is not None:
        ceiling = args.ceiling
    index = os.path.join(root, *policy.split("/"), INDEX)
    if cutoff is None and ceiling is None and not os.path.isfile(index):
        sys.stdout.write(
            f"fold-check: neither `{SHAPE_ROW}` nor `{CEILING_ROW}` is declared "
            f"in {where}, and there is no {policy}/{INDEX}, so nothing was "
            "checked\n"
        )
        return 0
    if not os.path.isdir(os.path.join(root, *policy.split("/"))):
        sys.stderr.write(
            f"fold-check: {root} has no {policy}/ directory — nothing was checked\n"
        )
        return 2
    # The run's lines are held until it has a result, so a file it cannot read
    # stops it with nothing on stdout that reads as one (round 1, finding 2).
    out = io.StringIO()
    try:
        problems = run(root, (cutoff, ceiling, policy), where, out)
    except Unusable as refused:
        sys.stderr.write(f"fold-check: {refused} — no result was printed\n")
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
