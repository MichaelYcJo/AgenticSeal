"""`settle` reads before it removes: what counts as released, the rule arm
for a spec-less directory, the merge base it asks at, the root it refuses,
and what the documents say about it. How a spec's rule changes are applied is
`tests/test_settle_applies_rule_changes_in_place.py`. #458, closing #83.
"""

import importlib.util
import io
import os
import subprocess
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, "skills", "settle", "scripts", "settle.py")


def load():
    spec = importlib.util.spec_from_file_location("settle", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


settle = load()


def git(repo, *args):
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)


@pytest.fixture
def tree(tmp_path):
    """Four work items: three released, one that arrives after the commit.

    `delta` is this branch's own unreleased work.
    """
    repo = tmp_path / "repo"
    (repo / "docs").mkdir(parents=True)
    (repo / "docs" / "one-root.md").write_text("# a policy\n\nA rule.\n", "utf-8")
    (repo / "seal").mkdir()
    (repo / "seal" / "README.md").write_text("# seal\n", encoding="utf-8")
    for name in ("1700000001-alpha", "1700000002-beta", "1700000003-gamma"):
        item = repo / "seal" / "specs" / name
        item.mkdir(parents=True)
        (item / "spec.md").write_text(f"# {name}\n\nWhat it decided.\n", "utf-8")
    git(repo, "init", "-q")
    git(repo, "config", "user.email", "x@example.com")
    git(repo, "config", "user.name", "x")
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "released")
    later = repo / "seal" / "specs" / "1700000004-delta"
    later.mkdir()
    (later / "spec.md").write_text("# delta\n\nIn flight.\n", encoding="utf-8")
    return repo


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


# --- A3: it names what it would do, and does nothing ------------------------


def test_a_spec_with_no_rule_changes_is_listed_and_kept(tree):
    """A spec written before the section existed has nothing to replay, so it
    is named under its own heading and stays."""
    code, text = run(tree)
    assert code == 0, text
    assert "released with a spec.md: 3 work items, 0 to apply\n" in text, text
    listed = text.split(settle.PREMODEL_HEADING)[1].split("\n\n")[0] + "\n"
    for name in ("1700000001-alpha", "1700000002-beta", "1700000003-gamma"):
        assert f"    {name}\n" in listed, text


def test_the_report_writes_nothing_and_removes_nothing(tree):
    before = sorted(str(p.relative_to(tree)) for p in tree.rglob("*") if p.is_file())
    run(tree)
    after = sorted(str(p.relative_to(tree)) for p in tree.rglob("*") if p.is_file())
    assert before == after, "the report touched the tree"
    assert "Nothing was written and nothing was removed" in run(tree)[1]


def test_an_unreleased_work_item_is_not_a_candidate(tree):
    """Released means present on the branch the release merges to, so this
    branch's own work item is outside the corpus entirely."""
    _, text = run(tree)
    assert "1700000004-delta" not in text, text
    assert "1 unreleased and untouched" in text, text


def test_a_ref_that_does_not_resolve_is_refused_rather_than_empty(tree):
    """The quiet zero this is written against: a ref nothing can read makes
    every work item look unreleased, and the report would then say there is
    nothing to do."""
    assert settle.survey(str(tree), "no/such/ref") is None


def test_apply_removes_only_what_it_applied(tree):
    no_rule(tree, "1700000001-alpha")
    code, text = run(tree, "--apply")
    assert code == 0, text
    assert not (tree / "seal" / "specs" / "1700000001-alpha").exists()
    assert (tree / "seal" / "specs" / "1700000002-beta").exists(), (
        "a spec with no `## Rule changes` was removed"
    )


def test_apply_leaves_a_team_specs_of_the_same_name_on_disk(tree):
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
    assert (team / "design.md").read_text(encoding="utf-8") == "# the team's design\n"
    assert (team / "spec.md").is_file()


# --- D3: a released work item with no spec.md is retired by a rule ---------

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


def test_a_spec_less_directory_is_listed_under_its_own_heading(tree):
    """D3: `settle` prints these under their own heading rather than with
    the specs, because there is nothing to apply."""
    moment(tree, overview=OVERVIEW_CLOSED)
    code, text = run(tree)
    assert code == 0, text
    assert "retired by the rule" in text, text
    assert MOMENT in text.split("retired by the rule")[1], text
    premodel = text.split(settle.PREMODEL_HEADING)[1].split("\n\n")[0]
    assert MOMENT not in premodel, text


def test_the_rule_arm_removes_it_with_no_marker(tree):
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


