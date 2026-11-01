#!/usr/bin/env python3
"""release-report — one table of the release against the last release tag.

  release_report.py --against TAG --at DIR [--root DIR]
                    [--ci-jobs FILE] [--ci-jobs-at FILE]

Prints one markdown table, `| What | <TAG> | Now | Change |`, under
`### Against <TAG>`: each agent's preload bytes, the suite's seconds, each CI
leg's minutes and each document's bytes, read from the tree at `--at` (the
tag's) and the tree at `--root` (this one, by default the repository this
script is in). The tests workflow runs it after the suite on a pull request
into `main` and appends what it prints to the job's summary.

  preload `<agent>`   the bytes of `agents/<agent>.md` and of each skill its
                      `skills:` list names, the agent's own share of
                      `skills/verify/scripts/payload_meter.py#composition`
  the suite           the seconds `.test_durations` prices every case at
  `<leg>` leg         the minutes of one run's `pytest (<leg>-latest, …)`
                      jobs, summed, each `completed_at` less `started_at`,
                      read from a job list as `gh api …/jobs --paginate
                      --jq '.jobs[]'` prints it; `no run found` where the
                      file is absent, empty or holds no such job
  `<document>`        the bytes of the core (`skills/core/SKILL.md`),
                      `CLAUDE.md`, `CONTRIBUTING.md` and each `docs/*.md`,
                      each CRLF counted as the LF git stores

Under it, a second table under `### Test files against <TAG>` gives one row
per test file `.test_durations` prices in either tree: its cases and seconds
at the tag and now, slowest now first.

It fails nothing: no row is held to a number, and its reader is whoever
prepares the release. A leg's minutes compare one run with one run, which
swing on the same code, and the table's header says so.

Exit codes: **0** the table was printed, whatever it shows · **2** a tree,
its `.test_durations`, an agent definition, or the meter it reads through
cannot be read.
"""

import argparse
import datetime
import glob
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
METER = os.path.join(ROOT, "skills", "verify", "scripts", "payload_meter.py")
DURATIONS = ".test_durations"
DOCUMENTS = ("skills/core/SKILL.md", "CLAUDE.md", "CONTRIBUTING.md", "docs/*.md")
# The legs of the tests workflow, in the order a reader compares them, and
# the name of a pytest job, whose leg is the operating system it opens with.
LEGS = ("ubuntu", "windows", "macos")
PYTEST_JOB = re.compile(r"pytest \(([a-z]+)-[^,)]*(?:,.*)?\)")
NO_RUN = "no run found"
ABSENT = "—"
HEADER = (
    "Each agent's preload, the suite's seconds, each CI leg's minutes and "
    "each document's size, at the last release tag and now. Nothing here "
    "fails: a leg's minutes compare one run with one run, which swing on the "
    "same code, so no row is a verdict."
)
FILES_HEADER = (
    "Each test file's priced cases and seconds in `.test_durations`, at the "
    "last release tag and now, slowest now first. A report and never a "
    "ceiling: a heavily exercised module needs the cases it needs."
)


class Unreadable(Exception):
    """A tree or a file the table reads could not be read, and the sentence
    says which."""


