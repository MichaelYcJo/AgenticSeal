# 1791384155-a-round-record-cell-has-one-reader — review round 2

| Field | Value |
|---|---|
| Target SHA | 03779b65f1549fe7ce75553080655366cd460b05 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | 890 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are written and no round has opened them |
| Fix range | `ff88f31dfd832cf486248966a766ff628586668f..07449c197391398a44b6b5acb4eac68e444e1802`, 3 commits |
| Contract changes | run → run, attempt, gh_json, _issue_api, drop_label, arrived, existing_labels, create_label, add_label, is_ancestor, commit_message, release_exists, merged_pulls, create, merge_base, subjects_since, milestone_titles, open_in_milestone, labelled, gh, tagged, rasterise, content_at, try_run, list_open_issues, close_issue, open_issue, add_xdist, add_markdown_it, add_pillow, add_cmarkgfm, build, main, README.md, git, _process, common_dir, _git, claude_ancestor, _ps, git_dir, dirty, resolve_runner, git_dir_of, repo_root, git_common_dir, current_branch, owner_pid, latest, ancestors, proc_cwd, host_app, tty_idle_minutes, lease_owner_alive, lease_dir, sessions_in_tree, tracked_changes, phantom_entries, repo_paths, 1791384155-a-round-record-cell-has-one-reader.md, 0.10.0.md, 0.11.2.md, 0.11.3.md, 0.12.2.md, 0.12.3.md, 0.15.4.md, 0.17.0.md, plan.md, questions.md, spec.md, overview.md, post-review-check-2.md, post-review-check.md, round-1-report.md, round-2-report.md, round-2.md, round-1.md, SKILL.md, config_at_head, pull_request_from_gh, carried_by_a_pull_head, resolves_to, pull_request_cell, read_blobs, config_at, git_asked, porcelain, tracked, install_workflow, remove_workflow, gitlinks_under_root, switch, released, tracked_text, run_arms, broad_gate.py, cmd_exe_reads, handed_to_shell, quote, compare_at_base, seal_record, gate, run_gh, commit_of, overviews_at, tree_at, wrote_a_spec, show, pytest |
| New units | none |
| Fix of a fix | first — 🟡 2 at skills/code-review/scripts/chain_check.py#main, a unit round-1's fixes changed |
| Needs a fix | yes — 🔴 1 the pasted phrase that fails three CI legs; 🟡 2 the three draft-worded notices printed for a run nobody observed |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Verifying round 2 of round 1's fixes: b10835ff..092808fe plus the table and the close at 03779b65. The job was the answers to round 1's six verdicts; round 1's new units were a finding surface. The spawn named four things to judge. First, whether unknown is ever read as ready, or ready as unknown, by any reader. Second, whether event_payload_present tells a real event from a stray file. Third, whether DEFERRED_HEAD_RE keeps every note byte. Fourth, a re-run of the base-against-branch chain_check comparison over every record under the unknown state. It also ran the eight guard modules once. Facts arrived labelled. Read: the orchestrator's direction that an unobserved state reads as unknown. Read from the smith: the stub default, the panel string, deferred_parts, two Corrected rows and the module runs.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🔴 1 | The fix pass wrote one phrase into both docs, so the pair shares 33 runs where 31 were measured, and three CI pytest legs fail at the target | `docs/review-chain-spec.md:656` | **fixed** `6b9f311e` | fixed at 6b9f311e — the review-chain-spec sentence reworded as the report showed; the paste ratchet counts the pair at 31 shared runs, its baseline, and the module passes; the file stays at 999 lines; executed: the module fails 2 of 8 in the scratch clone; the shared-run count is 31 at b10835ff and 33 at 092808fe; read: `gh pr checks 890` shows three legs failing the same two cases |
| 🟡 2 | With the state unknown, three notices still say a draft exists and send the reader to *Ready for review* | `skills/code-review/scripts/chain_check.py:5956` | **fixed** `3f08be56` | fixed at 3f08be56 — the empty-`rounds/` notice, the `Pass`-beside-`nobody` notice and the open-note notice each say they print for a pull request not marked ready, or none seen; each pinned in a draft and in an unseen run. The check's non-strict arms hold no fourth sentence naming a draft: `broad_gate` and `direct_seal` print nothing when not strict, and the other draft words print only at a ready pull request; executed: the unknown run prints the first notice for eight declarations, byte-identical to draft; read: the same wording at `chain_check.py:2721` and `chain_check.py:5095`; no case pins any of them |
| ⬜ 3 | The unseen state's line says CI judges it, and in local mode and on a route that stops before the pull request nothing does | `skills/code-review/scripts/chain_check.py:1335` | answered | the line names the source the decision rests on where one exists; in local mode and on a route that stops before the pull request no CI runs, and how such a route is read is `questions.md` Q1, the owner's to answer, with the default the check already follows; read: `templates/hygiene.yml` lines 12-22; `questions.md` Q1 |
| ⬜ 4 | `event_payload_present` re-decides what `pull_request_state` already decided, which makes a second reader of one fact | `skills/code-review/scripts/chain_check.py:1341` | answered | `event_payload_present` asks whether GitHub wrote a payload at all, which `pull_request_state`'s `(state, where)` does not carry; the two read the same environment variable and cannot disagree, which the reviewer executed on four shapes. Folding the question into the state's answer would change its shape for every caller, which this last fix pass does not take; read; executed: the two agree on a directory, an empty file, a file that does not parse and a payload with no pull request |
| ⬜ 5 | A note keeps a closing mark that the home opened (`**deferred #854 — the note**` gives `the note**`) | `skills/code-review/scripts/chain_check.py:1947` | answered | no cell in the tree has the shape (executed by the reviewer); the note is the fix pass's prose written as given, and a mark the home opened and the note closes is the writer's to balance. Recorded, not changed, in the run's last fix pass; executed on written cells; no cell in the tree has this shape |
| 🟢 | round 1's finding 1 is closed — an unseen pull request reads as unknown, and the generator does not fail the record it wrote | `skills/code-review/scripts/chain_check.py:5737` | confirmed | executed: unknown and no-`gh` output identical to draft over every record; payloads that cannot answer identical to ready; the new case fails without the fix |
| 🟢 | round 1's finding 2 is closed — the suite's stub defaults to unknown, and the helpers that mean ready say so | `tests/conftest.py:559` | confirmed | read: ten helpers on `gh_answers(…, "ready")`; executed: unknown is identical to draft |
| 🟢 | round 1's finding 3 is closed — the panel hands `says_reopened` the gate's string | `skills/verify/scripts/broad_gate.py:2942` | confirmed | executed: both invisible-led cells fail without the fix and pass with it |
| 🟢 | round 1's finding 4 is closed — the note keeps its marks | `skills/code-review/scripts/chain_check.py:1943` | confirmed | executed: both new cells fail without the fix; 90 cells, every note verbatim, no real home moved |
| 🟢 | round 1's notes 5 and 6 stand as the smith answered them | `skills/code-review/scripts/chain_check.py:1302` | confirmed | executed: a payload always wins over `gh`; read: `sealing_excuses` excuses one arm |

