"""#386 and #417: the checklist does not stop at the tag, and the merge-method
rule names the reader that arrived from outside.

  A5  a reader working down `docs/release-checklist.md` passes the tag and
      meets two boxes, each carrying the command that answers it
  A8  `docs/branch-and-release.md`'s squash rule cites the checklist section
      whose box reads what an outside directory pins, and names the file that
      holds the plugin's one name

**A box carrying no command is the defect this work item is about**, one layer
up: #386's measurement is that a step written as a sentence beside a step with
a reader is the one that stops happening. So the command is asserted, not only
the box — and it is asserted to be a command the tree can actually run, which
is what `test_each_box_names_something_that_exists` is for. A box naming a
script nobody wrote reads exactly like a box naming one somebody did.

**Position is asserted, not just presence.** A5's *Then* is that the boxes
follow the tag. A box above `git tag` would be read before the act it is about
has happened, and a reader working down the file would tick it against the
previous release.

**Every assertion reads the file with its wraps collapsed.** These documents
are hand-wrapped at 88 columns (`tests/behaviour/test_docs_line_wrap.py` covers
`docs/release-checklist.md`), so a phrase pinned as written on one line breaks
the moment a word is added earlier in the paragraph — the reader
`tests/behaviour/test_a_release_is_sized_by_a_criterion.py` already uses, for the reason
its own docstring gives.

**Shown red before it was committed (contract rule 15).** Each case was run against the two
documents with the sentence or box it pins removed; the mutations and what
each case said were recorded in
phase 2 of work item `1790076050-the-release-tail-is-three-acts-no-document-names`,
whose rule `docs/branch-and-release.md` *Cutting a release* now carries.
"""

import os
import re

from conftest import ROOT

CHECKLIST = "docs/release-checklist.md"
AFTER_THE_MERGE = "*6. After the merge*"
BRANCHING = "docs/branch-and-release.md"

# The two commands the boxes carry. Each is a real invocation, and the second
# element is the file it has to reach, so a renamed script fails here rather
# than at a release.
COMMANDS = (
    ("gh release view vX.Y.Z", None),
    (
        "python3 .github/scripts/plugin_directory_check.py",
        ".github/scripts/plugin_directory_check.py",
    ),
)


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as handle:
        return handle.read()


def flat(text):
    """The text with every run of whitespace collapsed to one space."""
    return " ".join(text.split())


def section(rel, heading):
    """One `##` section's text, heading included, up to the next `##`."""
    text = read(rel)
    start = text.index(heading)
    rest = text[start + len(heading) :]
    after = re.search(r"^## ", rest, re.M)
    return heading + (rest[: after.start()] if after else rest)


def after_the_tag():
    """`docs/release-checklist.md` *6. After the merge* from the acts after the tag on.

    A5's *Then* is about what FOLLOWS the tag, which the merge's workflow
    creates. A box above that paragraph is one a reader working down the file
    ticks against the release before this one.
    """
    body = section(CHECKLIST, "## 6. After the merge")
    return body[body.index("Two acts come after the tag") :]


def boxes(text):
    """Every checklist box in `text`, each flattened to one line."""
    found = []
    for line in text.splitlines():
        if line.lstrip().startswith("- [ ]"):
            found.append([line])
        elif found and line.strip() and line.startswith(" " * 6):
            found[-1].append(line)
        elif found and not line.strip():
            found.append(None)
            found = [f for f in found if f is not None]
    return [flat(" ".join(block)) for block in found]


# --- A5 --------------------------------------------------------------------


def test_two_boxes_follow_the_tag_and_each_carries_its_command():
    """A5. Both halves, because either alone is the failure: a box with no
    command cannot be acted on, and a command with no box is not a step."""
    tail = after_the_tag()
    for command, _ in COMMANDS:
        assert command in flat(tail), (
            f"{CHECKLIST} {AFTER_THE_MERGE} does not carry {command!r} after "
            "the tag, so the "
            "box it answers is one a reader cannot act on"
        )
        owning = [b for b in boxes(tail) if command in b]
        assert owning, (
            f"{command!r} is in {AFTER_THE_MERGE} but not inside a box — a "
            "command beside a "
            "step is the shape #386 measured being skipped three times"
        )


