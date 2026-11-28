# Design: 1795860048-what-iadd-claims

## Grounding

The tree as read at `5c18f931`.

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md`, its opening paragraph | the core governs work run through the IADD process, and a session doing other work is not bound by it |
| `skills/implement/routing-question.md` *Question 1, the mode* | the answer `direct` names every party and record that does not run |
| `skills/implement/orchestration.md` *Under agentic* | the orchestrator that takes `direct` under `agentic` writes one sentence of grounds into the commit |
| `docs/checks/the-routing-check.md` *At the pull request* | a commit of no work item carries `IADD-Routing: no work item`, and the check prints it |
| `docs/forms/the-inspection.md` *The inspection* | an inspection and its mark stand on a work item |
| `docs/method/iadd.md` *The principles* | each principle names the file that states it, and that file is the rule |

## Scope

In: one principle at the head of `docs/method/iadd.md` *The principles*. It says IADD claims only the work run through the IADD process, the plugin may offer a route outside it, and the route is shown where the person chooses it, on the commit, in the pull request's check, and by the inspection's absence. Each of its sentences points to the file above that holds the rule.

Out: any change to the files it cites. They already hold each rule.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | Given a reader of the definition, when they ask where IADD's claims stop, then one principle answers and names the file that holds each part | read |
| S2 | Given the principle, when a suite compares the definition with the documents it cites, then no passage is copied from them | `tests/text/test_no_passage_is_pasted_into_a_second_file.py` |

## Data & interfaces

None.

## Rule changes

- nothing
  why: `docs/method/iadd.md` governs nothing itself, and every rule the principle names stands in the file it cites

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| nothing | | the work adds one principle that points to existing rules |

Framed 2026-11-28 by the session, before the build.
