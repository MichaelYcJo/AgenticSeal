# Implementation Plan: the scribe and legacy-parity are written anew from the scribe's job (#970)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved <date> by <who>, when `smith` was spawned.

## Summary

The scribe's definition is written to the shape #957 gave the warden and the
smith: it preloads the contract alone and opens `skills/legacy-parity/SKILL.md`
at its first step, reading the sections that find and trace an original and
leaving the judging and recording sections to its caller. `legacy-parity` is
written to the same shape: its verdicts become four words, its record of a
comparison names who writes it, its field table points at
`templates/parity.md`, and no file proposes creating `docs/policies/`. The
skip entries that waited on this item leave, both files join the line-wrap
check, and the rewrite is measured on bytes, with the read set and not the
preload alone as the figure that has to hold.

## Technical context

Read at 1d665d48 (= 43cbc361 outside `seal/specs/`); `spec.md` §*How the
rewrite is measured* holds the byte figures, `executed`.

- **The model.** `agents/smith.md` (172 lines, 10,276 B) and `agents/warden.md`
  (167, 10,570): the contract sentence, `## Job` naming the writes, numbered
  steps whose step 1 opens a skill and says its paths are the plugin's,
  `## Never` one line each, `## Rules` each ending `Enforced by:`. #967's
  `phases/phase-2.md` §*The pins (Q5), sorted* is the shape of the pin sort.
  `skills/code-review/SKILL.md` (rewritten in #957) is the model for a skill:
  an opening paragraph, `##` sections each holding one rule and its table.
- **The two files today.** `agents/scribe.md` 71 lines / 3,763 B, sections
  `## Procedure` and `## Report`, no `Enforced by:` line, one prose line at
  160 columns (`:22`). `skills/legacy-parity/SKILL.md` 117 / 5,325, sections
  `Premise`, `Migration config`, `Three-way judgment` (with `### When "follow
  the original" is itself ambiguous`), `The original's coordinates`,
  `Replacement annotation`, `Parity review`, `Recording the comparison`; no
  `Enforced by:` line; four emoji at `:91-94`; lines over 88 columns at `:33`,
  `:48`, `:50`. No file outside the skill cites one of its headings
  (`git grep`, `executed`); the hooks name *the legacy-parity skill* and no
  section.
- **What holds the scribe's text** (`git grep -n -w scribe -- tests/`,
  `executed`): `tests/test_absence_claims.py:33-37` (*An absence carries its
  search*, *not under facts*), `tests/test_a_probe_that_commits_says_so.py:127-135`
  (*§8*, *read, not probed*), `tests/test_every_agent_reads_the_contract.py:36`
  (the skip), `tests/test_docs_line_wrap.py:21`, `:146-147`, `:152-154`
  (named as uncovered), `tests/test_no_passage_is_pasted_into_a_second_file.py:205-211`
  (four ceilings at 65, from the opening paragraph every definition carried),
  and a comment at `tests/test_chain_hooks_hardening.py:1327` dating #426's
  measurement, which is history and stays.
- **What holds `legacy-parity`'s text**: `tests/test_review_axes.py:62-65`
  (*the same comparison axes*), `tests/test_the_record_is_written_in_words.py:42`
  (the skip), `tests/test_no_passage_is_pasted_into_a_second_file.py:268`
  (a ceiling of 1 with `implement`). `tests/test_chain_hooks_hardening.py:285-316`
  reads `templates/parity.md`'s four field names and `parity-setup`, and both
  keep them.
- **The pasted-passage ratchet.** `test_no_pair_shares_more_than_it_was_measured_at`
  fails a pair over its `BASELINE` entry and any pair the table does not hold
  that shares a run. So the scribe states its steps by naming
  `legacy-parity`'s sections and copies none of their sentences, and the
  skill's resolution order is not reworded into `parity-setup`'s or the
  template's words. A pair whose count falls passes untouched.
- **No changelog template exists** (`ls templates/`); the fragment follows
  `docs/the-record-layout.md` §*A change writes fragments, never a shared
  file*, as #967's did.

