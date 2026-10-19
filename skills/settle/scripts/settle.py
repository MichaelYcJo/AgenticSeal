#!/usr/bin/env python3
"""settle — name the released work items a policy document has yet to absorb.

`seal/README.md` has said a work item's directory "waits until a later
`settle` folds it" since the root existed, and nothing was ever built. The
directory therefore never stops growing: 98 work items, 1,338 files, 15M on
the tree this shipped from, and no check reads any of it after the merge.

**This reads, groups and records. It never writes prose and it never judges.**
`docs/one-root-by-lifetime.md` §*What keeps `settle` light* says the step
"moves and does not verify", and folding *only what is still true* is exactly
a judgment about truth — so each standing statement is written by the
session, following `skills/settle/SKILL.md`, and this command
supplies the corpus it is written from. A script that wrote the prose itself
would either splice 97 sentences up under their provenance comments, which is
a move and not a compaction, or assert that each moved sentence still holds,
which is the one thing the clause above forbids.

  settle                        what would fold
  settle --retire               remove the directories whose fold is recorded,
                                and the released ones with no spec.md and
                                nothing open
  settle --retire-process       remove the process record of every released
                                work item, fold or no fold
  settle --released-at REF      what counts as released (default origin/main)
  settle --root DIR             a repository other than this one

**Released means present on the branch the release merges to**, which is why
`--released-at` names a ref rather than a date. A marker in the changelog
was measured on this repository as the alternative and is wrong: 11 work
items carry none although they plainly shipped.

**The fold record is the provenance comment, and there is no second file.**
A folded sentence carries `<!-- specs/<work-item-id> -->` in the `docs/`
document it landed in — the marker `.github/scripts/gather_changelog.py#marker`
already writes — so the
record is derived from the destination and cannot disagree with it. Reading
it is `skills/verify/scripts/unverified_check.py#folded_items`, loaded here
rather than re-spelled: that module is the fold record's one reader, and the
same arm of `unverified-check` is what would otherwise call a retirement this
branch's deletion.

**Two halves, and the retirement is the second.** The command lists what a
session has to write policy for; `--retire` removes the directories whose
policy was written, which the marker is the proof of. Nothing that states a
rule is removed without one, so the failure this arrangement can produce is a
thin policy document, which a reader can see, rather than a directory deleted
with nothing absorbing it, which nobody can.

**The process arm is its own act, and the fold does not gate it (#729).**
`--retire-process` removes a released work item's `rounds/`, `phases/`
and the files written only for a pull request, and leaves
`routing.md` and the SDD set for the fold. No check reads that part after
the release, and removing it judges nothing, so it does not wait on the fold's
judgment. What the SDD set still cites of it resolves at the release tag. It
is an allow-list: a file on neither list is kept and named. A citation into
a removed file is listed, never refused.

**The rule arm, and why it needs no marker.** A released work item that wrote
no `spec.md` states no rule — a release entry, a renumbering, a CI repair —
so there is nothing for a document to absorb, and #517's owner decision D3
retires it by that rule rather than by a record. One condition narrows it:
nothing in its record may be open, because an open `## Not verified` row is a
claim with an answerer, not a rule. Whether a
directory qualifies is `unverified_check.py#retired_by_rule`, the predicate
every CI reader asks of the merge-base, asked here of the working tree AND of
the merge base of `--released-at` and `HEAD` (#602). A CI reader on a pull
request stands on the merge ref, so its merge base is the base branch's tip:
the same commit as this one until the base moves past the fork, and a later
one after. Past the fork the two can disagree either way. A closure the base
took after the fork is read by CI and not here, so this keeps a directory CI
would pass. A `spec.md` the base added to the directory after the fork is
read by CI and not here, so this retires a directory CI refuses. A row closed on the working
branch and still open at that base is kept, under a heading of its own
naming the base and, where the base has moved, the merge that moves it.

**Local mode is refused rather than reported on.** A root under the common
git directory is never committed, so no ref holds the work item directories,
nothing in them reads as released, and nothing removed from them could be
recovered. `seal mode shared` moves the root into the tree and this command
works from there. A repository that opted out with the scratch marker is
refused too, and told which of the two it is. The marker is an empty FILE
under the common git directory, read the way `hooks/optin.py#home_at` reads
it; a directory of that name is not one, and is refused as no root.

Exit codes: 0 the report was produced, or the retirement ran, or the root
holds no work item at all — an empty or absent `seal/specs/` under a present
`seal/` is the state a complete fold reaches — or the process arm found
nothing left to remove · 1 a retirement was asked for
and something refused it — a spec-less directory's closure has not
reached the merge base of `--released-at` and `HEAD` · 2 the arguments or the
tree were unusable, which is six states: a
`--released-at` ref that does not resolve, a `--released-at` ref sharing no
commit with `HEAD` or a clone too shallow to reach the one they share, a root
at neither place, a root in local mode, a
repository that opted out, and a sibling script it loads that is not beside
it. An interpreter below the floor never reaches this file through
`bin/settle`: `hooks/launch.py` refuses it with 2 first.
"""

import argparse
import collections
import importlib.util
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
READER = os.path.join(HERE, "..", "..", "verify", "scripts", "unverified_check.py")
OPTIN = os.path.join(HERE, "..", "..", "..", "hooks", "optin.py")
RULES = os.path.join(HERE, "rule_changes.py")

# What each sibling is for, in the sentence `load` prints when it is missing.
PURPOSES = {
    READER: "it is where the fold record is read from",
    OPTIN: "it is what finds the repository's seal/ root",
    RULES: "it is what reads a spec's `## Rule changes`",
}

SPECS = "seal/specs"
TESTS = "tests/"

MARKER_LINE_RE = re.compile(r"^<!-- specs/(\S+) -->$", re.M)


