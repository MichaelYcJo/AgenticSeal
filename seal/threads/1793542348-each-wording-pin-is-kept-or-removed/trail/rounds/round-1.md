# Review round 1: 1793542348-each-wording-pin-is-kept-or-removed

```seal
target: e953d0a9 against 361ed0cb
```

The target is the branch at `e953d0a9` against its merge base with `origin/release/v0.27.3`, `361ed0cb`. No earlier round exists, so no fact is carried from one; every fact below was opened or run this round. The review was done in a `git clone --no-local` of the worktree at `e953d0a9`. No `seal/parity.md` is declared, so no parity reading and no `original:` line are owed.

The method for S8, the scenario put to this round: *The listing* of `frame/design.md` was re-run over `git archive` copies of `361ed0cb` and `e953d0a9`. The 109 rows it prints at HEAD were all read, each with the comment lines above its `assert`. The 399 base rows whose literal no longer stands in the same module at HEAD were ordered as the listing prints them, and every eighth was read with its whole `assert` and its case name at `361ed0cb`: 50 rows, spread across the four groups because the listing is sorted by path. The removed half is therefore a systematic sample, not a whole list (contract rule 12). The 349 removed rows outside it are a row of `## Not judged`.

## Findings

### 1. The rule change for the round-cap line says no case reads the cap, while this diff keeps a case that reads the cap's default count as a fact

```seal
severity: should
location: `seal/threads/1793542348-each-wording-pin-is-kept-or-removed/frame/design.md:110`, `seal/threads/1793542348-each-wording-pin-is-kept-or-removed/frame/design.md:13`, `seal/threads/1793542348-each-wording-pin-is-kept-or-removed/frame/design.md:126`, `tests/behaviour/test_chain_hooks_hardening.py:906-908`
evidence: read `seal/threads/1793542348-each-wording-pin-is-kept-or-removed/frame/design.md:11-13`, `seal/threads/1793542348-each-wording-pin-is-kept-or-removed/frame/design.md:104-110`, `tests/behaviour/test_chain_hooks_hardening.py:897-911`, `docs/the-review-record.md:427-428`, `seal/threads/1793542348-each-wording-pin-is-kept-or-removed/trail/phases/phase-4.md:39`
```

Why it matters: the settle writes `## Rule changes` into `docs/` as it stands. After that, the rule *The run* closes at `docs/the-review-record.md:428` will read `check: none reader: the settling session at the dry run's judgments`. Yet a case in the suite reads that rule's default count, and a change to the count turns that case red. The check line then names nobody where a case does read the rule. This is the situation #1216 exists to catch, and this work item would create it.

The grounds, each at its coordinate:

- The claim. `frame/design.md:11` (G5) says `:428`'s one case inside its span "asserts phrases only". `:13` (G7) moves the line to the settling session. `:126` names `#test_the_cap_counts_from_the_last_design_change` as "the round cap's only case". Issue #1277, filed by the orchestrator, repeats the claim: "Its only reading case, `#test_the_cap_counts_from_the_last_design_change`, was a wording pin and is already gone".
- What the tree holds. `tests/behaviour/test_chain_hooks_hardening.py:906-908`, at `e953d0a9`, keeps `assert "three finding rounds by default" in record`. `record` is `docs/the-review-record.md`, flattened. The literal stands in the bold lead sentence at `:427`, which is the rule `:428` closes. The comment above the assert names the fact: "The value three, the finding rounds at which the orchestrator weighs whether the run still pays".
- Phase 4 kept the assert as a value: `trail/phases/phase-4.md:39` ("kept as a value"). That reading matches *The criterion*'s "a number a person waits on", and phase 3 ruled the cap of four options the same way. This round finds the ruling sound. The rule change written before the build therefore no longer matches the build.
- The line names only `tests/text/test_the_rules_have_one_owner.py`, so `seal rules --check` sees nothing wrong (it passed, executed). That check cannot tell a target that reads its rule from one that does not (`plan.md` A8).

The fix keeps phase 4's ruling and names the module that still reads the rule in the `to:` value. The `from:` and `to:` sentences stay as they are, so `rule_changes.py#parse` reads one `change` as before. The other repair, ruling `:908` as wording and removing it, would contradict the ruling the plan itself gives for the cap of four options.

