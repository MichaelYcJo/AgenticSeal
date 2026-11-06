# Closing memo: 1793922918-a-keyword-inside-a-comment-reads-as-a-claim

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the branch's head. Phase 1 ran the seven modules its plan row names and the modules that read a path it changed, not the suite | the orchestrator, through the `Broad gate` row of `seal/config.md` |
| closed GitHub's reading of a `<!--` that never closes behind a list marker, a block quote marker or an indent, with a keyword after the list item or the quote has ended. No throwaway pull request measured it. `close_issues_on_release.py#COMMENT` masks it to the end of the body, which closes fewer, as `frame/design.md` *Data & interfaces* states | throwaway pull requests #1408, #1409 and #1410 into `main`, read by the orchestrator through `closingIssuesReferences` and closed unmerged: a list marker read `[1401]` and a quote marker read `[1401]`, so GitHub hides the `Closes #103` after each container, as `COMMENT` does; four spaces read `[103, 1401]`, so GitHub reads on where `COMMENT` masks. `frame/design.md` *Data & interfaces* states the four-space shape as a limit |

## Not done

`tests/github/test_label_merged_on_release_branch.py#test_the_readers_come_from_the_closer_rather_than_a_second_copy` refuses the labeler's own `CLOSING`, `FENCE` and `SPAN` and does not name `COMMENT` or `HIDDEN`. The labeler reads every body through `closer.keywords_in`, and its source compiles neither name, so the case stays true. Widening it is a change to a case the frame does not name.
