"""`hooks/commitgate.py`'s guarantee arm and its stamp, one class per function.

Written anew from the code by #942's phase 6; the old cases of
`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` were read for
their inputs. `guarantee_off_history`, `pre_commit` and `post_commit` run in
the process over one world built for the module: an opted-in repository on
`feat/x` whose work item holds two round records, `broad-gate.md`, a
`guarantee.md` reading `withheld` and a `routing.md` naming the branch, each
committed. Each case takes a copy and stages or commits in it. The commit
gate's other readings, the waiver, the mark and the backstop, run as git runs
them in the commit flow, `tests/e2e/commit/test_commit_flow.py`.
"""

import io
import os
import shutil
import subprocess
import sys

import pytest
from conftest import (
    ROOT,
    STAMP_ITEM,
    census_case,
    commit_everything_as_e,
    git,
    git_out,
    guarantee_record,
    load_module,
    queued_values,
    routing_record,
)

TARGET = "hooks/commitgate.py"


def _commitgate():
    """`hooks/commitgate.py`, which imports its siblings by their plain names,
    as `hooks/git/post-commit.py` puts them on the path."""
    hooks = os.path.join(ROOT, "hooks")
    if hooks not in sys.path:
        sys.path.insert(0, hooks)
    return load_module(os.path.join(hooks, "commitgate.py"), "commitgate_under_test")


commitgate = _commitgate()
gate = commitgate.gate

ITEM_ID = STAMP_ITEM.split("-")[0]
GUARANTEE_REL = f"seal/specs/{STAMP_ITEM}/guarantee.md"
ROUTING_REL = f"seal/specs/{STAMP_ITEM}/routing.md"
REFUSED = "specseal-stamp-refused"
SIGNED = ("-c", "user.name=e", "-c", "user.email=e@example.com")
TEMPLATE = os.path.join(ROOT, "templates", "sdd-guarantee.md")


@pytest.fixture(scope="module")
def _world(tmp_path_factory):
    """The declared work item, built once: (repo, target, base)."""
    repo = tmp_path_factory.mktemp("commitgate-world") / "repo"
    repo.mkdir()
    git(repo, "init", "-q", "-b", "main")
    (repo / "seal").mkdir()
    (repo / "seal" / "config.md").write_text("# config\n", encoding="utf-8")
    commit_everything_as_e(repo, "x")
    git(repo, "switch", "-qc", "feat/x")
    item = repo / "seal" / "specs" / STAMP_ITEM
    (item / "rounds").mkdir(parents=True)
    for n in (1, 2):
        (item / "rounds" / f"round-{n}.md").write_text("x\n", encoding="utf-8")
    commit_everything_as_e(repo, "the rounds")
    target = git_out(repo, "rev-parse", "--short", "HEAD")
    base = git_out(repo, "rev-parse", "--short", "main")
    (item / "broad-gate.md").write_text(
        f"| Field | Value |\n|---|---|\n| Broad gate | {target} against {base} |\n",
        encoding="utf-8",
    )
    (item / "guarantee.md").write_text(
        guarantee_record(target, base, "withheld reason: x"), encoding="utf-8"
    )
    commit_everything_as_e(repo, "the closing records")
    (item / "routing.md").write_text(routing_record(), encoding="utf-8")
    commit_everything_as_e(repo, "the routing")
    return repo, target, base


@pytest.fixture
def world(tmp_path, _world):
    """This case's copy: (repo, target, base)."""
    repo, target, base = _world
    copy = tmp_path / "repo"
    shutil.copytree(repo, copy)
    return copy, target, base


def short(repo, ref="HEAD"):
    return git_out(repo, "rev-parse", "--short", ref)


def staged(repo, text, name="guarantee.md"):
    """The work item's NAME rewritten to TEXT and staged, uncommitted."""
    (repo / "seal" / "specs" / STAMP_ITEM / name).write_text(text, encoding="utf-8")
    git(repo, "add", "-A")


def paths_of(repo):
    """`pre_commit`'s listing of the staged paths."""
    return lambda: gate.lines(gate.git(["diff", "--cached", "--name-only"], str(repo)))


