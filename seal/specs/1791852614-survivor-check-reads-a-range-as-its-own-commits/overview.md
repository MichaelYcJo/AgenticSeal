# 1791852614-survivor-check-reads-a-range-as-its-own-commits — overview

📋 implement applied
· spec:     `routing.md`, `spec.md`, `plan.md`, `questions.md` of this item; `docs/the-record-layout.md` §*A range owns the commits that descend from its start*; `docs/the-reader-registry.md` §*The four classes and the line that declares one*; `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment* (through `evidence-check --help`); `templates/sdd-phase.md`, `templates/sdd-overview.md`; `seal/config.md`
· evidence: `seal/ledger/1791852614-survivor-check-reads-a-range-as-its-own-commits.md` — 8 new claims (S1–S4, S5, S6, S7, S8, S9, S10, S11), 2 `Corrected ·` rows (0.9.3 `S3`, 0.11.2 `S2`), 25 `Re-read ·` rows written by `evidence-check --reverify --into`
· verified: executed — each phase's modules (`phases/phase-N.md`), every new case seen red under `bin/mutation-check`, every new unit broken by it, `bin/evidence-check --strict` at exit 0, `survivor-check` over the branch in both spellings at exit 0, Q1 measured on four real ranges; read — the 71 released rows the drift named, before re-reading them; unverified — the rows below

## Why this work exists

On a two-dot range holding a merge of the base, the survivor sweep read another work item's correction as the range's own and reported its standing copy; it now keeps only what the range's own commits removed or wrote, and refuses a two-dot range that owns nothing.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| S3's comparison | `spec.md` S3: "at the same score as on a history without `S1`" / the control is the history where the same sentence stood in `root`, before the range | code | the sentence `S1` writes is in the pool at the tip, so a history without it has different phrase weights and a different score for a reason the case is not about; with the sentence in `root` the tree at the tip is the same and only the range differs (`phases/phase-2.md`) |
| the released rows | `spec.md` §*Data & interfaces*: "`evidence-check --reverify --into` re-reads of every released row whose anchor on `corrected` or `parse_range` moves" / 25 re-reads and 2 `Corrected ·` rows | code | 0.9.3's `S3` lists the exceptions to "a sentence is corrected where the file holds it fewer times at `b` than at `a`", and this work adds one; 0.11.2's `S2` lists three ways a path list is accounted for, and this work adds a fourth. A re-read cannot restate a claim. The drift also reached `RULES`, the path-list case and the home section, beyond the two anchors the spec named |
| the spelling's reader | `spec.md` §*Data & interfaces*: "`parse_range` … returns the spelling it read, or a sibling unit does" / a new unit `separator`, which `parse_range` now calls too | the sibling | `parse_range`'s return shape is read by `whole_range`, which the frame keeps unchanged; one unit reading the dots keeps the spelling to one reader (`phases/phase-1.md`) |
| `corrected`'s docstring | `plan.md` phase 3 / written in phase 2 | code | written with the code it describes; phase 3 added the rest (`phases/phase-3.md`) |
| the home statement's `Enforced by:` line | `plan.md` phase 3: verified by `tests/test_a_folded_statement_names_what_enforces_it.py` / that module does not bind the line | the line kept, read by people | the section has no `<!-- specs/<id> -->` marker, and adding one would make `retired_directories` read this unshipped item as folded (`phases/phase-3.md`) |

## Not verified

| Item | Who must answer |
|---|---|
| the own-commits pass on the Windows leg's git: `own_changes` asks `cat-file --batch` for `<full>^:<path>`, measured on macOS only | CI's Windows shards at this pull request |
| closed `owned`'s refusal where `own_commits` returns None, which needs git to fail inside `git log` after the range resolved; no case reaches it | round 1's 🟡 2: `test_a_range_whose_own_commits_cannot_be_listed_is_refused` reaches it through a stub chain module, with the timeout beside it, at 7f08b48f |
| the full suite, repository-wide lint and typecheck | the sealer, after the review rounds settle |

## Not done

`skills/evidence-check/scripts/correction_check.py#parse_range` reads both
spellings the way this sweep used to. It was left alone: that check reads
the merges inside a range on purpose, and its question is what a merge
dropped, so its range is not the one this work's rule decides. A two-dot
range over hundreds of commits pays for the pass (55 s on a 169-commit
range in Q1); no skip was added, because the one such range measured holds
merges and its spelling for a whole branch is `A...B`.

## Fed back into the spec

none — the home's statement is the one `spec.md` §*In* 4 named, and the two
corrected ledger rows are recorded above
