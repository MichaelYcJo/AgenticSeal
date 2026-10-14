# the record of truth is tests, not coordinates (#944) — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. -->

## Why this work exists

The ledger re-read 1,421 prose claims to confirm 1,420, so the record of truth
moves to tests a rule's `Enforced by:` names, and the plugin stops shipping the
ledger.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| the owner's tenet, committed by #944 as its first act | `spec.md` §*Scope* names no `CLAUDE.md` section and no rewrite of `CONTRIBUTING.md` §*What a change to a gate must carry* beyond its ledger sentences / the build's first commit adds `CLAUDE.md` §*The rule a mechanism is kept against — subtract before you add* below the goal section, moves the goal's `CONTRIBUTING.md` link into it, and rewrites that `CONTRIBUTING.md` section in place so a pull request adding a mechanism names the one it removes, or why none can go, with what that one caught | the build | the owner set the tenet on 2026-10-14 and the orchestrator's spawn ordered it before phase 1, so every session reads it from the tree rather than from one session's memory. `CLAUDE.md` 9,261 → 9,827 B. One released row drifts on it, `seal/releases/0.18.1.md` row O1 under `CLAUDE.md#"## The goal a design is chosen against — verification that runs unattended"@d8810fc4`; its claim, "The goal section's batch sentence is folded into its link to `implement`'s step 1", still holds, and no `Re-read ·` row is written because this work item retires the ledger (phase 2 removes the arm that reads it) |
| phase 1's slice document lost more than its ledger sentences | `spec.md` §*Removes* names no part of `docs/the-record-layout.md` beyond the survivor paragraph, the `survivors.md` row and the `evidence-todo.md` row / phase 1 removed the 64 KB half of the size rule, the `- **A release ledger file.**` bullet, the `CHANGELOG.md` and `seal/releases/` history under it, and the whole §*What is decided and not built yet* (F1–F4) | the build | the owner's tenet: a rule nothing enforced, whose only grounds were ledger rows, and four "decided" items all built, were kept only for having been written. The live rules of F2, F3 and F4 stand with their tests; `phases/phase-1.md` carries the census |
| S6 allowed `nothing — <why>` at a count of 0 | `spec.md` S6 "names a resolving test or `nothing — <why>`" / S4 and §*The replacement* count `nothing` as unenforced | S4, by the owner's answer of 2026-10-14 | S6 is rewritten in place to agree with S4 |
| the resolver refuses a name defined twice | `spec.md` §*The replacement* item 1: "defined twice … fails the run" / `fold_check.py#target_problem` passed a name `named_unit` reports twice | the spec, by the owner's answer of 2026-10-14 | a rule bound to an ambiguous target is not bound; the one resolver both checkers read refuses it, with `tests/test_a_folded_statement_names_what_enforces_it.py::test_a_name_defined_twice_is_no_target` seen red first |
| `## Unenforced rules` lists every rule file | `spec.md` §*The replacement* "one row per rule file at today's count" / 55 files listed, the 11 at 0 held by the family row's ceiling of 0 | the code | a listed row at 0 holds exactly what the family row holds |
| `bin/rules <doc>` | not in the frame / built in phase 1 at the owner's direction of 2026-10-14, relayed by the orchestrator | the owner | a reader that prints and writes no record |
| four ledger-document statements left in phase 2 | `plan.md` phase 3 moves `docs/the-evidence-ledger.md`'s fold, settle, live-lines and baseline statements / phase 2 deleted the retirement-guard statement, the records arm's ship boundary, §*A correction a merge dropped* and the lenient-reader statement, and cut `anchored_rows` from the liveness statement | the build | `enforced-unresolved` named each one's enforcers as deleted by this phase; a statement whose test is gone states a rule nothing holds |
| six test modules deleted before phase 4 | `plan.md` phase 4 deletes the ledger-mechanics modules / phase 2 deleted `test_the_lenient_run_says_what_the_broad_gate_will_say.py`, `test_a_record_states_what_the_tree_has.py`, `test_a_merge_cannot_silently_drop_a_correction.py` and `test_the_ledger_rules_have_one_home.py` with the sweep's two | the build | each one's subject left in phase 2: the CI job and gate arm, the records arm, the correction step, the homes. W2's kernel cases are in none of them |
| the release checklist's §2 is renamed | not in the frame / `## 2. Gather, fold, bump` became `## 2. Gather, bump` once its fold lines went, and `CLAUDE.md`, `CONTRIBUTING.md` and the layout document cite the new heading | the build | the heading named an act the section no longer holds |
| settle's report stops grouping | `plan.md` phase 3 names no change to `settle.py` / `coordinates` and `segment_of` removed, the report lists the released, unfolded items, and settle §2 is renamed *Write one standing statement per rule* | the orchestrator, deciding phase 2's open item 1 | with the ledger gone every item was ungrouped, so the grouping named nothing |
| two ledger-document statements leave instead of moving | W1's default moves every statement whose target still exists / the parse-once and quoted-line statements are removed | the build | `evidence_check.py#py_spans` and `#resolve_unit` state each rule in their docstrings, and phase 4 moves their cases to the kernel module; the layout is no home for a coordinate library's rules |
| nothing moved into `skills/settle/SKILL.md` | the spawn names the settle skill as a home / every moved statement went to `docs/the-record-layout.md` | the build | `tests/test_docs_line_wrap.py` holds the skill to 88 columns and skips only an `Enforced by:` line inside a marked `docs/` statement, so a rule there could not name its test case |
| the gate's skip-at-main machinery | `spec.md` §*What happens to each reader* names the three arms / `SKIPPED_AT_MAIN`, `skipped_at_main` and `skipped_line` went too, with a case that no mirrored step skips at `main` | the build | they existed only for the two range arms; kept, they are a branch nothing reaches |
| the pact's change records lose their writer | `spec.md` §*Scope* "`pact_check.py` and the pact's hash anchors … left as they are" / `record_pact_changes` lived inside `--reverify` and leaves with it; `docs/the-pact.md` loses §*A signer records a pact change* and two statements about the writer; `pact_check.py` still reads the records, the reviews and a signer's `seal/ledger*.md` | the build | `plan.md` phase 4 deletes `--reverify`, and the recorder was triggered only by ledger rows moving; a statement whose test left states a rule nothing holds. Whether the record-and-review half of `pact-check` goes too is Q2 |
| the kernel is smaller than the frame's list | `spec.md` §*What happens to each reader* lists `ANCHOR_RE` and copies of `gfm_lines` and the fence rule in the kernel / `ANCHOR_RE`, `ANCHOR_PATH`, `resolve`, the minor-level readers and every vendored copy went; `gfm_lines`, `heading_level` and the fence rule ask `unverified_check.py` | the build | the two readers of `ANCHOR_RE` were deleted here, and the vendored copies existed for `evidence-ci` running the file alone, which no command does now |
| `root-migrate.py` loses step 6 with its mapping rows | `plan.md` phase 4 names the two mapping rows / the re-point of anchors in the old ledger went too, a 0.3.x map moves to `seal/map.md`, and both READMEs' by-hand block changed in this phase | the build | step 6 read the ledger through `ANCHOR_RE`; the by-hand block is run by `test_the_readmes_by_hand_sequence_yields_the_hooks_tracked_set`, so it moves with the hook |
| `.test_durations` is pruned, not refreshed | `plan.md` phase 4 "`.test_durations` from the run's `test-durations` artifact" / the deleted files' entries and the cut cases' entries removed, the 54 moved and renamed cases carry their old Windows prices | the build | no run exists without a push, and the deletion alone took the unpriced share to 5.4 %; carried prices bring it to 4.97 % |
| S9's grep cannot reach zero as written | `spec.md` S9 "`grep -rn '…evidence-check…\|survivor'` … nothing but `changelog/`" / `arm_check.py`, `round_record.py` and `skills/verify/SKILL.md` say `survivor` in 15 lines for a mutation that no case killed | the build | the mutation word is a different meaning; the grep holds with it excluded (`phases/phase-6.md`) |
| the kernel moves | `spec.md` §*What happens to each reader* and `plan.md` alternative G kept the kernel at `skills/evidence-check/scripts/evidence_check.py` / it is `skills/verify/scripts/coordinates.py`, with `pact_check.py` beside it | the owner, 2026-10-14 | the directory named a feature that left; the kernel's one dependency, `unverified_check.py`, is in `skills/verify/scripts/`, and the five loaders left each still use it (`phases/phase-6.md`) |
| no case was deleted with `seal.py`'s ledger path | the spawn "the test cases that exist only for it are deleted" / every case naming a ledger file guards something else, so all 96 stay with their fixture on `follow-up.md` and `specs/<id>/` | the build | the fragment branch of `work_item_of` had no case of its own (read) |
| three phase 4 leftovers are repaired in phase 6 | not in the frame / the bare-symbol refusal said `--reverify` fills the hash, `agents/warden.md` §Report described the evidence checker's scan of a committed report, and the gate-misfire issue template named the evidence check | the build | each named something phase 4 deleted; the refusal and the warden's pin were seen red first, and `preload:warden` and `unenforced:agents/warden.md` are lowered to what is measured |
| the census lines were removed, not re-recorded | the spawn "with their census hashes re-recorded" / the five units whose docstrings changed (`rider_check.py#reverify`, `#migrate`, `chain_check.py#fix_range`, `pact_check.py#shown`, `unverified_check.py#annotate`) declare a `Reads:` line and leave `tests/undeclared_readers.txt` | the build | the census refuses a moved hash: `test_a_reader_declares_its_input_class.py#census_unit_changed` says to declare the unit and remove its line |
| the design record is rewritten in place | `docs/one-root-by-lifetime.md` says its 2026-09-02 text "is a record … and is not rewritten" / both editions' ledger statements rewritten to what stands, release step 1 (the fold) and its rationale removed so step 2 became 1, and two decision rows (settle's grouping, anchored rows) rewritten or removed | the owner's rule of 2026-10-13 that a document states the latest and not the history, and S9 | the statements described a ledger the tree no longer has; `unenforced` and `docs-history` for both editions lowered by the rule paragraph and history lines that left |
| `CLAUDE.md` loses the `seal` paragraph's narrative | the spawn "cut an equivalent elsewhere in the same file" / the tenet gains the one-source sentence (+89 bytes) and the whose-rule section's account of how `seal` came to need the rule leaves (−188), keeping the pointer to `tests/test_one_word_one_meaning.py` | the build | that account is history the test module's own comment holds; `preload:claude-md` lowered 9,126 → 9,027 |
| `templates/config.md` §*Pact* rewritten | not in the frame / its `Pact notify` paragraph named `evidence-check --reverify` as the writer and linked `docs/the-pact.md` §*A signer records a pact change*, which phase 4 removed | the build | a shipped template linked a section that is gone and a writer that is gone; the paragraph says no command writes a record and how a held one is read, under Q2's default |
| a module phase 4 left red is repaired here | not in the frame / `tests/test_a_shrunken_corpus_declines_to_judge.py` still listed `test_the_root_migrates_itself.py#test_the_re_pointed_ledgers_are_staged_with_the_move`, which phase 4 deleted; three of its cases failed at 8cf9e1ff | the build | a defect this branch caused is fixed where it arose; phase 4's narrow runs did not include that module |
| two `seal/follow-up.md` rows change | not in the frame / the row asking whether `CONTRIBUTING.md` gains a third arm for a drifted ledger claim is removed, and the ledger and `evidence-check` clauses leave the `hits()` and `Broad gate` rows | the build | the third-arm question has no subject without a ledger; the other two rows' questions stand without the ledger clauses |

