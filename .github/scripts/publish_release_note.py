#!/usr/bin/env python3
"""Publish the GitHub Release for the tag that was just pushed.

A release note left to a person is a habit and nothing else: a checklist
that walks to the tag and stops leaves it to nobody, and **three consecutive
releases shipped without one**. The note is read:
`/agentic:update` reads the GitHub Releases (`skills/update/SKILL.md` step 3),
so a release without one is one an updating user is told nothing about.

So this reads the tag instead of asking anybody to remember. It runs in the
publish workflow after `tag_release.py`, which on the push to `main` that
ships a release creates the release's `vX.Y.Z` tag and passes it on, and on
a `v*` tag pushed by hand passes that tag on.

**The body is built from the release's changelog fragments, read from the
history at the tag.** A change writes its note once, in
`agentory/threads/<work-item-id>/changelog.md`, and no copy of the notes is kept
in the tree. The fragments are the ones the commits after the previous
`vX.Y.Z` tag added and that tag does not already hold, each read at the
newest commit of that range whose tree holds it, so a work item a settle
removed before the tag still has its entry.
Each opens with a link to the pull request that added it. The range's
commit that adds a fragment is its pull request's squash commit, whose
subject GitHub ends with `(#N)`, so the number is read here, once, from the
history. The pull request's body holds the work item's records (`agentic
pr-body`), so one click leads from an entry to the reasons behind it. A
fragment whose adding commit names no pull request is its text alone.

**A range of settles alone carries the release pull request's body where
the fragments stand.** A settle opens no work item, so it writes no
fragment (`skills/settle/SKILL.md` *A settle is not a work item*). Where the
range added no fragment and every commit in it other than a merge removes
whole a work item directory that stood at its parent, which
`chain_check.py#settled` reads as `docs/checks/the-fold.md` *The fold, and
what tells it from a deletion* states, the note's changes are the body of
the pull request merged from `release/vX.Y.Z` into `main` whose merge
commit is the tagged commit. The header, the theme, the folds, the thanks
and the update section are any note's, so the mark finds its header.

**The note opens with a header of the release's counts**, one HTML
paragraph on one line holding, parted by `<br>`, the pull requests merged,
the issues they closed, and the outside contributors where there are any.
**The release's theme follows it**, the first sentence of the description
of the milestone `release: X.Y.Z`, its `Purpose:` label left out.

The fragments are also a page of reasoning per change, and a note that is
only that reads as a wall of prose to somebody asking what changed. So
the note says what the pull requests merged into `release/vX.Y.Z` already
say -- the counts in its header, then one fold per conventional-commit type
under its name and count holding one line per pull request with the issues
its body closes, a credit for every outside contributor, how to
update -- and keeps the fragments beneath, folded. Nothing here composes
prose: every line is a milestone's sentence, a pull request title, a
number, a handle or a fragment.

**The title comes from the tagged commit's message**, which carries the
`release: X.Y.Z symptoms: <symptoms>` line `docs/releasing/release-checklist.md`
*The release pull request* prescribes. The other sources do not hold it:
the merge commit's *subject* is GitHub's `Merge pull request #N from
<owner>/...` line and not the title at all, and the twenty-three
hand-written release names reproduce no pull request title, so nothing can
reproduce them. That step's line is the only written-down source, and so
the only one anything can read.

Three things it deliberately does not do.

**It never republishes.** A release already at the tag is left exactly as it
is -- printed and exited 0 -- so a re-pushed tag and a re-run job change
nothing. The note may have been edited by hand after it was published, and
overwriting that is the one way this could destroy something a person wrote.

**It does not fail a release for a missing title line or theme.** No check
holds the commit subject or the milestone's description, so a missing title
line falls back to the tag name, and a milestone that cannot be listed, is
not found or has an empty description leaves the note without a theme line.
Either way the job log says which branch it took. A wrong title or a missing
theme is visible on the releases page and fixable in one edit; a failed job
at the tag is a release that stops after `main` has already moved.

**It does fail for a range that added no fragment the previous tag does not
already hold and carries more than settles**, which is the opposite
direction on purpose. That is the release shipping unexplained, and the
fragments are the whole of what this publishes. A range that holds no commit
but merges carries no settle. The job log names each commit of the range
that is no settle, by its short hash and subject. **It fails a range of
settles alone whose release pull request cannot be listed, is not found, or
has an empty body**, because that body is the whole of such a note.

**Outside contributors are thanked by handle.** An outside contribution
carries no work item and so no changelog fragment, so a release that carried
one credited it only when somebody remembered to write a sentence about it.
The set is read instead: the pull requests' authors, less the repository
owner and any bot. A release with none gets no credit line and no count.

**The summary adds no way to fail.** A `gh` call that cannot list the pull
requests publishes the theme line and the fragments alone, and says so in
the job log -- a plain note is fixable in one edit, and a failed job at the
tag is not.

**It says whether it created the release.** `created=true` or
`created=false` goes to `$GITHUB_OUTPUT` where the workflow sets it, and the
`mark` job in the same workflow runs only on `true`: the mark edits the note,
so it is held to the line above and never touches a release this run did
not write. The header is built by `header`, and the mark's replacement for
it by `marked_header`, with the mark's image or without it, so every
shape lives in the file that owns the counts and the mark finds the header
by the function that wrote it.

`DRY_RUN=1` prints the note it would create and writes nothing, for the reason
`close_issues_on_release.py`'s docstring gives: a tool whose only mode has
side effects gets run for its output sooner or later, and the first person to
do it is whoever wrote it.

Environment: `TAG` (the tag `tag_release.py` passed on), `REPO`,
`GH_TOKEN`, and `GITHUB_OUTPUT` where the workflow runner sets it.

Exit codes: 0 published, or already published, or a dry run -- 1 the tag is
not `vX.Y.Z`, or its range added no fragment the previous tag does not
already hold and carries more than settles, or its range carries settles
alone and the release pull request's body cannot be read or is empty, or a
git or `gh` command the note cannot go without exited non-zero or gave no
answer, said in `lib/gitcmd.py#Failed`'s one line.
"""

