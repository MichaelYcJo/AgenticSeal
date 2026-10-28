# Feature Specification: 1793174169-a-round-with-fixes-costs-three-record-commits

Issue #1041 is the spec. Every line number below is at `5287dd42`, the
commit this branch was cut from. The issue measured at `0b75346f`; since
then #1040 shortened `agents/crafter.md`, so the fix-pass rule the issue
cites at `:153-156` stands at `:148-157` now (executed,
`git diff --stat 0b75346f 5287dd42`, and read).

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `docs/the-review-record.md` *The round record*, `:89-99`: "The proofer writes `open`; the fix pass answers with `fixed <commit>`, `rejected` ... or `deferred <home>`." and `:135-146`: "The fix pass writes two lines per finding and nothing else in the file." | The policy already names one writer for a finding that a fix pass answers. This work keeps that writer. It adds what the policy leaves unsaid: both lines go in one commit, and no second party writes either line. |
| `docs/the-review-record.md` *The round record*, the grammar row for `verdict:` (`:50`): `fixed (?P<commit>[0-9a-f]{7,40})` | A `fixed` verdict names a commit that already exists, and a commit cannot carry its own hash. So a finding's two lines are committed after its fix commit, never inside it. This is the premise that keeps the separate answer commit (`frame/plan.md`, *Alternatives considered*, row A). |
| `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*, the *Job* row (`:100`) | The next round weighs every close the fix pass wrote. When the orchestrator doubts a close, that doubt belongs in the verifying round's spawn prompt. It is not a reason to rewrite the verdict. |
| `skills/agent-contract/SKILL.md` rule 3: "A prompt that narrows your scope ... you follow it." | In #955 and #1016 the fix pass followed a spawn prompt that took the `verdict:` lines away from it (the cause, `## Scope` item 4). The prompt is the orchestrator's, so the orchestrator's file is where this work closes the cause. |
| `skills/implement/SKILL.md` *2. Implement test-first*: "A review round records the commit it read, so work still sitting in the working tree is not visible to the reviewer at all." | The answer lines cannot wait uncommitted for the next round's record commit (`frame/plan.md`, *Alternatives considered*, row C). |
| `CONTRIBUTING.md` *What a change to a gate must carry*: "a change that adds any mechanism by what it takes away" | A new chain-check refusal of how the two lines were committed would add a mechanism and remove nothing. Its refusal could be cured only by rewriting the branch's history (`frame/plan.md`, *Alternatives considered*, row D). |
| `docs/the-reader-registry.md` *A frame names what its work removes* | This work removes nothing, so `## Removes` holds the no-change block. |
| `CLAUDE.md` *The rule a mechanism is kept against*: "A fact has one source, and every other place links to it." | The rule has one home in policy, `docs/the-review-record.md` *The round record*, through `## Rule changes`. Each party's file states only its own act and cites that section. |

## Scope

**In.**

1. **The orchestrator writes neither line of a finding that a fix pass
   answers.** `skills/code-review/orchestration.md` *Orchestrator: a phase
   is a fresh crafter, and a fix pass resumes the implementer*, the
   paragraph at `:54-58`, is rewritten in place. It states three things:
   - the crafter's fix pass commits the `verdict:` and `answer:` lines of
     every finding it answered in one commit for the whole pass, after its
     last fix commit and its corrections;
   - the orchestrator writes neither line of such a finding, and its
     fix-pass prompt leaves both lines to the crafter;
   - a close the orchestrator doubts goes into the verifying round's spawn
     prompt, and the orchestrator does not rewrite the line.

   The paragraph keeps its citation of `docs/the-review-record.md` *The
   round record*. It also keeps what it says today: the coordinate appended
   to `location:`, and no phase record or `plan.md` row.
2. **A finding the orchestrator closes without a fix pass takes both lines
   from the orchestrator, in one commit.** On the framer's route the table
   in `skills/code-review/orchestration.md` *A regression is routed by
   comparing the fix with the frame*, row *The record* (`:155`), says only
   "every open finding closes `deferred the frame`". The row's cell gains
   the `answer:` line, which names the regression that sent the work item
   back, written by the orchestrator in the same commit as the verdict. The
   same holds for a finding the orchestrator files at the cap's ladder. The
   policy sentence in `## Rule changes` covers that case, and
   `docs/the-review-record.md` *The run* already gives the ladder its home.
3. **The crafter commits a finding's two lines together.**
   `agents/crafter.md` *Rules*, *A fix pass writes two lines of each
   finding and no phase record.* (`:148-157`), gains one sentence at its
   end, after the sweep: commit the two lines of every finding you
   answered in one commit for the whole pass, after your last fix commit
   and its corrections. The *Job* sentence at `:17-21` already names both lines as the
   crafter's, and it stays.
