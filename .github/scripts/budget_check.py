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
  budget_check.py --ci-jobs FILE       the rows read off one CI run, and only
                                       those, from its job list, one JSON
                                       object a line
  budget_check.py --trend TAG          also set each budget beside its
                                       ceiling at TAG, one line each

**The band.** A row holds while `measured <= ceiling <= measured x (1 +
slack)`, or `measured + slack` where the slack is absolute (`+N`). The left
inequality is the ceiling. The right one is what records a cleanup: a change
that drops the measurement below the band fails until the same pull request
lowers the ceiling, so the next change starts from the new number rather than
from the old headroom.

**The ratchet.** With `--baseline`, a `gate` row whose ceiling is higher here
than at the merge base, or whose slack is wider (`one-sided` the widest), or
one that is gone or is no longer a gate, fails unless the pull request body
carries one line for it:

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

**The families.** A budget's name is `<family>` or `<family>:<subject>`:

  preload:<agent>   bytes of `agents/<agent>.md` and each `SKILL.md` its
                    `skills:` list names, never the `CLAUDE.md` pair
  preload:claude-md bytes of `CLAUDE.md`
  suite-seconds     seconds summed over `.test_durations`, rounded
  slow-file         seconds of one test file in `.test_durations`
  docs-history      history lines of one `docs/*.md` file
  ci-minutes:<leg>  minutes of one tests run, summed over the leg's pytest
                    jobs: `ubuntu`, `windows` or `macos`
  rounds-bytes      bytes of the largest `seal/specs/<id>/rounds/` in the
                    tree, each work item's listed in the summary
  enforced-unresolved  `Enforced by:` targets in the rule files that do not
                    resolve, each named with its file, heading and why
  unenforced        rule paragraphs of one rule file whose `Enforced by:`
                    line is missing or says `nothing — <why>`

`rounds-bytes` is a `report` row: its number is the review chain's and every
work item's together, so no pull request has a fix for it, and a `report`
row may be `one-sided` for that reason.

**A rule is held by what its `Enforced by:` line names.** The rule files are
`CLAUDE.md`, `CONTRIBUTING.md`, `agents/*.md`, `docs/*.md`,
`skills/*/SKILL.md`, `skills/*/orchestration.md` and `templates/*.md`. A
**rule paragraph** opens a block with `**`, `- **`, `* **` or `N. **`, outside
fences and comments, and closes after its `Enforced by:` line, at a blank
line, a heading, a table or the next list item. A target is a file, a
`path::name` unit as pytest spells a node id, or an eval case directory
`evals/behaviour/<agent>/<case>/` holding a `case.yaml`; every target but the
last resolves through `skills/settle/scripts/fold_check.py#target_problem`,
the one resolver `fold-check` reads with. `enforced-unresolved` reads every
`Enforced by:` line of those files, inside a rule paragraph or not.
`unenforced` counts `nothing — <why>` as unenforced, so the escape moves the
number. What neither reads: whether a target runs on every leg, whether it
asserts the rule, and a rule written as a plain sentence. A name its module
defines twice does not resolve, because it names no one unit.

A byte is counted with each CRLF read as one LF, which is what git stores
for these files: a Windows checkout that wrote CRLF measures the commit a
Linux one does.

**A row read off one run is one-sided.** One run's minutes swing 1.08 to 1.21
times from the next on the same code, and three of five quiet runs fell
under a two-sided band on one leg, so a `ci-minutes` row's slack is
`one-sided`: it holds while the run is under its ceiling, and nothing asks
for it to be lowered. The seconds rows are the same kind of reading:
`.test_durations` is one run's union, and one refresh moved each of its 19
test files of 100 seconds or more 0.76 to 1.14 times the level it moved the
whole by (its 72 files of 10 seconds or more, 0.46 to 1.54), so `suite-seconds` and
`slow-file` are `one-sided` too. Such a row's ceiling is 1.3 times its
reading, rounded up, which holds that spread with room, and the release
lowers it from the trend line. Only these rows and `report` rows may say
`one-sided`. The tree's run
shows the minutes rows unread; the tests workflow's `budgets` job, after the
suite, reads the run's job list with `--ci-jobs` and holds them, and prints
the billable line: each job's minutes rounded up, at its leg's multiple of a
Linux minute, priced at the figure #929 read, whose date nobody here has
checked.

`slow-file`, `docs-history` and `unenforced` are measured per file. The
family's own row in the Budgets
table gives the unit, the slack and the kind, and its ceiling is what every
file its table does not list is held to: `## Slow test files` (`| File |
Seconds ceiling |`), `## Docs history lines` (`| File | Lines ceiling |`) and
`## Unenforced rules` (`| File | Rules ceiling |`) list the files held to a
ceiling of their own. So an unlisted test file over
the threshold fails, and listing it is a raise from the threshold that needs
its line, as is a row the table drops whose ceiling was under it. Every test
file whose reading times 1.3 reaches the threshold is listed, so an unlisted
one has the same room to move before it crosses. A docs
line is a **history line** when it is not a rule line, not blank, not hidden
in a fence or a comment and not a heading, and matches `#NN`, `round N`, a
date or `measured`. A **rule line** is in a block from a line opening with
`**` to the next `Enforced by:` line, or to the end of its paragraph where no
such line closes it first. It errs both ways: a rule's grounds citing an
issue outside its paragraph count as history, and a narrative line with none
of the marks does not.

**The seconds rows are held to composition, not to the runners' speed.**
Every refresh of `.test_durations` prices the suite on a different set of
runners, and one measured refresh priced the same cases 1.07 times higher.
So the seconds ceilings are written in one set of prices, and `## Price
level` (`| Prices | Per mille |`, one row for `.test_durations`, 1000 where
the table is absent) states how the committed file's prices stand against
them. `suite-seconds` and every `slow-file` reading are the file's seconds
divided by that level, and the summary prints the raw value beside it. With
`--baseline`, the file's move is measured over the case ids both files hold,
as the median over the test files of 10 seconds or more of each file's
seconds here over its seconds there, and the level here must be the base's
times that ratio, rounded per mille, or the run fails naming the number to
write. A median of files moves with the runners and not with one file, so a
cleanup that speeds one file up moves only that file's reading. So a refresh restates
one number and no `Budget raised:` line, the level cannot move without the
file, and a later pull request reads the refreshed file at the level its
refresh wrote. A uniform rescale holds every row; cases added, cases removed
and one file growing against the rest move them. A file the base did not
have is a ratio of 1, and two files sharing no case id, or no test file of 10
seconds on the shared ids, is exit 2. A suite that is slower everywhere is what
the per-run CI minutes measure.

**The summary** is a table, one line per budget — measured, ceiling, headroom,
kind, verdict — and the raises the ratchet read. It goes to
`$GITHUB_STEP_SUMMARY` where the runner sets one and to stdout otherwise, and
it names no path on the machine that ran it. What failed is printed to stdout
either way.

