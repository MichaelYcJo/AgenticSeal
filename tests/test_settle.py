"""`skills/settle/scripts/settle.py`, one class per function.

`settle` reads before it removes: what counts as released, the rule arm for a
spec-less directory, the merge base it asks at and the root it refuses
(#458, closing #83). It applies each released spec's `## Rule changes` to the
policy root in place, in merge order, and refuses what it cannot place
(#953). `Test_report` and `Test_apply` drive the two arms over the `tree`
fixture's history; `Test_main` runs the command over a repository whose
merge order git holds. `Test_module` holds the loader, the headings, the
launcher, and two answers the command takes from its siblings,
`unverified_check.py#settled` and `rule_changes.py#order`, asked over the
repositories this file builds, the case that reads this module's source
for a call of `settled` and no second definition of it, the copy run without
its siblings, and `SPECS` held under `seal/`.

#942's phase 6 placed these cases from
`tests/test_settle_reads_before_it_removes.py` and
`tests/test_settle_applies_rule_changes_in_place.py`, which keep the cases
that read the skill, the documents, the READMEs, the checklist and the cheat
sheets. The source-reading case came from `tests/test_unverified_rows_close.py`.
The copy's case came from `tests/test_a_script_copied_alone_exits_2.py` and
the `SPECS` case from `tests/test_a_reference_root_is_read_and_never_taken.py`
in #942's round 9 fix pass, each a case of this module alone.
"""

import io
import os
import subprocess
import sys

import pytest
from conftest import DOC, census_case, line_of, load_module, names_path, op, spec
from conftest import flattened as flat

TARGET = "skills/settle/scripts/settle.py"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, "skills", "settle", "scripts", "settle.py")

settle = load_module(SCRIPT, "settle")
rules = load_module(
    os.path.join(ROOT, "skills", "settle", "scripts", "rule_changes.py"),
    "specseal_rule_changes",
)


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        encoding="utf-8",
    ).stdout


def item(repo, name, changes):
    path = repo / "seal" / "specs" / name
    path.mkdir(parents=True, exist_ok=True)
    (path / "spec.md").write_text(spec(changes), encoding="utf-8")


def commit(repo, message):
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", message)


@pytest.fixture
def repo(tmp_path):
    repo = tmp_path / "repo"
    (repo / "docs").mkdir(parents=True)
    (repo / "docs" / "a.md").write_text(DOC, encoding="utf-8")
    (repo / "seal").mkdir()
    (repo / "seal" / "README.md").write_text("# seal\n", encoding="utf-8")
    git(repo, "init", "-q", "-b", "main")
    git(repo, "config", "user.email", "x@example.com")
    git(repo, "config", "user.name", "x")
    commit(repo, "base")
    return repo


def files(repo):
    return {
        str(p.relative_to(repo)): p.read_bytes()
        for p in repo.rglob("*")
        if p.is_file() and ".git" not in p.parts
    }


def dry_run(repo, capfd, *args):
    code = settle.main(["--root", str(repo), "--released-at", "main", *args])
    out = capfd.readouterr()
    return code, out.out + out.err


def apply(repo, capfd):
    return dry_run(repo, capfd, "--apply")


def specs_dir(repo, name):
    return repo / "seal" / "specs" / name


OPEN = (
    "# x — overview\n\n## Not verified\n\n| Item | Who must answer |\n"
    "|---|---|\n| a claim nobody ran | the repository owner |\n"
)


def configure(repo, *rows):
    table = "".join(f"| {item} | {value} |\n" for item, value in rows)
    (repo / "seal" / "config.md").write_text(
        f"| Item | Value |\n|---|---|\n{table}", encoding="utf-8"
    )


def no_rule(repo, work_item_id):
    """Give a released spec a `## Rule changes` that changes nothing, and
    commit it, so `--apply` removes its directory."""
    path = repo / "seal" / "specs" / work_item_id / "spec.md"
    path.write_text(
        path.read_text(encoding="utf-8")
        + "\n## Rule changes\n\n- nothing\n  why: a moment.\n",
        encoding="utf-8",
    )
    git(repo, "add", "--", f"seal/specs/{work_item_id}")
    git(repo, "commit", "-qm", f"{work_item_id} states no rule")


def run(repo, *args):
    """`(exit code, what a person reads)`."""
    out = io.StringIO()
    found = settle.survey(str(repo), "HEAD")
    assert found is not None, "the fixture's HEAD does not resolve"
    if "--apply" in args:
        code = settle.apply(found, str(repo), out=out)
    else:
        code = settle.report(found, "HEAD", out=out)
    return code, out.getvalue()


OVERVIEW_OPEN = """# x — overview

## Not verified

| Item | Who must answer |
|---|---|
| a claim nobody ran | the repository owner |
"""


OVERVIEW_CLOSED = """# x — overview

## Not verified

| Item | Who must answer |
|---|---|
| closed a claim | run on 2026-01-01 |
"""


MOMENT = "1700000006-release-0-1-0"


def moment(repo, name=MOMENT, overview=None):
    """A released work item below the SDD ladder: a routing declaration and
    perhaps a memo, and no `spec.md`. Committed on its own path, so the
    unreleased `delta` the fixture leaves on disk stays unreleased."""
    item = repo / "seal" / "specs" / name
    item.mkdir(parents=True)
    (item / "routing.md").write_text(f"# {name} — routing\n", encoding="utf-8")
    if overview is not None:
        (item / "overview.md").write_text(overview, encoding="utf-8")
    git(repo, "add", "--", f"seal/specs/{name}")
    git(repo, "commit", "-qm", f"released {name}")
    return item


def docs_text(repo):
    return {p.name: p.read_text(encoding="utf-8") for p in (repo / "docs").glob("*")}


# The branch the release merges to, in the fixtures below. A name that
# appears nowhere else in the output, so the assertions on it read the base
# and nothing else.
BASE = "release-target"


def at(repo, ref, *args):
    """`(exit code, what a person reads)` for `survey` at `ref`, the way
    `main` reaches it with `--released-at ref`."""
    out = io.StringIO()
    found = settle.survey(str(repo), ref)
    assert found is not None, f"{ref} does not resolve in the fixture"
    if "--apply" in args:
        code = settle.apply(found, str(repo), out=out)
    else:
        code = settle.report(found, ref, out=out)
    return code, out.getvalue()


def closed_after_base(repo):
    """S4's tree: the moment released with its row open at `BASE`, and a
    later commit on the working branch closing it — the 0.15.3 shape, where
    the closure reached the release branch and not `main`."""
    moment(repo, overview=OVERVIEW_OPEN)
    git(repo, "branch", BASE)
    (repo / "seal" / "specs" / MOMENT / "overview.md").write_text(
        OVERVIEW_CLOSED, encoding="utf-8"
    )
    git(repo, "add", "--", f"seal/specs/{MOMENT}")
    git(repo, "commit", "-qm", "close the row")


def settled_repo(tmp_path, keep_empty_dir):
    """A repository whose settle is complete: a `seal/` root with its README,
    and `seal/specs/` either empty on disk — the tree `--apply` leaves — or
    absent, which is what a fresh checkout of that commit has."""
    repo = tmp_path / "repo"
    (repo / "docs").mkdir(parents=True)
    (repo / "docs" / "one-root.md").write_text("# a policy\n", encoding="utf-8")
    (repo / "seal").mkdir()
    (repo / "seal" / "README.md").write_text("# seal\n", encoding="utf-8")
    git(repo, "init", "-q")
    git(repo, "config", "user.email", "x@example.com")
    git(repo, "config", "user.name", "x")
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "settled")
    if keep_empty_dir:
        (repo / "seal" / "specs").mkdir()
    return repo


