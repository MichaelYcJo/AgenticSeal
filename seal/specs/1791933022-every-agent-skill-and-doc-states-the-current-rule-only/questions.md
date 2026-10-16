# every agent, skill and doc states the current rule only — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. -->

**Judgments the ticket left open that the tree answered** — listed so nobody
reopens them; the grounds are in `spec.md` and `plan.md` §*Alternatives
considered*. Re-read on 2026-10-15 against #923's body as rewritten that day.

- The agent set stays five: every job needing judgment has one of them, and
  the fix pass, the broad run and the pull-request check need no sixth
  (`spec.md` §*The jobs*; alternative N).
- The record is the warden's one file, and the smith's fix pass writes two
  cells per open row. No generator, no copy, no derived field: each of the
  eleven removed fields is judged in `spec.md` §*What leaves, what stays*
  against the 19 records of 0.22.0 (alternatives B, D, E, F, O, P, Q).
- ⬜ leaves the vocabulary; a wrong sentence an agent acts on is 🟡 and a
  sentence in a record is not a finding (alternative Q).
- The `fix of a fix` stop is the warden's mark and the orchestrator's rule; the
  cap is one orchestrator rule with one number; neither is a check at the pull
  request until a run shows the need (alternatives E, F, M).
- The broad gate's one home is `broad-gate.md` on both routing answers.
- The sealer's verdict is a file in the tree, `guarantee.md`, read by the
  check; an owner's answer to `undecidable` is a line under the verdict, then
  the sealer runs again at the new HEAD (alternative I).
