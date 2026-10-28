"""`skills/verify/scripts/mutation_check.py`, one class per function.

Begun by #942's phase 5 with the batch mode, `--replace OLD NEW` given once
per mutant: the baseline runs once, then each mutant once against the file as
it was, restored after each. Every batch case runs a stand-in for the cases, a
script under the case's own directory that logs what it saw of the target.

Phase 6 placed here the single-pair cases of
`tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py`,
#641's and #577's: one mutation of one unit, with the loop's housekeeping
derived from the file it mutated. The command derives the cache from the
file, for every interpreter tag; runs the cases with
`PYTHONDONTWRITEBYTECODE=1` under a bound; restores from bytes it held and
compares the hash; and prints one verdict whose exit code says which of three
things happened. Every fixture of those cases lives under `tmp_path`, and
every process a case starts is reaped or proven dead before the case returns.
The old file keeps the cases that read the crafter's definition and the verify
skill.
"""

import importlib.util
import os
import pathlib
import py_compile
import re
import shlex
import subprocess
import sys
import textwrap
import time

import conftest
import pytest
from conftest import census_case, load_module

TARGET = "skills/verify/scripts/mutation_check.py"

ROOT = pathlib.Path(conftest.ROOT)
mc = load_module(ROOT / TARGET, "mutation_check_under_test")
WRAPPER = os.path.join(ROOT, "bin", "seal")

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
        # Bytecode an earlier run left behind, which the baseline must not meet.
        py_compile.compile(str(target), doraise=True)
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


# --- the single-pair cases' helpers -------------------------------------------


def module():
    """The command, loaded afresh from its path, for a case that patches it."""
    return load_module(ROOT / TARGET, "agentic_mutation_check")


def run(argv, capsys):
    """`main(argv)` in-process: the exit code and everything it printed."""
    code = module().main([str(a) for a in argv])
    out = capsys.readouterr()
    return code, out.out + out.err


def probe(tmp_path, body, name="probe.py"):
    """A stand-in for the cases: a script that reports what it SAW."""
    path = tmp_path / name
    path.write_text(textwrap.dedent(body), encoding="utf-8")
    return path


def cases_command(*argv):
    return shlex.join([sys.executable, *[str(a) for a in argv]])


def snapshot(directory):
    """Every file under `directory`, with its bytes."""
    found = {}
    for here, _dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(here, name)
            with open(path, "rb") as f:
                found[os.path.relpath(path, directory)] = f.read()
    return found


PASSES = "import sys\nsys.exit(0)\n"
FAILS = "import sys\nsys.exit(1)\n"

# Fails only while the file it is handed carries the text it is handed, so
# the run against the file as it is passes and the run against the mutant is
# red -- the one shape a red means anything in (round 1, 🔴 1).
FAILS_ON_THE_MUTANT = """\
import sys
with open(sys.argv[1], encoding="utf-8") as f:
    sys.exit(1 if sys.argv[2] in f.read() else 0)
"""


def red_on(tmp_path, target, marker, name="red_on.py"):
    """The cases command that is red only against the mutant holding `marker`."""
    return cases_command(probe(tmp_path, FAILS_ON_THE_MUTANT, name), target, marker)


# Reports the bytes of the file it is handed, so a case can see what the
# cases saw at the moment they ran.
SEES_FILE = """\
import sys
with open(sys.argv[1], encoding="utf-8") as f:
    seen = f.read()
with open(sys.argv[2], "w", encoding="utf-8") as f:
    f.write(seen)
"""


def plant_import_cache(path):
    """A cache entry for `path`, the timestamp-checked kind an import writes.

    Written by `py_compile` rather than by importing, because an import
    honours `PYTHONDONTWRITEBYTECODE` -- and this module is itself run under
    `seal mutate`, which sets it, whenever a unit of the command is
    mutated. Planted by import, the cache is never written there and the case
    goes red on its own precondition whatever the mutation was: measured
    while mutating this module's script, 2026-10-01."""
    py_compile.compile(
        str(path), cfile=importlib.util.cache_from_source(str(path)), doraise=True
    )
    cached = list((path.parent / "__pycache__").glob(f"{path.stem}.*.pyc"))
    assert cached, "this case needs a real .pyc to remove; the interpreter wrote none"
    return cached


# Reports what it SAW rather than passing or failing: whether any cached
# bytecode for the module existed at the moment the cases ran, and whether the
# run was told to write none.
SEES_CACHE = """\
import glob, os, sys
module, log = sys.argv[1], sys.argv[2]
stem = os.path.splitext(os.path.basename(module))[0]
cache = os.path.join(os.path.dirname(module), "__pycache__")
found = sorted(os.path.basename(p) for p in glob.glob(os.path.join(cache, stem + ".*.pyc")))
with open(log, "a", encoding="utf-8") as f:
    f.write(repr((found, os.environ.get("PYTHONDONTWRITEBYTECODE"))) + "\\n")
"""


def seen_runs(log):
    """One `(caches found, the variable)` per run the command made."""
    return [eval(line) for line in log.read_text(encoding="utf-8").splitlines()]


# Imports the mutated module with bytecode writing switched back ON, the way
# a `--tests` command that builds its own environment would.
WRITES_CACHE = """\
import importlib.util, sys
sys.dont_write_bytecode = False
spec = importlib.util.spec_from_file_location("mutant", sys.argv[1])
spec.loader.exec_module(importlib.util.module_from_spec(spec))
"""


# Logs whether the planted file exists when the cases run, then leaves it there
# again, the way a command that builds its own environment would write it. So
# every run asks of the removal before it, and the caller asks of the last.
SEES_THE_MIRROR = """\
import os, sys
planted, log = sys.argv[1], sys.argv[2]
with open(log, "a", encoding="utf-8") as f:
    f.write(("cache" if os.path.exists(planted) else "clean") + "\\n")
os.makedirs(os.path.dirname(planted), exist_ok=True)
with open(planted, "wb") as f:
    f.write(b"stale")
"""