def under(root, rel):
    """The disk path of a `/`-joined repository-relative path."""
    return os.path.join(root, *rel.split("/"))


def plural(count):
    """`s` unless there is one of them. Every count this prints is read by a
    person, and `1 work items` is the tell that nobody read the output."""
    return "" if count == 1 else "s"


def load(path, name):
    """Import a sibling script by path, or refuse with a sentence saying what
    the missing file is for — its `PURPOSES` entry — and exit 2.

    Not a bare `exec_module`: `spec_from_file_location` hands back a spec for
    any path ending in `.py`, present or not, so a missing reader reaches the
    loader and raises `FileNotFoundError` — a traceback where this file's
    whole contract is that every failure is a sentence.

    Exit 2 and not 1, because nothing about the tree has been read and 1 here
    means a retirement was refused. It used to be `SystemExit(<sentence>)`,
    which exits 1, and it gave every file the fold record's purpose, which is
    false of `hooks/optin.py` (#590). The purpose is looked up by path rather
    than passed by each caller, so no call site can name the wrong one.
    """
    purpose = PURPOSES.get(path, "this command cannot run without it")
    if not os.path.isfile(path):
        sys.stderr.write(
            f"settle: cannot read {path}, and {purpose}. This command ships "
            "beside it under `skills/`; a copy of one script taken on its own "
            "is not a plugin. Nothing was read.\n"
        )
        raise SystemExit(2)
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        sys.stderr.write(f"settle: cannot load {path}, and {purpose}.\n")
        raise SystemExit(2)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# --- what the tree says ----------------------------------------------------


def work_items(root):
    """Every work item id with a directory under `seal/specs/`, in id order."""
    top = under(root, SPECS)
    if not os.path.isdir(top):
        return []
    return sorted(
        name for name in os.listdir(top) if os.path.isdir(os.path.join(top, name))
    )


