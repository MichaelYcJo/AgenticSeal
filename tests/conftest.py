"""The suite's shared helpers and fixtures, and the environment every case runs in.

The module body sets that environment for every case and every child: the
locale, git's template and maintenance, `gh`'s login and `PATH`.
"""

import ast
import atexit
import datetime
import functools
import importlib.util
import io
import json
import os
import pathlib
import re
import shlex
import shutil
import subprocess
import sys
import tempfile

import pytest

# pytest's default `prepend` import mode puts a test file's own directory on
# `sys.path` as it imports that file. A test file that imports a helper from
# a test file in another directory under `tests/` would then find it only
# where pytest happened to import that directory first, and never in a run
# that names the importing file alone. So each directory under `tests/` that
# holds a test file goes on the path here, before pytest imports a test file.
_TESTS = os.path.dirname(os.path.abspath(__file__))
for _directory, _subdirectories, _names in os.walk(_TESTS):
    _subdirectories[:] = sorted(d for d in _subdirectories if d != "__pycache__")
    if (
        _directory != _TESTS
        and _directory not in sys.path
        and any(n.startswith("test_") and n.endswith(".py") for n in _names)
    ):
        sys.path.append(_directory)

# The review run's documents: the record and the run, the hooks, the routing
# check, and what each arm wants. A case that reads one of them for what is
# THERE reads the one that holds the section; a case asserting what is NOT
# there reads all four through `review_chain_text`, because a sentence
# forbidden in one that returns in a sibling is the same sentence back, and
# an absence that holds in one part of the text proves nothing about the rest.
REVIEW_CHAIN_DOCS = (
    ("docs", "the-review-record.md"),
    ("docs", "the-session-hooks.md"),
    ("docs", "the-routing-check.md"),
    ("docs", "the-review-and-parity-arms.md"),
)


def review_chain_text(root):
    """The review chain's documents under `root`, each whitespace-collapsed,
    joined."""
    texts = []
    for parts in REVIEW_CHAIN_DOCS:
        with open(os.path.join(root, *parts), encoding="utf-8") as handle:
            texts.append(" ".join(handle.read().split()))
    return "\n".join(texts)


# --- a workflow's text, read the one way -------------------------------------
#
# No YAML parser is installed anywhere this suite runs, so every case that
# reads `.github/workflows/*.yml` reads text. Each one that re-derived what a
# comment is got it slightly differently: a flag in a comment counted as a
# base (#462), and a comment naming a script moved the region a case sliced
# out (#482). These three helpers are the one reading, driven over fixtures
# in `tests/test_conftest.py`. They are a test helper
# and refuse nothing.


def code_line(line):
    """`line` with any comment taken off, or `None` where all of it is one.

    A line whose first non-blank character is `#` is a comment. So is the
    rest of a line from a `#` that follows a blank and stands outside `"…"`
    and `'…'`: YAML ends a plain scalar there, and inside a `run:` block the
    shell ignores the rest of the line there, so both layers agree it does
    not run. Inside `"…"` a backslash escapes the next character, so `\"`
    does not close the string, as in YAML and the shell alike; `'…'` has no
    escape. A quote is tracked from wherever it stands, so a stray
    apostrophe in a plain scalar keeps a later ` #` as text, which reads a
    comment as code.

    **Not tracked, and named rather than claimed:** quotes are read one line
    at a time, so a double-quoted string that spans lines of a `run: |`
    block is not seen, and a line inside it whose first non-blank character
    is `#` is dropped as a comment. That one drops code. No workflow line in
    this repository had the shape when round 1 of work item 1790297086
    looked for it.
    """
    if line.lstrip().startswith("#"):
        return None
    quote, escaped = None, False
    for i, c in enumerate(line):
        if escaped:
            escaped = False
        elif quote:
            if quote == '"' and c == "\\":
                escaped = True
            elif c == quote:
                quote = None
        elif c in "\"'":
            quote = c
        elif c == "#" and i > 0 and line[i - 1] in " \t":
            return line[:i].rstrip()
    return line


def code_lines(text):
    """`text` with every comment removed, one line per line that is code."""
    return [kept for kept in map(code_line, text.splitlines()) if kept is not None]


def _indent(line):
    return len(line) - len(line.lstrip(" "))


def _unquote(value):
    """A YAML scalar with its matching quotes off, as `broad_gate.py#unquote`
    reads a step's name."""
    for mark in ('"', "'"):
        if len(value) >= 2 and value.startswith(mark) and value.endswith(mark):
            return value[1:-1]
    return value


_STEP_NAME = re.compile(r"^\s*-\s+name:\s*(\S.*?)\s*$")


def workflow_steps(text):
    """Every step of every job's `steps:` list: `(name, code lines)` pairs.

    A step runs from its `- ` at the list's own indentation to the next item
    at that indentation, or to the first code line shallower than the list,
    which is the next key of its job or the next job. A step's code lines
    keep their blank ones. `name` is the step's
    `- name:` value, read the way `broad_gate.py#STEP_RE` and `#unquote` read
    it, or `None` for a step with no name (`- uses: …`).
    """
    lines = code_lines(text)
    steps, i = [], 0
    while i < len(lines):
        if lines[i].strip() != "steps:":
            i += 1
            continue
        floor, i, level = _indent(lines[i]), i + 1, None
        # A blank line ends nothing: `run: |` blocks and the gaps between
        # steps both carry them.
        while i < len(lines) and (not lines[i].strip() or _indent(lines[i]) > floor):
            line = lines[i]
            if level is None and line.lstrip().startswith("- "):
                level = _indent(line)
            if (
                level is not None
                and _indent(line) == level
                and line.lstrip()[:2] == "- "
            ):
                steps.append([None, []])
                named = _STEP_NAME.match(line)
                if named:
                    steps[-1][0] = _unquote(named.group(1))
            if steps and level is not None:
                steps[-1][1].append(line)
            i += 1
    return [(name, "\n".join(block)) for name, block in steps]


def workflow_step(text, name):
    """The code lines of the one step called `name`. Asserts there is one."""
    found = [block for called, block in workflow_steps(text) if called == name]
    assert len(found) == 1, f"{len(found)} steps are called {name!r}"
    return found[0]


def step_running(text, script):
    """The code lines of the one step whose code names `script`. Asserts
    there is one, so a comment naming it can never move the region."""
    found = [block for _, block in workflow_steps(text) if script in block]
    assert len(found) == 1, f"{len(found)} steps run {script!r}"
    return found[0]


