# the record of truth is tests, not coordinates (#944) — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. -->

## Why this work exists

The ledger re-read 1,421 prose claims to confirm 1,420, so the record of truth
moves to tests a rule's `Enforced by:` names, and the plugin stops shipping the
ledger.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| the owner's tenet, committed by #944 as its first act | `spec.md` §*Scope* names no `CLAUDE.md` section and no rewrite of `CONTRIBUTING.md` §*What a change to a gate must carry* beyond its ledger sentences / the build's first commit adds `CLAUDE.md` §*The rule a mechanism is kept against — subtract before you add* below the goal section, moves the goal's `CONTRIBUTING.md` link into it, and rewrites that `CONTRIBUTING.md` section in place so a pull request adding a mechanism names the one it removes, or why none can go, with what that one caught | the build | the owner set the tenet on 2026-10-14 and the orchestrator's spawn ordered it before phase 1, so every session reads it from the tree rather than from one session's memory. `CLAUDE.md` 9,261 → 9,827 B. One released row drifts on it, `seal/releases/0.18.1.md` row O1 under `CLAUDE.md#"## The goal a design is chosen against — verification that runs unattended"@d8810fc4`; its claim, "The goal section's batch sentence is folded into its link to `implement`'s step 1", still holds, and no `Re-read ·` row is written because this work item retires the ledger (phase 2 removes the arm that reads it) |

## Not verified

none — the commit's narrow checks ran; the broad gate is the sealer's, after the rounds

## Not done

Phases 1–5 of `plan.md`: phase 1 waits for #930 to merge.

## Fed back into the spec

none
