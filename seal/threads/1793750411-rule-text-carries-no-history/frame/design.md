# Design: rule text carries no history (#1317)

Issue #1317, the first item of milestone `release: 0.31.1`. The issue body
is the one the spawn prompt hands over, read by the orchestrator with
`gh issue view 1317 --json body,comments` on 2026-11-04, with no comments
(the orchestrator's finding; this framer did not reopen it). Every
coordinate below is at 3bd60d29f. That commit differs from the base
8d5a59c6c only by `routing.md` (`git diff --stat`, executed).

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | "History goes to git, the release notes and the work record." "A fact has one source, and every other place links to it." These two sentences are the grounds of every removal (D2, D3). A count of the lines removed is context and never a criterion |
| `skills/core/SKILL.md` *A document is cut by who opens it and at which step* (read) | A party pays for every byte of a file it opens. So a sentence no reader acts on at that step costs every opening, and a sentence a reader needs at its step stays (D2's keep cases) |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | A work item whose subject is the policy root's text edits `docs/` directly in its pull request. This item's subject is the text of `docs/` and `skills/`, so `## Rule changes` holds the no-change block. No section moves, so no unsettled design's operation is re-pointed |
| Unsettled `## Rule changes` (read: every `frame/design.md` under `seal/threads/`) | Two designs hold pending `change` operations. `1793726048-the-stop-judgment-holds-against-later-rows` quotes three sentences of `docs/running/the-run.md` *The run*. `1793732301-the-readme-is-written-for-a-first-reader` quotes one sentence of `docs/layout/the-record-layout.md` *The root records*, the 15-word sentence. The settle locates each change by its `from` (`skills/settle/rule-changes.md` *Rule changes*), so this item edits none of those four sentences (O4). The other seven unsettled designs state `- nothing` |
| `docs/layout/the-record-layout.md` *The root records* and `tests/text/test_no_passage_is_pasted_into_a_second_file.py` (read) | The paste check fails on any 15-word run two rule documents share. With 1793732301's pending change, the rule in force reads "No two rule documents share a 15-word run". So the copies left in the tree are runs of 10 to 14 words, which the ten-word census lists (D4) |
| `tests/text/test_a_moved_rule_leaves_its_definition.py` module docstring (read) | `WINDOW` is 15 because the longest kept application measured was 10 words and the smallest real copy was 25. A 10-word run is therefore not a copy by itself. The census lists candidates, and each one is judged (D3) |
| `skills/agent-contract/SKILL.md` rules 12 and 19 (read) | Rule 12: a list built by reading each file whole is a whole list for that file, and a grep for one wording is a sample. Rule 19: a sentence, case or citation that states a removed sentence is removed or corrected in the same commit (S3) |
| `docs/README.md` (read) | "`docs/experiments/` holds dated scratch documents and is no policy". It holds no rule text, so it is out (O3) |
| `docs/releasing/branch-and-release.md` *Cutting a release* (read) | "The orchestrator moves it in the commit that adds the changelog fragment of the release's first work item". This is the first work item into `release/v0.31.1`, so that commit moves `.claude-plugin/plugin.json` from 0.31.0 to 0.31.1 (S6) |
| `docs/layout/the-record-layout.md` *A change to the way of working writes its process row in its own fragment* (read) | The diff changes `skills/*/orchestration.md`, so `changelog.md` ends with a `### Process changes` table, which the orchestrator writes with the fragment (S6) |
| Earlier work item `1793678623-each-rule-rides-with-the-agent-that-uses-it` (#1313), `frame/design.md` *D4 History* and *D6 The measurement* (read) | #1313 found two history lines in the preloaded files and removed both. Its ten-word census method is the one D4 reuses, with this item's scope |
| `seal/follow-up.md` (read) | No row is waiting on this work. The row on *a figure about a corpus, stated with no moment* records that each grep enumeration of a class of claims shipped short. That is why D2 reads each file whole instead of trusting the marker grep |
| `skills/implement/orchestration.md` *The frame is read against the issue at the spawn*, `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* and *Orchestrator: the pull request opens once the sealer seals* (executed: `grep -n`) | The issue's examples still stand at the base: `skills/implement/orchestration.md:119-120` and `:125-126`, `skills/code-review/orchestration.md:199-203` and `:290-291` |

Measurements, each taken by this framer at 3bd60d29f in a
`git clone --no-local` under the scratch directory (executed):

| Measurement | Reading |
|---|---|
| Scope size: `git ls-tree -r -l 3bd60d29f -- skills docs`, `.md` files, without `docs/experiments/`, `skills/core/SKILL.md` and `skills/agent-contract/SKILL.md` | 48 files, 595,984 bytes |
| Ten-word census before (D4's method) | 2,078 of the scope's 88,708 words sit inside a run another rule document also holds. 80 file pairs, 264 shared runs. The largest pairs: `skills/config/SKILL.md` and `templates/setup/config.md` 16; `docs/checks/the-fold.md` and `skills/settle/SKILL.md` 12; `skills/commit-pr-convention/SKILL.md` and `templates/setup/config.md` 11; `docs/running/what-a-script-gates.md` and `skills/core/SKILL.md` 10; `docs/releasing/issues-and-milestones.md` and `docs/releasing/release-checklist.md` 10; `skills/implement/SKILL.md` and `skills/implement/orchestration.md` 9 |
| History-marker sentences before (D4's marker probe) | 58 sentences in 22 files. Judged from their text, 17 are history the rule stands without (the rows of `## Removes`). The rest are coordinates, examples, version boundaries a reader needs, or no history at all. The count is noisy and is context only |
| The same marker grep over `agents/*.md`, `skills/core/SKILL.md` and `skills/agent-contract/SKILL.md` | one hit, `skills/core/SKILL.md:131` "never used to block", which is no history. This is a sample, and those files are outside this scope either way (O1) |

## Scope

In scope: every `.md` file under `skills/` other than `skills/core/SKILL.md`
and `skills/agent-contract/SKILL.md`, and every `.md` file under `docs/`
other than `docs/experiments/`. That is 48 files, the Korean edition
`docs/layout/one-root-by-lifetime.ko.md` among them.

1. **History sentences.** Each in-scope file is read whole. Each sentence
   that tells how a rule was found is removed where the rule stands without
   it: a count of work items, rounds or findings, the release that first
   showed something, a tool version and what it printed, a date of a past
   event, or a rule's earlier wording. D2 gives the test and its keep cases.
2. **Copies.** Each passage of 10 or more words that an in-scope file shares
   with another rule document (the census, D4) is judged. So is each
   paraphrase of another file met while reading for item 1. A copy whose
   reader opens the home at that step is removed from the copying side, and
   the home is cited where the reader needs the pointer. D3 gives the test.
3. **What stood on a removed sentence** goes in the same commit (contract
   rule 19): a test that pins the sentence, a `KNOWN_PROSE` entry, a
   citation of it, and its counterpart in a Korean edition.
4. **The census before and after** (D4). Both readings, with the commands
   and the commit each measured, go into the last phase record. `changelog.md`
   holds the reading at the work item's last code commit, and the pull
   request body copies it from there.
5. **Each removal is recorded with its grounds.** Each removal this frame
   names is a row of `## Removes`. Each other removal, a copy or a sentence
   the whole reading found, is listed in the phase record that made it, with
   its file, its line at the base, its class (D2 or D3) and its grounds. The
   same record lists each history-marker sentence the phase kept, with the
   keep case it meets.
6. **The release's first-item duties.** The commit that adds `changelog.md`
   moves `.claude-plugin/plugin.json` to `0.31.1`. `changelog.md` ends with
   a `### Process changes` table.

Out of scope:

- O1. The preloaded files `skills/core/SKILL.md`, `skills/agent-contract/SKILL.md`
  and `agents/*.md`. #1313 judged them. Where a copy pairs an in-scope file
  with one of them, only the in-scope side changes.
- O2. `skills/implement/acts.md`, and each census pair it belongs to, on
  both sides. #506 follows this item and judges "whether the table and its
  enumeration stay" (the owner's comment on #506, 2026-11-03, the
  orchestrator's finding). A citation of `acts.md` written now could name a
  table #506 removes. The marker probe found no history sentence in it.
- O3. `docs/experiments/`. It is dated scratch and no policy
  (`docs/README.md`), so its dates are its content.
- O4. The four sentences that pending `from` lines quote (*Grounding*), and
  every directory under `seal/threads/` other than this item's.
- O5. Files outside the issue's scope: `templates/`, `README*.md`,
  `CONTRIBUTING.md`, `CLAUDE.md`, and the comments and docstrings of `.py`
  files and tests. A census pair with one of them changes only its
  in-scope side. A docstring that narrates history is not this item's.
- O6. A new check or script. Plan row A2 gives the reasons.
- O7. Any change to what a rule says. Where a removal leaves a sentence
  broken, the repair is the smallest one that keeps the rule's meaning.
  Where a removal takes a rule's only stated grounds, the grounds are
  stated in the present tense or cited.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A1 The issue's examples are gone | Given HEAD, when the files are searched, then "Six of 0.27.x's fourteen", "Its first instance, #1148's frame", "read this signal in seven work items" and "With gh 2.100.0" stand in no in-scope file | `git grep -n -F` on each phrase over `skills` and `docs`, with no hit |
| A2 Every named removal is made | Given HEAD, when each `## Removes` row is read against the diff, then each named sentence or clause is gone, or the phase record names it as a departure with grounds | the proofer, row by row |
| A3 Every other removal has its grounds | Given the phase records, when the diff's removed lines are read, then each removed history sentence or copy appears in a phase record with its file, base line, class and grounds | the proofer, by reading the diff against the records |
| A4 What stays is argued | Given HEAD, when D4's marker probe runs, then each sentence it still lists is in a phase record with its keep case | the last phase record's table |
| A5 The census shows the change | Given the base and HEAD, when D4's two probes run on each, then the base readings equal the ones under *Grounding* and the HEAD readings are in the last phase record and in `changelog.md` | the probe commands in the last phase record |
| A6 No pending `from` moved | Given HEAD, when each of the four sentences under O4 is searched with whitespace collapsed, then each still stands where its design quotes it | `git grep -n -F` on a distinctive part of each sentence |
| A7 The pins follow the text | Given HEAD, when the tests of each touched file run narrow, then they pass, and no `KNOWN_PROSE` entry or assertion names a removed sentence | the narrow runs each phase record names, and `tests/behaviour/test_both_editions_carry_the_same_folds.py`, `tests/behaviour/test_docs_line_wrap.py` and `tests/text/test_no_passage_is_pasted_into_a_second_file.py` among them. The suite stays `unverified` until the orchestrator's broad gate |
| A8 The release starts | Given HEAD, then `.claude-plugin/plugin.json` reads `0.31.1`, and `changelog.md` ends with a `### Process changes` table whose rows name the orchestration files the diff changes | reading both files |

## Data & interfaces

No code, schema, command or form changes. The only file outside Markdown
that changes is `.claude-plugin/plugin.json`'s `version`. A test changes
only where it pins a removed sentence (S3).

### D2 What counts as history, and what stays

A sentence or clause is **history** where it says what happened, when, or
how often, and the rule's present reason does not depend on it. Examples:
"Six of 0.27.x's fourteen work items wrote such a row", "in 0.16.0 one
crafter call hung for 4 h 48 min", "With gh 2.100.0 it prints", "The top
rung used to read". It goes. Its record is git, the release notes and the
work item that wrote it.

A sentence **stays** where its reader needs it at its step:

- **A version boundary the reader acts on.** Examples: a pact header that
  0.18.x wrote still reads (`docs/layout/the-pact.md`), and a reading taken
  before the release that lists #300 (`skills/verify/orchestration.md`).
- **A definition that names its source.** Example: the resume threshold "is
  the largest context a fresh, never-resumed crafter reached in the 0.22.0
  run" (`skills/code-review/orchestration.md:39-41`). Without it the
  threshold has no value.
- **A coordinate a reader opens.** Examples: `#51`, the log a reader posts
  to, and "(issue #35)", which
  `tests/behaviour/test_the_set_a_work_item_always_has.py#test_the_rung_cites_the_issue_that_measured_the_count`
  pins for a reader to look up. A bare citation goes only with the
  sentence it stands in.
- **A dated observation of an outside system that the act depends on.**
  Example: the Console listing "by the repository owner's reading of the
  Console page on 2026-10-07" (`docs/releasing/release-checklist.md`). The
  date says when the claim was true.
- **An example that is not history.** Examples: `1.2.3`, and
  `closes #153 and closes #150`.

A clause that attributes a decision to a person and a date, such as "(the
owner, 2026-10-25)", is history: merging into `docs/` is what ratifies the
text. A borderline case is the phase's to decide, and its record states the
case and the grounds (questions Q1).

### D3 What counts as a copy, and which side stays

A census passage is a **copy** where it states a fact or a rule whose home
is another file. It is **shared wording** where two files name the same
thing in the same words, such as "the commit subject and body, the pull
request title and body", or a heading-like phrase in the index. Shared
wording stays.

For a copy, the side that stays is the home: the file that owns the fact by
`docs/README.md`'s index, by a skill's `SKILL.md`, or by what the rule says
about itself. The other side keeps the act its reader takes and cites the
home, or loses the passage where it already cites it. Where the copying
side's reader does not open the home at that step, the copy stays on both
sides and the phase record says why. #1313's D3 kept `skills/implement/SKILL.md`'s
copy of contract rule 9 on that ground. A `docs/README.md` row that names
the question a document answers is the index's own fact, and it stays.

### D4 The census

Both probes run read-only, from a `git clone --no-local` in the phase's
scratch directory, once at 3bd60d29f and once at HEAD. Neither is
committed, and each is deleted after it runs (contract rule 7).

- **The ten-word census.** The corpus is every path `git ls-files -- '*.md'`
  lists that `skills/settle/scripts/passages.py#in_corpus` accepts. Each
  file is normalised with that module's `words`. A run is 10 consecutive
  words. A run's owners are the corpus files that hold it. A file is **in
  scope** where its path starts with `skills/` and is neither
  `skills/core/SKILL.md` nor `skills/agent-contract/SKILL.md`, or starts
  with `docs/` and not with `docs/experiments/`. Count every unordered pair
  of a run's owners that are not both under `agents/` and of which at least
  one is in scope. Report three figures: the pairs, the sum over pairs of
  their distinct shared runs, and the in-scope words that sit inside any run
  another corpus file holds, against all in-scope words. Then list each
  maximal shared passage with its pair. The base reading must equal the one
  under *Grounding*, which shows the probe is the same one.
- **The marker probe.** Over the 48 in-scope files, drop fenced blocks,
  join the lines, split into sentences after `.`, `!` or `?` that is
  followed by a space and a capital, `` ` ``, `*` or `(`. Count the
  sentences that match, case-insensitive:

  ```
  #\d{2,}\b|\b\d+\.\d+\.(\d+|x)\b|\b20\d\d-\d\d-\d\d\b|\bwork items?\b[^.]{0,40}\b(wrote|did|ran|found|carried|had)\b|\bfirst instance\b|\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|\d+) of (the )?(\w+ )?\d*\s*(\w+ )?(work items|rounds|findings|releases|records)\b|\bin (seven|six|five|\d+) work items\b|\bwith gh \d|\bwas (found|measured|seen)\b|\bmeasured (on|at|in)\b|\bused to\b
  ```

  This is a reading guessed from words. It is reported, it blocks nothing,
  and it is no census of the class. The census of the class is what the
  phases list by reading each file whole (S1, S5).

## Rule changes

- nothing
  why: This work item's subject is the text of the policy root and of the skills, from which it removes history and copies without changing what any rule says, so it edits `docs/` directly in its pull request under `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, moves no section, and leaves the settle no decision to gather.

## Removes

Each row is at 3bd60d29f. "Clause" means that part of the sentence goes and
the rest stays.

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| "Six of 0.27.x's fourteen work items wrote such a row, and each restated the spawn." | `skills/implement/orchestration.md` *The frame is read against the issue at the spawn* (`:119-120`) | history (D2). The rule before it states the act. The count is in the 0.27.x work items' records |
| "Its first instance, #1148's frame: four proposals, one agreed, two agreed with a change, one rejected." | the same section (`:125-126`) | history (D2). #1148's records hold it |
| "Its first instance, #1148's frame, read four proposals: one agreed, two agreed with a change, one rejected." | `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each* (`:72-73`) | history (D2), and a copy of the row above |
| "every orchestrating session read its 1,783 words before #1148" (clause) | `docs/running/the-agent-set.md` *What a spawn costs* (`:166-168`, the sentence on why the acts table stands in a file of its own) | history (D2). The reason before it, that a maintainer reads the table and an orchestrator never does, stands alone |
| "The judgment rows of 0.27.x to 0.29.0 read this signal in seven work items." and the sentence after it, which reports what those runs showed | `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* (`:199-203`) | history (D2). The rule stands in the sentences before it. The judgment rows of those work items hold it |
| "With gh 2.100.0 it prints `no checks reported on the '<branch>' branch`" (clause) | `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* (`:290-291`) | history (D2): a tool version and what it printed. "exits 1 without waiting" stays, because the next sentence's act stands on the exit code alone |
| "The judgment rows of 0.26.0 to 0.29.0 trace nine regressions in seven work items to a paste-ready fix applied as given whose reach was one coordinate." | `skills/code-review/SKILL.md` *The record* (`:198-200`) | history (D2). #1286's records hold it |
| "The top rung used to read *6+ files, a new module, or an architectural choice*, and two of those three conditions measured size." | `skills/implement/orchestration.md` (`:443-445`) | the rule's earlier wording (D2). The bold sentence and the two bullets state the rule. The cost paragraph's "*six files* was a count" is repaired as O7 says |
| the `KNOWN_PROSE` entry `"used to read *6+ files, a new module, or an architectural choice*, and two of"` | `tests/behaviour/test_the_set_a_work_item_always_has.py#KNOWN_PROSE` | the line it allows is gone (S3) |
| "which is what every work item here did before the framer shipped, and what nothing in the set could say was wrong" (clause) | `skills/implement/SKILL.md` *3. The SDD file set* (`:291-293`) | history (D2). The sentence's first half states the effect |
| "in 0.16.0 one crafter call hung for 4 h 48 min and nobody noticed (#680)" (clause) | `docs/running/the-run.md` *The handoff* (`:87`); no pending `from` quotes it | history (D2). "an agent can end without one" grounds the rule alone |
| "and in 0.22.1 to 0.22.4 five verifying rounds confirmed such fixes and found nothing else" with its citation (clause) | `docs/checks/the-pull-request-check.md` | history (D2). The sealer's reading of every record at HEAD is the reason |
| "(the owner, 2026-10-25)" | `docs/checks/the-routing-check.md` | history (D2): an attribution. The reason stands in the sentence |
| "since the templates no longer invite it and #1147 audits what stands" (clause) | `docs/forms/the-round-record.md` | history (D2), and #1147 is closed (`gh issue view 1147`, executed), so the clause states a false present. The grounds are restated in the present tense, or cited from `docs/layout/the-record-layout.md` (O7) |
| "In 0.24.0, 12 of 17 recurring review findings stood only in a work item's own records, one restating another (#1148)." | `docs/layout/the-record-layout.md`, the paragraph opening *A fact of a work item has one record* | history (D2). The rule before it stands alone |
| "The reading is exact, and the rule it holds was approved on 2026-09-02, held by nothing, and broken by 14 of the 37 patch releases from v0.8.1 to v0.25.1." (everything after "The reading is exact") | `docs/releasing/branch-and-release.md` | history (D2) |
| "`release: 0.20.0` stood open eleven days after its tag and `release: 0.21.0` five, each closed by hand." | `docs/releasing/release-checklist.md` (`:363-364`) | history (D2). The sentence before it gives the reason |
| "A band read as a verdict filed #1259, for a session start that grew by 397 B because the core now reaches every session from one source, and the owner closed it as not a defect." | `docs/running/measuring-a-run.md` | history (D2). #1259 holds it |
| each other history sentence the whole reading finds (S1) | the 48 in-scope files | D2. Listed with grounds in the record of the phase that removed it |
| each copy the census or the reading finds (S2) | the in-scope side of each pair outside O2 | D3. The home keeps the fact. Listed with its pair and grounds in the phase record |
| each test pin, `KNOWN_PROSE` entry, citation or Korean counterpart of a removed sentence (S3) | wherever `git grep` on its words finds it | contract rule 19 |

This work adds no mechanism: no check, script, hook, label or mark.

The phases judge these candidates by the D2 test, because their sentences
also carry a reason a reader may need. The marker probe found them:
`docs/releasing/issues-and-milestones.md`'s two releases named in
*A release is sized by what has to be in effect* and "the branch
`release/v0.3.0` shipped as 0.2.0"; `docs/releasing/release-checklist.md`'s
#1148 sentences near `:84-96`; and the paraphrase in
`docs/running/the-agent-set.md` of `skills/implement/orchestration.md`
*The frame is read against the issue at the spawn*.

Framed 2026-11-04 by framer, before the build.
