# Review round 1: 1794406505-docstrings-recount-their-history

```seal
target: eee830571 against origin/release/v0.37.4
```

This is the first round, so no earlier record carries a coordinate and every
fact below was established here. The diff was read from the merge base
`810ef9018`, the tip of `origin/release/v0.37.4`, to `eee830571`, in a
`git clone --no-local` of the branch. `routing.md`, the three frame files,
`gaps.md`, `changelog.md` and `pr.md` were each read whole at `eee830571`,
and so were the six phase records. No `pr.<lang>.md` stands, and none is
owed: `seal/config.json` names English for both language keys. No
`seal/parity.json` is declared.

The diff holds 2,210 removed and 1,960 added lines under `lib`, `hooks`,
`.github/scripts`, `skills` and `bin` (executed: `git diff -U0` counted).
Design S4 asks that no removed sentence took the only statement of a
present reason with it. The round read S4 as a sample, by two methods.
First, a probe listed every removed prose line that carries a reason word
(because, rather than, why, otherwise, guard, deliberate, never, must and
the like) where fewer than half its words return in the added lines of the
same hunk. It listed 32 lines across 10 files, and each was read beside
its hunk and the code at HEAD. Second, the whole diff was read for the 16
files under `.github/scripts/`, `bin/test`, `hooks/core-start.py`, the 13
changed files under `lib/`, `skills/code-review/scripts/chain_check.py` and
`skills/verify/scripts/seal_stamp.py`, and in part for
`skills/implement/scripts/seal.py` (to its base line 1290),
`skills/verify/scripts/broad_gate.py` (to base line 830) and
`skills/verify/scripts/session_cost.py` (to base line 935). The diffs of
`pr_body.py`, `fold_check.py`, `rule_changes.py`, `settle.py`,
`coordinates.py`, `deferral_check.py`, `mutation_check.py`,
`pact_check.py`, `payload_meter.py`, `agentic_pytest_record.py`,
`test_layout.py`, `unverified_check.py` and the rest of the three partly
read files were reached by the first method only. Neither method found a
reason the rewrite lost. `## Not judged` names the part the second method
did not reach.

## Findings

### 1. The closing memo puts the 716 s median over all 433 segment rows, and the docstring it reports puts it over 381 named rows

```seal
severity: should
location: `seal/threads/1794406505-docstrings-recount-their-history/gaps.md:11-16`
evidence: read `seal/threads/1794406505-docstrings-recount-their-history/gaps.md:11-16`, `skills/verify/scripts/session_cost.py:1723-1728`, `skills/verify/scripts/session_cost.py:819-826`; executed `git show 810ef9018:skills/verify/scripts/session_cost.py | grep -n -E '716|433'`
```

Why it matters: `gaps.md` *Not done* is copied whole into the pull request
body by `seal pr-body` (`skills/code-review/scripts/pr_body.py:14-15`). Its
first paragraph exists to set two figures side by side for a reader who
will settle them, and it misreports one of the two.

- **Claimed** in `gaps.md:13-16`: "`measure_segments`' docstring says that
  over 433 segment rows the median is 716 s and 1,000 is the mean".
- **Found** at `skills/verify/scripts/session_cost.py:1724-1726`: "Over
  every segment row of 43 runs with a `subagents/` directory, the median is
  716 s over 381 named rows and 664 s over all 433, and 1,000 is the MEAN
  (1,018)". The median over all 433 rows is 664 s. The base holds the same
  sentence at line 1787, so the build did not move it. The memo's account
  of it is wrong.

The other statements of the figure hold. `frame/design.md` *Scope* Out
says the docstring "gives 716 s as the median and 1,000 s as the mean over
another population", which is loose and not false.
`trail/phases/phase-1.md:94-101` is the phase's own dated account and is
not corrected in place. The fix is the memo's first paragraph alone:

```markdown
Phase 1 left `skills/verify/scripts/session_cost.py`'s two statements of
how long a subagent runs side by side. `DELEGATING`'s comment and
`spawn_cycles`' docstring say "a median of about 1,000 seconds" over 67
spawns of three runs. `measure_segments`' docstring says that over the
segment rows of 43 runs the median is 716 s over the 381 named rows and
664 s over all 433, and that 1,000 is the mean. Which the first
figure is cannot be read from the tree, and settling it means re-reading
transcripts that live on one machine, which a prose-only phase does not do.
Both sentences are present-tense claims a reader can hold against each
other, so neither recounts history.
```