def _build_repo(d):
    """`git init` a repo at `d`, with one committed file and a feature branch."""
    git = lambda *a: subprocess.run(
        ["git", "-C", str(d), *a],
        check=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    git("init", "-q")
    git("config", "user.email", "t@t")
    git("config", "user.name", "t")
    (d / "f.txt").write_text("one\ntwo\nthree\n", encoding="utf-8")
    git("add", "-A")
    git("commit", "-qm", "base")
    git("branch", "feature/x")


def build_tracked_tree(d, files, deleted=()):
    """A repository at `d` holding `files`, with `deleted` removed from disk.

    `files` is `{relative path: text}`; every one of them is committed, and
    each entry of `deleted` is then unlinked WITHOUT staging the removal, so
    it stays in the index and leaves the working tree. That is the state the
    documented release sequence produces at step 3 of
    `docs/release-checklist.md`, and the state `on_disk` below is about.

    A real `git init` rather than a directory of files, for the reason
    `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#test_the_templates_check_reads_prose_only_and_descends`
    already records: a fixture git never sees would report nothing and the
    case would pass having exercised nothing. `GIT_TEMPLATE_DIR` is emptied
    above, so the `git init` costs almost nothing.
    """
    d = pathlib.Path(d)
    d.mkdir(parents=True, exist_ok=True)
    git = lambda *a: subprocess.run(
        ["git", "-C", str(d), *a],
        check=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    git("init", "-q")
    git("config", "user.email", "t@t")
    git("config", "user.name", "t")
    for rel, text in files.items():
        p = d / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    git("add", "-A")
    git("commit", "-qm", "base")
    for rel in deleted:
        (d / rel).unlink()
    return d


def git_listing(root, *args, check=False):
    """The paths `git <args>` names under `root`, whitespace-split.

    One spelling of a block six helpers had copied (round 1 ⬜ 8). `-C <root>`
    rather than `cwd=`, so the path the command acts on is written out.

    **The listing WORDS stay at the call site on purpose.**
    `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` finds a scope that
    derives a path list by the string constants the call itself names, so
    moving `ls-files` in here would take every one of those scopes out of the
    class it enumerates — the check going quiet on the very refactor that was
    meant to tidy it.
    """
    return subprocess.run(
        ["git", "-C", str(root), *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        check=check,
    ).stdout.split()


def on_disk(root, listed):
    """Split a git path listing into what is on disk and what is not.

    `git ls-files` lists the INDEX, so a tracked file the working tree has
    deleted is on the list with nothing behind it. A walk that opens every
    listed path ends there with a `FileNotFoundError`, no file after it is
    read, and the rule the walk holds reports nothing at all (#432, #282).

    **The missing half is returned rather than dropped.** A sweep that judges
    what it finds is strictly better off for the skip -- on this tree it used
    to report nothing about any file. A case that reads the corpus to prove an
    entry is still ALIVE is not: to it a skipped file and a deleted entry are
    the same evidence, so a silent skip buys it a false alarm. Those callers
    hand the missing list to `decline_if_shrunken`; a positive sweep judges
    what remains and ignores it.
    """
    present, missing = [], []
    for rel in listed:
        (present if os.path.isfile(os.path.join(root, rel)) else missing).append(rel)
    return present, missing


def shrunken_corpus(missing, what):
    """The reason a case gives when its verdict needs the whole corpus.

    Every path by name rather than a count. A claim removed from a corpus
    without a word is the direction `seal/follow-up.md`'s first row calls the
    one a checker of claims must not fail in, and a bare number is that
    silence with a digit in front of it -- the reader cannot tell which entry
    went unjudged, which is the one thing they need in order to judge it by
    hand.
    """
    return (
        f"{len(missing)} tracked path(s) are listed by git and not on disk, so "
        f"{what} cannot tell a file this run skipped from an entry that is "
        "really gone, and is not judging. Missing: " + ", ".join(sorted(missing))
    )


def decline_if_shrunken(missing, what):
    """`pytest.skip` with `shrunken_corpus`'s reason when anything is missing."""
    if missing:
        pytest.skip(shrunken_corpus(missing, what))


def gathered_entry(root, work_item_id):
    """The text a release file under `changelog/` carries for a work item
    whose fragment was gathered, or None when no marker for it is there.

    A changelog fragment moves once, the way a ledger fragment does:
    `gather_changelog.py` writes `<!-- specs/<id> -->` above the fragment's
    body in the release's own file, `changelog/X.Y.Z.md` since #728, and
    `seal settle --apply` later removes the directory the fragment lived in. So a
    case pinning what a fragment says reads the fragment while it exists and
    this block after. The block runs from the marker to the next marker line
    or heading, which is where the gatherer puts the next entry.
    """
    start = f"<!-- specs/{work_item_id} -->"
    directory = os.path.join(root, "changelog")
    names = sorted(os.listdir(directory)) if os.path.isdir(directory) else []
    for name in names:
        if not re.fullmatch(r"\d+\.\d+\.\d+\.md", name):
            continue
        with open(os.path.join(directory, name), encoding="utf-8") as handle:
            lines = handle.read().splitlines()
        if start in lines:
            break
    else:
        return None
    body = []
    for line in lines[lines.index(start) + 1 :]:
        # A heading is `#` to `######` and then a space: a body line opening
        # with an issue number such as `#120` is the entry's own text.
        if re.match(r"#{1,6}(?:\s|$)", line) or (
            line.startswith("<!-- specs/") and line.endswith("-->")
        ):
            break
        body.append(line)
    return "\n".join(body)


HOOKS = os.path.join(os.path.dirname(__file__), "..", "hooks")

# Default-locale determinism: the suite owns its locale. A plain setdefault
# is not enough — the author's machine exports SPECSEAL_LANG=ko session-wide
# (measured), which would flip every default-language assertion. The plugin
# option `worktree_guard_language` is read before it, so a value the shell
# running the suite carries for the option is removed. Tests that need Korean
# monkeypatch the env and fresh-load the module.
os.environ["SPECSEAL_LANG"] = "en"
os.environ.pop("CLAUDE_PLUGIN_OPTION_WORKTREE_GUARD_LANGUAGE", None)

# One run of this suite calls `git init` 403 times, and each call copies the
# default template into the new repository: 18 files where 2 are enough, 14 of
# them sample hooks that nothing in this suite runs or reads. That is roughly
# 6,400 files created and never opened again -- free on a filesystem that
# creates files cheaply, and not free on windows, where the virus scanner
# opens each one as it appears.
#
# Set here rather than at the fifteen `git init` call sites, because `git`
# reads the template location from the environment and the tests should not
# each have to remember. An empty template still leaves a complete repository:
# `config`, `HEAD`, `objects/` and `refs/` are `git init`'s own work, not the
# template's.
_EMPTY_GIT_TEMPLATE = tempfile.mkdtemp(prefix="agentic-empty-git-template-")
os.environ["GIT_TEMPLATE_DIR"] = _EMPTY_GIT_TEMPLATE
atexit.register(shutil.rmtree, _EMPTY_GIT_TEMPLATE, True)

# `git commit` forks a detached `git maintenance run --auto` when
# maintenance.auto is on (the default), which keeps touching
# `.git/objects/` -- creating and removing `maintenance.lock` -- after the
# `commit` call has already returned. Several fixtures in this suite build
# one repository and `shutil.copytree` it into many tests, so that detached
# process racing a copy is no longer a one-in-many-runs coincidence: it read
# `.git/objects/maintenance.lock`'s directory entry, then found the file gone
# by the time it opened it, and failed the copy (observed on ubuntu CI).
# Disabled through the environment, not a global git config write, so a
# developer's own `maintenance.auto` setting is untouched.
os.environ["GIT_CONFIG_COUNT"] = "1"
os.environ["GIT_CONFIG_KEY_0"] = "maintenance.auto"
os.environ["GIT_CONFIG_VALUE_0"] = "false"

# The suite runs with `gh` logged out, on every machine (#510). CI's pytest job
# has no token, so a case that falls through its stubs onto a live `gh` fails
# there -- and passed on every developer's machine and under the broad gate,
# because `gh` is logged in on both. Nothing local could see that class; CI
# found it after the branch was sealed.
#
# `gh` looks for its login in three places, in this order: a token variable,
# `hosts.yml` under its config directory, and the OS keyring. It reads the
# keyring even where no `hosts.yml` exists: `ActiveToken` falls back to the
# host's active-account slot, which `gh auth login` fills by default. Emptying
# the config directory hides only the second place. So the two variables `gh`
# reads first are SET, to a value no server accepts, and `gh` never reaches
# the keyring; the other two are removed. This happens at import, so every
# entry point (`bin/test`, bare `pytest`, the `uvx` fallback, each xdist
# worker) and every child that inherits `os.environ` sees it -- CI included,
# where a stray call now fails the same way it fails here: with a 401 from the
# server, instead of "gh auth login". A case that needs `gh` stubs it.
GH_CREDENTIALS = (
    "GH_TOKEN",
    "GITHUB_TOKEN",
    "GH_ENTERPRISE_TOKEN",
    "GITHUB_ENTERPRISE_TOKEN",
)
# Not a credential: what `gh` finds in place of one.
NOT_A_GH_TOKEN = "agentic-suite-runs-with-gh-logged-out"
_EMPTY_GH_CONFIG = tempfile.mkdtemp(prefix="agentic-empty-gh-config-")
os.environ["GH_CONFIG_DIR"] = _EMPTY_GH_CONFIG
atexit.register(shutil.rmtree, _EMPTY_GH_CONFIG, True)
for _name in GH_CREDENTIALS:
    os.environ.pop(_name, None)
os.environ["GH_TOKEN"] = NOT_A_GH_TOKEN
os.environ["GH_ENTERPRISE_TOKEN"] = NOT_A_GH_TOKEN

# The suite runs with no workflow variable, under every event (#1058). Every
# workflow run sets `GITHUB_ACTIONS`, `GITHUB_EVENT_PATH` and the rest, and
# only a `pull_request` run sets `GITHUB_HEAD_REF`; a local run and the broad
# gate set none. Three cases that judged the checked-out branch passed on a
# local run, the broad gate and a `workflow_dispatch` run, and failed on pull
# request #1057's run (`gh run view 40446828473 --log-failed`), because the
# script they drove reads `GITHUB_HEAD_REF` first. So every name that starts
# with `GITHUB_` is removed here, at import, for the reason the block above
# is: every entry point, every fixture of every scope and every child that
# inherits `os.environ` sees the same environment.
# The names are read from the environment itself, so a variable a script
# starts reading later is covered without an edit here. A case that needs one
# sets it with `monkeypatch.setenv`. The limit: code that runs in this process
# and needs the runner's real value, such as a pytest hook writing the step
# summary, has to read it before this file is imported.
for _name in [n for n in os.environ if n.startswith("GITHUB_")]:
    del os.environ[_name]

# `chain_check.py` asks `gh pr view --json isDraft` where no event payload
# exists (#866), and every run of it the generator and the broad gate make in
# this suite is such a run. A stub named `gh`, first on PATH from import,
# answers that one question and passes every other call to the `gh` that was
# on PATH, so `gh auth token` and the `PR` cell's question reach it as they
# did. Its default is the answer a branch with no pull request gets — exit 1,
# which the check reads as UNKNOWN and does not judge as a ready pull request
# (round 1's 🟡 2 of #866). A case that means a draft or a ready pull request
# says so (`gh_answers`).
# A child that imports this file again -- an xdist worker, a probe that runs
# it -- inherits a PATH that already holds a parent's stubs, so the real `gh`
# is looked for past every one of them.
GH_STUB_PREFIX = "agentic-gh-stubs-"
REAL_GH = shutil.which(
    "gh",
    path=os.pathsep.join(
        p
        for p in os.environ.get("PATH", "").split(os.pathsep)
        if GH_STUB_PREFIX not in p
    ),
)
GH_DRAFT_ARGS = ["pr", "view", "--json", "isDraft"]
GH_STATES = {
    "draft": '{"isDraft":true}',
    "ready": '{"isDraft":false}',
    # What `gh` printed with no pull request for the branch, measured
    # 2026-10-08 (`questions.md` M1 of 1791384155).
    "unknown": None,
}
_GH_STUBS = tempfile.mkdtemp(prefix=GH_STUB_PREFIX)
atexit.register(shutil.rmtree, _GH_STUBS, True)
GH_STUB_SCRIPT = """import subprocess, sys
ANSWER, REAL, ASKED = {answer!r}, {real!r}, {asked!r}
if sys.argv[1:] == ASKED:
    if ANSWER is None:
        sys.stderr.write('no pull requests found for branch "x"\\n')
        sys.exit(1)
    sys.stdout.write(ANSWER + "\\n")
    sys.exit(0)
if REAL is None:
    sys.stderr.write("gh: not on PATH under this suite\\n")
    sys.exit(1)
sys.exit(subprocess.call([REAL, *sys.argv[1:]]))
"""


def _write_gh_stub(state):
    """The directory holding a `gh` that answers STATE, written once."""
    home = os.path.join(_GH_STUBS, state)
    os.makedirs(home, exist_ok=True)
    script = os.path.join(home, "gh_stub.py")
    with open(script, "w", encoding="utf-8") as handle:
        handle.write(
            GH_STUB_SCRIPT.format(
                answer=GH_STATES[state], real=REAL_GH, asked=GH_DRAFT_ARGS
            )
        )
    if os.name == "nt":
        with open(os.path.join(home, "gh.cmd"), "w", encoding="utf-8") as handle:
            handle.write(f'@"{sys.executable}" "{script}" %*\r\n')
    else:
        stub = os.path.join(home, "gh")
        with open(stub, "w", encoding="utf-8") as handle:
            handle.write(f'#!/bin/sh\nexec "{sys.executable}" "{script}" "$@"\n')
        os.chmod(stub, 0o755)
    return home


GH_STUB_DIRS = {state: _write_gh_stub(state) for state in GH_STATES}


def gh_answers(env, state):
    """ENV with the `gh` that answers STATE first on its PATH, and no other
    of the suite's stubs anywhere on it."""
    parts = [
        p
        for p in env.get("PATH", "").split(os.pathsep)
        if p and GH_STUB_PREFIX not in p
    ]
    return {**env, "PATH": os.pathsep.join([GH_STUB_DIRS[state], *parts])}


os.environ["PATH"] = gh_answers(dict(os.environ), "unknown")["PATH"]


# The worktree guard reads the routing answer out of the session's transcript
# under `worktree_consent.PROJECTS_ROOT`, which is `~/.claude/projects` -- the
# real transcripts of whoever runs this suite. Every in-process case points it
# at an empty directory instead, so none reads a real transcript: the guard
# imports the module by its plain name, so one attribute on `sys.modules`
# covers every copy of the guard a test module loaded. A case that needs a
# transcript points it somewhere else itself.
_NO_TRANSCRIPTS = tempfile.mkdtemp(prefix="agentic-no-transcripts-")
atexit.register(shutil.rmtree, _NO_TRANSCRIPTS, True)


@pytest.fixture(autouse=True)
def _no_real_transcripts(monkeypatch):
    consent = sys.modules.get("worktree_consent")
    if consent is not None and hasattr(consent, "PROJECTS_ROOT"):
        monkeypatch.setattr(consent, "PROJECTS_ROOT", _NO_TRANSCRIPTS)


# What a Claude Code session exports to every Bash child, and so to every git
# hook a fixture repository's stub runs (#692, `trail/phases/phase-1.md` M4). A
# suite run from inside a session inherits them and CI does not, so a stub
# would judge a fixture's commit on one and stay silent on the other (P2).
# Every case starts with none of them; a case about a session sets its own.
SESSION_VARIABLES = (
    "CLAUDECODE",
    "CLAUDE_CODE_SESSION_ID",
    "CLAUDE_PID",
    "CLAUDE_CODE_CHILD_SESSION",
    "CLAUDE_CODE_SESSION_ATTENDED",
    "CLAUDE_CODE_ENTRYPOINT",
)


@pytest.fixture(autouse=True)
def _no_session_in_the_environment(monkeypatch):
    for name in SESSION_VARIABLES:
        monkeypatch.delenv(name, raising=False)


def load_hook_module(filename, name):
    """The file at FILENAME under `hooks/`, a gate by its name and a module
    as `lib/<name>`, run as a module named NAME. FILENAME is split on `/`, so
    the path is joined from single segments on every platform."""
    spec = importlib.util.spec_from_file_location(
        name, os.path.join(HOOKS, *filename.split("/"))
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# `hooks/lib/optin.py#MARKER`: a `seal/` is the plugin's root only where its
# `README.md` opens with this line, so every helper below that builds a root
# writes it.
ROOT_MARKER = load_hook_module("lib/optin.py", "agentic_optin_for_fixtures").MARKER


def mark_root(home):
    """HOME made a directory whose `README.md` opens with the marker, the way
    first setup leaves a root, and returned. A README already there is left
    as it is."""
    home = pathlib.Path(home)
    home.mkdir(parents=True, exist_ok=True)
    readme = home / "README.md"
    if not readme.exists():
        readme.write_text(ROOT_MARKER + "\n", encoding="utf-8")
    return home


def run_hook(filename, payload, env=None):
    """Feed a hook the stdin JSON the harness would send; return its stdout."""
    r = subprocess.run(
        [sys.executable, os.path.join(HOOKS, *filename.split("/"))],
        input=json.dumps(payload),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
        env={**os.environ, **(env or {})},
    )
    return r.stdout


def decision_of(stdout):
    """'silent' when a hook allowed by staying quiet, else its decision.
    STDOUT is the hook's output as text, or the finished process whose
    output is bytes, as a case run on a hostile console holds it."""
    if isinstance(stdout, subprocess.CompletedProcess):
        stdout = stdout.stdout.decode("utf-8")
    if not stdout.strip():
        return "silent"
    return json.loads(stdout)["hookSpecificOutput"]["permissionDecision"]


def fired(stdout):
    """True when a gate stopped the call at all.

    A gate with two ways on denies the FIRST time a session meets it in a
    repository — spending the reason on the question — and asks on every
    attempt after that. Detection tests care that the gate saw the command,
    not which of the two prompts it produced; the shape has tests of its own.
    """
    return decision_of(stdout) in ("deny", "ask")


# Told apart by `shell_probe` below, and the caller is expected to act on the
# difference: one is a name that was never a shell, the other is a shell whose
# environment ate the answer.
NOT_A_SHELL = "not a shell here"
ATE_THE_PROBE = "its environment ate the probe"


def shell_probe(name):
    """Why `name` on PATH is not usable as a shell here, or None if it is.

    `shutil.which` was the whole question once, and on a `windows-latest`
    runner it resolves `bash` to `C:/Windows/System32/bash.exe` -- the WSL
    launcher, with no distribution installed. That is not a shell: it exits
    non-zero and prints an install notice in UTF-16, which arrives here as a
    string full of NUL bytes.

    The two ways to fail are not the same failure, and a caller that cannot
    tell them apart either fails on a name that was never a shell or stays
    quiet when a real one drops out:

      - a non-zero exit is a name that is not a shell at all, and the runner's
        `bash` is exactly that;
      - a zero exit with the wrong answer is a working shell whose environment
        wrote to stdout first. `zsh` sources `.zshenv` even non-interactively,
        so one `echo` in a developer's own removes it from the run.
    """
    try:
        r = subprocess.run(
            [name, "-c", "printf ok"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=15,
        )
    except (OSError, subprocess.SubprocessError) as e:
        return f"did not run ({type(e).__name__}) -- {NOT_A_SHELL}"
    if r.returncode != 0:
        return f"exited {r.returncode} -- {NOT_A_SHELL}"
    if r.stdout.strip() != "ok":
        return f"answered {r.stdout.strip()!r}, not 'ok' -- {ATE_THE_PROBE}"
    return None


def symlink_or_skip(target, link):
    """`os.symlink(target, link)`, or skip the test where it is not permitted.

    Windows needs SeCreateSymbolicLinkPrivilege -- Developer Mode, or an
    elevated shell. A GitHub `windows-latest` runner has it and an ordinary
    developer machine does not, so `skipif(os.name == "nt")` and a bare
    `os.symlink` are both wrong in one direction each: the first drops the
    coverage where the privilege IS held, the second turns a missing
    privilege into a red suite for code nobody touched.

    Asked by attempting the call, because that is the only thing that answers
    it. Nothing is inferred from the platform.
    """
    # A missing parent is a fixture bug, and every one of its errors is an
    # `OSError` too -- so without this the skip would swallow it and the case
    # would read as "no privilege here" on a machine that has one.
    parent = os.path.dirname(os.path.abspath(str(link)))
    assert os.path.isdir(parent), f"the link's parent does not exist: {parent}"
    try:
        os.symlink(target, link)
    except OSError as exc:
        pytest.skip(f"symbolic links are not available here ({exc})")


def ps_names_the_parent_or_skip(limit):
    """Skip unless `ps -o ppid=,comm= -p <pid>` names this process's parent.

    That call is how the hooks walk up to the `claude` process: the commit
    gate's lease route and old spelling (`hooks/lib/hooksession.py`) and the
    worktree guard's count of other sessions. Git for Windows' `ps` takes no
    `-o`, so on a `windows-latest` runner every one of them finds nothing,
    and a case resting on the walk has no behaviour to pin there. LIMIT names
    the documented known limit the skip rests on (#692).

    Asked by attempting the call, for the reason `symlink_or_skip` gives:
    a Windows machine with another `ps` keeps the coverage, and nothing is
    inferred from the platform.
    """
    try:
        r = subprocess.run(
            ["ps", "-o", "ppid=,comm=", "-p", str(os.getpid())],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=15,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        pytest.skip(f"{limit} -- `ps` could not be run here ({exc})")
    parent = r.stdout.strip().partition(" ")[0]
    if r.returncode != 0 or parent != str(os.getppid()):
        pytest.skip(
            f"{limit} -- `ps -o ppid=,comm= -p` does not name a parent here "
            f"(exit {r.returncode})"
        )


def fifo_or_skip(path):
    """`os.mkfifo(path)`, or skip the test where it is not available.

    Asked by attempting the call, for the reason `symlink_or_skip` gives:
    `os.mkfifo` does not exist on Windows at all, and on a POSIX filesystem
    that has no named pipes it raises. Nothing is inferred from the platform.
    """
    parent = os.path.dirname(os.path.abspath(str(path)))
    assert os.path.isdir(parent), f"the fifo's parent does not exist: {parent}"
    maker = getattr(os, "mkfifo", None)
    if maker is None:
        pytest.skip("named pipes are not available here (no os.mkfifo)")
    try:
        maker(path)
    except OSError as exc:
        pytest.skip(f"named pipes are not available here ({exc})")


# What a POSIX shell answers, and what `cmd.exe` prints back verbatim.
POSIX_ROW_PROBE = "echo one; echo $(echo two)"


def posix_row_shell_or_skip():
    """Skip unless the shell behind `shell=True` here separates commands with
    `;` and substitutes `$(…)` — the two things a `Broad gate` row's fixture
    can be ABOUT.

    `broad_gate.run` hands the row to `subprocess(shell=True)`, which is
    `/bin/sh` on POSIX and `%COMSPEC%` — normally `cmd.exe` — on Windows.
    `cmd.exe` has neither: `echo a; echo b` is one `echo` that succeeds, and
    `$(echo x)` is a literal argument. So a fixture row written to fail, or
    to substitute, does neither there — and a case built on one is not
    failing to reproduce a defect, it has no defect to reproduce.

    **This is `symlink_or_skip`'s rule followed, not excepted.** That rule is
    *ask by attempting*, and the thing to attempt here is exactly which shell
    will run the row — asked through the same call the gate makes, so the
    answer is the gate's own shell rather than a guess from `os.name`.
    `skipif(os.name == "nt")` would be wrong in both of the directions that
    rule names: it drops the coverage on a Windows machine whose `COMSPEC` is
    a POSIX shell, and it keeps asserting on a POSIX machine whose `/bin/sh`
    is something nobody expected.

    A case that only reads a REFUSAL needs none of this. `not_as_written` is
    a string test that reaches no shell, and the refusal is right on both
    platforms — `templates/setup/config.md` names what each shell does with the
    forms it lists.
    """
    try:
        r = subprocess.run(
            POSIX_ROW_PROBE,
            shell=True,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=15,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        pytest.skip(f"the shell behind `shell=True` could not be probed ({exc})")
    if r.returncode != 0 or r.stdout.split() != ["one", "two"]:
        pytest.skip(
            f"`shell=True` here is not a POSIX shell: {POSIX_ROW_PROBE!r} "
            f"answered {r.stdout.strip()!r} (exit {r.returncode}). A `;` "
            "separator and `$(…)` substitution are what this case's row is "
            "made of, and this shell has neither"
        )


def local_home(repo):
    """Create `<git-common-dir>/seal/` for `repo` and return its path.

    The local-mode root (#80). Asked of git rather than spelled `.git/seal`,
    because in a linked worktree `.git` is a FILE and the root belongs to
    the main tree's common directory, which is what the hooks read.
    """
    common = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "--git-common-dir"],
        check=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    ).stdout.strip()
    home = pathlib.Path(os.path.normpath(os.path.join(str(repo), common))) / "seal"
    return mark_root(home)


@pytest.fixture
def local(repo):
    """The `repo` fixture in local mode: `seal/` under `.git/` and nowhere
    else."""
    home = local_home(repo)
    assert not (repo / "seal").exists()
    return repo, home


def declare_routing(
    repo, item="1787708604-a-work-item", review="through the review chain", home=None
):
    """Write a routing declaration for the repo's current branch, and return
    the work-item directory the round records now live in.

    Everything that used to key on a pull request number keys on this: the
    declaration names its branch, and the checked-out branch looks it up.

    `home` is the root to write under when it is not `<repo>/seal/` -- the
    path `local_home` returned, for a local-mode fixture.
    """
    branch = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "--abbrev-ref", "HEAD"],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    ).stdout.strip()
    d = mark_root(home if home else repo / "seal") / "threads" / item
    d.mkdir(parents=True, exist_ok=True)
    (d / "routing.md").write_text(
        f"# {item} -- routing\n\n"
        "| Axis | Answer |\n|---|---|\n"
        f"| Review | {review} |\n"
        "| Destination | open the pull request |\n"
        f"| Branch | {branch} |\n",
        encoding="utf-8",
    )
    return d


def rounds_dir(item):
    """`<item>/trail/rounds/`, created. Where the round records live.

    A helper rather than `item / "trail" / "rounds"` at each call site: the
    tests that write a record are the ones that would keep an old path alive,
    and one spelling is what makes moving it again a single edit.
    """
    d = item / "trail" / "rounds"
    d.mkdir(parents=True, exist_ok=True)
    return d


@pytest.fixture(scope="session")
def _repo_template(tmp_path_factory):
    """One built repo, shared for the session; `repo` copies it per test."""
    d = tmp_path_factory.mktemp("repo-template")
    _build_repo(d)
    return d


@pytest.fixture
def repo(tmp_path, _repo_template):
    """A git repo with one committed file and a feature branch to switch to."""
    d = tmp_path / "repo"
    shutil.copytree(_repo_template, d)
    return d


# --- a slow case is named (#841, #942) ----------------------------------------
#
# A wall-clock total hides the case that pushed it, so the run names each
# case whose call ran past this many seconds, in its terminal summary, and
# fails nothing for it (`CONTRIBUTING.md` *Running the checks* says why).
# Work item 1791270165 set the value at 1.5 times the slowest call on the
# Windows leg, rounded up to 30 s.
SLOW_CASE_S = 90


def slow_lines(reports):
    """One line for each call in REPORTS that ran past `SLOW_CASE_S`, naming
    the case and its seconds, slowest first. A setup or a teardown is not
    read: fixture building is a module's cost, not a case's."""
    slow = [r for r in reports if r.when == "call" and r.duration > SLOW_CASE_S]
    slow.sort(key=lambda r: -r.duration)
    return [
        f"slow case: {r.nodeid} ran {r.duration:.1f} s, past SLOW_CASE_S of {SLOW_CASE_S} s"
        for r in slow
    ]


def pytest_terminal_summary(terminalreporter):
    """Write `slow_lines` over every report of the run. Under xdist the
    controller holds the workers' reports, so one summary names them all."""
    reports = [r for kind in terminalreporter.stats.values() for r in kind]
    reports = [r for r in reports if hasattr(r, "when") and hasattr(r, "duration")]
    for line in slow_lines(reports):
        terminalreporter.write_line(line)


# --- a module's file runs the censuses over its module (#942) ------------------


def census_case(target):
    """The case a module file ends with, `test_census = census_case(TARGET)`:
    every census in `tests/censuses.py` over TARGET, so the run a
    contributor makes of one module judges that module under every census."""

    def test_census():
        import censuses

        problems = censuses.judge(target)
        assert not problems, "\n".join(problems)

    test_census.__doc__ = f"Every census in tests/censuses.py over {target}."
    return test_census


# --- the marker a check line names --------------------------------------------


def pytest_configure(config):
    """Register `rule`, the marker a gate test carries for the `check:` line
    that names it (`.github/scripts/rules.py#markers`), so pytest reads it
    without an unknown-mark warning."""
    config.addinivalue_line(
        "markers", "rule(name): the rule a `check:` line names by this marker"
    )


def rule_carriers(marker):
    """The qualified names of the tests that carry MARKER, as
    `.github/scripts/rules.py#markers` reads them over this repository, so a
    case pinning a rule's check line reads its tests the one way."""
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(root, ".github", "scripts", "rules.py")
    spec = importlib.util.spec_from_file_location("agentic_rules_carriers", path)
    rules = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rules)
    return {name for _path, name, _doc in rules.markers(root).get(marker, [])}


# Every character `str.splitlines` ends a line at and GFM does not.
SPLITLINES_ONLY = [chr(c) for c in (0x0B, 0x0C, 0x1C, 0x1D, 0x1E, 0x85, 0x2028, 0x2029)]
# Two of them by name, built from the code point, for the readers' cases that
# put one mid-line: an escape typed into an editing tool can come back as the
# character itself.
LS = chr(0x2028)
FF = chr(0x0C)


def texts():
    """Every shape the copies could part on: each line end GFM has, each of
    the eight mid-line and at a line end, no trailing newline, and nothing."""
    out = ["", "a", "a\n", "a\n\n", "\n", "a\nb", "a\r\nb\r\n", "a\rb\r", "a\r\n\r\n"]
    for char in SPLITLINES_ONLY:
        out += [f"a{char}b\n", f"a{char}\nb", f"{char}", f"a\n{char}\n\nc{char}"]
    return out


# --- the durations file prices the suite (#874) -------------------------------
#
# `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#
# test_the_durations_file_prices_the_suite` compares the suite's collection
# with `.test_durations`, and on a shard the items a case can see are only the
# shard's own: `pytest-split` replaces the list with the group.
COLLECTED_NODE_IDS = "agentic_collected_node_ids"


def pytest_collection_modifyitems(session, items):
    """Record every collected node id on the session, under
    `COLLECTED_NODE_IDS`, and change nothing.

    It must run before `pytest-split`'s hook, which is `trylast` and replaces
    `items[:]` with the shard's group, and it does: a hook with no ordering
    mark in a `conftest.py` is called before a `trylast` one. `-k` and
    `--deselect` trim the list after it as well, so the record is the whole
    collection on a shard as on ubuntu, and a case selected alone by `-k`
    still reads the suite. Under xdist each worker collects the whole suite
    and runs this hook itself.
    """
    setattr(session, COLLECTED_NODE_IDS, [item.nodeid for item in items])


def posix_id(value, sep=os.sep):
    """A parametrized path's id written with `/`, or None for a value that is
    not a string, which leaves pytest its own id.

    `.test_durations` is measured on Windows and read on every leg, so an id
    has to be one spelling on every machine: `os.path.join` writes `\\` on
    Windows, and the file then prices that case on Windows alone. Pass it as
    `ids=` where a parametrization's values are paths. `sep` is the platform's
    separator unless a case hands it Windows' to read this on POSIX.
    """
    if not isinstance(value, str):
        return None
    return value.replace(sep, "/")


def names_path(path, text):
    """Whether `text` names `path`, as written or as an `OSError` spells it.

    `str(OSError)` quotes the filename with `repr`, which doubles every
    backslash, so on Windows the path a refusal quotes from one is not the
    path as written. `chain_check.py` quotes one; the three loaders #590
    fixed write the path themselves."""
    return path in text or repr(path)[1:-1] in text


# --- helpers more than one test module uses (#942) ----------------------------
#
# Each was defined byte-identically in two or more test modules. A module
# imports the one it needs. A helper that reads a module the case loaded
# itself, such as the worktree guard or the chain check, takes that module as
# its first argument, and the case's module binds it with `functools.partial`.

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def read(*parts):
    """The text of the file at PARTS, joined under the repository root; an
    absolute path is read where it stands."""
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as handle:
        return handle.read()


def read_lossy(path):
    """The text of the file at PATH, each byte that is not UTF-8 read as the
    replacement character."""
    with open(path, encoding="utf-8", errors="replace") as handle:
        return handle.read()


def flat(*parts):
    """`read`'s text as one line, so a pinned phrase survives re-wrapping."""
    return flattened(read(*parts))


def flattened(text):
    """TEXT as one line, each run of whitespace one space."""
    return " ".join(text.split())


def repo_relative(path):
    """PATH relative to the repository root, written with `/`."""
    return posix_id(os.path.relpath(path, ROOT))


def load_module(path, name):
    """The Python file at PATH, run as a module named NAME, the arguments in
    `load_hook_module`'s order."""
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load(relative, name):
    path = os.path.join(ROOT, *relative.split("/"))
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def git_repo(where):
    where.mkdir(parents=True, exist_ok=True)
    for args in (
        ["init", "-q"],
        ["config", "user.email", "t@t.example"],
        ["config", "user.name", "t"],
    ):
        subprocess.run(
            ["git", "-C", str(where), *args], check=True, capture_output=True
        )
    (where / "f.txt").write_text("one\n", encoding="utf-8")
    subprocess.run(
        ["git", "-C", str(where), "add", "-A"], check=True, capture_output=True
    )
    subprocess.run(
        ["git", "-C", str(where), "commit", "-qm", "base"],
        check=True,
        capture_output=True,
    )
    return where


def lease_dir(repo):
    d = os.path.join(str(repo), ".git", "agentic-leases")
    os.makedirs(d, exist_ok=True)
    return d


def stub_process_tree(monkeypatch, start, tree):
    """`ps -o ppid=,comm= -p <pid>` against a fixture tree of {pid: (ppid, comm)},
    the walk starting at START as this process's parent.

    Only `ps` is faked; everything else (git, notably) reaches the real
    subprocess, so a hook's `main` can still resolve the repo. The hooks
    read `os.getppid` and `subprocess.run` off the modules every caller
    shares, so those are what is replaced.
    """
    import types

    real_run = subprocess.run
    monkeypatch.setattr(os, "getppid", lambda: start)

    def fake_run(cmd, **kwargs):
        if not (isinstance(cmd, (list, tuple)) and cmd and cmd[0] == "ps"):
            return real_run(cmd, **kwargs)
        pid = int(cmd[-1])
        if pid not in tree:
            return types.SimpleNamespace(stdout="")
        ppid, comm = tree[pid]
        return types.SimpleNamespace(stdout=f"{ppid} {comm}\n")

    monkeypatch.setattr(subprocess, "run", fake_run)


def run(module, monkeypatch, payload):
    monkeypatch.setattr(sys, "stdin", io.StringIO(json.dumps(payload)))
    module.main()


# A `config.md` text with its `Item | Value` table; `{rows}` takes the rows.
TABLE = "# Repository config\n\n| Item | Value |\n|---|---|\n{rows}"


@pytest.fixture
def config():
    return load_hook_module("lib/config.py", "agentic_config_for_tests")


# The config texts the reader's cases in `tests/hooks/test_config.py` and the
# writer's in `tests/skills/test_seal.py` both read. A row
# that parses comes first in the piped table, because the walker stops at the
# first line it refuses (#415, #871).
PIPED_TABLE = (
    "# Repository config\n\n"
    "| Item | Value |\n|---|---|\n"
    "| Record language | English |\n"
    "| Broad gate | bin/test -q \\| tee out.txt |\n"
    "| Mode | shared |\n"
    "| Commit and pull request language | English |\n"
)

# #429: a fenced example above the live table. Two cases build on these
# bytes: the writer's drives the write over them, and the unclosed-fence case
# uses them as a canary, so a refusal wide enough to swallow a file whose
# fence IS closed turns it red.
FENCED_ABOVE = (
    "# Repository config\n\n"
    "An example of the format, copied out of `templates/setup/config.md`:\n\n"
    "```markdown\n"
    "| Item | Value |\n"
    "|---|---|\n"
    "| Mode | local |\n"
    "| Broad gate | EXAMPLE |\n"
    "```\n\n"
    "| Item | Value |\n"
    "|---|---|\n"
    "| Mode | shared |\n"
    "| Broad gate | bin/test -q |\n"
)

# The same shape with nothing parsed above the fence: the live table's only
# line will not parse, and before the fence rule the example below supplied
# the rows.
FENCED_BELOW_A_TABLE_THAT_NEVER_BEGAN = (
    "| Item | Value |\n"
    "|---|---|\n"
    "| Broad gate | bin/test -q | tee out.txt |\n"
    "```markdown\n"
    "| Mode | local |\n"
    "| Broad gate | EXAMPLE |\n"
    "```\n"
)

# A fenced line that will not parse, standing ABOVE the first live row; the
# walker refuses the live row below the fence and never quotes the fenced one
# (#871).
FENCED_REFUSAL = (
    "| Item | Value |\n"
    "|---|---|\n"
    "```markdown\n"
    "| Broad gate | bin/test -q | tee out.txt |\n"
    "```\n"
    "| Mode | shared |\n"
)

# The walker's sentence for a live row written under a comment that sits
# inside the table: GFM ends the table at the comment, so the row below it is
# not one of the table's rows (#871).
UNDER_THE_COMMENT = "ends above `| Mode | shared |`, a row the walk never reaches"


def crlf(text):
    return text.replace("\n", "\r\n")


def shape_text(name):
    """`tests/block_shapes.py`'s shape NAME as one text, each line ended."""
    from block_shapes import SHAPES

    return "\n".join(SHAPES[name]) + "\n"


def opt_in_shared(repo):
    return mark_root(repo / "seal")


def write_config(home, text):
    """TEXT written as `<home>/config.md`, HOME made where it is missing."""
    os.makedirs(str(home), exist_ok=True)
    with open(os.path.join(str(home), "config.md"), "w", encoding="utf-8") as f:
        f.write(text)


def write_unreadable(home, shape):
    """`<home>/config.md` in one of the two unreadable shapes that hold on
    macOS, Linux and Windows alike: a directory of that name, and bytes that
    do not decode as UTF-8. A permission bit is left out on purpose: Windows
    and a root user both read through it."""
    path = os.path.join(str(home), "config.md")
    if shape == "directory":
        os.mkdir(path)
    else:
        with open(path, "wb") as f:
            f.write(b"| Item | Value |\n|---|---|\n| Mode | \xff\xfe shared |\n")
    return path


def git(repo, *args, check=True):
    """git driven from Python in REPO, so no Bash line carries a commit
    (contract rule 8); the completed process."""
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=check,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )


def git_out(repo, *args):
    """`git`'s standard output in REPO, stripped."""
    return git(repo, *args).stdout.strip()


def commit_everything(repo, message):
    """Every change in REPO committed under MESSAGE; the new HEAD."""
    git_out(repo, "add", "-A")
    git_out(repo, "commit", "-qm", message)
    return git_out(repo, "rev-parse", "HEAD")


def commit_everything_as_e(repo, message):
    """`commit_everything`, by the author `e <e@example.com>`."""
    git_out(repo, "add", "-A")
    identity = ["-c", "user.email=e@example.com", "-c", "user.name=e"]
    git_out(repo, *identity, "commit", "-qm", message)
    return git_out(repo, "rev-parse", "HEAD")


def branch_of(repo):
    """The branch REPO's HEAD is on, or `HEAD` when it is detached."""
    return git(repo, "rev-parse", "--abbrev-ref", "HEAD", check=False).stdout.strip()


def git_dir(repo):
    """REPO's git directory, an absolute path."""
    return git(repo, "rev-parse", "--absolute-git-dir", check=False).stdout.strip()


def linked_worktree(repo, tmp_path):
    """A worktree of REPO at TMP_PATH/linked, on `feature/x`."""
    other = tmp_path / "linked"
    git(repo, "worktree", "add", "-q", str(other), "feature/x")
    assert os.path.isfile(other / ".git"), "a linked worktree carries a .git FILE"
    return other


def staged(repo):
    """The paths staged in REPO, one per line."""
    return git(repo, "diff", "--cached", "--name-only").stdout


def stage(repo, name, body="x\n"):
    (repo / name).write_text(body, encoding="utf-8")
    git(repo, "add", name)


def write(root, rel, text):
    """TEXT written at REL under ROOT, its directories made."""
    path = pathlib.Path(root) / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def opt_in(repo):
    """REPO opted in to the workflow, in shared mode."""
    mark_root(repo / "seal")


def staged_repo(path, declared=False, review="straight to the PR"):
    """An opted-in repository with one commit and a staged change.

    `declared` writes a routing declaration answering `review`, `straight to
    the PR` unless told otherwise."""
    path.mkdir(parents=True)
    run = lambda *a: subprocess.run(
        ["git", "-C", str(path), *a], check=True, capture_output=True
    )
    run("init", "-q")
    (path / "f").write_text("1\n", encoding="utf-8")
    run("add", "f")
    run("-c", "user.email=e@example.com", "-c", "user.name=e", "commit", "-qm", "b")
    (path / "f").write_text("2\n", encoding="utf-8")
    run("add", "f")
    mark_root(path / "seal")
    if declared:
        declare_routing(path, review=review)
    return path


def dirty(repo):
    """REPO with an uncommitted change to its tracked `f.txt`."""
    (repo / "f.txt").write_text("changed\n", encoding="utf-8")


def imported_roots(path):
    """The top-level names the module at PATH imports, `.` for a relative
    import."""
    with open(path, encoding="utf-8") as handle:
        tree = ast.parse(handle.read())
    roots = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            roots.add((node.module or "").split(".")[0] if not node.level else ".")
    return roots


def iso(minutes_ago):
    """The UTC time MINUTES_AGO, as a transcript writes it."""
    t = datetime.datetime.now(datetime.UTC) - datetime.timedelta(minutes=minutes_ago)
    return t.isoformat().replace("+00:00", "Z")


def q(text):
    """TEXT quoted for a shell."""
    return shlex.quote(str(text))


def sh(path):
    r"""`path` as one shell word.

    These commands are read the way the harness hands them over: a string
    that a POSIX shell is about to run, because the `Bash` matcher in
    `hooks/hooks.json` is the only PreToolUse entry that carries commit
    commands. Interpolating a native path raw made the test string mean
    something else on Windows -- the shell drops an unquoted backslash, so
    `git -C C:\Users\x` arrived at the gate as `C:UsersX` and the
    second target resolved under the first. Nothing about the gate was wrong
    there; the test was writing a command no shell would carry.
    """
    return shlex.quote(str(path))


def payload(cmd, repo, session="s1"):
    """The JSON a PreToolUse hook reads for a Bash command CMD typed in REPO
    by SESSION."""
    return {
        "tool_name": "Bash",
        "session_id": session,
        "tool_input": {"command": cmd},
        "cwd": str(repo),
    }


def reason_of(out):
    """The reason a hook's decision gives."""
    return json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]


