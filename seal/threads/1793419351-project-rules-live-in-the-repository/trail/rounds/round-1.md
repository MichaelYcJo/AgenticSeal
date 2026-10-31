# Review round 1: 1793419351-project-rules-live-in-the-repository

target: 7a7f342f against release/v0.26.0

Round 1 covers both phases, the range `f80f48e6..7a7f342f`: C1 (`7306c33b`, `d094e66c`), C4 (`562067d6`), C3 (`bbdc6498`), C2 and the fragment (`c856b574`), and `79d27898`. There is no earlier round, so no fact is carried; every coordinate below was opened this round.

## Findings

### 1. A repair after a closed pull request is sent to a branch cut from a base that does not hold the work

severity: should
location: `skills/code-review/orchestration.md:190-194`
evidence: read `skills/code-review/orchestration.md:188-200`, `docs/release-checklist.md:13-16`, `seal/threads/1793419351-project-rules-live-in-the-repository/trail/phases/phase-2.md:11`, `seal/threads/1793419351-project-rules-live-in-the-repository/frame/design.md:184`
verdict: fixed a4280a14

The paragraph says "A `state` of `MERGED` or `CLOSED` stops the push", and then "The repair then goes on a new branch cut from the base". The second sentence follows both states, so it reads for both. Under `MERGED` it holds: the base holds the work, and `docs/release-checklist.md:13-16` already says the corrections then need a pull request of their own. Under `CLOSED` it does not. The base does not hold the work, so a branch cut from it has nothing for the repair to amend, and the owner closed the pull request, which is a decision the orchestrator has no grounds to route around.

Phase 2's record claimed the extension to `CLOSED` goes "beyond the frame's wording and not its scope". The frame's scenario (`frame/design.md:184`) names `MERGED` alone, so the extension rests on the crafter's account and on no frame text. This is the defect the run is watching for: a scope wider than the reading. An orchestrator acting on the sentence after a close would open a branch whose repair applies to nothing.

Rewrite the stop sentences in place, keeping the pinned clause `` `MERGED` or `CLOSED` stops the push `` word for word, and wrap to the file's width:

```markdown
A `state` of `MERGED` or `CLOSED` stops the push. The owner may merge or
close the pull request at any time after it opens, and a commit pushed to
its branch after that is in no pull request: nothing checks, reviews or
merges it. Under `MERGED` the repair goes on a new branch cut from the
base, which holds the work. Under `CLOSED` the base does not hold it, so the
orchestrator pushes nothing and says in its report that the pull request
was closed with a repair pending.
```

answer: Holds. The paste-ready fix was applied with the file's wrap: `MERGED` routes the repair to a new branch from the base, which holds the work, and `CLOSED` stops the push with the pending repair named in the orchestrator's report, because the base does not hold the work and the closing was the owner's decision. The pinned clause "`MERGED` or `CLOSED` stops the push" stands word for word, and `tests/text/test_the_rules_have_one_owner.py` passes. The fragment's sentence on the stop now says both routes. Phase 2's record called the extension to `CLOSED` within scope; this finding corrects that reading, and the record stays as the account of what the phase did.

### 2. The base comparison paragraph says the gate runs only the failing files at the base

severity: should
location: `skills/verify/orchestration.md:102-108`
evidence: read `skills/verify/orchestration.md:102-108`, `templates/setup/config.md:365`
verdict: fixed e971a99c

Phase 2's record claimed that C3 "cites the gate's own base run and does not restate it". The rewritten paragraph reads: "it is taken once an unexplained failure appears, and only for the files that failed. The gate takes it itself, at the base". The clause "only for the files that failed" stood before the change, in the sentence about the hand comparison under `git stash`. It now sits beside the gate's run and describes it. The rule the paragraph cites, `templates/setup/config.md:365` (rule 3), says the opposite: the row "runs once more, unchanged, at the base (nothing appended, no part cut, every part run as written)", and "The cost is one more run of the whole row, and only when the suite fails, whatever the number of failing files". So someone weighing the gate's cost, or deciding whether a failing file still needs a hand run, reads about a narrow base run that does not exist.

