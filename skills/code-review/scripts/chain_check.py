#!/usr/bin/env python3
"""chain-check — at the pull request, the records the declared parties owe
are in the tree and agree with HEAD.

Run by CI on every pull request (`.github/workflows/hygiene.yml`). It judges
the `seal/threads/<id>/routing.md` naming the pull request's branch and every
one its own commits add or change. One that reached the branch inside another
pull request's squash was judged at that pull request and is named, not
judged (`carried_by`). The arms are eight:

  trailer       on every pull request, a declaration or none: each
                `Seal-Routing` trailer of the pull request's own commits
                names a work item a judged declaration names, or reads
                `no work item`, which is printed (`routing_trailers`); a
                commit with no such trailer is not judged
  declaration   the file parses as a routing declaration; one the pull
                request removed is accepted where its work item's directory
                stood at the merge base and is gone whole, which reads as a
                settle (`retired`), and none is judged where the tree the
                check reads has no
                top-level `seal` entry, which the pull request moving the
                root to local mode leaves; that tree is HEAD, and the working
                tree under `--worktree`
  frame         `Planning | framer`: `frame/design.md` and `frame/plan.md`
                are committed, `frame/design.md` ends with the framer's mark,
                and every `Reframed` line under it names the framer
  rule changes  the `## Rule changes` section parses with
                `rule_changes.parse`, the one reader `settle` groups by, in
                the `frame/design.md` of each judged work item under either
                `Planning` answer, and, on a pull request that declares at
                least one work item, in every work item `frame/design.md` its
                own commits add or change (`edited_work_items`); a design with
                no such section, and a work item with no design, pass
  records       `Review | through the review chain`: `trail/rounds/` holds at least
                one `round-N.md`; each reads whole against the grammar table
                of `docs/the-review-record.md` *The round record*, which
                `grammar` loads at import, and no finding reads `open`; a
                `fixed` commit is on the branch and touches a path its
                `location:` line names; every `fixed` or `rejected` finding
                is named by the next record's `confirms:`, `reopens:` or
                `regression:` lines, and none stands in the last record but
                a `fixed` finding located in the work item's own records
                alone (`located_in_records`) whose commit touched them alone
                (`records_only`), which the sealer reads; the
                last record's `target:` commit is HEAD, or every commit after
                it touches only the work item's own directory
  original      where git carries `seal/parity.md` at HEAD and the pull
                request changes a path outside the document roots
                `hooks/lib/gate.py#touches_code` reads: the config's `Baseline
                commit` row names a SHA (`hooks/lib/config.py#baseline_commit`),
                and one `original:` line naming it stands in every round
                record under `Review | through the review chain`, and in
                `guarantee.md` under `Review | straight to the PR`
                (`originals_of`)
  broad gate    `trail/gate.md`'s newest run is HEAD, or every commit after it
                touches only the work item's own directory
  guarantee     `guarantee.md` names HEAD, or every commit after it touches
                only the closing records, and its one `Verdict:` line
                reads `sealed`

A ready pull request fails on any of them. A draft, or a run that observed no
pull request, prints the same lines and exits 0. `docs/the-review-record.md`
states the record and the rules these arms hold.

Each label is read in its one spelling. A line that opens like a label and
is not it, `Verdict: open` for `verdict:` or `**Verdict:**` for the
guarantee's `Verdict:`, is prose to every arm, and a file under
`trail/rounds/` that is no `round-N.md` is not read; the check names each
(`unread`) and decides nothing on it. Whether the line meant the label is
the judgment of the agent that reads the record.

Usage:
  chain_check.py --baseline <ref> [--root DIR] [--worktree] [--sealing]

`--worktree` reads the records from the working tree instead of HEAD, for a
check before the commit; CI never passes it. `--sealing` is the broad gate's
own run, before it writes `trail/gate.md` and the sealer `guarantee.md`: those
two arms, and the guarantee's `original:` line, print and do not fail.

Exit: 0 nothing to refuse · 1 a refusal, each named `path:line  why` (a
GitHub annotation in CI) · 2 the check could not run, a grammar table it
cannot read, named by its file, and a reader that will not load among the
causes. A line or a file the check did not read is printed
`path:line  not read: <why>`, a notice annotation in CI and never an error,
and changes no exit code.
"""

import argparse
import collections
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys

if __name__ == "__main__":
    # Before the grammar loads below: a refusal it prints at import must not
    # meet a console's code page.
    for _name, _errors in (
        ("stdin", "replace"),
        ("stdout", "replace"),
        ("stderr", "backslashreplace"),
    ):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)

HERE = os.path.dirname(os.path.abspath(__file__))
READER = os.path.join(HERE, "..", "..", "verify", "scripts", "unverified_check.py")
HOOKS = os.path.join(HERE, "..", "..", "..", "hooks", "lib")
ROUTING = os.path.join(HOOKS, "routing.py")

TARGET = "Target SHA"
BROAD_GATE = "Broad gate"
# A thread's files, relative to its directory: `hooks/lib/optin.py`'s `GATE`,
# `GUARANTEE`, `DESIGN` and `PLAN`, spelt here because this module loads
# `routing` only inside the functions that are handed it.
BROAD_GATE_FILE = "trail/gate.md"
GUARANTEE_FILE = "guarantee.md"
SPEC_FILE = "frame/design.md"
PLAN_FILE = "frame/plan.md"
# The closing records: the orchestrator's run writes the one, the sealer the
# other, and they are the only files that may follow the commit the
# guarantee names, since the sealer audited everything else on the branch.
CLOSING_RECORDS = (BROAD_GATE_FILE, GUARANTEE_FILE)
# The sealer's verdict is one line of `guarantee.md` in one of the three
# shapes `VERDICT_SHAPES` names, read whole, with no emphasis and a value
# after each label.
VERDICT = "Verdict:"
SEALED = "sealed"
WITHHELD = "withheld"
UNDECIDED = "undecided"
REASON = "reason:"
QUESTION = "question:"
VERDICT_SHAPE = re.compile(
    rf"{VERDICT} (?:({SEALED})|({WITHHELD}) {REASON} \S.*"
    rf"|({UNDECIDED}) {QUESTION} \S.*)"
)
# The three shapes, as a refusal names them.
VERDICT_SHAPES = (
    f"`{VERDICT} {SEALED}`, `{VERDICT} {WITHHELD} {REASON} <reason>` or "
    f"`{VERDICT} {UNDECIDED} {QUESTION} <question>`"
)
# A line that opens like the verdict: the label's word in any case, after any
# emphasis or block markup, then a colon. One that is not `Verdict:` at the
# start of the line is prose, named as not read (`unread_verdicts`).
OPENS_LIKE_VERDICT = re.compile(r"[\s*_`>#+-]*verdict[\s*_`]*:", re.IGNORECASE)
UNREAD_VERDICT = (
    "not read: `{said}` opens like `Verdict:` and is not it, so the check "
    "read it as prose; the verdict line opens with `Verdict:` at the start of "
    "the line, written exactly so"
)
# The words the verdict used before #969. A guarantee still carrying one was
# written by a sealer that ran before the words changed, so it is refused on
# its line with what to do, never read as the new word it meant.
RETIRED_VERDICTS = ("sound", "not sound", "undecidable")
RETIRED_SAYS = (
    f"is a word the verdict no longer uses: the line reads {VERDICT_SHAPES} "
    "now. Where `trail/gate.md` names a run at HEAD, or one followed only by "
    "the work item's records, spawn the sealer again at HEAD, which writes "
    "the new word; otherwise run `seal gate --base <base> --record <item>` "
    "and commit `trail/gate.md` first"
)
# What a gate record's entry is separated from the run behind it by. The newest
# run stands first; `broad_gate.py#kept_runs` writes the rest behind it.
EARLIER_RUN = "; earlier run: "
# The `Target SHA` row has one shape: the commit audited `against` the base,
# one word each, then each earlier run of the sealer as `EARLIER_RUN` and
# its commit, the base where the run names one, and its verdict's word
# alone. Any other text after the target is refused at the row.
COMMIT_WORD = r"[0-9a-f]{7,40}"
BASE_WORD = r"[^\s;,]+"
TARGET_HEAD = re.compile(rf"{COMMIT_WORD} against {BASE_WORD}")
EARLIER_ENTRY = re.compile(
    rf"({COMMIT_WORD})(?: against {BASE_WORD})? ({SEALED}|{WITHHELD}|{UNDECIDED})"
)
TARGET_WRITTEN = (
    "`<sha> against <base>`, then each earlier run as `; earlier run: "
    "<sha> <word>`, with `against <base>` after its SHA where it names one"
)

# A round record's grammar is the table in `docs/the-review-record.md`
# *The round record*, and nothing in this file restates it: `grammar` loads
# it once, when this file is imported, and every reader below reads a line
# through its row. What this file names is which row is which, by the row's
# `Line` cell, the named parts of a row's shape it reads, and the four
# verdict words it decides on.
GRAMMAR_DOC = os.path.join(HERE, "..", "..", "..", "docs", "the-review-record.md")
# Where `grammar` finds the table: the section's heading and its header row.
# A rewrite of the document that moves either moves these with it (#941).
GRAMMAR_SECTION = "## The round record"
GRAMMAR_COLUMNS = ("Line", "Shape", "Where", "How many", "Refused as")
# The words the table's `Where` and `How many` cells are written in. `How
# many` counts per finding for a line in a finding, per record otherwise.
IN_RECORD = "the record"
OUTSIDE_FINDINGS = "outside every finding"
IN_FINDING = "a finding"
ONE = "one"
AT_MOST_ONE = "at most one"
ANY = "any"
EACH_ONCE = "each number once"
# How a refusal says the count a row allows.
HOW_MANY = {ONE: "one", AT_MOST_ONE: "one at most"}
FINDINGS_HEADING = "## Findings"
CONFIRMATIONS_HEADING = "## Confirmations"
IN_FINDINGS = f"`{FINDINGS_HEADING}`"
IN_CONFIRMATIONS = f"`{CONFIRMATIONS_HEADING}`"
TARGET_ROW = "target:"
ORIGINAL_ROW = "original:"
HEADING_ROW = "### <n>. <symptom>"
LOCATION_ROW = "location:"
VERDICT_ROW = "verdict:"
REGRESSION_ROW = "regression:"
REOPENS_ROW = "reopens:"
CONFIRMS_ROW = "confirms:"
# The rows the check reads a meaning from, by their `Line` cell: the place its
# reader looks for each, the counts that reader can keep, and the named parts
# of the shape it reads. `grammar` refuses a table that moves one, gives it
# another count or lacks a part. A row read for one value keeps one line, and
# a row decided on needs that line. Every other row may take any `Where` and
# `How many` `grammar_row` admits for its kind, because the reader of each
# place counts each word, a section left out included.
Read = collections.namedtuple("Read", "where many parts")
READ_ROWS = {
    TARGET_ROW: Read(OUTSIDE_FINDINGS, (ONE,), ("commit",)),
    # At most one: a record is owed the line only in a migration repository,
    # and `originals_of` refuses one that has none there.
    ORIGINAL_ROW: Read(OUTSIDE_FINDINGS, (AT_MOST_ONE,), ("commit",)),
    FINDINGS_HEADING: Read(IN_RECORD, (ONE, AT_MOST_ONE), ()),
    HEADING_ROW: Read(IN_FINDINGS, (EACH_ONCE,), ("number",)),
    LOCATION_ROW: Read(IN_FINDING, (ONE,), ()),
    VERDICT_ROW: Read(IN_FINDING, (ONE,), ("commit", "home")),
    REGRESSION_ROW: Read(IN_FINDING, (ONE, AT_MOST_ONE), ("round", "finding")),
    REOPENS_ROW: Read(IN_FINDING, (ONE, AT_MOST_ONE), ("round", "finding")),
    CONFIRMATIONS_HEADING: Read(IN_RECORD, (ONE, AT_MOST_ONE), ()),
    CONFIRMS_ROW: Read(IN_CONFIRMATIONS, (ONE, AT_MOST_ONE, ANY), ("round", "finding")),
}
# Where a row may stand: the two sections in the record, the finding heading
# in `## Findings`, and a label in one of three places.
SECTION_ROWS = (FINDINGS_HEADING, CONFIRMATIONS_HEADING)
# What a refusal says of the place a label's row puts it.
PLACED = {
    OUTSIDE_FINDINGS: "outside every finding",
    IN_FINDING: "and with no emphasis",
    IN_CONFIRMATIONS: f"in `{CONFIRMATIONS_HEADING}`",
}
# One row of the table as `grammar` reads it: its `Line` cell, its shape
# compiled, its `Where` and `How many` words, and its `Refused as` sentence.
Row = collections.namedtuple("Row", "line shape where many refused")
# One finding as `findings` read it: the line of its `verdict:`, its heading
# and the heading's number, the verdict, the paths of its `location:`, its
# `regression:` reference and its `reopens:` reference, each with that
# line's number, where it has one, and the line of its heading.
Finding = collections.namedtuple(
    "Finding",
    "line heading number verdict paths regression regression_line reopens "
    "reopens_line heading_line",
)
# The one rule across two rows the table cannot hold in a cell, for the
# refusal of a finding holding both.
ONE_RELATION = (
    f"a finding carries one of `{REGRESSION_ROW}` and `{REOPENS_ROW}`: "
    f"`{REGRESSION_ROW}` where a fix pass's own commit made the defect, "
    f"`{REOPENS_ROW}` where an earlier close does not hold otherwise"
)
# One record as `channel` reads it: its path and number, its findings, the
# numbers of every `### <n>. ` heading it holds, its `confirms:` references,
# and the commit its `target:` line names.
Round = collections.namedtuple("Round", "path number findings held confirms target")
# The verdict words the check decides on: `open` fails a ready pull request,
# `fixed` and `rejected` owe the next round a reference, `deferred` owes
# nothing. What follows each is the `verdict:` row's.
OPEN = "open"
FIXED = "fixed"
REJECTED = "rejected"
DEFERRED = "deferred"
DASH = chr(0x2014)
EMPHASIS = re.compile(r"[*_`]+")
ISSUE_RE = re.compile(r"#(\d+)")
SHA_RE = re.compile(r"\b[0-9a-f]{7,40}\b")

