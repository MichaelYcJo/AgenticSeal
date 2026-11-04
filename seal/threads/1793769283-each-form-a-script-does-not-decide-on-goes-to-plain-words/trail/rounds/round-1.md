# Review round 1: 1793769283-each-form-a-script-does-not-decide-on-goes-to-plain-words

```seal
target: 415acf037 against origin/release/v0.31.1
```

This round read the branch at `415acf037` against `c186a59ac`, the commit `origin/release/v0.31.1` names, in a `git clone --no-local` checked out at the target. It read the issue (`gh issue view 1319`, body and three comments), `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, the four phase records, and the whole diff outside the work item's directory. No earlier round exists, so no fact was carried and every verdict below was reached here. No `seal/parity.md` is declared, so no parity comparison is owed. `seal/config.md` holds no `Record language` row, so this record is English.

Stage 1 read the build against the issue's *Done when*, the design's S1 to S7, D1 to D6 and C1 to C4, and the reason census R1 to R27. Stage 2 read the four scripts the diff changes (`hooks/lib/fields.py`, `skills/code-review/scripts/chain_check.py`, `skills/settle/scripts/rule_changes.py`, `skills/verify/scripts/unverified_check.py`) and followed each changed return shape to its callers. The axes were inputs (the values each key now takes), exclusions and boundaries (an empty value, an absent line, a first record), error paths (each refusal text the diff changed, and who reads it), response shape (`Parsed` and `nothing_block`'s answer), the committed records a relaxed reader still reads (C1), and the rule text that states each changed form (contract rule 19). Authorization, query scope, state transitions, concurrency and security have nothing to compare here: no changed unit acts as anyone, filters a set, holds state across a call, or takes input across a process boundary that it did not take before.

## Findings

### 1. The first-record refusal tells a proofer whose round 1 wrote a `regression:` or `reopens:` line that what it confirms is prose

```seal
severity: should
location: `skills/code-review/scripts/chain_check.py:871-875`, `tests/skills/test_chain_check.py:1248-1285`, `docs/forms/the-round-record.md:78-79`
evidence: read `skills/code-review/scripts/chain_check.py:863-876`, `tests/skills/test_chain_check.py:1254-1285`
```

Why it matters: `chain_check.py#channel` builds one list of references from a record's `confirms:` lines and its findings' `regression:` and `reopens:` lines (`:863-866`). Every one of them in the first record gets the same refusal. Phase 2 rewrote that refusal in `856a45327` to say "there is no earlier round to name, so what it confirms is prose with no `confirms:` line". For a `regression: round-1#1` line in round 1, that sentence answers a question the proofer did not ask, and it does not say what the record must do: drop the line, since a unit a build phase made is new work and takes neither line (`docs/running/the-run.md` *The run*). The case that pins the new text pins it on exactly that line. In `test_refuses_a_reference_naming_no_earlier_record_or_finding`, `said[0]` is the refusal of `regression: round-1#1` (`:1271`), and `:1282-1285` asserts it carries the confirmations sentence. The base text said "its `confirms:` lines read `none`" and had the same reach. The diff rewrote the message and pinned it, so contract rule 14 makes the new text this work item's. The function's own docstring states the rule the message should state: "the first record writes none" (`:850`).

The snippet below covers the message, its pin and the case's docstring. `docs/forms/the-round-record.md:78-79` says "Round 1 has no earlier record, so it writes no `confirms:` line", which is true but names one of the three lines. The fix pass owes that sentence the same three names. The paragraph's lines 77 to 79 were left ragged by phase 2's edit, and the same edit can rewrap them.

```python
# skills/code-review/scripts/chain_check.py, in channel()
            if k == 0:
                why = (
                    f"names `{said}` in the first record: there is no earlier "
                    f"round to name, so it holds no `{FIELDS.CONFIRMS}`, "
                    f"`{FIELDS.REOPENS}` or `{FIELDS.REGRESSION}` line, and what "
                    "it confirms is prose"
                )

# tests/skills/test_chain_check.py, test_refuses_a_reference_naming_no_earlier_record_or_finding
        assert all(
            "so it holds no `confirms:`, `reopens:` or `regression:` line" in why
            for why in said[:2]
        ), said
# and its docstring: "... and the refusal in the first record says the
# first record holds no reference line and that what it confirms is prose; ..."
```

