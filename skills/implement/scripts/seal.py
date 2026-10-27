#!/usr/bin/env python3
"""The root this plugin maintains: where it lives, and how a copy travels.

Three subcommands over one directory. `mode` says which of the two places
the root is at and moves it between them; `export` and `import` carry a copy
of it to another clone. A fourth, `pr-checks`, writes and removes the
workflow that checks pull requests against the committed root.

In local mode the work-item records live under the common git directory, so a new machine or a re-clone starts with nothing and CI's checks
cannot run. That is the mode's whole trade-off
(`docs/one-root-by-lifetime.md`, "Shared or local"), and without a way to
carry a copy it reads as *lose it* rather than *take a copy*. This is that
way:

  seal export                 write the root to a zip beside the clone
  seal export --check         the release reminder; writes nothing
  seal import <zip>           merge a zip's records in, overwriting nothing

Switching between the two modes was two shell lines in `README.md` that a
person had to find, and a repository arriving from the 0.3.x layout was
never asked which mode it wanted (#104). `seal mode` is that section made
runnable, and the section on the mode below this one is its reasoning:

  seal mode                   the folder, the row, and whether they agree
  seal mode --check           the same, writing nothing; exit 1 when they
                              disagree. This is what CI runs
  seal mode local|shared      switch, and write the row
  seal mode --apply           switch to whatever the row says

The switch moves the root and nothing else. Whether CI checks pull requests
is a second answer, and its record is the workflow file itself, so no row
says it (#952):

  seal pr-checks              whether .github/workflows/hygiene.yml is this
                              plugin's, and the release it pins; writes nothing
  seal pr-checks install      write it pinned to this release, and stage it;
                              refused unless seal/ is in the tree
  seal pr-checks remove       take out the file this plugin wrote, from the
                              working tree and the index; where HEAD carries
                              it, the deletion is staged for you to commit

One more subcommand records a fact about the session rather than the root:

  seal no-work-item           this session's change on the branch checked
                              out here belongs to no work item, so the edit
                              check lets its edits on that branch through

Every other command of the plugin is a subcommand of this one, and `TOOLS`
says which script each runs. `seal gate --base <base> --record <item>` hands
`--base <base> --record <item>` to `broad_gate.py` untouched, `--help` among
any arguments, so each script keeps its own parser and its own help, and a
subcommand is a dispatch and not a copy (#1051).

**The root is its own directory, and that is what makes the export safe.**
Beside it under the git directory sit the crafter mark, the worktree choices,
the review and parity marks, the throwaway opt-out, any lease file and this
command's own state. None of that belongs to another machine, and none of it
is in the zip — not because a list is maintained here, but because the export
walks the root and nothing else. A symbolic link inside the root is the one
way back out, so links are skipped and named rather than followed.

**A zip is untrusted input**, and `ZipFile.extractall` is not used on it.
What that buys is narrower than the usual telling, so it is written down
measured rather than repeated: on the CPython this ships on (3.12 to 3.14,
checked 2026-09-03) `extractall` already strips `..` and a leading `/` from a
member's name, and writes a link entry as an ordinary file. It is **not** a
path-traversal sink there.

What actually disqualifies it, in order:

  1. **it overwrites**, which is the one rule this command exists to keep;
  2. it writes members this format has no place for — a name like
     `a\\..\\..\\b.md` lands in the root as a literal file on POSIX;
  3. it follows a symbolic link that is already a directory in the
     destination, and so would a plain `open()`. That one is real and is
     checked for by `linked_path` below.

So every member's name is checked first, one bad member refuses the whole
archive before a byte is written, and each file is written at a path built
from segments this module produced. The name checks are defence that does not
depend on the standard library's sanitiser staying what it is today.

**Import never overwrites and never asks.** A path that is not there is
added. A path that is there with the same bytes is left alone. A path that is
there with different bytes gets the incoming copy beside it as
`<name>.incoming<ext>` — `threads/<id>/frame/design.incoming.md` beside
`threads/<id>/frame/design.md` — and the collision is reported. A copy is not a sync: which
of the two files is right is a judgement the person makes by reading them,
and there is no answer this command could give that would not sometimes throw
work away.

**What the reminder counts, and what it does not.** `--check` prints
`N work items changed since the last export`, where a work item is
its directory `specs/<id>/`. Root-level files — `follow-up.md`, `config.md`,
`parity.md` — are NOT counted, because the line
the design specifies says *work items* and this command does not get to widen
it. So a release whose only change was to `follow-up.md` reports 0. That gap
is Q1 in the work item's `questions.md`, with the owner named; it is written
here as well because this docstring is where the next reader meets the count.

Exit codes: 0 done · 1 nothing was written, and the message says why · 2 a
file this command loads from `hooks/` is not there, so nothing was read, or
the arguments were unusable (argparse's usage error, and any two of a mode,
`--check` and `--apply` given together). Every refusal here names the file,
the path, or the flag that gets past it.
"""

import argparse
import datetime
import errno
import hashlib
import json
import os
import re
import subprocess
import sys
import zipfile

HOOKS = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "hooks"
)
PLUGIN = os.path.normpath(os.path.join(HOOKS, ".."))

# The plugin's commands that are not about the root, one subcommand each: the
# name a person types, the script it runs (from the plugin's root), and the
# line `seal --help` prints for it.
TOOLS = {
    "gate": (
        "skills/verify/scripts/broad_gate.py",
        "the one broad run, taken once after the review rounds settle",
    ),
    "settle": (
        "skills/settle/scripts/settle.py",
        "show the released specs by section, and remove what a settle leaves",
    ),
    "cost": (
        "skills/verify/scripts/session_cost.py",
        "where a session's minutes went, read from its transcript",
    ),
    "mutate": (
        "skills/verify/scripts/mutation_check.py",
        "break one unit, run its cases, and say whether one went red",
    ),
    "unverified": (
        "skills/verify/scripts/unverified_check.py",
        "read what the work items recorded as not verified",
    ),
    "arms": (
        "skills/verify/scripts/arm_check.py",
        "list a module's arms, and report the ones no case kills",
    ),
    "deferrals": (
        "skills/verify/scripts/deferral_check.py",
        "resolve the answerer named in an `unverified` row",
    ),
    "fold": (
        "skills/settle/scripts/fold_check.py",
        "hold the policy root's documents to one read and one index",
    ),
    "pact": (
        "skills/verify/scripts/pact_check.py",
        "whether every signer still agrees with the pact",
    ),
    "payload": (
        "skills/verify/scripts/payload_meter.py",
        "what each agent's startup payload is made of, and its cost in tokens",
    ),
    "stamp": (
        "skills/verify/scripts/seal_stamp.py",
        "draw the sealer's stamp",
    ),
    "layout": (
        "skills/verify/scripts/test_layout.py",
        "whether each test file stands where the test layout puts it",
    ),
    "rules": (
        ".github/scripts/rules.py",
        "a document's sections with what their tests guard, or every check line read",
    ),
}

# What each module this command imports from `hooks/` is for, in the sentence
# printed when it is missing. They are checked before the `import` lines,
# because a plain `import` of an absent module dies with a
# `ModuleNotFoundError` traceback at exit 1 (#610) -- and a search for
# by-path loaders cannot see this shape, which is how #590 missed it.
HOOK_PURPOSES = {
    "config.py": "it is what reads the root's config.md, whose Mode row this "
    "command keeps",
    "optin.py": "it is what finds the repository's seal/ root",
    # `config.py` imports it, so a `hooks/` without it fails that import.
    "blocks.py": "it is the walk config.py reads config.md through, which "
    "tells a live row from one quoted in a fence or parked in a comment",
    "routing.py": "it is what writes the record `seal no-work-item` leaves, "
    "which the edit check reads",
    "hooksession.py": "it names the variable a session's id is read from",
}


def refuse_without_hooks(hooks=HOOKS):
    """Exit 2 with one sentence per `HOOK_PURPOSES` module absent from
    `hooks`, naming its path and what it is for; return where all are there.

    2 and not 1, because 1 here means *nothing was written* about a root this
    command read, and a missing sibling means nothing was read at all. A
    `SystemExit` carrying a string exits 1, so the sentences go to stderr and
    the code is the int -- the shape `settle.py#load` has."""
    missing = [
        name for name in HOOK_PURPOSES if not os.path.isfile(os.path.join(hooks, name))
    ]
    if not missing:
        return
    for name in missing:
        sys.stderr.write(
            f"seal: cannot read {os.path.join(hooks, name)}, and "
            f"{HOOK_PURPOSES[name]}.\n"
        )
    sys.stderr.write(
        "This command ships under `skills/`, in the plugin that holds "
        "`hooks/`; a copy of one script taken on its own is not a plugin. "
        "Nothing was read.\n"
    )
    raise SystemExit(2)


refuse_without_hooks()
sys.path.insert(0, HOOKS)
import config as repo_config  # noqa: E402
import hooksession  # noqa: E402
import optin  # noqa: E402
import routing  # noqa: E402

# The manifest's shape. An import refuses a number it does not know rather
# than guessing at fields: a zip whose fields moved, read by a build that
# assumes the old ones, merges records at the wrong paths — and that merge is
# the operation this command exists to make safe.
FORMAT = 1
MANIFEST = "manifest.json"

# Machine-local state, beside the root with everything else that must never
# leave this clone. Inside the root it would ride into the next zip and, in
# shared mode, into a commit.
STATE = "agentic-last-export.json"

UNSAFE_IN_A_NAME = re.compile(r"[^A-Za-z0-9._-]")
DRIVE = re.compile(r"^[A-Za-z]:")

ADDED, IDENTICAL, COLLIDED = "added", "identical", "collided"

# A record is markdown, and `write_members` reads each member whole. The zip
# arrives from another machine, so its declared sizes are the sender's choice
# rather than this root's honest contents: measured 2026-09-03, a 408 KB zip
# declaring 400 MB in one member wrote 419 MB and added as much to memory in
# 0.2 s. All three limits are read before a byte is written.
MEMBER_LIMIT = 32 * 1024 * 1024
ARCHIVE_LIMIT = 512 * 1024 * 1024
# The other axis. A member declaring zero bytes passes the member limit and
# adds nothing to the total, so neither byte bound sees a zip that is only a
# count: measured 2026-09-03, a 31 MB zip of 300,000 empty members wrote
# 300,002 files into the root at exit 0, in 34.5 s. A root of records is one
# directory per work item.
MEMBER_COUNT_LIMIT = 20_000


# --- git, asked the way `hooks/optin.py` asks it ----------------------------


