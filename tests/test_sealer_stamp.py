"""`hooks/sealer-stamp.py`, one class per function.

Written anew from the code by #942's phase 6; the old cases of
`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` were read for
their inputs. `main` runs in the process: the payload is handed to it on
stdin and the message read from stdout. One opted-in repository is built for
the module, and each case takes a copy, so the values files a case writes
under the copy's git directory are its own. The values files are written by
`skills/verify/scripts/seal_stamp.py#write_values`, as the stamp's writers
write them. One case runs the hook through `hooks/dispatch.py stop`, as the
harness runs it at `Stop`.
"""

import io
import json
import os
import shutil
import subprocess
import sys

import pytest
from conftest import ROOT, census_case, git, load_hook_module, mark_root

TARGET = "hooks/sealer-stamp.py"

hook = load_hook_module("sealer-stamp.py", "sealer_stamp_under_test")
stamp = hook.load_stamp()

# A panel in the shape `broad_gate.panel` returns since #832. Neutral values.
ROWS = [
    ("SEALED", ""),
    ("tree", "aaa1111"),
    ("", "feat/x"),
    ("base", "bbb2222  origin/base"),
    ("item", "#12 · 1799000000"),
    None,
    ("suite", "✓ 3 passed"),
    ("ledger", "✓ 4 ok · 0 drifted · 0 broken"),
    ("chain", "✓ exit 0"),
    ("rounds", "2"),
]

# The label a values file in `values()`'s shape draws under (#666).
LABEL = (
    "SEALED feat/x @ aaa1111 against origin/base @ bbb2222 · #12 · 1799000000-an-item"
)

# A panel as long as a real run's (#717), and one in the shape a gate wrote
# from #666 to #717, which a pending file may still carry.
FULL_ROWS = [
    ("SEALED", ""),
    ("tree", "aaa1111a"),
    ("", "feat/12-the-branch-names-the-work-item..."),
    ("base", "bbb2222b  origin/release/v1.2.3"),
    ("item", "#12 · 1799000000"),
    ("gate", "tree 1.2.3"),
    None,
    ("suite", "✓ 6621 passed · 11 skipped"),
    ("ledger", "✓ 3451 ok · 0 drifted · 0 broken"),
    ("chain", "✓ exit 0"),
    ("CI also", "· 4 more steps"),
    ("rounds", "2"),
]
OLD_ROWS = [
    ("SEALED", ""),
    None,
    ("tree", "aaa1111a"),
    ("", "feat/12-the-branch-n..."),
    ("base", "bbb2222b"),
    ("", "origin/release/v1.2.3"),
    ("item", "#12 . 1799000000"),
    None,
    ("suite", "6621 passed, 11 skipped"),
    ("chain", "exit 0"),
    None,
    ("rounds", "2"),
]


def values(rows=ROWS, **changed):
    """A values file in the shape the writers write."""
    written = {
        "tree": "aaa1111",
        "base": "bbb2222",
        "from": "origin/base",
        "branch": "feat/x",
        "pr": "#12",
        "item": "/x/seal/threads/1799000000-an-item",
        "session": "s-1",
        "rows": rows,
    }
    written.update(changed)
    return written


def full_values(tree="aaa1111a"):
    """A values file as long as a real run's, label included."""
    name = "the-branch-names-the-work-item-it-carries"
    return values(
        rows=FULL_ROWS,
        tree=tree,
        base="bbb2222b",
        item=f"/x/seal/threads/1799000000-{name}",
        branch=f"feat/12-{name}",
        **{"from": "origin/release/v1.2.3"},
    )


def block(label, rows, disc=True):
    """One block of the message as `fitted` draws it."""
    return "\n".join([label, *stamp.stamp(rows, shape=False, disc=disc)])


@pytest.fixture(scope="module")
def _opted_in_template(tmp_path_factory):
    """A repository with `seal/` at its root and one commit, built once."""
    repo = tmp_path_factory.mktemp("stamp-world") / "repo"
    repo.mkdir()
    git(repo, "init", "-q", "-b", "main")
    mark_root(repo / "seal")
    (repo / "seal" / "config.md").write_text("# config\n", encoding="utf-8")
    git(repo, "add", "-A")
    git(
        repo,
        "-c",
        "user.name=e",
        "-c",
        "user.email=e@example.com",
        "commit",
        "-qm",
        "x",
    )
    return repo


@pytest.fixture
def repo(tmp_path, _opted_in_template):
    """This case's copy of the opted-in repository."""
    d = tmp_path / "repo"
    shutil.copytree(_opted_in_template, d)
    return d


