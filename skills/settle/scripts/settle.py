#!/usr/bin/env python3
"""settle — apply the rule changes released specs state to the policy root.

  settle                        the dry run: what `--apply` would write and remove
  settle --apply                apply them in place, and remove what they settle
  settle --released-at REF      what counts as released (default origin/main)
  settle --root DIR             a repository other than this one

**Released means present on the branch the release merges to**, which is why
`--released-at` names a ref rather than a date.

**Each released spec's `## Rule changes` is applied in merge order, whole or
not at all.** `rule_changes.py` reads and replays the sections; this writes
the result into the policy root (`seal/config.md`'s `Policy root` row,
`docs` when absent, creating it with its index where it is absent) and
removes each applied spec's directory whole, its
process record included. A spec it cannot place, one whose record still holds
an open row, and two that merge order cannot decide at one place apply
nothing, and their directories stay. A spec with no section was written before
the section existed: it is named and kept. No marker is written. The judgment
was made when the spec was written and reviewed, so applying it judges
nothing.

**The rule arm.** A released work item that wrote no `spec.md` states no rule,
and it goes when nothing in its record is open (#517's D3). Whether a
directory qualifies is `unverified_check.py#settled`, the predicate
every CI reader asks of the merge base, asked here of the working tree and of
the merge base of `--released-at` and `HEAD` (#602). A CI reader on a pull
request stands on the merge ref, so its merge base is the base branch's tip:
the same commit as this one until the base moves past the fork. A row closed
here and still open at that base keeps its directory, under a heading naming
the base and, where the base has moved, the merge that moves it.

**Local mode is refused rather than reported on.** A root under the common
git directory is never committed, so no ref holds the work item directories
and nothing removed from them could be recovered. `seal mode shared` moves the
root into the tree. A repository that opted out with the scratch marker, an
empty FILE read the way `hooks/optin.py#home_at` reads it, is refused too.

Exit codes: 0 the report was produced, `--apply` refused and kept nothing, or
the root holds no work item, which is the state a complete settle reaches · 1
`--apply` refused or kept something — a spec it could not place, a record
with an open row, or a spec-less directory whose closure has not reached the
merge base of `--released-at` and `HEAD` · 2 the arguments or the tree were
unusable: a `--released-at` ref that does not resolve, a `--released-at` ref
sharing no commit with `HEAD` or a clone too shallow to reach the one they
share, a root at neither place, a root in local mode, a repository that opted
out, and a sibling script that is not beside it. An interpreter below the
floor never reaches this file through `bin/settle`: `hooks/launch.py`
refuses it with 2 first.
"""

import argparse
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
FOLD_CHECK = os.path.join(HERE, "fold_check.py")

# What each sibling is for, in the sentence `load` prints when it is missing.
PURPOSES = {
    READER: "it is where a record's open rows are read from",
    OPTIN: "it is what finds the repository's seal/ root",
    RULES: "it is what reads a spec's `## Rule changes`",
    FOLD_CHECK: "it is what reads the index and the one read after an apply",
}

SPECS = "seal/specs"
TESTS = "tests/"


def under(root, rel):
    """The disk path of a `/`-joined repository-relative path."""
    return os.path.join(root, *rel.split("/"))


def plural(count, many="s", one=""):
    """`s` unless there is one of them. Every count this prints is read by a
    person, and `1 work items` is the tell that nobody read the output."""
    return one if count == 1 else many


def load(path, name):
    """Import a sibling script by path, or refuse with a sentence saying what
    the missing file is for — its `PURPOSES` entry — and exit 2.

    Not a bare `exec_module`: `spec_from_file_location` hands back a spec for
    any path ending in `.py`, present or not, so a missing reader would raise
    `FileNotFoundError` — a traceback where every failure here is a sentence.
    Exit 2 and not 1, because nothing about the tree has been read (#590)."""
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

    None for a ref that does not resolve, and the caller refuses: a ref this
    cannot read would make every work item read as unreleased and the report
    say there is nothing to do, the quiet zero every checker here is written
    against."""
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


def has_spec(root, work_item_id):
    """Whether the work item's directory holds a `spec.md` on disk."""
    return os.path.isfile(under(root, f"{SPECS}/{work_item_id}/spec.md"))


def read_text(root, rel):
    """A file's text as it stands, line ends kept, or None where it is absent."""
    try:
        with open(under(root, rel), encoding="utf-8", newline="") as f:
            return f.read()
    except OSError:
        return None


