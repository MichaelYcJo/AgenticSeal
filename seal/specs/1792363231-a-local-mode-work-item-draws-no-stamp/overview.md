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
| Guard 3 of the refusal record (phase 3) | `spec.md` S13: "A refusal record is written only where all four guards hold … (3) The guarantee at `HEAD^` did not read one `sealed` over the same target, so this commit introduced the verdict"; `plan.md` row 3 names four guards and a case seen red for each | three guards: `seal_stamp._stamped_nowhere_else` holds guard 2 and guard 4, and guard 1 is the position of its call (9ad38d66). `docs/the-review-record.md` §*The stamp* states three | guard 1's order leaves guard 3 nothing to decide. A record is considered only after `sealed_before` returned False, so every `sealed` in HEAD^'s history is already one this clone refused, and guard 3 could only withhold a record that already exists. Shown by mutation at a6ee1176: with guard 3 deleted, all 39 selected cases stayed green (`phases/phase-3.md`). `test_a_body_edit_over_a_rewritten_seal_writes_no_refusal`, the shape the spec gives guard 3, stays; `sealed_before` refuses it first |
| How the local writer rules out shared mode (phase 1) | `spec.md` §*Data & interfaces*: "`<common>` is a git common directory and `optin.home_at` for that repository answers `<common>/seal`. That rules out shared mode and a repository with both roots" | the writer also requires `optin.git_common_dir(<main worktree>)` to resolve to the directory above `seal/` (256b1b4d) | for `<repo>/seal/specs/<id>/guarantee.md` the directory above `seal/` is `<repo>`, and `home_at` answers `<repo>/seal`, so `home_at` alone lets a shared-mode path through; `test_the_edit_gate_leaves_shared_mode_to_post_commit` went red with that check deleted (`phases/phase-1.md`) |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck at the last round's commit | the orchestrator's `broad-gate --base <base> --record <item>`, after the rounds settle |
| Windows path comparison: the edit gate's `os.sep` mapping and the local writer's two `realpath` comparisons (`questions.md` Q3) | CI's Windows leg, read by the orchestrator at the pull request |
| The reflog subjects guard 2 reads, on git versions other than 2.50.1 | CI's legs, through `test_guard_two_reads_what_post_commit_sees_in_the_reflog`, read by the orchestrator |
| A local-mode stamp drawn on a person's screen from the edit hook's line; this repository runs in shared mode, and its run draws through the installed plugin's hooks (`plan.md` §*Operational impact*) | the owner, on the first local-mode run after updating to the release that carries this work |
| The sealer measured against #975's phase-4 side after its one-word change (`spec.md` S9) | the orchestrator, phase 5 |

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