def off_branch_commit(repo):
    """A commit on top of `main` that no branch holds; its short SHA."""
    tree = git_out(repo, "rev-parse", "main^{tree}")
    sha = git_out(
        repo,
        *SIGNED,
        "commit-tree",
        tree,
        "-p",
        "main",
        "-m",
        "a commit no branch holds",
    )
    return sha[:7]


def refusals(repo):
    """The refusal records under REPO's git directory, by name."""
    try:
        return sorted(os.listdir(repo / ".git" / REFUSED))
    except OSError:
        return []


def before_the_commit(repo, session="s-1"):
    """(exit status, what it wrote) of `pre-commit` for a Claude session."""
    out = io.StringIO()
    environ = {"CLAUDE_CODE_SESSION_ID": session} if session else {}
    return commitgate.pre_commit(str(repo), environ, out), out.getvalue()


def after_the_commit(repo, session="s-1"):
    """What `post-commit` printed for a Claude session."""
    out = io.StringIO()
    assert (
        commitgate.post_commit(str(repo), {"CLAUDE_CODE_SESSION_ID": session}, out) == 0
    )
    return out.getvalue()


def sealed_and_committed(repo, target, base, message, earlier=""):
    """`guarantee.md` rewritten to read `sealed` over TARGET, committed."""
    staged(repo, guarantee_record(target, base, "sealed", earlier))
    commit_everything_as_e(repo, message)


@pytest.fixture
def loads(monkeypatch):
    """A recorder in front of `_stamp_module`, the arm's only way to
    `seal_stamp.py` and `chain_check.py`."""
    seen = []
    real = commitgate._stamp_module
    monkeypatch.setattr(commitgate, "_stamp_module", lambda: seen.append(1) or real())
    return seen


class Test_guarantee_off_history:
    @pytest.mark.parametrize(
        "wrong",
        [lambda repo: "deadbee", off_branch_commit],
        ids=["the-target-does-not-resolve", "the-target-is-off-the-branch"],
    )
    def test_refuses_a_sealed_over_a_commit_the_history_does_not_hold(
        self, world, wrong
    ):
        repo, _target, base = world
        off = wrong(repo)
        staged(repo, guarantee_record(off, base, "sealed"))
        head = git_out(repo, "rev-parse", "HEAD")
        text, ident, target = commitgate.guarantee_off_history(
            str(repo), head, paths_of(repo)
        )
        assert text == gate.guarantee_refusal(GUARANTEE_REL, off, "feat/x", short(repo))
        assert (ident, target) == (ITEM_ID, off)

    @pytest.mark.rule("refused-sealed-leaves-a-record")
    @pytest.mark.rule("sealed-off-the-branch-refused")
    @pytest.mark.parametrize(
        "written",
        [
            lambda t, h, b: guarantee_record(h, b, "sealed"),
            lambda t, h, b: guarantee_record(t, b, "sealed"),
            lambda t, h, b: guarantee_record("deadbee", b, "withheld reason: stale"),
            lambda t, h, b: (
                guarantee_record("deadbee", b, "sealed") + "\nVerdict: withheld\n"
            ),
            lambda t, h, b: guarantee_record("deadbee", b, "Sealed"),
            lambda t, h, b: open(TEMPLATE, encoding="utf-8").read(),
            lambda t, h, b: guarantee_record(
                t, b, "sealed", "; earlier run: deadbee sealed"
            ),
        ],
        ids=[
            "the-target-is-head",
            "the-target-is-an-ancestor",
            "withheld",
            "two-verdicts",
            "a-near-miss",
            "the-unfilled-template",
            "an-earlier-run-the-clone-does-not-hold",
        ],
    )
    def test_accepts_every_guarantee_but_one_sealed_off_the_history(
        self, world, written
    ):
        repo, target, base = world
        staged(repo, written(target, short(repo), base))
        head = git_out(repo, "rev-parse", "HEAD")
        assert commitgate.guarantee_off_history(str(repo), head, paths_of(repo)) is None

    @pytest.mark.parametrize(
        "unjudged",
        ["no-routing-in-the-index", "no-branch-row", "another-branch", "no-head"],
    )
    def test_accepts_a_sealed_off_the_history_it_has_no_declaration_to_judge_by(
        self, world, unjudged
    ):
        """A commit on any branch but the one the item's own `routing.md` in
        the index declares, a squash onto `main` among them, is not judged;
        nor is an unborn branch, which has no history to hold anything."""
        repo, _target, base = world
        head = git_out(repo, "rev-parse", "HEAD")
        if unjudged == "another-branch":
            git(repo, "switch", "-qc", "main-copy")
        staged(repo, guarantee_record("deadbee", base, "sealed"))
        if unjudged == "no-routing-in-the-index":
            git(repo, "rm", "-q", "--cached", ROUTING_REL)
        if unjudged == "no-branch-row":
            staged(repo, routing_record(None), name="routing.md")
        if unjudged == "no-head":
            head = ""
        assert commitgate.guarantee_off_history(str(repo), head, paths_of(repo)) is None

    def test_accepts_a_commit_that_stages_no_guarantee_without_loading_a_reader(
        self, world, loads
    ):
        repo, _target, _base = world
        (repo / "x.txt").write_text("more work\n", encoding="utf-8")
        git(repo, "add", "-A")
        head = git_out(repo, "rev-parse", "HEAD")
        assert commitgate.guarantee_off_history(str(repo), head, paths_of(repo)) is None
        assert loads == []

    def test_accepts_a_deleted_guarantee(self, world):
        repo, _target, _base = world
        git(repo, "rm", "-q", GUARANTEE_REL)
        head = git_out(repo, "rev-parse", "HEAD")
        assert commitgate.guarantee_off_history(str(repo), head, paths_of(repo)) is None


