# Review round 6: 1793922918-a-keyword-inside-a-comment-reads-as-a-claim

```seal
target: d44cbfa8, fixes f26036aa..d44cbfa8
```

This is a verifying round. It read the range `f26036aa..d44cbfa8` in the branch worktree with `git -C` and `git show`, and wrote nothing there but this record. The range holds two commits. `836ab34f` is the crafter's fix pass for round 5's finding 1, and it touches `.github/scripts/close_issues_on_release.py` and the work item's `changelog.md`. `d44cbfa8` is the orchestrator's fold of the same word into `frame/design.md` and `frame/plan.md`, and it adds the close block to `trail/rounds/round-5.md`. HEAD is `d44cbfa8` (executed, `git rev-parse HEAD`).

Carried from rounds 1 to 5 and not re-established: the class of six readers of a body's closing keyword (`frame/design.md:19`), the frame's probe over 300 merged bodies, `bin/seal layout --pairs` naming no pair among the new cases, and round 5's parser probe. That probe rendered `-<!-- note`, `*<!-- note`, `1.<!-- note`, `1)<!-- note` and `some text` followed by `2. <!-- note` as paragraph text in markdown-it (CommonMark mode) and in cmark-gfm, and `keywords_in` masked each. The range changes no code line and adds no case, so none of those checks has failed. No probe was needed: what the round judged is a word in six sentences, and reading the diff settles it.

The axes walked inside the fix diff were three. Scope of the diff: whether any line changed beyond the one word. The masking's direction: whether the reworded example still files each shape it names on the side GitHub's reading puts it. One reading of the rule's words, this change's own axis: whether "list marker" means what the frame and the closer's other sentences mean by it.

## Findings

None. The close of round 5's finding 1 holds, and the fix diff adds no defect this round found.

## Confirmations

```seal
confirms: round-5#1
```
What holds: each of the six statements on round 5's `location:` line now names a list marker, not a marker, as the one that opens no list item. They are `close_issues_on_release.py:158-161`, `changelog.md:3`, `frame/design.md:15`, `:33` and `:73`, and the Judgment cell of `frame/plan.md:91`. `git grep -n -E "marker that|that opens no"` over the tree at `d44cbfa8` lists the closer's `:159` and the five work item lines, each reading "list marker", and otherwise only round records and lines that state another fact (executed). The closer's sentence wraps across lines, so the round also joined the comment lines of the closer, `pr_body.py` and `issue_claims_check.py` and searched the joined text for "marker that opens". It found the closer's clause alone, reading "after a list marker that opens no list item" (executed). The work item's `gaps.md`, `trail/phases/` and `frame/questions.md` hold no statement of the clause (executed, the same `git grep`). `pr_body.py:75-79` cites the indented code block alone as its example and was right to stay unedited. The `to:` at `frame/design.md:108-113` stays unedited for the same reason.

The reworded example is true. In CommonMark a `<!--` opens an HTML block only where it starts a line of its container. Where a list marker character stands before the opener and opens no list item, that character is paragraph text before the opener, so no HTML block opens. GitHub then reads the opener as text and reads on, while `COMMENT`'s second arm (`close_issues_on_release.py:177`) treats the line as a line start and masks to the end of the text. That is the direction the sentence states: the closer closes fewer. Round 5's carried probe shows this for every list marker shape it ran. The quote marker is no longer taken in by the example's noun. The sentence beside it in each place still says GitHub hides behind a quote marker as the closer does (#1409), so the two no longer contradict each other (read, `close_issues_on_release.py:154-168`, `changelog.md:3`, `frame/design.md:15`, `:73`).

The claims in the close block were checked against the code. The close block claimed that the closer's Limits comment now reads "after a list marker that opens no list item", rewrapped as the paste-ready fix gives it. `close_issues_on_release.py:158-161` reads so, and the wrap matches round 5's snippet line for line (read). It claimed that every changed line in the closer is a comment. The hunk at `:156-161` changes four lines, each opening with `#` (read, `git diff f26036aa..d44cbfa8`). It claimed that `changelog.md` carries the same words, and it does (read). It claimed that `836ab34f` left the four frame lines for the orchestrator. `git show --stat 836ab34f` lists the closer and `changelog.md` alone, and `d44cbfa8` makes the frame edits (executed). The `fixed` commit touches two paths on the finding's `location:` line.

What matched, the range changes nothing else: `git diff --word-diff=porcelain f26036aa..d44cbfa8` lists the word "list" added six times, once in each of the six statements. It also lists the closer's rewrap, which moves `item,` to the next comment line and adds one `#` line holding `fewer.`, and the five lines of round 5's close block. It lists no other added or removed word (executed). The orchestrator's judgment at `frame/plan.md:91` still states the rule once, and the fold changed one word of its example and nothing of the rule.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `d44cbfa8`: `unverified` | `seal/config.md`, the `Broad gate` row | the orchestrator, through its broad run at `d44cbfa8`, which the spawn prompt says runs in parallel |

This round leaves nothing open. What comes due is the orchestrator's broad run at `d44cbfa8`, and the sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `git -C <worktree> rev-parse HEAD` | `d44cbfa8eea691d33d016e6e0a692bf216cf1a9d` |
| `git -C <worktree> diff --word-diff=porcelain f26036aa..d44cbfa8`, added and removed words only | Six additions of `list`, the closer's rewrap (`item,` moved, one `#` line added), and round 5's close block. No other word changed |
| `git -C <worktree> grep -n -E "marker that\|that opens no" d44cbfa8` over the work item's `gaps.md`, `trail/phases/`, `frame/questions.md`, and `docs`, `skills`, `tests` and `.github` | The closer's `:159` reading "list marker", and lines that state other facts: `issue_claims_check.py:126`, `skills/code-review/orchestration.md:122` and `:126`, `unverified_check.py:332`, and four test lines. None states the clause |
| `git -C <worktree> grep -n "opens no list item" d44cbfa8` | `changelog.md:3`, `frame/design.md:15`, `:33` and `:73` and `frame/plan.md:91`, each reading "list marker", and round 4's and round 5's records |
| The comment lines of the closer, `pr_body.py` and `issue_claims_check.py` at `d44cbfa8`, joined and searched for "marker that opens" | One match, the closer's "after a list marker that opens no list item" |
| `git -C <worktree> show --stat 836ab34f d44cbfa8` | `836ab34f`: the closer and `changelog.md`. `d44cbfa8`: `frame/design.md`, `frame/plan.md` and `trail/rounds/round-5.md` |
