"""`lib/gitcmd.py`: the one place a script starts git or `gh`, and the argv
of every git command, read the same under any person's or repository's git
configuration.

One parameter per key of `gitcmd.KEYS`. Each builds a repository in which
that key, set otherwise than git's default, changes what one command
prints, and names what the command prints under git's default. The scripts'
own readers start git through `git`, which builds the argv with `argv`, and
the proofer reads that in the diff (`docs/running/what-a-script-gates.md`
*Which gate a script holds*); the cases here hold each key once, over the
helper. `FLAGGED` does the same for `gitcmd.FLAGS`: one parameter for each
subcommand and each setting that takes a submodule's path out of what it
prints (#1640).

`Test_git`, `Test_gh` and `Test_is_ancestor` hold the runner (#1573): a
command that did not start or did not finish within `TIMEOUT` raises
`Unrun`, a non-zero exit is the caller's to read unless it passes
`check=True`, and `Test_Failed` holds what an uncaught one does to a
process. `Test_http_answer` holds the reader of what `gh api -i` printed,
the HTTP status the release scripts decide on. `Test_older` holds the read
of git's version against `OLDEST` (#1642).
"""

import os
import subprocess
import sys

import pytest
from conftest import census_case, gh_answers, git, load_lib_module, write

TARGET = "lib/gitcmd.py"

gitcmd = load_lib_module("gitcmd.py", "gitcmd_for_its_own_file")
# `git_path` and `under_root` came here from `unverified_check.py` (#1482),
# and their cases with them.


def new_repo(tmp_path):
    """An empty repository under TMP_PATH with an identity of its own."""
    repo = tmp_path / "repo"
    subprocess.run(["git", "init", "-q", str(repo)], check=True, capture_output=True)
    git(repo, "config", "user.email", "x@example.com")
    git(repo, "config", "user.name", "x")
    return repo


def commit(repo, message, *flags):
    git(repo, "add", "-A")
    git(repo, "commit", "-q", *flags, "-m", message)
    return git(repo, "rev-parse", "HEAD").stdout.strip()


def signed(repo, tmp_path):
    """A commit signed with an ssh key made here, by the `ssh-keygen` the
    repository's own config names, so a person's `gpg.ssh.program` does not
    reach it. Skipped where no key can be made or no commit signed: without
    `ssh-keygen`, or under a git older than 2.34, which signs with gpg only."""
    key = tmp_path / "signing"
    try:
        made = subprocess.run(
            ["ssh-keygen", "-q", "-t", "ed25519", "-N", "", "-f", str(key)],
            capture_output=True,
            encoding="utf-8",
        )
    except FileNotFoundError:
        pytest.skip("ssh-keygen is not installed, so no commit can be signed")
    if made.returncode != 0:
        pytest.skip(f"ssh-keygen made no key: {made.stderr.strip()}")
    git(repo, "config", "gpg.format", "ssh")
    git(repo, "config", "gpg.ssh.program", "ssh-keygen")
    git(repo, "config", "user.signingkey", str(key))
    write(repo, "a.txt", "a\n")
    git(repo, "add", "-A")
    signing = subprocess.run(
        ["git", "-C", str(repo), "commit", "-q", "-S", "-m", "signed"],
        capture_output=True,
        encoding="utf-8",
    )
    if signing.returncode != 0:
        pytest.skip(f"git could not sign a commit: {signing.stderr.strip()}")
    sha = git(repo, "rev-parse", "HEAD").stdout.strip()
    return ["log", "--format=%H"], f"{sha}\n"


def rooted(repo, tmp_path):
    """One commit, the root, which adds `a.txt`."""
    write(repo, "a.txt", "a\n")
    sha = commit(repo, "root")
    return ["log", "--name-only", "--format=%H"], f"{sha}\n\na.txt\n"


def renamed(repo, tmp_path):
    """`new.txt`, renamed from `old.txt` with its text unchanged."""
    write(repo, "old.txt", "one\ntwo\nthree\n")
    commit(repo, "add old")
    git(repo, "mv", "old.txt", "new.txt")
    commit(repo, "rename")
    return ["log", "--format=%s", "--", "new.txt"], "rename\n"


def accented(repo, tmp_path):
    """A commit whose subject holds a letter outside ASCII."""
    write(repo, "a.txt", "a\n")
    commit(repo, "é (#4)")
    return ["log", "-1", "--format=%s"], "é (#4)\n"


