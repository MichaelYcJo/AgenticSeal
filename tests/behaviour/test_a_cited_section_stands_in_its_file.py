"""A section another file cites is a heading or a bold rule lead that file has.

A file cites another file's section as the backticked path followed by the
section's text in italics, the shape `skills/writing-style/SKILL.md` states.
Before #1043 one case read such citations, and only those of
`skills/implement/SKILL.md`, so a heading renamed in any other file left its
citations pointing at nothing with the suite green. This module reads every
citation in the tracked text files outside the records and resolves each
against the cited file.

The fixtures below cite files under `manual/`, a top-level entry this
repository does not have, so the case that reads this repository does not
read the fixtures' own citations.
"""

import collections
import os
import pathlib
import re
import subprocess

import pytest
from censuses import RECORDS
from conftest import ROOT, build_tracked_tree, load_module, on_disk

rules = load_module(
    os.path.join(ROOT, "skills", "settle", "scripts", "rule_changes.py"),
    "agentic_rule_changes_for_citations",
)

# `read` is how many citations of a repository file were read, and
# `dangling` is `[(citing file, line, cited file, *cited text*)]`.
Found = collections.namedtuple("Found", "read dangling")


# A citation by path: the backticked path alone, then an optional
# possessive, then the italic text. A `<commit>:<path>` matches, and its
# first segment, which holds the colon, is no tracked top-level entry.
PATH_CITED = re.compile(r"`([^`\s]+\.md)`(?:'s)?\s+\*([^*]+)\*")
# A citation by a skill's name, read only where `skills/<name>/SKILL.md` is
# tracked: the name in backticks, or the name and the word `skill's`.
NAME_CITED = re.compile(r"`([a-z0-9][a-z0-9-]*)`(?: skill's)?\s+\*([^*]+)\*")
SKILL_FILE = re.compile(r"skills/([^/]+)/SKILL\.md")
# Outside a `.md` file, a `#` comment marker at the start of a line, so a
# citation wrapped across comment lines reads as one.
COMMENT_MARK = re.compile(r"^([ \t]*)#+[ \t]?", re.M)
# In a `.py` file, a literal's closing quote, the line break, and the next
# literal's opening quote, so adjacent literals read as one.
ADJACENT = re.compile(r"([\"'])[ \t]*\n[ \t]*(?:[rRbBuUfF]{1,2})?\1")
# A list item's marker before a bold rule lead.
LIST_MARK = re.compile(r"(?:[-*+]|\d{1,9}[.)])[ \t]+")


def text_of(path):
    """The UTF-8 text at PATH, or None where it is absent or not UTF-8."""
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read()
    except (OSError, UnicodeDecodeError):
        return None


def flowing(rel, text):
    """TEXT as a citation in file REL is read: adjacent `.py` literals
    joined and comment markers dropped, each line break kept so a match
    counts its line."""
    if rel.endswith(".py"):
        text = ADJACENT.sub("\n", text)
    if not rel.endswith(".md"):
        text = COMMENT_MARK.sub(r"\1", text)
    return text


def cited_in(rel, text, skills):
    """`[(line, cited file, cited text)]` for each citation TEXT makes, the
    line being the one its opening backtick stands on. A cited text holding
    `{` is a format placeholder and is not read."""
    flow = flowing(rel, text)
    found = [(m.start(), m.group(1), m.group(2)) for m in PATH_CITED.finditer(flow)]
    found += [
        (m.start(), f"skills/{m.group(1)}/SKILL.md", m.group(2))
        for m in NAME_CITED.finditer(flow)
        if m.group(1) in skills
    ]
    return sorted(
        (flow.count("\n", 0, at) + 1, target, " ".join(said.split()))
        for at, target, said in found
        if "{" not in said
    )


def sections(text):
    """The texts a citation of the file holding TEXT can name: each live
    heading, and each live bold lead opening a paragraph or a list item, the
    lead's whitespace collapsed."""
    if text is None:
        return []
    r = rules.reader()
    lines = r.gfm_lines(text)
    found = [t for _, _, t in rules.headings(lines)]
    live = [flag for _, flag in r.live_lines(lines)]
    for n, line in enumerate(lines):
        body = line.lstrip()
        marker = LIST_MARK.match(body)
        if marker:
            body = body[marker.end() :]
        opens = marker or n == 0 or not lines[n - 1].strip()
        if not (live[n] and opens and body.startswith("**")):
            continue
        rest, after = body[2:], n + 1
        while "**" not in rest and after < len(lines) and lines[after].strip():
            rest, after = rest + " " + lines[after], after + 1
        if "**" in rest:
            found.append(" ".join(rest.split("**", 1)[0].split()))
    return found


