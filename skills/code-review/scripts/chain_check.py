#!/usr/bin/env python3
"""chain-check — at the pull request, the records the declared parties owe
are in the tree and agree with HEAD.

Run by CI on every pull request (`.github/workflows/hygiene.yml`). It judges
the `seal/specs/<id>/routing.md` naming the pull request's branch and every
one its own commits add or change. One that reached the branch inside another
pull request's squash was judged at that pull request and is named, not
judged (`carried_by`). The arms are five:

  declaration   the file parses as a routing declaration; one the pull
                request removed is accepted where the work item was retired
  frame         `Planning | framer`: `spec.md` and `plan.md` are committed,
                `spec.md` ends with the framer's mark, and every `Reframed`
                line under it names the framer
  records       `Review | through the review chain`: `rounds/` holds at least
                one `round-N.md`; each holds one `## Findings` section whose
                every `### ` finding carries one `Verdict:` line reading
                `fixed <commit HEAD descends from>`, `answered` or
                `deferred <home>`, and whatever the reader cannot read is
                refused; the last record's `Target SHA` is HEAD, or every
                commit after it touches only the work item's own directory
  broad gate    `broad-gate.md`'s newest run is HEAD, or every commit after it
                touches only the work item's own directory
  guarantee     `guarantee.md` names HEAD, or every commit after it touches
                only the sealer's two files, and its one `Verdict:` line
                reads `sound`

A ready pull request fails on any of them. A draft, or a run that observed no
pull request, prints the same lines and exits 0. `docs/the-review-record.md`
states the record and the rules these arms hold.

Usage:
  chain_check.py --baseline <ref> [--root DIR] [--worktree] [--sealing]

`--worktree` reads the records from the working tree instead of HEAD, for a
check before the commit; CI never passes it. `--sealing` is the broad gate's
own run, before it writes `broad-gate.md` and the sealer `guarantee.md`: those
two arms print and do not fail.

Exit: 0 nothing to refuse · 1 a refusal, each named `path:line  why` (a
GitHub annotation in CI) · 2 the check could not run.
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
ROUTING = os.path.join(HERE, "..", "..", "..", "hooks", "routing.py")

TARGET = "Target SHA"
BROAD_GATE = "Broad gate"
BROAD_GATE_FILE = "broad-gate.md"
GUARANTEE_FILE = "guarantee.md"
# The sealer's two files: the only ones that may follow the commit its
# guarantee names, since it audited everything else on the branch.
SEALERS_FILES = (BROAD_GATE_FILE, GUARANTEE_FILE)
VERDICT_LINE = re.compile(r"^Verdict:\s*(.*?)\s*$")
SOUND = "sound"
NOT_SOUND = "not sound"
UNDECIDABLE = "undecidable"
# What a broad-gate entry is separated from the run behind it by. The newest
# run stands first; `broad_gate.py#kept_runs` writes the rest behind it.
EARLIER_RUN = "; earlier run: "

# A round record's findings: the one `## Findings` section, a `### ` section
# per finding, and in each exactly one line `Verdict: <value>` — at the start
# of the line, no emphasis, no table cell. That line is the one fact the
# check reads of a finding, and a spelling it does not read is refused by
# name, never passed (`findings`). These stay as the record's vocabulary,
# which no `Record language` translates.
FINDINGS_HEADING = "## Findings"
FINDING_LEVEL = 3
VERDICT = "Verdict:"
VERDICT_LABEL = re.compile(r"^" + re.escape(VERDICT) + r" (.*)$")
OPEN = "open"
FIXED = "fixed"
ANSWERED = "answered"
DEFERRED = "deferred"
# `fixed <commit>`: seven to forty lowercase hex digits and nothing after;
# `deferred <home>`: a home after the word, beginning and ending with a
# character that is not a space.
FIXED_VALUE = re.compile(r"^fixed ([0-9a-f]{7,40})$")
DEFERRED_VALUE = re.compile(r"^deferred (\S(?:.*\S)?)$")
SHAPES = "`open`, `fixed <commit>`, `answered` or `deferred <home>`"
ANSWERS = "`fixed <commit>`, `answered` or `deferred <home>`"
NO_FINDINGS = (
    f"no `{FINDINGS_HEADING}` section: a round record holds one, with a "
    "`### ` section and one `Verdict:` line per finding"
)
TWO_FINDINGS = f"a second `{FINDINGS_HEADING}` section; a round record holds one"
OUTSIDE = (
    f"a `Verdict:` line outside a finding: the check reads one inside each "
    f"`### ` section of `{FINDINGS_HEADING}`, and none elsewhere"
)
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
    """Import a sibling script by path, or raise SystemExit naming it.

    Reads: observed — the file at `path`, imported; unknown refused"""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"chain-check: cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def git(root, *args):
    """`git -C root <args>`'s stdout, or None where git exited non-zero.

    Reads: observed — git's output and exit code; unknown refused"""
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
    tree and untracked files count as added.

    Reads: observed — `git diff --raw -z --no-renames`; unknown refused"""
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
    """The routing declarations among `paths` that were not only moved.

    Reads: nothing — filters the paths `changed` handed it"""
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
    request's.

    Reads: observed — `git log`'s committer and subject; unknown refused"""
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
    """The regular files git carries directly in `where` at HEAD, by name.

    Reads: observed — `git ls-tree -z HEAD`; unknown refused"""
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
    """The regular files directly in `where` on disk, symbolic links excluded.

    Reads: observed — the directory listing; unknown refused"""
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
    where there is none.

    Reads: observed — `git show HEAD:<rel>` or the file; unknown refused"""
    if WORKTREE:
        try:
            with open(
                os.path.join(root, *rel.split("/")), encoding="utf-8", errors="replace"
            ) as f:
                return f.read()
        except OSError:
            return None
    return git(root, "show", f"HEAD:{rel}")


def round_records(routing, root, item):
    """`<item>/rounds/round-N.md` git carries, lowest round first.

    Reads: observed — the listing `tracked_files` or `worktree_files` returns; unknown refused"""
    where = f"{item}/{routing.ROUNDS_DIR}"
    listed = worktree_files(root, where) if WORKTREE else tracked_files(root, where)
    found = []
    for name in listed:
        number = routing.round_number(name)
        if number is not None:
            found.append((number, f"{where}/{name}"))
    return [rel for _, rel in sorted(found)]


def event_payload_present():
    """True where `GITHUB_EVENT_PATH` names a file.

    Reads: observed — the environment and the file's existence; unknown passed"""
    path = os.environ.get("GITHUB_EVENT_PATH")
    return bool(path) and os.path.exists(path)


