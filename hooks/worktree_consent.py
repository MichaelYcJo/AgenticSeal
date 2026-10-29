#!/usr/bin/env python3
"""PostToolUse: a worktree creation that actually RAN is consent for the rest
of the session.

`hooks/worktree-guard.py` answered worktree creation with `ask` at every site
that reached it, so no path through it cost zero prompts and the cost grew with
the number of worktrees. Measured on the 0.9.1 release run (#237): six work
items on six branches needed six `git worktree add` calls, and the guard held
the run at all six. An unattended run reaches the first and stops there.

`[worktree-ok]` could not fix that, and `has_token`'s docstring says why -- the
token is written into the command by whoever issues it, so the model can write
it on the first attempt, and reading it as consent turns the guard off with
nobody asked. This record is the evidence the token is not. A tool call reaches
PostToolUse only after it ran, and a `git worktree add` runs only if the
guard's `deny` did not fire and its `ask` was answered yes -- so the record is
written AFTER the answer rather than before the question, which is the one
thing a command text cannot forge.

The record is an empty file at
`<git-common-dir>/agentic-worktree-consent/<session-id>`. Its existence is the
whole fact, the way `agentic-worktree-choice/`'s markers and `optin.py`'s
`agentic-scratch` are. Three things about it were decisions rather than
defaults:

  A THIRD directory, not a value in `agentic-worktree-choice/create/`. That
  marker is written by PreToolUse BEFORE the answer and means "the question was
  put", so sharing one file would let the guard read its own question back as
  consent -- the `has_token` failure one directory over. The two also fail in
  opposite directions: an unwritable choice marker counts as ALREADY ASKED,
  because one missed question beats a deny nothing gets past, while an
  unwritable consent record must count as NO CONSENT, because the alternative
  is a guard that switches itself off when a disk is read-only. One file cannot
  fail two ways.

  The COMMON git directory, not `--absolute-git-dir`. The record stands for
  "this session may split this clone into worktrees", and a linked worktree is
  the same clone. Reading it through `optin.git_common_dir` keeps one answer to
  that question in this tree rather than two.

  NO expiry, and no pruning either. A session id is already scoped to a
  session, so a time bound on top of it can only produce one new outcome: a
  session that outlives the bound is asked a second time, which is the failure
  this removes. The choice markers beside it are not pruned either.

This is its own file rather than a branch inside the guard because
`hooks/dispatch.py` hands every gate the same payload with no event name. One
file wired to both events would have to tell them apart by sniffing
`hook_event_name`, and contract rule 13 refuses a defence
that rests on a platform guarantee: where the field were absent the writer
would silently never record, which reads as "nobody ever consented" and costs
back every prompt this removes. A gate wired only to PostToolUse needs no
guarantee. The filename carries an underscore rather than the hyphen every
other gate here uses, because the guard imports it for the READ and a hyphen is
not importable -- the same reason `cmdline.py` and `optin.py` are spelled that
way.

The exit status of the creation is never read. What the record is about is the
approval, and the approval happened whether or not git then refused the path;
the retry after a failure is the worst moment to put the question again.

This module is also where the guard asks *what is consent*, and the record is
one of two answers. The other is the person's `automation` answer to the
routing question, read out of this session's own transcript
(`automation_answered`). An automation run creates its worktrees before any of
them has run, so the record cannot exist yet at the first one, and the answer
the person gave a minute earlier is the one fact on disk that the model did
not write: the harness wrote it from the click. `consent` reads both, record
first.

Failure is silent and one-directional. An unwritable `.git` leaves no record,
the next creation asks, and that is the direction a guard should fail in -- a
crash would be worse than the prompt it saves, because a hook that raises dies
with stdout empty, which is how a hook says "nothing to see here" (the guard's
own `_idle_min` says the same thing about a different crash).
"""

import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
# Reading a command line is no gate's property; `hooks/lib/cmdline.py` owns it, and
# `hooks/lib/optin.py` owns resolving a repository's git directories. Plain
# filenames mean `sys.modules` deduplicates both when `dispatch.py` runs
# several gates in one process.
#
# The reader is `hooks/lib/cmdline_base.py`, frozen at `86256492`, the one the
# worktree guard reads through (#689), so the clone a creation is filed under
# is the one the guard judged and the one the release base filed.
import cmdline_base as cmdline
import console
import optin

# The press reader is `hooks/lib/press.py`'s. `consent` reads
# `automation_answered` by this module's name for it, and the guard reads
# both names off this module.
from press import _clone_of as _clone_of
from press import automation_answered as automation_answered

# One empty file per session per clone. Its existence is the fact.
CONSENT_DIR = "agentic-worktree-consent"


