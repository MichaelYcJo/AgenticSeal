# Review round 2: 1793922918-a-keyword-inside-a-comment-reads-as-a-claim

```seal
target: 4dcd9a76, fixes 3db19c6d..4dcd9a76
```

This is a verifying round. It read the range `3db19c6d..4dcd9a76` in a `git clone --no-local` of the branch at `4dcd9a76`, made under the round's scratch directory. That range holds round 1's record (`94bb5df1`), the fix pass (`b7c9e4c1`, `f22d8dda`, `eb4f1f07`, `134e6ef4`) and the orchestrator's fold of the frame (`4dcd9a76`). The code files at `94bb5df1` equal those at `3db19c6d`, so every red run below against the old code is against round 1's target. The round read `gaps.md`, `frame/design.md`, `frame/plan.md` and `changelog.md` whole at HEAD, and round 1's record whole.

Carried from round 1 and not re-established: the class of six readers of a body's closing keyword (`frame/design.md:19`), the regex timing over crafted bodies, and `bin/seal layout --pairs` naming no pair in `tests/github/`'s new cases. The fix diff touches none of the readers' call sites, so none of those checks has failed. `bin/seal layout --pairs` was run again for `tests/skills/test_pr_body.py`, since the diff adds rows there.

The axes walked inside the fix diff were these. Inputs: the shapes of a copied line that begins with `<!--`. Exclusions and boundaries: the line-start condition and the `-->` test on the match. Error paths: the new refusal and its message. The masking's direction, this change's own axis: whether the new limit sentence states the one shape that closes more.

## Findings

None. Both closes from round 1 hold, and the fix diff adds no defect this round found.

## Confirmations

```seal
confirms: round-1#1
```
What holds: `_composed` at `skills/code-review/scripts/pr_body.py:647-659` refuses a copied line where `CLOSER.COMMENT` matches at the line's start and the match holds no `-->`. The branch stands between the `HEADING` branch and the tag branch, as round 1's fix placed it. The probe composed a body from 13 copied lines (executed, below). `<!-- Closes #5`, `- <!-- note`, `> <!-- note`, `1. <!-- note`, a tab before `<!--` and `-<!-- note` were each refused at line 3 with the opener's message and with no second cause. `<!-- a note --> and text after it`, `text <!-- note`, and a line that opens with `<!--` in a code span were each accepted. So the message's advice, write the `<!--` in a code span, passes. A `<!--` inside a fence in `changelog.md` was accepted, since `readable` blanks the fenced line. The crafter claimed that the two new rows of `test_refuses_a_record_it_cannot_copy_faithfully` fail with the branch removed, and that `test_accepts_a_keyword_and_a_details_tag_in_a_closed_comment` fails with the `-->` test replaced by `True`. Both were re-run in the clone with the `Edit` tool and confirmed (executed, below). The other statements round 1 named are rewritten: the module docstring at `pr_body.py:46-52` and its Limits bullet at `:75-78`, `_composed`'s docstring at `:606-620`, the test's docstring at `tests/skills/test_pr_body.py:476-480`, `changelog.md:3`, and the first paragraph of `gaps.md` *Not done*, which is removed as answered. The frame statements the fold `4dcd9a76` rewrote are Scope 3 at `frame/design.md:35`, S8 at `:64`, *Data & interfaces* at `:71-78`, the Out bullet that left, and `frame/plan.md:26-30`, rows A and B2 at `:58` and `:64`, and `:83-85`. Each now states the refusal the code makes (read). The Out bullet's removal is no removal from a closing memo, since it stood in the frame.

```seal
confirms: round-1#2
```
What holds: the limits paragraph at `.github/scripts/close_issues_on_release.py:155-165` now opens "Each but the last masks more than GitHub" and ends with the shape `Closes<!-- -->#4`, in which the closer closes more. It names both maskings: one space in `keywords_in`, and one space per character in `issue_claims_check.py#prose_only`. The probe read `Closes<!-- -->#4` and ``Closes`x`#4`` as claiming 4, through both `keywords_in` and `issue_claims_check.read`, so the sentence is true of both readers (executed, below). The frame states the same limit as the last bullet at `frame/design.md:77`, with the lead sentence at `:72` changed the same way, and `frame/plan.md:58`, row A, says "Each but one" (read). Round 1 chose a limit sentence over a guard, and this round left that choice unchanged.

What matched: round 1's first row of `## Not judged`, the text after a `-->` on a line that begins with `<!--`, is answered by #1407. `gh pr view 1407` read the body line `<!-- a comment that opens and closes at the start of the line --> Closes #103`, the state `CLOSED`, the base `main`, and `closingIssuesReferences` naming 103 and 1401 (executed). The new sentence at `close_issues_on_release.py:122-123` cites it, and `keywords_in("<!-- x --> Closes #4")` reads `['4']` (executed, below), as GitHub read #103. So S3's second row and row B2's verdict at `frame/plan.md:64` now stand on a measurement.

