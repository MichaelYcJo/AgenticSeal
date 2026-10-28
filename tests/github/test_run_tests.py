"""`.github/scripts/run_tests.py`, the runner `bin/test` execs, one class per function.

Issue #156: the repository ships a command for its own suite, and the
second call is cheap. The form `CONTRIBUTING.md` named before resolved its
environment on every call, 55-58 seconds each. These cases pin what decides
whether the runner still works in six months:

  - a warm call reuses the environment and never rebuilds it, which is the
    whole work item;
  - the virtualenv it writes is invisible to git, whichever of the two tools
    built it (`uv venv` writes the ignore, `python -m venv` does not);
  - every way of failing produces a sentence, not a traceback, because the
    runner writes to the working tree and a machine with neither `uv` nor a
    new enough Python has to be told what to install;
  - the narrow form stays narrow, the whole suite runs in parallel by
    default, and the caller's own choice of workers, plugin or debugger wins.

The sentences are pinned because a person reads them and acts on them, which
is the only reason they exist.

#942's phase 6 placed these cases from
`tests/test_the_suite_has_a_command_that_is_cheap_twice.py`, which keeps the
cases that read the `bin/` wrappers, the workflows and the documents.
"""

import importlib.util
import os
import pathlib
import subprocess
import sys

import pytest
from conftest import ROOT, census_case

TARGET = ".github/scripts/run_tests.py"

SCRIPT = os.path.join(ROOT, ".github", "scripts", "run_tests.py")

# Held before any test can replace `subprocess.run` on the module the runner
# imports: `rt.subprocess` IS this module, so a case that fakes the builder's
# calls fakes the git calls that check what the builder left behind.
REAL_RUN = subprocess.run