def config_table(*rows):
    """A `seal/config.md` holding one row per `(item, value)` in ROWS."""
    return "# config\n\n| Item | Value |\n|---|---|\n" + "".join(
        f"| {item} | {value} |\n" for item, value in rows
    )


# A full commit id for a migration config's `Baseline commit` row.
BASELINE = "0123456789abcdef0123456789abcdef01234567"


def parity_file(sha):
    """`templates/setup/parity.md` with its `Baseline commit` placeholder
    replaced by SHA, or left standing where SHA is None."""
    text = pathlib.Path(ROOT, "templates", "setup", "parity.md").read_text(
        encoding="utf-8"
    )
    assert text.count("`<SHA>`") == 1
    return text if sha is None else text.replace("`<SHA>`", f"`{sha}`")


# --- the pact's world ---------------------------------------------------------
#
# `skills/verify/scripts/pact_check.py`'s cases in `tests/skills/test_pact_check.py`
# and the cases of `tests/hooks/test_config.py` that run it over a table the walker
# refuses share one world: the pact's repository, whose `seal/pact.md` carries
# one clause committed as v1 and then v2 on `main` and v3 on a side branch HEAD
# does not hold, and a signer beside it, which names the pact in its
# `seal/config.md`.


@functools.cache
def pact_check_modules():
    """`(pact_check, its evidence reader)`, loaded once, so the world's
    `check` and the cases that patch the module reach one module."""
    pc = load_module(
        os.path.join(ROOT, "skills", "verify", "scripts", "pact_check.py"),
        "pact_check_under_test",
    )
    return pc, pc.load(pc.CHECKER, "evidence_for_pact_tests")


