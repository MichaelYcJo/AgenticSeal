"""Each language's rules in `writing-style` open alone, and say what else applies.

An agent no longer preloads `skills/writing-style/SKILL.md`: its record step
opens the section for the record's language, `## English prose rules` or
`## 문장 규칙`, and reads it by range. A writer who reads one section by range
misses the rules that apply in every language, so each of the two sections
opens with one line naming them: `## 먼저`, `## 구성 규칙`, and the
per-document section for the text being written. And a step that names a
heading by its spelling breaks silently when the heading is renamed, so every
heading an agent's `writing-style` step names must stand in the file (T7 and
S8 of `1792251842-the-smith-is-written-anew-from-its-job`).

The home is a module of its own rather than the payload meter's: nothing here
reads what the meter measures, only what an agent opening a section finds.
"""

import glob
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..")
SKILL = "skills/writing-style/SKILL.md"

# The two sections an agent opens alone, spelled as `agents/warden.md` and
# `agents/smith.md` name them.
LANGUAGE_SECTIONS = ("## 문장 규칙", "## English prose rules")

# What each section's first paragraph names: the two language-agnostic
# sections, and both homes of a per-document section.
ALSO_APPLIES = (
    "`## 먼저`",
    "`## 구성 규칙`",
    "`## 리뷰 코멘트에만 해당하는 것`",
    "`outside-the-review.md`",
)

HEADING_SPAN = re.compile(r"`(## [^`]+)`")


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def headings(text):
    return [line for line in text.split("\n") if line.startswith("## ")]


def first_paragraph(lines, heading):
    """The first paragraph under HEADING: the lines after it, past blank
    lines, up to the next blank line."""
    i = lines.index(heading) + 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    para = []
    while i < len(lines) and lines[i].strip():
        para.append(lines[i])
        i += 1
    return " ".join(para)


def named_by_agents():
    """Every `## …` span in an agent's list item or paragraph that names
    `writing-style`, keyed by the definition that names it."""
    named = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "agents", "*.md"))):
        rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
        blocks = re.split(r"\n\s*\n|\n(?=\d+\. )", read(rel))
        for block in blocks:
            if "writing-style" in block:
                for span in HEADING_SPAN.findall(" ".join(block.split())):
                    named.setdefault(rel, set()).add(span)
    return named


def test_each_language_section_of_writing_style_opens_alone():
    text = read(SKILL)
    lines = text.split("\n")
    present = headings(text)

    for heading in LANGUAGE_SECTIONS:
        assert heading in present, (
            f"{SKILL} lost the heading {heading!r}, which an agent's record "
            "step opens by that spelling"
        )
        para = first_paragraph(lines, heading)
        missing = [name for name in ALSO_APPLIES if name not in para]
        assert not missing, (
            f"{SKILL} {heading}: its first paragraph does not name {missing}, "
            "so a writer who opened this section alone misses rules that apply "
            f"to them. It reads: {para[:200]}"
        )
        for span in HEADING_SPAN.findall(para):
            assert any(h == span or h.startswith(span + " ") for h in present), (
                f"{SKILL} {heading}: its first paragraph points at {span!r}, "
                "a heading the file does not have"
            )

    named = named_by_agents()
    assert set(LANGUAGE_SECTIONS) <= named.get("agents/warden.md", set()), (
        "agents/warden.md's record step no longer names both language sections "
        f"by heading; it names {sorted(named.get('agents/warden.md', set()))}"
    )
    dangling = [
        f"{rel}: {span}"
        for rel, spans in sorted(named.items())
        for span in sorted(spans)
        if not any(h == span or h.startswith(span + " ") for h in present)
    ]
    assert not dangling, (
        f"an agent's writing-style step names a heading {SKILL} does not have:\n"
        + "\n".join(dangling)
    )
