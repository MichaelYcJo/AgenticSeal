# Design: 1794178392-each-release-posts-the-readings-no-session-posted

## Grounding

The tree as read at `1f7aaa66`.

The ticket is #1439 as filed. The orchestrator read its comments on
2026-11-09 and found none. This framer read the comment count again with
`gh issue view 1439 --json comments` and got 0 (`executed`).

| Policy clause | What it fixes for this work |
|---|---|
| `skills/core/SKILL.md` *The rule a mechanism is kept against* | The work adds two things: a mode that posts readings, and one line form in a posted body. `## Removes` names what goes in return. The script reads only its own `# <file name>` line, in the one spelling it writes. It reads a spawn prompt only to decide what to post, never to block. |
| `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest* | What a reading says stays the session's sentence. The new mode keeps `--post`'s refusal without `--says` (`skills/verify/scripts/session_cost.py#emit`). |
| `skills/verify/orchestration.md` *Measure the segment, and feed the flow log* | A segment's reading goes to the one open `flow-measurement` issue, found by its label. Opening an issue is not a session's act. The tracker can be in five states, and `session_cost.py#post` answers each one. The new mode reuses `open_log` and `post` as they stand. |
| `docs/running/measuring-a-run.md` *Where a reading goes*, and `CONTRIBUTING.md` *House rules*, bullet **The plugin ships two hooks, and neither writes outside the repository** | Nothing posted may carry repository contents, paths or prompts, so a transcript is named by its file name. Two lines of the plain reading print command text: the `slowest` list and the `other` note's "Slowest command charged there" (`session_cost.py#report`, `read`). `report_spawns` and `report_segments` print none (`awk` over their lines, `executed`). Command text can hold an absolute path, a heredoc's body or a prompt. So a posted body carries no command text (scope item 7). |
| `.github/scripts/roll_flow_measurement_issue.py` docstring, and #198 | The release's push to `main` closes the open log and opens the next one. Where the log holds no comment, the roll says it closed empty. So posting what nobody posted has to happen before the release pull request merges. |
| `docs/releasing/release-checklist.md` *5. The release pull request* | The orchestrator opens the release pull request after the last pull request into `release/vX.Y.Z` has merged, and the owner's one required act is the merge. That step happens at every release, on the machine where the orchestrator runs, so it is where the posting goes. |
| `skills/settle/SKILL.md` *When it runs*, and the spawn prompt's note that settles ran over 0.30.0 to 0.32.5 and over 0.32.6 to 0.34.1 | A settle does not run at every release, and the logs of the releases it covers are already closed by the time it runs. The settle is not the home. |
| `.github/workflows/publish-release.yml` and `.github/workflows/close-issues-on-release.yml` (`read`) | Both run on `ubuntu-latest`. Transcripts live in the Claude Code config directory on one machine (#1367, `session_cost.py#projects_dir`), so no CI step can read them. |
| #51's body, as the spawn prompt quotes it (`unverified`; the orchestrator answers it) | The rolling log is thrown away by the release that ships it, and readings that span versions belong in `flow-baseline`. This work changes neither. |
| `lib/routing.py` (`BRANCH`, `parse`) | A work item's branch is the `Branch` row of its `routing.md`, read through this one reader. |
| Latest release `v0.35.1`, *Process changes* (`gh release view`, `executed`) | #1367 made transcript readers follow `CLAUDE_CONFIG_DIR`. The new mode finds transcripts through `projects_dir()`. |
| `tests/skills/test_session_cost.py#test_the_posted_body_does_not_carry_the_transcripts_path` (`read`) | An earlier round decided that a posted body keeps the transcript's file name: "a reading that names no file is a reading nobody can place". Scope item 1 extends that to the plain reading, which names no file today. |

Probes. Each one is `executed`, read-only, against this machine's config
directory and the tracker, on 2026-11-09:

- Transcript layout. A spawned agent's transcript is
  `projects/<cwd slug>/<session-id>/subagents/agent-<id>.jsonl`, with an
  `agent-<id>.meta.json` beside it. The first `type: user` entry of an agent's
  file holds its spawn prompt. Found with `ls` and a `python3 -I` read of the
  first entries.
- The `gitBranch` field cannot join a transcript to a work item. Of 1,046
  agent transcripts under this repository's project directory, 377 record
  `main` on their first entry. Sessions here start from the main checkout and
  work in worktrees by absolute path. Found with `python3 -I`, counting the
  first `gitBranch` of each file.
- Spawn prompts name the branch. Of the 498 `agentic:crafter`,
  `agentic:framer`, `agentic:proofer` and `agentic:sealer` prompts under this
  repository's project directory, 497 name a branch of the form
  `<type>/<n>-<slug>`. The `seal/threads/<id>` directory name is in 410 of
  them. Found with `python3 -I`, grouping by `.meta.json`'s `agentType`.
- One prompt can name several work items. 27 of the 425 prompts that name a
  `seal/threads/<id>` directory name more than one. Found with the same read.
- The ticket's machine-locality case is real today. A walk of all 1,744 agent
  transcripts under every project directory finds no spawn prompt naming the
  directory or the branch of 0.35.0's `1794128303-the-plugin-ships-two-hooks-again`
  or 0.35.1's `1794142458-config-dir-readers` and
  `1794142459-parity-reads-original-forward`. The only exceptions are this
  release's own prompts, which quote them. A `grep -rl` for those slugs over
  every `*.jsonl` agrees. Those runs' transcripts are not on this machine.
- Retention. The oldest top-level transcript under this repository's project
  directory is from 2026-10-13, and the oldest agent transcript is from
  2026-10-08 (`stat`). Claude Code's own retention rule is `unverified` here,
  and a measurement answers it (`frame/questions.md` Q2).
- The logs. `gh issue list --label flow-measurement --state all` lists 40
  logs, #842 to #1438. Each log the ticket names as empty holds one comment,
  and the roll's #198 sentence is that comment (#1434 read whole). The open
  log is #1438, created 2026-11-08 with no comments. Logs open and close
  within one to five days of each other.
- The release's work items. `git diff --name-only --diff-filter=A
  v0.35.0..v0.35.1 -- 'seal/threads/*/routing.md'` lists 0.35.1's two work
  items, and the same over `v0.34.1..v0.35.0` lists 0.35.0's one. `git
  describe --tags --abbrev=0 origin/main` prints `v0.35.1`. This is the
  listing the checklist rule in `## Rule changes` uses.
- What sessions post. #1414's and #1392's comments are plain readings of one
  agent file each. They print no file name. Their `slowest` lines carry
  command text with absolute paths (`gh issue view --json comments`).

## Scope

In:

1. **A posted reading names each transcript it was read from.** Inside its
   fence, `--post` writes one `# <file name>` line for each transcript the
   reading was taken from, before the report. That is the file given, and for
   `--segments`, each agent file a row was measured from. The line holds the
   file's name, never its path. What is printed locally does not change.
2. **`seal cost --work-item <dir>` finds a work item's segments.** It reads
   the `Branch` row of `<dir>/routing.md` through `lib/routing.py`. It walks
   every agent transcript under every project directory of `projects_dir()`.
   It takes each transcript whose spawn prompt (its first `type: user`
   entry) contains the directory's name or the branch. A prompt that names
   several work items is taken by each one asked about. Scope item 3 keeps it
   from being posted twice.
3. **It leaves out what the open log already holds.** It reads every comment
   of the one open log its `--label` resolves to, every page of them. It drops
   each transcript whose file name stands on a `# <file name>` line inside a
   fence of one of those comments. A comment without such a line names
   nothing. A comment posted before scope item 1 shipped holds no such line,
   so it names nothing.
4. **It prints, or posts, what is left.** The reading opens with four counts:
   the transcripts walked, the ones that named the work item, the ones already
   in the log, and the ones in this reading. Under the counts come the
   `# <file name>` lines of scope item 1. Then one `--segments` row per segment
   follows, one per slice for a resumed agent, each named by its transcript's
   file name. Where no transcript names the work item, the reading says that no
   segment transcript on this machine names the directory or the branch. With
   `--post`, that reading is posted. Where every transcript that named it is
   already in the log, the mode says so, posts nothing and exits 0.
5. **The log's states are answered as `post` answers them.** `--post` needs
   `--says`. A label with no history and an unreadable lookup post nothing and
   exit 0. A closed log, or more than one open log, is named and exits 1.
   Without `--post`, a log that cannot be read leaves out nothing, and the
   reading says so. With `--post`, a log found whose comments cannot be read
   posts nothing and exits 1, since posting would repeat readings already
   there (`trail/phases/phase-2.md`). `--work-item` refuses to run with a transcript argument,
   `--latest`, `--spawns`, `--segments` or `--json`.
6. **The shipped text says it.** In `skills/verify/orchestration.md`
   *Measure the segment, and feed the flow log*, three paragraphs change. The
   paragraph opening **The command does not make anybody run it.** becomes
   the paragraph stating that the release posts what no session posted,
   through `--work-item`. Step 2 states scope item 1's line. The paragraph
   opening "The orchestrator does this before the next segment spawns" keeps
   "never as a question" and loses its deadline. `README.md` *What runs on
   your machine* and the same table of `README.ko.md`, which
   `CONTRIBUTING.md` asks to move with it: the `seal cost --post` row's
   `When` cell names the release step, its `Sends` cell says `--work-item`
   first reads every comment of the open log with `gh api --paginate`, and
   the command table gains a `seal cost --work-item <dir>` row. These are direct edits, because none of
   the files is in the policy root.
7. **A posted body carries no command text.** In the body `--post` captures,
   the `slowest` list gives each call's seconds and its family (`git`,
   `test`, `read` and the rest), and leaves out the command. The `other` note
   keeps its sentence and leaves out the quoted command. What is printed
   locally does not change. The `seal cost --post` row of `README.md` and
   of `README.ko.md` says the comment holds no command text. This closes the path leak the frame found
   in #1414's posted comments, which this work would otherwise post at every
   release. Leaving the text out is chosen over removing paths from it,
   because a path is one spelling among many, and command text also carries
   heredoc bodies and prompts (`frame/plan.md` *Alternatives considered*).

