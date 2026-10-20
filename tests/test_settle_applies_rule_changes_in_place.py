"""`settle` applies each released spec's `## Rule changes` to the policy root
in place, in merge order, and refuses what it cannot place (#953).

The grammar is `skills/settle/SKILL.md` §*Rule changes*, and
`skills/settle/scripts/rule_changes.py` is its one reader. The first cases
ask that reader directly; the later ones build a git history, because merge
order is a fact only git holds.
"""

import importlib.util
import os
import subprocess

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPTS = os.path.join(ROOT, "skills", "settle", "scripts")


def load(name):
    spec = importlib.util.spec_from_file_location(
        f"specseal_{name}", os.path.join(SCRIPTS, f"{name}.py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


rules = load("rule_changes")
settle = load("settle")


def spec(changes):
    """A spec whose `## Rule changes` section holds CHANGES, with a section
    on either side so the reader has to find where it ends."""
    return (
        "# a work item\n\n## Scope\n\nIn.\n\n## Rule changes\n\n"
        f"{changes}\n\n## Open questions\n\nNone.\n"
    )


def parse(text):
    """The section of TEXT, read against a policy root of `docs/`."""
    return rules.parse(text, "docs")


def line_of(text, needle):
    return text.split("\n").index(needle) + 1


# What the reader says of a no-change line in any other spelling: the block
# it expects, by name (S10).
NO_CHANGE = (
    "a section that holds nothing writes the block `- nothing` with `  why: <reason>`"
)


# --- the reader ---------------------------------------------------------------

ALL_SHAPES = """\
- change
  file: docs/a.md
  section: S
  from: old sentence.
  to: New rule.
- add
  file: docs/a.md
  section: S
  to: **Rule.** Its grounds
    run on.
    check: none reader: review
- remove
  file: docs/a.md
  section: T
- remove
  file: docs/a.md
  section: S
  from: x.
- add
  file: docs/new.md
  to: # New"""


def test_each_shape_reads_into_one_operation_with_its_line():
    text = spec(ALL_SHAPES)
    parsed = parse(text)
    assert parsed.errors == [], parsed.errors
    got = [(o.kind, o.file, o.section, o.old, o.new) for o in parsed.ops]
    assert got == [
        ("change", "docs/a.md", "S", "old sentence.", "New rule."),
        (
            "add",
            "docs/a.md",
            "S",
            None,
            "**Rule.** Its grounds\nrun on.\ncheck: none reader: review",
        ),
        ("remove", "docs/a.md", "T", None, None),
        ("remove", "docs/a.md", "S", "x.", None),
        ("add", "docs/new.md", None, None, "# New"),
    ]
    assert [o.line for o in parsed.ops] == [
        i + 1 for i, line in enumerate(text.split("\n")) if line.startswith("- ")
    ]


def test_the_skills_example_reads_as_the_skill_says():
    """The grammar has one statement, the skill's; its example is read by the
    parser, so the two cannot drift apart."""
    with open(
        os.path.join(ROOT, "skills", "settle", "SKILL.md"), encoding="utf-8"
    ) as f:
        section = f.read().split("\n## Rule changes\n", 1)[1]
    example = section.split("```\n", 2)[1]
    parsed = parse(spec(example.rstrip("\n")))
    assert parsed.errors == [], parsed.errors
    [only] = parsed.ops
    assert (only.kind, only.file, only.section) == (
        "change",
        "docs/the-review-record.md",
        "The round record",
    )
    for kind, (need, may) in rules.GRAMMAR.items():
        row = next(
            line for line in section.splitlines() if line.startswith(f"| `{kind}`")
        )
        fields = row.split("|")[2]
        assert all(f"`{name}`" in fields for name in need + may), row


@pytest.mark.parametrize(
    "body, why",
    [
        ("- nothing\n  why: this item changes no rule.", "this item changes no rule."),
        (
            "- nothing\n  why: this item changes\n    no rule.",
            "this item changes\nno rule.",
        ),
    ],
    ids=["one line", "continued"],
)
def test_the_no_change_block_is_a_section_with_no_operation(body, why):
    """S10. `- nothing` with its one field, `why`, is a section that changes
    no rule: no operation and no error, and the reason read as any field's
    value is."""
    parsed = parse(spec(body))
    assert (parsed.ops, parsed.errors) == ([], [])
    assert parsed.nothing == why


def test_a_spec_with_no_section_is_told_apart_from_an_empty_one():
    """A spec written before the section existed has nothing to replay; an
    empty section is a frame nobody filled in, and it is refused."""
    assert parse("# old\n\n## Scope\n\nIn.\n").ops is None
    assert parse(spec("")).errors


def test_a_section_quoted_in_a_fence_or_a_comment_is_not_read():
    fenced = "# x\n\n```\n## Rule changes\n\n- remove\n  file: docs/a.md\n```\n"
    assert parse(fenced).ops is None
    commented = spec(
        "<!-- the grammar is the skill's\n- remove\n  file: docs/a.md -->\n"
        "- nothing\n  why: a reason."
    )
    parsed = parse(commented)
    assert parsed.errors == [] and parsed.nothing == "a reason."


@pytest.mark.parametrize(
    "body, bad, reason",
    [
        ("- rename\n  file: docs/a.md\n  to: x", "- rename", "`rename`"),
        (
            "- add\n  file: docs/a.md\n  heading: S\n  to: x",
            "  heading: S",
            "`heading`",
        ),
        (
            "- change\n  file: docs/a.md\n  section: S\n  to: y",
            "- change",
            "`from`",
        ),
        (
            "- add\n  file: docs/a.md\n  file: docs/b.md\n  to: x",
            "  file: docs/b.md",
            "twice",
        ),
        (
            "A sentence.\n- remove\n  file: docs/a.md\n  section: S",
            "A sentence.",
            "item",
        ),
        ("- remove\n  file: src/a.md\n  section: S", "- remove", "docs/"),
        ("- remove\n  file: docs/sub/a.md\n  section: S", "- remove", "docs/"),
        ("- add\n  file: docs/..\\..\\evil.md\n  to: x", "- add", "docs/"),
        ("- add\n  file: docs/C:\\x\\evil.md\n  to: x", "- add", "docs/"),
        ("- add\n  file: docs/\\evil.md\n  to: x", "- add", "docs/"),
        ("- add\n  file: docs/sub\\b.md\n  to: x", "- add", "docs/"),
        ("- add\n  file: docs/a.md\n  section: S\n  to:", "  to:", "empty"),
        ("nothing — a reason.", "nothing — a reason.", NO_CHANGE),
        ("nothing - a reason.", "nothing - a reason.", NO_CHANGE),
        ("Nothing — a reason.", "Nothing — a reason.", NO_CHANGE),
        ("- nothing", "- nothing", "`nothing` needs `why`"),
        ("- nothing\n  why:", "  why:", "`why` is empty"),
        (
            "- nothing\n  why: a reason.\n  file: docs/a.md",
            "  file: docs/a.md",
            "`file` is not a field of `nothing`",
        ),
        (
            "- nothing\n  why: a reason.\n- remove\n  file: docs/a.md\n  section: S",
            "- remove",
            "`- nothing` is the section's one item",
        ),
        (
            "- remove\n  file: docs/a.md\n  section: S\n- nothing\n  why: a reason.",
            "- nothing",
            "`- nothing` is the section's one item",
        ),
    ],
    ids=[
        "unknown-op",
        "unknown-field",
        "missing-field",
        "field-twice",
        "outside-an-item",
        "outside-the-root",
        "below-the-top-level",
        "windows-parent",
        "windows-drive",
        "windows-root",
        "windows-subdirectory",
        "empty-value",
        "the em-dash form",
        "the em-dash form with a hyphen",
        "the em-dash form capitalised",
        "the block without why",
        "the block with an empty why",
        "the block with another field",
        "the block beside an operation",
        "the block after an operation",
    ],
)
def test_a_block_that_does_not_match_whole_is_refused_at_its_line(body, bad, reason):
    """Never skipped and never half-read: one error at the line, and the spec
    applies nothing."""
    text = spec(body)
    parsed = parse(text)
    assert parsed.errors, parsed
    line, why = parsed.errors[0]
    assert line == line_of(text, bad), (line, why)
    assert reason in why, why


def test_a_second_block_is_refused_at_its_own_line():
    """The block stands alone, so a second `- nothing` is refused at its own
    line rather than passed unread behind the first; its unknown field would
    otherwise reach nobody."""
    text = spec("- nothing\n  why: a reason.\n- nothing\n  bogus: x")
    parsed = parse(text)
    lines = text.split("\n")
    second = lines.index("- nothing", lines.index("- nothing") + 1) + 1
    assert parsed.errors, parsed
    assert parsed.errors[0][0] == second, parsed.errors
    assert "`- nothing` is the section's one item" in parsed.errors[0][1]
    assert parsed.nothing is None and parsed.ops == []


# --- the replay ---------------------------------------------------------------

DOC = """\
# A policy

## S

Before. old sentence. After.

### S child

Child text.

## T

x.

T's text.

## U

Last.
"""


def replay(doc, *specs, held=None):
    """`(documents, applied, refused)` for SPECS, `(id, changes)` in merge
    order, over one document `docs/a.md` holding DOC."""
    texts = {"docs/a.md": doc}
    ordered = [(i, parse(spec(c)).ops) for i, c in specs]
    return rules.replay(texts.get, ordered, held or {})


def op(kind, section=None, old=None, new=None, file="docs/a.md"):
    lines = [f"- {kind}", f"  file: {file}"]
    for name, value in (("section", section), ("from", old), ("to", new)):
        if value is not None:
            lines.append(f"  {name}: {value}")
    return "\n".join(lines)


def test_a_change_rewrites_the_text_where_it_stands():
    """S1: the rest of the document is byte-identical."""
    docs, applied, refused = replay(
        DOC, ("a", op("change", "S", "old sentence.", "New rule."))
    )
    assert (applied, refused) == (["a"], [])
    assert docs["docs/a.md"] == DOC.replace("old sentence.", "New rule.")


def test_a_rewrapped_sentence_still_matches_and_non_ascii_is_plain_text():
    doc = "# P\n\n## S\n\nA rule that\nwraps — here 🙂 now.\n"
    docs, applied, _ = replay(
        doc,
        ("a", op("change", "S", "rule that wraps — here 🙂 now.", "rule.")),
    )
    assert applied == ["a"]
    assert docs["docs/a.md"] == "# P\n\n## S\n\nA rule.\n"


def test_an_add_ends_its_section_before_the_next_heading():
    """S2. A section with a sub-heading takes the rule at the end of its own
    text, so it is not read as the sub-section's."""
    docs, applied, _ = replay(DOC, ("a", op("add", "T", new="Rule.")))
    assert applied == ["a"]
    assert "T's text.\n\nRule.\n\n## U\n" in docs["docs/a.md"]
    docs, _, _ = replay(DOC, ("a", op("add", "S", new="Rule.")))
    assert "After.\n\nRule.\n\n### S child\n" in docs["docs/a.md"]
    docs, _, _ = replay(DOC, ("a", op("add", "U", new="Rule.")))
    assert docs["docs/a.md"].endswith("Last.\n\nRule.\n")


def test_a_remove_takes_the_text_or_the_whole_section():
    """S3: the section goes up to the next heading of its level or higher."""
    docs, applied, _ = replay(
        DOC, ("a", op("remove", "T", "x.")), ("b", op("remove", "S"))
    )
    assert applied == ["a", "b"]
    assert docs["docs/a.md"] == "# A policy\n\n## T\n\nT's text.\n\n## U\n\nLast.\n"


@pytest.mark.parametrize(
    "change, reason",
    [
        (op("change", "S", "not there.", "y."), "not in"),
        (op("change", "S", "x.", "y."), "not in"),
        (op("change", "Nowhere", "x.", "y."), "no heading"),
        (op("remove", "S", "e"), "not in"),
        (op("change", "T", "tex", "y"), "not in"),
        (op("remove", "S", file="docs/absent.md"), "does not exist"),
        (op("add", new="# again"), "exists"),
    ],
    ids=[
        "text-absent",
        "text-in-another-section",
        "heading-absent",
        "a-word-inside-another",
        "a-word-inside-another-at-the-end",
        "file-absent",
        "add-over-a-document",
    ],
)
def test_a_place_it_cannot_find_refuses_the_spec(change, reason):
    """S4: nothing applies, and the refusal names the spec, the line and the
    reason."""
    docs, applied, refused = replay(DOC, ("a", change))
    assert applied == [] and docs == {}
    [(work_item, line, why)] = refused
    assert work_item == "a" and line == line_of(spec(change), change.split("\n")[0])
    assert reason in why, why


def test_a_heading_or_a_text_found_twice_is_refused():
    doc = DOC + "\n## S\n\nold sentence.\n"
    _, _, refused = replay(doc, ("a", op("change", "S", "old sentence.", "y.")))
    assert "2 times" in refused[0][2], refused
    doc = DOC.replace("After.", "After. old sentence.")
    _, _, refused = replay(doc, ("a", op("change", "S", "old sentence.", "y.")))
    assert "2 times" in refused[0][2], refused


def test_a_heading_inside_a_fence_is_not_a_place():
    doc = "# P\n\n```\n## S\n```\n\n## T\n\nx.\n"
    _, _, refused = replay(doc, ("a", op("add", "S", new="Rule.")))
    assert "no heading" in refused[0][2], refused


def test_a_spec_applies_all_of_its_operations_or_none():
    """S7."""
    both = op("change", "S", "old sentence.", "y.") + "\n" + op("remove", "Nowhere")
    docs, applied, refused = replay(DOC, ("a", both))
    assert applied == [] and docs == {}
    assert refused[0][1] == line_of(spec(both), "- remove")


def test_the_later_spec_applies_over_the_earlier_one():
    """S5, in memory."""
    docs, applied, _ = replay(
        DOC,
        ("a", op("change", "S", "old sentence.", "y.")),
        ("b", op("change", "S", "y.", "z.")),
    )
    assert applied == ["a", "b"]
    assert "Before. z. After." in docs["docs/a.md"]


def test_a_spec_after_a_refused_one_at_its_place_waits():
    """Applying it now would let the earlier spec apply over it at the next
    settle, so the newer one would not win."""
    _, applied, refused = replay(
        DOC,
        ("a", op("change", "S", "not there.", "y.")),
        ("b", op("add", "S", new="Rule.")),
        ("c", op("add", "T", new="Rule.")),
    )
    assert applied == ["c"]
    assert [r[0] for r in refused] == ["a", "b"]
    assert "waits on a," in refused[1][2], refused


def test_a_spec_at_a_section_holding_or_held_by_a_refused_ones_waits():
    """A section's range holds its sub-sections, so `S` and `S child` can
    name one text; a section beside them cannot."""
    _, applied, refused = replay(
        DOC,
        ("a", op("change", "S", "not there.", "y.")),
        ("b", op("change", "S child", "Child text.", "z.")),
        ("c", op("add", "T", new="Rule.")),
    )
    assert applied == ["c"], refused
    assert "waits on a, refused earlier at docs/a.md section `S`" in refused[1][2]


def test_a_held_spec_applies_nothing_and_holds_its_places():
    _, applied, refused = replay(
        DOC,
        ("a", op("add", "S", new="One.")),
        ("b", op("add", "S", new="Two.")),
        held={"a": [(0, "its record holds an open row")]},
    )
    assert applied == []
    assert refused[0] == ("a", 0, "its record holds an open row")


# --- merge order, read from git ---------------------------------------------------


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        encoding="utf-8",
    ).stdout


def item(repo, name, changes):
    path = repo / "seal" / "specs" / name
    path.mkdir(parents=True, exist_ok=True)
    (path / "spec.md").write_text(spec(changes), encoding="utf-8")


def commit(repo, message):
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", message)


@pytest.fixture
def repo(tmp_path):
    repo = tmp_path / "repo"
    (repo / "docs").mkdir(parents=True)
    (repo / "docs" / "a.md").write_text(DOC, encoding="utf-8")
    (repo / "seal").mkdir()
    (repo / "seal" / "README.md").write_text("# seal\n", encoding="utf-8")
    git(repo, "init", "-q", "-b", "main")
    git(repo, "config", "user.email", "x@example.com")
    git(repo, "config", "user.name", "x")
    commit(repo, "base")
    return repo


def files(repo):
    return {
        str(p.relative_to(repo)): p.read_bytes()
        for p in repo.rglob("*")
        if p.is_file() and ".git" not in p.parts
    }


def dry_run(repo, capfd, *args):
    code = settle.main(["--root", str(repo), "--released-at", "main", *args])
    out = capfd.readouterr()
    return code, out.out + out.err


def test_the_dry_run_lists_pending_changes_in_merge_order_and_writes_nothing(
    repo, capfd
):
    """S8, and S5's order: B was added after A on one line of history, so B
    is listed after A whatever their ids say."""
    item(repo, "1700000009-a", op("change", "S", "old sentence.", "y."))
    commit(repo, "a")
    item(repo, "1700000001-b", op("change", "S", "y.", "z."))
    item(repo, "1700000002-c", op("remove", "Nowhere"))
    commit(repo, "b and c")
    before = files(repo)
    code, text = dry_run(repo, capfd)
    assert code == 0, text
    assert files(repo) == before, "the dry run wrote to the tree"
    pending = text.split("pending rule changes")[1].split("\n\n")[0]
    assert "docs/a.md" in pending
    assert pending.index("1700000009-a") < pending.index("1700000001-b"), text
    refused = text.split("refused")[1]
    assert "1700000002-c" in refused and "spec.md:" in refused, text
    removes = text.split("what `settle --apply` would remove")[1]
    assert "1700000009-a" in removes and "1700000001-b" in removes, text
    assert "1700000002-c" not in removes, text


@pytest.mark.parametrize("section", ["S", "S child"])
def test_two_specs_on_parallel_branches_at_one_place_are_a_conflict(
    repo, capfd, section
):
    """S6: ancestry cannot order them, so neither applies there, and both are
    printed for the owner. A sub-section is inside its section's range, so it
    is the same place."""
    git(repo, "switch", "-qc", "one")
    item(repo, "1700000001-a", op("change", "S", "old sentence.", "y."))
    commit(repo, "a")
    git(repo, "switch", "-q", "main")
    git(repo, "switch", "-qc", "two")
    item(repo, "1700000002-b", op("add", section, new="Rule."))
    commit(repo, "b")
    git(repo, "switch", "-q", "main")
    git(repo, "merge", "-q", "--no-ff", "-m", "one", "one")
    git(repo, "merge", "-q", "--no-ff", "-m", "two", "two")
    _, text = dry_run(repo, capfd)
    refused = text.split("refused")[1]
    for name in ("1700000001-a", "1700000002-b"):
        assert name in refused, text
    assert "conflict" in refused, text
    assert "would remove" not in text, text


# --- settle --apply ----------------------------------------------------------------


def apply(repo, capfd):
    return dry_run(repo, capfd, "--apply")


def specs_dir(repo, name):
    return repo / "seal" / "specs" / name


def test_apply_rewrites_in_place_and_removes_the_directory(repo, capfd):
    """S1: the change lands where the text stood, the rest is byte-identical,
    no marker is written, and the directory goes whole, its process record
    included."""
    item(repo, "1700000001-a", op("change", "S", "old sentence.", "New rule."))
    rounds = specs_dir(repo, "1700000001-a") / "rounds"
    rounds.mkdir()
    (rounds / "round-1.md").write_text("# round 1\n", encoding="utf-8")
    commit(repo, "a")
    code, text = apply(repo, capfd)
    assert code == 0, text
    after = (repo / "docs" / "a.md").read_text(encoding="utf-8")
    assert after == DOC.replace("old sentence.", "New rule."), after
    assert "<!-- specs/" not in after
    assert not specs_dir(repo, "1700000001-a").exists(), text
    assert "removed seal/specs/1700000001-a/" in text, text


def test_apply_follows_merge_order(repo, capfd):
    """S5: B was added after A on one line of history, so B applies over A
    although its id sorts first."""
    item(repo, "1700000009-a", op("change", "S", "old sentence.", "y."))
    commit(repo, "a")
    item(repo, "1700000001-b", op("change", "S", "y.", "z."))
    commit(repo, "b")
    code, text = apply(repo, capfd)
    assert code == 0, text
    assert "Before. z. After." in (repo / "docs" / "a.md").read_text(encoding="utf-8")
    assert not specs_dir(repo, "1700000009-a").exists()
    assert not specs_dir(repo, "1700000001-b").exists()


@pytest.mark.rule("a-settle-is-no-deletion")
def test_what_apply_removed_is_settled_for_the_readers(repo, capfd):
    """S9 from `settle`'s side: the CI readers ask
    `unverified_check.py#settled` of the base, and what `--apply` removed
    passes it. It answers for the set one pull request removes: B rewrote
    the text A placed, so A asked alone does not hold."""
    item(repo, "1700000009-a", op("change", "S", "old sentence.", "y."))
    commit(repo, "a")
    item(repo, "1700000001-b", op("change", "S", "y.", "z."))
    commit(repo, "b")
    code, text = apply(repo, capfd)
    assert code == 0, text
    reader = settle.load(settle.READER, "specseal_reader_for_settled")
    both = {"seal/specs/1700000009-a", "seal/specs/1700000001-b"}
    assert reader.settled(str(repo), "HEAD", sorted(both)) == both
    assert reader.settled(str(repo), "HEAD", ["seal/specs/1700000009-a"]) == set()


@pytest.mark.parametrize(
    "change, half",
    [
        (op("remove", "T"), lambda doc: doc),
        (
            op("change", "S", "old sentence.", "New rule."),
            lambda doc: doc.replace("old sentence.", "old sentence. New rule."),
        ),
    ],
    ids=["a section left in place", "the old text left beside the new"],
)
def test_a_rule_change_half_applied_is_not_settled(repo, capfd, change, half):
    """S10 per operation: each text an operation names is counted, the
    heading of a removed section and the `from` of a change included."""
    item(repo, "1700000001-a", change)
    commit(repo, "a")
    reader = settle.load(settle.READER, "specseal_reader_for_half")
    directory = "seal/specs/1700000001-a"
    doc = repo / "docs" / "a.md"
    doc.write_text(half(DOC), encoding="utf-8")
    assert reader.settled(str(repo), "HEAD", [directory]) == set()
    doc.write_text(DOC, encoding="utf-8")
    code, text = apply(repo, capfd)
    assert code == 0, text
    assert reader.settled(str(repo), "HEAD", [directory]) == {directory}


def test_apply_refuses_a_conflict_and_keeps_both(repo, capfd):
    """S6."""
    for branch, name, change in (
        ("one", "1700000001-a", op("change", "S", "old sentence.", "y.")),
        ("two", "1700000002-b", op("add", "S", new="Rule.")),
    ):
        git(repo, "switch", "-qc", branch, "main")
        item(repo, name, change)
        commit(repo, name)
    git(repo, "switch", "-q", "main")
    git(repo, "merge", "-q", "--no-ff", "-m", "one", "one")
    git(repo, "merge", "-q", "--no-ff", "-m", "two", "two")
    code, text = apply(repo, capfd)
    assert code == 1, text
    assert (repo / "docs" / "a.md").read_text(encoding="utf-8") == DOC
    assert specs_dir(repo, "1700000001-a").exists()
    assert specs_dir(repo, "1700000002-b").exists()
    assert "conflict" in text, text


def test_apply_writes_nothing_of_a_refused_spec(repo, capfd):
    """S4 and S7: the first operation would apply, the second cannot, so
    neither does; the refusal names the spec, the line and the reason."""
    both = op("change", "S", "old sentence.", "y.") + "\n" + op("remove", "Nowhere")
    item(repo, "1700000001-a", both)
    commit(repo, "a")
    code, text = apply(repo, capfd)
    assert code == 1, text
    assert (repo / "docs" / "a.md").read_text(encoding="utf-8") == DOC
    assert specs_dir(repo, "1700000001-a").exists()
    line = line_of(spec(both), "- remove")
    assert f"1700000001-a  spec.md:{line}  no heading `Nowhere`" in text, text


OPEN = (
    "# x — overview\n\n## Not verified\n\n| Item | Who must answer |\n"
    "|---|---|\n| a claim nobody ran | the repository owner |\n"
)


def test_an_open_record_row_holds_its_spec(repo, capfd):
    """Nothing open is one of the three things a settled directory holds; a
    row still open is a claim with an answerer, and it never leaves with the
    directory."""
    item(repo, "1700000001-a", op("add", "S", new="Rule."))
    (specs_dir(repo, "1700000001-a") / "overview.md").write_text(OPEN, encoding="utf-8")
    commit(repo, "a")
    code, text = apply(repo, capfd)
    assert code == 1, text
    assert (repo / "docs" / "a.md").read_text(encoding="utf-8") == DOC
    assert specs_dir(repo, "1700000001-a").exists()
    assert "a claim nobody ran" in text, text


def test_nothing_to_apply_leaves_and_a_spec_with_no_section_stays(repo, capfd):
    """A spec whose section is the no-change block states that no rule
    changes, so its directory goes, named under the block. A spec with no
    section was written before it existed, so there is nothing to replay and
    it is kept and named, which is not a refusal."""
    item(repo, "1700000001-a", "- nothing\n  why: a release entry.")
    old = specs_dir(repo, "1700000002-old")
    old.mkdir(parents=True)
    (old / "spec.md").write_text("# old\n\n## Scope\n\nIn.\n", encoding="utf-8")
    commit(repo, "a and old")
    code, text = apply(repo, capfd)
    assert code == 0, text
    assert not specs_dir(repo, "1700000001-a").exists(), text
    assert "no rule to apply (`- nothing`):\n    1700000001-a\n" in text, text
    assert old.exists(), text
    assert "1700000002-old" in text.split("no `## Rule changes`")[1], text
    assert (repo / "docs" / "a.md").read_text(encoding="utf-8") == DOC


@pytest.mark.parametrize("flag", ["--retire", "--retire-process"])
def test_the_retired_flags_are_an_argument_error(repo, flag, capfd):
    """A script that still calls either gets exit 2, which the changelog
    fragment says."""
    with pytest.raises(SystemExit) as raised:
        settle.main(["--root", str(repo), "--released-at", "main", flag])
    assert raised.value.code == 2


def test_a_section_that_does_not_parse_keeps_its_directory(repo, capfd):
    """A parse error leaves the spec no operations, which must not read as a
    spec with nothing to apply."""
    item(repo, "1700000001-a", "- rename\n  file: docs/a.md\n  to: x")
    commit(repo, "a")
    code, text = apply(repo, capfd)
    assert code == 1, text
    assert specs_dir(repo, "1700000001-a").exists(), text
    assert "`rename` is not one of" in text, text


def test_the_text_applied_is_the_spec_as_released(repo, capfd):
    """An edit on disk after the release is not what was reviewed."""
    item(repo, "1700000001-a", op("add", "U", new="Released."))
    commit(repo, "a")
    item(repo, "1700000001-a", op("add", "U", new="Edited later."))
    code, text = apply(repo, capfd)
    assert code == 0, text
    after = (repo / "docs" / "a.md").read_text(encoding="utf-8")
    assert after.endswith("Last.\n\nReleased.\n"), after


def test_a_spec_moved_into_place_is_ordered_by_the_commit_that_moved_it(repo, capfd):
    """git reads a moved directory as a rename, never as an add, unless it is
    told not to; the spec would then have no place in the order."""
    item(repo, "1700000001-old", op("add", "U", new="Rule."))
    commit(repo, "old")
    git(repo, "mv", "seal/specs/1700000001-old", "seal/specs/1700000002-new")
    commit(repo, "renamed")
    code, text = apply(repo, capfd)
    assert code == 0, text
    assert not specs_dir(repo, "1700000002-new").exists(), text


def test_merge_order_is_the_commit_that_adds_the_spec(repo):
    """A work item's directory is born with its `routing.md`, often well
    before its `spec.md`; the order is the spec's, not the directory's."""
    early = specs_dir(repo, "1700000001-a")
    early.mkdir(parents=True)
    (early / "routing.md").write_text("# a — routing\n", encoding="utf-8")
    commit(repo, "a is declared")
    item(repo, "1700000002-b", op("add", "U", new="B."))
    commit(repo, "b")
    item(repo, "1700000001-a", op("add", "U", new="A."))
    commit(repo, "a is framed")
    ids = ["1700000001-a", "1700000002-b"]
    found = [i for i, _ in rules.order(str(repo), "HEAD", ids)]
    assert found == ["1700000002-b", "1700000001-a"], found


def test_a_spec_no_commit_adds_is_held(repo, capfd, monkeypatch):
    """Where the history cannot place a spec, it has no place in the order,
    and it is held rather than applied first or last."""
    item(repo, "1700000001-a", op("add", "U", new="Rule."))
    commit(repo, "a")
    real = settle.load

    def load(path, name):
        module = real(path, name)
        if path == settle.RULES:
            monkeypatch.setattr(
                module, "order", lambda r, f, ids, s: [(i, None) for i in ids]
            )
        return module

    monkeypatch.setattr(settle, "load", load)
    code, text = apply(repo, capfd)
    assert code == 1, text
    assert "no commit on main adds its spec.md" in text, text
    assert specs_dir(repo, "1700000001-a").exists()


# --- the policy root and the one read ------------------------------------------


def configure(repo, *rows):
    table = "".join(f"| {item} | {value} |\n" for item, value in rows)
    (repo / "seal" / "config.md").write_text(
        f"| Item | Value |\n|---|---|\n{table}", encoding="utf-8"
    )


def test_apply_creates_the_policy_root_the_config_names(repo, capfd):
    """S14: with `Policy root` naming `policy/` and no such directory, the
    first `--apply` creates it with its index, writes there, touches no
    `docs/`, and names the index row the new document is owed. The readers
    replay into the same root."""
    configure(repo, ("Policy root", "policy"))
    item(repo, "1700000001-a", op("add", new="# New", file="policy/new.md"))
    commit(repo, "a")
    before = files(repo)
    code, text = apply(repo, capfd)
    assert code == 0, text
    assert (repo / "policy" / "new.md").read_text(encoding="utf-8") == "# New\n"
    assert (repo / "policy" / "README.md").is_file(), text
    docs = {k: v for k, v in files(repo).items() if k.startswith("docs")}
    assert docs == {k: v for k, v in before.items() if k.startswith("docs")}
    assert "policy/README.md has no row naming policy/new.md" in text, text
    reader = settle.load(settle.READER, "specseal_reader_for_policy_root")
    directory = "seal/specs/1700000001-a"
    assert reader.settled(str(repo), "HEAD", [directory]) == {directory}


@pytest.mark.parametrize(
    "names", [("docs/A.md",), ("docs/new.md", "docs/NEW.md")], ids=["disk", "specs"]
)
def test_a_name_that_differs_only_in_case_is_held(repo, capfd, names):
    """On a case-insensitive disk two such names are one file, and the second
    write would erase the first spec's change while its directory went."""
    for n, name in enumerate(names, 1):
        item(repo, f"170000000{n}-a", op("add", new="# X", file=name))
    commit(repo, "case")
    before = files(repo)
    code, text = apply(repo, capfd)
    assert code == 1, text
    assert "differs from another document only in case" in text, text
    assert files(repo) == before, text


def test_apply_names_a_document_past_the_ceiling(repo, capfd):
    """Scope 5: after applying, each document past `Document token ceiling`
    is named as one to split, and that refuses nothing."""
    configure(repo, ("Document token ceiling", "10"))
    item(repo, "1700000001-a", op("add", "U", new="Released."))
    commit(repo, "a")
    code, text = apply(repo, capfd)
    assert code == 0, text
    assert (
        "docs/a.md is about " in text.split("past the ceiling")[0].rsplit("\n", 1)[-1]
    ), text
    assert "past the ceiling of 10: split it along its own headings" in text, text
