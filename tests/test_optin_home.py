"""One opt-in signal, read one way: `seal/` at the first of two places.

`hooks/optin.py`'s cases moved to `tests/test_optin.py`, with the version
check's and the review-skill gate's cases that pin how a hook reads the two
places (#942's phase 6). What stays is the commit gate's: how it reads the
two places, the old name and the throwaway marker, and that `seal/` counts as
documents and not code. They wait for the commit gate's group.
"""

import subprocess

from conftest import (
    decision_of,
    fired,
    home,
    legacy,
    load_hook_module,
    payload,
    run_hook,
    scratch,
)

# --- the gates read it -----------------------------------------------------


def test_commit_gate_fires_on_the_new_home(repo):
    home(repo)
    assert fired(run_hook("commit-review-gate.py", payload("git commit -m x", repo)))


def test_commit_gate_stays_silent_on_the_legacy_marker(repo):
    """S3: every gate is silent over `.specseal/`, and the only thing that
    speaks is the migration hook at session start."""
    legacy(repo)
    out = run_hook("commit-review-gate.py", payload("git commit -m x", repo))
    assert decision_of(out) == "silent"


def test_the_home_directory_counts_as_documents_not_code(repo):
    """The parity gate compares code against an original; `seal/` is neither.

    Asking there would train people to click through the prompt, which costs
    more than the check is worth."""
    gate = load_hook_module("commit-review-gate.py", "commit_review_gate")
    (repo / "seal").mkdir()
    (repo / "seal" / "ledger.md").write_text("# ledger\n", encoding="utf-8")
    subprocess.run(
        ["git", "-C", str(repo), "add", "-A"], check=True, capture_output=True
    )
    assert not gate.touches_code(
        str(repo), gate.commit_invocations("git commit -m x")[0]
    )


def test_a_code_change_alongside_it_still_counts(repo):
    gate = load_hook_module("commit-review-gate.py", "commit_review_gate")
    (repo / "seal").mkdir()
    (repo / "seal" / "ledger.md").write_text("# ledger\n", encoding="utf-8")
    (repo / "app.py").write_text("x = 1\n", encoding="utf-8")
    subprocess.run(
        ["git", "-C", str(repo), "add", "-A"], check=True, capture_output=True
    )
    assert gate.touches_code(str(repo), gate.commit_invocations("git commit -m x")[0])


def test_the_commit_gate_is_silent_in_a_scratch_repository(repo):
    home(repo)
    scratch(repo)
    out = run_hook("commit-review-gate.py", payload("git commit -m x", repo))
    assert decision_of(out) == "silent"


def test_the_commit_gate_still_fires_beside_a_scratch_DIRECTORY(repo):
    """The gate-level half of the file-not-directory rule."""
    home(repo)
    (repo / ".git" / "specseal-scratch").mkdir()
    assert fired(run_hook("commit-review-gate.py", payload("git commit -m x", repo)))


def test_a_scratch_repository_gives_no_standing_over_a_target_it_cannot_read(repo):
    """The stop for an unreadable target is the session's own repository
    speaking, so the marker has to reach that too — otherwise the probe that
    prompted issue #68 keeps prompting, one door along."""
    home(repo)
    scratch(repo)
    out = run_hook("commit-review-gate.py", payload('git -C "$WT" commit -m x', repo))
    assert decision_of(out) == "silent"
