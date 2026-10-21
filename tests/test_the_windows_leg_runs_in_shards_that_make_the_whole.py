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
`tests/test_ci_gives_the_checks_what_they_need.py#
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
the job to that shape, and drive the script over fixture parts.

The durations file is read too. A file missing from the tree only unbalances
the shards (`pytest-split` then divides by count), but one that does not
parse stops every shard at collection.

And it is held to its age (#874, #931), in both directions, and that is the
whole schedule of its refresh. A case added since the last refresh has no
price in the file, `pytest-split` gives it the file's mean, and the shards
drift apart with nothing saying so: the file went from 3.9 % to 9.4 %
unpriced in five days. A case removed since leaves its entry behind, which
the division never reads but the file's sum still counts. More than
`STALE_SHARE` of the collected cases unpriced, or more than `STALE_SHARE` of
the file's seconds in entries the suite no longer collects, fails the suite
case below, and its sentence names the download that refreshes the file
from the branch's own run.
"""

import importlib.util
import json
import ntpath
import os
import re
import subprocess
import sys

import pytest
from conftest import COLLECTED_NODE_IDS, _unquote, posix_id, workflow_steps
from test_ci_gives_the_checks_what_they_need import (
    jobs,
    matrix_include_entries,
    read,
)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DURATIONS = os.path.join(ROOT, ".test_durations")
SUITE = os.path.join(ROOT, "tests")
UNION_SCRIPT = os.path.join(ROOT, ".github", "scripts", "durations_union.py")

_spec = importlib.util.spec_from_file_location("durations_union", UNION_SCRIPT)
du = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(du)

# What a storing shard hands pytest, and the one system whose shards store:
# the file is the Windows leg's (#864 D, #874), so a part priced anywhere
# else would mix two systems' prices in one file.
STORE = "--store-durations --clean-durations"
STORING = "windows-latest"

SPLIT = re.compile(r"--splits (\d+) --group (\d+)")

# Each sharded operating system and its count of shards. A system not named
# here runs the whole suite as one job and carries no split.
SHARDED = {"windows-latest": 4, "macos-latest": 3}

# The share the durations file may be out of date by before the suite case
# fails, one in twenty, read two ways under the one constant: of the
# collected cases unpriced, and of the file's seconds in entries nobody
# collects (`questions.md` Q1 of work item 1791852613 set the value; work item
# 1791876667 added the seconds side). Every id is one spelling on every
# machine -- a path is written with `/` (`conftest.py#posix_id`) and no id
# carries the interpreter's path -- so a file measured on Windows prices the
# whole collection on every leg. At about 44 cases a pull request the
# unpriced side fails about one release cycle after a refresh; the seconds
# side fails in the pull request that removes a twentieth of the suite's
# time. It bounds the file's age, not the shards' imbalance: how far an
# unpriced case's real cost sits from the mean is what each leg's
# `--durations=50` table and `timeout` hold.
STALE_SHARE = 0.05


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
    words = union["run"].split()
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


def unpriced(collected, durations):
    """The node ids of `collected` that `durations` gives no price, in
    collection order. An entry of `durations` nobody collected is not read.
    An empty collection is refused: no share of nothing says the file is
    fresh."""
    if not collected:
        raise ValueError("an empty collection: there is no suite to price")
    return [node for node in collected if node not in durations]


def dead(collected, durations):
    """The entries of `durations` that are no node id of `collected`, in the
    file's order."""
    live = set(collected)
    return [node for node in durations if node not in live]


# What the failing case tells a contributor to do. `gh run download` will
# not write over a file that is already there (it exits 1, `file exists`,
# measured on run 38475370013), so the artifact goes to a directory of its
# own and is moved over the committed file.
REMEDY = (
    "Refresh it from this branch's latest `tests` run, whose `durations` job "
    "unioned the Windows shards' parts: `gh run download <run id> -n "
    "test-durations -D <dir>`, then move <dir>/.test_durations over the "
    "committed .test_durations and commit it; "
    "the file's line ends are already LF. "
    "A run older than the artifact's seven days is re-run first, with "
    "`gh run rerun <run id>`; a branch with no pull request, or whose run "
    "is too old to re-run, gets one with `gh workflow run test.yml --ref "
    "<branch>` (CONTRIBUTING.md §Running the checks)."
)


