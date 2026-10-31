#!/usr/bin/env python3
"""settle — show the released designs by section, and remove what a settle leaves.

  settle                        the dry run: each group of released designs that
                                name one section, the designs to read whole, every
                                open row, the files named like a record and not
                                read, the judgments of each run, and what
                                `--apply` removes
  settle --apply                remove each released work item directory whose
                                record holds no open row
  settle --released-at REF      what counts as released (default origin/main)
  settle --root DIR             a repository other than this one

**Released means shipped on the branch the release merges to**, which is why
`--released-at` names a ref rather than a date. Where the root is shared, a
work item is released when its directory is present at that ref. In local
mode the root is under the common git directory and no ref holds a work
item's directory, so a work item is released when the pull request from the
branch its `routing.md` names has merged and that pull request's merge commit
is reachable from the ref. `gh pr list --head <branch> --state merged` names
the merge commit whatever the merge method was; it is asked once per branch,
and only in local mode.

**The designs say what was decided and in what order, the code says what holds
now, and the settling session writes each section as the latest decision the
code bears out. The script reads and removes; it neither writes `docs/` nor
judges.** `skills/settle/SKILL.md` is the settling session's procedure.

**The dry run is the timeline.** Each released design's `## Rule changes` is
read through `rule_changes.py`, as `--released-at` holds it where the root is
shared and from its directory in local mode. The designs whose
operations name one place, a file and a section, are one group, two places
one group where `rule_changes.py#overlapping` says they can name one text, and
each group is listed in merge order: the commits that add each design
(`rule_changes.py#order`), or in local mode the pull requests' merge commits
(`rule_changes.py#merge_order`). Each operation
carries its design's coordinate and two facts read from the working tree:
whether its `from` is found in the section, and whether its `to` is. Two designs
in one group whose commits no ancestry orders are marked unordered for
the settling session to order by content. A design whose section does not parse,
that has none, or in which the reader names a line it did not read, is
listed to read whole. Every open `## Not verified` row of
every released record is listed with the backticked paths it names and
whether each is in the working tree. A file in a released work item's
directory named like a record this reads there, `gaps.md`, `frame/design.md`
or `frame/plan.md`, at any path but that record's own, is named as not read,
with the record it is named like: only the name is read, so what it holds is
the settling session's to judge. Every row of every released
`frame/plan.md` *Judgments of the run* is listed, grouped by its `Judged
against` cell, with its work item's round count; a heading near the
section's, and a section whose table it cannot read, are named as not read. Nothing is refused or held in the dry
run.

**`--apply` removes, and only that.** It removes every released work item
directory whose record holds no open row in the working tree, whether or not
it wrote a `frame/design.md`, and prints the rows each removed record closed, with
what closed each. A directory whose record still holds an open row, or one
that cannot be read, is kept and named with its rows. A file the dry run
names as not read is named again under its directory's line, and decides
nothing: it goes or stays with the directory. It writes no policy
document: the settling session has written them by then, and `seal fold`'s
lines over the policy root are printed after the removals.

**In local mode the work items are read and removed under the git
directory.** Every `seal/threads/<id>/` path is read under the directory that
holds the resolved root, the repository's top where the root is shared and
the common git directory in local mode, and is printed as `seal/threads/<id>/`.
The policy root, the tracked files the citations are read from, and `tests/`
are read from the repository's top in both. The dry run's first line names a
local root, each released local work item is listed with its pull request's
number and its merge commit, and each unreleased one with why: no
`routing.md` that `hooks/lib/routing.py` reads as a declaration naming a branch,
no merged pull request from its branch, or no listed merge commit
`--released-at` reaches, a pull request listed with none among them. What `--apply` removes there no commit holds, and
the dry run names `seal export` for a copy. A `gh` that cannot be asked
refuses the run, since every local work item would then read as unreleased.
A repository that opted out with the scratch marker, an empty FILE read the
way `hooks/lib/optin.py#home_at` reads it, is refused.

Exit codes: 0 the report was produced, `--apply` kept nothing, or the root
holds no work item, which is the state a complete settle reaches; 1 `--apply`
kept a directory whose record holds an open row or cannot be read; 2 the
arguments or the tree were unusable: a `--released-at` ref that does not
resolve, a root at neither place, a repository that opted out, in local mode
a `gh` that is not on PATH or whose query fails, and a sibling script that is
not beside it. An interpreter below
the floor never reaches this file through `seal settle`: `hooks/lib/launch.py`
refuses `seal` with 2 first.
"""

import argparse
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
READER = os.path.join(HERE, "..", "..", "verify", "scripts", "unverified_check.py")
OPTIN = os.path.join(HERE, "..", "..", "..", "hooks", "lib", "optin.py")
ROUTING = os.path.join(HERE, "..", "..", "..", "hooks", "lib", "routing.py")
RULES = os.path.join(HERE, "rule_changes.py")
FOLD_CHECK = os.path.join(HERE, "fold_check.py")
CONFIG = os.path.join(HERE, "..", "..", "..", "hooks", "lib", "config.py")

# What each sibling is for, in the sentence `load` prints when it is missing.
PURPOSES = {
    READER: "it is where a record's open rows are read from",
    OPTIN: "it is what finds the repository's seal/ root",
    ROUTING: (
        "it is what reads the branch a local work item's `routing.md` names "
        "and counts a work item's round records"
    ),
    RULES: "it is what reads a design's `## Rule changes`",
    FOLD_CHECK: "it is what reads the index and the one read after an apply",
    CONFIG: "it is what reads a plan's *Judgments of the run* table",
}