def consent_path(top: str, session: str) -> str:
    """Where this session's record lives in this clone, or "" if nowhere.

    The id names a file, so a separator in a malformed one must not become a
    path escape: `../../escaped` put an empty file at a repository root once
    already, through the guard's other marker. `hooks/session-lease.py` and
    `already_asked` both reduce it the same way.

    "" is returned rather than a guess for every way of not having an answer --
    no repository, no session id, an id that is only separators, or a common
    git directory that could not be resolved. The read then says "no consent"
    and the write does nothing, which is the same direction both should fail
    in.
    """
    session = os.path.basename(str(session or ""))
    if not session or session in (".", ".."):
        return ""
    common = optin.git_common_dir(top)
    if not common:
        return ""
    return os.path.join(common, CONSENT_DIR, session)


def granted(top: str, session: str) -> bool:
    """True when this session already created a worktree in this clone.

    `isfile`, not `exists`: the record is a file, and a path that is a
    directory is not one. An unreadable path answers False, which is the
    direction a guard reads as "ask".
    """
    path = consent_path(top, session)
    return bool(path) and os.path.isfile(path)


def consent(top: str, session: str, transcript_path: str = "") -> str:
    """Which consent this session holds for splitting this clone, or "".

    `"record"` when a creation already ran (`granted`), `"answer"` when the
    person pressed `automation` (`automation_answered`), and "" for neither.
    The record is read first because it is one `stat`; the transcript is
    scanned only when there is no record, and once the first creation runs the
    writer below records it, so the scan is paid at most until then.
    """
    if granted(top, session):
        return "record"
    # Both call sites go through here, and `hooks/dispatch.py` skips a gate
    # that raises, which turns the guard's deny into no decision at all. So
    # every exception from the read is "no consent", the verdict from before
    # the answer was read.
    try:
        answered = automation_answered(top, session, transcript_path)
    except Exception:
        answered = False
    return "answer" if answered else ""


def record(top: str, session: str) -> bool:
    """Write the record. Silent on every failure; the caller ignores the answer.

    The return value exists for the tests, which need to tell "wrote it" from
    "could not" without inspecting a filesystem the failure case has made
    hostile on purpose.
    """
    path = consent_path(top, session)
    if not path:
        return False
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").close()
    except OSError:
        return False
    return True


def split_with_separators(command: str, windows=None):
    """`cmdline.split_segments_with_separators`, Windows separators carried across.

    Returns `([(operator, tokens), ...], parsed_cleanly)`. The operator is what
    joined each segment to the one before it, and reading a `cd` needs it: `&&`
    runs what follows where the `cd` arrived, `||` runs it only if the `cd`
    failed, which is where the shell already was.

    On Windows `\\` is the path separator, and POSIX-mode shlex reads it as an
    escape: `git -C C:\\proj\\repo switch topic` tokenizes to `C:projrepo` and
    the value naming the repository is gone. Doubling the backslashes first
    hands them back. The one form that comes out still doubled is a
    single-quoted path, where shlex unescapes nothing, and `apply_chdir`
    collapses those with `os.path.normpath` -- which is `ntpath` on Windows
    (measured).

    `windows` is overridable so the branch can be exercised from any platform:
    the failure it guards is invisible on the machines most sessions run on,
    and the value it destroys is the one that decides WHICH repository the
    command acts on.

    A `cd` argument is the same kind of value as a `-C` one, arrives the same
    way, and goes through this same doubling -- which is the whole of what the
    adapter has to say about it, since both then reach `apply_chdir` and its
    `normpath`.

    The worktree guard and this writer read every command through this one
    adapter (#868): the guard doubled the backslashes and the writer did not,
    so on Windows the two read different directories out of one command.
    """
    # RIDER: a UNC path in SINGLE quotes still loses the repository.
    # `git -C '\\\\server\\share\\repo' switch x` reaches `apply_chdir` with the
    # leading pair doubled: the line below doubles every backslash, shlex
    # unescapes nothing inside single quotes, and `ntpath.normpath` collapses
    # interior runs but not the leading pair that names the host. The guard
    # then finds no repository there and exits silently. The base hook handled
    # this form, so this one place went backwards; every other Windows form
    # (bare, double-quoted, relative) was compared against base and matches.
    #
    # A `cd` operand goes through this same doubling since that fix, so the
    # single-quoted UNC form loses the repository there too and the rider now
    # covers both. Read, not run: there is no Windows runner here. Since #868
    # the consent writer reads through this adapter too, so it files such a
    # creation nowhere, which is the record's own failure direction.
    if windows is None:
        windows = os.name == "nt"
    if windows:
        command = command.replace("\\", "\\\\")
    return cmdline.split_segments_with_separators(command)


def segment_cwd(tokens, cwd: str) -> str:
    """`cwd` with this segment's own `git -C` applied, or `cwd` unchanged.

    Takes the token list the walk produced, the same one the guard's
    `shape_of` read, so the verdict and the tree it is about come from one
    tokenization."""
    parsed = cmdline.parse_git(tokens)
    if not parsed:
        return cwd
    return cmdline.apply_chdir(cwd, parsed[2])


