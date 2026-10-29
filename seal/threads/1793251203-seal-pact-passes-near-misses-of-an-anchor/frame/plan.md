# Implementation Plan: 1793251203-seal-pact-passes-near-misses-of-an-anchor

Approved 2026-10-29 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phases 1 and 2.
Approved 2026-10-29 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phases 3 and 4.

## Summary

`seal pact` read a near miss of an anchor as no anchor. Phases 1 and 2
closed the facts the code can read exactly. A row of the anchor table
naming a remote the signer does not declare is refused, and the inline
token is refused in any case. Phase 1 also built a row scan, which refuses
a row outside the anchor table by its cells. The seal came back undecided on
that scan's limit. The owner then answered that the criterion is meaning,
not spelling, and P1 was answered (c).

This reframe splits the question by meaning. A header that differs from
`| Pact | Clause | Hash |` only by case, or by one emphasis run wrapping a
whole cell, is the anchor table by definition. One closed function in
`pact_check.py` reads it so, and `seal pact` grades its rows. Every other
shape is a judgment of meaning, and the proofer makes it at the signer's
review. Phase 3 removes the scan and adds the normalisation. Phase 4 gives
the proofer one sentence. Phases 1 and 2 keep their commits.

## Technical context

**What this builds on, by coordinate (read at `a5533a3d`).**

- `pact_check.py#check` (`:744` to `:790`). `declared_remotes` (`:744`) is
  every pact the signer's `Pact` row declares. The walk reads the anchor
  table with `first_table` (`:753`) and drops its "holds no" refusal. Each
  row is judged: `one_remote`, then `UNDECLARED` where the remote is not
  declared (`:766`), then `heading_parts` and the hash shape. Then the guard
  `if not table_refusals:` (`:780`) calls `stray_rows` and prints
  `OUTSIDE_TABLE`. Then `INLINE_TOKEN` is searched over
  `checker.unquoted(body)` (`:787`).
- `pact_check.py#first_table` (`:303`). It calls `config.gfm_table` with the
  header it is given, then, where the walk refused nothing, counts every
  further unfenced line whose `table_cells` equal that header and refuses
  each as a second header. It is called for the map (`:349`) and for the
  anchor table (`:753`), and nowhere else (`git grep`, executed).
- `hooks/lib/config.py#gfm_table` (`:1075`) finds the header as the first
  shown line whose `table_cells` equal the header it is given. So handing
  it the as-written cells of the first line the key matches finds that same
  line, because any earlier line with those cells would key the same.
- `pact_check.py#row_cells` (`:505`) and `#stray_rows` (`:531`) are the
  scan. No module outside `pact_check.py` calls either, and `OUTSIDE_TABLE`
  appears only there and in the test module (`git grep`, executed).
- `tests/skills/test_pact_check.py`:
  - `OUTSIDE_TABLE`'s copy (`:91`);
  - the passes case `test_accepts_a_signer_citing_the_current_clause`
    (`:540`), with the `| Repository | Role |` table (`:574`), the
    `| pact | clause | hash |` table over `ordres-api` (`:576` to `:578`) and
    frame z's indented rows (`:586`);
  - `test_refuses_an_anchor_row_nobody_reads`, with its `out.count`
    assertion (`:893`) and the id `a row under a blank line` (`:876`);
  - `test_refuses_an_anchor_row_no_anchor_table_holds` (`:965`), whose
    eleven ids hold the lower-case, emphasis, plural, reordered,
    extra-column, no-pipes, code-span, headerless and below-the-anchor-table
    shapes.
- `skills/code-review/SKILL.md` *Two stages, in order*, stage 1 (`:22`),
  under the rule whose check line is
  `evals/behaviour/proofer/rule-proofer-one-finding/`. `agents/proofer.md`
  step 3 already has the proofer read `frame/design.md`.
- The rounds. Round 1 finding 1, round 2 finding 1 and round 3 finding 1
  each stood in the scan's line reader or in a text describing it. Round 3
  and round 4 left one more question on it under *Not judged*.

**The failure scenario of the chosen approach, six months on.** There are
two.

