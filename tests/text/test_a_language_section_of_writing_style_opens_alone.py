"""Each language's rules in `writing-style` open alone, and say what else applies.

An agent no longer preloads `skills/writing-style/SKILL.md`: its record step
opens the section for the record's language and reads it by range. Contract
rule 11 names the two sections, `## English prose rules` and `## 문장 규칙`,
and the framer's, the crafter's and the proofer's record steps cite rule 11
for them, each at its own number (#1579). A writer who reads one section by
range misses the rules that apply in every language, so each of the two
sections opens with one line naming them: `## 먼저`, `## 구성 규칙`, and the
per-document section for the text being written. And a text that names a
heading by its spelling breaks silently when the heading is renamed, so every
heading the contract or an agent's `writing-style` step names must stand in
the file (T7 and S8 of work item 1792251842, which wrote the crafter's
definition anew).

The home is a module of its own rather than the payload meter's: nothing here
reads what the meter measures, only what an agent opening a section finds.
"""

import glob
import os
import re

from conftest import ROOT, read
from test_the_agent_contract_holds_the_universal_rules import TARGET as CONTRACT
from test_the_agent_contract_holds_the_universal_rules import bodies

# No TARGET: its cases hold the language sections of skills/writing-style/SKILL.md against contract rule 11 and every definition under agents/ that names them.

SKILL = "skills/writing-style/SKILL.md"

# The two sections an agent opens alone, spelled as contract rule 11 names
# them.
LANGUAGE_SECTIONS = ("## 문장 규칙", "## English prose rules")

# The contract rule that names them, and the definitions whose record step
# cites it.
NAMING_RULE = 11
CITING_STEPS = ("agents/crafter.md", "agents/framer.md", "agents/proofer.md")

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
# under `## 구성 규칙`, and its one `check:` line, which the first rule ends
# with. The other two rules carry none.
WRITING_RULES = "### 에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다"
WRITING_RULE_CHECKS = (
    "check: tests/skills/test_rules.py"
    " tests/skills/test_chain_check.py"
    " tests/skills/test_rule_changes.py"
    " tests/test_censuses.py"
    " tests/text/test_the_agent_contract_holds_the_universal_rules.py"
    " tests/behaviour/test_a_cited_section_stands_in_its_file.py",
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


def writing_style_blocks(rel):
    """Each list item or paragraph of REL that names `writing-style`, its
    whitespace folded."""
    blocks = re.split(r"\n\s*\n|\n(?=\d+\. )", read(rel))
    return [" ".join(block.split()) for block in blocks if "writing-style" in block]


def named_by_readers():
    """Every `## …` span in a list item or paragraph that names
    `writing-style`, keyed by the file that names it: each definition under
    `agents/`, and the contract."""
    named = {}
    paths = sorted(glob.glob(os.path.join(ROOT, "agents", "*.md")))
    rels = [os.path.relpath(p, ROOT).replace(os.sep, "/") for p in paths]
    for rel in [*rels, CONTRACT]:
        for block in writing_style_blocks(rel):
            for span in HEADING_SPAN.findall(block):
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

    rule = " ".join(bodies(read(CONTRACT))[NAMING_RULE].split())
    in_rule = set(HEADING_SPAN.findall(rule))
    assert set(LANGUAGE_SECTIONS) <= in_rule, (
        f"contract rule {NAMING_RULE} no longer names both language sections by "
        f"heading; it names {sorted(in_rule)}"
    )
    uncited = [
        rel
        for rel in CITING_STEPS
        if not any(f"rule {NAMING_RULE}" in b for b in writing_style_blocks(rel))
    ]
    assert not uncited, (
        f"a record step that opens a writing-style section no longer cites rule "
        f"{NAMING_RULE}, which names the sections: {uncited}"
    )
    named = named_by_readers()
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
    """The section of the three writing rules for text an agent or a check
    reads holds its one `check:` line, and a writer who opens either
    language section alone, the orchestrator at its spawn step, and every
    session through the core are pointed at the section.

    An agent opens one language section by range, so a rule under
    `## 구성 규칙` reaches it only through the line naming the section (S16
    of `1792540458-on-demand-files-state-the-current-rule`).
    """
    text = read(SKILL)
    lines = text.split("\n")
    body = [line.strip() for line in section(lines, WRITING_RULES, 3)]
    checks = tuple(line for line in body if line.startswith("check: "))
    # The check lines `seal rules --check` reads, and the paths of the
    # modules each names, which a reader of the rules opens.
    assert checks == WRITING_RULE_CHECKS, (
        f"{SKILL} {WRITING_RULES}: its check lines read {checks}, and the "
        f"section holds {WRITING_RULE_CHECKS}"
    )
    title = WRITING_RULES[len("### ") :]
    for heading in LANGUAGE_SECTIONS:
        named = " ".join(section(lines, heading, 2))
        # The heading cited in italics, which a writer who opened this
        # section alone resolves to the three rules.
        assert f"*{title}*" in named, (
            f"{SKILL} {heading}: nothing in it names *{title}*, so a writer "
            "who opened this section alone never reaches the three rules"
        )
    # The orchestrator writes a spawn prompt, which an agent reads, and opens
    # no language section to write it: the spawn step is where it is pointed.
    spawn = read("skills/implement/orchestration.md")
    spawn = spawn.split("### The frame is read against the issue at the spawn", 1)[-1]
    spawn = " ".join(spawn.split("\n## ", 1)[0].split())
    # The citation the orchestrator resolves at its spawn step.
    assert f"`{SKILL}` *{title}*" in spawn, (
        "the orchestrator's spawn step does not name the writing rules, so the "
        "one party that writes a spawn prompt is never pointed at them"
    )
    # A session writes skills, agents, templates and frames as its first act
    # and opens no writing skill before it, so the core every agent and every
    # session in a repository with a `seal/` root reads names the section.
    core = " ".join(read("skills/core/SKILL.md").split())
    # The citation those sessions and agents resolve through the core.
    assert f"`{SKILL}` *{title}*" in core, (
        "the core does not name the writing rules, so a session writes a "
        "skill before anything points it at them"
    )
