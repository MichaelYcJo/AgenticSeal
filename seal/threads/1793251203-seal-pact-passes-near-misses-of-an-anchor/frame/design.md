# Design: 1793251203-seal-pact-passes-near-misses-of-an-anchor

Issue #1132, row R24 of #956's audit. `seal pact` reads a signer's pact
anchors from the `| Pact | Clause | Hash |` table of each `frame/design.md`,
and refuses the inline `pact:` token that table replaced. Several near misses
of both are neither graded nor refused, so a signer that writes one is
reported as citing nothing. This work makes each near miss the issue names,
and the rest of its class, either refused at its line or stated as a limit.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `docs/the-pact.md` *The pact anchor*, as the unsettled design `seal/threads/1793169127-pact-check-reads-the-retired-grammar/frame/design.md` `## Rule changes` items 2 and 3 state it (#913, merged at `7da1a77e`) | The policy in force. A row naming another pact is passed over; a row it cannot grade and every `pact:` token are refused at exit 2. `## Rule changes` below quotes that text as its `from:` |
| `seal/threads/1793169127-pact-check-reads-the-retired-grammar/frame/questions.md` Q1 and `frame/plan.md` A9 to A11 | The inline form is refused, not graded and not passed over. That decision is not reargued here; this work widens which spellings of the token it reaches |
| `docs/the-record-layout.md` *Whether a line is live is asked by what the line does*, first bullet | A line that holds an anchor is read on doubt and the wrong answer is loud: exit 2, answered by an edit. So each near miss this work reads is refused, not reported in no exit class |
| `CLAUDE.md` *The rule a mechanism is kept against*: a check gates only a fact it reads, and a reading guessed from words is a report | No list of header spellings and no edit distance to the pact's remote. Each new refusal reads a fact: the remotes the signer's `Pact` row declares, and the cell shapes `seal pact` already judges (`pact_check.py#one_remote`, `#heading_parts`) |
| `CLAUDE.md` *Repo rule: text an agent or a check reads has one reading*, and `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* | A near miss is refused at its line rather than passed in silence |
| `skills/settle/SKILL.md` *Rule changes*, the `## Rule changes` heading rule | The tree's precedent for a near miss of a fixed spelling: the same letters, case folded, are refused; other letters are another thing. It grounds case folding the `pact:` token |
| `CONTRIBUTING.md` *What a change to a gate must carry* | The pull request body states the direction (`seal pact` refuses more), a prompt budget of zero, and what the work removes. The body is the orchestrator's |
| `skills/verify/scripts/pact_check.py#check` (`:524` to `:707`), `#first_table` (`:267`), `#INLINE_TOKEN` (`:194`), read at `28edee12` | The code this changes. `check` drops the walk's "holds no" refusal (`:659` to `:661`), passes over a row whose normalised `Pact` cell is not this pact (`:670`), and scans `unquoted` text for `INLINE_TOKEN` (`:683` to `:686`). `pacts`, the signer's declared remotes as `(as written, normalised)`, is already in scope at `:636` |
| `hooks/lib/config.py#gfm_table` (`:1075`), `#table_cells` (`:949`), `#unfenced` (`:239`), read | The walk matches a header by exact cells, after `table_cells` strips each one. A row needs its outer pipes (`TABLE_ROW`, `:940`) |

**Probes, executed at this frame's base.** Each ran in a `git clone
--no-local` of the worktree at `28edee12`, under the scratch directory, and
the directory was removed before hand-back.

- **The pact code is the issue's.** `git diff --stat 5287dd42 28edee12` over
  `pact_check.py`, `hooks/lib/config.py`, `coordinates.py`,
  `tests/skills/test_pact_check.py` and `docs/the-pact.md` prints nothing;
  `tests/conftest.py` changed, with no line naming the pact
  (`git diff ... | grep -c -i pact` prints 0). So *seen red against
  `5287dd42`* and against `28edee12` are one test.
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
- **A bare remote beside a heading cell is an anchor's shape only.** Over
  every table line of `seal/` markdown at the same four revisions (4,516
  lines at `HEAD`, 17,011 at `v0.22.0`), no row held both a cell that is a
  bare remote URL and a cell opening with `#`. This repository signs no
  pact, so the figure says no other table here takes that shape; it says
  nothing about a signer's own tables.
- **R24 at `c825fd2c`** (read, not run here:
  `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-5.md:52`):
  the reader before #913 graded and refused neither `PACT:` nor `pact: `. No
  release has graded either spelling.

## Scope

**In.**

1. **A row naming a pact the signer does not declare is refused at its
   line.** In `check`, a row of the anchor table whose `Pact` cell is one
   remote URL that matches none of the signer's declared remotes (`pacts`,
   compared normalised) is refused, at exit 2. A row naming another pact
   the signer declares is passed over as today, for that pact's
   `seal pact` to grade. This is the class of d10 and d16. It replaces a
   near-miss test, because the declared list is a fact and *one letter off*
   is a guess. Another pact's `seal pact` reports such a signer
   `ONE-SIDED` rather than reading its frames (`pact_check.py:639` to
   `:649`), so nothing graded these rows before.
