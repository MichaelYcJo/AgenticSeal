"""version-check — the one hook that reaches the network, and its three limits.

Plugin updates are keyed to plugin.json's version and nothing checks for them,
so a release reaches a user only if that user remembers to run two commands.
This hook removes the remembering. Every test here is about what it must NOT
do: no network without the opt-in, none more than daily, and no noise when
anything goes wrong.
"""

import json
import os
import subprocess
import time

import pytest
from conftest import census_case, load_hook_module, opt_in, run_hook

TARGET = "hooks/version-check.py"


@pytest.fixture
def hook(tmp_path, monkeypatch):
    """The module with its throttle marker redirected into the tmp dir."""
    mod = load_hook_module("version-check.py", "version_check")
    mod.STATE_DIR = str(tmp_path / "state")
    mod.MARKER = os.path.join(mod.STATE_DIR, "version-check")
    return mod


def drive(hook, repo, running=(0, 7, 1), remote=(0, 8, 0), monkeypatch=None):
    """Run main() with the version lookups stubbed; return what it printed."""
    calls = []
    hook.running = lambda: (running, "https://example.com/x/y")
    hook.latest = lambda repo_url: (calls.append(repo_url), remote)[1]
    import contextlib
    import io
    import sys

    buf = io.StringIO()
    stdin = sys.stdin
    sys.stdin = io.StringIO(json.dumps({"cwd": str(repo)}))
    try:
        with contextlib.redirect_stdout(buf):
            hook.main()
    finally:
        sys.stdin = stdin
    return buf.getvalue(), calls


class Test_main:
    # --- it speaks only when there is something to say ---------------------

    def test_accepts_a_newer_release_and_warns(self, hook, repo):
        opt_in(repo)
        out, _ = drive(hook, repo, running=(0, 7, 1), remote=(0, 8, 0))
        msg = json.loads(out)["systemMessage"]
        assert "0.8.0" in msg and "0.7.1" in msg

    def test_accepts_a_warning_that_names_both_commands_in_order(self, hook, repo):
        opt_in(repo)
        out, _ = drive(hook, repo)
        msg = json.loads(out)["systemMessage"]
        assert msg.index("marketplace update agenticseal") < msg.index(
            "update agentic@agenticseal"
        )
        assert "restart" in msg.lower()

    def test_accepts_a_warning_that_names_the_cheap_move_before_the_expensive_one(
        self, hook, repo
    ):
        """`/reload-plugins` costs no session and a restart costs the one you
        are in, so the cheaper move is named first — and the notice may not
        oversell it. The experiment behind this
        (`docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force.md`,
        run 6) measured one thing: a preloaded skill body handed to a SPAWNED
        AGENT is re-read at a reload. It measured nothing about hooks and
        nothing about agent definitions, and its sentinel sat in the running
        version's own directory, so it says nothing about picking up a newly
        installed one either.

        THE WHOLE MESSAGE IS PINNED, EXACTLY, because a predicate over this
        prose cannot be written. Four were tried and each was blind one word
        over:

          1. the words appear anywhere in the message;
          2. the words appear in the SENTENCE that makes the claim;
          3. the clause from `install` to the next comma carries the negation;
          4. and no adversative from a four-word list follows it.

        `unmeasured, yet it is picked up` walks through all four and tells a
        user the opposite of what run 6 found. English has more ways to hand
        an axis back than a list can hold, so this stops being a list.

        What that costs, stated rather than discovered: a legitimate rewording
        fails this case. That is the cost being accepted, because the wording
        IS the contract here — it is what a user reads about what was measured,
        and whoever changes it should have to state the new text deliberately
        instead of satisfying a checker.

        What this does NOT do is check a REWORDING. An author who changes the
        notice and pastes the new text in here passes both cases — measured,
        with the golden brought along each time: an overclaim added to the
        reload's claim, the gap flipped to `unmeasured, yet it is picked up`,
        the restart named before the reload, and the `measured` and `skill
        bodies` labels dropped. Every one left the module at `18 passed`.

        The one property the pair still holds across a rewording is the scope
        qualifier, because
        `test_the_notice_agrees_with_the_docstring_about_what_a_reload_re_reads`
        looks for it independently. Everything else is carried by the message
        below, which is an instruction to a person rather than a check.
        """
        opt_in(repo)
        out, _ = drive(hook, repo)
        msg = json.loads(out)["systemMessage"]

        assert msg == (
            "AgenticSeal 0.8.0 is out; this session is running 0.7.1.\n"
            "Run /agentic:update — it takes the release and tells you what is in "
            "it, which the version number does not.\n"
            "By hand: `claude plugin marketplace update agenticseal` then "
            "`claude plugin update agentic@agenticseal`, in that order. The second "
            "alone reports 'already at the latest version' against stale local "
            "data.\nThen load it. /reload-plugins costs no session, and what was "
            "measured is a re-read of preloaded skill bodies out of the copy you "
            "are already on. Whether it reaches hooks, agent definitions, or the "
            "version you just installed is unmeasured, so restart for those."
        ), (
            "the notice changed. State the new text here deliberately — and check "
            "it against run 6: the reload's claim carries its subject and the copy "
            "it re-reads, and all three unmeasured axes are named as unmeasured "
            "rather than left to silence"
        )

    def test_refuses_to_speak_when_current(self, hook, repo):
        opt_in(repo)
        out, _ = drive(hook, repo, running=(0, 8, 0), remote=(0, 8, 0))
        assert out == ""

    def test_refuses_to_speak_when_ahead_of_the_newest_tag(self, hook, repo):
        """A maintainer's working tree is ahead; telling them to downgrade is wrong."""
        opt_in(repo)
        out, _ = drive(hook, repo, running=(0, 9, 0), remote=(0, 8, 0))
        assert out == ""

    # --- the three limits --------------------------------------------------

    def test_refuses_output_and_network_without_the_opt_in(self, hook, repo):
        out, calls = drive(hook, repo)
        assert out == ""
        assert calls == [], "reached the network in a repo that never opted in"

    def test_refuses_to_speak_when_offline(self, hook, repo):
        opt_in(repo)
        out, calls = drive(hook, repo, remote=None)
        assert calls, "did not even try the lookup"
        assert out == ""

    # --- a hook that crashes must not wedge the session --------------------

    def test_refuses_malformed_stdin_silently(self):
        assert run_hook("version-check.py", None) == ""

    def test_refuses_a_missing_cwd_silently(self):
        assert run_hook("version-check.py", {}) == ""

    def test_refuses_a_path_that_is_not_a_repo_silently(self, tmp_path):
        assert run_hook("version-check.py", {"cwd": str(tmp_path)}) == ""


