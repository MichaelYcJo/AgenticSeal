"""`hooks/worktree_consent.py`: the record a creation that ran leaves, and
the routing answer, the two consent sources the worktree guard reads.

**The harness only runs a `git worktree add` that was approved**, so a
`PostToolUse` observation of one that actually ran is written after the
answer rather than before the question, which is the one thing a command text
cannot forge. An automation run creates its worktrees before any of them has
run, so the person's `automation` answer to the routing question, which the
harness writes into the session's transcript from the click, is the second
source. The writer files a creation under the clone the guard judged, through
the guard's own placement. The guard's reading of both is
`tests/hooks/test_worktree_guard.py`'s. The routing answer's reader is
`hooks/lib/press.py`, and its cases are `tests/hooks/test_press.py`'s.

The cases come from `tests/behaviour/test_the_guard_asks_once_per_session.py`,
`tests/text/test_guard_resolves_the_tree_it_judges.py` and
`tests/test_an_automation_run_meets_no_commit_prompt.py` (#942's phase 6).
"""

import json
import os
import subprocess
import sys

import pytest
from conftest import (
    BASE_TREE_CHAINS,
    PLACEMENT_CHAINS,
    ROOT,
    _a_dirty_w_under_a_clean_session,
    ask_entries,
    census_case,
    consent_dir,
    decision_of,
    grant,
    load_hook_module,
    run_hook,
    write_transcript,
)

TARGET = "hooks/worktree_consent.py"

wg = load_hook_module("worktree-guard.py", "wg_consent")
wc = load_hook_module("worktree_consent.py", "wc_consent")
HOOKS = os.path.join(ROOT, "hooks")


def decide(
    monkeypatch,
    capsys,
    repo,
    command,
    sessions=([], [], True),
    session_id="me",
    cwd=None,
    transcript_path=None,
):
    """`cwd` is where the SHELL is, which is not always `repo`: a `git -C
    <repo> worktree add` issued from outside any repository is the one shape
    that reaches the guard's second silent exit."""
    monkeypatch.setattr(wg, "sessions_in_tree", lambda top, own="": sessions)
    payload = {
        "tool_name": "Bash",
        "session_id": session_id,
        "tool_input": {"command": command},
        "cwd": str(cwd or repo),
    }
    if transcript_path is not None:
        payload["transcript_path"] = str(transcript_path)
    monkeypatch.setattr(wg, "load_input", lambda: payload)
    try:
        wg.main()
    except SystemExit:
        pass
    out = capsys.readouterr().out.strip()
    if not out:
        return "silent", ""
    d = json.loads(out)["hookSpecificOutput"]
    return d["permissionDecision"], d["permissionDecisionReason"]


def post(repo, tool="Bash", command="git worktree add ../wt feature/x", **extra):
    """The payload the harness sends AFTER a tool call has run."""
    payload = {
        "hook_event_name": "PostToolUse",
        "tool_name": tool,
        "session_id": "me",
        "cwd": str(repo),
        "tool_input": {"command": command} if tool == "Bash" else command,
        "tool_response": {"stdout": "", "stderr": "", "interrupted": False},
    }
    payload.update(extra)
    return payload


@pytest.fixture
def projects(monkeypatch, tmp_path):
    """A projects root this case owns, seen by the press reader every copy of
    this module and of the guard imports by its plain name."""
    root = tmp_path / "projects"
    root.mkdir()
    monkeypatch.setattr(sys.modules["press"], "PROJECTS_ROOT", str(root))
    return root


def dispatch_pre_bash(repo, session, transcript_path):
    """The group the harness actually runs, as a subprocess, so a gate that
    raises is skipped exactly the way `hooks/dispatch.py` skips it."""
    r = subprocess.run(
        [sys.executable, os.path.join(HOOKS, "dispatch.py"), "pre-bash"],
        input=json.dumps(
            {
                "tool_name": "Bash",
                "session_id": session,
                "transcript_path": transcript_path,
                "tool_input": {"command": "git worktree add ../wt f"},
                "cwd": str(repo),
            }
        ),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=60,
    )
    return r.stdout