2. **A row outside the anchor table that names a declared pact and a
   clause is refused at its line.** After the walk, `check` reads every
   line `config.unfenced` shows that is not a row the walk returned. Where
   the line splits into cells (`config.table_cells`, a line without its
   outer pipes given them), one cell is one remote URL matching a declared
   remote and another cell opens with a heading (`heading_parts`), the line
   is refused at exit 2. This covers every header spelling the probe found
   silent (d07, d08, d09, d12, d13, d14, d15, d26) and a row with no header
   (d24), because it reads the row and not the header's words. A table
   naming the pact's remote with no heading cell, such as a list of
   repositories (d23), is not refused. The scan runs only where the walk
   refused nothing, so a row the walk's refusal already names (d06) is not
   refused twice; once that refusal is fixed, the next run reads the rest.
3. **The inline token is read in any case.** `INLINE_TOKEN` takes
   `re.IGNORECASE`, so `PACT:abc`, `Pact:abc` and `PACT:pact/"## A"@deadbeef`
   (d18, d19, d22) are refused at their line with the `INLINE` sentence. The
   pattern stays one pattern, still with a non-space after the colon and
   the same characters barred before it. Its comment says so.
4. **A token with a space beside its colon is a limit, stated.** `pact: abc`
   and `pact :abc` (d20, d21) stay unread. Prose writes the word before a
   colon and a space (the probe above), and no release graded that spelling.
   The sentence goes into `docs/the-pact.md` *The pact anchor* by
   `## Rule changes`, and into `pact_check.py`'s docstring. This is the
   issue's second way to meet its first *Done when* bullet, for those two
   spellings only.
5. **The texts that state what a frame is read for.** `pact_check.py`'s
   docstring sections *What each frame is read for* and *Exit codes*, and
   the comment above `INLINE_TOKEN`, are rewritten in place to the new
   rules (contract rule 19).

**Out, and whose.**

| Left out | Whose, and why |
|---|---|
| Refusing `pact: ` or `pact :` | Nobody's: prose writes them (*Scope* item 4). The limit sentence is the issue's own alternative |
| A row that misses twice, such as a near-miss header over a row whose `Pact` cell is backticked or one letter off, or over a row whose `Clause` cell has no heading | Nobody's: it names no declared remote, or no clause, so it is no anchor's shape a fact can tell. Each miss alone is refused. `## Rule changes` adds the limit to *What this does not see* |
| Edit distance or similarity to the pact's remote, and a list of header spellings | Nobody's: each guesses from words (`plan.md` A1, A2, A5) |
| An anchor table inside an HTML comment, or below a fence nobody closed | A later item the owner opens: `config.unfenced` hides both, which is the line-liveness question of `docs/the-record-layout.md`, not a near miss, and #1132 does not name it |
| The `Signer` table's and the machine-local map's header near misses | Nobody's: each file is refused where it holds no such table (`hooks/lib/config.py#pact_signers`, `pact_check.py#path_map`), so a near-miss header there is already loud |
| `docs/` | Not edited in this diff: `## Rule changes` |
| `skills/verify/scripts/deferral_check.py`, `tests/text/`, `agents/framer.md` and the `rule-framer-sharp-s` eval | The parallel work items #1123, #1127 and #1158. This work touches none of them |

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1, a remote the signer does not declare | Given a signer declaring only the pact, and an anchor row whose `Pact` cell is `git@example.com:org/ordres-api.git` (one letter off), or the pact's path on another host, when `seal pact` runs, then each row is refused at its line with the new sentence, at exit 2 | a case in `tests/skills/test_pact_check.py` *Test_check*, both shapes, seen red against `28edee12`, where each row is passed over and the run exits 0 |
| S2, another declared pact | Given a signer whose `Pact` row declares the pact and `git@example.com:org/billing.git`, and a row naming billing whatever its other cells hold, when `seal pact` runs at the pact, then the row is neither graded nor refused | `test_accepts_a_signer_citing_the_current_clause`, its signer config rewritten to declare the other remotes its rows name |
| S3, a row no anchor table holds | Given a row naming the pact and `## Order response shape` under each header d07, d08, d09, d12, d13, d14, d15 and d26 of the probe, and with no header (d24), when `seal pact` runs, then the row is refused at its own line with the new sentence, at exit 2 | one parametrised case, one id per shape, seen red against `28edee12`, where each frame prints nothing |
| S4, what the row scan leaves alone | Given a table headed `Repository` and `Role` naming the pact's remote, a table inside a closed fence, the anchor table above a policy table, and a frame with no table, when `seal pact` runs, then none of them is refused | the passes case above, extended with the repositories table; `test_accepts_an_anchor_table_above_another_table_in_its_section` unchanged |
| S5, one refusal per row | Given the anchor table and the same row again below a blank line (d06), when `seal pact` runs, then the frame prints the walk's one refusal and no second refusal for that row | a case in *Test_check* counting the `REFUSED` lines for the frame |
| S6, the inline token in any case | Given `PACT:abc`, `Pact:abc` and `PACT:orders-api/"## A"@1a2b3c4d` in prose and in a table cell, when `seal pact` runs, then each is refused at its line with `INLINE`, at exit 2 | the existing `test_refuses_the_inline_anchor_naming_the_row_to_write`, new ids, each seen red against `28edee12` |
| S7, the limit | Given `pact: abc`, `pact :abc` and `Read the pact: it is short.`, when `seal pact` runs, then none is refused | the passes case, which already holds the third |
| S8, the words a person reads | Every new sentence `seal pact` prints is pinned by its case (contract rule 14) and passes `tests/behaviour/test_one_word_one_meaning.py` | that module |
| S9, the rule changes parse | `## Rule changes` below is read by `skills/settle/scripts/rule_changes.py` with no refusal | `chain-check` at the pull request reads it through that reader |

