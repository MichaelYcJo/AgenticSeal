"""A `<commit>:<path>` citation names a commit that outlives the squash.

A feature branch squashes into its release branch, and the squash discards
every commit the branch wrote (`docs/releasing/branch-and-release.md` *Work accumulates
on a release branch*). A citation of one of those commits opens in no clone
after the merge, and a reader sent to it finds no source. Before #1270 no
check read the form, and three work items reached a release with such a
citation in their frame, each through a sealed chain.

`cited(root)` reads each token `tests/censuses.py#COMMIT_PATH` matches, in
every tracked file that is on disk and decodes as UTF-8, read as
`tests/behaviour/test_a_cited_section_stands_in_its_file.py#corpus` reads its
files. Three kinds of file are left out: anything under `evals/behaviour/`, a
work item's `trail/` and its `guarantee.md`. Those record what a party ran at
the branch's own commits, which the squash orphans as it orphans a round's
`target:` line, and they leave with the work item. A bare commit is not read.

`unreached(root)` refuses a commit that no ref matching `REACHING` contains,
and a commit the object store lacks, since a fresh clone lacks every commit
a squash discarded. A feature branch's ref never counts, because a squashed
feature branch can be deleted. Where no such ref stands in the checkout,
nothing is judged.

Every token in the cases below is built when the case runs, from a commit
the case makes, so this file holds no `<commit>:<path>` of its own.
"""

import os
import subprocess

import pytest
from censuses import COMMIT_PATH
from conftest import ROOT, on_disk
from test_a_cited_section_stands_in_its_file import text_of

# The refs whose commits outlive a squash: `main` and the release branches,
# the patterns `docs/releasing/branch-and-release.md` names, local or remote-tracking.
REACHING = (
    "refs/remotes/*/main",
    "refs/remotes/*/release/*",
    "refs/heads/main",
    "refs/heads/release/*",
)
NO_REF = (
    "no ref matching " + ", ".join(REACHING) + " stands in this checkout, so no "
    "`<commit>:<path>` citation was judged"
)
REPAIR = (
    "Cite the squash commit on a release branch or on `main` that holds the "
    "same file, or the path at HEAD where the file is this branch's own."
)
FETCH = (
    "Where this checkout's `main` or release refs are older than the cited "
    "squash, `git fetch` answers the refusal."
)


def git(root, *args):
    """The stripped output of `git <args>` run in ROOT; a failure raises."""
    return subprocess.run(
        ["git", "-C", str(root), *args],
        capture_output=True,
        encoding="utf-8",
        check=True,
    ).stdout.strip()


def read_here(rel):
    """Whether the check reads the tracked file REL: not under
    `evals/behaviour/`, a work item's `trail/` or its `guarantee.md`."""
    if rel.startswith("evals/behaviour/"):
        return False
    parts = rel.split("/")
    if len(parts) > 3 and parts[:2] == ["seal", "threads"]:
        return parts[3:] != ["guarantee.md"] and not (
            parts[3] == "trail" and len(parts) > 4
        )
    return True


def cited(root):
    """`[(rel, line, commit)]` for each `COMMIT_PATH` token in the files
    `read_here` admits that are on disk and decode as UTF-8."""
    listed = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z"], capture_output=True, check=True
    ).stdout.decode("utf-8")
    # A positive sweep: a file the working tree deleted cites nothing.
    present, _missing = on_disk(
        root, [rel for rel in listed.split("\0") if rel and read_here(rel)]
    )
    found = []
    for rel in present:
        text = text_of(os.path.join(root, rel))
        if text is None:
            continue
        for m in COMMIT_PATH.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            found.append((rel, line, m.group().split(":", 1)[0]))
    return found


def reaching(root):
    """The refs in ROOT matching `REACHING`, from one `git for-each-ref`."""
    return git(root, "for-each-ref", "--format=%(refname)", *REACHING).split()


