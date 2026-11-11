#!/usr/bin/env python3
"""Close the issues a release's pull requests said they close.

A closing keyword is read by GitHub only for a pull request whose base is the
default branch. Everything here merges into `release/vX.Y.Z` first, so every
keyword a feature pull request writes is inert -- of three merged that way,
none fired. The answer is written down, and without this nothing acts on it.

This runs when `main` moves. It reads the pull request numbers out of the
commit subjects that arrived, fetches each of those pull request bodies, and
closes what their keywords name.

Three things it deliberately does not do.

**It does not parse the release pull request's own body.** That would be the
same manual step one layer up -- somebody assembling a list, and forgetting.
The keywords are already written, one per feature pull request, by the session
that knew which issue it was answering.

**It never reopens and never comments on an unrelated issue.** There are two
writes and no others: the close, and taking `size: now` off the issue being
closed -- the moment `docs/releasing/issues-and-milestones.md` names as
where a spent sizing label comes off.
Both are idempotent. A close of an issue already closed is skipped rather
than repeated, and the removal happens only after a read says the label is
there, so a re-run or a force-push changes nothing.

**The close comes first and the label after it**, because the close is what
this script exists for and the label is bookkeeping about it. An issue that
closed and kept a stale label is a wrong answer on a tracker; an issue left
open because a label write failed is a release that did not finish. So the
removal's failure is reported and the run goes on, which is the one place
this script does not fail loudly and the paragraph below says why it
otherwise does.

**It never ADDS a label.** That is the sibling's act at the squash
(`label_merged_on_release_branch.py`), and a second writer of labels is how
two scripts come to disagree about which is the current answer.

**A `(#N)` that names no pull request is skipped, not fatal.** People write
that form by hand to name the issue a commit fixes, and this repository's
history holds a `(#N)` that names an issue. Everything else still fails
loudly.

**It fails loudly, and it fails at the END.** A closing keyword nobody acted on
is the defect this exists for; a run that swallows its own error would be that
defect wearing a green check. But a run that dies on the first refusal leaves
every issue sorted after it open, with a re-run dying in the same place:
`gh issue close` has been refused on one issue with `GraphQL: Something went
wrong while executing your query`, twice in a row, and the four issues
behind it stayed open while the job went red. So every
issue is attempted, a refusal on the `gh issue close` route falls back to the
REST route (`gh api -X PATCH …/issues/<n> -f state=closed`, then the same
comment through `gh api …/issues/<n>/comments` where the refused route did
not already post it -- `gh issue close --comment` comments before it closes,
so it usually did; that pair closes such an issue by hand), each
fallback is printed so the log says how many took it,
and the run exits non-zero only once every issue has been tried, naming each
one that both routes refused with both errors. A partial close is repaired by
re-running this script with the run's `BEFORE`, `AFTER` and `REPO`: it skips
what is already closed and reaches the rest.

`DRY_RUN=1` prints what it would close and writes nothing. Without it, a
run by hand against a real commit range, made to check the output, closes
real issues. A tool whose only mode has side effects gets run for its output
sooner or later, and the first person to do it is whoever wrote it.
"""

import json
import os
import re
import subprocess
import sys

# `lib/` first on `sys.path`, where `lib/sibling.py` is imported from; it
# loads every other module this script reads.
sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "lib"),
)
import sibling

console = sibling.load("lib/console.py")
gitcmd = sibling.load("lib/gitcmd.py")

# GitHub's own set. Each has to appear immediately before its number -- the
# documentation asks for full syntax for each issue and sanctions no shorter
# form, so `Closes #1, #2` is not read as two here either.
KEYWORDS = (
    "close",
    "closes",
    "closed",
    "fix",
    "fixes",
    "fixed",
    "resolve",
    "resolves",
    "resolved",
)
CLOSING = re.compile(r"\b(?:" + "|".join(KEYWORDS) + r")\s+#(\d+)\b", re.IGNORECASE)
# `feat: … (#100)` -- what a squash merge puts in the subject.
MERGED_PR = re.compile(r"\(#(\d+)\)\s*$")

