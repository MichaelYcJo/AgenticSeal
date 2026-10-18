# 1792251842-the-smith-is-written-anew-from-its-job — review round 1

target: 37d7e68d against origin/release/v0.22.1

## Findings

### 1. The smith has nowhere to put a question only a person can answer, and a test comment says it reaches the filing ladder through a file that holds no link to it

severity: should
location: `agents/smith.md:17-21`, `agents/smith.md:51-55`, `tests/test_the_rules_have_one_owner.py:113-114`
verdict: fixed a72d5b53

Read. `spec.md` §*Data & interfaces* gives the hand-back five parts, the last
two "changed files with absolute paths, what only a person can answer". Step
10 of `agents/smith.md` carries the first four and drops the fifth. At the
same time `## Job` ends "a write not named here is a write you do not make",
and it names neither `questions.md` nor `seal/follow-up.md`. The smith is told
at step 1 to follow `skills/implement/SKILL.md`, whose §1 (lines 216-223)
sends "a decision only a person can make" to `questions.md` and "a finding
you neither fixed nor answered" to `seal/follow-up.md`. So a smith that meets
either has an instruction to write a file its own definition forbids, and no
field in the hand-back to carry it instead. The old definition held both
writes ("What surfaces later is written down rather than raised —
`questions.md`, `seal/follow-up.md` with an answerer"; its `## Report`
carried "open issues with who must answer each"), so this is a rule that
left while a reader still depends on it: the orchestrator, which files what
the smith hands back.

Read. The same removal re-pointed rule 14 of
`tests/test_the_rules_have_one_owner.py` and justified dropping the smith's
link with "a smith reaches it through `implement`, which it opens at its
first step". `skills/implement/SKILL.md` holds no link to
`docs/the-review-record.md` §*The run*'s ladder; its §6 has a destination
table of its own, and its one `§*The run*` citation (line 343) is about the
reframe line. The ladder's own `Enforced by:` reads "the orchestrator
files", and contract §6 withholds posting from every agent, so the smith
cannot file at rungs 2 and 3 anyway. The true replacement is that the smith
hands a leftover back and the orchestrator files it.

Executed. The fix below, applied in this round's clone together with
findings 2 to 5's, kept `bin/rules --check` at exit 0 and 46 modules green
(2266 passed): every module naming `agents/smith`, `smith.md`,
`implement/orchestration` or `verify/SKILL`, plus the contract-shape, line
wrap, one-word, pasted-passage and record-words modules. With every fix of
this round applied, `agents/smith.md` reads 10,276 B, under the 10,527 B
target.

```diff
--- a/agents/smith.md
+++ b/agents/smith.md
@@
     claim labelled `executed`, `read` or `unverified`, the suite labelled
     `unverified` with the orchestrator named as its answerer, each declined
     instruction as one line saying what was asked and which rule refused it
-    (§3), and changed files by absolute path.
+    (§3), what this file does not let you record yourself (a question only
+    a person can answer, a leftover for `seal/follow-up.md`) with who answers
+    each, and changed files by absolute path.
--- a/tests/test_the_rules_have_one_owner.py
+++ b/tests/test_the_rules_have_one_owner.py
@@
     "14 a finding is filed where somebody will act": (
         RECORD,
         "A leftover finding takes the first rung that fits.",
-        # The smith's copy of the ladder left with #967: a smith reaches it
-        # through `implement`, which it opens at its first step.
+        # The smith's copy of the ladder left with #967. Filing is the
+        # orchestrator's act (the ladder's own `Enforced by:` says so), and a
+        # smith hands a leftover back with its answerer (its step 10).
         {
```

answer: a72d5b53 applies the paste-ready text: step 10 hands back a question only a person can answer and a leftover for `seal/follow-up.md` with who answers each, and rule 14's comment says filing is the orchestrator's act and the smith hands a leftover back at step 10; `implement` gains no link, since the rewritten comment no longer claims it holds one.

### 2. The smith's fix-pass rule names an `Enforced by:` case that never opens `agents/smith.md`

severity: should
location: `agents/smith.md:155-164`, `tests/test_a_moved_rule_leaves_its_definition.py`
verdict: fixed a72d5b53