def git_asked(root, *args, answered=(0,)):
    """(`git -C root <args>` stdout stripped, "") — or (None, why).

    **The one place that can say why**, which is what separates *there is no
    remote* from *the question could not be answered*. `porcelain`, `tracked`
    and `gitlinks_under_root` each grew this shape for themselves; this is it
    promoted, so a fourth spelling is not what a caller needing the
    distinction has to write. `git()` below is this function with the
    distinction thrown away — the right reading for a caller that has nothing
    to do with `why`, and the wrong one for a caller that reads "" as a FACT
    about the repository. #111 found four call sites doing the second, one of
    which switched off `seal import`'s refusal.

    `answered` is the return codes that count as an answer, because for one
    command a non-zero code IS one: `git config --get` exits 1 when the key is
    not set. Every other caller leaves it at `(0,)`.

    Encoding named for the reason `optin.repo_root` names it: `text=True`
    alone decodes with the parent's locale, git answers UTF-8, and a
    repository under a path this locale cannot decode kills subprocess's
    reader thread without the exception propagating.
    """
    named = f"git {args[0]}" if args else "git"
    try:
        done = subprocess.run(
            ["git", "-C", root, *args],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=15,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return None, f"{named} could not be run ({exc})"
    # The return code, not the output alone. `git rev-parse HEAD` on a branch
    # with no commit yet exits 128 and still prints `HEAD`, which the manifest
    # would record as this export's SHA (measured 2026-09-03).
    if done.returncode not in answered:
        return None, (done.stderr or "").strip() or (
            f"{named} exited {done.returncode}"
        )
    return (done.stdout or "").strip(), ""


def git(root, *args):
    """`git -C root <args>` stdout, stripped, or "" for any failure.

    For the callers that are right not to care why one is the same as the
    other. A caller that would read "" as a fact about the repository wants
    `git_asked` instead — see its docstring, and `other_worktrees` for the one
    call site here that reads "" as a fact and is right to.
    """
    text, _ = git_asked(root, *args)
    return text or ""


def remote_url(root):
    """(`origin`'s fetch URL, "") — or (None, why) when git could not answer.

    `""` is a repository with no `origin`, and that is an ANSWER: it is the
    case `seal import`'s other-repository check is allowed to be switched off
    by, so it has to be tellable from a failure.

    **`git config --get` exits 1 with nothing on either stream when the key is
    not set**, so this is the one command here whose exit 1 is an answer
    (measured 2026-09-07 against git 2.50.1: unset gives `(1, '', '')` and a
    `.git/config` git cannot parse gives `(128, '', 'fatal: bad config line
    9 …')`). Two other states exit 1 with both streams empty, so **exit 1 is
    an answer only for a caller whose `root` git has already resolved**:
    `error: key does not contain a section`, which a literal well-formed key
    cannot reach, and a `root` that is not a repository at all, which is
    indistinguishable from an unset key. `repo` here comes from `resolve`,
    which is `optin.repo_root(cwd)` — a path git itself resolved one command
    earlier — and `import_` returns before this call when that is empty. A
    later caller reaching for `answered=(0, 1)` has to be able to say the
    same.

    `--default ""` would collapse the unset case into exit 0 and remove the
    special case. It is not used: it arrived in git 2.18 and nothing else this
    plugin runs needs a git that new, so leaning on it would turn an old git
    into a refusal on a path that works today.
    """
    return git_asked(root, "config", "--get", "remote.origin.url", answered=(0, 1))


def head_sha(root):
    """(the HEAD SHA, "") — or (None, why) when git could not answer.

    There is no empty answer. `git rev-parse HEAD` prints a SHA whenever it
    succeeds and exits 128 on a branch with no commit yet — printing `HEAD`,
    which is what #81's round 1 measured reaching the manifest as an export's
    SHA. So a repository with no commit is *unanswered* here, and the manifest
    leaves the field out rather than writing a string that is not a SHA.
    """
    return git_asked(root, "rev-parse", "HEAD")


# Moved to `hooks/config.py` (#647), where the `Pact` reader needs it and
# cannot import this file; the alias keeps one normaliser under the name every
# caller here already spells, as the config aliases below do.
normalise_remote = repo_config.normalise_remote


# --- the root, and the one walk everything reads it through -----------------


def resolve(cwd):
    """(repository root, root in force, shared path, local path, mode).

    Every path comes from `optin`: `home_at` says which root is in force and
    `home_paths` says where each mode's root would be, so nothing here spells
    `<repo>/seal` or `.git/seal` for itself.
    """
    repo = optin.repo_root(cwd)
    if not repo:
        return "", "", "", "", ""
    shared, local = optin.home_paths(repo)
    home = optin.home_at(repo)
    mode = "shared" if home and home == shared else "local" if home else ""
    return repo, home, shared, local, mode


def root_files(home):
    """([(relative path, disk path)], [skipped link]) for the whole root.

    Relative paths are `/`-joined on every platform, because they go into a
    zip that another machine reads. Both lists are sorted, so the same tree
    always produces the same zip and the same digest.

    **This is the only walk.** The zip's members and the digests the manifest
    records come from this one list. `tests/test_seal.py::Test_export`
    asserts the zip's namelist equal to `MEMBERS`, the manifest and then the
    sorted paths this walk gives for the case's root, and
    `Test_root_files` holds the walk's order. Two enumerations would
    drift at the seam — the manifest recording what one of them saw while the
    reminder compares against what the other sees — and the difference would
    read as a work item somebody changed.

    Symbolic links are excluded here rather than at the zip, so they are
    absent from the members and from the digest together. Excluding them in
    one place only would make every export of a repository holding one report
    a change that nothing made. `os.walk` does not descend into a linked
    directory by default; it is pruned as well so the exclusion is a decision
    in this function rather than a default somewhere else.
    """
    files, links = [], []

    def relative(path):
        return os.path.relpath(path, home).replace(os.sep, "/")

    for dirpath, dirnames, filenames in os.walk(home):
        linked = [d for d in dirnames if os.path.islink(os.path.join(dirpath, d))]
        for name in linked:
            links.append(relative(os.path.join(dirpath, name)) + "/")
        dirnames[:] = sorted(d for d in dirnames if d not in linked)
        for name in sorted(filenames):
            path = os.path.join(dirpath, name)
            if os.path.islink(path):
                links.append(relative(path))
            else:
                files.append((relative(path), path))
    return sorted(files), sorted(links)


def read_bytes(path):
    with open(path, "rb") as handle:
        return handle.read()


def digest(entries):
    """SHA-256 over a sorted [(relative path, disk path)].

    The path, a NUL, the byte length, a NUL, the bytes — so a file renamed to
    another file's name, or two files whose contents swap, change the digest.
    Hashing the concatenated contents alone would not.
    """
    running = hashlib.sha256()
    for rel, path in entries:
        data = read_bytes(path)
        running.update(rel.encode("utf-8"))
        running.update(b"\0")
        running.update(str(len(data)).encode("ascii"))
        running.update(b"\0")
        running.update(data)
    return running.hexdigest()


def work_item_of(rel):
    """The work item a root-relative path belongs to, or "".

    A work item writes in one place, its directory under `threads/`.
    """
    parts = rel.split("/")
    if len(parts) >= 3 and parts[0] == optin.WORK_ITEMS:
        return parts[1]
    return ""


def work_item_digests(files):
    """{work item id: digest}, built from the list the zip is built from."""
    groups = {}
    for rel, path in files:
        item = work_item_of(rel)
        if item:
            groups.setdefault(item, []).append((rel, path))
    return {item: digest(sorted(entries)) for item, entries in groups.items()}


# --- export -----------------------------------------------------------------


def manifest_of(repo, mode, files):
    """(the manifest, what git could not answer), a field LEFT OUT for each.

    Absent and empty are different facts, and `remote` needs all three states:
    a URL, `""` for a repository with no `origin`, and absent for a question
    that went unanswered. Freezing `""` in for the third switched off the
    receiving machine's own refusal (#111) — an export cannot ask the importer
    to tell two facts apart while writing one string for both.

    `head` has no empty state at all. `git rev-parse HEAD` prints a SHA
    whenever it succeeds, so present here means a SHA was read, and a
    repository with no commit leaves the field out.

    **The reasons come back rather than being dropped.** An omitted `remote`
    is refused on arrival, and the machine running THIS command is the only
    one that can clear the failure by running it again — so an export that
    said nothing left the diagnosis on the machine that cannot act on it.

    They come back KEYED BY FIELD, because only `remote` is refused on
    arrival. A caller handed a flat list has to match on the sentences to
    tell which field went unread, and the first cut of this did not try:
    it printed *the other machine takes in without a flag* for an export
    that had read the remote and only missed the HEAD SHA, promising a fix
    for a refusal that was never going to happen.

    The format number does not move for this. No field was renamed or
    repurposed, and format 1's only reader of these two already goes through
    `manifest.get`.
    """
    manifest = {
        "format": FORMAT,
        "mode": mode,
        "exported_at": datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        "items": work_item_digests(files),
    }
    unread = {}
    url, why = remote_url(repo)
    if url is not None:
        manifest["remote"] = url
    else:
        unread["remote"] = f"the remote was left out — {why}"
    # `is not None`, the same test as the line above. `if head` behaves
    # identically today — `head_sha`'s docstring argues there is no empty
    # answer — but it is the spelling that would silently drop a legitimate
    # empty one, and two spellings of one question five lines apart is what
    # sent a reader looking for a difference that is not there.
    head, head_why = head_sha(repo)
    if head is not None:
        manifest["head"] = head
    else:
        unread["head"] = f"the HEAD SHA was left out — {head_why}"
    return manifest, unread


def unused(directory, stem, suffix):
    """`<stem><suffix>`, then `<stem>-2<suffix>`, … — the first free path.

    The zip's name goes through this. (`place` has its own chain for the
    `.incoming` siblings, because it also compares bytes — this docstring used
    to claim both went through here, and a fix to one therefore missed the
    other.) The cap is a refusal to spin rather than a limit anyone should
    reach.

    `lexists`, for the reason `place` uses it: a symbolic link to nothing
    reads as absent to `exists`, so this returned a name somebody had made a
    link, and `os.replace` then removed it.
    """
    for n in range(1, 1000):
        tail = suffix if n == 1 else f"-{n}{suffix}"
        path = os.path.join(directory, stem + tail)
        if not os.path.lexists(path):
            return path
    return ""


def zip_stem(repo, when):
    """`seal-<repo>-<date>` — the name a person recognises on a USB stick."""
    base = UNSAFE_IN_A_NAME.sub("-", os.path.basename(repo.rstrip(os.sep))) or "repo"
    return f"seal-{base}-{when}"


def write_zip(path, home, files, manifest):
    """The zip, written to a temporary name and renamed once it is complete.

    A failed write leaves no half archive for someone to carry away and
    discover on the machine that has nothing else.

    `lexists` and then `O_EXCL`, in that order and for two different reasons.
    This name is predictable — `seal-<repo>-<date>.zip.partial`, beside the
    clone, which is where the default export writes — and a broken link
    planted there put the manifest and every record outside the clone at exit
    0, printing `wrote <path>` for a path that was the link (measured
    2026-09-03).

    `lexists` is the check: a link to nothing reads as absent to `exists`, so
    only the l-form sees it. `O_EXCL` is the backstop for the moment between
    the check and the open — **on POSIX**, where the kernel refuses to satisfy
    it through a symbolic link. It does not carry that meaning on Windows:
    CI's windows leg wrote the manifest and every record through a broken link
    at this name, at exit 0, with `O_EXCL` set and nothing else in front of it
    (run 33715420379, 2026-09-03). Seven review rounds and the broad gate all
    ran on macOS and none of them could see it.

    So the check is the defence on every platform and the flag narrows the
    race on one. The race stays open on Windows, recorded rather than closed:
    there is no portable open that refuses a reparse point.
    """
    partial = path + ".partial"
    # The check and the open sit OUTSIDE the try. A name this call did not
    # create is not this call's to remove, and the cleanup below exists so a
    # failed write leaves no half archive — a `.partial` that was already
    # there is not one. Round 3 graded `os.replace` removing a link at the
    # zip's own name; this was that same removal one name over, and it took a
    # concurrent export's in-flight temporary file too.
    if os.path.lexists(partial):
        raise FileExistsError(errno.EEXIST, os.strerror(errno.EEXIST), partial)
    opened = os.open(partial, os.O_RDWR | os.O_CREAT | os.O_EXCL, 0o666)
    try:
        with (
            os.fdopen(opened, "w+b") as raw,
            zipfile.ZipFile(raw, "w", zipfile.ZIP_DEFLATED) as archive,
        ):
            archive.writestr(MANIFEST, json.dumps(manifest, indent=2, sort_keys=True))
            for rel, disk in files:
                archive.write(disk, f"{optin.HOME}/{rel}")
        os.replace(partial, path)
    except BaseException:
        try:
            os.remove(partial)
        except OSError:
            pass
        raise


def export(args, cwd):
    repo, home, shared, local, mode = resolve(cwd)
    if not home:
        return no_root(repo, shared, local)

    if mode == "shared":
        print(
            f"shared mode: the records are committed at {display(repo, shared)}/, "
            "so every clone and CI already have them."
        )
        print(
            "A zip would be a second copy of what git carries, and nothing "
            "would keep it current — so none was written."
        )
        print(
            "\nTo switch this repository to local mode, from the repository "
            "root:\n"
            '  git rm -r --cached "$(git rev-parse --show-toplevel)/seal"\n'
            '  mv "$(git rev-parse --show-toplevel)/seal" '
            '"$(git rev-parse --git-common-dir)/seal"\n'
            "then commit the removal."
        )
        return 1

    files, links = root_files(home)
    when = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    stem = zip_stem(repo, when)

    if args.output:
        target = os.path.abspath(args.output)
        if os.path.isdir(target):
            target = unused(target, stem, ".zip")
        directory = os.path.dirname(target) or "."
        if inside(repo, target):
            print(
                f"note: {target} is inside the working tree, so `git add -A` "
                "can commit it — which is what local mode keeps the records "
                "out of the tree to avoid."
            )
    else:
        # Beside the clone, never in it. The normal place to run this is the
        # repository root, and an untracked zip there is one `git add -A` away
        # from committing the records local mode exists to keep out of the tree.
        directory = os.path.dirname(repo.rstrip(os.sep)) or "."
        target = unused(directory, stem, ".zip")

    if not target:
        print(f"no free name for {stem}*.zip in {directory} — pass --output")
        return 1
    if not os.path.isdir(directory):
        print(f"{directory} is not a directory — pass --output somewhere that is")
        return 1

    manifest, unread = manifest_of(repo, mode, files)
    try:
        write_zip(target, home, files, manifest)
    except OSError as exc:
        print(f"the zip could not be written to {target}: {exc}")
        return 1

    write_state(repo, manifest)
    print(f"wrote {target}")
    print(
        f"  {plural(len(files), 'file')} from {display(repo, home)}, "
        f"{plural(len(manifest['items']), 'work item')}"
    )
    for rel in links:
        print(
            f"  skipped the symbolic link {optin.HOME}/{rel} — links are not followed"
        )
    for line in unread.values():
        print(f"  {line}")
    if "remote" in unread:
        # Named here because this is the machine that can fix it. `seal
        # import` refuses a zip recording no remote, and re-running the
        # import there cannot change what these bytes say — so an export that
        # exits 0 in silence leaves the diagnosis with the person who has no
        # way to act on it.
        #
        # `remote` alone, because `remote` alone is refused on arrival. A
        # missing `head` costs the importing machine one line of its closing
        # summary and no flag, so promising this for it names a refusal that
        # never comes.
        print(
            "  Running this again once git answers writes a zip the other "
            "machine takes in without a flag."
        )
    print(
        f"\nTake it in on the other machine with:\n  seal import {os.path.basename(target)}"
    )
    return 0


# --- shared plumbing --------------------------------------------------------


def plural(count, noun):
    """`1 file` · `2 files`.

    `check()` does NOT use this. Its line is quoted text — the design and the
    issue's done-when list both write `N work items changed since the last
    export` — so it stays that, and at N=1 it reads `1 work items`. Reading
    the quoted line as a template with a grammar rule attached is a change to
    an acceptance criterion, which is not this command's to make; the work
    item's `gaps.md` records it where the owner can overturn it.
    """
    return f"{count} {noun}" if count == 1 else f"{count} {noun}s"


def display(repo, path):
    """A path as the reader recognises it: relative to the repository and
    `/`-joined where it is inside, absolute where it is not."""
    if not path:
        return ""
    if inside(repo, path):
        return os.path.relpath(path, repo).replace(os.sep, "/")
    return path


def inside(repo, path):
    """Whether `path` is inside the repository's working tree.

    `commonpath` rather than `startswith`, which reads `/repo-2/x` as being
    inside `/repo`. The git directory of a main worktree is inside the tree by
    this test, and that is correct: nothing here asks the question about it.
    """
    try:
        return os.path.commonpath(
            [os.path.abspath(repo), os.path.abspath(path)]
        ) == os.path.abspath(repo)
    except ValueError:  # different drives on Windows
        return False


def earlier_root():
    """The line every subcommand says where `<repo>/seal/` is an earlier
    release's root (`optin.earlier`), waiting for the session-start move: it
    is neither opted in nor a project's own, so nothing is written beside it
    and first setup is not what it needs."""
    return (
        f"{optin.HOME}/ is this plugin's root from a release before the rename, "
        "waiting for the move a session start makes. Commit the work in "
        "progress under it and start a new session, and the move runs. "
        "Nothing was written."
    )


def no_root(repo, shared, local):
    if not repo:
        print("not inside a git repository — seal works on a clone")
        return 1
    if optin.git_common_dir(repo) and os.path.isfile(
        os.path.join(optin.git_common_dir(repo), optin.SCRATCH)
    ):
        print(
            f"this repository is marked throwaway "
            f"({optin.SCRATCH} under the common git directory), so every gate "
            "reads it as one that never opted in. Remove the marker to work "
            "with its records."
        )
        return 1
    if optin.earlier(shared):
        print(earlier_root())
        return 1
    # Not "nothing to carry": `seal mode` reaches this too, and it carries
    # nothing anywhere. What all three subcommands share is that the root is
    # what they work on, and it is looked for at exactly two places.
    print("no seal/ here, so there is nothing to work with. It is looked for at:")
    print(f"  {shared}   (shared mode)")
    print(f"  {local}   (local mode)")
    print(
        "\nThe first time your session works in a repository it asks which one, "
        "and creates it."
    )
    return 1


def state_path(repo):
    common = optin.git_common_dir(repo)
    return os.path.join(common, STATE) if common else ""


def write_state(repo, manifest):
    """Record the manifest of this export, after the zip is on disk.

    Written even when `--output` sent the zip somewhere unusual: an export
    happened, and the reminder measures against the last one wherever it went.
    """
    path = state_path(repo)
    if not path:
        return
    try:
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(manifest, handle, indent=2, sort_keys=True)
    except OSError:
        # The zip is written and the export succeeded. A reminder that cannot
        # remember costs one over-count at the next release; failing the
        # export here would cost the copy.
        pass


def read_state(repo):
    path = state_path(repo)
    if not path or not os.path.isfile(path):
        return None
    try:
        with open(path, encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, ValueError):
        return None


# --- import -----------------------------------------------------------------


def unsafe(info):
    """Why this zip member may not be written, or "" when it may.

    Checked before anything is written, and one bad member refuses the whole
    archive: a partial import from a hostile zip is still a decision the zip
    made, and the person is then holding records they believe are a copy and
    cannot say of what.

    Some of these `extractall` would also have handled — it strips `..` and a
    leading `/` on today's CPython (the module docstring measures it). They
    are checked here anyway, because a defence that holds only while a
    standard-library sanitiser keeps its current shape is not one this file
    can claim, and because a refusal says what happened where a silent
    sanitise leaves a name nobody chose.

    What is refused, and why each one:

      - a backslash anywhere. A zip stores `/`-separated names (APPNOTE
        4.4.17), so a `\\` is a literal character on POSIX and a separator on
        Windows. `a\\..\\..\\b` is inert on one platform and an escape on the
        other, and a name that means two things is refused on both;
      - an absolute name, or one starting with a drive letter;
      - any `..` segment, which is the escape itself;
      - a NUL, which truncates the path at the C boundary underneath. Kept
        as a guard rather than a claim: `zipfile` cuts the name at the NUL
        before this reads it (measured 2026-09-03), so such a member arrives
        under a shortened name inside the root rather than being refused;
      - a symbolic link entry. A link written into the root is a way to reach
        outside it on the NEXT export, which is the loop this closes;
      - anything not under `seal/` and not the manifest. A member this build
        has no place for is a zip it does not understand, and writing the
        parts it does understand is guessing.
    """
    name = info.filename
    if not name:
        return "a member with no name"
    if "\\" in name:
        return f"{name!r} holds a backslash, which is a separator on one platform only"
    if name.startswith("/") or DRIVE.match(name):
        return f"{name!r} is an absolute path"
    if "\0" in name:
        return f"{name!r} holds a NUL"
    parts = [p for p in name.split("/") if p]
    if any(p == ".." for p in parts):
        return f"{name!r} climbs out of the root with `..`"
    if (info.external_attr >> 16) & 0o170000 == 0o120000:
        return f"{name!r} is a symbolic link"
    if name == MANIFEST or name.rstrip("/") == MANIFEST:
        # The manifest is exempt from the NAME checks — it is the one member
        # that is not a record. Its size is checked in `import_`, which has to
        # know it before reading the manifest and therefore before this runs.
        return ""
    if not parts or parts[0] != optin.HOME:
        return f"{name!r} is not under {optin.HOME}/ and is not the manifest"
    if info.file_size > MEMBER_LIMIT:
        return (
            f"{name!r} declares {info.file_size} bytes, more than the "
            f"{MEMBER_LIMIT} one record may hold"
        )
    return ""


def linked_path(into, archive):
    """A path inside the root that is a symbolic link, or "".

    This is the way a member can still land outside the root, and it is
    measured rather than assumed. `extractall` on the CPython this ships on
    (3.12 to 3.14, checked 2026-09-03) strips `..` and a leading `/` from a
    member's name and writes a link entry as an ordinary file, so those are
    not what a member can escape through. A path in the DESTINATION that is a
    symbolic link is: `extractall` follows it, and so does the plain `open()`
    this module writes with. `seal/threads` pointed elsewhere puts every work
    item there.

    The leaf counts, not only the directories above it. A link named
    `threads/w1/frame/design.md` whose target does not exist reads as absent to
    `os.path.exists`, so `place` calls the member ADDED and `open(target,
    "wb")` follows the link and writes outside the root — measured
    2026-09-03, exit 0 with no warning. A link whose target does exist is
    caught by the byte comparison instead and lands as `.incoming`, which is
    why only the broken one leaked.

    So it is refused before anything is written, and the whole import is
    refused rather than the member: the link is this clone's own state, not
    the zip's, and a person who removes it gets a complete copy on the next
    run instead of a partial one now.

    A link this command created is not possible — the export skips links and
    an import refuses a link member — so reaching this means someone made one
    by hand, which is exactly when a stop is worth more than a guess.
    """
    seen = set()
    for info in archive.infolist():
        parts = [p for p in info.filename.split("/") if p][1:]
        for depth in range(1, len(parts) + 1):
            prefix = tuple(parts[:depth])
            if prefix in seen:
                continue
            seen.add(prefix)
            if os.path.islink(os.path.join(into, *prefix)):
                return "/".join(prefix)
    return ""


def blocked_path(into, archive):
    """A path a member needs as a directory that is already a file, or "".

    `write_members` calls `os.makedirs(exist_ok=True)`, which raises
    `FileExistsError` when the name exists and is not a directory — uncaught,
    mid-write, with the records before it already on disk. Measured
    2026-09-03: a zip holding `seal/a` and `seal/a/b.md` left two records
    written, lost the one after them, and printed a traceback with no line of
    this command's own.

    Both the zip's own members and what the root already holds, because the
    clash comes from either side. Refused whole, like every other refusal
    here, and for the same reason: a partial copy is the thing this command
    exists not to leave.
    """
    members = set()
    for info in archive.infolist():
        parts = [p for p in info.filename.split("/") if p][1:]
        if info.is_dir() or not parts:
            continue
        members.add(tuple(parts))
    for parts in sorted(members):
        for depth in range(1, len(parts)):
            prefix = tuple(parts[:depth])
            here = os.path.join(into, *prefix)
            # `isfile` is not the question `makedirs` answers. It is False for
            # a FIFO, a socket and a device node, and `makedirs(exist_ok=True)`
            # raises on all three — measured 2026-09-03, a FIFO at `seal/a`
            # left one record on disk and lost the rest. `lexists and not
            # isdir` is the condition `makedirs` itself checks.
            if prefix in members or (os.path.lexists(here) and not os.path.isdir(here)):
                return "/".join(prefix)
    return ""


def read_manifest(archive, path):
    """The manifest, or (None, message).

    Never raises for a manifest this command cannot make sense of. It can
    still raise for a manifest whose DATA does not read — a bad CRC leaves
    `archive.read` as `BadZipFile`, which is not one of the three this
    catches. `import_` runs `testzip` before reaching here for that reason.
    """
    try:
        raw = archive.read(MANIFEST)
    except KeyError:
        return None, (
            f"{path} holds no {MANIFEST} — it was not written by `seal export`"
        )
    try:
        manifest = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as exc:
        return None, f"{path}'s {MANIFEST} could not be read: {exc}"
    if not isinstance(manifest, dict):
        return None, f"{path}'s {MANIFEST} is not an object"
    if manifest.get("format") != FORMAT:
        return None, (
            f"{path} is format {manifest.get('format')!r} and this build reads "
            f"format {FORMAT}. Reading it anyway would place records by fields "
            "that may have moved"
        )
    return manifest, ""


def place(destination, data):
    """(path to write, outcome) for one incoming file — never overwriting.

    `None` as the path means nothing to write. The candidates are the
    destination itself and then its `.incoming` siblings, in order, and the
    first one whose bytes already equal `data` ends the search: re-importing
    the same zip is then a run that writes nothing, rather than a second pile
    of `.incoming` copies of files that are already there.

    `lexists`, not `exists`. A candidate that is a symbolic link to nothing
    reads as absent to `exists`, and returning it would have the caller write
    THROUGH the link — round 2 measured a record leaving the root that way,
    at exit 0, reported as an ordinary collision. `lexists` calls such a name
    taken, `read_bytes` on it raises, and the copy moves to the next name.
    `linked_path` refuses the member's own name before any of this; the
    fallback names it never sees are what this covers.
    """
    if not os.path.lexists(destination):
        return destination, ADDED
    directory = os.path.dirname(destination)
    stem, ext = os.path.splitext(os.path.basename(destination))
    for n in range(0, 1000):
        candidate = (
            destination
            if n == 0
            else os.path.join(
                directory,
                f"{stem}.incoming{ext}" if n == 1 else f"{stem}.incoming-{n}{ext}",
            )
        )
        if not os.path.lexists(candidate):
            return candidate, COLLIDED
        try:
            if read_bytes(candidate) == data:
                return None, IDENTICAL
        except OSError:
            continue
    return None, COLLIDED


def destination_root(repo, home, shared, local, into):
    """(root to write into, message). Names it; `write_members` creates it.

    With no `--into`, the root in force wins; with none in force, local — the
    direction that puts nothing in the tree. Guessing shared would write this
    plugin's files into a repository that may be someone else's, which is the
    harm local mode exists to prevent, so the safe guess is the one made.

    Both roots present refuses whatever `--into` says, including nothing.
    The refusal used to sit inside the `--into` branch, which left the case
    the spec and both READMEs describe — `seal import` with no flag — writing
    into whichever root the gates happen to read first. A clone holding two
    roots is a clone whose owner has not said which is the real one, and a
    copy landing in one of them is not the moment to decide it.
    """
    if optin.marked(shared) and local and optin.marked(local):
        return "", (
            "both roots exist, and the gates read the first of them:\n"
            f"  {shared}   (shared mode — read first)\n"
            f"  {local}   (local mode)\n"
            "Importing into one would leave the other where nothing reads "
            "it. Move or remove one first; the plugin README's *Shared or "
            "local* section has both commands."
        )
    if into:
        wanted = shared if into == "shared" else local
        if not wanted:
            return "", "the common git directory could not be resolved"
        return wanted, ""
    if home:
        return home, ""
    if not local:
        return "", "the common git directory could not be resolved"
    return local, ""


def import_(args, cwd):
    """Write a carried root's records into this clone's, overwriting nothing."""
    repo, home, shared, local, _ = resolve(cwd)
    if not repo:
        print("not inside a git repository — seal works on a clone")
        return 1
    if not home and optin.earlier(shared):
        # With no root in force the import would make one under the git
        # directory, a second root beside the one the move is about to mark.
        print(earlier_root())
        return 1

    path = os.path.abspath(args.zip)
    if not os.path.isfile(path):
        print(f"{path} is not a file")
        return 1

    try:
        archive = zipfile.ZipFile(path)
    except (zipfile.BadZipFile, OSError) as exc:
        print(f"{path} is not a readable zip: {exc}")
        return 1

    with archive:
        # The order here is the fix for four separate measurements, and it is
        # the order itself rather than any one check: how big, then whether
        # the data reads, then the manifest, and only then the names. The
        # names go last because a later format is exactly what moves them.
        # `read_manifest` reads its member whole, so the bounds above it are
        # what keep that read affordable — and the member bound, which lives
        # in `unsafe`, is therefore read after the manifest rather than before.
        members = archive.infolist()
        if len(members) > MEMBER_COUNT_LIMIT:
            print(
                f"{path} holds {len(members)} members, more than the "
                f"{MEMBER_COUNT_LIMIT} this command will write."
            )
            print("\nNothing was written. A root this large is not a root of records.")
            return 1

        declared = sum(info.file_size for info in members)
        if declared > ARCHIVE_LIMIT:
            print(
                f"{path} declares {declared} bytes unpacked, more than the "
                f"{ARCHIVE_LIMIT} this command will read."
            )
            print("\nNothing was written. A root this large is not a root of records.")
            return 1

        # The manifest's own size, before it is read. It is exempt from the
        # name checks in `unsafe` and used to inherit the size exemption with
        # them, so a 400 MB one cost 400 MB of memory on its way to a verdict.
        fat = [
            info
            for info in members
            # `rstrip("/")`, matching the spelling `unsafe` exempts. The two
            # asked one question by different tests, so `manifest.json/`
            # passed the exemption there and the bound here.
            if info.filename.rstrip("/") == MANIFEST and info.file_size > MEMBER_LIMIT
        ]
        if fat:
            print(
                f"{path} declares {fat[0].file_size} bytes for {MANIFEST}, "
                f"more than the {MEMBER_LIMIT} a manifest may hold."
            )
            print("\nNothing was written. A root this large is not a root of records.")
            return 1

        # Every member's data, before the manifest is decoded and before the
        # first record is written. The manifest is a member too: a bad CRC on
        # it reached the console as a `BadZipFile` traceback, because
        # `read_manifest` ran first and its own `except` does not name that
        # type.
        #
        # `testzip` catches `BadZipFile` itself and answers with the member's
        # name, so that clause is a guard rather than a claim — it is the line
        # that would still be right if `testzip` stopped swallowing it. What
        # does leave `testzip` is an encrypted member (`RuntimeError`) and a
        # compression method this build has no decompressor for
        # (`NotImplementedError`), both measured 2026-09-03 as tracebacks.
        #
        # It reads every member, which the two bounds above are what make
        # affordable.
        try:
            corrupt = archive.testzip()
        except (zipfile.BadZipFile, RuntimeError, NotImplementedError) as bad:
            corrupt = str(bad)
        if corrupt:
            print(f"{path} holds a member this command cannot read: {corrupt}")
            print(
                "\nNothing was written. A zip that cannot be read whole is "
                "not a copy of anything."
            )
            return 1

        manifest, why = read_manifest(archive, path)
        if not manifest:
            print(why)
            return 1

        # The names AFTER the format, because a later format is exactly what
        # moves the names this checks. Measured 2026-09-03: a zip declaring
        # format 2 with its records under `records/` answered "is not under
        # seal/", which reads as a malformed zip where the truth is a build
        # too old — and that field exists for no other day.
        refusals = [reason for info in members if (reason := unsafe(info))]
        if refusals:
            print(f"{path} holds members this command will not write:")
            for reason in refusals:
                print(f"  {reason}")
            print(
                "\nNothing was written. A zip carrying one of these is not a "
                "zip to take a partial copy from."
            )
            return 1

        # Two facts, and they used to have one spelling. *There is no remote*
        # switches the check below off on purpose; *the question could not be
        # answered* switched it off just the same, so a git that timed out or
        # exited non-zero merged another project's records with no word about
        # it (#111). The unanswerable question refuses, which is the direction
        # `gitlinks_under_root` states and `porcelain` and `indexed` take.
        #
        # Read ONCE. The refusal below used to ask git a second time for the
        # URL it had already read and print whatever that call answered, so a
        # failure between the two put a blank where the message promises this
        # clone's URL — this ticket's own failure inside the message reporting
        # it.
        mine, why = remote_url(repo)
        theirs = manifest.get("remote")
        unreadable = []
        if mine is None:
            unreadable.append(f"this clone's remote could not be read: {why}")
        the_zip_is_silent = not isinstance(theirs, str)
        if the_zip_is_silent:
            # The TYPE, not the presence. Absent is the export's word for *I
            # could not read it*, and so is `null` — which is what any JSON
            # writer produces from the `None` this file's own `remote_url`
            # returns. Every other non-string reduces to "" in
            # `normalise_remote`, which is the empty ANSWER this check exists
            # to tell apart from silence, so presence alone let `null`, `42`,
            # `[]`, `{}` and `true` through at exit 0 with both guards off
            # (measured at `8fb1fb5`). An older build always wrote a string
            # here, so a zip carrying anything else either comes from a build
            # that could not look or was not written by `seal export` at all,
            # and neither answers the question.
            unreadable.append(
                "the zip records no remote this command can read, so the "
                "machine that exported it could not read one either"
            )
        if unreadable and not args.allow_unreadable_remote:
            print("whether this zip came from this repository cannot be answered:")
            for reason in unreadable:
                print(f"  {reason}")
            print(
                "\nNothing was written. Records are keyed by work-item id, so "
                "merging another project's would spread through the root with "
                "nothing to tell them apart afterwards, and a remote that "
                "could not be read is not the same fact as a repository "
                "without one."
            )
            # Which machine can fix this decides what to tell the person. A
            # git that failed HERE may answer on the next run; a zip that
            # records no remote reads the same on every run there is, so the
            # export has to happen again on the machine that wrote it. One
            # line for both sent a person into a re-run loop that can never
            # end.
            #
            # The ZIP's silence decides, not this clone's, and the two can be
            # silent at once. A first cut branched on `mine is None`, which
            # sent exactly the both-silent case back to the re-run advice —
            # this ticket's own defect, re-entered at a narrower coordinate
            # by the fix for it. Re-running here cannot clear the zip side no
            # matter what this clone's git does next, so that side wins.
            if the_zip_is_silent:
                print(
                    "Re-running this cannot change what the zip records — "
                    "export again on the machine that wrote it, or pass "
                    "--allow-unreadable-remote to import without the check."
                )
            else:
                print(
                    "Run this again if the failure here was transient, or "
                    "pass --allow-unreadable-remote to import without the "
                    "check."
                )
            return 1

        here = normalise_remote(mine)
        there = normalise_remote(theirs)
        if here and there and here != there and not args.allow_other_repo:
            print("this zip was exported from another repository:")
            print(f"  the zip says   {theirs}")
            print(f"  this clone is  {mine}")
            print(
                "\nNothing was written. Records are keyed by work-item id, so "
                "merging another project's would spread through the root with "
                "nothing to tell them apart afterwards.\n"
                "If the two are one repository under two spellings, pass "
                "--allow-other-repo."
            )
            return 1

        into, why = destination_root(repo, home, shared, local, args.into)
        if not into:
            print(why)
            return 1

        linked = linked_path(into, archive)
        if linked:
            print(
                f"{optin.HOME}/{linked} in this clone is a symbolic link, and "
                "writing through it would put records outside the root."
            )
            print(
                "\nNothing was written. Replace the link with a real "
                "file or directory and run this again."
            )
            return 1

        blocked = blocked_path(into, archive)
        if blocked:
            # Two sides, two remedies. The clash comes from this clone (move
            # the file) or from the zip alone (there is nothing here to move,
            # and the machine that exported it is who has to send another).
            # Measured 2026-09-03: the second answered with the first's words,
            # sending a person to rename a file they do not have.
            if os.path.lexists(os.path.join(into, *blocked.split("/"))):
                print(
                    f"{optin.HOME}/{blocked} in this clone is not a directory, "
                    "and this zip needs it as one."
                )
                print("\nNothing was written. Move or rename it and run this again.")
            else:
                print(
                    f"{path} names {optin.HOME}/{blocked} as a file and puts "
                    "members under it, which no filesystem can hold at once."
                )
                print(
                    "\nNothing was written. Ask the machine that exported it "
                    "for another zip."
                )
            return 1

        try:
            counts, collisions, refused = write_members(archive, into)
        except OSError as stopped:
            # Every refusal above happens before the first byte, and this is
            # the one failure that cannot: the filesystem can say no with
            # records already written — a directory in the root that is not
            # writable, a full disk. Measured 2026-09-03, both left a partial
            # copy and a traceback with no line of this command's own.
            print(f"the copy stopped part-way: {stopped}")
            print(
                "\nSome records were written and some were not. Fix what the "
                "line above names and run this again — this command "
                "overwrites nothing, so a second run finishes the copy and "
                "reports what was already here byte for byte."
            )
            return 1

    print(f"imported into {display(repo, into)}")
    print(f"  {plural(counts[ADDED], 'file')} added")
    print(f"  {plural(counts[IDENTICAL], 'file')} already here, byte for byte")
    print(
        f"  {plural(counts[COLLIDED], 'file')} landed beside an existing one"
        + (":" if collisions else "")
    )
    for existing, landed in collisions:
        print(f"    {existing}  ->  {landed}")
    for name in refused:
        print(f"  {name} was not written — its name was taken during the import")
    # Both fields read the way `remote` is read, and for the same reason: they
    # come from a manifest another machine wrote. `head` was guarded and
    # `exported_at` was not, so a manifest carrying one without the other
    # raised `KeyError` HERE — after every record was written, so the person
    # saw exit 1 and a traceback for a copy that had succeeded, and the two
    # lines below never printed.
    head = manifest.get("head")
    when = manifest.get("exported_at")
    if isinstance(head, str) and head:
        stamp = when if isinstance(when, str) and when else "an unrecorded time"
        print(f"\nExported at {stamp} from {head[:12]}.")
    print(
        "Which of a collided pair is right is a reading, not a merge — this "
        "command overwrites nothing."
    )
    return 0


def write_members(archive, into):
    """Write every `seal/…` member under `into`. Names are already checked.

    The path is rebuilt from segments rather than joined from the member's
    name, so nothing the archive wrote reaches the filesystem as a path.
    """
    counts = {ADDED: 0, IDENTICAL: 0, COLLIDED: 0}
    collisions, refused = [], []
    for info in archive.infolist():
        name = info.filename
        if info.is_dir() or name == MANIFEST:
            continue
        parts = [p for p in name.split("/") if p][1:]  # drop the `seal/` prefix
        if not parts:
            continue
        destination = os.path.join(into, *parts)
        data = archive.read(name)
        target, outcome = place(destination, data)
        if target is None:
            counts[outcome] += 1
            continue
        os.makedirs(os.path.dirname(target), exist_ok=True)
        # `place` has already turned every taken name down, so a target that
        # is taken by the time of this open is a name something else took in
        # between. `lexists` asks that question on every platform; `O_EXCL`
        # narrows the moment between the asking and the answering, and it
        # refuses to open THROUGH a symbolic link only on POSIX — CI's windows
        # leg wrote through a broken link with the flag set (run 33715420379,
        # 2026-09-03). Both answers are the same: do not write here.
        # Counted after the write, so the report never names a file that was
        # not written.
        try:
            if os.path.lexists(target):
                raise FileExistsError(errno.EEXIST, os.strerror(errno.EEXIST), target)
            opened = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o666)
        except FileExistsError:
            # The name was free when `place` chose it and is taken now. Named
            # rather than skipped: a silent drop reads as a zip that held one
            # fewer record, which is the one thing this report must not say.
            refused.append("/".join(parts))
            continue
        with os.fdopen(opened, "wb") as handle:
            handle.write(data)
        counts[outcome] += 1
        if outcome == COLLIDED:
            collisions.append(
                (
                    "/".join(parts),
                    os.path.relpath(target, into).replace(os.sep, "/"),
                )
            )
    return counts, collisions, refused


