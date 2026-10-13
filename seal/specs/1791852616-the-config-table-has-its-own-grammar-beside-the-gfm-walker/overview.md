# the config table is read by the walker cmark-gfm holds (#871) — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. Facts that must outlive this work item go to the
evidence ledger, not here. -->

📋 implement applied
· spec:     pending — filled when the build closes
· evidence: pending — filled when the build closes
· verified: pending — filled when the build closes

## Why this work exists

`seal/config.md`'s table is now read the way GitHub shows it — by the one
walker held to cmark-gfm — so a gate is never handed a row GitHub does not
show, a row GitHub shows is never dropped in silence, and every refused line
is named once, with its edit, by the first command that reads it.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| When the stop rule's names leave | `plan.md` phase 1: "`refusal`, `CONFIG_ROW` and `CONFIG_HEADER` removed" / they stayed through phases 1 and 2 | the code: removed in phase 3 with their last caller | `seal.py#table_span` (phase 2's) aliases both patterns at import and `broad_gate.py#refusal` (phase 3's) passes `refusal` through; removing them in phase 1 leaves `seal.py` failing to load. `phases/phase-1.md` |
| Two writer cases the plan calls green | `plan.md` phase 2: "`test_the_writer_reads_where_commonmark_breaks` and `test_the_writer_leaves_a_commented_row_alone` green" / both texts are tables the walker refuses | re-pinned to *nothing written, bytes unchanged* | `spec.md` S5: "given a table the walker refuses, it writes nothing and prints the sentence". The `-->` under the first case's row is a row GFM shows, and C10's comment directly under the delimiter row ends the table as GFM ends it. `phases/phase-2.md` |
| Two of #784's ways the walk passes a pact row by | `tests/test_a_signer_declares_its_pact.py#STRAY_WAYS` held W2 and W8 indented as refused | read, in a case of their own | a row indented one to three spaces is one cmark-gfm renders (the oracle's indentation case, all four headers); `spec.md` S1 is *cells equal cmark-gfm's or refused* |

## Not verified

| Item | Who must answer |
|---|---|
| the full suite, repository-wide lint and typecheck after the rounds settle | the sealer, spawned by the orchestrator |
| the refusal's cause where a `<!--` follows one of the eight characters only `str.splitlines` ends a line at: the walker reads Python's pieces, so it names an HTML block left open that GFM does not see. The direction is refused and no row GFM hides is read; the sentence names the wrong cause | the owner — the walker's line ending is `gfm_table`'s for all four tables, outside this work item (`tests/test_the_mode_question_is_asked_once.py#test_a_break_commonmark_does_not_honour_hides_no_config_row`) |

## Not done

Nothing yet.

## Fed back into the spec

none