Exit codes: **0** every gate row holds · **1** a gate row is over its ceiling,
under its band, or raised or removed with no line for it, each named · **2**
nothing was compared: `seal/budgets.md` is missing or a row of it cannot be
read, a row names a budget no measurer here reads or a file the tree does
not have, a family row and its file table are not both there, `CLAUDE.md` or
`.test_durations` is missing or unreadable, the baseline does not resolve,
`--pr-body-env` names a variable that is not set, the job list is missing or
unreadable or has no pytest job on a leg a row names, an `Enforced by:`
target names a Python file that will not parse, or a sibling module this
reads through is not beside it. Closed, never silent.
"""

import argparse
import collections
import datetime
import fractions
import glob
import importlib.util
import json
import math
import os
import re
import statistics
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

BUDGETS = os.path.join("seal", "budgets.md")
BUDGETS_GIT = "seal/budgets.md"
HEADER = ("Budget", "Unit", "Ceiling", "Slack", "Kind")
KINDS = ("gate", "report")
GATE = "gate"
REPORT = "report"
RELEASE_BRANCH = "main"
# What the summary says of a raise or a removal the body declares nothing for.
UNDECLARED = "**not declared** — the pull request body carries no line for it"

CLAUDE_MD = "claude-md"
DURATIONS = ".test_durations"
# The families read from `.test_durations`, compared in the prices their
# ceilings are written in, and the table stating how the file's prices stand
# against those, per mille.
PRICED = ("suite-seconds", "slow-file")
# A test file the base prices at fewer seconds than this is too noisy to say
# how the runners moved, and is left out of the price level's median.
PRICE_FILE_FLOOR = 10
PRICE_TITLE = "Price level"
PRICE_HEADER = ("Prices", "Per mille")
PER_MILLE = 1000
DOCS = "docs"
HISTORY = re.compile(r"#\d{2,}|round \d|20\d\d-\d\d-\d\d|[Mm]easured")
RULE_OPENER = "**"
RULE_CLOSER = "Enforced by:"
# Where a rule is stated, read by `rule_paragraphs` and `enforcer_lines`.
RULE_FILES = (
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "agents/*.md",
    "docs/*.md",
    "skills/*/SKILL.md",
    "skills/*/orchestration.md",
    "templates/*.md",
)
# A line opening a rule paragraph, and a line opening any list item: up to
# three spaces, then `**`, or a list marker and `**`.
LIST_MARKER = r"[ ]{0,3}(?:[-*+]|[0-9]+[.)])[ \t]+"
RULE_PARAGRAPH = re.compile(rf"(?:{LIST_MARKER}|[ ]{{0,3}})\*{{2,3}}[^*\s]")
LIST_ITEM = re.compile(r"[ \t]*(?:[-*+]|[0-9]+[.)])[ \t]+")
# The one target `fold_check.py#target_problem` does not read: an eval case,
# `evals/behaviour/<agent>/<case>/`, which resolves where this file is in it.
EVAL_CASES = "evals/behaviour/"
EVAL_CASE = "case.yaml"
# The families read off one CI run rather than off the tree: measured by the
# `budgets` job of the tests workflow from the run's job list, held to a
# ceiling and no lower band.
PER_RUN = ("ci-minutes",)
ONE_SIDED = "one-sided"
# A leg is the operating system a `pytest (<os>-latest, …)` job's name opens
# with, and each leg's minute is billed at a multiple of a Linux minute.
PYTEST_JOB = re.compile(r"pytest \(([a-z]+)-[^,)]*(?:,.*)?\)")
BILLING = {"ubuntu": 1, "windows": 2, "macos": 10}
LINUX_MINUTE_USD = 0.008
# A byte budget counts a CRLF as the LF git stores, so the same commit
# measures the same on a checkout that converted its line ends.
NEWLINES = (b"\r\n", b"\n")
# Why a row is shown and not measured on a run, by family.
UNREAD = {
    "ci-minutes": "read off each run by the tests workflow's `budgets` job",
}

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
    "fold_check": (
        os.path.join("skills", "settle", "scripts", "fold_check.py"),
        "it is the one resolver of an `Enforced by:` target",
    ),
}

Row = collections.namedtuple("Row", "line name unit ceiling slack kind")
Slack = collections.namedtuple("Slack", "amount absolute text")
Result = collections.namedtuple("Result", "row measured top problems")
# A per-file family: its table's heading and header, its unit, the reader
# that measures its files, what a file it lists must be in, and what the lines
# its reader keeps in `cache["at"][<family>]` are called where a file is over.
FileFamily = collections.namedtuple(
    "FileFamily",
    "title header unit reader source noun",
    defaults=(f"{DOCS}/", "history lines"),
)
# One rule paragraph: the line it opens on, the heading it stands under, its
# first line, and its `Enforced by:` value, or None where it carries none.
Paragraph = collections.namedtuple("Paragraph", "line heading first enforced")

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
    unit, which it may name after the number, or `one-sided`, no lower band.

    Reads: owned — a Slack cell of `seal/budgets.md`, in the vocabulary this module defines; unknown refused"""
    text = cell.strip()
    if text == ONE_SIDED:
        return Slack(None, False, text)
    relative = RELATIVE_SLACK.fullmatch(text)
    if relative:
        return Slack(fractions.Fraction(relative.group(1)) / 100, False, text)
    absolute = ABSOLUTE_SLACK.fullmatch(text)
    if absolute and absolute.group(2) in (None, unit):
        return Slack(int(absolute.group(1)), True, text)
    raise ValueError(f"`{cell}` is no slack: write `N %` or `+N`")


def parse_budgets(text, where):
    """Every row of the `| Budget | Unit | Ceiling | Slack | Kind |` table in
    `text`, then every file row of the per-file tables as `<family>:<file>`
    with its family's unit, slack and kind, or Unreadable naming the row and
    `where` it stands.

    Reads: guess — a person's markdown tables, through `hooks/config.py#gfm_table`; unknown refused"""
    config = sibling("config")
    rows, refusals = config.gfm_table(text, HEADER)
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
        family = name.partition(":")[0]
        one_run = family in PER_RUN or family in PRICED
        one_sided = parsed.amount is None
        if one_run and not one_sided:
            raise Unreadable(
                f"{at}: {name}'s slack is `{slack}`, and a row read off one run "
                f"— a CI run's minutes, or `{DURATIONS}`, one run's union — is "
                f"`{ONE_SIDED}`: one run's prices swing too far for a lower band"
            )
        if one_sided and not one_run and kind != REPORT:
            raise Unreadable(
                f"{at}: {name}'s slack is `{slack}`, and only a row read off "
                f"one run or a `{REPORT}` row is `{ONE_SIDED}`"
            )
        out.append(Row(line, name, unit, int(ceiling), parsed, kind))
    families = {row.name: row for row in out}
    for family, spec in FILE_TABLES.items():
        title, header = spec.title, spec.header
        written = "`| " + " | ".join(header) + " |`"
        under = section(text, title)
        listed, refused = (
            ([], [f"holds no {written} table"])
            if under is None
            else (config.gfm_table(under[0], header))
        )
        if under is not None:
            listed = [(line + under[1], cells) for line, cells in listed]
        absent = bool(refused) and refused[0].startswith("holds no ")
        if family not in families:
            if not absent:
                raise Unreadable(
                    f"{where} has a {written} table and no `{family}` row in its "
                    "Budgets table to give its unit, slack and kind"
                )
            continue
        if absent:
            raise Unreadable(
                f"{where} has a `{family}` row and no `## {title}` table "
                f"{written} listing its files"
            )
        if refused:
            raise Unreadable(f"{where} {refused[0]}")
        head = families[family]
        for line, cells in listed:
            path, ceiling = (c.strip().strip("`") for c in cells)
            name, at = f"{family}:{path}", f"{where}, line {line}"
            if not NAME.fullmatch(name):
                raise Unreadable(f"{at}: `{path}` is no file name")
            if name in seen:
                raise Unreadable(f"{at}: `{path}` is written twice")
            seen.add(name)
            if not CEILING.fullmatch(ceiling):
                raise Unreadable(
                    f"{at}: {path}'s ceiling `{ceiling}` is not a whole number "
                    "written in digits alone"
                )
            out.append(Row(line, name, head.unit, int(ceiling), head.slack, head.kind))
    return out