def pending_for(repo, session="s-1", now=None, **kw):
    """One values file for SESSION under REPO's git directory; its path."""
    return stamp.write_values(str(repo / ".git"), session, values(**kw), now=now)


@pytest.fixture
def stop(monkeypatch, capsys):
    """`main` at the end of a turn in CWD: what it printed."""

    def run(cwd, session="s-1", **payload):
        body = {"hook_event_name": "Stop", "session_id": session, "cwd": str(cwd)}
        body.update(payload)
        text = body if isinstance(body, str) else json.dumps(body)
        monkeypatch.setattr(sys, "stdin", io.StringIO(text))
        hook.main()
        return capsys.readouterr().out

    return run


def message(stdout):
    """The `systemMessage` the hook printed."""
    return json.loads(stdout)["systemMessage"]


class Test_toplevel:
    def test_accepts_a_subdirectory_as_its_repository(self, repo):
        (repo / "docs" / "deep").mkdir(parents=True)
        assert hook.toplevel(str(repo / "docs" / "deep")) == str(repo)
        assert hook.toplevel(str(repo)) == str(repo)

    def test_refuses_a_directory_outside_any_repository(self, tmp_path):
        outside = tmp_path / "outside"
        outside.mkdir()
        assert hook.toplevel(str(outside)) == ""


class Test_load_stamp:
    def test_accepts_the_shipped_seal_stamp(self):
        assert hook.load_stamp().MESSAGE_BUDGET == stamp.MESSAGE_BUDGET

    @pytest.mark.parametrize(
        "body", ["raise SyntaxError('x')\n", "raise SystemExit(3)\n"]
    )
    def test_refuses_a_seal_stamp_whose_import_raises(
        self, tmp_path, monkeypatch, body
    ):
        broken = tmp_path / "seal_stamp.py"
        broken.write_text(body, encoding="utf-8")
        monkeypatch.setattr(hook, "STAMP", str(broken))
        assert hook.load_stamp() is None


class Test_drawings:
    def test_accepts_the_oldest_file_first_and_claims_what_it_draws(self, repo):
        second = pending_for(repo, now=2, item="/x/seal/threads/1799000001-another")
        first = pending_for(repo, now=1)
        directory = os.path.dirname(first)
        drawn = []
        while stamp.pending(directory):
            blocks = hook.drawings(stamp, directory)
            assert blocks, "a pending file drew nothing"
            drawn += [label for label, _rows in blocks]
        assert drawn == [
            LABEL,
            LABEL.replace("1799000000-an-item", "1799000001-another"),
        ]
        assert os.path.exists(stamp.drawn_path(first))
        assert os.path.exists(stamp.drawn_path(second))

    def test_accepts_a_file_an_older_gate_wrote(self, repo):
        """A `scale` a gate before #853 wrote is read as nothing, and the rows
        a gate wrote from #666 to #717 are drawn as they stand (#832)."""
        old = {**full_values(), "rows": OLD_ROWS, "scale": 0.9}
        path = stamp.write_values(str(repo / ".git"), "s-1", old)
        blocks = hook.drawings(stamp, os.path.dirname(path))
        assert blocks == [(stamp.label(old), OLD_ROWS)]

    @pytest.mark.parametrize(
        "bad",
        ["not json", {"item": 5}, {"rows": [["SEALED"]]}],
        ids=["not-json", "an-item-that-is-no-string", "a-row-that-does-not-draw"],
    )
    def test_refuses_to_claim_a_file_that_is_no_stamps_values(self, repo, bad):
        """Round 1's yellow 2: every block is built whole before its file is
        claimed, so a bad file after a good one is left where it is and takes
        nothing down."""
        good = pending_for(repo, now=1)
        directory = os.path.dirname(good)
        bad_path = os.path.join(directory, "2-bad.json")
        with open(bad_path, "w", encoding="utf-8") as handle:
            handle.write(
                bad if isinstance(bad, str) else json.dumps({**values(), **bad})
            )
        assert hook.drawings(stamp, directory) == [(LABEL, ROWS)]
        assert stamp.pending(directory) == [bad_path]

    def test_refuses_to_claim_a_file_that_reads_and_labels_but_does_not_draw(
        self, repo
    ):
        """Every file the shipped `seal_stamp` reads also draws, so the draw
        before the claim is faked to fail for one file's rows, to remove that
        guarantee (contract rule 13; #1017, round 3's s4). The file is the
        older one, so a message carrying one seal would carry it. It is left
        pending, and the good one after it is drawn."""
        undrawable = [("tree", "does not draw")]

        class Undrawable:
            def __getattr__(self, name):
                return getattr(stamp, name)

            def stamp(self, rows, shape=False, disc=True):
                if list(rows) == undrawable:
                    raise ValueError("these rows do not draw")
                return stamp.stamp(rows, shape=shape, disc=disc)

        bad = pending_for(repo, now=1, rows=undrawable)
        good = pending_for(repo, now=2)
        directory = os.path.dirname(good)
        assert hook.drawings(Undrawable(), directory) == [(LABEL, ROWS)]
        assert stamp.pending(directory) == [bad]

    def test_refuses_to_claim_what_one_message_does_not_carry(self, repo):
        """The owner's rule of 2026-10-02: a pair that does not fit one message
        with its discs draws the oldest, and the next stays pending."""
        rows = list(FULL_ROWS)
        late = full_values("ccc3333c")
        while len(block(stamp.label(full_values()), FULL_ROWS)) + 2 + len(
            block(stamp.label(late), rows)
        ) <= (stamp.MESSAGE_BUDGET):
            rows.append(("", f"home-{len(rows)}"))
        first = stamp.write_values(str(repo / ".git"), "s-1", full_values(), now=1)
        second = stamp.write_values(
            str(repo / ".git"), "s-1", {**late, "rows": rows}, now=2
        )
        blocks = hook.drawings(stamp, os.path.dirname(first))
        assert blocks == [(stamp.label(full_values()), FULL_ROWS)]
        assert stamp.pending(os.path.dirname(first)) == [second]