def pull_request_state(root=None, which=shutil.which, run=subprocess.run):
    """(`draft` | `ready` | `unknown`, where that was read from).

    The event payload GitHub writes is the answer wherever it exists; with
    none, `gh pr view` is asked in `root`. A payload that cannot answer is
    `unknown`, which `main` judges as ready, so a harness fault is never the
    quiet way past the check.

    Reads: observed — the event payload's JSON, or `gh`'s; unknown refused"""
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
    """(`draft` | `ready` | `unknown`, where) from `gh pr view --json isDraft`.

    Reads: observed — `gh`'s exit code and JSON; unknown refused"""
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
    """The value of every `| label | value |` row, in order.

    Reads: owned — table rows `table_rows` split; unknown passed"""
    return [
        cells[1].strip()
        for cells in rows
        if len(cells) >= 2 and cells[0].strip() == label
    ]


def field(rows, label):
    """The value of the one `| label | value |` row, or None where it is
    absent or stands more than once.

    Reads: owned — table rows `table_rows` split; unknown refused"""
    found = fields(rows, label)
    return found[0] if len(found) == 1 else None


def table_rows(reader, lines):
    """Every table row in already-`readable` lines, as lists of cells.

    Reads: owned — markdown table rows, through the shared reader; unknown passed"""
    out = []
    for line in lines:
        cells = reader.split_row(line)
        if cells is not None:
            out.append(cells)
    return out


