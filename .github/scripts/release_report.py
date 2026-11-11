#!/usr/bin/env python3
"""release-report — one table of the release against the last release tag.

  release_report.py --against TAG --at DIR [--root DIR]
                    [--ci-jobs FILE] [--ci-jobs-at FILE]
                    [--durations FILE] [--durations-at FILE]

Prints one markdown table, `| What | <TAG> | Now | Change |`, under
`### Against <TAG>`: each agent's preload bytes, the suite's seconds, each CI
leg's minutes and each document's bytes, read from the tree at `--at` (the
tag's) and the tree at `--root` (this one, by default the repository this
script is in), and from the files each side's run left. The tests workflow
runs it after the suite on a pull request into `main` and appends what it
prints to the job's summary.

  preload `<agent>`   the bytes of `agents/<agent>.md` and of each skill its
                      `skills:` list names, the agent's own share of
                      `skills/verify/scripts/payload_meter.py#composition`
  the suite           the seconds the durations union prices every case at,
                      read from `--durations` (this run's) and
                      `--durations-at` (the tag's push run's), each the
                      `.test_durations` of a run's `test-durations`
                      artifact; `no union found` where the file is not given
                      or absent
  `<leg>` leg         the minutes of one run's `pytest (<leg>-latest, <python>,
                      …)` jobs at the floor `lib/launch.py#FLOOR`
                      holds, summed, each `completed_at` less `started_at`,
                      read from a job list as `gh api …/jobs --paginate
                      --jq '.jobs[]'` prints it; `no run found` where the
                      file is absent, empty or holds no such job
  `<leg> <python>` leg
                      the same, for the jobs at another Python: one row for
                      each, after the three, where either job list holds it.
                      A system other than the three gets a row at the floor
                      too, as `<leg>` leg
  `<document>`        the bytes of the core (`skills/core/SKILL.md`),
                      `CLAUDE.md`, `CONTRIBUTING.md` and each document of
                      the policy root that `seal fold` reads
                      (`skills/settle/scripts/fold_check.py#documents`),
                      each CRLF counted as the LF git stores

Under it, a second table under `### Test files against <TAG>` gives one row
per test file either union prices: its cases and seconds at the tag and now,
slowest now first, `no union found` in the cells of a side with no union.

It fails nothing: no row is held to a number, and its reader is whoever
prepares the release. A leg's minutes compare one run with one run, which
swing on the same code, and the table's header says so.

Exit codes: **0** the table was printed, whatever it shows · **2** a tree,
a durations union that is there and does not parse, an agent definition, its
policy root's index, or a module it reads through cannot be read.
"""

import argparse
import datetime
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
# `lib/` first on `sys.path`, where `lib/sibling.py` is imported from at the
# first load, in `module`; each module is named as `lib/sibling.py#load`
# names it.
sys.path.insert(0, os.path.join(ROOT, "lib"))
METER = "skills/verify/scripts/payload_meter.py"
FOLD = "skills/settle/scripts/fold_check.py"
CONFIG = "lib/config.py"
OPTIN = "lib/optin.py"
LAUNCH = "lib/launch.py"
# Beside these, each document of the policy root `FOLD`'s `documents` lists.
DOCUMENTS = ("skills/core/SKILL.md", "CLAUDE.md", "CONTRIBUTING.md")
# The legs of the tests workflow at the floor, in the order a reader compares
# them, and the name of a pytest job, which opens with its operating system
# and its Python.
LEGS = ("ubuntu", "windows", "macos")
PYTEST_JOB = re.compile(r"pytest \(([a-z]+)-[^,)]*, ([^,)]+)(?:,.*)?\)")
NO_RUN = "no run found"
NO_UNION = "no union found"
ABSENT = "—"
HEADER = (
    "Each agent's preload, the suite's seconds, each CI leg's minutes and "
    "each document's size, at the last release tag and now. Nothing here "
    "fails: a leg's minutes compare one run with one run, which swing on the "
    "same code, so no row is a verdict."
)
FILES_HEADER = (
    "Each test file's priced cases and seconds in the durations union, at the "
    "last release tag and now, slowest now first. A report and never a "
    "ceiling: a heavily exercised module needs the cases it needs."
)


