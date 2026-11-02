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
                no such section, and a work item with no design, pass, and a
                heading near `## Rule changes` outside the section is another
                section; in a section that parses, each `check:` line inside
                an `add` or `change` `to` is read by `.github/scripts/rules.py`,
                the reader `seal rules --check` uses, and a line it refuses is
                refused at its line in the design (`check_lines_in`); a `from`
                is read for no check line; and against each operation, the
                string constants of the tracked tests under `tests/` and the
                rule documents are read from the working tree, to name its
                test pins and copies (`pins_and_copies_in`)
  records       `Review | through the review chain`: `trail/rounds/` holds at least
                one `round-N.md`; each reads whole through
                `hooks/lib/fields.py`, its blocks placed by its `## Findings`
                section and finding headings (`round_read`), and every
                finding has a close block; a `fixed` commit is on the branch
                and touches a path its finding's or its close's `location:`
                line names; every `fixed` or `rejected` finding
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
                and one `original:` line naming it stands in the round block
                of every round record under `Review | through the review
                chain`, and in
                the newest verdict block of `guarantee.md` under `Review |
                straight to the PR` (`originals_of`, `guarantee_original`)
  broad gate    the last run block of `trail/gate.md`, the newest run, read
                through `hooks/lib/fields.py`, is HEAD, or every commit after
                it touches only the work item's own directory; a record with
                no run block, or with a line the reader refuses, fails
  guarantee     the last verdict block of `guarantee.md`, the newest run of
                the sealer, read through `hooks/lib/fields.py`, names HEAD,
                or every commit after it touches only the closing records,
                and its `Verdict:` reads `sealed`; a guarantee with no
                verdict block, or with a line the reader refuses, fails

A ready pull request fails on any of them. A draft, or a run that observed no
pull request, prints the same lines and exits 0. `docs/the-review-record.md`
states the record and the rules these arms hold.

In a round record, `guarantee.md` and `trail/gate.md` a field stands in a
`seal` block, every line of which parses or is refused at its line, and a
line outside every block is prose to every arm. A fence like the block's and
not it, and a file under `trail/rounds/` that is no `round-N.md`, are not
read; the check names each (`blocks_of`, `unread`) and decides nothing on
it. What such a fence meant is the judgment of the agent that reads the
record. The same holds for each line `rule_changes.parse` names in a design
the rule-changes arm reads, a heading near `## Rule changes` among them
(`rule_changes_read`), for each line of an `add` or `change` `to` that
`rules.py` names as opening like a check line and not being one
(`check_lines_in`), and for what the pin and copy reading could not read:
a listing git could not make, a test file under `tests/` it could not
open, decode or parse, a rule document it could not open or decode, and
the section a `remove` with no `from` takes out where the working tree
lacks its document or its heading. A design's operation that takes a
test's string constant of four words or more out of the policy root, and
an `add` or `change` `to` that shares a run of 15 words with another rule
document as the design's own removals leave it, read as
`tests/text/test_no_passage_is_pasted_into_a_second_file.py` reads one, are
named as notices at their lines in the design and refuse nothing
(`pins_and_copies_in`): whether a named pin or copy is a finding is the
proofer's judgment at review.

Usage:
  chain_check.py --baseline <ref> [--root DIR] [--worktree] [--sealing]

`--worktree` reads the records from the working tree instead of HEAD, for a
check before the commit; CI never passes it. `--sealing` is the broad gate's
own run, before it writes `trail/gate.md` and the sealer `guarantee.md`: those
two arms, and the guarantee's `original:` line, print and do not fail.

Exit: 0 nothing to refuse · 1 a refusal, each named `path:line  why` (a
GitHub annotation in CI) · 2 the check could not run, a reader that will not
load among the causes. A line or a file the check did not read is printed
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
    # Before the readers load below: a refusal printed at import must not
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
FIELDS_READER = os.path.join(HOOKS, "fields.py")
# `.github/scripts/rules.py`, the one reader of a `check:` line, which `seal
# rules --check` runs over the rule files. A user's CI clones the plugin
# whole, so it stands here there too (`templates/setup/hygiene.yml`).
CHECK_LINES_READER = os.path.join(
    HERE, "..", "..", "..", ".github", "scripts", "rules.py"
)

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
# A round record's fields stand in `seal` blocks, and `hooks/lib/fields.py`
# is the one spelling of their grammar (#1198). What this file holds is where
# a block stands, which turns on headings that module does not read: the one
# `## Findings` section, and a finding's `### <n>. <symptom>` heading in it,
# whose number names the finding across rounds.
FINDINGS_HEADING = "## Findings"
FINDING_LEVEL = 3
FINDING_HEADING = re.compile(r"### (?P<number>[1-9][0-9]*)\. .+")
ROUND_TEMPLATE = "templates/records/sdd-round.md"
# One finding as `round_read` reads it: the line of its close's `verdict:`,
# or of its heading where it has no close, its heading and the heading's
# number, the verdict, the paths of its finding's and its close's
# `location:`, its `regression:` reference and its `reopens:` reference,
# each with that line's number, where it has one, the line of its heading,
# and the paths of its finding's `location:` alone. `paths` is where the
# defect shows and where the fix went, which the pull-request check reads;
# `located` is where the defect shows, which a count of findings by place
# reads (`.github/scripts/finding_counts.py`).
Finding = collections.namedtuple(
    "Finding",
    "line heading number verdict paths regression regression_line reopens "
    "reopens_line heading_line located",
)
# One record as `channel` reads it: its path and number, its findings, the
# numbers of every `### <n>. ` heading it holds, its `confirms:` references,
# and the commit its round block's `target:` names.
Round = collections.namedtuple("Round", "path number findings held confirms target")
# One record as `round_read` reads it: its findings, its errors, its round
# block, the numbers of its finding headings, its `confirms:` references,
# its `## Findings` section and each finding's span in it, the blocks
# outside every finding, and the blocks of each finding's span by index.
Parsed = collections.namedtuple(
    "Parsed", "findings errors round held confirms section spans outside inside"
)
# The verdict words the check decides on: a finding with no close block is
# `open`, which fails a ready pull request; `fixed` and `rejected` owe the
# next round a reference, `deferred` owes nothing. What follows each is the
# close block's `verdict:` shape's.
OPEN = "open"
FIXED = "fixed"
REJECTED = "rejected"
DEFERRED = "deferred"
DASH = chr(0x2014)
ISSUE_RE = re.compile(r"#(\d+)")

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


