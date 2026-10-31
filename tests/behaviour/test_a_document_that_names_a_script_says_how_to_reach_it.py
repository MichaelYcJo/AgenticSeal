"""A shipped document that names a script says how to reach it.

Issue #318. `skills/code-review/scripts/round_record.py` was named on
thirty-six lines of nine shipped documents and no document anywhere gave a
path to it or a command that runs it. Four agent segments went looking,
concluded the generator does not ship, and hand-wrote the record it writes --
two of the resulting records had a field wrong in a way only the next round's
reader caught.

The defect has two halves and a command repairs one. Two of those thirty-six
lines show a command for somebody to TYPE; the other thirty-four describe what
the generator does, and a reader who meets one goes LOOKING for a filename.
Three of the four segments were the reviewer, whose definition never tells it
to run the script at all, so the typed half is the half those segments never
touched.

What this file pins is the looking half, as a property of the class rather
than of the instance the ticket named -- contract rule 12,
*do not fix the coordinate, enumerate the class*. The ticket named three
documents; there were nine, and the one the four segments actually hand-wrote
from (`templates/records/sdd-round.md`, seven mentions) was not among the three.

Two rules, and the second is narrower than the first on purpose:

  every script a shipped document names   has a `seal` subcommand in
                                          `seal.py#TOOLS`, or is classified
                                          below with its reason

  every shipped document that names a     carries the subcommand or the
  script with a subcommand                script's repo-relative path, at
                                          least once

A script with no subcommand is exempt from the second rule because it has no
command to name, and requiring its path in every document that mentions it
would touch six files for a script nobody is told to run.
`test_a_script_with_no_subcommand_is_shown_in_no_command_form` is what keeps
that exemption from being a loophole: the moment a document shows such a
script being invoked, the classification stops being true and goes red rather
than standing as a note.

Scope is what an agent's startup payload can contain: `agents/`, `skills/` and
`templates/`. `docs/` stays out under
`tests/behaviour/test_the_release_check_watches_what_ships.py`'s own classification --
it does not ship, no agent's payload holds it, and its readers have the whole
clone to `git grep`.

Shown red before it was committed (contract rule 15): against the tree as it stood, this
file failed on all nine of `round_record.py`'s documents and on
`chain_check.py` having no classification, and the command-form case was
driven red by planting an invocation in a shipped document. Since #1051 the
commands are `seal` subcommands rather than one `bin/` wrapper each, and the
cases read `seal.py#TOOLS` where they read `bin/`.
"""

import glob
import os
import re

import pytest
from conftest import ROOT, load_module, read

SEAL = load_module(
    os.path.join(ROOT, "skills", "implement", "scripts", "seal.py"),
    "seal_for_the_locator_rule",
)

# The subcommand each script answers to, by the script's file name.
SUBCOMMANDS = {
    os.path.basename(script): name for name, (script, _) in SEAL.TOOLS.items()
}

# What an agent's startup payload can contain. `docs/` is deliberately absent.
SHIPPED_ROOTS = ("agents", "skills", "templates")

# Scripts that ship without a `seal` subcommand, and the reason each one keeps
# none. A script named by a shipped document belongs here or in
# `seal.py#TOOLS`; a third state is the one `bin/` itself was in before work
# item 1788302682 -- a gap somebody notices while writing something up.
NO_SUBCOMMAND = {
    "rule_changes.py": (
        "A module `settle.py` and `unverified_check.py` load by path, with no "
        "command line of its own: no shipped document shows it with a flag."
    ),
    "chain_check.py": (
        "Named in shipped documents and shown with a flag only by its "
        "repo-relative path, as `agents/proofer.md` step 7 runs it -- which is "
        "what `test_a_script_with_no_subcommand_is_shown_in_"
        "no_command_form` asserts, and the whole of it. A flag is the only "
        "sound tell in prose, so a bare mention in a list of checks is not "
        "caught: `templates/setup/config.md` names it beside three commands. "
        "Every place outside `tests/` that invokes it carries its full path "
        "-- `.github/workflows/hygiene.yml`, `templates/setup/hygiene.yml` and "
        "`docs/release-checklist.md` by hand, and "
        "`skills/verify/scripts/broad_gate.py` in code; the test modules that "
        "load it build the "
        "same path -- so it is reachable everywhere it is reached. "
        "A subcommand would also change the row in "
        "`templates/setup/config.md` that spells the broad gate to a user, which is "
        "a user-facing change with no defect behind it (#318)."
    ),
}