PACT_URL = "git@example.com:org/orders-api.git"
SIGNER_URL = "https://example.com/org/orders-web"
MOBILE_URL = "https://example.com/org/orders-mobile"
CLAUSE_PATH = "## Order response shape / ### Fields"
PACT = "seal/pact.md"
SPEC = "seal/threads/1790000000-x/frame/design.md"
V1, V2, V3 = "id, total", "id, total, currency", "id, total, currency, tax"
# The pact a signer's `Pact` row names in the reader's cases, and what
# `hooks/lib/config.py#pact_declaration` answers for it.
URL = PACT_URL
ORDERS = [(URL, "example.com/org/orders-api")]
# The line of a frame `World.cite` writes its one anchor row on.
ANCHOR_LINE = 3


def pact(fields, signers=(SIGNER_URL,)):
    rows = "".join(f"| {s} |\n" for s in signers)
    return (
        "# Pact\n\n| Signer |\n|---|\n"
        + rows
        + f"\n## Order response shape\n\n### Fields\n\n{fields}\n\n## Errors\n\nx\n"
    )


def old_header(text):
    return text.replace("| Signer |\n|---|", "| Signatory |\n|---|", 1)


def clause(fields):
    pc, checker = pact_check_modules()
    digest, why = pc.clause_hash(checker, pact(fields), CLAUSE_PATH)
    assert why is None
    return digest