**What breaks in six months with the chosen approach.** No case runs the
scribe, so a scribe that skips its step 1 or reads the judging sections and
returns a verdict is seen by nobody until a parity run happens; the sentence
pins hold only that the rules are written. The `Policy root` placeholder
leaves the value to whoever runs the setup, and a repository whose policy
sits outside `docs/` meets the parity arm on every commit there, which is
true today as well. A fourth skill opened at a conditional step (as the
smith and the warden open this one) can change without guard 1 firing, and
the only thing that says so is `evals/` carrying no case with the condition.

## Alternatives considered

| Approach | Failure scenario (six months on) | Verdict |
|---|---|---|
| A. The scribe anew to #957's shape opening `legacy-parity` at step 1; the skill to the shape with the four words, its writer named, its field table pointed at the template; B5 across its five sites; measured on the read set | above | **chosen** |
| B. Fold the scribe's procedure into `legacy-parity` and leave the definition as frontmatter, the contract sentence and *open the skill* | the skill is also opened by the smith, the warden and a session that judges; the scribe's *no verdict, ask nobody, write nothing* would then sit in a file whose other readers do all three, the defect #2's C2 named | weighed as an equal and rejected |
| C. Split `legacy-parity` in two files, one for finding the original and one for judging | the scribe would read only its half and the bytes would fall; but `implement` §1 and the warden's step 5 name one file, and a second file is a second home for the resolution order, which both halves need | rejected; the skill's opening line says which sections the scribe reads |
| D. Keep `legacy-parity` on the scribe's `skills:` list | every spawn reads it anyway at step 1, so the preload saves nothing; but the list is what T1 holds to `agent-contract` alone, and a second entry is the shape the owner's rule refuses | rejected |
| E. Measure the preload alone, as `payload-meter --agent` prints it | the figure falls by the skill's 5,325 B whatever the rewrite says, and the scribe reads the same bytes at step 1; a counterfeit saving | rejected; the read set is the figure (#957's preload paragraph) |
| F. The scribe opens `writing-style` before its report, as the smith and the warden do before their records | the report is facts with coordinates for a caller, not a record a person reads later; #957's preload paragraph names `legacy-parity` alone for the scribe; 21 KB more on every spawn | rejected |
| G. Keep `SKIP` as an empty dict for the next file that needs one | a mechanism with nothing to catch; the next skip is one line to add back with its issue | rejected (`CLAUDE.md`, subtract before you add) |
| H. Leave `docs/policies/` and add a sentence that it is optional | `implement`'s layout and `orchestration.md:52-55` already say not to create it, and the template would still ship a value no other row ships | rejected; the placeholder and `none` |
| I. Measure the smith and the warden again, since their steps name `legacy-parity` | no case declares `seal/parity.md` (`git grep -l -i parity -- evals/` empty), so no run opens the file; two paid sides that can only read noise | rejected (`spec.md` §*How the rewrite is measured*) |
| J. Fix the hook messages and `docs/the-review-and-parity-arms.md:210` that say *the legacy-parity skill writes* the mark | they name the procedure the mark comes from, which stays true; changing a hook message is a change a person reads, with its own pins, in hooks near #976's work | rejected; out of scope in `spec.md` |
| K. Name an owner for the parity mark on a smith's commit in a parity repository | a design change to the parity arm or to the smith's writes, which #2's C1 settled the other way; nothing in #970 asks for it | rejected here; reported to the owner as a candidate issue (`questions.md`) |

## Phases

