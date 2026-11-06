# Implementation Plan: a keyword inside an HTML comment reads as a claim (#1181)

## Technical context

The tree as read at `3cdf510d`.

Every reader of a closing keyword in a pull request body reads one grammar,
`.github/scripts/close_issues_on_release.py#CLOSING` (`:99`). Before it
reads, it masks in one of two places. `#keywords_in` (`:135-137`) applies
`FENCE`, then `SPAN`, collapsing each match to one space.
`.github/scripts/issue_claims_check.py#prose_only` (`:151-164`) applies the
same two patterns and blanks each character, so offsets and line structure
survive. The closer's `main` (`:420`), `label_merged_on_release_branch.py#issues_in`
(`:216`), `release_completeness_check.py` through that function (`:393`),
`publish_release_note.py#closed_by` (`:576`) and `pr_body.py#_claims`
(`:589`) all call `keywords_in`. So a change to the two masking places
reaches all six readers, and the four the issue names among them.

Constraints the build keeps:

- `FENCE` carries a capture group and the backreference `\1`. In a combined
  pattern it stays the first alternative, or its group is named.
- `prose_only`'s substitution stays length-preserving with newlines kept
  (`issue_claims_check.py:151-164`, and the case
  `test_a_fence_does_not_splice_the_line_above_it_onto_the_line_below`).
- `pr_body.py` reads one copied line at a time over `readable` lines, which
  keep no comment state (`unverified_check.py#readable`). So it masks a
  comment that opens and closes on the line, refuses a line that begins
  with a `<!--` that never closes on it, and reads a `<!--` after other
  text as text.
- R26 imports from the closer and compiles nothing of its own. Two cases
  hold that: the identity case and `test_the_source_defines_no_keyword_list_of_its_own`.

The orchestrator measured what GitHub reads on #1402, #1403, #1404 and
#1405. The answers are recorded in `frame/questions.md` Q1 and Q2 at
`c1ae787d` and Q3 at `0be306a7` (design *Grounding*). They are three facts,
and they are CommonMark's reading. A closed comment hides its text wherever
it stands. A `<!--` that never closes hides everything below it where it
begins a line. A `<!--` that never closes after other text on its line is
text.

