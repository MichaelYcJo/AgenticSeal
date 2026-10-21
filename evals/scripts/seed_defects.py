#!/usr/bin/env python3
"""Generate the warden's seeded cases from the last release's shipped diffs.

A seeded case is the tree a shipped work item's round 1 reviewed, with one
mutation in it. For a squash commit the release branch shipped, the
generator reads the item's `rounds/round-1.md` at that commit, through
`replay_targets.py#round_target` for either record shape, and builds the
case at round 1's target against round 1's base. No round record exists in
that tree, and every branch commit its files name is an ancestor of the
target. The mutation lands on a line `base..target` added inside a Python
unit, and it is amended into the target commit with the target's own
committer and date. The scaffold then removes the remote, writing the base
ref round 1 names again, expires the reflog, removes `FETCH_HEAD` and
prunes what nothing reaches. So the target's original commit neither
resolves in the clone nor is named by any file under its `.git/` outside
the objects, and a `git fetch` with no URL has no remote to fetch from. A
fetch that names the repository's URL, which tracked files of the tree
hold, still reaches the shipped code.

Its truths are the mutated line, a `truth-` grader over the record's
`location:` lines for `path:<line>` within 15 lines of it either way, and
each finding round 1 closed `fixed` that round 2 confirms, by the replay
rule, since the tree at round 1's target holds the defects round 1 found.
The seed lands on no line the window of such a finding accepts. A real
defect that runs recurred on is a truth of the case too, where
`recurred_truths.json` adds it (`replay_targets.py#truths_with`). The
operators are `mutation-check`'s vocabulary, a replacement that lands
exactly once in the file.

A case keeps the name `seeded-<the squash commit's first 8 hex>`, which
names the shipped item and no object its clone holds.

Usage:
  seed_defects.py --list                 every shipped commit and the
                                         mutation it would carry
  seed_defects.py --count 4 [--out DIR]  write the COUNT smallest under DIR
                                         (evals/behaviour/warden/)
  seed_defects.py --case NAME [--out DIR]
                                         write the named case alone
                                         (`seeded-<commit[:8]>`), from any
                                         release's shipped commits;
                                         repeatable

Exit codes: 0 written or listed · 1 fewer cases than --count, or a named
case no release shipped · 2 the arguments were unusable.
"""

import argparse
import io
import itertools
import os
import re
import shlex
import sys
import tokenize

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import behaviour
import replay_targets as rt

OUT = rt.OUT
OPERATORS = (
    (" == ", " != "),
    (" != ", " == "),
    (" <= ", " < "),
    (" >= ", " > "),
    (" < ", " <= "),
    (" > ", " >= "),
    (" and ", " or "),
    (" or ", " and "),
    ("return True", "return False"),
    ("return False", "return True"),
    (" + 1", " + 2"),
    (" - 1", " - 2"),
    ("if not ", "if "),
)
TOKEN = {
    " == ": "==",
    " != ": "!=",
    " <= ": "<=",
    " >= ": ">=",
    " < ": "<",
    " > ": ">",
    " and ": "and",
    " or ": "or",
    "return True": "True",
    "return False": "False",
    " + 1": "+",
    " - 1": "-",
    "if not ": "not",
}
SPEC = re.compile(r"^seal/specs/(?P<item>[^/]+)/")
SUBJECT = re.compile(r"\(#\d+\)$")


def shipped(tags):
    """The first-parent commits of each release branch between consecutive
    TAGS (newest first), newest first.

    A release branch is its release merge's second parent."""
    found = []
    for newest, older in itertools.pairwise(tags):
        log = rt.git(
            "log", "--first-parent", "--format=%H", f"{older}..{newest}^2", check=False
        )
        found += [c for c in log.split("\n") if c]
    return found


def added_lines(base, target, path):
    """The line numbers at TARGET of the lines `base..target` added in
    PATH."""
    out = rt.git("diff", "-U0", base, target, "--", path)
    lines = set()
    for m in re.finditer(
        r"^@@ -\S+ \+(?P<start>\d+)(?:,(?P<count>\d+))? @@", out, re.M
    ):
        start, count = int(m["start"]), int(m["count"] or 1)
        lines.update(range(start, start + count))
    return lines


def code_tokens(source):
    """`{(line, token)}` for every operator and name token of Python SOURCE,
    so an operator inside a string or a comment is never a seed.

    A source that does not tokenize gives no tokens."""
    found = set()
    try:
        for tok in tokenize.generate_tokens(io.StringIO(source).readline):
            if tok.type in (tokenize.OP, tokenize.NAME):
                found.add((tok.start[0], tok.string))
    except (tokenize.TokenError, SyntaxError):
        return set()
    return found