class Test_main:
    """The writer: a creation that actually ran leaves the record."""

    def test_accepts_a_creation_that_ran_and_leaves_a_record(self, repo):
        run_hook("worktree_consent.py", post(repo))
        assert (consent_dir(repo) / "me").is_file()

    def test_accepts_a_creation_anywhere_in_the_command(self, repo):
        """A creation ANYWHERE in a command that ran is a creation that was
        approved, so the writer reads every segment until it finds one. The
        guard's PreToolUse walk judges that same first creation."""
        run_hook(
            "worktree_consent.py",
            post(repo, command="git status && git worktree add ../wt feature/x"),
        )
        assert (consent_dir(repo) / "me").is_file()

    def test_accepts_a_failed_creation_and_still_records_the_approval(self, repo):
        """Q2. The record is about the approval, which happened. The retry after a
        failure — a path that already exists, a branch already checked out — is the
        worst moment to put the question again."""
        run_hook(
            "worktree_consent.py",
            post(
                repo,
                tool_response={
                    "stdout": "",
                    "stderr": "fatal: '../wt' already exists",
                    "interrupted": False,
                    "is_error": True,
                },
            ),
        )
        assert (consent_dir(repo) / "me").is_file()

    def test_accepts_a_linked_worktree_and_files_under_its_clone(self, repo, tmp_path):
        """Q4's neighbour: the SCOPE. A session that creates its first worktree
        from the main tree and its second from inside a linked one has made one
        decision, so it pays for one."""
        linked = tmp_path / "linked"
        subprocess.run(
            ["git", "-C", str(repo), "worktree", "add", "-q", str(linked), "feature/x"],
            check=True,
            capture_output=True,
        )
        run_hook("worktree_consent.py", post(linked))
        assert (consent_dir(repo) / "me").is_file()
        assert consent_dir(linked) == consent_dir(repo)

    def test_accepts_an_isolated_agent_and_writes_the_record_bash_reads(
        self, monkeypatch, capsys, repo
    ):
        run_hook(
            "worktree_consent.py",
            post(repo, tool="Agent", command={"prompt": "x", "isolation": "worktree"}),
        )
        assert (consent_dir(repo) / "me").is_file()
        assert (
            decide(monkeypatch, capsys, repo, "git worktree add ../wt f")[0] == "allow"
        )

    def test_refuses_a_command_that_creates_nothing(self, repo):
        for command in ("git status", "git switch feature/x", "git worktree list"):
            run_hook("worktree_consent.py", post(repo, command=command))
        assert not consent_dir(repo).exists()

    def test_refuses_a_malformed_session_id_escaping_the_directory(self, repo):
        """The id names a file. `../../escaped` put an empty file at a repository
        root once already, through the other marker."""
        run_hook("worktree_consent.py", post(repo, session_id="../../escaped"))
        assert (consent_dir(repo) / "escaped").is_file()
        assert not (repo / "escaped").exists()

    def test_refuses_a_pre_tool_use_payload(self, repo):
        """The writer is wired to one event, and it also refuses a payload that
        names the other. Nothing sends it one; a group misconfigured by hand
        would."""
        payload = post(repo)
        payload["hook_event_name"] = "PreToolUse"
        payload.pop("tool_response")
        run_hook("worktree_consent.py", payload)
        assert not consent_dir(repo).exists()

    def test_refuses_an_agent_without_isolation(self, repo):
        run_hook(
            "worktree_consent.py", post(repo, tool="Agent", command={"prompt": "x"})
        )
        assert not consent_dir(repo).exists()

    def test_refuses_an_unrecordable_consent_and_asks_rather_than_crashing(
        self, monkeypatch, capsys, repo, tmp_path
    ):
        """Q3. A guard that crashes reads as a silent allow — the module says so
        about `_idle_minutes`. The write fails silently instead, no record exists,
        and the next creation meets the question it always did.

        stdout being empty is not the claim: a traceback goes to STDERR and leaves
        stdout empty too, which is how a crashing hook and a quiet one look alike.
        The exit status and stderr are what tell them apart, so both are read."""
        blocked = consent_dir(repo)
        blocked.parent.mkdir(parents=True, exist_ok=True)
        blocked.write_text("not a directory", encoding="utf-8")
        assert wc.record(str(repo), "me") is False
        r = subprocess.run(
            [sys.executable, os.path.join(HOOKS, "worktree_consent.py")],
            input=json.dumps(post(repo)),
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
        )
        assert r.returncode == 0, r.stderr
        assert r.stdout.strip() == ""
        assert r.stderr.strip() == "", r.stderr
        assert (
            decide(monkeypatch, capsys, repo, "git worktree add ../wt f")[0] == "deny"
        )


