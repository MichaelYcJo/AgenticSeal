"""A cited section stands in its file, a cited contract rule in the contract,
and a cited name in its file.

This module reads three shapes of citation: the two that
`skills/writing-style/SKILL.md` states, and a name. A file cites another
file's section as the backticked path followed by the section's text in
italics, and the section has to be a heading or a bold rule lead that file
has. Before #1043 one case read such citations, and only those of
`skills/implement/SKILL.md`, so a heading renamed in any other file left its
citations pointing at nothing with the suite green. A file cites a rule of
`skills/agent-contract/SKILL.md` as `contract rule <N>`, and the contract and
`agents/` cite it as `rule <N>`. The rule has to be a section the contract
has. Before #1127 the case that reads these read six trees and five file
extensions, and missed a citation wrapped across a `#` comment marker. A
file cites a name another file binds as `path#name`, the path ending in
`.py`, and the name has to be one that file, parsed with `ast`, binds: a
`def` or `class` at any depth, or a name bound at module scope. Before #1256
nothing read these, and a comment citing a function removed before the
comment was written stood through 25 release tags.

The three readers read one corpus, `corpus(root)`: every path `git ls-files`
lists, outside the prefixes of `tests/censuses.py#RECORDS`, that is on disk
and decodes as UTF-8. Three kinds of tracked file are left out, each for its
reason. A record keeps what it said when it was written, so its citations
are not judged against today's files. A file that does not decode as UTF-8,
such as an image, holds no text to cite from. A file the working tree
deleted cites nothing. Every other tracked file is read, whatever its tree or
extension. Each file is read through `flowing`, so a citation wrapped across
`#` comment lines or across adjacent `.py` string literals reads as one. A
`#` that opens a line of a `.md` file is a heading and is kept.

A name token preceded by a word character, `.`, `/`, `:` or `-` is not
read, so a `<commit>:<path>#<name>` is left unread and no commit is opened.
As for a section, a token is read only where its path's first segment is a
tracked top-level entry, so a bare file name with no directory is read only
where the top level holds that file. A tracked cited file that is not on
disk, does not decode as UTF-8 or does not parse is named in a warning and
decides nothing.

The fixtures below cite files under `manual/`, a top-level entry this
repository does not have, so the case that reads this repository does not
read the fixtures' own citations. A fixture's contract rule number is one
above the contract's last section, computed when the case runs, so this
file holds no dangling contract citation of its own.
"""

import ast
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
# `[(citing file, line, cited file, cited text)]`, the cited text being the
# `*section*` or the `path#name` token, and `excused` is the same with the
# work item directory whose pending rule change corrects it.
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


def holds(field, cited):
    """FIELD, an item's `from` or `to`, holds the citation CITED whole, its
    whitespace collapsed: a `*section*` as written, which its asterisks
    bound, or a `path#name` token as `NAME_TOKEN` reads one, so neither
    `manual/b.py#gone_all` nor `lib/manual/b.py#gone` holds
    `manual/b.py#gone`."""
    flat = " ".join((field or "").split())
    if cited.startswith("*"):
        return cited in flat
    return cited in {m.group(0) for m in NAME_TOKEN.finditer(flat)}


def excuser(rel, line, cited, text, pending):
    """The work item directory of the PENDING item that corrects the citation
    CITED, as written, at LINE of REL, whose text is TEXT, or None. An item
    whose `from` holds the citation whole (`holds`) and whose `to` does not
    corrects it, and so does a `remove` with no `from` whose section holds
    the line (`rule_changes.removed_by`). `parse` reads an item's `file` only
    as a file of the policy root or of one of its groups."""
    for o, item in pending:
        if o.file == rel and o.old is not None:
            if holds(o.old, cited) and not holds(o.new, cited):
                return item
    return rules.removed_by(pending, rel, text, line)


