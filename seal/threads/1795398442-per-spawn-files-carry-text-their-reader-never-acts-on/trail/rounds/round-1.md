# Review round 1: 1795398442-per-spawn-files-carry-text-their-reader-never-acts-on

```seal
target: 1486c223e5e2cfd2672d039a64713104a5f0a4b5 against origin/release/v0.38.6
```

The branch was read against `3c89a70d5`, where it was cut from
`origin/release/v0.38.6` and which is still its merge base. The base has
since moved to `f2a664eb8`, and the branch has not merged it. This is the
first round, so no coordinate or verdict was carried from an earlier one;
every fact below was established here. `seal/parity.json` is not declared,
so no parity comparison was owed. The work item's records were each read
whole at the target: `routing.md`, the three frame files, `gaps.md`,
`changelog.md`, `pr.md` and the three phase records. No `pr.<lang>.md`
stands, and `seal/config.json` names English for both language keys, so
none is owed.

The round read every file the diff changes outside the work item's
records. It compared the old pull request section with the kept section
and the new file paragraph by paragraph, with whitespace folded (executed).
It also read the citations of the kept heading and of
`skills/code-review/orchestration.md` by path across the tree outside
`seal/threads/`, each for which paragraph it means (executed). The
orchestrator's rewording at `e96d743c3`, outside any phase, was reviewed
as code.

## Findings

### 1. The paste check's refusal of a correct link was answered by rewording the text, and the check keeps counting a core-row link as a pasted passage

```seal
severity: should
location: `skills/code-review/gate-to-pull-request.md:126-128`, `skills/settle/scripts/passages.py:38-41`, `seal/threads/1795398442-per-spawn-files-carry-text-their-reader-never-acts-on/frame/plan.md:60`, `seal/threads/1795398442-per-spawn-files-carry-text-their-reader-never-acts-on/frame/design.md:40`, `seal/threads/1795398442-per-spawn-files-carry-text-their-reader-never-acts-on/gaps.md:21-35`
evidence: executed `python3 <scratchpad>/1795398442-per-spawn-files-carry-text-their-reader-never-acts-on/round-1/test_tmp_paste_fold.py <clone>`; read `skills/agent-contract/SKILL.md:186-192`, `skills/settle/scripts/passages.py:38-41`, `skills/settle/scripts/passages.py:69-92`, `tests/text/test_the_rules_have_one_owner.py:78-81`, `tests/text/test_the_rules_have_one_owner.py:192-195`, `skills/code-review/orchestration.md:192-207`
```

Why it matters: contract rule 18 (`skills/agent-contract/SKILL.md:186-192`)
says that when a check refuses correct code, you fix the check or report
the refusal, and never bend the code to pass it. The plan's row on the
paste check (`frame/plan.md:60`) concedes that the refused text was
correct. Its grounds say "the run is the link's words, not a pasted fact".
The row then answers the refusal by reordering the moved sentence at
`e96d743c3` (`gate-to-pull-request.md:126-128`), so the two files share no
15-word run. That is the act rule 18 withholds. `gaps.md:28-30` says the
same rule "forbids rewording it to pass", and `gaps.md:33-35` then records
the rewording, so the memo contradicts itself.

The cost reaches past this work item. `skills/settle/scripts/passages.py:40`
folds a `.md` path and its italic section into one token, but not the
italic row name before it. So the link form
`tests/text/test_the_rules_have_one_owner.py:78-81` requires,
"the row *No fix that no round reads* of `skills/core/SKILL.md` *Judgment
is not licence to skip a party*", is ten words to the check. Any five
shared words around it make a refused "copy". Four rule documents already
carry that link (`test_the_rules_have_one_owner.py:192-195`), and this
work adds a fifth. The next pair meets the same refusal. Once the settle
removes this work item's directory, the plan row and `gaps.md` are the
only places that say why, and nothing in the tree says it. The probe (see
`## Probes`) showed the current normaliser refusing the sentence as it
stood at `236d3c5e6`, with one shared run. With the row name folded into
the token, the same pair shares none, in both wordings.