def untracked(repo, tmp_path):
    """`u.txt`, beside a commit and never added."""
    write(repo, "a.txt", "a\n")
    commit(repo, "a")
    write(repo, "u.txt", "u\n")
    return ["status", "--porcelain", "--", "u.txt"], "?? u.txt\n"


# (key, a value a person sets, the repository it changes a reading in).
CASES = [
    pytest.param("log.showSignature", "true", signed, id="log.showSignature"),
    pytest.param("log.showRoot", "false", rooted, id="log.showRoot"),
    pytest.param("log.follow", "true", renamed, id="log.follow"),
    pytest.param(
        "i18n.logOutputEncoding", "iso-8859-1", accented, id="i18n.logOutputEncoding"
    ),
    pytest.param(
        "status.showUntrackedFiles", "no", untracked, id="status.showUntrackedFiles"
    ),
]


def printed(command):
    """What COMMAND writes to its standard output, as bytes."""
    return subprocess.run(command, check=True, capture_output=True).stdout


# A submodule's entry in `.gitmodules`, and the line that ignores it.
GITMODULES = '[submodule "sub"]\n\tpath = sub\n\turl = ./sub\n'
IGNORED = "\tignore = all\n"


def submoduled(tmp_path, setting):
    """A repository whose last commit moves the commit `sub`, a submodule,
    points to, and whose checkout of `sub` stands at a commit the index
    does not hold; SETTING tells git to ignore the submodule by
    `diff.ignoreSubmodules=all` in the repository's configuration
    (`configuration`), by `ignore = all` in its `.gitmodules` entry
    (`.gitmodules`), or not at all (None). The repository and its last
    commit.

    Each pointer is written into the index by `update-index`, since `add`
    and `commit` read an ignored submodule as no change on some gits, and
    each commit writes the index as it stands, with no `add` before it."""
    repo = new_repo(tmp_path)
    if setting == "configuration":
        git(repo, "config", "diff.ignoreSubmodules", "all")
    entry = GITMODULES + (IGNORED if setting == ".gitmodules" else "")
    write(repo, ".gitmodules", entry)
    commit(repo, "a submodule's entry")
    sub = repo / "sub"
    sub.mkdir()
    git(sub, "init", "-q")
    git(sub, "-c", "user.name=x", "-c", "user.email=x@example.com", "commit",
        "-q", "--allow-empty", "-m", "the checkout")  # fmt: skip
    for pointer in ("1" * 40, "2" * 40):
        git(repo, "update-index", "--add", "--cacheinfo", f"160000,{pointer},sub")
        git(repo, "commit", "-q", "--allow-empty", "-m", f"sub at {pointer[0]}")
    return repo, git(repo, "rev-parse", "HEAD").stdout.strip()


def submodule_read(subcommand, head):
    """`(command, printed)`: the read of SUBCOMMAND that names `sub` in a
    repository `submoduled` built, with HEAD its last commit, and what git
    prints for it where nothing ignores the submodule."""
    return {
        "diff": (["diff", "--name-only", "HEAD~1", "HEAD"], "sub\n"),
        "diff-tree": (
            ["diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"],
            "sub\n",
        ),
        "log": (["log", "-1", "--name-only", "--format=%H"], f"{head}\n\nsub\n"),
        "status": (["status", "--porcelain"], " M sub\n"),
    }[subcommand]


# (subcommand, the setting that takes `sub` out of what it prints). The
# configuration key leaves `diff-tree` as it is, so it has no parameter
# there (design G3).
FLAGGED = [
    pytest.param("diff", "configuration", id="diff-configuration"),
    pytest.param("diff", ".gitmodules", id="diff-gitmodules"),
    pytest.param("diff-tree", ".gitmodules", id="diff-tree-gitmodules"),
    pytest.param("log", "configuration", id="log-configuration"),
    pytest.param("log", ".gitmodules", id="log-gitmodules"),
    pytest.param("status", "configuration", id="status-configuration"),
    pytest.param("status", ".gitmodules", id="status-gitmodules"),
]


