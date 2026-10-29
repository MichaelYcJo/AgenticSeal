"""A section another file cites is a heading or a bold rule lead that file has.

A file cites another file's section as the backticked path followed by the
section's text in italics, the shape `skills/writing-style/SKILL.md` states.
Before #1043 one case read such citations, and only those of
`skills/implement/SKILL.md`, so a heading renamed in any other file left its
citations pointing at nothing with the suite green. This module reads every
citation in the tracked text files outside the records and resolves each
against the cited file.

The fixtures below cite files under `manual/`, a top-level entry this
repository does not have, so the case that reads this repository does not
read the fixtures' own citations.
"""

import collections
import os
import pathlib
import re
import subprocess
import warnings

import pytest
from censuses import RECORDS
from conftest import (
    ROOT,
    TABLE,
    build_tracked_tree,
    load_hook_module,
    load_module,
    on_disk,
    op,
    spec,
)
from test_the_agent_contract_holds_the_universal_rules import CONTRACT, spans
from test_the_agent_contract_holds_the_universal_rules import read as read_at_root

rules = load_module(
    os.path.join(ROOT, "skills", "settle", "scripts", "rule_changes.py"),
    "agentic_rule_changes_for_citations",
)
config = load_hook_module("lib/config.py", "agentic_config_for_citations")

# `read` is how many citations of a repository file were read, `dangling` is
# `[(citing file, line, cited file, *cited text*)]`, and `excused` is the
# same with the work item directory whose pending rule change corrects it.
Found = collections.namedtuple("Found", "read dangling excused")


# A citation by path: the backticked path alone, then an optional
# possessive, then the italic text. A `<commit>:<path>` matches, and its
# first segment, which holds the colon, is no tracked top-level entry.
PATH_CITED = re.compile(r"`([^`\s]+\.md)`(?:'s)?\s+\*([^*]+)\*")
# A citation by a skill's name: the name in backticks, or the name and the
# word `skill's`. The second group holds the word where it stands.
NAME_CITED = re.compile(r"`([a-z0-9][a-z0-9-]*)`( skill's)?\s+\*([^*]+)\*")
SKILL_FILE = re.compile(r"skills/([^/]+)/SKILL\.md")
# Outside a `.md` file, a `#` comment marker at the start of a line, so a
# citation wrapped across comment lines reads as one.
COMMENT_MARK = re.compile(r"^([ \t]*)#+[ \t]?", re.M)
# In a `.py` file, a literal's closing quote, the line break, and the next
# literal's opening quote, so adjacent literals read as one.
ADJACENT = re.compile(r"([\"'])[ \t]*\n[ \t]*(?:[rRbBuUfF]{1,2})?\1")
# A list item's marker before a bold rule lead.
LIST_MARK = re.compile(r"(?:[-*+]|\d{1,9}[.)])[ \t]+")


def text_of(path):
    """The UTF-8 text at PATH, or None where it is absent or not UTF-8."""
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read()
    except (OSError, UnicodeDecodeError):
        return None


def flowing(rel, text):
    """TEXT as a citation in file REL is read: adjacent `.py` literals
    joined and comment markers dropped, each line break kept so a match
    counts its line."""
    if rel.endswith(".py"):
        text = ADJACENT.sub("\n", text)
    if not rel.endswith(".md"):
        text = COMMENT_MARK.sub(r"\1", text)
    return text


def cited_in(rel, text, skills):
    """`[(line, cited file, cited text)]` for each citation TEXT makes, the
    line being the one its opening backtick stands on. A cited text holding
    `{` is a format placeholder and is not read."""
    flow = flowing(rel, text)
    found = [(m.start(), m.group(1), m.group(2)) for m in PATH_CITED.finditer(flow)]
    found += [
        (m.start(), f"skills/{m.group(1)}/SKILL.md", m.group(3))
        for m in NAME_CITED.finditer(flow)
        # The bare name is read only where the skill is tracked, since any
        # backticked word can stand before italics; the word `skill's`
        # names a skill, so a removed one leaves its citation dangling.
        if m.group(1) in skills or m.group(2)
    ]
    return sorted(
        (flow.count("\n", 0, at) + 1, target, " ".join(said.split()))
        for at, target, said in found
        if "{" not in said
    )


