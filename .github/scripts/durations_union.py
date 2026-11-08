#!/usr/bin/env python3
"""Union the Windows shards' durations parts into one file, and report it (#931).

Every Windows shard of `.github/workflows/test.yml` runs with
`--store-durations --clean-durations`, so pytest-split writes that shard's own
session -- its group, and nothing else -- to `.test_durations`, and the shard
uploads it as a part. The `durations` job downloads the parts, each into a
directory of its own under one directory, and runs this:

  durations_union.py --parts DIR --count K --committed FILE --out FILE
                     [--stale-fails]

It reads every file under `--parts` as one part, refuses unless there are
exactly `--count` of them, unions them into `--out` -- keys sorted, four-space
indent, LF line ends, the shape pytest-split writes -- and reports the union
against `--committed`, the file the tree holds. The report goes to
`$GITHUB_STEP_SUMMARY` when that is set and to stdout otherwise.

**The verdict on the committed file's age is asked, never assumed (#1444).**
`staleness` reads the union against the committed file once: the union's
cases the file gives no price, which pytest-split prices at the file's mean,
and the file's entries no part ran, which the division never reads but the
file's sum still counts. The report prints both shares from that reading.
With `--stale-fails`, which the job passes only on the release pull request,
the script then fails when more than `STALE_SHARE` of the union's cases are
unpriced or more than `STALE_SHARE` of the file's seconds are dead, and its
sentence, on stderr and in the summary, names the counts, the shares, the
first ids of each side and the refresh `REMEDY` states. The union is written
and reported first, because it is the file the refresh commits.

**The union is the whole suite or nothing.** A part missing, an id in two
parts, a part or committed file that does not parse as a durations map, an
empty part, or a `--count` below one, and the script writes nothing and
exits 2, saying which. A shard
killed at its `timeout` uploads no part or the committed file whole, and
either way the parts no longer make the suite; a smaller file uploaded as the
whole would price every case it lost at the mean on the next division.

The report names parts by their directory under `--parts`, which in CI is the
artifact's name, and never prints a path of the machine it ran on. A shard's
*measured seconds* is the sum of its part, every case's setup, call and
teardown as pytest-split adds them, summed over the xdist workers; the spread
is the slowest part's seconds over the parts' mean, the reading #874's S5 took.

Exit codes: 0 wrote the union, and the committed file is within the share or
the verdict was not asked; 1 wrote the union, and the committed file is past
the share; 2 refused and wrote nothing.

The standard library only, at the floor `.github/scripts/run_tests.py#FLOOR`
states, which is the Python the job installs.
"""

import argparse
import json
import os
import statistics
import sys
from typing import NamedTuple

# The share the committed file may be out of date by before the verdict
# fails, one in twenty, read two ways under the one constant: of the union's
# cases unpriced, and of the file's seconds in entries no part ran
# (`questions.md` Q1 of work item 1791852613 set the value; work item
# 1791876667 added the seconds side). Every id is one spelling on every
# machine -- a path is written with `/` (`tests/conftest.py#posix_id`) and no
# id carries the interpreter's path -- so a file measured on Windows prices
# the whole collection on every leg. It bounds the file's age, not the
# shards' imbalance: how far an unpriced case's real cost sits from the mean
# is what each leg's `--durations=50` table and `timeout` hold.
STALE_SHARE = 0.05

# What the red verdict tells whoever prepares the release to do. `gh run
# download` will not write over a file that is already there (it exits 1,
# `file exists`, measured on run 38475370013), so the artifact goes to a
# directory of its own and is moved over the committed file. The release
# branch takes no direct push, so the refresh reaches it by a pull request,
# and a change that is no work item carries the trailer
# (`docs/checks/the-routing-check.md` *At the pull request*).
REMEDY = (
    "Refresh it from this run's `test-durations` artifact: "
    "`gh run download <run id> -n test-durations -D <dir>`, then move "
    "<dir>/.test_durations over the committed .test_durations and commit it "
    "alone, with the trailer `Seal-Routing: no work item`, on a branch cut "
    "from `release/vX.Y.Z`; the file's line ends are already LF. "
    "A pull request merges that branch into `release/vX.Y.Z`, and "
    "the release pull request's next run reads the refreshed file. "
    "A work item never commits .test_durations "
    "(`CONTRIBUTING.md` *Running the checks*)."
)


class Refusal(Exception):
    """A reason the parts cannot make the whole suite."""


class Staleness(NamedTuple):
    """The union read against the committed file, as `staleness` reads it."""

    unpriced: list
    dead: list
    cases: int
    held: float
    dead_seconds: float

    @property
    def unpriced_share(self):
        """The share of the union's cases the committed file gives no price."""
        return len(self.unpriced) / self.cases

    @property
    def dead_share(self):
        """The share of the committed file's seconds held by entries no part
        ran; nothing, where the file holds no seconds."""
        return self.dead_seconds / self.held if self.held else 0.0