def place(tokens, wheres, cwd: str):
    """(shell directory, git directory) a segment of the frozen walk acts in.

    The one placement the worktree guard and this writer share (#868), so the
    clone a creation is filed under is the clone the guard judged it in.
    WHERES is the frozen walk's directories for the segment, and the first is
    where bash runs it: the walk lists the failure branch of a `||` first and
    the skipped live shells after it (`hooks/lib/cmdline_base.py`).

    Two destinations fall back to the session's own directory, which is the
    guard's answer from before it could read a `cd` at all:

      - one the reader could not compute (a variable, a glob, a subshell);
      - one that reads cleanly and holds no repository.

    The second was missed, and it is the more common of the two. `cd
    /no/such/dir ; git switch x` leaves the shell exactly where it started --
    `;` runs what follows whether the `cd` worked or not -- so the switch
    happens in the session's own tree, which is the tree another session may
    be sitting in. Judging the destination sent the guard to its `if not top`
    exit and it said nothing at all. This writer took the first entry that
    was not unresolved instead, which is the directory a `||` skips in `eval x
    ; cd A || git worktree add …`, and a directory that holds nothing in `cd
    <missing> ; git worktree add …`, where it filed no record at all
    (`frame/design.md` In 1 of work item 1791384157).

    The commit gate's text reading stopped on a target like this until #1027
    removed it, and the guard falls back instead. The two protected different
    things: a commit nobody judged is a commit nobody reviewed, while a guard
    that goes silent leaves a shared tree unguarded,
    and `docs/worktree-guard-spec.md` *Unknowns resolve conservatively* puts the
    cost of a wrong deny at one prompt against a wrong allow breaking another
    session's tree.

    A `git -C` that names no repository is NOT this case and keeps the guard's
    silence: git refuses that command itself, so no tree is touched.

    Which is why the segment's own `-C` is composed BEFORE the fallback is
    considered, and not after. Deciding first threw the destination away and
    then resolved a RELATIVE `-C` against the session directory instead:
    `cd ~/projects && git -C myrepo switch main` turned a real target
    repository into a path that does not exist, and the guard exited at
    `if not top` having said nothing. Returning both directories is what lets
    the guard classify against the tree it is about to judge.
    """
    where = wheres[0] if wheres else cwd
    here = cwd if isinstance(where, cmdline.Unresolved) else where
    target = segment_cwd(tokens, here)
    if here == cwd or optin.repo_root(target):
        return here, target
    return cwd, segment_cwd(tokens, cwd)


def creation_directory(command: str, cwd: str) -> str:
    """The directory a `git worktree add` in `command` acted on, or "".

    EVERY segment is read until the first creation, whatever comes before it:
    a creation anywhere in a command that ran is a creation that was approved.
    The guard's own PreToolUse walk judges the same first creation, and the
    first switch beside it in either order.

    Comments and heredoc bodies come out first, the pair the guard's
    `_judgment_text` uses, and for the same reason: this is a judgment read of
    what the shell EXECUTED, and neither is executed. There is no consent read
    here at all -- no token is involved on this side.

    The segment is placed by `place`, the guard's own placement, so a segment
    the reader could not place, or one whose directory holds no repository,
    is filed under the session's own directory, which is where the shell
    started. Getting that wrong lands the record in the wrong clone, so the
    next creation asks -- one prompt, on the side a guard should fail.

    Every reading here is `hooks/lib/cmdline_base.py`'s, the reader frozen at
    `86256492` that the guard reads through, so the creation found and the
    clone filed are the ones the guard judged (#689, #868).
    """
    text = cmdline.drop_heredoc_bodies(cmdline.drop_comments(command))
    items, _clean = split_with_separators(text)
    for tokens, wheres in cmdline.walk_directories(items, cwd):
        if cmdline.adds_a_worktree(tokens):
            return place(tokens, wheres, cwd)[1]
    return ""


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    # Wired to PostToolUse and nothing else, so the event is not inferred --
    # but a payload that NAMES the other event is refused rather than trusted.
    # Nothing sends one; a group edited by hand would.
    if data.get("hook_event_name", "PostToolUse") != "PostToolUse":
        return

    session = data.get("session_id", "")
    tool = data.get("tool_name", "")
    tool_input = data.get("tool_input") or {}
    cwd = data.get("cwd") or ""

    if tool in ("Agent", "Task"):
        # The same decision arriving through a different tool: the harness
        # creates the worktree at <repo>/.claude/worktrees/<name>, and this
        # call reaching PostToolUse means it was permitted.
        if str(tool_input.get("isolation", "")).lower() != "worktree":
            return
        where = cwd
    elif tool == "Bash":
        where = creation_directory(tool_input.get("command", "") or "", cwd)
    else:
        return

    top = optin.repo_root(where)
    if not top:
        return
    record(top, session)


if __name__ == "__main__":
    # A console that cannot encode what this prints kills it with stdout
    # empty, which is how a hook says "nothing to see here". `hooks/lib/console.py`
    # owns the reasoning and the three decisions behind these lines.
    console.to_utf8()
    main()
