"""#386: the release note publishes itself, or the job goes red saying why.

The cases here read the workflow the push to `main` and a tag pushed by
hand fire, and the release checklist's title command, and wait for #923. `docs/branch-and-release.md`
names this file on its `check:` line.

#942's phase 6 placed the cases of `.github/scripts/publish_release_note.py`'s
functions in `tests/github/test_publish_release_note.py`, and this file loads the
script through that file's `module`.
"""

import os

from conftest import ROOT, read
from test_publish_release_note import module

SCRIPTS = os.path.join(ROOT, ".github", "scripts")
SCRIPT = os.path.join(SCRIPTS, "publish_release_note.py")
WORKFLOW = os.path.join(ROOT, ".github", "workflows", "publish-release.yml")

# `tests/behaviour/test_release_hygiene.py` refuses a loaded document naming the running
# version or anything above it. These are illustrative, which is the form that
# document's own message points at.
VERSION = "1.2.3"
TAG = "v1.2.3"
SYMPTOMS = "two acts nobody wrote down"


def test_the_line_the_checklist_copies_is_the_line_the_reader_reads():
    """S17 of #1000. The command in `docs/release-checklist.md` *5*, filled
    with a version and a symptom, is the merge commit's body line, and
    `title_from` reads it as S15 does. Protects: the document a release
    session copies and the reader moving apart, which loses the next
    release's title."""
    doc = open(os.path.join(ROOT, "docs", "release-checklist.md"), encoding="utf-8")
    text = doc.read()
    doc.close()
    step = text[text.index("## 5. The release pull request") :]
    title = step.split('--title "', 1)[1].split('"', 1)[0]
    filled = title.replace("X.Y.Z", VERSION).replace(
        "<the symptoms the release answers>", SYMPTOMS
    )
    assert filled != title and "<" not in filled, title
    mod = module(SCRIPT, "publish_release_note_for_the_checklist")
    message = f"Merge pull request #500 from owner/release/v{VERSION}\n\n{filled}\n"
    title, source = mod.title_from(message, VERSION, TAG)
    assert (title, source) == (
        f"{VERSION} — {SYMPTOMS}",
        "the tagged commit's `release:` line",
    )
    # Trailing whitespace after the symptoms is no part of the title.
    spaced = mod.title_from(message.replace("\n", "  \n"), VERSION, TAG)[0]
    assert spaced == title, spaced


def workflow():
    """The workflow with its comment lines removed.

    A setting that exists only in a comment is not a setting —
    `tests/text/test_ci_gives_the_checks_what_they_need.py` measured that dropping
    a real line and keeping the comment above it left its checks green.
    """
    return "\n".join(
        line
        for line in read(WORKFLOW).splitlines()
        if not line.lstrip().startswith("#")
    )


def job(text, name):
    """One job's lines of the comment-free workflow, from its `  <name>:`
    line to the next job or the end."""
    lines = text.splitlines()
    start = lines.index(f"  {name}:")
    end = next(
        (
            i
            for i in range(start + 1, len(lines))
            if lines[i].startswith("  ") and not lines[i].startswith("   ")
        ),
        len(lines),
    )
    return lines[start:end]


def steps(lines):
    """A job's steps, each as its lines, split at every `      - ` line."""
    out = []
    for line in lines:
        if line.startswith("      - "):
            out.append([line])
        elif out:
            out[-1].append(line)
    return out


