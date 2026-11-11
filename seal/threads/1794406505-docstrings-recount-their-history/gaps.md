# Closing memo: 1794406505-docstrings-recount-their-history

## Not verified

| Item | Who must answer |
|---|---|
| the suite, the repository-wide lint and the format check beyond the boundary sets of phases 1 and 2 | the orchestrator's broad gate |

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
