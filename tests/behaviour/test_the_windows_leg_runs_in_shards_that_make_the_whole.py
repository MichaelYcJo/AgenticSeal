"""The Windows leg runs in shards whose union is the whole suite (#841).

The Windows leg runs in four shards (#841); ubuntu and macOS each run as
one job. macOS's whole suite finishes inside the slowest Windows shard, so a
shard of it would shorten no run (#1486).

`pytest-split` divides the suite by each case's duration, read from the
`.test_durations` the shard restored from the cache before its pytest line,
and every shard runs the group its matrix entry names. Where no cache
matches, the file is absent and `pytest-split` divides by count, which
unbalances the shards and drops no case. The file is measured on the
Windows leg and divides it alone, and no id carries the interpreter's path,
a key no other runner writes.
What decides whether a leg's union is the suite is the matrix itself: a
group named twice runs twice and a group named by no entry runs nowhere, and
nothing on the runner says so -- each shard passes. So the matrix is read
here, as `tests/workflows.py#load` parses it, and a matrix whose entries
would not be its jobs is refused: `include:` is the matrix's only key, every
entry of a sharded system is a shard of that system's count `K` in
`SHARDED`, its groups are exactly 1 to `K` once each, every other entry
carries no split, and the pytest line hands the split to pytest.

Every run measures the file as well (#931). Each Windows entry carries
`store`, the pytest line hands it to pytest after the split, and pytest-split
then writes that shard's own session to `.test_durations`; a step uploads it
as the shard's part, and the `durations` job unions the four parts through
`.github/scripts/durations_union.py` into the `test-durations` artifact. A
part nobody uploads, or one that is the union the shard restored, makes a
union that is not the suite, so the cases below hold the entries, the line,
the step and the job to that shape, and `tests/github/test_durations_union.py`
drives the script over fixture parts.

The union is kept in `actions/cache`, not in the tree (#1486). A run that is
no pull request's saves it under a key of its own, and each split shard
restores the newest key that shares its prefix; no file ages, because every
push to `main` writes a new one, and pytest-split prices only the cases it
collects. The cases below hold the save and the restore to one path, one
prefix and one cross-system flag, since a cache saved on ubuntu restores on
Windows only where both steps set it.
"""

import os
import re
import sys

import pytest
from conftest import COLLECTED_NODE_IDS, ROOT
from workflows import load

TEST = ".github/workflows/test.yml"
SUITE = os.path.join(ROOT, "tests")

# What a storing shard hands pytest, and the one system whose shards store:
# the file is the Windows leg's (#864 D, #874), so a part priced anywhere
# else would mix two systems' prices in one file.
STORE = "--store-durations --clean-durations"
STORING = "windows-latest"

SPLIT = re.compile(r"--splits (\d+) --group (\d+)")

# Each sharded operating system and its count of shards. A system not named
# here runs the whole suite as one job and carries no split.
SHARDED = {"windows-latest": 4}


def job(name):
    """The `test.yml` job NAME, as `tests/workflows.py#load` reads it."""
    return load(TEST)["jobs"][name]


def matrix_entries():
    """The `pytest` job's `include:` entries, each one job.

    GitHub runs each entry as a job of its own only where `include:` is the
    matrix's only key: beside a base axis an entry is merged into the axis'
    combinations, and an `exclude:` takes combinations away, so three shards
    can become fewer jobs while every entry still reads as a shard. A matrix
    with another key is refused here, naming the keys."""
    matrix = job("pytest")["strategy"]["matrix"]
    assert list(matrix) == ["include"], (
        f"a `matrix:` key beside `include:` changes which jobs the entries "
        f"are: {sorted(matrix)}"
    )
    return matrix["include"]


def test_every_group_of_each_sharded_leg_runs_exactly_once():
    entries = matrix_entries()
    for system, k in SHARDED.items():
        legs = [e for e in entries if e.get("os") == system]
        found = [SPLIT.fullmatch(e.get("split", "")) for e in legs]
        assert legs and all(found), f"a {system} leg that is not a shard: {legs}"
        counts = {int(m.group(1)) for m in found}
        assert counts == {k}, (
            f"the {system} shards say {sorted(counts)} shards, and the leg has {k}"
        )
        groups = sorted(int(m.group(2)) for m in found)
        assert groups == list(range(1, k + 1)), (
            f"{system} groups {groups} of {k}: a group named twice runs twice, "
            "and one named by no entry runs nowhere"
        )
    others = [e for e in entries if e.get("os") not in SHARDED]
    assert others and not any("split" in e for e in others), others


