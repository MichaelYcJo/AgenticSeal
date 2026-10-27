"""What is left of the rules command's old file: the cases that read the
record layout document, the `rule` marker's registration and the settle
skill, which wait for #923.

#942's phase 6 placed the cases of `.github/scripts/rules.py`'s functions in
`tests/test_rules.py`, and this file reads the command through that file's
`rules`.
"""

import os

from test_rules import rules

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SETTLE = os.path.join(ROOT, "skills", "settle", "SKILL.md")


def test_the_slice_document_resolves_every_target():
    """`docs/the-record-layout.md`, the document #944's phase 1 gave every
    rule its test, prints a section line for each of its targets and none
    that does not resolve."""
    path = os.path.join(ROOT, "docs", "the-record-layout.md")
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    out = rules.render(ROOT, text)
    assert out.count("  check, line ") >= 7, out
    # The render's own two line shapes are read, not the bare words, since a
    # marker name or a docstring the render prints may say "refused", as the
    # marker `record-comment-line-refused` does.
    failed = [
        line
        for line in out.splitlines()
        if line.startswith("    refused: ") or ": does not resolve: " in line
    ]
    assert not failed, out


def test_the_rule_marker_is_registered(pytestconfig):
    """`tests/conftest.py` registers `rule`, so a gate test carries it with no
    unknown-mark warning."""
    assert any(line.startswith("rule(") for line in pytestconfig.getini("markers")), (
        pytestconfig.getini("markers")
    )


def test_settle_owns_the_grammar():
    """The grammar is stated once, in the settle skill, the document a spec's
    author reads; this module and `rules.py` only read it."""
    with open(SETTLE, encoding="utf-8") as handle:
        text = handle.read()
    section = text.split("\n## A rule has one shape\n")[1].split("\n## ")[0]
    section = " ".join(section.split())
    for phrase in (
        "starts with `check: `",
        "`check: none reader: <who reads it>`",
        '`@pytest.mark.rule("<marker>")`',
        "It ships `seal rules --check`",
        "it is review's to find",
    ):
        assert phrase in section, f"settle no longer says: {phrase!r}"
