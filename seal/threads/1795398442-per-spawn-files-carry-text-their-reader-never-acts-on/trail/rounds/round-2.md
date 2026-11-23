# Review round 2: 1795398442-per-spawn-files-carry-text-their-reader-never-acts-on

```seal
target: 2669e43d4895719e1d565b8476c29bf40cf0cf2c, fixes ea06fdea8..2669e43d4895719e1d565b8476c29bf40cf0cf2c
```

This is a verifying round. Its code is the fix diff from round 1's record
(`ea06fdea8`) to the target: `eabe234b6`, `fe39a9f8d`, `9527f4bea`,
`b04c3ce1c`, `8d1343efa`, the close blocks at `de993b8a1`, the fold at
`718b58e49`, and the merge of `origin/release/v0.38.6` (`f2a664eb8`) at
the target. The merge was read where it meets this work's files, which
answers the row of round 1's `## Not judged` on it. `seal/parity.json` is
not declared, so no parity comparison was owed. The work item's records
were each read whole at the target: `routing.md`, the three frame files,
`gaps.md`, `changelog.md`, `pr.md` and the three phase records. No
`pr.<lang>.md` stands, and `seal/config.json` names English for both
language keys, so none is owed.

Carried from round 1, and not established again: the preload figures and
byte counts of `trail/phases/phase-3.md`, the twenty-one G21 searches, and
the reading of each citation of the kept heading. Each carries because its
files did not change. `git diff --stat 236d3c5e6 HEAD` over `agents`,
`skills/core`, `skills/agent-contract`, `skills/implement/SKILL.md`,
`skills/code-review/SKILL.md`, `skills/code-review/orchestration.md` and
`skills/code-review/gate-to-pull-request.md` prints nothing (executed). So
the measured files at the target are the ones phase 3 measured, and
*Scope* item 12 owes no new measurement. The fix pass returned the new
file to its bytes at `236d3c5e6`, 15,665.

## Findings

### 1. The plan keeps the row that answered the paste check by rewording, beside the row that reverses it

```seal
severity: should
location: `seal/threads/1795398442-per-spawn-files-carry-text-their-reader-never-acts-on/frame/plan.md:59-61`
evidence: read `seal/threads/1795398442-per-spawn-files-carry-text-their-reader-never-acts-on/frame/plan.md:59-61`, `skills/implement/orchestration.md:120-124`, `skills/agent-contract/SKILL.md:193-200`; executed `git diff ea06fdea8 718b58e49 -- seal/threads/1795398442-per-spawn-files-carry-text-their-reader-never-acts-on/frame/plan.md`, `git show --stat 718b58e49`, `wc -c skills/code-review/gate-to-pull-request.md`
reopens: round-1#1
```

Why the close does not hold: round 1's finding 1 named
`frame/plan.md:60` among its locations. It said the pass owed "the plan
row at `frame/plan.md:60`, rewritten to record that the check was fixed".
The close answered that the plan row "of the earlier answer" was the
orchestrator's to fold. The orchestrator added a new row at `eabe234b6`
that opens "The row on the paste check is reversed" (`plan.md:59`). The
fold at `718b58e49` changed `frame/design.md` and left the plan as it was
(executed: `git show --stat 718b58e49`). So the old row still stands at
`plan.md:61`. The rest of the close holds. The code fix, the new case, the
design's *Scope* item 4, the `gaps.md` row and the docstrings are all
right at the target; see `## Probes` and the prose under
`## Confirmations`.

Why it matters: `plan.md:61` still says the refusal "is answered by
ordering the moved sentence's citation differently (e96d743c3), not by
changing `skills/settle/scripts/passages.py#words`". It also says "the new
file grows by 18 bytes, to 15,683". At the target the normaliser is
changed, and the new file holds 15,665 bytes (executed: `wc -c`). Two
parties read this table. The sealer reads it for the orchestrator's
grounds, and `seal settle`'s dry run prints each row for the settling
session to weigh (`docs/running/the-run.md:54`). Both would read two
judgments of one decision, and the older one states the present wrongly.
Contract rule 19 says a correction written beside the sentence it corrects
leaves both for the next reader to choose between. When the framer rejects
a decision, `skills/implement/orchestration.md:120-124` has the
orchestrator rewrite its own row to record that. That is one row holding
the first answer and its reversal.

The fix replaces rows `:59` and `:61` with the one row below. It keeps the
first answer as history inside the row, and it drops the byte figure. No
other record cites either row by its words (executed: `git grep -n -F
'paste check'` over the work item outside `trail/rounds/`). The title row
at `:60` is finding 2's.

