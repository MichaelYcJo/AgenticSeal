"""A reader declares its input class, in its own docstring (#835).

**The rule.** Every top-level `def` and `class` in every tracked `.py` file
outside `tests/test_*.py` carries one docstring line in the grammar
`tests/reader_registry.py#GRAMMAR` states: the class of input it reads and
where an input it does not understand ends, read through to the decision it
feeds, or `nothing` and the
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
   line until somebody moves it. A helper's line goes stale the same way when
   only a caller changes: its direction, and its class where it parses text
   a caller handed it, are read at its callers, so its hash does not move
   and the diff the warden reads does not show its line.
6. A census line added by hand. The census only shrinks by convention: its
   writer refuses to run where the file exists, and a line put back passes,
   so its diff is the warden's.
"""

import os

import pytest
import reader_registry as rr
from conftest import build_tracked_tree, decline_if_shrunken

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


# --- the declaration and the census, judged --------------------------------------


def undeclared(unit):
    """The finding for a unit with no `Reads:` line and no census line."""
    return (
        f"{unit.key} (line {unit.line}) declares no input class. Add one line "
        f"to its docstring: {rr.GRAMMAR}. A unit that stood undeclared when the "
        "census was cut, and has not changed since, keeps its census line "
        f"`{unit.key}@{unit.hash}` in {rr.CENSUS}; every other unit declares."
    )


def malformed_declaration(site, decl):
    """The finding for a `Reads:` line outside the grammar."""
    return (
        f"{site} declares `{decl.line}`, read as class `{decl.kind or '(none)'}` "
        f"and direction `{decl.direction or '(none)'}`: {decl.problem}. The "
        f"grammar is {rr.GRAMMAR}."
    )


def declared_twice(site, count):
    """The finding for a docstring carrying more than one `Reads:` line."""
    return (
        f"{site} carries {count} `Reads:` lines. A unit declares once, the "
        "weakest class it reads, `guess` being the weakest."
    )


def census_unit_changed(unit, n, line):
    """The finding for an undeclared unit whose census hash moved."""
    return (
        f"{unit.key} (line {unit.line}) changed since {rr.CENSUS}:{n} listed it "
        f"as `{line}`, and its hash is now {unit.hash}. Declare it and remove "
        "its census line."
    )


GONE = "no top-level unit of that name is in the file: it went, or was renamed"
DECLARED_SINCE = "the unit declares now"
OUTSIDE = "the file is not in the population: it is untracked, or a test module"


def census_line_names_nothing(n, line, cause):
    """The finding for a census line naming no undeclared population unit."""
    return (
        f"{rr.CENSUS}:{n} `{line}` names no undeclared unit: {cause}. Remove the line."
    )


def module_undeclared(module, line, call):
    """The finding for a module body that reads with no module declaration."""
    return (
        f"{module.path} reads at module level — `{call}` at line {line} — and "
        "its module docstring carries no `Reads:` line. Declare for the module "
        f"body in the module docstring: {rr.GRAMMAR}."
    )


def judge_declaration(site, doc):
    """`(declarations, findings)` for one docstring: a second line and a line
    outside the grammar are findings."""
    found = rr.declarations(doc)
    out = []
    if len(found) > 1:
        out.append(declared_twice(site, len(found)))
    out += [malformed_declaration(site, d) for d in found if d.problem]
    return found, out


def findings(units, modules, missing, census):
    """Every finding over a population and its census, in a stable order.

    A census line naming a file the working tree deleted is the one finding
    that could be the tree rather than the registry, so it declines instead
    (`conftest.decline_if_shrunken`), and only after every positive finding
    was collected and found empty.
    """
    entries, out = census_entries(census)
    by_key = {}
    for u in units:
        by_key.setdefault(u.key, []).append(u)
    for u in units:
        found, problems = judge_declaration(f"{u.key} (line {u.line})", u.doc)
        out += problems
        if found:
            out += contradictions(u)
            continue
        entry = entries.get(u.key)
        if entry is None:
            out.append(undeclared(u))
        elif entry[2] != u.hash:
            out.append(census_unit_changed(u, entry[0], entry[1]))
    for m in modules:
        found, problems = judge_declaration(f"{m.path} (module docstring)", m.doc)
        out += problems
        if not m.body_calls:
            continue
        if not found:
            out += [module_undeclared(m, line, call) for line, call in m.body_calls]
        elif len(found) == 1 and not found[0].problem and found[0].kind == rr.NOTHING:
            site = f"{m.path} (module body)"
            out += [contradiction(site, line, call) for line, call in m.body_calls]
    files = {m.path for m in modules}
    gone = []
    for key, (n, line, _hash) in sorted(entries.items(), key=lambda e: e[1][0]):
        if key in by_key:
            if any(rr.declarations(u.doc) for u in by_key[key]):
                out.append(census_line_names_nothing(n, line, DECLARED_SINCE))
            continue
        path = key.split("#", 1)[0]
        if path in missing:
            gone.append(path)
        elif path in files:
            out.append(census_line_names_nothing(n, line, GONE))
        else:
            out.append(census_line_names_nothing(n, line, OUTSIDE))
    return out, sorted(set(gone))