def section(text, title):
    """`(text, lines before it)` of the part of `text` under its `## title`
    heading, to the next heading of level one or two, or None where no such
    heading stands. A per-file table is the one under its family's heading,
    so two families may share a header. A heading is one a renderer shows,
    read off `unverified_check.py#readable`: a line in a fence or a comment
    is none. A title written twice is refused, since then the table is not
    one, as `round_record.py#section_body` refuses a doubled section.

    Reads: guess — a person's markdown, through `unverified_check.py#gfm_lines`, `#readable` and `#heading_level`; unknown refused"""
    reader = sibling("unverified_check")
    lines = reader.gfm_lines(text, keepends=True)
    shown = reader.readable(text)
    levels = [reader.heading_level(line) for line in shown]
    starts = [
        at
        for at, line in enumerate(shown)
        if levels[at] == 2 and line.strip().lstrip("#").strip() == title
    ]
    if not starts:
        return None
    if len(starts) > 1:
        raise Unreadable(
            f"`## {title}` stands {len(starts)} times, so its table is not one"
        )
    end = next(
        (at for at in range(starts[0] + 1, len(lines)) if levels[at] in (1, 2)),
        len(lines),
    )
    return "".join(lines[starts[0] + 1 : end]), starts[0] + 1


def budgets_text_here(root):
    """The text of `seal/budgets.md` in the tree at `root`, or Unreadable.

    Reads: observed — the file on disk, as bytes decoded; unknown refused"""
    path = os.path.join(root, BUDGETS)
    if not os.path.isfile(path):
        raise Unreadable(f"{BUDGETS_GIT} is not in the tree, so no budget was read")
    with open(path, encoding="utf-8", errors="replace") as handle:
        return handle.read()


def budgets_here(root):
    """The rows of `seal/budgets.md` in the tree at `root`.

    Reads: guess — the file a person edits, through `parse_budgets`; unknown refused"""
    return parse_budgets(budgets_text_here(root), BUDGETS_GIT)


def stated_price(text, where):
    """The price level `## Price level` states for `.test_durations`, per
    mille of the prices the seconds ceilings are written in: 1000 where the
    table is not there, Unreadable where it is and does not read as one row.

    Reads: guess — a person's markdown table, through `hooks/config.py#gfm_table`; unknown refused"""
    rows, refused = sibling("config").gfm_table(text, PRICE_HEADER)
    if refused and refused[0].startswith("holds no "):
        return PER_MILLE
    if refused:
        raise Unreadable(f"{where} {refused[0]}")
    cells = [tuple(c.strip().strip("`") for c in cells) for _line, cells in rows]
    if (
        len(cells) != 1
        or cells[0][0] != DURATIONS
        or not CEILING.fullmatch(cells[0][1])
    ):
        raise Unreadable(
            f"{where}'s `## {PRICE_TITLE}` table is not one row "
            f"`| {DURATIONS} | <per mille, in digits> |`"
        )
    return int(cells[0][1])


def base_of(root, ref):
    """`(commit, label)` for `git merge-base REF HEAD`, or Unreadable where
    the base does not resolve.

    Reads: observed — git's merge base, through `unverified_check.py#merge_base`; unknown refused"""
    base = sibling("unverified_check").merge_base(root, ref)
    if base is None:
        raise Unreadable(
            f"the baseline `{ref}` gives no merge base with HEAD — it does not "
            "resolve here, or shares no history with it — so no ceiling was "
            "compared with the one before"
        )
    return base, f"the merge base of {ref} and HEAD ({base[:7]})"


def blob_at(root, base, path, label):
    """The text of `path` at commit `base`, or None where it was not there.

    Reads: observed — the blob git holds; unknown refused"""

    def git(*args):
        return subprocess.run(
            ["git", "-C", root, *args],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )

    listed = git("ls-tree", "--name-only", base, "--", path)
    if listed.returncode != 0:
        raise Unreadable(f"git could not list {path} at {label}")
    if not listed.stdout.strip():
        return None
    shown = git("show", f"{base}:{path}")
    if shown.returncode != 0:
        raise Unreadable(f"git could not read {path} at {label}")
    return shown.stdout


def measure_preload(root, agent, _cache):
    """Bytes of `agents/<agent>.md` and of each `SKILL.md` its `skills:` list
    names, the agent's own share of `payload_meter`'s rows — never the
    `CLAUDE.md` pair, which is the harness's and half of it is not in the tree.

    `preload:claude-md` is the one file every prefix carries, the
    orchestrator's included: `CLAUDE.md` at the root, by its bytes.

    Each file is counted by `lf_bytes`, so a checkout that writes CRLF
    measures what one that writes LF does.

    Reads: owned — an agent definition's frontmatter and the files it names, through `payload_meter`; unknown refused"""
    if agent == CLAUDE_MD:
        path = os.path.join(root, "CLAUDE.md")
        if not os.path.isfile(path):
            raise Unreadable(f"preload:{CLAUDE_MD}: CLAUDE.md is not in the tree")
        return lf_bytes(path)
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
    return sum(lf_bytes(os.path.join(root, row["path"])) for row in own)


def lf_bytes(path):
    """The bytes of the file at `path` with each CRLF counted as one LF:
    what git stores for it under this repository's `eol=lf`, and what every
    platform's checkout measures alike, whatever `core.autocrlf` wrote.

    Reads: observed — the file's bytes on disk; unknown refused"""
    with open(path, "rb") as handle:
        return len(handle.read().replace(*NEWLINES))


def seconds(value):
    """Seconds rounded to the nearest whole one, a half up.

    Reads: nothing — a number from the number handed to it"""
    return math.floor(value + 0.5)


def durations(root):
    """`{case id: seconds}` from `.test_durations`, or Unreadable.

    Reads: observed — the JSON the suite's durations plugin wrote; unknown refused"""
    path = os.path.join(root, DURATIONS)
    if not os.path.isfile(path):
        raise Unreadable(
            f"{DURATIONS} is not in the tree, and the seconds budgets read it"
        )
    with open(path, encoding="utf-8", errors="replace") as handle:
        return durations_from(handle.read(), DURATIONS)


