# Phase 1: 1793251201-a-push-only-workflow-answers-a-deferral

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 61e2e6be |

## What this phase was asked

Build phase 1 as `frame/plan.md` *Phases* states it. Cases S1 to S8 of
`frame/design.md` are seen red at this branch's base before the code
changes. Then come `read_events` and `inspect` in
`skills/verify/scripts/deferral_check.py`, the `KNOWN_LIMITS` clause, and
the fifth outcome in the module docstring, `skills/verify/SKILL.md`,
`README.md` and `README.ko.md`, with every `## Removes` row taken out. Run
the checks the plan's *Verified by* cell names, including `seal mutate`
over `read_events` and `inspect`. Write this record, set the phase's Status
in `plan.md`, and commit. Do not write `changelog.md` or touch
`.claude-plugin/plugin.json`.

## What this phase found

The frame held. Every coordinate in `plan.md` *Technical context* matched
the tree at `15c0d1f1`, and `git diff --stat c825fd2c 8d8d6390` over the
script and its test module was empty (executed).

The cases are in `tests/skills/test_deferral_check.py`, class `Test_main`,
under the heading *the trigger is read, or reported unread and not
counted*:

| Scenario | Case |
|---|---|
| S1, S2, S3 | `test_a_push_only_trigger_in_each_spelling_is_too_late`, six parameters |
| S4 | `test_a_pull_request_trigger_in_the_wider_spellings_answers` |
| S5 | `test_an_unread_trigger_is_reported_and_not_counted` |
| S6 | `test_an_unread_workflow_beside_one_that_answers_still_resolves` |
| S7 | `test_a_trailing_comment_is_not_read_as_an_event` |
| S8 | `test_the_printed_limit_names_a_trigger_it_cannot_read` |

Before the script changed, the 15 parameters of S1 to S8 failed and the 12
existing cases passed (executed). Each failure was the one the design
predicts. The push-only spellings exited 0. The wider pull-request
spellings printed `(trigger unread)`. The flow mapping printed `too late`
with no `unread` line, and S7 printed `on push] # trigger`.

`seal mutate` ran 14 mutants over `read_events`, `inspect` and the two
helpers the rewrite added, `block_entries` and `unquoted` (executed). Eight
went red and six survived. The survivors were a trigger read in part (`all`
weakened to `any`, a flow list not required to close, a block line that is
neither a key nor an item skipped), quotes around an event name kept, and a
comment left on a block line. The frame's *Scope* items 1 and 2 state each
of these, and no S-row parameter exercised it. Commit `5cc5c80d` adds five
parameters to S4 and S5. A probe running the base script showed each of
the five reading differently from what its case expects (executed). The
six mutants then went red (executed).

One more mutant survived: the `break` on a line shallower than the block.
That line is invalid YAML, and ending the block there returned the entries
above it as the whole trigger. Commit `61e2e6be` makes that block unread
and adds a sixth parameter, red against the base script, against the
`break` and against the arm removed (executed). `gaps.md` records it as a
divergence from *Scope* item 1.

Two units were not mutated. Dropping `names and` from the final test in
`read_events` is an equivalent mutant, because `set()` of an empty list is
the empty set either way. `KNOWN_LIMITS` is a string, and S8 reads it.

The rewrite took out the two `# exempt from heading_rule:` comments in
`read_events`. No line there tests `startswith("#")` now: `COMMENT` drops a
whole-line comment, and `tests/censuses.py#heading_rule` refuses an
exemption that excuses nothing.

Ruff's B007 refused `i` as unused when it was read after the loop, so the
reading moved into the loop body. An import added in an edit of its own is
removed by the formatter hook as unused; add it in the same edit as its
first use.

W1 of `frame/questions.md`, the wording, was settled here:

| Place | Wording |
|---|---|
| `KNOWN_LIMITS` | a trigger written as a flow mapping, or as a flow list across lines, reads as unread and is not counted |
| Module docstring | `unread trigger  something runs it on a trigger this cannot read; not counted` |
| `skills/verify/SKILL.md` *The answerer has to exist* | something runs it, but its trigger could not be read, so it is not counted |
| `README.md` | *trigger unread, not counted* |
| `README.ko.md` | 트리거를 읽지 못해 세지 않는 것 |
