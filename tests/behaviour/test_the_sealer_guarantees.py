"""The sealer's `guarantee.md`: its template, what `chain_check.py` reads of
it, and the definition that writes it.

`templates/records/sdd-guarantee.md` is the file the sealer fills, and
`chain_check.py#guarantee` is the arm that reads it at the pull request,
through `hooks/lib/fields.py`: a ready pull request passes only where the
newest verdict block names HEAD and reads `sealed`. Each group holds a case
on good input and one on bad.

#942 moved the cases of the arm, which read no file of this repository, into
`tests/skills/test_chain_check.py`, and #1198 put the reader's in
`tests/hooks/test_fields.py`. What stays reads the template, the definition,
the document, or every committed `guarantee.md`.
"""

import pathlib
import re

import conftest
from conftest import (
    load_module as load,
)

ROOT = pathlib.Path(conftest.ROOT)
CHAIN = ROOT / "skills" / "code-review" / "scripts" / "chain_check.py"
READER = ROOT / "skills" / "verify" / "scripts" / "unverified_check.py"
TEMPLATE = ROOT / "templates" / "records" / "sdd-guarantee.md"
SEALER = ROOT / "agents" / "sealer.md"
DOCUMENT = ROOT / "docs" / "the-review-record.md"


def between(path, start, end):
    """The text of `path` from `start` to `end`, whitespace collapsed."""
    text = " ".join(path.read_text(encoding="utf-8").split())
    head = text.index(start)
    return text[head : text.index(end, head)]


chain = load(CHAIN, "chain_check_for_the_guarantee")
reader = load(READER, "unverified_reader_for_the_guarantee")
fields = chain.FIELDS


# --- the template ---------------------------------------------------------------


def sealer_verdict_patterns():
    """Every `pattern:` a sealer eval grader matches a verdict line with, as
    `evals/scripts/rule_cases.py` generated it: a `truth-` grader's, which
    opens at the line, and a `shape-verdict` grader's, which opens at the
    verdict block holding it."""
    found = []
    for path in sorted(
        (ROOT / "evals" / "behaviour" / "sealer").glob("*/graders/*.md")
    ):
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("pattern: '") and "Verdict:" in line:
                found.append(line[len("pattern: '") : -1])
    return found


class TestTemplate:
    def test_no_sealer_grader_matches_a_line_of_the_template(self):
        """Round 2 of #1000, finding 2: a sealer that keeps the template's
        comment must not pass a verdict grader by it, so no line of the
        template opens with a verdict a grader reads. Seen red against the
        comment that listed the three shapes at the start of their lines."""
        patterns = sealer_verdict_patterns()
        assert len(patterns) >= 9, patterns
        text = TEMPLATE.read_text(encoding="utf-8")
        hits = [p for p in patterns if re.search(p, text, re.M)]
        assert hits == [], hits

    def test_the_template_carries_the_tables_sections_and_verdict_block(self):
        """#1198, *Scope* item 3: the run, the claims and the parties are
        tables for people, and the template's one verdict block holds
        `target:`, the `original:` line and `Verdict:`, in that order."""
        text = TEMPLATE.read_text(encoding="utf-8")
        lines = reader.readable(text)
        rows = chain.table_rows(reader, lines)
        assert [c[0].strip() for c in rows[:3]] == ["Field", "---", "Broad gate"]
        raw = text.split("\n")
        opener = raw.index(fields.OPENER)
        assert raw.count(fields.OPENER) == 1
        keys = [line.split(" ", 1)[0] for line in raw[opener + 1 : opener + 4]]
        assert keys == [fields.TARGET, fields.ORIGINAL, fields.SEALER_VERDICT]
        assert raw[opener + 4] == fields.FENCE
        assert reader.sections(lines, "## Claims re-run")
        assert reader.sections(lines, "## The parties")
        assert ["Claim", "Source", "Command", "Result"] in [
            [c.strip() for c in r] for r in rows
        ]
        assert ["Party", "Says", "Agrees with", "Disagrees with"] in [
            [c.strip() for c in r] for r in rows
        ]
        # T4, S9 of #969: `sealed` has one meaning in this file. The cell
        # quotes the run `trail/gate.md` names; it never says `sealed`, which
        # a reader would take for the sealer's verdict.
        cell = next(c[1] for c in rows if c[0].strip() == "Broad gate")
        assert "sealed" not in cell, cell
        assert "`trail/gate.md` names" in cell, cell

    def test_the_unfilled_template_is_no_guarantee(self):
        found = fields.read(TEMPLATE.read_text(encoding="utf-8"), fields.GUARANTEE)
        assert found.blocks == [] and found.refusals, found