def durations_from(text, where):
    """`{case id: seconds}` from the text of a `.test_durations`, or
    Unreadable naming `where` it was read.

    Reads: observed — the JSON the suite's durations plugin wrote, handed by its caller; unknown refused"""
    try:
        data = json.loads(text)
    except ValueError:
        raise Unreadable(f"{where} is not JSON") from None
    if not isinstance(data, dict) or not all(
        isinstance(v, (int, float)) and not isinstance(v, bool) for v in data.values()
    ):
        raise Unreadable(f"{where} is not an object of case ids to seconds")
    return data


def price_level(base, head, label):
    """`(ratio, common)`: how much higher HEAD's `.test_durations` prices the
    cases both files hold than the base's does, and how many ids that is.

    The ratio is the median, over the test files the base prices at
    `PRICE_FILE_FLOOR` seconds or more on the shared ids, of each file's
    seconds here over its seconds there. A median of files is what moves when
    the runners do and not when one file does: a cleanup that halves one
    file of three leaves it at 1, where the seconds-weighted ratio fell to
    0.706 and read every untouched file 1.42 times slower. On #931's refresh
    the two agree, 1.073 and 1.071.

    1 where the base has no such file, and exactly 1 where the two are the
    same file; Unreadable where they share no case id or no file of that many
    seconds, since then no level can be read.

    Reads: nothing — compares the two readings handed to it"""
    if base is None:
        return 1, 0
    common = base.keys() & head.keys()
    if not common:
        raise Unreadable(
            f"{DURATIONS} here and at {label} share no case id, so no price "
            "level between them can be read"
        )
    before, after = collections.defaultdict(float), collections.defaultdict(float)
    for case in common:
        path = case.split("::", 1)[0]
        before[path] += base[case]
        after[path] += head[case]
    ratios = [after[p] / before[p] for p in before if before[p] >= PRICE_FILE_FLOOR]
    if not ratios:
        raise Unreadable(
            f"{DURATIONS} at {label} prices no test file at {PRICE_FILE_FLOOR} "
            f"seconds or more over the {len(common)} cases it shares with this "
            "tree, so no price level can be read"
        )
    return statistics.median(ratios), len(common)


def measure_suite(root, _subject, cache):
    """Seconds summed over every case `.test_durations` prices, divided by
    the price level the budgets file states (`cache["level"]`), with the raw
    sum kept for the summary.

    Reads: observed — `.test_durations`, through `durations`; unknown refused"""
    raw = sum(durations(root).values())
    cache.setdefault("raw", {})["suite-seconds"] = seconds(raw)
    return seconds(raw / cache.get("level", 1))


def rule_lines(lines):
    """The indexes of LINES inside a rule block: from a line opening with
    `**` to the next `Enforced by:` line, or to the end of its paragraph
    where none closes it first.

    Reads: guess — the lines of a person's markdown its caller hands it; unknown passed"""
    out, at = set(), 0
    while at < len(lines):
        if not lines[at].startswith(RULE_OPENER):
            at += 1
            continue
        end = at
        while end < len(lines):
            if lines[end].startswith(RULE_CLOSER):
                end += 1
                break
            if not lines[end].strip():
                break
            end += 1
        out.update(range(at, end))
        at = end
    return out


def classify(text):
    """`(history line numbers, rule line count)` for one markdown document.

    The lines are GFM's (`unverified_check.py#gfm_lines`), so a line number
    is the one GitHub and `grep -n` show, and the fence and comment walk is
    handed those lines as they stand.

    Reads: guess — a person's markdown, through `hooks/config.py#unfenced` and `unverified_check.py#heading_level`; unknown passed"""
    lines = sibling("unverified_check").gfm_lines(text)
    shown = {index for index, _ in sibling("config").unfenced(lines)}
    heading_level = sibling("unverified_check").heading_level
    rules = rule_lines(lines)
    history, rule = [], 0
    for index, line in enumerate(lines):
        if index not in shown or not line.strip() or heading_level(line) is not None:
            continue
        if index in rules:
            rule += 1
        elif HISTORY.search(line):
            history.append(index + 1)
    return history, rule


def docs_lines(root):
    """`{docs/<file>.md: (history line numbers, rule line count)}` for every
    markdown file at the top of `docs/`.

    Reads: guess — the documents a person writes, through `classify`; unknown passed"""
    directory = os.path.join(root, DOCS)
    out = {}
    names = sorted(os.listdir(directory)) if os.path.isdir(directory) else []
    for name in names:
        path = os.path.join(directory, name)
        if name.endswith(".md") and os.path.isfile(path):
            with open(path, encoding="utf-8", errors="replace") as handle:
                out[f"{DOCS}/{name}"] = classify(handle.read())
    return out


def file_values(root, family, cache):
    """`{file: measured}` for a per-file family, measured once per run by the
    reader its `FILE_TABLES` entry carries, and kept in `cache`.

    Reads: guess — whatever the family's reader reads, through it; unknown refused"""
    if family not in cache:
        cache[family] = FILE_TABLES[family].reader(root, cache)
    return cache[family]


def slow_file_values(root, cache):
    """Each test file's seconds in `.test_durations`, divided by the price
    level, with its raw seconds kept in `cache["raw"]`.

    Reads: observed — `.test_durations`, through `durations`; unknown refused"""
    per_file = collections.defaultdict(float)
    for case, value in durations(root).items():
        per_file[case.split("::", 1)[0]] += value
    level = cache.get("level", 1)
    raw = cache.setdefault("raw", {})
    for path, value in per_file.items():
        raw[f"slow-file:{path}"] = seconds(value)
    return {path: seconds(v / level) for path, v in per_file.items()}


def docs_history_values(root, cache):
    """Each `docs/*.md` file's history lines, with the classification kept in
    `cache["docs"]` for the summary.

    Reads: guess — the documents a person writes, through `docs_lines`; unknown passed"""
    cache["docs"] = docs_lines(root)
    cache.setdefault("at", {})["docs-history"] = {
        path: h for path, (h, _) in cache["docs"].items()
    }
    return {path: len(h) for path, (h, _) in cache["docs"].items()}


def shown_lines(text):
    """`[(line, shown, heading)]` for one markdown document: each GFM line
    (`unverified_check.py#gfm_lines`), whether a renderer shows it outside a
    fence or a comment (`hooks/config.py#unfenced`), and the text of the
    heading it stands under, "" above the first.

    Reads: guess — a person's markdown, through `unverified_check.py#gfm_lines`, `#heading_level` and `hooks/config.py#unfenced`; unknown passed"""
    reader = sibling("unverified_check")
    lines = reader.gfm_lines(text)
    shown = {index for index, _ in sibling("config").unfenced(lines)}
    out, heading = [], ""
    for index, line in enumerate(lines):
        visible = index in shown
        if visible and reader.heading_level(line) is not None:
            heading = line.strip().strip("#").strip()
        out.append((line, visible, heading))
    return out


