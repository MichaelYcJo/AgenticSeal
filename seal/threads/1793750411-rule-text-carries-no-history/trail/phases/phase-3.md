# Phase 3: 1793750411-rule-text-carries-no-history

## What this phase found

**The frame holds for this phase's files.** Each `## Removes` row on a file
under `docs/` opens the sentence it names at 3bd60d29f (read, with `grep -n`
on `git show 3bd60d29f:<path>`): `docs/running/the-agent-set.md:72-73` and
`:166-168`, `docs/running/the-run.md:87`, `docs/releasing/release-checklist.md:363-364`,
and the rows that name a file without a line. Phases 1 and 2 changed no file
under `docs/` (`git diff --stat 3bd60d29f 93ae804ad -- docs` prints nothing,
executed), so each base line below is also the line at 93ae804ad. The
phase's files are the 23 that `git ls-files 'docs/**.md' 'docs/*.md'` lists
outside `docs/experiments/`, the Korean edition among them. Each was read
whole (rule 12's second method), so the removals below are a whole list for
these files. The paraphrases among them are a sample (Q2).

**What phase 2 handed this phase, confirmed against the tree (read).**

- `docs/running/the-agent-set.md:104-106` cites
  `skills/implement/orchestration.md` *Orchestrator: the order inside a
  ticket* for "a decision the orchestrator folds into the plan before the
  spawn". That section's paragraph opening **A decision made after the frame
  is committed is folded** states the fold, so the citation holds. The
  sentence stays on the `docs/` side: it is the reason the paragraph's rule,
  a phase leaves a record, keeps no copy of a spawn's scope, and the
  paragraph cites its home. `skills/implement/SKILL.md` *3. The SDD file set*
  keeps its own sentence, as phase 2 said.
- The `## Removes` row for `docs/checks/the-pull-request-check.md`'s
  "in 0.22.1 to 0.22.4" still stood at HEAD, and this phase removed it.
- The `docs/` side of each census pair phase 2 listed is judged below, under
  *Census passages kept*.

**Removals.** Each line number is at 3bd60d29f. A row marked `Removes` is a
row of `frame/design.md` *Removes*; every other row is a removal the whole
reading found.

| File | Base line | Class | What went, and its grounds |
|---|---|---|---|
| `docs/running/the-agent-set.md` | 64-72 | D3 | The steps of the frame exchange: the orchestrator proposes with grounds, the framer agrees, agrees with a change or rejects, a rejection is a row of *Alternatives considered*, a disagreement is named in the pull request body, and the counts go to the flow log. They paraphrase `skills/implement/orchestration.md` *The frame is read against the issue at the spawn*, which the paragraph names as the procedure. The paragraph keeps why the split holds, that the orchestrator edits no frame file, the one-exchange bound and that no check reads it. This was a candidate `frame/design.md` *Removes* named |
| `docs/running/the-agent-set.md` | 72-73 | D2, `Removes` | "Its first instance, #1148's frame, read four proposals: one agreed, two agreed with a change, one rejected." |
| `docs/running/the-agent-set.md` | 136-139 | D2, borderline (Q1), O7 repair | "a judgment it made in the run … reached the next session only through a spawn prompt or memory" is now "makes … would reach". The past tense told what happened before the rule. The sentence is the rule's only stated reason, so it stays in the present tense |
| `docs/running/the-agent-set.md` | 166-168 | D2, `Removes` | the clause "and every orchestrating session read its 1,783 words before #1148". The reason before it stands alone |
| `docs/running/the-run.md` | 81-82 | D3 | "a count can be checked while the claim it stands for cannot". It restates contract rule 5, which `skills/implement/SKILL.md` *1.* names as where "why an aggregate is not a coordinate" stands. The sentence now cites the rule |
| `docs/running/the-run.md` | 84 | D2 | the clause "which in 0.18.1 and in #1174 cost a repair and once a rewrite of the branch's history". The rule's reason, that an agent copies a prompt's paths into its records where a real path is refused, stands before it |
| `docs/running/the-run.md` | 87 | D2, `Removes` | the clause "in 0.16.0 one crafter call hung for 4 h 48 min and nobody noticed (#680)". "an agent can end without one" grounds the rule |
| `docs/running/the-broad-gate.md` | 39-41 | D3 | "A suite that is not mentioned reads as a suite that passed" and the handover label. It copies contract rule 2 (a 10-word census run with the contract and one with `agents/crafter.md`). The sentence before it already sends the reader to where an agent's rule lives, and it now cites rule 2 for the label |
| `docs/running/what-a-script-gates.md` | 3-4 | D3 | "A script holds a gate only on a fact it reads exactly, an agent holds the gates on meaning", a 10-word census run with `skills/core/SKILL.md` *The rule a mechanism is kept against*, which the next sentence names as the rule. The opening now says what the document lists |
| `docs/running/what-a-script-gates.md` | 12-13, 20-23 | D3 | From the bold rule, "and names as not read a line or a file that looks like one of the form's and is not one"; from its body, "No script carries a list of the spellings a label is written in" with its reason, and "What a script answers exactly stays a script and the session waits on its exit code". Each copies the core's *The rule a mechanism is kept against* or *Judgment is spent where meaning is the question* (two 10-word census runs). The body keeps the closed form, its examples, what is refused and what is named, and the check's pull-request duty, and cites the core's sections for the rest |
| `docs/running/measuring-a-run.md` | 97-100 | D2, `Removes` | "A band read as a verdict filed #1259, … and the owner closed it as not a defect." The sentence after it states the cost in the present tense |
| `docs/checks/the-pull-request-check.md` | 48 | D2, `Removes` | the clause "and in 0.22.1 to 0.22.4 five verifying rounds confirmed such fixes and found nothing else (#1045)". The sealer's reading of every record at HEAD is the reason |
| `docs/checks/the-routing-check.md` | 16-17 | D2, `Removes` | "(the owner, 2026-10-25)", an attribution. The reason stands in the sentence |
| `docs/forms/the-round-record.md` | 21 | D2, `Removes`, O7 repair | "since the templates no longer invite it and #1147 audits what stands". #1147 is closed, so the clause stated a false present. The grounds now read "since no template holds a place for a copy", citing `docs/layout/the-record-layout.md` *seal/threads/<work-item-id>/*, whose paragraph opening **A fact of a work item has one record** states it. The wording avoids a ten-word run with that paragraph |
| `docs/layout/the-record-layout.md` | 140-141 | D2 | the clause "and that state is where three reader defects of one release came from". "A record carries no comment, so a comment state in its reader models nothing the record holds" is the reason |
| `docs/layout/the-record-layout.md` | 153 | D2, `Removes` | "In 0.24.0, 12 of 17 recurring review findings stood only in a work item's own records, one restating another (#1148)." |
| `docs/layout/one-root-by-lifetime.md` | 246-247 | D2, borderline (Q1), O7 repair | "a reader that stopped at it silently took every row below it" is now "stops … takes". The past defect was the rule's only stated reason, so it stays in the present tense |
| `docs/layout/one-root-by-lifetime.ko.md` | 234-235 | the same, its Korean counterpart | "빼 버렸습니다" is now "빼 버립니다", following the English edition. The heading sequence is unchanged, which `tests/behaviour/test_both_editions_carry_the_same_folds.py` reads |
| `docs/releasing/branch-and-release.md` | 34-37 | D2, borderline (Q1), O7 repair | "Moved at the end, the version needed a pull request of its own, … and that pull request was one more wait" is now "would need … would be". It told the earlier practice as a past event, and it is the rule's only stated reason, so it stays as the cost of the alternative |
| `docs/releasing/branch-and-release.md` | 304-311 | D3 | The workflow file, its trigger and what the label does, which `docs/releasing/issues-and-milestones.md` *A label says a ticket is already in, before the release ships* states and the paragraph already named as the owner (a 10-word census run). The paragraph keeps the contrast its reader needs, *is this in yet* against *is this done*, and now cites the section |
| `docs/releasing/branch-and-release.md` | 351 | D2, `Removes` | everything after "The reading is exact": the approval date and the count of patch releases that broke the rule |
| `docs/releasing/release-checklist.md` | 87-89 | D2 | "0.24.0's four work items read 17 recurring of 36 findings, 12 in records alone, and 0.25.0's one read 3 of 10, 1 in a record alone." A count of past findings. The count's present use, a records-alone count that does not fall is read as one that rose, stands after it. This was a candidate `frame/design.md` *Removes* named |
| `docs/releasing/release-checklist.md` | 95-96 | D3, in the file | "; #1148 removed the records' copies of one another so that none could go stale", which restates `:86-87` of the same paragraph |
| `docs/releasing/release-checklist.md` | 112-114 | D2 | "In the 0.24 settle a switch to `main` and back restored 28 `gaps.md` files, the removal commit left them tracked, and the broad gate refused the tree." The sentence before it states what `git switch` does, which is the reason to commit first |
| `docs/releasing/release-checklist.md` | 229-230 | D3 | "The version hook reads tags and nothing else; an untagged release is one no installed session is ever told about." It copies `docs/releasing/branch-and-release.md` *Cutting a release* (a 10-word census run), the document the checklist's opening names as where each step's why stands. It now cites that section |
| `docs/releasing/release-checklist.md` | 295-297 | D2, then D3 | the clause "one of the two once went twenty-eight days without a commit". Its removal joined the reasons before and after it into a 10-word run of `docs/releasing/branch-and-release.md` *Cutting a release*, so the box's reason now cites that section (cc4d9902a). The census at af569f223 showed the new run |
| `docs/releasing/release-checklist.md` | 363-364 | D2, `Removes` | "`release: 0.20.0` stood open eleven days after its tag and `release: 0.21.0` five, each closed by hand." The sentence before it gives the reason |
| `docs/releasing/issues-and-milestones.md` | 25-30 | D2, borderline (Q1) | The two releases that showed the sizing criterion: the release that shipped the framer and the one that replaced the deleted checklist, with "Neither was cut short of a target. Both are named rather than numbered". They are past events told as examples. "One change that decides how the next ticket runs is a release on its own" states the criterion, and no case reads the examples (`git grep` on "shipped the framer" over `tests/`, executed). This was a candidate `frame/design.md` *Removes* named |
| `docs/releasing/issues-and-milestones.md` | 121-124 | D3 | Why the tag and never `plugin.json` decides, which `docs/releasing/release-checklist.md` *What a release pull request is held to* states with its check (two 10-word census runs). It now cites that section |
| `docs/releasing/issues-and-milestones.md` | 347-354 | D3 | Who retitles the issue, which `skills/commit-pr-convention/SKILL.md` *Commit messages* states, and where a `feat:` filed into a patch milestone moves, which `docs/releasing/branch-and-release.md` *Work accumulates on a release branch* states and the sentence already cited. Both now stand as citations. The bold rule and its reason, which the skill does not give, stay |

The commits are 36c88cc9c (the removals), af569f223 (the release checklist's
two shortened paragraphs wrapped again, no word changed:
`diff` of the word streams of the two trees' copies printed nothing,
executed) and cc4d9902a (the marketplace box's citation).

36c88cc9c is the amended form of 56a4e9afb. The amend changed the commit
message alone, whose counts of copies and repairs were wrong, before
anything named the commit or pushed it (`git status -sb` showed no
upstream, executed). The tree is the same.

**What stood on a removed sentence (S3, contract rule 19).** I ran `git grep
-n -F` over the whole tree, without `seal/threads/` and `docs/experiments/`,
on the words of each removal (executed): "0.18.1", "1174", "4 h 48",
"#680", "nobody noticed", "0.22.1 to 0.22.4", "#1045", "five verifying
rounds", "2026-10-25", "no longer invite", "#1147", "three reader defects",
"12 of 17", "In 0.24.0", "2026-09-02", "14 of the 37", "held by nothing",
"needed a pull request of its own", "one more wait", "label-merged-on-release-branch.yml",
"owns both mechanisms", "stops looking like one nobody", "twenty-eight",
"0.24 settle", "stood open eleven", "17 recurring", "measure of #1148",
"so that none could", "no installed session is ever told", "The version
hook reads tags", "shipped the framer", "Neither was cut short", "named
rather than numbered", "retitles the issue", "renamed forward only",
"moves at that moment", "only its tag says so", "#1259", "397 B",
"first instance", "1,783", "four proposals", "proposes, with grounds",
"not mentioned reads as", "labelled, never omitted", "claim it stands
for", "spellings a label", "silently took" and "빼 버렸습니다", with
`.test_durations` left out. No test, `KNOWN_PROSE` entry or citation states
a removed sentence. Each other hit is a different text:

- the homes the new citations name: contract rules 2 and 5,
  `skills/core/SKILL.md:128`, `skills/commit-pr-convention/SKILL.md:164`, and
  `docs/releasing/branch-and-release.md:20`;
- docstrings and comments under `.github/` and in the tests that tell their
  own history, or cite #1045, #1174 or "S12 of" another work item for
  another subject (O5);
- `assets/seals/` and `skills/verify/scripts/seal_stamp.py`, which cite
  #1174 for the seal's drawing;
- `tests/text/test_a_merged_ticket_says_so_on_the_tracker.py`, which reads
  the workflow file and no document.

`docs/layout/one-root-by-lifetime.ko.md` is the only Korean edition among
these files, and it follows its English edition above.

**Marker-probe sentences kept in these files**, 27 at cc4d9902a. With the 6
phase 1 kept and the 3 phase 2 kept, they are the 36 the probe lists at
cc4d9902a.

| File | Sentence | Keep case (D2) |
|---|---|---|
| `docs/checks/the-fold.md` | "A pull request outside a settle that removes a whole work item directory reads as a settle too; …" | no history: the regex matched "work item … wrote" across the joined check line |
| `docs/checks/the-fold.md` | "A released work item that wrote no `frame/design.md` states no rule and goes the same way." | no history: "work item that wrote" |
| `docs/checks/the-fold.md` | "Its session records `seal no-work-item` on the settle's branch, …, and what it wrote is reviewed at its pull request." | no history: "no work item … wrote" |
| `docs/checks/the-pull-request-check.md` | "Three readers outside the check still open merged records: … the one before 0.23.0, and `seal/threads/<id>/trail/rounds/` since …" | a version boundary the reader acts on: which record layouts the eval scripts read |
| `docs/checks/the-stamp.md` | "Whether a given work item's stamp was seen, and whether the orchestrator wrote its result …, are read by the person and by nobody else." | no history: "work item's stamp was seen" |
| `docs/forms/the-round-record.md` | "`rejected` means only that the finding does not hold." with the joined check line and the next bold sentence | no history: "one of its findings" |
| `docs/layout/the-pact.md` | "`seal pact` is the command that reads every signer from there." with the next bold sentence on the 0.18.x header | a version boundary the reader acts on; D2 gives the pact header as its example |
| `docs/layout/the-pact.md` | "No command rewrites a pact: the line says to rename the header …" with the next sentence on the 0.18.x word | the same keep case |
| `docs/layout/the-pact.md` | "A text that spells the 0.18.x header in order to read it, …, names no signer another way." | the same keep case |
| `docs/layout/the-pact.md` | "A `pact:` token outside a fenced code block, in any case, is the inline anchor `seal pact` read through 0.23.x, …" | a version boundary the reader acts on: frames written before the anchor table carry the token |
| `docs/layout/the-record-layout.md` | "No two rule documents may share more 15-word runs than their pair was measured at, …" | O4: 1793732301's pending `from` quotes it. It is also no history |
| `docs/releasing/branch-and-release.md` | "What GitHub does with `Closes #88, #92` is written down nowhere, …" | an example that is not history, and an observation of an outside system the act depends on |
| `docs/releasing/issues-and-milestones.md` | "So "what is in 1.2.3, and why in that order" is answered without opening a file." | an example that is not history; D2 gives `1.2.3` |
| `docs/releasing/issues-and-milestones.md` | "`#51` is the durable performance log …" | a coordinate a reader opens; D2 gives `#51` |
| `docs/releasing/issues-and-milestones.md` | "That field is spent on *when*, … `measurement` is carried by `#51`, …" | the same keep case |
| `docs/releasing/issues-and-milestones.md` | "Reading `--label flow-measurement --state all` finds the rolling logs and misses `#51`; …" | the same keep case |
| `docs/releasing/issues-and-milestones.md` | "That log opened at the 1.2.3 release, holds the measurements taken since, …" | an example that is not history: the number is illustrative, as the paragraph says |
| `docs/releasing/issues-and-milestones.md` | "A title carrying those words somewhere inside it, `docs: explain flow measurement — after 1.2.3`, …" | the same keep case |
| `docs/releasing/issues-and-milestones.md` | "It does compare the two and says which way they disagree: …" | no history: it states the gate's present behaviour |
| `docs/releasing/issues-and-milestones.md` | "**Write the keyword in front of every number**: `closes #153 and closes #150`." | an example that is not history; D2 gives it |
| `docs/releasing/issues-and-milestones.md` | "An issue that is a **log rather than a ticket**, `#51` and the rolling `flow-measurement` log, …" | a coordinate a reader opens |
| `docs/releasing/issues-and-milestones.md` | "`#51`'s own body says so at the top, …" | the same keep case |
| `docs/releasing/issues-and-milestones.md` | "A branch name is not that signal: the branch `release/v0.3.0` shipped as 0.2.0, and its own release pull request says so in its title." | borderline (Q1), kept. It is history, but it is the rule's only stated grounds (O7 keeps it), and it names a coordinate a reader opens, that release pull request's title. `tests/behaviour/test_the_contributor_has_a_procedure.py#RELEASE_BRANCH_HISTORY` allows the branch name in this sentence alone, and `tests/behaviour/test_release_hygiene.py#test_a_version_below_the_running_one_is_history_and_is_kept` takes the sentence as its case of history kept |
| `docs/releasing/release-checklist.md` | "They are this repository's measure of #1148, which removed the records' copies of one another." | a coordinate a reader opens, and a definition that names its source: the count is defined as the measure of what #1148 changed |
| `docs/releasing/release-checklist.md` | "A records-alone count that does not fall is no verdict. #1148 is measured by this count falling, …" | the same keep case |
| `docs/releasing/release-checklist.md` | "The plugin's listing is a Console listing, by the repository owner's reading of the Console page on 2026-10-07, …" | a dated observation of an outside system the act depends on; D2 gives it as its example |
| `docs/releasing/release-checklist.md` | "Every place this repository tells a user what to do after an update names the reload command, says what a reload was measured to do, …" | no history: an instruction, matched by "was measured" |

**Census passages kept in these files, with the D3 ground for each**, read
from the ten-word census at cc4d9902a. Shared wording is two files naming
one thing in the same words, and it stays. A pair whose other side is under
O1, O2 or O5 changes only its `docs/` side.

- The `docs/README.md` rows with `the-fold.md`, `the-pull-request-check.md`,
  `one-root-by-lifetime.md`, `branch-and-release.md`,
  `issues-and-milestones.md` and `the-review-and-parity-arms.md`: each row
  names the question its document answers, which D3 keeps as the index's
  own fact.
- Where the `docs/` side is the home and the other side is a skill a phase
  before this one kept: `the-routing-check.md` with
  `skills/implement/orchestration.md` (the edit gate) and with
  `skills/commit-pr-convention/SKILL.md` (the trailer, which the section
  names as "where a session reads it"); `the-stamp.md` with
  `skills/code-review/orchestration.md`; `the-round-record.md` with
  `skills/code-review/SKILL.md` and `skills/code-review/orchestration.md`;
  `the-run.md` with `skills/code-review/orchestration.md` (the regression
  route); `the-review-and-parity-arms.md` with
  `skills/implement/orchestration.md`; `measuring-a-run.md` and
  `the-broad-gate.md` with `skills/verify/orchestration.md`;
  `the-pact.md` with `skills/implement/multi-repository.md`;
  `the-agent-set.md` with `skills/implement/SKILL.md` ("the party that draws
  a contract is not the party that executes it", which the skill cites
  here) and with `skills/implement/orchestration.md` (the `Implementation`
  row's axis). This document states each rule, and the skill side is the
  act its reader takes at that step.
- `docs/checks/the-fold.md` with `skills/settle/SKILL.md` (three passages),
  `skills/settle/local-mode.md` and `skills/implement/SKILL.md`: the fold's
  opening says "This section holds the rules its readers share", so the
  `docs/` side is the home, and phase 2 kept the skill side as the
  procedure the settling session follows at each step.
- `docs/running/the-agent-set.md` with `skills/implement/SKILL.md`, "is a
  decision the orchestrator folds into the plan before the spawn": kept
  above, under what phase 2 handed this phase.
- `docs/checks/the-pull-request-check.md` with `skills/settle/rule-changes.md`
  (two check-line phrases) and with `docs/running/the-review-and-parity-arms.md`
  (a tree with no top-level `seal` entry): shared wording naming what the
  check reads, and the arms document cites this one for it.
- `docs/checks/the-pull-request-check.md` with `skills/legacy-parity/SKILL.md`:
  what a round that could not resolve the original writes. That skill's
  *Recording the comparison* is the home. It stays here because it is why
  the refusal stands until a round compares, and the person who changes the
  check does not open the parity skill at that step.
- `docs/checks/the-pull-request-check.md` and `docs/checks/the-unverified-record.md`,
  "the pull request that moves a root to local mode", and `the-fold.md` and
  `the-unverified-record.md`, "which keeps a misspelt path from passing in
  silence": shared wording. Each document states its own reader's
  behaviour in the same words.
- `docs/forms/the-round-record.md` with `docs/releasing/branch-and-release.md`,
  that the check reads a `target:` commit only while its branch is open:
  `branch-and-release.md` cites the round record for it and keeps it as the
  reason a squash breaks nothing the check needs.
- `docs/layout/the-record-layout.md` with `skills/implement/SKILL.md`: the
  rows on `frame/plan.md`'s judgments and on `gaps.md`. Each table names the
  same file's content, the layout by the question it answers and the skill
  by who writes it, and each cites the other.
- `docs/layout/one-root-by-lifetime.md` with `docs/releasing/branch-and-release.md`,
  "because the checks read committed files and local mode commits none":
  one reason, stated where each document's reader meets the refusal, at
  first setup and at the squashed branch's deletion. Neither reader opens
  the other document at that step.
- `docs/releasing/branch-and-release.md` with `skills/implement/orchestration.md`,
  "every later pull request into the branch leaves it": phase 1 kept the
  skill as the side that ships the rule. This side applies it to this
  repository's release.
- `docs/releasing/branch-and-release.md` with `docs/releasing/release-checklist.md`,
  which fragments the note reads: the checklist's box names them as what to
  check when the note is missing, the act its reader takes at that box.
- `docs/releasing/issues-and-milestones.md` with `docs/releasing/release-checklist.md`:
  the milestone the release branch does not carry, and the `merged:` labels
  a deletion would falsify. `issues-and-milestones.md` is the home. The
  checklist's step 0 and step 6 boxes keep each as the reason for the box,
  and the checklist sends its reader to `branch-and-release.md` for reasons,
  not to `issues-and-milestones.md`.
- `docs/releasing/issues-and-milestones.md` with `skills/commit-pr-convention/SKILL.md`,
  "takes the prefix the pull request that closes it will take": the bold
  rule stays with this document's own reason, which the skill does not
  give. A person filing an issue here reads this document and not the
  skill. The retitle, which only the orchestrator does, now cites the skill.
- `docs/releasing/release-checklist.md` with `skills/settle/SKILL.md`, what
  `--apply` removes: kept with the step 2b paragraph, below.
- Pairs whose other side is out of scope and so changes nothing here:
  `CONTRIBUTING.md` and `README.md` (O5), `agents/framer.md` and
  `agents/proofer.md` (O1), `templates/setup/config.md`,
  `templates/setup/pact.md` and `templates/setup/seal-README.md` (O5), and
  `skills/implement/acts.md` (O2). The `docs/` side of each is the home of
  the rule it states, or states the act its own reader takes.

**Judged and kept, with no census run and no marker hit**, at 3bd60d29f's lines.

- `docs/releasing/release-checklist.md:42-63`, step 2b's account of what
  each settle command does, restates `skills/settle/SKILL.md`, which `:65`
  names as the procedure. It stays: the person who works down the checklist
  types the commands in the block above it and reads what each does there,
  and that person does not run the skill's procedure.
- `docs/releasing/release-checklist.md:65-71`, that a settle is not a work
  item and its session runs `seal no-work-item` before the first edit,
  restates `docs/checks/the-fold.md` *The fold, and what tells it from a
  deletion*. It stays for the same reason: it is the act the person takes
  before the settle's first edit.
- `docs/checks/the-stamp.md:93-94`, "A screenshot of the probe proved once
  that such bytes render unfolded", is the evidence the claim rests on, an
  observation of an outside system (D2).
- `docs/layout/the-pact.md:127-128`, "no release read that spelling as an
  anchor", is a version boundary: it says why no frame carries that token.

**Census readings (S4, D4).** Both probes ran read-only. The probe was one
file, `test_tmp_census.py`, under the session's scratch directory,
implementing D4 as phases 1 and 2 did. It ran `python3 -I test_tmp_census.py
<clone>` over a `git clone --no-local` of the repository checked out at each
commit, and the file and both clones were deleted after the last run
(contract rule 7, executed). The scope size is `git ls-tree -r -l <commit>
-- skills docs`, summed over the `.md` files outside `docs/experiments/`,
`skills/core/SKILL.md` and `skills/agent-contract/SKILL.md` (executed).

| Reading | 3bd60d29f (base) | cc4d9902a (the last commit that changes a corpus file) |
|---|---|---|
| Scope size | 48 files, 595,984 bytes | 48 files, 589,672 bytes |
| Ten-word census: in-scope words inside a run another rule document holds | 2,078 of 88,708 | 1,799 of 87,579 |
| Ten-word census: file pairs, and the runs they share | 80 pairs, 264 runs | 74 pairs, 228 runs |
| Marker probe | 58 sentences in 22 files | 36 sentences in 15 files |

The base reading equals `frame/design.md` *Grounding*, so the probe is the
same one. 930ac879c and this record's commit change no corpus file:
`changelog.md` and this record are under `seal/`, outside
`skills/settle/scripts/passages.py#in_corpus`, and `plugin.json` is no `.md`.
So the reading at cc4d9902a is the reading at the work item's HEAD, and
`changelog.md` carries it. The probe also read 36c88cc9c (1,819 of 87,594
words, 74 pairs, 229 runs, 36 sentences in 15 files) and af569f223, the same
words. Those two readings are context, and they found the run the
twenty-eight-days removal had made.

**The scenarios this phase's row names (executed).**

- A1: `git grep -n -F` over `skills` and `docs` on "Six of 0.27.x's
  fourteen", "Its first instance, #1148's frame", "read this signal in seven
  work items" and "With gh 2.100.0" exits 1 for each, no hit.
- A5: the table above.
- A6: each of the four sentences O4 names stands whole in its file with
  whitespace collapsed (a `python3` read of each file, executed): the three
  of `docs/running/the-run.md` *The run* and the 15-word sentence of
  `docs/layout/the-record-layout.md` *The root records*. No directory under
  `seal/threads/` but this item's changed (`git diff --name-only 3bd60d29f
  HEAD -- seal/threads`, executed).
- A8: `.claude-plugin/plugin.json` reads `0.31.1`, and `changelog.md` ends
  with a `### Process changes` table whose three rows name the three
  orchestration files phase 1 changed. No other file of the way of working
  `docs/layout/the-record-layout.md` *A change to the way of working writes
  its process row in its own fragment* lists changed in this work item
  (`git diff --stat 3bd60d29f HEAD`, executed). Both are in 930ac879c, the
  commit that adds `changelog.md`. The fragment's category is `### Changed`,
  for the `refactor:` title the orchestrator chose.

**Narrow runs (executed, through `bin/test`).**

- The phase-boundary set (`skills/verify/SKILL.md` *Scope: cheap and often,
  broad and once*) was 74 modules in one command. They are every test
  module that names a changed file by its base name, listed by `git grep -l
  -F -f <names>` over `tests/`, every module that walks a corpus or a tree
  holding `docs/`, listed by `git grep -l -E` on `"docs"`, `in_corpus`,
  `passages` and `TOP_DIRS`, and `tests/behaviour/test_both_editions_carry_the_same_folds.py`
  and `tests/test_censuses.py`, which read `docs/` through a glob or a
  tracked listing that pattern does not name.
  `tests/behaviour/test_docs_line_wrap.py` and
  `tests/text/test_no_passage_is_pasted_into_a_second_file.py` are among
  them. `bin/test -q -p no:randomly <the 74>` exited 1 before the first
  commit and again at 36c88cc9c, each time on
  `test_prose_stays_within_the_wrap_limit[docs/releasing/release-checklist.md]`
  and nothing else: two paragraphs the removals shortened were rewrapped
  past 88 columns. It exited 0 with 3,610 passed and 11 skipped at af569f223,
  and again at cc4d9902a.
- After the version move, the 25 modules that read `plugin.json` or a
  changelog fragment (`git grep -l -e plugin.json -e changelog.md -- tests`,
  with `tests/test_censuses.py`) ran in one command: exit 0, 1,840 passed and
  1 skipped, on the tree 930ac879c commits.
- No unit adds behaviour, so no case was written new and no `seal mutate`
  ran (`skills/verify/SKILL.md` *The narrow command still has to be able to
  fail*, the prose row). The suite stays `unverified` until the
  orchestrator's broad gate.

**Q2: the paraphrases this phase met are a sample.** Reading each file whole
found the restatements in the removals table and the four kept above. A
restatement in other words shares no ten-word run, so no probe lists one,
and this list is the reading's. Judged against `frame/questions.md` Q2's
default.