# What a settled root prints, for the dry run and `--apply` alike.
SETTLED = (
    "settle: {specs}/ in {root} holds no work item — nothing to apply and "
    "nothing to remove. A complete settle ends here, and git keeps no empty "
    "directory, so a fresh checkout of this state has no {specs}/ at all.\n"
)

# The rule arm's headings. Pinned by `tests/test_settle_reads_before_it_removes.py`.
RULE_HEADING = (
    "retired by the rule — released, no `spec.md`, nothing open; "
    "`settle --apply`\nremoves these, because a moment states no rule:"
)
RULE_KEPT_HEADING = (
    "kept by the rule — no `spec.md`, but the record still holds an open "
    "row, which\nleaves by being closed (`closed` with what closed it) in a pull "
    "request merged before the\none that retires the directory, and merged "
    "to the branch the release merges to,\nnever with it:"
)
# #602: nothing is open in the tree, and the base still holds a row open.
# `{base}` is `unverified_check.py#base_label`'s spelling of the merge base of
# `--released-at` and `HEAD`; `RULE_MOVED_HEADING` is the case where the ref
# has moved past the fork.
RULE_BASE_HEADING = (
    "kept until the closure reaches {base} — no `spec.md` and nothing open "
    "here, but\nthe record there still holds an open row, and the CI readers "
    "ask the rule there.\nMerge the closure to the branch the release merges "
    "to first; the directory goes\nin a later pull request:"
)
RULE_MOVED_HEADING = (
    "kept: the closure has not reached {base} — no `spec.md` and nothing open "
    "here, but\nthe record there still holds an open row. {ref} has moved past "
    "that commit: where\n{ref} already holds the closure, merge {ref} into this "
    "branch and run `settle`\nagain; otherwise merge the closure to {ref} "
    "first. The directory goes in a later\npull request:"
)
PREMODEL_HEADING = (
    "no `## Rule changes` — written before the section existed, so nothing "
    "applies and\nthe directory stays:"
)
REMOVES_HEADING = "what `settle --apply` would remove:"
READERS_HEADING = (
    "checks that read `seal/specs` — each owes an answer "
    "(`skills/settle/SKILL.md`\n§*Answer every check that reads the corpus*) "
    "before the directories go:"
)

# What `report` and `apply` print for a survey that carries no base.
NO_BASE_SAYS = (
    "nothing read and nothing removed: no merge base between --released-at "
    "and HEAD was handed to this, and the rule arm asks its predicate there.\n"
)


def base_heading(found):
    """The heading for a directory kept at the base: the ref's own commit,
    where the CI readers ask too, or a fork the ref has moved past."""
    if found.get("base_moved"):
        return RULE_MOVED_HEADING.format(base=found["base_label"], ref=found["ref"])
    return RULE_BASE_HEADING.format(base=found["base_label"])


def write_rule_kept(kept, out, base=None):
    """Each spec-less directory the rule arm keeps, with every open row.

    With `base`, the rows are the ones open at that revision, and a directory
    kept there with no row open is absent at the base or wrote a `spec.md` in
    its history there, which the line says."""
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


def rule_arm(root, base, ids, reader):
    """`(retired, kept here, kept at the base)` for the spec-less IDS.

    The tree is asked first, so a directory with a row open on disk stays
    under *kept by the rule*; then the base, since a closure the base has not
    seen passes the tree and fails the release pull request (#602)."""
    retired, kept, base_kept = [], [], []
    dirs = [f"{SPECS}/{work_item_id}" for work_item_id in ids]
    here, at_base = reader.settled(root, None, dirs), reader.settled(root, base, dirs)
    for work_item_id in ids:
        directory = f"{SPECS}/{work_item_id}"
        if directory not in here:
            kept.append((work_item_id, reader.open_record_rows(root, None, directory)))
        elif directory not in at_base:
            base_kept.append(
                (work_item_id, reader.open_record_rows(root, base, directory))
            )
        else:
            retired.append(work_item_id)
    return retired, kept, base_kept


