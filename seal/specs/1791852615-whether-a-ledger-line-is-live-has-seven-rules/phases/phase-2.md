# 1791852615-whether-a-ledger-line-is-live-has-seven-rules — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | e080a995 |
| Ran by | unknown — the spawn prompt named the agent, `smith`, and not the model; the orchestrator fills this row |

## What this phase was asked

Build phase 2 of `plan.md`: a `Reads:` line and one consequence sentence in
each of the seven docstrings, starting from `spec.md` §*Data & interfaces*
and settled at each unit; the seven census lines removed; every drifted
released row answered by `evidence-check --reverify --into` with each row
read; the probe re-deriving the issue's two figures, deleted after; the
before and after counts of S6. The spawn added: open 1790645290's `spec.md`
before editing the docstrings of `hooks/config.py#hidden_lines` and the
rider check's `quoted_lines`.

**Direction.** Seven units' hashes move and no verdict moves: the edits are
docstring lines, and the counts below say so. **Prompt budget.** Zero.

## What this phase found

**Three declarations moved from the frame's proposal**, each settled at the
unit as `questions.md` D8 asks:

| Unit | Frame proposed | Declared | Why |
|---|---|---|---|
| the checker's `quoted_lines` | `owned` | `guess` | `unquoted` hands it the lines of every `.md` file an anchor names (`markdown_lines`, `heading_slugs`, `citation_for`), not only ledgers, and a unit declares the weakest class of what its callers hand it |
| `readable` | `owned`, `passed` | `guess`, `mixed` | it reads the same session-written records `claim_lines` reads, which the frame declares `guess`; and its callers end two ways: `check_text`, `chain_check.py`, `round_record.py` and `survivor_check.py#exemptions` refuse a table it hid, `release_seal.py` names the record unread, while `broad_gate.py#sealed_record` feeds a label that "never stops a sealed run". The frame's own cell, "every record reader refuses an absent table", is `refused`, so `passed` was not its reading either |
| `hidden_lines` | as framed | as framed, with the sentence saying "where the older reading would not take it" | phase 1's finding: a row below a comment opener nobody closed still declares (1790645290 §*A construct that never closes is not a construct*) |

The other four went in as framed: `claim_lines` `guess`/`passed`,
`anchored_rows` `owned`/`refused`, the rider check's `quoted_lines`
`guess`/`refused`, `live_lines` `guess`/`mixed` (Q5's default, the prose
naming the fold and `settle` as refusing and the changelog gather and the
ledger fold as passing).

**S3, seen red.** With the seven `Reads:` lines in and the census untouched,
`tests/test_a_reader_declares_its_input_class.py` failed naming each of the
seven census lines, "the unit declares now. Remove the line" (executed).
With the lines removed it passed: 76 cases. The census went from 1,581 lines
to 1,574.

**S5 and S6, executed.** All three commands' outputs were read in full.

| Command | Base (2e3e2670's tree) | After the declarations | After the re-reads |
|---|---|---|---|
| `evidence-check --strict .` ledger total | 8,426 ok · 0 drifted, exit 0 | 8,408 ok · 18 drifted, exit 2 | 8,465 ok · 0 drifted, exit 0 |
| its records arm | 0 read · 100 unread · 18 names · 0 refused | the same | 1 read · 99 unread · 157 names · 0 refused |
| `settle --released-at origin/main` survey | — | byte-identical before and after the declarations | — |
| `settle.py#anchored_rows` over all 100 work items | 0 rows | — | 0 rows |

The 18 drifted coordinates are the seven units and
`docs/the-evidence-ledger.md` §*The fold, and what tells it from a
deletion*, across 17 released rows; every pre-existing anchor reads `ok`
again after the re-reads, and the 39 anchors added are the 17 citing rows'.
The records arm's move is this work item entering it once its fragment
existed: no name refused, and the `## Removes` rows read as gone (none is
reported `STANDING`). The base column's records arm and the survey's "before"
were taken at the base tree and at 78237f6a respectively; the base export has
no `.git`, so the survey, which needs history, ran on the branch before the
docstrings changed.

**Every drifted row was read before `--into` wrote its citing row.** None of
the 17 claims rests on a docstring sentence: R11, G3, A4, P2-1, P2-3, P4-1,
P4-2, P1-4, P3-1, P5-1, G1, L8, C2, K12, K16, R5 and T2 each state behaviour
the edits did not touch, and five of them (R11, P2-1, A4, P3-1, P5-1) are
also cells of phase 1's table. C2's claim about the fold section, that
`fold-check` lists no document over the ceiling, was executed again: `0
listed over it`, exit 0. `correction-check --range
origin/release/v0.21.1..HEAD` exit 0, and `git diff --stat
origin/release/v0.21.1 -- seal/releases seal/ledger.md` is empty.

**S7, the two figures, executed at a0e8c214** with a `test_tmp_*` probe,
deleted after. The ledger files are unchanged from 321e9de1. Over
`seal/ledger.md` and the 44 files under `seal/releases/`, 3,242 table lines
of which 2,846 carry an anchor:

- the checker's `quoted_lines` skips 0 rows and `live_lines` parks 0, so
  they agree on every row;
- `readable` would blank 46 rows, every one anchored, in eight files:
  `0.7.0` 1, `0.8.1` 8, `0.9.1` 3, `0.10.0` 10, `0.13.0` 2, `0.15.0` 6,
  `0.15.3` 12, `0.16.0` 4.

Both match #867's figures, which `spec.md`'s Grounding labelled read.

**Per-reader modules, executed.** The thirteen modules `plan.md`
§*Technical context* names and the text hygiene ones passed, 1,315 cases,
with two failures in the first run. One was this work item's own
`overview.md`, which quoted a comment opener inside backticks in a table
cell: `readable` blanked everything below it, so `unverified-check` found no
`## Not verified` section. That is the third answer working as stated on the
very record that states it; the cell now says "comment opener" in words. The
other was
`tests/test_settle_reads_before_it_removes.py::test_no_row_of_this_repositorys_ledger_anchors_inside_a_work_item`
running 117 s against the suite's 90 s ceiling; run alone with
`SPECSEAL_CASE_CEILING_S=300` it passed, in 153 s. Whether the base is over
the ceiling too was not measured, and it goes to `overview.md`.

**One mistake in how a command was spelled.** The commit that added the
eighth shape (78237f6a) was made in one call as `cd <worktree> && git add …
&& git -C <worktree> commit …`, which the spawn prompt forbids. It went
through; every later commit is a `git -C` command of its own.
