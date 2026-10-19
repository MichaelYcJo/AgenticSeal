"""The broad gate's stamp reaches the person it is drawn for (#400).

Work item 1790562543. A sealer's stdout was a pipe into a report that arrived
folded behind `ctrl+o`, so a stamp drawn there was never seen. The gate now
draws only on a terminal; a recorded seal on a pipe writes its panel to a
values file under the git common dir, and a `Stop` hook in the session that
ran the gate (since #969 the orchestrator's) draws each undrawn file once,
after that turn's text.

This module holds the stamp's half — the values file, `seal-stamp --from`,
the scale #853 retired. The gate's half is in
`tests/test_the_seal_is_taken_once_by_the_sealer.py`, beside the fixtures
that drive a real gate over a settled work item.
"""

import importlib.util
import inspect
import json
import os
import subprocess
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
STAMP = os.path.join(ROOT, "skills", "verify", "scripts", "seal_stamp.py")
GATE = os.path.join(ROOT, "skills", "verify", "scripts", "broad_gate.py")

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


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def stamp_module():
    return _load("specseal_seal_stamp_for_its_values", STAMP)


NO_SCALE = object()


def values(scale=NO_SCALE, item="/x/seal/specs/1799000000-an-item", rows=ROWS):
    """A values file in the shape the gate writes: since #853 with no
    `scale`, or with the one a gate before #853 wrote where `scale` is
    given."""
    written = {
        "tree": "aaa1111",
        "base": "bbb2222",
        "from": "origin/base",
        "branch": "feat/x",
        "pr": "#12",
        "item": item,
        "session": "s-1",
        "rows": rows,
    }
    if scale is not NO_SCALE:
        written["scale"] = scale
    return written


# The label a values file in `values()`'s shape draws under (#666): the
# `SEALED` line's own names, the pull request, the work item.
LABEL = (
    "SEALED feat/x @ aaa1111 against origin/base @ bbb2222 · #12 · 1799000000-an-item"
)


def test_a_values_file_from_an_older_gate_draws_the_label_it_always_drew():
    """A15's compatibility half. A file with no `branch` key was written by
    a gate older than #666, and may still be pending when a newer hook draws
    it, so it gets the label it always got. `branch` present and `null` is a
    detached HEAD, which is the new shape with the branch left out; no `pr`
    leaves the pull request out."""
    mod = stamp_module()
    old = {k: v for k, v in values().items() if k not in ("branch", "pr")}
    assert mod.label(old) == "SEALED aaa1111 against bbb2222 · 1799000000-an-item"
    assert mod.label({**values(), "branch": None, "pr": None}) == (
        "SEALED aaa1111 against origin/base @ bbb2222 · 1799000000-an-item"
    )


def seal_stamp(*args):
    """`seal_stamp.py` as a person types it, stdout a pipe."""
    return subprocess.run(
        [sys.executable, STAMP, *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=60,
    )


# --- S11: a values file drawn by hand, once --------------------------------


def test_a_values_file_is_drawn_by_hand_once_and_then_refused(tmp_path):
    """S11. `seal-stamp --from <file>` draws that run's rows — not the
    sample — and marks the file drawn. The same command again refuses with
    one sentence and exit 2, because a sealed run's values are drawn once
    whoever draws them."""
    mod = stamp_module()
    path = mod.write_values(str(tmp_path), "s-1", values())
    out = seal_stamp("--from", path)
    assert out.returncode == 0, out.stderr
    assert out.stdout == "\n" + "\n".join(mod.stamp(ROWS, shape=True)) + "\n\n"
    assert "aaa1111" in out.stdout and "c46fd2d" not in out.stdout, (
        "the drawing is the sample's, not the run's"
    )
    assert not os.path.exists(path), "the file was drawn and not marked drawn"
    assert os.path.exists(mod.drawn_path(path)), "the drawn file's values are gone"

    again = seal_stamp("--from", path)
    assert again.returncode == 2, again.stdout + again.stderr
    assert again.stdout == "", f"something was drawn a second time:\n{again.stdout}"
    refusal = again.stderr.strip()
    assert "was drawn already" in refusal and "\n" not in refusal, refusal
    assert seal_stamp("--from", mod.drawn_path(path)).returncode == 2, (
        "the drawn file itself can be drawn again by naming it"
    )


def test_the_drawn_refusal_names_the_file_the_values_are_in(tmp_path):
    """Round 1's 🟡 3. Naming the drawn file itself was refused — rightly —
    with a sentence saying the values stay in `X.drawn.drawn.json`, which does
    not exist, on the one path a person has to recover them from. The file
    the refusal says holds the values exists, whichever name was given."""
    mod = stamp_module()
    path = mod.write_values(str(tmp_path), "s-1", values())
    assert seal_stamp("--from", path).returncode == 0
    drawn = mod.drawn_path(path)
    for given in (path, drawn):
        out = seal_stamp("--from", given)
        assert out.returncode == 2, out.stdout + out.stderr
        assert f"the values stay in {drawn}." in out.stderr, out.stderr
        assert ".drawn.drawn.json" not in out.stderr, out.stderr


def test_a_file_that_is_not_a_run_is_refused_and_left_for_a_repair(tmp_path):
    """A values file that is not in the gate's shape is refused before it is
    claimed, so it is still there to be drawn once somebody repairs it."""
    for broken, said in (
        ("not json", "it is not JSON"),
        (json.dumps({**values(), "rows": "SEALED"}), "`rows` is not a list"),
    ):
        path = tmp_path / "1-aaa1111.json"
        path.write_text(broken, encoding="utf-8")
        out = seal_stamp("--from", str(path))
        assert out.returncode == 2, (broken, out.stdout, out.stderr)
        assert said in out.stderr, out.stderr
        assert out.stdout == "", out.stdout
        assert path.exists(), f"a refused file was claimed: {broken!r}"


@pytest.mark.parametrize(
    "scale",
    [NO_SCALE, 0.9, 0.5, "large", None],
    ids=["none", "an-older-gates-0.90", "under-the-old-floor", "a-word", "null"],
)
def test_a_values_file_draws_whatever_scale_it_carries(tmp_path, scale):
    """S13 (#853). The gate writes no `scale` since #853, and a file a gate
    before it wrote carries one; both draw the same stamp, and a `scale`
    the old band would have refused, or that is no number, is read as
    nothing too — the stamp has one size, so the key decides nothing."""
    mod = stamp_module()
    path = mod.write_values(str(tmp_path), "s-1", values(scale=scale))
    assert mod.read_values(path)["rows"] == [
        None if row is None else tuple(row) for row in ROWS
    ]
    out = seal_stamp("--from", path)
    assert out.returncode == 0, out.stderr
    assert out.stdout == "\n" + "\n".join(mod.stamp(ROWS, shape=True)) + "\n\n"


def test_pending_lists_the_undrawn_oldest_first_and_claim_takes_one_once(tmp_path):
    """The reader the hook uses. `pending` lists undrawn files oldest first
    and skips drawn ones and the writer's hidden temporary; `claim` renames a
    file to its drawn name and answers None to the second caller, which is
    what keeps two drawers racing for one file to one drawing."""
    mod = stamp_module()
    older = mod.write_values(str(tmp_path), "s-1", values(), now=1)
    newer = mod.write_values(str(tmp_path), "s-1", values(), now=2)
    directory = mod.values_dir(str(tmp_path), "s-1")
    open(os.path.join(directory, ".3-aaa1111.tmp"), "w", encoding="utf-8").close()
    assert mod.pending(directory) == [older, newer]
    assert mod.claim(older) == mod.drawn_path(older)
    assert mod.claim(older) is None, "a claimed file was claimed a second time"
    assert mod.pending(directory) == [newer]
    assert mod.pending(str(tmp_path / "nowhere")) == []


def test_a_session_id_cannot_name_a_directory_outside_the_values_dir(tmp_path):
    """The session id names a directory, so a separator in a malformed one
    must not become a path escape, and an absent one lands under `none/`."""
    mod = stamp_module()
    assert mod.session_key("../../elsewhere") == "elsewhere"
    for absent in (None, "", "  ", ".", ".."):
        assert mod.session_key(absent) == mod.NO_SESSION, absent
    path = mod.write_values(str(tmp_path), "../../elsewhere", values())
    assert os.path.dirname(path) == os.path.join(
        str(tmp_path), mod.VALUES_DIR, "elsewhere"
    ), path


# --- S3-S6: the hook draws at the main session's `Stop`, once ---------------

DISPATCH = os.path.join(ROOT, "hooks", "dispatch.py")


def git(repo, *args):
    """git driven from Python, so no Bash line carries a commit (§8)."""
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        check=True,
    )


def opted_in(tmp_path, name="repo"):
    """A repository with `seal/` at its root and one commit, so a linked
    worktree can be added to it."""
    repo = tmp_path / name
    repo.mkdir()
    git(repo, "init", "-q", "-b", "main")
    (repo / "seal").mkdir()
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


def pending_for(repo, session, **kw):
    """One values file for `session` in `repo`'s common dir; its path."""
    return stamp_module().write_values(str(repo / ".git"), session, values(**kw))


def stop(cwd, session="s-1", **payload):
    """`dispatch.py stop` as the harness runs it: the payload on stdin, and
    what it printed."""
    body = {"hook_event_name": "Stop", "session_id": session, "cwd": str(cwd)}
    body.update(payload)
    r = subprocess.run(
        [sys.executable, DISPATCH, "stop"],
        input=json.dumps(body),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=60,
    )
    assert r.returncode == 0, r.stderr
    return r.stdout


def message(stdout):
    """The `systemMessage` the hook printed, as lines."""
    return json.loads(stdout)["systemMessage"].split("\n")


def drawn(mod, label, rows, disc=True):
    """One block of the hook's message as `fitted` draws it: the label, then
    the block form. `disc` False is the rung with no disc (#853)."""
    return "\n".join([label, *mod.stamp(rows, shape=False, disc=disc)])


def test_the_main_sessions_stop_draws_each_undrawn_file_once(tmp_path):
    """S3 and S4. The main session's `Stop` — `session_id` X, no `agent_id` —
    prints one JSON object whose `systemMessage` opens with a label naming
    what was sealed and then draws the block form of the file's rows with
    its disc, colour sequences and all. The file is marked drawn, so the
    next `Stop` of the same session prints nothing.

    #717's A15: the bytes are compared with the message `fitted` holds under
    the budget, not with the file drawn whatever its size — and at `ROWS`'
    size that message IS the file's drawing with its disc, so the step-down
    is asserted not to have fired here rather than assumed."""
    mod = stamp_module()
    repo = opted_in(tmp_path)
    path = pending_for(repo, "s-1")
    lines = message(stop(repo))
    assert lines[0] == LABEL, lines[0]
    assert "\n".join(lines) == mod.fitted([(LABEL, ROWS)]), "not the fitted form"
    assert lines[1:] == mod.stamp(ROWS, shape=False), "not the file's block form"
    assert any("\x1b[38;2;" in line for line in lines[1:]), "the drawing lost colour"
    assert not os.path.exists(path) and os.path.exists(mod.drawn_path(path))
    assert stop(repo) == "", "a drawn file was drawn a second time"


def test_a_subagents_end_draws_nothing_and_leaves_the_file(tmp_path):
    """S5. `SubagentStop` carries the parent's `session_id` and differs by
    `agent_id` alone (`questions.md` Q2), so a payload naming an agent is the
    sealer's own end — or any subagent's — and draws nothing; so does any
    event that is not `Stop`. The file stays for the main session."""
    mod = stamp_module()
    repo = opted_in(tmp_path)
    path = pending_for(repo, "s-1")
    assert stop(repo, agent_id="a-1", agent_type="specseal:sealer") == ""
    assert stop(repo, hook_event_name="SubagentStop", agent_id="a-1") == ""
    assert stop(repo, hook_event_name="SubagentStop") == ""
    assert mod.pending(os.path.dirname(path)) == [path], "the file was taken"


def test_another_sessions_stop_leaves_its_file_alone(tmp_path):
    """S6. A concurrent session of the same clone ends its turn: its own
    directory is empty, so it prints nothing and takes nothing, and session
    Y's file is still there for Y."""
    mod = stamp_module()
    repo = opted_in(tmp_path)
    path = pending_for(repo, "s-y")
    assert stop(repo, session="s-x") == ""
    assert mod.pending(os.path.dirname(path)) == [path]


# The smallest panel a run could carry. Whether two of its stamps share one
# message is the disc's mark's to say, not this module's: under #717's lily
# they did; under phase 2's § of #832 they did not; under the owner's 14-cell
# disc they did again; under the S of 2026-10-07 they do not, and under the
# archived key they do (`phases/phase-6.md` of work item 1791270164 and round
# 1's report there have the sizes). A case that needs a pair over the budget
# grows this panel until it is.
SMALL_ROWS = [("SEALED", ""), ("tree", "aaa1111"), ("", "feat/x"), ("rounds", "2")]