def rule_plan(root, ref, base, ids, reader):
    """What `--apply` does with the released specs IDS, replayed in memory.

    Each spec is read as REF holds it. One with no `## Rule changes` is
    `premodel`. One whose section does not parse, whose record holds an open
    row here or at BASE, whose adding commit is not on REF, or that conflicts
    with another at one place is held, and `rule_changes.replay` refuses it
    and waits every later spec at its places."""
    rules = load(RULES, "specseal_rule_changes")
    policy = reader.policy_root(root)
    parsed, premodel = {}, []
    for work_item_id in ids:
        text = reader.show(root, ref, f"{SPECS}/{work_item_id}/spec.md") or ""
        found = rules.parse(text, policy)
        if found.ops is None:
            premodel.append(work_item_id)
        else:
            parsed[work_item_id] = found
    ordered = rules.order(root, ref, list(parsed), SPECS)
    held = {i: list(p.errors) for i, p in parsed.items() if p.errors}
    # On a case-insensitive disk two names that differ only in case are one
    # file, and the second write would erase the first spec's change.
    top = under(root, policy)
    known = {f"{policy}/{n}" for n in (os.listdir(top) if os.path.isdir(top) else [])}
    known |= {op.file for p in parsed.values() for op in p.ops or []}
    for work_item_id, found in parsed.items():
        for op in found.ops or []:
            if any(k != op.file and k.casefold() == op.file.casefold() for k in known):
                held.setdefault(work_item_id, []).append(
                    (op.line, f"{op.file} differs from another document only in case")
                )
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

    def read(rel):
        return read_text(root, rel)

    for work_item_id, (other, at) in rules.conflicts(root, entries, read).items():
        held[work_item_id] = [
            (0, f"a conflict with {other} at {rules.where(at)}: "
                "merge order cannot decide them")
        ]  # fmt: skip
    documents, applied, refused = rules.replay(
        read, [(i, parsed[i].ops) for i, _ in ordered], held
    )
    return {
        "parsed": parsed,
        "premodel": premodel,
        "documents": documents,
        "applied": applied,
        "refused": refused,
    }


def write_outcome(plan, out):
    """The refusals, the specs with nothing to apply, and the pre-model ones."""
    if plan["refused"]:
        out.write("\nrefused — nothing of the spec applies, and its directory stays:\n")
        for work_item_id, line, why in plan["refused"]:
            where = f"spec.md:{line}" if line else "spec.md"
            out.write(f"    {work_item_id}  {where}  {why}\n")
    nothing = [i for i in plan["applied"] if not plan["parsed"][i].ops]
    if nothing:
        out.write("\nno rule to apply (`nothing — <why>`):\n")
        out.write("".join(f"    {i}\n" for i in nothing))
    if plan["premodel"]:
        out.write(f"\n{PREMODEL_HEADING}\n")
        out.write("".join(f"    {i}\n" for i in plan["premodel"]))


def write_rule_arm(found, retired, kept, base_kept, out, heading=True):
    if retired and heading:
        out.write(f"\n{RULE_HEADING}\n")
        out.write("".join(f"    {i}\n" for i in retired))
    if kept:
        out.write(f"\n{RULE_KEPT_HEADING}\n")
        write_rule_kept(kept, out)
    if base_kept:
        out.write(f"\n{base_heading(found)}\n")
        write_rule_kept(base_kept, out, base=found["base_label"])


# --- the dry run -----------------------------------------------------------


def survey(root, ref):
    """What the dry run prints, and where `--apply` gets *released* and the base.

    **`--apply` does not take its candidates from here.** It reads the
    directories, the specs and the records from the tree again, because a
    classification made for a printed list is not a guard on a destructive
    act. What it takes from here is `released`, `ref` and `base`, the merge
    base of `ref` and `HEAD` (#602), which only git answers.

    None where `ref` does not resolve. Where it shares no commit with `HEAD`,
    the dict holds `base` None and nothing else: the rule arm asks its
    predicate of the base, and asked of `None` it would ask the working tree
    alone."""
    present = work_items(root)
    on_base = released(root, ref)
    if on_base is None:
        return None
    reader = load(READER, "specseal_unverified_reader")
    base = reader.merge_base(root, ref)
    if base is None:
        return {"base": None, "base_label": None}
    ref_commit = reader.commit_of(root, ref)
    found = {
        "base": base,
        "base_label": reader.base_label(ref, ref_commit, base),
        "base_moved": base != ref_commit,
        "ref": ref,
        "released": [i for i in present if i in on_base],
        "unreleased": [i for i in present if i not in on_base],
    }
    with_spec = [i for i in found["released"] if has_spec(root, i)]
    spec_less = [i for i in found["released"] if not has_spec(root, i)]
    found["rule"], found["rule_kept"], found["rule_base_kept"] = rule_arm(
        root, base, spec_less, reader
    )
    found["plan"] = rule_plan(root, ref, base, with_spec, reader)
    found["removes"] = found["plan"]["applied"] + found["rule"]
    found["citations"], found["readers"] = citations(root, found["removes"])
    return found