def durations_map(text, what):
    """The `{node id: seconds}` map `text` holds, or `Refusal` naming `what`.

    A map is a JSON object whose keys are strings and whose values are
    non-negative numbers; a boolean is not a number here, although Python
    counts it as one.
    """
    try:
        data = json.loads(text)
    except ValueError as exc:
        raise Refusal(f"{what} does not parse as JSON: {exc}") from None
    if not isinstance(data, dict):
        raise Refusal(f"{what} is not a JSON object of node ids and seconds")
    for node, seconds in data.items():
        if (
            isinstance(seconds, bool)
            or not isinstance(seconds, (int, float))
            or seconds < 0
        ):
            raise Refusal(
                f"{what} prices {node!r} at {seconds!r}, which is not a number "
                "of seconds"
            )
    return data


def read_map(path, what):
    """`durations_map` of the file at `path`."""
    try:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
    except (OSError, UnicodeDecodeError) as exc:
        raise Refusal(f"{what} cannot be read: {exc.__class__.__name__}") from None
    return durations_map(text, what)


def find_parts(directory):
    """`[(label, path)]` for every file under `directory`, sorted by
    label; one that is not a readable part is refused where it is read. A label is the file's directory relative to `directory`, written
    with `/`, or the file's name when it sits in `directory` itself.
    """
    if not os.path.isdir(directory):
        raise Refusal("the parts directory does not exist: no part was downloaded")
    found = []
    for here, dirs, files in os.walk(directory):
        dirs.sort()
        for name in files:
            path = os.path.join(here, name)
            rel = os.path.relpath(here, directory)
            label = name if rel == os.curdir else rel.replace(os.sep, "/")
            found.append((label, path))
    return sorted(found)


def union(parts):
    """The one map the parts make, `parts` being `[(label, map)]`.

    An id in two parts is refused naming both, because the parts of one
    division are disjoint and a duplicate means a part is not a shard's.
    """
    merged, owner, twice = {}, {}, []
    for label, part in parts:
        if not part:
            raise Refusal(f"part {label} prices no case: it is not a shard's session")
        for node, seconds in part.items():
            if node in owner:
                twice.append((node, owner[node], label))
                continue
            owner[node] = label
            merged[node] = seconds
    if twice:
        node, first, second = twice[0]
        raise Refusal(
            f"{len(twice)} ids are in two parts, first {node!r} in {first} and "
            f"{second}: a part holding the whole suite is the committed file, "
            "uploaded by a shard that never wrote its own"
        )
    return merged


def rendered(merged):
    """The union as pytest-split writes a durations file, with LF line ends."""
    return json.dumps(merged, indent=4, sort_keys=True)


def staleness(merged, committed):
    """`Staleness` of `committed` against the union `merged`: the union's ids
    the file gives no price, in the union's order; the file's entries that
    are no id of the union, in the file's order; the union's count of cases;
    the file's seconds; and the seconds of its dead entries.

    An empty union is refused: no share of nothing says the file is fresh.
    """
    if not merged:
        raise Refusal(
            "the union prices no case: there is no suite to read the committed "
            "file against"
        )
    dead = [node for node in committed if node not in merged]
    return Staleness(
        unpriced=[node for node in merged if node not in committed],
        dead=dead,
        cases=len(merged),
        held=sum(committed.values()),
        dead_seconds=sum(committed[node] for node in dead),
    )


def verdict(stale):
    """The sentence the release pull request's run fails with when more than
    `STALE_SHARE` of the union's cases are unpriced in the committed file, or
    more than `STALE_SHARE` of the file's seconds belong to entries no part
    ran, `stale` being `staleness`'s reading; None when neither is over."""
    found, first = [], []
    if stale.unpriced_share > STALE_SHARE:
        found.append(
            f"{len(stale.unpriced):,} of the union's {stale.cases:,} cases "
            f"({stale.unpriced_share:.1%}) have no price in the committed "
            ".test_durations, and pytest-split gives each the file's mean"
        )
        first.append("First unpriced: " + ", ".join(stale.unpriced[:5]) + ".")
    if stale.dead_share > STALE_SHARE:
        found.append(
            f"{stale.dead_seconds:,.1f} s of the file's {stale.held:,.1f} s "
            f"({stale.dead_share:.1%}) belong to {len(stale.dead):,} entries no "
            "part ran, which the file's sum still counts"
        )
        first.append("First dead: " + ", ".join(stale.dead[:5]) + ".")
    if not found:
        return None
    return (
        "; and ".join(found)
        + f" -- over the {STALE_SHARE:.0%} STALE_SHARE allows. "
        + REMEDY
        + " "
        + " ".join(first)
    )


