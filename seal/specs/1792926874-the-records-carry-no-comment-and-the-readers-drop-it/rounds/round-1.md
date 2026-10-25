# Review round 1: 1792926874-the-records-carry-no-comment-and-the-readers-drop-it

target: 62e0b133 against release/v0.22.4

## Findings

### 1. The comment-line refusal's message is pinned by no test, so rewording it passes every case

severity: must
location: `tests/test_unverified_check.py:1371-1380`, `skills/verify/scripts/unverified_check.py:165-168`
evidence: executed `git grep -n -F 'delete the comment' 62e0b133 -- tests evals`, `git grep -n -F 'carries no HTML comment: the' 62e0b133 -- tests evals`, `git grep -n COMMENT_LINE 62e0b133 -- tests`
verdict: open

`spec.md` *Data & interfaces* says of `chain_check.py`: "The new message is pinned by a test (contract rule 14)". Contract rule 14 names the test that pins the new text. Each of the ten test references to the message compares a refusal against the constant itself, `UC.COMMENT_LINE` or `reader.COMMENT_LINE`. That comparison holds whatever the constant says, so an edit that empties or rewords the message passes every case. The two searches for the message's words under `tests/` and `evals/` find nothing. The phase record's `mutation-check` list (`phases/phase-1.md`, 17 mutants) mutates where the refusal stands, never what it says.

The message matters because of who reads it. The changelog fragment tells every consuming repository that `unverified-check` will turn each of its pull requests red on an old overview. This sentence is the whole of what that repository is told to do about it.

The fix pins the words once, in the shared reader's refusing case, `Test_check_text::test_refuses_a_comment_line_at_its_line`. Its last line, `tests/test_unverified_check.py:1380`, becomes the lines below. The other cases can keep comparing against the constant, because what they pin is that each reader uses the one message.

```python
        said = (
            "the line begins with `<!--`, and a record carries no HTML comment: "
            "the check reads one as text, so delete the comment"
        )
        assert UC.check_text(text) == ([], [], [(line, said)])
```

answer:

### 2. The `fence_spans` docstring says no reader of a record keeps a code-span state, and `rule_changes.py#parse` reads a spec with one

severity: should
location: `skills/verify/scripts/unverified_check.py:238-239`
evidence: read `skills/verify/scripts/unverified_check.py:238-242`, `skills/settle/scripts/rule_changes.py:13-20`, `skills/settle/scripts/rule_changes.py:106-115`
verdict: open

The phase-1 docstring says `fence_spans` is "the walk for a reader with no comment or code-span state of its own, which is every reader of a record (#1012)". `rule_changes.py`'s module text, rewritten by the same commit, calls a spec a record. Its `parse` reads that spec through `live_lines(lines, comments=False)` and `liveness(..., spans_cross_lines=False, comments=False)`, which keep the code-span state that #988 needed (`rule_changes.py:106` and `:114`). So the two docstrings state opposite facts about one reader. An agent who changes `parse` and trusts the first one would route it onto `fence_spans` and lose the #988 refusal. The fix narrows the clause to the readers it is true of.

```python
    The walk for a reader with no comment or code-span state of its own:
    `readable`, and through it `check_text` and `chain_check.py` (#1012).
    A reader that has either — `liveness`, and `rule_changes.py#parse`
    through it — walks with `fence_opener` and `fence_closes` directly,
    because whether a line can open a fence at all depends on the state it
    began in.
