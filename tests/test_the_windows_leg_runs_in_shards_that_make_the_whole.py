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

The durations file is read too. A file missing from the tree only unbalances
the shards (`pytest-split` then divides by count), but one that does not
parse stops every shard at collection.

And it is held to its age (#874). A case added since the last refresh has no
price in the file, `pytest-split` gives it the file's mean, and the shards
drift apart with nothing saying so: the file went from 3.9 % to 9.4 %
unpriced in five days. More than `STALE_SHARE` of the collected cases
unpriced fails the suite case below, which is when the file is refreshed next
outside the planned refresh at each release's preparation. Entries the suite
no longer collects are not counted, because the division never reads them.
"""

import json
import ntpath
import os
import re
import sys

import pytest
from conftest import COLLECTED_NODE_IDS, posix_id
from test_ci_gives_the_checks_what_they_need import (
    jobs,
    matrix_include_entries,
    read,
)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DURATIONS = os.path.join(ROOT, ".test_durations")
SUITE = os.path.join(ROOT, "tests")

SPLIT = re.compile(r"--splits (\d+) --group (\d+)")

# Each sharded operating system and its count of shards. A system not named
# here runs the whole suite as one job and carries no split.
SHARDED = {"windows-latest": 4, "macos-latest": 3}

# The share of the collected cases the durations file may leave unpriced
# before the suite case fails: one in twenty (`questions.md` Q1 of work item
# 1791852613). Every id is one spelling on every machine -- a path is written
# with `/` (`conftest.py#posix_id`) and no id carries the interpreter's path
# -- so a file refreshed on Windows prices the whole collection on every leg,
# and one release cycle's growth (4.9 % in 0.21.0) stays under the share until
# the next release's refresh; under the 9.4 % the file had reached when #874
# was framed. It bounds the file's age, not the shards' imbalance: how far an
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
    runs = [
        ln.strip()
        for ln in jobs(read("test.yml"))["pytest"].splitlines()
        if ln.strip().startswith("- run: pytest ")
    ]
    assert len(runs) == 1, runs
    assert runs[0].endswith("${{ matrix.split }}"), runs[0]


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


def staleness(collected, durations):
    """The sentence the suite case fails with when more than `STALE_SHARE`
    of `collected` is unpriced in `durations`, or None at or under it."""
    missing = unpriced(collected, durations)
    share = len(missing) / len(collected)
    if share <= STALE_SHARE:
        return None
    return (
        f"{len(missing)} of the {len(collected)} collected cases ({share:.1%}) "
        f"have no price in .test_durations, over the {STALE_SHARE:.0%} "
        "STALE_SHARE allows: pytest-split gives each the file's mean, which "
        "unbalances the Windows and macOS shards. Refresh the file by the "
        "recipe in CONTRIBUTING.md §Running the checks. First unpriced: "
        + ", ".join(missing[:5])
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
    collected = _collection(FIXTURE_SIZE)
    priced = {node: 1.0 for node in collected[AT_THE_SHARE + 1 :]}
    sentence = staleness(collected, priced)
    assert sentence is not None
    assert f"{AT_THE_SHARE + 1} of the {FIXTURE_SIZE} collected cases" in sentence
    assert f"({(AT_THE_SHARE + 1) / FIXTURE_SIZE:.1%})" in sentence
    assert "CONTRIBUTING.md §Running the checks" in sentence
    assert collected[0] in sentence


def test_an_empty_collection_is_refused():
    with pytest.raises(ValueError, match="empty collection"):
        unpriced([], {"tests/test_m.py::test_0": 1.0})


def test_an_entry_nobody_collects_is_not_counted():
    collected = _collection(FIXTURE_SIZE)
    priced = {node: 1.0 for node in collected}
    priced.update({f"tests/test_gone.py::test_{i}": 1.0 for i in range(5000)})
    assert unpriced(collected, priced) == []
    assert staleness(collected, priced) is None


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
