# Implementation Plan: 1794187229-the-body-carries-the-seal-mark

## Technical context

The tree as read at `857a7356`.

`skills/code-review/scripts/chain_check.py#main` (lines 1867 to 2046) judges
each declaration in turn and runs `broad_gate` and `guarantee` for every one;
under `--sealing` their findings go to the notices. `pull_request_state`
(line 536) opens the file `GITHUB_EVENT_PATH` names and reads
`pull_request.draft`; `event_payload_present` (line 530) says whether the
file is there. The arm reads `pull_request.body` from the same file.

`skills/code-review/scripts/pr_body.py#main` (line 836) builds the
composition from `seal_mark`, `read_item` and `read_own`, and under `--check`
hands it with the body file's text to `_check` (line 785), which raises
`Refused` with one cause per differing line through `difflib.SequenceMatcher`
and names the first line of each opcode. `pr_body.py` loads `chain_check.py`
by path at its import (line 141), which is why the arm loads `pr_body.py`
inside its function. `lib/blocks.py#gfm_lines` strips `\r\n`, so the
payload's line ends need no care (design G13).

`.github/workflows/hygiene.yml` runs `chain_check.py` with
`--baseline origin/<base>` and lists `edited` in `types:` already;
`templates/setup/hygiene.yml` lists the default events and the two draft
events, and `tests/text/test_ci_gives_the_checks_what_they_need.py` pins
the draft events wherever a workflow runs `chain_check.py` (`DRAFT_EVENTS`,
`DRAFT_READER`, line 71). `skills/verify/scripts/broad_gate.py` (line 3082)
runs the check with `--sealing` and no payload.

The failure scenario of the chosen approach: a repository whose workflow
clones the plugin at an older tag runs no arm, and one whose `types:` lacks
`edited` reads a body sent after the pull request opened only on the next
push. The arm is in the check and not in the workflow, so a repository
re-installing the workflow gets both at once, and `seal pr-checks` names the
pinned release. A second scenario: GitHub replays the event's body on a
re-run, so a body repaired without a push stays red until the next
`edited` or `synchronize` run; the orchestrator's `gh api -X PATCH` is an
`edited` event, so the normal repair re-runs it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. A `body` arm in `chain_check.py` reading the payload's `pull_request.body` and comparing through `pr_body.py`'s check (chosen) | A workflow pinned to an older release runs no arm; a workflow without `edited` reads a later body only on the next push; a re-run replays the old body (design G15 and *Technical context*) | chosen: the check already opens the payload (G8), already knows the judged declarations and the draft state, and already prints `path:line` annotations; the comparison already exists and runs for the sealer (G2, G4) |
| B. A workflow step that writes the mark into the body with `gh api -X PATCH` once the guarantee reads `sealed` at HEAD | Needs `pull-requests: write` where the template declares `contents: read`; writes into a body the sealer audited; every drift but the mark stays unread; the mark then says a workflow ran, not that the body is the records' | rejected |
| C. A command that composes the body and opens the pull request, such as `seal pr-open`, or a hook on `gh pr create` | `gh pr create` stays callable and no hook may intercept it (G17), so the step is still remembered; a subcommand is a mechanism with no catch of its own | rejected; re-weighed if the arm keeps turning red on bodies sent too early |
| D. Replacing the structure: drop the body file the sealer checks at step 2, have the sealer read `pr.md` and the records directly, and compose the body once after the seal, read by the arm alone | Local mode has no arm, so the body there is read by nobody (G16); a hand-edited body before the seal meets its reader only at the pull request | rejected: the premise that keeps the structure, that the sealer's check is local mode's one reader of the body, holds at `templates/setup/hygiene.yml`'s header and `skills/core/SKILL.md`'s invariants paragraph |
| E. A separate `hygiene` step running `seal pr-body <item> --body <file> --check` with the body from `env:` | The step has to find the work item's directory, which the check already does; two readers of one payload; the template and the repository's workflow each gain a step that has to agree with the check on what is declared | rejected in favour of A |
| F. Compare the mark's presence alone, not the whole body | The issue's *Done when* asks for drift too; a mark-only reader is a second comparison beside `_check`, with its own spelling of the mark line | rejected: `_check` compares the whole and the mark is one line of it |
| G. Leave the sentence in `skills/code-review/orchestration.md` as the hold | Design G10: every pull request of 0.36.0 opened without the mark under that sentence | rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* item 2, and the `tests/skills/test_pr_body.py` case of item 5 | the new case seen red against the current `_check` on a body lacking the mark line and its blank line (design G12's shape), then green; `tests/skills/test_pr_body.py` green | |
| 2 | *Scope* item 1, the `chain_check.py` sentences of item 4, and the `tests/skills/test_chain_check.py` cases of item 5 | each case seen red with the arm absent, then green; `tests/skills/test_chain_check.py` and `tests/skills/test_pr_body.py` green; `tests/behaviour/test_this_repository_passes_its_own_checks.py` green for the marker the check line names | |
| 3 | *Scope* item 3, the remaining sentences of item 4, and the work item's `changelog.md` | the `tests/text/test_ci_gives_the_checks_what_they_need.py` pin on `edited` seen red against the template as it stands, then green; `git grep` for the two sentences of *Removes* finds neither; the tree-wide files `CONTRIBUTING.md` *Running the checks* names green | |

## Overlap with the release

The spawn names no other work item running beside this one: #1439 to #1444
have merged into the base at `1af09327`. None meets this work.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| none | | | |

## Operational impact

No version move: #1443 moved it. No new dependency. A repository that
installed `hygiene.yml` from an earlier release runs no arm until it
re-installs the workflow or edits its `types:` line and the pinned tag
(design *Data & interfaces*). In this repository `edited` is already in
`.github/workflows/hygiene.yml`, so the arm runs on the next body edit.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