For `docs/forms/the-round-record.md`, the sentence at lines 78-79:

```markdown
Round 1 has no earlier record, so it writes no `confirms:`, `reopens:` or
`regression:` line.
```

```seal
verdict: fixed 669d93cab
answer: The message, the case's assertion and docstring, and the form's sentence now read as the paste-ready text gives them, and the paragraph's last lines are rewrapped. The changed assertion failed against the old message before the code changed, and `seal mutate` dropping `regression:` from the message gave red with the tree clean. The fragment says the reworded message in `590664858`.
```

### 2. The implement skill still says a no-change block without `why:` fails the check

```seal
severity: should
location: `skills/implement/SKILL.md:355-360`
evidence: read `skills/implement/SKILL.md:355-360`, `skills/verify/scripts/unverified_check.py:700-716`, `skills/settle/rule-changes.md:47-54`
```

Why it matters: `skills/implement/SKILL.md` *4. The closing memo — only what the diff cannot show* is what a builder reads when it writes `## Not verified`. It says the block is "`- nothing` with its one field `why:`. Any other spelling of the heading, the header row or the block fails the check rather than reporting zero". Since `9f8fe1e62`, `unverified_check.py#nothing_block` takes `why` as optional (`field_values(found[0], (), (WHY,))`, `:715`), so a block with no `why:` line reads and fails nothing. `skills/settle/rule-changes.md:47-50` now says "no script uses it, so none refuses a block that lacks it". The two documents state the block's rule differently. Phase 3 claimed this sentence "stays true" (`trail/phases/phase-3.md`, *Decisions in the build*, the fourth item, and its rule-19 list); read with the sentence after it, it states a refusal that no longer exists. Contract rule 19 asks the commit that changes a fact to correct every sentence that states it. No case pins the paragraph (executed: `git grep -n -E "its one field|Any other spelling"` over `tests`, `docs`, `skills` and `agents`, which lists only the two skill files).

```markdown
**`## Not verified` is read by a machine, so it has one shape** — a
`| Item | Who must answer |` table, or alone the no-change block
`skills/settle/rule-changes.md` *Rule changes* states, `- nothing` with the
reason in its one field `why:`, which the block may leave out. Any other
spelling of the heading, of the header row or of the `- nothing` line, or a
field of the block other than `why:`, fails the check rather than reporting
zero, because zero reads as "everything has been closed". The template's
placeholder row fails it too, until it is filled in or the block replaces
the table.
```

```seal
verdict: fixed b46133128
answer: The paragraph now says the block may leave out `why:`. I read the paste-ready text against `unverified_check.py#nothing_block` and `#field_values`, and wrote it in my own words: the reader also refuses a second item and an empty `why:`, so the sentence names those beside the other spellings and an unknown field. The modules that read the implement skill, with the wrap, passage and `test_unverified_check.py` modules, gave 1021 passed.
```

### 3. `gaps.md` keeps the process-rows item open after the orchestrator's judgment row accepted the rows

```seal
severity: should
location: `seal/threads/1793769283-each-form-a-script-does-not-decide-on-goes-to-plain-words/gaps.md`
evidence: read `seal/threads/1793769283-each-form-a-script-does-not-decide-on-goes-to-plain-words/gaps.md:14`, `seal/threads/1793769283-each-form-a-script-does-not-decide-on-goes-to-plain-words/frame/plan.md:81`
```

Why it matters: `gaps.md:14` holds an open `## Not verified` row: the `### Process changes` rows of `changelog.md`, to be answered by "the orchestrator, before the broad run". `frame/plan.md:81`, written at `415acf037`, records that the orchestrator "read both rows against the diff and accepts them". So the plan says the item is answered, and the memo still lists it as unverified. `seal unverified` counts the row as open, and `seal pr-body` copies it into the pull request body, where a reader on GitHub sees a pending item that the records elsewhere settle. `docs/forms/the-round-record.md` *A finding's `verdict:` decides it* makes a wrong line of a work item's record that a script reads or copies a `should`. An item is closed by marking it, never by deleting it (`skills/implement/SKILL.md` *4.*). The fix touches the work item's records alone, so the records arm lets a `fixed` close of it stand without a verifying round.

