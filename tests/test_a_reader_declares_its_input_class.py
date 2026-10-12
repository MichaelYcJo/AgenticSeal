"""A reader declares its input class, in its own docstring (#835).

**The rule.** Every top-level `def` and `class` in every tracked `.py` file
outside `tests/test_*.py` carries one docstring line in the grammar
`tests/reader_registry.py#GRAMMAR` states: the class of input it reads and
what it does with an input it does not understand, or `nothing` and the
reason it reads nothing. `docs/the-reader-registry.md` is the rule's home.

**The population is a rule a walk applies whole.** It is every unit, found
by `ast` over what `git ls-files` names, and no list of calls selects it. A
unit is exempt from nothing; a unit that reads nothing says so. K1, the list
of calls known to take an input, decides one thing only: a unit declaring
`nothing` that makes one of those calls is refused, naming the call.

**What the walk cannot see**, so a reader of this module meets the edge here:

1. A false declaration. `nothing` on a unit reading through a call K1 does
   not list passes, and so does `owned` or `observed` on a unit that guesses.
   The warden reads the diff's `Reads:` lines; nothing else reads the prose.
2. A unit inside `tests/test_*.py`. One rule on the file name excludes them.
3. A reader outside Python: `bin/`, a workflow's shell steps, a `sh -c`
   string inside a Python call. The walk is `ast`.
4. A module-level read through a call K1 does not list. Module bodies are the
   one place K1 selects who declares, and only for a call it knows.
5. A stale line: a reader redesigned from `guess` to `owned` keeps its old
   line until somebody moves it.
6. A census line added by hand. The census only shrinks by convention: its
   writer refuses to run where the file exists, and a line put back passes,
   so its diff is the warden's.
"""

import os

import pytest
import reader_registry as rr
from conftest import build_tracked_tree

ROOT = rr.ROOT


# --- the census's grammar ------------------------------------------------------


def malformed_census_line(n, line):
    """The finding for a census line outside the grammar."""
    return (
        f"{rr.CENSUS}:{n} `{line}` is not `path#unit@hash` — a tracked `.py` "
        "path, a top-level unit's name, and the eight-hex hash `content_hash` "
        "gives its span. Correct it or remove it."
    )


def repeated_census_line(n, line):
    """The finding for a census line naming a unit an earlier line names."""
    return (
        f"{rr.CENSUS}:{n} `{line}` repeats a unit the census already lists. "
        "Remove the line."
    )


def empty_census():
    """The finding for a census file that lists nothing."""
    return f"{rr.CENSUS} lists no unit: every unit it held declares. Delete the file."


def census_entries(census):
    """`({path#unit: (line number, line, hash)}, findings)` for the census
    `rr.read_census` returned, None reading as no census at all."""
    entries, found = {}, []
    if census is None:
        return entries, found
    if not census:
        found.append(empty_census())
    for n, line in census:
        m = rr.CENSUS_LINE.fullmatch(line)
        if not m:
            found.append(malformed_census_line(n, line))
            continue
        key = f"{m.group('path')}#{m.group('unit')}"
        if key in entries:
            found.append(repeated_census_line(n, line))
            continue
        entries[key] = (n, line, m.group("hash"))
    return entries, found


# --- the contradiction -----------------------------------------------------------


def contradiction(site, line, call):
    """The finding for a `nothing` declaration beside a K1 primitive."""
    return (
        f"{site} declares `Reads: nothing` and calls `{call}` at line {line}, "
        "which takes an input. Declare the class of what that call reads."
    )


def contradictions(unit):
    """The contradiction findings for one unit: one per K1 primitive in a
    unit whose declaration is a well-formed `nothing`."""
    found = rr.declarations(unit.doc)
    if len(found) != 1 or found[0].problem or found[0].kind != rr.NOTHING:
        return []
    return [contradiction(unit.key, line, call) for line, call in rr.k1_calls(unit)]


# --- helpers ---------------------------------------------------------------------


def planted(tmp_path, files):
    """`(units, modules, missing)` over a repository holding FILES."""
    return rr.population(build_tracked_tree(tmp_path / "r", files))


def keys(units):
    return sorted(u.key for u in units)


NOTHING_DOC = '    """Reads: nothing — a planted unit."""\n'