# A path into a work item directory, however it is spelled before `specs/`.
# The name may be cut short with an ellipsis, which is how this repository's
# prose abbreviates a long id; a marker and a bare id carry no `/` after the
# name, so neither is read as a citation.
CITATION_RE = re.compile(r"specs/(\d{6,}[^\s/`'\"()\[\]|<>*]*)/")
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
    r = subprocess.run(["git", "-C", root, "ls-files", "-z"], capture_output=True)
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


def citations(root, work_item_ids):
    """`({id: ["path:line", ...]}, [tests/ files naming seal/specs])`.

    A path outside `seal/specs/` that cites into a directory `--apply` removes
    stops resolving when it goes, and every `tests/` file that reads
    `seal/specs` is a check the skill says has to be answered first. One scan
    of the tracked tree answers both."""
    cited = {i: [] for i in work_item_ids}
    readers = []
    if not work_item_ids:
        return cited, readers
    for rel, text in tracked_text(root):
        if rel.startswith(TESTS) and SPECS in text:
            readers.append(rel)
        if "specs/" not in text:
            continue
        for number, line in enumerate(text.split("\n"), start=1):
            for m in CITATION_RE.finditer(line):
                for work_item_id in work_item_ids:
                    if names(m.group(1), work_item_id):
                        where = f"{rel}:{number}"
                        if where not in cited[work_item_id]:
                            cited[work_item_id].append(where)
    return cited, sorted(readers)


def report(found, ref, out):
    """The dry run: pending changes in merge order, refusals, what `--apply`
    would remove. A survey with no base is refused at exit 2, as `apply`
    refuses one."""
    if not found.get("base"):
        out.write(NO_BASE_SAYS)
        return 2
    write = out.write
    plan = found["plan"]
    specs = len(plan["parsed"]) + len(plan["premodel"])
    write(
        f"released with a spec.md: {specs} work item{plural(specs)}, "
        f"{len(plan['applied'])} to apply\n"
    )
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
    pending = {}
    for work_item_id in plan["applied"]:
        for op in plan["parsed"][work_item_id].ops:
            where = f"section `{op.section}`" if op.section else "a new document"
            pending.setdefault(op.file, []).append(
                f"        {op.kind} {where}  {work_item_id} spec.md:{op.line}"
            )
    if pending:
        write("\npending rule changes, in merge order:\n")
        for file, lines in pending.items():
            write(f"    {file}\n" + "\n".join(lines) + "\n")
    write_outcome(plan, out)
    write_rule_arm(
        found, found["rule"], found["rule_kept"], found["rule_base_kept"], out
    )
    if found["removes"]:
        write(f"\n{REMOVES_HEADING}\n")
        for work_item_id in found["removes"]:
            write(f"    {SPECS}/{work_item_id}/\n")
            for where in found["citations"].get(work_item_id, []):
                write(f"        cited from {where}\n")
        write(f"\n{READERS_HEADING}\n")
        for rel in found["readers"] or ["none under tests/"]:
            write(f"    {rel}\n")
    write(
        "\nNothing was written and nothing was removed; `settle --apply` does both.\n"
    )
    return 0


# --- the apply -------------------------------------------------------------

# The index `--apply` writes when it creates the policy root; `fold-check`
# then names the row each document is owed.
INDEX = (
    "# {policy}\n\nThe index of this policy root: one row per topic, naming "
    "its file.\n\n| File | The question it answers |\n|---|---|\n"
)
AFTER_HEADING = (
    "after applying — the index and the one read, as `fold-check` reads them; "
    "neither\nrefuses anything here:"
)


def write_after(root, policy, out):
    """The index rows owed and the documents past `Document token ceiling`,
    read by `fold_check.py` over what `--apply` wrote. A row it cannot read
    is said in its own sentence, never as a traceback after the writes."""
    fold = load(FOLD_CHECK, "specseal_fold_check_for_settle")
    try:
        ceiling = fold.declared(fold.seal_home(root))[1]
        lines = list(fold.index_problems(root, policy) or [])
        if ceiling is not None:
            lines += fold.past_ceiling_lines(
                fold.past_ceiling(root, policy, ceiling), ceiling
            )
    except fold.Unusable as refused:
        lines = [f"not read: {refused}"]
    if lines:
        out.write(f"\n{AFTER_HEADING}\n" + "".join(f"    {i}\n" for i in lines))