class Test_report:
    def test_accepts_a_spec_with_no_rule_changes_and_lists_it_kept(self, tree):
        """A spec written before the section existed has nothing to replay, so it
        is named under its own heading and stays."""
        code, text = run(tree)
        assert code == 0, text
        assert "released with a spec.md: 3 work items, 0 to apply\n" in text, text
        listed = text.split(settle.PREMODEL_HEADING)[1].split("\n\n")[0] + "\n"
        for name in ("1700000001-alpha", "1700000002-beta", "1700000003-gamma"):
            assert f"    {name}\n" in listed, text

    def test_the_report_writes_nothing_and_removes_nothing(self, tree):
        before = sorted(
            str(p.relative_to(tree)) for p in tree.rglob("*") if p.is_file()
        )
        run(tree)
        after = sorted(str(p.relative_to(tree)) for p in tree.rglob("*") if p.is_file())
        assert before == after, "the report touched the tree"
        assert "Nothing was written and nothing was removed" in run(tree)[1]

    def test_an_unreleased_work_item_is_not_a_candidate(self, tree):
        """Released means present on the branch the release merges to, so this
        branch's own work item is outside the corpus entirely."""
        _, text = run(tree)
        assert "1700000004-delta" not in text, text
        assert "1 unreleased and untouched" in text, text

    def test_a_spec_less_directory_is_listed_under_its_own_heading(self, tree):
        """D3: `settle` prints these under their own heading rather than with
        the specs, because there is nothing to apply."""
        moment(tree, overview=OVERVIEW_CLOSED)
        code, text = run(tree)
        assert code == 0, text
        assert "retired by the rule" in text, text
        assert MOMENT in text.split("retired by the rule")[1], text
        premodel = text.split(settle.PREMODEL_HEADING)[1].split("\n\n")[0]
        assert MOMENT not in premodel, text

    def test_the_report_does_not_promise_what_the_retirement_refuses(self, tree):
        """S7. The report used to list the directory under *retired by the rule*,
        the heading that says `settle --apply` removes what it lists, while the
        CI readers would refuse the removal."""
        closed_after_base(tree)
        code, text = at(tree, BASE)
        assert code == 0, text
        assert settle.RULE_HEADING not in text, text
        assert "0 to retire by the rule" in text, text
        assert settle.RULE_BASE_HEADING.format(base=BASE) in text, text
        kept = text.split(settle.RULE_BASE_HEADING.format(base=BASE))[1]
        assert MOMENT in kept and "a claim nobody ran" in kept, text
        # #611, round 3 of 1790297085 ⬜ 3: bc63b91d reworded the summary line and
        # nothing pinned the new words (contract rule 14).
        assert f"1 kept because the closure has not reached {BASE}" in text, text

    def test_refuses_a_survey_with_no_base(self, tree):
        """Round 1, ⬜ 4. `report` is the third reader of `survey`'s dict, and it
        refuses a base-less one the way `apply` does rather than raising
        `KeyError` on the keys that dict does not carry."""
        moment(tree, overview=OVERVIEW_CLOSED)
        out = io.StringIO()
        code = settle.report({"base": None, "base_label": None}, "HEAD", out=out)
        assert code == 2, out.getvalue()
        assert "no merge base" in out.getvalue(), out.getvalue()

    def test_the_report_lists_what_an_apply_would_remove(self, tree):
        """D1's table: the command reports by itself the paths outside
        `seal/specs/` that cite into what `--apply` would remove, and the
        `tests/` files that read `seal/specs` — what #514's frame found by
        hand."""
        no_rule(tree, "1700000001-alpha")
        moment(tree)
        (tree / "docs" / "cites.md").write_text(
            "See `seal/specs/1700000001-alpha/spec.md` for the decision.\n"
            f"And `seal/specs/{MOMENT[:11]}…/routing.md` for the moment.\n"
            "A marker <!-- specs/1700000002-beta --> and a bare 1700000002-beta.\n",
            encoding="utf-8",
        )
        (tree / "tests").mkdir()
        (tree / "tests" / "test_reads.py").write_text(
            'SPECS = "seal/specs"\n', encoding="utf-8"
        )
        git(tree, "add", "--", "docs", "tests")
        git(tree, "commit", "-qm", "citations")
        _, text = run(tree)
        takes = text.split(settle.REMOVES_HEADING)[1]
        assert f"seal/specs/{MOMENT}/" in takes, text
        assert "docs/cites.md:1" in takes, text
        assert "docs/cites.md:2" in takes, "an abbreviated path is a citation too"
        assert "1700000002-beta" not in takes, "a marker or a bare id is not a path"
        assert "tests/test_reads.py" in text.split("checks that read")[1], text
        # Contract rule 14: the heading a person reads names the section that
        # says what each check owes, by its heading text.
        assert (
            "(`skills/settle/SKILL.md` *Answer every check that reads the corpus*)"
        ) in " ".join(text.split()), text


