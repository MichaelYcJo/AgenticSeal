# Design: a keyword inside an HTML comment reads as a claim (#1181)

## Grounding

The tree as read at `3cdf510d`.

| Policy clause | What it fixes for this work |
|---|---|
| `docs/releasing/issues-and-milestones.md` *A keyword claims the one number after it* (read) | The rule this work changes. It says a keyword inside a fence or a code span claims nothing, and that an HTML comment is still read as a claim "because whether GitHub reads a keyword inside one is unmeasured". It also fixes the direction: "Masking more closes fewer, and that is the safe direction". The work's subject is the code, so the new sentence goes into `## Rule changes` below for the settle, and this pull request does not edit the document (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, read) |
| The measurement on #1181 (issuecomment-6672682090), as the spawn handed it (the orchestrator's finding; recorded `executed` by the orchestrator on 2026-11-06) | GitHub creates no closing reference from a keyword inside an HTML comment. On throwaway pull request #1402 into `main`, `closingIssuesReferences` read 0, twice, with `<!-- Closes #1181 -->` as the body's only keyword, and 1 with `Closes #1181` also outside the comment. This is the answer to R28, and the four readers differ from it |
| The second measurement, on throwaway pull request #1403 into `main` (the orchestrator's finding, executed 2026-11-06; `frame/questions.md` Q1 and Q2 Status cells at `c1ae787d`, read) | `closingIssuesReferences`, read twice, named only the control, a `Closes` line outside any comment. It named none of these four shapes: a comment in the middle of a line, a comment over three lines, a comment indented under a list item, and `<!-- Closes #32` at the start of the body's last line with no `-->` after it anywhere. So GitHub reads no keyword inside any closed comment it was shown, and none after an opener that begins a line and never closes. CommonMark's HTML block that opens with `<!--` at a line start runs to the end of the document, which agrees with this. The measurement had no keyword on a line below that opener, and it did not try an unclosed opener in the middle of a line (`frame/questions.md` Q3) |
| The side reading of the same probe (the orchestrator's finding) | After the body went back to the comment only, the count still read 1. It bears on no reader here: no code reads `closingIssuesReferences` (`git grep -n closingIssuesReferences` outside `seal/threads/` finds one line, `docs/releasing/branch-and-release.md:338`, executed). Every reader reads the body's text, and `docs/releasing/branch-and-release.md` *A closing keyword does nothing when the base is `release/vX.Y.Z`* (read) says GitHub forms no reference at all outside `main`. Nothing here builds on it |
| #956's audit, work item `1793171931-checks-that-read-text-pass-what-they-cannot-read` (#1134), read at `v0.24.0` with `git show` | Its `trail/phases/phase-3.md` rows name the two readers the issue calls R26 and R27. R26 is `.github/scripts/issue_claims_check.py#read`, `#prose_only` and `#claimed_spans`. R27 is `.github/scripts/release_completeness_check.py#judge` and the set D it reads. R28 found all four readers read every near miss alike, "since R26 imports `CLOSING`, `FENCE` and `SPAN` from the closer and `pr_body` calls `keywords_in`", and `<!-- Closes #18 -->` read as a claim by all four. Its `gaps.md` left one open row, R28's GitHub question, which #1181 now answers. This work keeps the audit's finding that the readers share one definition, and moves that definition |
| Why `keywords_in` strips fences and spans: `.github/scripts/close_issues_on_release.py:103-133` (read) | `docs/releasing/branch-and-release.md` carries `Closes #88` in a fence as the example to copy, and this repository's bodies quote its documents, so a quoted example would close the issue it names. Work item 1788844400 (#266), review round 1, listed five fence and span shapes the patterns missed. Three were masked. Two stayed unmasked on purpose: the four-space indented block, which bodies use to continue a bullet, and the HTML comment, because nobody had measured it. That comment block states the deciding direction: an issue left open is visible and a re-run reaches it, and a wrong close is a false record. This work masks the second shape now that it is measured, and leaves the first as it is. The same direction decides the one comment shape nobody has measured, the unclosed opener in the middle of a line: it is masked too (Scope 1) |
| `.github/scripts/issue_claims_check.py:36-40` (read) | "What GitHub does not read is defined once, next door." R26 imports its patterns from the closer and spells none of its own. The new pattern is imported the same way |
| `skills/code-review/scripts/pr_body.py:597-604` (read) | `_composed` reads the `details` tag and the closing keyword "on one line, blanked one way" (#1218). This work keeps that sentence true: the tag reading takes the same blanking as the keyword reading |
| `skills/verify/scripts/unverified_check.py:89-94` (read) | The pull request body readers keep their own fence rule on purpose: they open a fence at any indentation, as GitHub does. They are not moved onto the shared walk (`plan.md` *Alternatives considered*) |
| The class of readers, listed from what produces the defect (executed: `git grep -n "keywords_in\|CLOSING\b"` and a search for any other closing-keyword grammar in the code, outside `tests/`) | One grammar, `close_issues_on_release.py#CLOSING`, and two places that mask before it reads: `#keywords_in` and `issue_claims_check.py#prose_only`. Six readers stand on those two places. The four the issue names are the closer's `main` (`:420`), R26, R27 through `label_merged_on_release_branch.py#issues_in` (`release_completeness_check.py:393`) and `pr_body.py#_claims` (`:589`). Two more read through `keywords_in` and get the change without an edit of their own: `label_merged_on_release_branch.py#issues_in` (`:216`), which writes the `merged:` labels, and `publish_release_note.py#closed_by` (`:576`), which lists what a release closed. No other closing-keyword grammar exists in the code |
| Probe of the masking, executed at `3cdf510d` in a `git clone --no-local` under the scratchpad (`python3 -I test_tmp_comment_probe.py`, exit 0) | All 14 shapes the current cases pin read the same under the chosen approach as they do today. Under the chosen approach the measured shape, a comment followed by prose, a comment in the middle of a line, a comment over several lines, a comment under a list item and an empty comment are each masked, and the keyword after each is still read. A `<!--` inside a code span with `-->` in a later span masks nothing. That shape is common in this repository's bodies, which name the markers in code spans. The body `` <!-- it's ` here --> Closes #4 and `x` `` reads #4. Today's reader reads nothing there, because its span pattern pairs the comment's backtick with a later one |
| Probe of an opener with no `-->`, executed at `c1ae787d` in a new `git clone --no-local` under the scratchpad (`python3 -I test_tmp_unclosed_probe.py`, exit 0) | With `COMMENT` running to the end of the text where no `-->` follows, all 28 shapes read as wanted: the 14 the current cases pin read as today, every closed comment is masked, and `<!-- Closes #6\nCloses #4` and `text <!-- open\nCloses #4` read nothing. `Closes #4\n<!-- Closes #32` reads `["4"]`, as #1403 measured. A `<!--` alone in a code span, or alone in a fence, opens nothing. The length-preserving blanking keeps every newline. Over the same 300 merged bodies, none holds an opener with no `-->` outside code, and none reads differently from today |
| Probe over real bodies, executed: `gh pr list --state merged --limit 300 --json number,baseRefName,body`, then `python3 -I test_tmp_bodies_probe.py`, exit 0 | 300 merged pull requests, #700 to #1400, 10 of them holding `<!--`: none reads differently under the chosen approach. The change adds or drops no claim any merged body made |
| `.github/PULL_REQUEST_TEMPLATE.md` (read) | The template is HTML comments around two headings. An outside contributor's body keeps them, so a keyword typed inside one is a realistic shape |

## Scope

In:

1. `.github/scripts/close_issues_on_release.py` gains `COMMENT`, an HTML comment: `<!--` to the first `-->` after it, or to the end of the text where no `-->` follows. It also gains `HIDDEN`, one pattern over a fence, a comment and a code span, where whichever opens first in the text wins. `keywords_in` masks `HIDDEN` in one pass, in place of its two passes, `FENCE` and then `SPAN`. The comment block above the patterns (`:103-133`) is rewritten in place. It states the measured facts with #1402 and #1403 as their source: a closed comment anywhere, and an opener at a line start that never closes. It states the default for the one unmeasured shape, an opener in the middle of a line that never closes: masked to the end, because masking more closes fewer, and an issue left open is visible and re-runnable (#266's direction, `frame/questions.md` Q3).
2. `.github/scripts/issue_claims_check.py#prose_only` (R26) masks `HIDDEN` in one length-preserving pass, imported from the closer as `FENCE` and `SPAN` are today. Its import line, `__all__`, the docstring sentence at `:70-75` and `prose_only`'s docstring are rewritten in place to name the comment. A `#N` inside a closed comment is no longer listed as mentioned: GitHub renders neither the number nor its keyword.
3. `skills/code-review/scripts/pr_body.py`: `_claims` reads through `keywords_in` as before and inherits Scope 1. The `details` tag reading at `:631` blanks the line with `CLOSER.HIDDEN` in place of `CLOSER.SPAN`, so the tag and the keyword stay "blanked one way". The module docstring (`:40-45` and the *Limits* bullet at `:62-67`), `_claims`'s docstring (`:577-580`) and `_composed`'s docstring (`:597-604`) are rewritten in place.
4. `.github/scripts/release_completeness_check.py` (R27), `label_merged_on_release_branch.py#issues_in` and `publish_release_note.py#closed_by` read through `keywords_in` and take no code edit.
5. A case per named reader, each seen red against the code at `3cdf510d` (contract rule 15):
   - the closer, in `tests/github/test_close_issues_on_release.py#Test_keywords_in`;
   - R26, in `tests/github/test_issue_claims_check.py`;
   - R27, in `tests/github/test_release_completeness_check.py`;
   - `pr_body`, in `tests/skills/test_pr_body.py`.
   The closer's case holds the comment shapes of the two probe rows above. That covers both leftmost shapes, the backtick inside a comment and the opener inside a span, and both unclosed openers. `test_the_check_imports_the_closers_definition_rather_than_restating_it` asserts `check.HIDDEN is closer.HIDDEN` for each pattern R26 imports.
6. No comment shape is left read as a claim. `test_accepts_a_shape_left_unmasked_as_a_claim` keeps the four-space indented block as its one row, with its reason above it, and the comment's row leaves it. Two shapes of an unclosed opener are masked on a default, not on a measurement: one in the middle of a line, and a keyword on a line below one that begins a line. Each has a row of its own in the closer's case, with a comment naming Q3, so a later measurement that narrows either is a deliberate red.
7. The citation at `skills/verify/scripts/unverified_check.py:92` names the section *A keyword claims the one number after it* in place of the bold lead *A keyword inside a fence or a code span claims nothing*, which the rule change below rewrites.

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
| S4 an opener that never closes | Given `Closes #4\n<!-- Closes #32`, the shape #1403 measured, then `keywords_in` returns `["4"]`. Given `<!-- Closes #6\nCloses #4`, then `[]`: the keyword below the opener follows CommonMark's HTML block, on Q3's default. Given `text <!-- open\nCloses #4`, then `[]`, on Q3's default | the closer's new case; each is red at `3cdf510d`, where the three read `["4", "32"]`, `["6", "4"]` and `["4"]` |
| S5 nothing pinned moves | Given every body the existing cases of the six readers hold, then each reads as it did at `3cdf510d` | the existing cases of the four test modules in Scope 5, run narrow by the crafter |
| S6 R26 | Given `<!-- Closes #11, #22 -->\n\nDo not write that.`, when `issue_claims_check.read` reads it, then it returns `([], [], [])`. A comment over several lines keeps the line count, so the segments after it are cut where they were | R26's new case; red at `3cdf510d` |
| S7 R27 | Given a release range whose only body naming #92 holds it as `<!-- Closes #92 -->`, when the completeness check computes D, then #92 is not in D | R27's new case; red at `3cdf510d` |
| S8 `pr_body` | Given a copied `changelog.md` line holding `<!-- Closes #5 -->` after some text, and one holding `<!-- <details> -->` after some text, when `compose` runs, then neither is refused. The comment stands after text because the readers of a record refuse a line that begins with `<!--` (`unverified_check.py#comment_lines`, #1012), and that refusal is not this work's. A copied line holding `Closes #5` outside the comment is still refused at its line | `pr_body`'s new case; the first two are red at `3cdf510d` |
| S9 one definition | Given R26's module, then every masking pattern it uses is the closer's object, and the file compiles none of its own | the identity case and `test_the_source_defines_no_keyword_list_of_its_own`, both rewritten for `HIDDEN` |

## Data & interfaces

- `close_issues_on_release.py`: `COMMENT = re.compile(r"<!--.*?(?:-->|\Z)", re.S)`. `\Z` is the end of the text whatever the flags, so `re.M` in `HIDDEN` does not turn it into a line end. `HIDDEN` is built from `FENCE`, `COMMENT` and `SPAN`, in that order, with `re.M | re.S`. `FENCE` comes first so that its group stays group 1 for its `\1`. The crafter may use a named group instead and say so in the phase record. `FENCE`, `SPAN` and `CLOSING` keep their names and values, because `publish_release_note.py:127` imports `SPAN` and `unverified_check.py:90` cites `#FENCE`. `keywords_in(body)` returns `CLOSING.findall(HIDDEN.sub(" ", body))`.
- `issue_claims_check.py` imports `CLOSING`, `HIDDEN` and `KEYWORDS`. `FENCE` and `SPAN` leave its import line where nothing in the module uses them any more.
- No exit code, message text or command-line interface changes. A refusal `pr_body` gave for a keyword or a tag inside a comment on a copied line is no longer given. A claim the closer, the labeler, the completeness check and the release note read inside a comment, or after an opener that never closes, is no longer read.
- Limits, as sentences in the comment at the patterns, with no guard:
  - A `<!--` in the middle of a line, outside a code span, hides everything after it up to the next `-->`, or to the end of the body where none follows. CommonMark reads such an opener as text when its paragraph does not close it, and GitHub's reading is unmeasured (Q3). Where GitHub reads the keywords after it, the closer closes fewer, R26 reports fewer, and the completeness check refuses the release, which is loud. None of the 300 measured bodies holds this shape outside code.
  - `pr_body` reads one copied line at a time, so an opener with no `-->` on its line hides the rest of that line only. A copied line `text <!-- Closes #5` is no longer refused. Its pull request goes to a release branch, where GitHub acts on no keyword, and the closer reads the same mask, so that issue stays open.
  - A comment GitHub's renderer refuses for its contents, such as one holding `--`, is masked anyway, in the same direction.

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
    or two. A comment runs from `<!--` to the first `-->` after it, or to the
    end of the body where none follows. Whichever of the three opens first in
    the body hides the other two inside it. GitHub itself creates no closing
    reference from a keyword inside a closed comment, or after a `<!--` that
    begins a line and never closes, as measured on pull requests into `main`
    for #1181. Masking more closes fewer, and that is the safe direction: an
    issue left open is visible and a re-run reaches it, while a wrong close is
    a false record. So a `<!--` in the middle of a line that never closes is
    masked to the end as well, though nobody has measured GitHub's reading of
    it. One shape is still read as a claim, pinned by a case so a later
    widening is a deliberate red: a four-space indented block, because this
    repository's pull request bodies indent a bullet's continuation that way
    and masking it would drop a real `Closes #N`.
    `.github/scripts/issue_claims_check.py` imports the closer's patterns rather
    than spelling its own, so the check and the closer read one body the same
    way.
    check: tests/github/test_close_issues_on_release.py tests/github/test_issue_claims_check.py

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The sentence saying GitHub's reading of a comment is unmeasured, and that the shape is read until someone measures it | `.github/scripts/close_issues_on_release.py:122-125` | The measured facts replace it in the same comment block, with #1402 and #1403 as their source (Scope 1) |
| The sentence that two shapes stay unmasked on purpose, the comment among them | `.github/scripts/close_issues_on_release.py:116-121` | One shape stays unmasked, the four-space indented block, and the same comment block says so (Scope 1) |
| The row pinning `<!-- Closes #6 -->` as a claim, and the reason above it | `tests/github/test_close_issues_on_release.py#Test_keywords_in`, `test_accepts_a_shape_left_unmasked_as_a_claim`, `:440-444` | The shape is masked and S1 pins it. No comment shape is left read, so the row has no successor in that case. The unclosed openers are pinned as masked in S4 (Scope 6) |
| `keywords_in`'s two passes, `FENCE` and then `SPAN` | `.github/scripts/close_issues_on_release.py#keywords_in` | `HIDDEN`, one pass. The first probe shows the 14 pinned shapes unchanged |
| `prose_only`'s two passes, and its import of `FENCE` and `SPAN` | `.github/scripts/issue_claims_check.py#prose_only`, `:90`, `:331` | `HIDDEN`, imported from the closer |
| The identity asserts `check.FENCE is closer.FENCE` and `check.SPAN is closer.SPAN` | `tests/github/test_issue_claims_check.py#test_the_check_imports_the_closers_definition_rather_than_restating_it` | The assert on `HIDDEN`, the pattern R26 now imports (S9) |
| "in an HTML comment" among the places where `pr_body` refuses a tag GitHub renders as text | `skills/code-review/scripts/pr_body.py:62-67`, the module docstring's *Limits* | A comment on the line is masked now, to the line's end where it does not close on it (Scope 3) |
| The rule sentence holding the HTML comment among the shapes still read as claims | `docs/releasing/issues-and-milestones.md` *A keyword claims the one number after it* | `## Rule changes` above, written by the settle |
| The citation of the bold lead *A keyword inside a fence or a code span claims nothing* | `skills/verify/scripts/unverified_check.py:92` | The section heading, which the rule change leaves in place (Scope 7) |

Framed 2026-11-06 by framer, before the build.
