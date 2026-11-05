# Review round 2: 1793843890-the-directory-tracks-a-dist-branch

```seal
target: 37649c32, fixes 34fc7399..37649c32
```

This is the verifying round over round 1's fix pass. The diff read is `git diff d1431e49 37649c32`, less round 1's own record. It holds the orchestrator's fold before the pass (5e0fa2c5), the pass's four commits (60b917be, 5124a6d9, ea2d6cee, 6038444c), the close commit (06959035) and the fold after the pass (37649c32). The review stayed inside that diff and the statements of the facts it changes.

`origin/release/v0.32.3` names `2b72f892`, which is #1375 merged (#1377). The merge base is still `9dd67e2a`. `git merge-tree --write-tree HEAD origin/release/v0.32.3` exits 0. In the round's clone, `git merge --no-commit --no-ff` of that tip staged a clean merge. The census, the release-check, the publish-note, the `dist_branch.py` and the directory-check modules then ended 129 passed, exit 0, over the merged index, and the merge was aborted (executed). So the branch merges clean with the new tip, and #1375's removal of `assets/seals/candidates/` leaves no citation the archive reading refuses.

Carried from round 1 and not re-established: no ruleset reaches `dist`, no workflow starts on a push to `dist`, every `from:` passage of the rule changes stands in its section, and `marketplace.json`'s `source` is `./`. The fix diff touches none of the files those facts rest on except the workflow, whose `on:` block it leaves alone.

The fix pass claimed 82 modules passed, 5059 passed and 14 skipped, exit 0. That run was not repeated. This round ran the eight modules nearest the diff instead (`## Probes`).

## Findings

### 1. The frame's *Removes* paragraph still says the work adds five attribute lines, and `.gitattributes` holds six

```seal
severity: should
location: `seal/threads/1793843890-the-directory-tracks-a-dist-branch/frame/design.md:175`
evidence: read `seal/threads/1793843890-the-directory-tracks-a-dist-branch/frame/design.md:175`, `.gitattributes:16-21`; executed `git grep -n "five attribute\|five lines\|Five lines"` over the worktree
reopens: round-1#1
```

Why it matters: the code part of round 1's close holds. `.gitattributes:21` marks `/.github/workflows/ export-ignore`, and the confirmations below re-run it. What fails is the close's account of the fact's other statements. Contract rule 12 makes the work item's files that state the present a closed set, so a list of them is complete or it is wrong. The close said `frame/design.md` *Data & interfaces* and `frame/plan.md` *Operational impact* "still name five and are the orchestrator's to fold". The fold at 37649c32 changed those two. Neither the close nor the fold reached the last paragraph of `## Removes`, which reads "This work adds a job, a script, a census reading and five attribute lines" (`frame/design.md:175`). Round 1's snippet note, which listed the statements the fix owed, missed the same line, so this round names the method and not only the instance. The search above found no other statement of the count outside the dated *Grounding* row and the phase records, and each of those states the commit it names.

The sealer reads the frame against the tree. A count of five against a file of six lines is a contradiction it has to weigh, and the fix is one word.

```markdown
This work adds a job, a script, a census reading and six attribute lines.
```

## Confirmations

```seal
confirms: round-1#2
```
What holds: the `dist` job's `if:` is `${{ !cancelled() && needs.publish.outputs.tag != '' }}` (`.github/workflows/publish-release.yml:183`). Under it a failed `publish` job no longer skips `dist` by its status alone, which was the finding. The fix pass claimed the changed assertion goes red against the old line. In the round's clone, the old line `if: needs.publish.outputs.tag != ''` was put back with the `Edit` tool, and `test_the_dist_job_adds_the_release_to_dist_and_goes_red_where_it_cannot` failed on that assertion (executed). The fix pass also claimed the form can do no worse than the old line. That holds by reading. `publish` has no `if:` of its own, so it is never skipped (`publish-release.yml:70-109`). Where a failed job's output does not reach `dist`, the tag reads empty and `dist` is skipped, as before. Where the tag step set no tag, the job is skipped as before. The workflow's header comment (`:47-49`), the case's docstring and the changelog fragment now say the job also runs after a failed note step. That holds only if GitHub hands a failed job's outputs to the jobs that need it. GitHub's page on passing job outputs, fetched this round, says nothing about a failed job. `## Not judged` carries the question of those three sentences.