# --- the mode: a row that is declared, and a folder that decides ------------
#
# `README.md`'s *Shared or local* section carried both directions as two shell
# lines, a `mv` and a commit. They are correct, and a person who has not read
# that section has no way to arrive at them. This is that section made
# runnable, plus the three things a `mv` cannot do: refuse when the other
# root is already there, refuse when the tree is dirty under what it is about
# to stage, and write the row so the file and the folder agree afterwards.
# The workflow file is not among them: `.github/` is `seal pr-checks`'s
# (#952).
#
# **Nothing at runtime reads the row.** Every hook resolves the root through
# `hooks/optin.py#home_at`, which reads `<repo>/seal/` then
# `<git-common-dir>/seal/`, and that stays the only signal. The row says what
# the repository WANTS; the folder's location says what it HAS. A gate that
# trusted the row would go looking in a place with no folder, and everything
# in `optin` is documented to fail toward "not opted in" rather than toward a
# guess (`docs/one-root-by-lifetime.md`, "The opt-in signal is the root
# itself").

# The config table is READ in `hooks/config.py` and WRITTEN here. The reader
# moved because a `PreToolUse` gate needs the `Mode` row and must not import
# this file to get it (#151), and these aliases are what keeps the move from
# becoming a second parser: one implementation, reached by the name each
# caller already spells. Everything below the writer's own line -- `with_row`,
# `write_row`, `NEW_CONFIG` -- stays here, because writing the row is this
# command's job and nothing else does it; where to write it is the reader's
# walk, `config_table`, and nothing here walks the table again (#871).
CONFIG = repo_config.CONFIG
ROW_ITEM = repo_config.ROW_ITEM
LOCAL, SHARED = repo_config.LOCAL, repo_config.SHARED
MODES = repo_config.MODES