# GitHub creates no reference from a closing keyword inside a code fence, an
# HTML comment or a code span, and neither does this.
# `docs/releasing/branch-and-release.md` carries `Closes #88` in a fenced
# block as the example to copy, so a pull request body quoting the document
# would otherwise close the issue the document names -- and this
# repository's bodies quote its documents routinely.
#
# The fence and span patterns mask a tilde fence, a fence indented under a
# list item, and a double-backtick span, as well as the plain shapes. The
# direction is chosen rather than incidental --
# masking more closes FEWER issues, and an issue left open is visible on the
# tracker and closed by a re-run, where an issue closed on a quoted example
# is a false record. `issue_claims_check.py` imports `HIDDEN`, so it widens
# with it.
#
# The comment is masked as GitHub reads it, observed through
# `closingIssuesReferences` on the throwaway pull requests #1402 to #1410
# into `main`, each titled for the shape it probes. A comment that
# closes hides its keyword wherever it stands: at a line start, in the middle
# of a line, over several lines and under a list item. Text
# after its `-->` is read, on a line that begins with the `<!--` too. A
# `<!--` that no `-->` follows hides everything below it where it begins a
# line, on its own line and on the lines after it. A `<!--`
# that no `-->` follows, after other text on its line, is text, and a keyword
# on the next line is read. Behind a list marker or a block quote
# marker, a `<!--` that no `-->` follows hides everything below it too, past
# the end of its list item or its quote. Indented four spaces
# it is an indented code block, and a keyword after it is read, so
# the mask there runs past GitHub's, as the Limits below state.
#
# Two shapes stay unmasked, on purpose, and each has a row pinning it in
# `tests/github/test_close_issues_on_release.py#Test_keywords_in`. A four-space
# indented block is an indented code block to CommonMark and is ALSO how this
# repository's pull request bodies continue a bullet onto the next line, so
# masking it would drop real claims -- the wrong direction for a closer. A
# `<!--` that never closes after other text on its line is text to GitHub,
# so masking it would drop a claim GitHub reads.
#
# A fence is three backticks or three tildes, indented or not, closed by the
# same delimiter; `\1` is what keeps a tilde fence from ending at a backtick
# one. A comment is `<!--` to the first `-->` after it, or, where nothing but
# spaces, tabs and block markers stands before it on its line and no `-->`
# follows it anywhere, `<!--` to the end of the text. A span is one backtick
# to the next, or two backticks to the next two, and the double form may hold
# a single backtick inside.
#
# `HIDDEN` reads the three in one pass, and whichever opens first in the text
# wins, so a `<!--` inside a code span opens no comment and a backtick inside
# a comment opens no span. Two passes in either order lose one of those. The
# fence stays the first alternative, so its group stays group 1 for `\1`.
#
# Limits, stated and not guarded. Each but the last masks more than GitHub,
# so the closer closes fewer and the completeness check refuses the release,
# which is loud. The line-start test of `COMMENT`'s second arm reads one
# line's own text, with no block model. So where CommonMark's block rules make
# GitHub read on past an opener the test treats as a line start, such as an
# opener in an indented code block or after a list marker that opens no list
# item, it masks to the end of the text all the same, and the closer closes
# fewer.
# The observed shapes are examples, not a list: GitHub reads on past an
# opener with text before it, hides what follows an opener behind a
# list marker or a quote marker as the closer does, and reads
# on past an opener indented four spaces. Following those rules would
# mean modelling CommonMark's containers, and this repository's bodies write
# a bullet's continuation as an indent. A `<!--` in the middle of a line with
# a `-->` further down is a comment up to that `-->`, across blank lines too,
# where GitHub's inline comment ends with its paragraph. A comment GitHub's
# renderer refuses for its contents, such as one holding `--`, is masked
# anyway. And a fence, a comment or a span is masked to spaces, one in
# `keywords_in` and one per character in `issue_claims_check.py#prose_only`,
# so one standing between a keyword and its number, as in `Closes<!-- -->#4`,
# joins them into a claim GitHub does not read: there the closer closes more.
FENCE = re.compile(r"^[ \t]*(```|~~~).*?^[ \t]*\1", re.M | re.S)
COMMENT = re.compile(
    r"<!--.*?-->|^[ \t]*(?:(?:>|[-*+]|\d{1,9}[.)])[ \t]*)*<!--(?!.*?-->).*\Z",
    re.M | re.S,
)
SPAN = re.compile(r"``(?:[^`\n]|`(?!`))+?``|`[^`\n]*`")
HIDDEN = re.compile(
    "|".join(p.pattern for p in (FENCE, COMMENT, SPAN)),
    re.M | re.S,
)