# --- every committed guarantee ---------------------------------------------------


def test_every_committed_guarantee_in_blocks_reads_whole():
    """Round 1 of #1000, finding 2, under #1198: each `guarantee.md` under
    `seal/threads/` that holds a verdict block's opener reads through the
    reader with no refusal and at least one block. A guarantee of a work
    item released before #1198 holds none, and no check judges it again."""
    found = {}
    for path in (ROOT / "seal" / "threads").glob("*/guarantee.md"):
        text = path.read_text(encoding="utf-8")
        if fields.OPENER not in text.split("\n"):
            continue
        read = fields.read(text, fields.GUARANTEE)
        found[path.parent.name] = (len(read.blocks), read.refusals)
    assert {k: v for k, v in found.items() if v[1] or not v[0]} == {}, found


# --- the definition that writes it ---------------------------------------------


class TestDefinition:
    def test_the_sealer_runs_on_opus_with_the_core_and_the_contract(self):
        head = SEALER.read_text(encoding="utf-8").split("---")[1]
        # The frontmatter key `model`, which the harness reads when it
        # spawns the sealer.
        assert "\nmodel: opus\n" in head
        # The frontmatter list `skills`, whose two entries the harness
        # injects into the sealer before its first call.
        assert "skills:\n  - core\n  - agent-contract\n" in head
        assert head.count("\n  - ") == 2

    def test_the_sealer_writes_the_guarantee_from_the_template(self):
        text = " ".join(SEALER.read_text(encoding="utf-8").split())
        assert "templates/records/sdd-guarantee.md" in text
        assert "judges nothing" not in text

    def test_step_1_reads_the_record_and_runs_nothing(self):
        """T2, S1 of #969. Step 1 reads `trail/gate.md` and the commits after
        the run it names, and refuses with `withheld reason: no broad run at HEAD`
        where the record is absent or followed by a path outside the work
        item's records.

        Protects: a sealer that runs nothing and still writes a verdict over a
        run that never happened. That it runs no broad run is the
        `shape-runs-no-broad-run` and `truth-no-gate` graders'
        (`evals/behaviour/sealer/rule-sealer-no-gate/`); this holds the
        commands, paths and verdict lines the spawn reads. The conditions
        step 1 states are the proofer's to read."""
        step = " ".join(
            between(SEALER, "1. **Read the gate's record.**", "2. **").split()
        )
        # The path of the gate's record, which the sealer opens first.
        assert "`trail/gate.md`" in step, step
        # The `git` arguments the sealer runs to list what followed the run.
        assert "log --no-merges --name-only <named>..HEAD ^<base>" in step, step
        # The citation `chain_check.py#follows`, the reader the sealer
        # resolves to judge those paths as the check does.
        assert "`chain_check.py#follows`" in step, step
        # The verdict line `hooks/lib/fields.py` parses, as the sealer writes it.
        assert "`Verdict: withheld reason: no broad run at HEAD`" in step, step
        # Round 2 of #969, finding 1: the base arrives as a plain branch name,
        # a local ref, and a worktree with only `origin/<base>` gives step 1's
        # `^<base>` exit 128. It is resolved once, as the gate resolves it, and
        # every `<base>` after it is that ref's commit. Round 3, findings 1
        # and 2: the at-base clone carries no remote-tracking ref, so the
        # ref names nothing there; and a base resolving to nothing is the
        # orchestrator's input to repair, so `withheld`, not `undecided`.
        intro = " ".join(
            between(SEALER, "You work in the clone", "## Order of work").split()
        )
        # The citation of the gate's resolver, which the sealer's order
        # mirrors.
        assert "`broad_gate.py#resolve_base`" in intro, intro
        # The three refs, in order, and the `git` command the sealer runs to
        # resolve `<base>`; the commands are the fact.
        assert (
            "take the first of `<name>@{upstream}`, `origin/<name>` and "
            "`<name>` that `git -C <root> rev-parse --verify --quiet` answers, "
            "and every `<base>` below is the commit it prints"
        ) in intro, intro
        # The verdict line `hooks/lib/fields.py` parses, as the sealer writes it.
        assert (
            "`Verdict: withheld reason: the base <name> resolves to no commit here`"
        ) in intro, intro

    def test_the_sealer_checks_the_copy_and_reads_only_the_orchestrators_part(
        self,
    ):
        """S13 of #1044. The part of the body below `pr_body.py#HEADING` is
        the records' own text, so step 2 checks it with `seal pr-body
        --check` and withholds on any exit but 0, naming what the command
        printed; steps 2 and 4 and *Never* then read only the part above the
        heading as a party, the body's first part, which the orchestrator
        wrote (#1148 S6). Before this, most withheld verdicts were a body
        sentence restating a record."""
        step_2 = between(SEALER, "2. **", "3. **")
        step_4 = between(SEALER, "4. **", "5. **")
        never = between(SEALER, "## Never", "## Rules")
        pinned = [
            (step_2, "`seal pr-body <item> --body <file> --check`"),
            (step_2, "On any exit but 0"),
            (
                step_2,
                "`Verdict: withheld reason: <the first line the command printed>`",
            ),
            (step_2, "`skills/code-review/scripts/pr_body.py#HEADING`"),
            (step_2, "the part of the body below the line"),
            (step_2, "request body above that line, its first part"),
            (step_4, "the orchestrator's part of the pull request body"),
            (never, "the orchestrator's part of the pull request body"),
        ]
        missing = [phrase for where, phrase in pinned if phrase not in where]
        assert missing == [], missing
        assert "list of changes" not in never, never

    def test_the_guarantee_rule_exempts_only_the_closing_records(self):
        """Round 1 of #969, finding 1. `chain_check.py#guarantee` lets only
        `trail/gate.md` and `guarantee.md` follow the commit the guarantee
        names (`follows(..., only=CLOSING_RECORDS)`); a sealer told that any
        record of the work item may follow keeps an earlier verdict over a
        changelog or phase record it never read, and the check refuses it."""
        rule = " ".join(
            between(SEALER, "**The guarantee covers HEAD", " check: ").split()
        )
        # The two paths `chain_check.py#CLOSING_RECORDS` lets follow the
        # audited commit, which the sealer resolves to tell a commit that owes
        # a new audit; the code spans are the fact.
        assert (
            "other than one touching only the closing records, `trail/gate.md` "
            "and `guarantee.md`, owes a new audit"
        ) in rule, rule

    def test_the_orchestration_quotes_the_gates_outputs_line(self):
        """Moved by #969 from the sealer with the run. The outputs directory
        is a line a reader learns from nowhere else, and the orchestrator who
        runs the gate is the one who quotes it. The other lines it quotes, and
        that the sealer carries none, are the proofer's to read."""
        text = " ".join(
            (ROOT / "skills" / "code-review" / "orchestration.md")
            .read_text(encoding="utf-8")
            .split()
        )
        # The line `broad_gate.py` prints to stderr when it keeps its
        # outputs, which the orchestrator matches in the gate's output and
        # quotes.
        assert "`outputs kept under seal-gate-<random>/`" in text


# --- the document that states the guarantee ------------------------------------


class TestDocument:
    def test_the_guarantee_section_points_at_steps_3_and_4(self):
        """T23: `docs/the-review-record.md` *The guarantee* points at the
        definition's steps 3 and 4 for the acts. Whether it lists any of them
        is the proofer's to read."""
        section = between(DOCUMENT, "## The guarantee", "## The run")
        # The citation of `agents/sealer.md`'s steps 3 and 4, which a reader
        # resolves to the sealer's acts.
        assert "`agents/sealer.md` step 3" in section
        assert "step 4" in section
