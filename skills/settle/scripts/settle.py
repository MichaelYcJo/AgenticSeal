#!/usr/bin/env python3
"""settle — show the released specs by section, and remove what a settle leaves.

  settle                        the dry run: each group of released specs that
                                name one section, the specs to read whole, every
                                open row, and what `--apply` removes
  settle --apply                remove each released work item directory whose
                                record holds no open row
  settle --released-at REF      what counts as released (default origin/main)
  settle --root DIR             a repository other than this one

**Released means present on the branch the release merges to**, which is why
`--released-at` names a ref rather than a date.

**The specs say what was decided and in what order, the code says what holds
now, and the settling session writes each section as the latest decision the
code bears out. The script reads and removes; it neither writes `docs/` nor
judges.** `skills/settle/SKILL.md` is the settling session's procedure.

**The dry run is the timeline.** Each released spec's `## Rule changes` is
read as `--released-at` holds it, through `rule_changes.py`. The specs whose
operations name one place, a file and a section, are one group, two places
one group where `rule_changes.py#overlapping` says they can name one text, and
each group is listed in merge order (`rule_changes.py#order`). Each operation
carries its spec's coordinate and two facts read from the working tree:
whether its `from` is found in the section, and whether its `to` is. Two specs
in one group whose adding commits no ancestry orders are marked unordered for
the settling session to order by content. A spec whose section does not parse,
or that has none, is listed to read whole. Every open `## Not verified` row of
every released record is listed with the backticked paths it names and
whether each is in the working tree. Nothing is refused or held in the dry
run.

**`--apply` removes, and only that.** It removes every released work item
directory whose record holds no open row in the working tree, whether or not
it wrote a `spec.md`, and prints the rows each removed record closed, with
what closed each. A directory whose record still holds an open row, or one
that cannot be read, is kept and named with its rows. It writes no policy
document: the settling session has written them by then, and `fold-check`'s
lines over the policy root are printed after the removals.

**Local mode is refused rather than reported on.** A root under the common
git directory is never committed, so no ref holds the work item directories
and nothing removed from them could be recovered. `seal mode shared` moves the
root into the tree. A repository that opted out with the scratch marker, an
empty FILE read the way `hooks/optin.py#home_at` reads it, is refused too.

Exit codes: 0 the report was produced, `--apply` kept nothing, or the root
holds no work item, which is the state a complete settle reaches; 1 `--apply`
kept a directory whose record holds an open row or cannot be read; 2 the
arguments or the tree were unusable: a `--released-at` ref that does not
resolve, a root at neither place, a root in local mode, a repository that
opted out, and a sibling script that is not beside it. An interpreter below
the floor never reaches this file through `bin/settle`: `hooks/launch.py`
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
    # exempt from splitlines: git output
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
    "settle: {specs}/ in {root} holds no work item — nothing to show and "
    "nothing to remove. A complete settle ends here, and git keeps no empty "
    "directory, so a fresh checkout of this state has no {specs}/ at all.\n"
)

# The dry run's headings, each pinned by `tests/test_settle.py`.
GROUPS_HEADING = (
    "groups: the released specs whose rule changes name one section, in merge "
    "order.\nThe settling session writes each section as its group's latest "
    "decision, checked\nagainst the code (`skills/settle/SKILL.md`); `from` and "
    "`to` say whether that text\nis in the section now:"
)
UNORDERED = (
    "unordered: {a} and {b}: no ancestry orders the commits that add their "
    "spec.md,\n        so order them by content"
)
WHOLE_HEADING = (
    "to read whole: released specs no group holds, for the settling session "
    "to read\nand write any rule they state the same way:"
)
NO_SECTION = "no `## Rule changes` section"
NOTHING_HEADING = "the no-change block (`- {nothing}`), so no section to write:"
ROWS_HEADING = (
    "open rows: every open `## Not verified` row of every released record, for "
    "the\nsettling session to decide as moot, answered or a measurement to "
    "re-home, and\nclose with `closed` and what closed it:"
)
REMOVES_HEADING = (
    "what `settle --apply` removes: each released directory whose record "
    "holds no open row:"
)
READERS_HEADING = (
    "checks that read `seal/specs` — each owes an answer "
    "(`skills/settle/SKILL.md`\n*Answer every check that reads the corpus*) "
    "before the directories go:"
)


# A backticked span that names a repository path: a `/` in it, or a file
# name with one of the extensions this repository's files carry. What
# follows `#` or `::`, and a `:<line>` range, point inside the file and are
# not part of its path.
SPAN_RE = re.compile(r"`([^`\s]+)`")
FILE_NAME_RE = re.compile(r"[\w.-]+\.(?:py|md|cmd|sh|ps1|yml|yaml|json|toml|txt)")


def named_paths(item):
    """The repository paths an open row's ITEM names in backticks, in order."""
    out = []
    for span in SPAN_RE.findall(item):
        path = re.split(r"#|::", span, maxsplit=1)[0]
        path = re.sub(r":\d+(-\d+)?$", "", path).removeprefix("./")
        if not path or path.startswith(("/", "~", "-")) or "<" in path:
            continue
        if ("/" in path or FILE_NAME_RE.fullmatch(path)) and path not in out:
            out.append(path)
    return out


