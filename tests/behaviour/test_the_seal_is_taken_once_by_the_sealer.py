"""The seal is taken once, by the sealer, and what the documents say of it.

Issue #30. The stamp's own cases, `skills/verify/scripts/seal_stamp.py` one
class per function, are `tests/skills/test_seal_stamp.py`, and the gate's,
`skills/verify/scripts/broad_gate.py`, are `tests/skills/test_broad_gate.py`, since
#942.

Part 2 holds the cases about the gate command that read a document's prose,
which #923 places. Part 3 holds the cases that read the agent definitions.
"""

import os
import re

import pytest
from conftest import ROOT, load_module
from test_the_agent_contract_holds_the_universal_rules import HEADING

GATE = os.path.join(ROOT, "skills", "verify", "scripts", "broad_gate.py")
RECORDER_SOURCE = os.path.join(
    ROOT, "skills", "verify", "scripts", "pytest_record", "agentic_pytest_record.py"
)


def gate_module():
    return load_module(GATE, "agentic_broad_gate_for_tests")


# =============================================================================
# Part 2 — the gate's prose, left for #923
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
    config = module.load(module.CONFIG_READER, "agentic_config_for_this_case")
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
    """S15 of #789 and S19 of #825 (contract rule 14). Rule 3 is the one home of
    how the gate measures a command at the base, what that costs, and which
    commands it cannot measure, so each sentence a reader acts on is pinned
    there, and every sentence of the mechanism #825 retired is asserted gone.
    S6 of #1301: the two rows of *Everything else stays legal* that let a
    command compose after pytest say that a red session still fails the
    suite, and cite rule 3. #1454: the value is a key's command, so no
    sentence calls it a row."""
    with open(
        os.path.join(ROOT, "templates", "setup", "config.md"), encoding="utf-8"
    ) as handle:
        text = handle.read()
    for sentence in (
        "| 3 | Every pytest the command runs keeps the environment the gate hands it |",
        "On a failing test the gate compares each failing file with the base "
        "from a record, never from what pytest printed.",
        "the recorder's directory first on `PYTHONPATH`, `-p "
        "agentic_pytest_record` appended to `PYTEST_ADDOPTS`, and a key made "
        "fresh for the run.",
        "A pytest a test starts, and an xdist worker, inherit no key and write "
        "nothing, so nothing a test prints or runs changes a word.",
        "**Then the command runs once more, unchanged, at the base** (nothing "
        "appended, no part cut, every part run as written)",
        "where no pytest at the base left a record (the command ended before it "
        "started one, none loaded the recorder, "
        "or the one that did could not write its record and warned in "
        "`suite-at-base.txt`), `new?`; where the "
        "base's record holds a failing test or a failed collection of the file, "
        "`failing on base too`; where it holds the file and nothing of it "
        "failed, `new`; where it does not hold the file and the command exited "
        "0, `new`, because the command ran to its end and never collected the "
        "file; and where it does not hold the file and the command exited "
        "otherwise, `new?` naming the exit, because the run may have ended "
        "before reaching it; so a file the branch added reads `new?` wherever "
        "the base's command already fails.",
        "Where no pytest the command ran at `HEAD` left a record, for any of "
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
        # #883: that stop fails the suite even where the command exited 0.
        "Where one did, the suite fails even where the command exited 0, as it "
        "does when a test calls `pytest.exit()` with a return code of 0 or "
        "`os._exit(0)`, because a stop that chooses the exit code says neither "
        "that the session ran every test it collected nor that nothing it ran "
        "failed.",
        # #1301: so does a red session, whatever acted after the run loop.
        "So does a session whose `end` line shows exit 1 with nothing stopping "
        "it, whatever the command exited: that exit is the one pytest's run "
        "loop gave, which pytest hands every `pytest_sessionfinish` hook alike, "
        "so an act after the loop that turns the command's exit into 0 does "
        "not change it.",
        "Such an act is a hook that sets the session's exit status, a later "
        "`pytest_sessionfinish` hook that raises `pytest.exit()`, a "
        "`pytest_unconfigure` hook that ends the process, or a part of the "
        "command after pytest, such as `; true` or a pipe.",
        "In either case the failure form says so, and no `trail/gate.md` is written.",
        # #883 rounds 1 and 2: the stop no record shows, with what the gate
        # reads per session, so the sentence holds for a command that runs
        # pytest once or several times.
        "One stop is out of the record's reach. A stop raised before the "
        "recorder writes a session's first line, such "
        "as a `pytest.exit()` in a conftest's `pytest_configure`, leaves no "
        "record of that session, so the gate reads the run as though that "
        "session never started: it judges the run on the command's exit and on "
        "the records the command's other sessions left, where there are any.",
        "**The cost is one more run of the whole command, and only when the "
        "suite fails**, whatever the number of failing files.",
        "so a part after the runner that the branch's own run never reached, "
        "because `&&` stopped at its failing suite, runs at the base wherever "
        "the base's suite passes,",
        "So the runner may come first or last, and the order is the "
        "repository's trade: either way the command runs once, whole, at the "
        "base.",
        "**A command earns the measured word** by letting every pytest it runs "
        "load "
        "the recorder: it adds to the `PYTHONPATH` and `PYTEST_ADDOPTS` the "
        "gate hands it rather than replacing them, and runs pytest in that "
        "environment rather than in one it builds.",
        "A runner started by `tox`, `nox`, `env -i`, a container or a wrapper "
        "that rebuilds the environment without either variable writes no "
        "record, and so does a command that sets `PYTEST_ADDOPTS` to a value of "
        "its own; its files read `new?`.",
        # #825 round 1's 🟡 2: Q2's class, not its first instance.
        "A command that keeps `PYTEST_ADDOPTS` and loses `PYTHONPATH` fares worse "
        "(one that replaces `PYTHONPATH`, an interpreter run with `-I` or `-E`, "
        "a wrapper that passes `PYTEST_ADDOPTS` or `PYTEST_*` on and not "
        "`PYTHONPATH`): pytest cannot import the module the `-p` names and exits "
        "1 before any test runs, so the command fails at the gate.",
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
        "`--report-log` among them, writes it into the command's own log while "
        "the gate measures the command.",
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
        # #1301: the late hook named as a stop out of the record's reach, and
        # a piped row called green on its last part's exit.
        "Two stops are out of the record's reach",
        "comes after the session's `end` line, so that session reads as one "
        "that ran to its end",
        "is green whenever `tee` is",
        # #1454: the value is a key holding a command, not a row.
        "Every pytest the row runs",
        "**Then the row runs once more",
        "**A row earns the measured word**",
        "the base's row already fails",
    ):
        assert gone not in text, f"rule 3 still carries: {gone}"
    # #1301: the two rows of *Everything else stays legal* that a red pytest
    # under a composition reaches cite rule 3, whose sentences are above.
    for sentence in (
        "That is the repository's own claim about itself, which is what this "
        "key already is. A pytest session the command runs that did not pass by "
        "its own record still fails the suite, whatever the composition exits "
        "(rule 3 of *The criterion for choosing a value* below) |",
        "so `bin/test -q \\| tee out.txt` exits 0 whenever `tee` does. That "
        "exit is the repository's own claim about itself, and the gate still "
        "fails the suite where a pytest session under the pipe did not pass by "
        "its own record (rule 3 of *The criterion for choosing a value* "
        "below).",
    ):
        assert sentence in text, f"the allowed list does not carry: {sentence}"


