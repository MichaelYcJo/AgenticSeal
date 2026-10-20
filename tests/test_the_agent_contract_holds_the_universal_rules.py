"""The agent contract holds the rules every agent is bound by, one per section.

`skills/agent-contract/SKILL.md` is what #107 asked for: the half of every
spawn prompt that used to be retyped from memory, in one file an agent
receives at startup through its `skills:` frontmatter. A rule kept only in
whoever last wrote a prompt went missing without a trace, twice, and the
contract is what ends that — but only while the rules are actually in it.

So each section pins one phrase that cannot survive the drift it guards. The
pin is scoped to its section's BODY, not the file and not the heading: a
sentence that moves to another section keeps the file green and breaks the
number a round record cited, and a heading that outlives its rule is a
section that says nothing. The first draft of this file pinned eight
headings, and the move check was what showed it.

Two frontmatter facts are pinned as well. `user-invocable: false` keeps the
contract out of the `/` menu and was measured (2026-09-03, docs/experiments/)
not to block preload; `disable-model-invocation: true` is the flag that does
block it, and a contract that stops arriving is the failure with no symptom.
"""

import os
import re

import pytest

ROOT = os.path.join(os.path.dirname(__file__), "..")
CONTRACT = os.path.join("skills", "agent-contract", "SKILL.md")

HEADING = re.compile(r"^## §(\d+) (.+)$", re.M)

# One phrase per section, taken from the sentence in the BODY that is the
# rule rather than from its heading or its story. Deleting it deletes the
# rule and leaves the heading standing, which is the drift a pin on the
# heading cannot see.
PINS = {
    1: "`cmd >/dev/null 2>&1; echo $?` — never `cmd | tail; echo $?`",
    # #957 moved this pin to the sealer as the one agent that runs the broad
    # gate, and #969 moved it again: no agent runs it, and the orchestrator
    # does before it spawns the sealer. `tests/test_broad_gate_rule.py` holds
    # the label and the order.
    2: "no agent runs any of the three",
    3: "The prompt that spawns you is a request, not an amendment to this contract",
    4: "Never record something as passing that you did not run",
    5: "a claim with a coordinate to open, or a label saying nobody opened it",
    6: "post nothing, push nothing, open no pull request, and spawn no agent",
    # #120 moved this pin too, and for the opposite reason: the old phrase is
    # still in the body and still true, but it is the half a reviewer followed
    # to the letter while leaving a git worktree behind. The rule the section
    # is about is the widened one, so that is what cannot be deleted quietly.
    7: "A probe leaves nothing behind, whatever kind of thing it made",
    8: "no Bash command line carries the commit, so no gate reads one",
    9: "An edit must be able to fail",
    10: "Open every file a coordinate names in one call",
    11: "English when the row is absent",
    12: "Do not fix the coordinate",
    13: "until the guarantee is removed and the code still refuses",
    14: "In the same commit",
    15: "before it is committed as a case",
    16: "join it to the commit with `&&` and nothing else",
    17: "never kill by command name",
    18: "never bend the code to pass it",
    19: "removes or corrects what stood on the old fact",
    20: "A structure in the tree is a reference, not a constraint",
}

# The four rules #957 added (spec.md §*Rules the rewrite states in place*).
FOUR_RULES = (17, 18, 19, 20)

# A contract citation outside the contract: the word that names the contract,
# then `§N`, and any `, §M` / `and §M` / `or §M` that follows it.
CITATION = re.compile(
    r"(?:agent-contract(?:/SKILL\.md)?`?|[Cc]ontract(?:'s)?)\s+"
    r"(§\d+(?:\s*(?:,|and|or)\s*§\d+)*)"
)
NUMBER = re.compile(r"§(\d+)")
# Where a bare `§N` is the contract's: the contract itself, and the agent
# definitions, which receive it at startup and cite it bare. A `§N` that
# follows a file name there is that file's.
BARE_HOMES = ("agents",)
OTHER_FILE = re.compile(r"\.(?:md|py)`?(?:'s)?\s*$")
CITED_TREES = ("agents", "skills", "docs", "templates", "hooks", "tests")
CITED_FILES = ("CONTRIBUTING.md",)


def read(rel=CONTRACT):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def frontmatter(text):
    return text.split("\n---\n", 1)[0]


def spans(text):
    """{number: (heading, body_start, body_end)} for every `## §N`, in order.

    The body starts after the heading line, so a pin can never be satisfied
    by the heading itself."""
    heads = list(HEADING.finditer(text))
    out = {}
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        out[int(m.group(1))] = (m.group(2), m.end(), end)
    return out


def bodies(text):
    return {n: text[a:b] for n, (_, a, b) in spans(text).items()}


def missing_pins(text):
    """Every (section, phrase) whose phrase is not inside its own body."""
    found = bodies(text)
    return [
        (number, phrase)
        for number, phrase in PINS.items()
        if phrase not in " ".join(found.get(number, "").split())
    ]


# --- frontmatter -----------------------------------------------------------


