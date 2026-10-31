"""Prose in the hand-wrapped documents stays inside 88 display columns.

Nothing else guards this: ruff never opens a markdown file, so a session that
splices a sentence into a paragraph and does not re-wrap leaves a 145-column
line that no check complains about. It happened, which is why this exists.

Width is measured in DISPLAY columns, not characters — a Hangul or CJK
codepoint occupies two. Counting characters would let a Korean line run to
twice the visual width of an English one.

YAML frontmatter is excluded because `description:` is a field tools read, not
prose a reader wraps. That exclusion is load-bearing rather than incidental:
`skills/code-review/SKILL.md:6` is 92 columns, so covering that file at all
depends on it.

Scope is narrower than `agents/*.md` + `skills/*/SKILL.md`, which do not hold
the limit today. These are their current prose maxima, re-derived 2026-09-16
with `prose_lines` and `display_width` below — a number written by hand goes
stale silently, and two of the four once listed here had (#422 reported one):

    skills/writing-style/SKILL.md  209

`agents/crafter.md` and `skills/implement/SKILL.md` were on this list until
#967 wrote them anew, wrapped, and they joined `COVERED`; `agents/tracer.md`
was until #970 did the same.

`skills/commit-pr-convention/SKILL.md` is covered: it was written wrapped, so
it never had a maximum to bring down.

Add a file here once its prose fits, rather than raising LIMIT — the limit is
the thing with value.
"""

import fnmatch
import importlib.util
import os
import unicodedata

import pytest
from conftest import ROOT

LIMIT = 88


