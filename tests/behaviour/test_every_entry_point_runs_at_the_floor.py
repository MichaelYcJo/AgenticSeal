"""The plugin's Python floor has one source, and every way into the plugin
either checks it or is linted at it.

`lib/launch.py` holds the floor once, and the runner and `ruff.toml` agree
with it. Every `bin/` wrapper but `bin/test` and its twin runs its script
through the launcher. What runs before any floor is checked, which this file
derives from `hooks/hooks.json` and `bin/` over the tracked files, is linted
at the version `ruff.toml`'s `per-file-target-version` names. Each case
lists the tracked files or `bin/`, so it stands in a file that declares no
`TARGET`. They came, unchanged, from `tests/lib/test_launch.py`, which keeps
the launcher's own cases.
"""

import ast
import json
import os
import posixpath
import re
import shlex

from censuses import matches, ruff_targets
from conftest import ROOT, decline_if_shrunken, git_listing, on_disk, read
from test_launch import LAUNCH, load

BIN = os.path.join(ROOT, "bin")
RUNNER = os.path.join(ROOT, ".github", "scripts", "run_tests.py")
RUFF = os.path.join(ROOT, "ruff.toml")


def test_the_floor_has_one_source():
    """`lib/launch.py` is the one file that spells the floor, the runner
    builds its virtualenv against the launcher's number, and `ruff.toml`,
    which cannot import, lints at that number."""
    floor = tuple(load(LAUNCH, "agentic_launch_floor").FLOOR)
    assert floor_carriers() == {"lib/launch.py": floor}, floor_carriers()
    assert tuple(load(RUNNER, "agentic_runner_floor").FLOOR) == floor
    m = re.search(r'target-version = "py(\d)(\d+)"', read(RUFF))
    assert m, "ruff.toml lost its target-version"
    assert (int(m.group(1)), int(m.group(2))) == floor, (
        f"lib/launch.py holds {floor} and ruff.toml lints at {m.group(1)}.{m.group(2)}"
    )


def test_every_wrapper_runs_its_script_through_the_launcher():
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


def test_what_runs_before_any_floor_is_linted_at_the_floor():
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
    unlinted = sorted(r for r in unfloored if not any(matches(p, r) for p in targets))
    assert not unlinted, (
        f"{unlinted} run before any floor is checked and ruff lints them at the "
        "floor; add them to ruff.toml's per-file-target-version"
    )
    stale = sorted(p for p in targets if not any(matches(p, r) for r in unfloored))
    if stale:
        decline_if_shrunken(missing, "the liveness half of per-file-target-version")
    assert not stale, f"ruff.toml lints {stale} as if a floor-less run reached them"


def test_a_script_reaches_the_modules_under_lib():
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


def test_a_script_reaches_what_it_hands_the_loader():
    """S9 of #1482. A script loads every module but `lib/sibling.py`
    through `sibling.load("<rel>")`, the path under the plugin root, so
    `loaded_by` reads a string that is a tracked path in full. A walk that
    read only the import of `sibling` would stop at the loader, and the set
    above would shrink without failing."""
    tracked = {"skills/x/g.py", "skills/y/d.py", "lib/sibling.py"}
    text = 'import sibling\nD = sibling.load("skills/y/d.py")\n'
    assert loaded_by("skills/x/g.py", text, tracked) == {
        "lib/sibling.py",
        "skills/y/d.py",
    }


def test_a_script_reaches_no_module_under_tests():
    """S9 of #1482. A path under `tests/` is no load: `tests/` holds no
    module of the plugin, and pytest imports a test module in the
    virtualenv's process, at the floor. The runner names its pins' test
    modules by tracked path, so a walk that read them would lint test
    helpers at a floor nothing runs them under."""
    tracked = {".github/scripts/r.py", "tests/t.py", "lib/a.py"}
    text = 'import a\nPINS = (("x", "tests/t.py"),)\n'
    assert loaded_by(".github/scripts/r.py", text, tracked) == {"lib/a.py"}
    reached, _missing = before_any_floor()
    assert not sorted(r for r in reached if r.startswith("tests/"))


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
# The suite's own files, which no process of the plugin loads.
TESTS = "tests/"


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
    `<name>.py` beside it; a string that is a tracked path in full, the
    `/`-joined path under the root `lib/sibling.py#load` is handed; and
    the path an `os.path.join` spells whose last string part ends in
    `.py`, `..` left out. A path under `tests/` is none of them: `tests/`
    holds no module of the plugin, and pytest imports a test module in the
    virtualenv's process, at the floor. A module that does not parse here
    loads nothing."""
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
            elif node.value in tracked:
                found.add(node.value)
        if isinstance(node, ast.Call) and getattr(node.func, "attr", "") == "join":
            parts = [
                a.value
                for a in node.args
                if isinstance(a, ast.Constant) and isinstance(a.value, str)
            ]
            if parts and parts[-1].endswith(".py"):
                tail = "/".join(p for p in parts if p not in ("..", "."))
                found |= {t for t in tracked if t == tail or t.endswith("/" + tail)}
    return {t for t in found & tracked if not t.startswith(TESTS)}


def hooked(root=ROOT):
    """The repository paths `hooks/hooks.json` under ROOT hands an
    interpreter: the argument after `python3` in each command's first half,
    with `${CLAUDE_PLUGIN_ROOT}/` read as the root. That each first half
    opens with `python3` and that prefix, and that the `py -3` half names
    the same script, `tests/behaviour/test_chain_hooks_hardening.py` holds.
    A root with no registration hands none."""
    try:
        with open(os.path.join(root, *HOOKS), encoding="utf-8") as f:
            registered = json.load(f)["hooks"]
    except OSError:
        return set()
    found = set()
    for entries in registered.values():
        for entry in entries:
            for hook in entry["hooks"]:
                script = shlex.split(hook["command"].split(" || ")[0])[1]
                found.add(script[len(PLUGIN_ROOT) :])
    return found


def before_any_floor(root=ROOT):
    """`(paths, missing)`: every tracked `.py` an interpreter may run before
    any floor is checked, and the tracked paths the working tree deleted.

    It starts from what is handed an interpreter with nothing in front of it:
    the script each command of `hooks/hooks.json` hands its interpreter
    (`hooked`), and the file each `bin/` wrapper hands its interpreter
    first. Then it follows `loaded_by` until nothing new is found, so it
    reaches no file under `tests/`. It errs over, since a string can name a
    file nothing loads, and under, for a module reached by a path built any
    other way. No git hook of this plugin
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