Executed. `tests/test_the_record_is_written_in_words.py::test_a_repair_with_no_commit_closes_deferred_where_it_was_made`
reads `docs/the-review-record.md` §*The round record* and nothing else.
`mutation-check agents/smith.md` deleting the paragraph's bold lead, with that
case as `--tests`, printed `SURVIVED: the cases passed against the mutation`
(exit 1). So the paragraph, which also carries the `location:` append and the
§12 sweep ("Once the fixes are committed, find every other place stating each
rule your range reworded or removed"), can leave the smith in a later trim with
every case green. That is the failure T3 was planted against (#107), and
`spec.md` §*The shape this item gives each file* asks that each rule's
`Enforced by:` hold it. No case read this paragraph at the base either; the
rewrite gave it a target that looks like a hold and is not one.

Executed. The case below, as a `test_tmp_` probe in the round's clone, passed
on the tree and went red under two mutations through `mutation-check`: the
lead deleted, and "find" made "skip" in the sweep sentence (`red`, exit 0,
each). `bin/rules --check` resolved 483 of 483 with the new target.

```diff
--- a/agents/smith.md
+++ b/agents/smith.md
@@
 every other place stating each rule your range reworded or removed, by
 `git grep` and its `Enforced by:` target, and correct each or say in the
 hand-back why it stands (§12).
-Enforced by: tests/test_the_record_is_written_in_words.py::test_a_repair_with_no_commit_closes_deferred_where_it_was_made
+Enforced by: tests/test_a_moved_rule_leaves_its_definition.py::test_the_smiths_fix_pass_writes_two_lines_and_sweeps_what_its_range_reworded
--- a/tests/test_a_moved_rule_leaves_its_definition.py
+++ b/tests/test_a_moved_rule_leaves_its_definition.py
@@ def test_the_smiths_four_rules_stand_with_their_enforcers():
     )
 
 
+def test_the_smiths_fix_pass_writes_two_lines_and_sweeps_what_its_range_reworded():
+    """The smith's half of the fix pass: the two lines it writes, the
+    coordinate it appends, and the sweep for every other place stating a rule
+    its range reworded (contract §12). The record's grammar is
+    `docs/the-review-record.md`'s and is held there; this holds the
+    definition's paragraph, which no other case reads."""
+    paragraph = flat(
+        smith_rule("A fix pass writes two lines of each finding and no phase record.")
+    )
+    assert paragraph, "`agents/smith.md` lost its fix-pass rule"
+    for clause in (
+        "`fixed <commit>`, `rejected` or `deferred <home>`",
+        "`deferred <where it was repaired>`",
+        "append the one it did change after `, `",
+        "find every other place stating each rule your range reworded or removed",
+    ):
+        assert clause in paragraph, f"the fix-pass rule lost {clause!r}"
+
+
 # A batching figure: a number within a few words of "tools per turn", either
```

answer: a72d5b53 plants `test_the_smiths_fix_pass_writes_two_lines_and_sweeps_what_its_range_reworded` as written and points the rule's `Enforced by:` at it; green on the tree, and `red` (exit 0) under `mutation-check` deleting the bold lead and under "find" made "skip" in the sweep sentence, each run after the commit.

### 3. The smith's `## Never` drops the proof block the frame put there, and the changelog promises a behaviour that rests on it

severity: should
location: `agents/smith.md:71`, `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/changelog.md:16-17`
verdict: fixed a72d5b53

Read. `spec.md` §*The shape this item gives each file* lists under
`## Never`: "put an emoji or a proof block in anything it writes". Line 71
reads "Put an emoji in anything you write." and nothing else in the
definition mentions a block. Phase 2's ask was to take the proof block "out
of `agents/smith.md`, the word included", which removed the prohibition with
the word, and `overview.md` carries no divergence row for it. The changelog
then tells a plugin user that "a spawn prompt that asks a smith for one gets
the labels instead". No sentence a smith reads says so, no eval case asks
for a block, and contract §3 is about widening verification, not about the
shape of a hand-back. A prompt that asks for the block is exactly the case
the changelog names, and today nothing in the definition refuses it.

Executed. The line below kept a run of twelve modules green (771 passed),
among them T6's `test_the_record_is_written_in_words.py`,
`test_docs_line_wrap.py`, `test_one_word_one_meaning.py` and the contract-shape
module. It uses neither spelling T6's `PROOF_BLOCK` pattern refuses.

```diff
--- a/agents/smith.md
+++ b/agents/smith.md
@@
 - Restore a mutated file from HEAD.
-- Put an emoji in anything you write.
+- Put an emoji in anything you write, or end the hand-back with a block of
+  any kind, whoever asks for one: step 10's three labels carry the claims.
 - Write in a reference root, or move, edit or copy a file out of one.
```

answer: a72d5b53 writes the line as given, so `## Never` refuses a block at the end of the hand-back whoever asks, which is the definition sentence the changelog's promise needed; `agents/smith.md` reads 10,276 B (`wc -c`), under 10,527.

### 4. `implement`'s orchestrator half still says a smith spawn preloads `implement`

severity: should
location: `skills/implement/orchestration.md:19-21`, `tests/test_chain_hooks_hardening.py:303`
verdict: fixed a72d5b53

Read. `skills/implement/orchestration.md:19` reads "a `smith` spawn preloads
that one and never this". Since e61ac4e1 the smith preloads `agent-contract`
alone and opens `implement` at its first step. `spec.md` §*Scope* leaves this
file to #940 "beyond a pointer the rewrite keeps true", and this sentence is
one the rewrite made false. It is the file an orchestrator reads, so the
orchestrator is told the smith already holds `implement` when it spawns one.
The same fact sits in a comment at `tests/test_chain_hooks_hardening.py:303`
("the `SKILL.md` every smith spawn preloads"). `git grep` over `tests/` finds
no case pinning either phrase. `tests/test_review_axes.py:112` ("no smith
spawn preloads") stays true and needs nothing.

Executed. With both edits the 21 modules naming `implement/orchestration`,
line wrap and pasted passages among them, ran green (943 passed), and
`ruff format --check` passed on the test file.

```diff
--- a/skills/implement/orchestration.md
+++ b/skills/implement/orchestration.md
@@
 the test-first cadence, the SDD file set, the closing memo and the review
-incorporation. An orchestrator reads both; a `smith` spawn preloads that one
-and never this, because asking a person and writing `routing.md` are acts
-`agents/smith.md` leaves to the session that spawned it.
+incorporation. An orchestrator reads both; a `smith` spawn opens that one at
+its first step and never this, because asking a person and writing
+`routing.md` are acts `agents/smith.md` leaves to the session that spawned it.
--- a/tests/test_chain_hooks_hardening.py
+++ b/tests/test_chain_hooks_hardening.py
@@
     # The bootstrap and the parity setup are the orchestrator's half of the
     # skill since #292, so the file that has to point at the template is
-    # `orchestration.md`, not the `SKILL.md` every smith spawn preloads.
+    # `orchestration.md`, not the `SKILL.md` every smith spawn opens.
```

answer: a72d5b53 makes both say a smith spawn opens `implement` at its first step; `git grep` finds no other place saying a smith preloads it (`tests/test_review_axes.py:112` and `tests/test_waiver_decided_at_start.py:50` say no smith spawn preloads `orchestration.md`, which stays true).

### 5. `verify`'s condition 3 still tells every reader that an edit breaks "your seal"

severity: should
location: `skills/verify/SKILL.md:219-220`
verdict: fixed a72d5b53

Read. The rewritten section at `skills/verify/SKILL.md:239-244` says an
agent's hand-back carries its claims under the labels and "neither is a
seal", and the spec's grounding row says that once the proof block leaves,
`seal` keeps one meaning, the sealer's. Twenty lines above it, condition 3
still reads "any edit after the run breaks your seal". That sentence names an
instance and makes its reader the holder, which is the use the item set out
to remove; `implement` sends the smith to `verify` for mutation verdicts, so
the smith reads it. `git grep` misses it because the phrase wraps across
lines 219 and 220. The skill's other uses (line 21's "A claim is sealed",
the `Seal` column at 279, line 336's past-tense account) are the Seal Test
as a concept or history, and are not this finding.

Executed. With the edit, `test_one_word_one_meaning.py` and the modules naming
`verify/SKILL` stayed green in the 2266-case run of finding 1.

```diff
--- a/skills/verify/SKILL.md
+++ b/skills/verify/SKILL.md
@@
 Evidence attaches to a tree state, not to a session. Note the state the
-proof ran against (commit + dirty files); **any edit after the run breaks
-your seal** — re-run, don't re-tell.
+proof ran against (commit + dirty files); **any edit after the run voids
+the claim** — re-run, don't re-tell.
```

answer: a72d5b53 makes condition 3 read "any edit after the run voids the claim"; `git grep -F` for "your seal" and "breaks your" now finds nothing in the tree.

### 6. Phase 4 clears this item of the warden's fail on a list of changed files that leaves out two the warden read

severity: should
location: `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/phases/phase-4.md:27-29`, `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/phases/phase-4.md:66-71`, `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md:32`, `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/changelog.md:37-38`
verdict: fixed 44387d56

Executed. `git diff --stat 7053c184 af716289 -- agents skills templates docs`
lists, besides contract §2 and one line of `agents/warden.md`,
`docs/the-review-record.md` (21 lines) and `skills/code-review/orchestration.md`
(96 lines), both #969's. Read from the kept traces (read only): the warden's
tool calls named `docs/the-review-record.md` in all 18 runs of each take and
`skills/code-review/orchestration.md` in 6 of each. `phases/phase-4.md:68-70`
says "the only files the warden reads that differ between the two takes are
#969's contract §2 and its one warden sentence", and lines 27-29 and
`overview.md:32` describe #969's change to the read set the same way. The
changelog tells a plugin user "The second tree includes #969's change to
contract §2".

The disposition survives the correction: every changed file the warden read
is #969's, and `skills/writing-style/SKILL.md` and
`skills/code-review/SKILL.md` are byte-identical between the takes. The
sealer reads these records against the tree, and the sentence as written is
false of it.

```diff
--- a/seal/specs/1792251842-the-smith-is-written-anew-from-its-job/phases/phase-4.md
+++ b/seal/specs/1792251842-the-smith-is-written-anew-from-its-job/phases/phase-4.md
@@
-merged into `release/v0.22.1` (4a6e24f6) and changed contract §2, which all
-three agents preload, and one sentence of `agents/warden.md`. Under the
+merged into `release/v0.22.1` (4a6e24f6) and changed contract §2, which all
+three agents preload, one sentence of `agents/warden.md`, and
+`docs/the-review-record.md` and `skills/code-review/orchestration.md`, which
+the warden reads. Under the
@@
 files: the same `writing-style` text read at 7053c184 gave 81,965.0 tokens
-per call, 6.0% below the baseline, and the only files the warden reads that
-differ between the two takes are #969's contract §2 and its one warden
-sentence. Two takes of one text 6.8 points apart is the run-to-run spread
+per call, 6.0% below the baseline, and every file the warden reads that
+differs between the two takes is #969's: contract §2, one sentence of
+`agents/warden.md`, `docs/the-review-record.md` (named in all 18 runs of
+each take) and `skills/code-review/orchestration.md` (named in 6). Two
+takes 6.8 points apart is the run-to-run spread
--- a/seal/specs/1792251842-the-smith-is-written-anew-from-its-job/changelog.md
+++ b/seal/specs/1792251842-the-smith-is-written-anew-from-its-job/changelog.md
@@
-  eighteen for the warden, none cut short. The second tree includes #969's
-  change to contract §2, merged in at `16e8d4c8`, as well as this item's.
+  eighteen for the warden, none cut short. The second tree includes #969's
+  changes, merged in at `16e8d4c8`, as well as this item's: contract §2,
+  which all three agents preload, and for the warden
+  `docs/the-review-record.md` and `skills/code-review/orchestration.md` too.
```

In `overview.md:32`, the Grounds cell's "changing contract §2, which all three
agents preload, and one sentence of `agents/warden.md`" takes the same two
additions as `phase-4.md:27-29` above.

answer: 44387d56 names every file #969 changed that the warden reads, recounted over both takes' kept traces by the path a tool call names: `docs/the-review-record.md` and `skills/code-review/scripts/chain_check.py` at the evaluated tree's path in 17 or 18 of each take's 18 runs, and `agents/sealer.md` in 2 and 1, beside contract §2 and the warden's sentence; round 1's "`skills/code-review/orchestration.md` in 6" reproduces as a substring count, but every one of those calls names the reviewed fixture's copy (`home/cwd`, or a `git diff` of the fixture's own commits), so the records say that instead of counting it as a read; the judgement that the fail is not this item's stands, since every such file is #969's.

### 7. Phase 4 clears this item of the framer's fail because the framer never opened `writing-style`, which it preloads

severity: should
location: `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/phases/phase-4.md:76-79`, `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md:51-53`
verdict: fixed 44387d56

Read. `agents/framer.md` at af716289 lists `agent-contract`, `implement` and
`writing-style` under `skills:`, and `evals/framer-phase-4.json`'s
`specseal.preload` carries the sha256 of both skill files (executed: read
with `json.load`). So both files this item rewrote reached every one of the
eight framer runs at startup, whether or not a run then opened one.
`phases/phase-4.md:76-78` reads "It opened `writing-style` in none of its
eight runs, so this item's restructuring of that file is not the cause", and
`overview.md:53` repeats the premise. That inference is the one ground
offered against this item's own files, and plan row 4 sends a fail caused by
`implement` or `writing-style` to a fix and a second run rather than to
#968. The remaining ground, the same rise at #957's phase 3 when both skills
were byte-identical to 2fc33333 (`spec.md` §*The tree as it stands*), may
carry the call; whether it does is the orchestrator's, and is a row of
`## Not judged`.

```diff
--- a/seal/specs/1792251842-the-smith-is-written-anew-from-its-job/phases/phase-4.md
+++ b/seal/specs/1792251842-the-smith-is-written-anew-from-its-job/phases/phase-4.md
@@
-made 11 fewer tool calls, so tokens per call rose 9.5%. It opened
-`writing-style` in none of its eight runs, so this item's restructuring of
-that file is not the cause; the per-call rise repeats #957's framer reading
-(+18.9%), which `agents/framer.md` owns and #968 rewrites.
+made 11 fewer tool calls, so tokens per call rose 9.5%. It preloads
+`implement` and `writing-style`, both rewritten here, so every run read them
+at startup and no count of opens clears them. What points away from them is
+that the per-call rise repeats #957's framer reading (+18.9%), taken when
+both files were byte-identical to 2fc33333; `agents/framer.md` owns that
+rise and #968 rewrites it.
--- a/seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md
+++ b/seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md
@@
 The framer's `fail` on rule 5 (+9.5% tokens per tool call, every grader
 passing) goes to #968, which rewrites `agents/framer.md` (decision 5); the
-framer opened `writing-style` in none of its eight runs. The warden's
+framer preloads both skills this item rewrote, and its per-call rise repeats
+#957's reading, taken before either changed. The warden's
```

answer: 44387d56 rewrites the framer's ground in `phases/phase-4.md` and `overview.md` to the orchestrator's text: it preloads `implement` and `writing-style`, so all eight runs read both; total tokens fell 0.5% and tool calls fell 11, so the per-call rise is fewer calls on a smaller read; no sentence of this item's files is identified as the cause; the fail is recorded as it reads and carried to #968, which measures the framer on a tree carrying this item.

### 8. The memo's spend divergence says its row below is open, and that row is closed

severity: should
location: `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md:36`
verdict: fixed 44387d56

Read. 37d7e68d closed the `## Not verified` row at `overview.md:47` with the
owner's answer ("decide and go with your recommendation"), and left the
divergence row at line 36 ending "the tree records ... no decision to pass
the stop; it is open below with its answerer". Both now stand in one memo
and say opposite things, and the commit that changed the fact left the
sentence standing on the old one (`CLAUDE.md` §*The rule a mechanism is kept
against*: a change "in the same commit removes what stood on the old
fact"). `unverified-check` counts rows and cannot see it.

```markdown
| Q1's spend stop passed (phase 4's second take) | `questions.md` Q1: this item stops before the next agent once its summed spend passes $150 | phase 1 spent 104.1452 and phase 4's first take 60.5128, so the item stood at 164.6580 before the second take, which spent 63.2293 more; the item's total is 227.8873 | the owner, asked on 2026-10-18 whether to spend about $60 past the night's $200, answered "decide and go with your recommendation", and the orchestrator took the second take; the `## Not verified` row below is closed with that answer |
```

answer: 44387d56 replaces the row's Grounds cell with round 1's text, so it says the owner's answer closed the stop and points at the closed `## Not verified` row.

## Confirmations

confirms: none
The proof block is gone from every file an agent reads. Executed:
`git grep -n -i -E "proof block|seal block|implement applied|verify sealed"`
outside `seal/specs/`, `changelog/` and `CHANGELOG.md` names `CLAUDE.md:69`
(the owner's, open in `overview.md`) and six lines in three test modules that
quote history or define T6's pattern. A Python sweep with T6's own `EMOJI`
and `PROOF_BLOCK` patterns over `skills/**/*.md`, `docs/*.md`, the READMEs,
`CONTRIBUTING.md`, `CLAUDE.md` and `templates/` found `legacy-parity`'s four
(#970's) and four lines in `docs/` (#941's), nothing in an agent's corpus.
No hook or script reads an `applied` line or a `cost:` row.

confirms: none
Every heading of `implement` cited outside the records exists. Executed: the
`git grep` of `skills/implement/SKILL.md` §N and §*title* citations finds §1
and §3 by number in `CONTRIBUTING.md`, `agents/framer.md`, four `docs/` files,
both hooks, `orchestration.md` and `templates/sdd-routing.md`, the two titles
in `CLAUDE.md:33` and `:78`, and the contract's §11 by title; each resolves
against the `##` and `###` lines at 33-467. Read: the meanings sampled at
`CONTRIBUTING.md:259`, `agents/framer.md:63` and `:236`,
`hooks/commit-review-gate.py:802` and `hooks/mode-gate.py:38` (the price of a
question, the waiver offered where no work item owns the commit) still stand
in `implement` §1 at lines 167-228.

confirms: none
The smith names no runner of the broad gate. Read: `agents/smith.md:140-147`
says "contract §2 holds who does" and names no party; "the orchestrator" in
step 10 is the suite's answerer. T4 is green in the 1645-case run below.

confirms: none
The merge keeps #969's facts. Executed: `git show --remerge-diff 16e8d4c8`
shows `agents/sealer.md` taking #969's "work;" sentence and its
`broad-gate.md` paragraph with this item's section title, and the stamp
test keeping #969's `skills/code-review/orchestration.md` reader with this
item's smith phrase. Read: of the eleven files both #969 and this branch
changed, the branch's hunks over 4a6e24f6 restore no line #969 removed;
`skills/agent-contract/` is untouched, and `skills/code-review/` differs only
in one `Enforced by:` line re-pointed to T6.

confirms: none
Every figure the records quote from the six eval sides recounts. Executed:
`noninferiority.py#side_numbers` over the committed sides gives the
preload bytes, tokens over calls, spend, graders, truths and report rows of
`phases/phase-4.md`'s table and `changelog.md`'s table to the digit, with
`rev`, `suite_rev` and `cut` as stated and 8, 18 and 8 runs. `run --from-raw`
from `SpecSeal-worktrees/967-phase-4b-raw/` (read only) re-derived
`smith-phase-4.json` and `warden-phase-4.json` byte for byte (`cmp` exit 0
each), and `compare --phase 4` over the re-derived warden side re-rendered
`warden-phase-4.md` byte for byte. `check` exits 0 for the smith and 1 for
the warden and the framer with the single problem "its numbers give `fail`",
so no record states a verdict its numbers do not give. The first take's
81,965.0 tokens per call is `warden-phase-4.md` at a3bf3832.

confirms: none
The smith opened both skills in every run of the record take (S3, Q6).
Executed over the kept traces, read only: all 8 runs called `Read` on
`skills/implement/SKILL.md` within their first seven calls, and all 8 read
`## English prose rules` before their first write to a phase record, four
by `Read` and four by an `awk` range over the section.

confirms: none
The narrow modules the diff touches are green on the target. Executed in the
clone at 37d7e68d: `bin/rules --check` exit 0, 483 targets; `bin/test` over
the 26 test modules the diff changes and seven more that read the rewritten
files, 33 in all, exit 0, 1645 passed, 2 skipped.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the framer's rule-5 fail has its cause in `agents/framer.md`, as carrying it to #968 assumes, once finding 7's premise is gone: plan row 4 sends a cause in `implement` or `writing-style`, both in the framer's preload, to a fix and a second run | `seal/specs/1792251842-the-smith-is-written-anew-from-its-job/phases/phase-4.md:74-79` | the orchestrator |
| Whether a smith that reads `## English prose rules` alone goes on to `## 구성 규칙`, which the new orientation line names; four of eight record-take runs read only an `awk` range from that heading to the end of the file, and no grader in the suite at af9c924b reads it | `skills/writing-style/SKILL.md:280-285` | the orchestrator, at the milestone's close against af9c924b |
| The full suite, the repository-wide lint and the typecheck on this branch | the branch at 37d7e68d | the orchestrator's broad gate |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the checkout, checked out at 37d7e68d, into the round's scratch directory | exit 0; the clone has no `origin/release/v0.22.1`, so every diff in it was read against 4a6e24f6 |
| `bin/rules --check --root <clone>` | exit 0: all 483 `Enforced by:` targets in 60 rule files resolve |
| `bin/test` over the 26 test modules the diff changes plus `test_a_rewritten_definition_proved_non_inferior`, `test_no_passage_is_pasted_into_a_second_file`, `test_the_payload_meter_says_what_it_measured`, `test_a_section_marked_for_one_role_reaches_only_that_role`, `test_the_rules_claude_md_names_have_one_home`, `test_no_real_identifiers` and `test_evals_layout`, `-q` | exit 0: 1645 passed, 2 skipped |
| `mutation-check agents/smith.md --replace "**A fix pass writes two lines of each finding and no phase record.** It" "It" --tests "bin/test tests/test_the_record_is_written_in_words.py -p no:xdist -q -k test_a_repair_with_no_commit_closes_deferred_where_it_was_made"` | exit 1: `SURVIVED` (finding 2) |
| finding 2's case as a `test_tmp_` probe: run on the tree, then `mutation-check` deleting the lead and making "find" "skip" | 1 passed; then `red` (exit 0) under each mutation; the probe file deleted |
| findings 1 to 5's fixes applied together in the clone; `bin/rules --check`; `bin/test` over 46 modules (every one naming `agents/smith`, `smith.md`, `implement/orchestration` or `verify/SKILL`, plus the contract-shape, line wrap, one-word, pasted-passage and record-words modules); `ruff check` and `ruff format --check` on the three changed test files | exit 0, 483 resolve; exit 0, 2266 passed, 2 skipped; exit 0; exit 0 |
| finding 3's line alone; `bin/test` over twelve modules reading the smith, T6, line wrap and one-word among them | exit 0: 771 passed, 2 skipped |
| finding 4's two edits; `bin/test` over the 21 modules naming `implement/orchestration` | exit 0: 943 passed |
| a script calling `noninferiority.side_numbers` over the six committed sides | exit 0: every figure as tabled |
| `noninferiority.py check` on the three `-phase-4.md` records | exit 0 (smith); exit 1 (warden, framer), each with "its numbers give `fail`" alone |
| `noninferiority.py run --agent <a> --from-raw SpecSeal-worktrees/967-phase-4b-raw/<a> --out <scratch>` for smith and warden, then `cmp` against the committed side | exit 0 and `cmp` exit 0, each |
| `noninferiority.py compare --agent warden --phase 4` over the baseline and the re-derived side, then `cmp` against `warden-phase-4.md` | exit 0, `Verdict: fail`; `cmp` exit 0 |
| a trace reader over `SpecSeal-worktrees/967-phase-4b-raw/smith/traces/` counting `Read` and other calls naming the two skills, against the first phase-record write | exit 0: `implement` read by `Read` in 8 of 8; the `writing-style` section read in 8 of 8 before the record |
| the same reader over the warden's traces of both takes, for the files #969 changed | exit 0: `docs/the-review-record.md` named in 18 of 18 each take, `skills/code-review/orchestration.md` in 6 of 18 each |
| `git diff --stat 7053c184 af716289 -- agents skills templates docs CLAUDE.md hooks bin` | exit 0: 25 files, `skills/writing-style/SKILL.md` and `skills/code-review/SKILL.md` not among them |
