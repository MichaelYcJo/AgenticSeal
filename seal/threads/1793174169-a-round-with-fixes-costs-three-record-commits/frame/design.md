# Feature Specification: 1793174169-a-round-with-fixes-costs-three-record-commits

Issue #1041 is the spec, and the owner's answer of 2026-10-28 under the
sealer's verdict in `guarantee.md` decides its one open reading. This frame
was rewritten in place after that answer. Phase 1 was built to the earlier
frame, and its coordinates are at `5287dd42`, the commit this branch was
cut from. The coordinates of phase 2, the rework, are at `aa8b54cb`, the
merge of `origin/release/v0.24.0` into this branch (executed,
`git -C <this work item's worktree> log --oneline -1`), and every line
number below without a commit beside it is at `aa8b54cb`.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| Issue #1041 *Done when* bullet 1: "`skills/code-review/orchestration.md` says the orchestrator commits the fix pass's two lines as they stand and writes no `verdict:` of its own." And `guarantee.md:40`, the owner's answer of 2026-10-28: "The fix pass writes the `verdict:` and `answer:` lines and does not commit them; the orchestrator commits them as they stand and writes no `verdict:` of its own." | The fix pass writes both lines of a finding it answers. The orchestrator makes the one commit that carries them, and changes neither line. This is the decision phase 2 builds, and it replaces phase 1's design, where the fix pass made that commit itself. |
| Issue #1041 *Done when* bullet 2: "If the orchestrator is to keep a step after the fix pass, that step is written where the fix pass's step is." | The orchestrator now keeps one step after the fix pass, the commit. The step is written in `skills/code-review/orchestration.md` *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer*, in the paragraph that states the fix pass's last step. |
| `docs/the-review-record.md` *The round record*, `:89-99`: "The proofer writes `open`; the fix pass answers with `fixed <commit>`, `rejected` ... or `deferred <home>`." and `:135-146`: "The fix pass writes two lines per finding and nothing else in the file." | The policy names one writer for a finding that a fix pass answers, and this work keeps that writer. It adds what the policy leaves unsaid: the orchestrator commits the lines, in one commit for the pass, and no second party writes either line. |
| `docs/the-review-record.md` *The round record*, the grammar row for `verdict:` (`:50`): `fixed (?P<commit>[0-9a-f]{7,40})` | A `fixed` verdict names a commit that already exists, and a commit cannot carry its own hash. So the fix pass writes a finding's two lines after its fix commits, and the commit that carries them is a commit of its own. |
| `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test*: "A review round records the commit it read, so work still sitting in the working tree is not visible to the reviewer at all." | The verifying round weighs every close the fix pass wrote, so the lines must be in a commit before that round is spawned. The orchestrator commits them at the hand-back, before the spawn, and not with the next round's record (`frame/plan.md`, *Alternatives considered*, row C against row F). |
| `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*, the *Job* row (`:106`) | The next round weighs every close the fix pass wrote. When the orchestrator doubts a close, that doubt belongs in the verifying round's spawn prompt. It is not a reason to rewrite the verdict. |
| `docs/worktree-guard-spec.md` *Decision matrix*, table *A. Branch switch*, the row "single stream, tracked changes present": under the `automation` press it is "a deny to the model instead" of a question | A round record left modified between the hand-back and the orchestrator's commit meets this row only where a branch switch runs in that window. Under automation the row costs the model a turn and asks no person (`frame/plan.md`, *Technical context*, the failure scenario). |
| `skills/agent-contract/SKILL.md` rule 3: "A prompt that narrows your scope ... you follow it." | In #955 and #1016 the fix pass followed a spawn prompt that took the `verdict:` lines away from it (the cause, `## Scope` item 5). The prompt is the orchestrator's, so the orchestrator's file is where this work closes the cause. |
| `CONTRIBUTING.md` *What a change to a gate must carry*: "a change that adds any mechanism by what it takes away" | A new chain-check refusal of who committed the two lines would add a mechanism and remove nothing. Its refusal could be cured only by rewriting the branch's history (`frame/plan.md`, *Alternatives considered*, row D). |
| `docs/the-reader-registry.md` *A frame names what its work removes* | This work removes nothing the base held, so `## Removes` holds the no-change block. |
| `CLAUDE.md` *The rule a mechanism is kept against*: "A fact has one source, and every other place links to it." | The rule has one home in policy, `docs/the-review-record.md` *The round record*, through `## Rule changes`. Each party's file states only its own act and cites that section. |