def section_end(reader, lines, start):
    """The index of the line that ends the section opened at `start`: the
    first heading of its level or shallower, else `len(lines)`.

    Reads: owned — headings, through the shared reader's `heading_level`; unknown passed"""
    level = reader.heading_level(lines[start]) or 1
    for i in range(start + 1, len(lines)):
        found = reader.heading_level(lines[i])
        if found is not None and found <= level:
            return i
    return len(lines)


def verdict_of(value):
    """`(kind, its commit or home)` for one `Verdict:` value, or None.

    The four shapes, read as written and nothing else: `open`, `answered`,
    `fixed <commit>` with seven to forty lowercase hex digits, and
    `deferred <home>`. A different case, emphasis, a trailing word or mark,
    a bare `fixed` or `deferred` is None, which the arm refuses by name.

    Reads: owned — one value `findings` cut from its line; unknown refused"""
    if value in (OPEN, ANSWERED):
        return value, None
    for kind, shape in ((FIXED, FIXED_VALUE), (DEFERRED, DEFERRED_VALUE)):
        found = shape.match(value)
        if found:
            return kind, found.group(1)
    return None


def deferred_home(value):
    """The home a `deferred <home>` value names, or None.

    Reads: owned — through `verdict_of`; unknown refused"""
    verdict = verdict_of(value)
    return verdict[1] if verdict and verdict[0] == DEFERRED else None


def issue_of(home):
    """N where a deferral's home is exactly `#N`, else None.

    Reads: guess — a home `deferred_home` read; unknown refused"""
    found = ISSUE_RE.fullmatch(home or "")
    return int(found.group(1)) if found else None


def findings(reader, lines, rel):
    """`([(line, heading, verdict)], errors)` for a record's findings.

    `lines` are `reader.readable`'s, so a `Verdict:` inside a fence or a
    comment is no line. The one `## Findings` section is split at its `### `
    headings, and each holds exactly one line `VERDICT_LABEL` matches, its
    value read by `verdict_of`. Everything the reader cannot read is an
    error `(rel, line, why)` naming the finding's heading, in line order: no
    `## Findings` section or two, a finding with no `Verdict:` line or with
    two, a value outside the four shapes, a `Verdict:` line outside a
    finding. Nothing else of the record is read — not a severity, a
    location, an answer or another section's table.

    Reads: guess — the warden's record, a person-written file; unknown refused"""
    starts = reader.sections(lines, FINDINGS_HEADING)
    if not starts:
        return [], [(rel, 0, NO_FINDINGS)]
    if len(starts) > 1:
        return [], [(rel, starts[1] + 1, TWO_FINDINGS)]
    start = starts[0]
    end = section_end(reader, lines, start)
    heads = [
        i
        for i in range(start + 1, end)
        if reader.heading_level(lines[i]) == FINDING_LEVEL
    ]
    spans = list(zip(heads, [*heads[1:], end], strict=False))
    inside = {i for first, stop in spans for i in range(first, stop)}
    found, errors = [], []
    for i, line in enumerate(lines):
        if VERDICT_LABEL.match(line) and i not in inside:
            errors.append((rel, i + 1, OUTSIDE))
    for first, stop in spans:
        heading = lines[first].strip()
        said = [
            (i, VERDICT_LABEL.match(lines[i]).group(1))
            for i in range(first + 1, stop)
            if VERDICT_LABEL.match(lines[i])
        ]
        if not said:
            errors.append(
                (
                    rel,
                    first + 1,
                    f"{heading} {DASH} no `Verdict:` line: a finding carries one, "
                    f"at the start of a line and with no emphasis, reading {SHAPES}",
                )
            )
            continue
        if len(said) > 1:
            errors.append(
                (
                    rel,
                    said[1][0] + 1,
                    f"{heading} {DASH} {len(said)} `Verdict:` lines; a finding "
                    "carries one",
                )
            )
            continue
        i, value = said[0]
        verdict = verdict_of(value)
        if verdict is None:
            errors.append(
                (
                    rel,
                    i + 1,
                    f"{heading} {DASH} reads `Verdict: {value}`, which the check "
                    f"cannot read: a verdict is {SHAPES}",
                )
            )
            continue
        found.append((i + 1, heading, verdict))
    errors.sort(key=lambda error: error[1])
    return found, errors