def scripts():
    """Every script that ships under a skill, repo-relative with `/`."""
    found = glob.glob(os.path.join(ROOT, "skills", "*", "scripts", "*.py"))
    return sorted(os.path.relpath(p, ROOT).replace(os.sep, "/") for p in found)


def shipped_documents():
    """Every `.md` under the roots an agent's payload is drawn from."""
    found = []
    for root in SHIPPED_ROOTS:
        pattern = os.path.join(ROOT, root, "**", "*.md")
        found += glob.glob(pattern, recursive=True)
    return sorted(os.path.relpath(p, ROOT).replace(os.sep, "/") for p in found)


def command_name(script):
    """The command a person types for `script`: `seal` and its subcommand,
    or `seal` alone for `seal.py`, the script the command itself runs.
    None for a script with no subcommand."""
    base = os.path.basename(script)
    if base == "seal.py":
        return "seal"
    name = SUBCOMMANDS.get(base)
    return f"seal {name}" if name else None


def is_wrapped(script):
    """Whether a person can type a command that runs `script`."""
    return command_name(script) is not None


def names(text, script):
    """Whether `text` mentions the script by filename at all. A filename
    standing inside a longer one is another file's name: `tests/skills/test_settle.py`
    on a `check:` line is not a mention of `settle.py`."""
    base = re.escape(os.path.basename(script))
    return re.search(rf"(?<![\w-]){base}", text) is not None


def reachable(text, script):
    """Whether `text` gives a reader a way to GET to `script`.

    Either accepted form counts. The subcommand is what a session with the
    plugin enabled can type, because the loader puts `bin/` on the Bash
    tool's PATH and `bin/seal` is there. The repo-relative path is what a
    session working inside a clone with the plugin disabled can open.
    """
    command = command_name(script)
    # `seal` alone cannot be told from ordinary English -- this repository's
    # prose is made of that word -- so this reader does not take the bare
    # command as a locator for `seal.py`, and the path is the form that counts.
    #
    # A subcommand is two words, and two words can be prose too: *the seal
    # stamp*. So the subcommand counts only where it is shown as a command,
    # opening an inline code span or a line of a code block, which is how
    # every document that teaches one writes it. It counts with arguments
    # after it and not inside a longer word.
    if command == "seal":
        return script in text
    shown = rf"(?:`|^[ \t]*){re.escape(command)}(?![\w-])"
    typed = re.search(shown, text, re.M) is not None
    return typed or script in text


def command_forms(text, script):
    """Lines of `text` that show `script` being INVOKED rather than described.

    A flag is the tell, and it is the only sound one in prose. A subcommand
    cannot be told from the sentence around it -- *`round_record.py new`
    writes the record* names a subcommand and is a description -- but nothing
    writes `chain_check.py --worktree` except to say what to run.

    Used on the scripts that keep no subcommand: the classification below
    rests on nobody being told to type them without being told where they
    are, and this is the property, asked of the tree rather than assumed. An
    invocation by the script's repo-relative path carries its locator, the
    one the rule above asks of a script with a subcommand, so it is not
    counted (#1198 phase 3: `agents/proofer.md` step 7 runs `chain_check.py`
    by its path, which a wrap had hidden from this reader).
    """
    invoked = re.compile(rf"(?<![\w-]){re.escape(os.path.basename(script))}\s+-")
    located = re.compile(rf"(?<![\w./-]){re.escape(script)}\s+-")
    return [
        (number, line)
        for number, line in enumerate(text.splitlines(), 1)
        if len(invoked.findall(line)) > len(located.findall(line))
    ]


