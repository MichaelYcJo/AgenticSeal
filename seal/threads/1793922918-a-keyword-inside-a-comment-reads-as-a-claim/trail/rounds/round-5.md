# Review round 5: 1793922918-a-keyword-inside-a-comment-reads-as-a-claim

```seal
target: b154d288, fixes e70adbe6..b154d288
```

This is a verifying round. It read the range `e70adbe6..b154d288` in a `git clone --no-local` of the branch at `b154d288`, made under the round's scratch directory. The range holds three commits. `52c841f4` records the orchestrator's judgment in `frame/plan.md` *Judgments of the run*. `aceeed37` is the crafter's fix pass for round 4's finding 1. `b154d288` is the orchestrator's fold of the frame and the close block. The round read the closer's comment block whole (`.github/scripts/close_issues_on_release.py:103-178`), `pr_body.py`'s module docstring (`skills/code-review/scripts/pr_body.py:2-89`), `frame/design.md` and `frame/plan.md` whole, `changelog.md`, `gaps.md`, `routing.md` and rounds 1 to 4.

Carried from rounds 1 to 4 and not re-established: the class of six readers of a body's closing keyword (`frame/design.md:19`), the regex timing over crafted bodies, the frame's probe over 300 merged bodies, and `bin/seal layout --pairs` naming no pair among the new cases. The fix diff changes no code syntax tree and adds no case, so none of those checks has failed. Round 4's parser probe was written again for the marker shapes this round weighs, as `## Probes` shows.

The implementer's account was checked claim by claim. The crafter claimed no behaviour change; the closer's syntax tree is equal at `e70adbe6` and `b154d288`, and `pr_body.py`'s is equal once its docstrings are blanked (executed). The crafter claimed 287 passed over the plan row's seven modules; the round re-ran them in the clone and 287 passed, exit 0 (executed). The crafter claimed ruff clean; `ruff check` and `ruff format --check` over the two changed `.py` files each exited 0 (executed). That is a run over two files and not the repository-wide lint, which stays the orchestrator's.

The axes walked inside the fix diff were four. Inputs: the four measured bodies #1404 and #1408 to #1410 as `gh pr view` returns them, and ten marker shapes. Exclusions and boundaries: the prefix of `COMMENT`'s second arm (`close_issues_on_release.py:176`) against the block starts CommonMark reads. The masking's direction: whether each statement files each measured shape on the side GitHub's reading puts it. One reading of the rule's words, this change's own axis: whether each noun of the rule's examples means what the frame defines it to mean.

## Findings

### 1. The rule's example "after a marker that opens no list item" takes in the quote marker, which the frame lists as a block marker and behind which GitHub hides (#1409)

```seal
severity: should
location: `.github/scripts/close_issues_on_release.py:159`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/changelog.md:3`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/frame/design.md:15`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/frame/design.md:33`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/frame/design.md:73`, `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/frame/plan.md:91`
evidence: executed `uv run --no-project --with markdown-it-py --with cmarkgfm python test_tmp_round5_probe.py` in the clone (a probe, deleted) and `gh pr view 1409 --json body,closingIssuesReferences`; read `seal/threads/1793922918-a-keyword-inside-a-comment-reads-as-a-claim/frame/design.md:31`, `.github/scripts/close_issues_on_release.py:154-168`
regression: round-4#1
```

The unit is the second example of the rule stated once: "after a marker that opens no list item". `aceeed37` wrote it at `close_issues_on_release.py:159` and in the `changelog.md` sentence, and `52c841f4` and `b154d288` wrote it at `frame/plan.md:91` and `frame/design.md:15`, `:33` and `:73`. The judgment at `frame/plan.md:91` says to state the rule once and cite the measured shapes as examples; the fix states the rule as a true conditional, and the defect comes from the noun of one example, "a marker", which `frame/design.md:31` defines to include the quote marker.

Why it matters: Scope 1 at `frame/design.md:31` lists the block markers as "`>`, `-`, `*`, `+`, or a number with `.` or `)`". Of those, `>` never opens a list item. So read with the term as the frame defines it, the clause says GitHub reads on past an opener after `>`. #1409 measured `> <!-- an opener that never closes, inside a block quote` with `Closes #103` below it, and `closingIssuesReferences` named #1401 alone: GitHub hides there, as the closer does. The probe rendered `><!-- note` and `> <!-- note` with markdown-it in CommonMark mode and with cmark-gfm, and both parsers gave the same output for the two, a quote holding an HTML block. So the clause's literal reading files #1409's own shape on the wrong side, which is the defect round 4's finding named, now through a new word.

