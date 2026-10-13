#!/usr/bin/env python3
"""budget_check — every budget `seal/budgets.md` names, measured from the tree
and held to its ceiling from both sides.

  budget_check.py                      measure each row, hold it to its band
  budget_check.py --baseline REF       also hold each ceiling to the one
                                       `seal/budgets.md` states at
                                       `git merge-base REF HEAD`
  budget_check.py --pr-body-env VAR    the pull request body, from the
                                       environment variable VAR
  budget_check.py --base-ref BRANCH    the branch the pull request merges
                                       into; `main` is a release
  budget_check.py --root DIR           a tree other than this script's own

**The band.** A row holds while `measured <= ceiling <= measured x (1 +
slack)`, or `measured + slack` where the slack is absolute (`+N`). The left
inequality is the ceiling. The right one is what records a cleanup: a change
that drops the measurement below the band fails until the same pull request
lowers the ceiling, so the next change starts from the new number rather than
from the old headroom.

**The ratchet.** With `--baseline`, a `gate` row whose ceiling is higher here
than at the merge base, or one that is gone or is no longer a gate, fails
unless the pull request body carries one line for it:

  Budget raised: <name> <old> -> <new>: <reason>
  Budget removed: <name>: <reason>

The numbers in a raise are the two ceilings exactly, so a line written for an
earlier raise does not cover a later one. The line may sit in a list item and
the name may be in backticks. A row that is new needs no line, and neither
does a lower ceiling. Against `--base-ref main` no line is asked for: a
release carries every work item's rows, and each work item carried its own
line at its own pull request. The ceiling still holds there.

**Kind.** A `gate` row fails the run; a `report` row is measured and printed
beside the gates and never fails it.

**The summary** is a table, one line per budget — measured, ceiling, headroom,
kind, verdict — and the raises the ratchet read. It goes to
`$GITHUB_STEP_SUMMARY` where the runner sets one and to stdout otherwise, and
it names no path on the machine that ran it. What failed is printed to stdout
either way.

Exit codes: **0** every gate row holds · **1** a gate row is over its ceiling,
under its band, or raised or removed with no line for it, each named · **2**
nothing was compared: `seal/budgets.md` is missing or a row of it cannot be
read, a row names a budget no measurer here reads, the baseline does not
resolve, `--pr-body-env` names a variable that is not set, or a sibling module
this reads through is not beside it. Closed, never silent.
"""

import argparse
import collections
import fractions
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

BUDGETS = os.path.join("seal", "budgets.md")
BUDGETS_GIT = "seal/budgets.md"
HEADER = ("Budget", "Unit", "Ceiling", "Slack", "Kind")
KINDS = ("gate", "report")
GATE = "gate"
RELEASE_BRANCH = "main"
# What the summary says of a raise or a removal the body declares nothing for.
UNDECLARED = "**not declared** — the pull request body carries no line for it"

# The modules this reads through, each the one reader of its input: the table
# walker every `seal/` table is read by (#871), the meter the preload budgets
# are measured with, and the merge base `unverified_check.py` resolves.
SIBLINGS = {
    "config": (
        os.path.join("hooks", "config.py"),
        "it is the one reader of a `seal/` table",
    ),
    "payload_meter": (
        os.path.join("skills", "verify", "scripts", "payload_meter.py"),
        "it is what measures an agent's preload",
    ),
    "unverified_check": (
        os.path.join("skills", "verify", "scripts", "unverified_check.py"),
        "it is what resolves the merge base",
    ),
}

Row = collections.namedtuple("Row", "line name unit ceiling slack kind")
Slack = collections.namedtuple("Slack", "amount absolute text")
Result = collections.namedtuple("Result", "row measured top problems")

NAME = re.compile(r"[a-z][a-z0-9-]*(?::\S+)?")
CEILING = re.compile(r"[0-9]+")
RELATIVE_SLACK = re.compile(r"([0-9]+(?:\.[0-9]+)?)[ \t]*%")
ABSOLUTE_SLACK = re.compile(r"\+[ \t]*([0-9]+)(?:[ \t]+(\S+))?")

# One declaration per line of the body. A list marker in front and backticks
# around the name are what a person writes in markdown, and both are read.
_LEAD = r"(?:[-*+][ \t]+)?"
_NAME_CELL = r"`?(?P<name>[^\s`]+)`?"
RAISED = re.compile(
    _LEAD + r"Budget raised:[ \t]*" + _NAME_CELL + r"[ \t]+(?P<old>[0-9]+)[ \t]*->"
    r"[ \t]*(?P<new>[0-9]+)[ \t]*:[ \t]*(?P<reason>\S.*)"
)
REMOVED = re.compile(
    _LEAD + r"Budget removed:[ \t]*" + _NAME_CELL + r"[ \t]*:[ \t]+(?P<reason>\S.*)"
)


