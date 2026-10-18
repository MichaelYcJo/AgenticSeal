# 1792251842-the-smith-is-written-anew-from-its-job — phase 5

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | the commit that adds this record, `changelog.md` and the closed memo; `plan.md`'s Status names it |
| Ran by | specseal:smith on Opus 5.5 |

## What this phase was asked

The close, unattended and with no paid run. Write `overview.md`'s
divergences with grounds, at least: phase 1 taken twice, phase 2 split into
a and b, the verify section retitled, phase 4 taken twice on the merged
tree with phase 1's baselines kept, the merge's two conflicts, T5's walk
given `on_disk` (09d49365), and `write_case` writing LF (af716289). Close
each `## Not verified` row that is answered and name the answerer of each
that is not. Create `changelog.md` with the paragraph a plugin user reads
and the per-agent table of preload bytes, tokens per tool call, spend and
verdict at 2fc33333 and at af716289, each figure read with
`noninferiority.py#side_numbers` from the committed records. Answer the
`questions.md` rows the work or a measurement answered. Narrow
`seal/follow-up.md`'s line-wrap row to the scribe for #970. Fill `plan.md`
phase 5's Status in a second commit.

## What this phase found

**Every changelog figure equals phase 4's table.** `side_numbers` over the
six committed sides gives the figures below, and each one matches
`phases/phase-4.md` §*What this phase found* to the digit shown. The phase
record was not the source; the records were.

| Changelog figure | smith | warden | framer | Record, and the commit that added it |
|---|---|---|---|---|
| Preload bytes at 2fc33333 | 90,728 | 27,198 | 89,444 | `evals/baseline-<a>.json`, `specseal.preload_bytes`; b4e72dbe, dc8991c2, adbbea77 |
| Preload bytes at af716289 | 26,596 | 27,173 | 86,353 | `evals/<a>-phase-4.json`, `specseal.preload_bytes`; 6f3ee98b |
| Tokens per tool call at 2fc33333 | 43,068.0 (9,561,086 / 222) | 87,197.6 (81,616,964 / 936) | 27,296.7 (3,275,602 / 120) | `evals/baseline-<a>.json`, `tokens / calls`; as above |
| Tokens per tool call at af716289 | 35,993.1 (7,342,587 / 204) | 87,862.4 (82,590,654 / 940) | 29,894.6 (3,258,508 / 109) | `evals/<a>-phase-4.json`, `tokens / calls`; 6f3ee98b |
| Spend USD at 2fc33333 | 6.6210 | 42.2333 | 16.9055 | `evals/baseline-<a>.json`, `spend`, rounded to four places |
| Spend USD at af716289 | 5.3675 | 41.7424 | 16.1196 | `evals/<a>-phase-4.json`, `spend`, rounded to four places |
| Graders passed, 2fc33333 → af716289 | 48 → 48 of 48 | 86 → 91 of 96 | 64 → 64 of 64 | `graders`, summed passed over summed runs |
| Verdict | pass | fail, rule 5 alone | fail, rule 5 alone | `evals/<a>-phase-4.md`, its `Verdict:` line and the one reason under it; 6f3ee98b |

Every side reads `rev` 2fc33333 or af716289, `suite_rev` af9c924b, and
`cut` false, with 8, 18 and 8 runs. The percentages in the changelog are
computed from the same numbers: the smith's preload 26,596 / 90,728 is
-70.7%, the warden's per-call figure +0.8%, the framer's +9.5% with total
tokens 3,258,508 / 3,275,602 at -0.5%.

After round 1 the smith's side was taken again at 28d6a453, and the
changelog's smith row now reads that side; `phases/phase-4.md` traces it.
The table above is the close as this phase wrote it.

**The frame named a template that does not exist.** `plan.md` row 5 and
`spec.md` §*Data & interfaces* say `changelog.md` starts from
`templates/sdd-changelog.md`. No such file is in `templates/`, and
`git grep -n "sdd-changelog" -- . ':!seal/specs'` finds nothing, so no
shipped file sends a reader to it. The fragment follows the shape of the
finished items' fragments and `docs/the-record-layout.md` §*A change writes
fragments, never a shared file*: a `### Changed` list, no line starting
`## `, the item's directory and issue at the end. The row also names
`payload-meter` as a source of the preload figures; the eval records'
`preload_bytes` are what the table reads, and phase 1 found them equal to
the meter's agent shares at 2fc33333.