- The sealer pins `model: opus`; no other definition pins a model (owner,
  2026-10-15, #923 item 2).
- Every agent preloads the contract alone and opens its skill at the step; a
  case that shows the opened form falls short sends that skill back to the
  list (#923 item 4; alternative L).
- The contract numbers its rules anew; the citations outside the rewritten
  files (35 at 680142f2; part B counts them on its own tree) are rewritten in
  the same commit.
- The record lands first and the agents second, in two work items under one
  design, because the diff and the proof's baseline both ask for it
  (`plan.md` §*The split*; alternatives J, K). Overturnable at the approval
  of this plan.
- The three record documents are replaced by one; `docs/the-agent-set.md`,
  `docs/the-record-layout.md` and `docs/the-broad-gate.md` are rewritten where
  this item makes them false, and otherwise left to #941.
- (reframe after round 2) The check reads one fact per verdict row, the
  `Verdict` cell, and sorts no row into finding or non-finding by its `#`
  cell or its text: both sortings were guesses from words, each had an edge
  the next round found, and the finding-only word set caught nothing in the 36
  records round 2's probe read (`spec.md` §*What leaves*; alternative R).
  What that gave up — a 🔴 row closed `confirmed` passed the check — was
  written there with who read it instead, until the reframe after round 5
  closed it in the check (below).
- (reframe after round 2) `.test_durations`' staleness is decided by
  collection, which the durations case already reads; the fix is in the data
  (the dead entries pruned, nothing re-measured) and not in
  `release_report.py`, which sums the file as it is (alternatives S, T, U).
  No `tests` run of this branch exists to download a measured file from
  (`gh run list`, `gh pr list` on 2026-10-15: none), so the refresh that
  prices the unpriced cases waits for the pull request's first run.
- (reframe after round 4) The sealer's acts are listed once, in
  `agents/sealer.md` step 3; `docs/the-review-record.md` §*The guarantee* and
  the template point at step 3 and list no act (`spec.md` §*The sealer*;
  alternatives V, W). Round 4's paste, which extended the list in all three
  files to four acts, was the pattern that let the fourth act reach one file
  of three. The one-list design stands after round 5 with three acts.
- (reframe after round 4, narrowed after round 5) A figure in the changelog
  fragment or in a `docs/` sentence this item rewrote is a measurement naming
  its moment, a bound naming its check, or gone; a count of what the tree
  holds now is kept nowhere a reader acts on (`spec.md` §*A number in this
  frame names its moment or its bound*; alternatives X, Y, AC). The work
  item's own documents are readings at a moment — the frame's three at
  680142f2, the builder's two at the commits they name — and a figure there
  is history, not a finding. A check for it is refused: it would sort figures
  by their sentences, which `CLAUDE.md` calls a report; and no agent counts
  them against the tree.
- (reframe after round 5) A 🔴 or 🟡 row closed by a 🟢 or ❓ row's word
  fails the check at the pull request: the first cell's mark, which the
  refusal already reads to word itself, narrows the closing words to the fix
  pass's three, `fixed <commit>`, `answered` and `deferred <home>`. The
  sealer's duty to name such a row — round 3's fix, given a home in phase 5b
  and found with two shapes in round 5 — leaves with its pins, its pointers,
  Q8 and part B's fourth sealer case (`spec.md` §*What leaves*, S3, S20;
  alternatives AA, AB). The 83 🔴 and 🟡 rows of the 40 records in the tree
  at 81e8d785 all read one of the three, so no record is refused by it.
- (reframe after round 6) The round record is designed anew from its jobs,
  not patched a fifth time (owner, 2026-10-16). A finding is a `###` section
  of `## Findings` with `Severity:`, `Location:`, `Verdict:` and, where it
  applies, `Fix of a fix:` lines, its fenced fix inside it and the fix pass's
  `Answer:` line after it; a confirmation and a not-judged item are rows of
  `## Confirmations` and `## Not judged`; the probes are `## Probes`. The
  check reads one line per finding, `Verdict: <value>`, accepts four shapes,
  verifies a `fixed` commit is on the branch, and refuses by name whatever it
  cannot read — a value outside the four, emphasis, a missing or doubled
  line, a line outside `## Findings`, no `## Findings`. Severity is for
  people and the check ignores it; the emoji vocabulary leaves the record
  (`spec.md` §*What a round records*; alternatives AD–AL). The grounds for
  each rejected shape are in the Alternatives rows, and no person was asked.
- (reframe after round 6) No reader for the old shape: the check judges only
  the items the pull request's own commits declare or change, so the other
  0.22.0 items' records are read by nothing again; this item's six records
  are rewritten mechanically in phase 5d-i; the corpus test goes (alternative
  AJ); the old generator's words leave the accepted set (AK); the release
  seal and the panel report a record they cannot read as *not read*.
  `guarantee.md`'s `Verdict:` reader is left as it stands (AM).
- (reframe after round 6) The redesign is two spawns, 5d-i and 5d-ii, split
  where the tree has to be green between them: the reader, the template, the
  six records and every test and document `bin/test` and `rules --check`
  read in the first; the parties' instructions, the eval graders and the
  builder's documents in the second. One spawn hit 800K tokens once on a
  single phase in this run.
- (frame edit of 2026-10-16, after 5d-i) The owner's six decisions are
  written into `spec.md` §*What a round records* in place, and what each
  left open the tree answered: a `location:` holds one or more backticked
  coordinates joined by `, `, and a `fixed` commit must touch at least one
  path named, since the fact closed is an unrelated commit and completeness
  is the verifying round's reading (alternative AN); a fix that lives where
  the warden did not point is named on the same line — the warden names the
  path its paste goes to beside where the defect shows, and the fix pass
  appends the coordinate of a fix that went elsewhere again (AV); the reference is
  `round-<N>#<n>`, one token, the record's number and the finding's heading
  number, with `round-<N>` for a fix pass no finding named (AO); it stands in
  a `Confirms` first column of `## Confirmations` and on a `refixes:` line
  whose value is the reference alone (AP, AS); a label in another spelling is
  refused by line, never skipped (AR); a `fixed` or `answered` finding in the
  last record owes a verifying round, as the rule in words already said (AT);
  the check reads no emoji, since it decides on lines and cells an emoji
  cannot reach, and a test and the shape grader hold the shipped text to
  words (AQ); `guarantee.md` keeps its `Verdict:`, the sealer's file with a
  reader of its own (AM). The six records are given the references their
  prose states, and one line changes its fact: round 1's finding 5, whose
  `fixed 1b875efc` touched `.test_durations` and not the
  `release_report.py` lines it named, gains that path, which its own
  grounds, paste and answer name (AU). Round 1 owes nothing; the eight other
  `fixed` commits touch their path (`git diff-tree`, `executed`). 5d-ii
  splits into 5d-ii and 5d-iii, the check and the record first, the parties
  and the graders second, each ending green.
- Answered by the owner before this frame and still standing: the proof's run
  budget (≈ 120 runs, ≈ $150; 2026-10-14), the tree's
  `skills/writing-style/SKILL.md` as the one source (2026-10-13), no
  restatement report row (2026-10-15), `docs/one-root-by-lifetime.md` rewritten
  in #941 (2026-10-14).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | How many finding rounds may a run take before it stops and every open finding is deferred with a home? 0.22.0's runs: #944 two finding rounds then a verifying one, #930 two then one, #931 five then one, #929 six then one and the item was closed unfinished. The number is a cost a person is accountable for, and the tree holds no measurement that picks one | a person — the owner, who pays for the rounds | **3**: a run of #931's shape stops after its third finding round and defers the rest · **5**: #931 completes, #929 stops one round earlier than it did · **no cap**: the sealer and the person reading the pull request are the only bound | 3 | ✅ the owner answered on 2026-10-15: **3 by default, and variable with the run.** Past round 3 the orchestrator extends one round at a time while the latest round found fewer findings than the one before and none is a fix of a fix; a fix of a fix stops the fix passes before round 3 as well, and the item goes back to its framer. Each extension is one line in that round's record with its reason, and the sealer reads it. No person is asked mid-run |
| Q2 | What does one guarantor run cost — spend, seconds, tokens — on a real item? | a measurement — phase 4's first run of the three sealer cases, and part A's own sealer spawn | — | the estimate in `spec.md` §*The sealer*: ≈ $2–4, 5–10 min | ⬜ |
| Q3 | Which of the 70 test modules naming the three scripts keep a case in `test_chain_check.py` or `test_broad_gate.py`, and which leave whole? | the work — phase 3 sorts them as it rebuilds the arms and lists every deletion's guard in `phases/phase-3.md` | — | — | ✅ answered by the work in `phases/phase-3.md`: 28 modules left whole, two came back without the guard's cases, and the cases removed from kept modules are named there |
| Q4 | What are the real tokens a spawn reads after the rewrites, per agent? | a measurement — part B's baseline traces carry `usage`; `compare` writes both sides' pooled tokens | — | `payload_meter`'s estimate at 3.2 B/token, labelled estimated | ⬜ |
| Q5 | Of the pins the 52 test modules hold on `agents/*.md`, which pin a rule and which pin narration? | the work — each part B phase sorts its agent's and lists the dropped ones in its phase record and `overview.md` | — | — | ⬜ |
| Q6 | Which fields of the eval's per-run JSON and of the trace's `result` event carry a run's spend, seconds and tokens, on a real run? | a measurement — the first saved `raw.json` of part B's baseline, read against what `run` records (`total_cost_usd`, `duration_ms`, `usage.*`) | — | the names above | ⬜ |
| Q9 | Does the sentence **"a gate fails closed: input it cannot read is refused, never passed"** go into `CLAUDE.md` §*The rule a mechanism is kept against*? The round record's new shape embodies it (`spec.md` §*What a round records*): the check reads one `Verdict:` line per finding and refuses every spelling outside four. `CLAUDE.md` already says *a check gates only a fact it reads; a noisy reading, or one guessed from words, is a report*, which says what a gate may read and not which way an unreadable input falls, and the four misses of this run (rounds 1, 2, 5, 6) each fell to the passing side. Writing it into `CLAUDE.md` makes it a rule every check in the tree is judged against, and `chain_check.py#verdicts_of` (the guarantee's `Verdict:` line, read through emphasis) and `unverified_check.py`'s tolerant readings would be the first to meet it. The tree cannot answer whether a repository-wide rule is wanted; that is the owner's | a person — the owner | **not in `CLAUDE.md` in this item**: the record design embodies the rule, `docs/the-review-record.md` states it for the record, and a later item folds it over the tree's other readers if the owner wants the rule general · **into `CLAUDE.md`**, one sentence in §*The rule a mechanism is kept against*, in a commit of its own, with the readers that then fall short named in an issue | not in `CLAUDE.md` in this item; the record design embodies it. `CLAUDE.md` is not edited by phase 5d | ⬜ |
| Q10 | **Do the quotations of the old marks in this item's six round records stay?** The records hold 395 emoji characters (51, 105, 82, 55, 24, 78 at 614e4d66). 5d-ii respells every reference `round N's 🟡 k` as `round-N#k` and removes every mark from a label line; what remains is quotation — round 6's finding is about `**🔴 1** … confirmed` passing the check, round 2's confirmations say which `🟢` rows closed — and the check reads none of it (`spec.md` §*What a round records*; alternative AQ). The owner's decision says *no emoji anywhere in the record*, and whether a record of a moment is reworded to meet a rule it predates is a product choice the tree cannot make | a person — the owner | **stay**: the six records keep their quotations; the template, the format and the definitions carry none, T39 and the shape grader hold them to it, and every record from round 7 on is words only · **reword**: the 5d-ii script maps each remaining mark to a word (`🔴` → *must*, `🟡` → *should*, `🟢` → *a confirmation*, `❓` → *not judged*, `⬜` → *a note*) and the check refuses an emoji outside a fence or a comment, which is one more fact in `record_findings` and one more case | stay | ⬜ |
| Q7 | How does a pull request into `main` read a work item that was squashed into the release branch? The check judges every `routing.md` a pull request adds, and a squashed item's last `Target SHA`, `broad-gate.md` run and `guarantee.md` commit are not ancestors of the release branch's HEAD, so the records, broad-gate and guarantee arms refuse each one (`executed` at cba5e0cd on this branch, `chain_check.py --baseline origin/main` with `GITHUB_HEAD_REF=release/v0.22.0`: four squashed 0.22.0 items each named *which HEAD does not descend from*, and none of the four carrying a `broad-gate.md`). `skills/settle/SKILL.md` says those records are still read at the release pull request | a person — the owner, who decides what a release pull request re-proves | **judge at the item's own pull request only**: the release pull request judges the declarations naming its own branch and the ones its own commits changed, never an item merged by squash · **resolve the commit elsewhere**: what the removed pull-head fetch did, and a branch deleted or squashed is again a reason to fail · **the release pull request reads the release's own guarantee**: the release seal is one guarantee over the release, and the items' files are history | the first — an item is proved at the pull request that carries it | ✅ answered by default, by the orchestrator under automation on 2026-10-15, for the owner to confirm: an item is judged at the pull request that carries it. Built in phase 5 at 27dd748d: a declaration every commit after the base touched as a GitHub squash merge (committer `noreply@github.com`, subject ending `(#N)`) is named and not judged (`chain_check.py#carried_by`, `docs/the-review-record.md` §*What the check reads at the pull request*). Probed on a scratch squash of this branch into `release/v0.22.0`: the check at af4d0c31 exits 1 naming all five items, the new one exits 0 naming each with its squash, and a commit made on the release branch itself that changes this item's `routing.md` is judged and exits 1 (`phases/phase-5.md`). Overturning it is a change to `carried_by` and its four cases |

Q8 (reframe after round 4) asked the owner whether a behaviour eval of the
sealer's step-3 duty was owed in part A or part B. The reframe after round 5
removed the duty, so the row is gone: the rule is the check's and its proof is
`tests/test_chain_check.py` (alternatives Z, AA). Nothing was asked of anyone.

No row blocks the build. Q7's default is built and stands until the owner
confirms or overturns it. Q9's default continues the build without touching
`CLAUDE.md`, and either answer leaves phase 5d's code the same, so it waits
for the owner without stopping anything. Q10's default continues 5d-ii with
the quotations left in place; *reword* is one more mapping in the same
script and one more check fact, and can follow in a later commit of this
item without undoing anything. Q2, Q4 and Q6 are a measurement's; Q5 is the
work's, in part B.