## Not verified

| Item | Who must answer |
|---|---|
| `bin/rules.cmd` runs on Windows: written in lockstep with `bin/fold-check.cmd`, never executed | the pull request's Windows leg |
| the full suite, the repository-wide lint and the typecheck after phase 5 | the sealer, once, after the rounds |
| `.test_durations` priced by a Windows run after phase 4: the file holds pruned entries and carried prices, 610 of 12,270 cases unpriced (4.97 %, one case from `STALE_SHARE`) | the orchestrator, by the refresh recipe in `CONTRIBUTING.md` at the pull request's run |
| `bin/fold-check.cmd --help` from `/` on Windows: `test_bin_wrapper_resolves_the_checker_from_any_cwd` was re-pointed from the deleted `evidence-check` wrapper, executed on macOS only | the pull request's Windows leg |
| `bin/pact-check.cmd` after its script path moved to `skills\verify\scripts\pact_check.py`: edited in lockstep with `bin/pact-check`, whose `--help` exits 0 on macOS, never executed on Windows | the pull request's Windows leg |

## Not done

What still names the ledger after phase 6, each left on purpose:

- `skills/verify/scripts/pact_check.py` still globs a signer's
  `seal/ledger*.md` for pact anchors; the glob is Q2's.
- Test names and docstrings that say *ledger* (for example
  `test_the_target_is_resolved_by_the_ledgers_reader`, which
  `docs/the-record-layout.md` names in an `Enforced by:` line) are read as
  they are: rewriting each into the rule it guards is written by whoever
  moves a rule into a test — #941 and #940 under the reader criterion — and
  by #942 when it rebuilds the tests.
- `skills/writing-style/SKILL.md`'s translation example names
  `templates/ledger.md` as the file a translator opened; it is an example of
  choosing a word, and the file it names is gone.
- Records under `seal/specs/` and the released `changelog/` keep their
  history.

## Fed back into the spec

none