def sections(text):
    """The texts a citation of the file holding TEXT can name: each live
    heading, and each live bold lead opening a paragraph or a list item, the
    lead's whitespace collapsed."""
    if text is None:
        return []
    r = rules.reader()
    lines = r.gfm_lines(text)
    found = [t for _, _, t in rules.headings(lines)]
    live = [flag for _, flag in r.live_lines(lines)]
    for n, line in enumerate(lines):
        body = line.lstrip()
        marker = LIST_MARK.match(body)
        if marker:
            body = body[marker.end() :]
        opens = marker or n == 0 or not lines[n - 1].strip()
        if not (live[n] and opens and body.startswith("**")):
            continue
        rest, after = body[2:], n + 1
        while "**" not in rest and after < len(lines) and lines[after].strip():
            rest, after = rest + " " + lines[after], after + 1
        if "**" in rest:
            found.append(" ".join(rest.split("**", 1)[0].split()))
    return found


def resolves(said, targets):
    """SAID equals a target, or begins one with the next character neither
    a letter nor a digit; case for case."""
    return any(
        t == said or (t.startswith(said) and not t[len(said)].isalnum())
        for t in targets
    )


def corrections(root):
    """`[(rule_changes.Op, work item directory)]` for every item of a pending
    `## Rule changes`, as `rule_changes.pending` reads them against the
    policy root `hooks/lib/config.py#policy_root` names."""
    return rules.pending(root, config.policy_root(os.path.join(root, "seal")))


def excuser(rel, line, said, text, pending):
    """The work item directory of the PENDING item that corrects the citation
    of *SAID* at LINE of REL, whose text is TEXT, or None. An item whose
    `from` holds the citation and whose `to` does not corrects it, and so
    does a `remove` with no `from` whose section holds the line
    (`rule_changes.removed_by`). `parse` reads an item's `file` only as a
    top-level file of the policy root."""
    cited = f"*{said}*"
    for o, item in pending:
        if o.file == rel and o.old is not None:
            if cited in " ".join(o.old.split()) and cited not in " ".join(
                (o.new or "").split()
            ):
                return item
    return rules.removed_by(pending, rel, text, line)


def citations(root):
    """Every citation of another file's section in the tracked text files
    under ROOT outside the records, as a `Found`. A citation whose path's
    first segment is no tracked top-level entry is not a repository file's,
    and is not read."""
    listed = subprocess.run(
        ["git", "-C", root, "ls-files", "-z"], capture_output=True, check=True
    ).stdout.decode("utf-8")
    tracked = [rel for rel in listed.split("\0") if rel]
    top = {rel.split("/")[0] for rel in tracked}
    skills = {m.group(1) for m in map(SKILL_FILE.fullmatch, tracked) if m}
    # A positive sweep: a file the working tree deleted cites nothing.
    present, _missing = on_disk(
        root, [rel for rel in tracked if not rel.startswith(RECORDS)]
    )
    pending = corrections(root)
    held, read, dangling, excused = {}, 0, [], []
    for rel in present:
        text = text_of(os.path.join(root, rel))
        for line, target, said in cited_in(rel, text or "", skills):
            if target.split("/")[0] not in top:
                continue
            read += 1
            if target not in held:
                where = os.path.join(root, *target.split("/"))
                held[target] = sections(text_of(where) if target in tracked else None)
            if resolves(said, held[target]):
                continue
            item = excuser(rel, line, said, text, pending)
            if item:
                excused.append((rel, line, target, f"*{said}*", item))
            else:
                dangling.append((rel, line, target, f"*{said}*"))
    return Found(read, dangling, excused)


def assert_resolved(root):
    """Warn once for each excused citation under ROOT, fail on any dangling
    one, and return the `Found`."""
    found = citations(root)
    for rel, line, target, cited, item in found.excused:
        warnings.warn(
            f"{rel}:{line} cites `{target}` {cited}, which a pending rule "
            f"change in {item} corrects; it stands until the settle writes "
            "that correction",
            stacklevel=2,
        )
    assert not found.dangling, "a citation names a section its file lacks:\n" + (
        "\n".join(
            f"{rel}:{line} cites `{target}` {cited}"
            for rel, line, target, cited in found.dangling
        )
    )
    return found


# --- the tree ---------------------------------------------------------------


