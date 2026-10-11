"""A unit is bounded only where a real parser decides its extent, and a
quoted line is the format everywhere else (#870, #848).

Every file that was not `.py` or `.md` went through one rule — a declaration
line, then every line until the next line at the same or lower indentation.
In a brace language the indentation is formatting, so the rule ended a
Prettier-formatted multi-line TypeScript signature at its `): number {` line,
and the body sat outside the hash: a rewrite of it read `ok`. A bracket walk
over a hand-written lexer replaced it for one round, and round 1 found it
misreading the same shape through a regex. A rule that imitates a grammar
without that language's parser is right until the next form it does not
know, and silent there.

What is left is two rules that read a format the file itself declares —
Python's own `ast` and CommonMark's heading path — and the quoted line,
whose region is the paragraph it sits in.

  the table      `bounding_rule` answers "ast", "heading" or None, and the
                 four units that used to test the suffix read it
  the refusals   a `.py` that will not parse, a bare symbol in markdown, a
                 bare symbol in any other file: BROKEN, the reason and the
                 anchor to write instead on the line
  the format     a quoted line hashes its paragraph, so #848's function is
                 one quote, and a unit with blank lines one quote a paragraph
  one reading    `judge`, `read_citation`, the rider check and the survivor
                 sweep read the refusal from `resolve_unit`, none re-derives it
"""

import ast
import importlib.util
import os
import re
import subprocess
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, "skills", "evidence-check", "scripts", "evidence_check.py")
RIDER = os.path.join(ROOT, ".github", "scripts", "rider_check.py")
SURVIVOR = os.path.join(ROOT, "skills", "code-review", "scripts", "survivor_check.py")


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ec = _load("specseal_evidence_check_870", SCRIPT)


