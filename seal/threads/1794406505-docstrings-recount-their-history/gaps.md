# Closing memo: 1794406505-docstrings-recount-their-history

## Not verified

| Item | Who must answer |
|---|---|
| the suite, the repository-wide lint and the format check beyond the boundary sets of phases 1 to 6 | the orchestrator's broad gate |

## Not done

Phase 1 left `skills/verify/scripts/session_cost.py`'s two statements of
how long a subagent runs side by side. `DELEGATING`'s comment and
`spawn_cycles`' docstring say "a median of about 1,000 seconds" over 67
spawns of three runs. `measure_segments`' docstring says that over the
segment rows of 43 runs the median is 716 s over the 381 named rows and
664 s over all 433, and that 1,000 is the mean. Which the first figure is
cannot be read from the tree, and settling it means re-reading
transcripts that live on one machine, which a prose-only phase does not do.
Both sentences are present-tense claims a reader can hold against each
other, so neither recounts history.

Phase 2 left four printed strings that carry an issue number as they are:
the `--preflight` help text of `skills/verify/scripts/broad_gate.py`
("(#638)") and the `NO_ROUND_BLOCK`, `NO_RUN_BLOCK` and `NO_VERDICT_BLOCK`
refusals of `skills/code-review/scripts/chain_check.py` ("since #1198").
Design *Scope* Out keeps string constants and printed messages out of this
work, because changing what a person reads at a terminal owes a pin by
contract rule 14, which the issue does not ask for. They are code to the
counting command, so they are in no count.

Phase 3 opened the `# RIDER:` comment over
`skills/implement/scripts/seal.py#other_worktrees` and left its fix
undone. The rider asks that, when the function is next opened, the
worktree list be filtered by common git directory, refusing a path that is
not a work tree. A `--separate-git-dir` clone otherwise gets a note naming
its git directory as another worktree. That fix changes code, which design
S1 and *Scope* item 1 rule out of this work, so the phase rewrote only the
rider's history and kept its instruction for the next change to the
function.

Phase 5 left four printed strings under `.github/scripts/` that carry an
issue number as they are: the two report headings and the argparse
description of `durations_union.py`, each "(#931)", and
`roll_flow_measurement_issue.py#empty_log_note`, "(#198)". Design *Scope*
Out keeps printed messages out of this work, for the reason phase 2's
paragraph above gives.

The comment over the claims step of `.github/workflows/hygiene.yml` still
tells the `Closes #153 and #150` incident by pull request and release
number, which phase 5 removed from `issue_claims_check.py`. Design *Scope*
Out leaves the history in `.github/workflows/*.yml` comments to an issue of
its own. Phase 6 corrected only that comment's clause on where
`close_issues_on_release.py`'s comment stands, and the comment over the
second assert of `tests/github/test_label_merged_on_release_branch.py`'s
`test_the_label_reader_has_one_source`, and the two docstrings of
`tests/lib/test_optin.py` that cited a rider on `repo_root`, as design
*Scope* item 10 asks.