def test_an_open_memo_row_keeps_a_spec_less_directory(tree):
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


def test_a_closed_row_is_told_to_merge_before_its_directory_goes(tree):
    """Round 1's finding 2. The CI readers ask the rule of the merge base, so
    a row closed and its directory retired in one pull request is refused
    there after `settle` said the removal was fine. The report, the
    skill and the policy all say the closure merges first."""
    moment(tree, overview=OVERVIEW_OPEN)
    _, text = run(tree)
    assert "in a pull request merged before the one that retires the directory" in (
        flat(text)
    ), text
    assert "merge first" in flat(skill()), (
        "the skill lets a settle close a row and retire its directory in one "
        "pull request, which the CI readers refuse at the merge base"
    )
    assert "in a pull request merged before the one that retires" in document(
        "docs", "the-record-layout.md"
    )


# --- #602: the closure has to reach the release's base first ----------------

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


def test_a_closure_the_base_has_not_seen_keeps_the_directory(tree):
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


def test_an_uncommitted_closure_keeps_the_directory(tree):
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


def test_a_closure_the_base_has_seen_lets_the_directory_go(tree):
    """S6, the counter-case that keeps S4 from passing by refusing
    everything: once the closure has merged into the base, the rule holds at
    both and the directory goes with no marker."""
    closed_after_base(tree)
    git(tree, "branch", "-f", BASE, "HEAD")
    code, text = at(tree, BASE, "--apply")
    assert not (tree / "seal" / "specs" / MOMENT).exists(), text
    assert f"removed seal/specs/{MOMENT}/" in text, text
    assert code == 0, text


def test_the_report_does_not_promise_what_the_retirement_refuses(tree):
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
    # nothing pinned the new words (contract §14).
    assert f"1 kept because the closure has not reached {BASE}" in text, text


def test_the_base_heading_says_where_the_closure_has_to_go():
    """§14: the sentence a person acts on is pinned, not only its presence."""
    heading = flat(settle.RULE_BASE_HEADING.format(base="origin/main"))
    assert "origin/main" in heading, heading
    assert "the branch the release merges to" in heading, heading
    assert "a later pull request" in heading, heading


def test_the_documents_say_the_closure_has_to_reach_the_base():
    """S11, §14's half of #602: the skill, the policy, both cheat-sheet rows,
    the kept heading and the module docstring say the rule is asked at the
    merge base of `--released-at` and `HEAD`, and what a person does about a
    directory kept there."""
    text = flat(skill())
    assert "*kept until the closure reaches <base>*" in text, text
    # #611: `base_heading` prints `RULE_MOVED_HEADING` instead once
    # `--released-at` has moved past the fork, and the skill named only the
    # first of the two wordings.
    assert "*kept: the closure has not reached <base>*" in text, text
    assert "Merged first means merged to the branch the release merges to" in text
    assert "the merge base of `--released-at` and `HEAD`" in text
    policy = flat(document("docs", "the-record-layout.md"))
    assert "`settle` asks it at the merge base of `--released-at` and `HEAD`" in policy
    # Round 1, 🟡 1: that merge base is CI's only until the base moves.
    assert "until the base moves past the fork" in policy, policy
    # Round 2, ⬜ 5: `document` flattens, so a split on a newline took the rest
    # of the file as the row. The raw file is read, so the row is the row.
    for edition, phrase in (
        ("README.md", "until `--released-at` moves on past that commit"),
        ("README.ko.md", "앞으로 나아가기 전까지는"),
    ):
        with open(os.path.join(ROOT, edition), encoding="utf-8") as f:
            row = f.read().split("`settle [--apply]`")[1].split("\n")[0]
        assert "`--released-at`" in row and "`HEAD`" in row, (
            f"{edition}'s cheat-sheet row does not say the base is asked"
        )
        # Round 2, 🟡 1: CI's revision is the fork only until the base moves.
        assert phrase in row, row
        assert "because that is where CI asks" not in row, row
        assert "CI 가 그 지점에서 확인하기 때문입니다" not in row, row
    assert "which is the base's tip" in text, text
    assert "merging it into this branch and running `settle`" in text, text
    assert "to the branch the release merges to" in flat(settle.RULE_KEPT_HEADING)
    with open(SCRIPT, encoding="utf-8") as f:
        head = flat(f.read().split('"""')[1])
    assert "sharing no commit with `HEAD`" in head, "exit 2's seventh state is missing"
    assert "closure has not reached the merge base" in head, "exit 1's cause is missing"


