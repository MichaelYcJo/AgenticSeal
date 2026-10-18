"""A build phase had no committed record, and what it discovered reached the
next phase only if the orchestrator retyped it into the next spawn prompt.

Issue #107 is the worked failure: phase 4 of an earlier work item moved a
rule out of `agents/smith.md` into an interim home, and phase 5 removed that
interim home before the rule had actually reached anywhere else — the rule
left the repository with nothing recording that it had gone missing. #121
is the broader version: a phase's discoveries have no durable home at all,
so they live only in a transcript the next phase's session never opens.

`templates/sdd-phase.md` gives the build side the same committed,
per-segment record the review chain already has in `templates/sdd-round.md`
(`docs/the-review-record.md` §*The round record*). This module pins:

  the field table    `Phase`, `Commit` — nothing more, because a phase has
                     no `Target SHA` to squash away
  the two sections    ship outside HTML comments, as placeholders rather
                     than filled claims — a template whose only mention of
                     a section is commented out ships a record that is
                     missing it the moment someone copies the file
  no removal table    what a work item takes out of the tree is named once,
                     in `spec.md`'s `## Removes`, which the review reads
                     (#835); a per-phase table was a second record of the
                     same fact that nothing read
  the measured story  each section's own comment names the failure it
                     answers, so the template does not ship a blank nobody
                     can trace back to a reason
  the plan's pointer  `templates/sdd-plan.md` names the path a phase record
                     lives at, so a session reading the plan can find the
                     template without guessing

The placeholder check mirrors
`test_the_fixes_name_their_surface.py::test_the_template_rows_are_rows_a_session_can_copy`,
reading through the same `strip_comments` `chain_check.py` itself loads —
counted outside comments, because a row whose only mention is commented out
is absent to any reader that strips comments first, template included.
"""

import importlib.util
import os

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PHASE_TEMPLATE = os.path.join(ROOT, "templates", "sdd-phase.md")
PLAN_TEMPLATE = os.path.join(ROOT, "templates", "sdd-plan.md")
SMITH_AGENT = os.path.join(ROOT, "agents", "smith.md")
IMPLEMENT_SKILL = os.path.join(ROOT, "skills", "implement", "SKILL.md")