def unreached(root):
    """None where `reaching(root)` is empty, so nothing is judged; else each
    `cited(root)` entry whose commit no reaching ref contains. A commit the
    object store lacks makes `git for-each-ref --contains` exit non-zero,
    and it is refused the same way."""
    refs = reaching(root)
    if not refs:
        return None
    found = cited(root)
    dead = set()
    for commit in sorted({c for _, _, c in found}):
        run = subprocess.run(
            ["git", "-C", str(root), "for-each-ref", "--count=1",
             "--format=%(refname)", "--contains", commit, *refs],
            capture_output=True,
            encoding="utf-8",
        )  # fmt: skip
        if not (run.returncode == 0 and run.stdout.strip()):
            dead.add(commit)
    return [entry for entry in found if entry[2] in dead]


def refusal(found):
    """The assertion message naming each of FOUND, `[(rel, line, commit)]`,
    with the repair."""
    return "\n".join(
        [
            "a `<commit>:<path>` citation names a commit that no `main` or "
            "release ref contains, so it opens in no clone once its branch "
            "is squashed:",
            *(f"  {rel}:{line} cites {commit}" for rel, line, commit in found),
            REPAIR,
            FETCH,
        ]
    )


# --- the tree ---------------------------------------------------------------


def assert_outlives(root):
    """Skip with `NO_REF` where ROOT holds no reaching ref, and fail with
    `refusal` on any unreached citation; the tree case's whole verdict, so
    the planted cases run it."""
    found = unreached(root)
    if found is None:
        pytest.skip(NO_REF)
    assert not found, refusal(found)


def verdict(root):
    """`assert_outlives(root)`'s outcome as `(outcome, text)`: `("skipped",
    reason)` where no reaching ref stands, `("passed", "")` where refs stand
    and nothing is refused, and `("failed", message)` where a citation is
    refused. A case reads the outcome it expects, so a verdict that skips,
    passes or fails in the wrong state turns it red and never skips it."""
    try:
        assert_outlives(root)
    except pytest.skip.Exception as skipped:
        return "skipped", str(skipped)
    except AssertionError as failed:
        return "failed", str(failed)
    return "passed", ""


def test_every_cited_commit_outlives_the_squash():
    """S1: every `<commit>:<path>` this tree reads names a commit `main` or a
    release branch contains. A checkout with no such ref is not judged
    (S6)."""
    assert_outlives(ROOT)


# --- planted repositories -----------------------------------------------------

BASES = ("refs/heads/main", "refs/heads/release/v9.9.9")


def planted(tmp_path, bases=BASES, reach=()):
    """A repository on the branch `work`, whose first commit each ref in
    BASES points at and whose second, a child of it, each ref in REACH
    points at; returns `(root, second commit)`."""
    root = tmp_path / "repo"
    root.mkdir()
    git(root, "init", "-q")
    git(root, "config", "user.email", "t@t")
    git(root, "config", "user.name", "t")
    git(root, "symbolic-ref", "HEAD", "refs/heads/work")
    commits = []
    for name in ("base", "work"):
        (root / f"{name}.txt").write_text(f"{name}\n", encoding="utf-8")
        git(root, "add", f"{name}.txt")
        git(root, "commit", "-qm", name)
        commits.append(git(root, "rev-parse", "HEAD"))
    for ref in bases:
        git(root, "update-ref", ref, commits[0])
    for ref in reach:
        git(root, "update-ref", ref, commits[1])
    return str(root), commits[1]


