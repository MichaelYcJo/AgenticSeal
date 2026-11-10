# Guarantee: 1794271935-the-releasing-documents-describe-the-note-twice

The audit read the tree at `a098f4f55` against the base
`origin/release/v0.37.1`, which `release/v0.37.1@{upstream}` resolves to
`c5dad8d8c` (executed). The branch forked at `8657297d5`, so every diff below
is `git diff c5dad8d8c...HEAD`. `trail/gate.md` names `f1cd47377 against
c5dad8d8c`. That commit resolves, HEAD descends from it, and the one commit
after it, `a098f4f55`, touches only `trail/gate.md` of this work item
(executed, `git log --no-merges --name-only f1cd47377..HEAD ^c5dad8d8c`).
`seal pr-body seal/threads/1794271935-the-releasing-documents-describe-the-note-twice --body <scratchpad>/1794271935-the-releasing-documents-describe-the-note-twice/pr-body.md --check`
exited 0 (executed). The issue body was read with `gh issue view 1490`
(executed). No `seal/parity.json` is tracked (executed, `git ls-files`), and
`seal/config.json` names English for both language keys, so no
`pr.<lang>.md` is owed.

The `seen red` claims were re-run in a clone at `a098f4f55` under the
scratchpad, with the changed file restored from `c5dad8d8c` or the one guard
edited, and restored after each run. `git status --short` printed nothing
before the clone was removed.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The hold's case fails against the document before the change (`seen red`) | `trail/phases/phase-1.md:14-16` | `docs/releasing/branch-and-release.md` restored from `c5dad8d8c`, then `bin/test tests/text/test_the_release_tail_does_not_end_at_the_tag.py -q -p no:xdist -k test_the_listing_s_hold` | holds: exit 1, `test_the_release_tail_does_not_end_at_the_tag.py:175`, "*Cutting a release* does not say the listing is on hold" (executed) |
| The hold's case goes red on its date line with the date taken out of the hold's sentence (`seen red`, the one the plan's *Phases* row 1 names) | `trail/phases/phase-1.md:17-27`; `frame/plan.md` *Phases* row 1 | HEAD's document with "2026-11-08" replaced by "November" through the `Edit` tool, then the same command | holds: exit 1, "the hold's sentence carries no date", the date guard's own message (executed) |
| The census goes red with `docs/layout/the-record-layout.md:126` still citing *2b* (`seen red`) | `trail/phases/phase-2.md:24-32` | `docs/layout/the-record-layout.md` restored from `c5dad8d8c`, then `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:xdist -k every_cited_section` | holds: exit 1, 2 failed, each naming `docs/layout/the-record-layout.md:126 cites ... *2b*` and no other line (executed) |
| The census pins `finding_counts.py`'s `--help` citation (`seen red`) | `trail/phases/phase-2.md:34-42` | `*Settle what earlier releases "` replaced by `*2b. Settle what earlier releases "` in `.github/scripts/finding_counts.py` through the `Edit` tool, then the same census command | holds: exit 1, 1 failed, `.github/scripts/finding_counts.py:184 cites ... *2b. Settle what earlier releases left behind*` (executed) |
| `--help` prints the citation of the settle section | `trail/phases/phase-2.md:141-142`; `frame/plan.md` *Operational impact* | `python3 .github/scripts/finding_counts.py --help` at `a098f4f55` | holds: prints "Print the four numbers of `docs/releasing/release-checklist.md` *Settle what earlier releases left behind* per released work item." (executed) |
| The narrow run of the modules the plan's two phase rows name passes | `frame/plan.md` *Phases*; `trail/phases/phase-1.md`, `phase-2.md` | `bin/test` on the eleven modules the two rows and the fix name (`test_the_release_tail_does_not_end_at_the_tag`, `test_the_release_seal_is_drawn`, `test_a_release_publishes_its_note`, `test_a_cited_section_stands_in_its_file`, `test_docs_line_wrap`, `test_the_windows_leg_runs_in_shards_that_make_the_whole`, `test_finding_counts`, `test_publish_release_note`, `test_the_direct_answer_owes_the_sealers_record`, `test_a_release_is_sized_by_a_criterion`, `test_release_hygiene`) `-q` at `a098f4f55` | holds: 241 passed, 1 skipped, exit 0 (executed) |
| S1: the note's make-up is stated in `branch-and-release.md` alone | `frame/design.md` *User scenarios* S1 | `git grep -n -E 'Thanks to\|counts and the theme\|header of the release' -- docs/releasing` | holds: `docs/releasing/branch-and-release.md:85` alone (executed) |
| S2: no sentence describes a live listing | `frame/design.md` S2; `changelog.md` *Removed* item 2 | `git grep -n -i -E 'portal listing\|picks up each new version\|directory did not get\|#1383\|six hours\|search for the plugin' -- docs/releasing .github/workflows` | holds: no line (executed) |
| S3: no document names `#51` | `frame/design.md` S3; #1490 *Done when* | `git grep -n '#51' -- docs` | holds: no line (executed) |
| S4: no checklist step is cited by number | `frame/design.md` S4 | the S4 path grep, `grep -n -E 'step [0-9]' docs/releasing/release-checklist.md`, and `git grep -n -E '0\. Before starting\|2b\. Settle\|5\. The release pull\|6\. After the merge\|step 2b' -- . ':!seal/threads'` | holds: the first two find nothing; the third lists the census fixture at `tests/behaviour/test_a_cited_section_stands_in_its_file.py:518, 523` and `skills/update/SKILL.md`'s own step 2b at `tests/behaviour/test_release_hygiene.py:1064, 1081` and `tests/behaviour/test_update_reads_the_config_directory_in_use.py:75`, which `frame/design.md` *Scope* puts out of scope (executed) |
| S5: no executed line of the publish workflow changes | `frame/design.md` S5; #1490 *Decided* | `git diff c5dad8d8c...HEAD -- .github/workflows/publish-release.yml`, filtered to changed lines that do not open with `#` | holds: empty (executed); `plugin_directory_check.py` changes one docstring line (read, the diff) |
| `## Removes` row 1 and `changelog.md` *Removed* item 1: the checklist's copy of the note's make-up | `frame/design.md` *Removes* | S1's grep; `docs/releasing/release-checklist.md:273-315` read | holds: the box keeps the commands, the states and the repairs, and cites *Cutting a release* twice (read) |
| `## Removes` row 2: the workflow comment's copy of the header and of the key's values | `frame/design.md` *Removes* | `grep -n -E 'as badges\|alt text\|#1204\|#857' .github/workflows/publish-release.yml` | holds: no line (executed); the comment cites *Cutting a release* (read, diff) |
| `## Removes` rows 3 and 4: the portal-listing sentence, its mechanics, #1383, the search, and the case pinning it | `frame/design.md` *Removes* | S2's grep; `git grep -n 'records_which_kind_of_listing' -- . ':!seal/threads'` | holds: the case stands in no test file; its key stands only in `.test_durations:5973`, which `trail/phases/phase-1.md:92-94` names and leaves for the release's refresh (#1468) (executed) |
| `## Removes` rows 5 and 6: the step numbers and the #1148 history | `frame/design.md` *Removes* | `grep -n '^## ' docs/releasing/release-checklist.md`; `git grep -n 'which removed the records' -- . ':!seal/threads'` | holds: the headings read *Before starting*, *Settle what earlier releases left behind*, *The release pull request*, *After the merge* at lines 11, 35, 130, 252; the #1148 phrase stands nowhere (executed) |
| `## Removes` row 7: `#51` as the open log | `frame/design.md` *Removes* | S3's grep | holds (executed) |
| Each quote of `pr.md` stands at its coordinate | `pr.md` | a whitespace-collapsing substring check of each of the seven quotes against `changelog.md` and `frame/plan.md` | holds: seven of seven (executed) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| The design | The note's make-up stays in `branch-and-release.md` *Cutting a release*; the hold is stated once there; the checklist's headings carry no number; `#51` becomes the open `flow-baseline` issue; the `dist` job and the directory box keep running | #1490 *Change* and *Decided*, as the body reads now; the diff; the issue's choice of unnumbered headings, which #1490 *Change* bullet 4 records as "decided at the frame, 2026-11-10, in place of renumbering" | none. The issue body was edited to that wording after the frame (spawn prompt; read); `docs/releasing/issues-and-milestones.md:328-330` cites `skills/implement/orchestration.md` for folding a decision into the body, and `routing.md` records the owner's `agentic` answer |
| The build | Phase 1 delivers *Scope* items 1 to 4, with two departures: the workflow's `dist` sentence and the title fallback as a state; phase 2 delivers items 5 to 7, with one departure, the "never close" sentence at `issues-and-milestones.md:192` | the diff; the four `seen red` re-runs above; `frame/plan.md` *Phases*, whose Status cells `55c6e6095` and `c44121bff` each have their `trail/phases/phase-N.md` | `trail/phases/phase-2.md:90-95` calls its path census whole at `c44121bff`, where `tests/conftest.py:215` still cited step 3. Round 1 finding 1 found it, the close in `trail/rounds/round-1.md` corrects it, and `c15f827f2` rewrote both docstrings (read, diff); round 2 read that fix. Resolved, no reason to withhold |
| The last round | Round 2 at `9c00157f6` opens no finding and confirms round 1 finding 1 | the diff of `c15f827f2` (read); every commit after `9c00157f6` touches only `seal/threads/1794271935-the-releasing-documents-describe-the-note-twice/` (executed, `git log --name-only`) | none. Round 1's `## Not judged` row on "telling the plugin directory" (`release-checklist.md:262-263`) stays the owner's: #1490 asks that the checklist "no longer asserts a live listing", and the sentence it quoted for that, "The plugin's listing is a portal listing … picks up each new version from `dist`", stands nowhere (executed, S2). The directory box says the listing is on hold. Round 2's row on `tests/test_conftest.py` matches #1498, which says the two cases fail by test order and that the broad gate passes them (read, `gh issue view 1498`). They also failed when the module ran alone at `a098f4f55` here (executed), and this diff does not touch `tests/censuses.py` |
| The changelog | Five *Changed* items and three *Removed* items, as the diff makes them | the diff, line by line (read); the S1 to S5 and `Removes` re-runs above | none |
| The orchestrator's part of the pull request body | Seven quotes with coordinates, and `Closes #1490.` | `changelog.md` and `frame/plan.md` at their coordinates (executed); `seal pr-body --check` exit 0 (executed); `routing.md` *Why this way*, whose grounds name the two documents, the workflow comment and the renamed sections that scripts and tests cite, which is what the diff changes (read) | none |

Not in the tree, and owed by the orchestrator: #1464's body still cites
`docs/releasing/release-checklist.md` *2b*. `frame/plan.md` *Operational
impact* names it for `gh issue edit 1464` after the merge (read).

```seal
target: a098f4f55 against c5dad8d8c
Verdict: sealed
```