def test_the_note_box_names_the_workflow_and_the_command_that_reads_its_run():
    """The workflow publishes the note; the box reads whether it did, so it
    names the workflow and a command that reads the workflow's run."""
    box = [b for b in boxes(after_the_tag()) if "gh release view" in b]
    assert box, "no box carries the release-note command"
    # The workflow file a person opens when the note is missing.
    assert "publish-release.yml" in box[0], (
        "the box does not name the workflow, so there is nothing to go read "
        "when the release note is missing"
    )
    # Naming the workflow and giving a way to READ its run are two things,
    # and the box carried the first while losing the second under a measured
    # mutation. A reader who finds no release is one command short of knowing
    # why, and this repository's whole argument for the workflow shape is that
    # the answer should not be somebody remembering where to click. The
    # command a person types to read the run.
    assert "gh run list" in box[0], (
        "the box names the workflow without a command that reads its run, so "
        "a missing release note sends the reader to a UI rather than to an "
        "answer"
    )


def directory_box():
    box = [b for b in boxes(after_the_tag()) if "plugin_directory_check.py" in b]
    assert box, "no box carries the directory command"
    return box[0]


def test_the_directory_box_names_the_page_a_person_opens():
    """#858 A5: the directory answers a challenge page to any script, so the
    box names the page a person opens for each kind of listing."""
    box = directory_box()
    # The two pages a person opens to read the directory's answer, the
    # portal's for a portal listing and the Console's for a Console one.
    for page in ("Submissions page", "Console page"):
        assert page in box, f"the box does not name the {page}"


def test_the_directory_box_records_which_kind_of_listing_it_is_with_a_date():
    """#858 A6. Nothing in the tree can see the plugin's listing move from the
    Console to the portal, so the sentence saying which kind it is carries
    whose reading it is and when — a reader can then tell it has aged — and
    says what that kind means for a release and where the move is
    documented."""
    sentences = re.split(r"(?<=\.) ", directory_box())
    kind = [s for s in sentences if "The plugin's listing is a Console listing" in s]
    assert kind, "the box does not say which kind of listing the plugin's is"
    assert re.search(r"\b\d{4}-\d{2}-\d{2}\b", kind[0]), (
        f"the kind sentence carries no date: {kind[0]!r}"
    )
    assert "reading" in kind[0], (
        f"the kind sentence does not say it is somebody's reading: {kind[0]!r}"
    )
    assert "no new version" in kind[0], (
        "the kind sentence does not say what a Console listing means for a "
        f"release: {kind[0]!r}"
    )
    assert "claude.com/docs/directory/publish" in kind[0], (
        f"the kind sentence does not say where the move is documented: {kind[0]!r}"
    )


def test_each_box_names_something_that_exists():
    """A box naming a script nobody wrote reads exactly like a box naming one
    somebody did, and a reader finds out at the release."""
    for command, path in COMMANDS:
        if path is None:
            continue
        assert os.path.exists(os.path.join(ROOT, path)), (
            f"{CHECKLIST} {AFTER_THE_MERGE} tells a reader to run {command!r} "
            f"and {path} is "
            "not in the tree"
        )


# --- A8 --------------------------------------------------------------------


def squash_rule():
    """The paragraph enumerating who points at a release branch's commits.

    From the sentence that opens the enumeration to the next bold lead-in
    after the two this work item added, so a sentence dropped into a different
    part of the document does not satisfy these assertions.
    """
    text = read(BRANCHING)
    start = text.index("**What breaks when the last row is squashed.**")
    rest = text[start:]
    end = rest.index("**Two rulesets enforce the merge methods.**")
    return flat(rest[:end])


def test_the_squash_rule_cites_the_box_that_reads_what_is_pinned():
    """A8. The third reader of a release branch's commits is outside this
    repository, and the rule points to the checklist section whose box reads
    what it pins."""
    rule = squash_rule()
    # The section a reader of the squash rule resolves to the box.
    assert "docs/release-checklist.md` *6. After the merge*" in rule, (
        "nothing points from the rule to the box that reads what is pinned"
    )


def test_the_fixed_name_sentence_names_the_file_that_holds_the_name():
    """A8's second half: the plugin's name is fixed, and the sentence says
    which file holds its one copy."""
    rule = squash_rule()
    # The path `.claude-plugin/plugin.json`, the file a reader opens for the
    # one spelling of the plugin's name.
    assert ".claude-plugin/plugin.json` holds the one copy" in rule, (
        "the sentence says the name is fixed without saying where the one "
        "copy of it lives, so a reader cannot tell which spelling is the name"
    )