```markdown
| 2026-11-23 | The paste check's refusal at phase 3, a 15-word run shared by the moved repair sentence and *Orchestrator: the run ends with a verifying round*, is answered in `skills/settle/scripts/passages.py#words`, which folds the italic row name a section citation carries into the citation's one token, and the moved sentence keeps the words it had at `236d3c5e6`. The first answer, ordering the sentence's citation differently at `e96d743c3` and leaving the normaliser unchanged, was reversed after round 1's finding 1 | The two clauses cite the same core row in the form `tests/text/test_the_rules_have_one_owner.py#THE_CORES_ROW` requires and say different things, so the run is the link's words, not a pasted fact. Round 1's finding 1 showed the refusal is the normaliser's: the link stands in five rule documents, so the next pair meets the same refusal, and reordering the words kept the defect and hid it. The fix pass wrote the normaliser's case, seen red, and re-read `chain_check.py`'s use of the same reader | `skills/core/SKILL.md` *The rule a mechanism is kept against*, the sentence opening **Do not avoid the change a problem calls for**; `skills/agent-contract/SKILL.md` rule 18 |
```

```seal
verdict: fixed c5215301b
answer: The orchestrator merged the two rows into the round's paste-ready row: one row of `frame/plan.md` *Judgments of the run* states the answer in `passages.py#words` and that the first answer, reordering the sentence at `e96d743c3`, was reversed after round 1's finding 1. The wrong byte count went with the old row. The fix touches the work item's records alone, so the sealer reads it.
```

### 2. The title row says no behaviour is fixed, and the fix pass fixed the paste check's normaliser

```seal
severity: should
location: `seal/threads/1795398442-per-spawn-files-carry-text-their-reader-never-acts-on/frame/plan.md:60`, `seal/threads/1795398442-per-spawn-files-carry-text-their-reader-never-acts-on/pr.md:1`
evidence: read `seal/threads/1795398442-per-spawn-files-carry-text-their-reader-never-acts-on/frame/plan.md:60`, `skills/commit-pr-convention/SKILL.md:126-145`, `skills/commit-pr-convention/SKILL.md:169-172`, `skills/settle/scripts/passages.py:38-44`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py:17-25`; executed `git log --format='%h %s' ea06fdea8..HEAD --no-merges`
regression: round-1#1
```

The unit is `skills/settle/scripts/passages.py#SECTION`, which
`fe39a9f8d` changed. The frame's row on the title (`frame/plan.md:60`,
written at `1486c223e` before round 1) says "No behaviour is added or
fixed". The fix pass then changed what the paste check and
`chain_check.py`'s copy notice decide, and the defect is that the row
still states the old premise. Round 1's finding asked for the check to be
fixed and said nothing on the title, so the fix itself is sound. The
contradiction came from a judgment nobody re-read after it.

Why it matters: at the target, `passages.py#SECTION` changes what two
readers decide. One is the paste check,
`tests/text/test_no_passage_is_pasted_into_a_second_file.py`. The other is
`chain_check.py`'s notice, which a proofer in a user's repository meets
when a design's `to` carries a link to one row. Before the change both
counted two correct links to one row as a pasted passage. That went
against the method the paste check's docstring stated at the base: a link
shares its heading's words by design. The fix pass's own commit takes
`fix:` (`fe39a9f8d`). `skills/commit-pr-convention/SKILL.md:131` defines
`fix:` as "behaviour that was wrong against a rule the tree stated before
the change, now matching it". `:139-140` gives a change that does more
than one kind the prefix highest in the table, and `fix:` stands above
`refactor:`. The orchestrator titles the pull request from this row, and
`pr.md:1` quotes it. The sealer reads the grounds against the diff at step
4 and would name the disagreement then, after the broad run. A title fixed
then costs a later act.

The fix rewrites the row and the `pr.md` quote. Where the orchestrator
judges that `refactor:` stays, the row still has to drop "No behaviour is
added or fixed". It also has to say why the normaliser's fix does not
raise the prefix, and the highest-row rule leaves little room for that.
Under `fix:`, the orchestrator also retitles issue #1579 when it titles the
pull request (`skills/commit-pr-convention/SKILL.md:169-172`).