def rule_paragraphs(text):
    """Every rule paragraph of one markdown document, as `Paragraph`s in
    document order.

    A rule paragraph opens a block — the first line, or one after a blank, a
    heading or a hidden line, or any list item — with `**`, `- **`, `* **` or
    `N. **`, up to three spaces in. It runs to its `Enforced by:` line, which
    it keeps, or stops before a blank line, a heading, a table, a hidden line
    or the next list item. A bold word that a wrap carried to the front of a
    line inside a paragraph opens nothing.

    Reads: guess — a person's markdown, through `shown_lines`; unknown passed"""
    lines = shown_lines(text)
    reader = sibling("unverified_check")
    out, at, open_block = [], 0, True
    while at < len(lines):
        line, visible, heading = lines[at]
        if not visible or not line.strip() or reader.heading_level(line) is not None:
            open_block, at = True, at + 1
            continue
        opens = RULE_PARAGRAPH.match(line) and (open_block or LIST_ITEM.match(line))
        open_block = False
        if not opens:
            at += 1
            continue
        start, enforced, at = at, None, at + 1
        while at < len(lines):
            nxt, visible, _ = lines[at]
            stripped = nxt.strip()
            if (
                not visible
                or not stripped
                or reader.heading_level(nxt) is not None
                or stripped.startswith("|")
                or LIST_ITEM.match(nxt)
            ):
                break
            at += 1
            if stripped.startswith(RULE_CLOSER):
                enforced = stripped[len(RULE_CLOSER) :].strip()
                break
        out.append(Paragraph(start + 1, heading, line.strip(), enforced))
    return out


def enforcer_lines(text):
    """`[(line number, heading, value)]` for every `Enforced by:` line one
    markdown document shows, inside a rule paragraph or not.

    Reads: guess — a person's markdown, through `shown_lines`; unknown passed"""
    return [
        (index + 1, heading, line.strip()[len(RULE_CLOSER) :].strip())
        for index, (line, visible, heading) in enumerate(shown_lines(text))
        if visible and line.strip().startswith(RULE_CLOSER)
    ]


def rule_files(root):
    """`{path: text}` of every rule file in the tree at `root`, by
    `RULE_FILES`, its path written with `/`.

    Reads: observed — the files on disk, decoded; unknown passed"""
    out = {}
    for pattern in RULE_FILES:
        for path in sorted(glob.glob(os.path.join(root, *pattern.split("/")))):
            if os.path.isfile(path):
                rel = os.path.relpath(path, root).replace(os.sep, "/")
                with open(path, encoding="utf-8", errors="replace") as handle:
                    out[rel] = handle.read()
    return out


def targets_of(value):
    """The targets an `Enforced by:` value names, none where it says
    `nothing — <why>` — read by `fold_check.py#names_targets`, so the two
    checkers split one line alike.

    Reads: guess — the value of a line a person wrote; unknown passed"""
    if not sibling("fold_check").names_targets(value):
        return []
    return value.split(",")


def target_problem(root, target):
    """Why one `Enforced by:` target does not resolve in the tree at `root`,
    or None where it does. An eval case directory, `evals/behaviour/<agent>/
    <case>/` with its slash, resolves where it holds `case.yaml`; every other
    target is `fold_check.py#target_problem`'s, and a Python file it cannot
    parse is Unreadable.

    Reads: observed — the tree at `root`, through `fold_check.py#target_problem`; unknown refused"""
    cell = target.strip().strip("`")
    if cell.startswith(EVAL_CASES) and cell.endswith("/"):
        parts = cell[len(EVAL_CASES) : -1].split("/")
        if len(parts) < 2 or not all(parts):
            return f"{cell} is no eval case: write `{EVAL_CASES}<agent>/<case>/`"
        base = os.path.realpath(root)
        full = os.path.realpath(os.path.join(base, *cell[:-1].split("/")))
        if os.path.commonpath([full, base]) != base:
            return f"{cell} is not a path inside the repository"
        if not os.path.isfile(os.path.join(full, EVAL_CASE)):
            return f"{cell} holds no {EVAL_CASE}"
        return None
    fold_check = sibling("fold_check")
    try:
        return fold_check.target_problem(root, cell)
    except fold_check.Unusable as error:
        raise Unreadable(f"enforced-unresolved: a target {error}") from None


def measure_unresolved(root, _subject, cache):
    """How many `Enforced by:` targets in the rule files do not resolve, each
    kept in `cache["detail"]` as its file, heading and why.

    Reads: guess — the rule files, through `rule_files`, `enforcer_lines` and `target_problem`; unknown refused"""
    found = []
    for path, text in rule_files(root).items():
        for number, heading, value in enforcer_lines(text):
            for target in targets_of(value):
                problem = target_problem(root, target)
                if problem:
                    found.append(f"{path}:{number} §*{heading}*: {problem}")
    if found:
        cache.setdefault("detail", {})["enforced-unresolved"] = (
            ". The targets that do not resolve: " + "; ".join(found)
        )
    return len(found)


def unenforced_values(root, cache):
    """Each rule file's rule paragraphs that carry no `Enforced by:` line or
    one saying `nothing — <why>`, counted, with the lines they open on kept
    in `cache["at"]["unenforced"]`.

    Reads: guess — the rule files, through `rule_files` and `rule_paragraphs`; unknown passed"""
    at, out = {}, {}
    for path, text in rule_files(root).items():
        lines = [
            p.line
            for p in rule_paragraphs(text)
            if p.enforced is None or not targets_of(p.enforced)
        ]
        at[path], out[path] = lines, len(lines)
    cache.setdefault("at", {})["unenforced"] = at
    return out


# The families measured per file: the heading and header of each one's table,
# the unit its family row must state, and the reader that measures its files.
# A per-file family another work item adds is one entry here.
FILE_TABLES = {
    "slow-file": FileFamily(
        "Slow test files",
        ("File", "Seconds ceiling"),
        "seconds",
        slow_file_values,
        DURATIONS,
    ),
    "docs-history": FileFamily(
        "Docs history lines", ("File", "Lines ceiling"), "lines", docs_history_values
    ),
    "unenforced": FileFamily(
        "Unenforced rules",
        ("File", "Rules ceiling"),
        "rules",
        unenforced_values,
        "the rule files",
        "unenforced rules",
    ),
}


def measure_rounds(root, _subject, cache):
    """The largest `seal/specs/<id>/rounds/` in the tree, in bytes counted as
    `lf_bytes` counts them, with every work item's total and file count kept
    in `cache["rounds"]` for the summary.

    Reads: observed — the round records on disk, as bytes; unknown passed"""
    specs = os.path.join(root, "seal", "specs")
    items = {}
    for item in sorted(os.listdir(specs)) if os.path.isdir(specs) else []:
        rounds = os.path.join(specs, item, "rounds")
        if not os.path.isdir(rounds):
            continue
        files = [
            os.path.join(rounds, name)
            for name in sorted(os.listdir(rounds))
            if os.path.isfile(os.path.join(rounds, name))
        ]
        items[item] = (sum(lf_bytes(path) for path in files), len(files))
    cache["rounds"] = items
    return max((size for size, _ in items.values()), default=0)


