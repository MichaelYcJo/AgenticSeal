"""`skills/verify/scripts/core_check.py`: whether a session's context holds the core.

A session receives the core, `skills/core/SKILL.md`, from the plugin's
`SessionStart` hook under a first line naming the file printed, the
plugin's version and the file's SHA-256 (#1177). `seal core` reads that
entry back from the session's transcript and passes only where the context
holds it once, whole, and matching the file the line names. The cases are
S5 of work item 1793273065, over planted transcripts in the shape Claude
Code 2.1.312 writes: a `hook_success` attachment per hook run, and a
`compact_boundary` system entry at each compaction, listing the entries it
keeps in `compactMetadata.preservedMessages.uuids`. The harness drops the
trailing newlines of what it hands the model, so a planted entry's
`content` is its `stdout` without them, as a real one is.
"""

import hashlib
import os
import subprocess
import sys

import pytest
from conftest import (
    ROOT,
    census_case,
    git_repo,
    load_hook_module,
    load_module,
    write_transcript,
)

TARGET = "skills/verify/scripts/core_check.py"

SCRIPT = os.path.join(ROOT, *TARGET.split("/"))
CORE = ("skills", "core", "SKILL.md")


def check():
    return load_module(SCRIPT, "core_check_for_its_cases")


def core_module():
    return load_hook_module("lib/core.py", "core_for_the_checks_cases")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return path


def plugin(where, text="# The core\n\nOne value.\n"):
    """A scratch plugin root at WHERE, with a manifest and a core."""
    write(
        os.path.join(where, ".claude-plugin", "plugin.json"),
        '{"name": "agentic", "version": "0.25.0"}',
    )
    write(os.path.join(where, *CORE), text)
    return str(where)


def printed(root):
    """What the hook prints for a session outside any clone, as the
    dispatcher's `print` leaves it: `output` and a newline."""
    return core_module().output(str(root), str(root)) + "\n"


def hook(stdout, name="SessionStart:startup", uuid="h1", content=None, event=None):
    """A `hook_success` attachment entry, its `content` the `stdout` without
    its trailing newlines unless CONTENT is given."""
    return {
        "type": "attachment",
        "uuid": uuid,
        "attachment": {
            "type": "hook_success",
            "hookName": name,
            "hookEvent": event or name.split(":")[0],
            "stdout": stdout,
            "content": stdout.rstrip("\n") if content is None else content,
            "stderr": "",
            "exitCode": 0,
            "command": "python3 dispatch.py session-core",
        },
    }


def boundary(preserved=(), uuid="b1"):
    return {
        "type": "system",
        "subtype": "compact_boundary",
        "uuid": uuid,
        "parentUuid": None,
        "compactMetadata": {
            "trigger": "manual",
            "preservedMessages": {"uuids": list(preserved)},
        },
    }


def said(text, uuid):
    return {"type": "user", "uuid": uuid, "message": {"role": "user", "content": text}}


def summary(uuid="s1"):
    return {**said("This session is being continued.", uuid), "isCompactSummary": True}


class Test_find:
    def test_accepts_the_given_path_or_the_sessions_file_under_any_project(
        self, tmp_path
    ):
        """The project directory's name encodes where the session started,
        which a worktree changes, so every project directory is searched for
        the session's file."""
        check_ = check()
        given = write(str(tmp_path / "t.jsonl"), "")
        assert check_.find({}, given) == (given, None)
        config = tmp_path / "config"
        planted = write_transcript(config / "projects", "abc", [], slug="-Users-x-a")
        environ = {"CLAUDE_CODE_SESSION_ID": "abc", "CLAUDE_CONFIG_DIR": str(config)}
        assert check_.find(environ, None) == (str(planted), None)

    def test_accepts_the_newest_where_two_projects_hold_the_session(self, tmp_path):
        check_ = check()
        config = tmp_path / "config"
        older = write_transcript(config / "projects", "abc", [], slug="-Users-x-b")
        newer = write_transcript(config / "projects", "abc", [], slug="-Users-x-a")
        os.utime(older, (1_000, 1_000))
        os.utime(newer, (2_000, 2_000))
        environ = {"CLAUDE_CODE_SESSION_ID": "abc", "CLAUDE_CONFIG_DIR": str(config)}
        assert check_.find(environ, None) == (str(newer), None)

    def test_refuses_with_a_reason_where_no_transcript_can_be_named(self, tmp_path):
        """S5: no session id fails, and so does a session or a path with no
        file."""
        check_ = check()
        path, reason = check_.find({}, None)
        assert path is None
        assert "CLAUDE_CODE_SESSION_ID is not set" in reason, reason
        assert "--transcript" in reason, reason
        environ = {"CLAUDE_CODE_SESSION_ID": "abc", "CLAUDE_CONFIG_DIR": str(tmp_path)}
        path, reason = check_.find(environ, None)
        assert path is None
        assert "session abc" in reason and str(tmp_path) in reason, reason
        gone = str(tmp_path / "gone.jsonl")
        assert check_.find(environ, gone) == (None, f"no transcript at {gone}.")