def keywords_in(body):
    """Closing keywords GitHub itself would read: prose only, with every
    fence, comment and code span `HIDDEN` masks collapsed to one space."""
    return CLOSING.findall(HIDDEN.sub(" ", body))


def run(*args):
    out = subprocess.run(args, capture_output=True, encoding="utf-8")
    if out.returncode:
        sys.exit(f"{' '.join(args)} failed: {out.stderr.strip()}")
    return out.stdout


def attempt(*args):
    """`(ok, stderr)` for a write whose failure is not the run's.

    `run` exits on a non-zero `gh`, which is right for a read the rest of the
    run depends on and wrong for one issue's close: the issues sorted after
    it depend on nothing about it. The close loop reads this instead and
    decides at the end what the failures add up to.
    """
    out = subprocess.run(args, capture_output=True, encoding="utf-8")
    return out.returncode == 0, out.stderr.strip()


def _issue_api(repo, number):
    """(state_json, exists). A 404 here is input, not a failure.

    A number that names nothing reaches this from two directions: a `(#N)` a
    person typed in a commit subject, and a typo in a merged pull request
    body. Neither is a reason to fail a release -- and a run that died halfway
    would leave the issues after it in the sorted order open, with a re-run
    dying in the same place.
    """
    out = subprocess.run(
        ["gh", "api", f"repos/{repo}/issues/{number}"],
        capture_output=True,
        encoding="utf-8",
    )
    if out.returncode:
        if "Not Found" in out.stderr or "404" in out.stderr:
            return None, False
        sys.exit(f"gh api issues/{number} failed: {out.stderr.strip()}")
    return json.loads(out.stdout), True


def issue_state(repo, number):
    """`open`, `closed`, or None when no such issue exists."""
    data, exists = _issue_api(repo, number)
    return data.get("state") if exists else None


def comments_on(repo, number):
    """How many comments `number` carries, or None where the read did not say.

    The same read `issue_state` makes; taken before and after the first
    route so the fallback can tell whether that route's comment landed
    before its close was refused.
    """
    data, exists = _issue_api(repo, number)
    count = data.get("comments") if exists and isinstance(data, dict) else None
    return count if isinstance(count, int) else None


def issue_labels(repo, number):
    """(label names, exists) for an issue, or ([], False) if there is none.

    The one reader, here rather than beside either caller.
    `label_merged_on_release_branch.py` delegates to it, and the loop below
    reads it to know whether a spent
    `size: now` is there to remove. A second copy is what this module's
    neighbours already exist not to have.
    """
    data, exists = _issue_api(repo, number)
    if not exists:
        return [], False
    return [entry.get("name") for entry in data.get("labels") or []], True


# The sizing label, spent the moment the release that carried the ticket
# closes it. `docs/releasing/issues-and-milestones.md` says that is the moment, and
# this line is what acts on it: an answer written down with nothing reading
# it is the same shape as the closing keyword this whole script exists for.
# The name is the document's, and the description of what it
# means lives in `.github/scripts/tracker_labels.py`, which is what creates
# it.
SPENT_ON_CLOSE = "size: now"


def drop_label(repo, number, label):
    """Take `label` off an issue, tolerating a failure.

    **The close is the act; this is not.** An issue that closed and kept a
    stale label is a wrong answer on a tracker. An issue that stayed open
    because a label write failed is a release that did not finish, and
    `close_issues_on_release.py` failing loudly is right about the close and
    would be wrong about this. So the failure is reported and the run goes
    on.
    """
    out = subprocess.run(
        ["gh", "issue", "edit", str(number), "--repo", repo, "--remove-label", label],
        capture_output=True,
        encoding="utf-8",
    )
    if out.returncode:
        print(
            f"could not remove {label!r} from #{number}: "
            f"{out.stderr.strip()} — the issue is closed either way"
        )
        return False
    return True


