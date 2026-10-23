"""The commit flow: a commit is judged inside git, in the worktree it lands in
(#692), and the PreToolUse reading of the command stands aside where git
decides (#942 rebuilt it from the code into this file).

The flow starts at `hooks/git/pre-commit.py`, which the stubs
`hooks/hook-install.py` writes run from this checkout, beside
`reference-transaction.py` and `post-commit.py`; all three call
`hooks/commitgate.py`. Each class is a scenario, and its accepting cases are
commits that land or a reading that stands aside, its refusing cases commits
git stops or a reading that judges. The oracle of a real-git case is what git
did, whether HEAD moved, and never what a reading said it would do.

The world is built once for the module and copied for each case:

  * `main`, an opted-in clone on `release`, which no declaration names, the
    session's directory, as the main checkout was in the recorded run;
  * `w`, a linked worktree of it on `feat`, which a routing declaration names;
  * `u`, a second opted-in clone, undeclared.

The copy points the linked worktree's two links at itself. The sample of
commands bash commits (S2) copies two sandboxes built once, one without the
stubs and one with them. Both copies hardlink the stubs from the template
instead of copying them, and the template runs each stub once when it is
built: macOS makes a newly created executable wait 150 to 200 ms the first
time it runs, and a copied stub is a new file, so every committing case paid
that for each of the three stubs (`_link_or_copy`).

A case about which commands the reading stands aside for is judged without
git, through `hooks/tokens.py#is_plain`; the real-git rows that stay show
the reading and git agree, and the work item's `phases/phase-5.md` names
them.
"""

import io
import json
import os
import shlex
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path

import pytest
from conftest import (
    SESSION_VARIABLES,
    ask_entries,
    census_case,
    load_hook_module,
    ps_names_the_parent_or_skip,
    q,
    symlink_or_skip,
    write_transcript,
)

TARGET = "hooks/git/pre-commit.py"

HOOKS = Path(__file__).resolve().parents[3] / "hooks"
sys.path.insert(0, str(HOOKS))
import commitgate  # noqa: E402  -- the plain names the hooks import
import gate  # noqa: E402
import githooks  # noqa: E402
import hooksession  # noqa: E402
import tokens  # noqa: E402

install_mod = load_hook_module("hook-install.py", "hook_install_for_the_commit_flow")

BASH = shutil.which("bash")
# The stubs are the subject of every case here, so each case installs them.
pytestmark = [
    pytest.mark.skipif(BASH is None, reason="no bash to run commands in"),
    pytest.mark.usefixtures("git_hooks_installed"),
]

SESSION = "s-commit"


def env(home, session=SESSION, **extra):
    """The environment a case's git or shell runs in: none of git's own
    variables and none of a session's, whatever ran the suite, then the
    case's HOME, an identity and the case's session."""
    e = {
        k: v
        for k, v in os.environ.items()
        if not k.startswith("GIT_") and k not in SESSION_VARIABLES
    }
    # USERPROFILE as well: Python's `expanduser` reads it on Windows and HOME
    # nowhere else, so a hook there looked for the session's transcript in
    # the runner's own profile and never read the press (#692).
    e.update(
        HOME=str(home),
        USERPROFILE=str(home),
        XDG_CONFIG_HOME=str(home / ".config"),
        GIT_CONFIG_NOSYSTEM="1",
        GIT_AUTHOR_NAME="x",
        GIT_AUTHOR_EMAIL="x@example.com",
        GIT_COMMITTER_NAME="x",
        GIT_COMMITTER_EMAIL="x@example.com",
    )
    if session:
        e["CLAUDE_CODE_SESSION_ID"] = session
    e.update(extra)
    return e


def g(d, *args, home, check=True, session=SESSION, **extra):
    return subprocess.run(
        ["git", "-C", str(d), *args],
        capture_output=True,
        encoding="utf-8",
        check=check,
        env=env(home, session, **extra),
        stdin=subprocess.DEVNULL,
        timeout=60,
    )


def clone(path, home, branch):
    path.mkdir(parents=True)
    g(path, "init", "-q", home=home, session="")
    g(path, "symbolic-ref", "HEAD", f"refs/heads/{branch}", home=home, session="")
    for key, value in (
        ("commit.gpgsign", "false"),
        # In the repository, so `env -i git commit` still has an identity and
        # reaches its hooks rather than dying before them.
        ("user.name", "x"),
        ("user.email", "x@example.com"),
    ):
        g(path, "config", key, value, home=home, session="")
    (path / "seal").mkdir()
    (path / "seal" / "README.md").write_text("root\n", encoding="utf-8")
    # A recorded mode, so `mode-gate.py` has nothing to say in `pre-bash`.
    (path / "seal" / "config.md").write_text(
        "# Repository config\n\n| Item | Value |\n|---|---|\n| Mode | shared |\n",
        encoding="utf-8",
    )
    (path / "f.py").write_text("a = 1\n", encoding="utf-8")
    g(path, "add", ".", home=home, session="")
    g(path, "commit", "-q", "-m", "init", home=home, session="")
    return path


def declare(worktree, branch, review="through the review chain"):
    d = worktree / "seal" / "specs" / "1790000000-x"
    d.mkdir(parents=True, exist_ok=True)
    (d / "routing.md").write_text(
        f"| Axis | Answer |\n|---|---|\n| Review | {review} |\n"
        f"| Destination | open the pull request |\n| Branch | {branch} |\n",
        encoding="utf-8",
    )


def _link_or_copy(src, dst):
    """`shutil.copytree`'s copy of one file of a template: a file git or a
    shell executes is hardlinked, every other file copied.

    A hardlink is the template's own file, whose first run the template paid
    (`_run_each_stub_once`), so a case's commit starts each stub at once. A
    write into a linked file would reach the template, so a case that changes
    a stub writes a new file and `os.replace`s it, as
    `hooks/hook-install.py#write_stubs` does; no case here writes one. On
    Windows `os.access` reads no execute bit and calls every file
    executable, so there every file is copied, as it was before; a file
    system that refuses a hardlink gets a copy too."""
    if os.name != "nt" and os.access(src, os.X_OK):
        try:
            os.link(src, dst)
            return dst
        except OSError:
            pass
    return shutil.copy2(src, dst)


def _write_anew(path, text):
    """Replace the file at PATH with a new file holding TEXT.

    Not a write over the old file. Git for Windows marks a worktree's `.git`
    file hidden, and Windows refuses to open a hidden file for writing with
    the flags `write_text` passes: every case's copy failed there with
    `PermissionError` (CI run 39866987196). A new file also never writes
    through a hardlink into the template (`_link_or_copy`)."""
    path.unlink()
    path.write_text(text, encoding="utf-8")


def _copy_template(template, root):
    shutil.copytree(template, root, symlinks=True, copy_function=_link_or_copy)


def _run_each_stub_once(repo, home):
    """Run each stub REPO's installer wrote, once, so the template pays the
    first run of each new executable and every hardlinked copy finds it
    paid. With no session variable and no lease each stub leaves before
    Python. Not on Windows, where every file is copied (`_link_or_copy`)."""
    if os.name == "nt":
        return
    for hook in githooks.HOOKS:
        subprocess.run(
            [str(repo / ".git" / "hooks" / hook)],
            cwd=str(repo),
            capture_output=True,
            check=True,
            env=env(home, session=""),
            stdin=subprocess.DEVNULL,
            timeout=60,
        )


@pytest.fixture(scope="module")
def _world_template(tmp_path_factory):
    """The world, built once for the module with the stubs installed and
    each run once."""
    base = tmp_path_factory.mktemp("commit-world")
    home = base / "home"
    home.mkdir()
    main = clone(base / "main", home, "release")
    g(
        main,
        "worktree",
        "add",
        "-q",
        str(base / "w"),
        "-b",
        "feat",
        home=home,
        session="",
    )
    declare(base / "w", "feat")
    u = clone(base / "u", home, "main")
    with pytest.MonkeyPatch.context() as patched:
        patched.delenv("SPECSEAL_HOOK_INSTALL", raising=False)
        for r in (main, u):
            assert install_mod.install(str(r), "installer")
    for r in (main, u):
        _run_each_stub_once(r, home)
    return base


class World:
    """A copy of the module's world under one case's directory."""

    def __init__(self, template, tmp_path):
        self.tmp = tmp_path
        root = tmp_path / "world"
        _copy_template(template, root)
        self.home, self.main, self.w, self.u = (
            root / "home",
            root / "main",
            root / "w",
            root / "u",
        )
        # A linked worktree and its clone name each other by absolute path,
        # so the copy points both links at itself.
        link = self.main / ".git" / "worktrees" / "w"
        _write_anew(self.w / ".git", f"gitdir: {link.as_posix()}\n")
        _write_anew(link / "gitdir", f"{(self.w / '.git').as_posix()}\n")

    def head(self, d):
        return g(d, "rev-parse", "HEAD", home=self.home, session="").stdout.strip()

    def change(self, d, name="f.py", text=None):
        p = Path(d) / name
        p.write_text(
            text or (p.read_text(encoding="utf-8") if p.exists() else "") + "b = 2\n",
            encoding="utf-8",
        )
        g(d, "add", name, home=self.home, session="")

    def sh(self, command, cwd=None, session=SESSION, **extra):
        return subprocess.run(
            [BASH, "-c", command],
            cwd=str(cwd or self.main),
            capture_output=True,
            encoding="utf-8",
            env=env(self.home, session, **extra),
            stdin=subprocess.DEVNULL,
            timeout=60,
        )


@pytest.fixture
def world(_world_template, tmp_path):
    return World(_world_template, tmp_path)


def as_the_tool_spells_it(command):
    """The `-c` string the Bash tool hands its shell for COMMAND: the command
    inside `eval '…'`, with more after it (`pwd -P` into a file, in the
    harness).

    The more-after-it is what keeps the shell alive. bash 5.1 and later
    replace a `-c` shell with the last command of its list, so `bash -c
    "$COMMAND"` holds the command in no process by the time git's hook walks
    up to `claude`, and an answer `hooks/answers.py` can only give to the
    call whose argv carries it is given to nobody. macOS's bash 3.2 does not
    do that, so both cases that model a call that way passed there and
    failed on ubuntu's 5.2 (#692, after the chain: CI run 36965695916). The
    harness's own string cannot be replaced, because `eval` is not its last
    command; the argv `ps` shows for it is the one
    `tests/conftest.py#shell` records."""
    return f"eval {q(command)} < /dev/null && pwd -P >/dev/null"