class Test_entries:
    def test_accepts_each_json_object_in_file_order(self, tmp_path):
        check_ = check()
        path = write_transcript(tmp_path, "s", [said("a", "u1"), said("b", "u2")])
        assert [e["uuid"] for e in check_.entries(str(path))] == ["u1", "u2"]

    def test_refuses_a_line_that_is_not_a_json_object(self, tmp_path):
        """A torn last line, a blank line and a JSON value that is not an
        object are passed over, so the rest of the transcript is read."""
        check_ = check()
        path = write_transcript(
            tmp_path, "s", ["", "{torn", "[1, 2]", '"text"', said("a", "u1")]
        )
        assert check_.entries(str(path)) == [said("a", "u1")]


class Test_in_context:
    def test_accepts_every_entry_with_no_boundary_and_what_the_last_one_keeps(self):
        """S5: with no compaction every entry is in context; after one, what
        follows the last boundary and what that boundary preserves."""
        check_ = check()
        plain = [said("a", "u1"), said("b", "u2")]
        assert check_.in_context(plain) == plain
        kept, dropped = said("kept", "u1"), said("dropped", "u2")
        after = [boundary(["u1"]), summary(), said("c", "u3")]
        assert check_.in_context([kept, dropped, *after]) == [kept, *after]

    def test_refuses_what_only_an_earlier_boundary_kept(self):
        """S5: an entry before the last boundary is out of context unless
        that boundary lists it; an earlier boundary's list does not count."""
        check_ = check()
        first, second = said("first", "u1"), said("second", "u2")
        entries = [first, boundary(["u1"], "b1"), second, boundary([], "b2")]
        assert check_.in_context(entries) == [boundary([], "b2")]
        # A boundary with no list of what it keeps, or a field of another
        # type in its place, keeps nothing.
        bare = {"type": "system", "subtype": "compact_boundary", "uuid": "b3"}
        assert check_.in_context([first, bare]) == [bare]
        mapped = boundary(uuid="b4")
        mapped["compactMetadata"]["preservedMessages"]["uuids"] = {"u1": True}
        assert check_.in_context([first, mapped]) == [mapped]


class Test_core_entries:
    def test_accepts_a_sessionstart_hook_success_that_opens_with_a_header(
        self, tmp_path
    ):
        check_ = check()
        root = plugin(tmp_path / "plugin")
        entry = hook(printed(root), "SessionStart:compact")
        assert check_.core_entries([said("a", "u1"), entry]) == [entry]

    def test_refuses_every_other_entry(self, tmp_path):
        """A hook of another event, a hook that failed, a start hook whose
        output is JSON or the missing-core line, and an entry that is not an
        attachment are not core entries, so a transcript whose shape changed
        holds none."""
        check_ = check()
        root = plugin(tmp_path / "plugin")
        out = printed(root)
        missing = "AgenticSeal core: /x/SKILL.md is not a file, so no core was printed."
        failed = hook(out)
        failed["attachment"]["type"] = "hook_error"
        others = [
            hook(out, "PreToolUse:Bash"),
            failed,
            hook("{}\n"),
            hook(missing),
            {**hook(out), "type": "user"},
            {"type": "attachment", "attachment": "text"},
            {
                "type": "attachment",
                "attachment": {**hook(out)["attachment"], "stdout": 7},
            },
        ]
        assert check_.core_entries(others) == []