def corpus(root):
    """`(tracked, files)` for the repository at ROOT: `tracked` is every
    path `git ls-files` lists, and `files` is `[(rel, text)]` for each of
    them outside the records that is on disk and decodes as UTF-8."""
    listed = subprocess.run(
        ["git", "-C", root, "ls-files", "-z"], capture_output=True, check=True
    ).stdout.decode("utf-8")
    tracked = [rel for rel in listed.split("\0") if rel]
    # A positive sweep: a file the working tree deleted cites nothing.
    present, _missing = on_disk(
        root, [rel for rel in tracked if not rel.startswith(RECORDS)]
    )
    texts = [(rel, text_of(os.path.join(root, rel))) for rel in present]
    return tracked, [(rel, text) for rel, text in texts if text is not None]


def citations(root):
    """Every citation of another file's section in `corpus(root)`, as a
    `Found`. A citation whose path's first segment is no tracked top-level
    entry is not a repository file's, and is not read."""
    tracked, files = corpus(root)
    top = {rel.split("/")[0] for rel in tracked}
    skills = {m.group(1) for m in map(SKILL_FILE.fullmatch, tracked) if m}
    pending = corrections(root)
    held, read, dangling, excused = {}, 0, [], []
    for rel, text in files:
        for line, target, said in cited_in(rel, text, skills):
            if target.split("/")[0] not in top:
                continue
            read += 1
            if target not in held:
                where = os.path.join(root, *target.split("/"))
                held[target] = sections(text_of(where) if target in tracked else None)
            if resolves(said, held[target]):
                continue
            cited = f"*{said}*"
            item = excuser(rel, line, cited, text, pending)
            if item:
                excused.append((rel, line, target, cited, item))
            else:
                dangling.append((rel, line, target, cited))
    return Found(read, dangling, excused)


# A citation of a name: a path ending in `.py`, then `#` and the name. A
# token preceded by a word character, `.`, `/`, `:` or `-` stands inside a
# longer path, a URL or a `<commit>:<path>`, and is not read.
NAME_TOKEN = re.compile(r"(?<![\w./:-])((?:[\w.-]+/)*[\w.-]+\.py)#(\w+)")
# A statement at module scope whose own bodies still bind at module scope.
OPENS = (ast.If, ast.Try, ast.With, ast.AsyncWith, getattr(ast, "TryStar", ast.Try))


def named_in(rel, text):
    """`[(line, cited file, name, token)]` for each `path#name` TEXT, the text
    of file REL, holds, read through `flowing`, at the line it starts on."""
    flow = flowing(rel, text)
    return [
        (flow.count("\n", 0, m.start()) + 1, m.group(1), m.group(2), m.group(0))
        for m in NAME_TOKEN.finditer(flow)
    ]


def targets(node):
    """The names an assignment target NODE binds: a name, or the names of
    a tuple, a list or a starred target; an attribute or a subscript binds
    none."""
    if isinstance(node, ast.Name):
        return [node.id]
    if isinstance(node, ast.Starred):
        return targets(node.value)
    if isinstance(node, (ast.Tuple, ast.List)):
        return [name for element in node.elts for name in targets(element)]
    return []


def bound(text):
    """The names a citation of the `.py` file holding TEXT can name, or None
    where TEXT is None or `ast` cannot parse it: each `def`, `async def` and
    `class` at any depth, and each name bound at module scope by an
    assignment or an import, also inside a module-level `if`, `try` or
    `with`. A name bound only inside a function body is none of them."""
    if text is None:
        return None
    with warnings.catch_warnings():
        # An invalid escape in a string is the parsed file's to fix.
        warnings.simplefilter("ignore", SyntaxWarning)
        try:
            tree = ast.parse(text)
        except (SyntaxError, ValueError):
            return None
    defined = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
    names = {node.name for node in ast.walk(tree) if isinstance(node, defined)}
    body = list(tree.body)
    while body:
        node = body.pop()
        if isinstance(node, ast.Assign):
            names.update(name for t in node.targets for name in targets(t))
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
            names.update(targets(node.target))
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            names.update((a.asname or a.name).split(".")[0] for a in node.names)
        elif isinstance(node, OPENS):
            body += node.body + getattr(node, "orelse", [])
            body += getattr(node, "finalbody", [])
            body += [s for h in getattr(node, "handlers", []) for s in h.body]
    return names