```seal
verdict: fixed d1a2f007b
answer: The finding holds: `session_cost.py:1724-1726` gives 716 s over 381 named rows and 664 s over all 433. `gaps.md:14-17` takes the record's replacement text. The fix and the finding are in the work item's records alone, so the sealer reads it with no further round.
```

## Confirmations

What matched: design S1 holds over the whole review range. The code command
of design *Data & interfaces*, run from the frame's own block over
`810ef9018..eee830571` with `lib hooks .github/scripts skills`, printed `47
.py files differ in text; code differs in: none` and exited 0. With no
pathspec it names `tests/skills/test_session_cost.py` alone, the one
removed assert (executed).

What matched: design S2 and the changelog's table. The counting command
prints 869 hits, 13,216 prose lines and 17,499 code lines at `38123f839`;
869, 13,216 and 17,497 at `810ef9018`; and 115, 12,959 and 17,497 at
`eee830571` (executed). The two code lines moved at `810ef9018`, the merge
of #1489, as `changelog.md:7` says.

What matched: design S3. Each of the 115 lines of the `--hits` listing at
`eee830571` was read at its line. Each is K1 to K5 of design *Scope* item
1, in the class the phase records give it, or is one of the sentences a
phase record names under `frame/questions.md` Q1's default, such as
`.github/scripts/close_issues_on_release.py:120` (the probe pull requests
#1402 to #1410) and `skills/verify/scripts/seal_stamp.py:1116-1126`
(read). A wider listing of the same prose for `round N`, `finding N`,
`questions.md`, a work item id, `Q<N>`, `no longer`, `formerly`, a release
number, `the old`, `predecessor`, `first cut` and `review round` found no
pointer into a work item's records and no recounted former state that
item 1 removes, outside the K5 shapes and the Q1 sentences the phase
records name (executed, two `test_tmp_count` variants; read: each line).

What matched: the issue each K4 sentence now names is the one its base
coordinate pointed at, for the three this round traced (executed: `git log
-S` on each sentence's base words; read: the base text).
`seal_stamp.py:1116`'s #976 is the issue of `75502328`, which wrote the
sentence's earlier form around "Q2 of work item 1792363231".
`seal_stamp.py:520`'s #666 is what the base `broad_gate.py:1926-1927` cited
for the same choice, "`questions.md` Q1 of #666". `seal_stamp.py:666`'s
rule entered at `a56758fc`, whose subject is the stamp fitting the
harness's message limit, the work `admitted`'s base docstring cited as
#717; that `a56758fc`'s pull request closes #717 was not opened.
`.github/scripts/publish_release_note.py:664-665` rests on phase 5's quote
of #857's body, which this round did not open.

What matched: the printed text stays. The module docstring heads design G8
names, the first line of `issue_claims_check.py`, `release_report.py` and
`rules.py` and the first paragraph of `payload_meter.py`, are byte-equal at
`810ef9018` and `eee830571` (executed). No `check:` line in the tree
targets a script under the four trees, so `rules.py`'s docstring reader
prints nothing this work changed (executed: `git grep` over `check:`
lines).

What matched: design S5. The five docstring pins of design G9 and the whole
of G10's module, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`,
pass at `eee830571`: `bin/test` over the six files with `-k 'docstring or
Test_module or cited'` printed `130 passed`, and a collection run named
each of the five pins (executed).

What matched: `pr.md`'s 22 quotes each stand word for word, whitespace
collapsed, in `frame/plan.md`, in the row each coordinate names (executed:
a probe over both files; read: each row).

What matched: `changelog.md`. Its 50 files are the 32 Python files under
`lib/`, `hooks/` and `.github/scripts/` and the 18 under `skills/*/scripts/`;
47 of them changed, and `passages.py`, `lib/gitcmd.py` and `lib/launch.py`
did not (executed). Its third bullet matches the diff of
`.github/workflows/hygiene.yml:47-48`,
`tests/github/test_label_merged_on_release_branch.py:369-372` and
`tests/lib/test_optin.py:141` and `:236`, and no assert changed there
(read).

What matched: `gaps.md`'s other paragraphs. The `--preflight` help's
`(#638)` stands at `broad_gate.py:2443`; the three `since #1198` refusals
at `chain_check.py:323`, `:1674` and `:1721`; the three `(#931)` strings
at `durations_union.py:142`, `:178` and `:209`; `(#198)` at
`roll_flow_measurement_issue.py:317`; and the rider's instruction at
`skills/implement/scripts/seal.py:1716-1727` (executed: `git grep`).

What matched: rewritten sentences that make a new claim about the tree.
`plugin_directory_check.py:5-8` says a box of
`docs/releasing/release-checklist.md` *After the merge* runs the script,
and the box stands at line 316. `broad_gate.py`'s module docstring says
each check's output goes to a file, and `run` keeps it under
`keep/<name>.txt`. `broad_gate.py:290` and `:372` name `INVOKED_AS_VAR`,
defined at `:2376`. `lib/routing.py:432-437` names why `islink` is asked
before `exists` and `isdir`, which the code below it does. The
`merge_base` docstring of `release_completeness_check.py:124` points at
"the paragraph above", which rejects `origin/main..HEAD` at lines 113-117
(read).

What matched: design S7. This round's own search listed every line of the
named trees that names an edited script's docstring or comment beside a
verb. The six that name one function's docstring were each read against
`eee830571`. None was made false by this work (executed: `git grep`; read:
each line). `tests/lib/test_tables.py:44` says `gfm_table`'s docstring
names a container two blocks deep as what the walker cannot see, and the
docstring states that only as block state none of its three checks
carries. It said the same at `810ef9018`, so the sentence is outside
design *Scope* item 10, and this round names it here and opens no finding.

What matched: `frame/questions.md` Q1's answer. Each of the six phase
records has a section naming the sentences that took the default, by file
and function (read).

What matched: design *Removes*. `lib/routing.py`'s 84 and 86 declarations
and 28 of 35 work items, and `lib/lines.py`'s 944 lines, stand nowhere
under `lib/` at `eee830571` (executed: `git grep`). The removed
`token_thirds` assert leaves the case's assertions on the check's path and
both residuals (read: `tests/skills/test_session_cost.py:6960-6977`).

What matched: the closing memo's `## Not verified` row is honest. It names
the suite, the repository-wide lint and the format check beyond the
phases' boundary sets as unverified, with the orchestrator's broad gate as
its answerer.

The diff adds no test case, so no new case is read against its group. The
`chain_check.py` run over the worktree printed no notice at a line of
`frame/design.md`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite, the repository-wide lint and the format check at `eee830571` | the whole tree | the orchestrator's broad gate |
| Design S4 by a whole read of the diff, for the files and line ranges the intro names as reached by the reason-word probe alone | `pr_body.py`, `fold_check.py`, `rule_changes.py`, `settle.py`, `coordinates.py`, `deferral_check.py`, `mutation_check.py`, `pact_check.py`, `payload_meter.py`, `agentic_pytest_record.py`, `test_layout.py`, `unverified_check.py`, and `seal.py`, `broad_gate.py` and `session_cost.py` past the base lines the intro gives | the orchestrator, who decides whether a later round or the sealer reads them |
| The K4 decisions this round did not trace to their issue: `fold_check.py:22` (#953), `broad_gate.py:1890` (#832) and `:1908` (#666), `publish_release_note.py:665` (#857), `seal_stamp.py` lines naming #832 and #1174, and `session_cost.py:667` (#642) | those lines | the sealer, against each issue |

## Probes

| Command | Result |
|---|---|
| `python3 -I scratch/test_tmp_count.py clone <rev>` at `38123f839`, `810ef9018`, `eee830571`, the block extracted from `frame/design.md` | hits 869, 869, 115; prose 13,216, 13,216, 12,959; code 17,499, 17,497, 17,497 |
| `python3 -I scratch/test_tmp_count.py clone eee830571 --hits` | 115 lines, each read |
| `python3 -I scratch/test_tmp_same_code.py clone 810ef9018 eee830571 lib hooks .github/scripts skills`, and with no pathspec | `47 .py files differ in text; code differs in: none`, exit 0; with no pathspec, 50 files and `['tests/skills/test_session_cost.py']`, exit 1 |
| `python3 -I scratch/test_tmp_count2.py` and `test_tmp_count3.py`, the counting command with a pattern of history wording | 442 and 49 lines at `eee830571`, the specific markers filtered and each read |
| `python3 -I scratch/test_tmp_lost_reasons.py scratch/full.diff`, over `git diff -U0 810ef9018 eee830571 -- lib hooks .github/scripts skills bin` | 32 removed reason-word lines whose words the hunk's added lines mostly lack, each read with its hunk |
| `python3 -I scratch/test_tmp_quotes.py` over `pr.md` and `frame/plan.md` | 22 quotes, 22 found |
| `bin/test` over the five G9 pin files and `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `-q -k 'docstring or Test_module or cited'` | `130 passed, 3 warnings`, exit 0 |