# The workflow `seal pr-checks install` writes, as GIT spells a pathspec: forward
# slashes on every platform. `under()` turns it into a path for this
# filesystem. The two dialects live as separate strings rather than one
# string used for both, because a literal separator inside an
# `os.path.join` argument produces `C:/proj\.github/workflows` — a path in
# two dialects that equals nothing any caller built (`hooks/optin.py`
# carries the same reasoning about `repo_root`).
WORKFLOW = ".github/workflows/hygiene.yml"
# The row this command writes itself, spelled as git spells a pathspec —
# beside WORKFLOW and for the same reason.
CONFIG_PATHSPEC = f"{optin.HOME}/{CONFIG}"

# The line CI's own workflow uses to clone this plugin. A file at WORKFLOW
# carrying it is one this plugin wrote; a file that does not is somebody
# else's with our name, and `seal pr-checks` neither overwrites nor removes
# it. `tests/test_seal.py::Test_module` asserts the template still contains
# this, so the marker cannot drift away from what it identifies.
PLUGIN_CLONE = "https://github.com/MichaelYcJo/AgenticSeal.git"
# The clone line every workflow a release before the rename wrote carries:
# the repository under its name before #1051. For the minor release of the
# rename a file carrying it is this plugin's too, and `seal pr-checks
# install` writes the template over it at the new name; the next minor
# release removes this reading.
OLD_PLUGIN_CLONE = "https://github.com/MichaelYcJo/SpecSeal.git"
# The release a workflow's clone line pins, which `seal pr-checks` reports.
PIN = re.compile(r"--branch\s+(\S+)")

