"""A change writes a changelog fragment; the release gathers them.

Issue #46: one fragment per work item, gathered at release, because three
branches running in parallel shared exactly one file, the changelog. The
cases here read the workflow that runs the check, the documents that send a
change to its fragment, and this repository's own changelog and records.

#942's phase 6 placed the cases of `.github/scripts/gather_changelog.py`'s
functions in `tests/test_gather_changelog.py`.
"""

import os
import re

from conftest import flat, gathered_entry, read, workflow_step

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, ".github", "scripts", "gather_changelog.py")


def test_the_release_pull_request_runs_the_check():
    """A convention nothing enforces is a convention somebody forgets at the
    release, which is the last moment anyone is looking."""
    workflow = read(".github", "workflows", "hygiene.yml")
    assert "gather_changelog.py --check" in workflow, (
        "the release workflow does not check the fragments"
    )
    assert os.path.isfile(SCRIPT), "the workflow calls a script that is not there"


def test_the_check_only_runs_for_a_release():
    """On a feature pull request every fragment on the branch is legitimately
    ungathered — running it there would fail every branch that writes one."""
    workflow = read(".github", "workflows", "hygiene.yml")
    step = workflow_step(workflow, "every changelog fragment reached the released file")
    assert 'github.base_ref }}" != "main"' in step, (
        "the step no longer skips itself outside a release pull request"
    )


def test_the_accumulation_section_no_longer_exists():
    """`## Unreleased` is what the fragments replace.

    A heading by that name means somebody went back to appending to the shared
    file, which is the whole defect. `test_release_hygiene.py` used to check
    that it sat above every dated section; there is no longer one to place.
    """
    headings = re.findall(r"^## (.+)$", read("CHANGELOG.md"), re.M)
    unreleased = [h for h in headings if h.lower().startswith("unreleased")]
    assert not unreleased, (
        f"CHANGELOG.md has {unreleased} again. An entry goes in "
        "seal/specs/<work-item-id>/changelog.md, and the release gathers them"
    )


VERSION_NAME = re.compile(r"^(\d+)\.(\d+)\.(\d+)\.md$")


def release_files_on_disk():
    """`[(version, text)]` for every `changelog/<X.Y.Z>.md` in the working
    tree, newest first. Listed from the disk, not from `git ls-files`: a
    release preparation runs the suite before the new file is staged (#728,
    spec D9), and an index line whose file the listing missed would read as
    a file that is not there."""
    directory = os.path.join(ROOT, "changelog")
    found = []
    for name in os.listdir(directory):
        parts = VERSION_NAME.match(name)
        if parts:
            with open(os.path.join(directory, name), encoding="utf-8") as f:
                found.append((tuple(map(int, parts.groups())), name[:-3], f.read()))
    return [(version, text) for _, version, text in sorted(found, reverse=True)]


def test_the_index_and_the_release_files_agree():
    """S2 of #728. Each `changelog/<v>.md` opens with its one `## ` line,
    naming `<v>`; `CHANGELOG.md` carries that same line once per file, newest
    first, each followed by the link to its file, and no other `## ` line.
    The heading lives in both places on purpose (spec D2), and this is what
    keeps the two copies one line."""
    files = release_files_on_disk()
    assert len(files) >= 44, f"{len(files)} release files — this case is blind"
    want = []
    for version, text in files:
        lines = text.split("\n")
        sections = [line for line in lines if line.startswith("## ")]
        assert sections == [lines[0]], (
            f"changelog/{version}.md has {sections} as its `## ` lines; a "
            "release file opens with its one heading and carries no other"
        )
        assert re.match(rf"## {re.escape(version)} — \S+$", lines[0]), lines[0]
        assert text.endswith("\n") and not text.endswith("\n\n"), (
            f"changelog/{version}.md does not end with exactly one newline"
        )
        want.append(f"{lines[0]}\n\n[changelog/{version}.md](changelog/{version}.md)")
    index = read("CHANGELOG.md")
    at = index.index("\n## ")
    assert "\n\n".join(want) + "\n" == index[at + 1 :], (
        "CHANGELOG.md's entries are not the release files' headings, newest "
        "first, each with the link to its file. The gather writes both: "
        "`gather_changelog.py --version X.Y.Z`"
    )