import html
import json
import os
import re
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
# `lib/` first on `sys.path`, where `lib/sibling.py` is imported from; it
# loads every other module this script reads.
sys.path.insert(0, os.path.join(HERE, "..", "..", "lib"))
import sibling  # noqa: E402

console = sibling.load("lib/console.py")
gitcmd = sibling.load("lib/gitcmd.py")
optin = sibling.load("lib/optin.py")
gfm_lines = sibling.load("lib/blocks.py").gfm_lines
closing = sibling.load("lib/closing.py")
SPAN, keywords_in = closing.SPAN, closing.keywords_in
heading_level = sibling.load("lib/lines.py").heading_level

# `agentic settle`, for `adding_commit`: the one reader of the commit that adds
# a fragment and the pull request it names, kept in the settle so that the
# note and the settle read one number.
SETTLE = "skills/settle/scripts/settle.py"
settle = sibling.load(SETTLE)

# `chain-check`, for `settled`: the one predicate that reads a settle, which
# `docs/checks/the-fold.md` *The fold, and what tells it from a deletion*
# names, asked here of each commit of a range that added no fragment.
CHAIN_CHECK = "skills/code-review/scripts/chain_check.py"
chain_check = sibling.load(CHAIN_CHECK)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def fragment_re():
    """A work item's changelog fragment, its id captured, under the root's
    name, `lib/optin.py#HOME`."""
    return re.compile(
        rf"^{re.escape(optin.HOME)}/{re.escape(optin.WORK_ITEMS)}/([^/]+)/changelog\.md$"
    )


# The shape of a fragment's process section, which the note lifts into one
# table (`section`).
PROCESS_TEMPLATE = os.path.join(ROOT, "templates", "records", "process.md")
# The milestone a release's theme is read from, by its title.
MILESTONE_TITLE = "release: {version}"
PURPOSE_LABEL = "Purpose:"

# `vX.Y.Z`. Anything else under `v*` -- `v1.2`, `vnext`, a typo -- is a shape
# this cannot name a version for, and it says so rather than guessing one.
# `label_merged_on_release_branch.py#version_of` refuses a branch name the
# same way and for the same reason. It is `settle.py#VERSION_RE`, so the
# note is published at the version whose note `agentic settle --apply` reads.
TAG_RE = settle.VERSION_RE


# The title line `docs/releasing/release-checklist.md` *The release pull request*
# prescribes for the release
# pull request, which is what the merge commit's body carries: a whole line,
# one space after each colon and after the version, read exactly so.
#
# **The symptoms are required, not optional.** `release: 0.12.3` with nothing
# after it stands in this repository's own history, and reading a title
# out of it yields the version alone -- which is the tag name with the `v`
# removed, so the two branches would differ by one character and the log line
# saying which was taken would be telling a reader nothing. A line with no
# symptoms is not the prescribed line, so it takes the fallback and says so.
TITLE_LABEL = "release:"
SYMPTOMS_LABEL = "symptoms:"


def title_line_re(version):
    return re.compile(
        rf"^{TITLE_LABEL} {re.escape(version)} {SYMPTOMS_LABEL} (\S.*)$", re.M
    )


def version_of(tag):
    """`X.Y.Z` for a `vX.Y.Z` tag, or None for any other name."""
    found = TAG_RE.match((tag or "").strip())
    return found.group(1) if found else None


def git(*args):
    """`git` run in the repository at `ROOT` through `lib/gitcmd.py#git`;
    its standard output. A non-zero exit, or a git that gave no answer,
    ends the run with the runner's one line."""
    return gitcmd.git(ROOT, *args, check=True).stdout


def previous_tag(tag):
    """The highest `vX.Y.Z` tag merged into `tag`'s first parent, or None.

    The first parent is the release's own line: a tag the tagged merge brings
    in through its second parent was not released before this one. The
    highest is taken by number, so `v0.10.0` is above `v0.9.0`.
    """
    found = []
    for name in git("tag", "--merged", f"{tag}^", "--list", "v*").split():
        version = version_of(name)
        if version:
            found.append((tuple(int(n) for n in version.split(".")), name))
    return max(found)[1] if found else None