def resolves(said, targets):
    """SAID equals a target, or begins one with the next character neither
    a letter nor a digit; case for case."""
    return any(
        t == said or (t.startswith(said) and not t[len(said)].isalnum())
        for t in targets
    )


def citations(root):
    """Every citation of another file's section in the tracked text files
    under ROOT outside the records, as a `Found`. A citation whose path's
    first segment is no tracked top-level entry is not a repository file's,
    and is not read."""
    listed = subprocess.run(
        ["git", "-C", root, "ls-files", "-z"], capture_output=True, check=True
    ).stdout.decode("utf-8")
    tracked = [rel for rel in listed.split("\0") if rel]
    top = {rel.split("/")[0] for rel in tracked}
    skills = {m.group(1) for m in map(SKILL_FILE.fullmatch, tracked) if m}
    # A positive sweep: a file the working tree deleted cites nothing.
    present, _missing = on_disk(
        root, [rel for rel in tracked if not rel.startswith(RECORDS)]
    )
    held, read, dangling = {}, 0, []
    for rel in present:
        text = text_of(os.path.join(root, rel))
        for line, target, said in cited_in(rel, text or "", skills):
            if target.split("/")[0] not in top:
                continue
            read += 1
            if target not in held:
                where = os.path.join(root, *target.split("/"))
                held[target] = sections(text_of(where) if target in tracked else None)
            if not resolves(said, held[target]):
                dangling.append((rel, line, target, f"*{said}*"))
    return Found(read, dangling)


# --- the tree ---------------------------------------------------------------


def test_every_cited_section_stands_in_its_file():
    """S1: every citation in this repository names a heading or a bold rule
    lead its file has. The floor keeps a reader that stops matching from
    passing on nothing read."""
    found = citations(ROOT)
    assert found.read >= 100, (
        f"only {found.read} citations recognised, so a pass means nothing"
    )
    assert not found.dangling, "a citation names a section its file lacks:\n" + (
        "\n".join(
            f"{rel}:{line} cites `{target}` {cited}"
            for rel, line, target, cited in found.dangling
        )
    )


# --- fixtures ---------------------------------------------------------------


def repo(tmp_path, files):
    return str(build_tracked_tree(tmp_path / "repo", files))


def test_a_renamed_heading_leaves_its_citation_dangling(tmp_path):
    """S2: a citation resolves while its heading stands, and is named with
    its file and line once the heading is renamed."""
    root = repo(
        tmp_path,
        {
            "a.md": "Intro.\n\nSee `manual/b.md` *Old name* for it.\n",
            "manual/b.md": "# B\n\n## Old name\n\nText.\n",
        },
    )
    assert citations(root) == Found(1, [])
    pathlib.Path(root, "manual", "b.md").write_text(
        "# B\n\n## New name\n\nText.\n", encoding="utf-8"
    )
    assert citations(root).dangling == [("a.md", 3, "manual/b.md", "*Old name*")]


def test_a_heading_resolves_a_citation_of_its_opening_words(tmp_path):
    """S3: the cited text equals the heading, or begins it with the next
    character neither a letter nor a digit."""
    cited = ["*2b*", "*2b. Settle*", "*2*", "*2b. Settl*"]
    root = repo(
        tmp_path,
        {
            "a.md": "".join(f"`manual/b.md` {c}\n\n" for c in cited),
            "manual/b.md": "## 2b. Settle what earlier releases left behind\n",
        },
    )
    found = citations(root)
    assert found.read == 4
    assert [c for *_, c in found.dangling] == ["*2*", "*2b. Settl*"]


LEADS = """**First line lead.** It opens the file.

# B

**Commit before you mutate, and restore.** The rest of the rule.

A paragraph whose second line
**Mid paragraph.** is no lead.

- **Clean up only what you started.** The item.
- **A lead that wraps
  across two lines.** The item.

**An unclosed lead

whose paragraph ended.** Text.

```text

**Fenced lead.** An example.

## Fenced heading
```
"""


