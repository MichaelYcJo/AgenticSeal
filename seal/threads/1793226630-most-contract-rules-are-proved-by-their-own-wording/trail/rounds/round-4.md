# Review round 4: 1793226630-most-contract-rules-are-proved-by-their-own-wording

target: 400863f9, fixes 5b19ca0e..400863f9

## Findings

### 1. The count posted on #1111 gives a number for 10 of the 39 modules, and the issue's second *Done when* asks for each module with its number

severity: must
location: `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/frame/plan.md:88-90`, `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/frame/questions.md:43-46`, `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/trail/phases/phase-2.md:30-71`
evidence: executed `gh issue view 1111 --comments`, `gh issue view 1111 --json body`, `sed -n 32,70p seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/trail/phases/phase-2.md`
verdict: open

The caller asked this round to weigh whether the comment of 2026-10-28 on
#1111 states only what `trail/phases/phase-2.md` and the frame state. It
does. Every number in it matches the phase's table, and the confirmation
below lists them. What it leaves out is the defect.

The issue's second *Done when* reads: "The count of phrase pins on rule
sentences in the other `tests/text` modules is recorded on this issue, each
module with its number." `frame/design.md:19` ties the orchestrator's post
to that line. `frame/plan.md:88-90` says the orchestrator "posts phase 2's
table as a comment on #1111", and judgment 6 at `frame/questions.md:43-46`
says the same. The comment names 10 modules with their numbers. It says
"The rest are 9 or fewer, and 16 modules have 0", and names none of those
29. For the rest it points at `trail/phases/phase-2.md` on the work item's
branch. The settle after the release removes that directory
(`docs/the-review-record.md:169`), and the branch goes after its merge. The
issue is the count's one lasting home, and it would hold 10 of 39 numbers.

The comment's other statements need no change. This is a repair outside the
tree. It makes no commit on the branch, so by
`docs/the-review-record.md:142-145` it closes `deferred #1111`, and the
answer line says what changed there.

Add the table below to the comment, in place of the sentence "The
per-module table and each left-out line are in the work item's
`trail/phases/phase-2.md`, on branch
`chore/1111-most-contract-rules-are-proved-by-their-own-wording`." Its rows
are the first two columns of `phase-2.md:30-71`, copied:

```markdown
Each module's number, from the work item's `trail/phases/phase-2.md`:

| Module under `tests/text/` | Phrase pins |
|---|---|
| `test_a_document_has_room_for_the_next_fold.py` | 0 |
| `test_a_gate_that_fails_says_so.py` | 1 |
| `test_a_language_section_of_writing_style_opens_alone.py` | 1 |
| `test_a_merged_ticket_says_so_on_the_tracker.py` | 0 |
| `test_a_moved_rule_leaves_its_definition.py` | 12 |
| `test_a_parallel_agent_names_its_scratch_after_the_work_item.py` | 3 |
| `test_a_probe_does_not_outlive_its_round.py` | 5 |
| `test_a_question_says_who_can_answer_it.py` | 11 |
| `test_a_record_carries_no_comment.py` | 0 |
| `test_a_release_cannot_ship_an_untrue_milestone.py` | 0 |
| `test_a_rider_reaches_its_file.py` | 9 |
| `test_a_segment_feeds_the_flow_log.py` | 32 |
| `test_absence_claims.py` | 5 |
| `test_broad_gate_rule.py` | 31 |
| `test_ci_gives_the_checks_what_they_need.py` | 0 |
| `test_edits_go_through_the_edit_tool.py` | 6 |
| `test_every_agent_reads_the_contract.py` | 0 |
| `test_every_file_the_plugin_reads_or_writes_names_its_encoding.py` | 4 |
| `test_guard_resolves_the_tree_it_judges.py` | 7 |
| `test_no_case_tells_the_agent_it_is_evaluated.py` | 0 |
| `test_no_passage_is_pasted_into_a_second_file.py` | 0 |
| `test_review_axes.py` | 10 |
| `test_settle_reads_before_it_removes.py` | 25 |
| `test_the_chain_section_has_one_shape.py` | 2 |
| `test_the_changelog_is_gathered_at_release.py` | 0 |
| `test_the_direct_answer_owes_the_sealers_record.py` | 3 |
| `test_the_gate_hands_cmd_a_path_it_can_run.py` | 0 |
| `test_the_handoff_before_round_one.py` | 24 |
| `test_the_handoff_names_the_form_it_ran.py` | 2 |
| `test_the_mode_is_a_row_and_a_command.py` | 0 |
| `test_the_record_is_written_in_words.py` | 1 |
| `test_the_records_can_be_carried_out_and_in.py` | 0 |
| `test_the_release_table_reads_two_trees_and_fails_nothing.py` | 0 |
| `test_the_release_tail_does_not_end_at_the_tag.py` | 25 |
| `test_the_rules_claude_md_names_have_one_home.py` | 0 |
| `test_the_rules_have_one_owner.py` | 24 |
| `test_the_settings_have_a_front_door.py` | 12 |
| `test_the_suite_runs_with_gh_logged_out.py` | 0 |
| `test_the_verifying_round_is_bounded_not_cheapest.py` | 0 |
| Total | 255 |
```

