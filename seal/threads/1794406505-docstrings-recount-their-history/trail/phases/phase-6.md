# Phase 6: 1794406505-docstrings-recount-their-history

## What this phase found

**The count is 115 at the phase's last commit, below design S2's 150
(design *Scope* item 8).** The phase is 15 commits from `846a446a5` to
`54086012e`, started at `79a5f94c7`, the merge of `origin/release/v0.37.4`
at `810ef9018` that brought #1489 in, and one commit after the framer's fold
`b2ba1dcd0`, `a296ae8e4`, which changes two test docstrings (below) and no
file the count reads. The counting command of design *Data
& interfaces*, taken from that file into the phase's scratch directory and
run with `python3 -I`, printed these totals (executed):

| Commit | files | lines | blank | prose | code | hits |
|---|---|---|---|---|---|---|
| `38123f839`, the base | 50 | 33,491 | 2,776 | 13,216 | 17,499 | 869 |
| `79a5f94c7`, the phase's start | 50 | 33,279 | 2,778 | 13,004 | 17,497 | 225 |
| `54086012e`, the last commit before the fold | 50 | 33,234 | 2,778 | 12,959 | 17,497 | 115 |
| `a296ae8e4`, the phase's last commit | 50 | 33,234 | 2,778 | 12,959 | 17,497 | 115 |

117 of the 225 hit lines at `79a5f94c7` were in the files of design
*Scope* item 7, and 7 are left there. The other 108 stand in the files
phases 1 to 5 rewrote, unchanged by this phase. The code and blank figures
moved between the base and `79a5f94c7` because #1489's merge changed
`skills/verify/scripts/test_layout.py`'s code, not because of this work.

**Only prose changed in the scripts (design S1).** The code command over
`79a5f94c7..54086012e` with `lib hooks .github/scripts skills` printed `15
.py files differ in text; code differs in: none` and exited 0. With no
pathspec it printed `16 .py files differ in text; code differs in: none` and
exited 0; the sixteenth file is the test file below, whose change is a
comment (executed). Over the whole build range, `c21b4248f..54086012e`
with S1's pathspecs, it names `skills/verify/scripts/test_layout.py` and
exits 1 (executed). That is #1489's code, which the merge carried in, as
design *Data & interfaces* says a range holding a merge does. `bin/test` is
a shell script and outside the command; its diff changes two lines, both
comments.

**The frame held against the tree, except one coordinate.** Design *Scope*
item 10 places the comment of
`tests/github/test_label_merged_on_release_branch.py`'s
`test_the_label_reader_has_one_source` at `:365-368`, and *Removes* at
`:365-367`. At `79a5f94c7` it stood at `:369-372`, because #1489's merge
moved the file's lines (read). The comment is the one the frame means, and
the phase corrected it there. The hand-back names the coordinate for the
orchestrator.

**Every docstring and comment of the files of item 7 was read, not only
the hit lines.** `lib/blocks.py`, `lib/config.py`, `lib/console.py`,
`lib/core.py`, `lib/gate.py`, `lib/gitcmd.py`, `lib/items.py`,
`lib/launch.py`, `lib/sibling.py` and `hooks/core-start.py` were read whole.
For `lib/fields.py`, `lib/gaps.py`, `lib/lines.py`, `lib/optin.py`,
`lib/routing.py`, `lib/tables.py` and `skills/verify/scripts/test_layout.py`,
a scratch script printed every docstring and comment line with its number,
by the counting command's own rule. Each line was read, with the code at
its line where the sentence named it. `bin/test` was read whole. Each
sentence was judged by design *Scope* item 1. One commit per file or pair
of files. Outside the hit listing, these went or were rewritten:

- the reading before `lib/blocks.py`'s walk, called "the old one", "as it
  did before" and "from before #667" in `blocks.py`, `lines.py`,
  `routing.py` and `tables.py`. Each now names the reader's base reading,
  the term `blocks.py` already defined: a reader's own rule alone, such as
  `blocks.fence_only` for `tables.py`;
- coordinates into work items' records: "the frame's shapes" in
  `blocks.py` and `lines.py` (now "that file's named shapes", for the
  `SHAPES` the test files build), `frame/design.md`'s rule in `tables.py`,
  and `plan.md` *Alternatives considered* in `lines.py`;
