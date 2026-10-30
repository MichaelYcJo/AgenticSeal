"""A build phase had no committed record, and what it discovered reached the
next phase only if the orchestrator retyped it into the next spawn prompt.

Issue #107 is the worked failure: phase 4 of an earlier work item moved a
rule out of `agents/crafter.md` into an interim home, and phase 5 removed that
interim home before the rule had actually reached anywhere else — the rule
left the repository with nothing recording that it had gone missing. #121
is the broader version: a phase's discoveries have no durable home at all,
so they live only in a transcript the next phase's session never opens.

`templates/records/sdd-phase.md` gives the build side the same committed,
per-segment record the review chain already has in `templates/records/sdd-round.md`
(`docs/the-review-record.md` *The round record*). This module pins:

  one section        the title and `## What this phase found`, with a
                     placeholder rather than a filled claim. The field
                     table copied the file name and `plan.md`'s Status
                     cell, and `## What this phase was asked` copied the
                     plan's Delivers cell, so both left with #1148
  no removal table    what a work item takes out of the tree is named once,
                     in `frame/design.md`'s `## Removes`, which the review reads
                     (#835); a per-phase table was a second record of the
                     same fact that nothing read
  the measured story  `skills/implement/SKILL.md`, which the record's writer
                     opens, names the failure each section answers, so the
                     template does not ship a blank nobody can trace back to
                     a reason; the template itself carries no comment (#1005)

The placeholder check mirrors
`test_the_fixes_name_their_surface.py::test_the_template_rows_are_rows_a_session_can_copy`,
reading through the same `readable` `chain_check.py` itself loads, which
blanks fenced lines and keeps no comment state, because a record carries no
comment (#1012).
"""

import importlib.util
import os

import pytest
from conftest import ROOT, read

PHASE_TEMPLATE = os.path.join(ROOT, "templates", "records", "sdd-phase.md")
CRAFTER_AGENT = os.path.join(ROOT, "agents", "crafter.md")
IMPLEMENT_SKILL = os.path.join(ROOT, "skills", "implement", "SKILL.md")

SPEC_TEMPLATE = os.path.join(ROOT, "templates", "records", "sdd-design.md")
FRAMER_AGENT = os.path.join(ROOT, "agents", "framer.md")
REMOVES_RULE = os.path.join(ROOT, "docs", "the-reader-registry.md")