def named_pairs():
    """(document, script) for every shipped document naming a script with a
    command.

    The parametrisation both document cases run over. Built once, at
    collection, so a tenth document naming a script is a case that appears
    rather than a rule somebody has to remember.
    """
    texts = {d: read(os.path.join(ROOT, d)) for d in shipped_documents()}
    return [
        (document, script)
        for script in scripts()
        if is_wrapped(script)
        for document, text in texts.items()
        if names(text, script)
    ]


def unwrapped_pairs():
    """(document, script) for every shipped document naming a script with no
    command."""
    texts = {d: read(os.path.join(ROOT, d)) for d in shipped_documents()}
    return [
        (document, script)
        for script in scripts()
        if not is_wrapped(script)
        for document, text in texts.items()
        if names(text, script)
    ]


def label(pair):
    return f"{pair[0]}::{os.path.basename(pair[1])}"


# --- the script half -------------------------------------------------------


@pytest.mark.parametrize("script", scripts())
def test_every_script_a_shipped_document_names_has_a_subcommand_or_is_classified(
    script,
):
    """A script a document names either has a command or has a recorded
    reason for having none. Neither answer is safe to leave to whoever
    notices, which is the lesson `bin/` itself paid for."""
    texts = [read(os.path.join(ROOT, d)) for d in shipped_documents()]
    if not any(names(t, script) for t in texts):
        pytest.skip("no shipped document names it, so nobody goes looking")
    base = os.path.basename(script)
    if base in NO_SUBCOMMAND:
        assert NO_SUBCOMMAND[base].strip(), (
            f"{base} is classified as keeping no subcommand with an empty reason "
            f"-- say why in NO_SUBCOMMAND in {os.path.basename(__file__)}"
        )
        return
    assert is_wrapped(script), (
        f"a shipped document names {base} and no `seal` subcommand runs it. "
        f"Add it to `TOOLS` in `skills/implement/scripts/seal.py`, or classify "
        f"{base} in NO_SUBCOMMAND in {os.path.basename(__file__)} with the reason"
    )


def test_nothing_classified_has_grown_a_subcommand():
    """A classification is a claim about the tree, so it stops being true the
    moment somebody adds the subcommand. Left standing, it is a note nobody
    re-reads that says the opposite of what `seal.py#TOOLS` holds."""
    stale = [b for b in NO_SUBCOMMAND if is_wrapped(f"skills/x/scripts/{b}")]
    assert not stale, (
        f"{sorted(stale)} now have `seal` subcommands and are still classified "
        f"as keeping none -- drop the rows from NO_SUBCOMMAND in "
        f"{os.path.basename(__file__)}"
    )


def test_nothing_classified_has_stopped_shipping():
    """A row for a script that no longer exists reads as a live decision."""
    present = {os.path.basename(s) for s in scripts()}
    gone = sorted(set(NO_SUBCOMMAND) - present)
    assert not gone, (
        f"{gone} are classified in {os.path.basename(__file__)} and ship from "
        "no skill -- drop the rows with the script"
    )


# --- the document half -----------------------------------------------------


@pytest.mark.parametrize("pair", named_pairs(), ids=label)
def test_a_document_naming_a_script_with_a_command_says_how_to_reach_it(pair):
    """The half of #318 a command does not repair: a reader who meets
    *`round_record.py new` writes the record* goes looking for a filename, and
    finds nothing. One mention per document is enough -- a document naming a
    script forty times pays one sentence."""
    document, script = pair
    command, text = command_name(script), read(os.path.join(ROOT, document))
    # The repair offered has to be one that works. `reachable` does not read
    # the bare `seal` as a locator, so offering it to a reader who then adds
    # it leaves them red with nothing saying why -- #318's own shape,
    # reproduced inside #318's fix.
    forms = (
        f"the path `{script}`. `seal` alone is a word of prose, so this rule "
        "does not read the bare command as a locator -- see `reachable`"
        if command == "seal"
        else f"either reachable form: the command `{command}`, shown in code, "
        f"or the path `{script}`"
    )
    assert reachable(text, script), (
        f"{document} names {os.path.basename(script)} and never says where it "
        f"is. A reader who goes looking finds nothing, which is #318. Add "
        f"{forms}, once"
    )