def names(root):
    """Every citation of a name in `corpus(root)`, as a `Found` whose cited
    text is the `path#name` token. A token whose path's first segment is no
    tracked top-level entry is not read. A cited path that names no tracked
    file binds no name. A tracked cited file that is not on disk, does not
    decode as UTF-8 or does not parse is named in one warning as not read,
    and its citations are neither read nor dangling."""
    tracked, files = corpus(root)
    top = {rel.split("/")[0] for rel in tracked}
    listed = set(tracked)
    pending = corrections(root)
    held, read, dangling, excused = {}, 0, [], []
    for rel, text in files:
        for line, target, name, token in named_in(rel, text):
            if target.split("/")[0] not in top:
                continue
            if target not in held:
                where = os.path.join(root, *target.split("/"))
                held[target] = bound(text_of(where)) if target in listed else set()
            if held[target] is None:
                continue
            read += 1
            if name in held[target]:
                continue
            item = excuser(rel, line, token, text, pending)
            if item:
                excused.append((rel, line, target, token, item))
            else:
                dangling.append((rel, line, target, token))
    for target in sorted(t for t, held_names in held.items() if held_names is None):
        warnings.warn(
            f"`{target}` is cited by name and was not read: it is not on disk, "
            "does not decode as UTF-8 or does not parse, so its citations "
            "decide nothing",
            stacklevel=2,
        )
    return Found(read, dangling, excused)


def shown(target, cited):
    """A citation as a message names it: the `path#name` token, which holds
    its path, or the cited file and the italic section."""
    return f"`{cited}`" if cited.startswith(f"{target}#") else f"`{target}` {cited}"