def signer_config(*rows):
    return "# config\n\n| Item | Value |\n|---|---|\n| Mode | shared |\n" + "".join(
        f"| {item} | {value} |\n" for item, value in rows
    )


def anchor_table(*rows):
    """A signer frame's anchor table, one `| Pact | Clause | Hash |` row per
    ROW, each a tuple of the three cells as written."""
    return "| Pact | Clause | Hash |\n|---|---|---|\n" + "".join(
        f"| {pact_cell} | {clause_cell} | {hash_cell} |\n"
        for pact_cell, clause_cell, hash_cell in rows
    )


def init(d, url):
    d.mkdir(parents=True)
    git_out(d, "init", "-q", "-b", "main")
    git_out(d, "remote", "add", "origin", url)


# The name `_template` commits by, as `tests/skills/test_pact_check.py` imports it.
commit = commit_everything_as_e


@pytest.fixture(scope="module")
def _template(tmp_path_factory):
    """The pact's repository and the signer as siblings under `work/`, and
    an empty HOME, built once for the module."""
    base = tmp_path_factory.mktemp("pact-world")
    (base / "home").mkdir()
    api = base / "work" / "orders-api"
    init(api, PACT_URL)
    write(api, PACT, pact(V1))
    mark_root(api / "seal")
    commit(api, "pact v1")
    write(api, PACT, pact(V2))
    commit(api, "pact v2")
    git(api, "switch", "-qc", "side")
    write(api, PACT, pact(V3))
    commit(api, "pact v3")
    git(api, "switch", "-q", "main")
    web = base / "work" / "orders-web"
    init(web, SIGNER_URL)
    write(web, "seal/config.md", signer_config(("Pact", PACT_URL)))
    mark_root(web / "seal")
    commit(web, "signer")
    return base