The fix is to the check, in the module `chain_check.py` also reads through
(`skills/settle/scripts/rule_changes.py#copies`). It changes that notice
for a design's `to` too, so the pass owes a case in
`tests/skills/test_passages.py` for the link form, seen red against the
current pattern. Precondition: the pattern runs on the joined lines before
lowercasing, as `words` calls it at `passages.py:91`, so `[^*]` still
crosses a line break.

```python
# A section quoted by name after a `.md` path (with or without its
# possessive), and the italic name of a row or paragraph cited in it
# (`*<name>* of <path> *<section>*`), so a link to one row is one token.
# `[^*]` crosses a line break, so a wrapped name is one name.
SECTION = re.compile(
    r"(?:\*[^*]{1,200}\*\s+of\s+)?`?[\w./-]+\.md`?(?:'s)?\s+\*[^*]{1,200}\*"
)
```

The snippet does not cover the other statements of the decision. The fix
pass also owes them: the plan row at `frame/plan.md:60`, rewritten to
record that the check was fixed; Scope item 4's exception at
`frame/design.md:40`; the second paragraph of `gaps.md` *Not done*; and
the module docstring of `passages.py` where it says what a token is. With
the check fixed, the sentence at `gate-to-pull-request.md:126-128` can
return to its words at `236d3c5e6`, as Scope item 4 asked before the fold,
or keep its new order, whose meaning is the same. Where the orchestrator
judges the check change to be outside this pull request, the close is
`deferred <an issue>` naming the normaliser's defect, so that the defect
outlives the settle.

### 2. The steps moved to the new file leave the list of files whose change owes a process row

```seal
severity: should
location: `docs/layout/the-record-layout.md:51-53`, `skills/code-review/gate-to-pull-request.md`
evidence: executed `git ls-files 'skills/*.md'`, `git grep -n -F 'skills/*/orchestration.md' -- ':!seal/threads'`; read `docs/layout/the-record-layout.md:51-60`
```

Why it matters: `docs/layout/the-record-layout.md:51-53` says that a work
item whose diff changes `skills/core/SKILL.md`, `CLAUDE.md`, an
`agents/*.md` file, a `skills/*/orchestration.md` file or
`skills/implement/bootstrap.md` ends its `changelog.md` with
`### Process changes`. The party that writes the fragment, the last
phase's crafter or the orchestrator, reads that list to decide whether a
row is owed. At the base, the steps from the preflight to the open pull
request stood in `skills/code-review/orchestration.md`, inside that list.
This diff moves them to `skills/code-review/gate-to-pull-request.md`, which
the list does not name. So the next change to how the orchestrator runs the
preflight, the broad run, `seal pr-body`, the sealer's spawn or
`seal pr-wait` owes no process row, and the release note's process table
omits it. #1577 already edits one of the moved paragraphs, *A refusal about
the `Broad gate` key*. The sentence is the only statement of the trigger
(executed: `git grep` on `skills/*/orchestration.md` prints that line
alone).

The class was listed with `git ls-files 'skills/*.md'` minus each
`SKILL.md`. Two other orchestrator files stand outside the list as well:
`skills/implement/routing-question.md` and `skills/implement/merge-order.md`.
Earlier cuts made them, and this diff did not, so the snippet below names
the one file this diff adds. The pass may name the other two as well, or
record them as a home.

