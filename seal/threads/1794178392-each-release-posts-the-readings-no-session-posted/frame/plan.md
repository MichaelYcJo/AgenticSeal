# Implementation Plan: 1794178392-each-release-posts-the-readings-no-session-posted

## Technical context

The tree as read at `1f7aaa66`.

The work builds on `skills/verify/scripts/session_cost.py`:

- `projects_dir` (line 84) resolves the config directory's `projects/`.
- `subagent_transcripts` (line 1460) lists a run's agent files.
- `measure_segments` (line 1757) and `report_segments` (line 2668) give the
  `--segments` rows. Each row carries its transcript's path relative to the
  run, or the file's name for an agent's own file.
- `open_log` (line 2962) resolves the label to one open issue.
- `post` (line 3031) answers the five states and comments with
  `--body-file`.
- `emit` (line 3106) captures the report and swaps the given path for its
  file name before posting.
- `main` (line 3169) parses the flags.
- `report` (line 2108) prints the plain reading. Its `slowest` list and its
  `other` note are the only lines in the module that print command text.

The module imports nothing from `lib/`. Reading `Branch` through
`lib/routing.py#parse` (line 167) means adding the import path the way the
other `skills/*/scripts` that read `lib/` do. The crafter picks that way and
names it in the phase record.

What breaks in six months:

- **The orchestrator skips the release step.** The roll then names the empty
  log, as it does today (#198). Nothing is lost that the current design keeps.
- **A harness moves the spawn prompt out of an agent file's first `type: user`
  entry, or moves `subagents/`.** The mode then finds nothing and posts that
  no transcript on this machine names the work item. The walked count above
  the reading is what tells "walked 0" from "walked 1,700, none named it".
  That count is why scope item 4 prints it.
- **A session posts with a plugin older than this change.** Its comment holds
  no `# <file name>` line, so the release posts those segments a second time.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Post from the release workflow on CI (`publish-release.yml` or `close-issues-on-release.yml`) | The runner holds no transcript (#1367: they live in the config directory of the machine that ran the work), so every log would get "no transcript on this machine" and no reading | rejected |
| Post from the settle (`seal settle`) | The settle ran once over 0.30.0 to 0.32.5 and once over 0.32.6 to 0.34.1. By then each of those releases' logs is closed, and the roll has already said each one closed empty. Transcripts also age by a settle's distance (the oldest here is from 2026-10-13) | rejected |
| Post at release-checklist step 5, before the owner's merge, one command per work item the release ships | The orchestrator forgets the step. The roll then says the log closed empty, as today. The step sits at the one point every release passes, and the release orchestrator works it down with the release pull request. The settle's `finding_counts.py` step, which a session also runs from a checklist, reached #51 at every settle (ticket body) | chosen |
| Replace the in-run post: drop the shipped instruction and post every segment only at the release | `skills/verify/orchestration.md` ships to every repository, and the release step is this repository's checklist. The roll script that keeps a log alive is `export-ignore` (`.gitattributes`), so this repository's own. A user repository that keeps a log would lose its only path for posting. The sentence a session writes while the segment is fresh would also go | rejected. The structure is kept because a user repository gets no release step from this plugin. Premise checked in `.gitattributes`: `roll_flow_measurement_issue.py` and `.github/workflows/` are `export-ignore`, and the release checklist that ships under `docs/releasing/` names this repository's own tags and workflows. Its deadline goes (`frame/design.md` `## Removes`) |
| Post every segment at the release with no check against the log | In the 14 of 25 logs where sessions did post, every one of those segments would appear twice | rejected for scope item 3 |
| Tell posted from unposted by an agent id found anywhere in a comment's text | It reads prose: an id quoted in a sentence would count as a posted reading | rejected. Only the `# <file name>` line the script writes is read |
| Attribute by time window: every run since the open log was created, one comment per run | It cannot say which work item's transcripts are missing, so done-when (2) is met only when every one is missing. It also posts settle and investigation runs | rejected |
| Attribute by each transcript's `gitBranch` field | 377 of 1,046 agent transcripts here record `main`, because sessions start from the main checkout (probe in `frame/design.md` `## Grounding`) | rejected |
| A prompt naming several work items is attributed to none of them | 27 of 425 prompts naming a work item directory name more than one. Their readings would never be posted | rejected. Each work item asked about takes it, and scope item 3 stops a second post |
| A `release-report` row on the release pull request naming an empty open log | It catches what #198's sentence catches, only before the merge. It adds a mechanism with no catch record yet | rejected. Revisit if the step-5 command is missed |
| Post plain readings per segment instead of `--segments` rows | One full reading per segment puts 20 to 40 lines per agent into one comment, where a row is one line. A four-round work item could approach GitHub's comment size limit (`unverified`; the limit was not measured here) | rejected |
| Remove the paths from a posted body's command text, and keep the rest of the command | A path is one spelling among many: a relative path, `~`, a variable that expands to a path. Command text also carries heredoc bodies and prompts, which `CONTRIBUTING.md` *House rules* forbids sending as well. A script that removes paths would be guessing at spellings | rejected for *Scope* item 7, which leaves command text out of a posted body |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1 and 7, and the step 2 sentence of *Scope* item 6. It starts after #1440 has merged into `release/v0.36.0` and the branch has merged that in (`frame/design.md` *Scope*, the overlap paragraph) | new cases in `tests/skills/test_session_cost.py` for the plain reading, `--spawns` and `--segments` bodies, and for a body that would have carried a command with an absolute path. Each is shown red against the current `emit` and `report`. The module's other cases stay green, run narrow by the crafter. The suite is `unverified` until the orchestrator's broad gate | f886ff97 |
| 2 | *Scope* items 2, 3, 4 and 5, and the rest of *Scope* item 6 | new cases in `tests/skills/test_session_cost.py`, one per scenario of `frame/design.md` *User scenarios & acceptance* that names this file, each shown red first. A pin in `tests/text/test_a_segment_feeds_the_flow_log.py`, shown red with the sentence removed. A read-only run of `--work-item` without `--post` on `seal/threads/1794128303-the-plugin-ships-two-hooks-again` and on this work item's directory, quoted in `trail/phases/phase-2.md` | e3f07e9c |

## Operational impact

- **No new dependency, environment variable or config row.**
- **0.36.0's own release runs the tree's script.** At that release the
  installed plugin is 0.35.1, and it has no `--work-item`. The release
  orchestrator runs `python3 skills/verify/scripts/session_cost.py
  --work-item <dir> --post --says <file>` from a checkout of
  `release/v0.36.0`. From the next release on, `seal cost` has it.
- **One release of double posts.** Comments posted during 0.36.0's run by the
  installed 0.35.1 hold no `# <file name>` line. So the 0.36.0 release step
  posts those segments again into log #1438.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-09 | Phase 1's hand-back named four frame statements as contradicted by HEAD. The orchestrator read the frame against HEAD and rewrote three in `frame/design.md`: *Scope* items 6 and 7 now name `README.ko.md` beside `README.md`; *Data & interfaces* says `main` passes the command-free form and `analyse` adds `family`; and the overlap paragraph says #1443 and #1444 have merged, and that neither the #1441 branch nor the #1442 branch touches this item's files. The fourth, the function line numbers in *Technical context*, stays. | `CONTRIBUTING.md` asks both READMEs to move together. Phase 1 chose `main` for the switch (`trail/phases/phase-1.md`). `git diff --name-only` of each sibling branch was executed. *Technical context* is dated to `1f7aaa66`, and its line numbers hold there (`report` at 2108, `emit` at 3106, executed). | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
| 2026-11-09 | Phase 2's hand-back named six frame statements HEAD contradicts. The orchestrator rewrote them. In `frame/design.md`: the *A real work item* scenario gives the transcripts each run found; *Scope* item 4 says a row is named by its transcript's file name; *Scope* item 5 says a found log whose comments cannot be read posts nothing under `--post` and exits 1; *Scope* item 6 names the `Sends` cell; and *Removes* rows 3 and 4 cite the second and fourth `change`. In `frame/questions.md`, Q1 is closed as answered by the work. | Each is phase 2's build or measurement at `7e4430b1` (`trail/phases/phase-2.md`). The ordinals were checked against `## Rule changes`, where the premise and the remembering sentence are its second and fourth entries. | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
| 2026-11-09 | The pull request's title takes `feat:`, and the kind that came closest is `fix:`. | `seal cost --work-item` is a mode that did not exist, and a release step that runs it every release; the `# <file name>` line and the command-free posted body change what `--post` writes, which the new mode reads. | `skills/commit-pr-convention/SKILL.md` *Commit messages* |
| 2026-11-09 | Round 1's finding 2 names the *A real work item* scenario's count for the second run, which left out #1443's framer; the orchestrator rewrote the scenario to the three transcripts phase 2's run found, and the phase 2 fold row's clause to the transcripts each run found. | `trail/phases/phase-2.md` quotes three transcripts for this work item's directory, and #1443's framer prompt lists #1439 as a sibling (`trail/rounds/round-1.md`). | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