```markdown
**That comparison is reactive.** A baseline answers whose failure this is, so
it is taken only once an unexplained failure appears. The gate takes it
itself: it runs its whole row once more at the base and reads each failing
file against that run, as `templates/setup/config.md` *The criterion for
choosing a value*, rule 3, states. A file run at the base by hand runs in a
`git worktree add` of the base commit, never under `git stash`: every
worktree and session of the clone shares the one stash stack, so a pop can
take another session's entry.
```

answer: Holds. The paste-ready paragraph was checked against `templates/setup/config.md` rule 3 ("the row runs once more, unchanged, at the base", "one more run of the whole row, and only when the suite fails") and applied as written: the gate runs its whole row once more at the base and reads each failing file against that run. "Only for the files that failed" belonged to the hand comparison under `git stash`, and the hand run's sentence already says "a file".

### 3. Contract rule 12 asks every agent for a whole list, and says nothing of a class no list can close

severity: should
location: `skills/agent-contract/SKILL.md:159-166`
evidence: read `skills/agent-contract/SKILL.md:159-166`, `skills/code-review/SKILL.md:167-169`
verdict: fixed 9ad3b9f9

Rewritten rule 12 tells an agent to list the instances "by a method that makes the list whole". It names three methods and adds that "a list made by sampling is a finding even where every instance on it was fixed". Every agent receives this rule, and the crafter in a fix pass receives no other text on enumeration. Read alone, the rule says a whole list always exists. A class over a domain with no end, such as spellings, keywords or constructs, has no whole list. `skills/code-review/SKILL.md:167-169` says such an enumeration narrows a finding and does not close it, and sends the limit to Known limits or a `deferred <home>`. Only the proofer reads that sentence. So a crafter facing such a class can do one of two things. It can claim a method that makes the list whole, which it does not have. Or it can hand back a list the rule calls a finding, with no next step. The word "sampling" is also undefined: the sentence before it names two ways of listing, the instances in view and a search for one wording, and never says that these are what sampling means.

The phase record says nothing pins rule 12's wording (executed by the crafter: `tests/text/test_the_agent_contract_holds_the_universal_rules.py` pins no rule's text), so the rule's text is the only place this can be fixed. Write in fresh words, so that `tests/text/test_no_passage_is_pasted_into_a_second_file.py` finds no run shared with `skills/code-review/SKILL.md`:

```markdown
Do not fix the coordinate. A finding names an instance; the fix is owed to
every instance the same cause produces. List them by a method that makes the
list whole: build it from what produces the defect, take the artefact apart
into every one of its parts, or run a command that lists each thing holding
the property. The instances in view, or a search for one wording, find only
the spellings already seen, and a list made that way is a sample. Where the
class has no end, as spellings, keywords and constructs have none, no method
makes the list whole: the hand-back says so, and names where the open part
is recorded. The hand-back names the method and what it listed, and the
proofer judges the method as well as the instances: a sample handed back as
a whole list is a finding even where every instance on it was fixed.
```

answer: Holds. The paste-ready body was read against `skills/code-review/SKILL.md:167-169`, its grounds: it now defines a sample as a list made from the instances in view or a search for one wording, says that a class with no end has no whole list and that the hand-back says so and names where the open part is recorded, and makes the finding a sample handed back as a whole list. It shares no run of words with `skills/code-review/SKILL.md` (`tests/text/test_no_passage_is_pasted_into_a_second_file.py` passes), and was applied as written. The fragment's rule 12 sentence gains the open case.

### 4. The acts row of the pull request section still states the read that C4 replaced

severity: should
location: `skills/implement/acts.md:75`
evidence: executed `git grep -n -i 'json mergeable\|mergeable' -- . ':!seal/threads'`
verdict: fixed a4280a14