MARK_RE = re.compile(r"^Framed\s+(.+?)\s+by\s+(.+?),\s+before the build\.$")
REFRAME_RE = re.compile(r"^Reframed\s+(.+?)\s+by\s+(.+?),\s+after round\s+(\d+)\.$")

VERIFYING_ROUND = "a verifying round is owed"
SEALING = "--sealing"
SEALING_SAYS = (
    f"{SEALING}: `{BROAD_GATE_FILE}` is the file this run writes and "
    f"`{GUARANTEE_FILE}` the one the sealer writes after it, so their arms "
    "print and do not fail"
)
UNSEEN_SAYS = (
    "the pull request's state is unknown, and it is not judged as a ready "
    "pull request; CI judges it from GitHub's payload"
)
GH_DRAFT = ["gh", "pr", "view", "--json", "isDraft"]
GH_TIMEOUT = 30
NO_PAYLOAD = "no pull-request event payload"
REGULAR = ("100644", "100755")
# A squash merge on GitHub: the server commits it, and the subject ends with
# the number of the pull request it carried (`carried_by`).
SQUASH_COMMITTER = "noreply@github.com"
SQUASH_SUBJECT = re.compile(r"\(#\d+\)$")
CARRIED_SAYS = (
    "judged at its own pull request: {sha} `{subject}` squashed it onto this branch"
)


def load(path, name):
    """Import a sibling script by path, or raise SystemExit naming it."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"chain-check: cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def section_end(reader, lines, start):
    """The index of the line that ends the section opened at `start`: the
    first heading of its level or shallower, else `len(lines)`."""
    level = reader.heading_level(lines[start]) or 1
    for i in range(start + 1, len(lines)):
        found = reader.heading_level(lines[i])
        if found is not None and found <= level:
            return i
    return len(lines)


class GrammarError(ValueError):
    """The table `grammar` reads would not read: the sentence names the
    document, the line where there is one, and what it could not read."""


def code_span(cell):
    """The text of `cell` where the cell is one code span and nothing else,
    read as GFM reads one, or None: a run of backticks, text holding no run
    of the same length, the same run, and one space stripped from each end
    where both ends have one."""
    found = re.fullmatch(r"(`+)(.+?)\1", cell, re.S)
    if not found:
        return None
    run, text = found.groups()
    if any(len(inner) == len(run) for inner in re.findall("`+", text)):
        return None
    if len(text) > 2 and text[0] == text[-1] == " " and text.strip():
        text = text[1:-1]
    return text


def table_at(reader, lines, start, end, columns, refuse):
    """The rows of the table headed COLUMNS between START and END in
    already-`readable` LINES, as `[(line number, cells)]`, running to the
    first line that is no row; GrammarError where there is no such header
    or no separator under it."""
    header = next(
        (
            i
            for i in range(start + 1, end)
            if tuple(reader.split_row(lines[i]) or ()) == columns
        ),
        None,
    )
    if header is None:
        said = "| " + " | ".join(columns) + " |"
        raise refuse(f"its `{GRAMMAR_SECTION}` section holds no table headed {said}")
    if header + 1 >= end or not reader.is_separator(
        reader.split_row(lines[header + 1]) or []
    ):
        raise refuse("the header row is not followed by a separator row", header + 1)
    rows, i = [], header + 2
    while i < end and (cells := reader.split_row(lines[i])) is not None:
        rows.append((i + 1, cells))
        i += 1
    return rows


def grammar(path, reader):
    """`{Line: Row}` for the table under `path`'s `GRAMMAR_SECTION`, in its
    order, read with the shared `reader`; GrammarError where it cannot be.

    The section is found by its heading and the table by its header row,
    `GRAMMAR_COLUMNS`, followed by a separator; its rows run to the first
    line that is no row, and nothing else in the section is read, a second
    table among it. A `Line` cell and a `Shape` cell
    are each one code span, a `Shape` compiles, and its pattern opens with
    its label where the row is a label's. A `Where` and a `How many` are the
    words this file names, in the pairs it reads: a section in the record,
    once or at most once; the finding heading in `## Findings`, each number
    once; a label outside every finding, in a finding or in
    `## Confirmations`, once, at most once or any number of times. Every row
    `READ_ROWS` names stands where its reader looks, with a `How many` that
    reader can keep and the named parts it reads, and no heading row stands
    that this file reads nothing from. Anything else is GrammarError naming
    `path`, and the line where there is one."""

    def refuse(why, line=None):
        at = f"{path}:{line}" if line else path
        return GrammarError(f"{at}: {why}")

    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except (OSError, UnicodeDecodeError) as exc:
        raise refuse(f"cannot be read ({exc})") from None
    lines = reader.readable(text)
    starts = [
        i for i, said in reader.headings(lines) if said.strip() == GRAMMAR_SECTION
    ]
    if len(starts) != 1:
        raise refuse(f"holds {len(starts)} `{GRAMMAR_SECTION}` sections, not one")
    start = starts[0]
    end = section_end(reader, lines, start)
    rows = {}
    for number, cells in table_at(reader, lines, start, end, GRAMMAR_COLUMNS, refuse):
        rows.update([grammar_row(cells, refuse, number, rows, reader)])
    for key, read in READ_ROWS.items():
        row = rows.get(key)
        if row is None:
            raise refuse(f"the table has no `{key}` row, which the check reads")
        lacking = [p for p in read.parts if p not in row.shape.groupindex]
        if lacking:
            raise refuse(
                f"the `{key}` row's shape names no "
                + ", ".join(f"`(?P<{p}>…)`" for p in lacking)
                + ", which the check reads"
            )
        if row.where != read.where:
            raise refuse(
                f'the `{key}` row stands "{row.where}", and the check reads it '
                f'only where the table says "{read.where}"'
            )
        if row.many not in read.many:
            raise refuse(
                f"the `{key}` row's `How many` is `{row.many}`, and the check can "
                "honour only "
                + " or ".join(f"`{many}`" for many in read.many)
                + " for it"
            )
    return rows


def grammar_row(cells, refuse, number, rows, reader):
    """`(Line, Row)` for one table row's `cells` at line `number`, or the
    GrammarError `refuse` makes, by `grammar`'s rules."""
    if len(cells) != len(GRAMMAR_COLUMNS):
        raise refuse(
            f"{len(cells)} cells, and the table has {len(GRAMMAR_COLUMNS)}", number
        )
    line_cell, shape_cell, where, many, refused = cells
    key = code_span(line_cell)
    if key is None:
        raise refuse(f"its `Line` cell `{line_cell}` is not one code span", number)
    if key in rows:
        raise refuse(f"a second `{key}` row", number)
    if not refused:
        raise refuse(f"the `{key}` row's `Refused as` is empty", number)
    pattern = code_span(shape_cell)
    if pattern is None:
        raise refuse(f"the `{key}` row's shape is not one code span", number)
    try:
        shape = re.compile(pattern)
    except re.error as exc:
        raise refuse(
            f"the `{key}` row's shape does not compile ({exc})", number
        ) from None
    if key in SECTION_ROWS:
        allowed = where == IN_RECORD and many in (ONE, AT_MOST_ONE)
    elif key == HEADING_ROW:
        allowed = where == IN_FINDINGS and many == EACH_ONCE
    elif reader.heading_level(key) is not None:
        raise refuse(
            f"a `{key}` heading row, which the check reads nothing from", number
        )
    else:
        allowed = (
            key.endswith(":")
            and pattern.startswith(key)
            and where in (OUTSIDE_FINDINGS, IN_FINDING, IN_CONFIRMATIONS)
            and many in (ONE, AT_MOST_ONE, ANY)
        )
    if not allowed:
        raise refuse(
            f"the `{key}` row reads `{where}` and `{many}` with the shape "
            f"`{pattern}`, which the check cannot read",
            number,
        )
    return key, Row(key, shape, where, many, refused)


# Loaded once, here, and read by `main` and by every importer through this
# name. As a command, a reader or a table that will not load ends the run at
# exit 2 naming the file; imported, the error is raised and the importer
# decides what a check that cannot read a record means to it.
try:
    SHARED_READER = load(READER, "agentic_unverified_reader_for_grammar")
except (OSError, SyntaxError, ImportError, SystemExit) as _exc:
    if __name__ != "__main__":
        raise
    print(f"chain-check: the shared reader would not load ({_exc})", file=sys.stderr)
    raise SystemExit(2) from None
try:
    GRAMMAR = grammar(GRAMMAR_DOC, SHARED_READER)
except GrammarError as _exc:
    if __name__ != "__main__":
        raise
    print(
        f"chain-check: the round record's grammar would not load: {_exc}",
        file=sys.stderr,
    )
    raise SystemExit(2) from None

