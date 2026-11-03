"""The agent contract holds the rules every agent is bound by, one per section.

`skills/agent-contract/SKILL.md` is what #107 asked for: the half of every
spawn prompt that used to be retyped from memory, in one file an agent
receives at startup through its `skills:` frontmatter. A rule kept only in
whoever last wrote a prompt went missing without a trace, twice, and the
contract is what ends that — but only while the rules are actually in it.

So this module reads the contract's shape. Every rule is a numbered section,
and the numbers increase without a repeat. A rule that retires leaves the
file, and the preamble lists its number as retired. So every number from one
up to the highest that no heading holds is a listed one, and no listed
number holds a heading: a rule that goes whole with its number unlisted is
red, and so is a listed number that still has a section. Only the highest
number used can go unseen, from the list or as a rule, since nothing else
in the file says it was used; that is left to review. A rule's sentences
are not pinned here. #1111 found no pin's history showing a catch, and
every pin's change came with its own rule's rewording, so a rule reworded
to the same meaning stays green. A sentence deleted from inside a rule that
keeps its heading is left to review.

Two facts are pinned, because a reader depends on their characters: rule
1's two command forms, which an agent copies into a shell, and rule 11's two
places the `seal/` root resolves to, which an agent opens or runs. Each is
scoped to its section's BODY, not the file and not the heading: a fact that
moves to another section breaks the number a round record cited, and a
heading that outlives its rule is a section that says nothing.

Two frontmatter facts are pinned as well. `user-invocable: false` keeps the
contract out of the `/` menu and was measured (2026-09-03, docs/experiments/)
not to block preload; `disable-model-invocation: true` is the flag that does
block it, and a contract that stops arriving is the failure with no symptom.
"""

import os
import re

import pytest
from conftest import ROOT

CONTRACT = os.path.join("skills", "agent-contract", "SKILL.md")

# The one reader of a contract heading, `## <N> <title>`. Every other module
# that walks the contract's rules imports it from here.
HEADING = re.compile(r"^## (\d+) (.+)$", re.M)

# The preamble's list of retired numbers, `the retired numbers are 8, 16 and
# 20`, read across a line break.
RETIRED = re.compile(r"retired\s+numbers\s+are\s+((?:\d+,\s+)*\d+(?:\s+and\s+\d+)?)")

# A fact a reader needs fixed character for character, by the rule whose
# body holds it: what the fact is and who reads it, then the spellings that
# carry it. Nothing else of a rule's wording is pinned.
FACTS = {
    1: (
        "the two command forms an agent copies into a shell",
        ("`cmd >/dev/null 2>&1; echo $?`", "`cmd | tail; echo $?`"),
    ),
    11: (
        "the two places the `seal/` root resolves to, which an agent opens or runs",
        ("`<repo>/seal/`", "`$(git rev-parse --git-common-dir)/seal/`"),
    ),
}

SPELLINGS = [(number, spelling) for number in FACTS for spelling in FACTS[number][1]]


def read(rel=CONTRACT):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def frontmatter(text):
    return text.split("\n---\n", 1)[0]