def test_a_bold_rule_lead_resolves_outside_a_fence_and_case_for_case(tmp_path):
    """S4: a paragraph or list item opening with a bold lead is a section a
    citation can name, in its own case, and not inside a fenced block. A
    bold run in a paragraph's later line, or one its paragraph never closes,
    is no lead."""
    cited = [
        "*First line lead*",
        "*Commit before you mutate*",
        "*commit before you mutate*",
        "*Mid paragraph*",
        "*Clean up only what you started*",
        "*A lead that wraps across two lines*",
        "*An unclosed lead*",
        "*Fenced lead*",
        "*Fenced heading*",
    ]
    root = repo(
        tmp_path,
        {
            "a.md": "".join(f"`manual/b.md` {c}\n\n" for c in cited),
            "manual/b.md": LEADS,
        },
    )
    found = citations(root)
    assert found.read == 9
    assert [c for *_, c in found.dangling] == [
        "*commit before you mutate*",
        "*Mid paragraph*",
        "*An unclosed lead*",
        "*Fenced lead*",
        "*Fenced heading*",
    ]


SPELLINGS = """`manual/b.md`'s *Gone one*

`drafting` *Gone two*

the `drafting` skill's *Gone three*

`manual/b.md`'s *Here*, `drafting` *Here*, the `drafting` skill's *Here*.

A wrapped `manual/b.md` *Gone
four* here.

`unlisted` *Gone five*

`manual/b.md` *Fixed in
#120 here*

`manual/b.md` *Says "yes"
"no" twice*
"""


def test_each_spelling_of_a_citation_is_read(tmp_path):
    """S5: the possessive, a skill's name and the skill's possessive are
    read, a name only where `skills/<name>/SKILL.md` is tracked, and a
    citation wrapped across a line is named at the line it starts on. A
    markdown file is read as written: a line opening with `#` keeps it, and
    a quote ending one line meets the next line's quote."""
    root = repo(
        tmp_path,
        {
            "a.md": SPELLINGS,
            "manual/b.md": (
                '## Here\n\n## Fixed in #120 here\n\n## Says "yes" "no" twice\n'
            ),
            "skills/drafting/SKILL.md": "## Here\n",
        },
    )
    found = citations(root)
    assert found.read == 9
    assert found.dangling == [
        ("a.md", 1, "manual/b.md", "*Gone one*"),
        ("a.md", 3, "skills/drafting/SKILL.md", "*Gone two*"),
        ("a.md", 5, "skills/drafting/SKILL.md", "*Gone three*"),
        ("a.md", 9, "manual/b.md", "*Gone four*"),
    ]


PYTHON = """# A comment that cites `manual/b.md`
# *Gone in a comment* across two lines.
WHY = (
    "a literal that cites `manual/b.md` "
    "*Gone in literals* across two"
)
NAMED = f"`manual/b.md` *{WHY}*"
HELD = "`manual/b.md` *Here*"
"""


def test_a_citation_in_python_is_read_across_comments_and_literals(tmp_path):
    """S6: `#` comment markers are dropped and adjacent string literals are
    joined, and a cited text holding a placeholder is not read."""
    root = repo(tmp_path, {"b.py": PYTHON, "manual/b.md": "## Here\n"})
    found = citations(root)
    assert found.read == 3
    assert found.dangling == [
        ("b.py", 1, "manual/b.md", "*Gone in a comment*"),
        ("b.py", 4, "manual/b.md", "*Gone in literals*"),
    ]


ELSEWHERE = """`frame/design.md` *Scope*

`plan.md` *Alternatives considered*

`code.claude.com/docs/hooks.md` *Hook input*

`f6ae6db6:manual/b.md` *Gone*

`manual/none.md` *Anything*

`manual/loose.md` *Here*
"""


def test_a_path_outside_the_repository_is_not_read_and_a_missing_file_is(
    tmp_path,
):
    """S7: a path whose first segment no tracked entry has, and a
    `<commit>:<path>`, are not read; a path under a tracked entry that names
    no tracked file is dangling, though the file stands on disk untracked."""
    root = repo(tmp_path, {"a.md": ELSEWHERE, "manual/b.md": "## Here\n"})
    pathlib.Path(root, "manual", "loose.md").write_text("## Here\n", encoding="utf-8")
    assert citations(root) == Found(
        2,
        [
            ("a.md", 9, "manual/none.md", "*Anything*"),
            ("a.md", 11, "manual/loose.md", "*Here*"),
        ],
    )


@pytest.mark.parametrize("record", RECORDS)
def test_a_record_is_not_read(tmp_path, record):
    """S8: a file under a prefix of `tests/censuses.py#RECORDS` keeps what it
    said when it was written, so its citations are not read."""
    rel = record if record.endswith(".md") else record + "x.md"
    root = repo(
        tmp_path,
        {
            rel: "`manual/b.md` *Gone*\n",
            "a.md": "`manual/b.md` *Here*\n",
            "manual/b.md": "## Here\n",
        },
    )
    assert citations(root) == Found(1, [])
