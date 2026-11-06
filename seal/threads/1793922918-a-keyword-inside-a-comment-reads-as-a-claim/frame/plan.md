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
  keep no comment state (`unverified_check.py#readable`). So it masks only a
  comment that opens and closes on the line, and that is the safe direction
  for a reader that refuses.
- R26 imports from the closer and compiles nothing of its own. Two cases
  hold that: the identity case and `test_the_source_defines_no_keyword_list_of_its_own`.

What GitHub reads was measured twice by the orchestrator, on #1402 and
#1403, and is recorded in `frame/questions.md` Q1 and Q2 at `c1ae787d`
(design *Grounding*). It reads no keyword inside a closed comment, in any
of the four places tried, and none after a `<!--` that begins a line and
never closes. An unclosed `<!--` in the middle of a line was not tried
(`frame/questions.md` Q3).

Failure scenario of the chosen approach, six months on: a body writes a
`<!--` in the middle of a line, outside a code span, as prose about the
marker, and no `-->` follows. `COMMENT` hides everything after it, so a
`Closes` line further down is not read. The closer then closes fewer issues,
which is visible and re-runnable. R26 reports fewer. The completeness check
refuses the release, which is loud and names the issue. `pr_body` reads line
by line, so only the rest of that one line is hidden. Over the 300 bodies
measured (design *Grounding*), no body holds an unclosed opener outside code.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. `COMMENT` beside `FENCE` and `SPAN` in the closer, running to the first `-->` or to the end of the text, and `HIDDEN`, one pass over the three where the first to open wins, read by `keywords_in` and `prose_only`. `pr_body`'s tag reading takes the same blanking | The stray mid-line opener in *Technical context*. A comment GitHub refuses for its contents, such as one holding `--`, is masked anyway, and the closer closes fewer | Chosen. It reads every shape #1402 and #1403 measured as GitHub did. It keeps the 14 pinned shapes and the 300 measured bodies as they read today (executed, design *Grounding*). It keeps #956's finding that the readers share one definition, and #266's direction that masking more is safe for the closer, which decides the one unmeasured shape |
| A2. As A, but an opener that never closes is masked only where it begins a line, and read as text in the middle of a line, as CommonMark reads it | The closer would carry CommonMark's rule for where an HTML block may start: up to three spaces of indent, inside a list item at its content's column, after a block quote marker. #1403's comment under a list item shows the containers matter. Each container the rule misses is a shape where the closer reads a keyword GitHub hides, which is the wrong direction under #266 | Rejected until Q3 is measured. Where GitHub does read text after a mid-line opener, A closes fewer than GitHub, which is the safe direction, and A2 would then be the narrowing Q3 calls for |
| H. Keep an opener that never closes read as a claim, as the frame at `bc55d8da` had it | #1403 measured `<!-- Closes #32` at a line start with no `-->`, and GitHub made no reference. The closer would shut that issue when GitHub does not, which is the false record #266 guards against | Rejected on the measurement |
| B. Three passes in sequence: `FENCE`, then `COMMENT`, then `SPAN` | The body `` the `<!--` marker\nCloses #4\nthe `-->` end `` reads nothing, because the comment pass runs from inside the first span to inside the last. This repository's bodies name the markers in code spans, so real claims are lost (executed, `test_tmp_comment_probe.py`) | Rejected |
| B2. Three passes in sequence: `FENCE`, then `SPAN`, then `COMMENT` | `` <!-- it's ` here --> Closes #4 and `x` `` reads nothing, because the span pass pairs the comment's backtick with a later one and masks the claim. That is today's reading of this shape too (executed, same probe) | Rejected. A reads it as GitHub does |
| C. Replace the closer's patterns with the shared walk, `skills/verify/scripts/unverified_check.py#live_pieces` with comments on (#1185), the structure the tree keeps for every other reader of fences and comments | Two failures. First, the walk's fence rule is CommonMark's at most three spaces: `- item` then a fence indented four spaces reads `Closes #2` inside it as a claim under the line-local span reading (executed, same probe), where the closer masks it. Second, `CLOSING` matches across a newline (`Closes\n#7`), so the walk's pieces must be joined back before reading. The walk's treatment of an opener that never closes, hiding everything below it, was a third failure at `bc55d8da`. #1403 measured it as GitHub's own reading at a line start, so it no longer counts against C, and A now does the same | Rejected. The verdict no longer rests on the unclosed opener, where A and C now agree on every comment shape the probes tried. It rests on the premise that keeps the closer's own patterns, checked: `unverified_check.py:89-94` (read) lists the pull request body readers as keeping their own fence rule on purpose, opening a fence at any indentation as GitHub does, and the four-space fence shows C would change that |
| D. `hooks/lib/blocks.py#walk`, the hooks' walk of fences and comment blocks | It models only a comment that opens a line, so the inline comment stays a claim. It calls every line under a list marker uncertain and leaves it at the base reading, and bodies here are mostly bullets, so a comment under a bullet stays a claim | Rejected |
| E. Mask only the measured shape, a comment alone on its line | A comment in the middle of a line, one over several lines and one under a list item stay claims. #1403 measured that GitHub reads none of them (`frame/questions.md` Q1) | Rejected on the measurement |
| F. Leave `pr_body`'s tag reading on `SPAN` alone | `_composed`'s docstring, "blanked one way" (#1218), turns false: on one line, a keyword in a closed comment passes while a `<details>` beside it in the same comment is refused | Rejected. The tag reading follows the keyword reading, and the change is one name at `pr_body.py:631` |
| G. Keep R26 on its own copy of the masking, and widen only `keywords_in` | R26 reports a claim the closer no longer acts on, and the four readers stop reading alike. That reverses #956's R28 finding and `issue_claims_check.py:36-40` | Rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope 1 to 7 of `frame/design.md` | S1 to S9: the four new cases each shown red at `3cdf510d`, and the existing cases of `tests/github/test_close_issues_on_release.py`, `tests/github/test_issue_claims_check.py`, `tests/github/test_release_completeness_check.py`, `tests/github/test_label_merged_on_release_branch.py`, `tests/github/test_publish_release_note.py`, `tests/skills/test_pr_body.py` and `tests/behaviour/test_a_body_naming_two_issues_claims_one.py`, run narrow by the crafter | |

## Operational impact

None for a deployer. The release closer, the labeler, the completeness
check and the release note stop taking a keyword as a claim where it stands
inside an HTML comment or after a `<!--` that never closes. No body merged
in the last 300 pull requests reads differently (design *Grounding*).
`seal pr-body` stops refusing a copied line whose keyword or `details` tag
stands after a `<!--` on that line, up to a `-->` or the line's end.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
