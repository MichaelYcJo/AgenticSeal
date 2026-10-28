#!/usr/bin/env python3
"""Publish the GitHub Release for the tag that was just pushed.

Publishing a release note was a habit and nothing else. `docs/release-checklist.md`
walked to the tag and stopped, no workflow did it, and **three consecutive
releases shipped without one** -- measured on 2026-09-13 while cutting a
release, by the run that would have made it four (#386). The tag beside it
gets done every time, because `hooks/version-check.py` reads it and an
untagged release is one no installed session is ever told about. The note had
no reader in the tree at all, so nothing noticed its absence.

So this reads the tag instead of asking anybody to remember. It runs when a
`v*` tag is pushed, which is the release's last manual act and the moment
`docs/branch-and-release.md` says stays a person's.

**The body is built from the release's changelog fragments, read from the
history at the tag** (#1053). A change writes its note once, in
`seal/threads/<work-item-id>/changelog.md`, and no copy of the notes is kept
in the tree. The fragments are the ones the commits after the previous
`vX.Y.Z` tag added, each read at the newest commit of that range whose tree
holds it, so a work item a settle removed before the tag still has its entry.
Each goes under an HTML comment naming its work item, the one link from a
released entry back to the work that produced it.

**The note opens with the release's theme**, the first sentence of the
description of the milestone `release: X.Y.Z`, its `Purpose:` label left out.

The fragments are also a page of reasoning per change, and a note that was
only that read as a wall of prose to somebody asking what changed (#572). So
after the theme the note says what the pull requests merged into
`release/vX.Y.Z` already say -- a count, one line per pull request under its
conventional-commit type with the issues its body closes, a credit for every
outside contributor, how to update -- and keeps the fragments beneath,
folded. Nothing here composes prose: every line is a milestone's sentence, a
pull request title, a number, a handle or a fragment.

**The title comes from the tagged commit's message**, which carries the
`release: X.Y.Z symptoms: <symptoms>` line `docs/release-checklist.md`
*5. The release pull request* prescribes. Three other sources were measured and rejected: the merge
commit's *subject* is GitHub's `Merge pull request #N from <owner>/...` line
and not the title at all; the `## X.Y.Z -- <date>` changelog heading carries
a date and no prose, so a title taken from it drops the symptom line every
existing release carries; and the twenty-three hand-written release names
reproduce neither the pull request titles nor the changelog headings, so
nothing can reproduce them. That step's line is the only written-down source, and so
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

**It does fail for a range that added no fragment**, which is the opposite
direction on purpose. That is the release shipping unexplained, and the
fragments are the whole of what this publishes.

**Outside contributors are thanked by handle.** An outside contribution
carries no work item and so no changelog fragment, so a release that carried
one credited it only when somebody remembered to write a sentence about it.
The set is read instead: the pull requests' authors, less the repository
owner and any bot. A release with none gets no credit line and no count.

**The summary adds no way to fail.** A `gh` call that cannot list the pull
requests publishes the theme line and the fragments alone, as every note
before #572 was the section alone, and says so in the job log -- a plain
note is fixable in one edit, and a failed job at the tag is not.

**It says whether it created the release** (#718). `created=true` or
`created=false` goes to `$GITHUB_OUTPUT` where the workflow sets it, and the
`seal` job in the same workflow runs only on `true`: the seal edits the note,
so it is held to the line above and never touches a release this run did
not write. The glance block is built by `glance`, and the seal's replacement
for it by `sealed_glance`, so both shapes live in the file that owns the
heading and the seal finds the block by the function that wrote it.

`DRY_RUN=1` prints the note it would create and writes nothing, for the reason
`close_issues_on_release.py`'s docstring gives: a tool whose only mode has
side effects gets run for its output sooner or later, and the first person to
do it is whoever wrote it.

Environment: `TAG` (`github.ref_name`), `REPO`, `GH_TOKEN`, and
`GITHUB_OUTPUT` where the workflow runner sets it.

Exit codes: 0 published, or already published, or a dry run -- 1 the tag is
not `vX.Y.Z`, or its range added no fragment.
"""

