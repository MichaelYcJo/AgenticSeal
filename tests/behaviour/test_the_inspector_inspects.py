"""The inspector's `inspection.md`: its template, what `chain_check.py` reads of
it, and the definition that writes it.

`templates/records/sdd-inspection.md` is the file the inspector fills, and
`chain_check.py#inspection` is the arm that reads it at the pull request,
through `lib/fields.py`: a ready pull request passes only where the
newest verdict block names HEAD and reads `cleared`. Each group holds a case
on good input and one on bad.

The cases of the arm, which read no file of this repository, stand in
`tests/skills/test_chain_check.py`, and the reader's, the unfilled template
among them, in `tests/lib/test_fields.py`. What stays reads the template, the
definition, the document, the orchestration that hands the inspector its run,
or every committed `inspection.md`.
"""

import pathlib
import re

import conftest
from conftest import (
    load_module as load,
)
from test_fields import TEMPLATE, fields

# No TARGET: its cases walk every committed inspection.md and every inspector eval grader, and hold the inspection across its template, agents/inspector.md and docs/forms/the-inspection.md.


ROOT = pathlib.Path(conftest.ROOT)
READER = ROOT / "lib" / "lines.py"
INSPECTOR = ROOT / "agents" / "inspector.md"
DOCUMENT = ROOT / "docs" / "forms" / "the-inspection.md"


def between(path, start, end):
    """The text of `path` from `start` to `end`, whitespace collapsed."""
    text = " ".join(path.read_text(encoding="utf-8").split())
    head = text.index(start)
    return text[head : text.index(end, head)]


reader = load(READER, "lines_reader_for_the_inspection")
# The chain check, whose line at a finding no round read the orchestration
# names.
chain = load(
    ROOT / "skills" / "code-review" / "scripts" / "chain_check.py",
    "chain_check_for_the_inspection",
)


# --- the template ---------------------------------------------------------------


def inspector_verdict_patterns():
    """Every `pattern:` an inspector eval grader matches a verdict line with, as
    `evals/scripts/rule_cases.py` generated it: a `truth-` grader's, which
    opens at the line, and a `shape-verdict` grader's, which opens at the
    verdict block holding it."""
    found = []
    for path in sorted(
        (ROOT / "evals" / "behaviour" / "inspector").glob("*/graders/*.md")
    ):
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("pattern: '") and "Verdict:" in line:
                found.append(line[len("pattern: '") : -1])
    return found


class TestTemplate:
    def test_no_inspector_grader_matches_a_line_of_the_template(self):
        """Round 2 of #1000, finding 2: an inspector that keeps the template's
        comment must not pass a verdict grader by it, so no line of the
        template opens with a verdict a grader reads. Seen red against the
        comment that listed the three shapes at the start of their lines."""
        patterns = inspector_verdict_patterns()
        assert len(patterns) >= 9, patterns
        text = TEMPLATE.read_text(encoding="utf-8")
        hits = [p for p in patterns if re.search(p, text, re.M)]
        # The patterns the inspector's eval graders match a verdict with, which
        # `evals/scripts/rule_cases.py` generated: a template line one of
        # them matched would pass an inspector that left the template's comment
        # standing.
        assert hits == [], hits

    def test_the_template_carries_the_tables_sections_and_verdict_block(self):
        """#1198, *Scope* item 3: the claims and the parties stand under the
        two headings the document cites, and the template's one verdict block
        holds `target:`, the `original:` line and `Verdict:`, in that order.
        The columns of the tables for people are the proofer's to read. The
        run the inspector read is `trail/gate.md`'s, which the template no
        longer copies (#1319, D5)."""
        text = TEMPLATE.read_text(encoding="utf-8")
        lines = reader.readable(text)
        raw = text.split("\n")
        opener = raw.index(fields.OPENER)
        # The block's opener, its three keys in order and its closing fence,
        # which `chain_check.py#inspection` reads through `lib/fields.py`.
        assert raw.count(fields.OPENER) == 1
        keys = [line.split(" ", 1)[0] for line in raw[opener + 1 : opener + 4]]
        assert keys == [fields.TARGET, fields.ORIGINAL, fields.INSPECTOR_VERDICT]
        assert raw[opener + 4] == fields.FENCE
        # The two headings `docs/forms/the-inspection.md` *It checks a claim
        # against the fact, and the parties against each other.* cites,
        # which the inspector writes each act's row under.
        assert reader.sections(lines, "## Claims re-run")
        assert reader.sections(lines, "## The parties")


