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
| H. The mark's address drops the version: `<repository>/raw/HEAD/<icon>` (chosen after phase 2, design G21 and G22) | The picture is the icon at the default branch, so a change to its bytes there changes what every past body shows, and a renamed icon path or a moved repository breaks every past body's picture; a release that does either re-pins the workflow (design *Data & interfaces*) | chosen: the line reads nothing the two copies differ in, the stamp states no version and the mark means what the stamp means, and the tag address shows no picture for a body the tree's copy composes before the tag exists (G21) |
| I. The version read from a record both copies open at HEAD, such as a line of `trail/gate.md`'s run block or `guarantee.md`'s verdict block | Neither record holds a plugin version today (`lib/fields.py#GATE`, `#GUARANTEE`), so it adds a line to a record grammar, its writer and its reader, for a distinction no reader acts on; the version written is the installed plugin's, so a body of this repository during a release still names a tag that does not exist yet | rejected |
| J. The check compares the mark line with its version left out | `skills/core/SKILL.md` *The rule a mechanism is kept against*: a script holds a gate on a fact it reads exactly, and a line matched with a part left out is a pattern; the body still differs by which copy composed it, so two correct bodies for one commit exist | rejected |
| K. The orchestrator runs this tree's `bin/seal pr-body` in this repository | Holds only here; a user's repository composes with the installed plugin and checks with the tag its workflow pins, so every plugin update re-pins the workflow or turns the arm red | rejected as the fix; this repository still writes this work item's own body with the tree's copy, since the installed 0.35.1 writes the tag address (*Operational impact*) |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* item 2, and the `tests/skills/test_pr_body.py` case of item 5 | the new case seen red against the current `_check` on a body lacking the mark line and its blank line (design G12's shape), then green; `tests/skills/test_pr_body.py` green | 7252125d |
| 2 | *Scope* item 1, the `chain_check.py` sentences of item 4, and the `tests/skills/test_chain_check.py` cases of item 5 | each case seen red with the arm absent, then green; `tests/skills/test_chain_check.py` and `tests/skills/test_pr_body.py` green; `tests/behaviour/test_this_repository_passes_its_own_checks.py` green for the marker the check line names | f950b269 |
| 3 | *Scope* item 3, the remaining sentences of item 4, and the work item's `changelog.md` | the `tests/text/test_ci_gives_the_checks_what_they_need.py` pin on `edited` seen red against the template as it stands, then green; `git grep` for the two sentences of *Removes* finds neither; the tree-wide files `CONTRIBUTING.md` *Running the checks* names green | ce06efa7 |
| 4 | *Scope* item 6, and the `changelog.md` sentences it rewrites | the two-manifest case seen red against `_mark_line` as it stands, then green; `tests/skills/test_pr_body.py` and `tests/skills/test_chain_check.py` green; `git grep` for `raw/v` outside the work item's records finds nothing, and for the `templates/setup/config.md` sentence of *Removes* finds nothing; the mark line this tree's `bin/seal pr-body` writes for a sealed fixture equals the one `chain_check.py` composes | 429582c3 |

## Overlap with the release

The spawn named no other work item running beside this one: #1439 to #1444
have merged into the base at `1af09327`. The owner added #1453 to the release
after this frame was committed; its frame stands at `b0c63c8c` in
`seal/threads/1794188289-the-body-reads-in-the-teams-language/frame/`, and
its plan orders this work first.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1453 | `skills/code-review/scripts/pr_body.py`: this work moves the composition and the comparison into `compared` and changes the mark line; #1453's phase 2 changes what that function composes as the first part, with the language rows refused where absent and a `pr.<lang>.md` placed first. `tests/skills/test_pr_body.py` and `tests/skills/test_chain_check.py`: this work's cases write a `config.md` with the mark row; #1453 adds its two language rows to every fixture that runs the command. `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*: this work adds what a red body arm asks; #1453 rewrites the `pr.md` paragraphs | #1452 | `compared` is the structure #1453's phase 2 edits, and that phase's refusal turns every fixture of this work's arm red until the rows are added, so #1453 builds its phase 2 on the merged base and pays one pass over the fixtures; the reverse order would merge this work's function over a changed first part and edit the fixtures in both items. #1453's plan states the same order (its *Overlap with the release*) |

## Operational impact

No version move: #1443 moved it. No new dependency. A repository that
installed `hygiene.yml` from an earlier release runs no arm until it
re-installs the workflow or edits its `types:` line and the pinned tag
(design *Data & interfaces*). In this repository `edited` is already in
`.github/workflows/hygiene.yml`, so the arm runs on the next body edit.

The mark's address changes form (design *Scope* item 6). Bodies already on
GitHub keep their tag addresses, which render while their tags exist. In
this repository the installed plugin is 0.35.1 until the release carrying
this work is installed, and it writes the tag address, while `hygiene.yml`
runs the tree's `chain_check.py`, which composes the new one. So the
orchestrator writes this work item's own pull request body, and every body
of this repository until that install, with the tree's `bin/seal pr-body`
after the seal; the sealer's `seal pr-body --check` is unaffected, since it
runs before the verdict and composes no mark. In a user's repository the
arm and the new address arrive in one release, so the one re-install of
the workflow the arm already asks for covers both, and a later plugin
update needs none.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-09 | The mark line's address is decided by the framer before phase 4, and the framer decided an address without the version (*Alternatives considered* H, *Scope* item 6). | The phase 2 crafter found that the version in the address is the composing copy's: the installed plugin writes the body and the tree's or the pinned tag's `chain_check.py` composes the line it compares, so the arm would refuse every pull request whose two copies differ, and running `seal pr-body` again would not repair it. | `skills/core/SKILL.md` *The rule a mechanism is kept against*; `skills/implement/orchestration.md` *A decision made after the frame is committed is folded* |
| 2026-11-09 | The phase hand-backs' statements are folded by the framer with the address decision: `compared` returns `(note, causes)`, the body arm's refusal sits at the work item's directory line 0 with the body's line in its message (Q1 answered (b)), the `ruff.toml` rows and the `Test_main` cases are departures written into *Scope*, and *Technical context* stays as dated. | The crafter of phases 1 to 3 named each statement its build contradicts in a frame file. | `skills/implement/orchestration.md` *A decision made after the frame is committed is folded*; `agents/framer.md` *Rules* |
| 2026-11-09 | The overlap with #1453 is written in *Overlap with the release*, and #1452 merges first. | #1453 was added to the release beside this work item and rewrites the first part `compared` composes. | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
| 2026-11-09 | Round 1's *Not judged* row on a bot or integration that rewrites the body after the pull request opens gets no limit sentence and no framer spawn. | The shape is outside the workflow's flow: the orchestrator writes the body from `seal pr-body`, and a rewritten body is repaired the way any drifted body is, by that command and one `gh api -X PATCH`, which the arm's refusal already names. | `skills/core/SKILL.md` *The rule a mechanism is kept against* |
| 2026-11-09 | The fix pass's statement that *Scope* item 2 and *Data & interfaces* name `compared` without `base` is folded by the orchestrator, with no framer. | It records what the fix of round 1's finding 1 changed in the signature, not what the work is. | `skills/implement/orchestration.md` *A decision made after the frame is committed is folded* |
| 2026-11-09 | The pull request's title takes `fix:`, and the kind that came closest is `feat:`. | The work repairs a step the workflow already required, the seal mark in a sealed pull request's body, which six pull requests of this release lacked; the arm it adds holds that existing step, and the mark's address changes so the arm can read it across releases. | `skills/commit-pr-convention/SKILL.md` *Commit messages* |