def staleness(collected, durations):
    """The sentence the suite case fails with when more than `STALE_SHARE`
    of `collected` is unpriced in `durations`, or more than `STALE_SHARE` of
    the seconds of `durations` belong to entries `collected` does not hold;
    None when neither is over."""
    missing = unpriced(collected, durations)
    share = len(missing) / len(collected)
    gone = dead(collected, durations)
    held = sum(durations.values())
    gone_seconds = sum(durations[node] for node in gone)
    gone_share = gone_seconds / held if held else 0.0
    found, first = [], []
    if share > STALE_SHARE:
        found.append(
            f"{len(missing)} of the {len(collected)} collected cases "
            f"({share:.1%}) have no price in .test_durations, and "
            "pytest-split gives each the file's mean"
        )
        first.append("First unpriced: " + ", ".join(missing[:5]) + ".")
    if gone_share > STALE_SHARE:
        found.append(
            f"{gone_seconds:,.1f} s of the file's {held:,.1f} s "
            f"({gone_share:.1%}) belong to {len(gone)} entries the suite no "
            "longer collects, which the file's sum still counts"
        )
        first.append("First gone: " + ", ".join(gone[:5]) + ".")
    if not found:
        return None
    return (
        "; and ".join(found)
        + f" -- over the {STALE_SHARE:.0%} STALE_SHARE allows. "
        + REMEDY
        + " "
        + " ".join(first)
    )


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


def test_the_durations_file_prices_the_suite(request):
    """The suite's collection against the committed file, read from the
    record `tests/conftest.py#pytest_collection_modifyitems` makes before
    `pytest-split` keeps a shard's group, so every shard reads the whole
    suite. One module named on its own is not the suite, and the case
    declines rather than judging it; `bin/test tests -q -k
    test_the_durations_file_prices_the_suite` runs it alone."""
    config = request.config
    if not collects_the_suite(
        config.args, config.invocation_params.dir, config.rootpath
    ):
        pytest.skip(
            "the suite was not collected, so its collection cannot be read "
            "against .test_durations; run `bin/test tests -q -k "
            "test_the_durations_file_prices_the_suite` from the repository"
        )
    with open(DURATIONS, encoding="utf-8") as handle:
        durations = json.load(handle)
    sentence = staleness(getattr(request.session, COLLECTED_NODE_IDS), durations)
    assert sentence is None, sentence


def _collection(n):
    return [f"tests/test_m.py::test_{i}" for i in range(n)]


# The fixture cases sit at the boundary `STALE_SHARE` draws: on a thousand
# cases, exactly its share unpriced passes and one more fails.
FIXTURE_SIZE = 1000
AT_THE_SHARE = round(STALE_SHARE * FIXTURE_SIZE)


def test_exactly_the_share_unpriced_passes():
    collected = _collection(FIXTURE_SIZE)
    priced = {node: 1.0 for node in collected[AT_THE_SHARE:]}
    assert len(unpriced(collected, priced)) == AT_THE_SHARE
    assert staleness(collected, priced) is None


