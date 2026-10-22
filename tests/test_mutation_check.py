"""`skills/verify/scripts/mutation_check.py`, one class per function.

Begun by #942's phase 5 with the batch mode, `--replace OLD NEW` given once
per mutant: the baseline runs once, then each mutant once against the file as
it was, restored after each. The single-pair cases still stand in
`tests/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py`
until phase 6 places them here. Every case runs a stand-in for the cases, a
script under the case's own directory that logs what it saw of the target.
"""

import pathlib
import re
import shlex
import sys

import pytest
from conftest import census_case, load_module

TARGET = "skills/verify/scripts/mutation_check.py"

ROOT = pathlib.Path(__file__).resolve().parent.parent
mc = load_module(ROOT / TARGET, "mutation_check_under_test")

# The stand-in for a test command. It logs the target's text and whether any
# cached bytecode of the target existed when it ran, then writes that
# bytecode itself, as a command building its own environment would. It fails
# where the target holds one of the red markers, and hangs where it holds the
# hang marker.
STAND_IN = """\
import glob, os, py_compile, sys, time
target, log, red, hang = sys.argv[1:5]
with open(target, encoding="utf-8") as f:
    text = f.read()
cache = os.path.join(os.path.dirname(target), "__pycache__")
stem = os.path.splitext(os.path.basename(target))[0]
cached = bool(glob.glob(os.path.join(cache, stem + ".*.pyc")))
with open(log, "a", encoding="utf-8") as f:
    f.write(repr((text, cached)) + "\\n")
py_compile.compile(target, doraise=True)
if hang and hang in text:
    time.sleep(30)
sys.exit(1 if any(m and m in text for m in red.split(",")) else 0)
"""

ORIGINAL = "A = 1\nB = 1\nC = 1\n"
PAIRS = [("A = 1", "A = 2"), ("B = 1", "B = 2"), ("C = 1", "C = 2")]


def world(tmp_path, red="A = 2,C = 2", hang=""):
    """The target, the log, and the command that runs the stand-in."""
    target = tmp_path / "target.py"
    target.write_text(ORIGINAL, encoding="utf-8")
    script = tmp_path / "stand_in.py"
    script.write_text(STAND_IN, encoding="utf-8")
    log = tmp_path / "seen.log"
    words = [sys.executable, script, target, log, red, hang]
    return target, log, [str(w) for w in words]


def seen(log):
    """One `(text, a cache existed)` per run the stand-in made."""
    if not log.exists():
        return []
    return [eval(line) for line in log.read_text(encoding="utf-8").splitlines()]


def mutant_of(old, new):
    return ORIGINAL.replace(old, new)


class Test_batch_run:
    def test_accepts_each_pair_alone_after_one_baseline(self, tmp_path):
        target, log, command = world(tmp_path)
        results = list(mc.batch_run(str(target), PAIRS, command, cwd=str(tmp_path)))
        assert [r[0] for r in results] == [mc.BASELINE, mc.RED, mc.SURVIVED, mc.RED]
        assert all(r[3] >= 0 for r in results), results
        runs = seen(log)
        assert [text for text, _ in runs] == [ORIGINAL] + [
            mutant_of(*pair) for pair in PAIRS
        ], "the baseline ran more than once, or a mutant carried another's change"
        assert not any(cached for _, cached in runs), (
            "a run met the bytecode the run before it wrote"
        )
        assert target.read_text(encoding="utf-8") == ORIGINAL
        assert not list((tmp_path / "__pycache__").glob("target.*.pyc"))

    def test_accepts_a_run_with_no_verdict_and_goes_on_to_the_next_pair(self, tmp_path):
        target, log, command = world(tmp_path, hang="B = 2")
        results = list(
            mc.batch_run(str(target), PAIRS, command, cwd=str(tmp_path), timeout=2)
        )
        assert [r[0] for r in results] == [mc.BASELINE, mc.RED, mc.TIMED_OUT, mc.RED]
        assert seen(log)[-1][0] == mutant_of(*PAIRS[2])
        assert target.read_text(encoding="utf-8") == ORIGINAL

    @pytest.mark.parametrize(
        ("pairs", "number"),
        [
            ([("A = 1", "A = 2"), ("D = 1", "D = 2")], 2),
            ([("= 1", "= 2"), ("A = 1", "A = 2")], 1),
            ([("A = 1", "A = 2"), ("B = 1", "B = 1")], 2),
        ],
        ids=["lands-nowhere", "lands-three-times", "changes-nothing"],
    )
    def test_refuses_every_pair_when_one_cannot_land_once(
        self, tmp_path, pairs, number
    ):
        target, log, command = world(tmp_path)
        with pytest.raises(mc.Refused, match=rf"^pair {number}: "):
            list(mc.batch_run(str(target), pairs, command, cwd=str(tmp_path)))
        assert seen(log) == [], "the cases ran before the refusal"
        assert target.read_text(encoding="utf-8") == ORIGINAL

    def test_refuses_to_write_any_mutant_when_the_baseline_fails(self, tmp_path):
        target, log, command = world(tmp_path, red="A = 1")
        results = list(mc.batch_run(str(target), PAIRS, command, cwd=str(tmp_path)))
        assert [r[0] for r in results] == [mc.NO_BASELINE]
        assert "(exit 1)" in results[0][1]
        assert [text for text, _ in seen(log)] == [ORIGINAL]
        assert target.read_text(encoding="utf-8") == ORIGINAL


