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

from conftest import read

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

# The section that holds the three rules for text an agent or a check reads,
# under `## 구성 규칙`, and the `check:` line each of the three ends with.
WRITING_RULES = "### 에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다"
WRITING_RULE_CHECKS = (
    "check: tests/test_rules.py"
    " tests/test_rule_changes.py"
    " tests/test_censuses.py"
    " tests/test_the_agent_contract_holds_the_universal_rules.py",
    "check: tests/test_one_word_one_meaning.py",
    "check: none reader: the warden at review",
)


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


def section(lines, heading, level):
    """The lines under HEADING up to the next heading of LEVEL or higher."""
    i = lines.index(heading) + 1
    out = []
    while i < len(lines):
        mark = lines[i].split(" ", 1)[0]
        if mark and set(mark) == {"#"} and len(mark) <= level:
            break
        out.append(lines[i])
        i += 1
    return out


def test_the_rules_for_text_an_agent_or_a_check_reads_reach_both_languages():
    """The three writing rules for text an agent or a check reads stand in
    one section under `## 구성 규칙`, each ending with its `check:` line, and
    a writer who opens either language section alone is pointed at it.

    An agent opens one language section by range, so a rule under
    `## 구성 규칙` reaches it only through the line naming the section; and
    the skill loads by its description, so the description names this kind
    of text among its uses (S16 of `1792540458-on-demand-files-state-the-current-rule`).
    """
    text = read(SKILL)
    lines = text.split("\n")
    structure = next(h for h in headings(text) if h.startswith("## 구성 규칙"))
    assert WRITING_RULES in section(lines, structure, 2), (
        f"{SKILL}: {WRITING_RULES!r} does not stand under {structure!r}"
    )
    body = [line.strip() for line in section(lines, WRITING_RULES, 3)]
    checks = tuple(line for line in body if line.startswith("check: "))
    assert checks == WRITING_RULE_CHECKS, (
        f"{SKILL} {WRITING_RULES}: its check lines read {checks}, and the "
        f"three rules end with {WRITING_RULE_CHECKS}"
    )
    title = WRITING_RULES[len("### ") :]
    for heading in LANGUAGE_SECTIONS:
        named = " ".join(section(lines, heading, 2))
        assert f"*{title}*" in named, (
            f"{SKILL} {heading}: nothing in it names *{title}*, so a writer "
            "who opened this section alone never reaches the three rules"
        )
    # The orchestrator writes a spawn prompt, which an agent reads, and opens
    # no language section to write it: the spawn step is where it is pointed.
    spawn = read("skills/implement/orchestration.md")
    spawn = spawn.split("### The plan is approved at the spawn", 1)[-1]
    spawn = " ".join(spawn.split("\n## ", 1)[0].split())
    assert f"`{SKILL}` *{title}*" in spawn, (
        "the orchestrator's spawn step does not name the writing rules, so the "
        "one party that writes a spawn prompt is never pointed at them"
    )
    # A session in this repository writes skills, agents, templates and
    # frames as its first act and opens no writing skill before it, so
    # `CLAUDE.md` names the section; the shipped block does not, because in a
    # consuming repository each party's own file points it there.
    claude = " ".join(read("CLAUDE.md").split())
    assert f"`{SKILL}` *{title}*" in claude, (
        "CLAUDE.md does not name the writing rules, so a session here writes "
        "a skill before anything points it at them"
    )
    assert title not in " ".join(read("templates/claude-md-block.md").split()), (
        "the shipped block carries a line for the writing rules"
    )
    head = " ".join(text.split("\n---\n", 1)[0].split())
    assert "text an agent or a check reads" in head, (
        f"{SKILL}'s description does not name text an agent or a check reads "
        "among its uses, so the skill is not loaded to write one"
    )
