# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — overview

<!-- The closing memo (implement skill, step 4). Written at phase 5 from what
the phase records and the round records wrote when each call was made. Only
what the diff cannot show goes here. -->

## Why this work exists

The stamp a person sees now means the sealer verified the work item: it is
drawn once, at the commit of a `guarantee.md` reading `sealed`, and the broad
gate's run prints `BROAD GATE PASSED` or `BROAD GATE FAILED` and draws nothing.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The ASCII marks on a UTF-8 pipe (phase 1) | `spec.md` S3: "the same bytes on a terminal and a pipe, the letter twin's ASCII marks on a console that is not UTF-8"; `plan.md` row 1: "the twin's ASCII where `pick_shape` says so", and `pick_shape` answers True for every pipe | the spec's reading: the ASCII choice asks only the encoding, through `seal_stamp.is_utf8`, which `pick_shape` now calls too (fe201329) | the two frame documents disagree on a UTF-8 pipe, and S3 is the scenario the review reads (`phases/phase-1.md`) |
| The gate's other lines that called its run a seal (phase 1, round 1) | `spec.md` S1 names the pass line and a list of phrases; the coverage line said `this seal answers`, `PREFLIGHT_TAIL` said `nothing is sealed`, and the refusals said "no command to seal over" | all of them say `run`, `pass` or `written` (fe201329, 42ff7d11), and the sweep reads the class by construction rather than by listed phrases | contract §12; `questions.md` Q4 (a) reached the refusals (`phases/phase-1.md`, `rounds/round-1.md` finding 1) |
| Where `earlier_verdicts`' cases live (phase 2) | `plan.md` row 2: "`tests/test_chain_check.py` gains `earlier_verdicts`' cases" | `tests/test_the_sealer_guarantees.py::TestEarlierVerdicts`, beside `TestVerdictsOf` | that module holds the readers of `guarantee.md`, the group a new case starts from (`phases/phase-2.md`) |
| A blank row in the stamp (phase 2) | `spec.md` S9 lists the rows `SEALED`, `tree`, `base`, `item`, `gate`, `rounds` | a blank stands between the identity rows and `gate` | the owner's 2026-10-07 layout gives every panel that blank (`phases/phase-2.md`) |
| Local mode draws no stamp (phase 2) | spec silent; S4's writer reads `seal/specs/<id>/guarantee.md` among the commit's paths, which is the shared-mode layout alone | stated in `docs/the-review-record.md` §*The stamp*'s unchecked paragraph; no second trigger | a missing stamp, never a false one; `questions.md` Q5 (a), and the trigger is #976 (`phases/phase-2.md`) |
| The commit-gate document's heading (phase 3) | `plan.md` row 3 names `docs/the-commit-gate-inside-git.md:14` | the heading is kept, and the second duty is named in the opening paragraph and the **Latency** bullet | other documents cite that heading as §*The commit gate inside git* (`phases/phase-3.md`) |
| `bin/seal-stamp.cmd` (phase 3) | `spec.md` §*Scope* and `plan.md` row 3 list it among the files whose words change | unchanged | it names no stamp and no gate (`phases/phase-3.md`) |
| What §*The stamp*'s unchecked paragraph names (phase 3) | `spec.md` S10 names four silences | six: S10's four, local mode, and a person's own commit | the paragraph is where a person looks for why no stamp appeared; the person's own commit is `spec.md` §*Scope*'s (`phases/phase-3.md`) |
| Once per work item (round 1) | `plan.md` B1 holds it by the `Target SHA` row's earlier run and the file name `<ns>-<id>-<target sha>`, and accepts "a re-run after a `sealed` whose row was rewritten without the earlier run would draw again"; `spec.md` S8 matches the name with its target | a values file for the work item's id, whatever commit it named, is not written twice, and a commit whose audited commit is not in its history queues nothing (33a5b676) | round 1's finding 3 drew a second stamp from a fresh re-seal row and from a squash in another clone; the owner's rule is never twice (`rounds/round-1.md`); S8 stays true as a narrower case |
| Once per work item across clones (round 3) | round 1's fix left a second clone of the same branch to the `Target SHA` row's `; earlier run:`, the row an agent writes; `plan.md` B1 named nothing for a second clone at round 3, and since the reframe after round 5 it names the amend in a second clone as round 3's stated limit (the next row) | `seal_stamp.sealed_before`: a guarantee that read `sealed` at any earlier commit of HEAD's history, whatever that verdict's `Target SHA` named, queues nothing, in any clone and after a rebase (b2f97fb1). Round 4's narrowing, which counted an earlier `sealed` only where its target was an ancestor of its own commit (a226da11), is undone by the reframe after round 5, and a `sealed` that drew nothing now counts as the work item's stamp: the work item then draws none, the accepted gap. Stated limit: a `sealed` committed over a history that carries no earlier `sealed`, in a clone that holds no values file for the work item, still queues in that clone, the sealing commit amended or rewritten there over its own parent or a second seal on a copy of the branch that had not fetched the first (`rounds/round-6.md` finding 1) | round 3's finding 2 drew a second stamp in a second clone from a body edit and from a fresh re-seal row; the history is in every clone, the values files are not (`rounds/round-3.md`); round 4's finding 1 found that form drawing no stamp after a corrected row (`rounds/round-4.md`), and round 5's finding 1 found round 4's fix drawing a second stamp after a rebase in another clone (`rounds/round-5.md`). The history cannot tell the two apart, and `questions.md` Q8 (a) chose never twice; the rewritten or unfetched `sealed` is a stated limit by `questions.md` Q9 (a), the orchestrator's answer under the owner's delegation, since across clones the history is the only record read and nothing beside the tree counts stamps, and its fail direction is one more stamp in that clone |
| The double-stamp limit's extent (round 6) | `spec.md` §*Scope*: "The amend of the sealing commit itself in a second clone, which draws the stamp again there … Q8 was not asked about it and this reframe does not decide it. It stays a stated limit"; `plan.md` §*Technical context*: "an amend of the sealing commit itself in a second clone draws again there", and its B1 row: "An amend of the sealing commit itself in a second clone draws again there (round 3's stated limit, left standing)" | the class, stated in the fragment, §*The stamp* and `seal_stamp.py`'s once comment: a `sealed` committed over a history that carries no earlier `sealed`, in a clone that holds no values file for the work item, the sealing commit amended or rewritten there over its own parent or a second seal on a copy of the branch that had not fetched the first (d1af2e22, 9a1330e8) | round 6's finding 1 drew a second stamp from `rebase --force-rebase` and from an unfetched second seal beside the amend (`rounds/round-6.md`); `questions.md` Q9 (a) decided what `spec.md` left undecided: a stated limit, since across clones the history is the only record read and nothing beside the tree counts stamps. The frame's documents are left as written, and this row is where the difference is recorded |
| The sealer's `## Never` clause (round 1) | S12 and §*Scope* say it reads that the stamp is drawn in the orchestrator's session from the sealer's committed `sealed` verdict, once per work item; 6f7aacb2 made it "a stamp is drawn once from your committed `sealed`" | the shorter clause | phase 4's evaluation failed rule 4 alone at 24,757 preload bytes against #969's 24,702; the shorter clause brings the preload to 24,700 and still says what the owner's rule says: drawn once, from the sealer's committed `sealed`, never from the gate's run (`phases/phase-4.md`, `rounds/round-2.md` finding 3) |
| The words that called a broad run a seal outside the gate (phase 3, rounds 1 and 2) | phase 3 left the Seal Test's vocabulary standing, and round 1's fix pass left `the broad seal`, `that seal` and the twenty runs called seals for the owner | reworded to `run` in both READMEs and `skills/verify/SKILL.md`, and in four test failure messages (212db890, 56395233); the concept name, the counterfeit seal and the sealer's seal stay | `questions.md` Q6 (a): words a person reads in the gate's output and the documents follow, and code names and the concept name stay (`rounds/round-2.md` finding 1) |
| The emblems page (the sealer's `withheld`, after round 8) | `spec.md:181` removes `docs/the-broad-gate.md` §*Where the stamp is drawn*, and `phases/phase-3.md:42-46` says the sweep found and reworded every sentence calling the gate's run a stamp; `assets/seals/README.md:1, 3-4` still said "every emblem the broad gate's stamp has carried" and "The broad gate draws a stamp when a run earns it", citing the removed section | the page says the stamp is the sealer's, drawn once per work item at the commit of a `guarantee.md` reading `sealed` (`docs/the-review-record.md` §*The stamp*), and that the two released emblems were drawn by the broad gate's run before #975; the page joins `SEAL_SWEPT`, and `test_no_instructing_document_gives_the_stamp_to_the_broad_gate` refuses the gate owning a stamp and the removed section's name in every swept file, red on the page as f2f7b6d5 carries it (d6e9d285) | the sealer's `guarantee.md` at f2f7b6d5 read `withheld` on those lines, against #975 item 4; phase 3's record names what its sweep reworded and the page is not among them, and no case read the page, so the page went under a check rather than the sentences alone being repaired |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck at the last round's commit | the orchestrator's `broad-gate --base release/v0.22.1 --record <item>`, after the rounds settle |
| A stamp drawn from a real `sealed` guarantee in a person's session: this item's own run draws none, because the installed plugin's `post-commit` is 0.22.0's (`plan.md` §*Operational impact*) | the owner, on the first run after updating to 0.22.1 |
| closed Once per work item for a commit touching a `sealed` guarantee in a second clone of the same branch with no new run, held only by the sealer's `; earlier run:` row | executed: `test_a_sealed_item_recommitted_in_another_clone_queues_nothing` red at b81de037, green with `seal_stamp.sealed_before` (`rounds/round-3.md` finding 2); the rewritten or unfetched `sealed` it leaves is a stated limit above |
| CI on its three legs at the pull request's head | the orchestrator, at the pull request |

## Not done

- `.github/scripts/release_seal.py` still labels the release's PNG `SEALED`.
  It is a different object from the work item's stamp, and `spec.md`
  §*Scope* puts it out; whether the word may stand there is the owner's.
- A clone whose git hooks slot is somebody else's, and local mode, draw no
  stamp. Both are stated in §*The stamp*; no second trigger was built
  (`plan.md` A3, `questions.md` Q5, #976).
- A work item whose guarantee read `sealed` once without drawing a stamp
  draws none afterwards. A `sealed` over a commit the branch does not hold
  is the case rounds 4 and 5 measured, and a later commit that corrects the
  row draws nothing either, because the history cannot tell that `sealed`
  from one stamped before a rebase. `questions.md` Q7 and Q8 (a) accept
  the missing stamp over a second one, and #976 carries the gap; the
  pull request's check still says the work item was sealed.
- A `sealed` committed over a history that carries no earlier `sealed`, in
  a clone that holds no values file for the work item, draws the stamp
  again in that clone: the sealing commit amended or rewritten there over
  its own parent, or a second seal on a copy of the branch that had not
  fetched the first. The clone that drew the stamp keeps its values file,
  so an amend there draws nothing. `questions.md` Q9 (a) keeps it a
  stated limit, written in the fragment, §*The stamp* and `seal_stamp.py`'s
  comment, because a mechanism would need a count kept beside the tree.
- Test docstrings and comments that tell how the gate used to seal are left
  as history. Q6 (a) reaches the words a person reads in the gate's output
  and the documents, and a failure message is one of them; a docstring is
  not.
- `agents/warden.md` says a coverage probe is reported "never as a seal".
  That names the concept a claim is held to, not the gate's run, and
  changing the definition would move the warden's measured preload.

## Fed back into the spec

Inferred during implementation, and open to a planner to overturn:

- `docs/the-review-record.md` §*The stamp*: once per work item is held by the
  work item's id alone in the clone's values files, whatever commit they
  named, and by the audited commit being in the committing commit's history
  (round 1's fix, 33a5b676), and across clones by the guarantee having read
  `sealed` at any earlier commit of that history, whatever that verdict
  named (round 3's fix, restored by the reframe after round 5 at b2f97fb1
  once round 4's narrowing was undone).
- The same section's unchecked paragraph names local mode and a person's own
  commit beside S10's four silences (phase 3).
