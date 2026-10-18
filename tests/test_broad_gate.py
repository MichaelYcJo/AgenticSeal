"""`skills/verify/scripts/broad_gate.py`: the run's one record, one group per
function this module states.

The rest of the gate — the row, the base comparison, the panel and the
stamp — is still held by `tests/test_the_seal_is_taken_once_by_the_sealer.py`
until #942 moves it here.
"""

import importlib.util
import os
import pathlib
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
GATE = ROOT / "skills" / "verify" / "scripts" / "broad_gate.py"
CHAIN = ROOT / "skills" / "code-review" / "scripts" / "chain_check.py"
ITEM = "seal/specs/1799000001-a-gated-work-item"


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


gate = load(GATE, "broad_gate_under_test")
chain = load(CHAIN, "chain_check_beside_broad_gate")


def git(d, *args):
    return subprocess.run(
        ["git", "-C", str(d), *args],
        check=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    ).stdout.strip()


def write(d, rel, text):
    p = pathlib.Path(d) / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


# --- the spelling the gate writes and the check reads -------------------------


class TestSpelling:
    def test_the_gate_and_the_check_spell_the_file_and_separator_alike(self):
        assert gate.GATE_FILE == chain.BROAD_GATE_FILE
        assert gate.EARLIER_RUN == chain.EARLIER_RUN
        assert gate.ROW == chain.BROAD_GATE
        assert gate.CHAIN_SEALING == chain.SEALING

    def test_a_file_the_gate_wrote_is_read_by_the_check(self, tmp_path):
        path = gate.write_gate_file(str(tmp_path), "abc1234", "def5678")
        reader = load(
            ROOT / "skills" / "verify" / "scripts" / "unverified_check.py", "r"
        )
        text = pathlib.Path(path).read_text(encoding="utf-8")
        assert chain.newest_run(reader, text) == "abc1234"
        assert chain.newest_run(reader, text.replace("abc1234", "zz")) is None


# --- kept_runs ----------------------------------------------------------------


class TestKeptRuns:
    def test_a_new_run_stands_first_and_earlier_runs_are_kept(self):
        held = "aaa1111 against base1; earlier run: bbb2222 against base1"
        assert gate.kept_runs(held, "ccc3333 against base1") == (
            "ccc3333 against base1; earlier run: aaa1111 against base1"
            "; earlier run: bbb2222 against base1"
        )
        assert gate.kept_runs("", "ccc3333 against base1") == "ccc3333 against base1"

    def test_the_same_comparison_is_not_recorded_twice(self):
        held = "aaa1111 against base1; earlier run: bbb2222 against base1"
        assert gate.kept_runs(held, "aaa1111 against base1") == held
        assert gate.kept_runs(held, "aaa1111 against base2").count("aaa1111") == 2


# --- write_gate_file ----------------------------------------------------------


class TestWriteGateFile:
    def test_a_second_run_is_written_in_front_of_the_first(self, tmp_path):
        gate.write_gate_file(str(tmp_path), "aaa1111", "base1")
        path = gate.write_gate_file(str(tmp_path), "bbb2222", "base1")
        text = pathlib.Path(path).read_text(encoding="utf-8")
        assert os.path.basename(path) == "broad-gate.md"
        assert (
            "| Broad gate | bbb2222 against base1; earlier run: aaa1111 against base1 |"
        ) in text

    def test_a_file_that_cannot_be_written_is_a_refusal(self, tmp_path):
        missing = tmp_path / "no-such-item"
        with pytest.raises(gate.Refused, match="could not be written"):
            gate.write_gate_file(str(missing), "aaa1111", "base1")


# --- rounds_rows and item_value -----------------------------------------------


def a_record(*verdicts):
    """A round record in `templates/sdd-round.md`'s shape, one finding per
    `verdict:` value."""
    found = "".join(
        f"### {n}. x\n\nseverity: should\nlocation: `a:{n}`\n"
        f"verdict: {verdict}\n\nwhy\n\nanswer: \n\n"
        for n, verdict in enumerate(verdicts, 1)
    )
    return (
        "# r — review round 1\n\n"
        f"target: abc1234 against base\n\n## Findings\n\n{found}"
        "## Probes\n\n| Command | Result |\n|---|---|\n"
    )


# The table the old generator's records carried, which no reader reads.
OLD_RECORD = (
    "# r — review round 1\n\n## Verdicts\n\n"
    "| # | Finding | Location | Verdict | Grounds |\n|---|---|---|---|---|\n"
    "| 🟡 1 | x | `a:1` | deferred #9 | g |\n"
)


