#!/usr/bin/env python3
"""Generate the warden's replay cases from round records.

A replay case is a historical review target: the clone at the commit a
round record reviewed and the base it was reviewed against. Its truth is
every finding the round closed `fixed` that the next round confirmed
closed, and every truth `recurred_truths.json` adds for the case or widens
(`truths_with`, which the other two generators read too); each is a
`truth-` grader over the `location:` lines of the round record the warden
writes today. A record comes in one of two shapes:

  labelled   0.22.0's record (`docs/the-review-record.md` *The round
             record*), judged by the `chain_check.py` of the commit that
             last wrote it and its lines read by that commit's reader
             (#1012), with the grammar that commit's
             `docs/the-review-record.md` holds, so each record is judged by
             the grammar in force when it was written (the owner's decision
             on #985) and a line the grammar gained later is not owed; a
             record no commit wrote is read by this tree's check. The
             commit and the base are its `target:` line, a finding is a
             `### <n>. ` section at `verdict: fixed <commit>`, and the next
             round confirms it on a `confirms: round-<N>#<n>` line. It
             carries no asked paragraph, so the prompt carries none
  table      the records before it: the `Target SHA` row, the base and the
             prompt's paragraph from `## What this round was asked`, a
             numbered red or yellow row, and a green row naming it

Round records come from the working tree and from the last two release
tags (`git show <tag>:seal/specs/<id>/rounds/round-N.md`); `--case` reads
every release tag, so a committed case still regenerates after the release
that moved its records out of the last two.

Usage:
  replay_targets.py --list                 every round with truth, and why
                                           a round with none was left out
  replay_targets.py --count 4 [--out DIR]  write the COUNT smallest targets,
                                           one per work item, under DIR
                                           (evals/behaviour/proofer/)
  replay_targets.py --case NAME [--out DIR]
                                           write the named case alone
                                           (`replay-<id>-rN`), from any
                                           release tag; repeatable

Exit codes: 0 written or listed · 1 fewer targets than --count, or a
named case no release tag's records hold · 2 the arguments were unusable.
"""

import argparse
import ast
import atexit
import functools
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import behaviour

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "evals", "behaviour", "proofer")
CHECK = os.path.join(ROOT, "skills", "code-review", "scripts", "chain_check.py")
SHA = re.compile(r"[0-9a-f]{7,40}")
RECORD = re.compile(r"seal/specs/(?P<item>[^/]+)/rounds/round-(?P<n>\d+)\.md")
FINDING = re.compile(r"^(?P<marker>🔴|🟡) (?P<k>\d+)$")
CONFIRMS = re.compile(
    r"round (?P<n>\d+)'s (?:blocking )?(?:finding|🟡|🔴) (?P<k>\d+) is closed"
)
AGAINST_AT = re.compile(
    r"against\s+`?(?P<ref>origin/[\w./-]+?)`?(?:'s merge-base)?(?:\s+at)?\s+(?P<base>[0-9a-f]{7,40})\b"
)
FIX_RANGE = re.compile(r"(?P<base>[0-9a-f]{7,40})\.\.(?P<head>[0-9a-f]{7,40})")
AGAINST = re.compile(r"against\s+`?(?P<ref>origin/[\w./-]*[\w])`?")
LOCATION = re.compile(
    r"`(?P<path>[\w./-]+\.\w+)(?::(?P<line>\d+)(?:[-\N{EN DASH}]\d+)?|#(?P<unit>[\w.]+))?`"
)
WINDOW = 15
MODEL = "claude-opus-5-5"
# What every truth's pattern opens with: a finding's `location:` line.
LOCATION_LINE = "^location: .*"
# The truths a run recurred on, which the three generators add (#971).
TRUTHS = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "recurred_truths.json"
)


def git(*args, check=True):
    """`git -C ROOT <args>`'s stdout.

    A failure stops the run where CHECK is set and is empty otherwise."""
    run = subprocess.run(
        ["git", "-C", ROOT, *args], capture_output=True, text=True, encoding="utf-8"
    )
    if check and run.returncode != 0:
        raise SystemExit(f"git {' '.join(args)}: {run.stderr.strip()}")
    return run.stdout if run.returncode == 0 else ""


