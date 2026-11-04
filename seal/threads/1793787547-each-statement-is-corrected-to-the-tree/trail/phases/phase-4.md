# Phase 4: 1793787547-each-statement-is-corrected-to-the-tree

## What this phase found

**The frame holds for this phase.** I checked it against the tree at
`d9df861ec` before the first edit (read, unless marked).

- Each coordinate *Scope* S6 to S11 gives stood where the design puts it:
  the row at `seal/follow-up.md:42` and the blank line at `:45`, the
  comment at `.github/PULL_REQUEST_TEMPLATE.md:29-34`, `ruff.toml:40-42`,
  `CONTRIBUTING.md:125-129`, `docs/releasing/branch-and-release.md:204-206`,
  item 2 of both experiment editions at `:28` and `:28-29`, and `labels:
  gate` at `.github/ISSUE_TEMPLATE/gate-misfired.md:4`.
- `git show v0.13.0:seal/specs/1788817289-local-mode-from-first-setup-to-the-gate/spec.md`
  holds *The sharp question — where an untracked declaration lands* at line
  43 (executed). `read_record`'s docstring at
  `skills/code-review/scripts/chain_check.py:477-478` says only where the
  file is read from (read). `chain_check.py`'s usage text says `--worktree`
  is "for a check before the commit" (read: `:109-110`), so the row's
  closing clause on "the transient state that flag was built for" holds.
- `tests/hooks/test_launch.py#test_what_runs_before_any_floor_is_linted_at_the_floor`
  says it holds the set to the table and that the `floor_syntax` census
  refuses. `tests/censuses.py#floor_syntax` holds each file the table
  names to its version through `newer_than`, which returns what that
  version cannot run (read).
- `gh label list` lists `hooks-gates` and no `gate` (executed).
- `.github/ISSUE_TEMPLATE/` holds `config.yml` and `gate-misfired.md`, and
  only the second has a `labels:` line (executed: `grep`). So #1338's class
  is that one line, as the design says.

**The plugin version moved in this phase, and the frame says the
orchestrator moves it.** The spawn asked this phase to move
`.claude-plugin/plugin.json` from `0.31.1` to `0.31.2` in the commit that
adds the changelog fragment. `frame/plan.md` *Operational impact* and the
`plugin.json` row of `frame/design.md` *Grounding* say that this is the
orchestrator's act and not a phase.
`skills/implement/orchestration.md` *Orchestrator: how the work is routed*
asks only that the version moves in the commit that adds the entry, and
this phase writes the entry. So I made the move in `51cea954e`, with the
fragment. The two frame sentences are not mine to write, so the hand-back
names them for the orchestrator. `plugin.json` is the only tracked file
that holds `0.31.1` (executed: `git grep -F 0.31.1`). No test reads the
running version as a literal. The `hygiene.yml` step that compares
versions runs only on a pull request into `main` (read: `:77-79`).

**S6: the citation is kept, at a commit and not at the tag the frame
names.** `frame/plan.md` *Alternatives considered* A13 lets the crafter
pick. The cited section holds more than the row restates: why answer A, the
notice, was taken, and why answer C was rejected. The row restates only the
argument about answer B. So the row keeps a citation of *The sharp question
— where an untracked declaration lands*, and it states the argument about B
in its own words.

The citation departs from the frame. *Scope* S6 gives the form
`v0.13.0:seal/specs/…/spec.md`, and `51cea954e` wrote it so. The phase
boundary run then failed on
`tests/test_censuses.py::Test_module::test_every_file_no_module_file_declares_meets_every_census`:
"seal/follow-up.md:42: old_names: `seal/specs` is a name the rename to
AgenticSeal replaced" (executed). `tests/censuses.py#old_names` passes an
old record path only in the form `HISTORY_PATH` matches, a hex commit, a
colon and the path. A tag is not that form. The frame's *Grounding* row on
where the work item stands checked `COMMIT_PATH` and the cited-section case
and did not check this census. The census is right: its comment says a
released work item's record is cited "at the commit that holds it". So
`a5c2e825b` cites
`aa687d357:seal/specs/1788817289-local-mode-from-first-setup-to-the-gate/spec.md`.
`aa687d357` is the parent of `f51e634d2`, the commit that removed the
directory. It is an ancestor of `origin/main`, and its `spec.md` is byte-identical to
the one at `v0.13.0`, with the heading at line 43 (executed: `git
merge-base --is-ancestor`, `diff`, `grep -n`). The changelog fragment
cites the same commit.
The sentence that leaned on `read_record`'s docstring now reads "Reading the
working tree would not make the local run pass what HEAD refuses", and
the clause after the colon is unchanged. I dropped "Q3 of its
`questions.md`". That row of the removed work item asked the same question
the row asks now, and #225 already names where the work came from.
The question to the owner and the answerer cell are unchanged.

The blank line went. Rendered with `cmarkgfm`, the section *Schedulable
items with nowhere else to go* gives one table with 3 body rows at
`d9df861ec` and one table with 7 body rows at `51cea954e` (executed). So
the four rows below the blank line were rendered as a paragraph before.

**S7.** The comment keeps its first sentence and cites `CONTRIBUTING.md`,
"What a change to a gate must carry", as the list of what the body
answers. It names none of the section's seven items (`frame/plan.md` A5).

**S8.** Both sentences now say that `tests/hooks/test_launch.py` derives
the set and holds it to the table, and that `floor_syntax` in
`tests/censuses.py` refuses. `ruff.toml` names the census in prose without
backticks, as the comment around it does. In `CONTRIBUTING.md` the edit
reflowed the paragraph's last lines to 88 columns, after
`tests/behaviour/test_docs_line_wrap.py` refused a 105-column line in my
first edit (executed).

