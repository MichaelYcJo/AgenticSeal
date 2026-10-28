# Overview: 1793169126-a-case-passes-before-the-pull-request-and-fails-on-it

## Why this work exists

Three cases passed on every run before pull request #1057 and failed on its `pull_request` run, because that event alone sets `GITHUB_HEAD_REF`; the conftest now removes every `GITHUB_` variable at import, so a case sees one environment under every event.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| A pin on the CONTRIBUTING sentence | `frame/design.md` *Scope*: "`CONTRIBUTING.md`'s paragraph ... gains one sentence", and names one new case, in `tests/test_conftest.py`; the paragraph's sentences are already pinned by `tests/text/test_the_suite_runs_with_gh_logged_out.py#test_contributing_says_the_suite_runs_logged_out` | that case gains one needle for the new sentence, seen red with the sentence deleted | contract rule 14: "a change to a message, a verdict or a rendered line is a change someone reads and acts on, and the test that pins the new text is what keeps the next edit from quietly taking it back"; the frame was silent on this pin |
| Phase 1 in one commit | `frame/plan.md` phase 1 *Delivers*: "One commit."; the phase took two, `8b8e85f6` (the sweep, its case and every removal) and `84668705` (the case asserts what its child was given) | two commits | the frame's ground for one commit is `CLAUDE.md`'s rule that the removals go in the commit that adds the sweep, and `8b8e85f6` holds both; `84668705` came after `seal mutate` showed the first case could pass with its probe's environment dropped (`trail/phases/phase-1.md`) |
| S3's run as evidence | `frame/design.md` S3: the exported run over `tests/skills/test_broad_gate.py` verifies that the gate child sees neither variable | S1's case is the evidence, and S3's green run is recorded as consistent with it | a coverage probe with the sweep broken leaves `tests/skills/test_broad_gate.py` green under the exported variables (executed, `seal mutate`), so that module's run cannot tell the sweep from its absence |

## Not verified

| Item | Who must answer |
|---|---|
| The broad gate over this branch: the full suite, the repository-wide lint and the typecheck | the orchestrator |
| `frame/questions.md` M1: the three `declared_for_this_branch` cases and `a_recorded_run` on this pull request's own `pull_request` run of `tests`, on every platform leg; built on its default, phase 1's exported run | the orchestrator, reading the `pull_request` run once the pull request opens |

## Not done

nothing

## Fed back into the spec

none
