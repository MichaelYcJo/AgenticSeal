#!/usr/bin/env python3
"""Print the four numbers of `docs/release-checklist.md` step 2b, one row
per released work item routed through the review chain (#1223).

**A finding is counted once, by its own block.** The step counts, per work
item, its findings, the findings with a `regression:` or `reopens:` line,
the findings located in records alone, and its rounds. Each round record is
read through `skills/code-review/scripts/chain_check.py#record_findings`,
the reader the pull-request check holds a record to, and nothing here reads
the record's text by a pattern of its own. A finding is a `### <n>.
<symptom>` section that holds a finding block; its regression is that
block's `regression:` or `reopens:` line; and it is in records alone where
every path that block's `location:` names lies under `seal/threads/`
(`Finding.located`). A close block's `location:` names where the fix went,
not where the defect shows, so the count does not read it.

**The rows are the work items `seal settle` treats as released**: those
whose directory is present at `--released-at`
(`skills/settle/scripts/settle.py#released`, default `origin/main` as the
settle defaults it), that the tree still holds, and whose `routing.md`
parses with `Review` `through the review chain` (`hooks/lib/routing.py#parse`).
The rounds are `hooks/lib/routing.py#rounds`.

**An incomplete count is a wrong number**, the stance
`.github/scripts/release_seal.py#chain_counts` takes. A work item one of
whose records the reader refuses a line of, or that cannot be opened, reads
`not read` in its three finding cells, and its rounds cell holds the count.
A work item whose `trail/rounds/` cannot be listed reads `not read` in all
four. A released work item whose `routing.md` cannot be opened, or is no
declaration, is no row, since whether it went through the review chain is
not known. Under the table, one line names each record, directory or
`routing.md` not read, and why; a work item routed straight to the pull
request is no row and no line.

It ships to no user: this repository's settling session types it at step
2b and posts the table to the `flow-baseline` issue itself. It writes
nothing, posts nothing and fails nothing.

    python3 .github/scripts/finding_counts.py [--released-at REF] [--root DIR]

Exit codes: 0, the table was printed, whatever it shows; 2, the ref does not
resolve or a reader does not load, with the reason on stderr.
"""

import argparse
import importlib.util
import os
import sys

sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "..", "hooks", "lib"
    ),
)
import console

HERE = os.path.dirname(os.path.abspath(__file__))
# The repository this file is in, which the readers are loaded from and
# which `--root` defaults to.
CODE = os.path.abspath(os.path.join(HERE, "..", ".."))

HEADER = "| work item | findings | regression or reopens | records alone | rounds |"
SEPARATOR = "|---|---|---|---|---|"
NOT_READ = "not read"
DEFAULT_REF = "origin/main"
# Said of every state `hooks/lib/routing.py#rounds_unreadable` answers for,
# and so of none of them alone: any link, a path that is not a directory,
# and a directory nothing can list.
NOT_LISTED = (
    "the round records cannot be listed: it is a link, a file, or a "
    "directory nothing can list"
)
# Said of a released work item whose `routing.md` cannot be read or is no
# declaration: whether it is a row is not known, so it is none, and this
# line says so under the table.
NOT_ROUTED = "whether it went through the review chain is not read"
NO_DECLARATION = "it is no declaration `hooks/lib/routing.py#parse` reads"


def load(name, *parts):
    """The repository's module at `CODE/<parts>`, run under `name`."""
    path = os.path.join(CODE, *parts)
    spec = importlib.util.spec_from_file_location(name, path)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def readers():
    """`(routing, chain_check, the markdown reader, settle)`: the readers the
    review chain and the settle read with, so a change to the record's
    grammar or to where records live moves them and this count with them."""
    chain = load(
        "agentic_chain_check_for_counts",
        "skills",
        "code-review",
        "scripts",
        "chain_check.py",
    )
    routing = load("agentic_routing_for_counts", "hooks", "lib", "routing.py")
    settle = load(
        "agentic_settle_for_counts", "skills", "settle", "scripts", "settle.py"
    )
    return routing, chain, chain.SHARED_READER, settle


