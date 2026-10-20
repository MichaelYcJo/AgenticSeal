# 1791384159-a-unit-the-extractor-cannot-bound-is-refused — overview

`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. Facts that must outlive this work item go to the
evidence ledger, not here.

📋 implement applied
· spec:     this work item's `handoff.md`, `spec.md` and `plan.md` as reframed after round 1, `questions.md`, `routing.md`, `rounds/round-1.md`; #834's `handoff.md` §*Review of the run* (on `origin/chore/834-every-reader-and-record-is-inventoried`); `docs/the-evidence-ledger.md` §*A row is a content anchor, and it names no commit*, §*A released row is read again in the branch's fragment*, §*What the checker refuses, and what it says while refusing*; `skills/evidence-check/SKILL.md` §*A coordinate names content, never a position*, §*Resolving a unit without a parser*, §*Verdicts and what to do*, §*What the region is*, §*Known limits*, §*Migrating a pre-anchor ledger*; #848's body; `seal/config.md` (`Ledger frozen from`, no `Record language` row)
· evidence: `seal/ledger/1791384159-a-unit-the-extractor-cannot-bound-is-refused.md` — U1–U8 for the redesign; `Corrected ·` rows for 0.4.0's "An anchor resolves", "The declaration rule" and "`--migrate` answers an unsure place", 0.16.0's H1, 0.15.5's S7, 0.20.0's S1 and four 0.19.0 corrections; `Re-read ·` rows written by `--reverify --into` after each cited claim was read; in place, #864's seven and #869's two bare YAML rows re-anchored, and #867's K23, fenced-section `Corrected ·`, `Corrected · C1` and rider `Corrected · S1` rows re-stamped or corrected with a Notes trace
· verified: executed — every new case seen red against the merge head 1e05daa3 or the previous phase's head and green after (the paragraph cases, which `text_regions` makes green at the base, by mutation instead); `bin/mutation-check` on each changed unit, one break at a time; each phase's slice; the eight guard modules; `bin/evidence-check --strict .` with findings identical to `origin/release/v0.21.0`'s, file by file; `survivor-check` and `correction-check` over `origin/release/v0.21.0...HEAD`; `uvx ruff check` and `uvx ruff format --check` on the changed Python files. Read — each drifted released row's claim. Unverified — the full suite (the sealer's)

## Why this work exists

A bare symbol in any file but Python or markdown was bounded by a rule that
imitated the language's grammar — an indentation rule, then a hand-written
bracket-matching lexer — and both read `ok` over a body they left out
(#848); now a unit is bounded only by a real parser (`ast`, the CommonMark
heading path), every other bare symbol is `BROKEN` with the quoted-line
anchor written out, and a quoted line's region is its paragraph.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| How many production callers read the refusal | `spec.md` §*Data & interfaces* (first frame): three callers / `read_citation` is a fourth | all four, `read_citation` printing it | it calls `resolve_unit` for a citing row's section; the reframe's spec lists four |
| A bare symbol in a `.md` file | first frame: `.md` refuses "zero or several matches, as today" / a bare symbol ran the indentation rule over markdown | refused, naming the heading path | kept by the reframe (*In* 1, S6); measured, 1,964 `.md` coordinates in this repository's ledgers and none bare |
| What `--migrate` leaves a `.py` the interpreter cannot parse with | `spec.md` *In* 4 and S13: a file no rule bounds / also a `.py` that will not parse | both read their refusal | the same case for the same reason: no unit in the file can contain the range, and "no single unit contains" would hide why (`phases/phase-5.md`) |
| The refusal's wording | `spec.md` *In* 3: "keeps 'no bounding rule for `<suffix>`; anchor a quoted line instead' and adds the shape" / the shape is written on the row's own path, with the paragraph rule and `--reverify` named | the row's own path | the line on a `--strict` run is then the edit to make, written out; pinned whole by the work item's `no_rule` helper |
| How many bare YAML rows this repository holds | `spec.md` *In* 8: 14 / 16 | 16, all re-anchored | #869's fragment, in the release branch since the reframe, holds K14 and its `Corrected · W3` on `publish-release.yml#jobs`; both re-anchored in place (`phases/phase-7.md`) |
| What W3 quotes | `spec.md` *In* 8: `"publish:"` and `"seal:"` / three quotes | three | the `publish` job has a blank line inside it, and the claim's `created` output comes from the note step in the second paragraph (lines 62–69) |
| `"ledger:"`'s region | `spec.md` *In* 8: lines 163–181 / 147–181 | the paragraph as it is | the job's comment above the key has no blank line before it, and it is where the warning's three causes are written, which S7's claim is about |
| Which released families take a `Corrected ·` row | `plan.md` phase 7: 0.15.5 S7, 0.20.0's W3 correction, 0.20.0 S1, 0.4.0 L51 and L67 / not W3; also 0.16.0's H1 and four 0.19.0 corrections | the families the tree showed | W3's newest member is #869's `Corrected ·` row, re-anchored in place; H1 and the 0.19.0 corrections cited cases phase 6 deleted or re-fixtured, and each 0.19.0 correction is superseded by a row citing it (`docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment*: "A `Corrected ·` row supersedes the family of the row it cites, whose coordinates are not checked again, and starts a family of its own"; corrected in round 2's ⬜ 6, which found this cell grounding it on the two-corrections sentence instead). Round 2's 🟡 3 added 0.4.0's lines 20, 58 and 66, whose claims described the declaration rule |
| The rider check's docstring | `plan.md` phase 8 / phase 6 | phase 6 | its paragraph described the branch phase 6 removed, and S7 forbids the word in the three scripts |

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck | #889, merged with lint and the suite green on the ubuntu, macOS and Windows legs; the repository configures no typecheck |
| closed How many rows of a consuming repository's ledger change verdict on upgrade (`questions.md` Q3) | 5b1f6fae removed `evidence-check` and the ledger it graded |
| closed The walk against real code of each family beyond the fixtures — a large TypeScript or JSX codebase, C with preprocessor branches, Rust with macros | moot: the walk and its lexer left the tree in phase 5 of the redesign (1e00f933), so there is no walk to misread anything |

## Not done

- **A two-quote range anchor** and **`--migrate` writing a quoted-line
  anchor** for a row it leaves, both out by `spec.md` §*Out*; the range is to
  be weighed on a measured count of rows that needed more than one quote.
- **`.test_durations`** still names the cases phase 5 and 6 deleted; the
  entries drop no case from the shards and leave with the next refresh,
  which takes a CI run (`CONTRIBUTING.md` §*Running the checks*).
- **The release branch's own 33 drifted rows** — `agents/warden.md#"## Report"`,
  `templates/config.md#"# Repository config"`,
  `tests/test_every_reader_ends_a_line_where_gfm_does.py#OUT_OF_CLASS` and
  `skills/verify/scripts/payload_meter.py#heading_starts` — read `DRIFTED` at
  this branch's head exactly as on `origin/release/v0.21.0`. This work changed
  none of those units, read none of those rows, and removed the three
  `Re-read ·` rows its narrowed `--into` wrote for them. Named in the
  hand-back.
- **#888** (the opener's never-matched shapes) is moot once this lands: the
  opener left the tree in phase 5.

## Fed back into the spec

- *Inferred during implementation:* a bare symbol in a `.md` file is refused
  with the heading-path sentence (kept by the reframe as S6).
- *Inferred during implementation:* `--migrate` leaves a row citing a `.py`
  the running interpreter cannot parse with the Python refusal, as it leaves
  one in a file no rule bounds.