def commit_range(previous, tag):
    """The commits the release added: after `previous` up to `tag`, or every
    commit reachable from `tag` where there is no previous version tag."""
    return f"{previous}..{tag}" if previous else tag


def fragments(revisions):
    """`[(work item id, body, pull request number or None)]` for every
    changelog fragment a commit in `revisions` added, in id order, an empty
    body skipped. The paths are sorted, and each holds its id, so the paths'
    order is the ids'. The number is the one the oldest commit of the range
    that adds the fragment names (`settle.py#adding_commit`).

    Each is read at the newest commit of the range whose tree holds it, so a
    fragment a settle removed before the tag is read as it stood last.
    `--no-renames` keeps a fragment from reading as a rename of an older one
    the settle deleted in the same range. The per-path log walks every
    parent, `--full-history`, because the tag is a merge into `main` whose
    first parent never held a fragment the settle removed on the release
    branch. A fragment the range's lower tag already holds was
    released there and is skipped, though a commit in the range restored its
    directory. The added paths are read with `-z`, which ends each
    with a NUL and quotes none, whatever `core.quotePath` says, so a
    fragment whose id is not ASCII is read as it is.
    """
    added = git(
        "log",
        "-z",
        "--no-renames",
        "--diff-filter=A",
        "--name-only",
        "--format=",
        revisions,
    )
    out = []
    # The range's lower end, where there is one: a fragment that tag already
    # holds was released there, and a commit that restores its directory
    # adds nothing new.
    previous = revisions.split("..")[0] if ".." in revisions else None
    fragment = fragment_re()
    for path in sorted(set(added.split("\0"))):
        found = fragment.match(path)
        if not found:
            continue
        if previous and git("ls-tree", "--name-only", previous, "--", path).strip():
            continue
        # `--full-history`: the tag is a merge into `main`, whose first parent
        # never held the path. Where a settle removed the fragment on the
        # release branch, the default simplification follows that first
        # parent alone and finds no commit.
        for commit in git(
            "log", "--full-history", "--format=%H", revisions, "--", path
        ).split():
            if git("ls-tree", "--name-only", commit, "--", path).strip():
                body = git("show", f"{commit}:{path}").strip()
                if body:
                    out.append((found.group(1), body, pull_request(revisions, path)))
                break
    return out


def settles(revisions):
    """`(whether revisions hold a commit other than a merge, [(short hash,
    subject)] of each such commit that is no settle)`, oldest first.

    A commit is a settle where `chain_check.py#settled`, asked at the
    commit's parent, keeps at least one of the work item directories, the
    directories directly under `lib/optin.py#HOME`'s `WORK_ITEMS`, from
    which the commit deletes a path and in which its tree holds none. The
    range carries settles alone where it holds a commit other than a merge
    and the list is empty. A merge is passed over: the release's own merge
    into `main` is one. Each read here stops the run where git refuses, as
    `git` does. A git that fails inside `settled` returns no path there, so
    that commit reads as no settle and the release goes to the refusal.
    """
    held, unsettled = False, []
    directory = re.compile(
        rf"^({re.escape(optin.HOME)}/{re.escape(optin.WORK_ITEMS)}/[^/]+)/"
    )
    log = git("log", "--no-merges", "--reverse", "--format=%H %h %s", revisions)
    # exempt from splitlines: git's log, one commit to a line
    for line in log.splitlines():
        # The format's two spaces part three fields, an empty subject too.
        commit, short, subject = line.split(" ", 2)
        held = True
        deleted = git(
            "diff-tree",
            "--no-commit-id",
            "-r",
            "-z",
            "--no-renames",
            "--diff-filter=D",
            "--name-only",
            commit,
        )
        candidates = {
            found.group(1)
            for found in map(directory.match, deleted.split("\0"))
            if found
        }
        gone = {
            d
            for d in candidates
            if not git("ls-tree", "--name-only", commit, "--", d).strip()
        }
        if not chain_check.settled(ROOT, f"{commit}^", gone):
            unsettled.append((short, subject))
    return held, unsettled


def release_pull_body(repo, version, tag):
    """`(the body of the release pull request, where it came from)`, or
    `(None, why not)`.

    The release pull request is the one merged from `release/v<version>`
    into `main` whose merge commit is the commit `tag` names. `gh` that
    fails or gave no answer, a list that is not JSON, no such pull request
    and an empty body are each a sentence, and the caller fails the run on
    it: a note of settles alone has no other text, so this read is one the
    note cannot go without, unlike `merged_pulls`.
    """
    try:
        out = gitcmd.gh(
            "pr",
            "list",
            "--repo",
            repo,
            "--base",
            "main",
            "--head",
            f"release/v{version}",
            "--state",
            "merged",
            "--json",
            "number,body,mergeCommit",
        )
    except gitcmd.Unrun as unrun:
        return None, f"the release pull request could not be listed: {unrun.line}"
    if out.returncode:
        return (
            None,
            f"the release pull request could not be listed: {out.stderr.strip()}",
        )
    try:
        listed = json.loads(out.stdout)
    except ValueError:
        return (
            None,
            "gh pr list printed something that is not JSON, so the release pull "
            "request could not be read",
        )
    commit = git("rev-parse", f"{tag}^{{commit}}").strip()
    for entry in listed:
        if (entry.get("mergeCommit") or {}).get("oid") == commit:
            number, body = entry.get("number"), (entry.get("body") or "").strip()
            if not body:
                return None, f"the release pull request #{number} has an empty body"
            return body, f"the body of the release pull request #{number}"
    return (
        None,
        f"no pull request merged from release/v{version} into main has {tag}'s "
        "commit as its merge commit",
    )