def last_tags(count=2):
    """The COUNT highest `v*` release tags, newest first; every one where
    COUNT is None.

    A tag that is not `vX.Y.Z` is skipped."""
    tags = [
        t
        for t in git("tag", "--sort=-v:refname").split("\n")
        if re.fullmatch(r"v\d+\.\d+\.\d+", t)
    ]
    return tags[:count]


def records(tags, items=None):
    """`{(item, n): text}` for every round record in the working tree and at
    TAGS, the tree read first and a tag's copy of the same round skipped.
    Where ITEMS is given, only the work items whose `<epoch>` prefix it
    names are read.

    A path outside the record shape is skipped."""

    def wanted(item):
        return items is None or item.split("-")[0] in items

    found = {}
    specs = os.path.join(ROOT, "seal", "specs")
    for item in sorted(os.listdir(specs)) if os.path.isdir(specs) else []:
        rounds = os.path.join(specs, item, "rounds")
        if not wanted(item) or not os.path.isdir(rounds):
            continue
        for name in sorted(os.listdir(rounds)):
            m = RECORD.fullmatch(f"seal/specs/{item}/rounds/{name}")
            if m:
                with open(os.path.join(rounds, name), encoding="utf-8") as f:
                    found[(item, int(m["n"]))] = f.read()
    for tag in tags:
        for path in git("ls-tree", "-r", "--name-only", tag, "seal/specs").split("\n"):
            m = RECORD.fullmatch(path)
            key = (m["item"], int(m["n"])) if m else None
            if key and wanted(key[0]) and key not in found:
                found[key] = git("show", f"{tag}:{path}")
    return found


def load_check(path, name):
    """The `chain_check.py` at PATH, imported as NAME.

    A script that will not load stops the run naming it."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"replay_targets: cannot load {path}")
    check = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(check)
    except Exception as exc:
        raise SystemExit(f"replay_targets: {path} will not load: {exc}") from None
    return check


@functools.cache
def record_reader():
    """`(chain_check, its shared reader)`, `chain_check.py` beside this tree,
    loaded once: the check and reader of a record no commit wrote
    (`checks_at`), and the reader `labelled` decides a record's shape
    with."""
    check = load_check(CHECK, "specseal_chain_check")
    return check, check.SHARED_READER


# What a commit's check needs beside it to load: the script, the reader it
# loads when imported, the hook module that reader takes its fence rule and
# line split from (#1005), and the document whose grammar table it reads. A
# file a commit does not hold is not copied: a check from before the table
# carries its grammar in its code, and a reader from before #1005 keeps its
# own fence rule.
CHECK_FILES = (
    "skills/code-review/scripts/chain_check.py",
    "skills/verify/scripts/unverified_check.py",
    "hooks/blocks.py",
    "docs/the-review-record.md",
)
CHECKS = {}


def written_at(rel, tags):
    """The commit that last wrote record REL: in the working tree's history
    where the tree holds it, else in the history of the first of TAGS that
    holds it, the order `records` reads them in. None where no commit wrote
    it, a record the tree has not committed among them.

    The last write and not the first, because a commit that rewrites a record
    into a renamed label's new spelling moves it to that commit's grammar on
    purpose, and the record is then judged by the grammar it was rewritten
    into (#985, the orchestrator's decision under the owner's automation
    answer)."""
    if os.path.isfile(os.path.join(ROOT, rel)):
        return git("log", "-1", "--format=%H", "--", rel, check=False).strip() or None
    for tag in tags:
        if git("ls-tree", "--name-only", tag, "--", rel, check=False).strip():
            return git("log", "-1", "--format=%H", tag, "--", rel).strip() or None
    return None


def checks_at(at):
    """`(chain_check, its reader)` as commit AT holds them, loaded from a
    copy of `CHECK_FILES` at AT, once for each set of their contents; this
    tree's where AT is None. The copies are removed when the run ends."""
    if at is None:
        return record_reader()
    blobs = tuple(
        git("rev-parse", "-q", "--verify", f"{at}:{rel}", check=False).strip()
        for rel in CHECK_FILES
    )
    if blobs not in CHECKS:
        held = tempfile.mkdtemp(prefix="specseal-replay-check-")
        atexit.register(shutil.rmtree, held, True)
        for rel, blob in zip(CHECK_FILES, blobs, strict=True):
            if blob:
                path = os.path.join(held, *rel.split("/"))
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(git("show", blob))
        name = f"specseal_chain_check_{blobs[0][:12]}_{len(CHECKS)}"
        check = load_check(os.path.join(held, *CHECK_FILES[0].split("/")), name)
        CHECKS[blobs] = (check, check.load(check.READER, f"{name}_reader"))
    return CHECKS[blobs]