# What the readers below derive from the table: the labels a line may open
# with, the words of a line that opens like one, and the level of a
# finding's heading.
LABELS = tuple(k for k in GRAMMAR if k.endswith(":"))
SPELT = {" ".join(k[:-1].lower().split()): k for k in LABELS}
# A line that opens like a label: its first words, case folded and stripped
# of `*`, `_` and backticks, are a label's, followed by a colon. One that is
# not the label is prose to the check, named as not read (`opens_like`).
OPENS_LIKE = re.compile(
    r"^\s*[*_`]*\s*("
    + "|".join(
        r"\s+".join(re.escape(w) for w in words.split())
        for words in sorted(SPELT, key=len, reverse=True)
    )
    + r")\s*[*_`]*\s*:",
    re.IGNORECASE,
)
FINDING_LEVEL = len(HEADING_ROW) - len(HEADING_ROW.lstrip("#"))
# What the check prints of a line or a file it did not read. `main` prints
# each as a notice, `path:line  not read: <why>` and a notice annotation in
# CI, and none changes the exit code.
UNREAD_LINE = (
    "not read: `{said}` opens like the {label} label and is not it, so the "
    "check read it as prose; it reads {label} at the start of a line, "
    "lowercase, with no emphasis and one space after the colon"
)
UNREAD_FILE = (
    "not read: `{name}` is no `round-N.md`, so the check read nothing of it "
    "and judged the work item on the records it did read"
)


def section_count(key, many):
    """The refusal of a second `key` section, which holds `many`."""
    return f"a second `{key}` section; a round record holds {HOW_MANY[many]}"


def no_section(key):
    """The refusal of a record holding no `key` section, which it needs."""
    return f"no `{key}` section: {GRAMMAR[key].refused}"


NO_FINDINGS = no_section(FINDINGS_HEADING)
TWO_FINDINGS = section_count(FINDINGS_HEADING, GRAMMAR[FINDINGS_HEADING].many)
TWO_CONFIRMATIONS = section_count(
    CONFIRMATIONS_HEADING, GRAMMAR[CONFIRMATIONS_HEADING].many
)
CONFIRMATIONS_TABLE = (
    f"a table row in `{CONFIRMATIONS_HEADING}`: "
    f"{GRAMMAR[CONFIRMATIONS_HEADING].refused}"
)
OUTSIDE = (
    "a `{label}` line outside a finding: the check reads one inside each "
    f"`### ` section of `{FINDINGS_HEADING}`, and none elsewhere"
)
UNPLACED = (
    "a `{label}` line outside `{place}`: the check reads one there, and none elsewhere"
)


def no_record_line(key, scope="a round record"):
    """The refusal of a `scope` holding no `key` line, which it needs one of."""
    return (
        f"no `{key}` line: {scope} carries one, at the start of a line "
        f"{PLACED[GRAMMAR[key].where]}; {GRAMMAR[key].refused}"
    )


NO_TARGET = no_record_line(TARGET_ROW)