Failure scenario of the chosen approach, six months on: a body puts a
`<!--` that never closes where CommonMark's block rules make GitHub read
on past it, such as four spaces in (#1410), and a `Closes` line follows.
GitHub reads that `Closes` line. `COMMENT` treats
the opener as a line start and hides to the end of the text, so the closer
does not read it. The closer then closes fewer issues, which is visible and
re-runnable. R26 reports fewer. The completeness check refuses the release,
which is loud and names the issue. A `<!--` in the middle of a line with a
`-->` paragraphs further down fails the same way, in the same direction.
Over the 300 bodies measured (design *Grounding*), no body holds either
shape.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. `COMMENT` beside `FENCE` and `SPAN` in the closer, with two arms: a closed comment wherever it stands, and an opener that never closes where only spaces, tabs and block markers stand before it on its line, running to the end of the text. `HIDDEN` is one pass over the three where the first to open wins, read by `keywords_in` and `prose_only`. `pr_body`'s tag reading takes the same blanking | The openers the line-start test treats as a line start where CommonMark's block rules make GitHub read on, such as one in an indented code block (#1410), and the far `-->` in *Technical context*. A comment GitHub refuses for its contents, such as one holding `--`, is masked anyway. Each but one masks more than GitHub, so the closer closes fewer. A comment or a span between a keyword and its number closes more (`frame/design.md` *Data & interfaces*, Limits) | Chosen. It reads all three measured facts as GitHub did (#1402 to #1405), and all 35 probed shapes and the 300 measured bodies as wanted (executed, design *Grounding*). Its line-start test is one line's own text, with no block model. Behind a list or quote marker it reads as GitHub does (#1408, #1409). Where CommonMark's block rules make GitHub read on past an opener the test treats as a line start, it masks more (#1410), which is #266's direction. It keeps #956's finding that the readers share one definition |
| A1. `COMMENT` running to the first `-->` or to the end of the text from any opener, the frame at `c2732fb4` | #1404 measured `see the <!-- marker` with `Closes #1247` below it, and GitHub read #1247. A1 masks it, so the closer would leave #1247 open and the completeness check would refuse a release GitHub reads as complete. That is a false refusal on a shape the tree can tell apart, since text stands before the opener on its line | Rejected on the measurement. #266's direction licenses masking more only where the tree cannot tell, and here it can |
| A2. As A, but with CommonMark's container rules: an HTML block starts at up to three spaces of indent, or at a list item's content column, or after a block quote marker, and it ends where its container ends | The closer would carry a model of list items and quotes: where each starts, how far its content is indented, and where it ends. `skills/verify/scripts/unverified_check.py#live_lines` records what such a guess cost: "A guess at a block model fails for the same reason a guess at the comment state did, one level down". Each container the model gets wrong is either a keyword the closer reads and GitHub hides, which is the false record #266 guards against, or a mask A would also make | Rejected. Its gain over A is reading as GitHub does wherever CommonMark's block rules make GitHub read on past an opener A treats as a line start, as in an indented code block (#1410). No measured body holds such a shape. The list and quote shapes, its other gain, GitHub hides as A does (#1408, #1409), so its premise that an HTML block ends where its container ends is contradicted there. Its cost is a block model whose every miss can fall in the wrong direction. A's misses all fall in the safe one |
| A3. As A, but a line start allows only spaces and tabs before the opener, with no block markers | `- <!-- note` with no `-->` reads as text, while GitHub opens an HTML block inside the list item and hides every line below it, past the list's end (#1408). The closer would read a keyword there that GitHub hides, and close an issue GitHub does not | Rejected: it errs in the wrong direction under #266 |
| H. Keep an opener that never closes read as a claim, as the frame at `bc55d8da` had it | #1403 and #1405 measured an opener at a line start with no `-->`, with the keyword on its own line and on the line below, and GitHub made no reference either time. The closer would shut those issues when GitHub does not, which is the false record #266 guards against | Rejected on the measurement |
| B. Three passes in sequence: `FENCE`, then `COMMENT`, then `SPAN` | The body `` the `<!--` marker\nCloses #4\nthe `-->` end `` reads nothing, because the comment pass runs from inside the first span to inside the last. This repository's bodies name the markers in code spans, so real claims are lost (executed, `test_tmp_comment_probe.py`) | Rejected |
| B2. Three passes in sequence: `FENCE`, then `SPAN`, then `COMMENT` | `` <!-- it's ` here --> Closes #4 and `x` `` reads nothing, because the span pass pairs the comment's backtick with a later one and masks the claim. That is today's reading of this shape too (executed, same probe) | Rejected. A reads it as GitHub does: #1407 measured `<!-- ... --> Closes #103` at a line start, and GitHub read #103 |
| C. Replace the closer's patterns with the shared walk, `skills/verify/scripts/unverified_check.py#live_pieces` with comments on (#1185), the structure the tree keeps for every other reader of fences and comments | Three failures. First, the walk opens a comment at any `<!--` outside a span, mid-line included, and holds it to the next `-->` or the end of the file (`unverified_check.py#_scan`, `:393-397`, read). So #1404's shape, which GitHub reads, is hidden, as in A1. Second, the walk's fence rule is CommonMark's at most three spaces: `- item` then a fence indented four spaces reads `Closes #2` inside it as a claim under the line-local span reading (executed, `test_tmp_comment_probe.py`), where the closer masks it. Third, `CLOSING` matches across a newline (`Closes\n#7`), so the walk's pieces must be joined back before reading | Rejected. It fails a measured shape, and the premise that keeps the closer's own patterns is checked: `unverified_check.py:89-94` (read) lists the pull request body readers as keeping their own fence rule on purpose, opening a fence at any indentation as GitHub does, and the four-space fence shows C would change that |
| D. `hooks/lib/blocks.py#walk`, the hooks' walk of fences and comment blocks | It models only a comment that opens a line, so the inline comment stays a claim. It calls every line under a list marker uncertain and leaves it at the base reading, and bodies here are mostly bullets, so a comment under a bullet stays a claim | Rejected |
| E. Mask only the measured shape, a comment alone on its line | A comment in the middle of a line, one over several lines and one under a list item stay claims. #1403 measured that GitHub reads none of them (`frame/questions.md` Q1) | Rejected on the measurement |
| F. Leave `pr_body`'s tag reading on `SPAN` alone | `_composed`'s docstring, "blanked one way" (#1218), turns false: on one line, a keyword in a closed comment passes while a `<details>` beside it in the same comment is refused | Rejected. The tag reading follows the keyword reading, and the change is one name at `pr_body.py:631` |
| G. Keep R26 on its own copy of the masking, and widen only `keywords_in` | R26 reports a claim the closer no longer acts on, and the four readers stop reading alike. That reverses #956's R28 finding and `issue_claims_check.py:36-40` | Rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope 1 to 7 of `frame/design.md` | S1 to S9: the four new cases each shown red at `3cdf510d`, and the existing cases of `tests/github/test_close_issues_on_release.py`, `tests/github/test_issue_claims_check.py`, `tests/github/test_release_completeness_check.py`, `tests/github/test_label_merged_on_release_branch.py`, `tests/github/test_publish_release_note.py`, `tests/skills/test_pr_body.py` and `tests/behaviour/test_a_body_naming_two_issues_claims_one.py`, run narrow by the crafter | b28430f2 |

## Operational impact

None for a deployer. The release closer, the labeler, the completeness
check and the release note stop taking a keyword as a claim where it stands
inside an HTML comment, or below a `<!--` that never closes at a line start.
No body merged in the last 300 pull requests reads differently (design
*Grounding*). `seal pr-body` stops refusing a copied line whose keyword or
`details` tag stands inside a comment that closes on that line, and refuses
a copied line that begins with a `<!--` that no `-->` closes on it.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-06 | The closer's limits and every statement copying them name no shape of the line-start test one by one. They state the rule once: the test reads one line's own text with no block model, so where CommonMark's block rules make GitHub read on past an opener the test treats as a line start, such as an indented code block or a marker that opens no list item, it masks more, and the closer closes fewer. They then cite the measured shapes #1404, #1408, #1409 and #1410 as examples. | Rounds 3 and 4 each opened a `should` finding on a list the previous fix pass had grown: first the four-space shape called "the one", then the marker with no space, which holds for `-` and not for `>`. Each fix met one more CommonMark case, and the list cannot be finished without the block model row A2 rejects. A rule stated once has no list to contradict. | `skills/core/SKILL.md` *The rule a mechanism is kept against* ("when fixes chase one mechanism's edge cases, ask what it decides") |