class Test_judge:
    def test_accepts_one_whole_core_entry_matching_its_file(self, tmp_path):
        """S5: one startup entry passes, and the line names the file, the
        version, the digest and the hook."""
        check_ = check()
        root = plugin(tmp_path / "plugin")
        path = os.path.join(root, *CORE)
        with open(path, "rb") as f:
            digest = hashlib.sha256(f.read()).hexdigest()
        code, line = check_.judge([said("a", "u0"), hook(printed(root))], False, "/f")
        assert code == 0, line
        assert line == (
            f"seal core: {path}, plugin 0.25.0, sha256 {digest}, from "
            "SessionStart:startup, in context once."
        )
        # An entry that names no hook is named by its event.
        unnamed = hook(printed(root))
        del unnamed["attachment"]["hookName"]
        code, line = check_.judge([unnamed], False, "/f")
        assert (code, line.endswith("from SessionStart, in context once.")) == (0, True)

    def test_accepts_the_compact_entry_after_a_boundary_that_dropped_the_start(
        self, tmp_path
    ):
        """S5: startup, a compaction that kept nothing of it, then the
        compact run's entry: one in context."""
        check_ = check()
        out = printed(plugin(tmp_path / "plugin"))
        entries = [
            hook(out, uuid="h1"),
            said("work", "u1"),
            boundary(["u1"]),
            summary(),
            hook(out, "SessionStart:compact", uuid="h2"),
        ]
        code, line = check_.judge(entries, False, "/f")
        assert code == 0, line
        assert "from SessionStart:compact, in context once." in line, line

    def test_refuses_a_context_with_no_core_entry_and_names_the_file_to_open(
        self, tmp_path
    ):
        """S5: no entry fails, and so does an entry only before the last
        boundary. The line names the file the session opens instead."""
        check_ = check()
        out = printed(plugin(tmp_path / "plugin"))
        for entries in (
            [said("a", "u1")],
            [hook(out), boundary(), summary()],
        ):
            code, line = check_.judge(entries, False, "/Users/x/SKILL.md")
            assert code == 1, line
            assert line.startswith(
                "seal core: no core entry in this session's context"
            ), line
            assert "open /Users/x/SKILL.md once" in line, line
            assert "--bare" not in line, line

    def test_refuses_under_bare_and_names_it(self):
        """S5: `CLAUDE_CODE_SIMPLE=1` is a `--bare` session, which runs no
        plugin hook, and the line says so."""
        code, line = check().judge([], True, "/f")
        assert code == 1
        assert "--bare" in line and "CLAUDE_CODE_SIMPLE=1" in line, line

    def test_refuses_two_core_entries_in_context(self, tmp_path):
        """S5: a start entry the boundary preserves and the compact run's
        entry are two copies in context, and so are a start and a clear in
        one file."""
        check_ = check()
        out = printed(plugin(tmp_path / "plugin"))
        for entries in (
            [hook(out, uuid="h1"), boundary(["h1"]), hook(out, "SessionStart:compact")],
            [hook(out, uuid="h1"), hook(out, "SessionStart:clear", uuid="h2")],
        ):
            code, line = check_.judge(entries, False, "/f")
            assert code == 1, line
            assert line.startswith(
                "seal core: 2 core entries are in this session's context"
            ), line
            assert "SessionStart:startup" in line, line

    def test_refuses_a_preview_in_place_of_the_output(self, tmp_path):
        """S5: past the harness's cap the model receives a preview while
        `stdout` keeps the whole output, so `content` is compared."""
        check_ = check()
        out = printed(plugin(tmp_path / "plugin"))
        preview = "<persisted-output>\nOutput too large (12.0KB).\n</persisted-output>"
        code, line = check_.judge([hook(out, content=preview)], False, "/f")
        assert code == 1, line
        assert "is not what the hook printed" in line, line
        assert f"{len(preview)} characters" in line, line
        # An entry with no `content` at all says the model received nothing.
        silent = hook(out)
        del silent["attachment"]["content"]
        code, line = check_.judge([silent], False, "/f")
        assert code == 1 and "(0 characters of content)" in line, line

    def test_refuses_a_file_changed_or_gone_since_the_session_read_it(self, tmp_path):
        """S5: a file changed after the start fails on the digest, a named
        file that is gone fails, and a body that is not the file's fails
        though the digest agrees."""
        check_ = check()
        root = plugin(tmp_path / "plugin")
        path = os.path.join(root, *CORE)
        out = printed(root)
        write(path, "# The core\n\nAnother value.\n")
        code, line = check_.judge([hook(out)], False, "/f")
        assert code == 1, line
        assert line.startswith(f"seal core: {path} has changed since"), line
        os.remove(path)
        code, line = check_.judge([hook(out)], False, "/f")
        assert code == 1, line
        assert line.startswith(f"seal core: {path}, which the core entry's"), line
        write(path, "# The core\n\nOne value.\n")
        torn = out.replace("One value.", "One valve.")
        code, line = check_.judge([hook(torn)], False, "/f")
        assert code == 1, line
        assert "is not the text of" in line, line

    def test_refuses_nothing_for_line_endings_or_trailing_newlines(self, tmp_path):
        """A Windows console's carriage returns and the newlines the harness
        drops change no line of the core, so they are no difference."""
        check_ = check()
        out = printed(plugin(tmp_path / "plugin"))
        crlf = out.replace("\n", "\r\n")
        code, line = check_.judge([hook(crlf, content=out + "\n\n")], False, "/f")
        assert code == 0, line