# --- R5: the population is the file set ------------------------------------------


def test_the_population_is_every_top_level_unit_git_lists(tmp_path):
    """R5. A directory nobody names is in on arrival; a `tests/test_*.py`
    unit is out by its file name; a helper module under `tests/` is in."""
    units, modules, missing = planted(
        tmp_path,
        {
            "evals/new.py": "def fresh():\n    return 1\n\nclass Kept:\n    pass\n",
            "tests/test_x.py": "def helper():\n    return open('p')\n",
            "tests/helpers.py": "def helper():\n    return 2\n",
            "notes.txt": "def not_python():\n",
        },
    )
    assert keys(units) == [
        "evals/new.py#Kept",
        "evals/new.py#fresh",
        "tests/helpers.py#helper",
    ]
    assert sorted(m.path for m in modules) == ["evals/new.py", "tests/helpers.py"]
    assert missing == []


def test_a_test_module_is_excluded_only_by_its_name(tmp_path):
    """R5. The exclusion is the path `tests/test_*.py`, not the word: a
    `test_` file elsewhere, or deeper under `tests/`, is in the population."""
    units, _, _ = planted(
        tmp_path,
        {
            "hooks/test_like.py": "def a():\n    pass\n",
            "tests/sub/test_deep.py": "def b():\n    pass\n",
            "tests/test_top.py": "def c():\n    pass\n",
        },
    )
    assert keys(units) == ["hooks/test_like.py#a", "tests/sub/test_deep.py#b"]


def test_methods_and_nested_functions_fold_into_their_unit(tmp_path):
    """R5. The unit is the top-level one, and a `def` a module-level `if`
    or `try` holds is one too: it is inside no other `def` or `class`."""
    units, _, _ = planted(
        tmp_path,
        {
            "hooks/a.py": (
                "class C:\n    def m(self):\n        def inner():\n            pass\n"
                "\ndef outer():\n    def nested():\n        pass\n"
                "\nif True:\n    def guarded():\n        pass\n"
                "\ntry:\n    import x\nexcept ImportError:\n    def fallback():\n        pass\n"
            )
        },
    )
    assert keys(units) == [
        "hooks/a.py#C",
        "hooks/a.py#fallback",
        "hooks/a.py#guarded",
        "hooks/a.py#outer",
    ]


def test_a_path_with_a_space_is_one_path(tmp_path):
    """R5. The listing is NUL-separated, so a space splits nothing."""
    units, _, _ = planted(tmp_path, {"hooks/two words.py": "def a():\n    pass\n"})
    assert keys(units) == ["hooks/two words.py#a"]


def test_a_tracked_file_off_disk_is_returned_as_missing(tmp_path):
    """R5. A path git lists and the tree deleted is handed back, so the
    real-tree case can decline rather than read a census line as stale."""
    root = build_tracked_tree(
        tmp_path / "r",
        {"hooks/a.py": "def a():\n    pass\n", "hooks/b.py": "def b():\n    pass\n"},
        deleted=["hooks/b.py"],
    )
    units, _, missing = rr.population(root)
    assert keys(units) == ["hooks/a.py#a"] and missing == ["hooks/b.py"]


def test_the_census_hash_is_the_ledgers_hash_of_the_unit(tmp_path):
    """R5. A census line is the ledger's own spelling: `resolve_unit` finds
    `path#unit`, and `content_hash` over that span is the line's hash."""
    text = "import os\n\n@deco\ndef f(x):\n    return x\n"
    units, _, _ = planted(tmp_path, {"hooks/a.py": text})
    ec = rr.evidence_check()
    places = ec.resolve_unit("hooks/a.py", "f", text).places
    assert places == [(3, 5)]
    want = ec.content_hash(ec.gfm_lines(text)[2:5])
    assert [u.hash for u in units] == [want]
    assert rr.census_lines(units) == [f"hooks/a.py#f@{want}"]


def test_the_census_lists_undeclared_units_only_sorted(tmp_path):
    """R5. The writer's lines: every undeclared unit, sorted by path then
    unit, and none for a unit that declares."""
    units, _, _ = planted(
        tmp_path,
        {
            "hooks/b.py": "def z():\n    pass\n\ndef a():\n    pass\n",
            "hooks/a.py": "def y():\n" + NOTHING_DOC,
        },
    )
    assert [line.split("@")[0] for line in rr.census_lines(units)] == [
        "hooks/b.py#a",
        "hooks/b.py#z",
    ]