def seed(base, target, truths=()):
    """The first mutation for `base..target`: `(path, line, old, new,
    names)`, or None.

    A file is a non-test `.py` the range changed; a line is one it added
    inside a `def` or `class` whose text occurs once in the file, and whose
    `location:` window no regex of TRUTHS accepts on any line; the operator
    is the first that lands once on that line. OLD and NEW are the whole
    line before and after."""
    accepts = [re.compile(p, re.M) for p in truths]
    names = rt.git("diff", "--name-only", base, target).split("\n")
    for path in sorted(
        n for n in names if n.endswith(".py") and not n.startswith("tests/")
    ):
        source = rt.git("show", f"{target}:{path}", check=False)
        if not source:
            continue
        code = code_tokens(source)
        lines = source.split("\n")
        for line in sorted(added_lines(base, target, path)):
            if line > len(lines):
                continue
            unit, _span = rt.enclosing(source, line)
            if not unit:
                continue
            text = lines[line - 1]
            if source.count(text) != 1:
                continue
            window = range(line - rt.WINDOW, line + rt.WINDOW + 1)
            if any(
                a.search(f"location: `{path}:{n}`") for a in accepts for n in window
            ):
                continue
            for old, new in OPERATORS:
                if text.count(old) == 1 and (line, TOKEN[old]) in code:
                    return path, line, text, text.replace(old, new), unit
    return None


def target_of(commit):
    """`(target, "")` for the shipped squash COMMIT, or `(None, why)`: round
    1 of the one work item whose `routing.md` the commit adds, read at the
    commit by `replay_targets.py#round_target` with round 2 confirming its
    fixes, and the seed `seed` finds in round 1's `base..target`. A labelled
    record is judged by the check of the commit that last wrote it in
    COMMIT's history, and COMMIT's first parent, the release branch the item
    landed on, stands for a base ref round 1 names that no longer resolves.

    A commit that is no squashed pull request, adds no work item or two,
    holds no round 1 record, whose round 1 `round_target` leaves out, two
    of whose round 1 truths accept one `location:` line (`shared_line`), or
    whose range takes no seed is left out with the reason."""
    subject = rt.git("log", "-1", "--format=%s", commit).strip()
    if not SUBJECT.search(subject):
        return None, "not a squashed pull request"
    added = rt.git("diff", "--name-only", "--diff-filter=A", f"{commit}^1", commit)
    items = sorted(
        m["item"]
        for n in added.split("\n")
        if (m := SPEC.match(n)) and n.endswith("/routing.md")
    )
    if len(items) != 1:
        return None, f"adds {len(items)} work items' routing.md"
    item = items[0]
    rounds = f"{commit}:seal/specs/{item}/rounds"
    first = rt.git("show", f"{rounds}/round-1.md", check=False)
    if not first:
        return None, "holds no round 1 record"
    second = rt.git("show", f"{rounds}/round-2.md", check=False) or None

    def wrote(rel):
        return rt.git("log", "-1", "--format=%H", commit, "--", rel).strip() or None

    landed = rt.git("rev-parse", f"{commit}^1").strip()
    t, why = rt.round_target(item, 1, first, second, wrote, False, landed)
    if t is None:
        return None, f"round 1: {why}"
    patterns = [truth["pattern"] for truth in t["truths"]]
    row = shared_line(patterns, [truth["location"] for truth in t["truths"]])
    if row:
        return None, f"two of round 1's truths accept `{row}`"
    found = seed(t["base"], t["target"], patterns)
    if not found:
        return None, "no added line in a Python unit takes an operator"
    path, line, old, new, unit = found
    return dict(
        t,
        commit=commit,
        subject=subject,
        path=path,
        line=line,
        old=old,
        new=new,
        unit=".".join(unit),
        pattern=rt.truth_pattern(f"`{path}:{line}`", t["target"]),
    ), ""


def shared_line(patterns, locations):
    """A `location:` line two of PATTERNS accept, or None. The lines tried
    name each path LOCATIONS name, bare and at every line from 1 to twice
    the window past the highest line any of them names, which covers every
    line a truth's window can reach."""
    accepts = [re.compile(p, re.M) for p in patterns]
    found = [m for value in locations for m in rt.LOCATION.finditer(value)]
    top = max([int(m["line"]) for m in found if m["line"]] or [0])
    for path in sorted({m["path"] for m in found}):
        for n in [None, *range(1, top + 2 * rt.WINDOW + 2)]:
            row = f"location: `{path}`" if n is None else f"location: `{path}:{n}`"
            if sum(1 for a in accepts if a.search(row)) > 1:
                return row
    return None


def targets(tags, prefixes=None):
    """`[target]` for every shipped commit `target_of` builds a case on, and
    `[(commit, why)]` for each left out; where PREFIXES is given, only the
    commits whose first eight digits it names."""
    kept, left = [], []
    for commit in shipped(tags):
        if prefixes is not None and commit[:8] not in prefixes:
            continue
        t, why = target_of(commit)
        if t is None:
            left.append((commit, why))
        else:
            kept.append(t)
    return kept, left


MUTATE = """python3 - {path} {line} {old} {new} <<'PY'
import sys
path, line, old, new = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
with open(path, encoding="utf-8", newline="") as f:
    lines = f.read().split("\\n")
assert lines[line - 1] == old, f"{{path}}:{{line}} is not {{old!r}}"
lines[line - 1] = new
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write("\\n".join(lines))
PY"""