DECLINES = "the reader registry's census liveness half"


def registry_findings(root):
    """`findings` over the repository at ROOT, declining on a census line
    whose file the working tree deleted."""
    units, modules, missing = rr.population(root)
    out, gone = findings(units, modules, missing, rr.read_census(root))
    if not out:
        decline_if_shrunken(gone, DECLINES)
    return out


def failure(found):
    return f"{len(found)} reader-registry finding(s):\n" + "\n".join(found)


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
    """R5. A census line is the kernel's own spelling: `resolve_unit` finds
    `path#unit`, and `content_hash` over that span is the line's hash."""
    text = "import os\n\n@deco\ndef f(x):\n    return x\n"
    units, _, _ = planted(tmp_path, {"hooks/a.py": text})
    ec = rr.coordinates()
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
        ("import os", "return os.open(p, 0)", "os.open"),
        ("import re", "return re.split(',', s)", "re.split"),
        ("import ast", "return list(ast.walk(p))", ".walk"),
        ("import pathlib", "return pathlib.Path.read_text(p)", ".read_text"),
    ],
)
def test_nothing_beside_a_k1_primitive_is_refused_naming_the_call(
    tmp_path, head, body, call
):
    """R7, one or more per family: a boundary call, `os.environ`,
    `sys.stdin`, a parser through its import, `shlex.split`. The last four
    rows are round 1's 🟡 1: `os.open` and `re.split` are rows of the table,
    and `ast.walk` and `pathlib.Path.read_text` show that a module the table
    names is not vouched for by it, so a method the table lacks is judged by
    its name."""
    unit, line = nothing_unit(tmp_path, head, body)
    assert contradictions(unit) == [contradiction("hooks/a.py#f", line, call)]


