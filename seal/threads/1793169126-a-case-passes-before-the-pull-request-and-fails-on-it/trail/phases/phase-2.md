# Phase 2: 1793169126-a-case-passes-before-the-pull-request-and-fails-on-it

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 71dc7134 |

## What this phase was asked

`skills/code-review/orchestration.md`'s paragraph on reading CI before the
pull request names the run it reads and what that run lacks.
`tests/text/test_the_rules_have_one_owner.py#test_the_owner_states_the_dispatch_step_and_the_limit`
gains one assertion, seen red without the new sentence first. The phase also
writes the work item's `changelog.md` fragment.

## What this phase found

**The red and green runs (executed).** The new assertion ran before the
sentences existed and exited 1, the assertion naming the missing text. With
the sentences written after "then read that run's result before you take the
broad run", `bin/test tests/text/test_the_rules_have_one_owner.py -q` exited
0 (31 passed). The paragraph's other sentences, and the stated-limit
paragraph after it, keep their text.

**The text is three sentences, pinned as one assertion.** They name the run
(`workflow_dispatch` of `tests`), say why its cases see a `pull_request`
run's environment (`tests/conftest.py` removes every `GITHUB_` variable at
import), and name what it cannot have: a pull request's merge commit, and
the `hygiene` workflow, which starts only on a `pull_request` event
(`.github/workflows/hygiene.yml:3` and `:4`, read). The frame allowed "one
or two sentences"; the third keeps each sentence to one fact.

**Mutation (executed, `seal mutate`, red).** Replacing `hygiene` with `lint`
in the new text turns the case red.

**Other readers of the edited prose (executed).** `tests/behaviour/test_docs_line_wrap.py`,
`tests/behaviour/test_one_word_one_meaning.py` and
`tests/behaviour/test_every_orchestrator_act_names_its_delivery.py` exited 0
(78 passed). `uvx ruff check` and `uvx ruff format --check` over the test
file exit 0.

**Other statements of the step (read, contract rule 12).** `git grep` for
`workflow run tests`, `workflow run test.yml` and `workflow_dispatch` outside
`seal/` and the workflows finds `CONTRIBUTING.md:195`, which is about
refreshing `.test_durations` from a dispatched run and states nothing this
phase changed, `skills/implement/orchestration.md:668`, which says nothing
records the dispatch run and stays true, and two released changelog files,
which are history.