```markdown
| 2026-11-23 | The pull request's title takes `fix:` | Most of the change moves passages to the file whose reader acts on them, which alone is `refactor:`: every agent and the orchestrator follow the same rules, and every preload row of the release table falls. The change also fixes `skills/settle/scripts/passages.py#words`, which the paste check and `chain_check.py`'s copy notice read through. Both counted two correct links to one row of a section as a pasted passage, against the method `tests/text/test_no_passage_is_pasted_into_a_second_file.py` states, that a link shares its heading's words by design. A change that does more than one kind takes the prefix highest in the table, and `fix:` stands above `refactor:`. No `feat:` is added, so the release stays a patch | `skills/commit-pr-convention/SKILL.md` *Commit messages*, the table and the paragraph opening **Where a change does more than one of these**; `docs/releasing/branch-and-release.md` *The version is named at the cut, a `feat:` ships in the planned minor whose goal it shares, and the prefix is never lowered to fit the number* |
```

```markdown
- "The pull request's title takes `fix:`" (`frame/plan.md` *Judgments of the run*, the row on the title's prefix)
```

```seal
verdict: fixed c5215301b
answer: The orchestrator replaced the row on the title's prefix with the round's paste-ready row, which takes `fix:` for the normaliser fix, and `pr.md`'s quote with the round's line. The pull request's title takes `fix:`; the issue's title stays, as a title the pull request closes. The fix touches the work item's records alone, so the sealer reads it.
```

### 3. The changelog counts 38 designs where the tree holds 35 at the fix and 36 at the target

```seal
severity: should
location: `seal/threads/1795398442-per-spawn-files-carry-text-their-reader-never-acts-on/changelog.md:9`
evidence: executed `git ls-tree -r --name-only <rev> -- seal/threads` counted for `/frame/design.md` at `fe39a9f8d`, `718b58e49`, `f2a664eb8` and HEAD; `python3 <scratchpad>/1795398442-per-spawn-files-carry-text-their-reader-never-acts-on/round-2/test_tmp_round2_fold.py <clone>`
regression: round-1#1
```

The unit is the changelog entry opening **The paste check reads a link to
one row of a section as one token**, which `fe39a9f8d` added. Round 1's
finding 1 asked the pass to re-read `chain_check.py`'s use of the reader.
The pass did, and wrote the result into the fragment with a count it did
not hold. The close claimed "A probe over the 38 designs under
`seal/threads/`". The tree held 35 designs at `fe39a9f8d` and at
`718b58e49`, and holds 36 at the target, where the merge added
`1795390621` (executed).

Why it matters: the fragment is the text of the release note. Its last
sentence says "Over the 38 work items' designs in the tree, that notice
says the same before and after the change." The count is wrong at every
commit of the branch. "In the tree" names no commit, and at the release
the tree holds other designs. The finding the sentence reports does hold.
This round's probe read all 36 designs at the target and found zero copy
notices under either pattern, and 159 with the old pattern at a window of
4 as a control (`## Probes`). The fix names the commit and the count that
were read.

```markdown
Over the 36 work items' designs the tree held at `2669e43d4`, that notice says the same before and after the change.
```

```seal
verdict: fixed c5215301b
answer: The orchestrator replaced `changelog.md`'s sentence with the round's paste-ready one, which counts the 36 designs at `2669e43d4`. The fix touches the work item's records alone, so the sealer reads it.
```

## Confirmations

```seal
confirms: round-1#2
```
What holds: `docs/layout/the-record-layout.md:52` names
`skills/code-review/gate-to-pull-request.md` among the files whose change
owes a process row, with six more. The class was listed again by
enumeration. Every tracked `skills/*.md` other than a `SKILL.md` or an
`orchestration.md` was read at its opening, and the commit that added each
was listed with the files it cut (executed: `git ls-files`, then `git log
--diff-filter=A` for each `skills/implement/` file). The seven named files
each hold steps cut from `agents/*.md` or an `orchestration.md`. The six
others (`skills/settle/draft.md`, `local-mode.md`, `named-directories.md`
and `rule-changes.md`, `skills/verify/seal-mutate.md` and
`skills/writing-style/outside-the-review.md`) each open from a `SKILL.md`,
which the list does not name. The sentence is the one statement of the
trigger. `git grep` on its bold lead and on `bootstrap.md` finds no other
list (executed). No Korean edition of the document stands. `changelog.md`
carries the entry and its `### Process changes` row.

```seal
confirms: round-1#3
```
What holds: `changelog.md:4` now names one changed sentence, row 6 of the
`seal pr-wait` exit table. A whitespace-folded comparison read the 19
paragraphs of the old section at `3c89a70d5` against both files at the
target (executed). Two did not stand whole: the section's first paragraph,
which the cut splits at "committed and unpushed.", and the exit table. The
exit-1 sentence on reviewing a repair stands with its old words, since
`git diff 236d3c5e6 HEAD -- skills/code-review/gate-to-pull-request.md`
prints nothing (executed).

What matched: round 1's finding 1 is reopened above for the plan row
alone, and the rest of its close holds at the target. `passages.py#SECTION`
takes the optional `*<name>* of ` prefix the finding gave. The probe found
nine places in the corpus where the prefix folds text the old pattern left
as words. All nine are the core-row link "*No fix that no round reads* of
`skills/core/SKILL.md` *Judgment is not licence to skip a party*", in
`docs/checks/the-pull-request-check.md`, `docs/running/the-run.md`, both
orchestration files and the new file (executed). So the fold reaches no
other text in the tree as it stands. The two assertions of the new case
were run under both patterns. Under the old pattern, the two links share
a run, which is the claimed red. Under the new pattern they share none,
and the bare italic phrase still does (executed). The paste check passes
at the target (executed, in the narrow run). `frame/design.md` *Scope*
item 4 and the `gaps.md` row at `:9` state what the target does (read).
The `## Not done` paragraph that `fe39a9f8d` removed recorded a decision
that was later reversed. It is not a `## Not verified` row, which would
have to close with the word `closed`
(`skills/implement/SKILL.md` *4. The closing memo — only what the diff
cannot show*).

What matched: the new case,
`tests/skills/test_passages.py#Test_words::test_accepts_a_row_a_section_citation_names_as_part_of_its_token`,
was read against its group, the other `Test_words` cases. Only it holds the
row-name prefix and the bound that an italic phrase with no `of <path>`
after it stays words. Only the tree-wide paste case also reads the
prefix, and it reads the tree, not the rule.

What matched: the merge at the target keeps this work's edits where
#1577's diff touched the same files. The comments at
`skills/verify/scripts/broad_gate.py:477` and `:2058` cite
`skills/code-review/gate-to-pull-request.md` (read).
`tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py:34`
reads the new file, and the comment of
`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:224` names it
(read). #1577 added no citation of a moved step. Its one citation of the
kept heading, `templates/setup/config.md:175`, cites it for what `pr.md`
holds, which stayed (executed: `git grep` over the merged files). The
moved paragraph *A refusal about the `Broad gate` key*
(`gate-to-pull-request.md:222-231`) still matches #1577's rewrite of the
refused forms in `skills/config/SKILL.md`, because it names no form (read).
The design #1577 added, `1795390621`, names `docs/running/the-broad-gate.md`
*What the gate runs* and no section this work edits, so `frame/design.md`
`## Rule changes` still holds at the target (executed).

What matched: `pr.md`'s three quotes stand word for word at their
coordinates (read). Finding 2 changes the first of them.

What matched: `chain_check.py` run over the branch worktree before this
record was written printed no notice at a line of a `frame/design.md`
(executed).

The narrow run passed: 712 cases over eleven modules, the paste reader,
the paste check, the moved-rule margin, the rule-change reader, the
broad-gate modules #1577 changed, the wrap, the citation resolver, the
owner cases and the sealer cases (executed, `bin/test -q` in a clone at
the target). The suite stays `unverified`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the target: the full suite, the repository-wide lint and the format check. This round ran only the narrow modules above, and the suite is `unverified` | `seal/config.json` `Broad gate` | the orchestrator, at the broad run after the rounds settle |
| Q1: the release table on the release pull request, after the release's other items merge | `seal/threads/1795398442-per-spawn-files-carry-text-their-reader-never-acts-on/frame/questions.md:16` | whoever prepares the release |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over `tests/skills/test_passages.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/text/test_a_moved_rule_leaves_its_definition.py`, `tests/skills/test_rule_changes.py`, `tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py`, `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`, `tests/skills/test_broad_gate.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/text/test_the_rules_have_one_owner.py`, `tests/behaviour/test_the_sealer_guarantees.py`, in a `git clone --no-local` at the target | 712 passed, 1 skipped, 5 warnings; exit 0 |
| `python3 test_tmp_round2_fold.py <clone>`, run once from the round's scratch directory | 36 designs; copy notices from `chain_check.py#rule_changes_read`: 0 under the new pattern, 0 under the old, the same set; 159 under the old pattern at a window of 4, the control; 9 prefix folds in the corpus, each the core-row link; the new case's links share a run under the old pattern and none under the new, and the bare italic phrase shares one under both |
| `git ls-tree -r --name-only <rev> -- seal/threads`, counting `/frame/design.md` | 35 at `fe39a9f8d`, 35 at `718b58e49`, 35 at `f2a664eb8`, 36 at the target |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.38.6 --root <branch worktree> --worktree`, from the clone, before this record was written | exit 0; no notice at a line of `frame/design.md`; round 1's findings 1 and 2 named as owing a verifying round, and the absent `trail/gate.md` and `guarantee.md`, which come later |
| the same command after this record was written | exit 0; the record's refusals are its three findings, open for having no close block; the other lines name the absent `trail/gate.md` and `guarantee.md` |
