"""The agent contract holds the rules every agent is bound by, one per section.

`skills/agent-contract/SKILL.md` is what #107 asked for: the half of every
spawn prompt that used to be retyped from memory, in one file an agent
receives at startup through its `skills:` frontmatter. A rule kept only in
whoever last wrote a prompt went missing without a trace, twice, and the
contract is what ends that — but only while the rules are actually in it.

So this module reads the contract's shape. Every rule is a numbered section,
numbered from one with no gap, so a rule that goes whole is red. Every
section carries exactly one `check:` line, which names what reads the rule:
a case, an eval case, or `none reader:` and who reads it instead. A rule's
sentences are not pinned here. #1111 found no pin's history showing a catch,
and every pin's change came with its own rule's rewording, so a rule
reworded to the same meaning stays green. A sentence deleted from inside a
rule that keeps its heading and its `check:` line is left to review.

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

# A fact a reader needs fixed character for character, by the rule whose
# body holds it: what the fact is and who reads it, then the spellings that
# carry it. Nothing else of a rule's wording is pinned; its `check:` line
# names what reads it.
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

# A check line as `skills/settle/SKILL.md` *A rule has one shape* states it:
# after any leading spaces, `check: `, lowercase, one space after the colon.
CHECK_LINE = re.compile(r"^ *check: .*$", re.M)


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


def rules_without_one_check_line(text):
    """[N] for every rule whose body holds no `check:` line, or more than one."""
    return [
        number
        for number, body in bodies(text).items()
        if len(CHECK_LINE.findall(body)) != 1
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


def test_the_sections_are_numbered_from_one_without_a_gap_or_a_repeat():
    numbers = [int(n) for n, _ in HEADING.findall(read())]
    assert numbers == list(range(1, len(numbers) + 1)), numbers


def test_every_rule_carries_one_check_line():
    """`seal rules --check` reads the check lines there are, and cannot read
    whether a rule carries one at all (`skills/settle/SKILL.md` *A rule has
    one shape*). A rule with none names nothing that reads it."""
    assert rules_without_one_check_line(read()) == []


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


def test_a_rule_that_loses_or_doubles_its_check_line_is_named():
    """The check-line case can fail at every rule, both ways: a rule whose
    line goes, and a rule that carries a second one. A sentence that names
    `check: ` inside a line is prose, not a second line."""
    text = read()
    for number, (_, start, end) in spans(text).items():
        body = text[start:end]
        line = CHECK_LINE.search(body)
        dropped = body[: line.start()] + body[line.end() :]
        doubled = body[: line.end()] + "\n" + line.group(0) + body[line.end() :]
        for mutated in (dropped, doubled):
            assert rules_without_one_check_line(
                text[:start] + mutated + text[end:]
            ) == [number], number
        prose = (
            body[: line.start()]
            + "Name it on a `check: x` line.\n"
            + body[line.start() :]
        )
        assert rules_without_one_check_line(text[:start] + prose + text[end:]) == []


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
