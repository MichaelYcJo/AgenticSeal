"""The sharded legs run in shards whose union is the whole suite (#841, #864).

The Windows leg runs in four shards (#841) and the macOS leg in three
(#864); ubuntu runs as one job. The file keeps the name it was given when
Windows was the only sharded leg, because the sentence is still true and a
released ledger row anchors its three cases by this path.

`pytest-split` divides the suite by each case's duration, read from the
committed `.test_durations`, and every shard runs the group its matrix entry
names. One file divides both legs, because every leg collects the same
cases under the same ids: an id built from a path writes it with `/`, and
none carries the interpreter's path. What decides whether a leg's union is
the suite is the matrix itself: a group named twice runs twice and a group
named by no entry runs nowhere, and nothing on the runner says so -- each
shard passes. So the matrix is read here, through
`tests/text/test_ci_gives_the_checks_what_they_need.py#
matrix_include_entries`, the suite's one reading of the job's entries,
which refuses a matrix whose entries would not be its jobs: every entry of
a sharded system is a shard of that system's count `K` in `SHARDED`, its
groups are exactly 1 to `K` once each, every other entry carries no split,
and the pytest line hands the split to pytest.

Every run measures the file as well (#931). Each Windows entry carries
`store`, the pytest line hands it to pytest after the split, and pytest-split
then writes that shard's own session to `.test_durations`; a step uploads it
as the shard's part, and the `durations` job unions the four parts through
`.github/scripts/durations_union.py` into the `test-durations` artifact. A
part nobody uploads, or one that is the committed file, makes a union that is
not the suite, so the cases below hold the entries, the line, the step and
the job to that shape, and `tests/github/test_durations_union.py` drives the script
over fixture parts.

The durations file is read too. A file missing from the tree only unbalances
the shards (`pytest-split` then divides by count), but one that does not
parse stops every shard at collection.

Its age is held where it is measured, not here (#874, #931, #1444). A case
added since the last refresh has no price in the file, `pytest-split` gives
it the file's mean, and the shards drift apart with nothing saying so; a
case removed since leaves its entry behind, which the division never reads
but the file's sum still counts. The release pull request's `durations` job
is red when either share is past the script's `STALE_SHARE`, which is the
whole schedule of the refresh, so no work item commits the file and no case
here reads it against the collection. The case below holds the workflow to
asking that verdict on that pull request alone.
"""

import json
import os
import re
import sys

import pytest
from conftest import COLLECTED_NODE_IDS, ROOT, _unquote, workflow_steps
from test_ci_gives_the_checks_what_they_need import (
    jobs,
    matrix_include_entries,
    read,
)

DURATIONS = os.path.join(ROOT, ".test_durations")
SUITE = os.path.join(ROOT, "tests")

# What a storing shard hands pytest, and the one system whose shards store:
# the file is the Windows leg's (#864 D, #874), so a part priced anywhere
# else would mix two systems' prices in one file.
STORE = "--store-durations --clean-durations"
STORING = "windows-latest"

SPLIT = re.compile(r"--splits (\d+) --group (\d+)")

# Each sharded operating system and its count of shards. A system not named
# here runs the whole suite as one job and carries no split.
SHARDED = {"windows-latest": 4, "macos-latest": 3}


def test_every_group_of_each_sharded_leg_runs_exactly_once():
    entries = matrix_include_entries(read("test.yml"))
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
        ln.strip()
        for ln in jobs(read("test.yml"))["pytest"].splitlines()
        if ln.strip().startswith("- run: pytest ")
    ]
    assert len(runs) == 1, runs
    assert runs[0].endswith("${{ matrix.split }} ${{ matrix.store }}"), runs[0]


def test_the_windows_entries_store_and_the_other_entries_do_not():
    """S1 of work item 1791876667. A Windows entry without `store` leaves its
    group out of every union, and a `store` anywhere else prices the file on
    a second system."""
    entries = matrix_include_entries(read("test.yml"))
    windows = [e for e in entries if e.get("os") == STORING]
    assert windows, entries
    assert all(e.get("store") == STORE for e in windows), windows
    others = [e for e in entries if e.get("os") != STORING]
    assert others and not any("store" in e for e in others), others