def git(root, *args):
    """`git -C root <args>`'s stdout, or None where git exited non-zero."""
    r = subprocess.run(
        ["git", "-C", root, *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=60,
    )
    return r.stdout if r.returncode == 0 else None


# Set once by `main`: read the records from the working tree, not HEAD.
WORKTREE = False


NO_BLOB = re.compile(r"^0+$")


def changed(root, base):
    """`(paths, moved)` this pull request adds, changes or deletes, or None.

    Every path the diff `base...HEAD` names, read with `--no-renames`: the
    check reads declarations, not file identity, so a deleted declaration
    is never paired away with a similar added one. `moved` is both names of
    every exact move — a deleted file whose bytes an added file of the same
    name carries — which is what the root move of #90 does to every
    declaration at once. Under `WORKTREE` the diff is against the working
    tree and untracked files count as added."""
    if WORKTREE:
        fork = git(root, "merge-base", base, "HEAD")
        if fork is None:
            return None
        out = git(
            root, "diff", "--raw", "-z", "--no-renames", "--no-abbrev", fork.strip()
        )
        untracked = git(root, "ls-files", "--others", "--exclude-standard", "-z")
        if out is None or untracked is None:
            return None
        out += "".join(f":0 0 0 0 A\0{p}\0" for p in untracked.split("\0") if p)
    else:
        out = git(
            root, "diff", "--raw", "-z", "--no-renames", "--no-abbrev", f"{base}...HEAD"
        )
    if out is None:
        return None
    fields = out.split("\0")
    paths, deleted, added = [], {}, []
    for i in range(0, len(fields) - 1, 2):
        meta = fields[i].split()
        if len(meta) < 5:
            continue
        path = fields[i + 1]
        paths.append(path)
        if meta[4] == "D":
            deleted.setdefault(os.path.basename(path), {})[meta[2]] = path
        elif meta[4] == "A":
            added.append((path, meta[3]))
    moved = set()
    for path, blob in added:
        same_name = deleted.get(os.path.basename(path))
        if not same_name:
            continue
        if NO_BLOB.match(blob):
            hashed = git(root, "hash-object", "--", path)
            blob = hashed.strip() if hashed else blob
        if blob in same_name:
            moved.update((path, same_name[blob]))
    return paths, moved


def changed_routing(paths, moved, work_items):
    """The routing declarations among `paths` that were not only moved."""
    return sorted(
        p
        for p in paths
        if p.startswith(f"{work_items}/")
        and os.path.basename(p) == "routing.md"
        and p not in moved
    )


def carried_by(root, base, rel):
    """`(commit, subject)` of the squash that carried `rel` onto this branch
    for another pull request, or None where this pull request's own commits
    changed it.

    A declaration is judged at the pull request that carries it. Where every
    commit after `base` touching `rel` is a squash merge GitHub committed —
    committer `noreply@github.com`, subject ending `(#N)` — the declaration
    reached this branch inside that pull request, which judged it; the newest
    such commit is returned. Any other commit, an uncommitted change under
    `WORKTREE`, no commit at all, or git failing leaves it this pull
    request's."""
    if WORKTREE:
        dirty = git(root, "status", "--porcelain", "--", rel)
        if dirty is None or dirty.strip():
            return None
    out = git(
        root,
        "log",
        "--no-merges",
        "-z",
        "--format=%H%x1f%ce%x1f%s",
        f"{base}..HEAD",
        "--",
        rel,
    )
    commits = [e.split("\x1f") for e in (out or "").split("\0") if e.strip()]
    if not commits:
        return None
    for entry in commits:
        if (
            len(entry) != 3
            or entry[1].strip().lower() != SQUASH_COMMITTER
            or not SQUASH_SUBJECT.search(entry[2].strip())
        ):
            return None
    return commits[0][0].strip(), commits[0][2].strip()


def tracked_files(root, where):
    """The regular files git carries directly in `where` at HEAD, by name."""
    out = git(root, "ls-tree", "-z", "HEAD", "--", f"{where}/")
    if out is None:
        return []
    names = []
    for entry in out.split("\0"):
        if not entry:
            continue
        meta, _, path = entry.partition("\t")
        parts = meta.split()
        if len(parts) >= 3 and parts[0] in REGULAR:
            names.append(os.path.basename(path))
    return names


def worktree_files(root, where):
    """The regular files directly in `where` on disk, symbolic links excluded."""
    base = os.path.join(root, *where.split("/"))
    try:
        names = os.listdir(base)
    except OSError:
        return []
    return [
        n
        for n in names
        if os.path.isfile(os.path.join(base, n))
        and not os.path.islink(os.path.join(base, n))
    ]


def read_record(root, rel):
    """The file as git carries it at HEAD, or on disk under `WORKTREE`; None
    where there is none."""
    if WORKTREE:
        try:
            with open(
                os.path.join(root, *rel.split("/")), encoding="utf-8", errors="replace"
            ) as f:
                return f.read()
        except OSError:
            return None
    return git(root, "show", f"HEAD:{rel}")


def rounds_listed(routing, root, item):
    """`(the round records, the other files)` directly under
    `<item>/trail/rounds/`, as git carries them: the records are the names
    `routing.round_number` reads, lowest round first, and the others every
    other name, sorted."""
    where = f"{item}/{routing.ROUNDS_DIR}"
    listed = worktree_files(root, where) if WORKTREE else tracked_files(root, where)
    found, others = [], []
    for name in listed:
        number = routing.round_number(name)
        if number is None:
            others.append(f"{where}/{name}")
        else:
            found.append((number, f"{where}/{name}"))
    return [rel for _, rel in sorted(found)], sorted(others)


def round_records(routing, root, item):
    """`<item>/trail/rounds/round-N.md` git carries, lowest round first."""
    return rounds_listed(routing, root, item)[0]


def unread(reader, routing, root, item, chained):
    """[(path, line, why)] for what the check did not read of a work item:
    under `chained`, each file under `trail/rounds/` that is no
    `round-N.md` (`UNREAD_FILE`) and each line of a round record that opens
    like a label and is not it (`unread_lines`); each line of its
    `guarantee.md` that opens like `Verdict:` and is not it
    (`unread_verdicts`); and, where the work item is not chained, so that
    `originals_of` reads the guarantee's `original:` line, each line of it
    that opens like `original:` and is not it. `main` prints them as
    notices."""
    found = []
    if chained:
        records, others = rounds_listed(routing, root, item)
        found += [
            (rel, 0, UNREAD_FILE.format(name=rel.rsplit("/", 1)[-1])) for rel in others
        ]
        for rel in records:
            found += unread_lines(reader.readable(read_record(root, rel) or ""), rel)
    rel = f"{item}/{GUARANTEE_FILE}"
    text = read_record(root, rel)
    if text is not None:
        found += unread_verdicts(reader, text, rel)
        if not chained:
            label = f"`{ORIGINAL_ROW}`"
            found += [
                (rel, i + 1, UNREAD_LINE.format(said=line.strip(), label=label))
                for i, line in enumerate(reader.readable(text))
                if opens_like(line) == ORIGINAL_ROW
            ]
    return found


def event_payload_present():
    """True where `GITHUB_EVENT_PATH` names a file."""
    path = os.environ.get("GITHUB_EVENT_PATH")
    return bool(path) and os.path.exists(path)


def pull_request_state(root=None, which=shutil.which, run=subprocess.run):
    """(`draft` | `ready` | `unknown`, where that was read from).

    The event payload GitHub writes is the answer wherever it exists; with
    none, `gh pr view` is asked in `root`. A payload that cannot answer is
    `unknown`, which `main` judges as ready, so a harness fault is never the
    quiet way past the check."""
    path = os.environ.get("GITHUB_EVENT_PATH")
    if not path or not os.path.exists(path):
        if root is None:
            return "unknown", NO_PAYLOAD
        return pull_request_from_gh(root, which, run)
    try:
        with open(path, encoding="utf-8") as f:
            event = json.load(f)
    except (OSError, ValueError) as exc:
        return "unknown", f"the event payload would not read ({exc})"
    pr = event.get("pull_request")
    if not isinstance(pr, dict) or "draft" not in pr:
        return "unknown", "the event payload names no pull request"
    if not isinstance(pr["draft"], bool):
        return "unknown", (
            f"the event payload's `draft` is {type(pr['draft']).__name__}, "
            "not a boolean"
        )
    return ("draft" if pr["draft"] else "ready"), path


def pull_request_from_gh(root, which=shutil.which, run=subprocess.run):
    """(`draft` | `ready` | `unknown`, where) from `gh pr view --json isDraft`."""
    found = which(GH_DRAFT[0])
    if found is None:
        return "unknown", f"{NO_PAYLOAD}, and no `gh` on PATH to ask"
    try:
        r = run(
            [found, *GH_DRAFT[1:]],
            cwd=root,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=GH_TIMEOUT,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return "unknown", f"{NO_PAYLOAD}, and `gh pr view` did not run ({exc})"
    if r.returncode != 0:
        said = (r.stderr or r.stdout or "").strip().partition("\n")[0].strip()
        return "unknown", (
            f"{NO_PAYLOAD}, and `gh pr view` exited {r.returncode}"
            + (f": {said}" if said else "")
        )
    try:
        answer = json.loads(r.stdout)
    except ValueError:
        answer = None
    draft = answer.get("isDraft") if isinstance(answer, dict) else None
    if not isinstance(draft, bool):
        return "unknown", (
            f"{NO_PAYLOAD}, and `gh pr view` did not say whether the pull "
            "request is a draft"
        )
    return ("draft" if draft else "ready"), "`gh pr view --json isDraft`"


def fields(rows, label):
    """The value of every `| label | value |` row, in order."""
    return [
        cells[1].strip()
        for cells in rows
        if len(cells) >= 2 and cells[0].strip() == label
    ]


def field(rows, label):
    """The value of the one `| label | value |` row, or None where it is
    absent or stands more than once."""
    found = fields(rows, label)
    return found[0] if len(found) == 1 else None


def table_rows(reader, lines):
    """Every table row in already-`readable` lines, as lists of cells."""
    out = []
    for line in lines:
        cells = reader.split_row(line)
        if cells is not None:
            out.append(cells)
    return out


def label_of(line):
    """The label `line` opens with in its one spelling, the label then a
    space or the end of the line, or None."""
    for label in LABELS:
        if line == label or line.startswith(f"{label} "):
            return label
    return None


def value_of(line):
    """What follows a labelled line's label and its space."""
    return line[len(label_of(line) or "") + 1 :]


def as_row(key, value):
    """The match of `key`'s line reading `value` against its row whole, or
    None."""
    return GRAMMAR[key].shape.fullmatch(f"{key} {value}")


def reference(found):
    """`(round, finding or None)` from a reference row's match."""
    number = found["finding"]
    return int(found["round"]), int(number) if number else None


def verdict_of(value):
    """`(kind, its commit or home)` for one `verdict:` value, or None.

    Read against the `verdict:` row whole: its word, and the commit of a
    `fixed` or the home of a `deferred`. Anything the row does not match —
    another case, emphasis, a trailing word or mark, a bare `fixed` or
    `deferred` — is None.

    `finding_of` hands it only a line the row already matched whole, and
    `deferred_home` is called only by cases, so no record reaches the None.
    It stays because `Test_verdict_of` and `Test_deferred_home` call it with
    values the row refuses, and those cases are where the `verdict:` grammar
    is pinned."""
    found = as_row(VERDICT_ROW, value)
    if not found:
        return None
    return value.split(" ", 1)[0], found["commit"] or found["home"]


def deferred_home(value):
    """The home a `deferred <home>` value names, or None."""
    verdict = verdict_of(value)
    return verdict[1] if verdict and verdict[0] == DEFERRED else None


def issue_of(home):
    """N where a deferral's home is exactly `#N`, else None."""
    found = ISSUE_RE.fullmatch(home or "")
    return int(found.group(1)) if found else None


def location_of(value):
    """The paths one `location:` value names, in order, or None.

    Read against the `location:` row whole, then each backticked item to
    its first `:`, which the row keeps out of a path. Anything the row does
    not match — a bare `:617`, a path with no backticks, a URL, an absolute
    path, a `path#unit`, emphasis around an item, a trailing word or mark,
    an empty value — is None.

    `finding_of`, the one caller in the tree, hands it only a line the row
    already matched whole, so no record reaches the None. It stays because
    `Test_location_of` calls it with values the row refuses, and those cases
    are where the `location:` grammar is pinned."""
    if not as_row(LOCATION_ROW, value):
        return None
    return [item.strip("`").split(":")[0] for item in value.split(", ")]


def reference_of(value):
    """`(round, finding)` for a reference to a finding, `(round, None)` for
    one to a round's fix pass, or None.

    Read against the `regression:` row whole, the one reference row that
    takes both: a different case, a space, a leading zero, emphasis, a
    trailing mark or a second reference is None.

    `finding_of`, the one caller in the tree, hands it only a line the row
    already matched whole, so no record reaches the None. It stays because
    `Test_reference_of` calls this function with every spelling the row
    refuses, and those cases are where the `regression:` grammar is pinned."""
    found = as_row(REGRESSION_ROW, value)
    return reference(found) if found else None


def reopened_of(value):
    """`(round, finding)` for the value of a `reopens:` line, which takes a
    finding alone, since a close is a finding's verdict and a fix pass no
    finding named closed nothing to reopen.

    `finding_of`, the one caller, hands it only a line the `reopens:` row's
    shape already matched whole, so the match here is never None."""
    return reference(as_row(REOPENS_ROW, value))


def sections_of(reader, lines, key):
    """The index of every heading of already-`readable` lines the `key`
    row's shape matches whole."""
    shape = GRAMMAR[key].shape
    return [i for i, said in reader.headings(lines) if shape.fullmatch(said.strip())]


def finding_spans(reader, lines):
    """`((start, end), [(first, stop)], error)` for the one `## Findings`
    section of already-`readable` lines: where it stands, and each `### `
    section in it, from its heading to the next. `error` is the refusal for
    a record with no such section where it needs one, or with more than its
    row allows, and the spans are then empty."""
    starts = sections_of(reader, lines, FINDINGS_HEADING)
    many = GRAMMAR[FINDINGS_HEADING].many
    if not starts:
        return None, [], ((0, NO_FINDINGS) if many == ONE else None)
    if len(starts) > 1:
        return None, [], (starts[1] + 1, TWO_FINDINGS)
    start = starts[0]
    end = section_end(reader, lines, start)
    heads = [
        i
        for i in range(start + 1, end)
        if reader.heading_level(lines[i]) == FINDING_LEVEL
    ]
    return (start, end), list(zip(heads, [*heads[1:], end])), None


def finding_number(heading):
    """The `n` of a finding heading the heading row matches whole, or None."""
    found = GRAMMAR[HEADING_ROW].shape.fullmatch(heading)
    return int(found["number"]) if found else None


def opens_like(line):
    """The label `line` opens like and is not, or None."""
    found = OPENS_LIKE.match(line)
    if not found or label_of(line):
        return None
    return SPELT[" ".join(found.group(1).lower().split())]


def unread_lines(lines, rel):
    """[(rel, line, why)] for each line of `lines`, `readable`'s, that opens
    like a label and is not it (`opens_like`), at its line.

    Such a line is prose to every reader here: it decides nothing, and a
    finding that then lacks a line its row says is `one` is refused as
    lacking it. Whether the line meant the label is the reading agent's
    judgment, so the check names it and refuses nothing for it, and keeps
    no list of the other spellings a label is written in."""
    return [
        (rel, i + 1, UNREAD_LINE.format(said=line.strip(), label=f"`{label}`"))
        for i, line in enumerate(lines)
        if (label := opens_like(line))
    ]


def confirmations_span(reader, lines):
    """The indexes of every line under a `## Confirmations` heading."""
    return {
        i
        for start in sections_of(reader, lines, CONFIRMATIONS_HEADING)
        for i in range(start, section_end(reader, lines, start))
    }


def findings(reader, lines, rel):
    """`([Finding], errors)` for a record's findings.

    `lines` are `reader.readable`'s, so a labelled line inside a fence is no
    line. The one `## Findings` section is split at its `### `
    headings, and each finding is read by `finding_of` against the rows the
    table places in a finding. A line that opens like a label and is not it
    is prose here and refuses nothing; `unread_lines` names it.
    Everything the reader cannot read is an error `(rel, line, why)` naming
    the finding's heading, in line order: what `finding_spans` refuses, a
    heading the heading row does not match or with a number an earlier
    heading carries, what `finding_of` refuses, a label a finding's row
    names standing outside every finding, a label another row places
    standing inside one, and a `## Confirmations` row's label outside that
    section. A finding with an error is not in the list."""
    _section, spans, error = finding_spans(reader, lines)
    if error:
        return [], [(rel, *error)]
    inside = {i for first, stop in spans for i in range(first, stop)}
    confirming = confirmations_span(reader, lines)
    found, errors = [], []
    for i, line in enumerate(lines):
        if i in inside:
            continue
        key = label_of(line)
        where = GRAMMAR[key].where if key else None
        if where == IN_FINDING:
            errors.append((rel, i + 1, OUTSIDE.format(label=key)))
        elif where == IN_CONFIRMATIONS and i not in confirming:
            errors.append(
                (rel, i + 1, UNPLACED.format(label=key, place=CONFIRMATIONS_HEADING))
            )
    numbers = set()
    for first, stop in spans:
        heading = lines[first].strip()
        number = finding_number(heading)
        if number is None or number in numbers:
            errors.append(
                (
                    rel,
                    first + 1,
                    f"{heading} {DASH} "
                    + (
                        GRAMMAR[HEADING_ROW].refused
                        if number is None
                        else f"a second finding numbered {number}: a later "
                        f"round's `round-<N>#{number}` would name both"
                    ),
                )
            )
            continue
        numbers.add(number)
        elsewhere = [
            (i, key)
            for i in range(first + 1, stop)
            if (key := label_of(lines[i])) and GRAMMAR[key].where != IN_FINDING
        ]
        if elsewhere:
            errors.extend(
                (
                    rel,
                    i + 1,
                    f"{heading} {DASH} a `{key}` line inside a finding: the "
                    f"check reads it {PLACED[GRAMMAR[key].where]}, and none in one",
                )
                for i, key in elsewhere
            )
            continue
        found_here, errors_here = finding_of(lines, first, stop, heading, rel)
        errors.extend(errors_here)
        if not errors_here:
            found.append(found_here)
    errors.sort(key=lambda error: error[1])
    return found, errors


def finding_of(lines, first, stop, heading, rel):
    """`(Finding or None, errors)` for the `### ` section at `first`..`stop`.

    Every row the table places in a finding is read here: a row that needs
    one line and has none, or that allows one and has more, is refused at
    the heading or the second line, and each line a count leaves standing
    is refused where its row's shape does not match it whole. The verdict,
    the paths and the references are then read out of the lines that
    matched, and a finding holding both a `regression:` and a `reopens:`
    line is refused at the later one. A finding the check cannot decide —
    no verdict or location read — is never returned."""
    rows = [row for row in GRAMMAR.values() if row.where == IN_FINDING]
    at = {
        row.line: [i for i in range(first + 1, stop) if label_of(lines[i]) == row.line]
        for row in rows
    }
    errors, read = [], {}
    for row in rows:
        refused = counted(rel, row.line, at[row.line], "a finding", first, heading)
        if refused:
            errors.append(refused)
    for row in rows:
        said = at[row.line]
        if len(said) > 1 and row.many in HOW_MANY:
            continue
        for i in said:
            if row.shape.fullmatch(lines[i]):
                read[row.line] = i
                continue
            errors.append(
                (
                    rel,
                    i + 1,
                    f"{heading} {DASH} reads `{lines[i]}`, which the check cannot "
                    f"read: {row.refused}",
                )
            )
    both = [at.get(REGRESSION_ROW, []), at.get(REOPENS_ROW, [])]
    if all(len(said) == 1 for said in both):
        errors.append(
            (
                rel,
                max(said[0] for said in both) + 1,
                f"{heading} {DASH} a `{REGRESSION_ROW}` and a `{REOPENS_ROW}` line: "
                + ONE_RELATION,
            )
        )
    if errors:
        return None, errors

    def line_of(key):
        return read[key] + 1 if key in read else None

    def value(key):
        return value_of(lines[read[key]]) if key in read else None

    return (
        Finding(
            line_of(VERDICT_ROW),
            heading,
            finding_number(heading),
            verdict_of(value(VERDICT_ROW)),
            location_of(value(LOCATION_ROW)),
            reference_of(value(REGRESSION_ROW)) if REGRESSION_ROW in read else None,
            line_of(REGRESSION_ROW),
            reopened_of(value(REOPENS_ROW)) if REOPENS_ROW in read else None,
            line_of(REOPENS_ROW),
            first + 1,
        ),
        [],
    )


def unclosed(reader, text, rel):
    """[(rel, line, why)] for a fence in `text` that never closes, at the
    line that opened it.

    `reader.readable` blanks such a fence to the end of the file, so every
    `### ` heading and `verdict:` line after it would vanish and the record
    would read as having nothing open. The walk is `readable`'s own,
    `fence_spans` on the raw lines; a comment is text to it (#1012), and a
    line that begins one is `comment_lines`' to refuse."""
    return [
        (
            rel,
            first + 1,
            "a fence opened here never closes, so every line after it is "
            "hidden from the check",
        )
        for first, last in reader.fence_spans(reader.gfm_lines(text or ""))
        if last is None
    ]


def comment_lines(reader, text, rel):
    """[(rel, line, why)] for each line of `text` outside every fence that
    begins with `<!--`, at its line, with the shared reader's one message
    (`unverified_check.py#comment_lines`, #1012).

    A record carries no HTML comment, and the check keeps no comment state,
    so it reads a comment as text; a line that begins one is refused rather
    than read as part of the record. The read of a round record, a
    `guarantee.md` and a `trail/gate.md` each ask this."""
    lines = reader.readable(text or "")
    return [(rel, n + 1, reader.COMMENT_LINE) for n in reader.comment_lines(lines)]


def counted(rel, key, said, scope, first=-1, heading=None):
    """The refusal of `said`, the indexes of `key`'s lines in one `scope`,
    where its row's `How many` does not allow that many, or None: at the
    heading at index `first`, and led by it, where one is given."""
    row = GRAMMAR[key]
    lead = f"{heading} {DASH} " if heading else ""
    if not said and row.many == ONE:
        return (rel, first + 1, lead + no_record_line(key, scope))
    if len(said) > 1 and row.many in HOW_MANY:
        return (
            rel,
            said[1] + 1,
            f"{lead}{len(said)} `{key}` lines; {scope} carries {HOW_MANY[row.many]}",
        )
    return None


def unreadable(rel, line, number, row):
    """The refusal of a labelled `line` at index `number` its row's shape
    does not match whole."""
    return (
        rel,
        number + 1,
        f"reads `{line}`, which the check cannot read: {row.refused}",
    )


def record_lines(reader, lines, rel, key):
    """`(the match or None, errors)` for `key`'s line in a record, a row the
    table places outside every finding.

    `lines` are `reader.readable`'s. Its lines outside every finding are
    counted against the row's `How many` and each read against its shape
    whole (`findings` refuses one inside a finding). Where they are none —
    the old `| Target SHA |` table row is none — more than the row allows,
    or one the shape does not match, that is an error by line, and no
    match is returned."""
    _section, spans, _error = finding_spans(reader, lines)
    inside = {i for first, stop in spans for i in range(first, stop)}
    said = [
        i for i, line in enumerate(lines) if i not in inside and label_of(line) == key
    ]
    refused = counted(rel, key, said, "a round record")
    if refused:
        return None, [refused]
    row, found, errors = GRAMMAR[key], None, []
    for i in said:
        found = row.shape.fullmatch(lines[i])
        if not found:
            errors.append(unreadable(rel, lines[i], i, row))
    return (None if errors else found), errors


def read_whole(reader, text, rel):
    """`(lines, findings, errors, outside)` for one record, read once:
    `readable`'s lines, `findings` over them with `comment_lines`' and
    `unclosed`'s refusals first and `record_lines`' after, and
    `{key: match or None}` for every row the table places outside every
    finding."""
    lines = reader.readable(text or "")
    found, errors = findings(reader, lines, rel)
    outside, said = {}, []
    for key, row in GRAMMAR.items():
        if row.where == OUTSIDE_FINDINGS:
            outside[key], refused = record_lines(reader, lines, rel, key)
            said += refused
    first = comment_lines(reader, text, rel) + unclosed(reader, text, rel)
    return lines, found, first + errors + said, outside


def record_findings(reader, text, rel):
    """`findings` over a record's text, with `comment_lines`' and
    `unclosed`'s refusals first and `record_lines`' after, for every row the
    table places outside every finding: the one reader the arm, the panel
    and the release seal read a record through, so a comment line, a fence
    that hides findings, or a record naming no commit it reviewed, fails
    closed for each of them."""
    _lines, found, errors, _outside = read_whole(reader, text, rel)
    return found, errors


def confirmations(reader, lines, rel):
    """`([(line, (round, finding))], errors)` for a record's `confirms:`
    lines.

    A record with nothing to confirm may leave `## Confirmations` out, as
    far as its row allows: a section the row says is `one` is refused where
    it is absent, and each row the table places there is counted against
    no lines, so one at `one` is refused too. In the section, each line of
    such a row is counted against the row and read against its shape
    whole, and a `confirms:` line naming a finding is read with its line;
    one reading `none`, and the prose after any entry, are read for
    nothing. Everything else is an error by line: more sections than the row
    allows, a line its shape does not match, a table row, the old shape.
    What the reference names is `channel`'s."""
    starts = sections_of(reader, lines, CONFIRMATIONS_HEADING)
    if len(starts) > 1:
        return [], [(rel, starts[1] + 1, TWO_CONFIRMATIONS)]
    rows = [row for row in GRAMMAR.values() if row.where == IN_CONFIRMATIONS]
    at = {row.line: [] for row in rows}
    found, errors = [], []
    if not starts and GRAMMAR[CONFIRMATIONS_HEADING].many == ONE:
        errors.append((rel, 0, no_section(CONFIRMATIONS_HEADING)))
    span = range(starts[0] + 1, section_end(reader, lines, starts[0])) if starts else ()
    for i in span:
        if reader.split_row(lines[i]) is not None:
            errors.append((rel, i + 1, CONFIRMATIONS_TABLE))
            continue
        key = label_of(lines[i])
        if key not in at:
            continue
        at[key].append(i)
        said = GRAMMAR[key].shape.fullmatch(lines[i])
        if not said:
            errors.append(unreadable(rel, lines[i], i, GRAMMAR[key]))
        elif key == CONFIRMS_ROW and said["round"]:
            found.append((i + 1, reference(said)))
    for key, said in at.items():
        refused = counted(rel, key, said, f"`{CONFIRMATIONS_HEADING}`")
        if refused:
            errors.append(refused)
    return found, errors


def round_of(reader, text, rel, number):
    """`(Round, errors)` for one record: its findings, its errors and its
    `target:` line's `commit` part through `read_whole`, its `confirms:`
    references through `confirmations`, and the number of every `### <n>. `
    heading of its `## Findings`, read or refused, so a reference to a
    refused finding still names one it holds. A record whose `target:` line
    `read_whole` refused has no target."""
    lines, found, errors, outside = read_whole(reader, text, rel)
    target = outside[TARGET_ROW]["commit"] if outside[TARGET_ROW] else None
    confirmed, said = confirmations(reader, lines, rel)
    _section, spans, _error = finding_spans(reader, lines)
    held = {finding_number(lines[first].strip()) for first, _stop in spans}
    held.discard(None)
    errors = sorted(errors + said, key=lambda error: error[1])
    return Round(rel, number, found, held, confirmed, target), errors


def channel(rounds, read_at_head=lambda finding: False):
    """[(path, line, problem)] for what one round owes the next, over an
    item's records in number order.

    Every reference a record writes — a `confirms:` line, a `reopens:` line,
    a `regression:` line — names an earlier record of the item and, where it
    names a finding, one that record holds; the first record writes none.
    Every finding of a record at `fixed <commit>` or `rejected` is named by
    the next record's `confirms:`, `reopens:` or `regression:` lines, or
    refused at its own heading. A `rejected` finding of the last record, and
    a `fixed` one `read_at_head` does not pass, is refused as owing a
    verifying round, since nothing after it read the fix or the rejection.
    `records` passes it a `fixed` finding located in the work item's own
    records alone whose commit touched them alone, which the sealer reads at
    HEAD. A `deferred` finding owes
    nothing."""
    problems = []
    by_number = {r.number: r for r in rounds}
    for k, here in enumerate(rounds):
        references = sorted(
            [*here.confirms]
            + [(f.regression_line, f.regression) for f in here.findings if f.regression]
            + [(f.reopens_line, f.reopens) for f in here.findings if f.reopens],
        )
        for line, (n, m) in references:
            said = f"round-{n}" + (f"#{m}" if m else "")
            if k == 0:
                why = (
                    f"names `{said}` in the first record: there is no earlier "
                    f"round to name, so its `{CONFIRMS_ROW}` lines read `none`"
                )
            elif n >= here.number or n not in by_number:
                why = (
                    f"names `{said}`, which is not an earlier record of this work item"
                )
            elif m is not None and m not in by_number[n].held:
                why = f"names `{said}`, and round-{n}.md holds no finding {m}"
            else:
                continue
            problems.append((here.path, line, why))
        if k == 0:
            continue
        before = rounds[k - 1]
        named = {(n, m) for _line, (n, m) in references if m is not None}
        for f in before.findings:
            owed = f.verdict[0] in (FIXED, REJECTED)
            if owed and (before.number, f.number) not in named:
                problems.append(
                    (
                        before.path,
                        f.heading_line,
                        f"{f.heading} {DASH} reads `{VERDICT_ROW} "
                        f"{' '.join(x for x in f.verdict if x)}`, and the next "
                        f"record, {here.path}, names it on no `{CONFIRMS_ROW}`, "
                        f"`{REOPENS_ROW}` or `{REGRESSION_ROW}` line: one of them reads "
                        f"`round-{before.number}#{f.number}`",
                    )
                )
    if rounds:
        last = rounds[-1]
        for f in last.findings:
            if f.verdict[0] == REJECTED or (
                f.verdict[0] == FIXED and not read_at_head(f)
            ):
                problems.append(
                    (
                        last.path,
                        f.line,
                        f"{f.heading} {DASH} reads `{VERDICT_ROW} "
                        f"{' '.join(x for x in f.verdict if x)}` in the last "
                        f"record, and no round after it read it: {VERIFYING_ROUND}",
                    )
                )
    return problems


def touched(root, commit):
    """The paths `commit` changed, the root commit's included, or None
    where git cannot say."""
    out = git(
        root, "diff-tree", "--no-commit-id", "--name-only", "-r", "--root", "-z", commit
    )
    if out is None:
        return None
    return [path for path in out.split("\0") if path]


def under(path, located):
    """True where `path` is `located` or lies under it."""
    stem = located.rstrip("/")
    return path == stem or path.startswith(f"{stem}/")


def located_in_records(item, f):
    """True where finding `f` names at least one path and every path its
    `location:` names lies under `item/`, the work item's own records. A
    finding located in code is read by a round whatever its fix touched."""
    return bool(f.paths) and all(under(q, item) for q in f.paths)


def records_only(root, item, commit):
    """True where `commit` changed at least one path and every path it
    changed lies under `item/`, the work item's own records; False where it
    changed a path outside them, nothing, or git cannot say."""
    changed = touched(root, commit)
    return bool(changed) and all(under(p, item) for p in changed)


def target_of(reader, text):
    """The first SHA-shaped word of `guarantee.md`'s `Target SHA` row, or
    None. A round record names its commit on a `target:` line instead
    (`round_of`)."""
    rows = table_rows(reader, reader.readable(text or ""))
    found = SHA_RE.search(reader.visible(field(rows, TARGET) or ""))
    return found.group(0) if found else None


def earlier_verdicts(cell):
    """`[(sha, word)]` for each earlier run of a `guarantee.md` `Target SHA`
    cell, in the order written (#975), the cell read as one shape
    (`TARGET_WRITTEN`): after `TARGET_HEAD`, nothing, or `EARLIER_RUN` and an
    `EARLIER_ENTRY` whole, again and again. An entry that is not one comes
    back as `(EARLIER_RUN + entry, None)`; text after the target that does
    not open with `EARLIER_RUN` comes back whole as `(text, None)`. The
    guarantee arm refuses each, so no spelling of the separator passes
    unread. The stamp is drawn once per work item, and an earlier entry
    reading `sealed` is how the row says it was drawn already."""
    cell = cell or ""
    head = TARGET_HEAD.match(cell)
    rest = cell[head.end() :] if head else cell
    if not rest:
        return []
    if not rest.startswith(EARLIER_RUN):
        return [(rest.strip(), None)]
    out = []
    for entry in rest.split(EARLIER_RUN)[1:]:
        m = EARLIER_ENTRY.fullmatch(entry)
        out.append(
            (m.group(1), m.group(2)) if m else ((EARLIER_RUN + entry).strip(), None)
        )
    return out


def newest_run(reader, text):
    """The commit the newest run of `trail/gate.md`'s `Broad gate` row was
    taken at — the first word of its first entry, where that word is
    SHA-shaped — or None."""
    rows = table_rows(reader, reader.readable(text or ""))
    cell = reader.visible(field(rows, BROAD_GATE) or "")
    words = EMPHASIS.sub("", cell.split(EARLIER_RUN)[0]).split()
    return words[0] if words and SHA_RE.fullmatch(words[0]) else None


def is_ancestor(root, sha, ref):
    """True where `sha` is `ref` or an ancestor of it."""
    r = subprocess.run(
        ["git", "-C", root, "merge-base", "--is-ancestor", sha, ref],
        capture_output=True,
    )
    return r.returncode == 0


def follows(root, sha, base, item, only=None):
    """None where `sha` is HEAD or every commit after it on the branch
    touches only `item/` — only the files of `item/` named in `only`, where
    it is given; else why not.

    `("unseen", sha, "")` for a commit this repository cannot resolve,
    `("off", sha, "")` for one HEAD does not descend from, `("after",
    commit, path)` for the first commit after it, oldest first, touching
    `path` outside what may follow. Merge commits and the base's own commits
    are not the branch's."""
    allowed = None if only is None else {f"{item}/{name}" for name in only}
    full = git(root, "rev-parse", "--verify", "--quiet", f"{sha}^{{commit}}")
    if full is None:
        return ("unseen", sha, "")
    full = full.strip()
    if not is_ancestor(root, full, "HEAD"):
        return ("off", sha, "")
    out = git(
        root, "rev-list", "--reverse", "--no-merges", "HEAD", f"^{full}", f"^{base}"
    )
    for later in (out or "").split():
        touched = git(
            root, "diff-tree", "--no-commit-id", "--name-only", "-r", "-z", later
        )
        for path in (touched or "").split("\0"):
            if not path:
                continue
            if not path.startswith(f"{item}/") or (
                allowed is not None and path not in allowed
            ):
                return ("after", later, path)
    return None


def follows_reason(found, what, outside="the work item's records"):
    """The sentence `follows`'s answer is refused with, about `what`."""
    kind, sha, path = found
    if kind == "unseen":
        return f"{what} names `{sha}`, which this repository cannot resolve"
    if kind == "off":
        return f"{what} names `{sha}`, which HEAD does not descend from"
    return (
        f"{what} is behind HEAD: commit {sha[:8]} after it touches `{path}`, "
        f"outside {outside}"
    )


def frame_foot(reader, text):
    """(the `Framed` mark as (when, who) or None, [(when, who, round)] for
    every `Reframed` line under it), read from the last non-empty line up."""
    reframes = []
    for line in reversed(reader.gfm_lines(text or "")):
        line = line.strip()
        if not line:
            continue
        r = REFRAME_RE.match(line)
        if r:
            reframes.append((r.group(1).strip(), r.group(2).strip(), int(r.group(3))))
            continue
        m = MARK_RE.match(line)
        mark = (m.group(1).strip(), m.group(2).strip()) if m else None
        return mark, list(reversed(reframes))
    return None, list(reversed(reframes))


def frame(reader, routing, root, item, declared):
    """[problem] for a declaration that says a framer drew the frame."""
    if declared.get("planning") != routing.BY_FRAMER:
        return []
    who = f"`{routing.PLANNING} | {routing.BY_FRAMER}`"
    problems = []
    spec = read_record(root, f"{item}/{SPEC_FILE}")
    if spec is None:
        problems.append(f"declares {who} and git carries no {item}/{SPEC_FILE}")
    if read_record(root, f"{item}/{PLAN_FILE}") is None:
        problems.append(f"declares {who} and git carries no {item}/{PLAN_FILE}")
    if spec is None:
        return problems
    mark, reframes = frame_foot(reader, spec)
    if mark is None:
        problems.append(
            f"{item}/{SPEC_FILE} does not end with `Framed <date> by <who>, before "
            "the build.`, with any `Reframed <date> by <who>, after round <N>.` "
            "lines under it"
        )
    elif mark[0].startswith("<") or mark[1].startswith("<"):
        problems.append(f"{item}/{SPEC_FILE} ends with the template's unfilled mark")
    elif mark[1] != routing.BY_FRAMER:
        problems.append(
            f"{item}/routing.md says {who} and {item}/{SPEC_FILE}'s mark says `{mark[1]}`"
        )
    for when, by, n in reframes:
        line = f"`Reframed {when} by {by}, after round {n}.`"
        if when.startswith("<") or by.startswith("<"):
            problems.append(
                f"{item}/{SPEC_FILE}'s foot carries the unfilled line {line}"
            )
        elif by != routing.BY_FRAMER:
            problems.append(
                f"{item}/routing.md says {who} and {item}/{SPEC_FILE}'s foot says {line}"
            )
    return problems


RULE_CHANGES_SAYS = (
    "`## Rule changes` does not parse, so `settle` cannot group this design by the "
    "sections it names and the settle has to read it whole: {reason}"
)


def rule_changes_read(reader, root, item):
    """[(path, line, problem)] for the work item's `frame/design.md` whose
    `## Rule changes` section `rule_changes.parse`, the one reader `settle`
    groups by, refuses; [] where git carries no design. The reader is reached
    through `unverified_check.py#rule_changes`, which raises where it will
    not load."""
    rel = f"{item}/{SPEC_FILE}"
    text = read_record(root, rel)
    if text is None:
        return []
    parsed = reader.rule_changes().parse(text, reader.policy_root(root))
    return [
        (rel, line, RULE_CHANGES_SAYS.format(reason=reason))
        for line, reason in parsed.errors
    ]


def rule_changes_of(reader, root, items):
    """[(path, line, problem)] from `rule_changes_read` over every work item
    directory of ITEMS, or None where the reader would not load, which is
    said on stderr."""
    found = []
    try:
        for item in items:
            found.extend(rule_changes_read(reader, root, item))
    except (OSError, SyntaxError, ImportError, SystemExit) as exc:
        print(
            f"chain-check: the rule-changes reader would not load ({exc})",
            file=sys.stderr,
        )
        return None
    return found


def edited_work_items(root, base, paths, moved, routing):
    """The work item directories whose `frame/design.md` this pull request's
    own commits add or change: each path of PATHS that is
    `<WORK_ITEMS>/<id>/frame/design.md` exactly, is not in MOVED, and that
    `carried_by` leaves this pull request's, in the order of PATHS."""
    depth = len(routing.WORK_ITEMS.split("/")) + 1 + len(SPEC_FILE.split("/"))
    return [
        p[: -len(SPEC_FILE) - 1]
        for p in paths
        if p.startswith(f"{routing.WORK_ITEMS}/")
        and len(p.split("/")) == depth
        and p.endswith(f"/{SPEC_FILE}")
        and p not in moved
        and carried_by(root, base, p) is None
    ]


def verdict_problems(root, path, f):
    """[(path, line, problem)] for one finding's verdict: `open`; a `fixed`
    whose commit HEAD does not descend from; a `fixed` whose commit changed
    no path the `location:` names or lies under, named with what it did
    change."""
    kind, commit = f.verdict
    if kind == OPEN:
        return [
            (
                path,
                f.line,
                f"{f.heading} {DASH} reads `{VERDICT_ROW} {OPEN}`: the fix pass "
                f"answers it with another verdict, and "
                f"{GRAMMAR[VERDICT_ROW].refused}",
            )
        ]
    if kind != FIXED:
        return []
    if not is_ancestor(root, commit, "HEAD"):
        return [
            (
                path,
                f.line,
                f"{f.heading} {DASH} reads `{VERDICT_ROW} {FIXED} {commit}`, and "
                f"HEAD does not descend from `{commit}`: a `{FIXED}` names "
                "a commit on this branch",
            )
        ]
    changed_paths = touched(root, commit) or []
    if any(under(p, q) for p in changed_paths for q in f.paths):
        return []
    named = ", ".join(f"`{q}`" for q in f.paths)
    did = ", ".join(f"`{p}`" for p in changed_paths) or "nothing git can list"
    return [
        (
            path,
            f.line,
            f"{f.heading} {DASH} reads `{VERDICT_ROW} {FIXED} {commit}`, and "
            f"`{commit}` touches no path its `{LOCATION_ROW}` names ({named}): it "
            f"changed {did}. A fix that went elsewhere appends that coordinate "
            f"to the `{LOCATION_ROW}` line",
        )
    ]


def records(reader, routing, root, item, rel, base):
    """[(path, line, problem)] for a work item declared through the review
    chain: no record; a record `round_of` cannot read; a finding at `open`;
    a `fixed` naming a commit HEAD does not descend from, or one that
    changed no path the finding's `location:` names or lies under; what
    `channel` names between the rounds, a `fixed` of the last record located
    in the work item's own records alone, whose commit touched them alone,
    passing as read at HEAD by the sealer; a last record behind HEAD. A finding is named by its line
    and its heading."""
    found = round_records(routing, root, item)
    if not found:
        return [
            (
                rel,
                0,
                f"declares `{routing.CHAIN}` and {item}/{routing.ROUNDS_DIR}/ "
                "holds no `round-N.md`",
            )
        ]
    problems, rounds = [], []
    for path in found:
        text = read_record(root, path)
        number = routing.round_number(path)
        read, errors = round_of(reader, text, path, number)
        rounds.append(read)
        problems.extend(errors)
        for f in read.findings:
            problems.extend(verdict_problems(root, path, f))
    problems.extend(
        channel(
            rounds,
            lambda f: (
                located_in_records(item, f) and records_only(root, item, f.verdict[1])
            ),
        )
    )
    last = rounds[-1]
    # A record naming no commit it reviewed was refused by `read_whole`.
    if last.target is not None:
        behind = follows(root, last.target, base, item)
        if behind is not None:
            problems.append(
                (
                    last.path,
                    0,
                    follows_reason(behind, f"the last round's `{TARGET_ROW}`")
                    + (f"; {VERIFYING_ROUND}" if behind[0] == "after" else ""),
                )
            )
    return problems


# The parity arm at the pull request (#988). Under a routing declaration
# answering the review chain, each round record carries the comparison on its
# `original:` line, which these read.
NO_ORIGINAL = (
    f"no `{ORIGINAL_ROW}` line: `{{config}}` declares a migration and this "
    "pull request changes a path outside the document roots, so each round "
    f"record carries `{ORIGINAL_ROW} {{sha}}`, the migration config's "
    "baseline, written by the proofer once it compared the round's target "
    "with the original through `legacy-parity`"
)
OTHER_ORIGINAL = (
    f"`{ORIGINAL_ROW} {{said}}` names a commit other than the migration "
    "config's `Baseline commit`, {sha}: the line names the commit this round "
    "compared against, and a comparison against another original proves "
    "nothing"
)
NO_BASELINE = (
    "{why}: the migration config names the baseline every round record's "
    f"`{ORIGINAL_ROW}` line is compared with"
)


def parity_readers():
    """`(config, gate)`: `hooks/lib/config.py` and `hooks/lib/gate.py`, loaded by path.
    `gate.py` imports nothing since #1027, so the order no longer matters.
    Raises what `load` raises."""
    config = load(os.path.join(HOOKS, "config.py"), "agentic_config_for_parity")
    gate = load(os.path.join(HOOKS, "gate.py"), "agentic_gate_for_parity")
    return config, gate


NO_GUARANTEE_ORIGINAL = (
    f"no `{ORIGINAL_ROW}` line: `{{config}}` declares a migration, this work "
    "item answers `straight to the PR`, and this pull request changes a path "
    "outside the document roots, so no round record compares it and the "
    f"sealer's guarantee carries `{ORIGINAL_ROW} {{sha}}`, the migration "
    "config's baseline, written once it compared the audited commit with the "
    "original through `legacy-parity`"
)


def original_of(reader, text, rel, sha, config, missing=NO_ORIGINAL):
    """[(rel, line, problem)] for one record's `original:` line, held
    against SHA, the `Baseline commit` of the migration config at CONFIG:
    a record with no such line, said as MISSING, and one naming a commit
    that is not a prefix of SHA and of which SHA is not a prefix. The record
    is a round record, or the guarantee of a work item declaring `straight
    to the PR`, read by the same rule. A line the grammar table refuses,
    standing in a finding or a second one, is `read_whole`'s refusal at that
    line, and none is added here. A line that opens like the label and is
    not it is no `original:` line, so a record holding only such a line
    holds none (#1121's R9)."""
    lines, _found, _errors, outside = read_whole(reader, text, rel)
    at = [i for i, line in enumerate(lines) if label_of(line) == ORIGINAL_ROW]
    if not at:
        return [(rel, 0, missing.format(config=config, sha=sha))]
    found = outside[ORIGINAL_ROW]
    if found is None:
        return []
    said = found["commit"]
    if said.startswith(sha) or sha.startswith(said):
        return []
    return [(rel, at[0] + 1, OTHER_ORIGINAL.format(said=said, sha=sha))]


def originals_of(reader, routing, root, paths, items, direct=()):
    """[(path, line, problem)] for the round records of ITEMS, each declared
    through the review chain, and the `guarantee.md` of DIRECT, each
    declared `straight to the PR`, where git carries the migration config at
    HEAD and PATHS, this pull request's, reach outside the document roots;
    `hooks/lib/gate.py#touches_code` decides that, and paths git could not list
    reach outside them. A guarantee git does not carry is `guarantee`'s
    refusal, and none is added here. A config whose `Baseline commit` names
    no SHA is one refusal naming it. None where `hooks/` would not load,
    said on stderr."""
    config = f"{routing.optin.HOME}/{routing.optin.PARITY_CONFIG}"
    text = read_record(root, config)
    if text is None or not (items or direct):
        return []
    try:
        reads, gate = parity_readers()
    except (OSError, SyntaxError, ImportError, SystemExit) as exc:
        print(
            f"chain-check: the parity readers would not load ({exc})", file=sys.stderr
        )
        return None
    if not gate.touches_code(paths):
        return []
    sha, why = reads.baseline_commit(text)
    if sha is None:
        return [(config, 0, NO_BASELINE.format(why=why))]
    found = []
    for item in items:
        for rel in round_records(routing, root, item):
            found.extend(original_of(reader, read_record(root, rel), rel, sha, config))
    for item in direct:
        rel = f"{item}/{GUARANTEE_FILE}"
        said = read_record(root, rel)
        if said is not None:
            found.extend(
                original_of(reader, said, rel, sha, config, NO_GUARANTEE_ORIGINAL)
            )
    return found


def broad_gate(reader, root, item, base):
    """[(path, line, problem)] for the work item's `trail/gate.md`: absent,
    a line that begins with `<!--` (`comment_lines`), unreadable, or naming
    a run behind HEAD."""
    rel = f"{item}/{BROAD_GATE_FILE}"
    text = read_record(root, rel)
    if text is None:
        return [
            (
                rel,
                0,
                "git carries no gate record: the orchestrator runs "
                "`seal gate --base <base> --record <item>` before it spawns "
                "the sealer, and the run writes it on a green run",
            )
        ]
    problems = comment_lines(reader, text, rel)
    sha = newest_run(reader, text)
    if sha is None:
        return [*problems, (rel, 0, f"no SHA in its `{BROAD_GATE}` row")]
    behind = follows(root, sha, base, item)
    if behind is None:
        return problems
    return [*problems, (rel, 0, follows_reason(behind, "the newest gate run"))]


def verdicts_of(reader, text):
    """[(line number, line)] for every line outside fences that opens with
    `Verdict:` at the start of the line, exactly, trailing whitespace
    removed. An indent is markup, a code block at four spaces, so an
    indented line is no verdict line; `unread_verdicts` names it with every
    other line that opens like the label."""
    found = []
    for i, raw in enumerate(reader.readable(text or "")):
        line = reader.visible(raw)
        if line.startswith(VERDICT) and not raw[:1].isspace():
            found.append((i + 1, line))
    return found


def unread_verdicts(reader, text, rel):
    """[(rel, line, why)] for each line outside fences that opens like the
    verdict (`OPENS_LIKE_VERDICT`) and that `verdicts_of` does not read, at
    its line. Such a line is prose: whether it meant the verdict is the
    reader's judgment, and the check refuses nothing for it."""
    read = {n for n, _line in verdicts_of(reader, text)}
    return [
        (rel, i + 1, UNREAD_VERDICT.format(said=line))
        for i, raw in enumerate(reader.readable(text or ""))
        if (line := reader.visible(raw))
        and OPENS_LIKE_VERDICT.match(line)
        and i + 1 not in read
    ]


def verdict_word(line):
    """`sealed`, `withheld` or `undecided` where LINE is one of the three
    shapes whole; a word of `RETIRED_VERDICTS` where the value after the
    label, emphasis removed, is that word or opens with it and a space;
    else None."""
    m = VERDICT_SHAPE.fullmatch(line)
    if m:
        return next(word for word in m.groups() if word)
    value = EMPHASIS.sub("", line).split(":", 1)[-1].strip().lower()
    for word in RETIRED_VERDICTS:
        if value == word or value.startswith(word + " "):
            return word
    return None


def target_row(reader, text):
    """`(line number, cell)` of `guarantee.md`'s first `Target SHA` row, or
    `(0, None)`."""
    for i, line in enumerate(reader.readable(text or "")):
        cells = reader.split_row(line)
        if cells and len(cells) > 1 and reader.visible(cells[0]) == TARGET:
            return i + 1, reader.visible(cells[1])
    return 0, None


def guarantee(reader, root, item, base):
    """[(path, line, problem)] for the work item's `guarantee.md`: absent, no
    commit, a commit with anything but the closing records after it, an
    earlier run that is not `EARLIER_ENTRY` whole, a line that begins with
    `<!--` (`comment_lines`), a fence that never closes (`unclosed`), a word
    of `RETIRED_VERDICTS` on its `Verdict:` line, a verdict line in none of
    the three shapes, or one that does not read `sealed`."""
    rel = f"{item}/{GUARANTEE_FILE}"
    text = read_record(root, rel)
    if text is None:
        return [
            (
                rel,
                0,
                "git carries no guarantee file: the sealer writes it from "
                "`templates/records/sdd-guarantee.md` after the orchestrator's broad run",
            )
        ]
    problems = []
    sha = target_of(reader, text)
    if sha is None:
        problems.append((rel, 0, f"no SHA in its `{TARGET}` row"))
    else:
        behind = follows(root, sha, base, item, only=CLOSING_RECORDS)
        if behind is not None:
            problems.append(
                (
                    rel,
                    0,
                    follows_reason(behind, "the guarantee", "the closing records")
                    + ("; the sealer runs again" if behind[0] == "after" else ""),
                )
            )
    # A row with no SHA is refused above; one with a SHA is read whole.
    row, cell = target_row(reader, text)
    for entry, word in earlier_verdicts(cell) if sha else []:
        if word is None:
            problems.append(
                (
                    rel,
                    row,
                    f"`{entry}` on its `{TARGET}` row is not read: the row is "
                    f"{TARGET_WRITTEN}, and nothing else",
                )
            )
    # A comment line is text to the check, and a fence nobody closed hides
    # the verdict line; name each at its line.
    problems.extend(comment_lines(reader, text, rel))
    problems.extend(unclosed(reader, text, rel))
    verdicts = verdicts_of(reader, text)
    if len(verdicts) != 1:
        problems.append(
            (
                rel,
                verdicts[1][0] if verdicts else 0,
                f"{len(verdicts)} `{VERDICT}` lines; the guarantee carries one",
            )
        )
        return problems
    line, value = verdicts[0]
    word = verdict_word(value)
    if word in RETIRED_VERDICTS:
        said = f"`{word}` {RETIRED_SAYS}"
    elif word is None:
        said = f"the line reads only as {VERDICT_SHAPES}, written exactly so"
    elif word != SEALED:
        said = (
            f"a ready pull request needs `{SEALED}`: fix what it names, or answer "
            "its question under it, and the sealer runs again at the new HEAD"
        )
    else:
        return problems
    problems.append((rel, line, f"the sealer's verdict reads `{value}`: {said}"))
    return problems


def local_root(root, routing):
    """The local-mode root of `root`, or "" where the root is shared or absent."""
    optin = routing.optin
    common = optin.git_common_dir(root)
    home = optin.home_at(root, common)
    if not home:
        return ""
    shared, _local = optin.home_paths(root, common)
    return "" if os.path.realpath(home) == os.path.realpath(shared) else home


def tracked_declarations(root, routing):
    """(path, parsed) for every routing declaration git carries at HEAD."""
    out = git(root, "ls-tree", "-r", "-z", "HEAD", "--", f"{routing.WORK_ITEMS}/")
    found = []
    for entry in (out or "").split("\0"):
        meta, _, path = entry.partition("\t")
        parts = meta.split()
        if len(parts) < 3 or parts[0] not in REGULAR:
            continue
        if os.path.basename(path) != routing.FILENAME:
            continue
        parsed = routing.parse(read_record(root, path) or "")
        if parsed:
            found.append((path, parsed))
    return found


def declared_for_this_branch(root, routing):
    """([the one declaration naming this branch], why there is none).

    The branch is `GITHUB_HEAD_REF` in a workflow and the checked-out branch
    elsewhere."""
    branch = os.environ.get("GITHUB_HEAD_REF") or routing.current_branch(root)
    if not branch:
        return [], (
            "the branch could not be read — a detached HEAD with no "
            "GITHUB_HEAD_REF — so no declaration was matched to one"
        )
    matching = [
        p for p, d in tracked_declarations(root, routing) if d["branch"] == branch
    ]
    if len(matching) > 1:
        return [], (
            f"{len(matching)} committed declarations name `{branch}`, which is "
            f"not one answer: {', '.join(sorted(matching))}"
        )
    if not matching:
        home = local_root(root, routing)
        if home:
            return [], (
                f"this repository keeps its root at {home} — local mode, where "
                "nothing under the root is committed. So no routing declaration "
                f"for `{branch}` can be read from what git carries, and the "
                "review-chain check examined nothing. `seal mode shared` moves "
                "the root into the tree and gets the check running."
            )
        return [], (
            "this pull request declared neither way, so the review-chain check "
            f"examined nothing. Nothing git carries under `{routing.WORK_ITEMS}/` "
            f"declares `{branch}`. Add {routing.WORK_ITEMS}/<work-item>/"
            f"{routing.FILENAME} to declare."
        )
    return matching, ""


SETTLE_SAYS = (
    "retired: a settle — the work item's directory stood at the merge base "
    "and is gone whole"
)

# The pull request that moves the root to local mode deletes every
# declaration with the root (#952).
ROOT_LEFT_SAYS = (
    "the tree the check reads has no top-level `{home}` entry, so nothing is "
    "declared: the routing declarations this pull request deletes left the "
    "tree with the root, and the review-chain check judged the commit "
    "trailers and nothing else"
)

# The trailer a session's commit ends with (`docs/the-routing-check.md` *At
# the pull request*), and its one value that names no work item.
TRAILER = "Seal-Routing"
NO_WORK_ITEM = "no work item"
UNDECLARED_TRAILER = (
    f"commit {{sha}} carries `{TRAILER}: {{item}}`, and no routing declaration "
    "this pull request judges names that work item: commit its `routing.md`, "
    "naming this branch, or correct the trailer"
)
LOCAL_TRAILER = (
    f"commit {{sha}} carries `{TRAILER}: {{item}}` in a repository whose root "
    "is local, where no routing declaration is committed for it to name: "
    "printed, not judged"
)
NO_WORK_ITEM_TRAILER = (
    f"commit {{sha}} carries `{TRAILER}: {NO_WORK_ITEM}`: its session recorded "
    "that the change belongs to no work item, and nothing here checks it "
    "further"
)


def routing_trailers(root, base):
    """`[(commit, value)]` for each `Seal-Routing` trailer of this pull
    request's own commits, oldest first, or None where git cannot list them.

    The commits are `base..HEAD` with merges left out, read by git's own
    trailer parser so the key matches as git matches it. A commit someone
    other than its author committed is not judged: a person's cherry-pick or
    rebase of a session's commit, and GitHub's squash or rebase-merge, carry
    a trailer their committer did not write, and a session's own commit is
    committed by its author (round 1 of #1027, finding 2). The two emails are
    compared as git records them, case-folded, so a session whose committer
    email differs from its author email is not judged either."""
    out = git(
        root,
        "log",
        "--no-merges",
        "--reverse",
        "-z",
        "--format=%H%x1f%ae%x1f%ce%x1f%(trailers:"
        f"key={TRAILER},valueonly,separator=%x1e)",
        f"{base}..HEAD",
    )
    if out is None:
        return None
    found = []
    for entry in out.split("\0"):
        parts = entry.strip("\n").split("\x1f")
        if len(parts) != 4:
            continue
        sha, author, committer, values = parts
        if author.strip().lower() != committer.strip().lower():
            continue
        for value in values.split("\x1e"):
            if value.strip():
                found.append((sha.strip(), value.strip()))
    return found


def trailer_findings(trailers, judged, local=False):
    """`(problems, notices)` for TRAILERS, each `(commit, value)`: a value
    naming a work item that is not among JUDGED, the ids of the declarations
    this pull request judges, is a problem; `no work item` is a notice. Where
    LOCAL, the root is under the common git directory and no declaration is
    ever committed, so a work item's value is a notice too (round 1 of #1027,
    finding 1)."""
    problems, notices = [], []
    for sha, value in trailers:
        if value == NO_WORK_ITEM:
            notices.append(("", 0, NO_WORK_ITEM_TRAILER.format(sha=sha[:8])))
        elif local:
            notices.append(("", 0, LOCAL_TRAILER.format(sha=sha[:8], item=value)))
        elif value not in judged:
            problems.append(("", 0, UNDECLARED_TRAILER.format(sha=sha[:8], item=value)))
    return problems, notices


def retired(reader, root, fork, records):
    """The work item directories of the removed declarations that read as a
    settle: each stood at the merge base and is gone whole, asked of the one
    predicate, `unverified_check.py#settled`. RECORDS maps each declaration
    to its text at HEAD; a directory the disk still holds is a deletion of
    part of it, and never reaches the predicate."""
    gone = [os.path.dirname(rel) for rel, text in records.items() if text is None]
    gone = [d for d in gone if not os.path.isdir(os.path.join(root, d))]
    return reader.settled(root, fork, gone)


def main(argv=None):
    """The check. Returns the exit code."""
    ap = argparse.ArgumentParser(
        prog="chain-check",
        description="At the pull request: the declared parties left the records "
        "they owe, and the records agree with HEAD.",
    )
    ap.add_argument("--baseline", metavar="REF", required=True)
    ap.add_argument("--root", default=".")
    ap.add_argument("--worktree", action="store_true")
    ap.add_argument(SEALING, action="store_true")
    args = ap.parse_args(argv)
    global WORKTREE
    WORKTREE = args.worktree

    reader = SHARED_READER
    try:
        routing = load(ROUTING, "agentic_routing")
    except (OSError, SyntaxError, ImportError, SystemExit) as exc:
        print(f"chain-check: the shared reader would not load ({exc})", file=sys.stderr)
        return 2
    root = reader.repo_root(os.path.abspath(args.root))
    if root is None:
        print(f"chain-check: {args.root} is not in a git repository", file=sys.stderr)
        return 2
    if not reader.resolves(root, args.baseline):
        print(
            f"chain-check: --baseline {args.baseline} does not resolve in {root}; "
            "a shallow checkout lands here",
            file=sys.stderr,
        )
        return 2
    diff = changed(root, args.baseline)
    if diff is None:
        print(f"chain-check: cannot diff against {args.baseline}", file=sys.stderr)
        return 2
    paths, moved = diff
    own, why = declared_for_this_branch(root, routing)
    # A declaration naming this branch is always this pull request's; any
    # other one another pull request's squash carried was judged there.
    declarations, carried = set(own), []
    for rel in changed_routing(paths, moved, routing.WORK_ITEMS):
        by = None if rel in own else carried_by(root, args.baseline, rel)
        if by:
            said = CARRIED_SAYS.format(sha=by[0][:8], subject=by[1])
            carried.append((rel, 0, said))
        else:
            declarations.add(rel)
    declarations = sorted(declarations)
    # Where the tree the check reads has no top-level `seal` entry, nothing is
    # declared: the pull request moving the root to local mode leaves it so.
    # That tree is HEAD, and the working tree under `--worktree`, where
    # `read_record` and `changed` read the declarations from. An entry is
    # anything at that name, a file or a link as much as a directory, so a
    # `seal` that is not a directory keeps the declarations judged. Where git
    # cannot answer, `git()` is None and the declarations stay judged.
    home = routing.optin.HOME
    if WORKTREE:
        gone = not os.path.lexists(os.path.join(root, home))
    else:
        gone = git(root, "ls-tree", "HEAD", "--", home) == ""
    if declarations and gone:
        declarations, why = [], ROOT_LEFT_SAYS.format(home=home)

    state, where = pull_request_state(root)
    unseen = state == "unknown" and not event_payload_present()
    strict = state != "draft" and not unseen
    print(
        f"chain-check: {UNSEEN_SAYS} ({where})"
        if unseen
        else f"chain-check: judged as a {'draft' if state == 'draft' else 'ready'} "
        f"pull request ({where})"
    )
    if WORKTREE:
        print("chain-check: reading the working tree (--worktree); CI reads HEAD")
    for rel, line, message in carried:
        print(reader.annotate("notice", rel, line, message))
    trailers = routing_trailers(root, args.baseline)
    if trailers is None:
        print(
            f"chain-check: cannot read the commits after {args.baseline}",
            file=sys.stderr,
        )
        return 2
    judged_ids = {os.path.basename(os.path.dirname(rel)) for rel in declarations}
    problems, notices = trailer_findings(
        trailers, judged_ids, local=bool(local_root(root, routing))
    )
    kind = "error" if strict else "notice"
    if not declarations:
        print(reader.annotate("notice", "", 0, why))
        for rel, line, message in notices:
            print(reader.annotate("notice", rel, line, message))
        for rel, line, message in problems:
            print(reader.annotate(kind, rel, line, message))
        return 1 if problems and strict else 0

    fork = reader.merge_base(root, args.baseline)
    # A declared work item's commit can write another work item's section
    # without touching its `routing.md`, so the diff's designs are read too.
    judged = {os.path.dirname(rel) for rel in declarations}
    edited = [
        item
        for item in edited_work_items(root, args.baseline, paths, moved, routing)
        if item not in judged
    ]
    chained, direct = [], []
    texts = {rel: read_record(root, rel) for rel in declarations}
    by_settle = retired(reader, root, fork, texts)
    for rel in declarations:
        item = os.path.dirname(rel)
        text = texts[rel]
        if text is None:
            if item in by_settle:
                notices.append((rel, 0, SETTLE_SAYS))
            else:
                problems.append(
                    (
                        rel,
                        0,
                        "git does not carry this file at HEAD: a declaration CI "
                        "cannot open is not a declaration",
                    )
                )
            continue
        declared = routing.parse(text)
        if declared is None:
            problems.append(
                (
                    rel,
                    0,
                    "not a readable declaration: it needs a `Review`, a "
                    "`Destination` and a `Branch` row",
                )
            )
            continue
        problems.extend(
            (rel, 0, p) for p in frame(reader, routing, root, item, declared)
        )
        found = rule_changes_of(reader, root, [item])
        if found is None:
            return 2
        problems.extend(found)
        if declared["review"] == routing.CHAIN:
            problems.extend(records(reader, routing, root, item, rel, args.baseline))
            chained.append(item)
        else:
            direct.append(item)
        notices.extend(unread(reader, routing, root, item, item in chained))
        gate = broad_gate(reader, root, item, args.baseline)
        gate += guarantee(reader, root, item, args.baseline)
        if args.sealing:
            notices.extend((p, n, f"{SEALING_SAYS}: {m}") for p, n, m in gate)
        else:
            problems.extend(gate)
    found = rule_changes_of(reader, root, edited)
    if found is None:
        return 2
    problems.extend(found)
    found = originals_of(reader, routing, root, paths, chained, direct)
    if found is None:
        return 2
    for rel, line, message in found:
        # The guarantee's line is the sealer's to write, so `--sealing` reads
        # it as it reads every other guarantee check.
        if args.sealing and rel.endswith(f"/{GUARANTEE_FILE}"):
            notices.append((rel, line, f"{SEALING_SAYS}: {message}"))
        else:
            problems.append((rel, line, message))

    for rel, line, message in notices:
        print(reader.annotate("notice", rel, line, message))
    for rel, line, message in problems:
        print(reader.annotate(kind, rel, line, message))
    return 1 if problems and strict else 0


if __name__ == "__main__":
    sys.exit(main())