def test_a_base_that_moved_past_the_fork_names_the_merge_that_moves_it(tree):
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


def test_the_report_refuses_a_survey_with_no_base(tree):
    """Round 1, ⬜ 4. `report` is the third reader of `survey`'s dict, and it
    refuses a base-less one the way `apply` does rather than raising
    `KeyError` on the keys that dict does not carry."""
    moment(tree, overview=OVERVIEW_CLOSED)
    out = io.StringIO()
    code = settle.report({"base": None, "base_label": None}, "HEAD", out=out)
    assert code == 2, out.getvalue()
    assert "no merge base" in out.getvalue(), out.getvalue()


def test_a_shallow_clone_is_not_told_the_refs_share_no_commit(tree, tmp_path, capsys):
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


def test_the_apply_refuses_a_survey_with_no_base(tree):
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


@pytest.mark.parametrize("apply", [False, True])
def test_no_merge_base_is_refused_and_nothing_is_removed(tree, apply, capsys):
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


def test_an_unreadable_memo_keeps_a_spec_less_directory(tree):
    """A section this cannot read is a count it does not know, never zero."""
    moment(tree, overview="# x — overview\n\n## Not checked\n")
    code, text = run(tree, "--apply")
    assert code == 1, text
    assert (tree / "seal" / "specs" / MOMENT).exists(), text
    assert "cannot be read" in text, text


def test_an_unreleased_spec_less_directory_is_not_a_candidate(tree):
    item = tree / "seal" / "specs" / MOMENT
    item.mkdir()
    (item / "routing.md").write_text("# routing\n", encoding="utf-8")
    _, text = run(tree, "--apply")
    assert item.exists(), text


def test_the_report_lists_what_an_apply_would_remove(tree):
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


@pytest.mark.parametrize("ref", [None, "HEAD"])
def test_the_predicate_asks_every_condition_itself(tree, ref):
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
    assert not ok("1700000002-beta"), "a rule the tree does not hold read as applied"
    assert not ok("1700000008-with-memo")
    assert not ok("1700009999-nowhere"), "a directory that never existed was settled"
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


def test_the_predicate_is_what_settle_asks(tree, monkeypatch):
    """One predicate, asked by every reader. With it answering nothing, the
    rule arm lists nothing."""
    moment(tree)
    reader = settle.load(settle.READER, "specseal_unverified_reader")
    real_load = settle.load
    monkeypatch.setattr(reader, "settled", lambda root, ref, dirs, here=None: set())
    monkeypatch.setattr(
        settle,
        "load",
        lambda path, name: reader if path == settle.READER else real_load(path, name),
    )
    _, text = run(tree, "--apply")
    assert (tree / "seal" / "specs" / MOMENT).exists(), text


def test_the_documents_say_a_spec_less_directory_is_retired_by_the_rule():
    """§14's half of D3. The policy said such an item *is kept by name*; that
    is overturned, and the one condition the frame added is stated where the
    owner can overturn it."""
    policy = document("docs", "the-record-layout.md")
    assert "and it is kept by name" not in policy, (
        "the policy still keeps a spec-less directory by name"
    )
    assert "it is retired by that rule, with no marker" in policy
    assert "nothing in the record may still be open" in policy
    assert "a judgment the repository owner may overturn" in policy
    text = flat(skill())
    assert "A released work item with no `spec.md` states no rule" in text
    assert "*retired by the rule*" in text and "*kept by the rule*" in text
    for edition in ("README.md", "README.ko.md"):
        assert "`spec.md`" in document(edition).split("`settle [--apply]`")[1][:900], (
            f"{edition}'s cheat-sheet row does not name the rule arm"
        )


# --- what ships ------------------------------------------------------------


def test_the_command_is_reachable_by_the_name_a_document_gives_it():
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
        ("FOLD_CHECK", "it is what reads the index and the one read after an apply"),
    ],
)
def test_each_sibling_is_refused_with_its_own_purpose(
    which, phrase, monkeypatch, capsys
):
    """Round 1, ⬜ 5 — #590's second half, per file: the table entry for each
    real sibling, not an entry the case put there itself. A copy taken alone
    stops at `OPTIN` first, so the class case never reaches the other one."""
    path = getattr(settle, which)
    real = os.path.isfile
    monkeypatch.setattr(os.path, "isfile", lambda p: False if p == path else real(p))
    with pytest.raises(SystemExit) as raised:
        settle.load(path, "absent")
    assert raised.value.code == 2
    assert phrase in capsys.readouterr().err


