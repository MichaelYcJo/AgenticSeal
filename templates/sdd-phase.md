# Phase <N>: <work-item-id>

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md holds what this
phase of the build did, written by the party that builds it when the phase
closes. It is the build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | <the phase number, matching `plan.md`'s Phases table> |
| Commit | <the commit that closed this phase, the same hash `plan.md`'s Status cell for this phase carries> |


## What this phase was asked

<the phase-specific content of the spawn or task that started this phase,
never the boilerplate the contract, `skills/implement/SKILL.md`, and
`agents/smith.md` already carry>

<!-- This section is how a reader opening this record later, with the spawn
prompt gone, tells a scope the orchestrator gave this phase from a scope the
phase invented for itself. -->

## What this phase found

<what building this phase taught that `plan.md`'s Delivers and Status cells
do not capture: a design decision settled while writing the code, a
constraint discovered only by trying, anything the next phase needs and would
otherwise reach only if the orchestrator retyped it into the next spawn
prompt>

<!-- What a phase discovers reaches the next phase only through this section
or through the orchestrator retyping it into the next spawn prompt, and the
second goes missing without a trace when the orchestrator does not. This
section is that discovery's durable, committed home.

What a work item takes out of the tree is not recorded here. It is named
once, at the frame, in `spec.md`'s `## Removes` section, which the review
reads against the diff. A removal this phase made that the frame did not name
is a divergence, and it goes where divergences go: `overview.md`. -->
