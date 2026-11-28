#!/usr/bin/env python3
"""A release ships at the number its own commit subjects read, and every issue
labelled `merged: next` is one it carries.

Both questions are asked here by the machine, at the release pull request,
which is the last moment anybody is looking. Both read the same subjects:
`git log --format=%s` from the merge base of the base and the head to the
head, read once.

**The number (#1671).** `plugin.json` is read at the base and at the head. A
subject that opens with `feat:` makes the release the next minor of the
base's version, `A.(B+1).0`, and the absence of one makes it the next
patch, `A.B.(C+1)`. Each pull request's prefix was its writer's judgment
(`skills/commit-pr-convention/SKILL.md` *Commit messages*), and this reads
the prefixes exactly, so no person approves the number.

    head moved to the number read      passes
    head moved to another version      FAILS, naming the number and each
                                       `feat:` subject
    head moves the major, to a version passes, printed as not read against
    whose minor and patch are 0        the subjects: a major is the
                                       owner's word
    head where the base has it         refuses nothing here and prints the
                                       number; the version step of
                                       `.github/workflows/hygiene.yml`
                                       judges a release that leaves it

The reading counts that one spelling. A subject whose first word is `feat`
spelt otherwise, such as `Feat:` or `feat(agents):`, is printed as not read
and changes neither the number nor the exit code; whether it meant the
prefix is its writer's judgment. **A reverted squash stays in the range**,
read over the commits rather than over the tree at the tip, so a reverted
`feat:` still makes a minor.

**The labels (#359).** Two sets of issue numbers, and naming them is what
keeps a failure pointing at the right party.

    D   issues the release actually carries: its commit subjects -> `(#N)`
        -> those pull request bodies -> closing keywords. A reverted squash
        stays in D, for the reason above: the revert's own subject carries
        the revert pull request's `(#N)` and its body carries no closing
        keyword, so nothing subtracts the original claim.
    L   issues carrying the label `merged: next`, in every state

**D is the source of truth and L is a cache of it.** The signal
(`label_merged_on_release_branch.py`) writes L from D one push at a time;
this recomputes D in full from the release's own range.

    L \\ D   FAILS. A `merged: next` on an issue this release does not carry
            is a hand-edit, a squash subject that lost its `(#N)`, or a
            label the last release's close did not take off, and one
            command repairs each
    D \\ L   reports, passes. The signal missed one, and a release must not
            be held for a failure of the signal rather than of its contents

It writes nothing anywhere. Exit 0 or 1.

Environment: every entry the step in `.github/workflows/hygiene.yml` passes,
and the boundary is what the step must pass rather than what `os.environ`
reads -- `GH_TOKEN` reaches this through `gh` and is an input all the same.
What each entry's absence does:

    `REPO`      exit 1   `KeyError: 'REPO'` -- loud
    `HEAD_SHA`  exit 0   the commit the range is measured TO, and the
                         head's `plugin.json` is read at, falls back to `HEAD`,
                         which in CI is the merge ref; nothing printed says
                         so, and `merge_base` below carries what that costs
                         on a `pull_request` event
    `BASE`      exit 0   the default `origin/main`, the ref the range is
                         measured FROM and the base version is read at,
                         which is what a release pull request wants
    `GH_TOKEN`  exit 1   `gh issue list ... failed` -- loud

One absence is silent, and it is not caught here: the case
`tests/text/test_a_release_cannot_ship_an_untrue_milestone.py#test_every_input_the_script_reads_is_handed_to_it_by_the_step`
holds the step to every entry of the table.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# `lib/` first on `sys.path`, where `lib/sibling.py` is imported from; it
# loads every other module this script reads.
sys.path.insert(0, os.path.join(HERE, "..", "..", "lib"))
import sibling  # noqa: E402

# The signal holds the names, the integration branch and `merged: next`, and
# reaches the closer's `run` through its own `closer`.
# Loading it runs nothing: it defines constants and functions at module
# level and guards its `main`.
signal = sibling.load(".github/scripts/label_merged_on_release_branch.py")
closer = signal.closer
console = sibling.load("lib/console.py")

# Where the version a release ships at stands, read at a commit as the
# version step of `.github/workflows/hygiene.yml` reads it.
PLUGIN_JSON = ".claude-plugin/plugin.json"


# --- reads ----------------------------------------------------------------


def merge_base(base, head="HEAD"):
    """Where this branch left `base`.

    `origin/main..HEAD` is the obvious spelling and it is wrong the moment
    `main` moves during a release's life. What the release carries is what
    it accumulated since it left `main`, and that is measured from the fork
    point.

    **`head` is not `HEAD` in CI.** On a `pull_request` event
    `actions/checkout` checks out the merge ref GitHub builds — the head
    merged into the base — so `HEAD` in the job already contains
    `origin/main`, `git merge-base origin/main HEAD` returns the base tip
    rather than the fork point, and the range collapses to exactly the
    `base..HEAD` spelling the paragraph above rejects. That arrives through
    the checkout rather than through the code, so a case over the code alone
    passes with it. The caller passes the head commit the pull request
    names, so the fork point survives the merge ref; a session running this
    by hand has no such commit and gets `HEAD`, which is its own branch tip.
    """
    return closer.run("git", "merge-base", base, head).strip()


def subjects_since(point, head="HEAD"):
    out = closer.run("git", "log", "--format=%s", f"{point}..{head}")
    # exempt from splitlines: git output
    return out.splitlines()


def version_at(ref):
    """The version `plugin.json` holds at REF."""
    return json.loads(closer.run("git", "show", f"{ref}:{PLUGIN_JSON}"))["version"]


def issue_numbers(out):
    return {int(entry["number"]) for entry in json.loads(out)}


def labelled(repo, name):
    """L, in every state. An issue closed by hand mid-release still carries
    the label the signal put on it, and dropping it here would report it as
    `D \\ L` — the signal blamed for a person's edit."""
    return issue_numbers(
        closer.run(
            "gh",
            "issue",
            "list",
            "--repo",
            repo,
            "--label",
            name,
            "--state",
            "all",
            "--limit",
            "1000",
            "--json",
            "number",
        )
    )


