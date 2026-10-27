"""A script run below the plugin's Python floor says what it needs.

Issue #226: `round_record.py` died on a 3.9 `python3` with `TypeError: zip()
takes no keyword arguments`, after it had parsed its arguments and read the
report, so the failure read as a bug in the report and named neither the
version needed nor the flag. macOS still ships 3.9 as `/usr/bin/python3`.

`hooks/lib/launch.py` holds the floor once. Every `bin/` wrapper but `bin/test`,
and its `.cmd` twin, runs its script through it, and below the floor it
answers with one sentence and exit 2 before the script is read. These cases
pin that sentence, the moment it arrives, that the launched script cannot
tell it was launched, that the floor has one source, and that no wrapper but
`bin/test` goes around it.

**Testing a floor from an interpreter above it.** A copy of the launcher with
`FLOOR` moved is run instead of the real file: every other line is the
shipped line. The substitution asserts it matched once, because a test whose
edit missed passes by testing an unmodified file.
"""

import ast
import importlib.util
import json
import os
import posixpath
import re
import subprocess
import sys

from censuses import matches, ruff_targets
from conftest import census_case, decline_if_shrunken, git_listing, on_disk, read

TARGET = "hooks/lib/launch.py"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BIN = os.path.join(ROOT, "bin")
LAUNCH = os.path.join(ROOT, "hooks", "lib", "launch.py")
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


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def launcher(tmp_path, floor):
    """A copy of the launcher holding `floor`, under `tmp_path/hooks`."""
    text, count = FLOOR_LINE.subn(f"FLOOR = {tuple(floor)!r}", read(LAUNCH))
    assert count == 1, (
        f"hooks/lib/launch.py spells its floor {count} times as `FLOOR = (x, y)`, "
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

    def test_the_floor_has_one_source(self):
        """`hooks/lib/launch.py` is the one file that spells the floor, the runner
        builds its virtualenv against the launcher's number, and `ruff.toml`,
        which cannot import, lints at that number."""
        floor = tuple(load(LAUNCH, "agentic_launch_floor").FLOOR)
        assert floor_carriers() == {"hooks/lib/launch.py": floor}, floor_carriers()
        assert tuple(load(RUNNER, "agentic_runner_floor").FLOOR) == floor
        m = re.search(r'target-version = "py(\d)(\d+)"', read(RUFF))
        assert m, "ruff.toml lost its target-version"
        assert (int(m.group(1)), int(m.group(2))) == floor, (
            f"hooks/lib/launch.py holds {floor} and ruff.toml lints at "
            f"{m.group(1)}.{m.group(2)}"
        )

    def test_every_wrapper_runs_its_script_through_the_launcher(self):
        """Every file in `bin/`, found by listing it: each interpreter it starts
        is handed the launcher first, so a wrapper added later is held the day it
        is written. `bin/test` and its twin are the one exception, held the other
        way: each interpreter they start is handed the runner, so a launcher put
        back in front of it refuses the old `python3` the runner exists to get
        past."""
        unheld = {}
        for entry in sorted(os.listdir(BIN)):
            text = read(os.path.join(BIN, entry))
            if entry in RUNS_ITS_RUNNER_DIRECTLY:
                first, defined = RUNS_ITS_RUNNER_DIRECTLY[entry], True
            elif entry.endswith(".cmd"):
                first = '"%launch%"'
                defined = 'set "launch=%here%..\\hooks\\lib\\launch.py"' in text
            else:
                first, defined = '"$here/../hooks/lib/launch.py"', True
            found = launches(text)
            bypass = [line for line, arg in found if arg != first]
            if not found or bypass or not defined:
                unheld[entry] = bypass or "starts no interpreter through the launcher"
        assert not unheld, unheld

    def test_what_runs_before_any_floor_is_linted_at_the_floor(self):
        """The launcher holds the floor for `bin/`, and nothing holds it for a
        hook, a git hook, the launcher itself or `bin/test`'s runner: each runs on
        whatever `python3` starts it, 3.9 on a stock macOS, and so does every
        module it loads in its own process. A hook that raises there fails open,
        and the Stop hook loses the stamp it claimed. `ruff.toml` lints that set
        at the version its `per-file-target-version` names, so B905 and UP017 do
        not ask it for `zip`'s `strict=` or `datetime.UTC`. This case holds the
        set to that table, both ways; the `floor_syntax` census in
        `tests/censuses.py` refuses in each file the table names what a
        `python3` at its version cannot run."""
        loads = (
            'import a\nfrom e import f\nG = ("b.py",)\n'
            'D = os.path.join(H, "..", "s", "d.py")\n'
        )
        tracked = {"hooks/a.py", "hooks/b.py", "hooks/c.py", "hooks/e.py", "s/d.py"}
        assert loaded_by("hooks/c.py", loads, tracked) == tracked - {"hooks/c.py"}
        unfloored, missing = before_any_floor()
        targets = ruff_targets(RUFF)
        assert {"hooks/dispatch.py", "hooks/lib/launch.py"} <= unfloored, unfloored
        unlinted = sorted(
            r for r in unfloored if not any(matches(p, r) for p in targets)
        )
        assert not unlinted, (
            f"{unlinted} run before any floor is checked and ruff lints them at the "
            "floor; add them to ruff.toml's per-file-target-version"
        )
        stale = sorted(p for p in targets if not any(matches(p, r) for r in unfloored))
        if stale:
            decline_if_shrunken(missing, "the liveness half of per-file-target-version")
        assert not stale, f"ruff.toml lints {stale} as if a floor-less run reached them"

    def test_a_hook_reaches_the_modules_under_lib(self):
        """#1060. A gate at the top of `hooks/` puts `hooks/lib/` on its
        `sys.path` and imports a module there by its bare name, so `loaded_by`
        follows that import into `hooks/lib/`. A walk that looked only beside
        the gate and in `hooks/` would find none of them, and the set above
        would shrink to the gates without failing."""
        tracked = {"hooks/g.py", "hooks/lib/a.py", "hooks/lib/b.py"}
        assert loaded_by("hooks/g.py", "import a\nfrom b import c\n", tracked) == {
            "hooks/lib/a.py",
            "hooks/lib/b.py",
        }


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


# The one pair that hands its interpreter the runner itself, and what it hands
# it: `hooks/lib/launch.py`'s docstring says why `bin/test` is not launched.
RUNS_ITS_RUNNER_DIRECTLY = {"test": '"$script"', "test.cmd": '"%script%"'}


# --- what runs before any floor is checked -------------------------------------

# Where a hook command names its script.
PLUGIN_SCRIPT = re.compile(r"\$\{CLAUDE_PLUGIN_ROOT\}/([\w./-]+\.py)")
# A wrapper's own variables, sh's `name="value"` and cmd's `set "name=value"`.
ASSIGNED = re.compile(r'^\s*(?:set ")?(\w+)="?([^"\n]*?)"?\s*$', re.M)
VARIABLE = re.compile(r"\$(\w+)|%(\w+)%")
# A file named by itself, as `hooks/dispatch.py` names its gates.
BARE_SCRIPT = re.compile(r"[\w-]+\.py")


def handed_first(text):
    """The repository paths a `bin/` wrapper's text hands its interpreters
    first, with the wrapper's own variables filled in and its `here` read as
    `bin/`."""
    values = {name: value for name, value in ASSIGNED.findall(text)}
    values["here"] = "bin/"
    found = set()
    for _line, arg in launches(text):
        path = arg.strip('"')
        for _ in range(len(values)):
            path = VARIABLE.sub(lambda m: values.get(m[1] or m[2], m[0]), path)
        found.add(posixpath.normpath(path.replace("\\", "/")))
    return found


def loaded_by(rel, text, tracked):
    """The tracked `.py` files the module at `rel` loads in its own process:
    one it imports that sits beside it, in `hooks/`, where a hook's
    `sys.path[0]` is, or in `hooks/lib/`, which each gate inserts before it;
    a bare `<name>.py` beside it; and the path an
    `os.path.join` spells whose last string part ends in `.py`, `..` left
    out. A module that does not parse here loads nothing."""
    here = posixpath.dirname(rel)
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return set()
    found = set()
    for node in ast.walk(tree):
        names = []
        if isinstance(node, ast.Import):
            names = [alias.name.split(".")[0] for alias in node.names]
        elif isinstance(node, ast.ImportFrom) and not node.level and node.module:
            names = [node.module.split(".")[0]]
        found |= {
            posixpath.join(d, f"{n}.py")
            for n in names
            for d in (here, "hooks", "hooks/lib")
        }
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if BARE_SCRIPT.fullmatch(node.value):
                found.add(posixpath.join(here, node.value))
        if isinstance(node, ast.Call) and getattr(node.func, "attr", "") == "join":
            parts = [
                a.value
                for a in node.args
                if isinstance(a, ast.Constant) and isinstance(a.value, str)
            ]
            if parts and parts[-1].endswith(".py"):
                tail = "/".join(p for p in parts if p not in ("..", "."))
                found |= {t for t in tracked if t == tail or t.endswith("/" + tail)}
    return found & tracked


def before_any_floor(root=ROOT):
    """`(paths, missing)`: every tracked `.py` an interpreter may run before
    any floor is checked, and the tracked paths the working tree deleted.

    It starts from what is handed an interpreter with nothing in front of it:
    each script `hooks/hooks.json` names and the file each `bin/` wrapper
    hands its interpreter first. Then it follows `loaded_by` until nothing
    new is found. It errs over, since a string can name a file nothing loads,
    and under, for a module reached by a path built any other way. No git
    hook of this plugin runs a script since #1027."""
    listed, missing = on_disk(root, git_listing(root, "ls-files", "*.py"))
    tracked = set(listed)
    start = set(PLUGIN_SCRIPT.findall(read(os.path.join(root, "hooks", "hooks.json"))))
    for entry in sorted(os.listdir(os.path.join(root, "bin"))):
        start |= handed_first(read(os.path.join(root, "bin", entry)))
    seen, todo = set(), sorted(start & tracked)
    while todo:
        rel = todo.pop()
        if rel not in seen:
            seen.add(rel)
            todo += sorted(loaded_by(rel, read(os.path.join(root, rel)), tracked))
    return seen, missing


test_census = census_case(TARGET)
