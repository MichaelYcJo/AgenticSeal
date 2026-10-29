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

from conftest import ROOT

OPENER = "<" + "!--"

# The record templates, `templates/records/`: a work item's records, and
# `process.md`, the process section a work item's changelog fragment ends
# with where it changed the way of working (#1117).


def templates(root=ROOT):
    """Every record template under ROOT's `templates/records/`, sorted."""
    return sorted(glob.glob(os.path.join(root, "templates", "records", "*.md")))


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
    (tmp_path / "templates" / "records").mkdir(parents=True)
    (tmp_path / "templates" / "setup").mkdir()
    (tmp_path / "templates" / "records" / "sdd-x.md").write_text(
        f"# X\n\n{OPENER} guidance -->\n", encoding="utf-8"
    )
    (tmp_path / "templates" / "records" / "process.md").write_text(
        f"# Process changes\n{OPENER} guidance -->\n", encoding="utf-8"
    )
    (tmp_path / "templates" / "setup" / "config.md").write_text(
        f"{OPENER} not a record template -->\n", encoding="utf-8"
    )
    assert comments(str(tmp_path)) == [
        "templates/records/process.md:2",
        "templates/records/sdd-x.md:3",
    ]