# =============================================================================
# Part 3 — the owner, and the fourth definition
# =============================================================================

# `agents/crafter.md` and `agents/proofer.md` each carried the rule with no owner
# in it: *the full suite is the orchestrator's*. #30 named the sealer in both.
# Both were written anew since (#957, #967) and name no runner: the run's
# owner moves from the sealer to the orchestrator in #969, and contract rule 2 is
# where a reader finds it. What each definition still owes is the coverage
# probe, in its own words. The proofer's words are #985's absence rule: a
# claim that nothing catches a finding is a probe, named on the finding's
# `evidence: executed` line.
SEALER = os.path.join(ROOT, "agents", "sealer.md")
PROBE = {
    "crafter.md": (
        "Asking whether the suite catches something is a coverage probe, a "
        "different act: run it over the module that should catch it and "
        "report it as a probe."
    ),
    "proofer.md": (
        "A claim of absence, such as nothing in the suite catching this, is a "
        "probe: run it over the module that should catch it, report it as a "
        "probe, never as a seal, and name it on the finding's `evidence: "
        "executed` line."
    ),
}

# Contract rule 2 and contract rule 6, read from the contract rather than
# typed, so a rule that is rewritten (#120) is compared as it then stands.
CONTRACT = os.path.join(ROOT, "skills", "agent-contract", "SKILL.md")

# `tests/text/test_a_moved_rule_leaves_its_definition.py` measured this: 15 words is
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
    words is the paste `tests/text/test_a_moved_rule_leaves_its_definition.py`
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
