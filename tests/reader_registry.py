"""The reader registry's walk: every unit of shipped Python and what it declares (#835).

The registry is the code. Every top-level `def` and `class` in every tracked
`.py` file outside `tests/test_*.py` carries one line in its own docstring
that says what class of input it reads, and
`tests/test_a_reader_declares_its_input_class.py` refuses a unit without one.
This module is the walk that test reads, and the census writer the
transition was cut with. `docs/the-reader-registry.md` is the rule's home.

**The population is a rule, not a list of calls.** It is every unit not
inside another `def` or `class`, in every file `git ls-files -z -- '*.py'`
names, less the files whose path is `tests/test_*.py`. A unit reads nothing
by being exempt from nothing: it says so, `nothing` and a reason, and the
check reads the two words. A tracked `.py` in a directory nobody listed is in
the population on arrival, because git listed it.

**K1 is a contradiction list, and it selects nobody.** `k1_calls` finds the
calls a unit makes that are known to take an input: the process boundary and
a standard-library parser handed text. The one thing the answer decides is
that a unit declaring `nothing` while making one of those calls is refused.
A call the list does not know leaves the unit's duty to declare exactly where
it was, so a missing row costs one contradiction the check cannot see and
never a unit it does not ask. A missing row is a row to add to K1.

What a static walk cannot follow is stated rather than left to be found: a
call through a name the file binds at run time (`f = open; f(p)`), a method
reached on a receiver the file's imports bind to a module K1 does not list,
and the body of a `sh -c` string. The test's docstring lists the rest.
"""

import ast
import functools
import importlib.util
import os
import re
import subprocess
import sys

from conftest import on_disk

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
COORDINATES = os.path.join(ROOT, "skills", "verify", "scripts", "coordinates.py")
CENSUS = "tests/undeclared_readers.txt"
TEST_MODULE = re.compile(r"tests/test_[^/]*\.py")

CLASSES = ("owned", "observed", "guess")
NOTHING = "nothing"
DIRECTIONS = ("refused", "passed", "mixed")
GRAMMAR = (
    "`Reads: <owned|observed|guess> — <what it reads>; unknown "
    "<refused|passed|mixed>`, or `Reads: nothing — <why it reads nothing>`"
)

# --- K1, the contradiction list ---------------------------------------------
#
# Two families, each a list to extend. A method is matched by its attribute
# name on any receiver, because a compiled pattern or a path is called on a
# name, and a module's own reading function is matched the same way. A module
# function is matched by its dotted name only where the file's imports bind
# the name to that module, so a repository's own `load` or `run` never reads
# as the library's. Nothing here says a call does NOT read: `ast.walk` matches
# `walk`, and a `nothing` beside it is refused, which costs a truthful class
# word, where a table read as complete for a module let `os.open` pass: that
# was the build's `K1_MODULES` receiver rule, which round 1 of #835 removed.

K1_METHODS = frozenset(
    {
        # the process boundary
        "open",
        "read_text",
        "read_bytes",
        "read",
        "readline",
        "readlines",
        "listdir",
        "scandir",
        "walk",
        "glob",
        "iglob",
        "rglob",
        "iterdir",
        "exists",
        "isfile",
        "isdir",
        "lexists",
        "stat",
        "lstat",
        "readlink",
        # a standard-library parser handed text
        "match",
        "search",
        "fullmatch",
        "findall",
        "finditer",
        "sub",
        "subn",
        "splitlines",
    }
)
K1_FUNCTIONS = frozenset(
    {
        "builtins.open",
        "builtins.input",
        "io.open",
        "subprocess.run",
        "subprocess.check_output",
        "subprocess.check_call",
        "subprocess.call",
        "subprocess.Popen",
        "subprocess.getoutput",
        "subprocess.getstatusoutput",
        "os.popen",
        "os.getenv",
        "os.open",
        "os.read",
        "os.fdopen",
        "os.readlink",
        "os.listdir",
        "os.scandir",
        "os.walk",
        "os.stat",
        "os.lstat",
        "os.access",
        "os.path.exists",
        "os.path.isfile",
        "os.path.isdir",
        "os.path.lexists",
        "os.path.islink",
        "os.path.getsize",
        "os.path.getmtime",
        "glob.glob",
        "glob.iglob",
        "re.match",
        "re.search",
        "re.fullmatch",
        "re.findall",
        "re.finditer",
        "re.sub",
        "re.subn",
        "re.split",
        "shlex.split",
        "shlex.shlex",
        "json.load",
        "json.loads",
        "ast.parse",
        "tomllib.load",
        "tomllib.loads",
        "xml.etree.ElementTree.parse",
        "xml.etree.ElementTree.fromstring",
        "csv.reader",
        "csv.DictReader",
    }
)
K1_REFERENCES = frozenset({"os.environ", "sys.stdin", "sys.argv"})