def press(world):
    projects = world.home / ".claude" / "projects"
    write_transcript(projects, SESSION, ask_entries(world.main))


def fake_claude(world):
    """A shell named `claude`, so the hook's ancestry has one.

    A symlink to bash, executed through its own name: `ps` then names the
    process `claude` (its path, on macOS). Not `sh`, because macOS's `/bin/sh`
    is a launcher that re-executes another shell under another name; and not a
    copy, because macOS kills a copied system binary on launch (measured:
    exit 137)."""
    d = world.tmp / "bin"
    d.mkdir()
    symlink_or_skip(BASH, d / "claude")
    return d / "claude"


def lease_then(world, body):
    """A `claude` process that writes its own lease, then runs BODY."""
    leases = world.main / ".git" / "specseal-leases"
    # `; exit $?` keeps the shell from exec-ing the last command in its own
    # place, which would take the `claude` process out of the ancestry.
    return (
        f"mkdir -p {q(leases)} && printf '{{\"pid\": %s}}' $$ > {q(leases / SESSION)}"
        f" && {body}; exit $?"
    )


def under_shells(body, shells):
    """BODY run by SHELLS bash processes nested one inside the next, each
    kept alive by `; exit $?` so none is replaced by what it runs."""
    for _ in range(shells):
        body = f"{q(BASH)} -c {q(body + '; exit $?')}"
    return body


def as_claude(world, claude, body):
    """BODY run by the `claude` shell at CLAUDE after it writes its lease,
    with no session variable exported."""
    return subprocess.run(
        [str(claude), "-c", lease_then(world, body)],
        cwd=str(world.main),
        capture_output=True,
        encoding="utf-8",
        env=env(world.home, session=""),
        stdin=subprocess.DEVNULL,
        timeout=60,
    )


def group(world, name, command, call):
    """One dispatcher group for one Bash call, as the harness runs it."""
    payload = {
        "tool_name": "Bash",
        "tool_input": {"command": command},
        "cwd": str(world.main),
        "session_id": SESSION,
        "tool_use_id": call,
    }
    subprocess.run(
        [sys.executable, str(HOOKS / "dispatch.py"), name],
        input=json.dumps(payload),
        capture_output=True,
        encoding="utf-8",
        env=env(world.home),
        check=True,
        timeout=60,
    )


def as_a_call(world, command):
    """COMMAND as the Bash tool runs it: a shell of its own, carrying the
    command in its argv for as long as the command runs, below a process
    named `claude`."""
    claude = world.tmp / "bin" / "claude"
    if not claude.exists():
        fake_claude(world)
    return subprocess.run(
        [str(claude), "-c", f'{q(BASH)} -c "$CALL_COMMAND"; exit $?'],
        cwd=str(world.main),
        capture_output=True,
        encoding="utf-8",
        env=env(world.home, CALL_COMMAND=as_the_tool_spells_it(command)),
        stdin=subprocess.DEVNULL,
        timeout=60,
    )


def pre_bash(world, command, cwd):
    """The PreToolUse group's decision for COMMAND run in CWD: `silent`,
    `deny` or `ask`."""
    payload = {
        "tool_name": "Bash",
        "tool_input": {"command": command},
        "cwd": str(cwd),
        "session_id": SESSION,
    }
    out = subprocess.run(
        [sys.executable, str(HOOKS / "dispatch.py"), "pre-bash"],
        input=json.dumps(payload),
        capture_output=True,
        encoding="utf-8",
        env=env(world.home),
        timeout=60,
    ).stdout
    if not out.strip():
        return "silent"
    return (json.loads(out).get("hookSpecificOutput") or {}).get(
        "permissionDecision", "silent"
    )


# The known limits a case below rests on where it skips, as
# `docs/the-commit-gate-inside-git.md` *Known limits of the commit gate
# inside git* states them. The first two are the code's own `os.name == "nt"`
# branches (`hooks/commitgate.py#_sequencer_commit`, `#_git_process`), so
# their cases skip on the same test; the last two rest on `ps`, and their
# cases ask it (`conftest.py#ps_names_the_parent_or_skip`). #692's Windows
# pass is what found each case red on `windows-latest`.
NO_SEQUENCER_COMMIT = (
    "known limit: on Windows no commit counts as the sequencer's, so the "
    "sequencer's own commit is judged"
)
MARK_WITHOUT_PROCESS = (
    "known limit: on Windows the backstop's mark is keyed without the "
    "`git commit` process"
)
OLD_SPELLING_NEEDS_PS = (
    "known limit: the old spelling waives only where the hook can find the call's shell"
)
LEASE_NEEDS_PS = (
    "known limit: the lease names the session only where the hook can find "
    "its `claude` ancestor"
)


# --- S2: the commands bash commits ------------------------------------------
#
# Rows of the text readers' corpora, written out: name, subgroup and command,
# with `{W}` the declared clone and `{U}` an undeclared one. The hook judges
# inside git, in the worktree the commit lands in, so the text's shape is not
# what it sees; what a row can change for it is where the commit lands, the
# environment the hook inherits and the processes above it. So the rows are
# one of each such kind, and one of every subgroup work item 1791876666
# sampled: a commit into `main` and one into `u`; the session found through
# the variable and, under `env -i`, through the lease, directly and below a
# child shell; `exec`, a pipeline, a child shell, a subshell, a substitution,
# an `eval`, a redirected stdin; and `LD_PRELOAD`. Every row is one whose bare
# run commits into `main` or `u` on each leg, save the three named limits S2
# skips on Windows, and is built from bash, git and tools the stock macOS,
# ubuntu and Git for Windows images all carry; GNU `timeout` is not one. A
# row that commits nowhere undeclared fails S2 rather than skipping.
ROWS = {
    "ns: measured: a body line equal to the delimiter ends it early": (
        "ns: measured",
        "cat > note.md <<'EOF'\nquoted:\nEOF\ngit commit -m x\nEOF",
    ),
    "ns: r1: do -C w, then $'…'": (
        "ns: r1",
        "for d in a; do git -C '{W}' commit -m x; done; echo $'it\\'s'; "
        "git commit -m x",
    ),
    "ns: r2: control, bash reads stdin": (
        "ns: r2",
        "bash <<'EOF'\ngit commit -m x\nEOF",
    ),
    "ns: r3: an invalid name prefix": ("ns: r3", "a.b=1 cd '{W}' ; git commit -m x"),
    "shape: exec": ("shape: wrapped", "exec git commit -m x"),
    "shape: stdbuf": ("shape: wrapped", "stdbuf -oL git commit -m x"),
    "shape: env -i": ("shape: wrapped", "env -i git commit -m x"),
    "shape: a subshell in a body": (
        "shape: reserved",
        "for d in a; do ( git commit -m x ); done",
    ),
    "handed: bash -c": ("handed: HANDED", "bash -c 'git commit -m x'"),
    "handed: env -iS, a cluster": ("handed: HANDED", "env -iS 'git commit -m x'"),
    "handed: $( )": ("handed: SUBSTITUTED", "echo $(git commit -m x)"),
    "handed: <<<x git": ("handed: REDIRECTED", "<<<x git commit -m x"),
    "handed: a function body": ("handed: EVALS", "f() { eval 'git commit -m x'; }; f"),
    "position: followed by 2>&1 | tail": ("position", "git commit -m x 2>&1 | tail -1"),
    "#686: builtin cd": ("#686", "builtin cd {U} && git commit -m x"),
    "#686 ;: pushd": ("#686 ;", "pushd {U} >/dev/null ; git commit -m x"),
}

# A row whose bare run lands only in the declared clone: S2 has nothing to
# assert for it, and fails naming it rather than skipping.
VACUOUS = ("ns: r3", "cd '{W}' ; git commit -m x")


def _sandbox(base, with_hooks, home):
    """main (undeclared), w (declared) and u (undeclared), separate clones,
    each with a staged change, logging nothing: HEAD is the oracle."""
    for name in ("main", "w", "u"):
        d = clone(base / name, home, "release" if name != "w" else "feat")
        if name == "w":
            declare(d, "feat")
        (d / "f.py").write_text("a = 2\n", encoding="utf-8")
        g(d, "add", "f.py", home=home, session="")
        if with_hooks:
            assert install_mod.install(str(d), "installer")
            _run_each_stub_once(d, home)


@pytest.fixture(scope="module")
def _sandboxes(tmp_path_factory):
    """`bare` and `hooked`, built once for the module, and each clone's HEAD
    in each, which every copy shares."""
    base = tmp_path_factory.mktemp("commit-sandboxes")
    home = base / "home"
    home.mkdir()
    with pytest.MonkeyPatch.context() as patched:
        patched.delenv("SPECSEAL_HOOK_INSTALL", raising=False)
        for kind in ("bare", "hooked"):
            _sandbox(base / kind, kind == "hooked", home)
    heads = {
        (kind, name): g(
            base / kind / name, "rev-parse", "HEAD", home=home, session=""
        ).stdout
        for kind in ("bare", "hooked")
        for name in ("main", "w", "u")
    }
    return base, heads


def _as_a_session(base, repos):
    """The argv that runs `$CORPUS_COMMAND` the way the harness runs a Bash
    call: a process named `claude` holding a lease in every clone, and the
    command in a shell of its own below it.

    The shell of its own matters: a fork of a shell named `claude` is named
    `claude` too, so a subshell in the command would be the nearest `claude`
    and its pid would match no lease. The harness's own shell is a child of
    `claude` with another name, which is what this gives. The variable is
    exported as well; `env -i` is what takes it away, and the lease is what
    is left then (S9)."""
    claude = base / "claude"
    symlink_or_skip(BASH, claude)
    writes = "".join(
        f"mkdir -p {q(d / '.git' / 'specseal-leases')}"
        f" && printf '{{\"pid\": %s}}' $$ > "
        f"{q(d / '.git' / 'specseal-leases' / SESSION)}\n"
        for d in repos.values()
    )
    return [str(claude), "-c", writes + f'{q(BASH)} -c "$CORPUS_COMMAND"\nexit $?']


