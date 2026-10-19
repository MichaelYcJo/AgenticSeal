# 1792368013-the-scribe-is-written-anew-from-its-job — review round 1

target: d3a59161 against release/v0.22.2

## Findings

### 1. `legacy-parity`'s resolution-order rule names an enforcer that reads none of it

severity: should
location: `skills/legacy-parity/SKILL.md:33-38`, `tests/test_review_axes.py`
verdict: open

The rule under *The migration config* is the half of S4 every reader of the
skill opens: where no original resolves, the caller asks the user, and a
reader that cannot ask returns `original not found`. Its `Enforced by:` line
names `tests/test_chain_hooks_hardening.py::test_parity_declaration_is_bootstrappable_not_hand_written`.
That case opens `templates/parity.md`, `skills/implement/orchestration.md`
and `skills/parity-setup/SKILL.md`, and never this skill
(`tests/test_chain_hooks_hardening.py:285-316`, read). So `bin/rules --check`
resolves the target and the line vouches for a rule no case holds. The S4
defect is exactly the one that comes back unseen: a later trim that restores
*ask the user and record the answer* as the reader's own step.

Claimed: `phases/phase-1.md` §*`Enforced by:` per rule* says the rule has a
case, the one that "reads the template's fields and `parity-paths.md`".
Found: that case reads the template's fields, and nothing of the rule.

Executed, in a clone at d3a59161: I replaced lines 35-37 with the base's
wording, *Where none resolves, ask the user and record the answer.*, and
dropped *A comparison against a guessed original proves nothing.* With that
change, `bin/test` over `tests/test_chain_hooks_hardening.py`,
`tests/test_review_axes.py`, `tests/test_the_record_is_written_in_words.py`,
`tests/test_a_moved_rule_leaves_its_definition.py`,
`tests/test_docs_line_wrap.py` and
`tests/test_no_passage_is_pasted_into_a_second_file.py` exited 0 with 339
passed, and `bin/rules --check` exited 0. T3 holds the scribe's side only
(`tests/test_a_moved_rule_leaves_its_definition.py:570-598`, read).

Executed: the case below, run as a `test_tmp_` probe, passed on the tree at
d3a59161. Its clause check returned a non-empty list on the mutation above,
so the case is red against that mutation. The re-pointed line is 15 bytes
shorter than the one it replaces, which matters because the read set has 81
bytes of headroom (finding 3 says how the three fixes add up).

```python
# tests/test_review_axes.py, after test_the_record_of_a_comparison_names_its_writer
def test_the_resolution_order_ends_with_the_caller_asking():
    """S4 of #970, the skill's half: the order ends with the caller asking
    and recording, and a reader that cannot ask returns `original not
    found`. T3 holds the scribe's half; this is the text every reader of
    the skill opens, and the base's wording made the reader ask."""
    text = read("skills", "legacy-parity", "SKILL.md")
    heading = "\n## The migration config\n"
    assert heading in text, "`legacy-parity` lost its migration-config section"
    body = " ".join(text.split(heading, 1)[1].split("\n## ", 1)[0].split())
    for clause in (
        "it lives in `~/.claude/specseal/parity-paths.md`",
        "the caller asks the user and records the answer",
        "a reader that cannot ask returns `original not found` with what it tried",
        "A comparison against a guessed original proves nothing.",
    ):
        assert clause in body, f"the resolution order lost {clause!r}"
```

```markdown
Enforced by: tests/test_review_axes.py::test_the_resolution_order_ends_with_the_caller_asking
```

The second block replaces `skills/legacy-parity/SKILL.md:38`. Precondition:
see the new case red first (contract §15), for example with the mutation
above, before it is committed.

answer:

### 2. A section the scribe is told to read tells its reader to write a test

severity: should
location: `skills/legacy-parity/SKILL.md:66-69`, `agents/scribe.md:27-28`
verdict: open

The scribe's step 1 sends it to read *The original's coordinates*
(`agents/scribe.md:27-28`). The skill's opening says those sections "find and
trace the original" and that "the sections that judge and record are its
caller's" (`skills/legacy-parity/SKILL.md:15-17`). That section still says,
addressed to whoever reads it, "Start every comparison there instead of
searching the original, and pin what it settles with a test"
(`:67-68`). Writing a test is a durable write. The scribe's `## Never`
forbids it ("Write a file outside a probe"), so the scribe now meets two
instructions in conflict.

The frame says this should not happen. `spec.md` §*Grounding*, the row for
#2's C1 and C2: "The rewritten skill says which of its sections the scribe
reads, so a scribe opening it at step 1 is not told to judge or to write."
Read: the other two sections the scribe reads hold no instruction to write.
*The migration config* gives asking and recording to the caller, and *What
the original sends* addresses the porter ("needs no reproduction") without
asking for a write. This sentence is the one exception.