class Unreadable(Exception):
    """A tree or a file the table reads could not be read, and the sentence
    says which."""


def module(rel):
    """The module at REL, as `lib/sibling.py#load` returns it, and the one
    function every load of this script goes through. The loader is imported
    here, at the first module asked for, so a run that ends at its usage
    line loads nothing.

    Where `lib/sibling.py` is absent, the refusal is the loader's sentence
    about it at exit 2, spelt here because the file that holds the
    sentence is the one missing."""
    try:
        import sibling
    except ImportError:
        sys.stderr.write(
            "cannot read "
            + os.path.normpath(os.path.join(ROOT, "lib", "sibling.py"))
            + ", which this command loads. It ships in the plugin beside this "
            "script; a copy of one script taken on its own is not a plugin. "
            "Nothing was read.\n"
        )
        raise SystemExit(2) from None
    return sibling.load(rel)


def meter():
    """`payload_meter.py`, as `module` returns it."""
    return module(METER)


def floor():
    """The plugin's floor as a job name writes it, `3.12`, from `LAUNCH`'s
    `FLOOR`."""
    return ".".join(str(part) for part in module(LAUNCH).FLOOR)


def lf_bytes(path):
    """The bytes of the file at `path` with each CRLF counted as one LF."""
    with open(path, "rb") as handle:
        return len(handle.read().replace(b"\r\n", b"\n"))


def preloads(root, kernel):
    """`{agent: bytes}` for every agent the tree at `root` defines."""
    try:
        found = kernel.agents_in(root)
        out = {}
        for agent, definition in found.items():
            rows = kernel.composition(root, root, agent, definition, False)
            out[agent] = sum(row["bytes"] for row in rows if row["share"] == "agent")
    except OSError as error:
        raise Unreadable(
            f"an agent definition under {root} cannot be read: {error}"
        ) from None
    return out


def durations(path):
    """The durations union at `path`, `{case id: seconds}`; None where no
    path is given or no file is there, as a run that uploaded no union or a
    tag whose artifact has expired leaves it; Unreadable where the file is
    there and is no such map."""
    if not path or not os.path.isfile(path):
        return None
    try:
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, ValueError) as error:
        raise Unreadable(
            f"the durations union {path} cannot be read: {error}"
        ) from None
    if not isinstance(data, dict) or not all(
        isinstance(v, (int, float)) and not isinstance(v, bool) for v in data.values()
    ):
        raise Unreadable(
            f"the durations union {path} is no object of case ids to seconds"
        )
    return data


def by_file(priced):
    """`{test file: (cases, seconds)}` for `durations`' reading `priced`."""
    files = {}
    for case, seconds in priced.items():
        cases, total = files.get(case.split("::")[0], (0, 0.0))
        files[case.split("::")[0]] = (cases + 1, total + seconds)
    return files


def module_rows(at, now):
    """One table row per test file the union `at` or the union `now` prices,
    each `durations`' reading: its cases and seconds in each, slowest now
    first, a file absent from one union shown absent there, and both cells
    of a side with no union reading `NO_UNION`."""
    sides = [
        ({}, NO_UNION) if priced is None else (by_file(priced), ABSENT)
        for priced in (at, now)
    ]
    old, new = sides[0][0], sides[1][0]

    def slowest(path):
        return (-new.get(path, (0, 0.0))[1], -old.get(path, (0, 0.0))[1], path)

    rows = []
    for path in sorted(set(old) | set(new), key=slowest):
        cells = [f"`{path}`"]
        for side, missing in sides:
            cases, seconds = side.get(path, (None, None))
            cells += [cell(cases, 0, missing), cell(seconds, 1, missing)]
        rows.append("| " + " | ".join(cells) + " |")
    return rows