def spans(text):
    """{number: (heading, body_start, body_end)} for every `## <N>`, in order.

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


def missing_facts(text):
    """Every (section, spelling) of FACTS that is not inside its own body."""
    found = bodies(text)
    return [
        (number, spelling)
        for number, spelling in SPELLINGS
        if spelling not in " ".join(found.get(number, "").split())
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


# --- shape -----------------------------------------------------------------


def retired(text):
    """The numbers the preamble, the text before the first rule, lists as
    retired; none where it lists none."""
    match = RETIRED.search(text[: HEADING.search(text).start()])
    return [int(n) for n in re.findall(r"\d+", match.group(1))] if match else []


def numbering_faults(text):
    """[fault] for the contract's numbering: headings that do not increase or
    repeat a number, each number from one up to the highest heading or
    listed number that neither a heading nor the list holds, and each
    listed number a heading holds."""
    numbers = [int(n) for n, _ in HEADING.findall(text)]
    listed = retired(text)
    faults = []
    if numbers != sorted(set(numbers)):
        faults.append(f"the headings do not increase without a repeat: {numbers}")
    for n in range(1, max(numbers + listed) + 1):
        if n not in numbers and n not in listed:
            faults.append(f"{n} has no heading and the preamble does not list it")
        if n in numbers and n in listed:
            faults.append(f"{n} is listed as retired and has a heading")
    return faults


def test_the_sections_are_numbered_from_one_without_a_gap_or_a_repeat():
    assert numbering_faults(read()) == []


def test_a_gap_the_preamble_does_not_list_is_named():
    """A rule that goes whole, with its number left off the list, is red."""
    text = read()
    assert numbering_faults(text) == []
    heads = list(HEADING.finditer(text))
    first, after = heads[0], heads[1]
    mutated = text[: first.start()] + text[after.start() :]
    assert numbering_faults(mutated) == [
        f"{first.group(1)} has no heading and the preamble does not list it"
    ]


def test_a_repeated_number_is_named():
    """A second section under a number already used is red, though no
    number goes missing."""
    text = read()
    assert numbering_faults(text) == []
    first, after = list(HEADING.finditer(text))[:2]
    copy = text[first.start() : after.start()]
    mutated = text[: after.start()] + copy + text[after.start() :]
    numbers = [int(n) for n, _ in HEADING.findall(mutated)]
    assert numbering_faults(mutated) == [
        f"the headings do not increase without a repeat: {numbers}"
    ]


def test_a_listed_number_that_has_a_heading_is_named():
    """A number added to the list while its rule still stands is red."""
    text = read()
    assert numbering_faults(text) == []
    standing = HEADING.search(text).group(1)
    at = RETIRED.search(text).start(1)
    mutated = text[:at] + f"{standing}, " + text[at:]
    assert numbering_faults(mutated) == [
        f"{standing} is listed as retired and has a heading"
    ]


def test_no_pin_is_its_own_heading():
    """A fact the heading satisfies survives the body being emptied."""
    headings = {number: heading for number, (heading, _, _) in spans(read()).items()}
    for number, spelling in SPELLINGS:
        assert spelling not in headings[number], f"rule {number} pins its heading"


# --- the facts -------------------------------------------------------------


@pytest.mark.parametrize("number", sorted(FACTS))
def test_each_section_holds_its_rule(number):
    missing = [s for n, s in missing_facts(read()) if n == number]
    assert missing == [], f"rule {number} no longer holds {FACTS[number][0]}: {missing}"


# --- the check can fail ----------------------------------------------------


def without_fact(text, number, spelling):
    """The contract with one spelling of rule N's fact deleted from its body,
    as it sits in the file — wrapped or not. The heading is left standing."""
    _, start, end = spans(text)[number]
    pattern = r"\s+".join(re.escape(w) for w in spelling.split())
    body, n = re.subn(pattern, "", text[start:end], count=1)
    assert n == 1, f"could not find the wrapped form of {spelling} in rule {number}"
    return text[:start] + body + text[end:]


@pytest.mark.parametrize(
    "number, spelling", SPELLINGS, ids=[f"{n}-{s}" for n, s in SPELLINGS]
)
def test_deleting_a_pinned_phrase_is_caught(number, spelling):
    """A pin that survives its own deletion pins nothing."""
    text = read()
    mutated = without_fact(text, number, spelling)
    assert (number, spelling) in missing_facts(mutated)
    assert len(spans(mutated)) == len(spans(text)), "the heading was deleted too"


def test_moving_a_sentence_to_another_section_is_caught():
    """The fact is scoped to its section, so a rule that keeps its words and
    loses its number — the drift a cited rule number cannot survive — is red."""
    text = read()
    _, start, end = spans(text)[11]
    rest = text[start:end]
    _, _, end10 = spans(text)[10]
    # Rule 11 keeps its heading and nothing else; its body now sits under 10.
    moved = (
        text[:end10].rstrip("\n")
        + "\n"
        + rest
        + text[end10:start]
        + "\n\n"
        + text[end:]
    )
    missing = missing_facts(moved)
    assert [s for n, s in missing if n == 11] == list(FACTS[11][1])
    assert all(s in " ".join(bodies(moved)[10].split()) for s in FACTS[11][1])


def misspelled_headings(text):
    """[line] for every second-level heading of the contract HEADING does not
    read."""
    return [
        lineno
        for lineno, line in enumerate(text.splitlines(), 1)
        if line.startswith("## ") and not HEADING.match(line)
    ]


def test_every_heading_of_the_contract_is_a_numbered_rule():
    """S1 of #1005: a heading in another spelling is not a rule HEADING
    reads, so it is refused at its line rather than skipped."""
    assert misspelled_headings(read()) == []


def test_a_heading_in_the_old_spelling_is_refused_at_its_line():
    text = read()
    first = HEADING.search(text)
    old = f"## \N{SECTION SIGN}{first.group(1)} {first.group(2)}"
    mutated = text[: first.start()] + old + text[first.end() :]
    assert misspelled_headings(mutated) == [text.count("\n", 0, first.start()) + 1]
