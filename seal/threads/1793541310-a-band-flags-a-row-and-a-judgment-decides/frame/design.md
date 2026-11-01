# Design: a band flags a measured row, and a judgment of what the change buys decides it (#1263)

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| G1 Issue #1263, body and comments (executed: `gh issue view 1263 --json body,comments`, 2026-11-01; created 12:57:21Z, milestone `release: 0.27.3`) | The request is the body as folded. The issue has no comments. *Done when* asks for two things: a rule homed in `docs/measuring-a-run.md` and `docs/release-checklist.md` *5. The release pull request*, written through `## Rule changes`, with every other sentence that turns a moved number into an issue directly rewritten in place; and #51's section *The process at 0.27.2, against 0.21.x* reading its two band-only `worse` rows as judged |
| G2 `docs/release-checklist.md` *5. The release pull request*, the paragraph that opens **Read the release table before the merge.**, lines 126 to 133 at `cd694aa3` (read) | The one sentence in the policy root that turns a moved number into an issue with no weighing named: "A preload or a document that grew is a question the pull request's body answers, or an issue it opens." The paragraph carries no `check:` line of its own. It came in with `8350c578` (#959, for #923) (executed: `git log -S 'A preload or a document that grew'`) |
| G3 The pending change to the same section, `seal/threads/1793538228-the-release-pr-opens-after-the-last-merge/frame/design.md` *Rule changes* (read), and the policy in force (executed: `grep -n -E 'file: docs/(release-checklist\|measuring-a-run\|README)\.md'` over the three `seal/threads/*/frame/design.md` at `8a46ee09`) | #1258's `change` is the only pending operation on any file this work names. Its `from` and `to` cover the section's first paragraph, the one that opens **The orchestrator opens the release pull request**, and nothing after it. The paragraph this work changes stands unchanged by #1258, so its text at the base is its text at the moment this change applies, after #1258's in merge order (`skills/settle/SKILL.md` *What the dry run shows*: a group's operations are read in merge order). The two operations name one place, so the settle reads them as one group, and neither restates the other, so neither is superseded |
| G4 `docs/measuring-a-run.md`, read whole at `cd694aa3` | No sentence says how a reading compared with an earlier one is read, what a band decides, or when an issue follows a reading. Its opening says the document is about "what the measurement is read against". Its section *What a measurement must survive, and what it must not invent* holds the rules on what a measurement may not claim, a percentage for a span of zero among them. A verdict from a band alone is a claim of the same kind, so the new rule is an `add` to that section. The section has no sub-heading, so the `add` lands at its end |
| G5 The class: every sentence that turns a moved number into an issue or a verdict directly (executed: contract rule 12's first method, from what produces the defect, and a wording search as a sample) | **Producers.** A number compared with an earlier one is produced in this plugin by: `.github/scripts/release_report.py` (the release table); `skills/verify/scripts/session_cost.py` (segment readings, the per-segment bars, the run-level table); `skills/verify/scripts/payload_meter.py` (preloads, read by the release table and the eval suite); `evals/scripts/noninferiority.py` (a rewrite's side against its baseline); `.test_durations` (the release table's test-file rows); and a work item that measures the process, as #947's did, whose band lived in its own frame (G6). The readers of each were listed with `git grep -l -E 'payload_meter\|Document token ceiling\|test_durations\|session_cost\|release_report\|noninferiority'` over `docs`, `skills`, `agents`, `templates`, `CONTRIBUTING.md`, `README.md`, `evals/README.md` and `.github/workflows`, and every hit was read at the sentence. **Wording sample.** `git grep -n -i -E` for `grew`, `worse`, `band`, `issue it opens`, `opens an issue`, `issue of its own`, `gets an issue`, `files an issue`, `filed as`, `gh issue create` and `an issue follows` over `skills`, `agents`, `docs`, `templates`, `hooks`, `.github`, `bin`, `evals`, `CONTRIBUTING.md`, `README.md`, `README.ko.md` and `CLAUDE.md`, and `git grep` for `늘어`, `나빠`, `악화` and `커진` over the Korean editions. **Result.** G2's sentence is the one instance. Every other reader already reads a moved number as no verdict: G9's three, and the readers G10 places outside the class. The wording search is a sample over spellings; the producer list is whole for the scripts this tree ships, and its open part is a measurement a future work item adds with its own band, which the new rule governs |
| G6 #947's frame, `seal/threads/1793528484-the-process-measured-on-0-27-2/frame/design.md` at `v0.27.2` (executed: `git show v0.27.2:<path>`; the directory is not in the tree at `cd694aa3`, so the settle after 0.27.2 removed it) | *Scope* item 11 set the bands, `same` within 1 per cent for a measure read off the tree and within 20 per cent for one read off runs. S4 owed an issue draft for every `worse` row. Its `## Rule changes` was the no-change block, so neither the band nor S4 reached the policy root. They are history at a tag, and this work rewrites nothing there |
| G7 #51's section *The process at 0.27.2, against 0.21.x* (executed: `gh issue view 51 --json body`; `gh api graphql` on the issue's `userContentEdits`) | The owner edited #51 at 2026-11-01T12:57:59Z, 38 seconds after filing #1263. The version before that edit read the two rows `worse, +4.3 %` and `worse; one Read of skills/implement/SKILL.md`, and its closing sentence said "Each `worse` row has an issue: #1259 and #1260." The version now reads both as "past the band; judged not worse on 2026-11-01", each with its grounds, and closes "judged, neither is worse, and how a band became a verdict is #1263." *Done when*'s second item stands in #51 already. No agent posts or edits an issue (contract rule 6), so the build owes it nothing |
| G8 #1259 and #1260 (executed: `gh issue view`) | #1259 closed `NOT_PLANNED` at 12:57:30Z. #1260 is open and asks whether a crafter spawn can open the part of `skills/implement/SKILL.md` its step needs. That is a question of whether something serves, not a band's verdict, so it stays as it is |
| G9 The readers already in line with the rule (read) | `skills/verify/orchestration.md` *Measure the segment, and feed the flow log*: `seal cost` "refuses without `--says`: what the numbers mean is the orchestrator's sentence to write", and "The table carries no verdict." `docs/the-review-record.md` *The per-segment bars*: "the bar is a lens for rounds of ordinary size, never a refusal threshold". `.github/scripts/release_report.py#HEADER`: "no row is a verdict". None of the three files an issue from a number, so none changes |
| G10 Readers weighed and placed outside the class (read) | `docs/release-checklist.md` *5*, **Each release clears what grew.**: growth picks the modules the owner sweeps, and `bin/seal mutate` decides each cut. No verdict and no issue follows the growth. `evals/README.md` *The behaviour suite*: `noninferiority.py#verdict`'s fourth rule fails a side whose preload is not smaller than the baseline's. It is the criterion a preload rewrite states for its own claim, chosen before the run, and it files nothing ("Nothing in the tree makes a later edit owe a run"). `CONTRIBUTING.md`'s 60-second threshold for writing a module's tests anew, `Document token ceiling` (`skills/config/SKILL.md`) and the paste check's stored count in `docs/the-record-layout.md` *The root records*: each holds an absolute bound, or a script's exact count, and compares no reading with an earlier one under a band. `docs/the-review-record.md` *The per-segment bars* says "the run-level table judges a run against the last run measured", and `skills/verify/orchestration.md` says the same table "carries no verdict". The wording differs, and the effect is the same: the table files nothing. That wording is left as it stands |
| G11 The new `check:` line for *5*'s paragraph (read: `tests/github/test_release_report.py#Test_main::test_the_release_table_reads_two_trees_and_fails_nothing`; `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py`, docstring and its one case) | The first reads that the script prints the table and exits 0 whatever the table shows. The second reads that the `release-report` job runs after the suite, on a pull request into `main` alone, and appends to the job's summary. Together they read what the paragraph states as fact: where the table is and that it fails nothing. No rule cites either module today (executed: `git grep -n` of both names over `docs`, `CONTRIBUTING.md`, `skills` and `.github`) |
| G12 `docs/README.md` *The checks* (read) | The index row for `docs/measuring-a-run.md` reads "what a segment of a run measures, and where the reading goes". A framer picks each `file:` from the index (`skills/settle/SKILL.md` *The index*). Once the rule lands, the document also answers how a reading that moved is judged, and the row says so |
| G13 `skills/core/SKILL.md` *The first value: efficient development through the workflow* (read) | "Whether two things mean the same or give the same result is the judgment the workflow delegates", and "A script that answers 'these differ' where the meaning is the same is the worst result the workflow can give". A band is a script-shaped answer to a question of meaning, which is the grounds of the new rule |
| G14 The policy root's `check:` grammar and the wrap of `docs/` (read: `skills/settle/SKILL.md` *A rule has one shape*; `tests/behaviour/test_docs_line_wrap.py`, `LIMIT = 88`, check lines skipped) | Each `to` that states a rule opens with one bold sentence and ends with one `check:` line, with no comma, `::` or em dash in its value. Each prose line of a `to` stays within 76 columns |
| G15 The rule changes read as the settle will read them (executed: `test_tmp_rule_changes.py` under `<scratchpad>/1793541310-a-band-flags-a-row-and-a-judgment-decides/frame/`, against a `git clone --no-local` of the worktree at `8a46ee09` with this design copied in; the directory removed after) | `skills/settle/scripts/rule_changes.py#parse` reads three operations and no error and no unread line. `#section_lines` finds each named section once. `#pattern` finds each `from` in its section. Each `to`'s longest prose line is at most 76 columns. Recorded in `plan.md` *Technical context* |
| G16 `seal/follow-up.md` and the latest Release's `### Process changes` (executed: `gh release view --json body`; read: the follow-up rows) | No follow-up row is about a measurement or the release table. v0.27.2's one process change, #1222's wait on a pull request's checks, is unrelated |

## Scope

In:

1. `docs/measuring-a-run.md` *What a measurement must survive, and what it must not invent* gains the rule that a band flags a reading for judgment and a judgment decides whether it is `worse`. The rule names who writes the weighing and who files the issue that may follow. It is written as the `add` in *Rule changes*.
2. `docs/release-checklist.md` *5. The release pull request*: the paragraph **Read the release table before the merge.** no longer opens an issue for a preload or a document that grew. It treats growth as a row for item 1's judgment, which the orchestrator writes in the pull request's body, and it cites item 1's rule rather than restating it. It gains the `check:` line G11 names. It is written as a `change` in *Rule changes*, stacked after #1258's change to the same section (G3).
3. `docs/README.md` *The checks*: the row for `docs/measuring-a-run.md` names the new question its document answers (G12). It is written as a `change` in *Rule changes*.
4. The work item's `changelog.md`: one entry, and one `### Process changes` row in the shape of `templates/records/process.md`, because the way a moved number becomes an issue changes.
5. No other file in the tree changes, because no other sentence turns a moved number into an issue directly (G5, G9, G10).

Out:

- #51's section *The process at 0.27.2, against 0.21.x*. The owner rewrote both rows on 2026-11-01 (G7). An agent posts nothing (contract rule 6).
- #1260. It asks whether a part of a skill serves, which is not a band's verdict (G8).
- #947's frame at `v0.27.2`. It is history at a tag (G6).
- The wording "the run-level table judges a run" in `docs/the-review-record.md` *The per-segment bars*. It files nothing, and its effect already matches the rule (G10).
- `evals/README.md`'s fourth pass rule, `CONTRIBUTING.md`'s 60-second threshold, `Document token ceiling` and the paste check's count. Each is an absolute bound or a criterion chosen for one claim, not a reading under a band (G10).
- `.github/scripts/release_report.py`. Its header already says no row is a verdict (G9).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A process reading moves past its band | Given a measuring work item's reading that moved past its band toward more cost, when the crafter writes it into a phase record, then the weighing stands beside it: the change that moved it, what that change cost, what it bought, and the record each stands in. The reading is `worse` only where the cost outweighs what was bought | No case can read a judgment (`skills/core/SKILL.md` *The first value*). The reader is the proofer at review of that work item, as the new rule's `check:` line names |
| S2 A reading is judged `worse` | Given S1's weighing reads `worse`, when the orchestrator reads the phase record, then it files one issue for that reading. A reading whose only ground is its band gets none | The same reader. The case that set this work off is #1259: under the rule it is not filed, because the weighing reads the 397 B against one source for the core |
| S3 The release table shows a grown document | Given the release pull request's `release-report` summary shows a preload or a document larger than at the last tag, when the orchestrator writes the release pull request's body, then the body weighs that row as S1 says, and an issue follows only a row judged `worse` | The owner reads the body before the merge, as *5* already has the table read. The table's own facts stay pinned by G11's two modules |
| S4 The rule changes read at the pull request and at the settle | Given this design, when `skills/settle/scripts/rule_changes.py` parses its `## Rule changes`, then it yields one `add` and two `change` operations and no refusal, and each `from` stands in its section at the base with whitespace collapsed | Executed at framing (G15). `chain-check` at the pull request, and the settle's dry run |

## Data & interfaces

None. No schema, script, workflow or test changes. The new `check:` line names two test modules that already exist (G11).

## Rule changes

- add
  file: docs/measuring-a-run.md
  section: What a measurement must survive, and what it must not invent
  to: **A band flags a reading for judgment, and a judgment decides whether
    it is worse.** A band is how far a reading may move from the reading it
    is compared with and still read as the same. A reading past its band
    has moved past the noise its measure carries, and the band says nothing
    more: it cannot say whether what the change cost outweighs what the
    change bought. A reading past its band toward more cost is therefore
    weighed, and the weighing is written beside the reading: the change
    that moved it, what that change cost, what it bought, and the record
    each stands in. The reading is `worse` only where the cost outweighs
    what was bought. The party that writes the reading writes the weighing:
    the orchestrator in the sentence its `--says` carries or in a release
    pull request's body, and the crafter in the phase record of a work item
    that measures the process. The orchestrator files an issue for a
    reading judged `worse` so, and for none whose only ground is its band.
    A band read as a verdict filed #1259, for a session start that grew by
    397 B because the core now reaches every session from one source, and
    the owner closed it as not a defect. An issue a band files costs its
    reader a reading and a close, and the count of `worse` readings then
    says less than it seems to.
    check: none reader: the proofer at review
- change
  file: docs/release-checklist.md
  section: 5. The release pull request
  from: **Read the release table before the merge.** The pull request's `tests` run
    carries it in the `release-report` job's summary, under *Against vA.B.C*:
    each agent's preload bytes, the suite's seconds, each leg's minutes and each
    document's bytes, beside the same reading at the last release tag, and under
    it each test file's priced cases and seconds at the tag and now. It fails
    nothing. A preload or a document that grew is a question the pull request's
    body answers, or an issue it opens. A leg's minutes compare one run with one
    run and swing on the same code, so they are read and never acted on alone.
  to: **Read the release table before the merge.** The pull request's
    `tests` run carries it in the `release-report` job's summary, under
    *Against vA.B.C*: each agent's preload bytes, the suite's seconds,
    each leg's minutes and each document's bytes, beside the same reading
    at the last release tag, and under it each test file's priced cases
    and seconds at the tag and now. It fails nothing, and no row of it is
    a verdict. The table has no band, so a preload or a document that grew
    is a row for the judgment `docs/measuring-a-run.md` *A band flags a
    reading for judgment, and a judgment decides whether it is worse*
    asks. The orchestrator writes that weighing in the pull request's
    body, and opens an issue only for a row the weighing judges `worse`. A
    leg's minutes compare one run with one run and swing on the same code,
    so they are read and never acted on alone.
    check: tests/github/test_release_report.py tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py
- change
  file: docs/README.md
  section: The checks
  from: | `docs/measuring-a-run.md` | what a segment of a run measures, and where the reading goes |
  to: | `docs/measuring-a-run.md` | what a segment of a run measures, how a reading that moved is judged, and where the reading goes |

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The sentence that makes a grown preload or document "a question the pull request's body answers, or an issue it opens" | `docs/release-checklist.md` *5. The release pull request* | Replaced by the `change` above. The weighing's rule lands in `docs/measuring-a-run.md` *What a measurement must survive, and what it must not invent*, and *5* cites it |
| Outside the tree: an issue filed from a band alone, and the reading and close it costs the owner. #1259 is the instance, closed `NOT_PLANNED` (G8) | the measurement's and the release table's readers | The cause goes: a band no longer reads as a verdict, so no issue follows one. This design adds a rule, a mechanism under `skills/core/SKILL.md` *The rule a mechanism is kept against*, and what it takes out in return is the sentence above and the issues a band files. Its catch record is #1259, filed by a band and closed as not a defect, and #51's two rows that the owner rewrote from `worse` to judged (G7). The new `check:` line on *5*'s paragraph adds no test: it names two modules that already read what the paragraph states (G11) |

Framed 2026-11-01 by framer, before the build.
