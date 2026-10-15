"""`skills/code-review/scripts/chain_check.py`, one group per function.

Each group holds a case on good input and a case on bad input. The `main`
group runs the check end to end over a real git repository: a branch with a
routing declaration, a round record and a `broad-gate.md`, judged as a ready
or a draft pull request through the event payload GitHub writes.
"""

import importlib.util
import json
import os
import pathlib
import re
import subprocess

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHAIN = ROOT / "skills" / "code-review" / "scripts" / "chain_check.py"
READER = ROOT / "skills" / "verify" / "scripts" / "unverified_check.py"
ITEM = "seal/specs/1791999999-a-work-item"


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


chain = load(CHAIN, "chain_check_under_test")
reader = load(READER, "unverified_reader_for_chain_tests")


def git(d, *args):
    return subprocess.run(
        ["git", "-C", str(d), *args],
        check=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    ).stdout.strip()


def write(d, rel, text):
    p = pathlib.Path(d) / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def commit(d, message):
    git(d, "add", "-A")
    git(d, "commit", "-qm", message)
    return git(d, "rev-parse", "HEAD")


ROUTING = """# a work item -- routing

| Axis | Answer |
|---|---|
| Review | {review} |
| Destination | open the pull request |
| Planning | {planning} |
| Branch | feature/x |
"""


def record(target, rows):
    """A round record in the new shape, with `rows` as its verdict rows."""
    body = "\n".join(rows)
    return (
        "# 1791999999-a-work-item — review round 1\n\n"
        "| Field | Value |\n|---|---|\n"
        f"| Target SHA | {target} against main |\n\n"
        "## Verdicts\n\n"
        "| # | Finding | Location | Verdict | Grounds |\n"
        "|---|---|---|---|---|\n"
        f"{body}\n\n"
        "## Paste-ready fixes\n\n"
        "## Executed probes\n\n"
        "| What was run | Result |\n|---|---|\n"
    )


def gate_file(sha):
    return (
        "# 1791999999-a-work-item — broad gate\n\n"
        "| Field | Value |\n|---|---|\n"
        f"| Broad gate | {sha} against main |\n"
    )


SPEC = "# spec\n\nbody\n\nFramed 2026-10-15 by framer, before the build.\n"


@pytest.fixture
def branch(tmp_path):
    """A repository whose `feature/x` declares a work item and reviewed it.

    `main` holds one file. `feature/x` adds the declaration, a code commit,
    the round record at that commit with every finding closed, and
    `broad-gate.md` naming the code commit. Returns `(root, code commit)`.
    """
    d = tmp_path / "r"
    d.mkdir()
    git(d, "init", "-q", "-b", "main")
    git(d, "config", "user.email", "t@t")
    git(d, "config", "user.name", "t")
    write(d, "f.txt", "one\n")
    commit(d, "base")
    git(d, "switch", "-q", "-c", "feature/x")
    write(
        d,
        f"{ITEM}/routing.md",
        ROUTING.format(review="through the review chain", planning="the session"),
    )
    commit(d, "routing")
    write(d, "f.txt", "two\n")
    code = commit(d, "code")
    write(
        d,
        f"{ITEM}/rounds/round-1.md",
        record(code, ["| 🔴 1 | wrong | `f.txt:1` | fixed " + code[:8] + " | g |"]),
    )
    # Two runs, newest first: the earlier one names a commit nobody can see,
    # so a reader that took any run but the first would refuse the file.
    write(
        d,
        f"{ITEM}/broad-gate.md",
        gate_file(f"{code} against main; earlier run: {'1' * 40}"),
    )
    commit(d, "the round record and the broad gate")
    return d, code


@pytest.fixture
def ready(tmp_path, monkeypatch):
    event = tmp_path / "event.json"
    event.write_text(json.dumps({"pull_request": {"draft": False}}), encoding="utf-8")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event))
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
    monkeypatch.delenv("GITHUB_HEAD_REF", raising=False)


@pytest.fixture
def draft(tmp_path, monkeypatch):
    event = tmp_path / "event.json"
    event.write_text(json.dumps({"pull_request": {"draft": True}}), encoding="utf-8")
    monkeypatch.setenv("GITHUB_EVENT_PATH", str(event))
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)
    monkeypatch.delenv("GITHUB_HEAD_REF", raising=False)


def check(root, capsys, *extra):
    code = chain.main(["--baseline", "main", "--root", str(root), *extra])
    return code, capsys.readouterr().out


# --- changed ------------------------------------------------------------------