def why_not(problem):
    """Why a file was not read, in the error's own words and without the
    absolute path an `OSError`'s text carries: the line already names the
    file from the root, and the table is pasted into a public issue's
    comment. An `OSError` with no `strerror`, built without an errno, and a
    `UnicodeDecodeError`, whose text names no file, are said whole."""
    if isinstance(problem, OSError) and problem.strerror:
        return problem.strerror
    return str(problem)


def chained(routing, where):
    """`(True, None)` where `where/routing.md` parses with `Review` `through
    the review chain`, `(False, None)` where it parses with another answer,
    and `(None, why)` where it cannot be opened or is no declaration."""
    try:
        with open(os.path.join(where, routing.FILENAME), encoding="utf-8") as f:
            parsed = routing.parse(f.read())
    except (OSError, UnicodeDecodeError) as problem:
        return None, why_not(problem)
    if not parsed:
        return None, NO_DECLARATION
    return parsed["review"] == routing.CHAIN, None


def item_counts(root, where, routing, chain, reader, records_at):
    """`(cells, unread)` for the work item at `where`: its four cells, each a
    number or `NOT_READ`, and one line per record or directory not read. A
    finding is in records alone where every path its finding block's
    `location:` names lies under `records_at`, `seal/threads`."""

    def rel(path):
        return os.path.relpath(path, root).replace(os.sep, "/")

    if routing.rounds_unreadable(where):
        listed = os.path.join(where, routing.ROUNDS_DIR)
        return [NOT_READ] * 4, [f"{rel(listed)}: {NOT_LISTED}"]
    records = routing.rounds(where)
    found, unread = [], []
    for path in records:
        shown = rel(path)
        try:
            with open(path, encoding="utf-8") as handle:
                text = handle.read()
        except (OSError, UnicodeDecodeError) as problem:
            unread.append(f"{shown}: {why_not(problem)}")
            continue
        findings, errors = chain.record_findings(reader, text, shown)
        if errors:
            unread += [f"{at}:{line}: {why}" for at, line, why in errors]
            continue
        found += findings
    if unread:
        return [NOT_READ] * 3 + [len(records)], unread
    alone = sum(
        1
        for f in found
        if f.located and all(chain.under(p, records_at) for p in f.located)
    )
    again = sum(1 for f in found if f.regression or f.reopens)
    return [len(found), again, alone, len(records)], []


def main(argv=None):
    # Every entry point carries this (`hooks/lib/console.py`): a refusal
    # printed below is led by `chain_check.DASH`, an em dash, which a console
    # that cannot encode it would die on with stdout empty.
    console.to_utf8()
    parser = argparse.ArgumentParser(
        description="Print step 2b's four numbers per released work item."
    )
    parser.add_argument(
        "--released-at",
        default=DEFAULT_REF,
        help=f"the ref a released work item's directory is present at (default {DEFAULT_REF})",
    )
    parser.add_argument(
        "--root", default=CODE, help="the repository to count (default this one)"
    )
    args = parser.parse_args(argv)
    try:
        routing, chain, reader, settle = readers()
    except Exception as problem:
        print(f"finding-counts: a reader did not load ({problem})", file=sys.stderr)
        return 2
    root = os.path.abspath(args.root)
    released = settle.released(root, args.released_at)
    if released is None:
        print(
            f"finding-counts: --released-at {args.released_at} does not resolve "
            f"in {root}, so no work item can be read as released",
            file=sys.stderr,
        )
        return 2
    rows, unread = [], []
    for name in sorted(released):
        where = os.path.join(root, settle.SPECS, name)
        if not os.path.isdir(where):
            # Released and since removed from the tree: `seal settle` lists
            # it nowhere either, so it is no row and no line.
            continue
        through, why = chained(routing, where)
        if through is None:
            declared = os.path.join(where, routing.FILENAME)
            shown = os.path.relpath(declared, root).replace(os.sep, "/")
            unread.append(f"{shown}: {NOT_ROUTED}: {why}")
            continue
        if not through:
            continue
        cells, said = item_counts(root, where, routing, chain, reader, settle.SPECS)
        rows.append(f"| {name} | " + " | ".join(str(c) for c in cells) + " |")
        unread += said
    # A blank line ends the table, so a line under it is not read as a row.
    print("\n".join([HEADER, SEPARATOR, *rows, *(["", *unread] if unread else [])]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