- former states: `gate.py`'s paragraph on the commit gate that once lived
  there, `console.py`'s pull request that was closed and its two review
  rounds, `lines.py`'s five earlier spellings of the heading rule,
  `routing.py`'s commit gate that re-derived the route and its `Planning`
  axis arriving after seventy-two declarations, and `optin.py`'s "Found by
  CI's Windows leg";
- sentences in the past tense about a defect a branch guards, which now
  state the defect as a case that can happen. Examples: `optin.py`'s
  `.strip()` "raised", `gaps.py`'s zero-width space that "turned" a
  separator into an item, `config.py`'s "#151 is what that costs", and
  `routing.py#rounds_unreadable`'s first and second versions.

A removed sentence sometimes held the only statement of a reason. There the
reason is now in the present tense, in the same docstring or comment.
`lines.py#live_lines`' "This is what five review rounds cost" became "Both
readings, and not a better guess", which states the shape a single guess
reads wrong. `routing.py#parse`'s account of keeping the LAST row became the
reason a doubled label has no value: taking the last row lets a second
`Review` row answer for the first with nothing saying there were two.

**Four stored counts of the tree went (design *Scope* item 1).** The phase
took this as a departure from K3, which then kept an evidence count without
its date and issue, and the fold `b2ba1dcd0` wrote it into item 1's list of
what goes. These counts count the tree itself, and they no longer match it,
so they went:
`routing.py`'s "all 84 declarations already committed here", "none of the
86 committed declarations", "28 of this repository's 35 work items", and
`lines.py`'s "944 lines of them" for issue references. Each sentence now
states its reason without the count, such as "every declaration committed
without it". Judged against `skills/core/SKILL.md` *The rule a mechanism is
kept against*: nothing is kept beside the tree to stay in step with it,
such as a stored count. Evidence counts of
observations stay under K3: `tables.py#gfm_table`'s generator over 600,000
documents, and `bin/test`'s seventeen test calls.

**Two sentences pointed at a rider that does not stand.**
`lib/optin.py#git_common_dir` and `#home_paths` each said "the rider on
`repo_root` counts" what a `git` call costs. No `RIDER:` comment stands in
`lib/optin.py` at the base or at `79a5f94c7` (executed: `git show
38123f839:lib/optin.py | grep -n -i rider` printed only those two
sentences). A pointer to something that is gone states a former state.
Each sentence now states the cost directly: a `git` process started there is
paid on every gated command. `tests/lib/test_optin.py:141` and `:236`
stated the same fact in two test docstrings. Design *Scope* item 10, as the
fold `b2ba1dcd0` widened it, corrects every other statement of a fact this
work corrected, and `a296ae8e4` rewrote both clauses to the same cost ground:
"which every gated command would pay" and "A second `git` call here would
be paid on every gated command". No assert changed. `git grep -n 'rider on
.repo_root' -- . ':!seal'` prints nothing at `a296ae8e4` (executed).

**The hit lines of item 7 that stay, each with its keep class.**

| Line at `54086012e` | Class | Why it stays |
|---|---|---|
| `lib/core.py:43` | K3 | the harness's output cap, "Measured between 9,990 and 10,010 on Claude Code 2.1.312": the evidence `CAP` rests on, with the version, and its issue gone |
| `lib/gitcmd.py:8` | K3 | "each key measured to do that": the evidence each held key rests on |
| `lib/optin.py:100` | K3 | "Measured on a cp949 console": the observed behaviour the `encoding=` argument exists for, with no date |
| `lib/tables.py:243` | K3 | "a line the renderer was measured to end the table at": the evidence each END arm rests on |
| `lib/tables.py:250` | K3 | "measured against cmark-gfm one tag name at a time": the evidence `TABLE_END`'s HTML arms rest on |
| `lib/lines.py:302` | K1 | `` `#120) was …` ``, a sample of an issue reference opening a wrapped line, which `heading_level` reads as no heading |
| `lib/lines.py:502` | K1 | `` `#120)` ``, the same sample, in `headings`' reason for the one rule |