def test_the_writer_refuses_where_a_census_exists(tmp_path):
    """R5. The census only shrinks, so its writer cuts it once."""
    root = build_tracked_tree(
        tmp_path / "r",
        {"hooks/a.py": "def a():\n    pass\n", rr.CENSUS: "hooks/a.py#a@00000000\n"},
    )
    with pytest.raises(SystemExit) as refused:
        rr.write_census(root)
    assert str(refused.value) == (
        "tests/undeclared_readers.txt exists, and the census only shrinks: "
        "remove a line by hand when its unit declares, and never write it again"
    )


def test_the_writer_writes_the_census_where_none_exists(tmp_path):
    root = build_tracked_tree(tmp_path / "r", {"hooks/a.py": "def a():\n    pass\n"})
    assert rr.write_census(root) == 1
    with open(os.path.join(root, rr.CENSUS), encoding="utf-8", newline="") as f:
        text = f.read()
    assert text.startswith("hooks/a.py#a@") and text.endswith("\n")
    assert text.count("\n") == 1


# --- R6: the census grammar ------------------------------------------------------


@pytest.mark.parametrize(
    "line",
    [
        "hooks/a.py#a",
        "hooks/a.py@0123abcd",
        "hooks/a.py#a@0123ABCD",
        "hooks/a.py#a@0123abc",
        "hooks/a.md#a@0123abcd",
        "hooks/a.py#C.m@0123abcd",
        "hooks/a.py#a@0123abcd trailing",
    ],
)
def test_a_census_line_outside_the_grammar_is_refused_naming_it(line):
    """R6."""
    entries, found = census_entries([(3, line)])
    assert entries == {}
    assert found == [malformed_census_line(3, line)]


def test_a_census_line_is_read_into_its_unit_and_hash():
    entries, found = census_entries([(1, "hooks/a.py#a@0123abcd")])
    assert found == []
    assert entries == {"hooks/a.py#a": (1, "hooks/a.py#a@0123abcd", "0123abcd")}


def test_a_repeated_census_line_is_refused():
    entries, found = census_entries(
        [(1, "hooks/a.py#a@0123abcd"), (2, "hooks/a.py#a@99999999")]
    )
    assert list(entries) == ["hooks/a.py#a"]
    assert found == [repeated_census_line(2, "hooks/a.py#a@99999999")]


def test_an_empty_census_says_to_delete_it(tmp_path):
    """R6. A file with no line is a census of nothing."""
    root = build_tracked_tree(tmp_path / "r", {rr.CENSUS: "\n"})
    assert census_entries(rr.read_census(root)) == ({}, [empty_census()])


def test_no_census_file_is_no_census(tmp_path):
    """R6."""
    root = build_tracked_tree(tmp_path / "r", {"hooks/a.py": "x = 1\n"})
    assert rr.read_census(root) is None
    assert census_entries(None) == ({}, [])


def test_the_census_grammar_texts_are_pinned():
    """R9 for R6's findings (§14)."""
    assert malformed_census_line(4, "x") == (
        "tests/undeclared_readers.txt:4 `x` is not `path#unit@hash` — a tracked "
        "`.py` path, a top-level unit's name, and the eight-hex hash "
        "`content_hash` gives its span. Correct it or remove it."
    )
    assert repeated_census_line(5, "y") == (
        "tests/undeclared_readers.txt:5 `y` repeats a unit the census already "
        "lists. Remove the line."
    )
    assert empty_census() == (
        "tests/undeclared_readers.txt lists no unit: every unit it held "
        "declares. Delete the file."
    )


# --- R7: the contradiction -------------------------------------------------------


def nothing_unit(tmp_path, head, body):
    """The one unit of a planted module: HEAD at module level, then a `def`
    declaring `nothing` whose body is BODY."""
    source = f"{head}\ndef f(s, p):\n{NOTHING_DOC}    {body}\n"
    units, _, _ = planted(tmp_path, {"hooks/a.py": source})
    assert len(units) == 1
    return units[0], source.split("\n").index(f"    {body}") + 1


