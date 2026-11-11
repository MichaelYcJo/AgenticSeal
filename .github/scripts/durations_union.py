#!/usr/bin/env python3
"""Union the Windows shards' durations parts into one file, and report it.

Every Windows shard of `.github/workflows/test.yml` runs with
`--store-durations --clean-durations`, so pytest-split writes that shard's own
session -- its group, and nothing else -- to `.test_durations`, and the shard
uploads it as a part. The `durations` job downloads the parts, each into a
directory of its own under one directory, and runs this:

  durations_union.py --parts DIR --count K --out FILE

It reads every file under `--parts` as one part, refuses unless there are
exactly `--count` of them, unions them into `--out` -- keys sorted, four-space
indent, LF line ends, the shape pytest-split writes -- and reports the union.
The report goes to `$GITHUB_STEP_SUMMARY` when that is set and to stdout
otherwise. The job uploads the union as the `test-durations` artifact and,
on a run that is no pull request's, saves it to the cache every split shard
restores before it divides. No file's age is read: the union is
measured on every run, and pytest-split prices only the cases it collects.

**The union is the whole suite or nothing.** A part missing, an id in two
parts, a part that does not parse as a durations map, an empty part, or a
`--count` below one, and the script writes nothing and exits 2, saying
which. A shard killed at its `timeout` uploads no part or the union it
restored, whole, and either way the parts no longer make the suite; a
smaller file uploaded as the whole would price every case it lost at the
mean on the next division.

The report names parts by their directory under `--parts`, which in CI is the
artifact's name, and never prints a path of the machine it ran on. A shard's
*measured seconds* is the sum of its part, every case's setup, call and
teardown as pytest-split adds them, summed over the xdist workers; the spread
is the slowest part's seconds over the parts' mean.
A count split, where no shard restored a union, widens the spread.

Exit codes: 0 wrote the union and its report; 2 refused and wrote nothing.

The standard library only, at the floor `.github/scripts/run_tests.py#FLOOR`
states, which is the Python the job installs.
"""

import argparse
import json
import os
import statistics
import sys


class Refusal(Exception):
    """A reason the parts cannot make the whole suite."""


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
            f"{second}: a part holding the whole suite is the union the shard "
            "restored, uploaded by a shard that never wrote its own"
        )
    return merged


def rendered(merged):
    """The union as pytest-split writes a durations file, with LF line ends."""
    return json.dumps(merged, indent=4, sort_keys=True)


def report(parts, merged):
    """The summary's lines, `parts` being `[(label, map)]` and `merged`
    their union."""
    lines = [
        "### The Windows shards' durations, unioned (#931)",
        "",
        f"- entries: {len(merged):,} in the union of {len(parts)} parts",
        f"- seconds: {sum(merged.values()):,.1f} s live",
    ]
    measured = [(label, sum(part.values())) for label, part in parts]
    mean = statistics.mean(seconds for _, seconds in measured)
    for label, part in parts:
        lines.append(
            f"- part {label}: {len(part):,} cases, {sum(part.values()):,.1f} s measured"
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
    parser.add_argument("--out", required=True)
    return parser.parse_args(argv)


def main(argv=None, env=None):
    """Exit 0 having written the union and its report, or 2 having written
    nothing but the reason.
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
    emit(report(parts, merged), env)
    return 0


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