def test_several_files_come_out_one_stop_each_oldest_first(tmp_path):
    """Several pending seals come out one `Stop` at a time, oldest first,
    each stamp whole under its own label and with its disc, and a file that
    is not a stamp's values is skipped and left where it is rather than taking
    the others down.

    Phase 2's name for #717's case. The pair has to be over the budget
    together for the newer to wait for the next `Stop` rather than share the
    message, and whether a small pair is depends on the disc's mark, which
    #857 replaces by changing `seal-mark.txt` alone. So the panel is grown
    by deferral homes, one at a time, until the pair does not fit — none
    under the S, some under the archived key — and the premise is asserted
    rather than assumed (round 1's 🟡 3)."""
    mod = stamp_module()
    repo = opted_in(tmp_path)
    other = LABEL.replace("aaa1111", "ccc3333")
    rows = list(SMALL_ROWS)
    while sum(len(drawn(mod, who, rows)) for who in (LABEL, other)) + 2 <= (
        mod.MESSAGE_BUDGET
    ):
        rows.append(("", f"home-{len(rows)}"))
    small = values(rows=rows)
    first = mod.write_values(str(repo / ".git"), "s-1", small, now=1)
    second = mod.write_values(
        str(repo / ".git"), "s-1", {**small, "tree": "ccc3333"}, now=2
    )
    broken = os.path.join(os.path.dirname(first), "3-ddd4444.json")
    with open(broken, "w", encoding="utf-8") as handle:
        handle.write("not json")
    older, newer = (drawn(mod, who, rows) for who in (LABEL, other))
    assert len(older) + 2 + len(newer) > mod.MESSAGE_BUDGET, (
        "the grown pair shares one message; this case's premise moved"
    )
    assert len(older) <= mod.MESSAGE_BUDGET, "the grown stamp lost its disc alone"
    assert json.loads(stop(repo))["systemMessage"] == older
    assert not os.path.exists(first) and os.path.exists(second)
    assert json.loads(stop(repo))["systemMessage"] == newer
    assert all("\x1b[38;2;" in block for block in (older, newer)), "a disc was lost"
    assert not os.path.exists(second)
    assert mod.pending(os.path.dirname(first)) == [broken]
    assert stop(repo) == "", "the broken file was drawn"


def test_a_malformed_later_file_does_not_take_the_earlier_ones(tmp_path):
    """Round 1's 🟡 2. `drawings` claimed a file and only then built its
    label, and `label` raises `TypeError` on an `item` that is not a string —
    outside the guarded read, so the exception left the good file before it
    claimed and never printed, and `--from` then refused it as drawn. Every
    block is built whole before its file is claimed now: the good file is
    drawn, and the bad one stays pending under its own name."""
    mod = stamp_module()
    repo = opted_in(tmp_path)
    good = mod.write_values(str(repo / ".git"), "s-1", values(), now=1)
    bad = mod.write_values(str(repo / ".git"), "s-1", {**values(), "item": 5}, now=2)
    lines = message(stop(repo))
    assert lines[0] == LABEL, lines
    assert "\n".join(lines) == mod.fitted([(LABEL, ROWS)])
    assert os.path.exists(mod.drawn_path(good)) and not os.path.exists(good)
    assert os.path.exists(bad), "the malformed file was claimed"
    assert not os.path.exists(mod.drawn_path(bad))


def test_a_file_an_older_gate_wrote_with_its_scale_is_drawn_by_the_hook(tmp_path):
    """S13 (#853). A values file a gate before #853 wrote carries `"scale":
    0.9`, and one written since carries none; the hook draws both, oldest
    first, the same stamp under each label — the key decides nothing, so a
    file left pending across the update is not left behind by it."""
    mod = stamp_module()
    repo = opted_in(tmp_path)
    old = mod.write_values(str(repo / ".git"), "s-1", values(scale=0.9), now=1)
    new = mod.write_values(str(repo / ".git"), "s-1", values(), now=2)
    assert "\n".join(message(stop(repo))) == mod.fitted([(LABEL, ROWS)])
    assert os.path.exists(mod.drawn_path(old)) and os.path.exists(new)
    assert "\n".join(message(stop(repo))) == mod.fitted([(LABEL, ROWS)])
    assert os.path.exists(mod.drawn_path(new))


def test_the_sealers_worktree_and_the_main_checkout_share_the_file(tmp_path):
    """The sealer's root is a linked worktree while the main session's `cwd`
    is the checkout (Q2's reading: the `Stop` payload's `cwd` was the main
    checkout). The file lives under the COMMON dir, so a `Stop` from either
    tree finds it — a file written through the worktree is drawn from the
    main checkout, and one written there is drawn from inside the worktree."""
    repo = opted_in(tmp_path)
    tree = tmp_path / "tree"
    git(repo, "worktree", "add", "-q", str(tree))
    common = git(tree, "rev-parse", "--git-common-dir").stdout.strip()
    common = os.path.normpath(os.path.join(str(tree), common))
    assert common == os.path.normpath(str(repo / ".git")), common
    stamp_module().write_values(common, "s-1", values())
    assert message(stop(repo))[0].startswith("SEALED feat/x @ aaa1111"), (
        "not from the checkout"
    )
    pending_for(repo, "s-1", item="/x/seal/specs/1799000001-another")
    assert message(stop(tree))[0].endswith("1799000001-another"), "not from the tree"


def test_a_turn_ending_in_a_subdirectory_still_draws(tmp_path):
    """The payload's `cwd` is wherever the session last stood, which need not
    be the repository's root. The hook walks up to the `.git` entry rather
    than asking git, so a turn ending in a subdirectory draws the same."""
    repo = opted_in(tmp_path)
    (repo / "docs" / "deep").mkdir(parents=True)
    pending_for(repo, "s-1")
    assert message(stop(repo / "docs" / "deep"))[0].startswith(
        "SEALED feat/x @ aaa1111"
    )


def test_a_repository_that_never_opted_in_is_not_drawn_for(tmp_path):
    """No `seal/` at either place, and the hook stays silent and takes
    nothing — even over a file that is there."""
    repo = opted_in(tmp_path)
    for name in os.listdir(repo / "seal"):
        os.remove(repo / "seal" / name)
    os.rmdir(repo / "seal")
    path = pending_for(repo, "s-1")
    assert stop(repo) == ""
    assert os.path.exists(path), "a file was taken in a repository not opted in"


def test_the_stop_group_reports_the_stop_event(monkeypatch, capsys):
    """`dispatch.main` names the event on its decision path, and named every
    group that is not `pre-` as `PostToolUse`. The `stop` group answers
    `Stop`, so a decision coming out of it, should one ever do, says so."""
    dispatch = _load("specseal_dispatch_for_the_stop_group", DISPATCH)
    decision = json.dumps(
        {
            "hookSpecificOutput": {
                "permissionDecision": "ask",
                "permissionDecisionReason": "r",
            }
        }
    )
    monkeypatch.setattr(dispatch, "run_gate", lambda _gate, _payload: decision)
    monkeypatch.setattr(sys, "argv", ["dispatch.py", "stop"])
    monkeypatch.setattr(sys, "stdin", __import__("io").StringIO("{}"))
    dispatch.main()
    said = json.loads(capsys.readouterr().out)
    assert said["hookSpecificOutput"]["hookEventName"] == "Stop", said


def test_the_hook_is_registered_for_stop_and_nothing_else():
    """`hooks.json` runs the `stop` group at `Stop`, and `dispatch.GROUPS`
    holds the hook there. Registered at `SubagentStop` it would draw inside
    the sealer, where the whole work item began."""
    with open(os.path.join(ROOT, "hooks", "hooks.json"), encoding="utf-8") as handle:
        events = json.load(handle)["hooks"]
    commands = [h["command"] for group in events["Stop"] for h in group["hooks"]]
    assert commands and all(c.split()[-1] == "stop" for c in commands), commands
    assert "SubagentStop" not in events
    dispatch = _load("specseal_dispatch_for_its_groups", DISPATCH)
    assert dispatch.GROUPS["stop"] == ("sealer-stamp.py",)


# --- #975 S4-S9: the stamp is queued at the commit of a `sealed` guarantee ----
#
# The owner's rule of 2026-10-18: the stamp means every party verified the
# work item, the sealer last, and the work is done, so it is drawn once per
# work item from the sealer's `sealed` and never from the broad gate's run.
# git's `post-commit`, which already runs after every judged commit in the
# worktree the commit landed in, reads the committed `guarantee.md` and queues
# one values file for the session; the `Stop` hook above draws it.

HOOKS_DIR = os.path.join(ROOT, "hooks")
ITEM_NAME = "1799000000-an-item"
ITEM_ID = "1799000000"


def commitgate_module():
    """`hooks/commitgate.py`, which imports its siblings by their plain
    names, as `hooks/git/post-commit.py` puts them on the path."""
    if HOOKS_DIR not in sys.path:
        sys.path.insert(0, HOOKS_DIR)
    return _load(
        "specseal_commitgate_for_the_stamp", os.path.join(HOOKS_DIR, "commitgate.py")
    )


def commit_all(repo, message):
    """Everything in `repo` committed, driven from Python (§8)."""
    git(repo, "add", "-A")
    git(
        repo,
        "-c",
        "user.name=e",
        "-c",
        "user.email=e@example.com",
        "commit",
        "-qm",
        message,
    )


def guarantee_text(target, base, verdict, earlier=""):
    """A `guarantee.md` in `templates/sdd-guarantee.md`'s shape: its `Target
    SHA` row, with `earlier` after it, and one `Verdict:` line."""
    return (
        "# an item — guarantee\n\n| Field | Value |\n|---|---|\n"
        f"| Target SHA | {target} against {base}{earlier} |\n"
        f"| Broad gate | {target} against {base} |\n\nVerdict: {verdict}\n"
    )


def guaranteed(tmp_path, verdict="sealed", earlier="", branch="feat/x"):
    """An opted-in repository on `branch` whose work item carries two round
    records, then one commit adding its closing records — `broad-gate.md`
    naming the commit before it, and `guarantee.md` reading `verdict` over
    that commit. Returns (repo, target, base)."""
    repo = opted_in(tmp_path)
    git(repo, "switch", "-qc", branch)
    item = repo / "seal" / "specs" / ITEM_NAME
    (item / "rounds").mkdir(parents=True)
    for n in (1, 2):
        (item / "rounds" / f"round-{n}.md").write_text("x\n", encoding="utf-8")
    commit_all(repo, "the rounds")
    target = git(repo, "rev-parse", "--short", "HEAD").stdout.strip()
    base = git(repo, "rev-parse", "--short", "main").stdout.strip()
    (item / "broad-gate.md").write_text(
        f"| Field | Value |\n|---|---|\n| Broad gate | {target} against {base} |\n",
        encoding="utf-8",
    )
    (item / "guarantee.md").write_text(
        guarantee_text(target, base, verdict, earlier), encoding="utf-8"
    )
    commit_all(repo, "the closing records")
    return repo, target, base


def after_the_commit(repo, session="s-1"):
    """What `post-commit` printed in `repo` for a Claude session."""
    import io

    out = io.StringIO()
    environ = {"CLAUDE_CODE_SESSION_ID": session}
    assert commitgate_module().post_commit(str(repo), environ, out) == 0
    return out.getvalue()


def queued(repo):
    """Every values file under `repo`'s git common dir, drawn or not."""
    found = []
    for directory, _dirs, names in os.walk(repo / ".git" / "specseal-stamp"):
        found += [os.path.join(directory, n) for n in names if n.endswith(".json")]
    return sorted(found)


def test_a_sealed_guarantees_commit_queues_one_stamp(tmp_path):
    """#975 S4. The commit adds `guarantee.md` reading `sealed` over a
    `Target SHA` with no earlier run, so `post-commit` writes one values
    file for the session, named by the work item's id and the audited
    commit, and prints one line naming it and `seal-stamp --from`. The
    main session's `Stop` then draws it once, labelled with what was
    sealed. Red at `ddb5cf1a`: the hook queued nothing.

    Under a directory whose name holds a space, so the command the line
    names is quoted for the shell a person types it into."""
    mod = stamp_module()
    spaced = tmp_path / "a checkout"
    spaced.mkdir()
    repo, target, base = guaranteed(spaced)
    said = after_the_commit(repo)
    (path,) = queued(repo)
    assert " " in path and f"--from {path}`" not in said, said
    assert os.path.dirname(path) == str(repo / ".git" / "specseal-stamp" / "s-1")
    assert os.path.basename(path).endswith(f"-{ITEM_ID}-{target}.json"), path
    assert said == (
        f"specseal: the stamp for {ITEM_ID} is drawn at the end of this turn "
        f"from {path}; where none appears, `seal-stamp --from {mod.quote(path)}` "
        "draws it\n"
    ), said
    lines = message(stop(repo))
    assert lines[0] == f"SEALED feat/x @ {target} against {base} · {ITEM_NAME}", lines
    assert stop(repo) == "", "the stamp was drawn twice"


@pytest.mark.parametrize(
    "verdict",
    ["withheld — the README is stale", "undecided — does #12 ask for the flag?"],
)
def test_a_withheld_or_undecided_guarantee_queues_nothing(tmp_path, verdict):
    """#975 S5. The finished-work stamp is not drawn over unfinished work:
    a committed guarantee that does not read `sealed` queues nothing and
    says nothing about a stamp. Nor does a later commit that does not touch
    the guarantee."""
    repo, _target, _base = guaranteed(tmp_path, verdict=verdict)
    assert after_the_commit(repo) == ""
    (repo / "README.md").write_text("x\n", encoding="utf-8")
    commit_all(repo, "something else")
    assert after_the_commit(repo) == ""
    assert queued(repo) == []


def test_a_reseal_after_withheld_queues_the_stamp(tmp_path):
    """#975 S6. The sealer withheld at one commit, the work was fixed, and
    the sealer's second run reads `sealed`, keeping the earlier verdict on
    the row: that commit draws the stamp."""
    repo, target, _base = guaranteed(
        tmp_path, earlier="; earlier run: abc1234 withheld — the README is stale"
    )
    assert after_the_commit(repo)
    (path,) = queued(repo)
    assert path.endswith(f"-{ITEM_ID}-{target}.json"), path


def test_a_second_sealed_verdict_queues_nothing(tmp_path):
    """#975 S7. A work item is stamped once: a guarantee whose `Target SHA`
    row carries an earlier run reading `sealed` was stamped at that run, so
    a later `sealed` queues nothing — held by the row the tree carries and
    no count beside it."""
    repo, _target, _base = guaranteed(
        tmp_path,
        earlier="; earlier run: bbb2222 sealed; earlier run: abc1234 withheld — x",
    )
    assert after_the_commit(repo) == ""
    assert queued(repo) == []