def test_the_pytest_line_hands_the_split_to_pytest():
    """The split, then the store (#931): pytest-split reads both, and the
    store is about the session the split leaves, so it follows it."""
    runs = [
        step["run"]
        for step in job("pytest")["steps"]
        if step.get("run", "").startswith("pytest ")
    ]
    assert len(runs) == 1, runs
    assert runs[0].endswith("${{ matrix.split }} ${{ matrix.store }}"), runs[0]


def test_the_windows_entries_store_and_the_other_entries_do_not():
    """S1 of work item 1791876667. A Windows entry without `store` leaves its
    group out of every union, and a `store` anywhere else prices the file on
    a second system."""
    entries = matrix_entries()
    windows = [e for e in entries if e.get("os") == STORING]
    assert windows, entries
    assert all(e.get("store") == STORE for e in windows), windows
    others = [e for e in entries if e.get("os") != STORING]
    assert others and not any("store" in e for e in others), others


def uploads(steps):
    """`(index, step)` of each of STEPS that uploads an artifact."""
    return [
        (i, step)
        for i, step in enumerate(steps)
        if step.get("uses", "").startswith("actions/upload-artifact@")
    ]


def test_the_upload_step_runs_always_and_only_where_store_is_set():
    """S1. `always()`: a shard with a red case still wrote its part, and
    without it the part is skipped. `matrix.store != ''`: anywhere else the
    file is the union the shard restored, which the union reads as every id
    in two parts. `include-hidden-files`: the action skips a name starting with a
    dot, and uploads nothing. Seven days and `overwrite` (round 1's 🟡 1):
    re-running failed jobs re-runs the `durations` job, which reads every
    part again, so a part is kept as long as the union it makes, and the
    re-run shard's part replaces the one its first attempt uploaded."""
    steps = job("pytest")["steps"]
    (pytest_at,) = [
        i for i, step in enumerate(steps) if "pytest tests/" in step.get("run", "")
    ]
    found = uploads(steps)
    assert len(found) == 1, found
    at, step = found[0]
    assert at > pytest_at, "the part is uploaded before pytest wrote it"
    assert step.get("if") == "always() && matrix.store != ''", step
    fields = step.get("with", {})
    assert fields.get("path") == ".test_durations", fields
    assert fields.get("include-hidden-files") == "true", fields
    assert fields.get("name") == "test-durations-${{ strategy.job-index }}", fields
    assert fields.get("retention-days") == "7", fields
    assert fields.get("overwrite") == "true", fields


def union_step(steps):
    """`(index, options)` of the one of STEPS that runs the union script,
    its options being each `--name` word and the word after it."""
    (at,) = [
        i for i, step in enumerate(steps) if "durations_union.py" in step.get("run", "")
    ]
    words = steps[at]["run"].split()
    assert words[:2] == ["python", ".github/scripts/durations_union.py"], words
    return at, {words[i]: words[i + 1] for i in range(2, len(words) - 1, 2)}


def test_the_durations_job_needs_pytest_and_runs_unless_cancelled():
    """S2. Without `needs: pytest` the job runs before any part exists; with
    `success()`, the default, one red case anywhere loses the run's reading.
    It downloads what the shards uploaded, unions as many parts as entries
    store, and uploads the union as `test-durations`, which the release
    table downloads. S3 of #1486: the union step's command is the parts, the
    count and the output, and nothing reads a file's age."""
    durations = job("durations")
    assert durations.get("needs") == "pytest", durations
    assert durations.get("if") == "${{ !cancelled() }}", durations
    assert durations.get("runs-on") == "ubuntu-latest", durations
    steps = durations["steps"]
    (download,) = [
        step.get("with", {})
        for step in steps
        if step.get("uses", "").startswith("actions/download-artifact@")
    ]
    shard = uploads(job("pytest")["steps"])[0][1].get("with", {})
    pattern = download.get("pattern", "")
    assert pattern.endswith("-*") and shard["name"].startswith(pattern[:-1]), (
        pattern,
        shard["name"],
    )
    assert "merge-multiple" not in download, (
        "merged, the four parts are one `.test_durations` written four times"
    )
    _, opts = union_step(steps)
    assert sorted(opts) == ["--count", "--out", "--parts"], (
        f"the union step passes {sorted(opts)}: a file's age is no input (#1486)"
    )
    stores = [e for e in matrix_entries() if "store" in e]
    assert opts["--count"] == str(len(stores)), (opts, len(stores))
    assert opts["--parts"] == download.get("path"), (opts, download)
    ((_, step),) = uploads(steps)
    out = step.get("with", {})
    assert out.get("name") == "test-durations", out
    assert out.get("path") == opts["--out"], (out, opts)
    assert out.get("include-hidden-files") == "true", out
    assert out.get("overwrite") == "true", (
        "a re-run attempt's union is refused under the name its first attempt uploaded"
    )