**The smith opened both skills in all eight runs of the second take too.**
`phases/phase-4.md` counted the first take. Counted here from the kept
traces under `SpecSeal-worktrees/967-phase-4b-raw/smith/traces/`, read and
not written: each of the 8 runs holds a `Read`, `Bash` or `Grep` call whose
input names `skills/implement/SKILL.md`, and each holds one naming
`skills/writing-style/SKILL.md`. The count is of calls naming the path, so
a run that only grepped the file would count; it answers Q6 for the record
take.

**The item passed `questions.md` Q1's $150 stop before phase 4's second
take.** From the phase records' eval `costUsd`: phase 1 104.1452, phase 4's
first take 60.5128, so 164.6580 before the second take started, and
63.2293 for it, 227.8873 in all. Q1's own answer is a stop before the next
agent once the item's spend passes $150. The tree records the orchestrator's
decision to keep the baselines and none to pass the stop, so it stands in
`overview.md` as a divergence and an open `## Not verified` row with the
orchestrator as answerer. Of the 227.8873, 38.3854 (phase 1's first
attempt) and 60.5128 (phase 4's first take) bought no record that stands.

**#973's red Windows leg and this branch's green one are both read off
GitHub.** Run 39094763103 is `tests` on
`chore/969-the-sealer-reads-the-gate-the-orchestrator-ran` at c2ba7035,
`failure`, with `pytest (windows-latest, … --group 1 …)` the one failing
job. Run 39095623463 is `tests` on this branch at af716289, `success`, every
job `success` but `release-report`, which is `skipped`. Which case failed
in the first run is af716289's commit message, not a log read here.

**The merge's two conflicts, read with `git show --remerge-diff 16e8d4c8`.**
`agents/sealer.md` lines 23 to 35: the resolution keeps #969's sentence
and its paragraph about `broad-gate.md`, with this item's verify section
title. `tests/test_the_seal_is_taken_once_by_the_sealer.py` in
`test_the_unmeasured_word_says_so_and_every_reader_is_told_it`: #969's
reader of `skills/code-review/orchestration.md` and this item's smith
phrase, with no sealer reader.

**What the chain check says is owed is the orchestrator's.**
`chain_check.py --worktree` exits 0 and names three things the item does
not yet carry: no `rounds/round-N.md` under a `through the review chain`
declaration, no `broad-gate.md`, no `guarantee.md`. The review rounds, the
broad gate and the sealer are not this phase's acts.

### Commands, each with its exit code

Read directly with `> file; echo $?`, never through a pipe. `$R` is the
checkout, `$I` this work item's directory, `$S` the session scratch
directory's `967-phase-5/`.

| Command | Exit |
|---|---|
| `python3 $S/figures.py`, `side_numbers` over the six sides | 0 |
| `python3 $S/opens.py SpecSeal-worktrees/967-phase-4b-raw/smith` | 0: 8 runs, 8 and 8 |
| `git -C $R show --remerge-diff --format= 16e8d4c8` | 0: two conflicts |
| `gh run view 39095623463 --json conclusion,headSha,headBranch,workflowName,jobs`, then 39094763103 | 0, 0 |
| `bin/rules --check --root $R` | 0: all 483 targets in 60 rule files resolve |
| `bin/unverified-check --baseline origin/release/v0.22.1 $R/$I/overview.md` | 0: 3 open, 3 closed |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.22.1 --root $R --worktree` | 0, with the three owed records above |
| `bin/test` over the 69 modules `git grep -l -E "changelog\|overview.md\|questions.md\|follow-up.md" -- tests` names, plus `test_docs_line_wrap`, `test_one_word_one_meaning` and `test_no_real_identifiers` (70 once deduplicated), `-q` | 0: 4359 passed, 6 skipped |
