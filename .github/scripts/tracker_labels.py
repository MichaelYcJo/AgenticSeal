#!/usr/bin/env python3
"""Create the labels this repository's documents specify but the tracker lacks.

`docs/releasing/issues-and-milestones.md` specifies `size: now` -- two
states, the prefix argument, what its absence means -- and a specified label
the tracker lacks leaves that section describing a mechanism, and its
argument for the prefix over a bare `now` arguing about a label nobody can
apply.

**Creating the label is nobody's act unless a workflow does it.** Assigned
to a **person**, it has no queue this repository can read -- no open issue,
no checklist row, no failing check -- and `size: now` went uncreated across
three releases that way. What it costs is the reading the label exists to
make unnecessary: issue bodies re-read to decide which has to be in effect
next.

The repair is not *remember harder* and not a ticket, which is the same act
one queue over. It is this: a label a document specifies is the same kind of
object as a label a release needs, and
`label_merged_on_release_branch.py` creates one of those from a
workflow, with the `issues: write` the job already holds. So the
declaration below is what a document specifies, and the workflow that runs
when `main` moves reconciles it.

**It never deletes and never re-colours.** The only write is
`gh label create`, and it happens only after a read says the name is absent
-- which makes a re-run a no-op by construction rather than by assuming what
GitHub does with a duplicate. A label deleted by hand comes back at the next
release rather than immediately, and that is the accepted cost of hanging
this off a trigger that already exists rather than inventing one.

**It is not a gate and must not become one.** A hygiene step failing a pull
request for a missing label would be red on
the very branch that adds the label, because no agent in this repository's
chain may write to the tracker. A step that performs the act does not.

  tracker_labels.py --check   report what is missing, exit 0
  tracker_labels.py --apply   create what is missing

`DRY_RUN=1` makes `--apply` print what it would create and write nothing.

Environment: `REPO`, `GH_TOKEN`.
"""

import argparse
import os
import sys

# `lib/` first on `sys.path`, where `lib/sibling.py` is imported from; it
# loads every other module this script reads.
sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "lib"),
)
import sibling

console = sibling.load("lib/console.py")

# Loaded through `lib/sibling.py` for the reason
# `label_merged_on_release_branch.py` gives: a test importing THIS module by
# path gets the same neighbours the workflow does. `existing_labels` reads
# the whole label list rather than asking for one name, because every name
# here carries a space and a colon and the one-label read would turn on how
# those are encoded in a URL path.
signal = sibling.load(".github/scripts/label_merged_on_release_branch.py")
closer = signal.closer


# --- what the documents specify -------------------------------------------
#
# One row per label, and the row carries the document that specifies it.
# That last field is not decoration: this file is a copy of a decision made
# somewhere else, and a reader who cannot get back to the original has to
# take the copy's word for what the label means.
#
# The description is the document's OWN sentence, the way
# `label_merged_on_release_branch.py#label_description` derives one, and it
# says when the label stops being the current answer -- which is the half a
# person reading the tracker cannot otherwise know.
#
# It is also at most `LABEL_DESCRIPTION_LIMIT` characters, GitHub's cap, and
# that is why `size: now`'s is the document's clause rather than its whole
# sentence. Both halves in full come to 119 characters, which the tracker
# refuses with a 422, skipping the step behind it in the workflow.
# Shortening keeps both halves and drops the words that say
# neither: the subject a label is always about, and which release -- `its`
# is the one carrying the ticket.
#
# The colour is `chain: capped`'s. That is this repository's other
# `<subject>: <state>` label and the shape `size: now`'s name was taken from
# -- the specifying section says so in as many words -- so two labels of one
# shape read as one shape on the tracker. The topic labels carry five
# different colours between them, so there is no one family colour to join.
# Nothing turns on it either way.
LABELS = (
    {
        "name": "size: now",
        "color": "d4c5f9",
        "description": (
            "Has to be in effect before the next work item starts; "
            "removed when its release closes the issue"
        ),
        "specified_by": (
            "docs/releasing/issues-and-milestones.md "
            "*A label answers what it is about, and survives the move*"
        ),
    },
)


def declared():
    return LABELS


def missing(repo):
    """The declared labels the tracker does not have, in declared order."""
    present = signal.existing_labels(repo)
    return [label for label in declared() if label["name"] not in present]


def create(repo, label):
    closer.run(
        "gh",
        "label",
        "create",
        label["name"],
        "--repo",
        repo,
        "--description",
        label["description"],
        "--color",
        label["color"],
    )


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Reconcile the tracker's labels with what the documents specify."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--check", action="store_true", help="report what is missing, exit 0"
    )
    group.add_argument("--apply", action="store_true", help="create what is missing")
    args = parser.parse_args(argv)

    repo = os.environ["REPO"]
    dry = os.environ.get("DRY_RUN", "").strip() not in ("", "0", "false", "no")
    if dry:
        print("DRY_RUN — nothing will be written")

    absent = missing(repo)
    if not absent:
        print(f"all {len(declared())} declared labels exist — nothing to create")
        return 0

    for label in absent:
        print(f"{label['name']!r} is missing, specified by {label['specified_by']}")
        if args.check or dry:
            continue
        create(repo, label)
        print(f"created {label['name']!r}: {label['description']}")
    if args.check:
        print(
            "\nThe workflow that runs when `main` moves creates these:\n"
            "  python3 .github/scripts/tracker_labels.py --apply"
        )
    return 0


if __name__ == "__main__":
    # Every entry point carries this, because a script that raises while
    # printing dies with stdout empty and an empty stdout is how a gate says
    # "nothing to see here" (`lib/console.py`). The arm at risk is
    # `--check`, which is the one a person types: under cp949, cp932, cp936
    # or a bare `LC_ALL=C` the em dash `main` prints raises
    # `UnicodeEncodeError` and the process dies. The workflow's runner is
    # UTF-8, so `--apply` is not the exposed one.
    console.to_utf8()
    sys.exit(main())
