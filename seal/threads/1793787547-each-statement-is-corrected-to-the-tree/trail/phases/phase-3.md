# Phase 3: 1793787547-each-statement-is-corrected-to-the-tree

## What this phase found

**The frame holds for this phase, with two counts that differ.** I checked
it against the tree at `8bb802586` before the first edit (read, unless
marked).

- Phases 1 and 2 changed no file S4 or S5 names (executed: `git diff --stat
  a3e08d64a 8bb802586 -- tests/` lists only
  `test_the_pull_request_language_is_the_repositorys.py` and
  `test_no_case_tells_the_agent_it_is_evaluated.py`).
- Each statement S4 and S5 list stood at its coordinate. Two of them sit a
  line or two from where the design puts them: S5.2 at
  `test_a_shrunken_corpus_declines_to_judge.py:38`, and S5.3's paragraph at
  `:197-205`, with the catch at `:210-211`.
- Every module and case the statements cite is absent at HEAD. I traced
  each one to the commit that removed it (executed: `git log
  --diff-filter=D` or `git log -S`). `test_the_fixes_name_their_surface.py`
  and the case `test_the_documents_that_instruct_never_name_the_old_directory`
  left at 8350c5788 (#923).
  `test_a_corrected_sentence_survives_elsewhere.py`,
  `test_the_lenient_run_says_what_the_broad_gate_will_say.py` and
  `test_the_ledger_rules_have_one_home.py` left at 5b1f6faea (#944).
  `test_commit_review_gate.py` left at 61a8455aa (#1027).
  `test_the_closer_carries_on_past_a_refusal.py` left at de11df757 (#1088),
  and its docstring there says it held no case.
  `test_the_core_names_where_the_routing_question_is` left at ea220c9cd (#1314).
- The SyntaxWarning probe holds. I re-ran it as a `test_tmp_*` file in the
  scratch directory. Under Python 3.12.11, 3.13.9 and 3.14.3 it gave 155
  modules and no warning, and I deleted the file after the run (executed).
  `bin/test`, `.github/workflows/test.yml`, `.github/scripts/run_tests.py`
  and `tests/conftest.py` set no `filterwarnings`, no `-W` and no
  `PYTHONWARNINGS` (executed: `git grep`). The repository has no
  `pyproject.toml` and no `pytest.ini`.
- **Census 1 lists 48 lines, not the design's 51.** I ran the method the
  design describes, as the command in *The two censuses* below. It gives
  48 lines at `a3e08d64a` and 48 at `8bb802586` (executed). The design does
  not spell out its command, so I cannot say where the other three came
  from. Each of the 48 was read.
- **Census 2 lists 9 lines, not the design's 7.** The two extra lines are
  `tests/test_censuses.py:11` and `:15`. Each names a removed module, such
  as `test_no_living_file_writes_the_section_sign.py`, whose basename is
  also the name of a removed case. Both stand in "The cases came from …",
  which names its moment. The design's count probably left out a token
  that `.py` follows.

**S4: the module docstring's words.** I judged the docstring against the
module's own cases, `RULES`, `CARRIERS` and `LINKED`. Every sentence now
says what those cases hold, or tells the history in the past tense.

- The first line reads "The rules `CLAUDE.md` once named have one home
  each, and no other file restates them (#730)." The module keeps its
  name (`frame/plan.md` *Alternatives considered* A9).
- The sentence "`CLAUDE.md` keeps a row …" became the past tense. A new
  paragraph says the rows left with #940, #1169 and #1177, as the comment
  above `LINKED` says, and that `CLAUDE.md` keeps none of them. I wrote
  "keeps none of them" rather than "names none of the homes", because
  `CLAUDE.md` does name `CONTRIBUTING.md`, the identifiers rule's home,
  for another section (read).
- A new paragraph states what the three cases hold. Its sentence on where
  `CARRIERS` comes from now says the list "started as" the files the
  `67694cba` spec names. The old wording said the carriers *are* those
  files. `CARRIERS` holds `skills/core/SKILL.md`, which 334189fdb created
  after 67694cba3 (executed: `git log --diff-filter=A`, `git merge-base
  --is-ancestor`), so that wording did not hold the whole list.
- *What this does not hold* is now said of a carrier's own words, as S4
  asks. I dropped "That is spec D2's stated cost". D2 in that spec is the
  shape of a `CLAUDE.md` link row (read: `git show 67694cba:…/spec.md`), so
  the attribution went with the row.
- The paragraph on `tests/test_the_ledger_rules_have_one_home.py` went
  (`frame/design.md` *Removes*).

The comment above `LINKED` is code, not the docstring, and A4 has `git
diff` touch the docstring alone. I left it. Its sentence "`CLAUDE.md` is
loaded into every session" still holds at HEAD, and the rest of the
comment tells the history in the past tense.

**S5: the choice per statement.** Grounds: `frame/design.md` *Scope* S5
and `frame/questions.md`'s assumption. Every commit cited here is a parent
of a removal commit, an ancestor of `origin/main`, and holds the cited
file (executed: `git merge-base --is-ancestor`, `git cat-file -e`).

1. `test_a_phase_hands_the_next_one_a_record.py:30-31`: **dropped**. What
   the sentence needs is that the check reads through the same `readable`
   `chain_check.py` loads. That stands at HEAD (read:
   `chain_check.py:144`, `unverified_check.py#readable`). The mirrored
   case adds nothing a reader can use. It left with #923, together with
   the round record it read.
2. `test_a_shrunken_corpus_declines_to_judge.py:37-39`: **cited at a
   commit**,
   `f975ea66a:tests/test_a_corrected_sentence_survives_elsewhere.py#_derives_a_path_list`,
   "the last commit that held it". The comment goes on to say "both were
   bought by that module's own round 1", which needs the module to be
   readable.
3. `derivers`: **removed**, as *Removes* names. The paragraph, the
   `warnings.catch_warnings` block and `import warnings` went. Nothing
   else in the module used the import, and the `ruff` hook removed it on
   save.
4. `test_first_setup_asks_once.py:6-8`: **re-pointed** from
   `tests/test_commit_review_gate.py` to
   `tests/hooks/test_routing_edit_gate.py`. #1027 moved the routing check
   from the commit gate to the edit tools, and that module pins the edit
   gate resolving the root, both shared and local (read: `:307-314`,
   `:375-377`, and `home_at` monkeypatched at `:189`).
5. and 6. `test_the_gate_asks_the_range_ci_will_ask.py:38-40` and
   `:174-175`: **cited at a commit**,
   `f975ea66a:tests/test_the_lenient_run_says_what_the_broad_gate_will_say.py`.
   Its structural half and
   `test_no_document_describes_the_lenient_reader_alone` stand there
   (executed: `git show … | grep -n`). The first citation no longer
   splits the name across two lines.
7. `test_the_set_a_work_item_always_has.py:153-154`: **cited at a
   commit**. The case stands in
   `cdfdfedd8:tests/test_handoff_outlives_the_merge.py` (executed).
   `tests/behaviour/test_no_document_names_the_old_roots.py` holds a
   neighbouring rule, but it has an allowlist and the precedent has
   none, so I did not re-point to it.
8. `tests/github/test_close_issues_on_release.py:44-48`: **re-pointed**.
   "placed these cases from" still names all three source modules,
   because it names its moment. The present-tense "keep the cases that
   read …" now names only the two the tree holds, as "the first and the
   last".
9. `tests/hooks/test_question_gate.py:363-364`: **dropped**. The commit
   gate and its case left with #1027. The docstring now states the
   induced raise itself: `os.path.relpath` raising, as it does for a
   root on another drive.
10. `tests/text/test_review_axes.py:105-107`: **dropped**, along with the
    clause it held up. "The core … names this section" does not hold at
    HEAD: `skills/core/SKILL.md` names neither *Orchestrator: how the work
    is routed* nor "routing question" (executed: `git grep`). The case's
    own body at `ea220c9cd~1` shows that the core once did. So that
    clause is a statement HEAD contradicts, and it went with the
    citation.
11. `tests/text/test_the_verifying_round_is_bounded_not_cheapest.py:15-17`:
    **dropped**. The sentence already states the pair it holds, a phrase
    the new wording uses and the absence of the old sentence.

**The two censuses, as run at `bb9a21e77`.** `$S` is the session's
scratch directory.

Census 1, removed modules:

```
git log --diff-filter=D --name-only --format= -- 'tests/*.py' | sed 's#.*/##' | sort -u > $S/removed_modules
git ls-files 'tests/*.py' | sed 's#.*/##' | sort -u > $S/present_modules
comm -23 $S/removed_modules $S/present_modules > $S/gone_modules      # 131 names
while read n; do git grep -n -F "${n:0:28}" -- 'tests/*.py'; done < $S/gone_modules | sort -u
```

Census 2, removed cases, is `python3 $S/census2.py <repo>`. The script
collects every `def test_*` that a `-` line of `git log -p --format= --
'tests/*.py'` shows: 6,594 names. It removes each name that a tracked
`tests/*.py` defines, which leaves 5,691. Then it joins each line that
ends in `_` to the next line's text, past that line's indent and an
optional `#`. It lists each `test_\w+` token of the joined text that is
one of the 5,691 names.

At `8bb802586` census 1 listed 48 lines and census 2 listed 9 (executed).
At `bb9a21e77` census 1 lists 42 and census 2 lists 6 (executed). I read
each one:

- In census 1, four lines are this phase's citations at a commit:
  `test_a_shrunken_corpus_declines_to_judge.py:37`,
  `test_the_gate_asks_the_range_ci_will_ask.py:39` and `:176`, and
  `test_the_set_a_work_item_always_has.py:155`.
- Census 1 lists six case names that start with
  `test_a_script_copied_alone_e`, the 28-character prefix of a removed
  module's basename. They are in `test_chain_check.py:4174`,
  `test_core_check.py:486`, `test_fold_check.py:431`,
  `test_payload_meter.py:1298`, `test_seal.py:507` and
  `test_settle.py:3286`, and each is a case the tree defines.
- Every other line of census 1 names the moment it describes: "The cases
  come from", "placed these cases from", "came from", "The cases came
  from", or "which held no other case and went". Two lines are
  `test_close_issues_on_release.py:46` after item 8 and
  `test_session_cost.py:4878`, "from `tests/test_session_cost_post.py`".
- In census 2, `test_the_set_a_work_item_always_has.py:154` is item 7's
  citation at a commit. The `test_censuses.py` lines are the two module
  names above. The other three are the ones the design counts as holding:
  "at `release/v0.16.0`", "inverted from" and "Renamed and rewritten
  from".

This list is whole for the names the method spells, which are a removed
module's basename or its first 28 characters, and a removed case's name.
It is not whole for two kinds of citation:

- A citation of a moved module by its old path. The basename still
  stands, so census 1 drops the name.
- A citation that describes a removed thing without naming it.

The paragraph below names one class of the second kind that I found.

**A neighbouring class, named and not corrected.** While reading census
1's lines, I found `tests/hooks/test_routing.py:4` and `:7`. They say a
declaration "is what the commit gate reads", and "What the commit gate does
with an answer is its own file's". The commit gate left with #1027. These
sentences describe a removed hook as standing. They do not cite a removed
test module or case, which is #1344's class. `git grep -n -i "commit gate"
-- tests` lists 18 lines in 8 modules (executed). Three of them say the
gate is gone: `tests/hooks/test_gate.py:6`,
`tests/text/test_edits_go_through_the_edit_tool.py:17` and
`tests/text/test_the_direct_answer_owes_the_sealers_record.py:20`. I did
not classify the other fifteen: `tests/conftest.py:1716`,
`tests/hooks/test_cmdline.py:5`, `tests/hooks/test_optin.py:82`,
`tests/hooks/test_question_gate.py:203`, `tests/hooks/test_routing.py:4`,
`:7`, `:62`, `:111`, `:265`, `:416`, `:535` and `:557`,
`tests/text/test_edits_go_through_the_edit_tool.py:16` and `:51`, and
`tests/text/test_the_direct_answer_owes_the_sealers_record.py:9`.
Correcting them is outside S5's scope and outside `frame/plan.md` row 3.
`gaps.md` *Not done* records it, and the hand-back names it for the
orchestrator.

**Other places that state what this phase reworded, a sample.** None of
the corrected sentences carries a `check:` line. `git grep -n` outside
`seal/threads/` finds no other text that names any of these:
`test_the_ledger_rules_have_one_home`, `test_the_fixes_name_their_surface`,
`test_commit_review_gate`, `test_the_core_names_where_the_routing_question_is`,
`test_the_broad_gate_cell_keeps_every_run`, or a `CLAUDE.md` "keeps a row"
(executed). `docs/layout/the-record-layout.md:188` names the S4 module in
its `check:` line, and the module keeps its name, so that line holds.

**Seen red and mutation.** No case was written new, so contract rule 15
has nothing to show red. Every change is the *A comment or docstring
inside source* row of `skills/verify/SKILL.md` *The narrow command still
has to be able to fail*. The one exception is `derivers`, where a guard
that caught nothing went. The change adds no behaviour, so no `seal
mutate` run is owed. I still ran one at `bb9a21e77`, to show that the
citations at a commit are read. It put `cdfdfedd0` for `cdfdfedd8` in
`test_the_set_a_work_item_always_has.py` and ran
`tests/text/test_a_cited_commit_outlives_the_squash.py`. Verdict `red`:
`test_every_cited_commit_outlives_the_squash` failed on ":155 cites
cdfdfedd0", and the tree was clean after the restore (executed).

**Narrow run.** I ran the ten changed modules with
`test_a_cited_commit_outlives_the_squash.py` and
`test_a_cited_section_stands_in_its_file.py` in one `bin/test … -q` over
the tree `bb9a21e77` commits, before the commit: 222 passed (executed,
exit 0). `uvx ruff check` and `uvx ruff format --check` on the ten files
exited 0 (executed).

**Phase boundary run.** This is the *Phase boundary* row of
`skills/verify/SKILL.md` *Scope: cheap and often, broad and once*, run as
one `bin/test … -q` over 39 modules. The lists below came from `git grep
-l` over `tests/*.py` (executed):

- the ten modules the plan row names
- the modules that name one of them
- the modules that walk every tracked file or every `*.py` file
- `tests/test_censuses.py` and
  `tests/text/test_a_cited_commit_outlives_the_squash.py`, which read the
  text of tracked files across the tree, and
  `tests/text/test_no_passage_is_pasted_into_a_second_file.py` and
  `tests/text/test_a_moved_rule_leaves_its_definition.py`, which I added
  without checking what they read. The first of those two reads only
  `*.md` (read: its `corpus`)
- the four modules that read this work item's records

It ran over `bb9a21e77`, with this record, the `gaps.md` rows and the
Status cell in the working tree: 1984 passed and 9 skipped (executed, exit
0). The selection is my reading of "a module that reads a path the phase
changed". A module that reads those files
through a helper these searches do not name is outside it, and the broad
run covers that.
