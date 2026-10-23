"""`.github/scripts/durations_union.py`, one class per function.

Every Windows shard of the tests workflow stores its own session's
durations, a step uploads each as a part, and the `durations` job unions the
parts through this script into the `test-durations` artifact (#931). A part
nobody uploads, a part that is the committed file, or one that does not
parse makes a union that is not the suite, so the script refuses each with
exit 2 and writes nothing. The cases drive it over fixture parts.

  S2   the union of the parts is the whole suite, sorted, with LF line
       ends; a missing, duplicated or unparseable part is exit 2
  S3   the summary names each part's seconds, the spread and the live sum

#942's phase 6 placed these cases from
`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, which
keeps the cases that read the workflow, the durations file and the
documents.
"""

import importlib.util
import json
import os
import subprocess
import sys

import pytest
from conftest import census_case

TARGET = ".github/scripts/durations_union.py"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
UNION_SCRIPT = os.path.join(ROOT, ".github", "scripts", "durations_union.py")

_spec = importlib.util.spec_from_file_location("durations_union", UNION_SCRIPT)
du = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(du)

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


class Test_main:
    def test_accepts_the_parts_and_writes_their_union_sorted_with_lf(self, tmp_path):
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
    def test_refuses_a_missing_part_a_duplicate_id_or_an_unparseable_part(
        self, tmp_path, parts, count, said
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

    def test_a_committed_file_that_does_not_parse_is_exit_2(self, tmp_path):
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
    def test_a_count_below_one_is_exit_2_naming_it(self, tmp_path, count):
        """Round 1's finding 4. `--count 0` over an empty parts directory found
        the zero parts it asked for, unioned nothing, and divided by the
        union's size: exit 1 with a traceback, outside the script's 0-or-2
        contract. A union of no parts is no suite, and the argument is refused
        before anything is read."""
        root, held, out = write_parts(tmp_path, {})
        root.mkdir()
        summary = tmp_path / "summary.md"
        assert run_union(root, held, out, count, summary) == 2
        assert not out.exists(), "a refused union was written"
        text = summary.read_text(encoding="utf-8")
        assert f"--count is {count}: a union of no parts is no suite" in text, text

    def test_the_summary_names_each_parts_seconds_the_spread_and_the_live_sum(
        self,
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
        assert (
            "- entries: 6 in the union of 3 parts, 6 in the committed file" in lines
        ), text
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


class Test_module:
    def test_a_part_the_committed_file_does_not_price_says_so(self):
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


test_census = census_case(TARGET)
