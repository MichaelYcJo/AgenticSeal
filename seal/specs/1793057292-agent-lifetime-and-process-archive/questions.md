# Questions for the planner: #945 an agent lives one phase, the orchestrator's steps sit where it acts, two re-checks leave, and each release records how the process changed

## Answered by the tree

The ticket left these open, or stated them against a tree that has since
moved, and the tree answers them. Each names where the answer was read, so a
reviewer can overturn it by opening the same place.

1. **A1 Who writes the orchestrator rules.** This item does. The ticket's
   body says #940 writes them, and #940's frame took its Q2 default (b),
   leaving them to this frame (`seal/specs/1792540458-on-demand-files-state-the-current-rule/questions.md`
   Q2, `read`). #940 closed on 2026-10-24 and the fix-pass section still
   states the old rule (`skills/code-review/orchestration.md` lines 17 to
   30, `read`).
2. **A2 The orchestrator's re-run of each hand-back is deleted.** Its one
   recorded catch, #929's census defect, is a class each module's test file
   now closes (`tests/conftest.py#census_case`; #949 closed into #942,
   `executed`). `plan.md` rows H-A to H-C.
3. **A3 The unverified record loses its CI step and its broad-gate arm, and
   keeps its reader, its command and `--baseline`.** The step failed in none
   of 142 failed hygiene runs from 2026-09-23 to 2026-10-25 (`executed`).
   The ticket's figure of 262 open rows is from #944's audit; the tree now
   holds 63 open and 117 closed rows over 47 overviews (`executed`,
   `unverified-check seal/specs/`). `plan.md` rows U-A to U-D.
4. **A4 Round-record inheritance needs nothing here.** #923 took out the
   round reports and the inherited-coordinates section (`spec.md`
   *Grounding*, the #923 row).
5. **A5 The archive has no size check.** The ticket names a row of a
   release report #923 builds, and an earlier comment names
   `seal/budgets.md`. Neither exists, nor ever did (`executed`). `plan.md`
   row P-C.
6. **A6 Every framer reads the latest archive file, once.** No fact in the
   tree tells a framer it is the first of a release. `plan.md` rows F-A and
   F-B.
7. **A7 The base the archive records** is `CLAUDE.md`, `agents/*.md` and
   `skills/*/orchestration.md`, which takes in `skills/verify/orchestration.md`
   that #940 split out (`executed`, `git show --stat 5aed51cb`).
8. **A8 No paid behaviour run for the framer's line.** `evals/README.md`
   *The behaviour suite* binds a rewrite of a preload, and says nothing in
   the tree makes a later edit owe a run (`read`). One added line is not a
   rewrite.
9. **A9 The ticket's out-of-scope items are closed**: #943, #944 and #949
   (`executed`, `gh issue view`). The ticket's *Order* section, frame this
   before #940's smith reaches its orchestration phases, is moot.

## Rows

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Are archive files written for 0.22.0 to 0.22.3? The ticket says the first file, `seal/process/0.22.0.md`, is written at 0.22.0's release preparation, and that moment has passed: `v0.22.0` to `v0.22.3` are tagged (`executed`, `git tag`). Whether the process history of four shipped releases is worth a phase is a value the owner holds, and nothing in the tree weighs it | a person | (a) none: the first file is the one written at the preparation of the release that ships this item, and the changelog files keep what 0.22.0 to 0.22.3 shipped; (b) phase 4 writes `seal/process/0.22.0.md` to `0.22.3.md` from those milestones' issue comments, one more phase of reading; (c) the first file opens with rows for 0.22.0 to 0.22.3, which breaks the one-file-per-release shape | (a) | open |
| Q2 | The ticket asks that a rebase after review closes is followed by a verifying round on the rebased tip. Policy forbids it: `docs/release-checklist.md` *0. Before starting* says never rebase a work item's branch, for any reason, and policy outranks the ticket (`skills/implement/SKILL.md` *1. Read the spec before the code*). A ticket asking for what policy forbids is a person's question | a person | (a) policy holds: a conflict is integrated by merging the base, once, after the branch it conflicts with has landed, and a merge that resolved a conflict outside the work item's records gets a verifying round on that resolution; no round target is orphaned, and the chain check already refuses one that is; (b) the ticket's rule: this spec adds a `## Rule changes` item removing the never-rebase sentence, the orchestration file permits a rebase after review, and each one is followed by a verifying round on the rebased tip and a re-read of `plan.md`'s Status column | (a) | open |
| Q3 | What is the context threshold below which a fix pass resumes the implementer? The ticket gives 941,799 tokens for the resumed smith and 165k to 461k for fresh spawns, from the owner's comment of 2026-10-14; no tool in the tree measured either, because the column does not exist yet (`executed`) | a measurement | (a) phase 1 reads the 0.22.0 run's transcripts that remain with the new column, and phase 2 writes the largest context a fresh smith reached there; (b) where the transcripts holding those segments are gone, phase 2 writes 461,000 with the comment as its source, labelled `read` | (a), falling back to (b) | open |
