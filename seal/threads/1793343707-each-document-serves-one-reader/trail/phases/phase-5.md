# Phase 5: 1793343707-each-document-serves-one-reader

## What this phase found

**The frame holds for the generator, and it missed nine sentences that
state the old order.** Row 5 names four prose homes: the sealer's step 2,
`skills/code-review/orchestration.md` *Orchestrator: the pull request opens
once the sealer seals*, `skills/commit-pr-convention/SKILL.md` *Pull
request bodies* and the sealer scaffolds. A `git grep` for "first part",
"above the line", "under that line", "앞부분" and `pr_body.py#HEADING`
outside `seal/threads/` found more that said the records come first or
that the orchestrator writes under the line (executed). Each now states the
new order, in the same commit as the generator:

- the sealer's `description:` (`agents/sealer.md:4-10`);
- `skills/implement/orchestration.md:41-43`, the order inside a ticket;
- the acts row *Orchestrator: the pull request opens once the sealer seals*
  in `skills/implement/acts.md`;
- `templates/setup/config.md` under `Commit and pull request language`, and
  its *What no row governs* entry, which now names `## From the records`;
- `skills/writing-style/outside-the-review.md:21-29` and `:63`, in Korean;
- the sealer row of `README.md:42` and of `README.ko.md:42`.

Three tests pinned the old wording, and each pin now reads the new one:
`tests/behaviour/test_the_sealer_guarantees.py`,
`tests/text/test_the_rules_have_one_owner.py` (two cases) and
`tests/text/test_the_chain_section_has_one_shape.py`.
`tests/evals/test_rule_cases.py` read the orchestrator's part as
`split(body)[1]`; it now reads `[0]`, and its case is renamed
`test_a_sealer_case_body_is_its_own_part_then_its_records`.
`docs/the-review-record.md:378-385` still states the old order. A pull
request does not edit the policy root, and the design's `## Rule changes`
holds its new text for *The guarantee*.

**What the generator does now** (read, `skills/code-review/scripts/pr_body.py`
at `bed1f7b1`). `HEADING` is `## From the records`. `compose` returns that
line, a blank line, `FOLD` (`<details>`), the `SUMMARY` line, a blank line,
the seven sections as before, a blank line and `FOLD_END` (`</details>`).
`split` returns the orchestrator's part first. `main` writes that part as
its bytes stood, then the heading and the copy, and with no body file it
writes an empty first part. `_check` compares the part below the line and
counts a refused line from the body's first line, so an edit to the copy is
named at the body line a reader opens. `OPENING` became `SUMMARY`, and
`FIXED` opens with `HEADING`, `FOLD`, `SUMMARY` and `FOLD_END`.

**Decisions made under `automation`, each where the frame was silent.**

- A body file with no `## From the records` line is still refused, a body
  0.25.0 wrote among them, since its line reads `## Not from the records`.
  Taking such a file whole as the orchestrator's part would keep a stale
  copy of the records above the new one. `frame/plan.md` *Operational
  impact* already sends the orchestrator to a fresh run.
- The refusal of a copied `## From the records` line stays, as the design
  states, but its old ground is gone. `split` takes the first such line,
  which is now the orchestrator's boundary, so a copied one below it no
  longer splits the body. The refusal's sentence still says "the line the
  body's two parts split at", and the docstring says it would stand inside
  the fold as a second boundary line.
- `<details>` and `</details>` are compared with the record's line as
  `readable` gives it, fences blanked, so a fenced example is copied. The
  heading line is still compared raw, because `split` reads raw lines.
- The comparison is equality, as the design states. A `</details>` inside
  a sentence, an indented one, `<details open>` and `</DETAILS>` are not
  refused. Whether GitHub ends or nests the fold at any of them is not
  known here; `gaps.md` *Not verified* names the orchestrator as the reader
  of the first body.
- The `<summary>` line carries no backticks, as the design's text gives it.
- The sealer scaffolds' `OWN_PART` ends with a blank line, so the heading
  does not follow the `Closes` line with no blank line between them.