def files_table(tag, rows):
    """The test-file table printed under the release table."""
    lines = [
        f"### Test files against {tag}",
        "",
        FILES_HEADER,
        "",
        f"| Test file | Cases at {tag} | Seconds at {tag} | Cases now | Seconds now |",
        "|---|---|---|---|---|",
    ]
    return "\n".join(lines + rows) + "\n"


def documents(root):
    """`{path: bytes}` of the core, `CLAUDE.md`, `CONTRIBUTING.md` and each
    document of the policy root in the tree at `root`, as `FOLD`'s
    `documents` lists them: its top level and each group its index names.
    Each path is written with `/`; Unreadable where the index cannot be
    read."""
    paths = [
        path
        for pattern in DOCUMENTS
        for path in sorted(glob.glob(os.path.join(root, *pattern.split("/"))))
    ]
    config = module(CONFIG)
    optin = module(OPTIN)
    # The shared root's name, or `optin.HOME` where none is marked, as an
    # unmarked `seal/` was read before the second name.
    home = os.path.join(root, optin.home_name(root) or optin.HOME)
    policy = config.policy_root(home)
    if os.path.isdir(os.path.join(root, *policy.split("/"))):
        fold = module(FOLD)
        try:
            listed = fold.documents(root, policy)
        except fold.Unusable as refused:
            raise Unreadable(str(refused)) from None
        paths += [os.path.join(root, *rel.split("/")) for rel in listed]
    out = {}
    for path in paths:
        if os.path.isfile(path):
            out[os.path.relpath(path, root).replace(os.sep, "/")] = lf_bytes(path)
    return out


def leg_minutes(path, at_floor=None):
    """`{leg: minutes}` for one run's job list at `path`, the minutes of a
    leg summed over its pytest jobs; `{}` where there is no such file, it is
    empty, or a line of it is no job. A job at `at_floor`, `floor()` where
    none is given, is its operating system's leg, and a job at another
    Python is the leg `<os> <python>`. A job with no start or end time is
    not counted, and a leg none of whose jobs has both is no reading."""
    if not path or not os.path.isfile(path):
        return {}
    at_floor = at_floor or floor()
    legs = {}
    with open(path, encoding="utf-8", errors="replace") as handle:
        for line in handle:
            if not line.strip():
                continue
            try:
                job = json.loads(line)
            except ValueError:
                return {}
            if not isinstance(job, dict) or not isinstance(job.get("name"), str):
                return {}
            match = PYTEST_JOB.fullmatch(job["name"])
            if not match:
                continue
            try:
                started = datetime.datetime.fromisoformat(job["started_at"])
                completed = datetime.datetime.fromisoformat(job["completed_at"])
            except (KeyError, TypeError, ValueError):
                continue
            minutes = (completed - started).total_seconds() / 60
            system, python = match.groups()
            leg = system if python == at_floor else f"{system} {python}"
            legs[leg] = legs.get(leg, 0) + minutes
    return legs


def other_legs(jobs_at, jobs_now):
    """The legs either job list holds beyond `LEGS`, by `LEGS`' order of
    their operating system and then by Python version."""

    def order(leg):
        system, _, python = leg.partition(" ")
        rank = LEGS.index(system) if system in LEGS else len(LEGS)
        version = [
            (0, int(p), "") if p.isdigit() else (1, 0, p) for p in python.split(".")
        ]
        return rank, system, version

    return sorted((set(jobs_at) | set(jobs_now)) - set(LEGS), key=order)


def change(old, new, digits=0):
    """The Change cell: the difference and its share of the old reading, or
    which side has no reading."""
    if old is None and new is None:
        return ABSENT
    if old is None:
        return "new"
    if new is None:
        return "gone"
    delta = new - old
    text = f"{delta:+,.{digits}f}"
    return f"{text} ({delta / old:+.1%})" if old else text


def cell(value, digits=0, missing=ABSENT):
    """One reading as the table prints it."""
    return missing if value is None else f"{value:,.{digits}f}"