@pytest.mark.parametrize(
    ("head", "body"),
    [
        ("", "return s.split()"),
        ("def load(p):\n    return p\n", "return load(p)"),
        ("from mymodule import load", "return load(p)"),
        ("from mymodule import run", "return run(p)"),
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


# --- R8: this tree passes ----------------------------------------------------------


def test_every_unit_of_shipped_python_declares_or_is_on_the_census():
    """R8. The rule, over this repository: every population unit declares
    or stands on the census unchanged, every module body that reads
    declares, and every census line names an undeclared unit."""
    found = registry_findings(ROOT)
    assert not found, failure(found)


# --- R1: an undeclared unit ----------------------------------------------------------


def judge_planted(tmp_path, files):
    root = build_tracked_tree(tmp_path / "r", files)
    units, modules, missing = rr.population(root)
    out, gone = findings(units, modules, missing, rr.read_census(root))
    return units, out, gone


@pytest.mark.parametrize(
    "body",
    ["    return 1\n", "    return pickle.loads(p)\n"],
    ids=["calls no primitive", "calls a primitive k1 does not list"],
)
def test_a_new_unit_with_no_declaration_is_refused_whatever_it_calls(tmp_path, body):
    """R1. The duty to declare is the unit's, not its calls'."""
    units, out, _ = judge_planted(
        tmp_path, {"hooks/a.py": f"import pickle\n\ndef f(p):\n{body}"}
    )
    assert out == [undeclared(units[0])]


def test_a_unit_with_no_docstring_is_undeclared(tmp_path):
    units, out, _ = judge_planted(
        tmp_path, {"skills/x/scripts/a.py": "class C:\n    x = 1\n"}
    )
    assert out == [undeclared(units[0])]


@pytest.mark.parametrize(
    "line",
    [
        "Reads: owned — the census; unknown refused",
        "Reads: observed -- git ls-files; unknown mixed",
        "Reads: guess — a person's sentence; unknown passed",
        "Reads: nothing — a formatter of its own output",
        "Reads: nothing -- a pure function",
    ],
)
def test_a_declaration_in_the_grammar_passes(tmp_path, line):
    """R1's other side: each class and both separators."""
    source = f'def f(p):\n    """Summary.\n\n    {line}\n    """\n    return p\n'
    _, out, _ = judge_planted(tmp_path, {"hooks/a.py": source})
    assert out == []


# --- R2: a declaration outside the vocabulary -----------------------------------


@pytest.mark.parametrize(
    ("line", "kind", "direction", "problem"),
    [
        (
            "Reads: maybe — something; unknown refused",
            "maybe",
            "refused",
            "`maybe` is not a class; the class word is one of `owned`, "
            "`observed`, `guess` or `nothing`",
        ),
        (
            "Reads: owned — the census",
            "owned",
            "",
            "a class line ends `; unknown <refused|passed|mixed>`",
        ),
        (
            "Reads: observed — a file; unknown sometimes",
            "observed",
            "sometimes",
            "`sometimes` is not a direction; it is one of `refused`, `passed` "
            "or `mixed`",
        ),
        (
            "Reads: nothing",
            "nothing",
            "",
            "a `nothing` line names its reason after ` — `",
        ),
        (
            "Reads: nothing —",
            "nothing",
            "",
            "a `nothing` line names its reason after ` — `",
        ),
        (
            "Reads:",
            "",
            "",
            "`(none)` is not a class; the class word is one of `owned`, "
            "`observed`, `guess` or `nothing`",
        ),
    ],
)
def test_a_declaration_outside_the_grammar_is_refused_naming_its_words(
    tmp_path, line, kind, direction, problem
):
    """R2, one per defect: the finding names the unit and the two words the
    check reads."""
    source = f'def f(p):\n    """{line}"""\n    return p\n'
    _, out, _ = judge_planted(tmp_path, {"hooks/a.py": source})
    decl = rr.Declaration(line, kind, direction, problem)
    assert out == [malformed_declaration("hooks/a.py#f (line 1)", decl)]


def test_two_declarations_in_one_unit_are_refused(tmp_path):
    """R2. One line per unit."""
    source = (
        'def f(p):\n    """Reads: owned — a; unknown refused\n'
        '    Reads: guess — b; unknown passed\n    """\n    return p\n'
    )
    _, out, _ = judge_planted(tmp_path, {"hooks/a.py": source})
    assert out == [declared_twice("hooks/a.py#f (line 1)", 2)]


def test_a_reads_word_inside_a_sentence_is_not_a_declaration(tmp_path):
    """R2's edge: a declaration is a line that begins `Reads:`, so prose
    mentioning the word, or a quoted example, declares nothing."""
    source = 'def f(p):\n    """The line `Reads: maybe` is refused.\n    """\n'
    units, out, _ = judge_planted(tmp_path, {"hooks/a.py": source})
    assert out == [undeclared(units[0])]


# --- R3, R4: the census -------------------------------------------------------------


def test_an_unchanged_unit_on_the_census_passes(tmp_path):
    """The transition: a unit undeclared at the landing, unchanged, owes
    nothing."""
    files = {"hooks/a.py": "def f(p):\n    return p\n"}
    units, _, _ = judge_planted(tmp_path / "first", files)
    census = "".join(line + "\n" for line in rr.census_lines(units))
    _, out, _ = judge_planted(tmp_path / "second", {**files, rr.CENSUS: census})
    assert out == []


def test_a_changed_census_unit_must_declare(tmp_path):
    """R3."""
    files = {"hooks/a.py": "def f(p):\n    return p\n"}
    units, _, _ = judge_planted(tmp_path / "first", files)
    line = rr.census_lines(units)[0]
    changed = {"hooks/a.py": "def f(p):\n    return p + 1\n", rr.CENSUS: line + "\n"}
    now, out, _ = judge_planted(tmp_path / "second", changed)
    assert out == [census_unit_changed(now[0], 1, line)]


@pytest.mark.parametrize(
    ("files", "line", "cause"),
    [
        (
            {"hooks/a.py": 'def g():\n    """Reads: nothing — planted."""\n'},
            "hooks/a.py#f@0123abcd",
            GONE,
        ),
        (
            {"hooks/a.py": 'def f():\n    """Reads: nothing — planted."""\n'},
            "hooks/a.py#f@0123abcd",
            DECLARED_SINCE,
        ),
        ({"hooks/a.py": "x = 1\n"}, "hooks/b.py#f@0123abcd", OUTSIDE),
        (
            {"hooks/a.py": "x = 1\n", "tests/test_x.py": "def f():\n    pass\n"},
            "tests/test_x.py#f@0123abcd",
            OUTSIDE,
        ),
    ],
    ids=["gone or renamed", "declared since", "untracked", "a test module"],
)
def test_a_census_line_naming_no_undeclared_unit_is_refused(
    tmp_path, files, line, cause
):
    """R4, one per cause."""
    _, out, _ = judge_planted(tmp_path, {**files, rr.CENSUS: line + "\n"})
    assert out == [census_line_names_nothing(1, line, cause)]


def test_a_census_line_for_a_deleted_file_declines_rather_than_refuses(tmp_path):
    """The liveness half: a file off disk could be the tree mid-edit, so the
    line is not judged stale and the real-tree case declines on it."""
    root = build_tracked_tree(
        tmp_path / "r",
        {
            "hooks/a.py": 'def a():\n    """Reads: nothing — planted."""\n',
            "hooks/b.py": "def b():\n    pass\n",
            rr.CENSUS: "hooks/b.py#b@0123abcd\n",
        },
        deleted=["hooks/b.py"],
    )
    units, modules, missing = rr.population(root)
    assert findings(units, modules, missing, rr.read_census(root)) == (
        [],
        ["hooks/b.py"],
    )
    with pytest.raises(pytest.skip.Exception) as declined:
        registry_findings(root)
    assert DECLINES in str(declined.value) and "hooks/b.py" in str(declined.value)


# --- R10: a module body ---------------------------------------------------------


READING_BODY = "import os\nX = os.environ.get('X')\n"


def test_a_module_body_that_reads_without_a_declaration_is_refused(tmp_path):
    """R10."""
    _, out, _ = judge_planted(tmp_path, {"hooks/a.py": READING_BODY})
    _, modules, _ = planted(tmp_path / "again", {"hooks/a.py": READING_BODY})
    assert out == [module_undeclared(modules[0], 2, "os.environ")]


def test_a_module_body_declared_in_its_docstring_passes(tmp_path):
    """R10."""
    doc = '"""A module.\n\nReads: observed — the environment; unknown passed\n"""\n'
    _, out, _ = judge_planted(tmp_path, {"hooks/a.py": doc + READING_BODY})
    assert out == []


def test_a_module_body_with_no_k1_call_owes_no_line(tmp_path):
    """R10."""
    _, out, _ = judge_planted(tmp_path, {"hooks/a.py": "X = 1\n"})
    assert out == []


def test_a_module_body_declaring_nothing_beside_a_read_is_refused(tmp_path):
    """R10 meets R7: `nothing` on a module body that reads is the same lie."""
    doc = '"""Reads: nothing — planted."""\n'
    _, out, _ = judge_planted(tmp_path, {"hooks/a.py": doc + READING_BODY})
    assert out == [contradiction("hooks/a.py (module body)", 3, "os.environ")]


# --- R9: the failure is the instruction ------------------------------------------


def test_every_finding_text_is_pinned_whole():
    """R9 (§14): each finding names its site and its repair."""

    class U:
        key, line, hash = "hooks/a.py#f", 3, "0123abcd"

    class M:
        path = "hooks/a.py"

    grammar = (
        "`Reads: <owned|observed|guess> — <what it reads>; unknown "
        "<refused|passed|mixed>`, or `Reads: nothing — <why it reads nothing>`"
    )
    assert undeclared(U) == (
        "hooks/a.py#f (line 3) declares no input class. Add one line to its "
        f"docstring: {grammar}. A unit that stood undeclared when the census "
        "was cut, and has not changed since, keeps its census line "
        "`hooks/a.py#f@0123abcd` in tests/undeclared_readers.txt; every other "
        "unit declares."
    )
    decl = rr.Declaration("Reads: maybe", "maybe", "", "a problem")
    assert malformed_declaration("hooks/a.py#f (line 3)", decl) == (
        "hooks/a.py#f (line 3) declares `Reads: maybe`, read as class `maybe` "
        f"and direction `(none)`: a problem. The grammar is {grammar}."
    )
    assert declared_twice("hooks/a.py#f (line 3)", 2) == (
        "hooks/a.py#f (line 3) carries 2 `Reads:` lines. A unit declares once, "
        "the weakest class it reads, `guess` being the weakest."
    )
    assert census_unit_changed(U, 7, "hooks/a.py#f@99999999") == (
        "hooks/a.py#f (line 3) changed since tests/undeclared_readers.txt:7 "
        "listed it as `hooks/a.py#f@99999999`, and its hash is now 0123abcd. "
        "Declare it and remove its census line."
    )
    assert census_line_names_nothing(2, "hooks/a.py#g@0123abcd", GONE) == (
        "tests/undeclared_readers.txt:2 `hooks/a.py#g@0123abcd` names no "
        "undeclared unit: no top-level unit of that name is in the file: it "
        "went, or was renamed. Remove the line."
    )
    assert DECLARED_SINCE == "the unit declares now"
    assert OUTSIDE == (
        "the file is not in the population: it is untracked, or a test module"
    )
    assert module_undeclared(M, 2, "os.environ") == (
        "hooks/a.py reads at module level — `os.environ` at line 2 — and its "
        "module docstring carries no `Reads:` line. Declare for the module body "
        f"in the module docstring: {grammar}."
    )
    assert failure(["a", "b"]) == "2 reader-registry finding(s):\na\nb"
