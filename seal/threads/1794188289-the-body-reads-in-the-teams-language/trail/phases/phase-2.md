# Phase 2: 1794188289-the-body-reads-in-the-teams-language

## What this phase found

**The frame holds for this phase, with one statement the code reads
differently.** The phase was built at `4527db5f`, which merges
`origin/release/v0.36.0` at `c4bb8877`, where #1452 has landed. #1452's
`pr_body.py#compared(item, body, root, manifest=None, base=None)` returns
`(note, causes)`, and `main --check` and `chain_check.py#body` both call it
(read). So *Scope* item 3's change lands in that one function, as G14 says.
`frame/design.md` *Data & interfaces* says the four ways of not naming a
language are one state, absent, and that only a doubled row or a refused
table reaches the command as a refusal. `lib/config.py#declared_value`
refuses a `config.md` that will not read; it does not read it as absent
(read). Both paths exit 1 at `seal/config.md`, so the outcome is the same:
an absent or empty row gets the phase's own sentence, and a file that will
not read gets `lib/config.py`'s sentence.

**The fixture set of G20, listed again (executed: `git grep -l
'pr_body\|pr-body' -- tests evals` at `4527db5f`).** The command lists
fourteen files under `tests/` and eleven under `evals/`. A file was read to
see whether it runs the command over a fixture. Three test files do:
`tests/skills/test_pr_body.py`, `tests/skills/test_chain_check.py`, whose
arm cases call `compared`, and `tests/evals/test_rule_cases.py`, whose
sealer case runs `seal pr-body --check` over each sealer scaffold. So do the
five sealer scaffolds that `evals/scripts/rule_cases.py` writes. The other
eleven test files and the five sealer `prompt.md` files name the command in
prose, a docstring, a path table or a fixture's text. They build no
`config.md` that the command reads. The list is whole: it is the closed
set the command printed, each file read.

**Decision: a cause about a language row stands at the root's
`config.md`, in `seal pr-body` and in the pull request's body arm alike.**
`first_part` places such a cause at `ROOT_CONFIG`, `../../config.md`, the
root's `config.md` by its path from the work item's directory.
`pr_body.py#_place` and `chain_check.py#body` join that path to the work
item's path and normalise it, so both print `seal/config.md`. The spawn
left the arm's refusal for a missing row to this phase. The arm refuses,
because it reads the body through `compared`, and `seal pr-body` composes
no body for such a repository. A body that the command cannot compose is
not a body the arm can pass. Judged against #1452's
`frame/design.md` *Scope* items 1 and 2: a cause that `compared` places at
a record is annotated at that record's path, and the sealer and the pull
request read the body by one code path. `frame/plan.md` *Alternatives
considered* row F rejected a second arm that reads `config.md`. That does
not apply here: no second reader is added, and the one function refuses in
both places.

**Decision: where the rows name one language, every `pr.*.md` follows
`pr.md` in name order.** The count refusal applies only where the rows
differ, as *Scope* item 3 states. *Out* calls more than one translation
under one language a limit, not a guarded shape, so the code adds no guard
for it. The module docstring states what the code does with it.

**Decision: the fixtures read the rows of their own root, not the
checkout the suite runs in.** `seal pr-body` reads the rows in the work
item's checkout, and otherwise in the working directory's. Before this
phase, `tests/skills/test_pr_body.py#item_of` put the work item under a
directory that is no repository. The sealer case in
`tests/evals/test_rule_cases.py` did the same. Both therefore read this
repository's own `seal/config.md`, and would pass whatever rows the fixture
held. `item_of` now builds a shared root holding the case's `config.md` in
a git repository at the case's directory. The sealer case writes the
scaffold's whole `seal/` root into a git repository. Judged against
`frame/design.md` *Scope* item 7, which asks each fixture to carry the two
rows: only a fixture whose rows are read can show that it carries them.
Shown red by mutation: `evals/scripts/rule_cases.py` built without the
sealer config, and the sealer case refused at `seal/config.md`.

**Decision: only the sealer cases' config gains the rows.**
`evals/scripts/rule_cases.py` passes `SEALER_CONFIG` to `base_project` for
the sealer cases, and the config shared by every other case is unchanged.
*Scope* item 7 names the sealer cases, and no other agent's case runs
`seal pr-body`. The five sealer scaffolds were written again from the
script. Each gains the two rows and nothing else (executed: `git diff
--stat`).

**Decision: a `config.md` that will not read is named once, by the path
`_place` gives.** `lib/config.py#unreadable_config` opens its sentence with
the file's path on this machine, and both rows return that sentence.
`first_part` drops that path, so the line names no machine path, and
writes the cause once. Judged against `pr_body.py#_place`: the sealer
copies the first `refused:` line into a committed `guarantee.md`.

**Decision: the wording of the refusals.** The row refusal reads `names no
language in a `<row>` row`, not the design's `has no `<row>` row`, because
an empty row stands and names nothing. The count refusal names the files
as well as the count. `--check` names the file that gives each differing
line of the first part. `wrote:` and `matches:` name the files of the
first part in order, `` `pr.ko.md` then `pr.md` ``. `main --check` calls
`first_part` a second time to name them after `compared` passes, which
keeps #1452's `(note, causes)` interface. `frame/design.md` *Data &
interfaces* leaves the exact words to the crafter. Each line a person reads
is pinned by a case (contract rule 14).

**Seen red.** Each new case of `tests/skills/test_pr_body.py` was run
against `pr_body.py` as `4527db5f` left it. Each failed on the line its
guard names (executed):

- `#test_refuses_a_repository_without_a_language_row_naming_it`, all eight
  parameters, on `PR.main(argv) == 1`: both forms exited 0.
