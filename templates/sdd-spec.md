# Feature Specification: <work item>

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md holds WHAT this work
delivers and how we'll know. The policy documents in docs/ outrank this file;
the framer cites them and does not restate them. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| | |

<!-- A clause of a pact held in another repository is cited in this table as
`pact:<name>/"<heading path>"@<hash>` (`docs/the-pact.md`), and `pact-check`,
run at the pact's repository, is what reads it. -->

## Scope

What is in, what is explicitly out.

## User scenarios & acceptance *(mandatory)*

One row per scenario: these become the review's stage-1 checklist and the
regression tests' skeleton.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| | | |

## Data & interfaces

Schema deltas, endpoints, payload shapes. Reference the code's coordinates,
don't duplicate them.

## Rule changes

<!-- The rules this work adds to, changes in or removes from the policy
     root, which `settle --apply` applies after the release. The grammar is
     `skills/settle/SKILL.md` *Rule changes*. A spec that changes no rule
     writes the no-change block:

     - nothing
       why: <the reason>
     -->

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| <a copy, a reader, a rule sentence, a test pin> | <the backticked path, then the heading in italics, or `path#unit` for a unit of code> | <the file or record that now owns it, or why nothing needs to> |

<!-- What this work item takes out of the tree, named once, here, before the
     build; the review reads each row against the diff. A work item that
     removes nothing writes the no-change block in place of the table, as
     `## Rule changes` does. The rule is `docs/the-reader-registry.md` *A
     frame names what its work removes*. A removal is recorded because a
     rule taken out of a file with no record of where it went is lost
     between two phases. A removal a phase makes that this section did not
     name is a divergence, and the party that builds the phase records it
     in `overview.md`. -->

## Open questions

Anything a planner must answer lives in questions.md, not inline: unanswered
questions buried in prose read as decided.

<!-- The line below is the frame's mark in the tree; `agents/framer.md` says
     why CI needs it. Whoever drew the frame fills in the date and `<who>`,
     which takes the two values the `Planning` row of `routing.md` takes,
     `framer` or `the session`; a mark that disagrees with that row is
     refused at the pull request rather than guessed at. The shape (verb,
     date, who, the moment) is the one `routing.md` and `plan.md` end with,
     which keeps three such lines from becoming three conventions.
     A reframe adds `Reframed <date> by <who>, after round <N>.` UNDER this
     line when the review chain sends the work item back to its framer. It is
     never in this template; only a reframe writes it. -->

Framed <date> by <who>, before the build.