def run(args, cwd):
    return subprocess.run(
        [sys.executable, SCRIPT, *args],
        cwd=cwd,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


@pytest.fixture
def repo(tmp_path):
    d = tmp_path / "proj"
    (d / "src").mkdir(parents=True)
    (d / "seal" / "ledger").mkdir(parents=True)
    return d


def cite(repo, coordinate):
    """One ledger row citing COORDINATE, as a fragment."""
    (repo / "seal" / "ledger" / "f.md").write_text(
        "| Clause | Code grounds | Verified behavior | Checked | Notes |\n"
        "|---|---|---|---|---|\n"
        f"| C1 | `{coordinate}` | read | 2026-10-08 | n |\n",
        encoding="utf-8",
    )
    return (repo / "seal" / "ledger" / "f.md").read_text(encoding="utf-8")


def no_rule(path, named):
    """The refusal a bare symbol in PATH reads, pinned whole (§14): why no
    unit is bounded, and the anchor's shape so the row can be written
    without opening the skill."""
    return (
        f"no bounding rule for {named}; anchor a quoted line instead: "
        f'`{path}#"<a line of the unit>"@00000000`, whose region is the '
        "paragraph that line sits in, and `--reverify` fills the hash"
    )


# --- S3: every suffix outside the two parsers refuses a bare symbol -------

RUBY = "def render\n  1\nend\n"
NO_RULE = no_rule("svc.rb", "`.rb`")

# The suffixes the bracket walk and the block rule read for one round, a
# suffix neither ever read, and no suffix at all.
REFUSED = [
    ".ts",
    ".tsx",
    ".js",
    ".jsx",
    ".mjs",
    ".cjs",
    ".c",
    ".h",
    ".cc",
    ".cpp",
    ".hpp",
    ".cs",
    ".java",
    ".kt",
    ".kts",
    ".swift",
    ".go",
    ".rs",
    ".yml",
    ".yaml",
    ".rb",
    "",
]


@pytest.mark.parametrize("suffix", REFUSED)
def test_a_bare_symbol_outside_the_two_parsers_is_refused_with_the_shape(suffix):
    """S3. One sentence for every suffix, with the anchor's shape on it;
    the rider check returns the same sentence, read from the same answer."""
    path = f"src/unit{suffix}"
    text = "f() {\n  x\n}\n\nf:\n  - a\n"
    unit = ec.resolve_unit(path, "f", text)
    named = f"`{suffix}`" if suffix else "a file with no suffix"
    assert unit.places == [] and unit.refused == no_rule(path, named), unit.refused
    assert ec.bounding_rule(path) is None
    riders = _load("rider_check_870_" + (suffix.strip(".") or "none"), RIDER)
    assert riders.region_lines(ec, path, "f", text) == (None, no_rule(path, named))


def test_a_bare_symbol_in_a_suffix_no_rule_names_is_refused_with_the_remedy(repo):
    """S3's command half: the check prints the refusal and exits 2,
    `--reverify` prints it and writes nothing, and the quoted-line anchor it
    names resolves (S4's `.rb` half)."""
    unit = ec.resolve_unit("svc.rb", "render", RUBY)
    assert unit.places == [] and unit.refused == NO_RULE, unit.refused
    assert ec.resolve_unit("svc.rb", '"def render"', RUBY).places == [(1, 3)]
    assert ec.resolve_unit("svc.rb", '"def render"', RUBY).refused is None
    # A refused suffix yields no units, so the rename scan names nothing there.
    assert ec.file_units("svc.rb", "def render(x)\n  1\nend\n") == []

    (repo / "src" / "svc.rb").write_text(RUBY, encoding="utf-8")
    ledger = cite(repo, "src/svc.rb#render@00000000")
    r = run(["."], str(repo))
    assert r.returncode == 2, r.stdout
    assert "BROKEN" in r.stdout and no_rule("src/svc.rb", "`.rb`") in r.stdout, r.stdout
    rr = run(["--reverify", "--checked", "2026-10-08", "."], str(repo))
    assert no_rule("src/svc.rb", "`.rb`") in rr.stdout + rr.stderr, rr.stdout
    assert (repo / "seal" / "ledger" / "f.md").read_text(encoding="utf-8") == ledger


def test_a_bare_symbol_in_markdown_is_refused_and_names_the_heading_path():
    """S6. The heading rule bounds a quoted heading path; a bare symbol names
    no heading."""
    text = "## A\n\nrender: x\n  y\n"
    unit = ec.resolve_unit("d.md", "render", text)
    assert unit.places == [], unit
    assert unit.refused == (
        "a markdown unit is a heading, and a bare symbol names none — "
        'anchor its heading path instead, `"## <heading>"`'
    )
    assert ec.resolve_unit("d.md", '"## A"', text).places == [(1, 4)]


# --- S5: Python refuses, never guesses -------------------------------------

# A multi-line `def` the running interpreter cannot read, because of one
# deliberate SyntaxError line below it. The indentation rule bounded `f` at
# lines 1-2: `):` sits at the declaration's own indent.
UNPARSEABLE = "def f(\n    a,\n):\n    return a\n\nx = (:\n"


def test_a_python_file_that_will_not_parse_is_refused_naming_the_interpreter(repo):
    """S5. The fall-through to the text rule hashed lines 1-2 of the five
    and left the body out, silently. The refusal names the interpreter so a
    reader can tell a grammar mismatch from a missing file, and the line of
    the error so they can find it."""
    assert ec.py_spans(UNPARSEABLE) is None
    unit = ec.resolve_unit("bad.py", "f", UNPARSEABLE)
    version = ".".join(str(n) for n in sys.version_info[:3])
    assert unit.places == [], unit
    assert unit.refused.startswith(f"Python {version} cannot parse this file ("), (
        unit.refused
    )
    assert "at line 6)" in unit.refused, unit.refused
    assert unit.refused.endswith(
        "so no unit in it is bounded and none is guessed at — run the checker "
        "on the Python the file is written for, or anchor a quoted line instead"
    ), unit.refused

    lines = ec.gfm_lines(UNPARSEABLE)
    old = ec.content_hash(lines[0:2])
    (repo / "src" / "bad.py").write_text(UNPARSEABLE, encoding="utf-8")
    cite(repo, f"src/bad.py#f@{old}")
    r = run(["."], str(repo))
    assert r.returncode == 2 and "BROKEN" in r.stdout, r.stdout
    assert f"Python {version} cannot parse" in r.stdout, r.stdout
    assert old not in r.stdout.replace(f"#f@{old}", ""), r.stdout


def test_a_python_file_that_parses_is_read_as_it_was():
    parsing = UNPARSEABLE.replace("x = (:\n", "x = 1\n")
    assert ec.resolve_unit("ok.py", "f", parsing).places == [(1, 4)]
    assert ec.resolve_unit("ok.py", "f", parsing).refused is None
    assert ec.resolve_unit("ok.py", "missing", parsing).refused is None


# --- S7: one reading reaches every caller ----------------------------------


def callers(path, name):
    """{function: source of its body} for every function in PATH whose body
    calls NAME, by name or as an attribute."""
    tree = ast.parse(open(path, encoding="utf-8").read())
    out = {}

    def walk(node, owner):
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                walk(child, child)
                continue
            if isinstance(child, ast.Call) and owner is not None:
                f = child.func
                called = f.id if isinstance(f, ast.Name) else getattr(f, "attr", None)
                if called == name:
                    out[owner.name] = ast.unparse(owner)
            walk(child, owner)

    walk(tree, None)
    return out


def test_every_caller_reads_the_refusal_from_resolve_unit_and_derives_none():
    """S7. Two readings of one coordinate describe one row two ways (#809).
    So the refusal travels in `resolve_unit`'s answer, and the callers that
    print a verdict ask that answer for it; none of the five asks the suffix
    table or the parser for itself."""
    found = {
        "evidence_check": callers(SCRIPT, "resolve_unit"),
        "rider_check": callers(RIDER, "resolve_unit"),
        "survivor_check": callers(SURVIVOR, "resolve_unit"),
    }
    assert {k: sorted(v) for k, v in found.items()} == {
        "evidence_check": ["judge", "read_citation", "resolve"],
        "rider_check": ["region_lines"],
        "survivor_check": ["resolves"],
    }, found
    for module, funcs in found.items():
        for name, source in funcs.items():
            for derived in ("bounding_rule(", "py_spans(", "unbounded("):
                assert derived not in source, f"{module}.{name} calls {derived}"
    for name, source in [
        ("judge", found["evidence_check"]["judge"]),
        ("read_citation", found["evidence_check"]["read_citation"]),
        ("region_lines", found["rider_check"]["region_lines"]),
    ]:
        assert ".refused" in source, f"{name} drops the refusal"


def test_no_reader_of_a_resurrection_flag_is_left():
    """S7, widened. Once no text rule exists, nothing can resurrect a place,
    and a field nothing sets is read by nobody honestly: `resolve_unit`'s
    answer is no tuple to unpack a second field from, and no script names
    the flag."""
    unit = ec.resolve_unit("ok.py", "f", "def f():\n    pass\n")
    assert not isinstance(unit, tuple), type(unit)
    assert unit.places == [(1, 2)] and unit.refused is None
    with pytest.raises(TypeError):
        _places, _ = unit
    for path in (SCRIPT, RIDER, SURVIVOR):
        assert "resurrected" not in open(path, encoding="utf-8").read(), path
    assert [len(u) for u in ec.file_units("a.py", "def f():\n    pass\n")] == [2]


def test_two_identical_places_are_one_place_for_a_row_with_no_claim(repo):
    """`judge` lost its resurrection branch and kept the tie-break: two
    places that both reconstruct the recorded hash are identical spans, so
    choosing between them is no choice at the major level, and the row reads
    OK rather than ambiguous."""
    twins = "def render(x):\n    log(x)\n\n\ndef render(x):\n    log(x)\n"
    (repo / "src" / "app.py").write_text(twins, encoding="utf-8")
    h = ec.content_hash(["def render(x):", "    log(x)"])
    cite(repo, f"src/app.py#render@{h}")
    r = run(["."], str(repo))
    assert r.returncode == 0 and "1 ok" in r.stdout, r.stdout


def test_a_citation_of_a_released_row_by_a_bare_symbol_is_refused(tmp_path):
    """`read_citation` is the fourth caller: a citing row's first coordinate
    names a section of a released ledger file. A bare symbol there names no
    heading, and the line says so rather than calling the section gone."""
    body = "# 0.3.0\n\n## Rows\n\n| R1 · claim | `a.py#f@00000000` |\n"
    released = tmp_path / "seal" / "releases"
    released.mkdir(parents=True)
    (released / "0.3.0.md").write_text(body, encoding="utf-8")
    cite = ec.ANCHOR_RE.search('`seal/releases/0.3.0.md#Rows>"| R1 · claim"@0000abcd`')

    def load(path):
        return "id", (path, body, ec.gfm_lines(body), {5: None})

    verdict, at = ec.read_citation(cite, "Re-read", str(tmp_path), {}, None, load)
    assert verdict.status == "BROKEN" and at is None, verdict
    assert verdict.detail == ec.resolve_unit("x.md", "Rows", body).refused, verdict


def test_the_survivor_sweep_reads_a_refused_anchor_as_not_resolving():
    """A refused anchor resolves at neither end of a range, so it never
    counts as one the range removed. The sweep reads `resolve_unit`'s places,
    which a refusal leaves empty."""
    assert not ec.resolve_unit("bad.py", "f", UNPARSEABLE).places
    assert not ec.resolve_unit("svc.rb", "render", RUBY).places


# --- S8: one suffix table, three answers -----------------------------------


def test_the_four_dispatches_read_one_table():
    """S8. Four units tested the suffix on their own (inventory E16), so a
    language added in one was missing in three. The table answers "ast",
    "heading" or None and nothing else."""
    answers = {
        ec.bounding_rule(f"x{suffix}")
        for suffix in [".py", ".pyi", ".md", ".markdown", ".mdx", *REFUSED]
    }
    assert answers == {"ast", "heading", None}, answers
    assert ec.bounding_rule("a.py") == ec.bounding_rule("a.pyi") == "ast"
    assert ec.bounding_rule("a.md") == "heading"
    source = open(SCRIPT, encoding="utf-8").read()
    tree = ast.parse(source)
    bodies = {
        n.name: ast.unparse(n)
        for n in ast.walk(tree)
        if isinstance(n, ast.FunctionDef)
        and n.name in ("resolve_unit", "minor_region", "file_units", "content_matches")
    }
    assert len(bodies) == 4, sorted(bodies)
    for name, body in bodies.items():
        assert "bounding_rule(" in body, f"{name} does not read the table"
        for spelled in ('endswith(".py")', "endswith('.py')", ".md')", '.md")'):
            assert spelled not in body, f"{name} tests the suffix itself: {spelled}"


# --- S1, S2, S4: the quoted line is the format, and its region a paragraph ---

MULTI_LINE = (
    "export function multiLine(\n"
    "  opts: { a: number },\n"
    "): number {\n"
    "  return opts.a + 1\n"
    "}\n"
)


def test_848_is_answered_by_a_quoted_line_that_hashes_the_function():
    """S1. #848's function has no blank line inside it, so one quote of its
    signature hashes lines 1-5, body included; its bare symbol is refused."""
    assert ec.resolve_unit(
        "f.ts", '"export function multiLine("', MULTI_LINE
    ).places == [(1, 5)]
    assert ec.resolve_unit("f.ts", "multiLine", MULTI_LINE).refused == no_rule(
        "f.ts", "`.ts`"
    )


def test_848s_reproduction_reads_a_body_edit_as_drifted(repo):
    """#848's own script, with the quoted anchor: stamp the row with
    `--reverify`, change the body only, and `--strict` says DRIFTED where the
    indentation rule said `1 ok`."""
    (repo / "f.ts").write_text(MULTI_LINE, encoding="utf-8")
    cite(repo, 'f.ts#"export function multiLine("@00000000')
    ledger = "seal/ledger/f.md"
    rr = run(
        ["--reverify", "--checked", "2026-10-07", "--ledger", ledger, "."], str(repo)
    )
    assert rr.returncode == 0, rr.stdout + rr.stderr
    assert run(["--strict", "--ledger", ledger, "."], str(repo)).returncode == 0
    body = MULTI_LINE.replace("return opts.a + 1", "return opts.a * 100")
    (repo / "f.ts").write_text(body, encoding="utf-8")
    r = run(["--strict", "--ledger", ledger, "."], str(repo))
    assert r.returncode != 0 and "DRIFTED" in r.stdout, r.stdout
    assert "content changed at 1-5" in r.stdout, r.stdout


def test_a_quoted_line_is_its_paragraph_and_never_a_function():
    """S2. A blank line inside a unit divides it, and each quote hashes the
    paragraph it is in; a row resting on both quotes one line of each."""
    text = "export function g(\n  a: number,\n) {\n  const x = a;\n\n  return x;\n}\n"
    assert ec.resolve_unit("g.ts", '"export function g("', text).places == [(1, 4)]
    assert ec.resolve_unit("g.ts", '"return x;"', text).places == [(6, 7)]


def test_a_quoted_line_resolves_in_any_file():
    """S4. The quoted line needs no rule, so it resolves in a refused suffix
    and in this repository's own workflow, whose `pytest` job holds no blank
    line from its key to its last step."""
    assert ec.resolve_unit("svc.rb", '"def render"', RUBY).places == [(1, 3)]
    rel = ".github/workflows/test.yml"
    text = open(os.path.join(ROOT, rel), encoding="utf-8").read()
    lines = ec.gfm_lines(text)
    (place,) = ec.resolve_unit(rel, '"pytest:"', text).places
    start, end = place
    assert lines[start - 1].strip() == "pytest:", place
    assert all(line.strip() for line in lines[start - 1 : end]), place
    assert end == len(lines) or not lines[end].strip(), place
    assert end - start > 10, place


# --- round 2: a claim is bounded by the parser, or is its own line ---------


def test_a_claim_in_a_file_no_parser_reads_is_its_line():
    """Round 2's 🟡 1. A quoted claim was grown through every following line
    deeper than it, in every file: an indentation guess at the claim level,
    which ended a claim on #848's signature line at line 2. In a file no
    parser reads, a claim is the line it quotes, and the row says so on its
    face; a bare minor anchor there is a literal and the same."""
    claim = '"export function multiLine("'
    (region,) = ec.resolve_unit("f.ts", claim, MULTI_LINE).places
    assert region == (1, 5)
    assert ec.minor_region("f.ts", MULTI_LINE, region, claim) == [(1, 1)]
    assert ec.minor_region("f.ts", MULTI_LINE, region, '"opts: {"') == [(2, 2)]
    assert ec.minor_region("f.ts", MULTI_LINE, region, "return") == [(4, 4)]


BLACK = "def f(\n    a,\n):\n    if a:\n        b = 1\n        c = 2\n    return a\n"


def test_a_claim_in_python_is_the_statement_ast_gives():
    """Round 2's 🟡 1 in `.py`: the indentation guess ended a claim on a
    Black-formatted `def f(` at line 2, before its `):`. `ast` decides the
    statement a quoted line sits in, so the claim is the innermost statement
    holding that line: the whole definition for its first line, the `if`
    block for its header, and a line alone where it is a statement of its
    own."""
    (region,) = ec.resolve_unit("b.py", "f", BLACK).places
    assert region == (1, 7)
    assert ec.minor_region("b.py", BLACK, region, '"def f("') == [(1, 7)]
    assert ec.minor_region("b.py", BLACK, region, '"if a:"') == [(4, 6)]
    assert ec.minor_region("b.py", BLACK, region, '"b = 1"') == [(5, 5)]
    assert ec.minor_region("b.py", BLACK, region, '"return a"') == [(7, 7)]


def test_a_claim_row_in_python_drifts_on_an_edit_inside_its_statement(repo):
    """The command half: a claim on the `if` header hashes the block `ast`
    gives, so an edit to the block's last line reads DRIFTED at 4-6."""
    (repo / "src" / "b.py").write_text(BLACK, encoding="utf-8")
    cite(repo, 'src/b.py#f>"if a:"@00000000')
    ledger = "seal/ledger/f.md"
    fill = ["--reverify", "--checked", "2026-10-12", "--ledger", ledger, "."]
    assert run(fill, str(repo)).returncode == 0
    assert run(["--strict", "--ledger", ledger, "."], str(repo)).returncode == 0
    edited = BLACK.replace("c = 2", "c = 3")
    (repo / "src" / "b.py").write_text(edited, encoding="utf-8")
    r = run(["--strict", "--ledger", ledger, "."], str(repo))
    assert r.returncode != 0 and "content changed at 4-6" in r.stdout, r.stdout


# --- round 2: the remedy is written on the row's own path ------------------


def test_a_mapped_row_is_told_its_own_path(repo, tmp_path):
    """Round 2's 🟡 2. The shape is the edit to make, so it carries the
    `--map` prefix: written on the path inside the mapped checkout, the
    copied row would cite ROOT."""
    other = tmp_path / "orig"
    (other / "src").mkdir(parents=True)
    (other / "src" / "x.ts").write_text("export function f() {\n}\n", encoding="utf-8")
    cite(repo, "legacy/src/x.ts#f@00000000")
    r = run(["--strict", "--map", f"legacy={other}", "."], str(repo))
    assert no_rule("legacy/src/x.ts", "`.ts`") in r.stdout, r.stdout
    ledger = repo / "seal" / "ledger" / "f.md"
    ledger.write_text(
        "| C1 | `legacy/src/x.ts:1-2` | read | 2026-09-01 | n |\n", encoding="utf-8"
    )
    _migrated, left, _unproven = ec.migrate(
        [str(ledger)], str(repo), {"legacy": str(other)}
    )
    assert dict(left)["legacy/src/x.ts:1-2"] == no_rule("legacy/src/x.ts", "`.ts`")


def test_a_quoted_line_that_is_gone_says_to_quote_it_as_it_reads_now(repo):
    """Round 2's ⬜ 4. A reworded quoted line read `locator not found` and
    nothing else; no rename scan reads a file no parser reads, so the line
    says what to do."""
    (repo / "src" / "f.ts").write_text(MULTI_LINE, encoding="utf-8")
    cite(repo, 'src/f.ts#"export function gone("@00000000')
    r = run(["."], str(repo))
    assert r.returncode == 2, r.stdout
    assert (
        'src/f.ts#"export function gone("  locator not found — the quoted text '
        "is not in the file; quote the line as it reads now"
    ) in r.stdout, r.stdout


# --- S9: the guessing reader is gone ---------------------------------------

GONE = (
    "BRACE_FAMILY",
    "BRACE_SUFFIXES",
    "BLOCK_SUFFIXES",
    "brace_family",
    "StringForm",
    "_literal_at",
    "brace_lexed",
    "brace_span",
    "block_span",
    "declaration_opener",
    "opens_declaration",
    "STATEMENT_WORDS",
    "generic_units",
)


def test_no_rule_that_imitates_a_grammar_is_left_in_the_checker():
    """S9. The lexer, the walk, the block rule and the declaration opener
    each read someone else's text without that language's parser."""
    source = open(SCRIPT, encoding="utf-8").read()
    tree = ast.parse(source)
    defined = {
        n.name for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.ClassDef))
    } | {
        t.id
        for n in ast.walk(tree)
        if isinstance(n, ast.Assign)
        for t in n.targets
        if isinstance(t, ast.Name)
    }
    assert not defined & set(GONE), sorted(defined & set(GONE))
    for word in GONE:
        assert not re.search(r"\b" + re.escape(word) + r"\b", source), word


