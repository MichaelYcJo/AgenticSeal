"""Every agent definition has one shape and preloads the core, then the contract.

`frame/design.md` *The shape of a definition* of #957: frontmatter whose `skills:`
list is fixed, one opening paragraph naming the two files it preloads, then
`## Job`, `## Order of work`, `## Never` and `## Rules`, in that order. The
opening's words, and whether every definition words it alike, are the
proofer's to read. #1177 made the list `core` then `agent-contract`,
values before rules, so every agent receives `skills/core/SKILL.md` as well.
Every other skill is opened at the step that needs it, by its path, so a
path a definition names has to be a file in the tree.

The checks glob `agents/*.md` rather than naming the five, so a sixth
definition arriving in another shape is red on the day it lands. Every
definition is written in that shape, so the shape case skips none, and its
`skills:` check is what holds each definition to preloading the core and the
contract and nothing else.

#1475 deleted the `check:` lines of every file a spawn preloads, each
definition and each skill a `skills:` list names, because every spawn paid
for them and no agent acts on one. The preload case reads each such file
through `.github/scripts/rules.py#check_lines`, the grammar's one reader, so
a line written back into one is red here, while `seal rules --check` would
resolve it and pass.
"""

import glob
import os
import re

import pytest
from conftest import ROOT, load, read
from conftest import repo_relative as name

# No TARGET: its cases walk every definition under agents/ and each skill their skills: lists preload.

AGENTS = sorted(glob.glob(os.path.join(ROOT, "agents", "*.md")))
rules = load(".github/scripts/rules.py", "agentic_rules_for_the_preloads")

CORE = "skills/core/SKILL.md"
CONTRACT = "skills/agent-contract/SKILL.md"
# The `skills:` entries the harness preloads, in order.
PRELOADS = ["core", "agent-contract"]
# The opening sentence of the planted definition below. A definition's own
# opening paragraph is held to the two paths it names, which an agent opens;
# its words are the proofer's to read.
SENTENCE = (
    f"`{CORE}` and `{CONTRACT}` bind you, and both\n"
    "arrived before your first tool call."
)
# The headings a definition carries, which its own steps and the other
# definitions cite in italics.
SECTIONS = ("## Job", "## Order of work", "## Never", "## Rules")

# A backticked path into the plugin's own tree. A placeholder (`<…>`), a glob,
# a `path::name` target and a `path#anchor` are not paths and are not read.
PLUGIN_PATH = re.compile(r"`((?:skills|templates|docs|agents)/[A-Za-z0-9._/-]*)`")


def split(text):
    """`(frontmatter, body)`, or `(None, text)` where none opens the file."""
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return (m.group(1), text[m.end() :]) if m else (None, text)


def listed_skills(head):
    """The `skills:` entries the harness preloads, in order."""
    block = re.search(r"^skills:[ \t]*\n((?:[ \t]+- .*\n?)+)", head + "\n", re.M)
    inline = re.search(r"^skills:[ \t]*\[(.*)\][ \t]*$", head, re.M)
    if block:
        return re.findall(r"- (\S+)", block.group(1))
    if inline:
        return [s.strip() for s in inline.group(1).split(",") if s.strip()]
    return []


def opening_paragraph(body):
    """The first paragraph under the `# <name>` heading, and only that."""
    heading = re.search(r"^# \S.*$", body, re.M)
    if not heading:
        return None
    return body[heading.end() :].strip("\n").split("\n\n", 1)[0]


def shape_problems(text):
    """Every way TEXT departs from the shape, each as a sentence."""
    head, body = split(text)
    if head is None:
        return ["no frontmatter"]
    problems = []
    skills = listed_skills(head)
    if skills != PRELOADS:
        problems.append(f"`skills:` lists {skills}, not {PRELOADS}")
    opening = opening_paragraph(body) or ""
    if f"`{CORE}`" not in opening or f"`{CONTRACT}`" not in opening:
        problems.append(
            f"the opening paragraph is {opening!r}, which does not name "
            f"`{CORE}` and `{CONTRACT}`"
        )
    headings = tuple(re.findall(r"^## .*$", body, re.M))
    if headings != SECTIONS:
        problems.append(f"the `## ` headings are {headings}, not {SECTIONS}")
    return problems


def missing_paths(text):
    """Every backticked plugin path TEXT names that is not in the tree."""
    return [
        p
        for p in PLUGIN_PATH.findall(text)
        if not os.path.exists(os.path.join(ROOT, p))
    ]


# --- there is something to check -------------------------------------------


def test_the_glob_finds_the_definitions():
    """A glob that matches nothing passes every case parametrised on it."""
    assert len(AGENTS) >= 5, f"agents/*.md matched {len(AGENTS)} files"


def test_the_sentence_names_the_contract():
    """The sentence names a file that is the contract, so a sentence pointing
    at another skill that happens to exist is red here rather than nowhere."""
    with open(os.path.join(ROOT, *CONTRACT.split("/")), encoding="utf-8") as handle:
        # The numbered heading a `contract rule <N>` citation resolves to.
        assert "## 1 " in handle.read(), f"{CONTRACT} carries no numbered rules"


def test_the_sentence_names_the_core():
    """The sentence's first path is the core, by the two sections every
    citation of it names, so a sentence pointing at a file that is not the
    core is red here."""
    with open(os.path.join(ROOT, *CORE.split("/")), encoding="utf-8") as handle:
        text = handle.read()
    for heading in (
        # The two headings every citation of the core names, which a reader
        # of such a citation resolves.
        "## The first value: efficient development through the workflow",
        "## The rule a mechanism is kept against",
    ):
        assert heading in text.splitlines(), f"{CORE} has no `{heading}`"