- **A header outside the normalisation, with no proofer.** A signer's
  framer writes its anchors under `| Pact | Clause | Hashes |`. The work
  item is routed `straight to the PR`, so no proofer reads the frame.
  Months later the pact changes a clause, and `seal pact` reads that signer
  as citing nothing. It prints `READ ... — 0 pact anchors naming this pact`
  and exits on the other signers alone. The same happens through a proofer
  that misses the line. This is the silence #1132 reports, kept for the
  shapes outside the normalisation where no proofer catches them.
- **A table that is not an anchor table but keys like one.** A signer's
  frame holds a table headed `| pact | clause | hash |` that lists
  something other than anchors, for example a glossary of the three words.
  `seal pact` now reads it as the anchor table and refuses its rows at
  exit 2, `NOT_ONE_URL` for a cell that is not a remote. The remedy is one
  edit: rename the header. The exact header has the same exposure at the
  base, and this repository signs no pact, so the cost is unmeasured in a
  signer.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. A header near miss is refused at the header's line by a list of spellings: case, emphasis, code spans, plural | Every spelling outside the list passes in silence. The probe found five such shapes the issue did not list (d12 reordered, d13 an extra column, d14 no outer pipes, d26 `Clauses`, d24 no header at all). Each new one is another branch, which is how #913 plan A4 describes the near-miss grammar it removed. It also refuses a table that means the anchor table, which the owner calls the worst outcome | Not taken |