# Loaded once, here, and read by `main` and by every importer through this
# name. As a command, a reader that will not load ends the run at exit 2
# naming the file; imported, the error is raised and the importer decides
# what a check that cannot read a record means to it.
try:
    SHARED_READER = load(READER, "agentic_unverified_reader_for_grammar")
    # `hooks/lib/fields.py`, the one reader of a record's `seal` blocks.
    FIELDS = load(FIELDS_READER, "agentic_fields_for_the_chain")
except (OSError, SyntaxError, ImportError, SystemExit) as _exc:
    if __name__ != "__main__":
        raise
    print(f"chain-check: the shared reader would not load ({_exc})", file=sys.stderr)
    raise SystemExit(2) from None

# What the check prints of a file it did not read. `main` prints it as a
# notice, `path:line  not read: <why>` and a notice annotation in CI, and it
# changes no exit code; a fence like a `seal` block and not one is named in
# `hooks/lib/fields.py`'s words (`blocks_of`).
UNREAD_FILE = (
    "not read: `{name}` is no `round-N.md`, so the check read nothing of it "
    "and judged the work item on the records it did read"
)
# What the records arm refuses of where a round record's blocks stand. A
# refusal in a finding is led by its heading.
NO_ROUND_BLOCK = (
    "no round block: since #1198 a round record's fields stand in `seal` "
    "blocks, its `target:` line in the round block outside every finding, as "
    f"`{ROUND_TEMPLATE}` shows; a record written before then is rewritten "
    "into blocks with its verdicts unchanged"
)
SECOND_ROUND = "a second round block: a round record holds one, outside every finding"
NO_FINDINGS = (
    f"no `{FINDINGS_HEADING}` section: a round record holds one, with a "
    "`### <n>. <symptom>` section in it for each finding"
)
TWO_FINDINGS = f"a second `{FINDINGS_HEADING}` section; a round record holds one"
NO_NUMBER = (
    "no number: a finding's heading reads `### <n>. <symptom>`, and a later "
    "round names it by that `n`"
)
SECOND_NUMBER = (
    "a second finding numbered {number}: a later round's `round-<N>#{number}` "
    "would name both"
)
NO_FINDING_BLOCK = (
    "no finding block: under its heading a finding holds one `seal` block "
    f"opening with `severity:`, as `{ROUND_TEMPLATE}` shows"
)
SECOND_BLOCK = "a second {kind} block: a finding holds one"
INSIDE = "a {kind} block inside a finding: it stands outside every finding"
OUTSIDE = (
    "a {kind} block outside every finding: it stands in its finding's "
    f"`### <n>. <symptom>` section of `{FINDINGS_HEADING}`"
)
OPEN_SAYS = (
    "no close block, so the finding is open: the fix pass appends one after "
    "its paste-ready fix, opening with `verdict:` and reading "
    "`fixed <commit>`, `rejected` or `deferred <home>`"
)


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
    `round-N.md` (`UNREAD_FILE`) and each fence of a round record like a
    `seal` block and not one (`blocks_of`). `main` prints them as notices;
    such a fence of `guarantee.md` or `trail/gate.md` is named by
    `guarantee` and `broad_gate`."""
    found = []
    if chained:
        records, others = rounds_listed(routing, root, item)
        found += [
            (rel, 0, UNREAD_FILE.format(name=rel.rsplit("/", 1)[-1])) for rel in others
        ]
        for rel in records:
            blocks_of(rel, read_record(root, rel) or "", FIELDS.ROUND_RECORD, found)
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


def table_rows(reader, lines):
    """Every table row in already-`readable` lines, as lists of cells."""
    out = []
    for line in lines:
        cells = reader.split_row(line)
        if cells is not None:
            out.append(cells)
    return out


def reference(found):
    """`(round, finding or None)` from a reference's match."""
    number = found["finding"]
    return int(found["round"]), int(number) if number else None