def report(parts, merged, committed, stale):
    """The summary's lines, `parts` being `[(label, map)]` and `stale`
    `staleness`'s reading of `committed` against `merged`."""
    live = sum(merged.values())
    lines = [
        "### The Windows shards' durations, unioned (#931)",
        "",
        f"- entries: {len(merged):,} in the union of {len(parts)} parts, "
        f"{len(committed):,} in the committed file",
        f"- seconds: {live:,.1f} s live, {stale.held:,.1f} s in the committed file",
        f"- unpriced: {len(stale.unpriced):,} of the union's {stale.cases:,} "
        f"cases ({stale.unpriced_share:.2%}) have no price in the committed file",
        f"- dead: {len(stale.dead):,} entries of the committed file are no case "
        f"a part ran, {stale.dead_seconds:,.1f} s "
        f"({stale.dead_share:.2%} of its seconds)",
    ]
    measured = [(label, sum(part.values())) for label, part in parts]
    mean = statistics.mean(seconds for _, seconds in measured)
    for label, part in parts:
        seconds = sum(part.values())
        ratios = [
            part[node] / committed[node] for node in part if committed.get(node, 0) > 0
        ]
        ratio = (
            f"median price {statistics.median(ratios):.2f} x the committed "
            f"file's over {len(ratios):,} cases both price"
            if ratios
            else "no case the committed file also prices"
        )
        lines.append(
            f"- part {label}: {len(part):,} cases, {seconds:,.1f} s measured, {ratio}"
        )
    slowest = max(measured, key=lambda item: item[1])
    lines.append(
        f"- spread: the slowest part, {slowest[0]}, measured "
        f"{slowest[1] / mean if mean else 0:.2f} x the parts' mean of "
        f"{mean:,.1f} s"
    )
    return lines


def emit(lines, env):
    """Append `lines` to `$GITHUB_STEP_SUMMARY` where `env` sets it, or print
    them.
    """
    target = env.get("GITHUB_STEP_SUMMARY")
    text = "\n".join(lines) + "\n"
    if target:
        with open(target, "a", encoding="utf-8") as handle:
            handle.write(text)
    else:
        sys.stdout.write(text)


def arguments(argv):
    """The command line, parsed."""
    parser = argparse.ArgumentParser(
        description="Union the Windows shards' durations parts (#931)."
    )
    parser.add_argument("--parts", required=True)
    parser.add_argument("--count", required=True, type=int)
    parser.add_argument("--committed", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument(
        "--stale-fails",
        action="store_true",
        help="exit 1 when the committed file is past STALE_SHARE",
    )
    return parser.parse_args(argv)


def main(argv=None, env=None):
    """Exit 0 having written the union and its report, 1 having written them
    where `--stale-fails` asks the verdict and the committed file is past the
    share, or 2 having written nothing but the reason.
    """
    args = arguments(argv)
    env = os.environ if env is None else env
    try:
        if args.count < 1:
            raise Refusal(f"--count is {args.count}: a union of no parts is no suite")
        found = find_parts(args.parts)
        if len(found) != args.count:
            labels = ", ".join(label for label, _ in found) or "none"
            raise Refusal(
                f"{len(found)} parts were downloaded and --count says "
                f"{args.count} (found: {labels}): a shard that uploaded no "
                "part leaves its group out of the union"
            )
        parts = [(label, read_map(path, f"part {label}")) for label, path in found]
        merged = union(parts)
        committed = read_map(args.committed, "the committed file")
        stale = staleness(merged, committed)
    except Refusal as refusal:
        sentence = f"durations_union: {refusal}. Nothing was written."
        sys.stderr.write(sentence + "\n")
        if env.get("GITHUB_STEP_SUMMARY"):
            emit(["### The Windows shards' durations (#931)", "", sentence], env)
        return 2
    out_dir = os.path.dirname(args.out)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(rendered(merged))
    emit(report(parts, merged, committed, stale), env)
    sentence = verdict(stale) if args.stale_fails else None
    if sentence is None:
        return 0
    sentence = f"durations_union: {sentence}"
    sys.stderr.write(sentence + "\n")
    if env.get("GITHUB_STEP_SUMMARY"):
        emit(["", sentence], env)
    return 1


if __name__ == "__main__":
    # A console that cannot encode what this prints kills it with stdout
    # empty; `lib/console.py` owns the reasoning behind these lines.
    for _name, _errors in (
        ("stdin", "replace"),
        ("stdout", "replace"),
        ("stderr", "backslashreplace"),
    ):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)
    sys.exit(main())
