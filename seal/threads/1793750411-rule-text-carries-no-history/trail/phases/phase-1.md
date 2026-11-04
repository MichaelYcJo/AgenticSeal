# Phase 1: 1793750411-rule-text-carries-no-history

## What this phase found

**The frame holds against the tree.** Each coordinate `frame/design.md`
*Removes* gives for the three files of this phase opens the sentence it
names at 3bd60d29f (read, with `grep -n` in the base clone below). The
pins `frame/plan.md` *Technical context* names stand where it says. The
plan says no list of the other pins exists before a removal. Two more turned
up in this phase, and are listed under *What stood on a removed sentence*
below.

**The base census equals `frame/design.md` *Grounding*.** Both probes ran
read-only in `git clone --no-local` of the repository, checked out at
3bd60d29f under the session's scratch directory (executed). The probe was
one file, `test_tmp_census.py`, deleted after its runs (contract rule 7). It
implements D4 as written. The ten-word census builds its corpus from
`git ls-files -- '*.md'` filtered by `skills/settle/scripts/passages.py#in_corpus`.
It reads words through that module's `words`, uses runs of 10 words, and
applies D4's pair and scope rules. The marker probe uses D4's regex and
sentence split over the 48 in-scope files, with fenced blocks dropped.

| Reading at 3bd60d29f | Command | Result | *Grounding* |
|---|---|---|---|
| Scope size | `git ls-tree -r -l 3bd60d29f -- skills docs`, `.md` files without `docs/experiments/`, `skills/core/SKILL.md` and `skills/agent-contract/SKILL.md` | 48 files, 595,984 bytes | equal |
| Ten-word census | `python3 -I test_tmp_census.py <base clone>` | 2,078 of 88,708 in-scope words inside a shared run, 80 pairs, 264 shared runs. The six largest pairs, at 16, 12, 11, 10, 10 and 9 runs, are the ones *Grounding* lists | equal |
| Marker probe | the same command | 58 sentences in 22 files | equal |

The phase also took one reading at its build commit 19f0ceafe, by the same
command over a second clone. It is context for phase 3, and the HEAD
reading of record is phase 3's. It read 1,977 of 88,417 words, 80 pairs and
255 shared runs. The marker probe read 53 sentences in 22 files.

**Removals.** Each line number is at 3bd60d29f.