class Test_argv:
    @pytest.mark.parametrize("key, value, build", CASES)
    def test_accepts_what_git_prints_under_its_own_defaults(
        self, tmp_path, key, value, build
    ):
        """Each key is held at git's own default, so where nobody sets it the
        command reads as it would without the helper."""
        repo = new_repo(tmp_path)
        command, expected = build(repo, tmp_path)
        assert printed(gitcmd.argv("-C", str(repo), *command)) == expected.encode()

    @pytest.mark.parametrize("where", ["GIT_CONFIG_COUNT", "the repository"])
    @pytest.mark.parametrize("key, value, build", CASES)
    def test_refuses_a_value_a_person_or_a_repository_sets(
        self, tmp_path, monkeypatch, key, value, build, where
    ):
        """#1283. A key set in the environment, as a person's own config
        reaches git, or in the repository's own `.git/config`, changes what
        the bare command prints, and not what `argv`'s prints: `-c`
        outranks both. Each parameter was seen red with its key's `-c`
        taken out of `argv`."""
        repo = new_repo(tmp_path)
        command, expected = build(repo, tmp_path)
        if where == "GIT_CONFIG_COUNT":
            monkeypatch.setenv("GIT_CONFIG_COUNT", "1")
            monkeypatch.setenv("GIT_CONFIG_KEY_0", key)
            monkeypatch.setenv("GIT_CONFIG_VALUE_0", value)
        else:
            git(repo, "config", key, value)
        bare = printed(["git", "-C", str(repo), *command])
        assert bare != expected.encode(), f"{key}={value} changed nothing: {bare!r}"
        assert printed(gitcmd.argv("-C", str(repo), *command)) == expected.encode()

    @pytest.mark.parametrize("subcommand", sorted({c.values[0] for c in FLAGGED}))
    def test_accepts_a_submodule_named_as_git_names_it_under_its_own_defaults(
        self, tmp_path, subcommand
    ):
        """#1640, design S2. Where nothing ignores the submodule, the
        command `argv` builds prints what the bare command prints."""
        repo, head = submoduled(tmp_path, None)
        command, expected = submodule_read(subcommand, head)
        assert printed(["git", "-C", str(repo), *command]) == expected.encode()
        assert printed(gitcmd.argv("-C", str(repo), *command)) == expected.encode()

    @pytest.mark.parametrize("subcommand, setting", FLAGGED)
    def test_refuses_a_submodule_left_out_by_a_setting_no_key_reaches(
        self, tmp_path, subcommand, setting
    ):
        """#1640, design S1. `diff.ignoreSubmodules` and a `.gitmodules`
        entry's `ignore` take the submodule's path out of what the bare
        command prints, and not out of what `argv`'s prints: `FLAGS` puts
        `--ignore-submodules=none` after the subcommand. Each parameter was
        seen red with its subcommand's entry taken out of `FLAGS`."""
        repo, head = submoduled(tmp_path, setting)
        command, expected = submodule_read(subcommand, head)
        bare = printed(["git", "-C", str(repo), *command])
        assert bare != expected.encode(), f"{setting} changed nothing: {bare!r}"
        assert printed(gitcmd.argv("-C", str(repo), *command)) == expected.encode()

    def test_accepts_the_flags_after_the_subcommand_past_the_options_before_it(
        self,
    ):
        """#1640. The subcommand is the first argument that opens with no
        `-`, after `-C` and `-c` with their values and any other option
        before it, as `settle.py#git_run` passes `--literal-pathspecs`; a
        subcommand `FLAGS` does not hold gets nothing."""
        held = gitcmd.argv()[1:]
        none = "--ignore-submodules=none"
        assert gitcmd.argv("-C", "/r", "--literal-pathspecs", "log", "-z") == [
            "git", *held, "-C", "/r", "--literal-pathspecs", "log", none, "-z",
        ]  # fmt: skip
        assert gitcmd.argv("-c", "a.b=c", "-C", "/r", "status") == [
            "git", *held, "-c", "a.b=c", "-C", "/r", "status", none,
        ]  # fmt: skip
        assert gitcmd.argv("-C", "/r", "cat-file", "--batch") == [
            "git", *held, "-C", "/r", "cat-file", "--batch",
        ]  # fmt: skip


class Test_module:
    def test_every_key_has_a_case(self):
        """A key added to `KEYS` gets a parameter here, which shows the
        reading it changes."""
        assert [key for key, _ in gitcmd.KEYS] == [c.values[0] for c in CASES]

    def test_every_flag_has_a_case(self):
        """#1640, design S3. A subcommand added to `FLAGS` gets a parameter
        of `FLAGGED`, which shows the reading its flag changes."""
        assert sorted(gitcmd.FLAGS) == sorted({c.values[0] for c in FLAGGED})