```markdown
**A change to the way of working writes its process row in its own
fragment.** A work item whose diff changes `skills/core/SKILL.md`, `CLAUDE.md`, an `agents/*.md` file, a `skills/*/orchestration.md` file, `skills/code-review/gate-to-pull-request.md` or `skills/implement/bootstrap.md` ends its `changelog.md` with the line `### Process changes` and a table in
```

### 3. The changelog says the moved paragraphs kept their words, and two of their sentences changed

```seal
severity: should
location: `seal/threads/1795398442-per-spawn-files-carry-text-their-reader-never-acts-on/changelog.md:4`
evidence: executed a folded paragraph comparison of `git show 3c89a70d5:skills/code-review/orchestration.md` against `skills/code-review/orchestration.md` and `skills/code-review/gate-to-pull-request.md`; read `skills/code-review/gate-to-pull-request.md:46`, `skills/code-review/gate-to-pull-request.md:126-128`
```

Why it matters: `changelog.md:4` says the paragraphs moved "in their order
and with their words". The fragment ships as the release note's text. Two
moved sentences are not the words they had at the base. Row 6 of the
`seal pr-wait` exit table now cites the kept section "for a conflict with
the base" (`gate-to-pull-request.md:46`). The exit-1 sentence on reviewing a
repair was reordered at `e96d743c3` (`gate-to-pull-request.md:126-128`).
The frame states both exceptions (`frame/design.md:40`), and the fragment
states neither. Where finding 1's fix returns the exit-1 sentence to its old
words, the second exception leaves the sentence below too.

```markdown
The paragraphs it acts on only once the last round record has no finding open moved under *Orchestrator: from the preflight to the open pull request* in the new file, in their order and with their words, but for two sentences: row 6 of the `seal pr-wait` exit table now cites the kept section for a conflict with the base, and the sentence on reviewing a repair orders its citation of the core's row differently.
```

## Confirmations

What matched: every preload row of the release table is negative against
v0.38.5 at the target, with the same figures `trail/phases/phase-3.md`
quotes for `236d3c5e6`: crafter 30,613, framer 37,028, proofer 31,379,
sealer 31,909 and tracer 24,191. Executed from a clone at the target
against a clone at `641b6bfb5`. No preloaded file changed after
`236d3c5e6` (executed: `git diff --stat 236d3c5e6 HEAD -- agents
skills/core skills/agent-contract`). So S1 holds at the work's last code
commit, and `changelog.md`'s preload figures still hold.

What matched: S2 and S3 hold at the target (executed: `wc -c`). The
contract is 11,625 bytes, `skills/implement/SKILL.md` 22,114,
`skills/code-review/SKILL.md` 15,737 and `skills/code-review/orchestration.md`
23,920. The new file is 15,683 bytes, which is the figure the plan's row on
the paste check gives.

What matched: each of the twenty-one G21 searches, `git grep -n -F` with
its pathspec, printed nothing at the target (executed). So S4 holds, and
so do the census lines of S7 and S8.

What matched: every paragraph of the old section
*Orchestrator: the pull request opens once the sealer seals* stands
whitespace-folded in `skills/code-review/orchestration.md` or in
`skills/code-review/gate-to-pull-request.md`. The exceptions are the
section's first paragraph, cut at "committed and unpushed." with its
pointer, row 6 of the exit table, and the exit-1 paragraph reworded at
`e96d743c3` (executed, a folded paragraph comparison of `git show
3c89a70d5:skills/code-review/orchestration.md` against both files). No
moved step (`pr-wait`, `gh pr create`, `--preflight`, `seal stamp`, the
stated limit, `gh api -X PATCH`) remains in the kept file (executed:
`grep`). Each relative pointer in the moved text, "below" and "above",
resolves inside the new file (read). So S5 holds.

What matched: T1 to T14 stand in the tree as `frame/design.md`
*Data & interfaces* gives them (read, each against its file).

What matched: the citations of the kept heading that this work left
standing still mean material under it (read). `CONTRIBUTING.md:36` means
the order of pushing and opening. `docs/forms/the-guarantee.md:22`,
`skills/commit-pr-convention/SKILL.md`, `skills/writing-style/outside-the-review.md`,
`templates/setup/config.md` and both cells of `skills/implement/SKILL.md`
mean what `pr.md` holds. `docs/releasing/branch-and-release.md:290-291` and
`docs/releasing/release-checklist.md:25-26` mean the merge and the rebase
rule. Step 2 of `skills/implement/orchestration.md` means when the pull
request opens. The core's sentence on the four rows being held "by the
orchestrator keeping" the kept section still resolves to a section that
states the rule and points on to the new file for its steps (read).

What matched: a work item routed `straight to the PR` has no round record,
so T2's "once the last round record has no finding open" does not fire for
it. Such an orchestrator reaches the new file through step 2 of
`skills/implement/orchestration.md` and then the kept section's pointer at
`skills/code-review/orchestration.md:240-247`. The drain section already
uses the same phrase as its trigger (read).

What matched: the cases that read what moved pass at the target. That is
363 cases over sixteen modules: G13's, the citation resolver, the paste
check, the wrap, the owner cases and the contract cases (executed:
`bin/test -q` in a clone at the target). This is a narrow run, and the
suite stays `unverified`. The `uncited` clause and the contract-reading
clause of `tests/text/test_a_language_section_of_writing_style_opens_alone.py`
each hold a fact that no other case in the module holds, and phase 1
records each as seen red (read).

What matched: `pr.md` quotes three sentences, and each was found word for
word at its coordinate: the title row of `frame/plan.md` *Judgments of the
run*, and Q1's question and default in `frame/questions.md` (read). It holds
the `Closes` and attribution lines that the kept section says it holds.

What matched: the `straight to the PR` route, the kept merge paragraph, the
drain section's citation and the `pr_wait.py` docstring each name a
section that holds what they cite them for (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the target: the full suite, the repository-wide lint and the format check. This round ran only the narrow modules above, and the suite is `unverified` | `seal/config.json` `Broad gate` | the orchestrator, at the broad run after the rounds settle |
| The merge of `origin/release/v0.38.6` at `f2a664eb8`, where #1577 rewrote `templates/setup/config.md` *Broad gate* and how `skills/verify/scripts/broad_gate.py` reads the command. This branch moved the paragraph *A refusal about the `Broad gate` key* into the new file and edited two comments in `broad_gate.py`, so the merge's resolution in those places was read by nobody | `skills/code-review/gate-to-pull-request.md:222-231`, `skills/verify/scripts/broad_gate.py:476-478`, `skills/verify/scripts/broad_gate.py:2214-2217` | the orchestrator, at the merge, with a verifying round on the resolution where it touches a file outside the records (`skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*) |
| Q1: the release table on the release pull request, after the release's other items merge | `seal/threads/1795398442-per-spawn-files-carry-text-their-reader-never-acts-on/frame/questions.md:16` | whoever prepares the release |

