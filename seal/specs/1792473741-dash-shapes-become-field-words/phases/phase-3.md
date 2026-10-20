# 1792473741-dash-shapes-become-field-words — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 45ebceca |

## What this phase was asked

The grammar's two tables (S10 to S12). `docs/the-review-record.md` §*The
round record*'s three old-spelling rows move to an `| Old spelling | Means |`
table under the grammar table, and the section's two sentences that named
them are rewritten. `grammar` reads both tables; `NOWHERE`, `NOT_ANY`,
`meant_by` and the `nowhere` branch go. `templates/config.md`'s grammar
sentence names both tables. The table and its loader change in one commit.

## What this phase found

- **`grammar` returns both tables, `(rows, old)`.** The module binds them as
  `GRAMMAR` and `OLD_SPELLINGS` at import, and `SPELT` reads the labels and
  the old spellings together, so `misspelt` refuses an old spelling as the
  label its `Means` cell names, as before. Every case of
  `test_a_label_in_another_spelling_is_refused_by_line` passed unchanged;
  only its docstring's wording of where the spellings stand changed.
- **The header lookup is one function for both tables** (`table_at`), so
  the refusal for a missing table, `holds no table headed`, and the one for
  a missing separator are the same sentences for either.
- **A row with `Where` `nowhere` is no longer a kind the loader knows.** The
  old shape, a bare `—` shape cell, is refused as a shape that is not one
  code span; a code-span shape with `nowhere` is refused as a row the check
  cannot read. Both are S12 cases.
- **One mutation found a branch no case held:** a `Means` naming a section
  heading, `## Findings`, which is a row of the grammar table and no label.
  A case was added, and the mutation then went red. The other eight
  mutations of the loader's new branches went red on the first cases.
- **Three other documents say "the grammar table"** (`agents/warden.md`
  step 7, `skills/code-review/SKILL.md` §*The record*,
  `templates/sdd-round.md`'s comment), each about the row a written line
  follows, which is still the first table's. They stand.
  `skills/code-review/SKILL.md` also called that table "the grammar's one
  statement"; the sentence now says the section is.
