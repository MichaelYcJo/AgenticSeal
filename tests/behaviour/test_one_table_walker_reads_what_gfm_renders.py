"""The oracle `lib/tables.py#gfm_table` is held to, held first (#647).

`tests/gfm_table_oracle.py` says which tables GitHub's renderer, `cmarkgfm`,
puts in a markdown document, and their cells. The cases here hold the
oracle itself: it imports the renderer and nothing of this repository's, it
gives the two facts round 3 of #735 executed, and a tag left half written
above a table does not hide the table from it.

The walker's cases against the oracle, over the corpus enumerated from the
CommonMark and GFM block kinds, are `tests/lib/test_tables.py`'s
`Test_gfm_table`, with the corpus, and #1489's phase 3 moved them there.
"""

import gfm_table_oracle as oracle
from conftest import imported_roots

# --- the oracle is independent ---------------------------------------------


def test_the_oracle_imports_the_renderer_and_nothing_of_this_repositorys():
    """The oracle shares no code with the walk it checks, as
    `tests/commonmark_oracle.py` shares none with the readers under `lib/`
    (#667)."""
    assert imported_roots(oracle.__file__) == {"cmarkgfm", "html"}
    with open(oracle.__file__, encoding="utf-8") as handle:
        source = handle.read()
    # `tests/gfm_table_oracle.py` *It shares nothing with what it checks*:
    # the oracle's code reaches nothing under `lib/`, `skills/` or
    # `.github/`, by a path or through the import machinery.
    for reach in ("sys.path", "importlib", "lib/", "skills/", ".github/"):
        assert reach not in source.split('"""', 2)[-1], reach


def test_the_oracle_reads_a_table_and_a_row_gfm_adds():
    """The two facts round 3 of #735 executed, read through the oracle: an
    autolink line under a table is one of its rows, and a thematic break
    ends it."""
    head = "| Signer |\n|---|\n| https://example.com/org/a |\n"
    assert oracle.rows_under(head + "<https://example.com/org/b>\n", ("Signer",)) == [
        ("https://example.com/org/a",),
        ("https://example.com/org/b",),
    ]
    assert oracle.rows_under(head + "***\n| x |\n", ("Signer",)) == [
        ("https://example.com/org/a",)
    ]


def test_a_half_written_tag_does_not_hide_the_table_from_the_oracle():
    """`<h1` with no `>` above a table: cmark-gfm renders the table, and an
    oracle printing raw HTML handed `html.parser` a tag that swallowed the
    `<table>` after it, so the oracle said no table."""
    text = "<h1\n\n| Signer |\n|---|\n| https://example.com/org/a |\n"
    assert oracle.rows_under(text, ("Signer",)) == [("https://example.com/org/a",)]