## Data & interfaces

Two new refusal sentences in `pact_check.py`, each printed as
`REFUSED <signer> <frame>:<line> — <sentence>`, in `EXIT_TWO` like every
`REFUSED`. The names and the exact words are the build's, pinned by S1's
and S3's cases. What each must say:

- **The undeclared remote.** The `Pact` cell, as written, names a pact this
  signer's `seal/config.md` does not declare in its `Pact` row, so no
  `seal pact` grades the row. The remedy: write the origin URL of a pact the
  row declares, or add the pact to the `Pact` row.
- **The row no anchor table holds.** The row names a pact and a clause, and
  no `| Pact | Clause | Hash |` table holds it, so nothing grades it. The
  remedy: write it as a row of a table under that header, spelt exactly so.

`INLINE_TOKEN` becomes
`re.compile(r"(?<![A-Za-z0-9_.@/-])pact:(?=\S)", re.IGNORECASE)`. The
`INLINE` sentence is unchanged. No function changes its signature;
`check` reads `pacts` where it already holds it.

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
  to: **`seal pact` refuses, at exit 2, a row it cannot grade, a row no
    anchor table holds, and every `pact:` token in a signer's frame.** A row
    whose `Pact` cell is not one remote URL names no pact anybody can tell,
    and a row naming this pact whose `Clause` cell does not open with a
    heading, or whose `Hash` cell is not eight lowercase hex digits, grades
    nothing; each is refused at its line. A row whose `Pact` cell names a
    pact the signer's `Pact` row does not declare, such as a remote one
    letter off the pact's, is refused at its line, because no `seal pact`
    grades it. A row outside the anchor table that names a pact the signer
    declares in one cell and a heading path in another is refused at its
    line, whatever header it stands under, or with none, because the walk
    reads the `| Pact | Clause | Hash |` header alone. A `pact:` token
    outside a fenced code block, in any case, is the inline anchor
    `seal pact` read through 0.23.x, and it is refused at its line with the
    row to write in its place. A token with a space beside its colon is not
    read: prose writes the word before a colon and a space, and no release
    read that spelling as an anchor.
- add
  file: docs/the-pact.md
  section: What this does not see
  to: **A row that misses twice is not read.** A row outside the anchor
    table whose `Pact` cell is also a near miss, written in backticks or one
    letter off a declared remote, or whose `Clause` cell holds no heading,
    has no anchor's shape a fact can tell, and `seal pact` passes it over.
    Each miss alone is refused. A line four columns in, a tab counting to
    the next multiple of four, is read as no row: below a blank line it is
    an indented code block, and right under a paragraph line, where GitHub
    renders it as text, it is a row with no header that is also indented, a
    row that misses twice.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The pass of a row whose `Pact` cell names a pact the signer does not declare | `skills/verify/scripts/pact_check.py#check`, the `if named != ours: continue` arm | Refused at its line (*Scope* item 1); a row naming a declared pact is still passed over |
| The docstring's statement that a row naming another pact is passed over, and its list of what a frame is refused for | `skills/verify/scripts/pact_check.py`, the module docstring *What each frame is read for* and *Exit codes* | Rewritten in place to the new rules |
| The pin that an undeclared remote's row passes | `tests/skills/test_pact_check.py#Test_check`, `test_accepts_a_signer_citing_the_current_clause`, the rows naming `git@example.com:org/billing.git` and `https://example.com/org/orders-api-legacy` under a signer config that declares neither | The case declares both remotes in the signer's `Pact` row (S2), and S1's case pins the undeclared shape |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-29 by framer, before the build.
