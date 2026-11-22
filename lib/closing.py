"""What a pull request body and a squash subject say about issues and pull
requests, read once for every reader.

`keywords_in` reads the issues a body closes, as GitHub reads them on a pull
request into the default branch. `MERGED_PR` reads the pull request a squash
merge's subject names. The readers are `skills/code-review/scripts/pr_body.py`,
`skills/code-review/scripts/chain_check.py#carried_by`, and the release
automation under `.github/scripts/`: `close_issues_on_release.py`,
`issue_claims_check.py`, `label_merged_on_release_branch.py` and
`publish_release_note.py`. Each loads this module through
`lib/sibling.py#load` and keeps no copy, so a mask widened here widens for
all of them.

Standard library only, and Python 3.9 syntax: `pr_body.py` reaches it on
whatever `python3` starts it.
"""

import re

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
# `feat: … (#100)` -- what a squash merge puts in the subject. One pattern
# serves `search` and `sub` alike: on a stripped subject the leading `\s*`
# changes no `search`, and a `sub` takes the space before the number with it.
MERGED_PR = re.compile(r"\s*\(#(\d+)\)\s*$")

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
# `tests/lib/test_closing.py#Test_keywords_in`. A four-space
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