def job_steps(job):
    """`[(name, code lines)]` for each step of the `test.yml` job `job`."""
    return workflow_steps(jobs(read("test.yml"))[job])


def step_fields(block):
    """`{key: value}` of every `key: value` line in one step, its `with:`
    keys among them, a leading `- ` off and quotes off the value."""
    fields = {}
    for line in block.splitlines():
        m = re.match(r"^\s*(?:-\s+)?([A-Za-z0-9_-]+):\s*(\S.*?)\s*$", line)
        if m:
            fields[m.group(1)] = _unquote(m.group(2))
    return fields


def uploads(job):
    """`(index, fields)` of each step of `job` that uploads an artifact."""
    return [
        (i, step_fields(block))
        for i, (_, block) in enumerate(job_steps(job))
        if "uses: actions/upload-artifact@" in block
    ]


def test_the_upload_step_runs_always_and_only_where_store_is_set():
    """S1. `always()`: a shard with a red case still wrote its part, and
    without it the part is skipped. `matrix.store != ''`: anywhere else the
    file is the committed one, which the union reads as every id in two
    parts. `include-hidden-files`: the action skips a name starting with a
    dot, and uploads nothing. Seven days and `overwrite` (round 1's 🟡 1):
    re-running failed jobs re-runs the `durations` job, which reads every
    part again, so a part is kept as long as the union it makes, and the
    re-run shard's part replaces the one its first attempt uploaded."""
    steps = job_steps("pytest")
    (pytest_at,) = [
        i for i, (_, block) in enumerate(steps) if "run: pytest tests/" in block
    ]
    found = uploads("pytest")
    assert len(found) == 1, found
    at, fields = found[0]
    assert at > pytest_at, "the part is uploaded before pytest wrote it"
    assert fields.get("if") == "always() && matrix.store != ''", fields
    assert fields.get("path") == ".test_durations", fields
    assert fields.get("include-hidden-files") == "true", fields
    assert fields.get("name") == "test-durations-${{ strategy.job-index }}", fields
    assert fields.get("retention-days") == "7", fields
    assert fields.get("overwrite") == "true", fields


def job_keys(job):
    """`{key: value}` of the `test.yml` job's own one-line keys."""
    keys = {}
    for line in jobs(read("test.yml"))[job].splitlines():
        m = re.match(r"^    ([A-Za-z0-9_-]+):\s*(\S.*?)\s*$", line)
        if m:
            keys[m.group(1)] = _unquote(m.group(2))
    return keys


def test_the_durations_job_needs_pytest_and_runs_unless_cancelled():
    """S2. Without `needs: pytest` the job runs before any part exists; with
    `success()`, the default, one red case anywhere loses the run's reading.
    It downloads what the shards uploaded, unions as many parts as entries
    store, and uploads the union under the name the remedy downloads."""
    keys = job_keys("durations")
    assert keys.get("needs") == "pytest", keys
    assert keys.get("if") == "${{ !cancelled() }}", keys
    assert keys.get("runs-on") == "ubuntu-latest", keys
    steps = [step_fields(block) for _, block in job_steps("durations")]
    (download,) = [
        s for s in steps if s.get("uses", "").startswith("actions/download-artifact@")
    ]
    (_, shard) = uploads("pytest")[0]
    pattern = download.get("pattern", "")
    assert pattern.endswith("-*") and shard["name"].startswith(pattern[:-1]), (
        pattern,
        shard["name"],
    )
    assert "merge-multiple" not in download, (
        "merged, the four parts are one `.test_durations` written four times"
    )
    (union,) = [s for s in steps if "durations_union.py" in s.get("run", "")]
    words = union["run"].removesuffix(" " + ASK_THE_VERDICT).split()
    opts = {words[i]: words[i + 1] for i in range(2, len(words) - 1, 2)}
    stores = [e for e in matrix_include_entries(read("test.yml")) if "store" in e]
    assert opts.get("--count") == str(len(stores)), (opts, len(stores))
    assert opts.get("--parts") == download.get("path"), (opts, download)
    assert opts.get("--committed") == ".test_durations", opts
    ((_, out),) = uploads("durations")
    assert out.get("name") == "test-durations", out
    assert out.get("path") == opts.get("--out"), (out, opts)
    assert out.get("include-hidden-files") == "true", out
    assert out.get("retention-days") == "7", out
    assert out.get("overwrite") == "true", (
        "a re-run attempt's union is refused under the name its first attempt uploaded"
    )