answer:

### 2. Round 2's answer to finding 3 says the grep finds the ten `check:` lines "in 5 files", and the same grep finds them in 4

severity: should
location: `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/trail/rounds/round-2.md:128`
evidence: executed `git grep -l -E '^\s*check:.*evals/' -- ':!seal/'`, `git grep -l -E '^\s*check:.*evals/' 0f77a2d0 -- ':!seal/'`, `git grep -l -E 'check:.*evals/behaviour' -- ':!seal/'`, `git blame -L 128,128 --porcelain seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/trail/rounds/round-2.md`
verdict: open
regression: round-2#3

The unit is finding 3's `answer:` line at `round-2.md:128`, which `0f77a2d0`
wrote (executed `git blame`). `frame/design.md` *Why each eval case is the
reader it is* fixes which eval case reads which contract rule, and phase 1's
row of `frame/plan.md` re-points the 13 `check:` lines. Round 1's fix pass
swept every `check:` line that names an eval case under contract rule 12,
and round 2's fix restated that sweep's result. It got the line count right
and the file count wrong.

The answer reads "`git grep -n -E '^\s*check:.*evals/' -- ':!seal/'` finds
10 lines in 5 files". That command, run with `-l` at HEAD and at
`0f77a2d0`, lists 4 files: `agents/proofer.md`, `agents/sealer.md`,
`skills/agent-contract/SKILL.md` and `skills/code-review/SKILL.md`. Round
3's own probe row at `round-3.md:160` says "10 lines in 4 files", so the
records already disagree with each other. The wider pattern of round 2's
finding 3, without the `^\s*` anchor, also reaches
`tests/github/test_rules.py`, which makes 5. The 5 likely came from that
pattern. That is an inference; nothing in the records says so.

This is the same class as round-2#3: a count in a record that a sealer
re-runs and finds different. The answer line also says "Round 1's record
stays as written". That sentence stays. It is the reason for the `deferred`
verdict that round-3#1 reopened, and the reopen is the record's correction
of it. The file count is no part of that trail.

In `round-2.md:128`, replace:

```markdown
finds 10 lines in 5 files, the ten that round 1's answer listed (executed).
```

with:

```markdown
finds 10 lines in 4 files, the ten that round 1's answer listed (executed).
```

Commit that edit. The finding then closes `fixed <that commit>`, the
correction to a record that `docs/the-review-record.md:140-141` gives that
close.

answer:

## Confirmations