```markdown
| closed The `### Process changes` rows of `changelog.md`; the spawn said the orchestrator would hand them and the prompt carried none, so phase 4 derived them from the diff (`trail/phases/phase-4.md`). The orchestrator read both rows against the diff and accepts them (`frame/plan.md` *Judgments of the run*, the row on G8) | the orchestrator, before the broad run |
```

```seal
verdict: fixed 590664858
answer: The row now opens with `closed`. Its second cell says what closed it, the orchestrator's acceptance in the plan's last judgment row, and not the original answerer, which the implement skill's section 4 says leaves a closing unproven; that is where this differs from the paste-ready row. `seal unverified` on the work item exits 0.
```

## Confirmations

What matched: S6, the measurement. The design's command at `c186a59ac`, `3114868c1` and `415acf037` prints every figure of phase 4's file table, and the party sums and the template total (179 lines, 4911 characters, to 172 and 4764) follow from them. Every agent's `skills:` list at the base names `core` and `agent-contract` alone, which is what the design measures. No measured file changes between `3114868c1` and `415acf037`. The changelog's figures match the table. Executed: the `git show <commit>:<path>` and `wc -lm` loop over the sixteen files at the three commits, and `git diff --stat 3114868c1 415acf037` over `agents`, the core, the contract and `templates/records`, which is empty.

What matched: S5, the reason census. At HEAD the core lacks R2's clause and R4's clause, the contract's preamble lacks R11's test and cites `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each*, rule 1 lacks R12's sentence, and rule 9 lacks R17's sentence and keeps R19 as one clause citing `docs/checks/the-routing-check.md` *The edit check*. R11's and R12's homes hold the moved facts at `docs/running/the-agent-set.md:15-22`, and R19's home states the whole fact at `docs/checks/the-routing-check.md:72-78`. Read: the diff of both preload files. Executed: `git grep -n -F` outside `seal/threads/` on "sits above them", "separate agents because", "Two reasons point", "trailer arm is left", "per-role exception" and "failure is a habit", which lists only the two lines in `docs/running/the-agent-set.md`. The kept rows read as their grounds say.

What matched: S3 for `confirms: none`. `git grep -n -F 'confirms: none'` outside `seal/threads/` lists only the C1 readers phase 2 names: the fixtures of `tests/evals/test_replay_targets.py`, `tests/evals/test_noninferiority.py` and the labelled record in `tests/skills/test_chain_check.py`, the new `test_fields.py` case, and the template case asserting the line is gone (executed). No eval grader names the form (executed: `git grep` over `evals/behaviour` outside the scaffolds).

What matched: S7 and C1. `fields.read` over every round record, guarantee and gate record under `seal/threads/` at `415acf037`, 50 files, returns no refusal (executed). The relaxed shapes only widen what reads, so no committed record can newly fail them.

What matched: the callers of the changed return shapes. Phase 3 claimed no caller outside the tests used `Parsed.nothing` or `nothing_block`'s reason. `git grep` over `*.py` lists `nothing_block`'s callers as `rule_changes.py:228` and `unverified_check.py:737` alone, and `chain_check.py:1317-1330` and `settle.py:1225-1236` read `Parsed` by attribute, `ops`, `errors` and `unread` only (executed, then read). Phase 2 claimed no script used a finding's `severity:` or `evidence:` value. Outside the tests, `SEVERITY` and `EVIDENCE` appear only in `fields.py` (executed: `git grep`), and `evals/scripts/behaviour.py:83` pins `severity: \S` for the graders, which the new any-text shape does not contradict.

What matched: S4, the invariant readers. The D1 readers decide on the same inputs as at the base. The diff changes `channel`'s first-record refusal text (finding 1) and the `confirms:` shape message, and both still refuse what they refused before. `fields.py`'s finding block still opens with `severity:` and still requires `location:` (read: the diff of `fields.py` and `chain_check.py`).

What matched: the frame arm. Phase 2 claimed a `<who>` placeholder is still refused by the comparison with `framer`. `chain_check.py#frame` (`:1044-1056`) compares the mark's who and each reframe's who with `framer`, and `test_reads_who_alone_of_the_mark_and_each_reframe` holds both outcomes. No other script reads `MARK_RE`, `REFRAME_RE` or `frame_foot` (executed: `git grep`), so the round group turning from an integer to text reaches only the message.

