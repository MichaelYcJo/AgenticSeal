"""`hooks/lib/gitcmd.py`: the argv of a git command whose output a script
parses, read the same under any person's or repository's git configuration.

One parameter per key of `gitcmd.KEYS`. Each builds a repository in which
that key, set otherwise than git's default, changes what one command
prints, and names what the command prints under git's default. The scripts'
own readers build their `log` and `status` with `argv`, which the proofer
reads in the diff (`docs/running/what-a-script-gates.md` *Which gate a script
holds*); the cases here hold each key once, over the helper.
"""

import subprocess

import pytest
from conftest import census_case, git, load_hook_module, write

TARGET = "hooks/lib/gitcmd.py"

gitcmd = load_hook_module("lib/gitcmd.py", "gitcmd_for_its_own_file")


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


class Test_module:
    def test_every_key_has_a_case(self):
        """A key added to `KEYS` gets a parameter here, which shows the
        reading it changes."""
        assert [key for key, _ in gitcmd.KEYS] == [c.values[0] for c in CASES]


test_census = census_case(TARGET)