class Test_apply:
    def test_accepts_a_spec_that_states_no_rule_and_removes_only_it(self, tree):
        no_rule(tree, "1700000001-alpha")
        code, text = run(tree, "--apply")
        assert code == 0, text
        assert not (tree / "seal" / "specs" / "1700000001-alpha").exists()
        assert (tree / "seal" / "specs" / "1700000002-beta").exists(), (
            "a spec with no `## Rule changes` was removed"
        )

    def test_apply_leaves_a_team_specs_of_the_same_name_on_disk(self, tree):
        """#688 D3. A project's own `specs/` is read as history and never taken,
        even where a team directory carries the removed work item's very id: the
        removal is `seal/specs/` whatever else the tree holds (`SPECS`)."""
        team = tree / "specs" / "1700000001-alpha"
        team.mkdir(parents=True)
        (team / "design.md").write_text("# the team's design\n", encoding="utf-8")
        (team / "spec.md").write_text("# the team's spec\n", encoding="utf-8")
        git(tree, "add", "-A")
        git(tree, "commit", "-qm", "a team directory of the same name")
        no_rule(tree, "1700000001-alpha")
        code, text = run(tree, "--apply")
        assert code == 0, text
        assert not (tree / "seal" / "specs" / "1700000001-alpha").exists()
        assert (team / "design.md").read_text(
            encoding="utf-8"
        ) == "# the team's design\n"
        assert (team / "spec.md").is_file()

    def test_the_rule_arm_removes_it_with_no_marker(self, tree):
        moment(tree, overview=OVERVIEW_CLOSED)
        before = docs_text(tree)
        code, text = run(tree, "--apply")
        assert not (tree / "seal" / "specs" / MOMENT).exists(), text
        assert docs_text(tree) == before, "the rule arm wrote a marker into docs/"
        assert f"removed seal/specs/{MOMENT}/" in text, text
        assert "no `spec.md`" in text, text
        # The fixture's other released items carry a spec and no marker, so they
        # stay; nothing refused, so the run is clean.
        assert code == 0, text
        assert (tree / "seal" / "specs" / "1700000001-alpha").exists()

    def test_an_open_memo_row_keeps_a_spec_less_directory(self, tree):
        """G2: D3 is true of the spec and false of the memo. An open
        `## Not verified` row is a claim with an answerer, and it leaves by being
        closed or re-homed — never with the directory."""
        moment(tree, overview=OVERVIEW_OPEN)
        _, text = run(tree)
        assert "kept by the rule" in text, text
        assert "a claim nobody ran" in text.split("kept by the rule")[1], text
        code, text = run(tree, "--apply")
        assert code == 1, text
        assert (tree / "seal" / "specs" / MOMENT).exists(), text
        assert "a claim nobody ran" in text, text

    def test_a_closure_the_base_has_not_seen_keeps_the_directory(self, tree):
        """S4. The row is closed on the working branch and open at the base the
        release merges to. Both CI readers ask the rule of the merge base, so a
        retirement here would turn the release pull request red (#602, #598's
        second instance). It is kept, and the output names the base and the row
        open there."""
        closed_after_base(tree)
        code, text = at(tree, BASE, "--apply")
        assert (tree / "seal" / "specs" / MOMENT).exists(), text
        assert code == 1, text
        assert settle.RULE_BASE_HEADING.format(base=BASE) in text, text
        kept = text.split(settle.RULE_BASE_HEADING.format(base=BASE))[1]
        assert MOMENT in kept and "a claim nobody ran" in kept, text
        assert f"removed seal/specs/{MOMENT}/" not in text, text

    def test_an_uncommitted_closure_keeps_the_directory(self, tree):
        """S5. The same shape with the closure only on disk: the base is `HEAD`
        itself, where the row is still open."""
        moment(tree, overview=OVERVIEW_OPEN)
        (tree / "seal" / "specs" / MOMENT / "overview.md").write_text(
            OVERVIEW_CLOSED, encoding="utf-8"
        )
        code, text = at(tree, "HEAD", "--apply")
        assert (tree / "seal" / "specs" / MOMENT).exists(), text
        assert code == 1, text
        assert "a claim nobody ran" in text, text

    def test_a_closure_the_base_has_seen_lets_the_directory_go(self, tree):
        """S6, the counter-case that keeps S4 from passing by refusing
        everything: once the closure has merged into the base, the rule holds at
        both and the directory goes with no marker."""
        closed_after_base(tree)
        git(tree, "branch", "-f", BASE, "HEAD")
        code, text = at(tree, BASE, "--apply")
        assert not (tree / "seal" / "specs" / MOMENT).exists(), text
        assert f"removed seal/specs/{MOMENT}/" in text, text
        assert code == 0, text

    def test_a_base_that_moved_past_the_fork_names_the_merge_that_moves_it(self, tree):
        """Round 1, 🟡 1. `main` took the closure after this branch forked, and
        this branch never merged it back. CI asks at `main`'s tip and would pass;
        `settle` asks at the fork and keeps the directory. That keeps more than
        it must, which is the safe direction, but the remedy it prints has to be
        the one that works: merge `main` in."""
        moment(tree, overview=OVERVIEW_OPEN)
        git(tree, "branch", "-M", "main")
        git(tree, "switch", "-qc", "work")
        ov = tree / "seal" / "specs" / MOMENT / "overview.md"
        ov.write_text(OVERVIEW_CLOSED, encoding="utf-8")
        git(tree, "add", "--", f"seal/specs/{MOMENT}")
        git(tree, "commit", "-qm", "close on work")
        git(tree, "switch", "-q", "main")
        ov.write_text(OVERVIEW_CLOSED, encoding="utf-8")
        git(tree, "add", "--", f"seal/specs/{MOMENT}")
        git(tree, "commit", "-qm", "hotfix: close on main")
        git(tree, "switch", "-q", "work")
        code, text = at(tree, "main", "--apply")
        assert (tree / "seal" / "specs" / MOMENT).exists(), text
        assert code == 1, text
        flat_text = " ".join(text.split())
        assert "merge main into this branch" in flat_text, text
        # Round 2, ⬜ 4: the fork is a fixed past commit, so nothing waits for a
        # closure to reach it; the heading says it has not.
        assert "kept: the closure has not reached the merge-base of main" in flat_text
        assert "kept until the closure reaches the merge-base" not in flat_text, text
        assert "the CI readers ask the rule there" not in flat_text, text

    def test_refuses_a_survey_with_no_base(self, tree):
        """`apply`'s own guard, for a caller that hands it a survey `main` would
        have refused: the predicate asked of `None` is asked of the tree alone,
        which is the answer #602 removed, so nothing is read and nothing goes."""
        moment(tree, overview=OVERVIEW_CLOSED)
        found = settle.survey(str(tree), "HEAD")
        found["base"] = None
        out = io.StringIO()
        assert settle.apply(found, str(tree), out=out) == 2, out.getvalue()
        assert (tree / "seal" / "specs" / MOMENT).exists(), out.getvalue()
        assert "no merge base" in out.getvalue(), out.getvalue()

    def test_an_unreadable_memo_keeps_a_spec_less_directory(self, tree):
        """A section this cannot read is a count it does not know, never zero."""
        moment(tree, overview="# x — overview\n\n## Not checked\n")
        code, text = run(tree, "--apply")
        assert code == 1, text
        assert (tree / "seal" / "specs" / MOMENT).exists(), text
        assert "cannot be read" in text, text

    def test_an_unreleased_spec_less_directory_is_not_a_candidate(self, tree):
        item = tree / "seal" / "specs" / MOMENT
        item.mkdir()
        (item / "routing.md").write_text("# routing\n", encoding="utf-8")
        _, text = run(tree, "--apply")
        assert item.exists(), text

    def test_the_predicate_is_what_settle_asks(self, tree, monkeypatch):
        """One predicate, asked by every reader. With it answering nothing, the
        rule arm lists nothing."""
        moment(tree)
        reader = settle.load(settle.READER, "specseal_unverified_reader")
        real_load = settle.load
        monkeypatch.setattr(reader, "settled", lambda root, ref, dirs, here=None: set())
        monkeypatch.setattr(
            settle,
            "load",
            lambda path, name: (
                reader if path == settle.READER else real_load(path, name)
            ),
        )
        _, text = run(tree, "--apply")
        assert (tree / "seal" / "specs" / MOMENT).exists(), text

    def test_an_apply_with_nothing_to_do_is_no_refusal(self, tree):
        """Exit 1 is a refusal, and a tree whose specs predate the section
        refuses nothing: the run says what it did, which is nothing, and exits
        0."""
        before = sorted(
            str(p.relative_to(tree)) for p in tree.rglob("*") if p.is_file()
        )
        code, text = run(tree, "--apply")
        assert code == 0, text
        assert "applied 0 specs and removed 0 directories; 0 refused or kept" in text
        # The summary is the line read to decide whether the settle is finished,
        # so the specs it leaves in place are counted there too (round 1, 8).
        assert "; 3 with no `## Rule changes`, left in place\n" in text, text
        after = sorted(str(p.relative_to(tree)) for p in tree.rglob("*") if p.is_file())
        assert before == after, text


