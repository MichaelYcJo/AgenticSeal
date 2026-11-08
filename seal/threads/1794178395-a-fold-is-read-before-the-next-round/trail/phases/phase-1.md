# Phase 1: 1794178395-a-fold-is-read-before-the-next-round

## What this phase found

**The frame holds for this phase.** `8bdc8149` differs from `7056ee61`,
the commit the frame read, only by the three frame files (executed: `git
diff --stat 7056ee61 8bdc8149`). Every coordinate the phase row reaches
stood where the frame placed it: `skills/implement/orchestration.md:49-81`,
`:93-100` and `:389-392`, `skills/implement/SKILL.md:309-311`,
`agents/framer.md:240-247`,
`tests/text/test_the_rules_have_one_owner.py#test_a_decision_after_the_frame_is_folded_into_it`
at `:374-402` and rule 16 of `RULES` at `:122-126` (read). The three
`## Rule changes` operations name sentences that stand at
`docs/running/the-agent-set.md:66-69` and `:101-103` and at
`docs/running/the-run.md:65-67` (read). Issue #1442 has no comments
(executed: `gh issue view 1442 --json body,comments`, 2026-11-09).

**Decision: the orchestrator corrects its *Judgments of the run* row
before the fold commit, where the framer's hand-back names a defect in
it.** *Scope* item 5 has the framer name a defect in that row, and *Scope*
item 1 lists no receiver for the defect. The orchestrator writes the row,
and the framer writes no row, so the correction is the orchestrator's,
made before it commits the framer's changes and the row together. Judged
against `skills/implement/SKILL.md` *3. The SDD file set*, whose `Written
by` cell for `frame/plan.md` gives the rows of `## Judgments of the run`
to the orchestrator.

**Decision: the sentence "After the fold commit, the orchestrator reads
that commit" stays as written, and the paragraph scopes it.** The case
pins that sentence, and *Scope* item 1 keeps it for the statements a
crafter names. The sentence before it now says that the orchestrator folds
such a statement in a commit of its own, so "the fold commit" names that
commit. The same sentence ends "a decision's fold is read by the framer
that writes it". The framer's commit is called "one commit" and never "the
fold commit". Judged against `frame/design.md` *Removes*, row 2.

**Decision: the case pins five clauses beyond the three that *Scope* item 6
names.** The three named clauses are the framer folds the decision, the
row written before the framer reads `plan.md`, and the framer resumed or
spawned fresh. The five added clauses are what a decision is, the one
message with grounds and coordinates, the fresh spawn's inputs as their
own clause, the crafter-named statement folded with no framer spawned,
and the framer's hand-back feeding the fix pass. Each is a sentence that
*Scope* item 1 adds, and each was seen red alone (below). Judged against
`skills/implement/SKILL.md` *2. Implement test-first, and let each rule
name its test*.

**Decision: the prevention-home paragraph cites the fold paragraph by its
bold lead, with no path.** Both paragraphs stand in
`skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket*. The paragraph cites the fold paragraph by its bold lead, in
italics, as the sentence that opens it. Judged against
`skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만
읽히게 쓴다*, which cites by words and not by position.

**Seen red.** Both cases were run against `8bdc8149` before the prose
changed. `test_a_decision_after_the_frame_is_folded_into_it` failed on
"A decision is anything that changes what the frame says the work is or
why". `test_the_framer_folds_a_decision_it_is_sent` failed at
`text.index(lead)` with `ValueError: substring not found` (executed). After
the build was committed, each new clause was deleted alone by `seal
mutate`, run with `-x -p no:xdist -k <its case>`, and each mutant read
`red`, failing on its own pin's assertion message (executed). The
framer's fold half had 12 mutants: the bold lead put back to "The one
route back is the review chain's.", which failed at `text.index(lead)`,
and one deletion for each of its 11 pinned clauses. The order paragraph
had 8 mutants, one for each new clause of the case: the definition of a
decision, the framer's authorship, the one message, the resumed framer,
the fresh framer's inputs, the uncommitted row, the crafter-named
statement, and the framer's hand-back. The working tree was clean after
every run (executed: `git status --short`).

**The phase-boundary run passed.** One `bin/test` command ran 49
modules: the phase row's module, and each module that names, globs or
lists through `git ls-files` a path the phase changed. Modules whose only
match was a temporary fixture path were left out. It exited 0, with 1573
passed and 7 skipped (executed).

**No unit was renamed or moved,** so no census is owed. The removals
match `frame/design.md` `## Removes` row by row, and the phase removed
nothing the frame did not name.

**The policy root keeps three sentences that HEAD now contradicts, until
the settle.** `docs/running/the-agent-set.md` *One contract every agent
receives, and one definition each* and *What each party writes, and when*,
and `docs/running/the-run.md` *The run*, still say that the orchestrator
folds. They are the `from:` texts of `frame/design.md` `## Rule changes`,
and the settle writes them, because this work item's subject is the
skills and agent definitions and not the policy root (`frame/design.md`
G11; `skills/implement/SKILL.md` *Document layout — two roots, three
lifetimes*).
