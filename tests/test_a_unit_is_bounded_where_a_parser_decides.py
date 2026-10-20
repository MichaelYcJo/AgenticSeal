"""A unit of a file is bounded where a real parser decides its extent, and
named by content (#870, #519, #867).

`skills/verify/scripts/coordinates.py` is the coordinate kernel
`pact_check.py` and `chain_check.py` load. These are its cases:

  the unit        a symbol through `ast`, a heading path in markdown, a
                  quoted line's paragraph anywhere, and a bare symbol refused
                  where no parser bounds it
  the hash        trailing whitespace and blank lines are no change, and
                  indentation is one
  the parse       one per distinct text, keyed on the text, and no caller's
                  edit reaches the next caller
"""

import importlib.util
import os
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
KERNEL = os.path.join(ROOT, "skills", "verify", "scripts", "coordinates.py")


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ec = _load("specseal_kernel_for_its_cases", KERNEL)


def places(path, locator, text):
    return ec.resolve_unit(path, locator, text).places


SERVICE = (
    "import os\n"
    "\n"
    "\n"
    "def handler(x):\n"
    "    y = x + 1\n"
    "    return y\n"
    "\n"
    "\n"
    "class Box:\n"
    "    def open(self):\n"
    "        return 1\n"
)


# --- a symbol through `ast` ---------------------------------------------------


def test_a_symbol_anchor_resolves_through_ast():
    assert places("src/service.py", "handler", SERVICE) == [(4, 6)]
    assert places("src/service.py", "Box", SERVICE) == [(9, 11)]
    assert places("src/service.py", "Box.open", SERVICE) == [(10, 11)]


def test_a_decorator_is_part_of_the_span():
    """A decorator carries behaviour, so the span starts at the decorator."""
    text = "import functools\n\n\n@functools.cache\ndef f():\n    return 1\n"
    assert places("x.py", "f", text) == [(4, 6)]


def test_a_constant_is_a_unit_too():
    """A module-level constant has no `def` to hang on. `ast` spans the
    whole assignment statement, and `if review not in REVIEW_ANSWERS:` is a
    use it never confuses with the constant."""
    text = (
        "OTHER = 0\n"
        "\n"
        "REVIEW_ANSWERS = (\n"
        "    CHAIN,\n"
        "    DIRECT,\n"
        ")\n"
        "\n"
        "def check(review):\n"
        "    if review not in REVIEW_ANSWERS:\n"
        "        return None\n"
    )
    assert places("r.py", "REVIEW_ANSWERS", text) == [(3, 6)]


def test_a_module_constant_resolves_through_ast_in_a_parsing_file():
    """Module- and class-level assignments are units; a local assignment
    stays a local."""
    text = (
        "LIMIT = 12\n"
        "\n"
        "\n"
        "class Cfg:\n"
        "    RETRIES = 3\n"
        "\n"
        "\n"
        "def use():\n"
        "    n = LIMIT\n"
        "    return n\n"
    )
    assert places("c.py", "LIMIT", text) == [(1, 1)]
    assert places("c.py", "Cfg.RETRIES", text) == [(5, 5)]
    assert places("c.py", "n", text) == []
    assert places("c.py", "use.n", text) == []


def test_a_python_file_that_parses_is_read_as_it_was():
    parsing = "def f(\n    a,\n):\n    return a\n\nx = 1\n"
    assert ec.resolve_unit("ok.py", "f", parsing).places == [(1, 4)]
    assert ec.resolve_unit("ok.py", "f", parsing).refused is None
    assert ec.resolve_unit("ok.py", "missing", parsing).refused is None


# --- a file `ast` cannot read is refused, never guessed at ------------------

# A multi-line `def` the running interpreter cannot read, because of one
# deliberate SyntaxError line below it. The indentation rule bounded `f` at
# lines 1-2: `):` sits at the declaration's own indent.
UNPARSEABLE = "def f(\n    a,\n):\n    return a\n\nx = (:\n"


def test_a_file_that_will_not_parse_yields_no_symbols():
    """None, not `{}`: a file that cannot be parsed is refused, while a file
    that parses and lacks the symbol has no place for it."""
    assert ec.py_spans("def broken(:\n") is None


def test_a_python_file_that_will_not_parse_is_refused_naming_the_interpreter():
    """The fall-through to the text rule hashed lines 1-2 of the five and
    left the body out, silently. The refusal names the interpreter, so a
    reader can tell a grammar mismatch from a missing file, and the line of
    the error, so they can find it."""
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


def test_a_syntax_error_is_refused_rather_than_read_by_the_text_rule():
    """The reason travels with the empty answer."""
    text = "def handler(x):\n    return x + 1\n\ndef broken(:\n"
    assert ec.py_spans(text) is None
    assert places("bad.py", "handler", text) == []
    refused = ec.resolve_unit("bad.py", "handler", text).refused
    assert "cannot parse this file" in refused, refused


# --- a bare symbol where no parser bounds it is refused -------------------


def no_rule(path, named):
    """The refusal a bare symbol in PATH reads, pinned whole (§14): why no
    unit is bounded, and the anchor's shape."""
    return (
        f"no bounding rule for {named}; anchor a quoted line instead, "
        '`"<a line of the unit>"`, whose region is the paragraph that line '
        "sits in"
    )