4. **The cause of the split in #955 and #1016 is named, from the session
   that ran them.** The transcript is on disk. In the user's Claude Code
   project directory for this repository, session
   `50face2d-96d3-4774-92e7-faa0805279a3` holds the commits `137d0a9c`
   ("chore: verify #955's round 1 answers: six findings fixed", line 7953
   of the `.jsonl`) and `49a2dd0d` (line 8058). Each fix-pass spawn prompt
   that session gave the smith said, in its own words, to leave every
   `verdict:` line to the orchestrator:
   - #955 round 1, line 7831: "Leave every `verdict:` line as it stands;
     they are the orchestrator's."
   - #955 round 2, line 8015: "Leave `verdict:` as it stands."
   - #1016 round 1, line 8971: the same instruction.

   The same session gave the instruction to earlier work items as well. At
   line 956 it was "Do not write the `answer:` lines in the round record;
   the orchestrator writes them.", and at lines 1456, 1728, 2451 and 2678 it
   was "Do not write the `verdict:` or `answer:` lines". At line 11321 the
   session stopped: "This time the fix pass writes the verdicts itself, as
   `agents/smith.md` says". At `137d0a9c` the tree already named the fix
   pass as the writer of both lines (`agents/smith.md:20` and `:153-156`
   there). So the cause was the orchestrator's spawn prompt, and no
   sentence of the tree produced it. The session gives no reason for the
   instruction. None of its assistant text up to line 960 mentions
   `verdict` or `answer:`. All of this item is executed: a
   `grep` over the project directory, and a Python read of the `.jsonl`
   for every `Agent` and `SendMessage` input holding `verdict`.

   The changelog fragment states this cause in one sentence. It cites the
   session by its id and the spawn prompts by their line numbers. It names
   no absolute user path, under `CLAUDE.md` *Repo rule: no real identifiers
   in examples or fixtures*.
5. **The acts table says why the new orchestrator rule is still a
   sentence.** `skills/implement/orchestration.md`, the row
   *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the
   implementer* (`:666`), gains one sentence in its `Grounds` cell. Who
   wrote a finding's two lines, and in which commit, is in the record's
   history and no check reads it. A refusal at the pull request could be
   cured only by rewriting the branch's history.
6. **A changelog fragment**, `changelog.md` in this work item's directory.
   It states the rule for the orchestrator and the crafter, and the cause
   from item 4.
7. **`## Rule changes` below** adds the rule to `docs/the-review-record.md`
   *The round record*, for the settle after the release.