ROW_BOUND = 20


def _run_bounded(argv, *, cwd, env, timeout):
    """Run ARGV to its end or to TIMEOUT; True when it ended on its own.

    Not `subprocess.run(..., capture_output=True, timeout=…)`, which bounds
    the direct child alone: a row's shell runs below the `claude` one, so a
    row that never ends (the corpus's `until false` did not, before it got
    its `break`) outlived the kill. On POSIX it ran on, an orphan committing
    forever; on Windows `run` reads the pipes to their end after the kill,
    the orphan held them, and the windows-latest leg hung with no case named
    (#692, after the chain: CI run 36965695916). So nothing here is a pipe,
    and on POSIX the whole session the row started is ended, whether it
    ended on its own or not. Windows has no group kill without a job object,
    so there the direct child is ended and a row that did not end is still a
    failure that names itself."""
    group = os.name != "nt"
    proc = subprocess.Popen(
        argv,
        cwd=cwd,
        env=env,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=group,
    )
    try:
        proc.wait(timeout=timeout)
        ended = True
    except subprocess.TimeoutExpired:
        ended = False
    finally:
        if group:
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except (ProcessLookupError, PermissionError):
                pass
        else:
            proc.kill()
        proc.wait()
    return ended


def _run_row(tmp_path, sandboxes, kind, command):
    """The clones COMMAND committed into, run as a session's Bash call in a
    copy of the KIND sandbox."""
    template, heads = sandboxes
    base = tmp_path / kind
    _copy_template(template / kind, base)
    home = tmp_path / "home"
    home.mkdir(exist_ok=True)
    repos = {name: base / name for name in ("main", "w", "u")}
    text = command.replace("{W}", str(repos["w"])).replace("{U}", str(repos["u"]))
    ended = _run_bounded(
        _as_a_session(base, repos),
        cwd=str(repos["main"]),
        env=env(home, CORPUS_COMMAND=as_the_tool_spells_it(text)),
        timeout=ROW_BOUND,
    )
    assert ended, (
        f"the row did not end within {ROW_BOUND} s, so what it committed is "
        f"not an answer: {command!r}"
    )
    return {
        name
        for name, d in repos.items()
        if g(d, "rev-parse", "HEAD", home=home, session="").stdout != heads[kind, name]
    }


# `docs/the-commit-gate-inside-git.md` *Known limits of the commit gate
# inside git*. `stdbuf` exports `LD_PRELOAD` as an MSYS path; Git for Windows' `sh`
# reads it as a list split at `:`, dies loading `C`, and git commits as if
# every hook had passed (#692's Windows pass, CI run 37013783175, traced).
NO_HOOK_UNDER_LD_PRELOAD = (
    "known limit: on Windows a command that exports LD_PRELOAD runs no git "
    "hook, and the PreToolUse reading judges it instead"
)

# #692's Windows pass, beside S9's emptied-environment case: Git for Windows'
# `env -i` cannot find `git` on a `;`-separated PATH, so the row commits
# nowhere there.
NO_GIT_UNDER_ENV_I = (
    "known limit: on Windows `env -i` finds no git on the emptied PATH, so "
    "the row commits nowhere"
)

# A limit of the row, not of the gate. The `#686` rows write `{U}` unquoted,
# so on Windows bash takes the backslashes out of the path, the `cd` fails,
# and `&&` runs no commit; the `;` forms commit into `main` instead (PR #939's
# CI run 38477955404).
NO_CD_INTO_AN_UNQUOTED_PATH = (
    "known limit of the row: on Windows bash strips the backslashes of the "
    "unquoted path, so the cd fails and && runs no commit"
)

NOT_A_COMMIT = "commits into no undeclared repository without the hooks"


def _lands_nothing_undeclared(tmp_path, sandboxes, name, subgroup, command):
    """S2 for the row NAME. A row whose bare run commits into neither `main`
    nor `u` asserts nothing, and is a failure naming it."""
    if os.name == "nt" and command.startswith("stdbuf "):
        pytest.skip(NO_HOOK_UNDER_LD_PRELOAD)
    if os.name == "nt" and command.startswith("env -i"):
        pytest.skip(NO_GIT_UNDER_ENV_I)
    if os.name == "nt" and subgroup == "#686" and "{U}" in command:
        pytest.skip(NO_CD_INTO_AN_UNQUOTED_PATH)
    bare = _run_row(tmp_path, sandboxes, "bare", command)
    undeclared = bare & {"main", "u"}
    assert undeclared, (
        f"{name!r} {NOT_A_COMMIT} (it landed in {sorted(bare)}), so it "
        "asserts nothing: put another row of its subgroup in ROWS"
    )
    hooked = _run_row(tmp_path, sandboxes, "hooked", command)
    assert not (hooked & undeclared), (name, sorted(hooked))


# #748. One window is ten of the test loop's 0.1 s periods, so a loop still
# running touches the marker in every window. The deadline is five windows
# after the bound, and an orphaned loop lives at least ten seconds from its
# start, so a loop the group kill missed is still touching when it falls,
# and a loaded machine only slows the loop, which lengthens its life.
GONE_WINDOW = 1.0
GONE_DEADLINE = 5.0


def _stays_gone(marker, *, since):
    """Whether `marker`, unlinked at the start of a window, is still absent
    at its end in some window before `GONE_DEADLINE` after `since`.

    Polled rather than slept once: a fixed half second after the bound
    failed on a loaded machine with nothing wrong (#748). Unlinking again at
    each window is what makes a `touch` already in flight when the group was
    killed harmless: it can bring the marker back once, never twice."""
    while time.monotonic() - since < GONE_DEADLINE:
        marker.unlink(missing_ok=True)
        time.sleep(GONE_WINDOW)
        if not marker.exists():
            return True
    return False


class Test_a_commit_is_judged_in_the_worktree_it_lands_in:
    """S1 and S2 of #692: where a commit lands decides, never the command's
    text."""

    @pytest.mark.rule("judged-inside-the-commit")
    def test_accepts_a_commit_cd_takes_into_the_declared_worktree(self, world):
        """Rows 1 and 2 of 1790644505's table: `cd <W> && …` then a commit
        after a heredoc or after `;`. 0.15.7 asked the person both times,
        naming the main checkout; the commit lands in the declared worktree,
        and git says so."""
        (world.w / "CHANGES.md").write_text("x\n", encoding="utf-8")
        before = (world.head(world.main), world.head(world.w))
        first = world.sh(
            f"cd {q(world.w)} && python3 - <<'EOF'\n"
            "p = 'CHANGES.md'; open(p, 'a').write('entry\\n')\n"
            "EOF\n"
            "git add CHANGES.md && git commit -q -m 'docs: entry'"
        )
        assert first.returncode == 0, first.stderr
        second = world.sh(
            f"cd {q(world.w)} && grep -c nothing CHANGES.md ; "
            "echo more >> CHANGES.md && git add CHANGES.md && git commit -q -m 'docs: pin'"
        )
        assert second.returncode == 0, second.stderr
        assert world.head(world.main) == before[0]
        assert world.head(world.w) != before[1]
        assert gate.HEADER not in first.stderr + second.stderr

    def test_accepts_a_patch_whose_body_only_names_a_commit(self, world):
        """Row 4: 0.15.7 answered `UNREADABLE_CONSTRUCT`; nothing here
        commits."""
        before = (world.head(world.main), world.head(world.w))
        # The path with forward slashes, as a Python literal. A Windows path's
        # backslashes were read as `\U…`, and escaping them did not survive:
        # Git for Windows' bash halves a doubled backslash in its `-c` argument
        # (#692's Windows pass, CI run 37014766992).
        second = repr(f"cd {world.main.as_posix()}; git commit -m y")
        got = world.sh(
            f"cd {q(world.w)} && python3 - <<'EOF'\n"
            f"for c in ['git commit -m x', {second}]:\n"
            "    print(c)\nEOF"
        )
        assert got.returncode == 0, got.stderr
        assert (world.head(world.main), world.head(world.w)) == before
        assert gate.HEADER not in got.stderr

    @pytest.mark.rule("judged-inside-the-commit")
    def test_refuses_a_commit_a_heredoc_ending_early_makes_in_the_main_checkout(
        self, world
    ):
        """Row 3: the body's own `EOF` line ended the heredoc, so the commit
        became a real command line in the session's directory. That is a
        real commit into an undeclared checkout, and it is the one stop
        kept."""
        world.change(world.main)
        before = world.head(world.main)
        got = world.sh(
            f"cat > {q(world.tmp / 'issue.md')} <<'EOF'\nquoted:\nEOF\n"
            "git add f.py && git commit -q -m 'stray'\nEOF"
        )
        assert world.head(world.main) == before
        assert gate.HEADER in got.stderr
        assert f"No review is recorded for this cycle in {world.main}," in got.stderr

    @pytest.mark.rule("judged-inside-the-commit")
    @pytest.mark.parametrize("name", sorted(ROWS))
    def test_refuses_each_row_bash_commits_into_an_undeclared_repository(
        self, tmp_path, _sandboxes, name
    ):
        """M6's oracle as a case: where bash commits into `main` or `u` with
        no hooks, the same command with the hooks lands nothing there. The
        base's verdict is not asked. Of what the file holds, only these rows
        put a shell between `claude` and an emptied environment's `git`, so
        only they need the lease walk to climb past the call's shell."""
        subgroup, command = ROWS[name]
        _lands_nothing_undeclared(tmp_path, _sandboxes, name, subgroup, command)

    def test_refuses_a_row_that_commits_nowhere_undeclared(self, tmp_path, _sandboxes):
        """S3 of work item 1791876666: a row whose bare run lands only in the
        declared clone, put through S2, fails naming itself, where it used to
        skip after building its sandbox."""
        try:
            _lands_nothing_undeclared(tmp_path, _sandboxes, "vacuous", *VACUOUS)
        except AssertionError as failed:
            assert NOT_A_COMMIT in str(failed), failed
        except pytest.skip.Exception:
            pytest.fail("a row that commits nowhere undeclared was skipped")
        else:
            pytest.fail("a row that commits nowhere undeclared passed")

    def test_refuses_a_row_that_does_not_end_within_its_bound(self, tmp_path):
        """The bound S2's runner leans on, held without a row: a shell that
        starts a loop of its own and outlives the bound is reported as not
        ended, within the bound and not after the loop, and on POSIX the loop
        goes with it. The loop is finite, so where nothing ends it, on
        Windows, it is gone ten seconds later rather than at the end of the
        job."""
        alive = tmp_path / "alive"
        loop = f"for i in $(seq 1 100); do touch {q(alive)}; sleep 0.1; done"
        started = time.monotonic()
        ended = _run_bounded(
            [BASH, "-c", f"{q(BASH)} -c {q(loop)}; exit $?"],
            cwd=str(tmp_path),
            env=dict(os.environ),
            timeout=1,
        )
        assert not ended
        bound = time.monotonic()
        assert bound - started < 8, "the bound waited for the loop"
        if os.name != "nt":
            assert _stays_gone(alive, since=bound), "the row's loop outlived the bound"


