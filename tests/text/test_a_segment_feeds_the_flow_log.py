"""Issue #109 part 1: the instruction "measure every crafter/proofer segment and
log what it found" used to live only in a person's message
(`~/.claude/projects/.../memory/measure-every-segment-to-89.md`), retyped
every session and naming a hardcoded issue number that goes stale the moment
that issue closes. It moved into the verify skill, so a session does it
because the skill says so, and the destination becomes a
`flow-measurement`-labelled GitHub issue instead of a number. Since #940 the
section is `skills/verify/orchestration.md`'s, the orchestrator's half of the
skill, because posting is withheld from every agent.

This module pins what a session reading that section acts on: the command
it runs, and the exit codes it reads.

Issue #136 adds a second destination and a second zero. Two issues collect
measurements in the same shape and one of them is deleted at every release, so
the section now says which reading goes to which — a segment's own numbers to
the rolling `flow-measurement` log, a reading that only means something across
versions to the durable `flow-baseline` one — and separates a repository that
never measured from one whose log stopped. The cases below pin the durable
log's label, which the command takes on `--label`.

Issue #170 adds a second reading to the same section, one level up. Everything
above it measures one segment; a run is every segment plus the rounds and the
commits between them, and no segment's numbers say what the run cost. So the
section now states the run-level comparison table — its rows, what each row is
taken from, and the three sentences that keep it comparable: the tokens are
counted rather than estimated and counted the same way every time, a run whose
transcript covered only part of its branch says so in the prose rather than in
a column, and the table itself carries no verdict. The cases below pin the
rows, their sources and the token fields the count reads, and the three
sentences are the proofer's to read. One case is structural rather than textual — every row
of the table must name a source, because a row nobody can reproduce is a row
the next run fills in by feel.

Issue #1479 ends the per-segment post. The section is *Measure the run, and
feed the flow log*: the orchestrator posts once when a work item's run ends,
with `seal cost --work-item`, the command the release already ran for what
no session posted, after reading the same command without `--post`, and the
run's table goes into that one comment. The
by-hand lookups and post leave the section, because the command takes each
and the section states each outcome as an exit code; so do the per-segment
mode and the description of how the meter computes its columns, which
`session_cost.py` states. The cases that pinned those went with them.
"""

import os

from conftest import ROOT

# Since #940 the section is the orchestrator's, in the verify skill's
# orchestration file; the crafter's and the sealer's `SKILL.md` no longer
# carries it.
SKILL = os.path.join(ROOT, "skills", "verify", "orchestration.md")
CRAFTERS_SKILL = os.path.join(ROOT, "skills", "verify", "SKILL.md")

SECTION_HEADING = "## Measure the run, and feed the flow log"


def read(path=SKILL):
    with open(path, encoding="utf-8") as f:
        return f.read()


def section_text():
    """The section with its lines intact, from its heading to the next `## `
    or to the end of the file, where it is the last section."""
    text = read()
    start = text.index(SECTION_HEADING)
    rest = text[start + len(SECTION_HEADING) :]
    end = rest.find("\n## ")
    return rest if end == -1 else rest[:end]


def section_body():
    """Whitespace-collapsed, so a substring check does not break every time
    the prose re-wraps at a different column."""
    return " ".join(section_text().split())


RUN_TABLE_HEADER = "| Row | Taken from |"

RUN_TABLE_ROWS = (
    "Rounds",
    "Wall clock",
    "Commits, by kind",
    "Findings by severity",
    "Findings by `Location`",
    "Records' share of the diff",
    "Model turns",
    "Segments",
    "Broad gate",
)


def run_table_rows():
    """The run-level table's data rows, as `[row label, source]` pairs."""
    lines = section_text().splitlines()
    assert RUN_TABLE_HEADER in lines, (
        "the section carries no run-level table — `" + RUN_TABLE_HEADER + "` "
        "is the header row every case below reads"
    )
    rows = []
    for line in lines[lines.index(RUN_TABLE_HEADER) + 2 :]:
        if not line.startswith("|"):
            break
        rows.append([cell.strip() for cell in line.strip().strip("|").split("|")])
    return rows


