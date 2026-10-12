# 1791382684-every-reader-and-record-is-inventoried — round 1 report

| Field | Value |
|---|---|
| Round | 1 |
| Target SHA | 8938af5baa786798b60c8bc05db59856433b9926 |
| Base | `origin/release/v0.21.0` at dae101ab; the build under review is `7608d82c..8938af5b` |
| Reviewer | warden on Opus 5.5 |
| Where | a `git clone --no-local` at the target SHA, under the session scratchpad's `1791382684-every-reader-and-record-is-inventoried/round-1/clone`; removed before hand-over |

## How the findings relate

The build does what its frame says, and the frame's mapping is where most of
what is wrong comes from.

1. **What held, executed.** The 44 changed `.py` files have the same syntax
   tree at both ends once docstrings are taken out, so no reader's behaviour
   changed. The census lost exactly 189 lines and gained none (1,584 to 1,395).
   The registry and rider modules pass, 126 cases.
2. **What the round was asked, read.** I read all 189 `Reads:` lines beside
   the code of their unit. The transcription is faithful: each spot-checked
   line carries its row's words. But 40 of the 189 units (21%) carry a line or a
   paragraph under it that is wrong about that unit, and 32 of those (17%) are
   wrong on the `Reads:` line itself.
3. **Why.** 97 of the 180 lines I could match to their row came from a row
   naming several units, and 65 of those units were not the row's lead. The
   plan's rule gives every named unit the row's line, so a helper inherits a
   description of the reader it helps (🟡 1). The class word and the direction
   word survive this better than the prose does: 5 class words and 3
   direction words are contradicted by the unit's code or by the registry's
   own rule (🟡 2, and `short_commit`'s direction inside 🟡 1).
4. **Two smaller classes.** Three new paragraphs cite line numbers that were
   wrong at the commit that wrote them (🟡 3). Four lines carry the
   inventory's own shorthand (`same`, `wc`, `outside this part`), which reads
   only inside the inventory's table, and those sit inside 🟡 1.
5. **What is not a defect.** One shape is declared two ways (⬜ 4). Three
   paperwork corrections, one of which is what keeps phase 4 from repeating
   🟡 1 (⬜ 5, ⬜ 6, ⬜ 7).

The sample's figures, so the round's question has a number: of 189 lines,
27 misstate on the `Reads:` line what the unit reads, 5 more misstate the
class word, 8 carry a wrong paragraph under a line that
is right, and 3 of those 8 are the line numbers of 🟡 3. Wrong class word: 5
(2.6%). Wrong direction word: 3 (1.6%). All of it from reading.

## Findings from reading

### 🟡 1 · A helper unit's line describes the reader it helps, not itself

`hooks/commitgate.py:144` is the plainest case. `_process` runs
`ps -o ppid=,comm=` on one pid and nothing else. Its line says it reads
"sequencer files under `rev-parse --absolute-git-dir`". That is what the
inventory's part 1 row 62 says of `SEQUENCER` + `_process` +
`_sequencer_commit` together, and the build gave the whole row's prose to
each unit it named.

The same shape, read in the code of each unit:

- `skills/verify/scripts/broad_gate.py:700` — `short_commit` runs
  `rev-parse --short <rev>^{commit}`. Its line names `@{upstream}`,
  `refs/remotes/origin/<b>` and `check-ref-format`, which are
  `resolve_base`'s (part 5 row 8).
- `skills/code-review/scripts/chain_check.py:1705` — `carried_by_a_pull_head`
  runs `for-each-ref --contains`. Its line says `merge-base --is-ancestor`,
  which is `is_ancestor`'s, and `is_ancestor` (`:1634`) carries
  `for-each-ref` in its paragraph.
- `skills/evidence-check/scripts/evidence_check.py:3438` — `calendar_date`
  validates one string with `fromisoformat`. Its line names the `Checked` or
  `Date` header and cell 4, which is `reading_date`'s.
- `skills/verify/scripts/unverified_check.py:235` and `:882` — `visible`
  strips invisible characters and `sections` finds a heading; both lines say
  "exact header, 2-cell rows, ✅ prefix", which is `parse_section`'s.
- `hooks/cmdline.py:2559` and `:2579` — `_dedup` and `_directories`
  deduplicate a list of states. Their paragraph says "more than 64 states
  collapse into one `Unresolved`", which is `STATE_CAP` in another unit.
  `_expands` (`:2183`) likewise says "more than 32 headers gives True", which
  is `HEADERS_READ`'s.
- `hooks/sealer-stamp.py:97` — `load_stamp` imports `seal_stamp.py`; its line
  says it reads the values JSON, which `seal_stamp` reads later.
- `hooks/worktree_consent.py:284` — `_clone_of` asks git for a common dir;
  its line says "transcript lines filtered by substring first".
- `skills/implement/scripts/seal.py:670` and `:1809` — `no_root` calls none
  of the three `optin` functions its line names, and `plugin_workflow` runs
  no `git add`.
- `tests/conftest.py:105` and `:113` — `_indent` counts leading spaces and
  `_unquote` strips quotes; both lines say "every `steps:` list in a
  workflow", which is `workflow_steps`'s. `skills/verify/scripts/broad_gate.py:2410`
  (`unquote`) has the same shape.

The paste-ready block lists all 32 units. It also takes out the inventory's
shorthand, found by a search of every added line:
`hooks/answer-clear.py:15` and `hooks/evidence-advisor.py:88` open with
"same", which points at the previous row of a table the reader cannot see;
`hooks/commitgate.py:95` writes `wc`, part 1's abbreviation for
`worktree_consent.py`; and `hooks/worktree_consent.py:146` writes "outside
this part".

**Why it matters.** `docs/the-reader-registry.md` §*What neither check can
read* names a false declaration as limit 1, the thing only the reviewer reads.
These lines are what a reviewer reads, and a reviewer who trusts
`_process`'s line looks for a sequencer read that is not there. The registry
test cannot see any of it, and the ledger's B1 row says as much.

**What the fix keeps and costs.**

- **Kept** — every class and direction word in this block, except
  `short_commit`'s direction. That unit gives None and `resolve_base` tries
  the next step, so `passed` is what it does. No unit here is cited by a
  ledger row or carries a rider stamp, so no `Re-read ·` row is owed.
- **Diverges** — `spec.md` acceptance row 4 says the prose is the row's
  `What it reads`. The registry document is the ratified rule and says the
  prose is what the unit reads, so the fix follows it. `overview.md` gets a
  divergence row for these 32 units.
- **Not touched** — the 65 non-lead units I did not list. I read each one,
  and its line is true of it, either directly or by the registry's rule that
  a unit parsing text its caller handed it takes the caller's class.

### 🟡 2 · Five class words and two direction words the code contradicts

- `skills/evidence-check/scripts/correction_check.py:746` — `parse_range`
  declares `owned … refused`. Its body is the same code as
  `skills/code-review/scripts/survivor_check.py:458`, which declares
  `observed … mixed`, only the error message differs. Both resolve the ends
  through git, and both keep the left end silently when `merge-base` fails
  on `...`. That is the `mixed` part 3 row 2 records. One body, two
  declarations, and `grep "Reads: observed"` finds only one of them.
- `skills/verify/scripts/unverified_check.py:1401` — `tree_at` declares
  `owned — tree at base, no spec.md, no open rows; unknown mixed`. That is
  `retired_by_rule`'s row (part 5 row 82). `tree_at` lists paths by
  `os.walk` or by `git ls-tree` without `-z`, which is observed. A failed
  `ls-tree` gives `[]`, the same answer as an empty directory, which is
  passed.
- `hooks/hooksession.py:150` — `lease_dirs` declares `owned — every
  specseal-leases/* JSON …; record["pid"] == pid`. It lists directories and
  opens no JSON; `from_lease` does that. Observed.
- `skills/verify/scripts/deferral_check.py:156` — `other_ci_files` declares
  `guess — … + runner words`. It runs `isfile` on six paths and lists
  `.buildkite/`. It reads no file text, and the runner words are
  `inspect`'s. Existence tests are what the registry calls observed, so this
  line puts a unit that guesses nothing on the `Reads: guess` list.
- `skills/verify/scripts/payload_meter.py:375` — `agents_in` declares
  `owned`, but each agent's `name` comes through `frontmatter`, which
  declares `guess` (part 5 row 108). The registry says a unit reading
  several inputs declares the weakest.

**Why it matters.** The class word is the part the registry exists to make
greppable. A wrong one either hides a guess or lists a non-guess, and the
second unit of an identical pair declaring differently is the "one judgment
in several places, disagreeing" this item's own spec names as a finding of
the inventory.

### 🟡 3 · Three new paragraphs cite line numbers that were wrong at the commit that wrote them

- `hooks/cmdline.py:339` (`drop_heredoc_bodies`) and `hooks/cmdline.py:387`
  (`heredoc_bodies`) say the fail-open case is "documented at 443-446". At
  5623d728 and at 7608d82c that comment was at line 443. This build's own
  insertions above it moved it to 457, so the reference was wrong in the
  commit that added it.
- `skills/evidence-check/scripts/pact_check.py:301` (`origin`) says "refused
  at L518". The refusal was at 518 at 5623d728, at 520 at the build's base,
  and is at 541 now.

I enumerated this class by searching every added line of the build for a
line-number shape (`L` and digits, `at` and digits, a numeric range, a colon
and digits). These three were the only hits, and all three are wrong. A line
number in a docstring moves whenever any unit above it changes, so the fix
names the place instead of counting to it.

### ⬜ 4 · One shape, two class words: a marker file this plugin writes, asked whether it exists

`hooks/commit-review-gate.py:686` (`already_asked`) and
`hooks/worktree_consent.py:144` (`granted`) declare `owned`.
`hooks/review-skill-gate.py:118` (`already_asked`) and
`hooks/hook-install.py:75` (`say_once`) declare `observed`. All four ask
whether a file under the git directory exists, a file this plugin wrote. The
registry's table does not settle which class that is. A `grep` for either
class finds half of the shape until somebody does. No defect ships either
way; the registry's owner answers it.

### ⬜ 5 · Correction: `questions.md` Q4 is still open though phase 2 applied its answer

`seal/specs/1791382684-every-reader-and-record-is-inventoried/questions.md`
Q4's `Status` cell reads ⬜. `phases/phase-2.md` applied the trim it asks
about (32 units with `What it reads, continued:`) and the backslash cells,
and `overview.md` cites Q4 for the five backslash lines. Tick it with phase
2's answer.

### ⬜ 6 · Correction: the plan's mapping rule will repeat 🟡 1 on `hooks/worktree-guard.py`

`plan.md` §*Technical context*, the `Unit → units` bullet, gives the row's
line to every backticked name in the `Unit` cell. Phase 4 reruns that rule
on `hooks/worktree-guard.py`, and `overview.md` §*Not done* says the same
rules rerun for the 529 cited units later. Amend the bullet before phase 4:
a unit that is not the row's lead takes the row's class and direction, and
its prose is read from its own code, or it stays on the census.

### ⬜ 7 · Correction: the plan's approval line does not read as one, and the chain check says so on every run

`plan.md:7` reads "Approved 2026-10-12 by the repository owner, with
`questions.md` Q1 answered (c); `smith` is not yet spawned." The chain
check's pattern, `APPROVED_RE` in `skills/code-review/scripts/chain_check.py`,
wants the line to end with the words *when smith was spawned*, so it reports
the line as absent. Executed: running the record generator on
this report in the scratch clone printed that notice for this work item. It
is a notice and fails nothing. The line should end in the form the check
reads, now that the smith has run, with the Q1 answer moved to a sentence of
its own.

## What the code confirmed

- No behaviour change: executed, by comparing each changed file's syntax
  tree with every docstring removed. All 44 match.
- The census: executed. 189 lines removed, none added, 1,395 left, and the
  registry test refuses a census line for a declared unit.
- The three re-stamped riders (`hooks/optin.py#repo_root`,
  `hooks/review-skill-gate.py#already_asked`,
  `skills/code-review/scripts/round_record.py#units_named_earlier`): read.
  Each rider's text still describes its unit's code.
- `hooks/cmdline_base.py` and `hooks/worktree-guard.py` are untouched:
  executed, by `git diff --name-only`.
- Not checked by me: the smith's 45-module and 38-module runs and their
  counts, which stand as the smith's executed claims. The full suite, lint
  and typecheck are the sealer's, not yet run.

## Regression tests to plant

None. What 🟡 1 and 🟡 2 found is a false declaration, which the registry
names as the reviewer's to read (limit 1); no test reads prose against code.
A case that two identical bodies declare one line would catch the
`parse_range` pair and nothing else in the class, so I do not propose one.

## Facts for the evidence ledger

None. The build adds no claim a test can hold beyond B1 and B2, and both
read as written.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | 32 `Reads:` lines or their paragraphs describe a sibling unit's input, mostly a helper given its row's lead description; four carry the inventory's own shorthand | `hooks/commitgate.py:144` | open | read all 189 units against their code; 97 of 180 matched lines came from multi-unit rows, 65 as a non-lead unit (probe) |
| 🟡 2 | five class words and two direction words the unit's code contradicts, one an identical body declared two ways | `skills/evidence-check/scripts/correction_check.py:746` | open | `survivor_check.py:458` is the same body declared `observed … mixed`; `tree_at`, `lease_dirs`, `other_ci_files`, `agents_in` read in code |
| 🟡 3 | three new paragraphs cite line numbers that were wrong at the commit that wrote them | `hooks/cmdline.py:339` | open | the cited comment is at 457 (was 443), the cited refusal at 541 (was 518); found by a search of every added line, three hits |
| ⬜ 4 | one shape (does a marker this plugin wrote exist) is declared `owned` twice and `observed` twice | `hooks/commit-review-gate.py:686` | open | the registry's class table does not settle it; the registry's owner answers |
| ⬜ 5 | Q4 still ⬜ though phase 2 applied its answer | `seal/specs/1791382684-every-reader-and-record-is-inventoried/questions.md` | open | correction to the run's paperwork |
| ⬜ 6 | the plan's mapping rule gives a helper its lead's line, and phase 4 reruns it | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md` | open | correction to the run's paperwork; it is what keeps 🟡 1 from recurring on the guard |
| ⬜ 7 | the plan's approval line misses the form the chain check reads, so it reports the line absent | `seal/specs/1791382684-every-reader-and-record-is-inventoried/plan.md` | open | correction to the run's paperwork; the notice printed when the generator ran in the scratch clone |
| 🟢 | the build changes no reader's behaviour | the 44 changed `.py` files | confirmed | syntax trees equal at both ends with docstrings removed (probe) |
| 🟢 | the census lost exactly the written units' 189 lines | `tests/undeclared_readers.txt` | confirmed | numstat 0 added, 189 removed; registry test green |

## Executed probes

| What was run | Result |
|---|---|
| clone at 8938af5b; list every unit whose docstring gained a `Reads:` line between 7608d82c and HEAD, with its source | 189 units, 4,268 lines of source, all read |
| match each line to its inventory row by unit name and prose | 180 matched: 83 from single-unit rows, 97 from multi-unit rows (32 as the lead, 65 not); 9 unmatched |
| each changed `.py` file's syntax tree with docstrings removed, 7608d82c against HEAD | 44 files, 0 differ |
| `wc -l` and `git diff --numstat` on `tests/undeclared_readers.txt` | 1,395 lines; 0 added, 189 removed |
| `bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py tests/test_a_rider_reaches_its_file.py` | 126 passed |
| search of every added `.py` line for a line-number shape | 3 hits, all wrong (🟡 3) |
| search of every added `.py` line for the inventory's shorthand | `same` ×2, `wc`, `outside this part` (🟡 1) |
| `round_record.py new` on this report, in the scratch clone only, to see that the tables parse | wrote the clone's `round-1.md` with seven verdict rows and both lines; exit 1 from the chain check over the clone, whose other work items' targets it cannot reach, and the ⬜ 7 notice |
| the broad gate: full suite, lint, typecheck | not yet — the sealer's, after the rounds settle |

## Paste-ready fixes

### 🟡 1

Replace each named line, or paragraph, with the text given. Line numbers are
at 8938af5b. Indentation is the docstring's own four spaces, except a
one-line docstring, which keeps its quotes.

```
hooks/answer-clear.py:15  (one-line docstring)
    """Reads: observed — payload `tool_name`, `tool_input.command`, `tool_use_id`, `session_id`; unknown passed"""

hooks/cmdline.py:2183  _expands, the paragraph
    Refused: a first word holding an `EXPANDS` character counts as expanding, so the commit gate stops.

hooks/cmdline.py:2559  _dedup, the line and the two-line paragraph under it
    Reads: guess — the (directory, previous) states the walk built from the segments; unknown refused

    Refused: an `Unresolved` state is kept apart from a readable one that spells the same path.

hooks/cmdline.py:2579  _directories, the line and the two-line paragraph under it
    Reads: guess — the (directory, previous) states the walk built from the segments; unknown refused

    Refused: an `Unresolved` directory is kept apart from a readable one that spells the same path.

hooks/cmdline.py:2653  _step
    Reads: guess — a `cd` operand and the directory the shell stood in; unknown refused

hooks/commitgate.py:95  pressed
    Reads: guess — the transcript's routing answer, through `automation_answered`; unknown refused

hooks/commitgate.py:144  _process — and delete the two-line `What it reads, continued:` paragraph
    Reads: observed — `ps -o ppid=,comm=` of one process; unknown refused

hooks/dispatch.py:453  flat, the `Passed:` paragraph
    Passed: a value that is not a string gives "".

hooks/evidence-advisor.py:88  commits_in
    Reads: guess — the command split on `&&`, `||`, `;`, `|` and newlines, quotes ignored; unknown passed

hooks/sealer-stamp.py:97  load_stamp — and replace the two-line `What it reads, continued:` paragraph
    Reads: owned — `seal_stamp.py` beside this hook, loaded by path; unknown passed

    Passed: any exception, `SystemExit` included, gives None, so nothing is drawn.

hooks/tokens.py:160  _empties_the_environment, the `Refused:` paragraph
    Refused: `-i` anywhere in a short option cluster counts as emptying the environment.

hooks/version-check.py:91  due
    Reads: observed — the marker's mtime; unknown passed

hooks/worktree_consent.py:146  granted, the `What it reads, continued:` paragraph
    What it reads, continued: the path `consent_path` builds under the common git directory.

hooks/worktree_consent.py:269  _content — and delete the two-line `What it reads, continued:` paragraph
    Reads: guess — one transcript entry's `message.content` list; unknown refused

    Refused: an entry whose message holds no content list gives [].

hooks/worktree_consent.py:284  _clone_of — and delete the two-line `What it reads, continued:` paragraph
    Reads: guess — a transcript entry's `cwd`, resolved by git to its clone's common dir; unknown refused

    Refused: a `cwd` that is not a string, or sits in no clone, gives "".

skills/code-review/scripts/chain_check.py:1634  is_ancestor: delete the `What it reads, continued:` paragraph

skills/code-review/scripts/chain_check.py:1705  carried_by_a_pull_head — and delete the `What it reads, continued:` paragraph
    Reads: observed — `for-each-ref --contains <sha> refs/remotes/pull/`, exit and first line; unknown refused

skills/code-review/scripts/chain_check.py:2603  nobody_reason
    Reads: owned — one `Fixes checked by` cell: `nobody`, then a separator or nothing; unknown refused

skills/code-review/scripts/chain_check.py:4946  range_ends
    Reads: owned — the `Fix range` cell through `FIX_RANGE_RE`, both ends resolved; unknown passed

skills/code-review/scripts/round_record.py:3616  under_tests  (one-line docstring)
    """Reads: guess — a path's directories, for one named `tests`; unknown passed"""

skills/evidence-check/scripts/evidence_check.py:3438  calendar_date, the line and its `Passed:` paragraph
    Reads: owned — a `CHECKED_RE` match, asked of `datetime.date.fromisoformat`; unknown passed

    Passed: False, and the caller sorts that reading as "", oldest.

skills/evidence-check/scripts/evidence_check.py:5790  github_slug, the line and its `Passed:` paragraph
    Reads: guess — one heading's text from a `.md` file; unknown passed

    Passed: every character outside the kept set is dropped, never refused.

skills/evidence-check/scripts/pact_check.py:267  git
    Reads: observed — git's stdout and exit code; unknown passed

skills/evidence-check/scripts/pact_check.py:287  read
    Reads: observed — a file's text, decoded as strict UTF-8; unknown passed

skills/implement/scripts/seal.py:670  no_root  (one-line docstring)
    """Reads: observed — whether `optin.SCRATCH` is a file under `optin.git_common_dir`; unknown refused"""

skills/implement/scripts/seal.py:1809  plugin_workflow
    Reads: observed — `templates/hygiene.yml` and its `PLACEHOLDER`, with `plugin_version`; unknown refused

skills/verify/scripts/broad_gate.py:700  short_commit — and delete the `What it reads, continued:` paragraph
    Reads: observed — `rev-parse --short <rev>^{commit}`; unknown passed

    Passed: a failed git and a rev naming no commit both give None, and `resolve_base` tries its next step.

skills/verify/scripts/broad_gate.py:2410  unquote
    Reads: guess — one YAML scalar from a `hygiene.yml` step's `- name:` line; unknown passed

skills/verify/scripts/unverified_check.py:235  visible
    Reads: owned — a cell's text, with the `INVISIBLE` characters taken off; unknown refused

skills/verify/scripts/unverified_check.py:882  sections
    Reads: owned — a file's headings: the exact `## Not verified` first, else the matcher given; unknown refused

tests/conftest.py:105  _indent  (one-line docstring)
    """Reads: guess — one workflow line's leading spaces, by which `workflow_steps` splits steps; unknown passed"""

tests/conftest.py:113  _unquote
    Reads: guess — a step's `name:` scalar, its matching quotes taken off; unknown passed

overview.md, a row in "Where spec and implementation diverged":
| `Reads:` prose of 32 units named beside a reader in one row | `spec.md` acceptance row 4: the line carries the row's `What it reads` | each line says what its own unit reads; class and direction kept, `short_commit`'s direction `passed` | `docs/the-reader-registry.md`: the prose is what the unit reads, and a false one is limit 1; round 1 🟡 1 |

Verify: bin/test -q -p no:cacheprovider tests/test_a_reader_declares_its_input_class.py tests/test_a_rider_reaches_its_file.py
        bin/evidence-check .   (no unit above is cited; it should stay exit 0)
```

### 🟡 2

```
skills/evidence-check/scripts/correction_check.py:746  parse_range, the line, and a paragraph under it
    Reads: observed — `A..B` / `A...B` from the CLI, each end resolved by git; unknown mixed

    Mixed: no separator, or an end that does not resolve, is refused; a failing `merge-base` keeps the
    left end for `...`.

skills/verify/scripts/unverified_check.py:1401  tree_at, the line, and a paragraph under it
    Reads: observed — `os.walk` of the disk, or `git ls-tree -r --name-only <ref>` without `-z`; unknown passed

    Passed: a failed `ls-tree` gives [], the same answer as an empty directory.

hooks/hooksession.py:150  lease_dirs, the line; replace the `What it reads, continued:` paragraph
    Reads: observed — the `specseal-leases` directories under the common dir and `worktrees/*/`; unknown passed

    Passed: a `worktrees` directory that will not list reads as none.

skills/verify/scripts/deferral_check.py:156  other_ci_files
    Reads: observed — whether six fixed CI paths are files, and `.buildkite/*.yml`; unknown passed

skills/verify/scripts/payload_meter.py:375  agents_in  (one-line docstring)
    """Reads: guess — `agents/*.md`, each `name` through `frontmatter`, else the filename; unknown passed"""

Verify: the same two commands as 🟡 1, and `grep -rn "Reads: guess" skills/verify/scripts/deferral_check.py`
names `other_ci_files` no more.
```

### 🟡 3

```
hooks/cmdline.py:339-340  drop_heredoc_bodies, and hooks/cmdline.py:387-388  heredoc_bodies — the `Mixed:` paragraph in each
    Mixed: an unterminated body runs to the end of the input; an unbalanced `${` hides a
    `((` region (fails open, as `_heredoc_split`'s comment on an unbalanced `${` says)

skills/evidence-check/scripts/pact_check.py:303  origin, the `Passed:` paragraph
    Passed: "" gives no name, which `main` then refuses.
```

Needs a fix: yes — 🟡 1 (32 `Reads:` lines or paragraphs that describe another unit), 🟡 2 (five class words and two direction words the code contradicts), 🟡 3 (three wrong line references)
Loses a record or crashes: no

Not mine to run, and now come due only when these are closed: the sealer's
broad gate, once the rounds leave nothing open.

## Proof block

Opened in the clone at 8938af5b, or in the worktree for the frame:

- `seal/specs/1791382684-every-reader-and-record-is-inventoried/`: `spec.md`,
  `plan.md`, `questions.md`, `overview.md`, `phases/phase-1.md`,
  `phases/phase-2.md`, `phases/phase-3.md`, `survivors.md`, `changelog.md`,
  `routing.md`; and from `inventory/`, the rows named above, by search.
- `seal/ledger/1791382684-every-reader-and-record-is-inventoried.md`.
- `docs/the-reader-registry.md`.
- The source of all 189 units that gained a `Reads:` line, in the 44 changed
  `.py` files, and `resolve_base` in `skills/verify/scripts/broad_gate.py`.
- `hooks/cmdline.py` around lines 438 to 460, and `pact_check.py` around
  lines 514 to 545, at HEAD and at 5623d728.
- `seal/specs/1791384162-the-macos-test-leg-runs-in-shards/rounds/round-1-report.md`,
  for the report's house shape only.