What matched: the guarantee's D5 row. The crafter claimed the template edit in `3114868c1` removed only the `| Field | Value |` table with its `| Broad gate |` row. `git show 3114868c1 -- templates/records/sdd-guarantee.md` shows those four lines removed and nothing else. `agents/sealer.md` step 1 reads the gate record itself, and no sealer grader reads the row (executed: `grep` over `evals/behaviour/sealer/*/graders`).

What matched: S1 for family A's script constants, a spot check. Phase 2 claimed 66 upper-case constants in `chain_check.py`; an `ast` walk at `c186a59ac` and at `41bb0b456` lists 74 (executed). The count is an aggregate. Every constant the record's sets do not name is a path or module handle, a record file name its row's reader opens, a message of a row, or a reading of git or GitHub (read: `chain_check.py:143-237`, `:665-666`, `:1764-1790`), so no form lacks a row.

What matched: the phase records' own claims on cases that left. Each case phase 2 to phase 4 removed is gone from `.test_durations` too, and the narrow runs in `## Probes` pass at the target.

The new case `test_reads_the_lines_only_agents_read_whatever_they_say` covers what no other case of `Test_record_findings` or `tests/hooks/test_fields.py` covers: a block with any severity word, without `evidence:`, and a close without `answer:`. `test_the_proofer_and_the_review_skill_name_every_line_a_finding_needs` no longer asserts that `evidence:` is among the needed keys, so no case now pins that the proofer's step 7 names the line. The frame states no fact that would need that pin, so this is no finding (`tests/skills/test_chain_check.py:4238-4259`).

`skills/code-review/SKILL.md:150-155` still says the check refuses a block that "lacks a line it holds one of". In `fields.py`'s vocabulary that is a key whose count is one, so after `0b1879e82` it covers `severity:`, `location:` and `verdict:` alone, and the sentence holds.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether any refusal phase 2 and phase 3 removed (the severity and evidence shapes, the refusal of an absent `evidence:`, `answer:` or `why:`, the mark's date and round checks) caught a real record before it was committed. D3's first prong takes a branch that reads only its form's shape whatever it caught, and a catch by the proofer's own run of the check or the orchestrator's preflight lands in no record, so the records cannot answer it | `trail/phases/phase-2.md`, `trail/phases/phase-3.md`, the census rows | the repository owner, by the measurement over the hygiene workflow's runs that `gaps.md` already names for the D6 rows |
| S1 for families B and C beyond the spot check above: this round did not re-run M2 and M3 over the nine family B scripts, the agent definitions and every grader | `trail/phases/phase-3.md`, `trail/phases/phase-4.md`, *The enumeration methods, as I ran them* | the sealer, at its sample of the crafters' `executed` claims (`agents/sealer.md` step 3) |
| Whether an agent acted on a reason this work cut from the preload or moved out of it | `skills/core/SKILL.md`, `skills/agent-contract/SKILL.md` | the repository owner (`gaps.md`, its second row) |
| Phase 4's edit of `templates/records/sdd-guarantee.md` through a Python substitution, a departure from contract rule 9 the crafter disclosed. Its content is right (Confirmations); whether the departure needs an act beyond its disclosure is not this round's to decide | `trail/phases/phase-4.md`, *Decisions in the build*, the last item | the orchestrator |
| The full suite, the repository-wide lint and the format check at HEAD; the build's label for them is `unverified`, which is honest, since every phase names only narrow and boundary runs | `gaps.md`, its first row | the orchestrator, at the one broad run after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_chain_check.py -q -k "channel or Test_frame or record_findings or round_of or template_is_the_record"` | 32 passed, exit 0 |
| `bin/test tests/behaviour/test_docs_line_wrap.py tests/skills/test_unverified_check.py tests/skills/test_rule_changes.py tests/hooks/test_fields.py tests/behaviour/test_the_sealer_guarantees.py -q` | 652 passed, exit 0 |
| `python3 -I -c` loading `hooks/lib/fields.py` and reading every `trail/rounds/round-*.md`, `guarantee.md` and `trail/gate.md` under `seal/threads/` with its kinds | 50 files, no refusal |
| `git show <commit>:<path>` into `LC_ALL=en_US.UTF-8 wc -lm` for the sixteen measured files at `c186a59ac`, `3114868c1` and `415acf037` | every figure equals phase 4's table |
| an `ast` walk of `chain_check.py`'s top-level upper-case assignments at `c186a59ac` and `41bb0b456` | 74 at each |