def pull_request(revisions, path):
    """The pull request number the commit of `revisions` that adds `path`
    names, or None. A `git` that fails stops the run, as `git` does."""
    try:
        return settle.adding_commit(ROOT, revisions, path)[1]
    except RuntimeError as problem:
        sys.exit(str(problem))


def process_shape():
    """`(heading, header row, delimiter row)` of a fragment's process
    section, read from `templates/records/process.md`, the section's one
    source: its first line, and its first two table rows."""
    with open(PROCESS_TEMPLATE, encoding="utf-8") as handle:
        lines = gfm_lines(handle.read())
    rows = [line for line in lines if line.startswith("|")]
    return lines[0], rows[0], rows[1]


# An entry's first line: the pull request that added its fragment. It is
# `settle.py#PULL_LINK`, whose `BUILT_RE` tells `agentic settle --apply` that a
# note was built from the fragments.
PULL_LINK = settle.PULL_LINK


def split_process(body, heading):
    """`(body without its process section, the section's rows)`.

    The section is the line `heading` and every line after it up to the next
    heading (`lib/lines.py#heading_level`) or the body's end. Its rows
    are its table lines after the header and delimiter rows.
    """
    kept, table, inside = [], [], False
    for line in gfm_lines(body):
        if line.strip() == heading:
            inside = True
        elif inside and heading_level(line) is not None:
            inside = False
            kept.append(line)
        elif inside:
            if line.startswith("|"):
                table.append(line)
        else:
            kept.append(line)
    return "\n".join(kept).strip(), table[2:]


def section(entries, repo):
    """The fragments as the note carries them: each entry's link to the pull
    request that added it, in `repo`, its body, and a blank line before the
    next. An entry with no number has no link line, and one with neither a
    link nor a body left is not written.

    Every row of every fragment's process section is lifted into one
    `### Process changes` table above them, in id order and each fragment's
    own row order, and each fragment follows without its section, so a row
    is shown once. With no row anywhere the fragments are all there
    is.
    """
    heading, header, delimiter = process_shape()
    rows, parts = [], []
    for _, body, number in entries:
        rest, found = split_process(body, heading)
        rows += found
        lines = [] if number is None else [PULL_LINK.format(repo=repo, number=number)]
        if rest:
            lines.append(rest)
        if lines:
            parts.append("\n".join(lines))
    fragments = "\n\n".join(parts)
    if not rows:
        return fragments
    return "\n".join([heading, "", header, delimiter, *rows, "", fragments])


def milestone_description(repo, version):
    """`(the description of the milestone `release: <version>`, why not)`.

    The first element is "" where there is no description to read: the list
    could not be read, no milestone carries the title, or its description is
    empty. The second element says which, for the job log. `--paginate`
    merges the pages into one list, as `release_completeness_check.py`'s
    `milestone_titles` states. A `gh` that gave no answer is a list that
    could not be read, said in the runner's line.
    """
    try:
        out = gitcmd.gh(
            "api", "--paginate", f"repos/{repo}/milestones?state=all&per_page=100"
        )
    except gitcmd.Unrun as unrun:
        return "", f"the milestones could not be listed: {unrun.line}"
    title = MILESTONE_TITLE.format(version=version)
    try:
        listed = json.loads(out.stdout) if not out.returncode else None
    except ValueError:
        listed = None
    if listed is None:
        return "", f"the milestones could not be listed: {out.stderr.strip()}"
    for entry in listed:
        if entry.get("title") == title:
            text = (entry.get("description") or "").strip()
            if not text:
                return "", f"the milestone `{title}` has no description"
            return text, f"the milestone `{title}`"
    return "", f"no milestone is titled `{title}`"


def theme_of(description):
    """The release's theme line from a milestone's description.

    A leading `Purpose:` is left out. The sentence runs to the first `.`
    followed by whitespace or the end of the text, or to the first line end
    where that comes first, so a version such as `0.18.0` inside it does not
    end it. Its whitespace is collapsed and its first letter upper-cased.
    """
    text = description.strip()
    if text.startswith(PURPOSE_LABEL):
        text = text[len(PURPOSE_LABEL) :].lstrip()
    line = gfm_lines(text)[0] if text else ""
    stop = re.search(r"\.(?=\s|$)", line)
    sentence = " ".join((line[: stop.end()] if stop else line).split())
    return sentence[:1].upper() + sentence[1:]