class Test_main:
    def test_the_dry_run_lists_pending_changes_in_merge_order_and_writes_nothing(
        self, repo, capfd
    ):
        """S8, and S5's order: B was added after A on one line of history, so B
        is listed after A whatever their ids say."""
        item(repo, "1700000009-a", op("change", "S", "old sentence.", "y."))
        commit(repo, "a")
        item(repo, "1700000001-b", op("change", "S", "y.", "z."))
        item(repo, "1700000002-c", op("remove", "Nowhere"))
        commit(repo, "b and c")
        before = files(repo)
        code, text = dry_run(repo, capfd)
        assert code == 0, text
        assert files(repo) == before, "the dry run wrote to the tree"
        pending = text.split("pending rule changes")[1].split("\n\n")[0]
        assert "docs/a.md" in pending
        assert pending.index("1700000009-a") < pending.index("1700000001-b"), text
        refused = text.split("refused")[1]
        assert "1700000002-c" in refused and "spec.md:" in refused, text
        removes = text.split("what `settle --apply` would remove")[1]
        assert "1700000009-a" in removes and "1700000001-b" in removes, text
        assert "1700000002-c" not in removes, text

    @pytest.mark.parametrize("section", ["S", "S child"])
    def test_two_specs_on_parallel_branches_at_one_place_are_a_conflict(
        self, repo, capfd, section
    ):
        """S6: ancestry cannot order them, so neither applies there, and both are
        printed for the owner. A sub-section is inside its section's range, so it
        is the same place."""
        git(repo, "switch", "-qc", "one")
        item(repo, "1700000001-a", op("change", "S", "old sentence.", "y."))
        commit(repo, "a")
        git(repo, "switch", "-q", "main")
        git(repo, "switch", "-qc", "two")
        item(repo, "1700000002-b", op("add", section, new="Rule."))
        commit(repo, "b")
        git(repo, "switch", "-q", "main")
        git(repo, "merge", "-q", "--no-ff", "-m", "one", "one")
        git(repo, "merge", "-q", "--no-ff", "-m", "two", "two")
        _, text = dry_run(repo, capfd)
        refused = text.split("refused")[1]
        for name in ("1700000001-a", "1700000002-b"):
            assert name in refused, text
        assert "conflict" in refused, text
        assert "would remove" not in text, text

    def test_apply_rewrites_in_place_and_removes_the_directory(self, repo, capfd):
        """S1: the change lands where the text stood, the rest is byte-identical,
        no marker is written, and the directory goes whole, its process record
        included."""
        item(repo, "1700000001-a", op("change", "S", "old sentence.", "New rule."))
        rounds = specs_dir(repo, "1700000001-a") / "rounds"
        rounds.mkdir()
        (rounds / "round-1.md").write_text("# round 1\n", encoding="utf-8")
        commit(repo, "a")
        code, text = apply(repo, capfd)
        assert code == 0, text
        after = (repo / "docs" / "a.md").read_text(encoding="utf-8")
        assert after == DOC.replace("old sentence.", "New rule."), after
        assert "<!-- specs/" not in after
        assert not specs_dir(repo, "1700000001-a").exists(), text
        assert "removed seal/specs/1700000001-a/" in text, text

    def test_apply_follows_merge_order(self, repo, capfd):
        """S5: B was added after A on one line of history, so B applies over A
        although its id sorts first."""
        item(repo, "1700000009-a", op("change", "S", "old sentence.", "y."))
        commit(repo, "a")
        item(repo, "1700000001-b", op("change", "S", "y.", "z."))
        commit(repo, "b")
        code, text = apply(repo, capfd)
        assert code == 0, text
        assert "Before. z. After." in (repo / "docs" / "a.md").read_text(
            encoding="utf-8"
        )
        assert not specs_dir(repo, "1700000009-a").exists()
        assert not specs_dir(repo, "1700000001-b").exists()

    @pytest.mark.rule("a-settle-is-no-deletion")
    def test_what_apply_removed_is_settled_for_the_readers(self, repo, capfd):
        """S9 from `settle`'s side: the CI readers ask
        `unverified_check.py#settled` of the base, and what `--apply` removed
        passes it. It answers for the set one pull request removes: B rewrote
        the text A placed, so A asked alone does not hold."""
        item(repo, "1700000009-a", op("change", "S", "old sentence.", "y."))
        commit(repo, "a")
        item(repo, "1700000001-b", op("change", "S", "y.", "z."))
        commit(repo, "b")
        code, text = apply(repo, capfd)
        assert code == 0, text
        reader = settle.load(settle.READER, "specseal_reader_for_settled")
        both = {"seal/specs/1700000009-a", "seal/specs/1700000001-b"}
        assert reader.settled(str(repo), "HEAD", sorted(both)) == both
        assert reader.settled(str(repo), "HEAD", ["seal/specs/1700000009-a"]) == set()

    def test_apply_deletes_a_document_its_removal_leaves_empty(self, repo, capfd):
        """S18: the document's title and its first section read alike, so the
        removal names both and takes the outer one. The file goes, the index
        row naming it goes in the same spec, `fold-check` names nothing after
        the apply, and the readers count the removal settled."""
        (repo / "docs" / "gate.md").write_text(
            "# Gate\n\nIntro.\n\n## Gate\n\nBody.\n", encoding="utf-8"
        )
        row = "| `docs/gate.md` | the gate |"
        (repo / "docs" / "README.md").write_text(
            "# docs\n\n| File | The question it answers |\n|---|---|\n"
            f"| `docs/a.md` | a policy |\n{row}\n",
            encoding="utf-8",
        )
        commit(repo, "gate")
        item(
            repo,
            "1700000001-a",
            op("remove", "Gate", file="docs/gate.md")
            + "\n"
            + op("remove", "docs", row, file="docs/README.md"),
        )
        commit(repo, "a")
        code, text = apply(repo, capfd)
        assert code == 0, text
        assert not (repo / "docs" / "gate.md").exists(), text
        assert "deleted docs/gate.md: a removal left it empty\n" in text, text
        assert settle.AFTER_HEADING not in text, text
        assert (repo / "docs" / "a.md").read_text(encoding="utf-8") == DOC
        reader = settle.load(settle.READER, "specseal_reader_for_a_deletion")
        directory = "seal/specs/1700000001-a"
        assert reader.settled(str(repo), "HEAD", [directory]) == {directory}

    @pytest.mark.parametrize(
        "change, half",
        [
            (op("remove", "T"), lambda doc: doc),
            (
                op("change", "S", "old sentence.", "New rule."),
                lambda doc: doc.replace("old sentence.", "old sentence. New rule."),
            ),
        ],
        ids=["a section left in place", "the old text left beside the new"],
    )
    def test_a_rule_change_half_applied_is_not_settled(self, repo, capfd, change, half):
        """S10 per operation: each text an operation names is counted, the
        heading of a removed section and the `from` of a change included."""
        item(repo, "1700000001-a", change)
        commit(repo, "a")
        reader = settle.load(settle.READER, "specseal_reader_for_half")
        directory = "seal/specs/1700000001-a"
        doc = repo / "docs" / "a.md"
        doc.write_text(half(DOC), encoding="utf-8")
        assert reader.settled(str(repo), "HEAD", [directory]) == set()
        doc.write_text(DOC, encoding="utf-8")
        code, text = apply(repo, capfd)
        assert code == 0, text
        assert reader.settled(str(repo), "HEAD", [directory]) == {directory}

    def test_apply_refuses_a_conflict_and_keeps_both(self, repo, capfd):
        """S6."""
        for branch, name, change in (
            ("one", "1700000001-a", op("change", "S", "old sentence.", "y.")),
            ("two", "1700000002-b", op("add", "S", new="Rule.")),
        ):
            git(repo, "switch", "-qc", branch, "main")
            item(repo, name, change)
            commit(repo, name)
        git(repo, "switch", "-q", "main")
        git(repo, "merge", "-q", "--no-ff", "-m", "one", "one")
        git(repo, "merge", "-q", "--no-ff", "-m", "two", "two")
        code, text = apply(repo, capfd)
        assert code == 1, text
        assert (repo / "docs" / "a.md").read_text(encoding="utf-8") == DOC
        assert specs_dir(repo, "1700000001-a").exists()
        assert specs_dir(repo, "1700000002-b").exists()
        assert "conflict" in text, text

    def test_apply_writes_nothing_of_a_refused_spec(self, repo, capfd):
        """S4 and S7: the first operation would apply, the second cannot, so
        neither does; the refusal names the spec, the line and the reason."""
        both = op("change", "S", "old sentence.", "y.") + "\n" + op("remove", "Nowhere")
        item(repo, "1700000001-a", both)
        commit(repo, "a")
        code, text = apply(repo, capfd)
        assert code == 1, text
        assert (repo / "docs" / "a.md").read_text(encoding="utf-8") == DOC
        assert specs_dir(repo, "1700000001-a").exists()
        line = line_of(spec(both), "- remove")
        assert f"1700000001-a  spec.md:{line}  no heading `Nowhere`" in text, text

    def test_an_open_record_row_holds_its_spec(self, repo, capfd):
        """Nothing open is one of the three things a settled directory holds; a
        row still open is a claim with an answerer, and it never leaves with the
        directory."""
        item(repo, "1700000001-a", op("add", "S", new="Rule."))
        (specs_dir(repo, "1700000001-a") / "overview.md").write_text(
            OPEN, encoding="utf-8"
        )
        commit(repo, "a")
        code, text = apply(repo, capfd)
        assert code == 1, text
        assert (repo / "docs" / "a.md").read_text(encoding="utf-8") == DOC
        assert specs_dir(repo, "1700000001-a").exists()
        assert "a claim nobody ran" in text, text

    def test_nothing_to_apply_leaves_and_a_spec_with_no_section_stays(
        self, repo, capfd
    ):
        """A spec whose section is the no-change block states that no rule
        changes, so its directory goes, named under the block. A spec with no
        section was written before it existed, so there is nothing to replay and
        it is kept and named, which is not a refusal."""
        item(repo, "1700000001-a", "- nothing\n  why: a release entry.")
        old = specs_dir(repo, "1700000002-old")
        old.mkdir(parents=True)
        (old / "spec.md").write_text("# old\n\n## Scope\n\nIn.\n", encoding="utf-8")
        commit(repo, "a and old")
        code, text = apply(repo, capfd)
        assert code == 0, text
        assert not specs_dir(repo, "1700000001-a").exists(), text
        assert "no rule to apply (`- nothing`):\n    1700000001-a\n" in text, text
        assert old.exists(), text
        assert "1700000002-old" in text.split("no `## Rule changes`")[1], text
        assert (repo / "docs" / "a.md").read_text(encoding="utf-8") == DOC

    @pytest.mark.parametrize("flag", ["--retire", "--retire-process"])
    def test_the_retired_flags_are_an_argument_error(self, repo, flag, capfd):
        """A script that still calls either gets exit 2, which the changelog
        fragment says."""
        with pytest.raises(SystemExit) as raised:
            settle.main(["--root", str(repo), "--released-at", "main", flag])
        assert raised.value.code == 2

    def test_a_section_that_does_not_parse_keeps_its_directory(self, repo, capfd):
        """A parse error leaves the spec no operations, which must not read as a
        spec with nothing to apply."""
        item(repo, "1700000001-a", "- rename\n  file: docs/a.md\n  to: x")
        commit(repo, "a")
        code, text = apply(repo, capfd)
        assert code == 1, text
        assert specs_dir(repo, "1700000001-a").exists(), text
        assert "`rename` is not one of" in text, text

    def test_the_text_applied_is_the_spec_as_released(self, repo, capfd):
        """An edit on disk after the release is not what was reviewed."""
        item(repo, "1700000001-a", op("add", "U", new="Released."))
        commit(repo, "a")
        item(repo, "1700000001-a", op("add", "U", new="Edited later."))
        code, text = apply(repo, capfd)
        assert code == 0, text
        after = (repo / "docs" / "a.md").read_text(encoding="utf-8")
        assert after.endswith("Last.\n\nReleased.\n"), after

    def test_a_spec_moved_into_place_is_ordered_by_the_commit_that_moved_it(
        self, repo, capfd
    ):
        """git reads a moved directory as a rename, never as an add, unless it is
        told not to; the spec would then have no place in the order."""
        item(repo, "1700000001-old", op("add", "U", new="Rule."))
        commit(repo, "old")
        git(repo, "mv", "seal/specs/1700000001-old", "seal/specs/1700000002-new")
        commit(repo, "renamed")
        code, text = apply(repo, capfd)
        assert code == 0, text
        assert not specs_dir(repo, "1700000002-new").exists(), text

    def test_a_spec_no_commit_adds_is_held(self, repo, capfd, monkeypatch):
        """Where the history cannot place a spec, it has no place in the order,
        and it is held rather than applied first or last."""
        item(repo, "1700000001-a", op("add", "U", new="Rule."))
        commit(repo, "a")
        real = settle.load

        def load(path, name):
            module = real(path, name)
            if path == settle.RULES:
                monkeypatch.setattr(
                    module, "order", lambda r, f, ids, s: [(i, None) for i in ids]
                )
            return module

        monkeypatch.setattr(settle, "load", load)
        code, text = apply(repo, capfd)
        assert code == 1, text
        assert "no commit on main adds its spec.md" in text, text
        assert specs_dir(repo, "1700000001-a").exists()

    def test_apply_creates_the_policy_root_the_config_names(self, repo, capfd):
        """S14: with `Policy root` naming `policy/` and no such directory, the
        first `--apply` creates it with its index, writes there, touches no
        `docs/`, and names the index row the new document is owed. The readers
        replay into the same root."""
        configure(repo, ("Policy root", "policy"))
        item(repo, "1700000001-a", op("add", new="# New", file="policy/new.md"))
        commit(repo, "a")
        before = files(repo)
        code, text = apply(repo, capfd)
        assert code == 0, text
        assert (repo / "policy" / "new.md").read_text(encoding="utf-8") == "# New\n"
        assert (repo / "policy" / "README.md").is_file(), text
        docs = {k: v for k, v in files(repo).items() if k.startswith("docs")}
        assert docs == {k: v for k, v in before.items() if k.startswith("docs")}
        assert "policy/README.md has no row naming policy/new.md" in text, text
        reader = settle.load(settle.READER, "specseal_reader_for_policy_root")
        directory = "seal/specs/1700000001-a"
        assert reader.settled(str(repo), "HEAD", [directory]) == {directory}

    @pytest.mark.parametrize(
        "names", [("docs/A.md",), ("docs/new.md", "docs/NEW.md")], ids=["disk", "specs"]
    )
    def test_a_name_that_differs_only_in_case_is_held(self, repo, capfd, names):
        """On a case-insensitive disk two such names are one file, and the second
        write would erase the first spec's change while its directory went."""
        for n, name in enumerate(names, 1):
            item(repo, f"170000000{n}-a", op("add", new="# X", file=name))
        commit(repo, "case")
        before = files(repo)
        code, text = apply(repo, capfd)
        assert code == 1, text
        assert "differs from another document only in case" in text, text
        assert files(repo) == before, text

    def test_apply_names_a_document_past_the_ceiling(self, repo, capfd):
        """Scope 5: after applying, each document past `Document token ceiling`
        is named as one to split, and that refuses nothing."""
        configure(repo, ("Document token ceiling", "10"))
        item(repo, "1700000001-a", op("add", "U", new="Released."))
        commit(repo, "a")
        code, text = apply(repo, capfd)
        assert code == 0, text
        assert (
            "docs/a.md is about "
            in text.split("past the ceiling")[0].rsplit("\n", 1)[-1]
        ), text
        assert "past the ceiling of 10: split it along its own headings" in text, text

    def test_a_shallow_clone_is_not_told_the_refs_share_no_commit(
        self, tree, tmp_path, capsys
    ):
        """Round 1, ⬜ 3. A depth-1 clone of related history has no merge base
        either, and the refusal names that state too, the way `chain_check.py`'s
        does, so the reader looks at the clone's depth rather than at the ref."""
        moment(tree, overview=OVERVIEW_CLOSED)
        git(tree, "branch", "-M", "main")
        git(tree, "switch", "-qc", "work")
        (tree / "docs" / "later.md").write_text("# later\n", encoding="utf-8")
        git(tree, "add", "--", "docs")
        git(tree, "commit", "-qm", "on work")
        git(tree, "switch", "-q", "main")
        (tree / "docs" / "main.md").write_text("# on main\n", encoding="utf-8")
        git(tree, "add", "--", "docs")
        git(tree, "commit", "-qm", "on main")
        shallow = tmp_path / "shallow"
        subprocess.run(
            [
                "git",
                "clone",
                "-q",
                "--depth",
                "1",
                "--no-single-branch",
                "-b",
                "work",
                f"file://{tree}",
                str(shallow),
            ],
            check=True,
            capture_output=True,
        )
        code = settle.main(["--root", str(shallow), "--released-at", "origin/main"])
        err = " ".join(capsys.readouterr().err.split())
        assert code == 2, err
        assert "too shallow" in err and "git fetch --unshallow" in err, err
        assert (shallow / "seal" / "specs" / MOMENT).exists()

    @pytest.mark.parametrize("apply", [False, True])
    def test_no_merge_base_is_refused_and_nothing_is_removed(self, tree, apply, capsys):
        """S8. A `--released-at` sharing no history with `HEAD` has no merge
        base, so there is no revision to ask the rule of. Exit 2, the ref named,
        nothing read — never the working tree's answer alone."""
        moment(tree, overview=OVERVIEW_CLOSED)
        empty = subprocess.run(
            ["git", "-C", str(tree), "mktree"],
            input="",
            capture_output=True,
            encoding="utf-8",
            check=True,
        ).stdout.strip()
        lone = subprocess.run(
            ["git", "-C", str(tree), "commit-tree", empty, "-m", "unrelated"],
            capture_output=True,
            encoding="utf-8",
            check=True,
        ).stdout.strip()
        git(tree, "branch", "unrelated", lone)
        argv = ["--root", str(tree), "--released-at", "unrelated"]
        code = settle.main(argv + (["--apply"] if apply else []))
        err = capsys.readouterr().err
        assert code == 2, err
        assert "--released-at unrelated" in err and "share no commit" in err, err
        assert (tree / "seal" / "specs" / MOMENT).exists()

    def test_refuses_local_mode_rather_than_reading_an_empty_repository(self, tmp_path):
        """Round 1, finding 3. `settle` looked only at `<root>/seal/specs`, so a
        local-mode repository holding work items was told it had none — and the
        sentence written for local mode, behind the `--released-at` refusal, could
        never be printed because this check fired first and always.

        Resolving the root is half of it. With the root found, the run would go on
        to ask git which work items are released, git would answer with none — an
        uncommitted root has no path in any tree — and the report would say there
        is nothing to fold. That is the quiet zero by another door, so the state
        is named instead."""
        repo = tmp_path / "repo"
        (repo / "docs").mkdir(parents=True)
        git(repo, "init", "-q")
        item = repo / ".git" / "seal" / "specs" / "1700000001-alpha"
        item.mkdir(parents=True)
        (item / "spec.md").write_text("# a\n", encoding="utf-8")
        r = subprocess.run(
            [sys.executable, SCRIPT, "--root", str(repo), "--released-at", "HEAD"],
            capture_output=True,
            encoding="utf-8",
        )
        assert r.returncode == 2, r.stdout + r.stderr
        assert "which is local mode" in r.stderr, r.stderr
        assert "seal mode shared" in r.stderr, (
            "the refusal does not say how to get out of it"
        )
        assert "has nothing to settle" not in r.stderr, (
            "a repository holding a work item is still being told it has none"
        )

    def test_a_repository_with_no_root_at_either_place_says_so(self, tmp_path):
        """The other arm of the same resolution, kept apart from local mode
        because the two are different states and used to share one sentence."""
        repo = tmp_path / "repo"
        repo.mkdir()
        git(repo, "init", "-q")
        r = subprocess.run(
            [sys.executable, SCRIPT, "--root", str(repo), "--released-at", "HEAD"],
            capture_output=True,
            encoding="utf-8",
        )
        assert r.returncode == 2, r.stdout + r.stderr
        assert "at either place" in r.stderr, r.stderr

    def test_an_opted_out_repository_is_told_which_state_it_is_in(self, tmp_path):
        """Round 2, finding 7. `home_at` answers `""` for two states — no root at
        either place, and a repository that opted out with the scratch marker —
        and they were given one sentence, so a tree holding work items was told it
        had none. That is finding 3's defect through another door."""
        repo = tmp_path / "repo"
        (repo / "docs").mkdir(parents=True)
        git(repo, "init", "-q")
        item = repo / "seal" / "specs" / "1700000001-alpha"
        item.mkdir(parents=True)
        (item / "spec.md").write_text("# a\n", encoding="utf-8")
        (repo / ".git" / "specseal-scratch").write_text("", encoding="utf-8")
        r = subprocess.run(
            [sys.executable, SCRIPT, "--root", str(repo), "--released-at", "HEAD"],
            capture_output=True,
            encoding="utf-8",
        )
        assert r.returncode == 2, r.stdout + r.stderr
        assert "has opted out" in r.stderr, r.stderr
        assert "specseal-scratch" in r.stderr, r.stderr
        assert "has nothing to settle" not in r.stderr, (
            "a repository holding a work item is still being told it has none"
        )

    def test_a_directory_of_the_markers_name_is_not_an_opt_out(self, tmp_path):
        """Round 3, finding 1. `hooks/optin.py#home_at` reads the scratch marker
        with `os.path.isfile` and says why: `os.path.exists` also accepted a
        DIRECTORY of that name, and one created once turned every gate off in
        every clone. The refusal here asked `exists`, so a repository holding a
        directory of that name and no root was told it had opted out and to delete
        "that file" — and no gate reads a directory as the opt-out, so every clause
        of that sentence was false. The three readers of one marker answer alike."""
        repo = tmp_path / "repo"
        repo.mkdir()
        git(repo, "init", "-q")
        (repo / ".git" / "specseal-scratch").mkdir()
        r = subprocess.run(
            [sys.executable, SCRIPT, "--root", str(repo), "--released-at", "HEAD"],
            capture_output=True,
            encoding="utf-8",
        )
        assert r.returncode == 2, r.stdout + r.stderr
        assert "has no seal/specs/ at either place" in r.stderr, r.stderr
        assert "has opted out" not in r.stderr, (
            "a directory of the marker's name is read as the opt-out, which is the "
            "reading `hooks/optin.py` rejected by name"
        )

    def test_the_refusal_path_asks_for_the_common_directory_once(
        self, tmp_path, monkeypatch
    ):
        """Round 3, finding 5. `home_at(root)` resolves the common git directory
        for itself, and the opt-out arm then resolved it a second time, although
        `home_at(root, common)` exists for a caller that needs the value too and
        `hooks/optin.py` documents the parameter with the measurement that created
        it. Counted through the module `settle.load` hands `main`, and counted as
        calls rather than processes: on a main worktree the resolver's fast path
        costs no process, so a process count would have said nothing."""
        repo = tmp_path / "repo"
        repo.mkdir()
        git(repo, "init", "-q")
        optin = settle.load(settle.OPTIN, "specseal_optin_counted")
        calls, received = [], []
        common_dir, home_at = optin.git_common_dir, optin.home_at

        def counted(root):
            calls.append(root)
            return common_dir(root)

        def recorded(root, common=None):
            received.append(common)
            return home_at(root, common)

        # `home_at` reaches `git_common_dir` through the module global, so the
        # counter sees the resolver's own call as well as `main`'s.
        optin.git_common_dir, optin.home_at = counted, recorded
        real_load = settle.load
        monkeypatch.setattr(
            settle,
            "load",
            lambda path, name: optin if path == settle.OPTIN else real_load(path, name),
        )
        assert settle.main(["--root", str(repo), "--released-at", "HEAD"]) == 2
        assert len(calls) == 1, calls
        assert received == [common_dir(os.path.abspath(str(repo)))], received

    def test_the_released_at_refusal_is_about_the_ref_and_nothing_else(self, tmp_path):
        """Round 2, finding 4. The clause about local mode sat inside a message
        for a different failure and could not fire in the case it described:
        local mode returns before `survey` is ever called."""
        repo = tmp_path / "repo"
        (repo / "seal" / "specs" / "1700000001-alpha").mkdir(parents=True)
        (repo / "seal" / "specs" / "1700000001-alpha" / "spec.md").write_text(
            "# a\n", encoding="utf-8"
        )
        git(repo, "init", "-q")
        r = subprocess.run(
            [
                sys.executable,
                SCRIPT,
                "--root",
                str(repo),
                "--released-at",
                "no/such/ref",
            ],
            capture_output=True,
            encoding="utf-8",
        )
        assert r.returncode == 2, r.stdout + r.stderr
        assert "does not resolve" in r.stderr, r.stderr
        assert "local mode" not in r.stderr, (
            "the ref refusal still talks about a state it cannot be in"
        )

    @pytest.mark.rule("an-empty-root-is-settled")
    @pytest.mark.parametrize("keep_empty_dir", [True, False], ids=["empty", "absent"])
    @pytest.mark.parametrize("apply", [False, True], ids=["report", "apply"])
    def test_accepts_a_settled_root_and_says_so(self, tmp_path, keep_empty_dir, apply):
        """G7. After the last settle a fresh checkout has no `seal/specs/` at
        all and the tree that ran `--apply` has an empty one. Both are the state
        a complete settle reaches, and `settle` used to refuse the first at exit
        2 — so the command could not run on its own finished work."""
        repo = settled_repo(tmp_path, keep_empty_dir)
        argv = [sys.executable, SCRIPT, "--root", str(repo), "--released-at", "HEAD"]
        r = subprocess.run(
            argv + (["--apply"] if apply else []), capture_output=True, encoding="utf-8"
        )
        assert r.returncode == 0, r.stdout + r.stderr
        assert "holds no work item" in r.stdout, r.stdout + r.stderr
        assert "A complete settle ends here" in r.stdout, r.stdout