def issue_of(home):
    """N where a deferral's home is exactly `#N`, else None."""
    found = ISSUE_RE.fullmatch(home or "")
    return int(found.group(1)) if found else None


def location_paths(value):
    """The paths one `location:` value names, in order: each backticked
    item to its first `:`, which the value's shape keeps out of a path. The
    value is one `hooks/lib/fields.py` already matched whole."""
    return [item.strip("`").split(":")[0] for item in value.split(", ")]


def sections_of(reader, lines, heading):
    """The index of every heading of already-`readable` lines that reads
    HEADING."""
    return [i for i, said in reader.headings(lines) if said.strip() == heading]


def finding_spans(reader, lines):
    """`((start, end), [(first, stop)], error)` for the one `## Findings`
    section of already-`readable` lines: where it stands, and each `### `
    section in it, from its heading to the next. `error` is the refusal for
    a record with no such section or with two, and the spans are then
    empty."""
    starts = sections_of(reader, lines, FINDINGS_HEADING)
    if not starts:
        return None, [], (0, NO_FINDINGS)
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
    """The `n` of a finding heading that reads `### <n>. <symptom>`, or
    None."""
    found = FINDING_HEADING.fullmatch(heading)
    return int(found["number"]) if found else None


# The refusals `hooks/lib/fields.py` makes of a line outside every block. A
# refusal of a block's line leaves the finding holding it unread, and these
# do not; the last two hide every block below their line.
HIDING = (FIELDS.UNCLOSED, FIELDS.UNSURE)
NOT_A_BLOCK_LINE = (FIELDS.COMMENT_LINE, *HIDING)


def round_read(reader, text, rel):
    """`Parsed` for one round record: its `seal` blocks read through
    `hooks/lib/fields.py`, placed by its headings, read once.

    Every line that module refuses is an error at its line, led by the
    finding's heading where it stands in one. The one `## Findings` section
    is split at its `### ` headings: a heading that is not `### <n>.
    <symptom>`, or whose number an earlier heading carries, is refused at the
    heading, and `finding_of` reads the rest. A round or confirmation block
    inside a finding, and a finding or close block outside every finding,
    are refused at their opener, and so is a second round block. A record
    with no round block, where nothing else was refused, is refused with
    `NO_ROUND_BLOCK` alone and read no further: it is a record of an older
    shape, or one written past the template. A finding with an error is not
    in the list, nor one holding a block line the reader refused or a block
    out of its place. Below a fence that never closes, or one the walk could
    not place, no block is read: a finding reaching it is read for the
    blocks above it, and what it lacks is not refused again."""
    lines = reader.readable(text or "")
    read = FIELDS.read(text or "", FIELDS.ROUND_RECORD)
    section, spans, error = finding_spans(reader, lines)
    held = {finding_number(lines[first].strip()) for first, _stop in spans}
    held.discard(None)

    def span_of(line):
        """The index of the span holding 1-based LINE, or None."""
        return next(
            (k for k, (first, stop) in enumerate(spans) if first < line - 1 < stop),
            None,
        )

    def led(k, why):
        return f"{lines[spans[k][0]].strip()} {DASH} {why}"

    errors, spoilt = [], set()
    for line, why in read.refusals:
        k = span_of(line)
        if k is not None and why not in NOT_A_BLOCK_LINE:
            spoilt.add(k)
            why = led(k, why)
        errors.append((rel, line, why))
    # Below a fence that never closes, which a renderer runs to the end of
    # the file, or one the walk could not place, no block is read.
    blind = min((line for line, why in read.refusals if why in HIDING), default=None)
    outside, inside, rounds, confirms = [], {k: [] for k in range(len(spans))}, [], []
    for block in read.blocks:
        if blind is not None and block.line > blind:
            continue
        k = span_of(block.line)
        in_finding = block.kind in (FIELDS.FINDING_BLOCK, FIELDS.CLOSE_BLOCK)
        if k is None and in_finding:
            errors.append((rel, block.line, OUTSIDE.format(kind=block.kind.name)))
        elif k is not None and not in_finding:
            spoilt.add(k)
            said = INSIDE.format(kind=block.kind.name)
            errors.append((rel, block.line, led(k, said)))
        elif k is not None:
            inside[k].append(block)
        else:
            outside.append(block)
            if block.kind is FIELDS.ROUND_BLOCK:
                rounds.append(block)
            elif (said := block.fields[FIELDS.CONFIRMS]).match["round"]:
                confirms.append((said.line, reference(said.match)))
    if not rounds and not errors:
        return Parsed(
            [],
            [(rel, 0, NO_ROUND_BLOCK)],
            None,
            held,
            [],
            section,
            spans,
            outside,
            inside,
        )
    errors += [(rel, extra.line, SECOND_ROUND) for extra in rounds[1:]]
    if error:
        errors.append((rel, *error))
    found, numbers = [], set()
    for k, (first, stop) in enumerate(spans):
        heading = lines[first].strip()
        number = finding_number(heading)
        if number is None or number in numbers:
            said = NO_NUMBER if number is None else SECOND_NUMBER.format(number=number)
            errors.append((rel, first + 1, led(k, said)))
            continue
        numbers.add(number)
        if k in spoilt:
            continue
        finding, said = finding_of(rel, heading, number, first, inside[k])
        if blind is None or blind > stop:
            errors.extend(said)
        if finding is not None:
            found.append(finding)
    errors.sort(key=lambda error: error[1])
    round_block = rounds[0] if rounds else None
    return Parsed(
        found, errors, round_block, held, confirms, section, spans, outside, inside
    )