def target_of(reader, text):
    """The first SHA-shaped word of a record's `Target SHA` row, or None.

    Reads: guess — the warden's record; unknown refused"""
    rows = table_rows(reader, reader.readable(text or ""))
    found = SHA_RE.search(reader.visible(field(rows, TARGET) or ""))
    return found.group(0) if found else None


def newest_run(reader, text):
    """The commit the newest run of `broad-gate.md`'s `Broad gate` row was
    taken at — the first word of its first entry, where that word is
    SHA-shaped — or None.

    Reads: owned — the file `broad_gate.py` writes; unknown refused"""
    rows = table_rows(reader, reader.readable(text or ""))
    cell = reader.visible(field(rows, BROAD_GATE) or "")
    words = EMPHASIS.sub("", cell.split(EARLIER_RUN)[0]).split()
    return words[0] if words and SHA_RE.fullmatch(words[0]) else None


def is_ancestor(root, sha, ref):
    """True where `sha` is `ref` or an ancestor of it.

    Reads: observed — `git merge-base --is-ancestor`'s exit code; unknown refused"""
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
    are not the branch's.

    Reads: observed — `git rev-parse`, `rev-list` and `diff-tree`; unknown refused"""
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
    """The sentence `follows`'s answer is refused with, about `what`.

    Reads: nothing — formats the answer its caller hands it"""
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
    every `Reframed` line under it), read from the last non-empty line up.

    Reads: guess — the foot of a person-written `spec.md`; unknown refused"""
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
    """[problem] for a declaration that says a framer drew the frame.

    Reads: guess — `spec.md`'s foot and the presence of `plan.md`; unknown refused"""
    if declared.get("planning") != routing.BY_FRAMER:
        return []
    who = f"`{routing.PLANNING} | {routing.BY_FRAMER}`"
    problems = []
    spec = read_record(root, f"{item}/spec.md")
    if spec is None:
        problems.append(f"declares {who} and git carries no {item}/spec.md")
    if read_record(root, f"{item}/plan.md") is None:
        problems.append(f"declares {who} and git carries no {item}/plan.md")
    if spec is None:
        return problems
    mark, reframes = frame_foot(reader, spec)
    if mark is None:
        problems.append(
            f"{item}/spec.md does not end with `Framed <date> by <who>, before "
            "the build.`, with any `Reframed <date> by <who>, after round <N>.` "
            "lines under it"
        )
    elif mark[0].startswith("<") or mark[1].startswith("<"):
        problems.append(f"{item}/spec.md ends with the template's unfilled mark")
    elif mark[1] != routing.BY_FRAMER:
        problems.append(
            f"{item}/routing.md says {who} and {item}/spec.md's mark says `{mark[1]}`"
        )
    for when, by, n in reframes:
        line = f"`Reframed {when} by {by}, after round {n}.`"
        if when.startswith("<") or by.startswith("<"):
            problems.append(f"{item}/spec.md's foot carries the unfilled line {line}")
        elif by != routing.BY_FRAMER:
            problems.append(
                f"{item}/routing.md says {who} and {item}/spec.md's foot says {line}"
            )
    return problems