def test_a_missing_sibling_reader_is_a_sentence_and_not_a_traceback(
    tmp_path, monkeypatch, capsys
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


# --- what the skill has to say ---------------------------------------------

SKILL = os.path.join(ROOT, "skills", "settle", "SKILL.md")


def skill():
    with open(SKILL, encoding="utf-8") as f:
        return f.read()


def flat(text):
    return " ".join(text.split())


def test_the_skill_names_the_floors_a_fold_has_to_answer():
    """A11. `docs/one-root-by-lifetime.md` §*The dependency rule* names two
    readers and the real list is longer — fourteen test modules read this
    repository's own corpus and at least six carry a population floor. A
    session that folds without answering them removes the population its own
    suite was asserting over, and the commit under review is what broke it.

    The three answers are named because the fourth — lowering the floor until
    the run passes — is the one that turns a check into a comment."""
    text = flat(skill())
    assert "population floor" in text, (
        "the skill never tells a session that its own checks read the corpus"
    )
    assert "is not the whole list" in text, (
        "the skill lets `docs/one-root-by-lifetime.md`'s two readers stand as "
        "the whole list, which is what makes a fold turn a suite red"
    )
    for answer in ("retire the case", "re-point it at a fixture corpus", "decline"):
        assert answer in text, f"the skill does not offer `{answer}`"


def test_the_skill_says_the_spec_judges_and_the_command_applies():
    """#953: the judgment is made when the spec is written and reviewed, so a
    session running `settle` writes no policy prose."""
    text = flat(skill())
    assert "moves and does not verify" in text, text[:200]
    assert "The spec decides; the command applies." in text
    assert "you judge and write" not in text


def test_the_skill_says_a_settle_is_not_a_work_item_and_owes_no_range_row():
    """#517's D1: a settle with no work item has no directory, so the skill
    hands it no row shape to copy, and says how it commits instead."""
    text = flat(skill())
    assert "| Range | Grounds |" not in text, (
        "the skill still hands a settle a range row"
    )
    assert "## A settle is not a work item" in skill()
    assert "A settle opens no directory under `seal/specs/`" in text
    assert "`: '[no-review]';`" in text, "the skill does not say how a settle commits"
    assert "reviewed at its pull request" in text
    assert "keeps no log" in text


def test_the_skill_says_the_directory_goes_with_the_rule_it_applied():
    text = flat(skill())
    assert "A directory goes only with the rule changes it applied" in text


def test_the_skill_states_how_the_changes_land():
    """#953: in place, in merge order, the later spec winning, and no
    marker."""
    text = flat(skill())
    assert "in merge order" in text
    assert "the later spec wins" in text
    assert "No marker is written" in text
    assert "<!-- specs/" not in text


def test_the_skill_says_it_fails_no_build():
    """G5. `settle` is invoked, never triggered — the ticket's own *Not this*."""
    text = flat(skill())
    assert "It is invoked, never triggered" in text
    assert "It does not fail a build." in text


# --- A9: no document still describes a `settle` that does not exist --------


def document(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as f:
        return flat(f.read())


@pytest.mark.parametrize(
    "parts", [("seal", "README.md"), ("templates", "seal-README.md")]
)
def test_the_seal_readme_says_the_step_exists(parts):
    """Both editions of the same file, which
    `tests/test_first_setup_asks_once.py` holds byte for byte. It has said a
    work item "waits until a later `settle` folds it" since the root existed,
    and a reader who went looking for the step found nothing."""
    text = document(*parts)
    assert "settle --apply" in text and "skills/settle/SKILL.md" in text
    assert "A settle is not a work item and opens no directory here." in text, (
        f"{'/'.join(parts)} does not say a settle opens no work item (#517)"
    )
    assert "wrote no `spec.md` and holds nothing open" in text
    assert "retire-process" not in text and "folds it" not in text


def test_the_implement_skill_states_the_model():
    """S15. The policy root is the baseline a pull request does not edit, and
    the policy in force is it plus every unsettled spec's rule changes in
    merge order. The sentence it replaced made `settle` the one writer of a
    policy document a session wrote by hand."""
    text = document("skills", "implement", "SKILL.md")
    assert "one writer that does is `settle`" not in text
    assert "is the baseline, and a pull request does not edit it" in text
    assert "plus the rule changes of every unsettled spec, in merge order" in text


@pytest.mark.parametrize(
    "parts", [("agents", "framer.md"), ("README.md",), ("README.ko.md",)]
)
def test_every_other_carrier_points_to_the_model(parts):
    """S15. The model has one home, and every other carrier links to it."""
    text = document(*parts)
    assert "one writer that does is `settle`" not in text, "/".join(parts)
    assert (
        "`skills/implement/SKILL.md` §*Document layout — two roots, three lifetimes*"
        in text
    ), "/".join(parts)


@pytest.mark.parametrize(
    "parts, heading",
    [
        (("docs", "one-root-by-lifetime.md"), "## Decided when `settle` was built"),
        (("docs", "one-root-by-lifetime.ko.md"), "## `settle` 을 만들면서 정해진 것"),
    ],
)
def test_the_design_record_takes_the_later_decision_as_a_dated_section(parts, heading):
    """`tests/test_no_document_names_the_old_roots.py#DESIGN_RECORD`
    classifies this document as a record of a moment, and a record of a moment
    is not rewritten. The shape it already uses for a later decision is a
    dated section, and both editions take one."""
    text = document(*parts)
    assert heading in text, f"{'/'.join(parts)} carries no dated section for #458"
    assert "2026-09-22" in text
    assert "2026-09-02" in text, (
        "the dated section no longer says which text it is leaving alone"
    )


@pytest.mark.parametrize(
    "parts, heading",
    [
        (
            ("docs", "one-root-by-lifetime.md"),
            "## Decided when the fold stopped being a work item (2026-09-23)",
        ),
        (
            ("docs", "one-root-by-lifetime.ko.md"),
            "## fold 가 작업 항목이 아니게 되면서 정해진 것 (2026-09-23)",
        ),
    ],
)
def test_the_design_record_takes_d1_as_a_dated_section(parts, heading):
    """#517's D1 overturns the 2026-09-22 row that made the fold its own work
    item, and a record of a moment takes the overturning as a new dated
    section rather than an edit to the row."""
    text = document(*parts)
    assert heading in text, f"{'/'.join(parts)} carries no dated section for #517"
    later = text.split(heading, 1)[1]
    assert "2026-09-02" in later and "2026-09-22" in later, (
        "the new section does not say which two records it leaves alone"
    )
    assert "[no-review]" in later


DATED_SECTIONS = (
    ("## Decided when `settle` was built", "## `settle` 을 만들면서 정해진 것"),
    (
        "## Decided when the fold stopped being a work item",
        "## fold 가 작업 항목이 아니게 되면서 정해진 것",
    ),
    # #729: the process record leaves after its release, without the fold.
    (
        "## Decided when the process record stopped waiting for the fold",
        "## 과정의 기록이 fold 를 기다리지 않게 되면서 정해진 것",
    ),
)


def section(flat_text, heading):
    """A dated section of a flattened document, from its heading to the next."""
    rest = flat_text.split(heading, 1)[1]
    return rest.split(" ## ", 1)[0]


def test_both_editions_took_the_same_decisions():
    """`CONTRIBUTING.md` requires the two editions to move together, and a
    mirror drifts one edit at a time. The rows are prose in two languages, so
    what is compared is that each edition's section has as many rows as the
    other's."""
    en = document("docs", "one-root-by-lifetime.md")
    ko = document("docs", "one-root-by-lifetime.ko.md")
    # Each section is read up to the next `## ` heading, so a later dated
    # section is compared with its own twin rather than counted into this
    # one's (#517 added the second).
    for en_heading, ko_heading in DATED_SECTIONS:
        sections = (section(en, en_heading), section(ko, ko_heading))
        rows = tuple(s.count("|---|---|---|") for s in sections)
        assert rows == (1, 1), (en_heading, rows)
        counted = tuple(s.count(" | ") for s in sections)
        assert counted[0] == counted[1], (
            f"{en_heading}: the English section holds {counted[0]} cells and "
            f"the Korean {counted[1]} — one edition took a decision the other "
            "did not"
        )


# --- what the plugin says it ships -----------------------------------------


def test_the_release_checklist_carries_the_by_hand_step():
    """G5. `settle` is invoked and never triggered, so the only thing that
    makes it happen is a line in the list somebody works down on the day."""
    text = document("docs", "release-checklist.md")
    assert "settle --apply" in text, "the checklist never names the step"
    assert "retire-process" not in text and "settle --retire" not in text
    assert "A settle is not a work item" in text, (
        "the checklist does not say the settle opens no work item"
    )
    assert "range-row" not in text, "the checklist still owes a settle a range row"
    assert "skills/settle/SKILL.md" in text
    # Round 1, finding 10: a document past the ceiling is a report (Q6), and
    # the checklist points to the skill's section rather than ordering a split.
    assert (
        "`skills/settle/SKILL.md` *A document past its ceiling is split, never "
        "trimmed*" in " ".join(text.split())
    )
    assert "split along its headings in the same pull request" not in text


@pytest.mark.parametrize("edition", ["README.md", "README.ko.md"])
def test_both_cheat_sheets_carry_the_command(edition):
    """The count and the name are derived by
    `tests/test_chain_hooks_hardening.py`; what nothing derives is the row a
    reader actually types from. `CONTRIBUTING.md` requires the two editions to
    move together and the hygiene workflow only warns about it."""
    text = document(edition)
    assert "`settle [--apply]`" in text, (
        f"{edition}'s cheat sheet has no row for the command"
    )
    # The raw file is read, so the row is the row.
    with open(os.path.join(ROOT, edition), encoding="utf-8") as f:
        row = f.read().split("`settle [--apply]`")[1].split("\n")[0]
    assert "`## Rule changes`" in row, row
    assert "retire" not in row, row


# --- round 1's fixes -------------------------------------------------------


def test_local_mode_is_refused_rather_than_read_as_an_empty_repository(tmp_path):
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


def test_a_repository_with_no_root_at_either_place_says_so(tmp_path):
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


def test_an_apply_with_nothing_to_do_is_no_refusal(tree):
    """Exit 1 is a refusal, and a tree whose specs predate the section
    refuses nothing: the run says what it did, which is nothing, and exits
    0."""
    before = sorted(str(p.relative_to(tree)) for p in tree.rglob("*") if p.is_file())
    code, text = run(tree, "--apply")
    assert code == 0, text
    assert "applied 0 specs and removed 0 directories; 0 refused or kept" in text
    # The summary is the line read to decide whether the settle is finished,
    # so the specs it leaves in place are counted there too (round 1, 8).
    assert "; 3 with no `## Rule changes`, left in place\n" in text, text
    after = sorted(str(p.relative_to(tree)) for p in tree.rglob("*") if p.is_file())
    assert before == after, text


# --- round 2's fixes -------------------------------------------------------


def test_an_opted_out_repository_is_told_which_state_it_is_in(tmp_path):
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


def test_a_directory_of_the_markers_name_is_not_an_opt_out(tmp_path):
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


def test_the_refusal_path_asks_for_the_common_directory_once(tmp_path, monkeypatch):
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


def test_the_released_at_refusal_is_about_the_ref_and_nothing_else(tmp_path):
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
        [sys.executable, SCRIPT, "--root", str(repo), "--released-at", "no/such/ref"],
        capture_output=True,
        encoding="utf-8",
    )
    assert r.returncode == 2, r.stdout + r.stderr
    assert "does not resolve" in r.stderr, r.stderr
    assert "local mode" not in r.stderr, (
        "the ref refusal still talks about a state it cannot be in"
    )


def test_the_module_and_the_skill_both_say_local_mode_is_refused():
    """Round 2, finding 3 — §14's other half. The exit-code list named three
    causes of exit 2 and there were four, and the one document a session reads
    before it folds said nothing about the refusal at all. A person whose root
    sits under the git directory meets a stop no document predicted."""
    with open(SCRIPT, encoding="utf-8") as f:
        head = f.read().split('"""')[1]
    assert "Exit codes" in head, "the docstring no longer documents exit codes"
    assert "local mode" in head, "exit 2 covers a local-mode root and the list does not"
    assert "opted out" in head, "exit 2 covers the opt-out and the list does not"
    text = flat(skill())
    assert "refuses to run in local mode" in text, (
        "the skill never tells a session that this command stops in local mode"
    )
    assert "seal mode shared" in text, "the skill does not give the way out"


def test_surveys_docstring_does_not_invite_the_mutation_that_reopens_finding_4():
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
    assert "the retirement are both derived from" not in doc["survey"], doc["survey"]
    assert "does not take its candidates from here" in doc["survey"], doc["survey"]
    assert "not taken from `survey`" in doc["apply"], doc["apply"]


# --- G7: an empty seal/specs/ is not one state but two, and both are green --


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


@pytest.mark.rule("an-empty-root-is-settled")
@pytest.mark.parametrize("keep_empty_dir", [True, False], ids=["empty", "absent"])
@pytest.mark.parametrize("apply", [False, True], ids=["report", "apply"])
def test_a_settled_root_is_green_and_says_so(tmp_path, keep_empty_dir, apply):
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