def finding_of(rel, heading, number, first, blocks):
    """`(Finding or None, errors)` for the finding numbered NUMBER whose
    HEADING stands at index FIRST, from BLOCKS, its section's finding and
    close blocks in order: a section with no finding block is refused at
    the heading, and a second finding or close block at its opener. The
    verdict is its close block's, `(OPEN, None)` where it has none, its
    `located` is its finding block's `location:` paths in the order written,
    and its `paths` are those followed by its close block's."""
    finds = [b for b in blocks if b.kind is FIELDS.FINDING_BLOCK]
    closes = [b for b in blocks if b.kind is FIELDS.CLOSE_BLOCK]
    lead = f"{heading} {DASH} "
    errors = [
        (rel, b.line, lead + SECOND_BLOCK.format(kind=b.kind.name))
        for b in (*finds[1:], *closes[1:])
    ]
    if not finds:
        errors.append((rel, first + 1, lead + NO_FINDING_BLOCK))
    if errors:
        return None, sorted(errors, key=lambda error: error[1])
    said = finds[0].fields
    located = location_paths(said[FIELDS.LOCATION].value)
    paths = list(located)
    if closes:
        closed = closes[0].fields
        verdict = closed[FIELDS.VERDICT]
        word = verdict.value.split(" ", 1)[0]
        kind = (word, verdict.match["commit"] or verdict.match["home"])
        line = verdict.line
        if FIELDS.LOCATION in closed:
            paths += location_paths(closed[FIELDS.LOCATION].value)
    else:
        kind, line = (OPEN, None), first + 1
    regression, reopens = said.get(FIELDS.REGRESSION), said.get(FIELDS.REOPENS)
    return (
        Finding(
            line,
            heading,
            number,
            kind,
            paths,
            reference(regression.match) if regression else None,
            regression.line if regression else None,
            reference(reopens.match) if reopens else None,
            reopens.line if reopens else None,
            first + 1,
            located,
        ),
        [],
    )


def record_findings(reader, text, rel):
    """`(findings, errors)` of one round record through `round_read`: the
    one reader the arm, the panel and the release seal read a record
    through, so a comment line, a fence that hides blocks, or a record
    naming no commit it reviewed, fails closed for each of them."""
    parsed = round_read(reader, text, rel)
    return parsed.findings, parsed.errors


def round_of(reader, text, rel, number):
    """`(Round, errors)` for one record through `round_read`: its findings,
    the number of every `### <n>. ` heading of its `## Findings`, read or
    refused, so a reference to a refused finding still names one it holds,
    its `confirms:` references, and its round block's commit. A record
    whose round block was refused, or holds none, has no target."""
    parsed = round_read(reader, text, rel)
    block = parsed.round
    target = block.fields[FIELDS.TARGET].match["commit"] if block else None
    read = Round(rel, number, parsed.findings, parsed.held, parsed.confirms, target)
    return read, parsed.errors


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
                    f"round to name, so its `{FIELDS.CONFIRMS}` lines read `none`"
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
                        f"{f.heading} {DASH} reads `{FIELDS.VERDICT} "
                        f"{' '.join(x for x in f.verdict if x)}`, and the next "
                        f"record, {here.path}, names it on no `{FIELDS.CONFIRMS}`, "
                        f"`{FIELDS.REOPENS}` or `{FIELDS.REGRESSION}` line: one of "
                        f"them reads `round-{before.number}#{f.number}`",
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
                        f"{f.heading} {DASH} reads `{FIELDS.VERDICT} "
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
# A line `rule_changes.parse` names as one it did not read, with its reason,
# and a line of a `to` that `rules.py#unread_lines` names.
RULE_CHANGES_UNREAD = "not read: {why}"
# A check line inside an `add` or `change` `to` that `rules.py` refuses.
CHECK_LINE_SAYS = (
    "`.github/scripts/rules.py`, the reader `seal rules --check` uses, refuses "
    "this check line, which the settle writes into `{file}` as it stands: {why}"
)
# A string constant of a test that an operation takes out of the policy root
# and its `to` does not hold (`rule_changes.py#pins`), named at the `from`.
PIN_SAYS = (
    "a test pins text this operation takes out of `{file}`: `{test}:{line}` "
    'holds "{literal}", and the `to` does not'
)
# A run of `passages.py#WINDOW` words a `to` shares with another rule document
# (`rule_changes.py#copies`), named at the `to`.
COPY_SAYS = (
    "this `to` repeats a passage of `{path}`: {count} of its runs of {window} "
    'words stand there, one of them "{run}"'
)
# A test file the pin reading could not parse or decode, after `not read: `.
TEST_UNREAD = "`{path}` could not be read as Python ({why}), so no pin in it is named"
# A rule document the copy reading could not open or decode, after `not read: `.
DOCUMENT_UNREAD = "`{path}` could not be read ({why}), so no copy of it is named"
# The section a `remove` with no `from` takes out, which the pin reading could
# not read in the working tree, after `not read: `.
SECTION_UNREAD = (
    "the section `{section}` of `{file}` that this `remove` takes out could not "
    "be read ({why}), so no pin in it is named"
)
# A listing of tracked files git could not make, after `not read: `.
LISTING_UNREAD = (
    "git could not list the tracked files `{pathspec}` matches, so none of them "
    "is read for a {what}"
)
# The operations whose `to` the settle writes into the policy root.
WRITES_A_TO = ("add", "change")