## Scope

**In.** Items 1 to 4 are the text the work leaves. Item 6 lists what phase
2 changes in the build that phase 1 committed.

1. **The fix pass writes both lines and commits neither, and the
   orchestrator commits them as they stand.** `skills/code-review/orchestration.md`
   *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the
   implementer* states, in the paragraph *The fix pass then finds what the
   fixes left standing*, the fix pass's last step: it writes the
   `verdict:` and `answer:` lines of every finding it answered, after its
   fix commits and the corrections that paragraph names, and leaves the
   round record uncommitted. The same paragraph then states the
   orchestrator's step, as one bold sentence: on the hand-back the
   orchestrator commits the round record as the fix pass left it, in one
   commit for the whole pass, before it spawns the verifying round, and
   changes none of its lines. The commit holds `trail/rounds/round-N.md`
   alone.

   The paragraph at `:54-62` keeps what it says today: the bold sentence
   that the orchestrator writes neither line of a finding the fix pass
   answers and that its fix-pass prompt leaves both lines to the crafter,
   the coordinate appended to `location:`, no phase record or `plan.md`
   row, and a doubted close going into the verifying round's spawn prompt
   with no rewrite of the line. The section keeps its citation of
   `docs/the-review-record.md` *The round record*.
2. **A finding the orchestrator closes without a fix pass takes both lines
   from the orchestrator, in one commit.** Row *The record* of the
   framer's-route table in `skills/code-review/orchestration.md` *A
   regression is routed by comparing the fix with the frame* (`:161`)
   reads: "every open finding closes `deferred the frame`, and its
   `answer:` line names the regression that sent the work item back; you
   write both lines of every open finding in one commit". Phase 1 built
   it, and it stands. The same holds for a finding the orchestrator files at
   the cap's ladder. The policy sentence in `## Rule changes` covers that
   case, and `docs/the-review-record.md` *The run* already gives the ladder
   its home.
3. **The crafter writes both lines and leaves them to the orchestrator to
   commit.** `agents/crafter.md` *Rules*, *A fix pass writes two lines of
   each finding and no phase record.* (`:148-159`), ends with one sentence
   after the sweep: write the two lines of every finding you answered last,
   after your last fix commit and its corrections, and do not commit them,
   because the orchestrator commits them at the hand-back. The *Job*
   sentence at `:17-21` already names both lines as the crafter's writes,
   and it stays. *Order of work* step 6, "Commit, then run `seal mutate`",
   stays: it is the build phase's step, and the fix-pass rule states the
   one file the pass leaves uncommitted.
4. **The acts table says why the orchestrator's rule is still a
   sentence.** `skills/implement/orchestration.md`, row *Orchestrator: a
   phase is a fresh crafter, and a fix pass resumes the implementer*
   (`:666`), keeps one sentence in its `Grounds` cell on the two lines. The
   sentence names what nothing reads: who wrote a finding's two lines, who
   committed them, and whether that commit changed them are in the round
   record's history, no check reads it, and a refusal at the pull request
   could be cured only by rewriting the branch's history.
