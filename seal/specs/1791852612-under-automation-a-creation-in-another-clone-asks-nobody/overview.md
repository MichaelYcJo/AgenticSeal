# 1791852612-under-automation-a-creation-in-another-clone-asks-nobody — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. Facts that must outlive this work item go to the
evidence ledger, not here. -->

📋 implement applied
· spec:     this item's `spec.md` (Grounding, In 1, §The class, S1–S15, §Removes), `plan.md` (phases 1–2, W1, W2), `questions.md` (P1, M1, M2, W1, W2); `docs/worktree-guard-spec.md` §B, §Creation consent rule 4, §Choice sites *Under the press*, §Known limits; `docs/the-reader-registry.md` §The four classes
· evidence: `seal/ledger/1791852612-under-automation-a-creation-in-another-clone-asks-nobody.md` — S1–S14, 35 `Re-read ·` rows, one `Corrected ·` (#896's S13)
· verified: executed — the phase 1 and phase 2 test modules, ten mutations (all red), the S11 probe, the fragment and whole-ledger evidence checks, the survivor sweep; read — the 36 drifted released rows; unverified — S11 on Windows, the full suite

## Why this work exists

Under `automation`, a `git worktree add` in a clone the press was not given in put its two choice rows to a person who had said nobody would answer; it now denies to the model on every attempt, naming no way on, and nothing a person sees changes.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| S10's fourth count | `spec.md` S10: *the counts are 1, 2, 1, 1 — `consent` once each, and the rows' read only where a row fires under the press*. The code reads the transcript twice attended in the other clone's idle state | the code: `[1, 2, 1, 2]` | Row 3 fires attended too, and whether the press is there is what its read finds out; no reading knows the press is absent without it. The bound the frame argued — at most twice per creation — holds in every state (`phases/phase-1.md`) |
| S1's *no `worktree add` in the reason* | `spec.md` S1: *no `worktree add` in the reason*. Every creation row opens with `origin`, which names `git worktree add` as the command judged | the intent: no `worktree add` after the origin line | The sentence's purpose is that no command to run is named; the origin line is the situation, kept byte for byte as In 1 requires (*opens with the row's situation as today: `origin`, …*) |

| The prompt budget's zero | `docs/worktree-guard-spec.md` §*Creation consent*: *Zero for a session whose person pressed `automation`.* — already false at `321e9de1` in another clone, and `spec.md` S14 does not name the sentence | scoped to the press's own clone, pointing at the new subsection | A policy sentence the new subsection contradicts as written; leaving it would have the section state two budgets (`phases/phase-2.md`) |
| The frame's coordinates | `spec.md` (twice) and `plan.md` cited `hooks/worktree-guard.py#guard_worktree_creation` with its `321e9de1` hash, which the records arm reads as a claim about the tree | the unit named at `321e9de1` without the hash | The build moves that hash by design; the words are otherwise the framer's |

## Not verified

| Item | Who must answer |
|---|---|
| closed S11 / M1: on Windows a creation in another clone under the press is row 4's deny with nothing stubbed (`test_on_windows_a_creation_in_another_clone_is_row_fours_deny`, skipped off Windows) | #997's `windows-latest` shards ran `tests/test_a_creation_in_another_clone_asks_nobody.py` green |
| closed The full suite, the repository-wide lint and the typecheck | #916, merged with lint and the suite green on the ubuntu, macOS and Windows legs; the repository configures no typecheck |

## Not done

The tracked-changes row's deny under the press (#894) carries the press and
re-issue sentences inlined; W1 moved only `main`'s two locals, as framed,
and that third copy is left as it was (`phases/phase-1.md`).

## Fed back into the spec

none
