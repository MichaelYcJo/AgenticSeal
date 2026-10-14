"""A script run below the plugin's Python floor says what it needs.

Issue #226: `round_record.py` died on a 3.9 `python3` with `TypeError: zip()
takes no keyword arguments`, after it had parsed its arguments and read the
report, so the failure read as a bug in the report and named neither the
version needed nor the flag. macOS still ships 3.9 as `/usr/bin/python3`.

`hooks/launch.py` holds the floor once. Every `bin/` wrapper and `.cmd` twin
runs its script through it, and below the floor it answers with one sentence
and exit 2 before the script is read. These cases pin that sentence, the
moment it arrives, that the launched script cannot tell it was launched, that
the floor has one source, and that no wrapper goes around it.

**Testing a floor from an interpreter above it.** A copy of the launcher with
`FLOOR` moved is run instead of the real file: every other line is the
shipped line. The substitution asserts it matched once, because a test whose
edit missed passes by testing an unmodified file.
"""

import ast
import importlib.util
import json
import os
import re
import subprocess
import sys

from conftest import git_listing, on_disk

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BIN = os.path.join(ROOT, "bin")
LAUNCH = os.path.join(ROOT, "hooks", "launch.py")
RUNNER = os.path.join(ROOT, ".github", "scripts", "run_tests.py")
RUFF = os.path.join(ROOT, "ruff.toml")

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


def read(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def launcher(tmp_path, floor):
    """A copy of the launcher holding `floor`, under `tmp_path/hooks`."""
    text, count = FLOOR_LINE.subn(f"FLOOR = {tuple(floor)!r}", read(LAUNCH))
    assert count == 1, (
        f"hooks/launch.py spells its floor {count} times as `FLOOR = (x, y)`, "
        "so this case would be moving no floor or the wrong one"
    )
    copy = tmp_path / "hooks" / "launch.py"
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


def test_below_the_floor_the_launcher_refuses_before_the_script_runs(
    tmp_path, monkeypatch, capsys
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
    launch = load(LAUNCH, "specseal_launch_refusal")
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


def test_at_the_floor_the_script_runs_as_if_it_were_run_directly(tmp_path):
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


def test_the_refusal_is_ascii_whatever_path_it_names():
    """The refusal is written before anything sets up stderr, so a path the
    console cannot encode would end it in a traceback, on the machine that
    has no other way of being told what is wrong."""
    launch = load(LAUNCH, "specseal_launch_ascii")
    sentence = launch.refusal(
        "/Users/x/코드/round_record.py", (3, 9, 6), "/Users/x/파이썬/python3"
    )
    stowaways = sorted({c for c in sentence if not c.isascii()})
    assert not stowaways, f"the refusal carries {stowaways}"


# --- one number --------------------------------------------------------------


def floor_carriers(root=ROOT):
    """`{path: floor}` for every tracked `.py` on disk whose module level
    assigns `FLOOR` a tuple literal, read with `ast` rather than imported. A
    tracked file the working tree deleted carries nothing and is left out."""

    listed, _missing = on_disk(root, git_listing(root, "ls-files", "*.py"))
    found = {}
    for rel in listed:
        text = read(os.path.join(root, rel))
        if "FLOOR" not in text:
            continue
        for node in ast.parse(text).body:
            if (
                isinstance(node, ast.Assign)
                and any(
                    isinstance(t, ast.Name) and t.id == "FLOOR" for t in node.targets
                )
                and isinstance(node.value, ast.Tuple)
            ):
                found[rel] = ast.literal_eval(node.value)
    return found


def test_the_floor_has_one_source():
    """`hooks/launch.py` is the one file that spells the floor, the runner
    builds its virtualenv against the launcher's number, and `ruff.toml`,
    which cannot import, lints at that number."""
    floor = tuple(load(LAUNCH, "specseal_launch_floor").FLOOR)
    assert floor_carriers() == {"hooks/launch.py": floor}, floor_carriers()
    assert tuple(load(RUNNER, "specseal_runner_floor").FLOOR) == floor
    m = re.search(r'target-version = "py(\d)(\d+)"', read(RUFF))
    assert m, "ruff.toml lost its target-version"
    assert (int(m.group(1)), int(m.group(2))) == floor, (
        f"hooks/launch.py holds {floor} and ruff.toml lints at "
        f"{m.group(1)}.{m.group(2)}"
    )


# --- no way around it ---------------------------------------------------------

INTERPRETERS = {"python3", "python", "py"}


def launches(text):
    """`[(line, first argument)]` for every line of a wrapper whose command is
    an interpreter, after an `exec` and past `py`'s `-3`. Comments, sh's `#`
    and cmd's `rem`, are skipped, and so is a line naming an interpreter as an
    argument, `where /q py`."""
    found = []
    for line in text.split("\n"):
        words = line.split()
        if not words or words[0].startswith("#") or words[0].lower() == "rem":
            continue
        if words[0] == "exec":
            words = words[1:]
        if not words or words[0] not in INTERPRETERS:
            continue
        rest = words[1:]
        if words[0] == "py" and rest[:1] == ["-3"]:
            rest = rest[1:]
        found.append((line.strip(), rest[0] if rest else ""))
    return found


def test_every_wrapper_runs_its_script_through_the_launcher():
    """Every file in `bin/`, found by listing it: each interpreter it starts
    is handed the launcher first, so a wrapper added later is held the day it
    is written."""
    unheld = {}
    for entry in sorted(os.listdir(BIN)):
        text = read(os.path.join(BIN, entry))
        if entry.endswith(".cmd"):
            first = '"%launch%"'
            defined = 'set "launch=%here%..\\hooks\\launch.py"' in text
        else:
            first, defined = '"$here/../hooks/launch.py"', True
        found = launches(text)
        bypass = [line for line, arg in found if arg != first]
        if not found or bypass or not defined:
            unheld[entry] = bypass or "starts no interpreter through the launcher"
    assert not unheld, unheld