def test_every_cited_section_stands_in_its_file():
    """S1: every citation in this repository names a heading or a bold rule
    lead its file has, or one a pending rule change corrects (S9). The floor
    keeps a reader that stops matching from passing on nothing read."""
    found = assert_resolved(ROOT)
    assert found.read >= 100, (
        f"only {found.read} citations recognised, so a pass means nothing"
    )


# --- fixtures ---------------------------------------------------------------


def repo(tmp_path, files):
    return str(build_tracked_tree(tmp_path / "repo", files))


def test_a_renamed_heading_leaves_its_citation_dangling(tmp_path):
    """S2: a citation resolves while its heading stands, and is named with
    its file and line once the heading is renamed."""
    root = repo(
        tmp_path,
        {
            "a.md": "Intro.\n\nSee `manual/b.md` *Old name* for it.\n",
            "manual/b.md": "# B\n\n## Old name\n\nText.\n",
        },
    )
    assert citations(root) == Found(1, [], [])
    pathlib.Path(root, "manual", "b.md").write_text(
        "# B\n\n## New name\n\nText.\n", encoding="utf-8"
    )
    assert citations(root).dangling == [("a.md", 3, "manual/b.md", "*Old name*")]


def test_a_heading_resolves_a_citation_of_its_opening_words(tmp_path):
    """S3: the cited text equals the heading, or begins it with the next
    character neither a letter nor a digit."""
    cited = ["*2b*", "*2b. Settle*", "*2*", "*2b. Settl*"]
    root = repo(
        tmp_path,
        {
            "a.md": "".join(f"`manual/b.md` {c}\n\n" for c in cited),
            "manual/b.md": "## 2b. Settle what earlier releases left behind\n",
        },
    )
    found = citations(root)
    assert found.read == 4
    assert [c for *_, c in found.dangling] == ["*2*", "*2b. Settl*"]


LEADS = """**First line lead.** It opens the file.

# B

**Commit before you mutate, and restore.** The rest of the rule.

A paragraph whose second line
**Mid paragraph.** is no lead.

- **Clean up only what you started.** The item.
- **A lead that wraps
  across two lines.** The item.

**An unclosed lead

whose paragraph ended.** Text.

```text

**Fenced lead.** An example.

## Fenced heading
```
"""


def test_a_bold_rule_lead_resolves_outside_a_fence_and_case_for_case(tmp_path):
    """S4: a paragraph or list item opening with a bold lead is a section a
    citation can name, in its own case, and not inside a fenced block. A
    bold run in a paragraph's later line, or one its paragraph never closes,
    is no lead."""
    cited = [
        "*First line lead*",
        "*Commit before you mutate*",
        "*commit before you mutate*",
        "*Mid paragraph*",
        "*Clean up only what you started*",
        "*A lead that wraps across two lines*",
        "*An unclosed lead*",
        "*Fenced lead*",
        "*Fenced heading*",
    ]
    root = repo(
        tmp_path,
        {
            "a.md": "".join(f"`manual/b.md` {c}\n\n" for c in cited),
            "manual/b.md": LEADS,
        },
    )
    found = citations(root)
    assert found.read == 9
    assert [c for *_, c in found.dangling] == [
        "*commit before you mutate*",
        "*Mid paragraph*",
        "*An unclosed lead*",
        "*Fenced lead*",
        "*Fenced heading*",
    ]


# The skill names go in through `format`, so the `skill's` lines of this
# module's own text name no skill and the case that reads the tree skips
# them.
SPELLINGS = """`manual/b.md`'s *Gone one*

`{d}` *Gone two*

the `{d}` skill's *Gone three*

`manual/b.md`'s *Here*, `{d}` *Here*, the `{d}` skill's *Here*.

A wrapped `manual/b.md` *Gone
four* here.

`{u}` *Gone five*

`manual/b.md` *Fixed in
#120 here*

`manual/b.md` *Says "yes"
"no" twice*

the `{u}` skill's *Gone six*
""".format(d="drafting", u="unlisted")