def reader_module():
    """`unverified_check.py`, whose `readable` is the same reader
    `chain_check.py` loads for `trail/rounds/round-N.md`. A second implementation
    here would be free to drift from what actually reads these records."""
    spec = importlib.util.spec_from_file_location(
        "agentic_phase_reader_for_tests",
        os.path.join(ROOT, "skills", "verify", "scripts", "unverified_check.py"),
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def template_lines():
    return reader_module().readable(read(PHASE_TEMPLATE))


def section_body(lines, heading):
    """The non-blank lines between `heading` and the next `## ` heading (or
    end of file), from lines already run through `readable`."""
    start = None
    for i, line in enumerate(lines):
        if line.strip() == heading:
            start = i + 1
            break
    assert start is not None, f"heading not found: {heading}"
    body = []
    for line in lines[start:]:
        if line.strip().startswith("## "):
            break
        if line.strip():
            body.append(line)
    return body


# --- the template is its title and one section -------------------------------


def test_the_template_is_its_title_and_the_found_section():
    """#1148. Every other line the template carried copied another record:
    the field table the file name and `plan.md`'s Status cell, the asked
    section the plan's Delivers cell."""
    lines = [line.strip() for line in template_lines() if line.strip()]
    assert lines[0] == "# Phase <N>: <work-item-id>", lines[0]
    headings = [line for line in lines if line.startswith("## ")]
    assert headings == ["## What this phase found"], headings
    assert not [line for line in lines if line.startswith("|")], (
        "the template still carries a table, and every cell it could hold "
        "copies the file name or the plan's Status cell"
    )


def test_the_found_section_ships_a_placeholder():
    body = section_body(template_lines(), "## What this phase found")
    assert body, "`## What this phase found` has no content"
    text = " ".join(line.strip() for line in body)
    assert text.startswith("<") and text.endswith(">"), (
        f"`## What this phase found` ships `{text}` — a template must offer a "
        "placeholder, not a filled-in claim"
    )


def test_a_phase_record_carries_no_removal_table():
    """S8 of #835. A removal is named once, at the frame; a phase record
    carrying a second table for it is two records of one fact."""
    raw = read(PHASE_TEMPLATE)
    assert "## What this phase removes" not in raw
    assert "Removed item" not in raw
    skill = " ".join(read(IMPLEMENT_SKILL).split())
    assert "never what the work removes, which the frame's `## Removes` names once" in (
        skill
    ), "the skill's phase row does not say where a removal is recorded"
    rule = " ".join(read(REMOVES_RULE).split())
    assert "frame did not name is a divergence, and it goes to `gaps.md`" in rule


def test_the_spec_template_carries_the_removes_section_above_the_mark():
    """S8 of #835. The section ships with the three-column table and a
    placeholder row, and the framer's mark is still the last line."""
    raw = read(SPEC_TEMPLATE)
    lines = reader_module().readable(raw)
    body = section_body(lines, "## Removes")
    rows = [line.strip() for line in body if line.strip().startswith("|")]
    assert rows[0] == "| Removes | Coordinate | Where it lands, or why it can go |"
    assert len(rows) == 3, rows
    cells = [c.strip() for c in rows[2].strip("|").split("|")]
    assert all(c.startswith("<") and c.endswith(">") for c in cells), cells
    assert raw.index("## Removes") < raw.index("Framed <date> by <who>")
    assert raw.rstrip("\n").splitlines()[-1] == (
        "Framed <date> by <who>, before the build."
    )
    rule = " ".join(read(REMOVES_RULE).split())
    assert "removing nothing writes the no-change block" in rule
    assert "`nothing — <why>`" not in rule


def test_the_spec_template_carries_the_rule_changes_section_above_removes():
    """#953. The section ships empty, above `## Removes`, and the framer, who
    fills it, is pointed at the one statement of its grammar."""
    raw = read(SPEC_TEMPLATE)
    lines = reader_module().readable(raw)
    assert section_body(lines, "## Rule changes") == []
    assert raw.index("## Rule changes") < raw.index("## Removes")
    framer = " ".join(read(FRAMER_AGENT).split())
    assert "`skills/settle/SKILL.md` *Rule changes*" in framer
    assert (
        "## Rule changes"
        in read(os.path.join(ROOT, "skills", "settle", "SKILL.md")).splitlines()
    )


def test_the_framer_is_told_it_writes_the_removes_section():
    """S8 of #835. The framer's writes and its report name the section,
    because a frame that does not know it owes one ships without it."""
    flat = " ".join(read(FRAMER_AGENT).split())
    assert "what the work removes (`## Removes`)" in flat
    assert "What the frame says the work removes" in flat


# --- each section names the measured failure it answers ---------------------


def test_each_record_section_states_the_failure_it_prevents():
    """What goes wrong without each section is said where the record's writer
    reads it, as a property of the record rather than as the issue that first
    measured it (#940); since #1005 the template carries no comment, so the
    skill and the framer's definition say it."""
    skill = " ".join(read(IMPLEMENT_SKILL).split())
    assert "goes missing without a trace" in skill, (
        "the found section no longer says a discovery the orchestrator does "
        "not retype is lost"
    )
    framer = " ".join(read(FRAMER_AGENT).split())
    assert "reaches the reader only as a divergence after the fact" in framer, (
        "the framer is no longer told why a removal is recorded"
    )


# --- phase 2: crafter is told to write the record, and where ------------------
#
# `agents/crafter.md` is read by every spawn, so the instruction to write
# `trail/phases/phase-N.md` at each phase's close belongs there, and the skill's
# file-set table names the path and the template beside it.


def test_crafter_is_told_to_write_the_phase_record():
    crafter = read(CRAFTER_AGENT)
    assert "trail/phases/phase-N.md" in crafter, (
        "agents/crafter.md does not name `trail/phases/phase-N.md` — a spawned "
        "crafter has no instruction pointing it at the file to write"
    )
    assert "templates/records/sdd-phase.md" in crafter, (
        "agents/crafter.md does not name the template a phase record starts from"
    )
    assert "Each phase closes with its record" in crafter, (
        "agents/crafter.md does not say WHEN to write the record — a "
        "session that finds the file but not the timing writes it late or "
        "never"
    )
    rule = " ".join(
        crafter.split("**Each phase closes with its record.**", 1)[1]
        .split("\n\n", 1)[0]
        .split()
    )
    assert "every departure from the frame" in rule, rule
    assert "a removal the frame's `## Removes` did not name among them" in rule, rule
    assert "`gaps.md`" not in rule, (
        "the crafter's rule still sends a departure to `gaps.md`, whose "
        "divergence table left with #1148"
    )


# --- phase 2: the skill carries the file-set row and the copy instruction ---


def test_skill_file_set_table_carries_the_phase_row():
    skill = read(IMPLEMENT_SKILL)
    assert "trail/phases/phase-N.md" in skill, (
        "skills/implement/SKILL.md's SDD file-set table has no `trail/phases/phase-N.md` row"
    )
    assert "templates/records/sdd-phase.md" in skill, (
        "skills/implement/SKILL.md does not name the template the "
        "`trail/phases/phase-N.md` row starts from"
    )


def test_the_skill_says_the_record_copies_neither_the_ask_nor_the_commit():
    """#1148. What the phase was asked is the plan's Delivers cell, and a
    scope a spawn adds is a fold into the plan before the spawn, so the skill
    names the one section and says where the ask and the commit stand."""
    skill = " ".join(read(IMPLEMENT_SKILL).split())
    assert "What this phase was asked" not in skill, (
        "skills/implement/SKILL.md still names the asked section"
    )
    assert (
        "`trail/phases/phase-N.md` holds one section, `## What this phase found`"
        in (skill)
    )
    assert "every departure from the frame" in skill
    assert "folds into the plan before the spawn" in skill


# --- phase 2: carrier consistency ---------------------------------------------
#
# The files that point at the record from prose have to name its path the
# same way for a reader to find it by grepping any one of them: the
# bracket-free form the file is created with, `phase-N.md`, matching how they
# write `round-N.md` for the sibling record.

PROSE_CARRIERS = (
    ("agents", "crafter.md"),
    ("skills", "implement", "SKILL.md"),
)


@pytest.mark.parametrize("parts", PROSE_CARRIERS)
def test_the_phase_record_path_is_spelled_the_same_in_every_prose_carrier(parts):
    text = read(os.path.join(ROOT, *parts))
    assert "trail/phases/phase-N.md" in text, "/".join(parts)