class Test_git_path:
    def test_accepts_a_windows_path_as_git_spells_it(self, monkeypatch):
        r"""git answers and accepts `/` on every platform; `os.sep` is
        monkeypatched because `git_path` reads it at call time, so the
        Windows branch runs on every leg."""
        monkeypatch.setattr(os, "sep", "\\")
        assert gitcmd.git_path("specs\\1780000000-work\\gaps.md") == (
            "specs/1780000000-work/gaps.md"
        )
        assert gitcmd.git_path("specs/1780000000-work/gaps.md") == (
            "specs/1780000000-work/gaps.md"
        )

    def test_refuses_to_rewrite_a_backslash_in_a_posix_name(self, monkeypatch):
        monkeypatch.setattr(os, "sep", "/")
        assert gitcmd.git_path("specs/odd\\name.md") == "specs/odd\\name.md"


class Test_under_root:
    def test_accepts_a_slash_joined_path_as_the_disk_spells_it(self):
        assert gitcmd.under_root("r", "specs/a/gaps.md") == os.path.join(
            "r", "specs", "a", "gaps.md"
        )

    def test_refuses_to_read_the_path_as_one_name(self):
        assert gitcmd.under_root("r", "a/b") != os.path.join("r", "a" + chr(0) + "b")


class Test_inside:
    """`inside` came here from `agentic.py`, `settle.py` and `broad_gate.py`
    (#1575), each of which answered it by `commonpath`."""

    def test_accepts_the_top_itself_and_a_path_under_it(self, tmp_path, monkeypatch):
        """A relative path is read from the directory this runs in, as
        `agentic.py`'s `display` hands one over."""
        top = tmp_path / "repo"
        top.mkdir()
        assert gitcmd.inside(str(top), str(top))
        assert gitcmd.inside(os.path.join(str(top), "a", "b.md"), str(top))
        monkeypatch.chdir(top)
        assert gitcmd.inside(os.path.join("a", "b.md"), str(top))

    def test_refuses_a_sibling_sharing_its_prefix_a_parent_and_two_drives(
        self, tmp_path, monkeypatch
    ):
        """`/repo-2/x` begins with `/repo` and is not under it, which a
        `startswith` would miss. `commonpath` raises for paths on two drives,
        which only a Windows run meets, so the raise stands in for it."""
        top = str(tmp_path / "repo")
        assert not gitcmd.inside(str(tmp_path / "repo-2" / "x"), top)
        assert not gitcmd.inside(str(tmp_path), top)

        def two_drives(paths):
            raise ValueError("Paths don't have the same drive")

        monkeypatch.setattr(gitcmd.os.path, "commonpath", two_drives)
        assert not gitcmd.inside(top, top)


def starts(monkeypatch, outcome):
    """`subprocess.run` replaced by one that records each call's argv and
    keywords and answers OUTCOME: an exception raised, or a (code, stdout,
    stderr) triple. Returns the calls."""
    calls = []

    def run(command, **kwargs):
        calls.append((list(command), kwargs))
        if isinstance(outcome, BaseException):
            raise outcome
        return subprocess.CompletedProcess(command, *outcome)

    monkeypatch.setattr(gitcmd.subprocess, "run", run)
    return calls


def no_program_on_path(monkeypatch, tmp_path):
    """PATH set to one empty directory, so neither git nor `gh` is found."""
    empty = tmp_path / "empty-path"
    empty.mkdir()
    monkeypatch.setenv("PATH", str(empty))