def meter():
    """`payload_meter.py`, loaded by path, or Unreadable."""
    if not os.path.isfile(METER):
        raise Unreadable(
            "cannot read skills/verify/scripts/payload_meter.py, which measures "
            "an agent's preload"
        )
    spec = importlib.util.spec_from_file_location("agentic_release_meter", METER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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


def suite_seconds(root):
    """The seconds `.test_durations` in the tree at `root` prices every case
    at, summed, or Unreadable."""
    return sum(durations(root).values())


def durations(root):
    """`.test_durations` in the tree at `root`, `{case id: seconds}`, or
    Unreadable."""
    path = os.path.join(root, DURATIONS)
    try:
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, ValueError) as error:
        raise Unreadable(f"{DURATIONS} under {root} cannot be read: {error}") from None
    if not isinstance(data, dict) or not all(
        isinstance(v, (int, float)) and not isinstance(v, bool) for v in data.values()
    ):
        raise Unreadable(
            f"{DURATIONS} under {root} is no object of case ids to seconds"
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
    """One table row per test file `.test_durations` prices in the tree at
    `at` or the tree at `now`: its cases and seconds in each, slowest now
    first, a file absent from one tree shown absent there."""
    old, new = by_file(durations(at)), by_file(durations(now))

    def slowest(path):
        return (-new.get(path, (0, 0.0))[1], -old.get(path, (0, 0.0))[1], path)

    rows = []
    for path in sorted(set(old) | set(new), key=slowest):
        cells = [f"`{path}`"]
        for side in (old, new):
            cases, seconds = side.get(path, (None, None))
            cells += [cell(cases), cell(seconds, 1)]
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
    `docs/*.md` in the tree at `root`, each path written with `/`."""
    out = {}
    for pattern in DOCUMENTS:
        for path in sorted(glob.glob(os.path.join(root, *pattern.split("/")))):
            if os.path.isfile(path):
                out[os.path.relpath(path, root).replace(os.sep, "/")] = lf_bytes(path)
    return out


def leg_minutes(path):
    """`{leg: minutes}` for one run's job list at `path`, the minutes of a
    leg summed over its pytest jobs; `{}` where there is no such file, it is
    empty, or a line of it is no job. A job with no start or end time is not
    counted, and a leg none of whose jobs has both is no reading."""
    if not path or not os.path.isfile(path):
        return {}
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
            legs[match.group(1)] = legs.get(match.group(1), 0) + minutes
    return legs


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
    rows.append(
        (
            "the suite (seconds)",
            cell(at[1]),
            cell(now[1]),
            change(round(at[1]), round(now[1])),
        )
    )
    for leg in LEGS:
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


def reading(root, kernel):
    """`(preloads, seconds, documents)` of the tree at `root`, or Unreadable."""
    if not os.path.isdir(root):
        raise Unreadable(f"{root} is no directory")
    return preloads(root, kernel), suite_seconds(root), documents(root)


def main(argv=None):
    """Read both trees and both job lists, print the table; exit 0 whatever
    it shows, 2 where a tree cannot be read."""
    parser = argparse.ArgumentParser(description=__doc__.partition("\n")[0])
    parser.add_argument("--against", required=True, metavar="TAG")
    parser.add_argument("--at", required=True, metavar="DIR")
    parser.add_argument("--root", default=ROOT, metavar="DIR")
    parser.add_argument("--ci-jobs", metavar="FILE")
    parser.add_argument("--ci-jobs-at", metavar="FILE")
    args = parser.parse_args(argv)
    try:
        kernel = meter()
        at = reading(os.path.abspath(args.at), kernel)
        now = reading(os.path.abspath(args.root), kernel)
    except Unreadable as error:
        sys.stderr.write(f"release-report: {error}. Nothing was compared.\n")
        return 2
    jobs_at, jobs_now = leg_minutes(args.ci_jobs_at), leg_minutes(args.ci_jobs)
    rows = module_rows(os.path.abspath(args.at), os.path.abspath(args.root))
    sys.stdout.write(table(args.against, at, now, jobs_at, jobs_now))
    sys.stdout.write("\n" + files_table(args.against, rows))
    return 0


if __name__ == "__main__":
    # `hooks/lib/console.py#STREAMS` owns this answer. The loop is spelt here
    # rather than imported because this script loads the tree's modules only
    # when first asked (`meter`), so a module that will not load ends in the
    # script's own `Unreadable` and exit 2.
    for _name, _errors in (
        ("stdin", "replace"),
        ("stdout", "replace"),
        ("stderr", "backslashreplace"),
    ):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)
    sys.exit(main())