# A budget's name is `<family>` or `<family>:<subject>`; the family picks the
# measurer, the unit the row must state, and whether a subject is named. A
# family another work item adds is one more entry here and, where it is read
# per file, one more `FILE_TABLES` entry.
MEASURERS = {
    "preload": (measure_preload, "bytes", True),
    "suite-seconds": (measure_suite, "seconds", False),
    "rounds-bytes": (measure_rounds, "bytes", False),
    "enforced-unresolved": (measure_unresolved, "targets", False),
}


def families():
    """Every family's name as a row writes it, from the tables that define
    them, so a family added there is named here too.

    Reads: nothing — the module's own tables"""
    named = [f"{f}:<subject>" if MEASURERS[f][2] else f for f in MEASURERS]
    named += [*FILE_TABLES, *(f"{f}:<leg>" for f in PER_RUN)]
    return sorted(named)


def measure(root, row, cache):
    """What `row` measures in the tree at `root`, in the row's unit.

    Reads: owned — the row's family, in the vocabulary `MEASURERS` defines; unknown refused"""
    family, _, subject = row.name.partition(":")
    if family not in MEASURERS or bool(subject) != MEASURERS[family][2]:
        raise Unreadable(
            f"{row.name}: no measurer here reads a budget of that name — the "
            f"families are {', '.join(f'`{name}`' for name in families())}"
        )
    measurer, unit, _ = MEASURERS[family]
    if row.unit != unit:
        raise Unreadable(
            f"{row.name}: the unit is `{row.unit}`, and {family} is measured in {unit}"
        )
    return measurer(root, subject, cache)


def top_of_band(measured, slack):
    """The highest ceiling `measured` allows under `slack`, or None for a
    one-sided row, which has no band above its reading.

    Reads: nothing — a number from the numbers handed to it"""
    if slack.amount is None:
        return None
    if slack.absolute:
        return measured + slack.amount
    return int(measured * (1 + slack.amount))


def at_lines(lines, noun="history lines"):
    """The sentence naming where a document's `noun` stand, or "".

    Reads: nothing — formats the line numbers handed to it"""
    if not lines:
        return ""
    return f". Its {noun} are at lines {', '.join(str(n) for n in lines)}"


def band(row, measured, detail=""):
    """`Result` for one row: what is wrong with its ceiling against
    `measured`, from both sides. `detail` is the sentence naming what was
    counted — a document's history lines, the targets that do not resolve —
    said where it is over.

    Reads: nothing — compares the numbers handed to it"""
    top = top_of_band(measured, row.slack)
    problems = []
    if measured > row.ceiling:
        problems.append(
            f"measured {measured:,} {row.unit} is over the ceiling {row.ceiling:,} "
            f"by {round(measured - row.ceiling, 1):,}{detail}. Bring it "
            f"back under, or raise the ceiling in {BUDGETS_GIT} and write `Budget "
            f"raised: {row.name} {row.ceiling} -> <new>: <reason>` in the pull "
            "request body"
        )
    elif top is not None and row.ceiling > top:
        problems.append(
            f"the ceiling {row.ceiling:,} sits above the band: measured "
            f"{measured:,} {row.unit} at {row.slack.text} slack allows at most "
            f"{top:,}. Lower the ceiling in {BUDGETS_GIT} to {measured} — "
            f"anything from {measured} to {top} holds"
        )
    return Result(row, measured, top, problems)


def unlisted_band(row, unlisted, at):
    """`Result` for a per-file family's own row: each file its table does not
    list, held to the row's ceiling, and named where it is over with the
    lines `at` keeps for it. The row has no lower band, because its ceiling is
    a threshold rather than a reading.

    Reads: nothing — compares the numbers handed to it"""
    title, noun = FILE_TABLES[row.name].title, FILE_TABLES[row.name].noun
    problems = [
        f"{path} is not listed and measures {value:,} {row.unit}, over the "
        f"{row.ceiling:,} every file `## {title}` does not list is held to"
        f"{at_lines(at.get(path, ()), noun)}. Bring it under, or list it there and "
        f"write `Budget raised: {row.name}:{path} {row.ceiling} -> <new>: "
        "<reason>` in the pull request body"
        for path, value in sorted(unlisted.items())
        if value > row.ceiling
    ]
    return Result(row, max(unlisted.values(), default=0), None, problems)


def declarations(body):
    """`(raised, removed)` the body declares: `raised` maps a name to its
    `(old, new, reason)` lines, `removed` a name to its reasons.

    A line is a line where GitHub renders one (`unverified_check.py#gfm_lines`),
    so a declaration has to open a line the body shows.

    Reads: guess — a person's pull request body, one line at a time; unknown refused"""
    raised, removed = collections.defaultdict(list), collections.defaultdict(list)
    for line in sibling("unverified_check").gfm_lines(body):
        text = line.strip()
        up = RAISED.fullmatch(text)
        if up:
            raised[up["name"]].append((int(up["old"]), int(up["new"]), up["reason"]))
            continue
        gone = REMOVED.fullmatch(text)
        if gone:
            removed[gone["name"]].append(gone["reason"])
    return raised, removed


def effective(rows, others):
    """`{name: Row}` for ROWS, with every file row OTHERS has and ROWS lacks
    held at its family's ceiling in ROWS, which is what an unlisted file is
    held to there.

    Reads: nothing — rows its caller read"""
    out = {row.name: row for row in rows}
    for row in others:
        family, _, subject = row.name.partition(":")
        if subject and family in FILE_TABLES and family in out and row.name not in out:
            out[row.name] = out[family]._replace(name=row.name, line=None)
    return out


def widened(old, new, at):
    """Whether slack NEW lets a ceiling sit further over a reading of AT than
    slack OLD does; `one-sided` is the widest.

    Reads: nothing — compares the two slacks handed to it"""
    before, after = top_of_band(at, old), top_of_band(at, new)
    return before is not None and (after is None or after > before)