def test_each_spelling_of_a_citation_is_read(tmp_path):
    """S5: the possessive, a skill's name and the skill's possessive are
    read. A bare name is read only where `skills/<name>/SKILL.md` is
    tracked; the word `skill's` names a skill, so that spelling of a skill
    nobody tracks is dangling. A citation wrapped across a line is named at
    the line it starts on. A
    markdown file is read as written: a line opening with `#` keeps it, and
    a quote ending one line meets the next line's quote."""
    root = repo(
        tmp_path,
        {
            "a.md": SPELLINGS,
            "manual/b.md": (
                '## Here\n\n## Fixed in #120 here\n\n## Says "yes" "no" twice\n'
            ),
            "skills/drafting/SKILL.md": "## Here\n",
        },
    )
    found = citations(root)
    assert found.read == 10
    assert found.dangling == [
        ("a.md", 1, "manual/b.md", "*Gone one*"),
        ("a.md", 3, "skills/drafting/SKILL.md", "*Gone two*"),
        ("a.md", 5, "skills/drafting/SKILL.md", "*Gone three*"),
        ("a.md", 9, "manual/b.md", "*Gone four*"),
        ("a.md", 20, "skills/unlisted/SKILL.md", "*Gone six*"),
    ]


PYTHON = """# A comment that cites `manual/b.md`
# *Gone in a comment* across two lines.
WHY = (
    "a literal that cites `manual/b.md` "
    "*Gone in literals* across two"
)
NAMED = f"`manual/b.md` *{WHY}*"
HELD = "`manual/b.md` *Here*"
"""


def test_a_citation_in_python_is_read_across_comments_and_literals(tmp_path):
    """S6: `#` comment markers are dropped and adjacent string literals are
    joined, and a cited text holding a placeholder is not read."""
    root = repo(tmp_path, {"b.py": PYTHON, "manual/b.md": "## Here\n"})
    found = citations(root)
    assert found.read == 3
    assert found.dangling == [
        ("b.py", 1, "manual/b.md", "*Gone in a comment*"),
        ("b.py", 4, "manual/b.md", "*Gone in literals*"),
    ]


ELSEWHERE = """`frame/design.md` *Scope*

`plan.md` *Alternatives considered*

`code.claude.com/docs/hooks.md` *Hook input*

`f6ae6db6:manual/b.md` *Gone*

`manual/none.md` *Anything*

`manual/loose.md` *Here*
"""


def test_a_path_outside_the_repository_is_not_read_and_a_missing_file_is(
    tmp_path,
):
    """S7: a path whose first segment no tracked entry has, and a
    `<commit>:<path>`, are not read; a path under a tracked entry that names
    no tracked file is dangling, though the file stands on disk untracked."""
    root = repo(tmp_path, {"a.md": ELSEWHERE, "manual/b.md": "## Here\n"})
    pathlib.Path(root, "manual", "loose.md").write_text("## Here\n", encoding="utf-8")
    assert citations(root) == Found(
        2,
        [
            ("a.md", 9, "manual/none.md", "*Anything*"),
            ("a.md", 11, "manual/loose.md", "*Here*"),
        ],
        [],
    )


@pytest.mark.parametrize("record", RECORDS)
def test_a_record_is_not_read(tmp_path, record):
    """S8: a file under a prefix of `tests/censuses.py#RECORDS` keeps what it
    said when it was written, so its citations are not read."""
    rel = record if record.endswith(".md") else record + "x.md"
    root = repo(
        tmp_path,
        {
            rel: "`manual/b.md` *Gone*\n",
            "a.md": "`manual/b.md` *Here*\n",
            "manual/b.md": "## Here\n",
        },
    )
    assert citations(root) == Found(1, [], [])


# --- a pending correction in the policy root (S9) ----------------------------

# A file of the policy root whose citation at line 9 names a section
# `manual/b.md` no longer has.
POLICY_CITING = (
    "# A\n\n## Intro\n\nText.\n\n## Old section\n\nSee `manual/b.md` *Old name*.\n"
)
OLD = "See `manual/b.md` *Old name*."
# The same sentence with the cited text wrapped onto a continuation line of
# the item's field.
WRAPPED = "See `manual/b.md` *Old\n    name*."
NEW = "See `manual/b.md` *New name*."


def pending(tmp_path, changes, citing="docs/a.md", policy=None):
    """A repository whose CITING file holds `POLICY_CITING` and whose one
    work item's `## Rule changes` holds CHANGES, or that has no such
    section where CHANGES is None; `seal/config.md` names POLICY as the
    policy root where it is given."""
    design = spec(changes) if changes is not None else "# a work item\n"
    files = {
        citing: POLICY_CITING,
        "manual/b.md": "## New name\n",
        "seal/threads/1-x/frame/design.md": design,
    }
    if policy:
        files["seal/config.md"] = TABLE.format(rows=f"| Policy root | {policy} |\n")
    return repo(tmp_path, files)