@pytest.mark.parametrize(
    ("head", "body", "call"),
    [
        ("", "return open(p)", "open"),
        ("", "return p.read_text(encoding='utf-8')", ".read_text"),
        ("import subprocess", "return subprocess.run(['git'])", "subprocess.run"),
        ("import os", "return os.environ.get('X')", "os.environ"),
        ("import sys", "return sys.stdin", "sys.stdin"),
        ("import json", "return json.loads(s)", "json.loads"),
        ("from json import loads as parse", "return parse(s)", "json.loads"),
        ("import shlex", "return shlex.split(s)", "shlex.split"),
        ("import re", "return re.match('x', s)", "re.match"),
        ("PATTERN = None", "return PATTERN.fullmatch(s)", ".fullmatch"),
        ("import os", "return os.path.exists(p)", "os.path.exists"),
        ("import evidence_check as ec", "return ec.FENCE.sub('', s)", ".sub"),
    ],
)
def test_nothing_beside_a_k1_primitive_is_refused_naming_the_call(
    tmp_path, head, body, call
):
    """R7, one or more per family: a boundary call, `os.environ`,
    `sys.stdin`, a parser through its import, `shlex.split`."""
    unit, line = nothing_unit(tmp_path, head, body)
    assert contradictions(unit) == [contradiction("hooks/a.py#f", line, call)]


@pytest.mark.parametrize(
    ("head", "body"),
    [
        ("", "return s.split()"),
        ("def load(p):\n    return p\n", "return load(p)"),
        ("from mymodule import load", "return load(p)"),
        ("from mymodule import run", "return run(p)"),
        ("import ast", "return list(ast.walk(p))"),
        ("import os", "return os.path.join(p, s)"),
    ],
)
def test_a_call_k1_does_not_name_leaves_nothing_standing(tmp_path, head, body):
    """R7. `str.split` is no parser here, and a module function is the
    library's only where an import binds it to the library."""
    if head.startswith("def load"):
        source = f"{head}\ndef f(s, p):\n{NOTHING_DOC}    {body}\n"
        units, _, _ = planted(tmp_path, {"hooks/a.py": source})
        unit = next(u for u in units if u.name == "f")
    else:
        unit, _ = nothing_unit(tmp_path, head, body)
    assert contradictions(unit) == []


def test_the_stated_limit_a_primitive_k1_does_not_list_passes(tmp_path):
    """R7, the stated limit, not a pass anybody earned: `pickle.loads` reads
    its input, K1 does not list it, so a `nothing` beside it is not refused.
    A missing row is a row to add to K1."""
    unit, _ = nothing_unit(tmp_path, "import pickle", "return pickle.loads(s)")
    assert contradictions(unit) == []


def test_a_class_declares_for_its_methods(tmp_path):
    """R7. A method's call is the class's call."""
    source = (
        "class C:\n"
        '    """Reads: nothing — a planted class."""\n\n'
        "    def m(self, p):\n        return open(p)\n"
    )
    units, _, _ = planted(tmp_path, {"hooks/a.py": source})
    assert [contradictions(u) for u in units] == [
        [contradiction("hooks/a.py#C", 5, "open")]
    ]


def test_a_declared_class_is_not_contradicted(tmp_path):
    """R7. K1 judges `nothing` alone; a unit declaring a class may call
    whatever it reads through."""
    source = 'def f(p):\n    """Reads: observed — a file; unknown refused"""\n    return open(p)\n'
    units, _, _ = planted(tmp_path, {"hooks/a.py": source})
    assert contradictions(units[0]) == []


def test_the_contradiction_text_is_pinned():
    """R9 for R7 (§14)."""
    assert contradiction("hooks/a.py#f", 3, "open") == (
        "hooks/a.py#f declares `Reads: nothing` and calls `open` at line 3, "
        "which takes an input. Declare the class of what that call reads."
    )


def test_a_module_body_read_is_counted_outside_every_unit(tmp_path):
    """The walker's module-body half: a reference at module level is
    counted, one inside a unit is not."""
    source = "import os\nX = os.environ.get('X')\n\ndef f():\n    return os.environ\n"
    _, modules, _ = planted(tmp_path, {"hooks/a.py": source})
    assert [m.body_calls for m in modules] == [[(2, "os.environ")]]