# --- every committed inspection ---------------------------------------------------


def test_every_committed_inspection_in_blocks_reads_whole():
    """Round 1 of #1000, finding 2, under #1198: each `inspection.md` under
    `agentory/threads/` that holds a verdict block's opener reads through the
    reader with no refusal and at least one block. An inspection of a work
    item released before #1198 holds none, and no check judges it again."""
    found = {}
    for path in (ROOT / "agentory" / "threads").glob("*/inspection.md"):
        text = path.read_text(encoding="utf-8")
        if fields.OPENER not in text.split("\n"):
            continue
        read = fields.read(text, fields.INSPECTION)
        found[path.parent.name] = (len(read.blocks), read.refusals)
    assert {k: v for k, v in found.items() if v[1] or not v[0]} == {}, found


# --- the definition that writes it ---------------------------------------------


class TestDefinition:
    def test_the_inspector_runs_on_opus_with_the_core_and_the_contract(self):
        head = INSPECTOR.read_text(encoding="utf-8").split("---")[1]
        # The frontmatter key `model`, which the harness reads when it
        # spawns the inspector.
        assert "\nmodel: opus\n" in head
        # The frontmatter list `skills`, whose two entries the harness
        # injects into the inspector before its first call.
        assert "skills:\n  - core\n  - agent-contract\n" in head
        assert head.count("\n  - ") == 2

    def test_the_inspector_writes_the_inspection_from_the_template(self):
        text = " ".join(INSPECTOR.read_text(encoding="utf-8").split())
        # The path of the template the inspector opens to write `inspection.md`.
        assert "templates/records/sdd-inspection.md" in text

    def test_step_1_reads_the_record_and_runs_nothing(self):
        """T2, S1 of #969. Step 1 reads `trail/gate.md` and the commits after
        the run it names, and refuses with `withheld reason: no broad run at HEAD`
        where the record is absent or followed by a path outside the work
        item's records.

        Protects: an inspector that runs nothing and still writes a verdict over a
        run that never happened. That it runs no broad run is the
        `shape-runs-no-broad-run` and `truth-no-gate` graders'
        (`evals/behaviour/inspector/rule-inspector-no-gate/`); this holds the
        commands, paths and verdict lines the spawn reads. The conditions
        step 1 states are the proofer's to read."""
        step = " ".join(
            between(INSPECTOR, "1. **Read the gate's record.**", "2. **").split()
        )
        # The path of the gate's record, which the inspector opens first.
        assert "`trail/gate.md`" in step, step
        # The `git` arguments the inspector runs to list what followed the run.
        # #1640: the flag keeps a submodule's path in the listing under
        # `diff.ignoreSubmodules` and a `.gitmodules` entry's `ignore`, as
        # `lib/gitcmd.py#FLAGS` does for the scripts.
        assert (
            "log --ignore-submodules=none --no-merges --name-only <named>..HEAD ^<base>"
            in step
        ), step
        # The citation of `follows`, the reader the inspector resolves to judge
        # those paths as the check does.
        assert "`skills/code-review/scripts/chain_check.py#follows`" in step, step
        # The verdict line `lib/fields.py` parses, as the inspector writes it.
        assert "`Verdict: withheld reason: no broad run at HEAD`" in step, step
        # Round 2 of #969, finding 1: the base arrives as a plain branch name,
        # a local ref, and a worktree with only `origin/<base>` gives step 1's
        # `^<base>` exit 128. It is resolved once, as the gate resolves it, and
        # every `<base>` after it is that ref's commit. Round 3, findings 1
        # and 2: the at-base clone carries no remote-tracking ref, so the
        # ref names nothing there; and a base resolving to nothing is the
        # orchestrator's input to repair, so `withheld`, not `undecided`.
        intro = " ".join(
            between(INSPECTOR, "You work in the clone", "## Order of work").split()
        )
        # The citation of the gate's resolver, which the inspector's order
        # mirrors.
        assert "`broad_gate.py#resolve_base`" in intro, intro
        # The three refs, in order, and the `git` command the inspector runs to
        # resolve `<base>`; the commands are the fact.
        assert (
            "take the first of `<name>@{upstream}`, `origin/<name>` and "
            "`<name>` that `git -C <root> rev-parse --verify --quiet` answers, "
            "and every `<base>` below is the commit it prints"
        ) in intro, intro
        # The verdict line `lib/fields.py` parses, as the inspector writes it.
        assert (
            "`Verdict: withheld reason: the base <name> resolves to no commit here`"
        ) in intro, intro

    def test_the_inspector_checks_the_copy_with_the_command_and_its_exit(
        self,
    ):
        """S13 of #1044. The part of the body below `pr_body.py#HEADING` is
        the records' own text, so step 2 checks it with `iadd pr-body
        --check` and withholds on any exit but 0, naming what the command
        printed. Step 2 names the command, the exit code it waits on, the
        verdict line and the constant that holds the line; that steps 2 and 4
        and *Never* then read only the orchestrator's part as a party is the
        proofer's to read."""
        step_2 = between(INSPECTOR, "2. **", "3. **")
        pinned = [
            # The command the inspector runs on the body file.
            "`iadd pr-body <item> --body <file> --check`",
            # The exit code the inspector waits on before it reads on.
            "exit 0",
            # The verdict line `lib/fields.py` parses, as the inspector writes it.
            "`Verdict: withheld reason: <the first line the command printed>`",
            # The citation of the constant that holds the line the inspector
            # splits the body at.
            "`skills/code-review/scripts/pr_body.py#HEADING`",
        ]
        missing = [phrase for phrase in pinned if phrase not in step_2]
        assert missing == [], missing

    def test_step_4_withholds_where_a_declared_crafter_left_no_phase_record(self):
        """#1376, *Scope* item 6. The implementer mark and notice went with
        the hooks the plugin directory will not register, and the inspector's
        reading of the parties holds the fact they reminded a session of:
        where `routing.md` declares `crafter`, each closed phase of
        `frame/plan.md` has its phase record, and a declared party that left
        none is a reason to withhold. The `Planning` row's `framer` is
        `chain_check.py`'s to read against the frame's mark."""
        step_4 = between(INSPECTOR, "4. **", "5. **")
        pinned = [
            # The file, the row and the answer the inspector reads, the row and
            # answer `lib/routing.py#parse` reads.
            "`routing.md`",
            "`Implementation`",
            "`crafter`",
            # The file whose Status cells the inspector reads for closed phases.
            "`frame/plan.md`",
            # The record the crafter leaves, as the inspector resolves its path.
            "`trail/phases/phase-N.md`",
            # The verdict word `lib/fields.py` reads.
            "`withheld`",
        ]
        missing = [phrase for phrase in pinned if phrase not in step_4]
        assert missing == [], missing

    def test_step_4_reads_a_records_only_fix_over_its_diff(self):
        """#1615, *Scope* item 2. A `fixed` finding of the last record whose
        own `location:` names a place in the work item's records, and whose
        commit touched them alone, has the inspector as its only reader by the
        core's row *No fix that no round reads* (#1632), so step 4 reads the
        records' diff since the last record's target and the other
        statements of each fact it changed, and withholds where HEAD
        contradicts a sentence. Which sentences that reads, and how a dated
        frame section reads, are the proofer's to read."""
        step_4 = between(INSPECTOR, "4. **", "5. **")
        pinned = [
            # The command the inspector runs to list what the pass wrote.
            "`git -C <root> diff <the last record's target>..HEAD -- "
            "agentory/threads/<item>/`",
            # The command the inspector runs to list a changed fact's other
            # statements.
            "`git -C <root> grep -n -F '<the fact's words>' -- agentory/threads/<item>/`",
            # The verdict word `lib/fields.py` reads, beside what it names.
            "a sentence HEAD contradicts, are each a disagreement like any "
            "other, and a `withheld` reason naming its coordinate",
        ]
        missing = [phrase for phrase in pinned if phrase not in step_4]
        assert missing == [], missing

    def test_step_4_reads_the_path_outside_the_records_a_records_only_fix_left(
        self,
    ):
        """#1632, *Scope* items 3 and 5. The core's row gives the inspector a
        records-only fix of a finding that names a record beside a path
        outside the records, so step 4 names the row in place of restating
        its condition, opens that path, and withholds where the finding
        asked for a change there that the fix did not make."""
        step_4 = between(INSPECTOR, "4. **", "5. **")
        pinned = [
            # The row that gives the fix to the inspector, in the words of
            # `THE_CORES_ROW` in `tests/text/test_the_rules_have_one_owner.py`.
            "the row *No fix that no round reads* of `skills/core/SKILL.md` "
            "*Judgment is not licence to skip a party* gives its fix to you",
            # The read of the path the fix left as the last round read it.
            "Where the finding's `location:` names a path outside "
            "`agentory/threads/<item>/`, the fix left that path as the last round "
            "read it: open it at HEAD and read whether the finding asked for a "
            "change there.",
            # The verdict word `lib/fields.py` reads, beside what it names.
            "A change the finding asked for outside the records and did not "
            "get is a disagreement like any other, and a `withheld` reason "
            "naming the path.",
        ]
        missing = [phrase for phrase in pinned if phrase not in step_4]
        assert missing == [], missing

    def test_the_orchestration_reads_whether_a_round_follows_off_the_check(self):
        """#1615, *Scope* item 4. Whether the core's row gives a fix pass to
        the inspector is what the chain check's `--worktree` read prints, so
        the orchestrator runs it once the round record is committed and
        spawns a round only where its output names the record with the
        words a verifying round is owed. The words come from the module, so
        a change to the check's line turns this red. When the orchestrator
        stops instead is the proofer's to read."""
        text = " ".join(
            (ROOT / "skills" / "code-review" / "orchestration.md")
            .read_text(encoding="utf-8")
            .split()
        )
        start = text.index("**Whether a round follows a fix pass is read off")
        paragraph = text[start : text.index("**You end the rounds", start)]
        # The command the orchestrator runs, as the proofer runs it at its
        # hand-back.
        assert (
            "`python3 skills/code-review/scripts/chain_check.py --baseline <base> "
            "--root <the branch worktree> --worktree`"
        ) in paragraph, paragraph
        # The words the check prints at a finding no round read, which the
        # orchestrator matches in that output, and the constant that holds
        # them.
        assert f'"{chain.VERIFYING_ROUND}"' in paragraph, paragraph
        assert "`skills/code-review/scripts/chain_check.py#VERIFYING_ROUND`" in (
            paragraph
        ), paragraph

    def test_the_inspection_rule_exempts_only_the_closing_records(self):
        """Round 1 of #969, finding 1. `chain_check.py#inspection` lets only
        `trail/gate.md` and `inspection.md` follow the commit the inspection
        names (`follows(..., only=CLOSING_RECORDS)`); an inspector told that any
        record of the work item may follow keeps an earlier verdict over a
        changelog or phase record it never read, and the check refuses it."""
        text = INSPECTOR.read_text(encoding="utf-8")
        start = text.index("**The inspection covers HEAD")
        rule = " ".join(text[start:].split("\n\n", 1)[0].split())
        # The two paths `chain_check.py#CLOSING_RECORDS` lets follow the
        # audited commit, which the inspector resolves to tell a commit that owes
        # a new audit; the code spans are the fact.
        assert (
            "other than one touching only the closing records, `trail/gate.md` "
            "and `inspection.md`, owes a new audit"
        ) in rule, rule

    def test_the_orchestration_quotes_the_gates_outputs_line(self):
        """Moved by #969 from the inspector with the run. The outputs directory
        is a line a reader learns from nowhere else, and the orchestrator who
        runs the gate is the one who quotes it. The other lines it quotes, and
        that the inspector carries none, are the proofer's to read. Since #1579
        the run's steps stand in `skills/code-review/gate-to-pull-request.md`."""
        text = " ".join(
            (ROOT / "skills" / "code-review" / "gate-to-pull-request.md")
            .read_text(encoding="utf-8")
            .split()
        )
        # The line `broad_gate.py` prints to stderr when it keeps its
        # outputs, which the orchestrator matches in the gate's output and
        # quotes.
        assert "`outputs kept under iadd-gate-<random>/`" in text


# --- the document that states the inspection ------------------------------------


class TestDocument:
    def test_the_inspection_section_points_at_steps_3_and_4(self):
        """T23: `docs/forms/the-inspection.md` *The inspection* points at the
        definition's steps 3 and 4 for the acts. Whether it lists any of them
        is the proofer's to read."""
        text = " ".join(DOCUMENT.read_text(encoding="utf-8").split())
        section = text.split("## The inspection", 1)[1]
        # The citation of `agents/inspector.md`'s steps 3 and 4, which a reader
        # resolves to the inspector's acts.
        assert "`agents/inspector.md` step 3" in section
        assert "step 4" in section