What matched: the fix pass claimed A7, `tests/behaviour/test_a_cited_section_stands_in_its_file.py#test_this_repository_s_archive_holds_no_workflow_file`, is red against the tree without the sixth line. In the round's clone the line was removed with the `Edit` tool and A7 failed. Its message listed `close-issues-on-release.yml`, `hygiene.yml`, `label-merged-on-release-branch.yml`, `publish-release.yml` and `test.yml` (executed). The case reads the working tree's attributes through `archived` (`:236-264`), so an uncommitted removal of the line is seen. That is the reason commit 5124a6d9 moved it out of `tests/github/test_dist_branch.py`. A7 was read against its group. A1 and A2 read the archive's citations, and A3 to A6 read fixtures. None of them asserts what the archive leaves out, so A7 covers something new. It holds a fact *Scope* 1 states.

What matched: the fix pass claimed a dry run over HEAD builds a 182-file tree with nothing under `.github/workflows/`. Round 1's `executed` line for finding 1 was re-run in the round's clone with a scratch tag on 37649c32. `DRY_RUN=1 TAG=vprobe2 python3 .github/scripts/dist_branch.py` exited 0 and printed tree `2b48a756`. `git ls-tree -r --name-only` of that tree listed 182 files. None was under `.github/workflows/`, and 16 were under `.github/scripts/`, so the script `dist` ships with is still there. The list equalled the file entries of `git archive vprobe2 | tar -t` (`diff`, exit 0). The tag was then deleted (executed).

What matched: the statements of the six paths, apart from finding 1. `.gitattributes:3-15`'s comment, `changelog.md`, `frame/design.md` *Scope* 1, *Out* and *Data & interfaces*, `frame/plan.md` *Operational impact*, the census module's docstring (`:49-51`) and `tests/github/test_dist_branch.py`'s docstring each name the workflows as leaving, and each says it as the tree has it (read).

What matched: the new `gaps.md` row for a failed job's outputs names its answerer. The row's quotation of GitHub's documentation is read as a claim and was not re-fetched beyond the one page above.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the three sentences saying `dist` also runs where the note step failed are true. They hold only if GitHub hands a failed job's outputs to its dependents, which `gaps.md` *Not verified* leaves open. The changelog sentence ships in the release note. Hedging the three sentences to that condition costs a clause each. Leaving them stands on the `gaps.md` row. | `.github/workflows/publish-release.yml:47-49`, `tests/behaviour/test_a_release_publishes_its_note.py:195-198`, `seal/threads/1793843890-the-directory-tracks-a-dist-branch/changelog.md:3` | the orchestrator, which decides whether to hedge them or leave them to the `gaps.md` row's answerer |
| The fix pass's 82-module run and its `seal mutate` breaks of the sixth line. Read as claims and not re-run. This round ran eight modules and two seen-red edits. | `seal/threads/1793843890-the-directory-tracks-a-dist-branch/trail/rounds/round-1.md` | the sealer's sample of the crafters' claims |
| The full suite, the repository-wide lint and the format check at HEAD. The suite stays `unverified` here. | the whole tree | the orchestrator's broad run |

## Probes

| Command | Result |
|---|---|
| `git merge-tree --write-tree HEAD origin/release/v0.32.3` in the worktree | exit 0 |
| `bin/test` over `test_a_cited_section_stands_in_its_file.py`, `test_a_release_publishes_its_note.py`, `test_dist_branch.py`, `test_a_shrunken_corpus_declines_to_judge.py`, `test_the_release_check_watches_what_ships.py`, `test_the_release_seal_is_drawn.py`, `test_the_release_tail_does_not_end_at_the_tag.py` and `test_docs_line_wrap.py`, `-q`, in the round's clone at 37649c32 | 174 passed, exit 0 |
| The sixth `.gitattributes` line removed and the old `if:` put back, both with the `Edit` tool, then `bin/test` over the census and publish-note modules, `-q -p no:xdist -k "workflow_file or dist_job"` | 2 failed, exit 1: A7 on its workflow list, the `dist` case on the `if:` assertion. Both files were restored with `git checkout --`. |
| `git merge --no-commit --no-ff` of `2b72f892` in the round's clone, then `bin/test` over the census, release-check, publish-note, `test_dist_branch.py` and `test_plugin_directory_check.py` modules, `-q`, then `git merge --abort` | clean merge; 129 passed, exit 0; aborted, HEAD back at 37649c32 |
| `git tag vprobe2 HEAD`, then `DRY_RUN=1 TAG=vprobe2 python3 .github/scripts/dist_branch.py`, then `git ls-tree -r --name-only` of the printed tree compared with `git archive vprobe2 \| tar -t`'s files | exit 0; 182 files, none under `.github/workflows/`, 16 under `.github/scripts/`; `diff` exit 0; the tag was deleted |
| WebFetch of GitHub's documentation page on passing job outputs between jobs | the page says nothing about a failed job's outputs |