class Test_consent:
    def test_accepts_the_routing_preset_as_consent(self, projects, repo):
        """The measured answer, and the three decorations measured beside it --
        each on the pressed option's label, which is where a decoration lives. A
        pressed option's answer IS its label: 184 of 184 on disk."""
        for answer in (
            "automation",
            "automation (Recommended)",
            "automation (권장)",
            "automation — 안 멈추고 끝까지",
        ):
            options = (answer, "per axis", "no work item")
            write_transcript(
                projects, "me", ask_entries(repo, answer=answer, options=options)
            )
            assert wc.automation_answered(str(repo), "me"), answer
            assert wc.consent(str(repo), "me") == "answer", answer

    def test_refuses_any_exception_as_consent(self, monkeypatch, repo):
        """The class, not the two instances: both call sites go through
        `consent`, so whatever the reader raises next is *no consent* there."""

        def boom(*a, **k):
            raise RuntimeError("a shape nobody measured")

        monkeypatch.setattr(wc, "automation_answered", boom)
        assert wc.consent(str(repo), "me") == ""
        grant(repo)
        assert wc.consent(str(repo), "me") == "record"

    def test_refuses_a_directory_at_the_record_path(self, monkeypatch, capsys, repo):
        """The record is a FILE, and its existence is the fact. A directory of that
        name is not one — the same distinction `optin.py` draws for
        `agentic-scratch`, where a directory of the marker's name silenced every
        gate in the tree."""
        (consent_dir(repo) / "me").mkdir(parents=True)
        assert not wc.granted(str(repo), "me")
        assert (
            decide(monkeypatch, capsys, repo, "git worktree add ../wt f")[0] == "deny"
        )


class Test_segment_cwd:
    def test_accepts_the_C_target_of_the_segment_that_was_judged(self, repo):
        """`main()` asks `segment_cwd` for the `-C` target of the very segment
        whose shape it read, from the same token list. Reading the two from
        separate tokenizations is how a switch aimed at another repository gets
        judged against THIS tree."""
        cmd = "git -C /x/y switch b  # don't"
        segments, _ = wg.split_command(cmd)
        assert wg.shape_of(segments[0]) == "switch"
        # `normpath`, because `apply_chdir` ends in one: the assertion is that
        # the target followed the segment, not that this platform spells a path
        # with `/`.
        assert wg.segment_cwd(segments[0], "/base") == os.path.normpath("/x/y")

    def test_accepts_a_quoted_C_value_past_an_apostrophe(self, repo):
        """A `-C` value with a space is what separates a quote-aware splitter from
        a whitespace one, and an apostrophe elsewhere in the command must not cost
        it. Both forms were unclassified before the guard borrowed the splitter."""
        for cmd, target in (
            ('git -C "my repo" switch b', "/base/my repo"),
            ("git -C 'my repo' switch b  # don't", "/base/my repo"),
        ):
            segments, _ = wg.split_command(cmd)
            assert wg.shape_of(segments[0]) == "switch", cmd
            assert wg.segment_cwd(segments[0], "/base") == os.path.normpath(target), cmd

    def test_refuses_to_move_a_non_git_segment(self, tmp_path):
        assert wg.segment_cwd(["echo", "hello"], str(tmp_path)) == str(tmp_path)