| A2. The settle precedent: a header whose letters, case folded, are those of `Pact`, `Clause`, `Hash` is refused | Catches d07, d09 and d15, and misses d08 `Hashes`, which the issue names, with d12, d13, d14, d24 and d26. It refuses where the meaning is the same, and the owner's answer rejects closeness of spelling as the criterion | Not taken |
| A3. A row outside the anchor table that names a declared remote in one cell and a heading path in another is refused at its line (the row scan) | Built in phase 1 and reviewed four rounds. Three of them found a shape its line reader `row_cells` got wrong or described wrongly: a tab-indented row (round 1), a row right under a paragraph line (round 2), and the docstring pinning that (round 3). Round 4 carried one more, a row four columns in under the table. It refuses a table of another meaning whose row happens to hold a declared remote and a heading. It leaves a double miss (a near-miss header over an undeclared remote) silent, which is what the seal could not decide | Taken in phase 1; **removed** by this reframe (phase 3) |
| A4. No header at all: any row naming a declared remote is graded as an anchor (replaces the structure) | The premise the header keeps is that `gfm_table` reads the table as GitHub renders it, and judges a second table, a stray row and a row of another width (#913 plan A1, A6). A header-free scan is a second grammar beside the walker. It also grades a near miss as if it were right | Not taken |
| A5. A `Pact` cell close to the pact's remote, by edit distance, is refused | A threshold is a guess from words. `pakt` against `pact` is one letter, and so is `org/a` against `org/b`, two real repositories. `CLAUDE.md` makes such a reading a report, not a gate | Not taken |
| A6. A row of the anchor table naming a remote the signer does not declare is refused at its line | Premise of the old pass checked: *another pact's row is that pact's to grade* holds only where the signer declares that pact, because otherwise that pact's `seal pact` reports the signer `ONE-SIDED` and reads none of its frames (`pact_check.py#check`, the `ONE-SIDED` arm). So an undeclared row was graded by nobody. The cost is a frame in a signer citing a pact it does not declare, which is a one-sided relationship either way | **Taken** (phase 1, kept) |
| A7. A row naming another remote is printed in no exit class | A typo prints one line and the exit is decided by the other signers alone, which is the silence #1132 reports. `docs/the-record-layout.md` wants a held anchor's wrong answer loud | Not taken |
| A8. `INLINE_TOKEN` takes `re.IGNORECASE` | `**Pact:**` as a label is refused, as the case-sensitive token already refuses `**pact:**`; the remedy is `**Pact**:`. Measured: no line at `HEAD`, `v0.22.0`, `v0.23.0` or `v0.24.0` matches the case-folded token that the exact one misses, except lines quoting R24. It cost no finding in four rounds. It is the same case member A12 gives the header | **Taken** (phase 2, kept) |
| A9. The token also allows spaces beside the colon | Measured: 6 more lines at `v0.22.0`, 1 at `v0.23.0` and 4 at `HEAD`, all prose. Each would be refused at exit 2 in a signer's frame | Not taken; stated as a limit |
| A10. No change to the token, and a limit sentence for all three spellings | A `PACT:` leftover reads as a signer citing nothing, for a one-flag change that measured no false positive | Not taken |
| A11. The row scan runs whether or not the walk refused | d06's row is refused twice, once by the walk and once by the scan, for one defect | Moot: the scan goes (A3), and with it the guard and the count assertion that pinned this choice |
| A12. A closed header normalisation (the owner's answer in `guarantee.md`). A header whose cells differ from `Pact`, `Clause`, `Hash` only by case, or by one emphasis run wrapping a whole cell, is the anchor table, and its rows are graded; anything else, a plural among them, is another table. The members are decided from the tree. Whitespace around a cell is already stripped by `table_cells`. Case is the settle's precedent for one word. Emphasis is `*` or `_`, one to three long, the same run opening and closing the cell with no space inside it: GitHub renders a header cell bold, and `** Pact **` is not emphasis to GitHub. Code spans are out, because a code span marks a mention of the word, not a use, and the anchor's cells are written bare; HTML tags and strikethrough are out | It is a grammar of rendering, of the kind A3 was, so it is kept closed and reads header cells only. Every shape it leaves out (nested runs such as `**_Pact_**`, escaped delimiters, code spans, a plural) is another table, read by nothing in code. A table that keys like the anchor table and means something else is read as one (*Technical context*, the second failure scenario). Its cost is one function, its cases, `first_table` taking a keyword, and a second-header scan that matches by the key | **Taken** (phase 3), with A13 for the shapes it leaves out: P1 answered (c) |
| A13. `seal pact` reads only the exact anchor table and the exact token, and refuses only what it reads there; whether a line elsewhere in a signer's frame was meant as an anchor is judged by the proofer at stage 1 of the signer's own review | Where the judgment sits: the proofer, at each round of the signer's work item. It reads that item's `frame/design.md` against the shape `pact_check.py`'s docstring states and against the signer's `seal/config.md` `Pact` row. Both files are in the signer's repository, so nothing reads the pact (`docs/the-pact.md` *A signer's CI reads nothing of the pact*). Cost: one sentence in `skills/code-review/SKILL.md`, and the proofer's attention on a frame that cites a pact, which is rare. No new spawn and no question to a person. It catches every shape of intent with no list, at the signer's pull request, before anyone runs `seal pact`, which runs in no CI. It misses a work item routed `straight to the PR`, a frame edited after its last round, and a shape a proofer overlooks. Alone, it answers "these differ" in code for a lower-case anchor table, which the owner calls the worst outcome | **Taken** for the shapes A12 leaves out (phase 4); not taken alone |
| A14. A12 with the row scan kept for the headers outside the normalisation | Both grammars at once: the normalisation's shapes, and the scan's tab, paragraph and indentation shapes. A plural-headed row naming a declared pact is refused while the same row naming an undeclared one passes, which is the asymmetry the seal could not decide, moved to the plural | Not taken |
| A15. The build as it stands, the double miss stated as a limit | The sealer read it as not meeting #1132, and the owner answered "neither" | Not taken |

**Why A12 and A13 together.** `questions.md` P1 was answered (c) on the
owner's direction. A script answering "these differ" where the meaning is
the same is the worst outcome. So the shapes that mean the same by
definition are read in code. The shapes whose meaning needs judging are
left to the proofer.

The tree supports the split.

- This work item's rounds show that a grammar predicting rendering keeps
  finding its next shape. A12 is therefore closed to header cells and two
  members, and every shape outside it goes to judgment rather than to a new
  member.
- `CLAUDE.md` makes a reading guessed from words a report. The
  normalisation guesses nothing: a member is in or out by its stated
  definition.

**Where #1132's *Done when* is met.** Bullet 2 reads *A table whose header
differs from `| Pact | Clause | Hash |` only by case, a plural or emphasis is
refused at its line.* It is not met as written.

- Case and emphasis are met by grading in code. The table is the anchor
  table, and each of its rows is graded or refused at its own line. The
  header line itself is not refused.
- The plural is met by the proofer's judgment at the signer's review, not
  by a refusal at its line.

Bullet 3 is met in code for every row of the anchor table, through
`UNDECLARED`. Under a header outside the normalisation it is met only by the
proofer. Bullet 1 is met as built (A8, A9). Bullet 4 is met for phases 1 and
2 against `28edee12`, which is `5287dd42` for this code. Phase 3's cases are
seen red against `a5533a3d`, and those shapes printed nothing at `5287dd42`
too (`frame/design.md` *Where #1132's Done when is met*).

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The anchor table's near misses, as first framed: the `UNDECLARED` refusal, the row scan, two sentences, the docstring, and the passes case declaring the remotes its rows name | `tests/skills/test_pact_check.py`, `tests/behaviour/test_one_word_one_meaning.py`, `tests/behaviour/test_a_signer_declares_its_pact.py`, in one command; S1, and S3 and S5 as first framed (a row no anchor table holds, and one refusal per row), each seen red against `28edee12` or by `seal mutate` (`trail/phases/phase-1.md`) | ce323fe9 |
| 2 | The inline token: `INLINE_TOKEN` with `re.IGNORECASE`, its comment stating the case fold and the space limit, and the docstring's sentence on the token | the same three modules in one command; S6's ids seen red against `28edee12`; S7's spellings in the passes case | 063644e5 |
| 3 | The anchor table read by meaning, and the scan removed (`frame/design.md` *Scope* items 2, 3, 4 and 6, `## Removes` rows 4 to 6). Code: the key function and its comment listing the members and the shapes left out; `first_table` taking a keyword, used by the anchor call alone, to find the header by key, hand its as-written cells to `gfm_table` and count further headers by key; `stray_rows`, `row_cells`, `OUTSIDE_TABLE` and the guarded call deleted; the docstring's *What each frame is read for* and *Exit codes* rewritten. Tests: S3's graded case, one id per spelling; S4's `UNDECLARED` under `| pact | clause | hash |`, with that row taken out of the passes case; S5's id in `test_refuses_an_anchor_row_nobody_reads`; S6's shapes in a frame of the passes case in place of frame z's indented rows and the `| Repository | Role |` table; `OUTSIDE_TABLE`'s copy, `test_refuses_an_anchor_row_no_anchor_table_holds` and the `out.count` assertion removed; the passes case's docstring and comments rewritten | the same three modules in one command; S3's nine ids, S4, S5 and S6's shapes each seen red against `a5533a3d`; `seal mutate` over the key function, dropping the case fold and narrowing the run to one character, each red; S10's `git grep` printing nothing | 5267a54e |
| 4 | The proofer's judgment for the shapes the normalisation leaves out (*Scope* item 7): one sentence in `skills/code-review/SKILL.md` stage 1. It names a plural or other wording, a row with no header and a row outside the table, by the shape `pact_check.py`'s docstring states and the `Pact` row of the repository's `seal/config.md`. A line meant as an anchor that `seal pact` does not read is a finding | `tests/text/test_review_axes.py` and every test module that reads `skills/code-review/SKILL.md`, found by `git grep -l "code-review/SKILL.md" tests/`, in one command. No eval (`frame/design.md` *Out*) | 6303f97f |

Each phase runs the modules it names and no broad run: the full suite, the
repository-wide lint and the typecheck are the orchestrator's one broad gate
after the review rounds settle (contract rule 2).

## Operational impact

- **`seal pact` grades more tables, refuses more of their rows and more
  spellings of the token, and refuses nothing outside them.**
  - A table under a header that differs from the anchor header only by case
    or by one emphasis run per cell was read by nothing. It is now the
    anchor table: its rows are graded, and refused where they cannot be.
  - A row naming a remote the signer does not declare, and a `PACT:` or
    `Pact:` token, were passed in silence. Each is now refused at exit 2.
  - A table under any other header is still not read, as at the base, and
    the signer's `READ` line counts no anchor for it.
  - `seal pact` runs in no CI, so no pull request and no hook changes
    verdict.
- **A signer's review reads the anchors `seal pact` does not.** The proofer
  judges, at stage 1, a line meant as an anchor and written outside what
  `seal pact` reads. Only frames that cite a pact are affected.
- **The records that state the scan are rewritten by their owner.**
  `changelog.md` says a row outside the anchor table is refused and states
  the two limits. `gaps.md` holds the two S5 divergence rows, on a count
  assertion phase 3 removes. Both are the orchestrator's to rewrite before
  the next seal.
- No question is put to a person mid-run. No new dependency, no environment
  variable, no migration. `first_table` gains one keyword argument and no
  other function that stays changes its signature. `hooks/lib/config.py` is
  not edited.