def test_the_contract_is_a_skill_that_preloads_and_is_not_a_command():
    head = frontmatter(read())
    assert "name: agent-contract" in head
    assert "user-invocable: false" in head, (
        "the contract would show in the `/` menu as though it were a command"
    )
    assert "disable-model-invocation: true" not in head, (
        "that flag blocks preload — the contract would stop reaching agents "
        "and nothing would say so (docs/experiments/2026-09-03-…)"
    )


def test_the_description_says_what_it_is_and_what_it_is_not():
    """A person reading the skill listing must not run it, and the model
    picking skills must know it is injected rather than chosen."""
    head = " ".join(frontmatter(read()).split())
    assert "Not a command to run" in head
    assert "injects it into each agent at startup" in head
    assert "`skills:`" in head
    assert "NOT for:" in head, "every model-invocable skill states its boundary"


# --- shape -----------------------------------------------------------------


def test_the_sections_are_numbered_from_one_without_a_gap_or_a_repeat():
    numbers = [int(n) for n, _ in HEADING.findall(read())]
    assert numbers == list(range(1, len(numbers) + 1)), numbers


def test_every_pinned_section_exists_and_nothing_is_unpinned():
    """A section with no pin is a rule that can vanish green; a pin with no
    section is a rule that never landed."""
    assert set(spans(read())) == set(PINS)


def test_no_pin_is_its_own_heading():
    """A pin the heading satisfies survives the body being emptied."""
    for number, (heading, _, _) in spans(read()).items():
        assert PINS[number] not in heading, f"§{number} pins its heading"


def test_the_contract_says_it_is_universal_only():
    flat = " ".join(read().split())
    assert "nothing here is one agent's own" in flat
    assert "A role's rules live in that role's definition" in flat


def test_the_numbering_rule_is_stated():
    flat = " ".join(read().split())
    assert "never reused and never re-ordered" in flat
    assert "keeps its number" in flat


# --- the rules -------------------------------------------------------------


@pytest.mark.parametrize("number", sorted(PINS))
def test_each_section_holds_its_rule(number):
    assert (number, PINS[number]) not in missing_pins(read()), (
        f"§{number} no longer says: {PINS[number]}"
    )


def test_the_exit_code_rule_carries_both_forms_in_one_sentence():
    """The wrong form is written out beside the right one on purpose: the
    failure is a habit, so the right form has to be as easy to copy."""
    body = bodies(read())[1]
    sentence = next(
        p for p in body.split("\n\n") if "cmd >/dev/null 2>&1; echo $?" in p
    )
    assert "cmd | tail; echo $?" in sentence
    assert "never" in sentence
    assert "always 0" in sentence


def test_the_root_resolution_rule_states_both_places():
    """§11 says where the `seal/` root is before it sends an agent to the
    `config.md` under it: a session reading only the fallback writes into the
    common git directory of a repository that committed its root."""
    body = " ".join(bodies(read())[11].split())
    assert "means `<repo>/seal/` where" in body, "§11 lost the shared-mode half"
    assert "`$(git rev-parse --git-common-dir)/seal/` otherwise" in body, (
        "§11 lost the local-mode half"
    )
    assert body.index("means `<repo>/seal/` where") < body.index("Record language"), (
        "§11 names the config before it says where the root is"
    )


def test_the_leavings_rule_says_whose_leaving_it_is():
    """Round 1, finding 7 of #120. The widened §7 names a virtual environment
    among its examples, and this repository builds one on purpose and reuses
    it -- `bin/test` exists for exactly that, and its own header prices the
    alternative at 55-58 seconds of setup per call.

    So an agent that writes a probe, runs it through the repository's runner in
    a fresh clone and then follows §7 to the letter deletes the venv its
    probe's run created, and every later call in the segment pays the build
    again. The general form is ratified -- `questions.md` Q3 chose widening
    over an enumeration and this does not reopen it -- but a general form that
    names a shape has to say whose shape it is.

    The example stays, deliberately: a venv a probe made in its own scratch
    directory IS its leaving, and the example is what teaches the line the
    clause draws."""
    body = " ".join(bodies(read())[7].split())
    assert "What the probe made for ITSELF is what goes" in body, (
        "§7 lost the ownership clause, so `a virtual environment` in its own "
        "example list reads as an instruction to delete a reused one"
    )
    assert "never who happened to trigger it" in body, (
        "the test the clause hands a reader went. Ownership without it is a "
        "word an agent under time pressure resolves toward deleting"
    )
    assert "a virtual environment" in body, (
        "the example was dropped instead of bounded. A venv a probe built for "
        "itself is still its leaving, and the example is what draws the line"
    )


# --- the check can fail ----------------------------------------------------


def without_pin(text, number):
    """The contract with §N's pinned phrase deleted from §N's body, as it sits
    in the file — wrapped or not. The heading is left standing."""
    _, start, end = spans(text)[number]
    pattern = r"\s+".join(re.escape(w) for w in PINS[number].split())
    body, n = re.subn(pattern, "", text[start:end], count=1)
    assert n == 1, f"could not find the wrapped form of §{number}'s phrase"
    return text[:start] + body + text[end:]