def ratchet(base_rows, head_rows, body, release):
    """`(problems, moves)`: each gate row raised or removed since the base
    with no line for it, and every raise or removal read, as `(name, what,
    reason)` for the summary.

    Reads: guess — a pull request body its caller handed it, through `declarations`; unknown refused"""
    raised, removed = declarations(body)
    base = effective(base_rows, head_rows)
    head = effective(head_rows, base_rows)
    problems, moves = [], []
    for old in base.values():
        if old.kind != GATE:
            continue
        new = head.get(old.name)
        family, _, subject = old.name.partition(":")
        if new is None and subject and family in FILE_TABLES:
            # A file row whose family row is gone: the family's removal is
            # the one line it needs.
            continue
        if new is not None and new.kind == GATE:
            # A file row's slack is its family's, which the family row answers for.
            file_row = bool(subject) and family in FILE_TABLES
            wider = not file_row and widened(old.slack, new.slack, old.ceiling)
            if new.ceiling <= old.ceiling and not wider:
                continue
            what = f"raised {old.ceiling} -> {new.ceiling}"
            if wider:
                what += f", slack {old.slack.text} -> {new.slack.text}"
            lines = raised.get(old.name, [])
            match = [r for o, n, r in lines if (o, n) == (old.ceiling, new.ceiling)]
            if match or release:
                moves.append((old.name, what, match[0] if match else "at a release"))
                continue
            moves.append((old.name, what, UNDECLARED))
            wrote = "".join(f" The body's line says {o} -> {n}." for o, n, _ in lines)
            moved = []
            if new.ceiling > old.ceiling:
                moved.append(
                    f"the ceiling was raised from {old.ceiling} to {new.ceiling}"
                )
            if wider:
                moved.append(
                    f"the slack was widened from {old.slack.text} to {new.slack.text}"
                )
            problems.append(
                (
                    old.name,
                    f"{' and '.join(moved)}, and the pull request body declares no "
                    f"such raise.{wrote} Write `Budget raised: {old.name} "
                    f"{old.ceiling} -> {new.ceiling}: <reason>` in the body",
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


def render(results, moves, against, cache=None):
    """The summary as markdown: one line per budget, the raises read, the
    price level the seconds rows were read at, and where the docs were
    classified, each document's history and rule lines.

    Reads: nothing — formats the results handed to it"""
    cache = cache or {}
    docs, raw = cache.get("docs"), cache.get("raw", {})
    ratio, common = cache.get("price", (1, 0))
    level = cache.get("level", 1)
    lines = [
        "### Budgets",
        "",
        f"From `{BUDGETS_GIT}`; the ratchet read {against}.",
    ]
    if ratio != 1:
        lines.append(
            f"`{DURATIONS}` prices the {common:,} cases it shares with the base "
            f"x{ratio:.3f} the base's, the median over its test files."
        )
    if level != 1:
        lines.append(
            f"The seconds rows are divided by the price level x{float(level):.3f} "
            f"that `## {PRICE_TITLE}` states, into the prices their ceilings are "
            "written in."
        )
    lines += [
        "",
        "| Budget | Measured | Ceiling | Headroom | Kind | Verdict |",
        "|---|---|---|---|---|---|",
    ]
    for result in results:
        row = result.row
        if result.measured is None:
            why = UNREAD.get(row.name.partition(":")[0], "not read on this run")
            lines.append(
                f"| `{row.name}` | — ({why}) | {row.ceiling:,} | — | {row.kind} "
                "| not this run |"
            )
            continue
        room = round(row.ceiling - result.measured, 1)
        share = f"{room / row.ceiling:.1%}" if row.ceiling else "—"
        verdict = "holds" if not result.problems else "over" if room < 0 else "lower it"
        largest = " (largest unlisted)" if row.name in FILE_TABLES else ""
        if level != 1 and row.name in raw:
            largest += f" (raw {raw[row.name]:,} at x{float(level):.3f})"
        lines.append(
            f"| `{row.name}` | {result.measured:,} {row.unit}{largest} | "
            f"{row.ceiling:,} | {room:,} ({share}) | {row.kind} | {verdict} |"
        )
    if moves:
        lines += ["", "Ceilings moved since the base:", ""]
        lines += [f"- `{name}` {what}: {reason}" for name, what, reason in moves]
    if cache.get("legs"):
        lines += ["", billable(cache["legs"])]
    if cache.get("rounds"):
        lines += ["", "Round records per work item, the largest first:", ""]
        lines += [
            f"- `{item}`: {size:,} bytes over {count} files"
            for item, (size, count) in sorted(
                cache["rounds"].items(), key=lambda pair: (-pair[1][0], pair[0])
            )
        ]
    if cache.get("trend"):
        tag, then = cache["trend"]
        lines += ["", f"Against {tag}, one line per budget:", ""]
        for result in results:
            row = result.row
            before = then.get(row.name)
            now = "unread" if result.measured is None else f"{result.measured:,}"
            was = "new since then" if before is None else f"ceiling {before.ceiling:,}"
            lines.append(
                f"- `{row.name}`: {was}; ceiling {row.ceiling:,}, measured {now} {row.unit}"
            )
        gone = sorted(set(then) - {result.row.name for result in results})
        lines += [f"- `{name}`: gone since then" for name in gone]
    if docs:
        history = sum(len(h) for h, _ in docs.values())
        rule = sum(r for _, r in docs.values())
        lines += [
            "",
            "History and rule lines per document — the first is gated, the "
            "ratio is read:",
            "",
        ]
        lines += [
            f"- `{path}`: {len(h)} history · {r} rule" for path, (h, r) in docs.items()
        ]
        ratio = f"{rule / history:.1f}" if history else "—"
        lines.append(
            f"- all {len(docs)}: {history} history · {rule} rule · {ratio} rule per history"
        )
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


def trend_rows(root, tag):
    """`{name: Row}` of `seal/budgets.md` at `tag`, none where the file was
    not there yet, or Unreadable where the tag names nothing.

    Reads: guess — the file a person edits, as git holds it at a tag, through `blob_at` and `parse_budgets`; unknown refused"""
    if not tag:
        raise Unreadable("--trend names no tag, so nothing was compared with a release")
    text = blob_at(root, tag, BUDGETS_GIT, tag)
    rows = [] if text is None else parse_budgets(text, f"{BUDGETS_GIT} at {tag}")
    return {row.name: row for row in rows}


def check(root, baseline=None, body="", release=False, ci_jobs=None, trend=None):
    """`(problems, refusals, summary)` for the tree at `root`, or, with
    `ci_jobs`, for the rows read off that one run, and only those. With
    `trend`, the summary sets every budget beside its ceiling at that tag.

    Reads: guess — `seal/budgets.md` and the body its caller handed it, through the units above; unknown refused"""
    head_text = budgets_text_here(root)
    head = parse_budgets(head_text, BUDGETS_GIT)
    level = stated_price(head_text, BUDGETS_GIT)
    names = {row.name for row in head}
    results, refusals = [], []
    cache = {"level": fractions.Fraction(level, PER_MILLE)}
    if ci_jobs is not None:
        cache["legs"] = leg_minutes(read_jobs(ci_jobs))
        head = [row for row in head if row.name.partition(":")[0] in PER_RUN]
        if not head:
            raise Unreadable(
                f"--ci-jobs was given and {BUDGETS_GIT} has no row read off a "
                "run, so this run read a job list for nothing"
            )
    if trend is not None:
        cache["trend"] = (trend, trend_rows(root, trend))
    moves, against, base_rows, priced = [], "no baseline", None, []
    if baseline is not None:
        base, against = base_of(root, baseline)
        base_text = blob_at(root, base, BUDGETS_GIT, against)
        where = f"{BUDGETS_GIT} at {against}"
        base_rows = [] if base_text is None else parse_budgets(base_text, where)
        base_level = PER_MILLE if base_text is None else stated_price(base_text, where)
        if any(row.name.partition(":")[0] in PRICED for row in head):
            text = blob_at(root, base, DURATIONS, against)
            before = (
                None
                if text is None
                else durations_from(text, f"{DURATIONS} at {against}")
            )
            ratio, common = price_level(before, durations(root), against)
            cache["price"] = (ratio, common)
            priced = price_problems(base_level, ratio, common, level)
    for row in head:
        try:
            results.append(measured_row(root, row, names, cache))
        except Unreadable as error:
            refusals.append(str(error))
    # A price level left behind by a refresh comes first: every seconds row
    # below it is read at the wrong level until it is restated.
    problems = priced + [
        (r.row.name, p) for r in results if r.row.kind == GATE for p in r.problems
    ]
    if base_rows is not None:
        found, moves = ratchet(base_rows, head, body, release)
        problems += found
    return problems, refusals, render(results, moves, against, cache)


def price_problems(base_level, ratio, common, level):
    """The one problem a price level that does not follow the durations file
    is, or none: the level here has to be the base's times the ratio the
    file moved by, per mille and rounded, so a refresh restates it in one
    number and no other edit can move it.

    Reads: nothing — compares the numbers handed to it"""
    expected = seconds(base_level * ratio)
    if level == expected:
        return []
    return [
        (
            "price level",
            f"`{DURATIONS}` prices the {common:,} cases it shares with the base "
            f"x{ratio:.3f} the base's, so its price level is {base_level} x "
            f"{ratio:.3f} = {expected} per mille, and `## {PRICE_TITLE}` in "
            f"{BUDGETS_GIT} says {level}. Write {expected} there; a price level "
            "takes no `Budget raised:` line, because the durations file is what "
            "moves it",
        )
    ]


def measured_row(root, row, names, cache):
    """`Result` for one row of the tree at `root`: a per-file family's own
    row holds the files `names` does not list, a file row its file, and any
    other row its measurer's reading.

    Reads: guess — the tree, through `file_values` and `measure`; unknown refused"""
    family, _, subject = row.name.partition(":")
    if family in PER_RUN:
        return run_row(row, subject, cache.get("legs"))
    if family not in FILE_TABLES:
        value = measure(root, row, cache)
        if value is None:
            return Result(row, None, None, [])
        return band(row, value, cache.get("detail", {}).get(row.name, ""))
    spec = FILE_TABLES[family]
    if row.unit != spec.unit:
        raise Unreadable(
            f"{row.name}: the unit is `{row.unit}`, and {family} is measured in "
            f"{spec.unit}"
        )
    values = file_values(root, family, cache)
    at = cache.get("at", {}).get(family, {})
    if not subject:
        unlisted = {
            path: value
            for path, value in values.items()
            if f"{family}:{path}" not in names
        }
        return unlisted_band(row, unlisted, at)
    if subject not in values:
        raise Unreadable(
            f"{row.name}: {subject} is not in {spec.source}, so its row holds "
            "nothing — remove it"
        )
    return band(row, values[subject], at_lines(at.get(subject, ()), spec.noun))


def read_jobs(path):
    """The jobs of one workflow run, one JSON object a line, as `gh api
    …/actions/runs/<id>/jobs --paginate --jq '.jobs[]'` prints them, or
    Unreadable.

    Reads: observed — the job list GitHub's API returned, written by `gh`; unknown refused"""
    if not os.path.isfile(path):
        raise Unreadable(f"the job list {os.path.basename(path)} is not there")
    jobs = []
    with open(path, encoding="utf-8", errors="replace") as handle:
        for number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                job = json.loads(line)
            except ValueError:
                raise Unreadable(f"line {number} of the job list is not JSON") from None
            if not isinstance(job, dict) or not isinstance(job.get("name"), str):
                raise Unreadable(f"line {number} of the job list is no job with a name")
            jobs.append(job)
    return jobs


def leg_minutes(jobs):
    """`{leg: [minutes of each of its pytest jobs]}` for one run. A job's leg
    is read off its name, `pytest (<os>-latest, …)` — never off its runner's
    name, which carries no operating system — and its minutes are its
    `completed_at` less its `started_at`. A pytest job with no times is
    Unreadable: the run is read after its pytest jobs end.

    Reads: observed — the job list GitHub's API returned, through `read_jobs`; unknown refused"""
    legs = collections.defaultdict(list)
    for job in jobs:
        match = PYTEST_JOB.fullmatch(job["name"])
        if not match:
            continue
        try:
            started = datetime.datetime.fromisoformat(job["started_at"])
            completed = datetime.datetime.fromisoformat(job["completed_at"])
        except (KeyError, TypeError, ValueError):
            raise Unreadable(
                f"the job `{job['name']}` has no start and end time, and this "
                "reads a run after its pytest jobs have ended"
            ) from None
        legs[match.group(1)].append((completed - started).total_seconds() / 60)
    return dict(legs)


def run_row(row, leg, legs):
    """`Result` for one `ci-minutes:<leg>` row: the leg's minutes summed over
    its pytest jobs, held to its ceiling, or no reading where this run read
    no job list — the tree's run, whose rows the tests workflow measures.

    Reads: nothing — compares the minutes handed to it"""
    if leg not in BILLING:
        raise Unreadable(
            f"{row.name}: no leg of the tests workflow is called `{leg}` — the "
            f"legs are {', '.join(f'`ci-minutes:{name}`' for name in BILLING)}"
        )
    if row.unit != "minutes":
        raise Unreadable(
            f"{row.name}: the unit is `{row.unit}`, and ci-minutes is measured in minutes"
        )
    if legs is None:
        return Result(row, None, None, [])
    if leg not in legs:
        raise Unreadable(f"{row.name}: no pytest job of this run ran on {leg}")
    return band(row, round(sum(legs[leg]), 1))


def billable(legs):
    """The run's billable line: each job rounded up to its minute, as GitHub
    bills it, at its leg's multiple of a Linux minute, and the dollars at the
    price #929 read, labelled with that price's date as unverified.

    Reads: nothing — formats the minutes handed to it"""
    parts, total = [], 0
    for leg in sorted(legs):
        minutes = sum(math.ceil(m) for m in legs[leg])
        factor = BILLING.get(leg)
        if factor is None:
            return f"Billable: no multiple is known for the {leg} leg, so no total is given."
        total += minutes * factor
        parts.append(f"{leg} {minutes} x {factor}")
    return (
        f"Billable: {' + '.join(parts)} = {total:,} Linux-equivalent minutes, "
        f"US${total * LINUX_MINUTE_USD:,.2f} at ${LINUX_MINUTE_USD} a Linux minute "
        "— the price #929 read in mid-2026, its date unverified: check it "
        "against GitHub's Actions price list before quoting the dollars."
    )


def main(argv=None, env=None):
    """Measure, compare, print; the exit code is the verdict.

    Reads: guess — the arguments, the environment and the pull request body in it; unknown refused"""
    env = os.environ if env is None else env
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=ROOT)
    parser.add_argument("--baseline", metavar="REF")
    parser.add_argument("--pr-body-env", metavar="VAR")
    parser.add_argument("--base-ref", metavar="BRANCH", default="")
    parser.add_argument("--ci-jobs", metavar="FILE")
    parser.add_argument("--trend", metavar="TAG")
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
            ci_jobs=args.ci_jobs,
            trend=args.trend,
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
