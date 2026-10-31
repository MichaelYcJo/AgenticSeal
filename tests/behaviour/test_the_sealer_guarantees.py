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

    def test_an_earlier_run_is_a_block_and_no_row(self):
        """T3, S5 of #969, under #1198: a re-run at a new HEAD appends its
        block below the earlier run's, so the template holds no `Target SHA`
        row and no `; earlier run:` cell, and the definition re-runs only
        what a commit since touched. Protects: a full re-audit for a
        records-only commit, and an earlier verdict lost when the file is
        rewritten."""
        text = TEMPLATE.read_text(encoding="utf-8")
        assert "Target SHA" not in text and "earlier run" not in text, text
        rule = between(SEALER, "**The guarantee covers HEAD", " check: ")
        assert "re-runs only the claims whose coordinates a commit since" in rule
        # #1198, Scope item 7: the definition says the same as the template.
        # A re-run appends its block and edits none above it, and step 5
        # writes every verdict, steps 1 and 2's among them, in a block.
        assert "appends its own verdict block below the earlier ones" in rule, rule
        step_5 = between(SEALER, "5. **", "6. **")
        for said in (
            "append one verdict block below every block an earlier run left",
            "Edit no earlier block",
            "Every `Verdict:` this file names, steps 1 and 2's among them, "
            "stands in that block.",
        ):
            assert said in step_5, said
        sealer = SEALER.read_text(encoding="utf-8")
        assert "Target SHA" not in sealer and "earlier run:" not in sealer

    def test_the_unfilled_template_is_no_guarantee(self):
        found = fields.read(TEMPLATE.read_text(encoding="utf-8"), fields.GUARANTEE)
        assert found.blocks == [] and found.refusals, found

    def test_the_claims_table_takes_a_row_per_act_of_step_3_and_lists_none(self):
        """T22: the sealer's acts are listed once, in `agents/sealer.md`.
        `docs/the-review-record.md` *The guarantee* makes each act a row and
        names none, and the template's `## Claims re-run` holds its table
        alone, so a duty added to the definition has a row here without a
        second list to keep in step."""
        rule = between(
            ROOT / "docs" / "the-review-record.md", "## The guarantee", "## The stamp"
        )
        assert "Each act is one row of `## Claims re-run` or `## The parties`" in rule
        assert between(TEMPLATE, "## Claims re-run", "| Claim |") == "## Claims re-run "
        row = between(TEMPLATE, "| Claim |", "## The parties")
        assert "does not hold: what came back" in row
        for act in ("`fixed <commit>`", "sampled", "removal", "🔴"):
            assert act not in row, act


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
        assert "\nmodel: opus\n" in head
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
        item's records; no step of the definition runs `seal gate --base`.

        Protects: the sealer re-running a suite the orchestrator just ran
        (the 240K-token second run #957 measured), and a sealer that runs
        nothing and still writes a verdict over a run that never happened.
        Its conduct is the `shape-runs-no-broad-run` and `truth-no-gate`
        graders' (`evals/behaviour/sealer/rule-sealer-no-gate/`); this holds
        the words the spawn reads."""
        step = " ".join(
            between(SEALER, "1. **Read the gate's record.**", "2. **").split()
        )
        assert "`trail/gate.md`" in step, step
        assert "log --no-merges --name-only <named>..HEAD ^<base>" in step, step
        assert "`chain_check.py#follows`" in step, step
        assert "`Verdict: withheld reason: no broad run at HEAD`" in step, step
        assert "Absent" in step and "any other path" in step, step
        assert "not an ancestor of HEAD" in step, step
        assert "the plain branch name the prompt names" not in step, step
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
        assert "`broad_gate.py#resolve_base`" in intro, intro
        assert (
            "take the first of `<name>@{upstream}`, `origin/<name>` and "
            "`<name>` that `git -C <root> rev-parse --verify --quiet` answers, "
            "and every `<base>` below is the commit it prints"
        ) in intro, intro
        assert (
            "`Verdict: withheld reason: the base <name> resolves to no commit here`"
        ) in intro, intro
        order = between(SEALER, "## Order of work", "## Never")
        assert "seal gate --base" not in order, (
            "a step of the sealer's definition runs the broad gate"
        )

    def test_the_sealer_is_spawned_before_the_pull_request_and_reads_its_body_from_a_file(
        self,
    ):
        """S8 of #943. The pull request opens once the sealer has sealed, so
        no pull request exists when the sealer runs: the description no
        longer spawns it per ready pull request, and the body it audits is
        the file the prompt names, the one the pull request then opens
        with."""
        text = SEALER.read_text(encoding="utf-8")
        head = " ".join(text.split("---")[1].split())
        assert "once per ready pull request" not in head, head
        assert "before the pull request opens" in head, head
        intro = " ".join(
            between(SEALER, "You work in the clone", "## Order of work").split()
        )
        assert "a file holding the pull request body" in intro, intro
        # Round 1 of #943, finding 1: on the stated limit's path the sealer
        # runs again with the pull request already open.
        assert "or is given it where already open" in intro, intro
        assert "gh pr view" not in text, "the sealer still reads an open pull request"

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
        assert (
            "other than one touching only the closing records, `trail/gate.md` "
            "and `guarantee.md`, owes a new audit"
        ) in rule, rule
        assert "work item's records" not in rule, rule

    def test_the_orchestration_quotes_what_only_the_gate_can_tell(self):
        """Moved by #969 from the sealer with the run. The moved base, the
        copy of the gate that ran and the outputs directory are lines a reader
        learns from nowhere else, and the orchestrator who runs the gate is
        the one who quotes them; the sealer, which sees no gate output, no
        longer carries the instruction."""
        text = " ".join(
            (ROOT / "skills" / "code-review" / "orchestration.md")
            .read_text(encoding="utf-8")
            .split()
        )
        assert "where resolving the base moved it" in text.lower()
        assert "the tree's copy of the gate" in text
        assert "`outputs kept under seal-gate-<random>/`" in text
        sealer = " ".join(SEALER.read_text(encoding="utf-8").split())
        assert "outputs kept under" not in sealer

    def test_step_3_holds_two_acts_and_reads_no_location(self):
        """T40 (S22): step 3 is the one list of the sealer's acts, and it holds
        two — the sample of the crafter's claims re-run, and the removals
        confirmed absent. Whether a `fixed` commit touches its finding's
        `location:` is the check's to read, so no act of step 3 reads it."""
        step = between(SEALER, "3. **A claim against the fact.**", "4. **")
        assert "Choose a sample of the crafter's `executed`" in step, step
        assert "For every `## Removes` row of `frame/design.md`" in step, step
        assert "two acts" in step.lower(), step
        assert step.count("For every") == 1, step
        for word in ("touches", "Location", "location", "fixed <commit>"):
            assert word not in step, word

    def test_step_4_reads_a_records_only_fix_as_the_fix_passs_claim(self):
        """S4 of #1148. `chain_check.py#records` passes a `fixed` of the last
        record located in the work item's records alone whose commit touched
        them alone, with no verifying round after it, because the sealer is
        that fix's reader: step 4 says so, and reads it as a party's claim at
        HEAD."""
        step = between(SEALER, "4. **The parties against each other.**", "5. **")
        assert (
            "where the finding is located in `seal/threads/<item>/` alone and its "
            "commit touched nothing outside it" in step
        ), step
        assert "the fix pass's claim with you as its reader" in step, step
        assert "read the record at HEAD against what the finding asked" in step


# --- the document that states the guarantee ------------------------------------


class TestDocument:
    def test_the_guarantee_section_points_at_step_3_and_lists_no_act(self):
        """T23: `docs/the-review-record.md` *The guarantee* points at the
        definition's steps 3 and 4 for the acts and lists none of them. The
        record's vocabulary in *The round record* keeps `fixed <commit>`,
        and is outside the slice read here."""
        section = between(DOCUMENT, "## The guarantee", "## The run")
        assert "`agents/sealer.md` step 3" in section
        assert "step 4" in section
        assert "one row of `## Claims re-run` or `## The parties`" in section
        for act in ("`fixed <commit>`", "re-runs a sample", "stands in the tree"):
            assert act not in section, act