def test_the_section_is_the_orchestrators_and_the_crafters_skill_names_it():
    """#940 split the verify skill along its headings: posting is withheld
    from every agent (contract rule 6), so the section is in the
    orchestrator's file, and the opening of the file the crafter and the
    sealer open names the orchestrator's file. Which file carries which
    section is the proofer's to read."""
    crafters = read(CRAFTERS_SKILL)
    # The path a reader of `skills/verify/SKILL.md` resolves to the
    # orchestrator's two acts.
    assert "`skills/verify/orchestration.md`" in crafters.split("\n## ", 1)[0], (
        "the opening of `skills/verify/SKILL.md` does not say where the "
        "orchestrator's two acts are"
    )


def test_the_section_names_the_measure_step():
    body = section_body()
    # The script the orchestrator measures the run with.
    assert "session_cost.py" in body, (
        "the section never names `session_cost.py` — a session reading it "
        "has no command to measure the run with"
    )


def test_the_section_says_what_each_exit_of_the_command_means():
    """#1479, S2. The section once walked the lookups by hand, and each
    outcome had a paragraph. The command takes the lookups, so the section
    names each exit code with what it means and what the orchestrator does
    next. Whether each code's sentence states the outcomes the command
    gives it is the proofer's to read."""
    body = section_body()
    # The three exit codes of `seal cost --work-item --post`: 0 posted or
    # nothing due, 1 nothing posted and named, 2 the command line refused.
    for code in ("Exit 0", "Exit 1", "Exit 2"):
        assert code in body, (
            f"the section never says what `{code}` of the run's command means, "
            "so an orchestrator that meets it cannot tell a refusal it must "
            "name from one it must correct"
        )


def test_the_section_says_the_release_posts_what_no_session_posted():
    """#1439, and #1479. The run's one post and the release's are the same
    command. The section names it, and the `# <file name>` line it reads on
    the log to tell a segment the run's comment named from one no comment
    named, which is what leaves the release's run nothing to post for a
    work item whose run posted."""
    body = section_body()
    # The command the orchestrator and the release run.
    assert "seal cost --work-item" in body, (
        "the section never names `seal cost --work-item`, so a run's reading "
        "has no way onto the log"
    )
    # The line's spelling, which `seal cost --work-item` reads on the log.
    assert "`# <file name>`" in body, (
        "the section never says `--work-item` reads the `# <file name>` line "
        "inside a comment's fence, which is how it leaves out what a session "
        "posted"
    )


def test_the_section_names_the_durable_logs_label():
    body = section_body()
    # The label the command resolves to the durable log.
    assert "flow-baseline" in body, (
        "the section never names `flow-baseline`, so a reading that only "
        "means something across versions has nowhere to go but the rolling "
        "log — which is deleted when the version ships. That happened on "
        "2026-09-04 and is what #136 opened for"
    )


def test_the_section_states_the_run_level_table():
    assert RUN_TABLE_HEADER in section_text(), (
        "the section says where a run's reading goes and never says what "
        "the table in it carries. Without the table "
        "each run invents its own shape and two runs cannot be read side by "
        "side"
    )


def test_the_run_level_table_carries_every_row():
    labels = [row[0] for row in run_table_rows()]
    for expected in RUN_TABLE_ROWS:
        assert any(expected in label for label in labels), (
            f"the run-level table has no `{expected}` row. The rows are the "
            "whole point of stating the table: a run that drops one is a run "
            "the next comparison cannot line up against"
        )


def test_every_row_of_the_run_level_table_names_its_source():
    """Structural rather than textual. A row with no source is a number the
    next run produces by feel, which is exactly what one stated shape is for."""
    for row in run_table_rows():
        assert len(row) == 2 and row[1], (
            f"the run-level table's `{row[0]}` row names no source. Every row "
            "must say where its number is taken from, or the next run guesses"
        )


