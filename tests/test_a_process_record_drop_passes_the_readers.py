"""A range that drops a released work item's process record passes the
pull-request readers (#729, S5 and S7).

`settle --retire-process` removes `rounds/`, `phases/` and the
files written only for a pull request, and leaves `routing.md` and the SDD set
standing. Its first run in a repository is its own pull request into a release
branch, and every check on that pull request reads `seal/specs/`. So each
case builds the drop the command itself makes, commits it on a branch cut from
the base, and runs the reader as CI does:

- `chain_check.py` judges a work item only where the pull request adds or
  edits its `routing.md`, and the drop edits none;
- `unverified_check.py --baseline` counts the `## Not verified` rows of each
  `overview.md`, and the drop removes no overview.

The last case holds the arm's list, member by member.
"""

import importlib.util
import json
import os
import subprocess
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SETTLE = os.path.join(ROOT, "skills", "settle", "scripts", "settle.py")
CHAIN = os.path.join(ROOT, "skills", "code-review", "scripts", "chain_check.py")
UNVERIFIED = os.path.join(ROOT, "skills", "verify", "scripts", "unverified_check.py")


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ITEM = "seal/specs/1700000001-alpha"
BRANCH = "chore/drop-the-process-record"

# Wording that stands in `docs/`, and the process record's paraphrase of it,
# which is the shape of every real one: a round, a phase and a handoff restate
# what the documents say, and a broad-gate record restates what the suite
# printed. A paraphrase and not a copy, because the sweep reports two separate
# stretches of shared wording and stays quiet about one: a sentence removed
# whole and standing verbatim elsewhere shares a single run.
DOC = (
    "The verdict cell is written by the reviewing round itself, so the "
    "orchestrator never edits it afterwards."
)
QUOTE = (
    "The verdict cell is written by the reviewing round itself and the "
    "orchestrator never edits it afterwards."
)
SUITE = (
    "The sealer ran the whole suite once at the tip of the branch, and every "
    "module passed on both legs of the matrix."
)
GATE = (
    "The sealer ran the whole suite once at the tip, where every module "
    "passed on both legs of the matrix."
)
OVERVIEW = (
    "# alpha — overview\n\nWhy.\n\n## Not verified\n\n"
    "| Item | Who must answer |\n|---|---|\n"
    "| closed a claim nobody had run | run on 2026-01-01 |\n"
)
# A file that shares nothing. The sweep weighs a phrase by how few files
# carry it, so a corpus of two files weighs every phrase near zero, and the
# survivor sweep's own cases carry the same filler for the same reason.
FILLER = "# filler\n\nUnrelated prose that shares nothing.\n"


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        check=True,
    )


def write(repo, rel, text):
    path = repo / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def commit(repo, message):
    git(repo, "add", "-A")
    git(
        repo,
        "-c",
        "user.email=e@example.com",
        "-c",
        "user.name=e",
        "commit",
        "-qm",
        message,
    )


def routing():
    return (
        "# 1700000001-alpha — routing\n\n"
        "| Axis | Answer |\n|---|---|\n"
        "| Review | through the review chain |\n"
        "| Destination | open the pull request |\n"
        "| Branch | feat/alpha |\n"
    )