class Test_pre_commit:
    @pytest.mark.rule("refused-sealed-leaves-a-record")
    @pytest.mark.rule("sealed-off-the-branch-refused")
    @pytest.mark.parametrize(
        "wrong",
        [lambda repo: "deadbee", off_branch_commit],
        ids=["the-target-does-not-resolve", "the-target-is-off-the-branch"],
    )
    def test_refuses_a_sealed_off_the_history_and_records_the_refusal(
        self, world, wrong
    ):
        """1792363231 S11: exit 1, HEAD and the index as they were, the text
        naming the file, the commit, the branch, HEAD and the one way on, and
        the refusal recorded in this clone. The new audit's commit then lands
        and queues the work item's one stamp, its chain keeping the refused run
        as `; earlier run: <sha> sealed`."""
        repo, _target, base = world
        off = wrong(repo)
        staged(repo, guarantee_record(off, base, "sealed"))
        head = short(repo)
        index = git_out(repo, "write-tree")
        code, said = before_the_commit(repo)
        assert code == 1, said
        assert said == gate.guarantee_refusal(GUARANTEE_REL, off, "feat/x", head) + "\n"
        assert said.startswith(gate.HEADER + "\n\n"), said
        assert "spawn the sealer again at HEAD" in said
        assert "AskUserQuestion" not in said and "waive" not in said, said
        assert said.rstrip().endswith(gate.UNCHANGED), said
        assert (short(repo), git_out(repo, "write-tree")) == (head, index)
        assert refusals(repo) == [f"{ITEM_ID}-{off}"] and queued_values(repo) == []
        staged(
            repo, guarantee_record(head, base, "sealed", f"; earlier run: {off} sealed")
        )
        assert before_the_commit(repo) == (0, "")
        commit_everything_as_e(repo, "the sealer again at HEAD")
        assert after_the_commit(repo)
        (path,) = queued_values(repo)
        assert path.endswith(f"-{ITEM_ID}-{head}.json"), path

    def test_accepts_a_sealed_at_head_and_reaches_the_reader(self, world, loads):
        repo, _target, base = world
        staged(repo, guarantee_record(short(repo), base, "sealed"))
        assert before_the_commit(repo) == (0, "")
        assert loads == [1] and refusals(repo) == []

    @pytest.mark.parametrize(
        "broken",
        ["a-reader-that-will-not-load", "the-sequencers-own-commit", "no-session"],
    )
    def test_accepts_a_sealed_off_the_history_where_it_cannot_stand_on_the_fact(
        self, world, monkeypatch, broken
    ):
        """A `seal_stamp.py` that will not load stops nothing, because the pull
        request's check refuses the same file; nor does the commit git makes
        for its own rebase, or a commit no Claude session runs."""
        repo, _target, base = world
        staged(repo, guarantee_record("deadbee", base, "sealed"))
        session = "s-1"
        if broken == "a-reader-that-will-not-load":

            def loader():
                raise SyntaxError("a seal_stamp.py this python cannot load")

            monkeypatch.setattr(commitgate, "_stamp_module", loader)
        if broken == "the-sequencers-own-commit":
            monkeypatch.setattr(
                commitgate, "_sequencer_commit", lambda cwd, c=None: True
            )
        if broken == "no-session":
            session = ""
        assert before_the_commit(repo, session) == (0, "")
        assert refusals(repo) == []


