# Review round 2: 1793343707-each-document-serves-one-reader

target: 30fc1db0, fixes b3b36143..30fc1db0

## Findings

### 1. The settle's new step 7 counts "the four numbers" a section names that names none in the release that ships the step

severity: should
location: `skills/settle/SKILL.md:219-222`, `tests/text/test_settle_reads_before_it_removes.py:126-129`, `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:56`, `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:131`, `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:262-266`
evidence: executed `sed -n '/^## The run/,/^## The handoff/p' docs/the-review-record.md | grep -c -i 'round records\|review cost\|location:'`, `git grep -n -c 'review cost\|four numbers\|four counts' -- docs skills/settle`
verdict: fixed 634e8b26
regression: round-1#4

The unit is step 7 of `skills/settle/SKILL.md` *The settling session's
procedure*, which `0a15911b` added. The frame says step 7 counts "the four
numbers `docs/the-review-record.md` *The run* names" (`frame/design.md`
Scope item 7 and its Table B row; no `frame/plan.md` phase row covers a
fix pass), the fix wrote exactly that, and the defect came from round 1's
paste-ready fix for finding 4, which cited a rule that this design's
`## Rule changes` only `add`s, and which the fold at `6c3f6482` took
unchanged.

The four numbers are named nowhere a 0.25.1 reader can open. *The run* at
HEAD holds no line about round records, review cost or `location:` paths:
the search printed 0. The only file under `docs/` and `skills/settle/` that
speaks of four numbers is `skills/settle/SKILL.md` itself. The rule reaches
`docs/the-review-record.md` at the settle after 0.25.1 (`frame/plan.md`
*Operational impact*). So the step ships in 0.25.1 and points at text that
ships in a later release. A settling session on 0.25.1 opens *The run*,
finds no count to take, and either skips the step or invents the counts.
For this repository's own settle of #1148 the step happens to work,
because step 2 writes the `add` before step 7 runs. The `add` in turn says
the session counts "at step 7", so each of the two texts sends the reader
to the other for the rule.

The fix makes step 7 the home of the counts, which is where the reader is,
and lets the policy sentence cite it. It also says where the counts go,
since a repository with no `flow-baseline` log has nowhere to post them.

```markdown
<!-- skills/settle/SKILL.md, The settling session's procedure, step 7 -->
7. Where the repository keeps a `flow-baseline` log
   (`skills/verify/orchestration.md` *Measure the segment, and feed the
   flow log*), count for each released work item routed through the review
   chain, with `git grep -h` over its `trail/rounds/round-*.md`: the
   `### <n>.` finding headings, the `regression:` and `reopens:` lines, the
   `location:` lines left with no backticked path once every path under
   `seal/threads/` is deleted from them, and the record files. Post the four
   numbers to that log. Then run `seal settle --apply`, which removes the
   records.
```

```python
# tests/text/test_settle_reads_before_it_removes.py,
# test_the_skill_states_the_settling_sessions_procedure, the step 7 entries
        "Where the repository keeps a `flow-baseline` log",
        "the `location:` lines left with no backticked path once every path "
        "under `seal/threads/` is deleted from them",
        "Post the four numbers to that log.",
        "Then run `seal settle --apply`, which removes the records.",
```

The `add` to *The run* at `frame/design.md:262-266`, Scope item 7 and the
Table B row are the framer's. The `add` keeps its bold rule sentence and
replaces its how-to with "The settling session counts them at step 7 of
`skills/settle/SKILL.md` *The settling session's procedure*, which says
how, and posts them to the `flow-baseline` log."

answer: Step 7 of `skills/settle/SKILL.md` *The settling session's procedure* is now the home of the counts: where the repository keeps a `flow-baseline` log, it counts for each released work item routed through the review chain, with `git grep -h` over its `trail/rounds/round-*.md`, the numbered `###` finding headings, the `regression:` and `reopens:` lines, the `location:` lines left with no backticked path once every path under `seal/threads/` is deleted from them, and the record files, posts the four numbers to that log, then runs `seal settle --apply`. The round's text says `### <n>.`; the step says "the numbered `###` finding headings", because the procedure case splits the skill at `## ` and a `### <n>.` inside the step cut the procedure short. The case's guard that no `git grep` stands in the procedure was refused by step 7's own `git grep` over round records, which searches no test, so the guard now reads step 6 alone, as its message always said (contract rule 18). The pins were seen red before the step changed, and mutants that plant `git grep` in step 6 and drop "Post the four numbers to that log." both went red (executed). The fragment's process row now says the counts are taken at step 7 where a `flow-baseline` log is kept. No shipped sentence sends a reader to *The run* for the counts (executed, `git grep`); `frame/design.md`'s Table B row for `skills/settle/SKILL.md` (line 131) still says step 7 counts "the four numbers `docs/the-review-record.md` *The run* names" and posts them "as that section says", which the fold at dd3a7232 left, and it is the framer's line.