def labelled(text):
    """True for a record in 0.22.0's labelled lines: one whose readable
    lines hold a `target:` line, which no table record carries.

    This tree's reader decides it, because the shape is decided before any
    check judges the record, and the check of a commit before 0.22.0 has no
    `target:` label to ask. A comment line begins with `<!--`, so a
    `target:` line inside a comment is one a comment's inner line opens
    with, and the round template carried none in any comment at any
    release tag before 0.22.0."""
    check, reader = record_reader()
    return any(
        check.label_of(line) == check.TARGET_ROW for line in reader.readable(text)
    )


def labelled_round(text, rel, n, at=None):
    """`(round, why)` for record N in labelled lines, judged by
    `chain_check.py#round_of` as commit AT holds it, the commit that wrote
    the record (`written_at`), or this tree's where AT is None: `round` is
    `{"sha", "value", "findings", "confirms"}` — the `target:` commit and
    the line's whole value, each finding as `(n, symptom, its location
    value, fixed or not)`, and the `(round, finding)` pairs its `confirms:`
    lines name.

    A record that check refuses is `(None, the first refusal)`, so a replay
    reads only what the pull request accepted, by the grammar it was
    accepted under.

    **Its lines are read by the reader that judged it**, AT's
    `unverified_check.py`, never by this tree's: a record at a release tag
    can carry a template comment,
    which the reader of its commit hid and this tree's reads as text since
    #1012, so a label-shaped line inside the comment would be read as the
    record's own."""
    judge, reader = checks_at(at)
    found, errors = judge.round_of(reader, text, rel, n)
    # The labels and the finding split are this tree's check's, which names
    # them the same way for every record it reads; a commit's check spells
    # its helpers as that commit did, and only its `round_of` is asked.
    check, _ = record_reader()
    if errors:
        _rel, line, why = errors[0]
        return None, f"the check refuses the record at line {line}: {why}"
    lines = reader.readable(text)
    value = next(
        check.value_of(x) for x in lines if check.label_of(x) == check.TARGET_ROW
    )
    _section, spans, _error = check.finding_spans(reader, lines)
    stops = {first + 1: stop for first, stop in spans}
    rows = []
    for f in found.findings:
        location = next(
            check.value_of(lines[i])
            for i in range(f.heading_line, stops[f.heading_line])
            if check.label_of(lines[i]) == check.LOCATION_ROW
        )
        symptom = f.heading.split(". ", 1)[1]
        rows.append((f.number, symptom, location, f.verdict[0] == check.FIXED))
    confirms = {reference for _line, reference in found.confirms}
    return {
        "sha": found.target,
        "value": value,
        "findings": rows,
        "confirms": confirms,
    }, ""


def cells(line):
    """The cells of one table row, `\\|` kept inside its cell.

    A line that is no row gives no cells."""
    if not line.startswith("|"):
        return []
    parts = re.split(r"(?<!\\)\|", line.strip())
    return [p.strip() for p in parts[1:-1]]


def field(text, name):
    """The value of the `| NAME | value |` row of a record's header table.

    No such row is None."""
    for line in text.split("\n"):
        row = cells(line)
        if len(row) == 2 and row[0] == name:
            return row[1]
    return None


def asked(text):
    """The `## What this round was asked` paragraph of a record.

    A record without the section gives an empty string."""
    m = re.search(
        r"^## What this round was asked\n(?P<body>.*?)(?=^## )", text, re.M | re.S
    )
    return m["body"].strip() if m else ""


def resolve(rev):
    """The full SHA REV names as a commit, or an empty string.

    A REV that does not resolve is an empty string."""
    return git("rev-parse", "--verify", "-q", f"{rev}^{{commit}}", check=False).strip()


def ref_base(target, ref, landed=None):
    """The merge-base of TARGET and REF, or an empty string. Where REF no
    longer resolves, a release branch deleted after its release, LANDED,
    the commit the work landed on, stands for it: a squash puts none of
    TARGET's commits on that branch, so the two share the fork REF named."""
    tip = ref if resolve(ref) else landed
    return git("merge-base", target, tip, check=False).strip() if tip else ""