def records(reader, routing, root, item, rel, base):
    """[(path, line, problem)] for a work item declared through the review
    chain: no record; a record `findings` cannot read; a finding at `open`;
    a `fixed` naming a commit HEAD does not descend from; a last record
    behind HEAD. A finding is named by its line and its heading.

    Reads: guess — the warden's records, through `findings` and `target_of`; unknown refused"""
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
    problems = []
    for path in found:
        text = read_record(root, path)
        lines = reader.readable(text or "")
        read, errors = findings(reader, lines, path)
        problems.extend(errors)
        for line, heading, (kind, commit) in read:
            if kind == OPEN:
                problems.append(
                    (
                        path,
                        line,
                        f"{heading} {DASH} reads `Verdict: {OPEN}`: the fix pass "
                        f"answers it with {ANSWERS}",
                    )
                )
            elif kind == FIXED and not is_ancestor(root, commit, "HEAD"):
                problems.append(
                    (
                        path,
                        line,
                        f"{heading} {DASH} reads `Verdict: {FIXED} {commit}`, and "
                        f"HEAD does not descend from `{commit}`: a `{FIXED}` names "
                        "a commit on this branch",
                    )
                )
    last = found[-1]
    target = target_of(reader, read_record(root, last))
    if target is None:
        problems.append((last, 0, f"no SHA in its `{TARGET}` row"))
    else:
        behind = follows(root, target, base, item)
        if behind is not None:
            problems.append(
                (
                    last,
                    0,
                    follows_reason(behind, f"the last round's `{TARGET}`")
                    + (f"; {VERIFYING_ROUND}" if behind[0] == "after" else ""),
                )
            )
    return problems


def broad_gate(reader, root, item, base):
    """[(path, line, problem)] for the work item's `broad-gate.md`: absent,
    unreadable, or naming a run behind HEAD.

    Reads: owned — the file `broad_gate.py` writes, through `newest_run`; unknown refused"""
    rel = f"{item}/{BROAD_GATE_FILE}"
    text = read_record(root, rel)
    if text is None:
        return [
            (
                rel,
                0,
                "git carries no broad-gate file: the sealer runs `broad-gate "
                "--base <base> --record <item>`, which writes it on a green run",
            )
        ]
    sha = newest_run(reader, text)
    if sha is None:
        return [(rel, 0, f"no SHA in its `{BROAD_GATE}` row")]
    behind = follows(root, sha, base, item)
    if behind is None:
        return []
    return [(rel, 0, follows_reason(behind, "the newest broad-gate run"))]


def verdicts_of(reader, text):
    """[(line number, value)] for every `Verdict:` line outside comments and
    fences, emphasis removed from the value.

    Reads: guess — `guarantee.md`, which the sealer writes; unknown refused"""
    found = []
    for i, line in enumerate(reader.readable(text or "")):
        m = VERDICT_LINE.match(EMPHASIS.sub("", reader.visible(line)))
        if m:
            found.append((i + 1, m.group(1).strip()))
    return found


def verdict_word(value):
    """`sound`, `not sound` or `undecidable` where the value begins with one
    of them, else the value as it reads.

    Reads: nothing — maps the value `verdicts_of` read"""
    s = value.strip().lower()
    if s == SOUND:
        return SOUND
    for word in (NOT_SOUND, UNDECIDABLE):
        if s == word or s.startswith(word + " "):
            return word
    return value.strip()


