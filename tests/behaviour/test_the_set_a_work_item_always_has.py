"""The SDD file set was read two ways at once, and the counts said so.

`seal/threads/` is the root for a work item — its whole lifetime, its whole
contract.
`frame/design.md` was a file on a ladder keyed to how many files the work touched. Both
readings live in `skills/implement/SKILL.md`, neither is wrong on its own
terms, and under the second one 33 of 35 work items here carry only a closing
memo. That is either correct or a set that quietly fell apart, depending on
which reading a session happens to hold.

Three things settle it.

  the condition   `frame/design.md` is owed when the work alters observable
                  behaviour, not when it touches six files. A count also
                  never said WHEN it was taken (issue #54), and a test with
                  no number has no such moment
  the status      `plan.md` absorbs the task list nobody ever wrote, as a
                  column whose closed value is the commit that closed the
                  phase — a past state, which is what lets it sit inside the
                  contract at all
  the home        `.specseal/tasks/` is described in no shipped document,
                  because no code has ever read it and it has never once been
                  created

The cases below hold the issue the rung cites, the paths, the tables and
the cells the set's documents give a reader. How the skill words the
condition and the status column is the proofer's to read.
"""

from conftest import read

# --- the condition ----------------------------------------------------------


def test_the_rung_cites_the_issue_that_measured_the_count():
    """S6. The skill names both directions, the small change that qualifies
    and the large one that does not, which is the proofer's to read; it
    cites the issue where the count's missing moment is recorded. The branch
    that measured the first direction is history since #967, kept in the
    issue rather than the skill.
    """
    ladder = read("skills", "implement", "orchestration.md")
    # The issue number `#35`, which a reader looks up for when a count would
    # have been taken.
    assert "issue #35" in ladder, (
        "the count never said when it was taken, and that is the half a "
        "reader has to be able to look up"
    )


# --- the status column ------------------------------------------------------


def test_the_skill_lists_the_second_rung_work_and_what_lifts_it():
    """The examples are where the rung drifted, not the condition.

    Round 1 found two documents split: the skill named four kinds of
    second-rung work and `agents/crafter.md` named three, so a change touching
    only tests was decidable by one and not the other. Since #967 the crafter
    opens the skill and keeps no copy, so the list has one home, held here.
    The home is `skills/implement/orchestration.md` since #1312.

    Whitespace-normalised because the file is wrapped.
    """
    skill = " ".join(read("skills", "implement", "orchestration.md").split())
    for example in (
        "a refactor",
        "a performance pass",
        "a formatting sweep",
        "a test that pins what already holds",
    ):
        assert example in skill, f"the skill lost `{example}`"

    # The exception that lifts a default. Naming the value is what moves a
    # change up a rung, and a document that dropped the sentence would
    # silently make the four a closed list again.
    for named in ("a timeout", "a retry count", "a rate", "a size cap"):
        assert named in skill, f"the skill lost `{named}`"


def test_the_plan_template_carries_a_status_column():
    """S7. The column has to be in the shipped template, not only in prose:
    a session bootstraps from the template and never reads the argument."""
    tpl = read("templates", "records", "sdd-plan.md")
    # The header of the Phases table, which `evals/scripts/rule_cases.py`
    # matches and the session reads the Status column by.
    assert "| Phase | Delivers | Verified by | Status |" in tpl


def test_the_plan_template_carries_the_judgments_table():
    """#1167, *Scope* item 11. The orchestrator writes its judgments of the
    run to the plan, and `seal settle` reads them by this heading and this
    header (`skills/settle/scripts/settle.py#JUDGMENTS_HEADER`), so the
    shipped template carries both, with an empty row the settle reads as no
    judgment."""
    tpl = read("templates", "records", "sdd-plan.md")
    after = tpl.split("\n## Judgments of the run\n")
    assert len(after) == 2, "the plan template has no `## Judgments of the run`"
    # The header row `settle.py#JUDGMENTS_HEADER` matches, with the delimiter
    # row under it, as the orchestrator fills it in.
    assert (
        "\n| Date | Judgment | Grounds | Judged against |\n|---|---|---|---|\n"
        in (after[1])
    ), after[1]


def test_the_plan_template_carries_the_overlap_table():
    """#1443, *Scope* items 1 and 6. The framer writes where its work meets
    the release's other work items and which merges first, and the
    orchestrator merges in the order these sections state
    (`skills/implement/merge-order.md` *Orchestrator: the order the work
    items of a release merge in*), so the shipped template carries the heading and the header,
    immediately before `## Operational impact`, where the orchestrator reads
    the version move beside it."""
    tpl = read("templates", "records", "sdd-plan.md")
    after = tpl.split("\n## Overlap with the release\n")
    assert len(after) == 2, "the plan template has no `## Overlap with the release`"
    section = after[1].split("\n## ")[0]
    # The table's header row, whose columns the framer fills and the
    # orchestrator reads `Merges first` from to order the merges.
    assert (
        "\n| Work item | Where both change | Merges first | Grounds |\n|---|---|---|---|\n"
        in section
    ), section
    assert after[1].split("\n## ")[1].startswith("Operational impact\n"), after[1]


# --- who writes each member of the set --------------------------------------
#
# #1148 removed `plan.md`'s approval line, which no code read and whose whole
# record in the round records was findings about its own shape: reading the
# plan and spawning the build is the approval, and the phase's Status cell is
# its record. The cases that pinned the line's shape left with it.


def test_the_file_set_names_who_writes_each_file():
    """The table listed what each member holds and never whose it is.

    That was true while one agent wrote all of them. With the frame drawn by
    `framer` and the records written by the builder, a table with no author
    column reads as a list one session works through, which is the shape the
    split exists to end. How the table says the plan is approved, who it
    says writes the closing memo and the phase record, and when `gaps.md` is
    written are the proofer's to read.
    """
    skill = read("skills", "implement", "SKILL.md")
    header = [
        line for line in skill.splitlines() if line.startswith("| File | Starts from |")
    ]
    assert len(header) == 1, (
        "the SDD file-set table changed shape -- re-read *3. The SDD file set*"
    )
    # The column `Written by`, which a session reads to learn whose each file
    # of the set is, and whose cells the rest of this case reads.
    assert "| Written by |" in header[0], (
        "the file table of *3. The SDD file set* does not say who writes each "
        "member of the set. "
        "`frame/design.md` written by whoever then builds to it is an account of "
        "what got built, and the table is where a session learns otherwise"
    )

    def cells_of(line):
        return [cell.strip() for cell in line.strip().strip("|").split("|")]

    columns = cells_of(header[0])
    rows = {}
    for line in skill[skill.index(header[0]) :].splitlines()[2:]:
        if not line.startswith("| `"):
            break
        # `strict=True`: a row with a cell too few renders with its columns
        # shifted, and a dict built from a short zip would silently read the
        # wrong cell rather than say the table is malformed.
        cells = cells_of(line)
        rows[cells[0]] = dict(zip(columns, cells, strict=True))
    for name in ("`frame/design.md`", "`frame/plan.md`", "`frame/questions.md`"):
        # The agent `framer`, which the orchestrator spawns to write the
        # three frame files.
        assert "framer" in rows[name]["Written by"], (
            f"{name} is no longer the framer's in the file table, which is the "
            "one place a session reads the set as a whole"
        )