def spend_label(repo, number, dry):
    """Take the spent sizing label off `number`, and say what happened.

    **Three call sites reach this, and there is one copy.** The loop below
    spends the label on an issue it just closed and on one a previous run
    closed. A copy per site that did not guard its report on the write would
    print `could not remove …` and then `removed …` for the same issue, in
    the job log that is the only record of what the release did to the
    tracker, with the tracker in the state the first line describes and the
    second denies.

    The dry arm is here for the same reason: written at one of the three
    sites and not the others, a preview over an already-closed issue would
    say nothing about the label at all, and `DRY_RUN` exists precisely so a
    person can see the whole act before it happens.

    One copy is what keeps a fourth call site from being written unguarded.
    """
    if dry:
        print(f"would remove {SPENT_ON_CLOSE!r} from #{number}")
        return
    if drop_label(repo, number, SPENT_ON_CLOSE):
        print(f"removed {SPENT_ON_CLOSE!r} from #{number}")


def closing_comment(source):
    """What the closed issue says about why a workflow closed it."""
    return (
        f"Closed by #{source}, which shipped in the release that just "
        f"reached `main`.\n\nIts body carried the keyword; GitHub does not "
        f"read one on a pull request whose base is not the default branch, "
        f"so this workflow acts on it instead. "
        f"`docs/releasing/branch-and-release.md` has the reasoning."
    )


def close_issue(repo, number, comment):
    """Close `number` with `comment`; the errors, empty where it closed.

    Two routes to the same two writes. `gh issue close` is the first, and it
    goes through GraphQL. When that is refused -- GraphQL has refused one
    issue twice in a row, for a reason nobody has found -- the REST route
    takes over: a PATCH of the state, then the comment posted to the issue's
    comments where the refused route did not already post it. That is the
    pair a person types to close such an issue by hand, in that order.

    `gh issue close --comment` posts the comment and THEN sends the close, so
    the route that was refused usually leaves its comment behind, and posting
    it again on every run would leave an issue a run could not close with one
    identical closing comment per refused run. The comment count is read
    before and after the first route, and where it grew by one the sentence
    is already there. Where the read did not say, the comment is posted: a
    duplicate is the smaller wrong answer than a close nobody explained.

    A refused PATCH leaves the issue open and this answers both errors, so
    the caller can name them together. A comment the REST route could not
    post is reported and the close stands: the close is the act, the comment
    is what says why, and an issue closed without its sentence is a smaller
    wrong answer than an issue left open.
    """
    before = comments_on(repo, number)
    ok, first = attempt(
        "gh",
        "issue",
        "close",
        str(number),
        "--repo",
        repo,
        "--comment",
        comment,
    )
    if ok:
        return []
    ok, second = attempt(
        "gh",
        "api",
        "-X",
        "PATCH",
        f"repos/{repo}/issues/{number}",
        "-f",
        "state=closed",
    )
    if not ok:
        return [f"gh issue close: {first}", f"gh api PATCH: {second}"]
    print(
        f"closed #{number} through the REST route after `gh issue close` "
        f"was refused: {first}"
    )
    if before is not None and comments_on(repo, number) == before + 1:
        print(
            f"#{number} already carries the closing comment from the refused "
            f"`gh issue close` — not posting it again"
        )
        return []
    ok, third = attempt(
        "gh",
        "api",
        f"repos/{repo}/issues/{number}/comments",
        "-f",
        f"body={comment}",
    )
    if not ok:
        print(
            f"could not post the closing comment on #{number} through the REST "
            f"route: {third} — the issue is closed either way"
        )
    return []