def cache_step(steps, action):
    """The one of STEPS that uses `actions/cache/<action>`."""
    (step,) = [
        step
        for step in steps
        if step.get("uses", "").startswith(f"actions/cache/{action}@")
    ]
    return step


# What a run that is no pull request's keeps its union for, and what a pull
# request's keeps it for: the release table downloads the tag's push run's
# union (#1486 S4).
RETENTION = "${{ github.event_name == 'pull_request' && 7 || 90 }}"


def test_a_run_that_is_no_pull_request_saves_the_union_and_each_split_shard_restores_it():
    """S4 of #1486. The `durations` job saves the union it wrote to the
    cache on every run that is no pull request's, under a key of its own per
    attempt, since a key is immutable; a pull request's cache would reach no
    other pull request. Each split shard restores, before its pytest line,
    the newest key the save's prefix opens. Both steps name one path and set
    the cross-system flag, because the save runs on ubuntu and the restore on
    Windows. The upload keeps a push run's union as long as the release
    table reads it."""
    steps = job("durations")["steps"]
    union_at, out = union_step(steps)
    save = cache_step(steps, "save")
    assert steps.index(save) > union_at, "the union is saved before it is written"
    assert "github.event_name != 'pull_request'" in save.get("if", ""), save
    assert f"hashFiles('{out['--out']}') != ''" in save.get("if", ""), save
    ((_, upload),) = uploads(steps)
    assert upload["with"].get("retention-days") == RETENTION, upload

    shards = job("pytest")["steps"]
    restore = cache_step(shards, "restore")
    (pytest_at,) = [
        i for i, step in enumerate(shards) if step.get("run", "").startswith("pytest ")
    ]
    assert shards.index(restore) < pytest_at, "the union is restored after the split"
    assert restore.get("if") == "matrix.split != ''", restore
    saved, restored = save["with"], restore["with"]
    assert saved.get("path") == restored.get("path") == out["--out"], (saved, restored)
    prefix = restored.get("restore-keys", "")
    assert prefix and saved.get("key", "").startswith(prefix), (saved, restored)
    assert "github.run_attempt" in saved["key"], saved
    assert saved.get("enableCrossOsArchive") == "true", saved
    assert restored.get("enableCrossOsArchive") == "true", restored


def collects_the_suite(args, invocation_dir, rootdir):
    """True when an invocation collected the whole suite under node ids the
    durations file can be read against: the root is the repository's, so ids
    start `tests/`, and a path it collected (`config.args`, which pytest
    fills with the invocation directory when none was named) is the
    repository or its `tests` directory."""
    if os.path.realpath(rootdir) != os.path.realpath(ROOT):
        return False
    whole = {os.path.realpath(ROOT), os.path.realpath(SUITE)}
    for arg in args:
        if os.path.realpath(os.path.join(str(invocation_dir), str(arg))) in whole:
            return True
    return False


def test_only_the_suite_or_the_repository_is_the_whole_collection():
    assert collects_the_suite(["tests"], ROOT, ROOT)
    assert collects_the_suite(["tests/"], ROOT, ROOT)
    assert collects_the_suite([ROOT], ROOT, ROOT)
    assert collects_the_suite([SUITE], SUITE, ROOT)
    module = os.path.join("tests", "behaviour", os.path.basename(__file__))
    assert not collects_the_suite([module], ROOT, ROOT)
    assert not collects_the_suite([module + "::test_x"], ROOT, ROOT)
    assert not collects_the_suite([SUITE], SUITE, SUITE)


def test_no_collected_id_carries_the_interpreters_path(request):
    """An id holding `sys.executable` is a key no other runner writes, so a
    union measured on one runner leaves it unpriced on a runner whose
    interpreter stands elsewhere."""
    config = request.config
    if not collects_the_suite(
        config.args, config.invocation_params.dir, config.rootpath
    ):
        pytest.skip(
            "the suite was not collected; run `bin/test tests -q -k "
            "test_no_collected_id_carries_the_interpreters_path`"
        )
    collected = getattr(request.session, COLLECTED_NODE_IDS)
    bad = [node for node in collected if sys.executable in node]
    assert not bad, f"{len(bad)} collected ids carry {sys.executable}: {bad[:3]}"