# The version placeholder in `templates/setup/hygiene.yml`. A workflow written with
# it still in place fails CI's `git clone --branch` on the first pull
# request, so a version that cannot be read writes no file at all.
PLACEHOLDER = "v<version>"

PLUGIN_ROOT = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
)

# The table walk and the fence rule, taken from the reader rather than
# written again here: one implementation, reached by the name each caller
# already spells. `config_table` is the one walk of the table (#871), and
# `with_row` overwrites and inserts at the lines it names. `fence_map` is the
# fence walk with the state it ENDS in kept, which is what lets `write_row`
# tell an unclosed fence from every other reason a row would not read back.
config_table = repo_config.config_table
unfenced = repo_config.unfenced
fence_map = repo_config.fence_map

NEW_CONFIG = """# Repository config

<!-- What this repository says about itself, one row per item. This file was
created by `seal mode`; `templates/setup/config.md` in the plugin documents
every row and what an absent one means. -->

| Item | Value |
|---|---|
| {item} | {value} |
"""


def under(root, rel):
    """The disk path of a `/`-joined repository-relative path.

    Spelled the way `hooks/root-migrate.py#under` spells it, and the split
    happens HERE rather than inside `os.path.join`, for the reason WORKFLOW
    gives above.
    """
    return os.path.join(root, *rel.split("/"))


config_path = repo_config.config_path
config_rows = repo_config.config_rows


declared = repo_config.declared_mode


def ending_of(line, fallback):
    """The line's own ending, or FALLBACK where it has none."""
    bare = line.rstrip("\r\n")
    return line[len(bare) :] or fallback


def line_ending(lines):
    """The first ending in the file, so a CRLF file stays CRLF."""
    for line in lines:
        found = ending_of(line, "")
        if found:
            return found
    return "\n"


def doubled_modes(lines):
    """The sentence a file holding more than one `Mode` row is refused in,
    naming each line by its number and as written, or "" where it holds one
    or none. LINES keep their endings, and their join is the file the walk
    reads. It opens lower-case and ends with no full stop, so it reads after
    the path.

    **Every `Mode` row the walk read, not the first** (#867). A row written
    twice has no value (`hooks/config.py#config_value`), so the writer has no
    row to overwrite, and this sentence names each line from the walk's own
    line numbers (#871)."""
    rows, _refusals = config_table("".join(lines))
    modes = [index for index, item, _value in rows if item == ROW_ITEM]
    if len(modes) < 2:
        return ""
    named = ", ".join(f"line {i + 1} `{lines[i].strip()}`" for i in modes)
    return (
        f"holds {len(modes)} `{ROW_ITEM}` rows ({named}), and a row written "
        "twice has no value, so writing over one of them would leave the file "
        "saying two things — delete all but one and run this command again"
    )


def with_row(text, value):
    """(TEXT with the `Mode` row set to VALUE, every other line's bytes kept,
    "") — or (None, the refusal) where TEXT holds more than one `Mode` row,
    or a table the walker refused.

    Three cases, and the file is a person's in all three: an existing row is
    replaced where it stands, a table with no such row gains one at its end,
    and a file with no such table at all gets one appended after a blank
    line. Nothing is re-wrapped, re-ordered, or re-ended. A fourth, two rows
    or more, is refused rather than resolved (#867): no row of them is the
    answer, so there is none to replace, and adding one more is a third.

    **Where to write is the reader's walk, `config_table`, and nothing
    else** (#871). The line overwritten is the one the walk read as the
    `Mode` row; a new row goes after the last row the walk read, or under
    the delimiter row where it read none, the header being the first line
    `unfenced` shows whose cells are the config header -- the line the walk
    itself starts at. A writer with a walk of its own is the file two rows
    deep (#429, #415): a `Mode` row it adds under a line its walk reads past
    is a second `Mode` row to a reader that stops there. **A table the
    walker refused is refused here** in the
    shape a doubled row takes, with the walker's sentence: a row the walk
    did not read may be the `Mode` row, so there is none to replace, and
    adding one may make two.
    """
    row = f"| {ROW_ITEM} | {value} |"
    # exempt from splitlines: lines the GFM walk numbers
    lines = text.splitlines(keepends=True)
    ending = line_ending(lines)
    doubled = doubled_modes(lines)
    if doubled:
        return None, doubled
    rows, refused = config_table(text)
    if refused:
        return None, refused[0]
    modes = [index for index, item, _value in rows if item == ROW_ITEM]
    if rows:
        end = rows[-1][0] + 1
    else:
        header = next(
            (
                index
                for index, line in unfenced(lines, text)
                if repo_config.table_cells(line) == repo_config.CONFIG_TABLE
            ),
            None,
        )
        end = -1 if header is None else header + 2

    if modes:
        lines[modes[0]] = row + ending_of(lines[modes[0]], ending)
        return "".join(lines), ""
    if end >= 0:
        # **The line above the insertion point may carry no ending.** Where
        # the first table's last row is the file's last line and the file
        # ends without a newline, the inserted row is concatenated onto it:
        # `| Record language | Korean || Mode | shared |` is one line of four
        # cells, no walk of that table reads either row, and the person's own
        # row is gone. The third arm below has terminated the last line all
        # along; this one has to as well. Before this repair the same shape
        # was written silently and cost the row that was already there (#429,
        # round 2).
        if end == len(lines) and lines and not lines[-1].endswith(("\n", "\r")):
            lines[-1] += ending
        lines.insert(end, row + ending)
        return "".join(lines), ""

    if lines and not lines[-1].endswith(("\n", "\r")):
        lines[-1] += ending
    if lines:
        lines.append(ending)
    lines.extend([f"| Item | Value |{ending}", f"|---|---|{ending}", row + ending])
    return "".join(lines), ""


def write_row(home, value):
    """Write `| Mode | value |` into the root's `config.md`; "" or why not.

    Refused rather than followed: a symbolic link at that name is a write
    that leaves the root, which is the one way out of a structure the export
    walks (`root_files`), and a directory is `IsADirectoryError` arriving as
    a traceback.
    """
    path = config_path(home)
    if os.path.islink(path):
        return f"{path} is a symbolic link"
    if os.path.isdir(path):
        return f"{path} is a directory"
    try:
        # `newline=""` on both sides, so a CRLF file is read and written back
        # as one: with translation on, every line of somebody's file would be
        # rewritten by an edit to one row of it.
        with open(path, encoding="utf-8", newline="") as handle:
            text = handle.read()
    except FileNotFoundError:
        text = None
    except (OSError, ValueError) as exc:
        return f"{path} could not be read: {exc}"

    new, doubled = (
        (NEW_CONFIG.format(item=ROW_ITEM, value=value), "")
        if text is None
        else with_row(text, value)
    )
    if doubled:
        return f"{path} {doubled}. Nothing was written"
    # **The row is not written until it reads back.** The walk skips
    # fenced lines, so a file whose table is swallowed by a fence nobody
    # closed has no table this walk can see -- and `with_row` then appends
    # one at the END of the file, which is inside that fence. The write
    # succeeds, `declared_mode` still answers "none", and `seal mode` reports
    # a row that no walk reads: the mode gate asks again next session and the
    # file grows by a table a run. Measured over two fixtures, three runs
    # each: 9 -> 13 -> 17 -> 21 lines with `('none', '')` throughout.
    # Checked here rather than after the write, so a refusal leaves the
    # person's file exactly as it was (#429).
    if not any(item == ROW_ITEM for item, _value in config_rows(new)):
        # **The message names the cause it CHECKED, never one it inferred.**
        # This guard is about the row not reading back, and an unclosed fence
        # is one way for that to happen rather than the only one -- a file
        # whose last line carries no ending reached it too, and telling that
        # person to close a fence is the wrong-cause shape this work item is
        # about (#429, round 2). That shape is repaired above; the branch
        # stays because the next member of the class must not be misdescribed
        # either.
        # exempt from splitlines: lines the GFM walk numbers
        if fence_map(new.splitlines(), new)[1] is not None:
            return (
                f"{path} has a fenced code block that is never closed, and "
                "everything under it -- the table this command would have "
                f"written the `{ROW_ITEM}` row into -- is inside it, where no "
                "walk of that table reads it. Nothing was written. Close the "
                "fence and run this command again."
            )
        # The table walker refuses what this write would leave -- a table
        # appended under an HTML block nobody closed, for one -- and its
        # sentence names the cause and the edit.
        walked = config_table(new)[1]
        if walked:
            return (
                f"{path}, with the `{ROW_ITEM}` row written into it, "
                f"{walked[0]}. Nothing was written and your file is exactly "
                "as it was"
            )
        return (
            f"{path} would not read the `{ROW_ITEM}` row back after this "
            "write, so the row would land where no walk of that table reads "
            "it. Nothing was written and your file is exactly as it was. "
            "This is a defect in this command rather than in your file: "
            "please report it with the file's first lines."
        )
    try:
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(new)
    except (OSError, ValueError) as exc:
        return f"{path} could not be written: {exc}"
    return ""