def title_from(message, version, tag):
    """`(the release title, where it came from)`.

    The second element is what the job log prints. A title a reader cannot
    trace to a source is one nobody can correct at the right end.
    """
    found = title_line_re(version).search(message or "")
    if found:
        return (
            f"{version} — {found.group(1).strip()}",
            f"the tagged commit's `{TITLE_LABEL}` line",
        )
    # The search's own line rule: `re.M` ends a line at "\n" alone, so the
    # line quoted is a line `title_line_re` judged. Any case, any indent.
    seen = re.search(rf"(?im)^[ \t]*{re.escape(TITLE_LABEL)}.*$", message or "")
    first = seen.group(0).strip() if seen else None
    said = f"its first is `{first}`" if first else f"it carries no `{TITLE_LABEL}` line"
    expected = f"`{TITLE_LABEL} {version} {SYMPTOMS_LABEL} <the symptoms>`"
    return (
        tag,
        f"the tag name — the tagged commit's title line is {expected}, and {said}",
    )


def commit_message(tag):
    """The message of the commit `tag` names.

    `%B` is the raw body, so the `release:` line reaches this whether it sits
    in the subject or below it. In this repository it is below: the tagged
    commit is the release merge, whose subject GitHub writes as
    `Merge pull request #N from <owner>/release/vX.Y.Z`.
    """
    return git("log", "-1", "--format=%B", tag)


def release_exists(repo, tag):
    """Whether a GitHub Release already sits at `tag`.

    The HTTP status `gh api -i` printed decides, read by
    `lib/gitcmd.py#http_answer`, and the words of gh's stderr decide
    nothing. A 404 is the answer rather than a failure -- the usual case is
    that no release exists yet, which is the whole reason this job runs. A
    2xx status is a release. Any other status, and an answer with no status
    line, still stops the run with gh's stderr, because a token without the
    scope to read releases would otherwise be read as "none exists" and
    publish a second; a `gh` that gave no answer stops it in the runner's
    line.
    """
    out = gitcmd.gh("api", "-i", f"repos/{repo}/releases/tags/{tag}")
    status, _ = gitcmd.http_answer(out.stdout)
    if status == 404:
        return False
    if status is None or not 200 <= status < 300:
        sys.exit(f"gh api releases/tags/{tag} failed: {out.stderr.strip()}")
    return True


THANKS_HEADING = "### 🙌 Thanks to"
FULL_SUMMARY = "📋 Full changelog — what each change does and why"
UPDATE_HEADING = "### ⬆️ Update"

# A pull request title's conventional-commit type, and the name of the fold
# its line goes in. The order here is the order the note reads in: what a user can
# now do, then what stopped going wrong, then what only a contributor sees.
# A type not listed -- or a title with no type at all -- goes under Other
# rather than being dropped, so the list stays a partition of the release.
TYPES = (
    ("feat", "✨ Features"),
    ("fix", "🐛 Fixes"),
    ("perf", "⚡ Performance"),
    ("refactor", "♻️ Refactoring"),
    ("docs", "📚 Docs"),
    ("test", "🧪 Tests"),
    ("ci", "⚙️ CI"),
    ("build", "🧹 Chores"),
    ("chore", "🧹 Chores"),
    ("revert", "⏪ Reverts"),
)
OTHER = "📦 Other"
TITLE_RE = re.compile(r"^(?P<type>[a-z]+)(?:\([^)]*\))?!?:\s*(?P<text>.+)$", re.I)


def merged_pulls(repo, version):
    """The pull requests merged into `release/v<version>`, or None.

    Each is `{"number", "title", "body", "author": {"login", "is_bot"}}` as
    `gh pr list --json` prints it. None means the list could not be read, and
    the caller publishes the theme line and the fragments alone rather than
    failing the tag's job. A `gh` that gave no answer is read the same way,
    and the line names it in the runner's words.
    """
    try:
        out = gitcmd.gh(
            "pr",
            "list",
            "--repo",
            repo,
            "--base",
            f"release/v{version}",
            "--state",
            "merged",
            "--limit",
            "500",
            "--json",
            # `labels` and `headRefName` are read by the mark, not here
            # (`.github/scripts/release_mark.py#chain_counts`): one call
            # serves both, so the two cannot disagree about the set.
            "number,title,author,body,labels,headRefName",
        )
    except gitcmd.Unrun as unrun:
        said = unrun.line
    else:
        said = None if not out.returncode else out.stderr.strip()
    if said is not None:
        print(
            "gh pr list failed, so the note is the theme line and the fragments "
            f"alone: {said}"
        )
        return None
    try:
        return json.loads(out.stdout)
    except ValueError:
        print(
            "gh pr list printed something that is not JSON, so the note is the "
            "theme line and the fragments alone"
        )
        return None


def outside(pull, owner):
    """The login of `pull`'s author if it is an outside contributor, else "".

    Outside means neither `owner` -- the repository's, read from `REPO` and
    never written down here -- nor a bot, whether `gh` marks it one, its login
    carries the `[bot]` suffix, or `gh` prints it as an `app/` account.
    """
    author = pull.get("author") or {}
    login = author.get("login") or ""
    if not login or login.lower() == owner.lower():
        return ""
    if author.get("is_bot") or login.endswith("[bot]") or login.startswith("app/"):
        return ""
    return login


