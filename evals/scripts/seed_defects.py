#!/usr/bin/env python3
"""Generate the warden's seeded cases from the last release's shipped diffs.

A seeded case is a squash commit the release branch shipped, rebuilt in the
scaffold clone as one commit on its first parent with one mutation applied
to a line the diff added inside a Python unit, and the work item's
`rounds/` taken out so no earlier verdict is inherited. Its truth is the
mutated line: a `truth-` grader over the report's `location:` lines for
`path:<line>` within ±15 of it. The operators are `mutation-check`'s vocabulary, a
replacement that lands exactly once in the file.

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


def added_lines(commit, path):
    """The line numbers at COMMIT of the lines its diff to its first parent
    added in PATH."""
    out = rt.git("diff", "-U0", f"{commit}^1", commit, "--", path)
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


def seed(commit):
    """The first mutation for COMMIT: `(path, line, old, new, names)`, or None.

    A file is a non-test `.py` the commit changed; a line is one it added
    inside a `def` or `class` whose text occurs once in the file; the
    operator is the first that lands once on that line. OLD and NEW are the
    whole line before and after."""
    names = rt.git("diff", "--name-only", f"{commit}^1", commit).split("\n")
    for path in sorted(
        n for n in names if n.endswith(".py") and not n.startswith("tests/")
    ):
        source = rt.git("show", f"{commit}:{path}", check=False)
        if not source:
            continue
        code = code_tokens(source)
        lines = source.split("\n")
        for line in sorted(added_lines(commit, path)):
            if line > len(lines):
                continue
            unit, _span = rt.enclosing(source, line)
            if not unit:
                continue
            text = lines[line - 1]
            if source.count(text) != 1:
                continue
            for old, new in OPERATORS:
                if text.count(old) == 1 and (line, TOKEN[old]) in code:
                    return path, line, text, text.replace(old, new), unit
    return None


def targets(tags, prefixes=None):
    """`[target]` for every shipped commit a seed lands in, and
    `[(commit, why)]` for each left out; where PREFIXES is given, only the
    commits whose first eight digits it names."""
    kept, left = [], []
    for commit in shipped(tags):
        if prefixes is not None and commit[:8] not in prefixes:
            continue
        subject = rt.git("log", "-1", "--format=%s", commit).strip()
        if not SUBJECT.search(subject):
            left.append((commit, "not a squashed pull request"))
            continue
        added = rt.git("diff", "--name-only", "--diff-filter=A", f"{commit}^1", commit)
        items = sorted(
            m["item"]
            for n in added.split("\n")
            if (m := SPEC.match(n)) and n.endswith("/routing.md")
        )
        if len(items) != 1:
            left.append((commit, f"adds {len(items)} work items' routing.md"))
            continue
        item = items[0]
        branch = rt.field(
            rt.git("show", f"{commit}:seal/specs/{item}/routing.md", check=False),
            "Branch",
        )
        if not branch:
            left.append((commit, "routing.md names no branch"))
            continue
        found = seed(commit)
        if not found:
            left.append((commit, "no added line in a Python unit takes an operator"))
            continue
        path, line, old, new, unit = found
        stat = rt.git(
            "diff",
            "--shortstat",
            f"{commit}^1",
            commit,
            "--",
            ".",
            f":!seal/specs/{item}/rounds",
        )
        size = sum(int(x) for x in re.findall(r"(\d+) (?:insertion|deletion)", stat))
        base = rt.git("rev-parse", f"{commit}^1").strip()
        kept.append(
            {
                "commit": commit,
                "subject": subject,
                "item": item,
                "branch": branch,
                "base": base,
                "path": path,
                "line": line,
                "old": old,
                "new": new,
                "unit": ".".join(unit),
                "pattern": rt.truth_pattern(f"`{path}:{line}`", commit),
                "size": size,
            }
        )
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
    """The scaffold: the shipped commit fetched, the mutation applied, the
    work item's rounds removed, all amended into one commit on its parent."""
    mutate = MUTATE.format(
        path=shlex.quote(t["path"]),
        line=t["line"],
        old=shlex.quote(t["old"]),
        new=shlex.quote(t["new"]),
    )
    return "\n".join(
        [
            "git init -q .",
            f"git remote add origin {url}",
            f"git fetch -q --no-tags origin {t['commit']}",
            f"git checkout -q -b {t['branch']} {t['commit']}",
            mutate,
            f"git rm -rq --ignore-unmatch seal/specs/{t['item']}/rounds",
            "git -c user.name=eval -c user.email=eval@example.com commit -q -a --amend --no-edit --no-verify",
        ]
    )


def prompt(t):
    """The case prompt: the orchestrator's one spawn of a fresh round 1."""
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
    and whatever the input file of recurred truths adds for the case."""
    report = f"seal/specs/{t['item']}/rounds/round-1.md"
    seeded = (
        "seeded",
        t["pattern"],
        f"The seeded defect: {t['old'].strip()!r} made {t['new'].strip()!r} in `{t['path']}#{t['unit']}`.",
    )
    out = behaviour.report_shape("warden", report)
    for name, pattern, body in rt.truths_with(case_name(t), [seeded], t["commit"]):
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