# --- S13: `--migrate` names the remedy where it leaves a row ---------------


def test_migrate_leaves_a_row_in_a_refused_file_with_the_refusal(repo):
    """S13. An old `path:line` row in a file no rule bounds is left, and the
    reason a person reads names the quoted-line anchor rather than "no
    single unit contains"."""
    (repo / "src" / "svc.rb").write_text(RUBY, encoding="utf-8")
    (repo / "src" / "bad.py").write_text(UNPARSEABLE, encoding="utf-8")
    ledger = repo / "seal" / "ledger" / "f.md"
    ledger.write_text(
        "| C1 | `src/svc.rb:1-3` | read | 2026-09-01 | n |\n"
        "| C2 | `src/bad.py:1-4` | read | 2026-09-01 | n |\n",
        encoding="utf-8",
    )
    before = ledger.read_text(encoding="utf-8")
    migrated, left, _unproven = ec.migrate([str(ledger)], str(repo))
    assert migrated == 0, left
    reasons = dict(left)
    assert reasons["src/svc.rb:1-3"] == no_rule("src/svc.rb", "`.rb`"), left
    assert reasons["src/bad.py:1-4"].startswith("Python "), left
    assert ledger.read_text(encoding="utf-8") == before


# --- S11, S12: what a person reads says what the code does ----------------

