# Overview: 1793174171-code-no-input-reaches

## Scope confirmation

Each unit #1056 lists is removed or keeps a comment giving its reason. A unit is removed only after a `seal mutate` that removes it leaves the modules reading its file green. `chain_check.py`'s unit is measured but not edited, because #1041's branch holds that file. Nothing a caller receives changes.

## Why this work exists

#1017's mutants found code that no input reaches, and `CLAUDE.md` *The rule
a mechanism is kept against* keeps only what has a record of catching
something. This work removes that code, or writes beside it why it stays.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The k12 item is not built | #1056: "Each item above is removed or carries its reason". The spawn: "#1041: `agents/crafter.md`, `docs/the-review-record.md`, `skills/code-review/orchestration.md` and `chain_check.py`" are not edited here | the spawn | The spawn names who may edit `chain_check.py`. The measurement is recorded below for whichever branch removes the unit |
| One case moved to another class | #1056 names i7's removal and the case that pins it. `seal layout --check` then refused `tests/github/test_issue_claims_check.py`: "class Test_segments has no test_refuses_ case" | moved `Test_module::test_an_issue_body_is_cut_where_github_renders_a_block` into `Test_segments` as `test_refuses_a_cut_where_github_renders_no_block` | The case calls `segments` alone, and the module docstring says "one class per function". Its `.test_durations` entry moved with it |
| A seventh unit was removed | #1056 lists s47 alone, the `NotImplementedError` in `import_`'s except clause | also removed `UnicodeDecodeError` from `read_manifest`'s clause in the same file | Contract rule 12. Every except tuple in the shipped Python was read for a builtin named beside its own base class, and this was the only other one. Its `seal mutate` survived, exit 1 |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check` on this branch, including `test_the_durations_file_prices_the_suite` against the edited `.test_durations` | the orchestrator, through `seal gate` |

## Not done

**k12, `skills/code-review/scripts/chain_check.py#reopened_of`.** It stays as
it stands at `5287dd42`. This mutation was run:

`seal mutate skills/code-review/scripts/chain_check.py --replace $'found = as_row(REOPENS_ROW, value)\n    return reference(found) if found else None' 'return reference(as_row(REOPENS_ROW, value))' --tests "bin/test tests/skills/test_chain_check.py -q -p no:xdist"`

It printed SURVIVED and exited 1, with 261 passed. So nothing in that module
reaches the None branch. `reference_of` (`:928`) has the same shape and is
not part of this measurement. Its None branch is called only from
`finding_of`, but `Test_reference_of::test_refuses_every_other_spelling`
calls it directly. The removal is #1041's to make, or a branch's after
#1041 merges. The orchestrator answers which one.

**The recorder's other fields that no code reads.** `broad_gate.py#read_record`
reads no `pid`, `rootdir` or `pytest` on the `session` line, and no `nodeid`
or `when` on a `test` line. They stay. #1056 names only `invocation_dir` and
`wasxfail`. A record kept with `--keep-output` is read by a person, and these
fields are what tell its sessions and its test lines apart. Whether that
reader keeps them is the repository owner's decision.

`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#collects_the_suite`
still takes a parameter named `invocation_dir`. That is pytest's own
`invocation_params.dir`, read from the config, not the recorder's field.

## Fed back into the spec

none
