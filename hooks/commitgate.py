"""The commit gate as git runs it: `pre-commit`, its `reference-transaction`
backstop, and `post-commit`'s notice (#692) and stamp (#975). Since work item
1792363231 `pre-commit` also refuses a `sealed` guarantee whose audited
commit the history does not hold (`guarantee_off_history`).

`hooks/git/*.py` are thin entry points into this module, so that a case can
drive one hook in-process and the stubs run the same code from a shell. What
each hook reads, and why each reading is the right one, is in those files'
docstrings; what is judged is `hooks/gate.py`'s.

Nothing here reads `GIT_DIR`. git does not export it to `pre-commit`,
`post-commit` or `post-checkout` (phase 1's M4, on 2.50.1), so every reading
asks `git rev-parse` in the working directory git gave the hook.

**A commit git makes for its own sequencer is not judged** (round 1 of #692,
🟡 7). `rebase --continue`, a reword, `cherry-pick --continue` and `revert
--continue` each commit through a child `git commit`, which hands both hooks
the author date and, for the first, skips `pre-commit`. Measured on 2.34.1,
2.39.5, 2.43.0 and 2.50.1, that child is the one commit whose starter is
another `git` process while a sequencer state is on disk. A commit a shell
starts during a paused rebase -- `--amend` at an `edit` stop, `--no-verify`
before `--continue` -- has a shell for its starter, and is judged. An alias
(`git -c alias.ci=commit ci`) is started by git too, so the state has to be
there as well. `GIT_REFLOG_ACTION` is no criterion for this either: the
rebase's children set it, and cherry-pick's and revert's do not.
"""

import hashlib
import importlib.util
import os
import subprocess
import time

import answers
import gate
import hooksession
import optin
import routing

# One empty file per commit `pre-commit` let through, under the worktree's own
# git directory, named for the commit it judged. `reference-transaction`
# removes it when the branch moves; one left behind by a commit that aborted
# after `pre-commit` (an empty message, a failing `commit-msg`) names a tree
# and a date nothing will commit again, and is pruned after a day.
JUDGED = "specseal-judged"
PRUNE_AFTER = 24 * 60 * 60

ZERO = set("0")


def _context(cwd, environ):
    """(top, common, session) for a hook running in `cwd`, or None when the
    hook has nothing to judge: no repository, a repository that does not opt
    in (S13), or no Claude session behind the command (P2)."""
    top = optin.repo_root(cwd)
    if not top:
        return None
    common = optin.git_common_dir(top)
    if not optin.home_at(top, common):
        return None
    session, _route = hooksession.session(common, environ)
    if not session:
        return None
    return top, common, session


def waived(cwd, session):
    """The arms this command waived: `-c specseal.waive=<arm>`, and the old
    bare word carried over from the Bash call this commit runs under (P3,
    round 1's 🟡 9). The ancestry is walked once, and only if an answer is
    there to match it."""
    out = set()
    # `config --get-all` exits 1 where no such key is set: no waiver, git's
    # ordinary no, not a failure.
    configured = gate.git(["config", "--get-all", "specseal.waive"], cwd) or ""
    for value in configured.splitlines():
        for word in value.replace(",", " ").split():
            if word in (gate.REVIEW, gate.PARITY):
                out.add(word)
    walked = []

    def args():
        if not walked:
            walked.append(hooksession.call_args())
        return walked[0]

    for arm, token in gate.TOKENS.items():
        if answers.given(session, token, args):
            out.add(arm)
    return out


def pressed(top, session):
    """True when the session's person pressed `automation`. Every way of not
    reading it is False, the answer from before it was read."""
    try:
        import worktree_consent

        return worktree_consent.automation_answered(top, session, "") is True
    except Exception:
        return False


def _git_process():
    """The `git commit` process this hook runs under, as a string; "" where it
    cannot be named the same way from both hooks.

    The stub `exec`s the interpreter, so on a POSIX system its parent is the
    `git commit` that ran the hook, and both hooks of one commit share it
    (measured on four gits by round 1's fix pass). Git for Windows runs each
    hook through its own `sh.exe`, whose pid differs per hook, so there the
    mark is keyed without it.
    """
    return "" if os.name == "nt" else str(os.getppid())


def _key(old, tree, date, process=None):
    # The process is round 1's 🟡 10: a commit that aborted after
    # `pre-commit` (an empty message, a failing `commit-msg`) left a mark for
    # the same HEAD, tree and date, and a later `--no-verify` commit with that
    # date took it. The later commit is another `git` process.
    old = "" if not old or set(old) <= ZERO else old
    process = _git_process() if process is None else process
    return hashlib.sha1(f"{old}\n{tree}\n{date}\n{process}".encode()).hexdigest()


# What git leaves under a worktree's git directory while a rebase, a
# cherry-pick or a revert is in progress there.
SEQUENCER = (
    "rebase-merge",
    "rebase-apply",
    "sequencer",
    "CHERRY_PICK_HEAD",
    "REVERT_HEAD",
)