def plugin_json(directory, version="0.9.0"):
    """A `.claude-plugin/plugin.json` under DIRECTORY naming VERSION."""
    meta = directory / ".claude-plugin"
    meta.mkdir(parents=True)
    (meta / "plugin.json").write_text(
        json.dumps({"version": version, "repository": "https://example.com/x/y"}),
        encoding="utf-8",
    )


class Test_running:
    def test_accepts_the_loaded_plugins_version_and_repository(
        self, hook, tmp_path, monkeypatch
    ):
        plugin_json(tmp_path / "plugin")
        monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", str(tmp_path / "plugin"))
        assert hook.running() == ((0, 9, 0), "https://example.com/x/y")

    def test_refuses_no_plugin_root_whatever_the_cwd_holds(
        self, hook, tmp_path, monkeypatch
    ):
        """No root names no plugin, so the answer is nothing, and a
        `plugin.json` under the working directory is not read as the loaded
        one (#1017, the body's `running` row)."""
        plugin_json(tmp_path)
        monkeypatch.chdir(tmp_path)
        monkeypatch.setenv("CLAUDE_PLUGIN_ROOT", "")
        assert hook.running() == (None, None)
        monkeypatch.delenv("CLAUDE_PLUGIN_ROOT")
        assert hook.running() == (None, None)


class Test_due:
    def test_accepts_a_check_a_day_later(self, hook, repo):
        opt_in(repo)
        drive(hook, repo)
        os.utime(hook.MARKER, (0, 0))
        out, calls = drive(hook, repo)
        assert calls, "never rechecked after the interval elapsed"
        assert json.loads(out)["systemMessage"]

    def test_refuses_a_second_network_call_the_same_day(self, hook, repo):
        opt_in(repo)
        drive(hook, repo)
        out, calls = drive(hook, repo)
        assert out == ""
        assert calls == [], "checked twice in one day"