def test_the_token_row_names_the_command_that_prints_it():
    token_rows = [row for row in run_table_rows() if "Model turns" in row[0]]
    assert token_rows, "the run-level table lost its token row"
    # The script the token row's source names, which the orchestrator runs.
    assert "session_cost.py" in token_rows[0][1], (
        "the token row does not name `session_cost.py`. It is the one row "
        "nobody can produce by hand, and a run that sums `usage` with a "
        "script written for the occasion produces a number the next run "
        "cannot be compared against"
    )


def test_the_tokens_are_counted_rather_than_estimated():
    body = section_body()
    # The transcript's `usage` fields the count reads.
    for field in (
        "output_tokens",
        "cache_creation_input_tokens",
        "cache_read_input_tokens",
    ):
        assert field in body, (
            f"the counting rule never names `{field}`, so 'the same way every "
            "time' is not something a reader can check"
        )


def labelled(fragment):
    """The one run-level row whose label carries `fragment`, as [label, source]."""
    rows = [row for row in run_table_rows() if fragment in row[0]]
    assert len(rows) == 1, (
        f"expected exactly one run-level row labelled {fragment!r}, found "
        f"{len(rows)}. A row renamed has to bring its case with it"
    )
    return rows[0]


def test_the_location_buckets_are_the_repositorys_own_definition_of_a_record():
    """Round 1's finding 3. The row split `ledger` from `record` and the share
    row counted only `seal/threads/**`, where the review chain's own definition
    puts a work item's documents, the ledger and its fragments in ONE bucket:
    a finding in any of them is about the run's paperwork rather than about
    the tool. Two definitions of one word made the same run's share row read
    45 % as the row was written and 48 % under the policy — and a table exists
    to be comparable, which two fillings of one row destroy.

    A ticket is a request and a ratified document outranks it, so the buckets
    follow the policy. `gaps.md` *Where spec and implementation diverged*
    quotes both sides. The case reads the record path the `Location` row
    names."""
    _label, source = labelled("Findings by `Location`")
    # The path the row names as a record path, which the orchestrator sorts
    # each finding's `Location` by.
    for path in ("`seal/threads/`",):
        assert path in source, (
            f"the `Location` row no longer names {path} as a record path, so "
            "a finding about the run's own paperwork lands in the code bucket"
        )


def test_the_broad_gate_row_asks_for_what_the_file_actually_carries():
    """Round 1's finding 4, and the premise #174 reversed. The broad gate's
    record holds one entry per full-suite run, so the count is read off it
    rather than remembered, and the row's source names that record's file:
    `trail/gate.md` since the rename to AgenticSeal (#923, #1051). How the
    source describes the record's entries is the proofer's to read."""
    _label, source = labelled("Broad gate")
    # The path the orchestrator opens to read the count off.
    assert "`trail/gate.md`" in source, (
        "the row names no file the count is read from, which is the reason "
        "the count went unnoticed in the first place"
    )


def test_the_section_says_the_mode_notices_a_spawn_inside_a_segment():
    """#343, and #1479. The reading a run ends with, `seal cost
    --work-item`, prints the `Contract rule 6` line for a segment that
    spawned an agent, as `--segments` does, and the section is where the
    orchestrator learns what the line means and where it goes.

    Round 1's finding 1. With `--post` the reading goes into the comment and
    the terminal shows one state line, so the line reaches the orchestrator
    only through the read without `--post`. The section states that read as
    a command of its own."""
    body = section_body()
    # The label of the line `session_cost.py` prints for a spawn inside a
    # segment, which the orchestrator matches to this section.
    assert "`Contract rule 6` line" in body, (
        "the section names the command and not the one finding it can print "
        "that is about the agent's own conduct rather than its cost"
    )
    # The read the orchestrator runs before it posts, a fenced line of its
    # own with no `--post` on it.
    assert "seal cost --work-item <the work item's directory>" in (
        section_text().splitlines()
    ), (
        "the section states only the posting command, whose terminal shows a "
        "state line and no `Contract rule 6` line, so the orchestrator never "
        "sees the line it is told to give a home"
    )