import html
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "..", "hooks", "lib"))
import console  # noqa: E402
from blocks import gfm_lines  # noqa: E402
from close_issues_on_release import keywords_in  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
# A work item's changelog fragment, its id captured.
FRAGMENT_RE = re.compile(r"^seal/threads/([^/]+)/changelog\.md$")
# The milestone a release's theme is read from, by its title.
MILESTONE_TITLE = "release: {version}"
PURPOSE_LABEL = "Purpose:"

# `vX.Y.Z`. Anything else under `v*` -- `v1.2`, `vnext`, a typo -- is a shape
# this cannot name a version for, and it says so rather than guessing one.
# `label_merged_on_release_branch.py#version_of` refuses a branch name the
# same way and for the same reason.
TAG_RE = re.compile(r"^v(\d+\.\d+\.\d+)$")


# The title line `docs/release-checklist.md` *5. The release pull request*
# prescribes for the release
# pull request, which is what the merge commit's body carries: a whole line,
# one space after each colon and after the version, read exactly so.
#
# **The symptoms are required, not optional.** `release: 0.12.3` with nothing
# after it was measured in this repository's own history, and reading a title
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


def run(*args):
    out = subprocess.run(args, capture_output=True, encoding="utf-8")
    if out.returncode:
        sys.exit(f"{' '.join(args)} failed: {out.stderr.strip()}")
    return out.stdout


def version_of(tag):
    """`X.Y.Z` for a `vX.Y.Z` tag, or None for any other name."""
    found = TAG_RE.match((tag or "").strip())
    return found.group(1) if found else None


def git(*args):
    """`git` run in the repository at `ROOT`; its standard output."""
    return run("git", "-C", ROOT, *args)


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
    """`[(work item id, body)]` for every changelog fragment a commit in
    `revisions` added, in id order, an empty body skipped. The paths are
    sorted, and each holds its id, so the paths' order is the ids'.

    Each is read at the newest commit of the range whose tree holds it, so a
    fragment a settle removed before the tag is read as it stood last.
    `--no-renames` keeps a fragment from reading as a rename of an older one
    the settle deleted in the same range.
    """
    added = git(
        "log",
        "--no-renames",
        "--diff-filter=A",
        "--name-only",
        "--format=",
        revisions,
    )
    out = []
    # exempt from splitlines: git output
    for path in sorted(set(added.splitlines())):
        found = FRAGMENT_RE.match(path)
        if not found:
            continue
        for commit in git("log", "--format=%H", revisions, "--", path).split():
            if git("ls-tree", "--name-only", commit, "--", path).strip():
                body = git("show", f"{commit}:{path}").strip()
                if body:
                    out.append((found.group(1), body))
                break
    return out


def section(entries):
    """The fragments as the note carries them: each work item's marker line,
    its body, and a blank line before the next."""
    return "\n\n".join(f"<!-- specs/{item} -->\n{body}" for item, body in entries)


def milestone_description(repo, version):
    """`(the description of the milestone `release: <version>`, why not)`.

    The first element is "" where there is no description to read: the list
    could not be read, no milestone carries the title, or its description is
    empty. The second element says which, for the job log. `--paginate`
    merges the pages into one list (`release_completeness_check.py`'s
    `milestone_titles` measured it).
    """
    out = subprocess.run(
        [
            "gh",
            "api",
            "--paginate",
            f"repos/{repo}/milestones?state=all&per_page=100",
        ],
        capture_output=True,
        encoding="utf-8",
    )
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
    return run("git", "log", "-1", "--format=%B", tag)


def release_exists(repo, tag):
    """Whether a GitHub Release already sits at `tag`.

    A 404 here is the answer rather than a failure -- the usual case is that
    no release exists yet, which is the whole reason this job runs. Anything
    else still stops the run, because a token without the scope to read
    releases would otherwise be read as "none exists" and publish a second.
    """
    out = subprocess.run(
        ["gh", "api", f"repos/{repo}/releases/tags/{tag}"],
        capture_output=True,
        encoding="utf-8",
    )
    if out.returncode:
        if "Not Found" in out.stderr or "404" in out.stderr:
            return False
        sys.exit(f"gh api releases/tags/{tag} failed: {out.stderr.strip()}")
    return True


