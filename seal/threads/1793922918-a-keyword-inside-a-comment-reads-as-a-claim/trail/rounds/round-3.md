# Review round 3: 1793922918-a-keyword-inside-a-comment-reads-as-a-claim

```seal
target: 7aea41cd, fixes bc5dfb15..7aea41cd
```

This is a verifying round. It read the range `bc5dfb15..7aea41cd` in a `git clone --no-local` of the branch at `7aea41cd`, made under the round's scratch directory. The range holds the crafter's second fix pass (`a2e829ed`) and the orchestrator's fold of the frame and `gaps.md` (`7aea41cd`). No finding of round 2 named this fix pass, because round 2 opened none. The pass answers the measurements #1408, #1409 and #1410. The round read `frame/design.md` whole, `frame/plan.md` rows A to A3 and the failure scenario, `gaps.md` and `changelog.md` at HEAD, and rounds 1 and 2 whole.

Carried from rounds 1 and 2 and not re-established: the class of six readers of a body's closing keyword (`frame/design.md:19`), the regex timing over crafted bodies, the frame's probe over 300 merged bodies, and `bin/seal layout --pairs` naming no pair among the new cases. The fix diff changes no code, so none of those checks has failed.

The axes walked inside the fix diff were three. Inputs: the three measured bodies and the shapes of an unclosed `<!--` behind an indent or a marker. Exclusions and boundaries: the line-start prefix of `COMMENT`'s second arm against the block starts CommonMark reads. The masking's direction, this change's own axis: whether each statement says which way the closer errs.

## Findings

### 1. The closer's comment says the four-space opener is the one opener `COMMENT` masks that GitHub does not hide, and its own Limits paragraph names another

```seal
severity: should
location: `.github/scripts/close_issues_on_release.py:127-131`, `.github/scripts/close_issues_on_release.py:154-168`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/frame/design.md:73`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/frame/plan.md:60`
evidence: executed `bin/test tests/github/test_tmp_round3_probe.py -s -q -p no:xdist -p no:cacheprovider` (a probe, deleted); read `.github/scripts/close_issues_on_release.py:127-171`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/frame/design.md:12`
regression: round-2
```

The unit is the comment paragraph at `.github/scripts/close_issues_on_release.py:127-131`, which `a2e829ed` rewrote. The frame's Scope 1 at `frame/design.md:33` asks that paragraph to state #1408 to #1410, and calls the four-space shape "a limit". The fix wrote that it is "the one opener masked here that GitHub does not hide". The word "one" came from the fix, not the frame.

Why it matters: the claim is false by the same comment block. Its Limits paragraph at `:162-163` says "A marker without its space, such as `-<!--`, counts as a line start". That paragraph files the shape under "Each but the last masks more than GitHub". CommonMark reads no list item in `-<!-- note`, because a list marker needs a space or a tab after it. So text stands before the opener, and #1404 measured that GitHub reads on after such an opener (`frame/design.md:12`). The probe read `Control: Closes #1401`, then `-<!-- note`, a blank line and `Closes #103` through `keywords_in`. It returned `['1401']`, so `COMMENT` masks there.

The class is wider than the two shapes the comment names. It is built from the parts of `COMMENT`'s second-arm prefix (`:171`) that CommonMark reads as no HTML block start:

- Four or more spaces at the line's start. This is #1410's shape, named at `:156-157`.
- A tab at the line's start, named at `:159-160` as unmeasured.
- A marker without its space, named at `:162-163`.
- A list or quote marker followed by five spaces or more, such as `-     <!-- note`. CommonMark reads it as a list item or a quote whose content is an indented code block, so the opener is text. The probe read that body as `['1401']` too, and no Limits sentence names the shape.

Each member closes fewer, the direction #266 allows. So the defect is the sentence, not the masking. An agent that edits the closer reads the comment block as the list of shapes the closer gets wrong. Told the four-space shape is the one, it can drop or skip the others. That sentence is the frame's chosen mechanism here, "Limits, as sentences in the comment at the patterns, with no guard" (`frame/design.md:72`).