```markdown
- change
  file: docs/the-review-record.md
  section: The run
  from: No person is asked mid-run.
    check: tests/text/test_the_rules_have_one_owner.py
  to: No person is asked mid-run.
    check: tests/behaviour/test_chain_hooks_hardening.py
```

In the same commit, G7 (`frame/design.md:13`) and the `## Removes` row at `:126` say that the case reading the cap's default count is `tests/behaviour/test_chain_hooks_hardening.py#test_the_run_names_its_default_round_count_and_the_follow_up_file`, which stays. The orchestrator corrects the matching sentence of #1277, which the fix pass cannot edit.

### 2. The changelog fragment says a reworded rule no longer turns these cases red, but each kept assert still matches its whole literal

```seal
severity: should
location: `seal/threads/1793542348-each-wording-pin-is-kept-or-removed/changelog.md:3`
evidence: executed `S=<round>/t-e953d0a9 python3 -I <round>/audit.py pins -v`, `python3 -I <round>/show_kept.py <round>/pins-e953d0a9.txt <round>/clone`
```

Why it matters: the release note tells maintainers that "A rule reworded with its meaning unchanged no longer turns these cases red". "These cases" can only mean the cases of the 56 modules. Of those cases, the ones holding the 107 kept asserts still match their literal whole, the fact together with the words around it. Some examples at `e953d0a9`:

- `tests/behaviour/test_a_release_is_sized_by_a_criterion.py:165` matches `Three or four is a ceiling, not a target.`, and only the count is the fact.
- `tests/behaviour/test_a_commit_names_its_repository.py:44` matches `absolute path written out after `git -C`, in a command of its own`, and only `git -C` is the fact.
- `tests/behaviour/test_first_setup_asks_once.py:244` matches `*The criterion for choosing a value* owns the criterion`, and only the citation is the fact.

Reword "not a target" or "owns the criterion" without changing the meaning, and each of these turns red. *The criterion* of `frame/design.md` accepts this on purpose: a literal holding a code span inside a sentence is kept, and its comment names the span. The build is therefore right. The release note claims more than the build delivers, and a maintainer who believes it is surprised at the next rewording.

```markdown
A removed case no longer turns red when a rule is reworded with its meaning unchanged. A kept assert still matches its literal whole, the fact with the words beside it, so rewording those words turns it red, and its comment names the fact to keep. The proofer reads a rule's wording at review, as `docs/what-a-script-gates.md` *The checks* states.
```

This text replaces the sentence that opens "A rule reworded with its meaning unchanged" at the end of the first bullet of `changelog.md:3`.

## Confirmations

```seal
confirms: none
```
What matched: S1. *The listing* printed `pins 506 in 56 modules` at `361ed0cb` and `pins 109 in 43 modules` at `e953d0a9` (executed, *Probes* rows 1 and 2). Of the 109 HEAD rows, 108 have a comment directly above the `assert`. The 109th is `tests/text/test_a_gate_that_fails_says_so.py:25`, which Scope item 7 keeps whole (executed, row 3). The phase records' kept and removed counts per group, 18/129, 47/66, 21/108 and 21/96, add up to 107 and 399, which is 506 (read: `trail/phases/phase-1.md:17`, `phase-2.md:39`, `phase-3.md:16`, `phase-4.md:28`). Matching base rows to HEAD rows by module and literal also leaves 399 base rows unmatched (executed, row 4).

```seal
confirms: none
```
What matched: S8, the kept half, read in full. All 107 kept listed asserts and phase 2's two literals taken out of their tuples were read, each with its comment. Each comment names one of *The criterion*'s kinds and a reader, and each literal holds that fact:

- Citations a reader resolves: the *Branch names* citation at `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:195`, and `docs/release-checklist.md` *6. After the merge* at `tests/text/test_the_release_tail_does_not_end_at_the_tag.py:221`.
- Commands: the `gh issue list --label flow-measurement` pair at `tests/text/test_a_segment_feeds_the_flow_log.py:159` and `:226`, and `git reset -- :/seal` at `tests/text/test_the_settings_have_a_front_door.py:63`.
- Spellings a parser matches: the `Verdict: withheld reason:` lines at `tests/behaviour/test_the_sealer_guarantees.py:168` and `:190`, and the routing answers at `tests/behaviour/test_waiver_decided_at_start.py:152` and `:707`.
- Program output: the refusals the script modules print, for example `tests/skills/test_chain_check.py:3033` and `tests/hooks/test_config.py:724`.

