# Phase 5: 1793661729-each-document-is-cut-by-who-opens-it

## What this phase found

**The frame holds for this phase.** It was read against the tree at
ecaa65963 before the first move (read). `docs/the-review-record.md` held the
five sections D3 names, and `docs/the-record-layout.md` held the two it
names. The fifteen documents D3 moves whole stood at the top of `docs/`.
`ls seal/threads` listed one directory, this work item's, so no other
design's `## Rule changes` had an operation to re-point (D9).

**A repair of phase 2 opens the phase.** ecaa65963 gives
`tests/github/test_release_report.py` `Test_documents` an accepts case and a
refuses case, in the shape `seal layout` asks. `seal layout --check tests`
went from two refusals to "150 files read, 0 refused" (executed). The
refuses case was seen red with `seal mutate` on
`skills/settle/scripts/fold_check.py`. The mutation replaced
`for group in named` with a walk of every directory under the root, and the
refuses case failed while the accepts case passed (executed).

**The commits.** Each group went in its own commit, with its index table
and its re-pointed citations:

- 29d8ca6a4: the cut. Seven new documents, `docs/the-review-record.md`
  deleted, 226 lines out of `docs/the-record-layout.md`.
- 7f5690b2b: `docs/releasing/`.
- e7419b994: `docs/forms/the-reader-registry.md`.
- 8b6922aa0: `docs/checks/the-session-hooks.md` and
  `docs/checks/the-routing-check.md`.
- 7a7860cf7: `docs/running/`, five documents.
- 47533e717: `docs/layout/`, four documents. The same commit rewrote the
  index intro and added the axis sentence to `skills/implement/SKILL.md`
  *Document layout*.
- 2e7a946c9: the release report's table case reads the groups (below).

**A decision: the cut went in one commit, not one per group.** The seven
new documents stand in three groups. Cutting them group by group would have
deleted each section from `docs/the-review-record.md` in one commit and
written it into its new file in another. That writes each removal twice and
leaves a commit with the text in two places. The source file is deleted at
the end of the cut, so one commit holds the move whole. Judged against D3,
which deletes the file "once its sections have left it", and the spawn's
"commit each group with its index table and its re-pointed citations". Every
later group went one commit each.

**Four path-less cross-references now cross documents, and each carries a
path (D7).** A read-only scan of the old `docs/the-review-record.md` listed
every italic span not preceded by a backticked path (executed). Four of them
name a section that now stands in another document:

- old line 141, *The round record*, in the check's section. It now reads
  `` `docs/forms/the-round-record.md` *The round record* ``.
- old line 305, *What the check reads at the pull request*, in the
  guarantee. It gained `docs/checks/the-pull-request-check.md`.
- old line 327, "(*The stamp*)", in the guarantee. It became
  `` (`docs/checks/the-stamp.md` *The stamp*) ``.
- old line 471, *What the check reads at the pull request*, in *The run*. It
  gained the same path.

Old line 539 names *Alternatives considered*, a section of a frame's plan,
not of the record, so it stays as it was. The two sections cut from
`docs/the-record-layout.md` hold no path-less reference to a section that
moved (read). No case reads these references, so the proofer reads them.

**S7: the moved text is unchanged (executed).**

- Section moves, at 29d8ca6a4. Each new document's body was compared with
  its lines in `git show ecaa65963:docs/the-review-record.md` or
  `docs/the-record-layout.md` through `diff`. `the-round-record.md` (old
  lines 8-111), `the-stamp.md` (341-467), `the-fold.md` (record layout
  78-281) and `the-unverified-record.md` (283-302) exit 0. The other three
  differ only at the four cross-references above, and in one fold citation
  in `the-pull-request-check.md`, re-pointed to `docs/checks/the-fold.md`.
  Later group commits re-pointed paths inside them. One example is
  `docs/checks/the-stamp.md`'s citation of `docs/running/the-broad-gate.md`.
- Whole-document moves. `git diff -M --name-status ecaa65963 HEAD -- docs`
  lists each as `R` with similarity 88 to 100. `git diff -M
  --word-diff=porcelain` over them, keeping the added and removed words that
  do not contain `docs/`, prints nothing. So every changed word is a path,
  and the rest is re-wrapping.
- `docs/layout/the-record-layout.md` shows as `D` and `A`, since the cut
  took 226 of its lines first. Its HEAD text was compared with the base text
  minus lines 78-303 (`awk 'NR<78 || NR>303'`, then
  `git diff --no-index --word-diff=porcelain`). The only changes are
  `docs/release-checklist.md` and `docs/the-routing-check.md` re-pointed.

**S8: fifteen old paths list nothing; the sixteenth lists nine historical
lines (executed).** At ecaa65963,
`git grep -n -F "docs/<name>.md" -- ':!seal/' | wc -l` counted:

```
branch-and-release 39        the-agent-set 11
issues-and-milestones 46     the-broad-gate 11
measuring-a-run 5            the-pact 10
one-root-by-lifetime 14      the-reader-registry 3
one-root-by-lifetime.ko 3    the-record-layout 41
release-checklist 33         the-review-and-parity-arms 21
the-routing-check 26         the-review-record 104
the-session-hooks 5          what-a-script-gates 4
```

At 2e7a946c9 the same command prints 0 for every name but
`the-review-record`, which prints 9. A second grep, for the tuple spelling
`"docs", "<name>.md"` of all sixteen names, lists nothing. The nine lines
are:

```
evals/scripts/replay_targets.py:24:  labelled   0.22.0's record (`v0.22.0:docs/the-review-record.md` *The
evals/scripts/replay_targets.py:28:             `docs/the-review-record.md` holds, so each record is judged by
evals/scripts/replay_targets.py:281:    "docs/the-review-record.md",
hooks/lib/fields.py:127:# grammar table in `docs/the-review-record.md` gave its label before #1198,
tests/evals/test_replay_targets.py:483:        doc = held["docs/the-review-record.md"]
tests/evals/test_replay_targets.py:487:        put("docs/the-review-record.md", doc.replace(row, ""))
tests/evals/test_replay_targets.py:494:        put("docs/the-review-record.md", doc)
tests/evals/test_seed_defects.py:106:        if rel == "docs/the-review-record.md":
tests/skills/test_chain_check.py:4237:        table from `docs/the-review-record.md` at import, which raised
```

**A departure from S8: those nine lines stay.** Each one names the path at
an earlier commit, where the file still stands. `replay_targets.py` and its
two test modules build the tree of the last labelled release, 0.22.0, and
read the grammar that release's `docs/the-review-record.md` holds. Line 24
uses the `v0.22.0:` form. `fields.py:127` and `test_chain_check.py:4237`
describe the check before #1198. Re-pointing them would name a file that
never existed at the commit they describe, and the replay would miss the
grammar it reads. Judged against D7, whose list is of citations of what
moves, and `skills/core/SKILL.md` *The rule a mechanism is kept against*:
history goes to git, and these lines read it there. Contract rule 12 asks
for each place that states a moved rule. None of the nine states a rule in
force.

**A decision: the vacated-paths census holds S8 after this phase.**
`tests/censuses.py` gained `POLICY_GROUPS` and one `VACATING` entry per
group, `("docs/<group>/", "docs/")`, in 7f5690b2b. After that, a living
line that spells a moved document's old top-level path is flagged. Before
re-pointing, the census flagged 93 lines (executed). Its grounds are its own
purpose: it was written for #1060's move of a directory one level down, and
this is the same move. `.test_durations` and records are outside the census,
so their keys were re-pointed through the grep above.

**A decision: a test that pinned co-location lost that assertion.**
`tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py`
*stamp_section* asserted that *The guarantee* stands before *The stamp* in
one file. D3 puts them in two documents, so 29d8ca6a4 removed the assertion
and the docstring says they stand apart since #1312. The frame's
`## Removes` row for `docs/the-review-record.md` as one document covers it.

**A decision: one README link drops `./`.** README.md and README.ko.md
list the three decision-table documents as links on one line each. The
link `[docs/running/the-review-and-parity-arms.md](./docs/running/...)` is
92 columns, and `tests/behaviour/test_docs_line_wrap.py` holds 88. A link
destination cannot break, and the line holds no URL the case skips. 7a7860cf7
writes that one destination without `./`, which resolves to the same file,
and moves the ` ·` separator to the start of the next line. The line is now
88 columns. The link text is unchanged.

**The index (D3, D9).** `docs/README.md` holds five tables in the order
forms, running, releasing, checks, layout. Each group's reader sentence,
from D3's *Who opens it* cell, stands over its table. Each row keeps the
question it answered, and the new documents' rows take their reader
sentences. The record layout's row lost "and what tells a settle from a
deletion", since that section left it for `docs/checks/the-fold.md`. The
intro says the root is one directory per group and one table per group,
cites `skills/settle/rule-changes.md` *Rule changes*, and cites
`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*
for which kind of work item edits a document directly. The
`docs/experiments/` line stays. `seal fold` at 47533e717 printed "held 23
documents under docs/ to 25000 estimated tokens, 0 past it" and "the index
docs/README.md names every document" (executed).

**The axis sentence (D5's last paragraph).** `skills/implement/SKILL.md`
*Document layout* holds it after the axis paragraph, as its own paragraph:
"Inside the policy root, documents are grouped by who opens them and at
which step, and any party may open any group." The same commit also re-wrapped
the three lines above *The review round records live beside* that name
`docs/layout/the-record-layout.md`. With the longer path the line would have
been 82 columns, under the limit, so this re-wrap was not needed. It changes
no word.

**Phase 2's open item is closed.**
`tests/github/test_release_report.py::Test_module::test_the_table_reads_this_tree_against_the_last_tag`
listed `docs/` with `os.listdir`. Once the root was grouped, that listed
`docs/README.md` alone. 2e7a946c9 adds each document of the five groups,
read from `tests/censuses.py#POLICY_GROUPS`. `seal mutate` replaced
`for group in named` with `for group in ()` in `fold_check.py`. The case
went red on `forms/the-reader-registry.md`, and the file was restored
(executed).

**`ls seal/threads` at 47533e717 (executed, D9).**

```
1793661729-each-document-is-cut-by-who-opens-it
```

No other design is unsettled, so this phase re-pointed no other design's
operation.

**The narrow run.** Before 47533e717, the test modules that read `docs/`
paths, the policy-root readers and the census were run as one command,
`bin/test -q --no-header $(cat mods.txt)`. `mods.txt` holds 110 modules,
picked by `git grep -l -E 'docs/|"docs"|policy_root|policy_documents|fold_check|rules\.py|RULE_FILES|ls-files|running|layout'`
over `tests/`. It exited 0 with 5194 passed and 14 skipped (executed). The
first run after the cut had 32 failures. Each was a reader of moved text,
seen red before its re-point. `seal layout --check tests` printed "150 files
read, 0 refused" (executed). `uvx ruff check` and `uvx ruff format --check`
over every changed Python file passed (executed).