def pull_request_body(repo, number):
    """The body of pull request `number`, or None if it is not one.

    `(#N)` at the end of a subject is what a squash merge writes, and it is
    ALSO something a person writes by hand to name the issue a commit fixes.
    In this repository, `fix: a Target SHA the squash discarded …
    (#61)` names an issue rather than a pull request, and asking
    `repos/…/pulls/61` for it returns 404. A run that treated that as an error
    would fail the whole release for a number somebody typed in a commit
    message.

    So a 404 here is expected input rather than a failure, and it is told
    apart from a real one: anything other than "not found" still stops the
    run. `/issues/N` answers for both kinds and carries a `pull_request` key
    only for a pull request, so one call settles it.
    """
    data, exists = _issue_api(repo, number)
    if not exists or data.get("pull_request") is None:
        return None
    return data.get("body") or ""


def arrived(before, after):
    """Commit subjects new to `main` in this push.

    `before` is all zeroes for a branch's first push. A force-push is NOT
    that case -- it sends the SHA it displaced, and if the runner's clone
    cannot reach it the range fails and the run stops, which is the right
    direction and not the fallback. The fallback reads the tip alone and says
    so, because it drops every pull request behind it: a release push whose
    four pull requests name three issues collects one.
    """
    if not before or set(before) == {"0"}:
        print(
            "WARNING: no `before` commit — reading only the tip. Any pull "
            "request behind it in this push is not seen."
        )
        # exempt from splitlines: git output
        return run(*gitcmd.argv("log", "-1", "--format=%s", after)).splitlines()
    # exempt from splitlines: git output
    return run(*gitcmd.argv("log", "--format=%s", f"{before}..{after}")).splitlines()


def main():
    before, after = os.environ.get("BEFORE", ""), os.environ["AFTER"]
    repo = os.environ["REPO"]
    dry = os.environ.get("DRY_RUN", "").strip() not in ("", "0", "false", "no")
    if dry:
        print("DRY_RUN — nothing will be written")

    prs = []
    for subject in arrived(before, after):
        found = MERGED_PR.search(subject.strip())
        if found:
            prs.append(int(found.group(1)))
    print(f"pull requests in this push: {prs or 'none'}")

    wanted = {}
    for number in prs:
        body = pull_request_body(repo, number)
        if body is None:
            print(f"#{number} is not a pull request — a hand-written number")
            continue
        for issue in keywords_in(body):
            wanted.setdefault(int(issue), number)
    if not wanted:
        print("no closing keyword in any of them — nothing to close")
        return

    failures = []
    for issue, source in sorted(wanted.items()):
        carried, exists = issue_labels(repo, issue)
        state = issue_state(repo, issue)
        if state is None:
            print(f"#{issue} does not exist (named by #{source}) — skipping")
            continue
        spent = exists and SPENT_ON_CLOSE in carried
        if state == "closed":
            print(f"#{issue} already closed (named by #{source}) — leaving it")
            # A closed issue still carrying it is one closed by hand, or one
            # a previous run closed and whose removal failed. The label is
            # spent either way and the removal is idempotent, so taking it
            # off here costs one call and leaves no stale ones behind.
            if spent:
                spend_label(repo, issue, dry)
            continue
        if dry:
            print(f"would close #{issue}, named by #{source}")
            if spent:
                spend_label(repo, issue, dry)
            continue
        errors = close_issue(repo, issue, closing_comment(source))
        if errors:
            # Reported here and again at the end, and the loop goes on: the
            # issues sorted after this one depend on nothing about it. The
            # label stays, because it is bookkeeping about a close that did
            # not happen.
            print(f"could not close #{issue} (named by #{source}): {'; '.join(errors)}")
            failures.append((issue, source, errors))
            continue
        print(f"closed #{issue}, named by #{source}")
        # After the close, never before it. The close is what this script
        # exists for and the label is bookkeeping about it, so the order is
        # the one where a failing label write cannot cost an issue its close.
        if spent:
            spend_label(repo, issue, dry)

    if failures:
        named = "\n".join(
            f"  #{issue} (named by #{source}): {' — '.join(errors)}"
            for issue, source, errors in failures
        )
        sys.exit(
            f"{len(failures)} issue(s) could not be closed on either route, "
            f"after every issue was attempted:\n{named}\n"
            "Close each by hand, or re-run this script with the run's BEFORE, "
            "AFTER and REPO: it skips what is already closed and reaches the rest."
        )


if __name__ == "__main__":
    console.to_utf8()
    main()