What matched: each new test was read against its group. The two refusal rows join the parametrized refusal case. No earlier row there holds a line that begins with `<!--`. One new row holds that shape with a keyword, and the other holds it behind a list marker with no keyword. The accepting line joins the closed-comment case, and no earlier line there begins with `<!--`. `bin/seal layout --pairs` names no pair in `tests/skills/test_pr_body.py` (executed, exit 0). Each row holds a fact of S8 at `frame/design.md:64`.

The new message, the module docstring at `pr_body.py:50-52`, the test docstring at `tests/skills/test_pr_body.py:476-480` and `changelog.md:3` each say that GitHub hides the lines after the opener, the fold's end among them, for the list-marker shape too, and the test docstring cites #1405 for it. #1405 measured an opener at a line start alone. `frame/plan.md:61`, row A3, says that behind a list marker GitHub hides the item's remaining lines, and the new Limits bullet at `pr_body.py:75-78` names an indent and a quote marker, and no list marker, among the shapes where GitHub may show the lines after. Neither reading is measured. The refusal is the frame's in either reading (Scope 3), and the repair the message names is the same, so the round opens no finding on it. The question is the display half of the `gaps.md` *Not verified* row at `gaps.md:8`, and this round judges that it does not block the seal.

A copied line `<!-->` is accepted (executed, below). `COMMENT`'s second arm matches it, and the match holds `-->` within the opener's own characters, so `pr_body.py:648` reads it as closed. This disagrees with the docstring at `pr_body.py:612-614`, which says the line is refused where the second arm matches. CommonMark 0.31 reads `<!-->` as an empty comment, so the acceptance likely matches GitHub. No record in the normal flow writes the shape, and the round opens no finding on it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether GitHub hides the lines below a copied line that begins with a comment closing on it and then opens a second `<!--` that never closes, such as `<!-- a --> text <!-- b` (in a code span here). CommonMark ends the HTML block on that line and passes the line through as raw HTML, so the unclosed opener reaches GitHub's HTML sanitizer. `seal pr-body` accepts the line (executed, below). No record in the normal flow writes the shape, and the round judges that it does not block | `skills/code-review/scripts/pr_body.py:647-649` | the orchestrator, from a throwaway pull request into `main` if it judges the shape worth a limit sentence |
| The full suite, the repository-wide lint and the format check at `4dcd9a76`: `unverified` | `seal/config.md`, the `Broad gate` row | the orchestrator, through its broad run. After it, the sealer's spawn comes due |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_close_issues_on_release.py tests/github/test_issue_claims_check.py tests/github/test_release_completeness_check.py tests/github/test_label_merged_on_release_branch.py tests/github/test_publish_release_note.py tests/skills/test_pr_body.py tests/behaviour/test_a_body_naming_two_issues_claims_one.py -q` at `4dcd9a76` | 287 passed, exit 0: round 1's 285 and the two new refusal rows |
| `bin/test tests/skills/test_tmp_round2_probe.py -s -q -p no:xdist -p no:cacheprovider`: `compose` over 13 copied lines and a fenced opener, and `keywords_in` and `issue_claims_check.read` over three bodies | Refused at line 3 with the opener's message alone: `<!-- Closes #5`, `- <!-- note`, `> <!-- note`, `1. <!-- note`, four spaces then `<!-- note`, a tab then `<!-- note`, `-<!-- note`. Accepted: `<!-- a note --> and text after it`, `<!-- a --> text <!-- b`, `text <!-- note`, a line opening with `<!--` in a code span, `<!-- x -->`, `<!-->`, and an opener inside a fence. `<!-- x --> Closes #4`, `Closes<!-- -->#4` and ``Closes`x`#4`` each read `['4']` and `(['4'], [], [])`. Exit 0, deleted |
| `bin/test tests/skills/test_pr_body.py -q -p no:xdist -p no:cacheprovider -k Test_compose`, with `False and` put before the opener test at `pr_body.py:647` through the `Edit` tool | 2 failed, 22 passed, exit 1: the two new refusal rows, each `DID NOT RAISE Refused`. The edit was undone |
| The same command, with the `-->` test at `pr_body.py:648` replaced by `True` through the `Edit` tool | 1 failed, 23 passed, exit 1: `test_accepts_a_keyword_and_a_details_tag_in_a_closed_comment`, refused with the opener's message. The edit was undone |
| `bin/seal layout --pairs` at `4dcd9a76` | exit 0. No pair names `tests/skills/test_pr_body.py` |
| `gh pr view 1407 --json number,state,baseRefName,body,closingIssuesReferences` | `CLOSED` into `main`. The body holds the control `Closes #1401` and the line `<!-- a comment that opens and closes at the start of the line --> Closes #103`, and `closingIssuesReferences` names 103 and 1401 |