The policy root's two documents change through `## Rule changes`, which the
settle writes. Until then, the release orchestrator reads them as the policy
in force (`skills/implement/SKILL.md` *Document layout — two roots, three
lifetimes*).

Out:

- **Posting into logs that are already closed** (#1189 to #1434). The ticket's
  done-when asks for a step that runs from now on. The transcripts of the
  0.35.x items are not on this machine anyway (probes above).
- **The orchestrator's own `--spawns` reading and the run-level table** of
  the same section. One orchestrator session runs several work items, so its
  transcript belongs to no single one. The ticket counts segment readings.
  The run-level table is built from records as well as transcripts.
- **A row on the release pull request's `release-report` naming an empty
  log.** It catches what #198's sentence catches, only earlier, at the cost of
  one more mechanism (`frame/plan.md` *Alternatives considered*).
- **The version move**, which the orchestrator gives to another item.

**Where this meets the release's other items.** #1440 merges first; its plan
(`03cbad55`, as the orchestrator reads it) states that order, and the
orchestrator takes it. #1440 removes `SEGMENT_BARS`, `segment_kind`,
`report_grades`, the rows' `kind` and `bar` keys, and the plain reading's
batching advice in `session_cost.py#report`. Scope item 4 reuses
`report_segments`' rows and depends on no bar, so phase 2 is unaffected.
Scope item 7 edits `report`'s `slowest` list and `other` note. Those sit just
above the batching advice #1440 removes. So phase 1 starts from a branch that
has merged `release/v0.36.0` after #1440 landed there. Both items add cases
to `tests/skills/test_session_cost.py`. Since #1444 (`c7bb14ca`), no work
item commits `.test_durations`; the release refresh does. #1443
(`e244aa49`) and #1444 have merged and touch no file this item touches, and
the branches of #1441 and #1442 change none either (executed on 2026-11-09:
`git diff --name-only` of each branch against `release/v0.36.0`).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A plain reading is posted | Given one agent's transcript and one open log, when `seal cost <file> --post --says s.md` runs, then the comment's fence opens with `# <file name>` and no line carries the file's directory | a case in `tests/skills/test_session_cost.py`, shown red against the current `emit` |
| A posted body holds no command | Given a transcript whose slowest call and whose costliest `other` call each carry an absolute path, when `seal cost <file> --post --says s.md` runs, then the body holds neither path nor either command, the `slowest` lines give seconds and family, and the printed report without `--post` still shows the commands | a case in `tests/skills/test_session_cost.py`, shown red against the current `report` |
| A run's segments are posted | Given a run transcript with two agent files beside it, when `--segments <run> --post` runs, then the fence names the run's file and both agent files, one `# ` line each | a case in the same file, shown red first |
| Nothing was posted for a work item | Given a work item directory whose `routing.md` names branch B, and two agent transcripts under a temporary `CLAUDE_CONFIG_DIR`, one naming the directory and one naming B, and an open log with no comments, when `--work-item <dir>` runs, then both rows print, and with `--post` one comment holds both `# ` lines | a case with fixture transcripts and the `run_gh` stub, shown red first |
| Part of it was posted | Given the same work item and a comment on the log whose fence holds `# <one of the two names>`, when `--work-item` runs, then only the other row prints and the counts say one is already in the log | a case, shown red with the comment reader removed |
| All of it was posted | Given both names in the log's comments, when `--work-item <dir> --post` runs, then nothing is posted, the output says so, and the exit is 0 | a case |
| A prompt names something else | Given a transcript whose spawn prompt names neither the directory nor B, when `--work-item` runs, then it is not counted as naming the work item | a case |
| No transcript on this machine | Given no transcript naming the directory or B, when `--work-item <dir> --post` runs, then one comment is posted saying no segment transcript on this machine names the directory or the branch, under the session's sentence | a case, shown red first: done-when (2) |
| The log is missing or ambiguous | Given each of the label's states (no history, unreadable, closed, more than one open), when `--work-item --post` runs, then the outcome and exit code match `post`'s for that state | cases reusing the `Test_post` stubs |
| A refused combination | Given `--work-item` with `--json`, `--segments`, `--spawns`, `--latest` or a transcript, then the parser refuses and names both flags | a case |
| A real work item | Given this machine, when the crafter runs `--work-item` without `--post` on `seal/threads/1794128303-the-plugin-ships-two-hooks-again` and on this work item's directory, then each reports the transcripts that name its directory or branch: at `7e4430b1` the first finds two, this release's framers of #1439 and #1442, whose spawn prompts quote that directory, and the second finds this release's framer and crafter segments | an `executed` read-only run, quoted in the phase record |
| The text says it | Given `skills/verify/orchestration.md`, the section names `--work-item` and the `# <file name>` line, and still holds "never" and "question" | a case in `tests/text/test_a_segment_feeds_the_flow_log.py` shown red with the sentence removed, then the proofer's reading |