**S9.** The sentence now reads "`plugin_directory_check.py` reads the name
out of `.claude-plugin/plugin.json` instead of carrying a literal." It
makes no claim about the other files that spell the name
(`frame/plan.md` A7). The case
`test_the_fixed_name_sentence_names_the_file_that_holds_the_name` pins
those words, and its docstring and comment say what it pins. The module
docstring's A8 line said the file "holds the plugin's one name", and now
says the file the name "is read from". I kept the case's name.
`plugin.json` holds the name, and the case name does not claim that it
holds the only copy. Renaming it would also move its entry in
`.test_durations`.

**S10 and S11** are one word each: "Four runs" and "네 번", and
`labels: hooks-gates`.

**The changelog fragment.** No template for `changelog.md` exists under
`templates/records/` (executed: `ls`), though the spawn said "from its
template". I followed the shape of the fragments under `seal/threads/` and
in the history: one `### Fixed` section, and one bulleted item per issue
with a bold lead that ends in the issue number. It carries no `### Process
changes` table. The work item's diff touches none of the files
`docs/layout/the-record-layout.md` *A change to the way of working writes
its process row in its own fragment* names (executed: `git diff
--name-only a3e08d64a HEAD` filtered by those paths prints nothing).

**Seen red and mutation.** No unit adds behaviour, so no `seal mutate` run
is owed. Every change is the *Prose only* row of `skills/verify/SKILL.md`
*The narrow command still has to be able to fail*, or the *A comment or
docstring inside source* row. The exception is S9's case, whose pinned
literal moved. I showed that the moved case reads the sentence at
`51cea954e`. `seal mutate` put the old sentence back into
`docs/releasing/branch-and-release.md` and ran the case under `-k`, and the
verdict was `red`: the assert on "`plugin_directory_check.py` reads the
name out of `.claude-plugin/plugin.json`" failed, and the tree was clean
after the restore (executed).

Two more runs at `a5c2e825b` show that S6's citation is read (executed).
Putting `v0.13.0:` back for `aa687d357:` gave `red` from the census case
above, on the `old_names` line at `seal/follow-up.md:42`. Putting
`aa687d350` for `aa687d357` gave `red` from
`tests/text/test_a_cited_commit_outlives_the_squash.py`, which named
"seal/follow-up.md:42 cites aa687d350". The tree was clean after each
restore.

**Acceptance A6 to A11, run at `a5c2e825b`** (executed):

- A6: the `git show v0.13.0:…` heading check prints line 43, and the file
  is the one `aa687d357` holds. The `awk` over lines 40 to 50 shows one
  blank line, line 49, after the table's last row and before the next
  heading.
- A7: `sed -n '25,40p'` shows the comment citing the section and listing no
  item.
- A8: `git grep -n floor_syntax -- ruff.toml CONTRIBUTING.md` prints
  `CONTRIBUTING.md:127` and `ruff.toml:41`.
- A9: `git grep -n 'holds the one copy\|nothing else in the tree' --
  ':!seal/threads'` prints nothing and exits 1.
- A10: `sed -n '24,32p'` on each edition shows "Four runs" and "네 번".
- A11: the `gh label list` lookup prints `hooks-gates` and exits 0.
- The row's `bin/test` command over its eight modules: 172 passed, exit 0.

**Other places that state what this phase reworded, a sample.** `git grep`
outside `seal/threads/` for "three runs edited", "세 번은 클론", "holds the
one copy", "nothing else in the tree", "labels: gate", "refuses in each
the syntax", "the axis `read_record`" and "Q3 of its `questions.md`"
prints nothing (executed). "is the whole of it" stands at
`CONTRIBUTING.md:47`, which `frame/design.md` *Out of scope* O4 keeps, and
at three lines that say it of something else. `test_launch.py` is cited at
`hooks/lib/launch.py:27` for holding the floor's version equal to
`ruff.toml`'s, and at `tests/censuses.py:761` as deriving the set. Both
agree with the corrected sentences. None of the corrected sentences
carries a `check:` line. The list is a sample, because the searches match
spellings.

**Phase boundary run.** This is the *Phase boundary* row of
`skills/verify/SKILL.md` *Scope: cheap and often, broad and once*, run as
one `bin/test … -q` over 86 modules. The lists came from `git grep -l` over
`tests/*.py` (executed):

- the modules that name a changed path: `ISSUE_TEMPLATE`,
  `PULL_REQUEST_TEMPLATE`, `CONTRIBUTING`, `experiments`,
  `branch-and-release`, `ruff.toml`, `follow-up` or `FOLLOW_UP`,
  `plugin.json`, `changelog` or the changed test module
- the modules that walk files (`ls-files`, `rglob`, `os.walk`, `glob(`) and
  name `.md`, `.github` or `.toml`
- the plan row's eight modules, `tests/test_censuses.py`,
  `tests/hooks/test_launch.py`, and the four modules that read this work
  item's records

The first run, over `51cea954e` with this record, the `gaps.md` rows and
the Status cell in the working tree, failed one case, the `old_names`
census above. The second ran over `a5c2e825b` with the same three files in
the working tree: 3781 passed and 14 skipped (executed, exit 0). The
selection is my reading of "a module that reads a path the phase changed".
A module that reads those files through a helper these searches do not
name is outside it, and the broad run covers that.
