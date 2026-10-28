# Overview: 1793174171-code-no-input-reaches

## Scope confirmation

Each unit #1056 lists is removed or keeps a comment giving its reason. A unit is removed only after a `seal mutate` that removes it leaves the modules reading its file green. Nothing a caller receives changes.

## Why this work exists

#1017's mutants found code that no input reaches, and `CLAUDE.md` *The rule
a mechanism is kept against* keeps only what has a record of catching
something. This work removes that code, or writes beside it why it stays.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| One case moved to another class | #1056 names i7's removal and the case that pins it. `seal layout --check` then refused `tests/github/test_issue_claims_check.py`: "class Test_segments has no test_refuses_ case" | moved `Test_module::test_an_issue_body_is_cut_where_github_renders_a_block` into `Test_segments` as `test_refuses_a_cut_where_github_renders_no_block` | The case calls `segments` alone, and the module docstring says "one class per function". Its `.test_durations` entry moved with it |
| A seventh unit was removed | #1056 lists s47 alone, the `NotImplementedError` in `import_`'s except clause | also removed `UnicodeDecodeError` from `read_manifest`'s clause in the same file | Contract rule 12. Every except tuple in the shipped Python was read for a builtin named beside its own base class, and this was the only other one. Its `seal mutate` survived, exit 1 |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check` on this branch, including `test_the_durations_file_prices_the_suite` against the edited `.test_durations` | the orchestrator, through `seal gate` |

## Not done

**`chain_check.py#reference_of` keeps its None branch.** It has the shape
k12 had, and no record reaches that branch either, because `finding_of` is
its one caller in the tree. It stays because `Test_reference_of` pins the
`regression:` row's grammar by calling it with every spelling the row
refuses. Its docstring says so since `5d3e53c9`.

**`chain_check.py#deferred_home` has no caller outside the tests.** `git grep`
finds it only at its definition and in `Test_deferred_home` and
`Test_issue_of`. `.github/scripts/release_seal.py` calls `issue_of` and
takes the home from `record_findings`. #1056 does not list it, so it stays.
Whether it is removed is the repository owner's decision.

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
