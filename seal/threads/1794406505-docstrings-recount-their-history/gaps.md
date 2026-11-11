# Closing memo: 1794406505-docstrings-recount-their-history

## Not verified

| Item | Who must answer |
|---|---|
| the suite, the repository-wide lint and the format check beyond the boundary sets of phases 1 to 5 | the orchestrator's broad gate |

## Not done

Phase 1 left `skills/verify/scripts/session_cost.py`'s two statements of
how long a subagent runs side by side. `DELEGATING`'s comment and
`spawn_cycles`' docstring say "a median of about 1,000 seconds" over 67
spawns of three runs, and `measure_segments`' docstring says that over 433
segment rows the median is 716 s and 1,000 is the mean. Which the first
figure is cannot be read from the tree, and settling it means re-reading
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

Phase 5 also left two statements outside this work's files that its edits
made untrue or that were already untrue. Design *Scope* names the `.py`
files under `.github/scripts/` and leaves out `.github/workflows/` and the
comments of `tests/`, which #1489 rewrites.

- `.github/workflows/hygiene.yml`, the comment over the claims step, says
  `close_issues_on_release.py`'s comment stands "two lines above its
  regex". That comment stands over `KEYWORDS`, and its last line is twelve
  lines above `CLOSING`. The same comment also tells the `Closes #153 and #150`
  incident by pull request and release number, which this phase removed
  from `issue_claims_check.py`.
- `tests/github/test_label_merged_on_release_branch.py`, the comment over
  the second assert of `Test_module`'s
  `test_the_label_reader_has_one_source`, says the sibling's docstring "says in
  prose that it used to unpack `closer._issue_api` here and now delegates".
  `label_merged_on_release_branch.py#issue_labels` no longer says it used
  to unpack anything. The assert itself, `"_issue_api(" not in source`,
  still holds and pins the call, not the sentence.