class World:
    """A copy of the module's world under one case's directory."""

    def __init__(self, template, tmp_path):
        self.tmp = tmp_path
        shutil.copytree(template, tmp_path / "w", symlinks=True)
        base = tmp_path / "w"
        self.home = base / "home"
        self.api = base / "work" / "orders-api"
        self.web = base / "work" / "orders-web"

    def cite(self, digest, clause_path=CLAUSE_PATH, where=SPEC):
        """Write the signer's frame at WHERE holding one anchor row, naming
        the pact by its URL, on line `ANCHOR_LINE`."""
        write(self.web, where, anchor_table((PACT_URL, clause_path, digest)))

    def run(self, root=None):
        """(exit, the printed lines run together) for `check` at ROOT, the
        pact's repository by default."""
        pc, _checker = pact_check_modules()
        out = io.StringIO()
        code = pc.check(str(root or self.api), out=out, home_dir=str(self.home))
        return code, " ".join(out.getvalue().split())

    def map(self, *rows):
        write(
            self.home,
            ".claude/agentic/pact-paths.md",
            "| Remote | Path |\n|---|---|\n"
            + "".join(f"| {r} | {p} |\n" for r, p in rows),
        )


@pytest.fixture
def world(_template, tmp_path):
    return World(_template, tmp_path)


