# Review round 6: 1793174169-a-round-with-fixes-costs-three-record-commits

target: 77ece6ba, fixes 19d28cee..77ece6ba

## Findings

### 1. The release note says a round with fixes costs two record commits, and round 5 of this work item paid three under the rule it ships

severity: should
location: `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/changelog.md:3`, `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/design.md:164-179`
evidence: executed `git log --format='%h %s' -- seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/trail/rounds/round-5.md`, `git show --stat 30e31aac`, `git show --stat 77ece6ba`, `git log --format='%h %s' -- seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/trail/rounds/round-2.md`
verdict: fixed ef34bd42

The changelog's first bullet ends: "A round with fixes then costs two record
commits beside the fix commits: the round record's commit and the
orchestrator's answer commit." `frame/design.md:164-179`, *What a round
with fixes costs after this work*, says the same: "That is two record
commits, the number the tree describes."

Round 5 of this work item is a round with fixes, and its record took three
commits: `19d28cee` (the proofer's record), `30e31aac` (the orchestrator's
close of finding 2) and `77ece6ba` (the orchestrator's commit of the fix
pass's close of finding 1). Each holds `trail/rounds/round-5.md` alone
(executed). Each step followed the rule as written. Finding 2 sat in the
frame only, so the orchestrator repaired it at `e8bb7028` and closed it
itself. The `to:` text at `frame/design.md:252-253` gives such a finding
the orchestrator as its writer: "A finding closed with no fix pass, such
as ... has the orchestrator as its writer, and the orchestrator writes and
commits the lines of every finding it closes at that step together". The
fix pass then closed finding 1 at another step, and the orchestrator
committed that close in a second commit. Two steps, two answer commits,
three record commits. Nothing in the shipped files or the frame makes the
count two in that case.

The case is not rare. A finding located only in the frame is the
orchestrator's to repair, since the crafter does not write the frame
(`skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket*, the folding rule). This run met it in round 3 and round 5. Round 3
had no fix pass, so its count stayed at two. Round 5 had one, so its count
went to three.

This run also shows the other way the same case was handled. In round 2,
the orchestrator repaired a frame half at `4fa7a630`, and the fix pass
closed the whole finding in its own lines: round 2's record took two
commits, `921bfce7` and `38aea7be` (executed). Round 5's finding 1 was
handled that way too: its frame block is the orchestrator's `e8bb7028`,
and the fix pass's `answer:` names it. So the orchestrator can keep the
count at two by leaving a finding it repaired in the frame open for the
fix pass to close. No sentence asks it to, and round 5 did otherwise.

Why it matters: the release note tells a maintainer what the change buys.
It promises two record commits for every round with fixes, and the run
that built the rule shows three. Either the count is qualified, or the
orchestrator's text gains the step that keeps it at two. The second is a
new orchestrator sentence with a case to pin it. The orchestrator weighs
that against the first, which changes no rule. The paste-ready fix below
is the first.

The last sentence of the changelog's first bullet (`changelog.md:3`):

```markdown
A round whose findings the fix pass answers then costs two record commits beside the fix commits: the round record's commit and the orchestrator's answer commit. A finding the orchestrator closes itself, such as one it repaired in the frame, is closed at a step of its own and takes a commit of its own, so a round that has both kinds costs three.
```

`frame/design.md:166-167`, from "orchestrator's, holding both lines":

```markdown
orchestrator's, holding both lines of every finding the pass answered. That
is two record commits, the number the tree describes. A finding the
orchestrator closes itself in a round that also has a fix pass adds one
more, since its lines are closed at another step: round 5 of this work item
closed its finding 2 at `30e31aac`. The answer commit
```

The changelog is the crafter's to write and the frame the orchestrator's.
After the edit, the paste check has to read the changelog again: the new
sentence was written apart from `docs/the-review-record.md` and the two
edited files, and this round has not measured it.

answer: The finding holds: `git log` over `round-5.md` shows three commits, `19d28cee`, `30e31aac` and `77ece6ba`, and the last two each touch `round-5.md` alone (executed). `ef34bd42` rewrites the last sentence of the changelog's first bullet to the changelog block above, as given. The frame's block was applied by the orchestrator at `80325423`, since the frame is not the crafter's to write. `tests/text/test_no_passage_is_pasted_into_a_second_file.py` exits 0, but it leaves out everything under `seal/`, so it does not read the changelog. The new sentences were measured with that module's `longest_run` instead: 0 against `docs/the-review-record.md`, `frame/design.md`, `skills/code-review/orchestration.md`, `agents/crafter.md`, `skills/implement/orchestration.md` and `gaps.md` (executed). A `git grep` sweep for "record commits", "round with fixes", "answer commit", "per round" and "count at two" over `agents/`, `skills/`, `docs/`, `templates/`, `tests/` and this work item's records found no other sentence that promises two record commits for every round with fixes. `frame/plan.md:9`, `frame/design.md:173` and `tests/text/test_the_rules_have_one_owner.py:142` describe runs that already happened. `frame/plan.md:114`, row C's verdict, says F "keeps the count at two", which reads as a comparison with row C; it is the frame's, so it was left for the orchestrator.

## Confirmations

confirms: round-5#1
The close holds. `8b09c50d` rewrites the last sentence of the `Grounds`
cell at `skills/implement/orchestration.md:666` and the last two sentences
of the changelog's third bullet (`changelog.md:5`) to round 5's blocks,
word for word. `e8bb7028`, the orchestrator's, applies the frame's block at
`frame/design.md:79-84` word for word (read, `git diff 19d28cee..77ece6ba`).
Each new sentence holds against the rule beside it. The fix pass commits
neither line (`skills/code-review/orchestration.md:78-84`,
`agents/crafter.md:156-159`), so who wrote the lines is in no commit, and
whether the orchestrator's commit carried them is in the history (read).
The verdict's commit touches two of the three `location:` paths, and the
third is the frame's block at `e8bb7028`, which the `answer:` names. The
crafter's account says the new case ran red against the cell at `30e31aac`.
This round settled that by reading: at `30e31aac` the cell holds the old
phrase once and the new phrase not at all, so both assertions fail there
(executed, `git show 30e31aac:skills/implement/orchestration.md | grep -c -F`
for each phrase: 1 and 0). The group read: no other case in `tests/` reads
this row's words. `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`
requires the cell and reads none of it (executed, `git grep -F` for the
row's first cell over `tests/`). So the case covers what nothing else did.
Removing `gaps.md`'s *Not verified* row is right, since the row said no
case held the sentence. The `seal mutate` runs are the crafter's account,
and this round did not re-run them.

confirms: round-5#2
The close holds. `e8bb7028` replaces the last sentence of the `to:` text and
the first failure scenario in `frame/plan.md:86-92` with round 5's blocks,
and the words match (read). `frame/plan.md:92` now joins two lines of the
block into one long line, which no check reads and which changes no word.
S7 holds against the new `to:` text: `longest_run` gives 0 against
`skills/code-review/orchestration.md`, `agents/crafter.md`,
`docs/the-review-record.md`, `skills/implement/orchestration.md` and this
work item's `changelog.md`. S5 holds: `rule_changes.parse` gives one `add`
op and no errors (executed, see `## Probes`). The verdict's commit touches
both `location:` paths. The orchestrator wrote both lines and committed them
alone in `30e31aac`, as the `to:` text gives a finding closed with no fix
pass (read). That commit is the third record commit finding 1 above names.

confirms: none
The round's own history follows the rule the work item ships for the fix
pass's lines. `8b09c50d`, the fix pass's commit, does not touch
`trail/rounds/round-5.md`. `77ece6ba` touches that file alone and changes
two lines, finding 1's `verdict:` and `answer:` (executed, `git show --stat`
and `git show` on each). Whether those lines are the fix pass's unchanged is
in no commit, as the new `Grounds` sentence says. This round read it from
the session's transcripts instead. The fix pass's transcript,
`subagents/agent-a268e27eeda8d7d6e.jsonl` under session
`9dbfaaac-2128-47e8-aba4-ecd65a3d744c` in the user's Claude Code project
directory, holds two `Edit` calls on `round-5.md`, at lines 234 and 235.
Each `new_string` stands verbatim in the record at `77ece6ba`. The fix pass
ran no commit touching the record. In the orchestrator's transcript, the
only call on `round-5.md` after the fix pass's spawn is the commit at line
7209, with no `Edit` between (executed, see `## Probes`). So the two lines
reached the branch only in the orchestrator's commit, unchanged. This is
the evidence `frame/plan.md:89-91` names: only a transcript shows it.

confirms: none
The modules that read the files this fix range changed pass, and so do the
layout and rules checks (executed, see `## Probes`). The `git grep` sweep
for the old fact ("record's history", "who wrote", "in which commit")
outside the round records finds it only at `frame/design.md:133` and
`frame/plan.md:51`. Both describe phase 1's sentence as it stood at
`aa8b54cb`, which stays true (executed).

Facts carried from earlier rounds rather than re-established: round 5's
coordinates for the `Grounds` cell, the changelog's third bullet and the
frame's *Scope* item 4, and round 5's way of choosing the test modules.
Re-established this round: both closes, S5, S7, the test runs, the commit
shapes of the fix range and the transcript reading.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `77ece6ba`. Not run, under contract rule 2 | the branch | the orchestrator, through `seal gate` after the rounds settle |
| The crafter's `seal mutate` runs over the new case, which this round did not re-run; the red state against `30e31aac` was settled by reading the blob instead | `tests/text/test_the_rules_have_one_owner.py:402-418` | the sealer, where it samples the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over the 23 modules `git grep -l` finds under `tests/` for `skills/implement/orchestration.md`, `implement/orchestration`, the tuple `"implement", "orchestration.md"`, `test_the_rules_have_one_owner`, `ORCH_IMPL` and this work item's id, plus `tests/text/test_the_record_is_written_in_words.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and `tests/text/test_the_changelog_is_gathered_at_release.py` | exit 0, 688 passed |
| `bin/seal layout --check` | exit 0, 160 files read, 0 refused |
| `bin/seal rules --check` | exit 0, all 266 check lines in 55 rule files hold |
| `.venv/bin/python -B -c` calling `rule_changes.parse(<frame/design.md>, "docs")` and `longest_run(ops[0].new, <file>)` for five files | 1 `add` op, no errors; 0 against each of the five |
| `git show 30e31aac:skills/implement/orchestration.md \| grep -c -F` for the new phrase and for the old phrase | 0 and 1 |
| `git show --stat` and `git show` for `e8bb7028`, `30e31aac`, `8b09c50d` and `77ece6ba` | `30e31aac` and `77ece6ba` each touch `round-5.md` alone, two lines each; `8b09c50d` does not touch it |
| `git log --format='%h %s'` over `round-1.md` to `round-3.md` and `round-5.md` | two commits each for rounds 1 to 3, three for round 5 |
| `python3 -I -c` reading the `Edit`, `Write` and `Bash` calls on `round-5.md` in the fix pass's and the orchestrator's transcripts, and testing each `new_string` against `git show 77ece6ba:<round-5.md>` | fix pass: `Edit` at 234 and 235, both found verbatim, no commit; orchestrator after the spawn at 7188: one commit at 7209, no `Edit` |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.24.0 --root <worktree> --worktree`, after this record was written | see the hand-back |