def test_a_recommit_of_the_same_guarantee_queues_no_second_file(tmp_path):
    """#975 S8. An amend, and a second commit naming the same audited
    commit, find the first file — pending, or drawn and renamed — under any
    session's directory of the clone, and queue nothing more."""
    repo, _target, _base = guaranteed(tmp_path)
    assert after_the_commit(repo, session="s-1")
    git(
        repo,
        "-c",
        "user.name=e",
        "-c",
        "user.email=e@example.com",
        "commit",
        "--amend",
        "-qm",
        "the closing records, again",
    )
    assert after_the_commit(repo, session="s-2") == ""
    assert len(queued(repo)) == 1, queued(repo)
    stop(repo)
    (drawn_file,) = queued(repo)
    assert drawn_file.endswith(".drawn.json"), drawn_file
    git(
        repo,
        "-c",
        "user.name=e",
        "-c",
        "user.email=e@example.com",
        "commit",
        "--amend",
        "-qm",
        "the closing records, a third time",
    )
    assert after_the_commit(repo) == ""
    assert queued(repo) == [drawn_file]


def test_a_reseal_whose_row_lost_its_earlier_run_queues_nothing(tmp_path):
    """#975, once per work item. The sealer ran again at a new commit and
    wrote its row fresh, without `; earlier run: <sha> sealed`: the clone
    already holds the work item's stamp, so nothing more is queued. Red at
    a0ee12eb: the key named the audited commit, so a second file stood
    beside the drawn one."""
    repo, _target, base = guaranteed(tmp_path)
    assert after_the_commit(repo)
    stop(repo)
    item = repo / "seal" / "specs" / ITEM_NAME
    (repo / "x.txt").write_text("a fix after the seal\n", encoding="utf-8")
    commit_all(repo, "a fix")
    new = git(repo, "rev-parse", "--short", "HEAD").stdout.strip()
    (item / "guarantee.md").write_text(
        guarantee_text(new, base, "sealed"), encoding="utf-8"
    )
    commit_all(repo, "the sealer again, its row written fresh")
    assert after_the_commit(repo) == ""
    assert len(queued(repo)) == 1, queued(repo)


def test_a_squash_of_a_sealed_item_in_another_clone_queues_nothing(tmp_path):
    """#975, once per work item. The guarantee was stamped in one clone; a
    squash of its branch in another clone carries the verdict onto a commit
    whose history does not hold the audited commit, so nothing is queued.
    Red at a0ee12eb: the second clone held no values file, so it queued
    one."""
    repo, _target, _base = guaranteed(tmp_path)
    assert after_the_commit(repo)
    other = tmp_path / "other"
    subprocess.run(
        ["git", "clone", "-q", "--no-local", str(repo), str(other)], check=True
    )
    git(other, "switch", "-q", "main")
    git(other, "fetch", "-q", "origin", "feat/x:feat/x")
    git(other, "merge", "--squash", "feat/x")
    commit_all(other, "the squash, elsewhere")
    assert after_the_commit(other) == ""
    assert queued(other) == []


def test_a_sealed_item_recommitted_in_another_clone_queues_nothing(tmp_path):
    """#975 round 3, once per work item. The guarantee was stamped in one
    clone. In a second clone of the same branch, a commit that edits the
    sealed guarantee with no new run, and a re-seal whose row lost its
    earlier run, each find `sealed` earlier in the guarantee's history, so
    nothing is queued. Red at b81de037: the second clone held no values
    file, so the first of them queued one."""
    repo, _target, base = guaranteed(tmp_path)
    assert after_the_commit(repo)
    other = tmp_path / "other"
    subprocess.run(
        ["git", "clone", "-q", "--no-local", str(repo), str(other)], check=True
    )
    git(other, "switch", "-q", "feat/x")
    item = other / "seal" / "specs" / ITEM_NAME / "guarantee.md"
    item.write_text(item.read_text(encoding="utf-8") + "\na note\n", encoding="utf-8")
    commit_all(other, "a note in the guarantee, no new run")
    assert after_the_commit(other) == ""
    (other / "x.txt").write_text("a fix after the seal\n", encoding="utf-8")
    commit_all(other, "a fix")
    new = git(other, "rev-parse", "--short", "HEAD").stdout.strip()
    item.write_text(guarantee_text(new, base, "sealed"), encoding="utf-8")
    commit_all(other, "the sealer again, its row written fresh")
    assert after_the_commit(other) == ""
    assert queued(other) == []


def test_a_sealed_item_rebased_in_another_clone_queues_nothing(tmp_path):
    """#975 round 5, once per work item. The guarantee was stamped in one
    clone. A second clone rebases the branch, so the sealed commit is
    rewritten over a history that no longer holds its audited commit, and
    the sealer's re-run writes its row fresh. The rewritten `sealed` is the
    stamp's trace, so nothing is queued. Red at 5943f1d7: `sealed_before`
    skipped the rewritten commit and the second clone queued a second
    stamp."""
    repo, _target, _base = guaranteed(tmp_path)
    assert after_the_commit(repo)
    other = tmp_path / "other"
    subprocess.run(
        ["git", "clone", "-q", "--no-local", str(repo), str(other)], check=True
    )
    git(other, "switch", "-q", "main")
    (other / "base.txt").write_text("the base moved\n", encoding="utf-8")
    commit_all(other, "the base moved")
    git(other, "switch", "-q", "feat/x")
    git(
        other,
        "-c",
        "user.name=e",
        "-c",
        "user.email=e@example.com",
        "rebase",
        "-q",
        "main",
    )
    (other / "x.txt").write_text("a fix after the rebase\n", encoding="utf-8")
    commit_all(other, "a fix")
    new = git(other, "rev-parse", "--short", "HEAD").stdout.strip()
    base = git(other, "rev-parse", "--short", "main").stdout.strip()
    item = other / "seal" / "specs" / ITEM_NAME / "guarantee.md"
    item.write_text(guarantee_text(new, base, "sealed"), encoding="utf-8")
    commit_all(other, "the sealer again after the rebase, its row written fresh")
    assert after_the_commit(other) == ""
    assert queued(other) == []


def test_a_sealed_item_rebased_and_cloned_fresh_queues_nothing(tmp_path):
    """#975 round 6, once per work item. The guarantee was stamped in one
    clone, which then rebased the branch onto a moved base. A fresh clone
    of the rebased branch does not hold the commit the first `sealed`
    audited, and the sealer's re-run there writes its row fresh. The
    rewritten `sealed` still counts, so nothing is queued. Red with
    `sealed_before` counting a `sealed` only where its target resolves in
    the clone (`plan.md` B4): the fresh clone queued a second stamp."""
    repo, target, _base = guaranteed(tmp_path)
    assert after_the_commit(repo)
    git(repo, "switch", "-q", "main")
    (repo / "base.txt").write_text("the base moved\n", encoding="utf-8")
    commit_all(repo, "the base moved")
    git(repo, "switch", "-q", "feat/x")
    git(
        repo,
        "-c",
        "user.name=e",
        "-c",
        "user.email=e@example.com",
        "rebase",
        "-q",
        "main",
    )
    other = tmp_path / "other"
    subprocess.run(
        ["git", "clone", "-q", "--no-local", str(repo), str(other)], check=True
    )
    held = subprocess.run(
        ["git", "-C", str(other), "cat-file", "-e", target], capture_output=True
    )
    assert held.returncode != 0, "the fresh clone holds the pre-rebase commit"
    (other / "x.txt").write_text("a fix after the rebase\n", encoding="utf-8")
    commit_all(other, "a fix")
    new = git(other, "rev-parse", "--short", "HEAD").stdout.strip()
    base = git(other, "rev-parse", "--short", "origin/main").stdout.strip()
    item = other / "seal" / "specs" / ITEM_NAME / "guarantee.md"
    item.write_text(guarantee_text(new, base, "sealed"), encoding="utf-8")
    commit_all(other, "the sealer again in a fresh clone, its row written fresh")
    assert after_the_commit(other) == ""
    assert queued(other) == []


def test_the_guarantee_stamps_rows_are_read_from_the_records(tmp_path):
    """#975 S9, `questions.md` Q1's answer (a). The stamp carries what the
    records at the commit say and nothing re-measured: its title, the
    audited commit with the branch under it, the base, the work item's id,
    then the newest broad run `broad-gate.md` names and the count of round
    records. No `scale` is written."""
    mod = stamp_module()
    repo, target, base = guaranteed(tmp_path)
    after_the_commit(repo)
    (path,) = queued(repo)
    said = mod.read_values(path)
    assert said["rows"] == [
        ("SEALED", ""),
        ("tree", target),
        ("", "feat/x"),
        ("base", base),
        ("item", ITEM_ID),
        None,
        ("gate", f"✓ {target}"),
        ("rounds", "2"),
    ], said["rows"]
    assert "scale" not in said, said
    assert (said["tree"], said["base"], said["from"], said["branch"]) == (
        target,
        base,
        None,
        "feat/x",
    ), said
    assert said["item"] == str(repo / "seal" / "specs" / ITEM_NAME), said
    assert said["session"] == "s-1" and said["pr"] is None, said


# --- 1792363231: in local mode the stamp is queued at the write ---------------------
#
# A local-mode root sits under the git common dir and no commit carries it,
# so `post-commit` never sees its `guarantee.md`. `queue_for_local_guarantee`
# reads the file the sealer wrote, from disk, and queues the same values file
# the shared writer would; the `Stop` hook above draws it.

GUARANTEE_TEMPLATE = os.path.join(ROOT, "templates", "sdd-guarantee.md")


def routing_text(branch="feat/x"):
    """A `routing.md` in `templates/sdd-routing.md`'s shape, naming `branch`
    in its `Branch` row, or with no `Branch` row where `branch` is None."""
    rows = (
        "| Axis | Answer |\n|---|---|\n"
        "| Review | through the review chain |\n"
        "| Destination | open the pull request |\n"
    )
    return rows + (f"| Branch | {branch} |\n" if branch else "")


def local_guaranteed(tmp_path, verdict="sealed", earlier="", linked=False):
    """A repository in local mode — no `seal/` in its tree, its root under
    the git common dir (contract §11) — whose branch `feat/x` carries the
    audited commit, checked out in the main checkout or, with `linked`, in a
    linked worktree of it. The work item under that root holds `routing.md`
    naming the branch, two round records, `broad-gate.md` naming the audited
    commit and `guarantee.md` reading `verdict` over it. Returns (repo,
    target, base, the guarantee's path)."""
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init", "-q", "-b", "main")
    (repo / "README.md").write_text("x\n", encoding="utf-8")
    commit_all(repo, "x")
    where = repo
    if linked:
        where = tmp_path / "linked"
        git(repo, "worktree", "add", "-q", str(where), "-b", "feat/x")
    else:
        git(repo, "switch", "-qc", "feat/x")
    (where / "work.txt").write_text("the work\n", encoding="utf-8")
    commit_all(where, "the work")
    target = git(where, "rev-parse", "--short", "HEAD").stdout.strip()
    base = git(repo, "rev-parse", "--short", "main").stdout.strip()
    item = repo / ".git" / "seal" / "specs" / ITEM_NAME
    (item / "rounds").mkdir(parents=True)
    for n in (1, 2):
        (item / "rounds" / f"round-{n}.md").write_text("x\n", encoding="utf-8")
    (item / "routing.md").write_text(routing_text(), encoding="utf-8")
    (item / "broad-gate.md").write_text(
        f"| Field | Value |\n|---|---|\n| Broad gate | {target} against {base} |\n",
        encoding="utf-8",
    )
    path = item / "guarantee.md"
    path.write_text(guarantee_text(target, base, verdict, earlier), encoding="utf-8")
    return repo, target, base, path


def queue_local(path, session="s-1"):
    """What the local writer returned for the `guarantee.md` at `path`."""
    return stamp_module().queue_for_local_guarantee(str(path), session)


@pytest.mark.parametrize("linked", [False, True], ids=["main checkout", "linked"])
def test_a_local_mode_sealed_guarantee_queues_one_stamp(tmp_path, linked):
    """1792363231 S1. A local-mode `guarantee.md` reading `sealed` over a commit on
    the `Branch` row's branch, with no earlier run reading `sealed`, queues
    one values file for the session under the common dir, named by the work
    item's id and the audited commit, with the rows the shared writer
    builds from the same records, and returns the one line `post-commit`
    prints in shared mode. The main session's `Stop` then draws it once.
    The same from a linked worktree, whose common dir is the main
    checkout's `.git`. Red at d8f9eaef: `seal_stamp` had no local writer."""
    mod = stamp_module()
    repo, target, base, path = local_guaranteed(tmp_path, linked=linked)
    said = queue_local(path)
    (written,) = queued(repo)
    assert os.path.dirname(written) == str(repo / ".git" / "specseal-stamp" / "s-1")
    assert os.path.basename(written).endswith(f"-{ITEM_ID}-{target}.json"), written
    real = os.path.realpath(written)
    assert said == [mod.QUEUED.format(id=ITEM_ID, path=real, command=mod.quote(real))]
    values = mod.read_values(written)
    assert values["rows"] == [
        ("SEALED", ""),
        ("tree", target),
        ("", "feat/x"),
        ("base", base),
        ("item", ITEM_ID),
        None,
        ("gate", f"✓ {target}"),
        ("rounds", "2"),
    ], values["rows"]
    assert (values["tree"], values["base"], values["from"], values["branch"]) == (
        target,
        base,
        None,
        "feat/x",
    ), values
    assert values["item"] == os.path.realpath(path.parent), values
    assert values["session"] == "s-1" and values["pr"] is None, values
    lines = message(stop(repo))
    assert lines[0] == f"SEALED feat/x @ {target} against {base} · {ITEM_NAME}", lines
    assert stop(repo) == "", "the stamp was drawn twice"


