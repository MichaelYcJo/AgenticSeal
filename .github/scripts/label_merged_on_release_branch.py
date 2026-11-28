#!/usr/bin/env python3
"""Label the issues a squash into `release/next` just answered.

Between a work item squashing into `release/next` and the release reaching
`main`, a finished ticket is indistinguishable from one nobody has started:
an issue's state does not move until `main` moves, and `main` moves once per
release. A person reading the tracker mid-release cannot tell the two apart.

So this runs when a release branch moves. Where the branch is `release/next`,
it reads the pull request numbers out of the commit subjects that arrived,
fetches those pull request bodies, and puts `merged: next` on every issue
their closing keywords name. The label carries no number, because a release
takes its number only when it is cut. A push to any other branch under
`release/*`, such as the numbered branch of a release before #1671, labels
nothing and says so.

**Nothing here parses anything new.** `MERGED_PR` and `keywords_in` come
from `lib/closing.py`, whose `HIDDEN` treatment of a quoted keyword is the
behaviour a second reader would have to reproduce, and `pull_request_body`
and `arrived` come from `close_issues_on_release.py`, the closer, which reads
the same three things with them. Importing the closer runs nothing: its
`main` is guarded.

Four things it deliberately does not do.

**It does not close anything.** An issue closed at the squash into
`release/next` is closed for something nobody has received yet.
`close_issues_on_release.py` keeps the close, when `main` moves, and this
adds no second closer.

**It never removes a label and never comments.** The only two writes are
`gh label create` and `gh issue edit --add-label`. `merged: next` comes off
an issue at the close, and that removal is the closer's.

**It writes nothing it has not read first.** The label is created only after
a read says it is absent, and added to an issue only after a read says that
issue does not carry it. That is not tidiness -- it is what makes a re-run of
a push, or a re-push, a no-op *by construction* rather than by assuming what
GitHub does with a duplicate label. Nobody here has tested that assumption,
and this way nobody has to.

**A `(#N)` that names no pull request is skipped, not fatal**, and so is a
number naming no issue at all -- both for the reasons
`close_issues_on_release.py` gives, on the same readers.

`DRY_RUN=1` prints what it would write and writes nothing, for the reason
that script's docstring gives: a tool whose only mode has side effects gets
run for its output sooner or later.

Environment: `BRANCH` (`github.ref_name`), `BEFORE`, `AFTER`, `REPO`.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# `lib/` first on `sys.path`, where `lib/sibling.py` is imported from; it
# loads every other module this script reads.
sys.path.insert(0, os.path.join(HERE, "..", "..", "lib"))
import sibling  # noqa: E402

# Loaded through `lib/sibling.py` rather than by `import
# close_issues_on_release`, so that a test importing THIS module by path gets
# the same neighbour the workflow does. `sys.path[0]` is this directory only
# when the script is the entry point.
closer = sibling.load(".github/scripts/close_issues_on_release.py")
# `lib/closing.py`, the readers of a squash subject and a closing keyword the
# closer reads with.
closing = sibling.load("lib/closing.py")
console = sibling.load("lib/console.py")


# --- the names --------------------------------------------------------------
#
# The integration branch work squashes into, and the label a squash there
# puts on the issues it answered. Each is written once, here:
# `release_completeness_check.py` reads `MERGED_LABEL` as L, and
# `close_issues_on_release.py` takes it off an issue it closes.

INTEGRATION_BRANCH = "release/next"
MERGED_LABEL = "merged: next"

# The most characters GitHub accepts in a label's description. The number is
# GitHub's, not this repository's: `gh label create` with a longer one is
# refused with `HTTP 422 ... description is too long (maximum is 100
# characters)`, and a 119-character description sent there failed the
# close-issues workflow after a release and skipped the step behind it (#515).
# The description this script sends to `gh label create` is held under it
# by a case, so an over-long one is refused by the suite before a merge
# rather than by the tracker after one. Raising it does not make a longer
# description fit; it moves the refusal back to the tracker.
#
# No function here reads it. The case that reads it is in
# `tests/github/test_label_merged_on_release_branch.py`. It stays in this
# script rather than in a test because the cap binds the description this
# script writes: a person editing `LABEL_DESCRIPTION` meets it here, where a
# test would show it only after the edit fails.
LABEL_DESCRIPTION_LIMIT = 100

# What the label says on the tracker, where a person reads it. The name
# carries no number, so the description says which branch it records and
# when it stops being the current answer.
LABEL_DESCRIPTION = (
    f"Squash-merged into {INTEGRATION_BRANCH}; comes off when the release that "
    "ships it closes it"
)


# --- reads ----------------------------------------------------------------


def issue_labels(repo, number):
    """(label names, exists) for an issue, or ([], False) if there is none.

    `close_issues_on_release.py` reads an issue's labels too, to take a
    spent label off the issue it is closing, so the reader lives on
    that module, which owns the 404-tolerant read it is built on, and this
    is the delegation -- one source, the way both scripts take `MERGED_PR`
    and `keywords_in` from `lib/closing.py`, and `pull_request_body` and
    `arrived` from the closer. The name stays here, so a caller of this
    module reads labels through it.
    """
    return closer.issue_labels(repo, number)


def existing_labels(repo):
    """Every label name the repository has.

    The whole list rather than `GET /labels/{name}`, because the name carries
    a space and a colon and the one-label read would turn on how they are
    encoded in a path -- a detail nothing else here depends on.
    """
    out = closer.run(
        "gh", "label", "list", "--repo", repo, "--limit", "1000", "--json", "name"
    )
    return {entry["name"] for entry in json.loads(out)}


# --- writes ---------------------------------------------------------------


def create_label(repo):
    closer.run(
        "gh",
        "label",
        "create",
        MERGED_LABEL,
        "--repo",
        repo,
        "--description",
        LABEL_DESCRIPTION,
        # The green the first one was created with by hand, so a label this
        # writes and a label somebody wrote before it look the same.
        "--color",
        "0E8A16",
    )


def add_label(repo, number):
    closer.run(
        "gh",
        "issue",
        "edit",
        str(number),
        "--repo",
        repo,
        "--add-label",
        MERGED_LABEL,
    )


# --- the run --------------------------------------------------------------


def issues_in(repo, subjects):
    """{issue number: the pull request that claimed it}, in arrival order."""
    wanted = {}
    for subject in subjects:
        found = closing.MERGED_PR.search(subject.strip())
        if not found:
            continue
        number = int(found.group(1))
        body = closer.pull_request_body(repo, number)
        if body is None:
            print(f"#{number} is not a pull request — a hand-written number")
            continue
        for issue in closing.keywords_in(body):
            wanted.setdefault(int(issue), number)
    return wanted


def main():
    branch = os.environ.get("BRANCH", "")
    if branch != INTEGRATION_BRANCH:
        print(f"{branch!r} is not {INTEGRATION_BRANCH} — nothing to label")
        return
    before, after = os.environ.get("BEFORE", ""), os.environ["AFTER"]
    repo = os.environ["REPO"]
    dry = os.environ.get("DRY_RUN", "").strip() not in ("", "0", "false", "no")
    if dry:
        print("DRY_RUN — nothing will be written")

    label = MERGED_LABEL
    wanted = issues_in(repo, closer.arrived(before, after))
    if not wanted:
        print("no closing keyword in any of them — nothing to label")
        return

    if label in existing_labels(repo):
        print(f"label {label!r} exists")
    elif dry:
        print(f"would create label {label!r}")
    else:
        create_label(repo)
        print(f"created label {label!r}")

    for issue, source in sorted(wanted.items()):
        carried, exists = issue_labels(repo, issue)
        if not exists:
            print(f"#{issue} does not exist (named by #{source}) — skipping")
            continue
        if label in carried:
            print(f"#{issue} already carries {label!r} — leaving it")
            continue
        if dry:
            print(f"would label #{issue} {label!r}, named by #{source}")
            continue
        add_label(repo, issue)
        print(f"labelled #{issue} {label!r}, named by #{source}")


if __name__ == "__main__":
    console.to_utf8()
    sys.exit(main())
