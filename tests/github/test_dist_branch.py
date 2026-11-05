"""`.github/scripts/dist_branch.py`, through its `main`.

#1374: the plugin directory reads `dist`, and the publish workflow's `dist`
job adds one commit to it at each release, whose tree is `git archive` of
the release's tag:

  D1  no `dist` on the remote: the commit pushed has no parent, and its tree
      holds every file of the tag but those `.gitattributes` marks
      `export-ignore`, a directory pattern among them
  D2  a later release: the commit's parent is the remote's tip, which
      another clone made, and its message names the tag and its commit
  D3  the tip already holds the tag's archive: nothing is pushed, the run
      says so, and it exits 0
  D4  the remote's `dist` moved past the tip the run built on: the push is
      refused as a non-fast-forward, the run exits 1 with git's refusal,
      and no push or fetch it ran forces
  D5  a dry run prints what it would push and pushes nothing, and the
      checkout's own index is left as it was
  D6  a tag the checkout cannot resolve, or no tag named, pushes nothing
      and exits non-zero

**Nothing here reaches GitHub.** Each case drives a real repository in
`tmp_path` whose `origin` is a bare repository beside it.

**Shown red before it was committed (contract rule 15).** Every case was
run against no script, in phase 3 of work item
`1793843890-the-directory-tracks-a-dist-branch`. D5's index assertion,
added after that run, was shown red by a mutant whose `git` set no index
of the run's own.
"""

import importlib.util
import os

from conftest import ROOT, census_case, commit_everything, git, git_out, git_repo, write

TARGET = ".github/scripts/dist_branch.py"

SCRIPT = os.path.join(ROOT, ".github", "scripts", "dist_branch.py")

# `tests/behaviour/test_release_hygiene.py` refuses a loaded document naming
# the running version or anything above it. These are illustrative, which is
# the form that document's own message points at.
EARLIER = "v1.2.2"
TAG = "v1.2.3"
# The fixture's attributes: a directory pattern, which `git check-attr` does
# not answer for the files under it, and a file pattern.
ATTRIBUTES = "* text=auto eol=lf\n/dev/ export-ignore\n/notes.md export-ignore\n"
KEPT = [".gitattributes", "f.txt", "kept.md"]
DROPPED = ["dev/case.py", "notes.md"]
DIST = "refs/heads/dist"


def brancher():
    spec = importlib.util.spec_from_file_location(
        "agentic_dist_branch_for_tests", SCRIPT
    )
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


def released(tmp_path):
    """A repository tagged `EARLIER` and then `TAG`, with `main` and both
    tags on a bare `origin` that holds no `dist`; `(repo, remote)`."""
    remote = tmp_path / "remote.git"
    git(tmp_path, "init", "-q", "--bare", str(remote))
    repo = git_repo(tmp_path / "repo")
    write(repo, ".gitattributes", ATTRIBUTES)
    write(repo, "kept.md", "the release before\n")
    write(repo, "notes.md", "notes\n")
    write(repo, "dev/case.py", "case = 1\n")
    commit_everything(repo, "the release before")
    git_out(repo, "tag", EARLIER)
    write(repo, "kept.md", "the release\n")
    commit_everything(repo, "the release")
    git_out(repo, "tag", TAG)
    git_out(repo, "remote", "add", "origin", str(remote))
    git_out(repo, "push", "-q", "origin", "HEAD:refs/heads/main", "--tags")
    return repo, remote


def elsewhere(tmp_path, remote):
    """A second clone of `remote`, as a later run's checkout is."""
    clone = tmp_path / "elsewhere"
    git(tmp_path, "clone", "-q", "--no-checkout", str(remote), str(clone))
    git_out(clone, "config", "user.email", "t@t.example")
    git_out(clone, "config", "user.name", "t")
    return clone


def wire(monkeypatch, repo, **env):
    mod = brancher()
    monkeypatch.setattr(mod, "ROOT", str(repo))
    monkeypatch.setenv("TAG", env.pop("TAG", TAG))
    monkeypatch.delenv("DRY_RUN", raising=False)
    for key, value in env.items():
        monkeypatch.setenv(key, value)
    return mod


def tip_of(remote):
    """The commit `dist` names on `remote`, or "" where it names none."""
    found = git(remote, "rev-parse", "-q", "--verify", DIST, check=False)
    return found.stdout.strip()


def entries(repo, rev):
    """`{path: "<mode> <type> <object>"}` for every file of REV's tree."""
    out = git_out(repo, "ls-tree", "-r", rev)
    return dict(reversed(line.split("\t", 1)) for line in out.splitlines())