def tracked_names(root):
    """The base names of every tracked file, so a row naming `spec.md` or
    `broad_gate.py` alone is looked for by name."""
    r = subprocess.run(["git", "-C", root, "ls-files", "-z"], capture_output=True)
    listed = (
        r.stdout.decode("utf-8", "replace").split("\0") if r.returncode == 0 else []
    )
    return {rel.rsplit("/", 1)[-1] for rel in listed if rel}


def in_tree(root, work_item_id, path, names):
    """Whether PATH, as an open row of WORK_ITEM_ID names it, is in the
    working tree: under the root, under the work item's own directory, or,
    for a bare file name, as the name of a tracked file."""
    rel = path.rstrip("/")
    if os.path.exists(under(root, rel)):
        return True
    if os.path.exists(under(root, f"{SPECS}/{work_item_id}/{rel}")):
        return True
    return "/" not in rel and rel in names


def open_rows(root, ids, reader):
    """`[(id, [(file, item, [(path, in the tree)])])]` for each of IDS whose
    record holds an open row in the working tree
    (`unverified_check.py#open_record_rows`)."""
    out, names = [], None
    for work_item_id in ids:
        rows = reader.open_record_rows(root, None, f"{SPECS}/{work_item_id}")
        if not rows:
            continue
        names = tracked_names(root) if names is None else names
        out.append(
            (
                work_item_id,
                [
                    (
                        name,
                        item,
                        [
                            (p, in_tree(root, work_item_id, p, names))
                            for p in named_paths(item)
                        ],
                    )
                    for name, item in rows
                ],
            )
        )
    return out


def facts(root, op, rules):
    """`[(field, found)]` for one operation, read from the working tree:
    whether its `from` and its `to` are in the lines its place spans. Where
    the place is not there, neither is."""
    text = read_text(root, op.file)
    span, _ = rules.section_lines(text, op.section)
    region = ""
    if span:
        lines = rules.reader().gfm_lines(text)
        region = "\n".join(lines[span[0] - 1 : span[1]])
    return [
        (field, bool(span) and bool(rules.pattern(value).search(region)))
        for field, value in (("from", op.old), ("to", op.new))
        if value
    ]


def timeline(root, ref, ids, reader):
    """The released specs IDS as the dry run shows them.

    Each `spec.md` is read as REF holds it, the text that was reviewed and
    released. A spec with operations joins the groups `rule_changes.py#group`
    forms in merge order; one whose section does not parse, or that has
    none, is to be read whole; one holding the no-change block has nothing
    to write; a directory with no `spec.md` states no rule."""
    rules = load(RULES, "specseal_rule_changes")
    policy = reader.policy_root(root)
    parsed, whole, nothing, spec_less = {}, [], [], []
    for work_item_id in ids:
        if not has_spec(root, work_item_id):
            spec_less.append(work_item_id)
            continue
        text = reader.show(root, ref, f"{SPECS}/{work_item_id}/spec.md") or ""
        found = rules.parse(text, policy)
        if found.errors:
            whole.append((work_item_id, *found.errors[0]))
        elif found.ops is None:
            whole.append((work_item_id, 0, NO_SECTION))
        elif not found.ops:
            nothing.append(work_item_id)
        else:
            parsed[work_item_id] = found.ops
    ordered = rules.order(root, ref, list(parsed), SPECS)
    commits = dict(ordered)
    same = rules.overlapping(lambda rel: read_text(root, rel))
    groups = []
    for places, ops in rules.group([(i, parsed[i]) for i, _ in ordered], same):
        members = list(dict.fromkeys(i for i, _ in ops))
        groups.append(
            {
                "places": [
                    (p, *rules.section_lines(read_text(root, p[0]), p[1]))
                    for p in places
                ],
                "ops": [(i, o, facts(root, o, rules)) for i, o in ops],
                "unordered": rules.unordered(root, [(i, commits[i]) for i in members]),
            }
        )
    return {
        "groups": groups,
        "whole": whole,
        "nothing": nothing,
        "spec_less": spec_less,
        "with_rules": len(parsed),
    }


