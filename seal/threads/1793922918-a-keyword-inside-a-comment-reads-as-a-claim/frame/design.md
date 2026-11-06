# Design: a keyword inside an HTML comment reads as a claim (#1181)

## Grounding

The tree as read at `3cdf510d`.

| Policy clause | What it fixes for this work |
|---|---|
| `docs/releasing/issues-and-milestones.md` *A keyword claims the one number after it* (read) | The rule this work changes. It says a keyword inside a fence or a code span claims nothing, and that an HTML comment is still read as a claim "because whether GitHub reads a keyword inside one is unmeasured". It also fixes the direction: "Masking more closes fewer, and that is the safe direction". The work's subject is the code, so the new sentence goes into `## Rule changes` below for the settle, and this pull request does not edit the document (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, read) |
| The first measurement, on throwaway pull request #1402 into `main` (#1181 issuecomment-6672682090; the orchestrator's finding, executed 2026-11-06) | GitHub creates no closing reference from a keyword inside an HTML comment. `closingIssuesReferences` read 0, twice, with `<!-- Closes #1181 -->` as the body's only keyword, and 1 with `Closes #1181` also outside the comment. This is the answer to R28, and the four readers differ from it |
| The second measurement, on throwaway pull request #1403 into `main` (the orchestrator's finding, executed 2026-11-06; `frame/questions.md` Q1 and Q2 Status cells at `c1ae787d`, read) | `closingIssuesReferences`, read twice, named only the control, a `Closes` line outside any comment. It named none of these four shapes: a comment in the middle of a line, a comment over three lines, a comment indented under a list item, and `<!-- Closes #32` at the start of the body's last line with no `-->` after it anywhere |
| The third measurement, on throwaway pull requests #1404 and #1405 into `main`, one shape each with the control `Closes #1401` above it (the orchestrator's finding, executed 2026-11-06; `frame/questions.md` Q3 Status cell at `0be306a7`, read) | #1404 held `see the <!-- marker` in the middle of a line, no `-->` anywhere, and `Closes #1247` on the next line: GitHub named #1247. #1405 held `<!--` at a line start, no `-->` anywhere, and `Closes #103` on the next line: GitHub named the control alone. With #1402 and #1403 this gives three facts, and they are CommonMark's reading. A closed comment hides its text wherever it stands. An opener that never closes hides everything below it where it begins a line, since it opens an HTML block. An opener that never closes in the middle of a line is text |
| The side reading of #1402 (the orchestrator's finding) | After the body went back to the comment only, the count still read 1 at once; read again later on 2026-11-06 after #1402 was closed, it was empty (`gh pr view 1402`, executed by the crafter). It bears on no reader here: no code reads `closingIssuesReferences` (`git grep -n closingIssuesReferences` outside `seal/threads/` finds one line, `docs/releasing/branch-and-release.md:338`, executed). Every reader reads the body's text, and `docs/releasing/branch-and-release.md` *A closing keyword does nothing when the base is `release/vX.Y.Z`* (read) says GitHub forms no reference at all outside `main`. Nothing here builds on it |
| #956's audit, work item `1793171931-checks-that-read-text-pass-what-they-cannot-read` (#1134), read at `v0.24.0` with `git show` | Its `trail/phases/phase-3.md` rows name the two readers the issue calls R26 and R27. R26 is `.github/scripts/issue_claims_check.py#read`, `#prose_only` and `#claimed_spans`. R27 is `.github/scripts/release_completeness_check.py#judge` and the set D it reads. R28 found all four readers read every near miss alike, "since R26 imports `CLOSING`, `FENCE` and `SPAN` from the closer and `pr_body` calls `keywords_in`", and `<!-- Closes #18 -->` read as a claim by all four. Its `gaps.md` left one open row, R28's GitHub question, which #1181 now answers. This work keeps the audit's finding that the readers share one definition, and moves that definition |
| Why `keywords_in` strips fences and spans: `.github/scripts/close_issues_on_release.py:103-133` (read) | `docs/releasing/branch-and-release.md` carries `Closes #88` in a fence as the example to copy, and this repository's bodies quote its documents, so a quoted example would close the issue it names. Work item 1788844400 (#266), review round 1, listed five fence and span shapes the patterns missed. Three were masked. Two stayed unmasked on purpose: the four-space indented block, which bodies use to continue a bullet, and the HTML comment, because nobody had measured it. That comment block states the deciding direction: an issue left open is visible and a re-run reaches it, and a wrong close is a false record. This work masks the comment now that it is measured, and leaves the indented block as it is. The same direction decides the shapes the measurements did not reach, an unclosed opener behind a list marker, a block quote marker or an indent: they are masked as a line start (Scope 1) |
| `.github/scripts/issue_claims_check.py:36-40` (read) | "What GitHub does not read is defined once, next door." R26 imports its patterns from the closer and spells none of its own. The new pattern is imported the same way |
| `skills/code-review/scripts/pr_body.py:597-604` (read) | `_composed` reads the `details` tag and the closing keyword "on one line, blanked one way" (#1218). This work keeps that sentence true: the tag reading takes the same blanking as the keyword reading |
| `skills/verify/scripts/unverified_check.py:89-94` (read) | The pull request body readers keep their own fence rule on purpose: they open a fence at any indentation, as GitHub does. They are not moved onto the shared walk (`plan.md` *Alternatives considered*) |
| The class of readers, listed from what produces the defect (executed: `git grep -n "keywords_in\|CLOSING\b"` and a search for any other closing-keyword grammar in the code, outside `tests/`) | One grammar, `close_issues_on_release.py#CLOSING`, and two places that mask before it reads: `#keywords_in` and `issue_claims_check.py#prose_only`. Six readers stand on those two places. The four the issue names are the closer's `main` (`:420`), R26, R27 through `label_merged_on_release_branch.py#issues_in` (`release_completeness_check.py:393`) and `pr_body.py#_claims` (`:589`). Two more read through `keywords_in` and get the change without an edit of their own: `label_merged_on_release_branch.py#issues_in` (`:216`), which writes the `merged:` labels, and `publish_release_note.py#closed_by` (`:576`), which lists what a release closed. No other closing-keyword grammar exists in the code |
| Probe of the closed-comment masking, executed at `3cdf510d` in a `git clone --no-local` under the scratchpad (`python3 -I test_tmp_comment_probe.py`, exit 0) | All 14 shapes the current cases pin read the same under one leftmost pass as they do today. A `<!--` inside a code span with `-->` in a later span masks nothing. That shape is common in this repository's bodies, which name the markers in code spans. The body `` <!-- it's ` here --> Closes #4 and `x` `` reads #4. Today's reader reads nothing there, because its span pattern pairs the comment's backtick with a later one. Sequential passes in either order each lose one of these two shapes (`plan.md` rows B and B2) |
| Probe of the chosen `COMMENT`, executed at `0be306a7` in a new `git clone --no-local` under the scratchpad (`python3 -I test_tmp_line_start_probe.py`, exit 0) | All 35 shapes read as wanted, and the length-preserving blanking keeps every newline. The 14 pinned shapes read as today. Every closed comment is masked. The three measured unclosed shapes read as GitHub read them: `Closes #1401\nCloses #4\n<!-- Closes #32` gives `["1401", "4"]`, `Closes #1401\nsee the <!-- marker\nCloses #1247` gives `["1401", "1247"]`, and `Closes #1401\n<!--\nCloses #103` gives `["1401"]`. An unclosed opener after `- `, `> `, `1. ` or four spaces masks what follows. `a - <!-- b\nCloses #4` reads `["4"]`, since text stands before the marker. A `-->` on a later line ends a line-start opener. Read one line at a time, as `pr_body` reads, `text <!-- Closes #5` gives `["5"]` and `<!-- Closes #5` gives `[]` |
| Probe over real bodies, executed: `gh pr list --state merged --limit 300 --json number,body`, then the same probe file, exit 0 | 300 merged pull requests, #700 to #1400, 10 of them holding `<!--`: none reads differently under the chosen `COMMENT`. The change adds or drops no claim any merged body made |
| `.github/PULL_REQUEST_TEMPLATE.md` (read) | The template is HTML comments around two headings. An outside contributor's body keeps them, so a keyword typed inside one is a realistic shape |

## Scope

In:

1. `.github/scripts/close_issues_on_release.py` gains `COMMENT` with two arms.
   - A closed comment: `<!--` to the first `-->` after it, wherever it stands.
   - An opener that no `-->` follows anywhere, where nothing but spaces, tabs and block markers (`>`, `-`, `*`, `+`, or a number with `.` or `)`) stands before it on its line. It runs to the end of the text.

   An opener that never closes and has other text before it on its line is matched by neither arm, and stays text. The closer also gains `HIDDEN`, one pattern over a fence, a comment and a code span, where whichever opens first in the text wins. `keywords_in` masks `HIDDEN` in one pass, in place of its two passes, `FENCE` and then `SPAN`. The comment block above the patterns (`:103-133`) is rewritten in place. It states the three measured facts with #1402, #1403, #1404 and #1405 as their source. It also states the one judgment the measurements did not reach. An opener behind a block marker, or indented, is treated as a line start and hides to the end of the text, though GitHub may end it sooner, where its list item or quote ends. Masking more closes fewer (#266's direction).
2. `.github/scripts/issue_claims_check.py#prose_only` (R26) masks `HIDDEN` in one length-preserving pass, imported from the closer as `FENCE` and `SPAN` are today. Its import line, `__all__`, the docstring sentence at `:70-76` and `prose_only`'s docstring are rewritten in place to name the comment. A `#N` that `HIDDEN` hides is no longer listed as mentioned: GitHub renders neither the number nor its keyword.
3. `skills/code-review/scripts/pr_body.py`: `_claims` reads through `keywords_in` as before and inherits Scope 1. The `details` tag reading at `:631` blanks the line with `CLOSER.HIDDEN` in place of `CLOSER.SPAN`, so the tag and the keyword stay "blanked one way". The module docstring (`:40-45` and the *Limits* bullet at `:62-67`), `_claims`'s docstring (`:577-580`) and `_composed`'s docstring (`:597-604`) are rewritten in place. `seal pr-body` refuses a copied line that begins with a `<!--` that no `-->` closes on the line, where `close_issues_on_release.py#COMMENT`'s second arm matches at the line's start, since GitHub hides the lines after it (#1405). The line was refused at `063e0678` only where it held a keyword or a tag (round 1, finding 1).
4. `.github/scripts/release_completeness_check.py` (R27), `label_merged_on_release_branch.py#issues_in` and `publish_release_note.py#closed_by` read through `keywords_in` and take no code edit.
5. A case per named reader, each seen red against the code at `3cdf510d` (contract rule 15):
   - the closer, in `tests/github/test_close_issues_on_release.py#Test_keywords_in`;
   - R26, in `tests/github/test_issue_claims_check.py`;
   - R27, in `tests/github/test_release_completeness_check.py`;
   - `pr_body`, in `tests/skills/test_pr_body.py`.
   The closer's case holds S1 to S4. That covers both leftmost shapes, the backtick inside a comment and the opener inside a span, the two masked unclosed shapes, and one unclosed opener behind a list marker. `test_the_check_imports_the_closers_definition_rather_than_restating_it` asserts `check.HIDDEN is closer.HIDDEN` for each pattern R26 imports.
6. The comment shape still left read is the opener that never closes and has text before it on its line, #1404's shape. It takes the comment's row in `test_accepts_a_shape_left_unmasked_as_a_claim`, beside the four-space indented block, with #1404 named above the row. The code at `3cdf510d` already reads it as a claim, so contract rule 15's red is shown with the guard the row names removed: against `COMMENT` without its line-start condition, the frame's pattern at `c2732fb4`, the row fails. The phase record says so.
7. The citation at `skills/verify/scripts/unverified_check.py:92-93` names the section *A keyword claims the one number after it* in place of the bold lead *A keyword inside a fence or a code span claims nothing*, which the rule change below rewrites.

Out:

- The version move to 0.32.6 belongs to another work item of the release.
- The pull request template and every other reader of an HTML comment in a record or a config file (`hooks/lib/blocks.py` and its three readers, `unverified_check.py#live_lines`). They read records, not pull request bodies, and #1181 does not name them.
- GitHub's other differences from the closer that the audit recorded as limits, such as the four-space indented block, `Closes: #14` and an issue URL. #1181 asks about the comment alone.
- Whether a reference made by an earlier body edit survives a later one. No reader here reads GitHub's reference list (*Grounding*).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 the measured shape | Given a body whose only keyword is `<!-- Closes #6 -->`, when `keywords_in` reads it, then it returns `[]` | the closer's new case; red at `3cdf510d`, where it returns `["6"]` |
| S2 every closed comment | Given a comment in the middle of a line, a comment over several lines, a comment under a list item and an empty comment, each followed by `Closes #4` in prose, when `keywords_in` reads each, then it returns `["4"]` | the closer's new case |
| S3 the first to open wins | Given `` the `<!--` marker\nCloses #4\nthe `-->` end ``, then `["4"]`. Given `` <!-- it's ` here --> Closes #4 and `x` ``, then `["4"]` | the closer's new case; the second row is red at `3cdf510d` |
| S4 an opener that never closes | Given `Closes #1401\nCloses #4\n<!-- Closes #32` (#1403), then `["1401", "4"]`. Given `Closes #1401\n<!--\nCloses #103` (#1405), then `["1401"]`. Given `- <!-- note\nCloses #4`, then `[]`, the judgment the measurements did not reach. Given `Closes #1401\nsee the <!-- marker\nCloses #1247` (#1404), then `["1401", "1247"]` | the first three in the closer's new case, each red at `3cdf510d`, where they read `["1401", "4", "32"]`, `["1401", "103"]` and `["4"]`; the fourth is the row of Scope 6 |
| S5 nothing pinned moves | Given every body the existing cases of the six readers hold, then each reads as it did at `3cdf510d` | the existing cases of the four test modules in Scope 5, run narrow by the crafter |
| S6 R26 | Given `<!-- Closes #11, #22 -->\n\nDo not write that.`, when `issue_claims_check.read` reads it, then it returns `([], [], [])`. A comment over several lines keeps the line count, so the segments after it are cut where they were | the comment body as a row of R26's `test_the_shapes_the_closer_masks_since_266_are_masked_here_too`, and the line count as a new `Test_prose_only` case; red at `3cdf510d` |
| S7 R27 | Given a release range whose only body naming #92 holds it as `<!-- Closes #92 -->`, when the completeness check computes D, then #92 is not in D | R27's new case; red at `3cdf510d` |
| S8 `pr_body` | Given a copied `changelog.md` line holding `<!-- Closes #5 -->` after some text, and one holding `<!-- <details> -->` after some text, when `compose` runs, then neither is refused. A copied line holding `Closes #5` outside the comment is still refused at its line, and so is a copied line `text <!-- Closes #5`, which GitHub reads as text (#1404). A copied line `<!-- Closes #5` or `- <!-- note` is refused at its line for the opener, and a line `<!-- a note --> and text after it` is not refused, since GitHub reads the text after its `-->` (#1407) | `pr_body`'s new case; the first two are red at `3cdf510d` |
| S9 one definition | Given R26's module, then every masking pattern it uses is the closer's object, and the file compiles none of its own | the identity case and `test_the_source_defines_no_keyword_list_of_its_own`, both rewritten for `HIDDEN` |

## Data & interfaces

- `close_issues_on_release.py`: `COMMENT = re.compile(r"<!--.*?-->|^[ \t]*(?:(?:>|[-*+]|\d{1,9}[.)])[ \t]*)*<!--(?!.*?-->).*\Z", re.M | re.S)`, the pattern the probe ran. The crafter may spell it otherwise where S1 to S4 read the same, and says so in the phase record. `^` is a line start under `re.M`, and `\Z` is the end of the text whatever the flags. The lookahead keeps the second arm off an opener that a `-->` follows. `HIDDEN` is built from `FENCE`, `COMMENT` and `SPAN`, in that order, with `re.M | re.S`. `FENCE` comes first so that its group stays group 1 for its `\1`, or its group is named. `FENCE`, `SPAN` and `CLOSING` keep their names and values, because `publish_release_note.py:127` imports `SPAN` and `unverified_check.py:90` cites `#FENCE`. `keywords_in(body)` returns `CLOSING.findall(HIDDEN.sub(" ", body))`.
- `issue_claims_check.py` imports `CLOSING`, `HIDDEN` and `KEYWORDS`. `FENCE` and `SPAN` leave its import line where nothing in the module uses them any more.
- No exit code or command-line interface changes. `seal pr-body` gains one refusal message, for a copied line that begins with a `<!--` that no `-->` closes on the line. A refusal `pr_body` gave for a keyword or a tag that `HIDDEN` hides inside a comment that closes on the line is no longer given. A claim the closer, the labeler, the completeness check and the release note read where `HIDDEN` hides it is no longer read.
- Limits, as sentences in the comment at the patterns, with no guard. Each one but the last masks more than GitHub, so in each the closer closes fewer and the completeness check refuses the release, which is loud. None of the 300 measured bodies holds any of them.
  - An opener that never closes behind a list marker, a block quote marker or an indent hides to the end of the text. GitHub's HTML block may end sooner, where the list item or the quote ends. Following those ends would mean modelling CommonMark's containers (`plan.md` row A2).
  - A `<!--` in the middle of a line with a `-->` further down is read as a comment up to that `-->`, across blank lines too. GitHub's inline comment cannot cross the end of its paragraph.
  - A marker without its space, such as `-<!--`, is treated as a line start too.
  - A comment GitHub's renderer refuses for its contents, such as one holding `--`, is masked anyway.
  - A fence, a comment or a span is masked to spaces, so one standing between a keyword and its number, as in `Closes<!-- -->#4`, joins them into a claim GitHub does not read. In that one shape the closer closes more (round 1, finding 2).
- `pr_body` reads one copied line at a time. A copied line that begins with a `<!--` that no `-->` closes on the line is refused. A `<!--` with no `-->` after other text on its line is text, as GitHub reads it.

## Rule changes

- change
  file: docs/releasing/issues-and-milestones.md
  section: A keyword claims the one number after it
  from: **A keyword inside a fence or a code span claims nothing, whatever the fence
    or the span is made of.** A fence opens with backticks or tildes at any
    indent and closes on its own delimiter; a span is one backtick or two.
    Masking more closes fewer, and that is the safe direction: an issue left open
    is visible and a re-run reaches it, while a wrong close is a false record.
    Two shapes are still read as claims, each pinned by a case so a later
    widening is a deliberate red: a four-space indented block, because this
    repository's pull request bodies indent a bullet's continuation that way and
    masking it would drop a real `Closes #N`, and an HTML comment, because
    whether GitHub reads a keyword inside one is unmeasured.
    `.github/scripts/issue_claims_check.py` imports the closer's two patterns
    rather than spelling its own, so the check and the closer read one body the
    same way.
    check: tests/github/test_close_issues_on_release.py
  to: **A keyword inside a fence, a code span or an HTML comment claims nothing,
    whatever the fence or the span is made of.** A fence opens with backticks or
    tildes at any indent and closes on its own delimiter. A span is one backtick
    or two. Whichever of the three opens first in the body hides the other two
    inside it. Pull requests into `main` measured GitHub's reading of a comment
    for #1181, and the closer reads it the same way. A comment that closes hides
    its text wherever it stands. A `<!--` that never closes hides everything
    below it where it begins a line, and is text where other text stands before
    it on its line. Masking more closes fewer, and that is the safe direction:
    an issue left open is visible and a re-run reaches it, while a wrong close
    is a false record. So a `<!--` that never closes behind a list marker, a
    quote marker or an indent hides to the end of the body, though GitHub may
    end it where the list item or the quote ends. Two shapes are still read as
    claims, each pinned by a case so a later widening is a deliberate red. One
    is a four-space indented block, because this repository's pull request
    bodies indent a bullet's continuation that way and masking it would drop a
    real `Closes #N`. The other is a `<!--` that never closes after other text
    on its line, because GitHub reads what follows it.
    `.github/scripts/issue_claims_check.py` imports the closer's patterns rather
    than spelling its own, so the check and the closer read one body the same
    way.
    check: tests/github/test_close_issues_on_release.py tests/github/test_issue_claims_check.py

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The sentence saying GitHub's reading of a comment is unmeasured, and that the shape is read until someone measures it | `.github/scripts/close_issues_on_release.py:122-125` | The measured facts replace it in the same comment block, with #1402 to #1405 as their source (Scope 1) |
| The HTML comment as one of the two shapes that stay unmasked on purpose | `.github/scripts/close_issues_on_release.py:116-121` | The same comment block names the two shapes still read: the four-space indented block, and an opener that never closes after text on its line (Scope 1) |
| The row pinning `<!-- Closes #6 -->` as a claim, and the reason above it | `tests/github/test_close_issues_on_release.py#Test_keywords_in`, `test_accepts_a_shape_left_unmasked_as_a_claim`, `:441-445` | The shape is masked and S1 pins it. The row's place takes #1404's shape (Scope 6) |
| `keywords_in`'s two passes, `FENCE` and then `SPAN` | `.github/scripts/close_issues_on_release.py#keywords_in` | `HIDDEN`, one pass. The probes show the 14 pinned shapes unchanged |
| `prose_only`'s two passes, and its import of `FENCE` and `SPAN` | `.github/scripts/issue_claims_check.py#prose_only`, `:90`, `:331` | `HIDDEN`, imported from the closer |
| The identity asserts `check.FENCE is closer.FENCE` and `check.SPAN is closer.SPAN` | `tests/github/test_issue_claims_check.py#test_the_check_imports_the_closers_definition_rather_than_restating_it` | The assert on `HIDDEN`, the pattern R26 now imports (S9) |
| "in an HTML comment" among the places where `pr_body` refuses a tag GitHub renders as text | `skills/code-review/scripts/pr_body.py:62-67`, the module docstring's *Limits* | A comment `HIDDEN` hides on the line is masked now (Scope 3) |
| The rule sentence holding the HTML comment among the shapes still read as claims | `docs/releasing/issues-and-milestones.md` *A keyword claims the one number after it* | `## Rule changes` above, written by the settle |
| The citation of the bold lead *A keyword inside a fence or a code span claims nothing* | `skills/verify/scripts/unverified_check.py:92-93` | The section heading, which the rule change leaves in place (Scope 7) |

Framed 2026-11-06 by framer, before the build.