**Kept as K5.** These sentences name the shape of an older record or input
a branch still reads, and stay: `config.py`'s `config.md` table "an earlier
release read and no command reads now", 0.3.x's top-level `specs/`, and
the `Pact notify` key; `fields.py`'s `confirms: none` from "an earlier
release's template"; `gaps.py`'s old closing mark, U+2705; `items.py`'s old
`none — <why>` line; and `routing.py`'s `rounds` file that an earlier
release's migration command makes, and its old flat location that is not
read.

**Sentences no class fitted cleanly, and what each became.** Each took
`frame/questions.md` Q1's default and was kept, rewritten in the present
tense.

- `lib/blocks.py`'s FENCE comment named "#429's body and
  `trail/rounds/round-3-report.md`" as where this repository's records wrap
  an example in four backticks. The record path is a work item coordinate
  and the issue is provenance, so both went. The observation stays: "This
  repository's own records wrap a fenced example in FOUR backticks".
- `lib/gaps.py#open_record_rows` said "#514's frame measured the loss this
  prevents". It now states the loss as a case: the only record that a
  production workflow is red can sit in a retiring closing memo.
- `lib/lines.py#_paragraph_ends_at` gave a measurement of 2026-09-22 and
  two review rounds. The example input stays as the evidence, without its
  date: without the setext underline stop, it reads its last two lines
  live where the format parks them.
- `lib/routing.py`'s `Automation` comment said `no` is "the half the
  measured instance got wrong". It now says "the half a reader gets wrong",
  without the instance.
- `lib/console.py` opened its three decisions with "each was paid for once
  already on the branch that first attempted this". It now opens "each with
  the failure it prevents", and each decision already states its failure.
- `bin/test`'s "Issue #156: the form CONTRIBUTING.md named paid 55-58
  seconds of setup per call, on all seventeen test calls of one measured
  segment" became the cost without its issue and its document: "A command
  that resolves its environment pays 55-58 seconds of setup per call, and
  one session segment paid that on all seventeen of its test calls". It is
  the same wording `run_tests.py` took in phase 5.

**Printed strings stay, per design *Scope* Out.** No string constant of
item 7's files carries a hit. `test_layout.py`'s `--help` description is a
string constant, and its module docstring's first line did not change.

**Design *Scope* item 10: the sentences it names, and S7's search over the
whole build range.**

- `.github/workflows/hygiene.yml:47-48` said `close_issues_on_release.py`'s
  comment stands "two lines above its regex". It now says the comment stands
  "over `KEYWORDS`", which is where it stands at `54086012e` (read).
  Nothing else in the file changed.
- `tests/github/test_label_merged_on_release_branch.py:369-372`, the comment
  over `assert "_issue_api(" not in source`, said the sibling's docstring
  tells in prose that it used to unpack `closer._issue_api`. It now gives
  the reason the assert reads the call and not the bare name: the sibling's
  prose may name `closer._issue_api` to say what it delegates instead of
  calling. The assert did not change.
- `tests/lib/test_optin.py:141` and `:236`, after the fold `b2ba1dcd0`:
  two docstrings citing "the rider on `repo_root`", corrected in
  `a296ae8e4` as the paragraph on the rider above says.

S7's search ran over `c21b4248f..54086012e`. It covered the 48 files the
range changes under `lib hooks .github/scripts skills bin`, other than
markdown. A scratch script ran `git grep -i -E 'docstring|comment'` over
`tests`, `evals`, `.github/workflows`, `docs`, `skills/**/*.md`, `agents`,
`templates`, `CONTRIBUTING.md`, `README.md` and the five script trees. It
kept each line that names one of those files and has a verb such as says,
names, holds, states, gives, keeps or carries. It listed 32 lines
(executed). 17 match only on `test`, `bin/test`'s basename: they name a
test or a test function and no edited script's prose. Each of the other 15
was read against `54086012e`, and none is false.

- `publish_release_note.py:95` and `tag_release.py:36` cite the reason
  `close_issues_on_release.py`'s docstring gives for `DRY_RUN`, which it
  still gives.
- `release_seal.py:43` cites the rule `publish_release_note.py`'s
  docstring states for its summary, "The summary adds no way to fail".
- `lib/blocks.py:162` sends the reader to `lib/tables.py#hidden_lines`
  for why a row below an unclosed fence stays hidden, which that docstring
  states.