def replaces(pairs):
    """`--replace OLD NEW` once per pair."""
    return [word for old, new in pairs for word in ("--replace", old, new)]


def main_of(tmp_path, capsys, pairs, **kind):
    target, log, command = world(tmp_path, **kind)
    argv = [str(target), *replaces(pairs), "--tests", shlex.join(command)]
    argv += ["--cwd", str(tmp_path), "--timeout", "2"]
    code = mc.main(argv)
    return code, capsys.readouterr().out, log, target


SECONDS = r" \(\d+\.\ds\)$"


class Test_main:
    def test_accepts_a_batch_whose_every_mutant_is_red(self, tmp_path, capsys):
        pairs = [PAIRS[0], PAIRS[2]]
        code, out, log, target = main_of(tmp_path, capsys, pairs)
        lines = out.splitlines()
        assert code == 0, out
        assert re.match(
            r"baseline: the cases pass against the file as it is" + SECONDS, lines[0]
        ), out
        assert re.match(r"mutant 1: red" + SECONDS, lines[1]), out
        assert re.match(r"mutant 2: red" + SECONDS, lines[2]), out
        assert re.match(
            r"mutation-check: 2 mutants, 2 red, 0 SURVIVED, 0 with no verdict"
            + SECONDS,
            lines[3],
        ), out
        assert len(lines) == 4, out
        assert len(seen(log)) == 3
        assert target.read_text(encoding="utf-8") == ORIGINAL

    @pytest.mark.parametrize(
        ("kind", "verdicts", "exit_code"),
        [
            ({}, ["red", "SURVIVED", "red"], 1),
            ({"hang": "C = 2"}, ["red", "SURVIVED", "timed out"], 1),
            ({"red": "A = 2,B = 2", "hang": "C = 2"}, ["red", "red", "timed out"], 2),
        ],
        ids=["a-survivor", "a-survivor-and-no-verdict", "no-verdict-alone"],
    )
    def test_refuses_a_batch_with_a_survivor_or_a_run_with_no_verdict(
        self, tmp_path, capsys, kind, verdicts, exit_code
    ):
        code, out, log, target = main_of(tmp_path, capsys, PAIRS, **kind)
        printed = re.findall(r"^mutant (\d+): (red|SURVIVED|timed out)", out, re.M)
        assert printed == [(str(n), v) for n, v in enumerate(verdicts, 1)], out
        assert code == exit_code, out
        counts = (verdicts.count("red"), verdicts.count("SURVIVED"))
        assert f"3 mutants, {counts[0]} red, {counts[1]} SURVIVED" in out, out
        assert len(seen(log)) == 4, "the baseline or a mutant did not run once"
        assert target.read_text(encoding="utf-8") == ORIGINAL

    def test_refuses_a_pair_that_cannot_land_and_runs_nothing(self, tmp_path, capsys):
        pairs = [PAIRS[0], ("D = 1", "D = 2")]
        code, out, log, target = main_of(tmp_path, capsys, pairs)
        assert code == 2, out
        assert out.startswith("refused: pair 2: OLD occurs 0 times"), out
        assert seen(log) == []
        assert target.read_text(encoding="utf-8") == ORIGINAL

    def test_refuses_a_batch_whose_baseline_fails(self, tmp_path, capsys):
        code, out, log, target = main_of(tmp_path, capsys, PAIRS, red="A = 1")
        assert code == 2, out
        assert out.startswith("no baseline: the cases fail against the file"), out
        assert "mutant 1" not in out, out
        assert len(seen(log)) == 1
        assert target.read_text(encoding="utf-8") == ORIGINAL


test_census = census_case(TARGET)
