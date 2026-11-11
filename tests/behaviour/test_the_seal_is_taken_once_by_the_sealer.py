"""The seal is taken once, by the sealer, and what the documents say of it.

Issue #30. The stamp's own cases, `skills/verify/scripts/seal_stamp.py` one
class per function, are `tests/skills/test_seal_stamp.py`, and the gate's,
`skills/verify/scripts/broad_gate.py`, are `tests/skills/test_broad_gate.py`, since
#942.

Part 2 holds the cases about the gate command that read a document's prose
or this repository's config. Part 3 holds the cases that read the agent
definitions.
"""

import os
import re

import pytest
from conftest import ROOT, load_module

GATE = os.path.join(ROOT, "skills", "verify", "scripts", "broad_gate.py")
RECORDER_SOURCE = os.path.join(
    ROOT, "skills", "verify", "scripts", "pytest_record", "agentic_pytest_record.py"
)


def gate_module():
    return load_module(GATE, "agentic_broad_gate_for_tests")


# =============================================================================
# Part 2 — the gate's prose
# =============================================================================

KEY = "Broad gate"


def read_document(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as handle:
        return handle.read()


def test_this_repositorys_own_config_is_answered_exactly_as_before():
    """A11. The file this work item is about is in this repository, and every
    sentence above is a sentence about somebody else's file.

    `seal/config.json` here carries a `Mode` key and a `Broad gate` key and
    nothing the reader will not take, so all three answers are the ones it
    had before: the mode, the command as the key wrote it, and no refusal.
    """
    module = gate_module()
    config = module.sibling.load(module.CONFIG_READER)
    home = os.path.join(ROOT, "seal")

    assert config.declared_mode(home) == ("mode", "shared"), config.declared_mode(home)
    pairs, refusal = config.config_pairs(home)
    assert refusal is None, refusal
    command = module.broad_command(home)
    assert command and (KEY, command) in pairs, (
        f"the command the gate reads is not the key as written:\n{command}"
    )
    assert module.not_as_written(home, command) is None, command


def test_the_policy_names_the_value_the_gate_row_reads():
    """S6 for the panel (contract rule 14). The policy says what the panel's
    `gate` row prints now. When it prints it, where `skills/verify/orchestration.md`
    puts the ref on the `base` row, and the comments `broad_gate.py` carries
    on the third arm (round 1's 🟡 4 and ⬜ 5) are the proofer's to read."""
    broad = " ".join(
        read_document(os.path.join("docs", "running", "the-broad-gate.md")).split()
    )
    # The row name `gate` and the value `tree <version>` the panel prints on
    # it, which a person reads on the gate's output.
    assert (
        "the panel's `gate` row reads `tree <version>` wherever the copy that ran "
        "is not byte for byte the copy invoked"
    ) in broad


def test_the_stamp_docstring_names_the_file_its_mark_is_drawn_from():
    """#832 and #857: the disc's mark is a sprite in a file of its own, and
    changing the mark is changing that file alone. The stamp module's
    docstring names the file; how it describes the letter, the twin's
    characters and the panel's rows is the proofer's to read."""
    stamp = " ".join(
        read_document(
            os.path.join("skills", "verify", "scripts", "seal_stamp.py")
        ).split()
    )
    # The path `seal-mark.txt`, which a person opens to change the disc's
    # mark.
    assert "`seal-mark.txt`" in stamp


def test_the_unmeasured_word_says_so_and_every_reader_is_told_it():
    """A9 (#747, contract rule 14), S15 (#789), and S19 (#825). The reasons
    the gate prints are text a person reads and acts on, so they are pinned
    whole, and each starts with the word that marks it unmeasured; the names
    the record replaced are asserted gone from the module. Every document
    that tells a reader what the gate's words mean names `new?`, so an
    orchestrator handing it on and a crafter reading it are both told it is
    not `new`, and the **New?** bullet names the files a reader sent to the
    base opens. What each document says of the word is the proofer's to
    read."""
    gate = gate_module()
    assert gate.NOT_MEASURED == "new? not measured"
    earns = (
        "A command earns the measured word by letting every pytest it runs load "
        "the gate's recorder: it adds to the PYTHONPATH and PYTEST_ADDOPTS the "
        "gate hands it rather than replacing them, and runs pytest in that "
        "environment rather than one it builds, through any wrapper"
    )
    # #825 round 3's 🟡 3 and round 4's 🟡 3: every cause of a missing
    # record the records cannot tell apart, never one of them as the only one.
    causes = (
        "the command started no pytest, because a part before its runner failed "
        "or it has none; none it started loaded the recorder; or the one that "
        "did could not write its record and warned 'agentic_pytest_record: no "
        "record written' in "
    )
    assert (
        "new? not measured: no pytest the command ran here left a record of the "
        f"gate's recorder ({causes}suite.txt), so this file is named only by a "
        f"FAILED line of suite.txt and the base was not run. {earns}"
    ) == gate.NO_RECORD_AT_HEAD
    assert (
        "new? not measured: the command ran once at the base, and no pytest it ran "
        f"there left a record of the gate's recorder ({causes}suite-at-base.txt; "
        f"records/ is beside it). {earns}"
    ) == gate.NO_RECORD
    # The reframe's S27: what the record at `HEAD` left out is counted, and
    # the failure form says how many.
    assert gate.UNPLACED.format(count=1) == (
        "1 of the tests and collections the command's pytest reported had no file "
        "of their own and are in no list: a test a conftest or a plugin parents "
        "to the session or to a directory, a failed collection of the whole "
        "session, or a report a plugin built without its path (counted as "
        "unplaced on the end line of each record under records/)"
    )
    # #825 round 4's 🟡 2, the part its fix left: `new` from a base record
    # that left anything out is not measured.
    assert gate.UNPLACED_AT_BASE.format(count=2) == (
        "new? not measured: the command ran once at the base, and its sessions that "
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
        "new? not measured: the command ran once at the base, and 1 of its pytest "
        "sessions stopped part-way, because the process died or the recorder "
        "stopped writing before the session's end line, or pytest stopped the "
        "session (an interrupt, pytest.exit(), -x or --maxfail, a plugin's "
        "stop) or ended it on an error of its own, so this file's tests there "
        "may not have finished and whether the base fails it was not measured "
        "(kept as suite-at-base.txt, with records/ beside it)"
    )
    # #849 round 1's 🟡 2: the same at `HEAD`, under the list.
    assert gate.UNENDED_HERE.format(count=1) == (
        "1 of the command's pytest sessions here stopped part-way, because the "
        "process died or the recorder stopped writing before the session's end "
        "line, or pytest stopped the session (an interrupt, pytest.exit(), -x "
        "or --maxfail, a plugin's stop) or ended it on an error of its own, so "
        "a test it stopped in may be in no list and the tests it never reached "
        "are in none (each session's record is under records/)"
    )
    # #869: a line of a keyed record that did not parse, at the base and
    # under the list at `HEAD`.
    assert gate.UNREAD_AT_BASE.format(count=1) == (
        "new? not measured: the command ran once at the base, and 1 of the lines "
        "in the records its pytest wrote there did not parse as the recorder's "
        "and each was passed over, so one may have held this file's failure "
        "and whether the base fails it was not measured (kept as "
        "suite-at-base.txt, with records/ beside it)"
    )
    assert gate.UNREAD_HERE.format(count=1) == (
        "1 of the lines in the records the command's pytest wrote here did not "
        "parse as the recorder's and each was passed over, so a failing test "
        "may be in no list and the suite's counts are not given (each "
        "session's record is under records/)"
    )
    # The warning the recorder prints where it writes no record, which the
    # reasons above quote and a reader finds on `suite.txt`.
    with open(RECORDER_SOURCE, encoding="utf-8") as handle:
        assert "agentic_pytest_record: no record written" in handle.read()
    assert gate.NOT_REACHED.format(code=2) == (
        "new? not measured: the command ran once at the base and exited 2, and no "
        "pytest it ran there collected this file, so the run may have ended "
        "before reaching it and whether the base fails it was not measured "
        "(kept as suite-at-base.txt, with records/ beside it). A file the "
        "branch added reads this way wherever the base's own command already "
        "fails"
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
    # The word `new?`, which `broad_gate.py` prints beside a failing file and
    # each of these documents tells its reader the meaning of: the
    # orchestrator, the crafter, and the person choosing the `Broad gate` key.
    # `skills/verify/orchestration.md` names it as its bullet's bold lead.
    readers = {
        ("skills", "code-review", "orchestration.md"): "`new?`",
        ("agents", "crafter.md"): "`new?`",
        ("skills", "verify", "orchestration.md"): "**New?**",
        ("templates", "setup", "config.md"): "`new?`",
    }
    for parts, word in readers.items():
        with open(os.path.join(ROOT, *parts), encoding="utf-8") as handle:
            assert word in handle.read(), f"{'/'.join(parts)} does not name `new?`"
    # #825: the reader sent to the base by hand is told to open the one kept
    # run and its records.
    with open(
        os.path.join(ROOT, "skills", "verify", "orchestration.md"), encoding="utf-8"
    ) as handle:
        bullet = " ".join(handle.read().split())
    for path in (
        # The file the gate keeps the base's run in, which the reader opens.
        "`suite-at-base.txt`",
        # The directory of that run's records, which the reader opens beside it.
        "`records/`",
    ):
        assert path in bullet, f"the **New?** bullet does not name: {path}"


def test_the_measurement_its_cost_and_its_limits_are_told_where_the_row_is_written():
    """S15 of #789 and S19 of #825 (contract rule 14). Rule 3 of *The
    criterion for choosing a value* is the one home of how the gate measures
    a command at the base, what that costs, and which commands it cannot
    measure, so the spellings a reader acts on are pinned there: the words
    the gate prints, the files and the line it reads and writes, and the
    variables and the flag it hands a command. Its sentences are the
    proofer's to read. S6 of #1301: the two rows of *Everything else stays
    legal* that let a command compose after pytest cite rule 3."""
    with open(
        os.path.join(ROOT, "templates", "setup", "config.md"), encoding="utf-8"
    ) as handle:
        text = handle.read()
    for spelling in (
        # The row of rule 3, which the citations below resolve to.
        "| 3 |",
        # The plugin flag the gate appends to `PYTEST_ADDOPTS`, and the two
        # variables it hands the command, which a person writing the key
        # keeps.
        "`-p agentic_pytest_record`",
        "`PYTEST_ADDOPTS`",
        "`PYTHONPATH`",
        # The words `broad_gate.py` prints beside a failing file, which a
        # reader of the gate's output acts on.
        "`failing on base too`",
        "`new?`",
        "`new`",
        # The files the gate writes the two runs into, which a reader opens.
        "`suite-at-base.txt`",
        "`suite.txt`",
        # The pytest line the gate reads a file from where no record was
        # left.
        "`FAILED`",
        # The recorder's last line of a session, which the gate reads.
        "`end`",
        # The record the gate does not write where the suite fails.
        "`trail/gate.md`",
    ):
        assert spelling in text, f"rule 3 does not carry: {spelling}"
    # #1301: the two rows of *Everything else stays legal* that a red pytest
    # under a composition reaches cite rule 3.
    for spelling in (
        # The citation of rule 3, which a person reading the allowed list
        # resolves to the row above.
        "rule 3 of *The criterion for choosing a value*",
        # The pipe a person may compose the command with, as the row spells
        # it in the table.
        "`bin/test -q \\| tee out.txt`",
    ):
        assert spelling in text, f"the allowed list does not carry: {spelling}"


# =============================================================================
# Part 3 — the owner, and the fourth definition
# =============================================================================

# `agents/crafter.md` and `agents/proofer.md` each carried the rule with no owner
# in it: *the full suite is the orchestrator's*. #30 named the sealer in both.
# Both were written anew since (#957, #967) and name no runner: the run's
# owner moves from the sealer to the orchestrator in #969, and contract rule 2 is
# where a reader finds it. What each definition still owes is the coverage
# probe, in its own words, which are the proofer's to read. What is pinned is
# the line #985's absence rule names a probe on in the proofer's definition:
# the finding's `evidence: executed` line.
SEALER = os.path.join(ROOT, "agents", "sealer.md")
PROBE = {
    # The line of a round record's finding a probe is named on, the key and
    # value `chain_check.py` reads through `lib/fields.py`.
    "proofer.md": "`evidence: executed`",
}


def agent(name):
    with open(os.path.join(ROOT, "agents", name), encoding="utf-8") as handle:
        return " ".join(handle.read().split())


def sealer_text():
    with open(SEALER, encoding="utf-8") as handle:
        return handle.read()


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


def test_the_crafters_gate_rule_names_the_failure_words_and_rule_2():
    """T4 of #967 (S5): the crafter's broad gate paragraph cites contract
    rule 2, which holds who runs the broad gate, and keeps what is the
    crafter's own: what `failing on base too` and `new?` mean beside a broad
    gate failure handed to it. That it names nobody as the runner (#969 moved
    the run to the orchestrator) is the proofer's to read."""
    with open(os.path.join(ROOT, "agents", "crafter.md"), encoding="utf-8") as handle:
        crafter = handle.read()
    start = crafter.index("**The broad gate is not yours, and its label is.**")
    rule = " ".join(crafter[start:].split("\n\n", 1)[0].split())
    # The words `failing on base too` and `new?`, which `broad_gate.py`
    # prints beside a failing file and the crafter reads to tell the two
    # apart.
    assert "`failing on base too`" in rule and "`new?`" in rule, (
        "the crafter's gate rule stopped saying what the word beside a "
        "failing file means, which is the half that is the crafter's own"
    )
    # The contract rule number 2, which the crafter resolves for who runs
    # the broad gate.
    assert "rule 2" in rule, "the rule stopped pointing at where the runner is named"


# --- S7 the fourth definition ------------------------------------------------
#
# The contract paragraph this file opens with is held to byte identity by
# `tests/text/test_every_agent_reads_the_contract.py`, over a glob this file joins
# on the day it lands. Re-pinning it here would be the duplication that module
# and `tests/text/test_a_moved_rule_leaves_its_definition.py` exist to refuse, so
# what part 3 pins is what no existing module reads.


def test_the_fourth_definition_exists():
    assert os.path.exists(SEALER), "agents/sealer.md is not in the tree"


def test_the_sealer_preloads_the_core_and_the_contract_and_nothing_else():
    """Q5: its whole procedure is one command, and #292 measured every
    preloaded body as a cost paid again on every spawn. `verify` is 35 KB for
    four conditions the definition states in four lines. The core every
    agent preloads since #1177 is the one addition."""
    head = sealer_text().split("\n---\n", 1)[0]
    # The `skills:` list of the frontmatter, which the harness reads to
    # preload each skill named into every sealer spawn.
    assert re.findall(r"^  - (\S+)", head, re.M) == ["core", "agent-contract"], (
        "the sealer's `skills:` list is not `core` then `agent-contract`, so a "
        "body rides every spawn for a procedure that is one command"
    )


def test_the_sealer_names_the_one_write_its_definition_is_allowed():
    """Contract rule 6 says what an agent writes is named in its own definition
    and nothing else, so this file is the whole of the sealer's permission. A
    write nobody named is a review that certifies itself.

    Before #120 the same case read `as its own exception`, because rule 6 carved
    exceptions and pointed at the definition holding each one. The mechanism
    did not move -- it stopped being the exception and became the rule -- so
    every assertion below is unchanged and only the name and the grounds are.

    Since the sealer became the guarantor (#923) its one write in the tree
    is `guarantee.md`, and `trail/gate.md` is the gate's, through its
    command. Since #1376 the stamp's values file its `seal stamp --guarantee`
    queues is named beside it. How the definition ends the list is the
    proofer's to read."""
    text = " ".join(sealer_text().split())
    # The contract rule number 6, which the sealer resolves for what it may
    # write.
    assert "rule 6" in text, "the sealer cannot reach the rule that names its one write"
    # The command `seal gate --record`, which writes `trail/gate.md` and which
    # the sealer reads to tell that file from its own write.
    assert "through `seal gate --record`" in text, (
        "the gate's file does not name the command that makes it, so the "
        "sealer cannot tell its own write from the gate's"
    )
    # The path `guarantee.md`, the sealer's one write in the tree, which the
    # sealer reads for what it may write.
    assert "`guarantee.md`" in text, (
        "the permission does not say WHICH files, and a permission without a "
        "boundary is a general one"
    )


def test_the_sealer_cites_contract_rule_2():
    """The sealer shipped under a contract rule 2 that forbade its one act,
    for a window inside one release branch, and #120 closed it; #969 then
    moved the broad run to the orchestrator. The definition cites the rule
    that keeps the run out of its hands. Whether the window's paragraph or
    an assignment of the run to the sealer is back, and how the definition
    says whose the run is, are the proofer's to read."""
    text = " ".join(sealer_text().split())
    # The contract rule number 2, which the sealer resolves for who runs the
    # broad gate.
    assert "rule 2" in text, (
        "the definition stopped citing rule 2 altogether, so the sealer meets the "
        "rule that keeps the run out of its hands nowhere in its own file"
    )


def test_the_sealer_carries_the_labels_its_claims_are_written_under():
    """Q5 again, from the other side: dropping `verify` from the spawn is only
    correct if the conditions arrive some other way. The definition carries
    the labels a result is written under; how it words the conditions is the
    proofer's to read."""
    text = " ".join(sealer_text().split())
    for condition in (
        # The two labels a claim of the sealer's hand-back is written under,
        # which the orchestrator reads.
        "`executed`",
        "`unverified`",
    ):
        assert condition in text, (
            f"the sealer's definition does not carry `{condition}`, and "
            "`verify` is not in its `skills:` list to carry it instead"
        )