def guarantee(reader, root, item, base):
    """[(path, line, problem)] for the work item's `guarantee.md`: absent, no
    commit, a commit with anything but the sealer's two files after it, or
    one `Verdict:` line that does not read `sound`.

    Reads: guess — the file the sealer writes, through `target_of` and `verdicts_of`; unknown refused"""
    rel = f"{item}/{GUARANTEE_FILE}"
    text = read_record(root, rel)
    if text is None:
        return [
            (
                rel,
                0,
                "git carries no guarantee file: the sealer writes it from "
                "`templates/sdd-guarantee.md` after its broad run",
            )
        ]
    problems = []
    sha = target_of(reader, text)
    if sha is None:
        problems.append((rel, 0, f"no SHA in its `{TARGET}` row"))
    else:
        behind = follows(root, sha, base, item, only=SEALERS_FILES)
        if behind is not None:
            problems.append(
                (
                    rel,
                    0,
                    follows_reason(behind, "the guarantee", "the sealer's two files")
                    + ("; the sealer runs again" if behind[0] == "after" else ""),
                )
            )
    verdicts = verdicts_of(reader, text)
    if len(verdicts) != 1:
        problems.append(
            (
                rel,
                verdicts[1][0] if verdicts else 0,
                f"{len(verdicts)} `Verdict:` lines; the guarantee carries one",
            )
        )
    elif verdict_word(verdicts[0][1]) != SOUND:
        line, value = verdicts[0]
        problems.append(
            (
                rel,
                line,
                f"the sealer's verdict reads `{value}`, and a ready pull request "
                f"needs `{SOUND}`: fix what it names, or answer its question "
                "under it, and the sealer runs again at the new HEAD",
            )
        )
    return problems


def local_root(root, routing):
    """The local-mode root of `root`, or "" where the root is shared or absent.

    Reads: observed — `optin.home_at` and `optin.home_paths`; unknown passed"""
    optin = routing.optin
    common = optin.git_common_dir(root)
    home = optin.home_at(root, common)
    if not home:
        return ""
    shared, _local = optin.home_paths(root, common)
    return "" if os.path.realpath(home) == os.path.realpath(shared) else home


def tracked_declarations(root, routing):
    """(path, parsed) for every routing declaration git carries at HEAD.

    Reads: guess — `routing.md` files, through `routing.parse`; unknown refused"""
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
    elsewhere.

    Reads: observed — the environment, git, and the declarations at HEAD; unknown refused"""
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


def retired(reader, root, fork, item):
    """The sentence a removed declaration is accepted with, or None.

    Reads: observed — `docs/` markers and the merge base, through the shared reader; unknown refused"""
    name = os.path.basename(item)
    if name in reader.folded_items(root):
        return f"retired: `docs/` carries <!-- specs/{name} -->"
    if (
        fork
        and not os.path.isdir(os.path.join(root, item))
        and reader.retired_by_rule(root, fork, item)
    ):
        return "retired: by the rule — nothing open at the merge base"
    return None


def main(argv=None):
    """The check. Returns the exit code.

    Reads: guess — the arguments and the tree, through the arms above; unknown refused"""
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

    try:
        reader = load(READER, "specseal_unverified_reader")
        routing = load(ROUTING, "specseal_routing")
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
    if not declarations:
        print(reader.annotate("notice", "", 0, why))
        return 0

    fork = reader.merge_base(root, args.baseline)
    problems, notices = [], []
    for rel in declarations:
        item = os.path.dirname(rel)
        text = read_record(root, rel)
        if text is None:
            said = retired(reader, root, fork, item)
            if said:
                notices.append((rel, 0, said))
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
        if declared["review"] == routing.CHAIN:
            problems.extend(records(reader, routing, root, item, rel, args.baseline))
        gate = broad_gate(reader, root, item, args.baseline)
        gate += guarantee(reader, root, item, args.baseline)
        if args.sealing:
            notices.extend((p, n, f"{SEALING_SAYS}: {m}") for p, n, m in gate)
        else:
            problems.extend(gate)

    for rel, line, message in notices:
        print(reader.annotate("notice", rel, line, message))
    kind = "error" if strict else "notice"
    for rel, line, message in problems:
        print(reader.annotate(kind, rel, line, message))
    return 1 if problems and strict else 0


if __name__ == "__main__":
    for _name, _errors in (
        ("stdin", "replace"),
        ("stdout", "replace"),
        ("stderr", "backslashreplace"),
    ):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)
    sys.exit(main())