C4 rewrote the act. The orchestrator now reads `gh pr view <N> --json state,mergeable` when the pull request opens, before each push and after each push, and stops a push on `MERGED` or `CLOSED` (`skills/code-review/orchestration.md:188-200`). The section's row in `skills/implement/acts.md:75` still gives the old fact as its grounds: "nothing records that `mergeable` was read before CI was waited on". It does not name the read before a push or the stop, which nothing records either. Contract rule 19 asks that the same commit correct every other sentence stating the old fact. Phase 2's record lists the searches it ran for rule 12's words and for `git stash`, and names no search for this sentence. The search above returns this row and no other place outside C4's own paragraph and its pin.

Replace the clause in the row's last cell:

```markdown
nothing records that `state` and `mergeable` were read when the pull request opened and before and after each push, or that a push stopped on `MERGED` or `CLOSED`,
```

answer: Holds. The clause was replaced as given; it names the reads at the opening, before and after each push, and the stop on `MERGED` or `CLOSED`. `git grep -n 'mergeable' -- . ':!seal/threads'` after the fix returns C4's paragraph, its pin, this row and the test-duration index, and nothing else states the old read.

### 5. The new section's table sends one decision to two places

severity: should
location: `skills/implement/orchestration.md:360-364`
evidence: read `skills/implement/orchestration.md:360-364`, `skills/core/SKILL.md:67-73`
verdict: fixed 47cc66d2

Row 1 sends "a decision, with its grounds" to the work item's records, as the core's sentence at `skills/core/SKILL.md:67-73` does for every decision. Row 3 sends "a lesson or a decision whose home no work item in progress changes" to an issue. A decision made in a run about something no work item changes matches both rows. One example is the owner's ruling on a release's version, made while another work item is being built. Row 1 sends it to the records and row 3 to an issue. The text an agent reads should give one reading, and here the orchestrator picks between them. The core gives the records reading only. The frame's *In an issue* paragraph (`frame/design.md`) does send decisions to issues, but only decisions made outside the work item, such as #1199's owner decision. That points to keeping row 3 for decisions made while no work item is in progress.

