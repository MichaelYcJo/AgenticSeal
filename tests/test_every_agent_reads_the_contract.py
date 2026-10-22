"""Every agent definition has one shape and preloads the contract alone.

`spec.md` *The shape of a definition* of #957: frontmatter whose `skills:`
list is `agent-contract` and nothing else, one opening sentence naming the
contract, identical in every definition, then `## Job`, `## Order of work`,
`## Never` and `## Rules`, in that order. Every other skill is opened at the
step that needs it, by its path, so a path a definition names has to be a
file in the tree.

The checks glob `agents/*.md` rather than naming the five, so a sixth
definition arriving in another shape is red on the day it lands. Every
definition is written in that shape, so the shape case skips none, and its
`skills:` check is what holds each definition to preloading the contract
alone.
"""

import glob
import os
import re

import pytest
from conftest import read
from conftest import repo_relative as name

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

AGENTS = sorted(glob.glob(os.path.join(ROOT, "agents", "*.md")))

CONTRACT = "skills/agent-contract/SKILL.md"
SENTENCE = f"`{CONTRACT}` binds you, and it arrived before your first tool call."
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
    if skills != ["agent-contract"]:
        problems.append(f"`skills:` lists {skills}, not `agent-contract` alone")
    opening = opening_paragraph(body)
    if opening != SENTENCE:
        problems.append(f"the opening paragraph is {opening!r}, not the sentence")
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
    with open(os.path.join(ROOT, CONTRACT), encoding="utf-8") as handle:
        assert "## 1 " in handle.read(), f"{CONTRACT} carries no numbered rules"


# --- the shape ---------------------------------------------------------------


@pytest.mark.parametrize("path", AGENTS, ids=name)
def test_every_definition_has_the_shape_and_preloads_the_contract_alone(path):
    """A definition preloads `agent-contract` alone, opens with the one
    sentence and carries the four sections in order (S1).

    It catches a second skill creeping back into a `skills:` list, which no
    eval sees while the output is right, and a section lost or added in a
    later edit; no other case reads a definition's frontmatter or headings.
    With no definition skipped, it is also what keeps a definition that
    drops `agent-contract` red (#957 round 1, finding 3)."""
    assert shape_problems(read(path)) == [], name(path)


@pytest.mark.parametrize("path", AGENTS, ids=name)
def test_every_file_a_step_names_exists(path):
    """Every `skills/`, `templates/`, `docs/` or `agents/` path a definition
    names is a file or directory in the tree (S2).

    A step opens a skill by its path, so a renamed skill leaves an
    instruction an agent meets as *file not found* mid-run; `rules --check`
    reads only `check:` targets, and no other case reads the paths a
    step names."""
    assert missing_paths(read(path)) == [], name(path)


# The ways a definition is allowed to close its own list of durable writes.
# Under contract rule 6 a definition's named writes are its permission, so
# every definition says where that list stops, and each phrase names WRITING
# as its subject so only a sentence about what the agent writes can match it.
BOUNDS = (
    "a write not below is a write you do not make",
    "a write not named here is a write you do not make",
    "is the whole of what you may write",
    "You write nothing durable anywhere, and that is the whole of it",
)


@pytest.mark.parametrize("path", AGENTS, ids=name)
def test_every_definition_bounds_what_it_writes(path):
    """A definition that names writes and never says where the list stops
    reads its own examples as a floor, and under contract rule 6 every sentence about
    producing something becomes a grant."""
    text = " ".join(read(path).split())
    assert any(bound in text for bound in BOUNDS), (
        f"{name(path)} never says where its list of durable writes stops"
    )


# --- the check can fail ----------------------------------------------------


GOOD = f"""---
name: sixth
description: |
  A sixth agent.
skills:
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
check: none reader: a planted definition
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
        "skills:\n  - agent-contract\n", "skills: [agent-contract, implement]\n"
    )
    assert any("`skills:`" in p for p in shape_problems(inline))


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
    wrapped = GOOD.replace(SENTENCE, SENTENCE.replace(" binds", "\nbinds"))
    assert any("opening paragraph" in p for p in shape_problems(wrapped))


def test_a_path_that_does_not_resolve_is_caught():
    for path in ("skills/code-reviews/SKILL.md", "docs/no-such-document.md"):
        broken = GOOD.replace("skills/code-review/SKILL.md", path)
        assert missing_paths(broken) == [path]
