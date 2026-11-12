#!/usr/bin/env python3
"""seal pr-wait: wait on a pull request's checks at this checkout's HEAD,
and answer with one exit code per outcome.

  seal pr-wait <N>          wait on pull request N's checks at HEAD
  seal pr-wait <N> --once   read pull request N's state once, wait on nothing

The orchestrator runs `--once` before each push to the pull request's
branch, and the wait when the pull request opens and after each push. It
acts on the exit code; what it does at each one is
`skills/code-review/orchestration.md` *Orchestrator: the pull request opens
once the sealer seals*.

Exit codes:

  0  the deciding read holds only checks that passed or were skipped
  1  the deciding read holds a check that failed or was cancelled; each is
     named by its workflow and its name
  2  the command could not ask, or could not read the answer: no `gh`, a
     `gh` or `git` call that exits non-zero, a value of `state`, `mergeable`
     or `bucket` that `gh` does not name, or an unusable argument
  3  within two minutes of the start, the pull request's head never became
     HEAD, `mergeable` was never known, or no check of a `pull_request` run
     was listed on HEAD; or, after such a check was listed, the head left
     HEAD. The line names the one cause that held, and under a `mergeable`
     never known it says only that, since no check was read
  4  the pull request is merged
  5  the pull request is closed
  6  the pull request is open and conflicts with its base

Under `--once` the command reads the state once and exits 0 for an open
pull request, 4 and 5 as above, and reads nothing else, HEAD included.

What each poll reads, every ten seconds, in this order:

  1. `gh pr view <N> --json state,mergeable,headRefOid,statusCheckRollup`
  2. once the pull request is open, mergeable, its head is HEAD and the
     rollup holds a check, and after the start under a `mergeable` of
     `UNKNOWN` too: `gh pr checks <N> --json name,workflow,event,bucket`
  3. once a check of event `pull_request` is listed and none is pending:
     `gh run list --commit <HEAD> --event pull_request --json
     status,workflowName`, and where every run it lists has completed, an
     empty list among such answers, `gh pr checks` once more, and the
     command decides on that read where nothing in it is pending

Exits 4, 5 and 6 are taken at whichever read first shows them. The
two-minute limit runs from the start until the first check of a
`pull_request` run is listed on HEAD, and no time limit applies after
that: CI's own job timeouts bound the wait, and a job that waits for a
runner can run longer than any limit short enough to help. After the
start, a read whose head is not HEAD ends the wait at exit 3, and a
`mergeable` of `UNKNOWN` reads the checks as `MERGEABLE` does: GitHub
can compute it again while the checks of HEAD run, as when the base
moves, and those checks are still the ones to read. Each `gh` call is bounded at `GH_TIMEOUT`, so a call that hangs ends the
wait at exit 2.

Why each read is there:

- **The head is compared with HEAD.** The command answers for HEAD, and
  `gh pr checks` lists the checks of the pull request's head, so it reads
  them only while the two are one commit. Read right after a push, the
  head can still be the commit before it, whose checks may all have
  finished; how long GitHub takes to move it has not been measured here.
  After the start, another party can push to the branch, GitHub's "Update
  branch" button among them, and from then on no check of HEAD can be
  read, so the wait ends at exit 3 naming both commits.
- **The rollup is counted before the checks are asked for.** With no check
  reported, `gh pr checks` exits 1, with or without `--json`: its
  `no checks reported` is an error raised before any JSON is written
  (`pkg/cmd/pr/checks/checks.go` in `cli/cli`, at v2.92.0), while
  `gh pr view --json statusCheckRollup` exits 0 with an empty list. An exit
  1 is also every other `gh` failure, so this command reads "no check yet"
  from the empty list and takes every non-zero exit as exit 2.
- **The start counts checks of event `pull_request` alone.** A `push` run
  on the pushed commit lists its checks on the pull request too, often
  finished before the pull request opens.
  `.github/workflows/label-merged-on-release-branch.yml` runs on a push to
  `release/*`, so a pull request from a release branch lists its check. A check of another CI service,
  or of another event, counts toward the result and never toward the start,
  so a pull request whose checks all come from elsewhere ends at exit 3.
- **A read with nothing pending is held against the workflow runs.** A job
  that `needs:` another gets its check only when the job it needs ends, so
  between the two every listed check has finished while the run has not.
  `.github/workflows/test.yml` holds such jobs. A run's `status` stays
  short of `completed` until its last job
  ends, and a newer run that cancelled an older one on the same commit is
  not `completed` while the older run's cancelled check is still listed.
- **A cancelled check is not a pass.** `gh` puts `CANCELLED` in the
  `cancel` bucket, which is neither failed nor pending, so
  `gh pr checks --watch` exits 0 on a pull request whose only bad check was
  cancelled (`pkg/cmd/pr/checks/aggregate.go` in `cli/cli`, at v2.92.0).
  So this command reads `gh`'s JSON and decides by itself, and never runs
  `--watch`, which also ends in the gap above.
- **Every bad check is named at once.** The command waits until nothing is
  pending rather than stopping at the first failure, so a second check that
  fails on its own shows before the repair, not after the next push.

`bucket` is `gh`'s own reading of a check's state, so this command keeps no
table of states. A `gh` release that renames a field or a bucket ends at
exit 2 naming the value, or at exit 3, and never at a pass.

Every exit prints one line on stdout that opens `seal pr-wait:` and names
the pull request, the commit where one was read, and the outcome; exits 1
and 2 add indented lines below it. An unusable argument is argparse's
usage error on stderr, at exit 2.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(HERE, "..", "..", "..", "lib")

# `lib/sibling.py` loads every other module this command reads. Where it is
# absent, the refusal is its own sentence about itself, spelt here because
# the file that holds the sentence is the one missing.
sys.path.insert(0, LIB)
try:
    import sibling
except ImportError:
    sys.stderr.write(
        "cannot read "
        + os.path.normpath(os.path.join(LIB, "sibling.py"))
        + ", which this command loads. It ships in the plugin beside this "
        "script; a copy of one script taken on its own is not a plugin. "
        "Nothing was read.\n"
    )
    raise SystemExit(2) from None

console = sibling.load("lib/console.py")
gitcmd = sibling.load("lib/gitcmd.py")

PASSED, FAILED, UNANSWERED, NO_CHECK, MERGED, CLOSED, CONFLICTING = range(7)

INTERVAL = 10  # seconds between two polls, as `gh pr checks --watch` waits
LIMIT = 120  # seconds from the start for a `pull_request` check to be listed
GH_TIMEOUT = 60  # seconds one `gh` call may take before it is a failure

VIEW = ("state", "mergeable", "headRefOid", "statusCheckRollup")
CHECKS = ("name", "workflow", "event", "bucket")
RUNS = ("status", "workflowName")

STATES = {"OPEN": None, "MERGED": (MERGED, "merged"), "CLOSED": (CLOSED, "closed")}
MERGEABLE = ("MERGEABLE", "CONFLICTING", "UNKNOWN")
# `gh`'s five buckets, in the order its help gives them; how a bad one is
# named in the outcome.
BUCKETS = ("pass", "skipping", "fail", "cancel", "pending")
BAD = {"fail": "failed", "cancel": "cancelled"}

# What the module waits with; the cases replace both.
clock = time.monotonic
sleep = time.sleep


class Unanswered(Exception):
    """Exit 2: WHAT the command could not ask or read, and what the tool
    SAID on stderr."""

    def __init__(self, what, said=""):
        super().__init__(what)
        self.what, self.said = what, said

    def lines(self):
        """The outcome, then each line the tool said, indented."""
        said = self.said.strip()
        return [self.what] + (
            ["  " + line for line in said.split("\n")] if said else []
        )


def gh(*args):
    """`gh <args>`'s stdout, or `Unanswered` naming the call and its stderr."""
    shown = "`gh " + " ".join(args) + "`"
    found = shutil.which("gh")
    if found is None:
        raise Unanswered("could not ask: no `gh` on PATH")
    try:
        done = subprocess.run(
            [found, *args],
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=GH_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        raise Unanswered(
            f"could not ask: {shown} did not answer within {GH_TIMEOUT} seconds"
        ) from None
    except OSError as exc:
        raise Unanswered(f"could not ask: {shown} did not run ({exc})") from None
    if done.returncode:
        raise Unanswered(
            f"could not ask: {shown} exited {done.returncode}", done.stderr
        )
    return done.stdout


def head():
    """The commit this checkout's HEAD names, the one the orchestrator
    pushed last, or `Unanswered`."""
    try:
        done = subprocess.run(
            gitcmd.argv("rev-parse", "HEAD"),
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )
    except OSError as exc:
        raise Unanswered(
            f"could not ask: `git rev-parse HEAD` did not run ({exc})"
        ) from None
    if done.returncode:
        raise Unanswered(
            f"could not ask: `git rev-parse HEAD` exited {done.returncode}", done.stderr
        )
    return done.stdout.strip()


def _answer(kind, *args):
    """`gh <args>`'s stdout read as JSON of KIND, `dict` or `list`."""
    out = gh(*args)
    try:
        answer = json.loads(out)
    except ValueError:
        answer = None
    if not isinstance(answer, kind):
        shown = "`gh " + " ".join(args) + "`"
        raise Unanswered(
            f"could not read the answer: {shown} printed no JSON {kind.__name__}"
        )
    return answer


def _named(entry):
    """A check as its workflow and its name, the name alone where no
    workflow ran it."""
    name, workflow = entry.get("name") or "", entry.get("workflow") or ""
    return f"{workflow} / {name}" if workflow else name


def _view(number):
    """The pull request's state, mergeable, head and rollup, each a value
    `gh` names."""
    answer = _answer(dict, "pr", "view", str(number), "--json", ",".join(VIEW))
    state, mergeable = answer.get("state"), answer.get("mergeable")
    if state not in STATES:
        raise Unanswered(
            f"could not read the answer: `gh pr view` answered state {state!r}, "
            f"which is none of {', '.join(STATES)}"
        )
    if mergeable not in MERGEABLE:
        raise Unanswered(
            f"could not read the answer: `gh pr view` answered mergeable "
            f"{mergeable!r}, which is none of {', '.join(MERGEABLE)}"
        )
    if not isinstance(answer.get("headRefOid"), str) or not isinstance(
        answer.get("statusCheckRollup"), list
    ):
        raise Unanswered(
            "could not read the answer: `gh pr view` answered no headRefOid "
            "string or no statusCheckRollup list"
        )
    return answer


def _checks(number):
    """Every check `gh pr checks` lists, each with a bucket `gh` names."""
    listed = _answer(list, "pr", "checks", str(number), "--json", ",".join(CHECKS))
    for entry in listed:
        if not isinstance(entry, dict) or entry.get("bucket") not in BUCKETS:
            bucket = entry.get("bucket") if isinstance(entry, dict) else None
            named = _named(entry) if isinstance(entry, dict) else repr(entry)
            raise Unanswered(
                f"could not read the answer: `gh pr checks` answered bucket "
                f"{bucket!r} for {named}, which is none of {', '.join(BUCKETS)}"
            )
    return listed


def _completed(sha):
    """Whether every `pull_request` run on SHA has completed."""
    runs = _answer(
        list,
        "run",
        "list",
        "--commit",
        sha,
        "--event",
        "pull_request",
        "--json",
        ",".join(RUNS),
    )
    return all(isinstance(r, dict) and r.get("status") == "completed" for r in runs)


def _started(listed):
    """Whether LISTED holds a check of a `pull_request` run."""
    return any(entry.get("event") == "pull_request" for entry in listed)


def _settled(listed):
    """Whether LISTED holds a `pull_request` check and nothing pending."""
    return _started(listed) and not any(e["bucket"] == "pending" for e in listed)


def decide(listed):
    """(exit, lines) for a read with nothing pending: 0 where every check
    passed or was skipped, 1 naming each that failed or was cancelled."""
    bad = [entry for entry in listed if entry["bucket"] in BAD]
    if not bad:
        return PASSED, ["every check passed or was skipped"]
    return FAILED, ["a check failed or was cancelled"] + [
        f"  {BAD[entry['bucket']]}: {_named(entry)}" for entry in bad
    ]


def wait(number, sha):
    """(exit, lines) once pull request NUMBER's checks at SHA are decided,
    or it is merged, closed or conflicting, or no `pull_request` check was
    listed on SHA within `LIMIT`, or its head left SHA after one was. A
    call that fails raises `Unanswered`."""
    start, started = clock(), False
    while True:
        pr = _view(number)
        if STATES[pr["state"]]:
            code, outcome = STATES[pr["state"]]
            return code, [outcome]
        if pr["mergeable"] == "CONFLICTING":
            return CONFLICTING, ["conflicts with its base"]
        moved = pr["headRefOid"] != sha
        if moved and started:
            return NO_CHECK, [
                f"the pull request's head moved from {sha} to {pr['headRefOid']} "
                f"after its checks started, so no check of {sha} can be read any more"
            ]
        unknown = pr["mergeable"] == "UNKNOWN" and not started
        if not unknown and not moved and pr["statusCheckRollup"]:
            listed = _checks(number)
            started = started or _started(listed)
            if _settled(listed) and _completed(sha):
                final = _checks(number)
                if _settled(final):
                    return decide(final)
        if not started and clock() - start >= LIMIT:
            if unknown:
                return NO_CHECK, [
                    f"GitHub never said within {LIMIT} seconds whether the pull "
                    "request is mergeable"
                ]
            why = f", and the pull request's head stayed {pr['headRefOid']}"
            return NO_CHECK, [
                f"no check of a pull_request run was listed on {sha} within "
                f"{LIMIT} seconds{why if moved else ''}"
            ]
        sleep(INTERVAL)


def once(number):
    """(exit, the pull request's head, lines) from one read of its state."""
    pr = _view(number)
    if STATES[pr["state"]]:
        code, outcome = STATES[pr["state"]]
        return code, pr["headRefOid"], [outcome]
    return PASSED, pr["headRefOid"], ["open"]


def _number(text):
    """A pull request number: a whole number above 0."""
    if not text.isdigit() or int(text) < 1:
        raise argparse.ArgumentTypeError(f"{text!r} is not a pull request number")
    return int(text)


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="seal pr-wait",
        description="Wait on a pull request's checks at HEAD, and answer with "
        "one exit code per outcome: 0 passed, 1 failed or cancelled, 2 could "
        "not ask, 3 no check within two minutes, 4 merged, 5 closed, "
        "6 conflicting.",
    )
    parser.add_argument("number", type=_number, help="the pull request's number")
    parser.add_argument(
        "--once",
        action="store_true",
        help="read the state once: 0 open, 4 merged, 5 closed",
    )
    args = parser.parse_args(argv)
    sha = None
    try:
        if args.once:
            code, sha, lines = once(args.number)
        else:
            sha = head()
            code, lines = wait(args.number, sha)
    except Unanswered as exc:
        code, lines = UNANSWERED, exc.lines()
    at = f" at {sha}" if sha else ""
    print(f"seal pr-wait: pull request #{args.number}{at}: {lines[0]}")
    for line in lines[1:]:
        print(line)
    return code


if __name__ == "__main__":
    console.to_utf8()
    sys.exit(main())