## Data & interfaces

`seal cost --work-item <dir> [--post --says <file|->] [--label <label>]`,
added to `skills/verify/scripts/session_cost.py#main`.

- `<dir>` is a work item directory holding `routing.md`. The match keys are the
  directory's name (`<epoch>-<slug>`) and the `Branch` value `lib/routing.py`
  parses from it. A key matches only as a whole token. `fix/12-a` does not
  match inside `fix/12-a-b`.
- The candidates are every `*.jsonl` under a `subagents/` directory beneath
  `projects_dir()`, read up to their first `type: user` entry.
- The log's comments come from `gh`, every page. Only a line inside a fenced
  block that is exactly `# <name>.jsonl` names a transcript.
- The posted body is `comment_body(reading, says)`, as today. The reading
  opens with the counts, then the `# <file name>` lines, then the rows.
- Exit codes are `post`'s. Exit 0 also covers a run where nothing is due.

`emit` gains the `# <file name>` lines in the captured body only. For the
plain reading and `--spawns`, that is the file given. For `--segments`, it is
the file given plus each row's transcript. `report` gains a way to render the
`slowest` list and the `other` note without command text, and `main` passes
it for the captured body alone, because `emit`'s render function takes no
arguments and only `report` prints commands. `analyse` gives each `slowest`
row its `family`, which `--json` then carries as one more key.