confirms: round-3#1
`126cdfa7` changes one word of `round-1.md:104`, "11" to "10", and nothing
else (read, `git diff 5b19ca0e 400863f9`). `round-1.md:104` is on the
finding's `location:` line, so the close meets
`docs/the-review-record.md:101-108`. A correction to a record that a commit
made closes `fixed <commit>` (`docs/the-review-record.md:140-141`). I re-ran
the answer's executed line at `126cdfa7` and at HEAD. Both list the same ten
lines: `agents/proofer.md:74`, `agents/sealer.md:125`, `:130`, `:136` and
`:148`, `skills/agent-contract/SKILL.md:46`, `:78` and `:102`, and
`skills/code-review/SKILL.md:38` and `:140`. The answer's claim that
`round-2.md:97` was left as written holds: the range touches only
`round-1.md` and `round-3.md`. The orchestrator wrote the verdict and the
answer because no fix pass ran. Round 3 accepted the same form for
round-2#1. Re-running round 3's grep for `finds 11` now finds the number
only where a record quotes round 1 as it stood: round 2's heading and quote
at `round-2.md:92` and `:119`, and round 3's evidence, grounds and probe.
A finding's heading and grounds are the round's own and stay. The rewrite
made no new defect in the unit. Executed and read.

confirms: none
The comment of 2026-10-28 on #1111 states only what the records state
(executed `gh issue view 1111 --comments`). Its total, 255 across 39
modules, and its ten named numbers equal `phase-2.md:32-70`. "The rest are
9 or fewer, and 16 modules have 0" holds: of the 39 rows, 16 are 0, 13 are
1 to 9, and 10 are 10 or more (executed, `awk` over the table). Its
left-out kinds and their total of 124 equal `phase-2.md:71`. The 279 with
the commands counted equals `gaps.md:15` and `phase-2.md:120-121`. The
three Q2 lines equal `phase-2.md:135-141`. The 75 and 81 equal the last two
columns of the total row. The 182 and 168, and "no bound on this count",
equal `gaps.md:16`, `phase-2.md:146-155` and `frame/design.md:230-232`. Its
last paragraph equals the changelog's account of the module. One phrase
reads two ways: "168 over the same 39 modules" can suggest that the 182 is
over those 39 too. At `0b75346f` it is over all of `tests/text`, 174 of it
outside the contract module (round 1's probe row). The comment does not
say the 182 is over 39 modules, so this is no defect. Finding 1 is what the
comment leaves out. Executed and read.

confirms: none
The sweep the caller asked for found no other sentence that states an old
count, bound or reader. Readers: the `check:` lines at
`skills/agent-contract/SKILL.md` (executed `grep -n '^check:'`) equal the
rule rows at `frame/design.md:119-138`, the eval bullets at `:143-160`,
judgments 4 and 5 at `frame/questions.md:30-42`, rows C and E at
`frame/plan.md:72` and `:74`, the eval targets at `frame/plan.md:45-48`,
the changelog sentence, and `gaps.md:23`. The bound: 182 is called a bound
only where `gaps.md:16` and `phase-2.md:146-148` quote `frame/design.md` at
`d0b5cf4f`, and in round records describing that (executed `git grep -n -E
'182|bound'`). Counts: "12 lines" at `frame/design.md:15` holds at
`4134055a` (executed `git grep -c 'none reader: the proofer at review'`,
summed). "All 266 check lines in 55 rule files hold" in the earlier records
is what `bin/seal rules --check` prints at HEAD (executed). The 13 lines,
20 rows, and "16 of the contract's 20 rules" in the frame are states at
base. `phase-1.md:28` "all six eval targets" is the state at `9ad992b6`,
carried from rounds 1 and 2. "Eleven" at `phase-2.md:141-144` counts lead
literals. The shipped files: the module's docstring and comments
(`tests/text/test_the_agent_contract_holds_the_universal_rules.py:1-56`)
and `tests/text/test_the_handoff_before_round_one.py:106-110` state the
current readers. `git grep` over the tree outside `seal/` finds no
remaining name of `PINS`, `FOUR_RULES`, `missing_pins` or `without_pin`
(executed). The module's name stands in `.test_durations`, which `gaps.md`
*Not done* records, and in `docs/the-broad-gate.md:42`, which `frame/design.md`
*Rule changes* moves at the settle. Finding 2 is the one instance found.
Executed and read.

confirms: none
Carried, not re-established. The per-module decisions behind phase 2's
table were re-derived by rounds 1 and 2, and this round re-ran only the
table's sums and row counts. The readings of the graders behind
`agents/proofer.md:74`, `agents/sealer.md:125` and `:148`, and
`skills/code-review/SKILL.md:38` and `:140`, are still the round-1 fix
pass's. No file outside `seal/` changed in this fix range. Every verdict
above was reached this round. Read.

confirms: none
The checks the caller named, run narrow, each exit 0. Through `bin/test
-q`: the contract module (29 passed),
`tests/text/test_the_record_is_written_in_words.py` (3) and
`tests/behaviour/test_docs_line_wrap.py` (39). `bin/seal layout --check`
and `bin/seal rules --check` exit 0. The chain check over the worktree
reads this record. Its refusals are this round's two findings, which read
`open`, and the absent `trail/gate.md` and `guarantee.md`, which the
orchestrator's broad run and the sealer write after the rounds settle. The
suite stays labelled `unverified`, and the orchestrator answers it.
Executed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck, including `test_the_durations_file_prices_the_suite` | the branch at `400863f9` | the orchestrator, through `seal gate` |
| Whether the eval cases that rules 2, 5 and 7 name pass on a run | `evals/behaviour/sealer/`, `evals/behaviour/crafter/` | the orchestrator, at the next preload rewrite that runs the behaviour evals |
| `gaps.md:16` says `208f7076` wrote the count's reading of 182 into the frame, and `gaps.md:34-36` *Fed back into the spec* reads `none`. Whether the folds at `208f7076` and `5a77bc37` belong under that heading | `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/gaps.md` | the orchestrator |
| Rule 2's case reads one agent and one command spelling. Whether that partial reach is enough for rule 2 | `evals/behaviour/sealer/rule-sealer-no-gate/graders/shape-runs-no-broad-run.md` | the owner |
| `frame/questions.md` Q1 and Q2 stand on their defaults with Status `open` | `frame/questions.md` | the owner |

## Probes

| Command | Result |
|---|---|
| `git diff 5b19ca0e 400863f9`; `git show --stat 126cdfa7 400863f9` | one word of `round-1.md:104`; the verdict and answer lines of `round-3.md` finding 1 |
| `git grep -n -E '^\s*check:.*evals/' -- ':!seal/'`, at `126cdfa7` and at HEAD | 10 lines each, the same ten |
| `git grep -l -E '^\s*check:.*evals/' -- ':!seal/'`, at HEAD and at `0f77a2d0` | 4 files each |
| `git grep -l -E 'check:.*evals/behaviour' -- ':!seal/'` | 5 files, `tests/github/test_rules.py` the fifth |
| `git blame -L 128,128 --porcelain <work item>/trail/rounds/round-2.md` | `0f77a2d0` |
| `git grep -n -o 'finds 1[01] .check:. lines' -- <work item>` | 10 at `round-1.md:104`, `round-2.md:125`, `round-3.md:64`; 11 at `round-2.md:92`, `:119` and in `round-3.md` |
| `gh issue view 1111 --comments`; `gh issue view 1111 --json body` | one comment, 10 modules named with a number; the second *Done when* asks for each module |
| `awk` over `phase-2.md:32-70` | 39 rows; 16 at 0, 13 at 1 to 9, 10 at 10 or more; sum 255 |
| `git grep -c 'none reader: the proofer at review' 4134055a`, summed | 12 |
| `git grep -n -E '182\|bound'` and the reader patterns over the work item | no sentence outside quotes of `d0b5cf4f` calls 182 a bound; every reader matches the contract |
| `bin/test <module> -q` over the three modules in *Confirmations* | each exit 0 |
| `bin/seal layout --check`; `bin/seal rules --check` | exit 0; exit 0, "all 266 check lines in 55 rule files hold" |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.24.0 --worktree` | see *Confirmations* |