| File | Base line | Class | What went, and its grounds |
|---|---|---|---|
| `skills/implement/orchestration.md` | 19-21 | D3 | The rule for where a `seal/…` path resolves, copied from `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (and contract rule 11). It is now a citation of that section. The orchestrator reads that file too, as the same paragraph says ("The orchestrator reads both"). `tests/behaviour/test_first_setup_asks_once.py#test_the_session_rule_appears_once` already holds that the rule appears once in `SKILL.md` |
| `skills/implement/orchestration.md` | 116-117 | D3 | "Reading the plan and spawning the build is the approval, and no line records it", a 12-word run shared with `skills/implement/SKILL.md:297` *3. The SDD file set*. It now reads "The spawn is the approval (`skills/implement/SKILL.md` *3. The SDD file set*)". The consequence this section owns, no row of *Judgments of the run* for a frame spawned with no proposal, stays |
| `skills/implement/orchestration.md` | 119-120 | D2 | "Six of 0.27.x's fourteen work items wrote such a row, and each restated the spawn." This is the `## Removes` row. The rule before it states the act |
| `skills/implement/orchestration.md` | 125-126 | D2 | "Its first instance, #1148's frame: four proposals, one agreed, two agreed with a change, one rejected." This is the `## Removes` row. Its copy in `docs/running/the-agent-set.md:72-73` is phase 3's |
| `skills/implement/orchestration.md` | 225 | D2, borderline (Q1) | "`straight to the PR` was read as *call no agents at all*" is now "reads as". The past misreading is history. The example is the reason the rule gives a reader, so it stays in the present tense, as an example that is not history |
| `skills/implement/orchestration.md` | 276-277 | D2 | the clause ", and the room was made by taking the framer and the sealer out of the question". It tells how the four boxes came about. The ceiling rule, "a fifth box breaks this shape", stands without it. Why the framer is no box is stated in the present at `:324-327` |
| `skills/implement/orchestration.md` | 357-365 | D3 | The second statement of the edit gate in this file: which tools it refuses, that a `seal/` file is never refused, and what `seal no-work-item` records. All of it paraphrases `docs/checks/the-routing-check.md` *The edit check* (11-word census run), and `:166-174` of the same file already states it. The paragraph now points to that paragraph by its bold opening. It keeps the one act that paragraph lacks: run `seal no-work-item` on each branch the session edits, before its first edit there |
| `skills/implement/orchestration.md` | 443-445 | D2 | "The top rung used to read *6+ files, a new module, or an architectural choice*, and two of those three conditions measured size." This is the `## Removes` row: the rule's earlier wording |
| `skills/implement/orchestration.md` | 451 | O7 repair | "touched more files than that" is now "touched many files". "That" referred to the count in the sentence removed at `:443-445`. `frame/design.md` *Removes* did not name this line. It is the smallest repair that keeps the example's meaning |
| `skills/implement/orchestration.md` | 459-460 | O7 repair | "is a judgment where *six files* was a count" is now "is a judgment, not a count". The `## Removes` row asks for this repair |
| `skills/code-review/orchestration.md` | 98-101 | D3 | The explanation of why the contract reaches the orchestrator only when opened. It copies the opening of `skills/implement/SKILL.md` (`:21-25`, a 10-word census run), which every orchestrator reads before this file. The bold sentence stays, and now cites that opening |
| `skills/code-review/orchestration.md` | 199-203 | D2 | "The judgment rows of 0.27.x to 0.29.0 read this signal in seven work items." and the sentence after it. This is the `## Removes` row. The rule's reason, "a list of them is one more edge to chase", is in the present tense at `:193-195` |
| `skills/code-review/orchestration.md` | 290-291 | D2 | "With gh 2.100.0 it prints `no checks reported on the '<branch>' branch`". This is the `## Removes` row. The sentence now reads "the wait exits 1 without waiting", and the next sentence's act stands on that exit code |
| `skills/verify/orchestration.md` | 342-344 | D2 | "Measured over the transcripts on one machine, every second of overlap above a second came from calls batched into one message and none of it from a call that crossed a turn." It reports how a claim was measured, with no moment and no corpus a reader can open. The reading rule, read a share above 100 as concurrent calls, stands on the mechanism stated in the present before it: every call in one message carries that message's timestamp |

**What stood on a removed sentence (S3, contract rule 19).** Found by
`git grep -n -F` on the removed words over the whole tree, and by the
narrow runs below (executed).

- `tests/behaviour/test_the_set_a_work_item_always_has.py#KNOWN_PROSE`: the
  entry for `:444`, which `## Removes` names. Also the entry for `:460`,
  which `## Removes` does not name. That line no longer holds a count, so
  its entry allowed nothing. The comment in
  `test_the_top_rung_names_behaviour_rather_than_a_count` said a past-tense
  sentence marked by `used to read` was allowed. That sentence is gone, so
  the comment went with it.
- `tests/behaviour/test_release_hygiene.py#VERSIONS_OF_ANOTHER_PRODUCT`: the
  entry `("skills/code-review/orchestration.md", "2.100.0")` allowed the
  version that left `:290`.
- `tests/text/test_the_rules_have_one_owner.py#test_the_orchestrator_reads_mergeable_and_integrates_a_conflict_by_a_merge`:
  the asserted phrase `` `no checks reported on the '<branch>' branch` ``, the
  message that left with the gh version. The case's other phrase, "exits 1
  without waiting", still holds the act.

No Korean edition covers these three files. No other tree file states the
removed history sentences (`git grep -n -F` on "Six of 0.27", "the room was
made", "crossed a turn", "was read as *call", "seven work items" and
"2.100.0", executed). The two hits that remain are in later phases' files.
`skills/code-review/SKILL.md:199` is a different sentence and is phase 2's
`## Removes` row. `docs/running/the-agent-set.md:72` is phase 3's.

**Marker-probe sentences kept in these files**, six at 19f0ceafe:

| File | Sentence | Keep case (D2) |
|---|---|---|
| `skills/implement/orchestration.md` | "…plan approval — exists only before the first edit (issue #35)…" | a coordinate a reader opens, pinned by `tests/behaviour/test_the_set_a_work_item_always_has.py#test_the_rung_cites_the_issue_that_measured_the_count` |
| `skills/code-review/orchestration.md` | "The threshold is the largest context a fresh, never-resumed crafter reached in the 0.22.0 run, … (#945)…" | a definition that names its source; D2 gives this sentence as its example |
| `skills/verify/orchestration.md` | "**One segment measured on its own is still `session_cost.py <transcript>`**…" | no history: the regex matched "measured on" in "measured on its own" |
| `skills/verify/orchestration.md` | "A reading taken before the release whose release note lists #300 ended a span at the last call to begin…" | a version boundary the reader acts on when reading an older flow-log reading; D2 gives it as its example |
| `skills/verify/orchestration.md` | "In a reading taken before the release whose release note lists #377, `git` and `test` read low…" | the same keep case as #300 |
| `skills/verify/orchestration.md` | "In a reading taken before the release whose release note lists #642 there is no `read` row…" | the same keep case as #300 |

Every other base marker sentence in these files was removed above.

**Census passages kept in these files, with the D3 ground for each.**
Shared wording is two files naming one act or thing in the same words, and
it stays. An act is a passage this file's reader acts on at its step.

- `skills/implement/orchestration.md`, kept as shared wording or a
  citation phrase:
  - with `skills/core/SKILL.md`: "writes the decision, its grounds and the
    document it judged against".
  - with `skills/agent-contract/SKILL.md`: "each file of the work item's
    directory that states the present".
  - with `skills/code-review/orchestration.md`: "as contract rule 12 asks of
    the party that fixes".
  - with `skills/implement/SKILL.md`: "in place where the work item's subject
    is the policy root".
  - with `skills/implement/acts.md`: the heading citation "Orchestrator: what
    needs a person…" and "a work item that commits in more than one
    repository". Both are O2's.
- `skills/implement/orchestration.md`, kept as the act its reader takes,
  with the home cited:
  - with `skills/implement/bootstrap.md`: the condition under which the
    orchestrator opens bootstrap.
  - with `docs/running/the-review-and-parity-arms.md`: "`no` is never written
    where the question was not put", and "under `stop before the pull
    request` nothing runs at the end".
  - with `docs/running/the-agent-set.md`: the `Implementation` row's answer,
    already citing *What a spawn costs*. Its other side is phase 3's to
    judge.
- `skills/implement/orchestration.md`, kept where this file is the home:
  - with `CONTRIBUTING.md`: "The cost of a question is not its difficulty…".
    This file is that rule's home (`skills/core/SKILL.md` *Asking a person
    is the most expensive step* cites it), and the other side is O5.
  - with `docs/releasing/branch-and-release.md`: "every later pull request
    into the branch leaves it". This file ships the rule to every
    repository, and the `docs/releasing/` file applies it to this one.
    Phase 3 judges the other side.
- `skills/implement/orchestration.md`, kept on both sides because the
  copying side's reader does not open the home at that step:
  - with `agents/framer.md` (O1): the framer's three answers. An
    orchestrator never opens `agents/*.md`.
  - with `docs/checks/the-routing-check.md` *The edit check*: the gate's
    statement at `:166-174`. The orchestrator acts on it at the batch, and
    this section does not send it to that file.
- `skills/code-review/orchestration.md`, kept as shared wording or as the
  act its reader takes:
  - with `skills/verify/orchestration.md`: the opening "This file is the
    orchestrator's: …".
  - with `skills/implement/SKILL.md`: the fix pass's close blocks. The
    orchestrator acts on this when it writes the fix-pass prompt.
  - with `skills/implement/SKILL.md`: a commit after the build brings
    `changelog.md` along. This is the orchestrator's own commit, and both
    sides cite `docs/layout/the-record-layout.md`.
  - with `docs/forms/the-round-record.md`: the orchestrator's commit of the
    round record.
  - with `docs/running/the-run.md`: three runs in the regression routing
    table, the procedure that cites *The run* as its rule.
  - with `agents/sealer.md`: the verdict string `withheld reason: the base
    <name> resolves to no commit here`.
  - with `docs/checks/the-stamp.md`: "the pull request's check is what says
    the work item was sealed". The orchestrator tells the person this when
    no stamp is drawn.
  - with `skills/implement/bootstrap.md`: "the one value in this flow only
    a person may write". Bootstrap is opened only where no root exists, so
    this reader does not open it.