```markdown
| a decision, with its grounds, made in the work item in progress | the work item's records, as `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both* states |
| a lesson whose home no work item in progress changes, or a decision made while no work item is in progress | an issue that names the home |
```

answer: Holds, fixed in my own words. Read against the finding's own example, the paste-ready split by when the decision was made sends the owner's ruling on a release's version, made while another work item is built, to that work item's records, which is not about that work item and is not where the frame's *In an issue* paragraph puts #1199's owner decision. The rows now split by what the decision is about: row 1 takes a decision about the work item in progress or a file it changes, and row 3 a lesson or a decision whose home no work item in progress changes. No decision fits both, and the finding's example lands in row 3, an issue.

### 6. The bold sentence lets local memory keep a copy of a rule

severity: should
location: `skills/implement/orchestration.md:354-358`
evidence: read `skills/implement/orchestration.md:354-358`, `skills/implement/orchestration.md:374-377`, `seal/threads/1793419351-project-rules-live-in-the-repository/frame/plan.md:53`
verdict: fixed 47cc66d2

Issue #1200's *Done when* asks the skill to say that "a session's local memory is not that place". The section says "never into a session's local memory alone". The word "alone" makes memory one of the places, as long as the repository holds the rule too. That allows a second copy of a rule beside the tree, which `skills/core/SKILL.md` *The rule a mechanism is kept against* forbids: "A fact has one source, and every other place links to it". The work item's own plan contradicts it too. After the merge it deletes every entry whose content stands in the tree (`frame/plan.md:53`, under *Operational impact*). The section's last paragraph limits memory to one machine's facts and the person's preferences, so the bold sentence and the last paragraph give two readings.

```markdown
**The orchestrator writes each decision and each lesson of a run into the
repository, never into a session's local memory.** The harness keeps that
memory on one machine, outside the repository, so a rule kept there is
unknown to a run on any other machine and to anyone who reads the
repository.
```

answer: Holds. The bold sentence was applied as given: "alone" is gone, and "kept only there" became "kept there", so the sentence and the section's last paragraph give one reading. `skills/implement/acts.md`'s row for the section still says "a lesson kept only in a session's local memory leaves the same tree as a run that learned nothing"; it describes what no check can see, not the rule, and it stands.

### 7. A lesson about a file the plugin ships has no reachable home when the run is in another repository

severity: should
location: `skills/implement/orchestration.md:363-364`
evidence: read `skills/implement/orchestration.md:354-365`, `CLAUDE.md:21-23`, `seal/threads/1793419351-project-rules-live-in-the-repository/trail/phases/phase-1.md:9`
verdict: fixed 47cc66d2

The section ships with the plugin and is read by the orchestrator in every repository the plugin runs in. Phase 1's record says so itself: it took the issue number out of the measurement row for that reason. Most acts the orchestrator learns about are read from the plugin's own files, such as a skill, an agent definition or `seal gate`. Row 2 sends such a lesson to "the file the act is read from", but only through a work item that changes that file, and no work item in a user's repository changes the plugin's files. So the lesson falls to row 3: "an issue that names the home". That issue would be filed in the user's own tracker, where nobody who can change the plugin file reads it. The other way the lesson can go is to edit the file in place, but the copy that loads is the installed one in the harness's cache. An edit there is local to one machine, and the next update erases it, which is the memory trap this section exists to remove. The section never separates the repository's own files from the plugin's.

The snippet below includes finding 5's change to the left cell. Wrap the cell as the table's other rows are wrapped:

```markdown
| a lesson whose home no work item in progress changes, or a decision made while no work item is in progress | an issue that names the home, in the tracker of the repository that holds the home; where the home is a file the plugin ships and the run is in another repository, the orchestrator names the lesson and that file in its report to the person, and edits no installed copy |
```

answer: Holds, and the home is the plugin's tracker, reached through the person. The orchestrator files nothing in another repository's tracker on its own: the person decides what goes there, and `skills/core/SKILL.md` makes asking a person the most expensive step, so the lesson goes in the report the person already reads, not in a question. Row 3 now says the issue goes in the tracker of the repository that holds the home. Where the home is a file the plugin ships and the run is in another repository, the orchestrator names the lesson and the file in its report, points at the tracker `.claude-plugin/plugin.json` names under `repository`, and edits no installed copy, which stays on one machine and is replaced at the next update. The paste-ready cell carried finding 5's split by time, which was not applied (finding 5's answer), so this cell is written in my own words over finding 5's row 3. The limit: the lesson reaches the plugin's maintainer only if the person takes it there, and nothing records whether they did.

## Confirmations

confirms: none
The frame's *The entries* table names 53 entry files, 14 by name and 39 run logs, and the memory directory holds exactly those 53 besides the index and the stray old copy of the index (executed: a listing of the directory compared by name with the table, no difference either way; the stray file is 9,438 bytes, as `frame/design.md` says). The index lists 53 entries and includes `local-memory-vs-project-rule.md`.

confirms: none
Each coordinate that the *in the tree* rows of *The entries* and *The lessons* cite exists at this commit (executed: one `git grep -n -F` per heading or paragraph opening, 47 coordinates, each found). The content of several was read against its lesson and matches. The `Broad gate` row runs `ruff` before `bin/test` (`seal/config.md`). The stamp is drawn from the sealer's `sealed` (`docs/the-review-record.md:418-424`). A second failed fix goes to the framer (`docs/the-review-record.md:578`, `:609`). The gate runs the row at the base itself (`templates/setup/config.md:365`). The stale `.pyc` reason is at `skills/verify/SKILL.md:192-196`. A `Not verified` item is closed by marking it (`skills/implement/SKILL.md:443`). `flow-measurement` is a lookup key (`docs/issues-and-milestones.md:79`). The wrong-base check is at `docs/release-checklist.md:122`. The measurement entry's home exists: issue comment 5787486569 is on #51 (executed: `gh api` on the comment).

confirms: none
The *Not kept* grounds hold where they can be checked. No step of the tree outside the records prescribes `gh pr merge --match-head-commit` or `gh issue edit --milestone` (executed: `git grep`, which returns only `--add-label` and `--remove-label` uses). A handoff after the guarantee costs a new audit, as the grounds say: a commit other than the closing records owes a new audit and the check refuses until it has one (`agents/sealer.md:162-165`). That is also what the orchestrator's 0.22.4 account says the check did.

confirms: none
The phase 1 departures hold. The section claims nothing about whether an agent can read the memory (`skills/implement/orchestration.md:354-358`), and the measurement row names the section that picks the log and no issue number (`:365`). The acts row is `still a sentence`, and its grounds match what nothing reads. `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py` passes with it (executed, in the narrow run under `## Probes`).