def test_one_more_unpriced_fails_and_names_the_counts_and_the_recipe():
    """S4 of work item 1791876667: the counts, the share, and the recipe,
    which is the download of the branch's own `test-durations` artifact into
    a directory of its own -- `gh run download` refuses to write over the
    committed file -- the re-run for an artifact past its seven days, and
    the dispatch for a branch with no run to download from (round 1's 🟡 2):
    a branch with no pull request runs `tests` only when dispatched; and the
    file is the one thing the refresh commits."""
    collected = _collection(FIXTURE_SIZE)
    priced = {node: 1.0 for node in collected[AT_THE_SHARE + 1 :]}
    sentence = staleness(collected, priced)
    assert sentence is not None
    assert f"{AT_THE_SHARE + 1} of the {FIXTURE_SIZE} collected cases" in sentence
    assert f"({(AT_THE_SHARE + 1) / FIXTURE_SIZE:.1%})" in sentence
    assert "gh run download <run id> -n test-durations -D <dir>" in sentence
    assert "move <dir>/.test_durations over the committed" in sentence
    assert "over the committed .test_durations and commit it;" in sentence
    assert "gh run rerun <run id>" in sentence
    assert "gh workflow run test.yml --ref <branch>" in sentence
    assert "CONTRIBUTING.md §Running the checks" in sentence
    assert "First unpriced: " + collected[0] in sentence
    assert "First gone" not in sentence, sentence


def test_an_empty_collection_is_refused():
    with pytest.raises(ValueError, match="empty collection"):
        unpriced([], {"tests/test_m.py::test_0": 1.0})


def test_an_entry_nobody_collects_is_not_counted():
    """An entry the suite no longer collects is never an unpriced case: it
    counts toward the seconds the file holds for nobody, and only there. Five
    thousand of them beside a thousand live cases fail the seconds side and
    leave the unpriced side at zero."""
    collected = _collection(FIXTURE_SIZE)
    priced = {node: 1.0 for node in collected}
    priced.update({f"tests/test_gone.py::test_{i}": 1.0 for i in range(5000)})
    assert unpriced(collected, priced) == []
    sentence = staleness(collected, priced)
    assert sentence is not None
    assert "have no price" not in sentence, sentence
    assert "First unpriced" not in sentence, sentence
    assert "belong to 5000 entries the suite no longer collects" in sentence


def _with_gone(n_gone):
    """A collection of `FIXTURE_SIZE - AT_THE_SHARE` cases all priced, and
    `n_gone` entries nobody collects, every entry at one second."""
    collected = _collection(FIXTURE_SIZE - AT_THE_SHARE)
    priced = {node: 1.0 for node in collected}
    priced.update({f"tests/test_gone.py::test_{i}": 1.0 for i in range(n_gone)})
    return collected, priced


def test_dead_seconds_past_the_share_fail_and_at_the_share_pass():
    """S4 of work item 1791876667, the seconds side. A pull request that
    removes a twentieth of the suite's time and keeps the file leaves the
    division unharmed and the file's sum high; at exactly the share of the
    file's seconds it passes, and one entry more fails naming the seconds,
    the share, the count and the first gone entry."""
    collected, priced = _with_gone(AT_THE_SHARE)
    assert sum(priced[n] for n in dead(collected, priced)) == AT_THE_SHARE
    assert staleness(collected, priced) is None
    collected, priced = _with_gone(AT_THE_SHARE + 1)
    sentence = staleness(collected, priced)
    assert sentence is not None
    held = FIXTURE_SIZE + 1
    assert (
        f"{AT_THE_SHARE + 1:,.1f} s of the file's {held:,.1f} s "
        f"({(AT_THE_SHARE + 1) / held:.1%}) belong to {AT_THE_SHARE + 1} "
        "entries the suite no longer collects"
    ) in sentence, sentence
    assert "First gone: tests/test_gone.py::test_0" in sentence, sentence
    assert "gh run download <run id> -n test-durations -D <dir>" in sentence
    assert "have no price" not in sentence, sentence


def test_both_sides_over_are_named_in_one_sentence():
    collected = _collection(FIXTURE_SIZE)
    priced = {node: 1.0 for node in collected[AT_THE_SHARE + 1 :]}
    priced.update({f"tests/test_gone.py::test_{i}": 1.0 for i in range(100)})
    sentence = staleness(collected, priced)
    assert "have no price in .test_durations" in sentence, sentence
    assert "belong to 100 entries the suite no longer collects" in sentence
    assert sentence.count("gh run download") == 1, sentence


