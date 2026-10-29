# Design: 1793251203-seal-pact-passes-near-misses-of-an-anchor

Issue #1132, row R24 of #956's audit. `seal pact` reads a signer's pact
anchors from the `| Pact | Clause | Hash |` table of each `frame/design.md`,
and refuses the inline `pact:` token that table replaced. Several near misses
of both are neither graded nor refused, so a signer that writes one is
reported as citing nothing.

This reframe follows the owner's answer in `guarantee.md` and `questions.md`
P1, answered (c). Whether two headers mean the same thing is a question of
meaning, not of how close their spelling is. Part of it is settled by
definition. A header that differs from the anchor header only by case, or
by one emphasis run wrapping a whole cell, is the anchor table, and
`seal pact` grades its rows. One closed function in `pact_check.py` states
that. The rest is a judgment of meaning: a plural or other wording, a row
with no header, a row outside the table. The proofer makes it at stage 1 of
the signer's own review. The row scan built in phase 1 is removed.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `guarantee.md`, its last line, the owner's answer of 2026-10-29, and `questions.md` P1, answered (c) | A header that means the same is the anchor table and its rows are graded, so an undeclared remote under it is refused `UNDECLARED`. Sameness is one stated normalisation, and a header outside it, such as a plural, is another table. A script answering "these differ" where the meaning is the same is the worst outcome. Whether a header outside the normalisation was meant as an anchor is the proofer's judgment |
| `docs/the-pact.md` *The pact anchor*, as the unsettled design `seal/threads/1793169127-pact-check-reads-the-retired-grammar/frame/design.md` `## Rule changes` items 2 and 3 state it (#913, merged at `7da1a77e`) | The policy in force. A row naming another pact is passed over; a row it cannot grade and every `pact:` token are refused at exit 2. `## Rule changes` below quotes that text as its `from:` |
| `seal/threads/1793169127-pact-check-reads-the-retired-grammar/frame/questions.md` Q1 and `frame/plan.md` A9 to A11 | The inline form is refused, not graded and not passed over. That decision is not reargued here; this work widens which spellings of the token it reaches |
| `docs/the-pact.md` *A signer's CI reads nothing of the pact* | Nothing at a signer's pull request reads the pact, because no token reads another repository. The proofer's judgment in *Scope* item 7 reads the signer's own frame and the signer's own `seal/config.md`, and never the pact, so that section stands unchanged |
| `docs/the-record-layout.md` *Whether a line is live is asked by what the line does*, first bullet | A line that holds an anchor is read on doubt and the wrong answer is loud. Every row of the anchor table that `seal pact` cannot grade is refused at exit 2. A line outside that table is no anchor `seal pact` can tell, and the loud answer for it is a proofer's finding at the signer's review |
| `CLAUDE.md` *The rule a mechanism is kept against*: a check gates only a fact it reads, a reading guessed from words is a report, and a mechanism stays only while its history shows what it caught against what it costs | The declared-remote refusal reads a fact, the signer's `Pact` row. The normalisation is a closed definition, not a guess: it names its members and reads nothing else. A row's intent under any other header is guessed from words, so no gate decides it. The row scan has no catch in any release and cost this work item three rounds |
| `skills/settle/SKILL.md` *Rule changes*, the `## Rule changes` heading rule, and `skills/settle/scripts/rule_changes.py#letters` | The tree's precedent for case: the same letters, case folded, are the same word. It grounds the normalisation's case member and the case-folded `pact:` token, which phase 2 built |
| GitHub's rendering of a table header, as `hooks/lib/config.py#gfm_table`'s docstring treats it, and GFM's emphasis rule that a delimiter run with a space inside it is no emphasis | It grounds the emphasis member. GitHub renders a header cell bold, so `**Pact**` there shows the same word in the same weight, and `*Pact*` the same word in italics. `** Pact **` is not emphasis, so it is not stripped. A code span is a mention of the word, not a use of it, and the anchor's cells are written bare, so code spans stay out. Strikethrough marks the word deleted, and HTML tags are no markdown emphasis; both stay out |
| `trail/rounds/round-1.md` finding 1, `round-2.md` finding 1, `round-3.md` finding 1 | The tree's evidence that a grammar predicting how a line renders keeps finding its next shape. Each round found a shape the scan's line reader `row_cells` got wrong or described wrongly. This is why the normalisation is closed and reads header cells only, never the line around them |
| `skills/code-review/SKILL.md` *Two stages, in order*, stage 1, and `agents/proofer.md` step 3 | The proofer already reads the work item's `frame/design.md` at every round, and stage 1 reads it against the ratified documents. This is where the judgment of *Scope* item 7 sits, with no new spawn |
| `skills/implement/orchestration.md:394` to `:397` | A signer's framer writes its anchors as rows of a `| Pact | Clause | Hash |` table in `frame/design.md`. The exact shape is already the instruction |
| `CONTRIBUTING.md` *What a change to a gate must carry* | The pull request body states the direction: `seal pact` grades more tables, refuses more rows of them and more spellings of the token, and refuses nothing outside them. It also states a prompt budget of zero and what the work removes. The body is the orchestrator's |
| `skills/verify/scripts/pact_check.py#check` (`:744` to `:790`), `#first_table` (`:303`), `#row_cells` (`:505`), `#stray_rows` (`:531`), `#OUTSIDE_TABLE` (`:240`), read at `a5533a3d` | The code this changes. The `UNDECLARED` arm (`:766`) stays. The scan, its guard `if not table_refusals:` (`:780`) and the two functions it calls go. `first_table` is called twice, for the map (`:349`) and for the anchor table (`:753`), and by nothing outside `pact_check.py` |
| `hooks/lib/config.py#gfm_table` (`:1075`), `#table_cells` (`:949`), read | The walk matches a header by exact cells, after `table_cells` strips each one, so whitespace around a cell is already the same header. It is not edited: `first_table` hands it the header's cells as the frame writes them |

**Probes, executed at the first frame's base.** Each ran in a `git clone
--no-local` of the worktree at `28edee12`, under the scratch directory, and
the directory was removed before hand-back. They are carried from the first
frame and were not re-run for this reframe.

- **The pact code is the issue's.** `git diff --stat 5287dd42 28edee12` over
  `pact_check.py`, `hooks/lib/config.py`, `coordinates.py`,
  `tests/skills/test_pact_check.py` and `docs/the-pact.md` prints nothing;
  `tests/conftest.py` changed, with no line naming the pact
  (`git diff ... | grep -c -i pact` prints 0). So *seen red against
  `5287dd42`* and against `28edee12` are one test. The sealer re-ran both
  diffs (`guarantee.md`, *Claims re-run*).
- **The reprobe.** `python3 -I test_tmp_probe.py <clone> <dir>`: one pact
  repository, one signer declaring it, 26 frames, each with the hash
  `deadbeef` the pact does not hold. `check` exited 2. It printed:
  - graded `UNMATCHED`: the exact table (d01), the remote spelled
    `https://example.com/o/pact` (d02);
  - `REFUSED` at the row: a backticked `Pact` cell (d03), a `Clause` with no
    heading (d04), an upper-case hash (d05), and the row a blank line cut off
    (d06, one refusal for the frame plus the graded row above it);
  - `REFUSED` with `INLINE`: `pact:abc` (d17);
  - **nothing at all**: headers `| pact | clause | hash |` (d07),
    `| Pact | Clause | Hashes |` (d08), `| **Pact** | Clause | Hash |`
    (d09), `| Clause | Pact | Hash |` (d12), `| Pact | Clause | Hash | Note |`
    (d13), the table with no outer pipes (d14), header cells in code spans
    (d15), `| Pact | Clauses | Hash |` (d26), and an anchor row with no
    header above it (d24); rows naming `git@example.com:o/pakt.git` (d10)
    and `git@other.example.com:o/pact.git`, another host (d16); inline `PACT:abc` (d18),
    `Pact:abc` (d19), `pact: abc` (d20), `pact :abc` (d21) and
    `PACT:pact/"## A"@deadbeef` (d22); a table inside a fence (d11), a
    `| Repository | Role |` table naming the pact's remote (d23) and the
    label `**Pact:** the orders pact` (d25).
  The `READ` line counted 3 anchors (d01, d02, d06).
- **A space beside the colon is prose.** Over every `.md` file at `HEAD`,
  `v0.22.0`, `v0.23.0` and `v0.24.0` (`git grep -i -E` for `pact` before a
  colon, then three patterns over the lines found): the case-folded token
  with no space after the colon matched no line the exact token missed,
  except nine lines at `HEAD` and `v0.24.0` that quote R24's own near
  misses. A pattern allowing spaces beside the colon matched 6 lines more at
  `v0.22.0`, 1 at `v0.23.0` and 4 at `HEAD`, every one prose, such as *No
  command rewrites a pact: the line says*.
- **R24 at `c825fd2c`** (read, not run here:
  `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-5.md:52`):
  the reader before #913 graded and refused neither `PACT:` nor `pact: `. No
  release has graded either spelling.

**Read for this reframe, at `a5533a3d`.**

- `git grep -n "stray_rows\|row_cells\|OUTSIDE_TABLE"` outside `seal/threads`
  finds the three units in `pact_check.py` and `OUTSIDE_TABLE` once more in
  `tests/skills/test_pact_check.py` (`:91`, `:982`), and nowhere else
  (executed). `config.blocks` is read in `pact_check.py` by `row_cells` alone.
- `hooks/lib/routing.py:79` holds `BY_FRAMER = "framer"`, and
  `skills/code-review/scripts/chain_check.py#frame` refuses a `Reframed` line
  naming anyone else (executed, `git grep`). The `Reframed` line at this
  file's foot names `framer` for that reason.

## Scope

**In.**

1. **A row of the anchor table naming a pact the signer does not declare
   is refused at its line.** In `check`, a row of the anchor table whose
   `Pact` cell is one remote URL that matches none of the signer's declared
   remotes (`pacts`, compared normalised) is refused with `UNDECLARED`, at
   exit 2. A row naming another pact the signer declares is passed over as
   today, for that pact's `seal pact` to grade. Built in phase 1
   (`ce323fe9`) and kept: the declared list is a fact.
2. **The anchor table's header is read through one closed normalisation.**
   One function in `pact_check.py` takes a header cell and gives its key.
   - The key is the cell with one emphasis run removed where such a run
     wraps the whole cell, then case folded.
   - An emphasis run is `*` or `_`, one to three characters long. The same
     run opens and closes the cell, with no space just inside either run.
   - The run is removed once, so `**_Pact_**` keeps its inner run and is
     not the anchor header.
   - Whitespace around a cell is already stripped by `table_cells`, and the
     function adds nothing for it.
   - A code span, strikethrough, an HTML tag, an escaped delimiter, a
     plural, another word, another order or another width is outside the
     normalisation. Such a header is another table.

   A header whose cells' keys are those of `Pact`, `Clause` and `Hash`, in
   that order, is the anchor table. Its rows are graded and refused exactly
   as the exact header's are, so a row naming an undeclared remote under
   `| pact | clause | hash |` is refused `UNDECLARED`.
3. **`first_table` reads the anchor table by that key.** For the anchor
   table it finds the first line `config.unfenced` shows whose cells key to
   the anchor header. It hands that line's cells, as written, to
   `config.gfm_table`, so the walk is unchanged and its refusals quote the
   header as the frame writes it. Its second-header scan counts every
   further line whose cells key the same. So a second anchor table under
   another case or emphasis is refused as a second header. The machine-local
   map's header is read exactly, as today.
4. **The row scan is removed.** `stray_rows`, `row_cells`, the
   `OUTSIDE_TABLE` sentence and the guarded call in `check` that prints it
   go. A table under a header outside the normalisation, and a row no anchor
   table holds, are neither graded nor refused by `seal pact`.
5. **The inline token is read in any case, and a space beside its colon is
   a stated limit.** `INLINE_TOKEN` takes `re.IGNORECASE`, and `pact: abc`
   and `pact :abc` stay unread because prose writes the word before a colon
   and a space. Built in phase 2 (`063644e5`) and kept. Case folding the
   token is the same member as the header's case.
6. **The texts that state what a frame is read for.** `pact_check.py`'s
   docstring sections *What each frame is read for* and *Exit codes* are
   rewritten in place to items 1 to 5 (contract rule 19). The paragraph on
   the row scan goes, and with it the two limits it stated: the row that
   misses twice, and the line four columns in. Both were limits of the
   scan's reading of lines outside the table. With no scan, such a line is
   not read at all, so neither limit has anything left to describe. A
   double miss under a header inside the normalisation is no longer a
   miss: its rows are graded.
7. **The judgment of meaning for the rest goes to the proofer.** One
   sentence in `skills/code-review/SKILL.md` *Two stages, in order*, under
   stage 1, tells the proofer what to judge. Where the work item's
   `frame/design.md` holds a line that reads as meant for a pact anchor and
   that `seal pact` does not read, the line is a finding. Examples are a
   table under a plural or other wording, a row with no header, and a row
   outside the table. What `seal pact` reads is the shape `pact_check.py`'s
   docstring *What each frame is read for* states, against the `Pact` row
   of the repository's `seal/config.md`. The words and placement are the
   build's (`questions.md` W2).

**Where #1132's *Done when* is met.**

- **Bullet 1**, the inline token's near misses: met as built. `PACT:` and
  `Pact:` are refused at their line, and `pact: ` is a limit sentence in
  `docs/the-pact.md` by `## Rule changes`.
- **Bullet 2**, a header differing only by case, a plural or emphasis, is
  refused at its line. It is not met as written.
  - Case and emphasis are met by grading in code. The table is the anchor
    table, and each of its rows is graded or refused at its own line. The
    header line itself is not refused.
  - The plural is met by the proofer's judgment at the signer's review, not
    by a refusal at its line. `seal pact` reads it as another table.
  - This is the owner's answer to P1. The departure from the issue's
    wording is that answer, not an oversight.
- **Bullet 3**, a near-miss remote refused or reported.
  - Met in code for every row of the anchor table, under the exact header
    or one inside the normalisation, through `UNDECLARED`.
  - Under a header outside the normalisation it is met only by the
    proofer's judgment.
- **Bullet 4**, each case seen red against `5287dd42`.
  - Met for the phase 1 and phase 2 refusals, seen red against `28edee12`,
    which is `5287dd42` for this code.
  - Phase 3's cases are seen red against `a5533a3d`, the branch before this
    reframe. At `5287dd42` the same shapes printed nothing and exited 0, so
    each is red there too.

**Out, and whose.**

| Left out | Whose, and why |
|---|---|
| Code spans, strikethrough, HTML tags, nested or mixed emphasis runs, and escaped delimiters in the normalisation | Nobody's: each is outside what means the same by definition (*Grounding*, the rendering row), and a member added for it is the next grammar shape. A header written so is the proofer's to judge |
| Refusing a header outside the normalisation at its line, or refusing a row outside the anchor table by its cells | Nobody's: the row scan is removed (*Scope* item 4; `plan.md` A3, A14). Its catches are the proofer's |
| Normalising the machine-local map's, the `Signer` table's or `seal/config.md`'s header | Nobody's: each file is refused where it holds no such table (`hooks/lib/config.py#pact_signers`, `pact_check.py#path_map`), so a near-miss header there is already loud. #1132 names the anchor table only |
| Refusing `pact: ` or `pact :` | Nobody's: prose writes them (*Scope* item 5). The limit sentence is the issue's own alternative |
| Edit distance or similarity to the pact's remote | Nobody's: a threshold guesses from words (`plan.md` A5) |
| A proofer behaviour eval for the new sentence | Nobody's in this work item: the sentence is one instruction under a stage whose rule already names `evals/behaviour/proofer/rule-proofer-one-finding/`. A paid eval for a rare shape costs more than the shape. A later item opens one if a signer's review misses an anchor |
| A signer whose work item is routed `straight to the PR` | Nobody's: no proofer reads its frame. For a header outside the normalisation, the signer's `READ` line, which counts the anchors `seal pact` read, is the only sign. The `add` in `## Rule changes` states it |
| An anchor table inside an HTML comment, or below a fence nobody closed | A later item the owner opens: `config.unfenced` hides both, which is the line-liveness question of `docs/the-record-layout.md`, not a near miss, and #1132 does not name it |
| The walker's over-refusal of an indented code block below the anchor table | The orchestrator, for an issue (`gaps.md` *Not done*). It predates this work, and with the scan gone this work touches it nowhere |
| `docs/` | Not edited in this diff: `## Rule changes` |
| `skills/verify/scripts/deferral_check.py`, `tests/text/`, `agents/framer.md` and the `rule-framer-sharp-s` eval | The parallel work items #1123, #1127 and #1158. This work touches none of them |

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1, a remote the signer does not declare | Given a signer declaring only the pact, and a row of the anchor table whose `Pact` cell is `git@example.com:org/ordres-api.git` (one letter off), or the pact's path on another host, when `seal pact` runs, then each row is refused at its line with `UNDECLARED`, at exit 2 | built: two ids of `test_refuses_a_row_it_cannot_grade_at_its_line`, seen red against `28edee12` (phase 1; re-run by the sealer) |
| S2, another declared pact | Given a signer whose `Pact` row declares the pact and `git@example.com:org/billing.git`, and a row naming billing whatever its other cells hold, when `seal pact` runs at the pact, then the row is neither graded nor refused | built: `test_accepts_a_signer_citing_the_current_clause`, its signer config declaring the remotes its rows name |
| S3, a header inside the normalisation is the anchor table | Given a frame whose only table is headed by one member's spelling, over a row naming the pact's remote, a clause and its current hash, when `seal pact` runs, then the row is graded `OK`, the `READ` line counts it, and the run exits 0. The spellings: `| pact | clause | hash |`, `| PACT | CLAUSE | HASH |`, `| *Pact* | Clause | Hash |`, `| **Pact** | Clause | Hash |`, `| ***Pact*** | Clause | Hash |`, `| _Pact_ | Clause | Hash |`, `| __Pact__ | Clause | Hash |`, `| ___Pact___ | Clause | Hash |`, and `| **pact** | _CLAUSE_ | Hash |`, members together | one parametrised case, one id per spelling, seen red against `a5533a3d`, where the scan refuses each row `OUTSIDE_TABLE` at exit 2 |
| S4, the shape the seal could not decide | Given `| pact | clause | hash |` over a row naming `git@example.com:org/ordres-api.git`, a clause and a hash, under a signer declaring the pact alone, when `seal pact` runs, then the row is refused at its line with `UNDECLARED`, at exit 2 | a case or an id of its own, seen red against `a5533a3d`, where the passes case pins this row at exit 0. The row leaves the passes case |
| S5, a second anchor table by key | Given the anchor table, then `## More`, then a table headed `| pact | clause | hash |` with a row, when `seal pact` runs, then the frame is refused with the second-header sentence naming that header's line | an id of `test_refuses_an_anchor_row_nobody_reads`, in place of the scan's id `a near miss below the anchor table`; seen red against `a5533a3d`, where the row is refused `OUTSIDE_TABLE` instead |
| S6, a header outside the normalisation is not read | Given a frame with no anchor table holding, each under a heading of its own and below a blank line, tables headed `| Pact | Clause | Hashes |`, `| Pact | Clauses | Hash |`, `` | `Pact` | `Clause` | `Hash` | ``, `| ** Pact ** | Clause | Hash |`, `| ~~Pact~~ | Clause | Hash |` and `| **_Pact_** | Clause | Hash |`, each over a row naming the pact's remote, a clause and a hash, and that row once more with no header, when `seal pact` runs, then none is graded or refused, and the `READ` line does not count them | the passes case, these shapes in a frame of their own in place of frame z's indented rows; each seen red against `a5533a3d`, where the scan refuses it `OUTSIDE_TABLE` |
| S7, the walk's refusal of a cut-off row | Given the anchor table and the same row again below a blank line (d06), when `seal pact` runs, then the frame is refused with the walk's sentence | built: the id `a row under a blank line` of `test_refuses_an_anchor_row_nobody_reads`, kept. The count assertion phase 1 added to every id of that case goes with the scan it pinned (`plan.md` A11) |
| S8, the inline token in any case | Given `PACT:abc`, `Pact:abc` and `PACT:orders-api/"## A"@1a2b3c4d` in prose and in a table cell, when `seal pact` runs, then each is refused at its line with `INLINE`, at exit 2 | built: six ids of `test_refuses_the_inline_anchor_naming_the_row_to_write`, seen red against `28edee12` (phase 2; re-run by the sealer) |
| S9, the space limit | Given `pact: abc`, `pact :abc` and `Read the pact: it is short.`, when `seal pact` runs, then none is refused | built: the passes case |
| S10, the words a person reads | Every sentence `seal pact` prints is pinned by its case (contract rule 14) and passes `tests/behaviour/test_one_word_one_meaning.py`; no sentence names a refusal it no longer makes | that module, and `git grep -n -i "no anchor table holds\|misses twice\|four columns"` over `skills/verify/scripts/` and `tests/skills/` printing nothing |
| S11, the proofer is told | Given a signer's work item whose `frame/design.md` writes an anchor under `| Pact | Clause | Hashes |`, when the proofer reviews it, then stage 1 names the line as a finding | read: the sentence in `skills/code-review/SKILL.md` stage 1, by round 1 of this work item's review. No eval (*Out*) |
| S12, the rule changes parse | `## Rule changes` below is read by `skills/settle/scripts/rule_changes.py` with no refusal | `chain-check` at the pull request reads it through that reader |

## Data & interfaces

One refusal sentence stays new in `pact_check.py`, `UNDECLARED`, printed as
`REFUSED <signer> <frame>:<line> — <sentence>`, in `EXIT_TWO` like every
`REFUSED`. Its words are those phase 1 wrote (`trail/phases/phase-1.md`, W1).
`OUTSIDE_TABLE` goes, from the script and from the test module's copy.

One new function gives a header cell's key, as *Scope* item 2 states. Its
name is the build's. Its comment lists the members and the shapes left out,
so the closed list is read where it is applied.

`first_table` gains one keyword argument through which the anchor call asks
for the key. The map call leaves it out and is read exactly. With the key,
`first_table` passes the matched header's cells as written to
`config.gfm_table`. Its second-header sentence still names the anchor
header as `| Pact | Clause | Hash |`, at the line of the further header. A
walk refusal quotes the header as the frame writes it, for example "has a
`| pact | clause | hash |` header directly under ...".

`INLINE_TOKEN` is
`re.compile(r"(?<![A-Za-z0-9_.@/-])pact:(?=\S)", re.IGNORECASE)`, as built.
`stray_rows` and `row_cells` are deleted, and `declared_remotes` stays for
the `UNDECLARED` arm.

## Rule changes

- change
  file: docs/the-pact.md
  section: The pact anchor
  from: A row naming another pact is passed over.
  to: A row naming another pact the signer's `Pact` row declares is passed
    over, for that pact's `seal pact` to grade.
- change
  file: docs/the-pact.md
  section: The pact anchor
  from: **`seal pact` refuses, at exit 2, a row it cannot grade and every
    `pact:` token in a signer's frame.** A row whose `Pact` cell is not one
    remote URL names no pact anybody can tell, and a row naming this pact
    whose `Clause` cell does not open with a heading, or whose `Hash` cell
    is not eight lowercase hex digits, grades nothing; each is refused at
    its line. A `pact:` token outside a fenced code block is the inline
    anchor `seal pact` read through 0.23.x, and it is refused at its line
    with the row to write in its place.
  to: **`seal pact` refuses, at exit 2, a row of the anchor table it cannot
    grade and every `pact:` token in a signer's frame.** A row whose `Pact`
    cell is not one remote URL names no pact anybody can tell, and a row
    naming this pact whose `Clause` cell does not open with a heading, or
    whose `Hash` cell is not eight lowercase hex digits, grades nothing;
    each is refused at its line. A row whose `Pact` cell names a pact the
    signer's `Pact` row does not declare, such as a remote one letter off
    the pact's, is refused at its line, because no `seal pact` grades it:
    another pact's reports the signer `ONE-SIDED` and reads none of its
    frames. A `pact:` token outside a fenced code block, in any case, is the
    inline anchor `seal pact` read through 0.23.x, and it is refused at its
    line with the row to write in its place. A token with a space beside
    its colon is not read: prose writes the word before a colon and a
    space, and no release read that spelling as an anchor.
- add
  file: docs/the-pact.md
  section: The pact anchor
  to: **The anchor table is the table whose header means
    `| Pact | Clause | Hash |`, and one closed normalisation decides that.**
    Each header cell is compared case folded, after one emphasis run is
    removed where it wraps the whole cell: `*` or `_`, one to three long,
    the same run on both sides and no space just inside it. So
    `| pact | clause | hash |` and `| **Pact** | Clause | Hash |` head the
    anchor table, and its rows are graded and refused as the exact
    header's are. GitHub renders a header cell bold, and the same letters
    in another case are the same word, so a script that answered that these
    differ would report a signer citing nothing where it cites a clause.
    Nothing else is in the normalisation. A code span is a mention of the
    word rather than a use, strikethrough marks it deleted, and a plural,
    another word, another order or another width is another table. A
    second header the normalisation reads is refused as a second anchor
    table.
    check: tests/skills/test_pact_check.py
- add
  file: docs/the-pact.md
  section: What this does not see
  to: **`seal pact` reads the anchor table and nothing else in a frame.** A
    table under a header outside the normalisation, such as
    `| Pact | Clause | Hashes |`, and a row no anchor table holds are
    neither graded nor refused, and the signer's `READ` line does not count
    them. Whether such a line was meant as an anchor is a judgment of
    meaning, and a grammar written to make it finds a new shape at every
    reading. So the proofer makes it, at stage 1 of the signer's own
    review. It reads the work item's `frame/design.md` against the shape
    `seal pact` reads and the signer's `Pact` row, and a line meant as an
    anchor that `seal pact` does not read is a finding. A signer whose work
    item goes straight to the pull request has no proofer, and there the
    `READ` line's count is the only sign.
    check: tests/skills/test_pact_check.py

## Removes

The first three rows leave the base's tree. The last four name units phase 1
added and this reframe's phase 3 removes. The base never held them, so the
review reads those four against phase 3's diff, not against the base.

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The pass of a row whose `Pact` cell names a pact the signer does not declare | `skills/verify/scripts/pact_check.py#check`, the `if named != ours: continue` arm of the base | Refused at its line (*Scope* item 1); a row naming a declared pact is still passed over. Removed in phase 1 |
| The docstring's statement that a row naming another pact is passed over, and its list of what a frame is refused for | `skills/verify/scripts/pact_check.py`, the module docstring *What each frame is read for* and *Exit codes* | Rewritten in place to the new rules, in phase 1 and again in phase 3 |
| The pin that an undeclared remote's row passes | `tests/skills/test_pact_check.py#Test_check`, `test_accepts_a_signer_citing_the_current_clause`, the rows naming `git@example.com:org/billing.git` and `https://example.com/org/orders-api-legacy` under a signer config that declares neither | The case declares both remotes in the signer's `Pact` row (S2), and S1's ids pin the undeclared shape. Removed in phase 1 |
| The row scan and its line reader, built in phase 1 | `skills/verify/scripts/pact_check.py#stray_rows`, `#row_cells`, `#OUTSIDE_TABLE`, and in `#check` the `if not table_refusals:` block that calls `stray_rows` | The normalisation reads the headers that mean the same (*Scope* items 2 and 3). The judgment the scan made for every other header is the proofer's (*Scope* item 7) |
| The docstring paragraph on the row scan, with its two limits, the row that misses twice and the line four columns in | `skills/verify/scripts/pact_check.py`, *What each frame is read for*, its second paragraph, and the `Exit codes` words "a row no anchor table holds" | With no scan there is nothing for either limit to describe (*Scope* item 6) |
| The cases that pin the scan | `tests/skills/test_pact_check.py`: `OUTSIDE_TABLE`'s copy; `test_refuses_an_anchor_row_no_anchor_table_holds` with its eleven ids; the `out.count(...) == 1` assertion and its docstring sentence in `test_refuses_an_anchor_row_nobody_reads`; frame z's four indented rows; the `| Repository | Role |` table; the passes case's `| pact | clause | hash |` row over `ordres-api`; and the passes-case docstring's clauses on indented rows and on a row that misses twice | S3 to S6 replace them. The ids for lower case, emphasis and the near miss below the anchor table become S3's and S5's. The plural, code-span and headerless ids become S6's shapes, pinned as not read. The `ordres-api` row becomes S4. The id `a row under a blank line` stays as S7 |
| The changelog sentence and the gaps rows that state the scan | `changelog.md`, `gaps.md` *Where spec and implementation diverged*, the S5 rows | Rewritten by their owner, the orchestrator, to the reframed rule (`plan.md` *Operational impact*) |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-29 by framer, before the build.
Reframed 2026-10-29 by framer, after round 4.