# The suffixes a bracket walk and a block rule read for one round, a suffix
# neither ever read, and no suffix at all.
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
    """One sentence for every suffix, with the anchor's shape on it."""
    path = f"src/unit{suffix}"
    text = "f() {\n  x\n}\n\nf:\n  - a\n"
    unit = ec.resolve_unit(path, "f", text)
    named = f"`{suffix}`" if suffix else "a file with no suffix"
    assert unit.places == [] and unit.refused == no_rule(path, named), unit.refused
    assert ec.bounding_rule(path) is None


def test_a_bare_symbol_in_markdown_is_refused_and_names_the_heading_path():
    """The heading rule bounds a quoted heading path; a bare symbol names no
    heading."""
    text = "## A\n\nrender: x\n  y\n"
    unit = ec.resolve_unit("d.md", "render", text)
    assert unit.places == [], unit
    assert unit.refused == (
        "a markdown unit is a heading, and a bare symbol names none — "
        'anchor its heading path instead, `"## <heading>"`'
    )
    assert places("d.md", '"## A"', text) == [(1, 4)]


# --- a quoted line is its paragraph ----------------------------------------

RUBY = "def render\n  1\nend\n"
MULTI_LINE = (
    "export function multiLine(\n"
    "  opts: { a: number },\n"
    "): number {\n"
    "  return opts.a + 1\n"
    "}\n"
)


def test_848_is_answered_by_a_quoted_line_that_hashes_the_function():
    """#848's function has no blank line inside it, so one quote of its
    signature spans lines 1-5, body included; its bare symbol is refused."""
    assert places("f.ts", '"export function multiLine("', MULTI_LINE) == [(1, 5)]
    assert ec.resolve_unit("f.ts", "multiLine", MULTI_LINE).refused == no_rule(
        "f.ts", "`.ts`"
    )


def test_a_quoted_line_is_its_paragraph_and_never_a_function():
    """A blank line inside a unit divides it, and each quote spans the
    paragraph it is in."""
    text = "export function g(\n  a: number,\n) {\n  const x = a;\n\n  return x;\n}\n"
    assert places("g.ts", '"export function g("', text) == [(1, 4)]
    assert places("g.ts", '"return x;"', text) == [(6, 7)]


def test_a_quoted_line_resolves_in_any_file():
    """The quoted line needs no rule, so it resolves in a refused suffix and
    in this repository's own workflow, whose `pytest` job holds no blank line
    from its key to its last step."""
    assert places("svc.rb", '"def render"', RUBY) == [(1, 3)]
    assert ec.resolve_unit("svc.rb", '"def render"', RUBY).refused is None
    rel = ".github/workflows/test.yml"
    text = open(os.path.join(ROOT, rel), encoding="utf-8").read()
    lines = ec.gfm_lines(text)
    (place,) = places(rel, '"pytest:"', text)
    start, end = place
    assert lines[start - 1].strip() == "pytest:", place
    assert all(line.strip() for line in lines[start - 1 : end]), place
    assert end == len(lines) or not lines[end].strip(), place
    assert end - start > 10, place


def test_a_hash_in_python_is_a_comment_not_a_heading():
    """The heading rule is markdown-only: in Python a comment block is an
    ordinary contiguous run, and the same bytes in markdown are three H1
    headings, so the first owns only itself."""
    text = "x = 0\n\n# comment one\n# comment two\n# comment three\nVOCAB = 1\n"
    assert places("s.py", '"# comment one"', text) == [(3, 6)]
    assert places("s.md", '"# comment one"', text) == [(3, 3)]


def test_a_text_anchor_owns_its_contiguous_block():
    text = "one\ntwo\nthree\n\nfar away\n"
    assert places("d.txt", '"two"', text) == [(1, 3)]


def test_an_escaped_pipe_matches_a_real_one():
    """A locator naming a markdown table line escapes its pipes or it splits
    the table it lives in, and is unescaped before matching."""
    assert ec.unescape("a \\| b") == "a | b"
    text = "| Target SHA | value |\n"
    assert places("t.md", '"| Target SHA | value |"', text) == [(1, 1)]


# --- a heading path in markdown --------------------------------------------


def test_a_markdown_heading_owns_its_section():
    """Down to the next heading at its level OR ABOVE: a DEEPER one is part
    of the section, not the end of it."""
    text = (
        "# Top\n\nintro\n\n## A\n\nbody of A\n\n"
        "### A1\n\nnested body\n\n## B\n\nbody of B\n"
    )
    assert places("d.md", '"## A"', text) == [(5, 12)]
    assert places("d.md", '"### A1"', text) == [(9, 12)]
    assert places("d.md", '"# Top"', text) == [(1, 15)]


def test_a_markdown_locator_is_a_heading_path():
    """A section runs to the line before the next heading at its level or
    above, and a path narrows inside it."""
    text = "# Top\n\n## A\n\nbody\n\n### Deep\n\nmore\n\n## B\n\nlast\n"
    assert places("d.md", '"## A"', text) == [(3, 10)]
    assert places("d.md", '"## A / ### Deep"', text) == [(7, 10)]


