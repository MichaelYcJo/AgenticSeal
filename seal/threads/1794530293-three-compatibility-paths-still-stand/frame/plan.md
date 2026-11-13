# Implementation Plan: 1794530293-three-compatibility-paths-still-stand

## Technical context

The tree as read at `dda87704c`.

The three paths stand in three layers. The settings path is code: one arm
of `lib/config.py#config_pairs` (`:139-141`) that every settings reader
goes through, a converter in `skills/implement/scripts/seal.py`
(`#converted`, `#convert`, `#mode_report:2183-2202`), and the parity
refusal in `skills/code-review/scripts/chain_check.py#originals_of`
(`:1640-1655`). The block and the launcher are prose a session executes:
steps 4 and 4b of `skills/update/SKILL.md`, each with a shell command its
tests run. Around all three stand the prose that describes them and the
tests that pin them. `frame/design.md` *Removes* lists every coordinate.

The constraints the build works under:

- Contract rule 15: the one case *Scope* item 6 rewrites is seen red
  against `config_pairs` with its `config.md` arm still in place.
- The broad gate is the orchestrator's (contract rule 2). Each phase runs
  the narrow set its Verified by cell names.
- `tests/behaviour/test_release_hygiene.py#test_no_loaded_file_names_a_version_at_or_above_the_running_one`
  refuses any shipped text naming 0.38.1 once the version moves (G15).
- The `docs/` sentences stay as they read until the settle, and the
  citation of step 4b in `docs/checks/the-stamp.md` is excused by the
  `remove` item that quotes it (G11). No phase edits `docs/`.