class Test_module:
    def test_merge_order_is_the_commit_that_adds_the_spec(self, repo):
        """A work item's directory is born with its `routing.md`, often well
        before its `spec.md`; the order is the spec's, not the directory's."""
        early = specs_dir(repo, "1700000001-a")
        early.mkdir(parents=True)
        (early / "routing.md").write_text("# a — routing\n", encoding="utf-8")
        commit(repo, "a is declared")
        item(repo, "1700000002-b", op("add", "U", new="B."))
        commit(repo, "b")
        item(repo, "1700000001-a", op("add", "U", new="A."))
        commit(repo, "a is framed")
        ids = ["1700000001-a", "1700000002-b"]
        found = [i for i, _ in rules.order(str(repo), "HEAD", ids)]
        assert found == ["1700000002-b", "1700000001-a"], found

    def test_a_ref_that_does_not_resolve_is_refused_rather_than_empty(self, tree):
        """The quiet zero this is written against: a ref nothing can read makes
        every work item look unreleased, and the report would then say there is
        nothing to do."""
        assert settle.survey(str(tree), "no/such/ref") is None

    def test_the_base_heading_says_where_the_closure_has_to_go(self):
        """Contract rule 14: the sentence a person acts on is pinned, not only its presence."""
        heading = flat(settle.RULE_BASE_HEADING.format(base="origin/main"))
        assert "origin/main" in heading, heading
        assert "the branch the release merges to" in heading, heading
        assert "a later pull request" in heading, heading

    @pytest.mark.parametrize("ref", [None, "HEAD"])
    def test_the_predicate_asks_every_condition_itself(self, tree, ref):
        """`settle` sorts by `spec.md` before the predicate decides, so through
        `settle` alone the predicate's own conditions are never seen. The CI
        readers ask it of a merge-base where neither check has run, so each
        condition is asked here directly, of the working tree and of a ref."""
        reader = settle.load(settle.READER, "specseal_unverified_reader_rule")
        moment(tree, overview=OVERVIEW_CLOSED)
        moment(tree, name="1700000008-with-memo", overview=OVERVIEW_OPEN)
        unapplied = tree / "seal" / "specs" / "1700000002-beta" / "spec.md"
        unapplied.write_text(
            "# beta\n\n## Rule changes\n\n- add\n  file: docs/one-root.md\n"
            "  section: a policy\n  to: A rule nobody applied.\n",
            encoding="utf-8",
        )
        git(tree, "commit", "-qam", "beta states a rule")
        root = str(tree)

        def ok(name):
            directory = f"seal/specs/{name}"
            return reader.settled(root, ref, [directory]) == {directory}

        assert ok(MOMENT)
        assert ok("1700000001-alpha"), "a spec with no `## Rule changes` was refused"
        assert not ok("1700000002-beta"), (
            "a rule the tree does not hold read as applied"
        )
        assert not ok("1700000008-with-memo")
        assert not ok("1700009999-nowhere"), (
            "a directory that never existed was settled"
        )
        # Round 1's finding 3: a spec an earlier commit deleted was still written.
        dropped = moment(tree, name="1700000009-spec-dropped")
        (dropped / "spec.md").write_text("# a spec\n\nA rule.\n", encoding="utf-8")
        git(tree, "add", "--", "seal/specs/1700000009-spec-dropped")
        git(tree, "commit", "-qm", "a spec")
        git(tree, "rm", "-q", "seal/specs/1700000009-spec-dropped/spec.md")
        git(tree, "commit", "-qm", "the spec, dropped")
        assert not ok("1700000009-spec-dropped"), (
            "a directory whose spec.md an earlier commit deleted read as one that wrote none"
        )

    def test_the_command_is_reachable_by_the_name_a_document_gives_it(self):
        """A6. The pair rule is `tests/test_a_document_that_names_a_script_says_
        how_to_reach_it.py`'s; this is the instance, asked here so a missing twin
        names this work item rather than a parametrisation."""
        for name in ("settle", "settle.cmd"):
            assert os.path.isfile(os.path.join(ROOT, "bin", name)), name
        assert os.access(os.path.join(ROOT, "bin", "settle"), os.X_OK), (
            "`bin/settle` ships without its executable bit, so the command "
            "resolves on PATH and then refuses"
        )

    @pytest.mark.parametrize(
        "which, phrase",
        [
            ("READER", "it is where a record's open rows are read from"),
            ("OPTIN", "it is what finds the repository's seal/ root"),
            ("RULES", "it is what reads a spec's `## Rule changes`"),
            (
                "FOLD_CHECK",
                "it is what reads the index and the one read after an apply",
            ),
        ],
    )
    def test_each_sibling_is_refused_with_its_own_purpose(
        self, which, phrase, monkeypatch, capsys
    ):
        """Round 1, ⬜ 5 — #590's second half, per file: the table entry for each
        real sibling, not an entry the case put there itself. A copy taken alone
        stops at `OPTIN` first, so the class case never reaches the other one."""
        path = getattr(settle, which)
        real = os.path.isfile
        monkeypatch.setattr(
            os.path, "isfile", lambda p: False if p == path else real(p)
        )
        with pytest.raises(SystemExit) as raised:
            settle.load(path, "absent")
        assert raised.value.code == 2
        assert phrase in capsys.readouterr().err

    def test_a_missing_sibling_reader_is_a_sentence_and_not_a_traceback(
        self, tmp_path, monkeypatch, capsys
    ):
        """`spec_from_file_location` hands back a spec for any path ending in
        `.py`, present or not, so a missing sibling reaches `exec_module` and dies
        with `FileNotFoundError`. `skills/code-review/scripts/round_record.py#load`
        had that shape until #590; this copy arrived repaired, and this is the
        case that keeps it repaired. Since #590 the refusal is exit 2 on stderr,
        and it names what the missing file is for, per file."""
        missing = str(tmp_path / "not-here.py")
        monkeypatch.setitem(
            settle.PURPOSES, missing, "it is where the fold record is read from"
        )
        with pytest.raises(SystemExit) as raised:
            settle.load(missing, "absent")
        err = capsys.readouterr().err
        assert raised.value.code == 2, raised.value
        assert "not-here.py" in err, err
        assert "fold record" in err, (
            "the refusal does not say what the missing file was for"
        )

    def test_surveys_docstring_does_not_invite_the_mutation_that_reopens_finding_4(
        self,
    ):
        """Round 2, finding 6. `apply` performs the second traversal `survey`'s
        docstring warned against, and the two contradicted each other — the stale
        half being the one a reader meets first. A pin catches the edit; a
        docstring is what a reader consults before making it."""
        import ast

        with open(SCRIPT, encoding="utf-8") as f:
            tree_ = ast.parse(f.read())
        doc = {
            node.name: ast.get_docstring(node) or ""
            for node in tree_.body
            if isinstance(node, ast.FunctionDef)
        }
        assert "the retirement are both derived from" not in doc["survey"], doc[
            "survey"
        ]
        assert "does not take its candidates from here" in doc["survey"], doc["survey"]
        assert "not taken from `survey`" in doc["apply"], doc["apply"]

    def test_every_reader_of_a_retirement_calls_the_one_predicate(self):
        """Three parties ask whether a removed directory was settled, and a
        predicate spelled in each would take the next condition in one and not
        the others. The behaviour is pinned per reader in its own module; this
        pins that this one reaches the answer by calling `settled` on the
        module that owns it, so a reader that re-derives the rule inline goes
        red here even while it agrees today. `tests/test_chain_check.py` holds
        `chain_check.py` to the same."""
        import ast

        script = TARGET.split("/")
        with open(os.path.join(ROOT, *script), encoding="utf-8") as f:
            tree = ast.parse(f.read())
        calls = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "settled"
        ]
        assert calls, (
            f"{'/'.join(script)} decides a removal without asking the predicate"
        )
        assert not [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef) and node.name == "settled"
        ], f"{'/'.join(script)} defines a second `settled`"

    @pytest.mark.parametrize(
        "args, purpose, absent",
        [
            (
                ["--root", "{root}"],
                "it is what finds the repository's seal/ root",
                "fold record",
            )
        ],
        ids=["optin.py"],
    )
    def test_a_script_copied_alone_exits_2_and_names_what_it_misses(
        self, tmp_path, args, purpose, absent
    ):
        """#590. A copy of this script taken without its siblings exits 2, with
        a sentence naming the missing path and what it is for: 2 means the
        input or the tree was unusable and nothing was read, and a sibling that
        is not beside the command is that kind. It loads `hooks/optin.py`
        before it reads the root, so `--root` reaches the loader. The loader
        used to give every file the fold record's purpose, which is false of
        `optin.py`, so that phrase must not appear."""
        script = TARGET
        name = script.rsplit("/", 1)[1]
        alone = tmp_path / "alone"
        alone.mkdir()
        copy = alone / name
        with open(os.path.join(ROOT, *script.split("/")), encoding="utf-8") as f:
            copy.write_text(f.read(), encoding="utf-8")
        repo = tmp_path / "repo"
        repo.mkdir()
        done = subprocess.run(
            [sys.executable, str(copy), *(a.format(root=repo) for a in args)],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            cwd=str(repo),
        )
        assert done.returncode == 2, (done.returncode, done.stderr)
        assert "Traceback" not in done.stderr, done.stderr
        assert names_path(str(alone), done.stderr), (
            f"the refusal does not name the missing path: {done.stderr}"
        )
        assert purpose in done.stderr, (
            f"the refusal does not say what the missing file is for: {done.stderr}"
        )
        if absent:
            assert absent not in done.stderr, done.stderr

    def test_the_pinned_checks_read_under_the_root_alone(self):
        """#688's D3: the constant this command's walk of work items rests on,
        held under `seal/`. Widening it to a top-level `specs/` turns this red,
        which is the probe that work item's plan names for `SPECS`.
        `tests/test_routing.py` holds `hooks/routing.py#WORK_ITEMS` to the
        same, and `tests/test_a_reference_root_is_read_and_never_taken.py`
        classifies every shipped command by what keeps it off a reference
        root."""
        assert settle.SPECS == "seal/specs"


test_census = census_case(TARGET)
