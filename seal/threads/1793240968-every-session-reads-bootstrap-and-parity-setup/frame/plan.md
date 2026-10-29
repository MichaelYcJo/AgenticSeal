# Implementation Plan: 1793240968-every-session-reads-bootstrap-and-parity-setup

Approved 2026-10-29 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phases 1 and 2.

## Summary

Every orchestrating session reads all of `skills/implement/orchestration.md`
before its first edit, 7,835 words at `1e82fd0a` (executed, `wc -w`). Two
of its sections, 1,993 of those words, apply only where a repository has no
`seal/` root yet or a migration is being declared. This work removes the
parity setup's restatement of `skills/parity-setup/SKILL.md` and sends the
bootstrap's yes to that procedure (phase 1), then moves the bootstrap,
unchanged, to `skills/implement/bootstrap.md`, leaving one sentence in
`orchestration.md` that names the condition and the file (phase 2). The
acts table keeps the bootstrap's row by reading the new file as a third
file. Every reader of the two headings moves with them.

## Technical context

- `skills/implement/orchestration.md` *Orchestrator: Bootstrap* is lines 89
  to 280, and *Orchestrator: Parity setup* is lines 281 to 301. Neither holds
  a `###` heading or a `check:` line (executed, `grep`).
- `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py#acts`
  reads the `Orchestrator:` headings of the files in `#FILES` only, and
  `#findings` fails a row naming a heading that no listed file carries.
  Moving the heading without adding the file turns the case red, which is
  the reason the file is added rather than the row dropped.
- `tests/behaviour/test_a_cited_section_stands_in_its_file.py` resolves
  every citation of a section in the tracked text files outside the
  records, including `.py` docstrings and comments. A heading and every
  citation of it move in one commit, or that case goes red between commits.
  Today the two headings are cited by path and italics in
  `hooks/mode-gate.py:15-16` and `:50-51`, and named in the acts table.
- `tests/text/test_no_passage_is_pasted_into_a_second_file.py` reads every
  tracked `.md` under `skills/`, so the new file joins its corpus at birth.
  Its baseline allows one shared run between `README.md` and
  `skills/implement/orchestration.md`. A reimplementation of its
  normalisation, without its fence handling, places that run outside lines
  89 to 301 (executed, an inline `python3 -I` over the two files, window 15
  read from `tests/text/test_a_moved_rule_leaves_its_definition.py`), so the
  baseline needs no new key. `questions.md` Q1 leaves the exact answer to
  the module's own run in phase 2.
- `skills/parity-setup/SKILL.md` carries `disable-model-invocation: true`.
  The orchestrator cannot invoke it as a skill, so the bootstrap's sentence
  says to read the file and follow *Procedure*. Its step 1 (stop where
  `seal/parity.md` exists) never fires at first setup, and its steps 4 and
  7 add a module question and a closing note that the removed section did
  not carry.
- Sibling work in `release: 0.24.1`: #1142 edits
  `skills/implement/orchestration.md:398`, a row of *What the answer
  writes*, which neither phase touches (read, the issue body). The other
  sibling issues name none of this plan's files (executed, `grep` over the
  bodies and comments of #1047, #1049 and #1091). The branches of all four
  hold only their routing commits at framing (executed, `git log`).