def released(root, ref):
    """Work item ids whose directory is present at `ref`, or None if it is not.

    A work item is released when the branch the release merges to holds its
    directory, which is a question only git can answer. None is returned for
    a ref that does not resolve, and the caller refuses: a ref this cannot
    read would otherwise make every work item read as unreleased and the
    whole report as "nothing to fold", which is the quiet zero every checker
    in this plugin is written against.
    """
    r = subprocess.run(
        ["git", "-C", root, "ls-tree", "-r", "--name-only", ref],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    if r.returncode != 0:
        return None
    prefix = SPECS + "/"
    found = set()
    for line in r.stdout.splitlines():
        if line.startswith(prefix):
            rest = line[len(prefix) :]
            if "/" in rest:
                found.add(rest.split("/", 1)[0])
    return found


# What a settled root prints, for the report and the retirement alike.
SETTLED = (
    "settle: {specs}/ in {root} holds no work item — nothing to fold and "
    "nothing to retire. A complete fold ends here, and git keeps no empty "
    "directory, so a fresh checkout of this state has no {specs}/ at all.\n"
)

# The rule arm's headings, and the listings D1's table asks the command to
# print by itself. Pinned by `tests/test_settle_reads_before_it_removes.py`.
RULE_HEADING = (
    "retired by the rule — released, no `spec.md`, nothing open; "
    "`settle --retire`\nremoves these with no marker, because a moment "
    "states no rule to fold:"
)
RULE_KEPT_HEADING = (
    "kept by the rule — no `spec.md`, but the record still holds an open "
    "row, which\nleaves by being closed (`closed` with what closed it) in a pull "
    "request merged before the\none that retires the directory, and merged "
    "to the branch the release merges to,\nnever with it:"
)
# #602: nothing is open in the tree, and the base still holds a row open.
# `{base}` is `unverified_check.py#base_label`'s spelling of the merge base of
# `--released-at` and `HEAD`. It is the revision the CI readers ask at when
# the ref has not moved since the fork; `RULE_MOVED_HEADING` is the other case.
RULE_BASE_HEADING = (
    "kept until the closure reaches {base} — no `spec.md` and nothing open "
    "here, but\nthe record there still holds an open row, and the CI readers "
    "ask the rule there.\nMerge the closure to the branch the release merges "
    "to first; the directory goes\nin a later pull request:"
)
# #602, round 1: `--released-at` has moved past the fork. The CI readers ask
# at its tip (a pull request is checked out as the merge ref), and this asks
# at the fork, so a closure already merged there is not read here until the
# ref is merged into this branch.
RULE_MOVED_HEADING = (
    "kept: the closure has not reached {base} — no `spec.md` and nothing open "
    "here, but\nthe record there still holds an open row. {ref} has moved past "
    "that commit: where\n{ref} already holds the closure, merge {ref} into this "
    "branch and run `settle`\nagain; otherwise merge the closure to {ref} "
    "first. The directory goes in a later\npull request:"
)


# What `report` and `retire` print for a survey that carries no base, one
# sentence for both readers of it.
NO_BASE_SAYS = (
    "nothing read and nothing removed: no merge base between --released-at "
    "and HEAD was handed to this, and the rule arm asks its predicate there.\n"
)


def base_heading(found):
    """The heading for a directory kept at the base, true of both label forms:
    the ref's own commit, where the CI readers ask too, or a fork the ref has
    moved past, where they do not."""
    if found.get("base_moved"):
        return RULE_MOVED_HEADING.format(base=found["base_label"], ref=found["ref"])
    return RULE_BASE_HEADING.format(base=found["base_label"])


TAKES_HEADING = (
    "what a retirement here would take with it — read each before `settle --retire`:"
)
READERS_HEADING = (
    "checks that read `seal/specs` — each owes an answer by "
    "`skills/settle/SKILL.md` §3\nbefore the directories go:"
)


def write_rule_kept(kept, out, base=None):
    """Each spec-less directory the rule arm keeps, with every open row.

    With `base`, the rows are the ones open at that revision rather than in
    the tree, and each line says so. A directory kept there with no row open
    is absent at the base or wrote a `spec.md` in its history there, and the
    line says that rather than printing no reason."""
    where = f" at {base}" if base else ""
    for work_item_id, rows in kept:
        out.write(f"    {work_item_id}\n")
        for name, item in rows:
            out.write(f"        open in {name}{where}: {item}\n")
        if not rows and base:
            out.write(
                f"        the rule does not hold at {base}: the directory is "
                "absent there, or its history there wrote a `spec.md`\n"
            )
        elif not rows:
            out.write(
                "        the rule's predicate refused it with nothing open read\n"
            )


# --- the report ------------------------------------------------------------


def survey(root, ref):
    """What the report is derived from, and where the retirement gets released.

    One walk for the listing, so no work item appears in two of its lists.

    **The retirement does not take its candidates from here.** `retire` reads
    the markers, the directories and the guard from the tree again, and its
    own docstring says why: a classification made for a printed list is not a
    guard on a destructive act. This sentence used to say the opposite — that
    the retirement was derived from this walk, and that a second traversal was
    the failure mode to avoid — which after round 1's finding 4 was the stale
    half of a contradiction, and the half a reader meets first. Left standing
    it invites the next editor to simplify `retire` back to `found["folded"]`,
    which is exactly the mutation that reopens that finding.

    What the retirement does take from here is `released`, which only git can
    answer and which this has already asked, and `base`, the merge base of
    `ref` and `HEAD` (#602), for the same reason.

    None where `ref` does not resolve. Where it resolves and shares no commit
    with `HEAD`, the dict holds `base` None and nothing else is classified:
    the rule arm asks its predicate of the base, and asking it of `None`
    would ask the working tree instead, which is the one answer #602 exists
    to stop `settle` from giving alone."""
    present = work_items(root)
    on_base = released(root, ref)
    if on_base is None:
        return None
    reader = load(READER, "specseal_unverified_reader")
    base = reader.merge_base(root, ref)
    if base is None:
        return {"base": None, "base_label": None}
    folded = reader.folded_items(root)

    ref_commit = reader.commit_of(root, ref)
    survey = {
        "base": base,
        "base_label": reader.base_label(ref, ref_commit, base),
        "base_moved": base != ref_commit,
        "ref": ref,
        "released": [i for i in present if i in on_base],
        "unreleased": [i for i in present if i not in on_base],
        "folded": [],
        "unfolded": [],
        "rule": [],
        "rule_kept": [],
        "rule_base_kept": [],
        "retiring": [],
        "takes": {},
        "citations": {},
        "readers": [],
    }
    for work_item_id in survey["released"]:
        if work_item_id in folded:
            survey["folded"].append(work_item_id)
            continue
        # D3: a released work item with no `spec.md` states no rule, so there
        # is nothing to place and it is not waiting for a fold. Whether the rule arm
        # takes it is the predicate's answer, the one every CI reader asks of
        # the merge-base, and since #602 this asks it of the merge base of the
        # ref and `HEAD` as well: a closure on the working branch that the base
        # has not seen passes the tree and, while the base has not moved since
        # the fork, fails the release pull request. The tree is asked first, so a
        # directory with a row open on disk stays under *kept by the rule*.
        if not has_spec(root, work_item_id):
            directory = f"{SPECS}/{work_item_id}"
            if not reader.retired_by_rule(root, None, directory):
                survey["rule_kept"].append(
                    (work_item_id, reader.open_record_rows(root, None, directory))
                )
            elif not reader.retired_by_rule(root, base, directory):
                survey["rule_base_kept"].append(
                    (work_item_id, reader.open_record_rows(root, base, directory))
                )
            else:
                survey["rule"].append(work_item_id)
            continue
        survey["unfolded"].append(work_item_id)

    survey["plan"] = rule_plan(root, ref, base, survey["unfolded"], reader)
    survey["unfolded"] = survey["plan"]["premodel"]

    # What a retirement here would take with it, by either arm: D1's table,
    # the three things #514's frame found by hand and the command should
    # report by itself.
    survey["retiring"] = survey["folded"] + survey["rule"]
    if survey["retiring"]:
        for work_item_id in survey["retiring"]:
            survey["takes"][work_item_id] = reader.open_record_rows(
                root, None, f"{SPECS}/{work_item_id}"
            )
        survey["citations"], survey["readers"] = citations(root, survey["retiring"])
    # The process arm's dry run (#729), over every released directory, folded
    # or not, since that arm does not wait for the fold.
    survey["process"] = process_plan(root, survey["released"])
    return survey


def read_text(root, rel):
    """A file's text as it stands, line ends kept, or None where it is absent."""
    try:
        with open(under(root, rel), encoding="utf-8", newline="") as f:
            return f.read()
    except OSError:
        return None


def rule_plan(root, ref, base, ids, reader):
    """What `--apply` does with the released specs IDS, replayed in memory.

    Each spec is read as REF holds it. One with no `## Rule changes` is
    `premodel`. One whose section does not parse, whose record holds an open
    row here or at BASE, whose adding commit is not on REF, or that conflicts
    with another at one place is held, and `rule_changes.replay` refuses it
    and waits every later spec at its places."""
    rules = load(RULES, "specseal_rule_changes")
    parsed, premodel = {}, []
    for work_item_id in ids:
        text = reader.show(root, ref, f"{SPECS}/{work_item_id}/spec.md") or ""
        found = rules.parse(text)
        if found.ops is None:
            premodel.append(work_item_id)
        else:
            parsed[work_item_id] = found
    ordered = rules.order(root, ref, list(parsed), SPECS)
    held = {i: list(p.errors) for i, p in parsed.items() if p.errors}
    for work_item_id, commit in ordered:
        why = held.setdefault(work_item_id, [])
        if commit is None:
            why.append((0, f"no commit on {ref} adds its spec.md"))
        directory = f"{SPECS}/{work_item_id}"
        rows = reader.open_record_rows(root, None, directory) or (
            reader.open_record_rows(root, base, directory)
        )
        if rows:
            why.append((0, f"its record holds an open row: {rows[0][1]}"))
    held = {i: why for i, why in held.items() if why}
    entries = [(i, c, parsed[i].ops) for i, c in ordered if i not in held]
    for work_item_id, (other, (file, section)) in rules.conflicts(
        root, entries
    ).items():
        held[work_item_id] = [
            (0, f"a conflict with {other} at {file} section `{section}`: "
                "merge order cannot decide them")
        ]  # fmt: skip
    documents, applied, refused = rules.replay(
        lambda rel: read_text(root, rel),
        [(i, parsed[i].ops) for i, _ in ordered],
        held,
    )
    return {
        "order": [i for i, _ in ordered],
        "parsed": parsed,
        "premodel": premodel,
        "documents": documents,
        "applied": applied,
        "refused": refused,
    }


def write_plan(plan, rule, out):
    """The dry run's sections for the rule changes: pending, refused, and what
    `--apply` would remove."""
    pending = {}
    for work_item_id in plan["applied"]:
        for op in plan["parsed"][work_item_id].ops:
            where = f"section `{op.section}`" if op.section else "a new document"
            pending.setdefault(op.file, []).append(
                f"        {op.kind} {where}  {work_item_id} spec.md:{op.line}"
            )
    if pending:
        out.write("\npending rule changes, in merge order:\n")
        for file, lines in pending.items():
            out.write(f"    {file}\n" + "\n".join(lines) + "\n")
    if plan["refused"]:
        out.write("\nrefused — nothing of the spec applies, and its directory stays:\n")
        for work_item_id, line, why in plan["refused"]:
            where = f"spec.md:{line}" if line else "spec.md"
            out.write(f"    {work_item_id}  {where}  {why}\n")
    nothing = [i for i in plan["applied"] if not plan["parsed"][i].ops]
    if nothing:
        out.write("\nno rule to apply (`nothing — <why>`):\n")
        out.write("".join(f"    {i}\n" for i in nothing))
    removes = plan["applied"] + rule
    if removes:
        out.write("\nwhat `settle --apply` would remove:\n")
        out.write("".join(f"    {SPECS}/{i}/\n" for i in removes))


def has_spec(root, work_item_id):
    """Whether the work item's directory holds a `spec.md` on disk."""
    return os.path.isfile(under(root, f"{SPECS}/{work_item_id}/spec.md"))


# A path into a work item directory, however it is spelled before `specs/`
# (`seal/specs/`, the old `specs/`, a local-mode root). The name may be cut
# short with an ellipsis, which is how this repository's prose abbreviates a
# long id; a marker and a bare id carry no `/` after the name, so neither is
# read as a citation. `rest` is what follows the name, read by lookahead so
# that it consumes nothing a second citation on the line could start with: the
# process arm (#729) lists a citation only where it lands in a file it takes.
CITATION_RE = re.compile(
    r"specs/(\d{6,}[^\s/`'\"()\[\]|<>*]*)/(?=(?P<rest>[^\s`'\"()\[\]|<>*]*))"
)
ELLIPSES = ("…", "...")


def names(name, work_item_id):
    """Whether a cited directory name, possibly abbreviated, is this id."""
    for dots in ELLIPSES:
        if name.endswith(dots):
            stem = name[: -len(dots)]
            return bool(stem) and work_item_id.startswith(stem)
    return name == work_item_id


def tracked_text(root):
    """`(repo-relative path, text)` for every tracked text file outside
    `seal/specs/`. A file holding a NUL byte is binary and skipped."""
    r = subprocess.run(
        ["git", "-C", root, "ls-files", "-z"],
        capture_output=True,
    )
    if r.returncode != 0:
        return
    for rel in r.stdout.decode("utf-8", "replace").split("\0"):
        if not rel or rel.startswith(SPECS + "/"):
            continue
        try:
            with open(under(root, rel), "rb") as f:
                data = f.read()
        except OSError:
            continue
        if b"\0" in data:
            continue
        yield rel, data.decode("utf-8", "replace")


def citations(root, work_item_ids, inside=None):
    """`({id: ["path:line", ...]}, [tests/ files naming seal/specs])`.

    The two listings a fold otherwise builds by hand. A path outside
    `seal/specs/` that cites into a retiring directory stops resolving when
    it goes, and each one is the fold's to rewrite or leave with a reason;
    and every `tests/` file that reads `seal/specs` is a check
    `skills/settle/SKILL.md` §3 says has to be answered before anything is
    removed. One scan of the tracked tree answers both.

    `inside`, where given, narrows the first listing to the citations whose
    path after the directory name it accepts. The process arm (#729) removes
    part of a directory, and a citation into a file that stays still resolves.
    """
    cited = {i: [] for i in work_item_ids}
    readers = []
    for rel, text in tracked_text(root):
        if rel.startswith(TESTS) and SPECS in text:
            readers.append(rel)
        if "specs/" not in text:
            continue
        for number, line in enumerate(text.split("\n"), start=1):
            for m in CITATION_RE.finditer(line):
                if inside is not None and not inside(m.group("rest")):
                    continue
                for work_item_id in work_item_ids:
                    if names(m.group(1), work_item_id):
                        where = f"{rel}:{number}"
                        if where not in cited[work_item_id]:
                            cited[work_item_id].append(where)
    return cited, sorted(readers)


def report(found, ref, out=sys.stdout):
    """What a session reads before it writes its standing statements.

    A survey with no base is refused at exit 2 with `retire`'s sentence, for
    `retire`'s reason: a caller that skips `main` would otherwise meet a
    `KeyError` on the keys such a survey does not carry (round 1, ⬜ 4)."""
    if not found.get("base"):
        out.write(NO_BASE_SAYS)
        return 2
    write = out.write
    foldable = len(found["unfolded"])
    write(f"released and unfolded: {foldable} work item{plural(foldable)}\n")
    write(
        f"(released = present at {ref}; {len(found['unreleased'])} "
        "unreleased and untouched)\n"
    )
    write(
        f"no spec.md: {len(found['rule'])} to retire by the rule, "
        f"{len(found['rule_kept'])} kept by it, "
        f"{len(found['rule_base_kept'])} kept because the closure has not "
        f"reached {found['base_label']}\n"
    )

    if "plan" in found:
        write_plan(found["plan"], found["rule"], out)

    if found["unfolded"]:
        write(
            "\nwaiting for a fold — read each `spec.md` and place what is still true:\n"
        )
        for work_item_id in found["unfolded"]:
            write(f"    {work_item_id}\n")

    if found["folded"]:
        write("\nfolded already, waiting to be retired — `settle --retire`:\n")
        for work_item_id in found["folded"]:
            write(f"    {work_item_id}\n")

    if found["rule"]:
        write(f"\n{RULE_HEADING}\n")
        for work_item_id in found["rule"]:
            write(f"    {work_item_id}\n")

    if found["rule_kept"]:
        write(f"\n{RULE_KEPT_HEADING}\n")
        write_rule_kept(found["rule_kept"], out)

    if found["rule_base_kept"]:
        write(f"\n{base_heading(found)}\n")
        write_rule_kept(found["rule_base_kept"], out, base=found["base_label"])

    if found["retiring"]:
        write(f"\n{TAKES_HEADING}\n")
        for work_item_id in found["retiring"]:
            write(f"    {work_item_id}\n")
            rows = found["takes"].get(work_item_id, [])
            cited = found["citations"].get(work_item_id, [])
            if not rows and not cited:
                write(
                    f"        nothing open, and nothing outside {SPECS}/ "
                    "cites into it\n"
                )
            for name, item in rows:
                write(f"        open in {name}: {item}\n")
            for where in cited:
                write(f"        cited from {where}\n")
        write(f"\n{READERS_HEADING}\n")
        for rel in found["readers"] or ["none under tests/"]:
            write(f"    {rel}\n")

    if "process" in found:
        write_process_section(found, out)

    write(
        "\nNothing was written and nothing was removed. `skills/settle/SKILL.md`\n"
        "is the procedure: one standing statement per rule in `docs/`, each\n"
        "folded sentence carrying its `<!-- specs/<id> -->` comment, then\n"
        "`settle --retire` removes the directories that comment now covers.\n"
    )
    return 0


def retire(found, root, out=sys.stdout):
    """Remove the directories whose fold `docs/` records, and nothing else.

    The marker is the condition, so a directory is removed only where a
    policy document has absorbed the work item.

    **The candidate set is read from the tree, not taken from `survey`**: a
    classification made for a printed list is not a guard on a destructive
    act, so this one decides what is removed, and it answers to the tree.

    `found` is still where *released* comes from, because only git can answer
    that and `survey` has already asked.

    **`present` stays in the intersection although it decides nothing today.**
    Round 2's finding 6 is right that it is inert: `found["released"]` is
    already a subset of the directories `survey` saw, so the only case the
    term can catch is a directory removed between the two calls in this same
    process. What it costs is one set operation; what it buys is that
    `shutil.rmtree` below cannot be handed a path that is gone. Leaving it out
    would make a destructive call depend on an invariant held by another
    function at another moment, which is the coupling the paragraph above is
    about. It also has a second reader now — `stranded` is `marked & present`,
    and that one is not inert at all.

    **The rule arm asks its predicate twice (#602)**: of the tree, and of
    `found["base"]`, the merge base of `--released-at` and `HEAD`. It takes
    the base from `found` as it takes *released*, and asks the predicate
    itself. A `found` with no base is refused at exit 2 before anything is
    read, because the predicate asked of `None` is asked of the tree alone."""
    base = found.get("base")
    if not base:
        out.write(NO_BASE_SAYS)
        return 2
    label = found.get("base_label") or base
    reader = load(READER, "specseal_unverified_reader")
    marked = reader.folded_items(root)
    present = set(work_items(root))
    released_at_base = set(found["released"])
    # The rule arm (D3), read from the tree like the marker arm and for the
    # same reason: a released directory with no `spec.md` whose record holds
    # nothing open is a candidate with no marker, and one whose record does
    # is kept and named. The predicate is the one every CI reader asks, and it
    # is asked at the merge base of the ref and `HEAD` as well as here (#602),
    # which is where they ask until the base moves past the fork and earlier
    # than they do after: a directory whose closure that base has not seen is
    # kept and named with the rows open there.
    spec_less = sorted(
        i for i in (present & released_at_base) - marked if not has_spec(root, i)
    )
    by_tree = [
        i for i in spec_less if reader.retired_by_rule(root, None, f"{SPECS}/{i}")
    ]
    by_rule = [i for i in by_tree if reader.retired_by_rule(root, base, f"{SPECS}/{i}")]
    rule_kept = [
        (i, reader.open_record_rows(root, None, f"{SPECS}/{i}"))
        for i in spec_less
        if i not in by_tree
    ]
    base_kept = [
        (i, reader.open_record_rows(root, base, f"{SPECS}/{i}"))
        for i in by_tree
        if i not in by_rule
    ]
    removable = sorted((marked & present & released_at_base) | set(by_rule))
    if not removable and not rule_kept and not base_kept:
        # THREE states, and they are told apart by what the sentence asserts
        # rather than by what happens to be empty. Round 1 split one of them
        # out of the other; round 2's finding 2 is that the split fired on
        # `if marked:`, which asks only whether `docs/` records any fold at
        # all, while the sentence it prints asserts that none of the marked
        # items still has a directory. Nothing had asked that, and a reader
        # who acts on *the fold is complete* stops looking.
        stranded = sorted(marked & present)
        if marked and not stranded:
            out.write(
                f"nothing left to retire: docs/ records the fold of "
                f"{len(marked)} work item{plural(len(marked))}, and none of "
                f"them still has a directory under {SPECS}/. "
                "The fold is complete.\n"
            )
            return 0
        if stranded:
            # Marked, still on disk, and not present at `--released-at`. It is
            # reachable two ways: a policy absorbing work that has not merged
            # to the release branch yet, and a run pointed at an older ref
            # than the one the items merged to.
            out.write(
                f"nothing to retire: docs/ records the fold of "
                f"{len(stranded)} work item{plural(len(stranded))} whose "
                f"directory is still under {SPECS}/, and none of them is "
                "present at the release ref, so nothing here reads as "
                "released:\n"
            )
            for work_item_id in stranded:
                out.write(f"    {work_item_id}\n")
            return 1
        out.write(
            "nothing to retire: no released work item carries a "
            "`<!-- specs/<id> -->` marker in docs/, so none of them has been "
            "folded yet, and none is a released directory with no `spec.md`. "
            "`settle` alone says which ones are waiting for one.\n"
        )
        return 1
    for work_item_id in removable:
        shutil.rmtree(under(root, f"{SPECS}/{work_item_id}"))
        why = (
            "  (no `spec.md` — retired by the rule, with no marker)"
            if work_item_id in by_rule
            else ""
        )
        out.write(f"removed {SPECS}/{work_item_id}/{why}\n")
    if rule_kept:
        out.write(f"\n{RULE_KEPT_HEADING}\n")
        write_rule_kept(rule_kept, out)
    if base_kept:
        out.write(f"\n{base_heading(found)}\n")
        write_rule_kept(base_kept, out, base=label)
    kept = len(rule_kept) + len(base_kept)
    out.write(
        f"\nretired {len(removable)} work item{plural(len(removable))}; {kept} kept\n"
    )
    return 1 if kept else 0


# --- the process record (#729) ---------------------------------------------

# What a work item's directory holds for its pull request and nothing after
# its release: the round records and the reviewer's reports, the phase
# records, and the files a pull request alone reads.
# `docs/one-root-by-lifetime.md` names the class *the process record*.
#
# **An allow-list, because removal is the destructive direction.** A file on
# neither list is kept and printed, never taken: one released directory once
# held an `ab-comparison.md`, and a kind nobody anticipated is exactly the
# file a guess would lose. That is `chain_check.py#REGULAR`'s direction, for
# the same reason.
PROCESS_DIRS = ("rounds", "phases")
PROCESS_FILES = (
    "broad-gate.md",
    "guarantee.md",
    "handoff.md",
)
# What stays until the fold retires the directory. `routing.md` is the item's
# identity to `chain_check`, `release_seal` and `root-migrate`; `overview.md`
# holds the `## Not verified` rows `unverified_check --baseline` counts; and
# `changelog.md` is #728's to decide.
DURABLE = (
    "routing.md",
    "spec.md",
    "plan.md",
    "questions.md",
    "overview.md",
    "changelog.md",
)

# What the arm prints, and the dry run's heading. Pinned by
# `tests/test_settle_retires_the_process_record.py`, which also holds
# `skills/settle/SKILL.md` to quoting each one, because a person acts on them.
PROCESS_HEADING = (
    "the process record — no check reads it after its work item's release, so\n"
    "`settle --retire-process` takes it now, fold or no fold:"
)
PROCESS_UNKNOWN_HEADING = (
    "not a process record — on neither of `settle`'s lists, so it is kept "
    "rather than\nguessed at:"
)
PROCESS_CITED_HEADING = (
    "cited from outside seal/specs/ — each of these now resolves only in git "
    "history, at\nthe tag of the release that shipped it:"
)
PROCESS_DONE = (
    "nothing left to retire: no released work item still holds a process record."
)

# One released item's process record, as the tree holds it now. `take` is
# `(name, is_dir, file count)` per top-level entry the arm removes, and
# `unknown` the entries on neither list.
ProcessItem = collections.namedtuple("ProcessItem", "id take files unknown")


def is_process_record(name, is_dir):
    """Whether a top-level entry of a work item's directory is on the list."""
    if is_dir:
        return name in PROCESS_DIRS
    return name in PROCESS_FILES or (name.startswith("pr.") and name.endswith(".md"))


def process_plan(root, work_item_ids):
    """`[ProcessItem]` for each of these directories still on disk.

    Read from the tree each time it is asked. The report asks it for its
    section and the retirement asks it again, for `retire`'s reason: a
    classification made for a printed list is not a guard on a destructive
    act. A link is never followed into: it is an entry of its own and is
    removed as one, so nothing outside the directory can be reached."""
    plan = []
    for work_item_id in work_item_ids:
        top = under(root, f"{SPECS}/{work_item_id}")
        if not os.path.isdir(top):
            continue
        take, unknown = [], []
        for name in sorted(os.listdir(top)):
            path = os.path.join(top, name)
            is_dir = os.path.isdir(path) and not os.path.islink(path)
            if is_process_record(name, is_dir):
                count = (
                    sum(len(files) for _, _, files in os.walk(path)) if is_dir else 1
                )
                take.append((name, is_dir, count))
            elif is_dir or name not in DURABLE:
                unknown.append(name + ("/" if is_dir else ""))
        plan.append(
            ProcessItem(work_item_id, take, sum(c for _, _, c in take), unknown)
        )
    return plan


def taken_by(path, plan):
    """The id whose process record holds this repository-relative path, or
    None where the path lies in a file the arm leaves standing."""
    for entry in plan:
        for name, is_dir, _ in entry.take:
            spot = f"{SPECS}/{entry.id}/{name}"
            if path == spot or (is_dir and path.startswith(spot + "/")):
                return entry.id
    return None


# A file or directory name as prose writes it: runs of name characters joined
# by single dots, so it never ends in a dot. Whatever follows it in a sentence
# — a closing `.` or `,`, a `:40`, a `#anchor`, a dash — is not part of it,
# and a name that goes on (`handoff.md.bak`, `rounds-old`) is read whole.
CITED_NAME_RE = re.compile(r"[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*")


def cites_a_process_record(rest):
    """Whether the path after a cited directory's name lands in a file the
    process arm takes — `citations`' `inside` for this arm.

    The name is read off the front of `rest` by `CITED_NAME_RE` rather than
    by stripping the tails prose is known to add, because the list of tails
    is the list that missed four shapes in #729's round 1. A name on
    `PROCESS_DIRS` names the directory, with a slash after it or none. The
    answer is `is_process_record`'s, so the listing and the removal cannot
    disagree about a name; an empty name is on neither list."""
    m = CITED_NAME_RE.match(rest)
    name = m.group(0) if m else ""
    return is_process_record(name, name in PROCESS_DIRS)


def write_process_section(found, out):
    """The dry run's section: what `settle --retire-process` would take now,
    and what it would keep."""
    plan = found["process"]
    takeable = [p for p in plan if p.take]
    files = sum(p.files for p in takeable)
    out.write(f"\n{PROCESS_HEADING}\n")
    out.write(
        f"    {files} file{plural(files)} in {len(takeable)} released work "
        f"item{plural(len(takeable))}\n"
    )
    for entry in plan:
        for name in entry.unknown:
            out.write(f"    {SPECS}/{entry.id}/{name}  not a process record, kept\n")


def retire_process(found, root, out=sys.stdout):
    """Remove the process record of every released work item, and nothing
    else (#729).

    It does not wait for the fold, because it needs no judgment: what it
    removes is read by no check after the release that ships the item, and the
    SDD set and `routing.md` stay for the fold to absorb. A relative reference
    from that SDD set into what goes is not listed: it is a pointer a person
    follows, and it resolves at the release tag (#729's round 1, 🟡 1). *Released* is the
    same test the fold uses — the directory is present at `--released-at` —
    taken from `found` because only git answers it.

    A path outside `seal/specs/` that cites into a removed file is listed and
    never refused, as `--retire` lists one: it resolves in git history at the
    release's tag, and the tree already holds citations of that kind into
    directories a fold retired.

    Exit 0, including when nothing is left to remove, which is the state a
    previous run leaves, not work still to do."""
    present = set(work_items(root))
    ids = sorted(present & set(found["released"]))
    plan = process_plan(root, ids)
    removable = [p for p in plan if p.take]
    unknown = [(p.id, name) for p in plan for name in p.unknown]
    if not removable and not unknown:
        out.write(PROCESS_DONE + "\n")
        return 0
    cited = {}
    if removable:
        cited = citations(
            root, [p.id for p in removable], inside=cites_a_process_record
        )[0]
    for entry in removable:
        for name, is_dir, count in entry.take:
            path = under(root, f"{SPECS}/{entry.id}/{name}")
            if is_dir:
                shutil.rmtree(path)
                out.write(
                    f"removed {SPECS}/{entry.id}/{name}/  ({count} file{plural(count)})\n"
                )
            else:
                os.remove(path)
                out.write(f"removed {SPECS}/{entry.id}/{name}\n")
    if unknown:
        out.write(f"\n{PROCESS_UNKNOWN_HEADING}\n")
        for work_item_id, name in unknown:
            out.write(f"    {SPECS}/{work_item_id}/{name}\n")
    if any(cited.values()):
        out.write(f"\n{PROCESS_CITED_HEADING}\n")
        for work_item_id in sorted(cited):
            if cited[work_item_id]:
                out.write(f"    {work_item_id}\n")
                for where in cited[work_item_id]:
                    out.write(f"        cited from {where}\n")
    files = sum(p.files for p in removable)
    out.write(
        f"\nretired the process record of {len(removable)} work "
        f"item{plural(len(removable))} ({files} file{plural(files)})\n"
    )
    return 0


def main(argv=None):
    """Survey, retire or retire the process record; the exit code is the verdict."""
    ap = argparse.ArgumentParser(
        prog="settle",
        description="Name the released work items a `docs/` policy has yet to absorb.",
    )
    ap.add_argument(
        "--root", default=None, help="repository root (default: the one this is run in)"
    )
    ap.add_argument(
        "--released-at",
        default="origin/main",
        metavar="REF",
        help="the branch a release merges to. A work item is released when "
        "its directory is present there, and a directory with no spec.md is "
        "retired only when its record is closed at the merge base of this "
        "and HEAD too (default: origin/main)",
    )
    # Two removals, never one run of both: `--retire` is the second half of
    # the fold and never its own act, and `--retire-process` is its own act
    # and never waits for the fold. One flag with both meanings would make the
    # first sentence false (#729's plan, *Fold `--retire-process` into
    # `--retire`*).
    arms = ap.add_mutually_exclusive_group()
    arms.add_argument(
        "--retire-process",
        action="store_true",
        help="remove the process record of every released work item — "
        "rounds/, phases/ and the files written only for a pull "
        "request — and leave routing.md and the SDD set for the fold. Writes no "
        "prose and does not wait for the fold. A file on neither list is kept "
        "and named",
    )
    arms.add_argument(
        "--retire",
        action="store_true",
        help="remove the directories whose fold `docs/` records, and the "
        "released ones with no spec.md and nothing open in their record. "
        "Writes no prose: what it removes is what a policy document has "
        "already absorbed, or a record of a moment that states no rule",
    )
    args = ap.parse_args(argv)

    root = os.path.abspath(args.root or os.getcwd())
    # The root is resolved through the one resolver, `hooks/optin.py#home_at`.
    # Before this, `under(root, SPECS)` was the only place looked at, so a
    # local-mode repository holding ninety-eight work items was told it had
    # none — and the sentence written for local mode, in the `--released-at`
    # refusal below, could never be printed, because this check fired first
    # and always.
    optin = load(OPTIN, "specseal_optin")
    # The common git directory is resolved once and handed down: `home_at`
    # takes it for exactly this caller, the one that needs the value for the
    # opt-out sentence below as well, and resolving it here and again inside
    # `home_at` was round 3's finding 5.
    common = optin.git_common_dir(root)
    home = optin.home_at(root, common)
    if not home:
        # `home_at` answers "" for two states, and round 2's finding 7 is that
        # they were given one sentence: no root at either place, and a
        # repository that opted out with the scratch marker. The second was
        # told it had no work items while holding them in the tree, which is
        # the defect one refusal up reached through another door.
        #
        # `isfile`, the accessor `home_at` uses and says why: `exists` also
        # accepts a DIRECTORY of that name, which no gate reads as an opt-out,
        # so this arm told such a repository to delete "that file" to turn the
        # gates back on — every clause false (round 3, finding 1).
        if common and os.path.isfile(os.path.join(common, optin.SCRATCH)):
            sys.stderr.write(
                f"settle: {root} has opted out — `{optin.SCRATCH}` is under "
                "its git directory, so every gate in this plugin reads it as "
                "a repository that never opted in and this command will "
                "remove nothing. Delete that file to turn them back on.\n"
            )
            return 2
        sys.stderr.write(
            f"settle: {root} has no {SPECS}/ at either place — nothing was "
            "read. This command folds work items, and a repository with none "
            "has nothing to settle.\n"
        )
        return 2
    # **Local mode refuses, and it is not the same refusal.** Resolving the
    # root is only half the finding: with the root found, a local-mode run
    # would go on to ask git which work items are released, git would answer
    # with none — an uncommitted root has no path in any tree — and the report
    # would say there is nothing to fold. That is the quiet zero this whole
    # module is written against, reached by the other door. So the state is
    # named here. It is the right answer as well as the honest one: nothing
    # removed from a root git never held can be recovered.
    #
    # The sentence written for local mode used to live inside the
    # `--released-at` refusal below and this comment claimed the fix made it
    # reachable at last. It did the opposite — that branch fires only for a
    # ref that does not resolve, and this one returns before `survey` is
    # called, so the clause was more unreachable than it had been (round 2,
    # finding 4). It is stated here and taken out of there.
    if os.path.realpath(home) != os.path.realpath(under(root, "seal")):
        sys.stderr.write(
            f"settle: the seal root of {root} is {home}, which is local mode "
            "— nothing was read. Local mode never commits the root, so no ref "
            "holds the work item directories, nothing in them can be called "
            "released, and nothing removed from them could be recovered. "
            "`seal mode shared` moves the root into the tree, and this "
            "command works from there.\n"
        )
        return 2
    # **A settled root is not an unusable one (#517, `spec.md` G7).** After
    # the last retirement the tree that ran `--retire` holds an empty
    # `seal/specs/`, and a fresh checkout of that commit holds none at all,
    # because git keeps no empty directory. Both are the state a complete
    # fold reaches, with the `seal/` root still there, and this used to
    # refuse the second at exit 2 — the command unable to run on its own
    # finished work. A repository with no root at either place is still
    # refused above.
    if not work_items(root):
        sys.stdout.write(SETTLED.format(root=root, specs=SPECS))
        return 0

    found = survey(root, args.released_at)
    if found is None:
        sys.stderr.write(
            f"settle: --released-at {args.released_at} does not resolve in {root} — nothing was "
            "read. Without it every work item reads as unreleased and this "
            "would report nothing to fold, which is the one answer it must "
            "not give by accident.\n"
        )
        return 2
    # #602: the rule arm asks its predicate of the merge base of the ref and
    # `HEAD`. The CI readers compute the same merge base from their own
    # `HEAD`, which on a pull request is the merge ref, so theirs is the
    # base's tip: the same commit while the base has not moved since the
    # fork, and a later one when it has, where the two can disagree in either
    # direction (the module docstring says how). Two histories that share no
    # commit have none, and neither does a clone too shallow to reach the
    # commit they share; the predicate asked of nothing would be asked of the
    # working tree alone — the answer that let a closure the base had not
    # seen retire its directory. Refused in both arms, so the report never
    # lists what the retirement then refuses.
    if found["base"] is None:
        sys.stderr.write(
            f"settle: --released-at {args.released_at} and HEAD share no commit "
            f"in {root}, or this clone is too shallow to reach the one they "
            "share (`git fetch --unshallow`) — nothing was read. The rule arm "
            "asks whether a record is closed at their merge base, and there is "
            "none to ask.\n"
        )
        return 2

    if args.retire:
        return retire(found, root)
    if args.retire_process:
        return retire_process(found, root)
    return report(found, args.released_at, out=sys.stdout)


if __name__ == "__main__":
    # A console that cannot encode what this prints kills it with stdout
    # empty, which is how a hook says "nothing to see here". `hooks/console.py`
    # owns the reasoning and the three decisions behind these lines.
    for _name, _errors in (
        ("stdin", "replace"),
        ("stdout", "replace"),
        ("stderr", "backslashreplace"),
    ):
        _stream = getattr(sys, _name, None)
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors=_errors)
    sys.exit(main())
