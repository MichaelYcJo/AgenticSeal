# Closing memo: 1793922918-a-keyword-inside-a-comment-reads-as-a-claim

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the branch's head. Phase 1 ran the seven modules its plan row names and the modules that read a path it changed, not the suite | the orchestrator, through the `Broad gate` row of `seal/config.md` |
| GitHub's reading of a `<!--` that never closes behind a list marker, a block quote marker or an indent, with a keyword after the list item or the quote has ended. No throwaway pull request measured it. `close_issues_on_release.py#COMMENT` masks it to the end of the body, which closes fewer, as `frame/design.md` *Data & interfaces* states | the orchestrator, from a throwaway pull request into `main` read through `closingIssuesReferences`, as for #1402 to #1405 |

## Not done

A copied record line that begins with a `<!--` that never closes is not refused by `seal pr-body`. `skills/code-review/scripts/pr_body.py#_composed` copies record lines into the pull request body below `HEADING`, and #1405 shows that GitHub hides everything after such a line, so the rest of the records' copy and the fold's end would not show. Round records and `trail/gate.md` refuse such a line through `hooks/lib/fields.py` (`COMMENT_LINE`), and `pr_body.py` calls no `comment_lines`, so a `changelog.md`, `gaps.md` or `questions.md` line beginning `<!--` reaches the body unrefused. `frame/design.md` *Scope*, Out, leaves it out: this branch did not cause it, and #1181 does not name it.

`tests/github/test_label_merged_on_release_branch.py#test_the_readers_come_from_the_closer_rather_than_a_second_copy` refuses the labeler's own `CLOSING`, `FENCE` and `SPAN` and does not name `COMMENT` or `HIDDEN`. The labeler reads every body through `closer.keywords_in`, and its source compiles neither name, so the case stays true. Widening it is a change to a case the frame does not name.