Vertical slices — each phase ends with something runnable and verified. No
phase runs a paid case. Every phase enumerates the class of what it removes
by the `git grep` its record names, and every new case is seen red first
(contract §15), with the exit and the mutation named in the phase record.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **`legacy-parity` and the policy root.** `skills/legacy-parity/SKILL.md` written to the shape, wrapped at 88 columns: an opening line naming which sections the scribe reads (finding and tracing the original) and which are its caller's (judging, the annotation, recording); the premise; the migration config pointing at `templates/parity.md` for its fields, with the resolution order ending in *the caller asks and records; a reader that cannot ask returns `original not found`*; three-way judgment with *inherit before raising* in one sentence; the trace to the response and the later fix; the original's coordinates; the replacement annotation; the parity review with the four words of `spec.md` §*Data & interfaces*, said once; the record of the comparison naming its writer (C5) and keeping *only after a comparison* and the `[no-parity]` placement. Each rule ends in `Enforced by:`, a case or `nothing — <why>`. `test_review_axes.py:65`'s phrase *the same comparison axes* kept. B5: `templates/parity.md:16`, `:33`, `skills/parity-setup/SKILL.md:42-43`, `skills/implement/orchestration.md:240` rewritten to the placeholder and `none`. T4 and T5 planted; `SKIP` and its loop removed from `tests/test_the_record_is_written_in_words.py`; `skills/legacy-parity/SKILL.md` added to `tests/test_docs_line_wrap.py#COVERED` | T4 and T5 red on the tree at the phase's start, green after; T6 red once the emoji leave with `SKIP` still in place (its own *carries no mark any more* assertion), green after `SKIP` leaves; `bin/test tests/test_the_record_is_written_in_words.py tests/test_review_axes.py tests/test_docs_line_wrap.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_chain_hooks_hardening.py -q -k "parity or words or axes or wrap or pair or corpus or paste"`, then each module whole where `-k` narrowed it, exit 0; `bin/rules --check` exit 0; `uvx ruff check` and `uvx ruff format --check` on the changed `.py`, exit 0; S7's `git grep` | |
| 2 | **The scribe and its readers.** `agents/scribe.md` written anew to `spec.md` §*Data & interfaces*, wrapped: `skills: [agent-contract]`; the description naming the session as the spawner; step 1 opening `legacy-parity` by the sections phase 1 named; the rules with their `Enforced by:` lines; at or under 3,763 B where the shape allows, and the phase record says the bytes either way. The pins sorted (Q7): `tests/test_absence_claims.py:33-37` and `tests/test_a_probe_that_commits_says_so.py:127-135` re-pointed to the rules' new sentences; T3 planted; `NOT_YET_REWRITTEN`'s scribe entry and the docstring's *#968 to #970* (`:11-14`, `:139-141`) rewritten to what still stands; `agents/scribe.md` added to `COVERED`, `tests/test_docs_line_wrap.py:21`, `:146-147`, `:152-154` rewritten; the `seal/follow-up.md` row deleted. The READMEs: `README.md:41` and `README.ko.md:40` list `agent-contract` alone; `README.md:43` and `README.ko.md:42` count the skills the agents follow from their first tool call as the rows show them at this commit; `README.md:234`, `:421` and `README.ko.md:226`, `:379` name the session, not the smith, as the party that asks | T1 red on the old scribe with the skip entry deleted, green after; T2 green; T3 red first by deleting one rule paragraph; `bin/test tests/test_every_agent_reads_the_contract.py tests/test_absence_claims.py tests/test_a_probe_that_commits_says_so.py tests/test_docs_line_wrap.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_a_moved_rule_leaves_its_definition.py tests/test_the_payload_meter_says_what_it_measured.py tests/test_a_section_marked_for_one_role_reaches_only_that_role.py -q` exit 0; `bin/rules --check` exit 0; ruff on the changed `.py`; S10's `git grep`; `git grep -n -w 'scribe' -- tests/` re-read and each hit named in the phase record | |
| 3 | **The measurement and the close.** `bin/payload-meter --agent scribe` at phase 2's commit and at 1d665d48; the read set (the meter's agent share plus `skills/legacy-parity/SKILL.md`'s bytes) against 25,691 B, both in the phase record with their commits, and the outcome `unverified`, the owner named, until a parity run. `overview.md` from `templates/sdd-overview.md` (purpose, divergences, `## Not verified` with the outcome row, fed-back clauses). `changelog.md` as a fragment: the paragraph a plugin user reads (the scribe preloads the contract alone and opens `legacy-parity` at its first step; the parity verdicts are words; the record names its writer; the setup no longer proposes `docs/policies/`), and a one-row table for the scribe: preload bytes, read-set bytes, outcome. `questions.md` rows the work answered, in words | `bin/rules --check` exit 0; `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.22.2 --root /Users/michael/Documents/GitHub/SpecSeal-worktrees/970 --worktree` exit 0; `bin/unverified-check` on this item; each figure of the fragment traced to the command that printed it in the phase record; the read set at or below 25,691 B, or the phase record names the bytes over and the sentences that cost them and the row is carried to the owner | |