class Test_a_commit_with_no_session_behind_it:
    """P2, S9 and S13 of #692: a commit nobody's session made is a person's
    own and lands; a session the variable does not name is found through
    its lease, and that commit is judged."""

    @pytest.mark.rule("a-persons-own-commit")
    def test_accepts_a_commit_with_no_variable_and_no_lease(self, world):
        """P2, answer (a)."""
        world.change(world.main)
        before = world.head(world.main)
        g(world.main, "commit", "-q", "-m", "mine", home=world.home, session="")
        assert world.head(world.main) != before

    def test_accepts_a_commit_whose_only_lease_names_another_pid(self, world):
        leases = world.main / ".git" / "specseal-leases"
        leases.mkdir()
        (leases / "someone").write_text('{"pid": 1}', encoding="utf-8")
        world.change(world.main)
        before = world.head(world.main)
        g(world.main, "commit", "-q", "-m", "mine", home=world.home, session="")
        assert world.head(world.main) != before

    @pytest.mark.parametrize("how", ["scratch", "no root"])
    def test_accepts_a_commit_in_a_clone_that_opted_out(self, world, how):
        """S13: the stub in a scratch clone or one with no `seal/` root is
        silent, and the commit lands."""
        if how == "scratch":
            (world.main / ".git" / "specseal-scratch").write_text("", encoding="utf-8")
        else:
            shutil.rmtree(world.main / "seal")
        world.change(world.main)
        before = world.head(world.main)
        got = g(world.main, "commit", "-q", "-m", "x", home=world.home)
        assert world.head(world.main) != before
        assert got.stderr == ""

    def test_accepts_no_session_in_python_either(self, world):
        """The stub leaves before Python for P2; the entry point says the
        same thing on its own, for a stub an older plugin wrote."""
        world.change(world.main)
        environ = env(world.home, session="")
        assert commitgate.pre_commit(str(world.main), environ, io.StringIO()) == 0

    def test_accepts_two_leases_naming_one_pid_as_no_session(self, tmp_path):
        """W3: nobody can tell from here which of the two the hook runs
        under."""
        leases = tmp_path / "git" / "specseal-leases"
        leases.mkdir(parents=True)
        (leases / "a").write_text('{"pid": 4242}', encoding="utf-8")
        assert hooksession.from_lease(str(tmp_path / "git"), 4242) == "a"
        (leases / "b").write_text('{"pid": 4242}', encoding="utf-8")
        assert hooksession.from_lease(str(tmp_path / "git"), 4242) == ""

    @pytest.mark.rule("a-persons-own-commit")
    @pytest.mark.parametrize(
        "shells", [0, 2], ids=["claude-the-parent", "claude-four-levels-up"]
    )
    def test_refuses_a_commit_whose_session_the_lease_names(self, world, shells):
        """The walk up to `claude` climbs past the shells between it and git:
        with two, `claude` is four levels above the hook, one more than any
        other case here puts it."""
        ps_names_the_parent_or_skip(LEASE_NEEDS_PS)
        claude = fake_claude(world)
        press(world)
        world.change(world.main)
        before = world.head(world.main)
        got = as_claude(world, claude, under_shells("git commit -q -m x", shells))
        assert got.returncode != 0
        assert world.head(world.main) == before
        assert AUTOMATION_TEXT in got.stderr

    def test_refuses_a_commit_in_an_undeclared_linked_worktree_through_the_lease(
        self, world
    ):
        """P2's stub looks for a lease in the whole clone, from the common
        git directory: a session whose lease sits in the main checkout and
        whose commit lands in a linked worktree, with no variable, still
        starts Python, and the commit is judged."""
        ps_names_the_parent_or_skip(LEASE_NEEDS_PS)
        claude = fake_claude(world)
        (world.w / "seal" / "specs" / "1790000000-x" / "routing.md").unlink()
        world.change(world.w)
        before = world.head(world.w)
        got = as_claude(world, claude, f"git -C {q(world.w)} commit -q -m x")
        assert got.returncode != 0, got.stderr
        assert world.head(world.w) == before

    @pytest.mark.rule("a-persons-own-commit")
    def test_refuses_an_emptied_environment_through_the_lease(self, world):
        """M6's two rows a probe could not see: `env -i git commit …`. On
        Windows this case was green for another reason: `env -i` there
        cannot find `git` on a `;`-separated PATH (#692's Windows pass)."""
        ps_names_the_parent_or_skip(LEASE_NEEDS_PS)
        claude = fake_claude(world)
        world.change(world.main)
        before = world.head(world.main)
        path = os.environ.get("PATH", "")
        got = as_claude(
            world,
            claude,
            f"env -i PATH={q(path)} HOME={q(world.home)} git commit -q -m x",
        )
        assert got.returncode != 0, got.stderr
        assert world.head(world.main) == before

    def test_refuses_through_a_lease_in_a_linked_worktree(self, tmp_path):
        leases = tmp_path / "git" / "worktrees" / "wt" / "specseal-leases"
        leases.mkdir(parents=True)
        (leases / "s9").write_text('{"pid": 4242}', encoding="utf-8")
        assert hooksession.from_lease(str(tmp_path / "git"), 4242) == "s9"
        assert hooksession.from_lease(str(tmp_path / "git"), 4243) == ""

    @pytest.mark.rule("a-persons-own-commit")
    def test_refuses_through_the_exported_pid_with_no_ps_run(
        self, tmp_path, monkeypatch
    ):
        """S5 of work item 1791384157 (#868). Where the environment carries
        `CLAUDE_PID`, the lease route matches it against the leases and runs
        no `ps`; without it the walk runs as before. Red at `5623d728`, where
        the route walked the process table whatever the environment held."""
        leases = tmp_path / "git" / "specseal-leases"
        leases.mkdir(parents=True)
        (leases / "s5").write_text('{"pid": 4242}', encoding="utf-8")
        ran = []

        def no_process_table(*args, **kwargs):
            ran.append(args[0] if args else kwargs.get("args"))
            raise OSError("no ps here")

        monkeypatch.setattr(hooksession.subprocess, "run", no_process_table)
        common = str(tmp_path / "git")
        assert hooksession.session(common, {"CLAUDE_PID": "4242"}) == ("s5", "lease")
        assert not ran, ran
        assert hooksession.session(common, {}) == ("", "")
        assert ran, "the walk under the variable did not run"

    @pytest.mark.rule("a-persons-own-commit")
    def test_refuses_with_the_one_variable_the_stub_and_the_reader_name(self):
        """S6 of work item 1791384157 (#868). `hooksession.session` reads one
        variable, and the stub's short-cut names the same one and no other:
        `$CLAUDECODE` was read by the stub alone, so a stub that started
        Python on it started an interpreter that answered no session unless a
        lease stood. Red at `5623d728`, where the stub named both."""
        assert hooksession.SESSION_VARIABLE == "CLAUDE_CODE_SESSION_ID"
        for hook in githooks.HOOKS:
            text = githooks.stub_text(hook, version="0.0.1")
            assert "$CLAUDE_CODE_SESSION_ID" in text, hook
            assert "CLAUDECODE" not in text, hook


def status(world, d):
    return (
        world.head(d),
        g(d, "status", "--porcelain", home=world.home, session="").stdout,
        g(d, "write-tree", home=world.home, session="").stdout,
    )