THANKS_HEADING = "### 🙌 Thanks to"
GLANCE_HEADING = "### 📊 At a glance"
FULL_SUMMARY = "📋 Full changelog — what each change does and why"
UPDATE_HEADING = "### ⬆️ Update"

# A pull request title's conventional-commit type, and the heading its line
# goes under. The order here is the order the note reads in: what a user can
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
# The preparation pull request -- `chore: release X.Y.Z -- ...` -- moves the
# version and changes nothing a user reads, so it is not one of the changes.
PREPARATION_RE = re.compile(r"^chore:\s*release\s+\d+\.\d+\.\d+\b", re.I)
# A title that ends in the issue it closes, `... (#572)`, would read
# `(#572) (#574)`; the closing list carries the issue instead.
TRAILING_REF_RE = re.compile(r"\s*\(#\d+\)\s*$")


def merged_pulls(repo, version):
    """The pull requests merged into `release/v<version>`, or None.

    Each is `{"number", "title", "body", "author": {"login", "is_bot"}}` as
    `gh pr list --json` prints it. None means the list could not be read, and
    the caller publishes the theme line and the fragments alone rather than
    failing the tag's job.
    """
    out = subprocess.run(
        [
            "gh",
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
            # `labels` and `headRefName` are read by the seal, not here
            # (`.github/scripts/release_seal.py#chain_counts`): one call
            # serves both, so the two cannot disagree about the set.
            "number,title,author,body,labels,headRefName",
        ],
        capture_output=True,
        encoding="utf-8",
    )
    if out.returncode:
        print(
            "gh pr list failed, so the note is the theme line and the fragments "
            f"alone: {out.stderr.strip()}"
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
    """The release's own pull requests, oldest first, less the preparation."""
    return [
        p
        for p in sorted(pulls or (), key=lambda p: p["number"])
        if not PREPARATION_RE.match(p.get("title", "").strip())
    ]


def kind_and_text(title):
    """`(heading, text)`: where a title's line goes, and what it reads."""
    title = TRAILING_REF_RE.sub("", title.strip())
    found = TITLE_RE.match(title)
    heading, text = OTHER, title
    if found:
        heading = dict(TYPES).get(found.group("type").lower(), OTHER)
        text = found.group("text")
    # A line reads as a sentence; a title that opens on code keeps its case.
    return heading, text[:1].upper() + text[1:]


def closed_by(pull):
    """The issues `pull`'s body closes, in order, each once -- read the way
    `close_issues_on_release.py` reads them, which is what closed them."""
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
    logins -- what the glance block counts."""
    work, closed = changes(pulls), []
    for pull in work:
        closed += [n for n in closed_by(pull) if n not in closed]
    people = {outside(p, owner) for p in work} - {""}
    return work, closed, people


def glance(work, closed, people):
    """The `### 📊 At a glance` block exactly as the note carries it: the
    heading and a table of the counts, the outside contributors' row only
    where there are some. `release_seal.py` finds the block in a published
    note by this text, so a note edited by hand afterwards is left alone."""
    parts = [
        GLANCE_HEADING,
        "",
        "| | |",
        "| --- | ---: |",
        f"| 🔀 Pull requests | **{len(work)}** |",
        f"| ✅ Issues closed | **{len(closed)}** |",
    ]
    if people:
        parts.append(f"| 🙌 Outside contributors | **{len(people)}** |")
    return "\n".join(parts)


def sealed_glance(image_url, alt, width, work, closed, people):
    """What replaces `glance`'s block once the release seal is attached
    (#718): the heading, the seal as an image with `alt` as its text, a blank
    line, and one line carrying every row the table had, in its order, so a
    reader whose browser does not draw the image still has every count.

    The image is an `<img>` `width` CSS pixels wide (#832): the PNG is drawn
    at twice that for a high-density screen, and Markdown's image syntax has
    no width, so it would show twice its size. The URL and `alt` are escaped
    for the attribute each sits in, so a quote in either cannot end it."""
    counts = [
        f"🔀 Pull requests **{len(work)}**",
        f"✅ Issues closed **{len(closed)}**",
    ]
    if people:
        counts.append(f"🙌 Outside contributors **{len(people)}**")
    image = (
        f'<img src="{html.escape(image_url)}" alt="{html.escape(alt)}" '
        f'width="{int(width)}">'
    )
    return "\n".join([GLANCE_HEADING, "", image, "", " · ".join(counts)])


def write_output(name, value):
    """`name=value` appended to `$GITHUB_OUTPUT` where it is set. A write
    that fails is printed and ignored: the release is already published, and
    a job that went red over its own output would be a failed job at the tag
    for nothing (#718)."""
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    try:
        with open(path, "a", encoding="utf-8") as handle:
            handle.write(f"{name}={value}\n")
    except OSError as problem:
        print(f"could not write {name}={value} to $GITHUB_OUTPUT: {problem}")


def release_body(theme, rendered, pulls, owner):
    """The note: the theme line, a summary a reader scans, and the fragments
    they can open.

    Read top to bottom it answers, in order, what the release is for, how
    big it is, what changed -- one line per pull request under its type, with
    the issues it closed -- who outside the project helped, and how to get
    it. The fragments `section` rendered follow, folded, because they are
    the reasoning a reader wants for one change rather than the list they
    read for all of them. Every line is read from the milestone, the pull
    requests and the history; nothing here writes a sentence.

    With no pull request to read -- the list failed, or a release was cut
    with none -- the note is the theme line and `rendered`, unfolded. With no
    theme, the line and the blank line after it are left out.
    """
    opening = [theme, ""] if theme else []
    work, closed, people = tally(pulls, owner)
    if not work:
        return "\n".join([*opening, rendered])
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

    parts = [*opening, glance(work, closed, people)]
    order = list(dict.fromkeys([h for _, h in TYPES] + [OTHER]))
    for heading in order:
        if heading in groups:
            parts += ["", f"### {heading}", ""] + groups[heading]
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
    run(
        "gh",
        "release",
        "create",
        tag,
        "--repo",
        repo,
        "--title",
        title,
        "--notes",
        body,
    )


def main(argv=None):
    console.to_utf8()
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
    entries = fragments(commit_range(previous, tag))
    if not entries:
        span = f"after {previous} up to {tag}" if previous else f"up to {tag}"
        print(
            f"{tag} was pushed and no commit {span} added a changelog fragment, "
            "seal/threads/<work-item-id>/changelog.md, so this release would be "
            "published with no notes at all."
        )
        return 1

    if release_exists(repo, tag):
        print(
            f"a release already exists at {tag} — leaving it. Nothing here "
            "overwrites a note, because one may have been edited by hand "
            "after it was published"
        )
        write_output("created", "false")
        return 0

    title, source = title_from(commit_message(tag), version, tag)
    print(f"title {title!r}, from {source}")
    description, said = milestone_description(repo, version)
    theme = theme_of(description)
    if theme:
        print(f"theme {theme!r}, from {said}")
    else:
        print(f"no theme line: {said}")
    pulls = merged_pulls(repo, version)
    body = release_body(theme, section(entries), pulls, repo.split("/")[0])
    if pulls is not None and not thanks_section(pulls, repo.split("/")[0]):
        print("no outside contribution in this release, so no Thanks to section")
    if dry:
        print(f"would create the release at {tag} with {len(body)} characters of notes")
        print(body)
        write_output("created", "false")
        return 0
    create(repo, tag, title, body)
    print(f"published the release at {tag}")
    write_output("created", "true")
    return 0


if __name__ == "__main__":
    sys.exit(main())