def test_the_workflow_fires_on_the_tag_and_writes_one_release_one_asset_one_edit():
    """S5 (#718), and S8 of #1117. The workflow fires on the push to `main`
    and on a `v*` tag pushed by hand. `publish` runs the tag step first,
    which creates the tag where the push moved the version and passes it on;
    the note step runs only on a tag passed on and reads `TAG` from it, since
    `github.ref_name` is `main` on the push to `main`. Under
    `contents: write` it writes four things now -- one tag and one release
    (`publish`), one asset on it and one edit of its note (`seal`) -- and
    still declares no other scope. `publish` has no `needs` and says which
    tag it published for and whether it created the release; `seal` needs
    it, runs only on `created == 'true'`, checks out that tag and reads `TAG`
    from it, and every one of its steps is `continue-on-error`, so nothing
    the seal meets can turn the workflow red. A hung suite ends at the step's `timeout-minutes`, and
    the job's own timeout sits under a job-level `continue-on-error` (round
    1's finding 4). The token is on the drawing step alone, and the checkout
    does not persist it in `.git/config`, so the suite at the tag runs with
    none (round 1's finding 5). Since #1009 (S7) the job has five steps:
    none runs `apt-get`, so the job installs no system package and the image
    needs no renderer from the runner. Seen red against the workflow with no
    `seal` job, the two round-1 halves against the workflow without them,
    #1009's against the job with the SVG renderer's install step, and
    #1117's against the workflow at `4134055a`, which fired on the tag
    alone."""
    text = workflow()
    assert "    branches: [main]" in text, "the workflow does not fire on `main`"
    assert "    tags: ['v*']" in text, "a tag pushed by hand no longer publishes"
    assert "github.ref_name" not in text, (
        "a step reads the ref's name, which is `main` on the push to `main`"
    )
    assert "contents: write" in text
    for scope in ("issues:", "pull-requests:", "packages:"):
        assert scope not in text, (
            f"the workflow declares {scope}, which it does not use"
        )
    publish = job(text, "publish")
    assert not any(line.strip().startswith("needs:") for line in publish), publish
    assert "      created: ${{ steps.note.outputs.created }}" in publish, publish
    assert "      tag: ${{ steps.tag.outputs.tag }}" in publish, publish
    made = steps(publish)
    tagging = [i for i, step in enumerate(made) if "        id: tag" in step]
    noting = [i for i, step in enumerate(made) if "        id: note" in step]
    assert len(tagging) == 1 and len(noting) == 1, made
    assert tagging[0] < noting[0], "the note step runs before the tag exists"
    assert any("tag_release.py" in line for line in made[tagging[0]])
    note = made[noting[0]]
    assert any("publish_release_note.py" in line for line in note), note
    assert "        if: steps.tag.outputs.tag != ''" in note, note
    assert "          TAG: ${{ steps.tag.outputs.tag }}" in note, note
    seal = job(text, "seal")
    assert "    needs: publish" in seal, seal
    assert "    if: needs.publish.outputs.created == 'true'" in seal, seal
    assert "          ref: ${{ needs.publish.outputs.tag }}" in seal, seal
    assert "          TAG: ${{ needs.publish.outputs.tag }}" in seal, seal
    assert (
        "    timeout-minutes: 60" in seal and "    continue-on-error: true" in seal
    ), seal
    held = steps(seal)
    assert len(held) == 5, held
    assert not any("apt-get" in line for step in held for line in step), held
    assert any(line.strip() == "persist-credentials: false" for line in held[0]), held[
        0
    ]
    for step in held:
        assert any(line.strip() == "continue-on-error: true" for line in step), step
    tokened = [step for step in held if any("GH_TOKEN" in line for line in step)]
    assert len(tokened) == 1 and any("release_seal.py" in line for line in tokened[0])
    suite = [step for step in held if any("id: suite" in line for line in step)]
    assert len(suite) == 1, suite
    assert any(line.strip() == "timeout-minutes: 30" for line in suite[0]), suite
    assert any(
        "SUITE_OUTCOME: ${{ steps.suite.outcome }}" in line for line in tokened[0]
    ), tokened
    # #869 (S12 of 1791384158): the suite runs with the broad gate's recorder
    # loaded as the gate loads it, writes no JUnit file, and the drawing
    # step is handed the directory and the key the suite step wrote with.
    said = {
        line.strip().split(":", 1)[0]: line.strip().split(":", 1)[1].strip()
        for line in suite[0] + tokened[0]
        if line.strip().split(":", 1)[0].isupper()
    }
    assert said["PYTHONPATH"] == (
        "${{ github.workspace }}/skills/verify/scripts/pytest_record"
    ), said
    assert said["PYTEST_ADDOPTS"] == "-p agentic_pytest_record", said
    assert said["SUITE_RECORDS"] == said["AGENTIC_RECORD_DIR"], said
    assert said["SUITE_KEY"] == said["AGENTIC_RECORD_KEY"], said
    assert not any(
        "junitxml" in line or "SUITE_XML" in line for line in text.splitlines()
    )


def test_the_workflow_is_not_a_step_of_the_release_job():
    """`tests/behaviour/test_the_gate_names_every_step_ci_runs.py` partitions every step
    of `hygiene.yml`'s `release` job against `broad_gate.py`'s arms. This is a
    workflow of its own, on a different trigger, and adding a step there
    instead would have grown that partition for a job nothing local can run."""
    hygiene = read(os.path.join(ROOT, ".github", "workflows", "hygiene.yml"))
    assert "publish_release_note.py" not in hygiene
