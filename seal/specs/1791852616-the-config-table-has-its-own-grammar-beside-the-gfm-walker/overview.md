# the config table is read by the walker cmark-gfm holds (#871) — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. Facts that must outlive this work item go to the
evidence ledger, not here. -->

📋 implement applied
· spec:     `spec.md` (every section, S1–S9, §*Data & interfaces*, `## Removes`), `plan.md` (phases, alternatives, operational impact), `questions.md` Q1–Q6, `docs/the-reader-registry.md` §§*The four classes*, *Who declares*, *The census*, *A frame names what its work removes*, `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment*, `templates/config.md`, `skills/config/SKILL.md`, `skills/agent-contract/SKILL.md`
· evidence: `seal/ledger/1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker.md` — N1–N12 for the new units, eighteen `Corrected ·` rows for the released claims the stop rule's removal made false, and the `Re-read ·` rows `evidence-check --reverify --into` wrote for the rest
· verified: executed — each phase's modules (phase records name them and their exit codes), every new case red against the tree before it, `mutation-check` over each new arm, `evidence-check --strict .`; read — the claim of every released row a drifted coordinate cites, before its re-read was written

## Why this work exists

`seal/config.md`'s table is now read the way GitHub shows it — by the one
walker held to cmark-gfm — so a gate is never handed a row GitHub does not
show, a row GitHub shows is never dropped in silence, and every refused line
is named once, with its edit, by the first command that reads it.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| When the stop rule's names leave | `plan.md` phase 1 removes `refusal` and the stop rule's two patterns / they stayed through phases 1 and 2 | the code: removed in phase 3 with their last caller | `seal.py#table_span` (phase 2's) aliased both patterns at import and `broad_gate.py#refusal` (phase 3's) passed `refusal` through; removing them in phase 1 leaves `seal.py` failing to load. `phases/phase-1.md` |
| A removal the frame did not name | `spec.md` `## Removes` names `refusal` and not `hooks/config.py#refused_row` / `refused_row` is gone | removed | it read `refusal` and had no caller outside one test, which phase 1 re-pinned to `config_value`; `## Removes` is the frame's, so the removal is recorded here · NAME NOT IN TREE |
| Two writer cases the plan calls green | `plan.md` phase 2: "`test_the_writer_reads_where_commonmark_breaks` and `test_the_writer_leaves_a_commented_row_alone` green" / both texts are tables the walker refuses | re-pinned to *nothing written, bytes unchanged* | `spec.md` S5: "given a table the walker refuses, it writes nothing and prints the sentence". `phases/phase-2.md` |
| Two of #784's ways the walk passes a pact row by | `tests/test_a_signer_declares_its_pact.py#STRAY_WAYS` held W2 and W8 indented as refused | read, in a case of their own | a row indented one to three spaces is one cmark-gfm renders; `spec.md` S1 is *cells equal cmark-gfm's or refused* |
| Shape 5 in the twin's equality table | `plan.md` phase 3: `CONFIG_SHAPES` extended with shapes 1, 3, 4, 5, 6, 7, 8, 13, 14, 16 / shape 5 holds a comment inside the table | shape 5 is in the direction case, `LACKS_BLOCK_STATE`, with three shapes carrying a fence or a comment; every other shape of the sixteen is in the equality table | `spec.md` S7: where the twin lacks block state "it may refuse what the plugin reads and never reads what the plugin refuses". The twin refuses shape 5 at the comment line, the plugin at the row under it: both refuse, in two sentences |
| The mode gate's unit | `spec.md`, `plan.md` and `questions.md` named `hooks/mode-gate.py#unanswered_root` / the unit is `undeclared`, and no `unanswered_root` stood at 3bb2ea42 | corrected in place in the three records | `evidence-check --strict .` names it `NOT-IN-TREE`; `hooks/mode-gate.py:128` is `def undeclared` · NAME NOT IN TREE |
| Ten pact-change cases the build left red | `plan.md` phase 3 moves `evidence_check.py#cutoff_row` onto `config_value` and names no case of `tests/test_a_signer_records_a_pact_change.py` / ten of its cases still pinned exit 1 and the `LEFT` line for a config whose table the walk refuses, and failed from d427badd on; no phase or round ran the module | re-pinned in round 2's fix pass: where the walk refuses, exit 2 with the walker's sentence, the ledger untouched and no record; where only the pact reader refuses, the `LEFT` line at exit 1 as before. None of the cases' configs writes a `Ledger frozen from` row; one the walk reads above the refused line is a value, and the run reaches the `LEFT` line. The shapes that stop are listed by case id in `STOPPED_BY_THE_WALK` rather than asked of the walker under test | `spec.md` S2 and S4: an item the walk did not read in a table it refused is a refusal, and a command exits 2 on it. Measured: 137 passed at 321e9de1 and at ecb4f8fd, 10 failed at d427badd and at 4dfb3d0d. Whether the pact's own exit should win instead is `questions.md` Q7 |
| The third document | `spec.md` S8 names `templates/config.md`, `skills/config/SKILL.md` and `hooks/config.py#config_rows` / `skills/implement/orchestration.md`'s bootstrap warning still said a bare pipe parses as no row | rewritten, and its pin in `tests/test_first_setup_asks_once.py` re-pinned | found reading 0.12.0's row on *the three documents that promised the old behaviour* before re-reading it (contract §12) |

## Not verified

| Item | Who must answer |
|---|---|
| closed the full suite, repository-wide lint and typecheck after the rounds settle | #925, merged with lint and the suite green on the ubuntu, macOS and Windows legs; the repository configures no typecheck |
| the refusal's cause where an HTML comment opener follows one of the eight characters only `str.splitlines` ends a line at: the walker reads Python's pieces, so it names an HTML block left open that GFM does not see. The direction is refused and no row GFM hides is read; the sentence names the wrong cause | the owner — the walker's line ending is `gfm_table`'s for all four tables, outside this work item (`tests/test_the_mode_question_is_asked_once.py#test_a_break_commonmark_does_not_honour_hides_no_config_row`) |
| closed a repository's CI on a vendored `tools/evidence_check.py` keeps the stop rule's twin until `/specseal:evidence-ci` is run again | 5b1f6fae removed `evidence-check` and `/specseal:evidence-ci`, which no installed repository is asked to run again |

## Not done

`skills/evidence-check/scripts/pact_check.py#path_map` still reads the
machine-local `| Remote | Path |` map by the retired grammar
(`CONFIG_SEPARATOR`, `CELL`), as `spec.md` §*Scope* puts it out; the
orchestrator files its issue. `evidence_check.py#CONFIG_ROW_RE` and
`notify_may_be_always` were not touched: they judge a line's shape and read
no row's value, as `spec.md` §*Scope* says. None of `evidence_check.py`'s
`quoted_lines`, `claim_lines`, `anchored_rows`, `live_lines`, `hidden_lines`
or `readable` was edited (the seam with #872).

## Fed back into the spec

none