# Passes while the module it loads still says 15.
ASSERTS_FIFTEEN = """\
import importlib.util, sys
spec = importlib.util.spec_from_file_location("under_test", sys.argv[1])
loaded = importlib.util.module_from_spec(spec)
spec.loader.exec_module(loaded)
sys.exit(0 if loaded.VALUE == 15 else 1)
"""


REWRITES = """\
import sys
with open(sys.argv[1], "w", encoding="utf-8") as f:
    f.write("something the cases wrote\\n")
"""


# Makes the file it is handed read-only once it holds the mutant, so the
# restore's own write raises rather than its hash differing.
LOCKS_THE_MUTANT = """\
import os, stat, sys
with open(sys.argv[1], encoding="utf-8") as f:
    mutant = sys.argv[2] in f.read()
if mutant:
    os.chmod(sys.argv[1], stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
sys.exit(1 if mutant else 0)
"""


# Starts a child that keeps the cases' output open, then exits at once:
# red against the mutant, green against the file as it is.
LEAVES_A_CHILD_ON_THE_OUTPUT = """\
import subprocess, sys
with open(sys.argv[1], encoding="utf-8") as f:
    mutant = sys.argv[2] in f.read()
if mutant:
    child = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)"])
    with open(sys.argv[3], "w", encoding="utf-8") as f:
        f.write(str(child.pid))
sys.exit(1 if mutant else 0)
"""


# Prints bytes that are not UTF-8, then fails only on the mutant.
PRINTS_NOT_UTF8 = """\
import sys
sys.stdout.buffer.write(b"\\xff\\xfe\\n")
sys.stdout.flush()
with open(sys.argv[1], encoding="utf-8") as f:
    sys.exit(1 if sys.argv[2] in f.read() else 0)
"""


# A wrapper in `bin/test`'s position: against the mutant it starts the process
# that does the work as a child of its own and waits for it, and against the
# file as it is it passes at once, so the run the bound ends is the mutated
# one. The child's pid is written down first, so a case can ask afterwards
# whether it is still alive. Arguments: the file, the mutant's text, the pid
# file.
STARTS_A_CHILD = """\
import subprocess, sys
with open(sys.argv[1], encoding="utf-8") as f:
    if sys.argv[2] not in f.read():
        sys.exit(0)
child = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)"])
with open(sys.argv[3], "w", encoding="utf-8") as f:
    f.write(str(child.pid))
child.wait()
"""


def starts_a_child(tmp_path, target, pid_file, body=STARTS_A_CHILD):
    return cases_command(probe(tmp_path, body), target, "VALUE = 2", pid_file)


def alive(pid):
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def gone_within(pid, seconds):
    """Polled, because the orphan is reaped by the system, not by us."""
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        if not alive(pid):
            return True
        time.sleep(0.05)
    return not alive(pid)


def end_if_alive(pid):
    """So a red case leaves nothing running either (C5)."""
    if pid is not None and alive(pid):
        try:
            os.kill(pid, 9)
        except ProcessLookupError:
            pass