SKILL = os.path.join(ROOT, "skills", "evidence-check", "SKILL.md")
POLICY = os.path.join(ROOT, "docs", "the-evidence-ledger.md")
FRAGMENT = os.path.join(
    ROOT,
    "seal",
    "specs",
    "1791384159-a-unit-the-extractor-cannot-bound-is-refused",
    "changelog.md",
)


def flat(path):
    return " ".join(open(path, encoding="utf-8").read().split())


def module_docstring(path):
    return ast.get_docstring(ast.parse(open(path, encoding="utf-8").read())) or ""


def test_the_skill_no_longer_describes_the_indentation_rule():
    """S11. Every sentence that described a rule bounding a unit without that
    language's parser left with the rule; a reader who met one would expect
    a span the checker no longer computes. The skill says what the region of
    a quoted line is instead."""
    texts = {
        "SKILL.md": flat(SKILL),
        "the-evidence-ledger.md": flat(POLICY),
        "rider_check.py": " ".join(module_docstring(RIDER).split()),
    }
    for where, text in texts.items():
        for gone in (
            "bracket walk",
            "block rule",
            "declaration rule",
            "resurrect",
            "how sure it is",
            "lands on the closing brace in a brace language",
            "| a symbol elsewhere |",
        ):
            assert gone not in text.lower(), (where, gone)
    skill = texts["SKILL.md"]
    assert "A quoted line hashes the paragraph it is in and is never a function" in (
        skill
    ), "the region table lost the paragraph rule"
    assert "a unit with blank lines inside it is cited one quote per paragraph" in (
        skill
    )