class Test_main:
    @pytest.mark.rule("stamp-drawn-once")
    def test_accepts_the_main_sessions_stop_and_draws_once(self, repo, stop):
        """S3 and S4: one JSON object whose `systemMessage` is `fitted`'s
        message, the label on its first line and the drawing with its disc
        under it; the file is claimed, and the next `Stop` prints nothing."""
        path = pending_for(repo)
        text = message(stop(repo))
        assert text == stamp.fitted([(LABEL, ROWS)])
        assert text == block(LABEL, ROWS), "drawn without its disc"
        assert "\x1b[38;2;" in text, "the drawing lost colour"
        assert os.path.exists(stamp.drawn_path(path)) and not os.path.exists(path)
        assert stop(repo) == ""

    def test_accepts_a_turn_ending_in_a_subdirectory_or_a_linked_worktree(
        self, repo, stop, tmp_path
    ):
        """The `cwd` is wherever the session last stood, and the file lives
        under the COMMON dir, so a subdirectory and a linked worktree of the
        clone both find it."""
        (repo / "docs" / "deep").mkdir(parents=True)
        pending_for(repo)
        assert message(stop(repo / "docs" / "deep")).startswith(LABEL)
        tree = tmp_path / "tree"
        git(repo, "worktree", "add", "-q", str(tree))
        pending_for(repo, item="/x/seal/threads/1799000001-another")
        assert message(stop(tree)).split("\n", 1)[0].endswith("1799000001-another")

    @pytest.mark.parametrize(
        "payload",
        [
            {"agent_id": "a-1", "agent_type": "specseal:sealer"},
            {"hook_event_name": "SubagentStop", "agent_id": "a-1"},
            {"hook_event_name": "SubagentStop"},
            {"session_id": "s-x"},
            {"session_id": ""},
        ],
        ids=[
            "a-subagents-stop",
            "subagent-stop",
            "another-event",
            "another-session",
            "no-session",
        ],
    )
    @pytest.mark.rule("stamp-drawn-once")
    def test_refuses_any_end_but_its_own_sessions_stop(self, repo, stop, payload):
        """S5 and S6: a subagent's end carries the parent's session and
        differs by `agent_id` alone, so it draws nothing; nor does another
        event or another session's `Stop`. The file stays."""
        path = pending_for(repo)
        payload = dict(payload)
        session = payload.pop("session_id", "s-1")
        assert stop(repo, session=session, **payload) == ""
        assert stamp.pending(os.path.dirname(path)) == [path]

    def test_refuses_a_stop_with_no_session_where_a_file_waits_for_none(
        self, repo, stop
    ):
        """A values file written with no session waits in the `none`
        directory, which is also where a `Stop` with no session id would look.
        Such a `Stop` belongs to no session, so it draws nothing and the file
        stays (#1017, round 3's s8)."""
        path = pending_for(repo, session=None)
        assert stop(repo, session=None) == ""
        assert stamp.pending(os.path.dirname(path)) == [path]

    def test_refuses_a_repository_that_never_opted_in(self, repo, stop):
        shutil.rmtree(repo / "seal")
        path = pending_for(repo)
        assert stop(repo) == ""
        assert os.path.exists(path), "a file was taken in a repository not opted in"

    def test_refuses_a_cwd_outside_any_repository(self, stop, tmp_path, monkeypatch):
        outside = tmp_path / "outside"
        outside.mkdir()
        monkeypatch.setattr(hook, "load_stamp", lambda: pytest.fail("loaded"))
        assert stop(outside) == ""

    @pytest.mark.parametrize("text", ["not json", "[]"], ids=["not-json", "a-list"])
    def test_refuses_a_payload_that_is_no_object(self, text, monkeypatch, capsys):
        monkeypatch.setattr(sys, "stdin", io.StringIO(text))
        hook.main()
        assert capsys.readouterr().out == ""

    def test_refuses_to_draw_where_seal_stamp_will_not_load(
        self, repo, stop, monkeypatch
    ):
        """A `python3` that cannot load `seal_stamp.py` draws nothing, and the
        file stays for `seal-stamp --from`."""
        path = pending_for(repo)
        monkeypatch.setattr(hook, "load_stamp", lambda: None)
        assert stop(repo) == ""
        assert os.path.exists(path)

    def test_refuses_an_empty_directory_before_it_reads_the_opt_in(
        self, repo, stop, monkeypatch
    ):
        """The hook fires at the end of every turn, so a session with nothing
        pending returns before the opt-in is read."""
        monkeypatch.setattr(hook.optin, "opted_in", lambda top: pytest.fail("read"))
        assert stop(repo) == ""

    def test_accepts_one_seal_too_large_for_its_disc_drawn_alone_without_it(
        self, repo, stop
    ):
        """A4's last rung: a stamp that does not fit the budget with its disc
        by itself is drawn alone, with no disc, and the next waits."""
        label = stamp.label(full_values())
        homes = []
        while len(block(label, FULL_ROWS + homes)) <= stamp.MESSAGE_BUDGET:
            homes.append(("", f"home-{len(homes)}"))
        big = {**full_values(), "rows": FULL_ROWS + homes}
        stamp.write_values(str(repo / ".git"), "s-1", big, now=1)
        after = stamp.write_values(
            str(repo / ".git"), "s-1", full_values("ccc3333c"), now=2
        )
        text = message(stop(repo))
        assert text == block(label, big["rows"], disc=False)
        assert os.path.exists(after)
        later = message(stop(repo))
        assert later == block(stamp.label(full_values("ccc3333c")), FULL_ROWS)
        assert len(later) <= stamp.MESSAGE_BUDGET