@pytest.mark.parametrize(
    "written",
    [
        lambda t, b: guarantee_text(t, b, "withheld — the README is stale"),
        lambda t, b: guarantee_text(t, b, "undecided — does #12 ask for the flag?"),
        lambda t, b: guarantee_text(t, b, "sealed") + "\nVerdict: withheld — x\n",
        lambda t, b: open(GUARANTEE_TEMPLATE, encoding="utf-8").read(),
    ],
    ids=["withheld", "undecided", "two verdicts", "the unfilled template"],
)
def test_a_local_mode_withheld_or_undecided_guarantee_queues_nothing(tmp_path, written):
    """1792363231 S2. The finished-work stamp is not drawn over unfinished work in
    local mode either: a guarantee that does not read one `Verdict:` of
    `sealed` queues nothing and returns no line."""
    repo, target, base, path = local_guaranteed(tmp_path)
    path.write_text(written(target, base), encoding="utf-8")
    assert queue_local(path) == []
    assert queued(repo) == []


def test_a_local_mode_reseal_after_withheld_queues_the_stamp(tmp_path):
    """1792363231 S3. The sealer withheld, the work was fixed, and its second run
    reads `sealed` with the earlier verdict kept on the row: that write
    queues the stamp. A work item whose review went straight to the pull
    request holds no `rounds/`, and its stamp reads `0` rounds."""
    repo, target, _base, path = local_guaranteed(
        tmp_path, earlier="; earlier run: abc1234 withheld — the README is stale"
    )
    for name in ("round-1.md", "round-2.md"):
        (path.parent / "rounds" / name).unlink()
    (path.parent / "rounds").rmdir()
    assert queue_local(path)
    (written,) = queued(repo)
    assert written.endswith(f"-{ITEM_ID}-{target}.json"), written
    assert stamp_module().read_values(written)["rows"][-1] == ("rounds", "0")


def test_a_local_mode_second_sealed_queues_nothing(tmp_path):
    """1792363231 S3, once per work item. A row whose earlier-run chain reads
    `sealed` was stamped at that run, so it queues nothing. A values file
    for the work item under any session's directory of the clone, pending
    or drawn, is a complete record in local mode, since the root and the
    values directory share the common dir: a second write queues nothing
    beside it."""
    repo, target, base, path = local_guaranteed(
        tmp_path,
        earlier="; earlier run: bbb2222 sealed; earlier run: abc1234 withheld — x",
    )
    assert queue_local(path) == []
    assert queued(repo) == []
    path.write_text(guarantee_text(target, base, "sealed"), encoding="utf-8")
    assert queue_local(path, session="s-1")
    assert queue_local(path, session="s-2") == []
    assert len(queued(repo)) == 1, queued(repo)
    stop(repo)
    (drawn_file,) = queued(repo)
    assert drawn_file.endswith(".drawn.json"), drawn_file
    assert queue_local(path, session="s-3") == []
    assert queued(repo) == [drawn_file]


def _unresolved(repo, item, target, base):
    (item / "guarantee.md").write_text(
        guarantee_text("dead0000", base, "sealed"), encoding="utf-8"
    )


def _off_the_branch(repo, item, target, base):
    (item / "guarantee.md").write_text(
        guarantee_text(off_branch_commit(repo), base, "sealed"), encoding="utf-8"
    )


def _no_target(repo, item, target, base):
    (item / "guarantee.md").write_text(
        "# an item — guarantee\n\nVerdict: sealed\n", encoding="utf-8"
    )


def _no_routing(repo, item, target, base):
    (item / "routing.md").unlink()


def _no_branch_row(repo, item, target, base):
    (item / "routing.md").write_text(routing_text(None), encoding="utf-8")


def _a_branch_gone(repo, item, target, base):
    (item / "routing.md").write_text(routing_text("feat/merged"), encoding="utf-8")


@pytest.mark.parametrize(
    "given",
    [
        _no_target,
        _unresolved,
        _off_the_branch,
        _no_routing,
        _no_branch_row,
        _a_branch_gone,
    ],
    ids=[
        "no Target SHA row",
        "the target does not resolve",
        "the target is off the branch",
        "no routing.md",
        "no Branch row",
        "a branch the clone no longer holds",
    ],
)
def test_a_local_mode_guarantee_off_its_branch_queues_nothing(tmp_path, given):
    """1792363231 S4. `settle` never retires a local-mode work item, so a `sealed`
    the clone wrote long ago still stands under its root. A verdict over a
    commit the work item's branch does not hold — or one whose branch cannot
    be named or is gone — queues nothing, so editing an old guarantee draws
    no stamp for work finished long ago."""
    repo, target, base, path = local_guaranteed(tmp_path)
    given(repo, path.parent, target, base)
    assert queue_local(path) == []
    assert queued(repo) == []


def test_the_edit_gate_leaves_shared_mode_to_post_commit(tmp_path):
    """1792363231 S5, the writer's half. A `guarantee.md` reading `sealed` under
    `<repo>/seal/` is shared mode's, whose stamp `post-commit` queues at the
    commit; and a root under the git common dir of a repository that also
    has `<repo>/seal/` is shared too (contract §11). The local writer queues
    nothing for either, where every other fact would queue; nor for the
    same `sealed` text under a local work item in a file that is not its
    `guarantee.md`."""
    for name in ("shared", "both", "local"):
        (tmp_path / name).mkdir()
    shared, _target, _base = guaranteed(tmp_path / "shared")
    item = shared / "seal" / "specs" / ITEM_NAME
    (item / "routing.md").write_text(routing_text(), encoding="utf-8")
    assert queue_local(item / "guarantee.md") == []
    assert queued(shared) == []
    both, _target, _base, path = local_guaranteed(tmp_path / "both")
    (both / "seal").mkdir()
    assert queue_local(path) == []
    assert queued(both) == []
    local, _target, _base, path = local_guaranteed(tmp_path / "local")
    notes = path.parent / "notes.md"
    notes.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    assert queue_local(notes) == []
    assert queued(local) == []
    # The gate's half: a `Write` of the shared guarantee says nothing.
    assert post_edit(edit_payload(item / "guarantee.md", shared), shared) == ""
    assert queued(shared) == []


# --- 1792363231 S6: the `post-edit` gate queues it at the write ---------------------

QUEUE_GATE = "sealer-stamp-queue.py"


def post_edit(body, cwd):
    """`dispatch.py post-edit` as the harness runs it after a file edit:
    `body` on stdin, a dict sent as JSON and a string as it is, and what the
    group printed."""
    r = subprocess.run(
        [sys.executable, DISPATCH, "post-edit"],
        input=body if isinstance(body, str) else json.dumps(body),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=60,
        cwd=str(cwd),
    )
    assert r.returncode == 0, r.stderr
    return r.stdout


def edit_payload(path, cwd, tool="Write", session="s-1", **extra):
    """A `PostToolUse` payload for `tool` on the file at `path`."""
    body = {
        "hook_event_name": "PostToolUse",
        "tool_name": tool,
        "tool_input": {"file_path": str(path)},
        "cwd": str(cwd),
    }
    if session:
        body["session_id"] = session
    body.update(extra)
    return body


@pytest.mark.parametrize("tool", ["Write", "Edit"])
def test_the_edit_gate_queues_a_local_mode_sealed_guarantee(tmp_path, tool):
    """1792363231 S6. A `Write` or `Edit` that leaves a local-mode `guarantee.md`
    reading `sealed` runs the `post-edit` group, whose gate queues the work
    item's one values file for the payload's session and prints one JSON
    object whose `systemMessage` is the writer's line. The repository is
    found from the edited file, never from the payload's `cwd`, which here
    is outside it. The main session's `Stop` then draws the file this gate
    wrote, once. Red at f6ad0b2c: no gate in the group queued anything."""
    mod = stamp_module()
    repo, target, base, path = local_guaranteed(tmp_path)
    elsewhere = tmp_path / "elsewhere"
    elsewhere.mkdir()
    out = post_edit(edit_payload(path, elsewhere, tool=tool), elsewhere)
    (written,) = queued(repo)
    real = os.path.realpath(written)
    line = mod.QUEUED.format(id=ITEM_ID, path=real, command=mod.quote(real))
    assert json.loads(out) == {"systemMessage": line}, out
    lines = message(stop(repo))
    assert lines[0] == f"SEALED feat/x @ {target} against {base} · {ITEM_NAME}", lines
    assert stop(repo) == "", "the stamp was drawn twice"


def test_a_subagents_write_queues_and_draws_nothing(tmp_path):
    """1792363231 S6. The sealer writes its own `guarantee.md`, so the payload
    carries its `agent_id` beside the main session's `session_id`
    (`questions.md` Q1). Queueing is not drawing: the gate queues the same
    file for the main session, the subagent's end draws nothing and leaves
    it, and the main session's `Stop` draws it."""
    repo, _target, _base, path = local_guaranteed(tmp_path)
    sealer = {"agent_id": "a-1", "agent_type": "specseal:sealer"}
    assert json.loads(post_edit(edit_payload(path, repo, **sealer), repo))
    (written,) = queued(repo)
    assert os.path.dirname(written) == str(repo / ".git" / "specseal-stamp" / "s-1")
    assert stop(repo, agent_id="a-1") == ""
    assert queued(repo) == [written]
    assert message(stop(repo))[0].startswith("SEALED feat/x @ ")


@pytest.mark.parametrize(
    "given",
    [
        lambda path, cwd: edit_payload(path.parent / "notes.md", cwd),
        lambda path, cwd: edit_payload(cwd / "docs" / "guarantee.md", cwd),
        lambda path, cwd: edit_payload(path, cwd, tool="NotebookEdit"),
        lambda path, cwd: edit_payload(path, cwd, session=None),
        lambda path, cwd: "a payload that is not JSON",
    ],
    ids=[
        "another file of the item",
        "a guarantee.md outside seal/specs",
        "NotebookEdit",
        "no session_id",
        "not JSON",
    ],
)
def test_the_edit_gate_is_silent_off_a_guarantee(tmp_path, given, monkeypatch):
    """1792363231 S6. The gate runs after every file edit in every repository, so
    for any other edit it says nothing and writes nothing, and it loads
    `seal_stamp.py`, its only way to `git`, only once the edit has matched:
    a `Write` or `Edit`, with a session, of `…/seal/specs/<id>/guarantee.md`.
    The order is asked of the gate itself, with its loader replaced, and the
    guarantee's own `Write` is the control that the loader is reached."""
    repo, _target, _base, path = local_guaranteed(tmp_path)
    (path.parent / "notes.md").write_text(
        path.read_text(encoding="utf-8"), encoding="utf-8"
    )
    body = given(path, repo)
    assert post_edit(body, repo) == ""
    assert queued(repo) == []
    gate = _load(
        "specseal_queue_gate_for_its_order", os.path.join(HOOKS_DIR, QUEUE_GATE)
    )
    loads = []
    monkeypatch.setattr(gate, "load_stamp", lambda: loads.append(1))
    for sent, expected in ((body, []), (edit_payload(path, repo), [1])):
        text = sent if isinstance(sent, str) else json.dumps(sent)
        monkeypatch.setattr(sys, "stdin", __import__("io").StringIO(text))
        gate.main()
        assert loads == expected, (sent, loads)


# --- 1792363231 S11-S14: a `sealed` this clone refused leaves a refusal record ------
#
# `questions.md` Q2, answered (b): a `sealed` a writer refuses because its
# audited commit is not on the branch leaves an empty file in the clone's
# common dir, and the once readers skip a `sealed` this clone refused, so the
# repair draws the work item's one stamp. Four guards keep a record from
# standing where the refused `sealed` may have been stamped in another clone.

REFUSED = "specseal-stamp-refused"
SIGNED = ("-c", "user.name=e", "-c", "user.email=e@example.com")


def refusals(repo):
    """The refusal records under `repo`'s git common dir, by name."""
    try:
        return sorted(os.listdir(repo / ".git" / REFUSED))
    except OSError:
        return []


def short(repo, ref="HEAD"):
    return git(repo, "rev-parse", "--short", ref).stdout.strip()


def seal_and_commit(repo, target, base, message, earlier="", verdict="sealed"):
    """`guarantee.md` rewritten to read `verdict` over `target`, committed."""
    item = repo / "seal" / "specs" / ITEM_NAME / "guarantee.md"
    item.write_text(guarantee_text(target, base, verdict, earlier), encoding="utf-8")
    commit_all(repo, message)


def a_fix(repo, message="a fix after the seal"):
    """One commit of work after the seal; its short SHA."""
    (repo / "x.txt").write_text(message + "\n", encoding="utf-8")
    commit_all(repo, message)
    return short(repo)


def off_branch_commit(repo):
    """A commit on top of `main` that no branch holds; its short SHA."""
    tree = git(repo, "rev-parse", "main^{tree}").stdout.strip()
    sha = git(
        repo,
        *SIGNED,
        "commit-tree",
        tree,
        "-p",
        "main",
        "-m",
        "a commit no branch holds",
    ).stdout.strip()
    return sha[:7]


def rebased_and_cloned_fresh(tmp_path):
    """#975 round 6's shape: a guarantee stamped in one clone, whose branch
    that clone then rebases onto a moved base, and a fresh clone of the
    rebased branch, which does not hold the commit the `sealed` audited.
    Returns (the fresh clone, the audited commit)."""
    repo, target, _base = guaranteed(tmp_path)
    assert after_the_commit(repo)
    git(repo, "switch", "-q", "main")
    (repo / "base.txt").write_text("the base moved\n", encoding="utf-8")
    commit_all(repo, "the base moved")
    git(repo, "switch", "-q", "feat/x")
    git(repo, *SIGNED, "rebase", "-q", "main")
    other = tmp_path / "other"
    subprocess.run(
        ["git", "clone", "-q", "--no-local", str(repo), str(other)], check=True
    )
    held = subprocess.run(
        ["git", "-C", str(other), "cat-file", "-e", target], capture_output=True
    )
    assert held.returncode != 0, "the fresh clone holds the pre-rebase commit"
    return other, target