```

answer:

## Confirmations

confirms: none
S1 holds, re-derived with a separate script, not by running the smith's. The smith claimed 173 files changed with 0 differing. Each of the 173 files `3ae1bbed` changed under `seal/specs/` outside this work item was read twice: the base reader's `readable` on the `f7f5450a` text, and this head's `readable` on the `3ae1bbed` text. The non-blank lines, trailing whitespace removed, agree in all 173. None of the 173 is a `routing.md` (executed, `test_tmp_probe.py` step 2).

confirms: none
The strip removed comment text and nothing else. S1 alone cannot show this, because both readers blank fenced lines: a strip that deleted a fenced block would still pass S1. A diff of each of the 173 files against the base reader's `comment_scan` found that no removed or rewritten line lost text standing outside a comment. Every closed fence is identical before and after. Exactly 11 lines were rewritten rather than deleted (executed, `test_tmp_strip.py`). That matches `phases/phase-1.md`'s 11 insertions and the overview's 11 `NAME NOT IN TREE` markers. `git show f7f5450a:` counts 10 of those markers in that work item's `spec.md` and 1 in its `plan.md`, and `git grep` finds none at the head (executed).

confirms: none
S2 holds. This head's `comment_lines` over every tracked `.md` under `seal/specs/` finds lines in 35 files, every one a `routing.md` (executed, `test_tmp_probe.py` step 7). The phase record claimed the same (35 files, all `routing.md`).

confirms: none
The readers' change alters no reading of a record this tree holds. The base and head readers were run on the same head text. The 84 round records give identical `record_findings` (finding numbers, verdicts and refusals). Every `guarantee.md` gives identical `verdicts_of` and `target_of`, and every `broad-gate.md` gives an identical `newest_run`, none holding a comment line. Every `overview.md` gives an identical `check_text`. That includes `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/rounds/round-5.md` and `round-9.md`, whose fenced comments the strip left. `readable` itself differs only on the 35 `routing.md` files, which `hooks/routing.py#shown` reads and `readable` does not (executed, `test_tmp_probe.py` steps 1, 3, 4, 5).

confirms: none
S11 and Q2 hold more strongly than claimed. The phase record claimed every spec parses. Each of the 42 `spec.md` files parses at the head with no refusal. For each, the head's `parse` returns the same operations, `nothing` value and refusals as the base `parse` returned on the `f7f5450a` original, line numbers aside. So the strip changed no rule-change operation (executed, `test_tmp_probe.py` step 6). `seal/specs/1792627930-the-section-sign-is-still-syntax/spec.md` holds no line-start `<!--` at `f7f5450a`, and `3ae1bbed` leaves it unchanged (executed). That is the overview's ground for 40 stripped specs where the frame said 41.

confirms: none
This spec's `## Rule changes` applies. Its three operations apply to `docs/` at the head on their own, and still apply after `1792628098-tests-rebuilt-one-file-per-module`'s operations, which share *The fold, and what tells it from a deletion* (executed, `test_tmp_replay.py`). Replayed with every spec in id order, it waits behind the stale `from` of `1792619408`, which is #1025 and outside this work item.

confirms: none
Phase 2's reading holds S10, and the `labelled` divergence costs nothing on the corpus. `replay_targets.py --list` was run with the base tree's script and readers (exported from `4d5a6917`, git pointed at this repository) and with the head's. Both printed 144 lines, byte for byte the same (executed). The base export also stands in for phase 2's base `a9d8c93e`, since `replay_targets.py` is the same file at both. `labelled_round` judges a record with `checks_at(at)`, reads its lines with that commit's reader, and asks this tree's check only for labels and the finding split (read: `evals/scripts/replay_targets.py:266-290`). That matches `spec.md` *Scope* item 4. The overview's divergence, `labelled` keeping this tree's reader, rests on the template carrying no label-led line in a comment before 0.22.0. That rests on the smith's `git show <tag>` count, carried and not re-run here, and the identical `--list` above is consistent with it.

confirms: none
The build and `changelog.md` match `questions.md` Q1's default (a). No strip command was added: the diff outside `seal/specs/` is the 14 Python files of readers, evaluation scripts and their tests (executed: `git diff --stat 4d5a6917 62e0b133 -- ':!seal/specs'`). The fragment's third bullet says no command strips the comments and none ships while the owner's question is open.

confirms: none
The refusal stands where `spec.md` *Scope* item 3 places it, and nowhere else. `chain_check.py#read_whole`, `#guarantee` and `#broad_gate` ask `comment_lines`. `unverified_check.py#check_text` refuses the first comment line before looking for any section. `rule_changes.py#parse` refuses only between its section's heading and the next heading of level 2 or above. `seal_stamp.py#_queue_one` and `#queue_for_local_guarantee` take no stamp (read: the diff of the four scripts). One caller of `record_findings` is missing from *Scope* item 2's list: `skills/verify/scripts/broad_gate.py#rounds_rows`. A round record holding a comment line now adds nothing to its deferred row. Its docstring already says that a record the reader refuses anything of adds nothing, so its stated behaviour holds (read: `skills/verify/scripts/broad_gate.py:2514-2550`). `release_seal.py` lists such a record as unread (read: `.github/scripts/release_seal.py:372-376`).