class Test_retry_soon:
    def test_accepts_a_failed_lookup_and_costs_minutes_not_the_day(self, hook, repo):
        """Offline at session start must not spend the notice until tomorrow."""
        opt_in(repo)
        drive(hook, repo, remote=None)
        assert os.path.exists(hook.MARKER), "throttle was never stamped"

        # Still held: a failure must not make every session retry a hanging call.
        out, calls = drive(hook, repo, running=(0, 7, 1), remote=(0, 8, 0))
        assert out == "" and not calls, "retried immediately after a failure"

        # RETRY seconds later — not INTERVAL — it asks again and says its piece.
        # Without the handback the marker would still read as stamped just now,
        # and twenty minutes off a day leaves this silent.
        m = os.path.getmtime(hook.MARKER)
        os.utime(hook.MARKER, (m - hook.RETRY, m - hook.RETRY))
        out, _ = drive(hook, repo, running=(0, 7, 1), remote=(0, 8, 0))
        assert "0.8.0" in out

    def test_refuses_a_remote_with_no_tags_and_keeps_the_full_day(self, hook, repo):
        """An answer, not a failure: nothing to retry for."""
        opt_in(repo)
        out, _ = drive(hook, repo, remote=())
        assert out == ""
        age = time.time() - os.path.getmtime(hook.MARKER)
        assert age < hook.RETRY, "backed off as if the lookup had failed"


class Test_latest:
    """latest() tells "asked, no tags" from "could not ask" — the throttle
    branches on it, so a stub in `drive` could not carry these."""

    def test_accepts_an_untagged_remote_as_an_answer(self, hook, tmp_path):
        remote = tmp_path / "untagged.git"
        subprocess.run(["git", "init", "-q", "--bare", str(remote)], check=True)
        assert hook.latest(str(remote)) == (), "a reachable remote read as a failure"

    def test_refuses_a_remote_it_cannot_ask(self, hook, tmp_path):
        assert hook.latest(str(tmp_path / "does-not-exist.git")) is None


class Test_parse:
    def test_accepts_the_repo_tag_format(self, hook):
        assert hook.parse("v0.7.1") == (0, 7, 1)
        assert hook.parse("0.7.1") == (0, 7, 1)

    def test_refuses_unrecognised_tag_shapes(self, hook):
        """A tag scheme this does not know must degrade to silence, not a wrong warn."""
        for bad in ("specseal--v0.7.1", "release-0.7", "v1.2", "", None, "latest"):
            assert hook.parse(bad) is None, bad


# Left for #923, under its name: its assertion reads the module's docstring.
def test_the_notice_agrees_with_the_docstring_about_what_a_reload_re_reads(hook):
    """The module docstring scopes a reload to the copy already in force. A
    notice that sells the reload as the way to load the NEW version contradicts
    the file it lives in, and the contradiction is silent: the docstring is at
    the top of the module and the string a user reads is near the bottom, so
    nobody editing one has the other on screen.

    What this case checks is the PRESENCE half of that agreement: the notice
    carries the scope qualifier the docstring states. The absence half — that
    no sentence claims the reload picks up the newly installed version — is
    pinned in the case above, because a mutation that appends `and out of the
    one you just installed` to the reload's claim leaves every phrase this
    case looks for standing.

    The docstring is read whitespace-normalised: it is hand-wrapped prose, so
    `out of that same copy` straddles a line break and a raw `in` is False
    against the very text it is checking.
    """
    doc = " ".join((hook.__doc__ or "").split())
    assert "out of that same copy" in doc, (
        "the docstring no longer scopes the reload to the copy in force, so "
        "this case is comparing the notice against nothing"
    )

    msg = hook.notice((0, 7, 1), (0, 8, 0))
    claim = next((s for s in msg.replace("\n", " ").split(". ") if "/reload" in s), "")
    assert claim, "the notice names no reload for the docstring to disagree with"
    assert any(
        q in claim.lower() for q in ("already on", "in force", "already running")
    ), (
        "the docstring scopes the reload and the notice does not; a user reads the notice"
    )


test_census = census_case(TARGET)