def cite(root, files):
    """Write FILES, `{rel: text}`, under ROOT and stage them, so `git
    ls-files` lists them."""
    for rel, text in files.items():
        path = os.path.join(root, *rel.split("/"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)
    git(root, "add", *files)


def citing(commit):
    """A text whose second line cites COMMIT's first eight characters with a
    path."""
    return f"Intro.\nThe measure at {commit[:8]}:docs/measure.md holds it.\n"


@pytest.mark.parametrize("rel", ["docs/a.md", "hooks/a.py"])
def test_a_citation_of_a_feature_branchs_commit_is_refused(tmp_path, rel):
    """S2: a commit only the feature branch and a remote feature ref contain
    is named with its file and line, in a `.md` and a `.py` alike."""
    root, commit = planted(tmp_path, reach=("refs/remotes/origin/feature/x",))
    cite(root, {rel: citing(commit)})
    assert unreached(root) == [(rel, 2, commit[:8])]


@pytest.mark.parametrize(
    "ref",
    [
        "refs/heads/main",
        "refs/heads/release/v9.9.9",
        "refs/remotes/origin/main",
        "refs/remotes/origin/release/v9.9.9",
    ],
)
def test_a_citation_of_the_squash_is_accepted(tmp_path, ref):
    """S3: a commit that one ref of each pattern in `REACHING` contains, the
    other bases standing at its parent, is named nowhere, and the tree
    case's verdict passes rather than skipping. CI's checkout holds only the
    remote-tracking refs, and an open release branch's squash is reached
    there through `refs/remotes/*/release/*` alone."""
    root, commit = planted(tmp_path, reach=(ref,))
    cite(root, {"docs/a.md": citing(commit)})
    assert cited(root) == [("docs/a.md", 2, commit[:8])]
    assert unreached(root) == []
    assert verdict(root) == ("passed", "")


NOT_READ = (
    "seal/threads/1-x/trail/rounds/round-1.md",
    "seal/threads/1-x/trail/phases/phase-1.md",
    "seal/threads/1-x/guarantee.md",
    "evals/behaviour/crafter/rule-x/x.md",
)
READ = (
    "seal/threads/1-x/frame/plan.md",
    "seal/threads/1-x/changelog.md",
    "seal/threads/1-x/gaps.md",
)


def test_a_record_of_what_a_party_ran_is_not_read(tmp_path):
    """S4: a dead citation in a work item's `trail/`, its `guarantee.md` or
    under `evals/behaviour/` is not read."""
    root, commit = planted(tmp_path)
    cite(root, dict.fromkeys(NOT_READ, citing(commit)))
    assert unreached(root) == []


def test_the_rest_of_a_work_item_is_read(tmp_path):
    """S4: a dead citation in a work item's frame, changelog or closing memo
    is named."""
    root, commit = planted(tmp_path)
    cite(root, dict.fromkeys(READ, citing(commit)))
    assert sorted(unreached(root)) == sorted((rel, 2, commit[:8]) for rel in READ)


def test_a_commit_no_clone_holds_is_refused(tmp_path):
    """S5: a token whose hex names no object is refused as an unreached
    commit is."""
    root, commit = planted(tmp_path, reach=BASES)
    missing = commit[::-1][:12]
    cite(root, {"docs/a.md": citing(missing), "docs/b.md": citing(commit)})
    assert unreached(root) == [("docs/a.md", 2, missing[:8])]


def test_no_reaching_ref_judges_nothing(tmp_path):
    """S6: with no `main` and no release ref, local or remote, a tag and a
    trunk branch notwithstanding, nothing is judged, and the tree case's
    skip names the four patterns."""
    root, commit = planted(
        tmp_path, bases=("refs/tags/v9.9.9", "refs/heads/trunk"), reach=()
    )
    cite(root, {"docs/a.md": citing(commit)})
    assert unreached(root) is None
    outcome, reason = verdict(root)
    assert outcome == "skipped"
    assert all(pattern in reason for pattern in REACHING)


def test_the_refusal_says_where_and_the_repair(tmp_path):
    """S7: the tree case's failure holds each file and line, the commit, the
    repair and the `git fetch` sentence."""
    root, commit = planted(tmp_path)
    cite(root, {"docs/a.md": citing(commit), "hooks/a.py": citing(commit)})
    outcome, message = verdict(root)
    assert outcome == "failed"
    for part in ("docs/a.md:2", "hooks/a.py:2", commit[:8], REPAIR, FETCH):
        assert part in message