class Unreadable(Exception):
    """A reader of a design could not run, and the sentence says why."""


_check_lines = None


def check_lines_reader():
    """`CHECK_LINES_READER`, loaded by path once, or Unreadable naming it."""
    global _check_lines
    if _check_lines is None:
        try:
            _check_lines = load(CHECK_LINES_READER, "agentic_rules_for_the_chain")
        except (OSError, SyntaxError, ImportError, SystemExit) as exc:
            raise Unreadable(
                f"the check-line reader `.github/scripts/rules.py` would not load "
                f"({exc})"
            ) from None
    return _check_lines


def check_lines_in(root, rel, ops, notices=None):
    """[(path, line, problem)] for each check line inside the `to` of an
    `add` or `change` of OPS, a design's operations at REL, that
    `rules.py#refused_lines` refuses, at its line in the design (`Op.lines`),
    its targets resolved in the tree at ROOT. Each line of such a `to` that
    `rules.py#unread_lines` names goes to NOTICES. A `from` is not read: the
    settle writes none into the policy root. Unreadable where `rules.py`
    will not load or cannot read the tree."""
    found = []
    for op in ops:
        if op.kind not in WRITES_A_TO:
            continue
        numbers = [number for number, _ in op.lines["to"]]
        text = "\n".join(said for _, said in op.lines["to"])
        checks = check_lines_reader()
        try:
            refused = checks.refused_lines(root, text)
            unread = checks.unread_lines(text)
        except checks.Unreadable as exc:
            raise Unreadable(
                f"`.github/scripts/rules.py` could not read the check lines of "
                f"{rel}: {exc}"
            ) from None
        found += [
            (rel, numbers[n - 1], CHECK_LINE_SAYS.format(file=op.file, why=why))
            for n, _heading, why in refused
        ]
        if notices is not None:
            notices.extend(
                (rel, numbers[n - 1], RULE_CHANGES_UNREAD.format(why=why))
                for n, _heading, why in unread
            )
    return found


def _tracked(root, pathspec, unread, what):
    """The paths git tracks under ROOT that PATHSPEC matches; where git cannot
    list them, [] and a notice on UNREAD naming WHAT goes unread."""
    out = git(root, "ls-files", "-z", "--", pathspec)
    if out is None:
        why = LISTING_UNREAD.format(pathspec=pathspec, what=what)
        unread.append(("", 0, RULE_CHANGES_UNREAD.format(why=why)))
        return []
    return [p for p in out.split("\0") if p]


# What stops the pin reading of one test file: it cannot be opened or decoded,
# or `ast.parse` refuses it or gives up on its nesting.
TEST_UNREADABLE = (
    OSError,
    UnicodeDecodeError,
    SyntaxError,
    ValueError,
    RecursionError,
    MemoryError,
)


def _read_tree(rules, root):
    """What the pin and copy reading reads of the working tree at ROOT:
    `literals`, `[(path, line, text)]` of every tracked `*.py` under `tests/`
    (`rule_changes.py#literals`); `documents`, `{path: text}` of every
    tracked rule document (`passages.py#in_corpus`); and `unread`, a notice
    for each listing git could not make and, at line 0, for each such test
    or document that could not be opened, decoded or parsed. A file git
    lists and the tree has deleted is skipped: it is no file of the tree the
    settle writes into."""
    literals, unread, documents = [], [], {}
    for path in _tracked(root, "tests/*.py", unread, "pin"):
        try:
            with open(os.path.join(root, *path.split("/")), encoding="utf-8") as f:
                found = rules.literals(f.read())
        except FileNotFoundError:
            continue
        except TEST_UNREADABLE as exc:
            why = TEST_UNREAD.format(path=path, why=type(exc).__name__)
            unread.append((path, 0, RULE_CHANGES_UNREAD.format(why=why)))
            continue
        literals += [(path, line, text) for line, text in found]
    in_corpus = rules.passages().in_corpus
    for path in _tracked(root, "*.md", unread, "copy"):
        if not in_corpus(path):
            continue
        try:
            with open(os.path.join(root, *path.split("/")), encoding="utf-8") as f:
                documents[path] = f.read()
        except FileNotFoundError:
            continue
        except (OSError, UnicodeDecodeError) as exc:
            why = DOCUMENT_UNREAD.format(path=path, why=type(exc).__name__)
            unread.append((path, 0, RULE_CHANGES_UNREAD.format(why=why)))
    return {"literals": literals, "unread": unread, "documents": documents}