def test_the_documents_send_a_change_to_its_own_fragment():
    """Where an entry goes is decided in one home since #715,
    `docs/the-record-layout.md`, beside the release sequence that gathers it;
    `CONTRIBUTING.md`, where a contributor stops first, sends the reader there
    by name rather than saying it again. `CLAUDE.md` sent its reader there
    too until #940. The party that builds the work item writes the fragment,
    and `skills/code-review/orchestration.md` names that party at the step
    that waits on the fragment, before the preflight."""
    for parts in (("docs", "the-record-layout.md"), ("docs", "branch-and-release.md")):
        text = flat(*parts)
        assert "seal/specs/<work-item-id>/changelog.md" in text, (
            "/".join(parts) + " does not name the file a change writes"
        )
    review = flat("skills", "code-review", "orchestration.md")
    assert (
        "The party that builds the work item writes that fragment: the smith, or "
        "you where `routing.md` answers `Implementation` with `the session` "
        "(`docs/the-record-layout.md` *A change writes fragments, never a shared "
        "file*)."
    ) in review, "the step before the preflight does not say who writes the fragment"
    for parts in (("CONTRIBUTING.md",),):
        assert "docs/the-record-layout.md" in flat(*parts), (
            "/".join(parts) + " does not send the reader to the fragment rule's home"
        )


def test_the_release_sequence_names_the_gather_step():
    """The sequence in `docs/branch-and-release.md` is walked by whoever cuts
    a release. A step that is only in a workflow comment is a step that gets
    discovered by a red build."""
    doc = flat("docs", "branch-and-release.md")
    assert "gather_changelog.py" in doc, (
        "the release sequence does not name the script that gathers the entries"
    )
    # The PRESCRIPTIONS, not the word. Saying what `## Unreleased` used to be
    # is what a reader arriving from the old rule needs; telling them to write
    # into it, or to rename it at the release, is the thing that has to be
    # gone. Both spellings below were in this document.
    for old_rule in (
        "put their entry under `## Unreleased`",
        "renames `## Unreleased`",
        "Renaming `## Unreleased`",
    ):
        assert old_rule not in doc, f"the sequence still says: {old_rule}"
    assert "`CHANGELOG.md` holds no section that entries accumulate under" in doc, (
        "the document leaves a reader who knows the old rule to work out on "
        "their own that the heading is gone rather than moved"
    )


def test_this_work_item_wrote_its_own_fragment():
    """Dogfood. A convention the branch introducing it did not follow is one
    nobody has tried.

    Once the work item is released and retired, the fragment is gone and
    the marker `gather_changelog.py` wrote above its body is the proof it
    existed — a hand edit of the released notes leaves no marker behind."""
    item = "1788229400-every-branch-appends-to-the-same-two-files"
    frag = os.path.join(ROOT, "seal", "specs", item, "changelog.md")
    if os.path.isfile(frag):
        with open(frag, encoding="utf-8") as f:
            assert f.read().strip(), "the fragment is empty"
        return
    body = gathered_entry(ROOT, item)
    assert body is not None, "this work item edited the released notes instead"
    assert body.strip(), "the gathered fragment is empty"


def test_a_gathered_body_line_opening_with_an_issue_number_is_kept(tmp_path):
    """#497 round 1, finding 8. The block ends at the next marker or heading,
    and a heading is `#` and then a space; a body line wrapped onto `#120` is
    the entry's own sentence, and cutting it there reads as a shorter entry."""
    (tmp_path / "changelog").mkdir()
    (tmp_path / "changelog" / "1.0.0.md").write_text(
        "## [1.0.0]\n\n<!-- specs/1799000000-an-item -->\n- **A thing changed**, per\n"
        "#120, and the rest of it.\n\n## [0.9.0]\n- an older entry\n",
        encoding="utf-8",
    )
    body = gathered_entry(str(tmp_path), "1799000000-an-item")
    assert "#120, and the rest of it." in body, body
    assert "an older entry" not in body, body


def test_the_documents_say_a_fragment_carries_no_section_line():
    """S11 for #586: the fragment convention's home and the house rule a
    session meets when it writes one both say it, and the module docstring
    lists the exit."""
    for parts in (("docs", "branch-and-release.md"), ("docs", "the-record-layout.md")):
        text = flat(*parts)
        assert "no line starting `## `" in text, "/".join(parts)
    head = flat(".github", "scripts", "gather_changelog.py").split('"""')[1]
    assert "a fragment carries a line starting `## `" in head, head