### 2. The frame names the step 7 clause's pin in a module that does not hold it

severity: should
location: `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:56`
evidence: executed `git grep -n 'For each released work item' -- tests`
verdict: fixed dd3a7232
regression: round-1#4

The unit is Scope item 7 of `frame/design.md`, which the fold at
`6c3f6482` rewrote to close finding 4's frame part. The frame says the
step "gains the clause, pinned in `tests/skills/test_settle.py`", the fix
pass put the pin in
`tests/text/test_settle_reads_before_it_removes.py#test_the_skill_states_the_settling_sessions_procedure`
and gave its grounds in round 1's answer, and the defect came from round
1's finding 4, which named the module without opening it, and from the
fold taking that name before the fix pass chose.

The fix pass's choice is right: `tests/skills/test_settle.py` tests the
script, and the other case already holds every step of the procedure in
order. The search finds the clause only in that case. The sealer reads the
frame's verification claims against the tree, so the frame names the
module the pin is in. Where finding 1's fix lands, the pin's text changes
and the module stays.

```markdown
<!-- frame/design.md, Scope item 7 -->
... that step gains the clause, pinned in
`tests/text/test_settle_reads_before_it_removes.py#test_the_skill_states_the_settling_sessions_procedure`,
so the rule stands where the session that acts on it reads (round 1's
finding 4). ...
```

The line is the framer's, and the orchestrator folds it.

answer: The fold at dd3a7232 rewrites Scope item 7 to say the step "states the four counts and where they go, pinned in `tests/text/test_settle_reads_before_it_removes.py#test_the_skill_states_the_settling_sessions_procedure`" (read, `frame/design.md:56`). `git grep` finds the step's clause pinned only in that case, at `tests/text/test_settle_reads_before_it_removes.py:130` after 634e8b26 (executed), and `tests/skills/test_settle.py` holds none of it.

### 3. The frame's rule change to *The run* still spawns the verifying round only after fixes outside the records

severity: should
location: `seal/threads/1793343707-each-document-serves-one-reader/frame/design.md:250`
evidence: executed `git grep -n -i 'fixes to a file outside' -- skills docs seal/threads/1793343707-each-document-serves-one-reader/frame`
verdict: fixed dd3a7232
regression: round-1#1

The unit is the `to:` line of the `change` to `docs/the-review-record.md`
*The run* at `frame/design.md:250`, which the fold at `6c3f6482` rewrote
for finding 1. The frame's Scope item 5 says a `fixed` finding located in
code owes the round whatever its commit touched. The fold narrowed the
second clause of this line to match, but left the first clause, "It is
spawned after the last fixes to a file outside the work item's records are
committed". So the defect came from a fold that changed half a sentence.

Take a finding located at `f.txt:1` and at the work item's `gaps.md`,
closed by a commit that touched `gaps.md` alone. The first clause says no
round is spawned, because no fix touched a file outside the records. The
second clause says the pass owes one, because the finding is not located
in the records alone. The check refuses that pull request (round 1's
finding 1, and the third case at `tests/skills/test_chain_check.py`). The
settle writes this line into the policy root, where an orchestrator reads
it. The fix pass already removed the same clause from the *When* row of
`skills/code-review/orchestration.md:113`. The search finds the old clause
only here.

```markdown
<!-- frame/design.md:250 -->
  to: It is spawned after the last fixes are committed, and a fix pass owes none only where each finding it closed is located in `seal/threads/<id>/` alone and its commits touched nothing else, as *What the check reads at the pull request* states; its target is the diff of those fixes, new units included;
```

The line is the framer's, and the orchestrator folds it. The `from:` is
unchanged, so `rule_changes.py#parse` still finds it in its section.