The three asserts held back under Scope item 9 say in their comments that they are phrases kept for a `docs/` line: `tests/text/test_broad_gate_rule.py:65`, `tests/text/test_a_rider_reaches_its_file.py:88` and the loop in `tests/text/test_settle_reads_before_it_removes.py`. Issue #1277 lists all three (executed: `gh issue view 1277`). Finding 2 concerns what the changelog says about these asserts, not whether keeping them was right.

```seal
confirms: none
```
What matched: S8, the removed half, in the systematic sample of 50 named above (executed, row 4; read at `361ed0cb`). Each of the 50 pins a phrase of a rule. Examples:

- A lead sentence: `**The stated limit: ...**` (`tests/text/test_the_rules_have_one_owner.py:336`) and `**What the person's screen shows is not checked` (`tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:260`).
- A clause: `You ask nobody anything` (`tests/behaviour/test_waiver_decided_at_start.py:679`) and `never back to the framer` (`tests/behaviour/test_chain_hooks_hardening.py:1096`).
- A heading in its own file: `## The broad gate` (`tests/text/test_broad_gate_rule.py:51`).

Six sampled literals hold a code span, and for each the assert is about what the rule decides, not about the span:

- `still answers `the session`` (`tests/behaviour/test_waiver_decided_at_start.py:259`).
- `Commit, then run `seal mutate` over each unit that adds behaviour.` (`tests/text/test_the_handoff_before_round_one.py:129`).
- `the last `trail/rounds/round-N.md` has no finding open` (`tests/text/test_broad_gate_rule.py:95`).
- `A settle opens no directory under `seal/threads/`` (`tests/text/test_settle_reads_before_it_removes.py:203`).
- `and whose `target:` commit is HEAD, ...` (`tests/text/test_the_rules_have_one_owner.py:610`).
- `size: now` says this ticket ...` (`tests/behaviour/test_a_release_is_sized_by_a_criterion.py:228`).

Where a span is something a reader types, another case still holds it. The label `size: now` stays as `LABEL` in `tests/github/test_close_issues_on_release.py:66`. The `seal mutate` command line stays in `tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py` (read).

```seal
confirms: none
```
What matched: phase 4's removal of `join it to the commit with `&&` and nothing else` (`361ed0cb:tests/behaviour/test_a_commit_names_its_repository.py:41`) applies the frame's own ruling. `frame/design.md` G6 reads an operator the agent copies, when no command form stands in the literal, as the rule's meaning, and it rules on `&&` in the fixture chain that way. The kept `git -C` assert at `:44` holds rule 16's command form (read).

```seal
confirms: none
```
What matched: phase 2's judgment, put to this round, holds: an exit-code or value comparison in a script case takes no comment. *The criterion* rules an assert by "its literal", S1 asks a comment only of the asserts the listing prints, and `assert code == 1` or `assert [c[1] for c in cl] == [...]` carries no literal standing in a rule file. A scan of every test function the diff touched found 46 asserts comparing a literal of two words or more with no comment above (executed, row 5). Every one of them falls into one of these:

- Program output in a script module, for example `tests/skills/test_settle.py:1426-1441` and `tests/github/test_release_completeness_check.py:233-244`.
- A locator for kept asserts: `"## Branch names" in text` at `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:188`.
- An assert next to a commented citation: `"step 4"` at `tests/behaviour/test_the_sealer_guarantees.py:269`.
- An assert in a case that held no listed assert, whose docstring alone changed: for example `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py:81`. *Scope* (Out) leaves these out.

```seal
confirms: none
```
What matched: phase 4's judgment, put to this round, holds. The removed case `361ed0cb:tests/behaviour/test_unverified_rows_close.py#test_a_text_saying_a_row_counts_open_names_the_open_item_that_reads_closed` asserted two program outputs: `check_file` on a section with `| closed issues are not re-read | the owner |` gives one open row, and gives `["issues are not re-read"]` as closed. `tests/skills/test_unverified_check.py:1023`, run through `Test_parse_section#test_accepts_open_rows_and_the_word_that_closes_one` at `:1048-1054`, asserts the same two results for the same row. `check_file` reaches the same reader through `check_text` (`skills/verify/scripts/unverified_check.py:839-851`). So the removed case held a copy of one fact, and its listed assert was wording (read).