confirms: none
C4's pin was rewritten in the same commit as its sentence, and all three pinned clauses stand in the paragraph (`skills/code-review/orchestration.md:188-200`; `tests/text/test_the_rules_have_one_owner.py:353-358`, executed in the narrow run). The `gh pr edit` reason is written as history ("has stopped"). It matches the orchestrator's accounts of 0.4.0 and 0.8.0 in the session memory, which were read. The dangling citation of `docs/release-checklist.md` is gone: `git grep -n 'gh pr edit'` outside the work item returns only the new sentence (executed).

confirms: none
The two `from` texts of R1 and R2 stand in `docs/the-review-record.md` *The handoff* at this commit (executed: each `from` value, whitespace folded, found in the folded file). R1 to R4 are the latest decision of an unsettled design until the settle writes them, which `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* allows, so the issue's "written into its home" holds for them as a rule change.

confirms: none
The fragment's `### Process changes` rows each match a change the diff makes (C1, C2, C3, C4), with the date, one line of why and a source. `docs/the-record-layout.md:52-58` says the orchestrator writes the table with the fragment, while `agents/crafter.md:23` has the crafter write `changelog.md` in the last phase. The crafter's departure is between those two sentences, and both stood before this work item. The rows' content holds.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad suite, the repository-wide lint and `seal gate` at HEAD; the crafters' 93-module and 108-module runs and the `seal mutate` runs were not re-run here (`unverified`) | the branch at `7a7f342f` | the orchestrator, by `seal gate --base release/v0.26.0 --record seal/threads/1793419351-project-rules-live-in-the-repository` |
| Whether `gh pr edit` still stops on the Projects (classic) error today; a probe writes to a pull request, so this round did not run one, and the sentence is written as history | `skills/code-review/orchestration.md:236-239` | the orchestrator, at the next body replacement it makes |
| Whether `gh pr checks <N> --watch`, run at once after a push, waits for a workflow that has not yet reported a check (the `gaps.md` row stands as written) | `skills/code-review/orchestration.md:197-200` | the orchestrator, at the pull request's first push |
| Whether *The lessons* lists every lesson of the 39 run logs. This round read the logs of 0.8.0, 0.11.3, 0.18.0, 0.18.1, 0.22.4 and 0.25.1 in part and found no lesson without a row. 0.18.1's "two squashes green alone went red together" is covered by `docs/release-checklist.md:13-16` but not listed as a source of that row. The other logs were not read whole | `seal/threads/1793419351-project-rules-live-in-the-repository/frame/design.md` *The lessons* | the orchestrator, before it deletes the entries after the merge |
| Whether the orchestrator adopts the crafter's `### Process changes` rows as its own, which `docs/the-record-layout.md:52-58` assigns to it | `seal/threads/1793419351-project-rules-live-in-the-repository/changelog.md` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_every_orchestrator_act_names_its_delivery.py tests/text/test_the_agent_contract_holds_the_universal_rules.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_docs_line_wrap.py -q` | 119 passed, exit 0, in the branch worktree at `7a7f342f`; a narrow run, not the broad gate |
| a listing of the session memory directory compared by name with the entry names in `frame/design.md` *The entries* | 53 entry files on each side, no name on one side only |
| each R1 and R2 `from` value, whitespace folded, searched for in `docs/the-review-record.md`, folded the same way | both found |
| `git grep -n 'git stash' -- . ':!seal/threads'`, and the same for `gh pr edit`, `gh run watch` and `mergeable` | `git stash` stands only in C3's refusal and in one cost-classifier case; `gh pr edit` only in C4's sentence; `gh run watch` nowhere; `mergeable` in C4, its pin and `skills/implement/acts.md:75` (finding 4) |
