"""stub-remove: a session takes out the git hook stubs an earlier release wrote.

Nothing of this plugin is installed into git any more (#1027). An earlier
release wrote `pre-commit`, `reference-transaction` and `post-commit` stubs
into a clone's common `hooks/` directory, each carrying the marker line
`# specseal-git-hook` and the absolute path of the plugin copy that wrote it,
so a stub goes on running that copy while it is on disk. At session start the
stubs carrying the marker are removed, and a hook file without it -- a
person's own, or one husky, the pre-commit framework or lefthook wrote -- is
left byte for byte.
"""

import json
import os
import stat
import subprocess
import sys

from conftest import census_case, git, git_repo, load_hook_module

TARGET = "hooks/stub-remove.py"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
HOOKS = os.path.join(ROOT, "hooks")
GATE = "stub-remove.py"


def stub(target, version="0.22.3"):
    """A stub in the shape an earlier release wrote: the marker on its second
    line, then the plugin path it runs."""
    return (
        "#!/bin/sh\n"
        f"# specseal-git-hook {version}\n"
        "# Written by the SpecSeal plugin (hooks/hook-install.py), which rewrites\n"
        "# it when the installed plugin moves and never touches a hook file\n"
        "# without the line above. Removing the plugin leaves this a no-op.\n"
        f"h='{target}'\n"
        '[ -f "$h" ] || exit 0\n'
        'exec sh "$h" "$@"\n'
    )


# Hook files this plugin never wrote, each kept byte for byte. The second
# names the marker in its text, though not as its second line.
HUSKY = '#!/usr/bin/env sh\n. "$(dirname -- "$0")/_/husky.sh"\n\nnpx lint-staged\n'
OWN = (
    "#!/bin/sh\n# my own pre-push; it mentions # specseal-git-hook only here\nexit 0\n"
)


def common_hooks(repo):
    common = git(repo, "rev-parse", "--git-common-dir").stdout.strip()
    path = os.path.normpath(os.path.join(str(repo), common, "hooks"))
    os.makedirs(path, exist_ok=True)
    return os.path.realpath(path)


def plant(directory, name, text, executable=True):
    path = os.path.join(directory, name)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    if executable:
        os.chmod(path, os.stat(path).st_mode | stat.S_IXUSR)
    return path


def start(cwd, session="s1"):
    """Run the hook as a session start would; its stdout. Every failure is
    silent, so a run that exits non-zero or writes to stderr fails here."""
    r = subprocess.run(
        [sys.executable, os.path.join(HOOKS, GATE)],
        input=json.dumps(
            {"hook_event_name": "SessionStart", "session_id": session, "cwd": str(cwd)}
        ),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
    )
    assert (r.returncode, r.stderr) == (0, ""), r.stderr
    return r.stdout


def snapshot(path):
    with open(path, "rb") as f:
        return f.read(), os.stat(path).st_mode