def _process(pid):
    """(parent pid, command name) of process `pid`; (None, "") unreadable."""
    try:
        out = subprocess.run(
            ["ps", "-o", "ppid=,comm=", "-p", str(pid)],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=5,
        ).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return None, ""
    parent, _, comm = out.partition(" ")
    try:
        return int(parent), os.path.basename(comm.strip())
    except ValueError:
        return None, ""


def _sequencer_commit(cwd, commit=None):
    """True when git is making this commit for its own rebase, cherry-pick or
    revert: a sequencer state on disk, and the `git commit` running the hook
    started by another `git` process. Every way of not reading it is False,
    so the commit is judged; on Windows, where no `ps` answers, it always is.
    """
    git_dir = gate.git(["rev-parse", "--absolute-git-dir"], cwd) or ""
    if not git_dir or not any(
        os.path.exists(os.path.join(git_dir, name)) for name in SEQUENCER
    ):
        return False
    if commit is None:
        if os.name == "nt":
            return False
        commit = os.getppid()
    starter, _name = _process(commit)
    _parent, name = _process(starter)
    return name == "git"


def _judged_dir(cwd):
    # Outside a repository `rev-parse` exits non-zero: no directory, and no
    # mark is left or taken.
    git_dir = gate.git(["rev-parse", "--absolute-git-dir"], cwd) or ""
    return os.path.join(git_dir, JUDGED) if git_dir else ""


def _leave_mark(cwd, head, date):
    d = _judged_dir(cwd)
    # A tree git could not write leaves no mark, so the backstop judges.
    tree = gate.git(["write-tree"], cwd) or ""
    if not d or not tree or not date:
        return
    try:
        os.makedirs(d, exist_ok=True)
        cutoff = time.time() - PRUNE_AFTER
        for name in os.listdir(d):
            p = os.path.join(d, name)
            try:
                if os.stat(p).st_mtime < cutoff:
                    os.remove(p)
            except OSError:
                pass
        open(os.path.join(d, _key(head, tree, date)), "w", encoding="utf-8").close()
    except OSError:
        pass


def _take_mark(cwd, old, new, date):
    """True when `pre-commit` judged this update; the mark is used up."""
    d = _judged_dir(cwd)
    # `--verify --quiet` exits 1 for a name with no tree: no mark to take.
    tree = gate.git(["rev-parse", "--verify", "--quiet", f"{new}^{{tree}}"], cwd) or ""
    if not d or not tree:
        return False
    path = os.path.join(d, _key(old, tree, date))
    try:
        os.remove(path)
    except OSError:
        return False
    return True


def _refuse(stream, arms, top, cwd, session, backstop=False):
    branch = routing.current_branch(cwd)
    stream.write(
        gate.refusal(arms, top, branch, pressed(top, session), backstop) + "\n"
    )
    return 1


GUARANTEE_FILE = "guarantee.md"


def guarantee_off_history(cwd, head, paths):
    """The refusal's text where this commit stages a work item's
    `guarantee.md` reading one `Verdict:` of `sealed` whose `Target SHA`
    names a commit `head`'s history does not hold, on the branch the item's
    own `routing.md` declares; else None (work item 1792363231, `spec.md`
    S11 and S12).

    Both files are read from the index (`git show :<path>`), which is the
    commit git is about to make: `GIT_INDEX_FILE` names it for `-a` and for
    a pathspec commit as it does for the paths. The `; earlier run:` chain
    is not read, so a `sealed` that drew and went stale under a rebase is
    never stopped, and a commit on any other branch, a squash onto `main`
    among them, is not judged. `paths` is `pre_commit`'s one listing of the
    staged paths. `seal_stamp.py`, and through it `chain_check.py`, is
    loaded only once a staged path is shaped like a work item's guarantee,
    and `seal_stamp.GUARANTEE_PATH` decides which are. An unborn branch has
    no history to hold anything, and nothing is judged there."""
    if not head:
        return None
    shaped = [
        path
        for path in paths() or []
        if path.startswith(f"{routing.WORK_ITEMS}/")
        and path.endswith(f"/{GUARANTEE_FILE}")
    ]
    if not shaped:
        return None
    stamp = _stamp_module()
    chain = None
    branch = None
    for path in shaped:
        found = stamp.GUARANTEE_PATH.match(path)
        # A deleted guarantee is staged too, and `git show` finds none.
        text = gate.git(["show", f":{path}"], cwd) if found else None
        if text is None:
            continue
        chain = chain or stamp._chain_check()
        reader = chain.SHARED_READER
        verdicts = chain.verdicts_of(reader, text)
        if len(verdicts) != 1 or chain.verdict_word(verdicts[0][1]) != chain.SEALED:
            continue
        target = chain.target_of(reader, text)
        if target is None:
            continue
        rel = f"{routing.WORK_ITEMS}/{found.group(1)}/{routing.FILENAME}"
        declared = routing.parse(gate.git(["show", f":{rel}"], cwd) or "")
        if branch is None:
            branch = routing.current_branch(cwd)
        if not declared or not branch or declared["branch"] != branch:
            continue
        # A target that does not resolve exits 128 here, and one off the
        # branch exits 1: either way HEAD's history does not hold it.
        if gate.git(["merge-base", "--is-ancestor", target, head], cwd) is not None:
            continue
        short = gate.git(["rev-parse", "--short", head], cwd) or head
        return gate.guarantee_refusal(path, target, branch, short)
    return None