SECTIONS = (
    "## What this phase was asked",
    "## What this phase found",
)
SPEC_TEMPLATE = os.path.join(ROOT, "templates", "sdd-spec.md")
FRAMER_AGENT = os.path.join(ROOT, "agents", "framer.md")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def reader_module():
    """`unverified_check.py`'s `strip_comments` — the same reader
    `chain_check.py` loads for `rounds/round-N.md`. A second implementation
    here would be free to drift from what actually reads these records."""
    spec = importlib.util.spec_from_file_location(
        "specseal_phase_reader_for_tests",
        os.path.join(ROOT, "skills", "verify", "scripts", "unverified_check.py"),
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def stripped_lines():
    return reader_module().strip_comments(read(PHASE_TEMPLATE).splitlines())


def section_body(lines, heading):
    """The non-blank lines between `heading` and the next `## ` heading (or
    end of file), from lines already run through `strip_comments`."""
    start = None
    for i, line in enumerate(lines):
        if line.strip() == heading:
            start = i + 1
            break
    assert start is not None, f"heading not found outside comments: {heading}"
    body = []
    for line in lines[start:]:
        if line.strip().startswith("## "):
            break
        if line.strip():
            body.append(line)
    return body


# --- the field table ---------------------------------------------------------


def test_the_field_table_is_phase_and_commit():
    lines = stripped_lines()
    header_idx = next(
        (i for i, line in enumerate(lines) if line.strip().startswith("| Field")), None
    )
    assert header_idx is not None, "no `| Field | Value |` header outside comments"
    # The field table ends at the first `## ` heading — rows past it belong
    # to the removal table further down, not to this one.
    end = next(
        (
            i
            for i in range(header_idx + 1, len(lines))
            if lines[i].strip().startswith("## ")
        ),
        len(lines),
    )
    table_lines = lines[header_idx + 1 : end]
    rows = [line.strip() for line in table_lines if line.strip().startswith("|")]
    field_rows = [
        line for line in rows if not set(line.replace("|", "").strip()) <= {"-"}
    ]
    names = [line.split("|")[1].strip() for line in field_rows]
    assert names == ["Phase", "Commit"], (
        f"the field table carries {names}, not Phase/Commit — a phase has no "
        "Target SHA to squash away, and `Ran by` left with the round record's "
        "in 0.22.0 (#923)"
    )
    for name, row in zip(names, field_rows, strict=True):
        value = row.split("|")[2].strip()
        assert value.startswith("<") and value.endswith(">"), (
            f"a template must not ship a claim, and `{value}` is one ({name})"
        )


# --- the two sections exist and ship placeholders, not claims ---------------


def test_both_sections_exist_outside_comments():
    lines = stripped_lines()
    present = {line.strip() for line in lines}
    for heading in SECTIONS:
        assert heading in present, (
            f"`{heading}` is missing outside HTML comments — a heading only "
            "a comment carries is a heading a copied file does not have"
        )


def test_asked_and_found_sections_ship_a_placeholder():
    lines = stripped_lines()
    for heading in ("## What this phase was asked", "## What this phase found"):
        body = section_body(lines, heading)
        assert body, f"`{heading}` has no content outside comments"
        text = " ".join(line.strip() for line in body)
        assert text.startswith("<") and text.endswith(">"), (
            f"`{heading}` ships `{text}` — a template must offer a "
            "placeholder, not a filled-in claim"
        )


def test_a_phase_record_carries_no_removal_table():
    """S8 of #835. A removal is named once, at the frame; a phase record
    carrying a second table for it is two records of one fact."""
    raw = read(PHASE_TEMPLATE)
    assert "## What this phase removes" not in raw
    assert "Removed item" not in raw
    flat = " ".join(raw.split())
    assert "`spec.md`'s `## Removes` section" in flat, (
        "the phase template does not say where a removal is recorded now"
    )
    assert "goes where divergences go: `overview.md`" in flat


def test_the_spec_template_carries_the_removes_section_above_the_mark():
    """S8 of #835. The section ships outside comments, with the three-column
    table and a placeholder row, and the framer's mark is still the last
    line."""
    raw = read(SPEC_TEMPLATE)
    lines = reader_module().strip_comments(raw.splitlines())
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
    assert "`nothing — <why>`" in " ".join(raw.split())


def test_the_framer_is_told_it_writes_the_removes_section():
    """S8 of #835. The framer's writes table and its report name the
    section, because a frame that does not know it owes one ships without
    it."""
    flat = " ".join(read(FRAMER_AGENT).split())
    assert "what the work removes (`## Removes`)" in flat
    assert "**What the frame says the work removes.**" in flat


# --- each section's comment names the measured failure it answers -----------


def test_each_section_comment_names_its_measured_failure():
    raw = read(PHASE_TEMPLATE)
    # Comments are read from the RAW file (not stripped) — this is checking
    # the comments exist and say what they must, not that they are absent.
    assert "#119" in raw, (
        "no `#119` anywhere in the template — the asked/found split answers "
        "that issue's finding that neither record said what it was told to do"
    )
    assert "#107" in raw and "#121" in raw, (
        "no `#107`/`#121` — the found section answers the dropped-rule "
        "failure those issues measured"
    )
    # The removal's worked #107 story moved with the removal, to the frame's
    # `## Removes` comment (#835), and it is the story, not the bare number.
    spec = read(SPEC_TEMPLATE)
    tail = spec[spec.index("## Removes") :]
    assert "#107" in tail and "agents/smith.md" in tail, (
        "the `## Removes` comment must carry the #107 worked example "
        "(a rule moved out of agents/smith.md and lost between phases)"
    )
    assert "lost between two phases" in " ".join(tail.split())


# --- the plan points at the path ---------------------------------------------


def test_plan_names_the_phase_record_path():
    plan = read(PLAN_TEMPLATE)
    assert "phases/phase-N.md" in plan, (
        "templates/sdd-plan.md does not name `phases/phase-N.md` — a "
        "session reading the plan has no way to find the phase-record path"
    )
    assert "templates/sdd-phase.md" in plan, (
        "templates/sdd-plan.md does not name the template a phase record starts from"
    )


# --- phase 2: smith is told to write the record, and where ------------------
#
# Phase 1 built the template with nothing pointing a spawned smith at it
# except `plan.md`'s own pointer sentence — which a session reads only if it
# opens `plan.md` at all. `agents/smith.md` phase 3 ("Implement") is read by
# every spawn regardless, so the instruction to write `phases/phase-N.md` at
# each phase's close belongs there, not only in the plan template.


def test_smith_is_told_to_write_the_phase_record():
    smith = read(SMITH_AGENT)
    assert "phases/phase-N.md" in smith, (
        "agents/smith.md does not name `phases/phase-N.md` — a spawned "
        "smith has no instruction pointing it at the file to write"
    )
    assert "templates/sdd-phase.md" in smith, (
        "agents/smith.md does not name the template a phase record starts from"
    )
    assert "Each phase closes with its record" in smith, (
        "agents/smith.md does not say WHEN to write the record — a "
        "session that finds the file but not the timing writes it late or "
        "never"
    )


# --- phase 2: the skill carries the file-set row and the copy instruction ---


def test_skill_file_set_table_carries_the_phase_row():
    skill = read(IMPLEMENT_SKILL)
    assert "phases/phase-N.md" in skill, (
        "skills/implement/SKILL.md's SDD file-set table has no `phases/phase-N.md` row"
    )
    assert "templates/sdd-phase.md" in skill, (
        "skills/implement/SKILL.md does not name the template the "
        "`phases/phase-N.md` row starts from"
    )


def test_skill_says_what_is_copied_into_what_this_phase_was_asked():
    skill = read(IMPLEMENT_SKILL)
    assert "What this phase was asked" in skill, (
        "skills/implement/SKILL.md never names the section the copied content lands in"
    )
    assert "boilerplate" in skill, (
        "skills/implement/SKILL.md does not say that the copied content "
        "excludes the boilerplate the contract, the skill, and "
        "agents/smith.md already carry — without that line, a session "
        "copies the whole spawn prompt in, including what every phase "
        "already gets told"
    )
    assert "agents/smith.md" in skill


# --- phase 2: carrier consistency ---------------------------------------------
#
# The four files phase 1 and 2 touch have to name the record path the same
# way for a reader to find it by grepping any one of them. A template's own
# self-description is one exception: `templates/sdd-phase.md` names its own
# path the way `templates/sdd-round.md` names its own — `round-<N>.md`, the
# angle bracket marking a template placeholder, matching every other
# `<...>` already in that file's path comment (`<unix-epoch-seconds>-<slug>`
# sits in the same sentence). Every file that instead POINTS AT the record
# from prose — `templates/sdd-plan.md`, `agents/smith.md`,
# `skills/implement/SKILL.md` — uses the bracket-free form the file is
# actually created with, `phase-N.md`, matching how those same three files
# already write `round-N.md` for the sibling record
# (`docs/the-review-record.md`, `skills/code-review/SKILL.md`,
# `agents/warden.md` never write `round-<N>.md` in prose either).

PROSE_CARRIERS = (
    ("templates", "sdd-plan.md"),
    ("agents", "smith.md"),
    ("skills", "implement", "SKILL.md"),
)


@pytest.mark.parametrize("parts", PROSE_CARRIERS)
def test_the_phase_record_path_is_spelled_the_same_in_every_prose_carrier(parts):
    text = read(os.path.join(ROOT, *parts))
    assert "phases/phase-N.md" in text, "/".join(parts)


def test_the_phase_templates_own_path_comment_matches_the_round_templates():
    phase = read(PHASE_TEMPLATE)
    assert "phases/phase-<N>.md" in phase, (
        "templates/sdd-phase.md's own path comment does not spell its path "
        "`phase-<N>.md` — the same templated form `templates/sdd-round.md` "
        "uses for `round-<N>.md`, and the form every OTHER `<...>` in that "
        "same comment already uses"
    )