@pytest.mark.parametrize("pair", unwrapped_pairs(), ids=label)
def test_a_script_with_no_subcommand_is_shown_in_no_command_form(pair):
    """What keeps the exemption above from being a loophole. A script with no
    subcommand is excused the locator rule because nobody is told to type it,
    and this is that premise asked of the tree rather than assumed."""
    document, script = pair
    base = os.path.basename(script)
    shown = command_forms(read(os.path.join(ROOT, document)), script)
    assert not shown, (
        f"{document} shows {base} being invoked, so the classification in "
        f"{os.path.basename(__file__)} -- kept with no subcommand because no "
        "document tells anybody to run it -- is no longer true:\n"
        + "\n".join(f"  {document}:{n}: {line.strip()}" for n, line in shown)
        + "\n\nEither add it to `TOOLS` in `skills/implement/scripts/seal.py`, "
        "or take the invocation out."
    )


# --- the checks can fail ---------------------------------------------------


def test_a_document_with_no_locator_is_caught():
    """`reachable` is the whole of the document rule, so a reader that
    answered yes to any mention would make every case above vacuous."""
    arms = "skills/x/scripts/arm_check.py"
    assert not reachable("`arm_check.py` lists the arms.", arms)
    assert reachable("Run `seal arms hooks/x.py`.", arms)
    assert reachable("```\nseal arms hooks/x.py\n```\n", arms)
    assert reachable("It lives at `skills/x/scripts/arm_check.py`.", arms)


def test_the_failure_message_offers_a_repair_that_actually_works():
    """Contract rule 14: a message a person reads and acts on is pinned by a case.

    The repair the message names has to be one the rule accepts. For the bare
    `seal` it cannot be, so the message says the path and says why --
    otherwise a reader adds `seal`, re-runs, is still red, and has been told
    nothing. That is #318's own shape reproduced inside #318's fix.

    `templates/records/sdd-plan.md` is the document in both directions because it
    names neither script and carries neither command, so the case is
    guaranteed to fail and its message is the whole of what is being read.
    """
    seal = "skills/implement/scripts/seal.py"
    with pytest.raises(AssertionError) as raised:
        test_a_document_naming_a_script_with_a_command_says_how_to_reach_it(
            ("templates/records/sdd-plan.md", seal)
        )
    message = str(raised.value)
    assert "the command `seal`" not in message, (
        "the message offers a repair the rule rejects: a reader who adds the "
        f"bare command is still red and learns nothing from it -- {message}"
    )
    assert seal in message and "a word of prose" in message, (
        f"the message does not name the form that works, or why -- {message}"
    )

    arms = "skills/verify/scripts/arm_check.py"
    with pytest.raises(AssertionError) as raised:
        test_a_document_naming_a_script_with_a_command_says_how_to_reach_it(
            ("templates/records/sdd-plan.md", arms)
        )
    assert "the command `seal arms`" in str(raised.value), (
        "a subcommand still has both accepted forms offered"
    )


def test_the_bare_command_is_not_a_locator():
    """`seal.py` answers to `seal`, and every document in this repository
    contains that word. Read as a locator it makes the rule unfalsifiable for
    that script, which is the one thing Q1's general form was chosen to
    prevent."""
    seal = "skills/implement/scripts/seal.py"
    assert not reachable("The sealer takes the seal after the rounds.", seal)
    assert not reachable("Run `seal mode` first.", seal)
    assert reachable("It lives at `skills/implement/scripts/seal.py`.", seal)