def scaffold(t, url):
    """The scaffold: round 1's target checked out as the replay scaffold
    does it (`replay_targets.py#scaffold`), the mutation amended into the
    target commit with the target's own committer and date, so no field of
    the log marks the seed's commit. Then the remote goes (the module
    docstring says what that closes and what it leaves), and the base ref
    round 1 names is written again, since removing the remote removes it.
    Last the reflog is
    expired, `FETCH_HEAD` removed and what nothing reaches pruned, so no
    copy of the target's original commit is left."""
    mutate = MUTATE.format(
        path=shlex.quote(t["path"]),
        line=t["line"],
        old=shlex.quote(t["old"]),
        new=shlex.quote(t["new"]),
    )
    head = rt.scaffold(t, url)
    refs = [line for line in head.split("\n") if line.startswith("git update-ref ")]
    return "\n".join(
        [
            head,
            mutate,
            'GIT_COMMITTER_NAME="$(git log -1 --format=%cn)" '
            'GIT_COMMITTER_EMAIL="$(git log -1 --format=%ce)" '
            'GIT_COMMITTER_DATE="$(git log -1 --format=%cI)" '
            "git -c user.name=eval -c user.email=eval@example.com commit -q -a --amend --no-edit --no-verify",
            "git remote remove origin",
            *refs,
            "git reflog expire --expire=now --all",
            "rm -f .git/FETCH_HEAD",
            "git gc -q --prune=now",
        ]
    )


def prompt(t):
    """The case prompt: the orchestrator's one spawn of a fresh round 1, at
    HEAD against round 1's base."""
    report = f"seal/specs/{t['item']}/rounds/round-1.md"
    return f"""You are the review orchestrator of this repository. Spawn exactly one `specseal:warden` agent through the Agent tool. Its prompt is the whole paragraph between the `BEGIN PROMPT` and `END PROMPT` lines, copied verbatim with nothing dropped. Review, edit and commit nothing yourself. When it returns, run `cat {report}` once and reply with the report's path.

BEGIN PROMPT

Review round 1 of work item `{t["item"]}`. The clone is the current directory, on branch `{t["branch"]}` at HEAD; the base is `{t["base"]}`, so the diff is `{t["base"][:8]}..HEAD`. Write the report to `{report}` and return its path. This round reviews the whole build — {t["subject"]} — for spec compliance first, then quality.

END PROMPT"""


def case_name(t):
    """The case's directory name."""
    return f"seeded-{t['commit'][:8]}"


def graders(t):
    """Reach, shape and truth graders for one seeded case: the seeded line,
    each finding round 1 closed fixed that round 2 confirmed, and whatever
    the input file of recurred truths adds for the case at round 1's
    target."""
    report = f"seal/specs/{t['item']}/rounds/round-1.md"
    seeded = (
        "seeded",
        t["pattern"],
        f"The seeded defect: {t['old'].strip()!r} made {t['new'].strip()!r} in `{t['path']}#{t['unit']}`.",
    )
    found = [
        (
            f"{truth['k']}",
            truth["pattern"],
            f"Round 1's finding {truth['k']}: {truth['finding']}",
        )
        for truth in t["truths"]
    ]
    out = behaviour.report_shape("warden", report)
    for name, pattern, body in rt.truths_with(
        case_name(t), [seeded, *found], t["target"]
    ):
        out.append(behaviour.report_regex("truth", name, report, pattern, body))
    return out


def main(argv=None):
    """Parse the arguments, then list or write. `--case` reads every release
    tag's shipped commits; the rest reads the last three tags'.

    An unusable argument is argparse's exit 2."""
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--list", action="store_true")
    p.add_argument("--count", type=int, default=4)
    p.add_argument("--case", action="append", default=[])
    p.add_argument("--out", default=OUT)
    p.add_argument("--model", default=rt.MODEL)
    p.add_argument("--timeout", type=int, default=2400)
    a = p.parse_args(argv)
    if a.case:
        prefixes = {name.removeprefix("seeded-") for name in a.case}
        kept, left = targets(rt.last_tags(None), prefixes)
    else:
        kept, left = targets(rt.last_tags(3))
    if a.list:
        for t in sorted(kept, key=lambda t: t["size"]):
            print(
                f"{t['commit'][:8]} {t['path']}:{t['line']} {t['old'].strip()!r} -> {t['new'].strip()!r}  {t['size']} lines"
            )
        for commit, why in left:
            print(f"{commit[:8]} left out: {why}")
        return 0
    chosen = sorted(kept, key=lambda t: (t["size"], t["commit"]))[: a.count]
    if a.case:
        chosen = [t for t in kept if case_name(t) in a.case]
        a.count = len(a.case)
    url = rt.origin_url()
    for t in chosen:
        behaviour.write_case(
            os.path.join(a.out, case_name(t)),
            name=f"warden {case_name(t)}",
            tags=["behaviour", "warden", "seeded"],
            prompt=prompt(t),
            scaffold=scaffold(t, url),
            graders=graders(t),
            max_turns=12,
            timeout_seconds=a.timeout,
            model=a.model,
        )
        print(f"{case_name(t)}: {t['path']}#{t['unit']}, {t['size']} lines")
    return 0 if len(chosen) == a.count else 1


if __name__ == "__main__":
    sys.exit(main())