class Test_creation_directory:
    @pytest.mark.parametrize("name", sorted(BASE_TREE_CHAINS))
    def test_accepts_where_the_base_filed_whatever_the_walk_leads(
        self, repo, tmp_path, name
    ):
        """#689, the consent twin. At `542f920b` the writer filed each creation
        under the walk's first directory, the skipped or unreached one; bash
        creates from `w`, and `86256492` filed it there."""
        session, other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        chain = BASE_TREE_CHAINS[name].format(
            missing=tmp_path / "nosuch-either", other=other
        )
        acted = wg.worktree_consent.creation_directory(
            chain + "git worktree add ../wt", str(session)
        )
        assert os.path.normpath(acted) == str(session / "w"), (name, acted)

    def test_accepts_the_creations_own_dash_c_composed(self, repo, tmp_path):
        """S3 of work item 1791384157, the half the chains do not reach: the
        writer files under the directory the creation's own `-C` names, composed
        onto the directory its segment runs in, as the guard judges it. A
        relative `-C` after a `cd` is the case `place` composes before it falls
        back. A break returning the shell's directory survived until this case."""
        session, other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        for command, expected in (
            (f"git -C {other} worktree add ../wt f", other),
            ("cd w && git -C ../clean worktree add ../wt f", session / "clean"),
        ):
            acted = wg.worktree_consent.creation_directory(command, str(session))
            assert os.path.samefile(acted, expected), (command, acted)

    def test_accepts_the_creation_the_base_filed_behind_a_wider_one(
        self, repo, tmp_path
    ):
        """Round 1 of 1790745049, red 1, the consent twin. `86256492` filed under
        `w`; at `4bc94f05` the first creation, which it did not read as git, was
        filed under the session's clone."""
        session, _other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        acted = wg.worktree_consent.creation_directory(
            "2>/dev/null git worktree add ../wt-a; cd w && git worktree add ../wt-b",
            str(session),
        )
        assert os.path.normpath(acted) == str(session / "w"), acted

    @pytest.mark.parametrize(
        "name",
        [
            "an unreadable segment, then a cd whose failure branch creates",
            "a cd into nothing, then a semicolon",
        ],
    )
    def test_refuses_a_directory_bash_does_not_create_from(self, repo, tmp_path, name):
        """S1 and S2 of work item 1791384157. The writer took the first entry of
        the walk that was not `Unresolved`: the directory the `||` skips in the
        first chain, and a directory that holds nothing in the second, where no
        record was written at all. bash creates from the session's own directory
        in both. Red at `5623d728`, where the writer answered `{other}` and
        `{missing}`."""
        session, other = _a_dirty_w_under_a_clean_session(repo, tmp_path)
        chain = PLACEMENT_CHAINS[name].format(
            missing=tmp_path / "nosuch-either", other=other
        )
        acted = wg.worktree_consent.creation_directory(
            chain + "git worktree add ../wt f", str(session)
        )
        assert os.path.normpath(acted) == str(session), (name, acted)

    def test_refuses_a_creation_written_in_a_comment(self, repo):
        """A comment is not executed, so a `git worktree add` behind a `#`
        created nothing and is filed nowhere."""
        command = "echo hi #; git worktree add ../wt f"
        assert wc.creation_directory(command, str(repo)) == ""


class Test_module:
    def test_the_writer_is_in_both_post_groups(self):
        d = load_hook_module("dispatch.py", "dispatch_consent")
        assert "worktree_consent.py" in d.GROUPS["post-bash"]
        assert "worktree_consent.py" in d.GROUPS["post-agent"]

    def test_hooks_json_sends_the_agent_after_event_to_the_group(self):
        with open(os.path.join(ROOT, "hooks", "hooks.json"), encoding="utf-8") as f:
            cfg = json.load(f)
        matchers = {
            group["matcher"]: group["hooks"][0]["command"]
            for group in cfg["hooks"]["PostToolUse"]
        }
        assert "Agent|Task" in matchers, matchers
        assert "post-agent" in matchers["Agent|Task"]

    def test_a_session_id_that_is_only_separators_has_no_record_path(self, repo):
        """The id names a file, so an id that reduces to nothing must resolve to no
        path at all rather than to the directory above it. Left to the filesystem,
        `..` would be refused by `open` raising on a directory — a defence resting
        on a platform guarantee, which contract rule 13 refuses."""
        for bad in ("", ".", "..", "/", "../..", os.sep):
            assert wc.consent_path(str(repo), bad) == "", bad
        assert wc.consent_path(str(repo), "me").endswith(os.path.join("me"))

    def test_a_shape_the_reader_did_not_expect_keeps_the_guards_deny(
        self, repo, tmp_path
    ):
        """Round 1, finding 2. `dispatch.py` skips a gate that raises, so a
        consent read that raised turned the guard's deny into no decision at all.
        Two inputs raised: a `tool_use_id` that is a list (unhashable) and a NUL in
        `transcript_path`. Each is run through `dispatch.py pre-bash` beside a
        well-formed control, and each must reach the same stop the control does.
        A fresh session id per call, so the guard's own per-session memory is not
        what differs."""
        use, result = ask_entries(repo, answer="per axis")
        control = write_transcript(tmp_path / "t", "s-ok", [use, result])
        use, result = ask_entries(repo)
        result["message"]["content"][0]["tool_use_id"] = ["toolu_01routing"]
        listed = write_transcript(tmp_path / "t", "s-list", [use, result])
        outs = {
            "control": dispatch_pre_bash(repo, "s-ok", str(control)),
            "list id": dispatch_pre_bash(repo, "s-list", str(listed)),
            "NUL path": dispatch_pre_bash(repo, "s-nul", "/x/\x00y/s-nul.jsonl"),
        }
        assert decision_of(outs["control"]) == "deny", outs["control"]
        for name, out in outs.items():
            assert decision_of(out) == "deny", (name, out)


test_census = census_case(TARGET)