class TestRoundsRows:
    def test_the_count_and_every_records_deferred_homes(self, tmp_path):
        """S11 (T30): `deferred` is counted through the check's reader, so a
        record it refuses — one finding at a homeless `deferred` or an
        emphasised one, a label in another spelling, or the old table's shape
        — adds nothing beneath `rounds`, and the records it reads add every
        home they name."""
        item = tmp_path / "1799000002-x"
        write(item, "rounds/round-1.md", a_record("deferred #7", "fixed abc1234"))
        write(item, "rounds/round-2.md", a_record("deferred #8"))
        write(item, "rounds/round-3.md", a_record("deferred #9", "deferred"))
        write(item, "rounds/round-4.md", a_record("**deferred** #9"))
        write(item, "rounds/round-5.md", OLD_RECORD)
        write(
            item,
            "rounds/round-6.md",
            a_record("deferred #9").replace("verdict:", "Verdict:"),
        )
        rows = gate.rounds_rows(str(item))
        assert rows == [("rounds", "6"), ("", "2 deferred → #7, #8")], rows

    def test_no_record_and_no_deferral_print_the_count_alone(self, tmp_path):
        item = tmp_path / "1799000003-y"
        assert gate.rounds_rows(str(item)) == [("rounds", "0")]
        write(item, "rounds/round-1.md", a_record("fixed abc1234"))
        assert gate.rounds_rows(str(item)) == [("rounds", "1")]

    def test_the_item_row_is_the_ids_digits(self):
        # `seal_stamp`'s since #975, which the gate's `panel` reads it from.
        stamp = gate.stamp_module()
        assert stamp.item_value("seal/specs/1799000004-a-name") == "1799000004"
        assert stamp.item_value("plain") == "plain"


# --- the gate end to end ------------------------------------------------------


ROUTING = (
    "| Axis | Answer |\n|---|---|\n| Review | {review} |\n"
    "| Destination | open the pull request |\n| Branch | feature |\n"
)


@pytest.fixture
def repo(tmp_path):
    d = tmp_path / "repo"
    d.mkdir()
    git(d, "init", "-q", "-b", "base")
    git(d, "config", "user.email", "t@t")
    git(d, "config", "user.name", "t")
    write(d, "tests/test_one.py", "def test_one():\n    assert True\n")
    write(
        d,
        "seal/config.md",
        "| Item | Value |\n|---|---|\n| Mode | shared |\n"
        f"| Broad gate | {sys.executable} -m pytest -q -p no:cacheprovider tests |\n",
    )
    write(
        d,
        f"{ITEM}/overview.md",
        "# overview\n\n## Not verified\n\nnone — the fixture verifies nothing\n",
    )
    git(d, "add", "-A")
    git(d, "commit", "-qm", "base")
    git(d, "switch", "-qc", "feature")
    return d


def run(repo, *extra):
    env = {
        k: v
        for k, v in os.environ.items()
        if k not in ("GITHUB_EVENT_PATH", "GITHUB_HEAD_REF", "CLAUDE_CODE_SESSION_ID")
    }
    return subprocess.run(
        [sys.executable, str(GATE), "--base", "base", "--root", str(repo), *extra],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=300,
        env=env,
    )


class TestGate:
    @pytest.mark.parametrize(
        "review", ["through the review chain", "straight to the PR"]
    )
    def test_a_green_run_writes_the_file_on_either_route(self, repo, review):
        """S5 (T14): `--record` writes `broad-gate.md` naming HEAD against
        the base, whichever review answer the work item declared, and no
        round record is touched."""
        write(repo, f"{ITEM}/routing.md", ROUTING.format(review=review))
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "declare")
        out = run(repo, "--record", str(repo / ITEM))
        assert out.returncode == 0, out.stdout + out.stderr
        text = (repo / ITEM / "broad-gate.md").read_text(encoding="utf-8")
        head = git(repo, "rev-parse", "--short", "HEAD")
        base = git(repo, "rev-parse", "--short", "base")
        assert f"| Broad gate | {head} against {base} |" in text
        assert not (repo / ITEM / "rounds").exists()
        assert "not committed" in out.stdout

    def test_a_red_run_writes_nothing(self, repo):
        write(repo, f"{ITEM}/routing.md", ROUTING.format(review="straight to the PR"))
        write(repo, "tests/test_two.py", "def test_two():\n    assert False\n")
        git(repo, "add", "-A")
        git(repo, "commit", "-qm", "a failing test")
        out = run(repo, "--record", str(repo / ITEM))
        assert out.returncode == 1, out.stdout + out.stderr
        assert not (repo / ITEM / "broad-gate.md").exists()