**The new cases were seen red against the generator as it stood.** With
the test edits in place and `pr_body.py` at `91ebff35`,
`bin/test tests/skills/test_pr_body.py -q -p no:xdist` gave exit 1,
`9 failed, 14 passed` (executed). The nine:

- `test_accepts_a_work_item_as_the_records_text`, which holds the order,
  the one fold and the blank line after `<summary>`;
- three rows of `test_refuses_a_record_it_cannot_copy_faithfully`, for a
  copied heading line, `<details>` and `</details>`, the case for no second
  fold;
- both `Test_split` cases, on the new line;
- `test_accepts_a_stale_body_and_keeps_its_own_part_byte_for_byte`;
- `test_accepts_the_written_body_under_check_and_writes_nothing`, which
  now also passes a body whose part above the line changed;
- `test_refuses_an_edited_copy_naming_both_lines`, which now names line 13.

After the change the module gave exit 0, `23 passed` (executed). The
fenced `</details>` in the closing-keyword row came in a second commit,
`bed1f7b1`. It passed against `902da290` and was seen red through mutant 7
below.

**Seventeen mutants, all red** (executed, `seal mutate`, each run exit 0,
the tree clean after). One batch over `pr_body.py` at `bed1f7b1` gave
`11 mutants, 11 red, 0 SURVIVED`:

1. `HEADING` given back its old text;
2. `compose` with the heading after the copy;
3. no `<details>` line;
4. no blank line after `<summary>`;
5. no `</details>` line;
6. the refusal reading `FOLD` alone;
7. the refusal reading the raw line, not the one fences blank;
8. a missing body file written with a first part of `"\n"`;
9. `main` writing the orchestrator's part after the copy;
10. `_check` reading the part above the line;
11. `_check` counting no lines above the copy.

Six single mutants went red against the case that pins each:

- `evals/scripts/rule_cases.py` with the copy before `OWN_PART`;
- the sealer's step 2 with the copy above the line, and with the
  orchestrator's part under it;
- `skills/code-review/orchestration.md` with "under that line, to the end
  of the file";
- `skills/commit-pr-convention/SKILL.md` with "the first part's";
- `skills/implement/orchestration.md` with "first part";
- `templates/setup/config.md` naming `## Not from the records`.

**The sealer scaffolds come from the generator.** The five
`evals/behaviour/sealer/*/scaffold.sh` files are the output of
`.venv/bin/python evals/scripts/rule_cases.py` after `OWN_PART` moved
first (exit 0). Each body now opens with the orchestrator's part, then
`## From the records` and the fold. `test_evals_layout.py` and
`test_rule_cases.py` passed over them.

**`seal pr-body` over this work item.** The installed `seal` is 0.25.0's,
which runs the old generator, so the tree's `bin/seal` ran it. Into the
scratchpad's `pr-body.md` it gave exit 0, and `--check` on the same file
gave exit 0 (executed). The file is 75 lines. It opens:

```
## From the records

<details>
<summary>Copied from the records in seal/threads/1793343707-each-document-serves-one-reader/ by seal pr-body.</summary>

## What changed

`changelog.md` is not in this work item.

## How it was built

From `frame/plan.md`, its *Phases* section.
```

It ends with the `## Questions` section's table, a blank line and
`</details>`. The only other `<details>` in it is inside a code span of
row 5's Delivers cell, which the table copies. Phase 6 writes
`changelog.md`, and the orchestrator writes the round records and
`trail/gate.md`, so those three sections name their records as absent.

**The phase-boundary set is 112 modules, run as one command.** It holds
the five modules row 5 names, every module naming a changed path or
globbing `agents/`, `skills/`, `templates/` or `evals/`, and the modules
that read this work item's records. With this record, `gaps.md` and the
plan's Status cell written over `bed1f7b1` it gave exit 0, `5030 passed,
11 skipped` (executed). `ruff check` and `ruff format --check` passed
over the seven changed Python files, and `seal layout --pairs` over the
five changed test modules found 0 pairs (executed).

**One edit went through the shell** (contract rule 9). The fixture
`EXPECTED` in `tests/skills/test_pr_body.py` was rewritten by a Python
heredoc that asserted each of its two patterns matched once. The `Edit`
tool could have made it, and every later edit used it.