def test_an_empty_file_is_all_unpriced_and_nothing_gone():
    """No seconds to share the dead ones over is not a division by zero."""
    sentence = staleness(_collection(FIXTURE_SIZE), {})
    assert "1000 of the 1000 collected cases (100.0%)" in sentence, sentence
    assert "First gone" not in sentence, sentence


def test_only_the_suite_or_the_repository_is_the_whole_collection():
    assert collects_the_suite(["tests"], ROOT, ROOT)
    assert collects_the_suite(["tests/"], ROOT, ROOT)
    assert collects_the_suite([ROOT], ROOT, ROOT)
    assert collects_the_suite([SUITE], SUITE, ROOT)
    module = os.path.join("tests", os.path.basename(__file__))
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


def test_a_path_id_is_written_with_forward_slashes():
    assert posix_id(ntpath.join("agents", "framer.md"), "\\") == "agents/framer.md"
    assert posix_id("agents/framer.md") == "agents/framer.md"
    assert posix_id(None) is None


# --- the union of the parts (#931) ------------------------------------------
#
# Fixture parts in the shape the `durations` job downloads: one directory per
# artifact, each holding the `.test_durations` a shard wrote, with CRLF line
# ends because pytest-split writes in text mode on Windows. Ids are listed
# out of order inside each part and across parts, so a union that kept
# insertion order is not sorted.

PARTS = {
    "test-durations-4": {
        "tests/test_z.py::test_b": 4.0,
        "tests/test_z.py::test_a": 6.0,
    },
    "test-durations-5": {
        "tests/test_m.py::test_b": 10.0,
        "tests/test_a.py::test_c": 20.0,
    },
    "test-durations-6": {
        "tests/test_b.py::test_a": 15.0,
        "tests/test_b.py::test_b": 5.0,
    },
}
# The committed file: every part's cases at half the price, but one case it
# never priced (`test_b.py::test_b`, unpriced by the union) and one the parts
# never ran (`test_gone.py::test_x`, dead, 2 s).
COMMITTED = {
    "tests/test_z.py::test_b": 2.0,
    "tests/test_z.py::test_a": 3.0,
    "tests/test_m.py::test_b": 5.0,
    "tests/test_a.py::test_c": 10.0,
    "tests/test_b.py::test_a": 7.5,
    "tests/test_gone.py::test_x": 2.0,
}


def write_parts(tmp_path, parts=None, committed=None):
    """`(parts dir, committed path, out path)` with `parts` written as the
    job downloads them, and `committed` as the tree holds it. A part or a
    committed file given as `str` or `bytes` is written as it is."""

    def raw(value):
        if isinstance(value, bytes):
            return value
        text = value if isinstance(value, str) else json.dumps(value, indent=4)
        return text.replace("\n", "\r\n").encode("utf-8")

    root = tmp_path / "parts"
    for label, part in (PARTS if parts is None else parts).items():
        (root / label).mkdir(parents=True)
        (root / label / ".test_durations").write_bytes(raw(part))
    held = tmp_path / "committed.json"
    held.write_bytes(raw(COMMITTED if committed is None else committed))
    return root, held, tmp_path / "union" / ".test_durations"


def run_union(root, held, out, count, summary=None):
    """`main`'s exit code, the arguments being the job's."""
    env = {} if summary is None else {"GITHUB_STEP_SUMMARY": str(summary)}
    argv = ["--parts", str(root), "--count", str(count)]
    argv += ["--committed", str(held), "--out", str(out)]
    return du.main(argv, env)