class Test_module:
    def test_the_hook_is_registered_for_stop_and_nothing_else(self):
        """`hooks.json` runs the `stop` group at `Stop`, and the group holds
        this hook alone. Registered at `SubagentStop` it would draw inside the
        sealer."""
        with open(
            os.path.join(ROOT, "hooks", "hooks.json"), encoding="utf-8"
        ) as handle:
            events = json.load(handle)["hooks"]
        commands = [h["command"] for group in events["Stop"] for h in group["hooks"]]
        assert commands and all(c.split()[-1] == "stop" for c in commands), commands
        assert "SubagentStop" not in events
        dispatch = load_hook_module("dispatch.py", "dispatch_for_the_stop_group")
        assert dispatch.GROUPS["stop"] == ("sealer-stamp.py",)

    @pytest.mark.rule("stamp-drawn-once")
    def test_the_stop_group_draws_through_the_dispatcher(self, repo):
        """The hook as the harness runs it: `dispatch.py stop` with the payload
        on stdin prints the message, and a second `Stop` prints nothing."""

        def dispatched():
            body = {"hook_event_name": "Stop", "session_id": "s-1", "cwd": str(repo)}
            done = subprocess.run(
                [sys.executable, os.path.join(ROOT, "hooks", "dispatch.py"), "stop"],
                input=json.dumps(body),
                capture_output=True,
                encoding="utf-8",
                errors="replace",
                timeout=60,
            )
            assert done.returncode == 0, done.stderr
            return done.stdout

        pending_for(repo)
        assert message(dispatched()) == stamp.fitted([(LABEL, ROWS)])
        assert dispatched() == ""


test_census = census_case(TARGET)
