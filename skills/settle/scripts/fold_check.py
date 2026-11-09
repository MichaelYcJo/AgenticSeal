#!/usr/bin/env python3
"""seal fold — hold the policy root's documents to one read and one index.

`skills/settle/SKILL.md` gives a document one read, and
`skills/settle/rule-changes.md` gives the policy root one index. This is the
reader of both, shipped (#566, #953).

  seal fold                      every check, with the values seal/config.json states
  seal fold --ceiling N          report documents past N estimated tokens, this run
  seal fold --root DIR           a repository other than this one

The policy root is `seal/config.json`'s `Policy root` key, `docs` when absent,
read through `lib/config.py#policy_root`. Every check reads its top
level and each of its groups: a directory directly in it that a row of the
index names a document of (`groups`). A directory the index names nothing
of, and anything below a group, is not read.

**One read.** Each document whose estimate (`tokens`) is past the `Document
token ceiling` key is named as one to split by who opens each section and at
which step. That is a report and never a failure: the estimate is a guess from bytes, and a
document past one tool's per-call cap is still read in more calls (the
owner's answer of 2026-10-20).

**One index.** Where `<policy root>/README.md` exists, each other document
is named on exactly one row of its tables, and every row names one.

**What it cannot read.** Size and naming are all it checks. Whether a
document is true, or whether two contradict each other, stays review's.

**It sets no value.** The repository states the values as keys of
`seal/config.json`, read through `lib/config.py#config_value`, and
`templates/setup/config.md` *The fold's values* states each key once. An
absent key means *not declared*, as every optional key of that file does:
the check it governs is not run, and the output says so in one line rather
than refusing. A flag overrides its key for one run.

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
the floor never reaches this file through `seal fold`: `lib/launch.py`
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
CONFIG_READER = os.path.join(HERE, "..", "..", "..", "lib", "config.py")
OPTIN = os.path.join(HERE, "..", "..", "..", "lib", "optin.py")

CONFIG = "config.json"
INDEX = "README.md"

# The `seal/config.json` keys this reads, each optional.
CEILING_KEY = "Document token ceiling"
POLICY_KEY = "Policy root"
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
    """A key whose value will not parse, or a file the run had to read and
    could not (exit 2, no result printed)."""


# --- one read and one index --------------------------------------------------


def tokens(text):
    """The estimate: TEXT's UTF-8 bytes over `BYTES_PER_TOKEN`, rounded up."""
    return -(-len(text.encode("utf-8")) // BYTES_PER_TOKEN)


def documents(root, policy):
    """Every `.md` directly in the directory POLICY or in one of its
    `groups`, repo-relative with `/`: the top level first, then each group,
    each in name order."""
    out = []
    for rel in [policy, *(f"{policy}/{group}" for group in groups(root, policy))]:
        top = os.path.join(root, *rel.split("/"))
        out += [
            f"{rel}/{name}"
            for name in sorted(os.listdir(top))
            if name.endswith(".md") and os.path.isfile(os.path.join(top, name))
        ]
    return out


def groups(root, policy):
    """Each directory directly in POLICY that a row of `<policy>/README.md`
    names a document of, as `<policy>/<group>/<name>.md`, in name order;
    none where the index is absent. A directory the index names nothing of
    is no group, and nothing below a group is one."""
    index = f"{policy}/{INDEX}"
    if not os.path.isfile(os.path.join(root, *index.split("/"))):
        return []
    one_deep = re.compile(re.escape(policy) + r"/([^/\\:]+)/[^/\\:]+\.md")
    named = set()
    for _number, paths in index_rows(root, index):
        for path in paths:
            found = one_deep.fullmatch(path)
            if found and found.group(1) not in (".", ".."):
                named.add(found.group(1))
    return sorted(
        group
        for group in named
        if os.path.isdir(os.path.join(root, *policy.split("/"), group))
    )


def index_rows(root, index):
    """`[(line number, backticked texts)]` for each row of the tables of the
    index at INDEX after the header and the separator."""
    uc = reader()
    rows, in_table = [], False
    lines = uc.live_lines(uc.gfm_lines(read(root, index)))
    for number, (line, live) in enumerate(lines, 1):
        cells = uc.split_row(line) if live else None
        if cells is None or not in_table or uc.is_separator(cells):
            in_table = cells is not None
            continue
        rows.append((number, re.findall(r"`([^`]+)`", line)))
    return rows


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
    """`[(document, estimate)]` for each document `documents` lists whose
    estimate is past CEILING."""
    found = [(rel, tokens(read(root, rel))) for rel in documents(root, policy)]
    return [(rel, count) for rel, count in found if count > ceiling]


def past_ceiling_lines(found, ceiling):
    """The report a person reads for `past_ceiling`'s answer, one line each."""
    return [
        f"{rel} is about {count} tokens, past the ceiling of {ceiling}: split "
        "it by who opens each section and at which step"
        for rel, count in found
    ]


def index_problems(root, policy):
    """What is out of step in `<policy>/README.md`, or None where it is absent.

    Each row of its tables after the header names the documents it is about
    as backticked paths, and each other document `documents` lists is named
    on exactly one row."""
    index = f"{policy}/{INDEX}"
    if not os.path.isfile(os.path.join(root, *index.split("/"))):
        return None
    names = [rel for rel in documents(root, policy) if rel != index]
    rows, problems = {}, []
    for number, paths in index_rows(root, index):
        named = {t for t in paths if t in names}
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


# --- the keys --------------------------------------------------------------


def optin():
    """`lib/optin.py`, the one resolver, loaded once on first use."""
    if "optin" not in _loaded:
        _loaded["optin"] = load(
            OPTIN,
            "agentic_optin_for_folds",
            "it is what finds the repository's seal/ root",
        )
    return _loaded["optin"]


def located(root):
    """`(home, where)`: the `seal/` root of the repository at `root`, or ""
    where it has none, and the words that name where its keys were read.

    Through `lib/optin.py#home_at`, the way `settle.py#main` reaches it:
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
            "git directory, so its seal/config.json is not read"
        )
    return "", f"{root}, which has no seal/ root at either place"


def seal_home(root):
    """The `seal/` root of the repository at `root`, or "" where it has none
    or opted out."""
    return located(root)[0]


def config_reader():
    """`lib/config.py`, the one reader of `seal/config.json`, or exit 2."""
    return load(
        CONFIG_READER,
        "agentic_config_for_folds",
        "it is what reads the keys of seal/config.json",
    )


def declared(home):
    """`(ceiling, policy root)` as the root's `config.json` states them,
    None for a ceiling key that is absent or empty, or `Unusable` naming
    what will not read. No root and no file are no key at all; a file
    `lib/config.py#config_pairs` refuses is `Unusable` in the reader's own
    sentence (#867), because reading it as no key turned every check this
    command runs off at exit 0. Each value is the reader's own answer,
    `lib/config.py#config_value`, so a key written twice is `Unusable`
    rather than one of the two; the policy root is
    `lib/config.py#policy_root`'s."""
    reader = config_reader()
    pairs, refused = reader.config_pairs(home)
    if refused is not None:
        raise Unusable(refused)

    def stated(key):
        value, refused = reader.config_value(pairs, key)
        if refused is not None:
            raise Unusable(refused)
        return value or None

    ceiling = stated(CEILING_KEY)
    if ceiling is not None:
        if not WHOLE.fullmatch(ceiling) or int(ceiling) < 1:
            raise Unusable(
                f"the `{CEILING_KEY}` key holds `{ceiling}`, which is not a "
                "positive whole number of tokens"
            )
        ceiling = int(ceiling)
    stated(POLICY_KEY)
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
            f"seal fold: `{CEILING_KEY}` is not declared in {where}, so no "
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
        "index, with the values seal/config.json states.",
    )
    ap.add_argument("--root", help="the repository to read (default: cwd)")
    ap.add_argument(
        "--ceiling",
        type=positive,
        metavar="N",
        help=f"report each document of the policy root or of one of its "
        f"groups past N estimated tokens, for "
        f"this run only, over the `{CEILING_KEY}` key",
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
            f"seal fold: `{CEILING_KEY}` is not declared in {where}, and there "
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