def base_of(paragraph, target, landed=None):
    """`(base SHA, base ref or None)` the asked PARAGRAPH names for TARGET:
    `against <ref> at <sha>`, then a fix range `<a>..<b>`'s start, then
    `against <ref>` read as its merge-base with TARGET (`ref_base`, LANDED
    standing for a ref that no longer resolves); `("", None)` if none.

    A paragraph naming none of the three gives no base."""
    m = AGAINST_AT.search(paragraph)
    if m and resolve(m["base"]):
        return resolve(m["base"]), m["ref"]
    m = FIX_RANGE.search(paragraph)
    if m and resolve(m["base"]):
        return resolve(m["base"]), None
    m = AGAINST.search(paragraph)
    base = ref_base(target, m["ref"], landed) if m else ""
    if base:
        return base, m["ref"]
    return "", None


def target_base(value, target, landed=None):
    """`(base SHA, base ref or None)` a labelled record's `target:` VALUE
    names for TARGET: a fix range `<a>..<b>`'s start, an `against <sha>`
    commit, or `against <base>` read as the merge-base of TARGET and
    `origin/<base>` (`ref_base`, LANDED standing for a ref that no longer
    resolves); `("", None)` if none resolves."""
    m = FIX_RANGE.search(value)
    if m and resolve(m["base"]):
        return resolve(m["base"]), None
    _sha, _against, name = value.partition(" against ")
    if SHA.fullmatch(name) and resolve(name):
        return resolve(name), None
    ref = name if name.startswith("origin/") else f"origin/{name}"
    base = ref_base(target, ref, landed) if name else ""
    if base:
        return base, ref
    return "", None


def findings(text):
    """`[(marker, k, finding, location, verdict)]` for every numbered 🔴 and
    🟡 verdict row of a record.

    A row of another shape is skipped."""
    rows = []
    for line in text.split("\n"):
        row = cells(line)
        if len(row) >= 4:
            m = FINDING.fullmatch(row[0])
            if m:
                rows.append((m["marker"], int(m["k"]), row[1], row[2], row[3]))
    return rows


def confirmed(text, n, rel="the next round's record", at=None):
    """The finding numbers of round N a record confirms closed: its
    `confirms: round-<N>#<n>` lines where it is labelled, its 🟢 rows where
    it is a table.

    A line or row that names no round N finding confirms nothing, and a
    labelled record the check of AT refuses confirms nothing at all."""
    if labelled(text):
        read, _why = labelled_round(text, rel, n + 1, at)
        return {k for r, k in read["confirms"] if r == n} if read else set()
    done = set()
    for line in text.split("\n"):
        row = cells(line)
        if len(row) >= 4 and row[0] == "🟢" and row[3] == "confirmed":
            for m in CONFIRMS.finditer(row[1]):
                if int(m["n"]) == n:
                    done.add(int(m["k"]))
    return done


