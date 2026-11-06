# Phase 6: 1793935041-the-directory-refuses-every-command-hook

## What this phase found

**The frame holds for this phase, and the count is thirteen.** At
`ff955221`, `git ls-files '.github/scripts/'` listed sixteen Python files.
The three that stay are the ones a shipped file loads or runs by path:
`bin/test` and `bin/test.cmd` run `run_tests.py`,
`skills/implement/scripts/seal.py#TOOLS` and
`skills/code-review/scripts/chain_check.py#CHECK_LINES_READER` load
`rules.py`, and `skills/code-review/scripts/pr_body.py` loads
`close_issues_on_release.py`. None of the three imports one of the other
thirteen: `close_issues_on_release.py` puts `hooks/lib/` on its path and
names `tracker_labels.py` and `label_merged_on_release_branch.py` in
comments alone. Every workflow under `.github/workflows/` runs its script
through `actions/checkout`, with no `ref: dist`, and no test reads a
script out of `dist`. `plugin_directory_check.py` compares a pin against
`origin/dist` and is run from the tree.

**One departure from the frame: five shipped citations of a script that
leaves.** `tests/behaviour/test_a_cited_section_stands_in_its_file.py#test_every_cited_name_stands_in_what_the_archive_holds`
reads every `path#name` in a file the archive holds against the files the
archive holds. `docs/releasing/branch-and-release.md` *The plugin directory
reads `dist`* states the rule: a cited file marked `export-ignore` fails
CI. Once the thirteen lines stood, five citations dangled:

- `templates/setup/config.md:467`, `.github/scripts/release_seal.py#mark_on`
- `assets/seals/README.md:184`, `.github/scripts/release_seal.py#draw`
- `docs/checks/the-pull-request-check.md:60`, `.github/scripts/release_seal.py#chain_counts`
- `skills/settle/scripts/settle.py:336`, `.github/scripts/publish_release_note.py#fragments`
- `skills/settle/scripts/settle.py:434`, `.github/scripts/publish_release_note.py#section`

Each now names the release workflow's step that does the work, the `seal`
job of `.github/workflows/publish-release.yml` or the plugin's own publish
workflow, and cites no file. The frame's `## Removes` does not name these
five citations. Keeping a script in `dist` because a sentence cites it
would have put back what the frame takes out for the portal's holds
(`frame/questions.md` Q1). Judged against `skills/core/SKILL.md` *The
rule a mechanism is kept against*: the census holds what it reads, so the
fix is to the citing text, not to the census.

**One guard's floor was lowered.** The same case asserted at least 100
names read. With the thirteen scripts out of the archive, the archive reads
91 names, where the tree reads 263. The floor is now 50, and the docstring
says why. The tree reading's floor of 100 still holds the reader's
matching, in `#test_every_cited_name_stands_in_its_file`. The archive
reading of sections reads 377 citations and its floor is unchanged.

**A case pins which scripts stay, and it is a second statement of the
three.** `#test_this_repository_s_archive_holds_only_the_scripts_a_shipped_command_runs`
reads `git archive` of the index's tree and asserts that, of
`.github/scripts/`, it holds those three and no other, that each file that
runs one is in the archive, and that the `dist` paragraph of
`docs/releasing/branch-and-release.md` names each script with what runs
it. It stands beside the case that holds the archive carries no workflow
file. A fourteenth release-only script added without its line now fails
this case at the pull request, before any Validate.

**`.gitattributes`'s comment was rewritten in place.** It listed the
leaving paths as suites, records, a contributor's files and the workflows.
It now adds the scripts only the workflows run, says why each leaves by
its own line, and cites the release document's paragraph.

**The READMEs' sentence.** `README.md` *Shared or local* and `README.ko.md`
*shared 인가 local 인가* gain one paragraph right under the table of the
three answers. It cites `skills/core/SKILL.md` *Judgment is not licence to
skip a party*, whose closing sentence already says that in local mode the
last four rows are held by `agents/sealer.md` step 1 and the orchestrator.
The Korean edition says it in two sentences and calls the orchestrator
"작업을 이끄는 세션", as the rest of `README.ko.md` names that session.
`tests/behaviour/test_first_setup_asks_once.py#test_the_readme_states_what_local_mode_leaves_unchecked_under_the_table`
pins the paragraph in each edition as the one after the table.

**Path-only mentions of the thirteen in shipped files stand.** `git grep -c`
on the thirteen file names over the paths the archive holds lists
`docs/layout/the-record-layout.md`, `docs/releasing/branch-and-release.md`,
`docs/releasing/issues-and-milestones.md`, `docs/releasing/release-checklist.md`,
`docs/running/what-a-script-gates.md`, `hooks/lib/console.py`,
`skills/code-review/scripts/chain_check.py`, `skills/settle/SKILL.md`,
`skills/settle/scripts/settle.py`, `skills/verify/orchestration.md`,
`skills/verify/scripts/seal_stamp.py` and
`.github/scripts/close_issues_on_release.py`, besides `.gitattributes`.
Each names this repository's file by path, which no census reads, and most
stand in the documents of this repository's own release. A reader of
`dist` finds no such file at those paths. The list is whole for the
thirteen literal file names; `gaps.md` *Not done* carries it.

**Seen red.** Both new cases ran against the tree before the edits:
`#test_this_repository_s_archive_holds_only_the_scripts_a_shipped_command_runs`
failed on its first assertion, listing the sixteen scripts, and both
parameters of the README case failed. After the commits, each `seal
mutate` run below exited 0 with the verdict `red`:

- `.gitattributes` without the `release_seal.py` line, and without the
  `tracker_labels.py` line, against `-k only_the_scripts_a_shipped_command_runs`:
  2 mutants, 2 red.
- `docs/releasing/branch-and-release.md` without `` `bin/test` `` and
  without `` `skills/code-review/scripts/pr_body.py` ``, against the same
  case: 2 mutants, 2 red.
- `README.md` without "alone", and `README.ko.md` without its last
  sentence, against `-k local_mode_leaves_unchecked`: 1 failed each.
- `templates/setup/config.md` with its `release_seal.py#mark_on` citation
  put back, and `skills/settle/scripts/settle.py` with its
  `publish_release_note.py#section` citation put back, against
  `-k cited_name_stands_in_what_the_archive_holds`: 1 failed each, the
  failing line naming the citation.

**The read of the range.** After `bd971897`, the read of every hunk
rewrapped the paragraph of `docs/checks/the-pull-request-check.md` the
edit had left at one long line and the end of the `dist` paragraph, and
added there that CI fails a release-only script with no line of its own
(`86273523`).

**The phase boundary set.** At `86273523`, `git archive HEAD | tar -t`
lists `.github/scripts/close_issues_on_release.py`, `rules.py` and
`run_tests.py`, no other `.github/scripts/*.py`, and no path under
`hooks/` other than `hooks/lib/`. `bin/test
tests/behaviour/test_first_setup_asks_once.py tests/github/test_dist_branch.py`
passed 50, exit 0. `bin/test tests/behaviour/ tests/text/ tests/github/
tests/skills/test_settle.py tests/skills/test_seal.py` passed 2,879 with 9
skipped, exit 0. `seal rules --check` exited 0 over 217 check lines in 69
rule files. `seal layout --check` exited 0 with 132 files read and none
refused. `uvx ruff check` and `uvx ruff format --check` over the three
changed Python files exited 0.