def apply(found, root, out):
    """Write what the replay applies into the policy root, then remove each applied
    directory and each spec-less one the rule arm retires.

    **The candidates are read from the tree again, not taken from `survey`**:
    a classification made for a printed list is not a guard on a destructive
    act. `found` gives *released*, `ref` and the base, which only git answers.
    A `found` with no base is refused at exit 2 before anything is read.

    The documents are written before any directory is removed, so a run cut
    short keeps every spec whose rule it may not have written."""
    base = found.get("base")
    if not base:
        out.write(NO_BASE_SAYS)
        return 2
    reader = load(READER, "specseal_unverified_reader")
    ids = sorted(set(work_items(root)) & set(found["released"]))
    plan = rule_plan(
        root, found["ref"], base, [i for i in ids if has_spec(root, i)], reader
    )
    retired, kept, base_kept = rule_arm(
        root, base, [i for i in ids if not has_spec(root, i)], reader
    )
    policy = reader.policy_root(root)
    if plan["documents"] and not os.path.isdir(under(root, policy)):
        os.makedirs(under(root, policy))
        with open(under(root, f"{policy}/README.md"), "w", encoding="utf-8") as f:
            f.write(INDEX.format(policy=policy))
        out.write(f"wrote {policy}/README.md, the index, with the root\n")
    for rel, text in plan["documents"].items():
        path = under(root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(text)
        out.write(f"wrote {rel}\n")
    for work_item_id in plan["applied"] + retired:
        shutil.rmtree(under(root, f"{SPECS}/{work_item_id}"))
        why = (
            "  (no `spec.md` — retired by the rule)" if work_item_id in retired else ""
        )
        out.write(f"removed {SPECS}/{work_item_id}/{why}\n")
    write_outcome(plan, out)
    write_rule_arm(found, retired, kept, base_kept, out, heading=False)
    if plan["documents"]:
        write_after(root, policy, out)
    applied, removed = len(plan["applied"]), len(plan["applied"]) + len(retired)
    held = len(plan["refused"]) + len(kept) + len(base_kept)
    out.write(
        f"\napplied {applied} spec{plural(applied)} and removed {removed} "
        f"director{plural(removed, 'ies', 'y')}; {held} refused or kept\n"
    )
    return 1 if held else 0


def main(argv=None):
    """The dry run or the apply; the exit code is the verdict."""
    ap = argparse.ArgumentParser(
        prog="settle",
        description="Apply the rule changes released specs state to the policy root.",
    )
    ap.add_argument(
        "--root", default=None, help="repository root (default: the one this is run in)"
    )
    ap.add_argument(
        "--released-at",
        default="origin/main",
        metavar="REF",
        help="the branch a release merges to. A work item is released when "
        "its directory is present there, and a record is asked for open rows "
        "at the merge base of this and HEAD too (default: origin/main)",
    )
    ap.add_argument(
        "--apply",
        action="store_true",
        help="apply each released spec's rule changes to the policy root in merge order, "
        "whole or not at all, and remove each applied directory and each "
        "released one with no spec.md and nothing open",
    )
    args = ap.parse_args(argv)

    root = os.path.abspath(args.root or os.getcwd())
    # The root is resolved through the one resolver, `hooks/optin.py#home_at`,
    # handed the common git directory this also needs for the opt-out sentence.
    optin = load(OPTIN, "specseal_optin")
    common = optin.git_common_dir(root)
    home = optin.home_at(root, common)
    if not home:
        # `home_at` answers "" for no root and for an opt-out; they are two
        # sentences. `isfile`, as `home_at` reads it: a directory of the
        # marker's name is not an opt-out.
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
            "read. This command settles work items, and a repository with "
            "none has nothing to settle.\n"
        )
        return 2
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
    # A settled root is not an unusable one (#517): an empty `seal/specs/`, or
    # none in a fresh checkout of that commit, is where a complete settle ends.
    if not work_items(root):
        sys.stdout.write(SETTLED.format(root=root, specs=SPECS))
        return 0

    found = survey(root, args.released_at)
    if found is None:
        sys.stderr.write(
            f"settle: --released-at {args.released_at} does not resolve in {root} — nothing was "
            "read. Without it every work item reads as unreleased and this "
            "would report nothing to apply, which is the one answer it must "
            "not give by accident.\n"
        )
        return 2
    # #602: with no merge base the predicate would be asked of the working
    # tree alone, so both arms refuse rather than report what `--apply` then
    # refuses.
    if found["base"] is None:
        sys.stderr.write(
            f"settle: --released-at {args.released_at} and HEAD share no commit "
            f"in {root}, or this clone is too shallow to reach the one they "
            "share (`git fetch --unshallow`) — nothing was read. The rule arm "
            "asks whether a record is closed at their merge base, and there is "
            "none to ask.\n"
        )
        return 2
    if args.apply:
        return apply(found, root, out=sys.stdout)
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