Whether a reader recovers the meant reading differs by place:

- `close_issues_on_release.py:159`, `frame/design.md:15` and `:73`: the next sentence says GitHub hides behind a quote marker as the closer does, so a reader settles the clause by the contradiction.
- `frame/design.md:33` and `frame/plan.md:91`: no sentence near the clause says what GitHub does behind a quote marker, and `:31`, two lines above `:33`, is the definition that takes `>` in.
- `changelog.md:3`: the sentence just before names "a list marker or a quote marker", so "a marker that opens no list item" picks out the quote marker most directly of the two, and the two sentences then contradict each other.

The frame is text the sealer and the settle read and act on, and `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* asks that a term the work defines be used only in its defined sense. The changelog sentence goes into the release note.

The fix is one word in each place, and it re-grows no list: "a list marker that opens no list item". It names every shape where a list marker character stands before the opener and CommonMark opens no item: the probe rendered `-<!-- note`, `*<!-- note`, `1.<!-- note`, `1)<!-- note` and `some text` followed by `2. <!-- note` each as paragraph text, where GitHub reads on (#1404's reading of text before an opener), and `keywords_in` masked each. It leaves out `>`, whose shapes stay under the measured sentence on #1409.

```text
.github/scripts/close_issues_on_release.py:158-160, rewrapped:
# GitHub read on past an opener the test treats as a line start, such as an
# opener in an indented code block or after a list marker that opens no list
# item, it masks to the end of the text all the same, and the closer closes
# fewer.