This fix adds 8 bytes to the skill and keeps every line under 88 columns.

```markdown
A spec's Grounding cites the original's coordinates for the clauses in scope.
Start every comparison there instead of searching the original; the caller
pins what it settles with a test. A suspect coordinate is opened at the baseline:
`git show <baseline>:<path>`.
```

answer:

### 3. Two steps of the trace to the response were dropped, and `## Removes` names neither

severity: should
location: `skills/legacy-parity/SKILL.md:57-61`, `agents/scribe.md:33`
verdict: open

Two instructions the old texts stated are not moved anywhere and are not
listed under `spec.md` §*Removes*:

- The base skill said "Check git history too — if the original later fixed a
  behavior, the fix is its final intent" (`git show
  b196fe9b:skills/legacy-parity/SKILL.md`, read). The rewrite keeps the
  condition and drops the step: "Where the original later fixed a behavior,
  the fix is its intent" (`:60-61`). Nothing tells a reader to look, so a
  scribe tracing an axis finds a later fix only by chance.
- The base scribe's step 3 said "Note mid-layer conditions that never affect
  the response as exactly that" (`git show b196fe9b:agents/scribe.md`,
  read). That is a reporting instruction for the fact-finder. The new step 4
  reads "Trace each axis to what the original sends the client"
  (`agents/scribe.md:33`), and the skill section it reads says only that
  such a condition "needs no reproduction" (`:59-60`). That wording speaks
  to a porter and leaves the scribe free to omit the condition, so the caller
  loses a fact the old report carried.

Read: `## Removes` lists the narration under the three-way table and the
other cut passages row by row. Neither of these is among them, and
`phases/phase-1.md` and `phases/phase-2.md` record no decision to drop them.

The fix puts both back in the one section the scribe and the porter both
read. It adds 14 bytes to the skill. Fixes 1 to 3 together move the read set
by +7 bytes (-15, +8, +14), which leaves 74 of the 81 bytes of headroom. The
fix pass re-runs `bin/payload-meter --agent scribe` and states the figure.

```markdown
Where storage, query conditions and response assembly disagree inside the
original, its behavior is what it sends the client. Trace from the endpoint to
the finished response; a mid-layer condition that never changes the response
is reported as such and needs no reproduction. Read the original's history: a
later fix is its intent, and cloning the version before it preserves nothing.
```

answer:

## Confirmations

confirms: none
Nothing is carried from an earlier round, since this is round 1. I found the
frame's coordinates again by their words, not by line number. Every figure and
grep below was re-run in a `git clone --no-local` at d3a59161, apart from the
rows labelled read.

confirms: none
The byte figure holds. Executed: `bin/payload-meter --root <clone> --agent
scribe` printed a total of 34,697 B: `agents/scribe.md` 3,319,
`skills/agent-contract/SKILL.md` 16,603, and the `CLAUDE.md` pair 14,775.
`wc -c` gives `skills/legacy-parity/SKILL.md` 5,688 B. The agent's share of
the read set is 3,319 + 16,603 + 5,688 = 25,610 B. The baseline is
`git show 43cbc361:<file> | wc -c`: 3,763 + 5,325 + 16,603 = 25,691 B.
1d665d48 is not in the clone, so I measured at 43cbc361, which `spec.md`
gives as the same tree outside `seal/specs/`. `git diff --stat 43cbc361
b196fe9b` over the three files and `CLAUDE.md` printed nothing. The claimed
25,610 against 25,691 matches, with 81 B to spare.

confirms: none
No checker or hook reads the four old parity labels. Executed: `git grep`
for U+1F534, U+1F7E1, U+1F7E2, U+2753, *differs from original* and *out of
verified scope* across `hooks/`, `skills/`, `bin/`, `tests/`, `templates/`,
`docs/`, `agents/` and `evals/`. The hits that remain are round-record
markers cited in code comments, and `evals/scripts/replay_targets.py:60`,
which reads round-record markers and not parity labels. The one
`out of verified scope` hit is the scribe's own report row
(`agents/scribe.md:38`). No code reads a `seal/parity.md` field by name
(`git grep` of the four field names over `hooks/`, `skills/*/scripts`,
`bin/` printed nothing), so the `Policy root` placeholder changes nothing a
parser does.