## Rule changes

- change
  file: docs/running/measuring-a-run.md
  section: Where a reading goes
  from: so the posted body names the transcript by its
    file name and never by its path.
  to: so the posted body names the transcript by its
    file name and never by its path, and it carries no command text: its
    slowest calls are listed by seconds and family alone, because a command
    can hold a path, a heredoc's body or a prompt.

- change
  file: docs/running/measuring-a-run.md
  section: Where a reading goes
  from: Whichever
    session watched a segment finish is the only party still holding its
    transcript, so that session measures the segment and posts what it found to
    the repository's rolling measurement log, by label rather than by number, so
    the destination survives the log being rolled.
  to: The session
    that watched a segment finish measures it and posts what it found to the
    repository's rolling measurement log, by label rather than by number, so
    the destination survives the log being rolled. The transcript stays on the
    machine that ran the segment after the session ends. So before the release
    rolls the log, the release posts what no session posted, one work item at a
    time. Where no segment transcript on that machine names a work item, the
    comment says so, and the log does not close empty because a session forgot.
- change
  file: docs/running/measuring-a-run.md
  section: Where a reading goes
  from: **Posting a reading is one command, and a command does not make anybody run
    it.**
  to: **Posting a reading is one command, and the release runs it for every
    reading a session did not post.**