class Test_no_verify_is_met_where_the_branch_moves:
    """S3 of #692: `--no-verify` skips `pre-commit`, and the backstop in
    `reference-transaction` meets the commit where its branch moves, unless
    `pre-commit` left its one-shot mark for that very commit."""

    @pytest.mark.rule("no-verify-met-where-the-branch-moves")
    @pytest.mark.parametrize("head", ["a branch", "detached"])
    def test_refuses_no_verify_into_the_undeclared_checkout(self, world, head):
        if head == "detached":
            g(
                world.main,
                "switch",
                "-q",
                "--detach",
                "HEAD",
                home=world.home,
                session="",
            )
        world.change(world.main)
        before = status(world, world.main)
        got = g(
            world.main,
            *("commit", "--no-verify", "-q", "-m", "x"),
            home=world.home,
            check=False,
        )
        assert got.returncode != 0
        assert status(world, world.main) == before
        assert gate.BACKSTOP in got.stderr
        assert f"No review is recorded for this cycle in {world.main}," in got.stderr

    @pytest.mark.rule("no-verify-met-where-the-branch-moves")
    @pytest.mark.skipif(os.name == "nt", reason=MARK_WITHOUT_PROCESS)
    def test_refuses_a_mark_an_aborted_commit_left(self, world):
        """Round 1's yellow 10, c16: the same HEAD, tree and author date, and
        another `git commit` process, which `pre-commit` never saw."""
        world.change(world.main)
        date = {"GIT_AUTHOR_DATE": "@1790000000 +0000"}
        aborted = g(
            world.main,
            *("-c", "specseal.waive=review", "commit", "-q", "-m", ""),
            home=world.home,
            check=False,
            **date,
        )
        assert aborted.returncode != 0
        before = world.head(world.main)
        got = g(
            world.main,
            *("commit", "--no-verify", "-q", "-m", "x"),
            home=world.home,
            check=False,
            **date,
        )
        assert got.returncode != 0, "a stale mark let a later commit through"
        assert gate.BACKSTOP in got.stderr
        assert world.head(world.main) == before

    def test_refuses_a_mark_keyed_for_another_commit(self):
        """The old HEAD, the tree, the commit's own author date and the `git
        commit` process each name the commit a mark was left for, so a mark
        left by a commit that aborted after pre-commit does not pass a later
        one. A root commit's old value is the null id at the ref and nothing
        in pre-commit, and both name the same commit."""
        base = commitgate._key("a" * 40, "t", "@1 +0000", 7)
        assert base != commitgate._key("a" * 40, "t", "@2 +0000", 7)
        assert base != commitgate._key("b" * 40, "t", "@1 +0000", 7)
        assert base != commitgate._key("a" * 40, "u", "@1 +0000", 7)
        assert base != commitgate._key("a" * 40, "t", "@1 +0000", 8)
        assert commitgate._key("0" * 40, "t", "@1 +0000", 7) == commitgate._key(
            "", "t", "@1 +0000", 7
        )

    def test_accepts_no_verify_into_the_declared_worktree(self, world):
        world.change(world.w)
        before = world.head(world.w)
        g(world.w, "commit", "--no-verify", "-q", "-m", "x", home=world.home)
        assert world.head(world.w) != before

    def test_accepts_a_commit_pre_commit_let_through_and_leaves_no_mark(self, world):
        world.change(world.w)
        g(world.w, "commit", "-q", "-m", "x", home=world.home)
        judged = world.main / ".git" / "worktrees" / "w" / commitgate.JUDGED
        assert judged.is_dir() and not list(judged.iterdir())

    @pytest.mark.rule("no-verify-met-where-the-branch-moves")
    @pytest.mark.parametrize(
        "args",
        [
            ("reset", "-q", "--hard", "HEAD~1"),
            ("cherry-pick", "side"),
        ],
        ids=["a move with no new commit", "a new commit"],
    )
    def test_accepts_a_branch_moved_by_anything_but_git_commit(self, world, args):
        """M12: only `git commit` hands the backstop GIT_AUTHOR_DATE, so the
        undeclared checkout's branch moves for every other command as before:
        sampled to one move that makes no commit and one that makes one."""
        g(world.main, "branch", "side", home=world.home, session="")
        g(world.main, "switch", "-q", "side", home=world.home, session="")
        world.change(world.main)
        g(world.main, "commit", "-q", "-m", "on side", home=world.home, session="")
        g(world.main, "switch", "-q", "release", home=world.home, session="")
        if args[0] == "reset":
            g(
                world.main,
                "merge",
                "-q",
                "--ff-only",
                "side",
                home=world.home,
                session="",
            )
        got = g(world.main, *args, home=world.home, check=False)
        assert got.returncode == 0, got.stderr
        assert gate.HEADER not in got.stderr

    def test_accepts_every_transaction_state_but_prepared(self, world):
        """The backstop judges at `prepared` alone: a `committed` or an
        `aborted` update of a branch no mark names is let be."""
        world.change(world.main)
        lines = [f"{world.head(world.main)} {'f' * 40} refs/heads/release"]
        e = env(world.home, GIT_AUTHOR_DATE="@1 +0000")
        for state in ("committed", "aborted"):
            got = commitgate.reference_transaction(
                str(world.main), e, state, lines, io.StringIO()
            )
            assert got == 0, state


def diverged(world):
    """`release` and `side` in the undeclared main checkout, each changing
    f.py its own way, `side` with a second commit on top. Made as a person's
    commits, so nothing judges the setup."""
    d = world.main
    g(d, "branch", "side", home=world.home, session="")
    world.change(d, text="a = 'release'\n")
    g(d, "commit", "-q", "-m", "release", home=world.home, session="")
    g(d, "switch", "-q", "side", home=world.home, session="")
    world.change(d, text="a = 'side'\n")
    g(d, "commit", "-q", "-m", "side", home=world.home, session="")
    world.change(d, name="g.py", text="g = 1\n")
    g(d, "commit", "-q", "-m", "side 2", home=world.home, session="")
    return d


def resolve(world, d):
    world.change(d, text="a = 'both'\n")


def busy(world, d):
    return any(
        (d / ".git" / n).exists()
        for n in ("rebase-merge", "rebase-apply", "CHERRY_PICK_HEAD", "REVERT_HEAD")
    )


class Test_a_commit_git_makes_for_its_own_sequencer:
    """Round 1's yellow 7 of #692: a commit git's own rebase, cherry-pick or
    revert makes is not judged; a commit a shell starts, while a sequencer
    is paused or through an alias, is."""

    @pytest.mark.rule("gits-own-commits-not-judged")
    @pytest.mark.skipif(os.name == "nt", reason=NO_SEQUENCER_COMMIT)
    def test_accepts_a_rebase_git_continues(self, world):
        """c13: the sequencer's own `git commit -n` hands the backstop the
        author date and skips `pre-commit`. It is git's commit, made by a git
        process while a rebase is in progress, and is not judged."""
        d = diverged(world)
        g(d, "rebase", "-q", "release", home=world.home, check=False)
        resolve(world, d)
        got = g(
            d, "rebase", "--continue", home=world.home, check=False, GIT_EDITOR="true"
        )
        assert gate.HEADER not in got.stderr, got.stderr
        assert got.returncode == 0, got.stderr
        assert not busy(world, d)

    @pytest.mark.rule("gits-own-commits-not-judged")
    @pytest.mark.skipif(os.name == "nt", reason=NO_SEQUENCER_COMMIT)
    def test_accepts_an_interactive_rebases_reword(self, world):
        """c09: a reword runs `pre-commit` from the sequencer."""
        d = diverged(world)
        got = g(
            d,
            *("rebase", "-q", "-i", "HEAD~2"),
            home=world.home,
            check=False,
            GIT_EDITOR="true",
            GIT_SEQUENCE_EDITOR="sed -i.bak 1s/^pick/reword/",
        )
        assert gate.HEADER not in got.stderr, got.stderr
        assert got.returncode == 0, got.stderr
        assert not busy(world, d)

    @pytest.mark.rule("gits-own-commits-not-judged")
    @pytest.mark.skipif(os.name == "nt", reason=NO_SEQUENCER_COMMIT)
    @pytest.mark.parametrize("verb", ["cherry-pick", "revert"])
    def test_accepts_a_pick_git_continues(self, world, verb):
        """The same sequencer path, executed on four gits by round 1's fix
        pass: `cherry-pick --continue` and `revert --continue` run
        `pre-commit`."""
        d = diverged(world)
        g(d, "switch", "-q", "release", home=world.home, session="")
        if verb == "revert":
            g(
                d,
                *("merge", "-q", "--ff-only", "--no-edit", "side"),
                home=world.home,
                session="",
                check=False,
            )
            g(d, "reset", "-q", "--hard", "release", home=world.home, session="")
            world.change(d, text="a = 'later'\n")
            g(d, "commit", "-q", "-m", "later", home=world.home, session="")
            g(d, verb, "--no-edit", "HEAD~1", home=world.home, check=False)
        else:
            g(d, verb, "side~1", home=world.home, check=False)
        assert busy(world, d)
        resolve(world, d)
        got = g(d, verb, "--continue", home=world.home, check=False, GIT_EDITOR="true")
        assert gate.HEADER not in got.stderr, got.stderr
        assert got.returncode == 0, got.stderr
        assert not busy(world, d)

    @pytest.mark.rule("gits-own-commits-not-judged")
    def test_refuses_a_commit_typed_while_a_rebase_is_paused(self, world):
        """What the criterion keeps: a `git commit --no-verify` a shell
        starts during a paused rebase is a commit, and its branch move is
        refused."""
        d = diverged(world)
        g(d, "rebase", "-q", "release", home=world.home, check=False)
        resolve(world, d)
        before = world.head(d)
        got = g(
            d,
            *("commit", "--no-verify", "-q", "-m", "typed"),
            home=world.home,
            check=False,
        )
        assert got.returncode != 0
        assert gate.BACKSTOP in got.stderr
        assert world.head(d) == before

    @pytest.mark.rule("gits-own-commits-not-judged")
    def test_refuses_a_commit_an_alias_starts(self, world):
        """An alias runs `git commit` as a child of `git` too; with no
        sequencer state on disk it is a person's command, and is judged."""
        world.change(world.main)
        before = world.head(world.main)
        got = g(
            world.main,
            *("-c", "alias.ci=commit", "ci", "-q", "-m", "x"),
            home=world.home,
            check=False,
        )
        assert got.returncode != 0
        assert gate.HEADER in got.stderr
        assert world.head(world.main) == before

    @pytest.mark.rule("gits-own-commits-not-judged")
    def test_refuses_concluding_a_conflicted_merge(self, world):
        """Round 3's n07: `MERGE_HEAD` is no sequencer state, so `git merge
        --continue` in the undeclared main checkout is a commit the shell
        started, and it is refused with HEAD where it was."""
        d = diverged(world)
        g(d, "switch", "-q", "release", home=world.home, session="")
        g(d, "merge", "-q", "side", home=world.home, session="", check=False)
        resolve(world, d)
        before = world.head(d)
        got = g(
            d, "merge", "--continue", home=world.home, check=False, GIT_EDITOR="true"
        )
        assert got.returncode != 0, got.stderr
        assert gate.HEADER in got.stderr
        assert world.head(d) == before


AUTOMATION_TEXT = (
    "This session's person pressed `automation` on the routing question, so "
    "no question is put to them, and none is to be put to them in its place: "
    "the run was promised that nothing would stop to ask.\n\n"
    "The ways on, none of which needs a person:\n"
    "  1. Only for a commit that belongs to no work item: re-issue it as "
    "`git -c specseal.waive=review commit …`. The older spelling, "
    "`: '[no-review]'; git commit …`, still works.\n"
    "  2. Otherwise, do not retry it: write the commit down and hand it back "
    "at the end of the run."
)