def chain_check_run(chain, root, capsys, *extra):
    """CHAIN, the loaded chain check, run on ROOT against `main`; its exit
    code and what it printed."""
    code = chain.main(["--baseline", "main", "--root", str(root), *extra])
    return code, capsys.readouterr().out


def guard_decision(wg, monkeypatch, capsys, repo, command, sessions=([], [], True)):
    """WG, a loaded worktree guard, run on COMMAND in REPO with SESSIONS in
    its tree; its decision and reason, or `("silent", "")`."""
    monkeypatch.setattr(wg, "sessions_in_tree", lambda top, own="": sessions)
    monkeypatch.setattr(
        wg,
        "load_input",
        lambda: {
            "tool_name": "Bash",
            "session_id": "me",
            "tool_input": {"command": command},
            "cwd": str(repo),
        },
    )
    try:
        wg.main()
    except SystemExit:
        pass
    out = capsys.readouterr().out.strip()
    if not out:
        return "silent", ""
    d = json.loads(out)["hookSpecificOutput"]
    return d["permissionDecision"], d["permissionDecisionReason"]


@pytest.fixture
def projects(monkeypatch, tmp_path):
    """A projects root this case owns. Every loaded copy of the worktree
    guard imports the one `worktree_consent` by its plain name, so one patch
    reaches every copy."""
    root = tmp_path / "projects"
    root.mkdir()
    monkeypatch.setattr(sys.modules["worktree_consent"], "PROJECTS_ROOT", str(root))
    return root


# --- a routing declaration as text ----------------------------------------------


def two_axis_text(branch="feature/x"):
    """A declaration in the shape every one written before the third axis had."""
    return (
        "| Axis | Answer |\n|---|---|\n"
        "| Review | through the review chain |\n"
        "| Destination | open the pull request |\n"
        f"| Branch | {branch} |\n"
    )


def with_row(label, answer):
    """`two_axis_text()` with one more row in front of `Branch`."""
    return two_axis_text().replace("| Branch |", f"| {label} | {answer} |\n| Branch |")


# --- the worktree consent: its record, the routing press, the guard's rows ------

ACTIVE = [(111, "/tree", 1.0, 0.5, "VS Code")]
IDLE = [(222, "/tree", 400.0, 90.0, "Terminal")]


def common_dir(repo):
    """The clone's git directory — where the record lives.

    `--git-common-dir` rather than `--absolute-git-dir`: the record stands for
    "this session may split this clone into worktrees", and a linked worktree
    is the same clone. git answers relatively from a main worktree, so the
    join is not optional.
    """
    out = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "--git-common-dir"],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    ).stdout.strip()
    return pathlib.Path(os.path.normpath(os.path.join(str(repo), out)))


def consent_dir(repo):
    return common_dir(repo) / "agentic-worktree-consent"


def grant(repo, session="me"):
    """Write the record by hand — the reader's tests do not need the writer."""
    d = consent_dir(repo)
    d.mkdir(parents=True, exist_ok=True)
    (d / session).write_text("", encoding="utf-8")
    return d / session


ROUTING_QUESTION = "How should this work be routed?"
ROUTING_OPTIONS = ("automation (Recommended)", "per axis", "no work item")


def ask_entries(
    cwd,
    answer="automation (Recommended)",
    options=ROUTING_OPTIONS,
    multi=False,
    tool="AskUserQuestion",
    tool_id="toolu_01routing",
    result_id=None,
    question=ROUTING_QUESTION,
):
    """One question put and answered: the assistant's `tool_use`, then the
    `user` entry the harness writes with the structured `toolUseResult`."""
    asked = {
        "questions": [
            {
                "question": question,
                "header": "Routing",
                "multiSelect": multi,
                "options": [{"label": o, "description": "d"} for o in options],
            }
        ]
    }
    use = {
        "type": "assistant",
        "cwd": str(cwd),
        "message": {
            "role": "assistant",
            "content": [
                {"type": "tool_use", "id": tool_id, "name": tool, "input": asked}
            ],
        },
    }
    result = {
        "type": "user",
        "cwd": str(cwd),
        "isSidechain": False,
        "message": {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": result_id or tool_id,
                    "content": f'The user answered: "{question}"="{answer}".',
                }
            ],
        },
        "toolUseResult": {
            "questions": [dict(asked["questions"][0])],
            "answers": {question: answer},
        },
    }
    return [use, result]


def write_transcript(root, session, entries, slug="-Users-x-repo"):
    """`<root>/<slug>/<session>.jsonl`, one JSON object (or raw line) each."""
    d = pathlib.Path(root) / slug
    d.mkdir(parents=True, exist_ok=True)
    path = d / f"{session}.jsonl"
    with open(path, "w", encoding="utf-8") as f:
        for e in entries:
            f.write((e if isinstance(e, str) else json.dumps(e)) + "\n")
    return path


# The texts other test files compare the guard's deny with, for the
# tracked-changes row under the press (#894, work item 1791779434); the guard's
# own cases are `tests/hooks/test_worktree_guard.py`'s.
TOKEN = {
    "en": "[shared-tree-ok] carries the user's answer to switch in this shared tree",
    "ko": "[shared-tree-ok] 가 공용 트리에서 전환한다는 사용자의 답을 담고 있어",
}


# The press sentence, byte for byte the first frame's: #896 copies it.
PRESS = {
    "en": "This session's person pressed `automation` on the routing question, "
    "so this guard puts no question to them, and none is to be put to them in "
    "its place.",
    "ko": "이 세션의 사용자가 라우팅 질문에서 `automation` 을 눌렀습니다. 그래서 "
    "이 guard 는 사용자에게 아무것도 묻지 않으며, 다른 방법으로 대신 물어서도 "
    "안 됩니다.",
}


def dirty_deny(lang, lead):
    """W3: the deny's one text for `dirty(repo)`, issued from inside the tree.
    Every sentence is a fact the guard read or a fact about the guard; none
    says what git does for any switch form (the reframe after round 3)."""
    if lang == "en":
        return (
            f"{lead}, so no other row of this guard stops the switch, but 1 "
            "uncommitted tracked changes are present:\n"
            "     M  f.txt\n"
            "\n" + PRESS["en"] + "\n\n"
            "This row of the guard stops a branch switch while uncommitted "
            "tracked changes are present, and says nothing of a switch once "
            "none are.\n"
            "\n"
            "The ways on, none of which needs a person. Issue each command on "
            "its own: this guard reads the tree before a command runs, so `git "
            "stash && git switch <branch>` on one line meets this same refusal. "
            "`git commit` and `git stash` are on this guard's list of commands "
            "that leave the branch where it is, so each passes it when issued "
            "alone. Which of them fits this switch, and what to run after it, is "
            "yours to decide.\n"
            "\n"
            "Re-issuing this command unchanged meets this same refusal."
        )
    return (
        f"{lead} 이 guard 의 다른 규칙은 이 전환을 막지 않지만, 커밋되지 않은 "
        "추적 파일 변경이 1건 있습니다:\n"
        "     M  f.txt\n"
        "\n" + PRESS["ko"] + "\n\n"
        "이 guard 의 이 규칙은 커밋되지 않은 추적 파일 변경이 있는 동안 브랜치 "
        "전환을 막고, 변경이 없으면 전환에 대해 아무 말도 하지 않습니다.\n"
        "\n"
        "사람이 없어도 되는 길은 아래와 같습니다. 명령은 하나씩 따로 실행하세요. "
        "이 guard 는 명령이 실행되기 전에 트리를 읽으므로, `git stash && git "
        "switch <branch>` 처럼 한 줄에 쓰면 같은 거부를 받습니다. `git commit` 과 "
        "`git stash` 는 이 guard 가 브랜치를 그대로 두는 명령으로 꼽는 목록에 "
        "있어, 따로 실행하면 이 guard 를 통과합니다. 이 전환에 어느 쪽이 맞는지, "
        "그 뒤에 무엇을 실행할지는 직접 정하세요.\n"
        "\n"
        "이 명령을 그대로 다시 실행하면 같은 거부를 받습니다."
    )


# #689: the chains where the order of the walk's two threads decided the
# tree. The guard and the consent writer read through
# `hooks/lib/cmdline_base.py`, `86256492`'s reader frozen, so each judges the
# tree `86256492` judged, which is the dirty `w` bash runs the command in. `{missing}` is never created and
# `{other}` is a clean repository of its own.
BASE_TREE_CHAINS = {
    # Round 3 of #689's report: past `STATE_CAP` the walk collapses, and the
    # `cd {missing} ||` gives it a readable directory on the branch the `||`
    # skips, which led the base's thread.
    "the round-3 chain past the cap": "cd w; "
    + "2>/dev/null cd nosuch; " * 9
    + "cd {missing} || ",
    # PR #690's residuals. A `cd` landed past its redirection into a directory
    # that does not exist led, so the guard found no repository there and
    # fell back to the clean session tree.
    "a landing into a missing directory, then a semicolon": "cd w; "
    "2>/dev/null cd {missing}; ",
    "a glued landing into nothing, then one into a repository": "cd w; "
    "cd>/dev/null {missing} && 2>/dev/null cd {other}\n",
}