def _guarantee_refused(cwd, head, paths):
    """`guarantee_off_history`, and None where reading it failed: the
    refusal stops a commit on a fact it read, never on a reading that
    broke, and the pull request's check still refuses the same file."""
    try:
        return guarantee_off_history(cwd, head, paths)
    except (Exception, SystemExit):
        return None


def pre_commit(cwd, environ, stream):
    context = _context(cwd, environ)
    if context is None:
        return 0
    top, _common, session = context
    # An unborn branch exits non-zero: no HEAD is git's ordinary no.
    head = gate.git(["rev-parse", "--verify", "--quiet", "HEAD"], cwd) or ""
    listed = []

    def paths():
        # Read once for both readers. None where `git diff` failed, which
        # the parity arm asks about (#868).
        if not listed:
            listed.append(
                gate.lines(gate.git(["diff", "--cached", "--name-only"], cwd))
            )
        return listed[0]

    arms = gate.arms_missing(cwd, top, waived(cwd, session), paths, head=head)
    if arms:
        if not _sequencer_commit(cwd):
            return _refuse(stream, arms, top, cwd, session)
    else:
        refused = _guarantee_refused(cwd, head, paths)
        if refused and not _sequencer_commit(cwd):
            stream.write(refused + "\n")
            return 1
    _leave_mark(cwd, head, environ.get("GIT_AUTHOR_DATE", ""))
    return 0


def _commit_lines(lines, cwd):
    """The (old, new) pairs of this transaction that move a branch or a
    detached HEAD, once each."""
    # `symbolic-ref -q` exits 1 on a detached HEAD, which is the answer read.
    detached = not (gate.git(["symbolic-ref", "-q", "HEAD"], cwd) or "")
    seen, out = set(), []
    for line in lines:
        parts = line.split()
        if len(parts) != 3:
            continue
        old, new, ref = parts
        if set(new) <= ZERO:
            continue
        if not (ref.startswith("refs/heads/") or (ref == "HEAD" and detached)):
            continue
        if (old, new) in seen:
            continue
        seen.add((old, new))
        out.append((old, new))
    return out


def _paths_between(cwd, base, new):
    """A callable listing the paths the commit `new` carries over `base` --
    over nothing, for a root commit -- or answering None where git could not
    list them, which the parity arm asks about (#868)."""
    if base:
        args = ["diff", "--name-only", base, new]
    else:
        args = ["diff-tree", "--root", "-r", "--name-only", "--no-commit-id", new]
    return lambda: gate.lines(gate.git(args, cwd))


def reference_transaction(cwd, environ, state, lines, stream):
    date = environ.get("GIT_AUTHOR_DATE", "")
    if state != "prepared" or not date:
        return 0
    pairs = _commit_lines(lines, cwd)
    if not pairs:
        return 0
    context = _context(cwd, environ)
    if context is None:
        return 0
    top, _common, session = context
    for old, new in pairs:
        if _take_mark(cwd, old, new, date):
            continue
        base = "" if set(old) <= ZERO else old
        arms = gate.arms_missing(
            cwd, top, waived(cwd, session), _paths_between(cwd, base, new), head=base
        )
        if arms and not _sequencer_commit(cwd):
            return _refuse(stream, arms, top, cwd, session, backstop=True)
    return 0


def _notice_module():
    spec = importlib.util.spec_from_file_location(
        "specseal_implementer_notice",
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "implementer-notice.py"
        ),
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _stamp_module():
    spec = importlib.util.spec_from_file_location(
        "specseal_seal_stamp_for_post_commit",
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "skills",
            "verify",
            "scripts",
            "seal_stamp.py",
        ),
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def post_commit(cwd, environ, stream):
    """Two duties after a commit git made, each silent on every failure: the
    implementer notice, and since #975 the stamp — queued where the commit
    carries a `guarantee.md` reading `sealed` (`seal_stamp.queue_for_guarantee`
    says when), for the `Stop` hook to draw at the end of the session's turn."""
    context = _context(cwd, environ)
    if context is None:
        return 0
    top, common, session = context
    try:
        said = _notice_module().notify(cwd, session)
    except Exception:
        said = ""
    if said:
        stream.write(said + "\n")
    try:
        queued = _stamp_module().queue_for_guarantee(top, common, session)
    except (Exception, SystemExit):
        return 0
    for line in queued:
        stream.write(line + "\n")
    return 0