class Test_main:
    def test_accepts_a_passing_transcript_and_prints_one_line(self, tmp_path, capsys):
        root = plugin(tmp_path / "plugin")
        config = tmp_path / "config"
        write_transcript(config / "projects", "abc", [hook(printed(root))])
        environ = {"CLAUDE_CODE_SESSION_ID": "abc", "CLAUDE_CONFIG_DIR": str(config)}
        assert check().main([], environ, str(tmp_path)) == 0
        out = capsys.readouterr().out
        assert out.count("\n") == 1 and out.endswith("in context once.\n"), out

    def test_refuses_with_exit_1_and_names_the_plugins_core_to_open(
        self, tmp_path, capsys
    ):
        """S5: no session id and no transcript each exit 1 with the reason. A
        transcript with no core entry names the core this plugin's hook would
        print for the working directory: in a clone of the plugin, the
        clone's; elsewhere, the plugin's own. `CLAUDE_CODE_SIMPLE=1` names
        `--bare`."""
        check_ = check()
        assert check_.main([], {}, str(tmp_path)) == 1
        assert "CLAUDE_CODE_SESSION_ID is not set" in capsys.readouterr().out
        environ = {"CLAUDE_CODE_SESSION_ID": "abc", "CLAUDE_CONFIG_DIR": str(tmp_path)}
        assert check_.main([], environ, str(tmp_path)) == 1
        assert "no transcript for session abc" in capsys.readouterr().out
        planted = str(write_transcript(tmp_path, "s", [said("a", "u1")]))
        clone = plugin(git_repo(tmp_path / "clone"))
        assert check_.main(["--transcript", planted], {}, clone) == 1
        out = capsys.readouterr().out
        assert f"open {os.path.join(clone, *CORE)} once" in out, out
        assert "--bare" not in out, out
        outside = tmp_path / "outside"
        outside.mkdir()
        bare = {"CLAUDE_CODE_SIMPLE": "1"}
        assert check_.main(["--transcript", planted], bare, str(outside)) == 1
        out = capsys.readouterr().out
        own = os.path.normpath(os.path.join(ROOT, *CORE))
        assert f"open {own} once" in out and "--bare" in out, out

    def test_refuses_an_unknown_argument_with_exit_2(self, tmp_path):
        with pytest.raises(SystemExit) as stopped:
            check().main(["--nope"], {}, str(tmp_path))
        assert stopped.value.code == 2


class Test_module:
    def test_seal_core_runs_this_script(self, tmp_path):
        """The subcommand a person types, `! seal core`, reaches this script
        through `seal.py#TOOLS` and answers with its exit code."""
        root = plugin(tmp_path / "plugin")
        planted = write_transcript(tmp_path, "s", [hook(printed(root))])
        done = subprocess.run(
            [
                sys.executable,
                os.path.join(ROOT, "skills", "implement", "scripts", "seal.py"),
                "core",
                "--transcript",
                str(planted),
            ],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            cwd=str(tmp_path),
        )
        assert done.returncode == 0, done.stdout + done.stderr
        assert done.stdout.endswith("in context once.\n"), done.stdout

    def test_the_help_says_an_agents_run_reads_the_session_that_spawned_it(self):
        done = subprocess.run(
            [sys.executable, SCRIPT, "--help"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )
        assert done.returncode == 0, done.stderr
        text = " ".join(done.stdout.split())
        assert "spawned it" in text and "CLAUDE_CODE_SESSION_ID" in text, text

    def test_a_script_copied_alone_exits_2_and_names_the_module_it_misses(
        self, tmp_path
    ):
        alone = tmp_path / "alone"
        alone.mkdir()
        copy = alone / "core_check.py"
        with open(SCRIPT, encoding="utf-8") as f:
            copy.write_text(f.read(), encoding="utf-8")
        done = subprocess.run(
            [sys.executable, str(copy), "--transcript", "x"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            cwd=str(tmp_path),
        )
        assert done.returncode == 2, (done.returncode, done.stderr)
        assert "Traceback" not in done.stderr, done.stderr
        assert "core.py" in done.stderr and "Nothing was read." in done.stderr


test_census = census_case(TARGET)