class Test_git:
    def test_accepts_the_argv_argv_builds_and_returns_the_process(
        self, tmp_path, monkeypatch
    ):
        """The command started is `argv("-C", root, *args)`, under
        `TIMEOUT`, in text mode as UTF-8 with undecodable bytes replaced,
        and with `given` on stdin; the `CompletedProcess` is returned as
        it is."""
        calls = starts(monkeypatch, (0, "out\n", ""))
        done = gitcmd.git("/r", "cat-file", "--batch", given="HEAD\n")
        assert done.stdout == "out\n"
        [(command, kwargs)] = calls
        assert command == gitcmd.argv("-C", "/r", "cat-file", "--batch")
        assert kwargs["timeout"] == gitcmd.TIMEOUT
        assert kwargs["input"] == "HEAD\n"
        assert (kwargs["encoding"], kwargs["errors"]) == ("utf-8", "replace")
        assert kwargs["env"] is None

    def test_accepts_bytes_and_an_environment_added_to_this_one(
        self, tmp_path, monkeypatch
    ):
        """`binary=True` returns bytes, and `env` reaches git, both read
        from a real repository; `env` is added to the environment the
        process inherits rather than replacing it."""
        repo = new_repo(tmp_path)
        write(repo, "a.txt", "a\n")
        sha = commit(repo, "a")
        done = gitcmd.git(str(repo), "log", "-1", "--format=%H", binary=True)
        assert done.stdout == f"{sha}\n".encode()
        held = {
            "GIT_CONFIG_COUNT": "1",
            "GIT_CONFIG_KEY_0": "agentic.probe",
            "GIT_CONFIG_VALUE_0": "seen",
        }
        done = gitcmd.git(str(repo), "config", "--get", "agentic.probe", env=held)
        assert done.stdout == "seen\n"
        monkeypatch.setenv("AGENTIC_INHERITED", "kept")
        calls = starts(monkeypatch, (0, b"", b""))
        gitcmd.git(str(repo), "status", binary=True, env={"A": "1"})
        [(_, kwargs)] = calls
        assert kwargs["env"]["A"] == "1"
        assert kwargs["env"]["AGENTIC_INHERITED"] == "kept"
        assert (kwargs["encoding"], kwargs["errors"]) == (None, None)

    def test_accepts_a_non_zero_exit_as_the_callers_to_read(self, tmp_path):
        """For `merge-base --is-ancestor`, `diff --quiet`, `config --get`
        and `rev-parse --verify --quiet`, exit 1 is an answer, so without
        `check` the exit code is returned and nothing is raised."""
        repo = new_repo(tmp_path)
        done = gitcmd.git(str(repo), "config", "--get", "agentic.absent")
        assert done.returncode == 1
        assert done.stdout == ""

    def test_refuses_a_command_past_the_bound_as_no_answer(self, monkeypatch):
        """A command that did not finish within `TIMEOUT` raises `Unrun`,
        whose line names the program, the arguments the caller passed and
        the bound, and none of `argv`'s `-c` pairs or the `-C <root>`."""
        starts(monkeypatch, subprocess.TimeoutExpired(["git"], gitcmd.TIMEOUT))
        with pytest.raises(gitcmd.Unrun) as raised:
            gitcmd.git("/r", "rm", "-r", "--cached", ":/agentory")
        assert raised.value.command == ["git", "rm", "-r", "--cached", ":/agentory"]
        assert str(raised.value) == (
            f"`git rm -r --cached :/agentory` did not finish within "
            f"{gitcmd.TIMEOUT} seconds"
        )
        assert raised.value.code == str(raised.value)

    def test_refuses_a_git_that_is_not_on_path_as_no_answer(
        self, tmp_path, monkeypatch
    ):
        """A program that cannot be found raises `Unrun` naming it, and
        never the `FileNotFoundError` the process call raised."""
        no_program_on_path(monkeypatch, tmp_path)
        with pytest.raises(gitcmd.Unrun) as raised:
            gitcmd.git(str(tmp_path), "status")
        assert str(raised.value) == (
            "`git status` could not be run: `git` is not on PATH"
        )

    def test_refuses_a_command_that_could_not_start_as_no_answer(self, monkeypatch):
        """Any other error of the start raises `Unrun` with the error's
        text."""
        starts(monkeypatch, PermissionError(13, "Permission denied"))
        with pytest.raises(gitcmd.Unrun) as raised:
            gitcmd.git("/r", "status")
        assert str(raised.value) == (
            "`git status` could not be run: [Errno 13] Permission denied"
        )

    def test_refuses_a_non_zero_exit_where_the_caller_checks(self, tmp_path):
        """`check=True` turns a non-zero exit into `Exited`, which carries
        the code and stderr, and whose line holds the code and git's first
        line on stderr."""
        repo = new_repo(tmp_path)
        with pytest.raises(gitcmd.Exited) as raised:
            gitcmd.git(str(repo), "rev-parse", "--verify", "nowhere", check=True)
        assert raised.value.returncode == 128
        first = raised.value.stderr.strip().splitlines()[0]
        assert first.startswith("fatal: "), raised.value.stderr
        assert str(raised.value) == (
            f"`git rev-parse --verify nowhere` exited 128: {first}"
        )


