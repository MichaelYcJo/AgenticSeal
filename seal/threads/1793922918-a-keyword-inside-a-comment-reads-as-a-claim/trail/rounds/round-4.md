# Review round 4: 1793922918-a-keyword-inside-a-comment-reads-as-a-claim

```seal
target: cc63bf61, fixes 81cb7a4e..cc63bf61
```

This is a verifying round. It read the range `81cb7a4e..cc63bf61` in a `git clone --no-local` of the branch at `cc63bf61`, made under the round's scratch directory. The range holds the crafter's fix pass for round 3's finding 1 (`b7285b30`) and the orchestrator's fold of the frame and the close block (`cc63bf61`). The round read the closer's comment block whole (`.github/scripts/close_issues_on_release.py:103-178`), the changed lines of `frame/design.md`, `frame/plan.md` and `changelog.md` with their rows, `gaps.md`, and rounds 1 to 3.

Carried from rounds 1 to 3 and not re-established: the class of six readers of a body's closing keyword (`frame/design.md:19`), the regex timing over crafted bodies, the frame's probe over 300 merged bodies, the three measurements #1408 to #1410 as round 3's `gh pr view` read them, and `bin/seal layout --pairs` naming no pair among the new cases. The fix diff changes no code, so none of those checks has failed. The orchestrator's `slash_in_join` census over the nine changed `.py` files at the moved base `3282d799` is carried as its claim and was not re-run (see *Not judged*).

The axes walked inside the fix diff were three. Inputs: the shapes of an unclosed `<!--` behind a marker, with no space, one space, four spaces and five spaces after it, for the list markers and the quote marker apart. Exclusions and boundaries: the prefix of `COMMENT`'s second arm (`close_issues_on_release.py:176`) against the block starts CommonMark reads. The masking's direction, this change's own axis: whether each statement files each shape on the right side of GitHub's reading.

## Findings

### 1. The fix files every marker with no space as masked past GitHub, and the quote marker needs no space, so `><!--` is #1409's quote, which GitHub hides

```seal
severity: should
location: `.github/scripts/close_issues_on_release.py:165-167`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/changelog.md:3`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/frame/design.md:15`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/frame/design.md:33`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/frame/design.md:73`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/frame/design.md:75`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/frame/plan.md:59`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/frame/plan.md:61`
evidence: executed `uv run --no-project --with markdown-it-py --with cmarkgfm python test_tmp_round4_probe.py` in the clone (a probe, deleted); read `.github/scripts/close_issues_on_release.py:127-131`, `.github/scripts/close_issues_on_release.py:154-176`, `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py:402-404`, `.github/scripts/issue_claims_check.py:130`
regression: round-3#1
```

The unit is the sentence on a marker without its space, which `b7285b30` rewrote at `close_issues_on_release.py:165-167`, and its copies the fold `cc63bf61` added at `frame/design.md:15`, `:33`, `:75`, `frame/plan.md:59`, `:61` and the `changelog.md` sentence `b7285b30` added. The frame's Scope 1 before the fold (`frame/design.md:33` at `81cb7a4e`) called the four-space shape alone a limit, and its Limits bullet named `-<!--` with no reason given. The fix gave the reason "CommonMark reads no list item and so the opener stands after text" and the fold spread it to "a marker with no space", the wording of round 3's class list, though round 3 grounded it on `-<!--` alone.

Why it matters: the reason holds for a list marker and fails for the quote marker. A list marker needs a space or a tab after it, and a block quote marker does not (CommonMark 5.1). The tree says so twice: `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py:402-403` and `.github/scripts/issue_claims_check.py:130`. So `><!-- note` is a quote whose content opens an HTML block, with no text before the opener. The probe rendered `Closes #1401`, a blank line, the shape, a blank line and `Closes #103` with markdown-it in CommonMark mode and with cmark-gfm. For `><!-- note` both gave `<blockquote>\n<!-- note\n</blockquote>`, the same output as `> <!-- note`, which is #1409's shape and which GitHub hid. For `-<!-- note` and `1.<!-- note` both gave a paragraph holding the escaped text, as the sentence says. `keywords_in` read `['1401']` for all three, so `COMMENT` masks each.