# The words that end the union step's line: the verdict on the committed
# file's age is asked on a pull request into `main` and on no other run.
ASK_THE_VERDICT = "${{ github.base_ref == 'main' && '--stale-fails' || '' }}"


def test_the_verdict_is_asked_into_main_alone_and_the_upload_outlives_it():
    """S4 of work item 1794178397. Only the release pull request's run asks
    the verdict, so no work item's run is red on the file's age. A red
    verdict has written the union first, and the upload runs where the union
    file exists rather than where the step succeeded, so the red run still
    carries the file the release's refresh commits; a refusal writes
    nothing, and nothing is uploaded."""
    steps = job_steps("durations")
    (union_at,) = [
        i for i, (_, block) in enumerate(steps) if "durations_union.py" in block
    ]
    run = step_fields(steps[union_at][1])["run"]
    assert run.endswith(" " + ASK_THE_VERDICT), run
    assert jobs(read("test.yml"))["durations"].count("--stale-fails") == 1, (
        "the verdict is asked outside the condition"
    )
    ((at, out),) = uploads("durations")
    assert at > union_at, "the union is uploaded before it is written"
    written = f"hashFiles('{out.get('path')}') != ''"
    assert out.get("if") == "${{ !cancelled() && " + written + " }}", out


def test_the_durations_file_parses_and_names_cases():
    with open(DURATIONS, encoding="utf-8") as handle:
        durations = json.load(handle)
    assert durations, "the durations file is empty"
    bad = [
        node
        for node, seconds in durations.items()
        if not node.startswith("tests/")
        or "::" not in node
        or not isinstance(seconds, (int, float))
        or seconds < 0
    ]
    assert not bad, bad[:5]


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
    """An id holding `sys.executable` is a key no other machine writes, so
    every refresh would leave it unpriced on every leg but the one measured."""
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


# --- the words a contributor acts on (#931) -----------------------------------


def section(path, heading):
    """The text of `path` under the `## ` heading `heading`, up to the next
    `## ` heading."""
    with open(os.path.join(ROOT, path), encoding="utf-8") as handle:
        text = handle.read()
    head = f"\n## {heading}\n"
    assert head in text, f"{path} has no `## {heading}`"
    return text.split(head, 1)[1].split("\n## ", 1)[0]


def test_the_recipe_names_the_artifact_and_the_checklist_has_no_box():
    """S5 of work item 1794178397. The paragraph whoever prepares the
    release meets when the release pull request's `durations` job goes red
    names that job as the schedule, the artifact and the download that works
    -- into a directory of its own, because `gh` will not overwrite -- the
    no-work-item pull request into the release branch that lands it, the
    limit for a shard past its timeout, and that no work item commits the
    file; and nothing of the per-branch refresh it replaced. The release
    checklist has no refresh box: a box a person ticks was the schedule
    0.21.1 skipped (#931)."""
    running = section("CONTRIBUTING.md", "Running the checks")
    (recipe,) = [p for p in running.split("\n\n") if "goes stale" in p]
    flat = " ".join(recipe.split())
    for said in (
        "A work item never commits `.test_durations`",
        "the release pull request's `durations` job",
        "on a pull request into `main`, and on no other run",
        "`STALE_SHARE`",
        "entries no shard ran",
        "`test-durations`",
        "`gh run download <run id> -n test-durations -D <dir>`",
        "over the committed file and commits it alone",
        "`Seal-Routing: no work item`",
        "on a branch cut from `release/vX.Y.Z`",
        "A pull request merges that branch into `release/vX.Y.Z`",
        "the newest run whose `durations` job wrote the union",
    ):
        assert said in flat, f"the recipe paragraph does not say {said}"
    # The per-branch refresh's own words: the branch's run, its re-run and
    # its dispatch, and the suite case that scheduled it.
    for gone in (
        "the branch's latest",
        "gh run rerun",
        "gh workflow run",
        "prices_the_suite",
    ):
        assert gone not in flat, f"the recipe paragraph still says {gone!r}"
    before = section("docs/releasing/release-checklist.md", "0. Before starting")
    assert ".test_durations" not in before, "the checklist still has a refresh box"