EXCUSING = {
    "a change whose from holds it": (
        "docs/a.md",
        op("change", "Old section", OLD, NEW),
        None,
    ),
    "a change whose from wraps it": (
        "docs/a.md",
        op("change", "Old section", WRAPPED, NEW),
        None,
    ),
    "a removal of its section": ("docs/a.md", op("remove", "Old section"), None),
    "a policy root the config names": (
        "policy/a.md",
        op("change", "Old section", OLD, NEW, file="policy/a.md"),
        "policy",
    ),
}


@pytest.mark.parametrize(
    ("citing", "changes", "policy"), EXCUSING.values(), ids=EXCUSING
)
def test_a_pending_correction_excuses_a_policy_citation_and_warns(
    tmp_path, citing, changes, policy
):
    """S9: a citation in a file of the policy root that a pending rule
    change corrects passes until the settle, and is reported once."""
    root = pending(tmp_path, changes, citing, policy)
    with pytest.warns(UserWarning) as caught:
        found = assert_resolved(root)
    assert found.excused == [
        (citing, 9, "manual/b.md", "*Old name*", "seal/threads/1-x/")
    ]
    assert [str(w.message) for w in caught] == [
        f"{citing}:9 cites `manual/b.md` *Old name*, which a pending rule change "
        "in seal/threads/1-x/ corrects; it stands until the settle writes that "
        "correction"
    ]


REFUSING = {
    "no section": ("docs/a.md", None),
    "no item": ("docs/a.md", "- nothing\n  why: no rule changes"),
    "an item naming another file": (
        "docs/a.md",
        op("change", "Old section", OLD, NEW, file="docs/other.md"),
    ),
    "a change whose from lacks it": (
        "docs/a.md",
        op("change", "Intro", "Text.", "Other text."),
    ),
    "a to that keeps the citation": (
        "docs/a.md",
        op("change", "Old section", OLD, WRAPPED + " Still."),
    ),
    "a removal of another section": ("docs/a.md", op("remove", "Intro")),
    "a removal of a section the file lacks": (
        "docs/a.md",
        op("remove", "No such section"),
    ),
    "an addition to its section": (
        "docs/a.md",
        op("add", "Old section", new="A sentence added."),
    ),
    "a section parse refuses": ("docs/a.md", op("change", "Old section", OLD)),
    "a file outside the policy root": (
        "manual/a.md",
        op("change", "Old section", OLD, NEW, file="manual/a.md"),
    ),
}


@pytest.mark.parametrize(("citing", "changes"), REFUSING.values(), ids=REFUSING)
def test_a_citation_no_pending_correction_excuses_fails(tmp_path, citing, changes):
    """S9: without an item that corrects that file's citation, or with a
    section `rule_changes.parse` refuses, the citation fails and nothing
    is reported as excused."""
    root = pending(tmp_path, changes, citing)
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        with pytest.raises(AssertionError, match=r"cites `manual/b\.md` \*Old name\*"):
            assert_resolved(root)
    assert caught == []


# --- contract rule citations (#957) ------------------------------------------

# A contract citation is `contract rule <N>`, one number each. The contract
# itself and the agent definitions, which receive it at startup, cite the
# bare `rule <N>`. Both are read across a line break.
CITATION = re.compile(r"\b[Cc]ontract\s+rule\s+(\d+)\b")
BARE_CITATION = re.compile(r"\b[Rr]ule\s+(\d+)\b")
# A spelling that means a contract citation and is not the one CITATION
# reads: a plural or a list, a possessive, or a capital `Rule`.
NEAR_CITATION = re.compile(r"\b[Cc]ontract(?:'s)?\s+[Rr]ules?\s+\d")
BARE_HOMES = ("agents",)
CITED_TREES = ("agents", "skills", "docs", "templates", "hooks", "tests")
CITED_FILES = ("CONTRIBUTING.md",)


def cited_sections(rel, text):
    """[(line, number)] for every contract rule `rel` cites, at the line the
    citation starts on."""
    bare = rel == CONTRACT.replace(os.sep, "/") or rel.split("/")[0] in BARE_HOMES
    pattern = BARE_CITATION if bare else CITATION
    return [
        (text.count("\n", 0, m.start()) + 1, int(m.group(1)))
        for m in pattern.finditer(text)
    ]