def _rules():
    path = os.path.join(ROOT, ".github", "scripts", "rules.py")
    spec = importlib.util.spec_from_file_location("agentic_rules_wrap", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# The check lines are asked of their reader rather than spelled a second time
# here: a skip wider than the reader leaves unwrapped lines nobody checks.
# `seal rules --check` reads every such line a rule file shows (#957).
rules = _rules()


def is_rule_file(relative):
    """Whether `seal rules --check` reads RELATIVE's check lines."""
    return any(fnmatch.fnmatch(relative, p) for p in rules.RULE_FILES)


def _fence_reader():
    path = os.path.join(ROOT, "skills", "verify", "scripts", "unverified_check.py")
    spec = importlib.util.spec_from_file_location("agentic_fence_rule_wrap", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# What is fenced is asked of the shared delimiter rule, `unverified_check.py`'s
# `fence_opener` and `fence_closes`, rather than a toggle of this file's own
# (#658): a toggle on any line starting with three backticks closed a
# four-backtick block at the three-backtick line it quotes, and knew no tilde.
fence_rule = _fence_reader()


def fenced_numbers(lines):
    """1-based numbers of LINES inside a fenced block, delimiters included, a
    block that never closes running to the end.

    **The delimiter rule is shared and the opener is wider, on purpose.** Each
    line is asked with its indentation stripped, so a fence written under a
    list item — `skills/implement/orchestration.md` indents one five spaces,
    and a list item is what moves the column a fence is measured from — is
    still a fence here. The shared rule has no block model and reads that line
    as prose, which put a 155-column command under the limit."""
    out, opener = set(), None
    for number, line in enumerate(lines, 1):
        bare = line.lstrip()
        if opener is None:
            opener = fence_rule.fence_opener(bare)
            if opener is not None:
                out.add(number)
            continue
        out.add(number)
        if fence_rule.fence_closes(bare, opener):
            opener = None
    return out


# Both editions or neither. `CONTRIBUTING.md` requires the two READMEs to move
# together, so every documentation change touches the Korean one — and it was
# the furthest outside the limit, which made it the first file a
# "cover what already fits" rule dropped. That is exactly backwards: the file
# edits reach most often would have been the one nothing guarded.
README_PAIR = ["README.md", "README.ko.md"]

COVERED = [
    *README_PAIR,
    "CONTRIBUTING.md",
    # Wrapped from its first line, so it goes in at birth rather than waiting
    # for the sweep that would otherwise be needed to bring it under.
    "SECURITY.md",
    # The brand notice (#1174), wrapped from its first line, the same way.
    "TRADEMARKS.md",
    "agents/proofer.md",
    # Wrapped from its first line, so it goes in at birth rather than waiting
    # for the sweep that would otherwise be needed to bring it under. It was
    # the first `agents/*.md` file to arrive that way; `framer.md` below is
    # the second.
    "agents/sealer.md",
    # The fifth definition (#84), on the sealer's terms exactly: a file
    # written wrapped has no sweep to owe, so it goes in at birth.
    "agents/framer.md",
    # Written anew and wrapped in #967.
    "agents/crafter.md",
    "skills/implement/SKILL.md",
    "skills/code-review/SKILL.md",
    # Written anew and wrapped in #970.
    "agents/tracer.md",
    "skills/legacy-parity/SKILL.md",
    # The orchestrator's half of the same file (#265). It arrives
    # already wrapped, because it was wrapped as part of the file it
    # was cut from — dropping it here would lose coverage 418 lines
    # of prose already had.
    "skills/code-review/orchestration.md",
    # The orchestrator's half of `implement` (#292), the same way: its prose
    # fits at birth (83 columns, measured when it was cut), where the file it
    # was cut from does not, so covering it here loses nothing and keeps it.
    "skills/implement/orchestration.md",
    # Cut from it in #1148, wrapped as it was.
    "skills/implement/acts.md",
    "skills/implement/multi-repository.md",
    # The bootstrap, cut from that file in #1046, the same way: its prose
    # was covered there, so it goes in at birth and keeps that coverage.
    "skills/implement/bootstrap.md",
    # Wrapped from its first line, so it goes in at birth rather than waiting
    # for the sweep that would otherwise be needed to bring it under.
    "skills/commit-pr-convention/SKILL.md",
    # Wrapped from its first line, so it goes in at birth rather than waiting
    # for the sweep that would otherwise be needed to bring it under.
    "docs/release-checklist.md",
    # The same, and the first `templates/` entry. Its siblings are not here
    # because they hold tree drawings and placeholder rows wider than the
    # limit, and bringing those under is a sweep, not this work item.
    "templates/setup/config.md",
    # Wrapped from their first line, so they go in at birth rather than
    # waiting for a sweep; the directory holds measured platform facts.
    "docs/experiments/README.md",
    "docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force.md",
    "docs/experiments/README.ko.md",
    "docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force.ko.md",
    # Wrapped from its first line, so it goes in at birth rather than waiting
    # for the sweep that would otherwise be needed to bring it under.
    "skills/agent-contract/SKILL.md",
    # The core (#1177), moved whole out of `CLAUDE.md` and wrapped there, so
    # it goes in at birth with no sweep to owe.
    "skills/core/SKILL.md",
    # The twenty-fourth skill (#458), on the same terms: written wrapped, so
    # it has no sweep to owe and goes in with its first commit.
    "skills/settle/SKILL.md",
    # The same, and the tracker's own authority: it was written wrapped, so it
    # never had a maximum to bring down.
    "docs/issues-and-milestones.md",
    # Wrapped from its first line, so it goes in at birth. Nearly all of it is
    # HTML comments, which GitHub does not render and this file does not skip
    # — and the edit box a contributor reads them in wraps nothing for them,
    # so the limit is doing visible work here rather than tidying a source.
    ".github/PULL_REQUEST_TEMPLATE.md",
    # The policy documents the first fold wrote. Each was written wrapped,
    # so each goes in at birth with no sweep to owe.
    "docs/the-broad-gate.md",
    "docs/measuring-a-run.md",
    "docs/the-agent-set.md",
    # The routing check's documents, each written wrapped and in at birth.
    "docs/the-session-hooks.md",
    "docs/the-routing-check.md",
    "docs/the-review-and-parity-arms.md",
    # The pact's policy (#647), written wrapped and in at birth.
    "docs/the-pact.md",
]


def display_width(line):
    """Columns the line occupies: East Asian Wide and Fullwidth count as two."""
    return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in line)


def prose_lines(text, rule_file=False):
    """Every line that is hand-wrapped prose.

    Skipped: YAML frontmatter, fenced code, table rows, images and block
    quotes (all wrap on their own terms or not at all), any line carrying a
    URL, which cannot be broken, and a check line.

    **A check line is not prose either.** Its reader reads one line, so a
    wrapped one is a broken target or a reader cut short, and two test paths
    already overflow the limit. The lines skipped are the check lines
    `rules.py#check_lines` finds in a RULE_FILE and `rules.py#parse` reads,
    and no others, so a line it refuses, and every line outside a rule file,
    are still held here.
    """
    lines = text.splitlines()
    enforced = set()
    if rule_file:
        enforced = {
            number
            for number, _heading, line in rules.check_lines(text)
            if not rules.parse(line)[2]
        }
    fenced = fenced_numbers(lines)
    in_frontmatter = lines[:1] == ["---"]
    for number, line in enumerate(lines, 1):
        if in_frontmatter:
            if number > 1 and line.strip() == "---":
                in_frontmatter = False
            continue
        stripped = line.strip()
        if number in fenced or stripped.startswith(("|", "![", ">")):
            continue
        if "http://" in line or "https://" in line:
            continue
        if number in enforced:
            continue
        yield number, line


@pytest.mark.parametrize("relative", COVERED)
def test_prose_stays_within_the_wrap_limit(relative):
    with open(os.path.join(ROOT, relative), encoding="utf-8") as handle:
        text = handle.read()
    over = [
        (number, display_width(line))
        for number, line in prose_lines(text, rule_file=is_rule_file(relative))
        if display_width(line) > LIMIT
    ]
    assert not over, "\n".join(
        f"{relative}:{number} is {width} columns (limit {LIMIT})"
        for number, width in over
    )


def test_the_check_can_fail():
    """A limit nothing can trip is not a limit."""
    long_line = "word " * 30
    assert display_width(long_line) > LIMIT
    assert list(prose_lines(long_line)) == [(1, long_line)]


def test_both_readmes_are_covered_together():
    """Neither README may be dropped from COVERED without the other."""
    covered = [f for f in README_PAIR if f in COVERED]
    assert covered == README_PAIR, (
        "README.md and README.ko.md are covered together or not at all — "
        f"COVERED holds {covered}"
    )


def test_wide_characters_count_double():
    assert display_width("가나다") == 6
    assert display_width("abc") == 3


def test_tables_and_fences_are_not_prose():
    text = "| a | b |\n```\nlong fenced line\n```\nplain\n"
    assert [line for _, line in prose_lines(text)] == ["plain"]


def test_a_fence_is_read_by_the_shared_rule():
    """#658, phase 8 of work item 1790635413. The toggle flipped on any line
    starting with three backticks, so a ```` ```` ```` block quoting a
    ```` ``` ```` block closed at the inner delimiter and its content was
    held to the limit as prose, and a tilde fence was no fence at all. The
    rule is `unverified_check.py#fence_spans`."""
    nested = "````\n```\nquoted inside\n```\n````\nplain\n"
    assert [line for _, line in prose_lines(nested)] == ["plain"]
    tilde = "~~~\nquoted\n~~~\nplain\n"
    assert [line for _, line in prose_lines(tilde)] == ["plain"]
    under_a_list_item = "- a step:\n\n     ```bash\n     a command\n     ```\nplain\n"
    assert [line for _, line in prose_lines(under_a_list_item)] == [
        "- a step:",
        "",
        "plain",
    ], "a fence under a list item is a fence to this check, with a wider opener"


# Two targets wider than the limit together, as rule files write them.
WIDE_TARGET = (
    "tests/text/test_a_document_has_room_for_the_next_fold.py "
    "tests/behaviour/test_the_rules_command_reads_each_rule_off_its_test.py"
)
WIDE_READER = "none reader: " + "the proofer at review " * 4


def test_a_check_line_in_a_rule_file_is_skipped_wherever_it_stands():
    """A rule file's check line is not prose, inside a rule paragraph or not
    (#957), with targets or with a reader.

    An agent definition closes each rule with one such line, and
    `seal rules --check` reads every one in a rule file, so a wrapped line is a
    broken target. The skip is that reader's: `rules.py#check_lines` read by
    `rules.py#parse`, in a file `RULE_FILES` names. Outside a rule file the
    line is still held, which the case below keeps."""
    loose = f"check: {WIDE_TARGET}"
    reader = f"check: {WIDE_READER}"
    assert display_width(loose) > LIMIT and display_width(reader) > LIMIT
    text = f"# D\n\n**Rule.** It holds.\n{loose}\n\n**Other.** It too.\n{reader}\n"
    numbers = [n for n, _ in prose_lines(text, rule_file=True)]
    assert 4 not in numbers and 7 not in numbers, numbers
    assert 3 in numbers and 6 in numbers, numbers
    assert 4 in [n for n, _ in prose_lines(text)]
    assert is_rule_file("agents/proofer.md")
    assert is_rule_file("skills/code-review/SKILL.md")
    assert not is_rule_file("README.md")


def test_a_line_the_reader_refuses_is_still_prose():
    """S8. The skip is no wider than the reader: a spelling `seal rules --check`
    refuses stays under the limit in a rule file."""
    for label in ("Enforced by:", "Check:", "check: none"):
        text = f"# D\n\n{label} {WIDE_TARGET}\n"
        assert 3 in [n for n, _ in prose_lines(text, rule_file=True)], text