def two_declarations(tmp_path):
    """`main` holds one declaration; `feature/y` checked out, nothing yet."""
    d = tmp_path / "c"
    d.mkdir()
    git(d, "init", "-q", "-b", "main")
    git(d, "config", "user.email", "t@t")
    git(d, "config", "user.name", "t")
    old = ROUTING.format(review="straight to the PR", planning="the session")
    write(d, "seal/specs/1788000000-old/routing.md", old)
    commit(d, "base")
    git(d, "switch", "-q", "-c", "feature/y")
    return d, old


class TestChanged:
    def test_a_declaration_moved_unchanged_is_neither_judged_nor_missed(self, tmp_path):
        """A move of the whole root renames every declaration at once, and a
        declaration the pull request only moved is not one it made (#90)."""
        d, _old = two_declarations(tmp_path)
        git(d, "mv", "seal/specs/1788000000-old", "seal/specs/1788000000-moved")
        commit(d, "moved")
        paths, renamed = chain.changed(str(d), "main")
        assert renamed == {
            "seal/specs/1788000000-old/routing.md",
            "seal/specs/1788000000-moved/routing.md",
        }
        assert chain.changed_routing(paths, renamed, "seal/specs") == []

    def test_a_move_not_yet_committed_is_read_from_the_files(
        self, tmp_path, monkeypatch
    ):
        """Under `--worktree` an untracked file has no blob git can name, so
        the moved file's bytes are hashed to pair it."""
        d, _old = two_declarations(tmp_path)
        os.rename(d / "seal/specs/1788000000-old", d / "seal/specs/1788000000-moved")
        monkeypatch.setattr(chain, "WORKTREE", True)
        _paths, renamed = chain.changed(str(d), "main")
        assert renamed == {
            "seal/specs/1788000000-old/routing.md",
            "seal/specs/1788000000-moved/routing.md",
        }

    def test_a_deletion_beside_a_similar_addition_is_not_read_as_a_rename(
        self, tmp_path
    ):
        """Two declarations from one template differ in a row or two, which
        git's rename detection pairs. The check reads declarations, not file
        identity, so the deletion is seen."""
        d, old = two_declarations(tmp_path)
        git(d, "rm", "-q", "seal/specs/1788000000-old/routing.md")
        write(
            d,
            "seal/specs/1791999999-new/routing.md",
            old.replace("feature/x", "feature/y"),
        )
        commit(d, "one leaves, one arrives")
        paths, renamed = chain.changed(str(d), "main")
        assert renamed == set()
        assert chain.changed_routing(paths, renamed, "seal/specs") == [
            "seal/specs/1788000000-old/routing.md",
            "seal/specs/1791999999-new/routing.md",
        ]


# --- verdict_of ---------------------------------------------------------------


class TestVerdictOf:
    def test_a_closing_word_is_read_through_emphasis_and_a_commit(self):
        for cell, word in (
            ("fixed 1a2b3c4d", "fixed"),
            ("**fixed** `1a2b3c4d`", "fixed"),
            ("answered", "answered"),
            ("deferred #12", "deferred"),
            ("confirmed", "confirmed"),
            ("❓ out of verified scope", "out of verified scope"),
        ):
            assert chain.verdict_of([cell], 0) == word
            assert chain.verdict_of([cell], 0) in chain.CLOSED_WORDS

    def test_open_an_unknown_word_and_a_homeless_deferral_stay_open(self):
        for cell in ("open", "not fixed", "deferred", "deferred —", ""):
            assert chain.verdict_of([cell], 0) not in chain.CLOSED_WORDS


# --- deferred_home and issue_of -----------------------------------------------


class TestDeferredHome:
    def test_the_home_after_the_word_is_read(self):
        assert chain.deferred_home("deferred #12") == "#12"
        assert chain.issue_of(chain.deferred_home("deferred #12")) == 12
        assert chain.deferred_home("deferred `seal/follow-up.md`") == (
            "seal/follow-up.md"
        )

    def test_no_home_and_prose_name_no_issue(self):
        assert chain.deferred_home("deferred") is None
        assert chain.deferred_home("deferredness #12") is None
        assert chain.deferred_home("fixed abc1234") is None
        assert chain.issue_of(chain.deferred_home("deferred to #664")) is None


# --- verdict_table ------------------------------------------------------------