def _section_text(rules, root, op):
    """`(text, None)` for the section OP takes out, as its document in the
    working tree at ROOT holds it (`rule_changes.py#section_lines`), or
    `(None, why)` where the document cannot be opened or decoded, or the
    section is not there once."""
    try:
        with open(os.path.join(root, *op.file.split("/")), encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        text = None
    except (OSError, UnicodeDecodeError) as exc:
        return None, type(exc).__name__
    span, why = rules.section_lines(text, op.section)
    if span is None:
        return None, why
    return "\n".join(rules.reader().gfm_lines(text)[span[0] - 1 : span[1]]), None


def pins_and_copies_in(reader, root, rel, ops, sources):
    """[(path, line, notice)] for OPS, a design's operations at REL, refusing
    nothing: each test literal an operation takes out of the policy root and
    its `to` does not hold (`rule_changes.py#pins`), at the first line of its
    `from`, or at the operation's line for a `remove` with no `from`, which
    takes its section out whole; and each rule document an `add` or `change`
    `to` shares a run of `passages.py#WINDOW` words with
    (`rule_changes.py#copies`), at the `to`'s first line. The tests and the
    rule documents are read from the working tree at ROOT once per run, into
    SOURCES (`_read_tree`), and the first call returns the notices for what
    could not be read there. A copy is counted after the text the design's
    operations take out of each document leaves it (`rule_changes.py#copies`),
    so a passage the design moves is no copy. A section a `remove` with no
    `from` cannot read is named as not read at the operation's line."""
    if not ops:
        return []
    rules = reader.rule_changes()
    out = []
    if not sources:
        sources.update(_read_tree(rules, root))
        out += sources["unread"]
    window = rules.passages().WINDOW
    taking, gone = [], {}
    for op in ops:
        if op.old is not None:
            taken, at = op.old, op.lines["from"][0][0]
        elif op.kind == "remove":
            taken, why = _section_text(rules, root, op)
            at = op.line
            if taken is None:
                said = SECTION_UNREAD.format(file=op.file, section=op.section, why=why)
                out.append((rel, at, RULE_CHANGES_UNREAD.format(why=said)))
        else:
            taken, at = None, op.line
        taking.append((op, taken, at))
        if taken:
            gone.setdefault(op.file, []).append(taken)
    for op, taken, at in taking:
        out += [
            (rel, at, PIN_SAYS.format(file=op.file, test=t, line=n, literal=said))
            for t, n, said in rules.pins(op, taken, sources["literals"])
        ]
        out += [
            (
                rel,
                op.lines["to"][0][0],
                COPY_SAYS.format(path=path, count=count, window=window, run=run),
            )
            for path, count, run in rules.copies(op, sources["documents"], gone)
        ]
    return out


def rule_changes_read(reader, root, item, notices=None, sources=None):
    """[(path, line, problem)] for the work item's `frame/design.md` whose
    `## Rule changes` section `rule_changes.parse`, the one reader `settle`
    groups by, refuses, or, where it parses, for each check line inside an
    `add` or `change` `to` that `rules.py` refuses (`check_lines_in`); []
    where git carries no design. Each line the parser names as one it did
    not read, and each line of a `to` `rules.py` names so, goes to NOTICES
    (`RULE_CHANGES_UNREAD`), and so does each test pin and copy of its
    operations (`pins_and_copies_in`), read into SOURCES. The reader is
    reached through `unverified_check.py#rule_changes`, which raises where
    it will not load."""
    rel = f"{item}/{SPEC_FILE}"
    text = read_record(root, rel)
    if text is None:
        return []
    parsed = reader.rule_changes().parse(text, reader.policy_root(root))
    if notices is not None:
        notices.extend(
            (rel, line, RULE_CHANGES_UNREAD.format(why=why))
            for line, why in parsed.unread
        )
    found = [
        (rel, line, RULE_CHANGES_SAYS.format(reason=reason))
        for line, reason in parsed.errors
    ] + check_lines_in(root, rel, parsed.ops or [], notices)
    if notices is not None:
        notices.extend(
            pins_and_copies_in(
                reader, root, rel, parsed.ops or [], {} if sources is None else sources
            )
        )
    return found


def rule_changes_of(reader, root, items, notices=None, sources=None):
    """[(path, line, problem)] from `rule_changes_read` over every work item
    directory of ITEMS, its notices going to NOTICES and what it reads of the
    tree to SOURCES, or None where a reader would not load or could not
    read, which is said on stderr."""
    found = []
    try:
        for item in items:
            found.extend(rule_changes_read(reader, root, item, notices, sources))
    except (OSError, SyntaxError, ImportError, SystemExit) as exc:
        print(
            f"chain-check: the rule-changes reader would not load ({exc})",
            file=sys.stderr,
        )
        return None
    except Unreadable as exc:
        print(f"chain-check: {exc}", file=sys.stderr)
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
    """[(path, line, problem)] for one finding's verdict: no close block, at
    its heading; a `fixed` whose commit HEAD does not descend from; a
    `fixed` whose commit changed no path the finding's or its close's
    `location:` names or lies under, named with what it did change."""
    kind, commit = f.verdict
    if kind == OPEN:
        return [(path, f.line, f"{f.heading} {DASH} {OPEN_SAYS}")]
    if kind != FIXED:
        return []
    said = f"{f.heading} {DASH} reads `{FIELDS.VERDICT} {FIXED} {commit}`, and "
    if not is_ancestor(root, commit, "HEAD"):
        return [
            (
                path,
                f.line,
                f"{said}HEAD does not descend from `{commit}`: a `{FIXED}` names "
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
            f"{said}`{commit}` touches no path its `{FIELDS.LOCATION}` names "
            f"({named}): it changed {did}. A fix that went elsewhere names that "
            f"path on a `{FIELDS.LOCATION}` line of its close block",
        )
    ]


def records(reader, routing, root, item, rel, base):
    """[(path, line, problem)] for a work item declared through the review
    chain: no record; a record `round_of` cannot read; a finding with no
    close block; a `fixed` naming a commit HEAD does not descend from, or
    one that changed no path the finding's or its close's `location:` names
    or lies under; what `channel` names between the rounds, a `fixed` of the
    last record located in the work item's own records alone, whose commit
    touched them alone, passing as read at HEAD by the sealer; a last record
    behind HEAD. A finding is named by its line and its heading."""
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
    # A record naming no commit it reviewed was refused by `round_read`.
    if last.target is not None:
        behind = follows(root, last.target, base, item)
        if behind is not None:
            problems.append(
                (
                    last.path,
                    0,
                    follows_reason(behind, f"the last round's `{FIELDS.TARGET}`")
                    + (f"; {VERIFYING_ROUND}" if behind[0] == "after" else ""),
                )
            )
    return problems


# The parity arm at the pull request (#988). Under a routing declaration
# answering the review chain, each round record carries the comparison on the
# `original:` line of its round block, which these read.
NO_ORIGINAL = (
    f"no `{FIELDS.ORIGINAL}` line in the round block: `{{config}}` declares a "
    "migration and this pull request changes a path outside the document "
    f"roots, so each round record's round block carries `{FIELDS.ORIGINAL} "
    "{sha}`, the migration config's baseline, written by the proofer once it "
    "compared the round's target with the original through `legacy-parity`"
)
OTHER_ORIGINAL = (
    f"`{FIELDS.ORIGINAL} {{said}}` names a commit other than the migration "
    "config's `Baseline commit`, {sha}: the line names the commit this round "
    "compared against, and a comparison against another original proves "
    "nothing"
)
NO_BASELINE = (
    "{why}: the migration config names the baseline every round record's "
    f"`{FIELDS.ORIGINAL}` line is compared with"
)


def parity_readers():
    """`(config, gate)`: `hooks/lib/config.py` and `hooks/lib/gate.py`, loaded by path.
    `gate.py` imports nothing since #1027, so the order no longer matters.
    Raises what `load` raises."""
    config = load(os.path.join(HOOKS, "config.py"), "agentic_config_for_parity")
    gate = load(os.path.join(HOOKS, "gate.py"), "agentic_gate_for_parity")
    return config, gate


NO_GUARANTEE_ORIGINAL = (
    f"no `{FIELDS.ORIGINAL}` line in the newest verdict block: `{{config}}` "
    "declares a migration, this work "
    "item answers `straight to the PR`, and this pull request changes a path "
    "outside the document roots, so no round record compares it and the "
    f"sealer's guarantee carries `{FIELDS.ORIGINAL} {{sha}}`, the migration "
    "config's baseline, written once it compared the audited commit with the "
    "original through `legacy-parity`"
)


def original_of(reader, text, rel, sha, config, missing=NO_ORIGINAL):
    """[(rel, line, problem)] for the `original:` line of a round record's
    round block, held against SHA, the `Baseline commit` of the migration
    config at CONFIG: a round block with no such line, said as MISSING at
    its opener, and one naming a commit that is not a prefix of SHA and of
    which SHA is not a prefix, at its line. A guarantee's line is
    `guarantee_original`'s. A record holding a line `hooks/lib/fields.py`
    refuses, an `original:` line in a finding block, a second one or one
    spelt otherwise among them, or holding no round block, is the records
    arm's refusal, and none is added here."""
    block = round_read(reader, text, rel).round
    if block is None or FIELDS.read(text or "", FIELDS.ROUND_RECORD).refusals:
        return []
    said = block.fields.get(FIELDS.ORIGINAL)
    if said is None:
        return [(rel, block.line, missing.format(config=config, sha=sha))]
    commit = said.match["commit"]
    if commit.startswith(sha) or sha.startswith(commit):
        return []
    return [(rel, said.line, OTHER_ORIGINAL.format(said=commit, sha=sha))]


def guarantee_original(text, rel, sha, config):
    """[(rel, line, problem)] for the `original:` line of the newest verdict
    block of the guarantee TEXT at REL, held against SHA, the `Baseline
    commit` of the migration config at CONFIG: a newest block with no such
    line, at its opener, and one naming a commit that is not a prefix of SHA
    and of which SHA is not a prefix, at its line. An earlier block's line
    stands for no later run (#1198). A guarantee `hooks/lib/fields.py`
    refuses, or one holding no verdict block, is the guarantee arm's
    refusal, and none is added here."""
    found = FIELDS.read(text, FIELDS.GUARANTEE)
    if found.refusals or not found.blocks:
        return []
    newest = found.blocks[-1]
    said = newest.fields.get(FIELDS.ORIGINAL)
    if said is None:
        return [
            (rel, newest.line, NO_GUARANTEE_ORIGINAL.format(config=config, sha=sha))
        ]
    commit = said.match["commit"]
    if commit.startswith(sha) or sha.startswith(commit):
        return []
    return [(rel, said.line, OTHER_ORIGINAL.format(said=commit, sha=sha))]


def originals_of(reader, routing, root, paths, items, direct=()):
    """[(path, line, problem)] for the round records of ITEMS, each declared
    through the review chain, and the `guarantee.md` of DIRECT, each
    declared `straight to the PR`, where git carries the migration config at
    HEAD and PATHS, this pull request's, reach outside the document roots;
    `hooks/lib/gate.py#touches_code` decides that, and paths git could not list
    reach outside them. A guarantee git does not carry is `guarantee`'s
    refusal, and none is added here; a guarantee's line is its newest
    verdict block's (`guarantee_original`). A config whose `Baseline commit`
    names no SHA is one refusal naming it. None where `hooks/` would not
    load, said on stderr."""
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
            found.extend(guarantee_original(said, rel, sha, config))
    return found


# A gate record with no run block: one written before the run stood in a
# block, or one nobody wrote a run into (#1198, *Scope* item 9).
NO_RUN_BLOCK = (
    "no run block: since #1198 the run stands in a `seal` block holding "
    "`run: <tree> against <base commit>`, which `seal gate --base <base> "
    "--record <item>` appends below the text already there on a green run"
)


def blocks_of(rel, text, kinds, notices=None):
    """`(blocks, problems)` of the record REL holding KINDS, read through
    `hooks/lib/fields.py`: every block, and each line it refuses as
    `(rel, line, why)`. Each fence it names as not read goes to NOTICES."""
    found = FIELDS.read(text, kinds)
    if notices is not None:
        notices.extend((rel, line, why) for line, why in found.notices)
    return found.blocks, [(rel, line, why) for line, why in found.refusals]


def broad_gate(reader, root, item, base, notices=None):
    """[(path, line, problem)] for the work item's `trail/gate.md`: absent,
    a line `hooks/lib/fields.py` refuses, no run block, or a newest run, the
    last block, behind HEAD. A fence named as not read goes to NOTICES."""
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
    runs, problems = blocks_of(rel, text, FIELDS.GATE, notices)
    if problems:
        return problems
    if not runs:
        return [(rel, 0, NO_RUN_BLOCK)]
    sha = runs[-1].fields[FIELDS.RUN].match["commit"]
    behind = follows(root, sha, base, item)
    if behind is None:
        return []
    return [(rel, 0, follows_reason(behind, "the newest gate run"))]


# A guarantee with no verdict block: one written before the verdict stood in
# a block, or one the sealer never filled (#1198, *Scope* item 9).
NO_VERDICT_BLOCK = (
    "no verdict block: since #1198 the sealer's verdict stands in a `seal` "
    "block holding `target: <sha> against <base>`, the `original:` line where "
    "one is owed and `Verdict:`, as `templates/records/sdd-guarantee.md` "
    "shows; the sealer runs again at HEAD and appends one below the text "
    "already there"
)


def guarantee(reader, root, item, base, notices=None):
    """[(path, line, problem)] for the work item's `guarantee.md`: absent, a
    line `hooks/lib/fields.py` refuses, a fence nobody closed and a line that
    begins with `<!--` among them, no verdict block, or a newest block, the
    last, naming a commit with anything but the closing records after it or
    a verdict other than `sealed`. A fence named as not read goes to
    NOTICES."""
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
    verdicts, problems = blocks_of(rel, text, FIELDS.GUARANTEE, notices)
    if problems:
        return problems
    if not verdicts:
        return [(rel, 0, NO_VERDICT_BLOCK)]
    newest = verdicts[-1]
    sha = newest.fields[FIELDS.TARGET].match["commit"]
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
    said = newest.fields[FIELDS.SEALER_VERDICT]
    if FIELDS.verdict_word(newest) != FIELDS.SEALED:
        line = f"{FIELDS.SEALER_VERDICT} {said.value}"
        problems.append(
            (
                rel,
                said.line,
                f"the sealer's verdict reads `{line}`: a ready pull request needs "
                f"`{FIELDS.SEALED}`: fix what it names, or answer its question "
                "below the newest block, and the sealer runs again at the new "
                "HEAD and appends its block",
            )
        )
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
    # What the rule-changes arm reads of the tree for pins and copies, read
    # once on the first design with operations.
    sources = {}
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
        found = rule_changes_of(reader, root, [item], notices, sources)
        if found is None:
            return 2
        problems.extend(found)
        if declared["review"] == routing.CHAIN:
            problems.extend(records(reader, routing, root, item, rel, args.baseline))
            chained.append(item)
        else:
            direct.append(item)
        notices.extend(unread(reader, routing, root, item, item in chained))
        gate = broad_gate(reader, root, item, args.baseline, notices)
        gate += guarantee(reader, root, item, args.baseline, notices)
        if args.sealing:
            notices.extend((p, n, f"{SEALING_SAYS}: {m}") for p, n, m in gate)
        else:
            problems.extend(gate)
    found = rule_changes_of(reader, root, edited, notices, sources)
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