def _load_runner():
    spec = importlib.util.spec_from_file_location("agentic_run_tests", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


rt = _load_runner()


def fake_venv(root, xdist=True, markdown_it=True, pillow=True, cmarkgfm=True):
    """A directory that looks to `has_pytest` like a built environment, and
    to `has_xdist` like one that carries pytest-xdist (#337) -- the `xdist`
    package directory under site-packages, at the path each platform uses.
    `xdist=False` is the `.venv` built before #337, which the runner adopts
    and repairs. `markdown_it` is the same for the pinned parser (#667):
    its versioned `.dist-info` directory, or `markdown_it=False` for a
    `.venv` built before it, or a version string for one holding another
    version. `pillow` is the same again for the pinned Pillow (#718), and
    `cmarkgfm` for the pinned renderer (#647)."""
    venv = root / ".venv"
    python = rt.venv_python(venv)
    python.parent.mkdir(parents=True)
    python.write_text("", encoding="utf-8")
    (python.parent / ("pytest.exe" if os.name == "nt" else "pytest")).write_text(
        "", encoding="utf-8"
    )
    site = (
        venv / "Lib" / "site-packages"
        if os.name == "nt"
        else venv / "lib" / f"python{rt.FLOOR_TEXT}" / "site-packages"
    )
    site.mkdir(parents=True)
    if xdist:
        (site / "xdist").mkdir()
    if markdown_it:
        version = rt.MARKDOWN_IT_VERSION if markdown_it is True else markdown_it
        (site / f"markdown_it_py-{version}.dist-info").mkdir()
    if pillow:
        version = rt.PILLOW_VERSION if pillow is True else pillow
        (site / f"pillow-{version}.dist-info").mkdir()
    if cmarkgfm:
        version = rt.CMARKGFM_VERSION if cmarkgfm is True else cmarkgfm
        (site / f"cmarkgfm-{version}.dist-info").mkdir()
    return venv


class Recorder:
    """Stands in for `subprocess.run`; records commands, never runs one."""

    def __init__(self, returncode=0):
        self.calls = []
        self.kwargs = []
        self.returncode = returncode

    def __call__(self, command, **kwargs):
        self.calls.append(list(command))
        self.kwargs.append(kwargs)
        return subprocess.CompletedProcess(command, self.returncode)


class FakeSys:
    """An interpreter below the floor, without touching the real `sys`.

    `stderr` is looked up when it is asked for, not when this class is
    defined: capsys replaces `sys.stderr` per test, and a captured-at-import
    handle would send the sentences past the capture — leaving the cases that
    read them unable to fail.
    """

    version_info = (3, 9, 6)
    version = "3.9.6 (main, Jan 1 2026)"
    executable = "/usr/bin/python3"

    @property
    def stderr(self):
        return sys.stderr


def git_status(tmp_path):
    """`git status --porcelain`, run through the real `subprocess.run`.

    Saved at import: a test that fakes `rt.subprocess.run` is faking the
    module, so the git call below would be answered by the fake too.
    """
    return REAL_RUN(
        ["git", "-C", str(tmp_path), "status", "--porcelain"],
        capture_output=True,
        encoding="utf-8",
        check=True,
    ).stdout


# A `chmod 555` directory stops a write only where the operating system says
# it does. Root is not stopped by a permission bit, and on Windows `os.chmod`
# sets the read-only flag and nothing else -- the flag is ignored when a file
# is created inside a directory. On either, the write below would SUCCEED, the
# sentence would never print, and a case asserting it would fail for a reason
# that has nothing to do with the guard. So the fixture case is skipped there
# and `test_the_unwritable_sentence_is_the_same_on_every_platform` carries the
# wording on all three, by making the write itself refuse.
CHMOD_STOPS_A_WRITE = os.name != "nt" and hasattr(os, "geteuid") and os.geteuid() != 0


class Test_ensure:
    def test_accepts_a_built_environment_and_never_rebuilds_it(
        self, tmp_path, monkeypatch
    ):
        """The measured cost was setup paid on every call. A warm call must not
        reach the builder at all — not even to ask a tool whether it is current."""
        venv = fake_venv(tmp_path)
        monkeypatch.setattr(
            rt, "build", lambda _: pytest.fail("a warm call rebuilt the environment")
        )
        assert rt.ensure(venv) == rt.venv_python(venv)

    def test_a_missing_environment_is_built_once(self, tmp_path, monkeypatch):
        """And the cold call does reach it, once."""
        built = []

        def build(venv):
            built.append(venv)
            fake_venv(tmp_path)
            return None

        monkeypatch.setattr(rt, "build", build)
        venv = tmp_path / ".venv"
        assert rt.ensure(venv) == rt.venv_python(venv)
        assert built == [venv]

    def test_a_build_that_leaves_no_pytest_is_a_sentence(
        self, tmp_path, monkeypatch, capsys
    ):
        """A build that reports success and produces nothing usable is the
        half-built state, and the next call would loop through it forever."""
        monkeypatch.setattr(rt, "build", lambda _: None)
        assert rt.ensure(tmp_path / ".venv") is None
        assert "still not in it" in capsys.readouterr().err

    def test_refuses_an_environment_below_the_floor(self, tmp_path, capsys):
        """`FLOOR` was enforced where the runner BUILDS and nowhere else. A `.venv`
        the runner ADOPTS was accepted on the strength of an interpreter file and a
        `pytest*` script, so a directory left by an older Python -- a contributor's,
        or this repository's own from before the floor moved -- ran the suite on a
        version nothing here supports, and said nothing."""
        venv = fake_venv(tmp_path)
        (venv / "pyvenv.cfg").write_text("version = 3.9.6\n", encoding="utf-8")
        assert rt.ensure(venv) is None
        err = capsys.readouterr().err
        assert "3.9.6" in err, (
            "the sentence does not name the version found, so the reader cannot "
            "check the floor against anything"
        )
        assert f"below the {rt.FLOOR_TEXT} floor" in err
        assert "Remove that directory" in err, (
            "the reader is told the environment is wrong and not what to do about it"
        )
        assert "Traceback" not in err

    def test_an_environment_that_says_nothing_about_its_version_is_kept(self, tmp_path):
        """`pyvenv.cfg` is where both builders record the version, and a directory
        without a readable one is not evidence of an old interpreter -- a venv
        built by something else, or one whose file has been edited. Refusing on
        silence turns one unknown into a suite nobody can run, so only a version
        that is BOTH readable and below the floor is refused."""
        venv = fake_venv(tmp_path)
        assert not (venv / "pyvenv.cfg").exists()
        assert rt.ensure(venv) == rt.venv_python(venv)
        (venv / "pyvenv.cfg").write_text(
            "home = /usr/bin\nprompt = '.venv'\n", encoding="utf-8"
        )
        assert rt.ensure(venv) == rt.venv_python(venv)

    def test_an_adopted_environment_is_hidden_too(self, tmp_path):
        """`hide_from_git` ran only at the end of a build, so a `.venv` the runner
        ADOPTS never reached it. That directory is exactly the one with no ignore
        of its own -- `python -m venv` writes none -- and the runner that finds it
        is the one call in its life that could have written one."""
        REAL_RUN(["git", "init", "-q", str(tmp_path)], check=True)
        venv = fake_venv(tmp_path)
        (venv / "pyvenv.cfg").write_text(
            f"version = {rt.FLOOR_TEXT}.0\n", encoding="utf-8"
        )
        assert rt.ensure(venv) == rt.venv_python(venv)
        assert (venv / ".gitignore").read_text(encoding="utf-8").strip() == "*"
        status = git_status(tmp_path)
        assert ".venv" not in status, (
            f"the adopted virtualenv is visible to git: {status!r}"
        )

    def test_a_refused_environment_is_hidden_too(self, tmp_path):
        """The floor refusal returned one line ABOVE the ignore the fix for the
        case above had just added, so the one adopted `.venv` the runner refuses
        was the one it left in `git status` -- and it is the directory least
        likely to carry an ignore of its own, because every version that refusal
        rejects is older than the 3.13 where `python -m venv` began writing one.
        The reader is told to remove the directory; until they do, it is dirt in
        every `git status` they run."""
        REAL_RUN(["git", "init", "-q", str(tmp_path)], check=True)
        venv = fake_venv(tmp_path)
        (venv / "pyvenv.cfg").write_text("version = 3.11.9\n", encoding="utf-8")
        assert rt.ensure(venv) is None, "a below-floor environment is still refused"
        assert (venv / ".gitignore").read_text(encoding="utf-8").strip() == "*"
        status = git_status(tmp_path)
        assert ".venv" not in status, (
            f"the refused virtualenv is visible to git: {status!r}"
        )

    def test_a_directory_no_builder_can_finish_is_hidden_too(
        self, tmp_path, monkeypatch
    ):
        """`build` returns its no-tool sentence from the branch ABOVE its own
        `try`, so `build`'s `finally` never runs and a directory that was already
        there is never reached. Held by `ensure`'s `finally` instead, which is
        why the guarantee is stated over exits rather than over a list of paths:
        this one is not a path anybody would have thought to add.

        Reachable, and on the machines least able to notice: a half-built `.venv`
        from an earlier run, then `uv` gone from PATH and macOS's 3.9 answering
        to `python3`."""
        REAL_RUN(["git", "init", "-q", str(tmp_path)], check=True)
        venv = tmp_path / ".venv"
        venv.mkdir()
        (venv / "pyvenv.cfg").write_text("home = /usr/bin\n", encoding="utf-8")
        monkeypatch.setattr(rt.shutil, "which", lambda _: None)
        monkeypatch.setattr(rt, "sys", FakeSys())
        assert rt.ensure(venv) is None, "a machine with neither tool still refuses"
        monkeypatch.undo()
        assert (venv / ".gitignore").read_text(encoding="utf-8").strip() == "*"
        status = git_status(tmp_path)
        assert ".venv" not in status, (
            f"the unfinishable virtualenv is visible to git: {status!r}"
        )

    def test_nothing_announces_a_build_that_cannot_happen(self, monkeypatch, capsys):
        """The note printed before the strategy was chosen, so the machine with
        neither tool was told a build was starting and then told it was
        impossible. Measured on 3.9.6 with no uv, before the note moved."""
        monkeypatch.setattr(rt.shutil, "which", lambda _: None)
        monkeypatch.setattr(rt, "sys", FakeSys())
        assert rt.ensure(pathlib.Path("/nowhere/.venv")) is None
        err = capsys.readouterr().err
        assert "building" not in err, "a build was announced that could not happen"
        assert "Install uv" in err

    def test_the_unwritable_sentence_is_the_same_on_every_platform(
        self, tmp_path, monkeypatch, capsys
    ):
        """`Test_main::test_an_unwritable_venv_leaves_the_refusal_a_sentence` is
        skipped as root and on Windows, and the suite runs on `ubuntu-latest`,
        `macos-latest` and `windows-latest`. A sentence a person reads is pinned
        by contract rule 14 wherever it can print, so the write is made to
        refuse here instead of the directory being made to refuse it -- the
        guard catches `OSError` and every platform can raise one."""
        real_write_text = pathlib.Path.write_text

        def refuse(self, *args, **kwargs):
            if self.name == ".gitignore":
                raise PermissionError(13, "Permission denied", str(self))
            return real_write_text(self, *args, **kwargs)

        monkeypatch.setattr(pathlib.Path, "write_text", refuse)
        venv = fake_venv(tmp_path)
        (venv / "pyvenv.cfg").write_text("version = 3.11.9\n", encoding="utf-8")
        assert rt.ensure(venv) is None, "the refusal is unchanged"
        err = capsys.readouterr().err
        assert "Traceback" not in err, err
        assert "could not write the ignore" in err
        assert str(venv / ".gitignore") in err
        assert "git status" in err
        assert "Permission denied" in err, (
            "the sentence does not say why the write failed, so a full disk and a "
            "read-only directory read identically"
        )
        assert "until that write can succeed" in err, (
            "the remedy clause names a cause. `except OSError` is four cases -- "
            "permissions, a read-only filesystem, a full disk, a path that is a "
            "directory -- and `make it writable` is wrong advice on two of them "
            "(round 1's finding 3). The reason is carried by strerror above; the "
            "remedy has to say what must become true, not what to change"
        )
        assert "make it writable" not in err, (
            "the superseded remedy is back beside the new one -- a reader acts on "
            "the first thing that names an action"
        )


class Test_hide_from_git:
    def test_accepts_a_built_environment_and_hides_it_from_git(self, tmp_path):
        """`uv venv` writes this ignore and `python -m venv` does not (checked on
        3.12), so the runner writes it whichever built the directory — otherwise
        the fallback path leaves a virtualenv in every `git status`."""
        subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
        venv = tmp_path / ".venv"
        venv.mkdir()
        (venv / "pyvenv.cfg").write_text("home = /usr/bin\n", encoding="utf-8")
        rt.hide_from_git(venv)
        assert (venv / ".gitignore").read_text(encoding="utf-8").strip() == "*"
        status = subprocess.run(
            ["git", "-C", str(tmp_path), "status", "--porcelain"],
            capture_output=True,
            encoding="utf-8",
            check=True,
        ).stdout
        assert ".venv" not in status, f"the virtualenv is visible to git: {status!r}"

    def test_refuses_to_overwrite_an_existing_ignore(self, tmp_path):
        """`uv venv` wrote one already; overwriting it would be this runner
        editing another tool's file for no gain."""
        venv = tmp_path / ".venv"
        venv.mkdir()
        (venv / ".gitignore").write_text("*\n# written by uv\n", encoding="utf-8")
        rt.hide_from_git(venv)
        assert "written by uv" in (venv / ".gitignore").read_text(encoding="utf-8")


class Test_build:
    def test_a_failed_build_still_leaves_no_trace_in_git(self, tmp_path, monkeypatch):
        """The ignore was written after the LAST step succeeded, so the one run
        that ends in a sentence was the run that left a virtualenv behind. The
        install step is what fails on a machine with no network, and it fails
        after `uv venv` has already made the directory."""
        REAL_RUN(["git", "init", "-q", str(tmp_path)], check=True)
        venv = tmp_path / ".venv"

        def run(command, **kwargs):
            venv.mkdir(exist_ok=True)  # `uv venv` made the directory
            return subprocess.CompletedProcess(command, 1)  # the install step failed

        monkeypatch.setattr(rt.shutil, "which", lambda _: "/usr/bin/uv")
        monkeypatch.setattr(rt.subprocess, "run", run)
        assert rt.build(venv), "a failing build step still has to return a sentence"
        monkeypatch.undo()
        assert (venv / ".gitignore").read_text(encoding="utf-8").strip() == "*"
        status = git_status(tmp_path)
        assert ".venv" not in status, (
            f"the half-built virtualenv is visible to git: {status!r}"
        )

    def test_refuses_a_machine_with_neither_tool_and_names_what_to_install(
        self, monkeypatch
    ):
        """The failure to design against: the first call writes to the tree, and a
        machine with no `uv` and macOS's 3.9 under the name `python3` has to be
        told which of the two to fix."""
        monkeypatch.setattr(rt.shutil, "which", lambda _: None)
        monkeypatch.setattr(rt, "sys", FakeSys())
        sentence = rt.build("/nowhere/.venv")
        assert sentence, "no sentence at all — the caller sees a half-built directory"
        assert sentence.startswith("bin/test"), (
            "the sentence has to name the command it is about: the reader typed "
            "bin/test and the runner it reaches has a name they never saw"
        )
        assert "uv" in sentence
        assert "3.12" in sentence, "the floor is what makes the interpreter wrong"
        assert "3.9.6" in sentence, "a reader cannot check a floor without the version"

    def test_a_failing_build_step_is_a_sentence(self, tmp_path, monkeypatch, capsys):
        """A tool that is present and fails — no network, a broken uv — must not
        leave the caller reading exit codes. And the note that a build is starting
        names the tool, so a first call that pauses for a minute is legible."""
        monkeypatch.setattr(rt.shutil, "which", lambda _: "/usr/bin/uv")
        monkeypatch.setattr(rt.subprocess, "run", Recorder(returncode=1))
        sentence = rt.build(tmp_path / ".venv")
        assert sentence and "could not build" in sentence
        assert "run bin/test again" in sentence
        assert "building" in capsys.readouterr().err

    @pytest.mark.parametrize("uv", ["/usr/bin/uv", None])
    def test_accepts_a_fresh_build_and_installs_xdist_beside_pytest(
        self, tmp_path, monkeypatch, uv
    ):
        """A1's other half. Both build strategies -- `uv pip install` and
        `python -m pip install` -- name `pytest-xdist` in the install step, or the
        first call of a fresh clone refuses the parallel default `Test_main`
        pins."""
        recorder = Recorder()
        monkeypatch.setattr(rt.shutil, "which", lambda _: uv)
        monkeypatch.setattr(rt.subprocess, "run", recorder)
        assert rt.build(tmp_path / ".venv") is None
        install = recorder.calls[1]
        assert "install" in install, f"the second step is not the install: {install}"
        assert "pytest" in install and "pytest-xdist" in install, (
            f"the {'uv' if uv else 'pip'} strategy builds an environment without "
            f"xdist: {install}"
        )

    @pytest.mark.parametrize("uv", ["/usr/bin/uv", None])
    def test_a_fresh_build_installs_the_pinned_parser(self, tmp_path, monkeypatch, uv):
        """#667, phase 1. Both build strategies name the pinned markdown-it-py
        in the install step, exactly as `MARKDOWN_IT` spells it -- a bare
        `markdown-it-py` would hand the oracle whatever the index serves today."""
        recorder = Recorder()
        monkeypatch.setattr(rt.shutil, "which", lambda _: uv)
        monkeypatch.setattr(rt.subprocess, "run", recorder)
        assert rt.build(tmp_path / ".venv") is None
        install = recorder.calls[1]
        assert rt.MARKDOWN_IT in install, (
            f"the {'uv' if uv else 'pip'} strategy builds an environment without "
            f"the pinned parser: {install}"
        )
        assert f"markdown-it-py=={rt.MARKDOWN_IT_VERSION}" == rt.MARKDOWN_IT
        # #718: the release seal's renderer, pinned the same way.
        assert rt.PILLOW in install, (
            f"the {'uv' if uv else 'pip'} strategy builds an environment without "
            f"the pinned Pillow: {install}"
        )
        assert f"pillow=={rt.PILLOW_VERSION}" == rt.PILLOW
        # #647: the table walker's renderer, pinned the same way.
        assert rt.CMARKGFM in install, (
            f"the {'uv' if uv else 'pip'} strategy builds an environment without "
            f"the pinned cmarkgfm: {install}"
        )
        assert f"cmarkgfm=={rt.CMARKGFM_VERSION}" == rt.CMARKGFM


class Test_main:
    def test_refuses_a_tree_without_a_suite_in_a_sentence(
        self, tmp_path, monkeypatch, capsys
    ):
        """The shipped-copy case again, one level in: a runner that reaches a tree
        with no `tests/` says so rather than handing pytest an empty argument."""
        monkeypatch.setattr(rt, "repo_root", lambda: tmp_path)
        assert rt.main([]) == 2
        assert "no tests directory" in capsys.readouterr().err

    @pytest.mark.skipif(
        not CHMOD_STOPS_A_WRITE,
        reason="chmod 555 does not stop a write as root, and on Windows chmod "
        "sets only the read-only flag, which does not stop a file being created "
        "inside the directory",
    )
    def test_an_unwritable_venv_leaves_the_refusal_a_sentence(
        self, tmp_path, monkeypatch, capsys
    ):
        """Round 2 of #156's chain moved `hide_from_git` into `ensure`'s
        `finally`, which is what makes the guarantee exit-level rather than a list
        of remembered paths. It also put an unguarded write on the two exits whose
        entire product is a sentence, so a `.venv` the operator has made read-only
        turned the floor refusal into a `PermissionError` traceback printed after
        it -- the module's opening docstring says every failure here is a sentence
        rather than a traceback, and that was the one that was not.

        The runner does not try to make the write succeed. A read-only `.venv` is
        the operator's, and what they are owed is being told what it costs them."""
        REAL_RUN(["git", "init", "-q", str(tmp_path)], check=True)
        (tmp_path / "tests").mkdir()
        venv = fake_venv(tmp_path)
        (venv / "pyvenv.cfg").write_text("version = 3.11.9\n", encoding="utf-8")
        monkeypatch.setattr(rt, "repo_root", lambda: tmp_path)
        venv.chmod(0o555)
        try:
            assert rt.main([]) == 2, "the refusal keeps its own exit code"
            err = capsys.readouterr().err
        finally:
            venv.chmod(0o755)  # or tmp_path cleanup cannot unlink what is inside

        assert "Traceback" not in err, err
        assert "below the" in err and "3.11.9" in err, (
            "the refusal the reader actually needs no longer prints"
        )
        assert "could not write the ignore" in err, (
            "the ignore failed and nothing said so, which is the silent half of "
            "the defect the ignore exists against"
        )
        assert str(venv / ".gitignore") in err, (
            "the sentence does not name the file it could not write, so the "
            "reader cannot go and look at it"
        )
        assert "git status" in err, (
            "the reader is told a write failed and not what it costs them"
        )
        assert not (venv / ".gitignore").exists()
        assert ".venv" in git_status(tmp_path), (
            "the sentence promises the directory shows up in git status; it has "
            "to be true when it prints"
        )

    def test_accepts_the_callers_arguments_and_passes_them_through(
        self, tmp_path, monkeypatch
    ):
        """A5. The narrow form stays the narrow form: the file the caller named
        and nothing wider, with the parallel default appended after it."""
        (tmp_path / "tests").mkdir()
        venv = fake_venv(tmp_path)
        recorder = Recorder()
        monkeypatch.setattr(rt, "repo_root", lambda: tmp_path)
        monkeypatch.setattr(rt.subprocess, "run", recorder)
        assert rt.main(["tests/skills/test_session_cost.py", "-q"]) == 0
        assert recorder.calls == [
            [
                str(rt.venv_python(venv)),
                "-m",
                "pytest",
                "tests/skills/test_session_cost.py",
                "-q",
                "-n",
                "auto",
            ]
        ]

    def test_no_arguments_runs_the_whole_suite(self, tmp_path, monkeypatch):
        (tmp_path / "tests").mkdir()
        fake_venv(tmp_path)
        recorder = Recorder()
        monkeypatch.setattr(rt, "repo_root", lambda: tmp_path)
        monkeypatch.setattr(rt.subprocess, "run", recorder)
        rt.main([])
        assert recorder.calls[0][3] == "tests", (
            f"no arguments means `tests`, and it comes first: {recorder.calls[0]}"
        )

    def test_the_whole_suite_runs_in_parallel_by_default(self, tmp_path, monkeypatch):
        """A1, inverted from `test_it_does_not_pass_n_auto` (#337). That pin held
        the serial default in place: the environment was built with pytest alone,
        so the flag failed on every fresh build, so the runner withheld it, so
        nothing installed xdist. The build carries xdist now, and the default is
        the configuration CI has run on three platforms for every release."""
        (tmp_path / "tests").mkdir()
        fake_venv(tmp_path)
        recorder = Recorder()
        monkeypatch.setattr(rt, "repo_root", lambda: tmp_path)
        monkeypatch.setattr(rt.subprocess, "run", recorder)
        rt.main([])
        command = recorder.calls[0]
        assert "-n" in command and command[command.index("-n") + 1] == "auto", (
            f"the suite runs serially by default: {command}"
        )

    @pytest.mark.parametrize("uv", ["/usr/bin/uv", None])
    def test_an_adopted_environment_without_xdist_is_given_it_once(
        self, tmp_path, monkeypatch, uv
    ):
        """A2. A `.venv` built before #337 has pytest and no xdist, and the runner
        adopts it. One install step, by the same tool order `build` uses, then the
        suite under `-n auto`. Not refused: a missing speed-up is not a wrong
        interpreter, and the below-floor refusal exists because the suite is
        WRONG there, which it is not here."""
        (tmp_path / "tests").mkdir()
        venv = fake_venv(tmp_path, xdist=False)
        recorder = Recorder()
        monkeypatch.setattr(rt, "repo_root", lambda: tmp_path)
        monkeypatch.setattr(rt.shutil, "which", lambda _: uv)
        monkeypatch.setattr(rt.subprocess, "run", recorder)
        assert rt.main([]) == 0
        assert len(recorder.calls) == 2, recorder.calls
        install, run = recorder.calls
        if uv:
            assert install == [
                uv,
                "pip",
                "install",
                "--python",
                str(rt.venv_python(venv)),
                "pytest-xdist",
            ]
        else:
            assert install == [
                str(rt.venv_python(venv)),
                "-m",
                "pip",
                "install",
                "--quiet",
                "pytest-xdist",
            ]
        assert run[:3] == [str(rt.venv_python(venv)), "-m", "pytest"]
        assert run[-2:] == ["-n", "auto"], (
            f"the repaired environment ran serially: {run}"
        )

    def test_an_environment_with_xdist_takes_no_install_step(
        self, tmp_path, monkeypatch
    ):
        """A2's second call. The marker is found by the filesystem alone -- the
        `xdist` package directory under site-packages, never a subprocess -- so a
        warm call reaches pytest first. `Test_ensure::test_accepts_a_built_
        environment_and_never_rebuilds_it`'s rule, extended to the one step this
        work adds."""
        (tmp_path / "tests").mkdir()
        fake_venv(tmp_path)
        recorder = Recorder()
        monkeypatch.setattr(rt, "repo_root", lambda: tmp_path)
        monkeypatch.setattr(rt.subprocess, "run", recorder)
        rt.main([])
        assert len(recorder.calls) == 1, f"a warm call ran an install: {recorder.calls}"
        assert recorder.calls[0][2] == "pytest"

    def test_a_failed_xdist_install_is_a_sentence_and_the_suite_still_runs(
        self, tmp_path, monkeypatch, capsys
    ):
        """A3. No network, a broken uv: the install step exits non-zero. One
        sentence names the package, says the run is serial and names the remedy;
        the suite then runs without `-n auto`, and the exit code is pytest's, not
        the install's."""
        (tmp_path / "tests").mkdir()
        fake_venv(tmp_path, xdist=False)
        calls = []

        def run(command, **kwargs):
            calls.append(list(command))
            return subprocess.CompletedProcess(
                command, 1 if "install" in command else 0
            )

        monkeypatch.setattr(rt, "repo_root", lambda: tmp_path)
        monkeypatch.setattr(rt.shutil, "which", lambda _: "/usr/bin/uv")
        monkeypatch.setattr(rt.subprocess, "run", run)
        assert rt.main([]) == 0, "the exit code is pytest's, and pytest passed"
        err = capsys.readouterr().err
        assert "pytest-xdist" in err, "the sentence does not name the package"
        assert "serial" in err, "the reader is not told the run is serial"
        assert "run bin/test again" in err, "the reader is not told the remedy"
        assert "Traceback" not in err, err
        assert len(calls) == 2 and calls[1][2] == "pytest", calls
        assert "-n" not in calls[1], (
            f"the flag was passed into an environment without xdist: {calls[1]}"
        )

    @pytest.mark.parametrize("held", [False, "3.0.0"], ids=["none", "another version"])
    @pytest.mark.parametrize("uv", ["/usr/bin/uv", None])
    def test_an_adopted_environment_is_given_the_pinned_parser_once(
        self, tmp_path, monkeypatch, uv, held
    ):
        """#667, phase 1. A `.venv` built before #667 has no parser, and one
        somebody filled by hand may hold another version; the runner adopts
        either and gives it the pin in one step, `add_xdist`'s shape, then the
        suite under `-n auto` because xdist is there."""
        (tmp_path / "tests").mkdir()
        venv = fake_venv(tmp_path, markdown_it=held)
        recorder = Recorder()
        monkeypatch.setattr(rt, "repo_root", lambda: tmp_path)
        monkeypatch.setattr(rt.shutil, "which", lambda _: uv)
        monkeypatch.setattr(rt.subprocess, "run", recorder)
        assert rt.main([]) == 0
        assert len(recorder.calls) == 2, recorder.calls
        install, run = recorder.calls
        python = str(rt.venv_python(venv))
        if uv:
            assert install == [uv, "pip", "install", "--python", python, rt.MARKDOWN_IT]
        else:
            assert install == [
                python,
                "-m",
                "pip",
                "install",
                "--quiet",
                rt.MARKDOWN_IT,
            ]
        assert run[:3] == [python, "-m", "pytest"]
        assert run[-2:] == ["-n", "auto"], run

    def test_a_failed_parser_install_is_a_sentence_and_pytest_is_still_called(
        self, tmp_path, monkeypatch, capsys
    ):
        """#667, phase 1, and round 1's finding 3. The install exits non-zero: one
        sentence names the pinned package and says what its absence costs, as
        pytest does it, and names the remedy. Measured 2026-09-29 in a virtualenv
        with pytest 9.1.1 and pytest-xdist 3.8.0 and no parser, over the oracle's
        module and one other: under `-n 2` the other module's 31 cases ran and
        the run exited 1 with one collection error; under `-p no:xdist` pytest
        stopped at collection, `Interrupted: 1 error during collection`, exit 2,
        no case run. The sentence used to promise the first for every run and
        said the error was a sentence of the oracle's own, which it is not.
        pytest is still called, in parallel, and the exit code is pytest's."""
        (tmp_path / "tests").mkdir()
        fake_venv(tmp_path, markdown_it=False)
        calls = []

        def run(command, **kwargs):
            calls.append(list(command))
            return subprocess.CompletedProcess(
                command, 1 if "install" in command else 0
            )

        monkeypatch.setattr(rt, "repo_root", lambda: tmp_path)
        monkeypatch.setattr(rt.shutil, "which", lambda _: "/usr/bin/uv")
        monkeypatch.setattr(rt.subprocess, "run", run)
        assert rt.main([]) == 0
        err = capsys.readouterr().err
        assert rt.MARKDOWN_IT in err, err
        assert "fails to collect with a ModuleNotFoundError" in err, err
        assert "runs every other case and exits non-zero" in err, err
        assert "stops at collection and runs no case" in err, err
        assert "a sentence of their own" not in err, err
        assert "run bin/test again" in err, err
        assert "Traceback" not in err, err
        assert len(calls) == 2 and calls[1][2] == "pytest", calls
        assert calls[1][-2:] == ["-n", "auto"], calls[1]

    @pytest.mark.parametrize("held", [False, "11.0.0"], ids=["none", "another version"])
    @pytest.mark.parametrize("uv", ["/usr/bin/uv", None])
    def test_an_adopted_environment_is_given_the_pinned_pillow_once(
        self, tmp_path, monkeypatch, uv, held
    ):
        """#718, S16. A `.venv` built before Pillow joined `PACKAGES` is adopted
        and topped up in one step, `add_markdown_it`'s shape, then the suite runs
        under `-n auto`. Seen red against the runner with no `add_pillow`."""
        (tmp_path / "tests").mkdir()
        venv = fake_venv(tmp_path, pillow=held)
        recorder = Recorder()
        monkeypatch.setattr(rt, "repo_root", lambda: tmp_path)
        monkeypatch.setattr(rt.shutil, "which", lambda _: uv)
        monkeypatch.setattr(rt.subprocess, "run", recorder)
        assert rt.main([]) == 0
        assert len(recorder.calls) == 2, recorder.calls
        install, run = recorder.calls
        python = str(rt.venv_python(venv))
        if uv:
            assert install == [uv, "pip", "install", "--python", python, rt.PILLOW]
        else:
            assert install == [python, "-m", "pip", "install", "--quiet", rt.PILLOW]
        assert run[:3] == [python, "-m", "pytest"]
        assert run[-2:] == ["-n", "auto"], run

    def test_a_failed_pillow_install_is_a_sentence_and_pytest_is_still_called(
        self, tmp_path, monkeypatch, capsys
    ):
        """#718, S16. The top-up exits non-zero: one sentence names the pinned
        package, says what its absence costs -- the release seal's pixel cases
        fail, and nothing else does, because Pillow is imported inside those
        cases rather than at module level -- and names the remedy. pytest is
        still called, in parallel, and the exit code is pytest's."""
        (tmp_path / "tests").mkdir()
        fake_venv(tmp_path, pillow=False)
        calls = []

        def run(command, **kwargs):
            calls.append(list(command))
            return subprocess.CompletedProcess(
                command, 1 if "install" in command else 0
            )

        monkeypatch.setattr(rt, "repo_root", lambda: tmp_path)
        monkeypatch.setattr(rt.shutil, "which", lambda _: "/usr/bin/uv")
        monkeypatch.setattr(rt.subprocess, "run", run)
        assert rt.main([]) == 0
        err = capsys.readouterr().err
        assert rt.PILLOW in err, err
        # #1009 S9: Pillow draws the release seal and the seal's pixel cases
        # read what it draws, so the line announcing the top-up says both, and
        # the line after the failed install names those cases as the ones that
        # fail. Seen red against #832's sentences.
        assert "Pillow draws the release seal" in err, err
        assert "the release seal's pixel cases read what it draws" in err, err
        assert "Only the release seal's pixel cases import it" in err, err
        assert "so those cases fail with a ModuleNotFoundError" in err, err
        assert "every other case runs" in err, err
        assert "run bin/test again" in err, err
        assert "Traceback" not in err, err
        assert len(calls) == 2 and calls[1][2] == "pytest", calls
        assert calls[1][-2:] == ["-n", "auto"], calls[1]

    @pytest.mark.parametrize(
        "held", [False, "2024.11.20"], ids=["none", "another version"]
    )
    @pytest.mark.parametrize("uv", ["/usr/bin/uv", None])
    def test_an_adopted_environment_is_given_the_pinned_renderer_once(
        self, tmp_path, monkeypatch, uv, held
    ):
        """#647. A `.venv` built before cmarkgfm joined `PACKAGES` is adopted and
        topped up in one step, `add_markdown_it`'s shape, then the suite runs
        under `-n auto`."""
        (tmp_path / "tests").mkdir()
        venv = fake_venv(tmp_path, cmarkgfm=held)
        recorder = Recorder()
        monkeypatch.setattr(rt, "repo_root", lambda: tmp_path)
        monkeypatch.setattr(rt.shutil, "which", lambda _: uv)
        monkeypatch.setattr(rt.subprocess, "run", recorder)
        assert rt.main([]) == 0
        assert len(recorder.calls) == 2, recorder.calls
        install, run = recorder.calls
        python = str(rt.venv_python(venv))
        if uv:
            assert install == [uv, "pip", "install", "--python", python, rt.CMARKGFM]
        else:
            assert install == [python, "-m", "pip", "install", "--quiet", rt.CMARKGFM]
        assert run[:3] == [python, "-m", "pytest"]
        assert run[-2:] == ["-n", "auto"], run

    def test_a_failed_renderer_install_is_a_sentence_and_pytest_is_still_called(
        self, tmp_path, monkeypatch, capsys
    ):
        """#647. The top-up exits non-zero: one sentence names the pinned package,
        says what its absence costs as pytest does it -- the walker's module fails
        to collect, which a parallel run reports beside every other case and a
        serial one stops at -- and names the remedy. pytest is still called, in
        parallel, and the exit code is pytest's."""
        (tmp_path / "tests").mkdir()
        fake_venv(tmp_path, cmarkgfm=False)
        calls = []

        def run(command, **kwargs):
            calls.append(list(command))
            return subprocess.CompletedProcess(
                command, 1 if "install" in command else 0
            )

        monkeypatch.setattr(rt, "repo_root", lambda: tmp_path)
        monkeypatch.setattr(rt.shutil, "which", lambda _: "/usr/bin/uv")
        monkeypatch.setattr(rt.subprocess, "run", run)
        assert rt.main([]) == 0
        err = capsys.readouterr().err
        assert rt.CMARKGFM in err, err
        assert "fails to collect with a ModuleNotFoundError" in err, err
        assert "runs every other case and exits non-zero" in err, err
        assert "stops at collection and runs no case" in err, err
        assert "run bin/test again" in err, err
        assert "Traceback" not in err, err
        assert len(calls) == 2 and calls[1][2] == "pytest", calls
        assert calls[1][-2:] == ["-n", "auto"], calls[1]

    @pytest.mark.parametrize(
        "own",
        [
            ["-n", "2"],
            ["-n2"],
            ["-nauto"],
            ["--numprocesses", "2"],
            ["--numprocesses=2"],
            ["-p", "no:xdist"],
            ["-pno:xdist"],
            ["-p=no:xdist"],
            ["--pdb"],
        ],
    )
    def test_the_callers_own_choice_wins(self, tmp_path, monkeypatch, own):
        """A4. A worker count of the caller's own, the plugin switched off, or
        `--pdb`, and the runner adds nothing: the arguments pass through as
        typed. `--pdb` is there because a debugger and distribution do not mix --
        measured with pytest-xdist 3.8.0: `-n 2 --pdb` exits 4 with xdist's
        `UsageError`, and `-n auto --pdb` is collapsed by xdist to zero workers,
        so withholding reaches the serial run by the shorter route. W1 of the
        work item tried `--sw`, `--lf -x`, `-s`, `-x` and `--trace` beside
        `-n auto` against the built environment and pytest accepted each, so
        none joins the list."""
        (tmp_path / "tests").mkdir()
        venv = fake_venv(tmp_path)
        recorder = Recorder()
        monkeypatch.setattr(rt, "repo_root", lambda: tmp_path)
        monkeypatch.setattr(rt.subprocess, "run", recorder)
        rt.main(["tests/test_x.py", *own])
        assert recorder.calls == [
            [str(rt.venv_python(venv)), "-m", "pytest", "tests/test_x.py", *own]
        ], (
            f"the runner added to arguments the caller had already settled: {recorder.calls}"
        )

    def test_pytest_runs_from_the_repository_root(self, tmp_path, monkeypatch):
        """So `bin/test tests/x.py` means the same thing from any directory, which
        is the scenario a session hits: it is rarely at the root."""
        (tmp_path / "tests").mkdir()
        fake_venv(tmp_path)
        recorder = Recorder()
        monkeypatch.setattr(rt, "repo_root", lambda: tmp_path)
        monkeypatch.setattr(rt.subprocess, "run", recorder)
        rt.main([])
        assert recorder.kwargs[0]["cwd"] == str(tmp_path)

    def test_it_names_the_interpreter_it_used(self, tmp_path, monkeypatch, capsys):
        """Two virtualenvs on one machine is the ordinary case — a worktree has
        its own — so which one ran the suite is not something to infer."""
        (tmp_path / "tests").mkdir()
        venv = fake_venv(tmp_path)
        monkeypatch.setattr(rt, "repo_root", lambda: tmp_path)
        monkeypatch.setattr(rt.subprocess, "run", Recorder())
        rt.main([])
        assert str(rt.venv_python(venv)) in capsys.readouterr().err

    def test_the_exit_code_is_pytests(self, tmp_path, monkeypatch):
        """A runner that swallows the suite's verdict is a green gate over a red
        suite."""
        (tmp_path / "tests").mkdir()
        fake_venv(tmp_path)
        monkeypatch.setattr(rt, "repo_root", lambda: tmp_path)
        monkeypatch.setattr(rt.subprocess, "run", Recorder(returncode=1))
        assert rt.main([]) == 1


class Test_module:
    def test_the_root_is_the_repository_not_the_scripts_directory(self):
        """`.github/scripts/` up two. One level off and the virtualenv lands in
        `.github/`, where nothing looks for it."""
        assert rt.repo_root() == pathlib.Path(ROOT).resolve()


test_census = census_case(TARGET)