class TestVerdictTable:
    def test_the_rows_under_the_heading_are_read(self):
        lines = reader.readable(record("abc1234", ["| 🔴 1 | x | `a:1` | open | g |"]))
        rows, col, header, errors = chain.verdict_table(reader, lines, "r.md")
        assert errors == []
        assert header[col] == "verdict"
        assert [seen[0] for _n, seen in rows] == ["🔴 1"]

    def test_the_template_is_the_table_the_check_reads(self):
        text = (ROOT / "templates" / "sdd-round.md").read_text(encoding="utf-8")
        found, errors = chain.open_findings(reader, reader.readable(text), "t")
        assert errors == []
        assert [(mark, word) for _n, mark, word in found] == [("🔴 1", "open")]
        head = text.split(chain.VERDICTS)[0]
        rows = chain.table_rows(reader, reader.readable(head))
        labels = [c[0].strip() for c in rows if "-" not in c[0]]
        assert labels == ["Field", "Target SHA"]

    def test_a_record_with_no_verdicts_section_is_an_error(self):
        lines = reader.readable("# r\n\n| Field | Value |\n|---|---|\n")
        rows, col, _header, errors = chain.verdict_table(reader, lines, "r.md")
        assert rows == [] and col == -1
        assert "no `## Verdicts` section" in errors[0][2]


# --- open_findings ------------------------------------------------------------


class TestOpenFindings:
    def test_a_closed_blocking_row_and_rows_that_are_no_finding_pass(self):
        lines = reader.readable(
            record(
                "abc1234",
                [
                    "| 🔴 1 | x | `a:1` | fixed abc1234 | g |",
                    "| 🟡 2 | x | `a:2` | deferred #9 | g |",
                    "| 🟢 | x | `a:3` | confirmed | g |",
                    "| ❓ | x | `a:4` | ❓ out of verified scope | g |",
                    "| ⬜ 3 | an old record's note | `a:5` | open | g |",
                ],
            )
        )
        found, errors = chain.open_findings(reader, lines, "r.md")
        assert (found, errors) == ([], [])

    def test_an_open_red_or_yellow_row_is_named_by_line_id_and_word(self):
        lines = reader.readable(
            record(
                "abc1234",
                [
                    "| 🔴 1 | x | `a:1` | open | g |",
                    "| 🟡 2 | x | `a:2` | deferred | g |",
                ],
            )
        )
        found, errors = chain.open_findings(reader, lines, "r.md")
        assert errors == []
        assert [(mark, word) for _line, mark, word in found] == [
            ("🔴 1", "open"),
            ("🟡 2", "deferred (no home)"),
        ]
        assert found[0][0] == lines.index("| 🔴 1 | x | `a:1` | open | g |") + 1


# --- follows ------------------------------------------------------------------


class TestFollows:
    def test_head_and_record_commits_after_it_pass(self, branch):
        root, code = branch
        assert chain.follows(str(root), code, "main", ITEM) is None

    def test_a_code_commit_after_it_and_an_unseen_commit_are_named(self, branch):
        root, code = branch
        write(root, "f.txt", "three\n")
        later = commit(root, "a fix nobody reviewed")
        found = chain.follows(str(root), code, "main", ITEM)
        assert found[0] == "after" and found[1] == later and found[2] == "f.txt"
        assert chain.follows(str(root), "0" * 40, "main", ITEM)[0] == "unseen"

    def test_another_items_records_and_a_commit_off_the_branch_are_named(self, branch):
        root, code = branch
        write(root, "seal/specs/1791999998-another-item/routing.md", "x\n")
        later = commit(root, "another work item's file")
        found = chain.follows(str(root), code, "main", ITEM)
        assert found[:2] == ("after", later)
        git(root, "switch", "-q", "main")
        write(root, "g.txt", "elsewhere\n")
        off = commit(root, "a commit the branch never had")
        git(root, "switch", "-q", "feature/x")
        assert chain.follows(str(root), off, "main", ITEM)[0] == "off"


# --- frame --------------------------------------------------------------------


class TestFrame:
    def declared(self):
        return {"planning": "framer", "review": "through the review chain"}

    def routing(self):
        return load(ROOT / "hooks" / "routing.py", "routing_for_chain_tests")

    def test_a_framed_item_with_a_reframe_by_the_framer_passes(self, branch):
        root, _code = branch
        write(
            root,
            f"{ITEM}/spec.md",
            SPEC + "Reframed 2026-10-16 by framer, after round 2.\n",
        )
        write(root, f"{ITEM}/plan.md", "# plan\n")
        commit(root, "frame")
        assert (
            chain.frame(reader, self.routing(), str(root), ITEM, self.declared()) == []
        )

    def test_a_missing_plan_and_a_reframe_by_another_party_are_named(self, branch):
        root, _code = branch
        write(
            root,
            f"{ITEM}/spec.md",
            SPEC + "Reframed 2026-10-16 by the session, after round 2.\n",
        )
        commit(root, "frame")
        problems = chain.frame(reader, self.routing(), str(root), ITEM, self.declared())
        assert any("plan.md" in p for p in problems)
        assert any("Reframed 2026-10-16 by the session" in p for p in problems)