def test_a_subcommand_in_prose_or_inside_a_longer_word_does_not_count():
    """`seal stamp` in a sentence is two words of prose, and `seal arms`
    inside `seal arms-length` is a different name; a substring test would
    let either satisfy the rule."""
    stamp = "skills/x/scripts/seal_stamp.py"
    assert not reachable("A seal stamp is drawn once.", stamp)
    arms = "skills/x/scripts/arm_check.py"
    assert not reachable("`seal arms-length` is not a command", arms)
    assert not reachable("`unseal arms` is not a command", arms)


def test_a_test_file_named_for_a_script_does_not_name_it():
    """A `check:` line names test files, and rule 1 names each module's file
    for its module, so `tests/test_round_record.py` holds the script's
    filename without mentioning the script. Read as a mention, it asked
    `agents/proofer.md` for locators of two scripts it never names."""
    script = "skills/x/scripts/round_record.py"
    assert not names("check: tests/test_round_record.py", script)
    assert names("`round_record.py` writes the record.", script)
    assert names("It lives at `skills/x/scripts/round_record.py`.", script)
    assert not command_forms("bin/test tests/test_round_record.py -q\n", script)


def test_a_planted_invocation_turns_the_classification_red():
    """The classification-defence case, driven from a fixture: a document that
    starts showing a script with no subcommand being run has to fail rather
    than pass quietly. Neutral text, no real path."""
    script = "skills/x/scripts/chain_check.py"
    assert command_forms("Run `chain_check.py --worktree` first.\n", script)
    assert command_forms("    chain_check.py -q\n", script)
    assert not command_forms("`chain_check.py` reads the record.\n", script)
    assert not command_forms("what `chain_check.py new` would say\n", script)
    # #1198 phase 3: an invocation by the script's repo-relative path carries
    # its locator, so a reader reaches the script, and only a bare one counts.
    located = "Run `python3 skills/x/scripts/chain_check.py --worktree`.\n"
    assert not command_forms(located, script)
    assert command_forms(located.replace("skills/x/", "other/"), script)
    assert command_forms(located + "Then `chain_check.py -q`.\n", script)
    assert command_forms(
        located.replace(".\n", ", then `chain_check.py -q`.\n"), script
    )


def test_every_mention_lands_in_exactly_one_enumeration():
    """The two parametrisations partition the mentions between them.

    Without this, an enumeration that returned nothing would be a GREEN suite:
    an empty parametrisation runs no case and reports success. That is how the
    classification defence would go silent -- `unwrapped_pairs` answering with
    an empty list means `chain_check.py` is invoked nowhere, checked nowhere.
    """
    texts = {d: read(os.path.join(ROOT, d)) for d in shipped_documents()}
    every = {(d, s) for s in scripts() for d, t in texts.items() if names(t, s)}
    wrapped, unwrapped = set(named_pairs()), set(unwrapped_pairs())
    assert wrapped | unwrapped == every, (
        "a document naming a script reaches neither enumeration, so no case "
        f"runs over it: {sorted(every - wrapped - unwrapped)}"
    )
    assert not wrapped & unwrapped, (
        f"a script is enumerated as both wrapped and not: {sorted(wrapped & unwrapped)}"
    )
    if NO_SUBCOMMAND:
        assert unwrapped, (
            "a script is classified as keeping no subcommand and no document "
            "reaches the case defending that classification"
        )


def test_the_enumeration_is_not_empty():
    """Every case above is parametrised off the tree. An enumeration that
    silently returned nothing would be a green suite that checks nothing --
    the shape a `glob` typo produces, and it exits zero."""
    assert len(scripts()) >= 10, scripts()
    assert len(shipped_documents()) >= 20, len(shipped_documents())
    assert named_pairs(), "no shipped document names a script with a command"
    assert len(SUBCOMMANDS) == len(SEAL.TOOLS), SUBCOMMANDS
