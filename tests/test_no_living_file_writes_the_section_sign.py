"""No living file writes the section sign (#1005).

A reader can take the sign for syntax, so a living file cites in words, in
the shape `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만
읽히게 쓴다* states.

The records of a moment keep what they said when they were written:
`seal/specs/`, `changelog/`, `CHANGELOG.md`, and `evals/behaviour/`, whose
cases are generated from records. A fixture that needs the sign builds it
from its name, `\\N{SECTION SIGN}`, so its own file stays clean.
"""

import os

from conftest import build_tracked_tree, git_listing, on_disk

ROOT = os.path.join(os.path.dirname(__file__), "..")
SIGN = "\N{SECTION SIGN}"
RECORDS = ("seal/specs/", "changelog/", "CHANGELOG.md", "evals/behaviour/")
SAYS = (
    "a living file writes the section sign. Cite a contract rule as "
    "`contract rule <N>`, and another file's section by its path and its "
    "heading text in italics:"
)


def signs(root=ROOT):
    """[`<path>:<line>`] for every line of a tracked living file that holds
    the sign. A file that does not decode as UTF-8 is not text and is not
    read."""
    listed = [
        rel for rel in git_listing(root, "ls-files") if not rel.startswith(RECORDS)
    ]
    present, _missing = on_disk(root, listed)
    found = []
    for rel in present:
        try:
            with open(os.path.join(root, rel), encoding="utf-8") as handle:
                text = handle.read()
        except UnicodeDecodeError:
            continue
        found.extend(
            f"{rel}:{n}" for n, line in enumerate(text.splitlines(), 1) if SIGN in line
        )
    return found


def test_no_living_file_writes_the_section_sign():
    """S3 of #1005."""
    found = signs()
    assert not found, SAYS + "\n" + "\n".join(found)


def test_a_sign_is_refused_at_its_line_and_a_record_is_not_read(tmp_path):
    """The case can fail, names the path and the line, and leaves the four
    record paths alone."""
    line = f"see {SIGN}3\n"
    root = build_tracked_tree(
        tmp_path / "r",
        {
            "docs/a.md": "clean\n" + line,
            "hooks/b.py": "# clean\n",
            "seal/specs/1-x/spec.md": line,
            "changelog/0.1.0.md": line,
            "CHANGELOG.md": line,
            "evals/behaviour/c.md": line,
            "seal/follow-up.md": line,
        },
    )
    assert signs(root) == ["docs/a.md:2", "seal/follow-up.md:1"]