# #868 In 1: the two chains where the guard's `wheres[0]` and the writer's
# first resolved entry disagreed (`frame/design.md` In 1 of work item 1791384157).
# bash runs the `||` segment only where the `cd` failed, in the directory the
# shell was already in, and `;` runs its segment there when the `cd` fails, so
# the guard's answer is where bash creates in both.
PLACEMENT_CHAINS = {
    **BASE_TREE_CHAINS,
    "an unreadable segment, then a cd whose failure branch creates": (
        "eval x ; cd {other} || "
    ),
    "a cd into nothing, then a semicolon": "cd {missing} ; ",
}


def _a_dirty_w_under_a_clean_session(repo, tmp_path):
    session = tmp_path / "session"
    session.mkdir()
    subprocess.run(["git", "-C", str(session), "init", "-q"], check=True)
    shutil.copytree(repo, session / "w")
    (session / "w" / "f.txt").write_text("changed on purpose\n", encoding="utf-8")
    shutil.copytree(repo, session / "clean")
    other = tmp_path / "O"
    shutil.copytree(repo, other)
    return session, other


# --- a work item's closing records, as the stamp's queue gates read them -------
#
# `tests/hooks/test_sealer_stamp_queue.py` writes them.

STAMP_ITEM = "1799000000-an-item"


def guarantee_record(target, base, verdict, earlier=""):
    """A `guarantee.md` in `templates/records/sdd-guarantee.md`'s shape: its `Target
    SHA` row, with EARLIER after it, and one `Verdict:` line."""
    return (
        "# an item — guarantee\n\n| Field | Value |\n|---|---|\n"
        f"| Target SHA | {target} against {base}{earlier} |\n"
        f"| Broad gate | {target} against {base} |\n\nVerdict: {verdict}\n"
    )


def routing_record(branch="feat/x"):
    """A `routing.md` in `templates/records/sdd-routing.md`'s shape, naming BRANCH in
    its `Branch` row, or with no `Branch` row where BRANCH is None."""
    rows = (
        "| Axis | Answer |\n|---|---|\n"
        "| Review | through the review chain |\n"
        "| Destination | open the pull request |\n"
    )
    return rows + (f"| Branch | {branch} |\n" if branch else "")


def queued_values(repo):
    """Every values file under REPO's `.git/agentic-stamp`, drawn or not."""
    found = []
    for directory, _dirs, names in os.walk(repo / ".git" / "agentic-stamp"):
        found += [os.path.join(directory, n) for n in names if n.endswith(".json")]
    return sorted(found)


# --- the opt-in's two places, the old name and the throwaway marker -------------


def home(repo):
    mark_root(repo / "seal")


def legacy(repo):
    (repo / ".specseal").mkdir(exist_ok=True)
    (repo / ".specseal" / "map.md").write_text("# map\n", encoding="utf-8")


def scratch(repo):
    (repo / ".git" / "agentic-scratch").write_text("", encoding="utf-8")


# --- the implementer family's declaration and calls -----------------------------

ITEM = "1788137177-a-work-item"


def run_dispatch(group, payload, hooks=HOOKS):
    r = subprocess.run(
        [sys.executable, os.path.join(hooks, "dispatch.py"), group],
        input=json.dumps(payload),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
    )
    return r.stdout


def declare(repo, implementation="crafter", item=ITEM, planning=None):
    """A declaration for this repo's branch; a `None` answer omits its row."""
    d = mark_root(repo / "seal") / "threads" / item
    d.mkdir(parents=True, exist_ok=True)
    third = f"| Implementation | {implementation} |\n" if implementation else ""
    fourth = f"| Planning | {planning} |\n" if planning else ""
    (d / "routing.md").write_text(
        f"# {item} -- routing\n\n"
        "| Axis | Answer |\n|---|---|\n"
        "| Review | through the review chain |\n"
        "| Destination | open the pull request |\n"
        f"{fourth}"
        f"{third}"
        f"| Branch | {branch_of(repo)} |\n",
        encoding="utf-8",
    )
    return d


def declare_crafter(repo, home, item=ITEM):
    """A declaration under `home` whose third axis says `crafter`."""
    d = mark_root(home) / "threads" / item
    d.mkdir(parents=True, exist_ok=True)
    (d / "routing.md").write_text(
        f"# {item} -- routing\n\n"
        "| Axis | Answer |\n|---|---|\n"
        "| Review | through the review chain |\n"
        "| Destination | open the pull request |\n"
        "| Implementation | crafter |\n"
        f"| Branch | {branch_of(repo)} |\n",
        encoding="utf-8",
    )
    return d


def spawn(repo, agent="agentic:crafter", session="s1", **extra):
    return {
        "tool_name": "Agent",
        "session_id": session,
        "tool_input": {"subagent_type": agent, "prompt": "build it", **extra},
        "cwd": str(repo),
    }


def bash(repo, cmd="git commit -m x", session="s1"):
    return {
        "tool_name": "Bash",
        "session_id": session,
        "tool_input": {"command": cmd},
        "cwd": str(repo),
    }


# --- a console the gates cannot encode to --------------------------------------

# Korean, which cp949 encodes and ASCII does not; it is in the payload on
# purpose, because the payload carries the user's own command text, which is
# where the non-ASCII in production actually is.
KOREAN = "한글"

# Consoles that cannot carry what the gates say. `ascii` is the sharpest and is
# not hypothetical: it is what a bare `LC_ALL=C` gives a POSIX runner.
HOSTILE = ["cp949", "ascii", "latin-1"]


_CONSOLE_REPO_TEMPLATE = None


def _console_repo_template():
    """A repo with one committed file, built once per process -- `opted_in_repo`
    is called once per case of the hostile-console cases, always onto this
    shape."""
    global _CONSOLE_REPO_TEMPLATE
    if _CONSOLE_REPO_TEMPLATE is None:
        d = pathlib.Path(tempfile.mkdtemp(prefix="agentic-console-repo-template-"))
        d = d / "repo"
        d.mkdir(parents=True)
        git = lambda *a: subprocess.run(
            ["git", "-C", str(d), *a], check=True, capture_output=True
        )
        git("init", "-q")
        git("config", "user.email", "t@t.example")
        git("config", "user.name", "t")
        (d / "f.txt").write_text("one\n", encoding="utf-8")
        git("add", "-A")
        git("commit", "-qm", "base")
        atexit.register(shutil.rmtree, d, True)
        _CONSOLE_REPO_TEMPLATE = d
    return _CONSOLE_REPO_TEMPLATE


def opted_in_repo(where):
    """A repository the commit gate fires in, at a path holding non-ASCII."""
    shutil.copytree(_console_repo_template(), where)
    mark_root(where / "seal")
    return where


@pytest.fixture
def korean_repo(tmp_path):
    return opted_in_repo(tmp_path / KOREAN / "repo")


# A spec's `## Rule changes` and the history `settle` reads, shared by
# `tests/skills/test_rule_changes.py`, `tests/skills/test_settle.py` and the cases the two
# old settle files keep.


def spec(changes):
    """A spec whose `## Rule changes` section holds CHANGES, with a section
    on either side so the reader has to find where it ends."""
    return (
        "# a work item\n\n## Scope\n\nIn.\n\n## Rule changes\n\n"
        f"{changes}\n\n## Open questions\n\nNone.\n"
    )


def line_of(text, needle):
    return text.split("\n").index(needle) + 1


DOC = """\
# A policy

## S

Before. old sentence. After.

### S child

Child text.

## T

x.

T's text.

## U

Last.
"""


def op(kind, section=None, old=None, new=None, file="docs/a.md"):
    lines = [f"- {kind}", f"  file: {file}"]
    for name, value in (("section", section), ("from", old), ("to", new)):
        if value is not None:
            lines.append(f"  {name}: {value}")
    return "\n".join(lines)


@pytest.fixture
def tree(tmp_path):
    """Four work items: three released, one that arrives after the commit.

    `delta` is this branch's own unreleased work.
    """
    repo = tmp_path / "repo"
    (repo / "docs").mkdir(parents=True)
    (repo / "docs" / "one-root.md").write_text("# a policy\n\nA rule.\n", "utf-8")
    mark_root(repo / "seal")
    for name in ("1700000001-alpha", "1700000002-beta", "1700000003-gamma"):
        item = repo / "seal" / "threads" / name
        (item / "frame").mkdir(parents=True)
        (item / "frame" / "design.md").write_text(
            f"# {name}\n\nWhat it decided.\n", "utf-8"
        )
    git(repo, "init", "-q")
    git(repo, "config", "user.email", "x@example.com")
    git(repo, "config", "user.name", "x")
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "released")
    later = repo / "seal" / "threads" / "1700000004-delta"
    (later / "frame").mkdir(parents=True)
    (later / "frame" / "design.md").write_text(
        "# delta\n\nIn flight.\n", encoding="utf-8"
    )
    return repo