class Test__record_refusal:
    def test_accepts_a_row_and_writes_its_record(self, world):
        repo, _target, _base = world
        commitgate._record_refusal(str(repo / ".git"), ITEM_ID, "deadbee")
        assert refusals(repo) == [f"{ITEM_ID}-deadbee"]

    def test_refuses_to_raise_where_the_record_cannot_be_written(
        self, world, monkeypatch
    ):
        repo, _target, _base = world

        def broken():
            raise OSError("read-only")

        monkeypatch.setattr(commitgate, "_stamp_module", broken)
        commitgate._record_refusal(str(repo / ".git"), ITEM_ID, "deadbee")
        assert refusals(repo) == []


class Test_post_commit:
    @pytest.mark.rule("stamp-drawn-once")
    def test_accepts_a_commit_carrying_a_sealed_and_queues_one_stamp(self, world):
        repo, target, base = world
        sealed_and_committed(repo, target, base, "the seal")
        said = after_the_commit(repo)
        (path,) = queued_values(repo)
        assert os.path.realpath(path) in said or path in said, said
        assert after_the_commit(repo) == "", "the stamp was queued twice"

    def test_refuses_a_commit_no_claude_session_runs(self, world):
        repo, target, base = world
        sealed_and_committed(repo, target, base, "the seal")
        out = io.StringIO()
        assert commitgate.post_commit(str(repo), {}, out) == 0
        assert out.getvalue() == "" and queued_values(repo) == []

    def test_refuses_to_raise_where_the_notice_or_the_stamp_will_not_load(
        self, world, monkeypatch
    ):
        repo, target, base = world
        sealed_and_committed(repo, target, base, "the seal")

        def no_notice():
            raise ImportError("an implementer-notice.py this python cannot load")

        def no_stamp():
            raise SystemExit(3)

        monkeypatch.setattr(commitgate, "_notice_module", no_notice)
        monkeypatch.setattr(commitgate, "_stamp_module", no_stamp)
        assert after_the_commit(repo) == ""

    @pytest.mark.rule("refused-sealed-leaves-a-record")
    @pytest.mark.parametrize(
        "bring",
        [
            ("merge", "--squash", "origin/feat/x"),
            ("checkout", "--", f"seal/specs/{STAMP_ITEM}"),
        ],
        ids=["merge-squash-onto-main", "checkout-from-a-commit-no-ref-holds"],
    )
    def test_refuses_to_queue_a_copy_of_a_sealed_item_onto_main(
        self, world, tmp_path, bring
    ):
        """Round 1's shapes: the item sealed and stamped in one clone, then
        brought onto `main` of a second clone by a plain command. The copy
        lands and queues nothing, nor does its re-seal. For the checkout,
        round 2's finding 2: every ref that held the sealing commit is deleted
        first, as `fetch --prune` after the merge leaves it, and the item is
        taken from that commit by its SHA."""
        repo, target, base = world
        sealed_and_committed(repo, target, base, "the seal")
        assert after_the_commit(repo)
        other = tmp_path / "other"
        subprocess.run(
            ["git", "clone", "-q", "--no-local", str(repo), str(other)], check=True
        )
        git(other, "switch", "-q", "main")
        picked = bring
        if bring[0] == "checkout":
            sha = git_out(other, "rev-parse", "origin/feat/x")
            git(other, "branch", "-q", "-D", "feat/x")
            git(other, "remote", "set-head", "origin", "-d")
            git(other, "update-ref", "-d", "refs/remotes/origin/feat/x")
            assert git_out(other, "for-each-ref", f"--contains={sha}") == ""
            picked = ("checkout", sha, *bring[1:])
        git(other, *SIGNED, *picked)
        head = git_out(other, "rev-parse", "HEAD")
        (other / ".git" / "specseal-reviewed").write_text(head, encoding="utf-8")
        assert before_the_commit(other) == (0, "")
        git(other, *SIGNED, "commit", "-qm", "the item brought over")
        assert after_the_commit(other) == ""
        (other / "x.txt").write_text("a fix\n", encoding="utf-8")
        commit_everything_as_e(other, "a fix")
        sealed_and_committed(
            other,
            short(other),
            short(other, "origin/main"),
            "the sealer again",
            earlier=f"; earlier run: {target} sealed",
        )
        assert after_the_commit(other) == ""
        assert queued_values(other) == [] and refusals(other) == []

    @pytest.mark.rule("refused-sealed-leaves-a-record")
    def test_refuses_to_draw_again_over_a_refused_row_of_a_drawn_seal(
        self, world, tmp_path
    ):
        """S11's second case: the item was sealed and stamped, then its branch
        rebased onto a moved base, so a fresh clone does not hold the commit
        the rewritten `sealed` names. A plain commit there editing that
        guarantee is refused and recorded; the new audit's chain entry is
        skipped, and `sealed_before` still finds the rewritten `sealed` in
        HEAD's history, so nothing is drawn twice."""
        repo, target, base = world
        sealed_and_committed(repo, target, base, "the seal")
        assert after_the_commit(repo)
        git(repo, "switch", "-q", "main")
        (repo / "base.txt").write_text("the base moved\n", encoding="utf-8")
        commit_everything_as_e(repo, "the base moved")
        git(repo, "switch", "-q", "feat/x")
        git(repo, *SIGNED, "rebase", "-q", "main")
        other = tmp_path / "other"
        subprocess.run(
            ["git", "clone", "-q", "--no-local", str(repo), str(other)], check=True
        )
        assert git(other, "cat-file", "-e", target, check=False).returncode != 0
        item = other / GUARANTEE_REL
        item.write_text(
            item.read_text(encoding="utf-8") + "\na note\n", encoding="utf-8"
        )
        git(other, "add", "-A")
        code, _said = before_the_commit(other)
        assert code == 1 and refusals(other) == [f"{ITEM_ID}-{target}"]
        head = short(other)
        staged(
            other,
            guarantee_record(
                head,
                short(other, "origin/main"),
                "sealed",
                f"; earlier run: {target} sealed",
            ),
        )
        assert before_the_commit(other) == (0, "")
        commit_everything_as_e(other, "the sealer again at HEAD")
        assert after_the_commit(other) == ""
        assert queued_values(other) == []

    @pytest.mark.rule("refused-sealed-leaves-a-record")
    @pytest.mark.rule("sealed-off-the-branch-refused")
    def test_accepts_the_repair_of_a_row_refused_after_a_rebase(self, world, tmp_path):
        """Round 2's finding 1: the `withheld` was pushed and the branch then
        rebased, so `origin/feat/x` still holds the pre-rebase commit. A wrong
        row is refused and recorded, the gate reads no other ref, and the new
        audit queues the work item's one stamp."""
        repo, _target, _base = world
        other = tmp_path / "other"
        subprocess.run(
            ["git", "clone", "-q", "--no-local", str(repo), str(other)], check=True
        )
        git(other, "switch", "-q", "main")
        (other / "base.txt").write_text("the base moved\n", encoding="utf-8")
        commit_everything_as_e(other, "the base moved")
        git(other, "switch", "-q", "feat/x")
        git(other, *SIGNED, "rebase", "-q", "main")
        assert git_out(
            other, "log", "-1", "--format=%H", "--all", "--not", "HEAD", "--"
        )
        base = short(other, "main")
        staged(other, guarantee_record("deadbee", base, "sealed"))
        code, _said = before_the_commit(other)
        assert code == 1 and refusals(other) == [f"{ITEM_ID}-deadbee"]
        head = short(other)
        staged(
            other,
            guarantee_record(head, base, "sealed", "; earlier run: deadbee sealed"),
        )
        assert before_the_commit(other) == (0, "")
        commit_everything_as_e(other, "the sealer again at HEAD")
        assert after_the_commit(other)
        assert len(queued_values(other)) == 1, queued_values(other)


test_census = census_case(TARGET)
