"""A script run below the plugin's Python floor says what it needs.

Issue #226: `round_record.py` died on a 3.9 `python3` with `TypeError: zip()
takes no keyword arguments`, after it had parsed its arguments and read the
report, so the failure read as a bug in the report and named neither the
version needed nor the flag. macOS still ships 3.9 as `/usr/bin/python3`.

`lib/launch.py` holds the floor once. Every `bin/` wrapper but `bin/test`,
and its `.cmd` twin, runs its script through it, and below the floor it
answers with one sentence and exit 2 before the script is read. These cases
pin that sentence, the moment it arrives, and that the launched script cannot
tell it was launched. That the floor has one source, and that no wrapper but
`bin/test` goes around it, read the tracked files and `bin/`, so
`tests/behaviour/test_every_entry_point_runs_at_the_floor.py` holds them.

**Testing a floor from an interpreter above it.** A copy of the launcher with
`FLOOR` moved is run instead of the real file: every other line is the
shipped line. The substitution asserts it matched once, because a test whose
edit missed passes by testing an unmodified file.
"""

import importlib.util
import json
import os
import re
import subprocess
import sys

from conftest import ROOT, census_case, read

TARGET = "lib/launch.py"

LAUNCH = os.path.join(ROOT, "lib", "launch.py")

FLOOR_LINE = re.compile(r"^FLOOR = \(\d+, \d+\)$", re.M)

# A script that says what it saw. It imports a sibling, so a launch that left
# `sys.path[0]` on the launcher's directory fails at the import, and it
# writes a mark before anything else, so a refusal that came after it shows.
PROBE = """import json, os, sys
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ran"), "w").close()
import probe_sibling
print(json.dumps({
    "argv": sys.argv, "path0": sys.path[0], "file": __file__,
    "name": __name__, "sibling": probe_sibling.NAME,
}))
sys.exit(int(sys.argv[1]))
"""


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def launcher(tmp_path, floor):
    """A copy of the launcher holding `floor`, under `tmp_path/lib`."""
    text, count = FLOOR_LINE.subn(f"FLOOR = {tuple(floor)!r}", read(LAUNCH))
    assert count == 1, (
        f"lib/launch.py spells its floor {count} times as `FLOOR = (x, y)`, "
        "so this case would be moving no floor or the wrong one"
    )
    copy = tmp_path / "lib" / "launch.py"
    copy.parent.mkdir()
    copy.write_text(text, encoding="utf-8")
    return str(copy)


def probe(tmp_path):
    """The probe script and its sibling, under `tmp_path/scripts`."""
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    (scripts / "probe_sibling.py").write_text('NAME = "sibling"\n', encoding="utf-8")
    script = scripts / "probe_case.py"
    script.write_text(PROBE, encoding="utf-8")
    return str(script)


def run(*command, cwd):
    return subprocess.run(
        [sys.executable, *command],
        cwd=cwd,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


# --- the sentence, and the moment it arrives ----------------------------------


class Test_main:
    def test_accepts_the_floor_and_runs_the_script_as_if_run_directly(self, tmp_path):
        """At the floor itself, the launched script sees what a direct run sees:
        its arguments, `sys.path[0]`, `__file__` and `__name__`, and its exit
        code reaches the caller. A floor that refused itself would stop every
        command at the next release."""
        script = probe(tmp_path)
        args = (script, "3", "two words", "--flag")
        direct = run(*args, cwd=tmp_path)
        launched = run(launcher(tmp_path, sys.version_info[:2]), *args, cwd=tmp_path)
        assert direct.returncode == 3, direct.stderr
        assert (launched.returncode, launched.stderr) == (3, ""), launched.stderr
        assert json.loads(launched.stdout) == json.loads(direct.stdout)

    def test_refuses_below_the_floor_before_the_script_runs(
        self, tmp_path, monkeypatch, capsys
    ):
        """Exit 2, a sentence rather than a traceback, and the script never ran.

        The process half runs a copy with its floor raised, so the exit code and
        the moment are the shipped file's. The sentence half asks the real
        `main` with its floor raised in place, where the decision is made. The
        sentence names the floor and the version found, or a reader whose
        `python3` is secretly 3.9 cannot tell whether it means them; the
        interpreter's path, because on macOS the surprise is which file `python3`
        was; the command, because a reader typed the wrapper and not the file."""
        script = probe(tmp_path)
        out = run(launcher(tmp_path, (99, 0)), script, "0", cwd=tmp_path)
        assert out.returncode == 2, (out.returncode, out.stderr)
        assert "Traceback" not in out.stderr, out.stderr
        assert not out.stdout, out.stdout
        launch = load(LAUNCH, "agentic_launch_refusal")
        monkeypatch.setattr(launch, "FLOOR", (99, 0))
        assert launch.main(["launch.py", script, "0"]) == 2
        assert not (tmp_path / "scripts" / "ran").exists(), (
            "the script ran before the refusal, so the refusal is not at entry"
        )
        found = ".".join(str(part) for part in sys.version_info[:3])
        err = capsys.readouterr().err
        assert err.startswith(
            f"probe-case: needs python 99.0 or newer, and this is python {found} "
            f"at {sys.executable}.\n"
            "Nothing was read and nothing was written.\n"
        ), err
        assert "macOS ships python 3.9 under that name" in err, err
        # #1148: the sentence ends at the command to type. A user meets it in
        # their own repository, where no `CONTRIBUTING.md` of this plugin's
        # stands, so it names no document of this repository.
        assert err.endswith(f"so name one explicitly: `python99.0 {script} ...`.\n"), (
            err
        )
        assert "CONTRIBUTING" not in err, err


class Test_module:
    def test_the_refusal_is_ascii_whatever_path_it_names(self):
        """The refusal is written before anything sets up stderr, so a path the
        console cannot encode would end it in a traceback, on the machine that
        has no other way of being told what is wrong."""
        launch = load(LAUNCH, "agentic_launch_ascii")
        sentence = launch.refusal(
            "/Users/x/코드/round_record.py", (3, 9, 6), "/Users/x/파이썬/python3"
        )
        stowaways = sorted({c for c in sentence if not c.isascii()})
        assert not stowaways, f"the refusal carries {stowaways}"


test_census = census_case(TARGET)