- `skills/verify/orchestration.md`, kept because the orchestrator reads
  this section at the broad run, and the section does not send it to the
  `docs/` file:
  - with `docs/running/the-broad-gate.md`: the partition sentence.
  - with `docs/running/measuring-a-run.md`: "a head call can outlive its own
    row's cut".
- `skills/verify/orchestration.md`, with `templates/setup/config.md`
  rule 3 (O5 on that side): the `new?` causes. Kept because
  `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py#test_the_unmeasured_word_says_so_and_every_reader_is_told_it`
  pins them in this file as text the orchestrator acts on when it runs a
  file at the base by hand (contract rule 14).

**Judged and kept, with no marker hit**, at 3bd60d29f's lines.
`skills/code-review/orchestration.md:355-357`
says `gh pr edit`'s GraphQL query "has stopped on an error about Projects
(classic)". It is an observation of an outside system that the act, sending
the body through REST, depends on (D2). The base-resolution paragraph at
`skills/code-review/orchestration.md:441-446` restates
`skills/verify/orchestration.md` *The broad gate*'s *Which base*. It stays
because `tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py#test_no_document_leaves_the_base_reading_as_the_ref_you_typed`
requires both files to say what the base resolves to, as text a person
reads (contract rule 14).

**Q2: the paraphrases this phase met are a sample.** Reading each file
whole found the in-file restatement of the edit gate and the contract
binding. Both are removed above. A restatement in other words of a file
outside this phase shares no ten-word run, so no probe lists it, and this
list is the reading's. Judged against `frame/questions.md` Q2's default.

**Narrow runs (executed, through `bin/test`).**

- `bin/test -q -p no:randomly tests/behaviour/test_the_set_a_work_item_always_has.py
  tests/behaviour/test_release_hygiene.py tests/text/test_the_rules_have_one_owner.py
  tests/behaviour/test_docs_line_wrap.py tests/text/test_no_passage_is_pasted_into_a_second_file.py`:
  exit 0, 125 passed, before the commit.
- The phase-boundary set (`skills/verify/SKILL.md` *Scope: cheap and often,
  broad and once*): 70 modules in one command. These are every test module
  that names one of the three files, plus every module that walks or globs
  a tree holding `skills/`, listed by `git grep -l`. The run at 19f0ceafe
  exited 1: 4,474 passed, 11 skipped, and 1 failed. The failure was
  `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
  because this work item had no `gaps.md` yet. Once `gaps.md` was written,
  `bin/test -q tests/behaviour/test_chain_hooks_hardening.py
  tests/behaviour/test_docs_line_wrap.py` exited 0 with 76 passed, and
  `seal unverified` on the work item exited 0 and listed 2 open rows.

No unit adds behaviour, so no case was written new and no `seal mutate` ran
(`skills/verify/SKILL.md` *The narrow command still has to be able to fail*,
the prose row). The suite stays `unverified` until the orchestrator's broad
gate.

**For phase 2.**

- `skills/code-review/orchestration.md` now cites "the opening of
  `skills/implement/SKILL.md`" for the contract binding. Phase 2 may remove
  the history in that opening (`:25-26`, "#107's headline failure…"), but
  the bold sentence and its reason have to stay.
- `skills/implement/orchestration.md` now cites `skills/implement/SKILL.md`
  *3. The SDD file set* for "the spawn is the approval", and *Document
  layout — two roots, three lifetimes* for the `seal/` root. Both cited
  statements have to stay where they stand.
- To check that a removal leaves no new 15-word run,
  `tests/text/test_no_passage_is_pasted_into_a_second_file.py` runs in
  under a second.