At `.github/scripts/close_issues_on_release.py:127-131`:

```python
# on the next line is read (#1404). Behind a list marker or a block quote
# marker, a `<!--` that no `-->` follows hides everything below it too, past
# the end of its list item or its quote (#1408, #1409). Indented four spaces
# it is an indented code block, and a keyword after it is read (#1410), so
# the mask there runs past GitHub's: it is one of the Limits below.
```

At `.github/scripts/close_issues_on_release.py:156-160`, the first Limits sentence, with `:161` following unchanged:

```python
# which is loud. A `<!--` that no `-->` follows, indented four spaces or more,
# or after a list or quote marker and five spaces or more, as in
# `-     <!--`, hides to the end of the text, where GitHub reads on (#1410).
# Telling such an indent from a bullet's continuation, which this
# repository's bodies write the same way, would mean modelling CommonMark's
# containers; a tab indent is unmeasured and read the same. A `<!--` in the
# middle of a line with a `-->`
```

The snippets cover the closer's comment. They leave two frame statements, which are the orchestrator's:

- The first Limits bullet at `frame/design.md:73`, which names the four-space shape and not the marker followed by five spaces.
- Row A2 at `frame/plan.md:60`, "Its gain over A is the four-space shape alone (#1410)". A container model would also read `-<!--` and a marker followed by five spaces as GitHub does, so "alone" states the same false "one".

## Confirmations

No finding of round 2 was closed, so no `confirms:` line is owed.

What matched: every line the fix diff changes in a code file is a comment or a docstring. The probe parsed each of the four Python files at `bc5dfb15` and at `7aea41cd` and replaced each docstring with `pass`. The trees were equal for `.github/scripts/close_issues_on_release.py`, `skills/code-review/scripts/pr_body.py`, `tests/github/test_close_issues_on_release.py` and `tests/skills/test_pr_body.py`. The texts differ (executed, below). The diff also shows each changed line under a `#` or inside the module docstring at `pr_body.py:61-83` and the test docstring at `tests/skills/test_pr_body.py:476-480` (read).

What matched: `keywords_in` agrees with the three measurements in the direction the statements give. The probe used each body as `gh pr view` returned it (executed, below). #1408's body read `['1401']`, and GitHub read `[1401]`. #1409's body read `['1401']`, and GitHub read `[1401]`. #1410's body read `['1401']`, and GitHub read `[103, 1401]`. So the closer equals GitHub behind a list marker and a quote marker, and masks more in the four-space shape. `issue_claims_check.read` returned `(['1401'], [], [])` for each body. Each statement in the diff says that, apart from the "one opener" of finding 1. Those statements are the closer's comment at `close_issues_on_release.py:127-131` and `:154-160`, the Limits bullet at `pr_body.py:75-79`, the test comment at `tests/github/test_close_issues_on_release.py:459-461`, the test docstring at `tests/skills/test_pr_body.py:480` and `changelog.md:3`. In the frame they are `frame/design.md:15`, `:33`, `:60`, `:73` and `:109-112`, and `frame/plan.md:42-44`, `:58`, `:60` and `:61` (read). #1410's body holds a blank line above the indented line, so GitHub reads it as an indented code block, as `close_issues_on_release.py:130` and `frame/design.md:73` say.