# --- the report ------------------------------------------------------------


def listed(numbers):
    return ", ".join(f"#{n}" for n in sorted(numbers)) or "none"


def judge(carried, labels):
    """(lines, failed). Pure, so every direction is a case rather than a run.

    Order is the reader's: what stops the release first, then what is only
    being reported, then the two sets the reader needs to check any of it.
    """
    lines, failed = [], False
    label = signal.MERGED_LABEL

    stray = labels - carried
    if stray:
        failed = True
        lines.append(
            f"::error::L \\ D — {len(stray)} issue(s) carry {label!r} and are "
            f"not in this release: {listed(stray)}. A {label!r} on an issue "
            f"this release does not carry is a hand-edit, a squash subject "
            f"that lost its `(#N)`, or a label the last release's close did "
            f"not take off; `gh issue edit <n> --remove-label {label!r}` "
            f"repairs it"
        )

    unlabelled = carried - labels
    if unlabelled:
        lines.append(
            f"D \\ L — the signal missed {len(unlabelled)}: "
            f"{listed(unlabelled)}. Reported, not failed: a release is not "
            f"held for a failure of the signal rather than of its contents"
        )

    lines.append(f"D (carried by this release): {listed(carried)}")
    lines.append(f"L (carrying {label!r}): {listed(labels)}")
    return lines, failed


# The one spelling the number reading counts. A subject that spells the word
# otherwise is named as not read, and no list of its other spellings is kept
# (`skills/core/SKILL.md` *The rule a mechanism is kept against*).
FEAT = "feat:"


def first_word_is_feat(subject):
    """Whether SUBJECT's first word, case folded and cut at its first `(`,
    `!` or `:`, is `feat`."""
    words = subject.split()
    if not words:
        return False
    word = words[0]
    for mark in "(!:":
        word = word.split(mark, 1)[0]
    return word.casefold() == "feat"


def parts(version):
    """`(major, minor, patch)` of an `X.Y.Z` version, as integers."""
    major, minor, patch = (int(n) for n in version.split("."))
    return major, minor, patch


def number_read(version, subjects):
    """The number the release's SUBJECTS read from VERSION, the version the
    base holds: its next minor where a subject opens with `feat:`, and its
    next patch otherwise."""
    major, minor, patch = parts(version)
    if any(s.startswith(FEAT) for s in subjects):
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def judge_number(base, head, subjects):
    """(lines, failed). The version the head moves `plugin.json` to, against
    the number the release's own subjects read from the BASE version.

    Pure, like `judge`, and in the same order: what stops the release, then
    the number and what it was read from, then what is only reported.
    """
    counted = [s for s in subjects if s.startswith(FEAT)]
    near = [s for s in subjects if not s.startswith(FEAT) and first_word_is_feat(s)]
    number = number_read(base, subjects)
    kind = "minor" if counted else "patch"
    moved_to = parts(head)
    # The owner's word: the major moves up, to its first release.
    major = moved_to[0] > parts(base)[0] and moved_to[1:] == (0, 0)
    lines, failed = [], False

    if head not in (base, number) and not major:
        failed = True
        named = "; ".join(f"`{s}`" for s in counted) or "none"
        lines.append(
            f"::error::the head moves plugin.json to {head}, and the subjects "
            f"read {number}: {base} with {len(counted)} feat: subject(s) "
            f"makes the next {kind}. The feat: subjects: {named}. A feat: "
            f"makes a minor, and every other prefix a patch. The repair is to "
            f"move plugin.json to {number} in a pull request into "
            f"{signal.INTEGRATION_BRANCH}; a major, whose minor and patch are "
            f"0, is the owner's word alone. The prefix states what the change "
            f"is and is never lowered to fit the number"
        )

    lines.append(
        f"number read: {number}, the next {kind} of {base}, from "
        f"{len(counted)} feat: subject(s)"
    )
    lines.append(f"plugin.json: {base} at the base, {head} at the head")
    lines.extend(f"feat: subject: {s}" for s in counted)
    if head == base:
        lines.append(
            f"plugin.json is not moved from {base}, and the version step "
            f"judges a release that leaves it"
        )
    elif major:
        lines.append(
            f"{head} moves the major, the owner's word, and is not read "
            f"against the subjects"
        )
    lines.extend(f"not read: {s}" for s in near)
    return lines, failed


def main():
    repo = os.environ["REPO"]
    base = os.environ.get("BASE", "origin/main")
    # The commit the range is measured to, and the head version is read at.
    # `HEAD` is the merge ref in CI and already contains the base, which
    # collapses the fork point — `merge_base` carries the whole reading. The
    # pull request names its own head and the step passes it; by hand there
    # is none and `HEAD` is the branch tip.
    point = os.environ.get("HEAD_SHA") or "HEAD"

    # Read once and handed to both readings.
    subjects = subjects_since(merge_base(base, point), point)
    number_lines, number_failed = judge_number(
        version_at(base), version_at(point), subjects
    )
    for line in number_lines:
        print(line)

    carried = set(signal.issues_in(repo, subjects))
    lines, failed = judge(carried, labelled(repo, signal.MERGED_LABEL))
    for line in lines:
        print(line)
    return 1 if failed or number_failed else 0


if __name__ == "__main__":
    console.to_utf8()
    sys.exit(main())