5. **The cause of the split in #955 and #1016 is named, from the session
   that ran them.** The transcript is on disk. In the user's Claude Code
   project directory for this repository, session
   `50face2d-96d3-4774-92e7-faa0805279a3` holds the commit `137d0a9c`
   ("chore: verify #955's round 1 answers: six findings fixed", first at
   line 7954 of the `.jsonl`), and names `49a2dd0d` first at line 8067.
   Each fix-pass spawn prompt that session gave the smith said, in its own
   words, to leave every `verdict:` line to the orchestrator:
   - #955 round 1, line 7832: "Leave every `verdict:` line as it stands;
     they are the orchestrator's."
   - #955 round 2, line 8016: "Leave `verdict:` as it stands."
   - #1016 round 1, line 8972: the same instruction.

   The same session gave the instruction to earlier work items as well. At
   line 957 it was "Do not write the `answer:` lines in the round record;
   the orchestrator writes them.", and at lines 1457, 1729, 2452 and 2679 it
   was "Do not write the `verdict:` or `answer:` lines". At line 11322 the
   session stopped: "This time the fix pass writes the verdicts itself, as
   `agents/smith.md` says". At `137d0a9c` the tree already named the fix
   pass as the writer of both lines (`agents/smith.md:20` and `:153-156`
   there). So the cause was the orchestrator's spawn prompt, and no
   sentence of the tree produced it. The session gives no reason for the
   instruction. Every line number here is what `grep -n` prints, which
   counts from one (executed, `grep -n -F` over the `.jsonl` for each
   quoted sentence, 2026-10-28). The earlier frame gave each number one
   lower, and `gaps.md` holds that divergence.

   The changelog fragment states this cause in one sentence. It cites the
   session by its id and the spawn prompts by their line numbers. It names
   no absolute user path, under `CLAUDE.md` *Repo rule: no real identifiers
   in examples or fixtures*.
6. **Phase 2 changes the build to the owner's decision.** Each coordinate
   below was read at `aa8b54cb`.
   - `skills/code-review/orchestration.md:78-80`, the end of the paragraph
     *The fix pass then finds what the fixes left standing*: "Last, the fix
     pass commits the two lines of every finding it answered in one commit
     for the whole pass, after its fix commits and those corrections,
     because a `fixed` verdict names a commit that already exists." It is
     rewritten in place to item 1: the fix pass writes the lines last and
     commits neither, and the orchestrator's bold sentence follows.
   - `skills/code-review/orchestration.md:54-62` and `:161` stay as they
     read.
   - `agents/crafter.md:156-158`: "Then commit the `verdict:` and `answer:`
     lines of every finding you answered in one commit for the whole pass,
     after your last fix commit and its corrections." It is rewritten in
     place to item 3.
   - `skills/implement/orchestration.md:666`, the `Grounds` cell's last
     sentence: "Who wrote a finding's `verdict:` and `answer:` lines, and in
     which commit, is in the round record's history and no check reads it;
     a refusal at the pull request could be cured only by rewriting the
     branch's history". It is rewritten in place to item 4, naming the
     orchestrator's commit.
   - `tests/text/test_the_rules_have_one_owner.py`. In
     `test_the_fix_pass_reads_the_implementers_context_before_it_resumes`
     (`:176-199`), the clause at `:192-193`, "commits the two lines of every
     finding it answered in one commit for the whole pass, after its fix
     commits and those corrections", and its comment at `:189-191` are
     replaced by clauses for item 1's two new statements. `RULES` gains an
     entry for the orchestrator's new bold sentence with `ORCH` as its
     owner, read by `test_the_owner_states_the_rule`. Rule 19 (`:140-148`)
     and the clauses at `:194-195` stay.
   - `tests/text/test_a_moved_rule_leaves_its_definition.py`. In
     `test_the_crafters_fix_pass_writes_two_lines_and_sweeps_what_its_range_reworded`
     (`:495-516`), the clause at `:512-514`, "Then commit the `verdict:` and
     `answer:` lines of every finding you answered in one commit for the
     whole pass, after your last fix commit and its corrections.", and its
     comment at `:510-511` are replaced by a clause for item 3's sentence.
   - `changelog.md` in this work item's directory. Its first bullet says
     the crafter's fix pass commits the two lines. It is rewritten to item
     1: the fix pass writes both lines and leaves them uncommitted, and the
     orchestrator commits them as they stand, in one commit for the pass,
     before the verifying round, and writes no `verdict:` of its own. The
     second and third bullets stay.

   `gaps.md` *Where spec and implementation diverged* gains the rework's
   row from the crafter, not from this frame.
7. **`## Rule changes` below** adds the rule to `docs/the-review-record.md`
   *The round record*, for the settle after the release.

