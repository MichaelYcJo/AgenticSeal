# Phase 2: 1794178392-each-release-posts-the-readings-no-session-posted

## What this phase found

**The frame holds for this phase, read at `7bd317e9` after the fold of
phase 1's statements.** *Data & interfaces* now matches the build: `main`
passes the form without command text, and `analyse` adds `family`.

**`lib/` is imported on first use, through `lib_module`.** The plan left the
crafter to choose the way and name it (`frame/plan.md` *Technical
context*). `lib/routing.py` imports `optin` and `blocks` by their bare names
from its own directory. So `lib_module` puts the plugin's `lib/` on
`sys.path`, the way `skills/implement/scripts/seal.py` does, and then imports
the module by name. It runs only inside `--work-item`, so the plain reading,
`--spawns`, `--segments` and `payload_meter.py --calibrate`, which loads
this module, import nothing from `lib/`. Judged against the plan's sentence
and `lib/routing.py`'s own imports.

**A comment's fenced lines are read through `lib/blocks.py`.** `posted_names`
splits a body with `blocks.gfm_lines` and asks `blocks.fence_only` which lines
are fenced. Only a fenced line that is exactly `# <name>.jsonl` names a
transcript. A comment body is markdown, so the `splitlines` census in
`tests/censuses.py` asks for `gfm_lines`, and `lib/blocks.py` is the one home
of the fence rule. The `gh` error line in `log_comments` is a tool's output
and carries the census's exemption.

**`frame/questions.md` Q1 is answered by the work: `gh api --paginate`.**
`log_comments` asks for
`gh api --paginate repos/{owner}/{repo}/issues/<n>/comments`. `gh` writes one
JSON array per page, one after the other, so the arrays are decoded in turn
with `json.JSONDecoder.raw_decode`.
`test_reads_every_page_of_the_logs_comments` stubs two pages and puts a name
on each. GitHub's default page holds 30 comments, so a log as busy as #1280,
with 76, already spans three pages. The question's row stays for the
orchestrator to close, because this phase writes no frame file.

**A row is named by its file.** The design says a row is named as
`--segments` names a row. `--segments` names an agent's own file by its file
name, because no spawn is in view to join, and that is this mode's case too.
The `.meta.json` beside an agent file holds its `agentType`, and the mode
does not read it, so the transcript stays the one input. The rows print in
the order of the `# <file name>` lines.

**Decision where the design is silent: with `--post`, comments that cannot
be read post nothing and exit 1.** *Scope* item 5 lists the log's states, and
none of them is a log found whose comments then fail to read. Posting there
would treat every segment as unposted, and a reading posted twice is a
comment a person deletes. So the mode refuses, in the direction `post`'s
docstring gives every refusal. Without `--post`, the reading prints
everything and says nothing was left out, as *Scope* item 5 says for a log
that cannot be read.

**The log is looked up once.** `post` takes `found`, `open_log`'s answer
where the caller already asked for it. `--work-item` has to look the log up
before it reads the comments, and the post uses the same answer.
`test_accepts_both_segments_and_posts_them_in_one_comment` counts one
`issue list` call.

**Removed after it survived mutation: a branch that returned before the walk
where the log cannot take a post.** With `--post` and a log in any state but
one open, the branch called `post` before walking the transcripts. Without
it, the mode walks and then calls `post` with the same answer, and `post`
answers each state the same way: no post, and the same exit code. So the
mutant that removed the branch passed every case. The walk it skipped took
0.55 s over this machine's 1,788 agent transcripts. The branch left in
`b3be38b5`. Judged against `skills/core/SKILL.md` *The rule a mechanism is
kept against*.

**Two units moved and changed nothing they print.** `segment_table` holds
`report_segments`' column header and row loop, so `report_work_item` prints
the same table. `said` holds `emit`'s refusal of an empty `--says`, which
`--work-item` asks first, as `emit` does. The module's earlier cases cover
both, and they stayed green.

**`skills/verify/orchestration.md`.** The paragraph opening **The command
does not make anybody run it.** is now **What no session posted, the release
posts.**, with the command in a fence. The deadline paragraph now reads "The
orchestrator posts without asking, never as a question." One sentence
stands: "Where a log is open, the orchestrator takes the two steps as part
of the segment that just finished, not as a follow-up someone might do
later". It still holds for the in-run post, which the plan keeps (*Alternatives
considered*, the "Replace the in-run post" row). The release step catches
what the in-run post missed, and does not replace it.

**Both READMEs say that `--work-item` reads the log's comments.** I read the
range whole after the closing commit, and found that the `seal cost --post`
row's Sends cell listed only `gh issue list` and `gh issue comment`. But
`--work-item` also sends `gh api --paginate` for the open issue's comments,
whether or not it posts. The cell now says so in both editions. Judged
against `CONTRIBUTING.md` *House rules*: both READMEs move together, and
`README.md` *What runs on your machine* names what each command that
reaches a network sends.
`tests/behaviour/test_both_editions_carry_the_same_folds.py`,
`tests/text/test_no_passage_is_pasted_into_a_second_file.py`,
`tests/behaviour/test_docs_line_wrap.py`,
`tests/text/test_a_segment_feeds_the_flow_log.py`,
`tests/behaviour/test_the_release_check_watches_what_ships.py`,
`tests/behaviour/test_chain_hooks_hardening.py` and
`tests/behaviour/test_a_declared_label_reaches_the_tracker.py` passed after
the change: 155 passed.