answer: The fold at dd3a7232 rewrites the `to:` line at `frame/design.md:250` to the round's text: "It is spawned after the last fixes are committed, and a fix pass owes none only where each finding it closed is located in `seal/threads/<id>/` alone and its commits touched nothing else" (read). `git grep -i 'fixes to a file outside'` over `skills`, `docs` and the design prints nothing (executed). The `from:` line is unchanged and stands in `docs/the-review-record.md` with whitespace collapsed (executed, a one-line Python read of the file).

## Confirmations

confirms: round-1#1
The close holds. `records` hands `channel` `located_in_records(item, f)
and records_only(...)` (`skills/code-review/scripts/chain_check.py:1452-1456`,
`:1755-1762`). The crafter claimed the new case was red against the check
before the fix. With `chain_check.py` at `b3b36143`, the three #1148 cases
gave `1 failed, 2 passed`, and only
`test_refuses_a_last_records_code_finding_fixed_in_its_records_alone`
failed (executed). The old predicate is the mutant that returns `True`, so
that run also covers the claimed mutant. The new case covers what its two
siblings do not: a finding whose `location:` leaves the records. The
crafter also claimed that `--worktree` on the fix pass's tree owed this
round findings 1, 2 and 4 and not 3 or 5. The tree's `chain_check.py` at
`30fc1db0`, before this record existed, printed exactly those three
headings (executed). `bool(f.paths)` goes beyond the design's predicate,
but the two read the same, since the `location:` row is `one` and names at
least one path. `under` reads paths as text, so a `location:` path that
climbs out of the work item's directory with `..` would read as inside it.
`verdict_problems` reads every path the same way, and only the proofer and
the fix pass write the line, so this is no new boundary (read). Each
carrier states the narrowed condition: `README.md:207-213`,
`README.ko.md:201-207`, `agents/sealer.md:93-98`,
`skills/code-review/orchestration.md:99-150`, `skills/implement/acts.md:72`,
`skills/implement/SKILL.md:511`, the fragment's sentence and its process
row. A `git grep` for the old spellings outside `docs/` and `seal/threads/`
found none (executed). This also answers the phase 3 row of `gaps.md`
*Not verified*, which named the proofer for the four statements. The
crafter claimed the rewritten pins in `test_the_rules_have_one_owner.py`
and `test_the_sealer_guarantees.py` were seen red. Against the prose at
`b3b36143` all three cases failed (executed). Finding 3 above is in the
frame's half of the same class.

confirms: round-1#2
The close holds. The crafter claimed the refusal names the repair. Over a
body in 0.25.0's shape, `seal pr-body` with and without `--check` both
exited 1 and printed the repair, and the file's hash did not change
(executed). Following the repair worked: with the own part written above a
`## From the records` line, the write exited 0, kept that part, replaced
the old copy and `## Not from the records` below the line, and `--check`
then exited 0 (executed). `Test_split.test_refuses_a_body_with_no_heading_line`
failed against `pr_body.py` at `b3b36143` (executed). The old text of the
message stands nowhere else in the tree (executed, `git grep`). The
fragment's sentence and `frame/plan.md:75` say what the code does (read).

confirms: round-1#3
The close holds. The fragment states no word count, and its orchestration
row names the three bodies that moved (read,
`seal/threads/1793343707-each-document-serves-one-reader/changelog.md:3`,
`:16`). `frame/plan.md:78` reads "through this design's `## Rule
changes`" with no count. `trail/phases/phase-4.md:5-7` holds the
measurement the design now cites. `2641c43f` touched the fragment alone, so
the check passes it with no round, which is the narrowed exemption's first
real case (executed). The 17 operations of `## Rule changes` parse at
`30fc1db0` with no refusal, and every `section` and every `from` stands in
its document (executed).

confirms: round-1#4
The close holds as far as the finding asked: step 7 now takes the measure
in the procedure the settling session executes, before `--apply`, and
steps 6 and 8 keep their numbers. The pin failed against
`skills/settle/SKILL.md` at `b3b36143` (executed). What the step cites and
where the frame says its pin is are findings 1 and 2 above, on the unit
this fix made.

confirms: round-1#5
The close holds. The corrected third command counted 2 of 5 sample lines,
the two whose every path is under `seal/threads/`, and left out
`seal/README.md:3`, `setup.cfg:1` and a line mixing a records path with
`f.txt:1` (executed). Over #1177's records it reads 1, as the design says
(executed). `frame/design.md:184` describes what the command does.