class Test_main:
    def test_accepts_a_first_release_as_a_commit_with_no_parent(
        self, monkeypatch, tmp_path, capsys
    ):
        """D1. The tree is the tag's tree without the marked paths, each kept
        file with the tag's own mode and object."""
        repo, remote = released(tmp_path)
        mod = wire(monkeypatch, repo)
        assert mod.main() == 0
        tip = tip_of(remote)
        assert tip, capsys.readouterr().out
        assert git_out(remote, "rev-list", "--parents", "-n", "1", tip) == tip, (
            "the first commit of `dist` has a parent"
        )
        tagged = entries(repo, TAG)
        assert set(DROPPED) <= set(tagged), tagged
        assert entries(remote, tip) == {path: tagged[path] for path in KEPT}
        assert f"pushed {tip}" in capsys.readouterr().out

    def test_accepts_a_later_release_on_the_tip_another_clone_made(
        self, monkeypatch, tmp_path
    ):
        """D2. The tip is read from `origin`, fetched, and parented on, and
        the message's first line is `dist: <tag>` with the tag's commit in
        its body."""
        repo, remote = released(tmp_path)
        clone = elsewhere(tmp_path, remote)
        assert wire(monkeypatch, clone, TAG=EARLIER).main() == 0
        before = tip_of(remote)
        assert before
        assert wire(monkeypatch, repo).main() == 0
        tip = tip_of(remote)
        assert tip != before
        assert git_out(remote, "rev-parse", f"{tip}^") == before
        subject, body = git_out(remote, "log", "-1", "--format=%s%n%b", tip).split(
            "\n", 1
        )
        assert subject == f"dist: {TAG}", subject
        assert git_out(repo, "rev-parse", f"{TAG}^{{commit}}") in body, body

    def test_makes_nothing_where_the_tip_already_holds_the_tag(
        self, monkeypatch, tmp_path, capsys
    ):
        """D3. A re-run of the workflow after the push pushes nothing and is
        green, read against a tip another clone made."""
        repo, remote = released(tmp_path)
        assert wire(monkeypatch, elsewhere(tmp_path, remote)).main() == 0
        before = tip_of(remote)
        capsys.readouterr()
        assert wire(monkeypatch, repo).main() == 0
        assert tip_of(remote) == before
        out = capsys.readouterr().out
        assert f"already holds the archive of {TAG}" in out, out

    def test_refuses_to_push_over_a_dist_that_moved(
        self, monkeypatch, tmp_path, capsys
    ):
        """D4. Another writer moves `dist` between the run's read of the tip
        and its push. The push is refused, the run exits 1 with git's
        refusal, `dist` keeps the other writer's commit, and no push or
        fetch the run gave git carries a force flag or a `+` refspec."""
        repo, remote = released(tmp_path)
        assert wire(monkeypatch, repo, TAG=EARLIER).main() == 0
        first = tip_of(remote)
        mod = wire(monkeypatch, repo)
        real = mod.git
        ran, moved = [], []

        def racing(*args, **kwargs):
            ran.append(args)
            if args[0] == "push":
                other = git_out(
                    repo, "commit-tree", f"{first}^{{tree}}", "-p", first, "-m", "x"
                )
                git_out(repo, "push", "-q", "origin", f"{other}:{DIST}")
                moved.append(other)
            return real(*args, **kwargs)

        monkeypatch.setattr(mod, "git", racing)
        capsys.readouterr()
        assert mod.main() == 1
        assert moved and tip_of(remote) == moved[0]
        assert "rejected" in capsys.readouterr().out
        forced = [
            arg
            for args in ran
            if args[0] in ("push", "fetch")
            for arg in args
            if arg.startswith(("--force", "+")) or arg == "-f"
        ]
        assert not forced, ran

    def test_refuses_to_push_in_a_dry_run(self, monkeypatch, tmp_path, capsys):
        """D5. The checkout's own index is left as it was, a file staged in
        it among it: the tree is written from an index of the run's own."""
        repo, remote = released(tmp_path)
        write(repo, "staged.md", "s\n")
        git_out(repo, "add", "staged.md")
        staged = git_out(repo, "write-tree")
        assert wire(monkeypatch, repo, DRY_RUN="1").main() == 0
        assert tip_of(remote) == ""
        assert "would push" in capsys.readouterr().out
        assert git_out(repo, "write-tree") == staged

    def test_refuses_a_tag_the_checkout_cannot_resolve(
        self, monkeypatch, tmp_path, capsys
    ):
        """D6. The tag's name reaches the log."""
        repo, remote = released(tmp_path)
        assert wire(monkeypatch, repo, TAG="no-such-tag").main() == 1
        assert tip_of(remote) == ""
        assert "no-such-tag" in capsys.readouterr().out

    def test_refuses_a_run_that_names_no_tag(self, monkeypatch, tmp_path):
        """D6."""
        repo, remote = released(tmp_path)
        assert wire(monkeypatch, repo, TAG="").main() == 2
        assert tip_of(remote) == ""


test_census = census_case(TARGET)
