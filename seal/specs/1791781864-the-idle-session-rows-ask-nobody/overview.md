# 1791781864-the-idle-session-rows-ask-nobody — overview

<!-- The closing memo (implement skill, step 4). Not a summary of the work:
`git diff --stat` holds the file list and the diff holds the detail. Only what
the diff cannot show goes here, and each part is written when it happens rather
than reconstructed at the end. Facts that must outlive this work item go to the
evidence ledger, not here. -->

📋 implement applied
· spec:     `spec.md` In 1, In 2, §*The class*, S1–S14; `plan.md` §*Seams* and phases 1–3; `docs/worktree-guard-spec.md` §A, §*Choice sites*, §*What a blocking prompt must show*, §*Unknowns resolve conservatively*, §*Known limits*; `docs/the-reader-registry.md`; `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment*
· evidence: `seal/ledger/1791781864-the-idle-session-rows-ask-nobody.md` S1–S13 and M2, and two `Re-read ·` rows; `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md` S2 and S9 restated; `seal/ledger/1791384157-…md` rows re-stamped in place after reading
· verified: the cases and mutations each phase record names were executed; the Windows reading (M2) and the unattended loop (M1) were not

## Why this work exists

Under `automation` the switch ladder's idle-session and cannot-tell rows put
a question to the person anyway, and the line under them said a 4.7-hour-old
lease was working right now; now both rows refuse the switch to the model
naming the worktree split, and the line prints only what was measured.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| S6's dirty half | `spec.md` S6: *with one modified tracked file, #894's deny with the token lead*. Phase 2 could pin only the lead, because #894 was not merged | the whole deny, compared with #894's `dirty_deny`, added in phase 3 | `phases/phase-2.md` *What this phase found* 1 |
| S7's branch | `spec.md` S7 runs `git worktree add ../wt -b feature/x`; the `repo` fixture already holds `feature/x`, so git refuses it | `feature/y` | `tests/conftest.py#_build_repo` (`phases/phase-2.md` 2) |
| the split's consent in another clone | `spec.md` In 2: *under the press a creation is consented before any row is read*, and §*The class* calls §B's choice rows unreachable under the press. Round 1 executed a switch into another clone: the press is consent only in the clone it was given in (`hooks/worktree_consent.py#automation_answered`, condition 4), so the named split met §B's choice row and asked a person | the deny names the split only in the press's own clone or one holding this session's creation record, and names none elsewhere; whether §B's rows should deny there is #903 | round 1's 🔴 1 (`rounds/round-1-report.md`) |
| `## Removes` in `spec.md` | the frame has no such section; #835 landed `Removes from` at `1791780031`, below this id, so the records arm refuses the frame without one | the smith wrote the section in phase 3, naming the removals In 1 and §*Seams* already name | `docs/the-reader-registry.md` §*A frame names what its work removes* |

## Not verified

| Item | Who must answer |
|---|---|
| closed On Windows, with nothing stubbed, a switch under the press is row 2's deny (`questions.md` M2); `test_on_windows_a_switch_under_the_press_is_row_twos_deny` is skipped off Windows | #997's `windows-latest` leg ran `tests/test_the_idle_session_rows_ask_nobody.py` green |
| closed Whether the deny loops, or a Windows run splits twice, in a real `automation` run (`questions.md` M1) | another session's behaviour: the re-issue bullet of `docs/worktree-guard-spec.md` *Known limits* |
| closed The full suite, lint and typecheck over the merged tree | #902, merged with lint and the suite green on the ubuntu, macOS and Windows legs; the repository configures no typecheck |

## Not done

The steer and the new deny print `{wt_root}` unquoted, so a path holding a
space, or a Windows path in a POSIX shell, is not safe to copy. This predates
the work item, and the attended text is held byte for byte (S5), so it was
left (`phases/phase-2.md`).

## Fed back into the spec

`docs/worktree-guard-spec.md` §*Unknowns resolve conservatively* gained a
paragraph S13 did not list: its *a deny that fires on EVERY switch in an
environment is an outage* is now true of these two rows on Windows under the
press, and the paragraph says what keeps it a cost (inferred during
implementation).