class Test_the_refusal_names_who_answers_it:
    """S4 to S6 of #692: a refused commit's text is put to the session's
    person or, under the press, to nobody, and the ways on it names
    commit."""

    @pytest.mark.rule("how-a-stop-is-put")
    def test_refuses_under_the_press_naming_no_question_tool(self, world):
        """S4."""
        press(world)
        world.change(world.main)
        got = g(world.main, "commit", "-q", "-m", "x", home=world.home, check=False)
        assert got.returncode != 0
        assert got.stderr.startswith(
            "SpecSeal stopped this commit; nothing was committed.\n"
        )
        assert AUTOMATION_TEXT in got.stderr
        assert "AskUserQuestion" not in got.stderr
        assert got.stderr.rstrip().endswith(
            "Re-issuing this commit unchanged meets this same refusal."
        )
        assert (
            got.stderr
            == gate.refusal(["review"], str(world.main), "release", True) + "\n"
        )

    @pytest.mark.rule("how-a-stop-is-put")
    def test_refuses_an_attended_session_alike_twice_telling_it_to_ask(self, world):
        """S5."""
        world.change(world.main)
        first = g(world.main, "commit", "-q", "-m", "x", home=world.home, check=False)
        second = g(world.main, "commit", "-q", "-m", "x", home=world.home, check=False)
        assert first.returncode != 0 and second.returncode != 0
        assert first.stderr == second.stderr
        text = first.stderr
        assert (
            "Do not choose for the user. Ask with the AskUserQuestion tool, "
            "offering exactly these three options:" in text
        )
        assert '    1. "Declare the routing" — ' in text
        assert '    2. "Review it first" — ' in text
        assert (
            '    3. "Commit without a review" — re-issue it as '
            "`git -c specseal.waive=review commit …`. The older spelling, "
            "`: '[no-review]'; git commit …`, still works." in text
        )
        assert "Then do what they picked." in text

    def test_refuses_to_an_ascii_console_as_written(self, world):
        """#741 S8: `hooks/git/pre-commit.py` opens with
        `console.to_utf8()`.

        Without the call the hook did not crash here, which is what #741's
        frame expected: Python keeps `backslashreplace` on stderr whatever
        `PYTHONIOENCODING` says, so the refusal arrived with every em dash
        and ellipsis spelled `\\u2014` and `\\u2026`, including inside the
        waiver it tells the reader to type. Decoded here as UTF-8 rather than
        in the locale's encoding, so the Windows leg reads the same bytes."""
        world.change(world.main)
        got = subprocess.run(
            ["git", "-C", str(world.main), "commit", "-q", "-m", "x"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            env=env(world.home, PYTHONIOENCODING="ascii", PYTHONUTF8="0"),
            stdin=subprocess.DEVNULL,
            timeout=60,
        )
        assert got.returncode != 0
        assert "\\u20" not in got.stderr, got.stderr
        assert (
            got.stderr
            == gate.refusal(["review"], str(world.main), "release", False) + "\n"
        )

    @pytest.mark.rule("how-a-stop-is-put")
    def test_refuses_an_old_spelling_for_another_agents_commit(self, world):
        """Round 1's yellow 9, c25: while agent A's call carrying
        `[no-review]` runs, agent B's commit under the same session id is its
        own command, and is judged; and B's call starting does not take A's
        answer away."""
        ps_names_the_parent_or_skip(OLD_SPELLING_NEEDS_PS)
        a = ": '[no-review]'; git commit -q -m a"
        group(world, "pre-bash", a, "toolu_a")
        group(world, "pre-bash", "git commit -q -m b", "toolu_b")
        world.change(world.main)
        before = world.head(world.main)
        b = as_a_call(world, "git commit -q -m b")
        assert b.returncode != 0, "A's token waived B's commit"
        assert world.head(world.main) == before
        group(world, "post-bash", "git commit -q -m b", "toolu_b")
        got = as_a_call(world, a)
        assert got.returncode == 0, got.stderr
        assert world.head(world.main) != before

    @pytest.mark.rule("how-a-stop-is-put")
    def test_refuses_a_waiver_written_inside_a_message(self, world):
        """S6: inside a message the waiver is prose."""
        world.change(world.main)
        before = world.head(world.main)
        got = g(
            world.main,
            *("commit", "-q", "-m", "specseal.waive=review later"),
            home=world.home,
            check=False,
        )
        assert got.returncode != 0
        assert world.head(world.main) == before

    @pytest.mark.rule("how-a-stop-is-put")
    def test_accepts_both_spellings_the_refusal_names(self, world):
        """S5: the git-native waiver commits, and the old spelling does
        through the PreToolUse writer that carries it, for its own call
        alone."""
        world.change(world.main)
        before = world.head(world.main)
        g(
            world.main,
            *("-c", "specseal.waive=review", "commit", "-q", "-m", "x"),
            home=world.home,
        )
        assert world.head(world.main) != before
        ps_names_the_parent_or_skip(OLD_SPELLING_NEEDS_PS)
        world.change(world.main)
        before = world.head(world.main)
        command = ": '[no-review]'; git commit -q -m y"
        group(world, "pre-bash", command, "toolu_a")
        got = as_a_call(world, command)
        assert got.returncode == 0, got.stderr
        assert world.head(world.main) != before
        group(world, "post-bash", command, "toolu_a")
        world.change(world.main)
        again = as_a_call(world, "git commit -q -m z")
        assert again.returncode != 0, "the answer outlived the call that carried it"

    def test_accepts_a_review_mark_naming_head(self, world):
        (world.main / ".git" / "specseal-reviewed").write_text(
            world.head(world.main), encoding="utf-8"
        )
        world.change(world.main)
        before = world.head(world.main)
        g(world.main, "commit", "-q", "-m", "x", home=world.home)
        assert world.head(world.main) != before


class Test_the_parity_arm_inside_git:
    """#988: the parity arm meets a code commit where a migration config is
    declared, and stays quiet under the review chain."""

    @pytest.mark.rule("parity-quiet-under-the-chain")
    def test_accepts_a_chain_declared_code_commit(self, world):
        """S1 of #988, through `pre-commit`. `world.w`'s branch declares the
        review chain, so a code commit there lands with no parity mark at
        HEAD, and the comparison is owed in each round record at the pull
        request."""
        (world.w / "seal" / "parity.md").write_text("# parity\n", encoding="utf-8")
        g(world.w, "add", "seal/parity.md", home=world.home, session="")
        before = world.head(world.w)
        g(world.w, "commit", "-q", "-m", "the migration config", home=world.home)
        (world.w / "f.py").write_text("a = 3\n", encoding="utf-8")
        g(world.w, "commit", "-q", "-am", "code", home=world.home)
        assert world.head(world.w) != before

    def test_accepts_a_docs_commit_a_waived_one_and_one_compared_at_head(self, world):
        """`world.w` declares `straight to the PR` here, the answer under
        which the parity arm stays at the commit (#988, `questions.md` Q1):
        a commit of documents alone lands, a code commit waived with
        `specseal.waive=parity` lands, and a comparison recorded at HEAD lets
        the next code commit through."""
        declare(world.w, "feat", review="straight to the PR")
        (world.w / "seal" / "parity.md").write_text("# parity\n", encoding="utf-8")
        (world.w / "docs").mkdir()
        (world.w / "docs" / "a.md").write_text("x\n", encoding="utf-8")
        g(world.w, "add", "docs/a.md", home=world.home, session="")
        before = world.head(world.w)
        g(world.w, "commit", "-q", "-m", "docs only", home=world.home)
        assert world.head(world.w) != before
        (world.w / "f.py").write_text("a = 3\n", encoding="utf-8")
        g(
            world.w,
            *("-c", "specseal.waive=parity", "commit", "-q", "-am", "code"),
            home=world.home,
        )
        gitdir = world.main / ".git" / "worktrees" / "w"
        (gitdir / "specseal-parity").write_text(world.head(world.w), encoding="utf-8")
        (world.w / "f.py").write_text("a = 4\n", encoding="utf-8")
        before = world.head(world.w)
        g(world.w, "commit", "-q", "-am", "compared", home=world.home)
        assert world.head(world.w) != before

    def test_refuses_a_code_commit_nothing_compared(self, world):
        declare(world.w, "feat", review="straight to the PR")
        (world.w / "seal" / "parity.md").write_text("# parity\n", encoding="utf-8")
        (world.w / "f.py").write_text("a = 3\n", encoding="utf-8")
        before = world.head(world.w)
        got = g(world.w, "commit", "-q", "-am", "code", home=world.home, check=False)
        assert got.returncode != 0
        assert gate.STATES["parity"].format(top=world.w) in got.stderr
        assert world.head(world.w) == before


def routed_to_the_smith(world):
    routing_md = world.w / "seal" / "specs" / "1790000000-x" / "routing.md"
    routing_md.write_text(
        routing_md.read_text(encoding="utf-8") + "| Implementation | smith |\n",
        encoding="utf-8",
    )


class Test_post_commit_after_a_commit_git_made:
    """`post-commit` says what follows a commit git made: the implementer
    notice once, and the stamp's values where the commit adds a `sealed`
    guarantee."""

    def test_accepts_the_implementer_notice_once(self, world):
        routed_to_the_smith(world)
        world.change(world.w)
        first = g(world.w, "commit", "-q", "-m", "x", home=world.home)
        assert "answers `Implementation` with `smith`" in first.stdout + first.stderr
        world.change(world.w)
        second = g(world.w, "commit", "-q", "-m", "y", home=world.home)
        assert "answers `Implementation`" not in second.stdout + second.stderr

    @pytest.mark.rule("stamp-drawn-once")
    def test_accepts_a_sealed_guarantees_commit_naming_its_stamp(self, world):
        """#975 S4, through the stub git runs: the commit that adds a work
        item's `guarantee.md` reading `sealed` prints one line saying where
        the stamp's values wait and how to draw them by hand, and the file is
        there."""
        item = world.w / "seal" / "specs" / "1790000000-x"
        head = world.head(world.w)[:8]
        (item / "guarantee.md").write_text(
            "| Field | Value |\n|---|---|\n"
            f"| Target SHA | {head} against release |\n\nVerdict: sealed\n",
            encoding="utf-8",
        )
        g(world.w, "add", "-A", home=world.home, session="")
        got = g(world.w, "commit", "-q", "-m", "the guarantee", home=world.home)
        said = got.stdout + got.stderr
        assert (
            "specseal: the stamp for 1790000000 is drawn at the end of this turn "
            "from " in said
        ), said
        values = world.main / ".git" / "specseal-stamp" / SESSION
        (name,) = os.listdir(values)
        assert name.endswith(f"-1790000000-{head}.json"), name
        path = str(values / name)
        quoted = f'"{path}"' if os.name == "nt" else shlex.quote(path)
        assert f"`seal-stamp --from {quoted}`" in said, said

    def test_refuses_the_notice_in_the_post_tool_use_hook(self, world, monkeypatch):
        """Where git says the notice, the PostToolUse hook that read the
        command for `git commit` says nothing."""
        notice = load_hook_module("implementer-notice.py", "notice_beside_post_commit")
        routed_to_the_smith(world)
        payload = {
            "tool_name": "Bash",
            "tool_input": {"command": "git commit -m x"},
            "cwd": str(world.w),
            "session_id": "s-other",
        }
        out = io.StringIO()
        monkeypatch.setattr(sys, "stdin", io.StringIO(json.dumps(payload)))
        monkeypatch.setattr(sys, "stdout", out)
        notice.main()
        assert out.getvalue() == ""


# The refusal of a `sealed` the history does not hold, as a person reads it
# (work item 1792363231, `spec.md` S11). It is no arm: no question, no waiver.
GUARANTEE_TEXT = (
    "SpecSeal stopped this commit; nothing was committed.\n\n"
    "{path} reads `sealed` over {target}, a commit the history of this one "
    "does not hold: it is neither HEAD of `{branch}`, {head}, nor an ancestor "
    "of it. Committed, that verdict would draw no stamp, and the pull "
    "request's check would refuse it as stale.\n\n"
    "The way on is a new audit: spawn the sealer again at HEAD. Its `Target "
    "SHA` row then names {head} and keeps this verdict as `; earlier run: "
    "{target} sealed`. Do not edit the row by hand: a row the sealer did not "
    "write is a verdict nobody gave.\n\n"
    "Re-issuing this commit unchanged meets this same refusal.\n"
)
GUARANTEE = "seal/specs/1790000000-x/guarantee.md"


def guarantee(world, target, verdict):
    (world.w / GUARANTEE).write_text(
        "| Field | Value |\n|---|---|\n"
        f"| Target SHA | {target} against release |\n\n{verdict}\n",
        encoding="utf-8",
    )


def withheld_then_sealed(world):
    """A committed guarantee withheld over HEAD, and then on disk the same
    guarantee reading `sealed` over `deadbee`, which the branch does not
    hold; the withheld guarantee's target, to put it back."""
    withheld = world.head(world.w)[:8]
    guarantee(world, withheld, "Verdict: withheld reason: x")
    g(world.w, "add", "-A", home=world.home, session="")
    g(world.w, "commit", "-q", "-m", "withheld", home=world.home, session="")
    guarantee(world, "deadbee", "Verdict: sealed")
    return withheld


class Test_a_sealed_the_branch_does_not_hold:
    """1792363231 S11 through the stubs `hooks/hook-install.py` wrote, and
    `questions.md` Q6: on the declared branch, a commit carrying a
    `guarantee.md` that reads `sealed` over `deadbee` is refused inside the
    commit, HEAD unmoved. What is read is the index git is about to commit,
    not the disk."""

    @pytest.mark.rule("refused-sealed-leaves-a-record")
    @pytest.mark.rule("sealed-off-the-branch-refused")
    @pytest.mark.parametrize(
        "shape", ["commit <pathspec>", "staged, then put back on disk"]
    )
    def test_refuses_it_inside_the_commit(self, world, shape):
        """Sampled to one shape per index the hook reads: named by a
        pathspec, where git hands the hook a temporary index through
        `GIT_INDEX_FILE`, as `-a` does; and staged, then put back to
        `withheld` on disk, where the index still carries the `sealed`. Red
        at 37f96f7a: every shape landed."""
        withheld = withheld_then_sealed(world)
        before = world.head(world.w)
        args = {
            "commit <pathspec>": ("commit", "-q", "-m", "the seal", "--", GUARANTEE),
            "staged, then put back on disk": ("commit", "-q", "-m", "the seal"),
        }[shape]
        if shape == "staged, then put back on disk":
            g(world.w, "add", GUARANTEE, home=world.home, session="")
            guarantee(world, withheld, "Verdict: withheld reason: x")
        got = g(world.w, *args, home=world.home, check=False)
        assert got.returncode != 0, got.stderr
        assert world.head(world.w) == before
        short = g(world.w, "rev-parse", "--short", "HEAD", home=world.home).stdout
        assert got.stderr == GUARANTEE_TEXT.format(
            path=GUARANTEE, target="deadbee", branch="feat", head=short.strip()
        ), got.stderr

    @pytest.mark.rule("sealed-off-the-branch-refused")
    def test_accepts_a_pathspec_commit_that_leaves_it_out(self, world):
        """A pathspec commit of another file carries an index without the
        staged guarantee, so it lands and the guarantee stays staged."""
        withheld_then_sealed(world)
        before = world.head(world.w)
        g(world.w, "add", GUARANTEE, home=world.home, session="")
        world.change(world.w)
        got = g(
            world.w,
            *("commit", "-q", "-m", "f", "--", "f.py"),
            home=world.home,
            check=False,
        )
        assert got.returncode == 0, got.stderr
        assert gate.HEADER not in got.stderr, got.stderr
        assert world.head(world.w) != before

        # `--quiet` answers by its exit status alone, so no path list is read.
        def differs(*pathspec):
            quiet = ("diff", "--cached", "--quiet", "--", *pathspec)
            return g(world.w, *quiet, home=world.home, check=False).returncode

        assert differs(GUARANTEE) == 1, "the staged guarantee was committed"
        assert differs(".", f":(exclude){GUARANTEE}") == 0, "more than it is staged"

    def test_accepts_a_near_miss_of_sealed(self, world):
        """S7 of #1000 through the stubs: a guarantee whose verdict line only
        looks like `sealed`, over `deadbee`, is not a `sealed` the commit gate
        judges, so the commit lands; the pull request's check refuses the
        line. One near miss stands for the shapes
        `tests/test_the_sealer_guarantees.py#NEAR_MISSES` holds for the
        reader."""
        guarantee(world, "deadbee", "Verdict: Sealed")
        g(world.w, "add", "-A", home=world.home, session="")
        before = world.head(world.w)
        got = g(world.w, "commit", "-q", "-m", "x", home=world.home, check=False)
        assert got.returncode == 0, got.stderr
        assert world.head(world.w) != before


# --- the PreToolUse reading stands aside where git decides --------------------
#
# P7 of #692 (2026-10-02): `hooks/commit-review-gate.py#main` stands aside
# for a command only where its shape is known plain (`hooks/tokens.py#
# is_plain`) and git runs this plugin's judgment in the clone it lands in
# (`hooks/githooks.py#decides`). Which commands are plain is judged here
# without git. The real-git rows below show the reading and git agree: a
# plain command the reading stands aside for is one git itself refuses, and
# a command that is not plain, or a clone whose hooks slot is foreign, meets
# the reading's own refusal.

STEPS_AROUND = {
    "-c core.hooksPath": "git -c core.hooksPath=/dev/null commit -m x",
    "the key in another case": "git -c CORE.HOOKSPATH=/dev/null commit -m x",
    "--config-env": "git --config-env=core.hooksPath=H commit -m x",
    # #716: the same option with its value as a separate word. Seen red at
    # `233f0455`, where the reading took the value for the subcommand.
    "--config-env, spaced": "git --config-env core.hooksPath=H commit -m x",
    "GIT_CONFIG_COUNT": (
        "GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.hooksPath "
        "GIT_CONFIG_VALUE_0=/nonexistent git commit -m x"
    ),
    "GIT_CONFIG_PARAMETERS": (
        "GIT_CONFIG_PARAMETERS=\"'core.hookspath'='/x'\" git commit -m x"
    ),
    "an exported GIT_CONFIG": "export GIT_CONFIG_GLOBAL=/x/g; git commit -m x",
    "env -i": "env -i PATH=/usr/bin git commit -m x",
    "env --ignore-environment": "env --ignore-environment git commit -m x",
    "a path-qualified env -": "/usr/bin/env - git commit -m x",
    "env -i in a subshell": "(env -i git commit -m x)",
    "GIT_CONFIG in a subshell": "(GIT_CONFIG_GLOBAL=/x/g git commit -m x)",
    "an unreadable command": "git commit -m 'x",
    # Round 2's yellow 1: the session variable the stub reads, removed
    # another way than `env -i`. Since #868 the stub reads one name,
    # `CLAUDE_CODE_SESSION_ID`, and these rows name it.
    "an emptied session variable": "CLAUDE_CODE_SESSION_ID= git commit -m x",
    "a session variable in a subshell": "(CLAUDE_CODE_SESSION_ID= git commit -m x)",
    "env -u": "env -u CLAUDE_CODE_SESSION_ID git commit -m x",
    "env -u glued to its name": "env -uCLAUDE_CODE_SESSION_ID git commit -m x",
    "env --unset=": "env --unset=CLAUDE_CODE_SESSION_ID git commit -m x",
    "unset": "unset CLAUDE_CODE_SESSION_ID; git commit -m x",
    # Round 2's yellow 2: a config file the command names, which can carry
    # core.hooksPath where no word does.
    "include.path": "git -c include.path=/x/cfg commit -m x",
    "includeIf": "git -c includeIf.onbranch:main.path=/x/cfg commit -m x",
    "include.path through --config-env": "git --config-env=include.path=CFG commit -m x",
    "include.path through git config": (
        "git config include.path /x/cfg && git commit -m x"
    ),
    "HOME": "HOME=/x/h git commit -m x",
    "XDG_CONFIG_HOME": "XDG_CONFIG_HOME=/x/c git commit -m x",
    # Round 3's yellow 1: a string a shell parses again. None of these is
    # plain, so the reading judges each (P7, the owner's answer of
    # 2026-10-02).
    "sh -c unsetting a session variable": (
        "sh -c 'unset CLAUDE_CODE_SESSION_ID; git commit -m x'"
    ),
    "include.path behind cd in bash -c": (
        "bash -c 'cd . && git -c include.path=/x/cfg commit -m x'"
    ),
    "GIT_CONFIG behind cd in sh -c": (
        "sh -c 'cd . && GIT_CONFIG_GLOBAL=/x/g git commit -m x'"
    ),
    "HOME in a quoted substitution": 'echo "$(cd . && HOME=/x/h git commit -m x)"',
    "eval of a literal string": "eval 'unset CLAUDE_CODE_SESSION_ID; git commit -m x'",
    # P7: an `eval` is not plain, so the reading's fail-closed answer for one
    # whose argument it cannot reduce comes back, as 0.16.0 gave it.
    "eval of a variable": 'eval "$C"',
    # Round 3's yellow 2: the environment emptied with another option first.
    "env -v -i": "env -v -i git commit -m x",
    "env -u then -i": "env -u FOO -i git commit -m x",
    "env -u glued behind a flag": "env -vuCLAUDE_CODE_SESSION_ID git commit -m x",
    "env -S splitting a -u": "env -S'-u CLAUDE_CODE_SESSION_ID' git commit -m x",
    "exec -c": "(exec -c git commit -m x)",
    # The limit beside the removed stub: `rm` and `chmod` are not plain, so
    # a command that takes the stubs away first is judged (P7).
    "the stubs removed first": (
        "rm -f .git/hooks/pre-commit .git/hooks/reference-transaction"
        " && git commit -m x"
    ),
    "the stubs' execute bit taken first": (
        "chmod -x .git/hooks/pre-commit .git/hooks/reference-transaction"
        " && git commit -m x"
    ),
}

# Not plain for another condition of the rule than a word the list reads.
OTHER_CONDITIONS = {
    "a git with no subcommand": "git",
    "the same, before a separator": "git -C /x/m; echo y",
    "a global option outside the rule": "git --git-dir=/x/m commit -m x",
    "an assignment inside an expansion": ': "${X:=y}"; git commit -m x',
    "a parenthesis inside a word": "echo x(y); git commit -m x",
    "a brace outside quotes": "echo {a,b}; git commit -m x",
    "splits whole, but not once the body goes": "cat <<EOF\n'\nEOF\necho '",
    # A word the list reads, in an otherwise plain shape (round 3's m07): it
    # costs one judgment, which is the list's direction (P6).
    "a word the list reads in a plain shape": "git commit -m CLAUDE_CODE_SESSION_ID",
    "output duplicated onto a file": "git commit -m x >&f",
    "an option that writes": "git diff --output=/x/o; git commit -m x",
    "a program that is not the bare word": "/usr/bin/git commit -m x",
    # Programs outside the allowlist, and an empty command, which is no shape
    # at all. An assignment in a program's place is no plain shape either, so
    # `CLAUDECODE= git commit -m x` is judged although the list no longer
    # names the variable (S6 of work item 1791384157).
    "env with an assignment": "env FOO=1 git commit -m x",
    "printenv of a git variable": "printenv GIT_DIR",
    "printenv HOME": "printenv HOME",
    "an empty command": "",
    "an assignment of CLAUDECODE": "CLAUDECODE= git commit -m x",
    "env -u CLAUDECODE": "env -u CLAUDECODE git commit -m x",
    # The windows limit and the lease's: a command that exports
    # `LD_PRELOAD`, or empties the environment, is never plain, so the
    # reading judges it wherever it lands.
    "stdbuf": "stdbuf -oL git commit -m x",
    "LD_PRELOAD as an assignment": "LD_PRELOAD=/x git commit -m x",
    "LD_PRELOAD exported": "export LD_PRELOAD=/x; git commit -m x",
    "env -i alone": "env -i git commit -m x",
}

# Plain, so the reading stands aside for each in a clone git decides.
STILL_PLAIN = [
    "git commit -m x",
    "git -c specseal.waive=parity commit -m x",
    "echo GIT_CONFIG_NOSYSTEM",
    "echo $CLAUDECODE",
    "git commit -m 'mentions CLAUDE_CODE_SESSION_ID'",
    "cat $HOME/x",
    "git -c user.name=HOME commit -m x",
    "git commit -m 'read include.path'",
    # S6 of work item 1791384157 (#868): plain since the stub stopped
    # reading `CLAUDECODE`.
    "git commit -m CLAUDECODE",
]

# Words the hook-bypass list does not read: a session name or a config key
# read whole, expanded or inside a message, removes nothing (round 2 of #692).
NOT_ON_THE_LIST = [
    *STILL_PLAIN,
    "env FOO=1 git commit -m x",
    "printenv GIT_DIR",
    "printenv HOME",
    "",
    "CLAUDECODE= git commit -m x",
    "env -u CLAUDECODE git commit -m x",
]

# The shapes this repository's own agents type, and the same shape with one
# thing outside the rule. Each pair differs in one place.
PLAIN_AND_NOT = {
    "-m": ('git -C {d} commit -q -m "x"', 'git -C {d} commit -q -m "x"; ls'),
    "-F a file": ("git -C {d} commit -F {f}", "git -C {d} commit -F {f}; printenv"),
    "a quoted heredoc": (
        "git -C {d} commit -q -F - <<'EOF'\nfix `x` and $(y)\nEOF",
        "git -C {d} commit -q -F - <<EOF\nfix $(y)\nEOF",
    ),
    "cd first": ("cd {d} && git commit -q -m x", "cd {d} && X=1 git commit -q -m x"),
    "piped to tail": (
        "git -C {d} commit -q -m x 2>&1 | tail -3",
        "git -C {d} commit -q -m x 2>&1 | xargs echo",
    ),
    "to /dev/null": (
        "git -C {d} commit -q -m x >/dev/null",
        "git -C {d} commit -q -m x >{f}.out",
    ),
    "a -c the plugin reads": (
        "git -C {d} -c commit.gpgsign=false commit -q -m x",
        "git -C {d} -c core.editor=true commit -q -m x",
    ),
    "a subcommand outside the list": (
        "git -C {d} add f.py && git -C {d} commit -q -m x",
        "git -C {d} stash && git -C {d} commit -q -m x",
    ),
    "printf with no option": (
        "printf '%s\\n' x; git -C {d} commit -q -m x",
        "printf -v y x; git -C {d} commit -q -m x",
    ),
    "a substitution": (
        "git -C {d} commit -q -m 'it is $(x)'",
        'git -C {d} commit -q -m "it is $(echo x)"',
    ),
    "a subshell": ("git -C {d} commit -q -m x", "(git -C {d} commit -q -m x)"),
    "a second line": (
        "git -C {d} commit -q -m x\ngit -C {d} log -1",
        "git -C {d} commit -q -m x\nsh -c true",
    ),
}


def spelt(shape, which):
    """One of PLAIN_AND_NOT's forms with a fixed directory and file."""
    return PLAIN_AND_NOT[shape][which].format(d=q("/x/m"), f=q("/x/msg.txt"))


class Test_the_text_reading_stands_aside_where_git_decides:
    """P1, P5 and P7 of #692: the PreToolUse reading of a Bash command
    stands aside for a plain command in a clone where git runs this
    plugin's judgment, and judges every other command as 0.16.0 judged it."""

    @pytest.mark.rule("text-reading-stands-aside")
    def test_accepts_a_plain_command_git_then_refuses_itself(self, world):
        """The recorded run's 13 asks: a reading that named the main checkout
        for a commit landing in the declared worktree. Git decides in that
        clone, so the reading says nothing, whatever it read, and the plain
        commit into the undeclared checkout is the one git refuses."""
        for command in (
            f"cd {q(world.w)} && true; git commit -m x",
            "git commit -m x",
            PLAIN_AND_NOT["-m"][0].replace("{d}", q(world.main)),
        ):
            assert pre_bash(world, command, world.main) == "silent", command
        world.change(world.main)
        before = world.head(world.main)
        got = world.sh("git commit -q -m x")
        assert got.returncode != 0
        assert gate.HEADER in got.stderr
        assert world.head(world.main) == before

    @pytest.mark.rule("text-reading-stands-aside")
    @pytest.mark.parametrize(
        "command", [*STILL_PLAIN, *(spelt(s, 0) for s in sorted(PLAIN_AND_NOT))]
    )
    def test_accepts_each_plain_shape_without_git(self, command):
        assert tokens.is_plain(command), command

    @pytest.mark.parametrize("command", NOT_ON_THE_LIST)
    def test_accepts_a_word_the_bypass_list_does_not_read(self, command):
        """The word list alone does not over-read; since P7 the reading also
        judges every shape `is_plain` does not recognise, which the cases
        above pin."""
        assert not tokens.steps_around_hooks(command)

    @pytest.mark.rule("text-reading-stands-aside")
    def test_refuses_a_command_in_a_clone_whose_hooks_slot_is_foreign(self, world):
        """P1 (a), P5 (a): a clone whose hooks slot is somebody else's is
        judged as 0.16.0 judged it."""
        g(world.u, "config", "core.hooksPath", ".husky", home=world.home, session="")
        assert pre_bash(world, f"git -C {q(world.u)} commit -m x", world.main) == "deny"

    @pytest.mark.rule("text-reading-stands-aside")
    @pytest.mark.parametrize(
        "command",
        [
            STEPS_AROUND["-c core.hooksPath"],
            STEPS_AROUND["an unreadable command"],
            STEPS_AROUND["eval of a variable"],
            PLAIN_AND_NOT["-m"][1],
        ],
        ids=["a word the list reads", "unreadable", "an eval", "one word more"],
    )
    def test_refuses_a_command_that_is_not_plain_in_a_clone_git_decides(
        self, world, command
    ):
        """Round 1's yellow 2 and 8, and round 2's yellow 1 and 2: a command
        that can keep git from running the stubs, or the stub from finding
        the session, meets the reading that asked before the command. A
        misread costs one refusal. `{d}` is the undeclared main checkout."""
        command = command.replace("{d}", q(world.main))
        assert pre_bash(world, command, world.main) == "deny", command

    @pytest.mark.rule("text-reading-stands-aside")
    @pytest.mark.parametrize(
        "command",
        [
            *STEPS_AROUND.values(),
            *OTHER_CONDITIONS.values(),
            *(spelt(s, 1) for s in sorted(PLAIN_AND_NOT)),
        ],
    )
    def test_refuses_each_shape_that_is_not_plain_without_git(self, command):
        assert not tokens.is_plain(command), command


test_census = census_case(TARGET)
