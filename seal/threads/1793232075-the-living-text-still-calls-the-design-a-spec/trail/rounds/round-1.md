# Review round 1: 1793232075-the-living-text-still-calls-the-design-a-spec

target: 5c938223 against origin/release/v0.24.0

This is round 1, so no earlier round's coordinates or verdicts were carried.
Every fact below was established at `5c938223` in this round. The frame was
read at `d4b88f70`, and `frame/questions.md` Q1 at `6d33f30b`. The issue was
read with `gh issue view 1110`.

## Findings

### 1. The new phrase "the documents that outrank the code" names two different sets in `implement` and in `code-review`

severity: should
location: `skills/code-review/SKILL.md:22-24`
evidence: read `skills/code-review/SKILL.md:22-24`, `skills/implement/SKILL.md:139-149`, `skills/implement/SKILL.md:171-173`
verdict: fixed 227ea366

This branch coins one phrase for two places. `implement`'s step 1 is now
*1. Read the documents that outrank the code first*. Its precedence at
`skills/implement/SKILL.md:141-142` is policy, then the SDD set, then the
ticket, then the existing code. Its batch paragraph at `:172` reads "the
policy, the SDD set and the ticket". So in `implement` the phrase includes
the ticket. `code-review`'s stage 1 at `skills/code-review/SKILL.md:22-24`
uses the same phrase, "the documents that outrank it", and then lists only
the `docs/` policies and the work item's SDD set. There the phrase excludes
the ticket.

`frame/plan.md` A6a claims the stage checks the policy and the SDD set,
"which is what step 1 calls the documents that outrank the code". But step 1
ranks the ticket above the code too (`skills/implement/SKILL.md:147-149`),
so the claim does not hold. A proofer who follows the phrase back to
`implement` can read stage 1 two ways, with or without the ticket. That
breaks `CLAUDE.md` *Repo rule: text an agent or a check reads has one
reading*: "a defined term keeps its one meaning".

The fix keeps stage 1's scope as it was before this branch. It names the set
with the word `implement` itself uses for the line the ticket falls below,
"the documents that were ratified" (`skills/implement/SKILL.md:148-149`). No
test pins the stage-1 sentence: `git grep -n -i outrank` finds no line of
`tests/` that quotes it (executed). The paragraph also reflows, because this
branch left the word "Look" alone on a short line there.

```markdown
1. **Compliance**: the code against the ratified documents above it, the
   `docs/` policies first and then the work item's SDD set under
   `seal/threads/`. Look for behaviour that is missing and for behaviour
   nobody asked for. Read the code, not the implementer's report of it.
```

answer: The finding holds. In `implement`, the phrase covers the ticket (`skills/implement/SKILL.md:141-149`), and stage 1 lists only the policy and the SDD set. `227ea366` applies the paste-ready stage-1 sentence as written, which also reflows the short line "Look". `7d7288bf`, the orchestrator's, folds `frame/plan.md` A6a. No test reads the stage-1 sentence (executed, `git grep` over `tests/` for its phrases, exit 1), so no pin moved and none had to be seen red. Neither README nor `agents/proofer.md` carries the borrowed phrase: `git grep -n -i outrank` finds it only in `skills/code-review/SKILL.md:22` and in citations of `implement`'s heading (executed). The same phrase still stands in `frame/design.md:76`, *Scope* item 6. The frame is the orchestrator's to fold, because a crafter writes only Status cells there. `trail/phases/phase-3.md:57` keeps it as the record of what `3816dfca` wrote.

### 2. The closing memo misdescribes `evals/scripts/replay_targets.py` and leaves the defect it found with nobody to answer it

severity: should
location: `seal/threads/1793232075-the-living-text-still-calls-the-design-a-spec/gaps.md:34-37`, `seal/threads/1793232075-the-living-text-still-calls-the-design-a-spec/trail/phases/phase-2.md:63-69`
evidence: executed `python3 evals/scripts/replay_targets.py --list`, `git ls-tree -r --name-only v0.23.1 seal/specs`, `git ls-tree -r --name-only v0.23.0 seal/specs`, `git ls-tree -r --name-only v0.23.1 seal/threads`, `gh issue list --state open --search replay_targets`
verdict: fixed 227ea366

The phase record claims that the script's working-tree half is blind, "and
the half that reads tags still finds them" (`trail/phases/phase-2.md:66-68`).
That is not what the script does. With no flag it reads the working tree and
the two highest release tags (`evals/scripts/replay_targets.py:107-117`,
`:787`). Those tags are `v0.23.1` and `v0.23.0`, and at both of them
`seal/specs/` holds 0 round records. The 7 round records each tag holds are
under `seal/threads/<id>/trail/rounds/`, a layout `RECORD` (`:72`) does not
match. `replay_targets.py --list` prints nothing and exits 0. Only `--case`,
which reads every tag, still reaches the 0.22.x records. So the default run
has found no round record since 0.23.0, in either half.