SPECS = "seal/threads"
# A thread's design, relative to its directory: `hooks/lib/optin.py#DESIGN`.
DESIGN = "frame/design.md"
# A thread's plan, and the section and table the orchestrator writes its
# judgments of the run to (`templates/records/sdd-plan.md`).
PLAN = "frame/plan.md"
JUDGMENTS = "Judgments of the run"
JUDGMENTS_HEADER = ("Date", "Judgment", "Grounds", "Judged against")
# What the dry run says of a heading near the judgments section, at its line.
NEAR_JUDGMENTS = (
    "line {line}: `{written}` opens like `## {heading}` and is not it, so "
    "none of its rows were read"
)
TESTS = "tests/"

# The command asked in local mode, once per branch, and how long it may take.
GH = "gh"
GH_TIMEOUT = 60


def under(root, rel):
    """The disk path of a `/`-joined repository-relative path."""
    return os.path.join(root, *rel.split("/"))


def plural(count, many="s", one=""):
    """`s` unless there is one of them. Every count this prints is read by a
    person, and `1 work items` is the tell that nobody read the output."""
    return one if count == 1 else many


def load(path, name):
    """Import a sibling script by path, or refuse with a sentence saying what
    the missing file is for — its `PURPOSES` entry — and exit 2.

    Not a bare `exec_module`: `spec_from_file_location` hands back a spec for
    any path ending in `.py`, present or not, so a missing reader would raise
    `FileNotFoundError` — a traceback where every failure here is a sentence.
    Exit 2 and not 1, because nothing about the tree has been read (#590)."""
    purpose = PURPOSES.get(path, "this command cannot run without it")
    if not os.path.isfile(path):
        sys.stderr.write(
            f"settle: cannot read {path}, and {purpose}. This command ships "
            "beside it under `skills/`; a copy of one script taken on its own "
            "is not a plugin. Nothing was read.\n"
        )
        raise SystemExit(2)
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        sys.stderr.write(f"settle: cannot load {path}, and {purpose}.\n")
        raise SystemExit(2)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# --- what the tree says ----------------------------------------------------


def work_items(records):
    """Every work item id with a directory under `seal/threads/` in RECORDS,
    the directory holding the `seal/` root, in id order."""
    top = under(records, SPECS)
    if not os.path.isdir(top):
        return []
    return sorted(
        name for name in os.listdir(top) if os.path.isdir(os.path.join(top, name))
    )