- `#test_accepts_the_first_part_the_rows_ask_for`, `rows that differ` and
  `one language and a pr.en.md`, on the body file's bytes: `pr.md` alone
  was written.
- `#test_refuses_rows_that_differ_without_one_translation`, all four
  parameters, on the exit code.
- `#test_refuses_a_first_part_that_is_not_the_translation_then_pr_md`: the
  first parameter on the exit code, and the other two on the `refused:`
  line, which named `pr.md`.
- `#test_refuses_a_language_row_no_one_reads_naming_no_machine_path`, both
  parameters, on the exit code. These two cases and the third parameter
  above were added after the code commit. They were run in a scratch
  worktree of `4527db5f` holding this phase's test file, and the worktree
  was removed.

The `one language in two cases` parameter passes against the base, which
reads no row. It pins the case fold, and is shown red by the case-fold
mutant below. The two arm cases in `tests/skills/test_chain_check.py` fail
against the base inside the fixture, since `composed_body` calls
`first_part`. They are shown red by mutation, each on its own assertion
line.

**Mutation, `seal mutate` at `eff8a640`: 22 mutants, 22 red, 0 survived
(executed).**

- `pr_body.py`, against the new cases of `tests/skills/test_pr_body.py`, 19
  mutants. `elif not value:` read as `elif value is None:`. The row
  refusal's `raise` taken out. `ROOT_CONFIG` without `../../`. The check
  that writes a cause once taken out. The machine path kept. `casefold`
  taken out of the comparison. The translation placed after `pr.md`. The
  translations under one language dropped. `if not found:` read as
  `if False:`. `> 1` read as `> 2`. `TRANSLATED` read as `pr.ko.md`. The
  owner of a replaced line named as `pr.md`. The owner of an inserted run
  named as `pr.md`. `do not give` read as `does not give`. `compared`
  reading `pr.md` alone. The write path reading `pr.md` alone. `_place`
  without `normpath`. `_names` joining with `and`. `matches:` naming `pr.md`
  alone.
- `chain_check.py#body` without `normpath`, against
  `#test_refuses_a_repository_without_a_language_row_at_its_config`.
- `compared` reading `pr.md` alone, against that case and
  `#test_reads_the_translation_as_the_bodys_first_lines`, each red on its
  own assertion line.
- `evals/scripts/rule_cases.py` without `SEALER_CONFIG`, against
  `tests/evals/test_rule_cases.py#test_a_sealer_case_body_is_its_own_part_then_its_records`.

One more mutant is not counted. With the row refusal's branch taken out,
the arm case failed on an `AttributeError`, not on its assertion. The
`compared` mutant above shows the arm case red on its own line.

**Not mutated.** The docstrings of `pr_body.py`, `chain_check.py` and
`lib/config.py` are prose. The import of each module is what can fail
there, and the phase-boundary set imports all three. In `read_own`, the
`NO_OWN_PART` refusal for a translated file cannot be reached:
`first_part` passes only names it found by listing the directory.

**Census of the `## Removes` sentence this phase rewrites (executed: `git
grep` outside `seal/threads/`).** "The body opens with the work item's
`pr.md`" returns nothing. "every absent row but two" and "The file is
optional", the sentence `gaps.md` *Not done* handed to this phase in
`lib/config.py`, return nothing under `lib`, `skills`, `templates`, `docs`
and `agents`.

**Statements of the frame and the policy root that HEAD contradicts, for
the orchestrator.** None is a file this phase writes.

- `docs/layout/the-record-layout.md` *seal/threads/<work-item-id>/*, the
  `pr.md` row of its file table, says `pr.md` is "what the pull request
  body opens with". Where the rows differ, the body opens with
  `pr.<lang>.md`. `frame/design.md` *Rule changes* adds a row for
  `pr.<lang>.md` and changes no word of the `pr.md` row.
- `docs/running/the-run.md` *The run* calls `pr.md` "the pull request
  body's first part". Where the rows differ, the first part is
  `pr.<lang>.md` and then `pr.md`. *Rule changes* names no operation on
  that section.
- #1452's `frame/design.md` *Rule changes* adds to
  `docs/checks/the-pull-request-check.md` *What the check reads at the pull
  request* a paragraph that says the body arm compares the body with "its
  `pr.md`, the heading, the seal mark ... and the records' copy". The arm
  now compares the first part `first_part` gives, and the
  `seal/config.md` refusal is one more cause it places at a path. This
  work item's *Rule changes* names no operation on that paragraph. Both
  work items change the `seal pr-body --check` row of
  `docs/running/what-a-script-gates.md`, and this one's `from:` quotes the
  row as it stood before #1452's change.

**Phase boundary (executed, exit 0): 2749 passed, 8 skipped.** The one
command was `bin/test tests/text tests/behaviour tests/skills/test_pr_body.py
tests/skills/test_chain_check.py tests/evals/test_rule_cases.py
tests/skills/test_seal.py tests/lib/test_config.py -q`. It ran at
`eff8a640`, with this record, `changelog.md`, `gaps.md` and the plan's
Status cell written and not yet committed. The set is the plan row's
files, among them `tests/behaviour/test_the_sealer_guarantees.py` and
`tests/behaviour/test_evals_layout.py`, which `tests/behaviour` holds; the
three test files the phase changed; `tests/lib/test_config.py`, which
imports the `lib/config.py` whose docstring changed; and the tree-wide pair
`CONTRIBUTING.md` names. `677dde1b` follows that run and changes one
comment and one docstring of `tests/skills/test_chain_check.py`; that
module's `Test_body` passed after it (executed, 18 passed). The suite is
unverified; the orchestrator answers it at the broad gate.