def enclosing(source, line):
    """`(names, (first, last))` of the innermost `def` or `class` holding LINE
    in Python SOURCE, outermost name first, or `([], None)`.

    A source that does not parse gives no unit."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return [], None
    best = ([], None)

    def walk(node, names):
        nonlocal best
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                span = (child.lineno, child.end_lineno)
                inner = [*names, child.name]
                if line is None or span[0] <= line <= span[1]:
                    best = (inner, span)
                walk(child, inner)

    walk(tree, [])
    return best


def unit_span(source, dotted):
    """`(first, last)` of the unit DOTTED names in Python SOURCE, or None.

    A unit not found gives None."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    node, want = tree, dotted.split(".")
    for name in want:
        node = next(
            (
                c
                for c in ast.iter_child_nodes(node)
                if isinstance(c, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
                and c.name == name
            ),
            None,
        )
        if node is None:
            return None
    return node.lineno, node.end_lineno


def truth_pattern(location, target):
    """The regex a report's finding's `location:` line must match to have
    found the finding at LOCATION, read at TARGET: its line within ±15, or
    the lines of the unit an old `path#unit` LOCATION names, within ±15.
    Where no line can be read, the path alone or with a line. Never a
    `path#unit`, which `chain_check.py` refuses in a `location:` line.

    A location naming no backticked path gives None."""
    option = truth_option(location, target)
    return None if option is None else f"{LOCATION_LINE}(?:{option})"


def truth_option(location, target, window=WINDOW):
    """`truth_pattern`'s alternative for LOCATION, without the `location:`
    line around it: a line within WINDOW of the one LOCATION names, or of
    its unit's span.

    A location naming no backticked path gives None."""
    m = LOCATION.search(location)
    if not m:
        return None
    path = m["path"]
    lines = None
    if m["line"]:
        line = int(m["line"])
        lines = (line - window, line + window)
    if m["unit"] and path.endswith(".py"):
        source = git("show", f"{target}:{path}", check=False)
        span = unit_span(source, m["unit"]) if source else None
        if span:
            lines = (span[0] - window, span[1] + window)
    if lines:
        return lines_option(path, *lines)
    return f"{behaviour.js_escape(path)}(?![\\w./#-])"


def lines_option(path, first, last):
    """The alternative for PATH at any line from FIRST to LAST, the line
    numbers before 1 dropped."""
    numbers = "|".join(str(n) for n in range(max(1, first), last + 1))
    return f"{behaviour.js_escape(path)}:(?:{numbers})(?!\\d)"


def recurred_truths():
    """`{case: [entry]}` from the input file at TRUTHS: the truths a run
    recurred on, each a new grader or an existing one widened. An entry is
    `case`, `grader` (`truth-<slug>`), `finding` (a new grader's body),
    `locations` (`path`, `path:line` or `path:first-last` at the case's
    target), `from` (the classing rows it came from), for a widening
    `widens: true`, and where ±15 lines would reach another truth of the
    case, `window`, the lines either side its locations accept.

    An entry naming a case the warden's suite does not hold stops the run
    with exit 1, so the file cannot outlive its cases silently."""
    with open(TRUTHS, encoding="utf-8") as f:
        entries = json.load(f)
    out = {}
    for e in entries:
        if not os.path.isdir(os.path.join(OUT, e["case"])):
            raise SystemExit(f"{TRUTHS}: an entry names {e['case']}, no case of {OUT}")
        out.setdefault(e["case"], []).append(e)
    return out


def truths_with(case, truths, target):
    """TRUTHS, the `[(name, pattern, body)]` a generator derived for CASE
    (NAME without its `truth-` prefix), with the input file's entries for
    CASE applied at TARGET: a widening adds each of its locations to the
    named truth's pattern as an alternative and keeps its body; a new truth
    is one more `(name, pattern, finding)`. A location's alternative accepts
    its line, or every line of its range, and the entry's `window` (15
    where it names none) either side.

    An entry widening a truth CASE does not have, adding one it already has,
    naming no location, a location outside `path`, `path:line` and
    `path:first-last`, a range that ends before it starts, or a window that
    is no count stops the run with exit 1."""
    out = list(truths)
    for e in recurred_truths().get(case, []):
        name = e["grader"].removeprefix("truth-")
        window = e.get("window", WINDOW)
        if type(window) is not int or window < 0:
            raise SystemExit(f"{case}: {e['grader']}'s window {window!r} is no count")
        options = []
        for location in e["locations"]:
            m = LOCATION.fullmatch(f"`{location}`")
            if not m or m["unit"]:
                raise SystemExit(
                    f"{case}: {e['grader']} names `{location}`, no coordinate"
                )
            last = re.search(r"[-\N{EN DASH}](\d+)$", location) if m["line"] else None
            if last:
                first = int(m["line"])
                if int(last[1]) < first:
                    raise SystemExit(
                        f"{case}: {e['grader']} names `{location}`, a range "
                        "that ends before it starts"
                    )
                options.append(
                    lines_option(m["path"], first - window, int(last[1]) + window)
                )
            else:
                options.append(truth_option(f"`{location}`", target, window))
        if not options:
            raise SystemExit(f"{case}: {e['grader']} names no location")
        names = [n for n, _pattern, _body in out]
        if e.get("widens"):
            if name not in names:
                raise SystemExit(f"{case}: no {e['grader']} to widen")
            i = names.index(name)
            _n, pattern, body = out[i]
            if not pattern.startswith(LOCATION_LINE):
                raise SystemExit(f"{case}: {e['grader']} reads no `location:` line")
            rest = pattern[len(LOCATION_LINE) :]
            out[i] = (name, f"{LOCATION_LINE}(?:{rest}|{'|'.join(options)})", body)
        elif name in names:
            raise SystemExit(f"{case}: {e['grader']} is already a truth of the case")
        else:
            out.append((name, f"{LOCATION_LINE}(?:{'|'.join(options)})", e["finding"]))
    return out


def round_target(item, n, text, nxt, wrote, replay=True, landed=None):
    """`(target, "")` for round N of ITEM, or `(None, why)`. TEXT is the
    round's record and NXT the next round's, or None where there is none.
    WROTE maps a record's path to the commit whose check judges it: the
    commit that wrote it (`written_at`), or None for this tree's check.
    LANDED is the commit the work landed on, where the caller knows it
    (`ref_base`). A target is `{"item", "n", "target", "base", "base_ref",
    "branch", "asked", "truths", "size"}`, its truths each finding the
    round closed `fixed` that the next round confirms, as `{"k", "finding",
    "location", "pattern"}`.

    A round whose SHAs or branch do not resolve, or a labelled record the
    check of the commit that wrote it refuses, is left out with the reason.
    Where REPLAY is set, so is a round with no next round or with no
    truth; `seed_defects.py` builds on a round with neither."""
    rel = f"seal/specs/{item}/rounds/round-{n}.md"
    if labelled(text):
        read, why = labelled_round(text, rel, n, wrote(rel))
        if read is None:
            return None, why
        sha, para, label = read["sha"], "", "target"
        rows = read["findings"]
    else:
        sha = field(text, "Target SHA") or ""
        sha, para, label = sha.split()[0] if sha else "", asked(text), "Target SHA"
        rows = [(k, f, at, "fixed" in v) for _m, k, f, at, v in findings(text)]
    if not sha or not resolve(sha):
        return None, f"{label} {sha or '(none)'} does not resolve"
    if nxt is None and replay:
        return None, "no next round to confirm a fix"
    if labelled(text):
        base, base_ref = target_base(read["value"], sha, landed)
        names = "the target line"
    else:
        base, base_ref = base_of(para, sha, landed)
        names = "the asked paragraph"
    if not base:
        return None, f"{names} names no base that resolves"
    routing = git("show", f"{sha}:seal/specs/{item}/routing.md", check=False)
    branch = field(routing, "Branch")
    if not branch:
        return None, "routing.md at the target names no branch"
    following = f"seal/specs/{item}/rounds/round-{n + 1}.md"
    done = set() if nxt is None else confirmed(nxt, n, following, wrote(following))
    truths = []
    for k, finding, location, fixed in rows:
        if fixed and k in done:
            pattern = truth_pattern(location, sha)
            if pattern:
                truths.append(
                    {
                        "k": k,
                        "finding": finding,
                        "location": location,
                        "pattern": pattern,
                    }
                )
    if not truths and replay:
        return None, "no fixed finding the next round confirmed"
    stat = git("diff", "--shortstat", base, sha)
    size = sum(int(x) for x in re.findall(r"(\d+) (?:insertion|deletion)", stat))
    return {
        "item": item,
        "n": n,
        "target": git("rev-parse", sha).strip(),
        "base": base,
        "base_ref": base_ref,
        "branch": branch,
        "asked": para,
        "truths": truths,
        "size": size,
    }, ""


def targets(tags, items=None):
    """`[target]` for every round with truth, and `[(item, n, why)]` for each
    round left out, over the records `records` reads at TAGS for ITEMS, each
    judged by `round_target`."""
    found = records(tags, items)
    kept, left = [], []
    for (item, n), text in sorted(found.items()):
        t, why = round_target(
            item,
            n,
            text,
            found.get((item, n + 1)),
            lambda rel: written_at(rel, tags),
        )
        if t is None:
            left.append((item, n, why))
        else:
            kept.append(t)
    return kept, left


def origin_url():
    """The `origin` remote as an https URL a scaffold can fetch from.

    A URL of another shape stops the run."""
    url = git("remote", "get-url", "origin").strip()
    m = re.fullmatch(
        r"(?:git@github\.com:|https://github\.com/)(?P<repo>[\w.-]+/[\w.-]+?)(?:\.git)?",
        url,
    )
    if not m:
        raise SystemExit(f"origin {url!r} is not a GitHub remote a scaffold can fetch")
    return f"https://github.com/{m['repo']}.git"


def prompt(t):
    """The case prompt: the orchestrator's one spawn, then the report read
    back so the run's trace holds it. The round's asked paragraph ends the
    spawn where its record carried one, and nothing does where it did not."""
    report = f"seal/specs/{t['item']}/rounds/round-{t['n']}.md"
    base = f"`{t['base_ref']}` at `{t['base']}`" if t["base_ref"] else f"`{t['base']}`"
    asked = " ".join(t["asked"].split())
    asked = f" {asked}" if asked else ""
    return f"""You are the review orchestrator of this repository. Spawn exactly one `agentic:proofer` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Review, edit and commit nothing yourself. When it returns, run `cat {report}` once and reply with the report's path.

BEGIN PROMPT

Review round {t["n"]} of work item `{t["item"]}`. The clone is the current directory, on branch `{t["branch"]}` at `{t["target"]}`; the base is {base}. Write the report to `{report}` and return its path.{asked}

END PROMPT"""


def scaffold(t, url):
    """The scaffold: the target and its base fetched, the branch checked out,
    and the base ref the asked paragraph names."""
    lines = [
        "git init -q .",
        f"git remote add origin {url}",
        f"git fetch -q --no-tags origin {t['target']}",
        f"git fetch -q --no-tags origin {t['base']}",
    ]
    if t["base_ref"]:
        ref = t["base_ref"].removeprefix("origin/")
        lines.append(f"git update-ref refs/remotes/origin/{ref} {t['base']}")
    lines.append(f"git checkout -q -b {t['branch']} {t['target']}")
    return "\n".join(lines)


def graders(t):
    """Reach, shape and truth graders for one target."""
    report = f"seal/specs/{t['item']}/rounds/round-{t['n']}.md"
    own = [
        (
            f"{truth['k']}",
            truth["pattern"],
            f"Round {t['n']}'s finding {truth['k']}: {truth['finding']}",
        )
        for truth in t["truths"]
    ]
    out = behaviour.report_shape("proofer", report)
    for name, pattern, body in truths_with(case_name(t), own, t["target"]):
        out.append(behaviour.report_regex("truth", name, report, pattern, body))
    return out


def case_name(t):
    """The case's directory and display name."""
    return f"replay-{t['item'].split('-')[0]}-r{t['n']}"


def main(argv=None):
    """Parse the arguments, then list or write. `--case` reads its work
    items' records at every release tag; the rest reads the last two.

    An unusable argument is argparse's exit 2."""
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--list", action="store_true")
    p.add_argument("--count", type=int, default=4)
    p.add_argument("--case", action="append", default=[])
    p.add_argument("--out", default=OUT)
    p.add_argument("--model", default=MODEL)
    p.add_argument("--timeout", type=int, default=2400)
    a = p.parse_args(argv)
    if a.case:
        items = {name.removeprefix("replay-").rsplit("-r", 1)[0] for name in a.case}
        kept, left = targets(last_tags(None), items)
    else:
        kept, left = targets(last_tags())
    if a.list:
        for t in sorted(kept, key=lambda t: t["size"]):
            print(f"{t['item']} r{t['n']}  {len(t['truths'])} truth  {t['size']} lines")
        for item, n, why in left:
            print(f"{item} r{n}  left out: {why}")
        return 0
    chosen, items = [], set()
    for t in sorted(kept, key=lambda t: (t["size"], t["item"], t["n"])):
        if t["item"] not in items:
            chosen.append(t)
            items.add(t["item"])
        if len(chosen) == a.count:
            break
    if a.case:
        chosen = [t for t in kept if case_name(t) in a.case]
        a.count = len(a.case)
    url = origin_url()
    for t in chosen:
        name = case_name(t)
        behaviour.write_case(
            os.path.join(a.out, name),
            name=f"proofer {name}",
            tags=["behaviour", "proofer", "replay"],
            prompt=prompt(t),
            scaffold=scaffold(t, url),
            graders=graders(t),
            max_turns=12,
            timeout_seconds=a.timeout,
            model=a.model,
        )
        print(f"{name}: {len(t['truths'])} truth, {t['size']} lines")
    return 0 if len(chosen) == a.count else 1


if __name__ == "__main__":
    sys.exit(main())