def place_line(p, span, why):
    """A group's place as a person reads it, with its lines or why none."""
    file, section = p
    named = f"{file} section `{section}`" if section else f"{file}, the whole document"
    if span:
        return f"place: {named}, at {file}:{span[0]}-{span[1]}"
    return f"place: {named}: {why} in the working tree"


def op_line(work_item_id, op, found):
    """One operation of a group: its kind, its spec's coordinate and what the
    working tree holds of its texts."""
    where = f"{SPECS}/{work_item_id}/spec.md:{op.line}"
    said = (
        ", ".join(f"{f} {'found' if ok else 'not found'}" for f, ok in found)
        or "the whole section"
    )
    return f"{op.kind}  {work_item_id}  {where}  {said}"


# --- the dry run -----------------------------------------------------------


def survey(root, ref):
    """What the dry run prints, and where `--apply` gets *released*.

    **`--apply` does not take its candidates from here.** It reads the
    directories and the records from the tree again, because a
    classification made for a printed list is not a guard on a destructive
    act. What it takes from here is `released`, which only git answers.

    None where `ref` does not resolve."""
    present = work_items(root)
    on_base = released(root, ref)
    if on_base is None:
        return None
    reader = load(READER, "specseal_unverified_reader")
    ids = [i for i in present if i in on_base]
    found = {
        "ref": ref,
        "released": ids,
        "unreleased": [i for i in present if i not in on_base],
        "timeline": timeline(root, ref, ids, reader),
        "rows": open_rows(root, ids, reader),
        "nothing": reader.NOTHING,
    }
    found["citations"], found["readers"] = citations(root, ids)
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
    """The dry run: the groups, the specs to read whole, the open rows and
    what `--apply` removes. It refuses nothing, so it exits 0."""
    write = out.write
    t = found["timeline"]
    rows = dict(found["rows"])
    count = sum(len(r) for r in rows.values())
    total = len(found["released"])
    write(
        f"released at {ref}: {total} work item{plural(total)}; "
        f"{len(found['unreleased'])} unreleased and untouched\n"
        f"    {t['with_rules']} state rule changes, {len(t['nothing'])} hold the "
        f"no-change block, {len(t['whole'])} to read whole, "
        f"{len(t['spec_less'])} wrote no spec.md\n"
        f"    {len(t['groups'])} group{plural(len(t['groups']))}; {count} open "
        f"row{plural(count)} in {len(rows)} record{plural(len(rows))}\n"
    )
    if t["groups"]:
        write(f"\n{GROUPS_HEADING}\n")
        for n, g in enumerate(t["groups"], 1):
            write(f"\ngroup {n}\n")
            for p, span, why in g["places"]:
                write(f"    {place_line(p, span, why)}\n")
            for k, (work_item_id, op, said) in enumerate(g["ops"], 1):
                write(f"    {k}. {op_line(work_item_id, op, said)}\n")
            for a, b in g["unordered"]:
                write(f"    {UNORDERED.format(a=a, b=b)}\n")
    if t["whole"]:
        write(f"\n{WHOLE_HEADING}\n")
        for work_item_id, line, why in t["whole"]:
            where = f"{SPECS}/{work_item_id}/spec.md" + (f":{line}" if line else "")
            write(f"    {work_item_id}  {where}  {why}\n")
    if t["nothing"]:
        write(f"\n{NOTHING_HEADING.format(nothing=found['nothing'])}\n")
        write("".join(f"    {i}\n" for i in t["nothing"]))
    if t["spec_less"]:
        write("\nno `spec.md`, so no rule stated:\n")
        write("".join(f"    {i}\n" for i in t["spec_less"]))
    if rows:
        write(f"\n{ROWS_HEADING}\n")
        for work_item_id, held in found["rows"]:
            write(f"    {work_item_id}\n")
            for name, item, paths in held:
                write(f"        open in {name}: {item}\n")
                for path, present in paths:
                    there = "in the tree" if present else "not in the tree"
                    write(f"            `{path}` {there}\n")
    if found["released"]:
        write(f"\n{REMOVES_HEADING}\n")
        for work_item_id in found["released"]:
            held = len(rows.get(work_item_id, []))
            when = f"once its {held} open row{plural(held)} close" if held else "now"
            write(f"    {SPECS}/{work_item_id}/  {when}\n")
            for where in found["citations"].get(work_item_id, []):
                write(f"        cited from {where}\n")
        write(f"\n{READERS_HEADING}\n")
        for rel in found["readers"] or ["none under tests/"]:
            write(f"    {rel}\n")
    write(
        "\nNothing was written and nothing was removed. The settling session "
        "writes the\nsections and closes the rows; `settle --apply` removes.\n"
    )
    return 0


