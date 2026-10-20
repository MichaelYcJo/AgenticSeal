# 1791384155-a-round-record-cell-has-one-reader — overview

📋 implement applied
· spec:     this item's `spec.md` (J1–J5, S1–S14, §*Data & interfaces*), `plan.md`, `questions.md`; `docs/round-record-spec.md` §*`Pass` has to be checked*, §*The depth in `New units`*, §*A fix of a fix*, §*What `close` derives*; `docs/review-chain-spec.md` §*The reopening — one, and then the run is capped*; the owner's review in #834's `handoff.md` §*Review of the run*
· evidence: `seal/ledger/1791384155-a-round-record-cell-has-one-reader.md` — rows H1, H3–H6, `Corrected ·` N9, C3, A8, S7, B1, F9, R11, R3, and the `Re-read ·` rows each phase owed; sibling fragments' rows re-stamped in place where this work drifted them, and #860's `Corrected · A1` corrected in place
· verified: executed per phase (`phases/phase-N.md`); the full suite is the sealer's

## Why this work exists

Five judgments about a round record were each read by two to four scripts
that disagreed about the same cell; each now has one reader in
`chain_check.py`, so the gate, the generator, the broad gate's panel and the
release seal cannot give one cell two meanings.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The plan was written before #860, #837, #869 and #867 landed | `plan.md` §*Seams* names them as landing first / every phase was built on the release branch as merged at ad447367 | the tree as it is | the orchestrator's spawn: "Build each phase on the tree as it now is … record every divergence from the plan in `overview.md`" |
| The home reader is three functions, not two | J2: "a function deferred_home beside `verdict_of`, and issue_of over its answer" / `deferred_parts` returns the home and the note, `deferred_home` is its first half, `issue_of` reads the home | three | J2 also says the fix table takes "the home, with everything after the cut going to the note"; a second cut inside `fix_table` would be the copy this work removes |
| The layer the home's text loses | J2: "with the same two layers taken off (`EMPHASIS`, a trailing stop)" / `HOME_MARKS` (backticks, asterisks, an edge underscore) | `HOME_MARKS` | `EMPHASIS` removes every underscore, so `tests/test_x.py` read as `tests/testx.py`, which round 2 of #666 had fixed on the panel; the word itself is still matched through `EMPHASIS` by `verdict_of` |
| S4's Grounds cell | S4: "the Grounds cell `#854 — the run is capped; <reviewer's grounds>`" with a third cell `why` / `#854 — the run is capped — why; executed` | the third cell kept | the fix table's third cell is the fix pass's reasoning, which #391 part 1 made the generator keep; the spec's expected value dropped it silently |
| A bare `deferred` beside a home in the third cell | spec silent / the third cell is read as if the word stood before it | through `deferred_parts` | it used to write the whole third cell into the Verdict cell, the shape S4 removes for the other arm |
| The release seal's S10 fixture | spec silent / `**deferred** #13, #14` became two cells | changed | `#13, #14` is not a home `issue_of` reads as an issue, and keeping the case's three issues needs one per cell |
| `landings`' flag | J3 names only `depth_two` as the wide reader's caller / `landings` reached `path_forms` through it with `paths_only=True` | `landings` calls `path_forms` directly | the flag chose between two readers, and one of them left |
| A comment in `evidence_check.py` | spec silent / it named one of the five patterns as a second reader of the same shape | reworded | §12: the sentence was false once the pattern left |
| The suite's pull request | spec silent; J4 says the population with no payload and no `gh` that answers now exits 1 / the suite is that population (logged out, #510), 176 cases failed | a stub `gh` in `tests/conftest.py`; since round 1's fix pass its default is the *unknown* answer, and a case that means a draft or a ready pull request says so with `gh_answers` (ten helpers that meant ready now say ready) | no case reaches a live `gh` for the question, and no case is moved to a state its name does not state (round 1's 🟡 2) |
| An unseen pull request (round 1's 🟡 1) | J4 and the policy table: no payload and no `gh` answer is `unknown`, judged as **ready**, and `new`/`close` exit 1 / read as unknown, not judged as ready, the line naming every source tried; a payload that cannot answer stays ready | unknown | the orchestrator's direction for round 1, against the owner's review of the run (observe, do not predict): ready was a guess about a state nobody observed, and it failed a correct mid-run record before the draft opens, on a `stop before the pull request` route and with no `gh`. CI always has GitHub's payload and decides; `docs/round-record-spec.md` §*`Pass` has to be checked* says so. The route's own reading is `questions.md` Q1 |
| How `gh` is run | J4: "the exact call pull_request_is_ready makes today" / the path `shutil.which` found, not the bare name | the found path | a `gh.cmd` on Windows is found by `which` and not by a process call naming `gh` |
| `--sealing`'s reach | J4: "the `Broad gate` arm of the last record" / also the direct `broad-gate.md` home | both homes | the gate writes the cell into whichever home `seal` uses, and the draft payload excused both before |
| The environment-leak case (W2) | a failure to re-pin / the judgment's source | the source | under `--sealing` the leaked payload fails nothing; the kept output still shows which pull request judged the fixture |
| S10's red | S10: "red with either caller's old loop restored" / red against breaks of `floor_walks` | `floor_walks` | the old loops agreed by construction, so restoring one moves no answer; a break of the shared walk moves both |
| `cut_runs`' answer | J5: "the `Fix of a fix` counts in round order → the runs" / the indices a run is cut after | indices | `current_run` also names the `second` that stopped the run before |
| The gate's per-record readers of the reopening and of a fix | spec silent / removed with the loops | removed | no caller was left; four released rows re-pointed by `Corrected ·` rows |
| Phase 5's commit | a phase closes on its own commit / e682fe84 is the orchestrator's `wip:` commit of the staged phase, made at the machine move | closed there, not rewritten | the orchestrator asked that the `wip:` commit stay; the resumed session re-ran the phase's modules, lint, the chain check and `evidence-check` on it |
| Where a doubled field row fails | J5: "the duplicate error in `check_round`" / `doubled_fields` on every record; the box in `check_round` | every record | `check_round` reads the last record alone, and an earlier record's doubled row would reach its arms as an absent row |
| `field_index` | J5: under one count with `field` / its own line walk, same one-row rule | kept | it needs the line index it replaces, which the table rows cannot give |
| The document sentence | phase 6: "by replacement of the sentence that says the first wins where one does" / no such sentence existed; §*What `close` derives* gained one sentence in place of two clauses | that paragraph | the doubled-close paragraph is where the record's duplicates were already spoken of, and the document is at 998 of 1,000 lines |
| The panel's ASCII | spec silent / the home is ASCII-encoded in `rounds_rows`, not in the reader | in the panel | the letter twin maps only the owner's characters; the gate and the release seal want the home as written |

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck at this branch's head | #890, merged with lint and the suite green on the ubuntu, macOS and Windows legs; the repository configures no typecheck |
| closed The suite's `gh.cmd` stub and the check running `gh` at the path `which` found, on Windows: read and pinned by an in-process case, never run on Windows here | #997's `windows-latest` leg ran the suite green |

## Not done

- **Nothing was left out under the owner's review of 2026-10-08.** Every
  reader this work added or changed reads a format a writer in this
  repository owns — the round record's cells, the verdict words, `close`'s
  prefix and joins, the field and box shapes `new` writes — or observes a
  tool's own answer (`gh pr view --json isDraft`, git's ancestry). None
  predicts a format nothing owns, so no phase had a part to set aside.
- `docs/round-record-spec.md` ends at 1,000 lines and
  `docs/review-chain-spec.md` at 999, at the ceiling (`questions.md` W1). The
  next edit to either cuts it at a heading.
- The release branch carries 33 drifted ledger rows on four coordinates no
  phase of this work edits — `agents/warden.md#"## Report"` (8),
  `templates/config.md#"# Repository config"` (14),
  `tests/test_every_reader_ends_a_line_where_gfm_does.py#OUT_OF_CLASS` (10)
  and `skills/verify/scripts/payload_meter.py#heading_starts` (1) — measured
  on an archive of `origin/release/v0.21.0`. Nobody on this branch read their
  claims, so no row here re-reads them, and `evidence-check --strict` exits 2
  on this branch for them alone.

## Fed back into the spec

- *Inferred during implementation:* a deferral's home loses `HOME_MARKS`, not
  `EMPHASIS`, and a bare `deferred` reads its home from the third cell
  through the same grammar.
- *Inferred during implementation, revised at round 1:* the suite's own `gh`
  finds no pull request by default, which the check reads as unknown, and a
  case that means a draft or a ready pull request says so
  (`tests/conftest.py`, `CONTRIBUTING.md` §*Running the checks*).
- *Revised at round 1, from the orchestrator's direction:* no payload and no
  `gh` answer is unknown and not judged as ready; a payload that cannot
  answer stays ready (`docs/round-record-spec.md` §*`Pass` has to be
  checked*).
- *Inferred during implementation:* a doubled field row fails on every
  record, not on the last alone; `--sealing` reaches the direct
  `broad-gate.md` home as well as the last round record.
- `spec.md` §*Data & interfaces* gained a row naming what the build added
  beside the proposed names, with their classes (`questions.md` W3).