def changes(pulls):
    """The release's own pull requests, oldest first."""
    return sorted(pulls or (), key=lambda p: p["number"])


# A code span, read as `lib/closing.py#SPAN` reads one, or a `<`
# outside one.
SPAN_OR_LT_RE = re.compile(f"({SPAN.pattern})|<")


def kind_and_text(title):
    """`(heading, text)`: where a title's line goes, and what it reads.

    The title is written as text: each `<` outside a code span becomes
    `&lt;`, which GitHub shows as `<`, so a tag a title quotes shows as the
    tag and opens or closes no fold or other element, and a code span stays
    code (one title in this repository holds three `details` tags bare).
    Both the fold's lines and the thanks section's read a title through
    here."""
    # A title that ends in the issue it closes, `... (#572)`, would read
    # `(#572) (#574)`; the closing list carries the issue instead.
    title = closing.MERGED_PR.sub("", title.strip())
    found = TITLE_RE.match(title)
    heading, text = OTHER, title
    if found:
        heading = dict(TYPES).get(found.group("type").lower(), OTHER)
        text = found.group("text")
    # A line reads as a sentence; a title that opens on code keeps its case.
    text = text[:1].upper() + text[1:]
    return heading, SPAN_OR_LT_RE.sub(lambda m: m.group(1) or "&lt;", text)


def closed_by(pull):
    """The issues `pull`'s body closes, in order, each once -- read the way
    `lib/closing.py#keywords_in` reads them for the closer, which is what
    closed them."""
    seen = []
    for number in keywords_in(pull.get("body") or ""):
        if number not in seen:
            seen.append(number)
    return seen


def thanks_section(pulls, owner):
    """`### 🙌 Thanks to` and one line per outside contributor, or "".

    A person with several pull requests gets one line naming them all, oldest
    first; the lines are ordered by the contributor's first pull request, so
    the order is the release's own.
    """
    by_login = {}
    for pull in changes(pulls):
        login = outside(pull, owner)
        if login:
            by_login.setdefault(login, []).append(pull)
    if not by_login:
        return ""
    lines = [THANKS_HEADING, ""]
    for login, mine in by_login.items():
        named = "; ".join(
            f"{kind_and_text(p['title'])[1]} (#{p['number']})" for p in mine
        )
        lines.append(f"- **@{login}** — {named}")
    return "\n".join(lines)


def tally(pulls, owner):
    """`(work, closed, people)`: the release's own pull requests, the issues
    their bodies close in order and each once, and the outside contributors'
    logins -- what the header counts."""
    work, closed = changes(pulls), []
    for pull in work:
        closed += [n for n in closed_by(pull) if n not in closed]
    people = {outside(p, owner) for p in work} - {""}
    return work, closed, people


def counts(work, closed, people):
    """The release's counts in words, one line each: the pull requests
    merged, the issues they closed, and the outside contributors only where
    there are some. `header` states them in these words, and
    `marked_header` states the same counts as badges (`count_badges`)."""
    lines = [
        console.plural(len(work), "pull request") + " merged",
        console.plural(len(closed), "issue") + " closed",
    ]
    if people:
        lines.append(console.plural(len(people), "outside contributor"))
    return lines


def paragraph(lines, before="", after=""):
    """One HTML paragraph on one source line: `<p>`, then `before`, then
    `lines` parted by `<br>`, then `after`, then `</p>`. GitHub reads a line
    that opens with `<p>` as the start of one HTML block, and the Markdown
    after it starts on the blank line that follows. It is one line because
    a line holding only an `<img>` would start a block of its own, and
    GitHub would then wrap each image in a paragraph of its own. It is no
    table, because GitHub draws a border around every table cell whatever
    the note's HTML asks."""
    return f"<p>{before}{'<br>'.join(lines)}{after}</p>"


def header(work, closed, people):
    """The header the note opens with, exactly as the note carries it: a
    paragraph holding `counts`. `release_mark.py` finds the header in a
    published note by this text, so a note edited by hand afterwards, or one
    whose header a run of the mark already replaced, is left alone. The
    paragraph's `<p>` and `</p>` bound the text, so the header the mark
    computes never matches inside a longer header line, such as one that
    holds an outside contributors line the mark's header lacks, or one whose
    count has one more leading digit."""
    return paragraph([html.escape(line) for line in counts(work, closed, people)])