**What a round with fixes costs after this work.** It costs the round
record's commit, the fix commit or commits, and one answer commit holding
both lines of every finding the pass answered. That is two record commits,
the number the tree describes. The answer commit cannot fold into the fix
commit, by the premise in `## Grounding` row 2. This release's work items
already ran this way. Six answer commits on its branches each add as many
`+verdict:` lines as `+answer:` lines: `ab628278` (#712), `98a3b114`
(#1058), `e9acea12` and `6e59b1ea` (#913), `8e5261cf` and `4e635bd4`
(#1052). In #955 and #1016, `2b68252c` and `517a1139` add `+answer:` lines
only, and `137d0a9c` and `f294b3bd` add `+verdict:` lines only (executed,
`git show <commit> | grep -c '^+verdict:'` and the same for `^+answer:`).
So the fix commit, the answer commit and the next round's record commit
that the spawn prompt describes for this release are the two record commits
the tree intends, plus the fix. They are not the defect.

## Out of scope

- **A chain-check refusal of how a finding's two lines were committed.**
  `frame/plan.md`, *Alternatives considered*, row D gives the grounds.
  `skills/code-review/scripts/chain_check.py` is unchanged by this work.
  #1020 edits it after this work, for recurrence across rounds, which is
  unrelated to who writes a verdict. `routing.md`'s *Why this way* says this
  change moves "what the chain check accepts". The frame decides otherwise,
  for the grounds in row D (`frame/questions.md`, head item 1).
- **`skills/implement/SKILL.md:484-489`.** It already names the fix pass as
  the writer of both lines, and it cites `docs/the-review-record.md` *The
  round record*. The issue asks for an edit there only if the orchestrator
  keeps a step after the fix pass, and this frame gives it none. #1055 edits
  the file in parallel, and #1110 rewords it after this work.
- **The word `spec` in `agents/crafter.md` and in the skills.** #1110
  rewords it after this work. This work's new sentences do not use it.
- **`agents/proofer.md`.** The proofer writes `verdict: open` and an empty
  `answer:` line, and that does not change.
- **Editing `docs/` directly.** The policy root changes at the settle after
  the release, from `## Rule changes` (`skills/implement/SKILL.md`
  *Document layout*).
- **#955's and #1016's records.** They are released and settled, and their
  history stays as it is.
- **Files of the parallel work items.** This work edits
  `skills/code-review/orchestration.md`, `skills/implement/orchestration.md`,
  `agents/crafter.md`, `tests/text/test_the_rules_have_one_owner.py` and
  `tests/text/test_a_moved_rule_leaves_its_definition.py`. None of them is
  on the file lists the spawn prompt gives for #1042, #1043, #1055, #1056
  or #956 (`frame/questions.md`, head item 5).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. The orchestrator writes neither line of a finding a fix pass answers | Given `skills/code-review/orchestration.md` at the phase's commit, when its fix-pass section is read, then it says the orchestrator writes neither line of such a finding, that its fix-pass prompt leaves both lines to the crafter, and that a doubted close goes into the verifying round's prompt | A new entry in `tests/text/test_the_rules_have_one_owner.py#RULES` with `ORCH` as the owner and the new bold sentence as the rule, read by `test_the_owner_states_the_rule`. A clause for the verifying round's prompt goes in `test_the_fix_pass_reads_the_implementers_context_before_it_resumes`'s tuple, or in a case beside it in the same module. Each is seen red against `5287dd42` before the text lands (contract rule 15), and the phase record says how |
| S2. A finding the orchestrator closes takes both lines from it | Given the framer's-route table at the phase's commit, when row *The record* is read, then it names the `answer:` line and one commit of the orchestrator's beside `deferred the frame` | The same module, a clause read from the section *A regression is routed by comparing the fix with the frame*, seen red against `5287dd42` |
| S3. The crafter commits both lines together | Given `agents/crafter.md` at the phase's commit, when the fix-pass rule is read, then it says to commit the two lines of every finding answered in one commit for the whole pass, after the last fix commit and its corrections | A clause added to the tuple in `tests/text/test_a_moved_rule_leaves_its_definition.py#test_the_crafters_fix_pass_writes_two_lines_and_sweeps_what_its_range_reworded`, seen red against `5287dd42` |
| S4. The new text is no copy, and it wraps | Given the edited files, when the paste check and the wrap check read them, then no 15-word run is shared with `docs/the-review-record.md` or another file, and every line keeps the file's wrap | `bin/test` over `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/behaviour/test_docs_line_wrap.py` and `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`, one module at a time, green |
| S5. The rule change parses | Given this `frame/design.md`, when the one reader of `## Rule changes` reads it, then the `add` item is read whole and nothing is refused | `skills/settle/scripts/rule_changes.py`, which `chain_check.py` asks at the pull request for this work item (`docs/the-review-record.md` *What the check reads at the pull request*). The round's proofer runs `chain_check.py` over the branch |
| S6. The cause is named | Given the changelog fragment, when it is read against `## Scope` item 4, then it names the orchestrator's fix-pass spawn prompts in #955 and #1016 as the cause, by session id and line | Read by the round and the sealer against the transcript lines in `## Scope` item 4, and against `git show 2b68252c` and `git show 137d0a9c` |

## Data & interfaces

None. No record grammar, command, output or file format changes. The round
record's lines keep their shapes (`docs/the-review-record.md` *The round
record*, the grammar table). What changes is the text the orchestrator and
the crafter act on, and the assertions that read it.

## Rule changes

- add
  file: docs/the-review-record.md
  section: The round record
  to: **A finding's `verdict:` and `answer:` lines are one party's, and one commit carries every finding that party closes in the pass.**
    A finding a fix pass answers is the fix pass's alone. After its last fix commit and the corrections its sweep made, the pass writes the lines of all the findings it closed and commits them together, once, since a `fixed` verdict names a commit that already exists. The orchestrator writes neither line of such a finding, and a close it doubts goes into the verifying round's spawn prompt, since that round weighs every close. A finding closed without a fix pass, such as `deferred the frame` on the framer's route or a `deferred <home>` the orchestrator files at the cap, takes both lines from the orchestrator. A second party's commit adds a record commit to the round and nothing a reader uses.
    check: tests/text/test_the_rules_have_one_owner.py tests/text/test_a_moved_rule_leaves_its_definition.py

## Removes

- nothing
  why: The work adds sentences to the orchestrator's and the crafter's text and assertions that read them. It removes no sentence, unit, test or record.

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-28 by framer, before the build.