def porcelain(repo, *paths):
    """`git status --porcelain` lines under PATHS, or one line saying git
    could not answer.

    **Both paths this command stages, not just the root.** The switch stages
    a removal or an addition of the workflow file too, and a guard watching
    only the root would leave that path's uncommitted work to be taken by
    `git rm`. Enumerating the class is the point; `frame/design.md` *What the switch
    touches* lists all five.

    An unanswerable question reads as dirty, the direction
    `hooks/root-migrate.py#dirty` takes: moving on a guess is the one
    direction with no undo. `git rm -r --cached` drops a staged edit out of
    the index and prints nothing about it (measured 2026-09-03).
    """
    try:
        done = subprocess.run(
            ["git", "-C", repo, "status", "--porcelain", "--", *paths],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=15,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return [f"git status could not be run ({exc})"]
    if done.returncode != 0:
        return [(done.stderr or "").strip() or f"git status exited {done.returncode}"]
    # exempt from splitlines: git output
    return [line for line in (done.stdout or "").splitlines() if line.strip()]


def indexed(line, moved=False):
    """Whether a porcelain line is something the index can lose.

    **Untracked is not.** The guard exists because `git rm -r --cached` takes
    a staged edit out of the index and prints nothing about it (measured
    2026-09-03); a file the index has never heard of cannot be taken out of
    it, and it travels with the folder in both directions — moved out with
    the root going to local, staged by `git add` going to shared. Refusing
    over one was not a stricter version of the same rule, it was a different
    rule with no grounds, and it made the ordinary first run refuse: `seal
    mode` writes an absent row, and the switch a person runs next met the
    file it had just written.

    **A pure deletion is not, once the move has already happened.** That is
    the shape a stopped run — or a person who ran the README's `mv` by hand —
    leaves behind: the files are gone from the worktree because they are at
    the other root now, and the `git rm -r --cached` that stages it is the
    step still owed. `hooks/root-migrate.py#dirty` makes exactly this
    exception, in the same words: "a resume has to see past its own earlier
    steps or a stopped move can never finish". It is a deletion and NOTHING
    else — `MD` and `AD` still refuse, because a staged edit is precisely
    what `git rm -r --cached` drops without a word.

    **The row this command wrote itself is not, either.** `seal mode` fills
    an absent row in from the folder, so the switch a person runs next meets
    a worktree-only modification of the one file the switch rewrites anyway.
    The `??` exception above was written for this and reached half of it: an
    untracked `config.md` passed and a TRACKED one still refused — and the
    tracked spelling is every repository `hooks/root-migrate.py` carried over
    from the 0.3.x layout, whose `.specseal/config.md` arrives committed.
    That is the population this whole work item exists for. Measured
    2026-09-03: `seal mode` then `seal mode local` exits 1.

    A STAGED edit to it still refuses, for the reason every staged edit does:
    `git rm -r --cached` drops it without a word.

    A line git could not produce at all does not start with a status pair,
    and reads as indexed — the unanswerable question refuses, which is
    `hooks/root-migrate.py#dirty`'s direction.
    """
    pair = line[:2]
    if pair == "??":
        return False
    if pair == " M" and line[3:].strip() == CONFIG_PATHSPEC:
        return False
    return not (moved and pair in ("D ", " D"))


def tracked(repo, rel):
    """True when git tracks anything under REL.

    `git rm -r --cached` on a pathspec matching no index entry exits 128
    (measured 2026-09-03), so the step is skipped rather than run and
    excused — which is also what makes a second run of a stopped switch
    finish it instead of failing.
    """
    try:
        done = subprocess.run(
            ["git", "-C", repo, "ls-files", "-z", "--", rel],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=15,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    if done.returncode != 0:
        return False
    return bool([p for p in (done.stdout or "").split("\0") if p])


def committed(repo, rel):
    """True when HEAD carries REL; False on a branch with no commit yet."""
    _text, why = git_asked(repo, "cat-file", "-e", f"HEAD:{rel}")
    return not why


def staged_text(repo, rel):
    """The index's copy of REL, decoded as `open()` reads the working file,
    or None where git could not give it.

    Not `git_asked`, which strips: a trailing newline is part of what is
    compared byte for byte. Text mode turns CRLF into LF the way the working
    file's read does, so a checkout that converts line endings compares one
    file with itself.
    """
    try:
        done = subprocess.run(
            ["git", "-C", repo, "cat-file", "blob", f":{rel}"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=15,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    return done.stdout if done.returncode == 0 else None


def other_worktrees(repo):
    """Every other worktree of this clone, by path.

    Measured 2026-09-03: switching shared → local from one worktree leaves
    every other one holding the committed `<repo>/seal/` on its own branch,
    so the two read two different roots until the commit reaches both. It
    heals itself and loses nothing, so it is named rather than refused.

    **A git that cannot answer here is silent by design, and this is the one
    call site left that asks through `git()`.** `git()` reads every failure as
    `""`, so a timeout or a non-zero exit reads here as *this clone has no
    other worktrees* and the note does not print. That is the whole
    consequence: the note is advisory, nothing is lost and nothing is claimed
    falsely. The other four call sites read `""` as a fact somebody acts on
    and now ask through `git_asked` (#111) — this one is the member of that
    class that is right to.
    """
    # RIDER: `git worktree list --porcelain` prints the GIT DIRECTORY as the
    # worktree path for a repository built with `--separate-git-dir`, and for
    # a bare clone, with no `bare` line on the first to tell it by. Measured
    # 2026-09-08 against a scratch `--separate-git-dir` repository: this
    # returns `['<...>/sepgit']`, and `git -C <that> rev-parse --show-toplevel`
    # answers `fatal: this operation must be run in a work tree`. So `seal
    # mode` there prints a note calling the git directory another worktree of
    # this clone. Nothing decides on it and nothing is lost -- the caller at
    # `mode_switch` only prints -- which is why it was named here rather than
    # fixed in a round-1 fix pass that had no finding on this function.
    # The fix is to compare the clone by common git directory and refuse a
    # path that is not a work tree. Filter this list that way when this
    # function is next opened.
    here = os.path.realpath(repo)
    found = []
    # exempt from splitlines: git output
    for line in git(repo, "worktree", "list", "--porcelain").splitlines():
        if line.startswith("worktree "):
            path = line[len("worktree ") :].strip()
            if path and os.path.realpath(path) != here:
                found.append(path)
    return found


def plugin_version():
    """The installed plugin's version, or "".

    Read from beside this script rather than from `CLAUDE_PLUGIN_ROOT`: this
    file IS in the plugin, and an environment variable is one more thing that
    can be unset in the shell a person happens to be in.
    """
    try:
        with open(
            os.path.join(PLUGIN_ROOT, ".claude-plugin", "plugin.json"),
            encoding="utf-8",
        ) as handle:
            version = json.load(handle).get("version")
    except (OSError, ValueError, AttributeError):
        return ""
    return version if isinstance(version, str) else ""


def plugin_workflow():
    """The exact bytes `install_workflow` writes, or "" when it could not.

    One reader for two questions — what to write, and whether a file already
    there is the one this plugin would have written. `remove_workflow` asks
    the second: an untracked workflow this plugin can put back byte for byte
    costs nothing to remove, and that is the state the way back names.
    """
    version = plugin_version()
    if not version:
        return ""
    source = os.path.join(PLUGIN_ROOT, "templates", "setup", "hygiene.yml")
    try:
        with open(source, encoding="utf-8") as handle:
            text = handle.read()
    except (OSError, ValueError):
        return ""
    if PLACEHOLDER not in text:
        return ""
    return text.replace(PLACEHOLDER, "v" + version)


def carries_clone(text):
    """True where TEXT carries this plugin's clone line, at the repository's
    name or at the name it had before the rename."""
    return PLUGIN_CLONE in text or OLD_PLUGIN_CLONE in text


def workflow_at(repo):
    """What stands at WORKFLOW in `repo`: (kind, text or reason).

    `plugin`, a regular file that reads and carries PLUGIN_CLONE or
    OLD_PLUGIN_CLONE, with its text; `absent`, with ""; or, with the clause that says why the file is
    not this plugin's, `link`, `unreadable` or `other`. The one reader the
    three forms of `seal pr-checks` share, so the report, the install and the
    removal tell this plugin's file from somebody else's by one rule.
    """
    path = under(repo, WORKFLOW)
    if not os.path.lexists(path):
        return "absent", ""
    if os.path.islink(path):
        return "link", "is a symbolic link"
    try:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
    except (OSError, ValueError) as exc:
        return "unreadable", f"could not be read ({exc})"
    if not carries_clone(text):
        return "other", "does not carry this plugin's clone line"
    return "plugin", text


def pinned(text):
    """The release the clone line in `text` pins, or ""."""
    found = PIN.search(text)
    return found.group(1) if found else ""


def left_workflow_line(text):
    """What `seal mode local` says of this plugin's workflow, `text`, which
    the switch leaves in the tree.

    Pinned to the installed release, the steps read a tree with no root as
    nothing declared and pass. Pinned to an older one they fail every pull
    request there, so any other pin, and a version that cannot be read, is
    named with the two ways out rather than promised to pass (#952).
    """
    pin, version = pinned(text), plugin_version()
    if version and pin == "v" + version:
        return (
            f"{WORKFLOW} stays: in local mode its checks examine nothing and "
            "pass, and `seal pr-checks remove` takes them out"
        )
    named = pin or "no release its clone line names"
    here = (
        f"pinned to {named} and not to the installed v{version}"
        if version
        else f"pinned to {named}, and the installed release could not be read"
    )
    to = f"v{version}" if version else "the installed release"
    return (
        f"{WORKFLOW} stays, {here}: a release before this one fails every pull "
        f"request with no {optin.HOME}/ in the tree. Move its `--branch` line "
        f"to {to}, or run `seal pr-checks remove`"
    )


def install_workflow(repo):
    """Write the pull-request checks; (what happened, the line to print).

    Refused where `<repo>/seal/` is not the root, a directory whose README
    opens with the marker, because the checks read committed records and only
    a root in the tree is committed; a `seal/` the project keeps for itself
    holds none of them. Never overwrites, but for one file: this plugin's own
    file already there is reported with the release it pins, and anybody
    else's is left alone. The one is this plugin's file cloning the
    repository's name before the rename, which is written over at the new
    name.
    """
    shared, _local = optin.home_paths(repo)
    if optin.earlier(shared):
        return "no-root", earlier_root()
    if not shared or not optin.marked(shared):
        return "no-root", (
            f"{WORKFLOW} was NOT written: {optin.HOME}/ is not in this tree, "
            "and the checks read committed records, which only a root in the "
            f"tree has. `seal mode {SHARED}` puts it in the tree."
        )
    kind, found = workflow_at(repo)
    old_slug = kind == "plugin" and PLUGIN_CLONE not in found
    if kind == "plugin" and not old_slug:
        return "installed", (
            f"{WORKFLOW} is already this plugin's, pinned to "
            f"{pinned(found) or 'no release its clone line names'}, so nothing "
            "was written"
        )
    if kind != "absent" and not old_slug:
        return "kept", (
            f"{WORKFLOW} is there and {found}: it is not "
            "this plugin's file, so nothing was written. Move it aside and run "
            "this again, or add the checks to it by hand."
        )
    path = under(repo, WORKFLOW)
    version = plugin_version()
    if not version:
        return "no-version", (
            f"{WORKFLOW} was NOT written: the plugin's version could not be "
            f"read from {os.path.join(PLUGIN_ROOT, '.claude-plugin', 'plugin.json')}, "
            f"and a workflow still carrying `{PLACEHOLDER}` fails CI's clone "
            "on the first pull request. Copy templates/setup/hygiene.yml in by "
            "hand and replace that placeholder with the release you run."
        )
    source = os.path.join(PLUGIN_ROOT, "templates", "setup", "hygiene.yml")
    try:
        with open(source, encoding="utf-8") as handle:
            text = handle.read()
    except (OSError, ValueError) as exc:
        return "unreadable", f"{WORKFLOW} was NOT written: {source} — {exc}"
    if PLACEHOLDER not in text:
        # The substitution has to be able to fail. A template that stopped
        # carrying the placeholder would be written pinned to whatever it
        # says instead, and nothing would report it.
        return "no-placeholder", (
            f"{WORKFLOW} was NOT written: {source} no longer carries "
            f"`{PLACEHOLDER}`, so the version could not be pinned. This is a "
            "defect in the plugin — report it rather than working around it."
        )
    text = text.replace(PLACEHOLDER, "v" + version)
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)
    except (OSError, ValueError) as exc:
        return "failed", (
            f"{WORKFLOW} was NOT written: {exc}. Copy "
            "templates/setup/hygiene.yml in by hand, or run this command again."
        )
    # The return code here for the reason the root's `git add` in `switch`
    # reads it: `git()` answers "" for a failure, and an ignore rule matching
    # `.github/` reaches this one. Measured 2026-09-03 — the file was written,
    # nothing entered the index, and the command said `staged it` and `Now
    # commit`. This command exists to get the checks running, so a workflow
    # that never reaches the commit is the whole point lost, silently.
    done = subprocess.run(
        ["git", "-C", repo, "add", "--", WORKFLOW],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
    )
    if done.returncode != 0:
        return "unstaged", (
            f"{WORKFLOW} was written (pinned to v{version}) but could NOT "
            f"be staged: {(done.stderr or '').strip()}\n"
            f"A commit now would not carry it, so the pull-request checks "
            f"would never run. An ignore rule matching {WORKFLOW} or "
            f"`.github/` is the usual cause. Run `git add -f :/{WORKFLOW}` "
            "yourself, or take the rule out."
        )
    if old_slug:
        return "written", (
            f"rewrote {WORKFLOW}, which cloned the plugin from the repository's "
            f"name before the rename, at the new name (pinned to v{version}) "
            "and staged it"
        )
    return "written", f"wrote {WORKFLOW} (pinned to v{version}) and staged it"


def remove_workflow(repo):
    """Remove the pull-request checks; (what happened, the line to print).

    It needs no root: a workflow that outlived its root is the case it is
    for. Left in a local-mode repository and pinned to this release, every
    step of the workflow examines nothing and passes
    (`unverified_check.py#absent_root`), so there it is the person's choice
    and never a repair; pinned to an older release, it is the way out of a
    workflow that fails every pull request (`left_workflow_line`).

    A file this plugin did not write is left alone: deleting somebody's
    workflow because it shares a name is the destructive direction.
    """
    path = under(repo, WORKFLOW)
    kind, text = workflow_at(repo)
    if kind == "absent":
        if not tracked(repo, WORKFLOW):
            return "absent", f"there is no {WORKFLOW}, so there is nothing to remove"
        # Gone from the working tree is not gone from the next commit, which
        # is made from the index: a person deleted by hand the file `install`
        # staged, or a committed copy whose deletion is not staged (round 5,
        # finding 1). `git rm` of a path missing from the working tree exits
        # 0 and drops its index entry in both states (measured, round 5),
        # and with the file gone git's refusal of a staged change does not
        # fire, so it would drop a staged edit unasked (measured, round 6).
        # The index copy is taken only where a copy survives it: byte for
        # byte the copy HEAD carries, or what `install` writes back now.
        staged = staged_text(repo, WORKFLOW)
        if staged is None:
            return "kept", (
                f"there is no {WORKFLOW} in the working tree, and the index's "
                "copy of it could not be read, as for a path left unmerged, so "
                "it was left alone. Look at it with `git status` and take it "
                "out yourself."
            )
        if not carries_clone(staged):
            return "kept", (
                f"there is no {WORKFLOW} in the working tree, and the index "
                "holds a copy that does not carry this plugin's clone line, "
                "so it was left alone: the index may hold the only copy of "
                "somebody's file. Look at it with `git diff --cached` and take "
                "it out yourself."
            )
        # Exit 0 where the index's blob and mode are HEAD's. Every other
        # exit is read as "not HEAD's", so the arm fails closed: 1 where they
        # differ, HEAD lacks the path, or the branch has no commit (git
        # 2.50.1 compares with the empty tree there, measured round 6).
        as_head = subprocess.run(
            ["git", "-C", repo, "diff", "--cached", "--quiet", "--", WORKFLOW],
            capture_output=True,
            timeout=30,
        )
        if not (as_head.returncode == 0 or staged == plugin_workflow()):
            return "kept", (
                f"there is no {WORKFLOW} in the working tree, and the index "
                "holds a copy that is neither byte for byte the copy HEAD "
                "carries nor byte for byte what this plugin writes NOW, so it "
                "was left alone: removing it would take the only copy of that "
                "edit with it. Look at it with `git diff --cached` and take it "
                "out yourself."
            )
        done = subprocess.run(
            ["git", "-C", repo, "rm", "--quiet", "--", WORKFLOW],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
        )
        if done.returncode != 0:
            return "failed", (
                f"{WORKFLOW} could not be removed: {(done.stderr or '').strip()}"
            )
        return "removed", (
            f"there was no {WORKFLOW} in the working tree, but the index still "
            "held it; took it out of the index, so the next commit does not "
            "carry it"
        )
    if kind == "link":
        return "kept", (
            f"{WORKFLOW} {text}, so it is not this plugin's file to remove — "
            "left alone."
        )
    if kind == "unreadable":
        return "kept", (
            f"{WORKFLOW} {text}, so it was left alone. Check by hand whether "
            "it is this plugin's."
        )
    if kind == "other":
        return "kept", (
            f"{WORKFLOW} was not written by this plugin, so it was left alone."
        )
    if not tracked(repo, WORKFLOW):
        # git holds no copy, so removing it would take the only one — unless
        # this plugin can write it back byte for byte, which is the state
        # `seal pr-checks install` followed by a `git reset` leaves. Round 1's
        # guard was reasoned about SOMEBODY ELSE'S file and applied to one
        # this command had written a moment earlier.
        if text != plugin_workflow():
            return "kept", (
                f"{WORKFLOW} is not tracked and is not byte for byte what "
                "this plugin writes NOW — it may be somebody's own, or this "
                "plugin's from another release, since the file is pinned to "
                "the version that wrote it. Either way git holds no copy and "
                "removing it would take the only one, so it is left alone. "
                "Look at it and delete it yourself."
            )
        try:
            os.remove(path)
        except OSError as exc:
            return "failed", f"{WORKFLOW} could not be removed: {exc}"
        return "removed", (
            f"removed {WORKFLOW} — untracked, and byte for byte this "
            "plugin's, so `seal pr-checks install` writes it back"
        )
    force = []
    if not committed(repo, WORKFLOW):
        # Staged and never committed, which is how `install` leaves it: git
        # keeps no committed copy, so this is the untracked case above, and
        # git's own `rm` refuses it with "has changes staged in the index"
        # (the sealer, at `55aea15d`). Forced only where the index AND the
        # working file are what this plugin writes now, so the force takes
        # nothing `install` cannot write back.
        if not (text == plugin_workflow() == staged_text(repo, WORKFLOW)):
            return "kept", (
                f"{WORKFLOW} is staged and never committed, and its staged "
                "copy or its working copy is not byte for byte what this "
                "plugin writes NOW, so it is left alone: git holds no "
                "committed copy, and removing it would take that edit with "
                "it. Look at it and delete it yourself."
            )
        force = ["--force"]
    done = subprocess.run(
        ["git", "-C", repo, "rm", "--quiet", *force, "--", WORKFLOW],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
    )
    if done.returncode != 0:
        return "failed", (
            f"{WORKFLOW} could not be removed: {(done.stderr or '').strip()}"
        )
    if force:
        return "removed", (
            f"removed {WORKFLOW} and took it out of the index — staged, never "
            "committed, and byte for byte this plugin's, so `seal pr-checks "
            "install` writes it back"
        )
    return "removed", f"removed {WORKFLOW} and staged the removal"


def pr_checks(args, cwd):
    """`seal pr-checks [install|remove]`: report, write or remove the
    workflow. Exit 0 for a report, a file written or already this plugin's,
    and a file removed or nothing there; 1 for every refusal, which writes
    and removes nothing, and for a file written that git would not stage.

    The report is one of three states: installed, with the release the file
    pins; not installed; or a file at WORKFLOW this plugin did not write."""
    repo = optin.repo_root(cwd)
    if not repo:
        print("not inside a git repository — seal works on a clone")
        return 1
    if args.action == "install":
        kind, line = install_workflow(repo)
        print(line)
        return 0 if kind in ("written", "installed") else 1
    if args.action == "remove":
        kind, line = remove_workflow(repo)
        print(line)
        return 0 if kind in ("removed", "absent") else 1
    kind, found = workflow_at(repo)
    if kind == "plugin":
        print(
            f"installed: {WORKFLOW} is this plugin's pull-request checks, "
            f"pinned to {pinned(found) or 'no release its clone line names'}. "
            "`seal pr-checks remove` takes them out."
        )
    elif kind == "absent":
        print(
            f"not installed: there is no {WORKFLOW}. `seal pr-checks install` "
            f"writes it where {optin.HOME}/ is in the tree."
        )
    else:
        print(
            f"not this plugin's: {WORKFLOW} is there and {found}, so this "
            "plugin's checks are not installed and that file is left alone."
        )
    return 0


def say_report(repo, home, shared, local, current, kind, value):
    """The report both `seal mode` and `seal mode --check` print."""
    print(f"  folder: {current:<7}{display(repo, home)}/")
    if kind == "mode":
        print(f"  row:    {value:<7}{display(repo, config_path(home))}")
    elif kind == "unknown":
        print(
            f"  row:    {value} — which is not a mode. The two values are "
            f"`{LOCAL}` and `{SHARED}`."
        )
    elif kind == "refused":
        print(f"  row:    refused  ({display(repo, config_path(home))})")
    else:
        print(f"  row:    not declared  ({display(repo, config_path(home))})")


def mode_refusal(home):
    """The sentence `seal mode` refuses the root's `config.md` in, or "":
    the reader's own sentence for a file that will not read, for a `Mode`
    row written twice the writer's, which names each line (#867), and for a
    table the walker refused the walker's, after the path (#871) -- the
    three things `with_row` would refuse, so a switch is refused before
    anything moves. Read through `hooks/config.py#config_text`, the one
    place the file is opened to tell absent from unreadable."""
    text, refused = repo_config.config_text(home)
    if refused:
        return refused
    if text is None:
        return ""
    # exempt from splitlines: lines the GFM walk numbers
    doubled = doubled_modes(text.splitlines(keepends=True))
    if doubled:
        return f"{config_path(home)} {doubled}"
    walked = config_table(text)[1]
    return f"{config_path(home)} {walked[0]}" if walked else ""


def mode_report(args, repo, home, shared, local, current):
    """`seal mode` and `seal mode --check`: the folder, the row, and whether
    they agree. The folder is never moved here.

    An absent row is written from the folder — the state every repository
    with a `config.md` is in today, since the pull-request language shipped
    as its only row. The value is an observation this command just made, so
    it cannot be wrong; nothing falls back to a default, because there is
    none. `--check` writes nothing at all: it runs in CI, and a check that
    mutates the tree it checks is not a check.

    **A refused file is reported and exits 2, with or without `--check`**
    (#867): a `config.md` that is there and will not read, or a `Mode` row
    written twice. The folder is still reported, because where things stand
    does not need the row; nothing is written, because a row written into a
    file nobody can read, or beside one that already disagrees, cannot make
    it agree.
    """
    kind, value = declared(home)
    if kind == "refused":
        say_report(repo, home, shared, local, current, kind, value)
        print(f"\n{mode_refusal(home) or value}. Nothing was written.")
        return 2
    if kind == "none" and not args.check:
        failed = write_row(home, current)
        if failed:
            print(f"the `{ROW_ITEM}` row could not be written: {failed}")
            print("The folder is still the answer, and it is:")
        else:
            print(
                f"no `{ROW_ITEM}` row was declared, so one was written from "
                f"where the folder is: `| {ROW_ITEM} | {current} |` in "
                f"{display(repo, config_path(home))}"
            )
            kind, value = "mode", current

    say_report(repo, home, shared, local, current, kind, value)

    if kind == "unknown":
        print(
            f"\nThe row names no mode, so nothing can be applied from it. "
            f"`seal mode {current}` writes what the folder says; editing the "
            f"row to `{LOCAL}` or `{SHARED}` and running `seal mode --apply` "
            "moves the folder."
        )
        return 1 if args.check else 0
    if kind == "none":
        return 0
    if value == current:
        print("\nThey agree.")
        return 0
    print(
        f"\nThey disagree: the row says `{value}` and the folder is "
        f"{current}. Two commands end it —"
    )
    print(f"  seal mode --apply     move the folder to {value}, as the row says")
    print(f"  seal mode {current:<11}correct the row to {current}, as the folder is")
    return 1 if args.check else 0


def both_roots(shared, local):
    return (
        "both roots exist, and the gates read the first of them:\n"
        f"  {shared}   (shared mode — read first)\n"
        f"  {local}   (local mode)\n"
        "Switching from here would leave the other where nothing reads it. "
        "Move or remove one first."
    )


def gitlinks_under_root(repo):
    """(submodule entries under the root, why they could not be read).

    Entries is None when the question could not be answered. `git()` reads
    every failure as "", so asking through it would answer "no submodule" for
    a timeout or a git that is not on PATH — and this guard exists to stop a
    break that cannot be undone, which is the shape `indexed`'s docstring
    calls the unanswerable question refusing.

    Entries are as `git ls-files --stage` prints them.

    `git rm -r --cached <root>` drops a gitlink from the index and leaves
    `.gitmodules` naming the path, and moving the root breaks the submodule's
    relative gitdir. Measured 2026-09-03: the switch exited 0 and `git
    status` in the moved root died with `fatal: not a git repository`.

    A sixth member of the class `frame/design.md`'s *What the switch touches* table
    enumerates — the table that says it is enumerated rather than fixed where
    a finding points, and then listed five.
    """
    try:
        done = subprocess.run(
            ["git", "-C", repo, "ls-files", "--stage", "--", optin.HOME],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=15,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return None, f"git ls-files could not be run ({exc})"
    if done.returncode != 0:
        return None, (done.stderr or "").strip() or (
            f"git ls-files exited {done.returncode}"
        )
    return [
        line
        # exempt from splitlines: git output
        for line in (done.stdout or "").splitlines()
        if line.startswith("160000")
    ], ""


def refusals(repo, home, shared, local, wanted):
    """Every reason not to switch, gathered before anything is written.

    The list is the class in `frame/design.md` *What the switch touches*, walked in
    order, rather than the guards a reader thinks of first. The switch
    stages nothing outside the root, so nothing outside it is guarded.
    """
    if not local:
        return ["the common git directory could not be resolved"]
    if optin.marked(shared) and optin.marked(local):
        return [both_roots(shared, local)]

    source = shared if wanted == LOCAL else local
    destination = local if wanted == LOCAL else shared
    found = []

    # The row this switch ends by writing is refused before anything moves
    # (#867): a `config.md` that will not read, or one holding two `Mode`
    # rows, would stop `write_row` after the folder had already gone.
    refused = mode_refusal(home)
    if refused:
        found.append(refused)

    gitlinks, unreadable = gitlinks_under_root(repo)
    if gitlinks is None:
        found.append(
            f"whether there is a submodule under {optin.HOME}/ could not be "
            f"read: {unreadable}. A gitlink does not survive the move, so the "
            "unanswerable question refuses — the direction `porcelain` and "
            "`indexed` already take."
        )
    elif gitlinks:
        found.append(
            f"there is a submodule under {optin.HOME}/:\n  "
            + "\n  ".join(gitlinks)
            + f"\nMoving the root breaks its relative gitdir, and `git rm -r "
            f"--cached {optin.HOME}` drops the gitlink while .gitmodules goes "
            "on naming the path. Deinit it or move it out of the root first."
        )

    if os.path.islink(source):
        found.append(
            f"{source} is a symbolic link, not the root itself. Moving it "
            "would move the link and leave the records where they are."
        )
    if os.path.isdir(source) and os.path.lexists(destination):
        found.append(
            f"{destination} already exists, and nothing here overwrites. "
            "Move or remove it first."
        )

    # Whether the root is already where this is trying to put it. A move
    # somebody already made by hand is the one state whose deletions are not
    # work in progress — see `indexed`.
    moved = os.path.isdir(destination) and not os.path.lexists(source)
    lines = [line for line in porcelain(repo, optin.HOME) if indexed(line, moved=moved)]
    if lines:
        found.append(
            "the tree is not clean under the path this would stage:\n  "
            + "\n  ".join(lines)
            + "\nCommit or stash them first. `git rm -r --cached` takes a "
            "staged edit out of the index and prints nothing about it, so a "
            "half-staged switch is worse than none."
        )

    config = config_path(home)
    if os.path.islink(config):
        found.append(f"{config} is a symbolic link, and the row is written there")
    elif os.path.isdir(config):
        found.append(f"{config} is a directory, and the row is written there")
    elif os.path.isfile(config):
        try:
            with open(config, encoding="utf-8", newline="") as handle:
                handle.read()
        except (OSError, ValueError) as exc:
            found.append(
                f"{config} could not be read ({exc}), and the row is written there"
            )
    return found


def switch(args, repo, home, shared, local, current, wanted):
    """Move the root, write the row, and stage the index; `.github/` is left
    alone, and the pull-request checks are `seal pr-checks`'s.

    In the order of `frame/design.md` *Order, and what a stopped run leaves*: the
    rename first, because it is the step that can fail for reasons outside
    this command and until it succeeds nothing has happened. Every step after
    it is idempotent, so `seal mode <the same mode>` finishes a stopped run —
    and so does a person who already ran the README's `mv` by hand.
    """
    source = shared if wanted == LOCAL else local
    destination = local if wanted == LOCAL else shared

    stop = refusals(repo, home, shared, local, wanted)
    if stop:
        for line in stop:
            print(line)
        print("\nNothing was moved.")
        return 1

    if wanted == SHARED:
        print(
            "Going to shared mode puts the records in the tree. Until you "
            f"commit, `git reset -- :/{optin.HOME}` and then "
            "`seal mode local` walk the whole thing back — the switch stages, "
            "and the guard refuses a switch over a staged change. The "
            "pathspec is there because a bare `git reset` unstages the whole "
            "index, and this guard has never looked outside that path. "
            "`:/` makes the path mean the same thing from any directory — a "
            "git pathspec is read from where you stand, and without it the "
            "command exits 0 having unstaged nothing when you are not at the "
            "root. Every command this file hands you to run carries it, for "
            "that reason. "
            "After the commit they are in the history, and taking "
            "them out of the tree later does not take them out of it."
        )
    else:
        print(
            "Going to local mode takes the records out of the tree. Every "
            "other clone loses them at the next pull — `seal export` here "
            "and `seal import` there is how a teammate gets a copy."
        )
    for line in porcelain(repo, optin.HOME):
        # `??` itself, not `indexed`. That function has three exceptions now
        # and only this one means untracked — reading its answer as the
        # question called a tracked, modified `config.md` untracked, in a
        # note whose whole subject is what the index can lose.
        if line[:2] == "??":
            print(
                f"note: {line[3:]} is untracked, so the index cannot lose it "
                "— it travels with the folder."
            )
    for path in other_worktrees(repo):
        print(
            f"note: {path} is another worktree of this clone. Until the "
            "commit reaches its branch it reads the root its own tree has, "
            "which is not the one this move leaves."
        )
    print("")

    moved = False
    if os.path.isdir(source):
        try:
            os.rename(source, destination)
        except OSError as exc:
            print(f"the root could not be moved: {exc}")
            print(
                "Nothing else has run. From the repository root, this does "
                "the move across filesystems:\n"
                f'  mv "{source}" "{destination}"\n'
                "then run this command again to finish."
            )
            return 1
        moved = True
        print(f"  moved {display(repo, source)} to {display(repo, destination)}")
    else:
        print(f"  {display(repo, destination)} is already the root")

    failed = write_row(destination, wanted)
    if failed:
        print(f"  the `{ROW_ITEM}` row was NOT written: {failed}")
    else:
        print(f"  wrote `| {ROW_ITEM} | {wanted} |` in {CONFIG}")

    if wanted == LOCAL:
        if tracked(repo, optin.HOME):
            done = subprocess.run(
                [
                    "git",
                    "-C",
                    repo,
                    "rm",
                    "-r",
                    "--cached",
                    "--quiet",
                    "--",
                    optin.HOME,
                ],
                capture_output=True,
                encoding="utf-8",
                errors="replace",
                timeout=30,
            )
            if done.returncode != 0:
                print(
                    f"  the records are still tracked: "
                    f"{(done.stderr or '').strip()}\n"
                    f"  Run `git rm -r --cached :/{optin.HOME}` yourself, or "
                    "this command again."
                )
            else:
                print(f"  staged the removal of {optin.HOME}/ from the tree")
        else:
            print(f"  nothing under {optin.HOME}/ was tracked")
        kind, text = workflow_at(repo)
        if kind == "plugin":
            print(f"  {left_workflow_line(text)}")
    else:
        # The return code, not the call. `git()` reads a failure as "" — and
        # `git add` exits non-zero for an ignore rule matching the root, or a
        # held `index.lock`. Measured 2026-09-03: the root moved into the
        # tree, nothing was staged, and the command printed `staged seal/`
        # and `Now commit`. The local direction has read this code since it
        # was written; this side had not.
        done = subprocess.run(
            ["git", "-C", repo, "add", "--", optin.HOME],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
        )
        if done.returncode != 0:
            print(
                f"  {optin.HOME}/ could NOT be staged: "
                f"{(done.stderr or '').strip()}\n"
                f"  A commit now would record nothing. An ignore rule "
                f"matching the root is the usual cause. Run "
                f"`git add -f :/{optin.HOME}` yourself, or this command again."
            )
        else:
            print(f"  staged {optin.HOME}/")
        if workflow_at(repo)[0] == "absent":
            print(
                "  no pull-request checks are installed: `seal pr-checks "
                f"install` writes {WORKFLOW}"
            )

    print("\nNow commit. The switch is what the commit records:\n  git commit")
    if moved and wanted == SHARED:
        print(
            f"Until then, `git reset -- :/{optin.HOME}` and then "
            "`seal mode local` puts it back — the switch stages, and the "
            "guard refuses a switch over a staged change. The pathspec is "
            "there because a bare `git reset` unstages the whole index."
        )
    return 0


def mode(args, cwd):
    repo, home, shared, local, current = resolve(cwd)
    if not home:
        if args.check:
            if not repo:
                # Not the same answer as "there is no root". A repository
                # that could not be resolved is a check that did not RUN, and
                # a gate that cannot tell reads exactly like an allow — the
                # shape issue #28 was opened on. `optin.repo_root` answers ""
                # for a timeout or a git that is not on PATH, and a shared
                # root committed beside a row saying `local` is what CI is
                # here to catch.
                print(
                    "no git repository could be resolved here, so the mode "
                    "was never read. This is not agreement and it is not a "
                    "disagreement — the check could not run."
                )
                return 1
            # A check that fails where there is nothing to check teaches
            # people to delete the check. A workflow pinned to this release
            # that outlived its root examines nothing on every step,
            # `unverified_check.py` included (`absent_root`), and this one has
            # nothing to add to that.
            print("no seal/ here, so nothing is declared and nothing can disagree.")
            return 0
        return no_root(repo, shared, local)

    wanted = args.mode
    if args.apply:
        kind, value = declared(home)
        if kind == "mode":
            wanted = value
        elif kind == "refused":
            print(
                f"{mode_refusal(home) or value}, so there is nothing to apply. "
                "Nothing was moved."
            )
            return 2
        else:
            named = (
                f"names `{value}`, which is not a mode"
                if kind == "unknown"
                else "is not declared"
            )
            print(f"the `{ROW_ITEM}` row {named}, so there is nothing to apply.")
            print(
                f"Write one in {display(repo, config_path(home))} —\n"
                f"  | {ROW_ITEM} | {LOCAL} |\n"
                f"or run `seal mode {LOCAL}` / `seal mode {SHARED}` to switch "
                "and write the row in one step."
            )
            return 1

    if not wanted:
        return mode_report(args, repo, home, shared, local, current)
    return switch(args, repo, home, shared, local, current, wanted)


# --- the release reminder ---------------------------------------------------


def check(cwd):
    repo, home, shared, local, mode = resolve(cwd)
    if not home:
        return no_root(repo, shared, local)
    if mode == "shared":
        # Never a failure. A release script runs this unconditionally, and a
        # shared-mode repository has nothing to be reminded about: the records
        # are in the commit range already.
        print("shared mode: the records are committed, so there is nothing to export.")
        return 0

    files, _ = root_files(home)
    now = work_item_digests(files)
    last = read_state(repo)
    if not last or not isinstance(last.get("items"), dict):
        print(
            f"{len(now)} work items here and no export yet — "
            "`seal export` writes the first copy."
        )
        return 0

    then = last["items"]
    changed = len({*now, *then}) - sum(
        1 for item in now if item in then and now[item] == then[item]
    )
    print(f"{changed} work items changed since the last export")
    return 0


# --- a change that belongs to no work item -----------------------------------


def no_work_item(args, cwd):
    """Record, for this session on the branch checked out in the worktree at
    `--root` or the working directory, that its change belongs to no work
    item, so `hooks/routing-edit-gate.py` lets its edits on that branch
    through. The session is `CLAUDE_CODE_SESSION_ID`'s, and the branch is
    resolved as the edit gate resolves it (`routing.worktree_branch`): the
    branch checked out, else the branch a paused rebase there names. Where
    the repository, the session or the branch is missing, nothing is written.
    The rule is `docs/the-routing-check.md` *The edit check*."""
    where = args.root or cwd
    repo = optin.repo_root(where)
    if not repo:
        print(f"seal: {where} is in no git repository, so nothing was recorded.")
        return 1
    session = os.environ.get(hooksession.SESSION_VARIABLE, "")
    if not routing.session_name(session):
        print(
            f"seal: {hooksession.SESSION_VARIABLE} names no session in this "
            "environment, so nothing was recorded. Run this from the session's "
            "own Bash tool."
        )
        return 1
    branch = routing.worktree_branch(repo)
    if not branch:
        print(
            f"seal: HEAD is detached in {repo}, so no branch can be recorded and "
            "nothing was. Check out a branch there first, then run this again."
        )
        return 1
    path = routing.record_no_work_item(optin.git_common_dir(repo), session, branch)
    if not path:
        print(f"seal: the record could not be written under {repo}'s git directory.")
        return 1
    print(
        f"recorded: this session's change on `{branch}` in {repo} belongs to no "
        f"work item ({path}), so its edits on that branch go ahead."
    )
    return 0


# --- the tools --------------------------------------------------------------


def tool_command(name, argv):
    """The command line that runs the script `TOOLS` names for `name` with
    `argv`: this interpreter, which `hooks/launch.py` held to the floor before
    this file was read, the script's path under the plugin, and the arguments
    as they were typed."""
    script = os.path.join(PLUGIN, *TOOLS[name][0].split("/"))
    return [sys.executable, script, *argv]


def hand_over(command):
    """Run `command` in place of this one and answer its exit code.

    On POSIX the process is replaced, as the `exec` of a `bin/` wrapper
    replaced it, so the script's signals and exit code are the command's.
    Windows has no replacement that keeps the exit code, so the script runs
    as a child and its code is returned, as a `.cmd` wrapper returned it."""
    if os.name == "nt":
        return subprocess.call(command)
    sys.stdout.flush()
    sys.stderr.flush()
    os.execv(command[0], command)


# --- entry point ------------------------------------------------------------


def main(argv=None, cwd=None):
    cwd = cwd or os.getcwd()
    argv = sys.argv[1:] if argv is None else list(argv)
    # A tool's arguments are its script's to read, `--help` among them, so
    # they are handed on before the parser below sees any of them.
    if argv and argv[0] in TOOLS:
        return hand_over(tool_command(argv[0], argv[1:]))
    parser = argparse.ArgumentParser(
        prog="seal",
        description="the plugin's commands: where this repository's seal/ "
        "root lives, how a copy of it travels between clones, and one "
        "subcommand for each tool",
    )
    sub = parser.add_subparsers(dest="command", required=True)
    for name, (_, said) in TOOLS.items():
        sub.add_parser(name, help=said, add_help=False)

    ex = sub.add_parser("export", help="write the root to a zip")
    ex.add_argument("--output", help="the zip's path, or a directory to put it in")
    ex.add_argument(
        "--check",
        action="store_true",
        help="print how many work items changed since the last export, and "
        "write nothing",
    )

    im = sub.add_parser("import", help="merge a zip's records in")
    im.add_argument("zip", help="the zip `seal export` wrote")
    im.add_argument(
        "--into",
        choices=("shared", "local"),
        help="which mode's root to write into, creating it. Default: the one "
        "in force, or local where neither exists",
    )
    im.add_argument(
        "--allow-other-repo",
        action="store_true",
        help="import although the manifest names a different remote",
    )
    # A flag of its own, not a second meaning for the one above. Typing
    # `--allow-other-repo` is saying *I have read both URLs and they are one
    # repository under two spellings*; a person whose git could not answer has
    # read neither and is saying something else (#111).
    im.add_argument(
        "--allow-unreadable-remote",
        action="store_true",
        help="import although the remote could not be read on one side or "
        "the other, so whether the zip came from this repository is unknown",
    )

    md = sub.add_parser(
        "mode", help="report the mode, or switch between shared and local"
    )
    md.add_argument(
        "mode",
        nargs="?",
        choices=MODES,
        help="the mode to switch to. With none, the mode is reported",
    )
    md.add_argument(
        "--check",
        action="store_true",
        help="report, write nothing, and exit 1 when the row and the folder "
        "disagree. This is what CI runs",
    )
    md.add_argument(
        "--apply", action="store_true", help="switch to whatever the `Mode` row says"
    )

    pc = sub.add_parser(
        "pr-checks",
        help="report, write or remove the workflow that checks pull requests "
        "against the committed root",
    )
    pc.add_argument(
        "action",
        nargs="?",
        choices=("install", "remove"),
        help="write .github/workflows/hygiene.yml pinned to this release, or "
        "take out the one this plugin wrote. With none, whether it is "
        "installed is reported",
    )

    nw = sub.add_parser(
        "no-work-item",
        help="record that this session's change on the branch checked out "
        "belongs to no work item, so its edits on that branch go ahead",
    )
    nw.add_argument(
        "--root",
        help="the worktree whose checked-out branch is recorded. Default: the "
        "working directory's",
    )

    args = parser.parse_args(argv)
    if args.command == "no-work-item":
        return no_work_item(args, cwd)
    if args.command == "pr-checks":
        return pr_checks(args, cwd)
    if args.command == "export":
        return check(cwd) if args.check else export(args, cwd)
    if args.command == "mode":
        # Three spellings of one answer, and any two together is a question
        # with two answers rather than a shorthand. Refused here rather than
        # resolved by precedence: a person who typed both meant one of them,
        # and this command moves directories.
        given = [
            name
            for name, on in (
                ("a mode", bool(args.mode)),
                ("--check", args.check),
                ("--apply", args.apply),
            )
            if on
        ]
        if len(given) > 1:
            parser.error(f"{' and '.join(given)} cannot be given together")
        return mode(args, cwd)
    return import_(args, cwd)


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