# The marked header's badges, drawn by the Shields badge service from their
# address alone. A badge's two colours, the value's and then the label's, are
# read by its label from `BADGE_COLOURS`, so that a passing result does not
# read like a failure (#1496). Every label is grey except `CLEARED`'s. The
# suite's passed count is green, and the skipped, capped and deferred counts
# are grey. Every other label has no entry, so its value takes
# `BADGE_DEFAULT_COLOURS`, which is blue.
BADGE_LABEL_GREY = "555555"
BADGE_COLOURS = {
    # The wax seal's reds, read from `assets/seals/owl.svg`: the label's is the
    # wax's dark outer edge, the gradient's outer stop, and the value's is
    # the raised relief of the owl and its border. The owner chose the
    # stamp's reds for every colour of the wax seal (#857), so a wax seal redrawn in
    # other colours is a new icon, and the redraw edits this entry with it.
    "CLEARED": ("d42420", "8e0c12"),
    "suite": ("2ea44f", BADGE_LABEL_GREY),
    "skipped": ("6e7781", BADGE_LABEL_GREY),
    "capped": ("6e7781", BADGE_LABEL_GREY),
    "deferred": ("6e7781", BADGE_LABEL_GREY),
}
BADGE_DEFAULT_COLOURS = ("0969da", BADGE_LABEL_GREY)
BADGE_URL = "https://img.shields.io/badge/{label}-{value}-{colour}?labelColor={edge}"


def badge_text(text):
    """`text` as the badge service's address spells a label or a value: each
    `-` and then each `_` doubled, because the service splits the segment at
    a single `-` and reads a single `_` as a space, then percent-encoded with
    nothing left safe, so a space, a `/`, a `%`, a `?` and a `#` each mean
    themselves."""
    return urllib.parse.quote(text.replace("-", "--").replace("_", "__"), safe="")


def badge(label, value):
    """One badge as an `<img>`, in the service's default style: `label` and
    `value` on the two colours `BADGE_COLOURS` gives `label`, or
    `BADGE_DEFAULT_COLOURS` where it gives none. The value never changes
    them, so a `not read` takes its label's colours. Its alt text is the
    label and the value in words, so a reader whose client draws no image,
    or who opens the note while the service does not answer, still reads
    the result. The alt text is escaped, so a quote cannot end the
    attribute and a `<` opens no tag. The address needs no escape:
    `badge_text` leaves only letters, digits, `_.-~` and `%` in it, and
    `BADGE_URL`'s own characters mean nothing to HTML."""
    colour, edge = BADGE_COLOURS.get(label, BADGE_DEFAULT_COLOURS)
    url = BADGE_URL.format(
        label=badge_text(label),
        value=badge_text(value),
        colour=colour,
        edge=edge,
    )
    return f'<img src="{url}" alt="{html.escape(f"{label}: {value}")}">'


def count_badges(work, closed, people):
    """The counts `counts` states, as badge lines of `(label, value)` pairs:
    the pull requests merged, the issues they closed, and the outside
    contributors only where there are some."""
    lines = [
        [("pull requests", f"{len(work)} merged")],
        [("issues", f"{len(closed)} closed")],
    ]
    if people:
        lines.append([("outside contributors", str(len(people)))])
    return lines


def marked_header(image_url, alt, width, cleared, results, work, closed, people):
    """What replaces `header`'s paragraph once the release mark has run: a
    paragraph of the same shape holding the stamp's results as badges.
    `cleared` and `results` are badge lines, each a list of `(label, value)`
    pairs, as `release_mark.py#results` hands them: `cleared` the cleared
    version, then the commit and its branch; then the counts `count_badges`
    states; then `results`, the stamp's other rows. The badges of one line
    are parted by a space, and the lines by `<br>`. Given an `image_url`,
    the paragraph opens with the mark as an `<img>` `width` CSS pixels wide
    with `alt` as its text (the PNG is drawn at twice that for a
    high-density screen), floated left by `align="left"` so the badges stand
    beside it, and ends with a `<br clear="left">` that clears the float
    before the theme. Given none, where the repository leaves the image
    off, the paragraph holds the badges alone, with no float to clear, and
    `alt` and `width` are not read. A reader whose client draws no image
    still has every number, in each badge's alt text. The image's URL and
    `alt` are escaped, as `badge` escapes each badge's alt text, so a quote
    cannot end an attribute and a `<` opens no tag."""
    lines = [
        " ".join(badge(label, value) for label, value in line)
        for line in [*cleared, *count_badges(work, closed, people), *results]
    ]
    if image_url is None:
        return paragraph(lines)
    image = (
        f'<img src="{html.escape(image_url)}" alt="{html.escape(alt)}" '
        f'width="{int(width)}" align="left">'
    )
    return paragraph(lines, before=image, after='<br clear="left">')


