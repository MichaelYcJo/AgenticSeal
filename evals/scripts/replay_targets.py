#!/usr/bin/env python3
"""Generate the warden's replay cases from round records.

A replay case is a historical review target: the clone at the commit a
round record reviewed (its `Target SHA` row, in the records these targets
come from), the base its `## What this round was asked` paragraph names,
and that paragraph as the round's spawn prompt. Its truth is every finding
the round closed `fixed` that the next round confirmed closed — there a
numbered red or yellow row, and a green row naming it; each is a `truth-`
grader over the `location:` lines of the round record the warden writes
today. Round records come
from the working tree and from the last two release tags
(`git show <tag>:seal/specs/<id>/rounds/round-N.md`).

Usage:
  replay_targets.py --list                 every round with truth, and why
                                           a round with none was left out
  replay_targets.py --count 4 [--out DIR]  write the COUNT smallest targets,
                                           one per work item, under DIR
                                           (evals/behaviour/warden/)
  replay_targets.py --case NAME [--out DIR]
                                           write the named case alone, as
                                           `--list` shows it (`replay-<id>-rN`);
                                           repeatable

Exit codes: 0 written or listed · 1 fewer targets than --count, or a
named case not on the list · 2 the arguments were unusable.
"""

import argparse
import ast
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import behaviour

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "evals", "behaviour", "warden")
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


def git(*args, check=True):
    """`git -C ROOT <args>`'s stdout.

    A failure stops the run where CHECK is set and is empty otherwise.

    Reads: observed — git's stdout for the arguments given; unknown mixed"""
    run = subprocess.run(
        ["git", "-C", ROOT, *args], capture_output=True, text=True, encoding="utf-8"
    )
    if check and run.returncode != 0:
        raise SystemExit(f"git {' '.join(args)}: {run.stderr.strip()}")
    return run.stdout if run.returncode == 0 else ""


def last_tags(count=2):
    """The COUNT highest `v*` release tags.

    A tag that is not `vX.Y.Z` is skipped.

    Reads: observed — `git tag --sort=-v:refname`; unknown passed"""
    tags = [
        t
        for t in git("tag", "--sort=-v:refname").split("\n")
        if re.fullmatch(r"v\d+\.\d+\.\d+", t)
    ]
    return tags[:count]


def records(tags):
    """`{(item, n): text}` for every round record in the working tree and at
    TAGS, the tree read first and a tag's copy of the same round skipped.

    A path outside the record shape is skipped.

    Reads: observed — round records under ROOT and at each tag; unknown passed"""
    found = {}
    specs = os.path.join(ROOT, "seal", "specs")
    for item in sorted(os.listdir(specs)) if os.path.isdir(specs) else []:
        rounds = os.path.join(specs, item, "rounds")
        for name in sorted(os.listdir(rounds)) if os.path.isdir(rounds) else []:
            m = RECORD.fullmatch(f"seal/specs/{item}/rounds/{name}")
            if m:
                with open(os.path.join(rounds, name), encoding="utf-8") as f:
                    found[(item, int(m["n"]))] = f.read()
    for tag in tags:
        for path in git("ls-tree", "-r", "--name-only", tag, "seal/specs").split("\n"):
            m = RECORD.fullmatch(path)
            if m and (m["item"], int(m["n"])) not in found:
                found[(m["item"], int(m["n"]))] = git("show", f"{tag}:{path}")
    return found


def cells(line):
    """The cells of one table row, `\\|` kept inside its cell.

    A line that is no row gives no cells.

    Reads: guess — a line it is handed, split at every unescaped `|`; unknown passed"""
    if not line.startswith("|"):
        return []
    parts = re.split(r"(?<!\\)\|", line.strip())
    return [p.strip() for p in parts[1:-1]]


def field(text, name):
    """The value of the `| NAME | value |` row of a record's header table.

    No such row is None.

    Reads: guess — the record text it is handed; unknown passed"""
    for line in text.split("\n"):
        row = cells(line)
        if len(row) == 2 and row[0] == name:
            return row[1]
    return None