## Paste-ready fixes

```markdown
ready pull request, and where a payload cannot answer. In a draft, or where no
pull request was seen, it prints: the pair stands there between `close` and
the verifying round's record, and *Ready for review* re-runs the check.
```
```markdown
ready pull request, and where a payload cannot answer. It prints in a draft and
where no pull request was seen: the pair stands there between `close` and the
verifying round's record, and *Ready for review* re-runs the check.
```
```python
                        f"declares `{routing.CHAIN}` and "
                        f"{item}/{routing.ROUNDS_DIR}/ holds no `round-N.md` "
                        "— which is the state a draft pull request opens in, "
                        "and the state of a run no pull request was observed "
                        "for: the rounds run against it, so the record cannot "
                        "exist yet. It is still owed, and pressing *Ready "
                        "for review* fires `ready_for_review`, re-runs this "
                        "check, and fails the pull request if it is still "
                        "missing",
```
```python
                    f"`Pass` is checked beside `{CHECKED_BY}: {cell.strip()}` "
                    "on the last record — the state a draft, or a run no pull "
                    "request was observed for, is in between `close` ticking "
                    "`Pass` and the verifying round's record committing. It "
                    "prints because neither is a request to merge. It is "
                    "still owed: spawn one verifying round at "
                    "the diff of these fixes, and this cell names it. "
                    "Pressing *Ready for review* fires `ready_for_review`, "
                    "re-runs this check, and fails the pull request if the "
                    f"cell still says `{NOBODY}`",
```
```python
                        f"{said}. It prints because a draft, or a pull request "
                        "nobody observed, is not a request to merge; pressing "
                        "*Ready for review* re-runs this check and fails the "
                        "pull request if it is still open",
```
```python
    assert (
        "the state a draft pull request opens in, and the state of a run no "
        "pull request was observed for"
    ) in out, out
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` on the eight guard modules, in the scratch clone at 03779b65 | 437 passed, exit 0 |
| the branch's `chain_check.py` over the branch's tree, every declaration counted as changed (grafted empty root), under `gh` unknown, no `gh`, `gh` draft, `gh` ready, a draft payload, a ready payload, and four payloads that cannot answer with `gh` draft | unknown and no `gh` identical to `gh` draft (139 lines); `gh` ready identical to a ready payload (145 lines); all four payloads that cannot answer identical to a ready payload; all exit 1, on squash-removed `Target SHA` commits |
| the base's (ad447367) `chain_check.py` over the same tree with no payload, a draft payload and a ready payload | draft identical to the branch's; ready differs by the sealer advice line alone; no payload (ready at the base) against the branch's unknown: ready-only refusals become draft notices |
| `tests/test_no_passage_is_pasted_into_a_second_file.py` in the scratch clone at 03779b65 | 2 failed, 6 passed, exit 1, the same two cases as CI |
| the module's own shared-run counter over the two docs at b10835ff, 092808fe and HEAD | 31, 33, 33; two new windows, both the phrase in 🔴 1 |
| the same counter with 🔴 1's rewording applied in memory | 31 |
| `chain_check.py` and `broad_gate.py` restored from b10835ff, then the new panel, deferral and unknown-state cases | 2 failed (panel); then 3 failed (2 deferral, 1 unknown state); green once the files were restored |
| `deferred_parts` at b10835ff and at the target over 90 deferral cells from the tree plus 14 written to break it | home moved in 3, none a real record's; no note differs beyond its marks; every note is a substring of its cell |
| `gh pr checks 890` | read: three pytest legs fail on `tests/test_no_passage_is_pasted_into_a_second_file.py`, every other leg passes, at head 03779b65 (CI's run, read here) |
| the full suite, the repository-wide lint and the typecheck (the broad gate) | not yet — the sealer's, after the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|
| round-1 | `skills/code-review/scripts/round_record.py:2735` | round 1's 🟡 1 — fixed |
| round-1 | `tests/conftest.py:560` | round 1's 🟡 2 — fixed |
| round-1 | `skills/verify/scripts/broad_gate.py:2938` | round 1's 🟡 3 — fixed |
| round-1 | `skills/code-review/scripts/chain_check.py:1891` | round 1's 🟡 4 — fixed |
| round-1 | `skills/code-review/scripts/chain_check.py:1325` | round 1's ⬜ 5 — answered |
| round-1 | `skills/code-review/scripts/chain_check.py:4441` | round 1's ⬜ 6 — answered |
| round-1 | `skills/code-review/scripts/chain_check.py:5707` | round 1's 🟢 — confirmed |
| round-1 | `skills/code-review/scripts/chain_check.py:4448` | round 1's 🟢 — confirmed |
| round-1 | `skills/code-review/scripts/chain_check.py:1330` | round 1's 🟢 — confirmed |
| round-1 | `skills/code-review/scripts/chain_check.py:1255` | round 1's ❓ — out of verified scope |

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