## Probes

| Command | Result |
|---|---|
| `python3 .github/scripts/release_report.py --against v0.38.5 --at <clone at 641b6bfb5>`, from a `git clone --no-local` at the target | preload rows crafter 30,613 (-419), framer 37,028 (-339), proofer 31,379 (-299), sealer 31,909 (-161), tracer 24,191 (-161); exit 0 |
| `bin/test -q` over sixteen modules (the citation resolver, the language case, the contract cases, the core-sentence case, the broad-gate rule, the stamp, the scratch name, the owner cases, `tests/lib/test_config.py`, the wrap, the paste check, the sealer, the broad-gate row, the seal-once case, the probe-commit case, the contract-read case), in the clone | 363 passed, 5 warnings; exit 0 |
| `python3 test_tmp_paste_fold.py <clone>`, run once from the round's scratch directory | the current normaliser finds 1 shared 15-word run between `gate-to-pull-request.md` at `236d3c5e6` and `orchestration.md` at the target, and 0 at the target; with the row name folded into the section token, 0 in both wordings |
| `python3 skills/code-review/scripts/chain_check.py --baseline 3c89a70d5 --root <branch worktree> --worktree`, before this record was written | exit 0; no notice at a line of `frame/design.md` |
| the same command after this record was written, with `--baseline 3c89a70d5` and again with `--baseline origin/release/v0.38.6` | exit 0 both times; the record's refusals are the three open findings, which have no close block; the other lines name the absent `trail/gate.md` and `guarantee.md`, which come later |