class Test_one_run:
    """The accepting cases ask inside a run, the refusing ones outside one
    or of a command that gave no answer."""

    def test_accepts_one_process_for_a_command_asked_again_in_a_run(self, monkeypatch):
        """#1603, design S2. Inside a run, a command asked again with the
        same root, arguments, input, mode and environment starts no
        process and returns the first answer; a change to any of them is
        another command. A run entered inside it joins it, so its answers
        stand after the inner one ends."""
        calls = starts(monkeypatch, (0, "out\n", ""))
        with gitcmd.one_run():
            first = gitcmd.git("/r", "status")
            with gitcmd.one_run():
                assert gitcmd.git("/r", "status") is first
            assert gitcmd.git("/r", "status") is first
            gitcmd.git("/s", "status")
            gitcmd.git("/r", "status", "-z")
            gitcmd.git("/r", "status", given="x")
            gitcmd.git("/r", "status", binary=True)
            gitcmd.git("/r", "status", env={"A": "1"})
            gitcmd.git("/r", "status", env={"A": "1"})
        assert len(calls) == 6, calls

    def test_accepts_a_new_answer_in_a_run_entered_after_one_ended(self, tmp_path):
        """#1603, design S2. The answers die with their run, by return or
        by exception, so a run entered after a commit reads the commit."""
        repo = new_repo(tmp_path)
        write(repo, "a.txt", "a\n")
        first = commit(repo, "a")
        with gitcmd.one_run():
            assert gitcmd.git(str(repo), "rev-parse", "HEAD").stdout == f"{first}\n"
        write(repo, "a.txt", "b\n")
        second = commit(repo, "b")
        with pytest.raises(KeyError), gitcmd.one_run():
            assert gitcmd.git(str(repo), "rev-parse", "HEAD").stdout == f"{second}\n"
            raise KeyError("the run ends by an exception")
        write(repo, "a.txt", "c\n")
        third = commit(repo, "c")
        with gitcmd.one_run():
            assert gitcmd.git(str(repo), "rev-parse", "HEAD").stdout == f"{third}\n"

    def test_refuses_to_answer_again_outside_a_run(self, monkeypatch):
        """#1603, design S3. Outside a run, each ask starts its command."""
        calls = starts(monkeypatch, (0, "out\n", ""))
        gitcmd.git("/r", "status")
        gitcmd.git("/r", "status")
        assert len(calls) == 2, calls

    def test_refuses_to_keep_a_command_that_gave_no_answer(self, monkeypatch):
        """#1603, design S4. Inside a run, a command that did not finish
        raises `Unrun` on each ask and is started again, and a non-zero
        exit is read against `check` on each ask, so an ask with `check`
        after one without it raises `Exited`."""
        calls = starts(monkeypatch, subprocess.TimeoutExpired(["git"], gitcmd.TIMEOUT))
        with gitcmd.one_run():
            for _ in range(2):
                with pytest.raises(gitcmd.Unrun):
                    gitcmd.git("/r", "status")
        assert len(calls) == 2, calls
        calls = starts(monkeypatch, (1, "", "fatal: no\n"))
        with gitcmd.one_run():
            assert gitcmd.git("/r", "status").returncode == 1
            for _ in range(2):
                with pytest.raises(gitcmd.Exited) as raised:
                    gitcmd.git("/r", "status", check=True)
                assert str(raised.value) == "`git status` exited 1: fatal: no"
        assert len(calls) == 1, calls


class Test_gh:
    def test_accepts_the_gh_on_path_in_the_directory_named(self, tmp_path, monkeypatch):
        """The `gh` `shutil.which` finds is started in `root`, and what it
        printed is returned; the suite's stub answers this one question."""
        monkeypatch.setenv("PATH", gh_answers(dict(os.environ), "ready")["PATH"])
        done = gitcmd.gh("pr", "view", "--json", "isDraft", root=str(tmp_path))
        assert (done.returncode, done.stdout) == (0, '{"isDraft":false}\n')
        calls = starts(monkeypatch, (0, "", ""))
        gitcmd.gh("pr", "view", root=str(tmp_path))
        [(command, kwargs)] = calls
        assert command[1:] == ["pr", "view"]
        assert os.path.normcase(os.path.basename(command[0])).startswith("gh")
        assert kwargs["cwd"] == str(tmp_path)
        assert kwargs["timeout"] == gitcmd.TIMEOUT
        assert (kwargs["encoding"], kwargs["errors"]) == ("utf-8", "replace")

    def test_refuses_a_gh_that_is_not_on_path_as_no_answer(self, tmp_path, monkeypatch):
        no_program_on_path(monkeypatch, tmp_path)
        with pytest.raises(gitcmd.Unrun) as raised:
            gitcmd.gh("pr", "view")
        assert raised.value.command == ["gh", "pr", "view"]
        assert str(raised.value) == (
            "`gh pr view` could not be run: `gh` is not on PATH"
        )

    def test_refuses_a_command_past_the_bound_as_no_answer(self, monkeypatch):
        starts(monkeypatch, subprocess.TimeoutExpired(["gh"], gitcmd.TIMEOUT))
        with pytest.raises(gitcmd.Unrun) as raised:
            gitcmd.gh("api", "repos/x/y")
        assert str(raised.value) == (
            f"`gh api repos/x/y` did not finish within {gitcmd.TIMEOUT} seconds"
        )

    def test_refuses_a_non_zero_exit_where_the_caller_checks(self, monkeypatch):
        """Without `check` the exit is returned; with it, `Exited` names the
        code and the first line `gh` said."""
        monkeypatch.setenv("PATH", gh_answers(dict(os.environ), "unknown")["PATH"])
        done = gitcmd.gh("pr", "view", "--json", "isDraft")
        assert done.returncode == 1
        with pytest.raises(gitcmd.Exited) as raised:
            gitcmd.gh("pr", "view", "--json", "isDraft", check=True)
        assert str(raised.value) == (
            "`gh pr view --json isDraft` exited 1: no pull requests found for "
            'branch "x"'
        )