def assert_resolved(root, reader=citations):
    """Warn once for each citation under ROOT that READER excuses, fail on
    any dangling one, and return the `Found`."""
    found = reader(root)
    for rel, line, target, cited, item in found.excused:
        warnings.warn(
            f"{rel}:{line} cites {shown(target, cited)}, which a pending rule "
            f"change in {item} corrects; it stands until the settle writes "
            "that correction",
            stacklevel=2,
        )
    assert not found.dangling, "a citation names what its file lacks:\n" + (
        "\n".join(
            f"{rel}:{line} cites {shown(target, cited)}"
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


def test_every_cited_name_stands_in_its_file():
    """N1: every `path#name` in this repository names a name its file binds,
    or one a pending rule change corrects (S9). The floor keeps a reader that
    stops matching from passing on nothing read."""
    found = assert_resolved(ROOT, names)
    assert found.read >= 100, (
        f"only {found.read} names recognised, so a pass means nothing"
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


# The commit is joined to its path here, so this file holds no citation at
# a commit for the tree's readers to take as its own.
AT = "f6ae6db6"
ELSEWHERE = f"""`frame/design.md` *Scope*

`plan.md` *Alternatives considered*

`code.claude.com/docs/hooks.md` *Hook input*

`{AT}:manual/b.md` *Gone*

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


# --- name citations (N) ------------------------------------------------------

# A module binding a name in each way a citation can name it.
BINDS = """import os.path
import json as decoder
from collections import OrderedDict as Ordered

LIMIT = 3
FIRST, *REST = (1, 2, 3)
LIMIT += 1
if LIMIT:
    try:
        WIDE: int = 4
    except ImportError:
        NARROW = 1
    finally:
        DONE = True


def helper(argument):
    local = argument
    return local


async def fetch():
    pass


class Box:
    def method(self):
        def inner():
            pass

        return inner
"""

RESOLVING = [
    "os",
    "decoder",
    "Ordered",
    "LIMIT",
    "FIRST",
    "REST",
    "WIDE",
    "NARROW",
    "DONE",
    "helper",
    "fetch",
    "Box",
    "method",
    "inner",
]


def test_a_renamed_name_leaves_its_citation_dangling(tmp_path):
    """N2: a name resolves while its file binds it, at module scope or as a
    `def` or `class` at any depth, and is named with its file and line once
    the definition is renamed."""
    cites = "".join(f"See `manual/b.py#{n}`.\n" for n in RESOLVING)
    root = repo(tmp_path, {"a.md": cites, "manual/b.py": BINDS})
    assert names(root) == Found(len(RESOLVING), [], [])
    pathlib.Path(root, "manual", "b.py").write_text(
        BINDS.replace("def helper", "def renamed"), encoding="utf-8"
    )
    assert names(root).dangling == [
        ("a.md", RESOLVING.index("helper") + 1, "manual/b.py", "manual/b.py#helper")
    ]


def test_a_name_bound_only_in_a_function_does_not_resolve(tmp_path):
    """N3: a local variable is not a unit a reader can open, so a citation
    of one does not resolve, though the file binds the name."""
    root = repo(tmp_path, {"a.md": "`manual/b.py#local`\n", "manual/b.py": BINDS})
    assert names(root) == Found(
        1, [("a.md", 1, "manual/b.py", "manual/b.py#local")], []
    )


def test_a_cited_path_no_tracked_file_has_is_dangling(tmp_path):
    """N4: a path under a tracked entry that names no tracked file binds no
    name, though the file stands on disk untracked, as S7 has it for a
    section."""
    root = repo(
        tmp_path,
        {
            "a.md": "`manual/none.py#helper`\n\n`manual/loose.py#helper`\n",
            "manual/b.py": BINDS,
        },
    )
    pathlib.Path(root, "manual", "loose.py").write_text(BINDS, encoding="utf-8")
    assert names(root).dangling == [
        ("a.md", 1, "manual/none.py", "manual/none.py#helper"),
        ("a.md", 3, "manual/loose.py", "manual/loose.py#helper"),
    ]


def test_a_name_outside_the_repository_or_at_a_commit_is_not_read(tmp_path):
    """N5: a `<commit>:<path>#<name>`, a path whose first segment no tracked
    entry has, and a path that a `/` opens are not read, and nothing opens
    the commit. The token at a commit is built here from the fixture's own
    commit, so this file holds none."""
    root = repo(tmp_path, {"manual/b.py": BINDS})
    commit = subprocess.run(
        ["git", "-C", root, "rev-parse", "--short", "HEAD"],
        capture_output=True,
        check=True,
        encoding="utf-8",
    ).stdout.strip()
    pathlib.Path(root, "a.md").write_text(
        f"`{commit}:manual/b.py#gone`\n\n`elsewhere/b.py#gone`\n\n"
        "`/manual/b.py#gone`\n\n`manual/b.py#helper`\n",
        encoding="utf-8",
    )
    subprocess.run(["git", "-C", root, "add", "a.md"], check=True)
    assert names(root) == Found(1, [], [])


def test_a_cited_file_that_does_not_parse_is_named_and_decides_nothing(tmp_path):
    """N6: a tracked cited file that `ast` cannot parse, or that does not
    decode as UTF-8, is named in one warning as not read, and its citations
    are neither read nor dangling."""
    root = repo(
        tmp_path,
        {
            "a.md": "`manual/broken.py#helper`\n`manual/broken.py#other`\n"
            "`manual/latin.py#helper`\n",
            "manual/broken.py": "def helper(:\n",
        },
    )
    pathlib.Path(root, "manual", "latin.py").write_bytes(b"NAME = '\xe9'\n")
    subprocess.run(["git", "-C", root, "add", "manual/latin.py"], check=True)
    with pytest.warns(UserWarning) as caught:
        assert names(root) == Found(0, [], [])
    assert [str(w.message) for w in caught] == [
        f"`{rel}` is cited by name and was not read: it is not on disk, does "
        "not decode as UTF-8 or does not parse, so its citations decide nothing"
        for rel in ("manual/broken.py", "manual/latin.py")
    ]


@pytest.mark.parametrize("record", RECORDS)
def test_a_record_is_not_read(tmp_path, record):
    """S8: a file under a prefix of `tests/censuses.py#RECORDS` keeps what it
    said when it was written, so its citations are not read, a contract
    rule's and a name's among them (#1127 S4)."""
    numbers = set(spans(read_at_root()))
    cited = f"contract rule {max(numbers) + 1}\n"
    rel = record if record.endswith(".md") else record + "x.md"
    root = repo(
        tmp_path,
        {
            rel: "`manual/b.md` *Gone*\n`manual/b.py#gone`\n" + cited,
            "a.md": "`manual/b.md` *Here*\n`manual/b.py#here`\n" + cited,
            "manual/b.md": "## Here\n",
            "manual/b.py": "here = 1\n",
        },
    )
    assert names(root) == Found(1, [], [])
    assert citations(root) == Found(1, [], [])
    assert contract_dangling(corpus(root)[1], numbers) == [
        ("a.md:3", f"rule {max(numbers) + 1}")
    ]


# --- a pending correction in the policy root (S9) ----------------------------

# A file of the policy root whose citation at line 9 names a section
# `manual/b.md` no longer has, and whose citation at line 11 names a name
# `manual/b.py` no longer binds.
POLICY_CITING = (
    "# A\n\n## Intro\n\nText.\n\n## Old section\n\nSee `manual/b.md` *Old name*.\n"
    "\nSee `manual/b.py#gone`.\n"
)
OLD = "See `manual/b.md` *Old name*."
# The same sentence with the cited text wrapped onto a continuation line of
# the item's field.
WRAPPED = "See `manual/b.md` *Old\n    name*."
NEW = "See `manual/b.md` *New name*."
NAME_OLD = "See `manual/b.py#gone`."
NAME_NEW = "See `manual/b.py#kept`."
# Each shape's reader, and the citation it names: its line, its file, its
# cited text, and the citation as a message names it.
SHAPES = {
    "section": (
        citations,
        (9, "manual/b.md", "*Old name*"),
        "`manual/b.md` *Old name*",
    ),
    "name": (names, (11, "manual/b.py", "manual/b.py#gone"), "`manual/b.py#gone`"),
}


def pending(tmp_path, changes, citing="docs/a.md", policy=None):
    """A repository whose CITING file holds `POLICY_CITING` and whose one
    work item's `## Rule changes` holds CHANGES, or that has no such
    section where CHANGES is None; `seal/config.md` names POLICY as the
    policy root where it is given."""
    design = spec(changes) if changes is not None else "# a work item\n"
    files = {
        citing: POLICY_CITING,
        "manual/b.md": "## New name\n",
        "manual/b.py": "kept = 1\n",
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
        "section",
    ),
    "a change whose from wraps it": (
        "docs/a.md",
        op("change", "Old section", WRAPPED, NEW),
        None,
        "section",
    ),
    "a removal of its section": (
        "docs/a.md",
        op("remove", "Old section"),
        None,
        "section",
    ),
    "a policy root the config names": (
        "policy/a.md",
        op("change", "Old section", OLD, NEW, file="policy/a.md"),
        "policy",
        "section",
    ),
    "a change whose from holds a name": (
        "docs/a.md",
        op("change", "Old section", NAME_OLD, NAME_NEW),
        None,
        "name",
    ),
    "a change that renames the name to a longer one": (
        "docs/a.md",
        op("change", "Old section", NAME_OLD, "See `manual/b.py#gone_all`."),
        None,
        "name",
    ),
    "a change that moves the name's file under a longer path": (
        "docs/a.md",
        op("change", "Old section", NAME_OLD, "See `lib/manual/b.py#gone`."),
        None,
        "name",
    ),
}


@pytest.mark.parametrize(
    ("citing", "changes", "policy", "shape"), EXCUSING.values(), ids=EXCUSING
)
def test_a_pending_correction_excuses_a_policy_citation_and_warns(
    tmp_path, citing, changes, policy, shape
):
    """S9: a citation in a file of the policy root that a pending rule
    change corrects passes until the settle, and is reported once."""
    reader, (line, target, cited), message = SHAPES[shape]
    root = pending(tmp_path, changes, citing, policy)
    with pytest.warns(UserWarning) as caught:
        found = assert_resolved(root, reader)
    assert found.excused == [(citing, line, target, cited, "seal/threads/1-x/")]
    assert [str(w.message) for w in caught] == [
        f"{citing}:{line} cites {message}, which a pending rule change "
        "in seal/threads/1-x/ corrects; it stands until the settle writes that "
        "correction"
    ]


REFUSING = {
    "no section": ("docs/a.md", None, "section"),
    "no item": ("docs/a.md", "- nothing\n  why: no rule changes", "section"),
    "an item naming another file": (
        "docs/a.md",
        op("change", "Old section", OLD, NEW, file="docs/other.md"),
        "section",
    ),
    "a change whose from lacks it": (
        "docs/a.md",
        op("change", "Intro", "Text.", "Other text."),
        "section",
    ),
    "a to that keeps the citation": (
        "docs/a.md",
        op("change", "Old section", OLD, WRAPPED + " Still."),
        "section",
    ),
    "a removal of another section": ("docs/a.md", op("remove", "Intro"), "section"),
    "a removal of a section the file lacks": (
        "docs/a.md",
        op("remove", "No such section"),
        "section",
    ),
    "an addition to its section": (
        "docs/a.md",
        op("add", "Old section", new="A sentence added."),
        "section",
    ),
    "a section parse refuses": (
        "docs/a.md",
        op("change", "Old section", OLD),
        "section",
    ),
    "a file outside the policy root": (
        "manual/a.md",
        op("change", "Old section", OLD, NEW, file="manual/a.md"),
        "section",
    ),
    "a to that keeps the name": (
        "docs/a.md",
        op("change", "Old section", NAME_OLD, NAME_OLD + " Still."),
        "name",
    ),
    "a from that holds a longer name": (
        "docs/a.md",
        op("change", "Old section", "See `manual/b.py#gone_more`.", NAME_NEW),
        "name",
    ),
    "a from that holds the name under a longer path": (
        "docs/a.md",
        op("change", "Old section", "See `lib/manual/b.py#gone`.", NAME_NEW),
        "name",
    ),
}


@pytest.mark.parametrize(
    ("citing", "changes", "shape"), REFUSING.values(), ids=REFUSING
)
def test_a_citation_no_pending_correction_excuses_fails(
    tmp_path, citing, changes, shape
):
    """S9: without an item that corrects that file's citation, or with a
    section `rule_changes.parse` refuses, the citation fails and nothing
    is reported as excused."""
    reader, _, message = SHAPES[shape]
    root = pending(tmp_path, changes, citing)
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        with pytest.raises(AssertionError, match=re.escape(f"cites {message}")):
            assert_resolved(root, reader)
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


def cited_sections(rel, text):
    """[(line, number)] for every contract rule `rel` cites, at the line the
    citation starts on, read through `flowing`."""
    bare = rel == CONTRACT.replace(os.sep, "/") or rel.split("/")[0] in BARE_HOMES
    pattern = BARE_CITATION if bare else CITATION
    flow = flowing(rel, text)
    return [
        (flow.count("\n", 0, m.start()) + 1, int(m.group(1)))
        for m in pattern.finditer(flow)
    ]


def contract_dangling(files, numbers):
    """[(path:line, rule N)] for every rule FILES, a list of `(rel, text)`,
    cites that is not in NUMBERS, the contract's section numbers."""
    out = []
    for rel, text in files:
        for lineno, n in cited_sections(rel, text):
            if n not in numbers:
                out.append((f"{rel}:{lineno}", f"rule {n}"))
    return out


def test_every_cited_section_exists():
    """T3: every contract section the tree cites is a section the contract
    has. A rule that moves or retires leaves its number behind, and a
    citation left at an old number points a reader at a different rule or at
    none."""
    numbers = set(spans(read_at_root()))
    _, files = corpus(ROOT)
    assert len(files) > 100, "the corpus held almost nothing to read"
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


# Files the six-tree walk #1127 replaced did not read: a file at the top
# level, a tree it skipped, and a `.yml` file inside a tree it walked.
OUTSIDE_THE_SIX_TREES = (
    "CLAUDE.md",
    ".github/workflows/x.yml",
    "evals/scripts/x.py",
    "templates/x.yml",
)


def test_a_file_outside_the_six_trees_is_read(tmp_path):
    """#1127 S3: every tracked text file outside the records is read,
    whatever its tree or extension."""
    numbers = set(spans(read_at_root()))
    n = max(numbers) + 1
    root = repo(
        tmp_path, {rel: f"as contract rule {n} says\n" for rel in OUTSIDE_THE_SIX_TREES}
    )
    assert sorted(contract_dangling(corpus(root)[1], numbers)) == sorted(
        (f"{rel}:1", f"rule {n}") for rel in OUTSIDE_THE_SIX_TREES
    )


# A citation wrapped across `#` comment lines, flush and indented, and one
# split across two adjacent `.py` string literals. Each starts on line 1.
WRAPPED_IN_CODE = {
    "hooks/x.py": "# as the contract\n# rule {n} says\n",
    "hooks/x.yml": "  # as the contract\n  # rule {n} says\n",
    "hooks/y.py": 'WHY = ("as the contract "\n       "rule {n} says")\n',
}


@pytest.mark.parametrize("rel", WRAPPED_IN_CODE)
def test_a_citation_wrapped_in_code_is_named_at_the_line_it_starts_on(tmp_path, rel):
    """#1127 S5 and S6: comment markers are dropped and adjacent literals
    joined before the citation is read, and the line it starts on is
    named."""
    numbers = set(spans(read_at_root()))
    n = max(numbers) + 1
    root = repo(tmp_path, {rel: WRAPPED_IN_CODE[rel].format(n=n)})
    assert contract_dangling(corpus(root)[1], numbers) == [(f"{rel}:1", f"rule {n}")]


def near_citations(rel, text):
    """[line] where a near miss of `contract rule <N>` starts in file REL,
    read through `flowing`: such a spelling is neither read as a citation
    nor let pass."""
    flow = flowing(rel, text)
    return [
        flow.count("\n", 0, m.start()) + 1
        for m in NEAR_CITATION.finditer(flow)
        if not CITATION.match(flow, m.start())
    ]


def test_no_file_cites_the_contract_in_a_near_miss():
    found = [
        f"{rel}:{n}" for rel, text in corpus(ROOT)[1] for n in near_citations(rel, text)
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
    assert near_citations("docs/x.md", "intro\n" + shape.format(m=7, n=21)) == [2]


def test_a_near_miss_wrapped_across_comment_markers_is_refused_at_its_line():
    """#1127 S7: a near miss wrapped across `#` comment lines is read as
    one, and refused at the line it starts on."""
    assert near_citations("hooks/x.py", "# per the contract's\n# rule 7\n") == [1]


def test_the_one_spelling_is_no_near_miss():
    assert (
        near_citations("docs/x.md", "intro\ncontract rule 21 and Contract rule 3") == []
    )
