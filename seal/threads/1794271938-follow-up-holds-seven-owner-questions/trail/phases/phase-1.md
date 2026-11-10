# Phase 1: 1794271938-follow-up-holds-seven-owner-questions

## What this phase found

**The frame holds against the tree.** The frame names `eccf1bcb7`, and `360eb7cc9` changes only the three frame files, so every coordinate it gives still stands. I opened each one this phase builds on: the `ast` reader at `tests/github/test_close_issues_on_release.py:1160-1178`, the sentence at `:1122-1124`, the folded readers at `tests/github/test_release_completeness_check.py:571-574` and `tests/github/test_label_merged_on_release_branch.py:397-408`, and the import of `load` at `tests/github/test_label_merged_on_release_branch.py:30`. The argvs G9 lists are the ones the scripts hold. No coordinate was wrong.

**The folded cases were green against a comment-split plant before the conversion (executed, at `360eb7cc9`).** I ran each plant through `seal mutate`, which restored the script from the bytes it held. Each run read `SURVIVED`, exit 1:

- `release_completeness_check.py#open_in_milestone`: the argv's `"list"` replaced by a comment line and `"edit"`, making `gh issue edit`. `test_the_gate_writes_nothing` passed.
- `release_completeness_check.py#milestone_titles`: the `gh api` argv rewritten as `"gh", "label",  # comment` then `"delete"`. `test_the_gate_writes_nothing` passed.
- `label_merged_on_release_branch.py#add_label`: the argv's `"edit"` replaced by a comment line and `"close"`, making `gh issue close`. `test_the_script_only_ever_creates_a_label_and_adds_one` passed.

**The same plants are red against the converted cases (executed, at `08878411b`).** Each run read `red`, and I read each failing line for the guard it names:

- The `gh issue edit` plant failed at `tests/github/test_release_completeness_check.py:579` with `AssertionError: issue edit`.
- The `gh label delete` plant failed at `:580` with `AssertionError: label delete`.
- The `gh issue close` plant failed the label case on the forbidden-verb loop, with "the script gained `issue close`".
- S2, `"--add-label"` removed from `add_label`'s argv: the label case failed with "the script stopped adding".
- S2, `"create"` removed from `create_label`'s argv: the label case failed with "the script stopped creating".
- The closer's case, which this phase moves and does not change, also went red on a comment-split `gh issue reopen` planted in `close_issues_on_release.py#close_issue`'s REST argv. It failed on the forbidden-verb loop with "the script gained `issue reopen`". S3 needs only its existing red. I ran this one because it costs one command and shows the shared reader serves the closer as it did before.

**`argv_words` is the *Logic* row of `skills/verify/SKILL.md` *The narrow command still has to be able to fail*, not a move.** Its body is the case-local collection and `words`, but it now takes the source text and returns the word lists, so its signature and output changed. I ran three `seal mutate` breaks of it over the three cases (executed, at `08878411b`):

- Without the `ast.Call` half: `red`. The closer's and the label cases fail. The completeness case stays green, because it asserts only absences, and an empty reader satisfies an absence.
- Without the `ast.List` half: `red`. The closer's case fails, because its one `gh issue edit` is a list literal passed to `subprocess.run`.
- Without `isinstance(a.value, str)`: `SURVIVED`. The filter came over unchanged from the case-local `words`. No argv in the three scripts carries a constant that is not a string, so both readings give the same word lists. A case for it would need a source written for the case. *Scope* item 1 asks for none, and `skills/core/SKILL.md` *The rule a mechanism is kept against* weighs a case by what it catches. I left the filter in place and unpinned.

**The completeness case's red depends on the plants.** That case asserts only that verbs are absent. So any break that makes the reader return less, such as an empty list, leaves it green. The mutation table shows this. The plants above are what show its red, and they are the plan row's evidence.

**Two departures from the frame's wording, both inside *Scope* item 1.**

- The closer's case had a comment saying that its reader reads both argv shapes, `run("gh", …)` and `subprocess.run(["gh", …])`, and when that was measured. That comment moved into `argv_words`' docstring together with the paragraph *Removes* names. It describes the collection, and the collection moved. One line stays in the case. It says the case's own `gh issue edit` is the list shape and its close the call shape. Its first wording at `08878411b` said every other argv was call arguments, and the script's REST read in `_issue_api` is a list too; `2705f8d4f` corrects the comment and changes nothing else, so the runs above hold for it. Ground: `frame/design.md` *Removes*, the row for the case-local `words` and argv collection.
- `test_the_gate_writes_nothing` keeps its unused `monkeypatch` parameter. Removing it is a change *Scope* item 1 does not name.

**The other places that state the folded reader or the open escape (a sample).** I ran `git grep` over the tree, outside `seal/threads/`, for `fold`, `folded`, `constant-valued`, `resolving module-level names` and the three case names. One sentence HEAD contradicts stands outside this phase's files: `seal/follow-up.md:48` says the folded reader "still stands in" the two converted cases. Phase 3's *Scope* item 5 removes that row. The search covers an open class of spellings, so the list is a sample. A statement in other words is left to the proofer's reading of the diff.

**For the next phases.** Phase 1 renames no case, so `.test_durations` keeps every key it had.
