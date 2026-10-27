"""A record template carries no HTML comment (#1005).

A comment in a template is copied into every record started from it, so its
guidance becomes a second copy of the skill or definition the record's writer
reads, and every reader of the record has to model it. The guidance lives
once, where its writer reads it; a template holds headings, table headers,
placeholders, the labelled lines the record's grammar asks for and the foot
line.
"""

import glob
import os

ROOT = os.path.join(os.path.dirname(__file__), "..")
OPENER = "<" + "!--"

# The record templates under `templates/`: a work item's records, and the
# process archive's, whose files live under `seal/process/` (S13 of #945).
RECORD_TEMPLATES = ("sdd-*.md", "process.md")


def templates(root=ROOT):
    """Every record template under ROOT's `templates/`, sorted."""
    return sorted(
        path
        for pattern in RECORD_TEMPLATES
        for path in glob.glob(os.path.join(root, "templates", pattern))
    )


def comments(root=ROOT):
    """[`<path>:<line>`] for every line of a record template that opens an
    HTML comment."""
    found = []
    for path in templates(root):
        rel = os.path.relpath(path, root).replace(os.sep, "/")
        with open(path, encoding="utf-8") as handle:
            lines = handle.read().splitlines()
        found.extend(f"{rel}:{n}" for n, line in enumerate(lines, 1) if OPENER in line)
    return found


def test_the_record_templates_are_found():
    """A glob that matches nothing passes the case below on nothing."""
    assert len(templates()) == 9


def test_no_record_template_carries_a_comment():
    """S10 of #1005."""
    found = comments()
    assert not found, (
        "a record template opens an HTML comment; its guidance belongs in the "
        "skill or definition the record's writer reads:\n" + "\n".join(found)
    )


def test_a_comment_put_back_is_refused_at_its_line(tmp_path):
    (tmp_path / "templates").mkdir()
    (tmp_path / "templates" / "sdd-x.md").write_text(
        f"# X\n\n{OPENER} guidance -->\n", encoding="utf-8"
    )
    (tmp_path / "templates" / "process.md").write_text(
        f"# Process changes\n{OPENER} guidance -->\n", encoding="utf-8"
    )
    (tmp_path / "templates" / "config.md").write_text(
        f"{OPENER} not a record template -->\n", encoding="utf-8"
    )
    assert comments(str(tmp_path)) == [
        "templates/process.md:2",
        "templates/sdd-x.md:3",
    ]
