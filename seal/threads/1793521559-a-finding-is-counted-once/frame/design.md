# Design: 1793521559-a-finding-is-counted-once

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `docs/release-checklist.md` *2b. Settle what earlier releases left behind*, the paragraph opening "Before `seal settle --apply`, the settling session counts" (read) | The four numbers per released work item routed through the review chain: findings, findings with a `regression:` or `reopens:` line, findings located in records alone, rounds. Today the paragraph defines them as a `grep -h` reading, and it names no command, so the grep pattern is each reader's own. The step ships to no user, and its reader is this repository's owner. |
| `docs/the-review-record.md` *The round record*, the paragraph opening "The record's fields stand in `seal` blocks" (read) | A finding's own block opens with `severity:` and holds one `location:`. A close block opens with `verdict:` and may hold a `location:` "where the fix went to a path the finding does not name". `hooks/lib/fields.py` is the one spelling of that grammar. So since the blocks landed, one finding can carry two `location:` lines. |
| `docs/the-review-record.md` *The round record*, the paragraph opening "A finding's `location:` names where the defect shows" (read) | "Located in records alone" asks where the defect shows. That is the finding block's `location:`. The close block's `location:` names where the fix went, so the count does not read it. |
| `skills/core/SKILL.md` *The first value: efficient development through the workflow*, the paragraph opening "Judgment is spent where meaning is the question" (read) | A script "reads what a command wrote or what a real parser returns" and does not re-encode the grammar. A grep that tells a finding block's `location:` from a close block's would re-encode the block grammar. The count therefore reads `skills/code-review/scripts/chain_check.py#round_read`, which reads the record through `hooks/lib/fields.py`. |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | The count becomes a script. The design weighs what the script costs against what it catches, and `## Removes` names what goes in return: the grep recipe and the paragraph's `check: none` line. The two homes the brief named are weighed in `frame/plan.md` *Alternatives considered*. |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | `docs/` is the policy root, and a pull request does not edit it. The step's new text is written under `## Rule changes` below, and the settle after the release writes it. |
| `CONTRIBUTING.md` *What a change to a gate must carry*, the bullet "What it removes" (read) | The new script is a mechanism, even though it gates nothing. Its pull request names what it removes, and `## Removes` below holds that list. |
| The grep reading, run over the tree at `e156cf3b` (executed: a probe script under the scratch directory that runs `grep` over each work item's `trail/rounds/round-*.md` joined. The anchored form counts the lines matching `^### [0-9]+\.`, `^(regression\|reopens):` and `^location:`. A `location:` line counts as records alone where no backtick is left once each backticked `seal/threads/` path is deleted from it. The unanchored form drops the `^`) | Per work item, as findings / regression or reopens / records alone / rounds. Anchored: `1793457435` 6/3/0/5, `1793457436` 2/0/1/3, `1793457437` 3/0/1/2, `1793490088` 17/5/17/4, `1793504229` 9/4/3/7, `1793504230` 1/0/0/2, `1793513786` 0/0/0/1, `1793516191` 8/2/8/2. Unanchored, the regression count reads 1 for `1793457437`, 7 for `1793490088`, 5 for `1793504229` and 3 for `1793516191`. Prose that quotes the word `regression:` is what moves those counts. `1793504230` holds 2 `location:` lines and 1 finding. Its second `location:` line is a close block's. |
| The parser reading, run over a `git clone --no-local` of the worktree at `e156cf3b` (executed: `python3 -I <scratch>/test_tmp_count.py <clone>`, a probe that reads every record through `chain_check.round_read` and takes each finding's own block) | The same eight rows as the anchored grep: 6/3/0/5, 2/0/1/3, 3/0/1/2, 17/5/17/4, 9/4/3/7, 1/0/0/2, 0/0/0/1, 8/2/8/2. No record holds a refused line. The double count is therefore latent in this tree: `1793504230`'s close-block `location:` names no path under `seal/threads/`. |
| A constructed record: one finding located at `seal/threads/1-x/frame/design.md:3`, whose close block carries `location:` `seal/threads/1-x/frame/plan.md` (executed: the grep script above, and `chain_check.record_findings` from the clone) | The grep reads records alone as 2 for 1 finding, which is the issue's symptom. The parser reads 1 finding with no error. Its `Finding.paths` is `['seal/threads/1-x/frame/design.md', 'seal/threads/1-x/frame/plan.md']`, both blocks' paths joined. So `Finding.paths` cannot answer "where the defect shows": a close block that names code would turn a records-alone finding into a code finding. |
| `skills/code-review/scripts/chain_check.py#finding_of`, lines 735-780 (read) | `paths` is the finding block's `location:` paths followed by the close block's. `#located_in_records` (line 898) and `#verdict_problems` (line 1091) read that union. The pull-request check needs the union: a fix that went to code must be read by a round. `Finding` is built at line 767 only (executed: `git grep -n 'Finding(' -- '*.py'`). |
| `.github/scripts/release_seal.py#chain_counts`, lines 290-391 (read) | Precedent: a script that ships to no user, runs in this repository's release, and counts round records with `chain_check.record_findings`, `hooks/lib/routing.py#rounds` and `#item_dir`. A record that reader refuses any line of makes that count `not read`, "an incomplete count is a wrong number". The new script takes the same stance. |
| `skills/settle/scripts/settle.py#released`, lines 191-214 (read) | `seal settle` treats a work item as released where its directory is present at `--released-at` (default `origin/main`). Step 2b runs `seal settle` with no arguments. The script takes the same flag and the same default, and calls that function, so its rows are the work items the dry run lists. |
| `hooks/lib/routing.py#parse`, lines 187-280 (read) | The `Review` axis reads `through the review chain` (`routing.CHAIN`) in a parsed declaration. That is the step's "routed through the review chain". |
| Issue #51, the open `flow-baseline` issue (executed: `gh issue list --label flow-baseline --state all`, and `gh issue view 51 --json comments`) | The premise that keeps the step holds. #51 is open, and its comment of 2026-10-31 carries the 0.27.1 settle's four numbers as `\| work item \| findings \| regression or reopens \| records alone \| rounds \|`. The script prints that header. |
| The ticket, #1223 (executed: `gh issue view 1223 --json body,comments`, run by the orchestrator on 2026-11-01 and carried in the spawn prompt; title read by `gh issue view 1223 --json title`) | It has no comments. Done when the step counts a finding once by its finding block's `location:`, says so, and the four numbers remain a reading anyone can repeat with one command written in the step or with `seal settle`. |
| `seal/follow-up.md` (read) | No row there waits on this work. The row on `console.to_utf8()` under `.github/scripts/` says an entry point there that prints a non-ASCII character owes the call. The refusals this script prints are led by `chain_check.DASH`, an em dash, so the script calls it. |
| `.github/scripts/rules.py#RULE_FILES`, lines 68-76 (read) | `seal rules --check` reads `check:` lines in `docs/*.md` and the other rule files, and in no file under `seal/`. The third rule change names `tests/github/test_finding_counts.py`, and that line meets the reader only once the settle writes it into `docs/`. By then the module is in the tree. |
| This design's `## Rule changes`, read by `skills/settle/scripts/rule_changes.py#parse` and `#section_lines` from the clone (executed: a `python3 -I` probe that parses this file and searches each `from` in the section of `docs/release-checklist.md` at `e156cf3b`) | Three `change` operations, no error, no line named as unread. Each `from` is found in the section. |
| The unsettled designs' `## Rule changes` under `seal/threads/` (executed: an `awk` over each `frame/design.md`) | None names `docs/release-checklist.md`. The section as the baseline holds it is the policy in force. |
| The latest Release's `### Process changes` and the fragments under `seal/threads/` (executed: `gh release view --json body`, `grep -l 'Process changes' seal/threads/*/changelog.md`) | v0.27.1's body holds no such heading, and no fragment holds one. |

## Scope

In:

1. `skills/code-review/scripts/chain_check.py#Finding` gains a field, `located`: the paths of the finding block's own `location:`, in the order written. `paths` keeps the union it holds now. No gate reads `located`, and no exit code or message of the check changes. `#finding_of`'s docstring and the comment above `Finding` say which field holds which.
2. A new script, `.github/scripts/finding_counts.py`, ships to no user. It prints the four numbers of step 2b as the table #51's comments carry, one row per work item. The rows are the work items whose directory is present at `--released-at` (`settle.py#released`) and whose `routing.md` parses with `Review` `through the review chain`. It reads each `trail/rounds/round-N.md` through `chain_check.round_read`, by way of `#record_findings`, and counts as *Data & interfaces* states. It writes nothing, posts nothing and fails nothing.
3. `tests/github/test_finding_counts.py` holds the script's cases, scenarios S1 to S6. `tests/skills/test_chain_check.py` gains the `located` case, S7.
4. The step's new text, written under `## Rule changes` below for the settle to apply. The step names the command, says a finding is counted once by its finding block, and its check line names the new test module.

Out:

- `seal settle`'s output. The step is this repository's alone. Printing the four numbers in the dry run would ship a reading to every user that no installed repository reads (`frame/plan.md` *Alternatives considered*).
- What the pull-request check decides. `#located_in_records` and `#verdict_problems` keep reading the union, for the reason the Grounding row on `#finding_of` gives.
- Posting the comment. The step makes it the settling session's act, and a script that posted would write to the tracker from a reading.
- Local mode. This repository's root is shared (`seal/config.md` `Mode` `shared`, read). The script reads `<root>/seal/threads/` and says nothing about a root under the git directory.
- The 0.24.0 and 0.25.0 figures in the step's paragraph. They are what the measure read before the blocks landed, and this work does not re-derive them.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A close block's `location:` does not count a finding twice | Given a released work item routed through the review chain, with one round record holding one finding whose finding block names a path under `seal/threads/` and whose close block names another path under `seal/threads/`, when the script runs, then its row reads 1 finding, 0 with a regression or reopens, 1 in records alone, 1 round | a case in `tests/github/test_finding_counts.py`, seen red with the count rewritten to read `Finding.paths` and each `location:` line, and with the count of records-alone findings replaced by a count of `location:` lines |
| S2 Where the defect shows decides records alone, not where the fix went | Given one finding whose finding block names `seal/threads/<id>/frame/design.md` and whose close block names `hooks/lib/fields.py`, when the script runs, then records alone reads 1. Given one finding whose finding block names `hooks/lib/fields.py` and whose close block names a path under `seal/threads/`, records alone reads 0 | two cases in the same module, seen red with `located` replaced by `paths` (the first reads 0) |
| S3 Prose and fences are not fields | Given a record whose prose quotes `regression: round-1#1` on a line of its own, and whose paste-ready fix fence holds a `### 2. <symptom>` heading and a `location:` line, when the script runs, then findings reads 1 and regression or reopens reads 0 | a case in the same module. The grep script of the Grounding reads that record as 2 findings and 1 regression |
| S4 A record the reader refuses is not counted short | Given a work item one of whose round records holds a `seal` block line `hooks/lib/fields.py` refuses, when the script runs, then its findings, regression and records-alone cells read `not read`, its rounds cell holds the count, a line below the table names the record, the line and the refusal, and the exit code is 0 | a case in the same module |
| S5 The rows are the step's work items | Given three work item directories, one absent at `--released-at`, one whose `routing.md` reads `Review` `straight to the PR`, and one released and routed through the review chain, when the script runs, then the table holds one row, the third. Given a `--released-at` that does not resolve, the script prints why on stderr and exits 2 | cases in the same module |
| S6 The output is the comment's table | Given any tree, the first two lines printed are `\| work item \| findings \| regression or reopens \| records alone \| rounds \|` and `\|---\|---\|---\|---\|---\|`, and the rows follow in work item id order | a case in the same module, and the run below |
| S7 `located` holds the finding block's paths alone | Given the constructed record of the Grounding, when `chain_check.record_findings` reads it, then `located` is `['seal/threads/1-x/frame/design.md']` and `paths` is the two paths it holds now | a case in `tests/skills/test_chain_check.py`, seen red with `located` built from the union |
| S8 This tree reads as the probe read it | Given the worktree at the build's commit, when `python3 .github/scripts/finding_counts.py --released-at 813665f0` runs, then the eight rows read as the parser row of the Grounding, and `1793521559-a-finding-is-counted-once` is no row, because `813665f0` does not hold its directory | the phase runs it and pastes the output into its phase record |
| S9 The policy root is untouched and the rule changes parse | Given the branch at HEAD, `git diff --stat 813665f0...HEAD -- docs/` prints nothing, and the chain check reads this design's `## Rule changes` with no refusal | the sealer, at its guarantee |

## Data & interfaces

`chain_check.Finding` gains `located`, a list of the paths `#location_paths` reads from the finding block's `location:` value. `paths` stays as `located` followed by the close block's paths.

```
python3 .github/scripts/finding_counts.py [--released-at REF] [--root DIR]
```

- `--released-at`: default `origin/main`, as `seal settle` defaults it. `--root`: default the repository this file is in.
- **The counts, per work item, over its `routing.rounds` records**:
  - *findings*: the `Finding`s `chain_check.record_findings` returns.
  - *regression or reopens*: the findings whose `regression` or `reopens` is set.
  - *records alone*: the findings whose `located` is not empty and names only paths for which `chain_check.under(path, "seal/threads")` holds.
  - *rounds*: `len(routing.rounds(item))`.
- **Stdout**: the header, the separator, then one row per work item, `| <id> | <n> | <n> | <n> | <n> |`. A cell that could not be read reads `not read`. A work item whose `trail/rounds/` cannot be listed (`routing.rounds_unreadable`, which holds for a link, a path that is not a directory, and a directory nothing can list) reads `not read` in all four cells, and its line under the table names the directory in words true of all three. A released work item whose `routing.md` is missing or is not a declaration is no row, and its line under the table, `<path>/routing.md: whether it went through the review chain is not read: <why>`, says so; one the tree no longer holds is skipped, as `seal settle` skips it. Under the table, one line per unread record: `<path>:<line>: <why>` for each refusal `record_findings` returned, or `<path>: <why>` where the file could not be opened.
- **Exit codes**: 0, the table was printed, whatever it shows. 2, the ref does not resolve or a reader does not load, with the reason on stderr.
- **Entry**: it calls `hooks/lib/console.py#to_utf8` first, as `.github/scripts/tracker_labels.py:159` does.

## Rule changes

- change
  file: docs/release-checklist.md
  section: 2b. Settle what earlier releases left behind
  from: the findings whose every `location:` path is under `seal/threads/`,
  to: the findings whose finding block names only paths under `seal/threads/` on its `location:` line,
- change
  file: docs/release-checklist.md
  section: 2b. Settle what earlier releases left behind
  from: The four are read from the work item's `trail/rounds/round-*.md` with `grep -h`, which reads a file wherever it lies: the `### <n>.` finding headings; the `regression:` and `reopens:` lines; the `location:` lines left with no backticked path once every path under `seal/threads/` is deleted from them; and the files.
  to: `python3 .github/scripts/finding_counts.py` prints the four as the table the comment carries, one row per such work item. It reads each round record through `skills/code-review/scripts/chain_check.py#record_findings`, the reader the pull-request check holds a record to. So a finding is counted once: by its `### <n>. <symptom>` section that holds a finding block, by that block's `regression:` or `reopens:` line, and by that block's `location:` line alone. A close block's `location:` names where the fix went, not where the defect shows, and the count does not read it. A work item whose record the reader refuses a line of reads `not read` in its finding cells, and the refusal is printed under the table, because a count that skipped a refused finding is a wrong number.
- change
  file: docs/release-checklist.md
  section: 2b. Settle what earlier releases left behind
  from: most installed repositories keep no `flow-baseline` log.
    check: none reader: the owner's settling session at this step
  to: most installed repositories keep no `flow-baseline` log.
    check: tests/github/test_finding_counts.py

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The grep recipe of the four numbers: `grep -h` over `trail/rounds/round-*.md`, reading headings, `regression:` and `reopens:` lines, and `location:` lines with the `seal/threads/` paths deleted | `docs/release-checklist.md` *2b. Settle what earlier releases left behind*, the sentence opening "The four are read from the work item's" | `.github/scripts/finding_counts.py`, through `chain_check.py#record_findings`, at the settle that applies the second rule change. What it caught: the 0.24.0 and 0.25.0 readings the paragraph cites, and the 0.27.1 comment on #51. What it cost: a `location:` line counted once per block, and a pattern each reader spelt for themselves. The Grounding's unanchored grep reads a different regression count for four of eight work items. |
| The paragraph's `check: none reader: the owner's settling session at this step` | the same section, the check line under the paragraph opening "Before `seal settle --apply`, the settling session counts" | `tests/github/test_finding_counts.py`, through the third rule change. The session still posts the comment, but the count is a script's, and a test reads it. |

Framed 2026-11-01 by framer, before the build.