So for `><!--` the closer agrees with GitHub's reading, by the parsers and by #1409, and the statements file it as masked past GitHub:

- The closer's comment block contradicts itself. `:127-129` says a `<!--` behind a block quote marker hides everything below it on GitHub. `:165-167` files "A marker without its space" under "Each but the last masks more than GitHub" (`:154`).
- `changelog.md:3` tells the release's readers that GitHub reads on after "a marker with no space".
- `frame/design.md:15` and `:33` say the opener "after a marker with no space" is masked past GitHub's reading. `:75` says GitHub reads on there. `:73` says GitHub hides behind "a list or quote marker with fewer spaces", which takes in `-<!--`, zero spaces, where `:75` says GitHub reads on.
- `frame/plan.md:59` lists "a marker with no space" among row A's failure shapes. `:61` counts it as row A2's gain.

The direction of the code is safe either way. The defect is the statements, and an agent acts on them. The comment block is the frame's chosen mechanism for the limits, "Limits, as sentences in the comment at the patterns, with no guard" (`frame/design.md:72`). An agent that narrows the second arm's prefix to stop masking past GitHub reads the comment's `:165` as licence to require a space after every marker. With `>` among them it would read a keyword below `><!--` that GitHub hides, and close an issue GitHub leaves open, the false record #266 guards against.

At `.github/scripts/close_issues_on_release.py:164-169`:

```python
# comment up to that `-->`, across blank lines too, where GitHub's inline
# comment ends with its paragraph. A list marker without its space, such as
# `-<!--` or `1.<!--`, counts as a line start, where CommonMark reads no list
# item and so the opener stands after text, which GitHub reads on after
# (#1404). A quote marker needs no space, so `><!--` is a quote, as #1409's
# is, and hides as GitHub hides it. A comment GitHub's renderer refuses for
# its contents, such as one holding `--`, is masked anyway. And a
```

At `changelog.md:3`, the sentence before "That is the direction that closes fewer":

```markdown
So does an opener after a list or quote marker and five spaces or more, or after a list marker with no space, where GitHub reads the opener as code or as text.
```

The frame statements are the orchestrator's, and the same snippet does not reach them. Each takes "list marker" where it says "marker":

- `frame/design.md:15`: "and one after a list marker with no space, which stands after text (#1404)".
- `frame/design.md:33`: "or after a list marker with no space, hides to the end of the text too".
- `frame/design.md:73`, its last sentence: "Behind a list marker and one to four spaces, or a quote marker and up to four spaces, `><!--` among them, GitHub hides what follows as the closer does (#1408, #1409)."
- `frame/design.md:75`: "A list marker without its space, such as `-<!--` or `1.<!--`, is treated as a line start too, where GitHub reads on, since the opener stands after text (#1404). A quote marker needs no space, so `><!--` is a quote, as #1409's is."
- `frame/plan.md:59` and `:61`: "a list marker with no space".

```seal
verdict: fixed aceeed37
answer: The finding holds: the sentence filed every marker with no space as masked past GitHub, and a quote marker needs no space, so `><!--` is #1409's quote, which GitHub hides. The per-shape fix was not applied. The orchestrator's judgment of 2026-11-06 in `frame/plan.md` *Judgments of the run* rules that the limits list no shape of the line-start test. The closer's Limits paragraph now states the rule once: the test reads one line's own text with no block model, so where CommonMark's block rules make GitHub read on past an opener it treats as a line start, as in an indented code block or after a marker that opens no list item, it masks to the end of the text and the closer closes fewer. It cites #1404, #1408, #1409 and #1410 as examples, not a list. The far `-->`, the comment GitHub refuses for its contents and the keyword joined to its number stand as they were. `changelog.md`'s sentence and `pr_body.py`'s Limits bullet take the same form; `pr_body.py`, which the finding's `location:` does not name, is on this block's `location:` line. Every changed line in the closer is a comment, and in `pr_body.py` a docstring line. The frame lines are the orchestrator's and are named in the hand-back.
location: `skills/code-review/scripts/pr_body.py:75-79`
```