confirms: none
The prose of `docs/`, `skills/`, `agents/` and `templates/` states the removed comment state only in the two sentences `## Rule changes` rewrites: `docs/the-record-layout.md:172-174` and `docs/the-review-record.md:211-215`. Nothing outside `seal/specs/`, `.test_durations`, `changelog/0.8.2.md` and an unrelated YAML reader names `comment_scan` or `strip_comments` (executed: the `git grep` rows under `## Probes`).

confirms: none
The modules the phase records name pass at the head: 1111 passed, through `bin/test -n auto -q` over `tests/test_chain_check.py`, `tests/test_unverified_check.py`, `tests/test_rule_changes.py`, `tests/test_seal_stamp.py`, `tests/test_replay_targets.py`, `tests/test_noninferiority.py`, `tests/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py` and `tests/test_a_phase_hands_the_next_one_a_record.py` (executed). S9's four modules are not in the diff (executed: the `--stat` above), so they pass unchanged as `spec.md` asks. Each new test was read against its group. The `chain_check.py` cases of `Test_comment_lines` and `Test_broad_gate` cover the wrapper's own `readable` call and an accepting `broad_gate` run, which no earlier case covered. None duplicates its group.

Carried rather than re-established: that each new case was seen red against the old code, and the 17 mutants of the phase-1 `mutation-check` (both from `phases/phase-1.md`). This is round 1, so no earlier round carries anything.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and format check, and the typecheck at `62e0b133`, which `overview.md` labels unverified, honestly | the whole tree | the orchestrator, through `broad-gate` after the rounds settle |
| Whether each new case fails against the old code (contract rule 15), carried from the phase records and not re-run | `phases/phase-1.md`, `phases/phase-2.md` | the orchestrator |
| Whether this spec's operations still apply in true merge order once #1025 repairs `1792619408`'s `from` | `spec.md` *Rule changes* | the orchestrator, at the settle after 0.22.4 merges |

## Probes

| Command | Result |
|---|---|
| `git archive 4d5a6917` extracted into the round's scratch directory as the base tree, then removed | the base readers loaded by path beside the head's |
| `python3 -I <scratch>/test_tmp_probe.py` | step 1: `readable` differs on 35 files under `seal/specs/`, all `routing.md`; step 2: S1, 173 files changed, 0 differ, no `routing.md`; step 3: 84 round records, 0 read differently; step 4: no `guarantee.md` or `broad-gate.md` read differently or holding a comment line; step 5: no overview read differently; step 6: 42 specs parse, none refused, none with operations other than its original's; step 7: 35 files hold a comment line, all `routing.md` |
| `python3 -I <scratch>/test_tmp_strip.py` | 173 files; 11 lines rewritten; 0 lines lost text outside a comment; 0 files whose closed fences changed |
| `python3 -I <scratch>/test_tmp_replay.py`, three runs: this spec alone, all 42 in id order, then after `1792628098` alone | alone: applied; in id order: waits behind `1792619408` (#1025); after `1792628098`: applied |
| `python3 evals/scripts/replay_targets.py --list` at the head, and the base export's copy with `GIT_DIR` set to this repository | both exit 0, 144 lines each, `cmp` exit 0 |
| `bin/test -n auto -q` over the eight modules named in the confirmations | exit 0, 1111 passed |
| `git grep -n -E 'comment_scan\|strip_comments' 62e0b133 -- ':!seal/specs'` | `.test_durations` entries, `changelog/0.8.2.md:262`, and a different `strip_comments` in `tests/test_ci_gives_the_checks_what_they_need.py` that reads YAML; no reader of a record |
| `git grep -n -F 'delete the comment' 62e0b133 -- tests evals` | nothing, exit 1 |
