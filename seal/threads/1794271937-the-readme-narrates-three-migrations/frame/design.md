# Design: 1794271937-the-readme-narrates-three-migrations

## Grounding

The tree as read at `20f97977c` (`8657297d5`, the head of `release/v0.37.1`,
plus this work item's `routing.md`). Each row is labelled `executed` (a
command gave it) or `read` (the file was opened).

| Policy clause | What it fixes for this work |
|---|---|
| G1. `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*; `seal/config.json` has no `Policy root` key (executed: `cat seal/config.json`), so the policy root is `docs/` | This work changes documents' text and no code: the two READMEs, one sentence pair of `docs/checks/the-stamp.md`, and a new dated record under `docs/experiments/`. A work item whose subject is the policy root's text edits it directly, so `## Rule changes` holds the no-change block. The `the-stamp.md` edit replaces a narration with a citation and changes no rule |
| G2. `seal/threads/` holds this work item alone (executed: `ls seal/threads/`) | No unsettled design states a rule change, so the policy in force is `docs/` at `20f97977c` |
| G3. `skills/update/SKILL.md` *3. Name what changed.* prints the body of every release between the old version and the new one, and gives "anything the user has to do" a line of its own, "a compatibility fallback with an expiry" among it (read, lines 87–135). The 0.37.0 release note's *Updating* paragraph holds the `seal mode` conversion and the three files rewritten by hand, in the words `README.md:101-115` copies (executed: `gh release view v0.37.0 --json body`) | `/agentic:update` already tells a person coming from an earlier release what that release asks of them. The README's copy of the 0.37.0 note is a second copy. A removal date written into this work item's `changelog.md` reaches every person who runs `/agentic:update` through this same step |
| G4. `skills/update/SKILL.md` *4. Take out the preset block.* takes the `CLAUDE.md` block out after a backup (read, lines 137–213). *4b. The launcher an earlier release wrote.* reads whether the 0.33.0–0.34.1 launcher stands and names its two parts under *Needs action* (read, lines 215–233) | The update skill is the one home of both migrations. The README and `docs/checks/the-stamp.md` link to it and do not describe either |
| G5. `skills/config/SKILL.md` *A `config.md` standing in the root without a `config.json`* (read, lines 32–35) and `lib/config.py#unconverted_config` (read) both send a person to `seal mode` | Where a person meets the old `config.md`, the plugin already names the command. The README's list of which commands exit 2 and which read defaults is a copy of the refusal and of the 0.37.0 note |
| G6. Release history (executed: `gh release list`, `git log -1 --format=%ad v0.25.0`, `git tag --contains 591c136cc`). Releases 0.23.0 to 0.24.2 wrote the `CLAUDE.md` block, and 0.25.0 (2026-10-30) stopped writing it (read: `tests/behaviour/test_the_old_block_leaves_through_update.py` docstring). Releases 0.33.0 to 0.34.1 wrote the launcher, and 0.35.0 (published 2026-11-08) retired it. Releases through 0.36.0 read `seal/config.md`, and 0.37.0 (published 2026-11-09) reads `seal/config.json` alone | The dates the removal schedule in *Scope* item 7 counts from |
| G7. No policy document states how long a compatibility path stays (executed: `git grep -i 'compatib\|expir\|deprecat\|sunset'` over `docs`, `CONTRIBUTING.md`, `skills/update`, `skills/settle`, `templates/setup` and `lib/config.py`; the only hits are `skills/update/SKILL.md:135` and `:294`, which ask the update to name an expiry). No earlier frame set one (executed: the same grep over `seal/threads/` at `v0.35.0` and `v0.37.0`; 0.37.0's `frame/plan.md` A8 rejected reading both settings formats "for one release" and set no date for the converter) | The tree does not decide when the paths leave. *Scope* item 7 is this frame's default, and the owner reviews it at the pull request, as the spawn asks |
| G8. 32 version tags were cut from 2026-10-28 to 2026-11-09 (executed: `git tag -l 'v0.*' --format=...` filtered by date) | A count of releases measures nothing about how long a person goes without updating, so the schedule counts days |
| G9. `tests/behaviour/test_release_hygiene.py#test_no_loaded_file_names_a_version_at_or_above_the_running_one` refuses an untagged version at or above the running one, 0.37.1, in `README.md`, `README.ko.md`, `docs/`, `skills/` and `templates/`; a dated file under `docs/experiments/` is a record of a moment and keeps every version it names (read, `:43-51`, `:185-200`, `:565-588`) | No shipped file states the removal as a future version. The schedule is a date, and it stands in `changelog.md` and this frame |
| G10. `docs/experiments/README.md` (read): one file per experiment, named `<date>-<what-was-asked>.md`, in five sections, and a platform fact established there "lives under `docs/` and not with the work item that needed it". `docs/checks/`, `docs/running/` and `docs/layout/` cite no issue anywhere (executed: `git grep -E '#[0-9]{3,4}'` over them). The spike `docs/checks/the-stamp.md:125-127` names is issue #1376's comment 6675898172 of 2026-11-06, by the owner (executed: `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6675898172`), cited by `seal/threads/1793935041-the-directory-refuses-every-command-hook/frame/design.md` *Grounding* at `v0.33.0` (executed: `git grep -i spike v0.33.0 -- seal/threads/`) | The measurement moves into a dated record under `docs/experiments/`, transcribed from that comment, and `the-stamp.md` cites the record |
| G11. Tests that read the sentences this work moves (executed: `git grep` over `tests/` for `stamp.py`, `0.33.0`, `agentic:start`, `config.md`, the words "seal mode once", `pact-paths.md`, `### Updating`, `spike`; read each hit) | `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py#test_both_readmes_say_what_the_stamp_hook_writes_and_leaves` pins "`/agentic:update` names both for you to take out by hand." and its Korean twin "`/agentic:update` 가 이 둘을 알려 주면 사용자가 직접 지웁니다." (read, `:240-330`). No test pins the README's `CLAUDE.md` block paragraph's wording, though `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#test_every_template_is_named_by_a_document_that_ships` needs some shipped document to name `templates/setup/claude-md-block.md`, which only that paragraph did (found red in phase 1; the case now exempts the template by name, `READ_BY_AN_EARLIER_RELEASE`), its `config.md` paragraph, or the launcher and spike sentences of `docs/checks/the-stamp.md` (`stamp_section`'s asserts read, `:140-190`). `tests/behaviour/test_both_editions_carry_the_same_folds.py` reads the two READMEs' heading outline. `tests/behaviour/test_docs_line_wrap.py` covers both READMEs and lists each `docs/experiments/` file "at birth" (read, `:109-117`, `:163-168`). `tests/behaviour/test_a_cited_section_stands_in_its_file.py#sections` resolves a citation to a bold lead, so `skills/update/SKILL.md` *4b. The launcher an earlier release wrote* resolves (read, `:168-200`) |
| G12. Issue #1492 has no comments (executed: `gh issue view 1492 --json body,comments`, 2026-11-10) | The issue body is the whole request |
| G13. `seal/follow-up.md` holds no row on these paths (executed: `grep -n -i 'launcher\|config.md\|block'`), and says this repository has a tracker, so it should hold no schedulable item (read, lines 5–7) | The removal is scheduled through the tracker and the release note, not through `seal/follow-up.md` |

## Scope

**In.**

1. `README.md` *Updating*: the paragraph on the `CLAUDE.md` block
   (`README.md:95-99`) and the paragraph on `seal/config.md`
   (`README.md:101-115`) become one paragraph. It says that `/agentic:update`
   takes out what an earlier release wrote into their `CLAUDE.md`, and
   names what an earlier release left that only they can remove, with a link
   to `skills/update/SKILL.md`. It keeps two things for a person who updates
   without `/agentic:update`: the `seal mode` line (run it once in each
   repository that holds `seal/config.md`; it writes `seal/config.json` and
   removes the old file), and the files rewritten by hand (`seal/parity.md`
   to `seal/parity.json`, a `seal/pact.md`'s `| Signer |` table to a
   `Pact signers` key, `~/.claude/agentic/pact-paths.md` to
   `~/.claude/agentic/pact-paths.json`). The block's markers, the empty
   marker pair, `templates/setup/claude-md-block.md`, and the list of which
   commands exit 2 or read defaults until the conversion leave the README.
   The first paragraph, the by-hand update commands and the
   `seal pr-checks` paragraph stay as they are.
2. `README.md` *What runs on your machine*: the launcher's two sentences
   (`README.md:368-372`, from "Releases 0.33.0 to 0.34.1 drew the stamp")
   become one sentence. It says that a release from 0.33.0 to 0.34.1 may have
   left a launcher of its own that also runs at a turn's end, and that
   `/agentic:update` names it for the person to remove, with a link to
   `skills/update/SKILL.md` *4b. The launcher an earlier release wrote*. It
   names none of the launcher's files, no settings entry and no command.
3. `README.ko.md` *업데이트* (`README.ko.md:99-118`) and *내 컴퓨터에서 도는
   것* (`README.ko.md:365-369`): *Scope* items 1 and 2 in the Korean edition,
   with the same content and the same heading outline.
4. `docs/checks/the-stamp.md` *The stamp*: the launcher's description
   (`:94-98`, from "A release from 0.33.0 to 0.34.1 wrote") becomes a
   citation of `skills/update/SKILL.md` *4b. The launcher an earlier release
   wrote*. The rule the stamp keeps stays: where that launcher still runs
   beside the plugin's hook, a file is drawn once, since drawing claims the
   file first. The measurement clause (`:125-127`, "the owner's spike of
   2026-11-06 proved …") cites the record of *Scope* item 5 in place of the
   spike.
5. A new dated record under `docs/experiments/`, named
   `2026-11-06-<what-was-asked>.md` with the slug the crafter chooses, in the
   five sections `docs/experiments/README.md` gives. It transcribes what issue
   #1376's comment 6675898172 recorded about the stamp's hook on Claude Code
   2.1.319: a `Stop` command hook in the person's own settings runs as a
   plugin's does, without `CLAUDE_PLUGIN_ROOT` or the plugin's `bin/` on
   `PATH`; `${CLAUDE_PLUGIN_DATA}` survives updates and is substituted in a
   skill body; no other surface kept the stamp's four properties; a skill's
   `hooks:` frontmatter runs a command hook. It names the comment as its
   source, and its *What it did not establish* says the scratch plugin is
   not in this repository and the comment records results, not steps, so the
   method is the comment's account (folded after phase 1). The file joins
   `tests/behaviour/test_docs_line_wrap.py`'s covered list, as its siblings
   did at birth. It has no Korean edition.
6. The tests that pin the moved sentences change in place.
   `test_both_readmes_say_what_the_stamp_hook_writes_and_leaves` pins *Scope*
   item 2's sentence in each edition in place of the two it pins now, and its
   list of what is gone gains the launcher's old description (in English, "a
   launcher, `stamp.py`"; in Korean, "실행기 `stamp.py`").
   `test_the_policy_names_the_command_the_marker_and_the_command_to_draw`
   gains an assert that *The stamp* cites `skills/update/SKILL.md` *4b. The
   launcher an earlier release wrote* and no longer holds
   `${CLAUDE_PLUGIN_DATA}/stamp.py`. Each new assert is seen red against the
   sentence it replaces.
7. **The removal schedule.** Each compatibility path below leaves in the
   first release cut on or after 2027-02-07, together, in one work item.
   That date is 90 days after 0.37.0, the latest of the releases that stopped
   writing the old state (G6), so each path stands at least 90 days. Ninety
   days is this frame's default: the plugin publishes no support window, and
   nothing in the tree measures how long a person goes between updates (G7,
   G8). The owner sets it at the pull request. The schedule reaches persons
   as one *Updating* sentence in this work item's `changelog.md`, which
   `/agentic:update` step 3 then names as "a compatibility fallback with an
   expiry" (G3). The coordinates each removal touches are a sample from
   `git grep` on each path's words, so the removal's frame lists them whole.

   | Path | Wrote the old state | Stopped at | What the removal takes out (sample) |
   |---|---|---|---|
   | The `CLAUDE.md` block | 0.23.0 to 0.24.2 | 0.25.0, 2026-10-30 | `skills/update/SKILL.md` *4. Take out the preset block.*; `templates/setup/claude-md-block.md`, which 0.24.x's own update step diffs against; `tests/behaviour/test_the_old_block_leaves_through_update.py`; `tests/behaviour/test_release_hygiene.py#test_update_names_the_marker_of_the_block_it_takes_out`; the `READ_BY_AN_EARLIER_RELEASE` exemption in `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`; the README clause of *Scope* item 1 |
   | The stamp's launcher | 0.33.0 to 0.34.1 | 0.35.0, 2026-11-08 | `skills/update/SKILL.md` *4b. The launcher an earlier release wrote.* and the mention of step 4b in step 2; `tests/behaviour/test_update_reads_the_config_directory_in_use.py#test_step_4b_reads_the_old_launcher_and_writes_nothing`; *Scope* items 2 and 4's sentences and their pins |
   | The settings in `seal/config.md`, and the `parity.md` refusal of the same release | through 0.36.0 | 0.37.0, 2026-11-09 | `lib/config.py#unconverted_config`, `#old_config_path`, `#unconverted_parity` and the refusal arm of `#config_pairs`; `seal mode`'s converter in `skills/implement/scripts/seal.py`; the refusals in `skills/code-review/scripts/chain_check.py` and `skills/verify/scripts/broad_gate.py`; `skills/config/SKILL.md:32-35`; `templates/setup/config.md:55-65`; `docs/layout/one-root-by-lifetime.md:268` and `.ko.md:246`; `docs/checks/the-fold.md:118`; `docs/checks/the-pull-request-check.md:111`; `skills/parity-setup/SKILL.md:25`; the README lines *Scope* item 1 keeps; the cases in `tests/lib/test_config.py`, `tests/skills/test_seal.py`, `tests/skills/test_broad_gate.py`, `tests/skills/test_fold_check.py` and `tests/skills/test_pr_body.py` that hold the refusal |

**Out.**

- Removing any compatibility path now. The newest is one day old (G6), and
  removing one would turn a documentation change into a change of
  `lib/config.py`, `seal.py`, the update skill and their tests.
- `skills/update/SKILL.md`, `skills/config/SKILL.md` and `lib/config.py`.
  They are the homes the README links to, and they already say what
  this work needs (G4, G5).
- Filing the removal's issue. The orchestrator files it, or the owner at the
  pull request; a framer posts nothing.
- A Korean edition of the new experiment record. Only `the-stamp.md`, which
  has none, cites it.
- `skills/update/SKILL.md` step 4b's clause "a stamp is still drawn once,
  since drawing claims the file first", which `the-stamp.md` also states.
  The issue makes step 4b the launcher's one home and keeps the drawing rule
  in `the-stamp.md`; the step's clause tells the person why nothing draws
  twice, and the removal of step 4b takes it out.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A person updates with `/agentic:update` from 0.24.x, 0.34.x or 0.36.x | Given `README.md` *Updating* at the build's commit, when they read it, then one paragraph says what `/agentic:update` does for a person from an earlier release and links to `skills/update/SKILL.md`, and nothing in the section describes the `CLAUDE.md` block's markers or the launcher | read; `git grep -n -e 'agentic:start' -e 'claude-md-block' -e '`stamp.py`' -- README.md README.ko.md` prints nothing (the code span keeps `seal_stamp.py`, the plugin's own hook, out of the match; folded after phase 1) |
| A person updates by hand from 0.36.x and never runs `/agentic:update` | Given the same section, when they read it, then it tells them to run `seal mode` once in each repository holding `seal/config.md`, and names the files they rewrite by hand with what each becomes | read; `git grep -n 'seal mode' -- README.md README.ko.md` hits *Updating* and *업데이트* |
| A Korean reader | Given `README.ko.md`, when they read *업데이트* and *내 컴퓨터에서 도는 것*, then each carries what its English twin carries | read; `tests/behaviour/test_both_editions_carry_the_same_folds.py` passes |
| A person still holding the 0.33.0–0.34.1 launcher reads what runs on their machine | Given *What runs on your machine*, when they read it, then one sentence says such a launcher may also run at a turn's end and links to update step 4b | `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py#test_both_readmes_say_what_the_stamp_hook_writes_and_leaves`, seen red against the old sentence |
| A reviewer reads the stamp's policy | Given `docs/checks/the-stamp.md` *The stamp*, when they look for the launcher, then they find a citation of update step 4b and the draw-once rule, and no launcher path or settings entry; the measurement clause cites a `docs/experiments/` record | `test_the_policy_names_the_command_the_marker_and_the_command_to_draw`, seen red; `tests/behaviour/test_a_cited_section_stands_in_its_file.py` passes |
| A reader opens the experiment record | Given the new file, when they read it, then its five sections stand in the order `docs/experiments/README.md` gives and its source is issue #1376's comment | read; `tests/behaviour/test_docs_line_wrap.py` and `tests/behaviour/test_release_hygiene.py` pass |
| A person runs `/agentic:update` onto 0.37.1 | Given the 0.37.1 release note, when step 3 prints it, then one *Updating* sentence names the date in *Scope* item 7 after which the compatibility paths leave | read `changelog.md` at the build's commit |

## Data & interfaces

No schema, endpoint, command, exit code or printed message changes. The
interface a person reads changes: the two READMEs, one policy document's
paragraph pair, a new experiment record, and one *Updating* sentence of the
release note.

## Rule changes

- nothing
  why: The only policy document this work edits, `docs/checks/the-stamp.md`, gets a citation in place of a narration and a record in place of an attribution; no rule changes, and the work edits `docs/` directly as G1 says.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `CLAUDE.md` block paragraph: its markers, the empty marker pair and `templates/setup/claude-md-block.md` | `README.md` *Updating*, lines 95–99 | `skills/update/SKILL.md` *4. Take out the preset block.*, which the one paragraph links, for the block; the template's reason to stand is the comment above `READ_BY_AN_EARLIER_RELEASE` in `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` |
| The `config.md` paragraph's account of which commands exit 2, refuse or read defaults until the conversion | `README.md` *Updating*, lines 101–115 | `lib/config.py#unconverted_config`'s refusal, `skills/config/SKILL.md` *A `config.md` standing in the root without a `config.json`*, and the 0.37.0 release note, which `/agentic:update` step 3 prints |
| The launcher's description: its file, the settings entry, and that `/agentic:update` names both | `README.md` *What runs on your machine*, lines 368–372 | `skills/update/SKILL.md` *4b. The launcher an earlier release wrote.*, which the one sentence left there links |
| The same three passages in Korean | `README.ko.md` *업데이트*, lines 99–118, and *내 컴퓨터에서 도는 것*, lines 365–369 | the same homes |
| The launcher's description: its path under `${CLAUDE_PLUGIN_DATA}`, the `Stop` entry, and that it runs until both are removed | `docs/checks/the-stamp.md` *The stamp*, lines 94–98 | `skills/update/SKILL.md` *4b. The launcher an earlier release wrote.*, which the paragraph cites; the draw-once rule stays |
| "the owner's spike of 2026-11-06 proved" as the measurement's only source | `docs/checks/the-stamp.md` *What the person's screen shows is not checked*, lines 125–127 | the new `docs/experiments/2026-11-06-…` record of *Scope* item 5 |
| The pins on the launcher sentence, "`/agentic:update` names both for you to take out by hand." and its Korean twin | `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py#test_both_readmes_say_what_the_stamp_hook_writes_and_leaves` | the same case, pinning *Scope* item 2's sentence |

Framed 2026-11-10 by framer, before the build.