def resealed_draws_nothing(clone, base_ref):
    """The sealer's re-run in `clone` after a fix, its row written fresh,
    queues nothing, so the work item is not stamped a second time."""
    new = a_fix(clone)
    base = short(clone, base_ref)
    seal_and_commit(clone, new, base, "the sealer again, its row written fresh")
    assert after_the_commit(clone) == ""
    assert queued(clone) == []


@pytest.mark.parametrize(
    "earlier",
    ["", "; earlier run: deadbee sealed", "; earlier run: deadbee0 sealed"],
    ids=[
        "the row written fresh",
        "the row keeps the refused run",
        "the row keeps it spelled longer",
    ],
)
def test_a_seal_this_clone_refused_does_not_count_as_stamped(tmp_path, earlier):
    """1792363231 S11, #975 round 4's measured shape (`rounds/round-4.md` finding
    1, probe rows 4 and 5). The sealer withheld, then a plain commit makes
    the guarantee read `sealed` over `deadbee`, a commit the clone does not
    hold: nothing is queued, and this clone records that it refused that
    verdict. The repair in the same clone, its row written fresh or keeping
    the refused run, then queues the work item's one stamp; a later commit
    of the guarantee queues nothing. Red at f6ad0b2c: the refused `sealed`
    counted as stamped, so the repair queued nothing."""
    repo, target, base = guaranteed(tmp_path, verdict="withheld — the README is stale")
    assert after_the_commit(repo) == ""
    seal_and_commit(repo, "deadbee", base, "the sealer's row names a commit nobody has")
    assert after_the_commit(repo) == ""
    assert queued(repo) == [] and refusals(repo) == [f"{ITEM_ID}-deadbee"]
    seal_and_commit(repo, target, base, "the row repaired", earlier=earlier)
    assert after_the_commit(repo)
    (path,) = queued(repo)
    assert path.endswith(f"-{ITEM_ID}-{target}.json"), path
    item = repo / "seal" / "specs" / ITEM_NAME / "guarantee.md"
    item.write_text(item.read_text(encoding="utf-8") + "\na note\n", encoding="utf-8")
    commit_all(repo, "a note in the guarantee")
    assert after_the_commit(repo) == ""
    assert queued(repo) == [path]


def test_a_refusal_record_skips_only_its_own_verdict(tmp_path):
    """1792363231 S11's reader half. A record answers for one work item and
    one commit spelled at least seven characters long, so it skips nothing
    else. A record another work item left over the same commit leaves this
    item's earlier `sealed` counted, and so does a record of this item where
    the earlier `sealed` names no commit at all."""
    mod = stamp_module()
    for name in ("other item", "no target"):
        (tmp_path / name).mkdir()
    repo, _target, _base = guaranteed(
        tmp_path / "other item", earlier="; earlier run: deadbee sealed"
    )
    mod.record_refusal(str(repo / ".git"), "1700000000", "deadbee")
    assert after_the_commit(repo) == ""
    assert queued(repo) == []
    repo, target, base = guaranteed(tmp_path / "no target", verdict="withheld — x")
    item = repo / "seal" / "specs" / ITEM_NAME / "guarantee.md"
    item.write_text("# an item — guarantee\n\nVerdict: sealed\n", encoding="utf-8")
    commit_all(repo, "a sealed that names no commit")
    assert after_the_commit(repo) == ""
    mod.record_refusal(str(repo / ".git"), ITEM_ID, "deadbee")
    seal_and_commit(repo, target, base, "the sealer again")
    assert after_the_commit(repo) == ""
    assert queued(repo) == []


def test_a_seal_over_a_commit_off_the_branch_then_repaired_draws_once(tmp_path):
    """1792363231 S12. A plain commit makes the guarantee read `sealed` over a
    commit the clone holds on another branch, with no patch-equivalent copy
    in HEAD's history: nothing is queued and the refusal is recorded. The
    repair in the same clone queues one file. Red at f6ad0b2c: the repair
    queued nothing."""
    repo, target, base = guaranteed(tmp_path, verdict="withheld — x")
    git(repo, "switch", "-qc", "elsewhere", "main")
    (repo / "elsewhere.txt").write_text("other work\n", encoding="utf-8")
    commit_all(repo, "work on another branch")
    off = short(repo)
    git(repo, "switch", "-q", "feat/x")
    seal_and_commit(repo, off, base, "the sealer's row names another branch's commit")
    assert after_the_commit(repo) == ""
    assert queued(repo) == [] and refusals(repo) == [f"{ITEM_ID}-{off}"]
    seal_and_commit(repo, target, base, "the row repaired")
    assert after_the_commit(repo)
    assert len(queued(repo)) == 1, queued(repo)


def test_a_local_mode_seal_refused_off_its_branch_then_resealed_draws_once(tmp_path):
    """1792363231 S14. In local mode a `sealed` over a commit the `Branch` row's
    branch does not hold, while that branch exists, queues nothing and
    records the refusal; the re-seal whose row keeps that run as `sealed`
    then queues one file. Where the refusal is for a missing `Branch` row or
    a branch the clone no longer holds, nothing is recorded. Red at
    f6ad0b2c: the re-seal's chain counted the refused run as stamped."""
    (tmp_path / "held").mkdir()
    repo, target, base, path = local_guaranteed(tmp_path / "held")
    off = off_branch_commit(repo)
    path.write_text(guarantee_text(off, base, "sealed"), encoding="utf-8")
    assert queue_local(path) == []
    assert queued(repo) == [] and refusals(repo) == [f"{ITEM_ID}-{off}"]
    path.write_text(
        guarantee_text(target, base, "sealed", f"; earlier run: {off} sealed"),
        encoding="utf-8",
    )
    assert queue_local(path)
    assert len(queued(repo)) == 1, queued(repo)
    for given in (_no_branch_row, _a_branch_gone):
        (tmp_path / given.__name__).mkdir()
        repo, target, base, path = local_guaranteed(tmp_path / given.__name__)
        off = off_branch_commit(repo)
        path.write_text(guarantee_text(off, base, "sealed"), encoding="utf-8")
        given(repo, path.parent, target, base)
        assert queue_local(path) == []
        assert refusals(repo) == [], given.__name__


def test_a_conflicted_rebase_in_another_clone_writes_no_refusal(tmp_path):
    """1792363231 S13, guard 2. The guarantee was stamped in one clone. A second
    clone rebases the branch over a base that conflicts with the audited
    commit, so its copy has another patch, and the rewritten `sealed` over
    the old commit is refused there. A rebase rewrites history that may have
    been stamped elsewhere, so it writes no record, and the sealer's re-run
    in that clone queues nothing."""
    repo, _target, _base = guaranteed(tmp_path)
    assert after_the_commit(repo)
    other = tmp_path / "other"
    subprocess.run(
        ["git", "clone", "-q", "--no-local", str(repo), str(other)], check=True
    )
    git(other, "switch", "-q", "main")
    rounds = other / "seal" / "specs" / ITEM_NAME / "rounds"
    rounds.mkdir(parents=True)
    (rounds / "round-1.md").write_text("the base wrote this first\n", encoding="utf-8")
    commit_all(other, "the base moved under the audited commit")
    git(other, "switch", "-q", "feat/x")
    conflicted = subprocess.run(
        ["git", "-C", str(other), *SIGNED, "rebase", "-q", "main"], capture_output=True
    )
    assert conflicted.returncode != 0, "the rebase did not conflict"
    (rounds / "round-1.md").write_text("x\n", encoding="utf-8")
    git(other, "add", "-A")
    git(other, *SIGNED, "-c", "core.editor=true", "rebase", "--continue")
    assert after_the_commit(other) == ""
    assert refusals(other) == []
    resealed_draws_nothing(other, "main")


def test_an_amend_in_a_fresh_clone_writes_no_refusal(tmp_path):
    """1792363231 S13, guard 2. In a fresh clone of a branch rebased and
    force-pushed after its stamp, the sealing commit is amended: its
    `sealed` names a commit the clone does not hold, and is refused. An
    amend rewrites a commit that may have been stamped elsewhere, so it
    writes no record, and the sealer's re-run queues nothing."""
    other, _target = rebased_and_cloned_fresh(tmp_path)
    git(other, *SIGNED, "commit", "--amend", "-qm", "the closing records, amended")
    assert after_the_commit(other) == ""
    assert refusals(other) == []
    resealed_draws_nothing(other, "origin/main")


def test_a_body_edit_over_a_rewritten_seal_writes_no_refusal(tmp_path):
    """1792363231 S13, the shape `spec.md` gives guard 3. In the same fresh
    clone a plain commit edits the body of the rewritten `sealed`, which
    still names the commit the clone does not hold. That `sealed` was in the
    history before the edit, so `sealed_before` refuses the edit before the
    ancestry refusal is reached, no record is written, and the sealer's
    re-run queues nothing. Guard 3 itself was not built: no case could fail
    it (`phases/phase-3.md`)."""
    other, _target = rebased_and_cloned_fresh(tmp_path)
    item = other / "seal" / "specs" / ITEM_NAME / "guarantee.md"
    item.write_text(item.read_text(encoding="utf-8") + "\na note\n", encoding="utf-8")
    commit_all(other, "a note in the rewritten guarantee")
    assert after_the_commit(other) == ""
    assert refusals(other) == []
    resealed_draws_nothing(other, "origin/main")


def test_a_seal_whose_target_has_a_copy_writes_no_refusal(tmp_path):
    """1792363231 S13, guard 4. The sealer audited a commit, the branch was then
    rebased, and its verdict was committed after: a plain commit introducing
    a `sealed` over a commit whose patch-equivalent copy stands in HEAD's
    history. That verdict may have been stamped in a clone where the commit
    was still on the branch, so it writes no record, and the re-seal queues
    nothing."""
    repo = opted_in(tmp_path)
    git(repo, "switch", "-qc", "feat/x")
    item = repo / "seal" / "specs" / ITEM_NAME
    (item / "rounds").mkdir(parents=True)
    (item / "rounds" / "round-1.md").write_text("x\n", encoding="utf-8")
    commit_all(repo, "the rounds")
    target = short(repo)
    git(repo, "switch", "-q", "main")
    (repo / "base.txt").write_text("the base moved\n", encoding="utf-8")
    commit_all(repo, "the base moved")
    git(repo, "switch", "-q", "feat/x")
    git(repo, *SIGNED, "rebase", "-q", "main")
    base = short(repo, "main")
    (item / "broad-gate.md").write_text(
        f"| Field | Value |\n|---|---|\n| Broad gate | {target} against {base} |\n",
        encoding="utf-8",
    )
    seal_and_commit(repo, target, base, "the verdict, committed after a rebase")
    assert after_the_commit(repo) == ""
    assert refusals(repo) == []
    resealed_draws_nothing(repo, "main")


def test_guard_two_reads_what_post_commit_sees_in_the_reflog(tmp_path):
    """1792363231 S13 guard 2, `questions.md` Q4. A real `post-commit` hook logs
    `git reflog -1 --format=%gs HEAD` for each kind of commit git runs it
    after, which is what guard 2 reads there. A plain commit and an initial
    one carry the two subjects the guard accepts; an amend, a cherry-pick, a
    rebase's pick and its continue, and a concluded merge each carry another,
    so none of them writes a refusal record. Run on every CI leg, so a git
    whose subjects differ fails here and names the subject."""
    mod = stamp_module()
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init", "-q", "-b", "main")
    hooks = tmp_path / "hooks"
    hooks.mkdir()
    log = tmp_path / "subjects.log"
    hook = hooks / "post-commit"
    hook.write_text(
        f'#!/bin/sh\ngit reflog -1 --format=%gs HEAD >> "{log.as_posix()}"\n',
        encoding="utf-8",
    )
    hook.chmod(0o755)
    git(repo, "config", "core.hooksPath", hooks.as_posix())

    def put(name, text):
        (repo / name).write_text(text, encoding="utf-8")
        git(repo, "add", "-A")

    def said():
        return log.read_text(encoding="utf-8").split("\n")[-2]

    seen = {}
    put("a.txt", "a\n")
    git(repo, *SIGNED, "commit", "-qm", "initial")
    seen["initial"] = said()
    put("b.txt", "b\n")
    git(repo, *SIGNED, "commit", "-qm", "plain")
    seen["plain"] = said()
    git(repo, *SIGNED, "commit", "--amend", "-qm", "amended")
    seen["amend"] = said()
    git(repo, "switch", "-qc", "side")
    put("c.txt", "c\n")
    git(repo, *SIGNED, "commit", "-qm", "on side")
    git(repo, "switch", "-q", "main")
    # Main moves first: a cherry-pick onto the side commit's own parent in
    # the same second is that commit, byte for byte, and the rebase below
    # would then have nothing to pick.
    put("m.txt", "m\n")
    git(repo, *SIGNED, "commit", "-qm", "main moves")
    git(repo, *SIGNED, "cherry-pick", "side")
    seen["cherry-pick"] = said()
    git(repo, "switch", "-q", "side")
    put("d.txt", "d\n")
    git(repo, *SIGNED, "commit", "-qm", "more on side")
    git(repo, *SIGNED, "rebase", "-q", "main")
    seen["rebase pick"] = said()
    put("f.txt", "side\n")
    git(repo, *SIGNED, "commit", "-qm", "f on side")
    git(repo, "switch", "-q", "main")
    put("f.txt", "main\n")
    git(repo, *SIGNED, "commit", "-qm", "f on main")
    git(repo, "switch", "-q", "side")
    stopped = subprocess.run(
        ["git", "-C", str(repo), *SIGNED, "rebase", "-q", "main"], capture_output=True
    )
    assert stopped.returncode != 0, "the rebase did not conflict"
    put("f.txt", "both\n")
    git(repo, *SIGNED, "-c", "core.editor=true", "rebase", "--continue")
    seen["rebase continue"] = said()
    git(repo, "switch", "-q", "main")
    put("f.txt", "main again\n")
    git(repo, *SIGNED, "commit", "-qm", "f on main again")
    stopped = subprocess.run(
        ["git", "-C", str(repo), *SIGNED, "merge", "-q", "side"], capture_output=True
    )
    assert stopped.returncode != 0, "the merge did not conflict"
    put("f.txt", "merged\n")
    git(repo, *SIGNED, "commit", "-q", "--no-edit")
    seen["merge"] = said()
    prefixes = {
        "initial": "commit (initial): ",
        "plain": "commit: ",
        "amend": "commit (amend): ",
        "cherry-pick": "cherry-pick: ",
        "rebase pick": "rebase (pick): ",
        "rebase continue": "rebase (continue): ",
        "merge": "commit (merge): ",
    }
    for kind, prefix in prefixes.items():
        assert seen[kind].startswith(prefix), (kind, seen[kind])
        assert mod.plain_commit(seen[kind]) == (kind in ("initial", "plain")), kind