def bindings(tree):
    """`{local name: dotted target}` for every import in the module.

    Reads: observed — the import statements of an AST its caller parsed; unknown passed

    `import subprocess as sp` binds `sp` to `subprocess`; `from subprocess
    import run` binds `run` to `subprocess.run`. Collected over the whole
    module, so an import inside a function is seen too. The encoding test's
    `bindings`, copied rather than imported, because a helper importing a
    test module would collect that module's cases a second time.
    """
    bound = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.asname:
                    bound[alias.asname] = alias.name
                else:
                    top = alias.name.split(".")[0]
                    bound[top] = top
        elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
            for alias in node.names:
                bound[alias.asname or alias.name] = f"{node.module}.{alias.name}"
    return bound


def dotted(node, bound):
    """`a.b.c` with its head resolved through the module's imports, or None.

    Reads: nothing — resolves a name chain against the bindings it is handed
    """
    if isinstance(node, ast.Name):
        return bound.get(node.id)
    if isinstance(node, ast.Attribute):
        head = dotted(node.value, bound)
        return f"{head}.{node.attr}" if head else None
    return None


def k1_call(node, bound):
    """The K1 primitive one AST node is, spelled for a person, or None.

    Reads: observed — one node of an AST `ast` built; unknown passed

    A call K1 does not list is no primitive here, which is the list's stated
    limit and the reason the direction is `passed`.

    A call to a bare name is the builtin `open` or `input` where no import
    binds the name, and otherwise the dotted name its import binds. A method
    is K1 by its full dotted name where the table lists it, and by its
    attribute name on any receiver otherwise, a module's included: the table
    adds calls, and never vouches that a module's other calls read nothing.
    A reference to `os.environ`, `sys.stdin` or `sys.argv` counts without a
    call.
    """
    if isinstance(node, ast.Call):
        func = node.func
        if isinstance(func, ast.Name):
            if func.id not in bound:
                return func.id if func.id in ("open", "input") else None
            target = bound[func.id]
            return target if target in K1_FUNCTIONS else None
        if isinstance(func, ast.Attribute):
            target = dotted(func, bound)
            if target in K1_FUNCTIONS:
                return target
            return f".{func.attr}" if func.attr in K1_METHODS else None
        return None
    if isinstance(node, (ast.Attribute, ast.Name)):
        target = dotted(node, bound)
        return target if target in K1_REFERENCES else None
    return None


def k1_calls(unit):
    """`[(line, primitive)]` for every K1 primitive in a unit's body, in line
    order: its methods, nested functions and decorators fold into it.

    Reads: observed — the unit's AST, which `population` parsed; unknown passed
    """
    found = []
    for node in ast.walk(unit.node):
        hit = k1_call(node, unit.bound)
        if hit:
            found.append((node.lineno, hit))
    return sorted(found)


def module_body_calls(tree):
    """`[(line, primitive)]` for every K1 primitive in a module's statements
    outside every `def` and `class`, in line order.

    Reads: observed — a module's AST; unknown passed

    A module-level read through a call K1 does not list is unseen, and that
    is the whole of what stays quiet in rule 1.
    """
    bound = bindings(tree)
    found = []
    stack = list(ast.iter_child_nodes(tree))
    while stack:
        node = stack.pop()
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        hit = k1_call(node, bound)
        if hit:
            found.append((node.lineno, hit))
        stack.extend(ast.iter_child_nodes(node))
    return sorted(found)