confirms: none
The sentence naming the parity mark's writers contradicts neither the
wake/quiet table nor the gate. Read: `skills/implement/orchestration.md:457-460`
quiets the parity arm on "the parity mark stands at HEAD, written by a
recorded comparison against the original", which names no writer.
`hooks/gate.py:59` and `:206` and `hooks/commit-review-gate.py:1217` and
`:1228` read the mark file and name the procedure, which `plan.md`
Alternative J keeps. `agents/warden.md:37-39` names the write. The smith's
definition names none (`agents/smith.md:33-34` opens the skill only to
judge), and the scribe's `## Never` forbids it. The parity ask a smith's
commit meets is Q1, filed as #988.

confirms: none
The B5 sites and S7 hold. Executed: `git grep -n 'docs/policies' --
':!seal/specs' ':!changelog' ':!tests' ':!.test_durations'` prints only
`skills/implement/orchestration.md:52`, the sentence saying not to create it.
Read: `templates/parity.md:16`, `skills/parity-setup/SKILL.md:42-44` and
`skills/implement/orchestration.md:238-239` each read a directory the tree
already has, or `none`.

confirms: none
The README class and `seal.py` are enumerated. Executed: S10's `git grep`
printed nothing (exit 1). A `git grep` for the smith as the party that asks,
creates, sets up or bootstraps, over `hooks/`, `skills/`, `bin/`,
`.github/scripts`, `docs/` and `templates/`, finds no sentence beyond the
eight README lines and `skills/implement/scripts/seal.py:678`, all of which
now name the session. A `git grep -w scribe` outside records and tests finds
no other sentence saying the smith spawns the scribe.

confirms: none
The rows of `## Removes` are carried out as named. Read: the scribe's
`skills:` entry, its contract paragraph, *Called by smith*, the parenthesis
and the §6 paragraph, the four labels, the field table, the reader's *ask
the user*, the narration under the three-way table, both skip entries with
the code that read them, the line-wrap docstring lines, the follow-up row and
the README cells are each gone, and each removal lands where the table says.

confirms: none
The new cases were read against their groups, and each covers something its
group does not. T3 mirrors `test_the_smiths_four_rules_stand_with_their_enforcers`
for the scribe. T4 reads words that the emoji case
(`test_no_file_an_agent_reads_carries_an_emoji_or_a_proof_block`) cannot
see. T5 is the only case reading `legacy-parity` §*Recording the
comparison*. `test_the_refusal_names_the_session_as_the_one_that_asks`
asserts the sentence, which `test_everything_else_refuses_where_there_is_no_root`
never reads.

confirms: none
The touched modules are green at d3a59161. Executed through `bin/test` (see
`## Probes`). The suite stays `unverified` until the orchestrator's broad
gate runs.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether a scribe spawn opens `legacy-parity` at step 1, reads only the three named sections, returns facts and no verdict, and returns `original not found` where the original does not resolve. No case runs the scribe (#957's Q3) | `agents/scribe.md` | the repository owner, at the first parity run |
| The full suite, the repository-wide lint and the typecheck on this branch | the branch at d3a59161 | the orchestrator's broad gate, after the rounds settle |
| Whether the read set still holds after the fix pass. Fixes 1 to 3 are worked out to add +7 B against 81 B of headroom, and nothing measured them as applied | `skills/legacy-parity/SKILL.md` | the fix pass, by `bin/payload-meter --agent scribe` |

## Probes

| Command | Result |
|---|---|
| `bin/payload-meter --root <clone> --agent scribe` | exit 0; total 34,697 B, with `agents/scribe.md` 3,319 and `skills/agent-contract/SKILL.md` 16,603 |
| `bin/test tests/test_review_axes.py tests/test_the_record_is_written_in_words.py tests/test_every_agent_reads_the_contract.py tests/test_docs_line_wrap.py tests/test_a_moved_rule_leaves_its_definition.py tests/test_absence_claims.py tests/test_a_probe_that_commits_says_so.py tests/test_no_passage_is_pasted_into_a_second_file.py -q -p no:xdist` | exit 0; 318 passed, 1 skipped (the framer's `NOT_YET_REWRITTEN` entry) |
| `bin/test tests/test_chain_hooks_hardening.py -q -p no:xdist -k "readme_group_counts or parity_declaration"` | exit 0; 2 passed |
| `bin/test tests/test_the_mode_is_a_row_and_a_command.py -q -p no:xdist -k "refus"` | exit 0; 33 passed |
| `bin/rules --check --root <clone>` | exit 0 |
| `skills/legacy-parity/SKILL.md:35-37` replaced with the base's *ask the user and record the answer*, then `bin/test` over six modules and `bin/rules --check` | both exit 0, 339 passed: nothing caught it (finding 1); file restored by `git checkout` |
| `tests/test_tmp_resolution_order.py`, finding 1's clause check against the tree and against the mutation | exit 0, 2 passed: the clauses are present on the tree and missing under the mutation; file deleted |