What matched: the crafter's judgment that the four-space shape owes no behaviour change holds. The frame's direction allows a mask wider than GitHub's: the closer closes fewer, and the completeness check refuses the release loudly (`frame/design.md:72`, `close_issues_on_release.py:154-156`). R26 reports and never fails a pull request (`.github/scripts/issue_claims_check.py:27-29`, read). `seal pr-body` refuses the line, and its message names the repair, a code span (`pr_body.py:655-658`, read). The cheaper change would cap the indent before `<!--` at three spaces. That change errs the other way in a bullet's continuation. Take `- item`, a blank line, then `    <!-- note`. CommonMark places the indented line inside the list item as the start of an HTML block, the shape #1408 measured hidden. A capped prefix would read a keyword below it that GitHub likely hides, and close an issue GitHub does not. The comment at `close_issues_on_release.py:157-160` names that trade, and row A2 at `frame/plan.md:60` rejects the container model that would tell the two apart. The probe read the bullet's continuation as `['1401']` (executed, below).

What matched: the `gaps.md` *Not verified* row is closed in place, not removed. Its Item cell now opens with `closed`, and its second cell names #1408 to #1410 with what each read. That matches the `gh pr view` output below.

Two statements generalise past the measured body. Neither is wrong where the closer acts, so the round opens no finding on them. `pr_body.py:76-77` says GitHub reads a copied line four spaces in as an indented code block and shows the lines after it. Behind a bullet, CommonMark reads that line as an HTML block in the item, and the refusal holds there too. S4's row `- <!-- note\nCloses #4` at `frame/design.md:60` and the test comment at `tests/github/test_close_issues_on_release.py:459-461` cite #1408. #1408's body had a blank line below the opener, and the row has none. CommonMark ends the HTML block where the item ends in both, and in both the unclosed opener reaches GitHub's output as raw HTML.

The crafter's narrow run, 315 passed over eight modules, names no module list, so it was read as a claim and not re-run as stated. The round ran the seven modules of the plan's phase row: 287 passed, round 2's count, as a diff of comments alone gives.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether GitHub hides the lines below a bullet's continuation `    <!-- note` placed after `- item` and a blank line, the shape that grounds keeping the four-space mask. CommonMark makes it an HTML block in the item. No throwaway pull request measured it | `.github/scripts/close_issues_on_release.py:157-160` | the orchestrator, from a throwaway pull request into `main`, if it judges the trade worth a measurement |
| The full suite, the repository-wide lint and the format check at `7aea41cd`: `unverified` | `seal/config.md`, the `Broad gate` row | the orchestrator, through its broad run after the fix pass for finding 1 |

## Probes

| Command | Result |
|---|---|
| `gh pr view <n> -R MichaelYcJo/SpecSeal --json number,state,baseRefName,body,closingIssuesReferences,mergedAt` for 1408, 1409 and 1410 | Each is `CLOSED` into `main`, unmerged. #1408 holds `- a list item` with a mid-line opener, `- ` then an opener, a blank line, `Closes #103`, a quote opener and `Closes #1376`, and names 1401 alone. #1409 holds `> ` then an opener, a blank line and `Closes #103`, and names 1401. #1410 holds a blank line, four spaces then an opener, a blank line and `Closes #103`, and names 103 and 1401 |
| `bin/test tests/github/test_tmp_round3_probe.py -s -q -p no:xdist -p no:cacheprovider`: the four changed Python files compared at `bc5dfb15` and `7aea41cd` with docstrings replaced, and `keywords_in` and `issue_claims_check.read` over seven bodies | Each file's tree is equal without docstrings and its text differs. #1408, #1409 and #1410 read `['1401']` and `(['1401'], [], [])`. So do `-<!-- note`, `-     <!-- note`, a tab then `<!-- note`, and `- item`, a blank line and four spaces then `<!-- note`, each followed by a blank line and `Closes #103`. Exit 0, deleted |
| `bin/test tests/github/test_close_issues_on_release.py tests/github/test_issue_claims_check.py tests/github/test_release_completeness_check.py tests/github/test_label_merged_on_release_branch.py tests/github/test_publish_release_note.py tests/skills/test_pr_body.py tests/behaviour/test_a_body_naming_two_issues_claims_one.py -q -p no:cacheprovider` at `7aea41cd` | 287 passed, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over the four changed Python files | exit 0 each |
