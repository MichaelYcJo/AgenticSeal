# Phase 1: 1794530293-three-compatibility-paths-still-stand

## What this phase found

**The frame held against the tree, except for one grep.** Before the build,
each coordinate of `frame/design.md` *Removes* R1 to R21 was opened at
`9dc095ac6`, and each stood where the row says (`read`). The units each row
names were listed by `git grep` on their names, and no reader stood outside
the rows (`executed`).

**The census grep in `frame/plan.md`'s phase 1 Verified by cell cannot
print nothing.** Two of its patterns are substrings of names that stay.
`OLD_TABLE` matches `COMMENTED_OLD_TABLE`, which is the C6 shape's name in
`tests/lib/test_tables.py` and in `lib/tables.py#hidden_lines`' docstring.
`config_shapes` matches `_Old_config_shapes`, and `frame/plan.md` A5a keeps
that class. The run at `f20143fb5` printed those eight lines and nothing
else (`executed`). The grep was then asked by whole word,
`git grep -n -w -E 'OLD_CONFIG|OLD_TABLE|old_config_path|PARITY_KEYS|OLD_PARITY_CONFIG|config_shapes'`,
together with `git grep -n -E 'unconverted_'`, both outside `seal/threads/`.
Both found nothing and exited 1 (`executed`). The patterns can fail: the
same alternation counted 14 lines in `9dc095ac6:lib/config.py`, the reader
as it stood before the phase (`executed`). This was judged against the cell's
own aim, that no name the phase removes still stands, and not against its
spelling.

**The rewritten S3 case was seen red before the reader changed.**
`tests/lib/test_config.py::Test_config_pairs::test_reads_a_config_md_standing_alone_as_no_file`
was written first and run against `lib/config.py#config_pairs` with its
`config.md` arm in place. It failed on its first assert,
`config.config_pairs(...) == (None, None)`, and the value it printed was the
arm's refusal naming `seal mode` (`executed`). That is the one guard the case
names, as contract rule 15 asks. The case went green once the arm left
(`executed`). After the commit, `seal mutate` put a refusal back into the
branch for no `config.json`, for a root holding `config.md`, and the case
went red, exit 0 (`executed`). The phase's other changes add no behaviour.
They take out a branch, a name or a sentence, so no other unit owed a
`seal mutate` run, as `skills/verify/SKILL.md` *The narrow command still has
to be able to fail* states.

**The walker's comments name the callers that stand.** `seal.py` no longer
loads `lib/blocks.py` or `lib/tables.py`, and `git grep` finds no script
that loads `blocks.py` before `tables.py` (`executed`). So the comment above
`lib/tables.py`'s import of `blocks` names the scripts that load the walker
through `lib/sibling.py`: `pact_check.py`, `settle.py` and `rule_changes.py`.
The comment in the `ImportError` branch keeps its two ways a script can meet
the error and drops its citation of `seal.py`. `gfm_table` is called by
`pact_check.py` and `settle.py` alone (`executed`). So the walker's section
comment now says that the tables it reads are a record's. The docstring line
for BESIDE names `settle.py`'s *Judgments of the run* section as the caller
whose text holds one table. These were judged against `frame/design.md` R10,
"Rewritten to the callers that stand".

**`HEADERS["config"]` keeps its key and its value.** Its comment now follows
the one-cell `signer` header's precedent in the same dictionary: no reader
asks for it, and the pass holds the walk over a header of more than one
cell. The corpus count, `5455`, is unchanged (`executed`, in the boundary
run). `walk` and the fenced case read `HEADERS["config"]` where they read
`config.OLD_TABLE`. Judged against `frame/plan.md` A5a.

**Two cases changed name, because what they asserted changed.**
`test_a_repeated_header_is_read_as_a_row_and_the_doubled_item_is_refused`
became `test_a_repeated_header_is_read_as_a_row`, because its refusal was
`seal.converted`'s, the assert R18 removes. The case
`tests/skills/test_broad_gate.py#Test_missing_row.test_refuses_to_send_a_person_to_the_table_no_command_reads`
keeps its first assert, as R19 asks. Its first new name,
`test_names_the_config_json_path_the_key_is_missing_from`, was refused by
`seal layout --check` through
`tests/behaviour/test_this_repository_passes_its_own_checks.py::Test_seal_layout::test_accepts_this_repositorys_tests`:
"class Test_missing_row has no test_refuses_ case" (`executed`). The case
pins a refusal, so it is now
`test_refuses_naming_the_config_json_path_the_key_is_missing_from`, in
`d4de43351`. No document, census or `check:` line named any case this phase
removed or renamed, outside other work items' dated records (`executed`:
`git grep` on each name).

**`tests/skills/test_pact_check.py#test_refuses_a_pact_config_that_will_not_read`
lost its parametrize.** One shape was left. The case now writes the
`config.json` that will not parse itself, under the same name.

**The phase-boundary set excludes the test files that load `tests/conftest.py`
alone.** The phase changed `tests/conftest.py`. It took out `write_old_config`,
whose one importer was `tests/lib/test_config.py` (`executed`: `git grep`),
and it reworded two comments. Every other file that imports from it reads the
same names and bytes, so the change cannot move their result. That is the
reading `skills/verify/SKILL.md` *Scope: cheap and often, broad and once*
gives of a file that reads a path. The set was each `tests/` file outside
`tests/text/` and `tests/behaviour/` whose text names a changed path. It
holds 32 such files, among them the plan row's eight outside
`tests/behaviour/`, with `tests/text` and `tests/behaviour` beside them.

**The run at the phase boundary.** At `f20143fb5` the set ran as one
command, `bin/test -q` over those paths: 2 failed, 4435 passed, 10 skipped
(`executed`). One failure was the layout refusal above. The other was
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
red because this work item had no `gaps.md` yet. The run after both repairs
is the one `frame/plan.md`'s Status cell stands on, and the hand-back gives
its count.
