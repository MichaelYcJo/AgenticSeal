# Closing memo: 1793251201-a-push-only-workflow-answers-a-deferral

## Why this work exists

`seal deferrals` counted a workflow whose trigger it could not read as one that answers a deferral, so a push-only test run let a deferral to CI pass; it now reads the spellings in use and reports any trigger it still cannot read as `unread`, not counted.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| A line shallower than the event block but not at indent zero | `frame/design.md` *Scope* item 1: "A shallower line, or a line at indent zero that is not a `- ` item, ends the block." Built: such a line makes the whole block unread | the build | *Scope* item 2 of the same design: "A partly read trigger is not returned as a smaller set: one element it could not read makes the whole trigger unread." Ending the block at `on:` / `    pull_request:` / `  push:` returned `{pull_request}`, which answers. The shape is invalid YAML and GitHub does not run it. The `break` survived `seal mutate` with all 32 cases green (executed) |
| S1, S2 and S3 as one case | `frame/design.md` scenario table: S1 and S2 are each "A case", S3 is "One parametrised case". Built: one parametrised case with six parameters | the build | The three rows give the same Then over different trigger text: `too late` with `on push`, exit 1. `agents/crafter.md` *A new test starts from its group* adds a case only where it covers something its group does not |
| Cases beyond the S-rows | `frame/design.md` *Scope* item 6: "one per scenario row below". Built: six more parameters on the S4 and S5 cases | the build | Six of 14 mutants and then a seventh survived. Each was behaviour *Scope* items 1 and 2 state that no S-row exercised: a quoted event name, a comment on a block item, a trigger read in part, a line shallower than the block (`trail/phases/phase-1.md`) |
| Two exemption comments removed | `frame/design.md` *Removes* does not name them. Built: the two `# exempt from heading_rule:` comments in `read_events` are gone | the build | The lines they excused no longer test `startswith("#")`, and `tests/censuses.py#heading_rule` refuses an exemption that excuses nothing |

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch | executed by the orchestrator's broad gate at `6ef65ee06` against `10942072d`, passed (`trail/gate.md`), and this repository declares no typecheck (`seal/config.md` *Broad gate*; #951 would add one) |

## Not done

nothing

## Fed back into the design

none