def test_the_union_of_the_parts_is_the_whole_sorted_with_lf(tmp_path):
    """S2. Every part's ids, each once, sorted, LF, in the shape pytest-split
    writes, so the committed file's diff is the prices and nothing else. Run
    as the job runs it, as a process, so the entry point is the one driven."""
    root, held, out = write_parts(tmp_path)
    args = ["--parts", str(root), "--count", "3"]
    args += ["--committed", str(held), "--out", str(out)]
    run = subprocess.run(
        [sys.executable, UNION_SCRIPT, *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        env={k: v for k, v in os.environ.items() if k != "GITHUB_STEP_SUMMARY"},
        timeout=60,
    )
    assert run.returncode == 0, run.stderr
    raw = out.read_bytes()
    assert b"\r" not in raw, "the union carries CRLF line ends"
    union = json.loads(raw)
    whole = {node: s for part in PARTS.values() for node, s in part.items()}
    assert union == whole, union
    assert list(union) == sorted(whole), list(union)
    assert raw.decode("utf-8") == json.dumps(whole, indent=4, sort_keys=True)
    assert "### The Windows shards' durations, unioned (#931)" in run.stdout


@pytest.mark.parametrize(
    "parts, count, said",
    [
        pytest.param(
            None, 4, "3 parts were downloaded and --count says 4", id="missing"
        ),
        pytest.param(
            {**PARTS, "test-durations-7": {"tests/test_z.py::test_a": 1.0}},
            4,
            "1 ids are in two parts, first 'tests/test_z.py::test_a' in "
            "test-durations-4 and test-durations-7",
            id="duplicate",
        ),
        pytest.param(
            {**PARTS, "test-durations-7": '{"tests/test_q.py::test_a": '},
            4,
            "part test-durations-7 does not parse as JSON",
            id="unparseable",
        ),
        pytest.param(
            {**PARTS, "test-durations-7": {"tests/test_q.py::test_a": "slow"}},
            4,
            "part test-durations-7 prices 'tests/test_q.py::test_a' at 'slow'",
            id="not-seconds",
        ),
        pytest.param(
            {**PARTS, "test-durations-7": {"tests/test_q.py::test_a": True}},
            4,
            "part test-durations-7 prices 'tests/test_q.py::test_a' at True",
            id="a-boolean",
        ),
        pytest.param(
            {**PARTS, "test-durations-7": "[1, 2]"},
            4,
            "part test-durations-7 is not a JSON object",
            id="not-an-object",
        ),
        pytest.param(
            {**PARTS, "test-durations-7": b"\xff\xfe{}"},
            4,
            "part test-durations-7 cannot be read: UnicodeDecodeError",
            id="not-utf-8",
        ),
        pytest.param(
            {**PARTS, "test-durations-7": {}},
            4,
            "part test-durations-7 prices no case",
            id="empty",
        ),
        pytest.param(
            {}, 4, "the parts directory does not exist", id="nothing-downloaded"
        ),
    ],
)
def test_a_missing_part_a_duplicate_id_or_an_unparseable_part_is_exit_2(
    tmp_path, parts, count, said
):
    """S2. Exit 2 and nothing written, never a smaller file: a union that is
    not the suite would price every case it lost at the mean. The reason
    reaches the run's summary, where the person reading the red job looks."""
    root, held, out = write_parts(tmp_path, parts)
    summary = tmp_path / "summary.md"
    assert run_union(root, held, out, count, summary) == 2
    assert not out.exists(), "a refused union was written"
    text = summary.read_text(encoding="utf-8")
    assert said in text, text
    assert "Nothing was written." in text, text


def test_a_committed_file_that_does_not_parse_is_exit_2(tmp_path):
    """S2. The report is read against the committed file, and one that does
    not parse would also have stopped every shard at collection, so no run
    that reaches this job holds one; refusing it costs nothing."""
    root, held, out = write_parts(tmp_path, committed="{")
    summary = tmp_path / "summary.md"
    assert run_union(root, held, out, 3, summary) == 2
    assert not out.exists(), "a refused union was written"
    text = summary.read_text(encoding="utf-8")
    assert "the committed file does not parse as JSON" in text, text


@pytest.mark.parametrize("count", [0, -1])
def test_a_count_below_one_is_exit_2_naming_it(tmp_path, count):
    """Round 1's 🟡 4. `--count 0` over an empty parts directory found the
    zero parts it asked for, unioned nothing, and divided by the union's
    size: exit 1 with a traceback, outside the script's 0-or-2 contract. A
    union of no parts is no suite, and the argument is refused before
    anything is read."""
    root, held, out = write_parts(tmp_path, {})
    root.mkdir()
    summary = tmp_path / "summary.md"
    assert run_union(root, held, out, count, summary) == 2
    assert not out.exists(), "a refused union was written"
    text = summary.read_text(encoding="utf-8")
    assert f"--count is {count}: a union of no parts is no suite" in text, text


def test_the_summary_names_each_parts_seconds_the_spread_and_the_live_sum(
    tmp_path,
):
    """S3. The parts measure 10, 30 and 20 s, so the slowest is 1.50 x their
    mean of 20 s and 3.00 x the fastest; the spread is read over the mean.
    The committed file sums 29.5 s against the union's 60; each part's cases
    cost twice what the file says; one case is unpriced and one entry dead.
    No line carries a path of the machine it ran on."""
    root, held, out = write_parts(tmp_path)
    summary = tmp_path / "summary.md"
    assert run_union(root, held, out, 3, summary) == 0
    text = summary.read_text(encoding="utf-8")
    lines = text.splitlines()
    assert "- entries: 6 in the union of 3 parts, 6 in the committed file" in lines, (
        text
    )
    assert "- seconds: 60.0 s live, 29.5 s in the committed file" in lines, text
    assert (
        "- unpriced: 1 of the union's 6 cases (16.67%) have no price in the "
        "committed file" in lines
    ), text
    assert (
        "- dead: 1 entries of the committed file are no case a part ran, "
        "2.0 s (6.78% of its seconds)" in lines
    ), text
    assert (
        "- part test-durations-4: 2 cases, 10.0 s measured, median price 2.00 x "
        "the committed file's over 2 cases both price" in lines
    ), text
    assert (
        "- part test-durations-6: 2 cases, 20.0 s measured, median price 2.00 x "
        "the committed file's over 1 cases both price" in lines
    ), text
    assert (
        "- spread: the slowest part, test-durations-5, measured 1.50 x the "
        "parts' mean of 20.0 s" in lines
    ), text
    assert str(tmp_path) not in text, text
    assert os.sep + "parts" not in text, text


def test_a_part_the_committed_file_does_not_price_says_so():
    """S3. A part with no case the committed file prices has no ratio to
    take a median of, and an empty committed file has no seconds to share
    the dead ones over; each line says so rather than stopping the job."""
    lines = du.report([("p", {"tests/t.py::t": 1.0})], {"tests/t.py::t": 1.0}, {})
    assert (
        "- part p: 1 cases, 1.0 s measured, no case the committed file also prices"
        in lines
    ), lines
    assert (
        "- dead: 0 entries of the committed file are no case a part ran, "
        "0.0 s (0.00% of its seconds)" in lines
    ), lines


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
    """S6 of work item 1791876667. The paragraph a contributor meets when
    the staleness case goes red names the artifact and the download that
    works -- into a directory of its own, because `gh` will not overwrite --
    and nothing of the measuring run it replaced, and that the file is the
    one thing committed. The release checklist has no refresh box: a box a
    person ticks was the schedule 0.21.1 skipped."""
    running = section("CONTRIBUTING.md", "Running the checks")
    (recipe,) = [p for p in running.split("\n\n") if "goes stale" in p]
    flat = " ".join(recipe.split())
    for said in (
        "`test-durations`",
        "`gh run download <run id> -n test-durations -D <dir>`",
        "`gh run rerun <run id>`",
        "`gh workflow run test.yml --ref <branch>`",
        "over the committed file and commits it",
        "`durations` job",
        "`STALE_SHARE`",
        "entries the suite no longer collects",
    ):
        assert said in flat, f"the recipe paragraph does not say {said}"
    # The measuring run's own words. A dispatch is not among them: a branch
    # with no pull request gets its `tests` run that way (round 1's 🟡 2).
    for gone in ("restore the shards", "one job again", "for a single run"):
        assert gone not in flat, f"the recipe paragraph still says {gone!r}"
    before = section("docs/release-checklist.md", "0. Before starting")
    assert ".test_durations" not in before, "the checklist still has a refresh box"