# --- the declaration ----------------------------------------------------------

DECLARATION = re.compile(r"Reads:(?P<rest>.*)")
REASON = re.compile(r"\s+(?:—|--)\s+\S")
DIRECTION = re.compile(r";\s*unknown\s+(?P<word>\S+)\s*$")


class Declaration:
    """One unit's `Reads:` line as the check reads it: the class word, the
    direction word, and what is wrong with them, or None.

    Reads: owned — a docstring line in the grammar this module defines; unknown refused
    """

    __slots__ = ("direction", "kind", "line", "problem")

    def __init__(self, line, kind, direction, problem):
        self.line = line
        self.kind = kind
        self.direction = direction
        self.problem = problem


def declarations(doc):
    """Every `Reads:` line of a docstring, each read into a `Declaration`.

    Reads: owned — a docstring's lines, in the grammar this module defines; unknown refused

    A declaration is a line that begins `Reads:` once its indentation is
    gone. The class word is the first word after it and the direction word
    the last after `; unknown`, and nothing between them is read.
    """
    found = []
    for raw in (doc or "").split("\n"):
        line = raw.strip()
        m = DECLARATION.match(line)
        if not m:
            continue
        rest = m.group("rest")
        words = rest.split()
        kind = words[0] if words else ""
        after = rest[rest.find(kind) + len(kind) :] if kind else ""
        direction = DIRECTION.search(rest)
        word = direction.group("word") if direction else ""
        problem = None
        if kind == NOTHING:
            word = ""
            if not REASON.match(after):
                problem = "a `nothing` line names its reason after ` — `"
        elif kind not in CLASSES:
            problem = (
                f"`{kind or '(none)'}` is not a class; the class word is one of "
                "`owned`, `observed`, `guess` or `nothing`"
            )
        elif not direction:
            problem = "a class line ends `; unknown <refused|passed|mixed>`"
        elif word not in DIRECTIONS:
            problem = (
                f"`{word}` is not a direction; it is one of `refused`, `passed` "
                "or `mixed`"
            )
        found.append(Declaration(line, kind, word, problem))
    return found


# --- the population -----------------------------------------------------------


class Unit:
    """One unit of the population: a `def` or `class` inside no other.

    Reads: nothing — holds what `population` read and computed, and decides nothing
    """

    __slots__ = ("bound", "doc", "hash", "line", "name", "node", "path")

    def __init__(self, path, name, node, bound, digest):
        self.path = path
        self.name = name
        self.node = node
        self.bound = bound
        self.doc = ast.get_docstring(node)
        self.line = node.lineno
        self.hash = digest

    @property
    def key(self):
        return f"{self.path}#{self.name}"


class Module:
    """One file of the population, with its module docstring and the K1
    primitives its body makes outside every unit.

    Reads: nothing — holds what `population` read, and decides nothing.
    """

    __slots__ = ("body_calls", "doc", "path")

    def __init__(self, path, doc, body_calls):
        self.path = path
        self.doc = doc
        self.body_calls = body_calls


@functools.cache
def coordinates():
    """`skills/verify/scripts/coordinates.py`, loaded by path.

    Reads: observed — the coordinate kernel's own module, executed by the interpreter; unknown refused

    The census hashes a unit with the kernel's `py_spans` and `content_hash`,
    imported and never copied, so a census line is the kernel's spelling and
    `resolve_unit` finds it.
    """
    spec = importlib.util.spec_from_file_location(
        "specseal_coordinates_for_the_registry", COORDINATES
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def tracked_python(root=ROOT):
    """`(every population file on disk, the tracked paths that are not)`.

    Reads: observed — `git ls-files -z` over the root; unknown refused

    NUL-separated, so a path with a space in it is one path. A tracked path
    the working tree deleted is returned rather than dropped: the check
    declines on it, because a census line for a unit in a file that is not
    there is not evidence the unit went.
    """
    out = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z", "--", "*.py"],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        check=True,
    ).stdout
    listed = sorted(
        rel for rel in out.split("\0") if rel and not TEST_MODULE.fullmatch(rel)
    )
    return on_disk(root, listed)