The closing memo then leaves the line "for the review" (`gaps.md:36`), and
the review is nobody. `skills/implement/SKILL.md:211-217` says a finding the
work neither fixed nor answered gets an answerer named. `seal/follow-up.md`
says this repository files a schedulable item in its tracker. No open issue
names the script (executed, `gh issue list`, no result).

Whose fix this is: this work item's job is to write the home, not the fix.
Issue #1110 *Done when* covers the word only. The fix is not a re-point like
*Scope* item 8's. `RECORD` at `:72`, and the record paths at `:617`, `:646`,
`:718` and `:750` and at `evals/scripts/seed_defects.py:327` and `:348`, all
spell `seal/specs/<item>/rounds/round-<n>.md`. A reader of both layouts
changes which round records the generator picks, with its cases in
`tests/evals/test_replay_targets.py`, and that change needs a frame of its
own. The frame's grounds for putting `evals/` out cover scaffolds, which
are measured inputs (`frame/plan.md` A7a). They do not cover this generator,
so the frame does not settle the question either way.

The fix has two steps. First, the orchestrator files the issue, because an
agent posts nothing. Then the fix pass replaces `gaps.md:34-37` with the
paragraph below. `<N>` is the number the filed issue takes, and no such
issue exists yet. The phase record stays as the record of its moment.

```markdown
`evals/scripts/replay_targets.py` finds no round record written since
0.23.0. With no flag it reads the working tree and the last two release
tags, `v0.23.1` and `v0.23.0`, under `seal/specs/<item>/rounds/`, and
since 0.23.0 the records stand at `seal/threads/<id>/trail/rounds/`:
`--list` prints nothing. Only `--case`, which reads every tag, still
reaches the 0.22.x records. Teaching it the second layout changes what the
generator picks, outside this work's wording, so it is #<N>, filed by the
orchestrator.
```

A title for the issue, in this repository's form:

```text
fix: replay_targets.py reads round records only in the 0.22.x layout, so its default run has found none since 0.23.0
```

answer: The finding holds. The phase record's clause "the half that reads tags still finds them" was wrong: with no flag, the script reads `v0.23.1` and `v0.23.0`, and neither holds a round record under `seal/specs/`. `227ea366` replaces the closing memo's *Not done* paragraph with the round's text as written, `<N>` being #1150, which the orchestrator filed in `release: 0.24.2`. The same commit corrects that clause of `trail/phases/phase-2.md` in place, on the orchestrator's instruction, and names #1150 there. That is where this pass departs from the round's line that the phase record stays. `bin/seal unverified` over the work item's directory still reads the memo (executed, exit 0).

## Confirmations

confirms: none
One meaning of `spec`, S1. This round re-ran C1, C2, C3 and C4 of
`frame/design.md` *The class, enumerated* at `5c938223` (executed). C1 gives
140 lines in 39 files, C2 20 lines, C3 18 lines, and C4 one line outside
`tests/`. Each was read against *Occurrences kept, and why* (read). Every
hit is one of these: a policy document's name or its citation
(`skills/implement/orchestration.md:353` and `:357` cite
`docs/worktree-guard-spec.md`), a reference root, the release-note marker,
the methodology's name, history, the frozen file, another meaning in code,
an identifier, or #1045's lines. The rest are the `docs/` lines that the
nine rule changes name. C2's other lines hold the former brand `specseal`.
C3's lines are identifiers plus phase 1's two Q2 (b) lines. C4's one line
is finding 2's. A search for `specification`, `specified` and `specifies`
in the same scope found no line naming a work item's design (executed).

confirms: none
No word was broken (C5). C5 gives `design`, `Design` and `designs`, and
nothing else (executed). A read of every added line holding `design` found
each one naming a work item's `frame/design.md`, either through its owner,
its path, or a context of `## Rule changes`, Grounding or the settle. The
bare uses "A design states its rule changes"
(`agents/framer.md:152`) and "A design that changes no rule"
(`skills/settle/SKILL.md:79`) stand inside the rule-changes grammar, where
no other design can be meant (read).