@pytest.fixture
def dropped(tmp_path):
    """A released work item on `base`, and a branch whose one commit is what
    `settle --retire-process` removed from it."""
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init", "-q", "-b", "base")
    write(repo, "docs/a-policy.md", f"# a policy\n\n{DOC}\n\n{SUITE}\n")
    write(repo, "docs/another.md", f"# another\n\n{QUOTE}\n")
    write(repo, "docs/filler.md", FILLER)
    write(repo, f"{ITEM}/routing.md", routing())
    for name in ("spec.md", "plan.md", "questions.md", "changelog.md"):
        write(repo, f"{ITEM}/{name}", f"# alpha {name}\n\nWhat it decided.\n")
    write(repo, f"{ITEM}/overview.md", OVERVIEW)
    write(repo, f"{ITEM}/rounds/round-1.md", f"# round 1\n\n{QUOTE}\n")
    write(repo, f"{ITEM}/rounds/round-1-report.md", f"# report\n\n{QUOTE}\n")
    write(repo, f"{ITEM}/phases/phase-1.md", f"# phase 1\n\n{QUOTE}\n")
    write(repo, f"{ITEM}/handoff.md", f"# handoff\n\n{QUOTE}\n")
    write(repo, f"{ITEM}/broad-gate.md", f"# broad gate\n\n{GATE}\n")
    write(repo, f"{ITEM}/pr.ko.md", "# 본문\n\n바뀐 것을 적습니다.\n")
    commit(repo, "a released work item")
    git(repo, "switch", "-qc", BRANCH)
    r = subprocess.run(
        [
            sys.executable,
            SETTLE,
            "--root",
            str(repo),
            "--released-at",
            "base",
            "--retire-process",
        ],
        capture_output=True,
        encoding="utf-8",
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert not (repo / ITEM / "handoff.md").exists(), r.stdout
    assert (repo / ITEM / "routing.md").is_file(), r.stdout
    commit(repo, "drop the process record")
    return repo


def chain_check(repo):
    env = dict(os.environ)
    event = repo.parent / "event.json"
    event.write_text(json.dumps({"pull_request": {"draft": False}}), "utf-8")
    env["GITHUB_EVENT_PATH"] = str(event)
    env["GITHUB_HEAD_REF"] = BRANCH
    r = subprocess.run(
        [sys.executable, CHAIN, "--baseline", "base", "--root", str(repo)],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        env=env,
        timeout=120,
    )
    return r.returncode, r.stdout + r.stderr


# --- S5: chain_check judges nothing the drop touched -----------------------


def test_the_drop_puts_no_work_item_under_judgment(dropped):
    code, out = chain_check(dropped)
    assert code == 0, out
    assert "1700000001-alpha" not in out, out


def test_a_drop_that_also_removes_routing_is_refused(dropped):
    """The control: the case above would pass for a reader that judges
    nothing at all. A `routing.md` removed from a directory that still holds
    `spec.md` is a declaration deleted, and the same reader refuses it."""
    (dropped / ITEM / "routing.md").unlink()
    commit(dropped, "and the declaration")
    code, out = chain_check(dropped)
    assert code == 1, out
    assert "does not carry this file at HEAD" in out, out


# --- S7: no overview row leaves --------------------------------------------


def test_the_unverified_record_reads_the_same_after_the_drop(dropped):
    r = subprocess.run(
        [sys.executable, UNVERIFIED, "--baseline", "base", "seal/specs/"],
        cwd=str(dropped),
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=120,
    )
    assert r.returncode == 0, r.stdout + r.stderr
    assert "1 overviews" in r.stdout or "1 overview" in r.stdout, r.stdout


# --- the two lists agree ---------------------------------------------------

ENTRIES = (
    ("rounds/round-1.md", True),
    ("rounds/round-1-report.md", True),
    ("phases/phase-1.md", True),
    ("broad-gate.md", True),
    ("handoff.md", True),
    ("pr.ko.md", True),
    ("pr.en.md", True),
    ("tests-todo.md", False),
    ("routing.md", False),
    ("spec.md", False),
    ("plan.md", False),
    ("questions.md", False),
    ("overview.md", False),
    ("changelog.md", False),
    ("notes.md", False),
    ("notes/handoff.md", False),
    ("pr.d/notes.md", False),
)


@pytest.mark.parametrize("rel, process", ENTRIES)
def test_the_arm_names_each_member_of_the_process_record(rel, process):
    """`settle.py#is_process_record` spells the arm's allow-list where it
    removes, and every member and every near miss is held here."""
    settle = load(SETTLE, "settle_for_the_lists")
    first, slash, _ = rel.partition("/")
    arm = settle.is_process_record(first, bool(slash))
    assert arm == process, (rel, "settle", arm)