**Seen red.** The 18 new items in `tests/skills/test_session_cost.py::Test_work_item`
and the new case in `tests/text/test_a_segment_feeds_the_flow_log.py` ran
against `7bd317e9`: `bin/test tests/skills/test_session_cost.py
tests/text/test_a_segment_feeds_the_flow_log.py -q -p no:xdist -k
"Test_work_item or release_posts_what_no_session"`, 19 failed, exit 1. The
18 `Test_work_item` items failed because argparse refused the unknown
`--work-item` with exit 2. The refusal cases first asserted that the message
held `--work-item` and the other flag, and the argparse usage line already
did, so four of them passed. They now assert `--work-item and <flag>` and
fail at `7bd317e9`. The text case failed on its own assertion: `the section
never names \`seal cost --work-item\``. Each case's own guard was shown red
by the mutation runs below.

**Mutation.** `bin/seal mutate skills/verify/scripts/session_cost.py` ran 18
mutants over `0a52c24b`, using `bin/test tests/skills/test_session_cost.py
-q -x -p no:xdist -k Test_work_item`. Seventeen came back red:

- each side of the whole-token match removed;
- the spawn prompt read past its first user entry;
- every line of a comment read, not only its fenced ones;
- a fenced line matched by search, not as the whole line;
- a page's comments replacing the last page's;
- `--paginate` dropped;
- comments that cannot be read no longer refused with `--post`;
- the all-in-the-log stop removed;
- the none-found sentence removed;
- the already-in-the-log list emptied;
- the `routing.md` refusal removed;
- the `--json` and transcript refusals removed;
- `post` looking the log up again;
- the branch key dropped;
- nothing left out.

The eighteenth was the branch above, which survived and left. Over
`skills/verify/orchestration.md`, with the text case alone, both mutants
came back red: removing `--work-item` from the command, and removing
`` `# <file name>` `` from the sentence that says the command reads that
line. `git status` was clean after each run.

**The two read-only runs, from the tree's script, without `--post`, on
2026-11-09** (`python3 skills/verify/scripts/session_cost.py --work-item
<dir>`, exit 0 each). Both directories exist on this tree. The first:

```
1,788 segment transcripts walked on this machine, 2 naming 1794128303-the-plugin-ships-two-hooks-again or feat/1430-the-plugin-ships-two-hooks-again
  0 already in the log, 2 in this reading

# agent-aa0765332e9340577.jsonl
# agent-aa7ba6a7b5ce0cf20.jsonl

  agent                             span  calls  t/turn    gap        tokens     context
  …-aa0765332e9340577.jsonl  1/2   13.6m     54    1.29    18s     7,877,139     219,632
  …-aa0765332e9340577.jsonl  2/2    1.5m     16    2.29     9s             —     234,418
  agent-aa7ba6a7b5ce0cf20.jsonl    12.1m     37    1.23    24s     3,971,677     194,692
```

This work item's own:

```
1,788 segment transcripts walked on this machine, 3 naming 1794178392-each-release-posts-the-readings-no-session-posted or feat/1439-each-release-posts-the-readings-no-session-posted
  0 already in the log, 3 in this reading

# agent-aa0765332e9340577.jsonl
# agent-aaca855c2bab4243e.jsonl
# agent-ab8e8b8952399fc7d.jsonl

  agent                             span  calls  t/turn    gap        tokens     context
  …-aa0765332e9340577.jsonl  1/2   13.6m     54    1.29    18s     7,877,139     219,632
  …-aa0765332e9340577.jsonl  2/2    1.5m     16    2.29     9s             —     234,418
  agent-aaca855c2bab4243e.jsonl     8.2m     44    1.42    15s     3,956,328     170,120
  …-ab8e8b8952399fc7d.jsonl  1/2    9.9m     91    1.38     7s    22,167,277     256,503
  …-ab8e8b8952399fc7d.jsonl  2/2    8.6m     50    1.52    13s             —     326,040
```

Each matched file's `.meta.json` names its agent. `aa0765332e9340577` is
#1439's framer, `aa7ba6a7b5ce0cf20` is #1442's framer,
`aaca855c2bab4243e` is #1443's framer, and `ab8e8b8952399fc7d` is this
crafter, phases 1 and 2. **Departure from the scenario *A real work item*:**
it expected the first run to report no segment transcript on this machine.
It reports two, and both are 0.36.0 framers whose spawn prompts quote the
0.35.0 directory. The design's probe named #1439's framer as such an
exception, and #1442's framer is a second one. The same rule takes #1443's
framer into this work item's reading, because its prompt lists #1439 as a
sibling. So a prompt that names several work items is posted by whichever
work item's command runs first. Each command after that leaves it out,
because its name then stands on the log (*Scope* item 3). The open log, #1438,
held one comment, and it names no transcript.

**Phase boundary.** One `bin/test` command over the 43 modules of phase 1's
set, plus `tests/behaviour/test_a_phase_hands_the_next_one_a_record.py`,
`tests/behaviour/test_unverified_rows_close.py`,
`tests/behaviour/test_a_release_publishes_its_note.py`,
`tests/github/test_publish_release_note.py`,
`tests/github/test_release_seal.py`, `tests/skills/test_chain_check.py` and
`tests/lib/test_routing.py`. Those read the work item's records, its
changelog fragment, or `lib/routing.py`, which this module now imports. Its
first run, over `b3be38b5` with the records written, failed one case:
`tests/skills/test_test_layout.py::Test_main::test_accepts_this_repositorys_tests`.
The layout check asks every class for a `test_accepts_` case, and
`Test_work_item` had none. `d3ca21e5` renamed its first case. Over
`d3ca21e5`, the same command gave 2505 passed and 7 skipped (exit 0).
