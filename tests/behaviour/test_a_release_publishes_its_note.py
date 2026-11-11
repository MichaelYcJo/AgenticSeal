"""#386: the release note publishes itself, or the job goes red saying why.

The cases here read the workflow the push to `main` and a tag pushed by
hand fire, and the release checklist's title command, and wait for #923. `docs/releasing/branch-and-release.md`
names this file on its `check:` line.

#942's phase 6 placed the cases of `.github/scripts/publish_release_note.py`'s
functions in `tests/github/test_publish_release_note.py`, and this file loads the
script through that file's `module`.

The workflow is read as `tests/workflows.py#load` parses it, so a setting
that stands only in a comment is no setting.
"""

import os

from conftest import ROOT, read
from test_publish_release_note import module
from workflows import load

SCRIPTS = os.path.join(ROOT, ".github", "scripts")
SCRIPT = os.path.join(SCRIPTS, "publish_release_note.py")
WORKFLOW = ".github/workflows/publish-release.yml"

# `tests/behaviour/test_release_hygiene.py` refuses a loaded document naming the running
# version or anything above it. These are illustrative, which is the form that
# document's own message points at.
VERSION = "1.2.3"
TAG = "v1.2.3"
SYMPTOMS = "two acts nobody wrote down"


def test_the_line_the_checklist_copies_is_the_line_the_reader_reads():
    """S17 of #1000. The command in `docs/releasing/release-checklist.md` *The
    release pull request*, filled with a version and a symptom, is the merge
    commit's body line, and `title_from` reads it as S15 does. Protects: the
    document a release session copies and the reader moving apart, which
    loses the next release's title."""
    doc = open(
        os.path.join(ROOT, "docs", "releasing", "release-checklist.md"),
        encoding="utf-8",
    )
    text = doc.read()
    doc.close()
    step = text[text.index("## The release pull request") :]
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


def strings(node):
    """Every key and every scalar under a loaded NODE, depth first."""
    if isinstance(node, dict):
        for key, value in node.items():
            yield key
            yield from strings(value)
    elif isinstance(node, list):
        for item in node:
            yield from strings(item)
    else:
        yield node


def test_the_workflow_fires_on_the_tag_and_writes_one_release_one_asset_one_edit():
    """S5 (#718), and S8 of #1117. The workflow fires on the push to `main`
    and on a `v*` tag pushed by hand. `publish` runs the tag step first,
    which creates the tag where the push moved the version and passes it on;
    the note step runs only on a tag passed on and reads `TAG` from it, since
    `github.ref_name` is `main` on the push to `main`. Under
    `contents: write` it writes five things now -- one tag and one release
    (`publish`), one asset on it and one edit of its note (`seal`), one
    commit on `dist` (`dist`, the next case) -- and still declares no other
    scope. `publish` has no `needs` and says which
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
    #1117's against the workflow that fired on the tag alone."""
    workflow = load(WORKFLOW)
    push = workflow["on"]["push"]
    assert push.get("branches") == ["main"], "the workflow does not fire on `main`"
    assert push.get("tags") == ["v*"], "a tag pushed by hand no longer publishes"
    said = list(strings(workflow))
    assert not any("github.ref_name" in s for s in said), (
        "a step reads the ref's name, which is `main` on the push to `main`"
    )
    assert workflow.get("permissions") == {"contents": "write"}, (
        "the workflow declares a scope other than `contents: write`, which it "
        f"does not use: {workflow.get('permissions')}"
    )
    jobs = workflow["jobs"]
    assert not [name for name, job in jobs.items() if "permissions" in job], jobs
    publish = jobs["publish"]
    assert "needs" not in publish, publish
    outputs = publish.get("outputs", {})
    assert outputs.get("created") == "${{ steps.note.outputs.created }}", publish
    assert outputs.get("tag") == "${{ steps.tag.outputs.tag }}", publish
    made = publish["steps"]
    tagging = [i for i, step in enumerate(made) if step.get("id") == "tag"]
    noting = [i for i, step in enumerate(made) if step.get("id") == "note"]
    assert len(tagging) == 1 and len(noting) == 1, made
    assert tagging[0] < noting[0], "the note step runs before the tag exists"
    assert "tag_release.py" in made[tagging[0]].get("run", "")
    note = made[noting[0]]
    assert "publish_release_note.py" in note.get("run", ""), note
    assert note.get("if") == "steps.tag.outputs.tag != ''", note
    assert note.get("env", {}).get("TAG") == "${{ steps.tag.outputs.tag }}", note
    seal = jobs["seal"]
    assert seal.get("needs") == "publish", seal
    assert seal.get("if") == "needs.publish.outputs.created == 'true'", seal
    assert seal.get("timeout-minutes") == "60", seal
    assert seal.get("continue-on-error") == "true", seal
    held = seal["steps"]
    assert len(held) == 5, held
    assert any(
        step.get("with", {}).get("ref") == "${{ needs.publish.outputs.tag }}"
        for step in held
    ), held
    assert not any("apt-get" in s for s in strings(held)), held
    assert held[0].get("with", {}).get("persist-credentials") == "false", held[0]
    for step in held:
        assert step.get("continue-on-error") == "true", step
    tokened = [step for step in held if "GH_TOKEN" in step.get("env", {})]
    assert len(tokened) == 1 and "release_seal.py" in tokened[0].get("run", "")
    assert any(
        step.get("env", {}).get("TAG") == "${{ needs.publish.outputs.tag }}"
        for step in held
    ), held
    suite = [step for step in held if step.get("id") == "suite"]
    assert len(suite) == 1, suite
    assert suite[0].get("timeout-minutes") == "30", suite
    assert tokened[0]["env"].get("SUITE_OUTCOME") == "${{ steps.suite.outcome }}", (
        tokened
    )
    # #869 (S12 of 1791384158): the suite runs with the broad gate's recorder
    # loaded as the gate loads it, writes no JUnit file, and the drawing
    # step is handed the directory and the key the suite step wrote with.
    env = {**suite[0].get("env", {}), **tokened[0]["env"]}
    assert env.get("PYTHONPATH") == (
        "${{ github.workspace }}/skills/verify/scripts/pytest_record"
    ), env
    assert env.get("PYTEST_ADDOPTS") == "-p agentic_pytest_record", env
    assert env.get("SUITE_RECORDS") == env.get("AGENTIC_RECORD_DIR"), env
    assert env.get("SUITE_KEY") == env.get("AGENTIC_RECORD_KEY"), env
    assert not any("junitxml" in s or "SUITE_XML" in s for s in said)