**What a round with fixes costs after this work.** It costs the round
record's commit, the fix commit or commits, and one answer commit, the
orchestrator's, holding both lines of every finding the pass answered. That
is two record commits, the number the tree describes. The answer commit
cannot fold into a fix commit, by the premise in `## Grounding` row 4, and
it cannot wait for the next round's record commit, by row 5. This release's
work items already ran with two record commits per round. Six answer
commits on its branches each add as many `+verdict:` lines as `+answer:`
lines: `ab628278` (#712), `98a3b114` (#1058), `e9acea12` and `6e59b1ea`
(#913), `8e5261cf` and `4e635bd4` (#1052). In #955 and #1016, `2b68252c`
and `517a1139` add `+answer:` lines only, and `137d0a9c` and `f294b3bd`
add `+verdict:` lines only (executed by the earlier frame,
`git show <commit> | grep -c '^+verdict:'` and the same for `^+answer:`,
and re-run by the sealer, `guarantee.md:22`). The defect was the third
commit, a second hand rewriting the verdicts. Who makes the one answer
commit does not change the count.

## Out of scope

- **A chain-check refusal of who wrote or committed a finding's two
  lines.** `frame/plan.md`, *Alternatives considered*, row D gives the
  grounds. `skills/code-review/scripts/chain_check.py` is unchanged by this
  work. #1020 edits it after this work, for recurrence across rounds, which
  is unrelated to who writes a verdict. `routing.md`'s *Why this way* says
  this change moves "what the chain check accepts". The frame decides
  otherwise, for the grounds in row D (`frame/questions.md`, head item 1).
- **`skills/implement/SKILL.md:484-489`.** It names the fix pass as the
  writer of both lines and cites `docs/the-review-record.md` *The round
  record*, which stays true. It says nothing about who commits them. The
  issue's bullet 2 asks that the orchestrator's step be written where the
  fix pass's step is, and item 1 writes it in
  `skills/code-review/orchestration.md`, the orchestrator's file, beside
  the fix pass's last step. The implementer reads its own exception in
  `agents/crafter.md` (item 3). #1110 rewords `skills/implement/SKILL.md`
  after this work.
- **The paragraph *Two commits after the build are yours, not the
  crafter's* (`skills/code-review/orchestration.md:64-69`).** It lists the
  orchestrator's commits that change what the work item ships, each bringing
  `changelog.md` along. The answer commit changes a record only, like the
  round record commit the orchestrator already makes after each proofer
  (`agents/proofer.md`, whose description says it writes a round record
  "for the orchestrator to verify and commit"), so the paragraph stays.
- **A finding the fix pass leaves `open`.** The orchestrator commits the
  record as it stands, and today's rules on an unanswered finding stand:
  `skills/code-review/scripts/chain_check.py` refuses an `open` verdict in
  the record it reads (`chain_check.py#verdict_problems`). This work does
  not add a step for it.
- **The word `spec` in `agents/crafter.md` and in the skills.** #1110
  rewords it after this work. This work's new sentences do not use it.
- **`agents/proofer.md`.** The proofer writes `verdict: open` and an empty
  `answer:` line, and that does not change.
- **Editing `docs/` directly.** The policy root changes at the settle after
  the release, from `## Rule changes` (`skills/implement/SKILL.md`
  *Document layout — two roots, three lifetimes*).
- **#955's and #1016's records.** They are released and settled, and their
  history stays as it is.
- **Files of the parallel work items.** Phase 2 edits the same five files
  phase 1 edited, `skills/code-review/orchestration.md`,
  `skills/implement/orchestration.md`, `agents/crafter.md`,
  `tests/text/test_the_rules_have_one_owner.py` and
  `tests/text/test_a_moved_rule_leaves_its_definition.py`, and this work
  item's `changelog.md`. It adds no file.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. The fix pass writes and the orchestrator commits | Given `skills/code-review/orchestration.md` at phase 2's commit, when its fix-pass section is read, then it says that the fix pass writes the two lines of every finding it answered last and commits neither, and that the orchestrator commits the round record as the pass left it, in one commit for the whole pass, before it spawns the verifying round, changing none of its lines. It still says the orchestrator writes neither line, that its fix-pass prompt leaves both lines to the crafter, and that a doubted close goes into the verifying round's prompt | A new `RULES` entry in `tests/text/test_the_rules_have_one_owner.py` with `ORCH` as owner and the orchestrator's new bold sentence as its rule, read by `test_the_owner_states_the_rule`. The clauses of `test_the_fix_pass_reads_the_implementers_context_before_it_resumes` name the fix pass's uncommitted lines, and the clause naming the fix pass's own commit is gone. Each new clause is seen red against the text at `aa8b54cb` before the text lands (contract rule 15), and phase 2's record says how |
| S2. A finding the orchestrator closes takes both lines from it | Given the framer's-route table, when row *The record* is read, then it names the `answer:` line and one commit of the orchestrator's beside `deferred the frame` | `test_the_framers_route_closes_each_finding_with_both_lines_in_one_commit`, built in phase 1, green at phase 2's commit |
| S3. The crafter leaves both lines to the orchestrator to commit | Given `agents/crafter.md` at phase 2's commit, when the fix-pass rule is read, then it says to write the two lines of every finding answered last, after the last fix commit and its corrections, and not to commit them | A clause replacing the one-commit clause in `tests/text/test_a_moved_rule_leaves_its_definition.py#test_the_crafters_fix_pass_writes_two_lines_and_sweeps_what_its_range_reworded`, seen red against the text at `aa8b54cb` |
| S4. The new text is no copy, and it wraps | Given the edited files, when the paste check and the wrap check read them, then no 15-word run is shared with `docs/the-review-record.md` or another file, and every line keeps the file's wrap | `bin/test` over `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/behaviour/test_docs_line_wrap.py` and `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`, one module at a time, green |
| S5. The rule change parses | Given this `frame/design.md`, when the one reader of `## Rule changes` reads it, then the `add` item is read whole and nothing is refused | `skills/settle/scripts/rule_changes.py`, which `chain_check.py` asks at the pull request for this work item (`docs/the-review-record.md` *What the check reads at the pull request*). The round's proofer runs `chain_check.py` over the branch |
| S6. The cause is named | Given the changelog fragment, when it is read against `## Scope` item 5, then it names the orchestrator's fix-pass spawn prompts in #955 and #1016 as the cause, by session id and line | Read by the round and the sealer against the transcript lines in `## Scope` item 5, and against `git show 2b68252c` and `git show 137d0a9c` |
| S7. The policy sentence shares no run with the build | Given `## Rule changes`' `to:` text and the two edited files at phase 2's commit, when `longest_run` of `tests/text/test_no_passage_is_pasted_into_a_second_file.py` measures the text against each file, then it finds no shared run of 15 words with `skills/code-review/orchestration.md` or `agents/crafter.md` | The measurement, `rule_changes.parse(<this file>, "docs").ops[0].new` against each file read at the phase's commit, run by the phase and recorded in its phase record. At `aa8b54cb` the `to:` text shares no 15-word run with any file of the paste check's corpus except its own destination, which was not measured (executed, the framer, 2026-10-28). Phase 2's new sentences are worded on their own, not taken from the `to:` text |

## Data & interfaces

None. No record grammar, command, output or file format changes. The round
record's lines keep their shapes (`docs/the-review-record.md` *The round
record*, the grammar table). What changes is who commits the fix pass's
lines, the text the orchestrator and the crafter act on, and the
assertions that read it.

## Rule changes

- add
  file: docs/the-review-record.md
  section: The round record
  to: **Each finding's `verdict:` and `answer:` lines have one writer, and the lines closed at one step reach the branch in a single commit.**
    A finding a fix pass answers is the pass's to write: it writes both lines last, after its fix commits and the corrections its sweep made, because a `fixed` verdict names a commit that is already there, and it commits neither. The orchestrator takes the round record from the hand-back as it stands and commits it, once for the whole pass, before it spawns the verifying round, which can read only what a commit holds. It edits no line in that commit, and a close it doubts goes into that round's spawn prompt. A finding closed with no fix pass, such as `deferred the frame` on the framer's route or a `deferred <home>` the orchestrator files at the cap, has the orchestrator as its writer, and the orchestrator writes and commits the lines of every finding it closes at that step together. A second hand on either line costs the round a record commit and gives a reader nothing.
    check: tests/text/test_the_rules_have_one_owner.py tests/text/test_a_moved_rule_leaves_its_definition.py

## Removes

- nothing
  why: Against the base the work adds sentences to the orchestrator's and the crafter's text and assertions that read them. Phase 2 rewrites sentences phase 1 added, which the base never held. It removes no sentence, unit, test or record of the base.

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-28 by framer, before the build.
Reframed 2026-10-28 by framer, after round 4.
