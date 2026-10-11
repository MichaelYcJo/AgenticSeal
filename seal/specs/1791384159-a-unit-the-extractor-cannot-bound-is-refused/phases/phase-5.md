# 1791384159-a-unit-the-extractor-cannot-bound-is-refused — phase 5

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | 1e00f933 |
| Ran by | smith on Opus 5.5 |

## What this phase was asked

`plan.md` phase 5, the first of the redesign after round 1: `bounding_rule`
answers `"ast"`, `"heading"` or `None`; `resolve_unit`'s `"brace"`/`"block"`
arm goes; `unbounded` adds the anchor's shape to the refusal; `--migrate`'s
left reason for such a file reads the refusal (S13); the lexer, the walk,
the block rule, the opener, the statement words and `generic_units` are
deleted with the cases that pinned them; `text_regions`' docstring states the
paragraph rule. Cases S1, S2, S3, S4 (the `.rb` half), S8, S9, S13 red then
green. The spawn added: merge `origin/release/v0.21.0` (ad447367) first, which
holds #860 and #869, and never rebase.

## What this phase found

**The frame holds.** Every coordinate `plan.md` §*Technical context* names
was where it said at the merge head, and the deletion took the 490 lines it
measured. `file_units` keeps its third field, always `False`, until phase 6
removes it with the other readers of the flag.

**S2, S4 and #848's quoted reproduction were green before the change.**
`text_regions` is unchanged by this work, so a case pinning its paragraph
cannot be red against the base. Each was shown to watch the rule instead:
`bin/mutation-check` taking the paragraph's downward extension out of
`text_regions` turns them red. The cases that are new behaviour (S3 over 22
suffixes, S8's three answers, S9, S13 and S1's refusal half) were 27 red
against the merge head 1e05daa3 and green after.

**The refusal carries the path the row named.** After "no bounding rule for
`.ts`; anchor a quoted line instead:" it writes the row's own path, a `#`, a
placeholder quoted line and a zero hash, then says the region is the
paragraph that line sits in and that `--reverify` fills the hash — so the
line on a `--strict` run is the edit to make, written out. (The sentence is
pinned whole by `no_rule` in the work item's test module.)

**`--migrate` names the Python refusal too.** S13 asks for a file no rule
bounds; a `.py` the interpreter cannot parse is the same case for the same
reason (no unit there can contain the range), so it reads the Python
sentence rather than "no single unit contains".

**Which cases left, and which were re-fixtured (Q7, for this module).** From
`tests/test_a_row_points_by_content.py`, gone with the code they pinned: the
`BRACE` spans and the "generic rule cannot find" case, the mention-versus-
declaration case, the statement-keyword case, the C#/Swift resurrection
case, the bare call statement, `generic_units`' empty answer, the moved
brace-language and semicolonless
units, the resurrected `--reverify` refusal, the multi-line bare-name case,
the blocked declaration recorded by hand, the unchanged blocked row, both
`--migrate` unsure-place cases, the hash named for an unsure place, and the
stale claim on an unsure place, whose rule — a claim degrades to DRIFTED —
keeps its `.py` instance in the widening case. Re-fixtured: the form-feed
generic cases on a quoted line in `.js`, the tie-break cases and the shared
claim line on two Python definitions of one name, the brace-language drift on
a quoted signature, and the YAML half of the constant case removed. Phase 6
judges `tests/test_a_released_row_is_read_again_in_a_fragment.py` and
`tests/test_a_signer_records_a_pact_change.py`; at this commit their nine
unsure-place cases fail, which is the state the plan accepts between the two
phases.

**The CI `ledger` job is red from here to phase 7**, as the plan states:
`--strict .` reads the 14 bare YAML rows `BROKEN` with the refusal, and the
fragment rows citing deleted units `BROKEN`.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| `BRACE_FAMILY`, `BRACE_SUFFIXES`, `BLOCK_SUFFIXES`, `brace_family`, `StringForm` and its forms, `_literal_at`, `brace_lexed`, `brace_span`, `block_span`, `declaration_opener`, `opens_declaration`, `STATEMENT_WORDS`, `generic_units` | none: S9's case refuses each name, and the quoted line is the format they guessed at |
| The walk, lexer and YAML cases of the work item's own test module | S1–S4, S8, S9, S13 in the rewritten module |
| Eighteen cases of `tests/test_a_row_points_by_content.py` (listed above), and part (a) of `test_reverify_never_contradicts_the_checks_verdict` | re-fixtured where the property has an instance, gone where it had none |