def table(tag, at, now, jobs_at, jobs_now):
    """The printed table: `at` and `now` are each `(preloads, seconds,
    documents)`, `jobs_at` and `jobs_now` each `{leg: minutes}`."""
    rows = []
    for agent in sorted(set(at[0]) | set(now[0])):
        old, new = at[0].get(agent), now[0].get(agent)
        rows.append(
            (f"preload `{agent}` (bytes)", cell(old), cell(new), change(old, new))
        )
    old, new = at[1], now[1]
    rows.append(
        (
            "the suite (seconds)",
            cell(old, 0, NO_UNION),
            cell(new, 0, NO_UNION),
            ABSENT if old is None or new is None else change(round(old), round(new)),
        )
    )
    for leg in (*LEGS, *other_legs(jobs_at, jobs_now)):
        old, new = jobs_at.get(leg), jobs_now.get(leg)
        rows.append(
            (
                f"`{leg}` leg (minutes)",
                cell(old, 1, NO_RUN),
                cell(new, 1, NO_RUN),
                change(old, new, 1) if old is not None and new is not None else ABSENT,
            )
        )
    for path in sorted(set(at[2]) | set(now[2])):
        old, new = at[2].get(path), now[2].get(path)
        rows.append((f"`{path}` (bytes)", cell(old), cell(new), change(old, new)))
    lines = [
        f"### Against {tag}",
        "",
        HEADER,
        "",
        f"| What | {tag} | Now | Change |",
        "|---|---|---|---|",
    ]
    lines += ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join(lines) + "\n"


def reading(root, kernel, priced=None):
    """`(preloads, seconds, documents)` of the tree at `root`, the seconds
    being what the union `priced` sums to, None where there is no union; or
    Unreadable."""
    if not os.path.isdir(root):
        raise Unreadable(f"{root} is no directory")
    seconds = None if priced is None else sum(priced.values())
    return preloads(root, kernel), seconds, documents(root)


def main(argv=None):
    """Read both trees and both job lists, print the table; exit 0 whatever
    it shows, 2 where a tree cannot be read."""
    parser = argparse.ArgumentParser(description=__doc__.partition("\n")[0])
    parser.add_argument("--against", required=True, metavar="TAG")
    parser.add_argument("--at", required=True, metavar="DIR")
    parser.add_argument("--root", default=ROOT, metavar="DIR")
    parser.add_argument("--ci-jobs", metavar="FILE")
    parser.add_argument("--ci-jobs-at", metavar="FILE")
    parser.add_argument("--durations", metavar="FILE")
    parser.add_argument("--durations-at", metavar="FILE")
    args = parser.parse_args(argv)
    try:
        priced_at = durations(args.durations_at)
        priced_now = durations(args.durations)
        kernel = meter()
        at = reading(os.path.abspath(args.at), kernel, priced_at)
        now = reading(os.path.abspath(args.root), kernel, priced_now)
        at_floor = floor()
    except Unreadable as error:
        sys.stderr.write(f"release-report: {error}. Nothing was compared.\n")
        return 2
    jobs_at = leg_minutes(args.ci_jobs_at, at_floor)
    jobs_now = leg_minutes(args.ci_jobs, at_floor)
    rows = module_rows(priced_at, priced_now)
    sys.stdout.write(table(args.against, at, now, jobs_at, jobs_now))
    sys.stdout.write("\n" + files_table(args.against, rows))
    return 0


if __name__ == "__main__":
    # `lib/console.py#STREAMS` owns this answer. The loop is spelt here
    # rather than imported because this script loads the tree's modules only
    # when first asked (`module`), so an absent module ends in
    # `lib/sibling.py`'s sentence and exit 2 after the arguments are read.
    for _name, _errors in (
        ("stdin", "replace"),
        ("stdout", "replace"),
        ("stderr", "backslashreplace"),
    ):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)
    sys.exit(main())