def asked(text):
    """The `## What this round was asked` paragraph of a record.

    A record without the section gives an empty string.

    Reads: guess — the record text it is handed, up to the next `## `; unknown passed"""
    m = re.search(
        r"^## What this round was asked\n(?P<body>.*?)(?=^## )", text, re.M | re.S
    )
    return m["body"].strip() if m else ""


def resolve(rev):
    """The full SHA REV names as a commit, or an empty string.

    A REV that does not resolve is an empty string.

    Reads: observed — `git rev-parse --verify`; unknown passed"""
    return git("rev-parse", "--verify", "-q", f"{rev}^{{commit}}", check=False).strip()


def base_of(paragraph, target):
    """`(base SHA, base ref or None)` the asked PARAGRAPH names for TARGET:
    `against <ref> at <sha>`, then a fix range `<a>..<b>`'s start, then
    `against <ref>` read as its merge-base with TARGET; `("", None)` if none.

    A paragraph naming none of the three gives no base.

    Reads: guess — the paragraph it is handed, and git for each name; unknown passed"""
    m = AGAINST_AT.search(paragraph)
    if m and resolve(m["base"]):
        return resolve(m["base"]), m["ref"]
    m = FIX_RANGE.search(paragraph)
    if m and resolve(m["base"]):
        return resolve(m["base"]), None
    m = AGAINST.search(paragraph)
    if m and resolve(m["ref"]):
        base = git("merge-base", target, m["ref"], check=False).strip()
        if base:
            return base, m["ref"]
    return "", None


def findings(text):
    """`[(marker, k, finding, location, verdict)]` for every numbered 🔴 and
    🟡 verdict row of a record.

    A row of another shape is skipped.

    Reads: guess — the record text it is handed; unknown passed"""
    rows = []
    for line in text.split("\n"):
        row = cells(line)
        if len(row) >= 4:
            m = FINDING.fullmatch(row[0])
            if m:
                rows.append((m["marker"], int(m["k"]), row[1], row[2], row[3]))
    return rows