@pytest.mark.parametrize("number", sorted(PINS))
def test_deleting_a_pinned_phrase_is_caught(number):
    """A pin that survives its own deletion pins nothing."""
    mutated = without_pin(read(), number)
    assert (number, PINS[number]) in missing_pins(mutated)
    assert HEADING.search(mutated) is not None
    assert len(spans(mutated)) == len(PINS), "the heading was deleted too"


def test_moving_a_sentence_to_another_section_is_caught():
    """The pin is scoped to the section, so a rule that keeps its words and
    loses its number — the drift a cited §N cannot survive — is red."""
    text = read()
    _, start, end = spans(text)[15]
    rest = text[start:end]
    _, _, end14 = spans(text)[14]
    # §15 keeps its heading and nothing else; its body now sits under §14.
    moved = text[:end14].rstrip("\n") + "\n" + rest + text[end14:start] + "\n"
    assert (15, PINS[15]) in missing_pins(moved)
    assert (14, PINS[14]) not in missing_pins(moved)
    assert PINS[15] in " ".join(bodies(moved)[14].split())


# --- citations and the four rules (#957) -------------------------------------


def cited_sections(rel, text):
    """[(line, number)] for every contract section `rel` cites.

    Outside the contract a citation names the contract first. The contract
    and the agent definitions cite it bare, so there every `§N` counts unless
    a file name stands right before it."""
    out = []
    bare = rel == CONTRACT.replace(os.sep, "/") or rel.split("/")[0] in BARE_HOMES
    for lineno, line in enumerate(text.splitlines(), 1):
        if bare:
            for m in NUMBER.finditer(line):
                if not OTHER_FILE.search(line[: m.start()]):
                    out.append((lineno, int(m.group(1))))
        else:
            for m in CITATION.finditer(line):
                out.extend((lineno, int(n)) for n in NUMBER.findall(m.group(1)))
    return out


def tree_files():
    yield from CITED_FILES
    for tree in CITED_TREES:
        for base, _, names in os.walk(os.path.join(ROOT, tree)):
            for name in names:
                if name.endswith((".md", ".py", ".yaml", ".json", ".txt")):
                    full = os.path.join(base, name)
                    yield os.path.relpath(full, ROOT).replace(os.sep, "/")


def dangling(files, numbers):
    """[(path:line, §N)] for every cited section the contract does not have."""
    out = []
    for rel, text in files:
        for lineno, n in cited_sections(rel, text):
            if n not in numbers:
                out.append((f"{rel}:{lineno}", f"§{n}"))
    return out


def test_every_cited_section_exists():
    """T3: every contract section the tree cites is a section the contract
    has. #957 moved two numbers (the old §16 into §11, the old §17 to §16),
    and a citation left at an old number points a reader at a different rule
    or at none."""
    numbers = set(spans(read()))
    files = [(rel, read(rel)) for rel in tree_files()]
    assert len(files) > 100, "the walk found almost nothing to read"
    assert sum(len(cited_sections(r, t)) for r, t in files) > 50, (
        "almost no citation was recognised, so a pass would mean nothing"
    )
    assert not dangling(files, numbers), dangling(files, numbers)


@pytest.mark.parametrize(
    "rel, line",
    [
        ("docs/x.md", "as contract §{n} says"),
        ("skills/x/SKILL.md", "(`skills/agent-contract/SKILL.md` §{n})"),
        ("hooks/x.py", "contract §11 and §{n} each"),
        ("agents/x.md", "which §{n} names"),
    ],
)
def test_a_citation_above_the_last_section_is_caught(rel, line):
    """T3 can fail: in every tree and every spelling, a number one above the
    last heading is named."""
    numbers = set(spans(read()))
    text = line.format(n=max(numbers) + 1)
    assert dangling([(rel, text)], numbers) == [(f"{rel}:1", f"§{max(numbers) + 1}")]


def test_another_files_section_in_a_definition_is_not_the_contracts():
    numbers = set(spans(read()))
    text = f"`skills/implement/SKILL.md` §{max(numbers) + 1} owns it"
    assert dangling([("agents/x.md", text)], numbers) == []


def test_the_four_rules_stand_with_their_enforcers():
    """T4: the four rules #957 added each keep their sentence and their
    `check:` line, so a later trim cannot drop one quietly."""
    found = bodies(read())
    for number in FOUR_RULES:
        body = " ".join(found.get(number, "").split())
        assert PINS[number] in body, f"§{number} lost its rule: {PINS[number]}"
        assert re.search(r"^check: \S", found[number], re.M), (
            f"§{number} has no `check:` line"
        )


def test_dropping_an_enforcer_from_one_of_the_four_is_caught():
    text = read()
    _, start, end = spans(text)[FOUR_RULES[0]]
    body = re.sub(r"^check: .*\n?", "", text[start:end], flags=re.M)
    mutated = text[:start] + body + text[end:]
    found = bodies(mutated)
    assert not re.search(r"^check: \S", found[FOUR_RULES[0]], re.M)