def read_pid(path):
    try:
        return int(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


# A child that leaves the wrapper's process group and keeps the cases'
# output open, so no group kill reaches it.
STARTS_AN_ESCAPED_CHILD = STARTS_A_CHILD.replace(
    '"import time; time.sleep(30)"])',
    '"import time; time.sleep(30)"], start_new_session=True)',
)


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
            r"seal mutate: 2 mutants, 2 red, 0 SURVIVED, 0 with no verdict" + SECONDS,
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
        counts = [verdicts.count(v) for v in ("red", "SURVIVED", "timed out")]
        assert (
            "3 mutants, {} red, {} SURVIVED, {} with no verdict".format(*counts) in out
        ), out
        assert len(seen(log)) == 4, "the baseline or a mutant did not run once"
        assert target.read_text(encoding="utf-8") == ORIGINAL

    @pytest.mark.parametrize(
        "pairs", [[PAIRS[0]], [PAIRS[0], PAIRS[2]]], ids=["one-pair", "a-batch"]
    )
    def test_accepts_a_bound_of_zero_as_no_bound(self, tmp_path, capsys, pairs):
        """`--timeout 0` removes the bound, as its help says, for one pair and
        for a batch. Read as zero seconds, it would end every run before the
        cases could answer."""
        target, log, command = world(tmp_path)
        argv = [str(target), *replaces(pairs), "--tests", shlex.join(command)]
        code = mc.main([*argv, "--cwd", str(tmp_path), "--timeout", "0"])
        out = capsys.readouterr().out
        assert code == 0, out
        assert "timed out" not in out, out
        assert len(seen(log)) == len(pairs) + 1, out
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

    # --- S1 · the mutated file's bytecode is gone for every tag -------------

    def test_no_bytecode_for_the_mutated_file_exists_while_the_cases_run(
        self, tmp_path, capsys, monkeypatch
    ):
        """The mechanism, watched by what the subprocess can see.

        Two tags are planted, because two coexist beside one source on the
        machine this was built on: `python3` is 3.14 and `bin/test`'s virtualenv
        is 3.13. `importlib.util.cache_from_source` names the CALLING
        interpreter's file only, so a removal spelled that way leaves the other
        tag for the cases' interpreter to read. The foreign tag here is written by
        hand, since no second interpreter is guaranteed on a CI runner.

        Reproducing a stale read by timing is not attempted -- whether two writes
        land in one mtime second is the machine's, not the case's, which is what
        `tests/skills/test_arm_check.py` measured and says. S2 below makes the stale
        read deterministic instead.

        The variable is taken out of this process's environment first, so the
        flag the cases report is the one the command set and not one inherited
        from whatever ran this suite."""
        monkeypatch.delenv("PYTHONDONTWRITEBYTECODE", raising=False)
        target = tmp_path / "under_test.py"
        target.write_text("VALUE = 1\n", encoding="utf-8")
        plant_import_cache(target)
        foreign = tmp_path / "__pycache__" / "under_test.cpython-399.pyc"
        foreign.write_bytes(b"not bytecode any interpreter here reads")
        log = tmp_path / "seen.txt"

        code, out = run(
            [
                target,
                "--replace",
                "VALUE = 1",
                "VALUE = 2",
                "--tests",
                cases_command(probe(tmp_path, SEES_CACHE), target, log),
            ],
            capsys,
        )
        # Every run the command made: the baseline against the file as it is, and
        # the run against the mutant.
        for found, flag in seen_runs(log):
            assert found == [], (
                f"{found} -- cached bytecode for the mutated file existed while the "
                f"cases ran, so the interpreter can run a previous mutation instead of "
                f"this one. A tag left behind is the one `cache_from_source` does not name"
            )
            assert flag == "1", "the cases were not told to write no bytecode"
        assert not list((tmp_path / "__pycache__").glob("under_test.*.pyc"))
        assert code == 1, out

    def test_bytecode_the_baseline_wrote_is_gone_before_the_mutated_run(
        self, tmp_path, capsys
    ):
        """The baseline runs the cases against the original, and a command that
        builds its own environment writes the original's `.pyc` while it does. A
        same-length break written inside the same second matches that cache, so
        the mutated run would read the original. So the removal happens again
        between the write and the mutated run, and the mutated run sees none."""
        target = tmp_path / "under_test.py"
        target.write_text("VALUE = 1\n", encoding="utf-8")
        log = tmp_path / "seen.txt"
        run(
            [
                target,
                "--replace",
                "VALUE = 1",
                "VALUE = 2",
                "--tests",
                # Look first, then write: so each line says what the run before
                # this one left behind.
                cases_command(probe(tmp_path, SEES_CACHE + WRITES_CACHE), target, log),
            ],
            capsys,
        )
        runs = seen_runs(log)
        assert len(runs) == 2, f"the command ran the cases {len(runs)} times, not twice"
        assert runs[1][0] == [], (
            f"{runs[1][0]} -- the baseline's bytecode for the original was still "
            f"there when the mutated run started"
        )

    def test_bytecode_the_cases_wrote_for_the_mutant_is_not_left_behind(
        self, tmp_path, capsys
    ):
        """The second removal, after the restore. The environment variable stops
        a run that honours it; a command that builds its own environment does
        not, and the mutant's `.pyc` it leaves is the same size as the next
        same-length mutation's source."""
        target = tmp_path / "under_test.py"
        target.write_text("VALUE = 1\n", encoding="utf-8")

        run(
            [
                target,
                "--replace",
                "VALUE = 1",
                "VALUE = 2",
                "--tests",
                cases_command(probe(tmp_path, WRITES_CACHE), target),
            ],
            capsys,
        )
        left = list((tmp_path / "__pycache__").glob("under_test.*.pyc"))
        assert left == [], f"{left} -- the run left the mutant's bytecode behind"

    def test_a_relative_pycache_prefix_is_cleared_where_the_cases_run(
        self, tmp_path, capsys, monkeypatch
    ):
        """#703's S11, and this item's round 1 ⬜ 7. CPython joins
        `PYTHONPYCACHEPREFIX` as given, so a relative prefix names a mirror under
        the directory of the process that imports, which is the cases' `--cwd`.
        `arm_check.clear_bytecode_cache` reads it against the `cwd` it is handed,
        and this command used to hand it none, so with a `--cwd` other than the
        shell's the stale `.pyc` stayed exactly where the cases read it.

        The planted path is `cache_from_source`'s own, with the prefix as a
        process in `other/` resolves it, so the case asks CPython where the file
        is rather than repeating the clear's join.

        Red how: with `mutation_run`'s three calls passing no `cwd`, every run
        saw the planted file and it outlived the run. Executed."""
        target = tmp_path / "under_test.py"
        target.write_text("VALUE = 1\n", encoding="utf-8")
        other = tmp_path / "other"
        other.mkdir()
        prefix = "agentic-prefix-703"
        monkeypatch.setattr(sys, "pycache_prefix", os.path.join(str(other), prefix))
        planted = importlib.util.cache_from_source(str(target))
        # The prefix the clear reads is the environment's, as a session's would be.
        monkeypatch.setattr(sys, "pycache_prefix", None)
        monkeypatch.setenv("PYTHONPYCACHEPREFIX", prefix)
        os.makedirs(os.path.dirname(planted))
        with open(planted, "wb") as f:
            f.write(b"stale")
        log = tmp_path / "seen.txt"

        code, out = run(
            [
                target,
                "--replace",
                "VALUE = 1",
                "VALUE = 2",
                "--tests",
                cases_command(probe(tmp_path, SEES_THE_MIRROR), planted, log),
                "--cwd",
                other,
            ],
            capsys,
        )
        seen = log.read_text(encoding="utf-8").split()
        assert seen == ["clean", "clean"], (
            f"{seen} -- a run read the module's bytecode from the prefix mirror its "
            f"cwd resolves to, so the mutated run can read a previous mutation"
        )
        assert not os.path.exists(planted), "the last run's cache outlived the run"
        assert code == 1, out

    # --- S2 · the same-length mutation reads red ----------------------------

    def test_a_same_length_mutation_reads_red_over_a_trusted_cache(
        self, tmp_path, capsys
    ):
        """#641's *what must not break*, and the crafter's loop in miniature:
        `WINDOW = 15` to `25` read green once, because the interpreter ran the
        cached original.

        The cache planted here is an unchecked-hash `.pyc`, which CPython trusts
        without consulting the source at all. That makes the stale read the
        timestamp cache produces only inside one mtime second happen on every
        run, so this case is red whenever the removal is missing rather than
        whenever the machine is fast."""
        target = tmp_path / "under_test.py"
        target.write_text("VALUE = 15\n", encoding="utf-8")
        py_compile.compile(
            str(target),
            cfile=importlib.util.cache_from_source(str(target)),
            invalidation_mode=py_compile.PycInvalidationMode.UNCHECKED_HASH,
            doraise=True,
        )

        code, out = run(
            [
                target,
                "--replace",
                "VALUE = 15",
                "VALUE = 25",
                "--tests",
                cases_command(probe(tmp_path, ASSERTS_FIFTEEN), target),
            ],
            capsys,
        )
        assert code == 0 and out.startswith("red"), (
            f"the cases ran the cached original rather than the mutation: {out}"
        )

    # --- S3 · a replacement lands exactly once, or nothing is written -------

    @pytest.mark.parametrize(
        ("source", "count"),
        [("VALUE = 1\n", 0), ("OLD = 1\nOLD = 2\n", 2)],
        ids=["absent", "twice"],
    )
    def test_a_replacement_that_cannot_land_once_is_refused_before_any_write(
        self, tmp_path, capsys, source, count
    ):
        """Contract rule 9: an edit must be able to fail. A pattern that misses writes
        nothing and exits zero when the shell does it, so the loop records a
        verdict for a mutation that never happened -- the two-spaces incident
        `arm_check.run_arms`'s docstring records. One that lands twice breaks two
        units at once, and the verdict cannot say which one a case caught."""
        target = tmp_path / "target.py"
        target.write_text(source, encoding="utf-8")
        log = tmp_path / "ran.txt"
        before = snapshot(tmp_path)

        code, out = run(
            [
                target,
                "--replace",
                "OLD",
                "NEW",
                "--tests",
                cases_command(probe(tmp_path, SEES_FILE), target, log),
            ],
            capsys,
        )
        # The probe was written after the snapshot; take it out before comparing.
        after = snapshot(tmp_path)
        after.pop("probe.py")

        assert code == 2, out
        assert out.startswith("refused"), out
        assert f"{count} times" in out, f"the refusal does not name the count: {out}"
        assert after == before, "a refused replacement wrote something"
        assert not log.exists(), "a refused replacement still ran the cases"

    def test_a_replacement_that_lands_once_is_what_the_cases_see(
        self, tmp_path, capsys
    ):
        target = tmp_path / "target.py"
        target.write_text("VALUE = 15\n", encoding="utf-8")
        log = tmp_path / "seen.txt"

        run(
            [
                target,
                "--replace",
                "VALUE = 15",
                "VALUE = 25",
                "--tests",
                cases_command(probe(tmp_path, SEES_FILE), target, log),
            ],
            capsys,
        )
        assert log.read_text(encoding="utf-8") == "VALUE = 25\n"
        assert target.read_text(encoding="utf-8") == "VALUE = 15\n"

    @pytest.mark.parametrize(
        ("old", "new", "says"),
        [("", "x", "empty"), ("VALUE", "VALUE", "identical")],
        ids=["empty-old", "no-change"],
    )
    def test_a_replacement_that_mutates_nothing_is_refused(
        self, tmp_path, capsys, old, new, says
    ):
        """A mutation that changes no byte would read SURVIVED every time -- a
        verdict about the unmutated file, reported as a verdict about a unit."""
        target = tmp_path / "target.py"
        target.write_text("VALUE = 1\n", encoding="utf-8")
        code, out = run(
            [
                target,
                "--replace",
                old,
                new,
                "--tests",
                cases_command(probe(tmp_path, PASSES)),
            ],
            capsys,
        )
        assert code == 2, out
        assert out.startswith("refused") and says in out, out

    def test_a_file_that_is_not_utf8_text_is_refused_untouched(self, tmp_path, capsys):
        """The replacement is literal text, so a file that does not decode has no
        text to find it in. Re-encoded leniently it would come back different
        from the bytes it was read as, and the restore would be the mutation."""
        target = tmp_path / "blob.bin"
        original = b"OLD \xff\xfe not text\n"
        target.write_bytes(original)
        code, out = run(
            [
                target,
                "--replace",
                "OLD",
                "NEW",
                "--tests",
                cases_command(probe(tmp_path, FAILS)),
            ],
            capsys,
        )
        assert code == 2, out
        assert out.startswith("refused") and "UTF-8" in out, out
        assert target.read_bytes() == original

    def test_a_tests_command_that_names_nothing_is_refused(self, tmp_path, capsys):
        target = tmp_path / "target.py"
        target.write_text("VALUE = 1\n", encoding="utf-8")
        with pytest.raises(SystemExit) as raised:
            module().main([str(target), "--replace", "1", "2", "--tests", "  "])
        assert raised.value.code == 2
        assert "names no command" in capsys.readouterr().err
        assert target.read_text(encoding="utf-8") == "VALUE = 1\n"

    # --- S4 · restored from held bytes, and the restore is proved -----------

    @pytest.mark.parametrize(
        "cases",
        [
            REWRITES,
            # Removes the mutant. The restore compares the file with the kept
            # bytes before it writes (round 2, 🟡 9), and a file that cannot be
            # read has to count as differing, or this one is never written back.
            "import os, sys\n"
            "with open(sys.argv[1], encoding='utf-8') as f:\n"
            "    mutant = sys.argv[2] in f.read()\n"
            "if mutant:\n"
            "    os.remove(sys.argv[1])\n",
        ],
        ids=["rewritten", "removed"],
    )
    def test_the_file_is_restored_from_the_bytes_held_before_the_write(
        self, tmp_path, capsys, cases
    ):
        """Not from `HEAD`: `git checkout -- <file>` takes every uncommitted fix in
        the file with it, which is the round's work `agents/crafter.md`'s
        Boundaries says was wiped once. The cases here rewrite the file, or remove
        it, so the restore has something to undo besides the mutation."""
        target = tmp_path / "target.py"
        original = b"VALUE = 15\r\n# a CRLF and a byte the codec must keep: \xc3\xa9\n"
        target.write_bytes(original)

        run(
            [
                target,
                "--replace",
                "VALUE = 15",
                "VALUE = 25",
                "--tests",
                cases_command(probe(tmp_path, cases), target, "VALUE = 25"),
            ],
            capsys,
        )
        assert target.read_bytes() == original

    def test_a_restore_that_did_not_land_stops_the_run_and_says_so(
        self, tmp_path, capsys, monkeypatch
    ):
        """Every verdict taken against a file still holding its mutation is a
        verdict about the mutant. The command says so instead of printing one."""
        target = tmp_path / "target.py"
        target.write_text("VALUE = 15\n", encoding="utf-8")
        mc = module()

        def refuses(path, original, original_sha):
            raise RuntimeError(f"{path} was not restored: deadbeef != {original_sha}")

        monkeypatch.setattr(mc, "restore", refuses)
        code = mc.main(
            [
                str(target),
                "--replace",
                "VALUE = 15",
                "VALUE = 25",
                "--tests",
                red_on(tmp_path, target, "VALUE = 25"),
            ]
        )
        out = capsys.readouterr()
        text = out.out + out.err
        assert code == 2, text
        assert "was not restored" in text, text
        # The verdict word itself, not only the phrase the fake's message carries:
        # this is the line that tells a person the file holds a mutant (round 1,
        # 🟡 5).
        assert text.startswith("not restored:"), (
            f"the line that says the file still holds a mutation lost its verdict word: {text}"
        )

    @pytest.mark.skipif(
        os.name != "nt" and os.geteuid() == 0, reason="root writes a read-only file"
    )
    def test_a_restore_whose_write_raises_is_not_restored_and_exits_two(
        self, tmp_path, capsys
    ):
        """Round 1, 🟡 2. A restore can fail by raising as well as by landing the
        wrong bytes: the cases made the file read-only, or removed its directory,
        or a second Ctrl-C arrived inside the write. Each leaves the mutant on
        disk, which is the one outcome `not restored` exists to say."""
        target = tmp_path / "target.py"
        target.write_text("VALUE = 1\n", encoding="utf-8")
        try:
            code, out = run(
                [
                    target,
                    "--replace",
                    "VALUE = 1",
                    "VALUE = 2",
                    "--tests",
                    cases_command(
                        probe(tmp_path, LOCKS_THE_MUTANT), target, "VALUE = 2"
                    ),
                ],
                capsys,
            )
        finally:
            os.chmod(target, 0o644)
        assert code == 2, out
        assert out.startswith("not restored:"), out
        assert "PermissionError" in out, f"the cause is not named: {out}"

    # --- S7 · the verdict and the exit code say which of three things happened

    def test_cases_that_fail_against_the_mutant_read_red_and_exit_zero(
        self, tmp_path, capsys
    ):
        target = tmp_path / "target.py"
        target.write_text("VALUE = 1\n", encoding="utf-8")
        code, out = run(
            [
                target,
                "--replace",
                "1",
                "2",
                "--tests",
                cases_command(
                    probe(tmp_path, "print('the case output')\n" + FAILS_ON_THE_MUTANT),
                    target,
                    "VALUE = 2",
                ),
            ],
            capsys,
        )
        assert code == 0, out
        assert out.startswith("red"), out
        assert "the case output" in out, "the command's own output is not shown"
        first = out.splitlines()[0]
        assert re.search(r"\(\d+\.\ds\)$", first), (
            f"the verdict line no longer says how long the run took: {first}"
        )

    @pytest.mark.parametrize(
        ("exit_code", "why"),
        [
            (1, "a case already failing"),
            (5, "a -k that selects nothing"),
            (4, "a mistyped module"),
        ],
        ids=["failing", "nothing-selected", "usage-error"],
    )
    def test_cases_that_fail_without_the_mutation_measure_nothing(
        self, tmp_path, capsys, exit_code, why
    ):
        """Round 1, 🔴 1: a non-zero exit is red only when the cases passed
        against the file as it was. Otherwise a mistyped `-k` -- pytest's exit 5
        -- reads *a case watches this unit* for a file no case ran against, and
        the crafter hands over on it. So the cases run once against the file as it
        is, and a failure there is `no baseline`, exit 2, with the break never
        written."""
        target = tmp_path / "target.py"
        target.write_text("VALUE = 1\n", encoding="utf-8")
        log = tmp_path / "seen.txt"
        body = (
            SEES_FILE.replace('"w", encoding', '"a", encoding')
            + f"sys.exit({exit_code})\n"
        )
        code, out = run(
            [
                target,
                "--replace",
                "VALUE = 1",
                "VALUE = 2",
                "--tests",
                cases_command(probe(tmp_path, body), target, log),
            ],
            capsys,
        )
        assert code == 2, f"{why}: {out}"
        assert out.startswith("no baseline"), f"{why}: {out}"
        # The baseline's own exit, which is what tells a mistyped `-k` (5) from a
        # case already failing (1), and the sentence saying the break was never
        # written (round 2, ⬜ 12). Narrower than *nothing was written* since round
        # 3: the restore now covers the baseline, and puts back what its cases
        # changed.
        assert f"(exit {exit_code})" in out.splitlines()[0], f"{why}: {out}"
        assert "The break was never written" in out, f"{why}: {out}"
        assert target.read_text(encoding="utf-8") == "VALUE = 1\n"
        assert log.read_text(encoding="utf-8") == "VALUE = 1\n", (
            f"{why}: the cases saw a mutant after failing without one"
        )

    @pytest.mark.parametrize("kind", ["missing", "directory", "read-only"])
    def test_a_path_that_cannot_be_read_measures_nothing_and_exits_two(
        self, tmp_path, capsys, kind
    ):
        """Round 1, 🟡 3. Left to Python an uncaught exception exits 1, which is
        SURVIVED's code, so a mistyped path read as *nothing watches this unit*.

        Round 2, 🟡 9: a target read-only before the command starts never takes
        the break and still holds its original bytes, so `not restored` there
        would tell a person to restore a file nothing changed. It is a run that
        could not happen, and the file is left as it was."""
        if kind == "read-only" and os.name != "nt" and os.geteuid() == 0:
            pytest.skip("root writes a read-only file")
        names = {"missing": "no-such-file.py", "directory": "a-directory"}
        target = tmp_path / names.get(kind, "target.py")
        if kind == "directory":
            target.mkdir()
        if kind == "read-only":
            target.write_text("VALUE = 1\n", encoding="utf-8")
            os.chmod(target, 0o444)
        try:
            code, out = run(
                [
                    target,
                    "--replace",
                    "1",
                    "2",
                    "--tests",
                    cases_command(probe(tmp_path, PASSES)),
                ],
                capsys,
            )
        finally:
            if kind == "read-only":
                os.chmod(target, 0o644)
        assert code == 2, out
        assert out.startswith("could not run:"), out
        if kind == "read-only":
            assert "PermissionError" in out, f"the cause is not named: {out}"
            assert target.read_text(encoding="utf-8") == "VALUE = 1\n"

    @pytest.mark.skipif(os.name == "nt", reason="the process-group bound is POSIX's")
    def test_cases_that_exit_but_leave_a_child_on_the_output_read_red_at_once(
        self, tmp_path, capsys
    ):
        """Round 1, 🟡 4. A wait on the output pipe returns only when every
        holder has closed it, so a run that exited red at once read `timed out`
        after the whole bound -- 300 s per mutation at the default. The wait is on
        the process; and what the cases left behind is ended with them."""
        target = tmp_path / "target.py"
        target.write_text("VALUE = 1\n", encoding="utf-8")
        pid_file = tmp_path / "child.pid"
        started = time.monotonic()
        try:
            code, out = run(
                [
                    target,
                    "--replace",
                    "VALUE = 1",
                    "VALUE = 2",
                    "--tests",
                    cases_command(
                        probe(tmp_path, LEAVES_A_CHILD_ON_THE_OUTPUT),
                        target,
                        "VALUE = 2",
                        pid_file,
                    ),
                    "--timeout",
                    "20",
                ],
                capsys,
            )
            elapsed = time.monotonic() - started
            pid = read_pid(pid_file)
            assert pid is not None, "the cases never started their child"
            assert gone_within(pid, 5), "the run left the child the cases started"
        finally:
            end_if_alive(read_pid(pid_file))
        assert code == 0 and out.startswith("red"), out
        assert elapsed < 10, f"a run that exited at once took {elapsed:.1f}s to read"

    def test_output_that_is_not_utf8_does_not_cost_the_verdict(self, tmp_path, capsys):
        """Round 1, 🟡 5: the cases' output is shown, not trusted to decode."""
        target = tmp_path / "target.py"
        target.write_text("VALUE = 1\n", encoding="utf-8")
        code, out = run(
            [
                target,
                "--replace",
                "VALUE = 1",
                "VALUE = 2",
                "--tests",
                cases_command(probe(tmp_path, PRINTS_NOT_UTF8), target, "VALUE = 2"),
            ],
            capsys,
        )
        assert code == 0 and out.startswith("red"), out

    def test_cases_that_pass_against_the_mutant_read_survived_and_exit_one(
        self, tmp_path, capsys
    ):
        target = tmp_path / "target.py"
        target.write_text("VALUE = 1\n", encoding="utf-8")
        code, out = run(
            [
                target,
                "--replace",
                "1",
                "2",
                "--tests",
                cases_command(probe(tmp_path, PASSES)),
            ],
            capsys,
        )
        assert code == 1, out
        assert out.startswith("SURVIVED"), out

    @pytest.mark.parametrize(
        "error",
        ["this platform's", "one that names no file"],
        ids=["native", "no-filename"],
    )
    def test_a_command_that_cannot_start_measures_nothing_and_exits_two(
        self, tmp_path, capsys, monkeypatch, error
    ):
        """Not SURVIVED: nothing ran, so nothing was watched or not watched.

        The line names the program that could not start. On Windows the
        `FileNotFoundError` `Popen` raises carries no filename, so its text alone
        says *the system cannot find the file specified* and not which file: PR
        #698's `windows-latest` leg failed here. The second parameter raises that
        error on any platform."""
        target = tmp_path / "target.py"
        target.write_text("VALUE = 1\n", encoding="utf-8")
        missing = tmp_path / "no-such-runner"
        mc = module()
        if error == "one that names no file":

            def refuses(*_args, **_kwargs):
                raise FileNotFoundError(2, "The system cannot find the file specified")

            monkeypatch.setattr(mc.subprocess, "Popen", refuses)
        code = mc.main(
            [
                str(target),
                "--replace",
                "1",
                "2",
                "--tests",
                shlex.join([str(missing), "-q"]),
            ]
        )
        captured = capsys.readouterr()
        out = captured.out + captured.err
        assert code == 2, out
        assert out.startswith("could not start"), out
        assert str(missing) in out, f"the error is not named: {out}"
        # It failed in the baseline, so the break was never written, and the
        # verdict says which run it was -- in a sentence of its own, not as the
        # detail's last clause (round 3, ⬜ 16).
        assert (
            ". This was the run against the file as it is, before the mutation was written"
            in out
        ), out
        assert target.read_text(encoding="utf-8") == "VALUE = 1\n"

    def test_a_negative_bound_is_refused_rather_than_timing_every_run_out(
        self, tmp_path, capsys
    ):
        """`seal arms` refuses it for the same reason: a bound below zero ends
        every run before it starts, and a verdict nobody measured follows."""
        target = tmp_path / "target.py"
        target.write_text("VALUE = 1\n", encoding="utf-8")
        with pytest.raises(SystemExit) as raised:
            module().main(
                [
                    str(target),
                    "--replace",
                    "1",
                    "2",
                    "--tests",
                    cases_command(probe(tmp_path, FAILS)),
                    "--timeout",
                    "-1",
                ]
            )
        assert raised.value.code == 2
        assert "non-negative" in capsys.readouterr().err
        assert target.read_text(encoding="utf-8") == "VALUE = 1\n"

    # --- S8 · a file that is not Python is mutated the same way -------------

    def test_a_markdown_file_is_mutated_and_restored_the_same_way(
        self, tmp_path, capsys
    ):
        """The crafter's unit is often a sentence: `agents/*.md` and `skills/*.md`
        are what a session reads and acts on, and contract rule 14 pins them by case."""
        target = tmp_path / "notes.md"
        text = "# Notes\n\nThe sentence a case pins. Another one stays.\n"
        target.write_text(text, encoding="utf-8")
        log = tmp_path / "seen.txt"

        code, out = run(
            [
                target,
                "--replace",
                "The sentence a case pins. ",
                "",
                "--tests",
                cases_command(probe(tmp_path, SEES_FILE), target, log),
            ],
            capsys,
        )
        assert log.read_text(encoding="utf-8") == "# Notes\n\nAnother one stays.\n"
        assert target.read_text(encoding="utf-8") == text
        assert code == 1 and out.startswith("SURVIVED"), out
        assert not (tmp_path / "__pycache__").exists()

    # --- S5 · a run that never returns ends at the bound, and so does its child

    @pytest.mark.skipif(os.name == "nt", reason="the process-group bound is POSIX's")
    @pytest.mark.parametrize(
        "hangs",
        ["the mutated run", "the baseline"],
        ids=["mutated", "baseline"],
    )
    def test_a_run_past_the_bound_is_timed_out_and_leaves_nothing_it_started(
        self, tmp_path, capsys, hangs
    ):
        """#577: a mutated run hung for 32 minutes. #313 measured why a bound in
        the loop is not enough by itself: `subprocess.run`'s timeout ends the
        direct child, and `bin/test` puts pytest one process further down, so the
        suite outlives the verdict and runs on, unbounded and unreported.

        Not red, not SURVIVED: neither was measured.

        Round 2, 🟡 10: a hang that does not depend on the break -- the common
        kind -- now happens in the baseline, before anything is written, so that
        run's bound is the one most hangs meet and is held here too. Its fixture
        is the same wrapper with the gate turned round: it hangs against the file
        as it is."""
        body = STARTS_A_CHILD
        if hangs == "the baseline":
            body = STARTS_A_CHILD.replace(
                "if sys.argv[2] not in f.read():", "if sys.argv[2] in f.read():"
            )
            assert body != STARTS_A_CHILD, "the fixture did not change"
        target = tmp_path / "under_test.py"
        original = b"VALUE = 1\n"
        target.write_bytes(original)
        pid_file = tmp_path / "child.pid"
        started = time.monotonic()
        try:
            code, out = run(
                [
                    target,
                    "--replace",
                    "VALUE = 1",
                    "VALUE = 2",
                    "--tests",
                    starts_a_child(tmp_path, target, pid_file, body),
                    "--timeout",
                    "1",
                ],
                capsys,
            )
            elapsed = time.monotonic() - started
            pid = read_pid(pid_file)
            assert pid is not None, "the wrapper never started its child"
            assert gone_within(pid, 5), (
                "the bound ended the wrapper and left the process it started "
                "running -- a wrapper's pytest outliving the verdict, #313"
            )
        finally:
            end_if_alive(read_pid(pid_file))
        assert code == 2, out
        assert out.startswith("timed out after 1s"), out
        assert elapsed < 15, f"the bound of 1s took {elapsed:.1f}s to end {hangs}"
        assert target.read_bytes() == original
        assert not list(tmp_path.glob("__pycache__/under_test.*.pyc"))
        if hangs == "the baseline":
            assert (
                ". This was the run against the file as it is, before the mutation "
                "was written" in out
            ), out

    @pytest.mark.skipif(os.name == "nt", reason="the process-group bound is POSIX's")
    def test_a_process_outside_the_group_does_not_hold_the_verdict_back(
        self, tmp_path, capsys
    ):
        """A process that started a session of its own is outside the group, so
        the kill does not reach it, and it holds the cases' output for as long as
        it runs. Nothing after the kill may wait on that output, or the hang is
        back one step later; the verdict names the escape as the bound's limit."""
        assert STARTS_AN_ESCAPED_CHILD != STARTS_A_CHILD, "the fixture did not change"
        mc = module()
        target = tmp_path / "under_test.py"
        target.write_bytes(b"VALUE = 1\n")
        pid_file = tmp_path / "child.pid"
        started = time.monotonic()
        try:
            code = mc.main(
                [
                    str(target),
                    "--replace",
                    "VALUE = 1",
                    "VALUE = 2",
                    "--tests",
                    starts_a_child(tmp_path, target, pid_file, STARTS_AN_ESCAPED_CHILD),
                    "--timeout",
                    "1",
                ]
            )
            elapsed = time.monotonic() - started
        finally:
            end_if_alive(read_pid(pid_file))
        out = capsys.readouterr().out
        assert elapsed < 15, (
            f"collecting the output waited {elapsed:.1f}s on the escaped child"
        )
        assert code == 2 and out.startswith("timed out after 1s"), out
        assert "session of its own" in out, out
        assert target.read_bytes() == b"VALUE = 1\n"

    # --- Ctrl-C ends what the run started, then restores --------------------

    @pytest.mark.skipif(os.name == "nt", reason="the process-group bound is POSIX's")
    @pytest.mark.parametrize(
        "lands",
        ["the mutated run", "the baseline"],
        ids=["mutated", "baseline"],
    )
    def test_an_interrupt_ends_the_run_it_started_and_restores_the_file(
        self, tmp_path, capsys, monkeypatch, lands
    ):
        """The run is in a session of its own, so the terminal's Ctrl-C reaches
        this process and not the cases (#313 names that consequence). So the
        interrupt has to end the group here, or the suite runs on after the
        command has gone. Delivered as the `KeyboardInterrupt` Python raises for
        it, once the child is known to be running.

        Round 3, 🟡 15: the line then says the file holds the bytes it held
        before the command started, and that has to be true wherever the
        interrupt lands. The cases can write the file during the baseline, before
        any break exists, so the restore covers the baseline too."""
        target = tmp_path / "under_test.py"
        original = b"VALUE = 1\n"
        target.write_bytes(original)
        pid_file = tmp_path / "child.pid"
        mc = module()
        real_wait = mc._wait

        def interrupted(proc, timeout):
            if lands == "the baseline":
                # The cases finish what they write, then the Ctrl-C lands: the
                # first wait is the baseline's.
                proc.wait()
                raise KeyboardInterrupt
            # Against the file as it is the cases pass at once; the interrupt
            # lands in the mutated run, while the mutant is on disk.
            if "VALUE = 2" not in target.read_text(encoding="utf-8"):
                return real_wait(proc, timeout)
            deadline = time.monotonic() + 10
            while read_pid(pid_file) is None and time.monotonic() < deadline:
                time.sleep(0.05)
            raise KeyboardInterrupt

        cases = starts_a_child(tmp_path, target, pid_file)
        if lands == "the baseline":
            cases = cases_command(
                probe(
                    tmp_path,
                    "import sys\n"
                    "with open(sys.argv[1], 'w', encoding='utf-8') as f:\n"
                    "    f.write('VALUE = 99\\n')\n",
                    "rewrites.py",
                ),
                target,
            )
        monkeypatch.setattr(mc, "_wait", interrupted)
        try:
            code = mc.main(
                [
                    str(target),
                    "--replace",
                    "VALUE = 1",
                    "VALUE = 2",
                    "--tests",
                    cases,
                ]
            )
            out = capsys.readouterr().out
            if lands == "the mutated run":
                pid = read_pid(pid_file)
                assert pid is not None, "the wrapper never started its child"
                assert gone_within(pid, 5), (
                    "the interrupt left the process the run started"
                )
        finally:
            end_if_alive(read_pid(pid_file))
            monkeypatch.setattr(mc, "_wait", real_wait)
        assert code == 2, out
        assert out.startswith("interrupted"), out
        # What holds whether the interrupt landed in the baseline or after the
        # write, rather than a restore that may never have happened (round 2, ⬜ 12).
        assert "holds the bytes it held before the command started" in out, out
        assert target.read_bytes() == original


class Test_module:
    @pytest.mark.skipif(
        os.name == "nt", reason="the POSIX wrapper; its .cmd twin is read, not run"
    )
    def test_the_command_a_session_types_reaches_the_script(self, tmp_path):
        """`bin/seal mutate`, run the way the Bash tool runs it, through the
        shell: the verdict and the exit code arrive unchanged."""
        target = tmp_path / "target.py"
        target.write_text("VALUE = 1\n", encoding="utf-8")
        done = subprocess.run(
            [
                WRAPPER,
                "mutate",
                str(target),
                "--replace",
                "1",
                "2",
                "--tests",
                red_on(tmp_path, target, "VALUE = 2"),
            ],
            capture_output=True,
            encoding="utf-8",
            timeout=60,
        )
        assert done.returncode == 0, done.stdout + done.stderr
        assert done.stdout.startswith("red"), done.stdout + done.stderr
        assert target.read_text(encoding="utf-8") == "VALUE = 1\n"

    @pytest.mark.skipif(os.name == "nt", reason="the process-group bound is POSIX's")
    def test_a_group_that_ended_on_its_own_at_the_bound_is_not_an_error(self):
        """The command can finish between the bound expiring and the kill. The
        group is gone by then, and the run is still a `timed out` rather than a
        traceback that skips the verdict."""
        mc = module()
        proc = subprocess.Popen(
            [sys.executable, "-c", "pass"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding="utf-8",
            start_new_session=True,
        )
        proc.communicate(timeout=30)
        mc._end(proc, mc.GROUP)
        assert proc.returncode == 0

    # --- S6 · the Windows half ends the direct child and says what it did not

    def test_the_bound_is_chosen_by_the_platform_and_windows_says_what_it_left(self):
        """Contract rule 13: a defence resting on a platform's guarantee is asked without it.
        The chooser takes the platform as an argument, so the Windows half is
        pinned from a machine that is not Windows."""
        mc = module()
        assert mc.strategy("posix") == mc.GROUP
        assert mc.strategy("nt") == mc.CHILD
        windows = mc.timed_out_detail(5.0, mc.CHILD)
        assert "after 5s" in windows
        assert "not ended" in windows, (
            f"the Windows verdict does not say that what the command started may "
            f"still be running: {windows}"
        )
        posix = mc.timed_out_detail(5.0, mc.GROUP)
        assert "not ended" not in posix and "process group" in posix, posix


test_census = census_case(TARGET)