# What `gh api -i` printed to stdout, in the shape measured with gh 2.92.0
# for a release and an issue that are missing and present (#1572): the
# status line, the headers, an empty line and the body. `gitcmd.gh` reads it
# in text mode, so each line ends in LF.
MISSING = (
    "HTTP/2.0 404 Not Found\nContent-Type: application/json; charset=utf-8\n\n"
    '{"message":"Not Found","status":"404"}'
)
PRESENT = 'HTTP/2.0 200 OK\nContent-Type: application/json\n\n{"state":"open"}'


class Test_http_answer:
    @pytest.mark.parametrize(
        "stdout, answer",
        [
            (MISSING, (404, '{"message":"Not Found","status":"404"}')),
            (PRESENT, (200, '{"state":"open"}')),
            ("HTTP/1.1 204\nServer: x\n\n", (204, "")),
            ("HTTP/2 200 OK\n\nfirst\n\nsecond", (200, "first\n\nsecond")),
        ],
        ids=["a-404", "a-200", "no-reason-phrase", "a-body-holding-an-empty-line"],
    )
    def test_accepts_the_status_line_and_the_body_after_the_headers(
        self, stdout, answer
    ):
        """The status is the status line's second field, and the body is
        everything after the first empty line, an empty line of its own
        among it."""
        assert gitcmd.http_answer(stdout) == answer

    @pytest.mark.parametrize(
        "stdout",
        [
            "",
            "error connecting to no-such-host.invalid\n",
            "HTTP/2.0 2000 OK\n\n{}",
            "HTTP/2.0 20 OK\n\n{}",
            "HTTP/2.0 200OK\n\n{}",
            'Content-Type: x\nHTTP/2.0 200 OK\n\n{"state":"open"}',
        ],
        ids=[
            "nothing-printed",
            "no-http-answer",
            "four-digits",
            "two-digits",
            "no-space-after-the-code",
            "a-status-line-that-is-not-first",
        ],
    )
    def test_refuses_an_answer_with_no_status_line_as_no_status(self, stdout):
        """Text whose first line is not `HTTP/<version> <three digits>`
        carries no status, and the body after its empty line is read as it
        is printed: the callers decide on the status alone."""
        status, body = gitcmd.http_answer(stdout)
        assert status is None
        assert body == stdout.partition("\n\n")[2]


class Test_is_ancestor:
    def test_accepts_a_commit_the_ref_reaches_and_the_ref_itself(self, tmp_path):
        repo = new_repo(tmp_path)
        write(repo, "a.txt", "a\n")
        first = commit(repo, "a")
        write(repo, "a.txt", "b\n")
        second = commit(repo, "b")
        assert gitcmd.is_ancestor(str(repo), first, second) is True
        assert gitcmd.is_ancestor(str(repo), second, second) is True

    def test_refuses_a_commit_the_ref_does_not_reach(self, tmp_path, monkeypatch):
        """A later commit is not reached from an earlier one, and a git that
        did not answer is no `False`: it raises `Unrun`."""
        repo = new_repo(tmp_path)
        write(repo, "a.txt", "a\n")
        first = commit(repo, "a")
        write(repo, "a.txt", "b\n")
        second = commit(repo, "b")
        assert gitcmd.is_ancestor(str(repo), second, first) is False
        starts(monkeypatch, subprocess.TimeoutExpired(["git"], gitcmd.TIMEOUT))
        with pytest.raises(gitcmd.Unrun):
            gitcmd.is_ancestor(str(repo), first, second)


