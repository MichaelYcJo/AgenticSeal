# 1792363231-a-local-mode-work-item-draws-no-stamp — overview

<!-- The closing memo (implement skill, step 4). Only what the diff cannot
show goes here. -->

## Why this work exists

A work item in local mode now draws its stamp at the write of its `sealed`
guarantee, and a `sealed` the plugin refused no longer counts as the stamp
it never drew.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The repair after a refused commit drew nothing (phase 6) | `spec.md` S11 at d33e1021: the refusal at the commit points to a new audit that draws once | the framer corrected the frame at 59c65527: the gate records the refusal it makes, and the shared chain reader keeps its `refused_here` skip (candidate 2 of `phases/phase-6.md`); no `Reframed` mark line, since the review chain did not send the item back | the new audit keeps the refused verdict as `; earlier run: <sha> sealed`, and with no record the chain counted it; the refusal is a fact the gate holds in that clone at that moment, so the record needs no guard (`plan.md` §*Technical context*, the path walk) |
| `hooks/git/pre-commit.py`'s docstring (phase 6) | `spec.md` S10 at d33e1021: "`hooks/git/` is unchanged"; `plan.md` row 7: "`git diff --stat 769f2aa4 HEAD -- hooks/git/` empty" | the docstring names the third thing the hook judges, as row 6 asked (contract §19), so the diff names `pre-commit.py` alone (de80c2c2) | a hook's docstring that stops naming what the hook judges is the stale sentence §19 forbids; the correction at 59c65527 rewrote S10 to "changes in `pre-commit.py`'s docstring alone", so the row records the frame following the build |
| closed Guard 3 of the refusal record (phase 3), and the other-ref guard round 1 added beside it. Closed at 061dfdc2: `post-commit`'s record, `_stamped_nowhere_else`, `_guarantee_on_another_ref`, `plain_commit` and their cases are deleted, and the commit gate writes the record with no guard (`spec.md` S11 as corrected at 59c65527) | `spec.md` S13: "A refusal record is written only where all four guards hold … (3) The guarantee at `HEAD^` did not read one `sealed` over the same target, so this commit introduced the verdict"; `plan.md` row 3 names four guards and a case seen red for each | guard 3 is not built: `seal_stamp._stamped_nowhere_else` holds guard 2 and guard 4, and guard 1 is the position of its call (9ad38d66). Round 1's finding 1 added a condition the frame did not name, that no other ref holds, outside HEAD's history, a commit that changed the guarantee (`_guarantee_on_another_ref`), so `docs/the-review-record.md` §*The stamp* states four things that must hold, guard 3 not among them | guard 1's order leaves guard 3 nothing to decide. A record is considered only after `sealed_before` returned False, so every `sealed` in HEAD^'s history is already one this clone refused, and guard 3 could only withhold a record that already exists. Shown by mutation at a6ee1176: with guard 3 deleted, all 39 selected cases stayed green (`phases/phase-3.md`). `test_a_body_edit_over_a_rewritten_seal_writes_no_refusal`, the shape the spec gives guard 3, stays; `sealed_before` refuses it first |
| How the local writer rules out shared mode (phase 1) | `spec.md` §*Data & interfaces*: "`<common>` is a git common directory and `optin.home_at` for that repository answers `<common>/seal`. That rules out shared mode and a repository with both roots" | the writer also requires `optin.git_common_dir(<main worktree>)` to resolve to the directory above `seal/` (256b1b4d) | for `<repo>/seal/specs/<id>/guarantee.md` the directory above `seal/` is `<repo>`, and `home_at` answers `<repo>/seal`, so `home_at` alone lets a shared-mode path through; `test_the_edit_gate_leaves_shared_mode_to_post_commit` went red with that check deleted (`phases/phase-1.md`) |
| What the orchestrator quotes in local mode (round 1) | `spec.md` S7: "`skills/code-review/orchestration.md`'s stamp paragraph says the same for local mode: the stamp is drawn at the end of the turn in which the sealer's report arrives, and the line to quote is the edit hook's message" | the paragraph says the edit hook's line is shown to the person at the sealer's write and does not reach the orchestrator; where no stamp appeared, the orchestrator names the values file and leaves `seal-stamp --from` to the person | the edit gate prints only a `systemMessage` from a `PostToolUse` inside the sealer's run, and nothing hands it to the sealer's report or to the orchestrator (`rounds/round-1.md` finding 2) |

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck at the last round's commit | the orchestrator's `broad-gate --base release/v0.22.2 --record <item>` at 4415c5db, exit 0: 7547 passed, 14 skipped, chain exit 0 (`broad-gate.md`); the run at 59732199 failed on the census module, fixed at 20ea0280 and reviewed in round 6 |
| closed Windows path comparison: the edit gate's `os.sep` mapping and the local writer's two `realpath` comparisons (`questions.md` Q3) | #997's `windows-latest` leg ran the suite green |
| closed The reflog subjects guard 2 reads, on git versions other than 2.50.1 | 061dfdc2 deletes guard 2 and `test_guard_two_reads_what_post_commit_sees_in_the_reflog`; nothing reads the reflog, so no git version's subjects matter |
| closed A local-mode stamp drawn on a person's screen from the edit hook's line; this repository runs in shared mode, and its run draws through the installed plugin's hooks (`plan.md` §*Operational impact*) | a screen: the local-mode sentence of `docs/the-review-record.md` *The stamp*, *What the person's screen shows is not checked* |
| closed The sealer measured against #975's phase-4 side after its one-word change (`spec.md` S9) | executed by the orchestrator: `noninferiority.py` run, compare and check each exit 0, `evals/sealer-phase-5.md` reads `Verdict: pass`, committed at 11b90191 (`phases/phase-5.md`) |

## Not done

- `seal mode shared` moving a local root into the tree: the commit that adds
  it carries every `guarantee.md` at once, and `post-commit` reads each by
  the shared rules. `plan.md` §*Technical context* leaves it for the
  orchestrator to file.
- `skills/code-review/orchestration.md` still tells the orchestrator to
  commit `guarantee.md` and `broad-gate.md`, which local mode cannot commit.
  `spec.md` §*Scope* puts that wording outside this work.

## Fed back into the spec

none