# --- main: the arms over a pull request ---------------------------------------


class TestMain:
    def test_a_reviewed_branch_passes_a_ready_pull_request(self, branch, ready, capsys):
        root, _code = branch
        code, out = check(root, capsys)
        assert code == 0, out

    def test_an_open_verdict_fails_a_ready_pull_request(
        self, branch, ready, capsys, monkeypatch
    ):
        """S3 (T11): the rows decide, the row id and the word are named, and a
        draft prints the same line and passes."""
        root, code_sha = branch
        rel = f"{ITEM}/rounds/round-1.md"
        write(
            root,
            rel,
            record(code_sha, ["| 🔴 1 | wrong | `f.txt:1` | open | g |"]),
        )
        commit(root, "the record, still open")
        code, out = check(root, capsys)
        assert code == 1
        line = next(ln for ln in out.splitlines() if "🔴 1" in ln)
        assert line.startswith(f"{rel}:")
        assert "`open`" in line
        event = pathlib.Path(os.environ["GITHUB_EVENT_PATH"])
        event.write_text(
            json.dumps({"pull_request": {"draft": True}}), encoding="utf-8"
        )
        code, out = check(root, capsys)
        assert code == 0
        assert any("🔴 1" in ln and "`open`" in ln for ln in out.splitlines())

    def test_the_last_record_is_at_head_or_only_record_commits_follow(
        self, branch, ready, capsys
    ):
        """S4 (T12): a record commit after the last record passes; a code
        commit after it fails naming the commit and the verifying round."""
        root, _code = branch
        write(root, f"{ITEM}/overview.md", "# overview\n")
        commit(root, "a record commit")
        code, out = check(root, capsys)
        assert code == 0, out
        write(root, "f.txt", "three\n")
        later = commit(root, "a fix after the last round")
        code, out = check(root, capsys)
        assert code == 1
        assert later[:8] in out and "a verifying round is owed" in out

    def test_a_chain_with_no_record_fails_ready_and_prints_on_a_draft(
        self, tmp_path, monkeypatch, capsys, branch
    ):
        root, _code = branch
        git(root, "rm", "-rq", f"{ITEM}/rounds")
        commit(root, "no record")
        event = tmp_path / "e.json"
        event.write_text(
            json.dumps({"pull_request": {"draft": False}}), encoding="utf-8"
        )
        monkeypatch.setenv("GITHUB_EVENT_PATH", str(event))
        code, out = check(root, capsys)
        assert code == 1 and "holds no `round-N.md`" in out
        event.write_text(
            json.dumps({"pull_request": {"draft": True}}), encoding="utf-8"
        )
        code, out = check(root, capsys)
        assert code == 0 and "holds no `round-N.md`" in out

    def test_a_record_written_by_the_old_generator_reads(self, branch, ready, capsys):
        """S11 (T13): every round record committed in this repository reads
        under the new check — its `Target SHA` and its verdict table, with
        no finding left open — and the newest of them, copied in as the last
        record with its target moved to the fixture's reviewed commit, passes
        the whole check: the fields it no longer judges refuse nothing."""
        root, code_sha = branch
        corpus = sorted(
            (
                p
                for p in (ROOT / "seal" / "specs").glob("*/rounds/round-*.md")
                if re.fullmatch(r"round-\d+\.md", p.name)
            ),
            key=lambda p: (p.parent.parent.name, int(re.findall(r"\d+", p.name)[0])),
        )
        assert corpus, "no round record in the tree to read"
        for path in corpus:
            text = path.read_text(encoding="utf-8")
            assert chain.target_of(reader, text), f"{path}: no Target SHA read"
            found, errors = chain.open_findings(reader, reader.readable(text), "r")
            assert (found, errors) == ([], []), f"{path}: {found} {errors}"
        newest = corpus[-1].read_text(encoding="utf-8")
        assert "| Needs a fix |" in newest
        rel = f"{ITEM}/rounds/round-1.md"
        write(
            root,
            rel,
            re.sub(
                r"^\| Target SHA \|[^\n]*$",
                f"| Target SHA | {code_sha} |",
                newest,
                count=1,
                flags=re.M,
            ),
        )
        commit(root, "the newest record in the tree, copied")
        code, out = check(root, capsys)
        assert code == 0, out

    def test_a_broad_gate_file_naming_another_commit_fails_a_ready_pull_request(
        self, branch, ready, capsys
    ):
        """S5 (T15): the newest run must be HEAD or have only records after
        it; a stale run fails naming the file, and `--sealing` prints it."""
        root, _code = branch
        rel = f"{ITEM}/broad-gate.md"
        write(root, rel, gate_file("1" * 40))
        commit(root, "a run this repository cannot see")
        code, out = check(root, capsys)
        assert code == 1
        assert any(ln.startswith(f"{rel}:") for ln in out.splitlines())
        code, out = check(root, capsys, "--sealing")
        assert code == 0 and rel in out

    def test_a_straight_to_the_pr_item_owes_the_broad_gate_file(
        self, branch, ready, capsys
    ):
        root, _code = branch
        write(
            root,
            f"{ITEM}/routing.md",
            ROUTING.format(review="straight to the PR", planning="the session"),
        )
        git(root, "rm", "-rq", f"{ITEM}/rounds", f"{ITEM}/broad-gate.md")
        commit(root, "direct, and no run")
        code, out = check(root, capsys)
        assert code == 1 and "broad-gate.md" in out
        write(root, f"{ITEM}/broad-gate.md", gate_file(git(root, "rev-parse", "HEAD")))
        commit(root, "the run")
        code, out = check(root, capsys)
        assert code == 0, out

    def test_an_unreadable_declaration_fails_and_none_passes(
        self, branch, ready, capsys
    ):
        root, _code = branch
        write(root, f"{ITEM}/routing.md", "# nothing to read\n")
        commit(root, "garbled")
        code, out = check(root, capsys)
        assert code == 1 and "not a readable declaration" in out
        git(root, "rm", "-rq", ITEM)
        commit(root, "no work item")
        code, out = check(root, capsys)
        assert code == 0 and "declared neither way" in out

    def test_a_baseline_that_does_not_resolve_is_exit_2(self, branch, capsys):
        root, _code = branch
        code = chain.main(["--baseline", "no-such-ref", "--root", str(root)])
        assert code == 2
        assert "does not resolve" in capsys.readouterr().err