class Test_older:
    """#1642, design S6. The cases supply what `git version` printed, so a
    git older than `OLDEST` is read where none is installed."""

    @pytest.mark.parametrize("version", ["2.29.3", "1.8.3.1"])
    def test_refuses_a_git_older_than_the_floor_naming_both(self, monkeypatch, version):
        """The line names the version git printed and `OLDEST`. 1.8.3.1
        stands for the packaged git of a long-term-support distribution,
        the user #1642 names. Seen red with the comparison against `OLDEST`
        turned round."""
        calls = starts(monkeypatch, (0, f"git version {version}\n", ""))
        assert gitcmd.older("/r") == (
            f"git {version} answers here, and the plugin's scripts need git "
            "2.30 or newer"
        )
        [(command, _)] = calls
        assert command == gitcmd.argv("-C", "/r", "version")

    @pytest.mark.parametrize(
        "printed",
        [
            "git version 2.30.0\n",
            "git version 2.50.1 (Apple Git-155)\n",
            "git version 2.39.2.windows.1\n",
            "git version 3.0.0\n",
        ],
        ids=["the-floor", "apple", "windows", "a-higher-major"],
    )
    def test_accepts_a_git_at_the_floor_or_newer(self, monkeypatch, printed):
        """A version at `OLDEST` or newer is no answer, whatever follows its
        minor number. A major above `OLDEST`'s with a minor below it is
        newer, so the two numbers are compared as one version."""
        starts(monkeypatch, (0, printed, ""))
        assert gitcmd.older("/r") is None

    @pytest.mark.parametrize(
        "code, printed",
        [
            (0, "fakegit version 2.29.3\n"),
            (0, "git version v2.29.3\n"),
            (0, ""),
            (1, "git version 2.29.3\n"),
        ],
        ids=["another-program", "a-v-before-it", "nothing", "a-non-zero-exit"],
    )
    def test_refuses_to_read_a_line_in_another_shape(self, monkeypatch, code, printed):
        """A first line that is not `git version <major>.<minor>` followed
        by anything, or a git that exits non-zero, is not read, and refuses
        nothing. Seen red with the whole-line match loosened to a search,
        and with the exit code unread."""
        starts(monkeypatch, (code, printed, ""))
        assert gitcmd.older("/r") is None

    def test_accepts_the_line_the_git_running_the_suite_prints(self, tmp_path):
        """The git that runs the suite is no older than `OLDEST`, and its
        first line is one `VERSION` reads. None alone would also stand for
        a line in another shape, so the line is matched here too."""
        assert gitcmd.older(str(tmp_path)) is None
        done = subprocess.run(["git", "version"], capture_output=True, encoding="utf-8")
        assert gitcmd.VERSION.fullmatch(done.stdout.split("\n", 1)[0]), done.stdout


# A script that lets `Unrun` reach the interpreter, and an `except
# Exception` around it that must not catch it.
UNCAUGHT = """import sys
sys.path.insert(0, {lib!r})
import gitcmd
try:
    gitcmd.git({where!r}, "status")
except Exception:
    print("caught as an Exception")
"""


class Test_Failed:
    def test_accepts_an_uncaught_one_as_its_line_at_exit_1(self, tmp_path):
        """An entry point that catches nothing ends with the runner's line
        on stderr, at exit 1, and with no traceback (design G14)."""
        lib = os.path.dirname(gitcmd.__file__)
        script = tmp_path / "uncaught.py"
        script.write_text(
            UNCAUGHT.format(lib=lib, where=str(tmp_path)), encoding="utf-8"
        )
        empty = tmp_path / "empty-path"
        empty.mkdir()
        done = subprocess.run(
            [sys.executable, str(script)],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            env={**os.environ, "PATH": str(empty)},
        )
        assert done.returncode == 1, done
        assert done.stdout == ""
        assert done.stderr == "`git status` could not be run: `git` is not on PATH\n"

    def test_refuses_to_be_caught_as_an_exception(self):
        """A handler written for an error of the caller's own does not
        swallow a git that did not answer."""
        assert not issubclass(gitcmd.Failed, Exception)
        assert issubclass(gitcmd.Unrun, SystemExit)
        assert issubclass(gitcmd.Exited, gitcmd.Failed)


test_census = census_case(TARGET)