def test_a_repeated_heading_is_disambiguated_by_its_parent():
    text = "## A\n\n### Same\n\none\n\n## B\n\n### Same\n\ntwo\n"
    assert len(places("d.md", '"### Same"', text)) == 2
    assert places("d.md", '"## B / ### Same"', text) == [(9, 11)]


def test_only_a_real_heading_opens_a_section():
    """An INDENTED `## B` normalises to the same text as the heading but is
    not one."""
    text = "## A\n\n    ## B\n\n## B\n\nreal\n"
    assert ec.heading_level("    ## B") is None
    assert places("d.md", '"## B"', text) == [(5, 7)]


def test_a_heading_quoted_in_a_closed_fence_opens_no_section():
    """Read on the lines a renderer shows, a fenced `## B` is no heading: one
    place, and `## A` runs past the fence (#867)."""
    text = "## A\n\nintro\n\n```markdown\n## B\n```\n\nmore\n\n## B\n\nreal\n"
    assert places("d.md", '"## B"', text) == [(11, 13)]
    assert places("d.md", '"## A"', text) == [(1, 10)]


def test_a_heading_indented_three_spaces_is_a_heading_and_an_issue_number_is_not():
    """CommonMark 4.2 lets a heading stand three spaces in, and wants a space
    after the run, so `#84's line` at column 0 is prose and ends no section."""
    text = "## A\n\n#84's line\n\nbody\n\n   ## B\n\nlast\n"
    assert ec.heading_level("   ## B") == 2
    assert ec.heading_level("#84's line") is None
    assert places("d.md", '"## A"', text) == [(1, 6)]
    assert places("d.md", '"## B"', text) == [(7, 9)]


def test_text_regions_reads_a_heading_on_the_lines_it_is_shown():
    """The text is matched on LINES as written and a heading is read on
    SHOWN, so a heading's section ends at a shown heading and not at one a
    fence quotes."""
    text = "## A\n\nbody\n\n```\n## A2\n```\n\n## Z\n"
    lines = ec.gfm_lines(text)
    shown = ec.markdown_lines(text)
    assert ec.text_regions(lines, "## A", True, shown) == [(1, 8)]
    assert ec.text_regions(lines, "## A", True) == [(1, 5)]
    assert ec.text_regions(lines, "## A2", True, shown) == [(5, 7)]


# --- the hash ----------------------------------------------------------------


def test_the_hash_ignores_trailing_whitespace_and_blank_lines():
    a = ["def f():", "    return 1"]
    b = ["def f():   ", "", "    return 1\t"]
    assert ec.content_hash(a) == ec.content_hash(b)


def test_the_hash_does_not_ignore_indentation():
    """A dedent moves a statement out of the block it belonged to."""
    inside = ["def f():", "    if x:", "        go()"]
    outside = ["def f():", "    if x:", "    go()"]
    assert ec.content_hash(inside) != ec.content_hash(outside)


# --- the parse ---------------------------------------------------------------


def test_the_units_of_one_text_cost_one_parse(monkeypatch, tmp_path):
    """Five units of one Python text are one parse, not five (#519). The text
    is made unique to this case, so a parse another case already paid for
    cannot make the count read low."""
    body = (
        f"# {tmp_path}\n" + SERVICE + "\n\ndef third():\n    return 3\n\n\nLIMIT = 4\n"
    )
    parses = []
    real = ec.ast.parse

    def counting(source, *a, **k):
        if source == body:
            parses.append(1)
        return real(source, *a, **k)

    monkeypatch.setattr(ec.ast, "parse", counting)
    for anchor in ("handler", "Box", "Box.open", "third", "LIMIT"):
        assert len(places("src/many.py", anchor, body)) == 1, anchor
    assert len(parses) == 1, f"{len(parses)} parses of one text for five units"


def test_a_file_edited_between_two_reads_gets_its_new_spans():
    """The memo is keyed on the text, never the path. The two texts are the
    same length on purpose: a key that stood in for the text by a cheaper
    property would serve the stale answer here."""
    before = "def aa():\n    return 1\n"
    after = "def bb():\n    return 1\n"
    assert len(before) == len(after)
    assert ec.py_spans(before) == {"aa": [(1, 2)]}
    assert ec.py_spans(after) == {"bb": [(1, 2)]}


def test_changing_the_returned_spans_does_not_reach_the_next_caller():
    """Every caller gets its own dict and its own lists."""
    text = "def f():\n    return 1\n\n\ndef g():\n    return 2\n"
    first = ec.py_spans(text)
    first["f"].append((99, 99))
    first.pop("g")
    assert ec.py_spans(text) == {"f": [(1, 2)], "g": [(5, 6)]}


def test_a_word_ending_in_pact_is_not_a_pact_anchor():
    """`compact:` is a word, and the look-behind keeps it one."""
    assert ec.PACT_ANCHOR_RE.search('compact:x/"## A"@1a2b3c4d') is None
    assert ec.PACT_ANCHOR_RE.search('pact:x/"## A"@1a2b3c4d') is not None