def test_the_dist_job_adds_the_release_to_dist_and_goes_red_where_it_cannot():
    """#1374. The `dist` job needs `publish` and runs wherever `publish`
    passed on a tag, so a re-run of a release whose note already exists
    still fills `dist`. Its `if:` holds `!cancelled()`, which lifts the
    default `success()`, so a note step that fails after the tag step
    passed one on does not skip it (round 1's finding 2, seen red against
    the condition on the tag alone). Its checkout has the whole history and
    every tag, and keeps the credentials its push uses. Its second step runs
    `dist_branch.py` with the tag, as the GitHub Actions bot, author and
    committer alike. No `continue-on-error` stands
    anywhere in it, so a release that did not reach `dist` is a red run.
    Seen red against the workflow with no `dist` job."""
    dist = load(WORKFLOW)["jobs"]["dist"]
    assert dist.get("needs") == "publish", dist
    assert dist.get("if") == "${{ !cancelled() && needs.publish.outputs.tag != '' }}", (
        dist
    )
    assert not any("continue-on-error" in s for s in strings(dist)), dist
    held = dist["steps"]
    assert len(held) == 2, held
    checkout, run = held
    assert checkout.get("uses") == "actions/checkout@v4", checkout
    assert checkout.get("with", {}).get("fetch-depth") == "0", checkout
    assert "persist-credentials" not in checkout.get("with", {}), checkout
    assert run.get("run") == "python3 .github/scripts/dist_branch.py", run
    said = run.get("env", {})
    assert said.get("TAG") == "${{ needs.publish.outputs.tag }}", said
    bot = "github-actions[bot]"
    assert said.get("GIT_AUTHOR_NAME") == said.get("GIT_COMMITTER_NAME") == bot, said
    assert said.get("GIT_AUTHOR_EMAIL") == said.get("GIT_COMMITTER_EMAIL"), said
    assert "+github-actions[bot]@" in said.get("GIT_AUTHOR_EMAIL", ""), said


def test_the_workflow_is_not_a_step_of_the_release_job():
    """`tests/behaviour/test_the_gate_names_every_step_ci_runs.py` partitions every step
    of `hygiene.yml`'s `release` job against `broad_gate.py`'s arms. This is a
    workflow of its own, on a different trigger, and adding a step there
    instead would have grown that partition for a job nothing local can run."""
    hygiene = read(os.path.join(ROOT, ".github", "workflows", "hygiene.yml"))
    assert "publish_release_note.py" not in hygiene