## Confirmations

```seal
confirms: round-3#1
```
What holds: the closer's comment no longer calls the four-space opener the one shape masked past GitHub. `close_issues_on_release.py:130-131` now says the mask there "runs past GitHub's: it is one of the Limits below". The first Limits sentence at `:156-160` names the marker followed by five spaces, with `-     <!--` as its example, and labels it CommonMark's indented code block, unmeasured. Row A2 at `frame/plan.md:61` no longer says "alone", and `frame/design.md:73` names the marker shape. The probe confirmed the reading the fix gives: `-     <!-- note` and `>     <!-- note` each render as a list item or a quote holding `<pre><code>`, and `>    <!-- note`, four spaces, still renders as a quote holding the HTML block, so "five spaces or more" is the boundary for both markers (executed). The finding's own close holds. The `>` with no space is a new defect the fix's generalisation made, finding 1.

What matched: the fix diff changes comments alone in code. The probe parsed `close_issues_on_release.py` at `81cb7a4e` and at `cc63bf61`: the two syntax trees are equal and the texts differ (executed). The other changed files are the work item's records. The crafter's narrow run, 287 passed over the plan row's seven modules, was re-run in the clone at `cc63bf61`: 287 passed, exit 0 (executed, below).

What matched: apart from finding 1, no two statements of the closer's comment block contradict each other. `:127-129` states GitHub hiding behind a list or quote marker, citing #1408 and #1409, whose bodies held one space after the marker. `:156-160` narrows it for five spaces or more, which the probe showed CommonMark reads as code. `:154` says each limit but the last masks more than GitHub, and the five it lists bear it out: the indented shapes and the tab, the far `-->`, the list marker without its space, the comment GitHub refuses, and last the joined keyword, which closes more (read).

The orchestrator judged round 3's *Not judged* row, `- item`, a blank line and `    <!-- note`, an edge case to stay a limit and not to measure. This round agrees. `COMMENT` masks that line (round 3's probe, `['1401']`), so its reading is GitHub's if GitHub hides it and closes fewer if GitHub reads on. Neither outcome is the wrong direction. The comment at `close_issues_on_release.py:160-163` claims nothing about GitHub's reading of that shape. It names only the cost of telling it from a four-space opener. A measurement would change no line of code or comment.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The `slash_in_join` census from the moved base `3282d799` over the nine changed `.py` files, reported as no line. This round did not re-run it; the fix diff changes no code syntax tree | `tests/censuses.py` at `origin/release/v0.32.6` | the orchestrator, whose executed claim it is |
| The full suite, the repository-wide lint and the format check at `cc63bf61`: `unverified` | `seal/config.md`, the `Broad gate` row | the orchestrator, through its broad run after the fix pass for finding 1 |

## Probes

| Command | Result |
|---|---|
| `uv run --no-project --with markdown-it-py --with cmarkgfm python test_tmp_round4_probe.py` in the clone at `cc63bf61`: the closer's syntax tree at `81cb7a4e` and `cc63bf61`, and `keywords_in`, markdown-it (CommonMark mode) and cmark-gfm over `Closes #1401`, a blank line, a shape, a blank line and `Closes #103`, for nine shapes | The trees are equal and the texts differ. `keywords_in` read `['1401']` for all nine. Both parsers gave the same output for each shape. `><!-- note` and `> <!-- note` gave a quote holding the HTML block. `-<!-- note` and `1.<!-- note` gave a paragraph of escaped text. `- <!-- note` gave a list item holding the HTML block. `-     <!-- note`, `>     <!-- note` and `    <!-- note` gave a code block. `>    <!-- note` gave a quote holding the HTML block. Exit 0, deleted |
| `bin/test tests/github/test_close_issues_on_release.py tests/github/test_issue_claims_check.py tests/github/test_release_completeness_check.py tests/github/test_label_merged_on_release_branch.py tests/github/test_publish_release_note.py tests/skills/test_pr_body.py tests/behaviour/test_a_body_naming_two_issues_claims_one.py -q -p no:cacheprovider` in the clone at `cc63bf61` | 287 passed, exit 0 |