confirms: none
The renamed heading. At the base, `git grep -n -i 'Read the spec'` gives 12
lines: the heading, the prose line `skills/implement/SKILL.md:172` "Read the
spec chain", and 10 citations (executed). The closing memo claims ten
citations against the frame's twelve. That count holds: the frame's twelve
counted the heading and the prose line. At `5c938223` the grep prints
nothing, and `evals/` holds no citation of the old heading (executed).
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` passes in the
run below (executed).

confirms: none
The stage rename. The new step-1 heading reads clearly. "compliance" is
used the same way in `skills/code-review/SKILL.md:4`, `:9`, `:13`, `:22`,
`:116`, `agents/proofer.md:4`, `README.md:38`, `:40`, `:177`, the three Korean
README lines and `hooks/review-skill-gate.py:69` (read). A search for
`spec compliance`, `spec-compliance`, the Korean phrase and `spec first`
outside `seal/threads/` and `evals/` prints nothing (executed). Finding 1
is about the stage's appositive, not its name.

confirms: none
The changed pins. Each one's old text cannot satisfy its new assertion
(read):
- `tests/skills/test_chain_check.py:1691`;
- `tests/skills/test_settle.py:1532`;
- `tests/skills/test_unverified_check.py:2107`;
- `tests/text/test_a_moved_rule_leaves_its_definition.py:555`;
- `tests/behaviour/test_unverified_rows_close.py:207`;
- the five `tests/text/test_settle_reads_before_it_removes.py` pins at base
  lines `:81`, `:112`, `:150`, `:177` and `:223`;
- the four heading citations in tests;
- the new prompt pin at `tests/hooks/test_review_skill_gate.py:71-72`.

The crafter claims each was seen red under `bin/seal mutate`. This round
read the claims and did not re-run them. The prompt pin is the only test
string that reads `hooks/review-skill-gate.py#REASON`'s option, so it
covers what its group did not.

confirms: none
The divergences in the closing memo. The five extra pins are `Scope`
item 7's (read). The Korean README line `README.ko.md:438` mirrors
`README.md:445`, as Q2 (a) asks (read). The test local `threads` at
`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:251`
sits on the lines item 8 re-points (read). The two re-pointed cases pass
over `seal/threads/` in the run below (executed).

confirms: none
The rule changes (S9). All nine items of `frame/design.md` `## Rule changes`
parse through `skills/settle/scripts/rule_changes.py#parse` with no error.
Each `from` is found in its section at `475653e7`, and no `to` is there yet
(executed, the probe below). The C1 and C2 hits under `docs/` are all lines
those nine items name (read). No file under `docs/` changed (read, `git
diff --stat`).

confirms: none
The changelog fragment matches the diff (read). Each printed string it names
was read at its line: `settle.py#GROUPS_HEADING`, `#WHOLE_HEADING`, the
argparse description, `seal.py`'s `settle` row, the tally in
`unverified_check.py`, the refusal in `chain_check.py` and the gate's
option.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide `ruff check` and `ruff format --check`, the typecheck, and `.test_durations` against the renamed parametrize id of `test_each_sibling_is_refused_with_its_own_purpose`; the crafter labels the suite `unverified`, and that label is honest | `.test_durations:5526` | the orchestrator, through `seal gate` |
| Whether the crafter's `bin/seal mutate` runs turned each changed pin red; this round read the pins and did not mutate the worktree under review | `seal/threads/1793232075-the-living-text-still-calls-the-design-a-spec/trail/phases/phase-3.md` | the sealer, which re-runs a sample of the crafter's claims |

## Probes

| Command | Result |
|---|---|
| C1 to C6 of `frame/design.md` *The class, enumerated*, at `5c938223` | C1 140 lines in 39 files; C2 20 lines; C3 18 lines; C4 1 line outside `tests/` and 58 hits in `tests/` fixtures; C5 `design`, `Design`, `designs`; C6 830 hits in 77 files, against 852 in 81 at `475653e7` |
| `git grep -n -i 'Read the spec'` at `475653e7` and at `5c938223` | 12 lines at the base; none at the head |
| `python3 -I test_tmp_rule_changes.py <worktree> 475653e7`, a probe in the round's scratch directory, run twice: the first run passed the policy root as a path and `parse` refused it, and the second passed `docs` | 9 operations, 0 parse errors, every `from` found in its section at the base, no `to` there yet; the probe is deleted |
| `python3 evals/scripts/replay_targets.py --list` | no line printed, exit 0 |
| `git ls-tree -r --name-only <tag> seal/specs` and `seal/threads`, for `v0.22.3`, `v0.23.0` and `v0.23.1` | round records under `seal/specs/`: 173, 0, 0; under `seal/threads/*/trail/rounds/`: 0, 7, 7 |
| `bin/test -q` over 118 modules: every module under `tests/` naming a changed file by path or by a non-generic basename, plus `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py` and `tests/test_censuses.py` | 5712 passed, 14 skipped, exit 0 |
| `bin/seal layout --check` | exit 0 |
| `bin/seal rules --check` | exit 0 |
