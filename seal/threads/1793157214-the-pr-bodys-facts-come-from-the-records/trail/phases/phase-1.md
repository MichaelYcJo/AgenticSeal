# Phase 1: 1793157214-the-pr-bodys-facts-come-from-the-records

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 7d38665c |

## What this phase was asked

Build `frame/plan.md` row 1 and nothing of phases 2 and 3. That is
`skills/code-review/scripts/pr_body.py` with `HEADING`, `FIXED`, `Refused`,
`read_item`, `compose`, `split` and `main`, run as
`seal pr-body <item> --body <file> [--check]`. It also asked for the
`pr-body` entry in `seal.py#TOOLS` with its parametrize row in
`tests/skills/test_seal.py`, the `SHIPPED` row, the stored `== 13` taken
out, and `HEADING`, `## Phases` and `## Not done` added to the no-row list
with `_literal_strings` extended. `frame/design.md` is the source of every
rule: copy records, never summarise and never count. Round records are read
through `chain_check.py`'s grammar and other headings through
`unverified_check.py`'s reader, and no new parser is written. The
verification asked for is `frame/plan.md` *Verification this work item
owes*: a red run for each new case, no `seal mutate`, and one `bin/test` over
the row's cases and the modules `git grep -l` finds. It also asked for
`bin/seal layout --check` and `bin/seal rules --check` from the top, and a
run of `seal pr-body` over the owl thread at `74a680c1`.

## What this phase found

The frame holds against the tree. Every coordinate the plan's *Technical
context* names stands where it says: `seal.py#TOOLS`, the `== 13` at
`tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py:444`,
`SHIPPED` and `NO_WALK`, `_literal_strings`, and the readers of
`chain_check.py` and `unverified_check.py`.

Decisions settled while writing the code, where the design is silent:

- **Two fixed lines beyond the design's list.** A `frame/plan.md` with no
  `## Phases` section gives `` `frame/plan.md` has no `## Phases` section. ``,
  and a `trail/gate.md` with no table line gives
  `` `trail/gate.md` holds no table line. ``. They follow the shape of
  `gaps.md`'s and `frame/questions.md`'s lines. The plan's failure scenario
  expects a missing `## Phases` to show as such a line, not as a refusal.
  Both are in `FIXED`.
- **A second section is refused.** A second `## Phases`, `## Not verified`
  or `## Not done` heading is refused at its line, because copying one would
  leave the other out without a word.
- **The `HEADING` refusal reads the copied lines.** Design S6 says a record
  holding a line equal to `HEADING` is refused. The code refuses a copied
  line equal to it, at the record's path and line, since only a copied line
  can split the body. A line equal to it in a part the generator does not
  copy, such as `gaps.md`'s divergence table, is not refused.
- **Round names are read by `hooks/lib/routing.py#round_number`.** It is the
  one ordering rule the chain check's records arm uses, so the body lists
  the records the check judges. It also accepts `round-0.md`, where the
  design says a positive integer. Phase names are read by `PHASE_RE`, in the
  same shape.
- **`--check` compares lines, not line ends.** The body's part above the
  heading is split with `gfm_lines` and compared line by line, so a CRLF
  there is no difference. A write keeps the part under the heading as its
  bytes stood, CRLF included.
- **`--check` names one refusal per differing run of lines.** The runs come
  from `difflib`. Each refusal names the body's line and either the record's
  `path:line` or that the line is a fixed one.
- **A body file that is not there is refused under `--check` at exit 1.**
  Exit 2 stays for unusable arguments, an `<item>` that is not a directory,
  and a module that will not load.
- The *Review rounds* section has no `From` line, because each round's
  `###` heading names its record, as the design's block lays it out. The
  phase records' bullets form one block.

The cases written new are all in `tests/skills/test_pr_body.py`:
`Test_compose` (S1, S2, S3, S4, S5, and S6 over three records),
`Test_split` (S7, both cases), `Test_read_item` (both cases), and `Test_main`
(S8, S9's two cases, S6's exit over two inputs, and exit 2 for an item that
is not a directory). Each was seen red once against the tree before the
module existed. `bin/test tests/skills/test_pr_body.py` stopped at
collection on `FileNotFoundError` for `pr_body.py` and exited 2. The extended
`_literal_strings` was seen red with the `## Phases` item taken out of
`templates/setup/config.md`:
`test_the_exclusion_list_holds_every_string_a_checker_matches[## Phases]`
failed alone and the run exited 1. The item was then put back.

The existing cases relied on are the `pr-body` row of
`Test_main::test_accepts_each_tool_and_hands_its_script_every_argument` (S10),
`test_every_shipped_command_is_classified` with the new `SHIPPED` row, and
`test_the_enumeration_is_not_empty` with the equality and no stored count.

One `bin/test` ran over the row's modules and the readers `git grep -l`
found: `-e TOOLS -e "What no row governs"`, the readers of
`templates/setup/config.md`, and the two modules that walk every shipped
script. It passed 2020 cases, skipped 10 and failed 1. The failure is
`tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
which names this work item because its thread holds `frame/` and no
`gaps.md`. The thread stood that way at `e4b2c01f`, before this phase, and
row 1 does not ask for `gaps.md`. `bin/seal layout --check` and
`bin/seal rules --check` each exited 0 from the repository's top.

`bin/seal pr-body` ran over `74a680c1:seal/threads/1793152332-the-stamps-mark-is-an-owl/`,
taken out with `git archive` into a scratch directory. The write and then
`--check` each exited 0. The body is 11,857 bytes over 90 lines. Read against
the thread's records, section for section:

- *What changed* holds the changelog whole, its own `### Changed` and
  `### Removed` headings included.
- *How it was built* holds the four rows of the plan's *Phases* table and
  the four phase records' paths.
- Round 1 gives its `target:` line and finding 1's heading at `####`, with
  its `severity:`, `verdict:` and `answer:` lines. Round 2 gives its
  `target:` line and its line `None. The fix range closes round 1's one
  finding and introduces no defect.`
- *Broad gate* holds the one row, `081f9086 against c8bb9693`.
- *Not verified* holds the one row, and *Not done* holds `nothing`.
- *Questions* holds all four rows, the three `open` ones among them.

`diff` of the body's changelog, *Phases* table and question rows against the
records exited 0 for each.

For phase 3: `compose(name, texts)` takes any mapping of record paths to
texts, so the fixtures can be composed without a directory. `FIXED`'s lines
are templates over `{name}` and `{path}`. A round record whose `target:`
names `BUILD_SHA` is refused by `compose`, which is `frame/questions.md` Q6.