changelog.md:3:
Where CommonMark's block rules make GitHub read on past such an opener
instead, as in an indented code block (#1410) or after a list marker that
opens no list item, the closer masks more.

frame/design.md:15, :33 and :73, the same words in each:
such as an opener in an indented code block or after a list marker that opens
no list item,

frame/plan.md:91, the Judgment cell:
such as an indented code block or a list marker that opens no list item,
```

The snippet covers every statement of the clause: `git grep -n "opens no list item"` over the tree at `b154d288` lists these six lines and one more, round 4's close block at `trail/rounds/round-4.md`, which records what the fix did and states nothing a reader acts on (executed). `pr_body.py:75-79` states the rule with the indented code block alone as its example and needs no edit. The `to:` text at `frame/design.md:108-113` cites the indented code block alone and needs none.

## Confirmations

```seal
confirms: round-4#1
```
What holds: the sentence that filed every marker with no space as masked past GitHub is gone from each statement round 4's `location:` named. The closer's Limits paragraph (`close_issues_on_release.py:154-178`) no longer holds "A marker without its space"; `frame/design.md` no longer has the bullet at the old `:75`; `frame/plan.md`'s rows A and A2 (`:58`, `:60`) and the failure scenario (`:42-52`) name no marker shape; and the `changelog.md` sentence no longer says "after a marker with no space". `git grep -n -i -E "five spaces|no space|without its space|four spaces or more"` over `.github/scripts/close_issues_on_release.py`, `skills/code-review/scripts/pr_body.py` and the work item's `changelog.md`, `frame/` and `gaps.md` lists one line, the Grounds cell of `frame/plan.md:91`, which names round 4's finding as the judgment's grounds and states no shape as a limit (executed). The close's `location:` line names `pr_body.py:75-79`, which `aceeed37` rewrote in the same form. The close holds. The new example's wording is finding 1, which the fix's rewording made.

What matched, question 1 of the spawn prompt: no statement in the code comments, `changelog.md` or the frame lists the line-start test's shapes one by one. Seven statements state the rule once: the closer's Limits paragraph, `pr_body.py`'s Limits bullet at `:75-79`, the `changelog.md` sentence, `frame/design.md:15`, `:33`, `:73` and the `to:` at `:108-113`. Each cites the measured pull requests as examples and files each on the side its measurement gives. #1404 is read on by GitHub and by the closer, and #1408 and #1409 are hidden by both. #1410 is read on by GitHub and masked by the closer. `close_issues_on_release.py:130-131` points to the Limits, and the Limits state the indented code block, so the two agree. `frame/plan.md`'s rows A and A2 and its failure scenario name the indented code block (#1410) as the example. `gaps.md:8`'s last sentence, that *Data & interfaces* "states the four-space shape as a limit", stays true: `frame/design.md:73` cites it as one example of the limit. Apart from finding 1, no two of these statements contradict each other (read).

What matched, question 2: the rule is true of `COMMENT` on the measured bodies. `keywords_in` over each body as `gh pr view` returns it read #1404 as `[1247, 1401]`, #1408 as `[1401]` and #1409 as `[1401]`, each equal to its `closingIssuesReferences`. It read #1410 as `[1401]` where GitHub named `[103, 1401]`, which is the stated direction: GitHub reads on past an opener in an indented code block, the test treats the line as a line start, and the closer closes fewer (executed). The rule's conditional holds for every shape the probe ran: `keywords_in` masked all ten. Where the parsers read the opener as text or code, the closer masks more. Where they read an HTML block, GitHub hides as the closer does, per #1408 and #1409.

What matched, question 3: every changed line in the two `.py` files is a comment or a docstring line. The closer's syntax tree at `e70adbe6` equals its tree at `b154d288`. `pr_body.py`'s trees differ only in a docstring: they are equal with every docstring blanked, and the one hunk is in the module docstring's Limits bullet (executed).

What matched, the judgment at `frame/plan.md:91`, weighed against `skills/core/SKILL.md`: it holds. *The rule a mechanism is kept against* says that when fixes chase one mechanism's edge cases, the right question is what the mechanism decides. Rounds 3 and 4 each found a list the previous fix pass had grown. The shapes where CommonMark's block rules part from a one-line test have no end short of the block model row A2 rejects. `skills/code-review/SKILL.md` *A finding is not closed too early* says an enumeration over such a domain narrows a finding and does not close it, and sends the limit to a stated limit. A rule stated once is one source, and it has no list for the next case to contradict. The row carries its date, its grounds and the document it was judged against, as *A judgment stands on a source document, and is written down with both* asks. Finding 1 does not reopen the enumeration. It changes the noun of one example so that the example names no shape the measured sentence beside it contradicts.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `b154d288`: `unverified` | `seal/config.md`, the `Broad gate` row | the orchestrator, through its broad run after this round settles |

GitHub's own reading of `><!--` with no space is not measured. Finding 1 does not rest on it: the clause, read with `frame/design.md:31`'s term, also takes in `> <!--`, #1409's measured shape.

## Probes

| Command | Result |
|---|---|
| `gh pr view <n> --repo MichaelYcJo/SpecSeal --json number,body,state,baseRefName,closingIssuesReferences` for #1404, #1408, #1409 and #1410, saved under the round's scratch directory | Each exit 0. All four are closed with base `main`. `closingIssuesReferences`: #1404 `[1247, 1401]`, #1408 `[1401]`, #1409 `[1401]`, #1410 `[103, 1401]` |
| `uv run --no-project --with markdown-it-py --with cmarkgfm python test_tmp_round5_probe.py` in the clone at `b154d288`: `keywords_in` over the four bodies, the syntax trees of the two `.py` files at `e70adbe6` and `b154d288`, and `keywords_in`, markdown-it (CommonMark mode) and cmark-gfm over `Closes #1401`, a blank line, a shape, a blank line and `Closes #103`, for ten shapes | Exit 0, deleted. `keywords_in` equals GitHub for #1404, #1408 and #1409, and reads `[1401]` against GitHub's `[103, 1401]` for #1410. The closer's trees are equal. `pr_body.py`'s trees differ, and are equal with docstrings blanked. `keywords_in` read `['1401']` for all ten shapes. `><!-- note` and `> <!-- note` each gave a quote holding the HTML block, the same output in both parsers. `-<!-- note`, `*<!-- note`, `1.<!-- note`, `1)<!-- note` and `some text` followed by `2. <!-- note` each gave a paragraph of escaped text. `- <!-- note` gave a list item holding the HTML block. `>     <!-- note` and `    <!-- note` gave a code block |
| `bin/test tests/github/test_close_issues_on_release.py tests/github/test_issue_claims_check.py tests/github/test_release_completeness_check.py tests/github/test_label_merged_on_release_branch.py tests/github/test_publish_release_note.py tests/skills/test_pr_body.py tests/behaviour/test_a_body_naming_two_issues_claims_one.py -q -p no:cacheprovider` in the clone at `b154d288` | 287 passed, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over `.github/scripts/close_issues_on_release.py` and `skills/code-review/scripts/pr_body.py` in the clone | Each exit 0 |
| `git grep -n "opens no list item"` and `git grep -n -i -E "five spaces\|no space\|without its space\|four spaces or more"` over the clone at `b154d288` | The first lists the six lines on finding 1's `location:` and round 4's close block. The second, over the closer, `pr_body.py` and the work item's `changelog.md`, `frame/` and `gaps.md`, lists the Grounds cell of `frame/plan.md:91` alone |