def confirmed(text, n):
    """The finding numbers of round N a record's 🟢 rows confirm closed.

    A 🟢 row that names no round N finding confirms nothing.

    Reads: guess — the record text it is handed; unknown passed"""
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

    A source that does not parse gives no unit.

    Reads: guess — the source text it is handed, through `ast`; unknown passed"""
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

    A unit not found gives None.

    Reads: guess — the source text it is handed, through `ast`; unknown passed"""
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

    A location naming no backticked path gives None.

    Reads: observed — `git show TARGET:<path>` for a Python path; unknown passed"""
    m = LOCATION.search(location)
    if not m:
        return None
    path = m["path"]
    lines = None
    if m["line"]:
        line = int(m["line"])
        lines = (line - WINDOW, line + WINDOW)
    if m["unit"] and path.endswith(".py"):
        source = git("show", f"{target}:{path}", check=False)
        span = unit_span(source, m["unit"]) if source else None
        if span:
            lines = (span[0] - WINDOW, span[1] + WINDOW)
    if lines:
        numbers = "|".join(str(n) for n in range(max(1, lines[0]), lines[1] + 1))
        option = f"{behaviour.js_escape(path)}:(?:{numbers})(?!\\d)"
    else:
        option = f"{behaviour.js_escape(path)}(?![\\w./#-])"
    return "^location: .*(?:" + option + ")"


def targets(tags):
    """`[target]` for every round with truth, and `[(item, n, why)]` for each
    round left out.

    A round whose SHAs or branch do not resolve is left out with the reason.

    Reads: observed — the records `records` returns, and git per SHA; unknown passed"""
    found = records(tags)
    kept, left = [], []
    for (item, n), text in sorted(found.items()):
        sha = field(text, "Target SHA") or ""
        sha = sha.split()[0] if sha else ""
        nxt = found.get((item, n + 1))
        if not sha or not resolve(sha):
            left.append((item, n, f"Target SHA {sha or '(none)'} does not resolve"))
            continue
        if nxt is None:
            left.append((item, n, "no next round to confirm a fix"))
            continue
        para = asked(text)
        base, base_ref = base_of(para, sha)
        if not base:
            left.append((item, n, "the asked paragraph names no base that resolves"))
            continue
        routing = git("show", f"{sha}:seal/specs/{item}/routing.md", check=False)
        branch = field(routing, "Branch")
        if not branch:
            left.append((item, n, "routing.md at the target names no branch"))
            continue
        done = confirmed(nxt, n)
        truths = []
        for marker, k, finding, location, verdict in findings(text):
            if "fixed" in verdict and k in done:
                pattern = truth_pattern(location, sha)
                if pattern:
                    truths.append(
                        {
                            "k": k,
                            "marker": marker,
                            "finding": finding,
                            "pattern": pattern,
                        }
                    )
        if not truths:
            left.append((item, n, "no fixed finding the next round confirmed"))
            continue
        stat = git("diff", "--shortstat", base, sha)
        size = sum(int(x) for x in re.findall(r"(\d+) (?:insertion|deletion)", stat))
        kept.append(
            {
                "item": item,
                "n": n,
                "target": git("rev-parse", sha).strip(),
                "base": base,
                "base_ref": base_ref,
                "branch": branch,
                "asked": para,
                "truths": truths,
                "size": size,
            }
        )
    return kept, left


def origin_url():
    """The `origin` remote as an https URL a scaffold can fetch from.

    A URL of another shape stops the run.

    Reads: observed — `git remote get-url origin`; unknown refused"""
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
    back so the run's trace holds it.

    Reads: nothing — it formats the target it is handed."""
    report = f"seal/specs/{t['item']}/rounds/round-{t['n']}.md"
    base = f"`{t['base_ref']}` at `{t['base']}`" if t["base_ref"] else f"`{t['base']}`"
    asked = " ".join(t["asked"].split())
    return f"""You are the review orchestrator of this repository. Spawn exactly one `specseal:warden` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Review, edit and commit nothing yourself. When it returns, run `cat {report}` once and reply with the report's path.

BEGIN PROMPT

Review round {t["n"]} of work item `{t["item"]}`. The clone is the current directory, on branch `{t["branch"]}` at `{t["target"]}`; the base is {base}. Write the report to `{report}` and return its path. {asked}

END PROMPT"""


def scaffold(t, url):
    """The scaffold: the target and its base fetched, the branch checked out,
    and the base ref the asked paragraph names.

    Reads: nothing — it formats the target it is handed."""
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
    """Reach, shape and truth graders for one target.

    Reads: nothing — it formats the target it is handed."""
    report = f"seal/specs/{t['item']}/rounds/round-{t['n']}.md"
    out = behaviour.report_shape("warden", report)
    for truth in t["truths"]:
        out.append(
            behaviour.report_regex(
                "truth",
                f"{truth['k']}",
                report,
                truth["pattern"],
                f"Round {t['n']}'s finding {truth['k']}: {truth['finding']}",
            )
        )
    return out


def case_name(t):
    """The case's directory and display name.

    Reads: nothing — it formats the target it is handed."""
    return f"replay-{t['item'].split('-')[0]}-r{t['n']}"


def main(argv=None):
    """Parse the arguments, then list or write.

    An unusable argument is argparse's exit 2.

    Reads: owned — its own argument vector; unknown refused"""
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--list", action="store_true")
    p.add_argument("--count", type=int, default=4)
    p.add_argument("--case", action="append", default=[])
    p.add_argument("--out", default=OUT)
    p.add_argument("--model", default=MODEL)
    p.add_argument("--timeout", type=int, default=2400)
    a = p.parse_args(argv)
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
            name=f"warden {name}",
            tags=["behaviour", "warden", "replay"],
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