# --- the apply -------------------------------------------------------------

AFTER_HEADING = (
    "after the removals — the index and the one read, as `fold-check` reads "
    "them; neither\nrefuses anything here:"
)


def write_after(root, policy, out):
    """The index rows owed and the documents past `Document token ceiling`,
    read by `fold_check.py` over the policy root the settling session wrote.
    A row it cannot read is said in its own sentence, never as a traceback
    after the removals."""
    fold = load(FOLD_CHECK, "specseal_fold_check_for_settle")
    try:
        ceiling = fold.declared(fold.seal_home(root))[0]
        lines = list(fold.index_problems(root, policy) or [])
        if ceiling is not None:
            lines += fold.past_ceiling_lines(
                fold.past_ceiling(root, policy, ceiling), ceiling
            )
    except fold.Unusable as refused:
        lines = [f"not read: {refused}"]
    if lines:
        out.write(f"\n{AFTER_HEADING}\n" + "".join(f"    {i}\n" for i in lines))


def closed_rows(root, directory, reader):
    """`[(item, what closed it)]` for each closed row of DIRECTORY's record
    in the working tree, read by `unverified_check.py#check_text`."""
    text = read_text(root, f"{directory}/{reader.OVERVIEW}")
    if text is None:
        return []
    _, closed, _ = reader.check_text(text)
    return [(item, who) for _, item, who in closed]


def apply(found, root, out):
    """Remove each released directory whose record holds no open row in the
    working tree, printing the rows its record closed, and keep and name
    each one that still holds a row.

    **The candidates are read from the tree again, not taken from `survey`**:
    a classification made for a printed list is not a guard on a destructive
    act. `found` gives *released*, which only git answers."""
    reader = load(READER, "specseal_unverified_reader")
    ids = sorted(set(work_items(root)) & set(found["released"]))
    removed, kept = 0, 0
    for work_item_id in ids:
        directory = f"{SPECS}/{work_item_id}"
        rows = reader.open_record_rows(root, None, directory)
        if rows:
            kept += 1
            out.write(
                f"kept {directory}/: its record holds {len(rows)} open "
                f"row{plural(len(rows))}; close each (`closed` with what closed "
                "it) and run `settle --apply` again\n"
            )
            for name, item in rows:
                out.write(f"    open in {name}: {item}\n")
            continue
        closed = closed_rows(root, directory, reader)
        shutil.rmtree(under(root, directory))
        removed += 1
        out.write(f"removed {directory}/\n")
        for item, who in closed:
            out.write(f"    closed in {reader.OVERVIEW}: {item}\n")
            out.write(f"        what closed it: {who}\n")
    policy = reader.policy_root(root)
    if os.path.isdir(under(root, policy)):
        write_after(root, policy, out)
    out.write(
        f"\nremoved {removed} director{plural(removed, 'ies', 'y')}; kept {kept}, "
        f"each with a row to close\n"
    )
    return 1 if kept else 0


def main(argv=None):
    """The dry run or the apply; the exit code is the verdict."""
    ap = argparse.ArgumentParser(
        prog="settle",
        description="Show the released specs' rule changes by section, and "
        "remove released work item directories.",
    )
    ap.add_argument(
        "--root", default=None, help="repository root (default: the one this is run in)"
    )
    ap.add_argument(
        "--released-at",
        default="origin/main",
        metavar="REF",
        help="the branch a release merges to. A work item is released when "
        "its directory is present there (default: origin/main)",
    )
    ap.add_argument(
        "--apply",
        action="store_true",
        help="remove each released work item directory whose record holds no "
        "open row in the working tree, and name each one kept",
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
            "would report nothing to settle, which is the one answer it must "
            "not give by accident.\n"
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
