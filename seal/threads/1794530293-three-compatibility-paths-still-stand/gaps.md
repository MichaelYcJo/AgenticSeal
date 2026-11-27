# Closing memo: 1794530293-three-compatibility-paths-still-stand

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the format check, the `Broad gate` key of `seal/config.json`, at the work item's HEAD | answered: the work item's broad run, `trail/gate.md` at `700bd6f33` against `05a92dbee`, on which `guarantee.md` sealed |
| closed `frame/design.md` S2: bare `seal mode` over a root holding `config.md` and no `config.json` writes a `Mode` key from the folder and leaves `config.md` as it was. No case builds that root, by the frame's choice | answered: the review rounds `trail/rounds/round-1.md` to `round-2.md` read it, and `guarantee.md` sealed |
| closed `frame/design.md` S3: `chain-check`'s parity arm refuses nothing for a `seal/parity.md` that stands without a `seal/parity.json`. The case the phase ran, `Test_originals_of`'s case for no migration config, carries no `parity.md`, by the frame's choice | answered: the review rounds `trail/rounds/round-1.md` to `round-2.md` read it, and `guarantee.md` sealed |
| closed `frame/design.md` S7: the *Updating* line of this work item's `changelog.md` names each act *Scope* item 12 lists, each by the file it acts on and tied to no release the plugin runs. No case reads the fragment's prose, and no act it gives was run against a root an earlier release left | answered: the review rounds `trail/rounds/round-1.md` to `round-2.md` read it, and `guarantee.md` sealed |

## Not done

`tests/conftest.py`'s comment above `FENCED_ABOVE` says that two cases
build on those bytes. One case does, in `tests/lib/test_tables.py`, and so
the comment was already wrong before this work began. It describes no
compatibility path, so this phase left it as it was.

`tests/text/test_the_rules_claude_md_names_have_one_home.py#IMPORT` matches
an `@` at the start of the text or after whitespace. Phase 2 moved
`test_an_import_line_is_told_from_a_code_span` into that file word for
word, and none of its inputs puts `@` at the first character of the text.
So a mutant that drops the `^` alternative stays green (`executed`, `seal
mutate`). The gap predates this work, and a move owes no case written new,
so phase 2 left the input out.