class Test_main:
    def test_accepts_every_marked_stub_and_leaves_every_other_hook_file(self, tmp_path):
        """S15: the three stubs go, and a person's own hook file and a hook
        manager's stay as they were, bytes and mode."""
        repo = git_repo(tmp_path / "repo")
        hooks = common_hooks(repo)
        for name in ("pre-commit", "reference-transaction", "post-commit"):
            plant(hooks, name, stub(f"/x/plugin/hooks/git/{name}.py"))
        own = plant(hooks, "pre-push", OWN)
        husky = plant(hooks, "commit-msg", HUSKY)
        before = {p: snapshot(p) for p in (own, husky)}
        said = json.loads(start(repo))["systemMessage"]
        left = sorted(n for n in os.listdir(hooks) if not n.endswith(".sample"))
        assert left == ["commit-msg", "pre-push"], left
        assert {p: snapshot(p) for p in (own, husky)} == before
        assert said == (
            f"SpecSeal removed the git hooks an earlier release of it wrote in "
            f"{hooks}: pre-commit, reference-transaction and post-commit. "
            "Nothing of SpecSeal runs inside git any more, and a hook file "
            "without the line `# specseal-git-hook` was left as it was."
        )

    def test_refuses_a_foreign_pre_commit_where_a_stub_stood_beside_it(self, tmp_path):
        """A clone whose `pre-commit` slot a hook manager holds kept this
        plugin's stubs for the other two names; those go, and it stays."""
        repo = git_repo(tmp_path / "repo")
        hooks = common_hooks(repo)
        husky = plant(hooks, "pre-commit", HUSKY)
        plant(hooks, "post-commit", stub("/x/plugin/hooks/git/post-commit.py"))
        before = snapshot(husky)
        said = json.loads(start(repo))["systemMessage"]
        assert not os.path.exists(os.path.join(hooks, "post-commit"))
        assert snapshot(husky) == before
        assert f"wrote in {hooks}: post-commit. " in said, said

    def test_accepts_a_linked_worktree_and_takes_out_the_clones_stubs(self, tmp_path):
        """Every worktree of a clone shares one hooks directory, the common
        git directory's, so a session starting in a linked worktree takes the
        stubs out there."""
        repo = git_repo(tmp_path / "repo")
        tree = tmp_path / "tree"
        git(repo, "worktree", "add", "-q", "-b", "side", str(tree))
        hooks = common_hooks(repo)
        plant(hooks, "pre-commit", stub("/x/plugin/hooks/git/pre-commit.py"))
        assert start(tree)
        assert not os.path.exists(os.path.join(hooks, "pre-commit"))

    def test_refuses_to_say_or_change_anything_without_a_stub(self, tmp_path):
        repo = git_repo(tmp_path / "repo")
        hooks = common_hooks(repo)
        own = plant(hooks, "pre-push", OWN)
        before = snapshot(own)
        assert start(repo).strip() == ""
        assert snapshot(own) == before
        outside = tmp_path / "outside"
        outside.mkdir()
        assert start(outside).strip() == ""

    def test_accepts_a_persons_commit_that_runs_no_specseal_code_after_it(
        self, tmp_path
    ):
        """S17. The stub ran the plugin copy whose path it names while that
        copy is on disk: a commit made before the session started runs it, and
        one made after runs nothing of it."""
        repo = git_repo(tmp_path / "repo")
        hooks = common_hooks(repo)
        ran = tmp_path / "ran"
        copy = tmp_path / "plugin-copy.sh"
        copy.write_text(f"#!/bin/sh\necho ran >> '{ran}'\n", encoding="utf-8")
        plant(hooks, "pre-commit", stub(str(copy)))

        def commit(message):
            r = git(repo, "commit", "-q", "--allow-empty", "-m", message, check=False)
            assert r.returncode == 0, r.stderr

        commit("before the session")
        assert ran.read_text(encoding="utf-8") == "ran\n"
        start(repo)
        commit("after the session")
        assert ran.read_text(encoding="utf-8") == "ran\n"


class Test_module:
    def test_the_session_start_group_removes_and_no_group_installs(self):
        """S16's half for the registration: the session-start group runs the
        remover, and no group runs an installer or a gate that reads a commit
        or carries a waiver to git."""
        dispatch = load_hook_module("dispatch.py", "dispatch_for_stub_remove")
        assert GATE in dispatch.GROUPS["session-start"]
        everywhere = {g for gates in dispatch.GROUPS.values() for g in gates}
        for gone in (
            "hook-install.py",
            "commit-review-gate.py",
            "answer-write.py",
            "answer-clear.py",
        ):
            assert gone not in everywhere, gone
            assert not os.path.exists(os.path.join(HOOKS, gone)), gone
        assert not os.path.exists(os.path.join(HOOKS, "git")), "hooks/git/ is back"

    def test_the_dispatcher_carries_the_message(self, tmp_path):
        repo = git_repo(tmp_path / "repo")
        plant(common_hooks(repo), "pre-commit", stub("/x/hooks/git/pre-commit.py"))
        r = subprocess.run(
            [sys.executable, os.path.join(HOOKS, "dispatch.py"), "session-start"],
            input=json.dumps(
                {
                    "hook_event_name": "SessionStart",
                    "session_id": "s1",
                    "cwd": str(repo),
                }
            ),
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
        )
        assert "SpecSeal removed the git hooks" in r.stdout, r.stdout + r.stderr


test_census = census_case(TARGET)