def release_body(theme, rendered, pulls, owner):
    """The note: a header of the counts, the theme line, a summary a reader
    scans, and the fragments they can open.

    Read top to bottom it answers, in order, how big the release is -- the
    header `header` writes, which the mark later replaces -- what it is for,
    what changed -- one fold per type, its summary the type's
    name and the number of pull requests in it, holding one line per pull
    request with the issues it closed -- who outside the project
    helped, and how to get it. `rendered` follows, folded: the fragments
    `section` rendered, or for a range of settles alone the release pull
    request's body. It is the reasoning a reader wants for one change
    rather than the list they read for all of them. Every line is read from
    the milestone, the pull requests and the history; nothing here writes a
    sentence.

    Every fold's tags stand on lines of their own, with a blank line after
    the summary line and before the closing tag, so GitHub reads the lines
    between as Markdown. A pull request title reaches its fold with each `<`
    outside a code span written `&lt;` (`kind_and_text`), so a tag it quotes
    is text, inside a code span or out of one, and opens or closes no fold.
    A fragment is not escaped: it is the records' own text, and one holding
    a bare `details` tag is refused at `agentic pr-body` before its pull
    request opens. Nor is a release pull request's body, which the owner
    reads before the release merges.

    With no pull request to read -- the list failed, or a release was cut
    with none -- the note has no header and is the theme line and
    `rendered`, unfolded. With no theme, the line and the blank line beside
    it are left out.
    """
    work, closed, people = tally(pulls, owner)
    if not work:
        return "\n".join([*([theme, ""] if theme else []), rendered])
    groups = {}
    for pull in work:
        heading, text = kind_and_text(pull["title"])
        issues = closed_by(pull)
        line = f"- {text} (#{pull['number']})"
        if issues:
            line += " · closes " + ", ".join(f"#{n}" for n in issues)
        login = outside(pull, owner)
        if login:
            line += f" — thanks @{login}"
        groups.setdefault(heading, []).append(line)

    parts = [header(work, closed, people), *(["", theme] if theme else [])]
    order = list(dict.fromkeys([h for _, h in TYPES] + [OTHER]))
    for heading in order:
        if heading in groups:
            lines = groups[heading]
            parts += [
                "",
                "<details>",
                f"<summary>{heading} ({len(lines)})</summary>",
                "",
                *lines,
                "",
                "</details>",
            ]
    thanks = thanks_section(pulls, owner)
    if thanks:
        parts += ["", thanks]
    parts += [
        "",
        UPDATE_HEADING,
        "",
        "```",
        "/agentic:update",
        "```",
        "",
        "Then start a new session: the one you are in keeps the version it "
        "started with.",
        "",
        "<details>",
        f"<summary>{FULL_SUMMARY}</summary>",
        "",
        rendered,
        "",
        "</details>",
    ]
    return "\n".join(parts)


def create(repo, tag, title, body):
    gitcmd.gh(
        "release",
        "create",
        tag,
        "--repo",
        repo,
        "--title",
        title,
        "--notes",
        body,
        check=True,
    )


def main(argv=None):
    tag = os.environ["TAG"].strip()
    repo = os.environ["REPO"]
    dry = os.environ.get("DRY_RUN", "").strip() not in ("", "0", "false", "no")
    if dry:
        print("DRY_RUN — nothing will be written")

    version = version_of(tag)
    if version is None:
        print(
            f"{tag!r} is not a vX.Y.Z tag, so there is no release to read the "
            "fragments of. Nothing published."
        )
        return 1

    previous = previous_tag(tag)
    revisions = commit_range(previous, tag)
    entries = fragments(revisions)
    if not entries:
        span = f"after {previous} up to {tag}" if previous else f"up to {tag}"
        held = f" that {previous} does not already hold" if previous else ""
        commits, unsettled = settles(revisions)
        if not commits or unsettled:
            print(
                f"{tag} was pushed and no commit {span} added a changelog fragment"
                f"{held}, agentory/threads/<work-item-id>/changelog.md, so this "
                "release would be published with no notes at all."
            )
            for short, subject in unsettled:
                print(
                    f"{short} {subject} is no settle: it removes no work item "
                    f"directory under {optin.HOME}/{optin.WORK_ITEMS}/ whole"
                )
            return 1
        print(
            f"no commit {span} added a changelog fragment{held}, and each "
            "commit other than a merge is a settle, so the note carries the "
            "release pull request's body"
        )

    if release_exists(repo, tag):
        print(
            f"a release already exists at {tag} — leaving it. Nothing here "
            "overwrites a note, because one may have been edited by hand "
            "after it was published"
        )
        console.write_output("created", "false")
        return 0

    if entries:
        rendered = section(entries, repo)
    else:
        rendered, said = release_pull_body(repo, version, tag)
        if rendered is None:
            print(
                f"{tag}'s range carries settles alone, so its note is the release "
                f"pull request's body, and {said}. Nothing published."
            )
            return 1
        print(f"the note carries {said}")

    title, source = title_from(commit_message(tag), version, tag)
    print(f"title {title!r}, from {source}")
    description, said = milestone_description(repo, version)
    theme = theme_of(description)
    if theme:
        print(f"theme {theme!r}, from {said}")
    else:
        print(f"no theme line: {said}")
    pulls = merged_pulls(repo, version)
    body = release_body(theme, rendered, pulls, repo.split("/")[0])
    if pulls is not None and not thanks_section(pulls, repo.split("/")[0]):
        print("no outside contribution in this release, so no Thanks to section")
    if dry:
        print(f"would create the release at {tag} with {len(body)} characters of notes")
        print(body)
        console.write_output("created", "false")
        return 0
    create(repo, tag, title, body)
    print(f"published the release at {tag}")
    console.write_output("created", "true")
    return 0


if __name__ == "__main__":
    console.to_utf8()
    sys.exit(main())