confirms: none
What this round carried and did not re-establish: round 1's coordinates
for the four carriers of finding 1, the location of `split` in
`pr_body.py`, and phase 4's word counts as the measure's home. What it
re-ran: every executed line of findings 1 to 5 above. The narrow modules
`test_chain_check.py`, `test_pr_body.py`,
`test_settle_reads_before_it_removes.py`, `test_the_rules_have_one_owner.py`,
`test_the_sealer_guarantees.py`,
`test_every_orchestrator_act_names_its_delivery.py`,
`test_a_cited_section_stands_in_its_file.py`, `test_settle.py` and
`test_the_verifying_round_is_bounded_not_cheapest.py` gave 501 passed, exit
0. `ruff check` and `ruff format --check` over the seven Python files the
fix diff changed exited 0 (executed). Each of the seven commits in the fix
range carries `Seal-Routing: 1793343707-each-document-serves-one-reader`
(executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Round 1's finding 6 stands `deferred frame/questions.md Q2` and is not written up again. Q2 gives its counts at `16056d31`. At `30fc1db0` the three read 1,216 added and 995 removed outside `seal/threads/`, 598 and 652 outside `tests/`, 618 and 343 in `tests/` (executed). So Q2's cut option would now need 222 lines, not 141, and the body should state HEAD's counts | `seal/threads/1793343707-each-document-serves-one-reader/frame/questions.md` | the orchestrator, writing its part of the body; the owner, answering Q2 |
| 19 of the 25 commits in `fba13ab2..b3b36143` carry no `Seal-Routing:` trailer. They are outside this round's fix diff. `docs/the-routing-check.md` *At the pull request* says the check does not judge a commit with no trailer, so nothing refuses them (read); whether the history is rewritten is not a review question | `fba13ab2..b3b36143` | the orchestrator |
| Carried from round 1, still open: a finding located in `frame/design.md` `## Rule changes` and fixed there alone passes with no round, and the settle writes that text into the policy root. The narrowing leaves that case where it was | `skills/code-review/scripts/chain_check.py:1452-1456` | the owner |
| Carried from round 1: the behaviour suite over the four agent definitions, not run on Q1's default | `seal/threads/1793343707-each-document-serves-one-reader/frame/questions.md` | the owner, at the pull request |
| Carried from round 1: GitHub's rendering of the body's fold | `skills/code-review/scripts/pr_body.py` | the orchestrator, reading the first body this change writes |
| The full suite, the repository-wide lint and format check, and the cross-platform run at `30fc1db0`; the suite is `unverified` here and the label in the fix pass's hand-back is honest | the branch at `30fc1db0` | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `git checkout b3b36143 -- skills/code-review/scripts/chain_check.py`, then `bin/test tests/skills/test_chain_check.py -q -p no:xdist -k 'code_finding_fixed_in_its_records_alone or touched_only_its_records or also_touched_code'`, then the file restored from `30fc1db0` | exit 1, `1 failed, 2 passed`, the new case failing; `git status --short` empty after the restore |
| `git checkout b3b36143 --` the four prose and script files, then `bin/test -p no:xdist -q` over the five rewritten pins, then the files restored | exit 1, `5 failed`; `git status --short` empty after the restore |
| `python3 skills/code-review/scripts/chain_check.py --baseline fba13ab2 --root . --worktree` in the clone at `30fc1db0`, before this record | findings 1, 2 and 4 of round 1 refused as owing a verifying round, and the last target behind HEAD; 3 and 5 not named |
| `bin/seal pr-body seal/threads/1793343707-each-document-serves-one-reader --body <round scratch>/old-body.md --check`, then without `--check`, over a 0.25.0-shaped body | both exit 1, printing the repair; the hash unchanged |
| The same body with its own part moved above a `## From the records` line, then `bin/seal pr-body` without and with `--check` | exit 0 and exit 0; the own part kept, the old copy replaced |
| The corrected third measure command over five sample `location:` lines, and over #1177's records | 2; 1 |
| `rule_changes.parse` over the design at `30fc1db0`, each op's `section` and `from` looked up in its document | 17 ops, 0 refusals, 0 missing |
| `bin/test` over the nine narrow modules named in the last confirmation | exit 0, `501 passed` |
| `uvx ruff check` and `uvx ruff format --check` over the seven Python files the fix diff changed | exit 0; `7 files already formatted` |
| `git diff --shortstat fba13ab2...30fc1db0` outside `seal/threads/`, also outside `tests/`, and over `tests/` | `1216(+) 995(-)`; `598(+) 652(-)`; `618(+) 343(-)` |
