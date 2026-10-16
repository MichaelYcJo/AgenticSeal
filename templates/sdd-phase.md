# <work-item-id> — phase <N>

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | <the phase number, matching `plan.md`'s Phases table> |
| Commit | <the commit that closed this phase — the same hash `plan.md`'s Status cell for this phase carries> |


## What this phase was asked

<the phase-specific content of the spawn or task that started this phase —
never the boilerplate the contract, `skills/implement/SKILL.md`, and
`agents/smith.md` already carry>

<!-- #119: neither a round record nor a build phase said what it was ASKED to
do, only what it found. A reader opening this record later, with the spawn
prompt gone, had no way to tell a scope the orchestrator actually gave this
phase from a scope the phase invented for itself. -->

## What this phase found

<what building this phase taught that `plan.md`'s Delivers/Status cells do
not capture — a design decision settled while writing the code, a constraint
discovered only by trying, anything the next phase needs and would otherwise
reach it only if the orchestrator retyped it into the next spawn prompt>

<!-- #107, #121: what a phase discovers reaches the next phase only if the
orchestrator retypes it by hand into the next spawn prompt, and it goes
missing without a trace when the orchestrator doesn't. This section is that
discovery's durable, committed home instead.

What a work item takes out of the tree is not recorded here. It is named
once, at the frame, in `spec.md`'s `## Removes` section, which the review
reads against the diff (#835). A
removal this phase made that the frame did not name is a divergence, and it
goes where divergences go: `overview.md`. -->