# --- retired ------------------------------------------------------------------

OLD_ITEM = "seal/specs/1788000000-an-earlier-item"


def remove_an_earlier_item(root, marker):
    """Declare an earlier work item on `main`, bring it into the branch, and
    remove its directory there, with or without the `docs/` marker a fold
    writes."""
    git(root, "switch", "-q", "main")
    # Close enough to the branch's own declaration for git's rename detection
    # to pair the two, which `changed` reads without.
    write(
        root,
        f"{OLD_ITEM}/routing.md",
        ROUTING.format(review="straight to the PR", planning="the session"),
    )
    # A spec at the merge base keeps the rule arm (`retired_by_rule`) from
    # excusing the removal, so only the marker can.
    write(root, f"{OLD_ITEM}/spec.md", "# a spec\n\nA rule.\n")
    commit(root, "an earlier item, declared")
    git(root, "switch", "-q", "feature/x")
    git(root, "merge", "-q", "--no-edit", "main")
    git(root, "rm", "-rq", OLD_ITEM)
    if marker:
        write(
            root,
            "docs/policy.md",
            "<!-- specs/1788000000-an-earlier-item -->\nA rule.\n",
        )
    commit(root, "the earlier item leaves")


class TestRetired:
    def test_a_declaration_a_fold_retired_is_not_one_this_branch_made(
        self, branch, draft, capsys
    ):
        """A `routing.md` that `settle --retire` removed is a deletion in the
        diff, and the work item it declared was reviewed at its own pull
        request; the `docs/` marker is what tells it from a deletion."""
        root, _code = branch
        remove_an_earlier_item(root, marker=True)
        _code, out = check(root, capsys)
        assert "retired:" in out and "1788000000-an-earlier-item" in out
        assert "does not carry this file at HEAD" not in out

    def test_a_declaration_deleted_with_nothing_absorbing_it_is_refused(
        self, branch, draft, capsys
    ):
        root, _code = branch
        remove_an_earlier_item(root, marker=False)
        _code, out = check(root, capsys)
        assert "does not carry this file at HEAD" in out
        assert "retired:" not in out
