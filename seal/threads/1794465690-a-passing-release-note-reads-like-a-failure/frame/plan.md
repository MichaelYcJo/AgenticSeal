# Implementation Plan: 1794465690-a-passing-release-note-reads-like-a-failure

## Technical context

The tree as read at `3a75cc23d`.

`.github/scripts/publish_release_note.py` owns the note's header in both of its forms. `header` (`:652-657`) writes the counts in words, and `release_body` (`:757-836`) puts that header first in the note, followed by a blank line. `sealed_header` (`:712-739`) writes what replaces it once the seal has run. Both forms go through `table` (`:643-649`). Every badge is `badge(label, value)` (`:681-696`), coloured from the one pair at `:667-668`.

`.github/scripts/release_seal.py#seal_release` (`:513-592`) loads the publisher as a module and rebuilds `header` from the same pull request list. It refuses unless that text occurs exactly once in the published body, and then replaces it with `sealed_header`'s text (`:557-576`). The labels come from `results` (`:178-218`) and from `publish_release_note.py#count_badges` (`:699-709`).

Both headers become one line of the form `frame/design.md` *Data & interfaces* gives. The `<p>` and `</p>` around each header are what keep the seal's substring count exact. Without them, the seal's header text could also match inside a longer header line (`frame/design.md` S6).

GitHub's renderer was probed at framing (`frame/design.md` G9 to G12). A table cannot lose its border, and a seal standing alone on its first source line splits the badges into one paragraph each. The one-line paragraph keeps `align="left"` and `<br clear="left">` and renders as one block.

Failure scenario of the chosen approach, six months on:

- GitHub's sanitizer drops `align` from `<img>`. The seal would then stand above the badges instead of beside them. The note stays readable, and nothing in this repository would notice until a person looks at a release page.
- A changelog fragment quotes a whole header paragraph with the release's exact counts. The seal would then find the header twice and refuse with a warning, and that release would have no seal. That costs the image and never the counts (`release_seal.py` docstring).
- A badge label added later takes a blue value on a grey label without anyone choosing a colour for it. That is the owner's rule for every other value (issue #1496, *Colours C3*).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. Both headers are one line inside `<p>…</p>`, and the seal keeps its exact-text count and replace (`frame/design.md` *Data & interfaces*) | The scenarios under *Technical context* | **Chosen.** It meets the owner's layout C (G11), and the seal's reading is unchanged (G5). |
| A2. The counts header is a bare one-line `c1<br>c2`, with the same count and replace | A note reading `12 pull requests merged<br>3 issues closed` holds the seal's `2 pull requests merged<br>3 issues closed`. A note with an outside contributors line holds, as a prefix, the header the seal computes without it. In either case the count is 1, so the seal replaces part of a line and leaves a dangling `<br>1 outside contributor`, or it seals counts that disagree with the note. | Rejected. Today the table's tags bound the header, and this approach drops that bound. |
| A3. A bare header, and the seal matches it only as a whole line of the body | The seal's reading changes. The publisher and the seal then have to agree on line structure as well as text, and the spawn asked that the same reading find the header. The `<p>` tags give the same bound inside the text itself. | Rejected |
| A4. HTML comment markers around the header, such as `<!-- header -->` | It adds a mark that has caught nothing, where the `<p>` the rendering needs anyway already bounds the header (`agents/framer.md` *A mark is not the answer to a blocked step*). | Rejected |
| A5. Keep the table and turn its borders off with `border="0"` or `style` | GitHub drops both attributes (G9, and the issue's draft of 2026-11-10). The owner also chose layout C. | Rejected |
| A6. Layout C over several source lines, with the seal's `<img>` alone on the first line | GitHub reads the lone tag as the start of a raw HTML block and wraps each `<img>` in its own paragraph. The two badges of a line then stack, and each `<br>` adds a blank line (G10). | Rejected |
| A7. Replace the find-by-exact-text structure: the seal replaces the note's first paragraph, whatever it says | A note edited by hand after publication would be overwritten. The premise that keeps the structure is that a hand-edited note is left alone. That premise was checked at `release_seal.py:40-50` and is held by `tests/github/test_release_seal.py#test_a_hand_edited_note_is_left_alone_and_nothing_is_uploaded` (G6). | Rejected. The structure stays. |
| A8. Wrap only the counts header in `<p>`, and leave the sealed header unwrapped | It renders the same as A1 (G11, `test_tmp_v1.md` against `test_tmp_v2.md`). Two builders would then hold one shape. | Rejected for one builder |
| A9. One table keyed by label for the labels whose colours differ, plus one pair for every other label | The third scenario under *Technical context* | **Chosen.** It states the owner's C3 as the owner wrote it: four named classes, then "every other value". |
| A10. One table that names all the labels in `frame/design.md` G8, with no default, so that a missing label raises | A label added without a colour raises in the seal job, which turns the error into a warning, so that release has no seal. The cases that use labels made up for the test (`'a & b'`, `'a-b_c d'`) would have to change their labels, and the label escaping would then go untested. | Rejected |
| A11. `release_seal.py#results` hands a colour with each `(label, value)` pair | Colours would be chosen in two files, and the issue asks for one table keyed by label. | Rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 2, 3, and items 5 and 6 for the layout | `tests/github/test_publish_release_note.py` and `tests/github/test_release_seal.py`, run narrowly. S1, S2, S3, S5 and S7 pass. S6 is a new case, seen red against a `header` that writes no `<p>` and `</p>`. | `d5d029827` |
| 2 | `frame/design.md` *Scope* items 4, and 5 and 6 for the colours | The same two test files. S4 is seen red against the `badge` that read the one pair of constants. | `66cfb82b0` |

## Overlap with the release

The spawn named three items: #1516 (`chore/1516-feature-prs-wait-on-the-macos-runner`), #1510 (`refactor/1510-a-segment-counts-for-every-item-its-prompt-names`) and #1494 (`feat/1494-the-orchestrator-polls-ci-by-hand`). Each branch holds only its `routing.md` past `79f815a74` (executed: `git log` and `git diff --stat` per branch). So no frame of theirs is committed, and the files each item changes were read from its issue.

None of them meets this work. This work changes `.github/scripts/publish_release_note.py`, `.github/scripts/release_seal.py`, their two test files and this work item's directory. #1516 changes `.github/workflows/test.yml`, `CONTRIBUTING.md` and the version's files. #1510 changes `skills/verify/scripts/session_cost.py`, its tests and `skills/verify/orchestration.md`. #1494 adds `seal pr-wait` and changes `skills/code-review/orchestration.md`. None of the three issues adds a check that reads the whole tree, or reads the release note.

The merge order is therefore the milestone's, and nothing here argues against it. #1516 merges first, because it carries the version move and settles the matrix every later pull request waits on. This item and #1510 merge after it, each as it is sealed. #1494 merges last. This item needs no change from #1516's merge, since they share no file.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1516 | no shared file | #1516 | It carries the version move (`skills/implement/merge-order.md` *Orchestrator: the order the work items of a release merge in*), and the milestone orders it first |
| #1510 | no shared file | either, as sealed | No plan orders them against each other |
| #1494 | no shared file | #1496 | The milestone orders #1494 last |

## Operational impact

None for a deployer. Nothing migrates, and no environment variable or dependency is added. A note published before this change keeps its table, because the publisher never republishes and the seal edits only a header it generated itself. The first note with the new header is 0.38.0's, written and sealed by the code at its tag. This pull request does not move the version: #1516 does.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-12 | The title takes `feat:` | A reader of every later release note meets a new header: no table, the seal floated beside its badges, and each badge coloured by its label; the issue's *Why it is a feat* gives the same grounds, as #1299, which made the badges, was a feat | `skills/commit-pr-convention/SKILL.md`; issue #1496 *Why it is a feat* |
| 2026-11-12 | Round 1 finding 1 changes the frame: `## Rule changes` operations 1, 2 and 3 are rewritten so that the policy sentence after each `to:` still leans on the sentence it leaned on (operation 2's `from:` widened by one sentence where the proofer's fix asks), and operation 3 says `SEALED`'s dark red label stands beside its value, not under it | Settled as written, `docs/releasing/branch-and-release.md:78`, `:92` and `:98` would follow the new sentences and read with a wrong antecedent (read at e18a067b0); a badge's label stands left of its value | `trail/rounds/round-1.md` finding 1; `skills/implement/fold-and-reframe.md` |