- change
  file: docs/running/measuring-a-run.md
  section: Where a reading goes
  from: What
    the command cannot do is make a session remember to run it.
  to: A posted reading names each transcript it was read from, by file name, on
    a `# <file name>` line inside its fence.
    `seal cost --work-item <dir> --post --says <path|->` reads those lines
    on the open log. It posts the readings of the work item's segments that no
    comment names, and it finds a segment by its spawn prompt naming the work
    item's directory or its branch.
- add
  file: docs/releasing/release-checklist.md
  section: 5. The release pull request
  to: **Before the owner merges the release pull request, the orchestrator
    posts the segment readings no session posted, one command per work item the
    release ships.** It lists the work items with
    `git diff --name-only --diff-filter=A $(git describe --tags --abbrev=0 origin/main)..origin/release/vX.Y.Z -- 'seal/threads/*/routing.md'`.
    For each directory listed, it runs
    `seal cost --work-item <that directory> --post --says <file>`. The file
    holds its sentence on what that work item's readings say, read against the
    work item's records. The command leaves out each segment a comment on the
    open `flow-measurement` log already names, and posts the rest. Where no
    segment transcript on this machine names the work item, the comment says
    so. It runs before the merge because the merge's push rolls the log, and
    the roll says a log closed empty when it holds no comment (#198). It runs
    at the release and not at the settle, because a settle can cover several
    releases whose logs have already closed. No CI step can run it, because
    the transcripts are on the machine that ran the work and on no runner.
    check: tests/skills/test_session_cost.py

## Removes

The work adds the `# <file name>` line form and the `--work-item` mode. These
four rows are what goes in return:

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The paragraph saying the command makes nobody run it, and that nothing removes the remembering | `skills/verify/orchestration.md` *Measure the segment, and feed the flow log*, the paragraph opening **The command does not make anybody run it.** | The release step now runs the command for what a session left. The paragraph that replaces it says so (scope item 6). |
| The deadline "before the next segment spawns, or at the latest together with the round or phase record that closes this one: never later" | `skills/verify/orchestration.md` *Measure the segment, and feed the flow log*, the paragraph opening "The orchestrator does this before the next segment spawns" | Its ground was that only the watching session holds the transcript. The release reads the same transcript later on the same machine, so a late post loses nothing. "never as a question" stays, and `tests/text/test_a_segment_feeds_the_flow_log.py#test_the_section_says_it_happens_without_asking` still pins it. |
| The premise that the watching session is the only party holding the transcript | `docs/running/measuring-a-run.md` *Where a reading goes*, first paragraph | The second `change` of `## Rule changes` rewrites it. The settle writes it. |
| "What the command cannot do is make a session remember to run it." | `docs/running/measuring-a-run.md` *Where a reading goes*, the paragraph opening **Posting a reading is one command** | The fourth `change` of `## Rule changes` replaces it with the release step and the `# <file name>` line. |

Framed 2026-11-09 by framer, before the build.