- `lib/config.py:29` says `optin.py`'s docstring says there is no config
  key and everything fails toward *not opted in*, and it says both.
- `tests/behaviour/test_waiver_decided_at_start.py:245` says
  `routing.py#parse`'s docstring promises one template and a test that
  parses it, and that sentence stands.
- `tests/behaviour/test_every_entry_point_runs_at_the_floor.py:199` cites
  `lib/launch.py`'s docstring, which this work did not change.
- `tests/github/test_label_merged_on_release_branch.py:361` says the
  sibling's docstring says it exists not to keep a second reader, and
  `issue_labels`' docstring says one source.
- `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:69` names
  the comments `broad_gate.py` carries on the panel's `gate` arm. They
  stand at `broad_gate.py:287` and in `gate_copy`'s docstring.
- `hygiene.yml:47` is the line this phase corrected.
- The other five name a script's code, a function or a constant, not its
  prose: `docs/layout/the-record-layout.md:152`,
  `skills/settle/scripts/rule_changes.py:114`,
  `skills/verify/scripts/payload_meter.py:41`, `tests/lib/test_lines.py:148`,
  and a fixture string in
  `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:833`.

The wording is unbounded, so the list is a sample. The comment above in
`test_label_merged_on_release_branch.py` is one line it misses, because it
says "the sibling's docstring" without naming the file. The phase also
searched with `git grep` for the words of each sentence it removed. Two hit
test docstrings that stated the same fact as a removed sentence,
`tests/lib/test_optin.py:141` and `:236`, which `a296ae8e4` corrected.

**No case reads the prose of item 7's files.** Pins were looked for by
design G9's method, not taken from its list. `git grep -n -E
'__doc__|get_docstring|getdoc|inspect\.getsource' -- tests evals` names no
case on a file of item 7. A `test_tmp_*` probe listed each string constant
of four or more characters, in the tracked `tests/*.py` and `evals/*.py`,
that occurs in a changed file at `79a5f94c7` and not at `HEAD`. It listed
377 entries (executed). Among them, the 23 of three or more words or
fifteen or more characters are `CONTRIBUTING.md` (gone from `bin/test`),
`*Alternatives considered*` (gone from `lines.py`), `trail/rounds/round-`,
`the round record` and `two declarations`. Each was read at the case: the
cases read documents, fixtures or a commit message, never these files'
prose. No test file reads `bin/test`'s comments (executed: `git grep` for
the path in `tests`). A case that reads a script's text by a regular
expression is outside the probe, so this list is a sample. The boundary run
below reads every test file that names one of the changed paths.

**No unit adds behaviour, so no `seal mutate` run is owed.** The edits are
comments and docstrings, the *A comment or docstring inside source* row of
`skills/verify/SKILL.md` *The narrow command still has to be able to fail*.
The one test edit rewrites a comment, and no case was written or changed.

**Line width.** A scan of the lines `79a5f94c7..54086012e` adds under `lib
hooks skills bin` found none over 79 characters (executed). `54086012e`
rewraps the five lines the earlier commits left over 79.

**S6, S5 and the phase boundary run.** `uvx ruff check` and `uvx ruff
format --check` exit 0 over the 16 changed `.py` files at `54086012e`
(`16 files already formatted`) (executed). `sh -n bin/test` exits 0
(executed). The phase boundary set ran as one command, `bin/test -q`, over
`tests/text`, `tests/behaviour`, the changed test file, and the 45 test
files outside those two directories that name a changed path. A file names
one where it names a `lib/` module by path or by its import name, `"lib"`,
`core-start`, `test_layout`, `hooks.json`, `hygiene.yml` or `bin/test`. G10's
module, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, is in
the set. It ran at `54086012e` with this record, `gaps.md`, `changelog.md`
and the Status cell in the working tree, printed `5254 passed, 9 skipped`
and exited 0 (executed).

**The commit after the fold, `a296ae8e4`.** The code command over
`b2ba1dcd0..a296ae8e4` with no pathspec printed `1 .py files differ in
text; code differs in: none` and exited 0 (executed). `uvx ruff check` and
`uvx ruff format --check` over `tests/lib/test_optin.py` exit 0, and
`bin/test tests/lib/test_optin.py -q` printed `70 passed` and exited 0
(executed).