def tree_files():
    yield from CITED_FILES
    for tree in CITED_TREES:
        for base, _, names in os.walk(os.path.join(ROOT, tree)):
            for name in names:
                if name.endswith((".md", ".py", ".yaml", ".json", ".txt")):
                    full = os.path.join(base, name)
                    yield os.path.relpath(full, ROOT).replace(os.sep, "/")


def contract_dangling(files, numbers):
    """[(path:line, rule N)] for every cited rule the contract does not have."""
    out = []
    for rel, text in files:
        for lineno, n in cited_sections(rel, text):
            if n not in numbers:
                out.append((f"{rel}:{lineno}", f"rule {n}"))
    return out


def test_every_cited_section_exists():
    """T3: every contract section the tree cites is a section the contract
    has. #957 moved two numbers (the old rule 16 into rule 11, the old rule 17 to rule 16),
    and a citation left at an old number points a reader at a different rule
    or at none."""
    numbers = set(spans(read_at_root()))
    files = [(rel, read_at_root(rel)) for rel in tree_files()]
    assert len(files) > 100, "the walk found almost nothing to read"
    assert sum(len(cited_sections(r, t)) for r, t in files) > 50, (
        "almost no citation was recognised, so a pass would mean nothing"
    )
    assert not contract_dangling(files, numbers), contract_dangling(files, numbers)


@pytest.mark.parametrize(
    "rel, line",
    [
        ("docs/x.md", "as contract rule {n} says"),
        ("skills/x/SKILL.md", "(contract rule {n})"),
        ("hooks/x.py", "Contract rule {n} each"),
        ("skills/x/SKILL.md", "as the contract\nrule {n} says"),
        ("agents/x.md", "which rule {n} names"),
        ("agents/x.md", "which contract rule {n} names"),
        ("skills/agent-contract/SKILL.md", "rule {n} says"),
    ],
)
def test_a_citation_above_the_last_section_is_caught(rel, line):
    """T3 can fail: in every tree and every spelling, a number one above the
    last heading is named, at the line the citation starts on."""
    numbers = set(spans(read_at_root()))
    text = line.format(n=max(numbers) + 1)
    assert contract_dangling([(rel, text)], numbers) == [
        (f"{rel}:1", f"rule {max(numbers) + 1}")
    ]


def test_a_wrapped_citation_is_named_at_the_line_it_starts_on():
    numbers = set(spans(read_at_root()))
    text = f"intro\nas the contract\nrule {max(numbers) + 1} says"
    assert contract_dangling([("skills/x/SKILL.md", text)], numbers) == [
        ("skills/x/SKILL.md:2", f"rule {max(numbers) + 1}")
    ]


def test_a_bare_rule_outside_the_contracts_homes_is_not_a_citation():
    """Outside the contract and `agents/`, `rule <N>` can be any list's rule,
    such as the behaviour suite's pass rules, so only `contract rule <N>`
    is read there."""
    numbers = set(spans(read_at_root()))
    text = f"pass rule {max(numbers) + 1} holds"
    assert contract_dangling([("hooks/x.py", text)], numbers) == []


def near_citations(text):
    """[line] where a near miss of `contract rule <N>` starts, in any file:
    such a spelling is neither read as a citation nor let pass."""
    return [
        text.count("\n", 0, m.start()) + 1
        for m in NEAR_CITATION.finditer(text)
        if not CITATION.match(text, m.start())
    ]


def test_no_file_cites_the_contract_in_a_near_miss():
    found = [
        f"{rel}:{n}" for rel in tree_files() for n in near_citations(read_at_root(rel))
    ]
    assert not found, (
        "cite one contract rule as `contract rule <N>`, one number each: "
        + ", ".join(found)
    )


@pytest.mark.parametrize(
    "shape",
    ["Contract Rule {n}", "contract rules {m} and {n}", "the contract's rule {n}"],
)
def test_a_near_miss_citation_is_refused_at_its_line(shape):
    """A capital `Rule`, a plural with a list, and a possessive each mean a
    contract citation the reader does not read, so each is refused at the
    line it starts on; the shapes are built here so this file holds none."""
    assert near_citations("intro\n" + shape.format(m=7, n=21)) == [2]


def test_the_one_spelling_is_no_near_miss():
    assert near_citations("intro\ncontract rule 21 and Contract rule 3") == []