class Unreadable(Exception):
    """Nothing could be compared, and the sentence says why.

    Reads: nothing — an exception carrying the sentence its raiser wrote"""


_loaded = {}


def sibling(key):
    """The module `SIBLINGS[key]` names, loaded by path once, or Unreadable.

    Reads: owned — a module this repository ships beside this script; unknown refused"""
    if key in _loaded:
        return _loaded[key]
    rel, purpose = SIBLINGS[key]
    path = os.path.join(ROOT, rel)
    if not os.path.isfile(path):
        raise Unreadable(f"cannot read {rel}, and {purpose}")
    spec = importlib.util.spec_from_file_location(f"specseal_budget_{key}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    _loaded[key] = module
    return module


def parse_slack(cell, unit):
    """The `Slack` a cell states: `N %` relative, `+N` absolute in the row's
    unit, which it may name after the number.

    Reads: owned — a Slack cell of `seal/budgets.md`, in the vocabulary this module defines; unknown refused"""
    text = cell.strip()
    relative = RELATIVE_SLACK.fullmatch(text)
    if relative:
        return Slack(fractions.Fraction(relative.group(1)) / 100, False, text)
    absolute = ABSOLUTE_SLACK.fullmatch(text)
    if absolute and absolute.group(2) in (None, unit):
        return Slack(int(absolute.group(1)), True, text)
    raise ValueError(f"`{cell}` is no slack: write `N %` or `+N`")


def parse_budgets(text, where):
    """Every row of the `| Budget | Unit | Ceiling | Slack | Kind |` table in
    `text`, or Unreadable naming the row and `where` it stands.

    Reads: guess — a person's markdown table, through `hooks/config.py#gfm_table`; unknown refused"""
    rows, refusals = sibling("config").gfm_table(text, HEADER)
    if refusals:
        raise Unreadable(f"{where} {refusals[0]}")
    out, seen = [], set()
    for line, cells in rows:
        name, unit, ceiling, slack, kind = (c.strip().strip("`") for c in cells)
        at = f"{where}, line {line}"
        if not NAME.fullmatch(name):
            raise Unreadable(f"{at}: `{name}` is no budget name")
        if name in seen:
            raise Unreadable(f"{at}: `{name}` is written twice")
        seen.add(name)
        if not CEILING.fullmatch(ceiling):
            raise Unreadable(
                f"{at}: {name}'s ceiling `{ceiling}` is not a whole number "
                "written in digits alone"
            )
        try:
            parsed = parse_slack(slack, unit)
        except ValueError as error:
            raise Unreadable(f"{at}: {name}'s {error}") from None
        if kind not in KINDS:
            raise Unreadable(f"{at}: {name}'s kind `{kind}` is neither gate nor report")
        out.append(Row(line, name, unit, int(ceiling), parsed, kind))
    return out


def budgets_here(root):
    """The rows of `seal/budgets.md` in the tree at `root`.

    Reads: guess — the file a person edits, through `parse_budgets`; unknown refused"""
    path = os.path.join(root, BUDGETS)
    if not os.path.isfile(path):
        raise Unreadable(f"{BUDGETS_GIT} is not in the tree, so no budget was read")
    with open(path, encoding="utf-8", errors="replace") as handle:
        return parse_budgets(handle.read(), BUDGETS_GIT)


def budgets_at(root, ref):
    """`(label, rows)` for `seal/budgets.md` at `git merge-base REF HEAD`:
    no rows where the file was not there yet, Unreadable where the base does
    not resolve.

    Reads: observed — git's merge base and the blob it holds, parsed by `parse_budgets`; unknown refused"""
    base = sibling("unverified_check").merge_base(root, ref)
    if base is None:
        raise Unreadable(
            f"the baseline `{ref}` gives no merge base with HEAD — it does not "
            "resolve here, or shares no history with it — so no ceiling was "
            "compared with the one before"
        )
    label = f"the merge base of {ref} and HEAD ({base[:7]})"

    def git(*args):
        return subprocess.run(
            ["git", "-C", root, *args],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )

    listed = git("ls-tree", "--name-only", base, "--", BUDGETS_GIT)
    if listed.returncode != 0:
        raise Unreadable(f"git could not list {BUDGETS_GIT} at {label}")
    if not listed.stdout.strip():
        return label, []
    shown = git("show", f"{base}:{BUDGETS_GIT}")
    if shown.returncode != 0:
        raise Unreadable(f"git could not read {BUDGETS_GIT} at {label}")
    return label, parse_budgets(shown.stdout, f"{BUDGETS_GIT} at {label}")


def measure_preload(root, agent):
    """Bytes of `agents/<agent>.md` and of each `SKILL.md` its `skills:` list
    names, the agent's own share of `payload_meter`'s rows — never the
    `CLAUDE.md` pair, which is the harness's and half of it is not in the tree.

    Reads: owned — an agent definition's frontmatter and the files it names, through `payload_meter`; unknown refused"""
    meter = sibling("payload_meter")
    found = meter.agents_in(root, (agent,))
    if agent not in found:
        raise Unreadable(
            f"preload:{agent}: no agents/*.md under the tree is named {agent}"
        )
    rows = meter.composition(root, root, agent, found[agent], False)
    own = [row for row in rows if row["share"] == "agent"]
    missing = [row["path"] for row in own if row.get("missing")]
    if missing:
        raise Unreadable(
            f"preload:{agent}: {', '.join(missing)}, which {found[agent]} "
            "names, is not in the tree"
        )
    return sum(row["bytes"] for row in own)


# A budget's name is `<family>` or `<family>:<subject>`; the family picks the
# measurer and the unit the row must state.
MEASURERS = {"preload": (measure_preload, "bytes")}


def measure(root, row):
    """What `row` measures in the tree at `root`, in the row's unit.

    Reads: owned — the row's family, in the vocabulary `MEASURERS` defines; unknown refused"""
    family, _, subject = row.name.partition(":")
    if family not in MEASURERS or not subject:
        raise Unreadable(
            f"{row.name}: no measurer here reads a budget of that name — the "
            f"families are {', '.join(f'`{f}:<subject>`' for f in MEASURERS)}"
        )
    measurer, unit = MEASURERS[family]
    if row.unit != unit:
        raise Unreadable(
            f"{row.name}: the unit is `{row.unit}`, and {family} is measured in {unit}"
        )
    return measurer(root, subject)


def top_of_band(measured, slack):
    """The highest ceiling `measured` allows under `slack`.

    Reads: nothing — a number from the numbers handed to it"""
    if slack.absolute:
        return measured + slack.amount
    return int(measured * (1 + slack.amount))


def band(row, measured):
    """`Result` for one row: what is wrong with its ceiling against
    `measured`, from both sides.

    Reads: nothing — compares the numbers handed to it"""
    top = top_of_band(measured, row.slack)
    problems = []
    if measured > row.ceiling:
        problems.append(
            f"measured {measured:,} {row.unit} is over the ceiling {row.ceiling:,} "
            f"by {measured - row.ceiling:,}. Bring it back under, or raise the "
            f"ceiling in {BUDGETS_GIT} and write `Budget raised: {row.name} "
            f"{row.ceiling} -> <new>: <reason>` in the pull request body"
        )
    elif row.ceiling > top:
        problems.append(
            f"the ceiling {row.ceiling:,} sits above the band: measured "
            f"{measured:,} {row.unit} at {row.slack.text} slack allows at most "
            f"{top:,}. Lower the ceiling in {BUDGETS_GIT} to {measured} — "
            f"anything from {measured} to {top} holds"
        )
    return Result(row, measured, top, problems)


def declarations(body):
    """`(raised, removed)` the body declares: `raised` maps a name to its
    `(old, new, reason)` lines, `removed` a name to its reasons.

    Reads: guess — a person's pull request body, one line at a time; unknown refused"""
    raised, removed = collections.defaultdict(list), collections.defaultdict(list)
    for line in body.splitlines():
        text = line.strip()
        up = RAISED.fullmatch(text)
        if up:
            raised[up["name"]].append((int(up["old"]), int(up["new"]), up["reason"]))
            continue
        gone = REMOVED.fullmatch(text)
        if gone:
            removed[gone["name"]].append(gone["reason"])
    return raised, removed


def ratchet(base_rows, head_rows, body, release):
    """`(problems, moves)`: each gate row raised or removed since the base
    with no line for it, and every raise or removal read, as `(name, what,
    reason)` for the summary.

    Reads: guess — a pull request body its caller handed it, through `declarations`; unknown refused"""
    raised, removed = declarations(body)
    head = {row.name: row for row in head_rows}
    problems, moves = [], []
    for old in base_rows:
        if old.kind != GATE:
            continue
        new = head.get(old.name)
        if new is not None and new.kind == GATE:
            if new.ceiling <= old.ceiling:
                continue
            what = f"raised {old.ceiling} -> {new.ceiling}"
            lines = raised.get(old.name, [])
            match = [r for o, n, r in lines if (o, n) == (old.ceiling, new.ceiling)]
            if match or release:
                moves.append((old.name, what, match[0] if match else "at a release"))
                continue
            moves.append((old.name, what, UNDECLARED))
            wrote = "".join(f" The body's line says {o} -> {n}." for o, n, _ in lines)
            problems.append(
                (
                    old.name,
                    f"the ceiling was raised from {old.ceiling} to {new.ceiling} and "
                    f"the pull request body declares no such raise.{wrote} Write "
                    f"`Budget raised: {old.name} {old.ceiling} -> {new.ceiling}: "
                    "<reason>` in the body",
                )
            )
            continue
        what = "removed" if new is None else f"no longer a gate ({new.kind})"
        reasons = removed.get(old.name, [])
        if reasons or release:
            moves.append((old.name, what, reasons[0] if reasons else "at a release"))
            continue
        moves.append((old.name, what, UNDECLARED))
        problems.append(
            (
                old.name,
                f"the gate row was {what} and the pull request body declares no "
                f"removal. Write `Budget removed: {old.name}: <reason>` in the body",
            )
        )
    return problems, moves


def render(results, moves, against):
    """The summary as markdown: one line per budget, then the raises read.

    Reads: nothing — formats the results handed to it"""
    lines = [
        "### Budgets",
        "",
        f"From `{BUDGETS_GIT}`; the ratchet read {against}.",
        "",
        "| Budget | Measured | Ceiling | Headroom | Kind | Verdict |",
        "|---|---|---|---|---|---|",
    ]
    for result in results:
        row = result.row
        room = row.ceiling - result.measured
        share = f"{room / row.ceiling:.1%}" if row.ceiling else "—"
        verdict = "holds" if not result.problems else "over" if room < 0 else "lower it"
        lines.append(
            f"| `{row.name}` | {result.measured:,} {row.unit} | {row.ceiling:,} | "
            f"{room:,} ({share}) | {row.kind} | {verdict} |"
        )
    if moves:
        lines += ["", "Ceilings moved since the base:", ""]
        lines += [f"- `{name}` {what}: {reason}" for name, what, reason in moves]
    return "\n".join(lines) + "\n"


def write_summary(text, env):
    """Append `text` to the step summary the runner names, else print it.

    Reads: observed — the `GITHUB_STEP_SUMMARY` path the runner set; unknown passed"""
    path = env.get("GITHUB_STEP_SUMMARY")
    if path:
        with open(path, "a", encoding="utf-8") as handle:
            handle.write(text)
    else:
        sys.stdout.write(text)


def check(root, baseline=None, body="", release=False):
    """`(problems, refusals, summary)` for the tree at `root`.

    Reads: guess — `seal/budgets.md` and the body its caller handed it, through the units above; unknown refused"""
    head = budgets_here(root)
    results, refusals = [], []
    for row in head:
        try:
            results.append(band(row, measure(root, row)))
        except Unreadable as error:
            refusals.append(str(error))
    problems = [
        (r.row.name, p) for r in results if r.row.kind == GATE for p in r.problems
    ]
    moves, against = [], "no baseline"
    if baseline is not None:
        against, base_rows = budgets_at(root, baseline)
        found, moves = ratchet(base_rows, head, body, release)
        problems += found
    return problems, refusals, render(results, moves, against)


def main(argv=None, env=None):
    """Measure, compare, print; the exit code is the verdict.

    Reads: guess — the arguments, the environment and the pull request body in it; unknown refused"""
    env = os.environ if env is None else env
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=ROOT)
    parser.add_argument("--baseline", metavar="REF")
    parser.add_argument("--pr-body-env", metavar="VAR")
    parser.add_argument("--base-ref", metavar="BRANCH", default="")
    args = parser.parse_args(argv)
    try:
        body = ""
        if args.pr_body_env:
            if args.pr_body_env not in env:
                raise Unreadable(
                    f"--pr-body-env names {args.pr_body_env}, which is not set: "
                    "a step that read no body must not be green"
                )
            body = env[args.pr_body_env]
        problems, refusals, summary = check(
            os.path.abspath(args.root),
            baseline=args.baseline,
            body=body,
            release=args.base_ref == RELEASE_BRANCH,
        )
    except Unreadable as error:
        sys.stderr.write(f"budget-check: {error}. Nothing was compared.\n")
        return 2
    write_summary(summary, env)
    for refusal in refusals:
        sys.stderr.write(f"budget-check: {refusal}.\n")
    for name, problem in problems:
        print(f"budget-check: {name}: {problem}.")
    if refusals:
        return 2
    if problems:
        return 1
    print("budget-check: every gate row holds.")
    return 0


if __name__ == "__main__":
    for _name in ("stdout", "stderr"):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    sys.exit(main())