```seal
confirms: none
```
What matched: S2, S3 and S4, and the check-line question this round was asked to cover:

- `bin/seal rules --check` exited 0 with `all 283 check lines in 55 rule files hold.` (executed, row 6).
- `git grep -n` for each of the three deleted modules outside `seal/threads` exited 1, so no `check:` line under `docs/`, and no other line, names a removed module (executed, row 7).
- `git diff --stat 361ed0cb..HEAD -- docs` is empty: the diff changes no line under `docs/` (executed).
- The 19 changed check lines are the 19 `-`/`+` pairs in `agents/` and `skills/` (executed, row 8).
- `.test_durations` loads, holds 6045 keys and is byte-equal to its sorted dump (executed, row 9).
- Of the 171 case names the diff removed or renamed, none stands outside `seal/threads` (executed, row 9).
- The changelog's counts match the phase records (read): 110 cases leave (40+23+20+27) and 61 are renamed (8+14+19+20).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The 349 removed listed asserts outside this round's every-eighth sample. The sample found no misruled row, but a sample is not the whole list | the base rows *The listing* prints at `361ed0cb`, less the 50 read | the orchestrator, who decides whether a wider sample is worth a round |
| A comment or docstring that states a removed fact in words that name neither the case nor its module. One keyword search over the touched modules was run (executed, row 10), and the class is unbounded in its spellings | the 53 test modules the diff modifies | the sealer, reading the diff against the issue |
| The full suite. The crafters label it `unverified`, which this round finds honest: each phase record names its narrow run and leaves the rest to the gate. This round ran no test module | the whole suite at `e953d0a9` | the orchestrator, by `seal gate --base origin/release/v0.27.3 --record seal/threads/1793542348-each-wording-pin-is-kept-or-removed` |
| The 13 `docs/` lines G5 read by the names of their modules' cases rather than the cases whole, and whether each still has a reader | `frame/design.md:11` | the settling session at the settle after 0.27.3, with #1277 |

## Probes

`<round>` below stands for the round's scratch directory, `<scratchpad>/1793542348-each-wording-pin-is-kept-or-removed/round-1`, and `<clone>` for the clone inside it. Every file named here was removed before the hand-back.

| Command | Result |
|---|---|
| `S=<round>/t-361ed0cb python3 -I <round>/audit.py pins -v` over `git archive 361ed0cb` | exit 0, `pins 506 in 56 modules` |
| `S=<round>/t-e953d0a9 python3 -I <round>/audit.py pins -v` over `git archive e953d0a9` | exit 0, `pins 109 in 43 modules` |
| `python3 -I <round>/show_kept.py <round>/pins-e953d0a9.txt <clone>`, the comment lines above each listed `assert` | 108 of 109 rows have a comment; the one without is `tests/text/test_a_gate_that_fails_says_so.py:25` |
| `python3 -I <round>/removed.py <round>/pins-361ed0cb.txt <round>/pins-e953d0a9.txt <round>/t-361ed0cb/tree 8` | 399 base rows unmatched at HEAD; 50 printed with their whole `assert` and case |
| `python3 -I <round>/uncommented.py <clone> 361ed0cb`, the uncommented literal asserts in each test function the diff touched | 46 asserts, ruled under *Confirmations* |
| `bin/seal rules --check` in `<clone>` | exit 0, `seal rules: all 283 check lines in 55 rule files hold.` |
| `git grep -n <module> -- . ':!seal/threads'` for each of the three deleted modules | exit 1 for each |
| `git diff 361ed0cb..HEAD -- agents skills docs templates CLAUDE.md CONTRIBUTING.md`, the `-`/`+` lines | 19 `check:` line pairs, none under `docs/` |
| `python3 -I <round>/durations.py <clone> 361ed0cb` | 6045 keys, byte-equal to the sorted dump; 171 removed or renamed case names, none named outside `seal/threads`; the keys it flagged are the `test_census` assignments and parametrize ids holding `::`, which the script's parse misreads |
| `grep -n -i -E` for phrases claiming a wording pin, over the modified test modules | four lines; `tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py:13` says "the sentences a session acts on", which matches what that case keeps, and the others are in cases outside the listing |
