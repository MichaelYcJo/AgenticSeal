#!/usr/bin/env python3
"""Tag the release a push to `main` shipped, and pass the tag on.

A release ended with a tag the owner pushed by hand, after the release pull
request merged (#1117). Nothing else could push it: a tag pushed with the
workflow's own token starts no other workflow, so a tag a workflow pushed
would never have fired the note. So the publish workflow runs on the push to
`main` itself, and this step decides there whether that push shipped a
release, creates the tag where it did, and hands the tag to the note step of
the same job, which publishes for it.

**A push ships a release where it moved `.claude-plugin/plugin.json`'s
version.** The version moves once per release, in the release's first pull
request into `release/vX.Y.Z`, so on `main` it moves only at the release's
merge. The version is read at the push's `before` and its `after` commit;
where they differ and no `v<after>` tag exists, `v<after>` is created on the
pushed commit through the GitHub API, a lightweight tag like every tag this
repository holds, and then in the job's checkout so the note step finds it
without a fetch.

**A re-run passes the tag on.** Where `v<after>` already names the pushed
commit, the tag was created by an earlier run whose note step failed: it is
passed on and not created again, and the note step's own rule, never
republish, leaves a release that exists as it is. Where the tag names any
other commit, nothing is created and nothing published, and the log names
the commit the tag names.

**A tag pushed by hand is passed on as it is**, so pushing one still
publishes a release the push to `main` did not.

Every other push to `main` passes on no tag, and the note step and the seal
job are skipped.

`DRY_RUN=1` prints the tag it would create and the commit, creates none, and
passes on no tag, for the reason `close_issues_on_release.py`'s docstring
gives.

Environment: `REF` (`github.ref`), `BEFORE` (`github.event.before`), `AFTER`
(`github.sha`), `REPO`, `GH_TOKEN`, `DRY_RUN`, and `GITHUB_OUTPUT` where the
workflow runner sets it. Output: `tag=<tag>`, or `tag=` for no tag.

Exit codes: 0 for every decision, a dry run included -- 1 where GitHub
refused the tag's creation, naming its error, so a release on `main` that is
left untagged is a red run rather than a silent one.
"""

import collections
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "hooks", "lib"))
import console  # noqa: E402
from publish_release_note import write_output  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
MANIFEST = ".claude-plugin/plugin.json"
TAG_PREFIX = "refs/tags/"

# What `decide` answers: the tag to pass on ("" for none), whether to create
# it, and the line the job log prints.
Decision = collections.namedtuple("Decision", "tag create said")


def decide(ref, after, before_version, after_version, tag_commit, missing=""):
    """What to do for a push of `ref` whose pushed commit is `after`.

    `before_version` and `after_version` are `plugin.json`'s version at the
    push's two commits, None where it cannot be read, with `missing` saying
    why the first is None. `tag_commit` is the commit `v<after_version>`
    names, None where no such tag exists.
    """
    if ref.startswith(TAG_PREFIX):
        tag = ref[len(TAG_PREFIX) :]
        return Decision(tag, False, f"{tag} was pushed, so it is passed on as it is")
    if before_version is None:
        return Decision(
            "",
            False,
            f"no tag: {missing}, so whether this push moved the version cannot be read",
        )
    if after_version is None:
        return Decision("", False, f"no tag: {MANIFEST} at {after} names no version")
    if before_version == after_version:
        return Decision(
            "",
            False,
            f"no tag: this push did not move the version, which reads "
            f"{after_version} before and after it",
        )
    tag = f"v{after_version}"
    moved = f"the version moved from {before_version} to {after_version}"
    if tag_commit is None:
        return Decision(tag, True, f"{moved} and no tag {tag} exists")
    if tag_commit == after:
        return Decision(
            tag,
            False,
            f"{moved} and {tag} already names the pushed commit {after}, which "
            "is a re-run, so it is passed on and not created again",
        )
    return Decision(
        "",
        False,
        f"no tag: {moved}, but {tag} already names {tag_commit} and not the "
        f"pushed commit {after}, so nothing is created and nothing published",
    )


def git(*args):
    """`git` run in the repository at `ROOT`."""
    return subprocess.run(
        ["git", "-C", ROOT, *args], capture_output=True, encoding="utf-8"
    )


def version_at(commit):
    """`plugin.json`'s version at `commit`, or None where it cannot be read."""
    shown = git("show", f"{commit}:{MANIFEST}")
    if shown.returncode:
        return None
    try:
        version = json.loads(shown.stdout).get("version")
    except (ValueError, AttributeError):
        return None
    return version if isinstance(version, str) and version else None


def version_before(before):
    """`(the version at the push's earlier commit, why it is None)`."""
    if not before.strip("0"):
        return None, f"the push names no earlier commit (BEFORE is {before!r})"
    if git("cat-file", "-e", f"{before}^{{commit}}").returncode:
        return None, f"the checkout does not hold {before}, the push's earlier commit"
    version = version_at(before)
    if version is None:
        return None, f"{MANIFEST} at {before} names no version"
    return version, ""


def tag_commit_of(tag):
    """The commit `tag` names in the checkout, or None where there is none."""
    found = git("rev-parse", "-q", "--verify", f"refs/tags/{tag}^{{commit}}")
    if found.returncode:
        return None
    return found.stdout.strip() or None


def create(repo, tag, commit):
    """`tag` on `commit`, through the API and then in the checkout; the
    error that stopped it, or ""."""
    gh = shutil.which("gh")
    if gh is None:
        return "gh is not on PATH"
    made = subprocess.run(
        [
            gh,
            "api",
            "-X",
            "POST",
            f"repos/{repo}/git/refs",
            "-f",
            f"ref=refs/tags/{tag}",
            "-f",
            f"sha={commit}",
        ],
        capture_output=True,
        encoding="utf-8",
    )
    if made.returncode:
        return f"gh api refused it: {made.stderr.strip()}"
    local = git("tag", tag, commit)
    if local.returncode:
        return f"git tag failed in the checkout: {local.stderr.strip()}"
    return ""


def main():
    console.to_utf8()
    ref = os.environ.get("REF", "").strip()
    after = os.environ.get("AFTER", "").strip()
    repo = os.environ.get("REPO", "").strip()
    dry = os.environ.get("DRY_RUN", "").strip() not in ("", "0", "false", "no")
    if dry:
        print("DRY_RUN — nothing will be written")

    if ref.startswith(TAG_PREFIX):
        decided = decide(ref, after, None, None, None)
    else:
        before_version, missing = version_before(os.environ.get("BEFORE", "").strip())
        after_version = version_at(after)
        tag_commit = tag_commit_of(f"v{after_version}") if after_version else None
        decided = decide(ref, after, before_version, after_version, tag_commit, missing)
    print(decided.said)

    if decided.create:
        if dry:
            print(f"would create {decided.tag} on {after}")
            write_output("tag", "")
            return 0
        problem = create(repo, decided.tag, after)
        if problem:
            print(f"{decided.tag} was not created on {after}: {problem}")
            write_output("tag", "")
            return 1
        print(f"created {decided.tag} on {after}")
    write_output("tag", "" if dry else decided.tag)
    return 0


if __name__ == "__main__":
    sys.exit(main())