This table is also where the work records how far it got. **Status is empty,
or the commit that closed the phase.** Re-read the column after any rebase.

### Test rows — what each case protects and the mutation it kills

| Case | Protects | Mutation it kills |
|---|---|---|
| T1 `tests/test_every_agent_reads_the_contract.py::test_every_definition_has_the_shape_and_preloads_the_contract_alone`, run on the scribe (exists; its skip entry leaves in phase 2) | S1 — a second preload or a lost section | the scribe's entry left in `NOT_YET_REWRITTEN`; `legacy-parity` back on the list |
| T2 `…::test_every_file_a_step_names_exists` (exists) | S2 — a dangling path at step 1 | `skills/legacy_parity/SKILL.md` in the step |
| T3 `tests/test_a_moved_rule_leaves_its_definition.py::test_the_scribes_rules_stand_with_their_enforcers` (phase 2; NAME NOT IN TREE) | S3, S4 — *facts, never verdicts*, *a guessed original proves nothing* with `original not found`, *start from the spec's coordinates and report the axis nobody looked at*, each with its `Enforced by:` | one of the three paragraphs deleted; `original not found` reworded; an `Enforced by:` line missing |
| T4 `tests/test_the_record_is_written_in_words.py::test_the_parity_verdicts_are_four_words` (phase 1; NAME NOT IN TREE) | S5 — a mark or a fifth label in the parity review | one word renamed or capitalised; a fifth label line added; the section's sentence saying the words are the labels deleted |
| T5 `tests/test_review_axes.py::test_the_record_of_a_comparison_names_its_writer` (phase 1; NAME NOT IN TREE; the module that already pins `legacy-parity`, unless the smith's group rule finds a closer group) | S6 — C5, the record read as an instruction to whoever opened the skill | the warden or the session dropped from the section; *the scribe and the smith write none* deleted |
| T6 `tests/test_the_record_is_written_in_words.py::test_no_file_an_agent_reads_carries_an_emoji_or_a_proof_block` (exists; `SKIP` leaves in phase 1) | S8 — a mark in `legacy-parity`, which no case read before | one of the four emoji left in place |

Each rewrite is verified by the pins it re-points, the cases above,
`rules --check` and `payload-meter`, not by a case on every sentence; a case
on a sentence is what held the bloat in place.

### Lines another item also edits

Each concurrent item works in its own worktree; whichever merges second
rebases and keeps both changes.

| File and lines | This item | The other item |
|---|---|---|
| `tests/test_every_agent_reads_the_contract.py:11-14`, `:34-37`, `:139-141` | deletes the scribe's entry and rewrites the docstring sentences naming *#968 to #970* | #968 deletes the framer's entry and the same sentences. The item that merges second finds `NOT_YET_REWRITTEN` empty, and removes the dict, its skip in the shape case and those sentences whole |
| `README.md:38-43`, `README.ko.md:37-42` | the scribe's row and the count of skills followed from the first tool call | #968, the framer's row and the same count. The count is read off the rows at the rebase, not carried |
| `skills/implement/orchestration.md:240` | one line of §*Orchestrator: Parity setup* | #943 edits this file for PR timing; this item touches no other line of it |

## Operational impact

- **What a plugin user sees.** In a repository that declares
  `seal/parity.md`, a scribe spawn opens `legacy-parity` with a `Read` at its
  first step instead of receiving it at startup, and returns
  `original not found` where the original does not resolve, leaving the
  question to the session. A parity review's labels read `differs`,
  `grounded`, `equivalent` and `unread`. A new `seal/parity.md` written from
  the template carries a placeholder for the policy root instead of
  `docs/policies/`, and the setup no longer proposes creating that directory.
- **In-flight parity records.** A round record or report written with the
  emoji labels is history and stays; nothing reads the labels.
- **The run.** No paid evaluation. CI pays nothing new.
- **Compatibility.** No field of `seal/parity.md` is renamed, so an existing
  declaration still parses and the gate reads it as before. No new
  dependency.