def released(root, ref):
    """Work item ids whose directory is present at `ref`, or None if it is not.

    None for a ref that does not resolve, and the caller refuses: a ref this
    cannot read would make every work item read as unreleased and the report
    say there is nothing to do, the quiet zero every checker here is written
    against."""
    r = subprocess.run(
        ["git", "-C", root, "ls-tree", "-r", "--name-only", ref],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    if r.returncode != 0:
        return None
    prefix = SPECS + "/"
    found = set()
    # exempt from splitlines: git output
    for line in r.stdout.splitlines():
        if line.startswith(prefix):
            rest = line[len(prefix) :]
            if "/" in rest:
                found.add(rest.split("/", 1)[0])
    return found


def resolves(root, ref):
    """Whether REF names a commit in the repository at ROOT."""
    r = subprocess.run(
        ["git", "-C", root, "rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}"],
        capture_output=True,
    )
    return r.returncode == 0


def reaches(root, ref, commit):
    """Whether COMMIT is reachable from REF, REF itself included."""
    r = subprocess.run(
        ["git", "-C", root, "merge-base", "--is-ancestor", commit, ref],
        capture_output=True,
    )
    return r.returncode == 0


class Unasked(Exception):
    """`gh` could not be asked; the message says what it said."""


def merged_pull_requests(root, branch):
    """`[(number, merge commit or None)]` for the pull requests from BRANCH
    that have merged, as `gh` lists them, asked from the repository's top.
    Raises `Unasked` where `gh` is not on PATH, does not run, exits non-zero
    or answers anything but a list of objects."""
    found = shutil.which(GH)
    if found is None:
        raise Unasked(f"`{GH}` is not on PATH")
    asked = f"`{GH} pr list --head {branch}`"
    query = ["--head", branch, "--state", "merged", "--json", "number,mergeCommit"]
    try:
        r = subprocess.run(
            [found, "pr", "list", *query],
            cwd=root,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=GH_TIMEOUT,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise Unasked(f"{asked} did not run ({exc})") from exc
    if r.returncode != 0:
        said = (r.stderr or r.stdout or "").strip().partition("\n")[0].strip()
        raise Unasked(f"{asked} exited {r.returncode}" + (f": {said}" if said else ""))
    try:
        answer = json.loads(r.stdout)
    except ValueError:
        answer = None
    if not isinstance(answer, list) or not all(isinstance(pr, dict) for pr in answer):
        raise Unasked(f"{asked} did not answer a list of pull requests")
    out = []
    for pr in answer:
        merge = pr.get("mergeCommit")
        commit = merge.get("oid") if isinstance(merge, dict) else None
        out.append(
            (pr.get("number"), commit if isinstance(commit, str) and commit else None)
        )
    return out


# Why a local work item is unreleased, each pinned by `tests/skills/test_settle.py`.
# A `routing.md` that `hooks/lib/routing.py#parse` does not read, such as one whose
# `Review` answer is outside the vocabulary, names no branch whatever rows it
# holds, so the reason names the reader rather than the row.
NO_BRANCH = (
    "no `routing.md` that `hooks/lib/routing.py` reads as a declaration names a "
    "branch, so `gh` was not asked"
)
NO_PULL_REQUEST = "no pull request from `{branch}` has merged"
NOT_REACHED = (
    "{ref} reaches no merge commit of the pull requests from `{branch}` that "
    "merged: {listed}"
)


def declared_branch(records, work_item_id, routing):
    """The `Branch` row of the work item's `routing.md`, read by
    `hooks/lib/routing.py#parse`, or None where there is no file, no row, or a
    file `parse` does not read as a declaration."""
    path = under(records, f"{SPECS}/{work_item_id}/{routing.FILENAME}")
    try:
        with open(path, encoding="utf-8") as f:
            declared = routing.parse(f.read())
    except (OSError, UnicodeDecodeError):
        return None
    return (declared or {}).get("branch") or None


def released_local(root, records, ref, ids):
    """`(merged, why)` for the local work items IDS: `merged` is `{id:
    (number, merge commit)}` for each one released, `why` is `{id: reason}`
    for each one that is not.

    A work item is released when a pull request from the branch its
    `routing.md` names has merged and REF reaches its merge commit; `gh` is
    asked once per branch, and not for a work item that names none. Raises
    `Unasked` where `gh` cannot be asked: every work item would then read as
    unreleased, and the run would say there is nothing to settle."""
    routing = load(ROUTING, "agentic_routing_for_settle")
    asked, merged, why = {}, {}, {}
    for work_item_id in ids:
        branch = declared_branch(records, work_item_id, routing)
        if branch is None:
            why[work_item_id] = NO_BRANCH
            continue
        if branch not in asked:
            asked[branch] = merged_pull_requests(root, branch)
        prs = asked[branch]
        if not prs:
            why[work_item_id] = NO_PULL_REQUEST.format(branch=branch)
            continue
        reached = next(
            ((n, c) for n, c in prs if c is not None and reaches(root, ref, c)), None
        )
        if reached is None:
            listed = ", ".join(
                f"#{n} at {c}" if c else f"#{n} with no merge commit" for n, c in prs
            )
            why[work_item_id] = NOT_REACHED.format(
                ref=ref, branch=branch, listed=listed
            )
        else:
            merged[work_item_id] = reached
    return merged, why


def has_spec(records, work_item_id):
    """Whether the work item's directory holds a `frame/design.md` on disk."""
    return os.path.isfile(under(records, f"{SPECS}/{work_item_id}/{DESIGN}"))


def read_text(root, rel):
    """A file's text as it stands, line ends kept, or None where it is absent."""
    try:
        with open(under(root, rel), encoding="utf-8", newline="") as f:
            return f.read()
    except OSError:
        return None


# What a settled root prints, for the dry run and `--apply` alike.
SETTLED = (
    "settle: {specs}/ in {root} holds no work item — nothing to show and "
    "nothing to remove. A complete settle ends here, and git keeps no empty "
    "directory, so a fresh checkout of this state has no {specs}/ at all.\n"
)
# A checkout carries no local root, so the fresh checkout goes unsaid there.
SETTLED_LOCAL = (
    "settle: {home} is the seal/ root, in local mode, and its threads/ holds no "
    "work item — nothing to show and nothing to remove. A complete settle "
    "ends here.\n"
)
# The refusal where `gh` cannot be asked, in local mode alone.
UNASKED = (
    "settle: `gh` cannot be asked which pull requests merged: {why}. Nothing "
    "was read and nothing was removed. In local mode a work item is released "
    "when the pull request from the branch its `routing.md` names has merged, "
    "and `gh` is what names that pull request's merge commit, so a repository "
    "on a host `gh` cannot ask cannot settle in local mode.\n"
)

# The dry run's local lines, each pinned by `tests/skills/test_settle.py`.
LOCAL_LINE = "local mode: the seal/ root is {home}, under the git directory\n"
MERGED_HEADING = (
    "released in local mode, each with the pull request that merged it and "
    "its\nmerge commit, for the settle's pull request body to cite:"
)
UNMERGED_HEADING = "unreleased in local mode and untouched, each with why:"

# The dry run's headings, each pinned by `tests/skills/test_settle.py`.
GROUPS_HEADING = (
    "groups: the released designs whose rule changes name one section, in merge "
    "order.\nThe settling session writes each section as its group's latest "
    "decision, checked\nagainst the code (`skills/settle/SKILL.md`); `from` and "
    "`to` say whether that text\nis in the section now:"
)
UNORDERED = (
    "unordered: {a} and {b}: no ancestry orders the commits that add their "
    "frame/design.md,\n        so order them by content"
)
UNORDERED_LOCAL = (
    "unordered: {a} and {b}: no ancestry orders their pull requests' merge "
    "commits,\n        so order them by content"
)
WHOLE_HEADING = (
    "to read whole: released designs no group holds, for the settling session "
    "to read\nand write any rule they state the same way:"
)
NO_SECTION = "no `## Rule changes` section"
NOTHING_HEADING = "the no-change block (`- {nothing}`), so no section to write:"
ROWS_HEADING = (
    "open rows: every open `## Not verified` row of every released record, for "
    "the\nsettling session to decide as moot, answered or a measurement to "
    "re-home, and\nclose with `closed` and what closed it:"
)
MISPLACED_HEADING = (
    "not read: each file named like a record the settle reads, away from that "
    "record's place.\nThe settling session opens each one and decides each item "
    "in it that reads as an\nopen row; `--apply` decides nothing on it and "
    "removes it with its directory:"
)
# A misplaced record file, under the dry run's heading and after `not read: `
# under `--apply`'s `removed` or `kept` line.
MISPLACED = "{path}, named like `{place}` and away from its place"
JUDGMENTS_HEADING = (
    "the judgments: the orchestrators' rows of each released plan's *Judgments "
    "of the run*,\ngrouped by the document each stands on, with each work "
    "item's round count. The\nsettling session reads them before `--apply` "
    "removes them, and rewrites a section\nwhere one kind of judgment recurs or "
    "kept costing rounds (`skills/settle/SKILL.md`):"
)
REMOVES_HEADING = (
    "what `seal settle --apply` removes: each released directory whose record "
    "holds no open row:"
)
REMOVES_HEADING_LOCAL = (
    "what `seal settle --apply` removes: each released directory whose record "
    "holds no open row.\nIn local mode no commit holds these directories; "
    "`seal export` takes a copy for\nwhoever wants one:"
)
READERS_HEADING = (
    "checks that read `seal/threads` — each owes an answer "
    "(`skills/settle/SKILL.md`\n*Answer every check that reads the corpus*) "
    "before the directories go:"
)


# A backticked span that names a repository path: a `/` in it, or a file
# name with one of the extensions this repository's files carry. What
# follows `#` or `::`, and a `:<line>` range, point inside the file and are
# not part of its path.
SPAN_RE = re.compile(r"`([^`\s]+)`")
FILE_NAME_RE = re.compile(r"[\w.-]+\.(?:py|md|cmd|sh|ps1|yml|yaml|json|toml|txt)")


def named_paths(item):
    """The repository paths an open row's ITEM names in backticks, in order."""
    out = []
    for span in SPAN_RE.findall(item):
        path = re.split(r"#|::", span, maxsplit=1)[0]
        path = re.sub(r":\d+(-\d+)?$", "", path).removeprefix("./")
        if not path or path.startswith(("/", "~", "-")) or "<" in path:
            continue
        if ("/" in path or FILE_NAME_RE.fullmatch(path)) and path not in out:
            out.append(path)
    return out


def tracked_names(root):
    """The base names of every tracked file, so a row naming `design.md` or
    `broad_gate.py` alone is looked for by name."""
    r = subprocess.run(["git", "-C", root, "ls-files", "-z"], capture_output=True)
    listed = (
        r.stdout.decode("utf-8", "replace").split("\0") if r.returncode == 0 else []
    )
    return {rel.rsplit("/", 1)[-1] for rel in listed if rel}


def in_tree(root, records, work_item_id, path, names):
    """Whether PATH, as an open row of WORK_ITEM_ID names it, is in the
    working tree: under the repository's top ROOT, under the work item's own
    directory in RECORDS, or, for a bare file name, as the name of a tracked
    file."""
    rel = path.rstrip("/")
    if os.path.exists(under(root, rel)):
        return True
    if os.path.exists(under(records, f"{SPECS}/{work_item_id}/{rel}")):
        return True
    return "/" not in rel and rel in names


def open_rows(root, records, ids, reader):
    """`[(id, [(file, item, [(path, in the tree)])])]` for each of IDS whose
    record under RECORDS holds an open row in the working tree
    (`unverified_check.py#open_record_rows`)."""
    out, names = [], None
    for work_item_id in ids:
        rows = reader.open_record_rows(records, None, f"{SPECS}/{work_item_id}")
        if not rows:
            continue
        names = tracked_names(root) if names is None else names
        out.append(
            (
                work_item_id,
                [
                    (
                        name,
                        item,
                        [
                            (p, in_tree(root, records, work_item_id, p, names))
                            for p in named_paths(item)
                        ],
                    )
                    for name, item in rows
                ],
            )
        )
    return out


def misplaced(records, work_item_id, reader):
    """`[(path, place)]` for each misplaced record file in the work item's
    directory under RECORDS, sorted: a regular file, or a link to one, whose
    name is the last part of a record this reads in the directory, the
    closing memo (`unverified_check.py#OVERVIEW`), `DESIGN` or `PLAN`, and
    whose path from the directory is not that record's. PATH is that path,
    and PLACE is the record's.

    Only the exact name is read, and no file's content: whether such a file
    holds what its record would is the settling session's to judge. A linked
    directory is not followed."""
    places = {p.rsplit("/", 1)[-1]: p for p in (reader.OVERVIEW, DESIGN, PLAN)}
    top = under(records, f"{SPECS}/{work_item_id}")
    out = []
    for here, _dirs, names in os.walk(top):
        for name in names:
            place = places.get(name)
            path = os.path.join(here, name)
            if place is None or not os.path.isfile(path):
                continue
            rel = os.path.relpath(path, top).replace(os.sep, "/")
            if rel != place:
                out.append((rel, place))
    return sorted(out)


def judgments(records, ids):
    """`(groups, unread)` for the plans of IDS under RECORDS, as they stand
    in the working tree, where the open rows are read too.

      groups  `[(judged against, [(id, rounds, [(line, date, judgment,
              grounds)])])]`: every row of each plan's *Judgments of the run*,
              grouped by its `Judged against` cell exactly as written, each
              group and each work item in the order IDS lists them first.
              `rounds` is how many `round-N.md` the work item's
              `trail/rounds/` holds (`hooks/lib/routing.py#rounds`), or None
              where that is not a directory this can list
              (`hooks/lib/routing.py#rounds_unreadable`): a file, a link or
              a directory nothing can list, which holds a review git carries
      unread  `[(id, why)]` for each heading of a plan whose letters, case
              folded, are the section's and that is not it, at its line; and
              for a plan whose section holds no table under the exact
              header, or whose table stops at a row it cannot read

    A plan with no such section and no near heading holds no judgment and
    is in neither. A heading inside a fence or an HTML comment is no
    heading (`unverified_check.py#live_lines`). A row
    whose every cell is empty is the template's blank row, and no
    judgment. The table is read through `hooks/lib/config.py#gfm_table`
    over the section's lines alone, and nothing here grades a cell."""
    rules = load(RULES, "agentic_rule_changes")
    routing = load(ROUTING, "agentic_routing_for_settle")
    config = load(CONFIG, "agentic_config_for_settle")
    groups, unread = {}, []
    for work_item_id in ids:
        text = read_text(records, f"{SPECS}/{work_item_id}/{PLAN}")
        if text is None:
            continue
        lines = rules.reader().gfm_lines(text)
        marks = rules.headings(lines)
        unread += [
            (
                work_item_id,
                NEAR_JUDGMENTS.format(
                    line=n + 1, written=lines[n].strip(), heading=JUDGMENTS
                ),
            )
            for n, _lv, t in marks
            if t != JUDGMENTS and rules.letters(t) == rules.letters(JUDGMENTS)
        ]
        if not any(t == JUDGMENTS for _n, _lv, t in marks):
            continue
        span, why = rules.section_lines(text, JUDGMENTS)
        if span is None:
            unread.append((work_item_id, why))
            continue
        first, last = span
        rows, refusals = config.gfm_table(
            "\n".join(lines[first - 1 : last]), JUDGMENTS_HEADER
        )
        if refusals:
            unread.append((work_item_id, refusals[0]))
        where = under(records, f"{SPECS}/{work_item_id}")
        # `routing.rounds` returns [] both for no record and for a
        # `trail/rounds` it cannot list; `rounds_unreadable` says which.
        rounds = (
            None if routing.rounds_unreadable(where) else len(routing.rounds(where))
        )
        for line, (date, judgment, grounds, against) in rows:
            if not any((date, judgment, grounds, against)):
                continue
            members = groups.setdefault(against, {})
            members.setdefault(work_item_id, (rounds, []))[1].append(
                (first - 1 + line, date, judgment, grounds)
            )
    return (
        [
            (against, [(i, r, held) for i, (r, held) in members.items()])
            for against, members in groups.items()
        ],
        unread,
    )


def facts(root, op, rules):
    """`[(field, found)]` for one operation, read from the working tree:
    whether its `from` and its `to` are in the lines its place spans. Where
    the place is not there, neither is."""
    text = read_text(root, op.file)
    span, _ = rules.section_lines(text, op.section)
    region = ""
    if span:
        lines = rules.reader().gfm_lines(text)
        region = "\n".join(lines[span[0] - 1 : span[1]])
    return [
        (field, bool(span) and bool(rules.pattern(value).search(region)))
        for field, value in (("from", op.old), ("to", op.new))
        if value
    ]


def timeline(root, ref, ids, reader, records, merged=None):
    """The released designs IDS as the dry run shows them.

    Where the root is shared, each `frame/design.md` is read as REF holds it, the
    text that was reviewed and released, and the merge order is the commits
    that add the designs (`rule_changes.py#order`). In local mode no ref holds
    a design, so it is read from its directory under RECORDS, and the merge
    order is the merge commits MERGED names, `{id: (number, merge commit)}`
    (`rule_changes.py#merge_order`). A design with operations joins the groups
    `rule_changes.py#group` forms in merge order; one whose section does not
    parse, that has none, or that holds a line the reader names as not read
    (`Parsed.unread`), is to be read whole; one holding the no-change
    block has nothing to write; a directory with no `frame/design.md` states no
    rule."""
    rules = load(RULES, "agentic_rule_changes")
    policy = reader.policy_root(root)
    parsed, whole, nothing, spec_less = {}, [], [], []
    for work_item_id in ids:
        if not has_spec(records, work_item_id):
            spec_less.append(work_item_id)
            continue
        rel = f"{SPECS}/{work_item_id}/{DESIGN}"
        if merged is None:
            text = reader.show(root, ref, rel) or ""
        else:
            text = read_text(records, rel) or ""
        found = rules.parse(text, policy)
        if found.errors:
            whole.append((work_item_id, *found.errors[0]))
        elif found.unread:
            # A line the reader did not read can hold a rule change no group
            # would hold, so the design is read whole, at that line.
            whole.append((work_item_id, *found.unread[0]))
        elif found.ops is None:
            whole.append((work_item_id, 0, NO_SECTION))
        elif not found.ops:
            nothing.append(work_item_id)
        else:
            parsed[work_item_id] = found.ops
    if merged is None:
        ordered = rules.order(root, ref, list(parsed), SPECS)
    else:
        pairs = [(i, merged[i][1]) for i in parsed]
        ordered = rules.merge_order(root, ref, pairs)
    commits = dict(ordered)
    same = rules.overlapping(lambda rel: read_text(root, rel))
    groups = []
    for places, ops in rules.group([(i, parsed[i]) for i, _ in ordered], same):
        members = list(dict.fromkeys(i for i, _ in ops))
        groups.append(
            {
                "places": [
                    (p, *rules.section_lines(read_text(root, p[0]), p[1]))
                    for p in places
                ],
                "ops": [(i, o, facts(root, o, rules)) for i, o in ops],
                "unordered": rules.unordered(root, [(i, commits[i]) for i in members]),
            }
        )
    return {
        "groups": groups,
        "whole": whole,
        "nothing": nothing,
        "spec_less": spec_less,
        "with_rules": len(parsed),
    }


def place_line(p, span, why):
    """A group's place as a person reads it, with its lines or why none."""
    file, section = p
    named = f"{file} section `{section}`" if section else f"{file}, the whole document"
    if span:
        return f"place: {named}, at {file}:{span[0]}-{span[1]}"
    return f"place: {named}: {why} in the working tree"


def op_line(work_item_id, op, found):
    """One operation of a group: its kind, its design's coordinate and what the
    working tree holds of its texts."""
    where = f"{SPECS}/{work_item_id}/{DESIGN}:{op.line}"
    said = (
        ", ".join(f"{f} {'found' if ok else 'not found'}" for f, ok in found)
        or "the whole section"
    )
    return f"{op.kind}  {work_item_id}  {where}  {said}"


# --- the dry run -----------------------------------------------------------


def records_of(root, home):
    """`(local, records)` for the repository at ROOT whose resolved `seal/`
    root is HOME: whether it is in local mode, and the directory every
    `seal/threads/<id>/` path is read and removed under. That is ROOT where the
    root is shared, and the common git directory that holds it in local mode;
    every other read stays on ROOT."""
    local = os.path.realpath(home) != os.path.realpath(under(root, "seal"))
    return local, (os.path.dirname(home) if local else root)


def survey(root, ref, home=None):
    """What the dry run prints, and where `--apply` gets *released*.

    HOME is the resolved `seal/` root, `<root>/seal` when it is None. Where
    it is anywhere else the root is in local mode: the work items are read
    under the directory holding it, and released is asked of `gh` and git
    (`released_local`) rather than read from REF's tree.

    **`--apply` does not take its candidates from here.** It reads the
    directories and the records from the tree again, because a
    classification made for a printed list is not a guard on a destructive
    act. What it takes from here is `released`, which only git answers, and
    in local mode `gh` with git, and `records`, the directory the root is in.

    None where `ref` does not resolve. Raises `Unasked` where local mode
    needs `gh` and it cannot be asked."""
    home = home or under(root, "seal")
    local, records = records_of(root, home)
    present = work_items(records)
    merged, why = None, {}
    if local:
        if not resolves(root, ref):
            return None
        merged, why = released_local(root, records, ref, present)
        on_base = set(merged)
    else:
        on_base = released(root, ref)
        if on_base is None:
            return None
    reader = load(READER, "agentic_unverified_reader")
    ids = [i for i in present if i in on_base]
    found = {
        "ref": ref,
        "local": home if local else None,
        "records": records,
        "released": ids,
        "unreleased": [i for i in present if i not in on_base],
        "merged": merged or {},
        "why": why,
        "timeline": timeline(root, ref, ids, reader, records, merged),
        "rows": open_rows(root, records, ids, reader),
        "misplaced": [
            (i, held) for i in ids if (held := misplaced(records, i, reader))
        ],
        "judgments": judgments(records, ids),
        "nothing": reader.NOTHING,
    }
    found["citations"], found["readers"] = citations(root, ids)
    return found


# A path into a work item directory, however it is spelled before `threads/`.
# The name may be cut short with an ellipsis, which is how this repository's
# prose abbreviates a long id; a marker and a bare id carry no `/` after the
# name, so neither is read as a citation.
CITATION_RE = re.compile(r"threads/(\d{6,}[^\s/`'\"()\[\]|<>*]*)/")
ELLIPSES = ("…", "...")


def names(name, work_item_id):
    """Whether a cited directory name, possibly abbreviated, is this id."""
    for dots in ELLIPSES:
        if name.endswith(dots):
            stem = name[: -len(dots)]
            return bool(stem) and work_item_id.startswith(stem)
    return name == work_item_id


def tracked_text(root):
    """`(repo-relative path, text)` for every tracked text file outside
    `seal/threads/`. A file holding a NUL byte is binary and skipped."""
    r = subprocess.run(["git", "-C", root, "ls-files", "-z"], capture_output=True)
    if r.returncode != 0:
        return
    for rel in r.stdout.decode("utf-8", "replace").split("\0"):
        if not rel or rel.startswith(SPECS + "/"):
            continue
        try:
            with open(under(root, rel), "rb") as f:
                data = f.read()
        except OSError:
            continue
        if b"\0" in data:
            continue
        yield rel, data.decode("utf-8", "replace")


def citations(root, work_item_ids):
    """`({id: ["path:line", ...]}, [tests/ files naming seal/threads])`.

    A path outside `seal/threads/` that cites into a directory `--apply` removes
    stops resolving when it goes, and every `tests/` file that reads
    `seal/threads` is a check the skill says has to be answered first. One scan
    of the tracked tree answers both."""
    cited = {i: [] for i in work_item_ids}
    readers = []
    if not work_item_ids:
        return cited, readers
    for rel, text in tracked_text(root):
        if rel.startswith(TESTS) and SPECS in text:
            readers.append(rel)
        if "threads/" not in text:
            continue
        for number, line in enumerate(text.split("\n"), start=1):
            for m in CITATION_RE.finditer(line):
                for work_item_id in work_item_ids:
                    if names(m.group(1), work_item_id):
                        where = f"{rel}:{number}"
                        if where not in cited[work_item_id]:
                            cited[work_item_id].append(where)
    return cited, sorted(readers)


def report(found, ref, out):
    """The dry run: the groups, the designs to read whole, the open rows, the
    files named like a record and not read, the judgments and what `--apply`
    removes. It refuses nothing, so it exits 0. In local mode
    it names the root first, lists each released work item with the pull
    request that merged it and each unreleased one with why, and says no
    commit holds what `--apply` removes."""
    write = out.write
    t = found["timeline"]
    local = found["local"]
    rows = dict(found["rows"])
    count = sum(len(r) for r in rows.values())
    total = len(found["released"])
    if local:
        write(LOCAL_LINE.format(home=local))
    write(
        f"released at {ref}: {total} work item{plural(total)}; "
        f"{len(found['unreleased'])} unreleased and untouched\n"
        f"    {t['with_rules']} state rule changes, {len(t['nothing'])} hold the "
        f"no-change block, {len(t['whole'])} to read whole, "
        f"{len(t['spec_less'])} wrote no frame/design.md\n"
        f"    {len(t['groups'])} group{plural(len(t['groups']))}; {count} open "
        f"row{plural(count)} in {len(rows)} record{plural(len(rows))}\n"
    )
    if local and found["released"]:
        write(f"\n{MERGED_HEADING}\n")
        for work_item_id in found["released"]:
            number, commit = found["merged"][work_item_id]
            write(
                f"    {work_item_id}  pull request #{number}  merge commit {commit}\n"
            )
    if local and found["unreleased"]:
        write(f"\n{UNMERGED_HEADING}\n")
        for work_item_id in found["unreleased"]:
            write(f"    {work_item_id}  {found['why'][work_item_id]}\n")
    unordered = UNORDERED_LOCAL if local else UNORDERED
    if t["groups"]:
        write(f"\n{GROUPS_HEADING}\n")
        for n, g in enumerate(t["groups"], 1):
            write(f"\ngroup {n}\n")
            for p, span, why in g["places"]:
                write(f"    {place_line(p, span, why)}\n")
            for k, (work_item_id, op, said) in enumerate(g["ops"], 1):
                write(f"    {k}. {op_line(work_item_id, op, said)}\n")
            for a, b in g["unordered"]:
                write(f"    {unordered.format(a=a, b=b)}\n")
    if t["whole"]:
        write(f"\n{WHOLE_HEADING}\n")
        for work_item_id, line, why in t["whole"]:
            where = f"{SPECS}/{work_item_id}/{DESIGN}" + (f":{line}" if line else "")
            write(f"    {work_item_id}  {where}  {why}\n")
    if t["nothing"]:
        write(f"\n{NOTHING_HEADING.format(nothing=found['nothing'])}\n")
        write("".join(f"    {i}\n" for i in t["nothing"]))
    if t["spec_less"]:
        write("\nno `frame/design.md`, so no rule stated:\n")
        write("".join(f"    {i}\n" for i in t["spec_less"]))
    if rows:
        write(f"\n{ROWS_HEADING}\n")
        for work_item_id, held in found["rows"]:
            write(f"    {work_item_id}\n")
            for name, item, paths in held:
                write(f"        open in {name}: {item}\n")
                for path, present in paths:
                    there = "in the tree" if present else "not in the tree"
                    write(f"            `{path}` {there}\n")
    if found["misplaced"]:
        write(f"\n{MISPLACED_HEADING}\n")
        for work_item_id, held in found["misplaced"]:
            for rel, place in held:
                path = f"{SPECS}/{work_item_id}/{rel}"
                write(f"    {MISPLACED.format(path=path, place=place)}\n")
    groups, unread = found["judgments"]
    if groups or unread:
        write(f"\n{JUDGMENTS_HEADING}\n")
        for work_item_id, why in unread:
            write(
                f"    {work_item_id}  {SPECS}/{work_item_id}/{PLAN}  not read: {why}\n"
            )
        for against, members in groups:
            write(f"\njudged against: {against or 'an empty cell'}\n")
            for work_item_id, rounds, held in members:
                counted = (
                    f"{rounds} round{plural(rounds)}"
                    if rounds is not None
                    else "its trail/rounds is not a directory this can list, "
                    "so no round was counted"
                )
                write(f"    {work_item_id}  {counted}\n")
                for line, date, judgment, grounds in held:
                    write(f"        {PLAN}:{line}  {date}  {judgment}\n")
                    write(f"            grounds: {grounds}\n")
    if found["released"]:
        write(f"\n{REMOVES_HEADING_LOCAL if local else REMOVES_HEADING}\n")
        for work_item_id in found["released"]:
            held = len(rows.get(work_item_id, []))
            when = f"once its {held} open row{plural(held)} close" if held else "now"
            write(f"    {SPECS}/{work_item_id}/  {when}\n")
            for where in found["citations"].get(work_item_id, []):
                write(f"        cited from {where}\n")
        write(f"\n{READERS_HEADING}\n")
        for rel in found["readers"] or ["none under tests/"]:
            write(f"    {rel}\n")
    write(
        "\nNothing was written and nothing was removed. The settling session "
        "writes the\nsections and closes the rows; `seal settle --apply` removes.\n"
    )
    return 0


# --- the apply -------------------------------------------------------------

AFTER_HEADING = (
    "after the removals — the index and the one read, as `seal fold` reads "
    "them; neither\nrefuses anything here:"
)


def write_after(root, policy, out):
    """The index rows owed and the documents past `Document token ceiling`,
    read by `fold_check.py` over the policy root the settling session wrote.
    A row it cannot read is said in its own sentence, never as a traceback
    after the removals."""
    fold = load(FOLD_CHECK, "agentic_fold_check_for_settle")
    try:
        ceiling = fold.declared(fold.seal_home(root))[0]
        lines = list(fold.index_problems(root, policy) or [])
        if ceiling is not None:
            lines += fold.past_ceiling_lines(
                fold.past_ceiling(root, policy, ceiling), ceiling
            )
    except fold.Unusable as refused:
        lines = [f"not read: {refused}"]
    if lines:
        out.write(f"\n{AFTER_HEADING}\n" + "".join(f"    {i}\n" for i in lines))


def closed_rows(records, directory, reader):
    """`[(item, what closed it)]` for each closed row of DIRECTORY's record
    under RECORDS in the working tree, read by
    `unverified_check.py#check_text`."""
    text = read_text(records, f"{directory}/{reader.OVERVIEW}")
    if text is None:
        return []
    _, closed, _ = reader.check_text(text)
    return [(item, who) for _, item, who in closed]


def apply(found, root, out):
    """Remove each released directory whose record holds no open row in the
    working tree, printing the rows its record closed, and keep and name
    each one that still holds a row. Under each directory's line, each of
    its misplaced record files (`misplaced`) is named as not read, and
    decides nothing. The directories are under
    `found["records"]`: the repository's top ROOT, or in local mode the
    common git directory.

    **The candidates are read from the tree again, not taken from `survey`**:
    a classification made for a printed list is not a guard on a destructive
    act; the misplaced record files are read again the same way. `found`
    gives *released*, which only git answers, and in local mode `gh` with
    git."""
    reader = load(READER, "agentic_unverified_reader")
    records = found["records"]
    ids = sorted(set(work_items(records)) & set(found["released"]))
    removed, kept = 0, 0
    for work_item_id in ids:
        directory = f"{SPECS}/{work_item_id}"
        rows = reader.open_record_rows(records, None, directory)
        unread = [
            f"    not read: {MISPLACED.format(path=f'{directory}/{rel}', place=place)}\n"
            for rel, place in misplaced(records, work_item_id, reader)
        ]
        if rows:
            kept += 1
            out.write(
                f"kept {directory}/: its record holds {len(rows)} open "
                f"row{plural(len(rows))}; close each (`closed` with what closed "
                "it) and run `seal settle --apply` again\n"
            )
            for name, item in rows:
                out.write(f"    open in {name}: {item}\n")
            out.write("".join(unread))
            continue
        closed = closed_rows(records, directory, reader)
        shutil.rmtree(under(records, directory))
        removed += 1
        out.write(f"removed {directory}/\n")
        out.write("".join(unread))
        for item, who in closed:
            out.write(f"    closed in {reader.OVERVIEW}: {item}\n")
            out.write(f"        what closed it: {who}\n")
    policy = reader.policy_root(root)
    if os.path.isdir(under(root, policy)):
        write_after(root, policy, out)
    out.write(
        f"\nremoved {removed} director{plural(removed, 'ies', 'y')}; kept {kept}, "
        f"each with a row to close\n"
    )
    return 1 if kept else 0


def main(argv=None):
    """The dry run or the apply; the exit code is the verdict."""
    ap = argparse.ArgumentParser(
        prog="seal settle",
        description="Show the released designs' rule changes by section, and "
        "remove released work item directories.",
    )
    ap.add_argument(
        "--root", default=None, help="repository root (default: the one this is run in)"
    )
    ap.add_argument(
        "--released-at",
        default="origin/main",
        metavar="REF",
        help="the branch a release merges to. A work item is released when "
        "its directory is present there, or in local mode when this ref "
        "reaches the merge commit of the pull request from the work item's "
        "branch (default: origin/main)",
    )
    ap.add_argument(
        "--apply",
        action="store_true",
        help="remove each released work item directory whose record holds no "
        "open row in the working tree, and name each one kept",
    )
    args = ap.parse_args(argv)

    root = os.path.abspath(args.root or os.getcwd())
    # The root is resolved through the one resolver, `hooks/lib/optin.py#home_at`,
    # handed the common git directory this also needs for the opt-out sentence.
    optin = load(OPTIN, "agentic_optin")
    # The repository's top, as `fold_check.py` resolves it: the policy root,
    # the tracked files and `tests/` are read from it, and a subdirectory
    # holds none of them. `repo_root` answers "" outside a repository, where
    # ROOT stays as given and the no-root refusal below answers.
    root = optin.repo_root(root) or root
    common = optin.git_common_dir(root)
    home = optin.home_at(root, common)
    if not home:
        # `home_at` answers "" for no root and for an opt-out; they are two
        # sentences. `isfile`, as `home_at` reads it: a directory of the
        # marker's name is not an opt-out.
        if common and os.path.isfile(os.path.join(common, optin.SCRATCH)):
            sys.stderr.write(
                f"settle: {root} has opted out — `{optin.SCRATCH}` is under "
                "its git directory, so every gate in this plugin reads it as "
                "a repository that never opted in and this command will "
                "remove nothing. Delete that file to turn them back on.\n"
            )
            return 2
        sys.stderr.write(
            f"settle: {root} has no {SPECS}/ at either place — nothing was "
            "read. This command settles work items, and a repository with "
            "none has nothing to settle.\n"
        )
        return 2
    local, records = records_of(root, home)
    # A settled root is not an unusable one (#517): an empty `seal/threads/`, or
    # none in a fresh checkout of that commit, is where a complete settle ends.
    if not work_items(records):
        if local:
            sys.stdout.write(SETTLED_LOCAL.format(home=home))
        else:
            sys.stdout.write(SETTLED.format(root=root, specs=SPECS))
        return 0

    try:
        found = survey(root, args.released_at, home)
    except Unasked as refused:
        sys.stderr.write(UNASKED.format(why=refused))
        return 2
    if found is None:
        sys.stderr.write(
            f"settle: --released-at {args.released_at} does not resolve in {root} — nothing was "
            "read. Without it every work item reads as unreleased and this "
            "would report nothing to settle, which is the one answer it must "
            "not give by accident.\n"
        )
        return 2
    if args.apply:
        return apply(found, root, out=sys.stdout)
    return report(found, args.released_at, out=sys.stdout)


if __name__ == "__main__":
    # A console that cannot encode what this prints kills it with stdout
    # empty, which is how a hook says "nothing to see here". `hooks/lib/console.py`
    # owns the reasoning and the three decisions behind these lines.
    for _name, _errors in (
        ("stdin", "replace"),
        ("stdout", "replace"),
        ("stderr", "backslashreplace"),
    ):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)
    sys.exit(main())