# --- the shape ---------------------------------------------------------------


@pytest.mark.parametrize("path", AGENTS, ids=name)
def test_every_definition_has_the_shape_and_preloads_the_core_and_the_contract(path):
    """A definition preloads `core` then `agent-contract` and nothing else,
    opens with the one sentence and carries the four sections in order (S1).

    It catches a third skill creeping into a `skills:` list, which no eval
    sees while the output is right, and a section lost or added in a later
    edit; no other case reads a definition's frontmatter or headings. With no
    definition skipped, it is also what keeps a definition that drops
    `agent-contract` (#957 round 1, finding 3) or `core` (#1177 S1) red."""
    assert shape_problems(read(path)) == [], name(path)


@pytest.mark.parametrize("path", AGENTS, ids=name)
def test_every_file_a_step_names_exists(path):
    """Every `skills/`, `templates/`, `docs/` or `agents/` path a definition
    names is a file or directory in the tree (S2).

    A step opens a skill by its path, so a renamed skill leaves an
    instruction an agent meets as *file not found* mid-run; `seal rules --check`
    reads only `check:` targets, and no other case reads the paths a
    step names."""
    assert missing_paths(read(path)) == [], name(path)


# --- what a preload carries --------------------------------------------------


def preloaded():
    """Every file a spawn preloads: each definition, then each skill any
    definition's `skills:` list names, as `skills/<name>/SKILL.md`, once."""
    skills = []
    for path in AGENTS:
        head, _ = split(read(path))
        for skill in listed_skills(head or ""):
            skill_path = os.path.join(ROOT, "skills", skill, "SKILL.md")
            if skill_path not in skills:
                skills.append(skill_path)
    return AGENTS + skills


@pytest.mark.parametrize("path", preloaded(), ids=name)
def test_a_file_every_spawn_preloads_carries_no_check_line(path):
    """`skills/settle/rule-changes.md` *A rule has one shape*: a file every
    spawn preloads carries no check line (#1475). The set is derived from
    the definitions, so a skill added to a `skills:` list is read here
    without an edit to this case."""
    found = rules.check_lines(read(path))
    # `skills/settle/rule-changes.md` *A rule has one shape*: a `check:`
    # line, which `seal rules` reads and every spawn that preloads the file
    # pays for.
    assert found == [], (
        f"{name(path)} carries a check line at "
        + ", ".join(f"line {number} (`{line}`)" for number, _heading, line in found)
        + ", and a file every spawn preloads carries none "
        "(`skills/settle/rule-changes.md` *A rule has one shape*)"
    )


# --- the check can fail ----------------------------------------------------


GOOD = f"""---
name: sixth
description: |
  A sixth agent.
skills:
  - core
  - agent-contract
---

# sixth

{SENTENCE}

## Job

It does a sixth thing; a write not named here is a write you do not make.

## Order of work

1. Open `skills/code-review/SKILL.md` and follow it.

## Never

- Push.

## Rules

**A rule.** It holds.
"""


def test_the_planted_definition_has_the_shape():
    """The cases below break one thing each, so the one they start from has
    to pass, or a break that changes nothing would read as caught."""
    assert shape_problems(GOOD) == []
    assert missing_paths(GOOD) == []


def test_a_second_preload_is_caught():
    broken = GOOD.replace(
        "  - agent-contract\n", "  - agent-contract\n  - code-review\n"
    )
    assert broken != GOOD
    assert any("`skills:`" in p for p in shape_problems(broken))
    inline = GOOD.replace(
        "skills:\n  - core\n  - agent-contract\n",
        "skills: [core, agent-contract, implement]\n",
    )
    assert inline != GOOD
    assert any("`skills:`" in p for p in shape_problems(inline))


def test_a_dropped_or_reordered_core_is_caught():
    """The core is the value every rule after it is weighed by, so a list
    without it, or with it after the contract, is caught."""
    dropped = GOOD.replace("  - core\n", "")
    assert dropped != GOOD
    assert any("`skills:`" in p for p in shape_problems(dropped))
    swapped = GOOD.replace(
        "  - core\n  - agent-contract\n", "  - agent-contract\n  - core\n"
    )
    assert swapped != GOOD
    assert any("`skills:`" in p for p in shape_problems(swapped))


def test_a_missing_or_extra_section_is_caught():
    gone = GOOD.replace("## Order of work\n", "")
    assert any("headings" in p for p in shape_problems(gone))
    extra = GOOD + "\n## Report\n\nMore.\n"
    assert any("headings" in p for p in shape_problems(extra))
    swapped = GOOD.replace("## Never", "## Tmp").replace("## Job", "## Never")
    assert any("headings" in p for p in shape_problems(swapped))


def test_a_sentence_anywhere_but_the_opening_is_caught():
    moved = GOOD.replace(f"{SENTENCE}\n\n", "", 1) + f"\n{SENTENCE}\n"
    assert SENTENCE in moved
    assert any("opening paragraph" in p for p in shape_problems(moved))


def test_a_path_that_does_not_resolve_is_caught():
    for path in ("skills/code-reviews/SKILL.md", "docs/no-such-document.md"):
        broken = GOOD.replace("skills/code-review/SKILL.md", path)
        assert missing_paths(broken) == [path]
