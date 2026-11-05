# Design: `seal unverified --baseline` leaves (#1240)

## Grounding

Each row states the tree at a0303ee9, the base the frame was drawn on, unless it names another commit; the phases change several of the facts the rows cite.

| Policy clause | What it fixes for this work |
|---|---|
| Issue #1240, body rewritten 2026-11-05, and its two comments (executed: `gh issue view 1240 --json body,comments`) | The owner's decision is not reopened here. The `--baseline` mode of `seal unverified` leaves, and so does the code that compared a base listing with the scan's memos. `seal unverified` without `--baseline` stays. Every document, test and comment that named the mode says what stands now: the proofer reads a deleted row or memo in the closing memo's diff. #1238 and #1264 need nothing more. |
| Milestone `release: 0.32.5` (executed: `gh api repos/MichaelYcJo/AgenticSeal/milestones/89 --jq .description`) | A patch, and it builds no feature. A check whose edge fixes keep coming is kept, narrowed or removed according to its record. |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | The same change removes what stood on the old fact: each check, comment, copy and test pin that assumed the mode exists. Before an existing structure is kept, the frame asks whether it should change (plan *Alternatives considered*). |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | The subject of this work item is the code: a command loses a mode. The policy root changes only because the code changed, so the `docs/` sentences that state the mode go through `## Rule changes` below and wait for the settle. `skills/`, `README*.md`, tests and code are not the policy root, so the build edits them in place. |
| `skills/implement/SKILL.md` *4. The closing memo* lines 376-386 (read) | The proofer reads the closing memo's diff, where a row that left without `closed` shows. Today the same sentence adds that `seal unverified --baseline origin/<base>`, run by a person, names each such row. The paragraph after it ("What the command reads is the **number** of rows") describes that comparison. Once the mode is gone, the proofer's reading is the only one left. |
| Who runs the mode (executed: `git grep -n -e "--baseline"` with the threads excluded) | The only places that tell a person to run it are `skills/implement/SKILL.md:378` and `skills/verify/SKILL.md:231`. The `--baseline` that appears in `.github/`, `templates/setup/`, `agents/` and `skills/verify/scripts/broad_gate.py` is `chain_check.py`'s own flag, and the one in `payload_meter.py` is that script's own flag. No CI step runs `seal unverified` at all. The hygiene step that ran it went in `5daa931f` (executed: `git log -S unverified_check -- templates/setup/hygiene.yml .github/workflows/hygiene.yml`). |
| What other scripts take from the module (executed: `grep -o 'reader\.[a-z_]*'` over `chain_check.py` and `settle.py`, `grep 'uc\.'` over `fold_check.py`, then a `git grep -w` of each candidate name outside the module and its test module) | `chain_check.py` uses `annotate`, `gfm_lines`, `heading_level`, `headings`, `merge_base`, `policy_root`, `readable`, `repo_root`, `resolves`, `rule_changes`, `settled` and `split_row`. `settle.py` uses `check_text`, `NOTHING`, `open_record_rows`, `OVERVIEW`, `policy_root` and `show`. It calls `open_record_rows` with `ref` None only (`settle.py:944`, `:1795`), calls `check_text` on text read from disk (`:1770`), and calls `show` on a design, not on a `gaps.md` (`:1222`). `fold_check.py` uses `live_lines`, `gfm_lines`, `split_row` and `is_separator`. No file outside `skills/verify/scripts/unverified_check.py` and `tests/skills/test_unverified_check.py` names `repository_of`, `as_named`, `_absolute`, `spellings`, `real`, `nearest_existing`, `base_label`, `overviews_at`, `mode_at`, `LINK_MODE` or `compare_at`. |
| The module already holds code for `chain_check.py` alone (executed: `grep -n -w rule_changes skills/verify/scripts/unverified_check.py`) | `rule_changes` is defined at line 1419, and nothing else in the module calls it. A predicate that only `chain_check.py` calls after this change therefore matches a shape the module already has. |
| How the scan read its arguments before #1225 (executed: `git show bf9efcba^:skills/verify/scripts/unverified_check.py`, `def overviews`) | `overviews` resolved each argument once, with `p = real(p)`. #1225 (`bf9efcba`, `55b66958`) changed this to `as_named` so that the base comparison would read a named link at its own path (see the `as_named` docstring). That reason leaves with the base comparison. |
| The relaxed reading of a record at a ref (read: `check_text`'s docstring at `a0303ee9`; executed: `git grep -n -w` of `strict_header`, `LOOSE_HEADING`, `_text_at`, `open_record_rows` and `sections`, and `git log -S'open_record_rows(records, None' -- skills/settle/scripts/settle.py`) | The relaxation was built for base revisions written before the corpus was normalised, and its docstring said it "ends when every base carries the canonical wording". It is made up of `check_text`'s `heading` and `strict_header` arguments, the regex arm of `sections`, `parse_section`'s three relaxations under `strict_header=False`, and the ref arm of `open_record_rows` together with `_text_at`. Two callers reached it. The first was `compare_at`, which phase 1 removed (`a9661924`). The second was `open_record_rows` at a ref, and no shipped caller has reached that since `fa7d1374` (2026-10-27), when `settle.py` began passing `None`. `pr_body.py:448` and `tests/behaviour/test_the_sealer_guarantees.py` call `sections` with a string heading. |
| Rule markers (executed: `git grep -n 'mark.rule('` under `tests`, at `a0303ee9` and again at `7d8674e5`) | At `a0303ee9`, `one-merge-base` was carried only at `tests/skills/test_unverified_check.py:2704`, a `--baseline` case, and `a-settle-is-no-deletion` only at `:2775` and `:2803`, both `--baseline` cases. At `7d8674e5`, after phase 1, `one-merge-base` is carried nowhere, and `a-settle-is-no-deletion` is carried only at `tests/skills/test_chain_check.py:4026`. `an-empty-root-is-settled` is also carried at `tests/skills/test_settle.py:2510,2530`. `nothing-declared-nothing-owed` is also carried at `tests/skills/test_chain_check.py:4054,4086` and in `tests/e2e/teammate/test_teammate_flow.py`. `record-comment-line-refused` is also carried in the chain_check, rule_changes and seal_stamp test modules. |
| `skills/settle/rule-changes.md` *A rule has one shape* and `.github/scripts/rules.py` lines 42-51 (read) | `seal rules --check` excuses a refused check line inside a section that a pending `remove` with no `from` will take out at the settle. A pending `change`, or a `remove` with a `from`, excuses nothing, so the test that a line names has to stay until the settle. |
| `evals/README.md` *A proofer comparison compares two sides taken from the same point* (read, lines 78-83) and `evals/behaviour/proofer/seeded-55b66958/scaffold.sh` (read) | Removing a case changes the suite's tree, and `compare` refuses a pair of sides taken across that change. The case's scaffold fetches `ab958884` and `48d035aa` from the remote and reads nothing in the current tree. |
| Unsettled designs on the same documents (executed: `grep -n -A2 'file: docs/...'` over `seal/threads/*/frame/design.md`) | `1793853197` changes two other paragraphs of `docs/layout/the-record-layout.md` *seal/threads/<work-item-id>/*. `1793732301` changes a paragraph of *The root records*. None of them names `docs/checks/the-unverified-record.md`, `docs/checks/the-fold.md` or `docs/README.md`. |
| `routing.md` (read) | Planning framer, Implementation crafter, Review through the review chain, Automation yes. |

## Scope

In:

1. **`unverified_check.py#main` takes no `--baseline`.** The following go: the argparse option, the block that resolves the base, the branch for a missing path under a baseline, the per-file comparison, the loop over owed spellings, the loop over memos that left and their settles, the `deleted`, `uncompared` and `settles` reports with their fields in the summary line, and the messages `rows left the record without being closed` and `Re-add the row …`. Exit 1 means a section could not be read, and nothing else. `--baseline` is an unknown argument, so argparse refuses it with exit 2.
2. **The units only the base comparison used go:** `repository_of`, `as_named`, `_absolute`, `spellings`, `real`, `nearest_existing`, `base_label`, `overviews_at`, `mode_at`, `LINK_MODE` and `compare_at`, together with each import that only they used (`errno` and `pathlib` are candidates, and ruff's unused-import rule settles which).
3. **`overviews` reads each argument at its real path** (`os.path.realpath`), as it did before `bf9efcba`. The comment says why: the reference-root rule measures the path against the top that `git rev-parse --show-toplevel` gives with links resolved.
4. **The units that stay keep their code, and their text names the callers they have today.** `commit_of`, `resolves`, `merge_base`, `settled` and `tree_at` serve `chain_check.py`. `show`, `open_record_rows` and `under_root` serve `settle.py`. `repo_relative`, `git_path`, `display_path`, `unique_by_target` and `annotate` stay too. In `check_text`, the sentence that calls a base refusal the `--baseline` loop's `not compared` notice goes. `settled_root`, `absent_root` and `unwritten_root` stay, and so do their messages. `ABSENT` drops "and nothing to compare against the base", and the comment above its call in `main` drops the base. The module docstring drops the `fewer rows` and `no baseline` failure kinds and the paragraph *The base is the merge base, not the ref*. Its exit-code paragraph keeps the three exit-0 states.
5. **`tests/skills/test_unverified_check.py`.** Every case that runs `--baseline` goes, and so does the class of each unit removed in item 2. A case that pins a property of the plain run next to a baseline one keeps the plain run: the parametrized `baseline`/`plain` cases at 2855, 2876, 2886, 2906 and 2935, the walk over a team's `specs/` (2950), a person naming a team overview (2962), a copy with no `hooks/` (2973), and a tracked link counted once (2430). Each fixture that nothing uses after that goes. `test_accepts_the_baseline_help_naming_both_places` is replaced by the acceptance case A1.
6. **The marker `a-settle-is-no-deletion` moves** to `tests/skills/test_chain_check.py`'s case that reads a declaration a settle removed (`test_accepts_a_declaration_a_settle_removed`, at about line 4026). It moves in the same commit that removes the two cases now carrying it. In `Test_module::test_every_reader_of_a_retirement_calls_the_one_predicate`, the docstring names one reader, `chain_check.py`, and the pin stays: it keeps a second `settled` from being defined there.
7. **`tests/behaviour/test_unverified_rows_close.py`.** `test_the_skill_names_the_command_that_lists_a_deleted_row`, `test_the_documents_state_the_merge_base_footing` and `TIP_EN` go.
8. **`tests/behaviour/test_a_reference_root_is_read_and_never_taken.py:55`.** The reason given for `seal unverified` drops "and the base".
9. **`skills/implement/SKILL.md` *4. The closing memo*.** The clause that names `seal unverified --baseline origin/<base>` goes. The paragraph "What the command reads is the **number** of rows …" is rewritten to say that no check judges whether the second cell of a closed row says what closed the item: `seal unverified` refuses the cell only where it is empty or the template's placeholder, and `seal settle` prints it as it stands, so only a reader catches a closing that goes out unproven. A paragraph in `skills/code-review/SKILL.md` stage 1 tells the proofer to read each `gaps.md` the range changes for a row or a memo that left without the word `closed` (round 1, findings 1 and 2).
10. **`skills/verify/SKILL.md` *And something has to read the row afterwards*.** The second command line and the paragraph that opens "**`--baseline` names the branch**" go. In their place, one sentence says that the proofer reads a deleted row in the closing memo's diff, and cites `skills/implement/SKILL.md` *4. The closing memo*.
11. **`README.md:347` and `README.ko.md:350`.** The `seal unverified` row drops `[--baseline <ref>]`.
12. **The relaxed reading of a record at a ref leaves** (design *Grounding*, the relaxed-reading row):
    - `check_text(text)` takes no `heading` and no `strict_header`, and `sections` keeps only its string arm.
    - `parse_section` takes no `strict_header`. A section is read strictly whatever its source: the header is exactly `HEADER`, a row opening with U+2705 is refused with the edit named, and an old `none — <why>` line is prose, which `unread_block` names.
    - `open_record_rows(root, directory)` reads the record on disk, and `_text_at` goes. `settle.py:944` and `:1795` drop their `None`.
    - `LOOSE_HEADING` stays for the near-heading hint `check_text` gives, and its docstring names that one use.
    - In `tests/skills/test_unverified_check.py`, the following go: `Test__text_at`, the ref cases of `Test_open_record_rows`, the `legacy` fixture and `LEGACY`, the `strict_header=False` cases of `Test_parse_section`, and the regex case of `Test_sections`. Each other fixture left unused goes with them.
    - A new case is written only where removing a relaxation changes what the plain run says. Contract rule 15 applies to it.

Out:

- Rebuilding the comparison on `os.path.samefile`. The owner decided against it on 2026-11-05.
- Removing the exit-0 states `settled_root`, `absent_root` and `unwritten_root`. These apply to the plain run, which the owner kept (plan *Alternatives considered*, row 4).
- Moving `settled`, `tree_at`, `resolves`, `merge_base` and `commit_of` into `chain_check.py` (plan *Alternatives considered*, row 3).
- `evals/behaviour/proofer/seeded-55b66958/`. It stays as it is (plan *Alternatives considered*, row 6).
- `skills/implement/scripts/seal.py:2078` and `:2672`. Both cite `unverified_check.py#absent_root` as one step of the shipped workflow, but no workflow step has run `seal unverified` since `5daa931f`. That claim was already stale before this work and does not stand on `--baseline`. `absent_root` stays, so both citations still resolve.
- `.test_durations`. Stale ids drop no case (`CONTRIBUTING.md`, lines 166-167), and the contributor refreshes the file from a CI artifact.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A1 the mode is gone | Given the built tree, when a person runs `seal unverified --baseline HEAD .`, then argparse refuses the unknown argument with exit 2, and `seal unverified --help` names no `--baseline` | A new case in `tests/skills/test_unverified_check.py::Test_main`, seen red against `a0303ee9` (where the run exits 0 and the help names the option) |
| A2 the plain run is unchanged | Given open rows, an unreadable section, a missing path, a settled, absent or unwritten root, or a tracked link to a memo, when `seal unverified <path>` runs, then it exits 0, 1, 2, 0 and 0 as today, and counts the linked memo once | The kept plain cases of `Test_main`, unchanged in what they assert |
| A3 the settle reading at the pull request is unchanged | Given a declaration whose directory stood at the merge base and is gone whole, when `chain_check.py` runs, then it prints `retired: a settle` through `unverified_check.py#settled`, and `a-settle-is-no-deletion` is carried by that case | `tests/skills/test_chain_check.py`; the marker carried there, read with `git grep -n 'a-settle-is-no-deletion' -- tests` |
| A4 the settle reads a record as the plain run does | Given a released work item's `gaps.md` in the working tree, when `seal settle` lists its open rows, then `open_record_rows` reads it with the plain run's strict reader. A section that reader cannot read becomes one entry saying so, never zero rows | `tests/skills/test_unverified_check.py`, `Test_open_record_rows` (line 1743 at `7d8674e5`), and `tests/skills/test_settle.py` |
| A5 no text states the mode | Given the built tree, when `git grep -n -e "seal unverified --baseline" -e "\[--baseline <ref>\]" -- ':!seal/threads'` runs, then it names nothing outside the policy root. Under `docs/` it names `docs/checks/the-fold.md:21`, the `from` of a pending `## Rule changes` operation that the settle rewrites (plan *Alternatives considered* row 7); the design's own copies of the `from` values stand under `seal/threads`, which the command leaves out | That command, run by the proofer |
| A6 a deleted row is the proofer's to read | Given `skills/implement/SKILL.md` *4. The closing memo*, then it says the proofer reads the memo's diff and names no command that lists a deleted row | Read by review |

## Data & interfaces

- CLI: `seal unverified [path ...]`. It has no option except `-h`. Exit 0: the record is readable, or one of the three named states holds. Exit 1: a section could not be read. Exit 2: a path or argument is unusable, `--baseline` among them.
- Module surface kept for other scripts: everything that `chain_check.py`, `settle.py`, `fold_check.py`, `passages.py`, `rule_changes.py`, `pr_body.py`, `coordinates.py`, `payload_meter.py`, `.github/scripts/*` and `evals/scripts/replay_targets.py` load (*Grounding*, the importers row). Scope item 2 lists the names that leave the surface. Scope item 12 changes two signatures: `open_record_rows(root, directory)` and `check_text(text)`. It also removes `_text_at`.

## Rule changes

- remove
  file: docs/checks/the-unverified-record.md
  section: The unverified record, and the baseline it is read against
- add
  file: docs/checks/the-unverified-record.md
  section: The unverified record
  to: **A pull request that declares nothing owes the unverified check
    nothing.** Handed a `seal/` root's own `threads` path, `seal unverified`
    exits 0 and names the state in two more cases beside the settled root:
    where no `seal/` directory is in the tree, and where `threads/` holds
    work items none of which carries a `gaps.md`. There is no row to read.
    Every other path holding no `gaps.md` is still exit 2, which keeps a
    misspelt path from passing in silence.
    check: nothing-declared-nothing-owed
- change
  file: docs/README.md
  section: docs/checks/
  from: | `docs/checks/the-unverified-record.md` | what `unverified_check.py` reads, and the baseline it reads against |
  to: | `docs/checks/the-unverified-record.md` | what `unverified_check.py` reads, and the states in which it reads no row |
- change
  file: docs/checks/the-fold.md
  section: The fold, and what tells it from a deletion
  from: One predicate, `unverified_check.py#settled`, answers
    `seal unverified --baseline` and `chain-check`.
  to: `chain-check` asks one predicate, `unverified_check.py#settled`.
- change
  file: docs/checks/the-fold.md
  section: The fold, and what tells it from a deletion
  from: and `seal unverified --baseline` would read the root's own `threads`
    path as a typo when a person runs it after the fold, and refuse a
    finished settle.
  to: and `seal unverified` would read the root's own `threads` path as a
    typo when a person runs it after the fold, and refuse a finished settle.
- change
  file: docs/checks/the-fold.md
  section: The fold, and what tells it from a deletion
  from: **A line a record's rows are COUNTED on is blanked the same way on both
    sides of a comparison.** `unverified_check.py#readable` blanks fenced lines
    with the indices intact, and a fence nobody closed to the end of the file.
    It reads a comment as text, because a record carries none, and the reader
    that judges a record refuses a line that begins with `<!--`. So the working
    tree and the base revision count the same
    table, and the readers that judge a record refuse a hidden table as absent
    rather than read it as empty.
  to: **A line a record's rows are COUNTED on is blanked where a fence holds
    it.** `unverified_check.py#readable` blanks fenced lines with the indices
    intact, and a fence nobody closed to the end of the file. It reads a
    comment as text, because a record carries none, and the reader that
    judges a record refuses a line that begins with `<!--`. So the readers
    that judge a record refuse a hidden table as absent rather than read it
    as empty.
- remove
  file: docs/layout/the-record-layout.md
  section: seal/threads/<work-item-id>/
  from: A base revision that holds such a line is not compared, because
    nobody can edit a commit that already happened.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `--baseline` option and every arm that compares against a base | `skills/verify/scripts/unverified_check.py#main` | Nowhere. The owner's decision (#1240). The proofer reads a deleted row or memo in the closing memo's diff (`skills/implement/SKILL.md` *4. The closing memo*) |
| The units only the base comparison used | `skills/verify/scripts/unverified_check.py#repository_of`, `#as_named`, `#_absolute`, `#spellings`, `#real`, `#nearest_existing`, `#base_label`, `#overviews_at`, `#mode_at`, `#LINK_MODE`, `#compare_at` | Nowhere. No other file names them (*Grounding*, the importers row) |
| The module docstring's `fewer rows` and `no baseline` kinds and its merge-base paragraph; the base sentences in the docstrings of `check_text`, `overviews`, `git_path`, `repo_relative`, `unique_by_target`, `commit_of`, `resolves`, `merge_base`, `settled`, `open_record_rows`, `settled_root` and `unwritten_root`, and in `ABSENT` | `skills/verify/scripts/unverified_check.py` | Each docstring states what its unit does for the callers it has today (Scope item 4) |
| The `--baseline` cases, the unit classes of the removed units, and the fixtures only they used | `tests/skills/test_unverified_check.py` | Nowhere. What a plain-run case pinned stays in its plain run (Scope item 5) |
| The pin that the help names the fork point and the base's tip | `tests/skills/test_unverified_check.py#Test_main.test_accepts_the_baseline_help_naming_both_places` | Replaced by A1, which pins that the option is gone |
| The marker `one-merge-base` and its only case | `tests/skills/test_unverified_check.py:2704` | Nowhere. Its rule leaves with the section that the `remove` above takes out, and `seal rules --check` excuses its check line until the settle |
| The marker `a-settle-is-no-deletion` on two `--baseline` cases | `tests/skills/test_unverified_check.py:2775`, `:2803` | `tests/skills/test_chain_check.py`, the settled-declaration case (Scope item 6) |
| Two pins on the mode's prose | `tests/behaviour/test_unverified_rows_close.py#test_the_skill_names_the_command_that_lists_a_deleted_row`, `#test_the_documents_state_the_merge_base_footing` | Nowhere. The prose they pinned goes in Scope items 9 and 10 |
| The command a person ran to list deleted rows | `skills/implement/SKILL.md` *4. The closing memo*; `skills/verify/SKILL.md` *And something has to read the row afterwards* | The proofer's reading of the memo's diff, which the first already states |
| `[--baseline <ref>]` in the command row | `README.md` *Commands*, `README.ko.md` *명령* | Nowhere |
| The rule *A baseline reference is resolved once, to a merge base* and the sentence on comparing nothing against the base | `docs/checks/the-unverified-record.md` *The unverified record, and the baseline it is read against* | Nowhere for the first. The rest of the section lands under *The unverified record* (`## Rule changes`) |
| The relaxed reading at a ref: `check_text`'s `heading` and `strict_header`, the regex arm of `sections`, `parse_section`'s `strict_header` and its three relaxations, the ref arm of `open_record_rows`, and `_text_at` | `skills/verify/scripts/unverified_check.py#check_text`, `#sections`, `#parse_section`, `#open_record_rows`, `#_text_at` | Nowhere. It was built for base revisions, and no shipped caller reaches it after phase 1 (Scope item 12). A record a strict reader cannot read is one entry saying so |
| The cases and fixtures of that reading | `tests/skills/test_unverified_check.py#Test__text_at`, the ref cases of `#Test_open_record_rows`, `#legacy`, `#LEGACY`, the `strict_header=False` cases of `#Test_parse_section`, the regex case of `#Test_sections` | Nowhere |
| The claim that the working tree and the base revision count the same table | `docs/checks/the-fold.md` *The fold, and what tells it from a deletion* | Nowhere. The comparison left with `--baseline`, and the rule keeps the fence blanking it still states |
| The sentence that a base revision holding a comment line is not compared | `docs/layout/the-record-layout.md` *seal/threads/<work-item-id>/* | Nowhere. That comparison was the mode's |

Framed 2026-11-05 by framer, before the build.