# --- #717: the hook's whole message is held under a budget --------------------

# What `broad_gate.panel` returns for a real run since #832 — `full_values()`'s
# run, with values as long as a real run's: its branch elided at
# `PANEL_VALUE_WIDTH`, the base's ref beside its commit, the result rows behind
# a `✓`. Neutral values.
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

# A panel in the shape the gate wrote from #666 to #717, with values as long as
# a real run's. Its drawing with its disc under its label was over the harness's limit,
# which put every stamp drawn from #666 on behind a 2 KB preview of a file.
# Neutral values; a file in this shape may still be pending when a newer hook
# draws it, which is why a case keeps it rather than following `panel`.
OLD_ROWS = [
    ("SEALED", ""),
    None,
    ("tree", "aaa1111a"),
    ("", "feat/12-the-branch-n..."),
    ("base", "bbb2222b"),
    ("", "origin/release/v1.2.3"),
    ("item", "#12 . 1799000000"),
    ("gate", "tree 1.2.3"),
    None,
    ("suite", "6621 passed, 11 skipped"),
    ("", "exit 0"),
    ("ledger", "3451 ok"),
    ("", "0 drifted . 0 broken"),
    ("chain", "exit 0"),
    None,
    ("workflow", "4 of 9 not answered"),
    None,
    ("rounds", "2"),
]


def full_values(tree="aaa1111a"):
    """A values file as long as a real run's, label included: a branch and a
    work item named the way this repository names them."""
    name = "the-branch-names-the-work-item-it-carries"
    return {
        **values(item=f"/x/seal/specs/1799000000-{name}", rows=FULL_ROWS),
        "tree": tree,
        "base": "bbb2222b",
        "from": "origin/release/v1.2.3",
        "branch": f"feat/12-{name}",
    }


def test_the_budget_is_named_and_derived_from_the_measured_limit():
    """A2. The limit is the harness's, measured in characters, and the
    budget leaves room for the report `dispatch.py` prepends to the same
    message."""
    mod = stamp_module()
    assert mod.MESSAGE_LIMIT <= 10090, "above a size the harness has persisted"
    assert mod.MESSAGE_LIMIT == 10000, "not the number the probe measured"
    assert mod.MESSAGE_BUDGET <= mod.MESSAGE_LIMIT - 1000, mod.MESSAGE_BUDGET


def test_the_hooks_message_is_under_the_budget_for_one_file(tmp_path):
    """A3, one file. A run's values at a real run's size, drawn by the hook
    through `dispatch.py stop`: the printed `systemMessage` is no longer than
    `MESSAGE_BUDGET`, it still opens with the file's label, and it is the
    stamp WITH its disc. Under the budget by itself is what
    `admitted` guarantees whatever the stamp's size, by dropping the disc
    from a block that does not fit with it, so without the last assertion a
    stamp grown past the budget passed here as the text block alone (round
    1's 🟡 4)."""
    mod = stamp_module()
    repo = opted_in(tmp_path)
    mod.write_values(str(repo / ".git"), "s-1", full_values())
    text = json.loads(stop(repo))["systemMessage"]
    assert len(text) <= mod.MESSAGE_BUDGET, len(text)
    assert text.split("\n", 1)[0] == mod.label(full_values())
    assert text == drawn(mod, mod.label(full_values()), FULL_ROWS), (
        "a real work item's stamp no longer fits the budget with its disc"
    )


# The rows the owner's chosen reference was drawn over: the orchestrating
# session's `frames.py`'s `ROWS`, behind the panel's title row, which
# `frames.py#design_open` drew from a constant. They are the panel's shape
# with one difference the real panel does not have — a `flow` row where the
# panel carries `CI also` (`questions.md` Q15 of work item 1791270164) — and
# they stay here as data, because the owner's picture was drawn over them.
REFERENCE_ROWS = [
    ("SEALED", ""),
    ("tree", "aaa1111a"),
    ("", "feat/12-the-branch-names-the-work-item"),
    ("base", "bbb2222b  origin/release/v1.2.3"),
    ("item", "#12 · 1799000000"),
    ("gate", "tree 1.2.3"),
    None,
    ("suite", "✓ 6621 passed · 11 skipped"),
    ("ledger", "✓ 3451 ok · 0 drifted · 0 broken"),
    ("chain", "✓ exit 0"),
    ("flow", "· 4 of 9 not answered"),
    ("rounds", "2"),
]
# The owner's reference for a real work item's stamp, chosen on 2026-10-07: design 3
# of `frames.py`, `~/Desktop/specseal-frame-3-open.ans` on the owner's
# machine (`spec.md` decision 6 and S3 of work item 1791270164). Transcribed
# from that file's SGR stream and half-blocks by a script that read no line
# of `seal_stamp.py`: each disc cell its top half's letter (its bottom
# half's where the top is off the disc), the text as the twin writes it, and
# each line without the blank cells the reference carries past its end.
REFERENCE_TWIN = (
    "        mmmmmmmmmmmm           SEALED ------------------------------",
    "     mmmMMMMMMMMMMMMmmm",
    "   mmMMMMNNN....NNNnnnnmm      tree    aaa1111a",
    "  mmMMNN............NMnnmm             feat/12-the-branch-names-the-work-item",
    " mMMMN....YYxyyyXXYy..MnnNm    base    bbb2222b  origin/release/v1.2.3",
    "mmMMN....YXXy.....xy...MNNmm   item    #12 . 1799000000",
    "mMMN.....YXXXXYY...y....MNNm   gate    tree 1.2.3",
    "mMMN.......xxXXXXXX.....MNNm",
    "mMMNN....Y.....yXXXxy..MMNNm   suite   + 6621 passed . 11 skipped",
    " mMMN....YX......Yxxy..MNNm    ledger  + 3451 ok . 0 drifted . 0 broken",
    "  mnnNN..YyxxYYYYxyy.MMNNm     chain   + exit 0",
    "   mnnnMM..........MMNNNm      flow    . 4 of 9 not answered",
    "     mmnnNNMMMMMMNNNNmm        rounds  2",
    "        mmmNNNNNNmmm",
)
# The disc's twenty-eight half-rows in the reference, columns 0 to 27 of its
# fourteen lines, each half its colour's letter and a space off the disc.
REFERENCE_DISC = (
    "           mmmmmm           ",
    "        mmmMMMMMMmmm        ",
    "      mmMMMMMMMMMMMMmm      ",
    "     mmMMMMNNNNNNMMnnmm     ",
    "    mMMMMNNN....NNNnnnnm    ",
    "   mMMMNN..........NNnnnm   ",
    "  mmMMNN............NMnnmm  ",
    "  mMMNN....YYYYYY.Y..MMnnm  ",
    " mMMMN....YYxyyyXXYy..MnnNm ",
    " mMMN....YYxyy...Xxy...MNNm ",
    " mMMN....YXXy.....xy...MNNm ",
    "mMMNN....YXXX.....Yy...MMNNm",
    "mMMN.....YXXXXYY...y....MNNm",
    "mMMN......XXXXXXXY......MNNm",
    "mMMN.......xxXXXXXX.....MNNm",
    "mMMN........yyxXXXXx....MNNm",
    "mMMNN....Y.....yXXXxy..MMNNm",
    " mMMN....Yy......XXxy..MNNm ",
    " mMMN....YX......Yxxy..MNNm ",
    " mMnnN...YXX....YYxyy.MNNNm ",
    "  mnnNN..YyxxYYYYxyy.MMNNm  ",
    "  mmnnMM..y.yyyyyyy.MMNNmm  ",
    "   mnnnMM..........MMNNNm   ",
    "    mnnnnMMM....MMMNNNNm    ",
    "     mmnnNNMMMMMMNNNNmm     ",
    "      mmNNNNNNNNNNNNmm      ",
    "        mmmNNNNNNmmm        ",
    "           mmmmmm           ",
)
# The reference's colours by letter, the owner's `seal28.py`'s nine.
REFERENCE_COLOURS = {
    "m": (150, 24, 28),
    "M": (208, 68, 64),
    "n": (160, 30, 34),
    "N": (96, 10, 14),
    ".": (112, 16, 20),
    "X": (186, 38, 42),
    "Y": (222, 86, 78),
    "x": (90, 8, 12),
    "y": (84, 8, 12),
    " ": None,
}