**The chosen approach's failure scenario, six months on.** A first-setup
question added later is written into `orchestration.md`, because that is
the file its writer was reading, and every session pays for it again.
Nothing refuses that: which file a sentence belongs in is a judgment, and
only the proofer reads it. The second risk is the preset block already
copied into people's `~/.claude/CLAUDE.md`. Until `/agentic:update`
re-copies it, it names "the Bootstrap section of
`skills/implement/orchestration.md`", which no longer exists. The opening
sentence of that file is what catches such a session, which is why the
pointer sits at the top rather than at the place the section stood.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. Keep both sections in `orchestration.md` (the structure as it stands) | Every orchestrating session in a repository that has its root keeps reading 1,993 words it acts on none of. The premise that would keep the structure, that an orchestrating session may need the bootstrap at any point, was checked and is false: the bootstrap runs only where no root carrying the marker exists at either place (its own *Ask only here* paragraph, lines 276 to 279), and the parity setup only on a yes inside it | Rejected |
| A2. Move both sections, unchanged, into the new file (the issue's first reading) | The parity setup stays a second statement of `skills/parity-setup/SKILL.md` steps 2, 3, 5 and 6. The two have already drifted apart: the skill asks for the module (step 4) and says what changes after (step 7), and the section does neither. A third edit to one of them leaves the other stale | Rejected |
| A3. Move the bootstrap; replace the parity setup with one sentence sending a yes to `skills/parity-setup/SKILL.md` *Procedure* | Described under *Technical context*: a later first-setup sentence written into the wrong file, and stale installed blocks | Chosen |
| A4. Move the bootstrap under a heading without the `Orchestrator:` marker, drop its acts row, and add an "outside this table" paragraph like the flow-log one | The bootstrap's delivery, `hooks/mode-gate.py`, stops being read by any check, and the paragraph that replaces the row adds words to the file every session reads, which works against the reason for the move | Rejected |
| A5. Make first setup a skill of its own, `skills/first-setup/SKILL.md` | A skill's name and description load into every session's skill listing, so every session in every project pays for it, and it becomes a command people can type, which `README.md` would then list. Both widen what this work changes | Rejected |
| A6. Widen the acts check to every `skills/*/*.md` | It sweeps in `skills/verify/orchestration.md`, whose flow-log act the table holds outside on purpose, and `skills/writing-style/outside-the-review.md`. Changing what a gate reads beyond the moved file is a change of its own, with `CONTRIBUTING.md` *What a change to a gate must carry* to answer | Rejected |
| A7. Also add the new file to `.github/scripts/rules.py#RULE_FILES` | The moved text holds no `check:` line, so the reader would read nothing in it. `tests/github/test_rules.py` plants a defect in one file per pattern, so the entry also costs a planted case for a file with nothing to check | Rejected; `frame/design.md` *Scope* says who adds it later |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The parity setup is stated once. `skills/implement/orchestration.md` *Orchestrator: Parity setup* is removed. The Bootstrap's step 3 answers a yes with one sentence: the orchestrator reads `skills/parity-setup/SKILL.md` and follows its *Procedure*, then continues the work. The acts table loses the Parity setup row, and the Bootstrap row's `Grounds` carries what that row said, reworded for the procedure. `skills/parity-setup/SKILL.md:15-17` says the bootstrap's yes runs its procedure and the command is for a later answer. `tests/behaviour/test_chain_hooks_hardening.py:237-247` asserts that `orchestration.md` names `skills/parity-setup/SKILL.md` and that the skill names `templates/setup/parity.md`. The docstring at `tests/behaviour/test_first_setup_asks_once.py:243` names the skill as the never-guess rule's home | `bin/test` over `tests/behaviour/test_chain_hooks_hardening.py`, `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`, `tests/behaviour/test_first_setup_asks_once.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py` and `tests/behaviour/test_docs_line_wrap.py`. The re-pointed chain-hooks assertion is seen red with the new step 3 sentence deleted, per contract rule 15, and the phase record says how | 3890b230 |
| 2 | The bootstrap leaves the file every session reads. `skills/implement/bootstrap.md` is created with a title, an opening paragraph, and *Orchestrator: Bootstrap* moved byte for byte from `orchestration.md`. `orchestration.md`'s opening paragraph drops its clause about the root and parity mode and gains the pointer sentence of `frame/design.md` *Scope* item 3. The acts table's opening prose, the Bootstrap row's `File` cell and the table's own row name three files. `templates/setup/claude-md-block.md:16` and `hooks/mode-gate.py:15-16` and `:50-51` name the new file. The cases of `frame/design.md` *Data & interfaces* read the new file, and one new case pins the pointer sentence (S3). Phase 2's record holds `wc -w skills/implement/orchestration.md` before (7,835 at `1e82fd0a`) and after, and the S5 `diff` with its exit code | `bin/test` over the six modules of phase 1, `tests/behaviour/test_chain_hooks_hardening.py` reading the bootstrap file now, plus `tests/text/test_the_settings_have_a_front_door.py`, `tests/text/test_the_rules_have_one_owner.py` and `tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py`. The new S3 case is seen red against `orchestration.md` before the pointer sentence is written. The re-pointed cases are proved by passing at the new path, with no red-first run of their own, because their needles do not change | |

## Operational impact

- **Installed preset blocks.** A person's `~/.claude/CLAUDE.md` holds the
  copy `install.sh` made, and that copy names "the Bootstrap section of
  `skills/implement/orchestration.md`" until `/agentic:update` re-copies the
  block. Such a session lands on `orchestration.md`, whose opening sentence
  sends it to `skills/implement/bootstrap.md`. Nothing else breaks.
- **The changelog fragment carries a process row.** This work item's diff
  changes `skills/implement/orchestration.md`, so under the pending rule of
  `seal/threads/1793226631-every-release-ends-with-a-preparation-pull-request/frame/design.md`
  its `changelog.md` ends with `### Process changes` and one row in the
  shape `templates/records/process.md` gives. The orchestrator writes it
  with the fragment.
- **A sibling's rebase.** #1142 edits `skills/implement/orchestration.md:398`.
  Phase 2 removes 192 lines above that row, so the line moves while its text
  does not. The branch that lands second takes the first's change from
  `release/v0.24.1`, as the milestone description says, and re-runs its own
  phase's cases.
- No migration, no environment variable, no dependency, and no version
  move: `.claude-plugin/plugin.json` is the orchestrator's.
