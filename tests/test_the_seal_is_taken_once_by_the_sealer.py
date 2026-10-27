"""The seal is taken once, by the sealer, and what the documents say of it.

Issue #30. The stamp's own cases, `skills/verify/scripts/seal_stamp.py` one
class per function, are `tests/test_seal_stamp.py`, and the gate's,
`skills/verify/scripts/broad_gate.py`, are `tests/test_broad_gate.py`, since
#942.

Part 2 holds the cases about the gate command that read a document's prose,
which #923 places. Part 3 pins the agent and the owner sentences.
"""

import ast
import os
import re

import pytest
from conftest import load_module
from test_the_agent_contract_holds_the_universal_rules import HEADING

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GATE = os.path.join(ROOT, "skills", "verify", "scripts", "broad_gate.py")
RECORDER_SOURCE = os.path.join(
    ROOT, "skills", "verify", "scripts", "pytest_record", "specseal_pytest_record.py"
)


def gate_module():
    return load_module(GATE, "specseal_broad_gate_for_tests")


# =============================================================================
# Part 2 — the gate's prose, left for #923
# =============================================================================

ROW = "Broad gate"


def read_document(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as handle:
        return handle.read()


def refusal_over(tmp_path, name, table):
    """`missing_row` over a config written literally, with no helper between
    the case and the bytes. Every fixture in this region is malformed on
    purpose, so a builder that assembled a well-formed table and checked it
    read back would swallow the subject (`plan.md` *Every fixture here is
    malformed on purpose*)."""
    home = tmp_path / name / "seal"
    home.mkdir(parents=True)
    (home / "config.md").write_text(table, encoding="utf-8")
    return gate_module().missing_row(str(home))


def test_the_template_documents_the_commented_row_sentence():
    """S7's other half (contract rule 14): the sentence a person reads is stated
    where `templates/config.md` states the fenced one."""
    root = os.path.join(os.path.dirname(__file__), "..")
    with open(os.path.join(root, "templates", "config.md"), encoding="utf-8") as f:
        text = " ".join(f.read().split())
    assert "A row inside an HTML comment that closes is not a row either" in text
    assert "the refusal quotes that line and says it is commented out" in text


def test_the_template_names_every_inline_html_kind_it_reads_as_before():
    """#673's S10 (contract rule 14). The sentence tells a person which contexts
    are read as before, and the walk is unsure after any inline raw HTML a
    line leaves open, not after a comment opener alone. Each opener a
    person might write is named, and the old list's narrower phrase is gone."""
    root = os.path.join(os.path.dirname(__file__), "..")
    with open(os.path.join(root, "templates", "config.md"), encoding="utf-8") as f:
        text = " ".join(f.read().split())
    assert "after inline HTML a line leaves open" in text
    for opener in ("<" + "!--", "<![CDATA[", "<?", "<!DOCTYPE"):
        assert f"`{opener}`" in text, opener
    assert "or a tag started in the middle of a line" in text
    assert "after a `<" + "!--` in the middle of a line" not in text


def test_the_documents_state_the_fence_rule_the_refusal_points_at(tmp_path):
    """contract rule 14: a fix that changes what a person sees documents
    it and pins it, in the same commit.

    Two documents and one pointer. `templates/config.md` is the one home of
    what this table's format allows, and the refusal sends the reader to a
    named section of it — so the section has to still be there, and it has to
    say the thing the refusal is about. `skills/config/SKILL.md` step 3 is
    the coordinate that INVITES the shape: it tells a session to copy a block
    carrying a fenced example row and used to name no position for it.
    """
    template = open(
        os.path.join(ROOT, "templates", "config.md"), encoding="utf-8"
    ).read()
    skill = open(
        os.path.join(ROOT, "skills", "config", "SKILL.md"), encoding="utf-8"
    ).read()
    said = refusal_over(
        tmp_path,
        "pointer",
        "| Item | Value |\n|---|---|\n| Mode | shared |\n"
        f"```\n| {ROW} | bin/test -q |\n```\n",
    )

    section = "### What is refused, and what stays allowed"
    assert section in template, (
        f"the refusal points at a section that is not there:\n{said}"
    )
    assert section.lstrip("# ") in said, said
    for claim in (
        "A table inside a code fence is an example of this format",
        "outside every fenced code block",
        "runs to the end of the file",
    ):
        assert claim in template, f"`templates/config.md` does not say: {claim}"
    assert "The copied block lands BELOW the live table" in skill, (
        "the instruction that produces the shape still names no position for "
        "the block it copies"
    )


def test_this_repositorys_own_config_is_answered_exactly_as_before(tmp_path):
    """A11. The file this work item is about is in this repository, and every
    sentence above is a sentence about somebody else's file.

    `seal/config.md` here carries a `Mode` row and a `Broad gate` row and
    nothing the reader will not take, so all three answers are the ones it
    had before this work item: the mode, the command as the row wrote it, and
    no refusal to build at all. Run before and after each phase.
    """
    module = gate_module()
    config = module.load(module.CONFIG_READER, "specseal_config_for_this_case")
    home = os.path.join(ROOT, "seal")
    text = open(os.path.join(home, "config.md"), encoding="utf-8").read()

    assert config.declared_mode(home) == ("mode", "shared"), config.declared_mode(home)
    assert config.config_table(text)[1] == [], (
        "a refusal is built from this repository's own config:\n"
        f"{config.config_table(text)[1]}"
    )
    command = module.broad_command(home)
    assert command and f"| {ROW} | {command} |" in text, (
        f"the command the gate reads is not the row as written:\n{command}"
    )
    assert module.not_as_written(home, command) is None, command
    # Phase 2's half of the same question. This file carries no backticks at
    # all, so the fence rule removes no line of it and every answer above is
    # the one it had before #429 — asserted rather than assumed, because
    # `fenced_row` is what the new refusal is built from.
    assert module.fenced_row(home) is None, module.fenced_row(home)
    assert "```" not in text and "~~~" not in text, (
        "this repository's own config grew a fence, and the assertions above "
        "stop being about a file that has none. Its header comment does carry "
        "single backticks, which open nothing: a fence is a run of three"
    )


def test_the_documents_name_the_line_that_says_to_commit_the_cell():
    """S2's documentation (contract rule 14). The orchestrator is told
    what to do with the line — the commit is the orchestrator's act. Since
    #969 the sealer sees none of the gate's lines and is told no line's
    wording (`tests/test_the_sealer_guarantees.py::TestDefinition`)."""
    orchestration = " ".join(
        read_document(os.path.join("skills", "code-review", "orchestration.md")).split()
    )
    assert (
        "the report's last line says `broad-gate.md` is written and not committed: "
        "CI reads HEAD, so commit it before you push"
    ) in orchestration


def test_the_documents_say_where_the_panel_now_carries_each_name():
    """S6 for the panel (contract rule 14). Each sentence that named a
    row the panel lost, or the `gate` row printing on every stamp, says what
    the panel prints now."""
    broad = " ".join(read_document(os.path.join("docs", "the-broad-gate.md")).split())
    assert (
        "the panel's `gate` row reads `tree <version>` wherever the copy that ran "
        "is not byte for byte the copy invoked"
    ) in broad
    assert "panel's `gate` row reads `tree <version>` or `plugin <version>`" not in (
        broad
    )
    verify = " ".join(
        read_document(os.path.join("skills", "verify", "orchestration.md")).split()
    )
    # #832's S5a: the ref stands beside the commit on the `base` row.
    assert "names the ref beside the commit on the `base` row" in verify
    assert "names the ref on the row under the commit" not in verify
    # Round 1's 🟡 4 and ⬜ 5: the third arm, which fires on every seal an
    # installed copy older than #666 redirects, because it hands over no
    # invoked path to compare against. The sealer describes no panel row
    # since it became the guarantor (#923), so the documents that do are read.
    assert (
        "or where the tree's copy ran with no invoked copy named to compare against"
    ) in broad
    source = read_document(os.path.join("skills", "verify", "scripts", "broad_gate.py"))
    above = source.split("GATE_REL = ", 1)[0][-1500:].splitlines()
    comment = " ".join(" ".join(line.lstrip("# ") for line in above).split())
    assert "or where no invoked copy was handed over to compare" in comment


def test_the_docstrings_describe_the_letter_and_the_rows_it_carries():
    """#717, S7 for the code's own prose (contract rule 14). The stamp
    module's docstring describes the letter and the twin's characters rather
    than a rope and golds; the gate's module docstring and `panel`'s row
    diagram list the rows the panel carries now; the comment above
    `SAMPLE_ROWS` says which rows left. #832, the owner's frame and layout
    of 2026-10-07: the disc at the left and the text beside it with nothing
    painted outside the disc, the disc's mark a chart in a file of its own,
    the twin's letters the nine colours', and nothing names the parchment
    sheet, the 14-cell disc's four colours, the vector source, the area
    sampler, the corner overhang, a fleur-de-lis, a chart of stitches or the
    interim ring."""
    stamp = " ".join(
        read_document(
            os.path.join("skills", "verify", "scripts", "seal_stamp.py")
        ).split()
    )
    assert (
        "Two things side by side on the terminal's own background, and nothing "
        "else: at the left a wax disc with the disc's mark pressed into it"
    ) in stamp
    assert "a 28 x 28 chart in `seal-mark.txt` beside this file, read as data" in stamp
    assert "every cell exactly one of nine colours" in stamp
    assert "`m` its wax edge, `M n N` its rim lit, mid and dark, `.` its field" in (
        stamp
    )
    assert "nothing outside the disc is painted" in stamp
    for gone in (
        "lower right corner",
        "`M n` the rim's",
        "EMBLEM_D",
        "by area",
        "hangs",
        "half on and half off",
        "LILY_",
        "RIM_LIGHT",
        "RING_INSET",
        "24 cells",
        "nearest",
        "14 cells across",
        "four colours",
        "against its right edge",
        "parchment sheet, with",
        "`m` the disc's ring",
        "PARCHMENT",
        "SHEET_EDGE",
        "TEXT_LEFT",
        "PANEL_WIDTH",
    ):
        assert gone not in stamp, gone
    assert "fleur-de-lis" not in stamp and "stitch" not in stamp
    assert "cell's centre" not in stamp and "INTERIM" not in stamp
    assert "`o O` rope" not in stamp and "the lily's golds" not in stamp
    assert "ledger" not in stamp
    assert "Since #717 there is no blank row in it, no `chain`" not in stamp
    gate = " ".join(
        read_document(
            os.path.join("skills", "verify", "scripts", "broad_gate.py")
        ).split()
    )
    # #832's S5a: the module docstring and `panel`'s row diagram name the
    # rows the owner's design of 2026-10-07 put back.
    assert (
        "the suite's counts, the chain's exit, how many more steps CI runs "
        "than this run answers"
    ) in gate
    assert "the ledger's `ok` count, how many more steps" not in gate
    assert "CI also · <n> more steps absent without a hygiene workflow" in gate
    assert "chain ✓ exit <code> read off the chain's own check" in gate
    assert "workflow <n> of <m> not answered" not in gate
    assert "**A drawn panel says only what a `SEALED` stamp can say** (#717)" not in (
        gate
    )
    assert "**The result rows carry a `✓`, and the blank before them is a row**" in (
        gate
    )
    assert "**Separators are ASCII**" not in gate
    assert "No row is `None` since #717" not in gate


def test_the_documents_name_the_ci_also_row():
    """#717, S7 for the rows (contract rule 14). `skills/verify/orchestration.md`
    *A run says what it did not answer* and `agents/sealer.md` named the
    `workflow` row and its `<n> of <total> not answered` reading; both name
    the `CI also` row and its `<n> more steps` now, and the denominator is
    said to be on the stderr line. #832's S5a: the row's value leads with a
    dim `·`, the owner's mark for a row that is not a pass, and the value
    column is 41 wide."""
    verify = " ".join(
        read_document(os.path.join("skills", "verify", "orchestration.md")).split()
    )
    assert "the panel carries a `CI also` row, *· <n> more steps*, and" in verify
    # #940: the document carried a count of the steps a feature branch's run
    # leaves unanswered, and it went stale when a step left the workflow. The
    # gate prints the count; the document states no copy of it.
    assert "A run on a SpecSeal feature branch reads `CI also ·" not in verify
    assert "A feature seal of" not in verify
    assert "value is 41 columns and a step name is a sentence" in verify
    assert "value is 23 columns" not in verify
    assert "the panel carries a `workflow` row" not in verify
    # The sealer sees no output of the gate's (#969) and names no panel row
    # (#923).
    assert "the `workflow` count" not in " ".join(sealer_text().split())


def test_the_unmeasured_word_says_so_and_every_reader_is_told_it():
    """A9 (#747, contract rule 14), S15 (#789), and S19 (#825). The three
    reasons are text a person reads and acts on, so they are pinned whole,
    and each starts with the word that marks it unmeasured; the five the
    record replaced are asserted gone. Every document that tells a reader
    what the gate's words mean names `new?` beside the other two, so a sealer
    handing it on and a smith reading it are both told it is not `new`."""
    gate = gate_module()
    assert gate.NOT_MEASURED == "new? not measured"
    earns = (
        "A row earns the measured word by letting every pytest it runs load "
        "the gate's recorder: it adds to the PYTHONPATH and PYTEST_ADDOPTS the "
        "gate hands it rather than replacing them, and runs pytest in that "
        "environment rather than one it builds, through any wrapper"
    )
    # #825 round 3's 🟡 3 and round 4's 🟡 3: every cause of a missing
    # record the records cannot tell apart, never one of them as the only one.
    causes = (
        "the row started no pytest, because a part before its runner failed "
        "or it has none; none it started loaded the recorder; or the one that "
        "did could not write its record and warned 'specseal_pytest_record: no "
        "record written' in "
    )
    assert (
        "new? not measured: no pytest the row ran here left a record of the "
        f"gate's recorder ({causes}suite.txt), so this file is named only by a "
        f"FAILED line of suite.txt and the base was not run. {earns}"
    ) == gate.NO_RECORD_AT_HEAD
    assert (
        "new? not measured: the row ran once at the base, and no pytest it ran "
        f"there left a record of the gate's recorder ({causes}suite-at-base.txt; "
        f"records/ is beside it). {earns}"
    ) == gate.NO_RECORD
    # The reframe's S27: what the record at `HEAD` left out is counted, and
    # the failure form says how many.
    assert gate.UNPLACED.format(count=1) == (
        "1 of the tests and collections the row's pytest reported had no file "
        "of their own and are in no list: a test a conftest or a plugin parents "
        "to the session or to a directory, a failed collection of the whole "
        "session, or a report a plugin built without its path (counted as "
        "unplaced on the end line of each record under records/)"
    )
    # #825 round 4's 🟡 2, the part its fix left: `new` from a base record
    # that left anything out is not measured.
    assert gate.UNPLACED_AT_BASE.format(count=2) == (
        "new? not measured: the row ran once at the base, and its sessions that "
        "ended non-zero left 2 of the tests and collections their pytest "
        "reported in no list, such as "
        "a test whose xdist worker died before any report of it arrived, so one "
        "of them may be this file's failure and whether the base fails it was "
        "not measured (kept as suite-at-base.txt, with records/ beside it)"
    )
    # #849 (#825 round 6's 🟡 1): `new` from a base one of whose sessions
    # stopped part-way is not measured either -- and #849 round 1's 🟡 1: a
    # session pytest stopped itself is one.
    # #852: the stops the `end` line now names are among the causes.
    assert gate.UNENDED_AT_BASE.format(count=1) == (
        "new? not measured: the row ran once at the base, and 1 of its pytest "
        "sessions stopped part-way, because the process died or the recorder "
        "stopped writing before the session's end line, or pytest stopped the "
        "session (an interrupt, pytest.exit(), -x or --maxfail, a plugin's "
        "stop) or ended it on an error of its own, so this file's tests there "
        "may not have finished and whether the base fails it was not measured "
        "(kept as suite-at-base.txt, with records/ beside it)"
    )
    # #849 round 1's 🟡 2: the same at `HEAD`, under the list.
    assert gate.UNENDED_HERE.format(count=1) == (
        "1 of the row's pytest sessions here stopped part-way, because the "
        "process died or the recorder stopped writing before the session's end "
        "line, or pytest stopped the session (an interrupt, pytest.exit(), -x "
        "or --maxfail, a plugin's stop) or ended it on an error of its own, so "
        "a test it stopped in may be in no list and the tests it never reached "
        "are in none (each session's record is under records/)"
    )
    # #869: a line of a keyed record that did not parse, at the base and
    # under the list at `HEAD`.
    assert gate.UNREAD_AT_BASE.format(count=1) == (
        "new? not measured: the row ran once at the base, and 1 of the lines "
        "in the records its pytest wrote there did not parse as the recorder's "
        "and each was passed over, so one may have held this file's failure "
        "and whether the base fails it was not measured (kept as "
        "suite-at-base.txt, with records/ beside it)"
    )
    assert gate.UNREAD_HERE.format(count=1) == (
        "1 of the lines in the records the row's pytest wrote here did not "
        "parse as the recorder's and each was passed over, so a failing test "
        "may be in no list and the suite's counts are not given (each "
        "session's record is under records/)"
    )
    with open(RECORDER_SOURCE, encoding="utf-8") as handle:
        assert "specseal_pytest_record: no record written" in handle.read()
    assert gate.NOT_REACHED.format(code=2) == (
        "new? not measured: the row ran once at the base and exited 2, and no "
        "pytest it ran there collected this file, so the run may have ended "
        "before reaching it and whether the base fails it was not measured "
        "(kept as suite-at-base.txt, with records/ beside it). A file the "
        "branch added reads this way wherever the base's own row already fails"
    )
    for retired in (
        "NO_RUNNER",
        "NOT_ENDED",
        "COLLECTED_BEYOND",
        "MULTI_RUNNER",
        "COMPANY",
        "row_prefixes",
        "report_counts",
        "proof_refused",
        "JUNIT_REPORT",
        "COLLECT_ONLY",
    ):
        assert not hasattr(gate, retired), f"broad_gate.py still carries {retired}"
    readers = {
        # #969: the orchestrator meets the gate's words now, not the sealer.
        ("skills", "code-review", "orchestration.md"): "`new?`",
        ("agents", "smith.md"): "`new?` means nothing at the base measured that file",
        ("skills", "verify", "orchestration.md"): "**New?**",
        ("README.md",): "new? → not measured at the base",
        ("README.ko.md",): "new? → base 에서 재지 못했다",
        ("templates", "config.md"): "each file reads `new?` with the reason",
    }
    for parts, phrase in readers.items():
        with open(os.path.join(ROOT, *parts), encoding="utf-8") as handle:
            assert phrase in handle.read(), f"{'/'.join(parts)} does not name `new?`"
    # #825: the reader sent to the base by hand is told the three causes the
    # record leaves, and to open the one kept run and its records.
    with open(
        os.path.join(ROOT, "skills", "verify", "orchestration.md"), encoding="utf-8"
    ) as handle:
        bullet = " ".join(handle.read().split())
    for phrase in (
        # #825's reframe after round 3 and round 4's 🟡 3: every cause of a
        # missing record.
        "no pytest the `Broad gate` row ran left a record, because the row "
        "started no pytest, none it started loaded the gate's recorder, or the "
        "one that did could not write its record and warned in `suite.txt`, so "
        "the file is named only by a `FAILED` line and the base was not run",
        "no pytest the row ran at the base left a record, for any of those three "
        "causes, a part before the runner failing at the base among them",
        "A test with no file of its own is in no list at all, nor is a failed "
        "collection of the whole session or a report a plugin built without its "
        "path; the failure form says how many there were.",
        "the row's run at the base exited non-zero before any pytest collected "
        "the file, which is also how a file the branch added reads where the "
        "base's row already fails",
        "open the kept `suite-at-base.txt` and the `records/` beside it",
        # #825 round 5's 🟡 2: only a session of the base that ended non-zero.
        "or a session of the base that ended non-zero left tests or collections "
        "out of every list, a test whose xdist worker died in its setup among "
        "them, so the record cannot say the file passed.",
        # #849 (#825 round 6's 🟡 1): a session of the base with no end, and
        # #849 round 1's 🟡 1: one whose end shows pytest stopped it.
        # #852: one whose end line says pytest stopped it.
        "A session of the base that stopped part-way reads the same way: its "
        "record holds no `end` line, because the process died, which plain "
        "pytest does on a test that calls `os._exit`, or its recorder "
        "stopped writing; or its `end` line names a stop pytest made, which an "
        "interrupt, any `pytest.exit()`, `-x`, `--maxfail` and a plugin's stop "
        "all leave, or an exit outside 0, 1 and 5.",
        # #869: a line of the base's record that did not parse.
        "So does a base whose record holds a line that did not parse as the "
        "recorder's, which the gate counts and passes over.",
        # #849 round 1's 🟡 2 and #869: a session at `HEAD` that stopped
        # part-way, and a line of its record that did not parse.
        "Nor, where a session at `HEAD` stopped part-way, is the test it "
        "stopped in, nor a test named on a line of the record that did not "
        "parse; the failure form counts both too.",
        "how a row earns the measured word",
    ):
        assert phrase in bullet, f"the **New?** bullet does not carry: {phrase}"
    for gone in (
        "wrote the report the gate asked pytest for there",
        "the file's run alone ended without naming a failing test",
        "`collected-at-base-*.txt`",
        # One cause of a missing record named as the only one (#825 round 3).
        "row ran loaded the gate's recorder, so the file is named only",
        "no pytest the row ran at the base loaded the recorder",
        # Two causes named as though they were every one (#825 round 4).
        "for either of those causes",
        # Every base record's count, a green session's included (round 5).
        "or the base's record left tests or collections out of every list",
        # A missing `end` line named as the only stop (#849 round 1).
        "A session of the base that wrote no `end` line to its record reads "
        "the same way",
        # The stops read off the exit alone (#852).
        "as a `KeyboardInterrupt` or `pytest.exit()` in a test and xdist under "
        "`-x` give",
    ):
        assert gone not in bullet, f"the **New?** bullet still carries: {gone}"
    with open(GATE, encoding="utf-8") as handle:
        docstring = ast.get_docstring(ast.parse(handle.read()))
    assert "`new?` with the reason no run measured it" in docstring
    # The module docstring's paragraph on the comparison says how it measures
    # now, and no longer names the prefixes or the JUnit report.
    flat_doc = " ".join(docstring.split())
    assert "run the row there once, unchanged, with the recorder loaded again" in (
        flat_doc
    )
    assert "No line pytest printed decides a word" in flat_doc
    assert "running each prefix of the row" not in flat_doc
    assert "JUnit" not in flat_doc


def test_the_measurement_its_cost_and_its_limits_are_told_where_the_row_is_written():
    """S15 of #789 and S19 of #825 (contract rule 14). Rule 3 is the one home of
    how the gate measures a row at the base, what that costs, and which rows
    it cannot measure, so each sentence a reader acts on is pinned there, and
    every sentence of the mechanism #825 retired is asserted gone."""
    with open(os.path.join(ROOT, "templates", "config.md"), encoding="utf-8") as handle:
        text = handle.read()
    for sentence in (
        "| 3 | Every pytest the row runs keeps the environment the gate hands it |",
        "On a failing test the gate compares each failing file with the base "
        "from a record, never from what pytest printed.",
        "the recorder's directory first on `PYTHONPATH`, `-p "
        "specseal_pytest_record` appended to `PYTEST_ADDOPTS`, and a key made "
        "fresh for the run.",
        "A pytest a test starts, and an xdist worker, inherit no key and write "
        "nothing, so nothing a test prints or runs changes a word.",
        "**Then the row runs once more, unchanged, at the base** (nothing "
        "appended, no part cut, every part run as written)",
        "where no pytest at the base left a record (the row ended before it "
        "started one, none loaded the recorder, "
        "or the one that did could not write its record and warned in "
        "`suite-at-base.txt`), `new?`; where the "
        "base's record holds a failing test or a failed collection of the file, "
        "`failing on base too`; where it holds the file and nothing of it "
        "failed, `new`; where it does not hold the file and the row exited 0, "
        "`new`, because the row ran to its end and never collected the file; "
        "and where it does not hold the file and the row exited otherwise, "
        "`new?` naming the exit, because the run may have ended before reaching "
        "it; so a file the branch added reads `new?` wherever the base's row "
        "already fails.",
        "Where no pytest the row ran at `HEAD` left a record, for any of "
        "those causes, the files "
        "come from its `FAILED` lines, each file reads `new?` with the reason, "
        "and the base is not run; where one runner loaded it and another did "
        "not, the other's failures stay in `suite.txt` and out of the list.",
        # #825 round 4's 🟡 2, narrowed by round 5's: `new` from a base
        # session that ended non-zero and left anything out, and the limit.
        "Either `new` reads `new?` naming the count instead where a session of "
        "the base that ended non-zero left any test or collection out of every "
        "list, because one of them may be the file's failure: a test whose "
        "xdist worker died in its setup, before any report of it reached the "
        "controller, is one. A session that exited 0 failed nothing, so what it "
        "left out cannot be. One over-strictness is named rather than closed: a "
        "red session whose left-out reports all passed, such as a passing item "
        "a conftest parents to the session, still turns `new` into `new?`.",
        # #849 (#825 round 6's 🟡 1): a base session that stopped part-way,
        # #849 round 1's 🟡 1: one pytest stopped itself, and #852: the stop
        # read off the `end` line, which closes the two #849 left named.
        "Either `new` reads `new?` naming the count, too, where a session of "
        "the base stopped part-way, so the file's tests there may not have "
        "finished: it wrote no `end` line to its record, because its process "
        "died, as plain pytest does on a test that calls `os._exit` or "
        "segfaults, or its recorder stopped writing, a disk that filled among "
        "the causes; or its `end` line says pytest stopped it (an interrupt, "
        "`pytest.exit()` whatever code it chose, `-x` or `--maxfail`, a "
        "plugin's stop) or shows an exit other than 0, 1 and 5. Where a red "
        "session also left reports out, that count is the one named.",
        # #849 round 1's 🟡 2: the same stop at `HEAD`, counted.
        "The gate also says there how many sessions at `HEAD` stopped "
        "part-way, because the test such a session stopped in may be in no "
        "list.",
        "**The cost is one more run of the whole row, and only when the suite "
        "fails**, whatever the number of failing files.",
        "so a part after the runner that the branch's own run never reached, "
        "because `&&` stopped at its failing suite, runs at the base wherever "
        "the base's suite passes,",
        "So the runner may come first or last, and the order is the "
        "repository's trade: either way the row runs once, whole, at the base.",
        "**A row earns the measured word** by letting every pytest it runs load "
        "the recorder: it adds to the `PYTHONPATH` and `PYTEST_ADDOPTS` the "
        "gate hands it rather than replacing them, and runs pytest in that "
        "environment rather than in one it builds.",
        "A runner started by `tox`, `nox`, `env -i`, a container or a wrapper "
        "that rebuilds the environment without either variable writes no "
        "record, and so does a row that sets `PYTEST_ADDOPTS` to a value of its "
        "own; its files read `new?`.",
        # #825 round 1's 🟡 2: Q2's class, not its first instance.
        "A row that keeps `PYTEST_ADDOPTS` and loses `PYTHONPATH` fares worse "
        "(one that replaces `PYTHONPATH`, an interpreter run with `-I` or `-E`, "
        "a wrapper that passes `PYTEST_ADDOPTS` or `PYTEST_*` on and not "
        "`PYTHONPATH`): pytest cannot import the module the `-p` names and exits "
        "1 before any test runs, so the row fails at the gate.",
        "and passes `PYTHONPATH` on wherever `PYTEST_ADDOPTS` goes.",
        # #825's reframe after round 3 (S28): what a line names a file by,
        # and the two kinds of report the record leaves out.
        "The record names each file by the path pytest itself holds for the "
        "test or the collector, read in the process that holds it (an xdist "
        "worker too) and carried on the report, never by a name pytest made "
        "from that path, so a file outside the rootdir, a `--pyargs` module "
        "wherever Python imports it from and a collector a conftest builds are "
        "each named by their own path.",
        # #825 round 4: the session's failed collection, a crashed worker's
        # test, and the attribute a whole-report log carries.
        "It leaves three kinds of report out of every list, counts them on the "
        "record's `end` line, and the gate says how many under the failing "
        "files: a test with no file of its own, which a conftest "
        "or a plugin parents to the session or to a directory; a failed "
        "collection of the whole session, which is where pytest 7 lays a "
        "conftest's import error anywhere below the root; and a report "
        "that reached the recorder without its path, one a plugin built or "
        "rebuilt itself, unless the same xdist worker's last report was of the "
        "same test and not its teardown, as a test whose worker crashed in its "
        "body has; a report's node id alone never places it, because two tests "
        "can share one.",
        "so a plugin that writes reports whole, pytest-reportlog's "
        "`--report-log` among them, writes it into the row's own log while the "
        "gate measures the row.",
        "One limit is named rather than closed: a test written to append to the "
        "record file the recorder is writing, or to write a record of its own "
        "with the gate's key, can put a line into a keyed record |",
    ):
        assert sentence in text, f"rule 3 does not carry: {sentence}"
    for gone in (
        "The suite runner is a part of the row a cut can stop after",
        "until one writes that report",
        "--junitxml=<path>",
        "--collect-only",
        "A group of several failing files never earns",
        "The proof run",
        "proof run",
        "verbosity_test_cases",
        "#816 would mark",
        "until one prints pytest's summary line",
        "A runner with `-s` lets a test write to stderr",
        "One shape the gate cannot see through",
        "or reaches without the gate's environment**",
        "Two dependencies in one group whose counts cancel",
        "fewer tests than they fail one by one",
        "(`pytest -q tests`, `pytest -q tests/unit`)",
        # #825 round 1: one row of Q2's class named as though it were all of
        # it, and a forged record called the only way to the wrong word.
        "A row that replaces `PYTHONPATH` and keeps `PYTEST_ADDOPTS` fares",
        "and that is the one way to a wrong `failing on base too`",
        # #825 round 2: the refusal named by its path arguments alone, and
        # its files said to read `new?` wherever another runner recorded.
        "A pytest handed a path outside its rootdir — `-c` or `--rootdir` "
        "elsewhere, or a config file in one of its arguments' directories — "
        "names those files",
        "writes no record and its files read `new?`.",
        # #825's reframe after round 3: the refusal of a pytest naming files
        # outside its rootdir, and the limit that called it closed.
        "A pytest that names a file outside its rootdir",
        "so it writes no record, and its files are measured as a runner's",
        "builds a collector for a path no argument contains",
        "the refusals above close every branch",
        "no third way is known",
        # #825 round 3's 🟡 3: one cause of a missing record named as the only.
        "where no pytest at the base loaded the recorder, `new?`",
        "Where no pytest the row ran at `HEAD` loaded the recorder",
        # #825 round 4: two causes and two kinds named as though every one.
        "for either of those causes",
        "It leaves two kinds of report",
        # #825 round 5: the lookup by node id, and the count of every session.
        "unless an earlier report of the same test carried it",
        "where the base's record left any test or collection out of every list",
        # #849 round 1's 🟡 1: a missing `end` line named as the only stop.
        "where a session of the base wrote no `end` line to its record, because "
        "it stopped part-way",
        # #852: the stops read off the exit alone, and the two it left open,
        # which the `end` line's `stopped` closes.
        "a failed collection without `-x` and xdist under `-x` give",
        "Two stops are named rather than closed",
        "which leaves no file partly run only while each file's tests run together",
    ):
        assert gone not in text, f"rule 3 still carries: {gone}"


def test_what_a_line_names_a_file_by_is_told_where_each_reader_meets_it():
    """S28 (#825's reframe after round 3, contract rule 14). A line's path is
    the node's own, carried on the report, and never a name made from a
    node id and a rootdir. The comparison's docstring, the recorder's own
    and the released changelog entry each say so by their deciding sentence, and
    each sentence of the refusal the reframe retired is asserted gone."""
    gate = gate_module()
    docstring = " ".join(gate.compare_at_base.__doc__.split())
    assert (
        "Each line names its file by the path pytest holds for the test or the "
        "collector, carried on the report from the process that held it, and "
        "never by a name pytest made from that path"
    ) in docstring
    recorder = " ".join(
        read_document(
            os.path.join(
                "skills",
                "verify",
                "scripts",
                "pytest_record",
                "specseal_pytest_record.py",
            )
        ).split()
    )
    for sentence in (
        "A line's path is the node's own: `item.path` for a test, the module "
        "that COLLECTED it, and `collector.path` for a failed collection",
        "No path is ever made from a node id and a rootdir",
        "None of the three is written; each node is counted once on the `end` "
        "line, and the gate says the count under its list of failing files.",
        # #825 round 4: the session's failed collection, and the path an
        # earlier report of a node carried, reused for a crash report.
        "a failed collection of the session itself -- where pytest 7 lays a "
        "conftest's import error anywhere below the root",
        "unless the same xdist worker's last report was of the same node and "
        "not its teardown",
        "Never a lookup by node id alone: two nodes can share one",
        "`--report-log` writes what `pytest_report_to_serializable` returns",
        "it looks no module up and imports nothing but pytest",
    ):
        assert sentence in recorder, f"the recorder does not carry: {sentence}"
    # The work item's fragment is read where the release gathered it: in
    # `changelog/0.20.0.md`, from its `specs/<id>` comment up to the next
    # fragment's comment.
    marker = "<!-- specs/1791270161-the-broad-gate-reads-a-record-its-pytest-plugin-wrote -->"
    released = read_document(os.path.join("changelog", "0.20.0.md"))
    assert released.count(marker) == 1, (
        f"changelog/0.20.0.md does not hold {marker} once"
    )
    span = released.split(marker)[1].split("<!-- specs/")[0]
    changelog = " ".join(span.split())
    for sentence in (
        "**Each failing file is named by the path pytest holds for it.**",
        "counted on the record's `end` line, and the gate says how many under "
        "the failing files.",
        "names every cause the gate cannot tell apart: the row started no "
        "pytest, none it started loaded the recorder, or the one that did could "
        "not write its record.",
        "whose xdist worker crashed in its body keeps the path its `setup` report "
        "carried from that same worker, so its failure counts; a crash is never "
        "placed by a node id two tests can share.",
        "`new?` naming a count, too, where the file would read `new` but a "
        "session of the base that ended non-zero left tests or collections out "
        "of every list",
        "A red session whose left-out reports all passed still gives `new?`: a "
        "known over-strictness.",
        "a row that writes `--report-log` finds it in that log while the gate "
        "measures it.",
    ):
        assert sentence in changelog, f"the changelog does not carry: {sentence}"
    for gone, text in (
        ("so it writes no record at all", docstring),
        ("the recorder's refusals close it", docstring),
        ("A path is the rootdir joined to `report.fspath`", recorder),
        ("therefore writes no record at all", recorder),
        ("an_argument_lies_outside_the_rootdir", recorder),
        ("find_spec", recorder),
        ("A pytest that names a file outside its rootdir writes no record", changelog),
        ("Such a row's files are not measured", changelog),
        ("where no pytest at the base loaded the recorder", changelog),
        ("Where no pytest of the row loaded the recorder at all", changelog),
        ("names both causes", changelog),
        # #825 round 5: the lookup by node id, and every session's count.
        ("an earlier report of the same node in the session carried", recorder),
        ("keeps the path its earlier reports carried", changelog),
        ("base's record left tests or collections out of every list", changelog),
    ):
        assert gone not in text, f"still carried: {gone}"


# =============================================================================
# Part 3 — the owner, and the fourth definition
# =============================================================================

# `agents/smith.md` and `agents/warden.md` each carried the rule with no owner
# in it: *the full suite is the orchestrator's*. #30 named the sealer in both.
# Both were written anew since (#957, #967) and name no runner: the run's
# owner moves from the sealer to the orchestrator in #969, and contract rule 2 is
# where a reader finds it. What each definition still owes is the coverage
# probe, in its own words. The warden's words are #985's absence rule: a
# claim that nothing catches a finding is a probe, named on the finding's
# `evidence: executed` line.
SEALER = os.path.join(ROOT, "agents", "sealer.md")
PROBE = {
    "smith.md": (
        "Asking whether the suite catches something is a coverage probe, a "
        "different act: run it over the module that should catch it and "
        "report it as a probe."
    ),
    "warden.md": (
        "A claim of absence, such as nothing in the suite catching this, is a "
        "probe: run it over the module that should catch it, report it as a "
        "probe, never as a seal, and name it on the finding's `evidence: "
        "executed` line."
    ),
}

# Contract rule 2 and contract rule 6, read from the contract rather than
# typed, so a rule that is rewritten (#120) is compared as it then stands.
CONTRACT = os.path.join(ROOT, "skills", "agent-contract", "SKILL.md")

# `tests/test_a_moved_rule_leaves_its_definition.py` measured this: 15 words is
# longer than any phrase a kept application shares with a section, and shorter
# than the smallest real paste. Imported as a number rather than a rule — the
# case below applies it to ONE definition, the one that talks about rule 2 by name
# and is therefore the one at risk of quoting it.
WINDOW = 15


def agent(name):
    with open(os.path.join(ROOT, "agents", name), encoding="utf-8") as handle:
        return " ".join(handle.read().split())


def sealer_text():
    with open(SEALER, encoding="utf-8") as handle:
        return handle.read()


def section(number):
    """The body of `## <N>` in the contract, heading excluded."""
    with open(CONTRACT, encoding="utf-8") as handle:
        text = handle.read()
    heads = list(HEADING.finditer(text))
    for index, match in enumerate(heads):
        if int(match.group(1)) != number:
            continue
        end = heads[index + 1].start() if index + 1 < len(heads) else len(text)
        return " ".join(text[match.end() : end].split())
    raise AssertionError(f"the contract has no rule {number}")


# --- S6 the owner ------------------------------------------------------------


@pytest.mark.parametrize("definition", sorted(PROBE))
def test_the_definition_separates_a_coverage_probe_from_a_seal(definition):
    """The near miss a rule against the full suite creates. *Does anything in
    the suite catch this* is answered by running the suite, and an agent that
    reads only *the full suite is not yours* either does not ask it or reports
    the answer as a seal. It is a probe: run it, and label it one."""
    assert PROBE[definition] in agent(definition), (
        f"agents/{definition} does not separate a coverage probe from a seal, "
        "so the one run that is not a seal has no name"
    )


def test_the_warden_says_what_comes_due():
    """The warden's report is what ends the rounds, so it is the one segment
    positioned to say the gate is next. Saying so without naming what is
    spawned leaves the orchestrator to remember the sealer exists."""
    warden = agent("warden.md")
    assert (
        "what comes due is the orchestrator's broad run, and the sealer's "
        "spawn after it"
    ) in " ".join(warden.split()), (
        "the warden says the broad run is next and does not say who takes it"
    )


# Every party that could be written in as the broad gate's runner. A runner
# named in the smith's definition is a sentence #969 makes false by moving the
# run, from a worktree that does not touch this file (`spec.md` decision 6 of
# work item 1792251842).
RUNNERS = ("sealer", "orchestrator", "warden", "framer", "scribe", "session", "owner")
# A sentence anywhere in the file that hands the run to somebody: a party, then
# a verb of taking it, then the run, inside one sentence.
HANDS_THE_RUN = re.compile(
    r"\b(?:" + "|".join(RUNNERS) + r")s?\b[^.]{0,60}?\b(?:takes?|runs?|owns?)\b"
    r"[^.]{0,40}?\b(?:broad gate|full suite)",
    re.I,
)


def test_the_smith_names_no_runner_of_the_broad_gate():
    """T4 of #967 (S5): the smith says it does not run the broad gate and
    names nobody who does; contract rule 2 holds who does.

    This replaced a case that asserted *Then the sealer takes the broad gate
    once*. #969 moves the run to the orchestrator in a worktree beside this
    one, so either owner written here is false in one of the two trees."""
    smith = agent("smith.md")
    start = smith.index("**The broad gate is not yours, and its label is.**")
    rule = smith[start : smith.index(" check: ", start)]
    assert "You do not run the full suite, the lint or the typecheck" in rule, (
        "the smith's gate rule stopped saying the run is not the smith's"
    )
    assert "rule 2 holds who does" in rule, (
        "the rule stopped pointing at where the runner is named"
    )
    named = [party for party in RUNNERS if re.search(rf"\b{party}", rule, re.I)]
    assert not named, f"the smith's gate rule names {named}: {rule}"
    handed = HANDS_THE_RUN.findall(smith)
    assert not handed, f"`agents/smith.md` hands the broad gate to somebody: {handed}"


# --- S7 the fourth definition ------------------------------------------------
#
# The contract paragraph this file opens with is held to byte identity by
# `tests/test_every_agent_reads_the_contract.py`, over a glob this file joins
# on the day it lands. Re-pinning it here would be the duplication that module
# and `tests/test_a_moved_rule_leaves_its_definition.py` exist to refuse, so
# what part 3 pins is what no existing module reads.


def test_the_fourth_definition_exists():
    assert os.path.exists(SEALER), "agents/sealer.md is not in the tree"


def test_the_sealer_preloads_the_contract_and_nothing_else():
    """Q5: its whole procedure is one command, and #292 measured every
    preloaded body as a cost paid again on every spawn. `verify` is 35 KB for
    four conditions the definition states in four lines."""
    head = sealer_text().split("\n---\n", 1)[0]
    assert re.findall(r"^  - (\S+)", head, re.M) == ["agent-contract"], (
        "the sealer's `skills:` list is not `agent-contract` alone, so a body "
        "rides every spawn for a procedure that is one command"
    )


def test_the_sealer_names_the_one_write_its_definition_is_allowed():
    """Contract rule 6 says what an agent writes is named in its own definition
    and nothing else, so this file is the whole of the sealer's permission. A
    write nobody named is a review that certifies itself.

    Before #120 the same case read `as its own exception`, because rule 6 carved
    exceptions and pointed at the definition holding each one. The mechanism
    did not move -- it stopped being the exception and became the rule -- so
    every assertion below is unchanged and only the name and the grounds are.

    Since the sealer became the guarantor (#923) its one write is
    `guarantee.md`, and `broad-gate.md` is the gate's, through its command."""
    text = " ".join(sealer_text().split())
    assert "rule 6" in text, "the sealer cannot reach the rule that names its one write"
    assert "through `broad-gate --record`" in text, (
        "the gate's file does not name the command that makes it, so the "
        "sealer cannot tell its own write from the gate's"
    )
    assert "`guarantee.md` is the whole of what you may write" in text, (
        "the permission does not say WHICH file, and a permission without a "
        "boundary is a general one"
    )


def test_the_sealer_leaves_s6s_withheld_acts_to_s6():
    """Round 1, finding 10 of #120 found the definition reciting contract
    rule 6's withheld acts one short and one over, and this case held the
    recitation to that rule's own list. #943 removed the recitation: rule 6
    binds every agent
    whatever its file says, and the copy cost the sealer's preload bytes its
    measurement refused (round 1 of #943).

    Rewritten rather than deleted, for the reason the case below gives: a
    case removed with the passage it pinned leaves nothing to notice the
    passage coming back. A recitation that returns is a second source beside
    a countable list, so the assertions invert."""
    text = " ".join(sealer_text().split())
    assert "rule 6 withholds stays withheld" not in text, (
        "the sealer recites rule 6's withheld acts again; rule 6 is their one source"
    )
    assert "nothing posted, nothing pushed" not in text, (
        "the sealer recites rule 6's withheld acts again; rule 6 is their one source"
    )


def test_the_window_the_sealer_shipped_under_is_closed():
    """#120 closed it, and this case is the one that says so.

    The sealer shipped under a contract rule 2 that forbade its one act, for a window
    inside one release branch, and its definition wrote the contradiction down
    rather than leaving the next reader to guess which document wins. That
    paragraph carried its own expiry -- *when #120 lands, this section is the
    paragraph it deletes* -- and #120 deleted it.

    Rewritten rather than deleted, and that is the point of it. A case removed
    with the paragraph it pinned leaves nothing to notice the paragraph coming
    back, and this one came with a ticket number in it, which is exactly the
    prose a later session restores while tidying. So the assertions invert:
    the window's own words are absent, and what the section was standing
    against is now a positive assignment.

    The two facts `spec.md` requires the definition to keep -- rule 6 and the one
    cell -- are asserted by
    `test_the_sealer_names_the_one_write_its_definition_is_allowed` above, which
    is where they belong; repeating them here would make two cases fail for one
    edit and neither of them say which."""
    text = " ".join(sealer_text().split())
    assert "narrower document" not in text, (
        "the window paragraph is back. It says the definition wins over the "
        "contract, which was true only while rule 2 forbade the sealer's one act"
    )
    assert "#120" not in text, (
        "the definition still names the ticket that was to settle rule 2. #120 "
        "has landed, so a reader following it finds a closed issue and no "
        "contradiction to match it against"
    )
    assert "rule 2 as it stands" not in text, "the section heading survived"
    assert "rule 2" in text, (
        "the definition stopped citing rule 2 altogether, so the sealer meets the "
        "rule that keeps the run out of its hands nowhere in its own file"
    )
    # #969 moved the run to the orchestrator: the positive assignment is now
    # contract rule 2's and the orchestration's, and the sealer's file says
    # whose it is.
    assert "spawned for exactly that" not in text, (
        "the sealer's assignment of the run is back beside a rule 2 that gives "
        "the run to no agent"
    )
    assert "the orchestrator runs it" in text, (
        "the definition says the run is not the sealer's without saying whose "
        "it is, which is #30's opening: an act nobody holds"
    )


def test_the_sealer_carries_the_four_conditions_in_its_own_words():
    """Q5 again, from the other side: dropping `verify` from the spawn is only
    correct if the conditions arrive some other way."""
    text = " ".join(sealer_text().split())
    for condition in (
        "Name the command before you run it",
        "show the check can fail",
        "Bind the result to a tree state",
        "`executed`",
        "`unverified`",
    ):
        assert condition in text, (
            f"the sealer's definition does not carry `{condition}`, and "
            "`verify` is not in its `skills:` list to carry it instead"
        )


@pytest.mark.parametrize("number", (2, 6))
def test_the_sealer_cites_the_section_without_carrying_it(number):
    """The sealer is the one definition that talks about contract rule 2 and
    contract rule 6 by name, so
    it is the one at risk of quoting them. Citing a number and saying what it
    means for this role is the application form; a run of the section's own
    words is the paste `tests/test_a_moved_rule_leaves_its_definition.py`
    measured, and that module holds the whole glob to it."""
    body = section(number).split()
    text = " ".join(sealer_text().split())
    copied = [
        " ".join(body[i : i + WINDOW])
        for i in range(len(body) - WINDOW + 1)
        if " ".join(body[i : i + WINDOW]) in text
    ]
    assert not copied, (
        f"agents/sealer.md carries contract rule {number}'s own words: {copied}"
    )