def test_a_real_runs_stamp_is_the_owners_reference_cell_for_cell():
    """#832 S1-S4 against the picture the owner chose rather than against a
    rule: the stamp over the rows the reference was drawn over is the
    reference — 14 lines, the disc's grid at column 0 and half-row 0, each of
    its 784 half-cells the reference's colour or off the disc, the twin the
    reference's letters line for line, and the block form's text, codes
    stripped, the twin's with the owner's characters in place. The block
    form leads its `·` dim where the reference left it plain, which is the
    owner's decision 6's wording, and the reference is a picture of it.

    A real run's message is its label and its block and nothing else."""
    mod = stamp_module()
    letter = mod.compose(REFERENCE_ROWS)
    assert (letter.height, letter.width, letter.disc) == (14, 77, (0, 0, 28, 28))
    assert mod.stamp(REFERENCE_ROWS, shape=True) == list(REFERENCE_TWIN)
    for y, said in enumerate(REFERENCE_DISC):
        line = letter.cells[y // 2]
        for x, key in enumerate(said):
            # A line ends at its last visible cell, so past it is off the disc.
            char, fg, bg, _style = line[x] if x < len(line) else (None,) * 4
            top, bottom = (fg, bg) if char == "▀" else (bg, fg)
            half = top if y % 2 == 0 else bottom
            assert half == REFERENCE_COLOURS[key], (x, y, key, char, fg, bg)
    blocks = [mod.strip_ansi(line) for line in mod.stamp(REFERENCE_ROWS)]
    ascii_ = str.maketrans({"·": ".", "✓": "+", "─": "-", "→": ">"})
    for line, twin in zip(blocks, REFERENCE_TWIN, strict=True):
        assert len(line) == len(twin), (line, twin)
        text = line.translate(ascii_)
        same = zip(text, twin, strict=True)
        assert all(a == b for a, b in same if a not in "▀▄"), (line, twin)
    label = mod.label(full_values())
    assert mod.fitted([(label, FULL_ROWS)]) == "\n".join(
        [label, *mod.stamp(FULL_ROWS, shape=False)]
    )


def test_two_files_in_one_turn_are_under_the_budget_together(tmp_path):
    """A3, two files, under the owner's rule of 2026-10-02 (`questions.md`
    Q6). Two stamps of a real run's size do not fit one message together
    even at the last rung, so the old rule drew both with no disc. The disc is kept
    now: the first is drawn whole with its disc, the second stays pending
    under its own name, and the next `Stop` draws it whole — two turns,
    each message under the budget. The name is the case's from phase 1,
    kept because round 1's record cites it.

    Whether two real runs share a message is a fact about the drawing, and
    the emblem sets it (#832): under #717's lily two did not fit at 0.75, and
    under the interim ring of work item 1791270164 they did
    (`phases/phase-1.md` there has the sizes). The second run therefore
    carries deferral homes, one at a time, until the pair does not fit with
    their discs — none under the lily or under phase 2's §, where this is
    the case as it stood, and some under the owner's 14-cell disc, where two
    real runs share a message — and the premise is asserted rather than
    assumed."""
    mod = stamp_module()
    repo = opted_in(tmp_path)
    label = mod.label(full_values())
    budget = mod.MESSAGE_BUDGET
    alone = len(drawn(mod, label, FULL_ROWS))
    homes = []
    while alone + 2 + len(drawn(mod, label, FULL_ROWS + homes)) <= budget:
        homes.append(("", f"home-{len(homes)}"))
    rows = FULL_ROWS + homes
    late = {**full_values("ccc3333c"), "rows": rows}
    assert len(drawn(mod, mod.label(late), rows)) <= budget, (
        "the second no longer fits with its disc alone",
        len(homes),
    )
    first = mod.write_values(str(repo / ".git"), "s-1", full_values(), now=1)
    second = mod.write_values(str(repo / ".git"), "s-1", late, now=2)
    text = json.loads(stop(repo))["systemMessage"]
    assert len(text) <= mod.MESSAGE_BUDGET, len(text)
    assert text == drawn(mod, label, FULL_ROWS), "not the first, whole"
    assert os.path.exists(mod.drawn_path(first)) and not os.path.exists(first)
    assert os.path.exists(second), "the second was claimed with the first"
    later = json.loads(stop(repo))["systemMessage"]
    assert later == drawn(mod, mod.label(late), rows)
    assert os.path.exists(mod.drawn_path(second)) and not os.path.exists(second)
    assert stop(repo) == "", "a drawn file was drawn a second time"


def test_seals_past_what_one_message_carries_wait_for_the_next_turn(tmp_path):
    """A3, any set — round 1's 🟡 1. Twelve files of a real run's size were
    all claimed and printed at once with no disc, 15,000 characters and more,
    which the harness persists. Now each `Stop` draws the oldest that fit
    with their disc, under `MESSAGE_BUDGET`, and leaves the rest pending in
    order; the next `Stop` takes the next, so twelve turns draw all twelve
    and none is drawn without its disc."""
    mod = stamp_module()
    repo = opted_in(tmp_path)
    # `now` of one width: the name sort is oldest first because a real time
    # in nanoseconds always has the same number of digits.
    paths = [
        mod.write_values(str(repo / ".git"), "s-1", full_values(f"{n:08x}"), now=n)
        for n in range(101, 113)
    ]
    before = 0
    for turn in range(1, 13):
        text = json.loads(stop(repo))["systemMessage"]
        assert len(text) <= mod.MESSAGE_BUDGET, (turn, len(text))
        blocks = text.split("\n\n")
        assert all("\x1b[38;2;" in b for b in blocks), f"turn {turn} lost a disc"
        drawn_now = [p for p in paths if os.path.exists(mod.drawn_path(p))]
        waiting = [p for p in paths if os.path.exists(p)]
        assert drawn_now == paths[: len(drawn_now)], "not oldest first"
        assert waiting == paths[len(drawn_now) :], "a file was lost"
        assert len(drawn_now) >= turn, f"turn {turn} drew nothing new"
        # A claim renames the file whether or not its stamp is printed, so
        # the drawn names alone cannot see a file claimed and dropped: the
        # message's labels are exactly the files this turn claimed.
        assert [b.split("\n", 1)[0] for b in blocks] == [
            mod.label(full_values(f"{n:08x}"))
            for n in range(101 + before, 101 + len(drawn_now))
        ], f"turn {turn} claimed a file its message does not carry"
        before = len(drawn_now)
        if not waiting:
            break
    assert stop(repo) == "", "something was left to draw"


def test_one_seal_too_large_for_the_disc_is_drawn_alone_without_it(tmp_path):
    """A4's last rung, under the owner's rule. A record whose stamp does not
    fit the budget with its disc by itself — a
    long list of deferral homes — is the one case the text block is drawn
    with no disc, and it is drawn alone: the first pending file is always drawn, so
    the queue cannot stall, and the seal after it waits for the next `Stop`
    rather than losing its disc.

    The record carries deferral homes, one at a time, until its stamp does
    not fit with its disc: sixty did under phase 2's § of #832, and under
    the owner's 14-cell disc sixty fit, so the count is derived and the
    premise asserted rather than assumed."""
    mod = stamp_module()
    repo = opted_in(tmp_path)
    label = mod.label(full_values())
    homes = []
    while len(drawn(mod, label, FULL_ROWS + homes)) <= mod.MESSAGE_BUDGET:
        homes.append(("", f"home-{len(homes)}"))
    big = {**full_values(), "rows": FULL_ROWS + homes}
    oversized = mod.write_values(str(repo / ".git"), "s-1", big, now=1)
    after = mod.write_values(str(repo / ".git"), "s-1", full_values("ccc3333c"), now=2)
    assert mod.label(big) == label
    assert len(drawn(mod, label, big["rows"])) > mod.MESSAGE_BUDGET
    text = json.loads(stop(repo))["systemMessage"]
    assert text == drawn(mod, label, big["rows"], False), "not the text block alone"
    assert "\x1b[38;2;" not in text, "the oversized seal drew a disc"
    assert os.path.exists(mod.drawn_path(oversized)) and os.path.exists(after)
    later = json.loads(stop(repo))["systemMessage"]
    assert later == drawn(mod, mod.label(full_values("ccc3333c")), FULL_ROWS)


def test_a_character_outside_the_bmp_is_counted_as_two():
    """The round-1 question, measured in the fix pass: the harness counts a
    `systemMessage` in UTF-16 units, so 5,001 U+1D54F (10,002 units) were
    persisted where 4,999 were shown. Python's `len` counts each as one, so
    a label of them fitted a rung the harness would not. A budget between
    the two counts steps the block down — since #832 to the text block alone,
    the one step after the disc."""
    mod = stamp_module()
    label = LABEL + " " + "\U0001d54f" * 50
    at = {disc: drawn(mod, label, ROWS, disc) for disc in (True, False)}
    assert len(at[True].encode("utf-16-le")) // 2 == len(at[True]) + 50
    assert mod.fitted([(label, ROWS)], len(at[True]) + 10) == at[False]
    assert mod.fitted([(label, ROWS)], len(at[True]) + 50) == at[True]
    # A values file is JSON, which can carry a lone surrogate; counting it
    # must not raise, or every pending file would wait forever.
    lone = LABEL + "\ud800"
    assert mod.fitted([(lone, ROWS)]) == drawn(mod, lone, ROWS)


def test_a_values_file_from_an_older_gate_draws_every_row_in_the_new_layout(
    tmp_path,
):
    """A13. A file the gate wrote from #666 to #717 carries `null` blanks, a
    `chain` row, `exit 0` under the suite and `0 drifted . 0 broken` under
    the ledger, the base's ref on a row of its own and ` . ` between parts,
    and may still be pending when this hook draws it. Since #832 nothing
    converts it (`spec.md` §*Out* of work item 1791270164): every row it
    carries is drawn as text in the open layout, one line each and in order,
    its blanks as blank lines, under `label(values)`, with its disc.
    #717's name for this case said the blanks drew no line, which the sheet
    did; the open layout draws them, as `panel`'s own `None` is drawn."""
    mod = stamp_module()
    repo = opted_in(tmp_path)
    old = {**full_values(), "rows": OLD_ROWS}
    mod.write_values(str(repo / ".git"), "s-1", old)
    text = json.loads(stop(repo))["systemMessage"]
    label, *lines = text.split("\n")
    assert label == mod.label(old)
    assert lines == mod.stamp(OLD_ROWS, shape=False), "not the drawing with its disc"
    said = [mod.strip_ansi(line)[31:] for line in lines]
    rows = OLD_ROWS[1:]
    assert len(said) == max(14, 2 + len(rows)), len(said)
    top = (len(said) - 2 - len(rows)) // 2
    assert said[top].startswith("SEALED ─"), said[top]
    for k, row in enumerate(rows, top + 2):
        want = "" if row is None else f"{row[0]:<7} {row[1]}".rstrip()
        assert said[k] == want, (k, said[k], want)


def test_the_ladder_steps_down_in_order_and_ends_with_no_disc():
    """A4, over the two rungs #853 left. Driven at small budgets: the block
    with its disc where it fits, then the panel with no disc — which is
    returned whatever the budget, because nothing comes after it. Oldest
    first (`questions.md` Q6 of #717): a newer block that does not fit
    beside the older waits rather than losing its disc, because no smaller
    disc is drawn."""
    mod = stamp_module()
    at = {disc: drawn(mod, LABEL, ROWS, disc) for disc in (True, False)}
    assert len(at[True]) > len(at[False]), (len(at[True]), len(at[False]))
    one = [(LABEL, ROWS)]
    assert mod.fitted(one, len(at[True])) == at[True]
    assert mod.fitted(one, len(at[True]) - 1) == at[False]
    assert mod.fitted(one, 0) == at[False], "the last rung is the last"
    assert mod.fitted([]) == "" and mod.admitted([], 0) == []
    bare = mod.strip_ansi(at[False])
    assert "▀" not in bare and "▄" not in bare, "the last rung drew a disc"
    for row in ROWS[1:]:
        if row is not None:
            assert f"{row[0]:<7} {row[1]}".strip() in bare, row
    # Two blocks that fit together are one message; where the newer does not
    # fit beside the older, it is left out rather than both losing the disc.
    two = [(LABEL, ROWS), (LABEL, ROWS)]
    room = len(at[True]) * 2 + 2
    assert mod.fitted(two, room) == at[True] + "\n\n" + at[True]
    assert mod.admitted(two, room - 1) == [at[True]], "both drawn, or not whole"
    # Oldest first: a newer seal that would fit is not drawn ahead of an
    # older one that does not, which the hook would claim and not print.
    huge = (LABEL, ROWS + [("", f"home-{k}") for k in range(60)])
    plain = (LABEL, ROWS)
    assert mod.admitted([plain, huge, plain], room) == [at[True]], (
        "drawn past a seal that waits"
    )
    # A single seal exactly at the budget keeps its disc.
    assert mod.admitted([(LABEL, ROWS)], len(at[True])) == [at[True]]


def test_admitteds_docstring_fits_the_line_length():
    """S13 (#721). Round 3 of #717 reflowed one line of `admitted`'s
    docstring to 113 columns; the paragraph is round 3's paste-ready one,
    and no line of the docstring is wider than 79 as the source holds it —
    read from the source, because Python 3.13 strips a docstring's indent
    from `__doc__` and 3.12 keeps it. Seen red against the 113-column line."""
    source = inspect.getsource(stamp_module().admitted)
    doc = source.split('"""', 2)[1]
    wide = [line for line in source.splitlines() if line in doc and len(line) > 79]
    assert wide == [], wide


def stamp_section():
    """`docs/the-review-record.md` §*The stamp*, flattened: the stamp's rules
    stand beside the verdict they are drawn from since #975, and
    `docs/the-broad-gate.md` keeps none of them."""
    text = flat("docs", "the-review-record.md")
    assert "## Where the stamp is drawn" not in flat("docs", "the-broad-gate.md")
    section = text.split("## The stamp ", 1)[1]
    assert text.index("## The guarantee") < text.index("## The stamp ")
    return section.split("## The run", 1)[0]


def test_the_policy_states_the_budget_and_names_its_case():
    """A18. `docs/the-review-record.md` §*The stamp* carries the budget rule
    under #717's marker, and its `Enforced by:` line names A3's case; the
    marker stands a second time over the paragraph nothing enforces. #832
    and #853: the rule names the two rungs, with the disc and the text block
    alone, the owner's disc 28 cells across, and one real run to a message;
    the unchecked paragraph says nothing outside the disc is painted, so the
    stamp is read in the terminal's own theme, where it gave the parchment's
    contrast figures before decision 6 of work item 1791270164 retired the
    sheet. The section moved from `docs/the-broad-gate.md` with #975."""
    text = stamp_section()
    marker = "<!-- specs/1790913304-the-seal-stamp-is-a-letter-with-the-seal-on-its-corner -->"
    assert text.count(marker) == 2, "the rule and the unchecked half, one marker each"
    unchecked = text.split(marker)[2]
    assert "**What the person's screen shows is not checked" in unchecked
    assert (
        "So is how the stamp reads on a light background as well as a dark one. "
        "Nothing outside the disc is painted, so its text is in the terminal's "
        "own colours and theme"
    ) in unchecked
    assert "1.02 and 1.48" not in unchecked and "parchment" not in unchecked
    rule = text.split(marker)[1].split("<!--", 1)[0]
    assert "**The hook holds its whole message under a budget named in the code" in rule
    assert "::test_the_hooks_message_is_under_the_budget_for_one_file" in rule
    # Round 1's 🟡 1, under the owner's rule of 2026-10-02 (`questions.md` Q6).
    assert "A seal past what one message can carry stays pending" in rule
    assert "::test_seals_past_what_one_message_carries_wait_for_the_next_turn" in rule
    assert "a character outside the BMP is two" in rule
    # #832 and #853: two rungs, with the disc and without it — and the reason
    # is the owner's 28-cell disc having one size, not a smaller disc refused.
    assert "A stamp has two rungs, with its disc and then without it" in rule
    assert (
        "the owner's disc is drawn 28 cells across and has one size, so there "
        "is no smaller disc to step to, and since #853 no scale either"
    ) in rule
    assert "0.90" not in rule and "at every scale" not in rule
    assert "one stamp of a real work item's size goes out per message" in rule
    assert "does not fit with its disc by itself is the only one drawn" in rule
    assert "as the text block with no disc" in rule
    assert "0.80 and 0.75" not in rule and "at 0.75 by itself" not in rule
    assert "24 cells" not in rule and "§ fragment" not in rule
    assert "14 cells" not in rule and "sheet" not in rule
    assert "The gate's own terminal drawing" not in rule, "the gate draws nothing"


# --- S16: the rules are where they are read ----------------------------------


def test_the_orchestrator_is_told_the_stamp_is_drawn_for_it():
    """S16, the orchestrator's half (contract §14), and #975 S13. The rule
    sits in the section that spawns the sealer: the stamp is drawn at the end
    of the turn in which the sealer's `sealed` guarantee is committed, the
    result text comes first, the orchestrator draws none — by `seal-stamp` or
    by relaying a log, which 0.15.6 did — the broad run's lines are quoted as
    `BROAD GATE PASSED` and `BROAD GATE FAILED`, and no line of the run says
    `SEALED`. 1792363231 S7: in local mode the stamp is drawn at the end of
    the turn in which the sealer's report arrives, and the line to quote is
    the edit hook's message."""
    text = flat("skills", "code-review", "orchestration.md")
    section = text.split("## Orchestrator: the pull request opens before round 1", 1)[1]
    section = section.split("## Orchestrator: verify before posting", 1)[0]
    for said in (
        "**The stamp is drawn for you at the end of the turn in which "
        "`guarantee.md` reading `sealed` is committed, or in local mode the turn "
        "in which the sealer's report arrives, and you never draw one (#975).**",
        "In local mode no commit carries `guarantee.md`: the sealer's own "
        "`Write` of it queues the values, and the line arrives as the edit "
        "hook's message",
        "The broad run draws nothing: its stdout opens `BROAD GATE PASSED` or "
        "`BROAD GATE FAILED`",
        "So put the result text first",
        "Draw none yourself, neither with `seal-stamp` nor by relaying a log.",
        "On a red run relay the `BROAD GATE FAILED` lines.",
        # Round 1's 🟡 1 of #400: the command is named on the line that points
        # at a values file, and it stays the person's wherever it appears.
        "Wherever the commit's line or the edit hook's message names "
        "`seal-stamp --from`, quote it as it stands: that command is the "
        "person's to type, and never yours.",
    ):
        assert said in section, said
    assert "SEALED" not in section, "a line of the broad run is quoted as SEALED"


def test_the_form_bullet_says_what_draws_the_final_seal():
    """S16, `verify`'s half, and #975 S13. The **Form** bullet said
    `broad-gate` draws the stamp when every check passed; the stamp is the
    sealer's now, drawn once per work item from its `sealed` guarantee at
    that file's commit, and the gate draws nothing. 1792363231 S7: in local
    mode, at its write."""
    text = flat("skills", "verify", "SKILL.md")
    assert "`broad-gate` prints the disc on success alone" not in text
    assert "`broad-gate` draws the stamp" not in text
    for said in (
        "the stamp is drawn from the sealer's `guarantee.md` reading `sealed`, "
        "once per work item",
        "git's `post-commit` writes the values it is drawn from, or in local "
        "mode the edit hook does at the file's write",
        "the `Stop` hook draws them in the orchestrator's session",
        "The broad gate draws nothing",
    ):
        assert said in text, said


def test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does():
    """S16, the policy's half, and #975 S10 and S13. `docs/the-review-record.md`
    §*The stamp* carries the drawing rule under #400's and #975's markers
    with an `Enforced by:` line naming the cases that queue and draw it, and
    a second statement saying what the screen shows is enforced by nothing.
    That statement names every place the hook is silent — a foreign hooks
    slot, a `python3` that cannot load `seal_stamp.py`, a main session
    outside the clone, a plugin older than the hook — and `seal-stamp --from
    <path>` for where a file was written.

    1792363231 S7 and S8: the rule names both triggers, the commit in shared
    mode and the write in local mode, with the local facts that hold once
    per work item. The unchecked paragraph no longer names local mode among
    the silences, and no longer hands the never-twice gap to an issue: it
    names a local guarantee that arrived other than by `Write` or `Edit`, a
    verdict over a commit off the work item's branch, and the limits the
    refusal record leaves. Red against the paragraph at 769f2aa4."""
    text = stamp_section()
    marker = "<!-- specs/1790562543-the-stamp-reaches-the-person-it-is-drawn-for -->"
    ours = "<!-- specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict -->"
    assert text.count(marker) == 2, "the rule and the unchecked half, one marker each"
    assert text.count(ours) == 2, "the rule and the unchecked half, one marker each"
    rule, unchecked = text.split(marker)[1:3]
    assert (
        "**The stamp is drawn once per work item, from the sealer's `sealed`, at "
        "the end of the turn in which `guarantee.md` came to read it: at its "
        "commit in shared mode, and at its write in local mode.**"
    ) in rule
    for local in (
        "`hooks/sealer-stamp-queue.py`",
        "after each `Write` or `Edit` of a local root's `specs/<id>/guarantee.md`",
        "an ancestor of the branch the work item's `routing.md` names in its "
        "`Branch` row",
        "the root and the values directory share the common dir",
        "`settle` retires no local-mode work item",
    ):
        assert local in rule, local
    for case in (
        "::test_a_local_mode_sealed_guarantee_queues_one_stamp",
        "::test_a_local_mode_second_sealed_queues_nothing",
        "::test_a_local_mode_guarantee_off_its_branch_queues_nothing",
        "::test_the_edit_gate_leaves_shared_mode_to_post_commit",
        "::test_the_edit_gate_queues_a_local_mode_sealed_guarantee",
        "::test_a_subagents_write_queues_and_draws_nothing",
        "::test_the_edit_gate_is_silent_off_a_guarantee",
    ):
        assert case in rule, case
    # #975 round 6's finding 1: the double-stamp limit is stated where the
    # rule is, as the class `sealed_before` cannot see, with its reason.
    assert "draws the stamp again in that clone" in rule, (
        "the double-stamp limit is stated where the rule is"
    )
    assert "the history is the only record the rule reads" in rule, (
        "the limit says why it is one"
    )
    # #975 round 7's finding 1: the limit names the clone it holds in. The
    # clone that drew the stamp keeps its values file, and an amend there
    # queues nothing (`test_a_recommit_of_the_same_guarantee_queues_no_second_file`).
    assert "in a clone that holds no values file for the work item" in rule, (
        "the limit names the clone it holds in"
    )
    for case in (
        "::test_a_sealed_guarantees_commit_queues_one_stamp",
        "::test_a_withheld_or_undecided_guarantee_queues_nothing",
        "::test_a_second_sealed_verdict_queues_nothing",
        "::test_a_recommit_of_the_same_guarantee_queues_no_second_file",
        "::test_the_main_sessions_stop_draws_each_undrawn_file_once",
    ):
        assert case in rule, case
    assert "**What the person's screen shows is not checked" in unchecked
    assert "Enforced by: nothing — no case, hook or workflow can observe a screen" in (
        unchecked
    )
    # Round 1's 🟡 1 of #400: the hook's silence where it cannot draw is
    # stated where a person looks for why no stamp appeared, with the way to
    # draw it.
    assert "**Nor is the hook's silence where it cannot draw.**" in unchecked
    for silence in (
        "where git's hooks slot is somebody else's",
        "by a shell write or `seal import`",
        "a verdict over a commit off the work item's branch",
        "in a clone other than the one that refused",
        "introduced by an amend, a rebase or a cherry-pick",
        "a patch-equivalent copy in the history",
        "a clone whose reflog is off",
        "cannot load `seal_stamp.py`",
        "outside the clone the stamp was queued in",
        "predates the hook",
    ):
        assert silence in unchecked, silence
    assert "names `seal-stamp --from <path>`" in unchecked
    assert (
        "In local mode the line reaches the person as the edit hook's message, "
        "and nobody has watched that message on a screen yet."
    ) in unchecked
    for gone in (
        # Spelled in two pieces, so S8's `git grep` for the pointer finds the
        # policy clean and not this check on it.
        "#" + "976",
        "in local mode, where the `seal/` root sits under the git directory",
        "already read `sealed` and that verdict drew nothing",
    ):
        assert gone not in text, gone
    assert "`SEALED` line" not in text, "the gate's line is quoted as SEALED"
    assert "the stamp says which copy drew it" not in text


def test_the_policy_states_the_refusal_record_and_names_its_cases():
    """1792363231 S8. §*The stamp* carries the refusal record as a rule of
    its own under this work item's marker: a `sealed` a writer refused
    leaves a record in the clone, the once readers skip it, so the repair
    draws the work item's one stamp. It names the guards the build holds,
    three, and its `Enforced by:` line names the cases phase 3 planted."""
    text = stamp_section()
    marker = "<!-- specs/1792363231-a-local-mode-work-item-draws-no-stamp -->"
    assert marker in text
    rule = text.split(
        "**A `sealed` a writer refused leaves a refusal record in the clone", 1
    )[1].split("<!--", 1)[0]
    for said in (
        "`<git-common-dir>/specseal-stamp-refused/<id>-<target>`",
        "`sealed_before` and the `Target SHA` row's earlier-run chain skip",
        "at least seven characters",
        "three things must hold",
        "a plain `commit:` or `commit (initial):`",
        "HEAD's side holds no patch-equivalent copy of it",
        "where the `Branch` row's branch stands",
    ):
        assert said in rule, said
    assert "four guards" not in rule, "the build holds three"
    for case in (
        "::test_a_seal_this_clone_refused_does_not_count_as_stamped",
        "::test_a_refusal_record_skips_only_its_own_verdict",
        "::test_a_seal_over_a_commit_off_the_branch_then_repaired_draws_once",
        "::test_a_local_mode_seal_refused_off_its_branch_then_resealed_draws_once",
        "::test_a_conflicted_rebase_in_another_clone_writes_no_refusal",
        "::test_an_amend_in_a_fresh_clone_writes_no_refusal",
        "::test_a_body_edit_over_a_rewritten_seal_writes_no_refusal",
        "::test_a_seal_whose_target_has_a_copy_writes_no_refusal",
        "::test_guard_two_reads_what_post_commit_sees_in_the_reflog",
    ):
        assert case in rule, case


def test_both_readmes_list_the_stamp_hook():
    """Round 1's 🟡 4. The hook inventory a user reads to learn what runs on
    their machine did not list the `Stop` hook, in either edition: the gate
    table, the opt-in list, the count of gates that wake on a condition, and
    the side effects. The editions move together, so both are read.

    1792363231 S7: the gate that queues a local-mode stamp at the write has its own
    row, and the count and the opt-in list that row made false say twelve
    gates and two stamp hooks."""
    for edition, count, opt_in, effects, clause in (
        (
            "README.md",
            "Nine of the twelve gates",
            # The opt-in list's own words: the count sentence names the stamp
            # hooks too, so the bare name would pass with the list unchanged.
            "the two implementer hooks, the two stamp hooks and the version check.",
            "Four side effects",
            # The clause's own words (round 2's ⬜ 2): the gate-table row
            # carries `specseal-stamp/` too, so the bare directory passed
            # with the side effect deleted.
            "`<git-common-dir>/specseal-stamp/`, which the stamp hook renames "
            "once drawn and nothing prunes",
        ),
        (
            "README.ko.md",
            "게이트 열둘 중 아홉",
            "구현자 훅 둘, 도장 훅 둘, 버전 확인이다.",
            "네 가지 부수 효과",
            "도장 훅은 그린 뒤 그 파일의 이름을 바꿀 뿐 지우지 않습니다",
        ),
    ):
        text = flat(edition)
        for gate in ("sealer-stamp", "sealer-stamp-queue"):
            table = [ln for ln in text.split("| ") if ln.startswith(f"{gate} ")]
            assert table, f"{edition}'s gate table has no `{gate}` row"
        assert count in text, (edition, count)
        assert opt_in in text, (edition, opt_in)
        assert effects in text and clause in text, (edition, effects, clause)
        for gone in ("Seven of the ten", "게이트 열 중 일곱", "Eight of the eleven"):
            assert gone not in text, (edition, gone)
        assert "게이트 열하나 중 여덟" not in text, edition
    # #975 S11: both editions say the stamp's values are written at the
    # commit of a sealed guarantee, and neither says the broad gate leaves
    # them. 1792363231 S7: or, in local mode, at its write; and the refusal
    # record's directory stands beside the values' among the side effects.
    for edition, said, gone in (
        (
            "README.md",
            (
                "queued at the commit of a work item's `guarantee.md` reading "
                "`sealed`, or in local mode at its write",
                "the commit of a `guarantee.md` reading `sealed`, or in local mode "
                "its write, writes the stamp's values under",
                "a `sealed` the plugin refused leaves an empty file under "
                "`<git-common-dir>/specseal-stamp-refused/`",
            ),
            ("the broad gate left for this session", "a sealed broad-gate run writes"),
        ),
        (
            "README.ko.md",
            (
                "작업 항목의 `guarantee.md` 가 `sealed` 로 커밋될 때, local 모드에서는 "
                "그렇게 쓰일 때 남는",
                "`sealed` 로 읽히는 `guarantee.md` 를 커밋하면, local 모드에서는 그렇게 "
                "쓰면 도장에 들어갈 값을",
                "플러그인이 거절한 `sealed` 는 `<git-common-dir>/specseal-stamp-refused/` "
                "아래에 빈 파일을 남깁니다",
            ),
            ("광역 관문이 이 세션 앞으로", "광역 관문 실행은 도장에 들어갈 값을"),
        ),
    ):
        text = flat(edition)
        for phrase in said:
            assert phrase in text, (edition, phrase)
        for phrase in gone:
            assert phrase not in text, (edition, phrase)


# --- S16: the sealer is told it draws nothing --------------------------------


def flat(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as handle:
        return " ".join(handle.read().split())


def test_the_sealer_is_told_the_gate_draws_nothing_and_neither_does_it():
    """S16, the sealer's half (contract §14). `agents/sealer.md` said the
    drawing arrives as letters and to pass it through, which the 0.15.6 run
    did — every seal behind `ctrl+o`. Since #969 the sealer runs no gate, so
    there is no line of the gate's for it to pass on: it says it draws no
    stamp. Since #975 the stamp is drawn in the orchestrator's session from
    the sealer's own committed `sealed` verdict, once per work item, and
    never from the orchestrator's run; the old instructions are gone."""
    text = flat("agents", "sealer.md")
    for said in (
        "or draw a stamp",
        "a stamp is drawn once from your `sealed`.",
    ):
        assert said in text, said
    # 1792363231 S9: a local-mode verdict is never committed.
    assert "your committed `sealed`" not in text
    assert "from its own run" not in text, "the stamp is not the run's"
    assert "seal-stamp --from" not in text, (
        "the sealer is told to pass on a stamp command from a run it did not take"
    )
    assert "the drawing arrives as letters" not in text
    assert "pass it through as it came" not in text
    # Round 1's ⬜ 6: no gate draws in a sealer, so the `gate` row says which
    # copy measured the tree, not which drew the stamp.
    assert "which gate drew the stamp" not in text


# --- S13: the scale, retired (#853) -----------------------------------------


def test_the_stamp_says_why_it_has_no_scale_and_neither_command_offers_one():
    """S13 (#853). The comment where the scale stood says there is none and
    why — the disc has one size since #832 — so the next reader does not
    look for the dial; `seal-stamp` with no argument draws the sample, and
    neither command's help names a scale."""
    mod = stamp_module()
    with open(STAMP, encoding="utf-8") as handle:
        source = " ".join(handle.read().replace("#", " ").split())
    assert "There is no scale ( 853)." in source, "the retirement is not said"
    assert "the disc is `DISC_CELLS` across whatever a scale said" in source
    out = seal_stamp("--shape")
    assert out.returncode == 0, out.stderr
    assert out.stdout == "\n" + "\n".join(mod.stamp(mod.SAMPLE_ROWS, True)) + "\n\n"
    for command in ([sys.executable, STAMP], [sys.executable, GATE]):
        help_text = subprocess.run(
            [*command, "--help"],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
        ).stdout
        assert "scale" not in help_text, help_text