def test_the_policy_paragraph_names_the_cases_that_enforce_it():
    policy = open(POLICY, encoding="utf-8").read()
    marker = "<!-- specs/1791384159-a-unit-the-extractor-cannot-bound-is-refused -->"
    paragraph = policy.split(marker, 1)[1].split("\n\n", 1)[0]
    enforced = [
        line for line in paragraph.splitlines() if line.startswith("Enforced by:")
    ]
    assert len(enforced) == 1, paragraph
    for case in (
        "test_848_is_answered_by_a_quoted_line_that_hashes_the_function",
        "test_a_bare_symbol_outside_the_two_parsers_is_refused_with_the_shape",
    ):
        assert (
            f"test_a_unit_the_extractor_cannot_bound_is_refused.py::{case}"
            in (enforced[0])
        ), case


def test_the_changelog_fragment_tells_an_installer_what_to_run():
    """S12. The fragment is gathered into the release's notes, so it holds no
    `## ` line, and its `### Changed` entry says what an installer meets on
    upgrade and what each asks of them — and promises no verdict that
    changes, which the first design's fragment did (round 1's 🟡 3)."""
    text = open(FRAGMENT, encoding="utf-8").read()
    assert not [line for line in text.splitlines() if line.startswith("## ")]
    changed = " ".join(text.split("### Changed", 1)[1].split())
    for said in (
        "What an installer sees on upgrade",
        "every row citing a bare symbol in a file that is not `.py`, `.pyi` or "
        "`.md` reads `BROKEN` with the remedy on its line",
        "then run `evidence-check --reverify`",
        "`Corrected ·` row `--reverify` names",
        "stub that is decorated, or whose signature runs over several lines, "
        "reads `DRIFTED` once",
        "A row with a quoted claim",
        "Every `.md` row, and every `.py` row without a quoted claim, keeps its "
        "hash and its verdict",
    ):
        assert said in changed, said
    assert "every other row keeps its hash" not in changed
    # Round 2: a `.py` claim row can move, so the promise no longer covers it.
    assert "Every `.py` and `.md` row keeps its hash" not in changed
