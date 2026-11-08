"""A script run below the plugin's Python floor says what it needs.

Issue #226: `round_record.py` died on a 3.9 `python3` with `TypeError: zip()
takes no keyword arguments`, after it had parsed its arguments and read the
report, so the failure read as a bug in the report and named neither the
version needed nor the flag. macOS still ships 3.9 as `/usr/bin/python3`.

`lib/launch.py` holds the floor once. Every `bin/` wrapper but `bin/test`,
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
import shlex
import subprocess
import sys

from censuses import matches, ruff_targets
from conftest import ROOT, census_case, decline_if_shrunken, git_listing, on_disk, read

TARGET = "lib/launch.py"

BIN = os.path.join(ROOT, "bin")
LAUNCH = os.path.join(ROOT, "lib", "launch.py")
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

    def test_the_floor_has_one_source(self):
        """`lib/launch.py` is the one file that spells the floor, the runner
        builds its virtualenv against the launcher's number, and `ruff.toml`,
        which cannot import, lints at that number."""
        floor = tuple(load(LAUNCH, "agentic_launch_floor").FLOOR)
        assert floor_carriers() == {"lib/launch.py": floor}, floor_carriers()
        assert tuple(load(RUNNER, "agentic_runner_floor").FLOOR) == floor
        m = re.search(r'target-version = "py(\d)(\d+)"', read(RUFF))
        assert m, "ruff.toml lost its target-version"
        assert (int(m.group(1)), int(m.group(2))) == floor, (
            f"lib/launch.py holds {floor} and ruff.toml lints at "
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
                defined = 'set "launch=%here%..\\lib\\launch.py"' in text
            else:
                first, defined = '"$here/../lib/launch.py"', True
            found = launches(text)
            bypass = [line for line, arg in found if arg != first]
            if not found or bypass or not defined:
                unheld[entry] = bypass or "starts no interpreter through the launcher"
        assert not unheld, unheld

    def test_what_runs_before_any_floor_is_linted_at_the_floor(self):
        """The launcher holds the floor for `bin/`, and nothing holds it for
        the scripts `hooks/hooks.json`'s commands run, the launcher itself or
        `bin/test`'s runner: each runs on whatever `python3` starts it, 3.9 on
        a stock macOS, and so does every module it loads in its own process.
        A drawer that raises there loses the stamp it claimed, and the
        `Stop` hook draws nothing. `ruff.toml` lints that set
        at the version its `per-file-target-version` names, so B905 and UP017 do
        not ask it for `zip`'s `strict=` or `datetime.UTC`. This case holds the
        set to that table, both ways; the `floor_syntax` census in
        `tests/censuses.py` refuses in each file the table names what a
        `python3` at its version cannot run."""
        loads = (
            'import a\nfrom e import f\nG = ("b.py",)\n'
            'D = os.path.join(H, "..", "s", "d.py")\n'
        )
        tracked = {"x/a.py", "x/b.py", "x/c.py", "x/e.py", "s/d.py"}
        assert loaded_by("x/c.py", loads, tracked) == tracked - {"x/c.py"}
        unfloored, missing = before_any_floor()
        targets = ruff_targets(RUFF)
        assert {
            "skills/verify/scripts/seal_stamp.py",
            "hooks/core-start.py",
            "lib/core.py",
            "lib/launch.py",
        } <= unfloored, unfloored
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

    def test_a_script_reaches_the_modules_under_lib(self):
        """#1060. A script that puts `lib/` on its `sys.path` imports a module
        there by its bare name, as `skills/implement/scripts/seal.py` does, so
        `loaded_by` follows that import into `lib/`. A walk that looked only
        beside the script would find none of them, and the set above would
        shrink without failing."""
        tracked = {"skills/g.py", "lib/a.py", "lib/b.py"}
        assert loaded_by("skills/g.py", "import a\nfrom b import c\n", tracked) == {
            "lib/a.py",
            "lib/b.py",
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
# it: `lib/launch.py`'s docstring says why `bin/test` is not launched.
RUNS_ITS_RUNNER_DIRECTLY = {"test": '"$script"', "test.cmd": '"%script%"'}


# --- what runs before any floor is checked -------------------------------------

# The plugin's hook registration: each command hands its interpreter a script
# under the plugin root, which the harness spells `${CLAUDE_PLUGIN_ROOT}`.
HOOKS = ("hooks", "hooks.json")
PLUGIN_ROOT = "${CLAUDE_PLUGIN_ROOT}/"
# A wrapper's own variables, sh's `name="value"` and cmd's `set "name=value"`.
ASSIGNED = re.compile(r'^\s*(?:set ")?(\w+)="?([^"\n]*?)"?\s*$', re.M)
VARIABLE = re.compile(r"\$(\w+)|%(\w+)%")
# A file named by itself, beside the module that names it.
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
    one it imports that sits beside it, where its `sys.path[0]` is, or in
    `lib/`, which a script that imports from it inserts before it; a bare
    `<name>.py` beside it; and the path an
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
        found |= {posixpath.join(d, f"{n}.py") for n in names for d in (here, "lib")}
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


def hooked(root=ROOT):
    """The repository paths `hooks/hooks.json` under ROOT hands an
    interpreter: the first argument after `python3`, or after `py -3`, in
    each half of each command, with `${CLAUDE_PLUGIN_ROOT}/` read as the
    root. A root with no registration hands none."""
    try:
        with open(os.path.join(root, *HOOKS), encoding="utf-8") as f:
            registered = json.load(f)["hooks"]
    except OSError:
        return set()
    found = set()
    for entries in registered.values():
        for entry in entries:
            for hook in entry["hooks"]:
                for half in hook["command"].split(" || "):
                    words = shlex.split(half)
                    if words[:2] == ["py", "-3"]:
                        words = [words[0], *words[2:]]
                    if len(words) > 1 and words[0] in INTERPRETERS:
                        path = words[1]
                        if path.startswith(PLUGIN_ROOT):
                            found.add(path[len(PLUGIN_ROOT) :])
    return found


def before_any_floor(root=ROOT):
    """`(paths, missing)`: every tracked `.py` an interpreter may run before
    any floor is checked, and the tracked paths the working tree deleted.

    It starts from what is handed an interpreter with nothing in front of it:
    the script each command of `hooks/hooks.json` hands its interpreter
    (`hooked`), and the file each `bin/` wrapper hands its interpreter
    first. Then it follows `loaded_by` until nothing new is found. It errs
    over, since a string can name a file nothing loads, and under, for a
    module reached by a path built any other way. No git hook of this plugin
    runs a script since #1027."""
    listed, missing = on_disk(root, git_listing(root, "ls-files", "*.py"))
    tracked = set(listed)
    start = hooked(root)
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