**The failure scenario of the chosen approach, six months on.** A
repository last set up by 0.36.x or earlier updates past this release
without reading its note. Its `seal/config.md` is read as no file: `seal
gate` exits 2 naming a missing `Broad gate` key in a `config.json` that does
not exist (G6), `seal pr-body` refuses for the language keys, and `seal
mode` writes a `config.json` holding `Mode` alone beside the old table. A
migration repository there fares worse: its `seal/parity.md` declares
nothing, so the parity arm stops asking for `original:` lines without a
word (G7). Each command's refusal names `config.json` and the key, which
leads a person to `templates/setup/config.md`. Nothing names `parity.md`.
The owner judged on 2026-11-13 that no such repository needs the path
(G3), and the 0.38.1 note's *Updating* line is the one place that tells
such a person what to do.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. Remove all three paths together, in this release (chosen) | The scenario under *Technical context*: a repository on 0.36.x or earlier that skips the note reads its settings as absent | Chosen. The owner's comment of 2026-11-12 decides the release and the scope; the *Done when* items name all three |
| A2. Keep the structure: keep the `config_pairs` refusal and the `parity.md` refusal, naming a by-hand conversion, and remove only the converter and the update steps | The refusals stay with no date to leave by, and a reader of the code keeps meeting a file no release has written since 0.36.0. The premise that keeps them is that a repository on 0.36.x or earlier still exists and updates. Checked: the owner's comment judges that no such person needs the path, and nothing in the tree counts such repositories | Rejected. The issue's table lists the refusal arm of `#config_pairs` and both refusals as what the removal takes out |
| A3. Keep update steps 4 and 4b as steps that find nothing | Every `/agentic:update` run pays to read 97 lines of `skills/update/SKILL.md` and runs two commands that answer `nothing` for every person on 0.25.0 or later. The premise that keeps them is a person on 0.24.2 or earlier, or on 0.33.0 to 0.34.1, who updates. The owner judged none needs it | Rejected, on the owner's decision |
| A4. Edit the `docs/` sentences in this pull request, as a work item whose subject is the policy root | The subject here is code. Edited directly, the five sentences would bypass the settle, which writes each section as the latest decision of the released designs in merge order (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*). Two unsettled designs already change two of these sections (G2) | Rejected. The sentences go into `frame/design.md` *Rule changes*. The one dangling citation is excused until the settle (G11) |
| A5a. The walker's two-cell cases stay on a header literal the test file holds, and the pin to `OLD_TABLE` goes (chosen) | The pass walks a header no shipped reader hands the walker, against the premise `test_the_config_pass_is_the_config_readers_header` stated. The walker builds every shape from the header's width alone, so a two-cell pass still holds its multi-cell behaviour, which the three- and four-cell readers depend on (G9) | Chosen. It keeps the corpus count (`test_the_corpus_is_counted`'s `5455`) and every case's text |
| A5b. Delete the two-cell pass and the `_Old_config_*` cases with the converter | The walker's multi-cell readers, `pact_check.py#ANCHOR_TABLE` and `settle.py#JUDGMENTS_HEADER`, lose every corpus case, and a defect in a row of more than one cell goes uncaught | Rejected |
| A5c. Re-point the two-cell pass to a live reader's header, such as `pact_check.py#ANCHOR_TABLE` | Every case text in `_Old_config_table`, `_Old_config_shapes` and the conftest fixtures is a two-cell table, so each would be rewritten to three cells, with the corpus count measured again. The cost lands in a file the removal only has to unhook | Rejected. A5a keeps the coverage at none of that cost |
| A6. Keep the README's two by-hand sentences on the pact's `| Signer |` table and `pact-paths.md` | They serve only a person coming from 0.36.x or earlier, the reader the owner judged needs no path. Kept alone, they would describe one half of a migration whose other half the same paragraph no longer names | Rejected. The 0.38.1 note's *Updating* line carries both acts (`frame/design.md` *Scope* item 12) |
| A7a. Rewrite #1492's *Updating* line in its `changelog.md` (chosen) | The fragment then differs from the published v0.37.1 note it was built from. Nothing reads the fragment for a note again (G13), and the settle removes it | Chosen, because the owner's comment names that line as part of what changes |
| A7b. Leave #1492's fragment as the record of what 0.37.1 said | The tree keeps a line giving a date the owner overturned, which the owner asked to change | Rejected |
| A8. Delete the two `CLAUDE.md` import cases with `tests/behaviour/test_the_old_block_leaves_through_update.py` | `CLAUDE.md` *The core* says the file imports nothing, and nothing else holds it. An `@` line would load the core twice in every session here | Rejected. The cases move to `tests/text/test_the_rules_claude_md_names_have_one_home.py` |
| A9. Remove the S3 case of `tests/lib/test_config.py` and pin nothing in its place | What a person sees changes: every command stops refusing an old `config.md`. Contract rule 14 asks for a pin of the new behaviour | Rejected. The case is rewritten to pin `(None, None)` |
| A10. Leave `skills/update/SKILL.md`'s step 5 numbered 5 | A step list reading 1, 2, 2b, 3, 5 tells a reader something is missing, and nothing cites step 5 by number but one docstring (`frame/design.md` R29) | Rejected. Step 5 becomes step 4 |
| A11. One phase for the whole removal | The crafter holds every file of `frame/design.md` *Removes* in one pass, and a red narrow run cannot tell the settings removal from the update removal | Rejected. Two phases, one per kind of path, each green on its own |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 6, the settings and migration config path in code, shipped prose and tests | The rewritten S3 case seen red against `config_pairs` with its arm in place, then green. `tests/lib/test_config.py`, `tests/lib/test_tables.py`, `tests/skills/test_seal.py`, `tests/skills/test_broad_gate.py`, `tests/skills/test_fold_check.py`, `tests/skills/test_pr_body.py`, `tests/skills/test_pact_check.py`, `tests/skills/test_chain_check.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` green. `git grep -n -w -E 'OLD_CONFIG\|OLD_TABLE\|old_config_path\|PARITY_KEYS\|OLD_PARITY_CONFIG\|config_shapes'` and `git grep -n -E 'unconverted_'` find nothing outside `seal/threads/`; the first matches whole words, since `COMMENTED_OLD_TABLE` and `_Old_config_shapes` stay | 3fb5b69cd |
| 2 | `frame/design.md` *Scope* items 7 to 12, the update steps, the block's template and exemption, the READMEs, #1492's line, this work item's `changelog.md` and the version move | `tests/behaviour/test_update_reads_the_config_directory_in_use.py`, `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `tests/behaviour/test_release_hygiene.py`, `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`, `tests/text/test_the_rules_claude_md_names_have_one_home.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_both_editions_carry_the_same_folds.py`, `tests/behaviour/test_docs_line_wrap.py` green; each moved `CLAUDE.md` case seen red in its new file, the case that reads `CLAUDE.md` with an `@` line planted there and taken out before the commit, and the case that reads no file with its `IMPORT` pattern mutated. `git grep -n -E 'agentic:start\|claude-md-block\|CLAUDE_PLUGIN_DATA\|4b\. The launcher\|2027-02-07'` outside `seal/threads/` finds only `docs/checks/the-stamp.md`, whose sentence the `## Rule changes` `remove` item takes out at the settle, and `docs/experiments/2026-11-06-what-draws-the-stamp-without-a-plugin-hook.md`, which *Scope* puts out; under `seal/threads/`, 2027-02-07 stands only in #1492's records other than its `changelog.md` and in this work item's records, which quote it | e7215e0e4 |

## Overlap with the release

None of the release's other open work items meets this work. #1543 changes
the argparse description of `skills/code-review/scripts/pr_wait.py#main`
alone, and no file, rule or check of this work reads that text. #1422
changes `agents/framer.md` or `templates/records/sdd-design.md` only if its
paid runs show the label missing again, and this work touches neither. The
version move is the one point where order shows.
`docs/releasing/branch-and-release.md` *Work accumulates on a release
branch* puts the move in the first pull request into `release/v0.38.1`,
and this work carries it. Where #1543 merges first, the move lands in the
second pull request instead. Nothing fails for it, since the `hygiene`
workflow reads the move at the release pull request into `main` (read,
the same section), and which order the orchestrator takes is its own
judgment of the run.

## Operational impact

- **The version move.** `.claude-plugin/plugin.json` is the one file that
  holds the version (`frame/design.md` G14). Phase 2's crafter moves its
  `version` from `0.38.0` to `0.38.1` in the commit that adds this work
  item's `changelog.md`, and the fragment's `### Removed` section ends with
  the line `- The version moves to 0.38.1.`
- **A compatibility break, by the owner's decision.** A repository last set
  up by 0.36.x or earlier, or a machine last updated by 0.24.2 or earlier,
  or by 0.33.0 to 0.34.1, keeps what that release left, and nothing in
  this release reads or names it. The fragment's *Updating* line is the
  account a person reads, through `/agentic:update` step 3, which prints
  every note between their version and the new one.
- **No new dependency, environment variable or migration.** The release
  removes one exit-2 path from every settings reader and one refusal line
  from `chain-check`; no exit code changes for any other state.
- **The published v0.37.1 note keeps its date.** It names 2027-02-07 twice
  (`frame/design.md` G12). A person updating from 0.37.0 or earlier reads
  it before the 0.38.1 note, which says the paths left. Editing a published
  release is a GitHub write no agent makes (contract rule 6), and
  `frame/questions.md` names the assumption.
- **No `### Process changes` table** (`frame/design.md` G16).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-13 | Phase 1's census grep in *Phases* matches whole words and checks `unconverted_` apart | Phase 1's crafter found that the grep as framed could not print nothing: `OLD_TABLE` matched `COMMENTED_OLD_TABLE` and `config_shapes` matched `_Old_config_shapes`, both of which A5a keeps. The orchestrator ran the corrected form at `bf4f41711` and both commands exited 1. A crafter's statement in a frame file records what the build found, so the orchestrator folds it and spawns no framer | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph opening *The framer writes a decision's fold* |
| 2026-11-13 | Phase 2's Verified by cell, `frame/design.md` S8 and R22 are folded to what phase 2's build found | Phase 2's crafter found that the census grep also matches `docs/checks/the-stamp.md:95`, which a `## Rule changes` item removes, the dated experiment *Scope* puts out, and this work item's own records; that S8's search finds this work item's records; that the case reading no file cannot be reddened by a plant in `CLAUDE.md`, so its red came from mutating `IMPORT`; and that R22 did not name the *Procedure* clause that stood for step 4. The orchestrator ran both greps at `84631d9dc` and each printed what the folded cells name | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph opening *The framer writes a decision's fold* |
| 2026-11-13 | The second frame census that HEAD contradicted gets its prevention home in #1548, an issue on `agents/framer.md`, not in this work item | Both phases found a census command in a Verified by cell whose stated result its own patterns or scope made impossible. No spawn left in this run writes a census, so the problem cannot recur before the pull request; `agents/framer.md` is a file this work item does not change and #1422 of the same release may change, so a rule there built here would overlap that item | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph opening *A problem that recurs within a run gets a prevention home at once*, and *Orchestrator: where a decision or a lesson is written* |