def top_units(tree):
    """Every `def` and `class` inside no other, in line order, those a
    module-level `if`, `try`, `except` or `with` holds included.

    Reads: nothing — walks an AST its caller parsed.
    """
    found = []
    stack = [tree]
    while stack:
        node = stack.pop()
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                found.append(child)
            else:
                stack.append(child)
    return sorted(found, key=lambda n: n.lineno)


def unit_hash(ec, text, name):
    """The census hash of the unit NAME in TEXT: `content_hash` over every
    span `py_spans` gives the name, in order.

    Reads: nothing — hashes the text it is handed, through the kernel's two functions

    One span for every name in this tree. Several, where a module defines a
    name twice, are hashed together so that an edit to either moves it.
    """
    lines = ec.gfm_lines(text)
    spans = ec.py_spans(text).get(name, [])
    region = [line for a, b in spans for line in lines[a - 1 : b]]
    return ec.content_hash(region)


def population(root=ROOT):
    """`(units, modules, missing)` over every population file on disk.

    Reads: observed — each tracked file's AST, parsed by the running interpreter; unknown refused
    """
    ec = coordinates()
    files, missing = tracked_python(root)
    units, modules = [], []
    for rel in files:
        with open(os.path.join(root, rel), encoding="utf-8") as f:
            text = f.read()
        tree = ast.parse(text, filename=rel)
        bound = bindings(tree)
        hashes = {}
        for node in top_units(tree):
            if node.name not in hashes:
                hashes[node.name] = unit_hash(ec, text, node.name)
            units.append(Unit(rel, node.name, node, bound, hashes[node.name]))
        modules.append(Module(rel, ast.get_docstring(tree), module_body_calls(tree)))
    return units, modules, missing


# --- the census ---------------------------------------------------------------

CENSUS_LINE = re.compile(
    r"(?P<path>[^\s#@]+\.py)#(?P<unit>[A-Za-z_][A-Za-z0-9_]*)@(?P<hash>[0-9a-f]{8})"
)


def census_lines(units):
    """The census for a population: one `path#unit@hash` per undeclared
    unit, sorted by path then unit, each name once.

    Reads: owned — each unit's `Reads:` lines, through `declarations`; unknown refused

    A line outside the grammar still keeps its unit off the census, and the
    test refuses the line.

    A name a module defines twice is one unit here, and it is declared when
    any of its definitions declares; the test asks the same of every one.
    """
    declared = {u.key for u in units if declarations(u.doc)}
    lines = {(u.path, u.name, f"{u.key}@{u.hash}") for u in units}
    return [
        line for path, name, line in sorted(lines) if f"{path}#{name}" not in declared
    ]


def read_census(root=ROOT):
    """`[(line number, text)]` for the census file under ROOT, or None where
    there is no file.

    Reads: owned — `tests/undeclared_readers.txt`, which `census_lines` wrote; unknown refused
    """
    path = os.path.join(root, CENSUS)
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return [(n, line) for n, line in enumerate(text.split("\n"), 1) if line]


def write_census(root=ROOT):
    """Write the census for ROOT's population, refusing where one exists.

    Reads: observed — the population, through `population`; unknown refused

    The census only shrinks: the writer cuts it once, and every later change
    to it is a line removed by hand. Overwriting a file that exists would add
    every unit undeclared since, which is the one edit the census exists to
    refuse.
    """
    path = os.path.join(root, CENSUS)
    if os.path.exists(path):
        raise SystemExit(
            f"{CENSUS} exists, and the census only shrinks: remove a line by "
            "hand when its unit declares, and never write it again"
        )
    units, _modules, missing = population(root)
    if missing:
        raise SystemExit(f"tracked and not on disk: {', '.join(missing)}")
    lines = census_lines(units)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("".join(line + "\n" for line in lines))
    return len(lines)


if __name__ == "__main__":
    print(f"{write_census()} undeclared unit(s) written to {CENSUS}", file=sys.stderr)
